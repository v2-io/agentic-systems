import numpy as np
from scipy import linalg
exec(open('part-i-exit-time.py').read().split('print("=== (1)')[0])  # reuse helpers only
A = np.array([[1.0, 1.2], [0.0, 1.0]])
S = linalg.solve_continuous_lyapunov(A, np.eye(2)); Vmin = 1/(2*np.linalg.eigvalsh(S).max())
inv, lt = [], []
for sig in [0.5, 0.44, 0.39, 0.35]:
    t = mc_exit(lambda x: x @ A.T, sig, 1.0, 2, 800, 5e-4)
    m = np.nanmean(t); inv.append(1/sig**2); lt.append(np.log(m))
    print(f"sigma={sig}: kappa=V/sigma^2={Vmin/sig**2:.2f}  E[tau]={m:.2f} (se {np.nanstd(t)/np.sqrt(800):.2f})", flush=True)
for i in range(len(inv)-1):
    print(f"local slope {i}->{i+1}: {(lt[i+1]-lt[i])/(inv[i+1]-inv[i]):.3f}")
print(f"overall slope {np.polyfit(inv, lt, 1)[0]:.3f}; V_min {Vmin:.3f}; sector bound 0.400")
# 1-D reference: local log-slope of exact alpha*E[tau] vs kappa at matching kappa
