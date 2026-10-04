"""Note: in a cyclically arranged orientation set (AB, BC, CA) every 3-cycle is, by construction, the pattern
'same slot wins all three' — so the registered cycle rate cannot distinguish intransitivity from position
preference. Order-debiased transitivity: use each pair's two presentations (one per orientation set; opposite
slot orders) and keep only pairs that are consistent-directed (same winner in both orders). Among triads whose
three pairs are ALL consistent-directed, count 3-cycles. A pure position strategy yields no consistent pairs;
random-but-order-stable preferences yield 25% cycles."""
import collections
from common import *
out = [f"{'judge':22s} {'triads all-3-cdir':>17s} {'cycles':>6s} {'rate':>5s}  {'[wilson]':>13s}   registered-style cycle rate"]
reg = {}
for run in runs("triads-perp"):
    j = judge_of(run)
    rows, pres = parsed_presentations(run, "triads.jsonl")
    last = {p: v[-1] for p, v in pres.items()}
    byp = collections.defaultdict(dict); tri = collections.defaultdict(set)
    for pid, st in rows.items():
        k = frozenset((st["a"], st["b"])); byp[(st["triad"], k)][st["oset"]] = last.get(pid); tri[st["triad"]].add(k)
    n = c = 0
    for t, ks in tri.items():
        wins = []
        ok = True
        for k in ks:
            d = byp[(t, k)]; v0, v1 = d.get(0), d.get(1)
            if not (v0 and v1 and v0[0] == "dir" and v1[0] == "dir" and v0[1] == v1[1]): ok = False; break
            wins.append(v0[1])
        if ok and len(ks) == 3:
            n += 1; c += max(collections.Counter(wins).values()) == 1
    # registered style
    sets = collections.defaultdict(list)
    for pid, st in rows.items(): sets[(st["triad"], st["oset"])].append(pid)
    full = cyc = 0
    for key, pids in sets.items():
        vs = [last.get(p) for p in pids]
        if len(pids) == 3 and all(v and v[0] == "dir" for v in vs):
            full += 1; cyc += max(collections.Counter(v[1] for v in vs).values()) == 1
    lo, hi = wilson(c, n)
    out.append(f"{j:22s} {n:17d} {c:6d} {c/n if n else float('nan'):5.2f}  [{lo:.2f},{hi:.2f}]   {cyc}/{full}={cyc/full if full else float('nan'):.2f}")
txt = "\n".join(out); print(txt)
open(ROOT / "reading/tables/triad-transitivity.txt", "w").write(__doc__ + "\n" + txt + "\n")
