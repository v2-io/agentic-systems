# Check of spikes/temporal-nesting-rg/01-rg-0a §2.7: does the optimal symmetric
# macro-update's closure defect go to 0 as K_c grows (heterogeneous steady-state Kalman pair)?
import numpy as np
rng=np.random.default_rng(0)
def kss(q,r):
    P=(-q+np.sqrt(q*q+4*q*r))/2; return (P+q)/(P+q+r)
q=np.array([1.0,1.0]); r=np.array([0.2,5.0])   # different SNRs -> K1 != K2
K=kss(q,r); lam=1-K
print("K*",K)
T=400000
w=rng.normal(size=(T,2))*np.sqrt(q); om=np.cumsum(w,0)
o=om+rng.normal(size=(T,2))*np.sqrt(r)
est=np.zeros((T,2)); 
for t in range(1,T): est[t]=lam*est[t-1]+K*o[t]
Xc=(est[:,0]+est[:,1])/np.sqrt(2); Oc=(o[:,0]+o[:,1])/np.sqrt(2)
for Kc in [1,2,4,8,16,32,64]:
    ms=np.arange(Kc+100, T, Kc)
    A=np.column_stack([Xc[ms-Kc]]+[Oc[ms-k] for k in range(Kc)])
    y=Xc[ms]
    coef,*_=np.linalg.lstsq(A,y,rcond=None)
    res=y-A@coef
    print(f"K_c={Kc:3d}  eps*^2 ~ {np.mean(res**2):.4f}   tilde-lambda^2={((lam[0]**Kc-lam[1]**Kc)/2)**2:.2e}")
