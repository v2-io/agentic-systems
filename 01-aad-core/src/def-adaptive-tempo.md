---
slug: def-adaptive-tempo
type: definition
status: exact
depends:
  - emp-update-gain
  - form-event-driven-dynamics
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
- $\eta^{(k)\ast}$ is the optimal update gain on channel $k$ ( #emp-update-gain)

Single-channel special case: $\mathcal{T} = \nu \cdot \eta^\ast$.

### Tensor extension under Fisher-local invariance regime

*[Definition (tensor-adaptive-tempo)]*

Under the Fisher-local invariance regime ( #deriv-fisher-local-update-gain), the optimal update gain on channel $k$ is matrix-valued: $K^{(k)} = (H_M + H_L^{(k)})^{-1} H_L^{(k)}$, with $H_M = U_M^{-1}$ the prior precision and $H_L^{(k)} = (U_o^{(k)})^{-1}$ the channel-$k$ observed Fisher information. The tensor adaptive tempo is then

$$\mathcal{T} = \sum_k \nu^{(k)} \cdot K^{(k)}$$

— matrix-valued, with per-direction rates given by the eigenvalues of $\sum_k \nu^{(k)} K^{(k)}$ in the appropriate basis. The scalar form $\mathcal T = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$ is recovered in the **shared-eigenbasis collapse**: when all $H_M, \{H_L^{(k)}\}$ commute (always in 1-D; under (PI)/Čencov along the natural-gradient direction in higher dimensions), each $K^{(k)}$ acts as the eigenvalue $\eta^{(k)\ast} = U_M/(U_M + U_o^{(k)})$ on the shared natural-gradient direction and the matrix sum collapses to a scalar.

The matrix gain operator $K^{(k)}$ is the per-coordinate primitive: in anisotropic regimes where the prior and likelihoods do not share an eigenbasis (or where different channels pin down different directions), the tensor form preserves the per-direction information that the scalar form averages away.

## Epistemic Status

This is a *definition*. It names the quantity that characterizes an agent's total corrective capacity, combining loop speed ($\nu$) and epistemic quality ($\eta^\ast$). The definition itself is not a truth-claim; the substantive claims are in the results that use it ( #result-persistence-condition, #result-adversarial-tempo-advantage).

**Scope of scalar vs. tensor forms.** The scalar form is exact in the isotropic / shared-eigenbasis / nonredundant-channel case and is what downstream results currently invoke. The tensor form is the natural object under anisotropic gains, Fisher-whitened updates ( #deriv-fisher-whitened-update-rule), LMI causal-IB ( #deriv-causal-ib-lmi), and per-dimension persistence ( #result-per-dimension-persistence) — regimes where scalar tempo overestimates effective adaptation along weak dimensions. Downstream results that invoke scalar $\mathcal T$ implicitly assume scalar / isotropic / nonredundant-channel scope; promoting them to the tensor form under the appropriate anisotropic regime is a follow-on cycle item flagged in `TODO.md`.

## Discussion

**Speed-quality substitutability.** An agent can achieve the same tempo via a fast noisy loop (high $\nu$, low $\eta^\ast$) or a slower calibrated one (low $\nu$, high $\eta^\ast$). The product structure means improvements to *both* factors compound multiplicatively.

**Observation noise gating.** Because $\eta^\ast = U_M / (U_M + U_o)$, high observation noise ($U_o$) depresses gain and collapses tempo regardless of loop speed. You cannot outrun a bad observation channel by iterating faster. This grounds Boyd's emphasis on Orient quality over raw OODA speed.

**Centrality.** Tempo is AAD's core capacity metric. It appears on the left side of the persistence condition ( #result-persistence-condition), determines adversarial advantage ( #result-adversarial-tempo-advantage), and connects to code quality as observation infrastructure ( #der-code-quality-as-observation-infrastructure — cross-component reference, see `02-tst-core/`) in the software domain. The strategic analog $\mathcal{T}_\Sigma$ ( #def-strategic-tempo) extends the same structure to strategy-edge revision, with the key difference that strategic edge rates are endogenous (depend on action policy and upstream success).

**Temporal nesting.** Adaptive processes stratify by timescale, with convergence constraints between levels ( #der-temporal-nesting).

**Mismatch dynamics.** The evolution of mismatch over time is governed by the balance between correction (via tempo) and disturbance ($\rho$) ( #hyp-mismatch-dynamics).

**Channel independence assumption.** The additive formula assumes informationally independent channels — each channel contributes non-redundant correction capacity. When channels are correlated (overlapping sensors, repeated teammate reports, redundant telemetry), the additive formula *overcounts* effective tempo. The correct tempo satisfies:

$$\mathcal{T} \leq \sum_k \nu^{(k)} \cdot \eta^{(k)*}$$

with equality iff channels are informationally independent. The gap is the *redundancy penalty* — the effective correction capacity lost to overlapping information. For two correlated channels, the penalty involves the mutual information $I(e^{(1)}; e^{(2)} \mid M_{\tau^-})$ between their event streams conditioned on the current model. Since tempo is the core capacity variable (appearing in the persistence condition, adversarial dynamics, and composition), this overcounting inflates margins wherever channel independence fails. The additive formula remains an upper bound and is exact when channels measure genuinely different aspects of the environment. Multi-agent composition ( #der-team-persistence) inherits this limitation: the communication tempo contribution is additive in the same sense and overcounts when different allies report correlated information.

**Scalar vs. vector tempo.** The scalar $\mathcal{T}$ assumes isotropic correction capacity. When the agent corrects some dimensions faster than others, scalar tempo overestimates effective adaptation along weak dimensions. *[Empirical Claim]* Simulation confirms: in an anisotropic 3D system (gain varying 5:1), scalar $\rho/\mathcal{T}$ overestimated by 72%, with the weak dimension accounting for 84% of total mismatch ( #obs-section-i-validation-simulations). The correct formulation is per-dimension: $\mathcal{T}_k \gt \rho_k / \delta_{\text{critical},k}$ ( #result-per-dimension-persistence). The tensor extension above ( #deriv-fisher-local-update-gain) gives the per-coordinate primitive $K^{(k)}$ that the per-dimension persistence result invokes — the matrix gain operator on each channel — making the per-dimension formulation a direct consequence of the tensor tempo definition rather than a separate generalization. Under cross-dimensional correction (off-diagonal $\mathcal{T}$ in the coordinate basis of $D_\delta$), the matrix-Loewner persistence condition `#deriv-matrix-persistence-condition` is the canonical form: $\Sigma_\infty \prec D_\delta = \mathrm{diag}(\delta_{\text{critical},k}^2)$ in the strict positive-definite order, with $\Sigma_\infty$ solving the continuous Lyapunov equation $\mathcal{T}\Sigma_\infty + \Sigma_\infty\mathcal{T}^T = \Sigma_w$. The per-coordinate form is its diagonal-axis-aligned special case; matrix-Loewner is strictly sharper (the per-coordinate form is *unsafe* when $\mathcal{T}$'s eigenbasis misaligns with the coordinate axes — `#deriv-matrix-persistence-condition` §"Where per-coordinate is unsafe").