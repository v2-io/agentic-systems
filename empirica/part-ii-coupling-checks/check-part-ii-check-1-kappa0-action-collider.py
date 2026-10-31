# KR C.2 / C.1 -- independent check of the Part II integration (identification side), reviews/part-ii-check-1-identification.md, 2026-10-30. Run: python3 -I <this file>
"""kappa_processing = 0 (well-defined: H(G | e_1, M_0) > 0), bounded signaling, exogenous goal -- and the
M_t-stratum is still confounded, because the goal-blind update keeps an observation whose meaning depends on
the action and drops the action.  (Same mechanism as der-directed-separation's V7 instance.)
W ~ Bern(1/2) persistent world bit; G ~ Bern(1/2) exogenous goal, independent of W.
Step 0: a_0 = G w.p. 0.9 else flipped; event e_1 = (a_0, o_1), o_1 = W xor a_0.
Goal-blind update M_1 = o_1: a function of e_1, so I(G; M_1 | e_1, M_0) = 0 while H(G | e_1, M_0) > 0.
Step 1: a_1 = G w.p. 0.9 else flipped.  Y^(1) = W, Y^(0) ~ Bern(1/2).  The goal reaches the world only via actions.
Run: python3 -I kappa0_action_collider.py"""
from fractions import Fraction as F
from itertools import product
from math import log2
P = {}
for g, w, f0, f1 in product((0, 1), repeat=4):
    p = F(1, 4) * (F(1, 10) if f0 else F(9, 10)) * (F(1, 10) if f1 else F(9, 10))
    a0 = g ^ f0; o1 = w ^ a0; e1 = (a0, o1); M1 = o1; a1 = g ^ f1
    P[(g, w, e1, M1, a1)] = P.get((g, w, e1, M1, a1), F(0)) + p
def marg(keys):
    out = {}
    for k, p in P.items():
        kk = tuple(k[i] for i in keys); out[kk] = out.get(kk, F(0)) + p
    return out
def H(keys):
    return -sum(float(p) * log2(float(p)) for p in marg(keys).values() if p > 0)
# indices: 0 g, 1 w, 2 e1, 3 M1, 4 a1
HG_e = H([0, 2]) - H([2]); I = H([0, 2]) + H([3, 2]) - H([0, 3, 2]) - H([2])
print(f"H(G | e_1) = {HG_e:.4f} bits;  I(G; M_1 | e_1) = {I:.4f} bits  ->  kappa_processing = {I / HG_e:.4f}")
for m in (0, 1):
    on = sum(p * w for (g, w, e, M, a), p in P.items() if M == m and a == 1) / sum(p for (g, w, e, M, a), p in P.items() if M == m and a == 1)
    iv = sum(p * w for (g, w, e, M, a), p in P.items() if M == m) / sum(p for (g, w, e, M, a), p in P.items() if M == m)
    xs = []
    for gg in (0, 1):
        onx = sum(p * w for (g, w, e, M, a), p in P.items() if M == m and g == gg and a == 1) / sum(p for (g, w, e, M, a), p in P.items() if M == m and g == gg and a == 1)
        ivx = sum(p * w for (g, w, e, M, a), p in P.items() if M == m and g == gg) / sum(p for (g, w, e, M, a), p in P.items() if M == m and g == gg)
        xs.append(f"G={gg}: {float(onx):.3f} vs {float(ivx):.3f}")
    print(f"M_1={m}: on-policy P(o=1|a=1,M) = {float(on):.3f}  vs  interventional P(Y^(1)=1|M) = {float(iv):.3f};  X-stratified on-policy vs interventional: " + "; ".join(xs))
