#!/usr/bin/env python3
"""Fresh-glyph probe by UTF-8 length: per family, share of glyphs answered at all, and share whose first proposal is
the next code point (+1) or previous (-1)."""
import collections, json
from lib import DER
G = json.load(open(DER / "gt-probe.json"))
c = collections.defaultdict(collections.Counter)
for q, I in G["instances"].items():
    nb = len(q.encode())
    firsts = collections.defaultdict(list)
    for g, p in I["props"].items():
        for f in p["fams_first"]:
            firsts[f].append(g)
    for f in ("claude", "gemini", "grok"):
        c[(nb, f)]["n"] += 1
        if f in firsts:
            c[(nb, f)]["answered"] += 1
            d = ord(firsts[f][0]) - ord(q)
            c[(nb, f)]["±1"] += abs(d) == 1
print("bytes family   n  answered  first-proposal-is-±1 (share of all items)")
for k in sorted(c):
    n = c[k]["n"]
    print(f"  {k[0]}    {k[1]:7s} {n:3d}   {c[k]['answered']/n:.2f}      {c[k]['±1']/n:.2f}")
