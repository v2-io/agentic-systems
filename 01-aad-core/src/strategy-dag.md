---
slug: strategy-dag
type: definition
status: conditional
depends:
  - and-or-scope
  - causal-structure
  - pearl-causal-hierarchy
  - objective-functional
  - strategy-dimension
stage: draft
---

# Definition: Strategy DAG

The strategy $\Sigma_t$ is a directed acyclic graph with probabilistic edges and AND/OR combination semantics. Each edge carries the agent's causal credence that completing the parent step advances the child step. The graph encodes the agent's theory of how its actions produce progress toward its objectives.

**Why a DAG.** The DAG structure is not a modeling convenience but a *consequence* of operational requirements on any causally-reasoning bounded agent — at the level of sufficiency, not yet necessity. #graph-structure-uniqueness proves that directed temporal order plus probabilistic uncertainty plus causal sufficiency *suffice* for a DAG-with-Markov-factorization representation (the necessity direction — no non-DAG structure could satisfy these postulates — is an open stronger result). Acyclicity is proved from temporal ordering over a finite horizon. What remains a formulation choice is the *parameterization within* the DAG structure: AND/OR combination with single-parameter edges is the AAD choice, motivated by parsimony and convergence across three independent formalism attempts, but alternative parameterizations (within the derived graphical structure) are legitimate research directions.

**Strategy-layer exactness contract.** All formal results in AAD's strategy layer — the sector condition transfer ( #strategic-dynamics-derivation, Prop B.5), the persistence schema ( #strategy-persistence-schema), the gradient-based credit assignment ( #credit-assignment-boundary) — are proved under **L0 (independence)**: causally sufficient DAGs with independent edge outcomes. **L0 formal results transfer exactly to correctly constructed L1 DAGs (strict prerequisites, Prop B.6) and L1' DAGs (soft facilitators, Prop B.7) — provided the common cause is observable per trial.** When the common cause is unobservable, the per-conditional decomposition is *fundamentally* (not merely "openly") obstructed — the mixture parameters are non-identifiable from a single observation channel (Fisher rank deficiency / Cramér-Rao floor; see B.7 §"Refuted Under Unobservable $C$"), and the agent must either collect direct $C$-observations, run multi-child joint observations (Prop B.7 §"Repair routes"), or fall back to plan-level (L0-on-marginals) tracking. See the Correlation Hierarchy below for the full treatment.

## Formal Expression

*[Definition (strategy-dag)]*

$$\Sigma_t = (V_t, E_t, p_t, \gamma_t)$$

where:
- $V_t$: set of **propositional nodes** — each node represents a condition that could be true or false (including action-success propositions at the leaves)
- $E_t \subseteq V_t \times V_t$: directed causal edges
- $p_t : E_t \to [0,1]$: **causal credence** per edge — the agent's confidence that completing the parent advances the child
- $\gamma_t : V_t \to \{\text{AND}, \text{OR}\}$: combination rule per node ( #and-or-scope)

**Structural constraints:**

1. **Acyclicity.** $\Sigma_t$ is a DAG. This is *derived*, not assumed — see below.
2. **Rootedness.** Every node has a directed path to a unique root terminal $v_\text{root}$ — the single sink node (out-degree 0) of $\Sigma_t$. Compound objectives express their combination structure through the AND/OR machinery below $v_\text{root}$, consistent with scalar $V_{O_t}$ ( #objective-functional).
3. **Source constraint.** Leaf nodes are propositions about action success ("action $a$ succeeds at $\tau_v$") or observable conditions ("condition $C_v$ holds at $\tau_v$"). Both are propositional — the distinction is whether the proposition is within the agent's causal control (action) or not (condition).

**Leaf base credence.** For each leaf node $v \in V_t^{\text{leaf}}$, the base credence used in status propagation:

$$p_v(M_t) = \begin{cases} \Pr(\text{action } v \text{ succeeds at } \tau_v \mid M_t) & \text{if } v \text{ is an action node} \\[4pt] \Pr(C_v(\tau_v) \mid M_t) & \text{if } v \text{ is a condition node} \end{cases}$$

where $C_v$ is the propositional condition associated with node $v$ and $\tau_v$ is the node's temporal position (from the acyclicity structure). For action leaves, $p_v$ is *capability credence* — "can I execute this?" For condition leaves, $p_v$ is *state credence* — "will this hold?" Both are conditional on $M_t$ and update whenever $M_t$ updates. This is the mechanism by which Section I's adaptive machinery enters the strategy: $M_t$ changes → leaf credences change → status propagation produces new terminal credences.

**Edge semantics.** Each edge carries a single credence weight:

$$p_{ij} = \text{Cr}(j \text{ advances} \mid i \text{ completed},\, M_t)$$

This is the agent's credence that completing step $i$ advances step $j$, given its current model --- its **causal efficacy estimate** for the link. The agent treats $p_{ij}$ as a causal quantity for planning purposes (status propagation, plan-confidence scoring, action selection). Whether $p_{ij}$ is a *good* estimate of causal efficacy depends on the identification regime of the data that produced it ( #edge-update-causal-validity):

- **Regime A** (intervention-rich: software, laboratory science). The agent's execution-observation pairs are genuine interventions with clean attribution. $p_{ij}$ approximates the interventional probability $P(j \mid do(i), M_t)$.
- **Regime B** (partial intervention: organizational, coordinated action). The agent acts but attribution is blurred by concurrent actions and self-selection. $p_{ij}$ is a partially identified causal estimate, typically biased upward.
- **Regime C** (observation-only: passive monitoring, intelligence analysis). The agent observes associations but does not intervene. $p_{ij}$ is an observational proxy for the causal quantity --- useful for planning but potentially confounded.

The identifiability coefficient $\iota_{ij}$ ( #edge-update-causal-validity) quantifies the strength of the causal interpretation for each edge. When $\iota_{ij} \approx 1$, the agent's credence is well-identified causally. When $\iota_{ij} \approx 0$, the credence is associational. The single-parameter edge design is preserved: $p_{ij}$ is always the agent's working estimate, with $\iota_{ij}$ characterizing its causal warrant separately.

**Status propagation.** Forward pass in topological order, $O(\lvert V \rvert + \lvert E \rvert)$:

$$s_v = \begin{cases} p_v & \text{if } v \text{ is a leaf (base credence)} \\ \prod_{i \in \text{pa}(v)} p_{iv} \cdot s_i & \text{if } \gamma(v) = \text{AND} \\ 1 - \prod_{i \in \text{pa}(v)} (1 - p_{iv} \cdot s_i) & \text{if } \gamma(v) = \text{OR} \end{cases}$$

**Terminal satisfaction conditions.** The root terminal $v_\text{root}$ and any intermediate nodes near the top of the DAG carry **satisfaction conditions**: predicates on environment states/trajectories that the agent treats as operational success criteria for the objective. These conditions operationalize $O_t$ within $\Sigma_t$ — they are the agent's theory of what it means to satisfy the objective. $O_t$ itself lives outside $\Sigma_t$ ( #strategy-dimension); the terminal conditions are $\Sigma_t$'s internal encoding of what $O_t$ requires. When $O_t$ changes, terminal conditions must be reassessed and potentially replaced ( #structural-change-as-parametric-limit).

**Well-formedness.** $\Sigma_t$ is **$O_t$-well-formed** when the agent believes that achieving the terminal conditions yields a trajectory that satisfies the objective:

$$\Pr\!\left(O_t \text{ satisfied by } \tau \;\middle\vert\; \text{terminal conditions achieved},\; M_t\right) \geq 1 - \epsilon$$

where "$O_t$ satisfied" means $V_{O_t}(\tau)$ exceeds the objective's own satisfaction criterion (formalized as $V_{O_t}^{\min}$ in #satisfaction-gap). This is a constraint on the relationship between $\Sigma_t$ and $O_t$, not a separate state object. It is explicit and in-principle assessable, though evaluating it requires the same value-side machinery as $A_O$ — it is not a cheap structural test. Violation triggers terminal reassessment: either the terminals need revision (they don't operationalize $O_t$ correctly) or $O_t$ itself needs revision.

**Strategy self-assessment.** The root node's propagated status:

$$\hat{P}_\Sigma(M_t) = s_{v_\text{root}}$$

is the strategy's **plan-confidence score** — the DAG's own answer to "will this plan work?" This score is a correct probability only when the DAG is **causally sufficient** — when all common causes of strategy nodes are represented as nodes in the graph ( #graph-structure-uniqueness, Step 3). When the DAG is causally insufficient (the dominant real-world case — shared infrastructure, common-mode risks, correlated adversary actions introduce latent common causes), $\hat P_\Sigma$ systematically overestimates success likelihood because the AND/OR propagation treats joint failure probability as the product of marginals. See the **Correlation Hierarchy** below for the full treatment.

$\hat P_\Sigma$ is explicitly distinct from $A_O$ ( #satisfaction-gap), which optimizes over the entire policy class, and from $V_O(\pi_\text{current})$ ( #value-object), which evaluates the current policy. $\hat P_\Sigma$ is cheap to compute ($O(\lvert V\rvert + \lvert E\rvert)$ forward pass) and updates in real time as $M_t$ changes through leaf credences.

### Correlation Hierarchy

*[Discussion (correlation-hierarchy)]*

The AND/OR status propagation computes correct probabilities **if and only if** the strategy DAG is causally sufficient — that is, all common causes of any two strategy nodes are themselves represented as nodes. By the Causal Markov Condition theorem ( #graph-structure-uniqueness, Step 3), causal sufficiency guarantees independent exogenous noise, which guarantees the Markov factorization, which guarantees independent edge outcomes. **When causal sufficiency fails — the dominant case in complex, multi-stakeholder, or adversarial environments — edge outcomes are correlated and the independence model is biased.**

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

**L0 (Independence)** is the tractable baseline. All formal results in AAD's strategy layer — the sector condition transfer (Prop B.5 in #strategic-dynamics-derivation), the persistence schema ( #strategy-persistence-schema), the gradient-based credit assignment ( #credit-assignment-boundary) — are proved under L0. The plan-confidence error $\delta_s = \hat P_\Sigma - \Phi$ tracks calibration *within* the independence model; $\Phi = P_\Sigma(\boldsymbol\theta)$ is the AND/OR formula at true edge rates, not actual plan success probability.

**L1 (Augmented DAG)** is the practical sweet spot — *for strict-prerequisite common causes*. The agent models correlation structure explicitly by adding common-cause nodes to $\Sigma_t$ and restructuring the DAG so that the common cause is **factored above the correlation it creates**. The construction principle: place the common-cause node as an AND-prerequisite *above* the OR/AND structure whose children it correlates. This ensures that, conditional on the common cause being satisfied, the children are independent and standard AND/OR propagation is correct.

**Scope of the AND-prerequisite construction: strict prerequisites only.** The factoring-above principle requires that the common cause be a *strict* prerequisite — one for which $\theta_{\text{child} \mid \neg C} \approx 0$. Shared infrastructure going down, a required resource being absent, a gating permission being denied: in all of these, the correlated children fail when the common cause fails, so the AND-prerequisite correctly encodes the correlation. When the common cause is instead a *soft facilitator* — favorable market conditions, a supportive team culture, an enabling technology — children have $\theta_{\text{child} \mid \neg C} \gt 0$ and can succeed when the common cause is absent, just less reliably. The AND-prerequisite construction mathematically forces $P(\text{sub-plan} \mid \neg C) = 0$, which strictly understates success probability when $C$ is absent. Soft facilitators therefore fall outside L1's single-pass construction and require one of:

- **Mixture form (L1'):** split the sub-plan into two conditional structures and weight by $P(C)$:
$$\hat P_\Sigma = \theta_C \cdot P_{\Sigma}(G \mid C) + (1 - \theta_C) \cdot P_{\Sigma}(G \mid \neg C)$$
This keeps propagation polynomial but requires maintaining two parallel sub-DAGs per soft-facilitator node. Per-edge credences split into two regimes ($p_{ij \mid C}$ and $p_{ij \mid \neg C}$), doubling the parametric footprint for affected edges.
- **Explicit conditioning (L2 subcase):** $P_\Sigma(G) = \sum_c P(C = c) \cdot P_\Sigma(G \mid C = c)$, summing over common-cause states. For $k$ soft facilitators with binary states, this costs $O(2^k)$ in the number of common-cause states — the exponential blowup L2 was defined to name.

**The gap between L1 (strict) and L2 (arbitrary) was not previously named.** L1' (mixture form) fills this gap at linear cost per soft-facilitator node. The "L1 is the practical default" claim therefore applies most cleanly to strict prerequisites; for mixed environments (strict and soft common causes simultaneously), the correct construction mixes L1 factoring for strict prerequisites with L1' mixtures for soft facilitators. Treating all common causes as strict prerequisites systematically undervalues sub-plans that face soft facilitators (the opposite failure mode from L0's overestimation).

*Example — strict prerequisite* (see #worked-example-L1 for full treatment): Two OR-alternatives sharing infrastructure dependency ($\theta_C = 0.8$, $\theta_{1\mid C} = 0.9$, $\theta_{2\mid C} = 0.7$, and implicitly $\theta_{1\mid\neg C} = \theta_{2\mid\neg C} = 0$ — infrastructure is a strict prerequisite). L0 computes $\hat P_\Sigma = 0.877$; actual is $0.776$ (overestimation = $\rho$, the covariance from shared infrastructure). Naive L1 (common cause as parent of both alternatives, alternatives remain OR-siblings) gives the *same* overestimate because the OR-propagation still treats siblings as marginally independent. Correct L1 ($G = \text{AND}(C, G_{\text{sub}})$ where $G_{\text{sub}} = \text{OR}(A_1, A_2)$) gives the exact answer because $A_1$ and $A_2$ are conditionally independent given $C$ *and because $\theta_{i \mid \neg C} = 0$, so the AND-prerequisite is the correct encoding*. The sector condition is verified (Prop B.6 in #strategic-dynamics-derivation) with $\alpha_\Sigma = \min(1/(n_C+1),\;\theta_C(1-\varepsilon)/(n_{A_1}+1),\;\theta_C \varepsilon/(n_{A_2}+1))$ — combining evidence-starvation and exploration-gating effects. B.5b transfers losslessly.

All L0 formal results transfer to correctly constructed L1 DAGs *for strict-prerequisite common causes* because the augmented DAG is a standard AND/OR DAG that satisfies causal sufficiency. For L1' (mixture form) with **observable common cause**, the formal results transfer through Prop B.7 ( #strategic-dynamics-derivation) — five-way gating with $\alpha_{L1'} = \min(1/(n_C+1), \theta_C\pi_{j\mid C}/(n_{j\mid C}+1), (1-\theta_C)\pi_{j\mid\neg C}/(n_{j\mid\neg C}+1))$. For L1' with **unobservable common cause**, the per-conditional decomposition is identifiability-obstructed by the Cramér-Rao floor — the per-trial Fisher matrix is rank 1 rather than rank $2K+1$, so no unbiased online estimator on the joint conditional vector admits a sector parameter $\alpha \gt 0$. This is not "open" but structurally refuted; the agent must augment $C$-observability, run multi-child joint observations, or fall back to L0-on-marginals (losing per-conditional diagnostics). The practical challenges are: (1) identifying which common causes matter enough to model explicitly, (2) classifying each identified common cause as strict or soft, (3) verifying $C$-observability for soft cases, (4) restructuring the DAG correctly for each. All four are modeling judgments, not mechanical procedures.

**L2 (Full correlation)** is a mathematical ideal. Specifying the full joint failure distribution over $m$ edges requires $O(2^m)$ parameters, which violates the bounded-cognition constraint that motivates the DAG representation in the first place. L2 is useful as a reference point for characterizing the L0/L1 approximation error, not as a practical representation.

**Choosing among L1, L1', and L2 requires classifying each common cause and verifying observability.** $\theta_{\text{child}\mid\neg C} \approx 0$ → L1 (factor above the correlation, B.6). $\theta_{\text{child}\mid\neg C} \gt 0$ with **$C$ observable** → L1' (B.7, five-way gating). $\theta_{\text{child}\mid\neg C} \gt 0$ with $C$ unobservable → L1' is identifiability-obstructed by the Cramér-Rao floor; either augment $C$-observability (preferred), use L2 explicit conditioning, or fall back to L0-on-marginals (losing per-conditional diagnostics). Mixed-classification environments (some strict, some soft, varying observability) combine L1 factoring for the strict and L1' mixtures for the soft observable. Treating all common causes as strict prerequisites under L1 alone systematically *understates* success on soft-facilitator branches (the symmetric failure mode to L0's overestimation); treating L0 as the default leads to systematic overconfidence — the agent believes it has more redundancy than it actually does (OR-nodes) or more fragility than it actually does (AND-nodes). L0 remains appropriate for domains with genuinely independent risks (independent parallel experiments, diversified portfolios with low correlation) and as a computational stepping stone during strategy construction.

**Detecting latent common causes.** An agent at L0 can detect causal insufficiency from its own data: persistent overestimation of plan success after edge credences have converged is the signal ( #structural-adaptation-necessity applied to the strategy layer). The agent can localize the common cause by testing for pairwise covariance among sibling edges — positive covariance rejects the independence hypothesis and identifies where to add L1 nodes. The agent's interventions ( #loop-interventional-access) generate the joint outcome data needed for the test. Full treatment: #causal-insufficiency-detection; numerical instantiation: #worked-example-L1.

**Scope of the terminal construction.** Terminal conditions as Boolean predicates with AND/OR aggregation work naturally for threshold, constraint, and composite objectives. For continuous-valued objectives without natural thresholds, the agent must set an operational threshold — introducing a discretization that is a practical proxy, not a lossless encoding of $V_O$. The primary $O_t$ ↔ theory interface remains $V_O$ through the value object ( #value-object); terminal conditions are $\Sigma_t$'s internal operational encoding.

**Single-parameter edges.** Each edge carries one number ($p_{ij}$), not two. An earlier formalism attempt used $(p_{ij}, \theta_{ij})$ where $\theta$ was "contribution magnitude." This was dropped because the AND/OR combination rules at nodes absorb $\theta$'s role — the complexity budget goes to one bit per node ($\gamma$) instead of one float per edge.

### Acyclicity is Derived

*[Derived (from causal-structure + finite planning horizon)]*

Each node in $\Sigma_t$ represents a future event or state with temporal position $\tau_i \gt t$. An edge $X_i \to X_j$ requires $\tau_i \lt \tau_j$ ( #causal-structure: causes precede effects). A cycle $X_i \to X_j \to \cdots \to X_i$ would require $\tau_i \lt \tau_j \lt \cdots \lt \tau_i$, which is impossible for a real-valued time index.

Strategies involving iteration ("try A, if fail try B, if fail try A again") are acyclic when time-indexed. The sequence unfolds as:

$$A_1 \to \text{check}_1 \to B_1 \to \text{check}_2 \to A_2 \to \ldots$$

Each attempt is a distinct node at a distinct time. The apparent cycle is a linear chain in the unrolled view.

Formally: a finite set with a strict partial order (future events ordered by time) is representable as a DAG. This is a standard result in order theory.

**Scope of the acyclicity result.** This applies to $\Sigma_t$ (the agent's strategy over the future), not to $M_t$'s model of the environment, which may include cyclic causal processes (feedback loops in the physical world, market dynamics, ecosystem interactions). The acyclicity is specific to the purposeful substate.

## Epistemic Status

*Conditional* on the #and-or-scope restriction. The DAG structure itself follows from operational postulates: temporal ordering (acyclicity — exact), probabilistic uncertainty (Cox's theorem — exact), and the Causal Markov Condition theorem under causal sufficiency (Markov factorization — proved conditional). The full argument is in #graph-structure-uniqueness: P1 + P2 + causal sufficiency → CMC → DAG with Markov property. The result is *conditional on causal sufficiency* of the strategy (no latent common causes among strategy nodes). Causal sufficiency is a modeling ideal — the agent designed the graph, so *intended* causal relationships are explicit, but environmental common causes routinely go unmodeled in complex domains. When causal sufficiency fails, the Markov factorization breaks down, edge outcomes become correlated, and $\hat P_\Sigma$ overestimates success. This is model inadequacy ( #structural-adaptation-necessity), repairable by adding the missing common-cause nodes (L1 augmentation). See the Correlation Hierarchy above for the practical framework.

**Causal sufficiency and edge independence.** The AND/OR status propagation is correct when the DAG is causally sufficient (all common causes represented as nodes) — this follows from the Causal Markov Condition theorem ( #graph-structure-uniqueness). In complex real-world systems, causal sufficiency is systematically violated: shared infrastructure, common-mode risks, supply chain dependencies, and correlated adversary actions introduce latent common causes. Correlated failure is the dominant case, not the exception. The Correlation Hierarchy (above) characterizes three levels: independence (L0, tractable baseline), augmented DAG (L1, practical sweet spot), and full correlation (L2, mathematical ideal). AAD's formal strategy-layer results are proved under L0 but transfer to L1 (which is just a larger L0-compliant DAG). The independence model remains the tractable foundation for formal analysis; L1 augmentation is the recommended practice for deployment.

The AND/OR parameterization is a parsimony-motivated formulation choice within the strongly motivated graphical structure, not a derived necessity ( #and-or-scope). The single-parameter edge convention is similarly a formulation choice motivated by convergence across three independent attempts.

## Discussion

**The graph structure is derived; the parameterization is chosen.** The DAG structure follows from temporal ordering (acyclicity — proved) and the Causal Markov Condition theorem under causal sufficiency (Markov factorization — proved conditional; see #graph-structure-uniqueness). This is a theorem-backed result, not a sketch: the CMC (Spirtes et al. 2000, Pearl 2009) proves that any causally sufficient causal DAG with independent exogenous noise satisfies the Markov factorization. The status is therefore: DAG-with-Markov-property is *derived* from operational postulates plus causal sufficiency. AAD uses AND/OR parameterization within this derived structure because (a) AND/OR is the most parsimonious complete basis for binary combination, (b) the representation converged across three independent formalism attempts. Alternative parameterizations within the derived graphical structure are legitimate research directions.

**Combination assignment is principled but fallible.** The question "if I remove one parent, can $v$ still be achieved?" is derivable from $M_t$'s causal model — it's a principled assignment, not arbitrary. But the assignment can be wrong (false AND = pessimistic over-investment; false OR = optimistic under-investment), and should be updateable when evidence reveals a different structural relationship.

**Connection to Pearl's framework.** The strategy DAG is not merely analogous to a causal Bayesian network — it IS one, by construction. #graph-structure-uniqueness proves that the operational postulates (P1-P4) plus causal sufficiency yield the Markov factorization via the Causal Markov Condition theorem (Spirtes et al. 2000, Pearl 2009). Pearl's do-calculus therefore applies directly to status propagation and plan evaluation. In Regime A domains, where the agent performs genuine interventions and observes isolated outcomes, the DAG's edge credences approximate interventional probabilities and do-calculus yields clean causal estimates. In Regimes B and C, the edge credences are the agent's working causal beliefs, updated from data of weaker identification strength. The DAG remains useful for planning --- the agent must act on *some* causal model --- but the plan-confidence score $\hat P_\Sigma$ inherits the identification weaknesses of its constituent edges. An agent operating primarily in Regime C should treat $\hat P_\Sigma$ as a rough heuristic, not a calibrated probability.

**Depth penalties on calibration.** Beyond the confidence decay that deeper DAGs suffer ( #chain-confidence-decay), the two-edge strategic dynamics analysis ( #strategic-dynamics-derivation (Props B.2-B.3)) shows that deeper edges are also harder to calibrate. Edge $k$ in a chain is tested only when all upstream edges succeed, so its effective correction rate is attenuated by $\prod_{j\ltk}\theta_j$ (the evidence-starvation effect). Deeper DAGs therefore face a double penalty: lower aggregate confidence AND slower convergence of edge credences toward truth. This reinforces the structural pressure toward shallow, observable strategies — deep plans require both high per-edge reliability and sustained observability at every intermediate level to remain calibratable.

**Edge independence is a consequence of causal sufficiency, not a separate assumption.** The Correlation Hierarchy (Formal Expression, above) establishes this precisely: the AND/OR propagation's correctness is not a matter of "assuming independence" — it is a consequence of whether the DAG is causally sufficient. The CMC theorem ( #graph-structure-uniqueness) proves that causal sufficiency → exogenous independence → Markov factorization → correct AND/OR propagation. The assumption is causal sufficiency; independence is the consequence.

*What L0 buys:* Tractable $O(\lvert V\rvert + \lvert E\rvert)$ status propagation; single-parameter edges; clean persistence proofs (the sector condition transfers from per-edge credence to plan value via the Jacobian — Prop B.5 in #strategic-dynamics-derivation).

*What L0 costs when the DAG is causally insufficient:* $\hat P_\Sigma$ systematically overestimates success. The plan-confidence error $\delta_s = \hat P_\Sigma - \Phi$ proved persistent by B.5 tracks calibration *within the L0 model* — $\Phi$ is the AND/OR formula at true edge rates, not actual plan success ( #strategic-calibration). Gradient-based credit assignment ( #credit-assignment-boundary) inherits the same bias: the residual $(y_G - \hat P_\Sigma)$ conflates per-edge miscalibration with omitted correlation structure.

*The L1 remedy:* Add common-cause nodes and restructure the DAG so each common cause is factored above the correlation it creates (see Correlation Hierarchy above). The AND/OR propagation then applies correctly to the restructured DAG, and all L0 formal results transfer because the restructured DAG is itself L0-compliant. The key engineering challenge is twofold: identifying which common causes matter, and positioning them correctly in the graph topology.

## Working Notes

- The Correlation Hierarchy (L0/L1/L2) is now first-class in the Formal Expression. The relationship between causal sufficiency, edge independence, and $\hat P_\Sigma$ accuracy is grounded by the CMC theorem. The main open question is practical: what heuristics help agents identify which common causes are worth modeling at L1? This is a domain-specific engineering question, not a theoretical gap.
- The graph-uniqueness argument (P1-P4 + causal sufficiency → DAG with Markov property via CMC) is proved, not sketched. See #graph-structure-uniqueness for the full derivation and the parallel to Cox's theorem. The DAG structure is derived; the AND/OR parameterization remains a formulation choice. strategy-dag stays typed as Definition because the *parameterization* is chosen, even though the *graphical structure* is derived.
- Health metrics (groundedness, observability coverage, weighted redundancy, bottleneck scores) are scaffold — engineering quantities for monitoring DAG health, not principled derivations. They may be useful for implementation but should not enter the theory's formal chain.
- **Satisfaction criterion.** $V_{O_t}^{\min}$ is now introduced in #objective-functional as a parameter of the objective — the minimum acceptable trajectory value. The well-formedness constraint references it from there, not from #satisfaction-gap. The satisfaction gap diagnostic builds on $V_{O_t}^{\min}$ but does not define it.
- **Terminal alignment error.** When the agent achieves its terminal conditions but evaluates $V_{O_t}(\tau) \lt V_{O_t}^{\min}$ on the actual trajectory, the well-formedness belief was wrong — the operational success criteria didn't capture what the objective actually required. This is detectable only through experience (achieve the terminals, evaluate $V_{O_t}$), not through a priori analysis. It triggers terminal reassessment — a structural change in $\Sigma_t$ driven by the $O_t$ ↔ terminal mismatch. Whether this should be formalized as a named diagnostic signal ($\delta_\text{align}$) alongside $\delta_\text{sat}$, $\delta_\text{regret}$, and $\delta_\text{strategic}$ is open.
