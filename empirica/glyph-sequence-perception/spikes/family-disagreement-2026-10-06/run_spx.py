"""SPX (spx.py): held-out by item and by block (fit_lnb.py's folds), all-data fit, and strict prequential calibration
(features from earlier rounds only, lnb_prefix.py), with and without block-set features."""
import sys, pickle, numpy as np
import irt, lnb, preq, lnb_prefix, spx
items, seq, S, N, X = irt.load("continue-stop")
Fo, Ft, blk = lnb.block_features(items, S, N, grouping="blockset")
_, _, blk_last = lnb.block_features(items, S, N)
bn = sorted(set(blk_last)); rng = np.random.default_rng(0); bf = dict(zip(bn, rng.integers(0, 5, len(bn))))
folds = {"item": np.random.default_rng(0).integers(0, 5, len(S)), "block": np.array([bf[b] for b in blk_last])}
rows = preq.prefixes(items, seq, irt.MINDS); PFo, PFt = lnb_prefix.prefix_features(items, seq, rows)
for feats in (True, False):
    lab = "SPX" + (" + block-set features" if feats else " (no features)")
    for sc, fold in folds.items():
        tot = 0.0; per = []
        for k in range(5):
            tr, te = fold != k, fold == k
            Fo_tr, Ft_tr, _ = lnb.block_features(items, S, N, exclude_items=te, grouping="blockset")
            m = spx.SPX(feats=feats).fit(S[tr], N[tr], X[tr], Fo_tr[tr], Ft_tr[tr])
            v = np.logaddexp.reduce(m.comp_loglik_full(S[te], N[te], X[te], Fo[te], Ft[te]), 1).sum(); tot += v; per.append(round(v, 1))
        print(f"{lab}: held-out by {sc}: {tot / N.sum():.4f} per answer; total {tot:.1f}; folds {per}", flush=True)
    m = spx.SPX(feats=feats).fit(S, N, X, Fo, Ft, iters=300)
    print(f"{lab}: all-data ll {m.ll:.1f}, iters {m.iters}", flush=True)
    for j, mm in enumerate(irt.MINDS):
        print(f"   {mm:14s} a {m.alpha[j]:+.2f} s {m.slope[j]:.2f} g {m.gamma[j]:+.2f}" + (f" lam {m.lam[j]:+.2f} kap {m.kap[j]:+.2f}" if feats else "")
              + f"  pi {m.pi[j]:.3f}  Beta({m.a[j]}, {m.b[j]})", flush=True)
    if feats: pickle.dump((m, Fo, Ft), open("/private/tmp/claude-505/-Users-josephwecker-v2-src-arch-asf-empirica-glyph-sequence-perception/2c3109cb-51be-4d66-937d-88f689223324/scratchpad/spx_all.pkl", "wb"))
    preq.report(preq.score({None: spx.RowAdapter(m, PFo, PFt)}, None, items, seq, X), lab + ", strict prequential (features from earlier rounds)")
