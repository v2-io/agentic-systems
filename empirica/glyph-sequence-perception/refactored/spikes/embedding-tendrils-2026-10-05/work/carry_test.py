#!/usr/bin/env python3
"""Do minds' "next" proposals that track codepoint order behave like UTF-8 last-byte increments?

In UTF-8, consecutive code points (>= U+0080) differ only in the final byte, except where that byte wraps
0xBF -> 0x80 and a carry goes into the byte before. A mind that "increments the last byte" without carrying would,
at q with cp % 64 == 63, propose cp - 63 (same lead bytes, last byte 0x80) instead of cp + 1.
Across every answer we have (study r000-r012 next/between + this spike's probe), for each node q and each proposal g
by rank-0, classify g - q as +1, -63 (carry-free wrap), -1, other; split by whether q sits at a 64-boundary.
"""
import collections, json
from lib import DER, name
rows = []
for gt in ("r012", "probe"):
    G = json.load(open(DER / f"gt-{gt}.json"))
    for k, I in G["instances"].items():
        q = I["node"]
        if ord(q) < 0x80 or (I["kind"] == "between" and k.endswith("<")):
            continue
        for g, p in I["props"].items():
            for f in p["fams_first"]:
                rows.append((gt, k, q, g, f))
c = collections.defaultdict(collections.Counter)
ex = collections.defaultdict(list)
for gt, k, q, g, f in rows:
    d = ord(g) - ord(q)
    at = "q at 64-boundary (cp%64==63)" if ord(q) % 64 == 63 else "q elsewhere"
    cls = {1: "+1", -63: "-63 (carry-free wrap)", -1: "-1"}.get(d, "other")
    c[(at, f)][cls] += 1
    if at.startswith("q at"):
        ex[at].append(f"{f}: {q} U+{ord(q):04X} → {g} U+{ord(g):04X} ({cls})")
for key in sorted(c):
    t = sum(c[key].values())
    print(key, t, {k: f"{v/t:.2f}" for k, v in c[key].most_common()})
for at, v in ex.items():
    print("\n".join(v[:60]))
