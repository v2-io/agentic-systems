---
slug: explicit-strategy-condition
type: normative
status: conditional
depends:
  - temporal-optimality
  - strategy-dimension
  - causal-hierarchy-requirement
---

# Normative: Explicit Strategy Condition

An agent benefits from maintaining an explicit strategy $\Sigma_t$ when the cost of planning is less than the cost of learning through exploration alone. This is a normative design criterion — it tells you when explicit strategy is *worth it*, not that it's always necessary.

## Formal Expression

*[Normative (explicit-strategy-condition, via temporal-optimality)]*

An agent benefits from explicit $\Sigma_t$ when:

$$C_{\text{plan}} + C_{\text{maintain}} \lt C_{\text{explore}} + C_{\text{repair}}$$

where:
- $C_{\text{plan}}$: cost of constructing and evaluating the strategy (deliberation, simulation, model queries)
- $C_{\text{maintain}}$: ongoing cost of keeping $\Sigma_t$ current as $M_t$ evolves (edge revision, structural updates)
- $C_{\text{explore}}$: cost of learning action-outcome mappings through direct interaction (real actions, real time, real consequences)
- $C_{\text{repair}}$: cost of correcting errors discovered only through execution (rollbacks, rework, damage)

All costs are measured in time ( #temporal-optimality) under the precondition that the two approaches produce approximately equivalent non-temporal outcomes.

## Epistemic Status

*Normative, not derived.* This is labeled *normative* because #temporal-optimality requires identical non-temporal outcomes as a precondition — "given equivalent outcomes, prefer the faster approach." In practice, loop-based and model-based approaches may differ in:

- **Final value**: the model introduces bias; exploration may discover things planning cannot
- **Risk profile**: exploration risks real damage; planning risks wrong models
- **Reversibility**: some exploratory actions are irreversible
- **Model bias**: explicit $\Sigma_t$ inherits the biases of $M_t$; loop-based learning does not

The inequality is correct *when* the outcomes are approximately equivalent — a condition that must be verified case by case, not assumed. When the precondition fails (model-based and loop-based approaches produce qualitatively different outcomes), the cost inequality is insufficient and the choice requires richer analysis (e.g., expected regret including model error).

## Discussion

**When the inequality strongly favors planning.** The right side ($C_{\text{explore}} + C_{\text{repair}}$) is large when:
- Actions are expensive or irreversible (production deployments, military operations, surgical procedures)
- Exploration damage is severe (a wrong move in chess loses the game; a wrong deployment takes down the service)
- The environment is slow to respond (waiting for market feedback, waiting for test results)
- The action space is enormous (combinatorial planning problems)

In these domains, explicit $\Sigma_t$ is strongly motivated even if the planning model is imperfect.

**When the inequality favors pure exploration.** The left side ($C_{\text{plan}} + C_{\text{maintain}}$) is large when:
- The environment is too complex or novel for useful models (genuinely unknown territory)
- $M_t$ is severely inadequate (model predictions are worse than random)
- The environment changes faster than $\Sigma_t$ can be maintained ($\rho_\Sigma$ exceeds planning capacity)
- Actions are cheap and reversible (A/B testing, sandbox exploration)

**This makes #temporal-optimality load-bearing.** The postulate provides the normative grounding: among approaches producing equivalent outcomes, prefer the one requiring less time. The cost inequality instantiates this for the planning-vs-exploration choice. Without #temporal-optimality, the inequality would be an engineering heuristic without theoretical grounding.

**Connection to the three-way tradeoff.** For actuated agents, the binary explore/exploit tradeoff extends to three modes: exploit (pursue $O_t$ via $\Sigma_t$), explore (improve $M_t$), and deliberate (revise $\Sigma_t$). The cost inequality addresses the coarsest question (is explicit $\Sigma_t$ worth having?). The finer question of how to allocate between the three modes at each time step is open — it connects to #causal-information-yield's exploration price $\lambda$ extended with $\Sigma_t$ revision costs.

## Working Notes

- The inequality as stated is static — it compares cumulative costs. A dynamic version would ask: "given current $M_t$ quality, is it worth deliberating further or should I act now?" This connects to #deliberation-cost's threshold: deliberation is worthwhile only when additional deliberation improves action quality enough to justify the time spent.
- Part of $C_{\text{maintain}}$ is the cognitive cost of keeping $\Sigma_t$ in the agent's representational capacity. For LLM agents, this means fitting the strategy in the context window. A 500-node DAG may exceed this capacity, making the left side of the inequality large enough that simpler strategies (or pure exploration) become preferable despite higher exploration costs.
- The cost inequality may be most useful not as a binary decision rule but as a way to calibrate $\Sigma_t$ complexity: the agent should maintain a strategy just complex enough that $C_{\text{plan}} + C_{\text{maintain}}$ stays below $C_{\text{explore}} + C_{\text{repair}}$ for the current environment. This gives a principled answer to "how detailed should my plan be?"
