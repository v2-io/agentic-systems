---
spike: contraction-metric-generalization
date: 2026-04-22
status: draft
trigger: Gemini gap — Section III composition contraction results verified only for linear-Kalman; sub-scope β (PID / variational / non-convex-beyond-basin / rule-based) untouched by `#result-sector-persistence-template`. Lohmiller & Slotine's contraction-metric framework promises broad nonlinear lift.
posture: Strengthen-first. Push the metric formulation as far as it goes, then retreat honestly.
relates_to:
  - result-sector-persistence-template
  - deriv-sector-condition
  - der-gain-sector-bridge
  - form-composition-closure
  - deriv-critical-mass-composition
  - disc-separability-pattern
  - sketch-multi-timescale-stability
  - spikes/spike-critical-mass-composition.md
  - spikes/spike-adaptive-gain-dynamics.md
  - spikes/spike-bridge-lemma-contraction.md
---

# Spike: Contraction-Metric Generalization of `#result-sector-persistence-template`

## Problem statement

`#result-sector-persistence-template` states AAD's persistence results parameter-free in the form: state variable $\xi$ evolving under $\dot\xi = -F(\xi) + w(t)$ satisfies three preconditions (T1) zero-at-zero, (T2) **Euclidean sector condition** $\xi^T F(\xi) \geq \alpha \lVert\xi\rVert^2$ on $\lVert\xi\rVert \leq R$, (T3) bounded disturbance. The template yields ultimate bound $R^\ast = \rho_\xi/\alpha$ and adaptive reserve $\Delta\rho^\ast = \alpha R - \rho$. Six AAD segments invoke the template.

The template's **(T2) is a *one-point* sector bound matched to a *quadratic* Lyapunov candidate $V(\xi) = \tfrac{1}{2}\lVert\xi\rVert^2$ in the Euclidean norm.** This is load-bearing but restrictive:

1. **Sub-scope α coverage is uneven.** Matrix Kalman's natural sector bound is in the $(P^-)^{-1}$-weighted inner product, transferred to Euclidean A2' with a $\kappa(P^-)$ degradation (`#der-gain-sector-bridge` "Weighted-norm subtlety"). Exponential-family-in-natural-parameters sits more naturally under the Fisher metric. Strongly-convex gradient is more naturally measured under the Hessian-weighted norm.

2. **Sub-scope β is absent.** PID, rule-based agents, variational-approximate posteriors, and non-convex agents beyond basin fail the Euclidean sector condition generically. `#deriv-sector-condition`'s A2' sub-scope β entry is "A2' must be verified per-system" — the current architecture has no lift that generically buys β.

3. **Tier 2/3 agents lose closed form.** `#form-composition-closure` requires the **incremental sector bound** (DA2'-inc, strong monotonicity across the whole state space), which is strictly stronger than (T2). Tier 2 / Tier 3 sit at "local only" or "verify per-domain" — `#disc-separability-pattern`'s "general open" under the Contraction ladder.

4. **Composition results (`#deriv-critical-mass-composition`) are Tier-1-symmetric-matched only.** `#form-composition-closure` acquires composite $\alpha_c$ via weakest-link bound; `#deriv-critical-mass-composition` pushes to a closed form for matched-symmetric-Tier-1 pairs. Heterogeneous-architecture composites are §6.1 obstruction territory.

Contraction analysis (Lohmiller & Slotine 1998, *Automatica* 34:683; Slotine 2003, *Int. J. Adapt. Control Signal Process.* 17:397) offers a generalization: a state- and time-dependent **Riemannian (or Finsler) metric** $M(x, t)$ under which the *differential dynamics* contract:

$$\dot M + M \frac{\partial f}{\partial x} + \Big(\frac{\partial f}{\partial x}\Big)^T M \preceq -2\lambda M, \qquad \lambda \gt 0.$$

Two well-known properties make this a candidate for AAD generalization:

- **(C-α) Metric-freedom picks up sub-scope α "for free".** A contraction metric can be non-Euclidean, allowing systems that fail Euclidean A2' to satisfy the contraction condition in a suitably weighted coordinate. Weighted-norm Lyapunov is the matched canonical move (Khalil 2002 §4.2; also `#deriv-sector-condition`'s "Why Euclidean A2' specifically" passage).

- **(C-β) Compositional closure.** Contraction is preserved under (a) parallel (product), (b) hierarchical/lower-triangular cascade, (c) negative feedback with bounded loop gain. Slotine 2003 gives a clean compositional calculus that `#form-composition-closure` currently lacks above Tier 1.

The spike attacks: **recast (T2) in contraction-metric form; track which sub-scope items lift; derive a compositional upgrade for `#form-composition-closure`; draw the honest map of where metric formulation fails.**

---

## §1. Restating `#result-sector-persistence-template` in contraction-metric form

### 1.1 The contraction condition

Let $\xi(t) \in \mathbb{R}^n$ evolve under $\dot\xi = -F(\xi, t) + w(t)$ where $F$ is $C^1$ in $\xi$ and continuous in $t$. Let $M: \mathbb{R}^n \times \mathbb{R}_+ \to \mathbb{S}_{++}^n$ be a smooth symmetric-positive-definite matrix-valued function (the metric) with uniform conditioning: there exist constants $0 \lt m_1 \leq m_2 \lt \infty$ such that

$$m_1 I \preceq M(\xi, t) \preceq m_2 I \qquad \forall\, \xi \in \mathcal{B}_R,\, t \geq 0. \tag{M0}$$

*[Definition (contraction-template-preconditions)]*

**(CT1) Zero correction at zero state.** $F(0, t) = 0$ for all $t$ — same as (T1).

**(CT2) Local differential-contraction condition.** There exist $\lambda \gt 0$ and $R \gt 0$ such that for all $\xi \in \mathcal{B}_R$, $t \geq 0$:

$$-\dot M(\xi, t) - M(\xi, t)\frac{\partial F}{\partial \xi}(\xi, t) - \Big(\frac{\partial F}{\partial \xi}(\xi, t)\Big)^T M(\xi, t) \;\preceq\; -2\lambda M(\xi, t) \tag{CT2}$$

equivalently,

$$\dot M + M \frac{\partial F}{\partial \xi} + \Big(\frac{\partial F}{\partial \xi}\Big)^T M \;\succeq\; 2\lambda M$$

(because $F$ enters as $-F$ in the dynamics; the Jacobian of the dynamics is $-\partial F/\partial\xi$, which is what Lohmiller-Slotine's inequality would be stated on).

**(CT3) Bounded disturbance** — same menu as (T3): Model D $\lVert w\rVert \leq \rho_\xi$ or Model S $\mathbb{E}[\lVert w\rVert^2] = \sigma_\xi^2$.

### 1.2 The contraction template — Model D

*[Result (contraction-template-D, conditional on CT1, CT2, CT3-D, M0)]*

Let $V(\xi, t) = \xi^T M(\xi, t) \xi$ (a state- and time-weighted Lyapunov function). Under (CT1)–(CT3-D) and (M0), the state is ultimately bounded:

$$\limsup_{t\to\infty} \lVert \xi(t) \rVert \;\leq\; \frac{\rho_\xi}{\lambda} \sqrt{\frac{m_2}{m_1}} \tag{CT-D}$$

and structural persistence (the ultimate bound fits within the contraction region $\mathcal{B}_R$) requires

$$\lambda R \sqrt{m_1/m_2} \;\gt\; \rho_\xi. \tag{CT-D-persist}$$

**Proof.** Compute $\dot V$. Because $M$ is state- and time-dependent,

$$\dot V = \xi^T \dot M \xi + 2\xi^T M \dot\xi = \xi^T \dot M \xi - 2\xi^T M F(\xi, t) + 2\xi^T M w(t).$$

The adjoint-of-Jacobian manipulation used in Lohmiller-Slotine's differential form applies to the **bilinear form** $\xi^T M \xi$ precisely when the *logarithmic norm* of $-F$ in the metric $M$ is negative. Specifically, using a first-order expansion at $\xi$:

$$\xi^T M F(\xi, t) = \xi^T M \int_0^1 \frac{\partial F}{\partial\xi}(s\xi, t)\,\xi\,ds,$$

which under (CT2) satisfies $2\xi^T M F(\xi, t) \geq 2\lambda\, \xi^T M \xi - \xi^T \dot M \xi$ (after integration of the CT2 inequality along the ray $s\xi$, $s \in [0, 1]$, using $F(0, t) = 0$ from CT1 and assuming convexity of $\mathcal{B}_R$). Substituting:

$$\dot V \leq -2\lambda\,\xi^T M \xi + 2\xi^T M w = -2\lambda V + 2\xi^T M w.$$

Cauchy-Schwarz in the $M$-inner product: $\xi^T M w \leq \lVert\xi\rVert_M \lVert w\rVert_M \leq \sqrt{m_2}\,\lVert\xi\rVert_M \lVert w\rVert$ (with $\lVert\cdot\rVert_M^2 = \cdot^T M \cdot$ and $\lVert w\rVert_M^2 \leq m_2 \lVert w\rVert^2$).

Writing $W = \sqrt V = \lVert\xi\rVert_M$:

$$\dot W = \dot V/(2W) \leq -\lambda W + \sqrt{m_2}\,\rho_\xi$$

so $\limsup W \leq \sqrt{m_2}\rho_\xi / \lambda$. Converting back to Euclidean norm via (M0): $\lVert\xi\rVert \leq W/\sqrt{m_1}$, giving (CT-D). Persistence requires the Euclidean bound $\lVert\xi\rVert \leq R$, i.e., $\sqrt{m_2/m_1}\,\rho_\xi/\lambda \lt R$. $\square$

**Recovery of (T2).** When $M \equiv I$ (Euclidean metric, time-independent), (CT2) reduces to $-\partial F/\partial\xi - (\partial F/\partial\xi)^T \preceq -2\lambda I$, which is the **incremental Euclidean sector condition** (strong monotonicity of $F$ in Euclidean norm). This implies the one-point sector condition $\xi^T F(\xi) \geq \lambda \lVert\xi\rVert^2$ (integrating along $s\xi$), so $\alpha = \lambda$ when $M = I$. The template's ultimate bound $\rho/\alpha$ is reproduced with $m_1 = m_2 = 1$.

But (CT2) with $M = I$ is **strictly stronger than (T2)** — it requires the Jacobian's symmetric part to be uniformly positive definite, equivalent to `#form-composition-closure`'s DA2'-inc (strong monotonicity), not just (T2) (one-point sector). This is the key structural observation: the contraction formulation *collapses (T2) and DA2'-inc into one condition* at the cost of requiring differential (Jacobian-level) rather than integral (inner-product-at-a-point) information.

### 1.3 The contraction template — Model S

*[Result (contraction-template-S, conditional on CT1, CT2, CT3-S, M0, + Itô-compatible metric)]*

Under stochastic disturbance $d\xi = -F(\xi, t)\,dt + \sigma_\xi\,dW_t$, and with a metric $M$ satisfying additionally the Itô correction bound $\tfrac{1}{2}\sigma_\xi^2\,\mathrm{tr}(M + \text{Hessian correction}) \leq c_{\text{Itô}}\,m_2$ locally (automatic when $M$ is state-independent or has bounded state-derivatives in the drift direction), the stopped process satisfies the Grönwall bound

$$\mathbb{E}[V(\xi(t \wedge \tau_R), t \wedge \tau_R)] \leq V(\xi(0), 0)\,e^{-2\lambda t} + \frac{n\sigma_\xi^2\, c_{\text{Itô}}\, m_2}{2\lambda},$$

with stopping time $\tau_R = \inf\{t: \lVert\xi(t)\rVert \gt R\}$. The mean-square persistence condition becomes

$$\lambda R^2 \gt \frac{n\sigma_\xi^2\, c_{\text{Itô}}\, m_2^2}{2 m_1}. \tag{CT-S-persist}$$

This is the natural extension of Prop A.1S under a weighted metric. When $M \equiv I$, it reduces to the region-aware Prop A.1S (Khasminskii 2012 ch. 5). The extra $c_{\text{Itô}}$ factor captures the Itô-correction dependence on $M$'s curvature — it is 1 for constant metrics and bounded by the Hessian of $M$ in the drift direction otherwise.

### 1.4 What the contraction formulation gains

The **single substantive gain** of the contraction formulation over (T2) is **metric freedom**. Instead of requiring $F$ to point inward in Euclidean geometry, it requires $F$ to be contracting in *some* geometry — the geometry itself can be chosen to match the dynamics. Five specific wins:

- (G1) **Natural gradient dynamics** (`#emp-update-gain` with Fisher-information preconditioner): $F = \eta\,\mathbf{I}(\theta)^{-1}\nabla L(\theta)$ on an exponential-family natural parameter $\theta$. Euclidean sector fails in general (Fisher can be ill-conditioned, so $(\nabla L)^T (F) \neq \Theta(\lVert\nabla L\rVert^2)$). Fisher-metric contraction works: $M = \mathbf{I}(\theta)$, contraction rate $\lambda = \eta\mu_L$ where $\mu_L$ is $\nabla^2 L$'s lower bound in the Fisher metric (i.e., Riemannian strong convexity).

- (G2) **Hessian-metric gradient flow on non-Euclidean strongly convex losses.** If $L$ is $\mu$-strongly convex in the Hessian-induced norm (but not necessarily in Euclidean), $M = \nabla^2 L$ gives $\lambda = \eta\mu$ directly. Euclidean A2' would need condition-number degradation.

- (G3) **Matrix Kalman without $\kappa(P^-)$ degradation.** `#der-gain-sector-bridge`'s weighted-norm subtlety is exactly this: the natural metric is $M = (P^-)^{-1}$. Stating the contraction result in $M$ avoids the Euclidean transfer that introduced $\kappa(P^-)$.

- (G4) **Logarithmic-norm machinery for nonlinear control.** PID on a bounded Lipschitz nonlinearity: the Jacobian is affine in the gains; contraction holds in a metric $M$ solving a Lyapunov equation tuned to the plant's nonlinearity cone. Euclidean sector is regime-specific; contraction under an appropriate $M$ can be global.

- (G5) **Compositional closure without incremental sector bound upgrade.** Parallel and hierarchical composition preserve contraction under independent contraction metrics (Slotine 2003 Thm 2 sq.); one does not have to re-prove DA2'-inc at the composite level. Addressed in §4.

---

## §2. Sub-scope α promotion under the metric formulation

### 2.1 Kalman / conjugate Bayesian

**Linear-Gaussian Kalman filter**, scalar or matrix. The information-form recursion is:

$$P_{t\mid t}^{-1} = P_{t\mid t-1}^{-1} + H^T R^{-1} H,$$

with state-estimate error dynamics $\dot{\tilde x} = -K H \tilde x + (\text{noise})$. Under the metric $M = (P^-)^{-1}$ (information matrix), the Jacobian of the correction is $-KH = -P^- H^T R^{-1} H$, which in the $M$-weighted sense has

$$M \cdot (-KH) + (-KH)^T M = -(P^-)^{-1} P^- H^T R^{-1} H - H^T R^{-1} H (P^-)^{-1} P^- = -2 H^T R^{-1} H \preceq 0.$$

Strongly speaking, this shows the information-metric contraction rate $\lambda = \lambda_{\min}(H^T R^{-1} H) / 2$ for the observable subspace. In the observable subspace this is uniformly positive; in the unobservable subspace contraction is zero (as expected — Kalman cannot estimate unobservable modes).

**Outcome:** Kalman promotes to contraction-metric α *trivially* in the information metric, recovering the natural non-Euclidean geometry (G3). The condition-number degradation $\kappa(P^-)$ disappears.

### 2.2 Conjugate Bayesian / exponential-family in natural parameters

**Setup.** Exponential family $p(x \mid \theta) = h(x) \exp(\theta^T T(x) - A(\theta))$ with natural parameter $\theta$ and log-partition $A$. The Fisher information is $\mathbf{I}(\theta) = \nabla^2 A(\theta)$. The natural-gradient update with learning rate $\eta$ is $\dot\theta = -\eta\,\mathbf{I}(\theta)^{-1}(\theta - \theta^\ast)$ around a Bayesian-posterior target $\theta^\ast$ (equivalent form of the natural-parameter update, see Amari-Nagaoka 2000 §2.5). The Jacobian is $-\eta \mathbf{I}(\theta)^{-1}$.

Under the metric $M = \mathbf{I}(\theta)$ (Fisher metric):

$$M \cdot (-\eta \mathbf{I}(\theta)^{-1}) + (-\eta\mathbf{I}(\theta)^{-1})^T M = -2\eta I,$$

so the contraction rate $\lambda = \eta$ in the Fisher metric, *globally on the interior of the natural-parameter domain*, provided $\mathbf{I}$ is uniformly bounded (which it is on any compact subset of the interior). The Euclidean A2' entry of `#der-gain-sector-bridge` reads $\alpha = \eta \cdot \lambda_{\min}(\text{Fisher})$, which degrades as the Fisher spectrum spreads — Fisher-metric contraction removes this degradation.

**Outcome:** Exponential-family-in-natural-parameters promotes to contraction-metric α *strictly better* than its current Euclidean α. The contraction rate is the *learning rate itself*, independent of Fisher conditioning.

### 2.3 Strongly-convex gradient descent — two cases

**Case (a): Euclidean-strongly-convex.** $L$ is $\mu$-strongly convex in Euclidean norm; $\nabla^2 L \succeq \mu I$ globally. Under $M = I$, contraction holds with $\lambda = \eta\mu$ — same as the current `#der-gain-sector-bridge` α, no gain. But this is the weaker case.

**Case (b): Hessian-metric-strongly-convex.** $L$ is strongly convex in the Hessian-induced norm (a looser condition than Euclidean strong convexity for ill-conditioned problems). Under $M = \nabla^2 L$ (with a regularity condition that $M$'s state-derivative in the dynamics direction is bounded), contraction holds with $\lambda = \eta$. This is the (G2) gain.

**Outcome:** Gradient descent promotes under the Hessian metric; the gain is for ill-conditioned problems, where Euclidean strong convexity degrades by the condition number but Hessian-metric contraction does not.

### 2.4 L2-regularized convex

**Setup.** $L = L_0 + \tfrac{\lambda_{\text{reg}}}{2}\lVert\theta\rVert^2$ with $L_0$ convex (not necessarily strongly). $\nabla^2 L \succeq \lambda_{\text{reg}} I$.

**Euclidean case:** contraction rate $\eta \lambda_{\text{reg}}$ globally. No improvement over Euclidean (the regularizer makes the problem Euclidean-strongly-convex to start).

**Fisher-metric case (if the model is a parametric probabilistic model):** the regularizer + Fisher gives combined metric $\lambda_{\text{reg}} I + \mathbf{I}(\theta)$, contraction rate $\eta \cdot \min(\lambda_{\text{reg}}, \eta)$ in the combined metric. Usually no gain over Euclidean.

**Outcome:** L2-regularized convex lands at the same place under metric formulation as under Euclidean — regularization is already doing the work.

### 2.5 Linear with PD gain-observation product

**Setup.** Linear correction $F(\xi) = KH\xi$ with $KH \succ 0$ on the observable subspace. Euclidean sector gives $\alpha = \lambda_{\min}^+(KH)$ in the observable subspace.

**Metric formulation.** If $KH$ is symmetric, $M = I$ works with $\lambda = \lambda_{\min}^+(KH)$ (same as Euclidean). If $KH$ is *non-symmetric* (the general case — `K` and `H` need not commute), Euclidean sector requires the symmetric part $\tfrac{1}{2}(KH + H^T K^T) \succ 0$, which can fail even when $KH$ has positive spectrum (asymmetric matrices can have positive eigenvalues but negative symmetric part).

The **Lyapunov metric** $M$ solving $M(KH) + (KH)^T M = I$ restores contraction when $KH$ is Hurwitz-stable (all eigenvalues in the right-half plane). The contraction rate is $\lambda = \lambda_{\min}(M^{-1})/2$ in the $M$-metric. **This genuinely buys agents that the Euclidean formulation misses:** asymmetric-but-stable linear corrections.

**Outcome:** Linear-PD generalizes to *linear-Hurwitz-stable* under the metric formulation. This is a strict extension of the sub-scope α coverage.

### 2.6 Summary — the α sub-scope

Under contraction metrics, the current sub-scope α:

| Agent class | Euclidean A2' coverage | Contraction-metric $(M, \lambda)$ coverage |
|---|---|---|
| Scalar Kalman | Global | Global (trivial) |
| Matrix Kalman | Observable subspace, $(P^-)^{-1}$-weighted; $\kappa$ degraded to Euclidean | Information metric, **no condition-number degradation** |
| Conjugate Bayesian (exp family, natural params) | $\eta \lambda_{\min}(\text{Fisher})$ globally | Fisher metric, rate $\eta$ globally (**Fisher-conditioning removed**) |
| Gradient on strongly convex (Euclidean) | $\eta\mu$ globally | Same ($M = I$); no gain |
| Gradient on strongly convex (Hessian-induced) | Degraded by condition number | Hessian metric, rate $\eta$ globally (**gain for ill-conditioned**) |
| L2-regularized convex | $\eta\lambda_{\text{reg}}$ globally | Same |
| Linear PD gain-observation | $\lambda_{\min}^+(KH)$ on observable subspace | — |
| **Linear Hurwitz-stable (non-symmetric $KH$)** | **Fails Euclidean** | **Lyapunov-metric contraction — NEW COVERAGE** |

The gains are: (i) Kalman/exp-family lose their condition-number penalties, (ii) Hessian-metric strongly-convex-beyond-Euclidean enters, (iii) linear-Hurwitz non-symmetric enters.

---

## §3. Sub-scope β — the hard question

### 3.1 Prior constraint

`#deriv-sector-condition`'s β entries: PID with fixed gains, rule-based, human judgment, severely misspecified, variational approximation, non-convex beyond basin, per-step SGD. The question: **which of these promote to metric-α under *some* contraction metric?**

### 3.2 PID with bounded plant nonlinearity

**Setup.** PID controller $u = -K_p e - K_i \int e - K_d \dot e$ on a plant $\dot x = f_{\text{plant}}(x) + b u + w$ where $e = x - x^\ast$, $f_{\text{plant}}$ is Lipschitz with bounded Jacobian $\lVert\partial f_{\text{plant}}/\partial x\rVert \leq L_p$. State $\xi = (e, \int e, \dot e)$ (or the minimal state form equivalent).

The closed-loop Jacobian is $A_{\text{cl}}(x) = A_{\text{nom}} + \Delta(x)$ where $A_{\text{nom}}$ is the linearized nominal system (Hurwitz by PID tuning) and $\Delta(x)$ is the plant nonlinearity's deviation from its linearization, bounded by $\lVert\Delta\rVert \leq L_p$ in Euclidean.

**Euclidean sector fails** in general: the symmetric part of $A_{\text{cl}}(x) + A_{\text{cl}}(x)^T$ can be indefinite outside a basin because $\Delta(x)$'s symmetric part can dominate $A_{\text{nom}}$'s symmetric part if $L_p$ is large.

**Lyapunov-metric approach.** Solve $M A_{\text{nom}} + A_{\text{nom}}^T M = -Q$ for a chosen $Q \succ 0$. The closed-loop contraction in the $M$-metric:

$$M A_{\text{cl}}(x) + A_{\text{cl}}(x)^T M = -Q + M \Delta(x) + \Delta(x)^T M.$$

Contraction in the $M$-metric holds iff $\lVert M\Delta(x) + \Delta(x)^T M\rVert \lt \lambda_{\min}(Q)$. With $\lVert\Delta(x)\rVert \leq L_p$, the sufficient condition is $2 L_p \lVert M\rVert \lt \lambda_{\min}(Q)$, equivalently $L_p \lt \lambda_{\min}(Q) / (2 \lambda_{\max}(M))$.

**What this buys.** The Euclidean A2' for PID would require the symmetric part of $A_{\text{cl}}(x)$ to be uniformly negative-definite — a tight condition that fails for generic plants. The Lyapunov-metric condition requires only that the nominal design be Hurwitz-stable (standard PID design) *and* that the plant Lipschitz constant be below a specific threshold. For well-tuned PID on a Lipschitz plant, **this is a derivation, not an assumption**.

**Outcome: PID moves from sub-scope β to sub-scope metric-α,** conditional on the plant Lipschitz bound $L_p \lt \lambda_{\min}(Q)/(2\lambda_{\max}(M))$. This is a genuine promotion — previously A2' was an empirical posit; now it is derivable from PID-tuning-plus-plant-Lipschitz.

**Scope statement.** PID-with-bounded-plant-nonlinearity is *sub-scope metric-α₂* (new label): metric-contraction derived, not assumed, under plant-Lipschitz bound. Badly-tuned PID (nominal $A_{\text{nom}}$ not Hurwitz) remains β; aggressively nonlinear plants ($L_p$ exceeding the threshold) remain β.

### 3.3 Variational / approximate posteriors

**Setup.** Agent runs variational Bayesian update $q_t(\theta) \approx p_t(\theta \mid \text{data})$ via gradient descent on variational free energy $\mathcal{F}(q) = \mathbb{E}_q[-\log p(\text{data} \mid \theta)] + \mathrm{KL}[q \mid\mid p_{\text{prior}}]$.

**Obstruction.** The *true* gradient points toward $p_t$ (posterior); the *approximation-restricted* gradient points toward the best-in-class $q_t^\ast$, which can differ from $p_t$ by a projection error. B1 (directional fidelity) fails when the restriction class rotates the gradient significantly.

**Metric approach?** Under the Fisher metric of the *variational family* (not the true posterior), natural-gradient VI contracts to $q_t^\ast$ at rate $\eta$ — this is the same structural argument as (G1)/(2.2). **But this contracts to the *projected* target, not the true posterior.** The residual projection error is the variational gap $\text{KL}[q_t^\ast \mid\mid p_t]$, which is not reduced by contraction in the variational metric.

**Outcome: variational stays in β, sharpened.** The correct decomposition is:
- Contraction to $q_t^\ast$ holds under the variational-family Fisher metric (derivable, metric-α₂ to within the family).
- The residual $\text{KL}[q_t^\ast \mid\mid p_t]$ is a *projection-error disturbance* to the primary dynamics, not a contraction failure.

The honest landing is that **contraction metrics solve the within-family convergence**, but the variational error is a separate issue that contraction does not address. Sub-scope β is retained because the persistence-relative-to-$p_t$ claim is what AAD actually needs, and that requires bounding the residual — a different problem.

### 3.4 Non-convex gradient beyond basin

**Setup.** $L$ non-convex globally but locally strongly convex in some basin $\mathcal{B}$. Euclidean sector fails on $\mathcal{B}^c$; contraction-metric formulation?

**Answer:** contraction metrics *can* be globally valid in non-convex cases, *if* a valid metric exists — but constructing one for non-convex $L$ reduces to the converse-Lyapunov problem. Lohmiller-Slotine's theorem is: if the system is globally exponentially stable, then a valid $M$ exists. Finding $M$ constructively is the hard part.

**What can be said honestly.** For specific non-convex structures (e.g., saddle-free Newton on benign non-convexity), local metrics composable over basins can give a **basin-chart structure**: metric-α within each basin, structural-adaptation trigger at basin boundaries (the *separatrix* of the gradient flow).

**Outcome: partial promotion.** Non-convex gradient within a basin is metric-α₂ with basin-specific $M$; crossing a separatrix remains the `#result-structural-adaptation-necessity` trigger. The contraction-metric formulation does not escape `#result-structural-adaptation-necessity` — but it makes the basin structure explicit.

### 3.5 Rule-based agents

**Hard barrier.** Rule-based agents have non-smooth, often non-continuous dynamics. The differential condition (CT2) requires $C^1$ smoothness of $F$. Subdifferential extensions of contraction analysis exist (Di Bernardo et al. 2014, "Contraction in switched systems," *Automatica*) but apply to piecewise-smooth systems, not arbitrary rules.

**Outcome: rule-based stays firmly in β.** Contraction metrics do not help; the fundamental obstruction is smoothness, not metric choice. A possible separate extension via piecewise-contraction would cover switched controllers (a narrow slice of rule-based agents), but general rule-based reasoning does not admit the differential framework.

### 3.6 Per-step SGD / severely misspecified / human judgment

**Per-step SGD.** Euclidean A2' holds in expectation; per-step noise enters as effective disturbance (same structure under metric formulation; no help). Contraction metrics do not buy anything beyond expectation; the noise treatment is identical.

**Severely misspecified.** B1 fails at the objective level — the correction aims at the wrong target. Contraction to a wrong target is still wrong. **Contraction metrics address convergence geometry, not target validity.** Stays in β.

**Human judgment.** No formal update rule to evaluate (CT2) against. Stays in β.

### 3.7 β promotion summary

| Agent class | Under contraction metric | Notes |
|---|---|---|
| PID with bounded plant nonlinearity | **β → metric-α₂** | Derivable under plant-Lipschitz threshold |
| Variational approximate posteriors | Stays β | Contraction to projected target is derivable; residual projection error is separate |
| Non-convex beyond basin | **β → metric-α₂ within basin** | Basin-chart structure; basin boundaries = `#result-structural-adaptation-necessity` trigger |
| Rule-based | Stays β | Smoothness obstruction |
| Per-step SGD | Stays β (identical treatment) | Noise treated as disturbance regardless |
| Severely misspecified | Stays β | Target-validity problem, not geometry |
| Human judgment | Stays β | No formal update rule |

**Net β promotion:** two items (PID, non-convex-within-basin) gain derivation; the rest retain their β status. This is a substantive but bounded gain.

---

## §4. Compositional contraction — the big prize

### 4.1 Slotine's compositional theorems (summary)

Following Lohmiller & Slotine 1998 §3 and Slotine 2003, contraction is preserved under three composition operations:

- **Parallel (product) composition.** If systems 1 and 2 each contract under metrics $M_1, M_2$ at rates $\lambda_1, \lambda_2$, then the product system $\dot x = (\dot x_1, \dot x_2)^T$ with coupling $(f_1(x_1), f_2(x_2))^T$ contracts under $M = \mathrm{blockdiag}(M_1, M_2)$ at rate $\min(\lambda_1, \lambda_2)$.

- **Hierarchical / cascade composition.** If $\dot x_1 = f_1(x_1)$ contracts at rate $\lambda_1$, and $\dot x_2 = f_2(x_1, x_2)$ contracts in $x_2$ at rate $\lambda_2$ uniformly in $x_1$, with coupling gain $\lVert\partial f_2/\partial x_1\rVert \leq k$, then the cascade contracts. With $\lambda_2 \gt \lambda_1$ and a suitable weighted metric, the cascade rate is $\min(\lambda_1, \lambda_2)$. The coupling gain $k$ enters only the Lyapunov-equation constants, not the asymptotic rate.

- **Negative feedback with bounded loop gain.** If two systems contract at $\lambda_1, \lambda_2$ and are connected by negative feedback with loop gains $k_{12}, k_{21}$, the closed loop contracts iff $k_{12} k_{21} \lt 4\lambda_1\lambda_2$ (small-gain, Slotine 2003 Thm 3).

These are **strict generalizations** of what `#form-composition-closure` currently gets via the weakest-link bound (WL) and `#deriv-critical-mass-composition`'s (CM2) for the matched-symmetric dyad.

### 4.2 Lift into `#form-composition-closure`

The current bridge-lemma statement requires DA2'-inc (strong monotonicity of $F_c$) at the *composite* level, proved for Tier 1 and conditional for Tier 2/3. Under the metric formulation:

**Proposed lift.**

- Each sub-agent has an individual contraction metric $M_i$ and rate $\lambda_i$ (its A2' sub-scope α entry, promoted to metric α₁/α₂ per §2/§3).
- The **composite contraction metric** is constructed compositionally from sub-agent metrics per the topology:
  - Parallel: $M_c = \mathrm{blockdiag}(M_1, \ldots, M_N)$, rate $\min_i \lambda_i$.
  - Cascade: weighted block-lower-triangular $M_c$, rate $\min_i \lambda_i$ up to coupling-gain-dependent adjustment.
  - Feedback: small-gain with $M_c$ derived from Slotine 2003's construction, rate from loop-gain inequality.
- The **composite bridge lemma follows directly** from the composite contraction: trajectory-error bound is $\varepsilon^\ast \nu_c / \lambda_c$ in the composite metric, with ultimate Euclidean bound degraded by $\sqrt{m_{2,c}/m_{1,c}}$.

This is a **topology-indexed closure result**. The tier structure degrades from "Tier 1/2/3 depending on sub-agent type" to "topology-indexed: parallel / cascade / feedback / general-graph." Each topology has a specific compositional-contraction rate derivation; general-graph composites require either Slotine-Lohmiller-Wang's "virtual systems" technique or remain open.

### 4.3 Generalization of `#deriv-critical-mass-composition` (CM2)

The matched-symmetric-Tier-1 closed form (`#deriv-critical-mass-composition` (CM2)):

$$(\alpha - C) R \gt \rho + \gamma\mathcal{T}$$

is a *parallel-composition-with-feedback-coupling* special case. The generalization under Slotine 2003's negative-feedback-with-bounded-gain theorem:

$$(\lambda_1 - C_1)(\lambda_2 - C_2) \gt k_{12} k_{21} / 4 \tag{CM2-M}$$

for heterogeneous sub-agents with metric-contraction rates $\lambda_1, \lambda_2$, coordination costs $C_1, C_2$, and feedback loop gains $k_{12}, k_{21}$. Specializing to the symmetric case ($\lambda_1 = \lambda_2 = \lambda$, $C_1 = C_2 = C$, $k_{12} = k_{21} = k$):

$$(\lambda - C)^2 \gt k^2/4 \;\;\Leftrightarrow\;\; \lambda - C \gt k/2,$$

which matches `#deriv-critical-mass-composition`'s form (setting $k = \gamma\mathcal{T}/R \cdot 2$, adjusting normalization).

**Gain:** (CM2-M) is **heterogeneous** — sub-agents need not have matched architectures or sector constants. The critical-mass inequality lifts to a genuine $N$-agent result via the iterative small-gain construction (Slotine 2003 §IV). Heterogeneous teams get a derivation.

### 4.4 Bridge-lemma upgrade — honest statement

**Pre-contraction-metric state:** Bridge lemma is derived for Tier 1 (DA2'-inc global), local for Tier 2, discussion-grade for Tier 3.

**Post-contraction-metric state:** Bridge lemma is derived for:
- **Tier 1M (metric-contraction-global):** Kalman / exp-family / strongly-convex / L2-regularized / linear-Hurwitz. Global contraction in a specified metric. Composite bridge lemma via §4.1 compositional theorems.
- **Tier 2M (metric-contraction-basin):** PID-with-bounded-plant-Lipschitz / non-convex-within-basin. Contraction in basin-specific metric. Composite bridge lemma valid in the intersection-of-basins, with basin-crossing as structural-adaptation trigger.
- **Tier 3M (no global metric):** Rule-based / variational / severely-misspecified. Bridge lemma remains discussion-grade; `#disc-separability-pattern`'s "general open" entry.

**Net:** Tier 1 absorbs metric-α₁ and metric-α₂ cases; Tier 2 becomes basin-chart structure; Tier 3 shrinks to the cases where metric formulation genuinely fails. The three-part `#disc-separability-pattern` shape is preserved with the separable-core expanded and the structured-repair layer made more explicit (basin-chart).

### 4.5 Heterogeneous composition — the composition bridge lemma

**Current state:** `#form-composition-closure`'s composite (A4) from sub-agent properties is the weakest-link bound (WL), refined by `#deriv-critical-mass-composition` (CM2) only for matched-symmetric-Tier-1.

**Proposed upgrade.** Given heterogeneous sub-agents each in Tier 1M or Tier 2M with individual $(M_i, \lambda_i, R_i)$, the composite metric and rate follow compositionally from the topology:

- **Parallel topology:** $M_c = \bigoplus_i M_i$, $\lambda_c = \min_i \lambda_i$, $R_c = \min_i R_i$.
- **Cascade topology:** $M_c = \bigoplus_i w_i M_i$ with weights $w_i$ solving a cascade Lyapunov equation (Slotine 2003 Thm 2); $\lambda_c$ is bounded below by the weakest stage up to coupling-gain adjustment.
- **Negative-feedback topology (2-agent):** small-gain (CM2-M); rate determined by the loop-gain inequality.
- **General directed-graph topology:** Slotine 2003 §IV's virtual-system construction, conditional on loop gains along every cycle satisfying small-gain.

This is the **composition bridge lemma under contraction metrics.** It generalizes `#deriv-critical-mass-composition` from matched-symmetric-Tier-1 (the current closed form) to heterogeneous sub-agents under a characterized set of topologies. The composite bridge lemma becomes topology-indexed rather than tier-indexed.

---

## §5. A2' partition redrawn under the metric formulation

### 5.1 Current partition (from `#deriv-sector-condition`)

- **Sub-scope α (A2' derived):** Kalman / conjugate Bayesian / exp-family-natural-params / strongly-convex gradient / L2-regularized / linear-PD.
- **Sub-scope β (A2' assumed):** PID / rule-based / human-judgment / severely-misspecified / variational / non-convex-beyond-basin / per-step-SGD.

### 5.2 Proposed refined partition under metric formulation

- **Sub-scope metric-α₁ (Euclidean metric, one-point sector):** the Euclidean cases where nothing changes — Euclidean strongly-convex gradient, L2-regularized, scalar Kalman. The existing Euclidean A2' is the contraction-metric statement with $M = I$.

- **Sub-scope metric-α₂ (non-Euclidean metric, derived):** cases where a non-Euclidean metric is the natural contraction witness — matrix Kalman under information metric, exp-family under Fisher metric, Hessian-metric strongly-convex gradient, linear-Hurwitz-non-symmetric under Lyapunov metric, PID-with-bounded-plant under Lyapunov metric, non-convex-within-basin under basin-specific metric.

- **Sub-scope metric-β (metric formulation fails):** variational (contraction to wrong target), rule-based (non-smooth), severely misspecified (target-wrong), human judgment (no rule), per-step SGD (identical treatment).

### 5.3 What moves from β to α

Two items promote: **PID-bounded-plant** (metric-α₂ derived) and **non-convex-within-basin** (metric-α₂ within the basin).

Four items stay β: variational, rule-based, severely-misspecified, human-judgment.

One item is structurally unchanged: per-step SGD (noise-is-disturbance treatment identical under Euclidean and metric formulations).

### 5.4 How this interacts with `#disc-separability-pattern`

`#disc-separability-pattern`'s "A2' sub-scope partition is a binary special case" observation (its own §Discussion) becomes **three-part** under the metric formulation:

- Separable core: metric-α₁ (Euclidean metric, trivial).
- Structured repair: metric-α₂ (specific non-Euclidean metric derived under explicit conditions — basin-Lipschitz, plant-Lipschitz, Fisher-conditioning).
- General open: metric-β (smoothness / target-validity obstructions).

This is the **third part that `#disc-separability-pattern` flagged as missing** in its §Discussion under A2'. The metric formulation supplies it: the structured-repair tier is "derive contraction in a problem-appropriate metric, under stated conditions on smoothness / Lipschitz / basin structure."

**Consequence:** A2' now fits `#disc-separability-pattern` as a proper three-tier ladder, making it **the seventh ladder** in the six-ladder enumeration (Correlation, Convention, Architecture, Contraction, Identification-regime, Scope-hierarchy + **A2'-scope**).

---

## §6. Honest failure modes

Attempting the improbable first (as instructed), the spike pushed to find cases contraction metrics cover. The following are honest failures where the framework does NOT lift AAD's coverage:

### 6.1 Non-smooth dynamics

Rule-based agents, state-machine controllers, threshold-triggered switches, and discontinuous policies fail the $C^1$ requirement of Lohmiller-Slotine. Piecewise-contraction extensions (Di Bernardo et al. 2014) cover switched linear systems but not general rule-based reasoning. **This is a genuine barrier, not a technicality.** The contraction-metric formulation is fundamentally differential; non-smooth systems need set-valued / non-smooth analysis machinery (Clarke calculus, measure differential inclusions) that sits outside Section III's current scope.

### 6.2 Strategic (game-theoretic) equilibria

Two adversarial agents have joint dynamics with mixed-strategy Nash equilibria — fixed points of the best-response map, not fixed points of dynamics. Contraction analysis requires attracting fixed points; strategic equilibria can be saddle points (non-attracting) of the dynamics even when they are unique Nash equilibria. Game theory's fictitious-play / gradient-ascent-descent for saddle-finding is not contracting.

**This is `#der-adversarial-destabilization`'s non-linearity problem** restated — adversarial dynamics are generically *not* contracting in any metric. Slotine's machinery extends to cooperative multi-agent systems; it does not cover adversarial equilibria. The `#deriv-critical-mass-composition` adversarial regime ($\gamma \gt 0$, destabilization) is precisely where the contraction-metric picture fails.

**Honest landing:** contraction metrics cover the **cooperative half** of multi-agent Section III (`#der-team-persistence`, cooperative `#deriv-critical-mass-composition`, cooperative `#form-composition-closure`). Adversarial Section III (`#der-adversarial-destabilization`, `#result-adversarial-tempo-advantage`) is structurally outside — it needs the differential-game / monotone-operator-but-not-contracting apparatus.

### 6.3 Stochastic forcing (actually partial — Pham-Slotine exists)

Pham & Slotine 2007 ("Stable concurrent synchronization in dynamic system networks," *Neural Networks* 20:62–77) extends contraction to stochastic systems with small-noise bounds. The stochastic Model S extension (§1.3 above) is valid under their framework, subject to the Itô-compatibility condition $c_{\text{Itô}}$ that requires bounded metric-Hessian in the drift direction.

**Obstruction is not total** — but it is real for state-dependent metrics ($M$ depending strongly on $\xi$). Constant-metric contraction (Lyapunov-metric for Hurwitz linear, Fisher metric far from parameter-space boundary) is unaffected. State-dependent-metric contraction in stochastic regimes requires per-case verification.

### 6.4 Time-varying systems with fast metric variation

$M(\xi, t)$ time-varying introduces the $\dot M$ term in (CT2). When $M$'s time-variation is slow relative to the dynamics, this is absorbable (`#sketch-multi-timescale-stability` territory). When $M$ varies on the same timescale as $\xi$ (e.g., an adaptive-metric algorithm where $M$ is learned alongside $\xi$), the cross-coupling $\dot M$ can destabilize contraction. 

This is *exactly* the interaction `spikes/spike-adaptive-gain-dynamics.md` hit with the $\delta$-to-gain coupling in RMSProp (§4.3 of that spike): the meta-state (gain) feeds back into the primary state's contraction rate, and the coupled system requires a fixed-point closure argument. Under the metric formulation, the same issue recurs as metric-state coupling — a strictly genuine open item, not a metric-formulation failure per se, but a limit on how cleanly the metric formulation composes with adaptive-gain machinery.

### 6.5 Global contraction when basin-local only

The Lohmiller-Slotine theorem statement is "local contraction on a region implies local exponential stability." Global contraction requires a globally-valid metric. For agents with multiple basins of attraction (non-convex $L$ with multiple minima, multi-stable dynamical systems), no single global metric contracts — only basin-local metrics. The basin-chart picture (§3.4) covers this honestly, but it means the single-metric simplification of Slotine's theorems does not apply.

**Scope:** this is already visible in the current Section III through `#result-structural-adaptation-necessity`'s basin-boundary trigger. The metric formulation does not fix multi-basin structure; it makes the basin structure explicit.

### 6.6 Identifiability floor instances

The metric formulation operates **downstream of identification.** It assumes the correction function $F$ points in a valid direction (a B1-analog at the Jacobian level). If B1 fails (severe misspecification, unidentifiable meta-gain), the metric cannot recover — a wrong-direction correction in any metric is still wrong-direction. This is the `#disc-identifiability-floor` intersection: contraction metrics are silent on identification.

**Consequence:** the metric formulation and `#disc-identifiability-floor` are *orthogonal* architectural moves. Metric lifts the geometry-of-correction half of sub-scope α; identifiability-floor lives on the what-correction-to-make half. The metric formulation *cannot* escape identifiability-floor constraints.

---

## §7. Landing map — what lands where

Four promotion options, ranked:

### R1 (preferred): new meta-segment `#result-contraction-template`, retain `#result-sector-persistence-template`

**Create** `01-aad-core/src/result-contraction-template.md`, type:result, status:conditional, depending on `#deriv-sector-condition`, `#result-sector-persistence-template`, `#der-gain-sector-bridge`. The segment would:

1. State (CT1)–(CT3) as the metric-formulation preconditions.
2. Derive the ultimate-bound result (CT-D / CT-S) under (M0).
3. Prove that (CT2) with $M = I$ reduces to DA2'-inc (not (T2)) — making the relationship to the sector template precise.
4. Enumerate the §2 / §3 instances with their natural metrics and contraction rates.
5. Present the compositional theorems (§4.1) as a cross-reference / theorem-import from Slotine 2003.
6. State the compositional lift (§4.2 — topology-indexed bridge lemma, §4.3 — (CM2-M) heterogeneous critical-mass).
7. Document the failure modes (§6) honestly in a dedicated "Where the metric formulation does not lift AAD" section.
8. Cross-reference `#disc-separability-pattern` as the seventh ladder (A2'-scope with metric-α₁ / metric-α₂ / metric-β).

**Rationale:** the metric formulation is a genuine structural extension that deserves a segment rather than a paragraph. Retaining `#result-sector-persistence-template` parallel preserves the Euclidean-template narrative for readers who do not need the metric machinery and preserves the existing six instantiations as first-class items. `#result-contraction-template` sits as the more general form, with `#result-sector-persistence-template` as its $M = I$ specialization.

### R2: extend `#result-sector-persistence-template` with a "Metric-formulation extension" section

Add a §extension to `#result-sector-persistence-template` stating (CT2), the ultimate-bound result, and the three-or-four worked instances (Kalman-info-metric, Fisher, Lyapunov-PID). Compositional and tier-lift results would land separately in `#form-composition-closure` and `#deriv-critical-mass-composition`.

**Downside:** bloats `#result-sector-persistence-template` with a substantial new pattern that doesn't reduce to the existing preconditions cleanly. The compositional theorems (§4.1) are Slotine-theorem-imports that the template does not currently do — dedicated real estate is better.

### R3: add compositional-lift content to `#form-composition-closure` + `#deriv-critical-mass-composition` directly

Land §4.2 (topology-indexed bridge lemma) in `#form-composition-closure` as a new admissibility class; land (CM2-M) in `#deriv-critical-mass-composition` as a generalization. Leave the template unchanged.

**Downside:** the compositional results *rely* on the metric-template restatement, which under R3 lives nowhere. Orphaned derivation.

### R4: fold into `spikes/spike-bridge-lemma-contraction.md` and leave unpromoted

**Downside:** violates `feedback_math_lives_in_segments.md` — the metric-template restatement is substantive math. It belongs in a segment.

### Recommended: R1

A new meta-segment `#result-contraction-template` at type:result, status:conditional (conditional on the metric regularity + (CT1)–(CT3)). Status conditional — not exact — because the applicable metric must be specified per agent class, and the compositional results depend on Slotine 2003's theorems rather than being proved internal to AAD. Stage `draft` pending review.

**Dependent segment edits under R1:**

- `#result-sector-persistence-template`: add a one-paragraph "Relationship to `#result-contraction-template`" Discussion note pointing to the generalization.
- `#deriv-sector-condition`: extend the sub-scope partition to metric-α₁ / metric-α₂ / metric-β with cross-reference to `#result-contraction-template`. Extend the "What is derived vs chosen" table row on A2'.
- `#der-gain-sector-bridge`: clean up the "Weighted-norm subtlety" — move matrix-Kalman's $(P^-)^{-1}$-weighting to the information-metric statement in `#result-contraction-template`, removing the $\kappa(P^-)$ degradation.
- `#form-composition-closure`: add topology-indexed bridge-lemma results to the Tier-2-Tier-3 discussion; cross-reference Slotine 2003's compositional theorems.
- `#deriv-critical-mass-composition`: add (CM2-M) heterogeneous generalization; note that (CM2) is the matched-symmetric specialization.
- `#disc-separability-pattern`: promote A2'-scope from "binary special case" to a full seventh ladder (metric-α₁ / metric-α₂ / metric-β).
- `#der-adversarial-destabilization`: add a note in Working Notes that contraction metrics cover the cooperative half; adversarial remains in game-theoretic territory (§6.2).
- `#sketch-multi-timescale-stability`: add cross-reference to contraction-metric cascade composition as an alternative to singular-perturbation reduction (§6.4).

---

## §8. Honest epistemic assessment

### 8.1 What this spike achieves

1. **(CT1)–(CT3) preconditions + ultimate-bound result under (M0)** — Model D and Model S. Derivation under (M0) is a clean lift of the Grönwall argument to weighted norms. Strength: derived.

2. **§2 α sub-scope promotion.** Kalman / exp-family / Hessian-metric-convex / linear-Hurwitz-non-symmetric all admit natural contraction metrics with quantitatively better rates than their Euclidean counterparts. Strength: derived per case; the gains are concrete (removal of condition-number degradations, capture of asymmetric-stable systems).

3. **§3 β sub-scope promotion.** PID-bounded-plant and non-convex-within-basin promote to metric-α₂ under explicit conditions. Four β cases (variational, rule-based, severely-misspecified, human-judgment) do not promote. Strength: mixed — PID is a solid derivation, non-convex-within-basin introduces basin-chart structure that requires more formal treatment before promotion.

4. **§4 compositional lift.** Slotine 2003's three composition theorems import directly into Section III as the topology-indexed bridge lemma and the heterogeneous critical-mass generalization (CM2-M). Strength: derived via theorem-import, conditional on Slotine's theorems being correctly stated (which they are — Slotine 2003 is standard).

5. **§5 redrawn A2' partition.** metric-α₁ / metric-α₂ / metric-β as a proper three-tier scope partition, filling `#disc-separability-pattern`'s "A2' is binary" gap. Strength: structural/derived from §§2–3.

6. **§6 honest failure modes.** Non-smooth (rule-based), adversarial (strategic equilibria), state-dependent-metric stochastic, multi-basin, identifiability-floor intersection. These are genuine barriers, not softening retreats.

### 8.2 What this spike does NOT achieve

1. **Does not prove (CT2) from AAD-internal axioms.** (CT2) is a differential condition on $F$'s Jacobian; the B1 directional-fidelity axiom of `#der-gain-sector-bridge` is an integral (inner-product) condition. Bridging from B1 to (CT2) requires either (a) stronger B1 variants (Jacobian-level directional fidelity), or (b) relying on external-theorem-import for specific cases. The spike currently does (b); (a) is a candidate strengthening for follow-up work.

2. **Does not close adversarial composition** (§6.2). Contraction metrics cover cooperative multi-agent dynamics; adversarial dynamics need their own machinery. `#der-adversarial-destabilization`'s approach (coupling-amplified disturbance into the sector template) is the current AAD solution and remains the right tool for that regime.

3. **Does not eliminate the incremental-sector-bound requirement for `#form-composition-closure`** when (CT2) is *not* in hand. `#form-composition-closure`'s DA2'-inc remains the condition for Tier 1/2/3 when the metric formulation is not used. The lift adds a *route* (via metric contraction), not a *replacement*.

4. **Does not resolve metric-state coupling in adaptive-metric algorithms** (§6.4). The interaction with `spikes/spike-adaptive-gain-dynamics.md`'s (MG-4) coupling-boundedness is consistent but not tightened.

5. **Does not fix identifiability-floor instances** (§6.6). Metric formulation is geometry-of-correction; floor is what-correction-to-make. Orthogonal.

### 8.3 Tiering and confidence

| Claim | Tier | Confidence |
|---|---|---|
| (CT1)–(CT3) preconditions + (CT-D) / (CT-S) ultimate-bound results | Exact, conditional on (M0) | High (standard Lohmiller-Slotine + Grönwall) |
| Kalman info-metric contraction removes $\kappa(P^-)$ degradation | Derived | High |
| Exp-family Fisher-metric contraction at rate $\eta$ globally | Derived | High |
| Hessian-metric gain for ill-conditioned strongly-convex | Derived | High (standard natural-gradient) |
| Linear-Hurwitz-non-symmetric admits Lyapunov-metric contraction | Derived | High (standard Lyapunov theory) |
| PID-with-bounded-plant promotes under Lyapunov-metric | Derived, conditional on $L_p \lt \lambda_{\min}(Q)/(2\lambda_{\max}(M))$ | High |
| Non-convex-within-basin admits basin-chart structure | Robust qualitative | Medium (specific basin construction case-by-case) |
| Variational contraction is to *projected* target, not posterior | Derived | High (standard VI) |
| Rule-based / severely-misspecified / human-judgment do not promote | Robust qualitative (negative result) | High |
| Compositional theorems (parallel / cascade / negative-feedback) preserve contraction | Derived (theorem-import from Slotine 2003) | High |
| Topology-indexed bridge lemma in `#form-composition-closure` | Derived, conditional on compositional theorems | Medium (requires cleaning up the specific lift) |
| (CM2-M) heterogeneous critical-mass | Derived, conditional on small-gain theorem | High for 2-agent; requires Slotine 2003 §IV for N-agent |
| A2' three-tier partition metric-α₁ / metric-α₂ / metric-β | Robust qualitative | High (structural observation) |
| Adversarial dynamics are structurally outside metric scope | Robust qualitative | High (game-theoretic argument) |

### 8.4 Gain summary

**Net architectural move if R1 is adopted:**

- `#result-sector-persistence-template`'s six instantiations remain exactly as-is (Euclidean formulation preserved); a new more-general template `#result-contraction-template` sits alongside as the metric-formulation generalization.
- Sub-scope α gains metric-α₂ (information-metric Kalman, Fisher-metric exp-family, Hessian-metric strongly-convex, Lyapunov-metric linear-Hurwitz, Lyapunov-metric PID-bounded-plant, basin-chart non-convex-within-basin). Roughly **doubles the derived-A2' class.**
- Sub-scope β shrinks to the four cases where the metric formulation genuinely fails (variational, rule-based, severely-misspecified, human-judgment — all for distinct reasons named in §3).
- `#form-composition-closure` gets topology-indexed closure (parallel / cascade / feedback / general) via Slotine 2003 import. Tier 1/2/3 becomes Tier 1M / 2M / 3M with sharper tier boundaries.
- `#deriv-critical-mass-composition` (CM2) generalizes to (CM2-M) — heterogeneous sub-agents, not just matched-symmetric.
- `#disc-separability-pattern` gains a seventh ladder (A2'-scope), closing the binary-special-case gap flagged in its Discussion.
- `#der-adversarial-destabilization` remains the canonical tool for adversarial regimes; contraction metrics do not compete, they complement.

This is **a substantive architectural move** that lifts Section III's coverage from "linear-Kalman-centric with Tier 2/3 caveats" to "broadly-nonlinear-cooperative-via-Slotine-compositional-theorems with named honest failure modes." The Gemini gap is **substantially addressed** for the cooperative half of Section III; the adversarial half remains outside the metric framework by structural necessity, not by oversight.

### 8.5 Overall verdict

The contraction-metric generalization **works and is worth promoting** via R1. It is not a replacement for `#result-sector-persistence-template` — it is a generalization that preserves the existing template as its $M = I$ specialization. Its gains are concrete (removal of condition-number degradations, PID-derivation, heterogeneous-composition closure), and its failure modes are honest (non-smooth, adversarial, multi-basin — each for named structural reasons).

The spike's strongest claim is the **compositional lift** (§4) — Slotine 2003's three composition theorems give `#form-composition-closure` a topology-indexed closure result that the weakest-link bound (WL) and matched-symmetric (CM2) cannot match. This alone justifies promotion.

The spike's most honest retreat is **adversarial composition** (§6.2) — contraction metrics cover the cooperative half of Section III and no more. `#der-adversarial-destabilization`'s coupling-amplified-disturbance approach remains the adversarial-regime tool, and the metric-framework does not — cannot, in a structural sense — displace it.

The metric formulation does **not** resolve `#disc-identifiability-floor` instances, does **not** eliminate the need for basin-level analysis in non-convex cases, and does **not** make adaptive-metric algorithms clean. These are all honest limits that align with existing `#disc-separability-pattern` and `#disc-identifiability-floor` positioning.

---

## §9. Open questions after this spike

1. **Jacobian-level B1.** Can AAD's directional fidelity B1 (`#der-gain-sector-bridge`) be strengthened to a Jacobian-level condition that implies (CT2) directly, rather than requiring theorem-import for each case? This would make metric-α₂ derivation AAD-internal rather than via external-theorem dependency.

2. **General-graph composition.** Slotine 2003 §IV's virtual-system technique covers general directed graphs under a small-gain-along-every-cycle condition. Operationalizing this for `#form-composition-closure`'s general multi-agent setting — including identifying which cycle-gains to measure in practice — is a follow-up derivation.

3. **Adaptive-metric coupling.** The `spikes/spike-adaptive-gain-dynamics.md` (MG-1)–(MG-4) framework treats gain adaptation as a meta-state. Under the metric formulation, adapting $M$ itself is a meta-metric problem. Can (MG-2) — the meta-gain sector condition — be restated as a meta-metric contraction condition? This is Opus's "learning the metric" question.

4. **Finsler metrics.** Lohmiller-Slotine's differential contraction extends to Finsler metrics (Forni & Sepulchre 2014, "A differential Lyapunov framework for contraction analysis," *IEEE TAC* 59:614). Finsler is anisotropic (direction-dependent). Does Finsler buy AAD anything the Riemannian (quadratic) metric does not? Likely only for highly anisotropic corrections (e.g., coordinate-asymmetric agents); likely not priority.

5. **Connection to information geometry.** The Fisher-metric contraction for exp-family (G1) is a specific case of Riemannian contraction on statistical manifolds (Amari-Nagaoka 2000). Amari's α-connections give a one-parameter family of connections; each induces a different contraction metric. Is there an AAD-specific choice (e.g., the e-connection or m-connection) that is canonical? This is an interesting but non-critical question — the Fisher metric is the canonical Riemannian one, and other connections are compatible with it.

6. **Convergence-rate refinement.** `spikes/spike-critical-mass-composition.md`'s §Open items include rate-specific results. Contraction-metric formulation gives rate $\lambda$ directly; integrating with `#deriv-critical-mass-composition`'s convergence-rate open item may tighten both. Follow-up.

---

## §10. References

**Contraction analysis (primary):**
- Lohmiller, W. & Slotine, J.-J. E. (1998). "On contraction analysis for non-linear systems." *Automatica* 34(6):683–696.
- Slotine, J.-J. E. (2003). "Modular stability tools for distributed computation and control." *Int. J. Adapt. Control Signal Process.* 17(6):397–416. [compositional theorems: parallel, hierarchical, negative-feedback]
- Slotine, J.-J. E. & Wang, W. (2005). "A study of synchronization and group cooperation using partial contraction theory." In *Cooperative Control: A Post-Workshop Volume*, Springer. [group-synchronization results]
- Forni, F. & Sepulchre, R. (2014). "A differential Lyapunov framework for contraction analysis." *IEEE Trans. Automatic Control* 59(3):614–628. [Finsler metric extension]

**Stochastic contraction / Itô:**
- Pham, Q.-C. & Slotine, J.-J. E. (2007). "Stable concurrent synchronization in dynamic system networks." *Neural Networks* 20(1):62–77. [stochastic contraction under small noise]

**Non-smooth / switched contraction:**
- Di Bernardo, M., Liuzza, D. & Russo, G. (2014). "Contraction analysis for a class of nondifferentiable systems with applications to stability and network synchronization." *SIAM J. Control Optim.* 52(5):3203–3227.

**Information geometry / natural gradient:**
- Amari, S. & Nagaoka, H. (2000). *Methods of Information Geometry*. AMS / Oxford University Press.
- Amari, S. (1998). "Natural gradient works efficiently in learning." *Neural Computation* 10(2):251–276.

**Small-gain / interconnected-stability:**
- Jiang, Z.-P., Teel, A. R. & Praly, L. (1994). "Small-gain theorem for ISS systems and applications." *Math. Control Signals Syst.* 7:95–120.
- Sontag, E. D. (1989). "Smooth stabilization implies coprime factorization." *IEEE Trans. Automatic Control* 34:435–443.

**AAD segments referenced:**
- `#result-sector-persistence-template`, `#deriv-sector-condition`, `#der-gain-sector-bridge`, `#form-composition-closure`, `#deriv-critical-mass-composition`, `#disc-separability-pattern`, `#disc-identifiability-floor`, `#der-adversarial-destabilization`, `#sketch-multi-timescale-stability`, `#result-structural-adaptation-necessity`, `#deriv-discrete-sector-condition`.

**AAD spike trail:**
- `spikes/spike-bridge-lemma-contraction.md` (2026-04-06) — DA2'-inc and Tier 1/2/3.
- `spikes/spike-critical-mass-composition.md` (2026-04-22) — (CM2) matched-symmetric-Tier-1 closed form.
- `spikes/spike-adaptive-gain-dynamics.md` (2026-04-22) — (MG-1)–(MG-4) meta-gain sector conditions; relevant to §6.4 metric-state coupling.
- `spikes/spike-a2-prime-strengthening.md` — sub-scope α / β partition landing.

**Standard references already in `ref/INDEX.md`:**
- Khalil, H. K. (2002). *Nonlinear Systems*, 3rd ed. Ch. 4, 9, 11.
- Khasminskii, R. (2012). *Stochastic Stability of Differential Equations*, 2nd ed. Ch. 5.
- Nesterov, Y. (2004). *Introductory Lectures on Convex Optimization*. Thm 2.1.10.

---

*(End of spike.)*
