"""Is the repeat misfit selection on information outside the model? Survey seeds enter the tree as continuation votes
(era 'seed') and the early planner walked seeded sequences; the continue models exclude seed records. For each continue
answer: whether its context has a seed vote (a seed record with the same context). irtu prequential stops, observed vs
predicted, by group, era and seed vote; plus a combined table with same-sequence sheet-mates (sheetmates.py)."""
import sys, json, collections, numpy as np
sys.path.insert(0, "de-novo-2")
import irt, irtu, checks2, preq, lib, checks
from values import ckey
items, seq, S, N, X = irt.load("continue-stop")
P = json.load(open("de-novo-2/tau-pred.json"))["params"]; m = irtu.ModelU()
for k in ("alpha", "slope", "gamma", "tau", "pi", "eps", "dlt"): setattr(m, k, np.array(P[k]))
out = preq.score({None: checks2.AdaptU(m)}, None, items, seq, X)
recs, _ = lib.load()
seeded = set(tuple(r.get("context") or ()) for r in recs if r["era"] == "seed")
cell = collections.defaultdict(list)
for o in out:
    sd = tuple(items[o["i"]][1]) in seeded; era = "c001-c027" if o["rd"] <= 27 else "c028+"
    cell[(o["grp"], era, sd)].append((o["y"], o["p"]))
print("stops, observed / predicted (irtu prequential), by group, era, context has a seed vote")
for k in sorted(cell):
    L = cell[k]
    if len(L) < 30: continue
    o = sum(y for y, _ in L); e = sum(p for _, p in L); lo, hi = checks.band([p for _, p in L])
    print(f"  {k[0]:7s} {k[1]:10s} seeded {str(k[2]):5s} n={len(L):6d} obs {o:6d} / pred {e:8.1f} [{lo}-{hi}] ratio {o/e:.2f}")
