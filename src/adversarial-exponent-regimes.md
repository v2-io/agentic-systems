---
slug: adversarial-exponent-regimes
type: observation
status: empirical
depends:
  - adversarial-destabilization
  - adaptive-tempo
  - persistence-condition
---

# Observation: Adversarial Exponent Regimes

The adversarial tempo advantage exponent — the power $b$ in $\Vert\delta_B\Vert / \Vert\delta_A\Vert \sim (\mathcal T_A / \mathcal T_B)^b$ — is not a single number. It depends on two structural features of the disturbance: whether the adversarial coupling enters as deterministic drift or stochastic noise, and whether the coupling dominates the base disturbance rate. Three regimes emerge from simulation.

## Formal Expression

*[Observation (adversarial-exponent-regimes, from track-b simulations)]*

**Regime 1: Deterministic drift, coupling-dominant.** When adversarial coupling enters as a persistent directional disturbance ($\rho_B = \rho_{\text{base}} + \gamma \cdot \mathcal T_A$, deterministic) and coupling dominates ($\gamma \cdot \mathcal T_B \gg \rho_{\text{base}}$):

$$b \to 2.0 \qquad \text{(confirmed at 1.999)}$$

This is the exact prediction of the mismatch ODE steady state $\Vert\delta\Vert_{ss} = \rho / \mathcal{T}$.

**Regime 2: Stochastic noise, coupling-dominant.** When adversarial coupling enters through the noise scale of zero-mean perturbations ($\sigma_B = \sigma_{\text{base}} + \gamma \cdot \mathcal T_A$) and coupling dominates:

$$b \to 1.5$$

Root cause: the AR(1) steady-state RMS scales as $\rho / \sqrt{\mathcal{T}}$ (not $\rho / \mathcal{T}$), because variance scales as $\rho^2 / \mathcal{T}$ and the expected absolute deviation scales as the square root of variance.

**Regime 3: Non-coupling-dominant.** When base disturbance is comparable to or exceeds the adversarial coupling ($\rho_{\text{base}} \gtrsim \gamma \cdot \mathcal T_B$):

$$b \to 1.0 \text{ (deterministic)} \quad \text{or} \quad b \to 0.5 \text{ (stochastic)}$$

The exponent degrades smoothly as the base-to-coupling ratio increases.

| $\rho_{\text{base}} / (\gamma \cdot \mathcal T_B)$ | Exponent (deterministic) | Exponent (stochastic) |
|:---:|:---:|:---:|
| 0.002 | 1.999 | 1.481 |
| 0.20 | 1.877 | 1.101 |
| 2.0 | 1.445 | 0.791 |
| 6.3 | 1.213 | 0.577 |

## Epistemic Status

*Empirical.* Max attainable: exact conditional on disturbance model. The three regimes are established by simulation (6 variants, multiple parameter sweeps) and confirmed by analytical derivation of the AR(1) steady-state scaling. The deterministic exponent ($b = 2$) is derivable from the mismatch ODE; the stochastic exponent ($b = 1.5$) is derivable from the AR(1) stationary variance. What is empirical is the claim that real adversarial interactions fall into these regimes — whether a given adversary's tempo increases systematic drift vs. unpredictability is a domain question.

## Discussion

**The mismatch ODE conflates two quantities.** The equation $d\Vert\delta\Vert/dt = -\mathcal{T} \cdot \Vert\delta\Vert + \rho$ is ambiguous about whether $\rho$ represents deterministic drift (persistent directional change) or stochastic noise scale (unpredictable fluctuations). These give different steady-state scaling: $\rho / \mathcal{T}$ vs. $\rho / \sqrt{\mathcal{T}}$. For the mismatch dynamics ( #mismatch-dynamics), this distinction needs explicit treatment.

**Why the squared law held for the coupling-dominance sweep.** In Variant A, the coupling enters as deterministic drift: $\rho_B = \rho_{\text{base}} + \gamma \cdot \mathcal T_A$, and the steady state is $\Vert\delta_B\Vert = \rho_B / \mathcal T_B$. The ratio $\Vert\delta_B\Vert / \Vert\delta_A\Vert$ in the coupling-dominant limit gives $(\mathcal T_A / \mathcal T_B)^2$ directly.

**Nonlinear correction creates thresholds, not lower exponents.** For saturating, sigmoid, and breakdown correction functions under deterministic drift, the issue is not a reduced exponent but a catastrophic divergence when $\rho$ exceeds the correction capacity ($\rho \gt \mathcal{T} \cdot R$). This is exactly the persistence threshold failure ( #persistence-condition), observed directly in simulation.

**Domain interpretation.** Whether a given opponent's tempo increase causes deterministic drift or stochastic noise depends on the domain:
- Military: an opponent who maneuvers faster creates systematic positional change (drift, $b \approx 2$)
- Market: a competitor who acts unpredictably creates noise in signals ($b \approx 1.5$)
- Software: a fast-changing API creates systematic drift in the codebase state (drift)
- Adversarial ML: an opponent who varies attack vectors increases observation noise ($b \approx 1.5$)

## Working Notes
- The interpolation between drift and noise regimes (Variant B) shows smooth transition, not a sharp boundary. At mixed drift-noise coupling, the exponent lies between the two asymptotes. The drift fraction $f = \mu / (\mu + \sigma)$ continuously parameterizes the transition.
- The exponent of 1.05 from the original sim2 was not a falsification of Corollary 11.2 — it reflected a stochastic model (noise-variance coupling) tested in a non-coupling-dominant regime. The original simulation was testing the wrong regime for the ODE's prediction.
- Simulation code: `scratch/track-b-nonlinear-sims/variants/variant_ab_drift.py`, `variant_cd_regimes.py`. Results: `variant_ab_results.md`, `variant_cd_results.md`.
