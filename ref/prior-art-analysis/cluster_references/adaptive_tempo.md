# Cluster Reference: Adaptive Tempo and Fisher-Local Gain

**Overview:** Defines Adaptive Tempo as the central scalar and tensor capacity metric, bridging loop speed and epistemic update quality (gain) via Fisher information.

---

## Canonical Source Segments

### Source: `emp-update-gain.md`

```yaml
---
slug: emp-update-gain
type: empirical
status: robust-qualitative
depends:
  - def-mismatch-signal
  - def-observation-function
stage: claims-verified
---
```


# Empirical: Update Gain

The optimal weight an agent assigns to new observations when updating its model — the rate of *epistrophe* (turning toward reality). How much the agent should trust the incoming observation versus its own prior understanding.

## Formal Expression

*[Empirical Claim (uncertainty-ratio-principle)]*

$$\eta^* = \frac{U_M}{U_M + U_o}$$

where:
- $\eta^\ast$ is the optimal update gain (proportion of mismatch used to correct the model)
- $U_M$ is model uncertainty (predictive variance or entropy)
- $U_o$ is irreducible observation noise

The update rule takes the form:

*[Formulation]*

$$M_t = M_{t-1} + \eta^* \cdot g(\delta_t)$$

where $\delta_t$ is the mismatch ( #def-mismatch-signal) and $g(\cdot)$ is a correction mapping from observation space to model update space.

## Epistemic Status

*Derived* under the **Fisher-local invariance regime** ( #deriv-fisher-local-update-gain): for any smooth log-likelihood admitting non-degenerate local quadratic expansion, the natural-gradient Bayesian posterior mean shift at first order in the step size is exactly $\Delta\theta = K \cdot \tilde\nabla$ with gain operator $K = (H_M + H_L)^{-1} H_L$ and scalar collapse $\eta^\ast = U_M/(U_M + U_o)$ along the natural-gradient direction (always in 1-D; under (PI)/Čencov in higher dimensions). Linear-Gaussian (Kalman) and conjugate-Bayesian instances are cases where the local quadratic expansion is *globally* exact, so the form holds without truncation. For general smooth models, the natural-gradient invariance theorem of Amari 1998 guarantees the form is exact at the local-tangent-plane Pythagorean projection level.

Outside the Fisher-local regime — non-quadratic losses, non-conjugate priors, structurally non-Gaussian uncertainty (heavy tails, multimodality) — the dependence is *robust qualitative*: the **direction** is preserved (gain rises with model uncertainty, falls with observation noise) and the first-order form is recovered locally; what need not hold is global quantitative fidelity. The qualitative direction is the load-bearing claim for downstream tempo and persistence machinery; the Fisher-local exact form is the load-bearing claim for the Kalman, conjugate, and natural-gradient instantiations.

## Discussion

**Limiting behavior.** When $U_M \gg U_o$ (high model uncertainty — e.g., after initialization or structural adaptation), $\eta^\ast \to 1$: trust the observation. When $U_M \ll U_o$ (confident model, noisy channel), $\eta^\ast \to 0$: trust the model. The gain determines how strongly the agent corrects toward reality on each update.

**Resolving Epistemic Opacity.** The optimal gain equation requires the agent to know $U_o$, which seems to violate the epistemic opacity axiom established in `#def-observation-function` (the agent does not know the true noise distribution $\varepsilon_t$). This tension is resolved dynamically: the agent *estimates* $U_o$ (and $U_M$) from the observable statistics of its own mismatch sequence (innovations), treating the gain itself as an endogenous state variable. See `#deriv-adaptive-gain-dynamics` for the proof of how this meta-adaptation maintains Lyapunov stability without violating opacity.

**Gain collapse — epistrophe failure.** When the agent incorrectly estimates $U_M \to 0$ (spurious confidence) or $U_o \to \infty$ (spurious distrust of sensors), $\eta^\ast \to 0$ and epistrophe ceases. Aporia still arrives — the mismatch signal is still generated — but the agent no longer turns toward it. Mismatches are ignored, producing confirmation bias or a decoupled reality model. The cycle runs but the corrective phase is hollow.

**Multi-dimensional generalization.** In vector-valued systems, $U_M$ and $U_o$ are covariance matrices and $\eta^\ast$ becomes a gain matrix (as in the Kalman filter). The scalar form captures the essential structure.

**Connection to adaptive tempo.** The update gain is one factor in the agent's adaptive tempo ( #def-adaptive-tempo): $\mathcal{T} = \nu \cdot \eta^\ast$. Frequent aisthesis (high $\nu$) is useless if epistrophe extracts no information (low $\eta^\ast$). Gain measures the *quality* of the cycle's corrective phase; event rate measures its *speed*.

**Gain dynamics.** The optimal gain changes over time following predictable patterns:

- *Convergence*: As the model accumulates information, $U_M$ decreases, so $\eta^\ast \to 0$. The model becomes increasingly resistant to individual observations. This IS Kalman filter convergence, Bayesian posterior concentration, and RL learning rate annealing.
- *Reset after structural change*: When the environment changes in ways the model cannot track incrementally ( #result-structural-adaptation-necessity), $U_M$ should spike — the model "admits" its uncertainty. The gain increases, enabling rapid re-learning. An agent whose gain does NOT reset after structural change will continue trusting a stale model — Boyd's "incestuous amplification" and the cause of brittle failure in non-stationary environments.

**Overfitting as gain miscalibration.** From #result-mismatch-decomposition: $\mathbb{E}[\Vert\delta_t\Vert^2]$ = model error + irreducible noise. An agent with $\eta$ too high adjusts its model to explain observation noise, increasing model error on future predictions. An agent with $\eta$ too low fails to correct genuine model errors. The optimal gain implicitly separates signal from noise by weighting observations in proportion to their informativeness — exactly what $U_M/(U_M + U_o)$ achieves when $U_o$ captures the irreducible noise.

**Representation note.** The additive form operates in a *representation space* appropriate to the model. For Bayesian posteriors (where update is multiplicative: $P(\theta \mid D) \propto P(D \mid \theta) P(\theta)$), the additive rule operates in log-probability or natural parameter space. For models on constrained manifolds (probability simplices, rotation groups), the update must be projected onto the manifold. The claim is not that all updates are literally additive in native parameterization, but that they have the structure "current state + gain × transformed mismatch" in an appropriate coordinate system.

**Domain validation:**

| Domain | Gain form | Mapping quality |
|--------|-----------|-----------------|
| Kalman filter | $K_t = P_{t\Vertt-1} H^T (H P_{t\Vertt-1} H^T + R)^{-1}$ | **Exact.** Scalar case is exactly $U_M/(U_M + U_o)$. |
| Conjugate Bayesian | Posterior weight $n/(n + \kappa)$ cumulative; incremental $1/(n + \kappa)$ | **Exact** for conjugate families. Incremental gain decreases as data accumulates. |
| RL (Q-learning) | Fixed learning rate $\alpha$ | **Approximate.** $\alpha$ is a degenerate constant gain — does not adapt to uncertainty. Advanced methods (Bayesian RL, Adam) converge toward the optimal form. |
| PID control | Fixed gains $(K_p, K_i, K_d)$ | **Simplified.** Gains set at design time. Adaptive PID and MPC move toward the full framework. |
| Software developer | Implicit trust weighting of information sources | **Structural analogy.** New developer (high $U_M$) trusts observations heavily; experienced developer (low $U_M$) trusts their model. Gain reset after major refactoring. |

**Simulation validation.** Numerical experiments (track-b, Variant E) validated the uncertainty ratio principle under observation noise. Riccati-optimal gain reduced steady-state mismatch by 52% compared to fixed gain when observation noise was moderate. The optimal gain also proved critical in adversarial settings: under heavy observation noise, optimal gain preserved more than double the adversarial tempo advantage exponent (0.40 vs 0.18) compared to fixed gain.

**Open questions:**

1. *Non-parametric models*: For neural networks without well-defined scalar $U_M$, how should it be computed? Ensemble methods, dropout-based uncertainty, and Bayesian neural networks are all approximations.
2. *Matrix vs scalar gain*: In high-dimensional systems, the gain is a matrix (Kalman) or per-parameter (Adam). The cross-dimensional structure (covariance) adds complexity. The scalar captures the principle; the matrix captures the full optimization.

---

### Source: `def-adaptive-tempo.md`

```yaml
---
slug: def-adaptive-tempo
type: definition
status: exact
depends:
  - emp-update-gain
  - form-event-driven-dynamics
stage: claims-verified
---
```


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

**Centrality.** Tempo is AAT's core capacity metric. It appears on the left side of the persistence condition ( #result-persistence-condition), determines adversarial advantage ( #result-adversarial-tempo-advantage), and connects to code quality as observation infrastructure ( #der-code-quality-as-observation-infrastructure — cross-component reference, see `02-tst-core/`) in the software domain. The strategic analog $\mathcal{T}_\Sigma$ ( #def-strategic-tempo) extends the same structure to strategy-edge revision, with the key difference that strategic edge rates are endogenous (depend on action policy and upstream success).

**Temporal nesting.** Adaptive processes stratify by timescale, with convergence constraints between levels ( #der-temporal-nesting).

**Mismatch dynamics.** The evolution of mismatch over time is governed by the balance between correction (via tempo) and disturbance ($\rho$) ( #hyp-mismatch-dynamics).

**Channel independence assumption.** The additive formula assumes informationally independent channels — each channel contributes non-redundant correction capacity. When channels are correlated (overlapping sensors, repeated teammate reports, redundant telemetry), the additive formula *overcounts* effective tempo. The correct tempo satisfies:

$$\mathcal{T} \leq \sum_k \nu^{(k)} \cdot \eta^{(k)*}$$

with equality iff channels are informationally independent. The gap is the *redundancy penalty* — the effective correction capacity lost to overlapping information. For two correlated channels, the penalty involves the mutual information $I(e^{(1)}; e^{(2)} \mid M_{\tau^-})$ between their event streams conditioned on the current model. Since tempo is the core capacity variable (appearing in the persistence condition, adversarial dynamics, and composition), this overcounting inflates margins wherever channel independence fails. The additive formula remains an upper bound and is exact when channels measure genuinely different aspects of the environment. Multi-agent composition ( #der-team-persistence) inherits this limitation: the communication tempo contribution is additive in the same sense and overcounts when different allies report correlated information.

**Scalar vs. vector tempo.** The scalar $\mathcal{T}$ assumes isotropic correction capacity. When the agent corrects some dimensions faster than others, scalar tempo overestimates effective adaptation along weak dimensions. *[Empirical Claim]* Simulation confirms: in an anisotropic 3D system (gain varying 5:1), scalar $\rho/\mathcal{T}$ overestimated by 72%, with the weak dimension accounting for 84% of total mismatch ( #obs-section-i-validation-simulations). The correct formulation is per-dimension: $\mathcal{T}_k \gt \rho_k / \delta_{\text{critical},k}$ ( #result-per-dimension-persistence). The tensor extension above ( #deriv-fisher-local-update-gain) gives the per-coordinate primitive $K^{(k)}$ that the per-dimension persistence result invokes — the matrix gain operator on each channel — making the per-dimension formulation a direct consequence of the tensor tempo definition rather than a separate generalization. Under cross-dimensional correction (off-diagonal $\mathcal{T}$ in the coordinate basis of $D_\delta$), the matrix-Loewner persistence condition `#deriv-matrix-persistence-condition` is the canonical form: $\Sigma_\infty \prec D_\delta = \mathrm{diag}(\delta_{\text{critical},k}^2)$ in the strict positive-definite order, with $\Sigma_\infty$ solving the continuous Lyapunov equation $\mathcal{T}\Sigma_\infty + \Sigma_\infty\mathcal{T}^T = \Sigma_w$. The per-coordinate form is its diagonal-axis-aligned special case; matrix-Loewner is strictly sharper (the per-coordinate form is *unsafe* when $\mathcal{T}$'s eigenbasis misaligns with the coordinate axes — `#deriv-matrix-persistence-condition` §"Where per-coordinate is unsafe").

---

### Source: `deriv-fisher-local-update-gain.md`

```yaml
---
slug: deriv-fisher-local-update-gain
type: derivation
status: conditional
depends:
  - emp-update-gain
  - def-mismatch-signal
  - def-observation-function
  - scope-agent-identity
  - disc-additive-coordinate-forcing
  - deriv-fisher-whitened-update-rule
  - deriv-adaptive-gain-dynamics
stage: draft
---
```


# Derivation: Fisher-Local Update Gain

Under the **Fisher-local invariance regime** — smooth log-likelihood admitting non-degenerate local quadratic expansion at the current model parameter, with single-step update at first order in the step size — the natural-gradient Bayesian posterior mean shift has the form $\Delta\theta = K \cdot \tilde\nabla$ with **gain operator** $K = (H_M + H_L)^{-1} H_L$ and **scalar collapse** $\eta^\ast = U_M/(U_M + U_o)$ along the natural-gradient direction in the commuting / shared-eigenbasis case (always in 1-D; under (PI)/Čencov in the natural-gradient direction in higher dimensions). The result derives the form `#emp-update-gain` carries as an empirical claim, places it in the Fisher-local regime as exact, and recovers linear-Gaussian (Kalman) and conjugate-Bayesian instances as cases where the local quadratic expansion is globally exact. Companion at the model-parameter-update layer to `#deriv-fisher-whitened-update-rule`'s edge-update derivation: that segment derives update *direction* under correlated evidence; this segment derives update *magnitude* under the Fisher-local regime. Both share the (PI) parameterization-invariance axiom from `#scope-agent-identity` and Čencov 1982 uniqueness as AAT-internal forcing for the Fisher metric.

## Formal Expression

### Setup — Fisher-local quadratic regime

*[Definition (Fisher-local regime, conditions (R1)–(R3))]*

Let $\theta \in \mathbb R^d$ parameterize the agent's model and $\theta_t$ be the current point estimate (mode of the prior $\pi_0$, or center of expansion). Three regime conditions:

- **(R1) Smooth log-likelihood admitting non-degenerate local quadratic expansion.** $\log \pi_0$ and $\log p(o \mid \cdot)$ are $C^3$ in a neighborhood of $\theta_t$, with prior precision $H_M := -\nabla^2 \log \pi_0(\theta_t)$ and observed information $H_L := -\nabla^2 \log p(o \mid \theta) \big\vert_{\theta_t}$ satisfying $H_M + H_L \succ 0$ (joint positive-definiteness; see §"Boundary admissibility" for why this is weaker than $H_M \succ 0$ and $H_L \succ 0$ both).
- **(R2) First-order-in-step-size regime.** The posterior update $\Delta\theta = \theta_{t+1} - \theta_t$ is small enough that $O(\lVert\Delta\theta\rVert^3)$ terms in the quadratic expansion are negligible compared to the quadratic terms.
- **(R3) Bayesian-coherent update.** $\theta_{t+1}$ is taken to be a coordinate of the posterior $p(\theta \mid o) \propto \pi_0(\theta) \cdot p(o \mid \theta)$ — mean, mode, or natural-parameter (they coincide for Gaussian posteriors, which is what the quadratic expansion produces).

Under (R1)–(R3), the local log-posterior is

$$\log p(\theta \mid o) = \mathrm{const} + s^T(\theta - \theta_t) - \tfrac{1}{2}(\theta - \theta_t)^T (H_M + H_L)(\theta - \theta_t) + O(\lVert\theta - \theta_t\rVert^3),$$

where $s := \nabla_\theta \log p(o \mid \theta) \big\vert_{\theta_t}$ is the score. The posterior is approximately $\mathcal N(\theta^\star, (H_M + H_L)^{-1})$ with mean shift

*[Derived (posterior-mean-shift)]*

$$\theta^\star - \theta_t = (H_M + H_L)^{-1} s.$$

The AAT-vocabulary correspondences are

$$U_M := H_M^{-1}, \qquad U_o := H_L^{-1}$$

— model uncertainty is the inverse prior precision, observation uncertainty is the inverse Fisher / inverse observed information (Cramér-Rao floor on what the observation pins down). The matrix forms generalize `#emp-update-gain`'s scalar $U_M, U_o$ in the natural way.

### Gain decomposition on the natural-gradient direction

*[Definition (natural gradient at the current point)]*

The **natural gradient** of the log-likelihood at $\theta_t$ in the Fisher metric is

$$\tilde\nabla \log p(o \mid \theta_t) := \mathcal I(\theta_t)^{-1} s.$$

For a single observation in the Fisher-local regime, $\mathcal I(\theta_t) = H_L$ up to the observed-vs-expected information distinction (standard under (R1)+regularity); the derivations below use $H_L$ directly as the Fisher.

*[Derived (gain-decomposition)]*

Rewriting the posterior mean shift in the natural-gradient direction:

$$\Delta\theta = (H_M + H_L)^{-1} s = (H_M + H_L)^{-1} H_L \cdot (H_L^{-1} s) = K \cdot \tilde\nabla,$$

with **gain operator**

$$\boxed{\;K := (H_M + H_L)^{-1} H_L.\;}$$

The matrix-valued $K$ is the natural object. The scalar collapse follows in the commuting / shared-eigenbasis case (always in 1-D; under (PI)/Čencov along the natural-gradient direction in higher dimensions): eigenvalues of $K$ are

$$\eta^\ast_i = \frac{h_{L,i}}{h_{M,i} + h_{L,i}} = \frac{1/u_{o,i}}{1/u_{M,i} + 1/u_{o,i}} = \frac{u_{M,i}}{u_{M,i} + u_{o,i}}$$

per coordinate, collapsing to the scalar

$$\boxed{\;\eta^\ast = \frac{U_M}{U_M + U_o}\;}$$

— the form `#emp-update-gain` carries, derived from the Fisher-local quadratic expansion of prior and likelihood and applied to the natural-gradient direction.

### Boundary admissibility — improper-prior and degenerate-likelihood directions

*[Derived (admissibility-of-degenerate-curvature)]*

The gain operator $K = (H_M + H_L)^{-1} H_L$ is well-defined whenever $H_M + H_L \succ 0$ — not necessarily when both $H_M$ and $H_L$ are individually positive-definite. This admits **degenerate-likelihood directions** (observation uninformative along some coordinates, $H_L$ rank-deficient): $K$'s eigenvalue along those directions is $0$, $u_{o,i} \to \infty$, $\eta^\ast_i \to 0$, no update along that direction — *trust the prior where the observation says nothing*. It also admits **improper-prior directions** (degenerate prior, $H_M = 0$ along some coordinate) when $H_L$ pins the direction: $\eta^\ast_i \to 1$ along uninformative-prior directions where the observation is informative — *trust the observation where the prior says nothing*, the maximum-likelihood limit.

The minimal regime condition is $H_M + H_L \succ 0$, with $U_M/(U_M + U_o)$ defined per-eigendirection by the appropriate limit. This corresponds to standard improper-prior admissibility in Bayesian inference and to standard observation-non-identifiability admissibility in maximum-likelihood estimation.

### Recovery of linear-Gaussian and conjugate-Bayesian cases

*[Derived (global-exactness-special-cases)]*

When the quadratic expansion in (R1) holds *globally* — not just locally — the derivation gives $\eta^\ast$ without any expansion error. Two canonical cases:

- **Linear-Gaussian (Kalman).** Prior $\mathcal N(\theta_t, U_M)$, likelihood $\mathcal N(o; H \theta, U_o)$ with linear observation operator $H$: the log-posterior is exactly quadratic. The scalar Kalman gain $K = U_M H^T (H U_M H^T + U_o)^{-1}$ collapses to $\eta^\ast = U_M/(U_M + U_o)$ in the scalar case (Kalman 1960; Bishop 2006 §3.3). Exact globally.
- **Conjugate Bayesian (Beta-Bernoulli, Dirichlet-multinomial, Gaussian-Gaussian, exponential-family natural-parameter conjugacy).** Natural-gradient VI is the exact posterior update at step size $1$ for conjugate families (Khan-Lin 2017 conjugate-computation variational inference). The Fisher-local expansion is globally exact in natural-parameter coordinates; $\eta^\ast = U_M/(U_M + U_o)$ holds exactly with $U_M, U_o$ read from the conjugate sufficient-statistic precision counts.

For general smooth models, the natural-gradient invariance theorem of Amari 1998 guarantees that the natural gradient is parameterization-invariant; the Fisher-local quadratic expansion is the order at which the natural gradient and the exact posterior agree to first order in step size.

## Epistemic Status

*Conditional.* Max attainable: *exact* under (R1)–(R3) + (PI) parameterization-invariance from `#scope-agent-identity`. Under (PI) and Čencov 1982 uniqueness, the Fisher metric is the AAT-internally canonical metric on the statistical manifold (the 4th primary instance of `#disc-additive-coordinate-forcing`); the natural-gradient direction is therefore the AAT-internally canonical reference direction along which $\eta^\ast$ reads as $U_M/(U_M + U_o)$. The textbook information-geometry result (Amari 1998 natural-gradient invariance theorem) is imported; the (PI)/Čencov forcing in `#deriv-fisher-whitened-update-rule`'s Path A makes the import AAT-internal.

Linear-Gaussian (Kalman) and conjugate-Bayesian instances are cases where the local quadratic expansion is *globally* exact, so $\eta^\ast = U_M/(U_M + U_o)$ holds without truncation error.

Outside the Fisher-local regime — heavy-tailed posteriors (no second moment), structurally non-smooth likelihoods, multimodal uncertainty where the local quadratic misrepresents global structure — the quantitative form is *not* derived here. The *qualitative* direction (gain rises with model uncertainty, falls with observation noise) is preserved as *robust qualitative* from `#emp-update-gain`'s broader empirical scope; the first-order form is recovered locally; what need not hold is global quantitative fidelity.

This segment depends on (PI) from `#scope-agent-identity` only. The triple (PI)+(R)+(K) of the Markov-morphism layer (carried by the Fisher-Rao bias-bound machinery; the (R) Riemannian-structure and (K) KL-second-order-matching axioms are stronger) is *not* invoked here. If (R) and (K) are asserted at the scope-level in a future cycle, this segment's status remains conditional on (PI) alone unless explicitly extended.

## Discussion

**Why read $\eta^\ast$ off the natural-gradient direction.** The Bayesian-coherent posterior mean shift $\Delta\theta = (H_M + H_L)^{-1} s$ is a fixed vector; its decomposition into "gain times reference direction" depends on the choice of reference direction. Two natural choices give two faces of the same shift:

- **Natural-gradient direction $\tilde\nabla = H_L^{-1} s$.** Coefficient: $\eta^\ast_{\text{NG}} = H_L/(H_M + H_L) = U_M/(U_M + U_o)$. *AAT-internally canonical* under (PI)/Čencov — the Fisher metric is the unique Markov-invariant metric, so the natural gradient is the unique coordinate-invariant gradient direction (Čencov 1982; extended by Ay-Jost-Lê-Schwachhöfer 2017).
- **Prior-curvature-rescaled direction $H_M^{-1} s$.** Coefficient: $\eta^\star_{\text{prior}} = H_M/(H_M + H_L) = U_o/(U_M + U_o)$. The *complement*; the same algebraic decomposition arises in Kalman literature as the prior weight in the convex combination "posterior = (1-K) prior + K observation."

The two coefficients are duals on the same posterior shift; their product reduces to the posterior covariance $(H_M + H_L)^{-1}$. AAT names the natural-gradient coefficient as the canonical $\eta^\ast$ because (PI)/Čencov picks out the natural-gradient direction as the unique coordinate-invariant choice.

**Three derivation routes converge.** The same scalar $\eta^\ast = U_M/(U_M + U_o)$ falls out of three independent structural derivations:

| Route | Lever | Surface meaning of $\eta^\ast$ |
|---|---|---|
| Local-Gaussian Laplace expansion (§Setup–Gain decomposition above) | Algebraic completion of squares on additive log-posterior quadratics | Posterior mean shift coefficient on the natural-gradient direction |
| Bregman / KL projection onto the local tangent plane | First-order condition on the variational free energy along natural-gradient tilt | Projection coefficient of the posterior onto the local tangent plane (Pythagorean projection in Fisher metric per Amari-Nagaoka 2000 §3.2) |
| Cramér-Rao / inverse-Fisher | Precision-additive composition $1/U_M + 1/U_o$, inverted | Fractional observation contribution to posterior precision |

The agreement is not coincidence: the Fisher-local regime *is* the regime where prior and likelihood compose as a Pythagorean projection in the Fisher metric — the same exponential-family / Bregman / Pythagorean structure underlying `#deriv-strategy-cost-regret-bound`'s $\rho$-decomposition. The three routes are three faces of one geometric object: precision-additive composition of two Gaussian information sources, read off the natural-gradient direction.

**Sibling positioning vs `#deriv-fisher-whitened-update-rule`.** That segment lives at the **edge-update layer** of Section II's strategy DAG: it derives the Fisher-whitening correction for the *direction* of edge updates under correlated evidence (L1'/L2). This segment lives at the **model-parameter-update layer** of Section I: it derives the *magnitude* of the natural-gradient Bayesian update via the Fisher-local invariance regime. Both depend on (PI) + Čencov as the AAT-internal axiom forcing the Fisher metric. Together they make the Fisher-local invariance regime AAT-internally complete: direction (whitening) at the edge layer and magnitude (gain) at the model-parameter layer are both derived from the same axiomatic chain.

**Special case of `#deriv-adaptive-gain-dynamics`' meta-gain framework.** The gain operator $K = (H_M + H_L)^{-1} H_L$ is a *deterministic function of the current state* — it depends on the prior covariance $H_M^{-1}$ (part of the agent's $M_t$ state) and on the observation Fisher $H_L$ (depends on $\theta_t$ and $o$). It is therefore the **deterministic-meta-gain** special case of `#deriv-adaptive-gain-dynamics`' (MG-1)–(MG-4) machinery: the meta-gain is determined by the primary state rather than independently learned. All four meta-gain conditions are satisfied trivially (symmetric-positive-definite $K$ on the interior; smoothness for exponential families; bounded primary-meta coupling). Resolving the epistemic-opacity question that `#def-observation-function` axiomatizes — i.e., the agent does not know $U_o$ a priori and must estimate it from its own mismatch sequence — is one level up: it adds the Mehra-style meta-channel that `#deriv-adaptive-gain-dynamics` treats as its primary instance.

**Downstream tempo and persistence machinery.** `#emp-update-gain`'s Discussion §"Connection to adaptive tempo" names $\mathcal T = \nu \cdot \eta^\ast$. The derivation here promotes $\eta^\ast$'s tier from `empirical / robust-qualitative` (over the cross-domain validity tail — RL, PID, software-developer) to `derived (conditional on Fisher-local regime)` for the Kalman / conjugate / natural-gradient core. The tempo product $\mathcal T = \nu \cdot \eta^\ast$ inherits the regime distinction directly; the persistence-condition machinery (`#result-persistence-condition`, `#result-sector-condition-stability`) and the adaptive-tempo / aporia diagnostics (`#def-adaptive-tempo`, `#def-aporia`) all gain the tighter $\eta^\ast$ exactness statement in their Fisher-local instances. The qualitative direction claim and the failure-mode framing (gain-collapse → epistrophe failure) survive unchanged outside the Fisher-local regime.

**Tensor adaptive tempo connection.** The matrix gain operator $K$ is the per-coordinate primitive for tensor-valued adaptive tempo: $\mathcal T = \nu \cdot K$ as a matrix product, with the existing scalar $\mathcal T = \nu \cdot \eta^\ast$ recovered in the shared-eigenbasis limit. See `#def-adaptive-tempo`'s Tensor extension.

## Working Notes

- **Multi-step extrapolation rate.** The Fisher-local exactness is a one-step statement. Iterating over many observations accumulates higher-order curvature error in the non-Gaussian / non-conjugate case. Bernstein-von Mises asymptotics (van der Vaart 1998 §10.2) give a $1/\sqrt n$ posterior concentration rate; whether $\eta^\ast$'s exactness inherits a matching $1/\sqrt n$ degradation outside Kalman / conjugate is an open quantitative-rate question. Open spike candidate.
- **Edgeworth higher-order correction.** The $O(\lVert\Delta\theta\rVert^3)$ correction to $\eta^\ast$ in terms of third / fourth derivatives of the log-likelihood admits a standard Edgeworth-expansion treatment. Worth a follow-up spike if it becomes load-bearing for any AAT use case.
- **Variational-bound extension.** Under variational approximation $\mathrm{KL}(q \Vert p) \leq \varepsilon$, the gain inherits a Pinsker-tight degradation factor analogous to `#deriv-variational-sector-condition`'s $O(\sqrt\varepsilon)$ B1 degradation. Composing this with the derivation gives $\eta^\ast$ in sub-scope $\alpha'$ under approximate-posterior agents.
- **Multimodal posteriors.** When the prior or posterior is multimodal, the local-quadratic expansion around any one mode misses the global structure. Two natural moves: per-mode $U_M/(U_M + U_o)$ with mode-mixture weights as a separate state; or accept the qualitative direction claim only. Worth a follow-up spike if multimodal posteriors become load-bearing.
- **Consolidation / replay connection.** `#form-consolidation-dynamics`-style between-event consolidation drives $U_M$ up (model uncertainty grows under offline replay via IB-gap reduction). The next online observation gets up-weighted because $U_M/(U_M + U_o)$ rises with $U_M$. This is the formal connection between consolidation-induced uncertainty growth and increased online responsiveness — worth tightening into a result if `#form-consolidation-dynamics` lands a quantitative form.
- **Honest obstructions.** (O1) The natural-gradient invariance theorem (Amari 1998) is imported, not derived; the (PI)/Čencov forcing in `#deriv-fisher-whitened-update-rule`'s Path A makes the import AAT-internal. Without (PI), the natural-gradient direction is a chosen-not-forced direction and the derivation degrades to "the form on the chosen direction." (O2) Single-observation per-step setup; multi-observation batches generalize mechanically ($H_L = \sum_i H_{L,i}$ for independent observations). (O3) Matrix vs scalar — the matrix $K$ is the natural object; the scalar $U_M/(U_M + U_o)$ is its eigenvalue in the commuting / 1-D / shared-eigenbasis case. (O4) Step-size boundary qualitative; the actual Fisher-local cutoff depends on the third-derivative norms of $\log \pi_0$ and $\log p(o\mid\cdot)$. (O5) Robust-qualitative downstream survives outside the Fisher-local regime by the general structure of Bayesian updating, not by this derivation.
- **Cross-reference to Paper 3 chart-rescaling no-go.** The (PI) dependence is forced by the chart-rescaling no-go on Euclidean chart norms (NeurIPS 2026 Paper 3, "How Much Can LLMs Hallucinate?", §4 Theorem 4.2 / `#thm-no-go`): outside (PI), no universal-constant claim survives. The natural-gradient direction inherits this forcing; the canonical-direction argument depends on (PI), not on (R) or (K) of the Markov-morphism triple. See `msc/neurips-back-integration-2026-05-08.md` §1 Paper 3 entry #3 and the source `~/src/neurips/03-llm-hallucinate-bound/`.
- **Landing context.** Landed in the 2026-05-12 audit-strengthening cycle (AAT-5); see CHANGELOG 2026-05-12. The load-bearing three-route convergence and boundary-admissibility content is in the Derivation and Discussion above; the originating spike is absorbed archaeology, not a live reference.

- **Downstream consumer at the persistence layer.** The matrix gain operator $K = (H_M + H_L)^{-1}H_L$ derived here is the per-channel primitive that `#def-adaptive-tempo`'s Tensor extension aggregates into $\mathcal{T} = \sum_k \nu^{(k)} K^{(k)}$. The persistence-layer consumer is the matrix-Loewner persistence condition in `#deriv-matrix-persistence-condition`: under matrix $\mathcal{T}$ and matrix disturbance $\Sigma_w$, the agent persists iff $\mathcal{T}$ is Hurwitz and the stationary covariance $\Sigma_\infty$ (solving $\mathcal{T}\Sigma_\infty + \Sigma_\infty\mathcal{T}^T = \Sigma_w$) is strictly Loewner-dominated by $D_\delta = \mathrm{diag}(\delta_{\text{critical},k}^2)$. The matrix-Loewner form is *strictly sharper* than per-coordinate: under cross-dimensional correction (off-diagonal $\mathcal{T}$ — the generic Fisher-local case when prior and likelihood do not share the coordinate basis), per-coordinate gives a false-pass while matrix-Loewner reads persistence correctly off the worst direction.


---

### Source: `deriv-matrix-persistence-condition.md`

```yaml
---
slug: deriv-matrix-persistence-condition
type: derivation
status: conditional
stage: draft
depends:
  - def-adaptive-tempo
  - def-mismatch-signal
  - deriv-fisher-local-update-gain
  - result-persistence-condition
  - result-per-dimension-persistence
  - result-sector-persistence-template
---
```


# Derivation: Matrix-Loewner Persistence Condition

Under matrix adaptive tempo $\mathcal{T}$ from `#def-adaptive-tempo`'s Tensor extension (per-channel primitive $K^{(k)} = (H_M + H_L^{(k)})^{-1} H_L^{(k)}$ from `#deriv-fisher-local-update-gain`) and matrix disturbance covariance $\Sigma_w$, the operational persistence condition lifts from scalar to matrix-Loewner form: the agent persists iff $\mathcal{T}$ is Hurwitz (structural persistence) and the stationary covariance $\Sigma_\infty$ — solving the continuous Lyapunov equation $\mathcal{T}\Sigma_\infty + \Sigma_\infty\mathcal{T}^T = \Sigma_w$ — is strictly Loewner-dominated by the diagonal of squared per-direction critical thresholds $D_\delta := \mathrm{diag}(\delta_{\text{critical},k}^2)$. The matrix-Loewner condition $\Sigma_\infty \prec D_\delta$ recovers `#result-persistence-condition`'s scalar Model S form as the isotropic special case and `#result-per-dimension-persistence`'s per-coordinate form as the diagonal special case. Crucially, when $\mathcal{T}$ has off-diagonal entries that misalign with the coordinate basis — the generic situation under cross-dimensional correction — the per-coordinate condition is *unsafe*: it can declare persistence on systems whose stationary mismatch will exceed task-adequacy along the diagonal direction. The matrix-Loewner form is the canonical anisotropic persistence condition; per-coordinate is its diagonal-$\mathcal{T}$-axis-aligned-$D_\delta$ special case, sharp where the coordinate basis happens to be the correction-machinery's eigenbasis and unsafe outside it.

## Formal Expression

### Setup — Model S with matrix correction

*[Definition (matrix-Model-S-mismatch-dynamics)]*

Consider linear stochastic mismatch dynamics

$$d\delta_t \;=\; -\mathcal{T}\, \delta_t \, dt \;+\; \Sigma_w^{1/2}\, dW_t$$

with $\delta_t \in \mathbb{R}^d$, matrix adaptive tempo $\mathcal{T} \in \mathbb{R}^{d \times d}$, disturbance covariance $\Sigma_w \succ 0$, and standard $d$-dimensional Brownian $W_t$. Per `#def-adaptive-tempo`'s Tensor extension, $\mathcal{T} = \sum_k \nu^{(k)} K^{(k)}$ aggregates the per-channel matrix gain operators from `#deriv-fisher-local-update-gain`.

### Stationary covariance — continuous Lyapunov equation

*[Derived (stationary-covariance, exact under Hurwitz $\mathcal{T}$ and $\Sigma_w \succ 0$)]*

The stationary distribution of the linear stochastic dynamics is Gaussian $\mathcal{N}(0, \Sigma_\infty)$, with $\Sigma_\infty$ the unique positive-definite solution of the **continuous Lyapunov equation**

$$\boxed{\;\mathcal{T}\, \Sigma_\infty \;+\; \Sigma_\infty\, \mathcal{T}^T \;=\; \Sigma_w.\;}$$

Existence and uniqueness of $\Sigma_\infty \succ 0$ are equivalent to $\mathcal{T}$ being **Hurwitz** — all eigenvalues having strictly positive real part. The closed-form integral representation is

$$\Sigma_\infty \;=\; \int_0^\infty e^{-\mathcal{T} t}\, \Sigma_w\, e^{-\mathcal{T}^T t}\, dt.$$

When $\mathcal{T}$ is symmetric and commutes with $\Sigma_w$, the solution simplifies to $\Sigma_\infty = \tfrac{1}{2}\mathcal{T}^{-1}\Sigma_w$. Otherwise the integral form (or any standard Lyapunov-equation solver) gives the stationary covariance.

### The matrix-Loewner persistence condition

*[Derived (matrix-persistence-loewner-Model-S)]*

The agent persists operationally iff:

**(MP-1) Structural persistence.** $\mathcal{T}$ is Hurwitz — equivalently, $\Sigma_\infty$ exists as the unique positive-definite solution of the Lyapunov equation. This is the matrix analog of `#result-persistence-condition`'s structural condition $\alpha \gt 0$ (Hurwitz reduces to $\mathcal T_0 \gt 0$ in the scalar case).

**(MP-2) Matrix-Loewner task adequacy.**

$$\boxed{\;\Sigma_\infty \;\prec\; D_\delta \;:=\; \mathrm{diag}\!\big(\delta_{\text{critical},k}^2\big)\;}$$

with $\prec$ the strict Loewner (positive-definite) order: $D_\delta - \Sigma_\infty \succ 0$. The stationary mismatch ellipsoid is contained strictly inside the per-direction critical-threshold ellipsoid.

The two conditions are independent in the same sense as `#result-persistence-condition`'s structural-vs-task-adequacy split: (MP-1) is a property of the correction machinery alone; (MP-2) adds the domain-specific bound on per-direction tolerable mismatch.

### Three equivalent restatements

The Loewner condition (MP-2) admits three equivalent forms:

**(MP-2a) Per-direction.** For every unit direction $\hat v \in \mathbb{R}^d$:

$$\hat v^T \Sigma_\infty \hat v \;\lt\; \hat v^T D_\delta \hat v \;=\; \sum_k v_k^2\, \delta_{\text{critical},k}^2.$$

The projected stationary variance along $\hat v$ must be less than the direction-projected squared threshold along the same direction.

**(MP-2b) Spectral.** The generalized eigenvalue problem $\Sigma_\infty x = \lambda D_\delta x$ satisfies $\lambda_{\max} \lt 1$, equivalently

$$\lambda_{\max}\!\big(D_\delta^{-1/2}\Sigma_\infty D_\delta^{-1/2}\big) \;\lt\; 1.$$

The principal eigenvector identifies the *worst direction*; the eigenvalue's distance from $1$ is the worst-direction safety margin.

**(MP-2c) Ellipsoid containment.** The stationary noise ellipsoid $\{x : x^T \Sigma_\infty^{-1} x \le 1\}$ is contained strictly inside the threshold ellipsoid $\{x : x^T D_\delta^{-1} x \le 1\}$.

The three are mathematically equivalent under standard matrix-analysis (Horn & Johnson 2013, §4.6 and §7). (MP-2a) is cleanest for hand reasoning, (MP-2b) for computation (single generalized-eigenvalue solve), (MP-2c) for geometric intuition.

### Recovery of existing AAT persistence forms

| Special case | (MP-2) reduces to | Matches |
|---|---|---|
| Isotropic ($\mathcal{T} = \mathcal T_0 I$, $\Sigma_w = \sigma_w^2 I$, $\delta_{\text{critical}} = \delta_0 \mathbf{1}$) | $\sigma_w^2 / (2\mathcal T_0) \lt \delta_0^2$, i.e., $\mathcal T_0 \gt \sigma_w^2 / (2\delta_0^2)$ | Scalar Model S form, `#result-persistence-condition` |
| Diagonal $\mathcal{T}, \Sigma_w$ in the coordinate basis of $D_\delta$ | $\sigma_{w,k}^2 / (2\mathcal T_{kk}) \lt \delta_{\text{critical},k}^2$ per coordinate $k$ | Per-coordinate Model S RMS, `#result-per-dimension-persistence` |
| Symmetric $\mathcal{T}$ commuting with $\Sigma_w$, general $D_\delta$ | Per-eigendirection inequality in $\mathcal{T}$'s eigenbasis, with direction-projected thresholds | New content recovered from the matrix form — extends per-coordinate to non-axis-aligned $\mathcal{T}$ |

The third row is the content `#result-per-dimension-persistence` does not currently carry: when $\mathcal{T}$ and $\Sigma_w$ share an eigenbasis that is *not* the coordinate basis of $D_\delta$, the per-coordinate form misses the right direction-projected thresholds and the matrix-Loewner form handles them correctly.

### Where per-coordinate is unsafe — a constructive counterexample

The deeper structural question: is the matrix-Loewner form merely a generalization that agrees with per-coordinate in all real cases, or is it *strictly sharper* — does there exist a regime where per-coordinate says PASS but matrix-Loewner correctly says FAIL? The construction below establishes the latter: the per-coordinate form is **unsafe** under cross-dimensional correction.

**Construction.** Take $d = 2$, $\Sigma_w = I$, and

$$\mathcal{T} \;=\; \begin{pmatrix} 1 & -0.9 \\ -0.9 & 1 \end{pmatrix}.$$

This $\mathcal{T}$ is symmetric positive-definite with eigenvalues $1.9$ (along $(1, -1)/\sqrt{2}$) and $0.1$ (along $(1, 1)/\sqrt{2}$) — strongly anisotropic correction, with the $(1, 1)$ direction the weak axis. Per-coordinate naive reading of "diagonal of $\mathcal{T}$" sees uniform $\mathcal T_{11} = \mathcal T_{22} = 1$ and concludes correction is uniform at rate $1$ on each coordinate.

**Stationary covariance.** Since $\mathcal{T}$ is symmetric, $\Sigma_\infty = \tfrac{1}{2}\mathcal{T}^{-1}\Sigma_w = \tfrac{1}{2}\mathcal{T}^{-1}$. Direct computation:

$$\Sigma_\infty \;=\; \frac{1}{0.38}\begin{pmatrix} 1 & 0.9 \\ 0.9 & 1 \end{pmatrix} \;\approx\; \begin{pmatrix} 2.63 & 2.37 \\ 2.37 & 2.63 \end{pmatrix},$$

with eigenvalues $5.00$ along $(1, 1)/\sqrt{2}$ and $0.26$ along $(1, -1)/\sqrt{2}$.

**Set $\delta_{\text{critical}} = (1.7, 1.7)$**, so $D_\delta = 2.89\, I$.

- *Per-coordinate check (`#result-per-dimension-persistence` form):* per-coordinate stationary variance is $\Sigma_{\infty,kk} = 2.63 \lt 2.89 = \delta_{\text{critical},k}^2$ for each $k$. **Per-coordinate says PASS.** ✓
- *Matrix-Loewner check (MP-2 here):* worst-direction projected variance is $\lambda_{\max}(\Sigma_\infty) = 5.00$ along $(1, 1)/\sqrt{2}$. Direction-projected squared threshold along the same direction is $\hat v^T D_\delta \hat v = 2.89$. The condition $5.00 \lt 2.89$ fails. Equivalently, $\lambda_{\max}(D_\delta^{-1/2}\Sigma_\infty D_\delta^{-1/2}) = 5.00 / 2.89 \approx 1.73 \gt 1$. **Matrix-Loewner says FAIL.** ✗

**Conclusion.** Per-coordinate gives a false-pass. The agent will routinely produce mismatch vectors with RMS magnitude $\sqrt{5.00} = 2.24$ along the $(1, 1)/\sqrt{2}$ direction, exceeding the direction-projected threshold of $\sqrt{2.89} = 1.70$ on that direction. The per-coordinate analysis missed the diagonal direction because each coordinate alone stays within $\delta_{\text{critical},k} = 1.7$ — the failure is *only* visible at the matrix-Loewner level. Cross-dimensional correction (the off-diagonal entries of $\mathcal{T}$) is what creates the diagonal-direction concentration that per-coordinate cannot detect.

## Epistemic Status

*Conditional.* Max attainable: *exact* under (i) Model S linear stochastic dynamics, (ii) Hurwitz matrix tempo $\mathcal{T}$, (iii) positive-definite disturbance covariance $\Sigma_w$, (iv) diagonal critical-threshold structure $D_\delta = \mathrm{diag}(\delta_{\text{critical},k}^2)$. The Lyapunov equation, the existence-iff-Hurwitz fact, and the matrix-Loewner equivalence forms are all standard from Bellman 1960 / Khalil 2002 / Horn-Johnson 2013; the AAT-distinctive content is the application to the persistence condition and the recognition that per-coordinate is strictly sharper-or-unsafe rather than uniformly sharper.

**What is load-bearing:**

- The matrix-Loewner form as the canonical anisotropic persistence condition, with scalar and per-coordinate forms as special cases recovered exactly.
- The strict-sharpness result via the §4 counterexample: per-coordinate gives a false-pass when $\mathcal{T}$ has off-diagonal entries that misalign with the coordinate basis. The per-coordinate form is not merely incomplete in this regime — it is unsafe.
- The three equivalent restatements (per-direction, spectral, ellipsoid-containment) with their different operational readings.
- The structural-vs-task-adequacy decomposition from `#result-persistence-condition` transfers directly: (MP-1) is the matrix structural condition (Hurwitz); (MP-2) is the matrix task adequacy (Loewner $\Sigma_\infty \prec D_\delta$). The two conditions remain independent — Hurwitz $\mathcal{T}$ does not imply $\Sigma_\infty \prec D_\delta$ for any particular $D_\delta$, and conversely.

**What is not established here:**

- The nonlinear matrix-sector extension. Under sector-bounded $F(\mathcal{T}, \delta)$ with $\delta^T F \succeq \alpha I$ in matrix-Loewner form, the matrix-Lyapunov machinery extends to give an ultimate-bound matrix; the linear case here is the template instantiation. Full matrix-sector treatment is follow-on work in `#deriv-sector-condition`.
- The Model D matrix lift. Under deterministic bounded disturbance $\Vertw_t\Vert_M \le \rho$ in a quadratic norm, the ultimate-bound becomes an ellipsoid containment problem (a linear matrix inequality). Mechanical lift; not derived here.
- The non-Hurwitz boundary behaviour (eigenvalue exactly on the imaginary axis). Outside Hurwitz, the linear analysis fails — no stationary distribution. This matches the scalar case's $\alpha \gt 0$ requirement.
- The promotion of `#result-adversarial-tempo-advantage` to matrix form. The matrix-Loewner form sharpens the adversarial result via worst-direction targeting (an adversary controlling $\Sigma_w^{\text{adv}}$ maximizes $\lambda_{\max}(D_\delta^{-1/2}\Sigma_w^{\text{adv}} \mathcal T_{\text{eff}}^{-1} D_\delta^{-1/2})$), but the full adversarial promotion is a separate cycle.
- The matrix extension of `#deriv-persistence-cost`'s information-rate floor. The natural lift is $\dot R \ge \tfrac{1}{2}\mathrm{Tr}(\mathcal{T})$ — per-eigendirection application of the scalar derivation. Worth a cross-reference Working Note in that segment if it becomes load-bearing; not derived here.

## Discussion

**Why the Loewner form is the natural matrix lift.** The Lyapunov equation $\mathcal{T}\Sigma_\infty + \Sigma_\infty\mathcal{T}^T = \Sigma_w$ is itself a matrix-Loewner statement: it says $\Sigma_\infty$ balances correction (via $\mathcal{T}$) against disturbance (via $\Sigma_w$) in the PSD ordering. The task-adequacy condition $\Sigma_\infty \prec D_\delta$ reads this balance against the threshold ellipsoid. The whole structure lives in the cone of positive-semidefinite matrices ordered by Loewner dominance; scalar persistence is its 1D shadow, per-coordinate persistence is its axis-aligned-diagonal shadow, and the matrix form is the load-bearing object the shadows project from.

**The structural-vs-task-adequacy decomposition transfers.** `#result-persistence-condition`'s split — structural persistence (machinery works) vs task adequacy (machinery works well enough) — survives intact in the matrix lift: Hurwitz $\mathcal{T}$ is the matrix structural condition; Loewner $\Sigma_\infty \prec D_\delta$ is the matrix task-adequacy condition. The two are independent; an agent can have Hurwitz $\mathcal{T}$ (correction works in every direction) but fail Loewner on the worst direction (correction is not fast enough on the weak axis for the per-direction threshold). The remedies are different: structural failure requires changing the correction architecture (`#result-structural-adaptation-necessity`); task-adequacy failure requires either increasing $\mathcal{T}$ on the weak direction, decreasing $\Sigma_w$ on the weak direction, or relaxing the threshold along that direction.

**The weak-direction-bottleneck argument transfers and sharpens.** `#result-per-dimension-persistence`'s key insight — the weak dimension is the bottleneck — generalizes to the weak *direction* in the matrix lift: the worst eigenvector of $\Sigma_\infty$ relative to $D_\delta$ is what gates persistence. When this eigenvector aligns with a coordinate axis, the per-coordinate analysis catches it. When it points off-axis — the generic situation under cross-dimensional correction — the per-coordinate analysis misses it. The §4 counterexample is the canonical illustration: the worst direction is $(1, 1)/\sqrt{2}$, off-axis from both coordinate directions; per-coordinate evaluates the wrong directions; matrix-Loewner evaluates the right ones.

**Cross-coordinate correction is the generic case under Fisher-local invariance.** The matrix gain operator $K = (H_M + H_L)^{-1} H_L$ from `#deriv-fisher-local-update-gain` is diagonal in the coordinate basis only when prior precision $H_M$ and observation Fisher $H_L$ share an eigenbasis aligned with the coordinate axes. In general — and certainly in the natural-gradient regime where the agent's parameterization is statistical-manifold-natural rather than user-chosen — they do not, and $K$ has off-diagonal entries. The matrix-Loewner condition becomes the canonical form for any Fisher-local-derived persistence analysis; the per-coordinate form is the exceptional case where prior, likelihood, and threshold all happen to share the coordinate axes.

**Cross-reference to existing AAT machinery.** The matrix-Loewner form composes with:

- `#result-sector-persistence-template` (T1)–(T3) as the linear-case template instantiation; the matrix sector inequality $\delta^T F + F^T \delta \succeq 2\alpha I$ would extend the matrix-Lyapunov result to nonlinear $F$ via the template's (T2) condition lifted to matrix form.
- `#deriv-sector-condition` Prop A.1S (the Lyapunov-stochastic derivation underlying `#result-persistence-condition`'s scalar form) — the matrix derivation here is the analog at the matrix-Lyapunov level.
- `#deriv-fisher-local-update-gain` (matrix gain $K$ as the per-channel primitive) and `#def-adaptive-tempo` (Tensor extension aggregating $\mathcal{T} = \sum_k \nu^{(k)} K^{(k)}$).

**On the scope tag downstream.** Until the broader promotion of `#result-persistence-condition`, `#result-adversarial-tempo-advantage`, `#form-composition-closure`, `#der-team-persistence`, `#deriv-critical-mass-composition` to invoke the matrix form directly, those segments continue to read scalar and inherit the "scalar / isotropic / nonredundant-channel scope" tag from `#def-adaptive-tempo`'s Epistemic Status. The per-direction primitive is in place; the downstream promotion is a follow-on cycle in `TODO.md`.

## Working Notes

- **Counterexample as load-bearing content.** Section 4's $\mathcal{T} = \begin{pmatrix}1 & -0.9 \\ -0.9 & 1\end{pmatrix}$ example is the segment's strongest content — it shifts the matrix-Loewner form from "interesting generalization" to "the safe condition; per-coordinate is unsafe under cross-dimensional correction." The example uses the smallest nontrivial dimension ($d = 2$), the simplest non-diagonal symmetric $\mathcal{T}$ structure, and isotropic disturbance / threshold parameters. Generalizations to $d \gt 2$, asymmetric $\mathcal{T}$, and anisotropic $\Sigma_w / D_\delta$ are mechanical; the qualitative phenomenon (off-diagonal correction → diagonal-direction variance concentration → per-coordinate false-pass) is robust.
- **Empirical validation.** A 2D simulation matching the §4 parameters would confirm the predicted false-pass behaviour of per-coordinate: run the linear SDE with $\mathcal{T}, \Sigma_w$ from §4 for $N$ steps; observe that the per-coordinate marginals stay within $\pm 1.7$ most of the time (per-coordinate "passes") while the diagonal-direction projection routinely exceeds $\pm 1.7$ (matrix-Loewner "fails"). Mechanical simulation; would land cleanly under `obs-section-i-validation-simulations` as a new variant.
- **Open work — nonlinear matrix-sector.** The matrix-Loewner form is derived for linear correction. The nonlinear matrix-sector lift would replace the Lyapunov equation with the matrix-sector inequality $F(\delta) + F(\delta)^T \succeq 2\alpha \delta\delta^T / \Vert\delta\Vert^2$ (or a matrix-sector form derived from a quadratic Lyapunov function). Composes with `#deriv-sector-condition`'s nonlinear scalar machinery via the matrix template; not derived here.
- **Open work — adversarial extension.** The adversarial advantage exponent in `#result-adversarial-tempo-advantage` lifts to a matrix-eigenvalue-ratio exponent: an adversary controlling $\Sigma_w^{\text{adv}}$ maximizes the bad-direction stationary variance via the matrix-Loewner form. Worth a follow-on derivation if `#result-adversarial-tempo-advantage` is promoted to matrix form.
- **Open work — composition lift.** Composite stationary covariance $\Sigma_\infty^c$ solves the Lyapunov equation with composite $\mathcal{T}^c$ and $\Sigma_w^c$ (aggregated from sub-agents); composite Loewner condition $\Sigma_\infty^c \prec D_\delta^c$ governs composite persistence. Promoting `#form-composition-closure`, `#der-team-persistence`, and `#deriv-critical-mass-composition` to invoke the matrix form is the natural next AAT-1 follow-on cycle.
- **Landing context.** Landed in the 2026-05-12 AAT-1 follow-on cycle (matrix-Loewner persistence, succeed-beyond-claim); see CHANGELOG 2026-05-12 (late). The load-bearing derivation and counterexample are above; the follow-on extensions (Model D matrix lift, adaptive-gain matrix dynamics, variational matrix form) are flagged in the "Open work" notes here and in TODO. Originating spike is absorbed archaeology, not a live reference.


---

