"""De novo 3, check 8. c7's glyph covariates: how much of their gain is shared by all minds (one coefficient vector for
every mind) and how much is mind-specific (a vector per mind)? Pooled over the six minds with >= 3,000 answers; same
residual frame and group halves as c1/c7. Also prints the per-mind coefficients on 'contiguous' and 'single block'."""
import sys, collections, pickle, pathlib, math, numpy as np
HERE = pathlib.Path(__file__).resolve().parent; SP = HERE.parent
sys.path.insert(0, str(SP)); sys.path.insert(0, str(SP / "de-novo-2")); sys.path.insert(0, str(HERE))
import os; os.chdir(SP)
import irt, features as F
CACHE = pathlib.Path("/private/tmp/claude-505/-Users-josephwecker-v2-src-arch-asf-empirica-glyph-sequence-perception/2c3109cb-51be-4d66-937d-88f689223324/scratchpad/dn3/preq_irtu.pkl")
items, seq, S, N, X = irt.load("continue-stop"); out = pickle.load(open(CACHE, "rb"))
grp = [frozenset(F.block(g) for g in q[1]) for q in items]; gid = {g: k for k, g in enumerate(sorted(set(grp), key=repr))}
NAMES = ["contig", "mono", "oneblock", "nblocks", "len", "len2", "unfam", "laststep"]
def cov(i):
    c = [ord(g) for g in items[i][1]]; d = [b - a for a, b in zip(c, c[1:])]
    contig = float(all(x == 1 for x in d) or all(x == -1 for x in d)); mono = float(all(x > 0 for x in d) or all(x < 0 for x in d))
    nb = len(grp[i]); L = len(c)
    return [contig, mono, float(nb == 1), float(nb), L / 8, (L / 8) ** 2, float(X[i]), math.log1p(abs(d[-1])) / 10 if d else 0.0]
C = np.array([cov(i) for i in range(len(items))])
minds = [j for j in range(len(irt.MINDS)) if sum(1 for o in out if o["j"] == j) >= 3000]
L = [o for o in out if o["j"] in minds]
cv = np.array([C[o["i"]] for o in L]); jj = np.array([o["j"] for o in L])
off = np.log(np.clip([o["p"] for o in L], 1e-6, 1 - 1e-6)) - np.log(np.clip([1 - o["p"] for o in L], 1e-6, 1)); y = np.array([o["y"] for o in L], float)
half = np.array([gid[grp[o["i"]]] % 2 for o in L])
def fitlr(Zm, off, y):
    w = np.zeros(Zm.shape[1])
    for _ in range(40):
        p = 1 / (1 + np.exp(-(off + Zm @ w))); H = (Zm * (p * (1 - p))[:, None]).T @ Zm + 1e-4 * np.eye(Zm.shape[1]); w += np.linalg.solve(H, Zm.T @ (y - p))
    return w
def ll(Zm, off, y, w):
    p = np.clip(1 / (1 + np.exp(-(off + Zm @ w))), 1e-9, 1 - 1e-9); return float((y * np.log(p) + (1 - y) * np.log(1 - p)).sum())
one = np.ones((len(L), 1))
shared = np.c_[one, cv]
permind = np.concatenate([np.c_[one, cv] * (jj == j)[:, None] for j in minds], axis=1)
both = np.c_[shared, permind[:, :]]
for name, Zm in (("intercepts per mind only", np.concatenate([one * (jj == j)[:, None] for j in minds], axis=1)),
                 ("shared covariates (+ per-mind intercepts)", np.c_[np.concatenate([one * (jj == j)[:, None] for j in minds], axis=1), cv]),
                 ("per-mind covariates", permind)):
    g_ = 0.0
    for h in (0, 1):
        tr, te = half == h, half != h; w = fitlr(Zm[tr], off[tr], y[tr]); g_ += ll(Zm[te], off[te], y[te], w) - ll(Zm[te], off[te], y[te], np.zeros(Zm.shape[1]))
    print(f"{name:45s} held-out gain {g_:+.0f}")
w = fitlr(permind, off, y)
for k, j in enumerate(minds):
    ww = w[k * 9:(k + 1) * 9]
    print(f"   {irt.MINDS[j]:14s} " + "  ".join(f"{n} {v:+.2f}" for n, v in zip(["icpt"] + NAMES, ww)))
