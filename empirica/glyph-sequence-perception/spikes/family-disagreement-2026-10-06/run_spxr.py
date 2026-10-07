"""Fit SPXR (row-level, earlier-round features, covariates, ridge) on all snapshot continue answers; strict prequential
calibration (the same features); p001 / p002 per context (features for p001/p002 from all snapshot rounds, i.e. the
rounds before them). Variants: cov_oth_own (default) or cov."""
import sys, json, numpy as np
import irt, lnb, lnb_prefix, preq, covs, spx, spxr, lib
V = sys.argv[1] if len(sys.argv) > 1 else "cov_oth_own"
feats = V != "cov"; own = V == "cov_oth_own"
items, seq, S, N, X = irt.load("continue-stop")
C = covs.covs(items)
rows = preq.prefixes(items, seq, irt.MINDS)
PFo, PFt = lnb_prefix.prefix_features(items, seq, rows, composition_free=True)
if not own: PFo = np.zeros_like(PFo)
item_of_row = np.array([r[0] for r in rows]); M = len(irt.MINDS)
Sr = np.zeros((len(rows), M)); Nr = np.zeros((len(rows), M))
for k, (i, rd, Sp, Np, ans) in enumerate(rows):
    for j, y in ans: Sr[k, j] += y; Nr[k, j] += 1
m = spxr.SPXR(feats=feats, cov=C, own=own).fit_rows(item_of_row, Sr, Nr, X, PFo, PFt, C, iters=300)
print(f"SPXR {V}: ll {m.ll:.1f} iters {m.iters}", flush=True)
for j, mm in enumerate(irt.MINDS):
    print(f"   {mm:14s} a {m.alpha[j]:+.2f} s {m.slope[j]:.2f} g {m.gamma[j]:+.2f}" + (f" lam {m.lam[j]:+.2f} kap {m.kap[j]:+.2f}" if feats else "")
          + " beta " + " ".join(f"{b:+.2f}" for b in m.beta[j]) + f"  pi {m.pi[j]:.3f}", flush=True)
# p001 / p002: one more 'round' per context, features from all snapshot rounds before it
Fo_all, Ft_all, _ = lnb.block_features(items, S, N, grouping="blockset", composition_free=True)
if not own: Fo_all = np.zeros_like(Fo_all)
idx = {"".join(q[1]): i for i, q in enumerate(items)}
def p_next(i, j, S2, N2):
    L = m.comp_loglik_full(S2[i:i+1], N2[i:i+1], X[i:i+1], Fo_all[i:i+1], Ft_all[i:i+1], C[i:i+1])[0]
    r = np.exp(L - np.logaddexp.reduce(L)); ad = spx.RowAdapterC(m, Fo_all, Ft_all, C, [(ii, 0, None, None, None) for ii in range(len(items))])
    return float(r @ ad.cond_next_row(i, X[i], j, int(S2[i, j]), int(N2[i, j])))
def answers(rid):
    rs = [json.loads(l) for l in open(lib.ROOT / "data" / "answers" / f"{rid}.jsonl") if l.strip()]
    return [r for r in rs if not lib.sealed(r) and r["kind"] == "continue" and r["outcome"] in ("none", "continuation")]
S2, N2 = S.copy(), N.copy(); tot = {}
for rid in ("p001", "p002"):
    A = answers(rid); by = {}
    for r in A: by.setdefault(r["mind"], []).append(r)
    for mind, L in sorted(by.items()):
        j = irt.MINDS.index(mind); ps = [p_next(idx["".join(r["context"])], j, S2, N2) for r in L]; ys = [r["outcome"] == "none" for r in L]
        ll = sum(np.log(p if y else 1 - p) for p, y in zip(ps, ys)); tot[rid] = tot.get(rid, 0) + ll
        print(f"   {rid} {mind:14s} stops {sum(ys)} of {len(ys)}  expected {sum(ps):.1f}  log score {ll:.2f}", flush=True)
    for r in A:
        i = idx["".join(r["context"])]; j = irt.MINDS.index(r["mind"]); S2[i, j] += r["outcome"] == "none"; N2[i, j] += 1
print("   totals", {k: round(v, 2) for k, v in tot.items()}, flush=True)
preq.report(preq.score({None: spx.RowAdapterC(m, PFo, PFt, C, rows)}, None, items, seq, X), f"SPXR {V} (fitted on earlier-round features), strict prequential")
