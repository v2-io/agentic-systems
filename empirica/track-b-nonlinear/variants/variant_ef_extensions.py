"""
Variant E & F: Observation Noise and Multi-Dimensional Anisotropic Correction

Variant E tests TF-06's uncertainty ratio principle empirically:
  - The agent observes a noisy version of the mismatch: delta_obs = delta_true + noise
  - Optimal gain eta* = U_M / (U_M + U_o) should help when observations are noisy
  - Sweeps sigma_obs and compares fixed vs optimal gain

Variant F tests TF-11 Open Question #4 on anisotropic tempo:
  - Multi-dimensional environment (d=3) with different noise and gain per dimension
  - Tests whether scalar tempo predicts overall behavior or if the weak dimension
    is the bottleneck
  - Adversarial case: targeted vs uniform disturbance

Theory references:
  - TF-06: eta* = U_M / (U_M + U_o)
  - TF-11 Open Question #4: tempo as tensor
  - TF-11 Corollary 11.2: adversarial squared tempo advantage

Imports correction functions from parent sim1.
"""

import sys
from pathlib import Path

# Add parent directory to path for sim1 imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from typing import Dict, Tuple, Optional
from sim1_nonlinear_mismatch import g_linear, g_saturating

# ---------------------------------------------------------------------------
# Output directory
# ---------------------------------------------------------------------------
OUTPUT_DIR = Path(__file__).parent
FIGURE_DIR = OUTPUT_DIR

# ---------------------------------------------------------------------------
# Plotting style
# ---------------------------------------------------------------------------
plt.rcParams.update({
    "figure.figsize": (8, 6),
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "font.size": 12,
    "axes.titlesize": 14,
    "axes.labelsize": 12,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.fontsize": 10,
    "lines.linewidth": 1.5,
    "axes.grid": True,
    "grid.alpha": 0.3,
})


# ===================================================================
# VARIANT E: Observation Noise
# ===================================================================

def simulate_observation_noise(
    eta: float,
    q_env: float,
    sigma_obs: float,
    num_steps: int = 10_000,
    num_trials: int = 200,
    burn_in: int = 2_000,
    seed: int = 42,
    g=g_linear,
    **g_kwargs,
) -> Tuple[np.ndarray, np.ndarray]:
    """Simulate mismatch dynamics with noisy observations.

    Environment: x_{t+1} = x_t + q_env * eps_env
    Observation: o_t = x_t + sigma_obs * eps_obs
    Perceived mismatch: delta_obs_t = o_t - x_hat_t = delta_true_t + sigma_obs * eps_obs
    Update: x_hat_{t+1} = x_hat_t + eta * g(delta_obs_t)

    The true mismatch evolves as:
        delta_true_{t+1} = delta_true_t - eta * g(delta_obs_t) + q_env * eps_env

    Returns:
        (delta_true, delta_obs): each shape (num_trials, num_steps)
    """
    rng = np.random.default_rng(seed)
    n, T = num_trials, num_steps

    env_noise = rng.normal(0.0, q_env, size=(n, T))
    obs_noise = rng.normal(0.0, sigma_obs, size=(n, T)) if sigma_obs > 0 else np.zeros((n, T))

    delta_true = np.zeros((n, T))
    delta_obs = np.zeros((n, T))

    for t in range(T - 1):
        # Observed mismatch = true mismatch + observation noise
        delta_obs[:, t] = delta_true[:, t] + obs_noise[:, t]
        # Agent corrects based on observed mismatch
        correction = g(delta_obs[:, t], **g_kwargs)
        # True mismatch evolves: environment drifts, agent corrects
        delta_true[:, t + 1] = delta_true[:, t] - eta * correction + env_noise[:, t]

    # Final observation
    delta_obs[:, -1] = delta_true[:, -1] + obs_noise[:, -1]

    return delta_true, delta_obs


def compute_optimal_gain(q_env: float, eta_base: float, sigma_obs: float) -> float:
    """Compute TF-06's optimal gain: eta* = U_M / (U_M + U_o).

    For the random walk environment with base gain eta_base:
    - U_M (model uncertainty / process variance) ~ q_env^2 / (2*eta_base)
      This is the steady-state variance of the AR(1) process in the
      no-observation-noise case, which represents how uncertain the model
      is about the true state.
    - U_o (observation uncertainty) = sigma_obs^2

    The optimal gain eta* = U_M / (U_M + U_o).

    In steady state for the linear case, the Kalman-like optimal gain for
    a random walk observed in noise is:
        eta* = solution of eta = P / (P + sigma_obs^2)
        where P satisfies the Riccati equation P = (1-eta)^2 * P + q^2
    We solve this exactly.
    """
    if sigma_obs <= 0:
        return min(eta_base, 1.0)  # No obs noise -> trust observation fully (up to stability)

    q2 = q_env ** 2
    s2 = sigma_obs ** 2

    # Steady-state Riccati for scalar random walk + obs noise:
    # P = (1 - K)^2 * P + q^2, where K = P / (P + s2)
    # Substituting: P = (s2/(P+s2))^2 * P + q2
    # => P * (1 - s2^2/(P+s2)^2) = q2
    # => P * ((P+s2)^2 - s2^2) / (P+s2)^2 = q2
    # => P * (P^2 + 2*P*s2) / (P+s2)^2 = q2
    # => P^2 * (P + 2*s2) / (P+s2)^2 = q2
    # This is a cubic in P. Solve numerically.
    # Then eta* = P / (P + s2)

    from scipy.optimize import brentq

    def riccati_residual(P):
        if P <= 0:
            return -q2
        return P ** 2 * (P + 2 * s2) / (P + s2) ** 2 - q2

    # P must be positive; upper bound from no-obs-noise case
    P_upper = q2 / (2 * eta_base - eta_base ** 2) if eta_base < 1 else q2 * 100
    P_upper = max(P_upper, q2 + s2) * 10  # generous upper bound

    try:
        P_star = brentq(riccati_residual, 1e-15, P_upper)
        eta_star = P_star / (P_star + s2)
    except (ValueError, RuntimeError):
        # Fallback: use the approximate formula
        U_M = q2 / max(2 * eta_base - eta_base ** 2, 0.01)
        eta_star = U_M / (U_M + s2)

    return float(np.clip(eta_star, 0.001, 0.999))


def run_variant_e_sweep(
    sigma_obs_values: np.ndarray,
    eta_fixed: float = 0.1,
    q_env: float = 0.1,
    num_steps: int = 10_000,
    num_trials: int = 200,
    burn_in: int = 2_000,
    seed: int = 42,
) -> Dict[str, np.ndarray]:
    """Sweep sigma_obs and compare fixed vs optimal gain.

    Returns dict with keys:
        - sigma_obs: the sweep values
        - ss_fixed: steady-state E[|delta_true|] with fixed eta
        - ss_optimal: steady-state E[|delta_true|] with optimal eta*
        - eta_star: the optimal gain at each sigma_obs
        - ss_fixed_q10/q90: 10th/90th percentiles for fixed
        - ss_optimal_q10/q90: 10th/90th percentiles for optimal
    """
    ss_fixed = []
    ss_optimal = []
    eta_stars = []
    ss_fixed_q10, ss_fixed_q90 = [], []
    ss_optimal_q10, ss_optimal_q90 = [], []

    for sigma_obs in sigma_obs_values:
        # Fixed gain
        dt_fixed, _ = simulate_observation_noise(
            eta=eta_fixed, q_env=q_env, sigma_obs=sigma_obs,
            num_steps=num_steps, num_trials=num_trials,
            burn_in=burn_in, seed=seed,
        )
        trial_means_f = np.mean(np.abs(dt_fixed[:, burn_in:]), axis=1)
        ss_fixed.append(np.mean(trial_means_f))
        ss_fixed_q10.append(np.percentile(trial_means_f, 10))
        ss_fixed_q90.append(np.percentile(trial_means_f, 90))

        # Optimal gain
        eta_star = compute_optimal_gain(q_env, eta_fixed, sigma_obs)
        eta_stars.append(eta_star)

        dt_opt, _ = simulate_observation_noise(
            eta=eta_star, q_env=q_env, sigma_obs=sigma_obs,
            num_steps=num_steps, num_trials=num_trials,
            burn_in=burn_in, seed=seed,
        )
        trial_means_o = np.mean(np.abs(dt_opt[:, burn_in:]), axis=1)
        ss_optimal.append(np.mean(trial_means_o))
        ss_optimal_q10.append(np.percentile(trial_means_o, 10))
        ss_optimal_q90.append(np.percentile(trial_means_o, 90))

        print(f"  sigma_obs={sigma_obs:.3f}: eta*={eta_star:.4f}, "
              f"SS_fixed={ss_fixed[-1]:.4f}, SS_optimal={ss_optimal[-1]:.4f}")

    return {
        "sigma_obs": sigma_obs_values,
        "ss_fixed": np.array(ss_fixed),
        "ss_optimal": np.array(ss_optimal),
        "eta_star": np.array(eta_stars),
        "ss_fixed_q10": np.array(ss_fixed_q10),
        "ss_fixed_q90": np.array(ss_fixed_q90),
        "ss_optimal_q10": np.array(ss_optimal_q10),
        "ss_optimal_q90": np.array(ss_optimal_q90),
    }


def plot_variant_e_steadystate(
    results: Dict[str, np.ndarray],
    eta_fixed: float,
    q_env: float,
    save_path: Optional[Path] = None,
):
    """Plot 1: Steady-state |delta_true| vs sigma_obs for fixed and optimal gain."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    sigma = results["sigma_obs"]

    # Left panel: steady-state mismatch
    ax1.plot(sigma, results["ss_fixed"], "o-", color="#d62728", markersize=5,
             label=f"Fixed $\\eta = {eta_fixed}$")
    ax1.fill_between(sigma, results["ss_fixed_q10"], results["ss_fixed_q90"],
                     color="#d62728", alpha=0.15)
    ax1.plot(sigma, results["ss_optimal"], "s-", color="#1f77b4", markersize=5,
             label="Optimal $\\eta^* = U_M/(U_M+U_o)$")
    ax1.fill_between(sigma, results["ss_optimal_q10"], results["ss_optimal_q90"],
                     color="#1f77b4", alpha=0.15)

    # No-noise baseline
    ax1.axhline(y=results["ss_fixed"][0], color="gray", linestyle=":", alpha=0.5,
                label=f"No-noise baseline ({results['ss_fixed'][0]:.3f})")

    ax1.set_xlabel("Observation noise $\\sigma_{\\mathrm{obs}}$")
    ax1.set_ylabel("Steady-state $\\langle|\\delta_{\\mathrm{true}}|\\rangle$")
    ax1.set_title("Steady-State True Mismatch vs. Observation Noise")
    ax1.legend(fontsize=9)

    # Right panel: optimal gain
    ax2.plot(sigma, results["eta_star"], "o-", color="#2ca02c", markersize=5)
    ax2.axhline(y=eta_fixed, color="#d62728", linestyle="--", alpha=0.7,
                label=f"Fixed $\\eta = {eta_fixed}$")
    ax2.set_xlabel("Observation noise $\\sigma_{\\mathrm{obs}}$")
    ax2.set_ylabel("Optimal gain $\\eta^*$")
    ax2.set_title("Optimal Gain (TF-06) vs. Observation Noise")
    ax2.legend(fontsize=9)

    fig.suptitle(
        f"Variant E: Observation Noise  ($q_{{\\mathrm{{env}}}}={q_env}$)",
        fontsize=14, y=1.02,
    )
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        print(f"  Saved: {save_path}")
    return fig


def run_variant_e_adversarial(
    sigma_obs_values: np.ndarray,
    tempo_ratios: np.ndarray,
    eta_fixed: float = 0.1,
    q_env: float = 0.05,
    gamma: float = 0.5,
    num_steps: int = 15_000,
    num_trials: int = 200,
    burn_in: int = 4_000,
    seed: int = 42,
) -> Dict[str, np.ndarray]:
    """Adversarial variant E: two agents with observation noise.

    Agent A has tempo advantage via higher event rate nu_A (not higher gain).
    T_A = nu_A * eta, T_B = 1 * eta. The tempo ratio = nu_A.

    Within each timestep, agent A gets nu_A sub-updates (each with gain eta),
    while agent B gets 1. This keeps the per-update gain within stable range
    while giving A a genuine tempo advantage.

    For the "fixed" case, both agents use eta_fixed regardless of sigma_obs.
    For the "optimal" case, both use eta* from TF-06.

    Measure effective exponent for each sigma_obs level.

    Returns:
        Dictionary with exponents and mismatch ratios.
    """
    exponents_fixed = []
    exponents_optimal = []
    exponents_fixed_se = []
    exponents_optimal_se = []

    for sigma_obs in sigma_obs_values:
        medians_fixed = []
        medians_optimal = []

        eta_star = compute_optimal_gain(q_env, eta_fixed, sigma_obs)

        for r in tempo_ratios:
            # Effective tempo: T_A = r * eta, T_B = eta
            # We implement "r updates per step" for A by using the
            # effective single-step dynamics:
            # After r sub-updates each of size eta on a noisy observation:
            #   delta_A -> (1 - eta)^r * delta_A + noise_terms
            # For B with 1 sub-update:
            #   delta_B -> (1 - eta) * delta_B + noise_terms
            #
            # For simplicity and correctness, we use the composite
            # single-step contraction. T_A = r*eta (small eta, so
            # (1-eta)^r ~ 1 - r*eta = 1 - T_A for small eta).
            # We cap T at 0.9 for stability.

            T_A = min(r * eta_fixed, 0.9)
            T_B = eta_fixed

            rho_A = q_env + gamma * T_B
            rho_B = q_env + gamma * T_A

            for use_optimal, medians_list in [(False, medians_fixed), (True, medians_optimal)]:
                if use_optimal:
                    eta_star_val = compute_optimal_gain(q_env, eta_fixed, sigma_obs)
                    T_A_eff = min(r * eta_star_val, 0.9)
                    T_B_eff = eta_star_val
                    # Recompute rho with optimal-gain tempo
                    rho_A_eff = q_env + gamma * T_B_eff
                    rho_B_eff = q_env + gamma * T_A_eff
                else:
                    T_A_eff = T_A
                    T_B_eff = T_B
                    rho_A_eff = rho_A
                    rho_B_eff = rho_B

                rng = np.random.default_rng(seed)
                n, T = num_trials, num_steps

                noise_env_A = rng.normal(0.0, rho_A_eff, size=(n, T))
                noise_env_B = rng.normal(0.0, rho_B_eff, size=(n, T))
                noise_obs_A = rng.normal(0.0, sigma_obs, size=(n, T)) if sigma_obs > 0 else np.zeros((n, T))
                noise_obs_B = rng.normal(0.0, sigma_obs, size=(n, T)) if sigma_obs > 0 else np.zeros((n, T))

                delta_A = np.zeros((n, T))
                delta_B = np.zeros((n, T))

                for t in range(T - 1):
                    obs_A = delta_A[:, t] + noise_obs_A[:, t]
                    obs_B = delta_B[:, t] + noise_obs_B[:, t]
                    delta_A[:, t + 1] = delta_A[:, t] - T_A_eff * obs_A + noise_env_A[:, t]
                    delta_B[:, t + 1] = delta_B[:, t] - T_B_eff * obs_B + noise_env_B[:, t]

                ss_A = np.mean(np.abs(delta_A[:, burn_in:]), axis=1)
                ss_B = np.mean(np.abs(delta_B[:, burn_in:]), axis=1)
                valid = (ss_A > 1e-12) & np.isfinite(ss_A) & np.isfinite(ss_B)
                if np.any(valid):
                    medians_list.append(np.median(ss_B[valid] / ss_A[valid]))
                else:
                    medians_list.append(np.nan)

        # Estimate exponents
        medians_fixed = np.array(medians_fixed)
        medians_optimal = np.array(medians_optimal)

        b_f, se_f = _estimate_exponent(tempo_ratios, medians_fixed)
        b_o, se_o = _estimate_exponent(tempo_ratios, medians_optimal)
        exponents_fixed.append(b_f)
        exponents_optimal.append(b_o)
        exponents_fixed_se.append(se_f)
        exponents_optimal_se.append(se_o)

        print(f"  sigma_obs={sigma_obs:.3f}: "
              f"exp_fixed={b_f:.3f}+/-{se_f:.3f}, "
              f"exp_optimal={b_o:.3f}+/-{se_o:.3f}")

    return {
        "sigma_obs": sigma_obs_values,
        "exp_fixed": np.array(exponents_fixed),
        "exp_optimal": np.array(exponents_optimal),
        "exp_fixed_se": np.array(exponents_fixed_se),
        "exp_optimal_se": np.array(exponents_optimal_se),
    }


def _estimate_exponent(tempo_ratios, mismatch_ratios):
    """Estimate exponent b in mismatch_ratio ~ (T_A/T_B)^b via log-log OLS."""
    valid = np.isfinite(mismatch_ratios) & (mismatch_ratios > 0) & (tempo_ratios > 0)
    if np.sum(valid) < 3:
        return np.nan, np.nan
    x = np.log(tempo_ratios[valid])
    y = np.log(mismatch_ratios[valid])
    n = len(x)
    x_mean, y_mean = np.mean(x), np.mean(y)
    ss_xx = np.sum((x - x_mean) ** 2)
    ss_xy = np.sum((x - x_mean) * (y - y_mean))
    if ss_xx < 1e-12:
        return np.nan, np.nan
    b = ss_xy / ss_xx
    y_pred = y_mean + b * (x - x_mean)
    s2 = np.sum((y - y_pred) ** 2) / max(n - 2, 1)
    se = np.sqrt(s2 / ss_xx)
    return b, se


def plot_variant_e_adversarial(
    results: Dict[str, np.ndarray],
    save_path: Optional[Path] = None,
):
    """Plot adversarial exponent vs sigma_obs for fixed and optimal gain."""
    fig, ax = plt.subplots(figsize=(9, 6))

    sigma = results["sigma_obs"]
    ax.errorbar(sigma, results["exp_fixed"], yerr=2 * results["exp_fixed_se"],
                fmt="o-", color="#d62728", markersize=6, capsize=4,
                label="Fixed $\\eta$")
    ax.errorbar(sigma, results["exp_optimal"], yerr=2 * results["exp_optimal_se"],
                fmt="s-", color="#1f77b4", markersize=6, capsize=4,
                label="Optimal $\\eta^*$")

    ax.axhline(y=2.0, color="k", linestyle="--", linewidth=2, alpha=0.5,
               label="Corollary 11.2 prediction (exponent=2)")
    ax.axhline(y=1.0, color="gray", linestyle=":", alpha=0.5,
               label="Linear advantage (exponent=1)")

    ax.set_xlabel("Observation noise $\\sigma_{\\mathrm{obs}}$")
    ax.set_ylabel("Effective adversarial exponent $b$")
    ax.set_title("Variant E: How Observation Noise Affects the Adversarial Exponent")
    ax.legend(fontsize=9)
    ax.set_ylim(0, 3.0)
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path)
        print(f"  Saved: {save_path}")
    return fig


def plot_variant_e_gain_validation(
    sigma_obs_values: np.ndarray,
    eta_fixed: float,
    q_env: float,
    save_path: Optional[Path] = None,
):
    """Plot 2: Validate that the computed eta* actually minimizes steady-state mismatch.

    For a few sigma_obs values, sweep eta and measure SS mismatch. Show that
    eta* from TF-06 is at or near the minimum.
    """
    fig, ax = plt.subplots(figsize=(9, 6))
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

    test_sigmas = sigma_obs_values[::max(1, len(sigma_obs_values) // 4)][:5]
    eta_sweep = np.linspace(0.01, 0.5, 30)

    for idx, sigma_obs in enumerate(test_sigmas):
        ss_values = []
        for eta_test in eta_sweep:
            dt, _ = simulate_observation_noise(
                eta=eta_test, q_env=q_env, sigma_obs=sigma_obs,
                num_steps=6_000, num_trials=100, burn_in=2_000, seed=42,
            )
            ss = np.mean(np.abs(dt[:, 2_000:]))
            ss_values.append(ss)

        eta_star = compute_optimal_gain(q_env, eta_fixed, sigma_obs)
        color = colors[idx % len(colors)]
        ax.plot(eta_sweep, ss_values, "-", color=color, alpha=0.8,
                label=f"$\\sigma_{{obs}}={sigma_obs:.2f}$")
        ax.axvline(x=eta_star, color=color, linestyle="--", alpha=0.6)
        # Mark the minimum
        min_idx = np.argmin(ss_values)
        ax.plot(eta_sweep[min_idx], ss_values[min_idx], "v", color=color,
                markersize=10, zorder=5)
        ax.plot(eta_star, np.interp(eta_star, eta_sweep, ss_values), "*",
                color=color, markersize=12, zorder=5)

    ax.set_xlabel("Gain $\\eta$")
    ax.set_ylabel("Steady-state $\\langle|\\delta_{\\mathrm{true}}|\\rangle$")
    ax.set_title(
        "Gain Validation: $\\eta^*$ (stars) vs Empirical Minimum (triangles)\n"
        f"($q_{{\\mathrm{{env}}}}={q_env}$)"
    )
    ax.legend(fontsize=9)
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path)
        print(f"  Saved: {save_path}")
    return fig


# ===================================================================
# VARIANT F: Multi-Dimensional Anisotropic Correction
# ===================================================================

def simulate_anisotropic(
    eta_vec: np.ndarray,       # gain per dimension, shape (d,)
    q_vec: np.ndarray,         # env noise std per dimension, shape (d,)
    num_steps: int = 10_000,
    num_trials: int = 200,
    burn_in: int = 2_000,
    seed: int = 42,
) -> np.ndarray:
    """Simulate d-dimensional mismatch with anisotropic correction.

    delta_k[t+1] = delta_k[t] - eta_k * delta_k[t] + q_k * eps_k[t]

    Returns:
        delta: shape (num_trials, num_steps, d)
    """
    d = len(eta_vec)
    rng = np.random.default_rng(seed)

    delta = np.zeros((num_trials, num_steps, d))
    noise = np.zeros((num_trials, num_steps, d))
    for k in range(d):
        noise[:, :, k] = rng.normal(0.0, q_vec[k], size=(num_trials, num_steps))

    for t in range(num_steps - 1):
        for k in range(d):
            delta[:, t + 1, k] = (
                delta[:, t, k] - eta_vec[k] * delta[:, t, k] + noise[:, t, k]
            )

    return delta


def simulate_anisotropic_adversarial(
    eta_A: np.ndarray,  # A's gain per dim, shape (d,)
    eta_B: np.ndarray,  # B's gain per dim, shape (d,)
    q_base: float,
    gamma: float,
    disturbance_weights: np.ndarray,  # how adversary distributes disturbance across dims, shape (d,)
    num_steps: int = 15_000,
    num_trials: int = 200,
    burn_in: int = 4_000,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray]:
    """Two coupled agents in d dimensions with anisotropic correction.

    Agent A attacks B with disturbance distributed according to disturbance_weights
    (normalized so sum = 1).

    rho_B_k = q_base + gamma * T_A * w_k  where w_k = disturbance_weights[k]
    rho_A_k = q_base + gamma * T_B * w_k  (symmetric for simplicity)

    Returns:
        (delta_A, delta_B): each shape (num_trials, num_steps, d)
    """
    d = len(eta_A)
    rng = np.random.default_rng(seed)

    # Total tempo = sum of per-dimension tempos (each with nu=1)
    T_A_total = np.sum(eta_A)
    T_B_total = np.sum(eta_B)

    # Normalize disturbance weights
    w = disturbance_weights / np.sum(disturbance_weights)

    # Per-dimension disturbance rates
    rho_B = np.array([q_base + gamma * T_A_total * w[k] for k in range(d)])
    rho_A = np.array([q_base + gamma * T_B_total * w[k] for k in range(d)])

    delta_A = np.zeros((num_trials, num_steps, d))
    delta_B = np.zeros((num_trials, num_steps, d))

    noise_A = np.zeros((num_trials, num_steps, d))
    noise_B = np.zeros((num_trials, num_steps, d))
    for k in range(d):
        noise_A[:, :, k] = rng.normal(0.0, rho_A[k], size=(num_trials, num_steps))
        noise_B[:, :, k] = rng.normal(0.0, rho_B[k], size=(num_trials, num_steps))

    for t in range(num_steps - 1):
        for k in range(d):
            delta_A[:, t + 1, k] = (
                delta_A[:, t, k] - eta_A[k] * delta_A[:, t, k] + noise_A[:, t, k]
            )
            delta_B[:, t + 1, k] = (
                delta_B[:, t, k] - eta_B[k] * delta_B[:, t, k] + noise_B[:, t, k]
            )

    return delta_A, delta_B


def run_variant_f_anisotropic(
    num_steps: int = 10_000,
    num_trials: int = 300,
    burn_in: int = 2_000,
    seed: int = 42,
) -> Dict:
    """Run the anisotropic correction experiment.

    Three dimensions with different profiles:
      Dim 1: high rho (q=0.2), high eta (0.15) -- well-tracked
      Dim 2: high rho (q=0.2), low eta (0.03)  -- under-tracked (weak dimension)
      Dim 3: low rho  (q=0.02), low eta (0.03) -- doesn't matter much

    Returns dict with per-dimension and aggregate mismatch data.
    """
    # Configuration
    eta_vec = np.array([0.15, 0.03, 0.03])
    q_vec = np.array([0.2, 0.2, 0.02])
    dim_labels = [
        "Dim 1: high $\\rho$, high $\\eta$\n(well-tracked)",
        "Dim 2: high $\\rho$, low $\\eta$\n(under-tracked)",
        "Dim 3: low $\\rho$, low $\\eta$\n(unimportant)",
    ]

    delta = simulate_anisotropic(
        eta_vec=eta_vec, q_vec=q_vec,
        num_steps=num_steps, num_trials=num_trials,
        burn_in=burn_in, seed=seed,
    )

    # Steady-state statistics per dimension
    ss_data = np.abs(delta[:, burn_in:, :])  # (trials, ss_steps, d)

    per_dim_mean = []
    per_dim_theory = []
    for k in range(3):
        trial_means = np.mean(ss_data[:, :, k], axis=1)
        per_dim_mean.append(np.mean(trial_means))
        # Discrete-time AR(1) theory: E[|delta|] = q / sqrt(2*eta - eta^2) * sqrt(2/pi)
        std_k = q_vec[k] / np.sqrt(2 * eta_vec[k] - eta_vec[k] ** 2)
        per_dim_theory.append(std_k * np.sqrt(2 / np.pi))

    # Overall ||delta|| (L2 norm)
    norm_delta = np.sqrt(np.sum(delta[:, burn_in:, :] ** 2, axis=2))  # (trials, ss_steps)
    trial_norm_means = np.mean(norm_delta, axis=1)
    overall_mean = np.mean(trial_norm_means)

    # Scalar tempo prediction: T_scalar = sum(eta_k * nu_k) = sum(eta_k)
    # Scalar rho = sqrt(sum(q_k^2))  [root-sum-of-squares for independent noise]
    T_scalar = np.sum(eta_vec)
    rho_scalar = np.sqrt(np.sum(q_vec ** 2))
    scalar_prediction = rho_scalar / T_scalar

    # Weak-dimension bottleneck prediction: max_k(q_k/eta_k) * sqrt(2/pi)
    per_dim_ratios = q_vec / eta_vec
    bottleneck_dim = np.argmax(per_dim_ratios)
    bottleneck_prediction = per_dim_ratios[bottleneck_dim]

    # Also compare: isotropic case (same total resources, distributed evenly)
    eta_iso = np.mean(eta_vec)
    q_iso_vec = q_vec  # same environment noise
    delta_iso = simulate_anisotropic(
        eta_vec=np.array([eta_iso, eta_iso, eta_iso]),
        q_vec=q_iso_vec,
        num_steps=num_steps, num_trials=num_trials,
        burn_in=burn_in, seed=seed + 100,
    )
    norm_iso = np.sqrt(np.sum(delta_iso[:, burn_in:, :] ** 2, axis=2))
    iso_overall_mean = np.mean(np.mean(norm_iso, axis=1))

    print(f"  Anisotropic results:")
    for k in range(3):
        print(f"    Dim {k+1}: E[|delta_k|] = {per_dim_mean[k]:.4f} "
              f"(theory: {per_dim_theory[k]:.4f}, q/eta = {per_dim_ratios[k]:.2f})")
    print(f"    Overall ||delta|| = {overall_mean:.4f}")
    print(f"    Scalar T prediction (rho/T) = {scalar_prediction:.4f}")
    print(f"    Bottleneck dim = {bottleneck_dim + 1} "
          f"(q/eta = {per_dim_ratios[bottleneck_dim]:.2f})")
    print(f"    Isotropic (same resources) ||delta|| = {iso_overall_mean:.4f}")

    return {
        "eta_vec": eta_vec,
        "q_vec": q_vec,
        "dim_labels": dim_labels,
        "delta": delta,
        "per_dim_mean": np.array(per_dim_mean),
        "per_dim_theory": np.array(per_dim_theory),
        "per_dim_ratios": per_dim_ratios,
        "overall_mean": overall_mean,
        "scalar_prediction": scalar_prediction,
        "bottleneck_dim": bottleneck_dim,
        "bottleneck_prediction": bottleneck_prediction,
        "iso_overall_mean": iso_overall_mean,
        "burn_in": burn_in,
    }


def plot_variant_f_perdim(
    results: Dict,
    save_path: Optional[Path] = None,
):
    """Plot per-dimension mismatch distributions and aggregate norm."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    delta = results["delta"]
    burn_in = results["burn_in"]
    d = 3
    colors_dim = ["#1f77b4", "#d62728", "#2ca02c"]

    # Top row: per-dimension distributions
    for k in range(d):
        ax = axes[k // 2, k % 2] if k < 2 else axes[1, 0]
        ss_k = np.abs(delta[:, burn_in:, k]).ravel()
        clip = np.percentile(ss_k, 99.5)
        ax.hist(ss_k[ss_k < clip], bins=80, density=True,
                alpha=0.7, color=colors_dim[k], edgecolor="white", linewidth=0.3)
        ax.axvline(x=results["per_dim_mean"][k], color=colors_dim[k],
                   linewidth=2, label=f"Mean = {results['per_dim_mean'][k]:.3f}")
        ax.axvline(x=results["per_dim_theory"][k], color="k", linestyle="--",
                   linewidth=2, alpha=0.7, label=f"Theory = {results['per_dim_theory'][k]:.3f}")
        ax.set_title(results["dim_labels"][k], fontsize=10)
        ax.set_xlabel("$|\\delta_k|$")
        ax.set_ylabel("Density")
        ax.legend(fontsize=8)

    # Bottom right: aggregate comparison
    ax = axes[1, 1]
    bar_labels = [
        f"Dim {k+1}\n$q/\\eta$={results['per_dim_ratios'][k]:.1f}"
        for k in range(d)
    ]
    bar_labels += ["$\\|\\delta\\|$\n(L2 norm)", "Scalar\n$\\rho/T$", "Isotropic\n(same res.)"]
    bar_values = list(results["per_dim_mean"]) + [
        results["overall_mean"],
        results["scalar_prediction"],
        results["iso_overall_mean"],
    ]
    bar_colors = colors_dim + ["#ff7f0e", "#9467bd", "#8c564b"]

    bars = ax.bar(range(len(bar_labels)), bar_values, color=bar_colors, alpha=0.8,
                  edgecolor="black", linewidth=0.5)
    ax.set_xticks(range(len(bar_labels)))
    ax.set_xticklabels(bar_labels, fontsize=8)
    ax.set_ylabel("$\\langle|\\delta|\\rangle$ or $\\langle\\|\\delta\\|\\rangle$")
    ax.set_title("Per-Dim vs. Aggregate Mismatch", fontsize=11)

    # Annotate bar values
    for i, v in enumerate(bar_values):
        ax.text(i, v + 0.05, f"{v:.2f}", ha="center", fontsize=8)

    fig.suptitle(
        "Variant F: Anisotropic Correction ($d=3$)\n"
        f"$\\eta = [{', '.join(f'{e:.2f}' for e in results['eta_vec'])}]$, "
        f"$q = [{', '.join(f'{e:.2f}' for e in results['q_vec'])}]$",
        fontsize=13,
    )
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        print(f"  Saved: {save_path}")
    return fig


def run_variant_f_adversarial(
    num_steps: int = 15_000,
    num_trials: int = 200,
    burn_in: int = 4_000,
    seed: int = 42,
) -> Dict:
    """Adversarial anisotropic experiment.

    Agent A is strong (high gain on all dims).
    Agent B has anisotropic gains: strong on dim 1, weak on dim 2.

    Compare:
      (a) Uniform disturbance: adversary distributes equally across dims
      (b) Targeted disturbance: adversary concentrates on B's weak dimension
    """
    d = 3
    eta_A = np.array([0.15, 0.15, 0.15])  # A: isotropic, strong
    eta_B = np.array([0.15, 0.03, 0.03])  # B: anisotropic, weak on dims 2-3

    q_base = 0.05
    gamma = 0.5

    # Uniform disturbance weights
    w_uniform = np.array([1.0, 1.0, 1.0])

    # Targeted disturbance: concentrate on B's weakest dimension (dim 2)
    w_targeted = np.array([0.1, 0.8, 0.1])

    # Run both
    delta_A_unif, delta_B_unif = simulate_anisotropic_adversarial(
        eta_A, eta_B, q_base, gamma, w_uniform,
        num_steps=num_steps, num_trials=num_trials,
        burn_in=burn_in, seed=seed,
    )
    delta_A_targ, delta_B_targ = simulate_anisotropic_adversarial(
        eta_A, eta_B, q_base, gamma, w_targeted,
        num_steps=num_steps, num_trials=num_trials,
        burn_in=burn_in, seed=seed + 200,
    )

    # Compute per-dimension and overall steady-state mismatch for B
    results = {"eta_A": eta_A, "eta_B": eta_B, "q_base": q_base, "gamma": gamma}

    for label, dA, dB in [("uniform", delta_A_unif, delta_B_unif),
                           ("targeted", delta_A_targ, delta_B_targ)]:
        ss_B = np.abs(dB[:, burn_in:, :])
        ss_A = np.abs(dA[:, burn_in:, :])

        per_dim_B = [np.mean(np.mean(ss_B[:, :, k], axis=1)) for k in range(d)]
        per_dim_A = [np.mean(np.mean(ss_A[:, :, k], axis=1)) for k in range(d)]

        norm_B = np.mean(np.sqrt(np.sum(dB[:, burn_in:, :] ** 2, axis=2)), axis=1)
        norm_A = np.mean(np.sqrt(np.sum(dA[:, burn_in:, :] ** 2, axis=2)), axis=1)

        results[f"{label}_per_dim_B"] = np.array(per_dim_B)
        results[f"{label}_per_dim_A"] = np.array(per_dim_A)
        results[f"{label}_norm_B"] = np.mean(norm_B)
        results[f"{label}_norm_A"] = np.mean(norm_A)
        results[f"{label}_ratio"] = np.median(norm_B / norm_A)

        print(f"  {label} disturbance:")
        for k in range(d):
            print(f"    Dim {k+1}: B={per_dim_B[k]:.4f}, A={per_dim_A[k]:.4f}, "
                  f"ratio={per_dim_B[k]/max(per_dim_A[k],1e-12):.2f}")
        print(f"    Overall ||delta_B||/||delta_A|| = {results[f'{label}_ratio']:.3f}")

    return results


def plot_variant_f_adversarial(
    results: Dict,
    save_path: Optional[Path] = None,
):
    """Plot adversarial anisotropic results: uniform vs targeted disturbance."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    d = 3

    # Left: per-dimension mismatch for B under both strategies
    x = np.arange(d)
    width = 0.35
    ax1.bar(x - width / 2, results["uniform_per_dim_B"], width, color="#1f77b4",
            alpha=0.8, label="B: uniform disturbance")
    ax1.bar(x + width / 2, results["targeted_per_dim_B"], width, color="#d62728",
            alpha=0.8, label="B: targeted disturbance")

    # Overlay A's mismatch for reference
    ax1.bar(x - width / 2, results["uniform_per_dim_A"], width, color="#1f77b4",
            alpha=0.25, edgecolor="#1f77b4", linewidth=2, linestyle="--",
            label="A: uniform (reference)")

    ax1.set_xticks(x)
    eta_B = results["eta_B"]
    ax1.set_xticklabels([
        f"Dim {k+1}\n$\\eta_B={eta_B[k]:.2f}$" for k in range(d)
    ], fontsize=9)
    ax1.set_ylabel("Steady-state $\\langle|\\delta_k|\\rangle$")
    ax1.set_title("Per-Dimension Mismatch: Agent B")
    ax1.legend(fontsize=9)

    # Right: overall mismatch ratio
    categories = ["Uniform\ndisturbance", "Targeted\n(dim 2)"]
    B_norms = [results["uniform_norm_B"], results["targeted_norm_B"]]
    A_norms = [results["uniform_norm_A"], results["targeted_norm_A"]]
    ratios = [results["uniform_ratio"], results["targeted_ratio"]]

    x2 = np.arange(2)
    ax2.bar(x2 - 0.2, B_norms, 0.35, color="#d62728", alpha=0.8, label="Agent B")
    ax2.bar(x2 + 0.2, A_norms, 0.35, color="#1f77b4", alpha=0.8, label="Agent A")
    ax2.set_xticks(x2)
    ax2.set_xticklabels(categories, fontsize=10)
    ax2.set_ylabel("$\\langle\\|\\delta\\|\\rangle$")
    ax2.set_title("Overall Mismatch: Uniform vs. Targeted Attack")
    ax2.legend(fontsize=9)

    # Annotate with ratios
    for i, r in enumerate(ratios):
        y_pos = max(B_norms[i], A_norms[i]) + 0.1
        ax2.text(i, y_pos, f"B/A = {r:.2f}", ha="center", fontsize=10, fontweight="bold")

    # Compute amplification factor
    amp = results["targeted_ratio"] / max(results["uniform_ratio"], 1e-12)
    ax2.text(0.5, 0.95, f"Targeted amplification: {amp:.2f}x",
             transform=ax2.transAxes, ha="center", fontsize=11,
             bbox=dict(boxstyle="round,pad=0.3", facecolor="wheat", alpha=0.5))

    fig.suptitle(
        "Variant F: Adversarial Anisotropy\n"
        f"A: isotropic $\\eta={results['eta_A'][0]:.2f}$, "
        f"B: anisotropic $\\eta=[{', '.join(f'{e:.2f}' for e in results['eta_B'])}]$",
        fontsize=13,
    )
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        print(f"  Saved: {save_path}")
    return fig


# ===================================================================
# Main
# ===================================================================

def main():
    print("=" * 70)
    print("VARIANT E: Observation Noise")
    print("=" * 70)

    eta_fixed = 0.1
    q_env = 0.1

    # --- E1: Steady-state vs sigma_obs ---
    print("\n--- E1: Steady-state mismatch vs observation noise ---")
    sigma_obs_values = np.array([0.0, 0.02, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.7, 1.0])
    e1_results = run_variant_e_sweep(
        sigma_obs_values, eta_fixed=eta_fixed, q_env=q_env,
        num_steps=10_000, num_trials=200, burn_in=2_000, seed=42,
    )
    fig_e1 = plot_variant_e_steadystate(
        e1_results, eta_fixed, q_env,
        save_path=FIGURE_DIR / "varE_fig1_steadystate_vs_obs_noise.png",
    )

    # --- E2: Gain validation ---
    print("\n--- E2: Optimal gain validation ---")
    fig_e2 = plot_variant_e_gain_validation(
        sigma_obs_values, eta_fixed, q_env,
        save_path=FIGURE_DIR / "varE_fig2_gain_validation.png",
    )

    # --- E3: Adversarial exponent vs sigma_obs ---
    print("\n--- E3: Adversarial exponent vs observation noise ---")
    sigma_obs_adv = np.array([0.0, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0])
    tempo_ratios_adv = np.logspace(np.log10(0.5), np.log10(4.0), 12)
    e3_results = run_variant_e_adversarial(
        sigma_obs_adv, tempo_ratios_adv,
        eta_fixed=0.1, q_env=0.05, gamma=0.5,
        num_steps=15_000, num_trials=150, burn_in=4_000, seed=42,
    )
    fig_e3 = plot_variant_e_adversarial(
        e3_results,
        save_path=FIGURE_DIR / "varE_fig3_adversarial_exponent.png",
    )

    print("\n" + "=" * 70)
    print("VARIANT F: Multi-Dimensional Anisotropic Correction")
    print("=" * 70)

    # --- F1: Anisotropic correction ---
    print("\n--- F1: Per-dimension mismatch with anisotropic gains ---")
    f1_results = run_variant_f_anisotropic(
        num_steps=10_000, num_trials=300, burn_in=2_000, seed=42,
    )
    fig_f1 = plot_variant_f_perdim(
        f1_results,
        save_path=FIGURE_DIR / "varF_fig1_anisotropic_perdim.png",
    )

    # --- F2: Adversarial with targeted attack ---
    print("\n--- F2: Adversarial with targeted vs uniform disturbance ---")
    f2_results = run_variant_f_adversarial(
        num_steps=15_000, num_trials=200, burn_in=4_000, seed=42,
    )
    fig_f2 = plot_variant_f_adversarial(
        f2_results,
        save_path=FIGURE_DIR / "varF_fig2_adversarial_targeted.png",
    )

    # --- Print final summary ---
    print("\n" + "=" * 70)
    print("FINAL SUMMARY")
    print("=" * 70)

    print("\n  VARIANT E: Observation Noise")
    print("  " + "-" * 50)
    print(f"  At sigma_obs=0 (no noise):    SS = {e1_results['ss_fixed'][0]:.4f}")
    print(f"  At sigma_obs=0.5 (moderate):  SS_fixed = {e1_results['ss_fixed'][8]:.4f}, "
          f"SS_optimal = {e1_results['ss_optimal'][8]:.4f}")
    high_idx = -1
    print(f"  At sigma_obs=1.0 (heavy):     SS_fixed = {e1_results['ss_fixed'][high_idx]:.4f}, "
          f"SS_optimal = {e1_results['ss_optimal'][high_idx]:.4f}")
    improvement = (1 - e1_results['ss_optimal'][high_idx] / e1_results['ss_fixed'][high_idx]) * 100
    print(f"  Optimal gain improvement at sigma_obs=1.0: {improvement:.1f}%")

    print(f"\n  Adversarial exponents:")
    for i, s in enumerate(sigma_obs_adv):
        print(f"    sigma_obs={s:.2f}: "
              f"fixed={e3_results['exp_fixed'][i]:.3f}, "
              f"optimal={e3_results['exp_optimal'][i]:.3f}")

    print(f"\n  VARIANT F: Anisotropic Correction")
    print("  " + "-" * 50)
    print(f"  Per-dimension E[|delta_k|]:")
    for k in range(3):
        print(f"    Dim {k+1}: simulated={f1_results['per_dim_mean'][k]:.4f}, "
              f"theory={f1_results['per_dim_theory'][k]:.4f}, "
              f"q/eta={f1_results['per_dim_ratios'][k]:.2f}")
    print(f"  Overall ||delta|| = {f1_results['overall_mean']:.4f}")
    print(f"  Scalar rho/T prediction = {f1_results['scalar_prediction']:.4f}")
    print(f"  Isotropic (same resources) = {f1_results['iso_overall_mean']:.4f}")
    print(f"  Bottleneck dimension: {f1_results['bottleneck_dim'] + 1}")

    print(f"\n  Adversarial (targeted vs uniform):")
    print(f"    Uniform B/A ratio:  {f2_results['uniform_ratio']:.3f}")
    print(f"    Targeted B/A ratio: {f2_results['targeted_ratio']:.3f}")
    amp = f2_results['targeted_ratio'] / max(f2_results['uniform_ratio'], 1e-12)
    print(f"    Targeted amplification: {amp:.2f}x")

    print(f"\nDone. Figures saved to: {FIGURE_DIR}")


if __name__ == "__main__":
    main()
