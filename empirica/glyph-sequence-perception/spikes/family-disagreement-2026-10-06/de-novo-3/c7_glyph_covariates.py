"""De novo 3, check 7. Is the 'mind-specific sequence effect' a new structure, or the minds' known differing responses
to properties computable from the glyphs alone (a chart walk; one block or several; length; familiarity), which the
item models carry only as one familiarity covariate? Per mind, residual frame of c1 (irtu prequential offset), held
out by halves of block-set groups: gains of glyph covariates alone, + the others' group feature, + the mind's own.
Covariates, from the context's code points: contiguous (every step +1, or every step -1), monotone, single block,
number of blocks, length (2..8 one-hot-ish as linear + square), unfamiliar last glyph (irt's x), last step size
(log |dcp|), and the block of the last glyph's size class (log number of assigned code points is not available here,
so omitted)."""
import sys, collections, pickle, pathlib, math, numpy as np
HERE = pathlib.Path(__file__).resolve().parent; SP = HERE.parent
sys.path.insert(0, str(SP)); sys.path.insert(0, str(SP / "de-novo-2"))
import os; os.chdir(SP)
import irt, features as F
CACHE = pathlib.Path("/private/tmp/claude-505/-Users-josephwecker-v2-src-arch-asf-empirica-glyph-sequence-perception/2c3109cb-51be-4d66-937d-88f689223324/scratchpad/dn3/preq_irtu.pkl")
items, seq, S, N, X = irt.load("continue-stop"); out = pickle.load(open(CACHE, "rb"))
grp = [frozenset(F.block(g) for g in q[1]) for q in items]; gid = {g: k for k, g in enumerate(sorted(set(grp), key=repr))}
def cov(i):
    c = [ord(g) for g in items[i][1]]; d = [b - a for a, b in zip(c, c[1:])]
    contig = float(all(x == 1 for x in d) or all(x == -1 for x in d)); mono = float(all(x > 0 for x in d) or all(x < 0 for x in d))
    nb = len(grp[i]); L = len(c)
    return [contig, mono, float(nb == 1), float(nb), L / 8, (L / 8) ** 2, float(X[i]), math.log1p(abs(d[-1])) / 10 if d else 0.0]
C = np.array([cov(i) for i in range(len(items))])
Go = collections.defaultdict(lambda: np.zeros(2)); Io = collections.defaultdict(lambda: np.zeros(2))
for o in out:
    v = np.array([o["y"] - o["p"], 1.0]); Go[(grp[o["i"]], o["j"])] += v; Io[(o["i"], o["j"])] += v
M = len(irt.MINDS)
def gfeat(i, j):
    g = grp[i]; own = Go[(g, j)] - Io[(i, j)]
    oth = sum((Go[(g, jj)] - Io[(i, jj)] for jj in range(M) if jj != j), np.zeros(2))
    f = lambda a: a[0] / a[1] if a[1] > 0 else 0.0
    return f(own), f(oth)
def fitlr(Zm, off, y):
    w = np.zeros(Zm.shape[1])
    for _ in range(40):
        p = 1 / (1 + np.exp(-(off + Zm @ w))); H = (Zm * (p * (1 - p))[:, None]).T @ Zm + 1e-4 * np.eye(Zm.shape[1]); w += np.linalg.solve(H, Zm.T @ (y - p))
    return w
def ll(Zm, off, y, w):
    p = np.clip(1 / (1 + np.exp(-(off + Zm @ w))), 1e-9, 1 - 1e-9); return float((y * np.log(p) + (1 - y) * np.log(1 - p)).sum())
tot = collections.Counter()
for j, mm in enumerate(irt.MINDS):
    L = [o for o in out if o["j"] == j]
    if len(L) < 3000: continue
    gf = np.array([gfeat(o["i"], j) for o in L]); cv = np.array([C[o["i"]] for o in L]); one = np.ones((len(L), 1))
    off = np.log(np.clip([o["p"] for o in L], 1e-6, 1 - 1e-6)) - np.log(np.clip([1 - o["p"] for o in L], 1e-6, 1)); y = np.array([o["y"] for o in L], float)
    half = np.array([gid[grp[o["i"]]] % 2 for o in L])
    sets = {"oth": np.c_[one, gf[:, 1]], "oth+own": np.c_[one, gf], "cov": np.c_[one, cv], "cov+oth": np.c_[one, cv, gf[:, 1]], "cov+oth+own": np.c_[one, cv, gf]}
    row = {}
    for name, Zm in sets.items():
        g_ = 0.0
        for h in (0, 1):
            tr, te = half == h, half != h; w = fitlr(Zm[tr], off[tr], y[tr]); g_ += ll(Zm[te], off[te], y[te], w) - ll(Zm[te], off[te], y[te], np.zeros(Zm.shape[1]))
        row[name] = g_; tot[name] += g_
    print(f"{mm:14s} n={len(L):6d}  " + "  ".join(f"{k} {v:+.0f}" for k, v in row.items()) + f"   own beyond oth {row['oth+own']-row['oth']:+.0f}; own beyond cov+oth {row['cov+oth+own']-row['cov+oth']:+.0f}", flush=True)
print("TOTAL " + "  ".join(f"{k} {v:+.0f}" for k, v in tot.items()) + f"   own beyond oth {tot['oth+own']-tot['oth']:+.0f}; own beyond cov+oth {tot['cov+oth+own']-tot['cov+oth']:+.0f}")
