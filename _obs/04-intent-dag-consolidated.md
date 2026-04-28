# Intent DAG: Consolidated Formalism

**Status**: Synthesis of three independent formalism attempts (track-a/00, track-a/02, track-a/03) plus the founding sketch (scratch/03). States what's settled, frames what's open. This is the canonical reference for future work on AAD's purposeful agency layer.

**Epistemic status**: The settled core is **[Plausible]** — structurally motivated, converged across independent attempts, internally consistent. The predictions are **[Speculative]** — non-obvious consequences that haven't been empirically tested. Open decisions are genuine design freedom, not gaps in understanding.

---

## 1. Formal Objects

AAD's agent state has three components:

- **M_t** — reality model. The agent's compressed representation of how the world works. TFT (now absorbed into AAD) formalizes this completely: mismatch signal δ_t, update gain η*, adaptive tempo T, persistence condition.

- **O_t** — objective. What the agent wants. A target state, region, or condition in state space S. The port. Simple object. The PID has this (setpoint r_t). The Kalman filter does not.

- **Σ_t** — strategy. How the agent plans to get from current reality to O_t. A probabilistic causal DAG encoding the agent's theory of how its actions will produce goal-achievement. Complex object. The commander has this. The PID does not.

These relate via **directed separation** (P6):
- M_t dynamics can be designed independently of O_t and Σ_t
- O_t is independent of M_t (what you want doesn't depend on what you know)
- Σ_t depends on both M_t (what's feasible) and O_t (what you're aiming at)
- Action selection couples all three: a_t = π(M_t, O_t, Σ_t)

The old symbol G_t conflated O_t and Σ_t. Documents using G_t as a point in state space are superseded. The expression δ_goal = G_t − M_t is a type error — Σ_t is a graph, not a point. See DP-8 for what replaces it.

---

## 2. The Strategy DAG

**Definition.** The strategy is a directed acyclic graph:

    Σ_t = (V_t, E_t, p_t, γ_t, props_t)

where:
- V_t: set of propositional nodes (things that could be true or false)
- E_t ⊆ V_t × V_t: directed causal edges
- p_t : E_t → [0,1]: causal confidence weight per edge
- γ_t : V_t → {AND, OR}: combination rule per node (see §3)
- props_t : V_t → properties: per-node properties (see DP-1)

**Structural constraints:**
1. **Acyclicity.** Σ_t is a DAG. (This is a modeling assumption with limited scope — see DP-9.)
2. **Rootedness.** Every node has a directed path to at least one terminal (objective) node.
3. **Source constraint.** Leaf nodes are actions the agent can take or conditions the agent can observe.

### 2.1 Edge Semantics

Each edge carries a single causal confidence weight:

    p_ij = P(j advances toward true | do(i), M_t)

This is **interventional** (Pearl Level 2 — do-calculus), not merely associational. The agent's belief is: "if I make i happen, j becomes more likely with probability p_ij, given my current understanding of reality."

**Critical caveat (from review).** The edges claim interventional semantics but the update rule (§5) uses observational signals. This is valid when:
- The agent actually performed intervention i and observed the outcome (genuine experiment — available in software via tests, deploys, git bisect)
- Confounding is negligible (the agent's action was the only relevant cause)
- Identifiability assumptions hold (no unmeasured common causes of i and j)

In domains where evidence is confounded, delayed, or correlated (military, organizational), the edge weights are semantically weaker — they encode the agent's best causal belief, but that belief may be systematically biased by observational confounding. See DP-6 for the identifiability question.

### 2.2 Why Single-Parameter Edges

The first formalism attempt (track-a/00) used two parameters per edge:
(p_ij, θ_ij) where θ was "contribution magnitude." This was dropped because explicit AND/OR combination rules at nodes absorb θ's role. The complexity budget goes to one bit per node (AND vs OR) instead of one float per edge.

---

## 3. Combination Rules (Settled)

Each non-leaf node v has a combination type γ(v) ∈ {AND, OR}.

**AND-node** — all parents must succeed (conjunctive):

    P(v | parents) = ∏_{i ∈ pa(v)} p_iv · P(i)

Appropriate when v requires every parent contribution. "Backend AND frontend AND database migration." Removing any parent makes v unachievable.

**OR-node** — any parent sufficient (disjunctive):

    P(v | parents) = 1 − ∏_{i ∈ pa(v)} (1 − p_iv · P(i))

Appropriate when v is achievable through any of several paths. "Auth via library X OR raw HTTP OR third-party service." Removing one parent still leaves other routes.

**Status propagation** — forward pass in topological order, O(|V| + |E|):

    s_v = cases:
        base confidence p_v                     if v is leaf ∏_{i ∈ pa(v)} p_iv · s_i               if γ(v) = AND 1 − ∏_{i ∈ pa(v)} (1 − p_iv · s_i)    if γ(v) = OR

**How to assign γ.** Ask the causal question: "If I remove one parent, can v still be achieved?" YES → OR. NO → AND. This is derivable from M_t's causal model — it's principled, not arbitrary. But the assignment can be wrong (false AND = pessimistic over-investment; false OR = optimistic under-investment), and should be updateable when evidence reveals the structural relationship differs from assumed.

### 3.1 Why Not Noisy-OR

The first attempt used noisy-OR universally (implicit OR for all nodes).
This **systematically overestimates conjunctive structures**:

    Example: Objective requiring 3 KRs at p = 0.95, 0.90, 0.99 Noisy-OR: P(O) = 1 − (0.05)(0.10)(0.01) = 0.99995  [absurd] AND:      P(O) = 0.95 × 0.90 × 0.99 = 0.846         [realistic]

The noisy-OR model cannot represent "all of these are required." This is the single most damaging error in the first formalism, and the primary motivation for the AND/OR revision.

### 3.2 Why Not WEIGHTED

The clean-slate variant (track-a/02) introduced WEIGHTED combination:

    P(v | parents) = min(1, Σ_{i ∈ pa(v)} α_iv · p_iv · s_i)

This handles k-of-n thresholds but reintroduces the two-parameter estimation problem (α weights suffer the same issues as the old θ). If k-of-n semantics are genuinely needed, model as nested AND/OR:

    v [AND: threshold met] ├── group_1 [OR: any k paths from n] │   ├── path_a │   └── path_b └── group_2 [OR: remaining paths]
        └── path_c

This keeps the estimation problem localized to the node taxonomy rather than spreading it across a new per-edge parameter. Net assessment: drop WEIGHTED.

---

## 4. Compound Probability Decay (Settled)

For a directed path P = (v_1, v_2, ..., v_n):

    conf(P) = ∏_{k=1}^{n-1} p_{v_k, v_{k+1}}

**Depth is fragility.** Even high per-edge confidence decays exponentially:

    | Depth | conf (p=0.9) | conf (p=0.8) |
    |-------|-------------|-------------|
    |   1   |    0.90     |    0.80     |
    |   3   |    0.73     |    0.51     |
    |   5   |    0.59     |    0.33     |
    |  10   |    0.35     |    0.11     |
    |  20   |    0.12     |    0.01     |

AND-nodes amplify this: a chain of AND-nodes with k parents each at confidence p and depth d gives P = p^(k·d), not p^d. Deep conjunctive strategies are exponentially more fragile than deep disjunctive ones.

**Assumption.** Edge failures are independent. Real systems have correlated failures (shared infrastructure, common-mode risks). Actual confidence is lower than the independent-edge formula suggests. Correlation structure is unmodeled — acknowledged as a limitation.

---

## 5. Edge Update Rule (Settled in Structure, Open in Details)

Edge weights update via TFT's uncertainty ratio principle:

    p_ij^new = p_ij^old + η_edge · (signal(o_t, i, j) − p_ij^old)

where:
- signal(o_t, i, j) ∈ [0, 1]: evidential content of observation o_t about the causal link i → j
- η_edge = U_edge / (U_edge + U_obs): update gain

    U_edge: uncertainty about this specific causal link
            If p_ij ~ Beta(α_ij, β_ij):
            U_edge = Var[Beta] = αβ / ((α+β)²(α+β+1))

    U_obs: observation noise on the channel confirming this link
           U_obs ∝ 1/σ_j (inverse of observability of node j)

**Beta-Bernoulli equivalence.** For binary observations (success/failure):
- Observe success: α_ij → α_ij + 1
- Observe failure: β_ij → β_ij + 1
- Point estimate: p_ij = α / (α + β)

**Connection to P7 (observability).** When σ_j ≈ 0: U_obs → ∞, η_edge → 0.
The edge is frozen at its prior. Unobservable links cannot be updated — this is what makes unobservable paths epistemically dead.

**What's open.** The signal function signal(o_t, i, j) is not specified. How does an observation about node j translate into evidence about edge i → j specifically? In the binary case it's clear; in continuous domains it's a proper inference problem. See DP-6.

---

## 6. Observability Dominance (Settled)

For a path P, define:

    obs(P) = min_{v ∈ P} σ_v

This is the worst observability along the path — the darkest point in the causal chain.

**Observability-adjusted confidence:**

    conf_obs(P) = conf(P) · obs(P)

**Prediction [Speculative].** Given two paths with equal nominal confidence, the agent should prefer the one with higher observability. After one attempt: the high-σ path yields large η_edge (agent quickly learns viability or redirects); the low-σ path yields tiny η_edge (agent still guessing after n attempts).

**Prediction [Speculative].** Optimal decomposition depth balances incremental confirmation (finer segments = detect failure faster) against compound decay (more segments = more uncertain links). Decompose as finely as observation channels allow, but no finer.

---

## 7. The Orient Cascade (Settled in Structure, Open in Equations)

The cascade specifies the ORDER in which updates propagate. This is the formal content of Boyd's Orient — not just model updating, but the interaction between reality-understanding and strategy.

    Step 1. Observation arrives: o_t Step 2. M_t update: δ_epistemic = o_t − ô_t; standard AAD machinery Step 3. Edge revision: for each edge (i,j) in Σ_t, update p_ij given
            the new M_t and any evidence about link i → j
    Step 4. Status propagation: recompute s_v for all nodes via §3 Step 5. Feasibility check: are terminal objectives still achievable?
            (aggregate confidence above threshold?)
    Step 6. Possible O_t revision: if feasibility fails, revise objectives

**Timescale separation:**

    ν_weight-update >> ν_γ-reclassify >> ν_prune/graft >> ν_O-revision

Weight updates are frequent (every observation). γ reclassification is rare (needs strong structural evidence). Pruning/grafting is rarer (abandon or create causal hypotheses). Objective revision is rarest (change what you want, not how you get it).

**What's open.** The cascade is verbal, not equations. Steps 3-6 each need formal update rules:
- Step 3 needs the signal function and identifiability conditions
- Step 4 is specified (§3's forward pass)
- Step 5 needs a feasibility threshold — what aggregate confidence triggers revision? Is it path-dependent?
- Step 6 needs an O_t revision mechanism — how does the agent decide what to want instead?

Writing these equations is the core remaining work for the single-agent formalism.

---

## 8. Structural Change as Parametric Limit (Settled)

In the probabilistic DAG, "structural" changes are continuous operations on edge weights:
- Pruning: p_ij → ≈ 0 (confidence drops below threshold)
- Grafting: 0 → p_ij (new causal hypothesis, initialized at prior)

This dissolves the sharp line between parametric update (adjusting weights) and structural change (adding/removing edges). TF-10's destruction-creation cycle is the rare limiting case where the ENTIRE DAG must be replaced.

A healthy agent does continuous strategic maintenance (prune, graft, reweight, hedge) and rarely reaches catastrophic restructuring. The six operations, from most to least frequent:

    | Operation          | What changes               | Trigger                           |
    |--------------------|----------------------------|-----------------------------------|
    | Reweighting        | Edge confidence p_ij       | New observation about link         |
    | γ reclassification | Node combination type      | Structural evidence (rare)         |
    | Pruning            | Remove failed branch       | Confidence below threshold         |
    | Grafting           | Add new branch             | Discovery of new possible path     |
    | Objective revision | Change terminal node       | Feasibility failure or opportunity |
    | Full restructure   | Replace entire Σ_t         | Catastrophic failure (TF-10)       |

---

## 9. Predictions (Testable Consequences)

These follow from the settled core. All are **[Speculative]** — non-obvious but untested.

**Pred-1. AND-nodes create fragility cliffs.**

    AND with k parents at uniform p:  P(AND) = p^k OR with k parents at uniform p:   P(OR) = 1 − (1−p)^k

    | k | AND (p=0.8) | OR (p=0.8) |
    |---|-------------|------------|
    | 1 |    0.80     |    0.80    |
    | 2 |    0.64     |    0.96    |
    | 3 |    0.51     |    0.99    |
    | 5 |    0.33     |    1.00    |

Adding required dependencies DESTROYS confidence. Adding alternatives CREATES it. Strategic prescription: for AND-nodes, invest in weakest parent; for OR-nodes, invest in diversity.

**Pred-2. Observability dominates nominal confidence.** An agent choosing between a strong-but-blind path and a weak-but-visible path should prefer the visible one, because the visible path enables learning and course correction while the blind path freezes beliefs.

**Pred-3. Unobservable regions are absorbing states.** Once significant strategy operates through unobservable nodes: frozen beliefs → no mismatch signal → no reason to change → agent cannot learn and cannot recognize it cannot learn. Escape requires external shock, proactive observability investment, or another agent whose observations cover the blind spot.

**Pred-4. Strategic tempo predicts success better than initial confidence.**
Two agents with equal initial path confidence but different strategic tempo T_G: the higher-tempo agent succeeds more often because it corrects errors faster. Mediocre strategy + high T_G > brilliant strategy + low T_G. This is the intent-DAG analog of Boyd's insight that Orient quality beats raw OODA speed.

**Pred-5. Natural AND-of-ORs structure.** Well-formed strategies decompose as AND-of-ORs: conjunction across requirements, disjunction within each requirement. AND-of-ANDs (deep conjunctive chains) are exponentially fragile. OR-of-ANDs (each alternative is itself fragile) are brittle.

---

## 10. Open Design Decisions

Each of these is a genuine choice, not a gap in understanding. They're ordered by estimated impact on the formalism.

### DP-1. Node Taxonomy

**Categorical** (track-a/00): Four types — Objective (O), Key Result (K), Action (A), Observable (X). Each type has type-specific properties (e.g., deadline for K, cost for A, noise for X). Clean, intuitive, maps to OKR vocabulary.

**Continuous** (track-a/02): Four continuous properties per node — agency φ ∈ [0,1], observability σ ∈ [0,1], value ω ≥ 0, horizon λ ≥ 0. No type boundaries. An "action" is just a node with high φ. An "observable" is a node with high σ.

**Assessment.** Both satisfy P1-P7. Categorical is easier to reason about and matches domain vocabulary (OKRs, military planning). Continuous avoids boundary artifacts and allows mixed nodes (partially controllable, partially observable). The choice may depend on the domain instantiation.

**What would resolve it.** Multi-agent work: does intent decomposition across agents work better with categorical types (partition by type) or continuous properties (partition by property ranges)?

### DP-2. O_t Structure

Is the objective a point in S, a region, a set of conditions, or a utility function?

- **Point**: PID setpoint. Simplest. δ_objective = O_t − M_t(current state) is well-defined.
- **Region**: "temperature between 68-72°F." Allows tolerance.
- **Condition set**: "revenue > X AND churn < Y AND morale > Z." Compound objectives. But this looks like... a small AND-node in Σ_t.
- **Utility function**: Most general. But then O_t IS the reward function, and we're back to RL's framing.

**Assessment.** Compound objectives (condition sets) may not need separate treatment — they can be modeled as terminal AND-nodes in Σ_t whose children are individual conditions. This would mean O_t is always simple (one target condition per terminal node) and complexity lives in Σ_t where it belongs.

**What would resolve it.** Attempting to formalize a real multi-objective scenario (military operation with security, logistics, and political objectives) and seeing whether the single-terminal-per-condition model works or breaks.

### DP-3. Commitment State

The formalism doesn't distinguish "considering" from "executing." OR branches are options until something commits resources. The D_t (desire) / I_t (committed intent) split from Codex review:

- **D_t (desire)**: the holistic model of what the agent wants, including latent opportunities ("if this becomes feasible, grab it")
- **I_t (committed intent)**: the subset of Σ_t currently receiving resources and action

This distinction likely becomes load-bearing in multi-agent settings (shared desire vs shared commitment; what you tell allies you want vs what you're actually doing).

**What would resolve it.** Multi-agent directed opportunism: when a subordinate discovers a local opportunity, does it commit (allocate resources) or report (leave commitment to commander)? This reveals whether commitment state needs to be formal.

### DP-4. Resource Budget

Costs are invoked throughout the scratch docs but never modeled. Strategy evaluation requires knowing what paths cost. Options:

- **Unmodeled** (current): rank paths by confidence, ignore cost.
  Adequate for agents with negligible action cost (LLM making API calls).
- **Per-action cost**: each leaf node has cost c_v. Total strategy cost = sum of committed leaf costs. Portfolio optimization over paths.
- **Capacity constraint**: agent has budget B per time unit. Strategy must fit within B. Creates tradeoffs between breadth (more OR branches) and depth (investing more in each branch).

**What would resolve it.** Any real implementation will force this decision. The "developer allocating time" scenario and the "military unit allocating forces" scenario likely need different cost models.

### DP-5. Temporal Ordering

The DAG encodes causal dependency (i causes j) but not temporal ordering (do i before j). In many domains, sequencing matters independently of causation — you must lay foundations before building walls, even though "foundations" and "walls" have independent causal links to "building."

Options:
- **Encode in DAG**: sequential dependencies as edges. But this overloads edge semantics (causal vs temporal).
- **Separate ordering constraint**: a partial order on V_t alongside the causal DAG. More expressive but adds a second structure.
- **Time-indexed nodes**: v becomes v(t), allowing the same proposition at different times. Connects to time-unrolled DAG for cyclic processes.

**What would resolve it.** Attempting to formalize a multi-step plan with genuine sequencing constraints (software deployment pipeline, military phased operation) within the current DAG-only framework. If it works, no new structure needed. If it's awkward, that reveals what's missing.

### DP-6. Identifiability Conditions

Edges claim do-calculus semantics (§2.1) but update from observational signals (§5). Under what conditions is this valid?

**Software domain**: strong identifiability. Agent performs genuine interventions (run test, deploy, git bisect). Confounding is minimal when the agent controls the experimental conditions. Level 3 counterfactuals available via version control.

**Military/organizational domain**: weak identifiability. Multiple agents act simultaneously. Outcomes are delayed. Confounding from environmental and adversary actions. The "did my action cause this outcome?" question is frequently unanswerable from observation alone.

**Possible approaches:**
- State identifiability assumptions explicitly per domain instantiation
- Degrade edge semantics to "associational belief" when identifiability doesn't hold, with acknowledged bias
- Require intervention logs: only update edges for links the agent actually intervened on

**What would resolve it.** Formal analysis of when observational updates converge to the same edge weights as interventional updates (i.e., when is the causal effect identifiable from observational data given the DAG structure of M_t?). This connects to Pearl's do-calculus completeness results.

### DP-7. Cognitive Cost of Σ_t

TF-03 has β (compression cost for M_t). The intent DAG has no analog.
A 500-node strategy is qualitatively different from a 12-node one.

For AI agents with finite context windows, this is concrete: the DAG must fit in working memory or be compressed. This connects to IB-compressed shared intent — but for the self: how much of your own strategy can you hold?

**What would resolve it.** Implementation. Any agent that actually maintains a strategy DAG will hit context limits and need compression. The compression mechanism (which nodes to merge, which branches to abstract) will reveal the right cost model.

### DP-8. What Replaces δ_goal = G_t − M_t?

The old goal mismatch (point subtraction) is a type error for DAG-valued strategy. What's the mismatch signal for purposeful agency?

**Proposed decomposition:**
- **δ_objective** = distance from O_t. Still point-like if O_t is simple (see DP-2). "How far is current reality from what I want?" Measured as: M_t's estimate of current state vs O_t's target condition.
- **δ_strategic** = something about Σ_t's health vs observed progress.
  "Is my strategy working?" Not a single number but a profile across the DAG. Candidates:
  - Aggregate: Δ_G = Σ_v ω_v · (1 − s_v) (value-weighted gap)
  - Critical path: minimum confidence on the highest-value path
  - Rate: d(Δ_G)/dt — is the gap closing or opening?

The third mismatch signal, **δ_feasibility**, remains the least crisp.
It's a second-order inference: "trying hard with good model, gap not closing, therefore goal may be infeasible." Possible formalization: likelihood ratio test on critical-path confidence vs observed progress rate, with threshold triggering O_t revision (Orient cascade step 6).

### DP-9. DAG Acyclicity Scope

The formalism assumes acyclicity (constraint 1 in §2). This is motivated by Pearl's causal DAG framework but is an assumption, not forced.

Real control has feedback loops: monitor → adjust → monitor. These are cyclic in the strategy-space but acyclic in the time-unrolled graph.

**Options:**
- **Time-unrolled DAG**: each node is indexed by time step. Cycles in strategy become chains in the unrolled graph. Correct but potentially large.
- **Option-level abstraction**: a "monitor and adjust" loop is a single compound node whose internal structure is cyclic but whose interface (inputs, outputs, confidence) is acyclic.
- **Allow cycles**: extend the formalism to cyclic graphs. But then status propagation (§3's forward pass) doesn't terminate without fixed-point iteration.

**What would resolve it.** Attempting to formalize a real feedback-control strategy (continuous monitoring, iterative refinement) and seeing whether the DAG assumption creates real problems or is adequately handled by option-level abstraction.

---

## 11. Strategic Tempo and Persistence (Partially Settled)

The clean-slate variant (track-a/02) proposed:

    T_G(v_t) = Σ_{v ∈ V} ν_v · η_v · (∂s_{v_t}/∂s_v)

where ν_v is observation rate, η_v is effective gain, and ∂s_{v_t}/∂s_v is sensitivity of objective status to node v (computed from combination rules).

And a persistence ODE mirroring AAD's adaptive-systems layer:

    d(Δ_G)/dt = −T_G · Δ_G + ρ_G(t)

where Δ_G is value-weighted distance from objectives and ρ_G is the rate at which progress is undone (environmental change, adversary action, state decay).

**Steady state:** Δ_{G,ss} = ρ_G / T_G

**Persistence condition:** T_G > ρ_G / Δ_{G,critical}

**Assessment.** This is a direct transplant of the adaptive-systems persistence framework to the strategy domain. It inherits the same caveats: the linear ODE is a hypothesis (Appendix A's sector-condition framework is more robust), the stochastic treatment gives different scaling (ρ_G/√T_G instead of ρ_G/T_G), and scalar T_G may be a poor summary for strategies with anisotropic gain across different branches.

The T_G formula also has a numerical instability: ∂s_{v_t}/∂s_v at AND-nodes can be very large (bottleneck amplification) or very small (redundancy dampening), making the sum numerically ill-conditioned for deep AND-chains. This needs either regularization or a different formulation.

**Status:** [Plausible] in structure, not yet validated. Included here for completeness but should be treated as a working hypothesis, not settled.

---

## 12. Health Metrics (Scaffold)

These are engineering choices, not principled derivations. Useful for implementation but should be clearly marked as scaffold.

**Groundedness**: fraction of terminal objectives reachable from at least one leaf node with all edge confidences > p_min.

**Observability coverage**: fraction of intermediate nodes with at least one observable descendant (σ > σ_min).

**Weighted redundancy**: R_w(v) = 1 − ∏_{paths P to v} (1 − conf(P)).
Probability that at least one path succeeds, assuming independence.

**Bottleneck score**: Bottleneck(v) = dP(root)/dP(v). Sensitivity of top-level objective to node v. Computed via chain rule through the DAG. For AND-ancestors: multiplicative propagation. For OR-ancestors: diminishing weight.

**Aggregate health** (track-a/02):

    Health(Σ_t) = Groundedness · ObsCoverage · P(root objective)

P(root objective) already encodes conjunction fragility and disjunction robustness via the AND/OR propagation.

**Assessment.** These are reasonable monitoring quantities. They are NOT derived from first principles — they're scaffold. The principled quantities are: path confidence (from §4), observability-adjusted confidence (from §6), and strategic tempo (from §11, if it survives validation).

---

## 13. Provenance

| Element | First appeared | Converged across | Status |
|---------|---------------|-----------------|--------|
| DAG structure | scratch/03 §9 | all three variants | Settled |
| Single-parameter edges | track-a/02, track-a/03 | 02 + 03 (not 00) | Settled |
| AND/OR combination | track-a/02 (as critique), track-a/03 | 02 + 03 | Settled |
| Noisy-OR critique | track-a/02 | 02 + 03 | Settled |
| Orient cascade | scratch/03, track-a/00 | all three | Settled (structure) |
| Uncertainty-ratio update | track-a/00 §2 | all three | Settled (structure) |
| Depth fragility | track-a/00 | all three | Settled |
| Observability dominance | track-a/00, track-a/02 | all three | Settled |
| Directed separation | scratch/03 §10 | all three | Settled |
| Structural-parametric continuity | scratch/03 §9.4 | all three | Settled |
| Strategic tempo formula | track-a/02 | 02 only | Partially settled |
| Node taxonomy (categorical) | track-a/00 | 00 only | Open (DP-1) |
| Node taxonomy (continuous) | track-a/02, track-a/03 | 02 + 03 | Open (DP-1) |
| WEIGHTED combination | track-a/02 | 02 only | Dropped |
| Health metrics | track-a/00, track-a/02 | 00 + 02 | Scaffold |

---

## 14. What This Document Does NOT Include

- **Multi-agent intent dynamics.** Intent decomposition, directed opportunism, adversarial DAG targeting, team persistence — all identified as highest-value next work (see PLANS.md Phase 2 and track-a/04-multi-agent-intent-priorities.md). The single-agent formalism here is necessary scaffolding for multi-agent work.

- **Domain instantiations.** How this maps to software development, military operations, organizational design, or AI agent architectures. Each domain will have specific answers to the open design decisions.

- **Simulation or empirical validation.** The predictions (§9) are testable but untested. Validation is Phase 4 work.

- **The adaptive-systems foundation.** M_t dynamics, mismatch, gain, tempo, persistence — all inherited from TFT (now subsumed by AAD) and not repeated here. See priors/tft/ for the full treatment.
