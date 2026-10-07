# calibration with mind parameters fitted on OTHER items (5-fold), vs in-sample
import sys, numpy as np, collections
SP="/Users/josephwecker-v2/src/arch/asf/empirica/glyph-sequence-perception/spikes/family-disagreement-2026-10-06"
sys.path.insert(0, SP)
import irt
name=sys.argv[1] if len(sys.argv)>1 else "continue-stop"
var=sys.argv[2] if len(sys.argv)>2 else "2mf"
ops="--one-per-sheet" in sys.argv
items, seq, S, N, X = irt.load(name, one_per_sheet=ops)
pl,mix,fam=int(var[0]),"m" in var,"f" in var
I=len(items); f=np.random.default_rng(1).integers(0,5,I)
agg=collections.defaultdict(lambda: np.zeros(4)); 
for k in range(5):
    tr,te=f!=k,f==k
    m=irt.Model(pl,mix,fam).fit(S[tr],N[tr],X[tr])
    idx=np.where(te)[0]
    sub_items=[items[i] for i in idx]
    res=irt.pair_checks(m, sub_items, seq, S[idx], N[idx], X[idx], irt.PAIRS, sims=1)
    for r in res:
        a=agg[(r["A"],r["B"])]; a+= [r["obs"]*r["n"], r["pred"]*r["n"], r["o1"]+0, r["e1"]]
        agg[(r["A"],r["B"],"o2")] += [r["o2"], r["e2"],0,0]
mfull=irt.Model(pl,mix,fam).fit(S,N,X)
full={ (r["A"],r["B"]):r for r in irt.pair_checks(mfull, items, seq, S, N, X, irt.PAIRS, sims=1)}
print(f"== {name} {var} one_per_sheet={ops}")
for (A,B),r in full.items():
    a=agg[(A,B)]; b=agg[(A,B,"o2")]
    print(f"{A:14s}{B:14s} in-sample ratio {r['ratio']:.2f} | held-out-params ratio {a[0]/a[1]:.2f} | flat A0B1 obs {int(a[2])} pred in {r['e1']:.1f} held-out {a[3]:.1f} | A1B0 obs {int(b[0])} pred in {r['e2']:.1f} held-out {b[1]:.1f}")
