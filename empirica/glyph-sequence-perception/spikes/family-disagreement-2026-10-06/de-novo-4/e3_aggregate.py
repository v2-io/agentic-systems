# Aggregate version of e2: every real cohere run answered by >= 2 families (>= 1 answer each). Sum of T over runs,
# observed against its posterior-predictive distribution under L3 (no family x run term). Also per pair of families,
# and a 'leave-the-pair-out' variant where the run's beta posterior uses only minds outside the two families compared
# (less conservative: the data under test don't inform the position).
import sys, numpy as np
SP = "/Users/josephwecker-v2/src/arch/asf/empirica/glyph-sequence-perception/spikes/family-disagreement-2026-10-06"
sys.path.insert(0, SP); sys.path.insert(0, ".")
import abbott
from e2_run_family import FAM, m, Y, N, popi, items, P
fams = ["claude", "grok", "gemini"]; FI = {f: [j for j, mm in enumerate(abbott.MINDS) if FAM[mm] == f] for f in fams}
rng = np.random.default_rng(11); NS = 2000
def T2(y, n, Pp, fa, fb):
    lp, lq = np.log(Pp), np.log1p(-Pp)
    la = y[:, FI[fa]] @ lp[:, FI[fa]].T + (n[:, FI[fa]] - y[:, FI[fa]]) @ lq[:, FI[fa]].T
    lb = y[:, FI[fb]] @ lp[:, FI[fb]].T + (n[:, FI[fb]] - y[:, FI[fb]]) @ lq[:, FI[fb]].T
    return la.max(1) + lb.max(1) - (la + lb).max(1)
for fa, fb in (("claude", "grok"), ("claude", "gemini"), ("grok", "gemini")):
    for pops in ((0,), (1,), (0, 1)):
        obs = 0.0; sims = np.zeros(NS); k = 0
        for i in range(len(items)):
            if popi[i] not in pops: continue
            if N[i, FI[fa]].sum() < 1 or N[i, FI[fb]].sum() < 1: continue
            Pp = P[popi[i]]; k += 1
            # posterior of beta from the population prior only times answers of minds OUTSIDE fa, fb (none for most runs)
            lw = np.log(np.maximum(m.w[popi[i]], 1e-300))
            out = [j for j in range(len(abbott.MINDS)) if FAM[abbott.MINDS[j]] not in (fa, fb)]
            if out:
                lw = lw + Y[i, out] @ np.log(Pp[:, out]).T + (N[i, out] - Y[i, out]) @ np.log1p(-Pp[:, out]).T
            pw = np.exp(lw - np.logaddexp.reduce(lw))
            obs += T2(Y[i][None], N[i][None], Pp, fa, fb)[0]
            g = rng.choice(41, size=NS, p=pw)
            ys = rng.binomial(N[i][None, :].astype(int), Pp[g]).astype(float)
            sims += T2(ys, np.broadcast_to(N[i], ys.shape).astype(float), Pp, fa, fb)
        z = (obs - sims.mean()) / sims.std()
        print(f"{fa}-{fb} pops {[abbott.POPS[p] for p in pops]}: runs {k}, sum T obs {obs:.1f}, sim {sims.mean():.1f} ± {sims.std():.1f} (z {z:+.1f}; 99.9% {np.quantile(sims, .999):.1f})", flush=True)
