---
slug: objective-functional
type: formulation
status: axiomatic
depends:
  - complete-agent-state
stage: deps-verified
---

# Formulation: Objective Functional

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

**Satisfaction threshold.** Many objectives carry a natural threshold $V_{O_t}^{\min}$ — the minimum trajectory value the agent treats as acceptable. Point targets, constraint sets, and threshold objectives define this directly; utility-maximizing objectives may not. When $V_{O_t}^{\min}$ exists, it enables the satisfaction gap diagnostic ( #satisfaction-gap) and the well-formedness constraint on strategy ( #strategy-dag). $V_{O_t}^{\min}$ is a parameter of the objective, not a theory output — it encodes "what counts as success" in domain terms.

## Epistemic Status

*Axiomatic, with a substantive commitment.* This is a formulation — it names an object and specifies its interface, but the real-valued codomain is a genuine restriction, not a neutral naming. The claim that $V_{O_t}: \text{trajectories} \to \mathbb{R}$ is the right interface is grounded in: any evaluation criterion must ultimately answer "how good is this trajectory?" with a scalar, because the agent must compare alternatives. The real-valued codomain follows from this comparability requirement (total ordering of alternatives).

**Scope restriction: scalar comparability.** The real-valued codomain is a genuine restriction, and it is load-bearing — the satisfaction gap ( #satisfaction-gap) and control regret ( #control-regret) require comparing scalar values to produce their diagnostic. Three arguments ground the restriction:

1. **Revealed preference.** An agent that acts has implicitly scalarized: choosing action $a$ over $a'$ imposes a total ordering at the moment of choice. The scalar $V_{O_t}$ makes this implicit scalarization explicit. An agent that truly cannot compare alternatives cannot act coherently — it is stuck, not purposeful.
2. **Approximation.** Most multi-objective problems admit scalarization (weighted sum, lexicographic ordering, constraint-satisfaction with scalar residual) that preserves the diagnostic structure. The restriction excludes only agents with genuinely incommensurable objectives *and* no priority structure over them.
3. **Timescale separation.** When objectives conflict, the conflict is typically resolved at a slower timescale than strategy revision — the agent (or its principal) chooses weights, then acts within those weights. The scalar $V_{O_t}$ captures the resolved weights at the current timescale.

Agents with hard non-compensatory constraints (safety AND profitability as independent thresholds) can be modeled via the AND-node workaround: each constraint becomes a terminal node in $\Sigma_t$ with its own scalar satisfaction test, and the AND combination enforces joint feasibility. This handles constraint satisfaction cleanly but does not resolve cross-objective tradeoffs within the feasible region.

Organizations or AI agents with true Pareto structure — where no scalarization is accepted and tradeoffs are genuinely unresolved — require a vector-valued extension. The structural results of Section II (orient cascade ordering, strategy DAG, directed separation) survive such an extension; the diagnostic results (satisfaction gap, control regret, 2×2 table) degrade from quantitative scalar magnitudes to qualitative set-theoretic tests. See `msc/spike-scalar-objective-scope.md` for the full analysis.

## Discussion

**Filling TF-08's gap.** The existing policy objective ( #ciy-unified-objective) contains $\mathbb{E}[\text{value}(a) \mid M_t]$ without specifying what "value" means. $O_t$ provides the formal content: value is $V_{O_t}$ applied to expected trajectories. The #value-object segment develops the full evaluation machinery ($V_O$, $Q_O$ with horizon and continuation policy).

**$O_t$ evaluates; $\Sigma_t$ guides.** The objective says "is this trajectory satisfactory?" The strategy ( #strategy-dimension) says "which action sequence produces a satisfactory trajectory?" A chess player's objective (win) is simple; the strategy (how to win) is complex. These answer different questions and carry different kinds of information — the split is developed in #strategy-dimension.

**What $O_t$ is NOT.** $O_t$ does not encode how to achieve the objective (that's $\Sigma_t$), what the agent believes about the world (that's $M_t$), or the agent's commitment or resource state (open questions — see #strategy-dimension Working Notes). $O_t$ is purely an evaluation criterion.

## Working Notes

- Compound objectives (multiple simultaneous criteria) might be modeled as terminal AND-nodes in $\Sigma_t$, keeping $O_t$ always simple (one evaluation per terminal). Whether this works for genuinely incommensurable objectives (safety vs. speed) is open — a vector-valued $V_{O_t}$ or Pareto formulation might be needed.
- The trajectory functional is real-valued, which assumes all objectives are commensurable on a single scale. This is standard in decision theory (von Neumann–Morgenstern) but is a genuine restriction for multi-objective agents. Currently acknowledged, not resolved.
- $O_t$ can change over time — objectives evolve. The *rate* of objective revision ($\nu_O$) is typically much slower than strategy revision ($\nu_\Sigma$), which is much slower than epistemic update ($\nu_M$). This timescale separation is an empirical observation, not a derived result.
