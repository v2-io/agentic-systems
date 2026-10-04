"""Signa pairwise: per judge, the 55-pair tournament (both orders, perp format)."""
import collections, itertools, sys
from common import *

RUNS_P = sorted(p.name for p in RUNS.iterdir() if p.name.startswith("signa-perp"))
LINES = set(SIGNA[:6]); CIRC = set(SIGNA[6:])

def seg(k):
    a, b = sorted(k, key=IDX.get)
    if a in LINES and b in LINES: return "lines"
    if a in CIRC and b in CIRC: return "circles"
    return "seam"

summary = {}
for run in RUNS_P:
    rows, pres = parsed_presentations(run, "consumer-signa-pairs.jsonl")
    pv = pair_verdicts(rows, pres)
    # presentation-level
    pc = collections.Counter(v[-1][0] for v in pres.values())
    c = collections.Counter(v[0] for v in pv.values())
    agree = collections.Counter(); dis = collections.Counter(); kinds = collections.defaultdict(collections.Counter)
    edges = []
    for k, (kind, w, _) in pv.items():
        s = seg(k)
        kinds[s][kind] += 1
        if kind == "cdir":
            a, b = sorted(k, key=IDX.get)  # a lower intended
            loser = a if w == b else b
            edges.append((loser, w))
            (agree if w == b else dis)[s] += 1
    # cycles among consistent-directed edges (3-cycles)
    E = set(edges)
    cyc = 0; tri_full = 0
    for x, y, z in itertools.combinations(SIGNA, 3):
        es = [(p, q) for p, q in E if {p, q} <= {x, y, z}]
        if len(es) == 3:
            tri_full += 1
            outdeg = collections.Counter(p for p, q in es)
            if max(outdeg.values()) == 1: cyc += 1
    # Copeland score (wins - losses on cdir edges) -> implied order
    sc = collections.Counter()
    for l, w in edges: sc[w] += 1; sc[l] -= 1
    order = sorted(SIGNA, key=lambda g: (sc[g], -IDX[g]))
    tau, n = kendall_tau(order, SIGNA)
    summary[run] = dict(pres=pc, pairs=c, agree=agree, dis=dis, kinds=kinds, cyc=(cyc, tri_full), copeland=order, tau=tau, edges=edges)
    print(f"\n=== {run}")
    print(" presentations:", dict(pc))
    print(" pair verdicts:", dict(c))
    for s in ("lines", "circles", "seam"):
        print(f"  {s:8s} n={sum(kinds[s].values()):2d}", dict(kinds[s]), f" cdir agree-with-author {agree[s]} / against {dis[s]}")
    print(f" 3-cycles among fully-directed triples: {cyc}/{tri_full}")
    print(" Copeland order (low->high):", "".join(order), f" tau vs author {tau:+.2f}")
    print(" score:", " ".join(f"{g}{sc[g]:+d}" for g in SIGNA))
    against = [(l, w) for l, w in edges if IDX[w] < IDX[l]]
    print(" edges against author (winner<loser in author's order):", " ".join(f"{w}>{l}" for l, w in against))
