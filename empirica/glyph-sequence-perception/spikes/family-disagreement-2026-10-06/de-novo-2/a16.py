# MI between one more answer of a mind and the item's SHARED latent state (class, b), under the tau model: the
# mind's own u is integrated out given its own earlier answers. Flat Sonnet/Grok items vs all both-answered items.
import sys, json, numpy as np
sys.path.insert(0, ".")
import irtu, irt
items, seq, S, N, X = irt.load("continue-stop")
P=json.load(open("tau-pred.json"))["params"]; m=irtu.ModelU()
for k in ("alpha","slope","gamma","tau","pi","eps","dlt"): setattr(m,k,np.array(P[k]))
G,U=irtu.G,irtu.U; M=irt.MINDS
L,Qs=m.comp_loglik(S,N,X,keepQ=True); R=np.exp(L-np.logaddexp.reduce(L,axis=1)[:,None])
Q=np.zeros((len(items),len(G),len(U),len(M)),dtype=np.float32)
for (x,c0),(ii,q) in Qs.items(): Q[ii]=q
H=lambda p: -(p*np.log(np.clip(p,1e-12,1))+(1-p)*np.log(np.clip(1-p,1e-12,1)))
def mi(i,j):
    x=X[i]; z=m.alpha[j]+m.slope[j]*G[:,None]+m.gamma[j]*x+m.tau[j]*U[None,:]; p=1/(1+np.exp(-z))
    Pc=np.concatenate([[m.eps[x][j]],[1-m.dlt[x][j]],(Q[i,:,:,j]*p).sum(1)]); r=R[i]
    return H(r@Pc)-r@H(Pc)
a,b=M.index("sonnet55"),M.index("grok46")
allb=[i for i in range(len(items)) if N[i,a]>0 and N[i,b]>0]
flat=[i for i in allb if N[i,a]>=2 and N[i,b]>=2 and S[i,a]==0 and S[i,b]==N[i,b]]
for nm,ix in (("flat",flat),("all both-answered",allb)):
    print(f"{nm:18s} n={len(ix):5d}  MI nats (tau model): Grok {np.mean([mi(i,b) for i in ix]):.4f}  Sonnet {np.mean([mi(i,a) for i in ix]):.4f}  best mind {np.mean([max(mi(i,j) for j in range(len(M))) for i in ix]):.4f}")
