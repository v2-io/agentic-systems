#!/usr/bin/env python3
"""Tasks B and C on triad answers.

B (middle): among triads where >=2 families gave the SAME middle, how often does a ranker's similarity pick that
  middle? Prediction = the glyph left over when the least-similar pair is taken as the two ends (cp: median codepoint).
C (yield): does a ranker's coherence score for a triad separate triads minds order (>=2 families agree on a middle)
  from triads they don't (no middle given by >=2 families, and at least 2 families answered)? Reported as ROC AUC.
  Coherence = best chain score over the three possible middles: max_m  sim(a,m) + sim(m,b).

  python3 eval_triads.py [--gt r011] [--cat c1,c2] RANKER ...
"""
import argparse, collections, json
import numpy as np
from lib import DER
import rankers as RK

ap = argparse.ArgumentParser()
ap.add_argument("--gt", default="r011")
ap.add_argument("--cat", default=None)
ap.add_argument("rankers", nargs="+")
a = ap.parse_args()
G = json.load(open(DER / f"gt-{a.gt}.json"))

rows = []
for iid, T in G["triads"].items():
    fa = set(T["fams_answered"]) - {"muse"}
    if len(fa) < 2 or not all(g in RK.IDX for g in T["glyphs"]):
        continue
    if a.cat and not (T.get("category") and T["category"][-1] in a.cat.split(",")):
        continue
    cons = [m for m, fams in T["mid"].items() if len(set(fams) - {"muse"}) >= 2]
    mid = cons[0] if len(cons) == 1 else None
    rows.append((iid, T["glyphs"], mid, bool(cons)))

def auc(pos, neg):
    pos, neg = np.asarray(pos), np.asarray(neg)
    if not len(pos) or not len(neg):
        return float("nan")
    allv = np.concatenate([pos, neg]); r = allv.argsort().argsort().astype(float)
    # average ranks for ties
    _, inv, cnt = np.unique(allv, return_inverse=True, return_counts=True)
    sums = np.bincount(inv, weights=r); r = (sums / cnt)[inv]
    return float((r[:len(pos)].sum() - len(pos) * (len(pos) - 1) / 2) / (len(pos) * len(neg)))

def pair_sim(spec, x, y, cache={}):
    if spec == "cp":
        return -abs(ord(x) - ord(y))
    key = (spec, x)
    if key not in cache:
        cache[key] = RK.get(spec)(x)
    return float(cache[key][RK.IDX[y]])

npos = sum(1 for r in rows if r[3]); nmid = sum(1 for r in rows if r[2])
print(f"gt={a.gt} cat={a.cat or 'all'}: {len(rows)} triads with >=2 families answering; {npos} ordered by >=2 "
      f"families ({nmid} with a single consensus middle); {len(rows) - npos} not")
print(f"  {'ranker':44s} middle-acc  yield-AUC")
out = {}
for spec in a.rankers:
    hits, pos, neg = [], [], []
    for iid, g, mid, ordered in rows:
        s = {(x, y): pair_sim(spec, x, y) for x in g for y in g if x != y}
        sym = lambda x, y: (s[(x, y)] + s[(y, x)]) / 2
        chain, ends_gap = {}, {}
        for m in g:
            e1, e2 = [o for o in g if o != m]
            chain[m] = sym(e1, m) + sym(m, e2)
            ends_gap[m] = sym(e1, e2)                                       # similarity of the would-be ends
        pred = min(g, key=lambda m: (ends_gap[m], m))
        if mid:
            hits.append(pred == mid)
        (pos if ordered else neg).append(max(chain.values()))
    out[spec] = {"middle_acc": float(np.mean(hits)), "n_mid": len(hits), "yield_auc": auc(pos, neg)}
    print(f"  {spec:44s} {out[spec]['middle_acc']:.3f}      {out[spec]['yield_auc']:.3f}")
tag = a.gt + (f"-cat{a.cat.replace(',', '+')}" if a.cat else "")
p = DER / f"triads-{tag}.json"
old = json.load(open(p)) if p.exists() else {}
old.update(out); json.dump(old, open(p, "w"), ensure_ascii=False, indent=1)
