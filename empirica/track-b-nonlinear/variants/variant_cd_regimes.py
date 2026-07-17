"""
Variants C & D: Testing Whether TFT's Squared Tempo Advantage Emerges
in Specific Parameter Regimes

Corollary 11.2 predicts: ||delta_B||/||delta_A|| = (gamma_A/gamma_B) * (T_A/T_B)^2

The existing sims found exponent ~1.05 (linear correction), not 2.0. Two hypotheses:

  C. The continuous-time ODE approximation requires eta << 1 (many events per
     e-folding time). Existing sims use eta = T_B = 0.1. As eta -> 0, the
     discrete AR(1) dynamics should converge to the continuous ODE, potentially
     recovering the squared exponent.

  D. The coupling-dominant regime requires gamma*T >> q_base. Existing sims have
     gamma*T_A in [0.025, 0.25] vs q_base = 0.05 -- not clearly dominant.
     As q_base -> 0, coupling dominates and the squared law should emerge.

This script tests both hypotheses using ONLY the linear correction function
to isolate the regime effect from nonlinearity effects.

Theory reference: TF-11 Corollary 11.2, Appendix A.
"""

import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
from dataclasses import dataclass
from typing import Tuple, Dict, Optional
import time

# Import correction functions from parent sim1
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sim1_nonlinear_mismatch import g_linear

# ---------------------------------------------------------------------------
# Output directory
# ---------------------------------------------------------------------------
OUTPUT_DIR = Path(__file__).resolve().parent
FIGURE_DIR = OUTPUT_DIR

# ---------------------------------------------------------------------------
# Plotting style
# ---------------------------------------------------------------------------
plt.rcParams.update({
    "figure.figsize": (10, 7),
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


# ---------------------------------------------------------------------------
# Parameters
# ---------------------------------------------------------------------------

@dataclass
class RegimeParams:
    """Parameters for the regime-testing simulations."""
    T_A: float = 0.1
    T_B: float = 0.1
    gamma_A: float = 0.5
    gamma_B: float = 0.5
    q_base: float = 0.05
    num_steps: int = 20_000
    num_trials: int = 100
    burn_in_frac: float = 0.25  # fraction of steps to discard
    seed: int = 42

    @property
    def burn_in(self) -> int:
        return int(self.num_steps * self.burn_in_frac)

    @property
    def rho_A(self) -> float:
        return self.q_base + self.gamma_B * self.T_B

    @property
    def rho_B(self) -> float:
        return self.q_base + self.gamma_A * self.T_A


# ---------------------------------------------------------------------------
# Core simulation (linear correction only, optimized)
# ---------------------------------------------------------------------------

def simulate_coupled_linear(params: RegimeParams) -> Tuple[np.ndarray, np.ndarray]:
    """Run coupled linear agents. Returns per-trial time-averaged |delta|.

    For the linear case, delta_{t+1} = (1 - T) * delta_t + w_t, which is
    an AR(1) process. We simulate it directly.

    Returns:
        (mean_abs_A, mean_abs_B): each of shape (num_trials,)
    """
    rng = np.random.default_rng(params.seed)
    n = params.num_trials
    T = params.num_steps
    burn = params.burn_in

    rho_A = params.rho_A
    rho_B = params.rho_B
    T_A = params.T_A
    T_B = params.T_B

    # Stability check: |1 - T| < 1 required for AR(1) stationarity
    if T_A >= 2.0 or T_B >= 2.0:
        raise ValueError(f"T_A={T_A} or T_B={T_B} >= 2.0: AR(1) unstable")

    decay_A = 1.0 - T_A
    decay_B = 1.0 - T_B

    # Pre-generate noise
    noise_A = rng.normal(0.0, rho_A, size=(n, T))
    noise_B = rng.normal(0.0, rho_B, size=(n, T))

    # Simulate
    delta_A = np.zeros(n)
    delta_B = np.zeros(n)

    # Accumulate steady-state |delta| after burn-in
    sum_abs_A = np.zeros(n)
    sum_abs_B = np.zeros(n)
    count = 0

    for t in range(T):
        delta_A = decay_A * delta_A + noise_A[:, t]
        delta_B = decay_B * delta_B + noise_B[:, t]
        if t >= burn:
            sum_abs_A += np.abs(delta_A)
            sum_abs_B += np.abs(delta_B)
            count += 1

    mean_abs_A = sum_abs_A / count
    mean_abs_B = sum_abs_B / count

    return mean_abs_A, mean_abs_B


def measure_mismatch_ratio(params: RegimeParams) -> Tuple[float, float, float]:
    """Measure steady-state ||delta_B|| / ||delta_A|| with uncertainty.

    Returns:
        (median_ratio, p10, p90) across trials
    """
    abs_A, abs_B = simulate_coupled_linear(params)
    valid = abs_A > 1e-15
    if not np.any(valid):
        return np.nan, np.nan, np.nan
    ratios = abs_B[valid] / abs_A[valid]
    return np.median(ratios), np.percentile(ratios, 10), np.percentile(ratios, 90)


# ---------------------------------------------------------------------------
# Analytical predictions
# ---------------------------------------------------------------------------

def discrete_linear_prediction(params: RegimeParams) -> float:
    """Exact discrete-time AR(1) prediction for the mismatch ratio.

    For AR(1): delta_{t+1} = (1-T)*delta_t + w_t with noise std rho,
    stationary std = rho / sqrt(2*T - T^2).
    The ratio of E[|delta|] equals the ratio of stationary stds.
    """
    T_A, T_B = params.T_A, params.T_B
    rho_A, rho_B = params.rho_A, params.rho_B

    std_A = rho_A / np.sqrt(2 * T_A - T_A**2)
    std_B = rho_B / np.sqrt(2 * T_B - T_B**2)
    if std_A == 0:
        return np.inf
    return std_B / std_A


def continuous_ode_prediction(params: RegimeParams) -> float:
    """Continuous-ODE prediction: (rho_B / T_B) / (rho_A / T_A)."""
    T_A, T_B = params.T_A, params.T_B
    rho_A, rho_B = params.rho_A, params.rho_B
    delta_B = rho_B / T_B
    delta_A = rho_A / T_A
    if delta_A == 0:
        return np.inf
    return delta_B / delta_A


def coupling_dominant_prediction(params: RegimeParams) -> float:
    """Coupling-dominant prediction: (gamma_A/gamma_B) * (T_A/T_B)^2."""
    return (params.gamma_A / params.gamma_B) * (params.T_A / params.T_B)**2


# ---------------------------------------------------------------------------
# Exponent estimation
# ---------------------------------------------------------------------------

def estimate_exponent(
    tempo_ratios: np.ndarray,
    mismatch_ratios: np.ndarray,
    gamma_ratio: float = 1.0,
) -> Tuple[float, float]:
    """Estimate exponent b in mismatch_ratio ~ gamma_ratio * (T_A/T_B)^b.

    Uses OLS on log-transformed data.
    Returns: (b, b_stderr)
    """
    valid = np.isfinite(mismatch_ratios) & (mismatch_ratios > 0) & (tempo_ratios > 0)
    if np.sum(valid) < 3:
        return np.nan, np.nan

    x = np.log(tempo_ratios[valid])
    y = np.log(mismatch_ratios[valid] / gamma_ratio)

    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    ss_xx = np.sum((x - x_mean)**2)
    ss_xy = np.sum((x - x_mean) * (y - y_mean))

    if ss_xx < 1e-15:
        return np.nan, np.nan

    b = ss_xy / ss_xx
    a = y_mean - b * x_mean
    y_pred = a + b * x
    residuals = y - y_pred
    s2 = np.sum(residuals**2) / (n - 2) if n > 2 else np.nan
    b_stderr = np.sqrt(s2 / ss_xx) if np.isfinite(s2) else np.nan

    return b, b_stderr


def measure_exponent_at_params(
    eta: float,
    q_base: float,
    gamma: float = 0.5,
    num_trials: int = 100,
    tempo_ratios: Optional[np.ndarray] = None,
) -> Tuple[float, float, np.ndarray, np.ndarray]:
    """Measure the effective exponent for given (eta, q_base).

    Sweeps T_A/T_B from 0.5 to 5.0, measures mismatch ratios, fits exponent.

    Returns:
        (exponent, stderr, tempo_ratios, median_ratios)
    """
    if tempo_ratios is None:
        tempo_ratios = np.logspace(np.log10(0.5), np.log10(5.0), 15)

    # Scale num_steps with 1/eta to ensure enough e-folding times
    # Need at least ~10 e-folding times after burn-in for good statistics
    min_steps_per_efold = int(1.0 / eta) if eta > 0 else 100_000
    num_steps = max(20_000, min_steps_per_efold * 40)
    # Cap to prevent excessive computation
    num_steps = min(num_steps, 2_000_000)

    medians = []
    for r in tempo_ratios:
        T_A = r * eta
        # Skip if T_A >= 2 (AR(1) instability)
        if T_A >= 1.99:
            medians.append(np.nan)
            continue

        p = RegimeParams(
            T_A=T_A,
            T_B=eta,
            gamma_A=gamma,
            gamma_B=gamma,
            q_base=q_base,
            num_steps=num_steps,
            num_trials=num_trials,
            burn_in_frac=0.25,
            seed=42,
        )
        med, _, _ = measure_mismatch_ratio(p)
        medians.append(med)

    medians = np.array(medians)
    b, se = estimate_exponent(tempo_ratios, medians, gamma_ratio=1.0)
    return b, se, tempo_ratios, medians


# ---------------------------------------------------------------------------
# Analytical exponent predictions
# ---------------------------------------------------------------------------

def analytical_discrete_exponent(
    eta: float,
    q_base: float,
    gamma: float = 0.5,
    tempo_ratios: Optional[np.ndarray] = None,
) -> Tuple[float, float]:
    """Compute the exponent predicted by the exact discrete-time AR(1) formula.

    This is the 'truth' for the linear discrete simulation -- the simulation
    should match this. The question is whether THIS exponent approaches 2.0
    as eta -> 0 and q_base -> 0.
    """
    if tempo_ratios is None:
        tempo_ratios = np.logspace(np.log10(0.5), np.log10(5.0), 15)

    predictions = []
    for r in tempo_ratios:
        T_A = r * eta
        if T_A >= 2.0:
            predictions.append(np.nan)
            continue
        p = RegimeParams(
            T_A=T_A, T_B=eta,
            gamma_A=gamma, gamma_B=gamma,
            q_base=q_base,
        )
        predictions.append(discrete_linear_prediction(p))

    predictions = np.array(predictions)
    b, se = estimate_exponent(tempo_ratios, predictions, gamma_ratio=1.0)
    return b, se


def analytical_continuous_exponent(
    eta: float,
    q_base: float,
    gamma: float = 0.5,
    tempo_ratios: Optional[np.ndarray] = None,
) -> Tuple[float, float]:
    """Compute the exponent predicted by the continuous-ODE formula."""
    if tempo_ratios is None:
        tempo_ratios = np.logspace(np.log10(0.5), np.log10(5.0), 15)

    predictions = []
    for r in tempo_ratios:
        T_A = r * eta
        p = RegimeParams(
            T_A=T_A, T_B=eta,
            gamma_A=gamma, gamma_B=gamma,
            q_base=q_base,
        )
        predictions.append(continuous_ode_prediction(p))

    predictions = np.array(predictions)
    b, se = estimate_exponent(tempo_ratios, predictions, gamma_ratio=1.0)
    return b, se


# ---------------------------------------------------------------------------
# Variant C: Approaching the continuous-time limit
# ---------------------------------------------------------------------------

def run_variant_c():
    """Sweep eta (= T_B) and measure how the exponent changes."""
    print("\n" + "=" * 70)
    print("VARIANT C: Approaching the Continuous-Time Limit")
    print("=" * 70)

    eta_values = np.array([0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001])
    q_base = 0.05
    gamma = 0.5
    tempo_ratios = np.logspace(np.log10(0.5), np.log10(5.0), 15)

    results = {
        "eta": eta_values,
        "sim_exponent": [],
        "sim_stderr": [],
        "discrete_exponent": [],
        "continuous_exponent": [],
    }

    for eta in eta_values:
        t0 = time.time()

        # Analytical predictions (fast)
        b_disc, _ = analytical_discrete_exponent(eta, q_base, gamma, tempo_ratios)
        b_cont, _ = analytical_continuous_exponent(eta, q_base, gamma, tempo_ratios)

        # Simulation (slow)
        # Scale trials down for small eta (longer runs needed, but signal is cleaner)
        num_trials = max(30, int(100 * min(1.0, eta / 0.01)))
        b_sim, se_sim, _, _ = measure_exponent_at_params(
            eta, q_base, gamma, num_trials=num_trials, tempo_ratios=tempo_ratios,
        )

        elapsed = time.time() - t0
        results["sim_exponent"].append(b_sim)
        results["sim_stderr"].append(se_sim)
        results["discrete_exponent"].append(b_disc)
        results["continuous_exponent"].append(b_cont)

        print(f"  eta={eta:.4f}: sim={b_sim:.4f}+/-{se_sim:.4f}, "
              f"discrete={b_disc:.4f}, continuous={b_cont:.4f}  [{elapsed:.1f}s]")

    for key in ["sim_exponent", "sim_stderr", "discrete_exponent", "continuous_exponent"]:
        results[key] = np.array(results[key])

    return results


def plot_variant_c(results: dict, save_path: Optional[Path] = None):
    """Plot exponent vs eta for Variant C."""
    fig, ax = plt.subplots(figsize=(10, 7))

    eta = results["eta"]

    ax.errorbar(eta, results["sim_exponent"],
                yerr=2 * results["sim_stderr"],
                fmt="o-", color="#1f77b4", markersize=8, capsize=5,
                linewidth=2, label="Simulation (linear correction)")

    ax.plot(eta, results["discrete_exponent"],
            "s--", color="#2ca02c", markersize=7, linewidth=1.5,
            label="Analytical: discrete AR(1)")

    ax.plot(eta, results["continuous_exponent"],
            "^:", color="#d62728", markersize=7, linewidth=1.5,
            label="Analytical: continuous ODE")

    ax.axhline(y=2.0, color="k", linestyle="--", linewidth=2.5, alpha=0.6,
               label="Corollary 11.2 prediction (b=2)")
    ax.axhline(y=1.0, color="gray", linestyle=":", alpha=0.5,
               label="Linear advantage (b=1)")

    ax.set_xscale("log")
    ax.set_xlabel(r"$\eta$ (= $\mathcal{T}_B$)")
    ax.set_ylabel("Effective exponent $b$")
    ax.set_title(
        "Variant C: Does Exponent Approach 2.0 as $\\eta \\to 0$?\n"
        f"($q_{{\\mathrm{{base}}}}={0.05}$, $\\gamma={0.5}$, "
        "linear correction)"
    )
    ax.legend(fontsize=10, loc="best")
    ax.set_ylim(0.5, 2.5)
    ax.invert_xaxis()

    fig.tight_layout()
    if save_path:
        fig.savefig(save_path)
        print(f"  Saved: {save_path}")
    return fig


# ---------------------------------------------------------------------------
# Variant D: Approaching the coupling-dominant regime
# ---------------------------------------------------------------------------

def run_variant_d():
    """Sweep q_base and measure how the exponent changes."""
    print("\n" + "=" * 70)
    print("VARIANT D: Approaching the Coupling-Dominant Regime")
    print("=" * 70)

    eta = 0.01  # approaching continuous limit
    q_base_values = np.array([0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001, 0.0001])
    gamma = 0.5
    tempo_ratios = np.logspace(np.log10(0.5), np.log10(5.0), 15)

    results = {
        "q_base": q_base_values,
        "eta": eta,
        "sim_exponent": [],
        "sim_stderr": [],
        "discrete_exponent": [],
        "continuous_exponent": [],
        "coupling_ratio": [],  # gamma*T_B / q_base (measure of coupling dominance)
    }

    for q_base in q_base_values:
        t0 = time.time()

        coupling_ratio = gamma * eta / q_base
        results["coupling_ratio"].append(coupling_ratio)

        # Analytical predictions
        b_disc, _ = analytical_discrete_exponent(eta, q_base, gamma, tempo_ratios)
        b_cont, _ = analytical_continuous_exponent(eta, q_base, gamma, tempo_ratios)

        # Simulation
        num_trials = 60
        b_sim, se_sim, _, _ = measure_exponent_at_params(
            eta, q_base, gamma, num_trials=num_trials, tempo_ratios=tempo_ratios,
        )

        elapsed = time.time() - t0
        results["sim_exponent"].append(b_sim)
        results["sim_stderr"].append(se_sim)
        results["discrete_exponent"].append(b_disc)
        results["continuous_exponent"].append(b_cont)

        print(f"  q_base={q_base:.4f} (gamma*T/q={coupling_ratio:.2f}): "
              f"sim={b_sim:.4f}+/-{se_sim:.4f}, "
              f"discrete={b_disc:.4f}, continuous={b_cont:.4f}  [{elapsed:.1f}s]")

    for key in ["sim_exponent", "sim_stderr", "discrete_exponent",
                "continuous_exponent", "coupling_ratio"]:
        results[key] = np.array(results[key])

    return results


def plot_variant_d(results: dict, save_path: Optional[Path] = None):
    """Plot exponent vs q_base for Variant D."""
    fig, ax = plt.subplots(figsize=(10, 7))

    q_base = results["q_base"]
    eta = results["eta"]

    ax.errorbar(q_base, results["sim_exponent"],
                yerr=2 * results["sim_stderr"],
                fmt="o-", color="#1f77b4", markersize=8, capsize=5,
                linewidth=2, label="Simulation (linear correction)")

    ax.plot(q_base, results["discrete_exponent"],
            "s--", color="#2ca02c", markersize=7, linewidth=1.5,
            label="Analytical: discrete AR(1)")

    ax.plot(q_base, results["continuous_exponent"],
            "^:", color="#d62728", markersize=7, linewidth=1.5,
            label="Analytical: continuous ODE")

    ax.axhline(y=2.0, color="k", linestyle="--", linewidth=2.5, alpha=0.6,
               label="Corollary 11.2 prediction (b=2)")
    ax.axhline(y=1.0, color="gray", linestyle=":", alpha=0.5,
               label="Linear advantage (b=1)")

    # Secondary x-axis: coupling ratio
    ax2 = ax.twiny()
    ax2.set_xscale("log")
    coupling_ticks = results["coupling_ratio"]
    ax2.set_xlim(ax.get_xlim())
    # Place tick labels at a few representative q_base values
    selected_idx = [0, 2, 4, 6, 7]
    ax2.set_xticks([q_base[i] for i in selected_idx])
    ax2.set_xticklabels([f"{coupling_ticks[i]:.1f}" for i in selected_idx])
    ax2.set_xlabel(r"$\gamma \cdot \mathcal{T}_B / q_{\mathrm{base}}$ (coupling dominance)")

    ax.set_xscale("log")
    ax.set_xlabel(r"$q_{\mathrm{base}}$")
    ax.set_ylabel("Effective exponent $b$")
    ax.set_title(
        "Variant D: Does Exponent Approach 2.0 as $q_{\\mathrm{base}} \\to 0$?\n"
        f"($\\eta={eta}$, $\\gamma={0.5}$, linear correction)"
    )
    ax.legend(fontsize=10, loc="best")
    ax.set_ylim(0.5, 2.5)
    ax.invert_xaxis()

    fig.tight_layout()
    if save_path:
        fig.savefig(save_path)
        print(f"  Saved: {save_path}")
    return fig


# ---------------------------------------------------------------------------
# Combined deep-regime test
# ---------------------------------------------------------------------------

def run_deep_regime():
    """Test the deepest regime: eta=0.001 AND q_base=0.001."""
    print("\n" + "=" * 70)
    print("DEEP REGIME: eta=0.001, q_base=0.001")
    print("=" * 70)

    eta = 0.001
    q_base = 0.001
    gamma = 0.5
    tempo_ratios = np.logspace(np.log10(0.5), np.log10(5.0), 12)

    t0 = time.time()

    # Analytical
    b_disc, se_disc = analytical_discrete_exponent(eta, q_base, gamma, tempo_ratios)
    b_cont, se_cont = analytical_continuous_exponent(eta, q_base, gamma, tempo_ratios)

    # Simulation (use fewer trials but long runs)
    b_sim, se_sim, ratios, medians = measure_exponent_at_params(
        eta, q_base, gamma, num_trials=20, tempo_ratios=tempo_ratios,
    )

    elapsed = time.time() - t0
    coupling_ratio = gamma * eta / q_base

    print(f"  gamma*T/q_base = {coupling_ratio:.2f}")
    print(f"  Simulation:  b = {b_sim:.4f} +/- {se_sim:.4f}")
    print(f"  Discrete:    b = {b_disc:.4f}")
    print(f"  Continuous:  b = {b_cont:.4f}")
    print(f"  [{elapsed:.1f}s]")

    return {
        "eta": eta,
        "q_base": q_base,
        "coupling_ratio": coupling_ratio,
        "sim_exponent": b_sim,
        "sim_stderr": se_sim,
        "discrete_exponent": b_disc,
        "continuous_exponent": b_cont,
        "tempo_ratios": ratios,
        "sim_medians": medians,
    }


# ---------------------------------------------------------------------------
# 2D Heatmap: exponent vs (eta, q_base)
# ---------------------------------------------------------------------------

def run_2d_sweep():
    """Compute analytical exponents over a 2D grid of (eta, q_base)."""
    print("\n" + "=" * 70)
    print("2D SWEEP: Analytical Exponents over (eta, q_base)")
    print("=" * 70)

    eta_values = np.logspace(-3, -0.5, 20)  # 0.001 to ~0.316
    q_base_values = np.logspace(-4, -0.5, 20)  # 0.0001 to ~0.316
    gamma = 0.5
    tempo_ratios = np.logspace(np.log10(0.5), np.log10(5.0), 20)

    discrete_grid = np.zeros((len(eta_values), len(q_base_values)))
    continuous_grid = np.zeros((len(eta_values), len(q_base_values)))

    for i, eta in enumerate(eta_values):
        for j, q_base in enumerate(q_base_values):
            b_disc, _ = analytical_discrete_exponent(eta, q_base, gamma, tempo_ratios)
            b_cont, _ = analytical_continuous_exponent(eta, q_base, gamma, tempo_ratios)
            discrete_grid[i, j] = b_disc
            continuous_grid[i, j] = b_cont

    print(f"  Discrete exponent range: [{np.nanmin(discrete_grid):.3f}, "
          f"{np.nanmax(discrete_grid):.3f}]")
    print(f"  Continuous exponent range: [{np.nanmin(continuous_grid):.3f}, "
          f"{np.nanmax(continuous_grid):.3f}]")

    return {
        "eta_values": eta_values,
        "q_base_values": q_base_values,
        "discrete_grid": discrete_grid,
        "continuous_grid": continuous_grid,
    }


def plot_2d_heatmap(sweep_2d: dict, save_path: Optional[Path] = None):
    """Plot 2D heatmap of exponent vs (eta, q_base)."""
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))

    eta = sweep_2d["eta_values"]
    q_base = sweep_2d["q_base_values"]

    for ax, grid, title in [
        (axes[0], sweep_2d["discrete_grid"], "Discrete AR(1) Exponent"),
        (axes[1], sweep_2d["continuous_grid"], "Continuous ODE Exponent"),
    ]:
        # meshgrid for pcolormesh
        Q, E = np.meshgrid(q_base, eta)
        im = ax.pcolormesh(Q, E, grid, cmap="RdYlBu_r",
                           vmin=1.0, vmax=2.0, shading="auto")
        cb = fig.colorbar(im, ax=ax, label="Exponent $b$")

        # Contour lines
        cs = ax.contour(Q, E, grid, levels=[1.5, 1.8, 1.9, 1.95, 2.0],
                        colors="black", linewidths=1.0, linestyles="--")
        ax.clabel(cs, inline=True, fontsize=9, fmt="%.2f")

        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlabel(r"$q_{\mathrm{base}}$")
        ax.set_ylabel(r"$\eta$ (= $\mathcal{T}_B$)")
        ax.set_title(title)

        # Mark the original sim2 parameters
        ax.plot(0.05, 0.1, "w*", markersize=15, markeredgecolor="k",
                markeredgewidth=1.5, label="Original sim2 params")
        ax.legend(fontsize=9, loc="upper left")

    fig.suptitle(
        "Effective Exponent $b$ in "
        "$\\|\\delta_B\\|/\\|\\delta_A\\| \\propto "
        "(\\mathcal{T}_A/\\mathcal{T}_B)^b$\n"
        "($\\gamma_A = \\gamma_B = 0.5$, linear correction)",
        fontsize=14,
    )
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path)
        print(f"  Saved: {save_path}")
    return fig


# ---------------------------------------------------------------------------
# Detailed ratio-vs-tempo plot for select parameter sets
# ---------------------------------------------------------------------------

def plot_ratio_comparison(
    variant_c_results: dict,
    variant_d_results: dict,
    deep_results: dict,
    save_path: Optional[Path] = None,
):
    """Plot mismatch ratio vs tempo ratio for a few representative parameter sets."""
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    gamma = 0.5
    tempo_ratios = np.logspace(np.log10(0.5), np.log10(5.0), 50)

    configs = [
        ("Original (eta=0.1, q=0.05)", 0.1, 0.05),
        ("Variant D (eta=0.01, q=0.001)", 0.01, 0.001),
        ("Deep regime (eta=0.001, q=0.001)", 0.001, 0.001),
    ]

    for ax, (title, eta, q_base) in zip(axes, configs):
        # Analytical curves
        disc_ratios = []
        cont_ratios = []
        coup_ratios = []
        for r in tempo_ratios:
            T_A = r * eta
            if T_A >= 2.0:
                disc_ratios.append(np.nan)
                cont_ratios.append(np.nan)
                coup_ratios.append(np.nan)
                continue
            p = RegimeParams(T_A=T_A, T_B=eta, gamma_A=gamma, gamma_B=gamma, q_base=q_base)
            disc_ratios.append(discrete_linear_prediction(p))
            cont_ratios.append(continuous_ode_prediction(p))
            coup_ratios.append(coupling_dominant_prediction(p))

        disc_ratios = np.array(disc_ratios)
        cont_ratios = np.array(cont_ratios)
        coup_ratios = np.array(coup_ratios)

        ax.plot(tempo_ratios, coup_ratios, "k--", linewidth=2.5, alpha=0.6,
                label="Coupling-dominant $(T_A/T_B)^2$")
        ax.plot(tempo_ratios, cont_ratios, "r:", linewidth=2, alpha=0.7,
                label="Continuous ODE")
        ax.plot(tempo_ratios, disc_ratios, "g-", linewidth=2, alpha=0.7,
                label="Discrete AR(1)")

        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlabel(r"$\mathcal{T}_A / \mathcal{T}_B$")
        ax.set_ylabel(r"$\|\delta_B\| / \|\delta_A\|$")
        ax.set_title(title, fontsize=11)
        ax.legend(fontsize=8)

    fig.suptitle(
        "Mismatch Ratio vs Tempo Ratio: Three Predictions Compared",
        fontsize=14,
    )
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path)
        print(f"  Saved: {save_path}")
    return fig


# ---------------------------------------------------------------------------
# Mathematical explanation
# ---------------------------------------------------------------------------

def print_mathematical_analysis():
    """Print the analytical derivation explaining why the exponent changes."""
    print("\n" + "=" * 70)
    print("MATHEMATICAL ANALYSIS: Why the Exponent Depends on Regime")
    print("=" * 70)
    print("""
The mismatch ratio for the discrete AR(1) process with linear correction is:

  ||delta_B|| / ||delta_A|| = [rho_B / sqrt(2*T_B - T_B^2)]
                             / [rho_A / sqrt(2*T_A - T_A^2)]

where:
  rho_B = q_base + gamma_A * T_A
  rho_A = q_base + gamma_B * T_B

Setting gamma_A = gamma_B = gamma and T_B = eta, T_A = r * eta:

  ratio = [q_base + gamma*r*eta] * sqrt(2*r*eta - (r*eta)^2)
        / [q_base + gamma*eta]   * sqrt(2*eta - eta^2)         ... (inverted A/B factor)

Wait -- more carefully:

  ratio = (rho_B / rho_A) * sqrt(2*T_A - T_A^2) / sqrt(2*T_B - T_B^2)

The DISCRETE correction factor: sqrt(2*T - T^2) = sqrt(T) * sqrt(2 - T)

  sqrt factor ratio = sqrt(r*eta * (2 - r*eta)) / sqrt(eta * (2 - eta))
                    = sqrt(r) * sqrt((2 - r*eta) / (2 - eta))

As eta -> 0:  sqrt factor ratio -> sqrt(r)

The NOISE ratio:
  rho_B / rho_A = (q_base + gamma*r*eta) / (q_base + gamma*eta)

As q_base -> 0:  rho_B / rho_A -> r

Combined continuous+coupling-dominant limit (eta->0 AND q_base->0):
  ratio -> r * sqrt(r) = r^(3/2) ???

Wait, let me redo this carefully. For the AR(1):
  Var[delta] = rho^2 / (1 - (1-T)^2) = rho^2 / (2T - T^2)
  Std[delta] = rho / sqrt(2T - T^2)
  E[|delta|] = rho * sqrt(2/pi) / sqrt(2T - T^2)

  ratio = [rho_B / sqrt(2*T_B - T_B^2)] / [rho_A / sqrt(2*T_A - T_A^2)]
        = (rho_B / rho_A) * sqrt(2*T_A - T_A^2) / sqrt(2*T_B - T_B^2)

With T_A = r*eta, T_B = eta:

  sqrt ratio = sqrt(2*r*eta - r^2*eta^2) / sqrt(2*eta - eta^2)
             = sqrt(r * (2 - r*eta)) / sqrt(2 - eta)
             = sqrt(r) * sqrt((2 - r*eta) / (2 - eta))

  As eta -> 0: sqrt ratio -> sqrt(r)

  rho_B/rho_A = (q + gamma*r*eta) / (q + gamma*eta)

  As q -> 0: rho_B/rho_A -> r

  Combined ratio -> r * sqrt(r) = r^{3/2}  ... exponent 1.5!

NOT 2.0. The continuous-ODE prediction is ratio = (rho_B/T_B) / (rho_A/T_A)
                                                = (rho_B/rho_A) * (T_A/T_B)
                                                = (rho_B/rho_A) * r

  As q -> 0: ratio -> r * r = r^2  ... exponent 2.0

The discrepancy arises because the ODE steady-state is delta_ss = rho/T,
but the AR(1) steady-state is rho/sqrt(2T - T^2). These differ:

  rho/T vs rho/sqrt(2T - T^2)

  sqrt(2T - T^2) = sqrt(T) * sqrt(2 - T)

  rho/sqrt(2T - T^2) = rho / (sqrt(T) * sqrt(2 - T))

So the AR(1) scales as rho/sqrt(T), not rho/T. The sqrt(2-T) factor -> sqrt(2)
as T -> 0, which is just a constant. The key scaling is 1/sqrt(T), not 1/T.

THIS IS THE ROOT CAUSE. The linear ODE gives delta_ss = rho/T (inversely
proportional to T). But the stochastic AR(1) process gives
E[|delta|] ~ rho/sqrt(T) (inversely proportional to sqrt(T)).

The ODE is for the MEAN of delta, but the stochastic process has delta
fluctuating around zero. The RMS is rho/sqrt(2T) for small T. The mean
|delta| is proportional to the RMS. So E[|delta|] ~ rho/sqrt(T), not rho/T.

This means the coupling-dominant exponent for the stochastic model is:
  ratio = (rho_B/sqrt(T_B)) / (rho_A/sqrt(T_A))
        = (rho_B/rho_A) * sqrt(T_A/T_B)
        = r * sqrt(r) = r^{3/2}  ... when q_base -> 0

  EXPONENT = 1.5, NOT 2.0

The squared law (exponent 2) comes from the DETERMINISTIC ODE with
delta_ss = rho/T. The stochastic version has delta_ss ~ rho/sqrt(T),
giving exponent 1.5. This is a fundamental distinction.
""")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("VARIANTS C & D: Testing TFT Squared Tempo Advantage Regimes")
    print("=" * 70)
    print("Using ONLY linear correction function.")
    print("All simulations use stochastic (zero-mean Gaussian) model.\n")

    # --- Variant C ---
    c_results = run_variant_c()
    plot_variant_c(c_results, save_path=FIGURE_DIR / "variant_c_exponent_vs_eta.png")

    # --- Variant D ---
    d_results = run_variant_d()
    plot_variant_d(d_results, save_path=FIGURE_DIR / "variant_d_exponent_vs_qbase.png")

    # --- Deep regime ---
    deep_results = run_deep_regime()

    # --- 2D sweep (analytical only, fast) ---
    sweep_2d = run_2d_sweep()
    plot_2d_heatmap(sweep_2d, save_path=FIGURE_DIR / "variant_cd_2d_heatmap.png")

    # --- Comparison plot ---
    plot_ratio_comparison(
        c_results, d_results, deep_results,
        save_path=FIGURE_DIR / "variant_cd_ratio_comparison.png",
    )

    # --- Mathematical analysis ---
    print_mathematical_analysis()

    # --- Final summary ---
    print("\n" + "=" * 70)
    print("SUMMARY OF ALL RESULTS")
    print("=" * 70)

    print("\nVariant C: Exponent vs eta (continuous-time limit)")
    print(f"  {'eta':<10} {'Sim':>10} {'Discrete':>10} {'Continuous':>10}")
    print(f"  {'-'*40}")
    for i, eta in enumerate(c_results["eta"]):
        print(f"  {eta:<10.4f} {c_results['sim_exponent'][i]:>10.4f} "
              f"{c_results['discrete_exponent'][i]:>10.4f} "
              f"{c_results['continuous_exponent'][i]:>10.4f}")

    print("\nVariant D: Exponent vs q_base (coupling-dominant limit)")
    print(f"  {'q_base':<10} {'gamma*T/q':>10} {'Sim':>10} {'Discrete':>10} {'Continuous':>10}")
    print(f"  {'-'*52}")
    for i, q in enumerate(d_results["q_base"]):
        print(f"  {q:<10.4f} {d_results['coupling_ratio'][i]:>10.2f} "
              f"{d_results['sim_exponent'][i]:>10.4f} "
              f"{d_results['discrete_exponent'][i]:>10.4f} "
              f"{d_results['continuous_exponent'][i]:>10.4f}")

    print(f"\nDeep regime (eta={deep_results['eta']}, q_base={deep_results['q_base']}):")
    print(f"  Coupling ratio: {deep_results['coupling_ratio']:.2f}")
    print(f"  Simulation:  b = {deep_results['sim_exponent']:.4f} +/- {deep_results['sim_stderr']:.4f}")
    print(f"  Discrete:    b = {deep_results['discrete_exponent']:.4f}")
    print(f"  Continuous:  b = {deep_results['continuous_exponent']:.4f}")

    print("\n2D sweep (analytical):")
    print(f"  Discrete exponent range: [{np.nanmin(sweep_2d['discrete_grid']):.3f}, "
          f"{np.nanmax(sweep_2d['discrete_grid']):.3f}]")
    print(f"  Continuous exponent range: [{np.nanmin(sweep_2d['continuous_grid']):.3f}, "
          f"{np.nanmax(sweep_2d['continuous_grid']):.3f}]")

    # Find where discrete exponent is closest to 2.0
    dg = sweep_2d["discrete_grid"]
    max_idx = np.unravel_index(np.nanargmax(dg), dg.shape)
    print(f"  Max discrete exponent {dg[max_idx]:.3f} at "
          f"eta={sweep_2d['eta_values'][max_idx[0]]:.4f}, "
          f"q_base={sweep_2d['q_base_values'][max_idx[1]]:.6f}")

    cg = sweep_2d["continuous_grid"]
    max_idx_c = np.unravel_index(np.nanargmax(cg), cg.shape)
    print(f"  Max continuous exponent {cg[max_idx_c]:.3f} at "
          f"eta={sweep_2d['eta_values'][max_idx_c[0]]:.4f}, "
          f"q_base={sweep_2d['q_base_values'][max_idx_c[1]]:.6f}")

    # --- Save numerical results ---
    np.savez(
        FIGURE_DIR / "variant_cd_results.npz",
        # Variant C
        c_eta=c_results["eta"],
        c_sim_exp=c_results["sim_exponent"],
        c_sim_se=c_results["sim_stderr"],
        c_disc_exp=c_results["discrete_exponent"],
        c_cont_exp=c_results["continuous_exponent"],
        # Variant D
        d_qbase=d_results["q_base"],
        d_coupling_ratio=d_results["coupling_ratio"],
        d_sim_exp=d_results["sim_exponent"],
        d_sim_se=d_results["sim_stderr"],
        d_disc_exp=d_results["discrete_exponent"],
        d_cont_exp=d_results["continuous_exponent"],
        # Deep
        deep_sim_exp=deep_results["sim_exponent"],
        deep_sim_se=deep_results["sim_stderr"],
        deep_disc_exp=deep_results["discrete_exponent"],
        deep_cont_exp=deep_results["continuous_exponent"],
        # 2D
        sweep_eta=sweep_2d["eta_values"],
        sweep_qbase=sweep_2d["q_base_values"],
        sweep_disc_grid=sweep_2d["discrete_grid"],
        sweep_cont_grid=sweep_2d["continuous_grid"],
    )
    print(f"\n  Saved: {FIGURE_DIR / 'variant_cd_results.npz'}")

    print("\nDone. Figures saved to:", FIGURE_DIR)


if __name__ == "__main__":
    main()
