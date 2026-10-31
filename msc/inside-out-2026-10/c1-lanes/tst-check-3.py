#!/usr/bin/env python3
"""KR C.1 / H.2. Third independent check of the TST lane (round 3, 4ea60ca9..945bea3d on main).

Prints the numbers in c1-lanes/tst-check-3.md that elapsed_time.py does not print itself:
  (A) pair counts with and without squash-merge pairs, date equality, top-email shares at d <= 25;
  (B) the one-idle mixture from 30 random starts per form (does the toolkit's fit sit at the maximum?);
  (C) the two-idle power exponent on author-day bootstrap draws, warm-started from the full-data fit
      (as the toolkit does) and refitted from 10 random starts, side by side.
Run from a directory holding tst.log, obsidian-linter.log and ink.log, dumped with the command in
elapsed_time.py's header:  python3 <this> [A] [B] [C]   (C takes about 80 s)
"""
import sys
from pathlib import Path

import numpy as np
from scipy.stats import norm

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / '02-tst-core' / 'empirical-discontinuity'))
import elapsed_time as et  # noqa: E402

HIST = ('tst', 'obsidian-linter', 'ink')


def block_a():
    for name in HIST:
        cs = et.parse(f'{name}.log')
        et.KEEP_SQUASH = True; pk = et.pairs(cs)
        et.KEEP_SQUASH = False; pf = et.pairs(cs)
        sq = [c for c in cs if et.is_squash(c)]; ns = [c for c in cs if not et.is_squash(c)]
        a = pf['auth'][pf['d'] <= 25]; top = max(set(a), key=lambda x: (a == x).sum())
        print(f"(A) {name}: pairs d<=25 kept {(pk['d'] <= 25).sum()}, filtered {(pf['d'] <= 25).sum()}; "
              f"squash commits {len(sq)}, author date = commit date in {sum(c['ad'] == c['cd'] for c in sq)}; "
              f"other commits {len(ns)}, equal in {sum(c['ad'] == c['cd'] for c in ns)}; "
              f"top email {np.mean(a == top):.3f} of {len(a)} pairs from {len(set(a))} emails")


def em1_random(y, X, b, K, seed, iters=2000):
    r = np.random.default_rng(seed)
    beta = np.linalg.lstsq(X, y - r.uniform(0.5, 3.0), rcond=None)[0]
    mu_i, s_i, s_w = r.uniform(np.percentile(y, 30), np.percentile(y, 99)), r.uniform(0.5, 2), r.uniform(0.5, 2)
    pi, ll_old = np.full(K, r.uniform(0.3, 0.9)), -np.inf
    for _ in range(iters):
        pw = pi[b] * norm.pdf(y, X @ beta, s_w); pid = (1 - pi[b]) * norm.pdf(y, mu_i, s_i)
        tot = pw + pid + 1e-300; rr = pw / tot; ll = np.sum(np.log(tot))
        w = np.sqrt(rr); beta = np.linalg.lstsq(X * w[:, None], y * w, rcond=None)[0]
        for k in range(K):
            if (b == k).any():
                pi[k] = rr[b == k].mean()
        m = X @ beta; s_w = max(np.sqrt(np.sum(rr * (y - m) ** 2) / rr.sum()), 0.05)
        mu_i = np.sum((1 - rr) * y) / np.sum(1 - rr); s_i = max(np.sqrt(np.sum((1 - rr) * (y - mu_i) ** 2) / np.sum(1 - rr)), 0.05)
        if abs(ll - ll_old) < 1e-10:
            break
        ll_old = ll
    return dict(beta=beta, s_w=s_w, mu_i=mu_i, ll=ll)


def data(name):
    q = et.select(et.pairs(et.parse(f'{name}.log')), et.NONE, 25)
    return np.log(q['g']), q['d'], et.bin_index(q['d'], et.D_BINS), len(et.D_BINS), q['day']


def block_b():
    for name in HIST:
        y, d, b, K, _ = data(name)
        for form in ('pow', 'exp', 'nest'):
            X = et.design(d, form)
            tool = et.mixture_em(y, X, b, K)
            fits = [f for f in (em1_random(y, X, b, K, s) for s in range(30)) if np.isfinite(f['ll'])]
            best = max(fits, key=lambda f: f['ll'])
            print(f"(B) {name} {form}: toolkit ll {tool['ll']:.1f}, idle median {np.exp(tool['mu_i']):.0f} min; "
                  f"best of 30 ll {best['ll']:.1f}, idle median {np.exp(best['mu_i']):.0f} min, working s.d. {best['s_w']:.2f}")


def block_c(nb=40):
    y, d, b, K, days = data('obsidian-linter')
    X = et.design(d, 'pow')
    tp, _ = et.two_idle(y, X, b, K)
    warm, cold = [], []
    for i in et.boot(np.random.default_rng(77), days, nb):
        warm.append(et.mixture_em2(y[i], X[i], b[i], K, start=tp)['beta'][1])
        fits = [f for f in (et.mixture_em2(y[i], X[i], b[i], K, s) for s in range(10)) if np.isfinite(f['ll'])]
        cold.append(max(fits, key=lambda f: f['ll'])['beta'][1])
    warm, cold = np.array(warm), np.array(cold)
    print(f"(C) obsidian-linter two-idle power exponent {tp['beta'][1]:.3f}; {nb} draws, 2.5/50/97.5 percentiles: "
          f"warm-started {np.percentile(warm, [2.5, 50, 97.5]).round(2)}, best of 10 random starts "
          f"{np.percentile(cold, [2.5, 50, 97.5]).round(2)}; draws differing by more than 0.1: {np.mean(abs(warm - cold) > 0.1):.2f}")


if __name__ == '__main__':
    np.seterr(all='ignore')
    want = set(sys.argv[1:]) or {'A', 'B', 'C'}
    for k, f in (('A', block_a), ('B', block_b), ('C', block_c)):
        if k in want:
            f()
