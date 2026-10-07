import sys, json, numpy as np, pickle
SP="/Users/josephwecker-v2/src/arch/asf/empirica/glyph-sequence-perception/spikes/family-disagreement-2026-10-06"
sys.path.insert(0, SP)
import irt
items, seq, S, N, X = irt.load("continue-stop")
m = irt.Model(2, True, True).fit(S, N, X)
seqd={k:dict(v) for k,v in seq.items()}; pickle.dump((items, seqd, S, N, X, m.__dict__), open("fit2mf.pkl","wb"))
M=irt.MINDS; a=M.index("sonnet55"); b=M.index("grok46")
L=m.comp_loglik(S,N,X); R=np.exp(L-np.logaddexp.reduce(L,axis=1)[:,None])
flat=[i for i in range(len(items)) if N[i,a]>=2 and N[i,b]>=2 and S[i,a]==0 and S[i,b]==N[i,b]]
pre=json.load(open(SP+"/prereg-flat-splits.json"))
pc={tuple(c["context_glyphs"]):c for c in pre["contexts"]}
print(len(flat), len(pc))
diffs=[]; pg=[]; ps=[]
for i in flat:
    ctx=items[i][1]
    P=m.comp_probs(X[i]); p=R[i]@P
    c=pc.get(ctx)
    if c is None: print("missing", ctx); continue
    diffs.append(abs(p[b]-c["p_stop_next"]["grok46"])+abs(p[a]-c["p_stop_next"]["sonnet55"]))
    pg.append(p[b]); ps.append(1-p[a])
print("max abs diff vs prereg:", max(diffs))
pg=np.array(pg); ps=np.array(ps)
print("mean grok stop", pg.mean(), "mean sonnet continue", ps.mean())
# pure Bernoulli band
rng=np.random.default_rng(0)
sims=(rng.random((20000,len(pg)))<pg).mean(1); print("grok binomial-only band", np.percentile(sims,[2.5,50,97.5]))
sims=(rng.random((20000,len(ps)))<ps).mean(1); print("sonnet band", np.percentile(sims,[2.5,50,97.5]))
print("grok p range", np.round(np.sort(pg),2))
print("class mass of flat items", R[flat][:,:2].mean(0), R[flat][:,2:].sum(1).mean())
