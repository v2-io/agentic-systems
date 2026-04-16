---
slug: linear-ode-approximation
type: detail
status: exact
depends:
  - mismatch-dynamics
  - adaptive-tempo
  - sector-condition-stability
  - sector-condition-derivation
  - discrete-sector-condition
stage: draft
---

# Detail: Linear ODE Approximation

The full linear treatment of mismatch dynamics: scalar and vector forms, steady-state solutions under both disturbance models, transient behavior, convergence rate, validity conditions, breakdown modes, discrete-time connection, and adversarial coupling. This appendix collects the linear-case results that #mismatch-dynamics states as a hypothesis, derives them explicitly, and delineates exactly where the linear approximation is valid and where it fails.

## Formal Expression

### 1. The scalar and vector forms

The mismatch vector $\delta(t) \in \mathbb{R}^n$ evolves under the general dynamics from #sector-condition-derivation:

*[Definition (vector dynamics)]*

$$\frac{d\delta}{dt} = -F(\mathcal{T}, \delta) + w(t)$$

The **linear approximation** sets $F(\mathcal{T}, \delta) = \mathcal{T} \cdot \delta$, giving:

*[Hypothesis (linear-vector-ode)]*

$$\frac{d\delta}{dt} = -\mathcal{T} \cdot \delta + w(t)$$

This is exact when the correction function is linear in $\delta$ (Kalman filter, Beta-Bernoulli conjugate update). It is an approximation otherwise.

**Scalar form (equality).** For a scalar mismatch $\delta(t) \in \mathbb{R}$:

*[Derived (scalar-ode, from linear-vector-ode with $n = 1$)]*

$$\frac{d\delta}{dt} = -\mathcal{T} \cdot \delta + w(t)$$

This is an equality: the scalar ODE is exactly the $n = 1$ case of the vector ODE.

**Norm form (inequality).** For vector $\delta \in \mathbb{R}^n$, take the time derivative of $\lVert\delta\rVert = (\delta^T \delta)^{1/2}$:

$$\frac{d\lVert\delta\rVert}{dt} = \frac{\delta^T \dot\delta}{\lVert\delta\rVert} = \frac{\delta^T(-\mathcal{T}\delta + w)}{\lVert\delta\rVert} = -\mathcal{T}\lVert\delta\rVert + \frac{\delta^T w}{\lVert\delta\rVert}$$

By Cauchy-Schwarz, $\delta^T w / \lVert\delta\rVert \leq \lVert w\rVert$. Under Model D (GA-2: $\lVert w(t)\rVert \leq \rho$):

*[Derived (norm-inequality, from Cauchy-Schwarz)]*

$$\frac{d\lVert\delta\rVert}{dt} \leq -\mathcal{T} \cdot \lVert\delta\rVert + \rho$$

**This is an inequality, not an equality.** The Cauchy-Schwarz step is tight only when $w(t)$ is parallel to $\delta(t)$ (worst-case disturbance). The norm form stated in #mismatch-dynamics is this upper bound. For the scalar case ($n = 1$), Cauchy-Schwarz is automatically tight and the inequality becomes an equality.

### 2. Steady-state solutions

#### Model D (deterministic bounded disturbance, GA-2: $\lVert w(t)\rVert \leq \rho$)

Setting $d\lVert\delta\rVert/dt = 0$ in the norm inequality gives the worst-case steady state:

*[Derived (model-d-steady-state, from norm inequality)]*

$$\lVert\delta\rVert_{ss} = \frac{\rho}{\mathcal{T}}$$

This is the tight upper bound: steady-state mismatch equals the ratio of disturbance to correction. In the scalar case ($n = 1$), this is exact (the Ornstein-Uhlenbeck process with deterministic forcing converges to $\rho/\mathcal{T}$). In the vector case, it is the worst case over all disturbance directions.

#### Model S (stochastic zero-mean disturbance, GA-2S: $d\delta = -\mathcal{T}\delta\,dt + \sigma_w\,dW_t$)

The Ornstein-Uhlenbeck process has stationary variance derived via Ito-Lyapunov analysis (Prop A.1S in #sector-condition-derivation, specialized to $\alpha = \mathcal{T}$):

*[Derived (model-s-steady-state, from Ito-Lyapunov with linear correction)]*

$$\mathbb{E}[\lVert\delta\rVert^2]_{ss} = \frac{n\sigma_w^2}{2\mathcal{T}}$$

The RMS steady-state mismatch is:

$$\lVert\delta\rVert_{\text{rms}} = \sigma_w\sqrt{\frac{n}{2\mathcal{T}}}$$

For the scalar case ($n = 1$): $\lVert\delta\rVert_{\text{rms}} = \sigma_w / \sqrt{2\mathcal{T}}$.

**Scaling difference.** Model D gives $\lVert\delta\rVert_{ss} \propto 1/\mathcal{T}$; Model S gives $\lVert\delta\rVert_{\text{rms}} \propto 1/\sqrt{\mathcal{T}}$. Doubling the correction rate halves the deterministic steady-state mismatch but only reduces the stochastic steady-state by a factor of $\sqrt{2} \approx 1.41$. Correction is less effective against noise than against drift.

### 3. Transient solution

**Model D, constant $\rho$.** The linear ODE $d\lVert\delta\rVert/dt = -\mathcal{T}\lVert\delta\rVert + \rho$ with initial condition $\lVert\delta(0)\rVert = \lVert\delta_0\rVert$ has the standard first-order linear solution:

*[Derived (transient-model-d)]*

$$\lVert\delta(t)\rVert = \lVert\delta_0\rVert\,e^{-\mathcal{T} t} + \frac{\rho}{\mathcal{T}}(1 - e^{-\mathcal{T} t})$$

Mismatch decays exponentially from initial conditions toward the steady state $\rho/\mathcal{T}$ with time constant $\tau = 1/\mathcal{T}$. After $k$ time constants, the transient has decayed by a factor of $e^{-k}$: 63% after one time constant, 95% after three, 99.3% after five.

**Model S, Ornstein-Uhlenbeck.** The mean-square mismatch evolves as (from Prop A.1S with $\alpha = \mathcal{T}$):

*[Derived (transient-model-s)]*

$$\mathbb{E}[\lVert\delta(t)\rVert^2] = \lVert\delta_0\rVert^2\,e^{-2\mathcal{T} t} + \frac{n\sigma_w^2}{2\mathcal{T}}(1 - e^{-2\mathcal{T} t})$$

The variance converges twice as fast as the mean (rate $2\mathcal{T}$ vs. $\mathcal{T}$) because the Lyapunov function $V = \frac{1}{2}\lVert\delta\rVert^2$ is quadratic — its dynamics have doubled exponential rate.

### 4. When the linear approximation is valid

The linear case $F(\mathcal{T}, \delta) = \mathcal{T} \cdot \delta$ is a special case of the sector condition (GA-3) from #sector-condition-stability with:

*[Derived (linear-sector-parameters)]*

$$\alpha = \mathcal{T}, \qquad R \to \infty$$

That is, the sector condition holds globally with lower bound $\alpha$ equal to the tempo, and the sector-condition region has infinite radius. In the notation of #gain-sector-bridge:

- **Directional fidelity parameter:** $c_{\min} = 1$ (the correction points exactly at the mismatch).
- **Sector parameter:** $\alpha = \eta^\ast \cdot c_{\min} = \eta^\ast = \mathcal{T}/\nu$.
- **No upper saturation:** $c_{\max} = c_{\min} = 1$ (the sector bounds coincide).

**Consequence for persistence.** With $R \to \infty$, structural persistence ($\alpha \gt \rho/R$) is trivially satisfied for any $\mathcal{T} \gt 0$. The binding constraint is task adequacy alone: $\mathcal{T} \gt \rho/\lVert\delta_{\text{critical}}\rVert$ (Model D) or $\mathcal{T} \gt n\sigma_w^2 / (2\lVert\delta_{\text{critical}}\rVert^2)$ (Model S). This is why the linear operational forms in #persistence-condition exist: in the linear world, structural persistence is free.

**The linear approximation is exact when:**

1. **Kalman filter** (scalar or matrix): the gain $K_t$ produces $F(\delta) = K_t H \delta$, which is linear. The sector parameter equals the Kalman gain: $\alpha = K$ (scalar) or $\alpha = \lambda_{\min}^+(KH)$ (matrix). See #gain-sector-bridge.

2. **Beta-Bernoulli conjugate update:** the correction $F(\delta) = \delta/(n+1)$ is linear with $\alpha = 1/(n+1) = \eta_{\text{edge}}$.

3. **Exponential family with natural parameters:** the natural-parameter update is linear in the sufficient statistic, giving $\alpha = \eta \cdot \lambda_{\min}(\text{Fisher})$.

4. **Gradient descent on quadratic loss:** $F(\delta) = \eta \nabla^2 L \cdot \delta$ is linear with $\alpha = \eta \cdot \lambda_{\min}(\nabla^2 L)$.

### 5. When the linear approximation breaks down

The linear form $F = \mathcal{T} \cdot \delta$ fails when the true correction function deviates from linearity. Three failure modes, each corresponding to a specific nonlinearity:

**Saturation at large $\lVert\delta\rVert$.** The correction mechanism is overwhelmed by large mismatch. The true correction satisfies $F(\delta) \lt \mathcal{T}\lVert\delta\rVert$ for large $\lVert\delta\rVert$ — correction is slower than the linear prediction. Simulation confirms: for a saturating function $g(\delta) = \delta / (1 + \lvert\delta\rvert/R)$, the sector parameter at the capacity boundary is $\alpha \approx \mathcal{T}/2$ (half the linear value). The linear approximation overstates persistence margins. The sector-condition framework ( #sector-condition-stability) handles this via finite $R$ and reduced $\alpha$.

**Threshold effects at small $\lVert\delta\rVert$.** Below a detection threshold $\varepsilon$, small mismatches go uncorrected: $F(\delta) \approx 0$ for $\lVert\delta\rVert \lt \varepsilon$. This creates a dead zone where the model drifts. The linear approximation (which predicts correction at all scales) misses this. The sector condition fails locally at small $\lVert\delta\rVert$ (the ratio $\delta^T F / \lVert\delta\rVert^2 \to 0$), but the dead zone is bounded and does not affect large-scale stability.

**Structural breakdown.** Beyond some critical mismatch, the correction rate drops to zero because the model class is no longer appropriate: the mismatch exceeds the model's representational capacity. $F(\delta) \approx 0$ for $\lVert\delta\rVert \gt R$. This is the structural adaptation trigger ( #structural-adaptation-necessity). The linear approximation, which predicts correction growing without bound, misses this entirely. The sector-condition framework captures it via the finite radius $R$ of the sector-condition region.

### 6. Discrete-time connection

The continuous ODE is a fluid-limit approximation of the discrete event-driven dynamics ( #event-driven-dynamics). The discrete mismatch dynamics are:

$$\delta_{k+1} = \delta_k - \eta^\ast F_d(\delta_k) + w_k$$

In the linear case ($F_d(\delta) = \delta$), this becomes:

$$\delta_{k+1} = (1 - \eta^\ast)\delta_k + w_k$$

which is an AR(1) process with coefficient $\lambda = 1 - \eta^\ast$.

#discrete-sector-condition proves the formal connection:

**Model D.** The discrete and continuous steady states are *identical* — the fluid-limit gap is exactly zero. Both give $R^\ast = \rho/\alpha$. The discrete form has $\alpha = (1 - \lvert\lambda\rvert)/\eta^\ast = (1 - \lvert 1 - \eta^\ast\rvert)/\eta^\ast$, which equals $1$ (hence $\alpha_{\text{continuous}} = \nu \cdot 1 = \mathcal{T}$) when $0 \lt \eta^\ast \lt 1$.

**Model S.** The discrete steady-state variance is $\sigma^2_{\text{step}} / (1 - \lambda^2_{\text{eff}})$, which recovers the continuous result $n\sigma_w^2/(2\mathcal{T})$ in the fluid limit ($\eta^\ast \to 0$, $\nu \to \infty$, $\nu\eta^\ast = \mathcal{T}$ fixed). The variance gap is $O((\eta^\ast)^2 c^2_{\max})$ — quantitatively small whenever $\eta^\ast c_{\max} \ll 1$.

**Fluid-limit validity.** The ODE approximation is formally justified by the fluid limit theorem in #discrete-sector-condition (conditional on Lipschitz regularity of $F_d$). The approximation is most accurate when $\eta^\ast \ll 1$ (the small-gain regime). It is least accurate during initial transients when $\eta^\ast$ is large, but this phase is short-lived and the transient error is bounded by $O(\eta^\ast c_{\max} / \nu^{1/2})$.

### 7. Adversarial coupling in the linear case

When two agents are coupled, $A$'s praxis contributes to $B$'s disturbance:

*[Hypothesis (Linear Coupling Model)]*

$$\rho_B = \rho_{B,\text{base}} + \gamma_A \cdot \mathcal{T}_A$$

Under the linear approximation, the steady-state mismatches (Model D, coupling-dominant: $\gamma_A \mathcal{T}_A \gg \rho_{B,\text{base}}$) are:

*[Derived (linear-adversarial-steady-state, from Model D steady state + coupling model)]*

$$\lVert\delta_B\rVert_{ss} \approx \frac{\gamma_A \mathcal{T}_A}{\mathcal{T}_B}, \qquad \lVert\delta_A\rVert_{ss} \approx \frac{\gamma_B \mathcal{T}_B}{\mathcal{T}_A}$$

The ratio:

*[Derived (squared-tempo-law, from linear steady states)]*

$$\frac{\lVert\delta_B\rVert_{ss}}{\lVert\delta_A\rVert_{ss}} = \frac{\gamma_A}{\gamma_B}\left(\frac{\mathcal{T}_A}{\mathcal{T}_B}\right)^2$$

Under symmetric coupling ($\gamma_A \approx \gamma_B$), tempo advantage squares: a 2:1 tempo ratio yields a 4:1 mismatch ratio; a 3:1 ratio yields 9:1.

**Why the squared law.** The exponent 2 arises because the $1/\mathcal{T}$ steady-state scaling appears in both numerator (faster agent generates more disturbance) and denominator (faster agent corrects better): one power from the coupling, one from the steady-state. Under Model S (stochastic coupling, $1/\sqrt{\mathcal{T}}$ scaling), the exponent reduces to $3/2$. See #adversarial-exponent-regimes for the full regime analysis.

**Simulation validation.** Variant A confirmed $b = 1.999$ (Model D, coupling-dominant). Variants C-D confirmed $b = 1.481$ (Model S, coupling-dominant). Both within numerical precision of the derived values. See #simulation-results.

## Epistemic Status

*Exact for the linear case.* The linear ODE is a standard first-order linear system; the solutions (transient and steady-state, both Model D and Model S) are textbook results for the Ornstein-Uhlenbeck process and its deterministic analog. The sector-condition parameters ($\alpha = \mathcal{T}$, $R \to \infty$) are exact when the correction function is linear. The discrete-time connection is exact (zero gap for Model D, $O((\eta^\ast)^2)$ gap for Model S). The adversarial scaling law ($b = 2$ for Model D, $b = 3/2$ for Model S) is derived and simulation-validated.

**What is exact vs. what is an approximation.** The linear ODE is exact for systems with linear correction dynamics (Kalman, Beta-Bernoulli, quadratic loss). For nonlinear systems, the linear ODE is a local Taylor approximation valid near the steady state. The sector-condition framework ( #sector-condition-stability, #sector-condition-derivation) is the general treatment; this appendix derives what falls out when the sector bounds coincide.

**The norm form is an upper bound for $n \gt 1$.** The inequality introduced by Cauchy-Schwarz at the norm step is tight only in the worst case. For typical disturbances that are not persistently aligned with the mismatch direction, the actual norm trajectory lies below the upper bound. The scalar case ($n = 1$) is an equality. This distinction is load-bearing: downstream results that use $d\lVert\delta\rVert/dt = -\mathcal{T}\lVert\delta\rVert + \rho$ as an equality (e.g., the exact transient solution, the exact steady-state ratio) are strictly correct only for $n = 1$ or for worst-case disturbance. The Lyapunov analysis in #sector-condition-derivation avoids this issue by working with $V = \frac{1}{2}\lVert\delta\rVert^2$ directly, without passing through the norm derivative.

**Max attainable:** exact (the linear case is its own exact analysis; there is nothing to tighten).

## Discussion

**Why this appendix exists.** The linear ODE in #mismatch-dynamics is labeled as a hypothesis and described as a "first-order approximation." That is correct for the general case. But for agents with linear correction dynamics, the ODE is not an approximation at all -- it is exact. This appendix serves two roles: (1) providing the complete derivation that #mismatch-dynamics points to rather than carrying inline, and (2) making precise when the "approximation" is exact and when it genuinely introduces error.

**Pedagogical value.** The linear case is the entry point for understanding ACT's mismatch dynamics. The closed-form solutions (exponential convergence, ratio steady state, squared scaling law) build intuition that the general sector-condition results ( #sector-condition-stability) cannot provide -- Lyapunov gives bounds and existence, not quantitative trajectories. The linear treatment also connects directly to the AR(1) simulation framework ( #simulation-results) and classical control theory (PI controllers, Kalman filters).

**Speed-quality substitutability.** From $\mathcal{T} = \nu \cdot \eta^\ast$ (single channel): doubling event rate $\nu$ has the same effect on $\lVert\delta\rVert_{ss}$ as doubling update quality $\eta^\ast$. They are multiplicative when both improve: 50% improvement in each yields $1.5 \times 1.5 = 2.25\times$, not $3\times$. This is the formal analog of Boyd's insight that Orient quality often matters more than raw OODA speed.

**The persistence threshold in the linear world.** From the steady state: $\lVert\delta\rVert_{ss} \lt \lVert\delta_{\text{critical}}\rVert$ iff $\mathcal{T} \gt \rho/\lVert\delta_{\text{critical}}\rVert$ (Model D). This is task adequacy only -- structural persistence is trivially satisfied because $R \to \infty$. The linear world makes persistence look easier than it is. For nonlinear agents, both structural and task-adequacy conditions must hold ( #persistence-condition).

## Working Notes

- The vector ODE $d\delta/dt = -\mathcal{T}\delta + w$ assumes isotropic correction (same rate in all directions). For anisotropic agents (tempo tensor $\mathbf{T}$), the linear ODE generalizes to $d\delta/dt = -\mathbf{T}\delta + w$ with matrix exponential solutions and per-eigenvalue convergence rates. The per-dimension persistence condition ($\mathcal{T}_k \gt \rho_k / \delta_{\text{critical},k}$) from #per-dimension-persistence is the diagonal special case.
- The norm-inequality subtlety (Section 1 above) propagates into the adversarial scaling law: the squared law ($b = 2$) is exact for $n = 1$ and a worst-case upper bound for $n \gt 1$. Whether this matters quantitatively for multi-dimensional adversarial dynamics has not been tested in simulation.
- Model S's Ito-Lyapunov derivation assumes $\sigma_w$ is constant. When the noise scale depends on state ($\sigma_w(\delta)$, as in multiplicative noise models), the Ornstein-Uhlenbeck analysis no longer applies and the steady-state formula changes. The sector-condition results in #sector-condition-derivation handle additive noise only.
