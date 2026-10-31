#!/usr/bin/env python3
# KR C.2 -- de-novo-feedback-1.md check script (independent checker, Opus 5.5, 2026-10-30). Run: python3 -I <this file>
# Feedback section 8: single-trajectory, regime-switching version of the witness.
# Singular-trajectory version of the witness: ONE long run, regime theta_t switching with hazard h,
# G_t = exponentially-discounted Beta counts per action (forgetting factor lam), eps-greedy; M_t constant.
# Time-averaged on-policy E[o | a=1] vs time-averaged interventional E[q1(theta_t)] over the same steps (the M-stratum is all steps).
# Also the X-level check: bin G_t's action-1 mean (the policy's input) and compare within bins.
import random
from collections import defaultdict
def run(h, lam=0.9, eps=0.1, steps=2_000_000, seed=1):
    rng=random.Random(seed); th=rng.random()<0.5; c={0:[1.0,1.0],1:[1.0,1.0]}
    s1=n1=0; sq=0.0; nall=0
    bins=defaultdict(lambda:[0,0,0.0,0])
    for _ in range(steps):
        if rng.random()<h: th = not th
        q1=0.8 if th else 0.2
        m={a:c[a][0]/sum(c[a]) for a in (0,1)}
        g=1 if m[1]>m[0] else (0 if m[0]>m[1] else rng.choice((0,1)))
        a=g if rng.random()>=eps else rng.choice((0,1))
        o=1 if rng.random()<(q1 if a==1 else 0.5) else 0
        sq+=q1; nall+=1
        b=(round(m[0],1),round(m[1],1)); r=bins[b]; r[2]+=q1; r[3]+=1
        if a==1: s1+=o; n1+=1; r[0]+=1; r[1]+=o
        for k in (0,1): c[k]=[lam*c[k][0]+(1-lam), lam*c[k][1]+(1-lam)]   # forget toward Beta(1,1)
        c[a][0 if o else 1]+=1
    nc=ni=d=0.0
    for a1,o1,q,n in bins.values():
        if a1: nc+=o1; ni+=a1*q/n; d+=a1
    print(f"h={h}: M-stratum on-policy E[o|a=1]={s1/n1:.4f} interventional={sq/nall:.4f} gap={s1/n1-sq/nall:+.4f} | binned-G gap={nc/d-ni/d:+.4f}")
for h in (0.0005, 0.005, 0.05): run(h)
