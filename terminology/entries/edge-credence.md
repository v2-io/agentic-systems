---
slug: edge-credence
schema_version: 1
term: edge credence
name: Edge Credence
brief: The per-edge confidence weight $p_{ij}$ on a strategy-DAG edge — the agent's working causal belief in the link.
layer: prose-symbol
status: canon
notation: "$p_{ij}$"
tags: [core_quantities, structural_concepts]
source_type: asf
primary_source: 01-aat-core/src/def-strategy-dag.md
first_asf_mention: 01-aat-core/src/def-strategy-dag.md
see_also: [purposeful-substate]
aliases: []
do_not_confuse: []
---

The single-parameter confidence weight $p_{ij}$ carried by each edge of the strategy DAG: the agent's working causal belief that the parent's success facilitates the child's. Edge credences are updated via the uncertainty ratio (natively in the log-odds coordinate, the unique additive-evidence coordinate), inherit the identification strength of the data regime feeding them, and their near-zero tail is the DAG's latent structure.

Defined in [`#def-strategy-dag`](../../01-aat-core/src/def-strategy-dag.md); dynamics in [`#deriv-edge-credence-dynamics`](../../01-aat-core/src/deriv-edge-credence-dynamics.md).
