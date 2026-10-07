"""Within-item contrast for the sheet-mate effect (de-novo-feedback-3 §3): the same context and the same mind, answered
on at least one sheet WITH other contexts of the same block set and at least one WITHOUT. Per (item, mind): stop share
with mates minus without; mean over pairs, with a sign test and a paired bootstrap. Sequence strength is held fixed by
construction (same item); what differs is the sheet (and the round)."""
import collections, numpy as np
import irt, lib, features as F
from values import ckey
items, seq, S, N, X = irt.load("continue-stop")
idx = {q: i for i, q in enumerate(items)}
recs, _ = lib.load()
bs = lambda c: frozenset(F.block(g) for g in c)
sheet = collections.defaultdict(list); ans = []
for r in recs:
    if r["kind"] != "continue" or r["mind"] not in irt.MINDS or not r.get("sid"): continue
    if (r.get("tags") or {}).get("variant") not in (None, "plain") or r["outcome"] not in ("none", "continuation"): continue
    q = ckey(r)
    if q not in idx: continue
    sheet[(r["round"], r["mind"], r["sid"])].append(idx[q]); ans.append((idx[q], r["mind"], r["round"], r["sid"], r["outcome"] == "none"))
cell = collections.defaultdict(lambda: {True: [], False: []})
for i, mm, rd, sid, y in ans:
    me = bs(items[i][1]); mates = any(ii != i and bs(items[ii][1]) == me for ii in sheet[(rd, mm, sid)])
    cell[(i, mm)][mates].append(y)
diffs = collections.defaultdict(list)
for (i, mm), d in cell.items():
    if d[True] and d[False]: diffs[mm].append(np.mean(d[True]) - np.mean(d[False]))
rng = np.random.default_rng(0); allv = []
for mm, v in sorted(diffs.items()):
    v = np.array(v); allv += list(v)
    if len(v) < 10: print(f"  {mm:14s} pairs {len(v)} (too few)"); continue
    bs_ = [rng.choice(v, len(v)).mean() for _ in range(2000)]
    print(f"  {mm:14s} pairs {len(v):4d}  mean stop(with mates) - stop(without) {v.mean():+.3f}  95% [{np.quantile(bs_, .025):+.3f}, {np.quantile(bs_, .975):+.3f}]  (+ {np.sum(v > 0)} / - {np.sum(v < 0)} / 0 {np.sum(v == 0)})")
v = np.array(allv); bs_ = [rng.choice(v, len(v)).mean() for _ in range(2000)]
print(f"  all minds      pairs {len(v):4d}  mean {v.mean():+.3f}  95% [{np.quantile(bs_, .025):+.3f}, {np.quantile(bs_, .975):+.3f}]  (+ {np.sum(v > 0)} / - {np.sum(v < 0)} / 0 {np.sum(v == 0)})")
