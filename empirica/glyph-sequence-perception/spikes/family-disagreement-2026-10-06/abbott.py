"""Strengthening attempt 2 (de-novo-feedback-1 §4): Abbott against logit on cohere answers with their shuffled controls,
by held-out likelihood. Integration-plan item 2 rests on which fits.

Data: cohere answers yes/no (can't-tell dropped, counted), plain variant, the seven first-impression minds; items are
real runs (no control tag) and shuffled controls (tag 'shuffled'); chart windows and lookalike runs left out. Items
keyed by content (values.ckey); populations by (real | control) x set class (contiguous | other, catalog/build.py's rule).

Every model gets the same item-distribution freedom: a nonparametric prior on a 41-point grid, its weights fitted per
population (EM). What differs is the link:
  A1  catalog build 0: P(yes | m, real i) = c[m,k] + (1 - c[m,k]) * theta_i ; controls: P = c[m,k] (theta = 0)
  A2  CATALOG §9: P = c[m,k] + (1 - c[m,k]) * s[m] * theta_i ; controls as A1
  A3  A2, but controls also draw theta from their own populations (some shuffles are coherent, METHODOLOGY §4a)
  L1  logit P = alpha[m] + beta_i, every item (real or control) drawing beta from its population
  L2  logit P = alpha[m] + slope[m] * beta_i
  L3  L2 with a per-mind offset for set class: alpha[m, k]  (applies to controls and real runs of that set class alike)
  L4  L2 with a per-mind offset on REAL contiguous runs only (alpha[m, 1] used as that offset): a mind's extra yes to the
      ordered contiguous run beyond what its item position and criterion predict -- the 'contiguity lean' of FINDINGS 3
Held-out: 5-fold over items; marginal log-likelihood per answer of the held-out items, overall, per mind, per population.
"""
import collections, math, sys
import numpy as np
import lib
from values import ckey

MINDS = ["sonnet55", "opus55", "haiku45nt", "haiku45", "grok46", "gemini38flash", "gemini31pro"]
POPS = ["real-contig", "real-other", "ctl-contig", "ctl-other"]

def setcls(g):
    o = sorted(ord(x) for x in g)
    return "contig" if all(b - a == 1 for a, b in zip(o, o[1:])) else "other"

def load():
    recs, man = lib.load()
    Y = collections.defaultdict(lambda: np.zeros(len(MINDS))); Nn = collections.defaultdict(lambda: np.zeros(len(MINDS)))
    pop = {}; cant = 0
    for r in recs:
        if r["kind"] != "cohere" or r["mind"] not in MINDS: continue
        t = r.get("tags") or {}
        if t.get("variant") not in (None, "plain"): continue
        c = t.get("control")
        if c not in (None, "shuffled"): continue
        if r["outcome"] == "cant-tell": cant += 1; continue
        if r["outcome"] not in ("yes", "no"): continue
        q = ckey(r) + (("ctl",) if c else ("real",))
        pop[q] = ("ctl-" if c else "real-") + setcls(r["context"])
        j = MINDS.index(r["mind"]); Y[q][j] += r["outcome"] == "yes"; Nn[q][j] += 1
    items = sorted(pop, key=repr)
    return (items, np.array([Y[q] for q in items]), np.array([Nn[q] for q in items]),
            np.array([POPS.index(pop[q]) for q in items]), cant)

TH = np.linspace(0.0, 1.0, 41); BE = np.linspace(-7, 7, 41)

def golden(f, lo, hi, it=40):
    g = (math.sqrt(5) - 1) / 2; a, b = lo, hi
    c, d = b - g * (b - a), a + g * (b - a); fc, fd = f(c), f(d)
    for _ in range(it):
        if fc > fd: b, d, fd = d, c, fc; c = b - g * (b - a); fc = f(c)
        else: a, c, fc = c, d, fd; d = a + g * (b - a); fd = f(d)
    return (a + b) / 2

class Model:
    def __init__(s, kind):
        s.kind = kind; M = len(MINDS)
        s.w = np.ones((4, 41)) / 41
        s.c = np.full((M, 2), 0.2); s.s = np.ones(M)
        s.alpha = np.zeros((M, 2)); s.slope = np.ones(M)
    def P(s):
        """(4 populations, 41 grid, M) P(yes)"""
        M = len(MINDS); out = np.empty((4, 41, M))
        for p in range(4):
            k = p % 2                              # 0 contig, 1 other
            ctl = p >= 2
            if s.kind.startswith("A"):
                if ctl and s.kind != "A3":
                    out[p] = np.broadcast_to(s.c[:, k][None, :], (41, M))
                else:
                    out[p] = s.c[:, k][None, :] + (1 - s.c[:, k][None, :]) * (s.s[None, :] * TH[:, None])
            else:
                a = s.alpha[:, k] if s.kind == "L3" else s.alpha[:, 0]
                if s.kind == "L4" and p == 0: a = s.alpha[:, 0] + s.alpha[:, 1]
                out[p] = 1 / (1 + np.exp(-(a[None, :] + s.slope[None, :] * BE[:, None])))
        return np.clip(out, 1e-9, 1 - 1e-9)
    def comp_ll(s, Y, N, popi):
        P = s.P(); L = np.empty((len(Y), 41))
        for p in range(4):
            ix = popi == p
            if ix.any():
                L[ix] = Y[ix] @ np.log(P[p]).T + (N[ix] - Y[ix]) @ np.log1p(-P[p]).T + np.log(np.maximum(s.w[p], 1e-300))[None, :]
        return L
    def fit(s, Y, N, popi, iters=200, tol=1e-7):
        prev = -np.inf
        for it in range(iters):
            L = s.comp_ll(Y, N, popi); tot = np.logaddexp.reduce(L, axis=1); R = np.exp(L - tot[:, None])
            ll = tot.sum()
            if ll - prev < tol * abs(ll): break
            prev = ll
            for p in range(4):
                ix = popi == p
                if ix.any(): s.w[p] = R[ix].mean(0)
            # sufficient stats per (pop, grid, mind)
            A = np.stack([R[popi == p].T @ Y[popi == p] if (popi == p).any() else np.zeros((41, len(MINDS))) for p in range(4)])
            B = np.stack([R[popi == p].T @ N[popi == p] if (popi == p).any() else np.zeros((41, len(MINDS))) for p in range(4)])
            def mind_ll(j, Pj):          # Pj: (4, 41) P(yes) for mind j
                Pj = np.clip(Pj, 1e-9, 1 - 1e-9)
                return float((A[:, :, j] * np.log(Pj) + (B[:, :, j] - A[:, :, j]) * np.log1p(-Pj)).sum())
            for j in range(len(MINDS)):
                if s.kind.startswith("A"):
                    for _ in range(2):
                        for k in (0, 1):
                            def f(cv, k=k):
                                old = s.c[j, k]; s.c[j, k] = cv; v = mind_ll(j, s.P()[:, :, j]); s.c[j, k] = old; return v
                            s.c[j, k] = golden(f, 1e-4, 0.999)
                        if s.kind in ("A2", "A3"):
                            def g(sv):
                                old = s.s[j]; s.s[j] = sv; v = mind_ll(j, s.P()[:, :, j]); s.s[j] = old; return v
                            s.s[j] = golden(g, 1e-3, 1.0)
                else:
                    for _ in range(5):
                        ks = (0, 1) if s.kind in ("L3", "L4") else (0,)
                        params = [("a", k) for k in ks] + ([("s", None)] if s.kind in ("L2", "L3", "L4") else [])
                        gr = np.zeros(len(params)); H = np.zeros((len(params), len(params)))
                        for p in range(4):
                            k = p % 2
                            a = s.alpha[j, k] if s.kind == "L3" else s.alpha[j, 0]
                            if s.kind == "L4" and p == 0: a = s.alpha[j, 0] + s.alpha[j, 1]
                            pr = 1 / (1 + np.exp(-(a + s.slope[j] * BE)))
                            res = A[p, :, j] - B[p, :, j] * pr; w = B[p, :, j] * pr * (1 - pr)
                            if s.kind == "L4":
                                feats = [np.ones(41) if (t == "a" and kk == 0) else (np.full(41, 1.0 if p == 0 else 0.0) if t == "a" else BE) for t, kk in params]
                            else:
                                feats = [(np.ones(41) if (kk == k or s.kind != "L3") else np.zeros(41)) if t == "a" else BE for t, kk in params]
                            for u in range(len(params)):
                                gr[u] += (feats[u] * res).sum()
                                for v in range(len(params)): H[u, v] += (feats[u] * feats[v] * w).sum()
                        st = np.linalg.solve(H + 1e-6 * np.eye(len(params)), gr)
                        for (t, k), d in zip(params, st):
                            if t == "a":
                                if s.kind in ("L3", "L4"): s.alpha[j, k] += d
                                else: s.alpha[j, :] += d
                            else: s.slope[j] += d
        s.ll = ll
        return s

def heldout(kind, Y, N, popi, folds=5, seed=0):
    rng = np.random.default_rng(seed); f = rng.integers(0, folds, len(Y))
    per_ans = np.zeros(len(Y))                   # held-out marginal log-lik of each item
    for k in range(folds):
        tr, te = f != k, f == k
        m = Model(kind).fit(Y[tr], N[tr], popi[tr])
        per_ans[te] = np.logaddexp.reduce(m.comp_ll(Y[te], N[te], popi[te]), axis=1)
    return per_ans

if __name__ == "__main__":
    items, Y, N, popi, cant = load()
    print(f"cohere items {len(items)} (by population {[int((popi == p).sum()) for p in range(4)]}), answers {int(N.sum())}, can't-tell dropped {cant}")
    kinds = sys.argv[1:] or ["A1", "A2", "A3", "L1", "L2", "L3"]
    res = {}
    for kind in kinds:
        res[kind] = heldout(kind, Y, N, popi)
        print(f"  {kind}: held-out log-lik per answer {res[kind].sum() / N.sum():.4f}")
    print("\nper population, held-out log-lik per answer:")
    for p in range(4):
        ix = popi == p
        print(f"  {POPS[p]:12s} answers {int(N[ix].sum()):5d}  " + "  ".join(f"{k} {res[k][ix].sum() / N[ix].sum():.4f}" for k in kinds))
    # per mind: items answered only by that mind are not separable; report items' log-lik split by answers' mind share
    print("\nbest model's fit on all data, parameters:")
    for kind in kinds:
        m = Model(kind).fit(Y, N, popi)
        if kind.startswith("A"):
            print(f"  {kind}: " + "; ".join(f"{mm} c={m.c[j,0]:.2f}/{m.c[j,1]:.2f}" + (f" s={m.s[j]:.2f}" if kind != "A1" else "") for j, mm in enumerate(MINDS)))
        else:
            print(f"  {kind}: " + "; ".join(f"{mm} a={m.alpha[j,0]:+.2f}" + (f"/{m.alpha[j,1]:+.2f}" if kind in ("L3", "L4") else "") + (f" s={m.slope[j]:.2f}" if kind != "L1" else "") for j, mm in enumerate(MINDS)))
