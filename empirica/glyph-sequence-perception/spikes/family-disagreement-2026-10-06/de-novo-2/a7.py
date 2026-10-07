import sys, numpy as np
SP="/Users/josephwecker-v2/src/arch/asf/empirica/glyph-sequence-perception/spikes/family-disagreement-2026-10-06"
sys.path.insert(0, SP)
import irt
items, seq, S, N, X = irt.load("continue-stop")
m=irt.Model(2,True,True).fit(S,N,X); M=irt.MINDS
for mm in ("sonnet55","grok46","haiku45nt"):
    j=M.index(mm); So,No=S.copy(),N.copy(); So[:,j]=0; No[:,j]=0
    L=m.comp_loglik(So,No,X); R=np.exp(L-np.logaddexp.reduce(L,axis=1)[:,None])
    rows=[]
    for i in np.where(N[:,j]>=2)[0]:
        L2=sorted(seq[items[i]][mm], key=lambda t:t[0])
        if L2[0][0]==L2[1][0]: continue        # same round: skip
        p=m.comp_probs(X[i])[:,j]; r=R[i]
        rows.append((L2[0][1]==L2[1][1], r@(p**2+(1-p)**2), r@p))
    a=np.array(rows,float)
    print(mm, f"different rounds only: n={len(a)} obs agree {a[:,0].mean():.3f} pred {a[:,1].mean():.3f} ratio(dis) {(1-a[:,0].mean())/(1-a[:,1].mean()):.2f}")
    for lo,hi in ((0,.2),(.2,.4),(.4,.6),(.6,.8),(.8,1.01)):
        k=(a[:,2]>=lo)&(a[:,2]<hi)
        if k.sum()>=10:
            print(f"    predicted P(stop) {lo:.1f}-{hi:.1f}: n={int(k.sum()):4d} disagree obs {1-a[k,0].mean():.3f} pred {1-a[k,1].mean():.3f}")
