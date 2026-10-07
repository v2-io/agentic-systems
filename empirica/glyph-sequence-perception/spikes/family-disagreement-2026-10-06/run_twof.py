"""Fit 1-factor and 2-factor models (no features, then block-set features) on all snapshot continue answers; loadings;
held-out by item (irt.heldout folds); prequential same-round pair calibration (features from earlier rounds)."""
import sys, numpy as np
import irt, lnb, preq, lnb_prefix, twof, checks
items, seq, S, N, X = irt.load("continue-stop")
Fo, Ft, _ = lnb.block_features(items, S, N, grouping="blockset")
rows = preq.prefixes(items, seq, irt.MINDS); PFo, PFt = lnb_prefix.prefix_features(items, seq, rows)
fold = np.random.default_rng(0).integers(0, 5, len(S))
for feats in (False, True):
    for nf in (1, 2):
        lab = f"{nf}-factor{' + block-set features' if feats else ''}"
        m = twof.TwoF(feats=feats, nf=nf).fit(S, N, X, Fo, Ft)
        print(f"== {lab}: ll {m.ll:.1f} iters {m.iters}", flush=True)
        for j, mm in enumerate(irt.MINDS):
            print(f"   {mm:14s} a {m.alpha[j]:+.2f} s {m.slope[j]:.2f} t {m.t[j]:+.2f} g {m.gamma[j]:+.2f}" + (f" lam {m.lam[j]:+.2f} kap {m.kap[j]:+.2f}" if feats else ""), flush=True)
        if "--heldout" in sys.argv:
            tot = 0.0
            for k in range(5):
                tr, te = fold != k, fold == k
                Fo_tr, Ft_tr, _ = lnb.block_features(items, S, N, exclude_items=te, grouping="blockset")
                mk = twof.TwoF(feats=feats, nf=nf).fit(S[tr], N[tr], X[tr], Fo_tr[tr], Ft_tr[tr])
                tot += np.logaddexp.reduce(mk.comp_loglik_full(S[te], N[te], X[te], Fo[te], Ft[te]), 1).sum()
            print(f"   held-out by item: {tot / N.sum():.4f} per answer", flush=True)
        # same-round pairs, prequential: posterior from the item's earlier rounds, features from earlier rounds
        Sx = np.array([r[2] for r in rows]); Nx = np.array([r[3] for r in rows]); Xx = np.array([X[r[0]] for r in rows])
        L = m.comp_loglik_full(Sx, Nx, Xx, PFo, PFt); R = np.exp(L - np.logaddexp.reduce(L, 1)[:, None])
        cells = {}
        for rk, (i, rd, Sp, Np, ans) in enumerate(rows):
            js = [(j, y) for j, y in ans]
            q = {j: m.cond_next_row(PFo[rk], PFt[rk], X[i], j) for j, _ in js}
            for u in range(len(js)):
                for v in range(u + 1, len(js)):
                    (ja, ya), (jb, yb) = js[u], js[v]
                    if ja == jb: continue
                    a, b = min(ja, jb), max(ja, jb); pa, pb = q[a], q[b]
                    cells.setdefault((a, b), []).append((int(ya != yb), float(R[rk] @ (pa * (1 - pb) + pb * (1 - pa)))))
        bad = 0
        for (a, b), Lp in sorted(cells.items()):
            if len(Lp) < 300: continue
            o = sum(d for d, _ in Lp); e = sum(p for _, p in Lp); lo, hi = checks.band([p for _, p in Lp])
            f = "" if lo <= o <= hi else "  <--"; bad += bool(f)
            print(f"    {irt.MINDS[a]:14s}/{irt.MINDS[b]:14s} n={len(Lp):5d} obs {o:5d} / pred {e:7.1f} [{lo}-{hi}] ratio {o/e:.2f}{f}", flush=True)
        print(f"   pairs outside band: {bad}", flush=True)
