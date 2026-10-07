"""One check harness for any model exposing comp_loglik(S, N, X) -> (I, C) log P(component, answers), and per
component (C,) quantities p1(x, j), disagree2(x, j), allsame(x, j, n, y). The three checks of strengthening 2:
cross-mind single-answer disagreement, within-mind disagreement of first two answers from different rounds, flat-split
counts both ways; each against a 95% band from the per-item probabilities (Poisson-binomial, 2,000 draws)."""
import numpy as np
import irt

def band(q, draws=2000, seed=0):
    rng = np.random.default_rng(seed); q = np.asarray(q)
    if not len(q): return (0, 0)
    c = (rng.random((draws, len(q))) < q[None, :]).sum(1)
    return int(np.quantile(c, 0.025)), int(np.quantile(c, 0.975))

def posterior(m, S, N, X, excl):
    So, No = S.copy(), N.copy(); So[:, excl] = 0; No[:, excl] = 0
    L = m.comp_loglik(So, No, X); return np.exp(L - np.logaddexp.reduce(L, 1)[:, None])

def run(m, items, seq, S, N, X, label, minds_within=("sonnet55", "grok46", "haiku45nt", "haiku45", "opus55", "gemini38flash"), pairs=None):
    M = irt.MINDS; pairs = pairs or irt.PAIRS; out = {"label": label, "cross": [], "within": [], "flat": []}
    cache = {}
    def comp(x, j, what, *args):
        k = (x, j, what) + args
        if k not in cache: cache[k] = getattr(m, what)(x, j, *args)
        return cache[k]
    for A, B in pairs:
        a, b = M.index(A), M.index(B); R = posterior(m, S, N, X, [a, b])
        qd, od, qf1, of1, qf2, of2 = [], 0, [], 0, [], 0
        for i in np.where((N[:, a] > 0) & (N[:, b] > 0))[0]:
            ya = [y for _, y in sorted(seq[items[i]][A])]; yb = [y for _, y in sorted(seq[items[i]][B])]
            pa, pb = comp(X[i], a, "p1"), comp(X[i], b, "p1")
            qd.append(R[i] @ (pa * (1 - pb) + pb * (1 - pa))); od += ya[0] != yb[0]
            if len(ya) >= 2 and len(yb) >= 2:
                qf1.append(R[i] @ (comp(X[i], a, "allsame", len(ya), 0) * comp(X[i], b, "allsame", len(yb), 1)))
                qf2.append(R[i] @ (comp(X[i], a, "allsame", len(ya), 1) * comp(X[i], b, "allsame", len(yb), 0)))
                of1 += (not any(ya)) and all(yb); of2 += all(ya) and not any(yb)
        out["cross"].append((A, B, len(qd), od, sum(qd), band(qd)))
        if len(qf1) >= 20:
            out["flat"].append((A, B, len(qf1), of1, sum(qf1), band(qf1), of2, sum(qf2), band(qf2)))
    for mm in minds_within:
        j = M.index(mm); R = posterior(m, S, N, X, [j]); q, o, pp = [], [], []
        for i in np.where(N[:, j] >= 2)[0]:
            L2 = sorted(seq[items[i]][mm], key=lambda t: t[0])
            if L2[0][0] == L2[1][0]: continue
            q.append(R[i] @ comp(X[i], j, "disagree2")); o.append(L2[0][1] != L2[1][1]); pp.append(R[i] @ comp(X[i], j, "p1"))
        if len(q) >= 100:
            q, o, pp = np.array(q), np.array(o), np.array(pp)
            bins = []
            for lo, hi in ((0, .2), (.2, .4), (.4, .6), (.6, .8), (.8, 1.01)):
                k = (pp >= lo) & (pp < hi)
                if k.sum() >= 20: bins.append((lo, hi, int(k.sum()), int(o[k].sum()), float(q[k].sum()), band(q[k])))
            out["within"].append((mm, len(q), int(o.sum()), float(q.sum()), band(q), bins))
    return out

def show(out):
    print(f"== {out['label']}")
    bad = 0
    print("  cross-mind single-answer disagreement: obs / pred [95%]")
    for A, B, n, o, e, (lo, hi) in out["cross"]:
        flag = "" if lo <= o <= hi else "  <-- outside"; bad += bool(flag)
        print(f"    {A:14s}{B:14s} n={n:5d}  {o:5d} / {e:7.1f} [{lo}-{hi}]  ratio {o/e:.2f}{flag}")
    print("  within-mind, first two answers from different rounds, disagreements: obs / pred [95%]")
    for mm, n, o, e, (lo, hi), bins in out["within"]:
        flag = "" if lo <= o <= hi else "  <-- outside"; bad += bool(flag)
        print(f"    {mm:14s} n={n:5d}  {o:4d} / {e:6.1f} [{lo}-{hi}]{flag}")
        for blo, bhi, bn, bo, be, (l2, h2) in bins:
            f2 = "" if l2 <= bo <= h2 else "  <-- outside"; bad += bool(f2)
            print(f"        P(1) {blo:.1f}-{bhi:.1f}: n={bn:4d}  {bo:4d} / {be:6.1f} [{l2}-{h2}]{f2}")
    print("  flat splits (each >= 2 answers): A0/B1 and A1/B0, obs / pred [95%]")
    for A, B, n, o1, e1, (l1, h1), o2, e2, (l2, h2) in out["flat"]:
        f1 = "" if l1 <= o1 <= h1 else " <--"; f2 = "" if l2 <= o2 <= h2 else " <--"; bad += bool(f1) + bool(f2)
        print(f"    {A:14s}{B:14s} n={n:5d}  {o1:3d} / {e1:6.1f} [{l1}-{h1}]{f1}   {o2:3d} / {e2:6.1f} [{l2}-{h2}]{f2}")
    print(f"  checks outside their band: {bad}")
    return bad
