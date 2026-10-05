#!/usr/bin/env python3
"""Classify the codepoint-far truth pairs (|dcp| > 1) of a reference set by what relates them.
  python3 classify_far.py GT TRUTH   (e.g. r011 first2, survey first1)"""
import collections, json, re, sys
from lib import DER, name, block
gt, tk = sys.argv[1], sys.argv[2]
G = json.load(open(DER / f"gt-{gt}.json"))
def toks(g): return re.split(r"[ \-]+", name(g) or "")
def rel(q, g):
    a, b = toks(q), toks(g)
    if len(a) == len(b) and sum(x != y for x, y in zip(a, b)) == 1:
        return "name-template (one token differs)"
    if abs(len(a) - len(b)) == 1 and (set(a) <= set(b) or set(b) <= set(a)):
        return "name-template (one token added)"
    if block(q) == block(g):
        return "same block, names differ more"
    if set(a) & set(b) - {"WITH", "AND", "OF", "SIGN", "SYMBOL", "LETTER", "SMALL", "CAPITAL"}:
        return "other block, names share a content word"
    return "other block, no shared name word"
c, ex = collections.Counter(), collections.defaultdict(list)
for I in G["instances"].values():
    q = I["node"]
    for g, p in I["props"].items():
        fams = set(p["fams_first"] if tk.startswith("first") else p["fams"]) - {"muse"}
        if len(fams) >= int(tk[-1]) and g not in I["ctx_all"] and g != q and abs(ord(g) - ord(q)) > 1:
            r = rel(q, g); c[r] += 1
            if len(ex[r]) < 400: ex[r].append(f"{' '.join(I['ctx'][-3:])} → {g}")
t = sum(c.values())
print(f"{gt}/{tk}: {t} codepoint-far truth pairs")
import random; random.seed(0)
for r, v in c.most_common():
    print(f"  {v/t:5.2f}  {v:5d}  {r}")
    print("         e.g. " + " | ".join(random.sample(ex[r], min(8, len(ex[r])))))
