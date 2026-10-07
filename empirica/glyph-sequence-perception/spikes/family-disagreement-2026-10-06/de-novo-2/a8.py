# A competing prediction for p001, written before looking at p001's answers.
# Each mind's own propensity on an item ~ Beta(mean m, concentration kappa), m = the 2mf model's prediction for that
# mind from the OTHER minds' answers; kappa fitted per mind to that mind's observed retest disagreement (first two
# answers, different rounds). Then for a flat item: P(next answer repeats) = (m*kappa + 2)/(kappa + 2) for the mind's 2/2.
import sys, numpy as np, json
def brentq(f,lo,hi):
    import math
    a,b=math.log(lo),math.log(hi)
    for _ in range(200):
        c=(a+b)/2
        if f(math.exp(c))>0: b=c
        else: a=c
    return math.exp((a+b)/2)
SP="/Users/josephwecker-v2/src/arch/asf/empirica/glyph-sequence-perception/spikes/family-disagreement-2026-10-06"
sys.path.insert(0, SP)
import irt
items, seq, S, N, X = irt.load("continue-stop")
m=irt.Model(2,True,True).fit(S,N,X); M=irt.MINDS
def others_pred(j, idx=None):
    So,No=S.copy(),N.copy(); So[:,j]=0; No[:,j]=0
    L=m.comp_loglik(So,No,X); R=np.exp(L-np.logaddexp.reduce(L,axis=1)[:,None])
    return np.array([R[i]@m.comp_probs(X[i])[:,j] for i in range(len(items))])
kap={}; mo={}
for mm in ("sonnet55","grok46","haiku45nt"):
    j=M.index(mm); mu=others_pred(j); mo[mm]=mu
    rows=[]
    for i in np.where(N[:,j]>=2)[0]:
        L2=sorted(seq[items[i]][mm], key=lambda t:t[0])
        if L2[0][0]==L2[1][0]: continue
        rows.append((L2[0][1]!=L2[1][1], mu[i]))
    a=np.array(rows,float); obs=a[:,0].sum()
    f=lambda k: (2*a[:,1]*(1-a[:,1])*k/(k+1)).sum()-obs
    k=brentq(f,0.01,1e6) if f(1e6)>0 else np.inf
    kap[mm]=k; print(mm, "kappa", round(k,2), "obs disagreements", int(obs), "of", len(a), "| at kappa=inf (no extra consistency):", round(f(1e9)+obs,1))
a,b=M.index("sonnet55"),M.index("grok46")
flat=[i for i in range(len(items)) if N[i,a]>=2 and N[i,b]>=2 and S[i,a]==0 and S[i,b]==N[i,b]]
pg=np.array([(mo["grok46"][i]*kap["grok46"]+N[i,b])/(kap["grok46"]+N[i,b]) for i in flat])
ps=np.array([1-(mo["sonnet55"][i]*kap["sonnet55"]+0)/(kap["sonnet55"]+N[i,a]) for i in flat])
rng=np.random.default_rng(0)
print("Grok stops again: mean", pg.mean().round(3), "band", np.percentile((rng.random((20000,len(pg)))<pg).mean(1),[2.5,50,97.5]))
print("Sonnet continues again: mean", ps.mean().round(3), "band", np.percentile((rng.random((20000,len(ps)))<ps).mean(1),[2.5,50,97.5]))
print("Grok m from others (mean)", mo["grok46"][flat].mean().round(3), " Sonnet stop m from others", mo["sonnet55"][flat].mean().round(3))
json.dump({"grok_p":pg.tolist(),"sonnet_p":ps.tolist(),"ctx":["".join(items[i][1]) for i in flat],"kappa":kap}, open("alt-pred.json","w"), ensure_ascii=False)
