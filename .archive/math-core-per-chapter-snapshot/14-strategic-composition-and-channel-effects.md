# Strategic Composition and Channel Effects


## Derivation: Strategic Composition via Equilibrium Convergence

- **Slug**: `deriv-strategic-composition`
- **Type**: derivation
- **Status**: conditional
- **Stage**: draft
- **Depends**: `post-composition-consistency`, `scope-composite-agent`, `result-sector-persistence-template`, `form-objective-functional`, `der-adversarial-destabilization`, `der-team-persistence`, `deriv-critical-mass-composition`, `der-directed-separation`, `scope-agent-identity`

When two or more AAT agents interact through a shared environment with **partially-opposing objectives** $\{O_t^{(i)}\}$, the composition-level question is not "does the trajectory contract to zero closure-defect?" but "does the coupled best-response dynamics admit an equilibrium and converge to it?" Contraction to shared truth is a $U_O = 1$ special case; strategic composition is the $U_O < 1$ companion regime in which the correct primitive is **fixed-point existence and stability**, not Lyapunov contraction on a shared state. Under potential-game or monotone-game conditions (sub-scope $\alpha'$), the sector-persistence template transfers to the gradient of the joint potential (resp. to a weighted-norm variational inequality), recovering AAT's persistence machinery at the equilibrium layer. Outside sub-scope $\alpha'$, only set-convergence to coarse correlated equilibria is available (sub-scope $\beta'$). This segment establishes the framing, derives the $\alpha'$-transfer, documents the $\beta'$ scope limits honestly, and relates to `#der-adversarial-destabilization` (asymmetric adversarial) and `#deriv-critical-mass-composition` (aligned composition with shared target) as siblings on the composition axis.

### The framing move

*[Formulation (strategic-composition-framing)]*

For $N$ purposeful sub-agents with partially-opposing $\{O_t^{(i)}\}$ running coupled AAT loops through a shared environment, the composition-level question is:

**(SC-1) Existence of equilibrium.** Does there exist a joint state $(X_{c,1}^\ast, \ldots, X_{c,N}^\ast)$ — equivalently a joint policy profile $(\pi_1^\ast, \ldots, \pi_N^\ast)$ — such that no sub-agent has a unilateral mismatch reduction available?

**(SC-2) Stability of equilibrium.** Do coupled best-response dynamics, initialised near $(X_{c,i}^\ast)$, remain there or return to it?

**(SC-3) Convergence from interior.** Do coupled dynamics, initialised away from any equilibrium, converge to the equilibrium set?

(SC-1)–(SC-3) are a fixed-point-existence question, a local-stability question, and a reachability question respectively. None is a Lyapunov contraction question on a shared state variable. The contraction framing in `#form-composition-closure` / `#deriv-critical-mass-composition` is recovered as the $U_O = 1$ special case (unique Nash equilibrium at the shared-objective optimum; best-response dynamics collapse to single-objective optimization).

### Sub-scope $\alpha'$: potential and monotone games (A2'-analog derived)

*[Derived (A2'-analog-potential, from Monderer-Shapley 1996)]*

A strategic interaction $(\{A_i\}, \{O_t^{(i)}\})$ is a **potential game** (Monderer & Shapley 1996, *Games and Economic Behavior* 14) when there exists a scalar potential $\Phi$ such that each sub-agent's unilateral improvement matches the potential's unilateral improvement:

$$O_t^{(i)}(\pi_i', \pi_{-i}) - O_t^{(i)}(\pi_i, \pi_{-i}) = \Phi(\pi_i', \pi_{-i}) - \Phi(\pi_i, \pi_{-i}) \quad \forall i.$$

Under this condition plus each sub-agent's B1 directional fidelity ( #der-gain-sector-bridge) to $\nabla_{\pi_i} O_t^{(i)}$, the joint best-response dynamics satisfy

$$\frac{d\Phi(\pi)}{dt} = \sum_i \langle \nabla_{\pi_i}\Phi,\; \dot\pi_i\rangle \geq \alpha_{\text{joint}} \lVert\nabla\Phi\rVert^2 \quad \text{for some } \alpha_{\text{joint}} > 0$$

whenever the joint configuration is not at a stationary point of $\Phi$. This is (T2) transcribed to state variable $\xi = $ gradient-of-potential, correction function $F = $ joint best-response velocity field; the quadratic Lyapunov structure is the same. **The sector-persistence template transfers** with $\xi = \pi - \pi^\ast$ (deviation from Nash), $\alpha = \alpha_{\text{joint}}$, $R = $ basin-of-attraction radius, and $\rho_\xi$ the exogenous disturbance rate on strategy space. Equilibrium existence follows from potential-function compactness on compact strategy spaces; equilibrium stability follows from $\Phi$'s role as a joint Lyapunov function.

*[Derived (A2'-analog-monotone, from Rosen 1965)]*

Weaker than potential: a game is **diagonally strictly concave** (Rosen 1965, *Econometrica* 33) when the Jacobian of the joint gradient field is negative-definite on the joint strategy space. Under this condition, there exists a unique Nash equilibrium and the joint gradient dynamics converge to it exponentially. The convergence rate is bounded below by the smallest eigenvalue of the symmetric part of the joint Jacobian, playing the role of $\alpha_{\text{joint}}$. No scalar potential need exist; a *weighted-norm* Lyapunov argument on the joint Jacobian's symmetric part substitutes.

**Sub-scope $\alpha'$** comprises: potential games (Monderer-Shapley), monotone games (Rosen), strongly-monotone games, and exponential-family dual-averaging under concave objectives. For these classes, the sector-persistence template extends to equilibrium convergence with composite sector constant $\alpha_{\text{joint}}$ inheriting from the joint-gradient-field structure.

### Sub-scope $\beta'$: non-potential non-monotone games

*[Derived (equilibrium-existence-via-VI, from Facchinei-Pang 2003)]*

Every strategic interaction with continuous strategy spaces and regular payoffs can be reformulated as a **variational inequality**: find $\pi^\ast \in \mathcal K$ such that $\langle F(\pi^\ast), \pi - \pi^\ast\rangle \geq 0$ for all $\pi \in \mathcal K$, where $F$ is the joint pseudo-gradient field. When $\mathcal K$ is compact-convex and $F$ is continuous, a solution exists (Hartman-Stampacchia theorem). **Pure-strategy Nash equilibrium existence is therefore guaranteed** for continuous-strategy games with compact convex strategy sets and continuous payoffs. But the VI framework gives *existence* only, not *convergence of any specific dynamic to the solution*; solutions may be non-unique.

*[Derived (regret-minimization-convergence-to-CCE, from Hart-Mas-Colell 2000)]*

Under no-regret learning (e.g., Hedge / multiplicative weights, Freund-Schapire 1997), the empirical joint distribution converges to the set of **coarse correlated equilibria** (CCE) at rate $O(1/\sqrt T)$. This requires no structure on the game beyond each sub-agent computing its own regret.

Under $\beta'$, the macro-state of a strategic composite is a *distribution* on the joint strategy space — the empirical joint play whose support is the CCE — rather than a state-space point. This is the structural shape of "convergence" in the $\beta'$ regime: distributional convergence, not pointwise. Pure-strategy Nash may or may not exist (cyclic games — rock-paper-scissors, matching pennies — lack pure Nash but retain mixed Nash via Nash 1950 and CCE convergence via Hart-Mas-Colell 2000); the $\beta'$ machinery's guarantees are at the distributional layer regardless.

**Sub-scope $\beta'$** scope-honesty: AAT can predict that long-run joint play lies in the CCE support; it cannot predict short-run trajectory, per-sub-agent mismatch convergence, or selection among multiple equilibria. The sector-persistence template does *not* apply in $\beta'$. This is a genuine scope limit shared with game theory as a whole, not a defect of AAT.

### Zero-sum scalar worked example

*[Derived (zero-sum-scalar-instantiation)]*

Two agents $A, B$ with scalar actions $a_i \in [-1, 1]$ and state $s_{t+1} = s_t + a_A - a_B + w_t$, $w_t \sim \mathcal N(0, \sigma^2)$. Objectives $O_t^{(A)}(s) = s$ (maximize $s$), $O_t^{(B)}(s) = -s$ (minimize $s$); zero-sum at the state-dependent payoff level.

**Action-coefficient analysis.** The agents' state-preferences are opposite, but the action-coefficients in $s_{t+1}$ are also opposite: $\partial s/\partial a_A = +1$ and $\partial s/\partial a_B = -1$. Composing with the objectives' state-dependence:

$$\frac{\partial O^{(A)}}{\partial a_A} = \frac{\partial O^{(A)}}{\partial s}\cdot \frac{\partial s}{\partial a_A} = (+1)(+1) = +1$$

$$\frac{\partial O^{(B)}}{\partial a_B} = \frac{\partial O^{(B)}}{\partial s}\cdot \frac{\partial s}{\partial a_B} = (-1)(-1) = +1$$

Both agents marginal-prefer *increasing* their own action — the opposing state-preferences and opposing action-coefficients compose to aligned action-preferences.

**Potential function.** For Monderer-Shapley, $\partial \Phi/\partial a_i = \partial O^{(i)}/\partial a_i$ for each $i$. With both partial derivatives equal to $+1$, the potential is $\Phi(a_A, a_B) = a_A + a_B$ (modulo additive constant).

**Nash equilibrium.** Each agent's best response on $[-1,1]$ is to push its own action to $+1$; the unique Nash equilibrium is $(a_A^\ast, a_B^\ast) = (1, 1)$. At equilibrium, $\Delta s = a_A^\ast - a_B^\ast = 0$: the substantive zero-sum property is that equal opposing action-coefficients cancel under the agents' aligned action-preferences, so joint action contributes no net displacement to $s$ (state drift comes only from $w_t$). This is qualitatively different from the naive picture in which the agents push the state in opposite directions.

**Sector-persistence template — interior-NE instantiation via Cournot-style payoffs.** The unregularized example has a *linear* potential $\Phi$ and a *corner* equilibrium at $(1,1)$; the unconstrained gradient field $\nabla\Phi = (1,1)$ is constant in $\xi = \pi - \pi^\ast$, so there is no interior linear restoring force around the equilibrium and the template's (T2) sector lower bound $\xi^T F(\xi) \geq \alpha\lVert\xi\rVert^2$ does not hold without modification — the saturation, not a sector contraction, is what enforces equilibrium. The aligned-action-preferences finding is the conceptual payload of the unregularized form; the sector-template transfer requires a payoff structure whose curvature is genuinely quadratic, not merely projected onto a corner.

A Cournot-style duopoly (Cournot 1838; Monderer-Shapley 1996 §3 example) supplies that structure naturally. Two firms produce quantities $q_i \in [0, Q_{\max}]$; market price is $P(q_A, q_B) = a_0 - b(q_A + q_B)$; per-firm cost is linear at rate $\kappa$; per-firm profit is

$$O^{(i)}(q_A, q_B) = q_i\,(a_0 - b(q_A + q_B) - \kappa).$$

This is partially-opposing in the policy-conflict sense — each firm's marginal payoff is decreased by the other's production through the shared price — without being strictly zero-sum. It is a potential game with quadratic potential.

*[Derived (Cournot-as-potential, from Monderer-Shapley 1996 §3)]*

$$\Phi(q_A, q_B) = (a_0 - \kappa)(q_A + q_B) - b(q_A^2 + q_B^2) - b\,q_A q_B,$$

verified by $\partial \Phi/\partial q_i = (a_0 - \kappa) - 2b q_i - b q_{-i} = \partial O^{(i)}/\partial q_i$. The symmetric interior Nash equilibrium is $q^\ast = (a_0 - \kappa)/(3b)$, located strictly inside the action box whenever $0 \lt q^\ast \lt Q_{\max}$.

Under continuous-time best-response $\dot q_i = \partial O^{(i)}/\partial q_i$, writing $\xi = q - q^\ast \mathbf 1$, the joint dynamics are $\dot \xi = -bM\xi$ with $M = \bigl(\begin{smallmatrix}2 & 1\\ 1 & 2\end{smallmatrix}\bigr)$. Setting $F(\xi) = bM\xi$ (correction-strength sign convention; $\dot\xi = -F(\xi)$):

- (T1) $F(0) = 0$. ✓
- (T2) $\xi^T F(\xi) = b(2\xi_A^2 + 2\xi_B^2 + 2\xi_A\xi_B) \geq b\lVert\xi\rVert^2$, since $M$'s eigenvalues are $\{1, 3\}$. So $\alpha_{\text{joint}} = b$ — the smallest eigenvalue of the symmetric part of the joint Jacobian, exactly the quantity Rosen 1965 identifies as the convergence rate. ✓
- (T2-upper) $\lVert F(\xi)\rVert \leq 3b\lVert\xi\rVert$ from $M$'s largest eigenvalue.
- (T3) $R = \min(q^\ast, Q_{\max} - q^\ast)$ — the radius of the largest origin-centered ball in $\xi$-space contained in the feasible region; the closer of the two active constraints (zero-production and capacity) determines the basin.

The template's preconditions hold with $\alpha_{\text{joint}}$ inherited from the demand-side curvature parameter $b$ rather than from any individual sub-agent's $\alpha$. This is the substantive transfer: the composite-level sector constant lives at the *joint potential's curvature*, with economic interpretation (market-saturation slope) rather than ad-hoc parametrization. Other linear-quadratic strategic-substitutes games (LQR with coupled state, network-coordination with quadratic disagreement cost, public-goods with quadratic externalities) produce structurally equivalent template instantiations, with $\alpha_{\text{joint}}$ tracking the symmetric part of their respective joint Jacobians.

The unregularized scalar zero-sum and the Cournot instantiation are complementary: the former illustrates the framing's surprise — opposing state-preferences combined with opposing action-coefficients yield aligned action-preferences — while the latter exhibits the template transfer with genuine quadratic curvature and interior NE.

### New scope route (C-iv) in `#scope-composite-agent`

*[Proposed Scope (composition-scope-condition, route C-iv)]*

Strategic composition with partially-opposing $\{O_t^{(i)}\}$ admits a joint equilibrium structure $\mathcal E$ (Nash, correlated, or coarse correlated) such that coupled best-response dynamics converge to the support of $\mathcal E$. The composite exists as an AAT agent with macro-state defined relative to $\mathcal E$ rather than relative to a shared target state.

(C-iv) is qualitatively distinct from (C-i)–(C-iii): it does *not* require shared objectives, hierarchical derivation, or mutual benefit. It requires only structural convergence of the strategic interaction in the game-theoretic sense. Composites satisfying (C-iv) are **strategic composites**, distinguished from alignment composites (C-i, C-ii) and mutual-benefit composites (C-iii).

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Framing move (contraction → equilibrium convergence) | Standard game-theoretic positioning | Formulation choice |
| (SC-1) / (SC-2) / (SC-3) three-question decomposition | Parallel to fixed-point / stability / reachability in dynamical systems | Formulation choice |
| A2'-analog under potential-game condition | Monderer-Shapley 1996 transcribed into AAT notation with B1 directional fidelity | Derived (exact under potential-game + B1) |
| A2'-analog under monotone-game condition | Rosen 1965 transcribed with weighted-norm Lyapunov | Derived (exact under diagonal strict concavity) |
| Equilibrium existence via VI | Facchinei-Pang 2003 (Hartman-Stampacchia) | Derived (external theorem, applied to strategic composition setting) |
| Regret-minimization CCE convergence | Hart-Mas-Colell 2000 | Derived (external theorem applied) |
| Sub-scope $\alpha'$ / $\beta'$ partition | Parallel to `#deriv-sector-condition` α/β | Formulation choice |
| Zero-sum scalar instantiation (corner-NE conceptual lesson) | Direct substitution into potential-game framework | Exact (within stated setup) |
| Cournot-style sector-template instantiation (interior-NE quadratic) | Monderer-Shapley 1996 §3 + sector-persistence-template; demand-side curvature $b$ supplies $\alpha_{\text{joint}}$ | Exact (within stated setup) |
| (C-iv) scope route | Extension to `#scope-composite-agent` disjunction | Formulation choice (scope extension) |
| Effects-spiral eigenvalue condition | Joint-Jacobian Re($\lambda_{\max}$) > 0 at candidate equilibria — formalizes `#der-adversarial-destabilization`'s discussion-grade effects spiral | Sketch (specific AAT instantiations open) |
| Strategic composition produces Class 2 (Partial) composites from Class 1 (Separated) sub-agents | Across-agent coupling through environment + cross-agent observation; preserves within-agent modularity | Derived (scope-structural) |
| Mechanism-design impossibility as candidate adjacent-floor instance in `#disc-identifiability-floor` | Gibbard-Satterthwaite 1973-75, Arrow 1951, Myerson-Satterthwaite 1983 | Flagged; not derived in this segment |
| Potential function $\Phi$ as additive-coordinate-forcing instance | $\Phi$'s additivity is definitional consequence of being a potential game, not forced by AAT-internal axiom; adjacent family member | Discussion-grade |
| Bridge from strategic composition to `#form-composition-closure` $\varepsilon^\ast$ | Macro-description is an equilibrium statistic, not an equilibrium state | Open |
| General equilibrium-selection under multiple Nash | Existence theorems do not pin down which equilibrium; selection (risk-dominance, payoff-dominance, Pareto) is partial | Open |
| Mean-field-game limit ($N \to \infty$) | Lasry-Lions 2007; Huang-Malhamé-Caines 2006; requires population scope condition | Open (pending Section III population gaps) |

---



## Derived: Agent Opacity ($H_b$)

- **Slug**: `der-agent-opacity`
- **Type**: derived
- **Status**: conditional
- **Stage**: draft
- **Depends**: `scope-agent-identity`, `der-interaction-channel-classification`, `der-adversarial-destabilization`, `result-adversarial-tempo-advantage`, `der-team-persistence`, `der-directed-separation`, `disc-identifiability-floor`

Alongside AAT's heavily formalized *forward* observation quality (how well the agent sees the world — observation ambiguity, model-class fitness, identifiability floor on what the agent can infer), AAT carries a **dual quantity** measuring how well the world sees the agent: **backward predictive uncertainty $H_b$**, an observer-indexed, horizon-indexed, trajectory-indexed entropy of the agent's future actions given another agent's filtration. Adopted from Hafez et al. 2026 as a first-class multi-agent quantity. $H_b$ is the dual of observation quality $U_o$: where $U_o$ characterizes how well the agent sees the world, $H_b$ characterizes how well the world sees the agent. It is **sign-flipped in value across regimes**: low $H_b$ (legibility) enables cooperative coordination ( #der-team-persistence); high $H_b$ (opacity) enables adversarial effectiveness ( #der-adversarial-destabilization, #result-adversarial-tempo-advantage). The sign-flip is a direct consequence of AAT's existing signed-coupling structure rather than a separate posit. This segment's emitter-side four-regime classification is the dual of `#der-interaction-channel-classification`'s recipient-side theory; together they close `#adversarial-edge-targeting` as emitter-optimizer paired with recipient-classifier.

*[Definition (agent-opacity-Hb)]*

For agent $A$ on singular trajectory $\mathcal C_A$ and observer agent $B$ with filtration $\mathcal F_B^t$ (per-trajectory observable history per `#scope-agent-identity`'s token-level commitment):

$$H_b^{A \mid B}(t, \tau) := H(a_{A, t+\tau} \mid \mathcal F_B^t)$$

the entropy of agent $A$'s action at horizon $\tau$ conditional on observer $B$'s filtration at time $t$. **Four indexing arguments:** observer $B$, time $t$, horizon $\tau$, trajectory $\mathcal C_A$. Each is load-bearing:

- **Observer-indexed.** Different observers (allies with shared infrastructure; adversaries with limited instrumentation; environment itself) have different filtrations $\mathcal F_B^t$; $H_b$ varies accordingly.
- **Horizon-indexed.** Immediate-next-action opacity ($\tau = 1$) and long-horizon-plan opacity ($\tau \gg 1$) decouple: an agent may be predictable at immediate action but unpredictable at plan level, or vice versa.
- **Trajectory-indexed.** Per `#scope-agent-identity`, AAT applies to agents on singular trajectories. $H_b^{A\mid B}$ is the opacity of *this* trajectory's continuation, not a type-level claim.
- **Time-indexed.** Opacity may drift with learning (as $B$'s model of $A$ improves, $H_b^{A\mid B}(t)$ decreases); steady-state values exist for ergodic regimes.

Under the IDT-observer specialization — $B$ operates as Hafez's Information Digital Twin monitoring $(S_A, a_A, S'_A)$ from outside $A$'s processing — and under ergodicity, $H_b^{A\mid B}(t, \tau) \to H(S, A \mid S')$ as defined in Hafez et al. 2026. AAT's added features (observer-indexing, horizon-indexing, trajectory-indexing) are the distinctive extensions.

### Sign-flip via signed coupling

*[Derived (sign-flip-from-signed-coupling)]*

The value of $H_b^A$ *to $A$* depends on the sign of $A$'s coupling to other agents — the same signed-coupling structure that organizes `#der-team-persistence`, `#der-adversarial-destabilization`, and `#deriv-critical-mass-composition`'s (CM2) $\gamma$ parameter.

- **Cooperative coupling ($\gamma^{\text{coop}} \gt 0$, reducing allies' disturbance).** For $B$ to treat $A$'s action as cooperation rather than disturbance, $B$ must predict $A$'s action well enough to preempt or complement it. Under `#der-interaction-channel-classification`'s recipient-side decomposition, unpredictable ally actions fall into Regime II (magnitude/structural shock) rather than Regime I (informative update). Therefore cooperative coupling effectiveness $\gamma_{A \to B}^{\text{coop}}$ is *increasing in legibility*, equivalently decreasing in $H_b^{A\mid B}$. Under sub-scope $\alpha$ Gaussian coupling: $\gamma^{\text{coop, effective}} \propto (1 - H_b^{A\mid B}/H_b^{\max})$.
- **Adversarial coupling ($\gamma^{\text{adv}} \gt 0$, amplifying target's disturbance).** Predicted attacks are neutralized; unpredicted attacks deliver effective disturbance. Adversarial coupling effectiveness is *increasing in opacity* — the mechanism of adversarial advantage (per `#result-adversarial-tempo-advantage`) operates *through* $B$'s failure to predict $A$. Under the same sub-scope $\alpha$ setup: $\gamma^{\text{adv, effective}} \propto H_b^{A\mid B}/H_b^{\max}$.

**The sign-flip on $H_b$'s value-to-$A$ lives in the sign of $\gamma$ itself, not in a different sign on $H_b$.** Cooperative regime $(\gamma^{\text{coop}} \gt 0)$ rewards low $H_b$; adversarial regime ($\gamma^{\text{adv}} \gt 0$) rewards high $H_b$. The same $H_b$ quantity, the same monotone dependence; opposite value-to-$A$ because the signs of the coupling terms differ.

### Emitter-side four-regime classification

*[Formulation (emitter-regimes, dual to #der-interaction-channel-classification)]*

Parallel to `#der-interaction-channel-classification`'s recipient-side four regimes, the emitter $A$ sends events that fall into four emitter-side regimes based on $A$'s opacity signal structure and self-model quality:

- **E-I Broadcast.** $A$ emits actions transparently; $H_b^{A\mid B}$ is low for any observer $B$ with standard instrumentation. Examples: public announcements, published decisions, legible industrial controllers.
- **E-II Selective-signal.** $A$ is transparent to some observers and opaque to others (e.g., shared allied infrastructure gives allies lower $H_b$ than adversaries without that infrastructure). Boundary: differential instrumentation in $\mathcal F_B^t$ across observers.
- **E-III Information-hide.** $A$ is uniformly opaque to observers; actions are randomized, encrypted, or routed through dead-drops. $H_b^{A\mid B}$ near $H_b^{\max}$ for all observers lacking the key / pattern / channel.
- **E-IV Active-deceive.** $A$ emits actions that mispredict — the observer's model of $A$ converges to a *wrong* prediction that differs from the actual action by a larger margin than the same observer's model of the environment would accommodate. Boundary: $A$'s self-model quality (for active-deceive, $A$ must model the observer's model of $A$ well enough to choose actions that exploit it).

The 16-cell emitter-recipient composition (four emitter regimes × four recipient regimes) gives a closed-form *adversarial-targeting arg-max* under `#adversarial-edge-targeting`: the most-valuable-to-attack edge is the one where the product of emitter's opacity-to-target and target's vulnerability-to-shock is maximized. This closes the Section III gap that `#adversarial-edge-targeting` (previously GAP) was reserved for; the segment is now operationalized with targeting-fidelity factor $(1 - H_b^{B\mid A}/H_b^{\max})$ from $A$'s self-model quality plus the four-regime recipient classification from `#der-interaction-channel-classification`.

### Tempo amplification by opacity

*[Derived (tempo-amplification-by-opacity)]*

`#result-adversarial-tempo-advantage`'s tempo-multiplier $\gamma_A \mathcal T_A$ in `#der-adversarial-destabilization` decomposes into a tempo term and an opacity term:

$$\mathcal T_A^{\text{effective}} = \mathcal T_A \cdot \frac{H_b^{A\mid B}}{H_b^{\max}} \quad \text{(Model D adversarial coupling)}$$

The superlinear formula $(\mathcal T_A / \mathcal T_B)^2$ becomes $(\mathcal T_A / \mathcal T_B)^2 \cdot (H_b^{A\mid B} / H_b^{B\mid A})^2$ under bilateral opacity — a higher-order tensor product with the same exponent $b = 2$ (Model D) or $b = 3/2$ (Model S) from `#result-adversarial-exponent-regimes`. Whether $b$ itself is reshaped under bilateral opacity is open; the leading-order scaling is the tempo-opacity product.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| $H_b^{A\mid B}(t, \tau)$ definition | Adopted from Hafez et al. 2026; extended with observer / horizon / trajectory indexing per `#scope-agent-identity` | Formulation choice (adoption + AAT-extension) |
| Reduction to Hafez's $H(S, A \mid S')$ under IDT-observer + ergodic regime | Direct substitution | Derived (exact under IDT + ergodicity) |
| Sign-flip via signed coupling | Cooperative coupling requires predictability (allies preempt); adversarial coupling operates via disturbance-injection (predicted attack is neutralized) | Derived (from existing `#der-team-persistence` + `#der-adversarial-destabilization` signed-$\gamma$ structure) |
| Emitter-side four-regime classification | Dual construction to `#der-interaction-channel-classification`'s recipient-side four regimes | Formulation choice |
| 16-cell emitter-recipient composition closes `#adversarial-edge-targeting` | Product of emitter opacity × recipient vulnerability-to-shock over four × four cells | Derived (arg-max construction) |
| Tempo-amplification leading-order: $\mathcal T^{\text{eff}} = \mathcal T \cdot H_b/H_b^{\max}$ | First-order substitution into `#result-adversarial-tempo-advantage`'s tempo-multiplier under Model D | Derived (conditional on Gaussian-coupling sub-scope $\alpha$) |
| Parameterization-invariance of $H_b$ | $H_b$ is an action-marginal entropy; action space is coordinate-free per `#scope-agent-identity` | Derived |
| Candidate 4th `#disc-identifiability-floor` instance (generic observer-side form) | $H_b$'s formal structure — "observer cannot predict agent's future action better than $H_b^{A\mid B}$" — is a CHT-style no-go at the observer-side-inference task | Discussion-grade (framing; precise external theorem not yet identified) |
| Candidate opacity ladder for `#disc-separability-pattern` | Transparent-core / partial-transparency / full-opacity across observer filtrations | Formulation choice (ladder proposal) |
| Effects-spiral opacity amplification (higher $H_b$ → higher $\gamma_A$ → larger $\dot V_B$ → $B$'s actions become more erratic → observer's model of $B$ degrades → higher $H_b^{B\mid A}$) | Composition of sign-flip derivation with `#der-adversarial-destabilization`'s effects spiral | Sketch (discussion-grade; specific functional form open) |
| Dual-filtration apparatus (each agent's $M_t$ carries an other-filtration as feature) | Would unify observer-indexing with `#scope-agent-identity`'s single-trajectory formalism more tightly | Open extension (mild architectural, orthogonal to derivations) |
| Sharp functional form for $\gamma^{\text{adv}}_{\text{effective}} = f(H_b)$ | Leading-order: $\gamma \propto H_b$. Exact function depends on sub-scope — Gaussian-coupling linear; sigmoid-coupling saturating | Open per sub-scope |

---



## Result: Adversarial Exponent Regimes

- **Slug**: `result-adversarial-exponent-regimes`
- **Type**: result
- **Status**: conditional
- **Stage**: draft
- **Depends**: `der-adversarial-destabilization`, `result-adversarial-tempo-advantage`, `def-adaptive-tempo`, `result-persistence-condition`, `deriv-sector-condition`

The adversarial tempo advantage exponent — the power $b$ in $\lVert\delta_B\rVert / \lVert\delta_A\rVert \sim (\mathcal T_A / \mathcal T_B)^b$ — is not a single number. It depends on two structural features of the disturbance: whether the adversarial coupling enters as deterministic drift (Model D) or stochastic noise (Model S), and whether the coupling dominates the base disturbance rate. Three regimes, with the coupling-dominant exponents now derived analytically from the respective disturbance models.

*[Derived (adversarial-exponent-regimes, from Model D/S steady states + coupling model; validated by simulation)]*

**Regime 1: Model D (deterministic drift), coupling-dominant.** When adversarial coupling enters as a persistent directional disturbance ($\rho_B = \rho_{\text{base}} + \gamma \cdot \mathcal T_A$, GA-2) and coupling dominates ($\gamma \cdot \mathcal T_B \gg \rho_{\text{base}}$):

$$b = 2 \qquad \text{(simulation: 1.999)}$$

Derived from the Model D steady state $\lVert\delta\rVert_{ss} = \rho/\mathcal{T}$ (Prop A.1). See #result-adversarial-tempo-advantage.

**Regime 2: Model S (stochastic noise), coupling-dominant.** When adversarial coupling enters through the noise scale of zero-mean perturbations ($\sigma_B = \sigma_{\text{base}} + \gamma \cdot \mathcal T_A$, GA-2S) and coupling dominates:

$$b = \frac{3}{2} \qquad \text{(simulation: 1.481)}$$

Derived from the Model S steady state $\lVert\delta\rVert_{\text{rms}} = \sigma_w/\sqrt{2\mathcal{T}}$ (Prop A.1S). The $1/\sqrt{\mathcal{T}}$ scaling (vs. $1/\mathcal{T}$ for Model D) removes one half-power from the denominator, reducing the exponent from 2 to 3/2. See #result-adversarial-tempo-advantage.

**Regime 3: Non-coupling-dominant.** When base disturbance is comparable to or exceeds the adversarial coupling ($\rho_{\text{base}} \gtrsim \gamma \cdot \mathcal T_B$):

$$b \to 1.0 \text{ (Model D)} \quad \text{or} \quad b \to 0.5 \text{ (Model S)}$$

The exponent degrades smoothly as the base-to-coupling ratio increases. The asymptotic limits are derived (they reflect the $1/\mathcal{T}$ or $1/\sqrt{\mathcal{T}}$ scaling without the coupling numerator); the smooth interpolation is empirical.

| $\rho_{\text{base}} / (\gamma \cdot \mathcal T_B)$ | Exponent (deterministic) | Exponent (stochastic) |
|:---:|:---:|:---:|
| 0.002 | 1.999 | 1.481 |
| 0.20 | 1.877 | 1.101 |
| 2.0 | 1.445 | 0.791 |
| 6.3 | 1.213 | 0.577 |

---



## Observation: Gated Tempo Advantage

- **Slug**: `obs-gated-tempo-advantage`
- **Type**: observation
- **Status**: empirical
- **Stage**: draft
- **Depends**: `der-adversarial-destabilization`, `emp-update-gain`, `def-adaptive-tempo`

Observation noise collapses the adversarial tempo advantage. When agents observe their mismatch through a noisy channel, the faster agent's additional corrections become noisy, partially offsetting its tempo advantage. The optimal gain ( #emp-update-gain) partially restores the advantage but cannot fully recover it.

*[Observation (obs-gated-tempo-advantage, from track-b Variant E)]*

In a two-agent adversarial system with observation noise $\sigma_{\text{obs}}$ added to each agent's mismatch signal:

| $\sigma_{\text{obs}}$ | Exponent (fixed $\eta$) | Exponent (optimal $\eta^\ast$) |
|:---:|:---:|:---:|
| 0.00 | 1.04 | 1.04 |
| 0.10 | 1.00 | 0.97 |
| 0.20 | 0.92 | 0.94 |
| 0.50 | 0.60 | 0.63 |
| 1.00 | 0.18 | 0.40 |

At $\sigma_{\text{obs}} = 1.0$ (10x the process noise), the fixed-gain adversarial exponent drops from $\sim 1.0$ to $\sim 0.2$ — tempo advantage nearly vanishes. The Riccati-optimal gain restores it to $\sim 0.4$, more than doubling the advantage but not recovering the noise-free level.

**The mechanism.** When observation noise is high, each correction step adds noise to the mismatch estimate. The faster agent makes more corrections per unit time, each noisy, partially offsetting the benefit of higher tempo. The optimal gain mitigates this by reducing $\eta$ to match the noise level — correcting less aggressively but more accurately.

---



## Result: Per-Dimension Persistence

- **Slug**: `result-per-dimension-persistence`
- **Type**: result
- **Status**: conditional
- **Stage**: draft
- **Depends**: `result-persistence-condition`, `def-adaptive-tempo`, `deriv-sector-condition`

The scalar persistence condition overestimates adaptive capacity when the agent's correction gain varies across dimensions. The weak dimension is the bottleneck — it dominates the aggregate mismatch regardless of performance on strong dimensions. The correct condition is per-dimension, with the form depending on whether the disturbance is deterministic (Model D) or stochastic (Model S).

*[Result (per-dimension-persistence)]*

For an agent with $d$-dimensional mismatch $\delta_t \in \mathbb{R}^d$, diagonal correction gain $\eta = \text{diag}(\eta_1, \ldots, \eta_d)$, and per-dimension disturbance:

### Model D: Deterministic Per-Dimension Threshold

Under bounded disturbance $\lvert w_k(t)\rvert \leq \rho_k$ (GA-2, per dimension), the per-dimension steady-state mismatch is:

$$\lvert\delta_k\rvert_{ss} = \frac{\rho_k}{\alpha_k}$$

**Persistence requires** $\alpha_k \gt \rho_k / R_k$ **for each dimension**, or in linear operational form:

$$\mathcal{T}_k \gt \frac{\rho_k}{\delta_{\text{critical},k}} \quad \text{for each dimension } k$$

This is the deterministic worst-case bound — exact under bounded disturbance by the same Lyapunov argument as Prop A.1, applied per dimension.

### Model S: Stochastic Per-Dimension Steady State

Under stochastic disturbance $w_{k,t} \sim N(0, \rho_k^2)$ (GA-2S, per dimension), the discrete AR(1) process $\delta_{k,t+1} = (1 - \eta_k)\delta_{k,t} + w_{k,t}$ has stationary distribution:

$$\delta_k \sim N\!\left(0,\; \frac{\rho_k^2}{2\eta_k - \eta_k^2}\right)$$

The stationary distribution supplies three task-adequacy criteria, each with its own threshold. The choice of criterion is an engineering decision; the three are related by exact constants for Gaussian $\delta_k$.

**(a) RMS bound** (mean-square, matches the scalar form in #result-persistence-condition):

$$\sqrt{E[\delta_k^2]} = \frac{\rho_k}{\sqrt{2\eta_k - \eta_k^2}}$$

Requiring $\sqrt{E[\delta_k^2]} \lt \delta_{\text{critical},k}$ and using the small-$\eta_k$ approximation $2\eta_k - \eta_k^2 \approx 2\eta_k$:

$$\boxed{\;\eta_k \gt \frac{\rho_k^2}{2\,\delta_{\text{critical},k}^2}\;} \quad \text{(RMS criterion)}$$

This is the scalar Model S threshold in #result-persistence-condition ($\alpha \gt n\sigma_w^2/(2R^2)$) applied per dimension.

**(b) MAE bound** (mean absolute error; bounds the expected deviation rather than its square):

$$E\!\left[\lvert\delta_k\rvert\right] = \sqrt{E[\delta_k^2]} \cdot \sqrt{\frac{2}{\pi}} = \frac{\rho_k}{\sqrt{2\eta_k - \eta_k^2}} \cdot \sqrt{\frac{2}{\pi}}$$

Requiring $E\!\left[\lvert\delta_k\rvert\right] \lt \delta_{\text{critical},k}$:

$$\eta_k \gt \frac{\rho_k^2}{\pi\,\delta_{\text{critical},k}^2} \quad \text{(MAE criterion)}$$

MAE is smaller than RMS by the factor $\sqrt{2/\pi} \approx 0.798$, so the MAE threshold is $2/\pi \approx 0.637$ times the RMS threshold. The criteria differ by a constant but bound different quantities; applying the same numerical $\delta_{\text{critical},k}$ under both does not mean the same thing.

**(c) Probability bound** (tail-risk criterion, for applications where occasional excursions matter):

$$P\!\left(\lvert\delta_k\rvert \gt \delta_{\text{critical},k}\right) \lt \epsilon \;\Longleftrightarrow\; \eta_k \gt \frac{\rho_k^2 \cdot z_{1-\epsilon/2}^2}{2\,\delta_{\text{critical},k}^2}$$

where $z_{1-\epsilon/2}$ is the two-sided Gaussian quantile. The probability bound at $\epsilon = 0.05$ (two-sided $z \approx 1.96$) is about $1.96^2 \approx 3.84$ times the RMS threshold — stricter because it bounds tail excursions rather than typical magnitudes.

**Recommended primary form.** The RMS criterion (a) is the canonical form for Model S persistence, matching the scalar treatment in #result-persistence-condition and the Lyapunov-based derivation in #deriv-sector-condition (Prop A.1S). The MAE and probability-bound variants are provided for applications where those are the natural task-adequacy measures. All three thresholds are quadratic in $\rho_k/\delta_{\text{critical},k}$ (not linear as in Model D), reflecting the $1/\sqrt{\alpha}$ scaling of the Model S stationary variance.

### Common Structure

The aggregate $L_2$ mismatch $\lVert\delta\rVert = \sqrt{\sum_k \delta_k^2}$ is dominated by the dimension with the largest $\rho_k / \eta_k$ ratio (Model S) or $\rho_k / \alpha_k$ ratio (Model D). The qualitative conclusion — the weak dimension is the bottleneck — holds for both models.

---
