"""Strengthening 2: a mind x item model in which the interaction can sit anywhere, including near certainty.

Each (item i, mind m) has its own propensity p_im (here: of stopping); a mind's repeated answers on that item are
Bernoulli(p_im). Minds are coupled only through the item's shared position b_i, which sets each mind's MEAN propensity;
each mind's propensities scatter around that mean with its own concentration phi_m:
    p_im ~ Beta(mu_m phi_m, (1 - mu_m) phi_m),   mu_m = sigma(alpha_m + s_m b_i + gamma_m x_i)
so (k_im stops of n_im) is beta-binomial. Small phi_m makes the scatter U-shaped: a mind can be near-certain on an item
where others aren't. b_i has a NONPARAMETRIC prior: weights on a 41-point grid on [-5, 5], fitted per familiarity
population x (tok.py), which replaces irt.py's hand-built C/S classes. Anchors: sonnet55 alpha = 0, s = 1, gamma = 0.
phi -> infinity is a pure shared-threshold model (no interaction). Fitted by EM; the M-step per mind maximises the
expected beta-binomial log-likelihood (Newton with numeric derivatives on 4 parameters, over sufficient statistics).
"""
import numpy as np
import irt

G = np.linspace(-5, 5, 41)
ANCHOR = "sonnet55"

def logbb_table(a, b, nmax):
    """for arrays a, b (same shape): cumulative log sums up to nmax: ca[..., t] = sum_{u<t} log(a + u)"""
    t = np.arange(nmax)
    def cum(v):
        z = np.log(v[..., None] + t)                     # (..., nmax)
        return np.concatenate([np.zeros(v.shape + (1,)), np.cumsum(z, -1)], -1)
    return cum(a), cum(b), cum(a + b)

class BB:
    def __init__(s, fam=True, phi0=5.0):
        M = len(irt.MINDS); s.fam = fam
        s.alpha = np.zeros(M); s.slope = np.ones(M); s.gamma = np.zeros(M); s.lphi = np.full(M, np.log(phi0))
        s.w = np.ones((2, len(G))) / len(G)
        s.j0 = irt.MINDS.index(ANCHOR)
    def mu(s, x):                                        # (G, M)
        z = s.alpha[None, :] + s.slope[None, :] * G[:, None] + (s.gamma[None, :] * x if s.fam else 0)
        return 1 / (1 + np.exp(-z))
    def ab(s, x):
        mu = s.mu(x); phi = np.exp(s.lphi)[None, :]
        return mu * phi, (1 - mu) * phi
    def comp_loglik(s, S, N, X):
        """(I, G): log w + sum over minds of log BB(k | n) at each grid point"""
        I, M = S.shape; nmax = int(N.max()) + 1; out = np.zeros((I, len(G)))
        K = S.astype(int); Nn = N.astype(int)
        for x in (0, 1):
            ix = np.where(X == x)[0]
            if not len(ix): continue
            a, b = s.ab(x)                                # (G, M)
            ca, cb, cab = logbb_table(a, b, nmax)         # (G, M, nmax+1)
            for j in range(M):
                k = K[ix, j]; n = Nn[ix, j]
                out[ix] += (ca[:, j, :][:, k] + cb[:, j, :][:, n - k] - cab[:, j, :][:, n]).T
            out[ix] += np.log(np.maximum(s.w[x if s.fam else 0], 1e-300))[None, :]
        return out
    def fit(s, S, N, X, iters=300, tol=1e-7, verbose=False):
        K = S.astype(int); Nn = N.astype(int); nmax = int(N.max()) + 1; M = S.shape[1]; prev = -np.inf
        for it in range(iters):
            L = s.comp_loglik(S, N, X); tot = np.logaddexp.reduce(L, 1); R = np.exp(L - tot[:, None]); ll = tot.sum()
            if verbose and it % 20 == 0: print(it, ll)
            if ll - prev < tol * abs(ll): break
            prev = ll
            for x in (0, 1):
                ix = X == x
                if s.fam: s.w[x] = R[ix].mean(0)
            if not s.fam: s.w[:] = R.mean(0)
            # sufficient statistics per mind: weight of (x, g, k, n)
            for j in range(M):
                cells = []
                for x in (0, 1):
                    ix = np.where((X == x) & (Nn[:, j] > 0))[0]
                    if not len(ix): continue
                    keys = K[ix, j] * nmax + Nn[ix, j]
                    uk, inv = np.unique(keys, return_inverse=True)
                    Wt = np.zeros((len(uk), len(G))); np.add.at(Wt, inv, R[ix])
                    cells.append((x, uk // nmax, uk % nmax, Wt))
                def obj(th):
                    a_, s_, g_, lp = th; v = 0.0
                    for x, kk, nn, Wt in cells:
                        z = a_ + s_ * G + (g_ * x if s.fam else 0); mu = 1 / (1 + np.exp(-z)); phi = np.exp(lp)
                        ca, cb, cab = logbb_table(mu * phi, (1 - mu) * phi, nmax)       # (G, nmax+1)
                        lbb = ca[:, kk] + cb[:, nn - kk] - cab[:, nn]                  # (G, cells)
                        v += (Wt.T * lbb).sum()
                    return v - 0.01 * lp ** 2                    # a very weak prior keeps phi finite under separation
                free = [0, 1, 2, 3] if j != s.j0 else [3]
                if not s.fam: free = [f for f in free if f != 2]
                th = np.array([s.alpha[j], s.slope[j], s.gamma[j], s.lphi[j]])
                for _ in range(3):
                    h = 1e-4; f0 = obj(th); g = np.zeros(4); H = np.zeros((4, 4))
                    for a_ in free:
                        e = np.zeros(4); e[a_] = h
                        fp, fm = obj(th + e), obj(th - e); g[a_] = (fp - fm) / (2 * h); H[a_, a_] = (fp - 2 * f0 + fm) / h ** 2
                        for b_ in free:
                            if b_ <= a_: continue
                            e2 = np.zeros(4); e2[b_] = h
                            H[a_, b_] = H[b_, a_] = (obj(th + e + e2) - obj(th + e - e2) - obj(th - e + e2) + obj(th - e - e2)) / (4 * h * h)
                    fi = np.array(free); Hs = H[np.ix_(fi, fi)]; gs = g[fi]
                    try: st = -np.linalg.solve(Hs - 1e-6 * np.eye(len(fi)), gs)
                    except np.linalg.LinAlgError: st = 0.1 * gs
                    st = np.clip(st, -1, 1); step = 1.0
                    while step > 1e-3:
                        th2 = th.copy(); th2[fi] += step * st
                        if obj(th2) >= f0: th = th2; break
                        step /= 2
                s.alpha[j], s.slope[j], s.gamma[j], s.lphi[j] = th
        s.ll = ll; s.iters = it
        return s

    # ---- quantities for the checks, per grid component (G,), for mind j at familiarity x
    def p1(s, x, j): return s.mu(x)[:, j]
    def disagree2(s, x, j):
        mu = s.mu(x)[:, j]; phi = np.exp(s.lphi[j]); return 2 * mu * (1 - mu) * phi / (phi + 1)
    def allsame(s, x, j, n, y):
        a, b = s.ab(x); a, b = a[:, j], b[:, j]
        ca, cb, cab = logbb_table(a, b, n + 1)
        return np.exp(ca[:, n] - cab[:, n]) if y == 1 else np.exp(cb[:, n] - cab[:, n])
    def next1(s, x, j, k, n):
        """(G,) P(next answer = 1 | this mind's k of n on the item, at each grid point)"""
        mu = s.mu(x)[:, j]; phi = np.exp(s.lphi[j]); return (mu * phi + k) / (phi + n)
