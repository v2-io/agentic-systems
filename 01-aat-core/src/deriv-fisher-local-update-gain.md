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

# Derivation: Fisher-Local Update Gain

Under the **Fisher-local invariance regime** — smooth log-likelihood admitting non-degenerate local quadratic expansion at the current model parameter, with single-step update at first order in the step size — the natural-gradient Bayesian posterior mean shift has the form $\Delta\theta = K \cdot \tilde\nabla$ with **gain operator** $K = (H_M + H_L)^{-1} H_L$ and **scalar collapse** $\eta^\ast = U_M/(U_M + U_o)$ along the natural-gradient direction in the commuting / shared-eigenbasis case (always in 1-D; under (PI)/Čencov in the natural-gradient direction in higher dimensions). The result derives the form `#emp-update-gain` carries as an empirical claim, places it in the Fisher-local regime as exact, and recovers linear-Gaussian (Kalman) and conjugate-Bayesian instances as cases where the local quadratic expansion is globally exact. Companion at the model-parameter-update layer to `#deriv-fisher-whitened-update-rule`'s edge-update derivation: that segment derives update *direction* under correlated evidence; this segment derives update *magnitude* under the Fisher-local regime. Both share the (PI) parameterization-invariance axiom from `#scope-agent-identity` and Čencov 1982 uniqueness as AAD-internal forcing for the Fisher metric.

## Formal Expression

### Setup — Fisher-local quadratic regime

*[Definition (Fisher-local regime, conditions (R1)–(R3))]*

Let $\theta \in \mathbb R^d$ parameterize the agent's model and $\theta_t$ be the current point estimate (mode of the prior $\pi_0$, or center of expansion). Three regime conditions:

- **(R1) Smooth log-likelihood admitting non-degenerate local quadratic expansion.** $\log \pi_0$ and $\log p(o \mid \cdot)$ are $C^3$ in a neighborhood of $\theta_t$, with prior precision $H_M := -\nabla^2 \log \pi_0(\theta_t)$ and observed information $H_L := -\nabla^2 \log p(o \mid \theta) \big|_{\theta_t}$ satisfying $H_M + H_L \succ 0$ (joint positive-definiteness; see §"Boundary admissibility" for why this is weaker than $H_M \succ 0$ and $H_L \succ 0$ both).
- **(R2) First-order-in-step-size regime.** The posterior update $\Delta\theta = \theta_{t+1} - \theta_t$ is small enough that $O(\lVert\Delta\theta\rVert^3)$ terms in the quadratic expansion are negligible compared to the quadratic terms.
- **(R3) Bayesian-coherent update.** $\theta_{t+1}$ is taken to be a coordinate of the posterior $p(\theta \mid o) \propto \pi_0(\theta) \cdot p(o \mid \theta)$ — mean, mode, or natural-parameter (they coincide for Gaussian posteriors, which is what the quadratic expansion produces).

Under (R1)–(R3), the local log-posterior is

$$\log p(\theta \mid o) = \mathrm{const} + s^T(\theta - \theta_t) - \tfrac{1}{2}(\theta - \theta_t)^T (H_M + H_L)(\theta - \theta_t) + O(\lVert\theta - \theta_t\rVert^3),$$

where $s := \nabla_\theta \log p(o \mid \theta) \big|_{\theta_t}$ is the score. The posterior is approximately $\mathcal N(\theta^\star, (H_M + H_L)^{-1})$ with mean shift

*[Derived (posterior-mean-shift)]*

$$\theta^\star - \theta_t = (H_M + H_L)^{-1} s.$$

The AAD-vocabulary correspondences are

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

*Conditional.* Max attainable: *exact* under (R1)–(R3) + (PI) parameterization-invariance from `#scope-agent-identity`. Under (PI) and Čencov 1982 uniqueness, the Fisher metric is the AAD-internally canonical metric on the statistical manifold (the 4th primary instance of `#disc-additive-coordinate-forcing`); the natural-gradient direction is therefore the AAD-internally canonical reference direction along which $\eta^\ast$ reads as $U_M/(U_M + U_o)$. The textbook information-geometry result (Amari 1998 natural-gradient invariance theorem) is imported; the (PI)/Čencov forcing in `#deriv-fisher-whitened-update-rule`'s Path A makes the import AAD-internal.

Linear-Gaussian (Kalman) and conjugate-Bayesian instances are cases where the local quadratic expansion is *globally* exact, so $\eta^\ast = U_M/(U_M + U_o)$ holds without truncation error.

Outside the Fisher-local regime — heavy-tailed posteriors (no second moment), structurally non-smooth likelihoods, multimodal uncertainty where the local quadratic misrepresents global structure — the quantitative form is *not* derived here. The *qualitative* direction (gain rises with model uncertainty, falls with observation noise) is preserved as *robust qualitative* from `#emp-update-gain`'s broader empirical scope; the first-order form is recovered locally; what need not hold is global quantitative fidelity.

This segment depends on (PI) from `#scope-agent-identity` only. The triple (PI)+(R)+(K) of the Markov-morphism layer (carried by the Fisher-Rao bias-bound machinery; the (R) Riemannian-structure and (K) KL-second-order-matching axioms are stronger) is *not* invoked here. If (R) and (K) are asserted at the scope-level in a future cycle, this segment's status remains conditional on (PI) alone unless explicitly extended.

## Discussion

**Why read $\eta^\ast$ off the natural-gradient direction.** The Bayesian-coherent posterior mean shift $\Delta\theta = (H_M + H_L)^{-1} s$ is a fixed vector; its decomposition into "gain times reference direction" depends on the choice of reference direction. Two natural choices give two faces of the same shift:

- **Natural-gradient direction $\tilde\nabla = H_L^{-1} s$.** Coefficient: $\eta^\ast_{\text{NG}} = H_L/(H_M + H_L) = U_M/(U_M + U_o)$. *AAD-internally canonical* under (PI)/Čencov — the Fisher metric is the unique Markov-invariant metric, so the natural gradient is the unique coordinate-invariant gradient direction (Čencov 1982; extended by Ay-Jost-Lê-Schwachhöfer 2017).
- **Prior-curvature-rescaled direction $H_M^{-1} s$.** Coefficient: $\eta^\star_{\text{prior}} = H_M/(H_M + H_L) = U_o/(U_M + U_o)$. The *complement*; the same algebraic decomposition arises in Kalman literature as the prior weight in the convex combination "posterior = (1-K) prior + K observation."

The two coefficients are duals on the same posterior shift; their product reduces to the posterior covariance $(H_M + H_L)^{-1}$. AAD names the natural-gradient coefficient as the canonical $\eta^\ast$ because (PI)/Čencov picks out the natural-gradient direction as the unique coordinate-invariant choice.

**Three derivation routes converge.** The same scalar $\eta^\ast = U_M/(U_M + U_o)$ falls out of three independent structural derivations:

| Route | Lever | Surface meaning of $\eta^\ast$ |
|---|---|---|
| Local-Gaussian Laplace expansion (§Setup–Gain decomposition above) | Algebraic completion of squares on additive log-posterior quadratics | Posterior mean shift coefficient on the natural-gradient direction |
| Bregman / KL projection onto the local tangent plane | First-order condition on the variational free energy along natural-gradient tilt | Projection coefficient of the posterior onto the local tangent plane (Pythagorean projection in Fisher metric per Amari-Nagaoka 2000 §3.2) |
| Cramér-Rao / inverse-Fisher | Precision-additive composition $1/U_M + 1/U_o$, inverted | Fractional observation contribution to posterior precision |

The agreement is not coincidence: the Fisher-local regime *is* the regime where prior and likelihood compose as a Pythagorean projection in the Fisher metric — the same exponential-family / Bregman / Pythagorean structure underlying `#deriv-strategy-cost-regret-bound`'s ρ-decomposition. The three routes are three faces of one geometric object: precision-additive composition of two Gaussian information sources, read off the natural-gradient direction.

**Sibling positioning vs `#deriv-fisher-whitened-update-rule`.** That segment lives at the **edge-update layer** of Section II's strategy DAG: it derives the Fisher-whitening correction for the *direction* of edge updates under correlated evidence (L1'/L2). This segment lives at the **model-parameter-update layer** of Section I: it derives the *magnitude* of the natural-gradient Bayesian update via the Fisher-local invariance regime. Both depend on (PI) + Čencov as the AAD-internal axiom forcing the Fisher metric. Together they make the Fisher-local invariance regime AAD-internally complete: direction (whitening) at the edge layer and magnitude (gain) at the model-parameter layer are both derived from the same axiomatic chain.

**Special case of `#deriv-adaptive-gain-dynamics`' meta-gain framework.** The gain operator $K = (H_M + H_L)^{-1} H_L$ is a *deterministic function of the current state* — it depends on the prior covariance $H_M^{-1}$ (part of the agent's $M_t$ state) and on the observation Fisher $H_L$ (depends on $\theta_t$ and $o$). It is therefore the **deterministic-meta-gain** special case of `#deriv-adaptive-gain-dynamics`' (MG-1)–(MG-4) machinery: the meta-gain is determined by the primary state rather than independently learned. All four meta-gain conditions are satisfied trivially (symmetric-positive-definite $K$ on the interior; smoothness for exponential families; bounded primary-meta coupling). Resolving the epistemic-opacity question that `#def-observation-function` axiomatizes — i.e., the agent does not know $U_o$ a priori and must estimate it from its own mismatch sequence — is one level up: it adds the Mehra-style meta-channel that `#deriv-adaptive-gain-dynamics` treats as its primary instance.

**Downstream tempo and persistence machinery.** `#emp-update-gain`'s Discussion §"Connection to adaptive tempo" names $\mathcal T = \nu \cdot \eta^\ast$. The derivation here promotes $\eta^\ast$'s tier from `empirical / robust-qualitative` (over the cross-domain validity tail — RL, PID, software-developer) to `derived (conditional on Fisher-local regime)` for the Kalman / conjugate / natural-gradient core. The tempo product $\mathcal T = \nu \cdot \eta^\ast$ inherits the regime distinction directly; the persistence-condition machinery (`#result-persistence-condition`, `#result-sector-condition-stability`) and the adaptive-tempo / aporia diagnostics (`#def-adaptive-tempo`, `#def-aporia`) all gain the tighter $\eta^\ast$ exactness statement in their Fisher-local instances. The qualitative direction claim and the failure-mode framing (gain-collapse → epistrophe failure) survive unchanged outside the Fisher-local regime.

**Tensor adaptive tempo connection.** The matrix gain operator $K$ is the per-coordinate primitive for tensor-valued adaptive tempo: $\mathcal T = \nu \cdot K$ as a matrix product, with the existing scalar $\mathcal T = \nu \cdot \eta^\ast$ recovered in the shared-eigenbasis limit. See `#def-adaptive-tempo`'s Tensor extension.

## Working Notes

- **Multi-step extrapolation rate.** The Fisher-local exactness is a one-step statement. Iterating over many observations accumulates higher-order curvature error in the non-Gaussian / non-conjugate case. Bernstein-von Mises asymptotics (van der Vaart 1998 §10.2) give a $1/\sqrt n$ posterior concentration rate; whether $\eta^\ast$'s exactness inherits a matching $1/\sqrt n$ degradation outside Kalman / conjugate is an open quantitative-rate question. Open spike candidate.
- **Edgeworth higher-order correction.** The $O(\lVert\Delta\theta\rVert^3)$ correction to $\eta^\ast$ in terms of third / fourth derivatives of the log-likelihood admits a standard Edgeworth-expansion treatment. Worth a follow-up spike if it becomes load-bearing for any AAD use case.
- **Variational-bound extension.** Under variational approximation $\mathrm{KL}(q \| p) \leq \varepsilon$, the gain inherits a Pinsker-tight degradation factor analogous to `#deriv-variational-sector-condition`'s $O(\sqrt\varepsilon)$ B1 degradation. Composing this with the derivation gives $\eta^\ast$ in sub-scope $\alpha'$ under approximate-posterior agents.
- **Multimodal posteriors.** When the prior or posterior is multimodal, the local-quadratic expansion around any one mode misses the global structure. Two natural moves: per-mode $U_M/(U_M + U_o)$ with mode-mixture weights as a separate state; or accept the qualitative direction claim only. Worth a follow-up spike if multimodal posteriors become load-bearing.
- **Consolidation / replay connection.** `#form-consolidation-dynamics`-style between-event consolidation drives $U_M$ up (model uncertainty grows under offline replay via IB-gap reduction). The next online observation gets up-weighted because $U_M/(U_M + U_o)$ rises with $U_M$. This is the formal connection between consolidation-induced uncertainty growth and increased online responsiveness — worth tightening into a result if `#form-consolidation-dynamics` lands a quantitative form.
- **Honest obstructions.** (O1) The natural-gradient invariance theorem (Amari 1998) is imported, not derived; the (PI)/Čencov forcing in `#deriv-fisher-whitened-update-rule`'s Path A makes the import AAD-internal. Without (PI), the natural-gradient direction is a chosen-not-forced direction and the derivation degrades to "the form on the chosen direction." (O2) Single-observation per-step setup; multi-observation batches generalize mechanically ($H_L = \sum_i H_{L,i}$ for independent observations). (O3) Matrix vs scalar — the matrix $K$ is the natural object; the scalar $U_M/(U_M + U_o)$ is its eigenvalue in the commuting / 1-D / shared-eigenbasis case. (O4) Step-size boundary qualitative; the actual Fisher-local cutoff depends on the third-derivative norms of $\log \pi_0$ and $\log p(o\mid\cdot)$. (O5) Robust-qualitative downstream survives outside the Fisher-local regime by the general structure of Bayesian updating, not by this derivation.
- **Cross-reference to Paper 3 chart-rescaling no-go.** The (PI) dependence is forced by the chart-rescaling no-go on Euclidean chart norms (NeurIPS 2026 Paper 3, "How Much Can LLMs Hallucinate?", §4 Theorem 4.2 / `#thm-no-go`): outside (PI), no universal-constant claim survives. The natural-gradient direction inherits this forcing; the canonical-direction argument depends on (PI), not on (R) or (K) of the Markov-morphism triple. See `msc/neurips-back-integration-2026-05-08.md` §1 Paper 3 entry #3 and the source `~/src/neurips/03-llm-hallucinate-bound/`.
- **Landing context.** Landed in the 2026-05-12 audit-strengthening cycle (AAD-5); see CHANGELOG 2026-05-12. The load-bearing three-route convergence and boundary-admissibility content is in the Derivation and Discussion above; the originating spike is absorbed archaeology, not a live reference.

- **Downstream consumer at the persistence layer.** The matrix gain operator $K = (H_M + H_L)^{-1}H_L$ derived here is the per-channel primitive that `#def-adaptive-tempo`'s Tensor extension aggregates into $\mathcal{T} = \sum_k \nu^{(k)} K^{(k)}$. The persistence-layer consumer is the matrix-Loewner persistence condition in `#deriv-matrix-persistence-condition`: under matrix $\mathcal{T}$ and matrix disturbance $\Sigma_w$, the agent persists iff $\mathcal{T}$ is Hurwitz and the stationary covariance $\Sigma_\infty$ (solving $\mathcal{T}\Sigma_\infty + \Sigma_\infty\mathcal{T}^T = \Sigma_w$) is strictly Loewner-dominated by $D_\delta = \mathrm{diag}(\delta_{\text{critical},k}^2)$. The matrix-Loewner form is *strictly sharper* than per-coordinate: under cross-dimensional correction (off-diagonal $\mathcal{T}$ — the generic Fisher-local case when prior and likelihood do not share the coordinate basis), per-coordinate gives a false-pass while matrix-Loewner reads persistence correctly off the worst direction.
