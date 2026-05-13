# Deriving Purposeful Agency from First Principles (v3)

**Status**: Third pass. Incorporates all Codex/Gemini review corrections from v1 and v2. This is the document from which `src/` claim segments should be authored.

**Date**: 2026-03-09 **History**: v1 (exploratory spike) → v2 (clean rewrite, Codex round 1) → v3 (precision fixes, Codex round 2). Prior versions preserved in msc/ for archaeological record.

**Discipline**: Every step is labeled: **Formulation** (representational choice), **Definition** (names an object), **Scope** (restricts attention), **Derived** (mathematical necessity from prior steps), **Normative** (design criterion grounded in the axioms but requiring an outcome-equivalence precondition), **Proposed schema** (mathematical shape identified, formal content pending). No label inflation.

**The nuanced framing**: Most of this document provides better justification and clearer epistemic labels for architecture that already existed (the O_t/Σ_t split, the orient cascade, directed separation). This is valuable — it transforms design intuitions into precisely labeled theory — but it should not be confused with discovering new mathematics. The genuinely novel results are: the satisfaction gap / control regret split (§7), the G_t complexity bound (§7.6), and the graph structure uniqueness argument (see `spike-graph-uniqueness.md`). The theory's primary contribution is integration — connecting fields that don't normally talk to each other — with these specific novel results embedded within the integration.

---

## 1. The Complete Agent State (Formulation)

TF-03 defines M_t as the agent's complete internal state. To add purpose without breaking completeness, we lift.

*[Formulation (complete-agent-state)]*

$$X_t = (M_t, G_t)$$

- $M_t \in \mathcal{M}$: **epistemic substate** — compressed beliefs about reality. All of Section I's machinery (mismatch, gain, tempo, persistence) applies to $M_t$ unchanged.
- $G_t \in \mathcal{G}$: **purposeful substate** — what the agent wants and how it plans to get it. $G_t = \emptyset$ for Section I agents.

TF-03's completeness now applies to $X_t$. Section I is the special case $X_t = (M_t, \emptyset)$.

### Update dynamics

*[Derived (from TF-02 temporal axiom + completeness on X_t)]*

Policy: $a_t = \pi(M_t, G_t)$

On event $e_\tau$:
$$M_{\tau^+} = f_M(M_{\tau^-}, e_\tau)$$
$$G_{\tau^+} = f_G(G_{\tau^-}, M_{\tau^+}, e_\tau)$$

Between events: $\dot{M} = g_M(M)$, $\dot{G} = g_G(G, M)$.

**Directed separation of update functions** (Derived — §8 for the full statement with scope conditions): $f_M$ has no $G_t$ argument. $f_G$ references $M_{\tau^+}$.

---

## 2. The Objective: O_t Fills a Gap in TF-08 (Definition)

### 2.1 The existing gap

TF-08's policy objective contains a "value" term with no formal content within TFT. $O_t$ provides the missing parametrization.

### 2.2 The value object

*[Definition (horizon-conditioned value)]*

Given objective $O_t$, model $M_t$, policy $\pi$, continuation policy class $\Pi$, and horizon $N_h$:

$$V_O(M_t, \pi; N_h) = \mathbb{E}\!\left[V_{O_t}(\tau_{t:t+N_h}) \;\middle|\; M_t,\; \pi\right]$$

where $V_{O_t}: \text{trajectories} \to \mathbb{R}$ is the **induced value functional** — a scalar measure of how well a trajectory satisfies the objective.

Action-value form (for policy objective):

$$Q_O(M_t, a; \pi_{\text{cont}}, N_h) = \mathbb{E}\!\left[V_{O_t}(\tau) \;\middle|\; M_t,\; a_t = a,\; a_{t+1:} \sim \pi_{\text{cont}}\right]$$

**Continuation convention**: All value queries are conditioned on a specific continuation policy $\pi_{\text{cont}}$ and finite horizon $N_h$. This parallels TF-10's operational sufficiency $S_\Pi$, which also uses finite horizon and policy class.

**Policy closure**: $\pi_{\text{cont}}$ is a *parameter* of the value object, not a derived quantity. AAD does not prescribe a specific solution concept. Common choices:
- $\pi_{\text{cont}} = \pi_{\text{current}}$ — one-step improvement (evaluate each action assuming current behavior continues afterward)
- $\pi_{\text{cont}} = \pi^\ast$ — Bellman fixed point (self-consistent optimal continuation; requires solving a fixed-point equation)
- $\pi_{\text{cont}}$ re-optimized each step — receding-horizon / MPC

The one-step improvement ($\pi_{\text{cont}} = \pi_{\text{current}}$) is the natural default for AAD: it requires no fixed-point computation, aligns with the incremental update philosophy (TF-06), and is a practical default — not a convergence guarantee (specific convergence conditions depend on the environment and policy class). When a solution concept matters (e.g., for the optimality of $A_O$ in §7), it should be stated explicitly.

**Policy objective** (extending TF-08):

$$\pi^*(M_t, G_t) = \arg\max_a \left[Q_O(M_t, a; \pi_{\text{current}}, N_h) + \lambda(M_t, O_t, N_h) \cdot \text{CIY}(a; M_t)\right]$$

Note $\lambda$ now depends on $(M_t, O_t, N_h)$, not just $M_t$. The value of exploration depends on the objective and the horizon: an agent with a deadline should explore less as time runs out; an agent with a safety constraint should explore differently from a utility maximizer. Two agents with identical $M_t$ but different objectives should price exploration differently.

### 2.3 Objective representations

$O_t$ can take multiple forms, all unified through $V_{O_t}$:

| $O_t$ form | $V_{O_t}(\tau)$ | Example |
|---|---|---|
| Point target $r$ | $-\Verts_T - r\|$ | PID setpoint |
| Target region $R$ | $\mathbb{1}[s_T \in R]$ | "reach safe state" |
| Constraint set | $-\sum_t \max(0, g_i(s_t))$ | "never violate SLA" |
| Utility $U$ | $\sum_t \gamma^t U(s_t)$ | RL reward |
| Trajectory functional $J$ | $J(\tau)$ | "migrate, zero downtime" |

The trajectory functional is the most general; the others are special cases. **Type stability**: regardless of $O_t$'s internal form, the interface to the theory is $V_{O_t}: \text{trajectories} \to \mathbb{R}$.

---

## 3. Strategy as an Independent Dimension (Definition)

### 3.1 The ontological distinction

$O_t$ specifies *what* the agent wants (the evaluation criterion).
$\Sigma_t$ encodes the agent's theory of *how* its actions produce progress toward $O_t$.

These are different *kinds of information* answering different questions:
- $O_t$: "Is this trajectory satisfactory?" (evaluation)
- $\Sigma_t$: "Which action sequence produces a satisfactory trajectory?" (guidance)

The split is **definitional** — it reflects a structural difference in the information, not a dynamic or timescale claim:

$$G_t = (O_t, \Sigma_t)$$

### 3.2 Strategy representations (ordered by expressiveness)

| $\Sigma_t$ form | What it encodes |
|---|---|
| None (reactive) | $\pi$ is implicit in $M_t$ |
| Cached policy | Learned mapping $s \to a$ |
| Subgoal sequence | Waypoints with ordering |
| Causal DAG | Action-outcome chains with AND/OR and confidences |

### 3.3 When richer Σ_t is needed (Discussion)

A reactive agent ($\Sigma_t = \emptyset$) suffices when greedy optimization on $Q_O$ works — when the action-to-value mapping is approximately convex and single-step. When the environment has non-convex landscapes, prerequisite structure, or multi-step causal chains, greedy fails and the agent needs explicit strategy. The trigger is the **purposeful analog of TF-10**: inadequacy of $\Sigma_t$'s representational capacity for the environment's causal complexity.

*The formal trigger (strategic adequacy measure) is not yet defined — see §9. This subsection is discussion, not derivation.*

---

## 4. Causal Hierarchy and Level 2 Access

### 4.1 The causal hierarchy theorem (Mathematical fact)

Bareinboim et al. 2022: the three levels (association, intervention, counterfactual) form a strict hierarchy. Level 2 quantities cannot in general be computed from Level 1 data alone.

### 4.2 Consequence

Evaluating $Q_O(M_t, a; \cdot)$ requires answering "what is the expected outcome if I *do* $a$?" — a Level 2 query. Level 2 *knowledge* is required.

*[Scope Narrowing]*

We restrict to agents that must **acquire or refine** Level 2 knowledge during operation, as opposed to agents where the designer pre-compiled it (PID, LQR, hardcoded policy). Pre-compiled agents are purposeful but their causal structure is externally supplied.

### 4.3 The feedback loop provides interventional data access (Derived)

*[Derived (from TF-02 + temporal ordering)]*

An agent in the feedback loop generates interventional data:
$a_t$ causally precedes $o_{t+1}$; the mismatch $\delta_t$ conditioned on $a_t$ carries interventional information.

**Precision**: The loop provides **access to interventional data**.
Whether the agent *exploits* it for Level 2 reasoning depends on its update mechanism and model class. The claim is about data availability, not reasoning capacity.

### 4.4 Language training as causal priors (Discussion)

LLMs trained on causally-structured text absorb causal priors — noisy prior knowledge from mixed provenance (experimental, observational, speculative). This is not automatically-identified interventional structure. The IB objective (TF-03) predicts causal structure will be retained because it has predictive power for language, but the epistemic status is *prior* (plausible), not *derived* (from the agent's own interventions).

An LLM in the loop has both: priors from training AND interventional data from the loop. The priors accelerate; the loop verifies.

---

## 5. The Cost Inequality for Explicit Strategy

### 5.1 Two modes of purposeful action

**Loop-based** (model-free): Act, observe, adjust. Level 2 knowledge is acquired implicitly. Cost: real actions, real time, possible damage.

**Model-based** (explicit $\Sigma_t$): Build internal action-outcome model. Evaluate actions by mental simulation. Cost: computation, model maintenance, model inaccuracy.

### 5.2 The cost inequality

*[Normative design criterion (via #post-temporal-optimality)]*

An agent benefits from explicit $\Sigma_t$ when:

$$C_{\text{plan}} + C_{\text{maintain}} \lt C_{\text{explore}} + C_{\text{repair}}$$

**Epistemic status**: This is labeled *normative*, not *derived*, because #post-temporal-optimality requires identical non-temporal outcomes as a precondition. In practice, loop-based and model-based approaches may differ in final value, risk profile, reversibility, and model bias. The inequality is correct *when* the outcomes are approximately equivalent — a condition that must be verified case by case, not assumed.

**When the precondition holds**: The inequality makes #post-temporal-optimality load-bearing for the purposeful layer. An agent in an environment where $C_{\text{explore}} + C_{\text{repair}}$ is large (production software, military operations, irreversible decisions) is strongly driven toward explicit $\Sigma_t$.

**When the precondition fails**: Model-based and loop-based approaches may produce qualitatively different outcomes (the model introduces bias; exploration discovers things planning cannot). In such cases the inequality is insufficient and the choice requires richer analysis (e.g., which approach has lower expected regret including model error).

---

## 6. Properties of Multi-Step Strategies

### 6.1 Additive log-confidence (Derived)

*[Derived (mathematical property of sequential uncertain events)]*

For a chain of $n$ steps with conditional success probabilities:

$$\log P(\text{chain}) = \sum_{i=1}^{n} \log P(E_i \mid E_{\lti})$$

Chain confidence decays monotonically with depth. The rate depends on the conditional structure — the independent uniform case ($p^n$) is the simplest special case, not the general result.

**Robust qualitative consequence**: Longer chains are less confident than shorter ones, creating structural pressure toward short plans, parallel fallback paths, high-confidence critical links, and early monitoring for failure.

### 6.2 Combination semantics (Scope Narrowing)

*[Scope Narrowing]*

We restrict to environments where causal combination is approximately conjunctive (AND) or disjunctive (OR), without strong interaction.

**Justification**: Converged across three independent formalism attempts. Captures dominant structure in most planning domains. The excluded case (complementarity, substitutability, interaction effects) requires richer combination rules — a legitimate divergence point for future work.

Under this restriction: $\Sigma_t = (V, E, p, \gamma)$ with AND/OR nodes and single-parameter edges $p_{ij} \in [0,1]$.

---

## 7. Purposeful Mismatch: Satisfaction and Regret

With $X_t = (M_t, (O_t, \Sigma_t))$, three families of discrepancy arise. The key structural insight: the purposeful layer requires **two** distinct gap measures, not one — separating attainability from optimality.

### 7.1 δ_epistemic: Reality model error (unchanged from Section I)

$$\delta_{\text{epistemic}} = o_t - \hat{o}_t$$

**Update source**: observations. **Timescale**: fastest.

### 7.2 Objective attainability

*[Definition]*

$$A_O(M_t; \Pi, N_h) = \sup_{\pi \in \Pi} V_O(M_t, \pi; N_h)$$

The best achievable objective value given current beliefs $M_t$, available policies $\Pi$, and horizon $N_h$.

### 7.3 Satisfaction gap: Is the objective achievable?

*[Definition]*

$$\delta_{\text{sat}} = V_{O_t}^{\min} - A_O(M_t; \Pi, N_h)$$

where $V_{O_t}^{\min}$ is the minimum value that counts as "objective met" (a threshold set by the objective itself — for constraints, all satisfied; for utility, a minimum acceptable level).

- $\delta_{\text{sat}} \gt 0$: The objective is **unmet** under the best available policy, current model, and horizon.
- $\delta_{\text{sat}} \leq 0$: The objective is **attainable** in principle.

**Disambiguation**: $\delta_{\text{sat}} \gt 0$ does NOT automatically mean the *goal* is wrong. It means the goal is unmet given $(M_t, \Pi, N_h)$. The positive signal has multiple possible causes:

| Cause | Fix | How to distinguish |
|---|---|---|
| Goal is genuinely infeasible | Revise $O_t$ | Persists across $M_t$, $\Pi$, $N_h$ improvements |
| Policy class too narrow | Expand $\Pi$ (structural adaptation of $\Sigma_t$) | $\delta_{\text{sat}}$ decreases when richer policies are tried |
| Horizon too short | Extend $N_h$ | $\delta_{\text{sat}}$ decreases with longer planning horizon |
| Model is wrong about feasibility | Improve $M_t$ (reduce $\delta_{\text{epistemic}}$) | $\delta_{\text{sat}}$ changes when $M_t$ is corrected |

**The revised cascade** (replacing the simpler "fail → revise O_t"):
When $\delta_{\text{sat}} \gt 0$ persists, the agent should consider *all four* options. The orient cascade's ordering applies: first check $M_t$ adequacy (maybe the goal IS feasible but the model doesn't know it), then check $\Pi$ and $N_h$ adequacy, and only THEN consider revising $O_t$. Revising the objective is the last resort, not the first response to unmet goals.

### 7.4 Control regret: Is the policy suboptimal?

*[Definition]*

$$\delta_{\text{regret}} = A_O(M_t; \Pi, N_h) - V_O(M_t, \pi_{\text{current}}; N_h) \geq 0$$

The gap between best achievable and current performance. Always non-negative.

- $\delta_{\text{regret}} \approx 0$: The agent is already doing the best it can within current $(\Pi, N_h, M_t)$. If $\delta_{\text{sat}} \gt 0$ simultaneously, the problem is not the current strategy within current capabilities — it may be the goal, or it may be insufficient capability ($\Pi$, $N_h$, or $M_t$ inadequacy). See §7.3's disambiguation table.
- $\delta_{\text{regret}} \gg 0$: There's room for improvement without changing $O_t$. → Revise $\Sigma_t$.

**This is the signal for Σ_t revision.**

### 7.5 Strategic calibration residual: Is the plan's causal model correct?

*[Definition]*

For each edge $(i, j)$ in $\Sigma_t$ with confidence $p_{ij}$, define the **edge residual**: the difference between the predicted and observed value increment when traversing that edge.

$$r_{ij} = \mathbb{E}[\Delta V_O \mid \text{edge } (i,j) \text{ traversed}, M_t] - \Delta V_O^{\text{observed}}$$

where $\Delta V_O$ is the change in $V_O(M_t, \pi; N_h)$ attributable to completing step $j$ (as predicted by $\Sigma_t$) versus the observed change.

The **strategic calibration residual** aggregates across active edges:

$$\delta_{\text{strategic}} = \left(\sum_{(i,j) \in \text{active}} w_{ij} \cdot r_{ij}^2 \right)^{1/2}$$

where $w_{ij}$ weights edges by importance (e.g., criticality to the current plan's critical path).

**Typing**: Each edge predicts a value increment (scalar), not a full state transition. This is the most tractable typing because it connects directly to the value object $V_O$ and allows aggregation across heterogeneous step types.

**Conditioning**: The edge residual $r_{ij}$ is conditioned on:
- The edge being actually traversed (the agent attempted the step)
- $M_t$ being adequate (so the observed $\Delta V_O$ is meaningful)
- The agent following $\Sigma_t$'s prescription for step $j$ (execution fidelity — otherwise the residual conflates bad plan with bad execution)

Without the execution fidelity condition, a positive residual could mean "the plan is wrong" or "the agent didn't follow the plan." These require different corrections ($\Sigma_t$ revision vs. execution improvement).

This is a **second-order inference** — it requires accumulating evidence over multiple edge traversals. It is inherently slower to evaluate than $\delta_{\text{epistemic}}$.

**Connection to the persistence schema** (§9): $\delta_{\text{strategic}}$ as defined here IS the candidate strategic mismatch state. The correction function would be edge-confidence revision (reducing $p_{ij}$ when $r_{ij}$ is persistently positive, increasing it when consistently negative). The disturbance would be environmental changes that alter edge-traversal outcomes. Whether this correction function satisfies the sector condition remains open (§9.3).

### 7.6 The orient cascade (Derived)

The resolution ordering follows from logical dependency:

1. **Reduce $\delta_{\text{epistemic}}$** — understand reality (Orient).
   Prerequisite for all purposeful evaluation, because $M_t$ appears in every subsequent formula.

2. **Evaluate $\delta_{\text{sat}}$** — is the goal achievable?
   Requires adequate $M_t$ to assess $A_O$.

3. **If feasible, evaluate $\delta_{\text{regret}}$** — is the policy suboptimal? Requires both adequate $M_t$ and meaningful $A_O$.

4. **If $\delta_{\text{regret}}$ high, evaluate $\delta_{\text{strategic}}$** — is the plan's causal model wrong? Requires adequate $M_t$, feasible $O_t$, and evidence of suboptimal execution.

5. **If $\delta_{\text{sat}} \gt 0$ persists across $\Sigma_t$ revisions** — revise $O_t$.

**Derivation**: Each step's input depends on the output of prior steps.
You cannot evaluate strategy quality with a broken reality model; you cannot distinguish bad strategy from infeasible goal without evaluating attainability first. The ordering is forced by information dependency.

**G_t complexity bounded by M_t capacity**: $\Sigma_t$'s evaluable complexity is bounded by $M_t$'s ability to observe which strategy edges are intact. An agent with poor $S(M_t)$ cannot meaningfully evaluate a complex $\Sigma_t$. This creates a virtuous cycle (better $M_t$ → richer evaluable $\Sigma_t$ → better-directed action → faster $M_t$ improvement) and a vicious one (degraded $M_t$ → strategy simplification → cruder action → further $M_t$ degradation).

---

## 8. Directed Separation (Derived, with scope condition)

**The update function $f_M$ is $G_t$-independent**:
$$M_{\tau^+} = f_M(M_{\tau^-}, e_\tau)$$

**The update function $f_G$ depends on $M_t$**:
$$G_{\tau^+} = f_G(G_{\tau^-}, M_{\tau^+}, e_\tau)$$

**The policy couples all three**:
$$a_t = \pi(M_t, G_t)$$

*[Scope Condition]*

The claim "$f_M$ has no $G_t$ argument" requires that the epistemic update is goal-blind *conditional on the realized event*. This holds when:

- The observation mechanism $h$ is action-dependent (TF-01 allows this) but the update rule $f_M$ processes whatever event arrives without reference to why the agent sought that event.
- The agent doesn't use its goals to filter, weight, or interpret observations differently (no goal-dependent attention thresholds or confirmation bias baked into $f_M$).

If the agent's goals influence the observation mechanism (goal-directed sensing, attention allocation, query selection), the *event that arrives* depends on $G_t$ through $\pi \to a_t \to e_\tau$, but $f_M$ still processes it goal-blindly. The directed separation is about the **processing** of events, not the **selection** of events.

**This is a genuine scope restriction, not a footnote.** Many agents we care about — including LLM agents — violate it to some degree. An LLM agent's prompt includes the task objective, which shapes how it interprets code, documentation, and error messages. Its "f_M" is goal-conditioned in practice: the agent reading code with the goal "fix the auth bug" processes the same code differently than one with the goal "add logging."

**What this means**: For goal-conditioned agents, the directed separation is an *approximation* — useful as an analytical idealization but not exact. The approximation is better when:
- Goal-conditioning affects *attention* (which events to seek) more than *interpretation* (how to process events that arrive)
- The agent has strong epistemic discipline (updates beliefs based on evidence quality, not goal alignment)
- The epistemic update is architecturally separated from goal evaluation (e.g., separate model-update and planning modules)

The approximation is worse when:
- The agent exhibits confirmation bias (interpreting ambiguous evidence in goal-consistent ways)
- Goal-conditioning is deeply embedded in the processing architecture (as in attention-based models where the query includes intent)

**For the current theory**: We proceed with the directed separation as a scope condition, noting that goal-conditioned agents (including most LLM agents) are *approximately* within scope when their epistemic processing is *mostly* goal-blind. A future extension treating goal-conditioned epistemic dynamics would require coupling terms in $f_M$ and would likely produce richer (and more fragile) dynamics — the theory of motivated reasoning, confirmation bias, and wishful thinking formalized as a departure from directed separation.

---

## 9. Strategy Persistence (Proposed Theorem Schema)

### 9.1 The structural parallel

The sector-condition mathematics (Appendix A) proves bounded mismatch for any system with: a mismatch state, a correction function satisfying sector bounds, and bounded disturbance. This mathematics is agnostic to domain — it doesn't care whether the mismatch is epistemic, strategic, or something else.

### 9.2 The schema

*[Proposed Theorem Schema]*

**If** strategic update dynamics satisfy:
- (SA1) Zero correction at zero strategic mismatch
- (SA2') Local sector condition on strategic correction
- Bounded strategic disturbance

**Then** $\Sigma_t$ persists iff $\alpha_\Sigma \gt \rho_\Sigma / R_\Sigma$.

### 9.3 What's needed (genuine future work)

1. **Strategic mismatch state**: Candidate — aggregated calibration residual from §7.5 across strategy edges.
2. **Strategic correction function**: How $\Sigma_t$ updates in response to strategic mismatch. Candidate — edge confidence revision via the gain principle, but not yet formalized.
3. **Strategic disturbance**: Rate at which the environment invalidates causal links. Candidate — requirement changes, resource changes, adversary actions.
4. **Sector condition verification**: Whether the correction function satisfies the sector condition.

Until defined, this is a *schema* — "if the shape fits, the conclusion follows."

---

## 10. Summary

### Formulations (representational choices)
1. $X_t = (M_t, G_t)$ — complete agent state with epistemic and purposeful substates

### Definitions (naming objects)
2. $O_t$ as value parametrization — fills TF-08's gap
3. $V_{O_t}$: trajectory functional — type-stable interface
4. $V_O(M_t, \pi; N_h)$, $Q_O(M_t, a; \pi, N_h)$ — horizon/policy- conditioned value objects
5. $G_t = (O_t, \Sigma_t)$ — ontologically distinct components
6. Objective attainability $A_O$
7. Satisfaction gap $\delta_{\text{sat}}$
8. Control regret $\delta_{\text{regret}}$
9. Strategic calibration residual $\delta_{\text{strategic}}$

### Derived (mathematical necessity)
10. Causal hierarchy theorem: Level 2 knowledge needed for consequence- based action selection
11. Feedback loop provides interventional data access (TF-02)
12. Additive log-confidence in causal chains
13. Directed separation of update functions (with scope condition §8)
14. Orient cascade from information dependency between mismatch types
15. $\Sigma_t$ evaluable complexity bounded by $M_t$ capacity

### Scope narrowings
A. Agents that must learn Level 2 knowledge during operation B. AND/OR causal combination environments

### Normative (grounded in axioms, outcome-equivalence required)
C. Cost inequality for explicit $\Sigma_t$: planning preferred when
   $C_{\text{plan}} + C_{\text{maintain}} \lt C_{\text{explore}} + C_{\text{repair}}$, conditional on approximately equivalent non-temporal outcomes

### Proposed schema
D. Strategy persistence condition (§9) — awaiting formal definitions

### Empirical observations (available as additional scope narrowings)
E. Timescale separation $\nu_O \ll \nu_\Sigma$ for many agent populations F. LLM training data as causal priors (discussion-grade)

---

## 11. Implications for src/ Segments

### Proposed authoring order

| # | Slug | Type | Source |
|---|------|------|--------|
| 210 | complete-agent-state | Formulation | §1 |
| 215 | objective-functional | Definition | §2 |
| 220 | value-object | Definition | §2.2 |
| 225 | strategy-dimension | Definition | §3 |
| 230 | causal-hierarchy-requirement | Derived + Scope | §4 |
| 235 | loop-interventional-access | Derived | §4.3 |
| 240 | explicit-strategy-condition | Normative | §5 |
| 245 | chain-confidence-decay | Derived | §6.1 |
| 250 | directed-separation | Derived + Scope | §8 |
| 255 | satisfaction-gap | Definition | §7.3 |
| 260 | control-regret | Definition | §7.4 |
| 265 | strategic-calibration | Definition | §7.5 |
| 270 | orient-cascade | Derived | §7.6 |
| 275 | and-or-scope | Scope | §6.2 |
| 280 | strategy-dag | Definition | §6.2 (post-narrowing) |
| 285 | strategy-persistence-schema | Proposed schema | §9 |

### What changed from v2 (and post-v3 tightening)
- Epistemic labels corrected throughout (no label inflation)
- Cost inequality downgraded from "derived" to "normative"
- Unified value object ($V_O$, $Q_O$) with explicit continuation and horizon — cleans up interventional query, cost inequality, and all mismatch definitions in one pass
- **Policy closure**: $\pi_{\text{cont}}$ is a parameter; one-step improvement ($\pi_{\text{cont}} = \pi_{\text{current}}$) is the natural default; Bellman fixed point and MPC are alternatives
- **λ extended**: $\lambda(M_t, O_t, N_h)$ — exploration price depends on objective and horizon, not just epistemic state
- δ_objective split into satisfaction gap + control regret
- **Satisfaction gap disambiguated**: $\delta_{\text{sat}} \gt 0$ may indicate infeasible goal OR insufficient capability (narrow $\Pi$, short $N_h$, wrong $M_t$). The cascade checks $M_t$, $\Pi$, $N_h$ before revising $O_t$ — objective revision is last resort.
- **δ_strategic typed**: Edge residuals defined as value-increment predictions vs. observations, aggregated across active edges with criticality weighting. Connects directly to the persistence schema.
- **Directed separation scope condition elevated**: LLM agents' goal-conditioned processing explicitly acknowledged as a genuine scope restriction. Theory approximates well when epistemic processing is mostly goal-blind; a future extension of coupled dynamics would formalize motivated reasoning and confirmation bias.
- Timescale separation removed from derivation chain, available as empirical observation / additional scope narrowing

### Strings being pulled: graphical structure uniqueness

See `spikes/spike-graph-uniqueness.md` for an exploration of whether the DAG structure (not just "some causal representation") can be derived from first principles. The key insight: LOCAL REVISABILITY of the strategy → the Markov condition → directed graphical model. Combined with temporal ordering → acyclicity, this may constitute a uniqueness argument analogous to Cox's theorem for probability. The AND/OR semantics may follow from Boolean completeness + parsimony under bounded cognition. If this argument holds, it narrows the "formulation choice" space significantly — the graph structure is forced, and only the specific parameterization (CPT form) remains a choice.

### What remains open
- **Strategic correction dynamics**: §7.5 now defines the strategic mismatch state (edge residuals typed as value-increment predictions). Still needed: formal correction function (edge confidence revision rule), sector-condition verification, and disturbance characterization. These would promote §9 from schema to theorem.
- **Edge update rule**: The gain principle applied to edge confidences (η_edge = U_edge / (U_edge + U_obs)) is plausible but not validated independently. The edge residual definition in §7.5 provides the mismatch signal; the update rule is the correction function.
- **DAG acyclicity**: The graph-uniqueness spike sketches a derivation (temporal ordering over finite horizon forces acyclicity), but this argument is part of the broader P3→Markov sketch which is still provisional. Keep as open until that sketch is tightened. If it holds, acyclicity is derived for Σ_t specifically (not for M_t's model of the environment, which may include cyclic physical processes).
- **Cognitive cost of Σ_t**: No IB analog yet. A 500-node DAG is qualitatively different from a 12-node one, even at identical path confidences. For finite-context agents, the DAG must fit in working memory. This connects to the cost inequality (§5) — part of $C_{\text{maintain}}$ is the cognitive cost of keeping $\Sigma_t$ in the agent's representational capacity.
- **Edge identifiability in confounded domains**: Resolved in software (genuine interventions available); open in general. The scope narrowing to learning agents (§4.2) helps but doesn't fully resolve.
- **Goal-conditioned epistemic dynamics**: The directed separation scope condition (§8) excludes agents with strongly goal-dependent f_M. A future extension would formalize motivated reasoning, confirmation bias, and wishful thinking as departures from directed separation — likely producing coupled M_t/G_t dynamics with richer (and more fragile) behavior.
- **Whether "agents modifying own observation channels" is general**:
  The code-quality-as-observation-infrastructure insight may be an instance of a Section I pattern (any agent that can modify h) or may be genuinely software-specific. Unresolved.
- **Π and N_h adaptability**: Are the policy class and planning horizon fixed agent parameters or can they themselves adapt? If adaptable, there's a meta-level structural adaptation (expanding Π is analogous to TF-10's model class change). This connects to the δ_sat disambiguation — "insufficient Π" might be the fix, not "wrong O_t."
