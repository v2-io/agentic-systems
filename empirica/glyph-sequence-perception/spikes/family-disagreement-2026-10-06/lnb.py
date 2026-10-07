"""Strengthening 2: the item model with a mind x block term.

    logit P(stop | m, i, b, u) = alpha_m + s_m b + gamma_m x_i + lam_m F_own[i,m] + kap_m F_oth[i,m] + tau_m u_im
    b ~ nonparametric weights on a 41-point grid (per familiarity population x), u_im ~ N(0, 1) (9-point Hermite)

F_own[i,m]: mind m's stop rate on the OTHER items whose context ends in the same Unicode block as item i (the item
itself left out), as a log-odds shrunk to m's overall rate with 2 pseudo-answers, centred at m's overall log-odds; 0 if
m answered nothing else in the block. F_oth[i,m]: the same for the other minds pooled (m and item i left out). So lam_m
is mind m's own block propensity beyond what its item position and the other minds' block behaviour predict: a mind x
block interaction. With lam = kap = 0 and the grid prior this is the verifier's irtu with a nonparametric b.
Anchors: sonnet55 alpha = 0, s = 1, gamma = 0. EM; the M-step is Newton per mind over (alpha, s, gamma, tau, lam, kap).
"""
import collections, numpy as np
import irt, features as F

G = np.linspace(-5, 5, 41)
U, W = np.polynomial.hermite_e.hermegauss(9); W = W / W.sum(); LW = np.log(W)

GROUPINGS = {"block": lambda c: F.block(c[-1]), "blockset": lambda c: frozenset(F.block(g) for g in c)}

def block_features(items, S, N, minds=irt.MINDS, pseudo=2.0, exclude_items=None, grouping="block", composition_free=False):
    """F_own, F_oth (I, M), from answers on other items of the same block (vectorised). exclude_items: items whose
    answers may not be used as anyone's features (none by default)."""
    I, M = S.shape; gf = GROUPINGS[grouping]; blk = [gf(q[1]) for q in items]
    names = sorted(set(blk), key=repr); idx = {b: k for k, b in enumerate(names)}; bi = np.array([idx[b] for b in blk])
    use = np.ones(I, bool) if exclude_items is None else ~exclude_items
    Su, Nu = S * use[:, None], N * use[:, None]
    rate = (Su.sum(0) + 0.5) / (Nu.sum(0) + 1.0); lr = np.log(rate / (1 - rate))
    kb = np.zeros((len(names), M)); nb = np.zeros((len(names), M)); np.add.at(kb, bi, Su); np.add.at(nb, bi, Nu)
    k = kb[bi] - Su; n = nb[bi] - Nu                                  # other items of the block, per mind
    p = (k + pseudo * rate[None, :]) / (n + pseudo)
    Fo = np.where(n > 0, np.log(p / (1 - p)) - lr[None, :], 0.0)
    if composition_free:
        # each other mind's own centred log-odds on the group, averaged with equal weight over the minds present
        # (de-novo-feedback-3 §2a: a pooled rate reads 'stop' wherever high-threshold minds answered most)
        L = np.where(n > 0, np.log(p / (1 - p)) - lr[None, :], np.nan)                 # (I, M) per mind
        Ft = np.zeros((I, M))
        for j in range(M):
            others = np.delete(L, j, axis=1)
            cnt = np.sum(~np.isnan(others), 1)
            Ft[:, j] = np.where(cnt > 0, np.nansum(others, 1) / np.maximum(cnt, 1), 0.0)
        return Fo, Ft, blk
    ko = k.sum(1, keepdims=True) - k; no = n.sum(1, keepdims=True) - n  # other minds pooled, other items
    rr = (Su.sum() - Su.sum(0) + 0.5) / (Nu.sum() - Nu.sum(0) + 1.0)
    p2 = (ko + pseudo * rr[None, :]) / (no + pseudo)
    Ft = np.where(no > 0, np.log(p2 / (1 - p2)) - np.log(rr / (1 - rr))[None, :], 0.0)
    return Fo, Ft, blk

class LNB:
    def __init__(s, feats=True, tau0=1.0):
        M = len(irt.MINDS); s.feats = feats
        s.alpha = np.zeros(M); s.slope = np.ones(M); s.gamma = np.zeros(M); s.tau = np.full(M, tau0)
        s.lam = np.zeros(M); s.kap = np.zeros(M); s.w = np.ones((2, len(G))) / len(G); s.j0 = irt.MINDS.index("sonnet55")
    def _z(s, X, Fo, Ft):
        """(I, G, M, H) linear predictor"""
        off = s.gamma[None, :] * X[:, None] + (s.lam[None, :] * Fo + s.kap[None, :] * Ft if s.feats else 0)   # (I, M)
        return (s.alpha[None, None, :, None] + s.slope[None, None, :, None] * G[None, :, None, None]
                + off[:, None, :, None] + s.tau[None, None, :, None] * U[None, None, None, :])
    def item_terms(s, S, N, X, Fo, Ft):
        """per item: log P(answers | g) (I, G) with u integrated per mind, and the u-posterior weights (I, G, M, H)"""
        z = s._z(X, Fo, Ft); lp = -np.logaddexp(0, -z); lq = -np.logaddexp(0, z)
        T = S[:, None, :, None] * lp + (N - S)[:, None, :, None] * lq + LW[None, None, None, :]
        lf = np.logaddexp.reduce(T, axis=3)                                   # (I, G, M)
        return lf.sum(2), T, lf, z
    def comp_loglik_full(s, S, N, X, Fo, Ft):
        lg, _, _, _ = s.item_terms(S, N, X, Fo, Ft)
        return lg + np.log(np.maximum(s.w[X.astype(int)], 1e-300))
    def fit(s, S, N, X, Fo, Ft, iters=60, tol=1e-6, chunk=2500, verbose=False):
        I, M = S.shape; prev = -np.inf; Xi = X.astype(int)
        for it in range(iters):
            ll = 0.0; Rs = []
            npar = 6 if s.feats else 4
            grad = np.zeros((M, npar)); hess = np.zeros((M, npar, npar)); wnew = np.zeros((2, len(G)))
            for c0 in range(0, I, chunk):
                sl = slice(c0, c0 + chunk)
                lg, T, lf, z = s.item_terms(S[sl], N[sl], X[sl], Fo[sl], Ft[sl])
                L = lg + np.log(np.maximum(s.w[Xi[sl]], 1e-300)); tot = np.logaddexp.reduce(L, 1); ll += tot.sum()
                R = np.exp(L - tot[:, None])                                     # (n, G)
                for x in (0, 1): wnew[x] += R[Xi[sl] == x].sum(0)
                Q = np.exp(T - lf[..., None])                                    # (n, G, M, H) u-posterior given g
                p = 1 / (1 + np.exp(-z))
                wt = R[:, :, None, None] * Q                                     # (n, G, M, H)
                res = wt * (S[sl][:, None, :, None] - N[sl][:, None, :, None] * p)
                cur = wt * N[sl][:, None, :, None] * p * (1 - p)
                ones = np.ones_like(p)
                fl = [ones, np.broadcast_to(G[None, :, None, None], p.shape), np.broadcast_to(X[sl][:, None, None, None].astype(float), p.shape),
                      np.broadcast_to(U[None, None, None, :], p.shape)]
                if s.feats: fl += [np.broadcast_to(Fo[sl][:, None, :, None], p.shape), np.broadcast_to(Ft[sl][:, None, :, None], p.shape)]
                for a in range(npar):
                    grad[:, a] += (fl[a] * res).sum((0, 1, 3))
                    for b in range(a, npar):
                        v = (fl[a] * fl[b] * cur).sum((0, 1, 3)); hess[:, a, b] += v; hess[:, b, a] = hess[:, a, b]
            if verbose: print(it, round(ll, 1))
            if ll - prev < tol * abs(ll): break
            prev = ll
            s.w = wnew / np.maximum(wnew.sum(1, keepdims=True), 1e-12)
            for j in range(M):
                free = list(range(npar)) if j != s.j0 else [a for a in range(npar) if a not in (0, 1, 2)]
                # tau is updated on the log scale (chain rule on the 4th coordinate), with a floor: at tau = 0 the
                # gradient in tau is exactly zero (u is symmetric), so EM could never leave it (strengthening 2: a
                # first fit lost Sonnet's tau that way)
                g_ = grad[j].copy(); H_ = hess[j].copy(); t_ = s.tau[j]
                g_[3] = g_[3] * t_; H_[3, :] = H_[3, :] * t_; H_[:, 3] = H_[:, 3] * t_   # Fisher scoring on log tau (positive information)
                H = H_[np.ix_(free, free)] + 1e-6 * np.eye(len(free)); st = np.linalg.solve(H, g_[free])
                st = np.clip(st, -0.5, 0.5)
                th = [s.alpha, s.slope, s.gamma, None, s.lam, s.kap]
                for a, d in zip(free, st):
                    if a == 3: s.tau[j] = max(0.05, s.tau[j] * float(np.exp(np.clip(d, -0.3, 0.3))))
                    else: th[a][j] += d
        s.ll = ll; s.iters = it
        return s

class Adapter:
    """checks2/preq adapter. Features are bound per item via set_rows (preq passes rows in a known order)."""
    def __init__(s, m, Fo, Ft): s.m, s.Fo, s.Ft = m, Fo, Ft; s.rows = None
    def comp_loglik(s, S, N, X):
        rows = s.rows if s.rows is not None else np.arange(len(S))
        return s.m.comp_loglik_full(S, N, X, s.Fo[rows], s.Ft[rows])

    def cond_next_item(s, i, x, j, k, n):
        """(G,) P(next answer of mind j = 1 | grid point, item i's features, mind j's own k of n on the item)"""
        m = s.m; off = m.gamma[j] * x + (m.lam[j] * s.Fo[i, j] + m.kap[j] * s.Ft[i, j] if m.feats else 0)
        z = m.alpha[j] + m.slope[j] * G[:, None] + off + m.tau[j] * U[None, :]
        p = 1 / (1 + np.exp(-z)); w = W[None, :] * p ** k * (1 - p) ** (n - k)
        return (w * p).sum(1) / w.sum(1)
