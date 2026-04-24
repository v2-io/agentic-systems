---
slug: adaptive-tempo
type: definition
status: exact
depends:
  - update-gain
  - event-driven-dynamics
stage: claims-verified
---

# Definition: Adaptive Tempo

The effective rate at which an agent acquires useful information from its environment — the product of observation frequency and update quality across all channels.

## Formal Expression

*[Definition (adaptive-tempo)]*

$$\mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)*}$$

where:
- $k$ indexes the agent's distinct observation channels
- $\nu^{(k)}$ is the event rate on channel $k$
- $\eta^{(k)\ast}$ is the optimal update gain on channel $k$ ( #update-gain)

Single-channel special case: $\mathcal{T} = \nu \cdot \eta^\ast$.

## Epistemic Status

This is a *definition*. It names the quantity that characterizes an agent's total corrective capacity, combining loop speed ($\nu$) and epistemic quality ($\eta^\ast$). The definition itself is not a truth-claim; the substantive claims are in the results that use it ( #persistence-condition, #adversarial-tempo-advantage).

## Discussion

**Speed-quality substitutability.** An agent can achieve the same tempo via a fast noisy loop (high $\nu$, low $\eta^\ast$) or a slower calibrated one (low $\nu$, high $\eta^\ast$). The product structure means improvements to *both* factors compound multiplicatively.

**Observation noise gating.** Because $\eta^\ast = U_M / (U_M + U_o)$, high observation noise ($U_o$) depresses gain and collapses tempo regardless of loop speed. You cannot outrun a bad observation channel by iterating faster. This grounds Boyd's emphasis on Orient quality over raw OODA speed.

**Centrality.** Tempo is AAD's core capacity metric. It appears on the left side of the persistence condition ( #persistence-condition), determines adversarial advantage ( #adversarial-tempo-advantage), and connects to code quality as observation infrastructure ( #code-quality-as-observation-infrastructure — cross-component reference, see `02-tst-core/`) in the software domain. The strategic analog $\mathcal{T}_\Sigma$ ( #strategic-tempo) extends the same structure to strategy-edge revision, with the key difference that strategic edge rates are endogenous (depend on action policy and upstream success).

**Temporal nesting.** Adaptive processes stratify by timescale, with convergence constraints between levels ( #temporal-nesting).

**Mismatch dynamics.** The evolution of mismatch over time is governed by the balance between correction (via tempo) and disturbance ($\rho$) ( #mismatch-dynamics).

**Channel independence assumption.** The additive formula assumes informationally independent channels — each channel contributes non-redundant correction capacity. When channels are correlated (overlapping sensors, repeated teammate reports, redundant telemetry), the additive formula *overcounts* effective tempo. The correct tempo satisfies:

$$\mathcal{T} \leq \sum_k \nu^{(k)} \cdot \eta^{(k)*}$$

with equality iff channels are informationally independent. The gap is the *redundancy penalty* — the effective correction capacity lost to overlapping information. For two correlated channels, the penalty involves the mutual information $I(e^{(1)}; e^{(2)} \mid M_{\tau^-})$ between their event streams conditioned on the current model. Since tempo is the core capacity variable (appearing in the persistence condition, adversarial dynamics, and composition), this overcounting inflates margins wherever channel independence fails. The additive formula remains an upper bound and is exact when channels measure genuinely different aspects of the environment. Multi-agent composition ( #team-persistence) inherits this limitation: the communication tempo contribution is additive in the same sense and overcounts when different allies report correlated information.

**Scalar vs. vector tempo.** The scalar $\mathcal{T}$ assumes isotropic correction capacity. When the agent corrects some dimensions faster than others, scalar tempo overestimates effective adaptation along weak dimensions. *[Empirical Claim]* Simulation confirms: in an anisotropic 3D system (gain varying 5:1), scalar $\rho/\mathcal{T}$ overestimated by 72%, with the weak dimension accounting for 84% of total mismatch ( #observation-simulation-results). The correct formulation is per-dimension: $\mathcal{T}_k \gt \rho_k / \delta_{\text{critical},k}$ ( #per-dimension-persistence).

**(Descended from TF-11.)**