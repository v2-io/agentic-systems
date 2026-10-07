# 5-fold held-out log-likelihood per answer, same folds as irt.heldout (seed 0): 2mf vs 2mf + mind x item intercept
import sys, numpy as np
sys.path.insert(0, ".")
import irtu, irt
items, seq, S, N, X = irt.load("continue-stop")
I=S.shape[0]; f=np.random.default_rng(0).integers(0,5,I)
t0=t1=n=0.0
for k in range(5):
    tr,te=f!=k,f==k
    m0=irt.Model(2,True,True).fit(S[tr],N[tr],X[tr]); m1=irtu.ModelU().fit(S[tr],N[tr],X[tr])
    a=np.logaddexp.reduce(m0.comp_loglik(S[te],N[te],X[te]),axis=1).sum(); b=np.logaddexp.reduce(m1.comp_loglik(S[te],N[te],X[te]),axis=1).sum()
    t0+=a; t1+=b; n+=N[te].sum(); print(f"fold {k}: 2mf {a:.1f} tau {b:.1f} diff {b-a:+.1f}", flush=True)
print(f"held-out per answer: 2mf {t0/n:.4f}  tau {t1/n:.4f}  total diff {t1-t0:+.1f} nats over {int(n)} answers")
