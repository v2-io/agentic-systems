# Appendix — Details (group 2)


## Derivation: Critical-Mass Composition

- **Slug**: `deriv-critical-mass-composition`
- **Type**: derivation
- **Status**: conditional
- **Stage**: draft
- **Depends**: `form-composition-closure`, `scope-composite-agent`, `result-sector-persistence-template`, `deriv-sector-condition`, `der-team-persistence`, `der-adversarial-destabilization`, `hyp-symbiogenic-composition`, `result-unity-closure-mapping`

The composite sector constant $\alpha_c$ is derived — not merely bounded from below — for the symmetric-matched-Tier-1 two-agent case, yielding a closed-form critical-mass inequality in which the sign of the inter-agent coupling $\gamma$ and the teleological unity $U_O$ enter explicitly. The result subsumes the weakest-link bound, recovers #der-team-persistence (cooperative) and #der-adversarial-destabilization (adversarial) as signed special cases, formalizes #hyp-symbiogenic-composition's autonomy-reduction mechanism as an asymmetric Lyapunov-weight limit, and makes the scope-gate from #scope-composite-agent explicit as the second conjunct of composite persistence.

### Setup

Two sub-agents $A_1, A_2$, each a **Tier 1 agent** in the sense of #form-composition-closure's bridge-lemma taxonomy — mismatch-driven update, linear prediction, incremental sector-Lipschitz correction (Kalman, exponential-family Bayesian, gradient-on-strongly-convex, linear-with-PD-KH). **Matched architectures**: $f_1, f_2$ are structurally the same function, with $\alpha_1 = \alpha_2 = \alpha$, $R_1 = R_2 = R$. Disturbance statistics shared: each sees bounded $w_i(t)$ with $\lVert w_i\rVert \leq \rho$ (Model D, per #result-sector-persistence-template).

*[Formulation (coupling-model-C1, from #der-team-persistence + #der-adversarial-destabilization)]*

Inter-agent coupling enters additively to the disturbance at rate $\gamma \mathcal T_j$:

$$\rho_i^{\text{eff}} = \rho + \gamma \mathcal T_j \tag{C1}$$

with sign convention $\gamma \lt 0$ cooperative (ally's tempo-contribution reduces disturbance, recovering #der-team-persistence's $-\gamma^{\text{coop}}\mathcal T_j$ term), $\gamma \gt 0$ adversarial (ally's tempo-contribution amplifies disturbance, recovering #der-adversarial-destabilization's $+\gamma_A\mathcal T_A$ term). Symmetric case: $\gamma_{1 \to 2} = \gamma_{2 \to 1} = \gamma$.

*[Formulation (coordination-cost-C2)]*

Coordination overhead reduces each agent's effective correction rate symmetrically:

$$\alpha_i^{\text{eff}} = \alpha - C \tag{C2}$$

with $C \geq 0$ the $\Delta \mathcal T_i^{\text{cost}}$ from #der-team-persistence's coordination-overhead threshold.

### Critical-mass inequality (symmetric-matched-Tier-1 case)

*[Derived (critical-mass-symmetric, from #result-sector-persistence-template + C1 + C2)]*

Let $\xi = (\delta_1, \delta_2)^T$ and take the joint quadratic Lyapunov candidate $V(\xi) = \tfrac{1}{2}(\lVert\delta_1\rVert^2 + \lVert\delta_2\rVert^2)$. Under the block-diagonal correction structure with cross-coupling absorbed into $\rho_i^{\text{eff}}$ via (C1), and using $\lVert\delta_1\rVert + \lVert\delta_2\rVert \leq \sqrt{2(\lVert\delta_1\rVert^2 + \lVert\delta_2\rVert^2)}$ (Cauchy–Schwarz):

$$\dot V \leq -(\alpha - C)(\lVert\delta_1\rVert^2 + \lVert\delta_2\rVert^2) + (\rho + \gamma\mathcal T)\sqrt{2(\lVert\delta_1\rVert^2 + \lVert\delta_2\rVert^2)}.$$

Setting $\dot V = 0$ gives the ultimate bound on $\lVert\xi\rVert$ and, projecting to the macro-state $\delta_c = (\delta_1 + \delta_2)/\sqrt{2}$, the ultimate composite mismatch

$$R_c^\ast \leq \frac{\rho + \gamma\mathcal T}{\alpha - C}. \tag{L4}$$

The composite persists iff $R_c^\ast \lt R_c$. Inheriting $R_c = R$ from the symmetric-matched averaging projection:

$$\boxed{\;(\alpha - C)\,R \;\gt\; \rho + \gamma\mathcal T\;} \tag{CM2}$$

Rearranging into the composite contraction-rate form:

$$\kappa_c \;:=\; (\alpha - C) \;-\; \frac{\rho + \gamma\mathcal T}{R}, \qquad \text{composite persists iff } \kappa_c \gt 0. \tag{KC}$$

### Specialization checks

Under matched symmetry, (CM2) reduces correctly in four limits:

| Limit | Setting | (CM2) reduces to | Recovers |
|---|---|---|---|
| No coupling | $\gamma = 0$, $C = 0$ | $\alpha R \gt \rho$ | Single-agent #result-persistence-condition |
| Cooperative-symmetric | $\gamma \lt 0$, $C = 0$ | $\alpha R \gt \rho + \gamma\mathcal T$ (easier than individual) | #der-team-persistence's "teams persist where individuals can't" |
| Adversarial-symmetric | $\gamma \gt 0$, $C = 0$ | Fails when $\gamma\mathcal T \gt \alpha R - \rho$ | #der-adversarial-destabilization threshold (symmetric) |
| Coordination-dominated | $C \gt \alpha$, $\gamma = 0$ | LHS $\lt 0$; composite fails | Brooks's Law |

### Subsumption of the weakest-link bound

*[Derived (weakest-link-subsumption)]*

The weakest-link bound $\alpha_c \geq \min_i(\alpha_i - \Delta\mathcal T_i^{\text{cost}})$ from #form-composition-closure's derivation table specializes under matched symmetry to $\alpha_c \geq \alpha - C$. (KC) refines this by making the composite's effective disturbance explicit as $\rho + \gamma\mathcal T$, turning a correction-rate bound into a full persistence inequality. Critically, (KC) can yield $\kappa_c \gt 0$ even when the weakest-link bound alone fails — when cooperative coupling ($\gamma\mathcal T \lt 0$) reduces the effective disturbance below what the raw $\alpha - C$ margin would permit. The weakest-link bound cannot see this because it does not account for $\gamma$'s sign.

### $U_O$ entry: multiplicative-on-$\gamma$ plus scope-gate

*[Derived (unity-multiplicative-modulator, conditional on LQR-compatible action structure)]*

In a purposeful-agent setting where each sub-agent optimizes a quadratic objective $L_i(\omega) = \tfrac{1}{2}(\omega - r_i)^T Q(\omega - r_i)$ with target $r_i$, and $U_O := \operatorname{corr}(r_1, r_2)$ is the target correlation per #def-unity-dimensions' $U_O$, the cross-coupling in the joint dynamics has sign and magnitude controlled by $U_O$:

$$\gamma(U_O) \;=\; -\,\gamma_{\max}\, U_O, \qquad \gamma_{\max} \gt 0, \tag{UO-mult}$$

via aligned targets → aligned action directions in the shared environment → constructive (cooperative) cross-contribution in the symmetric eigendirection. Substituting into (KC):

$$\kappa_c(U_O) \;=\; (\alpha - C)R \;-\; \rho \;+\; \gamma_{\max}\,U_O\,\mathcal T. \tag{CM3}$$

*[Scope (scope-gate-from-composition-scope-condition)]*

(CM3) is necessary but not sufficient for composite existence. Under #scope-composite-agent, a composite exists as an AAT agent only when one of the three disjunctive alignment routes (shared objective, hierarchical derivation, mutual benefit) is satisfied. Below this threshold, no coherent $O_c$ is definable and composite-level quantities — including $R_c$ on the right of (CM2) — are ill-typed. The honest statement of composite persistence is therefore the conjunction:

$$\boxed{\;\kappa_c(U_O) \gt 0 \;\wedge\; \text{\#scope-composite-agent satisfied} \;\Leftrightarrow\; \text{composite persists as AAT agent}\;} \tag{CM4}$$

$U_O$ enters (CM4) in two independent ways: multiplicatively within (CM3), and as scope-gate via #scope-composite-agent. It does **not** enter purely additively as a separate reserve term — there is no free-floating "$U_O$ contribution" detached from the coupling it modulates.

### Asymmetric limit and symbiogenic composition

*[Sketch (asymmetric-limit-symbiogenesis, from weighted Lyapunov)]*

Drop the matched-symmetric assumption. Let $\alpha_1 \gg \alpha_2$ with $\alpha_2 \to 0$. The unweighted joint Lyapunov $V = \tfrac{1}{2}(\lVert\delta_1\rVert^2 + \lVert\delta_2\rVert^2)$ fails (the weakest-link ultimate bound diverges as $\alpha_2 \to 0$). A **weighted** Lyapunov $V_\mu(\xi) = \tfrac{1}{2}(\lVert\delta_1\rVert^2 + \mu\lVert\delta_2\rVert^2)$ with $\mu \to 0$ yields

$$\dot V_\mu \leq -\alpha_1\lVert\delta_1\rVert^2 + \rho_1\lVert\delta_1\rVert \;+\; O(\mu),$$

so in the limit the composite's stability is controlled **entirely by agent 1**; agent 2's autonomous correction dynamics are weighted out of the stability accounting.

This provides a Lyapunov-weighted formalization of #hyp-symbiogenic-composition's **(S-3) autonomy reduction**: the endosymbiont's effective action space contracts ($\mathcal A_e^{\text{effective}} \to \mathcal A_e^{\text{restricted}}$) and its autonomous dynamics fall out of the joint Lyapunov argument. The asymmetric limit is a smooth deformation of (CM4), not a discontinuous regime change — symbiogenesis and peer coupling are parameter-limits of the same weighted-Lyapunov analysis. The result does **not** close #hyp-symbiogenic-composition's (S-1) objective absorption or (S-2) function transfer: what happens to agent 1's state space when it inherits structure from agent 2 is a separate question the weighting argument does not address.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Coupling model (C1): $\rho_i^{\text{eff}} = \rho + \gamma\mathcal T_j$ | Import from #der-team-persistence and #der-adversarial-destabilization | Formulation choice (requirement for the derivation) |
| Coordination-cost model (C2): $\alpha_i^{\text{eff}} = \alpha - C$ | Import from #der-team-persistence's coordination-overhead threshold | Formulation choice |
| Joint quadratic Lyapunov $V = \tfrac{1}{2}(\lVert\delta_1\rVert^2 + \lVert\delta_2\rVert^2)$ | Standard vector-Lyapunov construction (Matrosov 1962; Bellman 1962) | Formulation choice (canonical for matched-symmetric dyads) |
| Ultimate bound $R_c^\ast \leq (\rho + \gamma\mathcal T)/(\alpha - C)$ | Lyapunov dissipation + Cauchy–Schwarz | Derived |
| Critical-mass inequality (CM2): $(\alpha - C)R \gt \rho + \gamma\mathcal T$ | (L4) + sector-region fit $R_c^\ast \lt R_c = R$ | Derived (conditional on Tier 1 + matched-symmetric + Model D) |
| Four specialization checks (no-coupling / cooperative / adversarial / coordination-dominated) | Direct substitution into (CM2) | Proved (within stated scope) |
| Subsumption of weakest-link bound | (CM2) sign-sensitive; weakest-link is sign-blind | Proved |
| (UO-mult): $\gamma(U_O) = -\gamma_{\max}U_O$ | LQR-compatibility sketch; aligned targets → aligned actions → constructive cross-contribution | Discussion-grade |
| Composite persistence as (CM3) ∧ scope-satisfaction: (CM4) | (KC) with (UO-mult) + #scope-composite-agent | Derived (conditional) |
| Asymmetric limit → #hyp-symbiogenic-composition (S-3) via weighted Lyapunov | Matrosov-style weighting; $\mu \to 0$ limit | Sketch (the weighting is standard; the identification with (S-3) is structurally motivated but not a theorem) |
| (S-1) objective absorption and (S-2) function transfer formalizations | Not addressed by this derivation | Open (in #hyp-symbiogenic-composition Working Notes) |
| Heterogeneous-architecture case ($A_1$ Tier 1, $A_2$ Tier 2/3) | Requires per-sub-agent tiering per #form-composition-closure | Open |
| Heterogeneous-metric Tier-1M dyad ($\lambda_1 \neq \lambda_2$, $C_1 \neq C_2$, $k_{12} \neq k_{21}$) | #result-contraction-template (CM2-M) via Slotine 2003 negative-feedback small-gain: $(\lambda_1 - C_1)(\lambda_2 - C_2) \gt k_{12} k_{21}/4$ | Derived (conditional on #result-contraction-template (CT2) preconditions + Slotine 2003) |
| Nonlinear coupling $\gamma = \gamma(\delta_j)$ | Requires full joint-Lyapunov machinery from #der-adversarial-destabilization (effects-spiral corollary) | Open |
| Dynamic coordination cost $C = C_0 + C_1\lVert\delta_j\rVert$ | Quadratic inequality; admits closed form, loses interpretive cleanliness | Open |
| Fully-coupled tempo dynamics ($\mathcal T_i$ responsive to $\delta_j$) | Requires joint tempo analysis from #der-adversarial-destabilization Working Notes | Open |
| $N \gt 2$ scaling of (CM4) | Conjunction over pairwise terms generalizes but loses closed form; see `spikes/spike-composition-scaling-N.md` | Open |

The dividing line: (C1), (C2), and the quadratic Lyapunov candidate are **formulation choices** imported from adjacent segments or from standard Lyapunov practice. The *consequences* under these choices — (L4), (CM2), (KC), the specialization checks, the weakest-link subsumption, and (CM4) with its scope-gate conjunct — are **derived**. The $U_O$-multiplicative modulator (UO-mult) is discussion-grade: it uses an LQR-compatibility argument whose rigor depends on an action-space inner-product analysis deferred to #result-unity-closure-mapping. The asymmetric-limit identification with #hyp-symbiogenic-composition (S-3) is sketch-level — the weighted-Lyapunov argument is standard but the semantic identification with autonomy reduction is structural, not proved.

---



## Sketch: Multi-Timescale Stability

- **Slug**: `sketch-multi-timescale-stability`
- **Type**: sketch
- **Status**: sketch
- **Stage**: draft
- **Depends**: `result-sector-condition-stability`, `der-temporal-nesting`

When adaptive processes operate at $N$ nested timescales, composite stability requires each level to be stable given its slower levels, with sufficient timescale separation between adjacent pairs.

*[Formulation (multi-timescale-stability sketch)]*

### The General $N$-Timescale System

The temporal nesting in #der-temporal-nesting creates a coupled multi-timescale system with $N$ levels. Singular perturbation theory provides tools to analyze such systems. Define a hierarchy of state variables:

*[Definition (State Hierarchy)]*

$$x^{(1)}, \; x^{(2)}, \; \ldots, \; x^{(N)}$$

where $x^{(1)}$ is the fastest (e.g., mismatch at the reactive/parametric level) and $x^{(N)}$ is the slowest (e.g., architectural or meta-structural state). The coupled dynamics:

*[Formulation (N-Timescale Dynamics)]*

$$\dot{x}^{(k)} = \frac{1}{\epsilon_k} \, G^{(k)}\!\left(x^{(1)}, \ldots, x^{(N)}\right) + w^{(k)}(t)$$

where $\epsilon_1 \ll \epsilon_2 \ll \cdots \ll \epsilon_N$ encode the timescale separation and each $G^{(k)}$ may depend on the states at all levels.

### The Two-Timescale Special Case

The simplest nontrivial instance has $N = 2$:

- Fast state $x^{(1)} = \delta$ (mismatch under parametric adaptation)
- Slow state $x^{(2)} = \mathcal{M}$ (model class, changing on a structural timescale)

$$\dot{x}^{(1)} = -F(\mathcal{T}, x^{(1)}; x^{(2)}) + w(t) \quad \text{(fast: parametric adaptation)}$$

$$\dot{x}^{(2)} = \epsilon \, G(x^{(1)}, x^{(2)}) \quad \text{(slow: structural adaptation)}$$

where $\epsilon \ll 1$ reflects the timescale separation and $F$ depends on $x^{(2)}$ (the correction function is determined by the current model class).

### Sketch of Approach (General Case)

The standard singular perturbation result (Tikhonov 1952, "Systems of differential equations containing a small parameter multiplying the derivative," *Matematicheskii Sbornik* 31(3):575–586; generalized $N$-level form per Khalil 2002, *Nonlinear Systems* (3rd ed.), Prentice Hall, Chapter 11) applies layer by layer: if level $k$ is stable for each fixed configuration of the slower levels $k+1, \ldots, N$ (each level has a stable attractor given the levels above it), and each successive slow manifold is itself stable, then the composite $N$-level system is stable.

#der-temporal-nesting's convergence constraint $\nu_{n+1} \ll \nu_n$ is the condition ensuring sufficient timescale separation at each boundary — i.e., $\epsilon_k / \epsilon_{k+1} \ll 1$ for each $k$. When this separation is violated between any adjacent pair, the faster level's transients contaminate the slower level's dynamics, potentially destabilizing the composite system.

---



## Derivation: Discrete-Time Sector Condition

- **Slug**: `deriv-discrete-sector-condition`
- **Type**: derivation
- **Status**: conditional
- **Stage**: draft
- **Depends**: `deriv-sector-condition`, `emp-update-gain`, `der-gain-sector-bridge`, `form-event-driven-dynamics`

Discrete-time analogs of Props A.1, A.1S, and A.2 via contraction mapping, closing the fluid-limit gap (GA-5) between the event-driven dynamics ( #form-event-driven-dynamics) and the continuous-time Lyapunov results in #deriv-sector-condition.

### Setup

The discrete mismatch dynamics at event step $k$ are:

*[Definition (Discrete Dynamics)]*

$$\delta_{k+1} = \delta_k - \eta^\ast F_d(\delta_k) + w_k$$

where $\eta^\ast$ is the update gain ( #emp-update-gain), $F_d$ is the discrete correction direction, and $w_k$ is the per-step disturbance. The continuous correction function $F(\mathcal{T}, \delta)$ from #deriv-sector-condition decomposes as $F = \nu \cdot \eta^\ast \cdot F_d$ at event rate $\nu$.

### (DA2') Discrete Sector-Lipschitz Condition

*[Assumption DA2' (discrete-sector-condition)]*

There exist constants $c_{\min} > 0$ and $c_{\max} < 2/\eta^\ast$ such that for all $\lVert\delta\rVert \leq R$:

**(DA2'a) Lower sector bound (directional fidelity):**

$$\delta^T F_d(\delta) \geq c_{\min} \lVert\delta\rVert^2$$

**(DA2'b) Lipschitz bound (bounded correction magnitude):**

$$\lVert F_d(\delta)\rVert \leq c_{\max} \lVert\delta\rVert$$

The **lower bound** (DA2'a) is directional fidelity — the correction points inward, identical to the continuous sector condition (A2') from #form-sector-condition via #der-gain-sector-bridge.

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

The discrete-to-continuous gap for Model S variance is $O(\eta^\ast c_{\max}^2/c_{\min}^2) = O(c_{\max}^2/(c_{\min}^2\,\nu))$, dominated by the conditioning ratio $c_{\max}^2/c_{\min}^2$. Substituting $\sigma^2_{\text{step}} = n\sigma_w^2/\nu$ and $\eta^\ast = \mathcal{T}/\nu$ into $V_{ss} = \sigma^2_{\text{step}}/(1 - \lambda^2_{\text{eff}})$ and Taylor-expanding at small $\eta^\ast$:

$$\frac{V_{ss}}{V_c} = \frac{1}{1 - \eta^\ast c_{\max}^2/(2 c_{\min})} = 1 + \frac{\eta^\ast c_{\max}^2}{2 c_{\min}} + O((\eta^\ast)^2)$$

so

$$V_{ss} - V_c \approx \frac{n\sigma_w^2\, c_{\max}^2}{4 c_{\min}^2\, \nu}$$

— a leading correction that scales as $1/\nu$. The $(\eta^\ast)^2 \lVert F_d\rVert^2$ term in the per-step recurrence enters $1 - \lambda^2_{\text{eff}}$ at order $(\eta^\ast)^2$, but the steady-state ratio $\sigma^2_{\text{step}}/(1 - \lambda^2_{\text{eff}})$ inverts the leading $2\eta^\ast c_{\min}$ contraction, yielding $O(\eta^\ast)$ asymptotic gap rather than $O((\eta^\ast)^2)$. This quantifies the error introduced by GA-5 and confirms it is small whenever $c_{\max}^2/(c_{\min}^2 \nu) \ll 1$.

### Fluid Limit Theorem

*[Derived (Conditional on Lipschitz regularity)]*

**Statement.** Let $F_d$ be Lipschitz continuous with constant $L_F$ on $\mathcal B_R$. Let $\delta^{(\nu)}(t)$ denote the piecewise-constant interpolation of the discrete trajectory at event rate $\nu$, and $\delta(t)$ the solution of the continuous ODE $d\delta/dt = -F(\mathcal{T}, \delta) + w(t)$ with $F = \nu \eta^\ast F_d$. Then:

$$\sup_{t \in [0,T]} \lVert\delta^{(\nu)}(t) - \delta(t)\rVert \leq C \cdot \frac{\eta^\ast c_{\max}}{\nu^{1/2}}$$

for a constant $C$ depending on $T$, $L_F$, and $R$.

**Sketch.** This follows from the standard ODE-approximation theory for Euler schemes (Kushner & Yin, 2003, Ch. 5). The discrete update $\delta_{k+1} = \delta_k - \eta^\ast F_d(\delta_k) + w_k$ is a forward Euler step for the ODE with step size $1/\nu$. The Lipschitz condition on $F_d$ ensures the local truncation error is $O(1/\nu^2)$. Summing over $O(\nu T)$ steps and applying the Gronwall inequality gives the $O(1/\nu^{1/2})$ bound.

For Model D (deterministic): the steady-state gap is exactly zero (both discrete and continuous converge to the same fixed point). The fluid-limit error affects only transients.

For Model S (stochastic): the steady-state variance gap is $O(\eta^\ast c_{\max}^2/c_{\min}^2) = O(c_{\max}^2/(c_{\min}^2\,\nu))$, dominated by the conditioning ratio $c_{\max}^2/c_{\min}^2$. The $(\eta^\ast)^2 \lVert F_d\rVert^2$ term in the per-step recurrence enters $1 - \lambda^2_{\text{eff}}$ at order $(\eta^\ast)^2$, but inverting the leading $2\eta^\ast c_{\min}$ in $V_{ss} = \sigma^2_{\text{step}}/(1 - \lambda^2_{\text{eff}})$ produces an $O(\eta^\ast)$ asymptotic gap, not $O((\eta^\ast)^2)$ — see the recovery calculation in Prop DA.1S above.

---



## Detail: Linear ODE Approximation

- **Slug**: `detail-linear-ode-approximation`
- **Type**: detail
- **Status**: exact
- **Stage**: draft
- **Depends**: `hyp-mismatch-dynamics`, `def-adaptive-tempo`, `result-sector-condition-stability`, `deriv-sector-condition`, `deriv-discrete-sector-condition`

The full linear treatment of mismatch dynamics: scalar and vector forms, steady-state solutions under both disturbance models, transient behavior, convergence rate, validity conditions, breakdown modes, discrete-time connection, and adversarial coupling. This appendix collects the linear-case results that #hyp-mismatch-dynamics states as a hypothesis, derives them explicitly, and delineates exactly where the linear approximation is valid and where it fails.

### 1. The scalar and vector forms

The mismatch vector $\delta(t) \in \mathbb{R}^n$ evolves under the general dynamics from #deriv-sector-condition:

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

**This is an inequality, not an equality.** The Cauchy-Schwarz step is tight only when $w(t)$ is parallel to $\delta(t)$ (worst-case disturbance). The norm form stated in #hyp-mismatch-dynamics is this upper bound. For the scalar case ($n = 1$), Cauchy-Schwarz is automatically tight and the inequality becomes an equality.

### 2. Steady-state solutions

#### Model D (deterministic bounded disturbance, GA-2: $\lVert w(t)\rVert \leq \rho$)

Setting $d\lVert\delta\rVert/dt = 0$ in the norm inequality gives the worst-case steady state:

*[Derived (model-d-steady-state, from norm inequality)]*

$$\lVert\delta\rVert_{ss} = \frac{\rho}{\mathcal{T}}$$

This is the tight upper bound: steady-state mismatch equals the ratio of disturbance to correction. In the scalar case ($n = 1$), this is exact (the Ornstein-Uhlenbeck process with deterministic forcing converges to $\rho/\mathcal{T}$). In the vector case, it is the worst case over all disturbance directions.

#### Model S (stochastic zero-mean disturbance, GA-2S: $d\delta = -\mathcal{T}\delta\,dt + \sigma_w\,dW_t$)

The Ornstein-Uhlenbeck process has stationary variance derived via Ito-Lyapunov analysis (Prop A.1S in #deriv-sector-condition, specialized to $\alpha = \mathcal{T}$):

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

The linear case $F(\mathcal{T}, \delta) = \mathcal{T} \cdot \delta$ is a special case of the sector condition (GA-3) from #result-sector-condition-stability with:

*[Derived (linear-sector-parameters)]*

$$\alpha = \mathcal{T}, \qquad R \to \infty$$

That is, the sector condition holds globally with lower bound $\alpha$ equal to the tempo, and the sector-condition region has infinite radius. In the notation of #der-gain-sector-bridge:

- **Directional fidelity parameter:** $c_{\min} = 1$ (the correction points exactly at the mismatch).
- **Sector parameter:** $\alpha = \eta^\ast \cdot c_{\min} = \eta^\ast = \mathcal{T}/\nu$.
- **No upper saturation:** $c_{\max} = c_{\min} = 1$ (the sector bounds coincide).

**Consequence for persistence.** With $R \to \infty$, structural persistence ($\alpha \gt \rho/R$) is trivially satisfied for any $\mathcal{T} \gt 0$. The binding constraint is task adequacy alone: $\mathcal{T} \gt \rho/\lVert\delta_{\text{critical}}\rVert$ (Model D) or $\mathcal{T} \gt n\sigma_w^2 / (2\lVert\delta_{\text{critical}}\rVert^2)$ (Model S). This is why the linear operational forms in #result-persistence-condition exist: in the linear world, structural persistence is free.

**The linear approximation is exact when:**

1. **Kalman filter** (scalar or matrix): the gain $K_t$ produces $F(\delta) = K_t H \delta$, which is linear. The sector parameter equals the Kalman gain: $\alpha = K$ (scalar) or $\alpha = \lambda_{\min}^+(KH)$ (matrix). See #der-gain-sector-bridge.

2. **Beta-Bernoulli conjugate update:** the correction $F(\delta) = \delta/(n+1)$ is linear with $\alpha = 1/(n+1) = \eta_{\text{edge}}$.

3. **Exponential family with natural parameters:** the natural-parameter update is linear in the sufficient statistic, giving $\alpha = \eta \cdot \lambda_{\min}(\text{Fisher})$.

4. **Gradient descent on quadratic loss:** $F(\delta) = \eta \nabla^2 L \cdot \delta$ is linear with $\alpha = \eta \cdot \lambda_{\min}(\nabla^2 L)$.

### 5. When the linear approximation breaks down

The linear form $F = \mathcal{T} \cdot \delta$ fails when the true correction function deviates from linearity. Three failure modes, each corresponding to a specific nonlinearity:

**Saturation at large $\lVert\delta\rVert$.** The correction mechanism is overwhelmed by large mismatch. The true correction satisfies $F(\delta) \lt \mathcal{T}\lVert\delta\rVert$ for large $\lVert\delta\rVert$ — correction is slower than the linear prediction. Simulation confirms: for a saturating function $g(\delta) = \delta / (1 + \lvert\delta\rvert/R)$, the sector parameter at the capacity boundary is $\alpha \approx \mathcal{T}/2$ (half the linear value). The linear approximation overstates persistence margins. The sector-condition framework ( #result-sector-condition-stability) handles this via finite $R$ and reduced $\alpha$.

**Threshold effects at small $\lVert\delta\rVert$.** Below a detection threshold $\varepsilon$, small mismatches go uncorrected: $F(\delta) \approx 0$ for $\lVert\delta\rVert \lt \varepsilon$. This creates a dead zone where the model drifts. The linear approximation (which predicts correction at all scales) misses this. The sector condition fails locally at small $\lVert\delta\rVert$ (the ratio $\delta^T F / \lVert\delta\rVert^2 \to 0$), but the dead zone is bounded and does not affect large-scale stability.

**Structural breakdown.** Beyond some critical mismatch, the correction rate drops to zero because the model class is no longer appropriate: the mismatch exceeds the model's representational capacity. $F(\delta) \approx 0$ for $\lVert\delta\rVert \gt R$. This is the structural adaptation trigger ( #result-structural-adaptation-necessity). The linear approximation, which predicts correction growing without bound, misses this entirely. The sector-condition framework captures it via the finite radius $R$ of the sector-condition region.

### 6. Discrete-time connection

The continuous ODE is a fluid-limit approximation of the discrete event-driven dynamics ( #form-event-driven-dynamics). The discrete mismatch dynamics are:

$$\delta_{k+1} = \delta_k - \eta^\ast F_d(\delta_k) + w_k$$

In the linear case ($F_d(\delta) = \delta$), this becomes:

$$\delta_{k+1} = (1 - \eta^\ast)\delta_k + w_k$$

which is an AR(1) process with coefficient $\lambda = 1 - \eta^\ast$.

#deriv-discrete-sector-condition proves the formal connection:

**Model D.** The discrete and continuous steady states are *identical* — the fluid-limit gap is exactly zero. Both give $R^\ast = \rho/\alpha$. The discrete form has $\alpha = (1 - \lvert\lambda\rvert)/\eta^\ast = (1 - \lvert 1 - \eta^\ast\rvert)/\eta^\ast$, which equals $1$ (hence $\alpha_{\text{continuous}} = \nu \cdot 1 = \mathcal{T}$) when $0 \lt \eta^\ast \lt 1$.

**Model S.** The discrete steady-state variance is $\sigma^2_{\text{step}} / (1 - \lambda^2_{\text{eff}})$, which recovers the continuous result $n\sigma_w^2/(2\mathcal{T})$ in the fluid limit ($\eta^\ast \to 0$, $\nu \to \infty$, $\nu\eta^\ast = \mathcal{T}$ fixed). The variance gap is $O(\eta^\ast c_{\max}^2/c_{\min}^2) = O(c_{\max}^2/(c_{\min}^2\,\nu))$ — quantitatively small whenever $c_{\max}^2/(c_{\min}^2\,\nu) \ll 1$. See #deriv-discrete-sector-condition for the leading-order Taylor expansion that gives this scaling.

**Fluid-limit validity.** The ODE approximation is formally justified by the fluid limit theorem in #deriv-discrete-sector-condition (conditional on Lipschitz regularity of $F_d$). The approximation is most accurate when $\eta^\ast \ll 1$ (the small-gain regime). It is least accurate during initial transients when $\eta^\ast$ is large, but this phase is short-lived and the transient error is bounded by $O(\eta^\ast c_{\max} / \nu^{1/2})$.

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

**Why the squared law.** The exponent 2 arises because the $1/\mathcal{T}$ steady-state scaling appears in both numerator (faster agent generates more disturbance) and denominator (faster agent corrects better): one power from the coupling, one from the steady-state. Under Model S (stochastic coupling, $1/\sqrt{\mathcal{T}}$ scaling), the exponent reduces to $3/2$. See #result-adversarial-exponent-regimes for the full regime analysis.

**Simulation validation.** Variant A confirmed $b = 1.999$ (Model D, coupling-dominant). Variants C-D confirmed $b = 1.481$ (Model S, coupling-dominant). Both within numerical precision of the derived values. See #obs-section-i-validation-simulations.

---



## Derivation: Graph Structure Uniqueness

- **Slug**: `deriv-graph-structure-uniqueness`
- **Type**: derivation
- **Status**: conditional
- **Stage**: claims-verified
- **Depends**: `def-strategy-dag`, `der-chain-confidence-decay`, `norm-explicit-strategy-condition`, `post-causal-structure`

Operational requirements on the agent's representation — directed temporal ordering, probabilistic uncertainty, and the ability to test strategy components — are *sufficient* for the strategy to be a directed acyclic graph with the Markov factorization property. The argument parallels Cox's theorem for probability in *form* but not yet in *strength*: Cox's theorem is necessary-and-sufficient (the only measure satisfying the desiderata is probability); this result is sufficient only (the desiderata guarantee DAG+Markov, but no one has shown a non-DAG structure cannot satisfy them). Acyclicity and directed edges are *proved* from temporal ordering over a finite horizon; the Markov factorization is *proved under causal sufficiency* via the Causal Markov Condition theorem (Spirtes–Glymour–Scheines, Pearl). A fourth postulate (observable intermediates) is required for localized strategic diagnosis but not for the representation or persistence results themselves.

**How far the Cox parallel goes.** Cox's theorem starts from desiderata on how a rational agent should quantify uncertainty (consistency, universality, continuous functional composition) and proves that the *only* measure satisfying them is probability — necessity. This segment starts from desiderata on how a bounded agent can represent its strategy under causal action (directed temporal order, probabilistic edge uncertainty, causal sufficiency of the chosen nodes) and proves that DAG+Markov *suffices* to satisfy them — sufficiency. The necessity direction — no non-DAG structure (factor graphs, junction trees with cyclic message schedules, chain graphs) can satisfy P1–P4 plus causal sufficiency — is not established here. In practical terms this gap is unimportant because the proved sufficiency gives a rigorous grounding for the DAG structure; claims that AAT's strategy *must* be a DAG should be read as "must-if-sufficient-via-this-route," not as a proved necessity. A stronger Cox-style result is open. The placement of the DAG structure on a footing comparable to probability — a consequence of operational requirements rather than a modeling convenience — holds in the sufficiency direction; the full parallel with Cox awaits a uniqueness argument.

### The Postulates

Four properties that a strategy representation must satisfy. Each is independently motivated from the adaptive-systems foundation.

#### P1: Directed Temporal Ordering

*[Derived (from #post-causal-structure)]*

If component $A$ of the strategy causally produces component $B$, then $A$ temporally precedes $B$. The strategy representation must respect this directionality — edges point from causes to effects, from actions to outcomes, from prerequisites to goals.

This is a consequence of the temporal postulate ( #post-causal-structure): the arrow of time is constitutive, not incidental. Reversing a causal edge would mean effects precede causes, which is physically impossible.

#### P2: Probabilistic Uncertainty

*[Derived (from Cox's theorem)]*

The agent's uncertainty about whether each step of the strategy will succeed must be quantified by a measure satisfying Cox's axioms (consistency, universality, non-negativity). The unique such measure is probability (Cox 1946, "Probability, Frequency and Reasonable Expectation," *American Journal of Physics* 14(1):1–13; modern exposition in Jaynes 2003, *Probability Theory: The Logic of Science*, Cambridge University Press, Chapter 2). The agent may use other representations internally (confidence scores, fuzzy logic), but these must be mappable to probability to be consistent.

#### P3: State-Local Revisability

*[Derived (from #der-chain-confidence-decay + bounded computation)]*

When the agent observes evidence about one component of its strategy (e.g., "step 3 succeeded" or "prerequisite 2 is blocked"), it must be able to update its beliefs about that component and its consequences without recomputing the entire strategy from scratch.

**Why this is forced, not chosen:**

*From fragility.* Additive log-confidence ( #der-chain-confidence-decay) means longer chains are exponentially less reliable. The agent will frequently encounter partial failures. Each partial failure requires re-evaluation of the affected portion of the strategy. If each re-evaluation requires full recomputation, the agent's planning tempo $T_\Sigma$ is catastrophically slow — potentially violating the strategy persistence condition.

*From bounded computation.* The agent has finite computational resources (the IB constraint applies to planning as well as model maintenance). Full recomputation of a strategy with $N$ components costs $O(N)$ or worse. Local revision costs $O(\lvert\text{affected}\rvert)$, which can be much smaller.

*From the persistence condition.* Strategy must be revised faster than the environment invalidates it. Local revision directly increases $T_\Sigma$ by reducing the per-update cost. An agent that must recompute everything on each update has lower $T_\Sigma$ and is more likely to fall below the persistence threshold.

#### P4: Observable Intermediates

*[Derived (from #der-chain-confidence-decay + monitoring requirement)]*

To support **localized strategic diagnosis and revision**, the strategy representation benefits from internal checkpoints — observable states between the initial action and the final goal — that the agent can monitor to detect partial failure.

Without intermediates, the agent cannot detect chain failure until the final outcome. By the time the final outcome reveals failure, all intermediate actions are wasted. With intermediates, the agent can detect failure at step $k$ and revise, saving the cost of steps $k+1$ through $n$. The value of early detection grows with chain length, because longer chains fail more often (P2 + #der-chain-confidence-decay).

**Observable intermediates are not required for strategy representation or persistence.** When intermediates are unobservable, plan-level tracking ( #schema-strategy-persistence, Case 3) preserves the sector condition at the cost of per-edge diagnostic resolution — the agent knows the plan is failing but cannot localize which step needs revision ( #der-observability-dominance). P4 is therefore a requirement for *strong diagnostics*, not for strategy representation per se. The observability investment tradeoff ( #der-observability-dominance) quantifies the payoff: making an intermediate observable improves the sector parameter from $1/(n_\Phi + 1)$ (plan-level) to $\min(1/(n_1+1),\; \theta_1/(n_2+1))$ (per-edge weakest-link).

### The Derivation

#### Step 1: P1 implies directed edges

Each component $X_i$ of the strategy has a set of direct causes $\text{Pa}(X_i)$ — the components whose outcomes directly influence $X_i$'s outcome. P1 requires that these causal relationships are directed: $\text{Pa}(X_i)$ temporally precedes $X_i$. This gives directed edges $\text{Pa}(X_i) \to X_i$.

#### Step 2: P2 implies probability distributions on edges

Each edge carries uncertainty: $P(X_i \mid \text{Pa}(X_i))$. By P2 (Cox), this is a probability distribution. The joint distribution over all strategy components is some $P(X_1, \ldots, X_n)$.

#### Step 3: Causal sufficiency implies the Markov condition (proved)

*[Derived (Conditional on causal sufficiency of $\Sigma_t$)]*

**Claim.** For a causally sufficient strategy DAG, the Markov factorization property is a theorem — a consequence of the Causal Markov Condition (CMC).

**The Markov factorization property.** Each variable $X_i$ is conditionally independent of its non-descendants given its parents:

$$X_i \perp \text{NonDesc}(X_i) \mid \text{Pa}(X_i)$$

Equivalently, the joint distribution factorizes as:

$$P(X_1, \ldots, X_n) = \prod_{i=1}^{n} P(X_i \mid \text{Pa}(X_i))$$

(The equivalence holds for positive distributions — Lauritzen 1996, Theorem 3.27.)

**The argument has five parts:**

**(a) The DAG is a causal model.** P1 establishes that edges represent causal relationships: completing a parent step causally advances the child step. P2 establishes probabilistic uncertainty over outcomes. Together: $\Sigma_t$ is a causal DAG in the sense of structural causal models (Pearl 2009, Definition 7.1.1) — each node's outcome is determined by its parents' outcomes (through the causal mechanism encoded in the edge credences) plus exogenous uncertainty specific to that step. Formally, each node admits a structural equation:

$$X_i = f_i(\text{Pa}(X_i), \varepsilon_i)$$

where $f_i$ is the local causal mechanism and $\varepsilon_i$ is the exogenous noise (the residual uncertainty at step $i$ not determined by its parents).

**(b) Causal sufficiency implies exogenous independence.** The exogenous terms $\varepsilon_i$ are mutually independent if and only if no unmodeled common cause affects two or more nodes in the graph. This is precisely the **causal sufficiency** assumption: every variable that is a direct common cause of two or more nodes in $\Sigma_t$ is itself a node in $\Sigma_t$.

For agent-constructed strategies, causal sufficiency is a **modeling ideal, not a typical condition**. The agent designed the graph, so all *intended* causal relationships are explicit — but environmental common causes (shared infrastructure, weather, market shifts, correlated adversary actions) routinely affect multiple strategy steps without appearing as nodes. In complex, multi-stakeholder, or adversarial environments, causal insufficiency is the dominant case ( #def-strategy-dag, Correlation Hierarchy). When an environmental factor is omitted, the exogenous terms become correlated and the Markov condition fails. This is model inadequacy ( #result-structural-adaptation-necessity), and the remedy is to add the missing common-cause node — but identifying which common causes matter is a modeling judgment, not a mechanical procedure ( #def-strategy-dag, L1 construction principle). The proof's conditional on causal sufficiency is therefore a condition on model quality: the result holds exactly when the DAG is well-constructed, approximately when it is close, and fails when major common causes are missing. The Correlation Hierarchy in #def-strategy-dag provides the practical framework: L0 (independence, this proof's assumption) gives tractable results; L1 (augmented DAG with explicit common-cause nodes) is the practical default in complex domains; L0 formal results transfer to correctly constructed L1 DAGs.

**(c) The Causal Markov Condition theorem.** For a DAG $G$ over variables $V = \{X_1, \ldots, X_n\}$ with structural equations $X_i = f_i(\text{Pa}(X_i), \varepsilon_i)$ where the $\varepsilon_i$ are mutually independent:

$$P(X_1, \ldots, X_n) = \prod_{i=1}^{n} P(X_i \mid \text{Pa}(X_i))$$

This is the **Causal Markov Condition** — a proved theorem, not a modeling assumption. The standard references are Spirtes, Glymour, and Scheines (2000, Theorem 3.4) and Pearl (2009, §1.4.1, Theorem 1.4.1). The proof applies the chain rule in topological order: $P(X_1, \ldots, X_n) = \prod_i P(X_i \mid X_1, \ldots, X_{i-1})$, then uses the independence of $\varepsilon_i$ to show that conditioning on all predecessors reduces to conditioning on parents only. Each non-parent predecessor's influence on $X_i$ is fully mediated through the parents — its direct contribution enters through the causal mechanism $f_i$, not through $\varepsilon_i$.

**(d) P3 as consequence.** State-local revisability (P3) was originally stated as an independent postulate. The CMC reveals it is a *consequence* of the causal structure under causal sufficiency: since $X_i \perp \text{NonDesc}(X_i) \mid \text{Pa}(X_i)$, updating beliefs about $X_i$ requires only $\text{Pa}(X_i)$ — local revision is automatically correct. No information from the rest of the graph changes the conditional distribution of $X_i$ given its parents. P3 was motivated as an operational requirement (agents *need* local revision for computational tractability, and the persistence condition demands it). The CMC shows the requirement is automatically satisfied by any causally sufficient causal DAG. The two arguments converge from different directions: P3 says local revision is *needed*; the CMC says it is *guaranteed* (under causal sufficiency).

**(e) Connection to edge independence.** The CMC's exogenous independence condition ($\varepsilon_i$ mutually independent) is precisely the **edge-independence assumption** in the AND/OR status propagation ( #def-strategy-dag). When exogenous noise terms are independent, edge outcomes are conditionally independent given parents, and the AND/OR formulas compute correct probabilities. When they are correlated (causal insufficiency — latent common causes), the AND/OR propagation systematically overestimates success because it treats joint failure probability as the product of marginals. The validity of the Markov factorization and the validity of the independence model are the *same condition*: causal sufficiency of $\Sigma_t$. See #def-strategy-dag for the full treatment of correlated failure as the primary case.

**Assembling (a)-(e).** P1-P2 establish that $\Sigma_t$ is a causal DAG with probabilistic uncertainty. Under causal sufficiency (exogenous independence), the CMC theorem proves the Markov factorization. P3 (local revisability) follows as a validated consequence. The Markov property is both operationally required (P3) and structurally guaranteed (CMC). When causal sufficiency fails, the Markov factorization is still the agent's *intended* factorization — the one its DAG represents — but it is wrong about the world. The gap between intended and actual factorization manifests as correlated failure and $\hat P_\Sigma$ overestimation, and the fix is structural: add the missing common-cause nodes to restore causal sufficiency.

#### Step 4: P1 + finite horizon implies acyclicity (proved)

This is the strongest piece of the argument. See the dedicated section below.

#### Step 5: Assembly

P1 (directed edges + causal interpretation) + P2 (probabilistic) + causal sufficiency (CMC → Markov factorization) + P4 (internal nodes) + finite horizon (acyclicity):

**The strategy representation must be representable as a directed acyclic graph with probability distributions at each node conditioned on its parents — a Bayesian network.** P3 (local revisability) is validated as a consequence of this structure, not required as a premise.

### Acyclicity Derivation

*[Derived (from #post-causal-structure + finite planning horizon)]*

This resolves a former known fragility in the theory. Acyclicity of $\Sigma_t$ is derived, not assumed.

**Result.** For a strategy representation over a finite future horizon, temporal ordering forces acyclicity.

**Derivation.**

1. Each node $X_i$ in $\Sigma_t$ represents a future event or state with temporal position $\tau_i \gt t$ (the future time at which the step occurs or the state is evaluated).
2. Each edge $X_i \to X_j$ requires $\tau_i \lt \tau_j$ (P1: causes temporally precede effects).
3. A cycle $X_i \to X_j \to \cdots \to X_i$ would require $\tau_i \lt \tau_j \lt \cdots \lt \tau_i$, which is impossible for a real-valued time index.
4. Therefore the graph is acyclic. $\square$

Formally: a finite set with a strict partial order (future events ordered by time) is representable as a DAG. This is a standard result in order theory — every finite partial order has a Hasse diagram, which is a DAG.

**The iteration objection resolved.** A strategy that says "try $A$, if fail try $B$, if fail try $A$ again" appears cyclic.

In the time-indexed representation:

$$A_1 \to \text{check}_1 \to B_1 \to \text{check}_2 \to A_2 \to \ldots$$

Each attempt is a distinct node at a distinct time. The apparent cycle is a linear chain in the unrolled view. Iteration "terminates" when either a node succeeds (remaining retry nodes become probability-zero), the agent exhausts its resource budget (a constraint truncating the chain), or the horizon ends. Any finite-horizon strategy, including those with "loops" in the informal sense, is acyclic when time-indexed.

**Scope.** This applies to $\Sigma_t$ (the agent's strategy over the future), not to $M_t$'s model of the environment. $M_t$ may include cyclic causal processes — feedback loops in the physical world, market dynamics, ecosystem interactions. The acyclicity is specific to the purposeful substate because $\Sigma_t$ represents planned future actions and the future is partially ordered by time. $M_t$'s model of environmental dynamics may need to represent cycles (via time-unrolled DBNs or other cyclic structures).

**Connection to Pearl.** Pearl's do-calculus is defined on DAGs. Extensions to cyclic structures exist (cyclic SCMs, equilibrium models) but are substantially more complex and lose some of do-calculus's clean properties. The temporal argument here shows that for strategy representations (future-looking plans), acyclicity is not a convenience restriction on Pearl's framework — it is a consequence of the temporal structure of planning.

### What Is Derived vs. What Is Chosen

| Property | Motivating postulate | Strength |
|---|---|---|
| Directed edges | Temporal ordering (P1, #post-causal-structure) | Proved |
| Probabilistic uncertainty | Cox's theorem (P2) | Proved |
| Acyclicity | Temporal ordering + finite horizon (P1) | Proved |
| Internal structure | Fragility + monitoring (P4, #der-chain-confidence-decay) | Derived |
| Markov factorization | Causal Markov Condition theorem (P1 causal interpretation + P2 probability + causal sufficiency) | Proved under causal sufficiency (CMC theorem) |
| **DAG with Markov property** | **P1 + P2 + causal sufficiency (CMC) + P4** | **Conditional on causal sufficiency — which is testable and repairable** |
| AND/OR parameterization | Boolean completeness + parsimony | Hypothesis (binary outcomes only) |
| Single-parameter edges | Parsimony / IB | Formulation choice |
| Specific node ontology | — | Formulation choice |

The dividing line: acyclicity and directed edges are proved; the full DAG-with-Markov-property is conditional on causal sufficiency. The parameterization (AND/OR, CPT form, edge semantics) is a formulation choice within the strongly motivated structure, motivated by parsimony and domain fit but not by mathematical necessity.

### Equivalence Class

**Within the DAG class.** Multiple DAGs can encode the same conditional independence relations, forming a Markov equivalence class identified by a CPDAG (completed partially directed acyclic graph). Two DAGs in the same equivalence class make identical probabilistic predictions but may differ in causal interpretation.

**Across representation types.** Factor graphs, junction trees, influence diagrams, and chain graphs are NOT simple presentational variants of DAGs:

- **Factor graphs** and **junction trees** preserve factorization and inference structure without necessarily preserving directed causal semantics.
- **Influence diagrams** add decision and utility nodes — a richer object, not an equivalent one.
- **Chain graphs** can express independence models that are not representable as DAGs at all.
- **Markov equivalence** is a statement within DAG classes, not across all graphical model types.

The correct claim is narrow: for a given factorized distribution, DAG and factor-graph representations can compute the same marginals. But causal semantics (do-calculus) are DAG-specific and do not transfer to undirected or mixed representations without additional structure.

**AAT's choice.** AAT uses DAG + AND/OR because: (a) AND/OR is the most parsimonious complete basis for binary combination ( #scope-and-or), (b) the DAG naturally supports causal/interventional reasoning (Pearl's do-calculus), and (c) the representation converged across three independent formalism attempts.

---
