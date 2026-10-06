#!/usr/bin/env python3
"""Score the carry probe (probe-carry/): per arm (boundary = cp%64==63, control = mid-run) and family, how the
FIRST proposal relates to q: +1 (correct next code point; at a boundary this needs a UTF-8 carry), -63 at a boundary
(last byte incremented with no carry), -1, other, or none."""
import collections, json
from lib import DER, SPIKE, name
G = json.load(open(DER / "gt-probe-carry.json"))
arm = {x["g"]: x["arm"] for x in json.load(open(SPIKE / "probe-carry" / "glyphs.json"))}
c = collections.defaultdict(collections.Counter)
for q, I in G["instances"].items():
    firsts = collections.defaultdict(list)
    for g, p in I["props"].items():
        for f in p["fams_first"]:
            firsts[f].append(g)
    for f in ("claude", "gemini", "grok"):
        if f not in I["fams_answered"]:
            continue
        gs = firsts.get(f)
        if not gs:
            c[(arm[q], f)]["none"] += 1; continue
        d = ord(gs[0]) - ord(q)
        c[(arm[q], f)][{1: "+1", -63: "-63 no-carry", -1: "-1"}.get(d, "other")] += 1
for k in sorted(c):
    t = sum(c[k].values())
    print(f"{k[0]:9s} {k[1]:7s} n={t:3d}  " + "  ".join(f"{x}:{c[k][x]/t:.2f}" for x in ("+1", "-63 no-carry", "-1", "other", "none")))
print()
for q, I in sorted(G["instances"].items(), key=lambda kv: arm[kv[0]]):
    if arm[q] == "boundary":
        print(q, f"U+{ord(q):05X}", (name(q) or "")[:34].ljust(34), " ".join(f"{g}({ord(g)-ord(q):+d})[{''.join(sorted(x[0] for x in p['fams_first']))}]" for g, p in I["props"].items() if p["fams_first"]))
