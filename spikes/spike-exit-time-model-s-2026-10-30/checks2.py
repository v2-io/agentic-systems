"""KR C.2 / C1 — follow-up checks prompted by checks.py's first sections.

(A) Discrete-monitoring bias: n=2 OU, alpha=2, kappa=2 — MC E[tau] at dt = 1e-3, 1e-4, 2e-5 vs Phi(0),
    and with the Broadie-Glasserman-Kou boundary correction R_eff = R - beta1 * sigma * sqrt(dt), beta1 = 0.5826.
(B) The radially-tight tangential field: Euler-Maruyama inflates |x| by a factor (1 + omega^2 dt^2)^(1/2) per step
    when the rotation is fast, which is a scheme artifact, not dynamics. Re-test the equality prediction with a
    splitting scheme that applies the rotation exactly (norm-preserving) and EM to the radial OU part, at two dt.
    Prediction (Theorem 1 equality clause / Theorem 2): same E[tau] and same survival curve as OU(alpha).
(C) Same tangential field, plain EM at dt = 2e-5: the artifact should shrink toward OU.
"""
import numpy as np
from scipy import integrate, special

rng = np.random.default_rng(20261031)


def Phi(r, alpha, n, sigma, R):
    a = alpha / sigma**2
    half = n / 2.0
    gam = special.gamma(half)

    def integrand(u):
        if u <= 0:
            return 0.0
        inner = 0.5 * a**(-half) * gam * special.gammainc(half, a * u * u)
        return inner / (u**(n - 1) * np.exp(-a * u * u))

    return (2.0 / sigma**2) * integrate.quad(integrand, r, R, limit=400)[0]


def mc_exit_generic(stepper, sigma, R, n_dim, n_paths, dt, record_at=(), max_steps=50_000_000):
    x = np.zeros((n_paths, n_dim))
    t_exit = np.full(n_paths, np.nan)
    alive = np.arange(n_paths)
    surv = {}
    rec = sorted(record_at)
    ri = 0
    for step in range(1, max_steps + 1):
        xa = stepper(x[alive], dt)
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


alpha, sigma, R, n = 2.0, 1.0, 1.0, 2
phi0 = Phi(0, alpha, n, sigma, R)
print(f"Phi(0) for n=2, alpha=2, kappa=2: {phi0:.4f}", flush=True)

print("\n=== (A) discrete-monitoring bias, OU n=2 alpha=2 ===", flush=True)
beta1 = 0.5826
for dt in [1e-3, 1e-4, 2e-5]:
    npaths = 3000 if dt >= 1e-4 else 1500
    ou_step = lambda xa, dt: xa - alpha * xa * dt + sigma * np.sqrt(dt) * rng.standard_normal(xa.shape)
    t, _ = mc_exit_generic(ou_step, sigma, R, n, npaths, dt)
    m, se = np.nanmean(t), np.nanstd(t) / np.sqrt(npaths)
    phi_corr = Phi(0, alpha, n, sigma, R + beta1 * sigma * np.sqrt(dt))  # discrete monitoring ~ exit from a slightly larger ball
    print(f"dt={dt:g}: MC {m:.4f} +- {se:.4f}   Phi(0)={phi0:.4f}   BGK-corrected Phi(0; R+beta1 sigma sqrt(dt))={phi_corr:.4f}", flush=True)

print("\n=== (B) radially tight tangential field, rotation-exact splitting ===", flush=True)
def omega_of(r2):
    return 6.0 + 20.0 * np.sin(5.0 * r2)

def split_step(xa, dt):
    r2 = np.einsum('ij,ij->i', xa, xa)
    th = omega_of(r2) * dt            # rotate exactly by angle omega*dt (sign convention immaterial for the norm)
    c, s = np.cos(th), np.sin(th)
    xr = np.stack([c * xa[:, 0] - s * xa[:, 1], s * xa[:, 0] + c * xa[:, 1]], axis=1)
    return xr - alpha * xr * dt + sigma * np.sqrt(dt) * rng.standard_normal(xr.shape)

rec = (0.25, 0.5, 1.0, 2.0)
for dt in [1e-4, 2e-5]:
    npaths = 3000 if dt >= 1e-4 else 1500
    ou_step = lambda xa, dt: xa - alpha * xa * dt + sigma * np.sqrt(dt) * rng.standard_normal(xa.shape)
    t_ou, s_ou = mc_exit_generic(ou_step, sigma, R, n, npaths, dt, rec)
    t_tg, s_tg = mc_exit_generic(split_step, sigma, R, n, npaths, dt, rec)
    print(f"dt={dt:g}: OU  E[tau] {np.nanmean(t_ou):.4f} +- {np.nanstd(t_ou)/np.sqrt(npaths):.4f}   survival {[round(s_ou[k],3) for k in rec]}", flush=True)
    print(f"dt={dt:g}: TAN E[tau] {np.nanmean(t_tg):.4f} +- {np.nanstd(t_tg)/np.sqrt(npaths):.4f}   survival {[round(s_tg[k],3) for k in rec]}   (predict equal to OU within MC error)", flush=True)

print("\n=== (C) same field, plain Euler-Maruyama at dt=2e-5 (artifact should shrink) ===", flush=True)
def em_step(xa, dt):
    r2 = np.einsum('ij,ij->i', xa, xa)[:, None]
    Jx = np.stack([-xa[:, 1], xa[:, 0]], axis=1)
    return xa - (alpha * xa + omega_of(r2) * Jx) * dt + sigma * np.sqrt(dt) * rng.standard_normal(xa.shape)
t, _ = mc_exit_generic(em_step, sigma, R, n, 1500, 2e-5)
print(f"plain EM dt=2e-5: E[tau] {np.nanmean(t):.4f} +- {np.nanstd(t)/np.sqrt(1500):.4f}   (checks.py had 0.895 at dt=1e-4; OU MC at this dt is above)", flush=True)
print("done", flush=True)
