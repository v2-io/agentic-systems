"""Does a pure per-mind logit threshold reproduce the class pattern Abbott's correction showed (Sonnet's excess low on
non-monotone runs)? Additive model on cohere real runs: logit P(yes) = alpha_m + beta_i, beta_i from the other minds.
Per (mind, chart class): observed yes share vs predicted. If predicted matches observed, the class pattern is a
threshold, not a class-specific (chart-reliant) style."""
import collections
import lib, additive as AD, features as F
from values import ckey

recs, man = lib.load()
sig = AD.sig
ans = collections.defaultdict(lambda: collections.defaultdict(list)); glyph = {}
for r in recs:
    x = AD.outcome(r)
    if not x or x[0] != "cohere-yes" or x[1] is None: continue
    q = ckey(r); ans[q][r["mind"]].append(x[1]); glyph[q] = q[1]
minds = sorted({m for d in ans.values() for m in d}); alpha = {m: 0.0 for m in minds}
def fit_beta(d, excl=()):
    obs = [(alpha[m], y) for m, ys in d.items() if m not in excl for y in ys]
    if not obs: return None
    b = 0.0
    for _ in range(25):
        g = sum(y - sig(a + b) for a, y in obs); h = sum(sig(a + b) * (1 - sig(a + b)) for a, _ in obs) + 0.25
        b += (g - 0.25 * b) / h
    return b
for _ in range(6):
    beta = {q: fit_beta(d) for q, d in ans.items()}
    for m in minds:
        obs = [(beta[q], y) for q in ans for y in ans[q].get(m, [])]
        a = alpha[m]
        for _ in range(10):
            g = sum(y - sig(a + b) for b, y in obs); h = sum(sig(a + b) * (1 - sig(a + b)) for b, _ in obs) + 1e-9
            a += g / h
        alpha[m] = a
cell = collections.defaultdict(lambda: [0, 0.0, 0])
for q, d in ans.items():
    cc = F.chart_class(glyph[q])
    for m, ys in d.items():
        if len(d) < 2: continue
        b = fit_beta(d, excl=(m,)); p = sig(alpha[m] + b)
        for y in ys:
            k = cell[(m, cc)]; k[0] += y; k[1] += p; k[2] += 1
print("mind            class        n     observed  predicted (threshold only)")
for m in ("sonnet55", "opus55", "haiku45nt", "grok46", "gemini38flash"):
    for cc in ("contiguous", "monotone", "other"):
        o, p, n = cell[(m, cc)]
        if n: print(f"  {m:14s} {cc:11s} {n:5d}   {o/n:.3f}     {p/n:.3f}")

# ---- slope on the shared item scale vs class-specific offsets, per mind (logistic regression, Newton)
def logreg(X, y, iters=30, ridge=1e-3):
    k = len(X[0]); w = [0.0] * k
    for _ in range(iters):
        g = [0.0] * k; H = [[0.0] * k for _ in range(k)]
        for xi, yi in zip(X, y):
            p = sig(sum(a * b for a, b in zip(w, xi)))
            for j in range(k):
                g[j] += (yi - p) * xi[j]
                for l in range(k): H[j][l] += p * (1 - p) * xi[j] * xi[l]
        for j in range(k): H[j][j] += ridge; g[j] -= ridge * w[j]
        # solve H d = g (Gauss)
        A = [row[:] + [g[i]] for i, row in enumerate(H)]
        for c in range(k):
            piv = max(range(c, k), key=lambda r: abs(A[r][c])); A[c], A[piv] = A[piv], A[c]
            for r in range(k):
                if r != c:
                    f = A[r][c] / A[c][c]
                    A[r] = [a - f * b for a, b in zip(A[r], A[c])]
        d = [A[i][k] / A[i][i] for i in range(k)]
        w = [a + b for a, b in zip(w, d)]
    se = [(1 / H[i][i]) ** 0.5 for i in range(k)]   # rough (diagonal) standard errors
    return w, se
print("\nper mind: logit P(yes) = a + s*beta_others + c_contig + c_mono   (rough diagonal SEs)")
for m in ("sonnet55", "opus55", "haiku45nt", "grok46", "gemini38flash"):
    X, Y = [], []
    for q, d in ans.items():
        if m not in d or len(d) < 2: continue
        b = fit_beta(d, excl=(m,)); cc = F.chart_class(glyph[q])
        for y in d[m]:
            X.append([1.0, b, 1.0 if cc == "contiguous" else 0.0, 1.0 if cc == "monotone" else 0.0]); Y.append(y)
    w, se = logreg(X, Y)
    print(f"  {m:14s} n={len(Y):5d}  a={w[0]:+.2f}  s={w[1]:.2f}±{se[1]:.2f}  c_contig={w[2]:+.2f}±{se[2]:.2f}  c_mono={w[3]:+.2f}±{se[3]:.2f}")
