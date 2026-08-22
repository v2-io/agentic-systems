# ACT-03: The Agent's State — Model, Objective, Strategy

*Depends on: ACT-01 (scope), ACT-02 (causal structure)*

An agent within ACT's scope maintains internal state that serves three distinct functions: understanding reality, specifying what it wants, and planning how to get there. These functions correspond to three formal objects that, together, characterize the agent's complete internal state.

## The Three State Objects

### M_t — The Reality Model

*[Formulation]*

The agent's compressed representation of how the world works:

$$M_t = \phi(\mathcal{C}_t)$$

where φ: C* → M maps the interaction history (chronica, ACT-02) to model space M. This is a **formulation choice** — we commit to analyzing the agent as having a complete state M_t that subsumes all retained information from its history.

**Information bottleneck formulation.** The optimal compression balances retained history against predictive power:

*[Formulation (IB-objective)]*
$$\phi^* = \arg\min_{\phi} \left[ I(M_t; \mathcal{C}_t) - \beta \cdot I(M_t; o_{t+1:\infty} \mid a_{t:\infty}) \right]$$

where I(M_t; C_t) is the compression cost (history retained) and I(M_t; o_{t+1:∞} | a_{t:∞}) is the predictive power (future prediction capability). The trade-off parameter β depends on environment volatility ρ (ACT-07): volatile environments favor aggressive compression (lower β); stable environments favor dense retention (higher β).

**Model space examples:**

| Agent | M_t space |
|-------|-----------|
| Kalman filter | State estimate + covariance: R^n × S^n_{++} |
| Bayesian agent | Distribution over parameters: Δ(Θ) |
| RL agent | Value function: {Q: S × A → R} |
| PID controller | R^3 (error, integral, derivative) — degenerate |
| Developer | Mental model of codebase architecture + state |
| Commander | Intelligence picture + force assessment |
| LLM agent | Context window contents + retrieved memory |

The PID controller's "model" is degenerate — it retains only the error signal and its history (integral, derivative), with no predictive capability. This is why the PID inhabits the "blind pursuer" quadrant (ACT-01): it has O_t but not a genuine M_t.

### O_t — The Objective

*[Definition]*

What the agent wants: a target state, region, or condition in environment state space S.

$$O_t \in \mathcal{S} \quad \text{or} \quad O_t \subseteq \mathcal{S}$$

The objective is conceptually simple — it's the port, the destination, the desired end-state. "Temperature at 72°F." "Enemy position secured." "Feature deployed and passing tests." "Revenue above threshold."

**The objective is not the strategy.** O_t specifies *what*, not *how*.
Two agents with identical O_t may have completely different strategies Σ_t.
Two agents with identical Σ_t may be pursuing different O_t (a shared strategy applied to different objectives).

**Compound objectives** (e.g., "revenue > X AND churn < Y AND morale > Z") can be modeled as multiple terminal nodes in the strategy DAG Σ_t, each with its own target condition. The complexity of compound objectives lives in Σ_t, not in O_t.

**Objective examples:**

| Agent | O_t |
|-------|-----|
| PID controller | Setpoint r_t |
| LQG controller | Quadratic cost minimum |
| RL agent | Cumulative reward maximization |
| Developer | Feature specification satisfied |
| Commander | Mission objective achieved |
| Organization | Strategic targets met |

**Agents without O_t** — the Kalman filter, the passive Bayesian learner — have no objective. They track reality without aiming. ACT's adaptive-systems machinery (mismatch, gain, tempo, persistence) fully describes them. The purposeful-agency machinery (O_t, Σ_t, Orient cascade) does not apply.

### Σ_t — The Strategy

*[Definition]*

How the agent plans to get from current reality to O_t: a probabilistic causal DAG encoding the agent's theory of how its actions will produce goal-achievement.

$$\Sigma_t = (V_t, E_t, p_t, \gamma_t, \text{props}_t)$$

where:
- V_t: propositional nodes (things that could be true or false)
- E_t ⊆ V_t × V_t: directed causal edges
- p_t: E_t → [0,1]: causal confidence per edge
- γ_t: V_t → {AND, OR}: combination rule per node
- props_t: per-node properties (see ACT-08 for full treatment)

The strategy DAG encodes the agent's belief about **causal chains from actions to objectives** — "if I do X, then Y becomes more likely, and if Y and Z both hold, then O_t is achieved."

**The strategy is distinct from the reality model.** M_t represents *what is*; Σ_t represents *what I intend to make happen*. A commander's intelligence picture (M_t) is distinct from the operational plan (Σ_t), even though the plan must be grounded in the intelligence picture.

**Agents without Σ_t** — the PID controller has O_t (setpoint) but no strategy DAG. It computes a correction from the error signal without modeling the causal chain from action to outcome. The Kalman filter has neither O_t nor Σ_t. The adaptive tracker with no objective has M_t alone.

The full treatment of strategy structure — AND/OR semantics, edge updates, depth fragility, observability dominance — is in ACT-08. Here we introduce Σ_t as a formal object and establish its relationships to M_t and O_t.

## Directed Separation

*[Derived — from causal structure]*

The three state objects have an asymmetric dependency structure:

1. **M_t dynamics are independent of O_t and Σ_t.** How the agent builds and updates its reality model does not depend on what it wants or how it plans to get there. The Kalman filter's estimation quality is invariant to the control policy (separation principle). More generally: the optimal gain η* (ACT-06) depends on U_M and U_o, not on O_t.

2. **O_t is independent of M_t.** What the agent wants does not depend on what it currently knows about reality. (O_t may be *revised* based on M_t via the feasibility check in the Orient cascade, but its *value* is not derived from M_t.)

3. **Σ_t depends on both M_t and O_t.** Strategy requires knowing both what's feasible (from M_t) and what's desired (from O_t). You cannot plan without understanding the terrain, and you cannot plan without knowing the destination.

4. **Action selection couples all three.** The policy π(M_t, O_t, Σ_t) produces actions that affect the environment, generating observations that update M_t, which may trigger Σ_t revision, which may trigger O_t revision. This is the Orient cascade (ACT-08).

**Implication for theory structure:** The adaptive-systems machinery (mismatch, gain, tempo, persistence) can be developed for M_t alone — this is what TFT did, and it's valid. But the purposeful-agency machinery (O_t, Σ_t, Orient cascade) requires M_t. ACT develops both together, and the directed separation tells us which results depend on what.

## The Recursive Update

From causal structure (ACT-02), the agent's state update must be recursive:

*[Derived (recursive-update)]*
$$M_{\tau^+} = f_M(M_{\tau^-}, e_\tau)$$

Between events, the model evolves autonomously:
$$\frac{dM}{d\tau} = g_M(M_\tau) \quad \text{(between events)}$$

**For the full agent state**, the update extends:

$$M_{\tau^+} = f_M(M_{\tau^-}, e_\tau)$$
$$\Sigma_{\tau^+} = f_\Sigma(\Sigma_{\tau^-}, M_{\tau^+}, e_\tau)$$
$$O_{\tau^+} = f_O(O_{\tau^-}, \Sigma_{\tau^+}, M_{\tau^+})$$

Note the ordering: M_t updates first (from observation), then Σ_t updates (using the new M_t), then O_t may revise (if Σ_t reveals infeasibility). This is the Orient cascade in update-rule form. The timescale separation (ACT-08) ensures these happen at decreasing frequencies:

$$\nu_{M\text{-update}} \gg \nu_{\Sigma\text{-update}} \gg \nu_{O\text{-revision}}$$

## The Agent's Internal State

The complete internal state is the triple:

*[Definition (agent-state)]*
$$(M_t, O_t, \Sigma_t)$$

For degenerate cases:
- **Adaptive tracker**: (M_t, ∅, ∅) — model only
- **Blind pursuer**: (∅, O_t, ∅) — objective only, no model or strategy
- **Simple purposeful**: (M_t, O_t, ∅) — model and objective but no explicit strategy (e.g., LQG where the optimal policy is derived directly from M_t and O_t without an intermediate DAG)
- **Full purposeful agent**: (M_t, O_t, Σ_t) — the general case

The "simple purposeful" case is worth noting: when the environment is sufficiently well-understood and the action space sufficiently small, the optimal action can be computed directly from M_t and O_t without maintaining an explicit strategy DAG. LQG control is the canonical example. Σ_t becomes necessary when the path from current state to objective involves contingencies, sequential dependencies, and alternative approaches that cannot be captured in a single policy function.

## Model Sufficiency

*[Definition (model-sufficiency)]*
$$S(M_t) = 1 - \frac{I(\mathcal{C}_t;\, o_{t+1:\infty} \mid M_t, a_{t:\infty})}{I(\mathcal{C}_t;\, o_{t+1:\infty} \mid a_{t:\infty})}$$

Model sufficiency measures how much predictive information the model retains relative to the full history. S(M_t) = 1 means M_t is a sufficient statistic for C_t with respect to future observations. S(M_t) < 1 means the model has lost predictive information that the raw history would provide.

**Model class fitness:**
$$\mathcal{F}(\mathcal{M}) = \sup_{M \in \mathcal{M}} S(M)$$

When F(M) < 1 − ε, no model in the current class can adequately represent reality. This triggers structural adaptation (ACT-10).

**Operational form:** The theoretical definition uses infinite future.
The operational form S_Π(M_t) uses finite horizon N_h and policy class Π.

## Software Domain: The Developer's State

For a software developer (or AI coding agent), the three state objects map concretely:

**M_t — codebase understanding**: The developer's mental model of the architecture, dependencies, conventions, and current state of the code. For an AI agent, this is what fits in the context window plus retrieved memory. For a human, this is the working mental model built from code reading, documentation, and team knowledge.

**O_t — the task objective**: "Implement OAuth flow." "Fix the race condition in the session handler." "Refactor the payment module for the new provider." The specification — what done looks like.

**Σ_t — the implementation strategy**: The plan. "First, add the token endpoint (KR1). Then update the session middleware (KR2). Verify existing auth still works (KR3). If the upstream API is unavailable, use the mock adapter pattern." This is a causal DAG with AND/OR structure, observable checkpoints (tests passing), and contingency branches.

**Code quality as observation infrastructure**: A unique property of software is that past actions (writing code) affect future observation quality (reading code). Well-written code has low U_o for future readers; obfuscated code has high U_o. This creates a second-order feedback loop:

    Code quality → U_o → η* → T_developer → slack for principled changes → code quality

This can be virtuous (good code → better comprehension → more tempo → more slack for good code) or vicious (bad code → poor comprehension → less tempo → more rushed code → worse code). The persistence condition (ACT-07) formalizes the threshold between these regimes.

**The specification bound** (from TST T-02): Implementation time is bounded below by specification time, which depends inversely on shared context between specifier and implementer. This is information-theoretic necessity, not technological limitation. As implementation approaches instantaneous (via AI), specification engineering becomes the bottleneck.

**The change-expectation baseline** (from TST T-04): With no additional information, E[n_future_changes | n_past_changes] = n_past_changes. This is the Bayesian consequence of maximum ignorance (Jeffrey's prior), not a heuristic. It provides a principled baseline for investment decisions: invest in abstraction proportionally to observed change frequency.
