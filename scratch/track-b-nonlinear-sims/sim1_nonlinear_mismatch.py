"""
Simulation 1: Nonlinear Mismatch Dynamics (Single Agent)

Tests TFT's linear mismatch ODE hypothesis by comparing steady-state mismatch,
convergence rate, persistence threshold, and mismatch distribution across five
correction functions:
  1. Linear:              g(delta) = delta
  2. Saturating:          g(delta) = delta / (1 + |delta|/R)
  3. Threshold (dead zone): g(delta) = delta * 1[|delta| > epsilon]
  4. Sigmoid:             g(delta) = R * tanh(delta/R)
  5. Structural breakdown: g(delta) = delta * 1[|delta| < R_max]

Theory reference: TF-11 mismatch dynamics equation
    d||delta||/dt = -T * ||delta|| + rho(t)
with steady-state prediction ||delta||_ss = rho / T.

The discrete-time agent dynamics are:
    delta_{t+1} = delta_t - eta * g(delta_t) + w_t
where w_t ~ N(0, q^2) and T = eta (with nu = 1 event/timestep).
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from pathlib import Path
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Tuple, Optional
import warnings

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

# Colorblind-safe palette (tab10 subset)
COLORS = {
    "linear": "#1f77b4",
    "saturating": "#ff7f0e",
    "threshold": "#2ca02c",
    "sigmoid": "#d62728",
    "breakdown": "#9467bd",
}

# ---------------------------------------------------------------------------
# Correction functions
# ---------------------------------------------------------------------------

def g_linear(delta: np.ndarray, **kwargs) -> np.ndarray:
    """Linear correction: g(delta) = delta."""
    return delta


def g_saturating(delta: np.ndarray, R: float = 1.0, **kwargs) -> np.ndarray:
    """Saturating correction: g(delta) = delta / (1 + |delta|/R).

    Bounded at |g| -> R for large |delta|. Linear near zero.
    """
    return delta / (1.0 + np.abs(delta) / R)


def g_threshold(delta: np.ndarray, epsilon: float = 0.1, **kwargs) -> np.ndarray:
    """Threshold (dead zone) correction: g(delta) = delta * 1[|delta| > epsilon].

    No correction when |delta| < epsilon.
    """
    return delta * (np.abs(delta) > epsilon).astype(float)


def g_sigmoid(delta: np.ndarray, R: float = 1.0, **kwargs) -> np.ndarray:
    """Sigmoid correction: g(delta) = R * tanh(delta/R).

    Smooth saturation at +/- R. Linear near zero.
    """
    return R * np.tanh(delta / R)


def g_breakdown(delta: np.ndarray, R_max: float = 2.0, **kwargs) -> np.ndarray:
    """Structural breakdown: g(delta) = delta * 1[|delta| < R_max].

    Correction ceases entirely when |delta| >= R_max.
    """
    return delta * (np.abs(delta) < R_max).astype(float)


# Registry of all correction functions with display metadata
CORRECTION_FUNCTIONS: Dict[str, Callable] = {
    "linear": g_linear,
    "saturating": g_saturating,
    "threshold": g_threshold,
    "sigmoid": g_sigmoid,
    "breakdown": g_breakdown,
}

CORRECTION_LABELS: Dict[str, str] = {
    "linear": "Linear: $g(\\delta)=\\delta$",
    "saturating": "Saturating: $g(\\delta)=\\delta/(1+|\\delta|/R)$",
    "threshold": "Threshold: $g(\\delta)=\\delta \\cdot \\mathbf{1}[|\\delta|>\\epsilon]$",
    "sigmoid": "Sigmoid: $g(\\delta)=R\\tanh(\\delta/R)$",
    "breakdown": "Breakdown: $g(\\delta)=\\delta \\cdot \\mathbf{1}[|\\delta|<R_{\\max}]$",
}


# ---------------------------------------------------------------------------
# Simulation parameters
# ---------------------------------------------------------------------------

@dataclass
class Sim1Params:
    """Parameters for Simulation 1."""
    # Agent parameters
    eta: float = 0.1          # Update gain (= adaptive tempo T with nu=1)

    # Environment parameters
    q: float = 0.1            # Noise std dev (controls rho)

    # Nonlinearity parameters
    R: float = 1.0            # Saturation radius (saturating, sigmoid)
    epsilon: float = 0.1      # Dead zone threshold
    R_max: float = 2.0        # Breakdown radius

    # Simulation parameters
    num_steps: int = 10_000   # Total timesteps per trial
    num_trials: int = 200     # Monte Carlo replicates
    burn_in: int = 2_000      # Steps to discard for steady-state stats
    seed: int = 42            # Random seed

    # Initial conditions
    delta_0: float = 0.0      # Initial mismatch

    @property
    def T(self) -> float:
        """Adaptive tempo (= eta with nu = 1)."""
        return self.eta

    @property
    def rho_over_T(self) -> float:
        """Ratio rho/T = q/eta (linear steady-state prediction)."""
        return self.q / self.eta

    def nonlinearity_kwargs(self) -> dict:
        """Return keyword arguments for correction functions."""
        return {"R": self.R, "epsilon": self.epsilon, "R_max": self.R_max}


# ---------------------------------------------------------------------------
# Core simulation
# ---------------------------------------------------------------------------

def simulate_single_agent(
    g: Callable,
    params: Sim1Params,
    delta_0: Optional[float] = None,
) -> np.ndarray:
    """Run Monte Carlo simulation of a single agent with correction function g.

    Returns:
        deltas: array of shape (num_trials, num_steps) containing delta_t trajectories
    """
    rng = np.random.default_rng(params.seed)
    n_trials = params.num_trials
    n_steps = params.num_steps
    d0 = delta_0 if delta_0 is not None else params.delta_0
    kwargs = params.nonlinearity_kwargs()

    # Pre-generate all noise: shape (num_trials, num_steps)
    noise = rng.normal(0.0, params.q, size=(n_trials, n_steps))

    # Initialize mismatch array
    deltas = np.zeros((n_trials, n_steps))
    deltas[:, 0] = d0

    # Run forward simulation (vectorized across trials)
    for t in range(n_steps - 1):
        correction = g(deltas[:, t], **kwargs)
        deltas[:, t + 1] = deltas[:, t] - params.eta * correction + noise[:, t]

    return deltas


def steady_state_stats(
    deltas: np.ndarray, burn_in: int
) -> Tuple[float, float, float, float]:
    """Compute steady-state statistics from trajectory data.

    Returns:
        (mean_abs_delta, median_abs_delta, p10, p90)
    """
    ss = np.abs(deltas[:, burn_in:])
    # Per-trial time-average, then statistics across trials
    trial_means = ss.mean(axis=1)
    return (
        np.mean(trial_means),
        np.median(trial_means),
        np.percentile(trial_means, 10),
        np.percentile(trial_means, 90),
    )


# ---------------------------------------------------------------------------
# M1: Steady-state |delta| vs rho/T
# ---------------------------------------------------------------------------

def run_steady_state_sweep(
    rho_over_T_values: np.ndarray,
    base_params: Sim1Params,
) -> Dict[str, Dict[str, np.ndarray]]:
    """Sweep rho/T and measure steady-state |delta| for each correction function.

    We fix eta and vary q to change rho/T.

    Returns:
        results[func_name] = {"mean": ..., "median": ..., "p10": ..., "p90": ...}
        each value is an array of length len(rho_over_T_values).
    """
    results = {}
    for name, g in CORRECTION_FUNCTIONS.items():
        means, medians, p10s, p90s = [], [], [], []
        for rot in rho_over_T_values:
            p = Sim1Params(
                eta=base_params.eta,
                q=rot * base_params.eta,  # q = (rho/T) * eta
                R=base_params.R,
                epsilon=base_params.epsilon,
                R_max=base_params.R_max,
                num_steps=base_params.num_steps,
                num_trials=base_params.num_trials,
                burn_in=base_params.burn_in,
                seed=base_params.seed,
            )
            deltas = simulate_single_agent(g, p)
            mean, median, lo, hi = steady_state_stats(deltas, p.burn_in)
            means.append(mean)
            medians.append(median)
            p10s.append(lo)
            p90s.append(hi)
        results[name] = {
            "mean": np.array(means),
            "median": np.array(medians),
            "p10": np.array(p10s),
            "p90": np.array(p90s),
        }
        print(f"  [M1] {name}: done ({len(rho_over_T_values)} points)")
    return results


def plot_steady_state(
    rho_over_T: np.ndarray,
    results: Dict[str, Dict[str, np.ndarray]],
    save_path: Optional[Path] = None,
):
    """Plot steady-state |delta| vs rho/T for all correction functions."""
    fig, ax = plt.subplots(figsize=(9, 6))

    # Exact discrete-time AR(1) prediction for E[|delta|]:
    # For delta_{t+1} = (1-eta)*delta_t + w_t with noise std q,
    # stationary std = q / sqrt(2*eta - eta^2),
    # E[|delta|] = std * sqrt(2/pi)
    eta = 0.1  # default from base_params
    q_vals = rho_over_T * eta
    discrete_pred = (q_vals / np.sqrt(2 * eta - eta ** 2)) * np.sqrt(2 / np.pi)
    ax.plot(
        rho_over_T, discrete_pred,
        "k-", linewidth=2, alpha=0.5,
        label="Discrete-time linear (exact)",
    )

    # Continuous ODE prediction for comparison
    ax.plot(
        rho_over_T, rho_over_T,
        "k--", linewidth=2, alpha=0.4,
        label="Continuous ODE: $\\rho/\\mathcal{T}$",
    )

    for name, data in results.items():
        color = COLORS[name]
        ax.plot(rho_over_T, data["median"], "-o", color=color, markersize=4,
                label=CORRECTION_LABELS[name])
        ax.fill_between(rho_over_T, data["p10"], data["p90"], color=color, alpha=0.15)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("$\\rho / \\mathcal{T}$ (= $q / \\eta$)")
    ax.set_ylabel("Steady-state $\\langle|\\delta|\\rangle$")
    ax.set_title("Steady-State Mismatch vs. $\\rho/\\mathcal{T}$")
    ax.legend(fontsize=9, loc="upper left")
    ax.set_xlim(rho_over_T[0] * 0.8, rho_over_T[-1] * 1.2)
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path)
        print(f"  Saved: {save_path}")
    return fig


# ---------------------------------------------------------------------------
# M2: Convergence rate from initial conditions
# ---------------------------------------------------------------------------

def run_convergence(
    base_params: Sim1Params,
    delta_0: float = 5.0,
    max_display_steps: int = 500,
) -> Dict[str, np.ndarray]:
    """Measure convergence from large initial mismatch.

    Returns:
        results[func_name] = array of shape (max_display_steps,) -- mean |delta_t|
    """
    results = {}
    p = Sim1Params(
        eta=base_params.eta,
        q=base_params.q,
        R=base_params.R,
        epsilon=base_params.epsilon,
        R_max=base_params.R_max,
        num_steps=max_display_steps,
        num_trials=base_params.num_trials,
        burn_in=0,
        seed=base_params.seed,
    )
    for name, g in CORRECTION_FUNCTIONS.items():
        deltas = simulate_single_agent(g, p, delta_0=delta_0)
        results[name] = np.mean(np.abs(deltas), axis=0)
        print(f"  [M2] {name}: done")
    return results


def plot_convergence(
    convergence: Dict[str, np.ndarray],
    params: Sim1Params,
    delta_0: float = 5.0,
    save_path: Optional[Path] = None,
):
    """Plot convergence trajectories for all correction functions."""
    fig, ax = plt.subplots(figsize=(9, 6))
    steps = np.arange(len(list(convergence.values())[0]))

    # Theoretical exponential decay (linear case)
    ss = params.q / params.eta
    theory = delta_0 * np.exp(-params.eta * steps) + ss * (1 - np.exp(-params.eta * steps))
    ax.plot(steps, theory, "k--", linewidth=2, alpha=0.7,
            label=f"Linear theory (decay rate $\\mathcal{{T}}$={params.eta:.2f})")

    for name, trajectory in convergence.items():
        ax.plot(steps, trajectory, color=COLORS[name], label=CORRECTION_LABELS[name])

    ax.axhline(y=ss, color="gray", linestyle=":", alpha=0.5,
               label=f"$\\rho/\\mathcal{{T}}$ = {ss:.2f}")
    ax.set_xlabel("Timestep $t$")
    ax.set_ylabel("Mean $|\\delta_t|$")
    ax.set_title(f"Convergence from $\\delta_0 = {delta_0}$  ($\\eta={params.eta}$, $q={params.q}$)")
    ax.legend(fontsize=9)
    ax.set_ylim(bottom=0)
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path)
        print(f"  Saved: {save_path}")
    return fig


# ---------------------------------------------------------------------------
# M3: Persistence threshold
# ---------------------------------------------------------------------------

def run_persistence_threshold(
    q_values: np.ndarray,
    base_params: Sim1Params,
    divergence_threshold: float = 100.0,
) -> Dict[str, np.ndarray]:
    """Measure fraction of persistent trials vs q/eta.

    A trial "diverges" if max |delta_t| exceeds divergence_threshold * R_max
    at any point after burn-in.

    Returns:
        results[func_name] = array of persistence fractions, shape (len(q_values),)
    """
    threshold = divergence_threshold * base_params.R_max
    results = {}
    for name, g in CORRECTION_FUNCTIONS.items():
        fractions = []
        for q in q_values:
            p = Sim1Params(
                eta=base_params.eta,
                q=q,
                R=base_params.R,
                epsilon=base_params.epsilon,
                R_max=base_params.R_max,
                num_steps=base_params.num_steps,
                num_trials=base_params.num_trials,
                burn_in=base_params.burn_in,
                seed=base_params.seed,
            )
            deltas = simulate_single_agent(g, p)
            # A trial persists if |delta| never exceeds the threshold after burn-in
            max_delta = np.max(np.abs(deltas[:, p.burn_in:]), axis=1)
            frac_persist = np.mean(max_delta < threshold)
            fractions.append(frac_persist)
        results[name] = np.array(fractions)
        print(f"  [M3] {name}: done ({len(q_values)} points)")
    return results


def plot_persistence_threshold(
    q_over_eta: np.ndarray,
    persistence: Dict[str, np.ndarray],
    params: Sim1Params,
    save_path: Optional[Path] = None,
):
    """Plot persistence fraction vs rho/T."""
    fig, ax = plt.subplots(figsize=(9, 6))

    # Theoretical breakdown threshold for structural breakdown case
    # T > rho / R_max  =>  rho/T < R_max  =>  q/eta < R_max
    critical_rot = params.R_max
    ax.axvline(x=critical_rot, color="gray", linestyle=":", alpha=0.6,
               label=f"Theory: $\\rho/\\mathcal{{T}}$ = $R_{{\\max}}$ = {params.R_max}")

    for name, frac in persistence.items():
        ax.plot(q_over_eta, frac, "-o", color=COLORS[name], markersize=4,
                label=CORRECTION_LABELS[name])

    ax.set_xlabel("$\\rho / \\mathcal{T}$ (= $q / \\eta$)")
    ax.set_ylabel("Fraction of persistent trials")
    ax.set_title("Persistence Threshold: Fraction of Bounded Trials vs. $\\rho/\\mathcal{T}$")
    ax.legend(fontsize=9)
    ax.set_ylim(-0.05, 1.05)
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path)
        print(f"  Saved: {save_path}")
    return fig


# ---------------------------------------------------------------------------
# M4: Mismatch distribution
# ---------------------------------------------------------------------------

def run_mismatch_distribution(
    base_params: Sim1Params,
) -> Dict[str, np.ndarray]:
    """Collect the distribution of |delta| at steady state.

    Returns:
        results[func_name] = 1D array of all |delta| values (post-burn-in, all trials)
    """
    results = {}
    for name, g in CORRECTION_FUNCTIONS.items():
        deltas = simulate_single_agent(g, base_params)
        ss_abs = np.abs(deltas[:, base_params.burn_in:]).ravel()
        results[name] = ss_abs
        print(f"  [M4] {name}: done ({len(ss_abs)} samples)")
    return results


def plot_mismatch_distribution(
    distributions: Dict[str, np.ndarray],
    params: Sim1Params,
    save_path: Optional[Path] = None,
):
    """Plot histogram of |delta| for each correction function."""
    fig, axes = plt.subplots(2, 3, figsize=(14, 9))
    axes_flat = axes.ravel()

    # Theoretical steady state for linear case
    ss_theory = params.q / params.eta

    for idx, (name, data) in enumerate(distributions.items()):
        ax = axes_flat[idx]
        # Clip extreme values for visualization
        clip_val = np.percentile(data, 99.5)
        clipped = data[data <= clip_val]
        ax.hist(clipped, bins=80, density=True, alpha=0.7, color=COLORS[name],
                edgecolor="white", linewidth=0.3)
        ax.axvline(x=ss_theory, color="k", linestyle="--", alpha=0.7,
                   label=f"$\\rho/\\mathcal{{T}}$ = {ss_theory:.2f}")
        ax.axvline(x=np.median(data), color=COLORS[name], linestyle="-",
                   alpha=0.9, linewidth=2,
                   label=f"Median = {np.median(data):.3f}")
        ax.set_title(CORRECTION_LABELS[name], fontsize=10)
        ax.set_xlabel("$|\\delta|$")
        ax.set_ylabel("Density")
        ax.legend(fontsize=8)

    # Hide unused subplot
    axes_flat[-1].set_visible(False)

    fig.suptitle(
        f"Mismatch Distribution at Steady State "
        f"($\\eta={params.eta}$, $q={params.q}$, $\\rho/\\mathcal{{T}}={params.q/params.eta:.1f}$)",
        fontsize=13,
    )
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path)
        print(f"  Saved: {save_path}")
    return fig


# ---------------------------------------------------------------------------
# M5: Phase portraits (deterministic flow)
# ---------------------------------------------------------------------------

def plot_phase_portraits(
    params: Sim1Params,
    save_path: Optional[Path] = None,
):
    """Plot the deterministic correction flow d(delta)/dt = -eta * g(delta) for each
    correction function, with noise scale overlaid."""
    fig, ax = plt.subplots(figsize=(9, 6))

    delta_range = np.linspace(-4.0, 4.0, 500)

    for name, g in CORRECTION_FUNCTIONS.items():
        flow = -params.eta * g(delta_range, **params.nonlinearity_kwargs())
        ax.plot(delta_range, flow, color=COLORS[name], label=CORRECTION_LABELS[name])

    # Noise scale
    ax.axhline(y=params.q, color="gray", linestyle=":", alpha=0.5)
    ax.axhline(y=-params.q, color="gray", linestyle=":", alpha=0.5,
               label=f"Noise scale $\\pm q$ = $\\pm${params.q}")

    ax.axhline(y=0, color="k", linewidth=0.5)
    ax.axvline(x=0, color="k", linewidth=0.5)

    # Mark key radii
    ax.axvline(x=params.R_max, color=COLORS["breakdown"], linestyle="--",
               alpha=0.4, label=f"$R_{{\\max}}$ = {params.R_max}")
    ax.axvline(x=-params.R_max, color=COLORS["breakdown"], linestyle="--", alpha=0.4)
    ax.axvline(x=params.epsilon, color=COLORS["threshold"], linestyle="--",
               alpha=0.4, label=f"$\\epsilon$ = {params.epsilon}")
    ax.axvline(x=-params.epsilon, color=COLORS["threshold"], linestyle="--", alpha=0.4)

    ax.set_xlabel("$\\delta$")
    ax.set_ylabel("$-\\eta \\cdot g(\\delta)$  (correction flow)")
    ax.set_title("Deterministic Correction Flow: Phase Portrait")
    ax.legend(fontsize=8, loc="lower left")
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path)
        print(f"  Saved: {save_path}")
    return fig


# ---------------------------------------------------------------------------
# Save numerical results
# ---------------------------------------------------------------------------

def save_results(
    rho_over_T: np.ndarray,
    ss_results: Dict[str, Dict[str, np.ndarray]],
    convergence_results: Dict[str, np.ndarray],
    persistence_q_over_eta: np.ndarray,
    persistence_results: Dict[str, np.ndarray],
    filepath: Path,
):
    """Save all numerical results to a single NPZ file."""
    data = {"rho_over_T_sweep": rho_over_T}

    for name in CORRECTION_FUNCTIONS:
        for stat in ["mean", "median", "p10", "p90"]:
            data[f"ss_{name}_{stat}"] = ss_results[name][stat]
        data[f"conv_{name}"] = convergence_results[name]

    data["persistence_q_over_eta"] = persistence_q_over_eta
    for name in CORRECTION_FUNCTIONS:
        data[f"persist_{name}"] = persistence_results[name]

    np.savez(filepath, **data)
    print(f"  Saved numerical results: {filepath}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    """Run the full Simulation 1 parameter sweep and produce all figures."""
    print("=" * 70)
    print("SIMULATION 1: Nonlinear Mismatch Dynamics (Single Agent)")
    print("=" * 70)

    base = Sim1Params(
        eta=0.1,
        q=0.1,
        R=1.0,
        epsilon=0.1,
        R_max=2.0,
        num_steps=10_000,
        num_trials=200,
        burn_in=2_000,
        seed=42,
    )

    # --- M1: Steady-state vs rho/T ---
    print("\n--- M1: Steady-state mismatch vs rho/T ---")
    rho_over_T = np.logspace(-1.0, 1.0, 25)  # 0.1 to 10
    ss_results = run_steady_state_sweep(rho_over_T, base)
    fig1 = plot_steady_state(
        rho_over_T, ss_results,
        save_path=FIGURE_DIR / "sim1_fig1_steadystate.png",
    )

    # --- M2: Convergence ---
    print("\n--- M2: Convergence from delta_0 = 5.0 ---")
    conv_results = run_convergence(base, delta_0=5.0, max_display_steps=500)
    fig2 = plot_convergence(
        conv_results, base, delta_0=5.0,
        save_path=FIGURE_DIR / "sim1_fig2_convergence.png",
    )

    # --- M3: Persistence threshold ---
    print("\n--- M3: Persistence threshold ---")
    q_over_eta_sweep = np.linspace(0.1, 5.0, 25)
    q_sweep = q_over_eta_sweep * base.eta
    persist_results = run_persistence_threshold(q_sweep, base)
    fig3 = plot_persistence_threshold(
        q_over_eta_sweep, persist_results, base,
        save_path=FIGURE_DIR / "sim1_fig3_persistence.png",
    )

    # --- M4: Mismatch distribution ---
    print("\n--- M4: Mismatch distribution at rho/T = 1.0 ---")
    dist_params = Sim1Params(
        eta=0.1, q=0.1,  # rho/T = 1.0
        R=1.0, epsilon=0.1, R_max=2.0,
        num_steps=10_000, num_trials=200, burn_in=2_000, seed=42,
    )
    dist_results = run_mismatch_distribution(dist_params)
    fig4 = plot_mismatch_distribution(
        dist_results, dist_params,
        save_path=FIGURE_DIR / "sim1_fig4_distribution.png",
    )

    # --- M5: Phase portraits ---
    print("\n--- M5: Phase portraits ---")
    fig5 = plot_phase_portraits(
        base,
        save_path=FIGURE_DIR / "sim1_fig5_phaseportrait.png",
    )

    # --- Save numerical results ---
    print("\n--- Saving numerical results ---")
    save_results(
        rho_over_T, ss_results, conv_results,
        q_over_eta_sweep, persist_results,
        FIGURE_DIR / "sim1_results.npz",
    )

    # --- Summary table ---
    print("\n" + "=" * 70)
    print("SUMMARY: Steady-state |delta| at rho/T = 1.0")
    print("=" * 70)
    # Find the index closest to rho/T = 1.0
    idx = np.argmin(np.abs(rho_over_T - 1.0))
    print(f"  Linear theory prediction: {rho_over_T[idx]:.3f}")
    print(f"  {'Function':<20} {'Median':>10} {'[P10, P90]':>20}")
    print(f"  {'-'*50}")
    for name in CORRECTION_FUNCTIONS:
        med = ss_results[name]["median"][idx]
        p10 = ss_results[name]["p10"][idx]
        p90 = ss_results[name]["p90"][idx]
        print(f"  {name:<20} {med:>10.4f} [{p10:.4f}, {p90:.4f}]")

    print("\nDone. Figures saved to:", FIGURE_DIR)
    plt.show()


if __name__ == "__main__":
    main()
