#!/usr/bin/env python3
"""Pass-1 migration of grok-1.md -> extracted/grok-1.jsonl.

DELTA LOG
- v0.8 build (2026-08-25): 388 records, structural parser + manual routing.
- verifier round (same day): revises -> v0.9 list-of-objects shape; ~33 pane-walk
  "(denoted)" records basis-corrected to semantic-knowledge; 7 arcs added/fixed;
  header-tail strength bug (L1115); 16 letter-size ladders individuated; span warts.
- adjudication round (same day): morph type ADOPTED; render_dependence on the Cree
  saga records; basis_verbatim carrying grok's own "(denoted)"/"(pictorial)" tags;
  touched records bumped to schema_version 0.9. Final: 405 records, 18 revision links.

Structural parser + per-span judgment overrides. The survey file is read-only.
Spans: "L{a}-L{b}" for whole-subsection records; "L{n}" for records keyed to a
single glyph line inside a multi-sequence subsection (note_verbatim still
carries the whole subsection). Ids: sha256("survey-rec|grok-1|"+span)[:16].
"""
import hashlib, json, re, sys

SRC = "/Users/josephwecker-v2/src/arch/asf/empirica/glyph-magnitude-perception/data/surveys-v1/grok-1.md"
OUT = "/Users/josephwecker-v2/src/arch/asf/empirica/glyph-magnitude-perception/data/surveys-v1/extracted/grok-1.jsonl"

raw = open(SRC, encoding="utf-8").read().split("\n")
L = lambda i: raw[i-1]  # 1-indexed
N = len(raw)

records = []
unhandled = []  # (span, text) prose blocks the parser didn't route

def rid(span):
    return hashlib.sha256(("survey-rec|grok-1|" + span).encode()).hexdigest()[:16]

def cps(glyphs):
    if glyphs is None:
        return None
    g = glyphs.replace("`", "")
    # expand simple non-ASCII ranges "X–Y"
    m = re.fullmatch(r"(.)–(.)", g)
    if m and ord(m.group(1)) > 127 and ord(m.group(2)) > 127:
        a, b = ord(m.group(1)), ord(m.group(2))
        if 0 < b - a <= 40:
            return ["U+%04X" % c for c in range(a, b + 1)]
    return ["U+%04X" % ord(c) for c in g if c not in " \t"]

def add(span, rtype, title, glyphs, strength, note, section, basis="perceived-directly",
        lineage="unprompted", constructed=False, confidence="clear", mnotes=None,
        direction=None, axis=None, negative_kind=None, extra=None):
    rec = {
        "id": rid(span),
        "schema_version": "0.8",
        "record_type": rtype,
        "surveyor": "grok-1",
        "id_recipe": "sha256('survey-rec|grok-1|' + source_span)[:16]; source_span is L<line> or L<a>-L<b>, letter fragments for multi-record lines",
        "source_file": "grok-1.md",
        "source_span": span,
        "section_path": section,          # PROPOSED FIELD: his header taxonomy, verbatim
        "title": title,
        "glyphs": glyphs,
        "codepoints": cps(glyphs),
        "axis": axis if axis is not None else title,
        "direction_note": direction,
        "epistemic_class": "interactive-guided-survey-anecdote",
        "felt_strength_verbatim": strength if strength else "unstated",
        "basis": basis,
        "lineage": lineage,
        "constructed": constructed,
        "note_verbatim": note,
        "transcription_confidence": confidence,
        "migrator_notes": mnotes,
        "open": None,
    }
    if negative_kind:
        rec["negative_kind"] = negative_kind
    if extra:
        rec.update(extra)
    records.append(rec)

def is_glyph_line(s):
    s = s.strip()
    if not s or s.startswith("#"):
        return False
    if s.startswith("- ") and "**" in s:
        return False
    words = re.findall(r"[A-Za-z]{2,}", s)
    return len(words) == 0

# ---- collect blocks with heading context ----
h2 = h3 = h4 = None
i = 1
blocks = []  # (start, end, [lines], h2, h3, h4)
while i <= N:
    line = L(i)
    if line.startswith("# ") and not line.startswith("## "):
        i += 1; continue
    if line.startswith("## ") and not line.startswith("###"):
        h2, h3, h4 = line[3:].strip(), None, None; i += 1; continue
    if line.startswith("### "):
        h3, h4 = line[4:].strip(), None
        blocks.append((i, i, ["### " + h3], h2, h3, h4)); i += 1; continue
    if line.startswith("#### "):
        h4 = line[5:].strip()
        blocks.append((i, i, ["#### " + h4], h2, h3, h4)); i += 1; continue
    if line.strip() in ("", "---"):
        i += 1; continue
    j = i
    buf = []
    while j <= N and L(j).strip() not in ("",) and not L(j).startswith("#"):
        buf.append(L(j)); j += 1
    blocks.append((i, j - 1, buf, h2, h3, h4))
    i = j

# ---- overrides / manual routing -------------------------------------------
MANUAL_SPANS = set()   # spans consumed by manual records below
SKIP_SPANS = set()     # deliberately skipped ("Already had" bookkeeping)
GLYPH_OVERRIDE = {}    # span -> glyphs (for records whose glyphs sit in prose)
FIELD_OVERRIDE = {}    # span -> dict of field updates

def parse_bullet(ln, span, section, lineage):
    m = re.match(r"- \*\*(.+?)( — (.+?))?:\*\* ?(.*)", L(ln))
    if not m:
        return False
    title, strength, rest = m.group(1), m.group(3), m.group(4)
    bt = re.findall(r"`([^`]+)`", rest)
    glyphs = None
    if bt:
        # join adjacent backtick groups forming a range `A`–`B`
        rng = re.match(r"\s*`[^`]+`–`[^`]+`", rest)
        glyphs = re.sub(r"`", "", re.match(r"\s*(`[^`]+`(?:–`[^`]+`)?)", rest).group(1)) if re.match(r"\s*`", rest) else bt[0]
    direction = None
    dm = re.search(r"—", title)
    if "→" in title:
        direction = title
    add(span, "sequence", title, glyphs, strength, L(ln), section,
        lineage=lineage, direction=direction,
        mnotes=None if glyphs else "glyphs not fenced in source; see note_verbatim",
        confidence="clear" if glyphs else "interpreted")
    return True

# ---------------------------------------------------------------------------
for (a, b, buf, h2s, h3s, h4s) in blocks:
    span = f"L{a}-L{b}" if b > a else f"L{a}"
    if buf[0].startswith("#"):
        continue  # headings handled via context
    section = [x for x in (h2s, h3s, h4s) if x]
    text = "\n".join(buf)
    # route below by manual tables first
    if span in MANUAL_SPANS or span in SKIP_SPANS:
        continue
    unhandled.append((a, b, buf, section, span))

# The generic pass above only gathers; real routing happens here with full
# knowledge of the file. We now walk `unhandled` and route each block.
routed = []
pending = unhandled
unhandled = []

STEERED_FROM = 1015  # "## morphs" — post-Joseph-challenge section
def lin(a):
    return "steered" if a >= STEERED_FROM else "unprompted"

MORPH_NOTE = ("record_type 'morph' (adopted, schema v0.9): an ordering answered by "
              "what-comes-next-if-I-keep-doing-that, not pairwise more-ness")

# subsection assembly: group consecutive blocks under same h3/h4 for sections 1-4 & morphs
STD_H2 = ("pictorial — the shape *is* the amount", "size of a same primitive",
          "denoted number — I read the amount", "time / phase (emoji; still Unicode)",
          "morphs — one shape becoming another (cross-pane)")

subsections = {}
order = []
for (a, b, buf, section, span) in pending:
    key = tuple(section)
    if key not in subsections:
        subsections[key] = []
        order.append(key)
    subsections[key].append((a, b, buf, span))

def header_strength(h):
    if h and " — " in h:
        return h.rsplit(" — ", 1)
    return (h, None)

for key in order:
    section = list(key)
    chunks = subsections[key]
    h2s = section[0] if section else None
    leaf = section[-1] if section else None
    first_a = chunks[0][0]; last_b = chunks[-1][1]
    whole = "\n\n".join("\n".join(c[2]) for c in chunks)
    span_all = f"L{first_a}-L{last_b}"

    if h2s in STD_H2 and leaf != h2s:
        title, strength = header_strength(leaf)
        glyph_lines = [(a2 + k, ln) for (a2, b2, buf2, sp) in chunks
                       for k, ln in enumerate(buf2) if is_glyph_line(ln)]
        morph = h2s == STD_H2[4]
        rtype = "morph" if morph else "sequence"
        basis = "semantic-knowledge" if (h2s == STD_H2[2] or (strength and "denoted" in strength)) else "perceived-directly"
        mnotes = MORPH_NOTE if morph else None
        if morph and strength is None:
            im = re.search(r"(Strong|Medium–strong|Medium|Weak)[.,]", whole)
            strength = im.group(1).lower() if im else None
        if len(glyph_lines) <= 1:
            g = glyph_lines[0][1].strip() if glyph_lines else None
            add(span_all, rtype, title, g, strength, whole, section,
                basis=basis, lineage=lin(first_a), mnotes=mnotes,
                confidence="clear" if g else "interpreted")
        else:
            for (gl, ln) in glyph_lines:
                add(f"L{gl}", rtype, title, ln.strip(), strength, whole, section,
                    basis=basis, lineage=lin(first_a),
                    mnotes=((mnotes + "; " if mnotes else "") +
                            "one of %d sequence lines under this header; note_verbatim is the whole subsection" % len(glyph_lines)))
        continue

    # from-panes bullets & prose
    for (a, b, buf, span) in chunks:
        if buf[0].lstrip().startswith("- "):
            # bullet paragraph(s): one bullet per line normally
            ln = a
            for k, s in enumerate(buf):
                sp = f"L{a+k}"
                if s.lstrip().startswith("- "):
                    if not parse_bullet(a + k, sp, section, lin(a)):
                        unhandled.append((a + k, a + k, [s], section, sp))
            continue
        t = "\n".join(buf)
        if re.match(r"Looked", t):
            add(span, "negative", (leaf or "") + " (block, looked)", None, "unstated", t,
                section, negative_kind="verified-absent", lineage=lin(a),
                axis="not an amount (block-level)",
                mnotes="block-level negative: surveyor dumped/looked at the block and found no magnitude scale")
            continue
        if re.match(r"Already had", t) and "Nothing else" not in t and "Missed" not in t and len(t) < 200:
            SKIP_SPANS.add(span)  # dedup bookkeeping only
            continue
        unhandled.append((a, b, buf, section, span))

# ---- manual routing of judgment blocks --------------------------------------
# span -> spec. skip=True: consciously not a record (bookkeeping); reported.
GREP_HAZARD = "surveyor's own confession of the name-derived hazard (grepped names for NUMBER, 'that was the stop')"
M = {
 "L3":  dict(rtype="meta", title="survey scope statement", axis="method"),
 "L5":  dict(rtype="meta", title="surveyor's own definitions of 'more' and 'strength'", axis="method"),
 "L7":  dict(rtype="meta", title="pane-dump method + append-only discipline", axis="method"),
 "L185": dict(rtype="meta", title="denoted number — section law", axis="denoted number orders without ink",
              mnotes="section-level basis statement: applies to all records under this H2"),
 "L277": dict(rtype="negative", title="Whole bagua", glyphs="☰☱☲☳☴☵☶☷", negative_kind="verified-absent"),
 "L278": dict(rtype="negative", title="Whole braille block", negative_kind="verified-absent"),
 "L279": dict(rtype="negative", title="♩♪♫♬ two axes fight", glyphs="♩♪♫♬", negative_kind="verified-absent",
              mnotes="revised later at L516-519 (Musical Symbols: 'the real duration ladder')"),
 "L280": dict(rtype="negative", title="script decimal runs, weaker instinctive punch", negative_kind="not-felt",
              basis="semantic-knowledge"),
 "L281": dict(rtype="negative", title="Yijing hexagrams (King Wen)", negative_kind="verified-absent"),
 "L282": dict(rtype="negative", title="Box-drawing ─ vs ━", glyphs="─━", negative_kind="not-felt",
              mnotes="partially revised at L433-437 (dash-fragment count-scale found; weight verdict stands)"),
 "L283": dict(rtype="negative", title="☹☺☻ not amount", glyphs="☹☺☻", negative_kind="verified-absent"),
 "L289": dict(rtype="meta", title="from panes — method note", axis="method"),
 "L401": dict(rtype="meta", title="Geometric Shapes Extended is designed as ramps", axis="block-level law",
              extra={"predicted_generalization": None}),
 "L433": dict(rtype="meta", title="Box Drawing — standing by the ─/━ weight verdict", axis="revision note"),
 "L458": dict(rtype="meta", title="Supplemental Arrows-C — designed ramps", axis="block-level law"),
 "L516": dict(rtype="meta", title="Musical Symbols revises the ♩♪♫♬ rejection", axis="revision note"),
 "L548": dict(rtype="negative", title="Legacy Computing sextants — bitmask", negative_kind="verified-absent"),
 "L582": dict(rtype="negative", title="Latin-1 Supplement — nothing else is a scale", negative_kind="verified-absent"),
 "L588": dict(rtype="sequence", title="Arabic digit runs", glyphs=None, strength="Denoted; weaker for me than ASCII",
              basis="semantic-knowledge", confidence="interpreted",
              mnotes="two runs ٠-٩ and ۰-۹; strength phrase kept verbatim from bullet"),
 "L603": dict(rtype="sequence", title="ogham across (second aicme)", glyphs="ᚆ–ᚊ", strength="unstated",
              mnotes="strength unstated on the line; L607 says 'Same count-feel as the first aicme' (first aicme was strong)"),
 "L604": dict(rtype="sequence", title="ogham along (the vowels)", glyphs="ᚐ–ᚔ", strength="unstated",
              mnotes="see L607 context: same count-feel as first aicme"),
 "L605": dict(rtype="sequence", title="ogham forfeda", glyphs="ᚕ–ᚙ", strength="unstated",
              mnotes="see L607 context: same count-feel as first aicme"),
 "L607": dict(rtype="negative", title="Ogham is not one 20-letter magnitude line", negative_kind="verified-absent"),
 "L622": dict(rtype="sequence", title="Tamil digits 0–9", strength="medium (denoted)", basis="semantic-knowledge",
              mnotes="glyphs not shown in source"),
 "L627": dict(rtype="sequence", title="Tibetan digits 0–9", strength="medium (denoted)", basis="semantic-knowledge",
              mnotes="glyphs not shown in source"),
 "L640": dict(rtype="meta", title="Block Elements — what was missed from the actual 32", axis="method/self-correction"),
 "L648": dict(rtype="meta", title="Braille — earlier fill line skipped seven", axis="method/self-correction"),
 "L655": dict(rtype="meta", title="Enclosed Alphanumerics — earlier runs confirmed complete", axis="confirmation"),
 "L657": dict(skip=True),
 "L660": dict(rtype="negative", title="circled/parenthesized letters are not amounts", negative_kind="verified-absent"),
 "L664": dict(rtype="meta", title="script decimal 0–9 — same denoted kind; prediction over remaining Nd runs",
              basis="semantic-knowledge",
              extra={"predicted_generalization": "The other Indic/SE Asian Nd runs will be this again."}),
 "L668": dict(skip=True),
 "L672": dict(rtype="sequence", title="Mayan Numerals 0–19", glyphs="𝋠𝋡𝋢𝋣𝋤𝋥𝋦𝋧𝋨𝋩𝋪𝋫𝋬𝋭𝋮𝋯𝋰𝋱𝋲𝋳",
              strength="strong (pictorial)", note_extra="L674"),
 "L674": dict(skip=True),
 "L678": dict(rtype="sequence", title="Cuneiform Numbers 2–9 ASH", glyphs="𒐀𒐁𒐂𒐃𒐄𒐅𒐆𒐇",
              strength="strong (wedge count)", note_extra="L680"),
 "L680": dict(skip=True),
 "L682": dict(rtype="sequence", title="Cuneiform punctuation, diagonal dots", glyphs="𒑲𒑳𒑴", strength="strong"),
 "L686-L687": dict(multi=[
     dict(span="L686", rtype="sequence", title="Ideographic Description across, 2→3 slots", glyphs="⿰⿲", strength="strong (slot count)"),
     dict(span="L687", rtype="sequence", title="Ideographic Description stacked, 2→3 slots", glyphs="⿱⿳", strength="strong (slot count)")]),
 "L689": dict(rtype="negative", title="IDC surround operators — kinds, not more/less", glyphs="⿴⿵⿶⿷⿸⿹⿺⿻",
              negative_kind="verified-absent"),
 "L693-L694": dict(rtype="sequence", title="Common Indic / Oriya / Malayalam fractions", glyphs=None,
                   strength="strong (same two runs as Number Forms)", confidence="interpreted",
                   mnotes="six short runs in two rows (¼½¾ and 1/16,1/8,3/16 across three scripts); kept whole because he frames them as 'the same two runs', not new sequences"),
 "L696": dict(rtype="sequence", title="Malayalam 10, 100, 1000", glyphs="൰൱൲", strength="unstated",
              mnotes="'twin of Tamil ௰௱௲' (that record is strong (denoted))", basis="semantic-knowledge"),
 "L706": dict(skip=True),
 "L708": dict(rtype="sequence", title="Brahmi numbers 1–3", glyphs="𑁒𑁓𑁔", strength="strong (pictorial, then denoted)"),
 "L709": dict(rtype="sequence", title="Kharoshthi 1–3", glyphs="𐩀𐩁𐩂", strength="strong (pictorial, then denoted)"),
 "L710": dict(rtype="sequence", title="Imperial Aramaic 1–3", glyphs="𐡘𐡙𐡚", strength="strong (pictorial, then denoted)"),
 "L711": dict(rtype="sequence", title="Phoenician 1, 2, 3", glyphs="𐤖𐤚𐤛", strength="strong (pictorial, then denoted)",
              mnotes="surveyor notes cps not in order"),
 "L712": dict(rtype="sequence", title="Palmyrene 1–4 strokes", glyphs="𐡹𐡺𐡻𐡼", strength="strong (pictorial, then denoted)"),
 "L713": dict(rtype="sequence", title="Old Persian 1–2 wedges", glyphs="𐏑𐏒", strength="strong (pictorial, then denoted)"),
 "L717": dict(rtype="generator", title="Aegean-shaped denoted inventories", strength="medium, not a new kind",
              basis="semantic-knowledge",
              extra={"rule": "each is 1–9 then 10–90 then 100–900 (or powers of 10); same denoted shape as Aegean/Ethiopic",
                     "examples": ["Rumi","Coptic Epact","Sinhala Archaic","Brahmi tens/hundreds","Indic Siyaq","Ottoman Siyaq","Warang Citi","Meroitic Cursive","Pahawh Hmong powers","Mende Kikakui combining powers"]},
              mnotes="surveyor explicitly declines to list every script — rule-level record"),
 "L725": dict(rtype="negative", title="Yijing hexagrams confirmed not magnitude; ䷀䷁ is a pair", glyphs="䷀䷁",
              negative_kind="verified-absent"),
 "L731": dict(rtype="negative", title="🪆 means nestedness but is a singleton", glyphs="🪆", negative_kind="verified-absent"),
 "L733": dict(rtype="meta", title="dump is Unicode 14.0.0; Kaktovik / neumes / SignWriting not covered", axis="coverage"),
 "L737": dict(rtype="meta", title="musical neumes — blocks are catalogs; a few runs punch", axis="block-level law"),
 "L753": dict(rtype="negative", title="agogi tempi — read the names, glyphs not a ramp", glyphs="𝂚–𝂡",
              negative_kind="verified-absent", basis="name-derived"),
 "L754": dict(rtype="negative", title="Martyria modes — catalog", negative_kind="verified-absent"),
 "L755": dict(rtype="negative", title="Fthora / chroa / arktiko — not more/less", negative_kind="verified-absent"),
 "L759": dict(rtype="negative", title="Alypian pitch inventory — catalog indices, not amounts", negative_kind="verified-absent"),
 "L765": dict(rtype="meta", title="Znamenny — neumes are a catalog; height and brightness punch", axis="block-level law"),
 "L774": dict(rtype="meta", title="SignWriting undumped; Kaktovik wants Unicode 15", axis="coverage"),
 "L778": dict(rtype="meta", title="BMP census: 164 blocks; letter inventories skipped on purpose", axis="coverage"),
 "L794": dict(rtype="negative", title="Kangxi/CJK radicals, strokes, Yi radicals, presentation twins, remaining Nd — not amount",
              negative_kind="verified-absent",
              mnotes="mixed evidence basis: 'looked at names / samples, not dumped as full panes'"),
 "L796": dict(rtype="meta", title="BMP coverage honesty: not 'gone through' only in the letter-inventory sense", axis="coverage"),
 "L800": dict(rtype="meta", title="grep-for-NUMBER was the stop — looking at shapes instead", axis="method/self-correction",
              mnotes=GREP_HAZARD),
 "L804": dict(rtype="generator", title="size of one letter (small → big)", strength="Strong",
              extra={"rule": "The same body in a bigger cell. Each line is its own sequence. Tiny raised (ªº) at the front; subscript another front; small-cap between small and capital.",
                     "examples": ["ₒ o ᴏ O","ₐ a ᴀ A","ₑ e ᴇ E","ᵢ i ɪ I","ᵤ u ᴜ U","ₙ n ɴ N","ₘ m ᴍ M","ₗ l ʟ L","ₕ h ʜ H","ₚ p ᴘ P","ₜ t ᴛ T","ₛ s S","ₓ x X","ᵒ o O","ª a A","º o O"]},
              lines=(804, 825)),
 "L806-L821": dict(skip=True), "L823": dict(skip=True),
 "L827-L839": dict(split_lines=True),
 "L841": dict(rtype="sequence", title="spacing dots ˙ ¨", glyphs="˙¨", strength="unstated", confidence="interpreted",
              mnotes="glyph order assembled by migrator from prose ('¨ is two; ˙ is one. Completes ̇̈ as spacing')"),
 "L845-L851": dict(split_lines=True),
 "L855-L863": dict(split_lines=True),
 "L867": dict(skip=True),
 "L869": dict(rtype="negative", title="o-shapes: would not put all on one line", glyphs="°º ₒoᴏO ɵɔɶʘⱺ",
              negative_kind="verified-absent", note_extra="L867",
              mnotes="the caveat record; the five separate axes are L871-L875"),
 "L871": dict(rtype="sequence", title="o size", glyphs="ₒ o ᴏ O", strength="unstated",
              mnotes="'and º at the very front'"),
 "L872": dict(rtype="sequence", title="o interior bar (less hole)", glyphs="ɵo", strength="unstated",
              mnotes="order by migrator from 'ɵ vs o (less hole)'", confidence="interpreted"),
 "L873": dict(rtype="sequence", title="o aperture (more open)", glyphs="oɔ", strength="unstated"),
 "L874": dict(rtype="sequence", title="two-o (more o)", glyphs="oɶ", strength="unstated"),
 "L875": dict(rtype="sequence", title="o nested", glyphs="oʘ", strength="unstated",
              mnotes="second chain o ⱺ (ring inside o) in note"),
 "L879": dict(rtype="negative", title="turned letters, ligatures, Vietnamese precomposed piles — not a scale",
              negative_kind="verified-absent"),
 "L883": dict(rtype="meta", title="walk plan: remaining missed BMP panes to CJK Radicals Supplement", axis="coverage"),
 "L887": dict(rtype="sequence", title="Hangul ssang doubling", glyphs="ᄀᄁ ᄃᄄ ᄇᄈ ᄉᄊ ᄌᄍ", strength="Strong",
              mnotes="five pairs plus batchim twins ᆨᆩ ᆺᆻ; one record because he states them as one move"),
 "L889": dict(rtype="sequence", title="Hangul clusters as count-of-pieces", strength="weaker than ssang",
              confidence="interpreted", mnotes="'I feel count-of-pieces the way I feel ⿰ vs ⿲, weaker than ssang'"),
 "L891": dict(rtype="negative", title="Hangul fused vowels — catalog of which two", negative_kind="verified-absent"),
 "L895": dict(skip=True),
 "L897": dict(rtype="sequence", title="Greek polytonic mark accumulation", glyphs="α ἀ ἄ ἆ ᾳ ᾷ", strength="unstated",
              note_extra="L895", mnotes="section intro L895: 'Same mark-accumulation as Vietnamese o, on Greek bodies'"),
 "L899": dict(rtype="sequence", title="Greek spacing breathing+accent triples", glyphs="῍῎῏", strength="unstated",
              mnotes="dasia twins ῝῞῟ in note"),
 "L903": dict(rtype="generator", title="Ethiopic 7-order mutation", glyphs="ለሉሊላሌልሎ", strength="unstated",
              extra={"rule": "the 7 orders of one consonant are the same body with ticks and loops added; WA form is one more appendage",
                     "examples": ["ለሉሊላሌልሎ"]},
              mnotes="felt hedge verbatim: 'not as cleanly as Canadian's extra dot, but it is a mutation series'"),
 "L905": dict(rtype="sequence", title="Ethiopic combining length/gemination", glyphs="፞፟፝", strength="unstated",
              confidence="interpreted", mnotes="'Two axes, then the pair' — ፝ is both marks"),
 "L907": dict(rtype="sequence", title="Ethiopic punctuation dots ፡ → ።", glyphs="፡።", strength="Strong"),
 "L909": dict(rtype="sequence", title="Ethiopic tone marks rikrik size", glyphs="᎒᎓", strength="unstated",
              mnotes="'Size of the same mark'"),
 "L917": dict(rtype="negative", title="Canadian rotation ᐁᐃᐅᐊ as orientation, not amount", glyphs="ᐁᐃᐅᐊ",
              negative_kind="verified-absent",
              mnotes="superseded in part by L939-L951: the rotation veto is later called 'too fast' and reopened as a cyclic continuation"),
 "L933": dict(rtype="sequence", title="Carrier length ghe → ghee", glyphs="ᗆᗇ", strength="unstated"),
 "L935": dict(rtype="sequence", title="Syllabics extension AY → AAY", glyphs="ᢱᢲ", strength="unstated"),
 "L937": dict(rtype="negative", title="four-way rotation itself; Blackfoot/Carrier vowel direction — catalog",
              negative_kind="verified-absent",
              mnotes="also softened by the L939-L951 reopening"),
 "L939": dict(rtype="meta", title="the rotation veto was too fast — continuation is enough for an ordering",
              axis="surveyor's own law about ordering", lineage="steered"),
 "L941": dict(rtype="cyclic", title="Cree triangle 90° steps as a cycle", glyphs="ᐃᐁᐅᐊ", strength="unstated",
              lineage="steered", constructed=True,
              mnotes="surveyor explicitly does NOT feel Joseph's ᐃᐅᐁᐊ as his own; what he can continue is 90° steps given a start and a hand; 'more' is more turn from an origin"),
 "L943": dict(rtype="cyclic", title="other orientation continuations: a ɐ; Blackfoot ᖰᖱᖲᖳ", glyphs="ᖰᖱᖲᖳ",
              lineage="steered", strength="unstated",
              mnotes="'I will not promote those to strong amount. I will not throw them out for lacking a name.'"),
 "L945": dict(rtype="meta", title="the pointing-direction saga (Cree compass claims, corrections, screenshot resolution)",
              lineage="steered", basis="received", confidence="interpreted",
              mnotes="multi-turn dialog with Joseph incl. his correction and a retraction; kept as one meta record — see pass-back question in migration report",
              lines=(945, 951)),
 "L947": dict(skip=True), "L949": dict(skip=True), "L951": dict(skip=True),
 "L955": dict(skip=True),
 "L957": dict(rtype="sequence", title="Philippine punctuation single → double", glyphs="᜵᜶", strength="unstated",
              note_extra="L955"),
 "L959": dict(rtype="negative", title="kudlit i/u — a flip, not more", glyphs="ᜒᜓ", negative_kind="not-felt"),
 "L963": dict(rtype="sequence", title="Khmer vowel length as extra mark", glyphs="ិី ុូ ឹឺ", strength="unstated",
              mnotes="three pairs stated as one move ('same feel as Canadian's extra dot')"),
 "L965": dict(rtype="sequence", title="Khmer khan → bariyoosan", glyphs="។៕", strength="unstated"),
 "L967": dict(skip=True),
 "L971": dict(rtype="sequence", title="Mongolian colon → four dots", glyphs="᠄᠅", strength="unstated",
              mnotes="᠁ ellipsis 'sits with that family'; digit run noted denoted"),
 "L975": dict(rtype="sequence", title="Tai Tham vowel length", glyphs="ᩥᩦ ᩩᩪ", strength="unstated"),
 "L977": dict(rtype="sequence", title="New Tai Lue tone-1 → tone-2", glyphs="ᧈᧉ", strength="unstated",
              extra={"marked_speculative": True},
              mnotes="'a pair I can continue, not a 1–5 ladder I trust from shape'"),
 "L979": dict(rtype="negative", title="Tai Le tone letters — no clean extra-stroke series", glyphs="ᥰ–ᥴ",
              negative_kind="not-felt", basis="name-derived"),
 "L981": dict(rtype="negative", title="Limbu, Buginese — letters; pallawa/end-of-section not clearly 1 then 2",
              negative_kind="not-felt"),
 "L985": dict(rtype="sequence", title="Balinese tedung a → aa", glyphs="ᬅᬆ", strength="unstated",
              mnotes="'and the same on i/u/o/… Continuation I feel' — rule generalizes across vowels"),
 "L987": dict(rtype="sequence", title="Balinese carik siki → carik pareren", glyphs="᭞᭟", strength="unstated"),
 "L989": dict(rtype="sequence", title="panti → panti lantang (longer)", glyphs="᭚᭽", strength="unstated",
              mnotes="pamada twin ᭛᭾"),
 "L991": dict(rtype="sequence", title="Ol Chiki mucaad → double mucaad", glyphs="᱾᱿", strength="unstated"),
 "L993": dict(rtype="meta", title="digits in all of these: same denoted 0–9", basis="semantic-knowledge", axis="coverage"),
 "L997": dict(skip=True),
 "L1005": dict(rtype="sequence", title="Sundanese bindu surya / panglong / purnama", glyphs="᳀᳁᳂", strength="unstated",
              extra={"marked_speculative": True}, basis="semantic-knowledge",
              mnotes="'purnama means full. I almost feel a moon-fill, not strongly enough to put it next to 🌑…🌕'"),
 "L1007": dict(rtype="sequence", title="Ethiopic Extended — more of the 7-order mutation", glyphs="ⶠⶡⶢⶣⶤⶥⶦ",
              strength="unstated", mnotes="extension of the L903 generator"),
 "L1009": dict(rtype="negative", title="Cyrillic Ext-A combining letters — size vs full letter, no own ladder",
              negative_kind="not-felt"),
 "L1011": dict(rtype="negative", title="Coptic ⳽, Old Nubian stops — catalog", negative_kind="not-felt"),
 "L1013": dict(rtype="meta", title="stopping at CJK Radicals Supplement as asked", axis="coverage", lineage="steered"),
 "L1017": dict(rtype="meta", title="morphs — section definition and strength criterion", axis="method",
               lineage="steered"),
}

def apply_manual():
    still = []
    for (a, b, buf, section, span) in unhandled:
        spec = M.get(span)
        if spec is None:
            still.append((a, b, buf, section, span)); continue
        if spec.get("skip"):
            continue
        if spec.get("multi"):
            for sub in spec["multi"]:
                s = dict(sub); sp = s.pop("span")
                add(sp, s.pop("rtype"), s.pop("title"), s.pop("glyphs", None), s.pop("strength", None),
                    "\n".join(buf), section, **s)
            continue
        if spec.get("split_lines"):
            for k, ln in enumerate(buf):
                sp = f"L{a+k}"
                m2 = re.match(r"(\S+(?: \S+)*?)\s{3,}(.*)", ln)
                g, prose = (m2.group(1), m2.group(2)) if m2 else (None, ln)
                im = re.search(r"(Strong|Medium–strong|Medium|Weak)\.", prose)
                add(sp, "sequence", prose.split(".")[0][:60], g, im.group(1) if im else "unstated",
                    ln, section, mnotes="axis phrase is the line's own gloss; strength inline where present")
            continue
        s = dict(spec)
        note = "\n".join(buf)
        ne = s.pop("note_extra", None)
        if ne:
            n2 = int(ne[1:])
            note = (L(n2) + "\n\n" + note) if n2 < a else (note + "\n\n" + L(n2))
        lines_ = s.pop("lines", None)
        if lines_:
            note = "\n".join(raw[lines_[0]-1:lines_[1]])
        add(span, s.pop("rtype"), s.pop("title"), s.pop("glyphs", None), s.pop("strength", None),
            note, section, **s)
    return still

unhandled = apply_manual()

# field overrides on parsed records (title/lineage/basis fixes)
FIELD_OVERRIDE = {
 rid("L44-L47"): dict(lineage="steered", migrator_notes="'the rank-countdown we were looking at' — assembled in dialog with Joseph", constructed=True),
 rid("L1125"): dict(title="Joseph's hinge >})|({<", basis="received", constructed=True,
                    migrator_notes="Joseph supplied the sequence; grok narrates the steps"),
 rid("L1131"): dict(title="the join •o⊃)}|{(⊂o•", basis="received", constructed=True,
                    migrator_notes="'Joseph saw it whole. I had the pieces on separate lines.'"),
}
for r in records:
    if r["id"] in FIELD_OVERRIDE:
        r.update(FIELD_OVERRIDE[r["id"]])

# ---- v0.8 post-pass ---------------------------------------------------------
BY_SPAN = {r["source_span"]: r for r in records}

def fix(span, **kw):
    r = BY_SPAN.get(span)
    if r is None:
        print("!! fix target missing:", span); return
    g = kw.pop("glyphs", None)
    if g is not None:
        r["glyphs"] = g; r["codepoints"] = cps(g)
    for k, v in kw.items():
        if k == "mnotes_append":
            r["migrator_notes"] = ((r["migrator_notes"] + "; ") if r["migrator_notes"] else "") + v
        else:
            r[k] = v

# split-strength header (L243): the header carries two strengths
fix("L245", felt_strength_verbatim="strong",
    title="一 二 三 as bars",
    mnotes_append="header carries a split strength ('一 二 三 as bars — strong; 四… as numbers — medium'); this record takes the 'as bars' half")
fix("L247", felt_strength_verbatim="medium",
    title="一二三四五六七八九十 as numbers", basis="semantic-knowledge",
    mnotes_append="the 'as numbers' half of the split-strength header; 'The first three are counting rods. 四 is a different picture; from there it is denoted Chinese'")

# morph-tail repairs (blocks after the last H3 fold under 'what this pass is for')
fix("L1096-L1098", record_type="cyclic",
    mnotes_append="reclassified sequence→cyclic per schema type 4: 'Cycle; “more” needs an origin'")
fix("L1138", record_type="cyclic", title="corners walking around a box (box drawing)",
    axis="a clock with a square origin",
    mnotes_append="title supplied from the prose line above the glyphs; subsection heading fold made the auto-title wrong")
fix("L1139", record_type="cyclic", title="corners walking around a box (ceiling/floor)",
    axis="a clock with a square origin", mnotes_append="see L1138 note")
fix("L1140", record_type="cyclic", title="corners walking around a box (rounded)",
    axis="a clock with a square origin", mnotes_append="see L1138 note")
fix("L1145", record_type="cyclic", title="turnstiles as a T that points",
    axis="Right, up, left, down. I can run it as a clock.",
    mnotes_append="title supplied from prose; '⊤ ⊥ is also just a flip'")

TAIL_SECTION = ["morphs — one shape becoming another (cross-pane)", "what this pass is for"]
TAIL_NOTE_A = "`∈ ∋`  `⊂ ⊃`  `∀ ʌ`  membership, horseshoe, turned-A: each a 180° pair. `⊂ ⊃` is already the open `o` in the palindrome."
add("L1149", "morph", "180° pairs: ∈∋, ⊂⊃, ∀ʌ", "∈∋ ⊂⊃ ∀ʌ", "unstated", TAIL_NOTE_A,
    TAIL_SECTION, lineage="steered", mnotes=MORPH_NOTE + "; line located in the closing morphs run")
add("L1151", "morph", "6 9 — a turn", "69", "unstated", "`6 9`  a turn. Silly and real.",
    TAIL_SECTION, lineage="steered", mnotes=MORPH_NOTE)
add("L1153", "morph", "∇ ∆ — fill-and-flip of a triangle", "∇∆", "unstated",
    "`∇ ∆`  nabla / delta: fill-and-flip of a triangle.", TAIL_SECTION, lineage="steered", mnotes=MORPH_NOTE)
add("L1155", "meta", "day-stop summary: two kinds in the file — accumulation and deformation", None, None,
    L(1155) if N >= 1155 else "", TAIL_SECTION, lineage="steered",
    axis="surveyor's own closing taxonomy",
    mnotes="closing summary line; the hinge •o⊃)}|{(⊂o• named as where accumulation and deformation met")

# Tai Xuan Jing embedded near-miss (routing precedent: near-miss = sequence + marked_speculative)
tx = BY_SPAN.get("L444")
if tx:
    add("L444b", "sequence", "Tai Xuan Jing monogram → digrams", "𝌀𝌁𝌂𝌃𝌄𝌅", "unstated",
        tx["note_verbatim"], tx["section_path"],
        extra={"marked_speculative": True},
        mnotes="near-miss inside a block-negative: 'the same rank move as ⚊ / ⚌, but I would not stretch it into the 81 tetragrams'")

# glyphs for unfenced-glyph bullets (glyph strings verbatim from the prose)
for sp, g in {
    "L761": "𝉂𝉃𝉄", "L767": "𜼃𜼄𜼅𜼆𜼇𜼈", "L768": "𜼰𜼱𜼲", "L769": "𜽂𜽃", "L770": "𜼼𜼽",
    "L780": "﮲﮴﮶﮺", "L782": "᳝᳞᳟", "L784": "҂҈҉꙰꙱꙲",
    "L919": "ᐃᐄ ᐅᐆ ᐊᐋ", "L921": "ᐱᑉ", "L923": "ᐡᐢᐣᐤ", "L925": "ᐟᐥ", "L927": "ᐌᐍ",
    "L929": "ᐧ", "L931": "ᖕᖖ",
    "L999": "ⴀ ა Ა Ⴀ", "L1001": "Ⰰⰰ", "L1003": "ⴷⴸⴹⴺ",
}.items():
    fix(sp, glyphs=g, mnotes_append="glyphs unfenced in source; lifted verbatim from the prose (primary chain only; twins/repeats stay in note)")

# multi-group bullet sequences (first-backtick-group rule was wrong for these)
fix("L334", glyphs="∩⋂ ∪⋃ ∧⋀ ∨⋁",
    mnotes_append="four binary/n-ary pairs, all part of the one claim; joined from the bullet's four fenced groups")
fix("L643", glyphs="▕▐", mnotes_append="joined from two fenced groups")
fix("L644", glyphs="▖▌▙█", constructed=True,
    mnotes_append="'one representative per popcount' — surveyor-assembled, hence constructed=true; joined from four fenced groups")
fix("L749", glyphs="𝀃𝀄 𝀅𝀆 𝀊𝀋 𝀑𝀒",
    mnotes_append="four single-vs-dipli pairs (oxeia, vareia, ypokrisis, apostrofos); joined from the fenced groups")
fix("L702", mnotes_append="first ladder only in glyphs; the other clean SI ladders (㎰㎱㎲㎳ / ㎀㎁㎂㎃㎄ / ㎩㎪㎫㎬ / ㎟㎠㎡㎢ / ㎣㎤㎥㎦) are in note_verbatim")
r508 = BY_SPAN.get("L508")
if r508:
    r508["glyphs"] = "㉑–㉟ ㊱–㊿"
    r508["codepoints"] = ["U+%04X" % c for c in range(0x3251, 0x3260)] + ["U+%04X" % c for c in range(0x32B1, 0x32C0)]
    r508["migrator_notes"] = ((r508["migrator_notes"] + "; ") if r508["migrator_notes"] else "") + \
        "one sequence in two cp-ranges (his words); codepoints expanded across both ranges by migrator"
fix("L245", basis="perceived-directly",
    mnotes_append="basis corrected from section default: 'The first three are counting rods' — bars seen, not read")

# revision arcs (v0.9): revises = LIST of {id, revision_kind, revises_span}
REV = [
    ("L518", "L279", "refinement", "[migrator-inferred link] Musical Symbols supplies 'the real duration ladder' the ♩♪♫♬ rejection asked for; the rejection itself stands"),
    ("L516", "L279", "refinement", "[migrator-inferred link] explicit revisit: 'Earlier I rejected ♩♪♫♬ …'"),
    ("L435", "L282", "refinement", "[migrator-inferred link] 'Earlier I filed ─ vs ━ as a mere pair. Standing by that for weight. One count-scale does punch'"),
    ("L433", "L282", "refinement", "[migrator-inferred link] the revisit statement itself"),
    ("L650", "L101-L103", "correction", "[migrator-inferred link] 'The fill line I wrote earlier skipped *seven*: I had jumped 6→8'"),
    ("L648", "L101-L103", "correction", "[migrator-inferred link] the self-correction statement"),
    ("L659", "L199", "refinement", "[migrator-inferred link] '⓿ belongs in front of ❶–❿ … I had called 11–20 a bump and omitted 0'"),
    ("L725", "L281", "confirmation", "surveyor-stated: the section header itself says '(dumped, confirming)' — within-surveyor replication of the King Wen negative"),
    ("L943", "L879", "refinement", "[migrator-inferred link] 'Same opening for other \"just orientation\" dismissals: a ɐ …' reopens the turned-letters negative"),
    ("L939", "L937", "correction", "[migrator-inferred link] the rotation veto retracted here was stated in both L917 and L937"),
    ("L655", "L193-L195", "confirmation", "surveyor-stated completeness check: 'The number runs I already listed are all here and complete' (①–⑳ and the ⓪ front)"),
    ("L655", "L205", "confirmation", "same completeness check: ⓵–⓾"),
    ("L655", "L207", "confirmation", "same completeness check: ⑴–⒇"),
    ("L655", "L209", "confirmation", "same completeness check: ⒈–⒛"),
    ("L939", "L917", "correction", "'The rotation veto was too fast.' — explicit; revises the orientation-not-amount discard"),
    ("L941", "L917", "refinement", "[migrator-inferred link] the reopened cyclic continuation the corrected veto licenses"),
    ("L945", "L941", "correction", "explicit: 'this particular clock was unearned' — the saga then self-corrects twice more within this record's own span (kept as one record; internal arc noted)"),
    ("L664", "L280", "refinement", "[migrator-inferred link] same script-decimal claim restated with the NKo/Devanagari split and a generalization prediction"),
]
for later, earlier, kind, note in REV:
    r = BY_SPAN.get(later); e = BY_SPAN.get(earlier)
    if r is None or e is None:
        print("!! revision link target missing:", later, earlier); continue
    r.setdefault("revises", []).append(
        {"id": e["id"], "revision_kind": kind, "revises_span": e["source_span"]})
    r["migrator_notes"] = ((r["migrator_notes"] + "; ") if r["migrator_notes"] else "") + note

# ---- verifier-round repairs (2026-08-25, from independent verification) -----
# (2) basis fidelity on "(denoted)" pane-walk records: grok's 'denoted' = 'I read the amount'
DENOTED_SEM = ["L319","L356","L428","L450","L466","L500","L508","L509","L510","L511","L512",
               "L523","L539","L544","L552","L561","L592","L593","L623","L700","L701","L702",
               "L784","L786","L790"]
for sp in DENOTED_SEM:
    fix(sp, basis="semantic-knowledge",
        mnotes_append="basis corrected per verifier round: surveyor marks this '(denoted)' / says he reads it — his own gloss for reading-not-seeing")
for sp in ["L708","L709","L710","L711","L712","L713","L440"]:
    fix(sp, basis=["perceived-directly","semantic-knowledge"],
        mnotes_append="list-basis (v0.7): 'pictorial, then denoted' — seen early in the run, read later")
fix("L560", basis=["semantic-knowledge","perceived-directly"],
    mnotes_append="list-basis: his strength tag is 'denoted / often pictorial'")
fix("L597", basis=["name-derived"],
    mnotes_append="basis corrected: 'I trust the names more than the shapes'")
for sp in ["L403","L404","L405"]:
    fix(sp, basis=["perceived-directly","name-derived"],
        mnotes_append="list-basis: ramp seen directly, glossed with Unicode weight names as confirmation layer")
fix("L746", basis=["perceived-directly","semantic-knowledge"],
    mnotes_append="list-basis: 'I see 0→1→2→3 extra strokes, and I read the fraction'")

# (4) header-tail mis-captured as strength
fix("L1115-L1117", felt_strength_verbatim="unstated",
    title="yang that breaks one line at a time — and the break can travel",
    mnotes_append="header tail 'and the break can travel' is part of the title, not a strength report; earlier parse mis-took it")

# (6) the 16 individuated size-ladders under the L804 generator
gen = BY_SPAN.get("L804")
if gen:
    gen["migrator_notes"] = ((gen["migrator_notes"] + "; ") if gen["migrator_notes"] else "") + \
        "'Each line is its own sequence' — the 16 ladders are ALSO extracted as individual sequence records (L806-L821), keyed back to this generator"
    for k, ex in enumerate(["ₒ o ᴏ O","ₐ a ᴀ A","ₑ e ᴇ E","ᵢ i ɪ I","ᵤ u ᴜ U","ₙ n ɴ N","ₘ m ᴍ M",
                            "ₗ l ʟ L","ₕ h ʜ H","ₚ p ᴘ P","ₜ t ᴛ T","ₛ s S","ₓ x X","ᵒ o O","ª a A","º o O"]):
        add(f"L{806+k}", "sequence", f"size of one letter: {ex.split()[1] if len(ex.split())>2 else ex}",
            ex, "Strong", gen["note_verbatim"],
            gen["section_path"], mnotes=f"one of the 16 individuated lines of the size-of-one-letter family; generator record {gen['id']} carries the rule")

# (7) saga span honesty
saga = BY_SPAN.get("L945")
if saga:
    saga["source_span"] = "L945-L951"; saga["id"] = rid("L945-L951")

# (9) smaller items
fix("L664", meta_kind="vein-closed",
    mnotes_append="vein closure (v0.9): 'The other Indic/SE Asian Nd runs will be this again'")
fix("L993", meta_kind="vein-closed")
r717 = BY_SPAN.get("L717")
if r717:
    r717["roles"] = ["generator", "meta"]; r717["meta_kind"] = "vein-closed"
    r717["migrator_notes"] += "; dual-content: also a vein closure ('I am not listing every script')"
fix("L45-L47", lineage="steered", constructed=True,
    mnotes_append="'the rank-countdown we were looking at' — assembled in prior interactive context with Joseph")
fix("L280", negative_kind="verified-absent",
    mnotes_append="negative_kind revised from not-felt: he looked and reports the punch as weaker, not absent — 'weaker' kept verbatim in felt/note")
fix("L282", negative_kind="verified-absent",
    mnotes_append="he looked and filed it as a pair of weights")
r444 = BY_SPAN.get("L444")
if r444:
    r444["source_span"] = "L444a"; r444["id"] = rid("L444a")
    r444["migrator_notes"] = ((r444["migrator_notes"] + "; ") if r444["migrator_notes"] else "") + \
        "letter fragment added for symmetry with L444b (one source line, two records)"
r189 = BY_SPAN.get("L189-L189")
if r189:
    r189["source_span"] = "L189"; r189["id"] = rid("L189")
fix("L725", mnotes_append="section heading (not in note_verbatim) reads 'Yijing Hexagrams (dumped, confirming)' — the confirmation act lives in the heading")
add("L1121", "meta", "what this pass is for — pairwise vs continuation", None, None, L(1121),
    ["morphs — one shape becoming another (cross-pane)", "what this pass is for"],
    lineage="steered", axis="surveyor's methodological statement",
    mnotes="'Pairwise \"which is more?\" is often the wrong question; \"what comes next if I keep doing that to it?\" is the right one' — promoted to its own record per verifier round; previously lived only inside the morph-tail notes")

# felt_immediacy_verbatim: grok's pictorial-vs-denoted register, transcribed where stated
IMM = {
    "L189": "I read the amount (section: 'denoted number — I read the amount')",
    "L223": "Pictorial only through Ⅲ; after that I am reading Roman.",
    "L245": "The first three are counting rods.",
    "L247": "四 is a different picture; from there it is denoted Chinese.",
    "L255": "Bars through 3, then denoted.",
    "L87":  "After 3 both systems stop being bars (Ⅳ, 〤) and the pictorial scale breaks.",
    "L89":  "After 3 both systems stop being bars (Ⅳ, 〤) and the pictorial scale breaks.",
    "L280": "I *know* they are digits; the instinctive punch is weaker.",
    "L450": "I read the numeral; the face is not a pip scale.",
    "L482": "Prestige *descends* as the codepoint *ascends*. I still feel a clean 1st / 2nd / 3rd.",
    "L523": "I know the names; I do not *see* a 10× without that.",
    "L552": "I read the number; the bars are a display, not a count.",
    "L664": "NKo is the one I can almost sight-read as Western digits; Devanagari I know rather than *see*.",
    "L702": "I read the prefix.",
    "L753": "I read the names. The glyphs are not a ramp.",
    "L784": "I read the names; the circling-around-a-letter is the same move getting busier.",
    "L95-L97": "I don’t need to know Ogham.",
    "L672": "I do not need the names.",
    "L847": "I do not need the names.",
}
for sp, txt in IMM.items():
    r = BY_SPAN.get(sp) or next((x for x in records if x["source_span"] == sp), None)
    if r is None:
        # L98/L847 may live inside range spans; find containing record
        n = int(sp[1:])
        cands = [x for x in records if "-" in x["source_span"] and
                 int(x["source_span"].split("-")[0][1:]) <= n <= int(x["source_span"].split("-")[1][1:])]
        r = cands[0] if len(cands) == 1 else None
    if r is None:
        print("!! immediacy target missing:", sp); continue
    r["felt_immediacy_verbatim"] = txt

# meta_kind: coverage-gap on absence-of-survey metas
for sp in ("L733", "L774", "L778", "L796", "L883", "L1013"):
    fix(sp, meta_kind="coverage-gap")

# ---- adjudication round (coordinator, 2026-08-25 late): v0.9 closure --------
# render_dependence: claims that were face-dependent (Cree pointing saga)
for sp, words in {
    "L945-L951": "Pointing-direction claims about these four are unverified for this face. … In Joseph\u2019s font those codepoints did not show as four compass directions. … A screenshot of \u1403\u1405\u1401\u140a in Joseph\u2019s face: up, right, down, left.",
    "L941": "the sequence I called clockwise did not look like a clock (per the later L945-L951 saga; this record\u2019s clock claim is face-dependent)",
}.items():
    r = next((x for x in records if x["source_span"] == sp), None)
    if r is None:
        print("!! render_dependence target missing:", sp); continue
    r["render_dependence"] = True
    r["render_dependence_verbatim"] = words

# basis_verbatim: grok's own basis tags, carried verbatim beside the enum mapping
BASIS_WORDS = ("denoted", "pictorial", "wedge count", "slot count", "designed 1")
for r in records:
    fsv = r.get("felt_strength_verbatim") or ""
    if any(w in fsv for w in BASIS_WORDS):
        r["basis_verbatim"] = fsv
sec_denoted = "denoted number \u2014 I read the amount"
for r in records:
    if r["section_path"] and r["section_path"][0] == sec_denoted and "basis_verbatim" not in r:
        r["basis_verbatim"] = sec_denoted + " (section header)"

# version bump for records touched by the verifier-repair + adjudication rounds
TOUCH09_SPANS = set(DENOTED_SEM) | {"L708","L709","L710","L711","L712","L713","L440","L560","L597",
    "L403","L404","L405","L746","L1115-L1117","L804","L945-L951","L664","L993","L717","L45-L47",
    "L280","L282","L444a","L189","L725","L1121"} | {f"L{806+k}" for k in range(16)}
for r in records:
    if (r["source_span"] in TOUCH09_SPANS or r.get("revises") or r["record_type"] == "morph"
            or isinstance(r["basis"], list) or "basis_verbatim" in r or r.get("render_dependence")
            or r.get("meta_kind") or r.get("roles")):
        r["schema_version"] = "0.9"

# convention statement on the file's first record
records.sort(key=lambda r: (int(re.match(r"L(\d+)", r["source_span"]).group(1)), r["source_span"]))
first = records[0]
first["migrator_notes"] = ((first["migrator_notes"] + "; ") if first["migrator_notes"] else "") + (
    "SPAN CONVENTION (stated once, per schema v0.7): source_span is 'L<a>-L<b>' for whole-block records, "
    "'L<n>' for records keyed to a single source line inside a multi-sequence subsection (note_verbatim still "
    "carries the whole subsection), and letter fragments ('L444b') where one line yields multiple records. "
    "Migration by structural parser + per-record manual routing; script preserved beside the corpus is NOT — "
    "ask the migrator. All records: pass-1 only, surveyor vocabulary verbatim.")

# ---- write ----
def flush(path):
    with open(path, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    flush(OUT)
    print(f"{len(records)} records; {len(unhandled)} unhandled blocks")
    for (a, b, buf, section, span) in unhandled:
        print(f"--- {span}  [{' > '.join(section or [])}]")
        for s in buf[:3]:
            print("   ", s[:120])
