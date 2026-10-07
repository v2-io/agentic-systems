"""De novo 3, check 3. c1's features, recomputed from OTHER ROUNDS only: for answer (mind j, item i, round rd), the
group features use residuals on other items of the same block set given in rounds != rd. If the mind-specific
increment (own beyond others) shrinks when same-round answers are removed, part of it is within-round correlation of
one mind's answers (same sheet or same call context), a probing effect, not a lean on the sequence. Same scoring
frame as c1 (irtu prequential offset; fit on half the groups, score on the other half)."""
import sys, collections, pickle, pathlib, numpy as np
HERE = pathlib.Path(__file__).resolve().parent; SP = HERE.parent
sys.path.insert(0, str(SP)); sys.path.insert(0, str(SP / "de-novo-2"))
import os; os.chdir(SP)
import irt, features as F
CACHE = pathlib.Path("/private/tmp/claude-505/-Users-josephwecker-v2-src-arch-asf-empirica-glyph-sequence-perception/2c3109cb-51be-4d66-937d-88f689223324/scratchpad/dn3/preq_irtu.pkl")
items, seq, S, N, X = irt.load("continue-stop"); out = pickle.load(open(CACHE, "rb"))
grp = [frozenset(F.block(g) for g in q[1]) for q in items]; gid = {g: k for k, g in enumerate(sorted(set(grp), key=repr))}
Z = lambda: np.zeros(2)
G_t = collections.defaultdict(Z); G_r = collections.defaultdict(Z); G_tm = collections.defaultdict(Z); G_rm = collections.defaultdict(Z)
I_t = collections.defaultdict(Z); I_r = collections.defaultdict(Z); I_tm = collections.defaultdict(Z); I_rm = collections.defaultdict(Z)
for o in out:
    g = grp[o["i"]]; v = np.array([o["y"] - o["p"], 1.0]); i, j, rd = o["i"], o["j"], o["rd"]
    G_t[g] += v; G_r[(g, rd)] += v; G_tm[(g, j)] += v; G_rm[(g, rd, j)] += v
    I_t[i] += v; I_r[(i, rd)] += v; I_tm[(i, j)] += v; I_rm[(i, rd, j)] += v
def feats(o, other_rounds):
    g, i, j, rd = grp[o["i"]], o["i"], o["j"], o["rd"]
    own = G_tm[(g, j)] - I_tm[(i, j)]; allm = G_t[g] - I_t[i]
    if other_rounds:
        own = own - (G_rm[(g, rd, j)] - I_rm[(i, rd, j)]); allm = allm - (G_r[(g, rd)] - I_r[(i, rd)])
    oth = allm - own
    f = lambda a: a[0] / a[1] if a[1] > 0 else 0.0
    return f(own), f(oth)
def fitlr(Zm, off, y):
    w = np.zeros(Zm.shape[1])
    for _ in range(30):
        p = 1 / (1 + np.exp(-(off + Zm @ w))); H = (Zm * (p * (1 - p))[:, None]).T @ Zm + 1e-6 * np.eye(Zm.shape[1]); w += np.linalg.solve(H, Zm.T @ (y - p))
    return w
def ll(Zm, off, y, w):
    p = np.clip(1 / (1 + np.exp(-(off + Zm @ w))), 1e-9, 1 - 1e-9); return float((y * np.log(p) + (1 - y) * np.log(1 - p)).sum())
for other_rounds in (False, True):
    tot = collections.Counter(); lines = []
    for j, mm in enumerate(irt.MINDS):
        L = [o for o in out if o["j"] == j]
        if len(L) < 3000: continue
        Fz = np.array([feats(o, other_rounds) for o in L])
        off = np.log(np.clip([o["p"] for o in L], 1e-6, 1 - 1e-6)) - np.log(np.clip([1 - o["p"] for o in L], 1e-6, 1)); y = np.array([o["y"] for o in L], float)
        half = np.array([gid[grp[o["i"]]] % 2 for o in L]); row = {}
        for name, cols in (("own", [0]), ("oth", [1]), ("both", [0, 1])):
            g_ = 0.0
            for h in (0, 1):
                tr, te = half == h, half != h; w = fitlr(Fz[tr][:, cols], off[tr], y[tr]); g_ += ll(Fz[te][:, cols], off[te], y[te], w) - ll(Fz[te][:, cols], off[te], y[te], np.zeros(len(cols)))
            row[name] = g_; tot[name] += g_
        lines.append(f"   {mm:14s} own {row['own']:+6.0f}  oth {row['oth']:+6.0f}  both {row['both']:+6.0f}  own beyond oth {row['both']-row['oth']:+5.0f}")
    print(("OTHER ROUNDS ONLY" if other_rounds else "ALL ROUNDS (as c1)") + f": total own {tot['own']:+.0f}, oth {tot['oth']:+.0f}, both {tot['both']:+.0f}, own beyond oth {tot['both']-tot['oth']:+.0f}")
    print("\n".join(lines), flush=True)
