# Persistence and Structural Limits


## Derived: Deliberation Cost

- **Slug**: `der-deliberation-cost`
- **Type**: derived
- **Status**: conditional
- **Stage**: claims-verified
- **Depends**: `der-action-selection`, `emp-update-gain`, `def-adaptive-tempo`, `form-event-driven-dynamics`

Explicit deliberation improves action quality by using the model for internal simulation before acting — pausing praxis to improve upcoming epistrophe. But deliberation takes time, and during that time aporia accumulates (the environment continues to evolve while the agent is not correcting). Deliberation is justified when the improvement in epistrophe quality exceeds the aporia accumulated during the pause.

**Assumption (local deliberation drift):**

*[Assumption (deliberation-drift)]*

During a deliberation pause of duration $\Delta\tau$, mismatch increases at an approximately constant local rate $\rho_{\text{delib}}$:

$$\Delta\Vert\delta\Vert_{\text{deliberation}} \approx \rho_{\text{delib}} \cdot \Delta\tau$$

This is a short-horizon assumption about inaction windows, not a full global dynamics model. It is weaker than the mismatch ODE and can be estimated directly from pause windows in empirical traces.

**Proposition (deliberation threshold):**

*[Derived (Conditional on deliberation-drift assumption)]*

Deliberation of duration $\Delta\tau$ is net-beneficial when:

$$\Delta\eta^*(\Delta\tau) \cdot \Vert\delta_{\text{post}}\Vert \gt \rho_{\text{delib}} \cdot \Delta\tau$$

where $\Delta\eta^\ast(\Delta\tau)$ is the improvement in post-deliberation update gain and $\Vert\delta_{\text{post}}\Vert$ is the mismatch magnitude the agent will face when it resumes acting.

### Derivation

1. Without deliberation, the agent acts immediately at current tempo $\mathcal{T}_0 = \nu \cdot \eta^\ast_0$.
2. With deliberation of duration $\Delta\tau$, the agent pauses, then acts with improved gain $\eta^\ast_0 + \Delta\eta^\ast$. But during the pause, mismatch has grown by $\rho_{\text{delib}} \cdot \Delta\tau$.
3. The net mismatch reduction from acting after deliberation versus acting immediately: $\text{Net} = \Delta\eta^\ast \cdot \Vert\delta_{\text{post}}\Vert - \rho_{\text{delib}} \cdot \Delta\tau$.
4. Deliberation is justified iff $\text{Net} \gt 0$. $\square$

**Optimal deliberation duration** (under diminishing returns):

*[Derived (Conditional on diminishing-returns + deliberation-drift)]*

$$\Delta\tau^* = \arg\max_{\Delta\tau} \left[\Delta\eta^*(\Delta\tau) \cdot \Vert\delta_{\text{post}}\Vert - \rho_{\text{delib}} \cdot \Delta\tau \right]$$

where $\Vert\delta_{\text{post}}\Vert$ is treated as a parameter estimated by the agent before deliberation begins (not optimized over — the agent estimates the mismatch it will face, then decides how long to deliberate). Under this approximation, the first-order condition is: $\frac{\partial \Delta\eta^\ast}{\partial \Delta\tau} \cdot \Vert\delta_{\text{post}}\Vert = \rho_{\text{delib}}$. Stop deliberating when the marginal improvement rate drops below the mismatch drift rate (normalized by post-deliberation mismatch). When the dependence $\Vert\delta_{\text{post}}\Vert = \Vert\delta_0\Vert + \rho_{\text{delib}} \cdot \Delta\tau$ is included in the optimization, the exact FOC acquires a correction factor $(1 - \Delta\eta^\ast)$ on the cost side; this is negligible when $\Delta\eta^\ast \ll 1$ (the typical case — deliberation produces small gain improvements).

---



## Formulation: Sector Condition (A2')

- **Slug**: `form-sector-condition`
- **Type**: formulation
- **Status**: conditional
- **Stage**: claims-verified
- **Depends**: `def-mismatch-signal`, `def-adaptive-tempo`, `emp-update-gain`

The sector condition (A2') is the structural shape AAT chooses for the correction-function geometry: the correction points roughly inward, with magnitude bounded below relative to the mismatch, on a local region of validity. Together with the companion structural properties (A1) zero-correction-at-zero-mismatch and (A3) tempo-monotonicity, A2' is the formal expression of "the agent's adaptation tracks reality with at least baseline efficiency" — the form on which the persistence and adaptive-reserve results of #deriv-sector-condition rest, and the form which downstream consumers (`#deriv-discrete-sector-condition`, `#deriv-variational-sector-condition`, `#deriv-adaptive-gain-dynamics`, `#der-gain-sector-bridge`) extend, weaken, or ground.

### Setup objects (carried into the form)

Let $\delta(t) \in \mathbb{R}^n$ be the mismatch vector ( #def-mismatch-signal — the difference between the model's predictions and reality across $n$ observable dimensions). Let $F(\mathcal{T}, \delta) \colon \mathbb R_+ \times \mathbb{R}^n \to \mathbb{R}^n$ be the **correction function** — how the agent's adaptive process reduces mismatch — mapping into the same space as $\delta$ so that the inner product $\delta^T F$ is well-defined. This subsumes the update gain $\eta^\ast$ ( #emp-update-gain), event rate $\nu$, and the structure of the update rule. The adaptive tempo $\mathcal{T}$ ( #def-adaptive-tempo) is the rate parameter.

### (A1) Zero Correction at Zero Mismatch

*[Assumption A1]*

$$F(\mathcal{T}, 0) = 0$$

No correction is applied when the model perfectly matches reality. Uncontroversial by construction.

### (A2') Local Sector Condition

There exists a region $\mathcal B_R = \{\delta : \lVert\delta\rVert \leq R\}$ and $\alpha \gt 0$ such that (following the sector-condition framework of Lur'e[^lure1957]):

*[Formulation A2' (sector-condition) — derived in sub-scope $\alpha$, assumed in sub-scope $\beta$ (see Grounding below)]*

$$\delta^T F(\mathcal{T}, \delta) \geq \alpha \lVert\delta\rVert^2 \quad \forall \delta \in \mathcal{B}_R$$

The correction function always points "inward" (reducing mismatch), and its magnitude is bounded below relative to $\lVert\delta\rVert^2$. The linear case has $\alpha = \mathcal{T}$. A saturating correction has $\alpha$ decreasing for large $\lVert\delta\rVert$. A threshold correction has $\alpha = 0$ for small $\lVert\delta\rVert$.

The local form allows the correction to break down outside $\mathcal B_R$ — the structural adaptation regime of #result-structural-adaptation-necessity.

### (A3) Tempo Monotonicity

*[Assumption A3]*

For fixed $\delta$, $\delta^T F(\mathcal{T}, \delta)$ is monotone increasing in $\mathcal{T}$. Higher tempo means faster correction.

### Parameter interpretation

The sector parameter $\alpha$ is determined by the adaptive tempo $\mathcal{T}$ and the structure of the correction function. In the linear case, $\alpha = \mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$. In nonlinear cases, $\alpha$ represents the *worst-case* correction efficiency within the valid region — the minimum ratio of correction power to mismatch magnitude. The radius $R$ represents the model class capacity: how large a mismatch can grow before the correction mechanism fails (i.e., before the sector condition ceases to hold), at which point structural adaptation ( #result-structural-adaptation-necessity) becomes necessary.

---



## Derived: Gain–Sector Bridge

- **Slug**: `der-gain-sector-bridge`
- **Type**: derived
- **Status**: conditional
- **Stage**: claims-verified
- **Depends**: `emp-update-gain`, `def-mismatch-signal`, `form-sector-condition`, `deriv-gain-sector`

The gain-based update principle ( #emp-update-gain) produces correction dynamics satisfying the sector condition (GA-3) whenever the update rule has *directional fidelity* — the correction points at least roughly toward reality. For gradient-based agents, local strong convexity of the loss is sufficient for the one-point sector condition (A2' as stated in #form-sector-condition) and bidirectionally equivalent to the two-point / incremental sector condition (DA2'-inc). The sector parameter $\alpha$ is not a free parameter but is determined by the gain and the correction geometry.

### The Bridge Theorem

*[Derived (gain-sector-bridge, from update-gain + directional fidelity)]*

Given the gain-based update $M_t = M_{t-1} + \eta^\ast \cdot g(\delta_t)$ ( #emp-update-gain), the induced correction function is:

$$F(\delta) = \eta^\ast \cdot H \, g(\delta)$$

where $H$ maps state-space corrections to observation-space mismatch reduction. The sector condition (GA-3) holds with parameter $\alpha > 0$ whenever:

**(B1) Directional fidelity.** The mismatch transform $g$ preserves the mismatch-reducing direction:

$$\delta^T H \, g(\delta) \geq c \lVert\delta\rVert^2 \quad \text{for } \lVert\delta\rVert \leq R$$

for some $c > 0$. The sector parameter is then:

$$\alpha = \eta^\ast \cdot c_{\min}, \qquad c_{\min} = \inf_{\lVert\delta\rVert \leq R} \frac{\delta^T H \, g(\delta)}{\lVert\delta\rVert^2}$$

### Gradient Equivalence

*[Derived (sector-convexity equivalence, two-point form)]*

For any agent updating via gradient descent on a loss $L$ with learning rate $\eta$:

$$\alpha = \eta \cdot \mu \qquad \text{where } \mu = \inf_{\lVert\delta\rVert \leq R} \lambda_{\min}(\nabla^2 L(M^\ast + \delta))$$

is the strong convexity modulus. The basin radius $R$ is the largest ball around the optimum where $\nabla^2 L$ remains positive definite. The equivalence has two forms — bidirectional under the stronger two-point sector condition, one-directional under the one-point form actually used by `#deriv-sector-condition`:

- **Two-point / incremental sector ⇔ strong convexity (full equivalence).** Under the incremental sector bound $(F(\delta_1) - F(\delta_2))^T(\delta_1 - \delta_2) \geq \alpha\lVert\delta_1 - \delta_2\rVert^2$ on $\mathcal B_R(M^\ast)$ — DA2'-inc in #deriv-discrete-sector-condition, the bridge-lemma precondition in #form-composition-closure — the iff holds via Nesterov 2004 Theorem 2.1.10:
  $$\text{Two-point sector with } (\alpha, R) \iff L \text{ is locally } (\alpha/\eta)\text{-strongly convex on } \mathcal B_R(M^\ast).$$
- **One-point sector ⇐ strong convexity (one direction only).** AAT's GA-3 / A2' as stated in #form-sector-condition is the one-point form $\delta^T F(\delta) \geq \alpha\lVert\delta\rVert^2$ at $\delta^\ast = 0$. Strong convexity implies the one-point sector ($\alpha = \eta\mu$); the converse fails. Counterexample: $L'(x) = x(1 + \tfrac{1}{2}\sin(10x))$ satisfies $x \cdot L'(x) \geq \tfrac{1}{2} x^2$ globally yet has $L''(\pi/10) \lt 0$, so it is not convex on any neighborhood of $x^\ast = 0$. The one-point sector at the equilibrium is genuinely weaker than full local strong convexity (cf. #result-sector-persistence-template's one-point/two-point distinction). Full proofs and the counterexample analysis in #deriv-gain-sector Prop B.4.

### Verified Instances

| Update class | Bridge status | Sector parameter $\alpha$ | Valid region |
|---|---|---|---|
| Scalar Kalman | Derived | $K = P^-/(P^- + R_{\text{obs}}) = \eta^\ast$ | Global |
| Matrix Kalman | Derived | $\lambda_{\min}^+(KH)$ in $(P^-)^{-1}$-norm | Observable subspace |
| Beta-Bernoulli | Derived | $1/(n+1) = \eta_{\text{edge}}$ | Global |
| Exponential family (natural params), bounded scope $\Theta_0 \subset \operatorname{int}(\Theta)$ | Derived | $\eta \cdot \mu_0$ where $\mu_0 = \inf_{\theta \in \Theta_0} \lambda_{\min}(\mathbf I(\theta)) \gt 0$ | $\Theta_0$ (compact / interior-bounded) — global only when the family has a uniform Fisher lower bound |
| Gradient on strongly convex loss | Derived | $\eta \cdot \mu$ | Global ($R = \infty$) |
| Gradient on locally convex loss | Derived | $\eta \cdot \mu_{\text{local}}$ | Basin of attraction |
| Gradient on non-convex loss | Fails at basin boundary | N/A beyond $R$ | Finite $R$ |
| SPR-tuned PID on positive-real plant with anti-windup | Derived | $\alpha_{\text{PID}} = \omega_c \sin(\varphi_m) / \kappa(P)$ (phase margin as sector constant; crossover frequency as tempo; KYP-certificate condition number as degradation) | Classical linear regime + Lur'e sector-bounded nonlinearity within specified plant-Lipschitz threshold |

### Failure Modes

The bridge fails precisely in five cases:

1. **Directional infidelity.** The mismatch transform $g$ rotates the correction away from the mismatch ($\delta^T H g(\delta) \leq 0$). Occurs with pathological parameterizations or severe model-observation misalignment. For optimal Bayesian updates, B1 holds by construction.

2. **Gain collapse.** $\eta^\ast \to 0$ while $\rho > 0$, so $\alpha \to 0$ and the persistence condition eventually fails. Not a failure of the bridge but of the persistence condition — see the gain-collapse analysis in #emp-update-gain.

3. **Nonlinear saturation.** The correction function $g$ saturates at large $\lVert\delta\rVert$, so the sector ratio $\delta^T g(\delta)/\lVert\delta\rVert^2$ decays. The sector condition holds locally with $\alpha$ depending on $R$. This is exactly what A2' (the local sector condition) is designed for.

4. **Unobservable directions.** When $\ker(H) \neq \{0\}$, the correction has no effect on mismatch in unobservable directions. The sector condition holds only in the observable subspace. See #der-observability-dominance.

5. **Model misspecification.** The model class does not contain the truth, so the gradient direction is wrong. B1 fails because the correction aims at the wrong target. This is the #result-structural-adaptation-necessity trigger.

---



## Result: Sector Condition Stability

- **Slug**: `result-sector-condition-stability`
- **Type**: result
- **Status**: exact
- **Stage**: claims-verified
- **Depends**: `def-adaptive-tempo`, `def-mismatch-signal`, `deriv-sector-condition`, `result-sector-persistence-template`

An agent's mismatch remains bounded if its correction function satisfies a sector condition (points inward with at least baseline efficiency) and the effective correction strength exceeds the environmental disturbance rate.

This segment is the **single-agent epistemic instantiation** of the sector-persistence template ( #result-sector-persistence-template). The template's state variable is $\xi = \delta(t) \in \mathbb{R}^n$ (model-reality mismatch); the correction function is $F(\mathcal{T}, \delta)$; the disturbance is environmental ($w(t)$); the region of validity $R$ is the model class capacity.

*[Formulation]*

$$\frac{d\delta}{dt} = -F(\mathcal{T}, \delta) + w(t)$$

*[Assumption (sector-condition)]*

$F$ satisfies the local sector condition (template condition (T2)) for $\lVert\delta\rVert \leq R$:

$$\delta^T F(\mathcal{T}, \delta) \geq \alpha \lVert\delta\rVert^2$$

with $\alpha \gt 0$. Disturbance is bounded: $\lVert w(t)\rVert \leq \rho$ (Model D, GA-2) or $\mathbb{E}[\lVert w(t)\rVert^2] = \sigma_w^2$ (Model S, GA-2S). Grounding of (T2) for gain-based agents: #der-gain-sector-bridge gives $\alpha = \eta^\ast \cdot c_{\min}$. The linear case $F = \mathcal{T} \cdot \delta$ yields $\alpha = \mathcal{T}$ exactly.

*[Derived (from sector-persistence-template)]*

The template's Model D conclusion specializes to: $\delta(t)$ is ultimately bounded by $R^\ast = \rho/\alpha$, and the agent persists iff

$$\alpha \gt \frac{\rho}{R}.$$

The adaptive reserve is $\Delta\rho^\ast = \alpha R - \rho$ — the additional disturbance the agent can absorb before $R^\ast$ exceeds the valid region.

The template's Model S conclusion specializes to: the steady-state RMS mismatch is $R^\ast_S = \sigma_w\sqrt{n/(2\alpha)}$ (where $n = \dim(\delta)$), and mean-square persistence requires $\alpha \gt n\sigma_w^2/(2R^2)$. Model D scales as $1/\alpha$; Model S scales as $1/\sqrt{\alpha}$ — correction is less effective against noise than against drift.

Full Lyapunov proofs: #deriv-sector-condition Props A.1, A.1S, A.2.

---



## Result: Persistence Condition

- **Slug**: `result-persistence-condition`
- **Type**: result
- **Status**: exact
- **Stage**: claims-verified
- **Depends**: `def-adaptive-tempo`, `def-mismatch-signal`, `result-sector-condition-stability`, `result-sector-persistence-template`

An agent persists when two independent conditions hold: the correction machinery can contain mismatch within its operating region (*structural persistence*), and the resulting steady-state mismatch is small enough for the agent's actions to remain adequate (*task adequacy*).

This segment is the canonical single-agent instantiation of the sector-persistence template ( #result-sector-persistence-template) with state variable $\xi = \delta_t$ (epistemic mismatch), correction function $F(\mathcal{T}, \delta)$, and disturbance rate $\rho_\xi = \rho$ (environmental change rate). Structural persistence is the direct template conclusion. Task adequacy adds a domain-specific constraint beyond the template's reach.

### Structural Persistence

*[Derived (structural-persistence, from sector-persistence-template)]*

Applying the template to the single-agent epistemic case gives: the correction machinery bounds $\delta$ within the model class capacity iff

$$\alpha \gt \frac{\rho}{R} \quad \text{(Model D)} \qquad \alpha \gt \frac{n\sigma_w^2}{2R^2} \quad \text{(Model S)}$$

with ultimate bound $R^\ast = \rho/\alpha$ (Model D) or $R^\ast_S = \sigma_w\sqrt{n/(2\alpha)}$ (Model S). See #result-sector-condition-stability for how (T1)–(T3) are verified in this instantiation, and #deriv-sector-condition for the proof. Structural persistence is a property of the adaptive architecture — the machinery's ability to contain mismatch — not of the task.

**Linear case.** When $F(\mathcal{T}, \delta) = \mathcal{T}\delta$, $\alpha = \mathcal{T}$ and $R \to \infty$, so structural persistence is trivially satisfied whenever $\mathcal{T} \gt 0$. The binding constraint then becomes task adequacy (below).

### Task Adequacy

*[Definition (task-adequacy)]*

The steady-state mismatch is small enough for the agent's actions to remain acceptable:

$$R^\ast \lt \lVert\delta_{\text{critical}}\rVert$$

where $\lVert\delta_{\text{critical}}\rVert$ is a domain-specific tolerance threshold — "how wrong can the model be before the agent's actions become harmful or ineffective?" This is set by the application domain, not derived by AAT.

**Task adequacy is a separate condition from structural persistence.** An agent can be structurally persistent ($R^\ast \lt R$) but task-inadequate ($R^\ast \gt \lVert\delta_{\text{critical}}\rVert$) — the machinery contains mismatch, but not tightly enough for the domain's needs. Conversely, when $\lVert\delta_{\text{critical}}\rVert \lt R$ (the domain's tolerance is stricter than the model class capacity), task adequacy is the binding constraint.

### Operational Persistence Condition

*[Derived (operational-persistence, conjunction of structural persistence + task adequacy)]*

The agent persists operationally when BOTH conditions hold. In the nonlinear case with $\lVert\delta_{\text{critical}}\rVert \lt R$, the binding condition is:

$$\alpha \gt \frac{\rho}{\lVert\delta_{\text{critical}}\rVert} \quad \text{(Model D)} \qquad \alpha \gt \frac{n\sigma_w^2}{2\lVert\delta_{\text{critical}}\rVert^2} \quad \text{(Model S)}$$

These are the same as the structural conditions with $R$ replaced by $\lVert\delta_{\text{critical}}\rVert$, because when $\lVert\delta_{\text{critical}}\rVert \lt R$, task adequacy is stricter.

**Linear operational forms:** In the linear case ($\alpha = \mathcal{T}$, $R \to \infty$), structural persistence is trivially satisfied and the operational condition reduces to task adequacy alone:

$$\mathcal{T} \gt \frac{\rho}{\lVert\delta_{\text{critical}}\rVert} \quad \text{(Model D)} \qquad \mathcal{T} \gt \frac{n\sigma_w^2}{2\lVert\delta_{\text{critical}}\rVert^2} \quad \text{(Model S)}$$

These are the forms used throughout the theory as the operational persistence condition. They are exact for linear correction and useful proxies for mildly nonlinear correction (where $\alpha \approx \mathcal{T}$), but they overstate the persistence margin when the correction function saturates, because they omit the structural constraint ($\alpha \gt \rho/R$) that becomes binding when $R$ is finite.

**Per-dimension (Model S):** $\eta_k \gt c \cdot \rho_k^2 / \delta_{\text{critical},k}^2$ where $c$ depends on the probability guarantee. See #result-per-dimension-persistence.

### The relationship between $\alpha$ and $\mathcal{T}$

#der-gain-sector-bridge shows that for agents with directional fidelity, $\alpha = \eta^\ast \cdot c_{\min}$ where $c_{\min}$ is the worst-case directional fidelity. For linear correction (Kalman, Beta-Bernoulli), $\alpha = \mathcal{T}$ exactly. For gradient descent on strongly convex losses, $\alpha = \eta \cdot \mu$ where $\mu$ is the strong convexity modulus — monotone in $\eta$ (and hence in $\mathcal{T}$) for fixed loss landscape. For nonlinear correction tested in simulation (saturating, sigmoid, threshold), $\alpha$ remains monotone increasing in $\mathcal{T}$: for a saturating function with capacity $R$, $\alpha \approx \mathcal{T}/2$ (worst case at the capacity boundary); for sigmoid (tanh), $\alpha \approx 0.76 \cdot \mathcal{T}$. The qualitative conclusion — "faster adaptation improves persistence" — is structurally grounded for the important cases and empirically confirmed for all correction function classes tested.

### Per-Dimension Extension

*[Empirical Claim (per-dimension-persistence, from simulation variant F)]*

For anisotropic systems (non-uniform $\rho$ or $\mathcal{T}$ across dimensions), the scalar persistence condition is insufficient. Per-dimension:

$$\mathcal{T}_k \gt \frac{\rho_k}{\delta_{\text{critical},k}} \quad \text{for each dimension } k$$

The scalar condition overestimates by up to 72% in simulation. The weak dimension is the bottleneck (84% of total mismatch in simulation). See #result-per-dimension-persistence.

**Robustness**: The per-dimension condition matches discrete AR(1) prediction to 4 significant figures. The scalar overestimate is a consequence of Jensen's inequality applied to the norm.

---



## Result: Structural Adaptation Necessity

- **Slug**: `result-structural-adaptation-necessity`
- **Type**: result
- **Status**: conditional
- **Stage**: claims-verified
- **Depends**: `def-model-sufficiency`, `def-model-class-fitness`, `result-mismatch-decomposition`, `emp-update-gain`

When model class fitness is insufficient — when no model in the current class can adequately represent reality — no amount of parametric adaptation can close the mismatch floor. The agent must change its model class, not just its parameters.

*[Derived (structural-adaptation-necessity)]*

If the model class fitness $\mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$ for some $\varepsilon \gt 0$, then no parametric adaptation within $\mathcal{M}$ can reduce the expected mismatch below a floor determined by $\varepsilon$ (under the alignment assumption — see Epistemic Status). Without the alignment assumption, the result holds for irreducible proper-scoring regret rather than one-step mean mismatch. The qualitative conclusion is the same either way: parametric adaptation cannot compensate for model-class inadequacy.

### Derivation

1. By definition, $S(M^\ast) = \mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$ where $M^\ast = \arg\sup_{M \in \mathcal{M}} S(M)$.
2. Therefore $I(\mathcal{C}_t; o_{t+1:\infty} \mid M^\ast, a_{t:\infty}) \gt 0$: the history contains predictive information that $M^\ast$ does not capture.
3. This uncaptured information manifests as *systematic* mismatch — structured residuals $\delta_t$ containing signal, not merely noise.
4. From #result-mismatch-decomposition, the model error component has a positive lower bound that cannot be reduced by any $M \in \mathcal{M}$.
5. The update rule ( #emp-update-gain) adjusts $M_t$ within $\mathcal{M}$, but $M^\ast$ is already (approximately) reached. Further updates oscillate without net improvement.
6. Therefore: reducing mismatch below the floor requires changing $\mathcal{M}$ — structural adaptation. $\square$

**Corollary.** Persistent irreducible mismatch (after parametric convergence) is *diagnostic* of model class inadequacy. Systematic patterns in residuals are evidence that $\mathcal{F}(\mathcal{M})$ is insufficient.

---



## Derived: Temporal Nesting

- **Slug**: `der-temporal-nesting`
- **Type**: derived
- **Status**: robust-qualitative
- **Stage**: deps-verified
- **Depends**: `def-adaptive-tempo`, `result-structural-adaptation-necessity`

An agent's adaptive processes stratify naturally by timescale, with each level operating on the quasi-steady-state output of the level below. Faster processes must approximately converge before slower ones act on their output.

*[Derived (temporal-nesting)]*

$$\nu_{\text{level } n+1} \ll \nu_{\text{level } n}$$

for each adjacent pair of adaptive timescales. If a slower process acts before the faster process beneath it has converged, the system oscillates — the slower process adjusts based on transient behavior rather than settled dynamics.

| Timescale | Process | What changes |
|-----------|---------|-------------|
| Fastest | Reactive response | Action given current model |
| Fast | Parametric update (online) | Model parameters within $\mathcal{M}$ |
| Intermediate | Consolidation (offline, cf. #form-consolidation-dynamics) | Redistribution of information within $M_t$'s sub-state factorization toward IB-optimum |
| Slow | Structural adaptation | Model class $\mathcal{M}$ |
| Slowest | Architectural change | The agent's fundamental structure |

This table is illustrative — real systems may have additional intermediate levels. The number of distinguishable timescales is not fixed; what matters is the structural relationship between adjacent levels.

---



## Scope: Agent Identity as Singular Causal Trajectory

- **Slug**: `scope-agent-identity`
- **Type**: scope
- **Status**: robust-qualitative
- **Stage**: draft
- **Depends**: `def-chronica`, `def-model-sufficiency`

AAT applies to agents instantiated on singular causal trajectories. Identity within AAT is grounded not in the model state $M_t$ (which can be copied) but in the unique causal trajectory $\mathcal C_t$ (which cannot).

*[Scope (scope-agent-identity, from chronica + model-sufficiency)]*

**Scope commitment.** AAT's formal apparatus presumes each agent is instantiated on a **singular, non-forkable causal trajectory** $\mathcal C_t$ ( #def-chronica). Sufficiency of the model state $M_t$ ( #def-model-sufficiency) is defined *relative to* this trajectory — not relative to a model-state equivalence class. Duplicating $M_t$ and exposing the copies to different future events produces two agents with *divergent* causal histories, each of which is a sufficient statistic only for *its own* trajectory.

**Three consequences of the scope commitment:**

1. **Sufficiency is trajectory-indexed.** $S(M_t)$ ( #def-model-sufficiency) measures against *this* agent's $\mathcal C_t$; not against a hypothetical parallel copy's $\mathcal C_t^{(2)}$.

2. **Model merging is lossy by construction.** Reconciling the models of two agents that share a prefix of their trajectory but have diverged requires choosing which causal history to privilege; no generally optimal merge exists. This is a structural constraint of the scope, not a defect of any particular merge algorithm.

3. **The loop's interventional access depends on the trajectory's singularity.** When the agent acts and observes, the observation is the response to *its* intervention on *its* single trajectory. Replaying a saved $M_t$ against a different event stream is not the same as intervening — the observed consequences are under a different causal trajectory. This grounds the interventional interpretation in #der-loop-interventional-access: the loop provides Level-2-quality data precisely because the agent is on a singular trajectory, not because of any architectural property of the agent itself.

**Natural extension: parameterization-invariance (PI).** The scope commitment motivates a companion axiom. AAT's predictions concern a singular causal trajectory $\mathcal C_t$; the trajectory itself is coordinate-free, while any parameterization of $M_t$'s internal state space is a modeling convention. Requiring AAT's theorems to be invariant under change of parameterization — *(PI): the theory's conclusions do not depend on arbitrary choice of coordinates on $M_t$* — is a natural axiomatic commitment consistent with (but not directly forced by) the three consequences above. When (PI) is adopted and combined with Čencov's 1982 uniqueness theorem (*Statistical Decision Rules and Optimal Inference*, AMS), the Fisher information metric is uniquely forced on statistical-manifold sub-cases of $M_t$ — which converts Fisher-metric-dependent derivations in #der-gain-sector-bridge from theorem-imported to AAT-internally-forced, and adds a fourth primary instance to the uniqueness-theorem-forced-coordinate pattern named in #disc-additive-coordinate-forcing (see that segment's four-instance table for structural positioning). (PI) is a genuine axiomatic choice — its cost is that AAT carries an additional invariance commitment at the scope layer; its benefit is that several Fisher-metric results throughout AAT become derivable rather than imported. The commitment is structurally analogous to the chain-rule-additivity and evidential-additivity axioms that ground the divergence-layer and update-layer Cauchy-FE theorems: each is a natural-from-adjacent-AAT-commitment axiom that a uniqueness theorem then operates on.

**What the scope excludes (or requires additional machinery for):**

- Agents conceived as type/equivalence-class entities (e.g., "the GPT-4 model") rather than token/trajectory entities (e.g., "this particular session with state $M_t$ on trajectory $\mathcal C_t$"). AAT's formal results apply to tokens, not types. Aggregated claims across tokens of the same type require additional machinery (e.g., population-level dynamics; see Section III gaps on latent structural diversity).
- "Clone problem" scenarios where multiple copies of an agent are formally the same until divergence — each copy becomes its own AAT agent at the moment it acquires a distinct event (Discussion below).
- Formal treatment of reincarnation, restoration from backup, or other operations that attempt to transplant $M_t$ across trajectories. AAT's sufficiency machinery does not apply across trajectory discontinuities; such operations are out-of-scope events whose epistemic consequences require separate treatment.

---
