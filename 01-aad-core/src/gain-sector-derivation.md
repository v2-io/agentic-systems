---
slug: gain-sector-derivation
type: derivation
status: conditional
depends:
  - update-gain
  - sector-condition-derivation
stage: deps-verified
---

# Derivation: Gain-Sector Bridge — Proofs and Verification

Complete derivations for the results stated in #gain-sector-bridge: gain-based updating produces correction functions satisfying the sector condition (GA-3) whenever the update rule has directional fidelity. Covers the Kalman case (scalar and matrix), the general bridge theorem, the gradient-descent equivalence, and numerical verification.

## Motivation

#sector-condition-derivation proves persistence and stability downstream of the sector condition (GA-3): $\delta^T F(\mathcal{T}, \delta) \geq \alpha \lVert\delta\rVert^2$. The sector parameter $\alpha$ governs the persistence bound ($R^\ast = \rho/\alpha$), the adaptive reserve ($\Delta\rho^\ast = \alpha R - \rho$), and the adversarial scaling exponent. But whether the correction function $F$ induced by the gain principle ( #update-gain) actually satisfies GA-3 was not derived — GA-3 was the theory's softest structural joint.

This appendix closes the gap. For optimal Bayesian updates (Kalman, conjugate families), the bridge is exact: the sector parameter equals the gain. For gradient-based agents, GA-3 is equivalent to local strong convexity of the loss function. The load-bearing assumption shifts from "the correction function satisfies the sector condition" (opaque) to "the update rule has directional fidelity" (transparent, checkable).


## Proposition B.1: Scalar Kalman Sector Condition

**Statement.** For a scalar linear-Gaussian system ($n = m = 1$, $H = 1$) with Kalman filter gain $K = P^- / (P^- + R_{\text{obs}})$, the correction function $F(e) = K \cdot e$ satisfies the sector condition with:

*[Derived (scalar-Kalman-sector, from Kalman update)]*

$$\alpha = K = \frac{P^-}{P^- + R_{\text{obs}}} = \eta^\ast$$

The sector parameter equals the Kalman gain, which equals the uncertainty-ratio gain from #update-gain. The bound is tight (the correction is linear).

**Proof.** The scalar Kalman update for state estimate $\hat x$ given innovation $\delta = o - \hat x$ is $\hat x_\text{post} = \hat x_\text{prior} + K \delta$, where the gain is $K = P^- / (P^- + R_\text{obs})$ with $P^-$ the prior variance and $R_\text{obs}$ the observation noise variance.

The state-space estimation error $e = x - \hat{x}$ evolves under the correction step as:

$$e_{\text{post}} = e_{\text{prior}} - K(He_{\text{prior}} + \varepsilon) = (1 - K) e_{\text{prior}} - K\varepsilon$$

With $H = 1$, the expected correction function is $F(e) = K \cdot e$. The sector product is:

$$e \cdot F(e) = K \cdot e^2$$

Since $P^- \gt 0$ and $R_\text{obs} \gt 0$, we have $K \in (0, 1)$. The sector condition $e \cdot F(e) \geq \alpha \cdot e^2$ holds with $\alpha = K$. The bound is tight because the correction is exactly linear. $\square$

**Steady-state sector parameter.** At steady state (random walk dynamics, $A = 1$), the prior variance satisfies the algebraic Riccati equation. Solving $K^2 R_{\text{obs}} + QK - Q = 0$ (where $Q$ is the process noise variance) gives:

*[Derived (steady-state scalar sector parameter)]*

$$\alpha_{ss} = K_{ss} = \frac{-Q + \sqrt{Q^2 + 4 Q R_{\text{obs}}}}{2 R_{\text{obs}}}$$

Limiting behavior: when $Q \gg R_{\text{obs}}$ (fast dynamics, clean observations), $K_{ss} \to 1$; when $Q \ll R_{\text{obs}}$ (slow dynamics, noisy observations), $K_{ss} \approx \sqrt{Q / R_{\text{obs}}}$.

**Connection to ACT quantities.** The adaptive tempo for a single observation channel at rate $\nu$ is $\mathcal{T} = \nu \cdot K_{ss}$, and the sector parameter in the continuous-time framework is $\alpha = \mathcal{T}$. The bridge is trivial in the scalar case: the gain IS the sector parameter.


## Proposition B.2: Matrix Kalman Sector Condition

**Statement.** For a linear-Gaussian system with state $x \in \mathbb{R}^n$, observations $o \in \mathbb{R}^m$, observation matrix $H$, and Kalman gain $K = P^- H^T (H P^- H^T + R_{\text{obs}})^{-1}$, the correction function $F(e) = KH \cdot e$ satisfies the sector condition in the $(P^-)^{-1}$-weighted inner product, restricted to the observable subspace $\mathcal{O} = \operatorname{range}(H^T)$:

*[Derived (matrix-Kalman-sector, from Kalman covariance reduction)]*

$$e^T (P^-)^{-1} KH \, e = e^T H^T S^{-1} H \, e \geq \alpha \cdot e^T (P^-)^{-1} e$$

where $S = H P^- H^T + R_{\text{obs}}$ is the innovation covariance, and:

$$\alpha = 1 - \lambda_{\max}(P_{t\vert t} \, P_{t\vert t-1}^{-1})$$

restricted to observable directions. In unobservable directions ($e \in \ker(H)$), $\alpha = 0$.

**Proof.** Define the $(P^-)^{-1}$-weighted inner product: $\langle u, v \rangle_{P^-} = u^T (P^-)^{-1} v$. In this inner product the sector product becomes:

$$\langle e, KH \, e \rangle_{P^-} = e^T (P^-)^{-1} KH \, e$$

Substituting $K = P^- H^T S^{-1}$:

$$e^T (P^-)^{-1} P^- H^T S^{-1} H \, e = e^T H^T S^{-1} H \, e$$

Since $S \succ 0$, the matrix $H^T S^{-1} H$ is symmetric positive semidefinite, with null space $\ker(H)$. So $\langle e, KH \, e \rangle_{P^-} \geq 0$ for all $e$, with equality iff $He = 0$.

For the sector bound, we need $e^T H^T S^{-1} H \, e \geq \alpha \cdot e^T (P^-)^{-1} e$. From the Kalman covariance identity $KH = I - P (P^-)^{-1}$ (where $P = P_{t\vert t}$ is the posterior covariance), the eigenvalues of $KH$ in the $(P^-)^{-1}$-weighted sense are $1 - \lambda_i(P(P^-)^{-1})$, where $\lambda_i$ denotes generalized eigenvalues.

Since $P \preceq P^-$ (the posterior is no less certain than the prior), $\lambda_i(P(P^-)^{-1}) \leq 1$, so all eigenvalues of $KH$ are non-negative. In observable directions, $P \prec P^-$ strictly, giving $\alpha \gt 0$. In unobservable directions, $P = P^-$ (no information gained), so $\alpha = 0$. $\square$

**Fully observable diagonal case.** When $H = I$, $A = I$, $Q = \operatorname{diag}(q_1, \ldots, q_n)$, $R_{\text{obs}} = \operatorname{diag}(r_1, \ldots, r_n)$, the problem decouples into $n$ scalar problems (each governed by Prop B.1), and:

*[Derived (diagonal-Kalman-sector)]*

$$\alpha = \min_{i=1}^n K_i = \min_{i=1}^n \frac{-q_i + \sqrt{q_i^2 + 4 q_i r_i}}{2 r_i}$$

The bottleneck is the dimension with the worst signal-to-noise ratio, consistent with #per-dimension-persistence.

**The weighted-norm subtlety.** The Lyapunov proofs in #sector-condition-derivation use the Euclidean norm ($V = \frac{1}{2}\lVert e\rVert^2$), while the matrix Kalman sector condition holds in the $(P^-)^{-1}$-weighted norm. For fully observable systems with bounded condition number $\kappa(P^-)$, the norms are equivalent:

$$\alpha_{\text{Euclidean}} \geq \alpha_{\text{weighted}} / \kappa(P^-)$$

The Lyapunov results remain valid with this quantitative adjustment. The weighted Lyapunov function $V(e) = \frac{1}{2} e^T (P^-)^{-1} e$ yields the tighter bound directly.


## Proposition B.3: Bridge Theorem

**Statement.** Given the gain-based update $M_t = M_{t-1} + \eta^\ast \cdot g(\delta_t)$ ( #update-gain), with $H$ mapping state-space corrections to observation-space mismatch reduction, the induced correction function $F(\delta) = \eta^\ast \cdot H \, g(\delta)$ satisfies the sector condition (GA-3) with parameter $\alpha \gt 0$ whenever:

**(B1) Directional fidelity.** The composite mismatch transform preserves the mismatch-reducing direction:

*[Derived (bridge-theorem, from update-gain + B1)]*

$$\delta^T H \, g(\delta) \geq c \lVert\delta\rVert^2 \quad \text{for } \lVert\delta\rVert \leq R$$

for some $c \gt 0$. The sector parameter is:

$$\alpha = \eta^\ast \cdot c_{\min}, \qquad c_{\min} = \inf_{\lVert\delta\rVert \leq R} \frac{\delta^T H \, g(\delta)}{\lVert\delta\rVert^2}$$

**Proof.** The gain-based update changes the model state by $\Delta M = \eta^\ast \cdot g(\delta)$. The induced change in predicted observation is $H \cdot \Delta M = \eta^\ast \cdot H \, g(\delta)$, so the expected correction function (the mismatch reduction per step) is:

$$F(\delta) = \eta^\ast \cdot H \, g(\delta)$$

The sector product is:

$$\delta^T F(\delta) = \eta^\ast \cdot \delta^T H \, g(\delta)$$

By B1: $\delta^T H \, g(\delta) \geq c_{\min} \lVert\delta\rVert^2$. Since $\eta^\ast \gt 0$ (the agent updates), we have:

$$\delta^T F(\delta) \geq \eta^\ast \cdot c_{\min} \lVert\delta\rVert^2 = \alpha \lVert\delta\rVert^2 \qquad \square$$

**When B1 holds by construction.** For optimal Bayesian updates (Kalman, conjugate families, exponential families), the posterior update minimizes expected loss, ensuring the correction aligns with the mismatch. B1 holds by optimality, not by assumption. The gain principle $\eta^\ast = U_M / (U_M + U_o)$ determines only the magnitude; the direction is guaranteed by the update rule's optimality. For gradient descent on a convex loss, B1 follows from gradient monotonicity (the defining property of convexity).


## Proposition B.4: Gradient Equivalence

**Statement.** For any agent updating via gradient descent on a differentiable loss $L$ with learning rate $\eta$ and minimizer $M^\ast$ (where $\nabla L(M^\ast) = 0$):

*[Derived (sector-convexity-equivalence)]*

$$\text{GA-3 holds with } (\alpha, R) \iff L \text{ is locally } (\alpha/\eta)\text{-strongly convex on } \mathcal{B}_R(M^\ast)$$

The sector parameter factors as $\alpha = \eta \cdot \mu$, where:

$$\mu = \inf_{\lVert\delta\rVert \leq R} \lambda_{\min}(\nabla^2 L(M^\ast + \delta))$$

is the strong convexity modulus. The basin radius $R$ is the largest ball around $M^\ast$ where $\nabla^2 L$ remains positive definite.

**Proof.** The correction function for gradient descent is $F(\delta) = \eta \cdot \nabla L(M^\ast + \delta)$ (continuous-time form absorbing event rate $\nu$ into $\mathcal{T} = \nu \cdot \eta$). The sector condition requires:

$$\delta^T F(\delta) = \eta \cdot \delta^T \nabla L(M^\ast + \delta) \geq \alpha \lVert\delta\rVert^2$$

Dividing by $\eta \gt 0$:

$$\delta^T \nabla L(M^\ast + \delta) \geq \frac{\alpha}{\eta} \lVert\delta\rVert^2$$

A differentiable function $L$ is $\mu$-strongly convex on $\mathcal{S}$ iff the gradient monotonicity condition holds (Nesterov 2004, Theorem 2.1.10): for all $x, y \in \mathcal{S}$,

$$(\nabla L(x) - \nabla L(y))^T (x - y) \geq \mu \lVert x - y\rVert^2$$

Setting $x = M^\ast + \delta$, $y = M^\ast$, and using $\nabla L(M^\ast) = 0$:

$$\nabla L(M^\ast + \delta)^T \delta \geq \mu \lVert\delta\rVert^2$$

This is identical to the sector condition divided by $\eta$. The equivalence follows:

($\Rightarrow$) GA-3 gives $\delta^T \nabla L(M^\ast + \delta) \geq (\alpha/\eta) \lVert\delta\rVert^2$. Since $\nabla L(M^\ast) = 0$, gradient monotonicity holds with $\mu = \alpha/\eta$.

($\Leftarrow$) $\mu$-strong convexity gives $\delta^T \nabla L(M^\ast + \delta) \geq \mu \lVert\delta\rVert^2$. Multiplying by $\eta$: $\delta^T F(\delta) \geq \eta\mu \lVert\delta\rVert^2$. So GA-3 holds with $\alpha = \eta\mu$. $\square$

**The $\alpha$ factorization.** The decomposition $\alpha = \eta \cdot \mu$ separates agent design ($\eta$, responsiveness) from environment structure ($\mu$, loss curvature). The adaptive tempo maps as $\alpha \propto \mathcal{T}$: higher gain or steeper curvature means faster mismatch correction.


## Loss Function Classification

The gradient equivalence (Prop B.4) classifies which loss functions satisfy GA-3, and with what parameters:

| Loss class | Strong convexity | $\alpha$ | Basin $R$ | Status |
|---|---|---|---|---|
| Quadratic (Kalman, linear regression) | Global: $\mu = \lambda_{\min}(H)$ | $\eta \cdot \lambda_{\min}(H)$ | $\infty$ | Exact |
| Exponential family (natural params) | Global: $\mu = \lambda_{\min}(\text{Fisher})$ | $\eta \cdot \lambda_{\min}(\text{Fisher})$ | $\infty$ | Exact |
| L2-regularized convex loss | Global: $\mu \geq \lambda$ | $\eta \cdot \lambda$ (floor) | $\infty$ | Exact |
| Unregularized logistic | Global convex, not strongly | $\eta \cdot \mu(R)$, decaying | $\infty$ (but $\alpha \to 0$) | Local |
| Quasi-convex | $\delta^T \nabla L \geq 0$ but ratio $\to 0$ | $\eta \cdot \mu(R) \to 0$ | Finite effective | Local |
| Non-convex within basin | Local: $\mu \gt 0$ in basin | $\eta \cdot \mu_\text{local}$ | Distance to nearest saddle | Local |
| Non-convex beyond basin | Fails: $\lambda_{\min}(\nabla^2 L) \lt 0$ | N/A | N/A | Fails |

**Key observations:**

1. *All exponential family models in natural parameter form satisfy GA-3 globally.* This subsumes Kalman, Beta-Bernoulli, Gaussian, and Poisson posteriors. The Hessian is the Fisher information matrix, which is positive definite in the interior of the natural parameter space.

2. *L2 regularization transforms locally strongly convex losses into globally strongly convex ones.* The regularization parameter $\lambda$ provides a floor: $\alpha \geq \eta \lambda$ everywhere.

3. *Non-convex losses satisfy GA-3 within each basin of attraction.* The basin radius $R$ is the distance from the local minimum to the nearest inflection surface (where $\lambda_{\min}(\nabla^2 L) = 0$). Beyond the basin, the sector condition fails — this IS the structural-adaptation trigger from #structural-adaptation-necessity.


## Failure Modes

The bridge fails in precisely five cases. These characterize the exact conditions under which the gain-based update does NOT produce a correction function satisfying the sector condition.

### FM-1: Directional Infidelity

The mismatch transform $g$ rotates the correction away from the mismatch direction, so $\delta^T H g(\delta) \leq 0$.

*Example.* If $\delta \in \mathbb{R}^2$ and $g(\delta) = R_{90}\delta$ (a 90-degree rotation), then $\delta^T g(\delta) = 0$ for all $\delta$. The correction is perpendicular to the mismatch and never reduces it.

*When it occurs.* Pathological parameterizations where the model-space update direction is misaligned with observation-space mismatch. For optimal Bayesian updates, B1 holds by construction — the posterior minimizes expected loss.

### FM-2: Gain Collapse

$\eta^\ast \to 0$ while $\rho \gt 0$, so $\alpha \to 0$ and the persistence condition $\alpha \gt \rho/R$ eventually fails. An agent accumulating experience in a non-stationary environment will eventually have gain too small to track changes. This is not a bridge failure but a persistence-condition failure — the bridge holds ($\alpha = \eta^\ast \cdot c \gt 0$ for finite experience), but $\alpha$ falls below $\rho/R$. See #update-gain.

### FM-3: Nonlinear Saturation

The correction function $g$ saturates at large $\lVert\delta\rVert$, so the sector ratio $\delta^T g(\delta) / \lVert\delta\rVert^2$ decays. For a saturating function such as $g(\delta) = \tanh(\delta)$, the local sector parameter is:

$$\alpha(R) = \eta^\ast \cdot \frac{\tanh(R)}{R}$$

For small $R$, $\alpha \approx \eta^\ast$ (linear regime). For large $R$, $\alpha \approx \eta^\ast / R$ (saturated regime). The sector condition holds locally — the valid region shrinks as the nonlinearity strengthens. This is exactly what the local form A2' in #sector-condition-derivation anticipates.

### FM-4: Unobservable Directions

When $\ker(H) \neq \{0\}$ (fewer observations than state dimensions), the correction has no effect on mismatch components in $\ker(H)$. The sector condition holds only in the observable subspace $\mathcal{O} = \operatorname{range}(H^T)$. This is a structural limitation: the agent cannot correct errors it cannot observe. See #observability-dominance.

For persistence in the full state space, the system must be *detectable*: all unstable modes must be observable. Stable unobservable modes decay naturally without correction.

### FM-5: Model Misspecification

The model class does not contain the truth, so the gradient direction is systematically wrong. B1 fails because the correction aims at the wrong target. The sector parameter degrades proportionally to the misspecification. This is the #structural-adaptation-necessity trigger: the correction function fails not because the gain is wrong but because the correction *direction* is wrong.


## Simulation Results Summary

Six numerical experiments validate the gradient equivalence (Prop B.4) and the loss-function classification. Full code and traces are in `msc/spike-gain-sector-bridge-nonlinear.md`.

### Experiment 1: Quadratic Loss (Global Strong Convexity)

$L(w) = \frac{1}{2}(w - w^\ast)^T H(w - w^\ast)$ with $w \in \mathbb{R}^5$, Hessian eigenvalues $\{0.5, 1.0, 2.0, 3.0, 5.0\}$, $\eta = 0.1$. The sector ratio $\delta^T F / \lVert\delta\rVert^2$ at every gradient-descent step fell within $[\eta\mu, \eta L] = [0.05, 0.50]$, confirming Prop B.4 exactly. No step violated the bound.

### Experiment 2: Logistic Regression (Position-Dependent Convexity)

Logistic regression with $d = 2$, $N = 5000$ samples. Unregularized: sector ratio positive along the entire trajectory, with local $\mu$ ranging from 0.076 (at MLE) to higher values far from it. With L2 regularization ($\lambda = 0.1$): sector ratio bounded below by $\eta\lambda = 0.03$ at every point, confirming the global floor.

### Experiment 3: Gaussian Mixture (Non-Convex, Basin Structure)

Two-component Gaussian mixture. Within basin ($r \lt 3.1$): Hessian positive definite, sector ratio positive, gradient descent converges to correct optimum. At basin boundary ($r \approx 3.1$): Hessian eigenvalue crosses zero. Beyond basin ($r \gt 3.5$): sector ratio negative, gradient descent converges to wrong optimum. Basin boundary confirmed as sharp transition, matching the #structural-adaptation-necessity trigger.

### Experiment 4: Local Sector Parameter Measurement

Same Gaussian mixture. Sector parameter $\alpha(r)$ decreases monotonically from 181.4 (at $r = 0.5$) to 125.8 (at $r = 3.0$), then drops to zero at $r \approx 3.1$. The decay is moderate within the basin (69% retention at the boundary); the transition at the boundary is sharp.

### Experiment 5: Exponential Family (Poisson, Natural Parameters)

Poisson in natural parameter space. Sector ratio positive at every step, ranging from 0.00177 to 0.00240 (with $\eta = 0.001$). Confirms global strong convexity of exponential family losses in natural parameterization.

### Experiment 6: Quasi-Convex and Multi-Modal Losses

*Quasi-convex* ($L(w) = -1/(1+w^2)$): sector ratio always positive but decays as $O(1/w^4)$. No uniform lower bound exists — $\alpha(R) \to 0$, making persistence bounds vacuous for large $R$.

*Multi-modal* ($L(w) = \sin(w) + 0.01w^2$): sector condition holds within each basin ($\lvert\delta\rvert \lt 3.0$), fails at basin boundary (gradient reversal at local maximum). Basin radius $\approx$ distance from local minimum to nearest local maximum.


## Epistemic Status

**Propositions B.1 and B.2** are *exact* — they follow from standard Kalman filter algebra. The only subtlety is the weighted norm in the matrix case (B.2), which is a quantitative refinement, not a qualitative gap. Both are standard results in estimation theory reframed in sector-condition language.

**Proposition B.3** (Bridge Theorem) is a *conditional derivation*: exact under B1 (directional fidelity). B1 holds by construction for optimal Bayesian updates (the posterior minimizes expected loss, ensuring the correction aligns with the mismatch). For approximate update rules, B1 is a design condition, not a global assumption. The condition is transparent and checkable for specific systems.

**Proposition B.4** (Gradient Equivalence) is an *exact mathematical equivalence* — the bidirectional implication is proved, not assumed. The loss-function classification follows directly. The simulation experiments confirm the theoretical predictions across all six loss classes tested; no violations were observed where the theory predicts the sector condition holds.

**Max attainable:** *conditional* for the bridge (B1 is inherent — pathological update rules exist), *exact* for the gradient equivalence. The condition cannot be removed: there exist correction functions that violate the sector condition (FM-1 through FM-5).

**What remains open.** (1) Non-gradient agents (PID controllers, rule-based systems, human judgment): GA-3 remains an empirical claim for these agent classes. (2) Time-varying $\alpha$: when the gain adapts (Adam, RMSprop, Kalman transient), $\alpha(t)$ varies; the Lyapunov analysis extends to time-varying $\alpha(t) \geq \underline{\alpha} \gt 0$ via standard results (Khalil 2002, Chapter 8). (3) Stochastic gradients: SGD satisfies the sector condition *in expectation*; the per-step noise enters as effective disturbance in the Prop A.1S framework.


## Discussion

**The formal chain is closed for well-designed agents.** The prediction chain becomes:

$$\text{gain principle} + \text{B1 (directional fidelity)} \;\xrightarrow{\text{Prop B.3 (exact)}}\; \text{sector condition (GA-3)} \;\xrightarrow{\text{Props A.1, A.1S, A.2 (exact)}}\; \text{persistence, reserve, scaling}$$

For optimal Bayesian updates, B1 holds by construction, making the full chain a derivation. For gradient agents, B1 is equivalent to local strong convexity — a well-characterized property.

**GA-3 is grounded, not floating.** The assumption load shifts from "the correction function satisfies the sector condition" (what correction function?) to "the update rule has directional fidelity" (the correction at least points toward reality). For the important agent classes — Kalman filters, conjugate posteriors, exponential families, gradient descent on convex losses — this is automatic.

**Basin boundary = structural adaptation trigger.** For gradient agents with non-convex losses, the basin radius $R$ is the convexity radius of the loss landscape. When mismatch exceeds $R$, the correction function reverses direction. This is the #structural-adaptation-necessity trigger with a precise geometric characterization: structural adaptation is needed when the agent crosses an inflection surface of its loss landscape.


## Working Notes

- The fluid-limit gap: the bridge analysis works in expected value. The actual per-step correction is stochastic; observation noise $\varepsilon$ contributes $K\varepsilon$ to each update, acting as effective disturbance of magnitude $\lVert K\rVert \sigma_\varepsilon$ per step. This maps to the Prop A.1S (stochastic) framework — the sector condition on the expected correction plus stochastic noise.
- For variational inference and other approximate methods, B1 is not guaranteed by optimality and must be verified per approximation scheme.
- The adaptive-reserve factorization for gradient agents is $\Delta\rho^\ast = \eta\mu R - \rho$, with three controllable factors: gain $\eta$, curvature $\mu$, and basin width $R$. An agent is robust when $\eta\mu R \gg \rho$.

---

[^khalil2002]: Khalil, H. K. (2002). *Nonlinear Systems* (3rd ed.). Prentice Hall.
[^nesterov2004]: Nesterov, Y. (2004). *Introductory Lectures on Convex Optimization*. Springer. Theorem 2.1.10.
[^lure1957]: Lur'e, A. I. (1957). *Some Nonlinear Problems in the Theory of Automatic Control*.

*(Consolidates `msc/spike-gain-sector-bridge.md` and `msc/spike-gain-sector-bridge-nonlinear.md`.)*
