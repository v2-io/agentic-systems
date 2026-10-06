"""Strengthening attempt 1 (de-novo-feedback-1 §1): a threshold model that can describe these items.

For one binary decision (additive.outcome: continue-stop, triad-commit, cohere-yes, inhibit-yes), each item i is one of
  C  near-certain 0 for everyone: P(1 | m) = eps[m, x_i]
  S  near-certain 1 for everyone: P(1 | m) = 1 - dlt[m, x_i]
  M  graded:  logit P(1 | m, b) = alpha[m] + slope[m] * b + gamma[m] * x_i,   b ~ N(0, 1) (grid quadrature)
with class weights pi. x_i is an item covariate from the glyphs alone (unfamiliar: the context's last glyph is more than
one token in both public byte-level vocabularies, tok.py); gamma = 0 and eps, dlt not split by x unless --fam.
Variants: --pl 1 (one slope shared by all minds) or 2 (a slope per mind); --nomix (class M only). Fitted by EM.

Checks, in this order (de-novo-feedback-1 asks for calibration first):
 1. held-out log-likelihood per answer, 5-fold over items;
 2. calibration: for pairs of minds, observed single-answer disagreement (first answers) against the model's prediction
    from the OTHER minds' answers only (the item posterior excludes both minds of the pair). Ratio obs/pred near 1;
 3. flat splits both directions (each of the pair >= 2 answers, unanimous, opposite), with a 400-draw band.
"""
import argparse, collections, math, random
import numpy as np
import lib, additive as AD, tok
from values import ckey

MINDS = ["sonnet55", "opus55", "haiku45nt", "haiku45", "grok46", "gemini38flash", "gemini31pro"]
G = np.linspace(-4, 4, 33); PHI = np.exp(-G ** 2 / 2); PHI /= PHI.sum()

def load(name, include_variants=False, one_per_sheet=False):
    """one_per_sheet: keep one answer per (item, mind, sheet), so repeats shown together in one call (triad rotations
    on a shared sheet) don't count as independent answers (de-novo-feedback-1 §9: correlated repeats)"""
    recs, man = lib.load()
    seen_sheet = set()
    seq = collections.defaultdict(lambda: collections.defaultdict(list))   # item -> mind -> [(round, y)]
    xs = {}
    for r in recs:
        if r["mind"] not in MINDS: continue
        t = r.get("tags") or {}
        rr = dict(r)
        if include_variants and t.get("variant") == "no-lookup":
            rr["tags"] = dict(t, variant=None)
        x = AD.outcome(rr)
        if not x or x[0] != name or x[1] is None: continue
        q = ckey(r)
        if one_per_sheet:
            sk = (q, r["mind"], r.get("sid") or r.get("pid"))
            if sk in seen_sheet: continue
            seen_sheet.add(sk)
        seq[q][r["mind"]].append((int(r["round"][1:]) if r["round"][1:].isdigit() else -1, x[1]))
        if q not in xs:
            g = (r.get("context") or r.get("shown") or [""])
            last = g[-1] if g else ""
            xs[q] = 1 if (last and min(tok.QWEN.ntok(last), tok.CLAUDE23.ntok(last)) > 1) else 0
    items = sorted(seq, key=repr)
    I, M = len(items), len(MINDS)
    S = np.zeros((I, M)); N = np.zeros((I, M)); X = np.array([xs[q] for q in items])
    for i, q in enumerate(items):
        for m, L in seq[q].items():
            j = MINDS.index(m); L.sort(key=lambda t: t[0])
            S[i, j] = sum(y for _, y in L); N[i, j] = len(L)
    return items, seq, S, N, X

class Model:
    def __init__(s, pl=2, mix=True, fam=False):
        s.pl, s.mix, s.fam = pl, mix, fam
        M = len(MINDS)
        s.alpha = np.zeros(M); s.slope = np.ones(M); s.gamma = np.zeros(M)
        s.eps = np.full((2, M), 0.05); s.dlt = np.full((2, M), 0.05)
        s.pi = np.array([0.3, 0.1, 0.6]) if mix else np.array([0.0, 0.0, 1.0])

    def comp_loglik(s, S, N, X):
        """(I, 2 + len(G)) log P(answers | component), component prior included"""
        I = S.shape[0]; out = np.empty((I, 2 + len(G)))
        F = N - S
        for x in (0, 1):
            ix = X == x
            if not ix.any(): continue
            e = s.eps[x if s.fam else 0]; d = s.dlt[x if s.fam else 0]
            out[ix, 0] = S[ix] @ np.log(e) + F[ix] @ np.log1p(-e)
            out[ix, 1] = S[ix] @ np.log1p(-d) + F[ix] @ np.log(d)
            z = s.alpha[None, :] + s.slope[None, :] * G[:, None] + (s.gamma[None, :] * x if s.fam else 0)   # (G, M)
            lp = -np.logaddexp(0, -z); lq = -np.logaddexp(0, z)
            out[ix, 2:] = S[ix] @ lp.T + F[ix] @ lq.T
        with np.errstate(divide="ignore"):
            lpri = np.concatenate([np.log(s.pi[:2]), np.log(s.pi[2]) + np.log(PHI)])
        return out + lpri[None, :]

    def fit(s, S, N, X, iters=150, tol=1e-6):
        prev = -np.inf
        for it in range(iters):
            L = s.comp_loglik(S, N, X)
            tot = np.logaddexp.reduce(L, axis=1)
            R = np.exp(L - tot[:, None])                          # posteriors
            ll = tot.sum()
            if ll - prev < tol * abs(ll): break
            prev = ll
            if s.mix:
                s.pi = R[:, :2].sum(0).tolist() + [R[:, 2:].sum()]; s.pi = np.array(s.pi) / R.shape[0]
                for x in ((0, 1) if s.fam else (None,)):
                    ix = (X == x) if x is not None else np.ones(len(X), bool)
                    k = x if x is not None else 0
                    rc, rs = R[ix, 0], R[ix, 1]
                    s.eps[k] = np.clip((rc @ S[ix] + 0.5 * 0.01) / (rc @ N[ix] + 0.5), 1e-4, 0.45)
                    s.dlt[k] = np.clip((rs @ (N[ix] - S[ix]) + 0.5 * 0.01) / (rs @ N[ix] + 0.5), 1e-4, 0.45)
                    if not s.fam: s.eps[1], s.dlt[1] = s.eps[0], s.dlt[0]
            RM = R[:, 2:]
            A = np.stack([RM[X == x].T @ S[X == x] for x in (0, 1)])     # (2, G, M) weighted 1s
            B = np.stack([RM[X == x].T @ N[X == x] for x in (0, 1)])     # (2, G, M) weighted answers
            for _ in range(4):                                          # Newton steps per mind
                for j in range(len(MINDS)):
                    th = [s.alpha[j], s.slope[j]] + ([s.gamma[j]] if s.fam else [])
                    gr = np.zeros(len(th)); H = np.zeros((len(th), len(th)))
                    for x in (0, 1):
                        z = th[0] + th[1] * G + (th[2] * x if s.fam else 0)
                        p = 1 / (1 + np.exp(-z))
                        feats = [np.ones_like(G), G] + ([np.full_like(G, x)] if s.fam else [])
                        res = A[x, :, j] - B[x, :, j] * p; w = B[x, :, j] * p * (1 - p)
                        for a in range(len(th)):
                            gr[a] += (feats[a] * res).sum()
                            for b in range(len(th)): H[a, b] += (feats[a] * feats[b] * w).sum()
                    if s.pl == 1:      # slope shared: per-mind step on alpha (and gamma) only
                        keep = [0] + ([2] if s.fam else [])
                        Hk = H[np.ix_(keep, keep)] + 1e-6 * np.eye(len(keep)); st = np.linalg.solve(Hk, gr[keep])
                        s.alpha[j] += st[0]
                        if s.fam: s.gamma[j] += st[1]
                    else:
                        st = np.linalg.solve(H + 1e-6 * np.eye(len(th)), gr)
                        s.alpha[j] += st[0]; s.slope[j] += st[1]
                        if s.fam: s.gamma[j] += st[2]
                if s.pl == 1:          # one shared slope, 1-D Newton over all minds
                    g1 = h1 = 0.0
                    for j in range(len(MINDS)):
                        for x in (0, 1):
                            z = s.alpha[j] + s.slope[j] * G + (s.gamma[j] * x if s.fam else 0)
                            p = 1 / (1 + np.exp(-z))
                            g1 += (G * (A[x, :, j] - B[x, :, j] * p)).sum(); h1 += (G * G * B[x, :, j] * p * (1 - p)).sum()
                    s.slope[:] = s.slope[0] + g1 / (h1 + 1e-9)
        s.ll = ll
        return s

    def comp_probs(s, x):
        """P(1 | m, component) for each component: (2 + G, M)"""
        k = x if s.fam else 0
        z = s.alpha[None, :] + s.slope[None, :] * G[:, None] + (s.gamma[None, :] * x if s.fam else 0)
        return np.vstack([s.eps[k][None, :], (1 - s.dlt[k])[None, :], 1 / (1 + np.exp(-z))])

def heldout(S, N, X, pl, mix, fam, folds=5, seed=0):
    I = S.shape[0]; rng = np.random.default_rng(seed); f = rng.integers(0, folds, I)
    tot = n = 0.0
    for k in range(folds):
        tr, te = f != k, f == k
        m = Model(pl, mix, fam).fit(S[tr], N[tr], X[tr])
        tot += np.logaddexp.reduce(m.comp_loglik(S[te], N[te], X[te]), axis=1).sum(); n += N[te].sum()
    return tot / n

def pair_checks(m, items, seq, S, N, X, pairs, sims=400, seed=0):
    rng = random.Random(seed); out = []
    for A, B in pairs:
        a, b = MINDS.index(A), MINDS.index(B)
        So, No = S.copy(), N.copy(); So[:, [a, b]] = 0; No[:, [a, b]] = 0
        L = m.comp_loglik(So, No, X); R = np.exp(L - np.logaddexp.reduce(L, axis=1)[:, None])
        both = (N[:, a] > 0) & (N[:, b] > 0)
        od = pd = 0.0; nn = 0; has_other = 0
        flat = []
        for i in np.where(both)[0]:
            P = m.comp_probs(X[i]); pa, pb = P[:, a], P[:, b]; r = R[i]
            ya = [y for _, y in sorted(seq[items[i]][A], key=lambda t: t[0])]
            yb = [y for _, y in sorted(seq[items[i]][B], key=lambda t: t[0])]
            od += ya[0] != yb[0]; pd += r @ (pa * (1 - pb) + pb * (1 - pa)); nn += 1
            has_other += No[i].sum() > 0
            if len(ya) >= 2 and len(yb) >= 2:
                flat.append((r, pa, pb, len(ya), len(yb), (not any(ya)) and all(yb), all(ya) and not any(yb)))
        e1 = sum(r @ ((1 - pa) ** na * pb ** nb) for r, pa, pb, na, nb, _, _ in flat)
        e2 = sum(r @ (pa ** na * (1 - pb) ** nb) for r, pa, pb, na, nb, _, _ in flat)
        o1 = sum(f1 for *_, f1, _ in flat); o2 = sum(f2 for *_, f2 in flat)
        c1s, c2s = [], []
        cum = [np.cumsum(r) for r, *_ in flat]
        for _ in range(sims):
            c1 = c2 = 0
            for (r, pa, pb, na, nb, _, _), cu in zip(flat, cum):
                k = min(int(np.searchsorted(cu, rng.random() * cu[-1])), len(cu) - 1)
                ya = [rng.random() < pa[k] for _ in range(na)]; yb = [rng.random() < pb[k] for _ in range(nb)]
                c1 += (not any(ya)) and all(yb); c2 += all(ya) and not any(yb)
            c1s.append(c1); c2s.append(c2)
        c1s.sort(); c2s.sort(); lo, hi = int(0.025 * sims), int(0.975 * sims) - 1
        out.append(dict(A=A, B=B, n=nn, other=has_other, obs=od / nn, pred=pd / nn, ratio=od / pd,
                        flat_n=len(flat), o1=o1, e1=e1, b1=(c1s[lo], c1s[hi]), o2=o2, e2=e2, b2=(c2s[lo], c2s[hi])))
    return out

PAIRS = [("sonnet55", "grok46"), ("sonnet55", "opus55"), ("sonnet55", "haiku45nt"), ("haiku45nt", "grok46"),
         ("sonnet55", "gemini38flash"), ("grok46", "gemini38flash"), ("gemini38flash", "gemini31pro"), ("opus55", "grok46")]

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("name", nargs="?", default="continue-stop")
    ap.add_argument("--variants", default="1n,2n,1m,2m,2mf"); ap.add_argument("--checks", default="2m")
    ap.add_argument("--with-nolookup", action="store_true"); ap.add_argument("--no-heldout", action="store_true")
    ap.add_argument("--one-per-sheet", action="store_true")
    a = ap.parse_args()
    items, seq, S, N, X = load(a.name, a.with_nolookup, a.one_per_sheet)
    print(f"== {a.name}: items {len(items)}, answers {int(N.sum())}, unfamiliar items {int(X.sum())}"
          + (" (no-lookup re-asks included as Gemini answers)" if a.with_nolookup else ""))
    spec = {v: (int(v[0]), "m" in v, "f" in v) for v in a.variants.split(",")}
    if not a.no_heldout:
        for v, (pl, mix, fam) in spec.items():
            print(f"  held-out log-lik per answer, {v} ({pl}PL{', mixture' if mix else ''}{', familiarity' if fam else ''}): {heldout(S, N, X, pl, mix, fam):.4f}")
    for v in a.checks.split(","):
        pl, mix, fam = int(v[0]), "m" in v, "f" in v
        m = Model(pl, mix, fam).fit(S, N, X)
        print(f"\n  -- variant {v}: pi(C, S, M) = {np.round(m.pi, 3).tolist()}")
        for j, mm in enumerate(MINDS):
            print(f"     {mm:14s} alpha {m.alpha[j]:+.2f} slope {m.slope[j]:.2f}" + (f" gamma {m.gamma[j]:+.2f}" if fam else "")
                  + f"  eps {m.eps[0][j]:.3f}" + (f"/{m.eps[1][j]:.3f}" if fam else "") + f"  dlt {m.dlt[0][j]:.3f}" + (f"/{m.dlt[1][j]:.3f}" if fam else ""))
        for r in pair_checks(m, items, seq, S, N, X, PAIRS):
            print(f"     {r['A']:13s}{r['B']:14s} n={r['n']:5d} (other answers on {r['other']})  disagreement obs {r['obs']:.3f} pred {r['pred']:.3f} ratio {r['ratio']:.2f}"
                  f" | flat n={r['flat_n']:4d}: A0/B1 obs {r['o1']:3d} pred {r['e1']:6.1f} [{r['b1'][0]}-{r['b1'][1]}]  A1/B0 obs {r['o2']:3d} pred {r['e2']:6.1f} [{r['b2'][0]}-{r['b2'][1]}]")
