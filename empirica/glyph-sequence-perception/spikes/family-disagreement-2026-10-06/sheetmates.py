"""Probing check (METHODOLOGY concern 1): does a continue answer's SHEET carry other contexts of the same sequence
(same set of Unicode blocks), and does that predict continuing beyond the item model? For every continue answer: the
number of its sheet-mates (other questions on the same sheet, same mind, same round) whose context spans the same block
set, and the irtu prequential prediction p (verifier's model). Reported per group (first / repeat) and era: observed
vs predicted stops with and without same-sequence sheet-mates, and the logistic coefficient of 'has same-sequence
sheet-mates' on top of logit p."""
import sys, json, collections, numpy as np
sys.path.insert(0, "de-novo-2")
import irt, irtu, checks2, preq, lib, features as F, checks
from values import ckey
items, seq, S, N, X = irt.load("continue-stop")
P = json.load(open("de-novo-2/tau-pred.json"))["params"]; m = irtu.ModelU()
for k in ("alpha", "slope", "gamma", "tau", "pi", "eps", "dlt"): setattr(m, k, np.array(P[k]))
out = preq.score({None: checks2.AdaptU(m)}, None, items, seq, X)
recs, _ = lib.load(); idx = {q: i for i, q in enumerate(items)}
bs = lambda c: frozenset(F.block(g) for g in c)
sheet = collections.defaultdict(list)                     # (round, mind, sid) -> [block sets of the questions]
ans_sheet = collections.defaultdict(list)                  # (item, mind, round) -> [sid]
for r in recs:
    if r["kind"] not in ("continue",) or not r.get("sid") or r["mind"] not in irt.MINDS: continue
    if (r.get("tags") or {}).get("variant") not in (None, "plain"): continue
    if r["outcome"] not in ("none", "continuation"): continue
    q = ckey(r)
    if q not in idx: continue
    rd = int(r["round"][1:]); sheet[(rd, r["mind"], r["sid"])].append((idx[q], bs(r["context"])))
    ans_sheet[(idx[q], r["mind"], rd)].append(r["sid"])
def mates(o):
    rd = o["rd"]; mm = irt.MINDS[o["j"]]; sids = ans_sheet.get((o["i"], mm, rd), [])
    if not sids: return None
    me = bs(items[o["i"]][1]); n = 0
    for sid in sids[:1]:
        for ii, b in sheet[(rd, mm, sid)]:
            if ii != o["i"] and b == me: n += 1
    return n
rows = []
for o in out:
    k = mates(o)
    if k is None: continue
    era = "c001-c027" if o["rd"] <= 27 else "c028+"
    rows.append((o["grp"], era, k > 0, o["y"], o["p"], irt.MINDS[o["j"]]))
cell = collections.defaultdict(list)
for g, e, h, y, p, mm in rows: cell[(g, e, h)].append((y, p))
print("stops, observed / predicted (irtu prequential), by group, era, same-sequence sheet-mates")
for k in sorted(cell):
    L = cell[k]; o = sum(y for y, _ in L); e = sum(p for _, p in L); lo, hi = checks.band([p for _, p in L])
    print(f"  {k[0]:7s} {k[1]:10s} sheet-mates same sequence: {str(k[2]):5s} n={len(L):6d} obs {o:6d} / pred {e:8.1f} [{lo}-{hi}] ratio {o/e:.2f}")
for grp in ("first", "repeat"):
    L = [(h, y, p) for g, e, h, y, p, mm in rows if g == grp]
    z = np.array([float(h) for h, _, _ in L]); y = np.array([y for _, y, _ in L], float); p = np.clip(np.array([p for _, _, p in L]), 1e-6, 1 - 1e-6)
    off = np.log(p / (1 - p)); w = 0.0
    for _ in range(30):
        q = 1 / (1 + np.exp(-(off + w * z))); w += (z * (y - q)).sum() / ((z * z * q * (1 - q)).sum() + 1e-9)
    q = 1 / (1 + np.exp(-(off + w * z))); se = 1 / np.sqrt((z * z * q * (1 - q)).sum() + 1e-9)
    print(f"  {grp}: logit coefficient of same-sequence sheet-mates on top of the model: {w:+.2f} ± {se:.2f} (share with mates {z.mean():.2f})")
