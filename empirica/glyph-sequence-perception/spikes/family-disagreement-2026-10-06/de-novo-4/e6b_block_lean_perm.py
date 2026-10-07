# e6 with a permutation reference instead of per-block sample variances (zero-variance blocks made e6's Q unreliable).
# S = sum_b n_b (d_b - dbar)^2 over blocks with >= 5 paired one-block contexts; block labels permuted within class.
import sys, collections
sys.path.insert(0, ".")
from e5_chart_given import first, cls, F
import numpy as np
rng = np.random.default_rng(3)
for a, b in (("sonnet55", "grok46"), ("sonnet55", "haiku45nt"), ("haiku45nt", "grok46"), ("sonnet55", "gemini38flash"), ("opus55", "grok46")):
    out = []
    for c in ("cg", "cn", "mono", "oth"):
        lab, x = [], []
        for q, d in first.items():
            if a in d and b in d and cls[q] == c:
                bl = {F.block(g) for g in q[1]}
                if len(bl) == 1: lab.append(bl.pop()); x.append(int(d[b]) - int(d[a]))
        cnt = collections.Counter(lab); keep = [i for i, l in enumerate(lab) if cnt[l] >= 5]
        if len(keep) < 20: out.append(f"{c}: thin"); continue
        lab = np.array([lab[i] for i in keep]); x = np.array([x[i] for i in keep], float)
        u, inv = np.unique(lab, return_inverse=True); nb = np.bincount(inv)
        def S(xx):
            m = np.bincount(inv, weights=xx) / nb; return float((nb * (m - xx.mean()) ** 2).sum())
        s0 = S(x); sp = np.array([S(rng.permutation(x)) for _ in range(500)])
        out.append(f"{c}: blocks {len(u)}, ctx {len(x)}, S/E[S|perm] {s0/sp.mean():5.2f} (perm 99% {np.quantile(sp,.99)/sp.mean():.2f})")
    print(f"{a} vs {b}:\n   " + "\n   ".join(out))
