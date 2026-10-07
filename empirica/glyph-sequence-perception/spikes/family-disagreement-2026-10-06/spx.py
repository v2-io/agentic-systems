"""Strengthening 2: a SPARSE mind x item interaction, plus the mind x sequence (block-set) features of lnb.py.

For each (item i, mind m), a latent z_im ~ Bernoulli(pi_m):
  z = 0  the mind follows the shared model:  logit p = alpha_m + s_m b_i + gamma_m x_i + lam_m F_own + kap_m F_oth
  z = 1  the mind has its own propensity on this item: p_im ~ Beta(a_m, b_m) (U-shaped when a, b < 1), shared by all of
         that mind's answers on the item and by no other mind's
b ~ nonparametric weights on a 41-point grid (per familiarity x). pi_m small means a mind departs on few items, but
strongly (the verifier's 'a mind that keeps stopping where everyone else continues'); the Gaussian intercept of irtu /
lnb spreads departures over every item instead. Anchors: sonnet55 alpha = 0, s = 1, gamma = 0. EM; Beta parameters
per mind by grid search on the expected log-likelihood."""
import numpy as np
import irt, lnb

G = lnb.G
ABGRID = [0.05, 0.1, 0.2, 0.3, 0.5, 0.8, 1.2, 2.0]

def logbb(k, n, a, b):
    """log of B(k + a, n - k + b) / B(a, b), the beta-binomial without the binomial coefficient (arrays k, n)"""
    from math import lgamma
    lg = np.vectorize(lgamma)
    return lg(k + a) + lg(n - k + b) - lg(n + a + b) - (lg(a) + lg(b) - lg(a + b))

class SPX:
    def __init__(s, feats=True, pi0=0.05):
        M = len(irt.MINDS); s.feats = feats
        s.alpha = np.zeros(M); s.slope = np.ones(M); s.gamma = np.zeros(M); s.lam = np.zeros(M); s.kap = np.zeros(M)
        s.pi = np.full(M, pi0); s.a = np.full(M, 0.3); s.b = np.full(M, 0.3)
        s.w = np.ones((2, len(G))) / len(G); s.j0 = irt.MINDS.index("sonnet55")
    def _z(s, X, Fo, Ft):
        off = s.gamma[None, :] * X[:, None] + ((s.lam[None, :] * Fo + s.kap[None, :] * Ft) if s.feats else 0)
        return s.alpha[None, None, :] + s.slope[None, None, :] * G[None, :, None] + off[:, None, :]    # (I, G, M)
    def _terms(s, S, N, X, Fo, Ft):
        z = s._z(X, Fo, Ft); lp = -np.logaddexp(0, -z); lq = -np.logaddexp(0, z)
        lf = S[:, None, :] * lp + (N - S)[:, None, :] * lq                                              # (I, G, M) z=0
        lh = np.stack([logbb(S[:, j], N[:, j], s.a[j], s.b[j]) for j in range(S.shape[1])], 1)        # (I, M)    z=1
        l0 = np.log1p(-s.pi)[None, None, :] + lf; l1 = (np.log(s.pi)[None, :] + lh)[:, None, :]
        lm = np.logaddexp(l0, l1); lm = np.where(N[:, None, :] > 0, lm, 0.0)
        return lm, l0, l1, z
    def comp_loglik_full(s, S, N, X, Fo, Ft):
        lm, _, _, _ = s._terms(S, N, X, Fo, Ft)
        return lm.sum(2) + np.log(np.maximum(s.w[X.astype(int)], 1e-300))
    def fit(s, S, N, X, Fo, Ft, iters=150, tol=1e-7, chunk=6000, verbose=False):
        I, M = S.shape; prev = -np.inf; Xi = X.astype(int); npar = 5 if s.feats else 3
        # Beta part's per-mind sufficient statistics are (k, n) pairs weighted by E[z]
        for it in range(iters):
            ll = 0.0; grad = np.zeros((M, npar)); info = np.zeros((M, npar, npar)); wnew = np.zeros((2, len(G)))
            ez_num = np.zeros(M); ez_den = np.zeros(M); kn_w = [dict() for _ in range(M)]
            for c0 in range(0, I, chunk):
                sl = slice(c0, c0 + chunk)
                lm, l0, l1, z = s._terms(S[sl], N[sl], X[sl], Fo[sl], Ft[sl])
                L = lm.sum(2) + np.log(np.maximum(s.w[Xi[sl]], 1e-300)); tot = np.logaddexp.reduce(L, 1); ll += tot.sum()
                R = np.exp(L - tot[:, None])                                                              # (n, G)
                for x in (0, 1): wnew[x] += R[Xi[sl] == x].sum(0)
                pz1 = np.exp(l1 - lm)                                                                     # (n, G, M)
                has = (N[sl] > 0)
                ez = (R[:, :, None] * pz1).sum(1) * has                                                   # (n, M) E[z]
                ez_num += ez.sum(0); ez_den += has.sum(0)
                for j in range(M):
                    ii = np.where(has[:, j])[0]
                    for k_, n_, e_ in zip(S[sl][ii, j].astype(int), N[sl][ii, j].astype(int), ez[ii, j]):
                        kn_w[j][(k_, n_)] = kn_w[j].get((k_, n_), 0.0) + e_
                w0 = R[:, :, None] * (1 - pz1) * has[:, None, :]                                          # weight of z=0
                p = 1 / (1 + np.exp(-z))
                res = w0 * (S[sl][:, None, :] - N[sl][:, None, :] * p); cur = w0 * N[sl][:, None, :] * p * (1 - p)
                fl = [np.ones_like(p), np.broadcast_to(G[None, :, None], p.shape), np.broadcast_to(X[sl][:, None, None].astype(float), p.shape)]
                if s.feats: fl += [np.broadcast_to(Fo[sl][:, None, :], p.shape), np.broadcast_to(Ft[sl][:, None, :], p.shape)]
                for a_ in range(npar):
                    grad[:, a_] += (fl[a_] * res).sum((0, 1))
                    for b_ in range(a_, npar):
                        v = (fl[a_] * fl[b_] * cur).sum((0, 1)); info[:, a_, b_] += v; info[:, b_, a_] = info[:, a_, b_]
            if verbose: print(it, round(ll, 1), np.round(s.pi, 3))
            if ll - prev < tol * abs(ll): break
            prev = ll; s.w = wnew / np.maximum(wnew.sum(1, keepdims=True), 1e-12)
            s.pi = np.clip(ez_num / np.maximum(ez_den, 1), 1e-4, 0.5)
            for j in range(M):
                free = [a_ for a_ in range(npar) if not (j == s.j0 and a_ in (0, 1, 2))]
                st = np.clip(np.linalg.solve(info[j][np.ix_(free, free)] + 1e-6 * np.eye(len(free)), grad[j][free]), -0.5, 0.5)
                th = [s.alpha, s.slope, s.gamma, s.lam, s.kap]
                for a_, d in zip(free, st): th[a_][j] += d
                if kn_w[j]:
                    ks = np.array([k for k, _ in kn_w[j]]); ns = np.array([n for _, n in kn_w[j]]); ws = np.array(list(kn_w[j].values()))
                    best = max(((aa, bb) for aa in ABGRID for bb in ABGRID), key=lambda ab: float((ws * logbb(ks, ns, ab[0], ab[1])).sum()))
                    s.a[j], s.b[j] = best
        s.ll = ll; s.iters = it
        return s
    def cond_next_row(s, Fo_row, Ft_row, x, j, k, n):
        """(G,) P(next answer of mind j = 1 | grid point, its own k of n on the item)"""
        z = s.alpha[j] + s.slope[j] * G + s.gamma[j] * x + ((s.lam[j] * Fo_row[j] + s.kap[j] * Ft_row[j]) if s.feats else 0)
        p = 1 / (1 + np.exp(-z)); lf = k * np.log(p) + (n - k) * np.log1p(-p)
        lh = float(logbb(np.array([k]), np.array([n]), s.a[j], s.b[j])[0])
        l0 = np.log1p(-s.pi[j]) + lf; l1 = np.log(s.pi[j]) + lh; q1 = np.exp(l1 - np.logaddexp(l0, l1))
        return (1 - q1) * p + q1 * (s.a[j] + k) / (s.a[j] + s.b[j] + n)

class ItemAdapter:
    """preq adapter with item-level features (all-snapshot, leave-item-out) -- or row-level via RowAdapter below"""
    def __init__(s, m, Fo, Ft): s.m, s.Fo, s.Ft = m, Fo, Ft; s.rows = None
    def comp_loglik(s, S, N, X):
        r = s.rows if s.rows is not None else np.arange(len(S)); return s.m.comp_loglik_full(S, N, X, s.Fo[r], s.Ft[r])
    def cond_next_item(s, i, x, j, k, n): return s.m.cond_next_row(s.Fo[i], s.Ft[i], x, j, k, n)

class RowAdapter:
    def __init__(s, m, Fo, Ft): s.m, s.Fo, s.Ft = m, Fo, Ft; s.cur = None
    def comp_loglik(s, S, N, X): return s.m.comp_loglik_full(S, N, X, s.Fo[s.cur], s.Ft[s.cur])
    def cond_next_row(s, row, x, j, k, n): return s.m.cond_next_row(s.Fo[row], s.Ft[row], x, j, k, n)
