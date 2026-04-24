---
slug: strategic-composition
type: derivation
status: conditional
depends:
  - postulate-composition-consistency
  - scope-composite-agent
  - sector-persistence-template
  - objective-functional
  - adversarial-destabilization
  - team-persistence
  - critical-mass-composition
  - directed-separation
  - scope-agent-identity
stage: draft
---

# Derivation: Strategic Composition via Equilibrium Convergence

When two or more AAD agents interact through a shared environment with **partially-opposing objectives** $\{O_t^{(i)}\}$, the composition-level question is not "does the trajectory contract to zero closure-defect?" but "does the coupled best-response dynamics admit an equilibrium and converge to it?" Contraction to shared truth is a $U_O = 1$ special case; strategic composition is the $U_O < 1$ companion regime in which the correct primitive is **fixed-point existence and stability**, not Lyapunov contraction on a shared state. Under potential-game or monotone-game conditions (sub-scope $\alpha'$), the sector-persistence template transfers to the gradient of the joint potential (resp. to a weighted-norm variational inequality), recovering AAD's persistence machinery at the equilibrium layer. Outside sub-scope $\alpha'$, only set-convergence to coarse correlated equilibria is available (sub-scope $\beta'$). This segment establishes the framing, derives the $\alpha'$-transfer, documents the $\beta'$ scope limits honestly, and relates to `#adversarial-destabilization` (asymmetric adversarial) and `#critical-mass-composition` (aligned composition with shared target) as siblings on the composition axis.

## Formal Expression

### The framing move

*[Formulation (strategic-composition-framing)]*

For $N$ purposeful sub-agents with partially-opposing $\{O_t^{(i)}\}$ running coupled AAD loops through a shared environment, the composition-level question is:

**(SC-1) Existence of equilibrium.** Does there exist a joint state $(X_{c,1}^\ast, \ldots, X_{c,N}^\ast)$ — equivalently a joint policy profile $(\pi_1^\ast, \ldots, \pi_N^\ast)$ — such that no sub-agent has a unilateral mismatch reduction available?

**(SC-2) Stability of equilibrium.** Do coupled best-response dynamics, initialised near $(X_{c,i}^\ast)$, remain there or return to it?

**(SC-3) Convergence from interior.** Do coupled dynamics, initialised away from any equilibrium, converge to the equilibrium set?

(SC-1)–(SC-3) are a fixed-point-existence question, a local-stability question, and a reachability question respectively. None is a Lyapunov contraction question on a shared state variable. The contraction framing in `#composition-closure` / `#critical-mass-composition` is recovered as the $U_O = 1$ special case (unique Nash equilibrium at the shared-objective optimum; best-response dynamics collapse to single-objective optimization).

### Sub-scope $\alpha'$: potential and monotone games (A2'-analog derived)

*[Derived (A2'-analog-potential, from Monderer-Shapley 1996)]*

A strategic interaction $(\{A_i\}, \{O_t^{(i)}\})$ is a **potential game** (Monderer & Shapley 1996, *Games and Economic Behavior* 14) when there exists a scalar potential $\Phi$ such that each sub-agent's unilateral improvement matches the potential's unilateral improvement:

$$O_t^{(i)}(\pi_i', \pi_{-i}) - O_t^{(i)}(\pi_i, \pi_{-i}) = \Phi(\pi_i', \pi_{-i}) - \Phi(\pi_i, \pi_{-i}) \quad \forall i.$$

Under this condition plus each sub-agent's B1 directional fidelity ( #gain-sector-bridge) to $\nabla_{\pi_i} O_t^{(i)}$, the joint best-response dynamics satisfy

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

**Sub-scope $\beta'$** scope-honesty: AAD can predict that long-run joint play lies in the CCE support; it cannot predict short-run trajectory, per-sub-agent mismatch convergence, or selection among multiple equilibria. The sector-persistence template does *not* apply in $\beta'$. This is a genuine scope limit shared with game theory as a whole, not a defect of AAD.

### Zero-sum scalar worked example

*[Derived (zero-sum-scalar-instantiation)]*

Two agents $A, B$ with scalar actions $a_i \in [-1, 1]$ and state $s_{t+1} = s_t + a_A - a_B + w_t$, $w_t \sim \mathcal N(0, \sigma^2)$. Objectives $O_t^{(A)}(s) = s$, $O_t^{(B)}(s) = -s$ (zero-sum).

The potential $\Phi(a_A, a_B) = a_A - a_B$ satisfies both agents' unilateral deviation conditions; this is a potential game. Nash equilibrium at $(a_A^\ast, a_B^\ast) = (1, -1)$ — $A$ pushes up maximally, $B$ pushes down maximally, the boundary of the feasible region. The sector-persistence template instantiates with $\xi = (a_A - 1, a_B + 1)$, $F(\xi) = -\xi$, $\alpha = 1$, $R = 2\sqrt 2$ (box diameter), $\rho_\xi$ from environmental $w_t$. Under Model S, $R^\ast_S = \sigma$; persistence requires $\sigma < 2\sqrt 2$.

### New scope route (C-iv) in `#scope-composite-agent`

*[Proposed Scope (composition-scope-condition, route C-iv)]*

Strategic composition with partially-opposing $\{O_t^{(i)}\}$ admits a joint equilibrium structure $\mathcal E$ (Nash, correlated, or coarse correlated) such that coupled best-response dynamics converge to the support of $\mathcal E$. The composite exists as an AAD agent with macro-state defined relative to $\mathcal E$ rather than relative to a shared target state.

(C-iv) is qualitatively distinct from (C-i)–(C-iii): it does *not* require shared objectives, hierarchical derivation, or mutual benefit. It requires only structural convergence of the strategic interaction in the game-theoretic sense. Composites satisfying (C-iv) are **strategic composites**, distinguished from alignment composites (C-i, C-ii) and mutual-benefit composites (C-iii).

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Framing move (contraction → equilibrium convergence) | Standard game-theoretic positioning | Formulation choice |
| (SC-1) / (SC-2) / (SC-3) three-question decomposition | Parallel to fixed-point / stability / reachability in dynamical systems | Formulation choice |
| A2'-analog under potential-game condition | Monderer-Shapley 1996 transcribed into AAD notation with B1 directional fidelity | Derived (exact under potential-game + B1) |
| A2'-analog under monotone-game condition | Rosen 1965 transcribed with weighted-norm Lyapunov | Derived (exact under diagonal strict concavity) |
| Equilibrium existence via VI | Facchinei-Pang 2003 (Hartman-Stampacchia) | Derived (external theorem, applied to strategic composition setting) |
| Regret-minimization CCE convergence | Hart-Mas-Colell 2000 | Derived (external theorem applied) |
| Sub-scope $\alpha'$ / $\beta'$ partition | Parallel to `#sector-condition-derivation` α/β | Formulation choice |
| Zero-sum scalar instantiation | Direct substitution into potential-game + sector-persistence-template | Exact (within stated setup) |
| (C-iv) scope route | Extension to `#scope-composite-agent` disjunction | Formulation choice (scope extension) |
| Effects-spiral eigenvalue condition | Joint-Jacobian Re($\lambda_{\max}$) > 0 at candidate equilibria — formalizes `#adversarial-destabilization`'s discussion-grade effects spiral | Sketch (specific AAD instantiations open) |
| Strategic composition produces Class 3 composites from Class 1 sub-agents | Across-agent coupling through environment + cross-agent observation; preserves within-agent modularity | Derived (scope-structural) |
| Mechanism-design impossibility as candidate 4th `#discussion-identifiability-floor` instance | Gibbard-Satterthwaite 1973-75, Arrow 1951, Myerson-Satterthwaite 1983 | Flagged; not derived in this segment |
| Potential function $\Phi$ as additive-coordinate-forcing instance | $\Phi$'s additivity is definitional consequence of being a potential game, not forced by AAD-internal axiom; adjacent family member | Discussion-grade |
| Bridge from strategic composition to `#composition-closure` $\varepsilon^\ast$ | Macro-description is an equilibrium statistic, not an equilibrium state | Open |
| General equilibrium-selection under multiple Nash | Existence theorems do not pin down which equilibrium; selection (risk-dominance, payoff-dominance, Pareto) is partial | Open |
| Mean-field-game limit ($N \to \infty$) | Lasry-Lions 2007; Huang-Malhamé-Caines 2006; requires population scope condition | Open (pending Section III population gaps) |

## Epistemic Status

*Conditional.* Max attainable: *exact* under potential-game + B1 (sub-scope $\alpha'$); *derived* under monotone-game + diagonal strict concavity; *discussion-grade* for the framing and sub-scope $\beta'$ set-convergence-only claim.

The A2'-analog results under Monderer-Shapley 1996 and Rosen 1965 are transcriptions of established game-theoretic theorems into AAD notation. AAD's contribution is not the mathematics but the recognition that the sector-persistence template transfers cleanly when these conditions hold, and that the composite-level sector constant $\alpha_{\text{joint}}$ lives at the *joint potential gradient* or *joint Jacobian's symmetric part*, not at any individual sub-agent's α. The framing move (contraction → equilibrium convergence) is a structural positioning move.

Sub-scope $\beta'$ gives AAD substantially weaker predictive power than sub-scope $\alpha'$: *set-convergence to CCE only*, not trajectory convergence or per-agent mismatch convergence. This is an honest scope limit, not a defect — it mirrors game theory's own scope at the no-potential-no-monotonicity regime. AAD does not claim to predict equilibrium selection under multiple Nash, short-run dynamics in cyclic games (rock-paper-scissors), or convergence rates better than $O(1/\sqrt T)$ in $\beta'$.

**What this segment does not establish:**

- General convergence proof for non-potential games under AAD-native update rules (imports Monderer-Shapley + Rosen as scope statements, doesn't re-prove them).
- Explicit joint-Jacobian analysis for specific AAD agent architectures (e.g., two Beta-Bernoulli agents on a shared DAG). Effects-spiral formalization is sketched, not derived per-instance.
- Bridge from strategic composition to `#composition-closure`'s closure-defect $\varepsilon^\ast$ — the macro-description of a strategic composite is a distributional equilibrium statistic rather than a state, so the closure-defect formulation needs re-specification. Open.
- Full mechanism-design derivation (VCG, Bayesian-Nash) for specific AAD-relevant settings.

## Honest Limits

*[Scope honesty — strategic-composition-failures]*

- **No equilibrium exists** in cyclic games (rock-paper-scissors pure-strategy Nash; mixed-Nash saddle of fictitious play). Strategic composition has no fixed point; ergodic / distributional analysis replaces convergence.
- **Multiple equilibria with ambiguous selection** (coordination games; drive-left vs drive-right). Convergence to *some* equilibrium; AAD does not predict which.
- **Slow mixing / finite-sample failure** under regret-minimization: $O(1/\sqrt T)$ cumulative regret implies finite-horizon play may be far from CCE support.
- **Non-compact strategy spaces** (unbounded prices, resource allocations). No equilibrium without compactification; compactification may be artificial.
- **Bayesian games with strategic + epistemic uncertainty compounding.** Existence and uniqueness become pathological under certain information structures.
- **Mean-field games** ($N \to \infty$) require population-scope machinery not covered here.

## Discussion

**Sibling to `#adversarial-destabilization`.** `#adversarial-destabilization` handles the *asymmetric* adversarial case: one agent is target; attacker's tempo is exogenous parameter; sector-persistence template applies to target's mismatch with coupling-amplified disturbance. This segment handles the *symmetric* strategic case: both agents running full AAD loops; state variable is joint deviation from equilibrium; correction function is joint best-response field. The two are siblings. `#adversarial-destabilization`'s Working-Notes-flagged "coupled Lyapunov analysis is the open problem" has its formal home here — but the analysis is *not* a Lyapunov problem; it is a fixed-point problem, and the correct primitive is equilibrium convergence rather than Lyapunov descent. `#team-persistence` is recovered as the cooperative limit (all $\gamma^{\text{coop}}$ dominate; joint dynamics reduce to parallel single-agent sector-persistence with reduced effective disturbance); `#critical-mass-composition` sits in the middle with signed $\gamma$ on a matched-symmetric-Tier-1 dyad under shared target.

**The effects spiral's formal home.** `#adversarial-destabilization`'s effects spiral — $B$'s degrading model causes $B$'s actions to destabilize $A$ further — is a **joint-Jacobian eigenvalue condition** in the strategic-composition framing: the spiral exists iff $\max_{\text{candidate equilibria } \pi^\ast} \text{Re}(\lambda_{\max}(\nabla F(\pi^\ast))) > 0$, where $F$ is the joint best-response field. This condition specializes monotone-game failure (the Jacobian's symmetric part fails to be negative-definite at equilibrium). The asymmetric formulation in `#adversarial-destabilization` cannot express this condition because it treats one agent's tempo as exogenous; the symmetric coupled formulation here does.

**Class-3-composite-from-Class-1-sub-agents.** `#directed-separation` classifies agents (Class 1 modular, Class 2 fully merged, Class 3 partially modular) based on within-agent coupling. Strategic composition introduces a distinct form of coupling: *across-agent* coupling through the shared environment and cross-agent observation — each sub-agent's $M_t^{(i)}$ contains a model of other sub-agents' policies, but its own $f_M^{(i)}$ remains goal-blind. Strategic composites of Class 1 sub-agents are therefore **Class 3 composites**: within-agent processing is modular, but composite-level directed separation fails because composite $(M_c, G_c)$ acquires intrinsic coupling through the sub-agents' observations of each other. This refines `#directed-separation`'s classification: class-type is a property of composites, not just of individual agents; strategic composition is the canonical Class-1-sub-agents → Class-3-composite case.

**Mechanism-design impossibility.** If an outside designer can shape $\{O_t^{(i)}\}$, strategic composition becomes a **mechanism-design problem**: choose objectives so that the induced equilibrium *is* contraction to a designed state. Impossibility results — Gibbard-Satterthwaite 1973–75 (no dominant-strategy non-dictatorial Pareto-efficient voting mechanism for ≥3 alternatives); Myerson-Satterthwaite 1983 (no efficient, individually-rational, incentive-compatible bilateral-trade mechanism without subsidies); Arrow 1951 (no social welfare function satisfying unrestricted-domain, Pareto-efficient, IIA, non-dictatorial) — are **candidate fourth instances of `#discussion-identifiability-floor`**: external theorems forbidding design-of-alignment under stated constraints, with AAD machinery (Bayes-Nash relaxation, randomized allocations, subsidy injection) as structural escapes. Flagged for future follow-up spike; not derived in this segment.

**Meta-pattern positioning.**

- *`#discussion-separability-pattern`:* sub-scope $\alpha'$ (potential / monotone — template transfers) is separable-core; sub-scope $\beta'$ (VI / regret-minimization — set-convergence only) is structured-repair; cyclic / non-convergent / multi-equilibrium-selection-ambiguous is general-open. Candidate additional ladder (strategic-interaction regime); decide whether to surface as 8th ladder or merge into an existing ladder.
- *`#discussion-identifiability-floor`:* mechanism-design impossibility is a candidate fourth instance (flagged above).
- *`#discussion-additive-coordinate-forcing`:* the potential function $\Phi$ plays an additive-coordinate role at the strategic layer, but its additivity is a *definitional consequence* of being a potential game (Monderer-Shapley require the additivity property by definition) rather than forced by a uniqueness theorem on an AAD-internal axiom. This positions $\Phi$ as an adjacent family member, parallel to Lyapunov quadratic and IB Lagrangian, not a primary instance.

**Active-inference sharpening.** Sun-Firestone 2020's dark-room argument observes that preferences-as-priors collapse under mutual prediction. Strategic composition gives this argument a formal substrate: two agents mutually predicting each other become a **fixed-point problem**, not a Lyapunov descent. The active-inference attempt to unify goal-seeking and prediction fails here in a derivable way — the fixed point is not at the prediction-optimum; it is at the strategic-equilibrium, which is structurally different. This strengthens `#satisfaction-gap`'s positioning against preferences-as-priors without requiring additional refutation machinery.

## Working Notes

- **Effects-spiral eigenvalue condition formalization.** The condition $\max_{\pi^\ast} \text{Re}(\lambda_{\max}(\nabla F(\pi^\ast))) > 0$ is sketched in §Discussion. Deriving it for specific AAD agent classes (two Beta-Bernoulli agents on a shared DAG; two Kalman agents with coupled observations) would upgrade the spiral from discussion-grade in `#adversarial-destabilization` to derived here. Follow-on spike candidate.

- **Mechanism-design impossibility as `#discussion-identifiability-floor` Instance 4.** Would require working out the external-theorem anchoring, the boundary characterization (Bayes-Nash / randomization / subsidies as structural escapes), and the strengthened consequence (which AAD machinery the escapes operationalize). Follow-on spike.

- **Composite-class-inheritance refinement.** The Class-1-sub-agents → Class-3-composite argument needs cross-checking against `#directed-separation-under-composition` for consistency. The refinement is structurally sound but deserves dedicated cross-reference work.

- **Bridge from strategic composition to `#composition-closure` $\varepsilon^\ast$.** The macro-description of a strategic composite is an equilibrium *statistic* (joint play distribution) rather than an equilibrium *state*. The closure-defect formulation needs re-specification for this case. Open.

- **Replicator / evolutionary dynamics.** Replicator-based strategic dynamics (Sandholm 2010, *Population Games and Evolutionary Dynamics*) converge to ESS (evolutionarily stable strategies), a subset of Nash. Under which AAD-native update rules does the induced strategic dynamic match replicator? Multi-armed-bandit with softmax choice approximates replicator; gradient-descent on log-likelihood of mixed strategy is replicator exactly. Worth follow-on spike on AAD → evolutionary-dynamics correspondence.

- **Mean-field extension.** $N \to \infty$ limit with each agent interacting with a population *distribution* rather than named others. Natural extension for market / population strategic composition. Lasry-Lions 2007; Huang-Malhamé-Caines 2006. Requires population-scope condition of Section III that is currently marked GAP.
