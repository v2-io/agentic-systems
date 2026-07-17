"""
Variant A/B: Deterministic Drift vs Stochastic Drift Disturbance Models

Tests whether TF-11's squared tempo advantage (Corollary 11.2) emerges when
the disturbance model matches the ODE's deterministic rho, rather than the
zero-mean Gaussian random walk used in sim1/sim2.

TF-11's mismatch ODE: d||delta||/dt = -T * ||delta|| + rho
This assumes a DETERMINISTIC, CONSTANT disturbance rate rho.

The existing sims use x_{t+1} = x_t + q*epsilon (zero-mean Gaussian random
walk), which produces an AR(1)/OU-like process with stochastic rho. This is
NOT the same as TF-11's deterministic rho. The mismatch exponent came out
~1.05 for linear, not the predicted 2.0.

Variant A: Pure deterministic drift.
    Environment: x_{t+1} = x_t + rho  (constant positive drift, no noise)
    Agent:       xhat_{t+1} = xhat_t + eta * g(x_t - xhat_t)
    Mismatch:    delta_{t+1} = delta_t - eta * g(delta_t) + rho

    This is the exact discrete-time analog of TF-11's ODE. Steady state for
    linear correction: delta_ss = rho / eta (= rho / T, matching the ODE).

    Adversarial: rho_B = rho_base + gamma_A * T_A
                 rho_A = rho_base + gamma_B * T_B

Variant B: Stochastic with positive mean drift (interpolation).
    Environment: x_{t+1} = x_t + mu + sigma * epsilon,  epsilon ~ N(0,1)
    Mismatch:    delta_{t+1} = delta_t - eta * g(delta_t) + mu + sigma * epsilon

    Interpolates between:
      mu=0, sigma>0:  the original sim (pure stochastic)
      mu>0, sigma=0:  Variant A (pure deterministic)

    Sweeps mu/sigma ratio from 0 to large, measuring adversarial exponent.

Key question: does the squared advantage (exponent = 2) appear when the
disturbance model matches TF-11's deterministic rho?
"""

import sys
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Callable, Dict, Tuple, Optional

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
# VARIANT A: Deterministic Drift
# ============================================================================

@dataclass
class VariantAParams:
    """Parameters for Variant A (deterministic drift)."""
    # Agent tempo (T = eta with nu = 1)
    eta: float = 0.1

    # Deterministic drift rate
    rho: float = 0.05

    # Nonlinearity parameters
    R: float = 1.0
    epsilon: float = 0.1
    R_max: float = 2.0

    # Simulation parameters
    num_steps: int = 20_000
    burn_in: int = 5_000

    @property
    def T(self) -> float:
        """Adaptive tempo (= eta with nu = 1)."""
        return self.eta

    @property
    def linear_ss(self) -> float:
        """Steady-state mismatch for linear correction: rho / eta."""
        return self.rho / self.eta

    def nonlinearity_kwargs(self) -> dict:
        return {"R": self.R, "epsilon": self.epsilon, "R_max": self.R_max}


@dataclass
class VariantAAdversarialParams:
    """Parameters for Variant A adversarial (deterministic drift)."""
    T_A: float = 0.1
    T_B: float = 0.1
    gamma_A: float = 0.5
    gamma_B: float = 0.5
    rho_base: float = 0.01

    R: float = 1.0
    epsilon: float = 0.1
    R_max: float = 2.0

    num_steps: int = 20_000
    burn_in: int = 5_000

    @property
    def rho_A(self) -> float:
        """Deterministic drift rate for A: rho_base + gamma_B * T_B."""
        return self.rho_base + self.gamma_B * self.T_B

    @property
    def rho_B(self) -> float:
        """Deterministic drift rate for B: rho_base + gamma_A * T_A."""
        return self.rho_base + self.gamma_A * self.T_A

    @property
    def linear_mismatch_ratio(self) -> float:
        """Predicted ratio under linear ODE: (rho_B / T_B) / (rho_A / T_A)."""
        delta_A = self.rho_A / self.T_A
        delta_B = self.rho_B / self.T_B
        if delta_A == 0:
            return np.inf
        return delta_B / delta_A

    @property
    def coupling_dominant_ratio(self) -> float:
        """Coupling-dominant prediction: (gamma_A/gamma_B) * (T_A/T_B)^2."""
        return (self.gamma_A / self.gamma_B) * (self.T_A / self.T_B) ** 2

    def nonlinearity_kwargs(self) -> dict:
        return {"R": self.R, "epsilon": self.epsilon, "R_max": self.R_max}


def simulate_variant_a_single(
    g: Callable,
    params: VariantAParams,
) -> np.ndarray:
    """Simulate single agent under deterministic drift.

    delta_{t+1} = delta_t - eta * g(delta_t) + rho

    This is deterministic (no stochasticity), so only one trajectory needed.

    Returns:
        deltas: array of shape (num_steps,)
    """
    n = params.num_steps
    kwargs = params.nonlinearity_kwargs()
    deltas = np.zeros(n)

    for t in range(n - 1):
        correction = g(np.array([deltas[t]]), **kwargs)[0]
        deltas[t + 1] = deltas[t] - params.eta * correction + params.rho

    return deltas


def simulate_variant_a_adversarial(
    g: Callable,
    params: VariantAAdversarialParams,
) -> Tuple[np.ndarray, np.ndarray]:
    """Simulate two adversarially coupled agents under deterministic drift.

    delta_A_{t+1} = delta_A_t - T_A * g(delta_A_t) + rho_A
    delta_B_{t+1} = delta_B_t - T_B * g(delta_B_t) + rho_B

    where rho_A = rho_base + gamma_B * T_B, rho_B = rho_base + gamma_A * T_A.

    Deterministic: one trajectory each.

    Returns:
        (deltas_A, deltas_B): each of shape (num_steps,)
    """
    n = params.num_steps
    kwargs = params.nonlinearity_kwargs()

    deltas_A = np.zeros(n)
    deltas_B = np.zeros(n)
    rho_A = params.rho_A
    rho_B = params.rho_B

    for t in range(n - 1):
        corr_A = g(np.array([deltas_A[t]]), **kwargs)[0]
        corr_B = g(np.array([deltas_B[t]]), **kwargs)[0]
        deltas_A[t + 1] = deltas_A[t] - params.T_A * corr_A + rho_A
        deltas_B[t + 1] = deltas_B[t] - params.T_B * corr_B + rho_B

    return deltas_A, deltas_B


def run_variant_a_single_agent():
    """Test single-agent steady state under deterministic drift."""
    print("\n" + "=" * 70)
    print("VARIANT A: Single-Agent Steady State (Deterministic Drift)")
    print("=" * 70)

    base = VariantAParams(eta=0.1, rho=0.05, num_steps=20_000, burn_in=5_000)

    print(f"\n  Parameters: eta = {base.eta}, rho = {base.rho}")
    print(f"  Linear prediction: delta_ss = rho/eta = {base.linear_ss:.4f}")

    fig, axes = plt.subplots(2, 3, figsize=(15, 9))
    axes_flat = axes.ravel()

    results = {}
    for idx, (name, g) in enumerate(CORRECTION_FUNCTIONS.items()):
        deltas = simulate_variant_a_single(g, base)
        ss_value = np.mean(np.abs(deltas[base.burn_in:]))
        ss_final = np.abs(deltas[-1])
        results[name] = {
            "ss_mean": ss_value,
            "ss_final": ss_final,
            "trajectory": deltas,
        }

        ax = axes_flat[idx]
        ax.plot(np.abs(deltas[:2000]), color=COLORS[name], linewidth=0.8)
        ax.axhline(y=base.linear_ss, color="k", linestyle="--", alpha=0.5,
                    label=f"$\\rho/\\eta$ = {base.linear_ss:.3f}")
        ax.axhline(y=ss_value, color=COLORS[name], linestyle="-", alpha=0.7,
                    linewidth=2, label=f"SS = {ss_value:.4f}")
        ax.set_title(f"{name}: SS = {ss_value:.4f}", fontsize=10)
        ax.set_xlabel("Timestep")
        ax.set_ylabel("$|\\delta_t|$")
        ax.legend(fontsize=7)

        print(f"  {name:<20} SS mean = {ss_value:.6f}  "
              f"SS final = {ss_final:.6f}  "
              f"ratio to rho/eta = {ss_value / base.linear_ss:.4f}")

    axes_flat[-1].set_visible(False)
    fig.suptitle(
        f"Variant A: Single-Agent Convergence under Deterministic Drift\n"
        f"($\\eta = {base.eta}$, $\\rho = {base.rho}$, "
        f"prediction: $\\delta_{{ss}} = \\rho/\\eta = {base.linear_ss}$)",
        fontsize=13,
    )
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "variant_a_single_agent.png")
    print(f"  Saved: {OUTPUT_DIR / 'variant_a_single_agent.png'}")

    return results


def run_variant_a_adversarial():
    """Test adversarial exponent under deterministic drift.

    Sweep T_A/T_B and measure mismatch ratio. Under deterministic drift,
    the steady state is exact (no stochastic fluctuations), so the exponent
    measurement should be clean.
    """
    print("\n" + "=" * 70)
    print("VARIANT A: Adversarial Exponent (Deterministic Drift)")
    print("=" * 70)

    base = VariantAAdversarialParams(
        T_A=0.1, T_B=0.1,
        gamma_A=0.5, gamma_B=0.5,
        rho_base=0.01,
        R=1.0, epsilon=0.1, R_max=2.0,
        num_steps=20_000, burn_in=5_000,
    )

    # Tempo ratio sweep
    tempo_ratios = np.logspace(np.log10(0.5), np.log10(5.0), 25)

    print(f"\n  Parameters: T_B = {base.T_B}, gamma = {base.gamma_A}, "
          f"rho_base = {base.rho_base}")
    print(f"  Sweeping T_A/T_B from {tempo_ratios[0]:.2f} to {tempo_ratios[-1]:.2f}")

    all_results = {}
    for name, g in CORRECTION_FUNCTIONS.items():
        ratios = []
        ss_A_list = []
        ss_B_list = []
        for r in tempo_ratios:
            p = VariantAAdversarialParams(
                T_A=r * base.T_B,
                T_B=base.T_B,
                gamma_A=base.gamma_A,
                gamma_B=base.gamma_B,
                rho_base=base.rho_base,
                R=base.R, epsilon=base.epsilon, R_max=base.R_max,
                num_steps=base.num_steps, burn_in=base.burn_in,
            )
            dA, dB = simulate_variant_a_adversarial(g, p)

            # Steady-state: take mean of absolute values after burn-in
            ss_A = np.mean(np.abs(dA[p.burn_in:]))
            ss_B = np.mean(np.abs(dB[p.burn_in:]))
            ss_A_list.append(ss_A)
            ss_B_list.append(ss_B)

            if ss_A > 1e-12:
                ratios.append(ss_B / ss_A)
            else:
                ratios.append(np.nan)

        all_results[name] = {
            "ratios": np.array(ratios),
            "ss_A": np.array(ss_A_list),
            "ss_B": np.array(ss_B_list),
        }
        print(f"  [Adv] {name}: done ({len(tempo_ratios)} ratio points)")

    # Estimate exponents
    gamma_ratio = base.gamma_A / base.gamma_B
    exponents = {}
    for name, data in all_results.items():
        b, se = _estimate_exponent(tempo_ratios, data["ratios"], gamma_ratio)
        exponents[name] = (b, se)

    # Compute theoretical predictions
    # Full linear ODE: (rho_B / T_B) / (rho_A / T_A)
    ode_pred = []
    coupling_dominant_pred = gamma_ratio * tempo_ratios ** 2
    for r in tempo_ratios:
        rho_B = base.rho_base + base.gamma_A * r * base.T_B
        rho_A = base.rho_base + base.gamma_B * base.T_B
        T_A = r * base.T_B
        T_B = base.T_B
        delta_B = rho_B / T_B
        delta_A = rho_A / T_A
        ode_pred.append(delta_B / delta_A if delta_A > 0 else np.inf)
    ode_pred = np.array(ode_pred)

    # --- Plot: mismatch ratio vs tempo ratio ---
    fig, ax = plt.subplots(figsize=(10, 7))

    ax.plot(tempo_ratios, coupling_dominant_pred, "k--", linewidth=2.5, alpha=0.7,
            label=f"Coupling-dominant: $(\\gamma_A/\\gamma_B)(T_A/T_B)^2$ [slope=2]",
            zorder=10)
    ax.plot(tempo_ratios, ode_pred, "k:", linewidth=2, alpha=0.5,
            label="Full linear ODE: $(\\rho_B/T_B)/(\\rho_A/T_A)$",
            zorder=9)

    for name, data in all_results.items():
        color = COLORS[name]
        ax.plot(tempo_ratios, data["ratios"], "-o", color=color, markersize=5,
                label=f"{name} (b={exponents[name][0]:.3f})")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Tempo ratio $T_A / T_B$")
    ax.set_ylabel("Mismatch ratio $|\\delta_B|_{ss} / |\\delta_A|_{ss}$")
    ax.set_title(
        f"Variant A: Adversarial Mismatch Ratio (Deterministic Drift)\n"
        f"($\\gamma = {base.gamma_A}$, $\\rho_{{base}} = {base.rho_base}$, "
        f"$T_B = {base.T_B}$)"
    )
    ax.legend(fontsize=8, loc="upper left")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "variant_a_adversarial_ratio.png")
    print(f"  Saved: {OUTPUT_DIR / 'variant_a_adversarial_ratio.png'}")

    # --- Plot: exponent bar chart ---
    fig2, ax2 = plt.subplots(figsize=(9, 5))
    names = list(exponents.keys())
    bs = [exponents[n][0] for n in names]
    ses = [exponents[n][1] for n in names]
    colors_list = [COLORS[n] for n in names]

    x_pos = np.arange(len(names))
    ax2.bar(x_pos, bs, yerr=[2 * se for se in ses], capsize=5,
            color=colors_list, alpha=0.8, edgecolor="black", linewidth=0.5)
    ax2.axhline(y=2.0, color="k", linestyle="--", linewidth=2, alpha=0.7,
                label="Predicted exponent = 2")
    ax2.axhline(y=1.0, color="gray", linestyle=":", alpha=0.5,
                label="Linear (exponent = 1)")
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels([n.capitalize() for n in names], fontsize=10)
    ax2.set_ylabel("Effective exponent $b$")
    ax2.set_title("Variant A: Effective Tempo Advantage Exponent (Deterministic Drift)")
    ax2.legend(fontsize=9)
    for i, (b_val, se_val) in enumerate(zip(bs, ses)):
        ax2.annotate(f"{b_val:.3f}",
                     xy=(i, b_val + 2 * se_val + 0.05),
                     ha="center", fontsize=9)
    ax2.set_ylim(0, max(max(bs) + 0.5, 2.5))
    fig2.tight_layout()
    fig2.savefig(OUTPUT_DIR / "variant_a_adversarial_exponents.png")
    print(f"  Saved: {OUTPUT_DIR / 'variant_a_adversarial_exponents.png'}")

    # Print summary
    print(f"\n  {'Function':<20} {'Exponent b':>12} {'95% CI':>22}")
    print(f"  {'-'*54}")
    for name, (b, se) in exponents.items():
        ci_lo = b - 2 * se
        ci_hi = b + 2 * se
        print(f"  {name:<20} {b:>12.4f} [{ci_lo:.4f}, {ci_hi:.4f}]")

    return all_results, exponents


def run_variant_a_coupling_dominance():
    """Test the coupling-dominance regime by varying rho_base.

    The squared law applies when adversarial coupling dominates base
    disturbance. Sweep rho_base from large (base-dominated) to near-zero
    (coupling-dominated) and measure exponent at each point.
    """
    print("\n" + "=" * 70)
    print("VARIANT A: Exponent vs Coupling Dominance")
    print("=" * 70)

    rho_base_values = np.logspace(-4, -0.5, 15)
    tempo_ratios = np.logspace(np.log10(0.5), np.log10(5.0), 20)

    T_B = 0.1
    gamma = 0.5
    # Coupling term = gamma * T ~ 0.5 * 0.1 = 0.05 at T_A/T_B = 1
    # So rho_base << 0.05 means coupling-dominated

    exponents_by_rho = []
    stderrs_by_rho = []

    for rho_base in rho_base_values:
        ratios = []
        g = CORRECTION_FUNCTIONS["linear"]
        for r in tempo_ratios:
            p = VariantAAdversarialParams(
                T_A=r * T_B, T_B=T_B,
                gamma_A=gamma, gamma_B=gamma,
                rho_base=rho_base,
                num_steps=20_000, burn_in=5_000,
            )
            dA, dB = simulate_variant_a_adversarial(g, p)
            ss_A = np.mean(np.abs(dA[p.burn_in:]))
            ss_B = np.mean(np.abs(dB[p.burn_in:]))
            ratios.append(ss_B / ss_A if ss_A > 1e-12 else np.nan)

        b, se = _estimate_exponent(tempo_ratios, np.array(ratios), 1.0)
        exponents_by_rho.append(b)
        stderrs_by_rho.append(se)
        coupling_strength = gamma * T_B  # typical coupling contribution
        print(f"  rho_base = {rho_base:.5f}  "
              f"(rho_base / coupling ~ {rho_base / coupling_strength:.3f})  "
              f"exponent = {b:.4f}")

    exponents_by_rho = np.array(exponents_by_rho)
    stderrs_by_rho = np.array(stderrs_by_rho)

    # Plot
    fig, ax = plt.subplots(figsize=(9, 6))
    coupling_term = gamma * T_B
    x_axis = rho_base_values / coupling_term  # ratio of base to coupling

    ax.errorbar(x_axis, exponents_by_rho, yerr=2 * stderrs_by_rho,
                fmt="-o", color=COLORS["linear"], markersize=6, capsize=4)
    ax.axhline(y=2.0, color="k", linestyle="--", linewidth=2, alpha=0.7,
               label="Predicted: exponent = 2")
    ax.axhline(y=1.0, color="gray", linestyle=":", alpha=0.5,
               label="Linear advantage")
    ax.set_xscale("log")
    ax.set_xlabel("$\\rho_{base} / (\\gamma \\cdot T_B)$  "
                   "(base-to-coupling ratio)")
    ax.set_ylabel("Effective exponent $b$")
    ax.set_title(
        "Variant A: Exponent vs Coupling Dominance (Linear Correction)\n"
        "Left = coupling-dominated, Right = base-dominated"
    )
    ax.legend(fontsize=9)
    ax.set_ylim(0, max(np.max(exponents_by_rho) + 0.3, 2.5))
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "variant_a_coupling_dominance.png")
    print(f"  Saved: {OUTPUT_DIR / 'variant_a_coupling_dominance.png'}")

    return rho_base_values, exponents_by_rho, stderrs_by_rho


# ============================================================================
# VARIANT B: Stochastic with Positive Mean Drift (Interpolation)
# ============================================================================

@dataclass
class VariantBAdversarialParams:
    """Parameters for Variant B (stochastic + mean drift)."""
    T_A: float = 0.1
    T_B: float = 0.1
    gamma_A: float = 0.5
    gamma_B: float = 0.5

    # Disturbance decomposition: rho_total = mu + sigma*|eps|_rms = mu + sigma
    # mu is the deterministic drift component
    # sigma is the stochastic noise std
    mu_base: float = 0.025       # Base deterministic drift
    sigma_base: float = 0.025    # Base noise std

    R: float = 1.0
    epsilon: float = 0.1
    R_max: float = 2.0

    num_steps: int = 20_000
    num_trials: int = 200
    burn_in: int = 5_000
    seed: int = 42

    @property
    def mu_A(self) -> float:
        """Deterministic drift on A: mu_base + gamma_B * T_B."""
        return self.mu_base + self.gamma_B * self.T_B

    @property
    def mu_B(self) -> float:
        """Deterministic drift on B: mu_base + gamma_A * T_A."""
        return self.mu_base + self.gamma_A * self.T_A

    @property
    def sigma_A(self) -> float:
        """Noise std on A (not coupled, just base noise)."""
        return self.sigma_base

    @property
    def sigma_B(self) -> float:
        """Noise std on B (not coupled, just base noise)."""
        return self.sigma_base

    def nonlinearity_kwargs(self) -> dict:
        return {"R": self.R, "epsilon": self.epsilon, "R_max": self.R_max}


def simulate_variant_b_adversarial(
    g: Callable,
    params: VariantBAdversarialParams,
) -> Tuple[np.ndarray, np.ndarray]:
    """Simulate two coupled agents with deterministic drift + stochastic noise.

    delta_A_{t+1} = delta_A_t - T_A * g(delta_A_t) + mu_A + sigma_A * eps
    delta_B_{t+1} = delta_B_t - T_B * g(delta_B_t) + mu_B + sigma_B * eps

    The adversarial coupling enters through the DETERMINISTIC drift component
    (mu), not the noise std. This matches TF-11's formulation more closely:
    the opponent's tempo increases the RATE of environmental change, not the
    stochastic amplitude.

    Returns:
        (deltas_A, deltas_B): each of shape (num_trials, num_steps)
    """
    rng = np.random.default_rng(params.seed)
    n = params.num_trials
    T = params.num_steps
    kwargs = params.nonlinearity_kwargs()

    mu_A = params.mu_A
    mu_B = params.mu_B
    sigma_A = params.sigma_A
    sigma_B = params.sigma_B

    noise_A = rng.normal(0.0, max(sigma_A, 1e-15), size=(n, T))
    noise_B = rng.normal(0.0, max(sigma_B, 1e-15), size=(n, T))

    deltas_A = np.zeros((n, T))
    deltas_B = np.zeros((n, T))

    for t in range(T - 1):
        corr_A = g(deltas_A[:, t], **kwargs)
        corr_B = g(deltas_B[:, t], **kwargs)
        deltas_A[:, t + 1] = deltas_A[:, t] - params.T_A * corr_A + mu_A + sigma_A * noise_A[:, t]
        deltas_B[:, t + 1] = deltas_B[:, t] - params.T_B * corr_B + mu_B + sigma_B * noise_B[:, t]

    return deltas_A, deltas_B


def run_variant_b_sweep():
    """Sweep mu/sigma ratio from pure noise to nearly deterministic.

    At each mu/sigma ratio, measure the adversarial exponent.
    The total "disturbance energy" is held roughly constant by keeping
    mu + sigma = constant, and varying their ratio.
    """
    print("\n" + "=" * 70)
    print("VARIANT B: Exponent vs mu/sigma Ratio (Drift-Noise Interpolation)")
    print("=" * 70)

    # Total disturbance budget (base component, before adversarial coupling)
    total_base = 0.05  # mu_base + sigma_base = constant

    # mu/sigma ratios to sweep (0 = pure noise, inf = pure drift)
    # We parameterize by the fraction of total that is deterministic: f = mu / total
    fractions = np.array([0.0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5,
                          0.6, 0.7, 0.8, 0.9, 0.95, 1.0])

    tempo_ratios = np.logspace(np.log10(0.5), np.log10(5.0), 20)
    T_B = 0.1
    gamma = 0.5

    exponents_by_frac = []
    stderrs_by_frac = []
    mu_sigma_ratios = []

    for f in fractions:
        mu_base = f * total_base
        sigma_base = (1.0 - f) * total_base

        if sigma_base > 0:
            mu_sigma_ratios.append(mu_base / sigma_base)
        else:
            mu_sigma_ratios.append(np.inf)

        g = CORRECTION_FUNCTIONS["linear"]
        medians = []

        for r in tempo_ratios:
            if sigma_base < 1e-12:
                # Pure deterministic: use Variant A code (no stochasticity)
                p_det = VariantAAdversarialParams(
                    T_A=r * T_B, T_B=T_B,
                    gamma_A=gamma, gamma_B=gamma,
                    rho_base=mu_base,
                    num_steps=20_000, burn_in=5_000,
                )
                dA, dB = simulate_variant_a_adversarial(g, p_det)
                ss_A = np.mean(np.abs(dA[p_det.burn_in:]))
                ss_B = np.mean(np.abs(dB[p_det.burn_in:]))
            else:
                p = VariantBAdversarialParams(
                    T_A=r * T_B, T_B=T_B,
                    gamma_A=gamma, gamma_B=gamma,
                    mu_base=mu_base,
                    sigma_base=sigma_base,
                    num_steps=20_000,
                    num_trials=200,
                    burn_in=5_000,
                    seed=42,
                )
                dA, dB = simulate_variant_b_adversarial(g, p)
                # Per-trial time-averaged absolute mismatch, then median across trials
                ss_A_trials = np.mean(np.abs(dA[:, p.burn_in:]), axis=1)
                ss_B_trials = np.mean(np.abs(dB[:, p.burn_in:]), axis=1)
                valid = ss_A_trials > 1e-12
                if np.any(valid):
                    trial_ratios = ss_B_trials[valid] / ss_A_trials[valid]
                    medians.append(np.median(trial_ratios))
                else:
                    medians.append(np.nan)
                continue

            # For deterministic case, just use the single ratio
            if ss_A > 1e-12:
                medians.append(ss_B / ss_A)
            else:
                medians.append(np.nan)

        medians = np.array(medians)
        b, se = _estimate_exponent(tempo_ratios, medians, 1.0)
        exponents_by_frac.append(b)
        stderrs_by_frac.append(se)

        label = f"f={f:.2f}"
        if sigma_base > 1e-12:
            label += f" (mu/sigma={mu_base/sigma_base:.2f})"
        else:
            label += " (pure deterministic)"
        print(f"  {label:<45} exponent = {b:.4f} +/- {se:.4f}")

    exponents_by_frac = np.array(exponents_by_frac)
    stderrs_by_frac = np.array(stderrs_by_frac)

    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.errorbar(fractions, exponents_by_frac, yerr=2 * stderrs_by_frac,
                fmt="-o", color=COLORS["linear"], markersize=7, capsize=4,
                linewidth=2)
    ax.axhline(y=2.0, color="k", linestyle="--", linewidth=2, alpha=0.7,
               label="Predicted: exponent = 2")
    ax.axhline(y=1.0, color="gray", linestyle=":", alpha=0.5,
               label="Linear advantage")
    ax.set_xlabel("Deterministic fraction $f = \\mu / (\\mu + \\sigma)$")
    ax.set_ylabel("Effective exponent $b$")
    ax.set_title(
        "Variant B: Tempo Advantage Exponent vs Drift-to-Noise Ratio\n"
        "(Linear correction, $\\mu_{base} + \\sigma_{base}$ held constant)"
    )
    ax.legend(fontsize=9)
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(0, max(np.nanmax(exponents_by_frac) + 0.5, 2.5))

    # Add secondary x-axis showing mu/sigma ratio
    ax2 = ax.twiny()
    ax2.set_xlim(ax.get_xlim())
    tick_fracs = [0.0, 0.2, 0.5, 0.8, 0.95, 1.0]
    tick_labels = ["0", "0.25", "1.0", "4.0", "19", "$\\infty$"]
    ax2.set_xticks(tick_fracs)
    ax2.set_xticklabels(tick_labels, fontsize=9)
    ax2.set_xlabel("$\\mu / \\sigma$ ratio", fontsize=10)

    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "variant_b_exponent_vs_drift_fraction.png")
    print(f"  Saved: {OUTPUT_DIR / 'variant_b_exponent_vs_drift_fraction.png'}")

    return fractions, exponents_by_frac, stderrs_by_frac


def run_variant_b_all_corrections():
    """Run Variant B at key mu/sigma ratios for all 5 correction functions.

    Tests three regimes: pure noise (f=0), balanced (f=0.5), pure drift (f=1).
    """
    print("\n" + "=" * 70)
    print("VARIANT B: All Correction Functions at Key Drift Fractions")
    print("=" * 70)

    total_base = 0.05
    test_fractions = [0.0, 0.5, 1.0]
    fraction_labels = ["Pure noise\n($f=0$)", "Balanced\n($f=0.5$)",
                       "Pure drift\n($f=1$)"]

    tempo_ratios = np.logspace(np.log10(0.5), np.log10(5.0), 20)
    T_B = 0.1
    gamma = 0.5

    results = {}  # results[(name, f)] = exponent

    for f in test_fractions:
        mu_base = f * total_base
        sigma_base = (1.0 - f) * total_base

        for name, g in CORRECTION_FUNCTIONS.items():
            medians = []
            for r in tempo_ratios:
                if sigma_base < 1e-12:
                    p_det = VariantAAdversarialParams(
                        T_A=r * T_B, T_B=T_B,
                        gamma_A=gamma, gamma_B=gamma,
                        rho_base=mu_base,
                        R=1.0, epsilon=0.1, R_max=2.0,
                        num_steps=20_000, burn_in=5_000,
                    )
                    dA, dB = simulate_variant_a_adversarial(g, p_det)
                    ss_A = np.mean(np.abs(dA[p_det.burn_in:]))
                    ss_B = np.mean(np.abs(dB[p_det.burn_in:]))
                    medians.append(ss_B / ss_A if ss_A > 1e-12 else np.nan)
                else:
                    p = VariantBAdversarialParams(
                        T_A=r * T_B, T_B=T_B,
                        gamma_A=gamma, gamma_B=gamma,
                        mu_base=mu_base, sigma_base=sigma_base,
                        num_steps=20_000, num_trials=200, burn_in=5_000,
                        seed=42,
                    )
                    dA, dB = simulate_variant_b_adversarial(g, p)
                    ss_A_trials = np.mean(np.abs(dA[:, p.burn_in:]), axis=1)
                    ss_B_trials = np.mean(np.abs(dB[:, p.burn_in:]), axis=1)
                    valid = ss_A_trials > 1e-12
                    if np.any(valid):
                        trial_ratios = ss_B_trials[valid] / ss_A_trials[valid]
                        medians.append(np.median(trial_ratios))
                    else:
                        medians.append(np.nan)

            medians = np.array(medians)
            b, se = _estimate_exponent(tempo_ratios, medians, 1.0)
            results[(name, f)] = (b, se)
            print(f"  f={f:.1f}  {name:<20} exponent = {b:.4f} +/- {se:.4f}")

    # Grouped bar chart
    fig, ax = plt.subplots(figsize=(12, 6))
    n_funcs = len(CORRECTION_FUNCTIONS)
    n_fracs = len(test_fractions)
    bar_width = 0.25
    x_base = np.arange(n_funcs)

    for fi, f in enumerate(test_fractions):
        bs = [results[(name, f)][0] for name in CORRECTION_FUNCTIONS]
        ses = [results[(name, f)][1] for name in CORRECTION_FUNCTIONS]
        colors_list = [COLORS[n] for n in CORRECTION_FUNCTIONS]
        alphas = [0.4, 0.7, 1.0][fi]

        offset = (fi - 1) * bar_width
        bars = ax.bar(x_base + offset, bs, bar_width,
                      yerr=[2 * se for se in ses], capsize=3,
                      color=colors_list, alpha=alphas, edgecolor="black",
                      linewidth=0.5, label=fraction_labels[fi])

    ax.axhline(y=2.0, color="k", linestyle="--", linewidth=2, alpha=0.7,
               label="Predicted exponent = 2")
    ax.axhline(y=1.0, color="gray", linestyle=":", alpha=0.5,
               label="Linear (exponent = 1)")
    ax.set_xticks(x_base)
    ax.set_xticklabels([n.capitalize() for n in CORRECTION_FUNCTIONS], fontsize=10)
    ax.set_ylabel("Effective exponent $b$")
    ax.set_title("Variant B: Exponent by Correction Function at Key Drift Fractions")
    ax.legend(fontsize=8, ncol=2)
    ax.set_ylim(0, max(max(r[0] for r in results.values()) + 0.5, 2.5))
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "variant_b_all_corrections.png")
    print(f"  Saved: {OUTPUT_DIR / 'variant_b_all_corrections.png'}")

    return results


# ============================================================================
# Shared utility: exponent estimation
# ============================================================================

def _estimate_exponent(
    tempo_ratios: np.ndarray,
    mismatch_ratios: np.ndarray,
    gamma_ratio: float = 1.0,
) -> Tuple[float, float]:
    """Estimate the effective exponent b in mismatch_ratio ~ gamma_ratio * (T_A/T_B)^b.

    Uses least squares on log-transformed data.

    Returns:
        (b, b_stderr)
    """
    valid = np.isfinite(mismatch_ratios) & (mismatch_ratios > 0) & (tempo_ratios > 0)
    if np.sum(valid) < 3:
        return np.nan, np.nan

    x = np.log(tempo_ratios[valid])
    y = np.log(mismatch_ratios[valid] / gamma_ratio)

    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    ss_xx = np.sum((x - x_mean) ** 2)
    ss_xy = np.sum((x - x_mean) * (y - y_mean))

    if ss_xx < 1e-12:
        return np.nan, np.nan

    b = ss_xy / ss_xx
    a = y_mean - b * x_mean

    y_pred = a + b * x
    residuals = y - y_pred
    s2 = np.sum(residuals ** 2) / (n - 2) if n > 2 else np.nan
    b_stderr = np.sqrt(s2 / ss_xx) if np.isfinite(s2) else np.nan

    return b, b_stderr


# ============================================================================
# Main
# ============================================================================

def main():
    print("=" * 70)
    print("VARIANT A/B: Drift Disturbance Models")
    print("Testing whether TF-11's squared advantage emerges with")
    print("deterministic rho (matching the ODE) vs stochastic rho")
    print("=" * 70)

    # --- Variant A ---
    single_results = run_variant_a_single_agent()
    adv_results, adv_exponents = run_variant_a_adversarial()
    coupling_rho, coupling_exp, coupling_se = run_variant_a_coupling_dominance()

    # --- Variant B ---
    b_fracs, b_exps, b_ses = run_variant_b_sweep()
    b_all_results = run_variant_b_all_corrections()

    # --- Final summary ---
    print("\n" + "=" * 70)
    print("FINAL SUMMARY")
    print("=" * 70)

    print("\nVariant A (Deterministic Drift) - Adversarial Exponents:")
    print(f"  {'Function':<20} {'Exponent':>10}")
    print(f"  {'-'*30}")
    for name, (b, se) in adv_exponents.items():
        print(f"  {name:<20} {b:>10.4f}")

    print(f"\nVariant A - Coupling Dominance Sweep (Linear):")
    print(f"  Most coupling-dominated (rho_base -> 0): "
          f"exponent = {coupling_exp[0]:.4f}")
    print(f"  Most base-dominated: "
          f"exponent = {coupling_exp[-1]:.4f}")

    print(f"\nVariant B (Drift-Noise Interpolation) - Linear Correction:")
    print(f"  {'Drift fraction f':>20} {'Exponent':>10}")
    print(f"  {'-'*30}")
    for f, b in zip(b_fracs, b_exps):
        print(f"  {f:>20.2f} {b:>10.4f}")

    print(f"\nVariant B - All Corrections at Key Drift Fractions:")
    for f in [0.0, 0.5, 1.0]:
        print(f"  f = {f:.1f}:")
        for name in CORRECTION_FUNCTIONS:
            b, se = b_all_results[(name, f)]
            print(f"    {name:<20} {b:.4f} +/- {se:.4f}")

    # Key diagnostic: does exponent reach 2.0?
    linear_det_exp = adv_exponents["linear"][0]
    linear_det_coupling = coupling_exp[0]
    print(f"\n*** KEY FINDING ***")
    print(f"  Linear correction, deterministic drift, standard params: "
          f"exponent = {linear_det_exp:.4f}")
    print(f"  Linear correction, deterministic drift, extreme coupling dominance: "
          f"exponent = {linear_det_coupling:.4f}")
    if abs(linear_det_coupling - 2.0) < 0.1:
        print(f"  --> YES: squared advantage (exponent ~ 2) DOES appear "
              f"under deterministic drift with coupling dominance!")
    elif linear_det_coupling > 1.5:
        print(f"  --> PARTIAL: exponent is superlinear ({linear_det_coupling:.3f}) "
              f"but does not fully reach 2.0")
    else:
        print(f"  --> NO: exponent remains near {linear_det_coupling:.3f} "
              f"even with deterministic drift + coupling dominance")

    print(f"\nDone. All figures saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
