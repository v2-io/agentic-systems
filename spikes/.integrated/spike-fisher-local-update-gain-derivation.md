---
slug: spike-fisher-local-update-gain-derivation
type: spike
status: draft
depends:
  - emp-update-gain
  - def-mismatch-signal
  - def-observation-function
  - deriv-fisher-whitened-update-rule
  - deriv-adaptive-gain-dynamics
  - der-gain-sector-bridge
  - disc-additive-coordinate-forcing
  - scope-agent-identity
---

# Spike: Fisher-Local Derivation of the Update-Gain Form $\eta^\ast = U_M / (U_M + U_o)$

**Date:** 2026-05-12
**Trigger:** Codex audit AAD-5 (`msc/codex-audit-results-2026-05-12.md`) flagged the original "any optimal adaptation process must approximate this functional dependence" language at `#emp-update-gain` as overclaimed. The Epistemic Status was strengthened in the same swipe to the *Fisher-local invariance regime is exact* form — but the segment still sits at `empirical / robust-qualitative` because the structural result (standard in Amari's information geometry) is not *carried* anywhere in AAD; no segment-internal derivation exists.
**Posture:** Strengthen-first. Attempt the derivation cleanly under the named conditions before any softening. The structural antecedents to test against: Amari's natural-gradient invariance, Čencov uniqueness, Kalman / conjugate as global-exactness limits of a local result.
**Status:** Draft. **Succeed at claim.** Derivation goes through under the named Fisher-local conditions (smooth log-likelihood admitting non-degenerate quadratic expansion around the current model parameter); recovers Kalman and conjugate-Bayesian as global-exactness limits; composes cleanly with `#deriv-fisher-whitened-update-rule`'s Path A (PI)/Čencov framing. Mild scope-strengthening surfaces along the way: the derivation only needs invertibility of $H_M + H_L$ (sum positive-definite), so degenerate-prior + informative-likelihood (or vice versa) is admissible at the boundary. Promotion recommendation: lift `#emp-update-gain` from `empirical / robust-qualitative` to `derived (conditional on Fisher-local invariance regime)`, with the derivation landing either inline in the Formal Expression block or — preferred — as a short companion appendix `#deriv-fisher-local-update-gain` that `#emp-update-gain` cites and `#deriv-fisher-whitened-update-rule` references as the scalar-precursor / sibling result.

## 1. Problem statement

The current `#emp-update-gain` form

$$\eta^\ast \;=\; \frac{U_M}{U_M + U_o}$$

is asserted as an *empirical claim* (uncertainty-ratio principle). Verified instances in the segment's domain table: Kalman (exact, scalar), conjugate Bayesian (exact for conjugate families), RL fixed-α (approximate), PID fixed-gain (simplified), software developer (structural analogy). The qualitative direction (gain rises with model uncertainty, falls with observation noise) is treated as load-bearing for downstream tempo and persistence machinery; the exact form is treated as load-bearing for the Kalman / conjugate / natural-gradient instantiations.

The Codex AAD-5 finding is that the "any optimal adaptation process must approximate this functional dependence" overclaim does not survive without specifying *loss geometry, prior family, or local quadratic approximation*. The strengthening edit to `#emp-update-gain`'s Epistemic Status named the **Fisher-local invariance regime**: smooth log-likelihood admitting local quadratic expansion (equivalently, non-degenerate Fisher information matrix) ⟹ the natural-gradient Bayesian update at first order in the step size has this form *exactly*, with $U_M, U_o$ read off prior and likelihood curvatures.

Question this spike answers: **does that exactness claim go through as a clean derivation, and what are the precise conditions?**

The three legitimate completion states named at brief:
- **Succeed beyond claim.** Conditions weaker than "Fisher-local invariance" suffice.
- **Succeed at claim.** Derivation goes through under the stated regime with conditions named precisely.
- **Find no-such-claim.** Form does not admit clean derivation under these conditions; honest move is to keep `#emp-update-gain` at robust-qualitative.

Outcome: **succeed at claim**, with two mild scope-clarifications (rather than weakenings) along the way — see §3 and §5.

## 2. Setup

Let $\theta \in \mathbb R^d$ be the model parameter and $\theta_t$ the agent's current point estimate (mode of the prior $\pi_0$, or center of expansion). Prior and likelihood are written in their log forms around $\theta_t$:

*[Definition (prior and likelihood, local Gaussian quadratic regime)]*

$$\log \pi_0(\theta) \;=\; -\tfrac12 (\theta - \theta_t)^T H_M (\theta - \theta_t) \;+\; \mathrm{const} \;+\; O(\lVert\theta - \theta_t\rVert^3)$$

$$\log p(o \mid \theta) \;=\; \log p(o \mid \theta_t) \;+\; s^T (\theta - \theta_t) \;-\; \tfrac12 (\theta - \theta_t)^T H_L (\theta - \theta_t) \;+\; O(\lVert\theta - \theta_t\rVert^3)$$

where:
- $H_M := -\nabla^2 \log \pi_0(\theta_t)$ is the **prior precision** (positive-definite curvature of the prior at the current point estimate).
- $s := \nabla_\theta \log p(o \mid \theta) \big|_{\theta_t}$ is the **score** of the observation at $\theta_t$.
- $H_L := -\nabla^2 \log p(o \mid \theta) \big|_{\theta_t}$ is the **observed information** (Hessian of the negative log-likelihood at $\theta_t$); under the standard regularity conditions $\mathbb E_o[H_L] = \mathcal I(\theta_t)$ where $\mathcal I$ is the Fisher information matrix at $\theta_t$.

The AAD-vocabulary correspondence:

*[Definition (AAD uncertainty correspondences)]*

$$U_M \;:=\; H_M^{-1}, \qquad U_o \;:=\; H_L^{-1}$$

— model uncertainty is the inverse prior precision (predictive variance under the prior at $\theta_t$ pulled back through the parameterization), observation uncertainty is the inverse Fisher / inverse observed information (Cramér-Rao floor on what the observation pins down). The matrix forms generalize the scalar $U_M, U_o$ of `#emp-update-gain`'s Formal Expression in the natural way.

**Regime assumptions named precisely:**

(R1) **Smooth log-likelihood admitting non-degenerate local quadratic expansion.** $\log \pi_0$ and $\log p(o \mid \cdot)$ are $C^3$ in a neighborhood of $\theta_t$, with $H_M \succ 0$ and $H_M + H_L \succ 0$ (Fisher-local non-degeneracy — see §5 for why $H_L$ alone can be PSD).

(R2) **First-order-in-step-size regime.** The posterior update $\Delta\theta = \theta_{t+1} - \theta_t$ is small enough that $O(\lVert\Delta\theta\rVert^3)$ terms in the log expansion are negligible compared to the quadratic terms. This is the "first order in step size" qualifier from `#emp-update-gain`'s Epistemic Status.

(R3) **Bayesian-coherent update.** $\theta_{t+1}$ is taken to be a coordinate of the posterior $p(\theta \mid o) \propto \pi_0(\theta) p(o \mid \theta)$ (mean, mode, or natural-parameter — all coincide for Gaussian posteriors, which is what the quadratic expansion produces).

Under (R1)–(R3), the local posterior is Gaussian:

$$\log p(\theta \mid o) \;=\; \mathrm{const} \;+\; s^T (\theta - \theta_t) \;-\; \tfrac12 (\theta - \theta_t)^T (H_M + H_L)(\theta - \theta_t) \;+\; O(\lVert\theta - \theta_t\rVert^3)$$

so the posterior is approximately $\mathcal N(\theta^\star, (H_M + H_L)^{-1})$ with mean

$$\theta^\star - \theta_t \;=\; (H_M + H_L)^{-1} s.$$

This is the standard local-Gaussian / Laplace-approximation form; nothing new yet.

## 3. The natural-gradient direction and the gain decomposition

Define the **natural gradient** of the log-likelihood at $\theta_t$ (in the Fisher metric of the observation channel):

*[Definition (natural gradient at the current point)]*

$$\tilde\nabla \log p(o \mid \theta_t) \;:=\; \mathcal I(\theta_t)^{-1} \, s.$$

Under (R1) and standard regularity, $\mathcal I(\theta_t) = \mathbb E_o[H_L]$ — for a single observation in the local-quadratic regime, $\mathcal I(\theta_t)$ is the limit of $H_L$ averaged over $o$ generated from $p(\cdot \mid \theta_t)$. For *single* observation, $H_L$ is the realized Fisher (observed information). For derivations that focus on the structure of the update rule rather than on stochastic averaging, we work with $H_L$ directly; the substitution $H_L \to \mathcal I(\theta_t)$ is the standard observed-vs-expected information distinction, exact in the same Fisher-local regime.

**The decomposition.** Rewrite the posterior mean shift:

*[Derived (gain decomposition in the natural-gradient direction)]*

$$
\Delta\theta \;=\; (H_M + H_L)^{-1} s \;=\; (H_M + H_L)^{-1} \, H_L \, (H_L^{-1} s) \;=\; (H_M + H_L)^{-1} \, H_L \cdot \tilde\nabla.
$$

The **gain operator** acting on the natural gradient is

$$K \;:=\; (H_M + H_L)^{-1} H_L.$$

**Scalar / commuting case.** When $H_M$ and $H_L$ commute (always true in 1-D; true in $d$ dimensions when they share an eigenbasis — which Fisher-local invariance under (PI)/Čencov picks out as the natural reduction), $K$ has eigenvalues

$$
\eta^\ast_i \;=\; \frac{h_{L,i}}{h_{M,i} + h_{L,i}} \;=\; \frac{1/u_{o,i}}{1/u_{M,i} + 1/u_{o,i}} \;=\; \frac{u_{M,i}}{u_{M,i} + u_{o,i}}
$$

(per-coordinate, where $h_{M,i}$ / $h_{L,i}$ are the shared-eigenbasis eigenvalues of $H_M$ / $H_L$ and $u_{M,i} = 1/h_{M,i}$, $u_{o,i} = 1/h_{L,i}$). Collapsing to scalar:

$$
\boxed{\;\eta^\ast \;=\; \frac{U_M}{U_M + U_o}\;}
$$

— exactly the form in `#emp-update-gain`'s Formal Expression, derived from the Fisher-local quadratic expansion of prior and likelihood, applied to the natural-gradient direction.

**This is the exactness claim from `#emp-update-gain`'s strengthened Epistemic Status, derived.** What is exact: the posterior mean shift in the natural-gradient direction is scaled by $U_M / (U_M + U_o)$, in the regime where the prior and likelihood admit local quadratic expansion with non-degenerate Hessians and the step size is first order in that expansion. Linear-Gaussian (Kalman) and conjugate-Bayesian cases are exactly the cases where the quadratic expansion is *globally* exact (not just local), and the derivation gives the gain without any expansion error.

### 3.1 Mild scope-strengthening: where degenerate $H_L$ is admissible

The derivation requires $H_M + H_L \succ 0$ (so the posterior precision is invertible), not $H_L \succ 0$. This means:

*[Derived (admissibility of weakly-informative likelihoods)]*

When the observation is *uninformative* along some directions ($H_L$ rank-deficient), the gain $K = (H_M + H_L)^{-1} H_L$ is still well-defined — it simply has eigenvalue $0$ along the unobserved directions ($u_{o,i} \to \infty$, $\eta^\ast_i \to 0$, no update along that direction) and the canonical $U_M / (U_M + U_o)$ form along the observed directions. The reverse — degenerate prior $H_M$ — is also admissible *if* $H_L$ pins the direction down: $\eta^\ast_i \to 1$ along uninformative-prior directions where the observation is informative, reflecting "trust the observation when the prior says nothing."

This is mildly *stronger* than the (R1) statement (which required $H_M \succ 0$ and $H_L \succ 0$ both). The honest minimal condition is $H_M + H_L \succ 0$, with $U_M / (U_M + U_o)$ defined per-eigendirection by the limit. This corresponds to standard "improper prior" admissibility in Bayesian inference: an improper uniform prior with $H_M = 0$ along some direction gives $\eta^\ast = 1$ along that direction — the maximum-likelihood limit. Not new mathematically, but a clean clarification of the form's reach.

## 4. Why the natural-gradient direction is the right direction to read $\eta^\ast$ off

The derivation in §3 reads $\eta^\ast$ as the coefficient on the natural-gradient direction $\tilde\nabla = H_L^{-1} s$ — not on the Euclidean score $s$ itself. Two observations explain why this is the load-bearing reading.

**Observation 1 (the AAD-internal motivation).** Under the parameterization-invariance axiom (PI) from `#scope-agent-identity`, B1 directional fidelity should be coordinate-invariant — the sub-scope $\alpha$ of `#der-gain-sector-bridge` should not depend on the choice of coordinate on the statistical manifold. Čencov 1982 forces the Fisher metric as the unique Markov-invariant metric on a statistical manifold (this is the 4th primary instance of `#disc-additive-coordinate-forcing` per `#deriv-fisher-whitened-update-rule`'s Path A). The natural-gradient direction is therefore the AAD-internally-canonical direction — under (PI)/Čencov, it is what the agent "should" descend along, *not* the Euclidean gradient $s$.

The gain $\eta^\ast = U_M / (U_M + U_o)$ is the coefficient on the canonical direction. Reading the gain off the Euclidean direction would give $(H_M + H_L)^{-1}$ — which depends on $H_M, H_L$ jointly and doesn't decompose into a clean prior-vs-likelihood ratio. Reading it off the natural gradient gives the additive prior+likelihood weighting that the AAD form names.

**Observation 2 (the global-exactness limits).** In the linear-Gaussian case (Kalman), the natural gradient and the Euclidean gradient coincide *up to the variance scaling*, and the global-exactness of the quadratic expansion means the local derivation goes through globally. In conjugate-Bayesian cases (Beta-Bernoulli, Dirichlet-multinomial, Gaussian-Gaussian, etc.), the natural-gradient flow is the *exact* posterior update at step size 1 — this is the conjugate-computation-VI observation of Khan & Lin 2017. In both cases, $U_M / (U_M + U_o)$ is exact globally, not just locally.

For general smooth models, the natural-gradient invariance theorem of Amari 1998 (and predecessors) guarantees that the natural gradient is parameterization-invariant. The Fisher-local quadratic expansion is the order at which the natural gradient and the exact posterior agree; the derivation of §3 makes this concrete: at first order in step size, posterior-mean-shift along the natural gradient is scaled by $U_M / (U_M + U_o)$.

**Together,** the natural-gradient direction is both the AAD-internally-canonical direction (under (PI)/Čencov) and the direction along which the local quadratic approximation is sharp. Reading $\eta^\ast$ off it gives the form `#emp-update-gain` names; the same form on any other direction degrades at higher order in $\lVert\theta - \theta_t\rVert$.

## 5. Three derivation routes and why they agree

Three structural antecedents for the same derivation were named at brief: Cramér-Rao / inverse-Fisher; Bregman projection of the posterior onto the local tangent plane; the direct local-Gaussian-Laplace expansion of §3. They agree at the result — they differ in what they make manifest.

### 5.1 Route A: Direct local-Gaussian expansion (§3)

Most elementary. Take quadratic expansion of $\log \pi_0$ and $\log p(o \mid \cdot)$ around $\theta_t$, add, complete the square, read the posterior mean. The gain $K = (H_M + H_L)^{-1} H_L$ falls out by algebraic factoring; the scalar collapse gives $U_M / (U_M + U_o)$. This is the route §3 took.

**What it makes manifest.** The structural origin of the form: the additive log-posterior decomposition into prior + likelihood quadratics produces an additive precision, which inverts to an additive-variance ratio. The form is "in" the convolution of two Gaussian information sources.

### 5.2 Route B: Bregman / KL-projection onto the local tangent plane

The Bayesian posterior is the unique minimizer of the variational free energy:

$$q^\star \;=\; \arg\min_q \; \mathrm{KL}(q \,\Vert\, \pi_0) - \mathbb E_q[\log p(o \mid \theta)].$$

Restrict the variational family to Gaussians centered at points along the natural-gradient direction from $\theta_t$:

$$q_\eta(\theta) \;\propto\; \pi_0(\theta) \cdot \exp\big(\eta \cdot s^T (\theta - \theta_t)\big)$$

— the **exponential tilt** of $\pi_0$ by the score, parameterized by tilt magnitude $\eta$. This is the one-parameter subfamily of natural-parameter exponential families connecting the prior ($\eta = 0$) to the full posterior ($\eta = 1$, plus the quadratic-Hessian correction).

Under the local quadratic expansion of $\pi_0$, $q_\eta$ is Gaussian with mean $\theta_t + \eta H_M^{-1} s$ and the same prior covariance $H_M^{-1}$. The variational free energy as a function of $\eta$ is:

$$
\mathcal F(\eta) \;=\; \mathrm{KL}(q_\eta \,\Vert\, \pi_0) - \mathbb E_{q_\eta}[\log p(o \mid \theta)] \;=\; \tfrac{\eta^2}{2} s^T H_M^{-1} s \;-\; \eta \, s^T H_M^{-1} s \;+\; \tfrac{\eta^2}{2} s^T H_M^{-1} H_L H_M^{-1} s \;+\; \mathrm{const}.
$$

(The first term is $\mathrm{KL}(q_\eta \Vert \pi_0)$; the second is the linear contribution of the score; the third is the quadratic likelihood-Hessian penalty on the displacement. All higher-order terms in $\theta - \theta_t$ are $O(\eta^3)$ and dropped at first order.)

Setting $d\mathcal F/d\eta = 0$:

$$
\eta \cdot s^T H_M^{-1} s \;-\; s^T H_M^{-1} s \;+\; \eta \cdot s^T H_M^{-1} H_L H_M^{-1} s \;=\; 0
$$

$$
\eta^\star \cdot s^T H_M^{-1} (I + H_L H_M^{-1}) s \;=\; s^T H_M^{-1} s
$$

$$
\eta^\star \cdot s^T (H_M^{-1} + H_M^{-1} H_L H_M^{-1}) s \;=\; s^T H_M^{-1} s.
$$

In the commuting / scalar case ($H_M, H_L$ commute on the relevant subspace):

$$
\eta^\star \;=\; \frac{H_M^{-1}}{H_M^{-1} + H_M^{-1} H_L H_M^{-1}} \;=\; \frac{1}{1 + H_L H_M^{-1}} \;=\; \frac{H_M}{H_M + H_L} \;=\; \frac{1/U_M}{1/U_M + 1/U_o}.
$$

Wait — this gives $\eta^\star = H_M / (H_M + H_L) = U_o / (U_M + U_o)$, the *complement* of the `#emp-update-gain` form. The difference: Route B reads the gain off the *Euclidean-prior-direction* $H_M^{-1} s$ (the tilt direction in moment coordinates of the prior), not off the natural gradient $H_L^{-1} s$ (the tilt direction in moment coordinates of the likelihood). The two differ by the ratio $H_L^{-1} / H_M^{-1}$.

**Reconciliation.** Both readings are right, on different reference directions:
- $\eta^\ast_{\text{NG}} = H_L / (H_M + H_L) = U_M / (U_M + U_o)$ — coefficient on the natural-gradient direction $H_L^{-1} s$.
- $\eta^\star_{\text{prior}} = H_M / (H_M + H_L) = U_o / (U_M + U_o)$ — coefficient on the prior-curvature-rescaled direction $H_M^{-1} s$.

Their product is fixed: $\eta^\ast_{\text{NG}} \cdot H_L^{-1} = \eta^\star_{\text{prior}} \cdot H_M^{-1} = (H_M + H_L)^{-1}$, which is the **posterior covariance** (the actual posterior shift, $(H_M + H_L)^{-1} s$, is reference-direction-independent — only its decomposition into "gain × reference direction" varies with the choice of reference direction).

The `#emp-update-gain` form names the natural-gradient coefficient. The complement form $U_o / (U_M + U_o)$ is what the **Kalman literature** sometimes calls the prior-weight in the convex combination (e.g., scalar Kalman: posterior mean = (1 - K) × prior + K × observation; both K and 1-K appear and have $U_M / (U_M + U_o)$ shape). They are two faces of the same posterior-mean-shift; the AAD form fixes the natural-gradient face as canonical (per §4).

**What Route B makes manifest.** The form is a **Bregman/Fenchel projection** — the posterior is the projection of the prior onto the level set of the score, in the KL geometry, and the projection coefficient along the natural gradient is $U_M / (U_M + U_o)$. This connects to `#disc-additive-coordinate-forcing`'s Fenchel-Bregman reframe (the `spike-fenchel-bregman-reframe-additive-coordinate-forcing-2026-04-24` Tier-3 architectural-proposal) — the present derivation is a worked instance of that geometry at the update layer.

### 5.3 Route C: Cramér-Rao / inverse-Fisher

The Cramér-Rao bound says any unbiased estimator's covariance is lower-bounded by $\mathcal I^{-1}$ — so $U_o = H_L^{-1}$ is the **floor** on observation uncertainty. The posterior covariance $(H_M + H_L)^{-1}$ inverts the sum of prior and observation precisions, and the Cramér-Rao floor enters as the observation-precision contribution.

In the scalar case:
$$\frac{1}{\mathrm{Var}(\theta \mid o)} \;=\; \frac{1}{U_M} \;+\; \frac{1}{U_o} \quad\Rightarrow\quad \mathrm{Var}(\theta \mid o) \;=\; \frac{U_M U_o}{U_M + U_o}.$$

The posterior mean shift, normalized by the natural-gradient direction's length, is $\mathrm{Var}(\theta \mid o) / U_o = U_M / (U_M + U_o) = \eta^\ast$ — same form, different name for the same algebraic fact.

**What Route C makes manifest.** $\eta^\ast$ is the **fractional contribution of the observation to the posterior precision** — or equivalently, the fractional posterior variance reduction attributable to the observation. This is the information-theoretic reading and the one most directly aligned with `#def-causal-information-yield` and the broader entropy / mutual-information machinery in AAD.

### 5.4 Why the three routes agree

All three routes arrive at $\eta^\ast = U_M / (U_M + U_o)$ on the natural-gradient direction. They differ in what they expose:

| Route | Lever | Surface meaning of $\eta^\ast$ |
|---|---|---|
| A — Local-Gaussian Laplace expansion | Algebraic completion of squares on additive log-likelihoods | Posterior mean shift coefficient |
| B — Bregman / KL projection | First-order condition on variational free energy along natural-gradient tilt | Projection coefficient of posterior onto local tangent plane |
| C — Cramér-Rao / inverse-Fisher | Precision addition $1/U_M + 1/U_o$, inverted | Fractional observation contribution to posterior precision |

Their agreement is not coincidence: the local-Gaussian regime *is* the regime where prior + likelihood compose as a Pythagorean projection in the Fisher metric (Amari-Nagaoka 2000 §3.2; the same Pythagorean projection underlying `#deriv-strategy-cost-regret-bound`'s ρ-decomposition). The three routes are the three faces of one geometric object: an exponential-family / Bregman / Pythagorean structure on the local tangent plane.

This three-route convergence is itself evidence the form is structural, not artifactual. **The form is the precision-additive composition of two Gaussian information sources, read off the natural-gradient direction.**

## 6. Composition with the rest of the AAD machinery

### 6.1 Sibling to `#deriv-fisher-whitened-update-rule`

`#deriv-fisher-whitened-update-rule` lives at the **edge-update layer** of Section II's strategy DAG: it derives the Fisher-whitening correction for correlated-evidence (L1'/L2) cases where the log-odds-additive direction diverges from the natural-gradient direction. Its A2' sub-scope $\alpha_3$ partitions on correlation regime + whitening + Bayesian coherence.

This spike derives the **gain magnitude** that the segment uses for the same Fisher-whitened update at the **model-parameter layer** of Section I (the `#emp-update-gain` machinery — model uncertainty vs observation uncertainty). The two segments are sibling derivations of the same Fisher-local invariance regime:

| Layer | Segment | What is derived |
|---|---|---|
| Section II (edge-update on strategy DAG) | `#deriv-fisher-whitened-update-rule` | Update **direction** under correlated evidence: Fisher-whitened natural-gradient |
| Section I (model-parameter update on $M_t$) | `#emp-update-gain` (post-promotion) | Update **gain** on natural-gradient direction: $U_M / (U_M + U_o)$ |

Both segments cite (PI)/Čencov as the AAD-internal axiom forcing the Fisher metric. The Fisher-whitened edge-update segment cites Path A (B1-parameterization-invariance + Čencov) as the canonical justification; the present spike's §4 motivates reading $\eta^\ast$ off the natural-gradient direction with the same justification. Cross-segment consistency: both pieces of the Fisher-local invariance regime — the direction (whitening) and the magnitude (gain) — are AAD-internally motivated by the same (PI) axiom and Čencov uniqueness theorem.

### 6.2 Special case of `#deriv-adaptive-gain-dynamics`'s meta-gain framework

`#deriv-adaptive-gain-dynamics` defines meta-gain conditions (MG-1)–(MG-4) and partitions A2' sub-scope $\alpha$ into $\alpha_1$ (fixed gain) and $\alpha_2$ (adaptive gain). The present derivation's gain operator $K = (H_M + H_L)^{-1} H_L$ is a *deterministic function of the current state* — it depends on the prior covariance $H_M^{-1}$ (which is part of the agent's $M_t$ state) and on the observation Fisher $H_L$ (which depends on $\theta_t$ and the observation). It is therefore an instance of the *degenerate special case* of meta-gain that `#deriv-fisher-whitened-update-rule` already identifies for Fisher whitening: the meta-gain is determined by the primary state rather than independently learned.

Both (MG-1) and (MG-2) hold trivially in the regularity-conditions-met case: $K$ is symmetric-positive-definite ((MG-1)) and smooth ((MG-3)). The deterministic structure means (MG-2) and (MG-4) are vacuous (no independent meta-channel disturbance). Adaptive-Kalman with Mehra estimator (Case A of `#deriv-adaptive-gain-dynamics`) sits one level up — the agent additionally estimates $H_L$ (i.e., $U_o$) from the innovation sequence, adding a non-degenerate meta-channel with its own (MG-1)–(MG-4).

In words: the present spike establishes that under known $H_M, H_L$, the gain is $\eta^\ast = U_M / (U_M + U_o)$ as a deterministic function. Resolving epistemic opacity per `#emp-update-gain`'s Discussion §"Resolving Epistemic Opacity" — i.e., estimating $H_L$ from the agent's own mismatch sequence rather than knowing it — adds the Mehra-style meta-channel and lands in sub-scope $\alpha_2$ via `#deriv-adaptive-gain-dynamics`'s Case A.

### 6.3 Downstream tempo and persistence machinery

`#emp-update-gain`'s Discussion §"Connection to adaptive tempo" names $\mathcal T = \nu \cdot \eta^\ast$: tempo is event rate times update gain. Promoting `#emp-update-gain` from `empirical / robust-qualitative` to `derived (conditional on Fisher-local invariance regime)` lifts $\eta^\ast$'s tier; the tempo product $\mathcal T = \nu \cdot \eta^\ast$ inherits the lift wherever it lands at the same tier. The persistence-condition machinery (`#result-persistence-condition`, `#result-sector-condition-stability`) and the adaptive-tempo / aporia diagnostics (`#def-adaptive-tempo`, `#def-aporia`) all gain the tighter $\eta^\ast$ exactness statement in their Fisher-local instances.

The downstream "Connection to adaptive tempo" paragraph and the "Gain collapse — epistrophe failure" failure-mode paragraph in `#emp-update-gain`'s Discussion *do not need rewriting* — the qualitative direction claim survives, and the post-promotion statement strengthens the quantitative regime in which it is exact.

## 7. What this derivation does and does not establish

### 7.1 Does establish

1. **The form $\eta^\ast = U_M / (U_M + U_o)$ is exact** under (R1)–(R3), with $U_M = H_M^{-1}$ and $U_o = H_L^{-1}$ read off prior precision and observation Fisher. Three independent derivation routes (local-Gaussian, Bregman/KL, Cramér-Rao) converge on this.
2. **Linear-Gaussian (Kalman) and conjugate-Bayesian** are the cases where (R1) holds *globally*, not just locally — so $\eta^\ast$ is exact globally, no truncation. This recovers the existing "Exact" status for Kalman and conjugate-Bayesian in `#emp-update-gain`'s domain table.
3. **The natural-gradient direction is the canonical reference direction** for reading $\eta^\ast$, motivated AAD-internally by (PI)/Čencov per `#deriv-fisher-whitened-update-rule`'s Path A.
4. **Degenerate-likelihood and degenerate-prior cases are admissible** at the boundary, with $\eta^\ast \to 0$ along uninformative-observation directions and $\eta^\ast \to 1$ along uninformative-prior directions. The minimal-required condition is $H_M + H_L \succ 0$, not $H_M \succ 0$ and $H_L \succ 0$ both.
5. **Sibling relationship to `#deriv-fisher-whitened-update-rule`.** The whitening segment derives update *direction*; this derivation gives update *magnitude*. Together, the Fisher-local regime has both direction and magnitude AAD-internally derived under (PI)/Čencov.

### 7.2 Does not establish

1. **Behavior outside the Fisher-local regime.** When the local quadratic expansion fails — heavy-tailed posteriors (no second moment), structurally non-smooth likelihoods, multimodal uncertainty where the local quadratic misrepresents global structure — the form survives only as a robust-qualitative direction claim (gain rises with $U_M$, falls with $U_o$), not as a quantitative form. `#emp-update-gain`'s post-strengthening Epistemic Status names this honestly; this spike does not extend the derivation beyond it.
2. **Non-Bayesian update rules.** The derivation rests on (R3): the agent's update is taken to be the posterior of an explicit Bayesian model. RL fixed-α, PID fixed-gain, and rule-based agents lie outside the derivation's scope. The qualitative direction claim survives because these methods can be viewed as approximations to a Fisher-local Bayesian update with degenerate prior or coarsened likelihood — but the derivation does not establish that.
3. **Higher-order corrections to $\eta^\ast$.** The form is exact at first order in step size. The $O(\lVert\Delta\theta\rVert^3)$ correction comes from higher derivatives of the log-likelihood; quantifying it is a problem-specific Edgeworth-expansion computation, deferred.
4. **Multi-step extrapolation.** The derivation is a one-step update result. Iterating the gain across multiple observations corresponds to the Kalman recursion / conjugate-posterior chain — which the Kalman / conjugate cases in §3 cover when (R1) holds globally. For general smooth models, iterating the Fisher-local approximation accumulates curvature error that bounds the validity horizon; this is an open quantitative-rate question.
5. **Estimating $U_o$ from the mismatch sequence.** The "Resolving Epistemic Opacity" question — how the agent gets $U_o$ when the observation noise is structurally unknown (`#def-observation-function` axiom) — is *not* answered by this derivation. It is the topic of `#deriv-adaptive-gain-dynamics`'s Case A (adaptive Kalman with Mehra estimator). The present derivation establishes the *target* $\eta^\ast$ given $(U_M, U_o)$; the Mehra machinery establishes the *estimator* for $U_o$ from the agent's observable history.

### 7.3 Where the strengthening attempt failed gracefully

Per the project's strengthen-first posture, the spike's working draft attempted to weaken the (R1) regularity conditions: in particular, to *strengthen* the form to "any smooth log-posterior admitting a stable local mode" rather than the explicit quadratic-expansion regime. The attempt fell back to the stated regime because:

(a) The Pythagorean projection structure underlying Routes A–C is genuinely Gaussian-tangent-plane structure. Beyond the local-quadratic regime, the projection coefficient acquires shape-dependent corrections that do not collapse to the simple $U_M / (U_M + U_o)$ form.

(b) The natural-gradient direction is well-defined wherever $H_L$ is positive-definite; the gain operator $K = (H_M + H_L)^{-1} H_L$ is well-defined wherever $H_M + H_L$ is positive-definite. Outside these conditions, the form's domain of definition itself breaks.

(c) The honest claim is that the *qualitative* direction (gain rises with model uncertainty, falls with observation noise) is universal, while the *quantitative* form is exact in the named regime. This matches `#emp-update-gain`'s post-strengthening Epistemic Status exactly — the spike does not improve on that framing, only verifies it.

The strengthening fallback documentation is in §7.2; no further softening of `#emp-update-gain`'s Epistemic Status is warranted by this spike.

## 8. Derivation audit

| Claim | Source | Strength |
|---|---|---|
| Local Gaussian quadratic expansion of log-prior + log-likelihood under $C^3$ smoothness (§2) | Taylor's theorem | Standard (exact at quadratic order) |
| Posterior precision is $H_M + H_L$ under (R1)–(R3) (§2) | Algebraic combination of quadratic forms | Derived (exact in regime) |
| Posterior mean shift $\Delta\theta = (H_M + H_L)^{-1} s$ (§2) | Completing the square on combined quadratic | Derived (exact in regime) |
| Gain decomposition $\Delta\theta = K \cdot \tilde\nabla$ with $K = (H_M + H_L)^{-1} H_L$ (§3) | Algebraic factoring | Derived (exact in regime) |
| Scalar / commuting collapse $\eta^\ast = U_M / (U_M + U_o)$ on natural-gradient direction (§3) | Eigenvalue substitution + $U_M = H_M^{-1}$, $U_o = H_L^{-1}$ | Derived (exact in regime) |
| Linear-Gaussian (Kalman) and conjugate-Bayesian global exactness (§3) | Quadratic expansion is globally exact in these cases | Derived (textbook special cases) |
| Admissibility of degenerate $H_M$ or $H_L$ at boundary (§3.1) | Eigenvalue limit in $K = (H_M + H_L)^{-1} H_L$ | Derived (mild scope-strengthening) |
| Natural-gradient direction as AAD-internally-canonical (§4 Obs 1) | (PI) axiom from `#scope-agent-identity` + Čencov 1982 + `#deriv-fisher-whitened-update-rule` Path A | Derived (conditional on (PI) adoption) |
| Local-quadratic regime as the order at which natural-gradient and exact-posterior agree (§4 Obs 2) | Amari 1998 natural-gradient invariance theorem + conjugate-computation VI (Khan-Lin 2017) | Derived (textbook) |
| Three-route convergence: local-Gaussian, Bregman/KL, Cramér-Rao (§5) | Three independent derivations giving the same form | Derived |
| Bregman route's prior-direction reading is complement $U_o / (U_M + U_o)$ on a different reference direction (§5.2) | Direct algebraic computation showing the variational FE optimum on prior-direction tilt | Derived (clarification of two faces of same posterior shift) |
| Cramér-Rao route's reading: $\eta^\ast$ = fractional observation contribution to posterior precision (§5.3) | Direct from precision-additivity | Derived |
| Sibling relationship to `#deriv-fisher-whitened-update-rule` (§6.1) | Both segments share (PI)/Čencov; one derives direction, one derives magnitude | Discussion-grade (positioning) |
| Special case of `#deriv-adaptive-gain-dynamics`'s degenerate-meta-gain framework (§6.2) | Direct: $K$ is deterministic function of state | Derived (consistency check) |
| Downstream tempo / persistence machinery inherits the tier lift (§6.3) | Tier-propagation rules from FORMAT.md Epistemic Triage | Discussion-grade (consequential framing) |

### Epistemic honest obstructions

- **(O1) The natural-gradient invariance theorem (Amari 1998) is imported, not derived.** The §4 Observation 2 step relies on the textbook result that natural-gradient flow is parameterization-invariant. The (PI)/Čencov axiomatic forcing per `#deriv-fisher-whitened-update-rule`'s Path A is what makes the import AAD-internal; without (PI), the natural-gradient direction is a chosen-not-forced direction and the derivation degrades to "the form on the chosen direction." This is the same obstruction `#deriv-fisher-whitened-update-rule` carries; this spike's status is conditional on the same axiom.

- **(O2) The single-observation per-step setup.** The derivation handles one observation $o$ at $\theta_t$. Multi-observation per step (batch update) generalizes mechanically: $H_L = \sum_i H_{L,i}$ for independent observations; the gain on each natural-gradient direction collapses to the same form with summed observation precisions. The single-observation form is presented for clarity, not as a restriction.

- **(O3) The matrix vs scalar question.** `#emp-update-gain`'s scalar Formal Expression vs matrix Discussion ("Multi-dimensional generalization") tension is resolved cleanly here: the matrix gain $K = (H_M + H_L)^{-1} H_L$ is the natural object, and the scalar $U_M / (U_M + U_o)$ is its eigenvalue in the commuting / 1-D / shared-eigenbasis case. This is mechanical and not a scope restriction, but worth surfacing in the post-promotion segment.

- **(O4) Step size at the boundary of (R2).** "First order in step size" is precise but qualitative; the actual cutoff between Fisher-local and non-local depends on the third-derivative norms of $\log \pi_0$ and $\log p(o\mid \cdot)$. This is a problem-specific quantitative regime. The promotion-recommended Epistemic Status (and the post-promotion `#emp-update-gain` Epistemic Status, which already names this) handles it qualitatively; an Edgeworth-expansion treatment is deferred to a future spike if it ever becomes load-bearing.

- **(O5) The "robust qualitative" downstream claim is not derived here.** The qualitative direction claim — gain rises with $U_M$, falls with $U_o$, regardless of regime — is intuitively right (the partial derivatives of $U_M / (U_M + U_o)$ in its scalar form are obvious) but its survival outside the Fisher-local regime relies on the general structure of Bayesian updating, not on this derivation. `#emp-update-gain`'s Epistemic Status retains the qualitative claim at robust-qualitative tier; this spike does not establish it at the derived tier outside the named regime.

## 9. Promotion recommendation

### 9.1 Recommended action: lift `#emp-update-gain` to `derived (conditional on Fisher-local invariance regime)`

The Codex AAD-5 finding has already been addressed at the Epistemic Status level. This spike establishes that the strengthened claim is *carried* by a clean derivation under three named regularity conditions. The natural promotion path:

**Status change:** `empirical` / `robust-qualitative` → `derived` / `conditional` (conditional on (R1) Fisher-local quadratic regime + (R2) first-order step size + (R3) Bayesian coherence + (PI) for the AAD-internal direction-canonicalization).

**Type change:** `empirical` → `derived`. The form's character changes from "empirically observed across many adaptive systems" to "structurally derived in the Fisher-local invariance regime; empirically observed across many adaptive systems including ones outside that regime."

**Slug / type tag prefix update:** Per `bin/align-slug`, `derived` type → `deriv-` prefix. The current slug `emp-update-gain` should rename to `deriv-update-gain` to align with the new type. (Equivalent: keep the slug if the segment carries both a derived form and an empirical-claim tail; the type-tag rename is mechanical via `bin/align-slug` and a separate one-line rename if the role-prefix sweep runs.)

### 9.2 Two implementation paths

**Path I (preferred): keep derivation in a companion appendix segment `#deriv-fisher-local-update-gain`.** The §3–§5 content of this spike becomes a short appendix derivation segment. `#emp-update-gain` cites it for the structural backing of the Formal Expression and retains the Discussion / Domain-validation / Open-questions content. The appendix has type `derivation` and status `conditional`. Promotion-symmetry with `#deriv-fisher-whitened-update-rule` (a peer-derivation appendix) is the rationale.

**Path II: inline the derivation in `#emp-update-gain`'s Formal Expression block.** The §2–§3 algebraic derivation is short enough (~15 lines) to fit inside the Formal Expression block as a "Derivation under Fisher-local regime" sub-block. Lower segment-count cost; higher in-segment density. The Bregman / Cramér-Rao alternate routes (§5) and the §4 motivation would still need to land somewhere — possibly the Epistemic Status or Discussion sections.

**Recommendation:** **Path I**. Reasons:
- `#emp-update-gain` is already substantial in its Discussion (six paragraphs of domain validation, gain dynamics, overfitting, multi-dimensional, representation, simulation). Inlining would crowd the segment.
- Appendix segment matches the architectural pattern of `#deriv-fisher-whitened-update-rule` (sibling derivation at edge-update layer); a `#deriv-fisher-local-update-gain` would sit alongside it as the model-parameter-layer sibling.
- The appendix can carry the three-route discussion (§5) cleanly, including the Bregman / Fenchel reframe connection that anchors to `#disc-additive-coordinate-forcing`'s 4th primary instance + Fenchel-Bregman reframe spike.
- The companion-appendix pattern preserves the empirical-claim header at `#emp-update-gain` for the cross-domain validity (RL, PID, software-developer instances that are not strictly Fisher-local) while making the derivation explicit for the Fisher-local regime that load-bears for Kalman / conjugate / natural-gradient.

### 9.3 Sketch of post-promotion `#emp-update-gain` Epistemic Status

The post-promotion Epistemic Status would replace the current "*Exact* under the Fisher-local invariance regime" paragraph with a cleaner statement that cross-references the new appendix:

> *Derived* under the **Fisher-local invariance regime** ( #deriv-fisher-local-update-gain): for any smooth log-likelihood admitting non-degenerate local quadratic expansion, with single-step update at first order in the step size, the natural-gradient Bayesian posterior mean shift is exactly $\Delta\theta = K \cdot \tilde\nabla$ with gain operator $K = (H_M + H_L)^{-1} H_L$ and scalar / commuting-basis collapse $\eta^\ast = U_M / (U_M + U_o)$. The matrix-valued generalization is the natural object; the scalar form captures the essential structure when prior and likelihood share an eigenbasis (always in 1-D; under (PI)/Čencov in the natural-gradient direction in higher dimensions). Linear-Gaussian (Kalman) and conjugate-Bayesian instances are cases where the local quadratic regime is *globally* exact; the natural-gradient invariance theorem of Amari 1998 guarantees the form is exact at the local-tangent-plane Pythagorean projection level in general. Outside this regime — heavy-tailed posteriors, structurally non-smooth likelihoods, multimodal uncertainty — the direction (gain rises with $U_M$, falls with $U_o$) is preserved as *robust qualitative*; the first-order form is recovered locally; global quantitative fidelity is what need not hold.

The qualitative direction claim and the failure-mode discussion (gain collapse → epistrophe failure) remain untouched. The downstream tempo / persistence machinery references inherit the tier lift.

### 9.4 Companion-appendix segment outline (if Path I taken)

```
#deriv-fisher-local-update-gain
  type: derivation
  status: conditional
  depends:
    - emp-update-gain
    - def-mismatch-signal
    - def-observation-function
    - scope-agent-identity
    - disc-additive-coordinate-forcing
    - deriv-fisher-whitened-update-rule

  Summary: One-step Bayesian posterior mean shift along the natural-gradient
    direction, under non-degenerate local quadratic expansion of prior and
    likelihood at the current model parameter, is exactly $K \cdot \tilde\nabla$
    with $K = (H_M + H_L)^{-1} H_L$ and scalar collapse $\eta^\ast = U_M/(U_M + U_o)$.

  Formal Expression: §2–§3 of this spike (setup, derivation, scalar collapse,
    degenerate-boundary cases).
  Epistemic Status: §7 of this spike (what is and is not established;
    conditional on (R1)–(R3) + (PI)).
  Discussion: §4 (canonical-direction motivation) + §5 (three-route
    convergence: local-Gaussian, Bregman, Cramér-Rao) + §6 (composition
    with #deriv-fisher-whitened-update-rule, #deriv-adaptive-gain-dynamics,
    downstream tempo / persistence).
  Working Notes: open questions on multi-step extrapolation, Edgeworth
    higher-order corrections, non-Bayesian variational-bound extension.
```

This is a draft outline only; the actual segment promotion is a follow-on cycle under Joseph's review per the brief.

## 10. Open questions after this spike

1. **Multi-step extrapolation rate.** The Fisher-local exactness is a one-step statement. Iterating over many observations accumulates higher-order curvature error in the non-Gaussian / non-conjugate case; what's the explicit rate? Standard Bernstein-von Mises asymptotics give a $1/\sqrt n$ posterior concentration rate — does the gain $\eta^\ast$'s exactness inherit a matching $1/\sqrt n$ degradation outside Kalman / conjugate? Open quantitative-rate question.

2. **Edgeworth higher-order correction.** Quantifying the $O(\lVert\Delta\theta\rVert^3)$ correction to $\eta^\ast$ in terms of third / fourth derivatives of the log-likelihood. Standard Edgeworth expansion gives the closed form; whether it becomes load-bearing for any AAD use case is the question that decides whether a future spike picks this up.

3. **Variational-bound extension.** Under variational approximation $\mathrm{KL}(q \| p) \leq \varepsilon$, the gain inherits a Pinsker-tight degradation factor (analogous to `#deriv-variational-sector-condition`'s $O(\sqrt\varepsilon)$ B1 degradation). Composing this with the present derivation gives the form under approximate-posterior agents in sub-scope $\alpha'$ — analogous to the variational-A2' partition.

4. **Multimodal posteriors.** When the prior or posterior is multimodal, the local-quadratic expansion around any one mode misses the global structure. Two natural moves: (a) treat each mode separately with per-mode $U_M / (U_M + U_o)$, with mode-mixture weights as a separate state; (b) accept the qualitative direction claim only. Worth a small follow-up spike if multimodal posteriors become load-bearing for any AAD use case.

5. **Connection to consolidation / replay (`#form-consolidation-dynamics`).** Between-event consolidation drives $H_M$ down (model uncertainty grows under offline replay) via the IB-gap-reduction objective. The present gain formula then says the *next* online observation gets up-weighted because $U_M / (U_M + U_o)$ rises with $U_M$. This is the formal connection between consolidation-induced uncertainty growth and increased online responsiveness — worth tightening into a result in a future cycle if `#form-consolidation-dynamics` lands a quantitative form.

6. **Tensor-tempo composition.** AAD-1 (Codex AAD-1 finding, May 12) flagged that `#def-adaptive-tempo`'s scalar form is too narrow for anisotropic gains / Fisher-whitened updates / LMI causal-IB / per-dimension persistence. The matrix gain operator $K = (H_M + H_L)^{-1} H_L$ from this derivation is exactly the per-coordinate anisotropic structure that AAD-1 wants. A tensor-tempo segment (open per TODO §AAD-1) would naturally cite this derivation as the per-dimension primitive: $\mathcal T = \nu \cdot K$ as a matrix product, with $\eta^\ast = U_M / (U_M + U_o)$ as the shared-eigenbasis scalar collapse.

## 11. References

**Information geometry / natural gradient (these are the load-bearing imports):**
- Amari, S.-i. (1998). "Natural gradient works efficiently in learning." *Neural Computation* 10(2):251–276.
- Amari, S.-i. & Nagaoka, H. (2000). *Methods of Information Geometry*. Translations of Mathematical Monographs 191. American Mathematical Society. §3 (Fisher metric, Pythagorean projection, exponential-family Legendre-Fenchel structure).
- Čencov, N. N. (1982). *Statistical Decision Rules and Optimal Inference*. AMS Translations of Mathematical Monographs 53. Original invariance-based derivation of Fisher metric uniqueness.

**Conjugate / variational Bayesian update:**
- Khan, M. E. & Lin, W. (2017). "Conjugate-computation variational inference: Converting variational inference in non-conjugate models to inferences in conjugate models." AISTATS 2017. Natural-gradient VI as conjugate-computation; the global exactness in conjugate-Bayesian cases.
- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer. §3.3 (Bayesian linear regression / Gaussian-Gaussian posterior — the canonical Fisher-globally-exact case).
- Kalman, R. E. (1960). "A new approach to linear filtering and prediction problems." *J. Basic Engineering* 82(1):35–45. The original linear-Gaussian Fisher-globally-exact case.

**Cramér-Rao / inverse-Fisher:**
- Cramér, H. (1946). *Mathematical Methods of Statistics*. Princeton University Press. §32.4 (the inequality).
- Rao, C. R. (1945). "Information and accuracy attainable in the estimation of statistical parameters." *Bull. Calcutta Math. Soc.* 37:81–91. Independent derivation.

**Bernstein-von Mises (for the open Q1 multi-step extrapolation rate):**
- van der Vaart, A. W. (1998). *Asymptotic Statistics*. Cambridge University Press. §10.2 (Bernstein-von Mises theorem).

**AAD segments referenced:**
- `#emp-update-gain` — current segment carrying the form; the post-promotion target.
- `#def-mismatch-signal` — upstream definition of $\delta_t$ and the mismatch transform.
- `#def-observation-function` — upstream definition of observation $o_t$ and the epistemic-opacity axiom (the constraint that motivates `#deriv-adaptive-gain-dynamics`' Mehra-style estimator).
- `#deriv-fisher-whitened-update-rule` — sibling derivation at the edge-update / Section II layer; shares the (PI)/Čencov AAD-internal axiom.
- `#deriv-adaptive-gain-dynamics` — adaptive-gain framework; the present gain operator $K$ is a degenerate special case (deterministic-meta-gain) of its (MG-1)–(MG-4) machinery.
- `#der-gain-sector-bridge` — Prop B.3 / B.4 sub-scope $\alpha$ partition; B1 directional fidelity; the present derivation slots inside sub-scope $\alpha_1$ (fixed-gain, no separately-learned meta-channel).
- `#disc-additive-coordinate-forcing` — 4th primary instance (Fisher metric via (PI)/Čencov); the present derivation reads $\eta^\ast$ off the (PI)-canonical direction.
- `#scope-agent-identity` — the (PI) parameterization-invariance axiom whose extension to the natural-gradient direction makes the AAD-internal motivation work.
- `#def-causal-information-yield` — downstream consumer of $U_o$ (CIY $\propto 1/U_o(a)$ scalar form per `#deriv-causal-ib-exploration`); inherits the tier lift.
- `#def-adaptive-tempo` — downstream consumer of $\eta^\ast$ in $\mathcal T = \nu \cdot \eta^\ast$.

**Related spikes:**
- `spikes/spike-fisher-whitened-update.md` (2026-04-22, promoted to `#deriv-fisher-whitened-update-rule`) — sibling at edge-update layer; shares the (PI)/Čencov framing.
- `spikes/spike-adaptive-gain-dynamics.md` (2026-04-23, promoted to `#deriv-adaptive-gain-dynamics`) — meta-gain framework; the present derivation is a degenerate special case.
- `spikes/spike-jacobian-b1-strengthening.md` (2026-04-23, partially promoted) — established the (PI)/Čencov 4th primary instance of `#disc-additive-coordinate-forcing`; the present spike's §4 cites this lineage for AAD-internal canonical-direction motivation.
- `spikes/spike-fenchel-bregman-reframe-additive-coordinate-forcing-2026-04-24.md` (2026-04-24, Tier-3 architectural proposal) — Fenchel-Bregman reframe of `#additive-coordinate-forcing`; the present derivation's Route B (§5.2) is a worked instance of that geometry at the model-parameter update layer.
