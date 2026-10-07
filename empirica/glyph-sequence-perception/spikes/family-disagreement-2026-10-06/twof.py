"""A second shared item factor (strengthening 2): is there a family axis?

    logit P(stop | m, i) = alpha_m + s_m b_i + t_m c_i + gamma_m x_i [+ lam_m F_own + kap_m F_oth]
    b ~ nonparametric weights on a 21-point grid (per familiarity x), c ~ N(0, 1) on a 9-point Hermite grid

No per-(item, mind) intercept here (it would multiply the grid by 9 per mind); this model is for the PAIRWISE
structure, which a per-mind intercept can't produce. t_m is each mind's loading on the second factor; if loadings
separate families, minds of one family share deviations from the first factor. Anchors: sonnet55 alpha = 0, s = 1,
gamma = 0, t >= 0 (sign). EM with Newton per mind."""
import numpy as np
import irt

G = np.linspace(-5, 5, 21)
C, CW = np.polynomial.hermite_e.hermegauss(9); CW = CW / CW.sum(); LCW = np.log(CW)

class TwoF:
    def __init__(s, feats=False, nf=2):
        M = len(irt.MINDS); s.feats = feats; s.nf = nf
        s.alpha = np.zeros(M); s.slope = np.ones(M); s.gamma = np.zeros(M); s.t = np.full(M, 0.3) if nf == 2 else np.zeros(M)
        s.lam = np.zeros(M); s.kap = np.zeros(M); s.w = np.ones((2, len(G))) / len(G); s.j0 = irt.MINDS.index("sonnet55")
        rng = np.random.default_rng(0); s.t = s.t + (0.3 * rng.standard_normal(M) if nf == 2 else 0)
    def _z(s, X, Fo, Ft):
        off = s.gamma[None, :] * X[:, None] + ((s.lam[None, :] * Fo + s.kap[None, :] * Ft) if s.feats else 0)
        return (s.alpha[None, None, None, :] + s.slope[None, None, None, :] * G[None, :, None, None]
                + s.t[None, None, None, :] * C[None, None, :, None] + off[:, None, None, :])          # (I, G, C, M)
    def comp_loglik_full(s, S, N, X, Fo, Ft):
        z = s._z(X, Fo, Ft); lp = -np.logaddexp(0, -z); lq = -np.logaddexp(0, z)
        L = (S[:, None, None, :] * lp + (N - S)[:, None, None, :] * lq).sum(3) + LCW[None, None, :]   # (I, G, C)
        L = L + np.log(np.maximum(s.w[X.astype(int)], 1e-300))[:, :, None]
        return L.reshape(len(S), -1)
    def fit(s, S, N, X, Fo=None, Ft=None, iters=150, tol=1e-7, chunk=4000):
        I, M = S.shape; Fo = np.zeros((I, M)) if Fo is None else Fo; Ft = np.zeros((I, M)) if Ft is None else Ft
        prev = -np.inf; Xi = X.astype(int); npar = 6 if s.feats else 4
        for it in range(iters):
            ll = 0.0; grad = np.zeros((M, npar)); info = np.zeros((M, npar, npar)); wnew = np.zeros((2, len(G)))
            for c0 in range(0, I, chunk):
                sl = slice(c0, c0 + chunk); n_ = len(S[sl])
                L = s.comp_loglik_full(S[sl], N[sl], X[sl], Fo[sl], Ft[sl]); tot = np.logaddexp.reduce(L, 1); ll += tot.sum()
                R = np.exp(L - tot[:, None]).reshape(n_, len(G), len(C))
                for x in (0, 1): wnew[x] += R[Xi[sl] == x].sum((0, 2))
                z = s._z(X[sl], Fo[sl], Ft[sl]); p = 1 / (1 + np.exp(-z))
                res = R[..., None] * (S[sl][:, None, None, :] - N[sl][:, None, None, :] * p)
                cur = R[..., None] * N[sl][:, None, None, :] * p * (1 - p)
                fl = [np.ones_like(p), np.broadcast_to(G[None, :, None, None], p.shape), np.broadcast_to(C[None, None, :, None], p.shape),
                      np.broadcast_to(X[sl][:, None, None, None].astype(float), p.shape)]
                if s.feats: fl += [np.broadcast_to(Fo[sl][:, None, None, :], p.shape), np.broadcast_to(Ft[sl][:, None, None, :], p.shape)]
                for a in range(npar):
                    grad[:, a] += (fl[a] * res).sum((0, 1, 2))
                    for b in range(a, npar):
                        v = (fl[a] * fl[b] * cur).sum((0, 1, 2)); info[:, a, b] += v; info[:, b, a] = info[:, a, b]
            if ll - prev < tol * abs(ll): break
            prev = ll; s.w = wnew / np.maximum(wnew.sum(1, keepdims=True), 1e-12)
            for j in range(M):
                free = [a for a in range(npar) if not (j == s.j0 and a in (0, 1, 3)) and not (s.nf == 1 and a == 2)]
                st = np.clip(np.linalg.solve(info[j][np.ix_(free, free)] + 1e-6 * np.eye(len(free)), grad[j][free]), -0.5, 0.5)
                th = [s.alpha, s.slope, s.t, s.gamma, s.lam, s.kap]
                for a, d in zip(free, st): th[a][j] += d
            if s.nf == 2 and s.t[s.j0] < 0: s.t = -s.t
        s.ll = ll; s.iters = it
        return s
    def cond_next_row(s, Fo_row, Ft_row, x, j):
        """(G*C,) P(1 | grid point) for mind j"""
        off = s.gamma[j] * x + ((s.lam[j] * Fo_row[j] + s.kap[j] * Ft_row[j]) if s.feats else 0)
        z = s.alpha[j] + s.slope[j] * G[:, None] + s.t[j] * C[None, :] + off
        return (1 / (1 + np.exp(-z))).reshape(-1)
