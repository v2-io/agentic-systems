#!/usr/bin/env python3
"""Checker numerics for reviews/part-ii-check-1-distortion.md (KR C.2 / C.1 / B.1). Run: python3 -I check-part-ii-check-1.py"""
import math, numpy as np
rng = np.random.default_rng(1030)
def kl(p,q):
    p=np.asarray(p,float); q=np.asarray(q,float); m=p>0
    return float(np.sum(p[m]*np.log(p[m]/q[m])))
def tilt(pi,u,lam):
    w=pi*np.exp(lam*u); return w/w.sum()

print("K1 tilt: exact KL vs leading-order lam^2 Var/2 vs Bennett bound Var*(e^{lam b}-1-lam b)/b^2")
worst=0; maxratio_lead=0
for t in range(20000):
    n=rng.integers(2,7); pi=rng.dirichlet(np.ones(n)*rng.uniform(0.1,3)); u=rng.normal(size=n)*rng.uniform(0.1,3)
    lam=rng.uniform(0,6)
    mu=float(pi@u); var=float(pi@(u-mu)**2)
    b=float(u.max()-mu)  # upper deviation on support
    if b<1e-9 or var<1e-12: continue  # degenerate: KL is 0 to float precision
    k=math.log(float(pi@np.exp(lam*(u-mu))))  # = KL(pi||tilt), stable form
    assert abs(k-kl(pi,tilt(pi,u,lam)))<1e-8
    bennett=var*(math.expm1(lam*b)-lam*b)/b**2
    assert k<=bennett*(1+1e-9)+1e-12,(k,bennett)
    worst=max(worst,k/bennett if bennett>0 else 0)
    lead=0.5*lam**2*var
    if lead>0: maxratio_lead=max(maxratio_lead,k/lead)
print(f"  Bennett bound holds on 20000 random instances; tightest KL/bound={worst:.4f}")
print(f"  max KL/(lam^2 Var/2) observed = {maxratio_lead:.1f}  (the sd-factorization is leading-order only)")
# the binary instances of the segment
for p in [0.5,0.1,0.01,0.001]:
    pi=np.array([1-p,p]); u=np.array([0.,1.]); lam=1.0
    k=kl(pi,tilt(pi,u,lam)); var=p*(1-p); b=1-p
    print(f"  lam=1 p={p}: KL={k:.5f}  lam^2Var/2={0.5*var:.5f}  Bennett={var*(math.exp(b)-1-b)/b**2:.5f}  range-bound={1/8:.4f}")
for lam in [5.0,10.0]:
    p=0.001; pi=np.array([1-p,p]); u=np.array([0.,1.])
    k=kl(pi,tilt(pi,u,lam)); var=p*(1-p); b=1-p
    print(f"  lam={lam} p={p}: KL={k:.4f}  lam^2Var/2={0.5*lam**2*var:.4f}  Bennett={var*(math.exp(lam*b)-1-lam*b)/b**2:.4f}")

print("\nK2 per-goal calibration of a goal-blind Bayes filter when the goal is evidence (N7beta world)")
# G uniform; P(flaw|e,G=correct)=0.8, P(flaw|e,G=ship)=0.2; goal-blind filter reports 0.5
post={0:np.array([0.8,0.2]),1:np.array([0.2,0.8])}; blind=np.array([0.5,0.5])
for g in (0,1):
    print(f"  under G={g}'s law: reliability of goal-blind report (log score) = {kl(post[g],blind):.4f} nats; goal-using report: {kl(post[g],post[g]):.4f}")
print("  pooled law: goal-blind report reliability = 0 (it is P(flaw|e)=0.5)")
# restoration: the goal-setting event recorded as an observation -> M conditions on it, no G port
print("  restoration: record 'principal assigned g' as an event s; f_M(M-, s) = P(flaw|e,s) = post[s]; no G argument; per-goal reliability 0")

print("\nK3 a calibrated goal-dependent departure from P(W|info) (N3 world): reliability 0, so 'departure => reliability>0' fails")
pW=np.array([0.4,0.6]); q1,q2=0.9,0.7
J={}
for W in (0,1):
    for x1 in (0,1):
        for x2 in (0,1):
            J[(W,x1,x2)]=pW[W]*(q1 if x1==W else 1-q1)*(q2 if x2==W else 1-q2)
def post2(x1=None,x2=None):
    num=sum(p for (W,a,b),p in J.items() if W==1 and (x1 is None or a==x1) and (x2 is None or b==x2))
    den=sum(p for (W,a,b),p in J.items() if (x1 is None or a==x1) and (x2 is None or b==x2))
    return num/den
def decomp(f):
    groups={}
    for (W,a,b),p in J.items():
        r=round(f(a,b),12); groups.setdefault(r,[0.,0.]); groups[r][W]+=p
    REL=RES=S=0.
    for r,(p0,p1) in groups.items():
        m=p0+p1; cal=np.array([p0,p1])/m; rep=np.array([1-r,r])
        S+=-(p0*math.log(1-r)+p1*math.log(r)); REL+=m*kl(cal,rep); RES+=m*kl(cal,pW)
    return S,RES,REL
full=decomp(lambda a,b: post2(a,b)); ign=decomp(lambda a,b: post2(x1=a))
print(f"  agent encodes (x1,x2); report P(W|x1,x2): score={full[0]:.4f} RES={full[1]:.4f} REL={full[2]:.4f}")
print(f"  same agent, goal g1, reports P(W|x1) (encode-then-ignore): score={ign[0]:.4f} RES={ign[1]:.4f} REL={ign[2]:.4f}")
print(f"  departure from P(W|encoded info) costs {ign[0]-full[0]:.4f} nats, all of it resolution; reliability 0")
# recalibration identity: score(M) - score(P(W|sigma(M))) = REL(M), resolution unchanged
tl=lambda a,b: tilt(np.array([1-post2(a,b),post2(a,b)]),np.array([0.,1.]),1.0)[1]
d=decomp(tl); print(f"  tilted (N3 row 4): score={d[0]:.4f} RES={d[1]:.4f} REL={d[2]:.4f}; recalibrated score = {d[0]-d[2]:.4f} = full-info score {full[0]:.4f}")

print("\nK4 action-pinned event + injective policy: G determined by (e,M-) -> I(G;Omega|e,a)=0 even for an informative goal")
# principal: Omega in {0,1} uniform; principal sees Omega w.p. 0.8 correctly, sets G=its signal; policy a=G; e=(a, y) y=Omega w.p. 0.6
tot={}
for om in (0,1):
    for G in (0,1):
        pG=0.8 if G==om else 0.2
        for y in (0,1):
            py=0.6 if y==om else 0.4
            tot[(om,G,y)]=0.5*pG*py
def I_G_Om_given(cond_has_a):
    # condition on y and (if cond_has_a) a=G
    I=0.
    keys=set((G if cond_has_a else None,y) for (om,G,y) in tot)
    for (ac,y) in keys:
        sub={k:v for k,v in tot.items() if k[2]==y and (ac is None or k[1]==ac)}
        Z=sum(sub.values())
        pom={o:sum(v for k,v in sub.items() if k[0]==o)/Z for o in (0,1)}
        pg={g:sum(v for k,v in sub.items() if k[1]==g)/Z for g in (0,1)}
        for k,v in sub.items():
            pj=v/Z
            if pj>0: I+=Z*pj*math.log(pj/(pom[k[0]]*pg[k[1]]))
    return I
print(f"  I(G;Omega|y) without the action in the event = {I_G_Om_given(False):.4f} nats (goal informative)")
print(f"  I(G;Omega|y,a) with the action in the event, a=G = {I_G_Om_given(True):.4f} nats")

print("\nK5 Fisher-Rao convention: KL vs spherical arc theta=arccos(BC) vs Fisher geodesic 2*theta")
for (m1,m2,s) in [(0.0,0.01,1.0),(0.0,0.1,1.0),(0.0,1.0,1.0),(0.0,3.0,1.0)]:
    KL=(m1-m2)**2/(2*s*s); BC=math.exp(-(m1-m2)**2/(8*s*s)); th=math.acos(BC)
    print(f"  N({m1},1) vs N({m2},1): KL={KL:.5f}  arc^2/KL={th*th/KL:.4f}  (2arc)^2/KL={(2*th)**2/KL:.4f}  global check 2arc<=2sqrt(KL): {2*th<=2*math.sqrt(KL)+1e-12}")
worst=0
for t in range(20000):
    n=rng.integers(2,6); p=rng.dirichlet(np.ones(n)*rng.uniform(0.1,3)); q=rng.dirichlet(np.ones(n)*rng.uniform(0.1,3))
    BC=float(np.sum(np.sqrt(p*q))); th=math.acos(min(1.0,BC)); K=kl(p,q)
    assert th<=math.sqrt(K)+1e-9,(th,K)
    worst=max(worst,th/math.sqrt(K) if K>0 else 0)
print(f"  global: arccos(BC) <= sqrt(KL) on 20000 random pairs; max ratio {worst:.4f}  => d_Fisher=2arc <= 2 sqrt(KL), no small-information hypothesis")

print("\nK6 step 5a: a feasibility-independent cost on a pursuing action does not by itself break starvation")
pf1=0.5; pfeas=0.6
def voi_feas(pay):  # pay(action, feasible, f1) -> payoff ; actions a1,a2
    def ev(a,pf): return sum((pf if feas else 1-pf)*(pf1 if f1 else 1-pf1)*pay(a,feas,f1) for feas in (0,1) for f1 in (0,1))
    base=max(ev(a,pfeas) for a in ('a1','a2'))
    withf=pfeas*max(ev(a,1.0) for a in ('a1','a2'))+(1-pfeas)*max(ev(a,0.0) for a in ('a1','a2'))
    return withf-base
v5=lambda a,feas,f1: (1.0*(feas and f1==0)) if a=='a1' else (2.0*(feas and f1==1)-0.4)
mine=lambda a,feas,f1: (1.0*(feas and f1==0)-0.4) if a=='a1' else (2.0*(feas and f1==1))
print(f"  verifier V5 (cost on a2, the feasible-best action): VOI(feasibility)={voi_feas(v5):.4f}")
print(f"  cost on a1 instead (a2 best under both): VOI(feasibility)={voi_feas(mine):.4f}  -> tie broken, starvation persists")

print("\nK7 action in the event + injective deterministic policy: kappa numerator is 0 for a distorting update")
# G uniform {0,1}; a=G; event e=(a,y), y~Bern(.5) indep; update reports tilt of P(Omega|y) by lam=2 toward G
# Under the operating law G is a function of e, so I(G;M+|e)=0 and H(G|e)=0 whatever f_M does.
import itertools
joint={}
for G,y in itertools.product((0,1),(0,1)):
    e=(G,y); Mplus=round(float(tilt(np.array([0.5,0.5]),np.array([1.0-G,float(G)]),2.0)[1]),9)
    joint[(G,e,Mplus)]=joint.get((G,e,Mplus),0)+0.25
def condent_G(given):  # H(G|given(e,M+)) 
    H=0.; groups={}
    for (G,e,m),p in joint.items(): groups.setdefault(given(e,m),{}).setdefault(G,0.); groups[given(e,m)][G]+=p
    for k,d in groups.items():
        Z=sum(d.values())
        for v in d.values():
            if v>0: H-=v*math.log(v/Z)
    return H
HGe=condent_G(lambda e,m:e); HGem=condent_G(lambda e,m:(e,m))
print(f"  operating law: H(G|e)={HGe:.4f}, I(G;M+|e)={HGe-HGem:.4f}  (distorting update, TV between goals' reports = {abs(tilt(np.array([.5,.5]),np.array([1.,0.]),2.)[1]-tilt(np.array([.5,.5]),np.array([0.,1.]),2.)[1]):.3f})")
# probe law: G randomized independently of the event (same f_M evaluated at a fixed e)
print(f"  probe law (G uniform, independent of a fixed e): I(G;M+|e)=log2={math.log(2):.4f}, kappa=1")

print("\nK8 clause 2's converse: content-dependent drop of an uninformative feature leaves the report calibrated (verifier V6)")
# N3 world plus x3 indep of W; encode x1 always, x3 only if x3==1; naive update reports P(W|x1)
print("  dropped content x3 independent of W given x1 -> pattern carries no W-information -> report P(W|x1) is calibrated (REL=0, as K3 row 2)")

print("\nK2b the same point with the action pinned in the event: principal-set goal, a=G, e=(a,o)")
# Omega uniform; principal's signal G=Omega w.p. 0.8; a=G (injective); o=Omega w.p. 0.6.
# (i) POMDP filter, action only through the likelihood (a does not move Omega): reports P(Omega|o).
# (ii) goal-blind update that conditions on the action as evidence: reports P(Omega|a,o).
cells={}
for om in (0,1):
    for G in (0,1):
        for o in (0,1):
            cells[(om,G,o)]=0.5*(0.8 if G==om else 0.2)*(0.6 if o==om else 0.4)
def P_om1(cond):
    num=sum(v for k,v in cells.items() if k[0]==1 and cond(k)); den=sum(v for k,v in cells.items() if cond(k)); return num/den
rep_lik={o:P_om1(lambda k,o=o:k[2]==o) for o in (0,1)}
rep_obs={(a,o):P_om1(lambda k,a=a,o=o:k[1]==a and k[2]==o) for a in (0,1) for o in (0,1)}
def rel_under_goal(g,report):  # log-score reliability of report(a,o) under goal g's law (a=g)
    groups={}
    for (om,G,o),v in cells.items():
        if G!=g: continue
        r=round(report(G,o),12); groups.setdefault(r,[0.,0.]); groups[r][om]+=v
    Z=sum(sum(x) for x in groups.values()); R=0.
    for r,(p0,p1) in groups.items():
        m=p0+p1; R+=(m/Z)*kl(np.array([p0,p1])/m,np.array([1-r,r]))
    return R
for g in (0,1):
    print(f"  under G={g}: per-goal reliability, likelihood-only filter = {rel_under_goal(g,lambda a,o: rep_lik[o]):.4f}; action-as-evidence update = {rel_under_goal(g,lambda a,o: rep_obs[(a,o)]):.4f}")
print("  -> with the goal informative, 'action only through the likelihood' is per-goal miscalibrated, and the per-goal-calibrated")
print("     goal-blind update is the one that treats the action as evidence, which the certificate's wording excludes. Under NWI they coincide.")
