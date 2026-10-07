"""One held-out fold of LNB: --scheme item|block (fit_lnb.py's folds), --fold k, --grouping block|blockset, --feats 0|1.
Prints and writes the fold's held-out log-likelihood as JSON (to --out)."""
import argparse, json, time, numpy as np
import irt, lnb
ap = argparse.ArgumentParser(); ap.add_argument("--scheme"); ap.add_argument("--fold", type=int); ap.add_argument("--grouping", default="block")
ap.add_argument("--feats", type=int, default=1); ap.add_argument("--oth-only", action="store_true"); ap.add_argument("--out"); a = ap.parse_args()
items, seq, S, N, X = irt.load("continue-stop")
_, _, blk = lnb.block_features(items, S, N)                      # folds always by block of the last glyph
bn = sorted(set(blk)); rng = np.random.default_rng(0); bf = dict(zip(bn, rng.integers(0, 5, len(bn))))
fold = np.random.default_rng(0).integers(0, 5, len(S)) if a.scheme == "item" else np.array([bf[b] for b in blk])
tr, te = fold != a.fold, fold == a.fold
Fo, Ft, _ = lnb.block_features(items, S, N, grouping=a.grouping)
Fo_tr, Ft_tr, _ = lnb.block_features(items, S, N, exclude_items=te, grouping=a.grouping)
if a.oth_only: Fo = np.zeros_like(Fo); Fo_tr = np.zeros_like(Fo_tr)        # shared sequence effect only: lam has nothing to fit
t0 = time.time(); m = lnb.LNB(feats=bool(a.feats)).fit(S[tr], N[tr], X[tr], Fo_tr[tr], Ft_tr[tr])
v = float(np.logaddexp.reduce(m.comp_loglik_full(S[te], N[te], X[te], Fo[te], Ft[te]), 1).sum())
r = dict(vars(a), heldout=v, n_answers_test=float(N[te].sum()), iters=m.iters, secs=round(time.time() - t0))
print(json.dumps(r)); json.dump(r, open(a.out, "w"))
