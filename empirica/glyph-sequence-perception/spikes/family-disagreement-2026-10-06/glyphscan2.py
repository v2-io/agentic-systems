"""glyphscan.py redone per de-novo-feedback-1 §5: one answer per (item, mind, sheet); the item's position from minds of
OTHER FAMILIES only (so a family-shared effect isn't diluted); the calibrated 2PL mixture (irt.py, 2m) supplies each
mind's P(commit); per (glyph, mind) the residual sum and z; and an empirical null: the distribution of z over all cells,
whose tails say what a z of -3.9 means here."""
import collections, math
import numpy as np
import irt

items, seq, S, N, X = irt.load("triad-commit", one_per_sheet=True)
m = irt.Model(2, True, False).fit(S, N, X)
M = irt.MINDS; fam = lambda mm: "claude" if mm.startswith(("sonnet", "opus", "haiku")) else ("grok" if mm.startswith("grok") else "gemini")
acc = collections.defaultdict(lambda: [0.0, 0.0, 0])
for i, q in enumerate(items):
    for j, mm in enumerate(M):
        if N[i, j] == 0: continue
        keep = [k for k, m2 in enumerate(M) if fam(m2) != fam(mm)]
        So = np.zeros_like(S[i:i+1]); No = np.zeros_like(N[i:i+1]); So[0, keep] = S[i, keep]; No[0, keep] = N[i, keep]
        L = m.comp_loglik(So, No, X[i:i+1])[0]; r = np.exp(L - np.logaddexp.reduce(L))
        p = float(r @ m.comp_probs(X[i])[:, j])
        for g in set(q[1]):
            a = acc[(g, mm)]; a[0] += S[i, j] - N[i, j] * p; a[1] += N[i, j] * p * (1 - p); a[2] += int(N[i, j])
rows = sorted(((a[0] / math.sqrt(a[1]) if a[1] > 0 else 0.0), g, mm, a[2]) for (g, mm), a in acc.items() if a[2] >= 8)
zs = np.array([z for z, *_ in rows])
print(f"cells {len(rows)}; empirical z quantiles 0.5% {np.quantile(zs, 0.005):.2f}, 1% {np.quantile(zs, 0.01):.2f}, 5% {np.quantile(zs, 0.05):.2f}, 50% {np.median(zs):.2f}; sd {zs.std():.2f}")
for k, (z, g, mm, n) in enumerate(rows[:15]):
    print(f"  rank {k+1:3d}  z={z:6.2f}  {g} U+{ord(g):04X} {mm:14s} n={n}")
for z, g, mm, n in rows:
    if g == "▁": print(f"  ▁ {mm:14s} z={z:6.2f} n={n}  rank {sorted(zs).index(z)+1} of {len(zs)}")
