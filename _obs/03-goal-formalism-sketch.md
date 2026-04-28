# The G_t Formalism: First Sketch

**Status**: First attempt at the mathematics. This is thinking-on-paper, not a finished formulation. Expect errors, dead ends, and revision. The goal is to get enough structure on the page that we can see what works and what doesn't.

**Approach**: Mirror TFT's structure wherever the parallel holds, then identify where it breaks and new machinery is needed.

---

## 1. Definitions

### 1.1 The Goal Model

*[Definition (goal-model)]*

    G_t = psi(I_t)

where:
- G_t is the agent's current goal — a compressed representation of the desired future state, drawn from model space S
- psi is the goal-compression function
- I_t is the **intent history** — the stream of goal-relevant inputs the agent has received

G_t and M_t live in the same state space S. The Kalman estimate x_hat_t and the LQR reference x_ref are both in R^n. The developer's mental model of the codebase and the feature spec both describe "a codebase state."

### 1.2 Intent History

*[Definition (intent-history)]*

    I_t = (g_1, r_1, g_2, r_2, ..., g_t)

where:
- g_i are **intent signals**: specifications, commands, discovered opportunities, feasibility discoveries, higher-level goal decompositions
- r_i are **revision signals**: feedback about whether the current goal is being achieved, is feasible, or should change

I_t is to G_t what C_t (interaction history) is to M_t. Note that I_t is NOT a subset of C_t — intent signals come from different sources than observations. A specification arrives from a stakeholder, not from the environment. A commander's intent arrives from above, not from the battlefield.

However, some intent signals ARE triggered by observations — the discovery that a goal is infeasible comes from observing reality. So I_t and C_t are coupled but distinct streams.

### 1.3 Goal Uncertainty

*[Definition (goal-uncertainty)]*

    U_G = Var_G[desired_outcome]

The agent's uncertainty about what it actually wants. Sources:

- **Specification ambiguity**: "make it fast" — how fast?
- **Incomplete decomposition**: the high-level goal is clear but the sub-goals haven't been worked out
- **Competing objectives**: speed vs. quality vs. cost — the tradeoff isn't resolved
- **Evolving preferences**: the stakeholder doesn't know what they want yet
- **Conditional goals**: "if X is feasible, do X; otherwise do Y" — the goal is a function of yet-to-be-discovered reality

U_G is NOT the same as the distance from the goal (that's ||delta_goal||).
U_G is uncertainty about the goal *itself* — the agent is unsure of its destination, not just far from it.

**Domain instantiations of U_G:**

| Domain | Low U_G | High U_G |
|--------|---------|----------|
| PID | Precise setpoint (r_t = 72°F) | Variable setpoint (track time-varying reference) |
| Software | Clear, unambiguous spec | Vague user story, "improve performance" |
| Military | Specific objective (take the bridge) | Strategic intent (disrupt enemy logistics) |
| RL | Well-defined reward function | Reward shaping still being tuned |
| Startup | Clear product-market fit | Searching for product-market fit |

The Auftragstaktik insight: the *optimal* U_G is not zero. Over-specified goals (U_G ≈ 0) prevent directed opportunism. The agent needs enough goal uncertainty to recognize and exploit opportunities the goal-setter couldn't foresee.

---

## 2. The Three Mismatch Signals

### 2.1 Epistemic Mismatch (TFT's delta — unchanged)

*[Definition — from TF-05]*

    delta_epistemic = o_t - hat{o}_t

"My model of reality is wrong." Drives model updating.

### 2.2 Goal-Reality Mismatch

*[Definition (goal-reality-mismatch)]*

    delta_goal = G_t - M_t

"Reality (as I understand it) isn't where I want it."

Critical subtlety: the agent can't observe delta_goal_true = G_t - Omega_t directly (partial observability). It can only compute delta_goal through its model M_t. If M_t is wrong, the agent's estimate of the goal-reality gap is wrong.

This means:
- High ||delta_epistemic|| *degrades* the quality of delta_goal estimation
- Closing delta_epistemic (improving M_t) indirectly improves goal-pursuit by giving the agent a more accurate picture of how far it is from G_t
- An agent with perfect G_t and perfect actions but poor M_t will flail — it doesn't know where it is relative to where it wants to be

**This formally justifies the "comprehend before you act" principle** (TST's T-05, TFT's deliberation threshold): reducing delta_epistemic first improves the accuracy of delta_goal estimation, which makes subsequent goal-pursuing actions more effective.

### 2.3 Feasibility Mismatch

*[Definition (feasibility-mismatch) — speculative]*

    delta_feasibility: a signal that delta_goal persists despite adequate M_t and competent action

This is not a simple difference — it's a *diagnosis*. The agent observes that:
1. M_t is adequate (delta_epistemic is low, model checks out)
2. Actions are competent (the agent is executing well)
3. But delta_goal isn't closing (or is closing too slowly)

The inference: the goal itself may be the problem. Either unrealizable, suboptimal, or at the wrong granularity.

This is more like TF-10's structural inadequacy signal than TF-05's prediction error. It's a second-order inference, not a direct observation.

**Formalization attempt:**

    delta_feasibility = ||delta_goal(t)|| - ||delta_goal(t - Delta_t)||
                        + integral[T_goal * ||delta_goal||]dt

If the expected goal-progress (from the agent's tempo and actions) isn't manifesting as actual goal-progress, something is wrong. The accumulated deficit between expected and actual goal-closure is the feasibility signal.

[Speculative] This needs work. The right formalization might be more like a likelihood ratio test: "given my model, my actions, and the observed lack of progress, how likely is it that G_t is achievable?"

---

## 3. Goal Update Dynamics

### 3.1 The Goal Update Rule

*[Formulation — mirroring TF-06]*

    G_t = G_{t-1} + eta_G * g_G(delta_intent)

where:
- eta_G is the **goal update gain**
- g_G is the intent-mismatch transform
- delta_intent = new_intent_signal - hat{g}_t (the difference between new intent information and the agent's current goal prediction)

### 3.2 The Goal Gain

*[Hypothesis — mirroring TF-06's uncertainty ratio]*

    eta_G* = U_G / (U_G + U_source)

where:
- U_G = goal uncertainty (how confident the agent is in its current goal)
- U_source = reliability of the intent source (clear spec vs. vague conversation; trusted commander vs. unclear directive)

**Behavior:**

- **New project, vague spec (high U_G)**: eta_G ≈ 1. The agent absorbs every bit of specification eagerly. Each stakeholder conversation shifts the goal substantially. The agent is searching for its port.

- **Well-specified project, clear spec (low U_G)**: eta_G << 1. The agent has a firm goal. New input from stakeholders is discounted — "that's a nice idea but we already know what we're building." The experienced developer who pushes back on scope creep.

- **After a pivot / strategic reframe (U_G reset)**: eta_G spikes back up.
  The startup that discovers its market hypothesis was wrong must become receptive again. The commander who learns the enemy has moved must re-evaluate the operational objective.

- **Unreliable source (high U_source)**: eta_G is low regardless of U_G.
  The agent doesn't shift its goal based on noisy or untrustworthy intent signals. The developer who doesn't change the spec based on a single offhand comment from a junior stakeholder.

### 3.3 Goal Revision (Structural Goal Change)

Analogous to TF-10's Proposition 10.1 (structural adaptation necessity):

*[Hypothesis (goal-revision-trigger)]*

When the agent's **goal class fitness** F_G is low — i.e., no achievable variant of the current goal specification can be realized — incremental goal adjustment (parametric update via eta_G) is insufficient. The goal must be structurally revised.

**Symptoms of goal class inadequacy (mirroring TF-10):**

| TFT symptom (model class) | AAD symptom (goal class) |
|---------------------------|--------------------------|
| Persistent irreducible mismatch | Persistent delta_goal despite adequate model and competent action |
| Gain collapse without performance | Agent "knows what it wants" but can't make progress |
| Systematic mismatch patterns | Same types of actions always fail to close the same aspects of the goal |

**Goal revision is Boyd's Orient applied to intent.** The agent doesn't just update its model of reality (TFT's Orient); it reframes what it's trying to achieve. This is the Orient → Orient self-loop — the most important arrow in Boyd's diagram, and the one TFT couldn't capture.

---

## 4. Action Selection with Dual Mismatch

### 4.1 The Extended Policy Objective

*[Formulation — extending TF-08]*

    pi*(M_t, G_t) = argmax_a [
        E[goal_progress(a) | M_t, G_t]        -- exploitation: close delta_goal
      + lambda_e(M_t) * CIY(a; M_t)            -- epistemic exploration: improve M_t + lambda_f(M_t, G_t) * FIY(a; M_t, G_t)  -- feasibility exploration: test G_t
    ]

where:
- goal_progress(a) replaces TF-08's generic "value(a)" — now the value is explicitly tied to delta_goal closure
- CIY(a; M_t) is TF-08's causal information yield — unchanged
- FIY(a; M_t, G_t) is **feasibility information yield** — how much action a reveals about whether G_t is achievable

**The three lambda coefficients:**

- lambda_e high when: U_M is high (model uncertain), agent is in early comprehension phase, recent observations have been surprising
- lambda_f high when: delta_goal is persistent despite adequate model, the agent suspects the goal might be wrong, the environment is revealing unexpected constraints
- Both lambda low when: the agent has a good model, a feasible goal, and should just execute

### 4.2 The Cold-Start Sequence

For an AI agent with 100% context turnover, the natural sequence is:

1. **Phase 0 — Goal absorption**: Read the task description, CLAUDE.md, intent documentation. Build G_t. (U_G starts high, drops as intent is absorbed.) This happens fast — G_t has low dimensionality compared to M_t.

2. **Phase 1 — Reality comprehension**: Read code, explore the codebase, build M_t. (U_M starts high, drops as observations accumulate.) lambda_e is dominant. The agent uses G_t to *guide* exploration — read the parts of the codebase relevant to the goal first (goal-directed exploration, high CIY relative to G_t).

3. **Phase 2 — Goal feasibility check**: Now that M_t is adequate, evaluate delta_goal = G_t - M_t. Is the goal feasible? Does the spec make sense given what the code actually is? lambda_f rises if there are concerns.

4. **Phase 3 — Execution**: Close delta_goal through environment-modifying actions (write code). lambda_e and lambda_f are low; exploitation dominates.

5. **Phase 4 — Verification**: Check that delta_goal has actually closed (run tests, verify spec compliance). This is a return to high lambda_e — the agent is updating M_t to confirm that Omega has moved toward G_t.

This sequence is exactly what skilled developers do. TST's T-05 ("bias toward comprehension") is the prescription for Phase 1. The goal-feasibility check (Phase 2) is what great developers do that mediocre ones skip.

---

## 5. The Separation Principle for AAD

### 5.1 When Separation Holds

M_t and G_t dynamics can be designed independently when:

1. **Observation independence**: The observation function h doesn't depend on G_t. Knowing the goal doesn't change what you observe about reality. *Usually true.* The compiler output is the same regardless of what feature you're building.

2. **Model update independence**: M_t update doesn't depend on G_t. Learning about reality doesn't require knowing what you want. *Usually true.* The Kalman filter estimates state regardless of the controller's setpoint.

3. **Goal update independence**: G_t update doesn't depend on M_t. Knowing what you want doesn't require knowing reality. *USUALLY FALSE.* Goal revision depends on feasibility, which depends on M_t. You need to know reality to know if your goal is achievable.

### 5.2 Directed Separation

The separation is *asymmetric*:

- **M_t can be designed first, independently.** TFT's entire machinery (mismatch, gain, tempo, persistence) applies to M_t without knowing G_t. This is why TFT is a valid and complete theory of the epistemic layer.

- **G_t dynamics depend on M_t.** Goal revision requires knowing what's feasible, which requires a model of reality. The goal layer sits *on top of* the epistemic layer.

- **But action selection couples them.** The agent's choice of action depends on BOTH M_t and G_t (the extended policy objective in §4). And actions affect future observations (TF-01's action-dependent h). So G_t influences what the agent does, which influences what it observes, which influences M_t. The coupling is indirect but real.

### 5.3 Implications

- TFT (Part I of AAD) is a *complete, self-contained* theory of the M_t dynamics. It doesn't need G_t to be internally valid. This is the separation principle working in our favor.

- The goal/intent layer (Part II of AAD) REQUIRES M_t. It cannot stand alone. This is the correct dependency direction — you need to understand reality before you can meaningfully pursue or revise goals.

- The full AAD (Part I + Part II) captures the coupled dynamics where goals influence actions influence observations influence models influence goal revision. This is the full Orient cycle.

---

## 6. Goal Tempo and Goal Persistence

### 6.1 Goal Tempo

*[Definition (goal-tempo) — speculative]*

    T_goal = sum_k nu_action^(k) * effectiveness^(k)

where:
- nu_action^(k) is the rate of environment-modifying actions on channel k
- effectiveness^(k) is the marginal reduction in ||delta_goal|| per action on channel k

T_goal is the rate at which the agent closes the goal-reality gap. It depends on both the agent's action capacity and the environment's responsiveness.

**Contrast with epistemic tempo T:**

| | Epistemic tempo T | Goal tempo T_goal |
|---|---|---|
| Measures | Rate of delta_epistemic reduction | Rate of delta_goal reduction |
| Driven by | Observations and model updates | Actions and their effects |
| Improved by | Better channels, better gain | Better tools, better action design |
| Limited by | Observation noise (U_o) | Environmental resistance, action capacity |

### 6.2 Goal Persistence Condition

*[Hypothesis — mirroring TF-11]*

    T_goal > rho_goal / ||delta_goal_critical||

where:
- rho_goal is the rate at which new goal-reality gap is introduced (requirements churn, enemy repositioning, market shifts, other agents' actions modifying shared environment)
- delta_goal_critical is the maximum tolerable distance from the goal

Below this threshold, the agent falls further behind — reality moves away from the goal faster than the agent can close the gap.

**The two persistence conditions:**

An agent needs BOTH:
1. T > rho_epistemic  (epistemic persistence — can track reality)
2. T_goal > rho_goal  (goal persistence — can close the goal-reality gap)

Failure of (1) means the agent loses its model of reality.
Failure of (2) means the agent can't achieve its goals.
Failure of both is catastrophic — the agent is both lost and ineffective.

Survival (TFT's implicit goal) requires only (1). Purposeful agency requires both.

---

## 7. Shared Intent

### 7.1 Intent Communication

*[Formulation — extending Appendix F]*

When agent j communicates intent to agent i:

    G_i_new = G_i_old + eta_intent_ji * g(G_j_communicated - G_i_old)

where:

    eta_intent_ji = U_G_i / (U_G_i + U_channel + U_authority + U_alignment)

- U_G_i: agent i's current goal uncertainty
- U_channel: noise in the communication (vague words vs. precise spec)
- U_authority: how much authority j has over i's goals (commander vs. peer)
- U_alignment: how aligned j's interests are with i's (trusted superior vs.
  potential adversary)

This mirrors Appendix F's communication gain but for intent rather than knowledge.

### 7.2 The Compression Principle for Shared Intent

*[Hypothesis — extending TF-03's IB to goals]*

    G_shared* = argmin_G [ I(G; Commander's_full_plan) -
                           beta_G * I(G; subordinate's_optimal_action | local_conditions) ]

Over-compressed intent (vague): Low first term, but low second term too — the subordinate doesn't know enough to act well.

Under-compressed intent (detailed orders): High second term in benign conditions, but FRAGILE — the subordinate can't adapt when conditions differ from what the commander expected.

Optimally compressed intent (Auftragstaktik sweet spot): Retains exactly what the subordinate needs to evaluate "does this action serve the intent?" without retaining specifics that would prevent adaptation to unforeseen conditions.

---

## 8. Domain Instantiation Table

| Component | PID | Kalman+LQR | Software Dev | Military | RL |
|-----------|-----|------------|-------------|----------|----|
| M_t | (none — PID has no reality model) | x_hat_t | Developer's codebase model | Situational awareness | Q(s,a) or world model |
| G_t | Setpoint r_t | Reference x_ref | Feature spec | Commander's intent | Reward function (implicit) |
| delta_epistemic | (none) | y_t - H*x_hat_t | "I misunderstood the code" | Intel contradicts assessment | TD error (model-learning component) |
| delta_goal | r_t - y_t | x_ref - x_hat_t | "Code doesn't match spec" | Objective not yet achieved | TD error (goal-pursuit component) |
| delta_feasibility | (n/a — setpoint assumed achievable) | (n/a — dynamics assumed known) | "Spec unrealizable given architecture" | "Objective impossible given terrain" | Reward is unachievable |
| eta_G update | Setpoint changes externally | Reference changes externally | Spec revision via stakeholder negotiation | Order revision from higher command | Reward shaping revision |
| T_goal | Closed-loop bandwidth | Control bandwidth | Features-shipped-per-sprint | Operational tempo toward objective | Episodes-to-convergence |
| Separation | Perfect (no M_t) | Perfect (separation principle) | Partial (comprehension informs feasibility) | Imperfect (intel shapes objectives) | Partial (model-based RL couples them) |

**The PID column is revealing**: PID has G_t (setpoint) and delta_goal (e_t = r_t - y_t) but NO M_t and NO delta_epistemic. It's pure goal-pursuit without epistemic modeling. TFT tried to fit this into the model framework and the fit was awkward. AAD gives it a proper home — the PID is a goal-persistence-only agent, the degenerate case where Part I (adaptive model) is absent and only Part II (purposeful agency) operates.

**The Kalman filter column is the opposite**: pure M_t, no G_t. It's an epistemic-only agent. TFT describes it perfectly. AAD's Part I covers it completely; Part II doesn't apply.

**LQG (Kalman + LQR together)** is the simplest case where BOTH parts operate. The separation principle tells us they can be designed independently in this case. AAD's claim is that this separation is the exception, not the rule — in complex domains (software, military, organizational), the M_t and G_t dynamics are coupled through action selection and goal revision.

---

## 9. G_t as Strategy Network, Not Point (Major Revision)

The initial sketch (§1-8) treats G_t as a point in state space — "the agent wants reality to be *here*." This is wrong, or at best a degenerate case (the PID setpoint). Real G_t is richer:

### 9.1 The Causal Intent DAG

G_t is not a point but a **structured network of expected causal chains from actions to sub-goals to objectives**, with observability constraints and contingency branches. In OKR terms:

    Objective: "Users can authenticate via OAuth" ├── KR1: "OAuth flow returns valid token" │   ├── Expected action path: implement token endpoint │   ├── Observable confirmation: test_oauth_token_flow passes │   └── Contingency: if upstream API is unavailable, mock + adapter pattern ├── KR2: "Session persists across requests" │   ├── Expected action path A: session middleware │   ├── Expected action path B (hedge): cookie-based fallback │   └── Observable confirmation: test_session_persistence passes └── KR3: "Existing auth still works"
        └── Observable confirmation: existing auth suite still green

This is a **causal DAG of intent**:
- Nodes are objectives (high-level G), key results (sub-goals), actions (expected causal interventions), and observables (how I'll know it worked)
- Edges are expected causal links (action → sub-goal → objective)
- Branches are contingencies (if path A fails, path B)
- Leaves are observations that confirm or deny progress

The "strategy" IS this DAG. It encodes the agent's theory of how its actions will produce goal-achievement, including what it expects to observe along the way and what it will do if expectations are violated.

### 9.2 delta_goal Observability

The "tree in the forest" problem: the agent acts toward G_t but may not know whether δ_goal has closed until a confirming observation arrives. Between action and confirmation, δ_goal is **unobservable** — the agent has a prediction about goal-state, filtered through M_t.

This means:
- Each node in the intent DAG has an *observability profile*: how and when the agent can confirm that this sub-goal was reached
- Some sub-goals are immediately observable (compiler output: did it compile?)
- Others are delayed (user behavior: do users actually use the OAuth flow?)
- Some are only statistically observable (performance: is it fast enough under load? requires sampling)

The agent's confidence in δ_goal at any moment depends on which confirmation observations have arrived. The unconfirmed portions of the DAG are in a Schrödinger-like state — the agent must plan as if they might or might not have succeeded.

### 9.3 Parallel Execution as Portfolio Optimization

When the agent is uncertain which action path in the DAG will succeed, the rational response is parallel execution — launching multiple paths simultaneously. This is already visible in practice: Claude Code sends parallel searches with different assumptions because the expected cost of redundancy is less than the expected cost of serial failure-then-retry.

Formally: for a set of candidate action paths {A_1, ..., A_n} toward sub-goal KR_k, with estimated probabilities of success {p_1, ..., p_n} and costs {c_1, ..., c_n}, the agent should pursue the portfolio that minimizes expected total cost:

    min E[cost] = min sum_i (c_i * x_i) + penalty(none_succeed | {x_i})

where x_i in {0,1} indicates whether path i is pursued. When the success probabilities are uncertain (which they always are — the agent doesn't know p_i exactly), this becomes a robust optimization problem. Hedging arises naturally.

### 9.4 Strategic Adaptation Beyond TF-10's "Panic"

TF-10's structural adaptation is: "the model class is wrong, destroy and recreate." This maps to: the entire strategy has failed catastrophically, start over. That's the nuclear option — biological "panic."

Real strategic adaptation operates on the intent DAG with much finer granularity:

| Operation | What changes | Trigger |
|-----------|-------------|---------|
| **Pruning** | Remove a failed branch | Confirming observation shows this path doesn't work |
| **Grafting** | Add a new branch | Discovery of a new possible action path |
| **Reweighting** | Shift resources between branches | Updated probability estimates after partial observations |
| **Parallel hedging** | Pursue multiple branches simultaneously | High uncertainty about which will succeed |
| **Objective revision** | Change a high-level node | Feasibility discovery or opportunity (directed opportunism) |
| **Structural collapse** | Replace the entire DAG | Catastrophic failure or paradigm shift (TF-10's nuclear option) |

The first five are *continuous strategic maintenance*. Only the last one is TF-10's structural adaptation. A good strategist (or a good AI agent) spends most of their time on the first five and rarely reaches the last one.

**Crucially**: even "structural" changes to the DAG don't require a discrete panic event. Because the edges are *probabilistic* — each causal link (action → sub-goal) has a confidence range — the DAG restructures *continuously* as confidence ranges update. When an edge's confidence drops below some threshold, the branch it supports becomes untenable and naturally gets pruned or replaced. When a new observation raises confidence on an alternative edge, resources flow toward it. The DAG is a living structure whose topology shifts as the agent's probabilistic causal beliefs update.

This dissolves the sharp line between "parametric update" (adjusting edge weights) and "structural change" (adding/removing edges). In the probabilistic DAG, a structural change IS an extreme parametric update — an edge weight dropping to near-zero or rising from near-zero. TF-10's Proposition 10.1 (structural adaptation necessity) might be better understood as: "when no reweighting of existing edges can produce an adequate strategy, new edges (new causal hypotheses) must be introduced." The "destruction-creation cycle" becomes continuous DAG evolution rather than discrete model-class switching.

### 9.5 The Strategy DAG and the Causal DAG of Reality

Two DAGs coexist in the agent's state:
- **M_t's causal DAG**: the agent's model of how reality works (what causes what in the environment)
- **G_t's intent DAG**: the agent's strategy for how to change reality toward the goal (what actions cause what sub-goals)

They interact: the intent DAG's edges (expected causal links from actions to outcomes) are hypotheses about M_t's causal DAG. When M_t reveals that an expected causal link doesn't hold (the action doesn't produce the expected sub-goal), the intent DAG must be revised.

In software: the developer's strategy ("add middleware to handle sessions") is a hypothesis about the codebase's causal structure ("this insertion point in the request pipeline will give middleware access to the request context"). When M_t reveals the hypothesis is wrong ("the pipeline doesn't work that way"), the strategy must be revised — not because the goal changed, but because the expected causal path to the goal was wrong.

This gives a precise meaning to "Orient" in the full Boydian sense: Orient is where M_t (reality model) meets G_t (intent DAG), and the interaction produces either *confirmation* (the strategy's causal hypotheses hold) or *revision* (they don't, and the strategy must adapt). The Orient → Orient self-loop is the continuous maintenance of the intent DAG in light of ongoing reality updates.

### 9.6 Implications for the Formalism

This revision suggests G_t shouldn't be formalized as a point in state space S but as a **weighted DAG** with:
- Nodes: objectives, sub-goals, actions, observables
- Edges: expected causal links (weighted by estimated probability)
- Contingency structure: alternative paths branching from uncertainty nodes

The "goal-reality mismatch" δ_goal is then not a single vector but a **mismatch profile across the DAG**: which nodes have been confirmed achieved, which are pending, which have failed.

The "goal update" is DAG maintenance: pruning, grafting, reweighting, and occasionally structural revision.

The "goal tempo" becomes something like: the rate at which the DAG's pending nodes are being resolved (either confirmed or failed), weighted by their importance to the objective.

This is richer than the point-in-S formalism but may be too rich for a first formal treatment. A pragmatic approach: develop the point-in-S case first (it handles PID, LQG, and simple goal-pursuit), noting that it's the degenerate case of the DAG formalism. Then develop the DAG formalism for domains where strategy matters (software, military, organizational).

---

## 10. What I'm Unsure About (revised)

### 10.1 What is the right level of formalism for the intent DAG?

The OKR/DAG structure feels right descriptively. But formalizing it risks over-engineering — do we need full DAG machinery, or is the point-in-S formalism with "structural revision when the point needs to change" sufficient for the core theory? Maybe the DAG is a domain-specific elaboration (useful for software, military) rather than a core theoretical construct.

### 10.2 Is delta_feasibility a separate signal or a DAG property?

### (Former §9.1-9.4 — superseded by §9 rewrite above. The uncertainty
### questions about feasibility, continuous-vs-discrete, goal tempo, and the
### M_t/G_t parallel depth are largely resolved by the DAG reframing:
### feasibility is a DAG property, updates are DAG maintenance operations
### which can be continuous or discrete, goal tempo is DAG resolution rate,
### and the M_t/G_t parallel holds for simple cases but the full picture is
### richer — two interacting DAGs.)

---

## 10. What Comes Next

Three paths forward from this sketch, in order of likely value:

1. **Test against PID + LQG formally.** These are cases where the answer is known. If AAD's formalism reproduces the PID error dynamics and the LQG separation principle as special cases, the formalism is on solid ground. If it doesn't, the formalism needs fixing before we go further.

2. **Test against a software development scenario.** Walk through a concrete feature implementation using AAD's framework: G_t = the spec, M_t = the codebase model, delta_goal = spec-reality gap, the cold-start sequence, goal revision when the spec turns out to be infeasible. See if the formalism produces non-obvious predictions.

3. **Formalize the goal dynamics ODE.** Write down the differential equation for delta_goal evolution, analogous to TF-11's mismatch ODE. Analyze stability. Derive a goal persistence condition. See if the adversarial dynamics (Cor. 11.2, effects spiral) have goal-level analogs.
