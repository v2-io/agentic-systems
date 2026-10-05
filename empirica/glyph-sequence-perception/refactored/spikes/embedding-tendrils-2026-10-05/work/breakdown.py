#!/usr/bin/env python3
"""hit@k per kind of node glyph, from a retrieval-*.json written by eval_retrieval.py.
  python3 breakdown.py RESULTFILE K RANKER ..."""
import collections, json, sys
from lib import DER, ucd
f, K, specs = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
R = json.load(open(DER / f))
def kind(g):
    c = ucd()[g][1]; cp = ord(g)
    if c[0] == "N": return "numerals (N*)"
    if c[0] == "L": return "letters (L*)"
    if c[0] == "P": return "punctuation (P*)"
    if cp >= 0x1F300: return "emoji & pictographs (S, >=U+1F300)"
    if 0x2500 <= cp <= 0x25FF or 0x1FB00 <= cp <= 0x1FBFF or 0x2800 <= cp <= 0x28FF: return "box/block/shape/braille (S)"
    return "other symbols (S*)"
rows = collections.defaultdict(dict)
for s in specs:
    by = collections.defaultdict(list)
    for d in R[s]["detail"]:
        by[kind(d["node"])].append(min(d["ranks"]) <= K)
    for k, v in by.items():
        rows[k][s] = (sum(v) / len(v), len(v))
print(f"hit@{K}  ({f})")
print(f"{'node kind':38s} {'n':>5s} " + " ".join(f"{s[:26]:>27s}" for s in specs))
for k in sorted(rows, key=lambda k: -rows[k][specs[0]][1]):
    print(f"{k:38s} {rows[k][specs[0]][1]:5d} " + " ".join(f"{rows[k][s][0]:27.2f}" for s in specs))
