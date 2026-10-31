"""Variant E, decomposed by noise placement (2026-10-30).

Variant E (variant_ef_extensions.py, run_variant_e_adversarial) put observation
noise of the same scale on BOTH agents' channels. This script asks which channel
the measured exponent collapse comes from.

1. Closed form. Each agent runs the discrete linear corrector
       delta_{t+1} = (1 - a) delta_t - a * eps_obs + w,   Var w = rho^2, Var eps_obs = s^2,
   whose stationary variance is V(a, rho, s) = (rho^2 + a^2 s^2) / (a (2 - a)).
   Variant E's coupling is rho_A = q + gamma * a_B, rho_B = q + gamma * a_A, and its
   tempo advantage is a_A = r * eta on one noisy observation per step (gain on a fixed
   channel, not event rate, despite the original docstring). The mismatch ratio is
   sqrt(V_B / V_A); the exponent is the OLS log-log slope over the 12 tempo ratios.
   The two-sided columns reproduce the recorded Variant-E table.

2. Simulation. The Variant-E fixed-gain loop, copied unchanged except that the two
   channels get separate noise scales (A only, B only, both).

3. Event-rate tempo (closed form only, not simulated): A takes r sub-updates per step
   at per-event gain eta, each on a fresh observation; c = (1 - eta)^r, and
   V_A = rho_A^2 / (1 - c^2) + eta s^2 / (2 - eta).

Run:  python3 -I variant_e_noise_placement.py   (seed 42; about a minute)
Results: variant_e_noise_placement_results.md
"""
import numpy as np
from scipy.optimize import brentq

Q, GAMMA, ETA = 0.05, 0.5, 0.1
RATIOS = np.logspace(np.log10(0.5), np.log10(4.0), 12)
SIGMAS = [0.0, 0.1, 0.2, 0.5, 1.0]


def stat_var(a, rho, s):
    return (rho ** 2 + a ** 2 * s ** 2) / (a * (2 - a))


def variant_e_gain(s):
    """compute_optimal_gain from variant_ef_extensions.py, same constants."""
    if s <= 0:
        return ETA
    q2, s2 = Q * Q, s * s
    f = lambda P: P * P * (P + 2 * s2) / (P + s2) ** 2 - q2
    P = brentq(f, 1e-15, max(q2 / (2 * ETA - ETA * ETA), q2 + s2) * 10)
    return float(np.clip(P / (P + s2), 0.001, 0.999))


def slope(y):
    return np.polyfit(np.log(RATIOS), np.log(y), 1)[0]


def closed_form(sA, sB, base=ETA, event_rate=False):
    aB = base
    aA = np.minimum(RATIOS * base, 0.9)
    rhoA = Q + GAMMA * aB
    VB = stat_var(aB, Q + GAMMA * aA, sB)
    if event_rate:
        c = (1 - base) ** RATIOS
        aA = 1 - c  # per-step contraction
        VB = stat_var(aB, Q + GAMMA * aA, sB)
        VA = rhoA ** 2 / (1 - c ** 2) + base * sA ** 2 / (2 - base)
    else:
        VA = stat_var(aA, rhoA, sA)
    return np.sqrt(VB / VA), np.sqrt(VB), np.sqrt(VA)


def simulate(sA, sB, n=150, T=15000, burn=4000, seed=42):
    meds = []
    for r in RATIOS:
        TA, TB = min(r * ETA, 0.9), ETA
        rng = np.random.default_rng(seed)
        eA = rng.normal(0, Q + GAMMA * TB, (n, T))
        eB = rng.normal(0, Q + GAMMA * TA, (n, T))
        oA = rng.normal(0, sA, (n, T)) if sA > 0 else np.zeros((n, T))
        oB = rng.normal(0, sB, (n, T)) if sB > 0 else np.zeros((n, T))
        dA, dB = np.zeros(n), np.zeros(n)
        sumA, sumB = np.zeros(n), np.zeros(n)
        for t in range(T - 1):
            dA = dA - TA * (dA + oA[:, t]) + eA[:, t]
            dB = dB - TB * (dB + oB[:, t]) + eB[:, t]
            if t + 1 >= burn:
                sumA += np.abs(dA)
                sumB += np.abs(dB)
        meds.append(np.median(sumB / sumA))
    return np.array(meds)


def at(y, r):
    return float(np.interp(np.log(r), np.log(RATIOS), y))


if __name__ == "__main__":
    print("## 1. Closed form at Variant-E parameters")
    print("sigma | both fixed | both Variant-E gain | B only | A only || ratio at r=4: both / B only / A only ; defender RMS at r=4: both / B only")
    for s in SIGMAS:
        rb, vb, _ = closed_form(s, s)
        ro, _, _ = closed_form(s, s, base=variant_e_gain(s))
        rB, vB, _ = closed_form(0, s)
        rA, _, _ = closed_form(s, 0)
        print(f"{s:4.2f} | {slope(rb):5.2f} | {slope(ro):5.2f} | {slope(rB):5.2f} | {slope(rA):5.2f} || "
              f"{rb[-1]:5.2f} {rB[-1]:5.2f} {rA[-1]:5.2f} ; {vb[-1]:.3f} {vB[-1]:.3f}")
    print("\n## 2. Simulation (Variant-E fixed-gain loop, channels separated)")
    for sA, sB, lab in [(0, 0, "none"), (1.0, 1.0, "both 1.0"), (0, 1.0, "B only 1.0"), (1.0, 0, "A only 1.0"),
                        (0.5, 0.5, "both 0.5"), (0, 0.5, "B only 0.5"), (0.5, 0, "A only 0.5")]:
        m = simulate(sA, sB)
        print(f"{lab:11s} slope {slope(m):5.2f}  ratio r=0.5 {m[0]:5.2f}  r=1 {at(m, 1):5.2f}  r=4 {m[-1]:5.2f}")
    print("\n## 3. Event-rate tempo, closed form only")
    for s in SIGMAS:
        rb, _, _ = closed_form(s, s, event_rate=True)
        rA, _, _ = closed_form(s, 0, event_rate=True)
        print(f"{s:4.2f} | both {slope(rb):5.2f} | A only {slope(rA):5.2f} | ratio at r=4 both {rb[-1]:5.2f}")
