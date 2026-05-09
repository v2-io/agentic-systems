---
slug: strategy-plan-confidence
schema_version: 1
term: strategy-plan confidence
name: Strategy-plan confidence
notation: $\hat{P}_\Sigma$
brief: The DAG's own answer to "will this plan work?" — root-node-propagated probability score from the agent's strategy DAG.
layer: prose-symbol
status: canon
tags: [core_quantities, diagnostic]
source_type: asf
primary_source: 01-aad-core/src/def-strategy-dag.md
first_asf_mention: 01-aad-core/src/def-strategy-dag.md
see_also: [strategy-dag, satisfaction-gap, control-regret]
aliases: ["plan confidence (in-segment shorthand once introduced)"]
do_not_confuse:
  - "plan confidence (bare; generic project-management / RL term used widely)"
internal_note: F1 batch citability fix (2026-05-04). Bare 'plan confidence' is generic across project management, military planning, RL value-function literature. The 'strategy-plan' qualifier anchors the strategy-DAG context. Symbol $\hat{P}_\Sigma$ stays unchanged; this entry binds the symbol-prose pair in NOTATION.md as well.
---

The strategy DAG's root-node-propagated probability score $\hat{P}_\Sigma(M_t) = s_{v_\text{root}}$ — the agent's own answer to "will this plan work?". Computed by AND/OR status-propagation from per-edge causal-efficacy estimates $p_{ij}$ up to the root.

A correct probability only when the DAG is **causally sufficient** — when all common causes of strategy nodes are represented as nodes in the graph (per [`#deriv-graph-structure-uniqueness`](../../01-aad-core/src/deriv-graph-structure-uniqueness.md), Step 3, via the Causal Markov Condition theorem). When the DAG is causally insufficient (the dominant real-world case — shared infrastructure, common-mode risks, correlated adversary actions introduce latent common causes), $\hat{P}_\Sigma$ systematically overestimates success likelihood because the AND/OR propagation treats joint failure probability as the product of marginals.

The **strategy-plan-confidence error** $\delta_s = \hat{P}_\Sigma - \Phi$ is the load-bearing diagnostic at the plan level: $\Phi$ is the AND/OR formula at true edge rates, $\hat{P}_\Sigma$ is the agent's current estimate. Persistence of $\delta_s$ is proved (Prop B.5 in [`#deriv-edge-credence-dynamics`](../../01-aad-core/src/deriv-edge-credence-dynamics.md)). Note: $\delta_s$ tracks calibration *within* the L0 independence model; gap to actual plan success under correlated failure is a model-class limitation, not estimation error.

Defined in [`#def-strategy-dag`](../../01-aad-core/src/def-strategy-dag.md). Symbol-prose pair $\hat{P}_\Sigma$ ↔ "strategy-plan confidence" canonically binds.
