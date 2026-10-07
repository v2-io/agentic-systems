#!/usr/bin/env python3
"""The givens: orders that exist before any mind answers (Joseph, 2026-10-06).

A given is a set of glyphs of one stylistic class (one dress) carrying a known total order: an alphabet in its
language's lexical order, or numbers in numeric value. It is "ready to use" by design, so a window of it, its reverse,
a rotation (cycling), a reflection, or a regular n-step stride are all implied by the order, not found by a mind
(Joseph: *"contiguous, have a known canonical lexical ordering, known total order, same stylistic class ... implies a
'ready to use' sequence by design, with shifting, mirroring, and cycling all implied, probably as well as regular
n-step sequences"*). Every given here comes from Unicode's own data, nothing hand-listed:

  alphabets  CLDR's standard exemplar letters for each language (ICU), ordered by that language's collation. Two
             readings of membership, both kept: "letters" (every exemplar letter, in full sort order: Russian е ё ж)
             and "base" (the letters collation treats as distinct at primary strength, the rest as forms of them:
             Spanish á is a form of a, ñ is its own letter). Upper case from ICU's case mapping, per language.
  numbers    every character with a Unicode numeric value, grouped by dress (its name with the number words removed,
             DIGIT/NUMBER unified, plus its compatibility tag), ordered by value: ASCII digits, each script's
             digits, circled 1-50 across three blocks, Roman numerals, vulgar fractions, superscripts.
  dresses    every character whose compatibility decomposition is a single letter (or, for the dresses Unicode leaves
             undecomposed -- negative circled/squared, regional indicators, tags -- whose name names one) is that
             letter in a dress: its name with the letter, script, LETTER and MATHEMATICAL removed, plus the
             compatibility tag. The holes Unicode left in the Mathematical Alphanumeric block are filled from
             NamesList's own cross-references (reserved 1D455 -> 210E PLANCK CONSTANT), so ℭ and ℎ join their sets.

Only characters assigned in this Python's Unicode (16.0) are kept; ICU's data may be newer, and its versions are
recorded. Output: data/unicode/givens.json (deterministic; committed, so the catalog build needs no ICU).
Run with the study's ICU environment: .venv-icu/bin/python catalog/givens.py
"""
import collections, hashlib, json, pathlib, re, sys, unicodedata as U

import icu

ROOT = pathlib.Path(__file__).resolve().parents[1]
UNI = ROOT / "data" / "unicode"
OUT = UNI / "givens.json"
MIN_POSITIONS = 3          # a given shorter than this can't hold a run of 3 (chosen without evidence)
EXCLUDED_SCRIPTS = {"Hani"}  # Han: no ordering intrinsic to the set -- its collation is a convention (pinyin,
                             # stroke, radical) that differs by locale. Every other script's letters have a standard
                             # enumeration, syllabaries and Hangul syllables included. A decision, with that reason.

def assigned(ch):
    return U.name(ch, None) is not None

# ------------------------------------------------------------------ dresses of letters
SCRIPT_WORDS = {"LATIN", "GREEK", "CYRILLIC", "COPTIC", "ARMENIAN", "GEORGIAN", "HEBREW", "ARABIC"}
DROP = {"LETTER", "MATHEMATICAL", "MODIFIER", "SUPERSCRIPT", "SUBSCRIPT"} | SCRIPT_WORDS
ALIAS = {"BLACK-LETTER": "FRAKTUR"}

def tag_of(ch):
    d = U.decomposition(ch)
    return d.split(" ")[0] if d.startswith("<") else ""

def letter_tokens(base):
    n = U.name(base, "")
    return n.split(" LETTER ", 1)[1].split() if " LETTER " in n else n.split()[-1:]

def dress_key(ch, base):
    words = U.name(ch, "").split()
    tail = letter_tokens(base)
    if tail and words[-len(tail):] == tail:
        words = words[:-len(tail)]
    words = [ALIAS.get(w, w) for w in words if w not in DROP]
    k = " ".join(words) or "plain"
    t = tag_of(ch)
    return (t + " " + k).strip() if t else k

UNDECOMPOSED = re.compile(r"^(NEGATIVE CIRCLED|NEGATIVE SQUARED|TAG|REGIONAL INDICATOR SYMBOL)( LATIN)?( CAPITAL| SMALL)? LETTER ([A-Z])$")

def dress_index():
    """-> {glyph: (base letter, dress)} for every assigned letter-like glyph that is a single letter in a dress"""
    idx = {}
    for cp in range(sys.maxunicode + 1):
        ch = chr(cp)
        if not assigned(ch):
            continue
        f = U.normalize("NFKC", ch)
        if len(f) == 1 and f != ch and U.category(f).startswith("L"):
            idx[ch] = (f, dress_key(ch, f))
            continue
        m = UNDECOMPOSED.match(U.name(ch))
        if m:
            case = (m.group(3) or " CAPITAL").strip()
            base = U.lookup(f"LATIN {case} LETTER {m.group(4)}")
            idx[ch] = (base, f"{m.group(1)} {case}")
    # holes in the Mathematical Alphanumeric block: NamesList's cross-reference names the character that serves
    hole, fill = None, {}
    for l in open(UNI / "NamesList-16.0.0.txt", encoding="utf-8"):
        m = re.match(r"^([0-9A-F]{4,6})\t<reserved>", l)
        if m:
            hole = int(m.group(1), 16); continue
        m = re.match(r"^\tx \(.* - ([0-9A-F]{4,6})\)", l)
        if m and hole is not None and 0x1D400 <= hole <= 0x1D7FF:
            fill[chr(int(m.group(1), 16))] = hole
        if not l.startswith("\t"):
            hole = None if not re.match(r"^([0-9A-F]{4,6})\t<reserved>", l) else hole
    for ch, h in fill.items():
        if ch not in idx:
            continue
        nb = chr(h + 1) if assigned(chr(h + 1)) else chr(h - 1)
        if nb in idx:
            idx[ch] = (idx[ch][0], idx[nb][1])
    return idx

# ------------------------------------------------------------------ alphabets
def alphabets():
    ids = set()
    for l in icu.Locale.getAvailableLocales().keys():
        loc = icu.Locale(l)
        ids.add(loc.getLanguage() + ("_" + loc.getScript() if loc.getScript() else ""))
    out = collections.defaultdict(lambda: {"languages": []})
    for lg in sorted(ids):
        try:
            s = icu.LocaleData(lg).getExemplarSet(0, icu.ULocaleDataExemplarSetType.ES_STANDARD)
        except icu.ICUError:
            continue
        by_script = collections.defaultdict(list)          # a language's letters, split by script (Japanese: kana, kanji)
        for x in s:
            if len(x) == 1 and assigned(x) and U.category(x).startswith("L"):
                by_script[icu.Script.getScript(x).getShortName()].append(x)
        for sc, letters in sorted(by_script.items()):
            if sc in EXCLUDED_SCRIPTS or len(letters) < MIN_POSITIONS:
                continue
            add_alphabet(out, lg, sc, letters)
    return list(out.values())

def add_alphabet(out, lg, sc, letters):
        loc = icu.Locale(lg)
        col = icu.Collator.createInstance(loc)
        letters.sort(key=lambda x: (col.getSortKey(x), x))
        prim = icu.Collator.createInstance(loc); prim.setStrength(icu.Collator.PRIMARY)
        base = []                                   # primary-equivalence classes, in order
        for x in letters:
            if base and prim.compare(base[-1][0], x) == 0:
                base[-1].append(x)
            else:
                base.append([x])
        caseless = all(str(icu.UnicodeString(x).toUpper(loc)) == x for x in letters)   # Hebrew, kana, Ethiopic...
        for case in (("none",) if caseless else ("lower", "upper")):
            def cased(x):
                return str(icu.UnicodeString(x).toUpper(loc)) if case == "upper" else x
            L = [cased(x) for x in letters]
            B = [[cased(x) for x in cls] for cls in base]
            if any(len(x) != 1 or not assigned(x) for x in L):     # e.g. ß has no single-letter capital
                L = [x for x in L if len(x) == 1 and assigned(x)]
                B = [[x for x in cls if len(x) == 1 and assigned(x)] for cls in B]
                B = [cls for cls in B if cls]
            for reading, pos in (("letters", [[x] for x in L]), ("base", B)):
                key = json.dumps([reading, pos], ensure_ascii=False)
                out[key].update(kind="alphabet", reading=reading, case=case, script=sc, positions=pos)
                out[key]["languages"].append(lg)

# ------------------------------------------------------------------ numbers
NUMBER_WORDS = set("""ZERO ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN ELEVEN TWELVE THIRTEEN FOURTEEN FIFTEEN
SIXTEEN SEVENTEEN EIGHTEEN NINETEEN TWENTY THIRTY FORTY FIFTY SIXTY SEVENTY EIGHTY NINETY HUNDRED THOUSAND MILLION
HALF HALVES THIRD THIRDS QUARTER QUARTERS FIFTH FIFTHS SIXTH SIXTHS SEVENTH SEVENTHS EIGHTH EIGHTHS NINTH NINTHS TENTH
TENTHS""".split())

def numbers():
    groups = collections.defaultdict(lambda: collections.defaultdict(list))
    for cp in range(sys.maxunicode + 1):
        ch = chr(cp)
        if not assigned(ch):
            continue
        v = U.numeric(ch, None)
        if v is None:
            continue
        n = U.name(ch)
        if n.startswith("CJK UNIFIED IDEOGRAPH") or n.startswith("CJK COMPATIBILITY IDEOGRAPH"):
            dress = "CJK ideograph numerals"
        else:
            words = [w for w in re.split(r"[ -]", n) if w not in NUMBER_WORDS]
            words = ["N" if w in ("DIGIT", "NUMBER") else w for w in words]
            dress = " ".join(words)
            t = tag_of(ch)
            if t:
                dress = t + " " + dress
        groups[dress][v].append(ch)
    out = []
    for dress, byv in sorted(groups.items()):
        vals = sorted(byv)
        if len(vals) < MIN_POSITIONS:
            continue
        out.append({"kind": "number", "dress": dress, "values": vals,
                    "positions": [sorted(byv[v]) for v in vals]})
    return out

def main():
    idx = dress_index()
    al = alphabets()
    nu = numbers()
    givens = []
    for g in sorted(al, key=lambda g: (g["reading"], g["case"], json.dumps(g["positions"], ensure_ascii=False))):
        gid = "A" + hashlib.sha256(json.dumps([g["reading"], g["positions"]], ensure_ascii=False).encode()).hexdigest()[:10]
        givens.append(dict(id=gid, **g))
    for g in nu:
        gid = "N" + hashlib.sha256(json.dumps([g["dress"], g["values"]]).encode()).hexdigest()[:10]
        givens.append(dict(id=gid, **g))
    doc = {"what": "the givens (catalog/givens.py): orders that exist before any mind answers",
           "unicode_python": U.unidata_version, "icu": icu.ICU_VERSION, "icu_unicode": icu.UNICODE_VERSION,
           "pyicu": icu.VERSION, "min_positions": MIN_POSITIONS,
           "namelist_sha256": hashlib.sha256((UNI / "NamesList-16.0.0.txt").read_bytes()).hexdigest(),
           "givens": givens,
           "dress": {ch: list(v) for ch, v in sorted(idx.items())}}
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=0, sort_keys=True))
    c = collections.Counter((g["kind"], g.get("reading"), g.get("case")) for g in givens)
    print(f"givens.json: {len(givens)} givens {dict(c)}; {len(idx)} dressed glyphs; {OUT.stat().st_size // 1024} KB")

if __name__ == "__main__":
    main()
