# Which RUNS are model-sensitive in recognition (cohere), beyond each mind's criterion and slope by set class?
# abbott.py's L3 (logit; per-mind alpha by set class and slope; item position beta from a per-population grid prior)
# fitted on all cohere real runs + shuffled controls. For each real run answered by >= 2 families with >= 2 answers
# each: T = sum_f max_beta ll_f(beta) - max_beta sum_f ll_f(beta) (a family-specific position against a shared one),
# and its posterior-predictive p (beta drawn from the run's posterior given all answers, answers re-simulated with the
# same counts per mind). Uniform p under the model; excess small p = family x run interaction.
import sys, collections, json, numpy as np
SP = "/Users/josephwecker-v2/src/arch/asf/empirica/glyph-sequence-perception/spikes/family-disagreement-2026-10-06"
sys.path.insert(0, SP)
import abbott
FAM = {"sonnet55": "claude", "opus55": "claude", "haiku45nt": "claude", "haiku45": "claude", "grok46": "grok",
       "gemini38flash": "gemini", "gemini31pro": "gemini"}
items, Y, N, popi, cant = abbott.load()
m = abbott.Model("L3").fit(Y, N, popi)
print("L3 fitted; alpha (contig/other), slope:", {mm: (round(m.alpha[j,0],2), round(m.alpha[j,1],2), round(m.slope[j],2)) for j, mm in enumerate(abbott.MINDS)})
P = m.P()                                                        # (4, 41, M)
L = m.comp_ll(Y, N, popi)                                        # (I, 41) incl. prior
post = np.exp(L - np.logaddexp.reduce(L, 1)[:, None])
fams = sorted(set(FAM.values())); FI = {f: [j for j, mm in enumerate(abbott.MINDS) if FAM[mm] == f] for f in fams}
rng = np.random.default_rng(7); NS = 1000
def T_of(y, n, Pp):
    """y, n: (S, M) ; Pp: (41, M) -> T (S,)"""
    lp, lq = np.log(Pp), np.log1p(-Pp)
    llf = {f: y[:, FI[f]] @ lp[:, FI[f]].T + (n[:, FI[f]] - y[:, FI[f]]) @ lq[:, FI[f]].T for f in fams}   # (S, 41)
    sep = sum(v.max(1) for v in llf.values()); sh = sum(llf.values()).max(1)
    return sep - sh
rows = []
for i, q in enumerate(items):
    p = popi[i]
    if p >= 2: continue                                          # real runs only
    nf = {f: N[i, FI[f]].sum() for f in fams}
    if sum(v >= 2 for v in nf.values()) < 2: continue
    Pp = P[p]
    t0 = T_of(Y[i][None, :], N[i][None, :], Pp)[0]
    g = rng.choice(41, size=NS, p=post[i])
    ys = rng.binomial(N[i][None, :].astype(int), Pp[g])          # (NS, M)
    ts = T_of(ys.astype(float), np.broadcast_to(N[i], ys.shape).astype(float), Pp)
    pv = (1 + (ts >= t0 - 1e-9).sum()) / (NS + 1)
    rows.append((pv, t0, q, abbott.POPS[p], {f: (int(Y[i, FI[f]].sum()), int(N[i, FI[f]].sum())) for f in fams},
                 {mm: (int(Y[i, j]), int(N[i, j])) for j, mm in enumerate(abbott.MINDS) if N[i, j]}))
pv = np.array([r[0] for r in rows])
print(f"runs tested {len(rows)}; p<0.01: {(pv<0.01).sum()} (expected ~{0.01*len(rows):.0f} if no interaction, fewer since posterior-predictive p is conservative); p<0.05: {(pv<0.05).sum()} (~{0.05*len(rows):.0f})")
for pop in ("real-contig", "real-other"):
    sel = np.array([r[3] == pop for r in rows]); print(f"  {pop}: tested {sel.sum()}, p<0.01 {(pv[sel]<0.01).sum()}, p<0.05 {(pv[sel]<0.05).sum()}")
rows.sort(key=lambda r: (r[0], -r[1]))
json.dump([[r[0], r[1], "".join(r[2][1]), r[3], r[4], r[5]] for r in rows], open(sys.argv[1] if len(sys.argv) > 1 else "e2_rows.json", "w"), ensure_ascii=False)
print("\nmost family-sensitive runs (p, T, run, pop, yes/n per family):")
for r in rows[:60]:
    print(f"  p={r[0]:.4f} T={r[1]:5.2f} {''.join(r[2][1]):24s} {r[3]:11s} " + " ".join(f"{f} {a}/{b}" for f, (a, b) in r[4].items()))
# direction of the sensitive ones: which family is the odd one out
odd = collections.Counter()
for r in rows:
    if r[0] >= 0.01: continue
    sh = {f: (a + 0.5) / (b + 1) for f, (a, b) in r[4].items() if b >= 2}
    mean = np.mean(list(sh.values()))
    f = max(sh, key=lambda f: abs(sh[f] - mean)); odd[(f, "lower" if sh[f] < mean else "higher")] += 1
print("\nodd family out among p<0.01 runs:", dict(odd))
