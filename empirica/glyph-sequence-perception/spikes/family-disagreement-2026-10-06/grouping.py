"""Which unit carries the mind-specific propensity? blockresid.py's own-mind feature (leave-the-item-out mean residual
of the same mind under irtu's prequential predictions), with items grouped by: the context's last glyph; its last two
glyphs (as a set); the Unicode block of its last glyph; the set of blocks of all its glyphs. Held-out (half the groups
fit, half scored) gain in log score per mind, for each grouping alone."""
import sys, json, collections, numpy as np
sys.path.insert(0, "de-novo-2")
import irt, irtu, checks2, preq, features as F
items, seq, S, N, X = irt.load("continue-stop")
P = json.load(open("de-novo-2/tau-pred.json"))["params"]; m = irtu.ModelU()
for k in ("alpha", "slope", "gamma", "tau", "pi", "eps", "dlt"): setattr(m, k, np.array(P[k]))
out = preq.score({None: checks2.AdaptU(m)}, None, items, seq, X)
GROUPS = {"last glyph": lambda c: c[-1], "last two (set)": lambda c: frozenset(c[-2:]),
          "block of last": lambda c: F.block(c[-1]), "blocks of all": lambda c: frozenset(F.block(g) for g in c)}
def fitlr(z, off, y):
    w = 0.0
    for _ in range(30):
        p = 1 / (1 + np.exp(-(off + w * z))); g = (z * (y - p)).sum(); h = (z * z * p * (1 - p)).sum() + 1e-9; w += g / h
    return w
def ll(z, off, y, w):
    p = np.clip(1 / (1 + np.exp(-(off + w * z))), 1e-9, 1 - 1e-9); return float((y * np.log(p) + (1 - y) * np.log(1 - p)).sum())
for gname, gf in GROUPS.items():
    grp = [gf(q[1]) for q in items]; gid = {g: k for k, g in enumerate(sorted(set(grp), key=repr))}
    agg = collections.defaultdict(lambda: [0.0, 0]); tot = collections.defaultdict(lambda: [0.0, 0])
    for o in out:
        a = agg[(grp[o["i"]], o["j"], o["i"])]; a[0] += o["y"] - o["p"]; a[1] += 1
    for (g, j, i), (s_, n_) in agg.items(): t = tot[(g, j)]; t[0] += s_; t[1] += n_
    row = []
    for j, mm in enumerate(irt.MINDS):
        L = [o for o in out if o["j"] == j]
        if len(L) < 3000: continue
        z = np.array([((tot[(grp[o["i"]], j)][0] - agg[(grp[o["i"]], j, o["i"])][0]) / max(tot[(grp[o["i"]], j)][1] - agg[(grp[o["i"]], j, o["i"])][1], 1)) for o in L])
        off = np.log(np.clip([o["p"] for o in L], 1e-6, 1 - 1e-6)) - np.log(np.clip([1 - o["p"] for o in L], 1e-6, 1)); y = np.array([o["y"] for o in L], float)
        half = np.array([gid[grp[o["i"]]] % 2 for o in L]); gain = 0.0
        for h in (0, 1):
            tr, te = half == h, half != h; w = fitlr(z[tr], off[tr], y[tr]); gain += ll(z[te], off[te], y[te], w) - ll(z[te], off[te], y[te], 0.0)
        row.append(f"{mm} {gain:+.0f}")
    print(f"{gname:16s} groups {len(gid):6d}:  " + "  ".join(row))
