---
slug: strategy-dag
schema_version: 1
term: strategy DAG
name: Strategy DAG
notation: "$\\Sigma_t = (V_t, E_t, p_t, \\gamma_t)$"
brief: The agent's causal plan — a directed acyclic graph whose edges carry the agent's credence that completing one step advances the next.
layer: prose-symbol
status: canon
tags: [core_quantities, structural_concepts]
source_type: asf
primary_source: 01-aat-core/src/def-strategy-dag.md
first_asf_mention: 01-aat-core/src/def-strategy-dag.md
see_also: [adaptive-system, strategic-tempo, strategy-persistence, credit-assignment-boundary, satisfaction-gap, control-regret]
aliases: []
do_not_confuse: []
---

The purposeful half of the agent's state: $\Sigma_t = (V_t, E_t, p_t, \gamma_t)$ where
$V_t$ is a set of propositional nodes, $E_t$ are directed causal edges, $p_t$ maps
each edge to a credence in $[0,1]$ (how confident the agent is that completing the
parent advances the child), and $\gamma_t$ assigns AND or OR combination semantics
to each node. The DAG structure is not a modeling convenience — acyclicity is
*derived* from temporal ordering (causes precede effects; a cycle would require a
time-index to be less than itself). The AND/OR parameterization is a parsimony-motivated
formulation choice confirmed by convergence across three independent formalism attempts.

**Status propagation** flows from leaves to the root in a single $O(|V|+|E|)$ forward pass,
producing the strategy-plan-confidence score $\hat P_\Sigma$ — the DAG's own answer to
"will this plan work?" The score is correct when the DAG is causally sufficient (no
latent common causes among nodes); when causal sufficiency fails, $\hat P_\Sigma$
systematically overestimates success (OR-dominated plans) or underestimates it
(AND-dominated plans) by an error equal to the covariance from shared causes.

Defined in [`#def-strategy-dag`](../../01-aat-core/src/def-strategy-dag.md), which
includes the Correlation Hierarchy (L0–L2) for handling correlated failures and the
formal treatment of L1 augmented DAGs.
