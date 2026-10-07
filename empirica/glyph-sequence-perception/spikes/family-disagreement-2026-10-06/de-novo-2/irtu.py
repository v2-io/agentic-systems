"""irt.py's 2PL mixture with familiarity (variant 2mf), plus a per-(item, mind) random intercept in the graded class:
   logit P(1 | m, b, u) = alpha_m + slope_m b + gamma_m x_i + tau_m u_{im},  u_{im} ~ N(0, 1) independent,
so a mind's repeated answers on one item share u (a stable mind x item propensity) while other minds don't.
tau = 0 is irt.py's 2mf exactly. Fitted by EM on the (b, u) grid; C and S classes unchanged."""
import sys, numpy as np
SP="/Users/josephwecker-v2/src/arch/asf/empirica/glyph-sequence-perception/spikes/family-disagreement-2026-10-06"
sys.path.insert(0, SP)
import irt
G, PHI = irt.G, irt.PHI
U, W = np.polynomial.hermite_e.hermegauss(9); W = W / W.sum()
LW = np.log(W)

class ModelU(irt.Model):
    def __init__(s, tau0=1.0, fix_tau=None):
        super().__init__(2, True, True)
        M = len(irt.MINDS); s.tau = np.full(M, tau0 if fix_tau is None else fix_tau); s.fix_tau = fix_tau
    def _T(s, S, N, x):
        z = (s.alpha[None, None, :] + s.slope[None, None, :] * G[:, None, None] + s.gamma[None, None, :] * x
             + s.tau[None, None, :] * U[None, :, None])                                         # (G, H, M)
        lp = -np.logaddexp(0, -z); lq = -np.logaddexp(0, z)
        return S[:, None, None, :] * lp[None] + (N - S)[:, None, None, :] * lq[None], z      # (n, G, H, M)
    def comp_loglik(s, S, N, X, keepQ=False):
        I = S.shape[0]; out = np.empty((I, 2 + len(G))); F = N - S; Qs = {}
        for x in (0, 1):
            ix = np.where(X == x)[0]
            if not len(ix): continue
            e = s.eps[x]; d = s.dlt[x]
            out[ix, 0] = S[ix] @ np.log(e) + F[ix] @ np.log1p(-e)
            out[ix, 1] = S[ix] @ np.log1p(-d) + F[ix] @ np.log(d)
            for c0 in range(0, len(ix), 3000):
                ii = ix[c0:c0 + 3000]
                T, _ = s._T(S[ii], N[ii], x)
                T = T + LW[None, None, :, None]
                lf = np.logaddexp.reduce(T, axis=2)                     # (n, G, M)
                out[ii, 2:] = lf.sum(2)
                if keepQ: Qs[(x, c0)] = (ii, np.exp(T - lf[:, :, None, :]))
        lpri = np.concatenate([np.log(s.pi[:2]), np.log(s.pi[2]) + np.log(PHI)])
        return (out + lpri[None, :], Qs) if keepQ else out + lpri[None, :]
    def fit(s, S, N, X, iters=300, tol=1e-7):
        prev = -np.inf; Mn = len(irt.MINDS)
        for it in range(iters):
            L, Qs = s.comp_loglik(S, N, X, keepQ=True)
            tot = np.logaddexp.reduce(L, axis=1); R = np.exp(L - tot[:, None]); ll = tot.sum()
            if ll - prev < tol * abs(ll): break
            prev = ll
            s.pi = np.array(R[:, :2].sum(0).tolist() + [R[:, 2:].sum()]) / R.shape[0]
            for x in (0, 1):
                ix = X == x; rc, rs = R[ix, 0], R[ix, 1]
                s.eps[x] = np.clip((rc @ S[ix] + 0.005) / (rc @ N[ix] + 0.5), 1e-4, 0.45)
                s.dlt[x] = np.clip((rs @ (N[ix] - S[ix]) + 0.005) / (rs @ N[ix] + 0.5), 1e-4, 0.45)
            A = np.zeros((2, len(G), len(U), Mn)); B = np.zeros_like(A)
            for (x, c0), (ii, Q) in Qs.items():
                w = R[ii, 2:][:, :, None, None] * Q                        # (n, G, H, M)
                A[x] += np.einsum("nghm,nm->ghm", w, S[ii]); B[x] += np.einsum("nghm,nm->ghm", w, N[ii])
            for _ in range(4):
                for j in range(Mn):
                    th = [s.alpha[j], s.slope[j], s.gamma[j], s.tau[j]]; k = 4 if s.fix_tau is None else 3
                    gr = np.zeros(k); H = np.zeros((k, k))
                    for x in (0, 1):
                        z = th[0] + th[1] * G[:, None] + th[2] * x + th[3] * U[None, :]
                        p = 1 / (1 + np.exp(-z)); res = A[x, :, :, j] - B[x, :, :, j] * p; ww = B[x, :, :, j] * p * (1 - p)
                        feats = [np.ones_like(z), np.broadcast_to(G[:, None], z.shape), np.full_like(z, x), np.broadcast_to(U[None, :], z.shape)][:k]
                        for a in range(k):
                            gr[a] += (feats[a] * res).sum()
                            for b in range(k): H[a, b] += (feats[a] * feats[b] * ww).sum()
                    st = np.linalg.solve(H + 1e-6 * np.eye(k), gr)
                    st = np.clip(st, -1, 1)
                    s.alpha[j] += st[0]; s.slope[j] += st[1]; s.gamma[j] += st[2]
                    if k == 4: s.tau[j] = abs(s.tau[j] + st[3])
        s.ll = ll; s.iters = it
        return s
    def predict_next(s, S1, N1, x, j):
        """P(next answer of mind j = 1 | all answers S1, N1 of one item)"""
        L, Qs = s.comp_loglik(S1[None], N1[None], np.array([x]), keepQ=True)
        r = np.exp(L[0] - np.logaddexp.reduce(L[0]))
        (ii, Q), = Qs.values()
        z = s.alpha[j] + s.slope[j] * G[:, None] + s.gamma[j] * x + s.tau[j] * U[None, :]
        p = 1 / (1 + np.exp(-z))                                               # (G, H)
        pm = (Q[0, :, :, j] * p).sum(1)                                        # (G,) given b, u-posterior
        return r[0] * s.eps[x][j] + r[1] * (1 - s.dlt[x][j]) + r[2:] @ pm
