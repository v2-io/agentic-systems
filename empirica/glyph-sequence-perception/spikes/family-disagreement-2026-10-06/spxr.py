"""Strengthening 3: spx.SPX fitted on ROWS -- one row per (context, round) -- with each row's sequence features computed
from earlier rounds only (lnb_prefix.prefix_features), so the model is fitted with the features it is used with
(the prequential check had used strong all-round features in fitting and weak earlier-round ones in prediction).
Covariates are per context; the shared position b and the sparse per-(context, mind) interaction are per context; the
binomial part of each mind's answers is a product over that context's rows. A weak ridge (N(0, 3^2)) on every per-mind
coefficient keeps thinly answered minds (Gemini Pro) finite under separation."""
import numpy as np
import irt, spx

G = spx.G
class SPXR(spx.SPX):
    RIDGE = 1 / 9.0
    def fit_rows(s, item_of_row, Sr, Nr, Xi, FoR, FtR, Citem, iters=300, tol=1e-7, verbose=False):
        """item_of_row (R,), Sr/Nr (R, M) answers given in that row's round, Xi (I,) familiarity, FoR/FtR (R, M) row
        features, Citem (I, K) covariates"""
        I = len(Xi); M = Sr.shape[1]; R_ = len(item_of_row)
        Si = np.zeros((I, M)); Ni = np.zeros((I, M)); np.add.at(Si, item_of_row, Sr); np.add.at(Ni, item_of_row, Nr)
        prev = -np.inf; npar = (5 if s.feats else 3) + s.K; nb = 5 if s.feats else 3
        Xr = Xi[item_of_row]; Cr = Citem[item_of_row] if s.K else None
        for it in range(iters):
            z = s._z(Xr.astype(float), FoR, FtR, Cr)                                  # (R, G, M)
            lp = -np.logaddexp(0, -z); lq = -np.logaddexp(0, z)
            lfr = Sr[:, None, :] * lp + (Nr - Sr)[:, None, :] * lq
            lf = np.zeros((I, len(G), M)); np.add.at(lf, item_of_row, lfr)           # (I, G, M)
            lh = np.stack([spx.logbb(Si[:, j], Ni[:, j], s.a[j], s.b[j]) for j in range(M)], 1)
            l0 = np.log1p(-s.pi)[None, None, :] + lf; l1 = (np.log(s.pi)[None, :] + lh)[:, None, :]
            lm = np.where(Ni[:, None, :] > 0, np.logaddexp(l0, l1), 0.0)
            L = lm.sum(2) + np.log(np.maximum(s.w[Xi.astype(int)], 1e-300)); tot = np.logaddexp.reduce(L, 1); ll = tot.sum()
            if verbose: print(it, round(ll, 1), flush=True)
            if ll - prev < tol * abs(ll): break
            prev = ll
            Rp = np.exp(L - tot[:, None])
            for x in (0, 1): s.w[x] = Rp[Xi == x].mean(0)
            pz1 = np.where(Ni[:, None, :] > 0, np.exp(l1 - np.logaddexp(l0, l1)), 0.0)
            has = Ni > 0
            ez = (Rp[:, :, None] * pz1).sum(1) * has
            if s.sparse: s.pi = np.clip(ez.sum(0) / np.maximum(has.sum(0), 1), 1e-4, 0.5)
            w0 = (Rp[:, :, None] * (1 - pz1) * has[:, None, :])[item_of_row]        # (R, G, M)
            p = 1 / (1 + np.exp(-z))
            res = w0 * (Sr[:, None, :] - Nr[:, None, :] * p); cur = w0 * Nr[:, None, :] * p * (1 - p)
            fl = [np.ones_like(p), np.broadcast_to(G[None, :, None], p.shape), np.broadcast_to(Xr[:, None, None].astype(float), p.shape)]
            if s.feats: fl += [np.broadcast_to(FoR[:, None, :], p.shape), np.broadcast_to(FtR[:, None, :], p.shape)]
            for kk in range(s.K): fl.append(np.broadcast_to(Cr[:, kk][:, None, None], p.shape))
            grad = np.zeros((M, npar)); info = np.zeros((M, npar, npar))
            for a_ in range(npar):
                grad[:, a_] = (fl[a_] * res).sum((0, 1))
                for b_ in range(a_, npar):
                    v = (fl[a_] * fl[b_] * cur).sum((0, 1)); info[:, a_, b_] = v; info[:, b_, a_] = v
            for j in range(M):
                th = np.concatenate([[s.alpha[j], s.slope[j] - 1.0, s.gamma[j]], ([s.lam[j], s.kap[j]] if s.feats else []), s.beta[j]])
                g_ = grad[j] - s.RIDGE * th; H_ = info[j] + s.RIDGE * np.eye(npar)
                free = [a_ for a_ in range(npar) if not (j == s.j0 and a_ in (0, 1, 2)) and not (s.feats and not s.own and a_ == 3)]
                st = np.clip(np.linalg.solve(H_[np.ix_(free, free)], g_[free]), -0.5, 0.5)
                for a_, d in zip(free, st):
                    if a_ == 0: s.alpha[j] += d
                    elif a_ == 1: s.slope[j] += d
                    elif a_ == 2: s.gamma[j] += d
                    elif s.feats and a_ == 3: s.lam[j] += d
                    elif s.feats and a_ == 4: s.kap[j] += d
                    else: s.beta[j, a_ - nb] += d
            for j in range(M):
                ks = Si[has[:, j], j].astype(int); ns = Ni[has[:, j], j].astype(int); ws = ez[has[:, j], j]
                if ws.sum() > 0:
                    s.a[j], s.b[j] = max(((aa, bb) for aa in spx.ABGRID for bb in spx.ABGRID), key=lambda ab: float((ws * spx.logbb(ks, ns, ab[0], ab[1])).sum()))
        s.ll = ll; s.iters = it
        return s
