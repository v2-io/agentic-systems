# The G_t Formalism: First Sketch

**Status**: First attempt at the mathematics. This is thinking-on-paper, not
a finished formulation. Expect errors, dead ends, and revision. The goal is
to get enough structure on the page that we can see what works and what doesn't.

**Approach**: Mirror TFT's structure wherever the parallel holds, then identify
where it breaks and new machinery is needed.

---

## 1. Definitions

### 1.1 The Goal Model

*[Definition (goal-model)]*

    G_t = psi(I_t)

where:
- G_t is the agent's current goal — a compressed representation of the
  desired future state, drawn from model space S
- psi is the goal-compression function
- I_t is the **intent history** — the stream of goal-relevant inputs the
  agent has received

G_t and M_t live in the same state space S. The Kalman estimate x_hat_t and
the LQR reference x_ref are both in R^n. The developer's mental model of
the codebase and the feature spec both describe "a codebase state."

### 1.2 Intent History

*[Definition (intent-history)]*

    I_t = (g_1, r_1, g_2, r_2, ..., g_t)

where:
- g_i are **intent signals**: specifications, commands, discovered
  opportunities, feasibility discoveries, higher-level goal decompositions
- r_i are **revision signals**: feedback about whether the current goal is
  being achieved, is feasible, or should change

I_t is to G_t what C_t (interaction history) is to M_t. Note that I_t is NOT
a subset of C_t — intent signals come from different sources than observations.
A specification arrives from a stakeholder, not from the environment. A
commander's intent arrives from above, not from the battlefield.

However, some intent signals ARE triggered by observations — the discovery
that a goal is infeasible comes from observing reality. So I_t and C_t are
coupled but distinct streams.

### 1.3 Goal Uncertainty

*[Definition (goal-uncertainty)]*

    U_G = Var_G[desired_outcome]

The agent's uncertainty about what it actually wants. Sources:

- **Specification ambiguity**: "make it fast" — how fast?
- **Incomplete decomposition**: the high-level goal is clear but the sub-goals
  haven't been worked out
- **Competing objectives**: speed vs. quality vs. cost — the tradeoff isn't
  resolved
- **Evolving preferences**: the stakeholder doesn't know what they want yet
- **Conditional goals**: "if X is feasible, do X; otherwise do Y" — the goal
  is a function of yet-to-be-discovered reality

U_G is NOT the same as the distance from the goal (that's ||delta_goal||).
U_G is uncertainty about the goal *itself* — the agent is unsure of its
destination, not just far from it.

**Domain instantiations of U_G:**

| Domain | Low U_G | High U_G |
|--------|---------|----------|
| PID | Precise setpoint (r_t = 72°F) | Variable setpoint (track time-varying reference) |
| Software | Clear, unambiguous spec | Vague user story, "improve performance" |
| Military | Specific objective (take the bridge) | Strategic intent (disrupt enemy logistics) |
| RL | Well-defined reward function | Reward shaping still being tuned |
| Startup | Clear product-market fit | Searching for product-market fit |

The Auftragstaktik insight: the *optimal* U_G is not zero. Over-specified
goals (U_G ≈ 0) prevent directed opportunism. The agent needs enough goal
uncertainty to recognize and exploit opportunities the goal-setter couldn't
foresee.

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

Critical subtlety: the agent can't observe delta_goal_true = G_t - Omega_t
directly (partial observability). It can only compute delta_goal through
its model M_t. If M_t is wrong, the agent's estimate of the goal-reality gap
is wrong.

This means:
- High ||delta_epistemic|| *degrades* the quality of delta_goal estimation
- Closing delta_epistemic (improving M_t) indirectly improves goal-pursuit
  by giving the agent a more accurate picture of how far it is from G_t
- An agent with perfect G_t and perfect actions but poor M_t will flail — it
  doesn't know where it is relative to where it wants to be

**This formally justifies the "comprehend before you act" principle** (TST's
T-05, TFT's deliberation threshold): reducing delta_epistemic first improves
the accuracy of delta_goal estimation, which makes subsequent goal-pursuing
actions more effective.

### 2.3 Feasibility Mismatch

*[Definition (feasibility-mismatch) — speculative]*

    delta_feasibility: a signal that delta_goal persists despite adequate M_t
    and competent action

This is not a simple difference — it's a *diagnosis*. The agent observes that:
1. M_t is adequate (delta_epistemic is low, model checks out)
2. Actions are competent (the agent is executing well)
3. But delta_goal isn't closing (or is closing too slowly)

The inference: the goal itself may be the problem. Either unrealizable,
suboptimal, or at the wrong granularity.

This is more like TF-10's structural inadequacy signal than TF-05's prediction
error. It's a second-order inference, not a direct observation.

**Formalization attempt:**

    delta_feasibility = ||delta_goal(t)|| - ||delta_goal(t - Delta_t)||
                        + integral[T_goal * ||delta_goal||]dt

If the expected goal-progress (from the agent's tempo and actions) isn't
manifesting as actual goal-progress, something is wrong. The accumulated
deficit between expected and actual goal-closure is the feasibility signal.

[Speculative] This needs work. The right formalization might be more like a
likelihood ratio test: "given my model, my actions, and the observed lack of
progress, how likely is it that G_t is achievable?"

---

## 3. Goal Update Dynamics

### 3.1 The Goal Update Rule

*[Formulation — mirroring TF-06]*

    G_t = G_{t-1} + eta_G * g_G(delta_intent)

where:
- eta_G is the **goal update gain**
- g_G is the intent-mismatch transform
- delta_intent = new_intent_signal - hat{g}_t (the difference between
  new intent information and the agent's current goal prediction)

### 3.2 The Goal Gain

*[Hypothesis — mirroring TF-06's uncertainty ratio]*

    eta_G* = U_G / (U_G + U_source)

where:
- U_G = goal uncertainty (how confident the agent is in its current goal)
- U_source = reliability of the intent source (clear spec vs. vague
  conversation; trusted commander vs. unclear directive)

**Behavior:**

- **New project, vague spec (high U_G)**: eta_G ≈ 1. The agent absorbs every
  bit of specification eagerly. Each stakeholder conversation shifts the
  goal substantially. The agent is searching for its port.

- **Well-specified project, clear spec (low U_G)**: eta_G << 1. The agent
  has a firm goal. New input from stakeholders is discounted — "that's a
  nice idea but we already know what we're building." The experienced
  developer who pushes back on scope creep.

- **After a pivot / strategic reframe (U_G reset)**: eta_G spikes back up.
  The startup that discovers its market hypothesis was wrong must become
  receptive again. The commander who learns the enemy has moved must
  re-evaluate the operational objective.

- **Unreliable source (high U_source)**: eta_G is low regardless of U_G.
  The agent doesn't shift its goal based on noisy or untrustworthy intent
  signals. The developer who doesn't change the spec based on a single
  offhand comment from a junior stakeholder.

### 3.3 Goal Revision (Structural Goal Change)

Analogous to TF-10's Proposition 10.1 (structural adaptation necessity):

*[Hypothesis (goal-revision-trigger)]*

When the agent's **goal class fitness** F_G is low — i.e., no achievable
variant of the current goal specification can be realized — incremental goal
adjustment (parametric update via eta_G) is insufficient. The goal must be
structurally revised.

**Symptoms of goal class inadequacy (mirroring TF-10):**

| TFT symptom (model class) | ACT symptom (goal class) |
|---------------------------|--------------------------|
| Persistent irreducible mismatch | Persistent delta_goal despite adequate model and competent action |
| Gain collapse without performance | Agent "knows what it wants" but can't make progress |
| Systematic mismatch patterns | Same types of actions always fail to close the same aspects of the goal |

**Goal revision is Boyd's Orient applied to intent.** The agent doesn't just
update its model of reality (TFT's Orient); it reframes what it's trying to
achieve. This is the Orient → Orient self-loop — the most important arrow in
Boyd's diagram, and the one TFT couldn't capture.

---

## 4. Action Selection with Dual Mismatch

### 4.1 The Extended Policy Objective

*[Formulation — extending TF-08]*

    pi*(M_t, G_t) = argmax_a [
        E[goal_progress(a) | M_t, G_t]        -- exploitation: close delta_goal
      + lambda_e(M_t) * CIY(a; M_t)            -- epistemic exploration: improve M_t
      + lambda_f(M_t, G_t) * FIY(a; M_t, G_t)  -- feasibility exploration: test G_t
    ]

where:
- goal_progress(a) replaces TF-08's generic "value(a)" — now the value is
  explicitly tied to delta_goal closure
- CIY(a; M_t) is TF-08's causal information yield — unchanged
- FIY(a; M_t, G_t) is **feasibility information yield** — how much action a
  reveals about whether G_t is achievable

**The three lambda coefficients:**

- lambda_e high when: U_M is high (model uncertain), agent is in early
  comprehension phase, recent observations have been surprising
- lambda_f high when: delta_goal is persistent despite adequate model,
  the agent suspects the goal might be wrong, the environment is revealing
  unexpected constraints
- Both lambda low when: the agent has a good model, a feasible goal, and
  should just execute

### 4.2 The Cold-Start Sequence

For an AI agent with 100% context turnover, the natural sequence is:

1. **Phase 0 — Goal absorption**: Read the task description, CLAUDE.md,
   intent documentation. Build G_t. (U_G starts high, drops as intent is
   absorbed.) This happens fast — G_t has low dimensionality compared to M_t.

2. **Phase 1 — Reality comprehension**: Read code, explore the codebase,
   build M_t. (U_M starts high, drops as observations accumulate.) lambda_e
   is dominant. The agent uses G_t to *guide* exploration — read the parts
   of the codebase relevant to the goal first (goal-directed exploration,
   high CIY relative to G_t).

3. **Phase 2 — Goal feasibility check**: Now that M_t is adequate, evaluate
   delta_goal = G_t - M_t. Is the goal feasible? Does the spec make sense
   given what the code actually is? lambda_f rises if there are concerns.

4. **Phase 3 — Execution**: Close delta_goal through environment-modifying
   actions (write code). lambda_e and lambda_f are low; exploitation
   dominates.

5. **Phase 4 — Verification**: Check that delta_goal has actually closed
   (run tests, verify spec compliance). This is a return to high lambda_e
   — the agent is updating M_t to confirm that Omega has moved toward G_t.

This sequence is exactly what skilled developers do. TST's T-05 ("bias toward
comprehension") is the prescription for Phase 1. The goal-feasibility check
(Phase 2) is what great developers do that mediocre ones skip.

---

## 5. The Separation Principle for ACT

### 5.1 When Separation Holds

M_t and G_t dynamics can be designed independently when:

1. **Observation independence**: The observation function h doesn't depend on
   G_t. Knowing the goal doesn't change what you observe about reality.
   *Usually true.* The compiler output is the same regardless of what feature
   you're building.

2. **Model update independence**: M_t update doesn't depend on G_t. Learning
   about reality doesn't require knowing what you want.
   *Usually true.* The Kalman filter estimates state regardless of the
   controller's setpoint.

3. **Goal update independence**: G_t update doesn't depend on M_t. Knowing
   what you want doesn't require knowing reality.
   *USUALLY FALSE.* Goal revision depends on feasibility, which depends on
   M_t. You need to know reality to know if your goal is achievable.

### 5.2 Directed Separation

The separation is *asymmetric*:

- **M_t can be designed first, independently.** TFT's entire machinery
  (mismatch, gain, tempo, persistence) applies to M_t without knowing G_t.
  This is why TFT is a valid and complete theory of the epistemic layer.

- **G_t dynamics depend on M_t.** Goal revision requires knowing what's
  feasible, which requires a model of reality. The goal layer sits *on top of*
  the epistemic layer.

- **But action selection couples them.** The agent's choice of action depends
  on BOTH M_t and G_t (the extended policy objective in §4). And actions
  affect future observations (TF-01's action-dependent h). So G_t influences
  what the agent does, which influences what it observes, which influences
  M_t. The coupling is indirect but real.

### 5.3 Implications

- TFT (Part I of ACT) is a *complete, self-contained* theory of the M_t
  dynamics. It doesn't need G_t to be internally valid. This is the
  separation principle working in our favor.

- The goal/intent layer (Part II of ACT) REQUIRES M_t. It cannot stand
  alone. This is the correct dependency direction — you need to understand
  reality before you can meaningfully pursue or revise goals.

- The full ACT (Part I + Part II) captures the coupled dynamics where
  goals influence actions influence observations influence models influence
  goal revision. This is the full Orient cycle.

---

## 6. Goal Tempo and Goal Persistence

### 6.1 Goal Tempo

*[Definition (goal-tempo) — speculative]*

    T_goal = sum_k nu_action^(k) * effectiveness^(k)

where:
- nu_action^(k) is the rate of environment-modifying actions on channel k
- effectiveness^(k) is the marginal reduction in ||delta_goal|| per action
  on channel k

T_goal is the rate at which the agent closes the goal-reality gap. It depends
on both the agent's action capacity and the environment's responsiveness.

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
- rho_goal is the rate at which new goal-reality gap is introduced
  (requirements churn, enemy repositioning, market shifts, other agents'
  actions modifying shared environment)
- delta_goal_critical is the maximum tolerable distance from the goal

Below this threshold, the agent falls further behind — reality moves away
from the goal faster than the agent can close the gap.

**The two persistence conditions:**

An agent needs BOTH:
1. T > rho_epistemic  (epistemic persistence — can track reality)
2. T_goal > rho_goal  (goal persistence — can close the goal-reality gap)

Failure of (1) means the agent loses its model of reality.
Failure of (2) means the agent can't achieve its goals.
Failure of both is catastrophic — the agent is both lost and ineffective.

Survival (TFT's implicit goal) requires only (1). Purposeful agency requires
both.

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

This mirrors Appendix F's communication gain but for intent rather than
knowledge.

### 7.2 The Compression Principle for Shared Intent

*[Hypothesis — extending TF-03's IB to goals]*

    G_shared* = argmin_G [ I(G; Commander's_full_plan) -
                           beta_G * I(G; subordinate's_optimal_action | local_conditions) ]

Over-compressed intent (vague): Low first term, but low second term too —
the subordinate doesn't know enough to act well.

Under-compressed intent (detailed orders): High second term in benign
conditions, but FRAGILE — the subordinate can't adapt when conditions differ
from what the commander expected.

Optimally compressed intent (Auftragstaktik sweet spot): Retains exactly what
the subordinate needs to evaluate "does this action serve the intent?" without
retaining specifics that would prevent adaptation to unforeseen conditions.

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

**The PID column is revealing**: PID has G_t (setpoint) and delta_goal
(e_t = r_t - y_t) but NO M_t and NO delta_epistemic. It's pure goal-pursuit
without epistemic modeling. TFT tried to fit this into the model framework
and the fit was awkward. ACT gives it a proper home — the PID is a
goal-persistence-only agent, the degenerate case where Part I (adaptive
model) is absent and only Part II (purposeful agency) operates.

**The Kalman filter column is the opposite**: pure M_t, no G_t. It's an
epistemic-only agent. TFT describes it perfectly. ACT's Part I covers it
completely; Part II doesn't apply.

**LQG (Kalman + LQR together)** is the simplest case where BOTH parts
operate. The separation principle tells us they can be designed independently
in this case. ACT's claim is that this separation is the exception, not the
rule — in complex domains (software, military, organizational), the M_t
and G_t dynamics are coupled through action selection and goal revision.

---

## 9. What I'm Unsure About

### 9.1 Is delta_feasibility a real signal or a diagnostic inference?

Delta_epistemic is a direct observation (the prediction was wrong). Delta_goal
is a direct computation (G_t - M_t). But delta_feasibility is an *inference*
— the agent must reason "I have a good model, good actions, but no progress,
therefore the goal might be wrong." This is more like TF-10's structural
inadequacy detection than TF-05's prediction error.

Maybe feasibility isn't a third mismatch signal but a property of the
delta_goal dynamics — when d||delta_goal||/dt stays positive despite adequate
T_goal, something structural is wrong. The diagnosis of whether it's the goal
(revise G_t), the model (improve M_t), or the actions (change strategy) is a
higher-order inference.

### 9.2 Does G_t update continuously or discretely?

M_t updates continuously (every observation shifts the model a little). Does
G_t work the same way? In some domains, goals change smoothly (the PID
setpoint ramps). In others, goals change in discrete jumps (new sprint,
new orders, pivot). Goal revision (structural G_t change) is definitely
discrete. But within a stable goal, there might be continuous refinement
(gradually understanding the spec better, which is really U_G decreasing
rather than G_t changing).

### 9.3 Is "goal tempo" actually well-defined?

Epistemic tempo T has a clean definition: sum of rate × gain across channels.
Goal tempo T_goal as I've defined it (rate × effectiveness of actions) is
fuzzier — "effectiveness" depends on the environment's response to actions,
which is exactly what the agent is uncertain about (that's U_M's job). Maybe
goal tempo is better defined in terms of delta_goal dynamics:

    d||delta_goal||/dt = -T_goal * ||delta_goal|| + rho_goal

...mirroring the mismatch ODE. But delta_goal isn't driven down by the same
mechanism as delta_epistemic. Delta_epistemic goes down through observation
and model update (passive-ish). Delta_goal goes down through action and
environmental modification (active). The dynamics might be fundamentally
different.

### 9.4 How deep is the M_t/G_t mathematical parallel?

The parallel is suggestive but might be superficial. Key differences:
- M_t is built *bottom-up* from observations; G_t is received *top-down*
  from specifications (or generated internally)
- M_t converges toward a fixed target (reality); G_t may not converge at all
  (goals can keep changing)
- M_t update is triggered by *surprise*; G_t update is triggered by
  *infeasibility* or *opportunity* — different trigger mechanisms

The parallel might hold for the update rule (gain × mismatch) but break for
the dynamics (convergence behavior, stability analysis).

---

## 10. What Comes Next

Three paths forward from this sketch, in order of likely value:

1. **Test against PID + LQG formally.** These are cases where the answer is
   known. If ACT's formalism reproduces the PID error dynamics and the LQG
   separation principle as special cases, the formalism is on solid ground.
   If it doesn't, the formalism needs fixing before we go further.

2. **Test against a software development scenario.** Walk through a concrete
   feature implementation using ACT's framework: G_t = the spec, M_t = the
   codebase model, delta_goal = spec-reality gap, the cold-start sequence,
   goal revision when the spec turns out to be infeasible. See if the
   formalism produces non-obvious predictions.

3. **Formalize the goal dynamics ODE.** Write down the differential equation
   for delta_goal evolution, analogous to TF-11's mismatch ODE. Analyze
   stability. Derive a goal persistence condition. See if the adversarial
   dynamics (Cor. 11.2, effects spiral) have goal-level analogs.
