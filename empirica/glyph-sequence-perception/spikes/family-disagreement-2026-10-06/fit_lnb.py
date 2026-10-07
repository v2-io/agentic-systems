"""Held-out comparison of 2mf, LNB without block features (lnb0) and LNB with them (lnb), on continue.
  by item  : irt.heldout's folds (rng seed 0 over items) -- the criterion written down before fitting (NOTES)
  by block : 5 folds over Unicode blocks (rng seed 0 over block names) -- stricter, added after: training never sees a
             test block, and features never use test items' answers for training items.
Test items' features come from all other items (never their own answers)."""
import sys, time, numpy as np
import irt, lnb
items, seq, S, N, X = irt.load("continue-stop")
Fo, Ft, blk = lnb.block_features(items, S, N)
bn = sorted(set(blk)); rng = np.random.default_rng(0); bf = dict(zip(bn, rng.integers(0, 5, len(bn))))
folds = {"item": np.random.default_rng(0).integers(0, 5, len(S)), "block": np.array([bf[b] for b in blk])}
for name in sys.argv[1:] or ["item", "block"]:
    fold = folds[name]; res = {"2mf": 0.0, "lnb0": 0.0, "lnb": 0.0}; per = {k: [] for k in res}
    for k in range(5):
        tr, te = fold != k, fold == k
        Fo_tr, Ft_tr, _ = lnb.block_features(items, S, N, exclude_items=te)
        m0 = irt.Model(2, True, True).fit(S[tr], N[tr], X[tr]); v = np.logaddexp.reduce(m0.comp_loglik(S[te], N[te], X[te]), 1).sum()
        res["2mf"] += v; per["2mf"].append(round(v, 1)); print(f"[{name}] fold {k} 2mf: {v:.1f}", flush=True)
        for key, fe in (("lnb0", False), ("lnb", True)):
            t0 = time.time(); m = lnb.LNB(feats=fe).fit(S[tr], N[tr], X[tr], Fo_tr[tr], Ft_tr[tr])
            v = np.logaddexp.reduce(m.comp_loglik_full(S[te], N[te], X[te], Fo[te], Ft[te]), 1).sum()
            res[key] += v; per[key].append(round(v, 1)); print(f"[{name}] fold {k} {key}: {v:.1f} ({time.time()-t0:.0f}s, iters {m.iters})", flush=True)
    for key in res: print(f"RESULT [{name}] {key:5s}: {res[key]/N.sum():.4f} per answer; total {res[key]:.1f}; folds {per[key]}", flush=True)
print("DONE", flush=True)
