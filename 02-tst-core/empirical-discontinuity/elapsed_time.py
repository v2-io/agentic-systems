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

Usage: python3 elapsed_time.py <name>.log ...

Per repository it prints: (1) single-form fits (linear; exponential by least squares) and
rank correlations at session caps of 60/120/240 min, d <= 25; (2) the nested form test
log T = c + a*d + b*log(1+d) [+ g*log(1+lines)] with 2000-draw bootstrap 95% intervals at caps
60/240/480 (the exponential form predicts a > 0 with b ~ 0; a power form predicts b > 0 with
a ~ 0); (3) binned medians on gaps up to 24 h with the share of each bin above 60 and 480 min,
which a session cap cannot distort while under half of a bin is censored.
"""
import sys
from collections import defaultdict
from pathlib import PurePosixPath

import numpy as np
from scipy import stats
from scipy.optimize import curve_fit

RNG = np.random.default_rng(0)


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


def dscore(files):
    """The toolkit's score: file transitions + 2 * directory transitions, in git's path order."""
    if len(files) <= 1:
        return 0
    dirs = [str(PurePosixPath(f).parent) for f in files]
    return (len(files) - 1) + 2 * sum(1 for i in range(1, len(dirs)) if dirs[i] != dirs[i - 1])


def gaps(commits, cap, dmax):
    by = defaultdict(list)
    for c in commits:
        if 'bot' in c['ae'] or not c['files']:
            continue
        by[c['ae']].append(c)
    D, G, L = [], [], []
    for cs in by.values():
        cs.sort(key=lambda c: c['ad'])
        for i in range(1, len(cs)):
            g = (cs[i]['ad'] - cs[i - 1]['ad']) / 60.0
            dd = dscore(cs[i]['files'])
            if 0 < g <= cap and dd <= dmax:
                D.append(dd); G.append(g); L.append(cs[i]['lines'])
    return np.array(D, float), np.array(G, float), np.array(L, float)


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
    for cap in (60, 240, 480):
        d, g, lc = gaps(commits, cap, 25)
        n = len(d)
        if n < 30:
            continue
        y, l = np.log(g), np.log1p(lc)
        for lines in (False, True):
            def coefs(idx):
                cols = [np.ones(len(idx)), d[idx], np.log1p(d[idx])] + ([l[idx]] if lines else [])
                return np.linalg.lstsq(np.column_stack(cols), y[idx], rcond=None)[0]
            full = coefs(np.arange(n))
            bs = np.array([coefs(RNG.integers(0, n, n)) for _ in range(2000)])
            lo, hi = np.percentile(bs, [2.5, 97.5], axis=0)
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


if __name__ == '__main__':
    for path in sys.argv[1:]:
        cs = parse(path)
        name = PurePosixPath(path).stem
        sq = sum(1 for c in cs if '(#' in c['subj'] and c['subj'].rstrip().endswith(')'))
        print(f"\n### {name}: {len(cs)} non-merge commits; {sq} with squash-merge subjects '(#N)'; "
              f"{len(set(c['ae'] for c in cs))} author emails")
        print(" single-form fits, d <= 25:"); single_form(name, cs)
        print(" nested form test, d <= 25:"); nested_form(name, cs)
        print(" medians on gaps <= 24 h:"); censoring(name, cs)
