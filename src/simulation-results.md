---
slug: simulation-results
type: detail
status: empirical
depends:
  - mismatch-dynamics
  - update-gain
  - persistence-condition
  - sector-condition-stability
  - adversarial-destabilization
---

# Detail: Simulation Results

Six simulation variants validated, refined, and extended the analytical predictions from Section I, forcing regime splits and discovering scaling laws that the analytical derivations left ambiguous.

## Overview

The track-b simulation program tested Section I's analytical predictions about mismatch dynamics, adversarial coupling, observation noise, correction function robustness, and anisotropic persistence. The simulations modeled discrete-time mismatch dynamics as AR(1) processes with five correction functions (linear, saturating, threshold/dead-zone, sigmoid, structural breakdown), sweeping parameter spaces across gain, disturbance rate, coupling strength, observation noise, and dimensional structure.

The simulations were theory-shaping, not merely confirmatory. In particular:

- The adversarial tempo exponent turned out to be regime-dependent (deterministic drift vs. stochastic noise, coupling-dominant vs. non-coupling-dominant), forcing a regime split that the mismatch ODE left ambiguous.
- Observation noise was found to gate the adversarial advantage, partially recoverable by optimal gain -- a finding that had no analytical treatment before the simulations.
- The scalar persistence condition was shown to overestimate adaptive capacity by 72% in anisotropic systems, motivating the per-dimension persistence condition.

## Variant Summary

| Variant | Tested | Key Finding | Theory Impact | Promoted Segment |
|---------|--------|-------------|---------------|------------------|
| A | Deterministic drift coupling; coupling-dominance sweep | Exponent $b \to 2.0$ in coupling-dominant limit (confirmed at 1.999) | Corollary 11.2 is exact under deterministic drift dominance | [#adversarial-exponent-regimes](adversarial-exponent-regimes.md) |
| B | Drift-noise interpolation across correction functions | Smooth transition between drift ($b = 2.0$) and noise ($b = 1.5$) regimes; coupling dominance is the key qualifier, not drift vs. noise per se | Confirmed that the coupling-dominant condition is quantitatively load-bearing | [#adversarial-exponent-regimes](adversarial-exponent-regimes.md) |
| C | Exponent vs. gain ($\eta$) in stochastic model | Exponent drops toward 0.5 as $\eta \to 0$ (away from coupling dominance at fixed $q_\text{base}$); discrete AR(1) exponent never exceeds 1.5 | Stochastic noise coupling has asymptotic exponent 1.5, not 2.0 -- a fundamental model distinction | [#adversarial-exponent-regimes](adversarial-exponent-regimes.md) |
| D | Exponent vs. base noise ($q_\text{base}$) at fixed $\eta$ | Continuous ODE exponent $\to$ 2.0, discrete AR(1) exponent $\to$ 1.5, as $q_\text{base} \to 0$ | Definitively separated the two asymptotes; simulations match discrete AR(1) prediction exactly | [#adversarial-exponent-regimes](adversarial-exponent-regimes.md) |
| E | Observation noise; optimal gain validation | Observation noise collapses adversarial exponent from $\sim 1.0$ to $\sim 0.2$; Riccati-optimal gain restores it to $\sim 0.4$; 52% mismatch reduction at moderate noise | Observation quality gates tempo advantage; optimal gain ( #update-gain) empirically validated | [#observation-gates-advantage](observation-gates-advantage.md) |
| F | Multi-dimensional anisotropic correction; targeted adversarial attack | Per-dimension theory exact to 4 significant figures; scalar tempo overestimates by 72%; targeted attack amplifies advantage by 17% | Scalar persistence condition is necessary but not sufficient; per-dimension condition required | [#per-dimension-persistence](per-dimension-persistence.md) |
| Hafez bridge | Bi-predictability $P$ vs. ACT mismatch in adversarial and non-adversarial settings | $P$ measures coupling architecture (scale-invariant); mismatch measures coupling performance; $P$ is blind to adversarial dynamics | $P$ and ACT mismatch are complementary diagnostics; $H_b$ (agent opacity) has no direct ACT analog -- potential gap for multi-agent work | -- |

## Methodology

**Discrete mismatch dynamics.** The environment follows a random walk $x_{t+1} = x_t + w_t$ with $w_t \sim N(0, q^2)$. The agent corrects via $\hat{x}_{t+1} = \hat{x}_t + \eta \cdot g(\delta_t)$, yielding the AR(1) mismatch process $\delta_{t+1} = (1 - \eta) \cdot \delta_t + w_t$ for linear $g$. This is the discrete-time analog of the mismatch ODE $d\|\delta\|/dt = -\mathcal{T} \cdot \|\delta\| + \rho$ from #mismatch-dynamics.

**Parameter sweeps.** Each variant swept its key parameter(s) across 7--20 values. Monte Carlo: 200 independent trials per parameter point, 10,000--20,000 timesteps per trial, with 2,000--5,000 step burn-in for steady-state convergence. Fixed random seeds for reproducibility.

**Exponent fitting.** Adversarial exponents were estimated by fitting $\log(\|\delta_B\| / \|\delta_A\|) = a + b \cdot \log(\mathcal{T}_A / \mathcal{T}_B)$ via weighted least squares, with weights inversely proportional to variance of each point's log-estimate. 95% confidence intervals via bootstrap (1,000 samples).

**Correction functions.** Five functions $g: \mathbb{R} \to \mathbb{R}$ were tested, all satisfying $g(0) = 0$ and $g'(0) = 1$: linear ($g(\delta) = \delta$), saturating ($g(\delta) = \delta / (1 + |\delta|/R)$), threshold ($g(\delta) = \delta \cdot \mathbf{1}[|\delta| > \epsilon]$), sigmoid ($g(\delta) = R \cdot \tanh(\delta/R)$), and structural breakdown ($g(\delta) = \delta \cdot \mathbf{1}[|\delta| < R_\text{max}]$).

**Simulation code.** All code is in `scratch/track-b-nonlinear-sims/`. Initial simulations: `sim1_nonlinear_mismatch.py` (single-agent), `sim2_adversarial_coupling.py` (two-agent). Variant extensions: `variants/variant_ab_drift.py`, `variants/variant_cd_regimes.py`, `variants/variant_ef_extensions.py`, `variants/variant_hafez_bridge.py`. Detailed result write-ups: `variants/variant_ab_results.md`, `variants/variant_cd_results.md`, `variants/variant_ef_results.md`, `variants/variant_hafez_results.md`.

## Key Findings

### The adversarial exponent is regime-dependent

The mismatch ODE's $\rho$ parameter conflates two quantities: deterministic drift (persistent directional change) and stochastic noise scale (unpredictable fluctuations). These yield different steady-state scaling:

- **Deterministic drift, coupling-dominant:** $\|\delta\|_{ss} = \rho / \mathcal{T}$. Adversarial exponent $b \to 2.0$.
- **Stochastic noise, coupling-dominant:** $\|\delta\|_{ss} = \rho / \sqrt{\mathcal{T}}$ (from AR(1) stationary variance). Adversarial exponent $b \to 1.5$.
- **Non-coupling-dominant:** Exponent degrades smoothly toward 1.0 (deterministic) or 0.5 (stochastic) as base disturbance grows relative to adversarial coupling.

The original sim2 result ($b \approx 1.05$) was not a falsification of Corollary 11.2 but a measurement in the wrong regime -- stochastic noise coupling at moderate coupling dominance. Variants A--D systematically mapped the full regime space and identified the analytical root causes. See #adversarial-exponent-regimes for the full treatment.

### Observation noise gates adversarial advantage

Adding observation noise $\sigma_\text{obs}$ to the mismatch signal collapsed the adversarial exponent from $\sim 1.0$ to $\sim 0.2$ at $\sigma_\text{obs} = 10 \times q_\text{env}$ (fixed gain). The Riccati-optimal gain ( #update-gain) partially restored the advantage to $\sim 0.4$, more than doubling it but not recovering the noise-free level. The optimal gain helps most in the moderate-noise regime, where it achieved a 52% mismatch reduction over fixed gain. See #observation-gates-advantage.

### Per-dimension persistence is exact; scalar overestimates

In a 3-dimensional system with 5:1 gain variation across dimensions, the per-dimension AR(1) steady-state prediction matched simulation to 4 significant figures. The scalar persistence condition overestimated aggregate mismatch by 72%, because it averages across dimensions while the weak dimension dominates the $L_2$ norm. Isotropic gain allocation reduced overall mismatch by 13%; targeted adversarial attack on the weak dimension amplified the mismatch ratio by 17%. See #per-dimension-persistence.

### Nonlinear correction creates thresholds, not lower exponents

Under deterministic drift, saturating, sigmoid, and breakdown correction functions did not simply reduce the adversarial exponent. Instead, they produced catastrophic divergence when disturbance exceeded the correction capacity ($\rho > \mathcal{T} \cdot R$). This is the persistence threshold failure from #persistence-condition, observed directly in simulation. The measured "exponents" above 3.0 for these functions were divergence artifacts, not meaningful scaling laws.

### Hafez bridge: architecture vs. performance

Bi-predictability $P$ (Hafez et al.) measures the informational architecture of agent-environment coupling; ACT mismatch measures the operational performance. In adversarial settings, $P$ remained nearly constant ($\sim 0.268$) across a 10:1 range of opponent tempo, while the mismatch ratio varied from 0.54 to 5.95. $P$ is scale-invariant after z-score normalization, making it insensitive to adversarial dynamics. The two metrics are complementary: $P$ diagnoses whether the coupling structure is sound; mismatch predicts how well it performs.

## Epistemic Status

*Empirical.* Simulation results are reproducible (code in `scratch/track-b-nonlinear-sims/`, fixed seeds, all results documented in variant write-ups). The key results -- regime-dependent exponents, observation noise gating, per-dimension exactness -- have been promoted to first-class segments ( #adversarial-exponent-regimes, #observation-gates-advantage, #per-dimension-persistence) with their own epistemic assessments. This appendix serves as reference for the simulation program as a whole.

## Discussion

**Internal validation, not external.** The simulations operate in the model's own terms: AR(1) processes with parameterized correction functions, Gaussian noise, and discrete-time dynamics. They validate the mathematical predictions within the model -- confirming that the analytical steady-state formulas, the exponent regimes, and the per-dimension theory are correct as statements about these stochastic processes. The gap between "the math predicts X within its own model" and "real agents exhibit X" remains an empirical question for each domain.

**What the simulations did not test.** The simulations did not test whether the AR(1) mismatch dynamics are a good model for any particular real-world adaptive system. They also did not test cross-dimensional coupling (off-diagonal correction), non-Gaussian disturbances, non-stationary parameters, or multi-agent composition dynamics. The interaction between observation noise and the deterministic-drift exponent regime ($b = 2.0$) was not tested -- Variant E used stochastic coupling only.

**Theory-shaping role.** The most important contribution of the simulations was not confirming predictions but forcing the theory to be more precise. The regime split in the adversarial exponent, the observation-noise gating mechanism, and the per-dimension bottleneck effect were all findings that the analytical derivations left ambiguous or unaddressed. The simulations narrowed the theory's claims from "the exponent is 2" to "the exponent is 2 under deterministic drift in the coupling-dominant regime, and 1.5 under stochastic noise in the coupling-dominant regime," which is a substantively different and more useful statement.
