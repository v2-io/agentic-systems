#!/usr/bin/env python3
# KR C.2 -- de-novo-feedback-1.md check script (independent checker, Opus 5.5, 2026-10-30). Run: python3 -I <this file>
# Feedback section 7: collider confounding at the M_t stratum when kappa > 0 -- exact enumeration.
# Collider route: an exogenous ("pure") goal G, a world bit W, observation o=W, and a goal-coupled model update:
# with prob kappa the update writes the goal into M ("wishful"), else it writes the observation. M = G w.p. kappa, else W.
# Policy reads G (a = G w.p. 0.9, else flipped): positivity at M holds. Outcome Y^(1) = W, Y^(0) ~ Bern(1/2).
# Compare on-policy P(o=1 | a=1, M) with interventional P(Y^(1)=1 | M). At kappa=0, M_t is not a collider of G and W.
from fractions import Fraction as F
from itertools import product
def table(kappa):
    out=[]
    for m in (0,1):
        num=den=iv=pm=F(0)
        for g,w,k,flip in product((0,1),(0,1),(0,1),(0,1)):
            p=F(1,4)*(kappa if k else 1-kappa)*(F(1,10) if flip else F(9,10))
            M = g if k else w
            if M!=m: continue
            a = g ^ flip
            pm+=p; iv+=p*w
            if a==1: den+=p; num+=p*w
        out.append(f"M={m}: on-policy {float(num/den):.3f} vs interventional {float(iv/pm):.3f}")
    print(f"kappa={kappa}: "+"; ".join(out))
for kappa in (F(0),F(1,10),F(3,10),F(1,2)): table(kappa)
