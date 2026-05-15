# DAG Boundary Type Closure (v2)

**Goal**: Close the two undefined interfaces at the strategy DAG's boundaries — leaf base credence (p_v) and the terminal-objective interface — so that the Section II object model is fully well-typed.

**Status**: Working spike, v2. Revised after Codex review that caught: (1) conflation of δ_sat with terminal misalignment detection, (2) "implicit φ" doesn't close the type boundary, (3) temporal indexing of p_v is load-bearing, (4) terminal-condition construction needs scoping to threshold objectives.


## 1. The Problem

The strategy DAG has well-defined *interior mechanics*: edge credences, AND/OR combination rules, status propagation, chain confidence decay. But both boundaries are formally undefined:

**Bottom (leaves)**: The status propagation formula uses $p_v$ for leaf nodes without defining it. The propagation builds upward from these base cases. Undefined base cases make the entire computation ill-founded.

**Top (terminals)**: Terminal nodes represent "objective achieved" conditions.
The rootedness constraint connects every node to a terminal. But: O_t lives outside Σ_t (strategy-dimension), terminal nodes live inside Σ_t (strategy-dag). What is the formal interface? If terminals encode O_t, then Σ_t contains O_t, blurring the split. If they don't, what constrains them?

Both gaps are load-bearing. The orient cascade flows through them:

    M_t update → leaf p_v changes → status re-propagation
              → terminal credences change → strategy self-assessment → comparison with δ_sat / δ_regret → possible revision

The boundary interfaces sit at the entry and exit of this flow.


## 2. Leaf Base Credence

### The definition

Each leaf node v represents either an action the agent can take or a condition the agent can observe (from strategy-dag's source constraint). The base credence is the agent's assessment of leaf achievability at the node's temporal position:

$$p_v(M_t) = \begin{cases}
  \Pr(\text{action } v \text{ succeeds at } \tau_v \mid M_t)
    & \text{if } v \text{ is an action node} \\[4pt]
  \Pr(C_v(\tau_v) \mid M_t)
    & \text{if } v \text{ is a condition node}
\end{cases}$$

where:
- $C_v$ is the propositional condition associated with node $v$
- $\tau_v$ is the node's temporal position (already present in the DAG via the acyclicity derivation — each node represents a future event with $\tau_v \gt t$)

Key properties:

1. **Grounded in M_t.** Both forms are conditional on M_t — they are epistemic assessments that update whenever M_t updates. This is what connects the DAG to Section I's adaptive machinery.

2. **Two types, same treatment.** For action leaves, p_v is *capability credence* — "can I do this?" For condition leaves, p_v is *state credence* — "will this be true?" Both are epistemic quantities with the same formal role (base cases for propagation) and the same update mechanism (M_t revision → p_v revision).

3. **Temporally indexed.** $p_v$ is about the condition at $\tau_v$, not at $t$. For near-future nodes ($\tau_v \approx t$), the distinction is minor. For far-future nodes, $p_v$ incorporates the agent's model of how states evolve — which lives in $M_t$. This means p_v for distant leaves is more uncertain (M_t's state predictions degrade with horizon), which is correct: far-future plans should have lower base confidence.

### What this is

**Formulation.** The definition is a representational choice: we parameterize leaf credences as M_t-conditional, temporally-indexed probabilities. The probabilistic form is consistent with (not additional to) the existing DAG formalism, which already assumes edges carry probabilities (Cox's theorem). The temporal indexing is consistent with the acyclicity derivation, which already assigns each node a temporal position.

### What this buys

- The status propagation formula is now well-defined from base cases through terminals
- The orient cascade's first propagation step (M_t → p_v → forward pass) becomes concrete
- The connection to #der-observability-dominance is tightened: high obs noise on a leaf → M_t poorly informed about C_v → p_v unreliable → but p_v is still the agent's best estimate given M_t. Observability affects the *accuracy* of p_v (whether it tracks reality), not its *definition*
- Far-future leaves naturally have lower confidence, creating pressure toward shorter or more robust strategies (consistent with #der-chain-confidence-decay)


## 3. Terminal-Objective Interface

### The problem, precisely stated

O_t defines V_O: trajectories → ℝ. Σ_t's terminal nodes carry conditions {C_v}. What formal relation constrains these conditions to be meaningful operationalizations of O_t?

Saying "the relation is implicit in Σ_t's structure" (the v1 approach) doesn't close the boundary — it restates the gap as a feature. We need an explicit well-formedness constraint: a formal statement of when a set of terminal conditions is an admissible operationalization of the current O_t.

### Well-formedness constraint

*[Definition (terminal-well-formedness)]*

$\Sigma_t$ is **$O_t$-well-formed** if:

$$\Pr\!\left(V_{O_t}(\tau) \geq V_{O_t}^{\min}
  \;\middle|\; \text{terminal conditions achieved},\; M_t\right) \geq 1 - \epsilon$$

where "terminal conditions achieved" means the conjunction/disjunction of terminal predicates as composed through the DAG's AND/OR structure near the terminals.

Properties:

1. **Not a separate state object.** This is a constraint on the relationship between Σ_t and O_t — a well-formedness condition on the strategy, not a new component of G_t. φ: O_t → terminals is not stored separately; it is the projection of strategy construction onto terminal selection. The well-formedness constraint is explicit and in-principle assessable, though evaluating it requires the same value-side machinery as A_O — it is not a cheap structural test.

2. **Conditional on M_t.** The agent's assessment of whether its terminals operationalize O_t depends on what it knows about the world. Better M_t → better assessment of terminal adequacy.

3. **Falsifiable through experience.** The agent believes its terminals operationalize O_t. Reality may disagree. When the agent achieves its terminal conditions and evaluates V_O on the resulting trajectory, it discovers whether the well-formedness belief was justified.

4. **Triggers structural change.** When O_t changes, well-formedness must be re-evaluated. If the new O_t makes current terminals inadequate, the agent must construct new terminals — this is the "objective revision → change terminal nodes" operation from #form-structural-change-as-parametric-limit.

### Scope of the terminal-condition construction

Terminal conditions are the agent's **operational success criteria** — a Boolean decomposition of "good enough" relative to V_O. This construction works naturally for:

- **Constraint satisfaction**: terminal per constraint (pass/fail)
- **Threshold objectives**: terminal = "value exceeds threshold"
- **Composite objectives**: AND-nodes for conjunction, OR-nodes for disjunction

It works less naturally for:

- **Pure utility maximization** without threshold: what counts as "success"?
  The agent must set an operational threshold ("good enough") and decompose it into Boolean conditions. This is an approximation — the DAG discretizes a continuous objective.
- **Continuous-valued trajectory functionals**: satisfaction is a matter of degree, not Boolean. The terminal construction imposes a threshold that may not exist in V_O.

The terminal conditions are a **useful operational proxy** for V_O, not the sole interface between O_t and Σ_t. The primary O_t ↔ theory interface remains V_O through the value object ( #def-value-object). The terminal conditions are Σ_t's internal encoding of what V_O requires — an encoding that (a) enables Boolean status propagation through the DAG, and (b) may be incomplete or wrong.

### Ill-formedness modes

When the well-formedness constraint is violated:

1. **Terminal misalignment**: achieving all terminals but V_O < V_min. The terminals don't capture what O_t actually requires. Example: all tests pass and code is deployed, but the feature doesn't solve the user's problem.

2. **Terminal incompleteness**: V_O requires conditions not represented in any terminal. Example: deployment succeeds but documentation wasn't included, which the objective implicitly required.

3. **Terminal over-specification**: terminals are stricter than V_O requires. The agent works harder than needed. Not a failure mode, but an efficiency concern.


## 4. Strategy Self-Assessment vs. Satisfaction Gap

### The critical distinction (v1 collapsed these)

The v1 spike conflated two quantities:

- **$\hat P_\Sigma$**: the strategy's self-assessed success probability (from status propagation through the DAG)
- **$A_O$**: the best achievable value across the entire policy class (from the satisfaction gap definition)

These are fundamentally different:

| Quantity | Definition | Scope | Computed from |
|----------|-----------|-------|---------------|
| $\hat P_\Sigma(M_t)$ | Combined terminal credence | Current strategy Σ_t | DAG status propagation |
| $A_O(M_t; \Pi, N_h)$ | $\sup_\pi V_O(M_t, \pi; N_h)$ | All policies in Π | Optimization over policy class |
| $V_O(M_t, \pi_\text{curr}; N_h)$ | Expected value under current policy | Current policy | Forward evaluation |

### $\hat P_\Sigma$ — the strategy's self-assessment

*[Definition (strategy-self-assessment)]*

$$\hat{P}_\Sigma(M_t) = s_\text{root}$$

where $s_\text{root}$ is the status of a unique root terminal in $\Sigma_t$.

**Unique-root requirement.** $\Sigma_t$ has exactly one sink node $v_\text{root}$ (out-degree 0). When the objective has multiple components, they feed into $v_\text{root}$ through AND/OR combination within the DAG. This is a structural constraint on well-formed strategies, consistent with scalar $V_O$ ( #form-objective-functional): if the objective produces a single evaluation, the strategy should have a single top-level success node. Agents with compound objectives express the combination structure (conjunctive, disjunctive, or mixed) through the DAG's existing AND/OR machinery in the layers immediately below $v_\text{root}$, not through an external aggregation operation.

$\hat P_\Sigma$ answers: "according to my strategy's own model of causation, what is my probability of achieving the terminal conditions?"

This is a **strategy-internal** quantity. It can be computed efficiently ($O(|V| + |E|)$ forward pass) and updates whenever M_t changes (through leaf credences) or when edge credences are revised.

### Diagnostic landscape (corrected)

The existing gap measures and $\hat P_\Sigma$ form a richer diagnostic system than either alone:

| Signal pattern | Interpretation | Action |
|---------------|---------------|--------|
| $\hat P_\Sigma$ high, $\delta_\text{sat} \leq 0$, $\delta_\text{regret} \approx 0$ | Strategy is good, objective achievable, near-optimal | Continue |
| $\hat P_\Sigma$ high, $\delta_\text{regret} \gg 0$ | DAG overconfident — edges or leaves are miscalibrated | Calibrate via #def-strategic-calibration |
| $\hat P_\Sigma$ low, $\delta_\text{sat} \leq 0$ | Objective is achievable but current strategy is pessimistic or weak | Revise Σ_t |
| $\hat P_\Sigma$ high, $\delta_\text{sat} \gt 0$ | DAG thinks it will succeed but even the best policy can't achieve V_min — M_t may be wrong about feasibility, Π may be too narrow, N_h too short, or goal genuinely infeasible | Check M_t, Π, N_h, then consider O_t revision |
| Terminals achieved, $V_O \lt V_\text{min}$ | **Terminal alignment error** — operational criteria don't match objective | Revise terminal conditions (structural Σ_t change) |

The last row is the specific failure mode where well-formedness was believed satisfied but turns out to be violated. It is detectable only through **experience** — the agent achieves its plan and evaluates V_O on the actual trajectory. No a priori gap measure (δ_sat, δ_regret, δ_strategic) catches this directly; it requires post-achievement evaluation.

### What $\hat P_\Sigma$ is NOT

$\hat P_\Sigma$ is not an estimate of $A_O$. $A_O$ optimizes over the entire policy class; $\hat P_\Sigma$ evaluates the single current strategy. The gap $A_O - V_O(\pi_\text{curr})$ is δ_regret's territory. The gap between $\hat P_\Sigma$ and the actual trajectory value after execution is a calibration question — does the DAG's self-assessment match reality?

$\hat P_\Sigma$ is the strategy's **internal consistency check**: given my leaf beliefs and edge beliefs and combination structure, does my plan think it will work? It is useful precisely because it is cheap to compute and updates in real time as M_t changes, unlike A_O which requires optimization.


## 5. The Orient Cascade Made Concrete

With both interfaces defined, the cascade's flow through the DAG becomes fully specified:

**Step 1: Epistemic update (Section I)** New observation arrives. M_t updates via mismatch signal and gain.

**Step 2: Leaf credence update (bottom interface)** Updated M_t → revised $p_v(M_t)$ for affected leaves.
- "Can I still execute action X at time τ_v?" (capability credence)
- "Will condition Y hold at time τ_v?" (state credence)

**Step 3: Status re-propagation** Forward pass through the DAG in topological order. $O(|V| + |E|)$. New leaf credences flow upward through edges and AND/OR gates. $\hat P_\Sigma$ updates.

**Step 4: Edge credence update** For edges whose consequences were observed, update p_ij via the gain principle ( #hyp-edge-update-via-gain). This happens in parallel with or after status propagation — the edge update uses the new M_t plus the observation.

**Step 5: Strategy self-assessment** Read off $\hat P_\Sigma$ from the propagated terminal credences. This is the strategy's own verdict on its chances.

**Step 6: Compute δ_sat and δ_regret (policy-class level)** These require the full value machinery (V_O evaluation, A_O computation) and are more expensive than the DAG propagation. They may be computed less frequently than $\hat P_\Sigma$.

**Step 7: Diagnostic triage** Use the diagnostic table from §4 to determine corrective action.

**Step 8: If needed, structural revision**
- δ_regret high → revise edges, prune/graft branches
- δ_sat > 0 persists → check well-formedness, then consider O_t revision
- Terminal alignment error (from past experience) → revise terminal conditions


## 6. What's Derived vs. Formulation Choice

| Element | Status | Justification |
|---------|--------|---------------|
| p_v is conditional on M_t | Derived | p_v is an epistemic assessment; epistemic state IS M_t |
| p_v is temporally indexed at τ_v | Derived | Nodes already have temporal positions (acyclicity); leaf conditions refer to future states |
| p_v is probabilistic | Consistent | DAG already uses probabilities; Cox's theorem |
| p_v splits into capability/state | Formulation | Follows from source constraint (leaves are actions or conditions) |
| Well-formedness constraint | Formulation | The NEED for a constraint is derived (O_t/Σ_t split requires a formal interface); the specific form (Pr ≥ 1-ε) is a formulation choice |
| $\hat P_\Sigma$ as separate quantity from A_O | Derived | Different computation, different scope, different information. Conflating them is a type error. |
| Terminal conditions as Boolean proxies for V_O | Formulation | Works for threshold/constraint objectives. For continuous V_O, it's an approximation that introduces a discretization threshold. |
| Terminal alignment error as experience-only signal | Derived | No a priori gap measure can detect wrong operationalization — you must achieve the terminals and evaluate V_O to discover the mismatch. |
| φ is not a separate state object | Design decision | Parsimony — φ is a projection of Σ_t's terminal structure. Well-formedness constraint is explicit instead. |


## 7. Proposed Edits to strategy-dag.md

### Add to Formal Expression (after structural constraints, before edge semantics):

**Leaf base credence.** For each leaf node $v \in V_t^{\text{leaf}}$, the base credence used in status propagation:

$$p_v(M_t) = \begin{cases}
  \Pr(\text{action } v \text{ succeeds at } \tau_v \mid M_t)
    & \text{if } v \text{ is an action node} \\[4pt]
  \Pr(C_v(\tau_v) \mid M_t)
    & \text{if } v \text{ is a condition node}
\end{cases}$$

where $C_v$ is the propositional condition associated with node $v$ and $\tau_v$ is the node's temporal position (from the acyclicity structure). Both forms are conditional on $M_t$ — they are epistemic assessments that update whenever $M_t$ updates. This is the mechanism by which Section I's adaptive machinery enters the strategy: M_t changes → leaf credences change → status propagation produces new terminal credences.

### Add to Formal Expression (after status propagation):

**Terminal satisfaction conditions.** Terminal nodes $V_t^{\text{term}} = \{v \in V_t : \text{out-degree}(v) = 0\}$ carry **satisfaction conditions**: predicates on environment states/trajectories that the agent treats as operational success criteria for the objective.

**Well-formedness.** $\Sigma_t$ is **$O_t$-well-formed** when the agent believes that achieving the terminal conditions (as composed through the DAG's AND/OR structure) yields objective satisfaction:

$$\Pr\!\left(V_{O_t}(\tau) \geq V_{O_t}^{\min}
  \;\middle|\; \text{terminals achieved},\; M_t\right) \geq 1 - \epsilon$$

This is a constraint on the relationship between $\Sigma_t$ and $O_t$, not a separate state object. When $O_t$ changes, well-formedness must be re-evaluated; violation triggers terminal reassessment ( #form-structural-change-as-parametric-limit).

**Unique root.** Well-formed strategies have exactly one sink node $v_\text{root}$. Compound objectives express their combination structure (conjunctive, disjunctive, or mixed) through the DAG's AND/OR machinery in the layers below $v_\text{root}$, not through external aggregation. This is consistent with scalar $V_O$ ( #form-objective-functional).

**Strategy self-assessment.** The root node's propagated status:

$$\hat{P}_\Sigma(M_t) = s_{v_\text{root}}$$

is the strategy's self-assessed success probability — the DAG's own answer to "will this plan work?" This is explicitly distinct from $A_O$ (which optimizes over the entire policy class) and from $V_O(\pi_\text{current})$ (which evaluates the current policy). $\hat P_\Sigma$ is cheap to compute ($O(|V| + |E|)$) and updates in real time as $M_t$ changes.

**Scope.** The terminal-condition construction works naturally for threshold, constraint, and composite objectives (Boolean decomposition via AND/OR). For continuous-valued objectives without natural thresholds, the agent must set an operational threshold — introducing a discretization that is a practical proxy, not a lossless encoding of $V_O$. The primary O_t ↔ theory interface remains $V_O$ through the value object ( #def-value-object); terminal conditions are Σ_t's internal encoding, which may be incomplete or misaligned.

### Replace Working Notes:

Remove the two Working Notes about p_v and O_t ↔ terminal interface. Add:

- **Terminal alignment error.** When the agent achieves its terminal conditions but evaluates $V_O(\tau) \lt V_{O_t}^{\min}$ on the actual trajectory, the well-formedness belief was wrong. This is detectable only through experience, not through a priori analysis. It triggers terminal reassessment — a structural change in $\Sigma_t$ driven by the O_t ↔ terminal mismatch.


## 8. Open Questions (post-closure)

1. **ε in the well-formedness constraint.** What determines an acceptable ε?
   Is it fixed, agent-specific, or objective-specific? A military operation might require ε ≈ 0 (terminals must guarantee success); a startup might accept ε ≈ 0.5 (terminals represent a reasonable bet). This may connect to the risk-sensitivity of the objective.

2. **Terminal alignment error as a formal signal.** Currently unnamed in the diagnostic apparatus. Could be defined as $\delta_\text{align} = V_{O_t}^{\min} - V_{O_t}(\tau_\text{achieved})$ when all terminal conditions are met. Positive means the terminals were insufficient. This would complement δ_sat, δ_regret, and δ_strategic as a fourth diagnostic. Whether it's worth formalizing depends on how often terminal misalignment is the binding failure mode in practice.

3. **Multiple independent objectives.** If O_t has genuinely independent components (see #form-objective-functional's scalar scope restriction), the terminal structure needs corresponding independence. This works naturally with the AND/OR machinery (independent objective components as separate terminal subtrees) but hasn't been formally verified.

4. **Leaf credence under deep planning.** For far-future leaves, $p_v = \Pr(C_v(\tau_v) \mid M_t)$ degrades with $|\tau_v - t|$ because M_t's state predictions are less reliable over long horizons. Does this create systematic underconfidence in long-range strategies? Or is this appropriate conservatism? Connects to #der-chain-confidence-decay: the decay from far-future leaf uncertainty compounds with the decay from edge uncertainty.

5. **Well-formedness vs. terminal alignment error.** Well-formedness is the agent's ex ante belief; terminal alignment error is the ex post discovery. Can the agent improve its well-formedness assessments over time (learn what makes good terminals for a given type of O_t)? This is meta-learning about strategy construction — possibly relevant for agents with many repeated objectives.
