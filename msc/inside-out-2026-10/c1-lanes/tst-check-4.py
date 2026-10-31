#!/usr/bin/env python3
"""TST lane, check 4 (KR C.1, H.2): the numbers in tst-check-4.md that the toolkit does not print.

  python3 tst-check-4.py hazard
      #der-change-expectation-baseline's hazard-mixture route under four observation models, prior f(k) = exp(-k)
      (f(0) = 1, a = 1). Exact: median remaining life (1 + t0) when survival is the whole observation,
      (sqrt(2) - 1)(1 + t0) under the uniform-age likelihood. About 2 minutes.
  python3 tst-check-4.py minp REPS SEED <dir holding tst.log obsidian-linter.log ink.log>
      Section (7)'s smallest-tail-share test of elapsed_time.py, re-run with REPS null replicates drawn from SEED,
      as shipped and with the observed history pooled among the replicates (exchangeable). The dumps are made as
      elapsed_time.py's header says. Each history first refits section (6), whose bootstraps take most of the time.
      `minp 1000 12 DIR` reproduces the shipped section (7) line; SEED may be a comma list, and with several seeds
      the spread of the shipped statistic across them is printed.
"""
import sys
from pathlib import Path

import numpy as np


def hazard():
    rng = np.random.default_rng(4)
    n = 40_000_000
    k = rng.exponential(1.0, n)
    # (A) one system, start uniform over [-L, 0], seen alive at 0: the likelihood is flat in T >= t0 (survival).
    L = 2000.0
    age_a = rng.uniform(0, L, n)
    T_a = rng.exponential(1 / k)
    alive = T_a >= age_a
    # (B) every system shares the unknown k, systems start at a constant rate, and one alive system is met, drawn
    #     uniformly from those alive. Given k: age ~ Exp(k), remaining ~ Exp(k). (If instead meeting a system is an
    #     event whose chance grows with how many are alive, the posterior is survival's and this case joins A and C.)
    age_b = rng.exponential(1 / k)
    rem_b = rng.exponential(1 / k)
    # (C) each system its own k drawn from f, constant start rate, one alive system met: length-biased in T.
    # (D) per-system sampling: one system drawn from all, looked at a uniform point of its life.
    T = rng.exponential(1 / k)
    age = rng.uniform(0, 1, n) * T
    rem = T - age

    def wmedian(x, w):
        o = np.argsort(x)
        c = np.cumsum(w[o])
        return x[o][np.searchsorted(c, c[-1] / 2)]

    print("median remaining life / (1 + t0); survival-only observation predicts 1, uniform-age predicts sqrt(2)-1 = 0.414")
    for t0 in (10, 30, 100):
        sa = alive & (np.abs(age_a - t0) < 0.05 * t0)
        sb = np.abs(age_b - t0) < 0.05 * t0
        s = np.abs(age - t0) < 0.05 * t0
        print(f"  t0={t0:>3}: (A) {np.median((T_a - age_a)[sa]) / (1 + t0):.3f} (n={sa.sum()})"
              f"  (B) {np.median(rem_b[sb]) / (1 + t0):.3f} (n={sb.sum()})"
              f"  (C) {wmedian(rem[s], T[s]) / (1 + t0):.3f}  (D) {np.median(rem[s]) / (1 + t0):.3f} (n={s.sum()})")


def minp(reps, seeds, logdir):
    sys.path.insert(0, str(Path(__file__).resolve().parents[3] / '02-tst-core' / 'empirical-discontinuity'))
    import elapsed_time as et
    for name in ('tst', 'obsidian-linter', 'ink'):
        cs = et.parse(str(Path(logdir) / f'{name}.log'))
        print(f"\n### {name}")
        d, g, fexp = et.mixture_form(name, cs)
        shipped = []
        for seed in seeds:
            shipped.append(null_test(et, d, g, fexp, reps, seed))
        if len(seeds) > 1:
            v = np.array(shipped)
            print(f"  {len(seeds)} seeds x {reps} reps, as shipped: min {v.min():.3f} median {np.median(v):.3f} "
                  f"max {v.max():.3f} s.d. {v.std(ddof=1):.4f}")


def null_test(et, d, g, fexp, reps, seed):
    rng = np.random.default_rng(seed)
    n, b = len(d), et.bin_index(d, et.D_BINS)
    X = np.column_stack([np.ones(n), d, np.log1p(d)])
    caps = (60, 240, 480, 1440)
    obs = {c: np.linalg.lstsq(X[g <= c], np.log(g[g <= c]), rcond=None)[0] for c in caps}
    null = {c: [] for c in caps}
    for _ in range(reps):
        work = rng.random(n) < fexp['pi'][b]
        ys = np.where(work, fexp['beta'][0] + fexp['beta'][1] * d + rng.normal(0, fexp['s_w'], n),
                      rng.normal(fexp['mu_i'], fexp['s_i'], n))
        for c in caps:
            m = ys <= np.log(c)
            null[c].append(np.linalg.lstsq(X[m], ys[m], rcond=None)[0])
    st = np.column_stack([-np.array(null[c])[:, 1] for c in caps] + [np.array(null[c])[:, 2] for c in caps])
    ob = np.array([-obs[c][1] for c in caps] + [obs[c][2] for c in caps])
    srt = np.sort(st, axis=0)
    tail = lambda v, k: 1 - np.searchsorted(srt[:, k], v, side='left') / reps
    p_obs = min(tail(ob[k], k) for k in range(8))
    p_rep = np.min(np.column_stack([tail(st[:, k], k) for k in range(8)]), axis=1)
    allst = np.vstack([ob[None, :], st])
    srt2 = np.sort(allst, axis=0)
    tail2 = lambda v, k: 1 - np.searchsorted(srt2[:, k], v, side='left') / (reps + 1)
    pm = np.min(np.column_stack([tail2(allst[:, k], k) for k in range(8)]), axis=1)
    se = np.sqrt(0.05 * 0.95 / reps)
    print(f"  reps={reps} seed={seed}: smallest tail share {p_obs:.4f}; as shipped {np.mean(p_rep <= p_obs):.4f}; "
          f"pooled {np.mean(pm <= pm[0]):.4f}; Monte Carlo s.e. at 0.05: {se:.4f}")
    return np.mean(p_rep <= p_obs)


if __name__ == '__main__':
    if sys.argv[1:2] == ['hazard']:
        hazard()
    elif sys.argv[1:2] == ['minp']:
        minp(int(sys.argv[2]), [int(x) for x in sys.argv[3].split(',')], sys.argv[4])
    else:
        print(__doc__)
