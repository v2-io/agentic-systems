"""De novo 3, check 1. Is strengthening 2's 'mind-specific sequence effect' a property of the sequence (a mind's lean
across a block set) or of near-duplicate questions (contexts that end at the same glyph, i.e. the same continuation
point asked at other lengths or orientations)? And is it mind-specific once the other minds' feature is
composition-free? Same frame as blockresid.py / grouping.py: irtu prequential predictions as offset; leave-the-item-out
mean residuals per group (group = set of blocks the context spans); coefficients fitted on half the groups and scored on
the other half, both ways. Features for answer (mind j, item i):
  own_all   j's mean residual on other items of the group
  own_far   the same, over items whose last glyph differs from i's AND that share no glyph with i's last two
  oth_all   the other minds' mean residual on other items of the group (residuals are per-mind, so composition-free)
  oth_far   the same, far items only
Loads through lib.py (seal applied first) via irt.load."""
import sys, json, collections, pickle, pathlib, numpy as np
HERE = pathlib.Path(__file__).resolve().parent; SP = HERE.parent
sys.path.insert(0, str(SP)); sys.path.insert(0, str(SP / "de-novo-2"))
import os; os.chdir(SP)
import irt, irtu, checks2, preq, features as F
CACHE = pathlib.Path("/private/tmp/claude-505/-Users-josephwecker-v2-src-arch-asf-empirica-glyph-sequence-perception/2c3109cb-51be-4d66-937d-88f689223324/scratchpad/dn3/preq_irtu.pkl")
items, seq, S, N, X = irt.load("continue-stop")
if CACHE.exists():
    out = pickle.load(open(CACHE, "rb"))
else:
    P = json.load(open("de-novo-2/tau-pred.json"))["params"]; m = irtu.ModelU()
    for k in ("alpha", "slope", "gamma", "tau", "pi", "eps", "dlt"): setattr(m, k, np.array(P[k]))
    out = preq.score({None: checks2.AdaptU(m)}, None, items, seq, X); pickle.dump(out, open(CACHE, "wb"))
print("answers scored", len(out), flush=True)
ctx = [q[1] for q in items]
grp = [frozenset(F.block(g) for g in c) for c in ctx]
gid = {g: k for k, g in enumerate(sorted(set(grp), key=repr))}
M = len(irt.MINDS)
# residual sum / count per (item, mind)
RS = np.zeros((len(items), M)); RN = np.zeros((len(items), M))
for o in out: RS[o["i"], o["j"]] += o["y"] - o["p"]; RN[o["i"], o["j"]] += 1
members = collections.defaultdict(list)
for i, g in enumerate(grp): members[g].append(i)
def far(i, k):
    a, b = ctx[i], ctx[k]
    if a[-1] == b[-1]: return False
    return not (set(a[-2:]) & set(b[-2:]))
cache = {}
def feats(i, j):
    key = (i, j)
    if key in cache: return cache[key]
    mem = [k for k in members[grp[i]] if k != i]
    fm = [k for k in mem if far(i, k)]
    def mean(ks, own):
        if not ks: return 0.0
        ks = np.array(ks)
        if own: s, n = RS[ks, j].sum(), RN[ks, j].sum()
        else: s, n = RS[ks].sum() - RS[ks, j].sum(), RN[ks].sum() - RN[ks, j].sum()
        return s / n if n > 0 else 0.0
    v = (mean(mem, True), mean(fm, True), mean(mem, False), mean(fm, False), len(fm) > 0)
    cache[key] = v; return v
def fitlr(Z, off, y, iters=30):
    w = np.zeros(Z.shape[1])
    for _ in range(iters):
        p = 1 / (1 + np.exp(-(off + Z @ w))); g = Z.T @ (y - p); H = (Z * (p * (1 - p))[:, None]).T @ Z + 1e-6 * np.eye(Z.shape[1])
        w += np.linalg.solve(H, g)
    return w
def ll(Z, off, y, w):
    p = np.clip(1 / (1 + np.exp(-(off + Z @ w))), 1e-9, 1 - 1e-9); return float((y * np.log(p) + (1 - y) * np.log(1 - p)).sum())
SETS = {"own_all": [0], "own_far": [1], "oth_all": [2], "oth_far": [3], "oth_all+own_all": [2, 0], "oth_all+own_far": [2, 1],
        "oth_far+own_far": [3, 1]}
tot = collections.Counter()
for j, mm in enumerate(irt.MINDS):
    L = [o for o in out if o["j"] == j]
    if len(L) < 3000: continue
    Fz = np.array([feats(o["i"], j)[:4] for o in L]); hasfar = np.array([feats(o["i"], j)[4] for o in L])
    off = np.log(np.clip([o["p"] for o in L], 1e-6, 1 - 1e-6)) - np.log(np.clip([1 - o["p"] for o in L], 1e-6, 1)); y = np.array([o["y"] for o in L], float)
    half = np.array([gid[grp[o["i"]]] % 2 for o in L]); row = {}
    for name, cols in SETS.items():
        g = 0.0
        for h in (0, 1):
            tr, te = half == h, half != h; w = fitlr(Fz[tr][:, cols], off[tr], y[tr]); g += ll(Fz[te][:, cols], off[te], y[te], w) - ll(Fz[te][:, cols], off[te], y[te], np.zeros(len(cols)))
        row[name] = g; tot[name] += g
    print(f"{mm:14s} n={len(L):6d} (with far items {hasfar.mean():.2f}) " + "  ".join(f"{k} {v:+.0f}" for k, v in row.items()), flush=True)
print("TOTAL " + "  ".join(f"{k} {v:+.0f}" for k, v in tot.items()))
print("mind-specific increments: own_all beyond oth_all", round(tot["oth_all+own_all"] - tot["oth_all"]),
      "; own_far beyond oth_all", round(tot["oth_all+own_far"] - tot["oth_all"]), "; own_far beyond oth_far", round(tot["oth_far+own_far"] - tot["oth_far"]))
