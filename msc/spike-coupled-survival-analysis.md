# Spike: Coupled Survival Analysis

> **Purpose**: Map which Section II (Actuated Adaptation) results depend on directed separation and which survive without it, for Class 2 (fully merged) agents like LLM-based systems.
>
> **Epistemic status**: Working analysis. The classifications are the author's best judgment after reading each segment. Some borderline cases are flagged with explicit uncertainty.
>
> **Date**: 2026-04-02

---

## 0. The Question

AAD's Section II develops purposeful agency under the assumption of directed separation:

$$M_{\tau^+} = f_M(M_{\tau^-}, e_\tau) \qquad \text{(no } G_t \text{ argument)}$$

This enables the sequential orient cascade ($M_t$ first, then $G_t$) and cleanly separates epistemic from strategic dynamics.

Class 2 agents (fully merged, like LLM-based agents) violate directed separation by construction. Their processing is goal-conditioned: the prompt includes the task objective, attention processes goals and observations together, and the forward pass simultaneously updates beliefs and revises strategy. The question: which Section II results are still valid when directed separation fails?

The #directed-separation segment itself says: "Class 2: Requires coupled formulation from the start — $X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$ without decomposition." This spike is the analysis that statement calls for.

---

## 1. Classification Framework

Four categories, ordered by severity of impact:

- **SURVIVES EXACTLY**: The result does not reference directed separation in its statement or derivation. It holds for any agent with $X_t = (M_t, G_t)$, regardless of how the update factorizes.
- **SURVIVES APPROXIMATELY**: The result's statement is exact under directed separation and becomes an approximation when directed separation fails. The approximation quality depends on $\kappa_{\text{processing}}$.
- **REQUIRES MODIFICATION**: The result's statement changes for Class 2 agents, but an analogous result exists in the coupled formulation.
- **FAILS**: The result is genuinely inapplicable to Class 2 agents — not just approximate, but structurally wrong.

---

## 2. Section I Floor

Before analyzing Section II, note what Section I already provides regardless of directed separation. The #directed-separation segment explicitly states: "Section I's $M_t$-side quantities — $\delta$, $\eta^\ast$, $\mathcal{T}$, the persistence condition — remain well-defined on $M_t$ regardless of whether directed separation holds."

However, for Class 2 agents, there is a subtlety: $M_t$ is not cleanly separable from $G_t$ in the processing. The Section I quantities are well-*defined* on the epistemic substate, but the epistemic substate itself is not independently *identifiable* in the agent's processing. The definitions remain valid; the *estimation* of these quantities from observing the agent's behavior becomes harder because you cannot isolate the epistemic update from the strategic update.

**What Section I provides for any agent (the floor):**
- Mismatch signal $\delta_t$ (defined on observable prediction error — this is observable regardless of internal architecture)
- Update gain $\eta^\ast$ (defined on uncertainty ratio — the concept applies, though the agent's actual gain may be goal-conditioned)
- Adaptive tempo $\mathcal{T}$ (rate of useful information acquisition — well-defined, though the "useful" may be goal-conditioned)
- Persistence condition $\alpha > \rho / R$ (structural persistence of the adaptive system)
- Sector-condition stability (Lyapunov bound on mismatch)

**What Section II adds above this floor** is the purposeful layer: objectives, strategy, diagnostics (satisfaction gap, control regret), the orient cascade that connects them, and the strategy-revision machinery. The question is how much of this purposeful layer survives.

---

## 3. Segment-by-Segment Classification

### 3.1 #agent-spectrum — SURVIVES EXACTLY

**Type**: Definition. **Depends on**: agent-environment, agent-model.

The agent spectrum (±model × ±objective quadrants) is a classification of agent types. It does not reference directed separation at all. Class 2 agents are actuated agents (structured $M_t$ and $O_t$) — they occupy the same quadrant regardless of how their internal processing is organized.

**Rationale**: The spectrum classifies agents by *what information they maintain*, not by *how that information is processed*. A fully merged LLM agent has both a reality model and objectives; it is an actuated agent.

---

### 3.2 #complete-agent-state — SURVIVES APPROXIMATELY

**Type**: Formulation. **Depends on**: agent-model, scope-condition, recursive-update.

The formulation $X_t = (M_t, G_t)$ is a representational choice. The segment itself notes: "Without directed separation, the general update is $X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$ — a single function on the full state. The decomposition into separate $f_M$ and $f_G$ is an additional structural claim about how the update factorizes."

**For Class 2 agents**: The decomposition $X_t = (M_t, G_t)$ is still *statable* — you can identify epistemic and purposeful content in the agent's state even when the processing entangles them. But the *factorized update dynamics* ($f_M$ independent of $G_t$, $f_G$ depending on $M_{\tau^+}$) become an approximation. The actual dynamics are:

$$X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$$

and the factored form

$$M_{\tau^+} \approx f_M(M_{\tau^-}, e_\tau), \qquad G_{\tau^+} \approx f_G(G_{\tau^-}, M_{\tau^+}, e_\tau)$$

becomes approximate, with error depending on $\kappa_{\text{processing}}$.

**Approximation quality**: When $\kappa_{\text{processing}} \approx 0$, the factorization is exact. As $\kappa_{\text{processing}} \to 1$, the factorization error grows. For a fully merged LLM ($\kappa \approx 1$), the factorization is not a useful approximation — the coupled form $f_X$ is the correct description. What survives exactly is the *notation* $X_t = (M_t, G_t)$ as a coordinate system on the state space; what fails is the *dynamical decomposition* into independent update functions.

---

### 3.3 #objective-functional — SURVIVES EXACTLY

**Type**: Formulation. **Depends on**: complete-agent-state.

$O_t$ induces $V_{O_t}: \text{trajectories} \to \mathbb{R}$. This is a definition of the objective's interface to the theory. It does not reference how the agent processes observations or updates its state. Whether the agent's epistemic update is goal-blind or goal-conditioned, the objective still evaluates trajectories via a scalar functional.

**Rationale**: The objective functional is about *evaluation*, not about *processing*. A Class 2 agent still has something it is trying to achieve, and that something still induces a value over trajectories.

---

### 3.4 #value-object — SURVIVES EXACTLY

**Type**: Definition. **Depends on**: objective-functional, agent-model.

$V_O(M_t, \pi; N_h) = \mathbb{E}[V_{O_t}(\tau) \mid M_t, \pi]$ and the action-value form $Q_O$ with $do(\cdot)$ notation. These are conditional expectations of the objective functional. They require $M_t$ and $\pi$ as inputs but do not require that $M_t$ was updated independently of $G_t$.

**Rationale**: The value object is a mathematical definition — conditional expectations given a model state and a policy. The model state may have been produced by a goal-conditioned update; the value object doesn't care how the state was produced, only what it currently is. The $do(\cdot)$ notation in $Q_O$ is about the agent's action being an intervention, not about the internal processing of observations.

**Subtlety**: For Class 2 agents, $M_t$ reflects goal-conditioned processing, so $V_O(M_t, \pi; N_h)$ incorporates whatever biases goal-conditioning introduced into the epistemic state. The value object is well-defined but potentially biased by motivated reasoning embedded in $M_t$. This is not a failure of the definition — it is a consequence of the agent's architecture.

---

### 3.5 #strategy-dimension — SURVIVES EXACTLY

**Type**: Definition. **Depends on**: complete-agent-state, objective-functional.

$G_t = (O_t, \Sigma_t)$. This is a definitional decomposition of the purposeful substate into evaluation (objective) and guidance (strategy). The decomposition is structural — "it reflects a structural difference in the information, not a dynamic or timescale claim."

**Rationale**: The distinction between "what makes a trajectory good" and "how to produce a good trajectory" exists for any purposeful agent. An LLM-based agent has both an objective (the task it was given) and a strategy (its plan for accomplishing it, possibly implicit in its reasoning trace). The decomposition does not require that these are processed independently.

---

### 3.6 #causal-hierarchy-requirement — SURVIVES EXACTLY

**Type**: Derived. **Depends on**: value-object, pearl-causal-hierarchy, scope-condition.

Evaluating $Q_O$ requires Level 2 (interventional) queries. This is a direct application of the causal hierarchy theorem to the value-object definition. The result depends on the structure of $Q_O$ (which contains $do(\cdot)$), not on how the agent processes observations.

**Rationale**: The need for Level 2 knowledge is about the *type of question* the agent must answer ($P(Y \mid do(X))$), not about its processing architecture. A Class 2 agent still needs to answer "what happens if I do $a$?" — and this still requires interventional knowledge.

**Note**: The segment's scope narrowing to "learning agents" (those that must acquire Level 2 knowledge during operation) actually highlights a Class 2 specificity: LLMs have pre-trained causal priors from language, which are then refined through loop-generated interventional data. The scope narrowing applies equally.

---

### 3.7 #loop-interventional-access — SURVIVES EXACTLY

**Type**: Derived. **Depends on**: causal-hierarchy-requirement, recursive-update, causal-structure.

The feedback loop provides interventional data by construction: $(a_t, o_{t+1})$ is generated under the agent's intervention. This is a property of the loop structure, not of the agent's internal processing.

**Rationale**: A Class 2 agent in a feedback loop still acts and observes consequences. The data $(a_t, o_{t+1})$ is interventional regardless of whether the agent's internal processing is goal-conditioned. The segment explicitly notes: "This includes LLM agents operating through a tool-use loop."

---

### 3.8 #ciy-observational-proxy — SURVIVES EXACTLY

**Type**: Scope. **Depends on**: causal-information-yield, loop-interventional-access.

The admissibility regimes (A/B/C) for CIY estimation are domain properties, not agent-architecture properties. The proxy definition and safety conditions are information-theoretic quantities that don't reference directed separation.

**Rationale**: Whether CIY can be estimated depends on the domain's action space and observation structure, not on the agent's internal processing topology.

---

### 3.9 #ciy-unified-objective — SURVIVES EXACTLY

**Type**: Discussion. **Depends on**: causal-information-yield, ciy-observational-proxy, value-object, action-selection.

The unified policy objective (exploit + explore) is a structural claim about optimal policy form. It references $V_O$ and CIY, both of which survive. The discussion-grade status is unchanged.

**Rationale**: The exploration-exploitation tradeoff exists for any learning agent. The extended three-way tradeoff (exploit/explore/deliberate) also exists for Class 2 agents. If anything, the deliberation mode is more prominent for LLM agents (reasoning traces = deliberation).

---

### 3.10 #explicit-strategy-condition — SURVIVES EXACTLY

**Type**: Normative. **Depends on**: temporal-optimality, strategy-dimension, causal-hierarchy-requirement.

The condition $C_{\text{plan}} + C_{\text{maintain}} < C_{\text{explore}} + C_{\text{repair}}$ is a cost comparison. It does not reference how the agent updates its model. The normative claim is about *when explicit strategy is worth maintaining*, not about *how the agent processes observations*.

**Rationale**: An LLM agent faces the same planning-vs-exploration tradeoff. The condition is arguably *more* relevant for Class 2 agents because $C_{\text{maintain}}$ includes the context-window cost of keeping $\Sigma_t$ in working memory.

---

### 3.11 #chain-confidence-decay — SURVIVES EXACTLY

**Type**: Derived. **Depends on**: strategy-dimension.

$\log P(\text{chain}) = \sum_i \log P(E_i \mid E_{<i})$ — this is a mathematical identity (chain rule of probability). It applies to any probabilistic multi-step plan regardless of the agent's architecture.

**Rationale**: This is pure probability theory. The decay of confidence with depth is about the structure of the strategy, not about how the agent processes observations.

---

### 3.12 #and-or-scope — SURVIVES EXACTLY

**Type**: Scope. **Depends on**: strategy-dimension, chain-confidence-decay.

The AND/OR combination restriction is a scope narrowing on strategy representation. It constrains how $\Sigma_t$ combines parent contributions, not how $M_t$ is updated.

**Rationale**: A Class 2 agent's strategy can still be modeled as an AND/OR DAG. The scope restriction is about the expressiveness of the strategy representation, not about the processing architecture.

---

### 3.13 #strategy-dag — SURVIVES EXACTLY (structure), REQUIRES MODIFICATION (leaf credence mechanism)

**Type**: Definition. **Depends on**: and-or-scope, causal-structure, pearl-causal-hierarchy, objective-functional, strategy-dimension.

The DAG structure $\Sigma_t = (V_t, E_t, p_t, \gamma_t)$ survives: acyclicity is derived from temporal ordering (independent of processing architecture), the propositional nodes and edge credences are about the strategy's content, not the agent's processing.

**However**: The leaf credence mechanism $p_v(M_t) = \Pr(\text{action } v \text{ succeeds at } \tau_v \mid M_t)$ and the edge semantics $p_{ij} = \text{Cr}_i(j \text{ advances} \mid i \text{ completed}, M_t)$ explicitly condition on $M_t$. Under directed separation, $M_t$ is a clean epistemic state produced by goal-blind processing. For Class 2 agents, the conditioning state is $M_t^{(G)}$ — an epistemic state produced by goal-conditioned processing.

**Modification needed**: The credences become explicitly conditioned on the full state:

$$p_v(X_t) = \Pr(\text{action } v \text{ succeeds at } \tau_v \mid X_t)$$

For Class 2 agents, the epistemic substate is not separable from the purposeful substate in the conditioning. The credences may exhibit goal-conditioned biases (optimism about goal-aligned actions, pessimism about alternatives). The DAG structure is unaffected; the *semantics of the credences* are subtly different.

**Status propagation**: The forward-pass computation $s_v = f(\text{parents})$ is a mathematical operation on the DAG and is architecture-independent. **Survives exactly.**

---

### 3.14 #directed-separation — FAILS (by definition)

**Type**: Derived + Scope. **Depends on**: complete-agent-state, recursive-update, scope-condition.

This is the result that defines the scope boundary. It holds for Class 1 agents and fails for Class 2 agents — that is its own statement. For Class 2 agents, the relevant formulation is the coupled update $X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$.

**What replaces it**: Not nothing. The *information dependency* that directed separation formalizes — "epistemic state informs purposeful evaluation" — still exists in a weaker form. Even in a fully merged processor, the agent's beliefs about reality constrain its strategic assessments. The dependency is bidirectional rather than unidirectional: beliefs inform strategy AND goals inform belief formation. The replacement is a mutual-information characterization rather than a conditional-independence statement.

---

### 3.15 #satisfaction-gap — SURVIVES EXACTLY

**Type**: Definition. **Depends on**: value-object, objective-functional.

$\delta_{\text{sat}} = V_{O_t}^{\min} - A_O(M_t; \Pi, N_h)$. This is a mathematical definition: the difference between a threshold and a supremum over a function class. It depends on $M_t$ and $V_{O_t}$, not on how $M_t$ was produced.

**Rationale**: An LLM agent can evaluate whether its goal is achievable given its current beliefs. The satisfaction gap is well-defined regardless of whether those beliefs were formed in a goal-blind or goal-conditioned manner.

**Subtlety**: For Class 2 agents, $A_O(M_t; \Pi, N_h)$ is computed from a goal-conditioned $M_t$. This means the agent's assessment of attainability may be biased — optimistic about goal-aligned possibilities, pessimistic about alternatives. The *definition* survives exactly; the *accuracy* of the agent's self-assessment is degraded by motivated reasoning. This is a property of $M_t$'s quality, not of the gap definition.

---

### 3.16 #control-regret — SURVIVES EXACTLY

**Type**: Definition. **Depends on**: value-object, satisfaction-gap.

$\delta_{\text{regret}} = A_O - V_O(M_t, \pi_{\text{current}}; N_h) \geq 0$. Same reasoning as satisfaction gap: a mathematical definition that depends on $M_t$ and $V_O$, not on how $M_t$ was produced.

The 2x2 diagnostic table ($\delta_{\text{sat}} \times \delta_{\text{regret}}$) also survives — it is a classification of situations based on two scalar quantities, both of which are well-defined.

---

### 3.17 #strategic-calibration — SURVIVES APPROXIMATELY

**Type**: Definition. **Depends on**: strategy-dag, value-object.

The edge residual $r_{ij} = \mathbb{E}[\Delta V_O \mid \text{edge traversed}, M_t] - \Delta V_O^{\text{observed}}$ is defined in terms of $M_t$ and $\Sigma_t$.

**For Class 2 agents**: The residual is still computable in principle — compare predicted value increment against observed. But the *predicted* value increment comes from a goal-conditioned model, which may introduce systematic bias. The residual conflates two sources of error: (1) the edge's causal credence is wrong, and (2) the underlying $M_t$ is biased by goal-conditioning. Under directed separation, source (2) is absent — the edge residual measures only the strategy's calibration against an unbiased epistemic state. Without directed separation, the residual measures the *joint* calibration of the coupled $(M_t, \Sigma_t)$ system.

**Approximation quality**: The strategic calibration residual is most meaningful when goal-conditioning effects on $M_t$ are small relative to the edge's own prediction error. When $\kappa_{\text{processing}} \approx 0$, the residual cleanly measures edge calibration. When $\kappa_{\text{processing}} \approx 1$, the residual is confounded — the agent cannot distinguish "my edge credence is wrong" from "my beliefs are biased by my goals." The error is bounded by the mutual information $I(G_t; M_{\tau^+} \mid e_\tau, M_{\tau^-})$ — the amount of goal information leaking into the epistemic update.

---

### 3.18 #orient-cascade — REQUIRES MODIFICATION

**Type**: Derived. **Depends on**: directed-separation, mismatch-signal, satisfaction-gap, control-regret, strategic-calibration.

This is the result most directly dependent on directed separation. The cascade's *ordering* is forced by information dependency: "You cannot evaluate strategy quality with a broken reality model." Under directed separation, the information dependency is strict and unidirectional: $M_t$ feeds into $\delta_{\text{sat}}$, which feeds into $\delta_{\text{regret}}$, which feeds into $\delta_{\text{strategic}}$, which feeds into $O_t$ revision. The sequential resolution is the unique correct order.

**For Class 2 agents**: The information dependency is *not* unidirectional. Goals inform belief formation (the agent reading code with goal "fix the auth bug" processes differently than with goal "add logging"). The cascade becomes a **simultaneous fixed-point problem**, not a sequential resolution.

**What replaces it**: A coupled fixed-point or iterative convergence process:

$$X^{(k+1)} = f_X(X^{(k)}, e_\tau)$$

where $k$ indexes iterations of the coupled update (which, for an LLM, may correspond to a single forward pass or to chain-of-thought steps). The *logical dependencies* still exist — you still cannot meaningfully evaluate strategy without some epistemic grounding — but they are satisfied approximately and simultaneously rather than exactly and sequentially.

**Modified cascade for Class 2**:

1. **Joint epistemic-strategic update**: Process the observation through the coupled system. The LLM's forward pass simultaneously updates beliefs about reality and evaluates strategic implications. The output is not "first beliefs, then strategy" but "beliefs-and-strategy co-determined by the observation and the current state."

2. **Post-hoc diagnostic decomposition**: After the coupled update, the agent can *decompose* the result into epistemic and strategic components for diagnostic purposes:
   - Evaluate $\delta_{\text{sat}}$ from the updated (goal-conditioned) $M_t$
   - Evaluate $\delta_{\text{regret}}$ similarly
   - Use the $2 \times 2$ diagnostic table to classify the situation
   - The diagnostic framework survives; the *sequential causal ordering* of the cascade does not

3. **Objective revision still last resort**: The normative ordering — "don't revise $O_t$ until you've verified $\Sigma_t$ cannot close the gap" — survives as a *design principle*, not as a derived result. For Class 2 agents, it must be enforced architecturally (e.g., by requiring explicit justification for objective revision) rather than derived from information dependency.

**The cascade's ORDERING survives as a normative design principle. The cascade's derivation from unidirectional information dependency does not survive.**

**Approximation quality**: For $\kappa_{\text{processing}} \approx 0$, the sequential cascade is a good approximation of the coupled fixed point. For $\kappa_{\text{processing}} \approx 1$, the sequential approximation can be arbitrarily poor — processing the same event with different goals produces systematically different "epistemic" updates. The error is not bounded by a simple function of $\kappa$; it depends on the specific observation, the agent's goals, and the degree to which the observation is ambiguous (ambiguous observations are where goal-conditioning has the most effect).

---

### 3.19 #observability-dominance — SURVIVES EXACTLY

**Type**: Derived. **Depends on**: strategy-dag, update-gain.

"Unobservable strategy edges cannot be updated — the gain principle drives their update rate to zero." This result depends on the structure of the gain principle ($\eta = U_{\text{edge}} / (U_{\text{edge}} + U_{\text{obs}})$) applied to strategy edges, not on directed separation.

**Rationale**: When $\sigma_v \approx 0$, $U_{\text{obs}} \to \infty$, and $\eta_{\text{edge}} \to 0$ regardless of the agent's processing architecture. An LLM agent cannot update credences about edges whose outcomes it cannot observe, for the same mathematical reason as any other agent. The mechanism is about the information channel, not about the internal processing.

---

### 3.20 #edge-update-via-gain — SURVIVES APPROXIMATELY

**Type**: Hypothesis. **Depends on**: strategy-dag, update-gain, mismatch-signal.

The edge update rule $p_{ij}^{\text{new}} = p_{ij} + \eta_{\text{edge}} \cdot (\text{signal} - p_{ij})$ extends the gain principle from $M_t$ to $\Sigma_t$ edges. The rule itself is architecture-independent — it is a generic update formula. The hypothesis is that the uncertainty-ratio gain is the right weighting.

**For Class 2 agents**: The update rule is applicable, but two complications arise:

1. **The signal function is goal-conditioned.** The observation $o_t$ is processed by a goal-conditioned mechanism, so the signal $\text{signal}(o_t, i, j)$ reflects goal-conditioned interpretation of the evidence. An agent optimistic about its current strategy may extract weaker disconfirmatory signals than an agent with goal-blind processing.

2. **Double-counting of evidence.** The working notes already flag this: "The orient cascade processes $M_t$ first, then edge updates. Both use the same observation $o_t$." Without directed separation, this double-counting is worse — the same observation simultaneously updates beliefs and edge credences through the same coupled mechanism, creating statistical dependencies that the independent-update formula does not account for.

**Approximation quality**: The gain principle's *form* (update toward observed value, weighted by uncertainty ratio) is robust — it applies wherever an agent updates a belief from noisy evidence. The *magnitude* of the update may be biased by goal-conditioning. For $\kappa_{\text{processing}} \approx 0$, the bias is negligible. For $\kappa_{\text{processing}} \approx 1$, the effective gain may be systematically wrong: $\eta_{\text{edge}}^{\text{effective}} = \eta_{\text{edge}} + O(\kappa_{\text{processing}} \cdot \text{goal-evidence correlation})$.

---

### 3.21 #edge-update-causal-validity — SURVIVES EXACTLY

**Type**: Scope. **Depends on**: edge-update-via-gain, causal-information-yield, loop-interventional-access, strategic-calibration, strategy-dag.

The three conditions (C1: agent controls leaf, C2: outcome attributable, C3: execution conditions vary) and three regimes (A/B/C) are about the domain's causal structure and the agent's action space, not about the agent's internal processing architecture.

**Rationale**: Whether the agent's action constitutes a genuine intervention (C1), whether outcomes are attributable (C2), and whether execution conditions vary (C3) are properties of the agent-environment interface, not of the agent's epistemic-strategic coupling. An LLM agent running tests in a CI pipeline has the same causal identification strength as a modular agent running the same tests.

The identifiability coefficient $\iota_{ij}$ and identifiability-adjusted gain similarly depend on the DAG structure and observability, not on directed separation.

---

### 3.22 #credit-assignment-boundary — SURVIVES EXACTLY

**Type**: Discussion. **Depends on**: strategy-dag, edge-update-via-gain, strategic-calibration, observability-dominance, gain-sector-bridge, strategic-dynamics-derivation.

The credit-assignment boundary characterization — tractable cases, intractability barriers, design requirement, hierarchy of quality — is about the structure of the DAG inference problem, not about the agent's processing architecture.

**Key result**: "Persistence is credit-assignment-free" (Prop B.5) — the sector condition transfers from credence space to value space via the Jacobian, regardless of how the credences were formed. This holds for Class 2 agents.

**The default signal function** (gradient-based attribution) is defined in terms of the DAG's Jacobian and observed outcomes. It does not reference directed separation.

---

### 3.23 #structural-change-as-parametric-limit — SURVIVES EXACTLY

**Type**: Formulation. **Depends on**: strategy-dag, structural-adaptation-necessity.

The six operations on $\Sigma_t$ (reweighting, $\gamma$ reclassification, pruning, grafting, objective revision, full restructure) are defined in terms of the DAG representation, not in terms of how the agent processes observations.

**Rationale**: An LLM agent can reweight edges, prune failing branches, graft new alternatives, and revise objectives. The continuity of structural change as a parametric limit is about the *probabilistic representation*, not about the *processing architecture*.

---

### 3.24 #strategy-persistence-schema — SURVIVES APPROXIMATELY

**Type**: Proposed-schema. **Depends on**: sector-condition-stability, strategic-calibration, strategy-dag.

The schema states: if strategic update dynamics satisfy sector conditions (SA1, SA2', SA3), then $\Sigma_t$ persists iff $\alpha_\Sigma > \rho_\Sigma / R_\Sigma$.

**For Class 2 agents**: The sector-condition framework is domain-agnostic — it applies to any system with a mismatch state, correction function, and bounded disturbance. The question is whether the *strategic update dynamics* of a Class 2 agent satisfy the preconditions.

**Complications**:

1. **SA1 (zero correction at zero mismatch)**: For Class 2 agents, "zero strategic mismatch" may not be a stable state. Goal-conditioned processing may produce phantom corrections — the agent "improves" its strategy based on goal-biased interpretation of neutral evidence, violating SA1. The violation is proportional to $\kappa_{\text{processing}}$.

2. **The sector parameter $\alpha_\Sigma$**: The verified cases (Props B.1-B.4) assume that the edge update uses the gain principle with an unbiased signal. For Class 2 agents with goal-conditioned signals, the effective sector parameter is:

$$\alpha_\Sigma^{\text{eff}} = \alpha_\Sigma - O(\kappa_{\text{processing}} \cdot \text{bias magnitude})$$

The persistence threshold $\alpha_\Sigma > \rho_\Sigma / R_\Sigma$ requires a larger $\alpha_\Sigma$ to compensate for the bias.

3. **The four verified cases**: These hold as mathematical results about Beta-Bernoulli dynamics in specific DAG topologies. If the edge updates are biased (from goal-conditioned processing), the sector parameter changes but the framework still applies. The framework is robust to approximation — what changes is the tightness of the bound, not whether persistence holds.

**Approximation quality**: The schema survives in form. The sector parameters are degraded by $O(\kappa_{\text{processing}})$, making the persistence condition harder to satisfy. For $\kappa_{\text{processing}} \approx 1$ (fully merged), the effective $\alpha_\Sigma$ may be significantly lower than the goal-blind value, requiring either higher observation rates or more tolerance for strategic mismatch.

---

## 4. Summary Table

| # | Segment | Classification | Key Dependency on Directed Separation |
|---|---------|---------------|--------------------------------------|
| 1 | #agent-spectrum | **SURVIVES EXACTLY** | None |
| 2 | #complete-agent-state | **SURVIVES APPROX** | Factorized update dynamics |
| 3 | #objective-functional | **SURVIVES EXACTLY** | None |
| 4 | #value-object | **SURVIVES EXACTLY** | None |
| 5 | #strategy-dimension | **SURVIVES EXACTLY** | None |
| 6 | #causal-hierarchy-requirement | **SURVIVES EXACTLY** | None |
| 7 | #loop-interventional-access | **SURVIVES EXACTLY** | None |
| 8 | #ciy-observational-proxy | **SURVIVES EXACTLY** | None |
| 9 | #ciy-unified-objective | **SURVIVES EXACTLY** | None |
| 10 | #explicit-strategy-condition | **SURVIVES EXACTLY** | None |
| 11 | #chain-confidence-decay | **SURVIVES EXACTLY** | None |
| 12 | #and-or-scope | **SURVIVES EXACTLY** | None |
| 13 | #strategy-dag | **SURVIVES EXACTLY** (structure); **REQUIRES MOD** (credence conditioning) | Leaf credences conditioned on $M_t$ alone |
| 14 | #directed-separation | **FAILS** | This IS the result |
| 15 | #satisfaction-gap | **SURVIVES EXACTLY** | None (definition) |
| 16 | #control-regret | **SURVIVES EXACTLY** | None (definition) |
| 17 | #strategic-calibration | **SURVIVES APPROX** | Residual conflated with $M_t$ bias |
| 18 | #orient-cascade | **REQUIRES MODIFICATION** | Sequential ordering derived from unidirectional dependency |
| 19 | #observability-dominance | **SURVIVES EXACTLY** | None |
| 20 | #edge-update-via-gain | **SURVIVES APPROX** | Signal function goal-conditioned |
| 21 | #edge-update-causal-validity | **SURVIVES EXACTLY** | None (domain property) |
| 22 | #credit-assignment-boundary | **SURVIVES EXACTLY** | None |
| 23 | #structural-change-as-parametric-limit | **SURVIVES EXACTLY** | None |
| 24 | #strategy-persistence-schema | **SURVIVES APPROX** | Sector parameter degraded |

**Scorecard**:
- SURVIVES EXACTLY: 16 of 24 (including the exact part of #strategy-dag)
- SURVIVES APPROXIMATELY: 5 of 24 (#complete-agent-state, #strategic-calibration, #edge-update-via-gain, #strategy-persistence-schema, and the credence conditioning part of #strategy-dag)
- REQUIRES MODIFICATION: 2 of 24 (#orient-cascade, credence conditioning in #strategy-dag)
- FAILS: 1 of 24 (#directed-separation — by definition)

**The majority of Section II's architecture survives.** The damage from dropping directed separation is concentrated in the *processing dynamics* — the orient cascade ordering and the accuracy of individual update steps — not in the *definitional and structural* results.

---

## 5. Approximation Error Analysis

For the five "SURVIVES APPROXIMATELY" results, the error depends on $\kappa_{\text{processing}}$.

### 5.1 General Error Structure

The fundamental error source is goal-information leaking into the epistemic update:

$$\Delta M_{\text{bias}} = M_{\tau^+}^{\text{coupled}} - M_{\tau^+}^{\text{decoupled}} = f_X^M(X_{\tau^-}, e_\tau) - f_M(M_{\tau^-}, e_\tau)$$

where $f_X^M$ denotes the epistemic component of the coupled update. This bias is bounded (in expectation) by:

$$\lVert \Delta M_{\text{bias}} \rVert \leq C \cdot \kappa_{\text{processing}} \cdot H(G_t \mid e_\tau, M_{\tau^-})$$

where $C$ is a domain-dependent constant relating information-theoretic coupling to state-space error. The bias is zero when $\kappa = 0$ (modular) and maximal when $\kappa \approx 1$ and the goal state is highly informative.

### 5.2 Per-Result Error Characterization

**#complete-agent-state** (factorized dynamics):
- Error: $\lVert f_X(X, e) - (f_M(M, e), f_G(G, f_M(M, e), e)) \rVert$
- Behavior: Grows monotonically with $\kappa$. At $\kappa = 0$, zero. At $\kappa = 1$, can be $O(1)$ (order of the state change itself).
- For Class 2: The factorized form is not a useful approximation. Use $f_X$ directly.

**#strategic-calibration** (residual conflation):
- Error: The residual $r_{ij}$ gains an additive bias term $b_{ij}(\kappa)$ reflecting goal-conditioned $M_t$ bias.
- Behavior: $b_{ij} = O(\kappa \cdot \text{ambiguity}(e_\tau))$, where ambiguity measures how much the observation's interpretation depends on goals. Unambiguous observations (test passes/fails) have low bias regardless of $\kappa$. Ambiguous observations (code review assessments, strategic intelligence) have bias proportional to $\kappa$.
- Implication: In software domains (high-ambiguity-free observations), strategic calibration remains useful even for Class 2 agents. In organizational domains (high ambiguity), the residual is unreliable.

**#edge-update-via-gain** (goal-conditioned signal):
- Error: The effective signal becomes $\text{signal}_{\text{eff}} = \text{signal}_{\text{clean}} + \epsilon(\kappa, G_t)$, where $\epsilon$ is a goal-dependent bias.
- Behavior: The gain formula's *form* is unaffected. The *signal* fed into it carries bias $O(\kappa)$. The bias has a consistent direction: toward confirming the current strategy (optimism about $G_t$-aligned evidence).
- Consequence: The Beta-Bernoulli equivalence remains exact for binary observations (test pass/fail is not goal-conditioned). It degrades for continuous or interpreted observations.

**#strategy-persistence-schema** (degraded sector parameter):
- Error: $\alpha_\Sigma^{\text{eff}} \leq \alpha_\Sigma^{\text{clean}} - O(\kappa^2)$ (the squared dependence arises because the bias must both enter the signal and survive the sector-condition averaging).
- Behavior: Persistence still holds at a stricter threshold. The required tempo increases as $1/(1 - O(\kappa^2))$.
- Consequence: Class 2 agents need faster correction rates to achieve the same persistence guarantees, or equivalently, they tolerate lower strategic disturbance rates.

### 5.3 Where Ambiguity Matters

A crucial insight: the impact of $\kappa$ on approximation quality is **modulated by observation ambiguity**. Binary, verifiable observations (test results, deployment outcomes, measurable metrics) carry minimal goal-conditioning bias because the observation's meaning is not interpretation-dependent. Ambiguous observations (code quality assessments, strategic intelligence, user feedback) carry maximal bias because their interpretation depends heavily on the agent's goals and priors.

This suggests a practical rule: **the approximation error of Section II results for Class 2 agents is proportional to $\kappa \times \text{ambiguity}$, not to $\kappa$ alone.** In domains with low observation ambiguity (software with good tests, manufacturing with precise sensors), Section II results are good approximations even for fully merged agents. In domains with high observation ambiguity (organizational strategy, intelligence analysis), the approximation degrades severely.

---

## 6. Modified Results for Class 2 Agents

### 6.1 Orient Cascade Replacement: Coupled Resolution

The sequential orient cascade:

$$\delta_{\text{epistemic}} \to \delta_{\text{sat}} \to \delta_{\text{regret}} \to \delta_{\text{strategic}} \to O_t \text{ revision}$$

is replaced by a **coupled resolution** process:

*[Discussion (coupled-resolution)]*

$$X^{(\text{post})} = f_X(X^{(\text{pre})}, e_\tau)$$

followed by post-hoc diagnostic decomposition:

1. **Identify** the epistemic and purposeful components of $X^{(\text{post})}$ — what does the agent now believe, and what does it now intend?
2. **Evaluate** $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$ from the (goal-conditioned) post-update state
3. **Apply** the 2x2 diagnostic table
4. **If** the diagnostic indicates strategy revision: revise through a second coupled update (the agent re-processes the situation with attention to strategic alternatives)
5. **If** the diagnostic indicates objective revision: flag for explicit deliberation (not automatic — require justification)

The diagnostic framework survives; the causal derivation of the ordering does not. The ordering becomes a normative design pattern ("check if the model is adequate before concluding the goal is infeasible") rather than a logical consequence of information dependency.

### 6.2 Strategy-DAG Credence Conditioning

For Class 2 agents, edge credences and leaf credences are conditioned on the full state:

$$p_v(X_t) = \Pr(\text{action } v \text{ succeeds at } \tau_v \mid X_t)$$

$$p_{ij}(X_t) = \text{Cr}_i(j \text{ advances} \mid i \text{ completed}, X_t)$$

The practical consequence: credences may be *goal-dependent*. The agent assessing "will this test pass?" while pursuing "ship the feature today" may assess differently than when pursuing "achieve 100% test coverage." This is not a theoretical failure — it is a description of how LLM agents actually behave.

**Mitigation**: For LLM agents operating through a tool-use loop, the *tool results* are goal-independent (the test either passes or fails regardless of what the agent wants). The goal-conditioning enters through *interpretation* of results, not through the results themselves. This means the leaf credences for action nodes are approximately goal-independent (the action either succeeds or doesn't), while internal node credences (combining results into strategic assessments) are more goal-conditioned.

### 6.3 Strategic Calibration Under Coupling

The edge residual becomes:

$$r_{ij}^{\text{coupled}} = \mathbb{E}[\Delta V_O \mid \text{edge traversed}, X_t] - \Delta V_O^{\text{observed}}$$

The conditioning on $X_t$ (rather than $M_t$) means the residual is measuring calibration of the coupled system, not of the strategy alone. The aggregate $\delta_{\text{strategic}}$ is still meaningful — it measures "how well is the strategy working?" — but it cannot cleanly separate "the causal model is wrong" from "the beliefs are biased by goals."

---

## 7. Minimal Viable Coupled Formulation for 03-logogenic-agents/

Based on this analysis, the minimum new content needed for `03-logogenic-agents/` to have a coherent theory:

### 7.1 New Definitions (3 segments)

**D1: Logogenic agent as AAD agent** (#ai-agent-as-act-agent — already planned). Define the LLM-in-loop as an actuated agent. Map: context window → $X_t$, prompt → $e_\tau$, response → $a_t$, tool results → $o_{t+1}$.

**D2: Context turnover** (#context-turnover — already planned). Formalize the 100% $M_t$ reset per session. The LLM agent has no persistent internal state between sessions; $M_t$ is reconstructed from external memory and the current prompt.

**D3: Coupled update dynamics** (NEW). The logogenic-specific formulation:

$$X_{\tau^+} = f_{\text{LLM}}(\text{prompt}(X_{\tau^-}, e_\tau))$$

where $\text{prompt}(\cdot)$ assembles the context window from the prior state and the new observation. This is the coupled $f_X$ made concrete for the LLM architecture. The key property: the forward pass is a *single computation* that simultaneously produces updated beliefs and strategic assessments. There is no internal sequential cascade.

### 7.2 New Results (3 segments)

**R1: Section II survival classification** (this spike, promoted to a segment). State which results survive exactly, approximately, and which require modification. This is the bridge between Section II and the logogenic formulation.

**R2: Coupled diagnostic framework.** Formalize the post-hoc diagnostic decomposition: given the coupled update output, how to extract $\delta_{\text{sat}}$, $\delta_{\text{regret}}$, and $\delta_{\text{strategic}}$ and apply the $2 \times 2$ diagnostic. State the conditions under which the sequential cascade is a good approximation of the coupled resolution (low ambiguity, low $\kappa$).

**R3: External memory as persistent $M_t$** (#m-preservation — already planned). The mechanism by which $M_t$ survives context turnover: file-backed memory, retrieval-augmented generation, structured state stores. This is the logogenic analog of the persistence condition — not "does $M_t$ remain bounded?" but "can $M_t$ be reconstructed after a context reset?"

### 7.3 New Scope Conditions (1 segment)

**S1: Observation ambiguity modulation.** Formalize the insight from Section 5.3: the approximation quality of Section II results for Class 2 agents depends on $\kappa \times \text{ambiguity}$, not on $\kappa$ alone. State the conditions under which a Class 2 agent can be analyzed using (most of) Section II's machinery without modification.

### 7.4 Total: 7 segments minimum

Three definitions (D1, D2, D3), three results (R1, R2, R3), one scope condition (S1). This is a minimal skeleton, not a complete theory. It would fill the three named gaps (#ai-agent-as-act-agent, #context-turnover, #m-preservation) plus four new segments addressing the coupled formulation.

---

## 8. The Language-Specific Orient Cascade

The key question from `03-logogenic-agents/OUTLINE.md`: "Language-specific orient cascade — what's specific to logogenic agents?"

### 8.1 The Forward Pass as Simultaneous Update

An LLM processes a prompt in a single forward pass. The attention mechanism processes all tokens together — goals, observations, beliefs, strategy — without a sequential factorization. This means:

- There is no "epistemic update first, then strategic evaluation." There is a single computation that produces a response, which may contain updated beliefs, strategic assessments, action choices, and objective evaluations all at once.
- The "cascade" is not sequential but **implicit in the token-generation process**. The LLM's autoregressive generation can be viewed as an approximate fixed-point iteration: each token conditions on all previous tokens (including those expressing beliefs, strategies, and evaluations), progressively refining the coupled state.
- Chain-of-thought reasoning is the closest analog to the sequential cascade. When the LLM explicitly reasons step-by-step ("First, let me understand the situation... Now, given that, what's my best approach... Actually, wait, that goal seems infeasible..."), it is *implementing an approximate cascade in language*. The cascade's ordering becomes a property of the reasoning trace, not of the underlying architecture.

### 8.2 What's Specific to Logogenic Agents

Three things are specific to agents whose processing is constituted in language:

**1. The cascade is a reasoning pattern, not an architectural constraint.** A modular agent (Kalman filter + LQR) has directed separation by construction — the architecture *forces* the correct ordering. An LLM agent can implement the cascade ordering by choosing to reason in the right order, but nothing in its architecture prevents it from, say, revising its objective before adequately updating its model. The cascade's normative ordering must be *prompted* or *trained into* the agent, not assumed.

**2. Epistemic states are expressed in language, not in parameter space.** The LLM's "beliefs" are not probability distributions over a state space — they are linguistic representations that *encode* probabilistic judgments. The mismatch signal is not a numerical residual but a *felt sense of surprise* expressed in language ("That's unexpected — I thought the auth module was stable"). The gain is not a computed ratio but a *judgment of credibility* ("This is from the CI pipeline, which is reliable, so I should take it seriously"). The theory's quantities exist but are estimated through linguistic reasoning, not numerical computation.

**3. The observation channel is linguistic.** The LLM agent's observations are text (tool outputs, user messages, file contents). The observation function $h$ maps environment states to linguistic descriptions, which introduces a layer of representation that does not exist for numerical observers. Ambiguity in the linguistic observation channel is a dominant source of goal-conditioning: the same text can be interpreted differently depending on the agent's goals (reading code with "fix the bug" vs "add logging" goals).

### 8.3 The Logogenic Orient Cascade (Sketch)

*[Discussion (logogenic-orient-cascade)]*

For a logogenic agent, the orient cascade is replaced by a **reasoning discipline** — a learned or prompted pattern of deliberation that approximates the cascade's logical structure:

1. **State the observation clearly** (what did I just learn?)
2. **Update beliefs explicitly** (what do I now think is true about reality?)
3. **Assess feasibility** (is my goal still achievable given updated beliefs?)
4. **Evaluate strategy** (is my current approach still the best one?)
5. **Decide whether to act, explore, or deliberate further**

This is the cognitive loop from `msc/agentic-tft-cognitive-loop-spec.md` (PERCEIVE → CONTEXTUALIZE → CHOOSE → EFFECT) instantiated as a reasoning pattern. The four-phase loop maps onto the cascade:

| Cognitive Loop Phase | AAD Cascade Step | What Happens for LLM Agent |
|---------------------|------------------|---------------------------|
| PERCEIVE | (input) | New token(s) enter context window |
| CONTEXTUALIZE (predict) | Reduce $\delta_{\text{epistemic}}$ | "What was I expecting? How does this differ?" |
| CONTEXTUALIZE (assess) | Evaluate $\delta_{\text{sat}}$ | "Is my goal still feasible?" |
| CHOOSE | Evaluate $\delta_{\text{regret}}$, $\delta_{\text{strategic}}$ | "Is my approach working? Should I try something different?" |
| EFFECT | Action | Tool call, message, or internal deliberation |

The key difference from Section II's cascade: for a logogenic agent, **the quality of the cascade depends on the quality of the reasoning**, not on the architecture. A well-prompted LLM agent can implement a high-fidelity cascade; a poorly prompted one may skip steps or get the ordering wrong. The cascade becomes a **competency** rather than a **guarantee**.

### 8.4 Chain-of-Thought as Approximate Cascade

Chain-of-thought reasoning is the mechanism by which an LLM approximates the sequential cascade within a single generation:

- The early tokens in a reasoning trace tend to address "what is happening?" (epistemic update)
- Middle tokens tend to address "what does this mean for my plan?" (strategic evaluation)
- Late tokens tend to address "what should I do?" (action selection)

This ordering is not guaranteed — it is a statistical tendency shaped by training data. When the LLM encounters a highly goal-relevant observation, the ordering may be disrupted: the agent jumps directly to strategic evaluation before adequately processing the epistemic content. This is the computational analog of motivated reasoning — and it is the mechanism by which $\kappa_{\text{processing}} \approx 1$ manifests in practice.

**Training implication**: An LLM agent trained to follow the cascade ordering explicitly (e.g., through structured reasoning templates that separate epistemic update from strategic evaluation) would approximate a partially modular architecture (Class 3) at the behavioral level, even though its processing architecture is Class 2. The residual $\kappa_{\text{processing}}$ would reflect the training's success at instilling the cascade discipline, not the architecture's inherent coupling.

---

## 9. Open Questions

1. **Can $\kappa_{\text{processing}}$ be measured for specific LLM agents?** In principle, it requires measuring $I(G_t; M_{\tau^+} \mid e_\tau, M_{\tau^-})$ — the mutual information between goals and the epistemic update, conditioned on the observation and prior state. This is not computable in closed form for transformer architectures. Empirical proxies: run the same observation through the agent with different goals and measure how much the "epistemic" portion of the response changes.

2. **Is the $\kappa \times \text{ambiguity}$ modulation the right structure?** The claim that observation ambiguity modulates the impact of coupling is plausible but not derived. It needs formal treatment — possibly through the information geometry of the observation channel.

3. **What is the correct fixed-point characterization of the coupled update?** The sequential cascade is a unique resolution order. The coupled update may have multiple fixed points (the agent could converge to different belief-strategy pairs depending on initialization). Uniqueness conditions for the coupled fixed point would be important for the theory's predictive power.

4. **Does chain-of-thought training actually reduce effective $\kappa$?** If structured reasoning can make a Class 2 agent behave like a Class 3 agent, this has both theoretical implications (the architectural classification becomes partly behavioral) and practical implications (training methodology for better epistemic discipline).

5. **What is the strategy persistence condition for an agent with 100% context turnover?** The standard persistence condition assumes continuous state evolution. An agent that resets $X_t$ every session faces a qualitatively different persistence problem: not "can the correction rate outpace disturbance?" but "can the state be reconstructed from external memory with bounded error?"

---

## 10. Conclusion

The survival analysis reveals a surprisingly optimistic picture for applying AAD's Section II to Class 2 agents:

**The definitions survive.** The conceptual architecture — $X_t = (M_t, G_t)$, $G_t = (O_t, \Sigma_t)$, $V_{O_t}$, $\Sigma_t$ as DAG, satisfaction gap, control regret — is intact. These are about the *structure* of purposeful agency, not about the *processing architecture*.

**The structural results survive.** Causal hierarchy requirement, loop interventional access, chain confidence decay, observability dominance, credit assignment boundary, structural change as parametric limit — all architecture-independent.

**The processing results degrade gracefully.** The orient cascade, edge updates, strategic calibration, and strategy persistence degrade with $\kappa_{\text{processing}}$. The degradation is modulated by observation ambiguity — verifiable, unambiguous observations limit the damage from goal-conditioned processing.

**One result fails by definition** — directed separation itself.

The minimal coupled formulation for `03-logogenic-agents/` requires approximately 7 new segments: 3 definitions, 3 results, and 1 scope condition. The language-specific orient cascade is best understood as a *reasoning discipline* that approximates the cascade's logical structure, with quality depending on training and prompting rather than architecture.

The deepest insight: for Class 2 agents, the cascade ordering transitions from a *derived consequence* of directed information dependency to a *normative design pattern* that must be enforced through training, prompting, or system-level architecture (e.g., separating observation processing from strategy evaluation at the system level, even though the LLM component is internally merged). This is the bridge between AAD's mathematical core and the engineering of logogenic agent systems.
