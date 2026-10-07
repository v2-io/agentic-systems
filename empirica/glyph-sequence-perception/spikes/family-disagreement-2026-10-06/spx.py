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

import os
G = np.linspace(-10, 10, 81) if os.environ.get("SPX_GRID") == "wide" else lnb.G   # wide: the anchor mind (Sonnet, slope 1) can reach logit +-10
ABGRID = [0.05, 0.1, 0.2, 0.3, 0.5, 0.8, 1.2, 2.0]

def logbb(k, n, a, b):
    """log of B(k + a, n - k + b) / B(a, b), the beta-binomial without the binomial coefficient (arrays k, n)"""
    from math import lgamma
    lg = np.vectorize(lgamma)
    return lg(k + a) + lg(n - k + b) - lg(n + a + b) - (lg(a) + lg(b) - lg(a + b))

class SPX:
    def __init__(s, feats=True, pi0=0.05, cov=None, cov_shared=False, own=True, sparse=True):
        """cov: (I, K) glyph covariates bound to the items fitted (rows must align with S); cov_shared: one coefficient
        vector for all minds; own=False drops the own-sequence feature (lam fixed 0); sparse=False drops the sparse
        interaction (pi fixed ~0)."""
        M = len(irt.MINDS); s.feats = feats; s.cov = cov; s.cov_shared = cov_shared; s.own = own; s.sparse = sparse
        s.K = 0 if cov is None else cov.shape[1]; s.beta = np.zeros((M, s.K))
        s.alpha = np.zeros(M); s.slope = np.ones(M); s.gamma = np.zeros(M); s.lam = np.zeros(M); s.kap = np.zeros(M)
        s.pi = np.full(M, pi0); s.a = np.full(M, 0.3); s.b = np.full(M, 0.3)
        s.w = np.ones((2, len(G))) / len(G); s.j0 = irt.MINDS.index("sonnet55")
    def _z(s, X, Fo, Ft, C=None):
        off = s.gamma[None, :] * X[:, None] + ((s.lam[None, :] * Fo + s.kap[None, :] * Ft) if s.feats else 0)
        if s.K: off = off + C @ s.beta.T                                                              # (I, M)
        return s.alpha[None, None, :] + s.slope[None, None, :] * G[None, :, None] + off[:, None, :]    # (I, G, M)
    def _terms(s, S, N, X, Fo, Ft, C=None):
        z = s._z(X, Fo, Ft, C); lp = -np.logaddexp(0, -z); lq = -np.logaddexp(0, z)
        lf = S[:, None, :] * lp + (N - S)[:, None, :] * lq                                              # (I, G, M) z=0
        lh = np.stack([logbb(S[:, j], N[:, j], s.a[j], s.b[j]) for j in range(S.shape[1])], 1)        # (I, M)    z=1
        l0 = np.log1p(-s.pi)[None, None, :] + lf; l1 = (np.log(s.pi)[None, :] + lh)[:, None, :]
        lm = np.logaddexp(l0, l1); lm = np.where(N[:, None, :] > 0, lm, 0.0)
        return lm, l0, l1, z
    def comp_loglik_full(s, S, N, X, Fo, Ft, C=None):
        lm, _, _, _ = s._terms(S, N, X, Fo, Ft, C)
        return lm.sum(2) + np.log(np.maximum(s.w[X.astype(int)], 1e-300))
    def fit(s, S, N, X, Fo, Ft, iters=150, tol=1e-7, chunk=6000, verbose=False, C=None):
        I, M = S.shape; prev = -np.inf; Xi = X.astype(int); npar = (5 if s.feats else 3) + s.K
        if not s.sparse: s.pi[:] = 1e-6
        Cm = np.zeros((I, 0)) if C is None else C
        # Beta part's per-mind sufficient statistics are (k, n) pairs weighted by E[z]
        for it in range(iters):
            ll = 0.0; grad = np.zeros((M, npar)); info = np.zeros((M, npar, npar)); wnew = np.zeros((2, len(G)))
            ez_num = np.zeros(M); ez_den = np.zeros(M); kn_w = [dict() for _ in range(M)]
            for c0 in range(0, I, chunk):
                sl = slice(c0, c0 + chunk)
                lm, l0, l1, z = s._terms(S[sl], N[sl], X[sl], Fo[sl], Ft[sl], Cm[sl] if s.K else None)
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
                for kk in range(s.K): fl.append(np.broadcast_to(Cm[sl][:, kk][:, None, None], p.shape))
                for a_ in range(npar):
                    grad[:, a_] += (fl[a_] * res).sum((0, 1))
                    for b_ in range(a_, npar):
                        v = (fl[a_] * fl[b_] * cur).sum((0, 1)); info[:, a_, b_] += v; info[:, b_, a_] = info[:, a_, b_]
            if verbose: print(it, round(ll, 1), np.round(s.pi, 3), flush=True)
            if ll - prev < tol * abs(ll): break
            prev = ll; s.w = wnew / np.maximum(wnew.sum(1, keepdims=True), 1e-12)
            s.pi = np.clip(ez_num / np.maximum(ez_den, 1), 1e-4, 0.5) if s.sparse else np.full(M, 1e-6)
            nb = 5 if s.feats else 3
            cov_idx = list(range(nb, npar))
            for j in range(M):
                free = [a_ for a_ in range(npar) if not (j == s.j0 and a_ in (0, 1, 2)) and not (s.feats and not s.own and a_ == 3)
                        and not (s.cov_shared and a_ in cov_idx)]
                st = np.clip(np.linalg.solve(info[j][np.ix_(free, free)] + 1e-6 * np.eye(len(free)), grad[j][free]), -0.5, 0.5)
                for a_, d in zip(free, st):
                    if a_ == 0: s.alpha[j] += d
                    elif a_ == 1: s.slope[j] += d
                    elif a_ == 2: s.gamma[j] += d
                    elif s.feats and a_ == 3: s.lam[j] += d
                    elif s.feats and a_ == 4: s.kap[j] += d
                    else: s.beta[j, a_ - nb] += d
            if s.cov_shared and s.K:
                g_ = grad[:, cov_idx].sum(0); H_ = info[:, cov_idx][:, :, cov_idx].sum(0)
                st = np.clip(np.linalg.solve(H_ + 1e-6 * np.eye(len(cov_idx)), g_), -0.5, 0.5); s.beta += st[None, :]
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

class RowAdapterC:
    """prequential adapter with per-row sequence features and per-item covariates (rows from preq.prefixes)"""
    def __init__(s, m, Fo, Ft, C, rows): s.m, s.Fo, s.Ft, s.C = m, Fo, Ft, C; s.item = np.array([r[0] for r in rows]); s.cur = None
    def comp_loglik(s, S, N, X): return s.m.comp_loglik_full(S, N, X, s.Fo[s.cur], s.Ft[s.cur], s.C[s.item[s.cur]] if s.m.K else None)
    def cond_next_row(s, row, x, j, k, n):
        m = s.m; z = m.alpha[j] + m.slope[j] * G + m.gamma[j] * x + ((m.lam[j] * s.Fo[row, j] + m.kap[j] * s.Ft[row, j]) if m.feats else 0)
        if m.K: z = z + float(s.C[s.item[row]] @ m.beta[j])
        p = 1 / (1 + np.exp(-z)); lf = k * np.log(p) + (n - k) * np.log1p(-p)
        lh = float(logbb(np.array([k]), np.array([n]), m.a[j], m.b[j])[0])
        l0 = np.log1p(-m.pi[j]) + lf; l1 = np.log(m.pi[j]) + lh; q1 = np.exp(l1 - np.logaddexp(l0, l1))
        return (1 - q1) * p + q1 * (m.a[j] + k) / (m.a[j] + m.b[j] + n)
