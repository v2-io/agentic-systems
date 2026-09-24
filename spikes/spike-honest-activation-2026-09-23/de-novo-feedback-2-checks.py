#!/usr/bin/env python3
"""De-novo re-check (de-novo-feedback-2.md): sensitivity of S13 consensus-trust capture to the deceiver's initial trust, incumbency, Sybil voice count, kernel width and rate; plus BSC capacity with honest error. The simulation core is copied from sims/checks.py run_consensus, extended with nA (deceiver voices) and dissent_from_start."""
import numpy as np
b=5.0
def run(K, D, T=6000, T0=300, kap=0.2, alpha=0.05, c=1.5, rA=0.99, rH0=0.5, seed=0, simultaneous=False, W=None, nA=1, dissent_from_start=False):
    # nA: number of deceiver voices (Sybils), all asserting b, all present from t=0
    g=np.random.default_rng(seed); mu=0.0
    r=[rA]*nA
    start = 0 if dissent_from_start else T0
    arrive=[0]*nA + ([start]*K if simultaneous else [start+k*D for k in range(K)])
    r += [rH0]*K
    for t in range(T):
        act=[j for j in range(nA+K) if arrive[j]<=t and (W is None or j<nA or t<arrive[j]+W)]
        y=np.array([(b if j<nA else 0.0)+g.normal(0,1) for j in act]); rr=np.array([r[j] for j in act])
        mu=(1-kap)*mu+kap*(rr*y).sum()/rr.sum()
        ag=np.exp(-(y-mu)**2/(2*c*c))
        for i,j in enumerate(act): r[j]+=alpha*(ag[i]-r[j])
    return mu
def cap(**kw): 
    v=[run(seed=s,**kw) for s in range(5)]; return f"{np.mean([x>2.5 for x in v]):.1f} captured (beliefs {', '.join(f'{x:.2f}' for x in v)})"
print("1. Authority irrelevant? lone dissenter (K=1), rA varied, incumbency from 300 steps of isolation")
for rA in [0.99,0.5,0.1]: print(f"  rA={rA}: {cap(K=1,D=0,simultaneous=True,rA=rA)}")
print("2. No incumbency: dissenter present from t=0")
for rA in [0.99,0.5]: print(f"  rA={rA}: {cap(K=1,D=0,simultaneous=True,rA=rA,dissent_from_start=True)}")
print("3. Two concurrent dissenters, rA varied")
for rA in [0.99,0.5]: print(f"  rA={rA}: {cap(K=2,D=0,simultaneous=True,rA=rA)}")
print("4. Sybil deceiver (nA voices) vs K concurrent dissenters")
for nA in [2,3]:
  for K in [2,3,4]:
    print(f"  nA={nA}, K={K}: {cap(K=K,D=0,simultaneous=True,nA=nA)}")
for K in [5,6,8]: print(f"  nA=3, K={K}: {cap(K=K,D=0,simultaneous=True,nA=3)}")
print("6. c (agreement kernel width) and alpha sensitivity, nA=1, K=2 concurrent")
for c in [0.75,1.5,3.0,6.0]: print(f"  c={c}: {cap(K=2,D=0,simultaneous=True,c=c)}")
for al in [0.01,0.2]: print(f"  alpha={al}: {cap(K=2,D=0,simultaneous=True,alpha=al)}")
from math import log2
H = lambda p: 0 if p in (0, 1) else -p*log2(p) - (1-p)*log2(1-p)
print("8. BSC capacity with honest error e and deception q (flip rate e+q-2eq)")
for e in [0, 0.02, 0.05]:
    for q in [0, 0.05]:
        f = e + q - 2*e*q; print(f"  e={e}, q={q}: capacity {1-H(f):.3f}")
