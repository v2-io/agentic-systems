# within-mind retest agreement: observed vs model-predicted from OTHER minds' answers only (tests the model's
# assumption of no mind x item interaction). Also restricted to items in the graded middle.
import sys, numpy as np, collections
SP="/Users/josephwecker-v2/src/arch/asf/empirica/glyph-sequence-perception/spikes/family-disagreement-2026-10-06"
sys.path.insert(0, SP)
import irt
name=sys.argv[1] if len(sys.argv)>1 else "continue-stop"; var=sys.argv[2] if len(sys.argv)>2 else "2mf"
items, seq, S, N, X = irt.load(name, one_per_sheet="--one-per-sheet" in sys.argv)
m=irt.Model(int(var[0]),"m" in var,"f" in var).fit(S,N,X)
M=irt.MINDS
print(f"== {name} {var}")
for j,mm in enumerate(M):
    So,No=S.copy(),N.copy(); So[:,j]=0; No[:,j]=0
    L=m.comp_loglik(So,No,X); R=np.exp(L-np.logaddexp.reduce(L,axis=1)[:,None])
    Lf=m.comp_loglik(S,N,X); Rf=np.exp(Lf-np.logaddexp.reduce(Lf,axis=1)[:,None])
    rows=[]
    for i in np.where(N[:,j]>=2)[0]:
        ys=[y for _,y in sorted(seq[items[i]][mm], key=lambda t:t[0])]
        p=m.comp_probs(X[i])[:,j]; r=R[i]
        pred=r@(p**2+(1-p)**2); obs=ys[0]==ys[1]
        # 'middle' items by the full posterior: M-class mass > .8 and other-mind info present
        mid = Rf[i,2:].sum()>0.8
        rows.append((obs,pred,mid, No[i].sum()>0))
    if len(rows)<30: continue
    a=np.array(rows,dtype=float)
    def s(mask):
        if mask.sum()<10: return "-"
        o=a[mask,0].mean(); p=a[mask,1].mean(); n=mask.sum()
        return f"obs {o:.3f} pred {p:.3f} (disagree obs/pred {(1-o)/(1-p):.2f}, n={int(n)})"
    allm=np.ones(len(a),bool)
    print(f"{mm:14s} all: {s(allm)} | other-mind answers present: {s(a[:,3]>0)} | graded middle: {s((a[:,2]>0)&(a[:,3]>0))}")
