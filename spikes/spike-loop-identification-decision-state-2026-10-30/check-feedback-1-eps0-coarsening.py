#!/usr/bin/env python3
# KR C.2 -- de-novo-feedback-1.md check script (independent checker, Opus 5.5, 2026-10-30). Run: python3 -I <this file>
# Feedback sections 3 and 8: re-runs the spike witness (seeds 1-3) and counts single-action X cells rescued by Z=(t, a1-counts).
# Re-run the spike's witness at several seeds, and at eps=0 ask: at the coarsening Z=(t, a1-counts),
# which is outcome-sufficient by construction (theta's posterior depends only on action-1 counts),
# how many visited X_t cells have the untaken action's effect identified via Z (both actions seen in the Z-cell)?
import random, sys
from collections import defaultdict
def run(eps, episodes=40000, T=8, seed=1):
    rng = random.Random(seed)
    byM = defaultdict(lambda:[0,0,0.0,0]); byX = defaultdict(lambda:[0,0,0.0,0]); byZ = defaultdict(lambda:[0,0,0.0,0])
    actsX = defaultdict(set); actsZ = defaultdict(set); Xvisits=defaultdict(int); XtoZ={}
    # for identification check: per Z cell, on-policy success of a=1 and a=0; truth per X cell
    for _ in range(episodes):
        th = rng.random()<0.5; q1 = 0.8 if th else 0.2
        c = {0:[1,1],1:[1,1]}
        for t in range(T):
            X=(t,c[0][0],c[0][1],c[1][0],c[1][1]); Z=(t,c[1][0],c[1][1]); XtoZ[X]=Z
            m={a:c[a][0]/(c[a][0]+c[a][1]) for a in (0,1)}
            g = 1 if m[1]>m[0] else (0 if m[0]>m[1] else rng.choice((0,1)))
            a = g if rng.random()>=eps else rng.choice((0,1))
            actsX[X].add(a); actsZ[Z].add(a); Xvisits[X]+=1
            o = 1 if rng.random() < (q1 if a==1 else 0.5) else 0
            for s,k in ((byM,t),(byX,X),(byZ,Z)):
                r=s[k]; r[2]+=q1; r[3]+=1
                if a==1: r[0]+=1; r[1]+=o
            c[a][0 if o else 1]+=1
    def gap(s):
        nc=ni=d=0.0
        for n1,s1,sq,n in s.values():
            if n1==0: continue
            nc+=s1; ni+=n1*sq/n; d+=n1
        return nc/d-ni/d
    det_X = [X for X,acts in actsX.items() if len(acts)==1]
    rescued = [X for X in det_X if len(actsZ[XtoZ[X]])==2]
    w = sum(Xvisits[X] for X in rescued)/sum(Xvisits[X] for X in det_X)
    print(f"eps={eps} seed={seed}: gap M={gap(byM):+.4f} X={gap(byX):+.4f} Z={gap(byZ):+.4f} | X cells {len(actsX)}, single-action X cells {len(det_X)}, of which contrast identified via Z: {len(rescued)} (visit-weighted {w:.2f})")
for seed in (1,2,3):
    for eps in (0.2,0.0): run(eps, seed=seed)
