"""Prequential scoring for LNB with features computed from EARLIER ROUNDS ONLY: for each (item, round) prefix row,
F_own / F_oth use only answers given before that round, on other items of the same group (lnb.block_features' rule
otherwise). Parameters are the all-data fit. Same report as preq.py (groups, flips, same-round pairs)."""
import bisect, collections, pickle, sys, numpy as np
import irt, lnb, preq

def prefix_features(items, seq, rows, grouping="blockset", pseudo=2.0, minds=irt.MINDS):
    M = len(minds); gf = lnb.GROUPINGS[grouping]; grp = [gf(q[1]) for q in items]
    ev = collections.defaultdict(list)                     # (group, mind) -> [(round, item, y)]
    allev = collections.defaultdict(list)                  # mind -> [(round, y)]
    for i, q in enumerate(items):
        for mm, L in seq[q].items():
            j = minds.index(mm)
            for rd, y in L: ev[(grp[i], j)].append((rd, i, y)); allev[j].append((rd, y))
    cum = {}
    for key, L in ev.items():
        L.sort(); rds = [r for r, _, _ in L]; cy = np.cumsum([y for _, _, y in L]); cum[key] = (rds, cy, L)
    gcum = {}
    for j, L in allev.items():
        L.sort(); gcum[j] = ([r for r, _ in L], np.cumsum([y for _, y in L]))
    def before(key, t):
        if key not in cum: return 0.0, 0
        rds, cy, L = cum[key]; k = bisect.bisect_left(rds, t)
        return (float(cy[k - 1]) if k else 0.0), k
    def own_item_before(i, j, t):
        L = [y for rd, y in seq[items[i]].get(minds[j], []) if rd < t]; return float(sum(L)), len(L)
    Fo = np.zeros((len(rows), M)); Ft = np.zeros((len(rows), M))
    for r_, (i, t, Sp, Np, ans) in enumerate(rows):
        g = grp[i]; ks = np.zeros(M); ns = np.zeros(M); rate = np.zeros(M)
        for j in range(M):
            k, n = before((g, j), t); ki, ni = own_item_before(i, j, t); ks[j], ns[j] = k - ki, n - ni
            gr, gc = gcum.get(j, ([], np.array([0])))
            kk = bisect.bisect_left(gr, t); rate[j] = ((float(gc[kk - 1]) if kk else 0.0) + 0.5) / (kk + 1.0)
        for j in range(M):
            if ns[j] > 0:
                p = (ks[j] + pseudo * rate[j]) / (ns[j] + pseudo); Fo[r_, j] = np.log(p / (1 - p)) - np.log(rate[j] / (1 - rate[j]))
            ko, no = ks.sum() - ks[j], ns.sum() - ns[j]
            if no > 0:
                rr = rate[np.arange(M) != j].mean()
                p = (ko + pseudo * rr) / (no + pseudo); Ft[r_, j] = np.log(p / (1 - p)) - np.log(rr / (1 - rr))
    return Fo, Ft

class RowAdapter:
    """features per prefix row; preq.score calls comp_loglik on its selected rows in order, then cond_next_item"""
    def __init__(s, m, Fo, Ft, rows): s.m, s.Fo, s.Ft = m, Fo, Ft; s.key = {(r[0], r[1]): k for k, r in enumerate(rows)}; s.rows = None; s.cur = None
    def comp_loglik(s, S, N, X):
        return s.m.comp_loglik_full(S, N, X, s.Fo[s.cur], s.Ft[s.cur])
    def cond_next_row(s, row, x, j, k, n):
        m = s.m; off = m.gamma[j] * x + m.lam[j] * s.Fo[row, j] + m.kap[j] * s.Ft[row, j]
        z = m.alpha[j] + m.slope[j] * lnb.G[:, None] + off + m.tau[j] * lnb.U[None, :]
        p = 1 / (1 + np.exp(-z)); w = lnb.W[None, :] * p ** k * (1 - p) ** (n - k); return (w * p).sum(1) / w.sum(1)
