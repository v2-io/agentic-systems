# KR C.2 / C.1 -- independent check of the Part II integration (identification side), reviews/part-ii-check-1-identification.md, 2026-10-30. Run: python3 -I <this file>
"""Does the on-policy sufficiency test I(X; o | M, a) 'pass for free' under a deterministic policy?
Uses the C2 spike's witness (sim-strategy-counts-confound.py) at epsilon = 0, with ties broken
deterministically (prefer action 0) so the policy is a deterministic function of X_t = (M_t, G_t).
Computes the on-policy conditional mutual information I(G_t; o_{t+1} | M_t, a_t) in bits (plug-in)
and the gap between the M_t-stratified and X_t-stratified on-policy estimates of E[o | a=1]."""
import random, math
from collections import defaultdict

def run(epsilon, tie, episodes=200000, T=8, seed=7):
    rng = random.Random(seed)
    joint = defaultdict(int)  # (M, a, X, o) -> count
    for _ in range(episodes):
        theta = rng.random() < 0.5
        q1 = 0.8 if theta else 0.2
        c = {0: [1, 1], 1: [1, 1]}
        for t in range(T):
            X = (t, *c[0], *c[1])
            m = {a: c[a][0] / sum(c[a]) for a in (0, 1)}
            if m[1] > m[0]: g = 1
            elif m[0] > m[1]: g = 0
            else: g = tie if tie is not None else rng.choice((0, 1))
            a = g if rng.random() >= epsilon else rng.choice((0, 1))
            o = int(rng.random() < (q1 if a == 1 else 0.5))
            joint[(t, a, X, o)] += 1
            c[a][0 if o else 1] += 1
    # I(X; o | M, a) plug-in
    n = sum(joint.values())
    cMa = defaultdict(int); cMaX = defaultdict(int); cMao = defaultdict(int)
    for (M, a, X, o), k in joint.items():
        cMa[(M, a)] += k; cMaX[(M, a, X)] += k; cMao[(M, a, o)] += k
    I = 0.0
    for (M, a, X, o), k in joint.items():
        I += k / n * math.log2(k * cMa[(M, a)] / (cMaX[(M, a, X)] * cMao[(M, a, o)]))
    # E[o | a=1] stratified on M vs averaged X-stratified, a=1 cells only
    print(f"eps={epsilon} tie={tie}: on-policy I(X; o | M, a) = {I:.4f} bits")
    for M in range(T):
        num = sum(k for (MM, a, X, o), k in joint.items() if MM == M and a == 1 and o == 1)
        den = sum(k for (MM, a, X, o), k in joint.items() if MM == M and a == 1)
        Xs = {X for (MM, a, X, o) in joint if MM == M and a == 1}
        if den == 0: continue
        vals = []
        for X in Xs:
            s = joint.get((M, 1, X, 1), 0); d = cMaX[(M, 1, X)]
            vals.append((s / d, d))
        lo, hi = min(v for v, d in vals if d > 200), max(v for v, d in vals if d > 200)
        print(f"   M={M}: E[o|M,a=1]={num/den:.3f}; across X-cells (n>200) E[o|X,a=1] ranges {lo:.3f}..{hi:.3f}")

run(0.0, tie=0)
