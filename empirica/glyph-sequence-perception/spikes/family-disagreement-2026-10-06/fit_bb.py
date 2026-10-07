"""Fit bb.BB on continue (all snapshot answers), report parameters, run checks.py, and 5-fold held-out log-lik on
irt.heldout's folds (rng seed 0)."""
import sys, time, numpy as np
import irt, bb, checks
items, seq, S, N, X = irt.load("continue-stop")
t0 = time.time(); m = bb.BB(fam=True).fit(S, N, X); print(f"fit: ll {m.ll:.1f} iters {m.iters} ({time.time()-t0:.0f}s)")
for j, mm in enumerate(irt.MINDS):
    print(f"   {mm:14s} alpha {m.alpha[j]:+.2f} slope {m.slope[j]:.2f} gamma {m.gamma[j]:+.2f} phi {np.exp(m.lphi[j]):.3f}")
checks.show(checks.run(m, items, seq, S, N, X, "beta-binomial, nonparametric b, familiarity"))
if "--heldout" in sys.argv:
    rng = np.random.default_rng(0); f = rng.integers(0, 5, len(S)); tot = 0.0; per = []
    for k in range(5):
        tr, te = f != k, f == k
        mk = bb.BB(fam=True).fit(S[tr], N[tr], X[tr])
        v = np.logaddexp.reduce(mk.comp_loglik(S[te], N[te], X[te]), 1).sum(); per.append(v); tot += v
    print(f"held-out per answer {tot / N.sum():.4f}; per fold {[round(v, 1) for v in per]}")
