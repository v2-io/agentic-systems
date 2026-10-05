#!/usr/bin/env python3
"""Per family: how often is the FIRST proposal the next code point (+1), within +-3, or elsewhere; and the none rate.
  python3 family_cp.py GT [GT ...]"""
import collections, json, sys
from lib import DER
for gt in sys.argv[1:]:
    G = json.load(open(DER / f"gt-{gt}.json"))
    c = collections.defaultdict(collections.Counter)
    for k, I in G["instances"].items():
        if k.endswith("<"):
            continue
        q = I["node"]
        for g, p in I["props"].items():
            for f in p["fams_first"]:
                d = ord(g) - ord(q)
                c[f]["+1" if d == 1 else "-1" if d == -1 else "±2..3" if abs(d) <= 3 else "elsewhere"] += 1
    print(gt)
    for f in sorted(c):
        t = sum(c[f].values())
        print(f"  {f:7s} first proposals={t:5d}  " + "  ".join(f"{k}:{c[f][k]/t:.2f}" for k in ("+1", "-1", "±2..3", "elsewhere")))
