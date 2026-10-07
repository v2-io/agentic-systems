"""Selection-robust checks (strengthening 2). The planner re-asks a context far more often after some answers than
others (Sonnet: re-asked in a later round 0.077 of the time after continuing, 0.005 after stopping), so a mind's repeats
are a population selected on its own first answer. Predictions of repeats must therefore condition on that answer:
adaptive designs are ignorable for posterior prediction only given everything the design used.

A model adapter exposes comp_loglik(S, N, X) -> (I, C) and cond_next(x, j, k, n) -> (C,) = P(next answer of mind j is 1
| component, mind j's own k of n earlier answers on the item). Checks:
  cross    first answers of A and B (asked on the same sheet, so not selected on each other): P(differ) from the
           posterior given the OTHER minds' answers;
  within   items a mind answered in two different rounds: P(second differs from first | first, all other minds);
  flatC    items A and B each answered >= 2 times, first answers opposite: P(both second answers repeat the first
           | first answers, all other minds) -- the selection-robust form of the flat-split count.
Bands: Poisson-binomial over the per-item probabilities (2,000 draws)."""
import numpy as np
import irt, checks

def _post(m, S1, N1, x):
    L = m.comp_loglik(S1[None], N1[None], np.array([x]))[0]
    return np.exp(L - np.logaddexp.reduce(L))

def run(m, items, seq, S, N, X, label, minds=("sonnet55", "grok46", "haiku45nt", "haiku45", "opus55", "gemini38flash"), pairs=None):
    M = irt.MINDS; pairs = pairs or irt.PAIRS; out = {"label": label, "within": [], "flat": [], "cross": []}
    for mm in minds:
        j = M.index(mm); q, o = [], []
        for i in np.where(N[:, j] >= 2)[0]:
            L2 = sorted(seq[items[i]][mm], key=lambda t: t[0])
            if L2[0][0] == L2[1][0]: continue
            y1, y2 = L2[0][1], L2[1][1]
            S1, N1 = S[i].copy(), N[i].copy(); S1[j] = y1; N1[j] = 1
            r = _post(m, S1, N1, X[i]); p2 = r @ m.cond_next(X[i], j, y1, 1)
            q.append(p2 if y1 == 0 else 1 - p2); o.append(y2 != y1)
        if len(q) >= 100:
            out["within"].append((mm, len(q), int(sum(o)), float(sum(q)), checks.band(q)))
    for A, B in pairs:
        a, b = M.index(A), M.index(B)
        R = checks.posterior(m, S, N, X, [a, b]); qd, od = [], 0
        cells = {(0, 1): ([], 0), (1, 0): ([], 0)}
        for i in np.where((N[:, a] > 0) & (N[:, b] > 0))[0]:
            ya = [y for _, y in sorted(seq[items[i]][A])]; yb = [y for _, y in sorted(seq[items[i]][B])]
            pa = m.cond_next(X[i], a, 0, 0); pb = m.cond_next(X[i], b, 0, 0)
            qd.append(R[i] @ (pa * (1 - pb) + pb * (1 - pa))); od += ya[0] != yb[0]
            if len(ya) >= 2 and len(yb) >= 2 and ya[0] != yb[0]:
                S1, N1 = S[i].copy(), N[i].copy(); S1[a], N1[a], S1[b], N1[b] = ya[0], 1, yb[0], 1
                r = _post(m, S1, N1, X[i])
                qa = m.cond_next(X[i], a, ya[0], 1); qb = m.cond_next(X[i], b, yb[0], 1)
                qa = qa if ya[0] == 1 else 1 - qa; qb = qb if yb[0] == 1 else 1 - qb
                L_, c_ = cells[(ya[0], yb[0])]; L_.append(r @ (qa * qb)); cells[(ya[0], yb[0])] = (L_, c_ + (ya[1] == ya[0] and yb[1] == yb[0]))
        out["cross"].append((A, B, len(qd), od, sum(qd), checks.band(qd)))
        for k, (L_, c_) in cells.items():
            if len(L_) >= 15: out["flat"].append((A, B, k, len(L_), c_, sum(L_), checks.band(L_)))
    return out

def show(out):
    bad = 0; print(f"== {out['label']}")
    print("  cross-mind first answers, disagreements obs / pred [95%]")
    for A, B, n, o, e, (lo, hi) in out["cross"]:
        f = "" if lo <= o <= hi else "  <-- outside"; bad += bool(f)
        print(f"    {A:14s}{B:14s} n={n:5d} {o:5d} / {e:7.1f} [{lo}-{hi}]  ratio {o/e:.2f}{f}")
    print("  within-mind: second answer differs from first, given the first (different rounds), obs / pred [95%]")
    for mm, n, o, e, (lo, hi) in out["within"]:
        f = "" if lo <= o <= hi else "  <-- outside"; bad += bool(f)
        print(f"    {mm:14s} n={n:5d} {o:4d} / {e:6.1f} [{lo}-{hi}]{f}")
    print("  flat, selection-robust: first answers opposite (A, B); both second answers repeat; obs / pred [95%]")
    for A, B, k, n, o, e, (lo, hi) in out["flat"]:
        f = "" if lo <= o <= hi else "  <-- outside"; bad += bool(f)
        print(f"    {A:14s}{B:14s} first {k} n={n:4d} {o:4d} / {e:6.1f} [{lo}-{hi}]{f}")
    print(f"  checks outside their band: {bad}"); return bad

# ---------------------------------------------------------------- adapters
class Adapt2mf:
    def __init__(s, m): s.m = m
    def comp_loglik(s, S, N, X): return s.m.comp_loglik(S, N, X)
    def cond_next(s, x, j, k, n): return s.m.comp_probs(x)[:, j]

class AdaptU:
    """the verifier's irtu (de-novo-2/irtu.py): within the graded class a mind's earlier answers update its u"""
    def __init__(s, m): s.m = m
    def comp_loglik(s, S, N, X): return s.m.comp_loglik(S, N, X)
    def cond_next(s, x, j, k, n):
        import irtu
        m = s.m; z = m.alpha[j] + m.slope[j] * irtu.G[:, None] + m.gamma[j] * x + m.tau[j] * irtu.U[None, :]
        p = 1 / (1 + np.exp(-z)); w = irtu.W[None, :] * p ** k * (1 - p) ** (n - k)
        g = (w * p).sum(1) / w.sum(1)
        return np.concatenate([[m.eps[x][j]], [1 - m.dlt[x][j]], g])

class AdaptBB:
    def __init__(s, m): s.m = m
    def comp_loglik(s, S, N, X): return s.m.comp_loglik(S, N, X)
    def cond_next(s, x, j, k, n): return s.m.next1(x, j, k, n)
