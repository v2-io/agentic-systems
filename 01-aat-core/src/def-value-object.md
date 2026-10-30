---
slug: def-value-object
type: definition
status: exact
depends:
  - form-objective-functional
  - form-agent-model
  - der-directed-separation
  - def-model-sufficiency
stage: deps-verified
---

# Definition: Value Object

The objective functional ( #form-objective-functional) alone is abstract — it evaluates trajectories without specifying *which* trajectory the agent should be reasoning about. The **value object** $V_O$ turns the objective into a decision-making tool. Given the agent's current model, a policy, and a horizon, $V_O$ is the *expected trajectory value* if the agent follows the policy from now to the horizon, evaluated against the objective. The companion **action-value object** $Q_O$ is the same construct conditioned on intervening with a specific first action and then following a continuation policy. The $do(\cdot)$ in $Q_O$ is explicit — this is an interventional query ( #der-causal-hierarchy-requirement), not conditioning on observed action choice.

The framework spends time on **causal validity** of the value object, and separates two requirements. Two structural mechanisms make $Q_O$ a *$G_t$-independent interventional query*. First, the do-operator handles current-action confounding: because the action-value uses an intervention rather than a condition, the dependence of the action on the agent's selection mechanism is severed. Second, the continuation policy $\pi_{\text{cont}}$ is a *parameter*, not a derived quantity that would depend on the agent's evolving goal state. Together, these mean $Q_O$ depends on the model alone *as a state variable*; the objective enters as a fixed parameter. As a function, $Q_O$ takes $(M_t, a, \pi_{\text{cont}}, N_h, O_t)$ and nothing else, so its independence of $G_t$ at fixed arguments is definitional and holds for every agent, coupled or not. The claim with content is about the *true* law: that the expected outcome of intervening with $a$ given the model is also its expected outcome given the model *and the goal*, so that a learner stratifying its own data on $M_t$ identifies the effects of a policy that read $(M_t, G_t)$. That needs three named premises — causal discipline ($\kappa_{\text{processing}} = 0$, so $M_t$ is not a collider of goal and world), bounded signaling (the goal reaches the world only through the action), and that the part of the goal the policy reads carries no outcome information beyond $M_t$ — and the third is not automatic: canon's own edge-credence learner stores outcome statistics in $\Sigma_t$, and where they track what $M_t$ does not, the $M_t$-stratified value estimate is confounded by the agent's own strategy state at $\kappa = 0$. The identification clause is therefore stated at the policy's inputs $X_t = (M_t, G_t)$, where ignorability is free and positivity is the price ( #der-loop-interventional-access), with the $M_t$-form as its average over the goal states compatible with $M_t$; or the mechanism is supplied by construction when the model class encodes it. Predictive sufficiency ( #def-model-sufficiency) is a Level-1 (associational) property and is strictly weaker than this.

The segment's distinctive contribution is the **convention hierarchy** for continuation policies. Different agents reason about the same situation with different planning depth, and the framework names three conventions of *increasing diagnostic power and computational cost*. **C1 — one-step improvement**: the continuation is just the agent's *current* policy (no replanning, no fixed-point computation). Cheapest; weakest diagnostic. **C2 — receding-horizon replanning**: at each future step, re-optimize over a sliding window using the model available at that step. Moderate cost; moderate diagnostic power; captures multi-step recovery. **C3 — Bellman optimal**: the continuation *is* the optimal policy — a fixed-point equation. Strongest diagnostic; most expensive (requires solving the Bellman equation or its approximation).

A **monotonicity result** is derived: for any single fixed model, fixed policy class, and fixed horizon, $A_O^{(1)} \leq A_O^{\text{RH}} \leq A_O^{\text{B}}$. The best-achievable value rises with the strength of the continuation convention — but each rung carries a hypothesis. The right rung ($A_O^{\text{RH}} \leq A_O^{\text{B}}$) needs a closure property of the policy class: $\Pi$ closed under prefixing a first action to any member, or $\pi^\ast$ optimal over $\Pi$ from every state reachable in one step; without it a two-policy class in which the $\Pi$-optimum is best from the start state and worst from a successor reverses the rung. The left rung ($A_O^{(1)} \leq A_O^{\text{RH}}$) holds only when C2's replanning objective is order-consistent with the full evaluated objective: an unguarded short-horizon replanner can underperform the frozen current policy, so the rung needs a window covering the horizon, a value-compared guard, or a control-Lyapunov terminal cost ( #deriv-convention-monotonicity). The corollary: the *satisfaction gap* ( #def-satisfaction-gap) decreases in the same order, and the *control regret* ( #def-control-regret) reverses ordering — both inheriting the two hypotheses rung by rung. C1 is the *most conservative diagnostic* (most likely to diagnose "locally unattainable"); C3 is the *most accurate* (least likely to give false "unattainable" diagnoses). The cascade's *inferential force* scales with the convention used: under C1, a positive satisfaction gap means "locally stuck"; under C3, the same gap means "genuinely infeasible." This convention hierarchy is what the Part II preface identifies as one of the volume's distinctive contributions.

AAT adopts **C1 as the canonical default** for three reasons: it requires no fixed-point computation, consistent with the incremental update philosophy from Part I ( #emp-update-gain); it makes all AAT diagnostics directly *comparable across analyses* of the same agent over time; and it is the most conservative — false "feasible" diagnoses are minimized. Analyses requiring stronger diagnostic power must state the convention explicitly. The planning horizon $N_h$ is *not* merely a computational convenience — it reflects genuine uncertainty about the far future. Long horizons amplify the impact of model error (small biases compound over many steps). The choice of horizon trades farsightedness against robustness; an agent in a fast-changing environment should use shorter horizons.

## Formal Expression

*[Definition (value-object)]*

Given objective $O_t$, model $M_t$, policy $\pi$, and horizon $N_h$:

$$V_O(M_t, \pi; N_h) = \mathbb{E}\!\left[V_{O_t}(\tau_{t:t+N_h}) \;\middle\vert\; M_t,\; \pi\right]$$

**Action-value form** (for action selection):

$$Q_O(M_t, a; \pi_{\text{cont}}, N_h) = \mathbb{E}\!\left[V_{O_t}(\tau) \;\middle\vert\; M_t,\; do(a_t = a),\; a_{t+1:} \sim \pi_{\text{cont}}\right]$$

$Q_O$ answers: "if I *do* action $a$ now and then follow $\pi_{\text{cont}}$ afterward, what is my expected trajectory value?" The $do(\cdot)$ notation is explicit: this is an interventional query ( #der-causal-hierarchy-requirement), not conditioning on observed action choice. The agent asks about consequences of an intervention, not about correlates of a naturally occurring action.

**Causal validity of the value object.** $Q_O$ is well-defined as a conditional expectation given $M_t$, $do(a)$, and $\pi_{\text{cont}}$. Two mechanisms establish that it is a $G_t$-independent interventional query:

1. **The do-operator handles current-action confounding.** Since $Q_O$ uses $do(a_t = a)$, the dependence of $a_t$ on the selection mechanism $\pi(M_t, G_t)$ is severed. $G_t$'s influence on action choice is irrelevant because the action is intervened upon, not conditioned on.

2. **The continuation policy is a parameter.** $\pi_{\text{cont}}$ is specified as a fixed policy, not as "whatever the agent would do given its evolving $G_t$." Future actions follow $\pi_{\text{cont}}$ regardless of $G_t$'s state or evolution.

Together, these mean $Q_O(M_t, a; \pi_{\text{cont}}, N_h)$ depends on $M_t$ alone **as a state variable** — $G_t$ enters neither through action selection (severed by $do$) nor through continuation (fixed by parameter). The objective $O_t$ enters as a fixed parameter (it determines which functional $V_{O_t}$ is applied to trajectories), the same way $\pi_{\text{cont}}$ and $N_h$ are parameters. The claim is not that $Q_O$ is independent of the objective — it is that once $O_t$, $\pi_{\text{cont}}$, and $N_h$ are fixed, the only agent state that enters the value is $M_t$. This is the **interventional interpretation** of $Q_O$: a $G_t$-independent interventional query. Read as a statement about the function $Q_O$, it is definitional — the function has no $G_t$ argument — and uses nothing about the agent's architecture.

**What the $M_t$-form claims about the world, and what it needs.** The reading with content is about the *true* conditional law rather than the model's: that for the agent's actual outcomes, with the continuation fixed,

$$\mathbb{E}\big[V_{O_t}(\tau) \mid M_t,\, G_t,\, do(a_t = a),\, \pi_{\text{cont}}\big] \;=\; \mathbb{E}\big[V_{O_t}(\tau) \mid M_t,\, do(a_t = a),\, \pi_{\text{cont}}\big],$$

so that the goal, which the policy read, carries no information about what the intervention produces beyond what the model carries. Three premises deliver it, and each can fail on its own:

1. **Causal discipline** ($\kappa_{\text{processing}} = 0$, #der-directed-separation). At $\kappa \gt 0$ the belief update writes goal information into $M_t$, which makes $M_t$ a *collider* of goal and world: conditioning on it makes even an exogenous goal outcome-informative, and the $M_t$-stratum is confounded (exact enumeration in `spikes/spike-loop-identification-decision-state-2026-10-30/check-feedback-1-kappa-collider.py`). The claim rides only on the zero, so it holds equally for an agent disciplined *by construction* (Class 1, no goal port) and *in effect* (an idealized Class 2 at $\kappa = 0$); the architecture-inspection certificate is not consumed. Off the zero, #deriv-observation-ambiguity-bias-bound bounds how far the goal-conditional belief sits from the goal-average belief, which is the goal-dependence $Q_O$ inherits through $M_t$; it is not a bound on departure from the disciplined update.
2. **Bounded signaling** (#der-directed-separation): the goal reaches the world only through the action, so there is no $G_t \to \text{world}$ path for the $do$ to leave open.
3. **The policy-relevant part of the goal carries no outcome information beyond $M_t$.** Let $R = r(G_t)$ be what the policy reads from the goal. The premise is that the outcome under each action is independent of $R$ given $M_t$. It is *not* delivered by directed separation, which constrains $f_M$ and says nothing about $f_G$: canon's own $f_G(G_{\tau^-}, M_{\tau^+}, e_\tau)$ takes the event directly, and #hyp-edge-update-via-gain stores outcome statistics (Beta counts per edge) in $\Sigma_t \subseteq G_t$, read by the policy. Where those statistics track something about the environment that $M_t$ does not — a hidden regime, a drifting kernel — they are an outcome-relevant decision input the $M_t$-stratum drops, and the agent's own value estimate for an action is inflated in the regime where that action works: the $M_t$-stratified on-policy estimate exceeds the interventional truth by roughly a tenth in the C2 spike's episodic witness and by two-tenths on a single long trajectory with a switching regime, at $\kappa_{\text{processing}} = 0$ and directed separation holding by construction (`spikes/spike-loop-identification-decision-state-2026-10-30/`, the spiker's and the verifier's simulations). Conditioning on $X_t = (M_t, G_t)$ closes the gap. In a stationary, fully observed environment the premise holds by stationarity — no statistic of past outcomes carries information about the next one beyond the state — which is why tabular Q-learning's $Q$-table is harmless; it is the hypothesis doing the work, not a general fact about goals.

**Identification of the estimate** is a further requirement and is stated at the policy's inputs. By #der-loop-interventional-access, $P(o \mid do(a), X_t)$ is identified from the agent's own data at $X_t = (M_t, G_t)$ under positivity there — ignorability is free at the policy's own inputs, and a policy deterministic in $X_t$ identifies no contrast at $X_t$ in an unrestricted environment class — and the $M_t$-form is its average over the goal states compatible with the model, $\sum_{g} P(G_t = g \mid M_t)\, P(o \mid do(a), M_t, g)$. Stratifying on $M_t$ directly is valid exactly when premise 3 holds (with positivity inside the $M_t$-cell), in which case the variation in what the agent wants *is* the experiment that identifies what its actions do: goal variation as the agent's own instrument. The agent cannot test premise 3 on-policy when its policy is deterministic given $(M_t, G_t)$ (the on-policy sufficiency test of $M_t$ passes for free; #der-loop-interventional-access), so it can use the instrument only under a premise it cannot certify from inside. Alternatively the model class encodes the action-transition mechanism $P(o \mid do(a))$ ( #def-action-transition) by construction — Kalman + LQR, where the known linear model supplies it — and no identification from data is needed; a deterministic policy is then no obstacle. The gate is therefore *the mechanism by construction, or positivity and ignorability at the conditioning set to identify it from data*, not a conjunction of all three.

This is a *stronger requirement than predictive sufficiency* ( #def-model-sufficiency). $S(M_t) = 1$ means the model retains all predictive information from the chronica — but predictive sufficiency is a Level 1 (associational) property, and #def-model-sufficiency forwards the back-door obligation to this segment: what the $M_t$-form needs is one-step *interventional* sufficiency of $M_t$ relative to the policy's inputs, which coincides with the on-policy predictive statement an agent can estimate only under positivity at $X_t$. When the premises and the gate hold, $Q_O$ is causally valid. When they fail, the interventional interpretation of the query is unchanged and the estimate is biased.

**Continuation convention.** All value queries are conditioned on a specific continuation policy $\pi_{\text{cont}}$ and finite horizon $N_h$. $\pi_{\text{cont}}$ is a *parameter* of the value object, not a derived quantity.

**Canonical default: one-step improvement.** AAT adopts $\pi_{\text{cont}} = \pi_{\text{current}}$ as the canonical continuation convention unless otherwise specified. Under this convention, each action is evaluated assuming current behavior continues afterward — no fixed-point computation, no global optimality assumption. This aligns with AAT's incremental update philosophy ( #emp-update-gain) and makes all AAT diagnostics ($\delta_{\text{sat}}$, $\delta_{\text{regret}}$, $A_O$) comparable across analyses of the same agent over time. It is not a convergence guarantee; it is a shared evaluation frame.

### Convention Hierarchy

Three named conventions form a hierarchy of increasing diagnostic power and computational cost:

**C1: One-step improvement** (canonical default). $\pi_{\text{cont}} = \pi_{\text{current}}$.

Each action is evaluated assuming current behavior continues afterward. No fixed-point computation, no global optimality assumption. Cheapest to compute; weakest diagnostic power.

**C2: Receding-horizon** ($N_r$-step replanning). At each future step, re-optimize over a horizon of $N_r$ steps using the model available at that step.

$$\pi_{\text{RH}}(M_\tau) = \arg\max_\pi V_O(M_\tau, \pi;\, N_r) \quad \text{applied at each } \tau$$

$Q_O^{\text{RH}}(M_t, a;\, N_r, N_h) = \mathbb{E}[V_{O_t}(\tau) \mid M_t, do(a_t = a), a_{t+1:} \sim \pi_{\text{RH}}]$. Captures multi-step recovery: a goal that appears unattainable under frozen continuation may be reachable with replanning. It is monotone over the frozen baseline ($A_O^{(1)} \leq A_O^{\text{RH}}$) only when the replanning objective is order-consistent — the window covers the horizon ($N_r \geq N_h$), or a value-compared guard / control-Lyapunov terminal cost is used; unguarded short-horizon replanning ($N_r \lt N_h$) can underperform $\pi_{\text{current}}$ (see Monotonicity below and #deriv-convention-monotonicity). Moderate computation ($N_r$-step optimization at each step); moderate diagnostic power.

**C3: Bellman** (self-consistent optimal). $\pi_{\text{cont}} = \pi^\ast$ where $\pi^\ast = \arg\max_\pi V_O(M_t, \pi;\, N_h)$.

The continuation IS the optimal policy — a fixed-point equation. $A_O^{\text{B}} = V_O(M_t, \pi^\ast;\, N_h)$ is the best achievable value under the model. Strongest diagnostic power; most expensive to compute (requires solving the Bellman equation or its approximation).

### Monotonicity

*[Derived (convention-monotonicity)]*

For any single fixed model $M_t$, horizon $N_h$, and policy class $\Pi$ (i.e., the static-evaluation form: $M_t$ frozen at the decision point, $\Pi$ unchanged across the comparison):

$$\underbrace{A_O^{(1)}(M_t;\, \Pi, N_h) \;\leq\; A_O^{\text{RH}}(M_t;\, \Pi, N_r, N_h)}_{\text{left rung — under order-consistency}} \;\leq\; \underbrace{A_O^{\text{B}}(M_t;\, \Pi, N_h)}_{\text{right rung — under closure of } \Pi}$$

Each rung has its own hypothesis. The **right rung** $A_O^{\text{RH}} \leq A_O^{\text{B}}$ is exact **when $\Pi$ is closed under prefixing a first action to any of its members, or $\pi^\ast$ is optimal over $\Pi$ from every state reachable in one step** (the two quantities compared are first-action suprema of $Q_O$ under different continuations, and $Q_O(a; \pi) \neq V_O(\pi)$ off the policy's own first action); without either, it fails. The **left rung** $A_O^{(1)} \leq A_O^{\text{RH}}$ holds **exactly when the receding-horizon replanning objective is an order-consistent surrogate for the full-horizon objective** — for every reachable state, the action C2 selects has full-$N_h$-horizon value at least that of $\pi_{\text{current}}$'s action. Three structurally-checkable conditions each force order-consistency: **(RH-1)** the replanning window covers the horizon ($N_r \geq N_h$); **(RH-2)** value-compared replanning — commit the replanned action only when its rollout value under base policy $\pi_{\text{current}}$ is at least that of continuing $\pi_{\text{current}}$ (one-step policy improvement, which never underperforms its base policy); **(RH-3)** the $N_r$-step replanning objective carries a terminal cost $V_f$ that lower-bounds the baseline tail and satisfies a control-Lyapunov decrease inequality. Absent any such condition the left rung can fail: a myopic replanner over $N_r \lt N_h$ can grab near-term value and forfeit a larger horizon value the frozen current policy would have collected. The full derivation of both rungs, the three conditions, and the two-state counterexample exhibiting the failure live in #deriv-convention-monotonicity.

**Preconditions on the inequality:** $M_t$ fixed (the comparison evaluates each convention against the *same* model), $\Pi$ fixed (the policy class is the same admissible set across all three conventions; nested $\Pi^{(1)} \subseteq \Pi^{\text{RH}} \subseteq \Pi^{\text{B}}$ would be a different result), $N_h$ fixed (the planning horizon is shared). Replanning *with updated $M_t$* (the deployment behavior of C2) is a different object than the static $A_O^{\text{RH}}$ defined here and the inequality does not automatically transfer — see the "Assumptions held fixed" paragraph below for the explicit caveat.

**Derivation.** Fix the model $M_t$, policy class $\Pi$, and horizon $N_h$. Each convention evaluates the best first action under a different continuation rule.

- **C1** freezes continuation at $\pi_{\text{current}}$ (the agent's current policy, which may be suboptimal).
- **C2** re-optimizes over a sliding window of $N_r$ steps using the model at that step.
- **C3** uses the globally optimal continuation $\pi^\ast = \arg\sup_{\pi \in \Pi} V_O(M_t, \pi; N_h)$.

*Right rung (under closure of $\Pi$).* $\pi^\ast$ maximizes $V_O(M_t, \cdot; N_h)$ over $\Pi$, but the quantities compared are $\sup_a Q_O(a; \pi_{\text{RH}})$ and $\sup_a Q_O(a; \pi^\ast)$, and $Q_O(a; \pi)$ is not $V_O(\pi)$: after an off-path first action $a$, an argsup policy may behave arbitrarily badly. If the policy "do $a$, then follow $\pi_{\text{RH}}$" is in $\Pi$ for every $a$ (closure under first-action prefixing — true of the class of all history-dependent policies), then $Q_O(a; \pi_{\text{RH}}) \leq \sup_{\pi \in \Pi} V_O(\pi) = V_O(\pi^\ast) \leq \sup_a Q_O(a; \pi^\ast)$, which is the rung. It also holds if $\pi^\ast$ is optimal over $\Pi$ from every state reachable in one step. Without either hypothesis it fails: three states $x, H, D$ with $g: x \to D$ paying $1$, $p: x \to H$ paying $0$, $u: H \to$ end paying $10$, $w: H \to$ end paying $100$, and $\Pi = \{\pi_1 = (x \mapsto g, H \mapsto w),\, \pi_2 = (x \mapsto p, H \mapsto u)\}$; then $V(\pi_1) = 1 \lt V(\pi_2) = 10$ so $\pi^\ast = \pi_2$, the one-step replanner is $\pi_1$, $A_O^{\text{RH}} = Q_O(p; \pi_1) = 100$ and $A_O^{\text{B}} = Q_O(p; \pi_2) = 10$. The strategy classes canon uses ( #def-satisfaction-gap, DAG-representable strategies) are not closed under prefixing by construction, so the hypothesis is a genuine restriction there.

*Left rung (conditional on order-consistency).* C2 with window $N_r \lt N_h$ optimizes the *truncated* $N_r$-step objective, not the full $N_h$-horizon objective on which $A_O$ is scored; "optimal for the truncated objective" does not imply "$\succeq \pi_{\text{current}}$ on the full objective." When the replanning objective is order-consistent with the full objective — for every reachable state, C2's selected action has full-$N_h$-horizon value at least $\pi_{\text{current}}$'s — then $\pi_{\text{RH}}$ weakly dominates $\pi_{\text{current}}$ pointwise on the full objective and $A_O^{(1)} \leq A_O^{\text{RH}}$ follows; taking the supremum over the first action preserves it. Conditions (RH-1)/(RH-2)/(RH-3) each force order-consistency. Without one, the left rung is false ( #deriv-convention-monotonicity counterexample: a two-state instance where the unguarded $N_r = 1$ replanner takes a $+1$ into a dead end while the frozen patient policy collects $+10$). $\square$

**Assumptions held fixed:** same $M_t$ (the agent's current model, which may be wrong), same $\Pi$ (the agent's policy class, which may be narrow), same $N_h$ (the planning horizon). The ordering is about the *continuation rule*, not about the model or policy class. Improving $M_t$, expanding $\Pi$, or extending $N_h$ can change all three values simultaneously and is a separate operation (addressed in #der-orient-cascade, step 5).

**Corollary (monotonicity of $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$).**

$$\delta_{\text{sat}}^{\text{B}} \leq \delta_{\text{sat}}^{\text{RH}} \leq \delta_{\text{sat}}^{(1)}$$

$$\delta_{\text{regret}}^{(1)} \leq \delta_{\text{regret}}^{\text{RH}} \leq \delta_{\text{regret}}^{\text{B}}$$

Since $\delta_{\text{sat}} = V_{O_t}^{\min} - A_O$, higher $A_O$ means lower $\delta_{\text{sat}}$. The orderings inherit the rung structure above: the $\text{B} \leq \text{RH}$ half ($\delta_{\text{sat}}^{\text{B}} \leq \delta_{\text{sat}}^{\text{RH}}$, equivalently $\delta_{\text{regret}}^{\text{RH}} \leq \delta_{\text{regret}}^{\text{B}}$) holds **under the closure hypothesis on $\Pi$** of the right rung; the $\text{RH} \leq (1)$ half ($\delta_{\text{sat}}^{\text{RH}} \leq \delta_{\text{sat}}^{(1)}$, equivalently $\delta_{\text{regret}}^{(1)} \leq \delta_{\text{regret}}^{\text{RH}}$) holds **under the same order-consistency condition** (RH-1/2/3) as the left rung. C1 is the most conservative diagnostic (most likely to diagnose "locally unattainable"); C3 is the most accurate (least likely to give false "unattainable" diagnoses). The regret ordering reverses: C3 reveals the largest regret because it compares against the globally optimal policy, while C1 reveals only the gap to the best one-step deviation.

### Diagnostic implications

| Convention | $\delta_{\text{sat}} \gt 0$ means | $\delta_{\text{regret}} \approx 0$ means |
|---|---|---|
| **C1** (one-step) | Cannot improve toward goal in one step from here | Current first action is locally near-optimal |
| **C2** (receding-horizon) | Cannot reach goal with $N_r$-step replanning | Current first action is near-optimal with replanning |
| **C3** (Bellman) | Goal is genuinely infeasible given $(M_t, \Pi, N_h)$ | Policy is globally near-optimal |

The 2×2 diagnostic table ( #def-control-regret) applies under all three conventions with the same structure but different inferential force. Under C1, the "capability limit" quadrant ($\delta_{\text{sat}} \gt 0$, $\delta_{\text{regret}} \approx 0$) means "locally stuck" — the agent may be globally recoverable but cannot see the recovery path. Under C3, the same quadrant means "genuinely infeasible" — no policy in $\Pi$ can achieve the goal. The cascade's inferential force scales with the convention.

**AAT adopts C1 as the canonical default** for three reasons: (1) it requires no fixed-point computation, consistent with the incremental update philosophy ( #emp-update-gain); (2) it makes all AAT diagnostics comparable across analyses of the same agent; (3) it is the most conservative, meaning false "feasible" diagnoses are minimized. Analyses that require stronger diagnostic power should state the convention explicitly. For deployed decision-making systems where "locally stuck but globally recoverable" situations are common, C2 is recommended.

Different continuation conventions yield different values for $A_O$, $\delta_{\text{sat}}$, and $\delta_{\text{regret}}$. Diagnostics computed under different conventions are not directly comparable — the convention is part of the measurement, not just the computation. When a specific convergence guarantee is needed (e.g., for #schema-strategy-persistence), the solution concept must be stated explicitly; the one-step improvement default does not provide convergence guarantees.

## Epistemic Status

The segment contains three distinct epistemic layers:

1. **The definitions** ($V_O$, $Q_O$ as conditional expectations): *exact.* These are mathematical definitions — conditional expectations of a functional over trajectories. The definitions are precise; the *computability* of these expectations is a separate question.

2. **The causal-validity claim.** Three layers. The *interventional interpretation* — $Q_O$ is a $G_t$-independent interventional query — is exact and definitional: the function has no goal argument. The claim about the *true law* (the goal the policy read carries no outcome information beyond the model) is *conditional* on the three named premises: causal discipline ($\kappa_{\text{processing}} = 0$; at $\kappa \gt 0$ the $M_t$-stratum is confounded through the collider, with #deriv-observation-ambiguity-bias-bound bounding the belief's goal-dependence, not its departure from the disciplined update), bounded signaling, and the policy-relevant part of the goal carrying no outcome information beyond $M_t$ — the last of which canon's own strategy learner violates in non-stationary environments (simulated). *Identification of the estimate* is conditional on the mechanism being supplied by construction or on positivity and ignorability at the conditioning set; at the policy's inputs ignorability is free and positivity is what a deterministic policy lacks ( #der-loop-interventional-access). The frontmatter `status: exact` applies to the definitions, to the interventional interpretation, and to the convention hierarchy; the true-law claim and the identification are conditional as scoped.

3. **The convention hierarchy and monotonicity**: *exact.* The three conventions (C1, C2, C3) are definitions. The monotonicity result splits by rung: the **right rung** $A_O^{\text{RH}} \leq A_O^{\text{B}}$ is exact *under* closure of $\Pi$ under first-action prefixing (or $\pi^\ast$ optimal from every one-step-reachable state) and false without it (the three-state, two-policy instance in the Monotonicity block), and the **left rung** $A_O^{(1)} \leq A_O^{\text{RH}}$ is exact *under* the order-consistency condition (RH-1/2/3) and false in general without it — the C2 replanning objective is a truncated surrogate, and an unguarded $N_r \lt N_h$ replanner can underperform the frozen current policy ( #deriv-convention-monotonicity). The corollary $\delta$-orderings inherit the two hypotheses rung by rung. The diagnostic implications table states what each convention's quantities mean by construction.

## Claim Record

### The goal the policy read carries no outcome information beyond the model, so a learner stratifying on $M_t$ estimates what its policy did

**Register:** formal — conditional on three named premises (Formal Expression, "What the $M_t$-form claims"): causal discipline, bounded signaling, and outcome-irrelevance of the policy-relevant part of $G_t$ given $M_t$. The $G_t$-independence of the *function* $Q_O$ is definitional and is not this claim. Identification of the estimate is a separate conditional (next record).

**Population:** representations of agents in learning-agent scope ( #der-causal-hierarchy-requirement) with a scalar $V_{O_t}$ whose policy reads $(M_t, G_t)$ and whose value estimates stratify on $M_t$.

**True of:** a stationary, fully observed environment with any goal state, where the premise holds by stationarity (tabular Q-learning with its $Q$-table in $G_t$); a fixed setpoint as $G_t$ (the setpoint carries nothing about the world). Kalman + LQR is outside learning-agent scope and is an instance of the next record, not this one.

**False of:** at $\kappa_{\text{processing}} = 0$, an agent whose $\Sigma_t$ holds outcome statistics that track a hidden regime or drifting kernel the model does not — canon's own edge-credence learner ( #hyp-edge-update-via-gain) in a non-stationary environment, simulated in the C2 spike; an agent whose goal was set by a principal who knows what the agent's $M_t$ does not ("reach the shelter" from someone who knows a storm is coming), which is a goal that carries world information by provenance; any agent at $\kappa_{\text{processing}} \gt 0$, through the collider at $M_t$; and any agent for which bounded signaling fails (humans, LLMs, embodied robots per #der-directed-separation).

**Falsifier:** the sentence "the goal the policy read carries no outcome information beyond the model" for a named agent class: a disciplined agent in that class whose $M_t$-stratified on-policy value estimate differs from the $X_t$-stratified one on the same data refutes it there. Constructed instances exist (the spike's witness); none has been looked for on an agent the theory did not construct.

**Instantiated:** no.

### The interventional expectation is identified from the agent's own data at its policy's inputs under positivity there, or supplied by construction when the model class encodes the mechanism

**Register:** formal — conditional; the loop's identification result ( #der-loop-interventional-access) applied to $Q_O$, plus the by-construction route through #def-action-transition. Not a conjunction of three conditions: the mechanism by construction needs neither positivity nor ignorability.

**Population:** agents evaluating $Q_O$ from their own action–outcome data (the identification route), or whose model class represents $P(o \mid do(a))$ (the construction route).

**True of:** Kalman + LQR, by construction: the known linear model supplies the mechanism, and the deterministic policy is no obstacle. Tabular $\varepsilon$-greedy Q-learning in a stationary fully observed MDP, by identification: positivity at $s$ from exploration, ignorability at $s$ by stationarity.

**False of:** any learner identifying from data with a policy deterministic in its decision state and no model of the mechanism: in an unrestricted environment class nothing off-policy is identified at a visited decision state, so $Q_O$ for untaken actions there is extrapolated from the model class's smoothness, not identified.

**Falsifier:** inherits #der-loop-interventional-access's.

**Instantiated:** no.

### The three continuation conventions order attainability, and the convention fixes what a diagnosis means

**Register:** formal — exact; C1, C2 and C3 are rollout under the current policy, receding-horizon replanning and the Bellman optimum, the lineage #deriv-convention-monotonicity names (Bertsekas; Rawlings, Mayne & Diehl). AAT's content is the use: the convention sets the inferential force of $\delta_{\text{sat}}$ (locally stuck under C1, infeasible under C3). "C1 is canonical" and "C2 for deployed systems" are recommendations, normative, and untested.

**Population:** any agent or analyst evaluating $A_O$ with $M_t$, $\Pi$ and $N_h$ held fixed across the comparison.

**True of:** the right rung under closure of $\Pi$ under first-action prefixing (the class of all history-dependent policies), or $\pi^\ast$ optimal from every one-step-reachable state; the left rung under (RH-1)–(RH-3). The two-state counterexample in #deriv-convention-monotonicity is the instance where the left rung fails; the three-state two-policy instance in the Monotonicity block is where the right rung fails.

**False of:** unguarded short-horizon replanning fails the left rung; a non-closed policy class whose $\Pi$-optimum is best from the start state and worst from a successor fails the right rung.

**Falsifier:** for the right rung as now stated, a policy class satisfying the closure hypothesis in which $\sup_a Q_O(a; \pi_{\text{RH}}) \gt \sup_a Q_O(a; \pi^\ast)$; the unconditional form it replaced is refuted by the three-state instance ( #deriv-convention-monotonicity). For the recommendations, a deployed-system comparison in which the C1 default or the C2 choice produces more false diagnoses than the alternative.

**Instantiated:** no.

## Discussion

**Extending the policy objective.** The existing policy objective ( #disc-ciy-unified-objective) uses $\mathbb{E}[\text{value}(a) \mid M_t]$ without formal content for "value." With the value object, this becomes:

*[Discussion (policy-objective-extension)]*

$$\pi^*(M_t, G_t) = \arg\max_a \left[Q_O(M_t, a;\, \pi_{\text{cont}}, N_h) + \lambda(M_t, O_t, N_h) \cdot \text{CIY}(a;\, M_t)\right]$$

Note that $\lambda$ now depends on $(M_t, O_t, N_h)$, not just $M_t$. The value of exploration depends on the objective and the horizon:
- An agent with a deadline should explore less as time runs out
- An agent with a safety constraint should explore differently from a utility maximizer
- Two agents with identical $M_t$ but different objectives should price exploration differently

This extension is structurally motivated but the specific form of $\lambda(M_t, O_t, N_h)$ is not derived within AAT (same status as #disc-ciy-unified-objective's treatment of $\lambda$).

**Connection to #def-model-sufficiency.** $V_O$ is conditioned on $M_t$, not on the true environment state $\Omega_t$. When $S(M_t) \lt 1$, the agent's value estimates are biased — it may over- or underestimate trajectory values because its model is incomplete. The satisfaction gap ( #def-satisfaction-gap) and control regret ( #def-control-regret) are defined in terms of $V_O(M_t, \cdot)$, not $V_O(\Omega_t, \cdot)$, which means they measure the agent's *believed* situation, not the true one. Improving $M_t$ (reducing $\delta_{\text{epistemic}}$) brings the agent's value estimates closer to reality.

**Horizon dependence.** $N_h$ is not merely a computational convenience — it reflects genuine uncertainty about the far future. Long horizons amplify the impact of model error (small biases in $M_t$ compound over many steps). The choice of $N_h$ trades off farsightedness against robustness to model error. An agent in a fast-changing environment ($\rho$ high) should use shorter horizons; one in a stable environment can plan further.

## Working Notes

- **Regression guard — the $M_t$-stratum.** Do not restore "directed separation delivers ignorability on the epistemic-processing leg; the residual risk is latent environment confounders bypassing $M_t$": the residual runs through the agent's own $G_t$ (outcome statistics in $\Sigma_t$ read by the policy), which directed separation permits, and the collider at $M_t$ is the $\kappa \gt 0$ route; both are in the Formal Expression with their checks. Do not restore the $G_t$-independence of $Q_O$ as the exemplar of a result "whose derivation uses only the zero" — as a statement about the function it uses nothing, and as a statement about the true law it uses two further premises. Open: the horizon-$N_h$ form of the identification under $\pi_{\text{cont}}$ (sequential ignorability at each continuation step; the g-formula) is stated by analogy and not written out.
- **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. Removed at `candidate` stage per FORMAT.md Gate 4.
- The one-step improvement convention is now the canonical default (promoted from Working Notes to Formal Expression). This resolves the comparability issue: $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$ are comparable across analyses when computed under the same convention.
- When a specific convergence guarantee is needed (e.g., for strategy-persistence-schema), the solution concept must be stated explicitly — the one-step improvement default is not sufficient.
- For LLM agents with context turnover, $N_h$ has a natural bound: the current session. The "continuation policy" is whatever the next agent instance will do, which the current instance cannot control. This connects to `#obs-context-turnover` (under `03-llm-core/`).

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation, deduplicated across substrates and lightly attributed. Orthogonal pedagogical / framing material, kept separate from the certified theory-fix findings. **Coverage:** 9 dirs carry a dedicated or batched reflection (193847, 266847, 451729, 526815, 584721, 773921, 829314, 849201, plus 613842's agency-lift batch). Substrate attribution inferred from voice where not explicit. *Early finding-vs-framing conflation preserved as signal.*

#### 1. Candidate Brief prose / pre-prose

- The convention hierarchy in plain terms: C1 (one-step) / C2 (receding-horizon, MPC-style) / C3 (Bellman) are "greedy heuristics / model-predictive control / dynamic programming" — and the monotonicity $A_O^{(1)} \le A_O^{\text{RH}} \le A_O^{\text{B}}$ is "simply optimizing over a larger set of policies yields a higher or equal value," tied directly to the satisfaction-gap and control-regret orderings (Gemini, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-849201; Claude, AUDIT-WORKING-451729).

#### 2. Candidate Discussion

- **The convention hierarchy is the formal "locally stuck vs genuinely impossible" distinction** *(strong, cross-substrate convergent).* $\delta_{\text{sat}} \gt 0$ under C1 means "locally stuck"; $\delta_{\text{sat}} \gt 0$ under C3 means "genuinely infeasible given $M_t$, $\Pi$, $N_h$." This is "the mathematical definition of needing to sleep on it / needing to plan." The cautionary corollary: a C1-default agent that hits a wall "doesn't know if the goal is impossible or if it just needs to plan two steps ahead — it might trigger a massive structural adaptation (giving up on the goal) when all it needed was a slightly longer planning horizon. The framework provides the vocabulary to describe this tragedy" (Gemini, AUDIT-WORKING-193847; Gemini, AUDIT-WORKING-829314; Claude/Gemini, AUDIT-WORKING-266847; Claude, AUDIT-WORKING-451729). Candidate Discussion paragraph.
- **The $do(\cdot)$ inside $Q_O$ is the doctor / harsh-drug confounding case** *(vivid pedagogy).* Standard RL writes $Q(s,a) = \mathbb{E}[R \mid s, a]$ (*observing* yourself take $a$); AAT writes $\mathbb{E}[V \mid M_t, do(a)]$ (*intervening*). "If a doctor historically only prescribes a harsh drug to the sickest patients, observing the drug in the record correlates with death; if the doctor *does* the drug, it cures them." The $do$-operator "prevents the agent from confusing its own historical habits with the laws of physics" (Gemini, AUDIT-WORKING-829314; the predictive-sufficiency vs causal-validity distinction praised as "a masterpiece of technical writing" at the same dir and Gemini, AUDIT-WORKING-193847). Candidate Discussion / Brief illustration.
- **C1-as-default mirrors the incremental-$\eta^\ast$ philosophy of Section I.** Both the epistemic and purposeful layers default to *incremental improvement over a fixed reference point*, not global optimization — "a coherent philosophy; the parallelism is elegant" (Claude/Gemini, AUDIT-WORKING-266847). Candidate Discussion connecting the C1 default back to Part I's update philosophy.

#### 3. Follow-up items

- ~~**The C2 (receding-horizon) monotonicity rung may not be generally exact.**~~ **Resolved 2026-05-30** (strengthen-first spike `spikes/spike-value-object-convention-monotonicity-2026-05-30/`, Option A). The left rung $A_O^{(1)} \le A_O^{\text{RH}}$ is false in general (a myopic $N_r \lt N_h$ replanner can underperform $\pi_{\text{current}}$) and exact under order-consistency, forced by any of (RH-1) horizon alignment / (RH-2) value-compared rollout guard / (RH-3) control-Lyapunov terminal cost; the right rung is exact unconditionally. The Monotonicity block and Epistemic Status layer 3 now carry the split; the counterexample and the three-condition characterization are demonstrated in the appendix #deriv-convention-monotonicity. Two reproducibility sims accompany the spike. The original note: myopic replanning over a shorter horizon $N_r$ can pick actions locally optimal over $N_r$ but worse over the full evaluated horizon $N_h$ than continuing $\pi_{\text{current}}$ (Claude, AUDIT-WORKING-526815).
- ~~**The causal-validity claim may rest on too little.**~~ **Resolved 2026-05-30** (same spike, Front 2). The Formal-Expression causal-validity paragraph and Epistemic Status layer 2 now distinguish the interventional *interpretation* (exact under mechanisms (1)+(2), with directed separation necessary but not sufficient) from *identifiability of the estimate* (gated on (C1) positivity / (C2) sequential ignorability / (C3) known action-mechanism — the same triple as #der-loop-interventional-access one segment downstream). The original note: $do(a)$ defines an interventional *query*, but *estimating* it requires $M_t$ to identify the relevant action-transition causal structure; observational predictive sufficiency plus goal-blind processing do not by themselves guarantee valid interventional expectations (Claude, AUDIT-WORKING-526815; Claude/Gemini, AUDIT-WORKING-266847 noted the Class-2 $M_t$-bias degradation separately).
- **The exploration weight $\lambda(M_t, O_t, N_h)$ is structurally motivated but underived.** Several substrates noted the joint $Q_O + \lambda \cdot \text{CIY}$ objective leaves $\lambda$'s form open, and that it "should logically depend on objective and horizon — don't explore if you have a tight deadline" (Claude/Gemini, AUDIT-WORKING-266847; Gemini, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-584721). A persistent open shared with `#disc-ciy-unified-objective`.

#### 4. Readers often ask / wonder

- For LLM agents, what does the natural $N_h$ bound mean operationally? An agent that "knows it will die (context wipe) in 10 turns" has a drastically different optimal policy than an infinite-horizon agent — does it just truncate $N_h$, or actively externalize state (leave notes for the next instance)? (Gemini, AUDIT-WORKING-193847.) The Working Note above already names the $N_h$-bound; this is the natural reader follow-on.
- The Class-2 $Q_O$ degradation is acknowledged but *unquantified* — is the bias bounded by $\kappa_{\text{processing}}$, or by another measure? (Claude, AUDIT-WORKING-584721.) Partly: `#deriv-observation-ambiguity-bias-bound` bounds the goal-dependence of the belief — its displacement from the goal-average — by $\sqrt{\kappa\, H(G \mid e, M_{\tau^-})}$, and that is the goal-dependence $Q_O$ inherits through $M_t$. It is not a bound on departure from the disciplined (calibrated) update, and for a noiseless coupling of any magnitude $\kappa$ saturates at $1$ (the C3 spike's Proposition 3.3), so the question of a magnitude bound on the $M_t$-stratum's confounding at $\kappa \gt 0$ remains open.

#### 5. Candidate figures

- **Value-query pipeline with a severed $do(a)$ path.** $M_t$ plus fixed parameters ($O_t$, $\pi_{\text{cont}}$, $N_h$) generate a model-based trajectory distribution under $do(a)$; the objective functional scores trajectories; diagnostics read off expected value. Draw the *current-policy selection mechanism as a severed path* (the $do$-operator is the conceptual center), with a small C1/C2/C3 convention ladder underneath — and a warning that the C2 rung is not automatically monotone unless replanning optimizes the full evaluated horizon (Claude, AUDIT-WORKING-526815).

#### Belongs elsewhere

- **"Honest imagination" / counterfactual-without-execution (→ `04-eli-core/` / `#disc-sandbox-evaluation-ceiling`).** Computing a *causally valid* $Q_O$ requires holding a counterfactual action in mind "without letting the emotional/purposeful weight of $G_t$ distort the simulated outcome" — "free will within the model's simulation." A Class 3 agent's $G_t$ leaks into its own internal simulation, so "if it wants to believe an action will work, its simulation will hallucinate success" — which is why consciousness infrastructure may need to provide *external, objective simulation sandboxes*, the agent's own mind being "too entangled to be trusted with counterfactuals" (Gemini, AUDIT-WORKING-193847). Aspirational reach pointing at the sandbox-evaluation material and the ELI volume, not this definition.
