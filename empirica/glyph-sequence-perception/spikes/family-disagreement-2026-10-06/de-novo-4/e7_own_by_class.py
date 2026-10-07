# Verifier 3's c7 frame (irtu prequential offsets, cached; halves of block-set groups), extended: the 'own beyond
# covariates + others' gain split by the class of the answer predicted (cg / cn / mono / oth, as e5), and a variant whose
# own/others features are built only from contexts of OTHER classes in the block set (is the lean block-wide, or
# chart-walk appetite in that block?).
import sys, collections, pickle, pathlib, math, os, numpy as np
SP = pathlib.Path("/Users/josephwecker-v2/src/arch/asf/empirica/glyph-sequence-perception/spikes/family-disagreement-2026-10-06")
ROOT = SP.parents[1]
sys.path.insert(0, str(SP)); sys.path.insert(0, str(SP / "de-novo-2")); sys.path.insert(0, str(ROOT / "catalog"))
os.chdir(SP)
import irt, features as F, given_walk as GW
CACHE = pathlib.Path("/private/tmp/claude-505/-Users-josephwecker-v2-src-arch-asf-empirica-glyph-sequence-perception/2c3109cb-51be-4d66-937d-88f689223324/scratchpad/dn3/preq_irtu.pkl")
items, seq, S, N, X = irt.load("continue-stop"); out = pickle.load(open(CACHE, "rb"))
grp = [frozenset(F.block(g) for g in q[1]) for q in items]; gid = {g: k for k, g in enumerate(sorted(set(grp), key=repr))}
def klass(q):
    g = list(q[1]); cc = F.chart_class(g)
    if cc == "contiguous": return "cn" if not GW.is_given(GW.classify_cached(tuple(g), 2)) else "cg"
    return {"monotone": "mono", "other": "oth"}[cc]
K = [klass(q) for q in items]
def cov(i):
    c = [ord(g) for g in items[i][1]]; d = [b - a for a, b in zip(c, c[1:])]
    contig = float(all(x == 1 for x in d) or all(x == -1 for x in d)); mono = float(all(x > 0 for x in d) or all(x < 0 for x in d))
    nb = len(grp[i]); L = len(c)
    return [contig, mono, float(nb == 1), float(nb), L / 8, (L / 8) ** 2, float(X[i]), math.log1p(abs(d[-1])) / 10 if d else 0.0, float(K[i] == "cg")]
C = np.array([cov(i) for i in range(len(items))])
M = len(irt.MINDS)
def build(crossclass):
    Go = collections.defaultdict(lambda: np.zeros(2)); Io = collections.defaultdict(lambda: np.zeros(2))
    for o in out:
        v = np.array([o["y"] - o["p"], 1.0]); key = (grp[o["i"]], o["j"]) + ((K[o["i"]],) if crossclass else ())
        Go[key] += v; Io[(o["i"], o["j"])] += v
    def gfeat(i, j):
        g = grp[i]
        if crossclass:   # sum over the block set's OTHER classes only (the context itself is never in them)
            own = sum((Go[(g, j, k)] for k in ("cg", "cn", "mono", "oth") if k != K[i]), np.zeros(2))
            oth = sum((Go[(g, jj, k)] for jj in range(M) if jj != j for k in ("cg", "cn", "mono", "oth") if k != K[i]), np.zeros(2))
        else:
            own = Go[(g, j)] - Io[(i, j)]; oth = sum((Go[(g, jj)] - Io[(i, jj)] for jj in range(M) if jj != j), np.zeros(2))
        f = lambda a: a[0] / a[1] if a[1] > 0 else 0.0
        return f(own), f(oth)
    return gfeat
def fitlr(Zm, off, y):
    w = np.zeros(Zm.shape[1])
    for _ in range(40):
        p = 1 / (1 + np.exp(-(off + Zm @ w))); H = (Zm * (p * (1 - p))[:, None]).T @ Zm + 1e-4 * np.eye(Zm.shape[1]); w += np.linalg.solve(H, Zm.T @ (y - p))
    return w
def llv(Zm, off, y, w):
    p = np.clip(1 / (1 + np.exp(-(off + Zm @ w))), 1e-9, 1 - 1e-9); return y * np.log(p) + (1 - y) * np.log(1 - p)
for cross in (False, True):
    gfeat = build(cross); tot = collections.Counter()
    print(f"\n== own/others features from {'OTHER classes in the block set only' if cross else 'all other contexts in the block set (c7)'}")
    for j, mm in enumerate(irt.MINDS):
        L = [o for o in out if o["j"] == j]
        if len(L) < 3000: continue
        gf = np.array([gfeat(o["i"], j) for o in L]); cv = np.array([C[o["i"]] for o in L]); one = np.ones((len(L), 1))
        off = np.log(np.clip([o["p"] for o in L], 1e-6, 1 - 1e-6)) - np.log(np.clip([1 - o["p"] for o in L], 1e-6, 1)); y = np.array([o["y"] for o in L], float)
        half = np.array([gid[grp[o["i"]]] % 2 for o in L]); kl = np.array([K[o["i"]] for o in L])
        A = np.c_[one, cv, gf[:, 1]]; B = np.c_[one, cv, gf]
        g = np.zeros(len(L))
        for h in (0, 1):
            tr, te = half == h, half != h
            wa = fitlr(A[tr], off[tr], y[tr]); wb = fitlr(B[tr], off[tr], y[tr])
            g[te] = llv(B[te], off[te], y[te], wb) - llv(A[te], off[te], y[te], wa)
        parts = {k: g[kl == k].sum() for k in ("cg", "cn", "mono", "oth")}
        for k, v in parts.items(): tot[k] += v
        print(f"  {mm:14s} own beyond cov+oth {g.sum():+6.0f}  by class: " + "  ".join(f"{k} {v:+5.0f} (n {int((kl == k).sum())})" for k, v in parts.items()))
    print("  TOTAL " + "  ".join(f"{k} {v:+.0f}" for k, v in tot.items()))
