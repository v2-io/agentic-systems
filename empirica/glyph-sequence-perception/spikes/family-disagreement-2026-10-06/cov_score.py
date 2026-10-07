"""Strengthening 3: fit a ladder variant on all snapshot continue answers; strict prequential calibration (features from
earlier rounds, composition-free; covariates static); and p001 / p002 scored per context. The covariates were added
after p002 showed chart class mattering (de-novo-feedback-3 §1), so the p002 score is a late test of a model fitted on
the snapshot alone, not a pre-registered one.
  python3 cov_score.py VARIANT [--no-preq]"""
import json, sys, numpy as np
import irt, lnb, spx, covs, preq, lnb_prefix, lib
V = sys.argv[1]
items, seq, S, N, X = irt.load("continue-stop")
C = covs.covs(items)
use_cov = V.startswith("cov"); shared = V == "cov_shared"
feats = V in ("cov_oth", "cov_oth_own", "oth_own_cf", "cov_othp_own"); own = V in ("cov_oth_own", "oth_own_cf", "cov_othp_own"); cf = V != "cov_othp_own"
Fo, Ft, _ = lnb.block_features(items, S, N, grouping="blockset", composition_free=cf)
if not own: Fo = np.zeros_like(Fo)
m = spx.SPX(feats=feats, cov=C if use_cov else None, cov_shared=shared, own=own).fit(S, N, X, Fo, Ft, iters=400, C=C if use_cov else None)
print(f"{V}: all-data ll {m.ll:.1f}, iters {m.iters}", flush=True)
for j, mm in enumerate(irt.MINDS):
    print(f"   {mm:14s} a {m.alpha[j]:+.2f} s {m.slope[j]:.2f} g {m.gamma[j]:+.2f}" + (f" lam {m.lam[j]:+.2f} kap {m.kap[j]:+.2f}" if feats else "")
          + (" beta " + " ".join(f"{b:+.2f}" for b in m.beta[j]) if use_cov else "") + f"  pi {m.pi[j]:.3f}", flush=True)
idx = {"".join(q[1]): i for i, q in enumerate(items)}
def p_stop(ctx, mind, S2, N2):
    i = idx[ctx]; j = irt.MINDS.index(mind)
    L = m.comp_loglik_full(S2[i:i+1], N2[i:i+1], X[i:i+1], Fo[i:i+1], Ft[i:i+1], C[i:i+1] if use_cov else None)[0]
    r = np.exp(L - np.logaddexp.reduce(L))
    return float(r @ m.cond_next_row(Fo[i], Ft[i], X[i], j, int(S2[i, j]), int(N2[i, j])) if not m.K else r @ _cn(i, j, int(S2[i, j]), int(N2[i, j])))
def _cn(i, j, k, n):
    z = m.alpha[j] + m.slope[j] * spx.G + m.gamma[j] * X[i] + ((m.lam[j] * Fo[i, j] + m.kap[j] * Ft[i, j]) if m.feats else 0) + float(C[i] @ m.beta[j])
    p = 1 / (1 + np.exp(-z)); lf = k * np.log(p) + (n - k) * np.log1p(-p)
    lh = float(spx.logbb(np.array([k]), np.array([n]), m.a[j], m.b[j])[0])
    l0 = np.log1p(-m.pi[j]) + lf; l1 = np.log(m.pi[j]) + lh; q1 = np.exp(l1 - np.logaddexp(l0, l1))
    return (1 - q1) * p + q1 * (m.a[j] + k) / (m.a[j] + m.b[j] + n)
def answers(rid):
    rs = [json.loads(l) for l in open(lib.ROOT / "data" / "answers" / f"{rid}.jsonl") if l.strip()]
    return [r for r in rs if not lib.sealed(r) and r["kind"] == "continue" and r["outcome"] in ("none", "continuation")]
def score(rid, S2, N2):
    by = {}
    for r in answers(rid): by.setdefault(r["mind"], []).append(r)
    for mind, L in sorted(by.items()):
        ps = [p_stop("".join(r["context"]), mind, S2, N2) for r in L]; ys = [r["outcome"] == "none" for r in L]
        ll = sum(np.log(p if y else 1 - p) for p, y in zip(ps, ys))
        print(f"   {rid} {mind:14s} stops {sum(ys)} of {len(ys)}  expected {sum(ps):.1f}  log score {ll:.2f}", flush=True)
    return by
p1 = score("p001", S, N)
S2, N2 = S.copy(), N.copy()
for mind, L in p1.items():
    for r in L:
        i = idx["".join(r["context"])]; j = irt.MINDS.index(mind); S2[i, j] += r["outcome"] == "none"; N2[i, j] += 1
score("p002", S2, N2)
if "--no-preq" not in sys.argv:
    rows = preq.prefixes(items, seq, irt.MINDS)
    PFo, PFt = lnb_prefix.prefix_features(items, seq, rows, composition_free=cf)
    if not own: PFo = np.zeros_like(PFo)
    preq.report(preq.score({None: spx.RowAdapterC(m, PFo, PFt, C, rows)}, None, items, seq, X), f"{V}, strict prequential")
