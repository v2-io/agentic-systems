#!/usr/bin/env python3
"""At the END of a Unicode-allocated series, codepoint+1 and the perceived continuation come apart
(⑳ U+2473 is followed in the chart by ⑴ PARENTHESIZED DIGIT ONE, while 21 lives at ㉑ U+3251).
Find every instance (r012 data) whose node is such a series end, approached along its series, and show what minds
proposed first: the chart's next code point, or something else.
A 'series end' here: node q and the previous context glyph p share a name template with a numeral token, and q+1's
name does NOT continue that template (so the chart turns a corner at q)."""
import collections, json, re
from lib import DER, name
G = json.load(open(DER / "gt-r012.json"))
NUM = "ZERO ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN ELEVEN TWELVE THIRTEEN FOURTEEN FIFTEEN SIXTEEN SEVENTEEN EIGHTEEN NINETEEN TWENTY".split()
def tmpl(g):
    n = name(g) or ""
    t = re.split(r"[ \-]+", n)
    idx = [i for i, x in enumerate(t) if x in NUM or x.isdigit() or re.fullmatch(r"[IVXLCDM]+", x or "-")]
    if not idx: return None
    i = idx[-1]; return tuple(t[:i]) + ("#",) + tuple(t[i + 1:])
rows = collections.defaultdict(lambda: collections.Counter())
fams = collections.defaultdict(lambda: collections.defaultdict(set))
for k, I in G["instances"].items():
    if I["kind"] != "next" or len(I["ctx"]) < 2:
        continue
    q, p = I["node"], I["ctx"][-2]
    tq = tmpl(q)
    if not tq or tmpl(p) != tq:
        continue
    nx = chr(ord(q) + 1)
    if tmpl(nx) == tq:
        continue           # the chart continues the series: not an end
    for g, pr in I["props"].items():
        for f in pr["fams_first"]:
            rows[q][g] += 1; fams[q][g].add(f)
for q in sorted(rows, key=ord):
    nx = chr(ord(q) + 1)
    tot = sum(rows[q].values())
    chart = rows[q][nx]
    print(f"{q} ({name(q)}) chart-next {nx} ({name(nx)}): {chart}/{tot} first proposals")
    print("     " + "  ".join(f"{g}×{c}[{''.join(sorted(x[0] for x in fams[q][g]))}]" for g, c in rows[q].most_common(8)))
