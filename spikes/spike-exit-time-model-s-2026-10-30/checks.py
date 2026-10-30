"""KR C.2 / C1 — numerical checks for the exit-time comparison theorem.

Everything here is a *check* of statements derived in 03-derivation.md, not the basis for them.

Objects:
  Phi(r; alpha, n, sigma, R)   mean exit time of the isotropic n-dim OU(alpha) process from the
                               ball of radius R, started at radius r (closed form, double integral).
  kappa = alpha R^2 / sigma^2  the exit exponent.

Checks:
  (1) 1-D: Phi reproduces the explorer's exact table (scale-function quadrature) and MC.
  (2) n-D: Phi(0) vs Euler-Maruyama MC for n = 2, 3; and the Laplace asymptotic
      Phi(0) ~ Gamma(n/2)/(2 alpha) kappa^{-n/2} e^{kappa}.
  (3) alpha * Phi(0) at the mean-square threshold kappa = n/2, for several n.
  (4) Adversarial sector drifts F with A2' floor alpha: E[tau] >= Phi(0) must hold.
      (a) tangential nonlinear field, delta^T F = alpha |delta|^2 exactly  -> equality predicted
      (b) diag(alpha, 5 alpha)                                            -> strict
      (c) kinked piecewise-linear radial F (no Lipschitz at the kink)      -> holds
      (d) the Lemma A.1N dip drift                                         -> far above
      (e) upper bound with ceiling alpha_bar for (b)                        -> E[tau] <= Phi_{alpha_bar}(0)
  (5) Lifetime bound P_0(tau <= L) <= L / Phi(0), against MC, for OU and for (b).
  (6) Stochastic domination spot-check: empirical survival P(tau > t) of (b) vs OU(alpha) at a few t.
"""
import sys
import numpy as np
from scipy import integrate, special

rng = np.random.default_rng(20261030)
np.set_printoptions(precision=4, suppress=True)


def Phi(r, alpha, n, sigma, R):
    """E_r[tau_R] for isotropic n-dim OU(alpha): (2/sigma^2) int_r^R (int_0^u m)/m(u) du,
    m(u) = u^{n-1} exp(-a u^2), a = alpha/sigma^2.  Inner integral via regularized lower incomplete gamma."""
    a = alpha / sigma**2
    half = n / 2.0
    gam = special.gamma(half)

    def integrand(u):
        if u <= 0:
            return 0.0
        inner = 0.5 * a**(-half) * gam * special.gammainc(half, a * u * u)
        return inner / (u**(n - 1) * np.exp(-a * u * u))

    val, err = integrate.quad(integrand, r, R, limit=400)
    return (2.0 / sigma**2) * val


def Phi_asym(alpha, n, sigma, R):
    k = alpha * R**2 / sigma**2
    return special.gamma(n / 2.0) / (2 * alpha) * k**(-n / 2.0) * np.exp(k)


def exact_T0_1d(U, sigma, R):
    """Explorer's 1-D formula for even U (reference)."""
    inner = lambda y: integrate.quad(lambda z: np.exp(-2 * U(z) / sigma**2), 0, y)[0]
    return (2 / sigma**2) * integrate.quad(lambda y: np.exp(2 * U(y) / sigma**2) * inner(y), 0, R, limit=200)[0]


def mc_exit(drift, sigma, R, n_dim, n_paths, dt, x0=None, max_steps=20_000_000, record_survival_at=None):
    """Euler-Maruyama first exit of |x| > R. Returns exit times (and survival fractions at requested t)."""
    x = np.zeros((n_paths, n_dim)) if x0 is None else np.tile(np.asarray(x0, float), (n_paths, 1))
    t_exit = np.full(n_paths, np.nan)
    alive = np.arange(n_paths)
    sq = sigma * np.sqrt(dt)
    surv = {}
    rec = sorted(record_survival_at) if record_survival_at else []
    ri = 0
    for step in range(1, max_steps + 1):
        xa = x[alive]
        xa = xa - drift(xa) * dt + sq * rng.standard_normal(xa.shape)
        x[alive] = xa
        out = np.einsum('ij,ij->i', xa, xa) > R**2
        if out.any():
            t_exit[alive[out]] = step * dt
            alive = alive[~out]
        t = step * dt
        while ri < len(rec) and t >= rec[ri]:
            surv[rec[ri]] = alive.size / n_paths
            ri += 1
        if alive.size == 0:
            break
    while ri < len(rec):
        surv[rec[ri]] = 0.0
        ri += 1
    return t_exit, surv


def report_mc(label, t, pred_lo=None, pred_hi=None):
    m, se = np.nanmean(t), np.nanstd(t) / np.sqrt(np.sum(~np.isnan(t)))
    cv = np.nanstd(t) / m
    s = f"{label:<58} MC E[tau] = {m:8.3f} +- {se:6.3f}  (CV {cv:.2f})"
    if pred_lo is not None:
        s += f"   lower bound Phi_alpha(0) = {pred_lo:8.3f}  ratio {m/pred_lo:6.3f}"
    if pred_hi is not None:
        s += f"   upper bound Phi_abar(0) = {pred_hi:8.3f}"
    print(s, flush=True)
    return m, se


print("=== (1) 1-D: Phi vs explorer's quadrature, sigma = R = 1 (kappa = alpha) ===", flush=True)
print(f"{'alpha':>6} {'Phi(0)':>10} {'explorer exact':>15} {'alpha*Phi':>10} {'asym':>10} {'Phi/asym':>9}")
for alpha in [0.5, 1, 2, 3, 4, 6, 8]:
    p = Phi(0, alpha, 1, 1.0, 1.0)
    e = exact_T0_1d(lambda y: alpha * y**2 / 2, 1.0, 1.0)
    print(f"{alpha:6.1f} {p:10.4f} {e:15.4f} {alpha*p:10.3f} {Phi_asym(alpha,1,1,1):10.4f} {p/Phi_asym(alpha,1,1,1):9.3f}", flush=True)

print("\n=== (2) n-D OU: Phi(0) vs MC, and vs the Laplace asymptotic; sigma = R = 1 ===", flush=True)
for n, alpha in [(2, 1.0), (2, 2.0), (2, 3.0), (3, 1.5), (3, 3.0), (5, 2.5)]:
    p = Phi(0, alpha, n, 1.0, 1.0)
    t, _ = mc_exit(lambda x: alpha * x, 1.0, 1.0, n, 2000, 1e-4)
    m, se = np.nanmean(t), np.nanstd(t) / np.sqrt(2000)
    print(f"n={n} alpha={alpha:.1f} kappa={alpha:.1f}: Phi(0)={p:8.4f}  MC={m:8.4f}+-{se:.4f}  asym={Phi_asym(alpha,n,1,1):8.4f}  Phi/asym={p/Phi_asym(alpha,n,1,1):.3f}", flush=True)
print("Phi/asym -> 1 as kappa grows (n=2):", [round(Phi(0, k, 2, 1, 1) / Phi_asym(k, 2, 1, 1), 3) for k in [4, 8, 12, 16]], flush=True)
print("Phi/asym -> 1 as kappa grows (n=5):", [round(Phi(0, k, 5, 1, 1) / Phi_asym(k, 5, 1, 1), 3) for k in [6, 12, 20, 30]], flush=True)

print("\n=== (3) alpha * Phi(0) at the mean-square threshold kappa = n/2 (R = R*_S) ===", flush=True)
for n in [1, 2, 3, 5, 10, 20, 50]:
    k = n / 2.0
    p = Phi(0, k, n, 1.0, 1.0)  # alpha = kappa when sigma = R = 1
    print(f"n={n:3d}: kappa=n/2={k:5.1f}  alpha*E[tau] = {k*p:.4f}", flush=True)
print("and at kappa = n/2 + c for n=3:", [(c, round((1.5 + c) * Phi(0, 1.5 + c, 3, 1, 1), 3)) for c in [0, 1, 2, 4, 6]], flush=True)

print("\n=== (4) adversarial sector drifts, n = 2, sigma = R = 1, alpha floor = 2 (kappa = 2) ===", flush=True)
alpha = 2.0
lo = Phi(0, alpha, 2, 1.0, 1.0)
t_ou, surv_ou = mc_exit(lambda x: alpha * x, 1.0, 1.0, 2, 3000, 1e-4, record_survival_at=[0.5, 1, 2, 4])
report_mc("OU(alpha=2) reference", t_ou, lo)

def F_tangential(x):   # alpha x + omega(|x|) J x, omega nonlinear and large: x^T F = alpha |x|^2 exactly
    r2 = np.einsum('ij,ij->i', x, x)[:, None]
    omega = 6.0 + 20.0 * np.sin(5.0 * r2)
    Jx = np.stack([-x[:, 1], x[:, 0]], axis=1)
    return alpha * x + omega * Jx
t, _ = mc_exit(F_tangential, 1.0, 1.0, 2, 3000, 1e-4)
report_mc("(a) tangential nonlinear field, radially tight (predict ==)", t, lo)

A_diag = np.diag([2.0, 10.0])
t_b, surv_b = mc_exit(lambda x: x @ A_diag.T, 1.0, 1.0, 2, 3000, 1e-4, record_survival_at=[0.5, 1, 2, 4])
report_mc("(b) diag(2, 10): floor 2, ceiling 10 (predict strict >)", t_b, lo, Phi(0, 10.0, 2, 1.0, 1.0))

def F_kink(x):          # radial g(r) r-hat with g(r) = 2 r for r<0.5, 2r + 6(r-0.5) for r>=0.5 : floor alpha=2, kink at 0.5
    r = np.sqrt(np.einsum('ij,ij->i', x, x))[:, None]
    g = 2.0 * r + 6.0 * np.maximum(r - 0.5, 0.0)
    return np.where(r > 0, g * x / np.maximum(r, 1e-12), 0.0)
t, _ = mc_exit(F_kink, 1.0, 1.0, 2, 3000, 1e-4)
report_mc("(c) kinked radial F, floor 2 attained on r<0.5 (predict >)", t, lo)

def F_dip(x):           # A.1N-style: g = 20 everywhere except a dip to g = 2 near r = 0.5 (floor alpha = 2)
    r = np.sqrt(np.einsum('ij,ij->i', x, x))[:, None]
    g = 20.0 - 18.0 * np.exp(-((r - 0.5) / 0.03)**2)
    return g * x
t, _ = mc_exit(F_dip, 1.0, 1.0, 2, 3000, 1e-4)
report_mc("(d) dip drift: floor 2 only on a thin shell at r=0.5 (predict >>)", t, lo)

def F_rot_aniso(x):     # non-normal: sym part has eigenvalues 2 and 10, plus rotation; floor = lambda_min(sym) = 2
    A = np.array([[6.0, 4.0 + 5.0], [4.0 - 5.0, 6.0]])   # sym = [[6,4],[4,6]] -> eig 2, 10 ; antisym = 5 J
    return x @ A.T
t, _ = mc_exit(F_rot_aniso, 1.0, 1.0, 2, 3000, 1e-4)
report_mc("(e) non-normal, sym eig {2,10} + rotation (predict in [Phi_2, Phi_10])", t, lo, Phi(0, 10.0, 2, 1.0, 1.0))

print("\n=== (4') same adversarial set at kappa = 4 (alpha floor 4) ===", flush=True)
alpha = 4.0
lo4 = Phi(0, alpha, 2, 1.0, 1.0)
t, _ = mc_exit(lambda x: alpha * x, 1.0, 1.0, 2, 2000, 1e-4); report_mc("OU(alpha=4)", t, lo4)
def F_tangential4(x):
    r2 = np.einsum('ij,ij->i', x, x)[:, None]
    omega = 6.0 + 20.0 * np.sin(5.0 * r2)
    Jx = np.stack([-x[:, 1], x[:, 0]], axis=1)
    return alpha * x + omega * Jx
t, _ = mc_exit(F_tangential4, 1.0, 1.0, 2, 2000, 1e-4); report_mc("(a) tangential, tight at 4 (predict ==)", t, lo4)
t, _ = mc_exit(lambda x: x @ np.diag([4.0, 12.0]).T, 1.0, 1.0, 2, 2000, 1e-4); report_mc("(b) diag(4,12) (predict >)", t, lo4, Phi(0, 12.0, 2, 1, 1))

print("\n=== (5) lifetime bound P_0(tau <= L) <= L / Phi_alpha(0), n=2, alpha=2, kappa=2 ===", flush=True)
alpha = 2.0
for L in [0.5, 1.0, 2.0, 4.0]:
    bound = L / lo
    p_ou = 1 - surv_ou[L]
    p_b = 1 - surv_b[L]
    print(f"L={L:4.1f}: bound {min(bound,1):.3f}   MC OU {p_ou:.3f}   MC diag(2,10) {p_b:.3f}   Prop A.1S(iv) bound n*sigma^2*L/R^2 = {min(2*L,1):.3f}", flush=True)
print("At kappa = 6 (alpha=6, n=2): Phi(0) =", round(Phi(0, 6, 2, 1, 1), 2), " so P(exit by L=1) <=", round(1 / Phi(0, 6, 2, 1, 1), 4), "; (iv) gives", min(2 * 1, 1), flush=True)
print("At kappa = 10 (alpha=10, n=2): Phi(0) =", round(Phi(0, 10, 2, 1, 1), 2), " so P(exit by L=1) <=", round(1 / Phi(0, 10, 2, 1, 1), 5), flush=True)

print("\n=== (6) stochastic domination spot-check: survival P(tau > t), diag(2,10) vs OU(2) ===", flush=True)
for tt in [0.5, 1, 2, 4]:
    print(f"t={tt}: OU {surv_ou[tt]:.3f}   diag(2,10) {surv_b[tt]:.3f}   (domination predicts diag >= OU)", flush=True)

print("\n=== (7) Phi is decreasing in r and the start-dependence: n=2, alpha=2 ===", flush=True)
print([round(Phi(r, 2.0, 2, 1, 1), 3) for r in [0, 0.25, 0.5, 0.75, 0.9, 1.0]], flush=True)
print("done", flush=True)
