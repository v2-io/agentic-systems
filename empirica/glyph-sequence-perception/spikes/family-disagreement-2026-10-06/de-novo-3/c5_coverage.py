"""De novo 3, check 5. FINDINGS 3 says Grok and Haiku without thinking lean hardest on their own sequence-level
behaviour, Opus and Gemini Pro on the shared part. The minds with large own effects are the core minds that answer
every sheet; Opus, Haiku with thinking and the Gemini minds are sampled and have 3-30x fewer answers, so their own
feature is noisier and would attenuate even if their lean were the same. Test: for the core minds, build the OWN
feature from a random fraction of the mind's answers (matched to Opus's coverage, about 0.2), score every answer, and
compare the per-answer mind-specific increment with the sampled minds'. Residual frame of c1/c3 (all rounds)."""
import sys, collections, pickle, pathlib, numpy as np
HERE = pathlib.Path(__file__).resolve().parent; SP = HERE.parent
sys.path.insert(0, str(SP)); sys.path.insert(0, str(SP / "de-novo-2"))
import os; os.chdir(SP)
import irt, features as F
CACHE = pathlib.Path("/private/tmp/claude-505/-Users-josephwecker-v2-src-arch-asf-empirica-glyph-sequence-perception/2c3109cb-51be-4d66-937d-88f689223324/scratchpad/dn3/preq_irtu.pkl")
items, seq, S, N, X = irt.load("continue-stop"); out = pickle.load(open(CACHE, "rb"))
grp = [frozenset(F.block(g) for g in q[1]) for q in items]; gid = {g: k for k, g in enumerate(sorted(set(grp), key=repr))}
def fitlr(Zm, off, y):
    w = np.zeros(Zm.shape[1])
    for _ in range(30):
        p = 1 / (1 + np.exp(-(off + Zm @ w))); H = (Zm * (p * (1 - p))[:, None]).T @ Zm + 1e-6 * np.eye(Zm.shape[1]); w += np.linalg.solve(H, Zm.T @ (y - p))
    return w
def ll(Zm, off, y, w):
    p = np.clip(1 / (1 + np.exp(-(off + Zm @ w))), 1e-9, 1 - 1e-9); return float((y * np.log(p) + (1 - y) * np.log(1 - p)).sum())
def run(j, frac, seed):
    rng = np.random.default_rng(seed)
    keep = [o for o in out if o["j"] != j or rng.random() < frac]           # answers that may enter features
    Go = collections.defaultdict(lambda: np.zeros(2)); Io = collections.defaultdict(lambda: np.zeros(2))
    Ga = collections.defaultdict(lambda: np.zeros(2)); Ia = collections.defaultdict(lambda: np.zeros(2))
    for o in keep:
        v = np.array([o["y"] - o["p"], 1.0]); g = grp[o["i"]]
        if o["j"] == j: Go[g] += v; Io[o["i"]] += v
        else: Ga[g] += v; Ia[o["i"]] += v
    L = [o for o in out if o["j"] == j]
    f = lambda a: a[0] / a[1] if a[1] > 0 else 0.0
    Fz = np.array([(f(Go[grp[o["i"]]] - Io[o["i"]]), f(Ga[grp[o["i"]]] - Ia[o["i"]])) for o in L])
    off = np.log(np.clip([o["p"] for o in L], 1e-6, 1 - 1e-6)) - np.log(np.clip([1 - o["p"] for o in L], 1e-6, 1)); y = np.array([o["y"] for o in L], float)
    half = np.array([gid[grp[o["i"]]] % 2 for o in L]); row = {}
    for name, cols in (("oth", [1]), ("both", [0, 1])):
        g_ = 0.0
        for h in (0, 1):
            tr, te = half == h, half != h; w = fitlr(Fz[tr][:, cols], off[tr], y[tr]); g_ += ll(Fz[te][:, cols], off[te], y[te], w) - ll(Fz[te][:, cols], off[te], y[te], np.zeros(len(cols)))
        row[name] = g_
    return (row["both"] - row["oth"]) / len(L), len(L)
for mm in irt.MINDS:
    j = irt.MINDS.index(mm); n = sum(1 for o in out if o["j"] == j)
    if n < 3000: continue
    full, _ = run(j, 1.0, 0)
    line = f"{mm:14s} n={n:6d}  own-beyond-others per answer, own feature from all its answers: {full:+.4f}"
    if n > 15000:
        th = [run(j, 4547 / n, s)[0] for s in range(3)]
        line += f";  from a {4547/n:.2f} sample (Opus's count), 3 draws: " + ", ".join(f"{t:+.4f}" for t in th)
    print(line, flush=True)
