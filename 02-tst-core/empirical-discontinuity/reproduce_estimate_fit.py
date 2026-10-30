#!/usr/bin/env python3
"""Reproduce the original alpha ~ 0.118 fit and show what sets it (README.md section 1).

Input: data/commits.json, the 229 commits the original fit used. The script checks that the
saved commit_time_estimate equals the miner's formula 10 + 5n + 0.15L, refits the exponential
under other time formulas (V1 is the formula the former METHODOLOGY.md printed, which the code
never ran), reports the fix-message rate by d, and, as a first look, fits the same commits'
real inter-commit gaps (elapsed_time.py is the fuller test).
Usage: python3 reproduce_estimate_fit.py data/commits.json
"""
import json, sys
from datetime import datetime
import numpy as np
from scipy.optimize import curve_fit
from scipy import stats

path = sys.argv[1]
C = json.load(open(path))

def td_min(s):
    days = 0
    if 'day' in s:
        dpart, s = s.split(', ')
        days = int(dpart.split()[0])
    h, m, sec = s.split(':')
    return days * 1440 + int(h) * 60 + int(m) + float(sec) / 60

n = np.array([c['files_changed'] for c in C], float)
L = np.array([c['lines_added'] + c['lines_deleted'] for c in C], float)
U = np.array([c['unique_directories'] for c in C], float)
d = np.array([c['discontinuity_score'] for c in C], float)
T_saved = np.array([td_min(c['commit_time_estimate']) for c in C])
ts = np.array([datetime.fromisoformat(c['timestamp']).timestamp() for c in C])

def exp_model(x, a, al):
    return a * (1 + al) ** x

def fit(x, y, label):
    out = {}
    sl, ic, r, _, _ = stats.linregress(x, y)
    out['lin_r2'] = r * r
    try:
        p, _ = curve_fit(exp_model, x, y, p0=[np.median(y), 0.05], maxfev=20000)
        yp = exp_model(x, *p)
        out['exp_r2'] = 1 - np.sum((y - yp) ** 2) / np.sum((y - y.mean()) ** 2)
        out['alpha'] = p[1]
    except Exception as e:
        out['exp_r2'] = float('nan'); out['alpha'] = float('nan')
    print(f"  {label:<52} N={len(x):<4} linR2={out['lin_r2']:.3f} expR2={out['exp_r2']:.3f} alpha={out['alpha']:.3f}")
    return out

# 0. the saved estimate equals the code's formula?
T_code = 10 + 5 * n + 0.15 * L
print("max |saved - (10+5n+0.15L)| =", np.abs(T_saved - T_code).max())
# d vs n
print("corr(d, n) =", np.corrcoef(d, n)[0, 1])

windows = [None, 100, 50, 25]
def run(T, label):
    print(label)
    for w in windows:
        m = np.ones_like(d, bool) if w is None else d <= w
        fit(d[m], T[m], f"d<={w}" if w else "all")

run(T_saved, "V0: saved estimate (code: 10 + 5n + 0.15L)")
run((30 + 15 * n + 0.5 * L) * (1 + 0.2 * U), "V1: METHODOLOGY.md's printed formula ((30+15n+0.5L)(1+0.2U))")
run(10 + 0.15 * L, "V2: lines only, no file term (10 + 0.15L)")
run(10 + 5 * n, "V3: files only (10 + 5n)")
run(10 + 5 * n + 1.5 * L, "V4: code formula with 10x per-line weight")

fix = np.array([c['is_bug_fix'] for c in C], bool)
print(f"\nfix-like message rate: d>10 {fix[d > 10].mean():.3f} (n={(d > 10).sum()}), "
      f"d<=10 {fix[d <= 10].mean():.3f} (n={(d <= 10).sum()})")

# real elapsed time: gap to previous commit (chronological), same author, capped sessions
order = np.argsort(ts)
gap = np.full(len(C), np.nan)
for i in range(1, len(order)):
    a, b = order[i - 1], order[i]
    if C[a]['author'] == C[b]['author']:
        gap[b] = (ts[b] - ts[a]) / 60.0
print("\nauthors:", set(c['author'] for c in C))
for cap in [60, 120, 240]:
    m = (~np.isnan(gap)) & (gap > 0) & (gap <= cap)
    print(f"\nV5: real inter-commit gap (minutes), session cap {cap} min: N={m.sum()}")
    for w in windows:
        mm = m & (np.ones_like(d, bool) if w is None else d <= w)
        if mm.sum() > 5:
            fit(d[mm], gap[mm], f"d<={w}" if w else "all")
    mm = m & (d <= 25)
    rho, p = stats.spearmanr(d[mm], gap[mm])
    print(f"  spearman(d, gap | d<=25) = {rho:.3f} (p={p:.3g})")
