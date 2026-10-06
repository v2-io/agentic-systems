"""Versioned parsers: verbatim raw sheet answer -> one parsed record per presentation. Never imputes.

Outcome vocabulary for a triad (glyphs as shown):
  ("mid", g)            ordered, g in the middle
  ("tie2", end, a, b)   a and b at the same step, `end` separate
  ("tie3",)             all three at the same step
  ("two", a, b)         only a and b go together (a < b by codepoint)
  ("none",)
Order answers: lines = list of sequences, each a list of steps (lists of glyphs), with "GAP" markers kept as
  steps of their own; extra = glyphs placed in extra; omitted = shown glyphs mentioned nowhere.
Next/between answers: proposals = list of strings (verbatim, NFC), or none.
Any element that is neither a shown glyph, a #k position, a nested tie list, nor GAP (order) makes the
whole answer 'unparsed'; so does a glyph used twice, or a triad 'seq' that is not exactly the three glyphs.
"""
import json, re, unicodedata as U

PARSER = "q0.1"

def _answers(raw):
    if not raw:
        return None
    dec = json.JSONDecoder()
    for m in reversed([m.start() for m in re.finditer(r'\{\s*"answers"', raw)]):
        try:
            d, _ = dec.raw_decode(raw[m:])
            a = d.get("answers")
            if isinstance(a, list):
                return a
        except Exception:
            continue
    return None

class Bad(Exception):
    pass

def _elem(x, shown, allow_gap=False, allow_tie=True):
    """-> a step: list of glyphs (len>1 = tie), or 'GAP'."""
    if isinstance(x, list):
        if not allow_tie or not x:
            raise Bad("nested")
        out = []
        for y in x:
            if isinstance(y, list):
                raise Bad("deep-nest")
            out += _elem(y, shown, allow_gap=False)
        return out
    if not isinstance(x, str):
        raise Bad("type")
    t = U.normalize("NFC", x).strip()
    if allow_gap and t.upper() == "GAP":
        return "GAP"
    if t in shown:
        return [t]
    m = re.fullmatch(r"#\s*(\d+)", t)
    if m and 1 <= int(m.group(1)) <= len(shown):
        return [shown[int(m.group(1)) - 1]]
    raise Bad(f"unknown:{t[:12]}")

def _steps(seq, shown, allow_gap=False):
    if not isinstance(seq, list) or not seq:
        raise Bad("seq")
    return [_elem(x, shown, allow_gap) for x in seq]

def parse_triad(a, shown):
    keys = [k for k in ("seq", "two", "none") if a.get(k) not in (None, False, [], "")]
    if len(keys) != 1:
        raise Bad(f"keys:{keys}")
    k = keys[0]
    if k == "none":
        return ("none",)
    if k == "two":
        st = _steps(a["two"], shown)
        g = [x for s in st for x in s]
        if len(g) != 2 or len(set(g)) != 2:
            raise Bad("two")
        x, y = sorted(g)
        return ("two", x, y)
    st = _steps(a["seq"], shown)
    flat = [x for s in st for x in s]
    if sorted(flat) != sorted(shown) or len(set(flat)) != 3:
        raise Bad("seq-members")
    lens = [len(s) for s in st]
    if lens == [1, 1, 1]:
        return ("mid", st[1][0])
    if lens == [3]:
        return ("tie3",)
    if lens in ([1, 2], [2, 1]):
        end = st[0][0] if lens == [1, 2] else st[1][0]
        pair = sorted(st[1] if lens == [1, 2] else st[0])
        return ("tie2", end, pair[0], pair[1])
    raise Bad("seq-shape")

def parse_order(a, shown):
    if a.get("none") and not a.get("seqs"):
        return {"none": True}
    seqs = a.get("seqs")
    if not isinstance(seqs, list) or not seqs:
        raise Bad("seqs")
    if seqs and all(isinstance(x, str) for x in seqs):
        seqs = [seqs]                      # a single flat list: one sequence
    lines, seen = [], []
    for s in seqs:
        st = _steps(s, shown, allow_gap=True)
        glyph_steps = [x for x in st if x != "GAP"]
        if not glyph_steps:
            continue
        seen += [g for x in glyph_steps for g in x]
        lines.append(st)
    extra = []
    for x in a.get("extra") or []:
        st = _elem(x, shown, allow_tie=False)
        extra += st
    if len(seen + extra) != len(set(seen + extra)):
        raise Bad("dup")
    omitted = [g for g in shown if g not in set(seen + extra)]
    if not lines:
        return {"none": True, "extra": extra, "omitted": omitted}
    return {"lines": lines, "extra": extra, "omitted": omitted}

def parse_props(a, key):
    if a.get("none") and not a.get(key):
        return {"none": True}
    v = a.get(key)
    if isinstance(v, str):
        v = [v]
    if not isinstance(v, list) or not v:
        raise Bad("props")
    out = [U.normalize("NFC", str(x)).strip() for x in v if str(x).strip()]
    if not out:
        raise Bad("props-empty")
    return {"proposals": out[:3]}

def parse_continue(a):
    """-> {"continuation": [...]} in the mind's order, repeats kept (they are the point), up to 16; or {"none": True}."""
    if a.get("none") and not a.get("continue"):
        return {"none": True}
    v = a.get("continue")
    if isinstance(v, str):
        v = v.split() if " " in v.strip() else list(v.strip())
    if not isinstance(v, list) or not v:
        raise Bad("continue")
    out = [U.normalize("NFC", str(x)).strip() for x in v if str(x).strip()]
    if not out:
        raise Bad("continue-empty")
    return {"continuation": out[:16]}

def parse_sheet(raw, sheet):
    """-> {pid: {"status": "ok"|"unparsed", "answer": ..., "why": ...}} for every entry of the sheet."""
    ans = _answers(raw)
    byid = {}
    for a in ans or []:
        if isinstance(a, dict) and isinstance(a.get("id"), int):
            byid.setdefault(a["id"], []).append(a)
    out = {}
    for e in sheet["entries"]:
        lst = byid.get(e["id"], [])
        if len(lst) != 1:
            out[e["pid"]] = {"status": "unparsed", "why": "missing" if not lst else "duplicate-id"}
            continue
        a, shown, k = lst[0], [g for g in e["shown"] if g != "GAP"], sheet["kind"]
        try:
            if k == "triad":
                v = parse_triad(a, shown)
            elif k == "order":
                v = parse_order(a, shown)
            elif k == "next":
                v = parse_props(a, "next")
            elif k == "continue":
                v = parse_continue(a)
            else:
                v = parse_props(a, "between")
            out[e["pid"]] = {"status": "ok", "answer": v}
        except Bad as ex:
            out[e["pid"]] = {"status": "unparsed", "why": str(ex)}
    return out
