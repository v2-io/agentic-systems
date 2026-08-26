#!/usr/bin/env python3
"""Pass-1 migration of grok-1.md -> extracted/grok-1.jsonl (schema v0.5).

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
        "schema_version": "0.5",
        "record_type": rtype,
        "surveyor": "grok",
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
    if not s or s.startswith("#") or s.startswith("-") and len(s) > 1 and s[1] == " ":
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

MORPH_NOTE = ("record_type 'morph' is a migrator-proposed type (not in schema v0.5): "
              "deformation-continuation, surveyor's own framing: 'what comes next if I "
              "keep doing that to it?' rather than pairwise 'which is more?'")

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

# ---- write ----
def flush(path):
    with open(path, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    flush(OUT + ".partial")
    print(f"{len(records)} records; {len(unhandled)} unhandled blocks")
    for (a, b, buf, section, span) in unhandled:
        print(f"--- {span}  [{' > '.join(section or [])}]")
        for s in buf[:3]:
            print("   ", s[:120])
