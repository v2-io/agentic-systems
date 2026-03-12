---
slug: structural-change-as-parametric-limit
type: formulation
status: robust-qualitative
depends:
  - strategy-dag
  - structural-adaptation-necessity
---

# Formulation: Structural Change as Parametric Limit

In the probabilistic DAG, "structural" changes to $\Sigma_t$ are continuous operations on edge weights and node sets — not a separate mechanism. Pruning is a credence dropping below threshold; grafting is a new causal hypothesis initialized at a prior. This dissolves the sharp line between parametric update (adjusting weights) and structural change (adding/removing edges).

## Formal Expression

*[Formulation (structural-change-as-parametric-limit)]*

The six operations on $\Sigma_t$, ordered from most to least frequent:

| Operation | What changes | Trigger |
|-----------|-------------|---------|
| Reweighting | Edge credence $p_{ij}$ | New observation about the link ( #edge-update-via-gain) |
| $\gamma$ reclassification | Node combination type AND↔OR | Strong structural evidence that combination semantics changed |
| Pruning | Remove failed branch ($p_{ij} \to \approx 0$) | Credence drops below viability threshold |
| Grafting | Add new branch ($0 \to p_{ij}$) | Discovery of a new possible path (initialized at prior) |
| Objective revision | Change terminal nodes | Feasibility failure or opportunity ( #satisfaction-gap) |
| Full restructure | Replace entire $\Sigma_t$ | Catastrophic failure ( #structural-adaptation-necessity) |

A healthy agent does continuous strategic maintenance (reweight, occasionally prune and graft) and rarely reaches catastrophic restructuring. Full restructure is the strategic analog of #structural-adaptation-necessity's model-class change — the rare, expensive event when the entire representational structure must be replaced.

## Epistemic Status

*Robust qualitative.* The continuity claim (structural change as parametric limit) is a property of the probabilistic representation: in a space where edges carry real-valued credences, adding or removing an edge is a boundary event, not a discontinuity. The frequency ordering of operations is an empirical pattern, not a derived result — it's consistent with the observation that deeper changes (restructuring > pruning > reweighting) require more evidence and are more costly.

## Discussion

**Connection to TF-10's destruction-creation.** #structural-adaptation-necessity describes the rare case when the entire model class must be replaced — the agent's representational framework is fundamentally inadequate. In the strategy DAG, this corresponds to full restructure: the causal theory encoded in $\Sigma_t$ is so wrong that incremental revision (reweighting, pruning) cannot fix it. The DAG must be rebuilt from a different starting point.

The key insight is that this extreme case is the *limit* of the continuous process, not a separate mechanism. An agent that maintains healthy strategic hygiene (regular reweighting, timely pruning of failing branches, proactive grafting of alternatives) will rarely need full restructure. An agent that neglects maintenance — letting failing branches persist, ignoring negative evidence — accumulates strategic debt until catastrophic restructuring becomes unavoidable.

**Pruning and grafting thresholds.** When should the agent prune (remove an edge with very low credence) rather than just keeping it at low $p_{ij}$? The answer involves the cognitive cost of maintaining edges in $\Sigma_t$ — each edge consumes representational capacity and evaluation time. For agents with bounded representational capacity (LLMs with finite context windows), pruning is necessary to keep $\Sigma_t$ within capacity. The threshold is domain-dependent and connects to the open question of cognitive cost of $\Sigma_t$ ( #strategy-dimension Working Notes).

## Working Notes

- The timescale ordering (reweight ≫ reclassify ≫ prune/graft ≫ revise O_t ≫ full restructure) is an empirical observation that should be testable. In software development: edge reweighting ≈ updating confidence after a test passes/fails; γ reclassification ≈ realizing two tasks are both required (not alternatives); pruning ≈ abandoning an approach that isn't working; grafting ≈ discovering a new approach; objective revision ≈ changing the feature scope; full restructure ≈ starting the project over.
- Grafting (adding new edges) is qualitatively different from other operations because it requires the agent to hypothesize a causal relationship that isn't in its current $\Sigma_t$. Where do new causal hypotheses come from? From $M_t$ (the model suggests a possible path), from external sources ( #communication-gain — another agent suggests an approach), or from exploration ( #causal-information-yield — the agent discovers an unexpected effect). This is the creative step in strategic revision.
