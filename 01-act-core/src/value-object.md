---
slug: value-object
type: definition
status: exact
depends:
  - objective-functional
  - agent-model
stage: draft
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

**Causal validity of the value object.** Computing $Q_O$ from $M_t$ requires that the model supports interventional queries — that $P(o \mid do(a), M_t) = P(o \mid a, M_t)$ (the conditional, given $M_t$, equals the interventional). This holds when $M_t$ satisfies the backdoor criterion with respect to the agent's own actions: since $a_t = \pi(M_t, G_t)$, the agent's action is a deterministic function of $M_t$ (and $G_t$), so conditioning on $M_t$ blocks confounding paths between action selection and outcomes — provided that no unmodeled common cause affects both the action mechanism and the outcome independently of $M_t$.

This is a *stronger requirement than predictive sufficiency* (#model-sufficiency). $S(M_t) = 1$ means the model retains all predictive information from the chronica — but predictive sufficiency is a Level 1 (associational) property. It does not automatically confer Level 2 (interventional) validity, because the agent's environment may contain confounders that correlate actions and outcomes through paths not mediated by $M_t$. In practice: when $S(M_t) = 1$ *and* the agent's action is selected solely from $M_t$ (no unmodeled external influences on action selection), the backdoor criterion is satisfied and $Q_O$ is causally valid. When $S(M_t) \lt 1$, the interventional interpretation is the correct one but the conditional estimate may be biased by unmodeled confounders. When there are unmodeled influences on the action-selection mechanism itself (e.g., hardware failures, external overrides), even $S(M_t) = 1$ is insufficient — the backdoor criterion requires conditioning on all common causes of action and outcome.

**Continuation convention.** All value queries are conditioned on a specific continuation policy $\pi_{\text{cont}}$ and finite horizon $N_h$. $\pi_{\text{cont}}$ is a *parameter* of the value object, not a derived quantity.

**Canonical default: one-step improvement.** ACT adopts $\pi_{\text{cont}} = \pi_{\text{current}}$ as the canonical continuation convention unless otherwise specified. Under this convention, each action is evaluated assuming current behavior continues afterward — no fixed-point computation, no global optimality assumption. This aligns with ACT's incremental update philosophy ( #update-gain) and makes all ACT diagnostics ($\delta_{\text{sat}}$, $\delta_{\text{regret}}$, $A_O$) comparable across analyses of the same agent over time. It is not a convergence guarantee; it is a shared evaluation frame.

**Alternative conventions** are legitimate but must be stated explicitly when used:

- $\pi_{\text{cont}} = \pi^\ast$ — **Bellman fixed point** (self-consistent optimal continuation). Requires solving a fixed-point equation. Standard in RL and dynamic programming.
- $\pi_{\text{cont}}$ re-optimized each step — **receding horizon / MPC**. Re-plans at each step with updated $M_t$.

Different continuation conventions yield different values for $A_O$, $\delta_{\text{sat}}$, and $\delta_{\text{regret}}$. Diagnostics computed under different conventions are not directly comparable — the convention is part of the measurement, not just the computation. When a specific convergence guarantee is needed (e.g., for #strategy-persistence-schema), the solution concept must be stated explicitly; the one-step improvement default does not provide convergence guarantees.

## Epistemic Status

*Exact* under the assumption that $M_t$ supports the required conditional expectations. The value object is a mathematical definition — conditional expectations of a functional over trajectories. The definitions are precise; the *computability* of these expectations is a separate question (in practice, they are approximated via simulation, sampling, or function approximation).

## Discussion

**Extending the policy objective.** The existing policy objective ( #ciy-unified-objective) uses $\mathbb{E}[\text{value}(a) \mid M_t]$ without formal content for "value." With the value object, this becomes:

*[Discussion (policy-objective-extension)]*

$$\pi^*(M_t, G_t) = \arg\max_a \left[Q_O(M_t, a;\, \pi_{\text{cont}}, N_h) + \lambda(M_t, O_t, N_h) \cdot \text{CIY}(a;\, M_t)\right]$$

Note that $\lambda$ now depends on $(M_t, O_t, N_h)$, not just $M_t$. The value of exploration depends on the objective and the horizon:
- An agent with a deadline should explore less as time runs out
- An agent with a safety constraint should explore differently from a utility maximizer
- Two agents with identical $M_t$ but different objectives should price exploration differently

This extension is structurally motivated but the specific form of $\lambda(M_t, O_t, N_h)$ is not derived within ACT (same status as #ciy-unified-objective's treatment of $\lambda$).

**Connection to #model-sufficiency.** $V_O$ is conditioned on $M_t$, not on the true environment state $\Omega_t$. When $S(M_t) \lt 1$, the agent's value estimates are biased — it may over- or underestimate trajectory values because its model is incomplete. The satisfaction gap ( #satisfaction-gap) and control regret ( #control-regret) are defined in terms of $V_O(M_t, \cdot)$, not $V_O(\Omega_t, \cdot)$, which means they measure the agent's *believed* situation, not the true one. Improving $M_t$ (reducing $\delta_{\text{epistemic}}$) brings the agent's value estimates closer to reality.

**Horizon dependence.** $N_h$ is not merely a computational convenience — it reflects genuine uncertainty about the far future. Long horizons amplify the impact of model error (small biases in $M_t$ compound over many steps). The choice of $N_h$ trades off farsightedness against robustness to model error. An agent in a fast-changing environment ($\rho$ high) should use shorter horizons; one in a stable environment can plan further.

## Working Notes

- The one-step improvement convention is now the canonical default (promoted from Working Notes to Formal Expression). This resolves the comparability issue: $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$ are comparable across analyses when computed under the same convention.
- When a specific convergence guarantee is needed (e.g., for strategy-persistence-schema), the solution concept must be stated explicitly — the one-step improvement default is not sufficient.
- For LLM agents with context turnover, $N_h$ has a natural bound: the current session. The "continuation policy" is whatever the next agent instance will do, which the current instance cannot control. This connects to #context-turnover (Section V).
