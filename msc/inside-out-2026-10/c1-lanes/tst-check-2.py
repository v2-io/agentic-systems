#!/usr/bin/env python3
"""KR C.1 / H.2. TST lane, second independent check: robustness of elapsed_time.py's form tests.

Imports the toolkit's own functions, so every baseline number is the landed script's.
Usage (from the directory holding the three dumps made with elapsed_time.py's header command):
    python3 <asf>/msc/inside-out-2026-10/c1-lanes/tst-check-2.py tst.log obsidian-linter.log ink.log
Prints, per history: (A) an author-day block bootstrap of section (6)'s window-free fits;
(B) a three-component mixture (one working, two idle); (C) low-quantile regressions on uncapped gaps;
(D) leave-outs (the top author only, without squash-merge-subject commits) with per-bin working medians and
capped Spearman; (E) section (7)'s null tested on the coefficient a as well as b; (F) changeset-size working
slopes under the block bootstrap, with and without squash-merge-subject commits. Seeds are fixed; runtime ~10 min.
"""
import contextlib
import io
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy import stats
from scipy.optimize import linprog
from scipy.stats import norm

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / '02-tst-core' / 'empirical-discontinuity'))
import elapsed_time as E  # noqa: E402

K = len(E.D_BINS)


def pairs(commits, dmax):
    by = defaultdict(list)
    for c in commits:
        if 'bot' in c['ae'] or not c['files']:
            continue
        by[c['ae']].append(c)
    rows = []
    for a, cs in by.items():
        cs.sort(key=lambda c: c['ad'])
        for i in range(1, len(cs)):
            g = (cs[i]['ad'] - cs[i - 1]['ad']) / 60.0
            dd = E.dscore(cs[i]['files'])
            if g > 0 and dd <= dmax:
                s = cs[i]['subj'].rstrip()
                rows.append((dd, g, cs[i]['lines'], len(cs[i]['files']), a, f"{a}|{cs[i]['ad'] // 86400}", '(#' in s and s.endswith(')')))
    cols = list(zip(*rows))
    return dict(d=np.array(cols[0], float), g=np.array(cols[1], float), L=np.array(cols[2], float), N=np.array(cols[3], float),
                auth=np.array(cols[4]), day=np.array(cols[5]), sq=np.array(cols[6]))


def sub(p, m):
    return {k: v[m] for k, v in p.items()}


def fit(y, d, b, form):
    return E.mixture_em(y, E.design(d, form), b, K)


def block_idx(rng, groups):
    pos = defaultdict(list)
    for i, gname in enumerate(groups):
        pos[gname].append(i)
    u = np.array(list(pos))
    return np.concatenate([pos[x] for x in rng.choice(u, len(u))])


def ci(a):
    return f"[{np.percentile(a, 2.5):+.2f},{np.percentile(a, 97.5):+.2f}]"


def em3(y, X, b, iters=1500):
    """Working N(X beta, s_w) with a per-bin share; two idle log-normal components with a shared split q."""
    beta = np.linalg.lstsq(X, y - 1, rcond=None)[0]
    mu1, mu2, s1, s2, s_w, q, pi, ll_old = np.percentile(y, 70), np.percentile(y, 92), 1.0, 1.0, 1.0, 0.5, np.full(K, 0.6), -np.inf
    for _ in range(iters):
        m = X @ beta
        p0 = pi[b] * norm.pdf(y, m, s_w); p1 = (1 - pi[b]) * q * norm.pdf(y, mu1, s1); p2 = (1 - pi[b]) * (1 - q) * norm.pdf(y, mu2, s2)
        tot = p0 + p1 + p2 + 1e-300; r0, r1, r2 = p0 / tot, p1 / tot, p2 / tot; ll = np.sum(np.log(tot))
        w = np.sqrt(r0); beta = np.linalg.lstsq(X * w[:, None], y * w, rcond=None)[0]
        for k in range(K):
            if (b == k).any():
                pi[k] = r0[b == k].mean()
        m = X @ beta; s_w = np.sqrt(np.sum(r0 * (y - m) ** 2) / r0.sum()); q = r1.sum() / (r1.sum() + r2.sum())
        mu1 = np.sum(r1 * y) / r1.sum(); s1 = max(np.sqrt(np.sum(r1 * (y - mu1) ** 2) / r1.sum()), 0.05)
        mu2 = np.sum(r2 * y) / r2.sum(); s2 = max(np.sqrt(np.sum(r2 * (y - mu2) ** 2) / r2.sum()), 0.05)
        if abs(ll - ll_old) < 1e-10:
            break
        ll_old = ll
    return dict(beta=beta, ll=ll, mu=(mu1, mu2), q=q)


def qreg(y, X, tau):
    n, p = X.shape
    c = np.r_[np.zeros(2 * p), tau * np.ones(n), (1 - tau) * np.ones(n)]
    z = linprog(c, A_eq=np.hstack([X, -X, np.eye(n), -np.eye(n)]), b_eq=y, bounds=[(0, None)] * (2 * p + 2 * n), method='highs').x
    return z[:p] - z[p:2 * p]


def window_free(p, label, nb=200, seed=21):
    rng = np.random.default_rng(seed)
    y, d, b = np.log(p['g']), p['d'], E.bin_index(p['d'], E.D_BINS)
    f, fp, fe, fb = (fit(y, d, b, k) for k in ('nest', 'pow', 'exp', 'bins'))
    med = np.exp(fb['beta'][0] + np.r_[0, fb['beta'][1:]])
    print(f"  [{label}] N={len(y)}: nested a={f['beta'][1]:+.3f} b={f['beta'][2]:+.3f}; power exponent {fp['beta'][1]:.2f}; "
          f"LL power-exp {fp['ll'] - fe['ll']:+.1f}; working medians by d bin {', '.join(f'{x:.1f}' for x in med)}")
    bs, fail = [], 0
    for _ in range(nb):
        i = block_idx(rng, p['day'])
        try:
            bs.append((fit(y[i], d[i], b[i], 'nest')['beta'], fit(y[i], d[i], b[i], 'pow')['beta'][1]))
        except Exception:
            fail += 1
    print(f"     author-day block bootstrap ({len(set(p['day']))} blocks, {nb} draws, {fail} failed): "
          f"a {ci([x[0][1] for x in bs])}  b {ci([x[0][2] for x in bs])}  exponent {ci([x[1] for x in bs])}")
    return fe


def main(path):
    with contextlib.redirect_stderr(io.StringIO()):
        cs = E.parse(path)
        p = pairs(cs, 25)
        name = Path(path).stem
        print(f"\n### {name}")
        top = max(set(p['auth']), key=lambda a: (p['auth'] == a).sum())
        print(f"  pairs {len(p['d'])}; author emails with pairs {len(set(p['auth']))}; top email share {(p['auth'] == top).mean():.2f}; "
              f"author-days {len(set(p['day']))}; pairs whose commit has a squash-merge subject {int(p['sq'].sum())}")
        print(" (A) window-free fits, author-day block bootstrap:")
        window_free(p, 'all pairs')
        y, d, b = np.log(p['g']), p['d'], E.bin_index(p['d'], E.D_BINS)
        print(" (B) three-component mixture (two idle components):")
        o = {f: em3(y, E.design(d, f), b) for f in ('nest', 'pow', 'exp')}
        rng = np.random.default_rng(31); bs = []
        for _ in range(100):
            i = rng.integers(0, len(y), len(y))
            try:
                bs.append((em3(y[i], E.design(d[i], 'nest'), b[i])['beta'], em3(y[i], E.design(d[i], 'pow'), b[i])['beta'][1]))
            except Exception:
                pass
        print(f"  nested a={o['nest']['beta'][1]:+.3f} b={o['nest']['beta'][2]:+.3f}; exponent {o['pow']['beta'][1]:.2f}; LL power-exp {o['pow']['ll'] - o['exp']['ll']:+.1f}; "
              f"iid bootstrap ({len(bs)}): a {ci([x[0][1] for x in bs])} b {ci([x[0][2] for x in bs])} exponent {ci([x[1] for x in bs])}")
        print(" (C) low-quantile regression of log T on (1, d, log(1+d)), uncapped (biased by the per-bin idle share; a sensitivity):")
        for tau in (0.1, 0.2):
            qb = qreg(y, E.design(d, 'nest'), tau)
            print(f"  tau={tau}: a={qb[1]:+.3f} b={qb[2]:+.3f}")
        print(" (D) leave-outs:")
        window_free(sub(p, p['auth'] == top), f"only {top.split('@')[0]}", nb=100)
        if p['sq'].any():
            ns = sub(p, ~p['sq'])
            window_free(ns, 'no squash-merge-subject commits', nb=200)
            for cap in (60, 240):
                k = ns['g'] <= cap
                print(f"     no-squash cap={cap}: N={k.sum()} Spearman={stats.spearmanr(ns['d'][k], ns['g'][k])[0]:.2f}")
        print(" (E) section (7)'s pure-exponential null, tested on a as well as b:")
        with contextlib.redirect_stdout(io.StringIO()):
            dd, gg, fexp = E.mixture_form(name, cs)
        rng = np.random.default_rng(12); n, bb = len(dd), E.bin_index(dd, E.D_BINS)
        X = np.column_stack([np.ones(n), dd, np.log1p(dd)]); caps = (60, 240, 480, 1440)
        obs = {c: np.linalg.lstsq(X[gg <= c], np.log(gg[gg <= c]), rcond=None)[0] for c in caps}
        null = {c: [] for c in caps}
        for _ in range(300):
            work = rng.random(n) < fexp['pi'][bb]
            ys = np.where(work, fexp['beta'][0] + fexp['beta'][1] * dd + rng.normal(0, fexp['s_w'], n), rng.normal(fexp['mu_i'], fexp['s_i'], n))
            for c in caps:
                m = ys <= np.log(c); null[c].append(np.linalg.lstsq(X[m], ys[m], rcond=None)[0])
        be = fexp['beta']
        print(f"  the null's working median: {np.exp(be[0]):.1f} min at d=0, {np.exp(be[0] + 10 * be[1]):.0f} at d=10, {np.exp(be[0] + 20 * be[1]):.0f} at d=20; its idle median {np.exp(fexp['mu_i']):.0f}")
        for c in caps:
            nb_ = np.array(null[c])
            print(f"  cap={c:<5} observed a={obs[c][1]:+.3f}; null a 2.5% {np.percentile(nb_[:, 1], 2.5):+.3f}, median {np.median(nb_[:, 1]):+.3f}; "
                  f"P(null a <= observed a)={np.mean(nb_[:, 1] <= obs[c][1]):.3f}; P(null b >= observed b)={np.mean(nb_[:, 2] >= obs[c][2]):.3f}")
        print(" (F) changeset size, working-time slopes under the author-day block bootstrap (all d):")
        pa = pairs(cs, 10 ** 9)
        for lab, q in (('all', pa), ('no squash-merge-subject', sub(pa, ~pa['sq']))):
            if lab != 'all' and len(q['g']) == len(pa['g']):
                continue
            yy = np.log(q['g']); rng = np.random.default_rng(41)
            for nm, x, v, edges in (('lines', np.log1p(q['L']), q['L'], E.L_BINS), ('files', np.log(q['N']), q['N'], E.F_BINS)):
                bq = E.bin_index(v, edges); Xc = np.column_stack([np.ones(len(yy)), x])
                s = E.mixture_em(yy, Xc, bq, len(edges))['beta'][1]; bs = []
                for _ in range(200):
                    i = block_idx(rng, q['day'])
                    try:
                        bs.append(E.mixture_em(yy[i], Xc[i], bq[i], len(edges))['beta'][1])
                    except Exception:
                        pass
                print(f"  [{lab}] N={len(yy)} slope on {nm} {s:.2f} block {ci(bs)}")


if __name__ == '__main__':
    import warnings
    warnings.filterwarnings('ignore')
    for path in sys.argv[1:]:
        main(path)
