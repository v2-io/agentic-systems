"""Glyph-level, mind-specific departures: for every triad answer (both eras), the residual y - p of committing to a
middle under the additive model (alpha_m fitted on all triads; beta_i from minds other than the answering one). Per
(glyph, mind): the residuals summed over triads holding the glyph, and a z-score against their binomial variance.
Glyphs with a large negative z for one mind are those that mind specifically declines to place. Also: per (glyph,
mind), the share of order answers whose set holds the glyph that put it in 'extra' or left it out."""
import collections, math, sys
import lib, additive as AD
from values import ckey

recs, man = lib.load()
sig = AD.sig
tri = collections.defaultdict(lambda: collections.defaultdict(list))
glyphs_of = {}
for r in recs:
    x = AD.outcome(r)
    if not x or x[0] != "triad-commit" or x[1] is None: continue
    q = ckey(r); tri[q][r["mind"]].append(x[1]); glyphs_of[q] = tuple(r.get("shown") or r.get("context"))
minds = sorted({m for d in tri.values() for m in d}); alpha = {m: 0.0 for m in minds}
def fit_beta(d, excl=()):
    obs = [(alpha[m], y) for m, ys in d.items() if m not in excl for y in ys]
    if not obs: return None
    b = 0.0
    for _ in range(25):
        g = sum(y - sig(a + b) for a, y in obs); h = sum(sig(a + b) * (1 - sig(a + b)) for a, _ in obs) + 0.25
        b += (g - 0.25 * b) / h
    return b
for _ in range(6):
    beta = {q: fit_beta(d) for q, d in tri.items()}
    for m in minds:
        obs = [(beta[q], y) for q in tri for y in tri[q].get(m, [])]
        a = alpha[m]
        for _ in range(10):
            g = sum(y - sig(a + b) for b, y in obs); h = sum(sig(a + b) * (1 - sig(a + b)) for b, _ in obs) + 1e-9
            a += g / h
        alpha[m] = a
acc = collections.defaultdict(lambda: [0.0, 0.0, 0])
for q, d in tri.items():
    for m, ys in d.items():
        b = fit_beta(d, excl=(m,))
        if b is None: continue
        p = sig(alpha[m] + b)
        for g in set(glyphs_of[q]):
            for y in ys:
                a = acc[(g, m)]; a[0] += y - p; a[1] += p * (1 - p); a[2] += 1
rows = [(a[0] / math.sqrt(a[1]) if a[1] > 0 else 0, g, m, a[2], a[0] / a[2]) for (g, m), a in acc.items() if a[2] >= 8]
rows.sort()
print("most negative (declines to place, beyond its threshold and the item):")
for z, g, m, n, mr in rows[:40]: print(f"  z={z:6.2f}  {g} U+{ord(g):04X}  {m:14s} n={n:3d} mean resid {mr:+.2f}")
print("most positive:")
for z, g, m, n, mr in rows[-15:]: print(f"  z={z:6.2f}  {g} U+{ord(g):04X}  {m:14s} n={n:3d} mean resid {mr:+.2f}")
print("triads scanned", len(tri), "glyph-mind cells", len(rows))
