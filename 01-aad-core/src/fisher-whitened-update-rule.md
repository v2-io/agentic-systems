---
slug: fisher-whitened-update-rule
type: derivation
status: conditional
depends:
  - credit-assignment-boundary
  - edge-update-natural-parameter
  - gain-sector-bridge
  - discussion-additive-coordinate-forcing
  - agent-identity
stage: draft
---

# Derivation: Fisher-Whitened Edge Update Under Correlated Evidence

Under L1'/L2 correlated-evidence regimes, the default log-odds edge-update (from `#edge-update-natural-parameter`) retains correct *direction* — the angle between log-odds gradient and natural gradient never exceeds $45°$ at finite correlation $\rho$, so B1 directional fidelity ( #gain-sector-bridge) is never actively violated — but its *magnitude alignment* degrades by a factor $\sqrt{1-r^2}$ in the sector constant. The Fisher-whitened correction restores sharp B1 on the Fisher-weighted inner product. Under the (PI) parameterization-invariance axiom named in `#agent-identity` and promoted to a primary instance of `#discussion-additive-coordinate-forcing` via Čencov 1982, Fisher whitening is **AAD-internally derivable** rather than externally imported. The result adds sub-scope $\alpha_3$ (correlated evidence + Fisher-whitened update + Bayesian coherence → A2' derived) to the A2' partition and composes cleanly with the meta-gain machinery of `#adaptive-gain-dynamics` (Fisher whitening is a special case of meta-gain with $K_t = \mathbf I^{-1}(\lambda_t)$).

## Formal Expression

### Angle characterization under L1' correlation

*[Derived (angle-bound-finite-correlation)]*

For a block-correlated two-edge evidential model (soft-facilitator Prop B.7 parameterization), the Fisher information matrix has off-diagonal entry

$$r = \frac{\theta_C(1-\theta_C)\Delta_1 \Delta_2}{\sigma_1 \sigma_2} \in [-1, 1],$$

where $\theta_C$ is the latent-cause probability, $\Delta_j = p_{j\mid C} - p_{j\mid \neg C}$ is the separability gap, and $\sigma_j$ is the marginal-edge standard deviation. The Euclidean angle between the log-odds update direction and the natural-gradient direction (at single-edge plan residual) satisfies

$$\theta_{\text{LO-NG}} = \arccos\frac{1}{\sqrt{1 + r^2}} \leq 45° \quad \text{for all } r \in [-1, 1].$$

The log-odds update **never flips sign** under any finite correlation — B1 is never actively violated, only degraded in magnitude. Under the operational claim that "the default signal function needs validation under correlated failures," the finding is: **the default direction is preserved; only magnitude alignment degrades**. The sector constant in B1 degrades by a factor $\sqrt{1-r^2}$ under Euclidean B1; the Fisher-weighted B1 recovers the unperturbed sector constant.

### Fisher-whitened update rule

*[Definition (Fisher-whitened-update)]*

In log-odds coordinates $\lambda \in \mathbb R^{\lvert E\rvert}$ with Fisher information $\mathbf I(\lambda)$, the Fisher-whitened edge update is

$$T_{\text{FW}}(\lambda) = \lambda - \eta_{\text{edge}} \cdot \mathbf I^{-1}(\lambda) \cdot \mathbf J \cdot (\hat P_\Sigma(\sigma(\lambda)) - y_G)$$

(compared to the Euclidean log-odds update $T_{\text{edge}}(\lambda) = \lambda + \eta_{\text{edge}} \cdot \text{diag}(\iota) \cdot \mathbf J(y_G - \hat P_\Sigma)/\lVert\mathbf J\rVert^2$). The Fisher-weighted inner product $\langle a, b\rangle_\mathbf I = a^T \mathbf I^{-1} b$ makes the update's directional fidelity invariant under reparameterization of the natural-parameter coordinate.

### Two AAD-internal axiom paths

*[Derived (Fisher-whitening-from-B1-parameterization-invariance)]*

**Path A (B1-parameterization-invariance).** Require B1 directional fidelity to be *parameterization-invariant* in the sense of `#agent-identity`'s (PI) axiom: the theorems about sub-scope α derivation in `#gain-sector-bridge` should not depend on arbitrary coordinate choices for $M_t$'s natural parameters. Under (PI), B1 sub-scope α partition is coordinate-invariant iff the inner product defining the directional-fidelity condition is the Fisher metric (Čencov 1982 uniqueness theorem under (PI); extended by Ay-Jost-Lê-Schwachhöfer 2017). The Fisher-weighted inner product is therefore *forced* by (PI), and the Fisher-whitened update is the AAD-internally derived correction direction for directional-fidelity preservation across parameterizations.

**Path B (Lyapunov-coordinate-matching via adjacent-family classification).** In the adjacent-family framing of `#discussion-additive-coordinate-forcing`, the Lyapunov coordinate is *matched* (not forced) to the sector condition. For natural-gradient updates, the canonical Lyapunov is Fisher-weighted (Amari 1998, "Natural gradient works efficiently in learning," *Neural Computation* 10); this matches the geometry of the update operator. The two paths converge on the same Fisher-weighted result; Path A forces it via axiomatics, Path B confirms it via adjacent-family coordinate-matching.

Under L0 (no correlation), $r = 0$ and $\mathbf I$ is diagonal — Fisher whitening is vacuous (reduces to the existing Euclidean log-odds update). The axioms pick out Fisher whitening *uniquely* only under L1'/L2 (correlated evidence) regimes; they are vacuously satisfied under L0.

### New sub-scope $\alpha_3$

*[Derived (sub-scope-alpha-3)]*

Correlated-evidence + Fisher-whitened update + Bayesian coherence yields A2' *derived*:

$$(T_{\text{FW}}(\lambda) - \lambda^\ast)^T \mathbf I(\lambda^\ast)^{-1}(\lambda - \lambda^\ast) \geq \beta \lVert\lambda - \lambda^\ast\rVert_\mathbf{I}^2 \quad \text{with } \beta = \eta_{\text{edge}} \mu$$

on the Fisher-metric sector region around the fixed point $\lambda^\ast = \text{logit}(\theta^\ast)$. The directional-fidelity proof of `#gain-sector-bridge` carries over with $\kappa(\mathbf I)$ as Euclidean-transfer penalty — structurally identical to the Kalman case's $(P^-)^{-1}$-norm weighted-norm treatment. The Kalman case in `#gain-sector-bridge`'s Verified Instances is a special case of Fisher-weighted sector.

Sub-scope $\alpha_3$ extends the refinement introduced by `#adaptive-gain-dynamics`:
- **Sub-scope $\alpha_1$**: fixed-gain, independent evidence (Euclidean B1 applies; the existing A2' partition).
- **Sub-scope $\alpha_2$**: adaptive-gain, independent evidence (meta-gain conditions (MG-1)–(MG-4) per `#adaptive-gain-dynamics`).
- **Sub-scope $\alpha_3$**: fixed-gain, correlated evidence (Fisher-whitened update; this segment).

Additional composition: adaptive-gain + correlated-evidence (sub-scope $\alpha_4$) would compose `#adaptive-gain-dynamics` meta-gain machinery with Fisher whitening at the primary state; open.

### Connection to meta-gain as special case

*[Derived (Fisher-whitening-as-special-meta-gain)]*

The Fisher-whitened update is a meta-gain law in the sense of `#adaptive-gain-dynamics` with $K_t = \mathbf I^{-1}(\lambda_t)$ — a *degenerate* special case where the meta-gain is a deterministic function of the primary state rather than an independently learned variable. All four meta-gain conditions (MG-1)–(MG-4) are satisfied trivially:
- (MG-1) Meta-gain sector: $\mathbf I^{-1}$ is symmetric-positive-definite on the interior of the natural-parameter domain.
- (MG-2) Meta-gain bounded: $\lVert\mathbf I^{-1}\rVert$ bounded on compact natural-parameter subsets.
- (MG-3) Smoothness: $\mathbf I^{-1}$ depends smoothly on $\lambda$ for exponential families.
- (MG-4) Primary-meta coupling bounded: $\mathbf I^{-1}$'s state-derivative in the drift direction is bounded for exponential families.

This hands `#adaptive-gain-dynamics` a **concrete second instance** of derivable meta-gain alongside adaptive-Kalman-with-Mehra-estimator (its primary instance). The machinery of meta-gain composition via `#sector-persistence-template` (augmented-state Lyapunov) applies directly.

### L2 regime: candidate third `#discussion-identifiability-floor` instance or strengthening of Instance 2

*[Hypothesis (L2-latent-floor)]*

Under L2-latent regimes (unobservable correlation structure beyond what Fisher information can resolve), Fisher whitening fails: the correlation sub-block of Fisher is rank-deficient (Cramér-Rao floor on unobservable parameters). This parallels `#discussion-identifiability-floor` Instance 2's L1'-unobservable-$C$ Fisher-rank-1 obstruction — potentially a new L2 instance, or potentially a generalization of Instance 2 to higher correlation orders. Open whether these are distinct floors or a single unified obstruction.

L2-degenerate (perfect correlation, $r \to 1$) is a *structural* collapse — it requires DAG repair (edge merging) rather than update repair. This sits outside the Fisher-whitening framework.

## Epistemic Status

*Conditional.* Max attainable: *exact* under Path A ((PI) + Čencov combined with B1 directional fidelity) + L1'/L2 regimes + Bayesian coherence. The derivation is textbook information-geometry (Amari 1998; Amari-Nagaoka 2000) plus the AAD-internal (PI) axiom from `#agent-identity`. What is AAD-distinctive is (a) the identification of (PI)/Čencov as the forcing machinery rather than merely a preferred choice; (b) the sub-scope $\alpha_3$ labeling within the A2' partition; (c) the composition with `#adaptive-gain-dynamics`' meta-gain framework as a degenerate special case.

**The angle bound is ≤ 45° for all finite $r$.** This is a sharp load-bearing observation: AAD's existing default log-odds signal function is *directionally robust* under correlated failures. The bias formula in `#l1-update-bias` gives the quantitative magnitude-bias; this segment gives the qualitative direction-preservation. Together they characterize the default signal function's behavior under L1' fully: **direction preserved, magnitude biased, observable-$C$ restores exactness (Prop B.7), unobservable-$C$ floor per F13**.

**Without (PI) adoption.** If (PI) is not adopted as an AAD axiom, Fisher whitening remains a theorem-imported technique from information geometry. The sub-scope $\alpha_3$ labeling still applies (correlated evidence + Fisher-whitened + Bayesian coherence → A2' derived) but without the AAD-internal forcing. This is the adjacent-family status.

## Discussion

**Relationship to the default signal function.** `#credit-assignment-boundary`'s default log-odds signal was landed in the 2026-04-22/23 strengthening cycle via the Cauchy-FE uniqueness theorem in `#edge-update-natural-parameter`. Under L0 evidence independence, the default signal is exact. Under L1' correlated evidence, the default signal's direction is preserved (≤ 45° angle to natural-gradient direction) but magnitude degrades by $\sqrt{1-r^2}$. This segment's Fisher-whitened update is the correction under (PI)/Čencov; it recovers sharp B1 under L1' by lifting the inner product from Euclidean to Fisher.

**Relationship to `#discussion-identifiability-floor` Instance 2.** Instance 2 (L1' unobservable-$C$ Cramér-Rao floor) refutes single-channel identification of mixture parameters. Under observable $C$, Prop B.7 gives the L1' transfer; under unobservable $C$, no update — including Fisher-whitened — recovers identification. Fisher whitening operates *downstream* of identification: it corrects the update direction given that the Fisher information is known; it does not manufacture Fisher information that the data cannot yield.

**Composition with the (PI)/Čencov 4th primary instance.** The Fisher-metric cases in `#gain-sector-bridge`'s Verified Instances table (Matrix Kalman, Exponential family in natural parameters) are also AAD-internally forced under (PI)/Čencov. Fisher whitening at the edge-update layer of Section II therefore shares the same AAD-internal axiom as the Kalman / exp-family cases in Section I's update machinery. This is a cross-layer consistency: the (PI) axiom operates uniformly across Sections I and II whenever the natural parameters are parameters on a statistical manifold.

## Working Notes

- **Sub-scope $\alpha_4$ composition** (adaptive-gain + correlated-evidence). Composing `#adaptive-gain-dynamics` meta-gain machinery with Fisher whitening gives an augmented-state contraction argument where both the primary state (log-odds) and the meta-state (Fisher information estimate) are updated. Open derivation.

- **L2 regime.** Fisher whitening at L2 (non-tree correlation structure) requires computing higher-order Fisher correlations. For sparse DAG structures with limited correlation order, Fisher-tree approximations may suffice; for dense correlation structures, the computational cost scales exponentially. Scope boundary for Fisher whitening as a practical technique.

- **Relationship to natural-gradient variational inference.** Khan & Lin 2017 (*Conjugate-computation variational inference*) derives natural-gradient VI as a special case of conjugate Bayesian computation. Under (PI)/Čencov, their result becomes AAD-internally derived within sub-scope $\alpha_3$. This composes with `#variational-sector-condition` if that segment lands — natural-gradient VI would be the $\varepsilon = 0$ limit of ε-fidelity B1.

- **Landing context.** This segment lands from `msc/spike-fisher-whitened-update.md` (2026-04-23 Gap A/B cycle). The AAD-internal axiom path via (PI)/Čencov was validated by `msc/spike-jacobian-b1-strengthening.md` (2026-04-23 follow-up); see that spike for the broader discussion of uniqueness-theorem machinery clearing the `#discussion-additive-coordinate-forcing` discipline.
