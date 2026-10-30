#!/usr/bin/env python3
# KR C.2 -- de-novo-feedback-1.md check script (independent checker, Opus 5.5, 2026-10-30). Run: python3 -I <this file>
# Feedback section 3: identified untaken-action effect vs hidden-theta truth at eps=0. Seed 7 here; the file reports seeds 11 and 23 too (edit Random(7)).
# eps=0: for X cells where only a=0 was ever taken, estimate P(o=1|do(a=1),X) via the Z=(t,a1-counts) cell's
# on-policy a=1 success rate (taken at OTHER X cells), and compare against truth E[q1 | X] from hidden theta.
import random
from collections import defaultdict
rng=random.Random(7); T=8
Xq=defaultdict(lambda:[0.0,0]); Xacts=defaultdict(set); XtoZ={}; Z1=defaultdict(lambda:[0,0])
for _ in range(200000):
    th=rng.random()<0.5; q1=0.8 if th else 0.2; c={0:[1,1],1:[1,1]}
    for t in range(T):
        X=(t,*c[0],*c[1]); Z=(t,*c[1]); XtoZ[X]=Z
        m={a:c[a][0]/sum(c[a]) for a in (0,1)}
        a=1 if m[1]>m[0] else (0 if m[0]>m[1] else rng.choice((0,1)))
        o=1 if rng.random()<(q1 if a==1 else 0.5) else 0
        Xq[X][0]+=q1; Xq[X][1]+=1; Xacts[X].add(a)
        if a==1: Z1[Z][0]+=o; Z1[Z][1]+=1
        c[a][0 if o else 1]+=1
err=[]; 
for X,acts in Xacts.items():
    if acts=={0} and Z1[XtoZ[X]][1]>=2000:
        est=Z1[XtoZ[X]][0]/Z1[XtoZ[X]][1]; tru=Xq[X][0]/Xq[X][1]; err.append((abs(est-tru),X,est,tru,Xq[X][1]))
err.sort(reverse=True)
print(len(err),"a=0-only X cells with >=2000 a=1 samples in their Z cell; max |est-truth| =", round(err[0][0],4))
for e in err[:5]: print("  X",e[1],"est",round(e[2],3),"truth",round(e[3],3),"visits",e[4],"Z a=1 n",Z1[XtoZ[e[1]]][1])
