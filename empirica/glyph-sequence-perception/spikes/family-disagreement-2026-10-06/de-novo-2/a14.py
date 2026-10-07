# Checks of the tau model (2mf + mind x item intercept) on the snapshot: cross-mind single-answer calibration,
# within-mind retest calibration, flat-split counts -- the same checks irt.py and a6/a7 run on 2mf.
import sys, json, numpy as np
sys.path.insert(0, ".")
import irtu, irt
items, seq, S, N, X = irt.load("continue-stop")
P=json.load(open("tau-pred.json"))["params"]
m=irtu.ModelU()
for k in ("alpha","slope","gamma","tau","pi","eps","dlt"): setattr(m,k,np.array(P[k]))
G,U,W=irtu.G,irtu.U,irtu.W; M=irt.MINDS
def pm(x,j,kind):
    """(2+G,) per component: kind 'p' P(1); 'agree' P(two answers agree); ('all',n,y) P(n answers all = y)"""
    z=m.alpha[j]+m.slope[j]*G[:,None]+m.gamma[j]*x+m.tau[j]*U[None,:]; p=1/(1+np.exp(-z))
    e,d=m.eps[x][j],1-m.dlt[x][j]
    if kind=="p": f=lambda q:q
    elif kind=="agree": f=lambda q:q**2+(1-q)**2
    else: _,n,y=kind; f=(lambda q:q**n) if y==1 else (lambda q:(1-q)**n)
    return np.concatenate([[f(e)],[f(d)],(f(p)*W[None,:]).sum(1)])
def post(excl):
    So,No=S.copy(),N.copy(); So[:,excl]=0; No[:,excl]=0
    L=m.comp_loglik(So,No,X); return np.exp(L-np.logaddexp.reduce(L,axis=1)[:,None])
print("cross-mind single-answer disagreement, obs/pred:")
for A,B in irt.PAIRS:
    a,b=M.index(A),M.index(B); R=post([a,b]); od=pd=0; o1=e1=0
    for i in np.where((N[:,a]>0)&(N[:,b]>0))[0]:
        ya=[y for _,y in sorted(seq[items[i]][A])]; yb=[y for _,y in sorted(seq[items[i]][B])]
        pa,pb=pm(X[i],a,"p"),pm(X[i],b,"p"); od+=ya[0]!=yb[0]; pd+=R[i]@(pa*(1-pb)+pb*(1-pa))
        if len(ya)>=2 and len(yb)>=2:
            o1+=(not any(ya)) and all(yb); e1+=R[i]@(pm(X[i],a,("all",len(ya),0))*pm(X[i],b,("all",len(yb),1)))
    print(f"   {A:14s}{B:14s} ratio {od/pd:.2f} | flat A0/B1 obs {o1} pred {e1:.1f}")
print("within-mind retest (first two answers, different rounds), disagreements obs/pred:")
for mm in ("sonnet55","grok46","haiku45nt","haiku45","opus55"):
    j=M.index(mm); R=post([j]); o=p=n=0
    for i in np.where(N[:,j]>=2)[0]:
        L2=sorted(seq[items[i]][mm])
        if L2[0][0]==L2[1][0]: continue
        o+=L2[0][1]!=L2[1][1]; p+=1-R[i]@pm(X[i],j,"agree"); n+=1
    print(f"   {mm:14s} n={n} obs {o} pred {p:.1f}")
