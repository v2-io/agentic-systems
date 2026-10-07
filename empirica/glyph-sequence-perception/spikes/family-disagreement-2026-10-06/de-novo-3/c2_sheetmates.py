"""De novo 3, check 2. Is sheetmates.py's -0.70 logit a format effect, or selection: the planner draws several
questions from a claim it weights highly (METHODOLOGY 5, 'a strong sequence can get several questions in a round'), so
same-sequence sheet-mates co-occur with strong sequences, which continue more than an item-level model with no
knowledge of the item predicts. Test: add a measure of the sequence's strength taken from OTHER rounds only (so it
contains no answer given on, or beside, the sheet in question): the mean irtu-prequential residual over other items of
the same block set, all minds, other rounds; and the same for the mind alone. If the sheet-mate coefficient survives,
the format reading stands. Uses sheetmates.py's definition of a sheet-mate unchanged, and c1's cached prequential
predictions."""
import sys, json, collections, pickle, pathlib, numpy as np
HERE = pathlib.Path(__file__).resolve().parent; SP = HERE.parent
sys.path.insert(0, str(SP)); sys.path.insert(0, str(SP / "de-novo-2"))
import os; os.chdir(SP)
import irt, lib, features as F
from values import ckey
CACHE = pathlib.Path("/private/tmp/claude-505/-Users-josephwecker-v2-src-arch-asf-empirica-glyph-sequence-perception/2c3109cb-51be-4d66-937d-88f689223324/scratchpad/dn3/preq_irtu.pkl")
items, seq, S, N, X = irt.load("continue-stop"); out = pickle.load(open(CACHE, "rb"))
recs, _ = lib.load(); idx = {q: i for i, q in enumerate(items)}
bs = lambda c: frozenset(F.block(g) for g in c)
sheet = collections.defaultdict(list); ans_sheet = collections.defaultdict(list)
for r in recs:
    if r["kind"] != "continue" or not r.get("sid") or r["mind"] not in irt.MINDS: continue
    if (r.get("tags") or {}).get("variant") not in (None, "plain"): continue
    if r["outcome"] not in ("none", "continuation"): continue
    q = ckey(r)
    if q not in idx: continue
    rd = int(r["round"][1:]); sheet[(rd, r["mind"], r["sid"])].append((idx[q], bs(r["context"])))
    ans_sheet[(idx[q], r["mind"], rd)].append(r["sid"])
def mates(o):
    rd = o["rd"]; mm = irt.MINDS[o["j"]]; sids = ans_sheet.get((o["i"], mm, rd), [])
    if not sids: return None
    me = bs(items[o["i"]][1]); n = 0
    for sid in sids[:1]:
        for ii, b in sheet[(rd, mm, sid)]:
            if ii != o["i"] and b == me: n += 1
    return n
grp = [bs(q[1]) for q in items]
# residual sums per (group, round) and per (group, round, mind), and per (item, round)/(item, round, mind)
G_r = collections.defaultdict(lambda: np.zeros(2)); G_rm = collections.defaultdict(lambda: np.zeros(2))
I_r = collections.defaultdict(lambda: np.zeros(2)); I_rm = collections.defaultdict(lambda: np.zeros(2))
G_t = collections.defaultdict(lambda: np.zeros(2)); G_tm = collections.defaultdict(lambda: np.zeros(2))
I_t = collections.defaultdict(lambda: np.zeros(2)); I_tm = collections.defaultdict(lambda: np.zeros(2))
for o in out:
    g = grp[o["i"]]; v = np.array([o["y"] - o["p"], 1.0])
    G_r[(g, o["rd"])] += v; G_rm[(g, o["rd"], o["j"])] += v; I_r[(o["i"], o["rd"])] += v; I_rm[(o["i"], o["rd"], o["j"])] += v
    G_t[g] += v; G_tm[(g, o["j"])] += v; I_t[o["i"]] += v; I_tm[(o["i"], o["j"])] += v
def strength(o):
    g, rd, i, j = grp[o["i"]], o["rd"], o["i"], o["j"]
    # all minds: group total - this round's group answers - this item's other-round answers
    a = G_t[g] - G_r[(g, rd)] - (I_t[i] - I_r[(i, rd)])
    b = G_tm[(g, j)] - G_rm[(g, rd, j)] - (I_tm[(i, j)] - I_rm[(i, rd, j)])
    return (a[0] / a[1] if a[1] > 0 else 0.0), (b[0] / b[1] if b[1] > 0 else 0.0), a[1]
rows = []
for o in out:
    k = mates(o)
    if k is None: continue
    sa, sm, n = strength(o); rows.append((o["grp"], k > 0, o["y"], o["p"], sa, sm, n > 0))
def fit(Z, off, y):
    w = np.zeros(Z.shape[1])
    for _ in range(40):
        q = 1 / (1 + np.exp(-(off + Z @ w))); H = (Z * (q * (1 - q))[:, None]).T @ Z + 1e-6 * np.eye(Z.shape[1]); w += np.linalg.solve(H, Z.T @ (y - q))
    q = 1 / (1 + np.exp(-(off + Z @ w))); H = (Z * (q * (1 - q))[:, None]).T @ Z + 1e-6 * np.eye(Z.shape[1])
    return w, np.sqrt(np.diag(np.linalg.inv(H)))
for g in ("first", "repeat"):
    L = [r for r in rows if r[0] == g]
    h = np.array([float(r[1]) for r in L]); y = np.array([r[2] for r in L], float); p = np.clip(np.array([r[3] for r in L]), 1e-6, 1 - 1e-6)
    sa = np.array([r[4] for r in L]); sm = np.array([r[5] for r in L]); off = np.log(p / (1 - p))
    print(f"{g}: n={len(L)}, share with same-sequence mates {h.mean():.3f}; mean other-round strength with mates {sa[h==1].mean():+.3f}, without {sa[h==0].mean():+.3f}")
    for name, Z in (("mates only", np.c_[h]), ("mates + strength (all minds, other rounds)", np.c_[h, sa]),
                    ("mates + strength (all minds) + strength (this mind), other rounds", np.c_[h, sa, sm])):
        w, se = fit(Z, off, y); print(f"   {name:62s} mates {w[0]:+.2f} ± {se[0]:.2f}" + "".join(f"  f{k} {w[k]:+.2f}" for k in range(1, len(w))))
