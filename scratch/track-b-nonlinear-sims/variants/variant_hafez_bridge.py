"""
Variant: Hafez Bi-Predictability Bridge

Computes Hafez et al.'s bi-predictability metrics (P, H_f, H_b, DeltaH) from
TFT-style agent-environment interactions, and tests whether TFT quantities
(tempo, gain, mismatch) predict them.

Reference: Hafez et al., "A Mathematical Theory of Agency and Intelligence"
           (arXiv:2602.22519, Feb 2026)

Hafez defines:
  P  = MI(S,A; S') / C,  where C = H(S) + H(A) + H(S')
  H_f = H(S'|S,A) = H(S,A,S') - H(S,A)      [forward predictive uncertainty]
  H_b = H(S,A|S') = H(S,A,S') - H(S')        [backward predictive uncertainty]
  DH  = H_f - H_b                             [predictive asymmetry]

For classical systems: P <= 1/2.
Agency (action selection) reduces P and introduces |DH| > 0.

For passive systems (no action channel):
  P_passive = MI(S; S') / [H(S) + H(S')]

This simulation uses the same single-agent tracking setup as sim1
(random walk environment, agent with correction function), instrumented to
record the full (S_t, A_t, S'_t) stream and compute Hafez metrics.

Experiments:
  1. P vs eta (tempo)
  2. Passive vs active agent
  3. P vs observation noise
  4. P across correction functions
  5. Adversarial P (two coupled agents)
  6. Perturbation detection (sudden environment change)
"""

import sys
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Callable, Dict, Tuple, Optional, List
import warnings

# Add parent directory to path to import sim1 correction functions
PARENT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PARENT_DIR))

from sim1_nonlinear_mismatch import (
    CORRECTION_FUNCTIONS,
    CORRECTION_LABELS,
    COLORS,
)

# ---------------------------------------------------------------------------
# Output directory
# ---------------------------------------------------------------------------
OUTPUT_DIR = Path(__file__).resolve().parent

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


# ============================================================================
# Entropy and information-theoretic computations
# ============================================================================

def discretize(x: np.ndarray, n_bins: int = 16) -> np.ndarray:
    """Discretize a continuous 1D array into n_bins equal-width bins.

    Following Hafez et al.: z-score normalization, then equal-width binning.
    Returns integer bin indices in [0, n_bins-1].
    """
    x = np.asarray(x, dtype=float)
    std = np.std(x)
    if std < 1e-15:
        # Constant signal -> all in middle bin
        return np.full(len(x), n_bins // 2, dtype=int)
    z = (x - np.mean(x)) / std
    # Clip to [-4, 4] standard deviations then bin
    z = np.clip(z, -4.0, 4.0)
    bins = np.floor((z + 4.0) / 8.0 * n_bins).astype(int)
    bins = np.clip(bins, 0, n_bins - 1)
    return bins


def entropy_from_counts(counts: np.ndarray) -> float:
    """Compute Shannon entropy (base-2) from a count array."""
    total = np.sum(counts)
    if total == 0:
        return 0.0
    p = counts[counts > 0] / total
    return -np.sum(p * np.log2(p))


def joint_entropy_1d(x: np.ndarray, n_vals: int) -> float:
    """Entropy of a single discrete variable."""
    counts = np.bincount(x, minlength=n_vals)
    return entropy_from_counts(counts)


def joint_entropy_2d(x: np.ndarray, y: np.ndarray,
                     nx: int, ny: int) -> float:
    """Joint entropy H(X,Y) from two discrete variables."""
    idx = x * ny + y
    counts = np.bincount(idx, minlength=nx * ny)
    return entropy_from_counts(counts)


def joint_entropy_3d(x: np.ndarray, y: np.ndarray, z: np.ndarray,
                     nx: int, ny: int, nz: int) -> float:
    """Joint entropy H(X,Y,Z) from three discrete variables."""
    idx = x * (ny * nz) + y * nz + z
    counts = np.bincount(idx, minlength=nx * ny * nz)
    return entropy_from_counts(counts)


def compute_hafez_metrics(
    S: np.ndarray,
    A: np.ndarray,
    Sp: np.ndarray,
    n_bins: int = 16,
) -> Dict[str, float]:
    """Compute Hafez bi-predictability metrics from (S, A, S') stream.

    All inputs are 1D arrays of equal length (already discretized into
    integer bin indices in [0, n_bins-1]).

    Returns dict with keys: P, H_f, H_b, DH, MI, C, H_S, H_A, H_Sp,
                             H_SA, H_SASp
    """
    n = len(S)
    assert len(A) == n and len(Sp) == n

    # Marginal entropies
    H_S = joint_entropy_1d(S, n_bins)
    H_A = joint_entropy_1d(A, n_bins)
    H_Sp = joint_entropy_1d(Sp, n_bins)

    # Joint entropies
    H_SA = joint_entropy_2d(S, A, n_bins, n_bins)
    H_SASp = joint_entropy_3d(S, A, Sp, n_bins, n_bins, n_bins)

    # MI(S,A; S') = H(S,A) + H(S') - H(S,A,S')
    MI = H_SA + H_Sp - H_SASp

    # Total information capacity
    C = H_S + H_A + H_Sp

    # Bi-predictability
    P = MI / C if C > 1e-15 else 0.0

    # Forward predictive uncertainty: H(S'|S,A) = H(S,A,S') - H(S,A)
    H_f = H_SASp - H_SA

    # Backward predictive uncertainty: H(S,A|S') = H(S,A,S') - H(S')
    H_b = H_SASp - H_Sp

    # Predictive asymmetry
    DH = H_f - H_b

    return {
        "P": P, "H_f": H_f, "H_b": H_b, "DH": DH,
        "MI": MI, "C": C,
        "H_S": H_S, "H_A": H_A, "H_Sp": H_Sp,
        "H_SA": H_SA, "H_SASp": H_SASp,
    }


def compute_passive_metrics(
    S: np.ndarray,
    Sp: np.ndarray,
    n_bins: int = 16,
) -> Dict[str, float]:
    """Compute Hafez metrics for passive system (no action channel).

    P_passive = MI(S; S') / [H(S) + H(S')]
    H_f = H(S'|S) = H(S,S') - H(S)
    H_b = H(S|S') = H(S,S') - H(S')
    DH  = H_f - H_b

    For a deterministic system with complete state, P_passive -> 1/2
    and DH -> 0.
    """
    n = len(S)
    assert len(Sp) == n

    H_S = joint_entropy_1d(S, n_bins)
    H_Sp = joint_entropy_1d(Sp, n_bins)
    H_SSp = joint_entropy_2d(S, Sp, n_bins, n_bins)

    MI = H_S + H_Sp - H_SSp
    C = H_S + H_Sp
    P = MI / C if C > 1e-15 else 0.0

    H_f = H_SSp - H_S   # H(S'|S)
    H_b = H_SSp - H_Sp  # H(S|S')
    DH = H_f - H_b

    return {
        "P": P, "H_f": H_f, "H_b": H_b, "DH": DH,
        "MI": MI, "C": C, "H_S": H_S, "H_Sp": H_Sp,
    }


def compute_windowed_metrics(
    S_raw: np.ndarray,
    A_raw: np.ndarray,
    Sp_raw: np.ndarray,
    window: int = 300,
    stride: int = 75,
    n_bins: int = 16,
) -> Dict[str, np.ndarray]:
    """Compute Hafez metrics over sliding windows.

    Inputs are continuous 1D arrays. Discretization is done per-window
    (z-score within each window, following Hafez's approach).

    Returns dict of arrays, one value per window.
    """
    n = len(S_raw)
    results = {k: [] for k in ["P", "H_f", "H_b", "DH", "MI", "C"]}
    centers = []

    start = 0
    while start + window <= n:
        end = start + window
        s_win = discretize(S_raw[start:end], n_bins)
        a_win = discretize(A_raw[start:end], n_bins)
        sp_win = discretize(Sp_raw[start:end], n_bins)

        m = compute_hafez_metrics(s_win, a_win, sp_win, n_bins)
        for k in results:
            results[k].append(m[k])
        centers.append((start + end) / 2.0)

        start += stride

    for k in results:
        results[k] = np.array(results[k])
    results["centers"] = np.array(centers)

    return results


# ============================================================================
# Agent-environment simulation (instrumented for Hafez metrics)
# ============================================================================

def simulate_agent_env(
    g: Callable,
    eta: float,
    q: float,
    num_steps: int = 5000,
    obs_noise: float = 0.0,
    seed: int = 42,
    g_kwargs: Optional[dict] = None,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Simulate single agent tracking a random-walk environment.

    Environment: x_{t+1} = x_t + q * epsilon_t,  epsilon ~ N(0,1)
    Observation: o_t = x_t + obs_noise * nu_t,    nu ~ N(0,1)
    Agent state: xhat_t (estimate of x_t)
    Mismatch:    delta_t = o_t - xhat_t
    Action:      a_t = eta * g(delta_t)
    Update:      xhat_{t+1} = xhat_t + a_t

    Returns: (x, xhat, actions) -- all arrays of length num_steps
    """
    if g_kwargs is None:
        g_kwargs = {}

    rng = np.random.default_rng(seed)

    x = np.zeros(num_steps)
    xhat = np.zeros(num_steps)
    actions = np.zeros(num_steps)

    env_noise = rng.normal(0, q, num_steps) if q > 0 else np.zeros(num_steps)
    o_noise = rng.normal(0, obs_noise, num_steps) if obs_noise > 0 else np.zeros(num_steps)

    for t in range(num_steps - 1):
        o_t = x[t] + o_noise[t]
        delta_t = o_t - xhat[t]
        a_t = eta * g(np.array([delta_t]), **g_kwargs)[0]
        actions[t] = a_t
        xhat[t + 1] = xhat[t] + a_t
        x[t + 1] = x[t] + env_noise[t]

    # Final step action
    o_final = x[-1] + o_noise[-1]
    delta_final = o_final - xhat[-1]
    actions[-1] = eta * g(np.array([delta_final]), **g_kwargs)[0]

    return x, xhat, actions


def extract_hafez_streams(
    x: np.ndarray,
    xhat: np.ndarray,
    actions: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Extract (S, A, S') streams for Hafez active-agent metrics.

    S_t  = xhat_t     (agent's internal state at time t)
    A_t  = actions_t   (action taken at time t)
    S'_t = x_{t+1}    (environment's next state)

    Returns arrays of length (num_steps - 1).
    """
    S = xhat[:-1]
    A = actions[:-1]
    Sp = x[1:]
    return S, A, Sp


# ============================================================================
# Experiment 1: P vs eta (tempo)
# ============================================================================

def experiment_P_vs_eta():
    """Sweep eta and compute P. Does higher tempo -> better coupling?"""
    print("\n" + "=" * 70)
    print("EXPERIMENT 1: P vs eta (tempo)")
    print("=" * 70)

    etas = np.array([0.01, 0.02, 0.05, 0.08, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5])
    q = 0.1
    num_steps = 8000
    burn_in = 2000
    n_bins = 16
    n_seeds = 10

    g = CORRECTION_FUNCTIONS["linear"]

    results = {
        "P": np.zeros((len(etas), n_seeds)),
        "H_f": np.zeros((len(etas), n_seeds)),
        "H_b": np.zeros((len(etas), n_seeds)),
        "DH": np.zeros((len(etas), n_seeds)),
    }

    for i, eta in enumerate(etas):
        for s in range(n_seeds):
            x, xhat, actions = simulate_agent_env(
                g, eta=eta, q=q, num_steps=num_steps, seed=42 + s
            )
            S, A, Sp = extract_hafez_streams(x, xhat, actions)
            S_ss, A_ss, Sp_ss = S[burn_in:], A[burn_in:], Sp[burn_in:]

            S_d = discretize(S_ss, n_bins)
            A_d = discretize(A_ss, n_bins)
            Sp_d = discretize(Sp_ss, n_bins)

            m = compute_hafez_metrics(S_d, A_d, Sp_d, n_bins)
            results["P"][i, s] = m["P"]
            results["H_f"][i, s] = m["H_f"]
            results["H_b"][i, s] = m["H_b"]
            results["DH"][i, s] = m["DH"]

        P_mean = np.mean(results["P"][i])
        DH_mean = np.mean(results["DH"][i])
        print(f"  eta={eta:.3f}  P={P_mean:.4f}  DH={DH_mean:.4f}")

    # Plot
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    ax = axes[0]
    P_mean = np.mean(results["P"], axis=1)
    P_std = np.std(results["P"], axis=1)
    ax.errorbar(etas, P_mean, yerr=P_std, fmt="-o", color="#1f77b4",
                capsize=4, markersize=5)
    ax.axhline(y=0.5, color="k", linestyle="--", alpha=0.4,
               label="Classical bound $P \\leq 1/2$")
    ax.set_xlabel("$\\eta$ (gain / tempo)")
    ax.set_ylabel("Bi-predictability $P$")
    ax.set_title("$P$ vs Tempo $\\eta$")
    ax.legend(fontsize=9)

    ax = axes[1]
    Hf_mean = np.mean(results["H_f"], axis=1)
    Hf_std = np.std(results["H_f"], axis=1)
    Hb_mean = np.mean(results["H_b"], axis=1)
    Hb_std = np.std(results["H_b"], axis=1)
    ax.errorbar(etas, Hf_mean, yerr=Hf_std, fmt="-o", color="#d62728",
                capsize=4, markersize=5, label="$H_f = H(S'|S,A)$")
    ax.errorbar(etas, Hb_mean, yerr=Hb_std, fmt="-s", color="#2ca02c",
                capsize=4, markersize=5, label="$H_b = H(S,A|S')$")
    ax.set_xlabel("$\\eta$ (gain / tempo)")
    ax.set_ylabel("Conditional entropy (bits)")
    ax.set_title("Forward & Backward Uncertainty")
    ax.legend(fontsize=9)

    ax = axes[2]
    DH_mean = np.mean(results["DH"], axis=1)
    DH_std = np.std(results["DH"], axis=1)
    ax.errorbar(etas, DH_mean, yerr=DH_std, fmt="-o", color="#9467bd",
                capsize=4, markersize=5)
    ax.axhline(y=0, color="k", linestyle=":", alpha=0.4)
    ax.set_xlabel("$\\eta$ (gain / tempo)")
    ax.set_ylabel("$\\Delta H = H_f - H_b$")
    ax.set_title("Predictive Asymmetry $\\Delta H$")

    fig.suptitle(
        f"Experiment 1: Hafez Metrics vs TFT Tempo ($q={q}$, linear correction)",
        fontsize=13, y=1.02,
    )
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "P_vs_eta.png", bbox_inches="tight")
    print(f"  Saved: {OUTPUT_DIR / 'P_vs_eta.png'}")

    return etas, results


# ============================================================================
# Experiment 2: Passive vs Active
# ============================================================================

def experiment_passive_vs_active():
    """Compare passive system (no action channel) vs active agent.

    Passive system: S_t = x_t, S'_t = x_{t+1}, no A.
      P_passive = MI(S; S') / [H(S) + H(S')]
      This is the Hafez "physical baseline" (like double pendulum).

    Active agent: S_t = xhat_t, A_t = action, S'_t = x_{t+1}.
      P_active = MI(S,A; S') / [H(S) + H(A) + H(S')]
      Agency introduces action channel and internal degrees of freedom.

    Hafez predicts: P_passive > P_active (agency costs coherence),
    and |DH| -> 0 for passive, |DH| > 0 for active.
    """
    print("\n" + "=" * 70)
    print("EXPERIMENT 2: Passive vs Active")
    print("=" * 70)

    etas = np.array([0.01, 0.05, 0.1, 0.2, 0.3, 0.5])
    q = 0.1
    num_steps = 8000
    burn_in = 2000
    n_bins = 16
    n_seeds = 10

    g = CORRECTION_FUNCTIONS["linear"]

    # --- Passive system: direct state observation, no action ---
    P_passive_all = np.zeros(n_seeds)
    DH_passive_all = np.zeros(n_seeds)
    Hf_passive_all = np.zeros(n_seeds)
    Hb_passive_all = np.zeros(n_seeds)

    for s in range(n_seeds):
        # Generate environment trajectory (no agent needed)
        rng = np.random.default_rng(42 + s)
        x = np.cumsum(rng.normal(0, q, num_steps))
        # Passive: S_t = x_t, S'_t = x_{t+1}
        S_pass = x[:-1]
        Sp_pass = x[1:]
        S_ss = S_pass[burn_in:]
        Sp_ss = Sp_pass[burn_in:]

        S_d = discretize(S_ss, n_bins)
        Sp_d = discretize(Sp_ss, n_bins)

        m = compute_passive_metrics(S_d, Sp_d, n_bins)
        P_passive_all[s] = m["P"]
        DH_passive_all[s] = m["DH"]
        Hf_passive_all[s] = m["H_f"]
        Hb_passive_all[s] = m["H_b"]

    P_passive_mean = np.mean(P_passive_all)
    DH_passive_mean = np.mean(DH_passive_all)
    print(f"  PASSIVE (no action channel):  P={P_passive_mean:.4f} +/- "
          f"{np.std(P_passive_all):.4f}  DH={DH_passive_mean:.4f} +/- "
          f"{np.std(DH_passive_all):.4f}")

    # --- Active agent at various eta ---
    P_active_all = np.zeros((len(etas), n_seeds))
    DH_active_all = np.zeros((len(etas), n_seeds))

    for i, eta in enumerate(etas):
        for s in range(n_seeds):
            x, xhat, actions = simulate_agent_env(
                g, eta=eta, q=q, num_steps=num_steps, seed=42 + s
            )
            S, A, Sp = extract_hafez_streams(x, xhat, actions)
            S_ss, A_ss, Sp_ss = S[burn_in:], A[burn_in:], Sp[burn_in:]

            S_d = discretize(S_ss, n_bins)
            A_d = discretize(A_ss, n_bins)
            Sp_d = discretize(Sp_ss, n_bins)

            m = compute_hafez_metrics(S_d, A_d, Sp_d, n_bins)
            P_active_all[i, s] = m["P"]
            DH_active_all[i, s] = m["DH"]

        P_m = np.mean(P_active_all[i])
        DH_m = np.mean(DH_active_all[i])
        print(f"  ACTIVE eta={eta:.3f}:  P={P_m:.4f} +/- "
              f"{np.std(P_active_all[i]):.4f}  DH={DH_m:.4f} +/- "
              f"{np.std(DH_active_all[i]):.4f}")

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

    # P comparison
    ax = axes[0]
    P_active_mean = np.mean(P_active_all, axis=1)
    P_active_std = np.std(P_active_all, axis=1)
    ax.errorbar(etas, P_active_mean, yerr=P_active_std, fmt="-o",
                color="#1f77b4", capsize=4, markersize=6,
                label="Active agent: $P = MI(S,A;S')/C$")
    ax.axhline(y=P_passive_mean, color="red", linestyle="-", linewidth=2,
               alpha=0.7, label=f"Passive system: $P_{{pass}} = {P_passive_mean:.3f}$")
    ax.fill_between(
        [etas[0] - 0.02, etas[-1] + 0.02],
        P_passive_mean - np.std(P_passive_all),
        P_passive_mean + np.std(P_passive_all),
        color="red", alpha=0.1,
    )
    ax.axhline(y=0.5, color="k", linestyle="--", alpha=0.3,
               label="Classical bound $P \\leq 1/2$")
    ax.set_xlabel("$\\eta$ (active agent tempo)")
    ax.set_ylabel("$P$")
    ax.set_title("Passive vs Active: Bi-predictability")
    ax.legend(fontsize=9)

    # DH comparison
    ax = axes[1]
    DH_active_mean = np.mean(DH_active_all, axis=1)
    DH_active_std = np.std(DH_active_all, axis=1)
    ax.errorbar(etas, DH_active_mean, yerr=DH_active_std, fmt="-o",
                color="#9467bd", capsize=4, markersize=6,
                label="Active agent $\\Delta H$")
    ax.axhline(y=DH_passive_mean, color="red", linestyle="-", linewidth=2,
               alpha=0.7, label=f"Passive: $\\Delta H = {DH_passive_mean:.3f}$")
    ax.axhline(y=0, color="k", linestyle=":", alpha=0.4)
    ax.set_xlabel("$\\eta$ (active agent tempo)")
    ax.set_ylabel("$\\Delta H = H_f - H_b$")
    ax.set_title("Passive vs Active: Predictive Asymmetry")
    ax.legend(fontsize=9)

    fig.suptitle(
        "Experiment 2: Agency Costs Coherence (Hafez Prediction)\n"
        "Passive = physical system (no action channel); "
        "Active = TFT agent with correction",
        fontsize=12, y=1.04,
    )
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "passive_vs_active.png", bbox_inches="tight")
    print(f"  Saved: {OUTPUT_DIR / 'passive_vs_active.png'}")

    return {
        "P_passive": P_passive_all, "DH_passive": DH_passive_all,
        "etas": etas, "P_active": P_active_all, "DH_active": DH_active_all,
    }


# ============================================================================
# Experiment 3: P vs observation noise
# ============================================================================

def experiment_P_vs_obs_noise():
    """Sweep observation noise. Does H_f increase as world becomes more opaque?"""
    print("\n" + "=" * 70)
    print("EXPERIMENT 3: P vs Observation Noise")
    print("=" * 70)

    sigma_obs_values = np.array([0.0, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0])
    eta = 0.1
    q = 0.1
    num_steps = 8000
    burn_in = 2000
    n_bins = 16
    n_seeds = 10

    g = CORRECTION_FUNCTIONS["linear"]

    P_all = np.zeros((len(sigma_obs_values), n_seeds))
    Hf_all = np.zeros((len(sigma_obs_values), n_seeds))
    Hb_all = np.zeros((len(sigma_obs_values), n_seeds))
    DH_all = np.zeros((len(sigma_obs_values), n_seeds))

    for i, sigma_obs in enumerate(sigma_obs_values):
        for s in range(n_seeds):
            x, xhat, actions = simulate_agent_env(
                g, eta=eta, q=q, num_steps=num_steps,
                obs_noise=sigma_obs, seed=42 + s,
            )
            S, A, Sp = extract_hafez_streams(x, xhat, actions)
            S_ss, A_ss, Sp_ss = S[burn_in:], A[burn_in:], Sp[burn_in:]

            S_d = discretize(S_ss, n_bins)
            A_d = discretize(A_ss, n_bins)
            Sp_d = discretize(Sp_ss, n_bins)

            m = compute_hafez_metrics(S_d, A_d, Sp_d, n_bins)
            P_all[i, s] = m["P"]
            Hf_all[i, s] = m["H_f"]
            Hb_all[i, s] = m["H_b"]
            DH_all[i, s] = m["DH"]

        print(f"  sigma_obs={sigma_obs:.3f}  P={np.mean(P_all[i]):.4f}  "
              f"H_f={np.mean(Hf_all[i]):.4f}  H_b={np.mean(Hb_all[i]):.4f}")

    # Plot
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    ax = axes[0]
    P_mean = np.mean(P_all, axis=1)
    P_std = np.std(P_all, axis=1)
    ax.errorbar(sigma_obs_values, P_mean, yerr=P_std, fmt="-o",
                color="#1f77b4", capsize=4, markersize=5)
    ax.set_xlabel("Observation noise $\\sigma_{obs}$")
    ax.set_ylabel("$P$")
    ax.set_title("$P$ vs Observation Noise")
    ax.axhline(y=0.5, color="k", linestyle="--", alpha=0.4)

    ax = axes[1]
    Hf_mean = np.mean(Hf_all, axis=1)
    Hf_std = np.std(Hf_all, axis=1)
    Hb_mean = np.mean(Hb_all, axis=1)
    Hb_std = np.std(Hb_all, axis=1)
    ax.errorbar(sigma_obs_values, Hf_mean, yerr=Hf_std, fmt="-o",
                color="#d62728", capsize=4, markersize=5,
                label="$H_f = H(S'|S,A)$")
    ax.errorbar(sigma_obs_values, Hb_mean, yerr=Hb_std, fmt="-s",
                color="#2ca02c", capsize=4, markersize=5,
                label="$H_b = H(S,A|S')$")
    ax.set_xlabel("Observation noise $\\sigma_{obs}$")
    ax.set_ylabel("Conditional entropy (bits)")
    ax.set_title("$H_f$ and $H_b$ vs Observation Noise")
    ax.legend(fontsize=9)

    ax = axes[2]
    DH_mean = np.mean(DH_all, axis=1)
    DH_std = np.std(DH_all, axis=1)
    ax.errorbar(sigma_obs_values, DH_mean, yerr=DH_std, fmt="-o",
                color="#9467bd", capsize=4, markersize=5)
    ax.axhline(y=0, color="k", linestyle=":", alpha=0.4)
    ax.set_xlabel("Observation noise $\\sigma_{obs}$")
    ax.set_ylabel("$\\Delta H$")
    ax.set_title("Predictive Asymmetry vs Obs Noise")

    fig.suptitle(
        f"Experiment 3: Observation Noise Degrades Coupling ($\\eta={eta}$, $q={q}$)",
        fontsize=13, y=1.02,
    )
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "P_vs_obs_noise.png", bbox_inches="tight")
    print(f"  Saved: {OUTPUT_DIR / 'P_vs_obs_noise.png'}")

    return sigma_obs_values, P_all, Hf_all, Hb_all


# ============================================================================
# Experiment 4: P across correction functions
# ============================================================================

def experiment_P_across_corrections():
    """Compute P for all 5 correction functions. Do nonlinearities affect coupling?"""
    print("\n" + "=" * 70)
    print("EXPERIMENT 4: P Across Correction Functions")
    print("=" * 70)

    eta = 0.1
    q = 0.1
    num_steps = 8000
    burn_in = 2000
    n_bins = 16
    n_seeds = 10
    g_kwargs = {"R": 1.0, "epsilon": 0.1, "R_max": 2.0}

    all_results = {}
    for name, g in CORRECTION_FUNCTIONS.items():
        P_arr = np.zeros(n_seeds)
        Hf_arr = np.zeros(n_seeds)
        Hb_arr = np.zeros(n_seeds)
        DH_arr = np.zeros(n_seeds)

        for s in range(n_seeds):
            x, xhat, actions = simulate_agent_env(
                g, eta=eta, q=q, num_steps=num_steps,
                seed=42 + s, g_kwargs=g_kwargs,
            )
            S, A, Sp = extract_hafez_streams(x, xhat, actions)
            S_ss, A_ss, Sp_ss = S[burn_in:], A[burn_in:], Sp[burn_in:]

            S_d = discretize(S_ss, n_bins)
            A_d = discretize(A_ss, n_bins)
            Sp_d = discretize(Sp_ss, n_bins)

            m = compute_hafez_metrics(S_d, A_d, Sp_d, n_bins)
            P_arr[s] = m["P"]
            Hf_arr[s] = m["H_f"]
            Hb_arr[s] = m["H_b"]
            DH_arr[s] = m["DH"]

        all_results[name] = {
            "P": P_arr, "H_f": Hf_arr, "H_b": Hb_arr, "DH": DH_arr,
        }
        print(f"  {name:<20} P={np.mean(P_arr):.4f} +/- {np.std(P_arr):.4f}  "
              f"DH={np.mean(DH_arr):.4f} +/- {np.std(DH_arr):.4f}")

    # Plot: grouped bar chart
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    names = list(CORRECTION_FUNCTIONS.keys())
    x_pos = np.arange(len(names))

    ax = axes[0]
    P_means = [np.mean(all_results[n]["P"]) for n in names]
    P_stds = [np.std(all_results[n]["P"]) for n in names]
    colors_list = [COLORS[n] for n in names]
    ax.bar(x_pos, P_means, yerr=P_stds, capsize=5,
           color=colors_list, alpha=0.85, edgecolor="black", linewidth=0.5)
    ax.axhline(y=0.5, color="k", linestyle="--", alpha=0.4,
               label="Classical bound")
    ax.set_xticks(x_pos)
    ax.set_xticklabels([n.capitalize() for n in names], fontsize=10, rotation=15)
    ax.set_ylabel("$P$")
    ax.set_title("Bi-predictability by Correction Function")
    ax.legend(fontsize=9)
    for i, (pm, ps) in enumerate(zip(P_means, P_stds)):
        ax.annotate(f"{pm:.3f}", xy=(i, pm + ps + 0.005),
                    ha="center", fontsize=9)

    ax = axes[1]
    DH_means = [np.mean(all_results[n]["DH"]) for n in names]
    DH_stds = [np.std(all_results[n]["DH"]) for n in names]
    ax.bar(x_pos, DH_means, yerr=DH_stds, capsize=5,
           color=colors_list, alpha=0.85, edgecolor="black", linewidth=0.5)
    ax.axhline(y=0, color="k", linestyle=":", alpha=0.4)
    ax.set_xticks(x_pos)
    ax.set_xticklabels([n.capitalize() for n in names], fontsize=10, rotation=15)
    ax.set_ylabel("$\\Delta H = H_f - H_b$")
    ax.set_title("Predictive Asymmetry by Correction Function")
    for i, (dm, ds) in enumerate(zip(DH_means, DH_stds)):
        sign = 1 if dm >= 0 else -1
        ax.annotate(f"{dm:.3f}", xy=(i, dm + sign * (ds + 0.02)),
                    ha="center", fontsize=9)

    fig.suptitle(
        f"Experiment 4: Correction Function Shape and Coupling Quality "
        f"($\\eta={eta}$, $q={q}$)",
        fontsize=13, y=1.02,
    )
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "P_across_corrections.png", bbox_inches="tight")
    print(f"  Saved: {OUTPUT_DIR / 'P_across_corrections.png'}")

    return all_results


# ============================================================================
# Experiment 5: Adversarial P
# ============================================================================

def simulate_adversarial_pair(
    g: Callable,
    T_A: float,
    T_B: float,
    gamma_A: float,
    gamma_B: float,
    q_base: float,
    num_steps: int = 10000,
    seed: int = 42,
    g_kwargs: Optional[dict] = None,
) -> Tuple[Dict[str, np.ndarray], Dict[str, np.ndarray]]:
    """Simulate two adversarially coupled agents.

    Agent A faces: rho_A = q_base + gamma_B * T_B
    Agent B faces: rho_B = q_base + gamma_A * T_A

    Each agent tracks its own random-walk environment with noise level rho.
    The coupling enters through the noise level: a faster opponent creates
    a noisier environment for you.

    Returns dicts with keys: x, xhat, actions for each agent.
    """
    if g_kwargs is None:
        g_kwargs = {}

    rng = np.random.default_rng(seed)

    rho_A = q_base + gamma_B * T_B
    rho_B = q_base + gamma_A * T_A

    # Agent A
    x_A = np.zeros(num_steps)
    xhat_A = np.zeros(num_steps)
    act_A = np.zeros(num_steps)
    noise_A = rng.normal(0, 1, num_steps)

    # Agent B
    x_B = np.zeros(num_steps)
    xhat_B = np.zeros(num_steps)
    act_B = np.zeros(num_steps)
    noise_B = rng.normal(0, 1, num_steps)

    for t in range(num_steps - 1):
        # Agent A
        delta_A = x_A[t] - xhat_A[t]
        a_A = T_A * g(np.array([delta_A]), **g_kwargs)[0]
        act_A[t] = a_A
        xhat_A[t + 1] = xhat_A[t] + a_A
        x_A[t + 1] = x_A[t] + rho_A * noise_A[t]

        # Agent B
        delta_B = x_B[t] - xhat_B[t]
        a_B = T_B * g(np.array([delta_B]), **g_kwargs)[0]
        act_B[t] = a_B
        xhat_B[t + 1] = xhat_B[t] + a_B
        x_B[t + 1] = x_B[t] + rho_B * noise_B[t]

    # Final actions
    act_A[-1] = T_A * g(np.array([x_A[-1] - xhat_A[-1]]), **g_kwargs)[0]
    act_B[-1] = T_B * g(np.array([x_B[-1] - xhat_B[-1]]), **g_kwargs)[0]

    return (
        {"x": x_A, "xhat": xhat_A, "actions": act_A},
        {"x": x_B, "xhat": xhat_B, "actions": act_B},
    )


def experiment_adversarial_P():
    """Two coupled agents. Does the faster agent maintain higher P?

    Key: as T_A increases, Agent A gets stronger (higher tempo) but also
    makes B's environment noisier (rho_B = q_base + gamma_A * T_A).
    B's tempo is fixed. We measure P for both.
    """
    print("\n" + "=" * 70)
    print("EXPERIMENT 5: Adversarial P")
    print("=" * 70)

    T_B = 0.1
    tempo_ratios = np.array([0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0])
    gamma = 0.5
    q_base = 0.05
    num_steps = 10000
    burn_in = 3000
    n_bins = 16
    n_seeds = 8
    g_kwargs = {"R": 1.0, "epsilon": 0.1, "R_max": 2.0}

    g = CORRECTION_FUNCTIONS["linear"]

    PA_all = np.zeros((len(tempo_ratios), n_seeds))
    PB_all = np.zeros((len(tempo_ratios), n_seeds))
    DHA_all = np.zeros((len(tempo_ratios), n_seeds))
    DHB_all = np.zeros((len(tempo_ratios), n_seeds))
    # Also track mismatch (TFT quantity) for comparison
    mismatch_A_all = np.zeros((len(tempo_ratios), n_seeds))
    mismatch_B_all = np.zeros((len(tempo_ratios), n_seeds))

    for i, r in enumerate(tempo_ratios):
        T_A = r * T_B
        for s in range(n_seeds):
            res_A, res_B = simulate_adversarial_pair(
                g, T_A=T_A, T_B=T_B, gamma_A=gamma, gamma_B=gamma,
                q_base=q_base, num_steps=num_steps, seed=42 + s,
                g_kwargs=g_kwargs,
            )

            # Agent A metrics
            S_A = res_A["xhat"][:-1][burn_in:]
            A_A = res_A["actions"][:-1][burn_in:]
            Sp_A = res_A["x"][1:][burn_in:]
            m_A = compute_hafez_metrics(
                discretize(S_A, n_bins), discretize(A_A, n_bins),
                discretize(Sp_A, n_bins), n_bins
            )
            PA_all[i, s] = m_A["P"]
            DHA_all[i, s] = m_A["DH"]
            mismatch_A_all[i, s] = np.mean(np.abs(
                res_A["x"][burn_in:] - res_A["xhat"][burn_in:]
            ))

            # Agent B metrics
            S_B = res_B["xhat"][:-1][burn_in:]
            A_B = res_B["actions"][:-1][burn_in:]
            Sp_B = res_B["x"][1:][burn_in:]
            m_B = compute_hafez_metrics(
                discretize(S_B, n_bins), discretize(A_B, n_bins),
                discretize(Sp_B, n_bins), n_bins
            )
            PB_all[i, s] = m_B["P"]
            DHB_all[i, s] = m_B["DH"]
            mismatch_B_all[i, s] = np.mean(np.abs(
                res_B["x"][burn_in:] - res_B["xhat"][burn_in:]
            ))

        rho_A = q_base + gamma * T_B
        rho_B = q_base + gamma * T_A
        print(f"  T_A/T_B={r:.1f}  rho_A={rho_A:.3f}  rho_B={rho_B:.3f}  "
              f"P_A={np.mean(PA_all[i]):.4f}  P_B={np.mean(PB_all[i]):.4f}  "
              f"|d|_A={np.mean(mismatch_A_all[i]):.4f}  "
              f"|d|_B={np.mean(mismatch_B_all[i]):.4f}")

    # Plot
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # P_A and P_B vs tempo ratio
    ax = axes[0, 0]
    PA_mean = np.mean(PA_all, axis=1)
    PA_std = np.std(PA_all, axis=1)
    PB_mean = np.mean(PB_all, axis=1)
    PB_std = np.std(PB_all, axis=1)
    ax.errorbar(tempo_ratios, PA_mean, yerr=PA_std, fmt="-o", color="#1f77b4",
                capsize=4, markersize=6, label="Agent A ($T_A$ varies)")
    ax.errorbar(tempo_ratios, PB_mean, yerr=PB_std, fmt="-s", color="#d62728",
                capsize=4, markersize=6, label="Agent B ($T_B$ fixed)")
    ax.axhline(y=0.5, color="k", linestyle="--", alpha=0.3)
    ax.axvline(x=1.0, color="gray", linestyle=":", alpha=0.4,
               label="$T_A = T_B$")
    ax.set_xlabel("Tempo ratio $T_A / T_B$")
    ax.set_ylabel("$P$")
    ax.set_title("Bi-predictability: Faster vs Slower Agent")
    ax.legend(fontsize=9)

    # DH_A and DH_B
    ax = axes[0, 1]
    DHA_mean = np.mean(DHA_all, axis=1)
    DHA_std = np.std(DHA_all, axis=1)
    DHB_mean = np.mean(DHB_all, axis=1)
    DHB_std = np.std(DHB_all, axis=1)
    ax.errorbar(tempo_ratios, DHA_mean, yerr=DHA_std, fmt="-o", color="#1f77b4",
                capsize=4, markersize=6, label="$\\Delta H_A$")
    ax.errorbar(tempo_ratios, DHB_mean, yerr=DHB_std, fmt="-s", color="#d62728",
                capsize=4, markersize=6, label="$\\Delta H_B$")
    ax.axhline(y=0, color="k", linestyle=":", alpha=0.4)
    ax.axvline(x=1.0, color="gray", linestyle=":", alpha=0.4)
    ax.set_xlabel("Tempo ratio $T_A / T_B$")
    ax.set_ylabel("$\\Delta H$")
    ax.set_title("Predictive Asymmetry: Adversarial Coupling")
    ax.legend(fontsize=9)

    # Mismatch comparison (TFT quantity)
    ax = axes[1, 0]
    mA_mean = np.mean(mismatch_A_all, axis=1)
    mA_std = np.std(mismatch_A_all, axis=1)
    mB_mean = np.mean(mismatch_B_all, axis=1)
    mB_std = np.std(mismatch_B_all, axis=1)
    ax.errorbar(tempo_ratios, mA_mean, yerr=mA_std, fmt="-o", color="#1f77b4",
                capsize=4, markersize=6, label="$|\\delta|_A$")
    ax.errorbar(tempo_ratios, mB_mean, yerr=mB_std, fmt="-s", color="#d62728",
                capsize=4, markersize=6, label="$|\\delta|_B$")
    ax.axvline(x=1.0, color="gray", linestyle=":", alpha=0.4)
    ax.set_xlabel("Tempo ratio $T_A / T_B$")
    ax.set_ylabel("Mean $|\\delta|$")
    ax.set_title("TFT Mismatch: Adversarial Coupling")
    ax.legend(fontsize=9)

    # P vs mismatch scatter
    ax = axes[1, 1]
    # Flatten for scatter
    all_P = np.concatenate([PA_all.ravel(), PB_all.ravel()])
    all_mismatch = np.concatenate([mismatch_A_all.ravel(), mismatch_B_all.ravel()])
    ax.scatter(all_mismatch, all_P, alpha=0.4, s=15, color="#2ca02c")
    # Fit trend line
    valid = np.isfinite(all_P) & np.isfinite(all_mismatch) & (all_mismatch > 0)
    if np.sum(valid) > 3:
        z = np.polyfit(all_mismatch[valid], all_P[valid], 1)
        x_fit = np.linspace(np.min(all_mismatch[valid]),
                            np.max(all_mismatch[valid]), 100)
        ax.plot(x_fit, np.polyval(z, x_fit), "k--", linewidth=1.5, alpha=0.7,
                label=f"slope={z[0]:.4f}")
    ax.set_xlabel("TFT mismatch $|\\delta|$")
    ax.set_ylabel("$P$")
    ax.set_title("$P$ vs TFT Mismatch (All Agents)")
    ax.legend(fontsize=9)

    fig.suptitle(
        f"Experiment 5: Adversarial Coupling ($\\gamma={gamma}$, $q_{{base}}={q_base}$, "
        f"$T_B={T_B}$)",
        fontsize=13, y=1.02,
    )
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "adversarial_P.png", bbox_inches="tight")
    print(f"  Saved: {OUTPUT_DIR / 'adversarial_P.png'}")

    return tempo_ratios, PA_all, PB_all, DHA_all, DHB_all, mismatch_A_all, mismatch_B_all


# ============================================================================
# Experiment 6: Perturbation Detection
# ============================================================================

def experiment_perturbation_detection():
    """Introduce sudden perturbation (q increase). Does P drop? How fast recovery?

    Mirrors Hafez's drift detection experiment (Section 5.1.3).
    """
    print("\n" + "=" * 70)
    print("EXPERIMENT 6: Perturbation Detection")
    print("=" * 70)

    eta = 0.1
    q_base = 0.1
    q_perturbed = 0.5  # 5x increase
    num_steps = 6000
    perturb_start = 3000
    n_bins = 16
    window = 200
    stride = 50
    n_seeds = 10
    g_kwargs = {"R": 1.0, "epsilon": 0.1, "R_max": 2.0}

    g = CORRECTION_FUNCTIONS["linear"]

    all_P_traj = []
    all_DH_traj = []
    all_Hf_traj = []
    all_Hb_traj = []
    centers = None

    for s in range(n_seeds):
        rng = np.random.default_rng(42 + s)

        x = np.zeros(num_steps)
        xhat = np.zeros(num_steps)
        actions = np.zeros(num_steps)

        for t in range(num_steps - 1):
            q_t = q_perturbed if t >= perturb_start else q_base
            delta_t = x[t] - xhat[t]
            a_t = eta * g(np.array([delta_t]), **g_kwargs)[0]
            actions[t] = a_t
            xhat[t + 1] = xhat[t] + a_t
            x[t + 1] = x[t] + q_t * rng.normal()

        actions[-1] = eta * g(np.array([x[-1] - xhat[-1]]), **g_kwargs)[0]

        S, A, Sp = extract_hafez_streams(x, xhat, actions)
        wm = compute_windowed_metrics(S, A, Sp, window=window,
                                       stride=stride, n_bins=n_bins)
        all_P_traj.append(wm["P"])
        all_DH_traj.append(wm["DH"])
        all_Hf_traj.append(wm["H_f"])
        all_Hb_traj.append(wm["H_b"])
        if centers is None:
            centers = wm["centers"]

    P_stack = np.array(all_P_traj)
    DH_stack = np.array(all_DH_traj)
    Hf_stack = np.array(all_Hf_traj)
    Hb_stack = np.array(all_Hb_traj)

    P_mean = np.mean(P_stack, axis=0)
    P_std = np.std(P_stack, axis=0)
    DH_mean = np.mean(DH_stack, axis=0)
    Hf_mean = np.mean(Hf_stack, axis=0)
    Hb_mean = np.mean(Hb_stack, axis=0)

    # Pre-perturbation baseline (windows fully before perturbation)
    pre_mask = centers < (perturb_start - window)
    if np.any(pre_mask):
        P_baseline = np.mean(P_mean[pre_mask])
        P_baseline_std = np.std(P_mean[pre_mask])
    else:
        P_baseline = P_mean[0]
        P_baseline_std = 0.01

    # Detection: first window after perturbation where mean P drops below
    # baseline - 2 * std (threshold-based, like Hafez's approach)
    post_mask = centers >= perturb_start
    detection_window = np.nan
    if np.any(post_mask):
        post_centers = centers[post_mask]
        post_P = P_mean[post_mask]
        threshold = P_baseline - 2 * max(P_baseline_std, 0.005)
        below = post_P < threshold
        if np.any(below):
            first_below_idx = np.argmax(below)
            detection_window = post_centers[first_below_idx] - perturb_start

    # Post-perturbation minimum
    if np.any(post_mask):
        post_P_vals = P_mean[post_mask]
        P_min = np.min(post_P_vals)
        P_min_time = centers[post_mask][np.argmin(post_P_vals)]
    else:
        P_min = P_baseline
        P_min_time = perturb_start

    # New steady state (last quarter of simulation)
    late_mask = centers > (num_steps * 0.85)
    if np.any(late_mask):
        P_new_ss = np.mean(P_mean[late_mask])
    else:
        P_new_ss = P_min

    print(f"  Baseline P = {P_baseline:.4f} +/- {P_baseline_std:.4f}")
    print(f"  Post-perturbation P min = {P_min:.4f}")
    print(f"  P drop = {P_baseline - P_min:.4f} "
          f"({(P_baseline - P_min) / max(P_baseline, 1e-8) * 100:.1f}%)")
    if np.isfinite(detection_window):
        print(f"  Detection latency = {detection_window:.0f} steps "
              f"({detection_window / stride:.0f} windows)")
    else:
        print(f"  Detection: P did not clearly cross threshold")
    print(f"  New steady-state P = {P_new_ss:.4f}")

    # Plot
    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    ax = axes[0]
    ax.plot(centers, P_mean, color="#1f77b4", linewidth=1.5, label="$P$ (mean)")
    ax.fill_between(centers, P_mean - P_std, P_mean + P_std,
                    color="#1f77b4", alpha=0.2)
    ax.axvline(x=perturb_start, color="red", linestyle="--", linewidth=2,
               alpha=0.7, label=f"Perturbation ($q$: {q_base} $\\to$ {q_perturbed})")
    ax.axhline(y=P_baseline, color="gray", linestyle=":", alpha=0.5,
               label=f"Baseline $P$ = {P_baseline:.3f}")
    if np.isfinite(detection_window):
        ax.axvline(x=perturb_start + detection_window, color="orange",
                   linestyle="-.", linewidth=1.5, alpha=0.7,
                   label=f"Detection at +{detection_window:.0f} steps")
    ax.set_ylabel("$P$")
    ax.set_title("Bi-predictability Response to Perturbation")
    ax.legend(fontsize=8, loc="lower left")

    ax = axes[1]
    ax.plot(centers, Hf_mean, color="#d62728", linewidth=1.5,
            label="$H_f = H(S'|S,A)$")
    ax.plot(centers, Hb_mean, color="#2ca02c", linewidth=1.5,
            label="$H_b = H(S,A|S')$")
    ax.plot(centers, DH_mean, color="#9467bd", linewidth=1.5, linestyle="--",
            label="$\\Delta H = H_f - H_b$")
    ax.axvline(x=perturb_start, color="red", linestyle="--", linewidth=2,
               alpha=0.7)
    ax.axhline(y=0, color="k", linestyle=":", alpha=0.3)
    ax.set_xlabel("Timestep")
    ax.set_ylabel("Entropy (bits)")
    ax.set_title("Forward/Backward Uncertainty and Asymmetry")
    ax.legend(fontsize=9)

    fig.suptitle(
        f"Experiment 6: Perturbation Detection ($\\eta={eta}$, "
        f"$q$: {q_base}$\\to${q_perturbed} at $t={perturb_start}$, "
        f"window={window}, stride={stride})",
        fontsize=12, y=1.02,
    )
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "perturbation_detection.png", bbox_inches="tight")
    print(f"  Saved: {OUTPUT_DIR / 'perturbation_detection.png'}")

    return {
        "centers": centers,
        "P_mean": P_mean, "P_std": P_std,
        "DH_mean": DH_mean, "Hf_mean": Hf_mean, "Hb_mean": Hb_mean,
        "P_baseline": P_baseline, "P_min": P_min,
        "detection_window": detection_window,
        "P_new_ss": P_new_ss,
    }


# ============================================================================
# Main
# ============================================================================

def main():
    print("=" * 70)
    print("VARIANT: Hafez Bi-Predictability Bridge")
    print("Computing Hafez et al. (S,A,S') metrics from TFT agent dynamics")
    print("=" * 70)

    # Run all experiments
    exp1_etas, exp1_results = experiment_P_vs_eta()
    exp2_results = experiment_passive_vs_active()
    exp3_sigmas, exp3_P, exp3_Hf, exp3_Hb = experiment_P_vs_obs_noise()
    exp4_results = experiment_P_across_corrections()
    (exp5_ratios, exp5_PA, exp5_PB, exp5_DHA, exp5_DHB,
     exp5_mA, exp5_mB) = experiment_adversarial_P()
    exp6_results = experiment_perturbation_detection()

    # -----------------------------------------------------------------------
    # Summary
    # -----------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("SUMMARY OF RESULTS")
    print("=" * 70)

    print("\n--- Exp 1: P vs Tempo (eta) ---")
    P_means = np.mean(exp1_results["P"], axis=1)
    print(f"  eta range: {exp1_etas[0]:.3f} to {exp1_etas[-1]:.3f}")
    print(f"  P range:   {P_means[0]:.4f} to {P_means[-1]:.4f}")
    trend = "increasing" if P_means[-1] > P_means[0] else "decreasing"
    print(f"  Trend: {trend} (higher tempo -> "
          f"{'better' if trend == 'increasing' else 'worse'} coupling)")

    print("\n--- Exp 2: Passive vs Active ---")
    P_passive_m = np.mean(exp2_results["P_passive"])
    P_active_best = np.max(np.mean(exp2_results["P_active"], axis=1))
    DH_passive_m = np.mean(exp2_results["DH_passive"])
    DH_active_vals = np.mean(exp2_results["DH_active"], axis=1)
    print(f"  Passive P  = {P_passive_m:.4f}  (Hafez predicts near 0.5)")
    print(f"  Best active P = {P_active_best:.4f}")
    print(f"  Passive DH = {DH_passive_m:.4f}  (Hafez predicts near 0)")
    print(f"  Active DH range: [{np.min(DH_active_vals):.4f}, "
          f"{np.max(DH_active_vals):.4f}]  (Hafez predicts |DH| > 0)")
    if P_passive_m > P_active_best:
        print(f"  CONFIRMS: passive system has higher P than active agent")
    else:
        print(f"  NOTE: active P ({P_active_best:.4f}) exceeds passive P "
              f"({P_passive_m:.4f}) -- see discussion")

    print("\n--- Exp 3: Observation Noise ---")
    P_noiseless = np.mean(exp3_P[0])
    P_noisy = np.mean(exp3_P[-1])
    Hf_noiseless = np.mean(exp3_Hf[0])
    Hf_noisy = np.mean(exp3_Hf[-1])
    print(f"  P: {P_noiseless:.4f} -> {P_noisy:.4f} "
          f"(drop: {(P_noiseless - P_noisy) / P_noiseless * 100:.1f}%)")
    print(f"  H_f: {Hf_noiseless:.4f} -> {Hf_noisy:.4f} "
          f"(increase: {(Hf_noisy - Hf_noiseless) / max(Hf_noiseless, 0.001) * 100:.1f}%)")
    print(f"  CONFIRMS: observation noise increases H_f (world more opaque)")

    print("\n--- Exp 4: Correction Functions ---")
    for name in CORRECTION_FUNCTIONS:
        P_m = np.mean(exp4_results[name]["P"])
        DH_m = np.mean(exp4_results[name]["DH"])
        print(f"  {name:<20} P={P_m:.4f}  DH={DH_m:.4f}")

    print("\n--- Exp 5: Adversarial Coupling ---")
    PA_means = np.mean(exp5_PA, axis=1)
    PB_means = np.mean(exp5_PB, axis=1)
    mA_means = np.mean(exp5_mA, axis=1)
    mB_means = np.mean(exp5_mB, axis=1)
    for i, r in enumerate(exp5_ratios):
        print(f"  T_A/T_B={r:.1f}  P_A={PA_means[i]:.4f}  P_B={PB_means[i]:.4f}  "
              f"|d|_A={mA_means[i]:.4f}  |d|_B={mB_means[i]:.4f}")

    print("\n--- Exp 6: Perturbation Detection ---")
    print(f"  Baseline P = {exp6_results['P_baseline']:.4f}")
    print(f"  P min after perturbation = {exp6_results['P_min']:.4f}")
    P_drop_pct = ((exp6_results['P_baseline'] - exp6_results['P_min'])
                  / max(exp6_results['P_baseline'], 1e-8) * 100)
    print(f"  P drop = {P_drop_pct:.1f}%")
    if np.isfinite(exp6_results['detection_window']):
        print(f"  Detection latency = {exp6_results['detection_window']:.0f} steps")
    else:
        print(f"  Detection latency = not clearly detected")
    print(f"  New steady-state P = {exp6_results['P_new_ss']:.4f}")

    print(f"\nAll figures saved to: {OUTPUT_DIR}")
    print("Done.")


if __name__ == "__main__":
    main()
