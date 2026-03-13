---
slug: value-object
type: definition
status: exact
depends:
  - objective-functional
  - agent-model
---

# Definition: Value Object

The horizon- and policy-conditioned value object $V_O$ turns the abstract objective functional $V_{O_t}$ into a decision-making tool: "given what I believe, what I plan to do next, and how far I'm looking ahead, how good is this situation?"

## Formal Expression

*[Definition (value-object)]*

Given objective $O_t$, model $M_t$, policy $\pi$, and horizon $N_h$:

$$V_O(M_t, \pi; N_h) = \mathbb{E}\!\left[V_{O_t}(\tau_{t:t+N_h}) \;\middle|\; M_t,\; \pi\right]$$

**Action-value form** (for action selection):

$$Q_O(M_t, a; \pi_{\text{cont}}, N_h) = \mathbb{E}\!\left[V_{O_t}(\tau) \;\middle|\; M_t,\; a_t = a,\; a_{t+1:} \sim \pi_{\text{cont}}\right]$$

$Q_O$ answers: "if I take action $a$ now and then follow $\pi_{\text{cont}}$ afterward, what is my expected trajectory value?" This is the interventional query that connects the value object to action selection.

**Continuation convention.** All value queries are conditioned on a specific continuation policy $\pi_{\text{cont}}$ and finite horizon $N_h$. $\pi_{\text{cont}}$ is a *parameter* of the value object, not a derived quantity. ACT does not prescribe a specific solution concept. Common choices:

- $\pi_{\text{cont}} = \pi_{\text{current}}$ — **one-step improvement** (evaluate each action assuming current behavior continues afterward). Natural default for ACT: requires no fixed-point computation and aligns with incremental update philosophy ( #update-gain). Not a convergence guarantee; a practical default.
- $\pi_{\text{cont}} = \pi^\ast$ — **Bellman fixed point** (self-consistent optimal continuation). Requires solving a fixed-point equation. Standard in RL and dynamic programming.
- $\pi_{\text{cont}}$ re-optimized each step — **receding horizon / MPC**. Re-plans at each step with updated $M_t$.

The one-step improvement is the natural default because it mirrors ACT's general philosophy: update incrementally from where you are, using the best available information, without requiring global optimality.

## Epistemic Status

*Exact* under the assumption that $M_t$ supports the required conditional expectations. The value object is a mathematical definition — conditional expectations of a functional over trajectories. The definitions are precise; the *computability* of these expectations is a separate question (in practice, they are approximated via simulation, sampling, or function approximation).

## Discussion

**Extending the policy objective.** The existing policy objective ( #causal-information-yield) uses $\mathbb{E}[\text{value}(a) \mid M_t]$ without formal content for "value." With the value object, this becomes:

*[Discussion (policy-objective-extension)]*

$$\pi^*(M_t, G_t) = \arg\max_a \left[Q_O(M_t, a;\, \pi_{\text{cont}}, N_h) + \lambda(M_t, O_t, N_h) \cdot \text{CIY}(a;\, M_t)\right]$$

Note that $\lambda$ now depends on $(M_t, O_t, N_h)$, not just $M_t$. The value of exploration depends on the objective and the horizon:
- An agent with a deadline should explore less as time runs out
- An agent with a safety constraint should explore differently from a utility maximizer
- Two agents with identical $M_t$ but different objectives should price exploration differently

This extension is structurally motivated but the specific form of $\lambda(M_t, O_t, N_h)$ is not derived within ACT (same status as #causal-information-yield's treatment of $\lambda$).

**Connection to #model-sufficiency.** $V_O$ is conditioned on $M_t$, not on the true environment state $\Omega_t$. When $S(M_t) \lt 1$, the agent's value estimates are biased — it may over- or underestimate trajectory values because its model is incomplete. The satisfaction gap ( #satisfaction-gap) and control regret ( #control-regret) are defined in terms of $V_O(M_t, \cdot)$, not $V_O(\Omega_t, \cdot)$, which means they measure the agent's *believed* situation, not the true one. Improving $M_t$ (reducing $\delta_{\text{epistemic}}$) brings the agent's value estimates closer to reality.

**Horizon dependence.** $N_h$ is not merely a computational convenience — it reflects genuine uncertainty about the far future. Long horizons amplify the impact of model error (small biases in $M_t$ compound over many steps). The choice of $N_h$ trades off farsightedness against robustness to model error. An agent in a fast-changing environment ($\rho$ high) should use shorter horizons; one in a stable environment can plan further.

## Working Notes

- The continuation convention is a degree of freedom that interacts with the satisfaction gap and control regret: different $\pi_{\text{cont}}$ choices give different $A_O$ values, which changes what "best achievable" means. The theory needs to be explicit about which convention is used when these quantities are compared.
- When a specific convergence guarantee is needed (e.g., for strategy-persistence-schema), the solution concept must be stated explicitly — the one-step improvement default is not sufficient.
- For LLM agents with context turnover, $N_h$ has a natural bound: the current session. The "continuation policy" is whatever the next agent instance will do, which the current instance cannot control. This connects to #context-turnover (Section V).
