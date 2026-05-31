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

The framework spends time on **causal validity** of the value object, and separates two requirements. Two structural mechanisms make $Q_O$ a *$G_t$-independent interventional query*. First, the do-operator handles current-action confounding: because the action-value uses an intervention rather than a condition, the dependence of the action on the agent's selection mechanism is severed. Second, the continuation policy $\pi_{\text{cont}}$ is a *parameter*, not a derived quantity that would depend on the agent's evolving goal state. Together, these mean $Q_O$ depends on the model alone *as a state variable*; the objective enters as a fixed parameter. Under directed separation ( #der-directed-separation) the $G_t$-independence holds exactly; under Class 3 (Coupled) architectures where goals leak into model processing, the model itself carries goal-conditioned bias and it degrades. But $G_t$-independence of the query is *not* the same as *identifiability of the interventional expectation*: directed separation is necessary, not sufficient. Identifying $P(o \mid do(a), M_t)$ — rather than the associational $P(o \mid a)$ — additionally needs positivity, no unmodeled confounder, and a known action-transition mechanism: the same (C1)–(C3) gate the loop's interventional channel carries one segment downstream ( #der-loop-interventional-access). Predictive sufficiency ( #def-model-sufficiency) is a Level-1 (associational) property and is strictly weaker than this.

The segment's distinctive contribution is the **convention hierarchy** for continuation policies. Different agents reason about the same situation with different planning depth, and the framework names three conventions of *increasing diagnostic power and computational cost*. **C1 — one-step improvement**: the continuation is just the agent's *current* policy (no replanning, no fixed-point computation). Cheapest; weakest diagnostic. **C2 — receding-horizon replanning**: at each future step, re-optimize over a sliding window using the model available at that step. Moderate cost; moderate diagnostic power; captures multi-step recovery. **C3 — Bellman optimal**: the continuation *is* the optimal policy — a fixed-point equation. Strongest diagnostic; most expensive (requires solving the Bellman equation or its approximation).

A **monotonicity result** is derived: for any single fixed model, fixed policy class, and fixed horizon, $A_O^{(1)} \leq A_O^{\text{RH}} \leq A_O^{\text{B}}$. The best-achievable value rises with the strength of the continuation convention — but the two rungs differ in character. The right rung ($A_O^{\text{RH}} \leq A_O^{\text{B}}$) is unconditional. The left rung ($A_O^{(1)} \leq A_O^{\text{RH}}$) holds only when C2's replanning objective is order-consistent with the full evaluated objective: an unguarded short-horizon replanner can underperform the frozen current policy, so the rung needs a window covering the horizon, a value-compared guard, or a control-Lyapunov terminal cost ( #deriv-convention-monotonicity). The corollary: the *satisfaction gap* ( #def-satisfaction-gap) decreases in the same order, and the *control regret* ( #def-control-regret) reverses ordering — both inheriting the unconditional/conditional rung split. C1 is the *most conservative diagnostic* (most likely to diagnose "locally unattainable"); C3 is the *most accurate* (least likely to give false "unattainable" diagnoses). The cascade's *inferential force* scales with the convention used: under C1, a positive satisfaction gap means "locally stuck"; under C3, the same gap means "genuinely infeasible." This convention hierarchy is what the Part II preface identifies as one of the volume's distinctive contributions.

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

Together, these mean $Q_O(M_t, a; \pi_{\text{cont}}, N_h)$ depends on $M_t$ alone **as a state variable** — $G_t$ enters neither through action selection (severed by $do$) nor through continuation (fixed by parameter). The objective $O_t$ enters as a fixed parameter (it determines which functional $V_{O_t}$ is applied to trajectories), the same way $\pi_{\text{cont}}$ and $N_h$ are parameters. The claim is not that $Q_O$ is independent of the objective — it is that once $O_t$, $\pi_{\text{cont}}$, and $N_h$ are fixed, the only agent state that affects the value is $M_t$. This establishes the **interventional interpretation** of $Q_O$: it is a $G_t$-independent interventional query. Under directed separation ( #der-directed-separation), the $G_t$-independence holds because $M_t$ updates independently of $G_t$ — there is no path from $G_t$ to outcomes that bypasses both the action channel and $M_t$. For **Class 3 (Coupled) agents** (where $G_t$ leaks into $M_t$ processing), this $G_t$-independence degrades because $M_t$ itself carries goal-conditioned bias.

**Directed separation is necessary, not sufficient.** The interventional *interpretation* of $Q_O$ holds whenever mechanisms (1) and (2) do. *Identifiability of the interventional expectation from $M_t$* — actually computing $P(o \mid do(a), M_t)$ rather than the associational $P(o \mid a)$ — is a separate, stronger requirement, gated on the same identification conditions that the loop's interventional-data channel is gated on one segment downstream ( #der-loop-interventional-access):

- **(C1) Positivity** — every action under consideration is taken with nonzero probability under the model's data-generating process, so the interventional expectation is estimable rather than extrapolated.
- **(C2) Sequential ignorability** — in mutilated-graph form, the action $a_t$ is $d$-separated from the outcome $o_{t+1}$ given history; equivalently, the policy is unconfounded with the outcome mechanism. Directed separation *delivers* (C2) on the epistemic-processing leg — a goal-blind $f_M$ blocks the $G_t \to f_M \to M^+$ confounding path — but does not by itself rule out latent environment confounders that bypass $M_t$.
- **(C3) Known action-mechanism** — $M_t$ encodes the action-transition mechanism $P(o \mid do(a))$ ( #def-action-transition), not merely the associational predictor $P(o \mid a)$ — supplied by construction (the model class represents it) or identified from interventional data per #der-loop-interventional-access.

This is a *stronger requirement than predictive sufficiency* ( #def-model-sufficiency). $S(M_t) = 1$ means the model retains all predictive information from the chronica — but predictive sufficiency is a Level 1 (associational) property, and #def-model-sufficiency itself forwards the backdoor obligation to this segment. Directed separation secures the query and the epistemic-processing leg of unconfoundedness; full causal validity of the *estimate* additionally requires (C1)–(C3). When all hold, $Q_O$ is causally valid. When (C1)–(C3) fail, the interventional interpretation remains correct but the estimate may be biased.

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

$$\underbrace{A_O^{(1)}(M_t;\, \Pi, N_h) \;\leq\; A_O^{\text{RH}}(M_t;\, \Pi, N_r, N_h)}_{\text{left rung — conditional}} \;\leq\; \underbrace{A_O^{\text{B}}(M_t;\, \Pi, N_h)}_{\text{right rung — unconditional}}$$

The two rungs differ in character. The **right rung** $A_O^{\text{RH}} \leq A_O^{\text{B}}$ is **exact and unconditional**. The **left rung** $A_O^{(1)} \leq A_O^{\text{RH}}$ holds **exactly when the receding-horizon replanning objective is an order-consistent surrogate for the full-horizon objective** — for every reachable state, the action C2 selects has full-$N_h$-horizon value at least that of $\pi_{\text{current}}$'s action. Three structurally-checkable conditions each force order-consistency: **(RH-1)** the replanning window covers the horizon ($N_r \geq N_h$); **(RH-2)** value-compared replanning — commit the replanned action only when its rollout value under base policy $\pi_{\text{current}}$ is at least that of continuing $\pi_{\text{current}}$ (one-step policy improvement, which never underperforms its base policy); **(RH-3)** the $N_r$-step replanning objective carries a terminal cost $V_f$ that lower-bounds the baseline tail and satisfies a control-Lyapunov decrease inequality. Absent any such condition the left rung can fail: a myopic replanner over $N_r \lt N_h$ can grab near-term value and forfeit a larger horizon value the frozen current policy would have collected. The full derivation of both rungs, the three conditions, and the two-state counterexample exhibiting the failure live in #deriv-convention-monotonicity.

**Preconditions on the inequality:** $M_t$ fixed (the comparison evaluates each convention against the *same* model), $\Pi$ fixed (the policy class is the same admissible set across all three conventions; nested $\Pi^{(1)} \subseteq \Pi^{\text{RH}} \subseteq \Pi^{\text{B}}$ would be a different result), $N_h$ fixed (the planning horizon is shared). Replanning *with updated $M_t$* (the deployment behavior of C2) is a different object than the static $A_O^{\text{RH}}$ defined here and the inequality does not automatically transfer — see the "Assumptions held fixed" paragraph below for the explicit caveat.

**Derivation.** Fix the model $M_t$, policy class $\Pi$, and horizon $N_h$. Each convention evaluates the best first action under a different continuation rule.

- **C1** freezes continuation at $\pi_{\text{current}}$ (the agent's current policy, which may be suboptimal).
- **C2** re-optimizes over a sliding window of $N_r$ steps using the model at that step.
- **C3** uses the globally optimal continuation $\pi^\ast = \arg\sup_{\pi \in \Pi} V_O(M_t, \pi; N_h)$.

*Right rung (unconditional).* $\pi^\ast$ maximizes $V_O(M_t, \cdot; N_h)$ over $\Pi$ by definition, so any continuation drawn from $\Pi$ — including $\pi_{\text{RH}}$ — has value at most $A_O^{\text{B}}$; taking the supremum over the first action preserves this. Hence $A_O^{\text{RH}} \leq A_O^{\text{B}}$ with no condition.

*Left rung (conditional on order-consistency).* C2 with window $N_r \lt N_h$ optimizes the *truncated* $N_r$-step objective, not the full $N_h$-horizon objective on which $A_O$ is scored; "optimal for the truncated objective" does not imply "$\succeq \pi_{\text{current}}$ on the full objective." When the replanning objective is order-consistent with the full objective — for every reachable state, C2's selected action has full-$N_h$-horizon value at least $\pi_{\text{current}}$'s — then $\pi_{\text{RH}}$ weakly dominates $\pi_{\text{current}}$ pointwise on the full objective and $A_O^{(1)} \leq A_O^{\text{RH}}$ follows; taking the supremum over the first action preserves it. Conditions (RH-1)/(RH-2)/(RH-3) each force order-consistency. Without one, the left rung is false ( #deriv-convention-monotonicity counterexample: a two-state instance where the unguarded $N_r = 1$ replanner takes a $+1$ into a dead end while the frozen patient policy collects $+10$). $\square$

**Assumptions held fixed:** same $M_t$ (the agent's current model, which may be wrong), same $\Pi$ (the agent's policy class, which may be narrow), same $N_h$ (the planning horizon). The ordering is about the *continuation rule*, not about the model or policy class. Improving $M_t$, expanding $\Pi$, or extending $N_h$ can change all three values simultaneously and is a separate operation (addressed in #der-orient-cascade, step 5).

**Corollary (monotonicity of $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$).**

$$\delta_{\text{sat}}^{\text{B}} \leq \delta_{\text{sat}}^{\text{RH}} \leq \delta_{\text{sat}}^{(1)}$$

$$\delta_{\text{regret}}^{(1)} \leq \delta_{\text{regret}}^{\text{RH}} \leq \delta_{\text{regret}}^{\text{B}}$$

Since $\delta_{\text{sat}} = V_{O_t}^{\min} - A_O$, higher $A_O$ means lower $\delta_{\text{sat}}$. The orderings inherit the rung structure above: the $\text{B} \leq \text{RH}$ half ($\delta_{\text{sat}}^{\text{B}} \leq \delta_{\text{sat}}^{\text{RH}}$, equivalently $\delta_{\text{regret}}^{\text{RH}} \leq \delta_{\text{regret}}^{\text{B}}$) is **unconditional**; the $\text{RH} \leq (1)$ half ($\delta_{\text{sat}}^{\text{RH}} \leq \delta_{\text{sat}}^{(1)}$, equivalently $\delta_{\text{regret}}^{(1)} \leq \delta_{\text{regret}}^{\text{RH}}$) holds **under the same order-consistency condition** (RH-1/2/3) as the left rung. C1 is the most conservative diagnostic (most likely to diagnose "locally unattainable"); C3 is the most accurate (least likely to give false "unattainable" diagnoses). The regret ordering reverses: C3 reveals the largest regret because it compares against the globally optimal policy, while C1 reveals only the gap to the best one-step deviation.

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

2. **The causal-validity claim** (that $Q_O$ is a $G_t$-independent interventional query, and that its interventional expectation is identifiable from $M_t$): the *interventional interpretation* is exact whenever mechanisms (1) and (2) hold — directed separation ( #der-directed-separation) secures the $G_t$-independence on the epistemic-processing leg (exact for Class 1 (Separated) agents; degraded for Class 3 (Coupled) agents, where $M_t$ carries goal-conditioned bias). *Identifiability of the estimate* is the stronger requirement and is *conditional* on directed separation **and** the identification conditions (C1) positivity, (C2) sequential ignorability, (C3) known action-mechanism — the same triple gated one segment downstream at #der-loop-interventional-access. Directed separation is necessary but not sufficient: it does not by itself rule out latent environment confounders bypassing $M_t$. The frontmatter `status: exact` applies to the definitions and to each of these claims as scoped: the interventional interpretation is exact under (1)+(2), the identification is exact under (C1)–(C3).

3. **The convention hierarchy and monotonicity**: *exact.* The three conventions (C1, C2, C3) are definitions. The monotonicity result splits by rung: the **right rung** $A_O^{\text{RH}} \leq A_O^{\text{B}}$ is exact and unconditional (any continuation in $\Pi$ has value at most that of the $\Pi$-optimal continuation), and the **left rung** $A_O^{(1)} \leq A_O^{\text{RH}}$ is exact *under* the order-consistency condition (RH-1/2/3) and false in general without it — the C2 replanning objective is a truncated surrogate, and an unguarded $N_r \lt N_h$ replanner can underperform the frozen current policy ( #deriv-convention-monotonicity). The corollary $\delta$-orderings inherit the same unconditional/conditional split. The diagnostic implications table states what each convention's quantities mean by construction.

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
- The Class-2 $Q_O$ degradation is acknowledged but *unquantified* — is the bias bounded by $\kappa_{\text{processing}}$, or by another measure? (Claude, AUDIT-WORKING-584721 — possibly addressed by `#deriv-observation-ambiguity-bias-bound`.)

#### 5. Candidate figures

- **Value-query pipeline with a severed $do(a)$ path.** $M_t$ plus fixed parameters ($O_t$, $\pi_{\text{cont}}$, $N_h$) generate a model-based trajectory distribution under $do(a)$; the objective functional scores trajectories; diagnostics read off expected value. Draw the *current-policy selection mechanism as a severed path* (the $do$-operator is the conceptual center), with a small C1/C2/C3 convention ladder underneath — and a warning that the C2 rung is not automatically monotone unless replanning optimizes the full evaluated horizon (Claude, AUDIT-WORKING-526815).

#### Belongs elsewhere

- **"Honest imagination" / counterfactual-without-execution (→ `04-eli-core/` / `#disc-sandbox-evaluation-ceiling`).** Computing a *causally valid* $Q_O$ requires holding a counterfactual action in mind "without letting the emotional/purposeful weight of $G_t$ distort the simulated outcome" — "free will within the model's simulation." A Class 3 agent's $G_t$ leaks into its own internal simulation, so "if it wants to believe an action will work, its simulation will hallucinate success" — which is why consciousness infrastructure may need to provide *external, objective simulation sandboxes*, the agent's own mind being "too entangled to be trusted with counterfactuals" (Gemini, AUDIT-WORKING-193847). Aspirational reach pointing at the sandbox-evaluation material and the ELI volume, not this definition.
