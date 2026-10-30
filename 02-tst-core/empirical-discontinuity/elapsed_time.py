#!/usr/bin/env python3
"""Elapsed-time test of the exponential discontinuity form.

Time here is real: for each author, the elapsed time between a commit and that author's
previous commit. Nothing in it is computed from the counts that build the discontinuity
score d, unlike `commit_time_estimate` in analyze_git_history.py (see reproduce_estimate_fit.py).

Input: one dump per repository, made with
    git -C <repo> log --no-merges --date=unix --format='@@@%H|%ae|%ad|%cd|%s' --numstat > <name>.log

Run on 2026-10-30 against (path, HEAD):
    ~/src/_core/tst (v2-io/temporal-software-theory)           a37e5eff5124be4d39d892e235c9882e38cc3d17
    ~/src/_ref/obsidian-linter (github.com/platers/obsidian-linter) b8f4168680e2967a70c566fb5ba3f7c89119a4dd
    ~/src/_ref/ink (github.com/vadimdemedes/ink)               45ed972ddfd3b508ed6397f9f844d076454a891c
    ~/src/_ref/anthropic-sdk-python                            2e2f663104c8926434088828c08fbdf202d6d6fd
    ~/src/_ref/gemini-cli (github.com/google-gemini/gemini-cli) 2515b89e2b03e241a8301d18ab8de1e2fbf9149c
    ~/src/_ref/codex (github.com/openai/codex)                 1cd1cf17c6f11d5d7f513763b47ec55d1fe980a4

Usage: python3 elapsed_time.py [--keep-squash] <name>.log ...

Pairs. A pair is an author's commit and that author's previous commit; its time is the gap
between their author dates, its d and size are the later commit's. Bot authors and commits
with no changed paths are left out. So is every pair with a squash-merged commit at either end,
recognized by GitHub's squash subject ending "(#N)": a squash merge's author date is the merge
time, so a gap ending or starting there measures merge cadence, not work. --keep-squash keeps
them; that is how the three squash-merged histories above are run, as a check on the method.
Every bootstrap resamples author-days (all pairs whose later commit falls on one UTC day for
one author), because consecutive gaps within a session are not independent.

Per repository it prints: (1) single-form fits (linear; exponential by least squares) and
rank correlations at session caps of 60/120/240 min, d <= 25; (2) the nested form test
log T = c + a*d + b*log(1+d) [+ g*log(1+lines)] with 2000-draw bootstrap 95% intervals at caps
60/240/480 (the exponential form predicts a > 0 with b ~ 0; a power form predicts b > 0 with
a ~ 0); (3) binned medians on gaps up to 24 h with the share of each bin above 60 and 480 min;
(4) changeset-size slopes and medians on gaps up to 24 h.

Every window drops the gaps above it, and the dropped share grows with d, so (2)-(4) are
truncated samples: their medians and slopes depend on the window, and counting the dropped gaps
as censored instead puts days away into the median. (5)-(8) measure that dependence and remove it.
(5) the window sweep: per bin, the share above 24 h and the median with those gaps dropped vs
counted as censored; and at caps 60 min to none, the nested fit, the pure power slope of log T on
log(1+d), the least-squares exponential rate of log T on d, and the slope on log(1+lines);
(6) a window-free form test: a two-component log-normal mixture on uncapped log gaps, a working
component whose mean is a form in d and an idle component, with a mixing weight per d bin; it
prints per-bin working-time medians, the nested form inside the working component, the
working-time power exponent, and the log-likelihoods of the exponential, power and nested forms;
then the power exponent again with time away modelled by two idle components, a likelihood with
several optima, so the fit is the best of 30 starts and each bootstrap draw starts from it;
(7) a parametric null for the windowed test of (2): 1000 times, simulate the fitted mixture with a PURE
EXPONENTIAL working component on the history's own d values, apply each cap, refit (2)'s nested
OLS, and report how often the null's b reaches the observed b and how often its a falls as low as
the observed a; it also prints that fitted exponential's working medians at d = 10 and 20 beside
its idle median; (8) changeset size, window-free: the same mixture with the working mean linear in
log(1+lines) or log(files), per-bin working medians by lines, and the ratio of the 201-1000-line
bin's working median to the 11-50-line bin's, with and without the 0-10-line bin's median
subtracted from both as a fixed per-commit overhead (not defined unless the three medians rise). The mixture is a modelling choice
(log-normal components, one or two idle components); its numbers are heuristic tier like the
rest. Sections (5)-(8) use their own seeded generators.
"""
import sys
from collections import defaultdict
from pathlib import PurePosixPath

import numpy as np
from scipy import stats
from scipy.optimize import curve_fit
from scipy.stats import norm

RNG = np.random.default_rng(0)
KEEP_SQUASH = False


def parse(path):
    commits, cur = [], None
    for line in open(path, errors='replace'):
        line = line.rstrip('\n')
        if line.startswith('@@@'):
            h, ae, ad, cd, subj = line[3:].split('|', 4)
            cur = dict(h=h, ae=ae.lower(), ad=int(ad), cd=int(cd), subj=subj, files=[], lines=0)
            commits.append(cur)
        elif line.strip() and cur is not None:
            parts = line.split('\t')
            if len(parts) == 3:
                a, dl, p = parts
                cur['files'].append(p)
                cur['lines'] += (int(a) if a.isdigit() else 0) + (int(dl) if dl.isdigit() else 0)
    return commits


def is_squash(c):
    s = c['subj'].rstrip()
    return '(#' in s and s.endswith(')')


def dscore(files):
    """The toolkit's score: file transitions + 2 * directory transitions, in git's path order."""
    if len(files) <= 1:
        return 0
    dirs = [str(PurePosixPath(f).parent) for f in files]
    return (len(files) - 1) + 2 * sum(1 for i in range(1, len(dirs)) if dirs[i] != dirs[i - 1])


def pairs(commits):
    """Every same-author consecutive pair with a positive gap; see the module docstring for what is left out."""
    by = defaultdict(list)
    for c in commits:
        if 'bot' in c['ae'] or not c['files']:
            continue
        by[c['ae']].append(c)
    rows = []
    for cs in by.values():
        cs.sort(key=lambda c: c['ad'])
        for i in range(1, len(cs)):
            if not KEEP_SQUASH and (is_squash(cs[i]) or is_squash(cs[i - 1])):
                continue
            g = (cs[i]['ad'] - cs[i - 1]['ad']) / 60.0
            if g > 0:
                rows.append((dscore(cs[i]['files']), g, cs[i]['lines'], len(cs[i]['files']), cs[i]['ae'], f"{cs[i]['ae']}|{cs[i]['ad'] // 86400}"))
    if not rows:
        return dict(d=np.zeros(0), g=np.zeros(0), L=np.zeros(0), N=np.zeros(0), auth=np.zeros(0, str), day=np.zeros(0, str))
    d, g, L, N, auth, day = zip(*rows)
    return dict(d=np.array(d, float), g=np.array(g, float), L=np.array(L, float), N=np.array(N, float),
                auth=np.array(auth), day=np.array(day))


def select(p, cap, dmax):
    m = (p['g'] <= cap) & (p['d'] <= dmax)
    return {k: v[m] for k, v in p.items()}


def gaps(commits, cap, dmax):
    q = select(pairs(commits), cap, dmax)
    return q['d'], q['g'], q['L']


def boot(rng, groups, nb):
    """nb resampled index arrays, drawing whole author-days with replacement."""
    pos = defaultdict(list)
    for i, gname in enumerate(groups):
        pos[gname].append(i)
    blocks = [np.array(v) for v in pos.values()]
    for _ in range(nb):
        yield np.concatenate([blocks[j] for j in rng.integers(0, len(blocks), len(blocks))])


def draws(fn, rng, groups, nb):
    """fn on nb author-day resamples; a draw whose fit fails or is not finite is skipped and counted."""
    out, failed = [], 0
    for i in boot(rng, groups, nb):
        try:
            r = np.asarray(fn(i), float)
        except Exception:
            failed += 1; continue
        if np.all(np.isfinite(r)):
            out.append(r)
        else:
            failed += 1
    return np.array(out), failed


def ci(x):
    lo, hi = np.percentile(x, [2.5, 97.5], axis=0)
    return lo, hi


def expm(x, a, al):
    return a * (1 + al) ** x


def single_form(name, commits):
    for cap in (60, 120, 240):
        d, g, lc = gaps(commits, cap, 25)
        if len(d) < 30:
            print(f"  cap={cap:<4} N={len(d)} too few"); continue
        r = stats.linregress(d, g)[2]
        try:
            p, _ = curve_fit(expm, d, g, p0=[np.median(g), 0.05], maxfev=20000)
            yp = expm(d, *p)
            er2, al = 1 - np.sum((g - yp) ** 2) / np.sum((g - g.mean()) ** 2), p[1]
        except Exception:
            er2 = al = float('nan')
        rd, rg, rl = (stats.rankdata(x) for x in (d, g, lc))
        res = lambda y, x: y - np.polyval(np.polyfit(x, y, 1), x)
        prho = np.corrcoef(res(rd, rl), res(rg, rl))[0, 1]
        print(f"  cap={cap:<4} N={len(d):<5} spearman={stats.spearmanr(d, g)[0]:.2f} "
              f"partial|lines={prho:.2f} linR2={r * r:.3f} expR2={er2:.3f} forced-alpha={al:.3f}")


def nested_form(name, commits):
    p = pairs(commits)
    for cap in (60, 240, 480):
        q = select(p, cap, 25)
        d, g, lc, n = q['d'], q['g'], q['L'], len(q['d'])
        if n < 30:
            continue
        y, l = np.log(g), np.log1p(lc)
        for lines in (False, True):
            def coefs(idx):
                cols = [np.ones(len(idx)), d[idx], np.log1p(d[idx])] + ([l[idx]] if lines else [])
                return np.linalg.lstsq(np.column_stack(cols), y[idx], rcond=None)[0]
            full = coefs(np.arange(n))
            lo, hi = ci(np.array([coefs(i) for i in boot(RNG, q['day'], 2000)]))
            tag = '+lines' if lines else '      '
            extra = f"  g(lines)={full[3]:+.3f} [{lo[3]:+.3f},{hi[3]:+.3f}]" if lines else ''
            print(f"  cap={cap:<3} N={n:<4} {tag} a(d)={full[1]:+.3f} [{lo[1]:+.3f},{hi[1]:+.3f}]  "
                  f"b(log1+d)={full[2]:+.3f} [{lo[2]:+.3f},{hi[2]:+.3f}]" + extra)


def censoring(name, commits):
    d, g, _ = gaps(commits, 1440, 10 ** 9)
    for lo, hi in [(0, 0), (1, 2), (3, 5), (6, 10), (11, 25), (26, 60)]:
        m = (d >= lo) & (d <= hi)
        if m.sum():
            x = g[m]
            print(f"  d {lo:>2}-{hi:<2} n={m.sum():<4} median={np.median(x):7.1f} min  "
                  f"P(>60)={np.mean(x > 60):.2f}  P(>480)={np.mean(x > 480):.2f}")


def changeset_size(name, commits):
    """Proportionality to changeset size predicts a log-log slope of 1 and medians that scale with size."""
    q = select(pairs(commits), 1440, 10 ** 9)
    G, L, N = q['g'], q['L'], q['N']
    if len(G) < 30:
        return
    for lo, hi in [(0, 10), (11, 50), (51, 200), (201, 1000), (1001, 10 ** 9)]:
        m = (L >= lo) & (L <= hi)
        if m.sum():
            print(f"  lines {lo:>5}-{hi if hi < 10 ** 9 else 'inf':<5} n={m.sum():<4} median={np.median(G[m]):7.1f} min")
    for lo, hi in [(1, 1), (2, 3), (4, 10), (11, 30), (31, 10 ** 9)]:
        m = (N >= lo) & (N <= hi)
        if m.sum():
            print(f"  files {lo:>3}-{hi if hi < 10 ** 9 else 'inf':<4} n={m.sum():<4} median={np.median(G[m]):7.1f} min")
    for cap in (240, 1440):
        m = G <= cap
        y, days = np.log(G[m]), q['day'][m]
        for lab, x in (('log(1+lines)', np.log1p(L[m])), ('log(files)', np.log(N[m]))):
            s = np.polyfit(x, y, 1)[0]
            lo_, hi_ = ci([np.polyfit(x[i], y[i], 1)[0] for i in boot(RNG, days, 1000)])
            print(f"  cap={cap:<5} slope of log T on {lab:<13} = {s:.3f} [{lo_:.3f},{hi_:.3f}]")


D_BINS = [(0, 0), (1, 2), (3, 5), (6, 10), (11, 25)]
L_BINS = [(0, 10), (11, 50), (51, 200), (201, 1000), (1001, 10 ** 12)]
F_BINS = [(1, 1), (2, 3), (4, 10), (11, 30), (31, 10 ** 12)]
NONE = float('inf')


def bin_index(v, edges):
    b = np.full(len(v), -1)
    for k, (lo, hi) in enumerate(edges):
        b[(v >= lo) & (v <= hi)] = k
    return b


def window_sweep(name, commits):
    rng = np.random.default_rng(10)
    p = pairs(commits)
    d, g = p['d'], p['g']
    for lo, hi in [(0, 0), (1, 2), (3, 5), (6, 10), (11, 25), (26, 60)]:
        x = g[(d >= lo) & (d <= hi)]
        if len(x):
            print(f"  d {lo:>2}-{hi:<2} n={len(x):<4} P(>24h)={np.mean(x > 1440):.2f}  median, >24h dropped={np.median(x[x <= 1440]):7.1f}"
                  f"  median, >24h censored={np.median(np.where(x <= 1440, x, np.inf)):7.1f} min")
    for cap in (60, 240, 480, 1440, 10080, NONE):
        q = select(p, cap, 25)
        d, g, n = q['d'], q['g'], len(q['d'])
        if n < 30:
            continue
        y = np.log(g)
        X = np.column_stack([np.ones(n), d, np.log1p(d)])
        full = np.linalg.lstsq(X, y, rcond=None)[0]
        lo, hi = ci(np.array([np.linalg.lstsq(X[i], y[i], rcond=None)[0] for i in boot(rng, q['day'], 1000)]))
        pw = np.polyfit(np.log1p(d), y, 1)[0]
        er = np.expm1(np.polyfit(d, y, 1)[0])
        q2 = select(p, cap, 10 ** 9)
        ls = np.polyfit(np.log1p(q2['L']), np.log(q2['g']), 1)[0]
        print(f"  cap={'none' if cap == NONE else int(cap):<5} N={n:<5} a(d)={full[1]:+.3f} [{lo[1]:+.3f},{hi[1]:+.3f}]  "
              f"b(log1+d)={full[2]:+.3f} [{lo[2]:+.3f},{hi[2]:+.3f}]  power slope={pw:.2f}  exp rate(log-OLS)={er:.3f}  "
              f"slope on log(1+lines), all d={ls:.2f}")


def mixture_em(y, X, b, K, iters=600):
    """Working component N(X beta, s_w), idle component N(mu_i, s_i), working share pi[k] per bin k."""
    beta = np.linalg.lstsq(X, y - 1, rcond=None)[0]
    mu_i, s_i, s_w, pi = np.percentile(y, 85), 1.0, 1.0, np.full(K, 0.7)
    ll_old = -np.inf
    for _ in range(iters):
        m = X @ beta
        pw = pi[b] * norm.pdf(y, m, s_w); pid = (1 - pi[b]) * norm.pdf(y, mu_i, s_i)
        tot = pw + pid + 1e-300; r = pw / tot; ll = np.sum(np.log(tot))
        w = np.sqrt(r); beta = np.linalg.lstsq(X * w[:, None], y * w, rcond=None)[0]
        for k in range(K):
            if (b == k).any():
                pi[k] = r[b == k].mean()
        m = X @ beta; s_w = np.sqrt(np.sum(r * (y - m) ** 2) / r.sum())
        mu_i = np.sum((1 - r) * y) / np.sum(1 - r); s_i = np.sqrt(np.sum((1 - r) * (y - mu_i) ** 2) / np.sum(1 - r))
        if abs(ll - ll_old) < 1e-10:
            break
        ll_old = ll
    return dict(beta=beta, s_w=s_w, mu_i=mu_i, s_i=s_i, pi=pi, ll=ll)


def mixture_em2(y, X, b, K, start=None, iters=3000):
    """As mixture_em, with time away modelled by two idle log-normal components sharing a split q.
    This likelihood has several optima, so the full-data fit takes the best of many starts (two_idle)
    and a bootstrap draw starts from that fit. start: an int seeds a random start; a dict is a fitted state."""
    if isinstance(start, dict):
        beta, mu1, mu2, s1, s2, s_w, q, pi = (start[k] if k != 'pi' else start[k].copy() for k in ('beta', 'mu1', 'mu2', 's1', 's2', 's_w', 'q', 'pi'))
    else:
        r = np.random.default_rng(start)
        beta = np.linalg.lstsq(X, y - r.uniform(0.5, 2.5), rcond=None)[0]
        mu1, mu2 = np.sort(r.uniform(np.percentile(y, 50), np.percentile(y, 99), 2))
        s1, s2, s_w, q, pi = r.uniform(0.5, 1.5), r.uniform(0.5, 1.5), r.uniform(0.6, 1.4), r.uniform(0.2, 0.8), np.full(K, r.uniform(0.4, 0.8))
    ll_old = -np.inf
    for _ in range(iters):
        m = X @ beta
        p0 = pi[b] * norm.pdf(y, m, s_w); p1 = (1 - pi[b]) * q * norm.pdf(y, mu1, s1); p2 = (1 - pi[b]) * (1 - q) * norm.pdf(y, mu2, s2)
        tot = p0 + p1 + p2 + 1e-300; r0, r1, r2 = p0 / tot, p1 / tot, p2 / tot; ll = np.sum(np.log(tot))
        w = np.sqrt(r0); beta = np.linalg.lstsq(X * w[:, None], y * w, rcond=None)[0]
        for k in range(K):
            if (b == k).any():
                pi[k] = r0[b == k].mean()
        m = X @ beta; s_w = max(np.sqrt(np.sum(r0 * (y - m) ** 2) / r0.sum()), 0.05); q = r1.sum() / (r1.sum() + r2.sum())
        mu1 = np.sum(r1 * y) / r1.sum(); s1 = max(np.sqrt(np.sum(r1 * (y - mu1) ** 2) / r1.sum()), 0.05)
        mu2 = np.sum(r2 * y) / r2.sum(); s2 = max(np.sqrt(np.sum(r2 * (y - mu2) ** 2) / r2.sum()), 0.05)
        if abs(ll - ll_old) < 1e-10:
            break
        ll_old = ll
    return dict(beta=beta, mu1=mu1, mu2=mu2, s1=s1, s2=s2, s_w=s_w, q=q, pi=pi, ll=ll)


def two_idle(y, X, b, K, starts=30):
    """The best of `starts` random starts of mixture_em2, and the number of distinct optima they reached."""
    fits = [mixture_em2(y, X, b, K, s) for s in range(starts)]
    fits = [f for f in fits if np.isfinite(f['ll'])]
    return max(fits, key=lambda f: f['ll']), len({round(f['ll'], 1) for f in fits})


def design(d, form):
    cols = {'exp': [d], 'pow': [np.log1p(d)], 'nest': [d, np.log1p(d)],
            'bins': [(bin_index(d, D_BINS) == k).astype(float) for k in range(1, len(D_BINS))]}[form]
    return np.column_stack([np.ones(len(d))] + cols)


def mixture_form(name, commits):
    rng = np.random.default_rng(11)
    q = select(pairs(commits), NONE, 25)
    d, g, days = q['d'], q['g'], q['day']
    y, b, n, K = np.log(g), bin_index(d, D_BINS), len(d), len(D_BINS)
    fits = {f: mixture_em(y, design(d, f), b, K) for f in ('bins', 'exp', 'pow', 'nest')}
    med = lambda fit: np.exp(fit['beta'][0] + np.r_[0, fit['beta'][1:]])  # intercept + per-bin offset
    bs, f1 = draws(lambda i: med(mixture_em(y[i], design(d[i], 'bins'), b[i], K)), rng, days, 100); lo, hi = ci(bs)
    print(f"  N={n} uncapped gaps, d <= 25, {len(set(days))} author-days; idle median {np.exp(fits['bins']['mu_i']):.0f} min; working share by bin "
          + ', '.join(f'{p:.2f}' for p in fits['bins']['pi']))
    print("  working-time medians, d = 0, 1-2, 3-5, 6-10, 11-25: "
          + ', '.join(f'{m:.1f} [{a:.1f},{c:.1f}]' for m, a, c in zip(med(fits['bins']), lo, hi)) + ' min')
    bs, f2 = draws(lambda i: mixture_em(y[i], design(d[i], 'nest'), b[i], K)['beta'], rng, days, 200); lo, hi = ci(bs); be = fits['nest']['beta']
    print(f"  nested form in the working component: a(d)={be[1]:+.3f} [{lo[1]:+.3f},{hi[1]:+.3f}]  b(log1+d)={be[2]:+.3f} [{lo[2]:+.3f},{hi[2]:+.3f}]")
    bs, f3 = draws(lambda i: mixture_em(y[i], design(d[i], 'pow'), b[i], K)['beta'][1], rng, days, 200); plo, phi = ci(bs)
    print(f"  working-time power exponent={fits['pow']['beta'][1]:.2f} [{plo:.2f},{phi:.2f}]; "
          f"working-time exponential rate={np.expm1(fits['exp']['beta'][1]):.3f}")
    print(f"  log-likelihood: exponential {fits['exp']['ll']:.1f}, power {fits['pow']['ll']:.1f}, nested {fits['nest']['ll']:.1f}")
    rng2 = np.random.default_rng(14)
    (te, ne), (tp, npw) = two_idle(y, design(d, 'exp'), b, K), two_idle(y, design(d, 'pow'), b, K)
    bs, f4 = draws(lambda i: mixture_em2(y[i], design(d[i], 'pow'), b[i], K, start=tp)['beta'][1], rng2, days, 100); plo, phi = ci(bs)
    idle = sorted(np.exp([tp['mu1'], tp['mu2']]))
    print(f"  with two idle components (best of 30 starts; {npw} distinct optima for the power form, {ne} for the exponential): "
          f"power exponent={tp['beta'][1]:.2f} [{plo:.2f},{phi:.2f}] (bootstrap draws start from the best fit); "
          f"idle medians {idle[0]:.0f} and {idle[1]:.0f} min, working s.d. {tp['s_w']:.2f}; log-likelihood power - exponential {tp['ll'] - te['ll']:+.1f}")
    if f1 + f2 + f3 + f4:
        print(f"  (bootstrap draws whose fit failed and were skipped: {f1}, {f2}, {f3}, {f4} of 100, 200, 200, 100)")
    return d, g, fits['exp']


def windowed_null(name, d, g, fexp, reps=1000):
    rng = np.random.default_rng(12)
    n, b = len(d), bin_index(d, D_BINS)
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
    be = fexp['beta']
    print(f"  the fitted exponential's working median: {np.exp(be[0]):.1f} min at d=0, {np.exp(be[0] + 10 * be[1]):.0f} at d=10, "
          f"{np.exp(be[0] + 20 * be[1]):.0f} at d=20; its idle median {np.exp(fexp['mu_i']):.0f} min")
    for c in caps:
        nb = np.array(null[c])
        print(f"  cap={c:<5} observed a={obs[c][1]:+.3f} b={obs[c][2]:+.3f}; pure-exponential null: a median {np.median(nb[:, 1]):+.3f}, "
              f"b 95% [{np.percentile(nb[:, 2], 2.5):+.3f},{np.percentile(nb[:, 2], 97.5):+.3f}], "
              f"P(null b >= observed b)={np.mean(nb[:, 2] >= obs[c][2]):.3f}, P(null a <= observed a)={np.mean(nb[:, 1] <= obs[c][1]):.3f}")


def changeset_mixture(name, commits):
    rng = np.random.default_rng(13)
    p = pairs(commits)
    y, L, N, days = np.log(p['g']), p['L'], p['N'], p['day']
    n = len(y)
    for lab, x, v, edges in (('log(1+lines)', np.log1p(L), L, L_BINS), ('log(files)', np.log(N), N, F_BINS)):
        b = bin_index(v, edges); X = np.column_stack([np.ones(n), x])
        s = mixture_em(y, X, b, len(edges))['beta'][1]
        bs, fl = draws(lambda i: mixture_em(y[i], X[i], b[i], len(edges))['beta'][1], rng, days, 200); lo, hi = ci(bs)
        print(f"  N={n} uncapped; working-time slope on {lab:<13}= {s:.2f} [{lo:.2f},{hi:.2f}]" + (f" ({fl} failed draws skipped)" if fl else ''))
    b = bin_index(L, L_BINS)
    X = np.column_stack([np.ones(n)] + [(b == k).astype(float) for k in range(1, len(L_BINS))])
    be = mixture_em(y, X, b, len(L_BINS))['beta']
    med = np.exp(be[0] + np.r_[0, be[1:]])
    print("  working-time medians by lines 0-10, 11-50, 51-200, 201-1000, >1000: " + ', '.join(f'{m:.1f}' for m in med)
          + " min; median lines per bin: " + ', '.join(f'{np.median(L[b == k]):.0f}' for k in range(len(L_BINS))))
    ratio = f"{(med[3] - med[0]) / (med[1] - med[0]):.2f}x" if med[3] > med[1] > med[0] else "not defined (the medians do not rise across these bins)"
    print(f"  201-1000 over 11-50 lines: {np.median(L[b == 3]) / np.median(L[b == 1]):.1f}x the lines ({(b == 3).sum()} and {(b == 1).sum()} pairs), "
          f"{med[3] / med[1]:.2f}x the working time; with the 0-10 bin's median subtracted from both as overhead, {ratio}")


if __name__ == '__main__':
    args = sys.argv[1:]
    if '--keep-squash' in args:
        KEEP_SQUASH = True
        args.remove('--keep-squash')
    for path in args:
        cs = parse(path)
        name = PurePosixPath(path).stem
        sq = sum(1 for c in cs if is_squash(c))
        p = pairs(cs)
        if len(p['g']):
            top = max(set(p['auth']), key=lambda a: (p['auth'] == a).sum())
            who = f"; {len(p['g'])} pairs from {len(set(p['auth']))} author emails, {np.mean(p['auth'] == top):.2f} of them from the most frequent"
        else:
            who = '; no pairs'
        print(f"\n### {name}: {len(cs)} non-merge commits; {sq} with squash-merge subjects '(#N)' "
              f"({'kept' if KEEP_SQUASH else 'pairs touching them left out'}); {len(set(c['ae'] for c in cs))} author emails{who}")
        print(" (1) single-form fits, d <= 25:"); single_form(name, cs)
        print(" (2) nested form test, d <= 25:"); nested_form(name, cs)
        print(" (3) medians on gaps <= 24 h (gaps above dropped):"); censoring(name, cs)
        print(" (4) changeset size (gaps <= 24 h):"); changeset_size(name, cs)
        print(" (5) window sweep:"); window_sweep(name, cs)
        print(" (6) window-free form test (work/idle mixture):"); d, g, fexp = mixture_form(name, cs)
        print(" (7) windowed nested fit against a pure-exponential null:"); windowed_null(name, d, g, fexp)
        print(" (8) changeset size, window-free:"); changeset_mixture(name, cs)
