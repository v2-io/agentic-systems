# Mutual information between one more answer of a mind and the item's latent state (class, b), under 2mf,
# flat Sonnet-continues/Grok-stops items vs all items both answered -- against flatread.py's variance-of-b measure.
import sys, numpy as np
SP="/Users/josephwecker-v2/src/arch/asf/empirica/glyph-sequence-perception/spikes/family-disagreement-2026-10-06"
sys.path.insert(0, SP)
import irt
items, seq, S, N, X = irt.load("continue-stop")
m=irt.Model(2,True,True).fit(S,N,X); M=irt.MINDS
L=m.comp_loglik(S,N,X); R=np.exp(L-np.logaddexp.reduce(L,axis=1)[:,None])
H=lambda p: -(p*np.log(np.clip(p,1e-12,1))+(1-p)*np.log(np.clip(1-p,1e-12,1)))
def mi(i,j):
    P=m.comp_probs(X[i])[:,j]; r=R[i]; return H(r@P)-r@H(P)
a,b=M.index("sonnet55"),M.index("grok46")
allb=[i for i in range(len(items)) if N[i,a]>0 and N[i,b]>0]
flat=[i for i in allb if N[i,a]>=2 and N[i,b]>=2 and S[i,a]==0 and S[i,b]==N[i,b]]
for nm,ix in (("flat",flat),("all both-answered",allb)):
    g=np.mean([mi(i,b) for i in ix]); s=np.mean([mi(i,a) for i in ix]); best=np.mean([max(mi(i,j) for j in range(len(M))) for i in ix])
    print(f"{nm:18s} n={len(ix):5d}  MI nats: Grok {g:.4f}  Sonnet {s:.4f}  best mind {best:.4f}")
