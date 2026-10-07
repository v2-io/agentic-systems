import sys, numpy as np, json, time
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import irtu, irt
items, seq, S, N, X = irt.load("continue-stop")
t=time.time(); m=irtu.ModelU().fit(S,N,X); print("fit", round(time.time()-t), "s, iters", m.iters, "ll", round(m.ll,1))
m0=irt.Model(2,True,True).fit(S,N,X); print("2mf ll", round(m0.ll,1))
for j,mm in enumerate(irt.MINDS): print(f"  {mm:14s} alpha {m.alpha[j]:+.2f} slope {m.slope[j]:.2f} gamma {m.gamma[j]:+.2f} tau {m.tau[j]:.2f}")
print("pi", m.pi.round(3))
M=irt.MINDS; a,b=M.index("sonnet55"),M.index("grok46")
flat=[i for i in range(len(items)) if N[i,a]>=2 and N[i,b]>=2 and S[i,a]==0 and S[i,b]==N[i,b]]
pg=np.array([m.predict_next(S[i],N[i],X[i],b) for i in flat]); ps=np.array([1-m.predict_next(S[i],N[i],X[i],a) for i in flat])
rng=np.random.default_rng(0)
print("tau model: Grok stops again mean", pg.mean().round(3), np.percentile((rng.random((20000,len(pg)))<pg).mean(1),[2.5,50,97.5]))
print("tau model: Sonnet continues again mean", ps.mean().round(3), np.percentile((rng.random((20000,len(ps)))<ps).mean(1),[2.5,50,97.5]))
json.dump({"ctx":["".join(items[i][1]) for i in flat],"grok_p":pg.tolist(),"sonnet_p":ps.tolist(),
           "params":{k:(v.tolist() if hasattr(v,"tolist") else v) for k,v in m.__dict__.items() if k in ("alpha","slope","gamma","tau","pi","eps","dlt")}},
          open("tau-pred.json","w"), ensure_ascii=False, indent=0)
