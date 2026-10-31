#!/usr/bin/env python3
# KR C.2 -- de-novo-feedback-1.md check script (independent checker, Opus 5.5, 2026-10-30). Run: python3 -I <this file>
# Feedback section 1: Lemma 1(b) (P-stream) with past actions retained -- exact enumeration.
# Lemma 1(b) under (P-stream) with past ACTIONS retained but not past coins/observations.
# Exact enumeration. theta ~ Bern(1/2) static env; o1 = theta; one shared coin u ~ Bern(1/2) used at both steps.
# X1 = o1; a1 = X1 xor u.  X2 = a1 (retains past action, drops o1).  a2 = u (policy reads coin; P(a2=a|X2)=1/2: positivity holds).
# Outcome of step 2: Y2^(a) = 1[a == theta].
from itertools import product
from fractions import Fraction as F
joint = {}
for th, u in product((0,1),(0,1)):
    p = F(1,4); a1 = th ^ u; X2 = a1; a2 = u
    joint[(th,u)] = (p, X2, a2)
for x in (0,1):
    for a in (0,1):
        num = sum(p for (th,u),(p,X2,a2) in joint.items() if X2==x and a2==a and (1 if a==th else 0)==1)
        den = sum(p for (th,u),(p,X2,a2) in joint.items() if X2==x and a2==a)
        intv = sum(p*(1 if a==th else 0) for (th,u),(p,X2,a2) in joint.items() if X2==x) / sum(p for (th,u),(p,X2,a2) in joint.items() if X2==x)
        print(f"X2={x} a={a}: P(a|X2)={den/sum(p for k,(p,X2,_) in joint.items() if X2==x)}  on-policy P(o=1|a,X2)={num/den}  interventional P(Y^a=1|X2)={intv}")
