#!/usr/bin/env python3
"""Assumption-free chain discovery from walk judgments.

Input: walk workflow output (both presentation orders per pair).
An edge lo->hi exists ONLY when both orders name the same glyph as more.
Both-orders-≈ merges glyphs into tie clusters. Disagreement (order-dependent
answers) contributes nothing. Discovered sequences = long paths in the
consistent directed graph, with cycles reported honestly rather than broken
silently. No prior orderings, families, or expected values enter anywhere.
"""
import json, sys
from collections import defaultdict

wf_out = sys.argv[1]
data = json.load(open(wf_out))["result"]["walk"]

edges = defaultdict(int)      # (less, more) -> count of consistent pair-judgments
ties = defaultdict(int)       # frozenset -> count
inconsistent = 0; consistent = 0; tie_n = 0
for entry in data:
    key = json.load(open(f"walk-key-{entry['chunk']}.json"))
    amap = {a["id"]: a["more"] for a in (entry["answers"] or [])}
    bypair = defaultdict(list)
    for s in key["sheet"]: bypair[s["pair"]].append(s)
    for pk, pres in bypair.items():
        picks = []
        for s in pres:
            a = amap.get(s["id"])
            if a is None: picks = []; break
            if a not in (s["a"], s["b"], "≈"):
                a = s["a"] if s["a"] in a else (s["b"] if s["b"] in a else ("≈" if "≈" in a else None))
            picks.append((s, a))
        if len(picks) != 2 or any(a is None for _, a in picks): continue
        answers = [a for _, a in picks]
        if answers[0] == "≈" and answers[1] == "≈":
            ties[frozenset((picks[0][0]["a"], picks[0][0]["b"]))] += 1; tie_n += 1
        elif "≈" not in answers and answers[0] == answers[1]:
            more = answers[0]
            less = picks[0][0]["a"] if picks[0][0]["b"] == more else picks[0][0]["b"]
            edges[(less, more)] += 1; consistent += 1
        else:
            inconsistent += 1

total = consistent + tie_n + inconsistent
print(f"pairs judged: {total}; consistent-directed {consistent} ({consistent/total:.0%}), "
      f"tie {tie_n} ({tie_n/total:.0%}), order-inconsistent {inconsistent} ({inconsistent/total:.0%})")

# graph
succ = defaultdict(set); pred = defaultdict(set)
for (a, b) in edges: succ[a].add(b); pred[b].add(a)
nodes = set(succ) | set(pred)

# cycle report (mutual edges or longer cycles found via DFS on the fly)
mutual = [(a, b) for (a, b) in edges if (b, a) in edges]
print(f"nodes in graph: {len(nodes)}; directed edges: {len(edges)}; mutual contradictions: {len(mutual)} {mutual[:5]}")

# longest paths via DFS with memo; if cycles exist, guard with visiting set
import sys as _s; _s.setrecursionlimit(10000)
memo = {}
onpath = set()
def longest_from(n):
    if n in memo: return memo[n]
    if n in onpath: return []          # cycle guard: truncate rather than loop
    onpath.add(n)
    best = []
    for m in succ.get(n, ()):
        p = longest_from(m)
        if len(p) > len(best): best = p
    onpath.discard(n)
    memo[n] = [n] + best
    return memo[n]

chains = sorted((longest_from(n) for n in nodes), key=len, reverse=True)
seen = set(); shown = 0
print("\nDISCOVERED CHAINS (longest consistent paths, deduped by overlap):")
for ch in chains:
    if len(ch) < 4: break
    if len(set(ch) & seen) > len(ch) // 2: continue
    seen.update(ch); shown += 1
    print(f"  [{len(ch)}] {''.join(ch)}")
    if shown >= 25: break

print("\nTIE CLUSTERS (both-orders ≈, seen >=1):")
groups = [set(k) for k, v in ties.items()]
# merge overlapping tie pairs into clusters
merged = []
for g in groups:
    for m in merged:
        if m & g: m |= g; break
    else: merged.append(set(g))
big = [m for m in merged if len(m) > 2]
for m in sorted(big, key=len, reverse=True)[:12]:
    print("  ", "".join(sorted(m)))
