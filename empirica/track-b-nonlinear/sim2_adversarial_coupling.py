"""
Simulation 2: Adversarial Coupling (Two Agents)

Tests TFT's squared tempo advantage (Corollary 11.2) under nonlinear correction
functions. Two agents A and B each track a drifting scalar target with adversarial
coupling: each agent's adaptive tempo contributes to the other's environmental
disturbance.

    rho_B = q_base + gamma_A * T_A
    rho_A = q_base + gamma_B * T_B

Under the linear ODE + linear coupling, the steady-state mismatch ratio is:

    ||delta_B||_ss / ||delta_A||_ss = (gamma_A / gamma_B) * (T_A / T_B)^2

The key question: does the squared exponent survive nonlinear correction dynamics?

Theory reference: TF-11 Corollary 11.2, Appendix A Propositions A.1-A.3.

Builds on correction functions from sim1_nonlinear_mismatch.py.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from dataclasses import dataclass
from typing import Callable, Dict, List, Tuple, Optional
import warnings

# Import correction functions from sim1
from sim1_nonlinear_mismatch import (
    CORRECTION_FUNCTIONS,
    CORRECTION_LABELS,
    COLORS,
)

# ---------------------------------------------------------------------------
# Output directory
# ---------------------------------------------------------------------------
OUTPUT_DIR = Path(__file__).parent
FIGURE_DIR = OUTPUT_DIR

# ---------------------------------------------------------------------------
# Plotting style (inherit from sim1, but set here for standalone runs)
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


# ---------------------------------------------------------------------------
# Parameters
# ---------------------------------------------------------------------------

@dataclass
class Sim2Params:
    """Parameters for Simulation 2 (adversarial coupling)."""
    # Agent tempos (T = eta with nu = 1)
    T_A: float = 0.1             # Agent A's adaptive tempo
    T_B: float = 0.1             # Agent B's adaptive tempo

    # Coupling coefficients
    gamma_A: float = 0.5         # A's disruption effectiveness on B
    gamma_B: float = 0.5         # B's disruption effectiveness on A

    # Base environmental noise (non-adversarial)
    q_base: float = 0.05         # Base noise std dev

    # Nonlinearity parameters
    R: float = 1.0               # Saturation radius
    epsilon: float = 0.1         # Dead zone threshold
    R_max: float = 2.0           # Breakdown radius

    # Simulation parameters
    num_steps: int = 20_000      # Total timesteps
    num_trials: int = 200        # Monte Carlo replicates
    burn_in: int = 5_000         # Steps to discard
    seed: int = 42               # Random seed

    @property
    def rho_A(self) -> float:
        """Effective disturbance rate on A (additive std coupling)."""
        return self.q_base + self.gamma_B * self.T_B

    @property
    def rho_B(self) -> float:
        """Effective disturbance rate on B (additive std coupling)."""
        return self.q_base + self.gamma_A * self.T_A

    @property
    def tempo_ratio(self) -> float:
        """T_A / T_B."""
        return self.T_A / self.T_B

    @property
    def gamma_ratio(self) -> float:
        """gamma_A / gamma_B."""
        return self.gamma_A / self.gamma_B

    @property
    def linear_mismatch_ratio(self) -> float:
        """Predicted ||delta_B||/||delta_A|| under linear theory.

        Uses the exact discrete-time AR(1) formula. For delta_{t+1} = (1-eta)*delta_t + w_t,
        the stationary std is rho / sqrt(2*eta - eta^2). The ratio of E[|delta|] equals
        the ratio of stationary stds (the sqrt(2/pi) factor cancels).

        The continuous-ODE prediction rho/T overestimates E[|delta|] for moderate eta;
        the discrete formula is exact for the simulation.
        """
        std_A = self.rho_A / np.sqrt(2 * self.T_A - self.T_A ** 2)
        std_B = self.rho_B / np.sqrt(2 * self.T_B - self.T_B ** 2)
        if std_A == 0:
            return np.inf
        return std_B / std_A

    @property
    def continuous_ode_mismatch_ratio(self) -> float:
        """Continuous-ODE prediction for comparison: (rho_B/T_B) / (rho_A/T_A)."""
        delta_B = self.rho_B / self.T_B
        delta_A = self.rho_A / self.T_A
        if delta_A == 0:
            return np.inf
        return delta_B / delta_A

    @property
    def coupling_dominant_ratio(self) -> float:
        """Coupling-dominant approximation: (gamma_A/gamma_B) * (T_A/T_B)^2."""
        return self.gamma_ratio * self.tempo_ratio ** 2

    def nonlinearity_kwargs(self) -> dict:
        """Return keyword arguments for correction functions."""
        return {"R": self.R, "epsilon": self.epsilon, "R_max": self.R_max}


# ---------------------------------------------------------------------------
# Core simulation: two coupled agents
# ---------------------------------------------------------------------------

def simulate_coupled_agents(
    g: Callable,
    params: Sim2Params,
) -> Tuple[np.ndarray, np.ndarray]:
    """Run Monte Carlo simulation of two adversarially coupled agents.

    Agent dynamics:
        delta_A_{t+1} = delta_A_t - T_A * g(delta_A_t) + w_A_t
        delta_B_{t+1} = delta_B_t - T_B * g(delta_B_t) + w_B_t

    where:
        w_A_t ~ N(0, rho_A^2),  rho_A = q_base + gamma_B * T_B
        w_B_t ~ N(0, rho_B^2),  rho_B = q_base + gamma_A * T_A

    Note: The adversarial coupling enters through the noise variance (disturbance
    rate), not through direct state coupling. This matches TF-11's formulation
    where rho is the environment change rate.

    Returns:
        (deltas_A, deltas_B): each of shape (num_trials, num_steps)
    """
    rng = np.random.default_rng(params.seed)
    n = params.num_trials
    T = params.num_steps
    kwargs = params.nonlinearity_kwargs()

    rho_A = params.rho_A
    rho_B = params.rho_B

    # Pre-generate noise
    noise_A = rng.normal(0.0, rho_A, size=(n, T))
    noise_B = rng.normal(0.0, rho_B, size=(n, T))

    # Initialize
    deltas_A = np.zeros((n, T))
    deltas_B = np.zeros((n, T))

    # Run forward
    for t in range(T - 1):
        corr_A = g(deltas_A[:, t], **kwargs)
        corr_B = g(deltas_B[:, t], **kwargs)
        deltas_A[:, t + 1] = deltas_A[:, t] - params.T_A * corr_A + noise_A[:, t]
        deltas_B[:, t + 1] = deltas_B[:, t] - params.T_B * corr_B + noise_B[:, t]

    return deltas_A, deltas_B


def steady_state_mismatch_ratio(
    deltas_A: np.ndarray,
    deltas_B: np.ndarray,
    burn_in: int,
) -> Tuple[float, float, float]:
    """Compute steady-state ||delta_B|| / ||delta_A|| with uncertainty.

    Returns:
        (median_ratio, p10_ratio, p90_ratio) across trials
    """
    # Per-trial time-averaged absolute mismatch
    ss_A = np.mean(np.abs(deltas_A[:, burn_in:]), axis=1)
    ss_B = np.mean(np.abs(deltas_B[:, burn_in:]), axis=1)

    # Avoid division by zero
    valid = ss_A > 1e-12
    if not np.any(valid):
        return np.nan, np.nan, np.nan

    ratios = ss_B[valid] / ss_A[valid]
    return np.median(ratios), np.percentile(ratios, 10), np.percentile(ratios, 90)


# ---------------------------------------------------------------------------
# M1: Mismatch ratio vs tempo ratio (the key plot)
# ---------------------------------------------------------------------------

def run_ratio_vs_tempo_sweep(
    tempo_ratios: np.ndarray,
    base_params: Sim2Params,
) -> Dict[str, Dict[str, np.ndarray]]:
    """Sweep T_A/T_B and measure mismatch ratio for each correction function.

    T_B is fixed; T_A = ratio * T_B.

    Returns:
        results[func_name] = {"median": ..., "p10": ..., "p90": ...}
    """
    results = {}
    for name, g in CORRECTION_FUNCTIONS.items():
        medians, p10s, p90s = [], [], []
        for r in tempo_ratios:
            p = Sim2Params(
                T_A=r * base_params.T_B,
                T_B=base_params.T_B,
                gamma_A=base_params.gamma_A,
                gamma_B=base_params.gamma_B,
                q_base=base_params.q_base,
                R=base_params.R,
                epsilon=base_params.epsilon,
                R_max=base_params.R_max,
                num_steps=base_params.num_steps,
                num_trials=base_params.num_trials,
                burn_in=base_params.burn_in,
                seed=base_params.seed,
            )
            dA, dB = simulate_coupled_agents(g, p)
            med, lo, hi = steady_state_mismatch_ratio(dA, dB, p.burn_in)
            medians.append(med)
            p10s.append(lo)
            p90s.append(hi)
        results[name] = {
            "median": np.array(medians),
            "p10": np.array(p10s),
            "p90": np.array(p90s),
        }
        print(f"  [M1] {name}: done ({len(tempo_ratios)} ratio points)")
    return results


def compute_full_linear_prediction(
    tempo_ratios: np.ndarray,
    base_params: Sim2Params,
) -> np.ndarray:
    """Compute the exact discrete-time linear prediction.

    For the AR(1) process delta_{t+1} = (1-eta)*delta_t + w_t with noise std rho,
    the stationary std is rho / sqrt(2*eta - eta^2). The ratio of E[|delta|] equals
    the ratio of stationary stds.

    This is the correct reference line for the simulation. The continuous-ODE
    prediction rho/T differs at moderate eta due to discretization.
    """
    predictions = []
    for r in tempo_ratios:
        rho_B = base_params.q_base + base_params.gamma_A * r * base_params.T_B
        rho_A = base_params.q_base + base_params.gamma_B * base_params.T_B
        T_A = r * base_params.T_B
        T_B = base_params.T_B
        std_A = rho_A / np.sqrt(2 * T_A - T_A ** 2)
        std_B = rho_B / np.sqrt(2 * T_B - T_B ** 2)
        predictions.append(std_B / std_A if std_A > 0 else np.inf)
    return np.array(predictions)


def compute_continuous_ode_prediction(
    tempo_ratios: np.ndarray,
    base_params: Sim2Params,
) -> np.ndarray:
    """Compute the continuous-ODE prediction: (rho_B/T_B) / (rho_A/T_A).

    This is TF-11's prediction in the continuous limit (eta -> 0). It overestimates
    the mismatch ratio at moderate eta but converges to the discrete-time prediction
    as eta -> 0.
    """
    predictions = []
    for r in tempo_ratios:
        rho_B = base_params.q_base + base_params.gamma_A * r * base_params.T_B
        rho_A = base_params.q_base + base_params.gamma_B * base_params.T_B
        T_A = r * base_params.T_B
        T_B = base_params.T_B
        delta_B = rho_B / T_B
        delta_A = rho_A / T_A
        predictions.append(delta_B / delta_A if delta_A > 0 else np.inf)
    return np.array(predictions)


def plot_ratio_vs_tempo(
    tempo_ratios: np.ndarray,
    results: Dict[str, Dict[str, np.ndarray]],
    base_params: Sim2Params,
    save_path: Optional[Path] = None,
):
    """Plot mismatch ratio vs tempo ratio on log-log axes."""
    fig, ax = plt.subplots(figsize=(9, 7))

    # Coupling-dominant prediction: (gamma_A/gamma_B) * (T_A/T_B)^2
    gamma_ratio = base_params.gamma_A / base_params.gamma_B
    coupling_dominant = gamma_ratio * tempo_ratios ** 2
    ax.plot(tempo_ratios, coupling_dominant, "k--", linewidth=2.5, alpha=0.7,
            label=f"$(\\gamma_A/\\gamma_B)(\\mathcal{{T}}_A/\\mathcal{{T}}_B)^2$"
                  f"  [slope=2]",
            zorder=10)

    # Exact discrete-time linear prediction
    full_linear = compute_full_linear_prediction(tempo_ratios, base_params)
    ax.plot(tempo_ratios, full_linear, "k:", linewidth=2, alpha=0.5,
            label="Discrete-time linear (exact for sim)",
            zorder=9)

    for name, data in results.items():
        color = COLORS[name]
        ax.plot(tempo_ratios, data["median"], "-o", color=color, markersize=5,
                label=CORRECTION_LABELS[name])
        ax.fill_between(tempo_ratios, data["p10"], data["p90"],
                        color=color, alpha=0.12)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Tempo ratio $\\mathcal{T}_A / \\mathcal{T}_B$")
    ax.set_ylabel("Mismatch ratio $\\|\\delta_B\\| / \\|\\delta_A\\|$")
    ax.set_title(
        f"Adversarial Mismatch Ratio vs. Tempo Ratio\n"
        f"($\\gamma_A={base_params.gamma_A}$, $\\gamma_B={base_params.gamma_B}$, "
        f"$q_{{\\mathrm{{base}}}}={base_params.q_base}$, "
        f"$\\mathcal{{T}}_B={base_params.T_B}$)"
    )
    ax.legend(fontsize=8, loc="upper left")
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path)
        print(f"  Saved: {save_path}")
    return fig


# ---------------------------------------------------------------------------
# M2: Effective exponent estimation
# ---------------------------------------------------------------------------

def estimate_exponent(
    tempo_ratios: np.ndarray,
    mismatch_ratios: np.ndarray,
    gamma_ratio: float = 1.0,
) -> Tuple[float, float]:
    """Estimate the effective exponent b in mismatch_ratio ~ gamma_ratio * (T_A/T_B)^b.

    Uses weighted least squares on log-transformed data.

    Returns:
        (b, b_stderr)
    """
    # Filter out NaN and non-positive values
    valid = np.isfinite(mismatch_ratios) & (mismatch_ratios > 0) & (tempo_ratios > 0)
    if np.sum(valid) < 3:
        return np.nan, np.nan

    x = np.log(tempo_ratios[valid])
    y = np.log(mismatch_ratios[valid] / gamma_ratio)

    # Least squares: y = a + b*x
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    ss_xx = np.sum((x - x_mean) ** 2)
    ss_xy = np.sum((x - x_mean) * (y - y_mean))

    if ss_xx < 1e-12:
        return np.nan, np.nan

    b = ss_xy / ss_xx
    a = y_mean - b * x_mean

    # Residual standard error
    y_pred = a + b * x
    residuals = y - y_pred
    s2 = np.sum(residuals ** 2) / (n - 2) if n > 2 else np.nan
    b_stderr = np.sqrt(s2 / ss_xx) if np.isfinite(s2) else np.nan

    return b, b_stderr


def run_exponent_analysis(
    tempo_ratios: np.ndarray,
    results: Dict[str, Dict[str, np.ndarray]],
    gamma_ratio: float = 1.0,
) -> Dict[str, Tuple[float, float]]:
    """Estimate effective exponent for each correction function.

    Returns:
        exponents[func_name] = (b, b_stderr)
    """
    exponents = {}
    for name, data in results.items():
        b, se = estimate_exponent(tempo_ratios, data["median"], gamma_ratio)
        exponents[name] = (b, se)
    return exponents


def plot_exponent_summary(
    exponents: Dict[str, Tuple[float, float]],
    save_path: Optional[Path] = None,
):
    """Bar chart of effective exponents with error bars."""
    fig, ax = plt.subplots(figsize=(9, 5))

    names = list(exponents.keys())
    bs = [exponents[n][0] for n in names]
    ses = [exponents[n][1] for n in names]
    colors = [COLORS[n] for n in names]
    labels = [CORRECTION_LABELS[n] for n in names]

    x_pos = np.arange(len(names))
    bars = ax.bar(x_pos, bs, yerr=[2 * se for se in ses], capsize=5,
                  color=colors, alpha=0.8, edgecolor="black", linewidth=0.5)

    ax.axhline(y=2.0, color="k", linestyle="--", linewidth=2, alpha=0.7,
               label="Predicted exponent = 2")
    ax.axhline(y=1.0, color="gray", linestyle=":", alpha=0.5,
               label="Linear advantage (exponent = 1)")

    ax.set_xticks(x_pos)
    ax.set_xticklabels([n.capitalize() for n in names], fontsize=10)
    ax.set_ylabel("Effective exponent $b$ in $\\|\\delta_B\\|/\\|\\delta_A\\| "
                   "\\propto (\\mathcal{T}_A/\\mathcal{T}_B)^b$")
    ax.set_title("Effective Tempo Advantage Exponent by Correction Function")
    ax.legend(fontsize=9)

    # Annotate each bar with its value
    for i, (b_val, se_val) in enumerate(zip(bs, ses)):
        ax.annotate(f"{b_val:.2f} +/- {2*se_val:.2f}",
                    xy=(i, b_val + 2 * se_val + 0.1),
                    ha="center", fontsize=9)

    ax.set_ylim(0, max(bs) + 1.0)
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path)
        print(f"  Saved: {save_path}")
    return fig


# ---------------------------------------------------------------------------
# M3: Effect of gamma asymmetry
# ---------------------------------------------------------------------------

def run_gamma_asymmetry_sweep(
    gamma_ratios: np.ndarray,
    base_params: Sim2Params,
    tempo_ratio: float = 2.0,
    func_name: str = "linear",
) -> Dict[str, np.ndarray]:
    """Sweep gamma_A/gamma_B at fixed tempo ratio, for one correction function.

    Returns:
        {"median": ..., "p10": ..., "p90": ..., "theory": ...}
    """
    g = CORRECTION_FUNCTIONS[func_name]
    medians, p10s, p90s, theory = [], [], [], []
    for gr in gamma_ratios:
        p = Sim2Params(
            T_A=tempo_ratio * base_params.T_B,
            T_B=base_params.T_B,
            gamma_A=gr * base_params.gamma_B,
            gamma_B=base_params.gamma_B,
            q_base=base_params.q_base,
            R=base_params.R,
            epsilon=base_params.epsilon,
            R_max=base_params.R_max,
            num_steps=base_params.num_steps,
            num_trials=base_params.num_trials,
            burn_in=base_params.burn_in,
            seed=base_params.seed,
        )
        dA, dB = simulate_coupled_agents(g, p)
        med, lo, hi = steady_state_mismatch_ratio(dA, dB, p.burn_in)
        medians.append(med)
        p10s.append(lo)
        p90s.append(hi)
        theory.append(p.linear_mismatch_ratio)

    return {
        "median": np.array(medians),
        "p10": np.array(p10s),
        "p90": np.array(p90s),
        "theory": np.array(theory),
    }


def plot_gamma_asymmetry(
    gamma_ratios: np.ndarray,
    results_by_func: Dict[str, Dict[str, np.ndarray]],
    tempo_ratio: float,
    save_path: Optional[Path] = None,
):
    """Plot mismatch ratio vs gamma_A/gamma_B for multiple correction functions."""
    fig, ax = plt.subplots(figsize=(9, 6))

    for name, data in results_by_func.items():
        color = COLORS[name]
        ax.plot(gamma_ratios, data["median"], "-o", color=color, markersize=5,
                label=CORRECTION_LABELS[name])
        ax.fill_between(gamma_ratios, data["p10"], data["p90"],
                        color=color, alpha=0.12)

    # Theoretical prediction for linear case
    if "linear" in results_by_func:
        ax.plot(gamma_ratios, results_by_func["linear"]["theory"], "k--",
                linewidth=2, alpha=0.7, label="Full linear prediction")

    ax.set_xlabel("$\\gamma_A / \\gamma_B$")
    ax.set_ylabel("Mismatch ratio $\\|\\delta_B\\| / \\|\\delta_A\\|$")
    ax.set_title(
        f"Effect of Coupling Asymmetry at "
        f"$\\mathcal{{T}}_A/\\mathcal{{T}}_B = {tempo_ratio}$"
    )
    ax.legend(fontsize=9)
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path)
        print(f"  Saved: {save_path}")
    return fig


# ---------------------------------------------------------------------------
# M4: Catastrophic collapse threshold (structural breakdown)
# ---------------------------------------------------------------------------

def run_collapse_threshold(
    tempo_ratios: np.ndarray,
    base_params: Sim2Params,
    divergence_threshold: float = 10.0,
) -> Dict[str, np.ndarray]:
    """Measure fraction of trials where B diverges, for each correction function.

    Returns:
        results[func_name] = array of divergence fractions
    """
    threshold = divergence_threshold * base_params.R_max
    results = {}
    for name, g in CORRECTION_FUNCTIONS.items():
        fracs = []
        for r in tempo_ratios:
            p = Sim2Params(
                T_A=r * base_params.T_B,
                T_B=base_params.T_B,
                gamma_A=base_params.gamma_A,
                gamma_B=base_params.gamma_B,
                q_base=base_params.q_base,
                R=base_params.R,
                epsilon=base_params.epsilon,
                R_max=base_params.R_max,
                num_steps=base_params.num_steps,
                num_trials=base_params.num_trials,
                burn_in=base_params.burn_in,
                seed=base_params.seed,
            )
            _, dB = simulate_coupled_agents(g, p)
            max_B = np.max(np.abs(dB[:, p.burn_in:]), axis=1)
            frac_diverge = np.mean(max_B > threshold)
            fracs.append(frac_diverge)
        results[name] = np.array(fracs)
        print(f"  [M4] {name}: done ({len(tempo_ratios)} ratio points)")
    return results


def plot_collapse_threshold(
    tempo_ratios: np.ndarray,
    collapse: Dict[str, np.ndarray],
    base_params: Sim2Params,
    save_path: Optional[Path] = None,
):
    """Plot B's divergence fraction vs tempo ratio."""
    fig, ax = plt.subplots(figsize=(9, 6))

    # Theoretical collapse threshold from Appendix A Prop A.3:
    # gamma_A * T_A > alpha_B * R_B - rho_B_base
    # => T_A > (T_B * R_max - q_base) / gamma_A
    # => T_A/T_B > (T_B * R_max - q_base) / (gamma_A * T_B)
    alpha_B = base_params.T_B
    R_B = base_params.R_max
    rho_B_base = base_params.q_base
    reserve_B = alpha_B * R_B - rho_B_base
    if base_params.gamma_A > 0:
        critical_T_A = reserve_B / base_params.gamma_A
        critical_ratio = critical_T_A / base_params.T_B
        ax.axvline(x=critical_ratio, color="gray", linestyle=":", linewidth=2,
                   alpha=0.7,
                   label=f"Prop A.3 threshold: $\\mathcal{{T}}_A/\\mathcal{{T}}_B$ "
                         f"= {critical_ratio:.1f}")

    for name, frac in collapse.items():
        ax.plot(tempo_ratios, frac, "-o", color=COLORS[name], markersize=5,
                label=CORRECTION_LABELS[name])

    ax.set_xlabel("Tempo ratio $\\mathcal{T}_A / \\mathcal{T}_B$")
    ax.set_ylabel("Fraction of trials where B diverges")
    ax.set_title(
        f"Catastrophic Collapse of Agent B vs. Tempo Ratio\n"
        f"($R_{{\\max}}={base_params.R_max}$, "
        f"$\\gamma_A={base_params.gamma_A}$, "
        f"$q_{{\\mathrm{{base}}}}={base_params.q_base}$)"
    )
    ax.legend(fontsize=8)
    ax.set_ylim(-0.05, 1.05)
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path)
        print(f"  Saved: {save_path}")
    return fig


# ---------------------------------------------------------------------------
# M5: Phase portrait of coupled system
# ---------------------------------------------------------------------------

def plot_coupled_phase_portrait(
    base_params: Sim2Params,
    tempo_ratio: float = 3.0,
    func_name: str = "breakdown",
    n_trajectories: int = 20,
    save_path: Optional[Path] = None,
):
    """Plot trajectories in (|delta_A|, |delta_B|) space for the coupled system."""
    g = CORRECTION_FUNCTIONS[func_name]
    p = Sim2Params(
        T_A=tempo_ratio * base_params.T_B,
        T_B=base_params.T_B,
        gamma_A=base_params.gamma_A,
        gamma_B=base_params.gamma_B,
        q_base=base_params.q_base,
        R=base_params.R,
        epsilon=base_params.epsilon,
        R_max=base_params.R_max,
        num_steps=base_params.num_steps,
        num_trials=n_trajectories,
        burn_in=0,
        seed=base_params.seed,
    )

    dA, dB = simulate_coupled_agents(g, p)

    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot a subsample of each trajectory
    subsample = max(1, p.num_steps // 2000)
    for i in range(n_trajectories):
        abs_A = np.abs(dA[i, ::subsample])
        abs_B = np.abs(dB[i, ::subsample])
        # Color by time (early = light, late = dark)
        ax.scatter(abs_A, abs_B, c=np.arange(len(abs_A)), cmap="viridis",
                   s=2, alpha=0.4, zorder=2)
        # Draw line for first trajectory to show flow
        if i == 0:
            ax.plot(abs_A, abs_B, "-", color="navy", alpha=0.3, linewidth=0.5,
                    zorder=1)

    # Mark R_max boundary
    ax.axvline(x=p.R_max, color=COLORS["breakdown"], linestyle="--", alpha=0.5,
               label=f"$R_{{\\max}} = {p.R_max}$")
    ax.axhline(y=p.R_max, color=COLORS["breakdown"], linestyle="--", alpha=0.5)

    # Mark theoretical steady states (linear)
    ss_A = p.rho_A / p.T_A
    ss_B = p.rho_B / p.T_B
    ax.plot(ss_A, ss_B, "k*", markersize=15, zorder=10,
            label=f"Linear SS: ({ss_A:.2f}, {ss_B:.2f})")

    ax.set_xlabel("$|\\delta_A|$")
    ax.set_ylabel("$|\\delta_B|$")
    ax.set_title(
        f"Phase Portrait: Coupled Agents ({func_name})\n"
        f"$\\mathcal{{T}}_A/\\mathcal{{T}}_B = {tempo_ratio}$"
    )
    ax.legend(fontsize=9)
    ax.set_aspect("equal")
    # Set reasonable limits
    max_val = min(max(np.percentile(np.abs(dB), 99), p.R_max * 2), p.R_max * 10)
    ax.set_xlim(0, max_val)
    ax.set_ylim(0, max_val)
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path)
        print(f"  Saved: {save_path}")
    return fig


# ---------------------------------------------------------------------------
# M6: Sensitivity of exponent to nonlinearity parameter R
# ---------------------------------------------------------------------------

def run_exponent_vs_R(
    R_values: np.ndarray,
    tempo_ratios: np.ndarray,
    base_params: Sim2Params,
    func_name: str = "saturating",
) -> Tuple[np.ndarray, np.ndarray]:
    """Sweep R (saturation radius) and estimate the effective exponent at each R.

    Returns:
        (exponents, stderrs) each of shape (len(R_values),)
    """
    g = CORRECTION_FUNCTIONS[func_name]
    exponents, stderrs = [], []

    for R_val in R_values:
        medians = []
        for r in tempo_ratios:
            p = Sim2Params(
                T_A=r * base_params.T_B,
                T_B=base_params.T_B,
                gamma_A=base_params.gamma_A,
                gamma_B=base_params.gamma_B,
                q_base=base_params.q_base,
                R=R_val,
                epsilon=base_params.epsilon,
                R_max=base_params.R_max,
                num_steps=base_params.num_steps,
                num_trials=base_params.num_trials,
                burn_in=base_params.burn_in,
                seed=base_params.seed,
            )
            dA, dB = simulate_coupled_agents(g, p)
            med, _, _ = steady_state_mismatch_ratio(dA, dB, p.burn_in)
            medians.append(med)

        medians = np.array(medians)
        gamma_ratio = base_params.gamma_A / base_params.gamma_B
        b, se = estimate_exponent(tempo_ratios, medians, gamma_ratio)
        exponents.append(b)
        stderrs.append(se)
        print(f"  [M6] R={R_val:.2f}: exponent = {b:.3f} +/- {se:.3f}")

    return np.array(exponents), np.array(stderrs)


def plot_exponent_vs_R(
    R_values: np.ndarray,
    exponents: np.ndarray,
    stderrs: np.ndarray,
    func_name: str = "saturating",
    save_path: Optional[Path] = None,
):
    """Plot effective exponent vs saturation radius R."""
    fig, ax = plt.subplots(figsize=(9, 6))

    ax.errorbar(R_values, exponents, yerr=2 * stderrs, fmt="-o",
                color=COLORS[func_name], markersize=6, capsize=4,
                label=f"Effective exponent ({func_name})")

    ax.axhline(y=2.0, color="k", linestyle="--", linewidth=2, alpha=0.7,
               label="Predicted exponent = 2 (linear limit)")
    ax.axhline(y=1.0, color="gray", linestyle=":", alpha=0.5,
               label="Linear advantage (exponent = 1)")

    ax.set_xscale("log")
    ax.set_xlabel("Saturation radius $R$")
    ax.set_ylabel("Effective exponent $b$")
    ax.set_title(
        f"How Nonlinearity Strength Affects the Tempo Advantage Exponent\n"
        f"({func_name} correction, $R \\to \\infty$ recovers linear)"
    )
    ax.legend(fontsize=9)
    ax.set_ylim(0, 3.0)
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path)
        print(f"  Saved: {save_path}")
    return fig


# ---------------------------------------------------------------------------
# Save numerical results
# ---------------------------------------------------------------------------

def save_results(
    tempo_ratios: np.ndarray,
    ratio_results: Dict[str, Dict[str, np.ndarray]],
    exponents: Dict[str, Tuple[float, float]],
    collapse_results: Dict[str, np.ndarray],
    R_sweep_R: Optional[np.ndarray] = None,
    R_sweep_exp: Optional[np.ndarray] = None,
    R_sweep_se: Optional[np.ndarray] = None,
    filepath: Optional[Path] = None,
):
    """Save all numerical results."""
    data = {"tempo_ratios": tempo_ratios}

    for name in CORRECTION_FUNCTIONS:
        for stat in ["median", "p10", "p90"]:
            data[f"ratio_{name}_{stat}"] = ratio_results[name][stat]
        b, se = exponents[name]
        data[f"exponent_{name}"] = np.array([b, se])
        data[f"collapse_{name}"] = collapse_results[name]

    if R_sweep_R is not None:
        data["R_sweep_R"] = R_sweep_R
        data["R_sweep_exponents"] = R_sweep_exp
        data["R_sweep_stderrs"] = R_sweep_se

    if filepath:
        np.savez(filepath, **data)
        print(f"  Saved numerical results: {filepath}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    """Run the full Simulation 2 parameter sweep and produce all figures."""
    print("=" * 70)
    print("SIMULATION 2: Adversarial Coupling (Two Agents)")
    print("=" * 70)

    base = Sim2Params(
        T_A=0.1,
        T_B=0.1,
        gamma_A=0.5,
        gamma_B=0.5,
        q_base=0.05,
        R=1.0,
        epsilon=0.1,
        R_max=2.0,
        num_steps=20_000,
        num_trials=200,
        burn_in=5_000,
        seed=42,
    )

    # Tempo ratio sweep (log-spaced from 0.5 to 5.0)
    tempo_ratios = np.logspace(np.log10(0.5), np.log10(5.0), 20)

    # --- M1: Mismatch ratio vs tempo ratio ---
    print("\n--- M1: Mismatch ratio vs tempo ratio ---")
    ratio_results = run_ratio_vs_tempo_sweep(tempo_ratios, base)
    fig1 = plot_ratio_vs_tempo(
        tempo_ratios, ratio_results, base,
        save_path=FIGURE_DIR / "sim2_fig1_ratio_vs_tempo.png",
    )

    # --- M2: Effective exponents ---
    print("\n--- M2: Effective exponent estimation ---")
    gamma_ratio = base.gamma_A / base.gamma_B
    exponents = run_exponent_analysis(tempo_ratios, ratio_results, gamma_ratio)

    print(f"\n  {'Function':<20} {'Exponent b':>12} {'95% CI':>20}")
    print(f"  {'-'*52}")
    for name, (b, se) in exponents.items():
        ci_lo = b - 2 * se
        ci_hi = b + 2 * se
        print(f"  {name:<20} {b:>12.3f} [{ci_lo:.3f}, {ci_hi:.3f}]")

    fig2 = plot_exponent_summary(
        exponents,
        save_path=FIGURE_DIR / "sim2_fig2_exponents.png",
    )

    # --- M3: Gamma asymmetry ---
    print("\n--- M3: Effect of gamma asymmetry ---")
    gamma_ratios = np.linspace(0.5, 2.0, 10)
    gamma_results = {}
    for func_name in ["linear", "saturating", "sigmoid"]:
        gamma_results[func_name] = run_gamma_asymmetry_sweep(
            gamma_ratios, base, tempo_ratio=2.0, func_name=func_name,
        )
        print(f"  [M3] {func_name}: done")

    fig3 = plot_gamma_asymmetry(
        gamma_ratios, gamma_results, tempo_ratio=2.0,
        save_path=FIGURE_DIR / "sim2_fig3_gamma_asymmetry.png",
    )

    # --- M4: Catastrophic collapse ---
    print("\n--- M4: Catastrophic collapse threshold ---")
    collapse_ratios = np.linspace(0.5, 5.0, 20)
    collapse_results = run_collapse_threshold(collapse_ratios, base)
    fig4 = plot_collapse_threshold(
        collapse_ratios, collapse_results, base,
        save_path=FIGURE_DIR / "sim2_fig4_collapse.png",
    )

    # --- M5: Phase portrait ---
    print("\n--- M5: Phase portrait (breakdown at T_A/T_B = 3.0) ---")
    fig5 = plot_coupled_phase_portrait(
        base, tempo_ratio=3.0, func_name="breakdown",
        save_path=FIGURE_DIR / "sim2_fig5_phaseportrait.png",
    )

    # --- M6: Exponent vs R (saturating) ---
    print("\n--- M6: Exponent sensitivity to saturation radius R ---")
    R_values = np.logspace(-0.5, 1.5, 12)  # ~0.3 to ~30
    # Use fewer ratio points for this sweep (computational efficiency)
    sweep_ratios = np.logspace(np.log10(0.5), np.log10(5.0), 12)
    R_exponents, R_stderrs = run_exponent_vs_R(R_values, sweep_ratios, base)
    fig6 = plot_exponent_vs_R(
        R_values, R_exponents, R_stderrs,
        save_path=FIGURE_DIR / "sim2_fig6_exponent_vs_R.png",
    )

    # --- Save all results ---
    print("\n--- Saving numerical results ---")
    save_results(
        tempo_ratios, ratio_results, exponents, collapse_results,
        R_sweep_R=R_values,
        R_sweep_exp=R_exponents,
        R_sweep_se=R_stderrs,
        filepath=FIGURE_DIR / "sim2_results.npz",
    )

    # --- Summary ---
    print("\n" + "=" * 70)
    print("SUMMARY: Effective Tempo Advantage Exponents")
    print("=" * 70)
    print(f"  Corollary 11.2 predicts exponent = 2.0")
    print(f"  {'Function':<20} {'Exponent':>10} {'Interpretation':>30}")
    print(f"  {'-'*60}")
    for name, (b, se) in exponents.items():
        if abs(b - 2.0) < 2 * se:
            interp = "Consistent with squared"
        elif b > 2.0:
            interp = "SUPER-squared (unexpected)"
        elif b > 1.5:
            interp = "Sub-squared but superlinear"
        elif b > 1.0:
            interp = "Weakly superlinear"
        else:
            interp = "Linear or sublinear"
        print(f"  {name:<20} {b:>10.3f} {interp:>30}")

    print(f"\n  Saturation radius sweep (saturating correction):")
    print(f"  R -> infinity: exponent -> 1.5 (stochastic coupling limit; 2.0 only under deterministic drift)")
    print(f"  R -> 0: exponent -> ? (strongly nonlinear limit)")
    for i, (R_val, exp_val) in enumerate(zip(R_values, R_exponents)):
        print(f"    R = {R_val:>6.2f}: exponent = {exp_val:.3f}")

    print("\nDone. Figures saved to:", FIGURE_DIR)
    plt.show()


if __name__ == "__main__":
    main()
