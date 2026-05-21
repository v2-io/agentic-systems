# Strategy Structure and the Diagnostic Split


## Derived: Chain Confidence Decay

- **Slug**: `der-chain-confidence-decay`
- **Type**: derived
- **Status**: exact
- **Stage**: claims-verified
- **Depends**: `def-strategy-dimension`

Confidence in a multi-step strategy decays monotonically with depth. The rate depends on the conditional dependence structure, but the qualitative result — longer chains are less confident than shorter ones — is robust.

*[Derived (chain-confidence-decay, mathematical identity)]*

For a chain of $n$ uncertain steps with conditional success probabilities:

$$\log P(\text{chain}) = \sum_{i=1}^{n} \log P(E_i \mid E_{\lt i})$$

Since each $\log P(E_i \mid E_{\lt i}) \leq 0$, chain confidence decays monotonically with depth.

**The independent case** ($p^n$) is the simplest special case, not the general result. When steps are conditionally dependent — success at step $k$ makes step $k+1$ more likely — the decay is slower. When steps have negative dependence (success at $k$ makes $k+1$ harder — resource depletion, adversary adaptation), decay is faster.

**Quantitative illustration** (independent, uniform $p$):

| Depth | $p = 0.9$ | $p = 0.8$ |
|-------|-----------|-----------|
| 1 | 0.90 | 0.80 |
| 3 | 0.73 | 0.51 |
| 5 | 0.59 | 0.33 |
| 10 | 0.35 | 0.11 |
| 20 | 0.12 | 0.01 |

---



## Scope: AND/OR Combination Scope

- **Slug**: `scope-and-or`
- **Type**: scope
- **Status**: robust-qualitative
- **Stage**: draft
- **Depends**: `def-strategy-dimension`, `der-chain-confidence-decay`

We restrict to environments where the causal combination of strategy steps is approximately conjunctive (AND: all parents required) or disjunctive (OR: any parent sufficient), without strong interaction effects between parents.

*[Scope Narrowing (and-or-scope)]*

Under this restriction, strategy nodes combine parent contributions via:

**AND-node** (all parents must succeed):

$$P(v \mid \text{parents}) = \prod_{i \in \text{pa}(v)} p_{iv} \cdot P(i)$$

**OR-node** (any parent sufficient):

$$P(v \mid \text{parents}) = 1 - \prod_{i \in \text{pa}(v)} (1 - p_{iv} \cdot P(i))$$

The combination type $\gamma(v) \in \{\text{AND}, \text{OR}\}$ is assigned per node. The causal question determines assignment: "if I remove one parent, can $v$ still be achieved?" YES → OR. NO → AND.

---



## Definition: Strategy DAG

- **Slug**: `def-strategy-dag`
- **Type**: definition
- **Status**: conditional
- **Stage**: draft
- **Depends**: `scope-and-or`, `post-causal-structure`, `def-pearl-causal-hierarchy`, `form-objective-functional`, `def-strategy-dimension`

The strategy $\Sigma_t$ is a directed acyclic graph with probabilistic edges and AND/OR combination semantics. Each edge carries the agent's causal credence that completing the parent step advances the child step. The graph encodes the agent's theory of how its actions produce progress toward its objectives.

**Why a DAG.** The DAG structure is not a modeling convenience but a *consequence* of operational requirements on any causally-reasoning bounded agent — at the level of sufficiency, not yet necessity. #deriv-graph-structure-uniqueness proves that directed temporal order plus probabilistic uncertainty plus causal sufficiency *suffice* for a DAG-with-Markov-factorization representation (the necessity direction — no non-DAG structure could satisfy these postulates — is an open stronger result). Acyclicity is proved from temporal ordering over a finite horizon. What remains a formulation choice is the *parameterization within* the DAG structure: AND/OR combination with single-parameter edges is the AAT choice, motivated by parsimony and convergence across three independent formalism attempts, but alternative parameterizations (within the derived graphical structure) are legitimate research directions.

**Strategy-layer exactness contract.** All formal results in AAT's strategy layer — the sector condition transfer ( #deriv-edge-credence-dynamics, Prop B.5), the persistence schema ( #schema-strategy-persistence), the gradient-based credit assignment ( #disc-credit-assignment-boundary) — are proved under **L0 (independence)**: causally sufficient DAGs with independent edge outcomes. **L0 formal results transfer exactly to correctly constructed L1 DAGs (strict prerequisites, Prop B.6) and L1' DAGs (soft facilitators, Prop B.7) — provided the common cause is observable per trial.** When the common cause is unobservable, the per-conditional decomposition is *fundamentally* (not merely "openly") obstructed — the mixture parameters are non-identifiable from a single observation channel (Fisher rank deficiency / Cramér-Rao floor; see B.7 §"Refuted Under Unobservable $C$"), and the agent must either collect direct $C$-observations, run multi-child joint observations (Prop B.7 §"Repair routes"), or fall back to plan-level (L0-on-marginals) tracking. See the Correlation Hierarchy below for the full treatment.

*[Definition (strategy-dag)]*

$$\Sigma_t = (V_t, E_t, p_t, \gamma_t)$$

where:
- $V_t$: set of **propositional nodes** — each node represents a condition that could be true or false (including action-success propositions at the leaves)
- $E_t \subseteq V_t \times V_t$: directed causal edges
- $p_t : E_t \to [0,1]$: **causal credence** per edge — the agent's confidence that completing the parent advances the child
- $\gamma_t : V_t \to \{\text{AND}, \text{OR}\}$: combination rule per node ( #scope-and-or)

**Structural constraints:**

1. **Acyclicity.** $\Sigma_t$ is a DAG. This is *derived*, not assumed — see below.
2. **Rootedness.** Every node has a directed path to a unique root terminal $v_\text{root}$ — the single sink node (out-degree 0) of $\Sigma_t$. Compound objectives express their combination structure through the AND/OR machinery below $v_\text{root}$, consistent with scalar $V_{O_t}$ ( #form-objective-functional).
3. **Source constraint.** Leaf nodes are propositions about action success ("action $a$ succeeds at $\tau_v$") or observable conditions ("condition $C_v$ holds at $\tau_v$"). Both are propositional — the distinction is whether the proposition is within the agent's causal control (action) or not (condition).

**Leaf base credence.** For each leaf node $v \in V_t^{\text{leaf}}$, the base credence used in status propagation:

$$p_v(M_t) = \begin{cases} \Pr(\text{action } v \text{ succeeds at } \tau_v \mid M_t) & \text{if } v \text{ is an action node} \\[4pt] \Pr(C_v(\tau_v) \mid M_t) & \text{if } v \text{ is a condition node} \end{cases}$$

where $C_v$ is the propositional condition associated with node $v$ and $\tau_v$ is the node's temporal position (from the acyclicity structure). For action leaves, $p_v$ is *capability credence* — "can I execute this?" For condition leaves, $p_v$ is *state credence* — "will this hold?" Both are conditional on $M_t$ and update whenever $M_t$ updates. This is the mechanism by which Section I's adaptive machinery enters the strategy: $M_t$ changes → leaf credences change → status propagation produces new terminal credences.

**Edge semantics.** Each edge carries a single credence weight:

$$p_{ij} = \text{Cr}(j \text{ advances} \mid i \text{ completed},\, M_t)$$

This is the agent's credence that completing step $i$ advances step $j$, given its current model --- its **causal efficacy estimate** for the link. The agent treats $p_{ij}$ as a causal quantity for planning purposes (status propagation, strategy-plan-confidence scoring, action selection). Whether $p_{ij}$ is a *good* estimate of causal efficacy depends on the identification regime of the data that produced it ( #scope-edge-update-causal-validity):

- **Regime A** (intervention-rich: software, laboratory science). The agent's execution-observation pairs are genuine interventions with clean attribution. $p_{ij}$ approximates the interventional probability $P(j \mid do(i), M_t)$.
- **Regime B** (partial intervention: organizational, coordinated action). The agent acts but attribution is blurred by concurrent actions and self-selection. $p_{ij}$ is a partially identified causal estimate, typically biased upward.
- **Regime C** (observation-only: passive monitoring, intelligence analysis). The agent observes associations but does not intervene. $p_{ij}$ is an observational proxy for the causal quantity --- useful for planning but potentially confounded.

The identifiability coefficient $\iota_{ij}$ ( #scope-edge-update-causal-validity) quantifies the strength of the causal interpretation for each edge. When $\iota_{ij} \approx 1$, the agent's credence is well-identified causally. When $\iota_{ij} \approx 0$, the credence is associational. The single-parameter edge design is preserved: $p_{ij}$ is always the agent's working estimate, with $\iota_{ij}$ characterizing its causal warrant separately.

**Status propagation.** Forward pass in topological order, $O(\lvert V \rvert + \lvert E \rvert)$:

$$s_v = \begin{cases} p_v & \text{if } v \text{ is a leaf (base credence)} \\ \prod_{i \in \text{pa}(v)} p_{iv} \cdot s_i & \text{if } \gamma(v) = \text{AND} \\ 1 - \prod_{i \in \text{pa}(v)} (1 - p_{iv} \cdot s_i) & \text{if } \gamma(v) = \text{OR} \end{cases}$$

**Terminal satisfaction conditions.** The root terminal $v_\text{root}$ and any intermediate nodes near the top of the DAG carry **satisfaction conditions**: predicates on environment states/trajectories that the agent treats as operational success criteria for the objective. These conditions operationalize $O_t$ within $\Sigma_t$ — they are the agent's theory of what it means to satisfy the objective. $O_t$ itself lives outside $\Sigma_t$ ( #def-strategy-dimension); the terminal conditions are $\Sigma_t$'s internal encoding of what $O_t$ requires. When $O_t$ changes, terminal conditions must be reassessed and potentially replaced ( #form-structural-change-as-parametric-limit).

**Well-formedness.** $\Sigma_t$ is **$O_t$-well-formed** when the agent believes that achieving the terminal conditions yields a trajectory that satisfies the objective:

$$\Pr\!\left(O_t \text{ satisfied by } \tau \;\middle\vert\; \text{terminal conditions achieved},\; M_t\right) \geq 1 - \epsilon$$

where "$O_t$ satisfied" means $V_{O_t}(\tau)$ exceeds the objective's own satisfaction criterion (formalized as $V_{O_t}^{\min}$ in #def-satisfaction-gap). This is a constraint on the relationship between $\Sigma_t$ and $O_t$, not a separate state object. It is explicit and in-principle assessable, though evaluating it requires the same value-side machinery as $A_O$ — it is not a cheap structural test. Violation triggers terminal reassessment: either the terminals need revision (they don't operationalize $O_t$ correctly) or $O_t$ itself needs revision.

**Strategy self-assessment.** The root node's propagated status:

$$\hat{P}_\Sigma(M_t) = s_{v_\text{root}}$$

is the strategy's **strategy-plan-confidence score** — the DAG's own answer to "will this plan work?" This score is a correct probability only when the DAG is **causally sufficient** — when all common causes of strategy nodes are represented as nodes in the graph ( #deriv-graph-structure-uniqueness, Step 3). When the DAG is causally insufficient (the dominant real-world case — shared infrastructure, common-mode risks, correlated adversary actions introduce latent common causes), $\hat P_\Sigma$ systematically overestimates success likelihood because the AND/OR propagation treats joint failure probability as the product of marginals. See the **Correlation Hierarchy** below for the full treatment.

$\hat P_\Sigma$ is explicitly distinct from $A_O$ ( #def-satisfaction-gap), which optimizes over the entire policy class, and from $V_O(\pi_\text{current})$ ( #def-value-object), which evaluates the current policy. $\hat P_\Sigma$ is cheap to compute ($O(\lvert V\rvert + \lvert E\rvert)$ forward pass) and updates in real time as $M_t$ changes through leaf credences.

### Correlation Hierarchy

*[Discussion (correlation-hierarchy)]*

The AND/OR status propagation computes correct probabilities **if and only if** the strategy DAG is causally sufficient — that is, all common causes of any two strategy nodes are themselves represented as nodes. By the Causal Markov Condition theorem ( #deriv-graph-structure-uniqueness, Step 3), causal sufficiency guarantees independent exogenous noise, which guarantees the Markov factorization, which guarantees independent edge outcomes. **When causal sufficiency fails — the dominant case in complex, multi-stakeholder, or adversarial environments — edge outcomes are correlated and the independence model is biased.**

**Direction and magnitude of bias.** For two binary sibling nodes $X_1, X_2$ with marginal success probabilities $\theta_1, \theta_2$ and covariance $\rho = \text{Cov}(X_1, X_2) \gt 0$ (positive correlation from a latent common cause):

| Node type | True probability | Independence estimate | Bias |
|---|---|---|---|
| **AND** | $\theta_1\theta_2 + \rho$ | $\theta_1\theta_2$ | $+\rho$ (underestimates — conservative) |
| **OR** | $[1-(1-\theta_1)(1-\theta_2)] - \rho$ | $1-(1-\theta_1)(1-\theta_2)$ | $-\rho$ (overestimates — optimistic) |

The independence model error is exactly $\pm\text{Cov}(X_1, X_2)$, with sign determined by node type. AND-nodes are conservative because clustering of successes helps joint success. OR-nodes are optimistic because clustering of failures undermines the redundancy that OR-structure is supposed to provide. Same magnitude, opposite signs.

For strategies with OR-structure near the root (the typical case — multiple alternative paths to the objective), the net bias is overestimation: the agent believes it has more redundancy than it actually does. For AND-heavy strategies (all components must work, no alternatives), the net bias is underestimation. Mixed strategies depend on the graph topology, but OR-dominated roots are far more common than AND-dominated roots in practice.

Four regimes, in order of increasing realism:

| Level | Model | When correct | $\hat P_\Sigma$ status | Sector transfer status | Computation |
|---|---|---|---|---|---|
| **L0: Independence** | AND/OR propagation as-is | Causally sufficient DAG (all common causes explicit) | Correct probability | Prop B.5 (linear), B.5b (componentwise nonlinear): $\alpha_s = \alpha_c$ | $O(\lvert V\rvert + \lvert E\rvert)$ |
| **L1: Augmented DAG (strict prerequisites)** | Strict-prerequisite common-cause nodes added explicitly; AND/OR propagation on augmented graph | Augmented DAG is causally sufficient *and* every modeled common cause has $\theta_{\text{child}\mid\neg C} \approx 0$ | Correct for augmented graph | Prop B.6: $\alpha_\Sigma = \min(1/(n_C+1), \theta_C\pi_j/(n_j+1))$ — three-way gating | $O(\lvert V'\rvert + \lvert E'\rvert)$, larger graph |
| **L1': Mixture form (soft facilitators)** | Conditional sub-DAGs weighted by common-cause state: $\hat P_\Sigma = \theta_C P_\Sigma(G\mid C) + (1-\theta_C) P_\Sigma(G\mid\neg C)$ | Soft-facilitator common causes ($\theta_{\text{child}\mid\neg C} \gt 0$) **with $C$ observable per trial** | Correct for the weighted combination | Prop B.7: $\alpha_{L1'} = \min(1/(n_C+1), \theta_C\pi_{j\mid C}/(n_{j\mid C}+1), (1-\theta_C)\pi_{j\mid\neg C}/(n_{j\mid\neg C}+1))$ — five-way gating. **Refuted when $C$ unobservable** (Fisher rank-1; falls back to plan-level tracking or multi-child joint observation) | $O(\lvert V'\rvert + \lvert E'\rvert)$ per common cause; doubles parametric footprint for affected edges |
| **L2: Full correlation** | Arbitrary joint failure distribution over edges | Always (but requires specifying the full joint) | Correct | Reduces to L0 on the augmented joint state | Exponential in general |

**L0 (Independence)** is the tractable baseline. All formal results in AAT's strategy layer — the sector condition transfer (Prop B.5 in #deriv-edge-credence-dynamics), the persistence schema ( #schema-strategy-persistence), the gradient-based credit assignment ( #disc-credit-assignment-boundary) — are proved under L0. The strategy-plan-confidence error $\delta_s = \hat P_\Sigma - \Phi$ tracks calibration *within* the independence model; $\Phi = P_\Sigma(\boldsymbol\theta)$ is the AND/OR formula at true edge rates, not actual plan success probability.

**L1 (Augmented DAG)** is the practical sweet spot — *for strict-prerequisite common causes*. The agent models correlation structure explicitly by adding common-cause nodes to $\Sigma_t$ and restructuring the DAG so that the common cause is **factored above the correlation it creates**. The construction principle: place the common-cause node as an AND-prerequisite *above* the OR/AND structure whose children it correlates. This ensures that, conditional on the common cause being satisfied, the children are independent and standard AND/OR propagation is correct.

**Scope of the AND-prerequisite construction: strict prerequisites only.** The factoring-above principle requires that the common cause be a *strict* prerequisite — one for which $\theta_{\text{child} \mid \neg C} \approx 0$. Shared infrastructure going down, a required resource being absent, a gating permission being denied: in all of these, the correlated children fail when the common cause fails, so the AND-prerequisite correctly encodes the correlation. When the common cause is instead a *soft facilitator* — favorable market conditions, a supportive team culture, an enabling technology — children have $\theta_{\text{child} \mid \neg C} \gt 0$ and can succeed when the common cause is absent, just less reliably. The AND-prerequisite construction mathematically forces $P(\text{sub-plan} \mid \neg C) = 0$, which strictly understates success probability when $C$ is absent. Soft facilitators therefore fall outside L1's single-pass construction and require one of:

- **Mixture form (L1'):** split the sub-plan into two conditional structures and weight by $P(C)$:
$$\hat P_\Sigma = \theta_C \cdot P_{\Sigma}(G \mid C) + (1 - \theta_C) \cdot P_{\Sigma}(G \mid \neg C)$$
This keeps propagation polynomial but requires maintaining two parallel sub-DAGs per soft-facilitator node. Per-edge credences split into two regimes ($p_{ij \mid C}$ and $p_{ij \mid \neg C}$), doubling the parametric footprint for affected edges.
- **Explicit conditioning (L2 subcase):** $P_\Sigma(G) = \sum_c P(C = c) \cdot P_\Sigma(G \mid C = c)$, summing over common-cause states. For $k$ soft facilitators with binary states, this costs $O(2^k)$ in the number of common-cause states — the exponential blowup L2 was defined to name.

**The gap between L1 (strict) and L2 (arbitrary) was not previously named.** L1' (mixture form) fills this gap at linear cost per soft-facilitator node. The "L1 is the practical default" claim therefore applies most cleanly to strict prerequisites; for mixed environments (strict and soft common causes simultaneously), the correct construction mixes L1 factoring for strict prerequisites with L1' mixtures for soft facilitators. Treating all common causes as strict prerequisites systematically undervalues sub-plans that face soft facilitators (the opposite failure mode from L0's overestimation).

*Example — strict prerequisite* (see #example-L1 for full treatment): Two OR-alternatives sharing infrastructure dependency ($\theta_C = 0.8$, $\theta_{1\mid C} = 0.9$, $\theta_{2\mid C} = 0.7$, and implicitly $\theta_{1\mid\neg C} = \theta_{2\mid\neg C} = 0$ — infrastructure is a strict prerequisite). L0 computes $\hat P_\Sigma = 0.877$; actual is $0.776$ (overestimation = $\rho$, the covariance from shared infrastructure). Naive L1 (common cause as parent of both alternatives, alternatives remain OR-siblings) gives the *same* overestimate because the OR-propagation still treats siblings as marginally independent. Correct L1 ($G = \text{AND}(C, G_{\text{sub}})$ where $G_{\text{sub}} = \text{OR}(A_1, A_2)$) gives the exact answer because $A_1$ and $A_2$ are conditionally independent given $C$ *and because $\theta_{i \mid \neg C} = 0$, so the AND-prerequisite is the correct encoding*. The sector condition is verified (Prop B.6 in #deriv-edge-credence-dynamics) with $\alpha_\Sigma = \min(1/(n_C+1),\;\theta_C(1-\varepsilon)/(n_{A_1}+1),\;\theta_C \varepsilon/(n_{A_2}+1))$ — combining evidence-starvation and exploration-gating effects. B.5b transfers losslessly.

All L0 formal results transfer to correctly constructed L1 DAGs *for strict-prerequisite common causes* because the augmented DAG is a standard AND/OR DAG that satisfies causal sufficiency. For L1' (mixture form) with **observable common cause**, the formal results transfer through Prop B.7 ( #deriv-edge-credence-dynamics) — five-way gating with $\alpha_{L1'} = \min(1/(n_C+1), \theta_C\pi_{j\mid C}/(n_{j\mid C}+1), (1-\theta_C)\pi_{j\mid\neg C}/(n_{j\mid\neg C}+1))$. For L1' with **unobservable common cause**, the per-conditional decomposition is identifiability-obstructed by the Cramér-Rao floor — the per-trial Fisher matrix is rank 1 rather than rank $2K+1$, so no unbiased online estimator on the joint conditional vector admits a sector parameter $\alpha \gt 0$. This is not "open" but structurally refuted; the agent must augment $C$-observability, run multi-child joint observations, or fall back to L0-on-marginals (losing per-conditional diagnostics). The practical challenges are: (1) identifying which common causes matter enough to model explicitly, (2) classifying each identified common cause as strict or soft, (3) verifying $C$-observability for soft cases, (4) restructuring the DAG correctly for each. All four are modeling judgments, not mechanical procedures.

**L2 (Full correlation)** is a mathematical ideal. Specifying the full joint failure distribution over $m$ edges requires $O(2^m)$ parameters, which violates the bounded-cognition constraint that motivates the DAG representation in the first place. L2 is useful as a reference point for characterizing the L0/L1 approximation error, not as a practical representation.

**Choosing among L1, L1', and L2 requires classifying each common cause and verifying observability.** $\theta_{\text{child}\mid\neg C} \approx 0$ → L1 (factor above the correlation, B.6). $\theta_{\text{child}\mid\neg C} \gt 0$ with **$C$ observable** → L1' (B.7, five-way gating). $\theta_{\text{child}\mid\neg C} \gt 0$ with $C$ unobservable → L1' is identifiability-obstructed by the Cramér-Rao floor; either augment $C$-observability (preferred), use L2 explicit conditioning, or fall back to L0-on-marginals (losing per-conditional diagnostics). Mixed-classification environments (some strict, some soft, varying observability) combine L1 factoring for the strict and L1' mixtures for the soft observable. Treating all common causes as strict prerequisites under L1 alone systematically *understates* success on soft-facilitator branches (the symmetric failure mode to L0's overestimation); treating L0 as the default leads to systematic overconfidence — the agent believes it has more redundancy than it actually does (OR-nodes) or more fragility than it actually does (AND-nodes). L0 remains appropriate for domains with genuinely independent risks (independent parallel experiments, diversified portfolios with low correlation) and as a computational stepping stone during strategy construction.

**Detecting latent common causes.** An agent at L0 can detect causal insufficiency *under joint sibling observability generated by its own interventions* — not from on-policy traces alone. On-policy execution alone cannot distinguish the with-and-without-latent-common-cause worlds (the no-go in #der-causal-insufficiency-detection); the unique broadly-available escape is joint sibling observability under exploration, where the agent's interventions ( #der-loop-interventional-access) generate the joint outcome data the test requires. Persistent overestimation of plan success after edge credences have converged is the *signal* of insufficiency ( #result-structural-adaptation-necessity applied to the strategy layer); pairwise covariance among observed siblings is the *test* (positive covariance rejects independence and identifies where to add L1 nodes). Full treatment: #der-causal-insufficiency-detection; numerical instantiation: #example-L1. Summary references in dependent segments that elide the on-policy / interventional distinction should be treated with caution — the load-bearing scope is "joint sibling observability under exploration," not "from observational data alone."

**Scope of the terminal construction.** Terminal conditions as Boolean predicates with AND/OR aggregation work naturally for threshold, constraint, and composite objectives. For continuous-valued objectives without natural thresholds, the agent must set an operational threshold — introducing a discretization that is a practical proxy, not a lossless encoding of $V_O$. The primary $O_t$ ↔ theory interface remains $V_O$ through the value object ( #def-value-object); terminal conditions are $\Sigma_t$'s internal operational encoding.

**Single-parameter edges.** Each edge carries one number ($p_{ij}$), not two. An earlier formalism attempt used $(p_{ij}, \theta_{ij})$ where $\theta$ was "contribution magnitude." This was dropped because the AND/OR combination rules at nodes absorb $\theta$'s role — the complexity budget goes to one bit per node ($\gamma$) instead of one float per edge.

**Edge-credence presentation coordinates.** Each edge's single-number credence has two equivalent presentations: the *probability-space* coordinate $p_{ij} \in [0, 1]$ (convenient for AND/OR propagation and interpretation) and the *log-odds* coordinate $\lambda_{ij} = \log(p_{ij}/(1 - p_{ij})) \in \mathbb{R}$ (the unique additive-evidence coordinate forced by the evidential-additivity axiom; see #deriv-edge-update-natural-parameter). The two coordinates are related by the sigmoid $p_{ij} = \sigma(\lambda_{ij})$. AAT's AND/OR status propagation and Correlation Hierarchy algebra operate in probability space; the continuous-gradient update machinery in #disc-credit-assignment-boundary operates natively in log-odds and projects back to $[0, 1]$ via sigmoid at the readout interface. Props B.1–B.7 of #deriv-edge-credence-dynamics are stated in moment-parameter (probability-space) form; their sector-parameter content is Fisher-equivalent in either coordinate.

### Acyclicity is Derived

*[Derived (from causal-structure + finite planning horizon)]*

Each node in $\Sigma_t$ represents a future event or state with temporal position $\tau_i \gt t$. An edge $X_i \to X_j$ requires $\tau_i \lt \tau_j$ ( #post-causal-structure: causes precede effects). A cycle $X_i \to X_j \to \cdots \to X_i$ would require $\tau_i \lt \tau_j \lt \cdots \lt \tau_i$, which is impossible for a real-valued time index.

Strategies involving iteration ("try A, if fail try B, if fail try A again") are acyclic when time-indexed. The sequence unfolds as:

$$A_1 \to \text{check}_1 \to B_1 \to \text{check}_2 \to A_2 \to \ldots$$

Each attempt is a distinct node at a distinct time. The apparent cycle is a linear chain in the unrolled view.

Formally: a finite set with a strict partial order (future events ordered by time) is representable as a DAG. This is a standard result in order theory.

**Scope of the acyclicity result.** This applies to $\Sigma_t$ (the agent's strategy over the future), not to $M_t$'s model of the environment, which may include cyclic causal processes (feedback loops in the physical world, market dynamics, ecosystem interactions). The acyclicity is specific to the purposeful substate.

---



## Definition: Satisfaction Gap

- **Slug**: `def-satisfaction-gap`
- **Type**: definition
- **Status**: exact
- **Stage**: draft
- **Depends**: `def-value-object`, `form-objective-functional`

The satisfaction gap measures the distance between what the objective requires and what the best available one-step policy improvement can deliver, under the current model and horizon. Under the canonical continuation convention ( #def-value-object), this is a *local* diagnostic — it answers "can I improve toward the goal from here?" not "is the goal globally feasible?" A multi-step recoverable objective may show positive $\delta_{\text{sat}}$ because continuation is frozen at $\pi_{\text{current}}$. Different continuation conventions yield different gap values; see Epistemic Status.

*[Definition (objective-attainability)]*

$$A_O(M_t;\, \Pi, N_h) = \sup_{\pi \in \Pi} V_O(M_t, \pi;\, N_h)$$

The **objective attainability** — the best achievable value given current beliefs $M_t$, available policy class $\Pi$, and horizon $N_h$.

*[Definition (satisfaction-gap)]*

$$\delta_{\text{sat}} = V_{O_t}^{\min} - A_O(M_t;\, \Pi, N_h)$$

where $V_{O_t}^{\min}$ is the minimum trajectory value that counts as "objective met" — a threshold set by the objective itself (for constraints: all satisfied; for utility: a minimum acceptable level).

- $\delta_{\text{sat}} \gt 0$: The objective is **unmet** under the best available policy, current model, and horizon.
- $\delta_{\text{sat}} \leq 0$: The objective is **attainable** in principle.

**Disambiguation.** $\delta_{\text{sat}} \gt 0$ does NOT automatically mean the goal is wrong. It means the goal is unmet given $(M_t, \Pi, N_h)$. The positive signal has multiple possible causes:

| Cause | Fix | How to distinguish |
|---|---|---|
| Goal is genuinely infeasible | Revise $O_t$ | Persists across $M_t$, $\Pi$, $N_h$ improvements |
| Policy class too narrow | Expand $\Pi$ (structural adaptation of $\Sigma_t$) | $\delta_{\text{sat}}$ decreases when richer policies are tried |
| Horizon too short | Extend $N_h$ | $\delta_{\text{sat}}$ decreases with longer planning horizon |
| Model is wrong about feasibility | Improve $M_t$ (reduce $\delta_{\text{epistemic}}$) | $\delta_{\text{sat}}$ changes when $M_t$ is corrected |
| Objectives jointly infeasible | Revise $O_t$ or relax constraints | Individual terminal satisfaction gaps are zero but AND-node fails; cross-terminal tradeoff is required |

Objective revision is the **last resort**, not the first response to unmet goals. The orient cascade ( #der-orient-cascade) formalizes this ordering.

---



## Definition: Control Regret

- **Slug**: `def-control-regret`
- **Type**: definition
- **Status**: exact
- **Stage**: draft
- **Depends**: `def-value-object`, `def-satisfaction-gap`

Control regret measures the gap between the best available one-step policy improvement and the agent's current policy, under the current model and horizon. Under the canonical continuation convention ( #def-value-object), this is a *local* diagnostic — it answers "could I do better right now?" not "is my overall strategy globally suboptimal?" A revisable policy may show low δ_regret simply because continuation is frozen. This is the signal for strategy revision, with the caveat that the signal's scope matches the continuation convention's scope.

*[Definition (control-regret)]*

$$\delta_{\text{regret}} = A_O(M_t;\, \Pi, N_h) - V_O(M_t, \pi_{\text{current}};\, N_h) \geq 0$$

Always non-negative: the current policy cannot outperform the best in its class.

- $\delta_{\text{regret}} \approx 0$: The agent is doing the best it can within current $(\Pi, N_h, M_t)$. If $\delta_{\text{sat}} \gt 0$ simultaneously, the problem is not the current strategy — it's either the goal, the capability ($\Pi$, $N_h$), or the model ($M_t$). See #def-satisfaction-gap's disambiguation.
- $\delta_{\text{regret}} \gg 0$: There's room for improvement without changing $O_t$. → Revise $\Sigma_t$.

---
