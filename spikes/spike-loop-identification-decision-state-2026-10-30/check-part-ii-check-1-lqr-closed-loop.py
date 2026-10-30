# KR C.2 / C.1 -- independent check of the Part II integration (identification side), reviews/part-ii-check-1-identification.md, 2026-10-30. Run: python3 -I <this file>
"""Is Kalman + LQR closed-loop data uninformative about untaken actions *within the linear-Gaussian class*?
Scalar plant x' = a x + b u + w, y = x + v; steady-state Kalman filter + LQR, u = -k xhat (deterministic in xhat).
(i) Full-state feedback (v = 0, xhat = x): only a - b k is identified -- any (a', b') with a' - b' k = a - b k fits.
(ii) With measurement noise the regulator is dynamic in y; fit ARMAX(1,1,1) y_{t+1} = A y_t + B u_t + e_{t+1} + C e_t
by prediction-error minimization on the closed-loop data and see whether (A, B) -> (a, b)."""
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(3)
a, b, sw, sv, q, r = 0.9, 0.5, 1.0, 1.0, 1.0, 0.1
# LQR gain (scalar DARE)
P = 1.0
for _ in range(2000): P = q + a*a*P - (a*b*P)**2/(r + b*b*P)
k = a*b*P/(r + b*b*P)
# steady-state Kalman (predictor) covariance and filter gain
S = 1.0
for _ in range(2000): S = a*a*S - (a*S)**2/(S + sv*sv) + sw*sw
L = S/(S + sv*sv)
T = 200000
x = 0.0; xpred = 0.0; ys = np.empty(T); us = np.empty(T)
for t in range(T):
    y = x + sv*rng.standard_normal()
    xhat = xpred + L*(y - xpred)          # filtered estimate
    u = -k*xhat                           # deterministic in the decision state xhat
    ys[t], us[t] = y, u
    x = a*x + b*u + sw*rng.standard_normal()
    xpred = a*xhat + b*u
print(f"true a={a}, b={b}; LQR k={k:.4f}, Kalman L={L:.4f}; corr(u_t, y_t)={np.corrcoef(us, ys)[0,1]:.4f}")
def pe(theta):
    A, B, C = theta
    e = np.zeros(T); 
    for t in range(1, T):
        e[t] = ys[t] - A*ys[t-1] - B*us[t-1] - C*e[t-1]
    return np.mean(e[100:]**2)
# coarse vectorized-ish: use scipy on a subsample for speed
ys_full, us_full = ys, us
ys, us = ys_full[:40000], us_full[:40000]; T = len(ys)
for start in ([0.5, 0.0, 0.0], [0.2, 1.5, 0.3], [1.2, 1.2, -0.3]):
    res = minimize(pe, start, method="Nelder-Mead", options={"xatol":1e-4, "fatol":1e-8, "maxiter":4000})
    print("start", start, "-> A=%.3f B=%.3f C=%.3f  mse=%.5f" % (*res.x, res.fun))
# compare: the (a', b') with a'-b'k = a-bk that full-state data could not distinguish
for bb in (0.0, 0.5, 1.0):
    aa = a - b*k + bb*k
    print(f"alt (a',b')=({aa:.3f},{bb}) with a'-b'k fixed: PE mse = {pe([aa, bb, res.x[2]]):.5f}")
from scipy.optimize import minimize_scalar
print("--- profile over B (A, C optimized) ---")
for Bfix in (0.0, 0.25, 0.5, 0.75, 1.0, 1.5):
    r2 = minimize(lambda th: pe([th[0], Bfix, th[1]]), [0.5, 0.0], method="Nelder-Mead", options={"xatol":1e-5,"fatol":1e-10,"maxiter":4000})
    print(f"B={Bfix}: best A={r2.x[0]:.3f} C={r2.x[1]:.3f} mse={r2.fun:.6f}")
