---
slug: mismatch-dynamics
type: hypothesis
status: heuristic
depends:
  - adaptive-tempo
  - mismatch-signal
stage: deps-verified
---

# Hypothesis: Mismatch Dynamics

The evolution of model-reality mismatch over time is governed by the balance between the agent's corrective capacity (tempo) and the rate of environmental change (disturbance). The linear ODE is a first-order approximation; the general nonlinear case is handled by the sector-condition framework ( #sector-condition-stability).

## Formal Expression

*[Hypothesis (mismatch-dynamics)]*

$$\frac{d\Vert\delta\Vert}{dt} = -\mathcal{T} \cdot \Vert\delta\Vert + \rho(t)$$

where:
- $\mathcal{T} \cdot \Vert\delta\Vert$ is the rate at which the agent corrects mismatch (proportional to both tempo and current mismatch)
- $\rho(t)$ is the **environment change rate** — the rate at which new mismatch is introduced by changes in $\Omega$

**Steady state, Model D (deterministic bounded disturbance, $\lVert w(t)\rVert \leq \rho$):**

Setting $d\lVert\delta\rVert/dt = 0$:

*[Derived (from linear hypothesis, deterministic)]*

$$\lVert\delta\rVert_{ss} = \frac{\rho}{\mathcal{T}}$$

Steady-state mismatch is the ratio of how fast the environment changes to how fast the agent adapts.

**Steady state, Model S (stochastic zero-mean disturbance, $d\delta = -\mathcal{T}\delta\,dt + \sigma_w\,dW_t$):**

*[Derived (from Itô-Lyapunov analysis — see Prop A.1S in #sector-condition-derivation)]*

$$\lVert\delta\rVert_{\text{rms}} = \frac{\sigma_w}{\sqrt{2\mathcal{T}}}$$

(scalar case, $n = 1$; general: $\sigma_w\sqrt{n/(2\mathcal{T})}$). Steady-state mismatch scales as the square root of the disturbance-to-correction ratio, not the ratio itself. The $1/\sqrt{\mathcal{T}}$ scaling (vs. $1/\mathcal{T}$ for Model D) means correction is less effective against noise than against drift.

**Transient solution (Model D):**

$$\lVert\delta(t)\rVert = \lVert\delta_0\rVert e^{-\mathcal{T} t} + \frac{\rho}{\mathcal{T}}(1 - e^{-\mathcal{T} t})$$

Mismatch decays exponentially from initial conditions toward the steady state.

## Epistemic Status

*Heuristic.* This is explicitly a first-order linear approximation. The qualitative behavior (bounded mismatch, steady-state ratio, exponential convergence) is robust across correction function forms. The quantitative predictions (exact steady-state value, convergence rate, the squared adversarial scaling law) are specific to the linear case. The general nonlinear treatment ( #sector-condition-stability) replaces the linear correction term with a sector-bounded correction function and proves persistence without committing to a specific functional form.

**Bridging assumption (discrete to continuous).** This ODE is a fluid-limit approximation of the discrete event-driven dynamics ( #event-driven-dynamics). The fluid limit is formally justified by [#discrete-sector-condition](discrete-sector-condition.md): for Model D (deterministic), the discrete and continuous steady states are identical (zero gap); for Model S (stochastic), the variance gap is $O(\eta^\ast c_{\max})$, quantitatively small whenever $\eta^\ast c_{\max} \ll 1$. The approximation is least accurate during initial transients when $\eta^\ast$ is large, but this phase is short-lived and the transient error is bounded by $O(\eta^\ast c_{\max} / \nu^{1/2})$ under Lipschitz regularity.

## Discussion

**Speed-quality substitutability.** From $\mathcal{T} = \nu \cdot \eta^\ast$ (single-channel case): doubling event rate $\nu$ has the same effect on $\Vert\delta\Vert_{ss}$ as doubling update quality $\eta^\ast$. They are multiplicative when both improve: 50% improvement in each yields $1.5 \times 1.5 = 2.25\times$, not $3\times$. This is the formal analog of Boyd's insight that Orient quality often matters more than raw OODA speed — the same structural observation (quality and speed are substitutable, quality often dominates) appears in the model.

**The persistence threshold.** From the steady-state: $\Vert\delta\Vert_{ss} \lt \Vert\delta_{\text{critical}}\Vert$ iff $\mathcal{T} \gt \rho/\Vert\delta_{\text{critical}}\Vert$ ( #persistence-condition). Below this threshold, the model cannot support effective action. The same structural pattern — correction capacity falling below disturbance rate — appears across domains: extinction (environment changes faster than organism adapts), organizational failure (market moves faster than company learns), control instability (disturbances exceed correction capacity), cognitive overload (information arrives faster than processing). The persistence condition captures the common structure; whether it captures the dominant mechanism in each domain is an empirical question.

**Nonlinear reality.** The true correction dynamics are almost certainly nonlinear:
- *Saturation at large $\Vert\delta\Vert$*: correction mechanism overwhelmed, so correction is slower than linear for large errors. Makes the persistence threshold harder to satisfy.
- *Threshold effects*: small mismatches go uncorrected ($F \approx 0$ for $\Vert\delta\Vert \lt \varepsilon$), creating a dead zone.
- *Structural breakdown*: beyond some critical $\Vert\delta\Vert$, correction drops to zero because the model class is no longer appropriate ( #structural-adaptation-necessity).

These nonlinearities are exactly what the sector-condition framework ( #sector-condition-stability) handles.

**Adversarial coupling.** When two agents are coupled ($A$'s actions increase $B$'s disturbance): $\rho_B = \rho_{B,\text{base}} + \gamma_A \cdot \mathcal T_A$. The steady-state mismatch ratio scales superlinearly with the tempo ratio, but the exponent depends on the disturbance model. Under Model D (deterministic drift, coupling-dominant): $(\mathcal T_A/\mathcal T_B)^2$ — the squared law, derived from the $1/\mathcal{T}$ steady-state scaling. Under Model S (stochastic noise, coupling-dominant): $(\mathcal T_A/\mathcal T_B)^{3/2}$ — derived from the $1/\sqrt{\mathcal{T}}$ steady-state scaling. See #adversarial-tempo-advantage.

**(Descended from TF-11.)**
