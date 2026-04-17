---
slug: strategy-dimension
type: definition
status: axiomatic
depends:
  - complete-agent-state
  - objective-functional
stage: deps-verified
---

# Definition: Strategy Dimension

The purposeful substate $G_t$ decomposes into two structurally distinct components: $O_t$ (the objective — what the agent wants) and $\Sigma_t$ (the strategy — the agent's theory of how its actions produce progress toward $O_t$). These carry different kinds of information answering different questions.

## Formal Expression

*[Definition (strategy-dimension)]*

$$G_t = (O_t, \Sigma_t)$$

where:
- $O_t$: **evaluation** — "Is this trajectory satisfactory?" ( #objective-functional)
- $\Sigma_t$: **guidance** — "Which action sequence produces a satisfactory trajectory?"

The split is **definitional** — it reflects a structural difference in the information, not a dynamic or timescale claim. $O_t$ and $\Sigma_t$ are different *kinds* of state answering different questions:

| | $O_t$ (objective) | $\Sigma_t$ (strategy) |
|---|---|---|
| **Question** | How good is this trajectory? | How do I produce a good trajectory? |
| **Type** | $V_{O_t}: \text{trajectories} \to \mathbb{R}$ | Structured representation (see below) |
| **Richness varies** | Point target → utility → trajectory functional | Reactive → cached → subgoals → causal DAG |
| **Update source** | External (assigned, discovered, revised) | Internal (deliberation, evidence, cascade) |

**Strategy representations**, ordered by expressiveness:

| $\Sigma_t$ form | What it encodes | Example |
|---|---|---|
| None (reactive) | No explicit strategy; policy implicit in $M_t$ | Thermostat, reflex |
| Cached policy | Learned mapping $s \to a$ | Trained RL policy |
| Subgoal sequence | Waypoints with ordering | Navigation, recipe |
| Causal DAG | Action-outcome chains with AND/OR structure and confidence weights | Military plan, software project |

## Epistemic Status

*Axiomatic.* This is a definition — it names a structural distinction that exists in the information. The distinction between "what makes a trajectory good" (evaluation) and "how to produce a good trajectory" (guidance) is a categorical difference, not a quantitative one. The claim is NOT that all agents maintain both explicitly — reactive agents have $\Sigma_t = \emptyset$, and that's fine. The claim is that when an agent does maintain purposeful state, it decomposes along this line.

The two dimensions vary independently: a chess player has a simple $O_t$ (win) and a complex $\Sigma_t$ (opening theory, tactical patterns, endgame knowledge). A multi-objective optimizer may have a complex $O_t$ (Pareto frontier) and a simple $\Sigma_t$ (gradient descent). This independence is why the split matters — conflating them in a single hierarchy obscures the fact that objective richness and strategic richness are separate design axes.

## Discussion

**When richer $\Sigma_t$ is needed.** A reactive agent ($\Sigma_t = \emptyset$) suffices when greedy optimization on $Q_O$ ( #value-object) works — when the action-to-value mapping is approximately convex and single-step. When the environment has non-convex landscapes, prerequisite structure, or multi-step causal chains, greedy optimization fails and the agent needs explicit strategy. The trigger is the purposeful analog of #structural-adaptation-necessity: inadequacy of the current $\Sigma_t$ representation for the environment's causal complexity.

**$O_t$ and $\Sigma_t$ have different update dynamics.** Objectives change slowly: an organization's mission, a developer's feature goal, a commander's campaign objective. Strategies change faster: adjust the plan when step 3 fails, redirect resources, try an alternative path. Epistemic state changes fastest: each observation updates $M_t$. This timescale ordering ($\nu_M \gg \nu_\Sigma \gg \nu_O$) is an empirical observation, not a derived result. It holds for many agent populations but is not universal — an agent discovering its goal is infeasible may revise $O_t$ faster than $\Sigma_t$.

**The decomposition resolves a type error.** Earlier formulations used $\delta_{\text{goal}} = G_t - M_t$ as a goal mismatch signal. When $\Sigma_t$ is a DAG, this is a type error — you cannot subtract a graph from a state vector. The #satisfaction-gap and #control-regret replace this with properly typed gap measures.

## Working Notes

- The independence of $O_t$ and $\Sigma_t$ richness has a practical consequence for agent design: you can upgrade the strategy engine (from reactive to DAG-based planning) without changing the objective representation, and vice versa. This is a desirable architectural property, not just an analytical convenience.
- **Cognitive cost of $\Sigma_t$**: maintaining a 500-node DAG is qualitatively different from maintaining a 12-node one. The IB framework ( #information-bottleneck) applies to strategy as well as to models — the agent must compress its strategy to fit in working memory. For finite-context agents (LLMs), this is concrete: the DAG must fit in the context window. No formal analog of $\beta$ (compression cost) exists yet for strategy; this is an open question.
- **Commitment state** (from intent-dag-consolidated DP-3): the formalism doesn't distinguish "considering" from "executing." OR branches in $\Sigma_t$ are options until something commits resources. A $D_t$ (desire) / $I_t$ (committed intent) split may become load-bearing in multi-agent settings (shared desire vs. shared commitment). Open for Section III.
- **Resource budget**: strategy evaluation requires knowing what paths cost, but costs are currently unmodeled. For agents with negligible action cost (LLM API calls), this is adequate. For resource-constrained agents (military units, development teams), per-action costs and capacity constraints would need to enter the formalism. Open.
