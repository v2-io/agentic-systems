---
slug: deriv-strategic-composition
type: derivation
status: conditional
depends:
  - post-composition-consistency
  - scope-composite-agent
  - result-sector-persistence-template
  - form-objective-functional
  - der-adversarial-destabilization
  - der-team-persistence
  - deriv-critical-mass-composition
  - der-directed-separation
  - scope-agent-identity
stage: draft
---

# Derivation: Strategic Composition via Equilibrium Convergence

When two or more AAT agents interact through a shared environment with **partially-opposing objectives** $\{O_t^{(i)}\}$, the composition-level question is not "does the trajectory contract to zero closure-defect?" but "does the coupled best-response dynamics admit an equilibrium and converge to it?" Contraction to shared truth is a $U_O = 1$ special case; strategic composition is the $U_O \lt 1$ companion regime in which the correct primitive is **fixed-point existence and stability**, not Lyapunov contraction on a shared state. The framework names three composition-level questions distinctively here: **(SC-1)** does an equilibrium joint policy exist where no sub-agent has a unilateral mismatch reduction available; **(SC-2)** do coupled best-response dynamics initialized near it stay there; **(SC-3)** do they converge from arbitrary initialization to the equilibrium set? Fixed-point, local-stability, and reachability questions respectively — none a Lyapunov contraction question on a shared state variable.

Two sub-scopes carry progressively weaker conditions. Under potential-game (Monderer-Shapley 1996) or monotone-game (Rosen 1965) conditions — *sub-scope $\alpha'$* — the sector-persistence template transfers to the gradient of the joint potential (resp. to a weighted-norm variational inequality on the joint Jacobian's symmetric part), and AAT's persistence machinery recovers at the equilibrium layer with state variable $\xi = \pi - \pi^\ast$ (deviation from Nash) and sector constant $\alpha_{\text{joint}}$ living at the *joint potential's curvature* rather than at any individual sub-agent's $\alpha$. Outside $\alpha'$ — *sub-scope $\beta'$* — only set-convergence to coarse correlated equilibria is available (Hart-Mas-Colell 2000, rate $O(1/\sqrt T)$), and the macro-state of a strategic composite is a *distribution* on joint strategy space rather than a state-space point. The right structural consequence is named on the **dynamic-regime axis** rather than the architectural-class axis (the latter framing was carried in earlier drafts as "Class 1 sub-agents → Class 2 (Partial) composite" — that claim was withdrawn 2026-05-21 per `spikes/strategic-composition-class-3-attempt-2026-05-21/`; see `#disc-dynamic-regime-axis` for the surfacing): the strategic-composition move transitions the composite from contraction-regime (R0, under aligned objectives — scope routes C-i/ii/iii) to equilibrium-regime (R1, under partially-opposing objectives with potential/monotone structure — sub-scope $\alpha'$) or to cyclic-distributional-regime (R2, under partially-opposing objectives without potential/monotone structure — sub-scope $\beta'$). The composite's *macro-state type* changes correspondingly — state-variable in R0 / fixed-point object in R1 / distributional object in R2 — but the *architectural class* of the composite is preserved under goal-blind routing and distinct sub-agent substrates (it is Class 1 per the formal criterion when the sub-agents are Class 1; the Class 2 / Class 3 changes per `#hyp-directed-separation-under-composition` Case 2 require routing-structure goal-dependence or shared-substrate $G^c$-allocation, not strategic composition itself). This segment establishes the framing, derives the $\alpha'$-transfer (R0 → R1 Lyapunov-machinery transfer per `#disc-dynamic-regime-axis` §"Lyapunov-machinery transfer R0 → R1"), documents the $\beta'$ scope limits honestly, and relates to `#der-adversarial-destabilization` (asymmetric adversarial) and `#deriv-critical-mass-composition` (aligned composition with shared target) as siblings on the composition axis.

## Formal Expression

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

$$\frac{d\Phi(\pi)}{dt} = \sum_i \langle \nabla_{\pi_i}\Phi,\; \dot\pi_i\rangle \geq \alpha_{\text{joint}} \lVert\nabla\Phi\rVert^2 \quad \text{for some } \alpha_{\text{joint}} \gt 0$$

whenever the joint configuration is not at a stationary point of $\Phi$. This is (T2) transcribed to state variable $\xi =$ gradient-of-potential, correction function $F =$ joint best-response velocity field; the quadratic Lyapunov structure is the same. **The sector-persistence template transfers** with $\xi = \pi - \pi^\ast$ (deviation from Nash), $\alpha = \alpha_{\text{joint}}$, $R =$ basin-of-attraction radius, and $\rho_\xi$ the exogenous disturbance rate on strategy space. Equilibrium existence follows from potential-function compactness on compact strategy spaces; equilibrium stability follows from $\Phi$'s role as a joint Lyapunov function.

*[Derived (A2'-analog-monotone, from Rosen 1965)]*

Weaker than potential: a game is **diagonally strictly concave** (Rosen 1965, *Econometrica* 33) when the Jacobian of the joint gradient field is negative-definite on the joint strategy space. Under this condition, there exists a unique Nash equilibrium and the joint gradient dynamics converge to it exponentially. The convergence rate is bounded below by the smallest eigenvalue of the symmetric part of the joint Jacobian, playing the role of $\alpha_{\text{joint}}$. No scalar potential need exist; a *weighted-norm* Lyapunov argument on the joint Jacobian's symmetric part substitutes.

**Sub-scope $\alpha'$** comprises: potential games (Monderer-Shapley), monotone games (Rosen), strongly-monotone games, and exponential-family dual-averaging under concave objectives. For these classes, the sector-persistence template extends to equilibrium convergence with composite sector constant $\alpha_{\text{joint}}$ inheriting from the joint-gradient-field structure.

### Sub-scope $\beta'$: non-potential non-monotone games

*[Derived (equilibrium-existence-via-VI, from Facchinei-Pang 2003)]*

Every strategic interaction with continuous strategy spaces and regular payoffs can be reformulated as a **variational inequality**: find $\pi^\ast \in \mathcal{K}$ such that $\langle F(\pi^\ast), \pi - \pi^\ast\rangle \geq 0$ for all $\pi \in \mathcal{K}$, where $F$ is the joint pseudo-gradient field. When $\mathcal{K}$ is compact-convex and $F$ is continuous, a solution exists (Hartman-Stampacchia theorem). **Pure-strategy Nash equilibrium existence is therefore guaranteed** for continuous-strategy games with compact convex strategy sets and continuous payoffs. But the VI framework gives *existence* only, not *convergence of any specific dynamic to the solution*; solutions may be non-unique.

*[Derived (regret-minimization-convergence-to-CCE, from Hart-Mas-Colell 2000)]*

Under no-regret learning (e.g., Hedge / multiplicative weights, Freund-Schapire 1997), the empirical joint distribution converges to the set of **coarse correlated equilibria** (CCE) at rate $O(1/\sqrt T)$. This requires no structure on the game beyond each sub-agent computing its own regret.

Under $\beta'$, the macro-state of a strategic composite is a *distribution* on the joint strategy space — the empirical joint play whose support is the CCE — rather than a state-space point. This is the structural shape of "convergence" in the $\beta'$ regime: distributional convergence, not pointwise. Pure-strategy Nash may or may not exist (cyclic games — rock-paper-scissors, matching pennies — lack pure Nash but retain mixed Nash via Nash 1950 and CCE convergence via Hart-Mas-Colell 2000); the $\beta'$ machinery's guarantees are at the distributional layer regardless.

**Sub-scope $\beta'$** scope-honesty: AAT can predict that long-run joint play lies in the CCE support; it cannot predict short-run trajectory, per-sub-agent mismatch convergence, or selection among multiple equilibria. The sector-persistence template does *not* apply in $\beta'$. This is a genuine scope limit shared with game theory as a whole, not a defect of AAT.

**Cross-layer linearization fingerprint.** The joint Jacobian of $F$ at saddle-only Nash equilibria in $\beta'$ has imaginary-axis (semisimple) spectrum — the linearization fingerprint of the R0-loss rung in the single-agent certificate-strength ladder of `#result-certificate-existence`. FTRL × graphical-constant-sum-with-fully-mixed Nash (Cheung-Piliouras-Tao 2021 Theorem 19: lossless DGS + Poincaré recurrence on bounded level sets) is the worked composite instance of R0-loss; the connection is between layers (single-agent linearized error space $\mathbb{R}^n$ vs composite joint-strategy space $\mathcal{X}^c$), not a collision of R-letter ladders.

### Zero-sum scalar worked example

*[Derived (zero-sum-scalar-instantiation)]*

Two agents $A, B$ with scalar actions $a_i \in [-1, 1]$ and state $s_{t+1} = s_t + a_A - a_B + w_t$, $w_t \sim \mathcal{N}(0, \sigma^2)$. Objectives $O_t^{(A)}(s) = s$ (maximize $s$), $O_t^{(B)}(s) = -s$ (minimize $s$); zero-sum at the state-dependent payoff level.

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

Strategic composition with partially-opposing $\{O_t^{(i)}\}$ admits a joint equilibrium structure $\mathcal{E}$ (Nash, correlated, or coarse correlated) such that coupled best-response dynamics converge to the support of $\mathcal{E}$. The composite exists as an AAT agent with macro-state defined relative to $\mathcal{E}$ rather than relative to a shared target state.

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
| Sub-scope $\alpha'$ / $\beta'$ partition | Parallel to `#deriv-sector-condition` $\alpha$/$\beta$ | Formulation choice |
| Zero-sum scalar instantiation (corner-NE conceptual lesson) | Direct substitution into potential-game framework | Exact (within stated setup) |
| Cournot-style sector-template instantiation (interior-NE quadratic) | Monderer-Shapley 1996 §3 + sector-persistence-template; demand-side curvature $b$ supplies $\alpha_{\text{joint}}$ | Exact (within stated setup) |
| (C-iv) scope route | Extension to `#scope-composite-agent` disjunction | Formulation choice (scope extension) |
| Effects-spiral eigenvalue condition | Joint-Jacobian Re($\lambda_{\max}$) > 0 at candidate equilibria — formalizes `#der-adversarial-destabilization`'s discussion-grade effects spiral | Sketch (specific AAT instantiations open) |
| Strategic composition transitions composite from contraction-regime (R0) to equilibrium-regime (R1, under $\alpha'$) or cyclic-distributional-regime (R2, under $\beta'$) per `#disc-dynamic-regime-axis` | Game-structure (potential / monotone / cyclic) under partially-opposing objectives, *not* architectural-class change | Derived (regime-axis, surfaced 2026-05-21; supersedes the earlier "Class 1 sub-agents → Class 2 composite" architectural-class framing) |
| Mechanism-design impossibility landed in `#disc-implementation-impossibility` (designer-side sister meta-pattern to identifiability-floor) | Gibbard-Satterthwaite 1973-75, Arrow 1951, Myerson-Satterthwaite 1983 | Charter instances at `#deriv-strategy-proofness-impossibility` / `#deriv-bilateral-trade-impossibility` / `#deriv-social-welfare-aggregation-impossibility`; sub-scope $\alpha'$ named as adjacent-but-not-identical to the preference-domain-restriction escape |
| Potential function $\Phi$ as additive-coordinate-forcing instance | $\Phi$'s additivity is definitional consequence of being a potential game, not forced by AAT-internal axiom; adjacent family member | Discussion-grade |
| Bridge from strategic composition to `#form-composition-closure` $\varepsilon^\ast$ | Macro-description is an equilibrium statistic, not an equilibrium state | Open |
| General equilibrium-selection under multiple Nash | Existence theorems do not pin down which equilibrium; selection (risk-dominance, payoff-dominance, Pareto) is partial | Open |
| Mean-field-game limit ($N \to \infty$) | Lasry-Lions 2007; Huang-Malhamé-Caines 2006; requires population scope condition | Open (pending Section III population gaps) |

## Epistemic Status

*Conditional.* Max attainable: *exact* under potential-game + B1 (sub-scope $\alpha'$); *derived* under monotone-game + diagonal strict concavity; *discussion-grade* for the framing and sub-scope $\beta'$ set-convergence-only claim.

The A2'-analog results under Monderer-Shapley 1996 and Rosen 1965 are transcriptions of established game-theoretic theorems into AAT notation. AAT's contribution is not the mathematics but the recognition that the sector-persistence template transfers cleanly when these conditions hold, and that the composite-level sector constant $\alpha_{\text{joint}}$ lives at the *joint potential gradient* or *joint Jacobian's symmetric part*, not at any individual sub-agent's $\alpha$. The framing move (contraction → equilibrium convergence) is a structural positioning move.

Sub-scope $\beta'$ gives AAT substantially weaker predictive power than sub-scope $\alpha'$: *set-convergence to CCE only*, not trajectory convergence or per-agent mismatch convergence. This is an honest scope limit, not a defect — it mirrors game theory's own scope at the no-potential-no-monotonicity regime. AAT does not claim to predict equilibrium selection under multiple Nash, short-run dynamics in cyclic games (rock-paper-scissors), or convergence rates better than $O(1/\sqrt T)$ in $\beta'$.

**What this segment does not establish:**

- General convergence proof for non-potential games under AAT-native update rules (imports Monderer-Shapley + Rosen as scope statements, doesn't re-prove them).
- Explicit joint-Jacobian analysis for specific AAT agent architectures (e.g., two Beta-Bernoulli agents on a shared DAG). Effects-spiral formalization is sketched, not derived per-instance.
- Bridge from strategic composition to `#form-composition-closure`'s closure-defect $\varepsilon^\ast$ — the macro-description of a strategic composite is a distributional equilibrium statistic rather than a state, so the closure-defect formulation needs re-specification. Open.
- Full mechanism-design derivation (VCG, Bayesian-Nash) for specific AAT-relevant settings.

## Honest Limits

*[Scope honesty — strategic-composition-failures]*

- **No pure-strategy Nash equilibrium** in cyclic games (rock-paper-scissors; matching pennies). Mixed-Nash equilibrium exists universally for finite games (Nash 1950) but is a saddle point of best-response dynamics rather than a basin attractor; fictitious play orbits the mixed-Nash without converging pointwise to it. No-regret dynamics still drive the *empirical joint distribution* to the CCE set at rate $O(1/\sqrt T)$ (Hart-Mas-Colell 2000), so $\beta'$ machinery applies; the macro-state of a strategic composite in this regime is a distribution over the strategy space, not a state-space point.
- **Multiple equilibria with ambiguous selection** (coordination games; drive-left vs drive-right). Convergence to *some* equilibrium; AAT does not predict which.
- **Slow mixing / finite-sample failure** under regret-minimization: $O(1/\sqrt T)$ cumulative regret implies finite-horizon play may be far from CCE support.
- **Non-compact strategy spaces** (unbounded prices, resource allocations). No equilibrium without compactification; compactification may be artificial.
- **Bayesian games with strategic + epistemic uncertainty compounding.** Existence and uniqueness become pathological under certain information structures.
- **Mean-field games** ($N \to \infty$) require population-scope machinery not covered here.

## Discussion

**Sibling to `#der-adversarial-destabilization`.** `#der-adversarial-destabilization` handles the *asymmetric* adversarial case: one agent is target; attacker's tempo is exogenous parameter; sector-persistence template applies to target's mismatch with coupling-amplified disturbance. This segment handles the *symmetric* strategic case: both agents running full AAT loops; state variable is joint deviation from equilibrium; correction function is joint best-response field. The two are siblings. `#der-adversarial-destabilization`'s Working-Notes-flagged "coupled Lyapunov analysis is the open problem" has its formal home here — but the analysis is *not* a Lyapunov problem; it is a fixed-point problem, and the correct primitive is equilibrium convergence rather than Lyapunov descent. `#der-team-persistence` is recovered as the cooperative limit (all $\gamma^{\text{coop}}$ dominate; joint dynamics reduce to parallel single-agent sector-persistence with reduced effective disturbance); `#deriv-critical-mass-composition` sits in the middle with signed $\gamma$ on a matched-symmetric-Tier-1 dyad under shared target.

**The effects spiral's formal home.** `#der-adversarial-destabilization`'s effects spiral — $B$'s degrading model causes $B$'s actions to destabilize $A$ further — is a **joint-Jacobian eigenvalue condition** in the strategic-composition framing: the spiral exists iff $\max_{\text{candidate equilibria } \pi^\ast} \text{Re}(\lambda_{\max}(\nabla F(\pi^\ast))) \gt 0$, where $F$ is the joint best-response field. This condition specializes monotone-game failure (the Jacobian's symmetric part fails to be negative-definite at equilibrium). The asymmetric formulation in `#der-adversarial-destabilization` cannot express this condition because it treats one agent's tempo as exogenous; the symmetric coupled formulation here does.

**Dynamic-regime transition (not architectural-class change).** `#der-directed-separation` classifies agents into Class 1 (Separated) / Class 2 (Partial) / Class 3 (Coupled) based on within-agent coupling between $f_M$ and $G_t$. An earlier draft of this segment claimed that strategic composition produces Class 2 (Partial) *composites* from Class 1 (Separated) sub-agents — but that claim was withdrawn 2026-05-21 (per `spikes/strategic-composition-class-3-attempt-2026-05-21/02-REFRAME-INSIGHT.md` §6) because it conflated *belief content* (each sub-agent's $M_t^{(i)}$ containing models of other agents' goal-state, which is a normal POMDP feature) with *processing pathway* (a $G^c \to f^c_M$ pathway bypassing $e^c$, which is the actual Class 1/3 boundary). Per the formal $\kappa^c$ criterion of `#der-directed-separation`, under goal-blind routing and distinct sub-agent substrates the strategic composite is Class 1 (Separated) at the composite level — same architectural class as the sub-agents. Class change requires routing-structure goal-dependence (`#hyp-directed-separation-under-composition` Case 2) or shared-substrate $G^c$-allocation, neither of which is implied by strategic composition itself; the Cournot duopoly is the canonical witness for the architectural-class invariance under strategic composition (per `spikes/strategic-composition-class-3-attempt-2026-05-21/01-STRENGTHEN-ATTEMPTS.md` §2). What strategic composition *does* change is the **dynamic regime** (per `#disc-dynamic-regime-axis`): from R0 contraction-regime under aligned objectives to R1 equilibrium-regime under $\alpha'$ or R2 cyclic-distributional-regime under $\beta'$. The macro-state type changes correspondingly — state-variable (R0) / fixed-point object $\mathcal{E}$ (R1) / distributional object $\mu \in \Delta(\mathcal{X}^c)$ (R2). The dynamic-regime framing carries the load the architectural-class framing was inappropriately carrying, and does so on more honest ground (the regime change is exactly what this segment derives in the $\alpha'/\beta'$ partition; the architectural-class change was not derivable under the formal criterion).

**Mechanism-design impossibility.** If an outside designer can shape $\{O_t^{(i)}\}$, strategic composition becomes a **mechanism-design problem**: choose objectives so that the induced equilibrium *is* contraction to a designed state. Three classical impossibility results — Gibbard-Satterthwaite 1973-75 (no dominant-strategy non-dictatorial Pareto-efficient voting mechanism for ≥3 alternatives), Myerson-Satterthwaite 1983 (no efficient, individually-rational, incentive-compatible bilateral-trade mechanism without subsidies), Arrow 1951 (no social welfare function satisfying unrestricted-domain, Pareto-efficient, IIA, non-dictatorial) — land as the three charter instances of `#disc-implementation-impossibility`, the designer-side sister meta-pattern to `#disc-identifiability-floor`. Sub-scope $\alpha'$ of this segment is named there as *adjacent to but not identical with* the preference-domain-restriction escape (single-peaked / single-crossing): sub-scope $\alpha'$ secures best-response convergence under fixed reports, not strategy-proof revelation — the 2026-05-20 strengthen-first arm's three-reframing argument is the documented record (see `#deriv-strategy-proofness-impossibility` Discussion). Supporting derivations carry the formal statements, AAT translations, and escape characterizations: `#deriv-strategy-proofness-impossibility` (GS), `#deriv-bilateral-trade-impossibility` (MS), `#deriv-social-welfare-aggregation-impossibility` (Arrow).

**Meta-pattern positioning.**

- *`#disc-separability-pattern`:* sub-scope $\alpha'$ (potential / monotone — template transfers) is separable-core; sub-scope $\beta'$ (VI / regret-minimization — set-convergence only) is structured-repair; cyclic / non-convergent / multi-equilibrium-selection-ambiguous is general-open. Candidate additional ladder (strategic-interaction regime); decide whether to surface as 8th ladder or merge into an existing ladder.
- *`#disc-identifiability-floor`:* mechanism-design impossibility is *not* an identifiability-floor instance (the 2026-05-20 strengthen-first arm at `spikes/.integrated/spike-4th-identifiability-floor-instance-2026-05-20.md` §4 confirmed actor-positioning mismatch — designer-side vs agent-side; the named AAT-side escape sub-scope $\alpha'$ addresses best-response-dynamics convergence, not strategy-proof revelation) — the cluster lands in the designer-side sister meta-pattern `#disc-implementation-impossibility` instead. See Discussion above and the Related Work entry.
- *`#disc-implementation-impossibility`:* this segment's sub-scope $\alpha'$ is named there as adjacent-but-not-identical to the preference-domain-restriction escape in two charter instances (`#deriv-strategy-proofness-impossibility` for GS and `#deriv-social-welfare-aggregation-impossibility` for Arrow — both sharing the same adjacency).
- *`#disc-additive-coordinate-forcing`:* the potential function $\Phi$ plays an additive-coordinate role at the strategic layer, but its additivity is a *definitional consequence* of being a potential game (Monderer-Shapley require the additivity property by definition) rather than forced by a uniqueness theorem on an AAT-internal axiom. This positions $\Phi$ as an adjacent family member, parallel to Lyapunov quadratic and IB Lagrangian, not a primary instance.

**Active-inference sharpening.** Sun-Firestone 2020's dark-room argument observes that preferences-as-priors collapse under mutual prediction. Strategic composition gives this argument a formal substrate: two agents mutually predicting each other become a **fixed-point problem**, not a Lyapunov descent. The active-inference attempt to unify goal-seeking and prediction fails here in a derivable way — the fixed point is not at the prediction-optimum; it is at the strategic-equilibrium, which is structurally different. This strengthens `#def-satisfaction-gap`'s positioning against preferences-as-priors without requiring additional refutation machinery.

## Working Notes

- **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. The canonical strategic-composition pattern "Class-1-sub-agents → Class-3-composite" (old vocab; Class 3 = partially modular) is now "Class 1 (Separated) sub-agents → Class 2 (Partial) composite." Removed at `candidate` stage per FORMAT.md Gate 4.

- **No $\gamma'$ sub-scope.** A $\gamma'$ sub-scope for cyclic-distributional equilibria (games where no pure-strategy Nash exists but mixed Nash and/or CCE do exist, with macro-state as equilibrium distribution rather than equilibrium point) was considered and collapsed into $\beta'$: cyclic games are paradigmatic $\beta'$ instances, with the same machinery (regret-minimization), the same convergence guarantee (CCE set-convergence), and the same rate ($O(1/\sqrt T)$). The $\alpha'/\beta'$ decomposition is the right granularity at the regret-minimization layer; the type-of-object distinction (distribution vs state-space point) is surfaced within $\beta'$ framing rather than as a third sub-scope.

- **Effects-spiral eigenvalue condition formalization.** The condition $\max_{\pi^\ast} \text{Re}(\lambda_{\max}(\nabla F(\pi^\ast))) \gt 0$ is sketched in §Discussion. Deriving it for specific AAT agent classes (two Beta-Bernoulli agents on a shared DAG; two Kalman agents with coupled observations) would upgrade the spiral from discussion-grade in `#der-adversarial-destabilization` to derived here. Follow-on spike candidate.

- **Mechanism-design impossibility landed as `#disc-implementation-impossibility` sister meta-pattern (closed 2026-05-22).** The candidate-fourth-instance flag is resolved. The 2026-05-20 strengthen-first arm at `spikes/.integrated/spike-4th-identifiability-floor-instance-2026-05-20.md` §4 confirmed the cluster does *not* fit `#disc-identifiability-floor`'s actor-positioning (designer-side construction task vs agent-side inferential task); the cluster lands instead as a sister meta-pattern with three charter instances: `#deriv-strategy-proofness-impossibility` (GS), `#deriv-bilateral-trade-impossibility` (MS), `#deriv-social-welfare-aggregation-impossibility` (Arrow). Sub-scope $\alpha'$ of this segment is named in the GS and Arrow charter instances as *adjacent to but not identical with* the preference-domain-restriction escape (single-peaked / single-crossing): convergence-under-current-reports is not dominance-over-all-reports. The 2026-05-20 spike's recommended near-term re-home in `#disc-separability-pattern`'s strategic-composition ladder general-open tier was *not* executed — `#disc-separability-pattern`'s 8th ladder landed as Dynamic regime per `#disc-dynamic-regime-axis` 2026-05-21 instead (the strategic-composition ladder never materialized in `#disc-separability-pattern`); the sister meta-segment landing supersedes the candidate routing.

- **Composite-class-inheritance refinement (resolved 2026-05-21 — withdrawn).** The earlier-drafted "Class 1 (Separated) sub-agents → Class 2 (Partial) composite" architectural-class claim has been *withdrawn* per the strategic-composition spike at `spikes/strategic-composition-class-3-attempt-2026-05-21/` — the formal $\kappa^c$ criterion of `#der-directed-separation` gives Class 1 at the composite level under goal-blind routing (Cournot witness; conflation diagnosis at `02-REFRAME-INSIGHT.md` §6). The dynamic-regime axis (`#disc-dynamic-regime-axis`) carries the regime-change content that the architectural-class claim was attempting; the cross-axis interaction is the substantive structural finding (wrapping operates on Axis A architectural class; alignment work operates on Axis B dynamic regime; they are independent). `#hyp-directed-separation-under-composition` retains its existing Case 1 / Case 2 dichotomy unchanged.

- **Bridge from strategic composition to `#form-composition-closure` $\varepsilon^\ast$.** The macro-description of a strategic composite is an equilibrium *statistic* (joint play distribution) rather than an equilibrium *state*. The closure-defect formulation needs re-specification for this case. Open.

- **Replicator / evolutionary dynamics.** Replicator-based strategic dynamics (Sandholm 2010, *Population Games and Evolutionary Dynamics*) converge to ESS (evolutionarily stable strategies), a subset of Nash. Under which AAT-native update rules does the induced strategic dynamic match replicator? Multi-armed-bandit with softmax choice approximates replicator; gradient-descent on log-likelihood of mixed strategy is replicator exactly. Worth follow-on spike on AAT → evolutionary-dynamics correspondence.

- **Mean-field extension.** $N \to \infty$ limit with each agent interacting with a population *distribution* rather than named others. Natural extension for market / population strategic composition. Lasry-Lions 2007; Huang-Malhamé-Caines 2006. Requires population-scope condition of Section III that is currently marked GAP.

- **Worked-example structure — Cournot substitution for sector-template instantiation.** The unregularized scalar zero-sum case carries a non-trivial conceptual lesson: with $\Phi = a_A + a_B$, both agents' marginal preferences align ($+1$ each) and the unique Nash equilibrium is the *corner* $(1, 1)$, where joint action contributes no net displacement to the shared state via cancellation of opposing action-coefficients rather than via opposing action-directions. This is preserved as the framing illustration. Sector-template instantiation is then carried by a Cournot-style duopoly (Cournot 1838; Monderer-Shapley 1996 §3) whose interior NE arises from genuine demand-side curvature rather than from an ad-hoc per-agent quadratic action cost. The reasoning trail — including a discarded $-\tfrac{c}{2}a_i^2$ regularization that placed an interior NE at $(1/c, 1/c)$ but introduced a parameter without economic interpretation, and an algebra error in that regularization's $R$ (stated as $(1-1/c)\sqrt{2}$ where the inscribed-ball radius of the action box around the interior NE is $1 - 1/c$, the corner-distance over-counting by $\sqrt{2}$) — is recorded in `spikes/spike-strategic-composition.md` §5.2–5.4 along with the original sign error in the potential function. Brainstormed alternatives (LQR with coupled state; network-coordination with quadratic disagreement cost; public-goods with quadratic externalities) all give structurally equivalent template instantiations; Cournot was chosen for textbook authority and for the strategic-substitutes interpretation that retains the partially-opposing-objectives flavor without requiring strict zero-sum.

- **Track E surface-back of catalog citations (2026-05-22) — uncoupled-dynamics + passivity + distributed Nash-seeking neighbors.** Adjacent prior-art literatures surfaced 2026-05-22 from Track E catalog at `ref/prior-art-analysis/14-composition-under-goal-divergence.md` (Pillars 2 + 3 + key anchor papers), each marked `[^cat-2026-05-22]` for verification-deferred attribution:
   - **Hart & Mas-Colell 2003**, *Uncoupled Dynamics Do Not Lead to Nash Equilibrium* (American Economic Review 93:1830)[^cat-2026-05-22] — sweeping negative result: if agents do not know the utility functions of other agents (uncoupled dynamics), no general learning algorithm is guaranteed to converge to Nash equilibrium. The classical companion to this segment's sub-scope $\beta'$ "set-convergence to CCE only" honest scope limit; provides the uncoupled-side complement to Hart-Mas-Colell 2000's regret-minimization positive result. Strengthens the framework's $\beta'$ scope-honesty discipline by naming the structural reason convergence guarantees are weak in the general case.
   - **Milionis et al. 2023**, expanded uncoupled-dynamics impossibility[^cat-2026-05-22] — Nash existence proofs are non-constructive; natural game dynamics fundamentally fail to converge in general games (chaos / cycles); empirically aligned with Mertikopoulos-Papadimitriou-Piliouras 2017 *Cycles in Adversarial Regularized Learning* (already cited in `#disc-identifiability-floor` Instance 3 escape (e) per the BG2 verdict). Provides the modern reinforcement for the uncoupled-impossibility line.
   - **Fox & Shamma 2012**, *Population games, stable games, and passivity* (Games 3:692)[^cat-2026-05-22]; **Arcak & Martins 2020**, *Dissipativity Tools for Convergence to Nash Equilibria in Population Games* (IEEE TAC 65:1681)[^cat-2026-05-22] — pioneering use of control-theoretic passivity / dissipativity to analyze game-theoretic convergence; population games mapped onto passive input-output systems with stability proven via passivity. Strongly mirrors this segment's transfer of the sector-persistence template to the equilibrium layer (the sub-scope $\alpha'$ result is structurally adjacent to the passivity-based convergence guarantees). Closest control-theoretic adjacent literature.
   - **Gadjov & Pavel 2019, 2023**[^cat-2026-05-22]; **Belgioioso & Grammatico 2018**[^cat-2026-05-22] — distributed Nash-equilibrium seeking via monotone-operator theory; proximal-point algorithms and Laplacian feedback as convergence machinery even in partially-observable or hypomonotone regimes. Adjacent to the (C-iv) strategic-equilibrium scope route and the sub-scope $\alpha'$ monotone-games treatment.

Primary-source verification queued in the BG2 cluster — see `#disc-identifiability-floor` Working Notes for the verification-targets list. Catalog citations had prior Pillar-style search support but were not verified by the current executor at landing time.

[^cat-2026-05-22]: Citation surfaced 2026-05-22 from the Track E catalog at `ref/prior-art-analysis/` (intermediate work artifacts that captured Pillar-style prior-art searches). Catalog has more verification support than raw Undermind synthesis but less than full primary-source reading. Verification queued with the BG2 cluster.
