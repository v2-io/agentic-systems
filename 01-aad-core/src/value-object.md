---
slug: value-object
type: definition
status: exact
depends:
  - objective-functional
  - agent-model
  - directed-separation
stage: deps-verified
---

# Definition: Value Object

The horizon- and policy-conditioned value object $V_O$ turns the abstract objective functional $V_{O_t}$ into a decision-making tool: "given what I believe, what I plan to do next, and how far I'm looking ahead, how good is this situation?"

## Formal Expression

*[Definition (value-object)]*

Given objective $O_t$, model $M_t$, policy $\pi$, and horizon $N_h$:

$$V_O(M_t, \pi; N_h) = \mathbb{E}\!\left[V_{O_t}(\tau_{t:t+N_h}) \;\middle\vert\; M_t,\; \pi\right]$$

**Action-value form** (for action selection):

$$Q_O(M_t, a; \pi_{\text{cont}}, N_h) = \mathbb{E}\!\left[V_{O_t}(\tau) \;\middle\vert\; M_t,\; do(a_t = a),\; a_{t+1:} \sim \pi_{\text{cont}}\right]$$

$Q_O$ answers: "if I *do* action $a$ now and then follow $\pi_{\text{cont}}$ afterward, what is my expected trajectory value?" The $do(\cdot)$ notation is explicit: this is an interventional query ( #causal-hierarchy-requirement), not conditioning on observed action choice. The agent asks about consequences of an intervention, not about correlates of a naturally occurring action.

**Causal validity of the value object.** $Q_O$ is well-defined as a conditional expectation given $M_t$, $do(a)$, and $\pi_{\text{cont}}$. Two mechanisms ensure causal validity:

1. **The do-operator handles current-action confounding.** Since $Q_O$ uses $do(a_t = a)$, the dependence of $a_t$ on the selection mechanism $\pi(M_t, G_t)$ is severed. $G_t$'s influence on action choice is irrelevant because the action is intervened upon, not conditioned on.

2. **The continuation policy is a parameter.** $\pi_{\text{cont}}$ is specified as a fixed policy, not as "whatever the agent would do given its evolving $G_t$." Future actions follow $\pi_{\text{cont}}$ regardless of $G_t$'s state or evolution.

Together, these mean $Q_O(M_t, a; \pi_{\text{cont}}, N_h)$ depends on $M_t$ alone **as a state variable** — $G_t$ enters neither through action selection (severed by $do$) nor through continuation (fixed by parameter). The objective $O_t$ enters as a fixed parameter (it determines which functional $V_{O_t}$ is applied to trajectories), the same way $\pi_{\text{cont}}$ and $N_h$ are parameters. The claim is not that $Q_O$ is independent of the objective — it is that once $O_t$, $\pi_{\text{cont}}$, and $N_h$ are fixed, the only agent state that affects the value is $M_t$. The remaining requirement: $M_t$ must support the interventional query $P(o \mid do(a), M_t)$. Under directed separation ( #directed-separation), this holds because $M_t$ updates independently of $G_t$ — there is no path from $G_t$ to outcomes that bypasses both the action channel and $M_t$. For **Class 2 agents** (where $G_t$ leaks into $M_t$ processing), the causal validity of $Q_O(M_t, a; \pi_{\text{cont}}, N_h)$ is degraded because $M_t$ itself carries goal-conditioned bias — see `msc/spike-coupled-survival-analysis.md` §3.4.

This is a *stronger requirement than predictive sufficiency* (#model-sufficiency). $S(M_t) = 1$ means the model retains all predictive information from the chronica — but predictive sufficiency is a Level 1 (associational) property. Causal validity additionally requires that no unmodeled common cause affects both the environment and the agent's epistemic processing through paths not captured in $M_t$. In practice: when $S(M_t) = 1$ and directed separation holds, $Q_O$ is causally valid. When $S(M_t) \lt 1$ or directed separation fails, the interventional interpretation is correct but the conditional estimate may be biased.

**Continuation convention.** All value queries are conditioned on a specific continuation policy $\pi_{\text{cont}}$ and finite horizon $N_h$. $\pi_{\text{cont}}$ is a *parameter* of the value object, not a derived quantity.

**Canonical default: one-step improvement.** AAD adopts $\pi_{\text{cont}} = \pi_{\text{current}}$ as the canonical continuation convention unless otherwise specified. Under this convention, each action is evaluated assuming current behavior continues afterward — no fixed-point computation, no global optimality assumption. This aligns with AAD's incremental update philosophy ( #update-gain) and makes all AAD diagnostics ($\delta_{\text{sat}}$, $\delta_{\text{regret}}$, $A_O$) comparable across analyses of the same agent over time. It is not a convergence guarantee; it is a shared evaluation frame.

### Convention Hierarchy

Three named conventions form a hierarchy of increasing diagnostic power and computational cost:

**C1: One-step improvement** (canonical default). $\pi_{\text{cont}} = \pi_{\text{current}}$.

Each action is evaluated assuming current behavior continues afterward. No fixed-point computation, no global optimality assumption. Cheapest to compute; weakest diagnostic power.

**C2: Receding-horizon** ($N_r$-step replanning). At each future step, re-optimize over a horizon of $N_r$ steps using the model available at that step.

$$\pi_{\text{RH}}(M_\tau) = \arg\max_\pi V_O(M_\tau, \pi;\, N_r) \quad \text{applied at each } \tau$$

$Q_O^{\text{RH}}(M_t, a;\, N_r, N_h) = \mathbb{E}[V_{O_t}(\tau) \mid M_t, do(a_t = a), a_{t+1:} \sim \pi_{\text{RH}}]$. Captures multi-step recovery: a goal that appears unattainable under frozen continuation may be reachable with replanning. Moderate computation ($N_r$-step optimization at each step); moderate diagnostic power.

**C3: Bellman** (self-consistent optimal). $\pi_{\text{cont}} = \pi^\ast$ where $\pi^\ast = \arg\max_\pi V_O(M_t, \pi;\, N_h)$.

The continuation IS the optimal policy — a fixed-point equation. $A_O^{\text{B}} = V_O(M_t, \pi^\ast;\, N_h)$ is the best achievable value under the model. Strongest diagnostic power; most expensive to compute (requires solving the Bellman equation or its approximation).

### Monotonicity

*[Derived (convention-monotonicity)]*

For any model $M_t$, horizon $N_h$, and policy class $\Pi$:

$$A_O^{(1)}(M_t;\, \Pi, N_h) \leq A_O^{\text{RH}}(M_t;\, \Pi, N_r, N_h) \leq A_O^{\text{B}}(M_t;\, \Pi, N_h)$$

**Derivation.** Fix the model $M_t$, policy class $\Pi$, and horizon $N_h$. Each convention evaluates the best first action under a different continuation rule, holding these fixed:

- **C1** freezes continuation at $\pi_{\text{current}}$ (the agent's current policy, which may be suboptimal).
- **C2** re-optimizes periodically: at each replanning step, the agent selects the best available first action from $\Pi$ given $M_t$ at that time. By construction, $\pi_{\text{RH}} \succeq \pi_{\text{current}}$ at each future step, because C2 optimizes where C1 holds fixed.
- **C3** uses the globally optimal continuation $\pi^\ast = \arg\sup_{\pi \in \Pi} V_O(M_t, \pi; N_h)$, which is at least as good as any replanning policy because it optimizes over the full trajectory.

A weakly better continuation yields a weakly higher expected trajectory value (the objective $V_{O_t}$ is evaluated on the same trajectory distribution, with only the continuation policy changed). The ordering of continuations ($\pi_{\text{current}} \preceq \pi_{\text{RH}} \preceq \pi^\ast$) therefore implies $A_O^{(1)} \leq A_O^{\text{RH}} \leq A_O^{\text{B}}$. Taking the supremum over the first action preserves the ordering because the supremum of a larger set is at least as large. $\square$

**Assumptions held fixed:** same $M_t$ (the agent's current model, which may be wrong), same $\Pi$ (the agent's policy class, which may be narrow), same $N_h$ (the planning horizon). The ordering is about the *continuation rule*, not about the model or policy class. Improving $M_t$, expanding $\Pi$, or extending $N_h$ can change all three values simultaneously and is a separate operation (addressed in #orient-cascade, step 5).

**Corollary (monotonicity of $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$).**

$$\delta_{\text{sat}}^{\text{B}} \leq \delta_{\text{sat}}^{\text{RH}} \leq \delta_{\text{sat}}^{(1)}$$

$$\delta_{\text{regret}}^{(1)} \leq \delta_{\text{regret}}^{\text{RH}} \leq \delta_{\text{regret}}^{\text{B}}$$

Since $\delta_{\text{sat}} = V_{O_t}^{\min} - A_O$, higher $A_O$ means lower $\delta_{\text{sat}}$. C1 is the most conservative diagnostic (most likely to diagnose "locally unattainable"); C3 is the most accurate (least likely to give false "unattainable" diagnoses). The regret ordering reverses: C3 reveals the largest regret because it compares against the globally optimal policy, while C1 reveals only the gap to the best one-step deviation.

### Diagnostic implications

| Convention | $\delta_{\text{sat}} \gt 0$ means | $\delta_{\text{regret}} \approx 0$ means |
|---|---|---|
| **C1** (one-step) | Cannot improve toward goal in one step from here | Current first action is locally near-optimal |
| **C2** (receding-horizon) | Cannot reach goal with $N_r$-step replanning | Current first action is near-optimal with replanning |
| **C3** (Bellman) | Goal is genuinely infeasible given $(M_t, \Pi, N_h)$ | Policy is globally near-optimal |

The 2×2 diagnostic table ( #control-regret) applies under all three conventions with the same structure but different inferential force. Under C1, the "capability limit" quadrant ($\delta_{\text{sat}} \gt 0$, $\delta_{\text{regret}} \approx 0$) means "locally stuck" — the agent may be globally recoverable but cannot see the recovery path. Under C3, the same quadrant means "genuinely infeasible" — no policy in $\Pi$ can achieve the goal. The cascade's inferential force scales with the convention.

**AAD adopts C1 as the canonical default** for three reasons: (1) it requires no fixed-point computation, consistent with the incremental update philosophy ( #update-gain); (2) it makes all AAD diagnostics comparable across analyses of the same agent; (3) it is the most conservative, meaning false "feasible" diagnoses are minimized. Analyses that require stronger diagnostic power should state the convention explicitly. For deployed decision-making systems where "locally stuck but globally recoverable" situations are common, C2 is recommended.

Different continuation conventions yield different values for $A_O$, $\delta_{\text{sat}}$, and $\delta_{\text{regret}}$. Diagnostics computed under different conventions are not directly comparable — the convention is part of the measurement, not just the computation. When a specific convergence guarantee is needed (e.g., for #strategy-persistence-schema), the solution concept must be stated explicitly; the one-step improvement default does not provide convergence guarantees.

## Epistemic Status

The segment contains three distinct epistemic layers:

1. **The definitions** ($V_O$, $Q_O$ as conditional expectations): *exact.* These are mathematical definitions — conditional expectations of a functional over trajectories. The definitions are precise; the *computability* of these expectations is a separate question.

2. **The causal-validity claim** (that $Q_O$ depends on $M_t$ alone as a state variable): *conditional* on directed separation ( #directed-separation). For Class 1 (modular) agents, this is exact. For Class 2 (fully merged) agents, $M_t$ carries goal-conditioned bias and the causal validity degrades. The frontmatter `status: exact` applies to the definitions; the causal-validity argument is conditional on the architectural scope restriction.

3. **The convention hierarchy and monotonicity**: *exact.* The three conventions (C1, C2, C3) are definitions. The monotonicity result ($A_O^{(1)} \leq A_O^{\text{RH}} \leq A_O^{\text{B}}$) is a direct consequence of "better continuation policy yields higher expected value" — the ordering is forced by the definition of optimality. The diagnostic implications table states what each convention's quantities mean by construction.

## Discussion

**Extending the policy objective.** The existing policy objective ( #ciy-unified-objective) uses $\mathbb{E}[\text{value}(a) \mid M_t]$ without formal content for "value." With the value object, this becomes:

*[Discussion (policy-objective-extension)]*

$$\pi^*(M_t, G_t) = \arg\max_a \left[Q_O(M_t, a;\, \pi_{\text{cont}}, N_h) + \lambda(M_t, O_t, N_h) \cdot \text{CIY}(a;\, M_t)\right]$$

Note that $\lambda$ now depends on $(M_t, O_t, N_h)$, not just $M_t$. The value of exploration depends on the objective and the horizon:
- An agent with a deadline should explore less as time runs out
- An agent with a safety constraint should explore differently from a utility maximizer
- Two agents with identical $M_t$ but different objectives should price exploration differently

This extension is structurally motivated but the specific form of $\lambda(M_t, O_t, N_h)$ is not derived within AAD (same status as #ciy-unified-objective's treatment of $\lambda$).

**Connection to #model-sufficiency.** $V_O$ is conditioned on $M_t$, not on the true environment state $\Omega_t$. When $S(M_t) \lt 1$, the agent's value estimates are biased — it may over- or underestimate trajectory values because its model is incomplete. The satisfaction gap ( #satisfaction-gap) and control regret ( #control-regret) are defined in terms of $V_O(M_t, \cdot)$, not $V_O(\Omega_t, \cdot)$, which means they measure the agent's *believed* situation, not the true one. Improving $M_t$ (reducing $\delta_{\text{epistemic}}$) brings the agent's value estimates closer to reality.

**Horizon dependence.** $N_h$ is not merely a computational convenience — it reflects genuine uncertainty about the far future. Long horizons amplify the impact of model error (small biases in $M_t$ compound over many steps). The choice of $N_h$ trades off farsightedness against robustness to model error. An agent in a fast-changing environment ($\rho$ high) should use shorter horizons; one in a stable environment can plan further.

## Working Notes

- The one-step improvement convention is now the canonical default (promoted from Working Notes to Formal Expression). This resolves the comparability issue: $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$ are comparable across analyses when computed under the same convention.
- When a specific convergence guarantee is needed (e.g., for strategy-persistence-schema), the solution concept must be stated explicitly — the one-step improvement default is not sufficient.
- For LLM agents with context turnover, $N_h$ has a natural bound: the current session. The "continuation policy" is whatever the next agent instance will do, which the current instance cannot control. This connects to #context-turnover (Section V).
