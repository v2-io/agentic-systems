"""Exit-time check for the Part I containment dichotomy (explorer follow-up, 2026-10-30).

(1) 1-D gradient drift: exact mean exit time from (-R, R) starting at 0 by quadrature,
    vs the Kramers asymptotic, vs Euler-Maruyama Monte Carlo.
(2) Sector-F lower bound on the Freidlin-Wentzell barrier: for linear A with
    alpha_s = lambda_min(sym A) > 0, compare min_{|x|=R} V(x) with alpha_s R^2,
    V(x) = (sigma^2/2) x^T Sigma^{-1} x, A Sigma + Sigma A^T = sigma^2 I.
(3) Monte Carlo slope check of log E[tau] vs 1/sigma^2 for a non-normal 2-D A.
"""
import numpy as np
from scipy import integrate, linalg

rng = np.random.default_rng(20261030)


def exact_T0(U, sigma, R):
    """E[tau] from 0 for dX = -U'(X) dt + sigma dW on (-R, R), U even."""
    inner = lambda y: integrate.quad(lambda z: np.exp(-2 * U(z) / sigma**2), 0, y)[0]
    return (2 / sigma**2) * integrate.quad(lambda y: np.exp(2 * U(y) / sigma**2) * inner(y), 0, R, limit=200)[0]


def kramers_linear(alpha, sigma, R):
    k = alpha * R**2 / sigma**2
    return (np.sqrt(np.pi) / 2) * k**-0.5 * np.exp(k) / alpha


def mc_exit(drift, sigma, R, n_dim, n_paths, dt, max_steps=5_000_000):
    """Euler-Maruyama first exit of the ball |x| > R, start at 0; returns times (s)."""
    x = np.zeros((n_paths, n_dim))
    t_exit = np.full(n_paths, np.nan)
    alive = np.arange(n_paths)
    sq = sigma * np.sqrt(dt)
    for step in range(1, max_steps + 1):
        xa = x[alive]
        xa = xa - drift(xa) * dt + sq * rng.standard_normal(xa.shape)
        x[alive] = xa
        out = np.einsum('ij,ij->i', xa, xa) > R**2
        if out.any():
            t_exit[alive[out]] = step * dt
            alive = alive[~out]
            if alive.size == 0:
                break
    return t_exit


print("=== (1) 1-D linear OU, sigma=1, R=1 (kappa = alpha R^2/sigma^2 = alpha) ===")
print(f"{'alpha':>6} {'exact E[tau]':>13} {'alpha*E':>9} {'Kramers':>10} {'ratio':>7} {'MC mean':>9} {'MC se':>7}")
R, sigma = 1.0, 1.0
for alpha in [0.5, 1, 2, 3, 4, 6]:
    ex = exact_T0(lambda y: alpha * y**2 / 2, sigma, R)
    kr = kramers_linear(alpha, sigma, R)
    mc = ""
    if alpha <= 4:
        t = mc_exit(lambda x: alpha * x, sigma, R, 1, 2000, 1e-4)
        mc = f"{np.nanmean(t):9.3f} {np.nanstd(t)/np.sqrt(np.sum(~np.isnan(t))):7.3f}"
    print(f"{alpha:6.1f} {ex:13.4f} {alpha*ex:9.3f} {kr:10.4f} {ex/kr:7.3f} {mc}")

print("\n--- dt sensitivity at alpha=2 (discrete monitoring overestimates tau) ---")
for dt in [1e-3, 1e-4, 2e-5]:
    t = mc_exit(lambda x: 2 * x, sigma, R, 1, 2000, dt)
    print(f"dt={dt:g}: MC mean {np.nanmean(t):.3f} +- {np.nanstd(t)/np.sqrt(2000):.3f}   exact {exact_T0(lambda y: y**2, 1, 1):.3f}")

print("\n--- 1-D nonlinear sector F(x) = alpha x + beta x^3 (gradient; barrier 2U(R) = alpha R^2 + beta R^4/2) ---")
for alpha, beta in [(1, 2), (2, 2)]:
    ex = exact_T0(lambda y: alpha * y**2 / 2 + beta * y**4 / 4, 1, 1)
    print(f"alpha={alpha} beta={beta}: exact E[tau] {ex:.3f}; linear-alpha E[tau] {exact_T0(lambda y: alpha*y**2/2, 1, 1):.3f}  (sector floor only bounds from below)")

print("\n=== (2) barrier vs sector bound, linear A, random 2-D/3-D draws ===")
worst = np.inf
for trial in range(20000):
    n = rng.choice([2, 3])
    A = rng.normal(size=(n, n))
    a_s = np.linalg.eigvalsh((A + A.T) / 2).min()
    if a_s <= 1e-3:
        A = A + (1e-3 - a_s + rng.uniform(0, 1)) * np.eye(n)
        a_s = np.linalg.eigvalsh((A + A.T) / 2).min()
    S = linalg.solve_continuous_lyapunov(A, np.eye(n))  # A S + S A^T = I  (sigma = 1)
    Vmin = 1.0 / (2 * np.linalg.eigvalsh(S).max())       # (1/2) R^2 lambda_min(S^{-1}), R = 1
    worst = min(worst, Vmin / a_s)
print(f"min over 20000 draws of (barrier / (alpha_sector R^2)) = {worst:.4f}   (claim: >= 1)")
A = np.array([[1.0, 1.2], [0.0, 1.0]])
a_s = np.linalg.eigvalsh((A + A.T) / 2).min()
S = linalg.solve_continuous_lyapunov(A, np.eye(2))
Vmin = 1.0 / (2 * np.linalg.eigvalsh(S).max())
print(f"non-normal A=[[1,1.2],[0,1]]: alpha_sector={a_s:.3f}, barrier V_min={Vmin:.4f}, ratio {Vmin/a_s:.3f}")
for A_name, A_rot in [("rotation alpha=1, omega=3", np.array([[1.0, 3.0], [-3.0, 1.0]]))]:
    S = linalg.solve_continuous_lyapunov(A_rot, np.eye(2))
    print(f"{A_name}: alpha_sector=1.000, barrier V_min={1/(2*np.linalg.eigvalsh(S).max()):.4f} (tight)")

print("\n=== (3) MC slope of log E[tau] vs 1/sigma^2, non-normal A, R=1 ===")
A = np.array([[1.0, 1.2], [0.0, 1.0]])
inv_s2, logT = [], []
for sig in [1.0, 0.8, 0.65, 0.55]:
    t = mc_exit(lambda x: x @ A.T, sig, 1.0, 2, 1500, 2e-4)
    inv_s2.append(1 / sig**2); logT.append(np.log(np.nanmean(t)))
    print(f"sigma={sig}: E[tau]={np.nanmean(t):.3f}")
slope = np.polyfit(inv_s2, logT, 1)[0]
print(f"fitted slope {slope:.3f}  vs barrier V_min {Vmin:.3f}  vs sector bound alpha_s R^2 {a_s:.3f}")
