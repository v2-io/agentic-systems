"""Strengthening 3: the held-out ladder with glyph covariates (covs.py) and a composition-free others' feature
(lnb.block_features(composition_free=True)), on the sparse-interaction model (spx.py). Folds as fit_lnb.py (by item:
irt.heldout's; by block: over the block of the last glyph). Test items' features come from all other items; training
items' only from training items. 300 EM iterations at most, tolerance 1e-7 (the iteration count is recorded per fold).
  python3 ladder.py VARIANT   writes strengthening-3-logs/ladder-VARIANT.json
Variants:
  base         no covariates, no sequence features
  cov_shared   covariates, one coefficient vector for all minds
  cov          covariates, a vector per mind
  cov_oth      cov + others' sequence feature (composition-free)
  cov_oth_own  cov + others' (composition-free) + own sequence feature
  oth_own_cf   no covariates; others' (composition-free) + own
  cov_othp_own cov + others' (pooled, as strengthening 2) + own"""
import json, sys, time, numpy as np
import irt, lnb, spx, covs
V = sys.argv[1]
items, seq, S, N, X = irt.load("continue-stop")
C = covs.covs(items)
_, _, blk_last = lnb.block_features(items, S, N)
bn = sorted(set(blk_last)); rng = np.random.default_rng(0); bf = dict(zip(bn, rng.integers(0, 5, len(bn))))
folds = {"item": np.random.default_rng(0).integers(0, 5, len(S)), "block": np.array([bf[b] for b in blk_last])}
use_cov = V.startswith("cov"); shared = V == "cov_shared"
feats = V in ("cov_oth", "cov_oth_own", "oth_own_cf", "cov_othp_own"); own = V in ("cov_oth_own", "oth_own_cf", "cov_othp_own")
cf = V != "cov_othp_own"
out = {"variant": V, "folds": []}
for sc, fold in folds.items():
    for k in range(5):
        tr, te = fold != k, fold == k
        Fo, Ft, _ = lnb.block_features(items, S, N, grouping="blockset", composition_free=cf)
        Fo_tr, Ft_tr, _ = lnb.block_features(items, S, N, exclude_items=te, grouping="blockset", composition_free=cf)
        if not own: Fo = np.zeros_like(Fo); Fo_tr = np.zeros_like(Fo_tr)
        t0 = time.time()
        m = spx.SPX(feats=feats, cov=C[tr] if use_cov else None, cov_shared=shared, own=own).fit(
            S[tr], N[tr], X[tr], Fo_tr[tr], Ft_tr[tr], iters=300, C=C[tr] if use_cov else None)
        v = float(np.logaddexp.reduce(m.comp_loglik_full(S[te], N[te], X[te], Fo[te], Ft[te], C[te] if use_cov else None), 1).sum())
        out["folds"].append(dict(scheme=sc, fold=k, heldout=v, n=float(N[te].sum()), iters=m.iters, secs=round(time.time() - t0)))
        print(V, sc, k, round(v, 1), m.iters, flush=True)
for sc in folds:
    F_ = [f for f in out["folds"] if f["scheme"] == sc]
    out[sc] = sum(f["heldout"] for f in F_) / sum(f["n"] for f in F_)
    print(f"RESULT {V} {sc}: {out[sc]:.4f}", flush=True)
json.dump(out, open(f"strengthening-3-logs/ladder-{V}.json", "w"), indent=1)
