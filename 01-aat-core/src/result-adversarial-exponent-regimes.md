---
slug: result-adversarial-exponent-regimes
type: result
status: conditional
depends:
  - der-adversarial-destabilization
  - result-adversarial-tempo-advantage
  - def-adaptive-tempo
  - result-persistence-condition
  - deriv-sector-condition
stage: draft
---

# Result: Adversarial Exponent Regimes

The adversarial tempo advantage exponent — the power $b$ in $\lVert\delta_B\rVert / \lVert\delta_A\rVert \sim (\mathcal T_A / \mathcal T_B)^b$ — is not a single number. It depends on two structural features of the disturbance: whether the adversarial coupling enters as deterministic drift (Model D) or stochastic noise (Model S), and whether the coupling dominates the base disturbance rate. Three regimes, with the coupling-dominant exponents now derived analytically from the respective disturbance models.

## Formal Expression

*[Derived (adversarial-exponent-regimes, from Model D/S steady states + coupling model; validated by simulation)]*

**Regime 1: Model D (deterministic drift), coupling-dominant.** When adversarial coupling enters as a persistent directional disturbance ($\rho_B = \rho_{\text{base}} + \gamma \cdot \mathcal T_A$, GA-2) and coupling dominates ($\gamma \cdot \mathcal T_B \gg \rho_{\text{base}}$):

$$b = 2 \qquad \text{(simulation: 1.999)}$$

Derived from the Model D steady state $\lVert\delta\rVert_{ss} = \rho/\mathcal{T}$ (Prop A.1). See #result-adversarial-tempo-advantage.

**Regime 2: Model S (stochastic noise), coupling-dominant.** When adversarial coupling enters through the noise scale of zero-mean perturbations ($\sigma_B = \sigma_{\text{base}} + \gamma \cdot \mathcal T_A$, GA-2S) and coupling dominates:

$$b = \frac{3}{2} \qquad \text{(simulation: 1.481)}$$

Derived from the Model S steady state $\lVert\delta\rVert_{\text{rms}} = \sigma_w/\sqrt{2\mathcal{T}}$ (Prop A.1S). The $1/\sqrt{\mathcal{T}}$ scaling (vs. $1/\mathcal{T}$ for Model D) removes one half-power from the denominator, reducing the exponent from 2 to 3/2. See #result-adversarial-tempo-advantage.

**Regime 3: Non-coupling-dominant.** When base disturbance is comparable to or exceeds the adversarial coupling ($\rho_{\text{base}} \gtrsim \gamma \cdot \mathcal T_B$):

$$b \to 1.0 \text{ (Model D)} \quad \text{or} \quad b \to 0.5 \text{ (Model S)}$$

The exponent degrades smoothly as the base-to-coupling ratio increases. The asymptotic limits are derived (they reflect the $1/\mathcal{T}$ or $1/\sqrt{\mathcal{T}}$ scaling without the coupling numerator); the smooth interpolation is empirical.

| $\rho_{\text{base}} / (\gamma \cdot \mathcal T_B)$ | Exponent (deterministic) | Exponent (stochastic) |
|:---:|:---:|:---:|
| 0.002 | 1.999 | 1.481 |
| 0.20 | 1.877 | 1.101 |
| 2.0 | 1.445 | 0.791 |
| 6.3 | 1.213 | 0.577 |

## Epistemic Status

*Exact conditional on disturbance model.* The coupling-dominant exponents are derived, not empirical: $b = 2$ follows from the Model D steady state (Prop A.1) and the coupling model; $b = 3/2$ follows from the Model S steady state (Prop A.1S) and the coupling model. The simulation results (6 variants, multiple parameter sweeps) now serve as validation of the derived exponents, not as their epistemic foundation. The non-coupling-dominant limits ($b \to 1$, $b \to 1/2$) are derived asymptotically; the smooth interpolation between coupling-dominant and non-coupling-dominant is empirical. What remains empirical is whether a given real adversarial interaction is better modeled as Model D or Model S — that is a domain question, not a theory question.

## Discussion

**The disturbance model determines the exponent.** The mismatch dynamics ( #hyp-mismatch-dynamics) now distinguish two disturbance models: Model D (bounded deterministic, GA-2) with steady-state $\rho/\mathcal{T}$, and Model S (stochastic zero-mean, GA-2S) with steady-state $\sigma_w/\sqrt{2\mathcal{T}}$. The different steady-state scaling is the root cause of the different exponents. This resolves the ambiguity that previously existed in the single-$\rho$ formulation.

**Why the squared law held for the coupling-dominance sweep.** In Variant A, the coupling enters as deterministic drift: $\rho_B = \rho_{\text{base}} + \gamma \cdot \mathcal T_A$, and the steady state is $\Vert\delta_B\Vert = \rho_B / \mathcal T_B$. The ratio $\Vert\delta_B\Vert / \Vert\delta_A\Vert$ in the coupling-dominant limit gives $(\mathcal T_A / \mathcal T_B)^2$ directly.

**Nonlinear correction creates thresholds, not lower exponents.** For saturating, sigmoid, and breakdown correction functions under deterministic drift, the issue is not a reduced exponent but a catastrophic divergence when $\rho$ exceeds the correction capacity ($\rho \gt \mathcal{T} \cdot R$). This is exactly the persistence threshold failure ( #result-persistence-condition), observed directly in simulation.

**Domain interpretation.** Whether a given opponent's tempo increase causes deterministic drift or stochastic noise depends on the domain:
- Military: an opponent who maneuvers faster creates systematic positional change (drift, $b \approx 2$)
- Market: a competitor who acts unpredictably creates noise in signals ($b \approx 1.5$)
- Software: a fast-changing API creates systematic drift in the codebase state (drift)
- Adversarial ML: an opponent who varies attack vectors increases observation noise ($b \approx 1.5$)

## Working Notes
- The interpolation between drift and noise regimes (Variant B) shows smooth transition, not a sharp boundary. At mixed drift-noise coupling, the exponent lies between the two asymptotes. The drift fraction $f = \mu / (\mu + \sigma)$ continuously parameterizes the transition.
- The exponent of 1.05 from the original sim2 was not a falsification of Corollary 11.2 — it reflected a stochastic model (noise-variance coupling) tested in a non-coupling-dominant regime. The original simulation was testing the wrong regime for the ODE's prediction.
- Simulation code: `../../spikes/track-b-nonlinear-sims/variants/variant_ab_drift.py`, `variant_cd_regimes.py`. Results: `variant_ab_results.md`, `variant_cd_results.md`.
