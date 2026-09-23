#!/usr/bin/env python3
"""Checks run by the de-novo auditor (de-novo-feedback-1.md). Sections A-D: corroboration closed form, real-vs-model honest scatter, oracle gain comparison, R7 interior policy (first parameter set), K=0 knowledge check. Then the R7 parameter scan and the linear-pool vs median check."""

import numpy as np
from itertools import product
from scipy.stats import multivariate_normal as mvn, norm
from scipy.optimize import minimize

def p_adv_liar_m(m, pA, pH, U0=1e4, L2=25.0, eps2=1e-4):
    m = np.asarray(m, float); J = len(m)
    ps = np.array([pA] + [pH]*(J-1)); num = den = 0.0
    for lm in product([0,1], repeat=J):
        lm = np.array(lm)
        prior = np.prod(np.where(lm==1, 1-ps, ps))
        cov = U0*np.ones((J,J)) + np.diag(np.where(lm==1, L2, eps2))
        w = prior*mvn.pdf(m, mean=np.zeros(J), cov=cov)
        den += w; num += w*(lm[0]==1)
    return num/den

b, L2 = 5.0, 25.0
print("A. corroboration factor: measured vs asymptotic closed form (K>=2 transitions)")
for eps2 in [1e-4, 1e-2, 1.0]:
    odds = []
    for K in [1,2,3,4]:
        p = p_adv_liar_m([b]+[0.0]*K, 0.99, 0.5, eps2=eps2); odds.append(p/(1-p))
    for K in [1,2,3]:
        pred = np.sqrt(L2/eps2)*np.exp(b*b/(2*L2))*np.sqrt(K/(K+1))
        print(f"  sqrt(L2/eps2)={np.sqrt(L2/eps2):6.0f} K={K}->{K+1}: measured {odds[K]/odds[K-1]:8.2f}  closed(asymptotic) {pred:8.2f}")
print("  pH dependence (eps2=1e-2, K=2->3): ")
for pH in [0.1,0.5,0.9]:
    o2 = p_adv_liar_m([b,0,0],0.99,pH,eps2=1e-2); o3 = p_adv_liar_m([b,0,0,0],0.99,pH,eps2=1e-2)
    r = (o3/(1-o3))/(o2/(1-o2)); print(f"   pH={pH}: measured {r:8.2f}  closed {pH/(1-pH)*50*np.exp(0.5)*np.sqrt(2/3):8.2f}")

print("\nA2. honest reports with REAL scatter delta (sd) vs model eps: P(A liar) with K=3 honest")
rng = np.random.default_rng(1)
for delta in [0.0, 0.1, 1.0]:
    for eps in [0.01, 0.1, 1.0]:
        ps_ = [p_adv_liar_m([b]+list(rng.normal(0,delta,3)),0.99,0.5,eps2=eps**2) for _ in range(20)]
        print(f"  actual scatter {delta:4}  model eps {eps:5}:  mean P(A liar) = {np.mean(ps_):.3f}")

print("\nB. honest-gain 'suppression' is identical for an honest source; compare oracle gain")
U0, s2, sH2 = 4.0, 1.0, 1.0
for n in [1,10,100,1000]:
    Un = 1/(1/U0+n/s2); etaH = Un/(Un+sH2)
    mse_lie = (Un*n*b/s2)**2 + Un**2*n/s2
    mse_honest = Un**2*n/s2 + (Un/U0*0)**2
    print(f"  n={n:5}: believed gain {etaH:.4f} (same under honest source);  oracle gain under lie {mse_lie/(mse_lie+sH2):.3f};  oracle under honest {(mse_honest+0)/(mse_honest+sH2):.4f}")

print("\nC. R7 interior policy: steady-state tracking with own channel + biased testimony")
Q, Ro, RT, qB, dcrit = 0.1, 1.0, 0.01, 1.0, 0.5
def mse(k):
    ko, kT = k
    if ko<0 or kT<0 or ko+kT>=2 or ko+kT<=0: return 1e9
    bias = kT*qB/(ko+kT)
    var = (Q + ko**2*Ro + kT**2*RT)/(1-(1-ko-kT)**2)
    return bias**2+var
own = minimize(lambda k: mse([k[0],0.0]), [0.3], method='Nelder-Mead').fun
# full trust = Kalman gains treating testimony as unbiased: steady state of 2-channel KF
P=1.0
for _ in range(10000):
    Pp=P+Q; Pn=1/(1/Pp+1/Ro+1/RT); P=Pn
Pp=P+Q; ko_f=Pn/Ro; kT_f=Pn/RT
full = mse([ko_f,kT_f])
best = minimize(mse,[0.3,0.05],method='Nelder-Mead')
print(f"  tolerance MSE <= {dcrit**2:.3f}")
print(f"  own-channel only (best gain): MSE={own:.3f}  -> {'fails' if own>dcrit**2 else 'ok'}")
print(f"  full trust in testimony:      MSE={full:.3f}  (bias {kT_f*qB/(ko_f+kT_f):.3f}) -> {'fails' if full>dcrit**2 else 'ok'}")
print(f"  interior (ko,kT)={best.x.round(3)}: MSE={best.fun:.3f} bias={best.x[1]*qB/best.x.sum():.3f} -> {'fails' if best.fun>dcrit**2 else 'ok'}")

print("\nD. K=0, content prior N(0,1), lie at 5 prior-sd, pA=0.99: P(A liar)")
num = 0.01*norm.pdf(5,0,np.sqrt(1+25)); den = num + 0.99*norm.pdf(5,0,np.sqrt(1+1e-4))
print(f"  {num/den:.4f}")

print("\n=== R7 scan ===")
def run(Q,Ro,RT,qB,dcrit):
    def mse(k):
        ko,kT=k
        if ko<0 or kT<0 or ko+kT>=2 or ko+kT<=1e-9: return 1e9
        return (kT*qB/(ko+kT))**2 + (Q+ko**2*Ro+kT**2*RT)/(1-(1-ko-kT)**2)
    own=min(mse([k,0]) for k in np.linspace(1e-3,1.5,3000))
    P=1.0
    for _ in range(5000):
        Pp=P+Q; P=1/(1/Pp+1/Ro+1/RT)
    full=mse([P/Ro,P/RT])
    best=min((minimize(mse,x0,method='Nelder-Mead') for x0 in ([0.3,0.05],[0.5,0.2],[0.2,0.01])), key=lambda r:r.fun)
    return own,full,best
for Q,Ro,RT,qB,dcrit in [(0.1,1,0.01,0.6,0.5),(0.1,1,0.01,0.55,0.5),(0.08,1,0.001,0.6,0.5),(0.1,1,0.05,0.7,0.5)]:
    own,full,best=run(Q,Ro,RT,qB,dcrit)
    k=best.x; print(f"Q={Q} Ro={Ro} RT={RT} qB={qB} tol MSE={dcrit**2:.3f}: own={own:.3f} full={full:.3f} interior={best.fun:.3f} (ko,kT)={k.round(3)} bias={k[1]*qB/k.sum():.3f}")
for Q in [0.05,0.06,0.07]:
  for qB in [0.55,0.7,1.0]:
    own,full,best=run(Q,1.0,0.001,qB,0.5); k=best.x
    flag = own>0.25 and full>0.25 and qB>0.5 and best.fun<0.25
    print(f"Q={Q} qB={qB}: own={own:.3f} full={full:.3f} interior={best.fun:.3f} bias={k[1]*qB/k.sum():.3f} {'<-- dilemma condition met, interior policy succeeds' if flag else ''}")

print("\n=== minority independent deceivers: linear pool vs median (no token history) ===")
r = np.random.default_rng(0)
for B in [5, 50, 500]:
    em, ed = [], []
    for _ in range(20000):
        x = np.r_[r.normal(0, 1, 7), B + r.normal(0, 1, 3)]
        em.append(x.mean()); ed.append(np.median(x))
    print(f"B={B}: linear-pool bias {np.mean(em):7.2f}; median bias {np.mean(ed):.3f}")
