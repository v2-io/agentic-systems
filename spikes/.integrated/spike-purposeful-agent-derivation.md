# Theoretical Spike: Deriving Purposeful Agency from First Principles

**Status**: Working document — exploratory, not settled. This is the raw thinking behind the purposeful agency derivation. Future agents: this is meant to be messy, honest, and detailed. The cleaned-up results, if any, will migrate into `src/` claim segments.

**Date**: 2026-03-09 **Author**: Joseph Wecker + Claude Opus 4.6 session

**Revision note (same session, after Codex review)**: Codex identified seven structural issues, several of which require significant rework. The most critical: (1) state completeness — TF-03 claims M_t is the complete state, so introducing G_t alongside it is a contradiction unless we lift to X_t = (M_t, G_t); (2) the G_t hierarchy conflates objective richness with strategy richness — these are independent dimensions and the O_t/Σ_t split should happen EARLIER; (3) "needs Level 2" is too strong — pre-compiled controllers are purposeful at Level 1; (4) the mismatch mathematics is too narrow for non-point objectives. See Part 11 (Codex review integration) for the full analysis and proposed fixes. The body of Parts 1-10 retains the original reasoning for context; Part 11 is where the corrections live.

**Goal**: Start with the simplest possible abstract object representing "what an agent wants" and derive, through mathematical necessity, what structure that object must have. See where the DAG (or something else) *emerges* rather than being assumed. Specifically:

1. When does a purposeful agent need more than a reference signal?
2. When does it need causal structure? (Pearl's hierarchy gives us this.)
3. When does the O_t / Σ_t split become necessary?
4. When does the DAG with AND/OR semantics become the right formalism?

**The key constraint**: Every step must be *derived* or *motivated by mathematical necessity*, not assumed by architectural choice. If the DAG is the right answer, we should be *forced* into it.

**The methodological discipline** (added after review): Where a claim cannot be derived, it should be stated as an explicit **scope narrowing** — "we now restrict attention to agents with property X" — with justification for why the narrowing is interesting or natural. This prevents hand-waving from masquerading as derivation. The theory should read as a progressive telescoping of scope, each step either derived (mathematical necessity) or narrowed (explicit restriction with motivation).

---

## Part 0: What We Already Have

Section I of AAD (from TFT) gives us an agent with:
- M_t ∈ M — a compressed model of reality
- δ_t = o_t − ô_t — mismatch between prediction and observation
- η* = U_M / (U_M + U_o) — optimal update gain
- T = Σ ν^(k) · η*^(k) — adaptive tempo
- The persistence condition: T > ρ / ‖δ_critical‖

This agent *tracks reality*. It adapts. It can even act (TF-07: a_t = π(M_t)).
But its actions serve no declared purpose — the policy π could be arbitrary, random, or emergent. The agent has no *goal*.

**The question**: What is the minimal formal object that makes the agent *purposeful*? And how does that object's necessary structure relate to the environment's causal complexity?

---

## Part 1: The Purposeful State G_t — Minimal Definition

### 1.1 What must G_t do?

By analogy with M_t:

M_t answers: "What is the world like?" (epistemic — reality tracking) G_t answers: "What do I want the world to be like, and what must I do to get there?" (instrumental — reality shaping)

More precisely, G_t must support:

1. **Evaluation**: Given M_t (what the world is like), is the current state satisfactory? G_t provides the criterion for "satisfactory."
2. **Action guidance**: Given M_t and G_t, which action moves the world toward the desired state? G_t constrains the policy π.
3. **Revision**: When evidence suggests the purpose should change (the goal was achieved, or became infeasible, or was superseded).

### 1.2 The minimal G_t

*[Formulation (purposeful-state)]*

Define G_t ∈ G as the agent's **purposeful state**: a compressed representation of what the agent is trying to achieve.

Just as M_t = φ(C_t) compresses the interaction history into a model of reality, we can write:

    G_t = ψ(C_t, M_t, G_{t-1})

G_t depends on:
- The interaction history (what has happened)
- The current reality model (what the agent believes about the world)
- The previous purposeful state (purposes evolve, they aren't built from scratch each step)

**Note**: Unlike M_t, which is derived solely from C_t (the history determines the model), G_t also depends on G_{t-1}. This is because purpose is not fully determined by history — the same history is compatible with different goals. Two agents with identical M_t may want different things. This is a first sign that G_t has different dynamics from M_t.

### 1.3 The purposeful state hierarchy

The simplest possible G_t forms, in order of representational richness:

**Level 0: No purpose.** G_t = ∅. This is a Section I agent — pure adaptive tracking. The policy π(M_t) may be effective, but it serves no declared purpose. (A thermostat with no setpoint. A Kalman filter estimating without controlling.)

**Level 1: Reference signal.** G_t = r_t ∈ S. A target state. The agent wants the world to be in state r_t. Purposeful mismatch is:

    δ_G = r_t − M_t(relevant dimensions)

This is what a PID controller has (setpoint), what a simple pursuit agent has (target location), what gradient descent has (loss minimum). The policy is: move to reduce ‖δ_G‖.

**Level 2: Evaluation function.** G_t = U: S × A → ℝ. A reward or utility function. More expressive than a reference signal — the agent can represent preferences over states, tradeoffs, and multi-objective optimization. The policy is: maximize expected U given M_t.

**Level 3: Subgoal decomposition.** G_t = (r_t, {r_i}, ordering).
A target state plus intermediate waypoints with prerequisite ordering.
The agent represents not just WHERE it wants to be but WHAT PATH gets it there. This is where planning lives.

**Level 4: Causal action-outcome model.** G_t = (O_t, Σ_t). The agent represents the target (O_t) separately from its theory of how actions produce outcomes (Σ_t). This is where the DAG enters — if it must.

**The theoretical question: What forces the agent from Level k to Level k+1?**

---

## Part 2: Where the Reference Signal Breaks

### 2.1 The adequacy test

A Level 1 G_t (reference signal r_t) is adequate when:

1. The mapping from actions to progress-toward-r is approximately monotone in the relevant dimensions. ("Moving toward the goal is always possible and always helps.")
2. The agent can select actions that reduce ‖δ_G‖ using only M_t and r_t — no further information about the causal structure of the environment is needed.
3. The path from current state to r_t doesn't require going "away" from r_t first.

### 2.2 When does it break?

**Non-convex landscapes.** If reaching r_t requires first moving away from it (navigating around an obstacle, going through an intermediate state that increases ‖δ_G‖ temporarily), the gradient on δ_G leads to local minima. The agent gets stuck.

*Formal version*: Let V(s) = ‖r − s‖ be the "goal distance" function.
If V is non-convex in the action-reachable state space — if there exist states s where ∇_a V(s) points toward a local minimum that is not r — then greedy action on δ_G fails.

**Multi-step prerequisites.** If achieving r_t requires first achieving intermediate states r_1, r_2, ... (in order), the agent needs to represent this decomposition. The reference signal r_t alone doesn't encode the prerequisite structure.

*Example*: An agent wants to be at state "deployed software." But first it needs "compiled code," which requires "written code," which requires "understood requirements." The reference signal "deployed software" provides no guidance about which intermediate state to pursue first.

**Uncertain feasibility.** The agent might not know WHETHER r_t is achievable from the current state. A reference signal carries no confidence information — it's just a point. The agent has no way to represent "I think there's a 60% chance I can reach r_t from here."

**Multi-agent communication.** When purpose must be shared with other agents, a bare reference signal is either too dense (the destination without the reasoning) or too sparse (it doesn't communicate which constraints matter, which paths are acceptable, what tradeoffs are permitted). This is the Auftragstaktik insight: communicating purpose requires compressing G_t in a way that preserves action-guiding capacity while reducing communication cost — an information bottleneck problem.

### 2.3 The formal trigger for Level 1 → Level 2+

*[Hypothesis]*

The reference signal becomes inadequate — requiring richer G_t — when the agent's policy π(M_t, r_t) cannot produce actions that reduce ‖δ_G‖ below a satisfactory threshold, *even though M_t is adequate* (the agent understands the world well enough).

This is the purposeful analog of TF-10's structural adaptation trigger:
just as F(M) < 1 − ε triggers M_t structural adaptation (the reality model class is inadequate), a similar condition on G_t triggers purposeful structural adaptation (the goal representation class is inadequate).

Define **purposeful model adequacy** by analogy with model sufficiency:

    A_G(G_t, M_t) = degree to which G_t supports effective action
                     selection given accurate-enough M_t

When A_G is low despite adequate M_t, the problem is not that the agent misunderstands the world — it's that the agent's *representation of its purpose* is too impoverished to guide action in this environment.

**Key insight**: This is domain-dependent. A PID controller (Level 1) is perfectly adequate for linear SISO tracking. It becomes inadequate for nonlinear multi-step problems — not because the setpoint is wrong, but because the setpoint *representation* can't encode the information needed for effective action.

---

## Part 3: The Causal Hierarchy Theorem and the Necessity of Causal Structure

This is where Pearl's work becomes essential, and where we get a *mathematical proof* that purposeful agents must maintain causal structure.

### 3.1 The three levels

Pearl's causal hierarchy (formalized by Bareinboim et al. 2022 as the **Causal Hierarchy Theorem**):

**Level 1 — Association**: P(Y | X). "What is Y if I *observe* X?" Passive prediction. This is what M_t provides.

**Level 2 — Intervention**: P(Y | do(X)). "What is Y if I *do* X?" Active prediction — what happens when I intervene. This is what purposeful action requires.

**Level 3 — Counterfactual**: P(Y_x | X = x', Y = y'). "What *would* Y have been if I had done X instead of X'?" Retrospective causal reasoning.

### 3.2 The impossibility result

**The Causal Hierarchy Theorem** (Bareinboim, Correa, Ibeling, Icard, 2022): The three levels form a *strict* hierarchy. In general:

- Level 2 quantities (interventional) CANNOT be computed from Level 1 data (observational) alone, without causal assumptions.
- Level 3 quantities (counterfactual) CANNOT be computed from Level 2 data alone, without structural assumptions.

This is not a practical limitation — it is a *mathematical impossibility*.
Simpson's paradox is the canonical demonstration: the same observational data is compatible with opposite interventional conclusions, depending on the causal structure.

### 3.3 The consequence for purposeful agents

A purposeful agent must select actions based on their *consequences* — on "what will happen IF I DO this" (Level 2), not on "what typically happens when this is observed" (Level 1).

*If M_t is a purely predictive model (Level 1), it cannot answer Level 2 questions.* The agent that selects actions based only on M_t's predictions (Level 1) will be misled whenever the observational distribution P(Y|X) differs from the interventional distribution P(Y|do(X)) — which is exactly when confounding is present.

**Therefore**: A purposeful agent operating in an environment with any non-trivial causal structure MUST maintain some representation of that causal structure — something beyond M_t's associational predictions — in order to correctly evaluate the consequences of its actions.

This "something" is what G_t provides at Level 2+. The causal structure might be:
- Implicit in the policy (Level 2 access through trial-and-error, without explicit causal representation — as in model-free RL)
- Encoded in a causal DAG (explicit structural causal model)
- Approximated by heuristics (rules of thumb about what causes what)
- Acquired through the feedback loop itself (the agent's action → observation cycle generates interventional data — Level 2 access by construction, even if the internal model is associational)

### 3.4 The feedback loop as a causal engine

**This is the key insight for LLM agents and the Pearl reconciliation.**

TF-02 already establishes that the agent's action-observation loop has causal structure by construction: a_t temporally precedes o_{t+1}, and the agent chose a_t. The mismatch signal δ_t conditioned on a_{t-1} is an *interventional* signal (TF-02, TF-06).

This means: **an agent embedded in the feedback loop achieves Level 2 epistemic access *through the loop*, regardless of whether its internal model M_t explicitly represents causal structure.**

An LLM with no causal DAG, operating in an action loop (write code → run tests → observe results → update plan → write code), achieves Level 2 access not through internal causal reasoning but through *actually intervening and observing consequences*. The loop provides the causal engine that the model architecture lacks.

In software, the agent even achieves Level 3: git checkout → implement alternative → observe difference provides *literal counterfactual evaluation* with ground-truth verification.

Pearl's objection (LLMs are Level 1 pattern matchers) is correct about the model *in isolation*. AAD's response: the model never operates in isolation. The feedback loop elevates the system's causal access beyond the model's internal level. The agent = model + loop, not model alone.

**Formal statement**: Let A be an agent with internal model M_t (Level 1 capacity) embedded in a feedback loop L with the environment. The composite system (A, L) has Level 2 capacity by construction (TF-02), because:
1. The agent selects actions (TF-07)
2. Actions causally affect the environment (TF-01)
3. Observations arrive post-action (temporal ordering, TF-02)
4. The mismatch signal conditioned on the action is interventional
5. The agent updates M_t from this interventional signal (TF-06)

The agent need not *represent* causal structure to *use* it. It gets causal structure for free from the loop. The cost: it must actually act and observe, which takes time and may be dangerous. This is exactly the exploration-exploitation tradeoff (TF-08) — the agent trades action for causal information.

---

## Part 4: What Causal Structure Must G_t Contain?

We've established: a purposeful agent needs causal structure beyond M_t to select actions based on consequences. Now: what *kind* of causal structure?

### 4.1 The minimal requirement

The agent needs to evaluate: P(outcome | do(action), M_t). This is a *conditional interventional query*. The agent asks: "given what I believe about the world (M_t), what outcome will my action produce?"

**If the action directly produces the outcome** (one-step causal chain), the agent just needs to know the action-outcome mapping: P(o_{t+1} | do(a_t), M_t). This is Level 2 access, achievable through the feedback loop alone. No explicit causal representation is needed beyond "try it and see."

**If the outcome requires a causal chain** (a_1 → intermediate_1 → a_2 → intermediate_2 → ... → outcome), the agent needs to represent:
1. The intermediate states and their ordering
2. The causal links between actions and intermediates
3. The confidence in each link

This is where the chain/graph structure becomes necessary.

### 4.2 The depth-fragility argument

Consider a causal chain of depth n: a_1 → s_1 → a_2 → s_2 → ... → O_t.

If each link succeeds with probability p, the chain confidence is p^n.
This is the compound probability decay that AAD already identifies (#260).

Five links at p = 0.9: chain confidence 0.59.
Ten links at p = 0.9: chain confidence 0.35.
Twenty links at p = 0.9: chain confidence 0.12.

This is not an assumption about DAGs — it is a *mathematical property of sequential uncertain causal chains*. Any representation of multi-step purposeful action that involves chained uncertain steps will exhibit this decay.

**Consequence**: Deep strategies are exponentially fragile. This creates structural pressure toward:
- Short chains (simple strategies)
- OR-branches (fallback paths if a link fails)
- High-confidence links (investing in certainty)
- Observability (monitoring link status to detect failure early)

These are properties the agent is *forced* toward by the mathematics, not design choices.

### 4.3 The combination problem

When multiple causal paths converge on a single outcome, how do they combine?

**AND combination**: All parents must succeed. The child succeeds with probability ≤ min(parent probabilities). Example: shipping a feature requires BOTH code AND tests AND documentation.

**OR combination**: Any parent suffices. The child succeeds with probability ≥ max(parent probabilities). Example: reaching a customer through email OR phone OR in-person.

The AND/OR distinction is not arbitrary — it reflects the *causal structure of the environment*. Some outcomes require conjunctive causes (all necessary); others respond to disjunctive causes (any sufficient). The agent's representation of its purpose must be able to express both.

**Why not just conditional probability tables?** Standard Bayesian networks use arbitrary CPTs (conditional probability tables) at each node. The AND/OR restriction is a structural simplification. It holds when:
- Each causal link is approximately independent (no interaction effects)
- The combination rule is purely conjunctive or purely disjunctive (no partial substitutability or complementarity)

When these conditions fail, richer combination rules are needed. The AND/OR semantics with single-parameter edges is the simplest faithful approximation — the claim is that it captures the dominant structure in most strategic/planning domains, not that it's universally exact.

This was validated empirically by the convergence across three independent formalism attempts (track-a-intent-dag/).

### 4.4 Where we are

We've derived:
1. A purposeful agent needs *something* beyond M_t (from the causal hierarchy theorem)
2. This something must represent action-consequence chains when the environment has multi-step causal structure
3. Chain confidence decays exponentially with depth (mathematical necessity)
4. Convergent causal paths combine via AND/OR rules (from the structure of conjunctive/disjunctive causation)
5. The agent achieves Level 2 access through the feedback loop even without internal causal representation

The result looks like... a causal DAG with AND/OR nodes and confidence- weighted edges. But we didn't assume it — we were pushed toward it by the mathematics of multi-step uncertain causal reasoning.

---

## Part 5: The Emergence of the O_t / Σ_t Split

### 5.1 When does purpose decompose?

At Level 1 (reference signal), G_t = r_t. There's no split — the goal IS the representation.

At Level 2 (evaluation function), G_t = U(s, a). Still no split — the utility function encodes both "what is desirable" and (implicitly through optimization) "what to do."

At Level 3+ (subgoal decomposition / causal model), the agent must represent both:
- **What it wants** (the destination, the desired end-state)
- **How it thinks it can get there** (the path, the causal chain, the plan)

These are *different kinds of information* that *may* update at different rates.

### 5.1a Scope narrowing: Timescale-separated purposeful agents

**CAUTION**: The claim that goals are always more stable than plans is NOT derived. It's empirically common but not universal:
- A startup pivoting weekly has ν_O > ν_Σ (goals change faster than plans, because each new goal inherits the same basic approach)
- A bureaucrat with rigid procedures has ν_Σ < ν_O (the plan never changes even when the objectives shift)
- An agent in crisis may have ν_O ≈ ν_Σ (everything in flux)

What IS derivable: when G_t contains multiple components that respond to different evidence types with different arrival rates, SOME timescale separation will emerge. This is a general property of multi-component adaptive systems (singular perturbation theory, TF-11's temporal nesting). The specific identification of O_t as "slow" and Σ_t as "fast" is a modeling choice that is APPROPRIATE when goals are more stable than plans — a condition true for many interesting agents but not all.

*[Scope Narrowing]*

We narrow to agents where the purposeful state G_t has components with distinct update frequencies: some components update in response to frequent tactical evidence (strategy), others update in response to rare strategic evidence (objectives). For such agents, the O_t/Σ_t decomposition is the natural partition along the dominant timescale boundary.

**Justification**: This scope includes most purposeful agents that humans care about (commanders, developers, organizations, autonomous systems with defined missions). The excluded cases (agents with unified-timescale purpose, or with reversed timescale ordering) are real but less common as long-running purposeful systems.

**What this buys us**: TF-11's temporal nesting constraint applies:
ν_Σ ≫ ν_O (strategy adapts much faster than objectives). The faster component should approximately converge before the slower component acts on its output. If objectives are revised before the strategy has had time to test them, the agent is "pivoting prematurely" — acting on transient performance rather than settled dynamics. This is TF-10's conservatism principle applied to purpose.

**Broader framing**: Any G_t that contains heterogeneous components will decompose along its dominant timescale boundaries. O_t/Σ_t is the two-level case. Real agents may have additional levels: mission → objectives → strategy → tactics → reflexes. The O_t/Σ_t framework is the simplest non-trivial case, just as TF-10's parametric/structural distinction is the simplest non-trivial timescale boundary for M_t.

### 5.2 Directed separation, derived

**M_t is independent of G_t.**

M_t tracks reality — it updates from observations, which don't depend on what the agent wants. The world doesn't change its dynamics because the agent has a goal. (This is a scope assumption: we're not in the regime where the agent's *declaration* of a goal changes the environment's behavior — though that regime exists in game theory and social dynamics.)

*Formally*: M_{t+1} = f(M_t, o_{t+1}). The observation o_{t+1} depends on Ω_t (world state) and a_t (agent's action), but NOT on G_t directly. M's update function has no G_t dependence.

**G_t depends on M_t.**

The strategy Σ_t must reference the reality model to evaluate which causal chains are currently viable. An edge confidence p_ij in the strategy should be updated when M_t reveals new information about the link (e.g., the agent observes that a prerequisite has been achieved or blocked).

O_t may also depend on M_t: a goal may be abandoned when the reality model shows it's infeasible. But this is a slow process — O_t revision requires strong evidence that no strategy can bridge the gap.

**Action couples all three.**

The policy π(M_t, G_t) selects actions that depend on both the reality model and the purposeful state. Actions affect the world (changing Ω_t), which changes observations, which updates M_t, which triggers G_t revision. The coupling is through the action-observation-update cycle, not through direct state dependence.

This is exactly AAD's #250 (directed separation), but derived from the different update sources rather than assumed.

---

## Part 6: The Three Mismatch Types — Derived

### 6.1 What can go wrong?

With M_t and G_t = (O_t, Σ_t) both in play, there are three distinct kinds of discrepancy between the agent's state and reality:

### 6.2 δ_epistemic: Reality model error

    δ_epistemic = o_t − ô_t

This is Section I's mismatch signal, unchanged. The agent's predictions about reality don't match observations. **Update source**: observations. **Timescale**: fastest (every observation cycle). **Correction**: gain- weighted model update (TF-06).

### 6.3 δ_objective: Goal-state gap

    δ_objective = O_t − M_t(relevant dimensions)

The world is not in the state the agent wants it to be in. This is the simplest purposeful mismatch — the distance between "where I am" (M_t) and "where I want to be" (O_t). **Update source**: M_t updates (changes in the agent's understanding of current state). **Timescale**: intermediate. **Correction**: action selection (pursue the goal).

**Note**: δ_objective being large is *normal* — it's why the agent is acting. δ_objective being small means the goal is nearly achieved or the agent has given up and moved the goalposts. The pathology is not large δ_objective but *unchanging* δ_objective despite sustained action.

### 6.4 δ_strategic: Strategy-effectiveness error

This is the tricky one — the one the contents marks as "least crisp."

    δ_strategic = E[progress | Σ_t, actions taken] − observed progress

The agent's *strategy* predicts that its actions should be producing progress toward O_t. If the agent is executing its strategy with adequate M_t (low δ_epistemic) and δ_objective is not decreasing, then the strategy itself is wrong.

**Why this is second-order**: δ_strategic is not a direct observation- vs-prediction error. It's an inference from the *pattern* of δ_objective over time:

    If (δ_epistemic is small) AND (actions follow Σ_t) AND
       (δ_objective is not decreasing):
    Then (Σ_t is likely wrong)

This requires accumulating evidence over multiple action cycles.
δ_strategic is inherently slower to detect than δ_epistemic.

**Formal attempt**: Define δ_strategic as a likelihood ratio.

Let p_critical be the edge confidence on the critical path of Σ_t.
Let progress_observed be the rate of δ_objective reduction.
Let progress_predicted = f(p_critical, actions taken, time).

    δ_strategic = progress_predicted − progress_observed

When δ_strategic > 0 persistently (the strategy predicts more progress than is observed), at least one edge confidence p_ij is too high — the strategy is overconfident about a causal link.

### 6.5 The interaction ordering

**Claim**: δ_epistemic must be resolved before δ_strategic is meaningful.

If δ_epistemic is large (the agent misunderstands reality), then δ_objective may be wrong (the agent doesn't know how far it is from the goal) and δ_strategic is meaningless (the "lack of progress" might be a measurement error, not a strategy failure).

This gives a natural resolution ordering:
1. First: reduce δ_epistemic (understand reality — the Orient phase)
2. Then: evaluate δ_objective (assess how far from the goal)
3. Then: evaluate δ_strategic (assess whether the strategy is working)
4. If δ_strategic is high: revise Σ_t (strategy adaptation)
5. If δ_strategic persists across strategy revisions: revise O_t (goal adaptation)

This IS the orient cascade (#280), derived from the logical dependency between the mismatch types rather than assumed.

---

## Part 7: The Purposeful Persistence Condition

If M_t has a persistence condition (T > ρ / ‖δ_critical‖), does G_t have one too?

### 7.1 Strategy persistence

Σ_t must be revised fast enough to keep up with changes that affect its edge confidences. If the environment changes and a causal link in the strategy breaks (p_ij drops because circumstances changed), the agent must detect this and revise before the broken link leads to wasted action.

Define T_Σ: the rate at which the agent detects and corrects strategy errors. This combines:
- Observation channels that reveal edge status (can the agent see whether step j is proceeding?)
- The agent's capacity to revise the strategy (how quickly can it re-plan?)

Define ρ_Σ: the rate at which the environment invalidates strategy edges.
Requirements change, obstacles appear, resources become unavailable.

Then: Σ_t persists (remains viable) iff T_Σ > ρ_Σ / ‖δ_Σ_critical‖

**This is a structural parallel** to M_t's persistence condition, and it's motivated by the same mathematics (the general sector-condition argument from Appendix A doesn't depend on what the "mismatch" represents — it applies to any system with correction dynamics and bounded disturbance).

### 7.2 Objective persistence

O_t is more stable by assumption — objectives change slowly. But they CAN be invalidated:
- Infeasibility: M_t reveals that no viable Σ_t can bridge to O_t
- Irrelevance: The environment has changed so much that O_t is no longer the right goal
- Achievement: O_t is reached and a new goal is needed

Objective revision is the slowest timescale, consistent with TF-11's temporal nesting constraint: ν_M ≫ ν_Σ ≫ ν_O.

---

## Part 8: What Does This Mean for the Theory Structure?

### 8.1 Summary: what's derived vs. scope-narrowed

Starting from "the simplest possible purposeful state" and squeezing, distinguishing *derived* results (mathematical necessity) from *scope narrowings* (explicit restrictions with justification):

**Derived** (mathematical necessity):
1. Purposeful agents need Level 2 (interventional) reasoning to select actions based on consequences. (Causal hierarchy theorem.)
2. The feedback loop provides Level 2 access even to agents without internal causal models. (TF-02 + temporal ordering.)
3. Multi-step action plans exhibit exponential fragility — p^n decay.
   (Mathematical property of chained uncertain steps.)
4. Convergent causes require AND/OR combination rules. (From the structure of conjunctive/disjunctive causation.)
5. Directed separation follows from different update sources: M_t from observations (which don't depend on G_t), G_t from evaluation of progress (which depends on M_t). Coupling is through action only.
6. Three mismatch types emerge from the M_t + G_t hierarchy, with a resolution ordering (δ_epistemic before δ_strategic) following from logical dependency — you can't evaluate strategy quality with a broken reality model.
7. Strategy persistence parallels model persistence: the sector- condition mathematics applies to any bounded-correction system with bounded disturbance, regardless of what the "mismatch" represents.

**Scope narrowings** (explicit restrictions):
A. *Agents in non-trivial causal environments*: We restrict to agents
   where the action-outcome mapping has sufficient causal complexity that Level 1 (associational) reasoning is inadequate. Justification: this is where purposeful behavior becomes non-trivial.
B. *Agents where planning is cheaper than experimentation*: We restrict
   to agents where mental simulation costs less than physical trial-and- error. Justification: temporal optimality (#010) then selects for explicit causal models. This rules out cheap-simulation domains where model-free RL is legitimately preferred.
C. *Agents with timescale-separated purposeful state*: We restrict to
   agents where G_t has components that update at different frequencies.
   Justification: this is where the O_t/Σ_t decomposition is natural.
   It excludes agents with unified-timescale purpose (rare among long- running purposeful systems) or reversed timescale ordering.
D. *AND/OR with single-parameter edges*: We restrict to environments
   where causal combination is approximately conjunctive or disjunctive, without strong interaction effects. Justification: converged across three independent formalism attempts, but this is an empirical observation about the structure of most strategic/planning domains, not a derivation.

### 8.2 Proposed Section II restructuring

The current contents (#210–#350) assume the DAG and then explore its properties. The derivation above suggests a different structure: **progressive scoping**, where each step is either a derivation or an explicit scope narrowing.

**Proposed flow:**

1. **G_t as minimal purposeful state** — Definition. The agent has *some* representation of what it wants. No structure assumed. (Currently #210 agent-spectrum can stay, but G_t definition is new.)

2. **Purposeful action requires Level 2 access** — Derived (from causal hierarchy theorem). The agent cannot select actions based on consequences using only Level 1 reasoning. This is a mathematical proof, not an assumption.

3. **The feedback loop provides Level 2 access** — Derived (from TF-02 + temporal ordering). This connects the adaptive-systems foundation to purposeful agency. An agent in the loop achieves Level 2 by construction, even without internal causal structure. *(This is also the LLM-in-loop theorem — Pearl reconciliation.)*

4. **Scope narrowing: planning-capable agents** — Scope. We restrict to agents where mental simulation is cheaper than physical experimentation. By #post-temporal-optimality, these agents are driven toward explicit causal models of their purpose.

5. **Multi-step fragility** — Derived (mathematical property of chained uncertain steps). p^n decay. This is not DAG-specific.

6. **Scope narrowing: timescale-separated purpose** — Scope. We restrict to agents where G_t components update at different frequencies. This gives us the O_t/Σ_t decomposition.

7. **Directed separation** — Derived (from different update sources).
   M_t independent of G_t. G_t depends on M_t. Action couples all.

8. **Three mismatch types** — Derived (from M_t + G_t structure).
   δ_epistemic, δ_objective, δ_strategic, with resolution ordering.

9. **Orient cascade** — Derived (from mismatch interaction ordering).
   Reduce δ_epistemic before evaluating δ_strategic.

10. **Scope narrowing: AND/OR environments** — Scope. We restrict to environments where causal combination is approximately conjunctive or disjunctive. This gives us the DAG with AND/OR semantics.

11. **Strategy DAG formalism** — Definition. Σ_t = (V, E, p, γ) with the AND/OR semantics. NOW the DAG is introduced — motivated by everything above.

12. **Strategy persistence** — Derived (from sector-condition mathematics applied to Σ_t mismatch).

**What this buys**: Each step is either derived or explicitly scoped.
The reader knows exactly where the generality narrows and why. The excluded systems (agents without timescale separation, agents in cheap- simulation environments, agents in non-AND/OR causal structures) are honestly acknowledged as out-of-scope — unexplored paths for future work, not hidden assumptions.

**What this costs**: More claims in Section II (12 vs current ~15, but structured differently). Some current claims get absorbed or reordered. The agent-spectrum (#210) and objective (#220) definitions survive but move to after the scope narrowings that motivate them.

### 8.2a Methodological note: scope narrowings as gifts

Each scope narrowing in the proposed structure does double duty:

1. **For the current theory**: It honestly marks where generality ends and specific commitment begins, preventing hand-waving from masquerading as derivation.

2. **For future work**: It clearly marks *divergence points* — places where a different researcher could take a different path. "What happens for agents without timescale-separated purpose?" is not a failure of AAD — it's an explicitly marked research question that AAD's structure makes precise.

This is better than the common theoretical practice of making assumptions silently (so they're invisible) or stating them as axioms (which implies they can't be questioned). Scope narrowings say: "we could go either way here; we're choosing this direction for these reasons; the other direction is legitimate and unexplored."

The progressive scoping structure also tightens the theory's claims:
each result holds for the *intersection* of all prior scopes. A claim about "purposeful agents with timescale-separated purpose in AND/OR environments where planning is cheaper than experimentation" is more honest (and more precisely testable) than a claim about "purposeful agents in general."

### 8.3 What's still assumed (not derived)

- AND/OR with single-parameter edges as the best DAG variant (converged empirically across three formalisms, not derived from first principles)
- The specific update rule for edge confidences (the gain principle
  #290 applied to strategy edges — plausible by analogy but not
  independently validated)
- DAG acyclicity (an assumption, not forced — real control loops are cyclic; acyclicity holds after time-unrolling)
- The specific cognitive cost structure (no β analog for Σ_t yet)

### 8.4 What's still open

- **The edge identifiability problem**: Σ_t edges claim interventional semantics (p_ij = P(j | do(i), M_t)) but may be updated from observational data. In confounded domains, this is a real problem. In software (where genuine interventions are available), it's less severe. Resolution may come from the software domain pushing requirements back up.

- **Temporal structure in the DAG**: Current DAG has no explicit temporal ordering among actions. Real strategies have sequential dependencies ("do A before B"). This might need to be added as edge metadata or node ordering.

- **Resource constraints**: The DAG doesn't represent resource budgets, commitment costs, or opportunity costs. A full intention theory would need these. Current AAD defers this.

### 8.5 The G_t / M_t compatibility constraint

An insight that emerged during review: the useful complexity of G_t is *bounded by* the capacity of M_t.

A Level 1 G_t (reference signal) works with any M_t. It just needs M_t to report the agent's current state in the relevant dimensions.

A Level 3+ G_t (subgoal decomposition, causal DAG) requires M_t to have sufficient fidelity to evaluate the DAG's edge confidences. The agent needs M_t to answer: "has prerequisite r_1 been achieved?" and "is the causal link between action a_j and outcome s_k still viable?" These are increasingly demanding questions.

*[Derived]*

The useful complexity of G_t is bounded by the evaluative capacity of M_t:

    effective_complexity(G_t) ≤ f(S(M_t), M_capacity)

where S(M_t) is model sufficiency and M_capacity is the richness of M_t's state representation.

**Consequence**: You can't have a sophisticated strategy with a crude reality model. An elaborate 50-node strategy DAG is useless if M_t can't tell you which edges are intact. The strategy's evaluability depends on M_t's observational reach.

**Connection to the orient cascade**: This is another reason why δ_epistemic must be resolved before δ_strategic can be evaluated — not just because a wrong M_t gives wrong evaluations, but because a *poor* M_t limits how much of G_t is even evaluable. An agent with low S(M_t) should have a correspondingly simple G_t, because the extra structure would be invisible to evaluation anyway.

**Connection to structural adaptation**: When the agent upgrades M_t's model class (TF-10 structural adaptation), it also expands the evaluable complexity of G_t. This creates a virtuous cycle: better M_t → can support richer G_t → more sophisticated purposeful action → better-directed exploration → faster M_t improvement.

And a vicious one: if M_t degrades, the effective complexity of G_t shrinks — the agent is forced to simplify its strategy because it can no longer evaluate the complex one. Under adversarial pressure (effects spiral), this manifests as "the agent's plans become increasingly crude as its model collapses."

---

## Part 9: Connection to the Software Domain

The derivation above has a specific payoff for TST grounding:

**Software developers operate at Level 2-3 naturally.** When a developer runs a test, they perform do(change) → observe(test result). When they git bisect, they perform counterfactual evaluation. Software is the domain where Pearl's hierarchy is most directly accessible — and AAD formalizes why.

**The developer's G_t is explicit.** A developer's O_t is the task ("implement OAuth"). Their Σ_t is the plan (an AND/OR structure: need BOTH auth flow AND token storage AND rate limiting; each achievable through multiple approaches). This plan is often literally written down (in a ticket, a TODO list, or a PLANS.md).

**Code quality affects ALL mismatch types.** Poor code quality:
- Raises δ_epistemic (harder to understand the codebase → worse M_t)
- Raises δ_strategic (harder to evaluate whether the plan is working)
- Doesn't directly affect δ_objective (the goal-state gap is the same) but DOES affect the agent's MEASUREMENT of δ_objective through M_t

This connects "code quality as observation infrastructure" (#590) directly to the three-mismatch-types framework.

---

## Part 10: Residual Puzzles

### 10.1 M_t already contains causal structure?

One might object: M_t in a sufficiently rich model class could *already* represent causal structure. A Bayesian network IS a causal model. A neural network trained on interventional data implicitly learns causal relationships.

Response: Yes, and when M_t's model class includes causal structure, the agent effectively has Level 2 access through M_t alone. The question is whether to carve this out as G_t or leave it embedded in M_t.

The argument for separating G_t: the purposeful component has *different update dynamics* (timescale separation, different correction sources) and *different adequacy criteria* (action-guiding vs. predictive) from the reality-tracking component. Lumping them together makes the theory less modular and harder to analyze.

The argument for NOT separating: some agents genuinely have a unified model that combines prediction and action-guidance (model-based RL, active inference). For these agents, the M_t/G_t separation is an analytical convenience, not a structural fact.

**Resolution**: M_t and G_t are *analytical distinctions*, not necessarily architectural ones. Some agents implement them in separate data structures (PID controller + setpoint). Others merge them (model- based RL with learned reward). The theory analyzes them separately because they have different dynamics, but acknowledges that the implementation may merge them.

### 10.2 Is this just active inference?

Active inference (Friston) also derives purposeful behavior from an epistemic framework. The agent minimizes expected free energy, which decomposes into epistemic value (exploration) and instrumental value (exploitation). Prior preferences (the analog of O_t) shape the generative model.

Similarities:
- Both derive purpose from information-theoretic principles
- Both ground exploration and exploitation in a unified objective
- Both make the feedback loop central

Differences:
- AAD uses causal feedback dynamics (mismatch → gain → tempo); active inference uses variational free energy
- AAD's purposeful state is explicit (G_t with possible DAG structure);
  active inference embeds preferences in the generative model
- AAD's derivation uses Pearl's causal hierarchy directly; active inference uses the free energy principle's blanket formalism
- AAD is more transparent and measurable (the claim); active inference is more general (their claim)

**Open question**: Is there a formal mapping between AAD's G_t and active inference's prior preferences + expected free energy? If so, AAD and active inference may be different coordinate systems for the same underlying mathematics.

### 10.3 The transition from loop-based to model-based causal access

The weakest link: the transition from "the agent needs Level 2 access" to "the agent needs an explicit causal representation in G_t."

The feedback loop provides Level 2 access *without* explicit causal representation. An agent could just try actions and observe consequences indefinitely, never building an internal causal model, and still achieve purposeful behavior through trial and error.

**Two modes of Level 2 access:**

*Loop-based* (model-free): The agent acts, observes consequences, adjusts. Level 2 access comes from the physical act-observe cycle. Cost: real actions, real time, real consequences. The agent must explore in the world.

*Model-based* (explicit G_t with causal structure): The agent simulates interventions internally — "what would happen if I do(X)?" — using its causal model. Level 2 access comes from mental simulation. Cost: computation time, model inaccuracy. The agent explores in its head.

Both achieve the same epistemic goal (Level 2 access). They differ in temporal cost.

*[Scope Narrowing via #post-temporal-optimality]*

We narrow to agents where mental simulation (planning) is cheaper than physical experimentation (trial-and-error) for the class of action- consequence queries the agent faces. For such agents, the explicit causal model is *temporally optimal* — it achieves the same outcomes in less time. By the temporal optimality axiom (#010), the agent with the explicit model is preferred.

**Justification**: This scope includes nearly all multi-step purposeful agents in non-trivial environments. Trial-and-error is cheaper than planning only when: (a) actions are cheap and fast, (b) consequences are immediately observable, (c) failure is reversible, and (d) the environment doesn't change during exploration. When any of these fail (which is most interesting environments), planning wins on time.

**What this buys us**: The explicit causal model (a structured G_t that supports mental intervention queries) is now *derived* as the temporally optimal representation for purposeful agents in environments where physical exploration is costly relative to mental simulation. The DAG (or whatever structural form G_t takes) isn't just useful — it's what temporal optimality selects for.

**The beautiful connection**: This makes #post-temporal-optimality genuinely load-bearing for the purposeful agency layer, not just a meta-principle. It does real theoretical work: it narrows us from "any Level 2 access mechanism" to "explicit causal models" by ruling out the temporally suboptimal (but epistemically equivalent) trial-and-error alternative.

**Limitation**: The scope narrowing is one-directional. It says explicit causal models are preferred WHERE planning is cheaper than acting. It does not claim all agents have them or should. Model-free RL agents operating in cheap simulation environments (Atari, simple robotics) may legitimately prefer loop-based access because the environment itself serves as a fast simulator. The narrowing excludes them from scope, not from existence.

---

## Part 11: Codex Review Integration (same session)

Codex reviewed the spike with fresh eyes and identified seven structural issues. This section records them, assesses each, and sketches the fixes for the next revision. The body of Parts 1-10 is preserved as-is for context — the corrections here supersede specific claims above.

### 11.1 State completeness (CRITICAL — must fix)

**Problem**: TF-03 defines M_t as the agent's *complete* internal state.
TF-07 derives action as a function of M_t alone: a_t = π(M_t). The spike introduces G_t as a *separate* state and writes π(M_t, G_t), which contradicts TF-03's completeness claim.

**Fix**: Lift the complete state to X_t = (M_t, G_t). TF-03's claims apply to X_t. M_t becomes the **epistemic substate** (beliefs about reality). G_t becomes the **purposeful substate** (goals and plans). The recursive update becomes:

    X_{t+1} = f(X_t, o_t, a_t)

which decomposes as:

    M_{t+1} = f_M(M_t, o_{t+1}, a_t)        -- epistemic update G_{t+1} = f_G(G_t, M_{t+1}, feedback_t)  -- purposeful update

The directed separation claim becomes precise:
- f_M has no G_t dependence (reality doesn't care about your goals)
- f_G depends on M_t (strategy evaluation needs the reality model)
- π depends on both: a_t = π(M_t, G_t)
- Closed-loop M transition depends on G_t through π → a_t → o_{t+1}

**Impact**: This is a foundational fix that makes AAD's extension of TFT formally clean. Section I agents have X_t = (M_t, ∅) — the purposeful substate is empty. Section II adds G_t ≠ ∅.

This also addresses Codex's point 6: the precise claim is that f_M is independent of G_t (the epistemic update function doesn't reference purpose), not that M_t's closed-loop trajectory is independent of G_t (it isn't, because actions depend on G_t).

### 11.2 Level 2 claim too strong (must weaken)

**Problem**: The spike claims "purposeful agents need Level 2 access" as derived. But a PID controller with a setpoint is purposeful and operates at Level 1. A pre-compiled LQR controller is purposeful at Level 1. The causal hierarchy theorem proves Level 2 is needed for *learning* action consequences, not for *executing* pre-compiled action consequences.

**Fix**: The correct claim is: purposeful agents that must *learn about* or *disambiguate* action consequences during operation need Level 2 access. Pre-compiled controllers have Level 2 knowledge baked in by the designer — the designer did the causal reasoning at design time, not the agent at runtime.

**Revised derivation**: The causal hierarchy theorem tells us that Level 2 KNOWLEDGE is required to select actions based on consequences. This knowledge can be: (a) Pre-compiled into the agent by the designer (PID, LQR, hardcoded
    policy) — the agent operates at Level 1 online, using Level 2 knowledge that was derived offline.
(b) Acquired through the feedback loop at runtime (RL, model-based
    planning, LLM in a loop) — the agent must achieve Level 2 access during operation.
(c) Absorbed from training data (LLM language priors) — Level 2
    knowledge encoded in the model from causally-structured data.

The scope narrowing should be: "We consider agents that must acquire or refine Level 2 knowledge during operation (cases b and c), as opposed to agents with pre-compiled Level 2 knowledge (case a)."

This actually strengthens the argument: pre-compiled controllers are explicitly out of scope, and the agents we're studying are exactly those for whom the loop and/or training provide Level 2 access.

### 11.3 Conflation of objective and strategy richness (must restructure)

**Problem**: The G_t hierarchy (Levels 0-4) mixes two independent dimensions — how rich is the agent's representation of WHAT it wants (objective) vs. HOW it plans to get it (strategy). The non-convexity argument proves the need for richer strategy, not richer objective. A point goal + a good planner handles non-convex landscapes fine.

**Fix**: Split into two independent dimensions:

**Objective richness** (O_t representations, ordered by expressiveness):
- Point target: r_t ∈ S
- Target set/region: O_t ⊆ S
- Constraint set: O_t = {s : g_i(s) ≤ 0 ∀i}
- Utility/reward function: U: S × A → ℝ
- Trajectory functional: J: trajectories → ℝ (handles path-dependent goals like "migrate with zero downtime")

**Strategy richness** (Σ_t representations, ordered by expressiveness):
- None (reactive/reflexive — implicit in π)
- Cached policy (lookup table, trained network)
- Subgoal sequence with ordering
- Causal DAG with confidence weights (AND/OR, the current Σ_t)

**Consequence**: The O_t/Σ_t split is not a late emergence from timescale separation — it's the recognition that objectives and strategies are DIFFERENT KINDS OF INFORMATION that naturally separate because they vary along independent dimensions. The timescale separation (ν_O < ν_Σ for many interesting agents) is a further empirical observation about their dynamics, not the reason for the split.

This means the O_t/Σ_t split should happen EARLY in Section II — as a definitional observation about the structure of purposeful state, not as a derived consequence of dynamics.

**Codex's further suggestion**: Introduce O_t as the missing state that parametrizes TF-08's currently unexplained "value" term in the unified policy objective. This is a *much* cleaner insertion point than starting from zero — TF-08 already has the placeholder; O_t fills it.

### 11.4 Mismatch mathematics too narrow (must generalize)

**Problem**: δ_objective = O_t − M_t only works for point targets in the same vector space as the state estimate. For utility functions, constraint satisfaction, or trajectory functionals, the mismatch needs a different form.

**Fix**: Replace with more general forms:

- δ_objective as **satisfaction functional**:
  For point target: δ_O = ‖r_t − M_t(relevant)‖ (current form) For constraint set: δ_O = Σ max(0, g_i(M_t))  (violation magnitude) For utility: δ_O = U_max − E[U(s) | M_t, π] (regret) For trajectory: δ_O = J* − E[J(τ) | M_t, π] (trajectory regret)

- δ_strategic as **calibration residual** (Bellman-style):
  δ_Σ = E[progress | Σ_t, M_t, actions] − observed_progress

  More precisely: the strategy predicts that executing step k should yield outcome with probability p_k. The calibration residual is the systematic deviation between predicted and observed step outcomes. This is a proper calibration measure, not just a progress-rate difference.

### 11.5 p^n fragility is narrower than claimed (must qualify)

**Problem**: The p^n decay assumes one-shot sequential chains with independent, uniformly-bounded conditional success. With retries, monitoring, contingent branching, or correlated failures, the relevant quantity is more complex.

**Fix**: The robust result is **additive log-confidence growth** (or equivalently, multiplicative confidence decay):

    log P(chain) = Σ log P(E_i | E_{<i})

This is the general form. p^n is the special case where all conditional probabilities are equal and independent. The qualitative insight — "longer chains are less confident" — is robust. The specific form p^n is a simplification.

AND/OR composition remains an approximation family (scope narrowing D), not derived. The spike already correctly reclassified it in Part 8.1.

### 11.6 Strategy persistence is a theorem schema (must frame correctly)

**Problem**: The spike states the strategy persistence condition by analogy with model persistence, but hasn't defined the strategic error state, correction operator, or disturbance class needed to apply the sector-condition framework.

**Fix**: Frame as a theorem schema: "If strategic update dynamics satisfy assumptions analogous to (A1), (A2'), and bounded disturbance, then an analogous persistence threshold follows." Making this a full theorem requires:
- Defining the strategic mismatch state (the analog of δ for Σ_t)
- Defining the strategic correction function (how Σ_t updates in response to strategic mismatch)
- Showing this correction function satisfies a sector condition
- Identifying the strategic disturbance (rate at which the environment invalidates strategy edges)

This is genuine future work, not a gap that can be hand-waved.

### 11.7 Promising paths from Codex

Three suggestions that should inform the next revision:

**(a) O_t parametrizes TF-08's value term.** TF-08 already has:
    π*(M_t) = argmax_a [E[value(a)|M_t] + λ(M_t)·CIY(a; M_t)]

The "value" term is currently unexplained within TFT — it's just "expected value." O_t provides the missing parametrization: value(a) = E[progress toward O_t given action a and model M_t]. This is a MUCH cleaner insertion point for purpose than starting from scratch. It means Section II doesn't introduce a new policy objective — it fills the gap in the existing one.

**(b) Objective as trajectory functional.** Instead of O_t ∈ S (point target), define O_t as J: trajectories → ℝ. This handles:
- Point targets: J(τ) = -‖τ_final − r‖
- Constraints: J(τ) = -Σ violation(τ_t)
- "Ship without breaking auth": J(τ) penalizes trajectories where auth tests fail at any point
- "Zero-downtime migration": J(τ) penalizes trajectories with any period of unavailability

Reference signals, target sets, utilities, and temporal-logic constraints are all special cases. This is genuinely more general and avoids the spike's current limitation (point-valued δ_objective).

**(c) Cost inequality for deriving Σ_t.** Instead of relying on Pearl's hierarchy alone, derive the need for explicit Σ_t from:

    cost(planning + maintaining Σ_t) < cost(real-world exploration + repair)

This makes temporal optimality load-bearing through a *concrete inequality* rather than a scope-narrowing appeal. The action-fluency story from TF-07 becomes directly relevant: when should the agent invest in explicit strategic representation vs. rely on implicit (loop-based) causal access?

### 11.8 Revised derivation sketch (post-Codex)

Incorporating all fixes, the cleaner derivation would be:

1. **X_t = (M_t, G_t)** — Formulation. The complete agent state has an epistemic substate and a purposeful substate. Section I agents have G_t = ∅.

2. **O_t parametrizes value** — Definition. O_t is the missing state that gives meaning to TF-08's "value" term. This fills a gap in TFT, not a new invention.

3. **O_t and Σ_t are independent dimensions** — Definition. Objective richness (what to want) and strategy richness (how to get it) vary independently. The split is definitional, not dynamic.

4. **Causal hierarchy theorem** — Derived. Agents that must learn about action consequences need Level 2 knowledge. (Scope: excludes pre- compiled controllers.)

5. **The loop provides Level 2** — Derived (TF-02). Agents in the feedback loop achieve Level 2 by construction.

6. **Cost inequality for explicit Σ_t** — Derived (via #temporal- optimality). When planning is cheaper than experimentation, explicit Σ_t is temporally optimal. Cost inequality makes #010 genuinely load-bearing.

7. **Additive log-confidence in causal chains** — Derived. The robust result. p^n is the independent-uniform special case. Qualitative implication: deeper strategies are less confident.

8. **Scope narrowing: timescale-separated purpose** — Scope. For agents where O_t and Σ_t update at different frequencies, temporal nesting constraints apply.

9. **Scope narrowing: AND/OR environments** — Scope. For environments with approximately conjunctive/disjunctive causal combination.

10. **Three mismatch types** — Derived. δ_epistemic (from M_t), δ_objective (satisfaction functional on O_t), δ_strategic (calibration residual on Σ_t). Resolution ordering derived from G_t/M_t compatibility constraint.

11. **Directed separation** — Derived. f_M is G_t-independent. f_G depends on M_t. Coupling through action channel only.

12. **Strategy persistence** — Theorem schema. If strategic dynamics satisfy sector conditions, analogous threshold follows. Full theorem awaits definition of strategic error state.
