#!/usr/bin/env python3
"""Triad analysis: per-judge cycles, cross-judge agreement, graded distances, chains.

Each triad (A,B,C): judge 2p sees A·B, B·C, C·A; judge 2p+1 sees B·A, C·B, A·C.
"""
import json, sys
from collections import defaultdict, Counter

BY = {"somewhat": 1, "much": 2, "vastly": 3}
data = json.load(open(sys.argv[1]))["result"]["walk"]
triads = json.load(open("walk5-triads.json"))

# per-judge: triad -> list of (a, b, answer, dist)
jt = defaultdict(lambda: defaultdict(list))
for entry in data:
    c = entry["chunk"]
    key = json.load(open(f"walk5-key-{c}.json"))
    amap = {a["id"]: (a["more"], BY.get(a.get("by"))) for a in (entry["answers"] or [])}
    for s in key:
        if s["id"] in amap:
            m, b = amap[s["id"]]
            jt[c][s["triad"]].append((s["a"], s["b"], m, b))

def norm(a, b, m):
    """return +1 if a judged more, -1 if b, 0 tie, None perp/invalid"""
    if m == "≈": return 0
    if m == "⟂": return None
    if m == a: return 1
    if m == b: return -1
    if m and a in m: return 1
    if m and b in m: return -1
    return None

cycle_viol = 0; cycle_ok = 0; partial = 0
cross_agree = 0; cross_disagree = 0; cross_n = 0
succ = defaultdict(dict)
perp_cut = 0
for ti, (A, B, C) in enumerate(triads):
    p = ti % 6
    rels = {}   # (x,y) -> judged sign from either judge, keyed per judge
    per_judge = {}
    for j in (2*p, 2*p+1):
        signs = {}
        for (a, b, m, d) in jt[j].get(ti, []):
            signs[(a, b)] = (norm(a, b, m), d)
        per_judge[j] = signs
    # per-judge cycle check: within judge j, orient the three relations; a strict cycle = violation
    for j, signs in per_judge.items():
        oriented = []
        for (a, b), (s, d) in signs.items():
            if s == 1: oriented.append((a, b))
            elif s == -1: oriented.append((b, a))
        if len(oriented) == 3:
            # cycle iff each node has exactly one in and one out
            outs = Counter(x for x, _ in oriented); ins = Counter(y for _, y in oriented)
            if all(outs[n] == 1 and ins[n] == 1 for n in (A, B, C)): cycle_viol += 1
            else: cycle_ok += 1
        elif oriented: partial += 1
    # cross-judge agreement on shared pairs (reverse presentation)
    j1, j2 = 2*p, 2*p+1
    for (a, b), (s1, d1) in per_judge.get(j1, {}).items():
        m2 = per_judge.get(j2, {}).get((b, a))
        if m2 is None: continue
        s2, d2 = m2
        cross_n += 1
        if s1 is None and s2 is None: cross_agree += 1
        elif s1 is not None and s2 is not None and s1 == -s2:
            cross_agree += 1
            # consistent directed edge -> graph
            if s1 == 1: succ[b].setdefault(a, []).append((d1, d2))
            elif s1 == -1: succ[a].setdefault(b, []).append((d1, d2))
        elif s1 == 0 and s2 == 0: cross_agree += 1
        else: cross_disagree += 1

print(f"per-judge triads fully oriented: {cycle_ok+cycle_viol}; CYCLE VIOLATIONS: {cycle_viol} "
      f"({cycle_viol/max(cycle_ok+cycle_viol,1):.0%}); partially oriented: {partial}")
print(f"cross-judge (reverse-cycle) pairs: {cross_n}; agree {cross_agree} ({cross_agree/max(cross_n,1):.0%})")

# distance agreement on cross-consistent edges
dd = [abs(d1-d2) for v in succ.values() for pairs in v.values() for (d1, d2) in pairs if d1 and d2]
if dd:
    print(f"felt-distance cross-judge: exact {sum(1 for x in dd if x==0)}/{len(dd)}, within-1 {sum(1 for x in dd if x<=1)}/{len(dd)}")

# chains
memo = {}; onpath = set()
def lf(n):
    if n in memo: return memo[n]
    if n in onpath: return []
    onpath.add(n); best = []
    for m in succ.get(n, {}):
        pth = lf(m)
        if len(pth) > len(best): best = pth
    onpath.discard(n); memo[n] = [n] + best
    return memo[n]
nodes = set(succ) | {m for v in succ.values() for m in v}
chains = sorted((lf(n) for n in nodes), key=len, reverse=True)
seen = set()
print("\nCHAINS (cross-judge-consistent edges only):")
for ch in chains:
    if len(ch) < 3: break
    if len(set(ch) & seen) > len(ch)//2: continue
    seen.update(ch)
    print(f"  [{len(ch)}] {''.join(ch)}")
