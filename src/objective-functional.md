---
slug: objective-functional
type: definition
status: axiomatic
depends:
  - complete-agent-state
---

# Definition: Objective Functional

The objective $O_t$ is the component of $G_t$ that specifies what the agent wants — the evaluation criterion for trajectories. Its interface to the theory is a single functional $V_{O_t}: \text{trajectories} \to \mathbb{R}$, regardless of how the objective is internally represented.

## Formal Expression

*[Definition (objective-functional)]*

The **objective** $O_t$ induces a **value functional**:

$$V_{O_t}: \text{trajectories} \to \mathbb{R}$$

$V_{O_t}(\tau)$ is a scalar measure of how well trajectory $\tau$ satisfies the objective. This is the sole interface between $O_t$ and the rest of the theory — the type-stable evaluation surface.

**Objective representations.** $O_t$ can take multiple internal forms, all unified through $V_{O_t}$:

| $O_t$ form | $V_{O_t}(\tau)$ | Example |
|---|---|---|
| Point target $r$ | $-\lVert s_T - r \rVert$ | PID setpoint |
| Target region $R$ | $\mathbb{1}[s_T \in R]$ | "reach safe state" |
| Constraint set | $-\sum_t \max(0, g_i(s_t))$ | "never violate SLA" |
| Utility $U$ | $\sum_t \gamma^t U(s_t)$ | RL reward |
| Trajectory functional $J$ | $J(\tau)$ | "migrate with zero downtime" |

The trajectory functional is the most general; the others are special cases.

## Epistemic Status

*Axiomatic.* This is a definition — it names an object and specifies its interface. The claim that $V_{O_t}: \text{trajectories} \to \mathbb{R}$ is the right interface is grounded in: any evaluation criterion must ultimately answer "how good is this trajectory?" with a scalar, because the agent must compare alternatives. The real-valued codomain follows from this comparability requirement (total ordering of alternatives).

**Scope restriction: scalar comparability.** The real-valued codomain is a genuine restriction. Agents with incommensurable objectives — where no total ordering of alternatives exists — require a vector-valued or Pareto formulation outside this definition. The restriction is standard in decision theory (von Neumann–Morgenstern) and covers most practical cases, including scalarized multi-objective problems and lexicographically ordered priorities. But organizations or AI agents with hard non-compensatory constraints (safety AND profitability as independent thresholds, not a weighted sum) are only approximately covered. This should be acknowledged wherever downstream results depend on scalar $V_{O_t}$, particularly the satisfaction gap ( #satisfaction-gap) and its single-threshold feasibility test.

## Discussion

**Filling TF-08's gap.** The existing policy objective ( #causal-information-yield) contains $\mathbb{E}[\text{value}(a) \mid M_t]$ without specifying what "value" means. $O_t$ provides the formal content: value is $V_{O_t}$ applied to expected trajectories. The #value-object segment develops the full evaluation machinery ($V_O$, $Q_O$ with horizon and continuation policy).

**$O_t$ evaluates; $\Sigma_t$ guides.** The objective says "is this trajectory satisfactory?" The strategy ( #strategy-dimension) says "which action sequence produces a satisfactory trajectory?" A chess player's objective (win) is simple; the strategy (how to win) is complex. These answer different questions and carry different kinds of information — the split is developed in #strategy-dimension.

**What $O_t$ is NOT.** $O_t$ does not encode how to achieve the objective (that's $\Sigma_t$), what the agent believes about the world (that's $M_t$), or the agent's commitment or resource state (open questions — see #strategy-dimension Working Notes). $O_t$ is purely an evaluation criterion.

## Working Notes

- Compound objectives (multiple simultaneous criteria) might be modeled as terminal AND-nodes in $\Sigma_t$, keeping $O_t$ always simple (one evaluation per terminal). Whether this works for genuinely incommensurable objectives (safety vs. speed) is open — a vector-valued $V_{O_t}$ or Pareto formulation might be needed.
- The trajectory functional is real-valued, which assumes all objectives are commensurable on a single scale. This is standard in decision theory (von Neumann–Morgenstern) but is a genuine restriction for multi-objective agents. Currently acknowledged, not resolved.
- $O_t$ can change over time — objectives evolve. The *rate* of objective revision ($\nu_O$) is typically much slower than strategy revision ($\nu_\Sigma$), which is much slower than epistemic update ($\nu_M$). This timescale separation is an empirical observation, not a derived result.
