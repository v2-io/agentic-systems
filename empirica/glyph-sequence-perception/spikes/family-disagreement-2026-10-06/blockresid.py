"""Do contexts share a mind-specific propensity beyond the item-level model? For every continue answer, the irtu
prequential prediction p (from earlier rounds on the same item) and residual y - p. Features, leave-the-item-out:
  own   = the same mind's mean residual on OTHER items whose context ends in the same Unicode block
  other = the other minds' mean residual on other items of that block
Per mind: logistic regression y ~ offset(logit p) + b_own * own + b_other * other, with each feature's gain in log score
(fitted on even-numbered blocks, scored on odd-numbered, and the reverse: no answer scores a model fitted on itself)."""
import sys, json, collections, numpy as np
sys.path.insert(0, "de-novo-2")
import irt, irtu, checks2, preq, features as F

items, seq, S, N, X = irt.load("continue-stop")
P = json.load(open("de-novo-2/tau-pred.json"))["params"]; m = irtu.ModelU()
for k in ("alpha", "slope", "gamma", "tau", "pi", "eps", "dlt"): setattr(m, k, np.array(P[k]))
out = preq.score({None: checks2.AdaptU(m)}, None, items, seq, X)
blk = [F.block(q[1][-1]) for q in items]
bnames = sorted(set(blk)); bid = {b: k for k, b in enumerate(bnames)}
# residual sums per (block, mind, item)
agg = collections.defaultdict(lambda: [0.0, 0])          # (block, mind, item) -> [sum resid, n]
for o in out:
    a = agg[(blk[o["i"]], o["j"], o["i"])]; a[0] += o["y"] - o["p"]; a[1] += 1
tot_bm = collections.defaultdict(lambda: [0.0, 0]); tot_b = collections.defaultdict(lambda: [0.0, 0])
for (b, j, i), (s_, n_) in agg.items():
    t = tot_bm[(b, j)]; t[0] += s_; t[1] += n_; u = tot_b[b]; u[0] += s_; u[1] += n_
def feats(o):
    b, j, i = blk[o["i"]], o["j"], o["i"]
    s_i, n_i = agg[(b, j, i)]; t = tot_bm[(b, j)]
    own = (t[0] - s_i) / (t[1] - n_i) if t[1] - n_i > 0 else 0.0
    # other minds, other items
    so = no = 0.0
    for jj in range(len(irt.MINDS)):
        if jj == j: continue
        tt = tot_bm.get((b, jj))
        if not tt: continue
        si, ni = agg.get((b, jj, i), [0.0, 0])
        so += tt[0] - si; no += tt[1] - ni
    return own, (so / no if no > 0 else 0.0)
def logit(p): return np.log(p / (1 - p))
def fitlr(Z, off, y, iters=30):
    w = np.zeros(Z.shape[1])
    for _ in range(iters):
        p = 1 / (1 + np.exp(-(off + Z @ w))); g = Z.T @ (y - p); H = (Z * (p * (1 - p))[:, None]).T @ Z + 1e-6 * np.eye(Z.shape[1])
        w += np.linalg.solve(H, g)
    return w
def ll(Z, off, y, w):
    p = np.clip(1 / (1 + np.exp(-(off + Z @ w))), 1e-9, 1 - 1e-9); return float((y * np.log(p) + (1 - y) * np.log(1 - p)).sum())
print("per mind: coefficients on the block features (fitted on half the blocks) and held-out log-score gain on the other half")
for j, mm in enumerate(irt.MINDS):
    L = [o for o in out if o["j"] == j]
    if len(L) < 1000: continue
    Fz = np.array([feats(o) for o in L]); off = logit(np.clip(np.array([o["p"] for o in L]), 1e-6, 1 - 1e-6)); y = np.array([o["y"] for o in L], float)
    half = np.array([bid[blk[o["i"]]] % 2 for o in L])
    gains = {"own": 0.0, "other": 0.0, "both": 0.0}; coef = None
    for h in (0, 1):
        tr, te = half == h, half != h
        for name, cols in (("own", [0]), ("other", [1]), ("both", [0, 1])):
            w = fitlr(Fz[tr][:, cols], off[tr], y[tr]); gains[name] += ll(Fz[te][:, cols], off[te], y[te], w) - ll(Fz[te][:, cols], off[te], y[te], np.zeros(len(cols)))
            if name == "both" and h == 0: coef = w
    print(f"  {mm:14s} n={len(L):6d}  coef own {coef[0]:+.2f} other {coef[1]:+.2f}   held-out gain (nats): own {gains['own']:+.1f}  other {gains['other']:+.1f}  both {gains['both']:+.1f}")
