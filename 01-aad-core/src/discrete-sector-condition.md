---
slug: discrete-sector-condition
type: derivation
status: conditional
depends:
  - sector-condition-derivation
  - update-gain
  - gain-sector-bridge
  - event-driven-dynamics
stage: draft
---

# Derivation: Discrete-Time Sector Condition

Discrete-time analogs of Props A.1, A.1S, and A.2 via contraction mapping, closing the fluid-limit gap (GA-5) between the event-driven dynamics ( #event-driven-dynamics) and the continuous-time Lyapunov results in #sector-condition-derivation.

## Formal Expression

### Setup

The discrete mismatch dynamics at event step $k$ are:

*[Definition (Discrete Dynamics)]*

$$\delta_{k+1} = \delta_k - \eta^\ast F_d(\delta_k) + w_k$$

where $\eta^\ast$ is the update gain ( #update-gain), $F_d$ is the discrete correction direction, and $w_k$ is the per-step disturbance. The continuous correction function $F(\mathcal{T}, \delta)$ from #sector-condition-derivation decomposes as $F = \nu \cdot \eta^\ast \cdot F_d$ at event rate $\nu$.

### (DA2') Discrete Sector-Lipschitz Condition

*[Assumption DA2' (discrete-sector-condition)]*

There exist constants $c_{\min} > 0$ and $c_{\max} < 2/\eta^\ast$ such that for all $\lVert\delta\rVert \leq R$:

**(DA2'a) Lower sector bound (directional fidelity):**

$$\delta^T F_d(\delta) \geq c_{\min} \lVert\delta\rVert^2$$

**(DA2'b) Lipschitz bound (bounded correction magnitude):**

$$\lVert F_d(\delta)\rVert \leq c_{\max} \lVert\delta\rVert$$

The **lower bound** (DA2'a) is directional fidelity — the correction points inward, identical to the continuous sector condition (A2') from #sector-condition-derivation via #gain-sector-bridge.

The **Lipschitz bound** (DA2'b) controls the *magnitude* of the correction, not merely its projection onto the mismatch direction. The combined constraint $c_{\max} < 2/\eta^\ast$ is the **no-overshoot condition**: each correction step must not reverse the mismatch. This is the classical step-size condition $\eta^\ast < 2/L$ for gradient descent (where $L$ is the Lipschitz constant of the gradient). For Bayesian updates, this is satisfied by construction — the posterior lies between prior and data.

**Why DA2'b is stronger than an inner-product upper bound.** A two-sided inner-product condition $\delta^T F_d(\delta) \leq c_{\max}\lVert\delta\rVert^2$ constrains only the projection of $F_d$ onto $\delta$. By Cauchy-Schwarz, the Lipschitz bound (DA2'b) implies the inner-product upper bound: $\delta^T F_d(\delta) \leq \lVert\delta\rVert \cdot \lVert F_d(\delta)\rVert \leq c_{\max}\lVert\delta\rVert^2$. But the converse fails — a correction function with a large transverse component (orthogonal to $\delta$) can satisfy the inner-product bound while violating the norm bound. The proofs below (especially DA.1S) require the norm bound $\lVert F_d(\delta)\rVert^2 \leq c_{\max}^2\lVert\delta\rVert^2$, which follows from DA2'b but not from an inner-product condition alone.

**Scalar case.** In one dimension, DA2'a and DA2'b together reduce to the classical sector condition $c_{\min} \leq F_d(\delta)/\delta \leq c_{\max}$, since norm and inner product coincide. No generality is lost for scalar systems.

**Relationship to the continuous-time condition.** The continuous sector condition (A2'/GA-3) is a one-sided inner-product bound $\delta^T F \geq \alpha\lVert\delta\rVert^2$ — this suffices for continuous-time Lyapunov analysis because $\dot{V}$ involves only $\delta^T F$, not $\lVert F\rVert$. Discretization introduces the quadratic term $(\eta^\ast)^2\lVert F_d\rVert^2$ (see DA.1S proof), which requires the Lipschitz bound. This is the standard sector-vs-Lipschitz distinction in nonlinear systems theory.

### Contraction factor

Under DA2', the per-step Lyapunov function $V_k = \frac{1}{2}\lVert\delta_k\rVert^2$ satisfies (in the zero-disturbance case $w_k = 0$):

*[Derived (contraction, from DA2')]*

$$\lVert\delta_{k+1}\rVert^2 = \lVert\delta_k - \eta^\ast F_d(\delta_k)\rVert^2 = \lVert\delta_k\rVert^2 - 2\eta^\ast \delta_k^T F_d(\delta_k) + (\eta^\ast)^2 \lVert F_d(\delta_k)\rVert^2$$

Applying DA2'a (lower sector bound on $\delta^T F_d$) and DA2'b (Lipschitz bound on $\lVert F_d\rVert$):

$$\lVert\delta_{k+1}\rVert^2 \leq (1 - 2\eta^\ast c_{\min} + (\eta^\ast)^2 c_{\max}^2) \lVert\delta_k\rVert^2 = \lambda_{\text{eff}}^2 \lVert\delta_k\rVert^2$$

where:

$$\lambda_{\text{eff}}^2 = 1 - 2\eta^\ast c_{\min} + (\eta^\ast)^2 c_{\max}^2$$

**Stability condition.** $\lambda_{\text{eff}}^2 < 1$ requires $2\eta^\ast c_{\min} > (\eta^\ast)^2 c_{\max}^2$, i.e.:

$$\eta^\ast < \frac{2 c_{\min}}{c_{\max}^2}$$

This is automatically satisfied when $c_{\min} \approx c_{\max}$ (well-conditioned correction), recovering the standard step-size condition $\eta^\ast < 2/c_{\max}$. For ill-conditioned corrections ($c_{\min} \ll c_{\max}$), the constraint is tighter. For Bayesian updates with bounded condition number, both conditions are satisfied.

**Scalar (colinear) specialization.** When $F_d(\delta) \parallel \delta$ (scalar system or colinear correction), $\lVert F_d(\delta)\rVert = |F_d(\delta)/\delta| \cdot \lVert\delta\rVert$ and the contraction factor simplifies to $\lambda = \max(|1 - \eta^\ast c_{\min}|, |1 - \eta^\ast c_{\max}|)$, the classical form. The general vector formula $\lambda_{\text{eff}}^2$ reduces to $\lambda^2$ in this case.

With disturbance $w_k \neq 0$:

$$\lVert\delta_{k+1}\rVert^2 \leq \lambda_{\text{eff}}^2 \lVert\delta_k\rVert^2 + 2\lVert\delta_k\rVert \lVert w_k\rVert + \lVert w_k\rVert^2$$

### Proposition DA.1: Bounded Mismatch (Deterministic)

**Statement.** Under DA2' with $\eta^\ast < 2c_{\min}/c_{\max}^2$ and bounded per-step disturbance $\lVert w_k\rVert \leq \rho_{\text{step}}$, the mismatch is ultimately bounded:

*[Derived (DA.1, discrete bounded mismatch)]*

$$R^\ast_D = \frac{\rho_{\text{step}}}{1 - \lambda_{\text{eff}}}$$

**Proof.** By the triangle inequality: $\lVert\delta_{k+1}\rVert = \lVert(\delta_k - \eta^\ast F_d(\delta_k)) + w_k\rVert \leq \lVert\delta_k - \eta^\ast F_d(\delta_k)\rVert + \lVert w_k\rVert$. The contraction bound gives $\lVert\delta_k - \eta^\ast F_d(\delta_k)\rVert \leq \lambda_{\text{eff}} \lVert\delta_k\rVert$. Therefore:

$$\lVert\delta_{k+1}\rVert \leq \lambda_{\text{eff}} \lVert\delta_k\rVert + \rho_{\text{step}}$$

This is an affine contraction with $\lambda_{\text{eff}} < 1$. By the Banach fixed-point theorem, all trajectories starting in $\mathcal B_R$ converge to the ball of radius $R^\ast_D = \rho_{\text{step}}/(1 - \lambda_{\text{eff}})$, provided $R^\ast_D < R$. $\square$

**Recovery of continuous result.** In the fluid limit ($\eta^\ast \to 0$, $\nu \to \infty$, $\nu \eta^\ast = \mathcal{T}$ fixed), $\lambda_{\text{eff}}^2 = 1 - 2\eta^\ast c_{\min} + O((\eta^\ast)^2)$, so $\lambda_{\text{eff}} \to 1 - \eta^\ast c_{\min}$ and $\rho_{\text{step}} \to \rho/\nu$. Then:

$$R^\ast_D = \frac{\rho/\nu}{\eta^\ast c_{\min}} = \frac{\rho}{\nu \eta^\ast c_{\min}} = \frac{\rho}{\alpha}$$

recovering Prop A.1 exactly. The discrete-to-continuous gap for Model D steady state is **zero**.

### Proposition DA.2: Adaptive Reserve (Discrete)

**Statement.** Under the conditions of DA.1, the agent can absorb an additional per-step disturbance of:

*[Derived (DA.2, discrete adaptive reserve)]*

$$\Delta\rho^\ast_{\text{step}} = (1 - \lambda_{\text{eff}}) R - \rho_{\text{step}}$$

**Proof.** Identical to Prop A.2: the new $R^\ast_D = (\rho_{\text{step}} + \Delta\rho)/(1 - \lambda_{\text{eff}})$ must satisfy $R^\ast_D \leq R$. $\square$

The structure is identical to the continuous adaptive reserve $\Delta\rho^\ast = \alpha R - \rho$. The per-event contraction rate is $(1 - \lambda_{\text{eff}})$; the per-unit-time rate is $\nu(1 - \lambda_{\text{eff}})$. In the fluid limit, $\nu(1 - \lambda_{\text{eff}}) \to \nu \cdot \eta^\ast c_{\min} = \alpha$, recovering the continuous result. (Note: the per-event rate $(1 - \lambda_{\text{eff}})$ converges to $\eta^\ast c_{\min}$, not to $\alpha$ directly — the factor of $\nu$ converts between per-event and per-unit-time.)

### Proposition DA.1S: Stochastic Bounded Mismatch (Discrete)

**Statement.** Under DA2' with $\eta^\ast < 2c_{\min}/c_{\max}^2$ and i.i.d. zero-mean disturbance $\mathbb{E}[w_k] = 0$, $\mathbb{E}[\lVert w_k\rVert^2] = \sigma^2_{\text{step}}$, the mismatch satisfies:

*[Derived (DA.1S, discrete stochastic bounded mismatch)]*

$$\mathbb{E}[\lVert\delta_k\rVert^2] \leq \lambda^{2k}_{\text{eff}} \lVert\delta_0\rVert^2 + \frac{\sigma^2_{\text{step}}}{1 - \lambda^2_{\text{eff}}}$$

where $\lambda^2_{\text{eff}} = 1 - 2\eta^\ast c_{\min} + (\eta^\ast)^2 c^2_{\max}$.

**Proof.** Define $V_k = \lVert\delta_k\rVert^2$. Taking expectations of the squared update:

$$\mathbb{E}[V_{k+1} \mid \delta_k] = \lVert\delta_k - \eta^\ast F_d(\delta_k)\rVert^2 + \sigma^2_{\text{step}}$$

The first term expands as:

$$\lVert\delta_k - \eta^\ast F_d(\delta_k)\rVert^2 = V_k - 2\eta^\ast \delta_k^T F_d(\delta_k) + (\eta^\ast)^2 \lVert F_d(\delta_k)\rVert^2$$

By DA2'a (lower sector bound): $\delta_k^T F_d(\delta_k) \geq c_{\min} V_k$.

By DA2'b (Lipschitz bound): $\lVert F_d(\delta_k)\rVert^2 \leq c^2_{\max} V_k$.

Note that the second step requires the *norm* bound DA2'b, not merely an inner-product upper bound — this is where the Lipschitz condition is essential. Combining:

$$\mathbb{E}[V_{k+1} \mid \delta_k] \leq \lambda^2_{\text{eff}} V_k + \sigma^2_{\text{step}}$$

The condition $\eta^\ast < 2c_{\min}/c_{\max}^2$ ensures $\lambda^2_{\text{eff}} < 1$. This is a supermartingale (when $V_k$ is large enough). Iterating:

$$\mathbb{E}[V_k] \leq \lambda^{2k}_{\text{eff}} V_0 + \frac{\sigma^2_{\text{step}}}{1 - \lambda^2_{\text{eff}}}$$

The steady-state mean-square mismatch is $\sigma^2_{\text{step}} / (1 - \lambda^2_{\text{eff}})$. $\square$

**Recovery of continuous result.** In the fluid limit: $\sigma^2_{\text{step}} \to n\sigma^2_w / \nu$, $\lambda^2_{\text{eff}} \to 1 - 2\eta^\ast c_{\min}$, and $(1 - \lambda^2_{\text{eff}}) \to 2\eta^\ast c_{\min}$. The steady-state becomes $n\sigma^2_w / (2\nu \eta^\ast c_{\min}) = n\sigma^2_w / (2\alpha)$, recovering Prop A.1S exactly.

The discrete-to-continuous gap for Model S variance is $O((\eta^\ast)^2 c^2_{\max})$ — the $(\eta^\ast)^2 \lVert F_d\rVert^2$ term that vanishes in the fluid limit. This quantifies the error introduced by GA-5 and confirms it is small whenever $\eta^\ast c_{\max} \ll 1$.

### Fluid Limit Theorem

*[Derived (Conditional on Lipschitz regularity)]*

**Statement.** Let $F_d$ be Lipschitz continuous with constant $L_F$ on $\mathcal B_R$. Let $\delta^{(\nu)}(t)$ denote the piecewise-constant interpolation of the discrete trajectory at event rate $\nu$, and $\delta(t)$ the solution of the continuous ODE $d\delta/dt = -F(\mathcal{T}, \delta) + w(t)$ with $F = \nu \eta^\ast F_d$. Then:

$$\sup_{t \in [0,T]} \lVert\delta^{(\nu)}(t) - \delta(t)\rVert \leq C \cdot \frac{\eta^\ast c_{\max}}{\nu^{1/2}}$$

for a constant $C$ depending on $T$, $L_F$, and $R$.

**Sketch.** This follows from the standard ODE-approximation theory for Euler schemes (Kushner & Yin, 2003, Ch. 5). The discrete update $\delta_{k+1} = \delta_k - \eta^\ast F_d(\delta_k) + w_k$ is a forward Euler step for the ODE with step size $1/\nu$. The Lipschitz condition on $F_d$ ensures the local truncation error is $O(1/\nu^2)$. Summing over $O(\nu T)$ steps and applying the Gronwall inequality gives the $O(1/\nu^{1/2})$ bound.

For Model D (deterministic): the steady-state gap is exactly zero (both discrete and continuous converge to the same fixed point). The fluid-limit error affects only transients.

For Model S (stochastic): the steady-state variance gap is $O((\eta^\ast)^2 c^2_{\max})$, which equals $O(\eta^\ast c_{\max} / \nu)$ when expressed in terms of the event rate.

## Epistemic Status

**DA.1, DA.1S, and DA.2** are *conditional* on DA2', which now includes both a sector lower bound (DA2'a) and a Lipschitz upper bound (DA2'b). The Lipschitz condition is strictly stronger than an inner-product upper bound — this is a real assumption, not a technicality. For Bayesian updates and gradient descent on smooth losses, DA2'b is satisfied (the correction magnitude is controlled by the loss curvature). For agents with non-smooth or pathological correction functions, DA2'b must be verified independently.

The proofs themselves are standard contraction-mapping (DA.1/DA.2) and supermartingale (DA.1S) arguments. The step-size constraint $\eta^\ast < 2c_{\min}/c_{\max}^2$ is essential and is stated explicitly in each proposition.

**Fluid limit theorem** is *conditional* on Lipschitz regularity of $F_d$ — a standard regularity condition satisfied by all correction functions in the verified instances table ( #gain-sector-bridge). The convergence rate follows from classical ODE approximation theory (Kushner & Yin, 2003); the application to the AAD mismatch dynamics is new but the mathematics is not.

**Max attainable:** conditional — the Lipschitz bound DA2'b is inherent to the discrete-time treatment and cannot be replaced by a weaker inner-product condition without losing the norm bound used in the proofs.

## Discussion

**GA-5 is closed.** The fluid-limit bridging assumption is no longer required as an ungrounded assumption. For Model D, the discrete and continuous steady states are identical — the gap is zero. For Model S, the gap is $O(\eta^\ast c_{\max})$ in variance, quantitatively bounded and small in the regime where $\eta^\ast c_{\max} \ll 1$. The continuous-time results in #sector-condition-derivation are formally justified as the fluid limit of the discrete results here.

**DA2' is a sector-Lipschitz condition, not a pure sector condition.** The continuous-time treatment ( #sector-condition-derivation) requires only the one-sided sector bound $\delta^T F \geq \alpha\lVert\delta\rVert^2$ because the Lyapunov derivative $\dot{V}$ depends only on $\delta^T F$. Discretization introduces a quadratic term $(\eta^\ast)^2\lVert F_d\rVert^2$ that requires the Lipschitz bound $\lVert F_d\rVert \leq c_{\max}\lVert\delta\rVert$. This is the standard distinction between sector conditions and Lipschitz conditions in nonlinear systems theory. For all agents in the verified instances table ( #gain-sector-bridge), the Lipschitz bound holds alongside the sector bound, so DA2' imposes no additional restriction in practice.

**The step-size constraint has two forms.** For well-conditioned corrections ($c_{\min} \approx c_{\max}$), the constraint reduces to $\eta^\ast < 2/c_{\max}$ — the classical form. For ill-conditioned corrections ($c_{\min} \ll c_{\max}$), the tighter constraint $\eta^\ast < 2c_{\min}/c_{\max}^2$ applies. This distinction is invisible in scalar systems but matters for high-dimensional agents with anisotropic correction.

**No downstream results change qualitatively.** The persistence condition, adaptive reserve, and adversarial scaling laws derived in #sector-condition-derivation and #adversarial-destabilization hold as stated. The discrete framework provides sharper constants (replacing $\alpha$ with $\nu(1 - \lambda_{\text{eff}})$) and a quantitative transient error bound, but the qualitative structure is unchanged.

**Section I's formal chain is now complete.** The prediction chain:

$$\text{gain principle} + \text{B1} \;\xrightarrow{\text{derived}}\; \text{sector condition} \;\xrightarrow{\text{Lyapunov/contraction}}\; \text{persistence, reserve, scaling}$$

holds in both continuous time (via #sector-condition-derivation) and discrete time (via this segment), with a quantitative bridge between them (the fluid limit theorem).

## Working Notes

- Non-stationary gain: when $\eta^\ast$ varies over time (as in Kalman filtering with growing $P^-$), the contraction factor $\lambda$ changes per step. The ultimate bound still holds if $\sup_k \lvert\lambda_k\rvert < 1$, but the transient analysis requires time-varying contraction arguments.
- Heavy-tailed disturbances: DA.1S assumes finite second moment. Sub-Weibull or heavy-tailed $w_k$ would need truncation arguments or alternative Lyapunov functions. These extreme cases are better modeled as triggers for structural adaptation ( #structural-adaptation-necessity).
- Non-i.i.d. disturbances: correlated $w_k$ (e.g., Markov environment noise) weakens the supermartingale argument. The contraction still holds per-step, but the steady-state bound requires mixing conditions. This connects to the adversarial coupling analysis in #adversarial-destabilization.
