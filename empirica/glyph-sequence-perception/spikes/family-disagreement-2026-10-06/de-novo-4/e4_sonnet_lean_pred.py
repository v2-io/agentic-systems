# Does a logit model with NO contiguity term (abbott L2: per-mind criterion + slope) already predict e1's table?
# For pair (sonnet, X), runs both answered, panel (all other minds) >= 2 answers all yes: predicted no-rate of each,
# beta posterior from the panel's answers only (population prior x panel likelihood). Fitted on all cohere items.
import sys, collections, numpy as np
SP = "/Users/josephwecker-v2/src/arch/asf/empirica/glyph-sequence-perception/spikes/family-disagreement-2026-10-06"
sys.path.insert(0, SP)
import abbott
items, Y, N, popi, cant = abbott.load()
for kind in ("L2", "L4"):
    m = abbott.Model(kind).fit(Y, N, popi); P = m.P(); M = abbott.MINDS
    print(f"\n{kind}")
    for b in M:
        if b == "sonnet55": continue
        a = "sonnet55"; ja, jb = M.index(a), M.index(b)
        for p in (0, 1):
            obs = {a: [0, 0], b: [0, 0]}; pred = {a: 0.0, b: 0.0}; k = 0
            for i in range(len(items)):
                if popi[i] != p or N[i, ja] == 0 or N[i, jb] == 0: continue
                pan = [j for j in range(len(M)) if j not in (ja, jb)]
                if N[i, pan].sum() < 2 or Y[i, pan].sum() != N[i, pan].sum(): continue
                lw = np.log(np.maximum(m.w[p], 1e-300)) + Y[i, pan] @ np.log(P[p][:, pan]).T + (N[i, pan] - Y[i, pan]) @ np.log1p(-P[p][:, pan]).T
                w = np.exp(lw - np.logaddexp.reduce(lw)); k += 1
                for mm, j in ((a, ja), (b, jb)):
                    obs[mm][0] += N[i, j] - Y[i, j]; obs[mm][1] += N[i, j]; pred[mm] += N[i, j] * float(w @ (1 - P[p][:, j]))
            print(f"  {abbott.POPS[p]:11s} vs {b:13s} runs {k:4d}: sonnet no {obs[a][0]:.0f}/{obs[a][1]:.0f} pred {pred[a]:.1f} | {b[:8]} no {obs[b][0]:.0f}/{obs[b][1]:.0f} pred {pred[b]:.1f}")
