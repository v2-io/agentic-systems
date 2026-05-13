---
spike: strategic-composition
date: 2026-04-22
status: first-pass structural spike
related_segments:
  - form-composition-closure
  - scope-composite-agent
  - result-sector-persistence-template
  - der-adversarial-destabilization
  - der-team-persistence
  - der-interaction-channel-classification
  - deriv-critical-mass-composition
  - der-directed-separation
related_gaps:
  - adversarial-edge-targeting (now closed via #der-interaction-channel-classification per TODO.md)
---

# Spike: Strategic Composition via Equilibrium Convergence

**Motivation.** AAD's Section III composition machinery is organized around *contraction to a shared target*. The sector-persistence template's state variable $\xi$ is a mismatch to some fixed point — epistemic truth, a composite strategy, or a coarse-grained macro-state. The bridge lemma then asks whether the composite trajectory contracts to zero closure-defect. This framing works when the sub-agents share objectives: $O_t^{(i)} = O_c$ or $O_i = \mathcal D(O_c)$ with consistent decomposition. It works for adversarial coupling in the limited sense that `#der-adversarial-destabilization` models: a single target agent $B$ with an exogenously-parametrized attacker $A$, where the template's state variable is $B$'s mismatch and $A$'s tempo is a coupling-amplifier of $B$'s disturbance.

What the machinery does *not* cover is the central case of strategic interaction: **two or more purposeful agents with partially-opposing $O_t^{(i)}$, each running its full AAD loop, coupled through a shared environment whose dynamics neither unilaterally controls.** Market participants, bargaining partners, competing firms, nation-states in a treaty game, two humans in a negotiation. None of these systems contracts to a shared truth. They converge (when they converge) to an *equilibrium* — a joint policy/state configuration where no agent has a unilateral improvement available. Contraction is the wrong primitive; fixed-point existence and stability is the right one.

This spike does three things:
1. Re-poses the composition question for partially-opposing objectives as an equilibrium-convergence problem.
2. Identifies where AAD's sector-persistence template transfers (under an A2'-analog from monotone- or potential-game conditions) and where it breaks (in fully general strategic settings).
3. Proposes a landing plan: a new Section III segment sibling to `#der-adversarial-destabilization` rather than a rewrite of `#form-composition-closure`.

**Depends on** (for reading): #post-composition-consistency, #scope-composite-agent, #form-composition-closure, #result-sector-persistence-template, #der-adversarial-destabilization, #result-adversarial-tempo-advantage, #der-team-persistence, #der-interaction-channel-classification, #deriv-critical-mass-composition, #der-directed-separation, #scope-agent-identity, #form-objective-functional, #def-value-object, #def-strategy-dag, #disc-identifiability-floor, #disc-separability-pattern.

---

## 1. The Gap: Contraction Is the Wrong Primitive for Strategic Composition

### 1.1 Where contraction is load-bearing in AAD's current Section III

The bridge lemma in `#form-composition-closure` (§4 of that segment, via `#result-sector-persistence-template`) asks: does the trajectory error $e_m = X_{c,m} - \Lambda_x(X_{\text{micro},\,mK_c})$ contract toward zero under the composite's correction machinery? The answer is "yes under the incremental sector bound DA2'-inc." Similarly, `#der-team-persistence`'s sub-agent condition $\alpha_i R_i \gt \rho_i^{\text{eff}}$ is a contraction condition on each sub-agent's mismatch $\delta_i$ toward its target-prediction. `#deriv-critical-mass-composition` gives $(\alpha - C)R \gt \rho + \gamma\mathcal T$ for the matched-symmetric-Tier-1 dyad — still a contraction inequality.

All three results share a common shape: *the composite has a target state (the true environment, the shared truth, the coarse-grained reality), and the Lyapunov $V(\xi) = \tfrac{1}{2}\lVert\xi\rVert^2$ decreases along the composite's correction machinery when disturbance is bounded.* The target is a *point*; the machinery *drives toward* it.

### 1.2 The strategic case: no shared target exists

Consider two purposeful agents $A$, $B$ whose objectives are partially opposing:

$$O_t^{(A)} \neq O_t^{(B)}, \quad \text{with at least one dimension of disagreement.}$$

Each runs its full AAD loop: $M_t^{(A)}, \Sigma_t^{(A)}, a_t^{(A)}, \ldots$ through the environment and $M_t^{(B)}, \Sigma_t^{(B)}, a_t^{(B)}, \ldots$. The environment couples them: $A$'s action influences $B$'s observations, $B$'s action influences $A$'s. Neither of them is optimizing $O_t^{(A)} + O_t^{(B)}$ — each optimizes its own.

*[Observation — strategic-no-shared-target]* There is no target state $\xi^\ast$ such that both $A$'s and $B$'s correction machinery drive toward it. $A$'s machinery drives toward an $A$-optimum; $B$'s drives toward a $B$-optimum; these differ.

The composite system does not contract in any direct sense. It can *converge* — in favourable cases — to a joint configuration where each agent's correction machinery no longer prescribes improvement given the other's current behaviour: a **Nash equilibrium** (Nash 1950), a **correlated equilibrium** (Aumann 1974), or at minimum the support of a **coarse correlated equilibrium** (Hannan 1957 / Moulin-Vial 1978). But equilibrium is a *fixed point* of a coupled system, not a *minimum* of a single scalar.

This is not a mild extension of the contraction framework. It is a different mathematical object: fixed-point theory on the joint best-response dynamics, not Lyapunov stability on a shared state variable. A naive attempt to fit it into `#result-sector-persistence-template` (by setting $\xi$ = "distance to joint Nash equilibrium") fails because the equilibrium point depends on *both* agents' correction machineries simultaneously — it is not exogenous, not shared, and generically not unique.

### 1.3 Symptoms in the current segment coverage

- `#scope-composite-agent` (C-i, C-ii, C-iii) enumerates three routes to composite status, all of which presume alignment. Adversarial/strategic pairs explicitly *fail* this scope. The current text labels adversarial pairs as "multi-agent, not composite," handing them off to `#der-adversarial-destabilization` — but `#der-adversarial-destabilization`'s machinery only covers the *asymmetric* case where one agent is exogenous and the other is the target. It does not cover the *symmetric* case where both agents are purposeful and running their full loops simultaneously.
- `#der-adversarial-destabilization`'s scope is exactly this gap, as its Working Notes acknowledge: "The decoupled analysis (treating $\mathcal T_A$ as exogenous) is conservative — it's the best case for $A$. In a fully coupled system, $A$'s actions against $B$ may divert adaptive capacity from $A$'s own mismatch correction, creating a self-limiting effect. The coupled Lyapunov analysis is the open problem." Reframed in this spike's terms: the coupled Lyapunov analysis is not a Lyapunov problem; it is a fixed-point problem on the joint best-response dynamics.
- `#result-adversarial-tempo-advantage`'s superlinear $b = 2$ / $b = 3/2$ scaling assumes $B$'s correction machinery is still oriented toward the true environment, not reoriented toward anticipating $A$. When $B$ is strategic — when $B$'s model $M_B$ includes $A$'s policy as a variable to track — $B$'s orientation is toward a moving $A$-dependent target, not the static environment. The superlinear advantage may attenuate or amplify, but the derivation does not apply without modification.

Gemini's broader-agent-class gap is sharp here: *strategic agents* (market participants, negotiators, adversaries in full-information games) are a large and important class that the current Section III does not formally cover.

---

## 2. The Framing Move: Fixed-Point Existence + Stability

### 2.1 Replace the primitive

*[Formulation (strategic-composition-framing)]*

For a composite of $N$ purposeful agents with partially-opposing $\{O_t^{(i)}\}$, the composition-level question is not "does the trajectory contract to zero closure-defect?" but:

(SC-1) **Existence of equilibrium.** Does there exist a joint state $(X_{c,1}^\ast, \ldots, X_{c,N}^\ast)$ — equivalently a joint policy profile $(\pi_1^\ast, \ldots, \pi_N^\ast)$ — such that no agent has a unilateral mismatch reduction available?

(SC-2) **Stability of equilibrium.** Do the coupled best-response dynamics, initialised in a neighbourhood of $(X_{c,i}^\ast)$, remain in that neighbourhood or return to it?

(SC-3) **Convergence from interior.** Do the coupled dynamics, initialised away from any equilibrium, converge to the set of equilibria?

(SC-1)-(SC-3) form a fixed-point question, a stability question, and a reachability question respectively. None of them is a Lyapunov contraction question on a shared state.

*[Discussion — why each question is independently load-bearing]*

- (SC-1) can fail: rock-paper-scissors has no pure Nash equilibrium (but does have a mixed one; the question then shifts to mixed-strategy existence). Markets in certain configurations have no equilibrium at all (e.g., Grossman-Stiglitz 1980 on informationally efficient markets with costly information).
- (SC-2) can hold when (SC-3) fails: equilibria can be locally stable but globally unreachable from most initial conditions. This is the "basin of attraction" question, central in evolutionary game theory.
- (SC-3) can hold when (SC-2) does not hold sharply: cycling or chaos can still exhibit bounded-set convergence (e.g., the *ergodic set* of a replicator dynamic). The support of a coarse correlated equilibrium is reachable even when no individual equilibrium is stable.

The three questions correspond to three levels of composition coherence. (SC-1) is a *structural* check — the interaction admits a stable joint behaviour *in principle*. (SC-2) is an *operational* check — the stable joint behaviour is reachable from nearby states. (SC-3) is a *global* check — the stable joint behaviour is reachable from most states.

### 2.2 Relation to the contraction framing

Contraction to shared truth is a *special case* of fixed-point convergence, recoverable under teleological unity $U_O = 1$:

*[Derived (contraction-as-unity-special-case)]* Under $U_O = 1$ — all agents have the same objective $O_c$ — the joint best-response dynamics degenerate into a single-objective optimization, and the composite fixed point is the joint $O_c$-optimum (assumed to be the true environment's representation, per the Section I alignment of objectives with accurate prediction in cooperative settings). The sector-persistence template applies on the joint mismatch. The equilibrium question reduces to the contraction question.

As $U_O$ decreases from 1, the equilibrium point drifts away from the shared truth and becomes a compromise between the $\{O_t^{(i)}\}$. The Lyapunov function loses its interpretation as "distance to truth" and must be re-specified as "distance to equilibrium" — a different object with different existence and stability theorems.

The composition-scope-condition's (C-i) / (C-ii) / (C-iii) routes are all $U_O$-high regimes. The strategic-composition regime is exactly $U_O$-low — what the scope condition currently *excludes* from composite status. This spike's proposal is that $U_O$-low composites are not "non-composites" but composites of a *different type*: equilibrium composites rather than contraction composites.

### 2.3 New scope route (proposed)

*[Proposed Scope (composition-scope-condition, route C-iv)]*

**(C-iv) Equilibrium-convergent strategic interaction.** There exists an equilibrium concept $\mathcal E$ (Nash, correlated, or coarse correlated) such that the joint best-response dynamics of $\{A_i\}$ converge to (or cycle within the support of) $\mathcal E$. The sub-agents' objectives may be partially opposing, but the interaction admits a stable joint behaviour.

This is qualitatively distinct from (C-i)-(C-iii): it does not require shared objectives, hierarchical derivation, or mutual benefit. It requires only that the strategic interaction is *structurally convergent* in the game-theoretic sense.

*[Epistemic Status]* This is a candidate scope route. The current `#scope-composite-agent` presents three routes disjunctively; adding (C-iv) would admit strategic interactions as composites of a specific type — call them **strategic composites** — distinguished from **alignment composites** (C-i, C-ii) and **mutual-benefit composites** (C-iii). Whether this distinction is worth surfacing as a formal scope addition, or whether strategic composites are better handled as a separate Section III segment parallel to `#form-composition-closure`, is one of this spike's landing decisions (§9).

---

## 3. Monotone-Game / Potential-Game Conditions: The A2'-Analog

### 3.1 The lift target

AAD's A2' sub-scope partition (`#deriv-sector-condition`, `#der-gain-sector-bridge`) gives sub-scope $\alpha$ — where A2' is *derived* under B1 directional fidelity — a principled place where the sector condition holds by construction. The corresponding lift target for strategic composition is: under what strategic-interaction conditions can we *derive* an equivalent of A2' for the coupled best-response dynamics?

### 3.2 Potential games (Monderer-Shapley 1996)

A strategic interaction $(\{A_i\}, \{O_t^{(i)}\})$ is a **potential game** (Monderer & Shapley 1996, *Games and Economic Behavior* 14) when there exists a scalar potential function $\Phi$ such that for each agent $i$ and each unilateral deviation:

$$O_t^{(i)}(\pi_i', \pi_{-i}) - O_t^{(i)}(\pi_i, \pi_{-i}) = \Phi(\pi_i', \pi_{-i}) - \Phi(\pi_i, \pi_{-i})$$

i.e., each agent's unilateral improvement matches the potential's unilateral improvement in direction and magnitude. When $\Phi$ exists, the best-response dynamics monotonically improve $\Phi$: every unilateral improvement step is a $\Phi$-ascent step.

*[Derived (A2'-analog-potential, from Monderer-Shapley 1996)]* If $(\{A_i\}, \{O_t^{(i)}\})$ is a potential game with potential $\Phi$, and each agent's correction machinery is directionally faithful (B1 in the `#der-gain-sector-bridge` sense) to $\nabla_{\pi_i} O_t^{(i)}$, then the joint best-response dynamics satisfies:

$$\frac{d\Phi(\pi)}{dt} = \sum_i \langle \nabla_{\pi_i}\Phi,\; \dot\pi_i\rangle \geq \alpha_{\text{joint}} \lVert \nabla\Phi \rVert^2$$

for some $\alpha_{\text{joint}} \gt 0$ whenever the joint configuration is not at a stationary point of $\Phi$. This is A2' transcribed to $\xi = $ gradient-of-potential, $F = $ best-response velocity field, with the same quadratic Lyapunov structure.

**What this buys.** Under the potential-game condition:

1. **Equilibrium existence** follows from potential-function compactness (if the strategy space is compact and $\Phi$ is continuous, $\Phi$ attains a maximum at some $\pi^\ast$, which is a Nash equilibrium).
2. **Equilibrium stability** follows from $\Phi$'s role as a Lyapunov function — the dynamics monotonically ascend $\Phi$ and approach its stationary points.
3. **Convergence from interior** follows under additional regularity (Lojasiewicz-type inequalities for analytic $\Phi$, or strict concavity near equilibria).
4. **Sector-persistence template transfers.** The state variable is $\xi = \pi - \pi^\ast$ (deviation from equilibrium); the correction function is the joint best-response velocity field; the potential's $\alpha_{\text{joint}}$ supplies the sector-condition lower bound.

Potential games are a *rich* class: congestion games (Rosenthal 1973), coordination games, strategic-complement games, public-goods games with quadratic utility. A2' transfers cleanly to each. **The sector-persistence template applies to potential-game composites**, with $\xi = \pi - \pi^\ast$, $F$ = joint best-response field, $\alpha = \alpha_{\text{joint}}$ from $\Phi$'s gradient bound, $R$ = size of the basin around $\pi^\ast$, $\rho_\xi$ = exogenous disturbance rate on strategy space.

*[Epistemic Status — A2'-analog-potential]* **Exact** under the potential-game condition + B1 directional fidelity. The derivation is essentially Monderer-Shapley's convergence theorem rewritten in AAD's notation. The contribution is the recognition that the A2'-analog for strategic composition lives at the *potential-function gradient*, not at any individual agent's mismatch.

### 3.3 Monotone games (Rosen 1965)

Weaker than potential games: a game is **diagonally strictly concave** (Rosen 1965, *Econometrica* 33) when the Jacobian of the joint gradient field is negative definite on the joint strategy space:

$$\forall \pi, \pi' \text{ distinct}: \quad \sum_i \langle \pi_i' - \pi_i,\; \nabla_{\pi_i} O_t^{(i)}(\pi') - \nabla_{\pi_i} O_t^{(i)}(\pi)\rangle \lt 0$$

This is the game-theoretic analog of strong monotonicity. It is weaker than the potential-game condition in that no scalar potential need exist; it is stronger than mere concavity of each agent's payoff in its own strategy.

*[Derived (A2'-analog-monotone, from Rosen 1965)]* Under Rosen's diagonal strict concavity, there exists a unique Nash equilibrium, and the joint best-response dynamics (or any dynamics whose velocity field is the joint gradient) converges to it exponentially. The convergence rate is bounded below by the smallest eigenvalue of the symmetric part of the joint Jacobian. This plays the role of $\alpha_{\text{joint}}$.

**What this buys and does not buy.** Uniqueness of equilibrium is stronger than potential-game gives (potential games can have multiple local maxima of $\Phi$, hence multiple Nash equilibria). But no scalar Lyapunov function exists — the convergence argument uses a *vector-valued* Lyapunov argument, or equivalently, a non-symmetric quadratic form on the joint deviation. The sector-persistence template's quadratic Lyapunov $V(\xi) = \tfrac{1}{2}\lVert\xi\rVert^2$ is not directly applicable; a weighted norm version (weighted by the symmetric part of the Jacobian) is required.

This is a genuine extension of the template, not a direct transfer. The extension is standard in variational-inequality theory (see §4 below).

### 3.4 The A2' sub-scope partition for strategic composition

Compiling §3.2 and §3.3 into a sub-scope partition parallel to `#deriv-sector-condition`'s $\alpha / \beta$ split:

**Sub-scope $\alpha'$ (derived A2'-analog for strategic composition):**
- Potential games (Monderer-Shapley 1996) with B1 directional fidelity: full sector-persistence template applies on the joint potential's gradient.
- Monotone games (Rosen 1965) with B1 directional fidelity: weighted-norm template applies; convergence rate from Jacobian eigenvalues.
- Strongly-monotone games (Jacobian's symmetric part uniformly positive-definite): exponential convergence; quadratic Lyapunov applies in the Jacobian-induced inner product.
- Exponential-family dual-averaging under concave objectives: classical online-learning convergence theorems transfer.

**Sub-scope $\beta'$ (A2'-analog assumed or unavailable):**
- Non-monotone games (e.g., rock-paper-scissors, matching pennies): fixed points exist only in mixed strategies; best-response dynamics cycle rather than converge. A2'-analog is false.
- Games without Jacobian regularity (discontinuous payoffs, non-differentiable best-responses): variational-inequality formulation is required, but the standard monotonicity conditions may fail.
- Games with multiple equilibria and no potential: selection among equilibria is not determined by the dynamics; A2'-analog holds locally within each basin, but the inter-basin structure is beyond the template.

The partition is **parallel in form** to `#deriv-sector-condition`'s $\alpha / \beta$ partition but lives at a different level — it partitions *strategic-interaction structures* rather than *single-agent update rules*. Under sub-scope $\alpha'$, the sector-persistence template extends to strategic composition via its joint-gradient transcription; under sub-scope $\beta'$, the template does not apply and weaker results must be used (§4).

---

## 4. Non-Potential / Non-Monotone Games: What Remains

### 4.1 Variational-inequality formulation (Facchinei-Pang 2003)

Every strategic interaction with continuous strategy spaces and sufficiently regular payoffs can be reformulated as a **variational inequality (VI)**:

$$\text{find } \pi^\ast \in \mathcal K \text{ such that } \langle F(\pi^\ast),\; \pi - \pi^\ast\rangle \geq 0 \quad \forall \pi \in \mathcal K$$

where $F$ is the joint pseudo-gradient field (agent $i$'s own gradient on its own strategy) and $\mathcal K$ is the joint strategy space. Nash equilibria are exactly the solutions of this VI (Facchinei-Pang 2003, *Finite-Dimensional Variational Inequalities and Complementarity Problems*).

*[Derived (equilibrium-existence-via-VI)]* When $\mathcal K$ is compact and convex and $F$ is continuous, the VI has at least one solution (Hartman-Stampacchia theorem). Hence: **pure-strategy Nash equilibrium exists for continuous-strategy games with compact convex strategy sets and continuous payoffs.** Nash's 1950 existence result for mixed-strategy equilibrium in finite games is a discrete analog.

**What this does not buy.** VI existence does not imply convergence of any specific dynamic to the solution. Solutions may be non-unique. Solution sets may be disconnected. The VI framework is powerful for existence and characterization but weak on dynamics — which is the load-bearing question for AAD.

### 4.2 Regret minimization and correlated equilibrium

Under fully general strategic interaction (no monotonicity, no potential), a weaker convergence result is available via **regret minimization** (Foster-Vohra 1997, Hart-Mas-Colell 2000):

*[Derived (regret-minimization-convergence)]* If each agent runs a no-regret learning algorithm (e.g., Hedge / multiplicative weights, Freund-Schapire 1997), then the empirical joint distribution of play converges to the set of **coarse correlated equilibria** (CCE) as $T \to \infty$. Convergence rate: $O(1/\sqrt T)$ for cumulative regret, hence $O(1/\sqrt T)$ to the CCE set.

**What this buys.** The regret-minimization result does not require any structure on the game beyond "each agent can compute its own regret." It applies to arbitrary strategic interactions, including non-monotone non-potential games. It gives a concrete **convergence guarantee** — to the CCE set, not to any specific equilibrium — and a concrete **rate** ($1/\sqrt T$ in cumulative regret).

**What this does not buy.** Convergence is to the *support* of the CCE, not to any specific correlated equilibrium. The CCE set can be large (includes all Nash equilibria, all correlated equilibria, and additional joint distributions). The empirical distribution may cycle within the CCE support without ever converging pointwise.

*[Derived (CCE-as-weakest-composite-consistency)]* Under sub-scope $\beta'$, the strongest available composite consistency claim is: the empirical joint behaviour converges to the CCE set. This is *weaker* than Nash-equilibrium convergence and *much weaker* than contraction-to-truth. It is, however, a consistency claim: asymptotically, the joint play is statistically characterizable by a set of equilibrium-like constraints.

**AAD's honest limit in this regime.** Under sub-scope $\beta'$, AAD can predict:
1. Long-run joint play lies in the CCE support (Foster-Vohra / Hart-Mas-Colell).
2. Short-run dynamics may cycle, exhibit chaos, or drift (no guarantee).
3. The per-agent mismatch $\delta_i$ does not converge to zero (each agent has residual prediction error about the others' behaviour).
4. The sector-persistence template does not apply.

### 4.3 The hierarchy

*[Discussion — strategic-composition-hierarchy]*

Compiling §3 and §4 into a ladder parallel to `#disc-separability-pattern`'s six ladders:

| Strategic-interaction regime | A2'-analog | Equilibrium | Convergence | Template applies? |
|---|---|---|---|---|
| Shared objective ($U_O = 1$) | A2' (single-agent) | Joint optimum | To shared truth | Yes (`#form-composition-closure`) |
| Potential game | A2'-analog on $\nabla\Phi$ | Nash via $\Phi$-max | Best-response to Nash | Yes (joint gradient) |
| Monotone game (Rosen) | Weighted A2'-analog | Unique Nash | Exponential to Nash | Yes (weighted norm) |
| Non-monotone / non-potential with regularity | VI existence | Some Nash (possibly many) | Not guaranteed | No |
| Fully general (no-regret only) | None | CCE support | To CCE set only | No |
| Non-convergent (cyclical / chaotic) | None | May not exist | Ergodic at best | No |

This is a candidate **seventh ladder for `#disc-separability-pattern`**: strategic-interaction regime. The separable-core is potential/monotone games (template transfers); the structured-repair is VI / regret-minimization (weaker guarantees); the general-open is non-convergent strategic interaction.

---

## 5. Two-Agent Zero-Sum Worked Example

To check the framing has force, derive a specific two-agent zero-sum case explicitly. This is the cleanest non-trivial strategic composition: adversarial, with a potential function (the negative of one agent's objective is the other's), so the A2'-analog applies and the sector-persistence template should transfer.

### 5.1 Setup

Two agents $A$ and $B$ interact through a shared scalar state $s \in \mathbb R$. Each chooses an action $a_i \in [-1, 1]$; the state evolves as $s_{t+1} = s_t + a_A - a_B + w_t$ with $w_t \sim \mathcal N(0, \sigma^2)$.

Objectives (zero-sum):

$$O_t^{(A)}(s) = s, \quad O_t^{(B)}(s) = -s$$

$A$ wants $s$ high; $B$ wants $s$ low. Payoff per step for each agent is its objective.

Each agent runs a simple AAD-style update: maintains a model of the environment dynamics (including the other agent's action), updates it from observations of $s$, and chooses its action greedily given its model. Class 1 (modular) architecture; sub-scope $\alpha$ updates.

### 5.2 Potential-function verification

Define $\Phi(a_A, a_B) = a_A - a_B$ — the drift rate of $s$. Then:

$$O_t^{(A)}(a_A', a_B) - O_t^{(A)}(a_A, a_B) = \mathbb E[s \mid a_A', a_B] - \mathbb E[s \mid a_A, a_B] = a_A' - a_A$$

$$\Phi(a_A', a_B) - \Phi(a_A, a_B) = a_A' - a_A$$

These match. Similarly for $B$'s deviations:

$$O_t^{(B)}(a_A, a_B') - O_t^{(B)}(a_A, a_B) = -(a_B' - a_B) = -(a_B' - a_B)$$

$$\Phi(a_A, a_B') - \Phi(a_A, a_B) = -(a_B' - a_B)$$

These also match. So $(O_t^{(A)}, O_t^{(B)})$ admits the potential $\Phi(a_A, a_B) = a_A - a_B$. Zero-sum games on scalar actions are potential games in this weak sense.

### 5.3 Equilibrium and stability

The potential $\Phi$ is unbounded on $\mathbb R^2$ but bounded on $[-1, 1]^2$. Its maximum over the box is at $(a_A, a_B) = (1, -1)$ — $A$ pushes up maximally, $B$ pushes down maximally. This is the Nash equilibrium: each agent plays its extreme, no unilateral deviation helps.

*[Derived — zero-sum-scalar-Nash]* The Nash equilibrium of the scalar zero-sum example is $(a_A^\ast, a_B^\ast) = (1, -1)$, located at the boundary of the strategy space.

**Stability under best-response dynamics.** Starting from any interior point $(a_A, a_B) \in (-1, 1)^2$, each agent's best response is to move toward its own extreme. Best-response dynamics converges to $(1, -1)$ in finite time (one update per agent). Stability is trivial: the equilibrium is at a vertex of the feasible set, robust to any perturbation that stays in the feasible set.

### 5.4 Sector-persistence template transfer

*[Derived — zero-sum-scalar-template-instantiation]* With state variable $\xi = (a_A - 1, a_B + 1)$ (deviation from Nash) and correction function $F(\xi) = -\xi$ (each agent moves toward its extreme at unit rate), the template's preconditions are satisfied:

- (T1) $F(0) = 0$. At equilibrium, no correction is applied. ✓
- (T2) $\xi^T F(\xi) = \lVert\xi\rVert^2 \geq \alpha\lVert\xi\rVert^2$ with $\alpha = 1$, on the feasible region $\lVert\xi\rVert \leq R$ with $R = 2\sqrt 2$ (the box's diameter). ✓
- (T3) $\lVert w_t\rVert \leq \rho$ — environmental disturbance bounded (say $\sigma \lt \infty$ gives Model S form with $\sigma_\xi^2 = 2\sigma^2$). ✓

Ultimate bound under Model S: $R^\ast = \sigma\sqrt{n/(2\alpha)} = \sigma$ (for $n = 2$ agents, $\alpha = 1$). For this to fit in $R$: $\sigma \lt 2\sqrt 2 \approx 2.83$. Under any reasonable noise level, the composite strategic dynamics is bounded around Nash.

**What this establishes.** The scalar zero-sum example is a genuine strategic composite where:
- No shared objective exists.
- An equilibrium exists (at the strategy-space boundary).
- The equilibrium is stable in the strong sector-condition sense.
- The sector-persistence template transfers with $\xi$ = deviation-from-Nash, $\alpha$ from potential gradient.

This is the cleanest evidence that the framing move works: strategic composition with potential structure *is* a valid instance of the sector-persistence template, with the equilibrium point (not shared truth) as the target.

### 5.5 Why this is not trivial

One might object: "zero-sum scalar games are boring; the Nash equilibrium is just at the boundary." The non-trivial content is:

- The framing **treats strategic agents as full AAD agents** running their own loops, with the composite dynamics emerging from the coupling. The Nash equilibrium is *not* given exogenously; it arises from the interaction of each agent's correction machinery.
- The sector-persistence template's application **does not require goal alignment** — the two agents have maximally opposing objectives, yet the template works with $\Phi$ as the scalar coordinate.
- The $\alpha_{\text{joint}}$ that gates convergence **inherits from the potential's gradient**, not from any individual agent's $\alpha_i$. This is a new quantity — "interaction contraction rate" — that does not appear in the single-agent template.
- The `#deriv-critical-mass-composition` inequality $(\alpha - C)R \gt \rho + \gamma\mathcal T$ takes a new form under strategic composition: $\gamma$ is no longer "one-sided coupling effectiveness" but "two-sided *potential-gradient* coupling," and the sign-structure is determined by the potential rather than by the cooperative/adversarial label.

### 5.6 What this case does not cover

The scalar zero-sum example is the *easiest* strategic-composition case. It is zero-sum *and* potential *and* scalar *and* has equilibrium at the boundary. Harder cases:

- **Non-scalar actions:** matrix games with payoff matrices that admit mixed-strategy equilibria but not pure. The potential function is more subtle (Nash equilibrium in mixed strategies corresponds to saddle points of the payoff; convergence requires averaging dynamics).
- **Non-zero-sum:** coordination games (multiple Nash equilibria, potential function is max-plus), chicken / hawk-dove (non-unique equilibrium, selection depends on dynamics).
- **Rock-paper-scissors cyclical:** no pure-strategy Nash; mixed-strategy Nash exists but is a saddle point of fictitious play; best-response dynamics cycles.
- **Imperfect information:** Bayesian games where each agent's model of the other's objective is uncertain, and the update dynamics compound strategic uncertainty with epistemic uncertainty.

These require stronger machinery (the variational-inequality formulation §4.1, the regret-minimization convergence §4.2, or Bayesian-Nash equilibrium concepts with their own existence and stability theorems).

---

## 6. Mechanism-Design Connection

### 6.1 The designer's question

If an outside designer — call them $D$ — has control over the agents' objectives (e.g., by choosing a reward function, by contract design, by institutional constraints), then strategic composition becomes a **mechanism-design problem**: under what conditions can $D$ design $\{O_t^{(i)}\}$ such that the equilibrium of the induced strategic interaction *is* contraction to a desired state?

This reverses the composition direction. Instead of asking "what does this strategic interaction converge to?" we ask: "choose the objectives so that convergence is to what we want."

### 6.2 The connection to `#adversarial-edge-targeting`

The TODO.md notes that `#adversarial-edge-targeting` is now closed via `#der-interaction-channel-classification` — the recipient-side theory pairs with an emitter-side optimizer for which edges to attack. Mechanism design is the *inverse* problem: choose the strategic interaction's payoff structure such that *no* edge attack succeeds, i.e., the equilibrium is robust.

*[Proposed — mechanism-design-robust-composition]* A composite is **mechanism-design-robust** if:

1. The induced potential function $\Phi$ has a unique maximum at the desired joint state $\pi^\ast$.
2. The maximum is strict (strict concavity in a neighborhood; or equivalently, strong monotonicity of the gradient field).
3. The strategy space is compact and convex, ensuring equilibrium existence.
4. The potential's gradient bound $\alpha_{\text{joint}}$ exceeds the environmental disturbance rate $\rho$, ensuring sector-persistence at the composite level.

Under (1)-(4), the sector-persistence template transfers, the equilibrium is the designed joint state, and the composite is a *designed contraction composite* — a strategic composite engineered to behave like a contraction composite.

**Example.** Vickrey-Clarke-Groves (VCG) auctions (Vickrey 1961, Clarke 1971, Groves 1973) design the payoff structure so that truthful bidding is a dominant-strategy equilibrium, and the equilibrium allocation maximizes social welfare. The potential function is the social welfare; the mechanism's design is the payoff transformation that makes each agent's incentive gradient align with the social-welfare gradient.

*[Hypothesis — mechanism-design-as-route-C-i-engineering]* Mechanism design is the *engineering* counterpart of `#scope-composite-agent`'s (C-i) route. (C-i) asks "does a shared composite objective exist such that each agent's effective policy is $\epsilon$-compatible?"; mechanism design asks "can we *construct* the payoff structure so that a shared composite objective emerges from the equilibrium?" The two are dual: (C-i) is a *test*, mechanism design is a *construction*.

### 6.3 When mechanism design fails

Impossibility results in mechanism design (Gibbard-Satterthwaite 1973-75, Myerson-Satterthwaite 1983, Arrow 1951) identify conditions under which *no* mechanism can achieve certain joint objectives:

- **Gibbard-Satterthwaite:** no dominant-strategy voting mechanism is both non-dictatorial and Pareto-efficient for three or more alternatives.
- **Myerson-Satterthwaite:** no mechanism for bilateral trade with private valuations is simultaneously efficient, individually rational, and incentive-compatible, without subsidies.
- **Arrow:** no social welfare function satisfies unrestricted domain, Pareto efficiency, independence of irrelevant alternatives, and non-dictatorship.

These correspond to cases where the strategic-composition design problem is *unsolvable* — there is no choice of $\{O_t^{(i)}\}$ that makes the equilibrium align with the designer's goals under the given constraints. In AAD's framing, this is a **composition-design identifiability floor**: a structural no-go result derived from an external theorem, analogous to the floor results in `#disc-identifiability-floor`.

*[Discussion — composition-design-floor]* These impossibility results are candidates for an extension to `#disc-identifiability-floor`. The pattern is the same: an external theorem (Gibbard-Satterthwaite, Arrow) establishes a structural no-go; AAD machinery names the unique escape (relaxing one of the constraints — e.g., Bayes-Nash instead of dominant-strategy, randomized allocations, etc.). This is a candidate fourth instance of the `#disc-identifiability-floor` pattern, joining the two current instances (on-policy detection, L1' mixture identifiability).

---

## 7. Relation to Existing `#der-adversarial-destabilization`

### 7.1 Sibling, not replacement

`#der-adversarial-destabilization` handles the **asymmetric adversarial case**: one agent $B$ is the target, the attacker $A$ is treated as exogenous (its tempo $\mathcal T_A$ is a parameter, not a dynamical variable). The sector-persistence template applies to $B$'s mismatch $\delta_B$ with coupling-amplified disturbance $\rho_B = \rho_{B,\text{base}} + \gamma_A \mathcal T_A$.

This spike's strategic-composition framing handles the **symmetric strategic case**: both agents are full AAD agents, running their own loops, with their dynamics coupled. The state variable is the *joint* deviation from equilibrium, not any individual mismatch; the correction function is the joint best-response field, not any individual agent's correction.

The two are siblings, not competitors. Specifically:

*[Derived — sibling-relationship]*

1. **`#der-adversarial-destabilization`** is the strategic-composition framing *restricted* to the case where one agent's correction machinery is held fixed (exogenous). This is the "worst case for $B$" analysis — assumes $A$ can always play its best response and does not accrue its own disturbance.
2. **Strategic-composition (this spike)** is the *symmetric* full analysis where both agents' corrections co-evolve. It recovers `#der-adversarial-destabilization` in the limit where $A$'s own sector-persistence is far from its limit (so $A$'s tempo is effectively exogenous).
3. **`#der-team-persistence`** is the strategic-composition framing *restricted* to the cooperative limit where all $\gamma_{j\to i}^{\text{coop}}$ terms dominate and $\gamma_{j\to i}^{\text{adv}} = 0$. The joint dynamics then reduces to parallel single-agent sector-persistence with reduced effective disturbance.
4. **`#deriv-critical-mass-composition`** sits in the middle: symmetric-matched-Tier-1 dyad, signed $\gamma$, but still with a *shared target state*. Strategic composition with partially-opposing objectives generalizes this by allowing the target state to depend on the agents' interaction, not to be fixed exogenously.

### 7.2 What strategic composition adds to `#der-adversarial-destabilization`

The recipient-side classification (`#der-interaction-channel-classification`) gives a structural picture of what happens when $A$'s event arrives at $B$. Strategic composition closes the loop on the *emitter* side: $A$ is also running its full AAD loop, $B$'s actions are also entering $A$'s disturbance, and the composite equilibrium depends on both sides' sector-parameters.

Specifically: the **effects spiral** discussed in `#der-adversarial-destabilization` — where $B$'s degrading model causes $B$'s actions to be more destabilizing to $A$ — is a **coupled-dynamics phenomenon** that the strategic-composition framing naturally captures. When the spiral exists, the joint best-response dynamics has a diverging trajectory; when it is absent, the joint dynamics converges to some equilibrium.

The strategic-composition framing is therefore the *formal home* for the effects spiral, which `#der-adversarial-destabilization`'s Working Notes currently acknowledge as a qualitatively-clear but not formally-derived mechanism.

### 7.3 The fully-coupled Lyapunov / fixed-point characterization

*[Sketch — effects-spiral-formal]* In the strategic-composition framing, the effects spiral corresponds to the joint dynamics having no stable equilibrium in the interior of the joint strategy space. This is a property of the joint Jacobian's eigenstructure: when the joint gradient field has *positive* real eigenvalues at any putative equilibrium (or when no equilibrium exists in the feasible set), the dynamics diverges. The *rate* of divergence is set by the largest positive real eigenvalue.

The strategic-composition framing thus promotes the effects spiral from "qualitatively clear" to "eigenvalue condition on the joint Jacobian at candidate equilibria." The condition is:

$$\text{Effects spiral iff } \max_{\text{candidate equilibria }\pi^\ast} \text{Re}(\lambda_{\max}(\nabla F(\pi^\ast))) \gt 0$$

where $F$ is the joint best-response field and $\nabla F$ is its Jacobian. This is a standard dynamical-systems condition that specializes the monotone-game condition's failure.

*[Epistemic Status]* Sketch. The condition is formal but requires a specific model of the coupled dynamics to evaluate. The contribution is the recognition that the spiral is a *joint-eigenvalue* phenomenon, not a separate mechanism.

---

## 8. Class-2 (Merged) Scope: Does Strategic Composition Land in Class 3?

### 8.1 The question

Class 2 (fully merged) architectures fail `#der-directed-separation` by construction — LLM-based agents in particular have $f_M$ and $f_G$ entangled. The current scope exit directs Class 2 agents to `03-logogenic-agents/`. But strategic composition naturally involves Class 2-like coupling: each agent's model $M_t^{(i)}$ includes *the other agent's policy*, so $M_t$ is entangled with $G_t$ in a different sense — not internally within one agent, but across agents.

Does this push strategic composites out of Section II's scope and into `03-logogenic-agents/` territory? Or does strategic composition have a principled place in **Class 3 (partially modular)** — where the entanglement is across-agent rather than within-agent?

### 8.2 The distinction

Let us distinguish two kinds of coupling:

1. **Within-agent coupling** (Class 2): agent $i$'s own $f_M^{(i)}$ depends on $G_t^{(i)}$. This violates `#der-directed-separation`'s scope condition for *agent $i$*. Hands off to `03-logogenic-agents/`.
2. **Across-agent coupling** (strategic): agent $i$'s $M_t^{(i)}$ depends on agent $j$'s state, but agent $i$'s own $f_M^{(i)}$ is still goal-blind — it updates $M_t^{(i)}$ based on whatever events arrive, without reference to $G_t^{(i)}$. The across-agent coupling is through the environment and through agent $i$'s observations of agent $j$'s actions.

*[Derived — strategic-composition-class-preservation]* Strategic composition does **not** force Class 2 status. Each agent individually can be Class 1 (modular within itself), yet the composite dynamics exhibits strategic coupling. The across-agent coupling is *through the environment and the event stream*, not through internal entanglement. Hence strategic composites of Class 1 sub-agents are Class 3 composites: the sub-agents' internal processing is modular, but the composite-level observable state $(M_c, G_c)$ — if we try to define it — has intrinsic coupling because the sub-agents' observations include each other's actions.

### 8.3 The composite's own class

*[Discussion — composite-class-inheritance]* Composite class inherits from sub-agents but with an additional coupling factor:

- Composite of Class 1 sub-agents with *aligned* objectives (scope route C-i, C-ii, or C-iii): Class 1 composite. Standard `#form-composition-closure` applies.
- Composite of Class 1 sub-agents with *partially-opposing* objectives (strategic composition): Class 3 composite. `#der-directed-separation` fails at the composite level because the composite's $M_c$ (the joint model of the shared environment, plus each agent's model of the others) includes goal-dependent content from each sub-agent, which enters the composite via the coarse-graining. Strategic composition is the *canonical Class 3 composite case*.
- Composite of Class 2 sub-agents: Class 2 composite. Inherits logogenic-agent status; `03-logogenic-agents/` territory.

The key point: **strategic composition gives AAD a clean Class 3 composite type that the current framework does not explicitly cover.** It is not Class 2 (the sub-agents are modular), and it is not Class 1 (the composite's directed separation fails). It is Class 3 *at the composite level* even when all sub-agents are Class 1.

This is a refinement of the current Class 1/2/3 classification: the classes apply not just to individual agents but to *composites*, and composite class is a function of sub-agent class and the scope route (alignment vs strategic).

---

## 9. Honest Limits

### 9.1 Where strategic-composition convergence fails

*[Scope honesty — strategic-composition-failures]*

- **No equilibrium exists.** Classic case: rock-paper-scissors (no pure Nash, mixed Nash is a saddle of fictitious play). Generalization: games with cyclic preference structures. Strategic composition has no fixed point; dynamics cycles indefinitely. AAD machinery says: long-run joint behaviour is captured by the ergodic distribution on the strategy space, which may be the mixed Nash support. The sector-persistence template does *not* apply.
- **Multiple equilibria, selection ambiguous.** Coordination games (two equilibria of equal quality — e.g., drive-on-the-left vs drive-on-the-right). Strategic composition converges to *some* equilibrium; which one depends on initial conditions and dynamics. Selection results (risk-dominance, payoff-dominance, Pareto-dominance) give partial guidance but no unique prediction.
- **Slow mixing / finite-sample failure.** Even under regret-minimization, convergence rate is $O(1/\sqrt T)$. For large strategy spaces, the time to be close to the CCE set may exceed any practical horizon. AAD's tempo framework can name this: the composite's effective tempo on strategic convergence is $O(1/\sqrt T)$, much slower than single-agent sector-convergence's exponential rate.
- **Non-compact strategy spaces.** Continuous actions with unbounded ranges (prices in an unbounded market, resource allocations with no upper bound) can have no equilibrium. Compactification (e.g., pricing ceiling) restores existence but may be artificial.
- **Imperfect information with strategic uncertainty compounding epistemic uncertainty.** Bayesian-Nash equilibria can have pathological existence and uniqueness properties (multiplicity, non-existence for certain information structures). AAD's scope in this regime is sketch-grade.

### 9.2 Where the sector-persistence template does not extend

*[Sub-scope $\beta'$ scope exit]*

Under sub-scope $\beta'$ (§3.4) — non-potential non-monotone games — the sector-persistence template's quadratic Lyapunov machinery does not apply. The strongest available result is regret-minimization convergence to the CCE set. This is:

- A set-convergence result, not a point-convergence result.
- A *cumulative average* result, not a *trajectory* result.
- A weak notion of consistency, not a contraction to truth.

AAD's honest claim in sub-scope $\beta'$ is narrow: long-run joint play is statistically characterizable. Short-run dynamics and per-agent mismatch are not predicted by AAD machinery.

### 9.3 What this spike does not establish

- **General convergence proof for non-potential games under AAD-native update rules.** Potential-game and monotone-game convergence results are imported from the game-theory literature (Monderer-Shapley 1996, Rosen 1965). The AAD contribution is the recognition that the sector-persistence template transfers when these conditions hold; the derivations themselves are not re-proved here.
- **Explicit joint Jacobian analysis for specific AAD agent architectures.** The eigenvalue condition for the effects spiral (§7.3) is stated abstractly; working it out for specific Bayesian-updating or gradient-descent agents with their own sector-parameters is a follow-on exercise.
- **Bridge from strategic composition to `#form-composition-closure`'s closure-defect $\varepsilon^\ast$.** The coarse-graining question — does the macro-description of a strategic composite as a single AAD agent have bounded closure defect? — is not addressed. Heuristically, the macro-description is an equilibrium *statistic* (joint play distribution) rather than an equilibrium *state*, so the closure-defect formulation needs re-specification.
- **Full mechanism-design derivation for specific AAD-relevant settings.** The VCG connection (§6.2) is sketched; a full derivation showing that VCG-designed mechanisms produce $\alpha_{\text{joint}}$-bounded strategic composites is a follow-on spike.

---

## 10. Landing Plan

### 10.1 Primary landing

Recommend a new Section III segment `#deriv-strategic-composition`:

- **Type**: *derived* + *scope* — the result is derived (under A2'-analog-potential or A2'-analog-monotone); the scope restriction to sub-scope $\alpha'$ is explicit.
- **Status**: *conditional* (under potential/monotone-game scope) or *robust-qualitative* (overall, for the framing move).
- **Depends on**: #post-composition-consistency, #scope-composite-agent, #result-sector-persistence-template, #form-objective-functional, #der-adversarial-destabilization, #der-team-persistence, #deriv-critical-mass-composition, #der-interaction-channel-classification.
- **Position**: Section III, after `#der-adversarial-destabilization` and `#der-interaction-channel-classification`, before (or alongside) `#result-adversarial-tempo-advantage`. It is the *symmetric* counterpart to `#der-adversarial-destabilization`'s asymmetric treatment.

### 10.2 Satellite moves

- **`#scope-composite-agent`**: add route (C-iv) equilibrium-convergent strategic interaction to the disjunctive scope, with reference to `#deriv-strategic-composition` for the formal content. Alternative: keep (C-iv) out of the scope disjunction and treat strategic composites as a *separate* type of composite (not covered by composition-scope-condition, but covered by a parallel strategic-composition scope statement). The choice hinges on whether strategic composites are "composites of a different type" (unify under one scope condition with multiple routes) or "a different thing entirely" (separate scope condition). **Preferred reading**: treat as a different type within the same scope condition, via (C-iv). Reason: the composite is still a coherent object with a joint persistence story; calling it "not a composite" overclaims the alignment requirement.
- **`#der-adversarial-destabilization`**: add cross-reference to `#deriv-strategic-composition` indicating the fully-coupled analysis is the strategic-composition segment. The Working Note's "coupled Lyapunov analysis is the open problem" can be replaced with a reference.
- **`#deriv-critical-mass-composition`**: add a note that the matched-symmetric-Tier-1 dyad generalizes to strategic composition under the potential-game condition, with $\gamma$ in the signed coupling form becoming a potential-gradient coupling.
- **`#disc-separability-pattern`**: add seventh ladder — strategic-interaction regime (separable-core: potential/monotone games; structured-repair: VI/regret-minimization; general-open: non-convergent / cyclic).
- **`#disc-identifiability-floor`**: add fourth instance candidate — mechanism-design impossibility (Gibbard-Satterthwaite, Arrow, Myerson-Satterthwaite) as a structural no-go derived from external social-choice theorems, with AAD machinery naming the escape routes (Bayes-Nash relaxation, randomized allocation, etc.).
- **`#der-directed-separation`**: add a clause indicating that composite class inherits from sub-agent class with a scope-route modifier — strategic composition produces Class 3 composites even from Class 1 sub-agents.
- **`#result-adversarial-tempo-advantage`**: add a scope caveat that the superlinear tempo advantage assumes $B$'s correction machinery is oriented toward the true environment; when $B$ is strategic (orients toward anticipating $A$), the tempo scaling may differ. This is a candidate follow-on spike.

### 10.3 What NOT to promote yet

- The mechanism-design connection (§6). The hypothesis that (C-i) and mechanism design are test/construction duals is attractive but needs a concrete derivation for a specific AAD-relevant setting (e.g., VCG over a network of AAD agents). Retain as spike content.
- The composite-class-inheritance refinement (§8). The proposal to lift Class 1/2/3 to composite-level classification is structurally sound but needs cross-checks against the existing `#hyp-directed-separation-under-composition` segment. Retain as spike content; cross-reference in a single Working Note on `#der-directed-separation`.
- The effects-spiral eigenvalue condition (§7.3). The formal statement is sketched but not derived for specific AAD agents. Worth a follow-on spike.

### 10.4 A candidate meta-pattern

Strategic composition fits all three of AAD's meta-patterns:

- **`#disc-separability-pattern`**: sub-scope $\alpha'$ (potential/monotone) is separable-core; sub-scope $\beta'$ (VI / regret-minimization) is structured-repair; non-convergent strategic interaction is general-open. This is the seventh ladder candidate.
- **`#disc-identifiability-floor`**: mechanism-design impossibility is a candidate fourth instance; cyclic games (no equilibrium) are a candidate fifth instance (structural limit on convergence derived from combinatorial game theory, e.g., Shapley 1964 on fictitious-play non-convergence in 3x3 non-zero-sum).
- **`#additive-coordinate-forcing`**: the potential function $\Phi$ plays the role of an additive coordinate at the *strategic* layer — unilateral payoff improvements are additive in $\Phi$. Whether this is a genuine instance of the Cauchy-FE forcing (axiom-motivated) or an adjacent family member (coordinate-matched, like Lyapunov quadratic) is a follow-up question. Preferred provisional classification: adjacent family member — the additivity of $\Phi$ is a *definitional consequence* of being a potential game, not forced by a Cauchy-FE argument on an AAD-internally-motivated additivity axiom.

---

## 11. Summary

Strategic composition — composition of agents with partially-opposing objectives — is structurally distinct from contraction-to-shared-truth composition. The correct primitive is **equilibrium existence + stability** (fixed-point convergence), not Lyapunov contraction on a shared state.

Three regimes:

- **Potential games** (Monderer-Shapley 1996): A2'-analog derived on $\nabla\Phi$; sector-persistence template transfers with joint-gradient state variable; equilibrium existence via potential-function compactness; convergence via best-response monotonicity. This is sub-scope $\alpha'$ — the separable core.
- **Monotone games** (Rosen 1965): A2'-analog in weighted-norm form; unique equilibrium; exponential convergence under diagonal strict concavity. Also sub-scope $\alpha'$, with slightly weaker Lyapunov machinery.
- **Non-potential non-monotone games**: Variational-inequality existence (Facchinei-Pang 2003); regret-minimization convergence to coarse correlated equilibrium only (Hart-Mas-Colell 2000). Sub-scope $\beta'$ — the structured repair; the sector-persistence template does not apply.

The scalar zero-sum example (§5) is a worked instance: two agents with maximally opposing objectives, but a potential function exists, the sector-persistence template transfers with $\xi = $ deviation-from-Nash, and the equilibrium at the strategy-space boundary is the composite fixed point.

**Relation to existing machinery:**
- Sibling to `#der-adversarial-destabilization` (asymmetric adversarial → this spike is symmetric).
- Generalization of `#der-team-persistence` (cooperative limit) and `#deriv-critical-mass-composition` (symmetric-matched-Tier-1 with shared target).
- Formal home for `#der-adversarial-destabilization`'s effects spiral (joint-Jacobian eigenvalue condition).
- Class 3 composite case — composite-level directed-separation failure from across-agent coupling, even with Class 1 sub-agents.

**Recommendation:** promote to a new Section III segment `#deriv-strategic-composition` with sub-scope $\alpha'$ (derived under potential/monotone-game conditions) and explicit sub-scope $\beta'$ scope exit (regret-minimization CCE support only); add (C-iv) route to `#scope-composite-agent`; flag seventh-ladder candidate for `#disc-separability-pattern` and fourth-instance candidate for `#disc-identifiability-floor` (mechanism-design impossibility).

---

## 12. Epistemic Assessment

*[Status — overall]*

- **Framing move** (contraction → equilibrium): *robust qualitative*. The claim that strategic composition requires fixed-point theory rather than Lyapunov contraction is standard in game theory; the AAD contribution is the recognition that the sector-persistence template transfers under specific conditions (potential-game / monotone-game) and does not transfer otherwise.
- **Potential-game A2'-analog**: *exact* under Monderer-Shapley 1996 + B1 directional fidelity. The derivation is a routine transcription of their result into AAD notation.
- **Monotone-game A2'-analog (weighted norm)**: *exact* under Rosen 1965's diagonal strict concavity. Again a transcription; the contribution is recognizing the natural inner product.
- **Sub-scope $\alpha'/\beta'$ partition**: *derived* (parallel to `#deriv-sector-condition`'s $\alpha/\beta$).
- **Zero-sum scalar worked example** (§5): *exact* for the stated case.
- **Mechanism-design connection** (§6): *hypothesis*. The duality with (C-i) scope route is attractive but needs a concrete worked example to rise above sketch.
- **Composite-class-inheritance refinement** (§8): *sketch*. Needs checking against `#hyp-directed-separation-under-composition`.
- **Effects-spiral eigenvalue condition** (§7.3): *sketch*. Formal statement is clean; derivation for specific AAD agents is open.
- **Seventh-ladder and fourth-instance meta-pattern claims** (§10.4): *hypothesis*. Worth flagging but not promoting.

**Max attainable**: *derived* for the core framing and the sub-scope partition; *exact* for the potential-game and monotone-game A2'-analogs; *conditional* for the full strategic-composition segment that would land as the primary deliverable.

**Honest weakest link.** The VI / regret-minimization machinery in sub-scope $\beta'$ gives only set-convergence to CCE, not trajectory-level or per-agent results. Under sub-scope $\beta'$, AAD's predictive power on the composite dynamics is substantially weaker than under sub-scope $\alpha'$. This is not a defect of the framing — it is an honest scope limit shared with game theory as a whole. The spike's recommendation is to land the segment under sub-scope $\alpha'$ primarily, with $\beta'$ clearly marked as structured-repair.

---

## Working Notes

- **Nash vs correlated equilibrium as the working equilibrium concept.** Nash is cleaner but requires existence (not always; RPS in pure strategies). Correlated equilibrium always exists for finite games (Aumann 1974 existence theorem) and has simpler convergence properties (Hart-Mas-Colell 2000 via regret). The spike uses Nash for the sub-scope $\alpha'$ results (where it exists and is unique) and CCE for sub-scope $\beta'$ (where only regret-minimization guarantees are available). This matches the standard game-theoretic hierarchy.
- **Is the strategic composite a "real" composite?** Depends on definition. Mechanically: yes — there is a joint state, joint dynamics, and (under sub-scope $\alpha'$) a joint stability property. Teleologically: ambiguous — there is no shared $O_c$, hence no shared purposeful substate $G_c$. The spike's position is that strategic composites are *real but of a different type* — the composite does not have a single $G_c$ but has a *joint dynamics* characterizable by equilibrium analysis. This preserves composition-consistency (the composite's predictions at different levels are compatible via the equilibrium structure) without requiring shared purpose.
- **Connection to online learning / multi-agent RL.** The regret-minimization machinery in sub-scope $\beta'$ is essentially the multi-agent reinforcement learning (MARL) literature's approach. Convergence of self-play to CCE is a central MARL result. Strategic-composition under AAD machinery is a natural home for a bridge to MARL; a follow-on spike could formalize the map.
- **Evolutionary dynamics as a separate regime.** Replicator dynamics (evolutionary game theory) is another dynamic for strategic interaction, different from best-response. It converges to ESS (evolutionarily stable strategies) which are a subset of Nash equilibria. Under what AAD-native update rules does the induced strategic dynamic match replicator? Multi-armed bandit with logit choice (softmax) approximates replicator; gradient-descent on the log-likelihood of a mixed strategy is replicator exactly. Worth a follow-on spike on AAD $\to$ evolutionary dynamics correspondence.
- **The information-theoretic structure of strategic composition.** Each agent's $M_t^{(i)}$ includes a model of agent $j$'s $M_t^{(j)}$, which includes a model of agent $i$'s $M_t^{(i)}$, and so on — an infinite regress of "I know that you know that I know." Classical game theory cuts this regress via common knowledge; AAD's machinery cuts it via `#scope-agent-identity` (token-level commitment, no type-level claims) and `#disc-identifiability-floor` (structural limits on mutual modelling). The regress itself is an identifiability-floor candidate: under what conditions can two AAD agents have consistent mutual models? This is a connection worth flagging, not formalizing here.
- **Dark-room / preferences-as-priors connection.** The `#def-satisfaction-gap` segment notes Sun-Firestone 2020's dark-room argument — that preferences as priors collapse under mutual prediction. Strategic composition is the formal home for one aspect of that critique: two agents both predicting each other's behaviour reduce to a fixed-point problem, not to a Lyapunov descent. The active-inference framing's attempt to unify goal-seeking and prediction fails here in a derivable way: the fixed point is not at the prediction-optimum, it is at the equilibrium of the strategic interaction, which is structurally different. This strengthens the `#def-satisfaction-gap` segment's positioning.
- **Refs to acquire if deepening this spike.** Monderer-Shapley 1996 (potential games); Rosen 1965 (concave games; almost certainly in the economics / operations research literature and likely obtainable); Facchinei-Pang 2003 (VI book); Hart-Mas-Colell 2000 (regret / correlated equilibrium); Sandholm 2010 (*Population Games and Evolutionary Dynamics*, MIT Press — comprehensive treatment of dynamics); Fudenberg-Tirole 1991 (*Game Theory* — the standard reference); Nash 1950 (existence), Aumann 1974 (correlated equilibrium), Foster-Vohra 1997 (calibrated play), Freund-Schapire 1997 (Hedge algorithm). The citations in this spike are placeholders for these references; before segment-level promotion, a PDF-level verification pass (per Joseph's citation-audit posture) would confirm the exact theorem attributions.
- **One thing this spike does not do.** It does not cover **mean-field games** (Lasry-Lions 2007, Huang-Malhamé-Caines 2006) — the $N \to \infty$ limit of strategic interaction, where each agent interacts with a *distribution* rather than named others. This is the natural extension for large strategic composites (markets, populations) and is a follow-on spike topic. The mean-field limit has its own A2'-analog (monotonicity of the mean-field operator) and its own sector-persistence template transfer, but it requires the population scope condition of Section III that is currently marked GAP.
