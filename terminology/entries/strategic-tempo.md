---
slug: strategic-tempo
schema_version: 1
term: strategic tempo
name: Strategic Tempo
notation: "$\\mathcal T_\\Sigma$"
brief: The effective rate at which an agent revises its strategy — the sum of per-edge correction capacities weighted by causal identifiability.
layer: prose-symbol
status: canon
tags: [core_quantities, structural_concepts]
source_type: asf
primary_source: 01-aat-core/src/def-strategic-tempo.md
first_asf_mention: 01-aat-core/src/def-strategic-tempo.md
see_also: [strategy-dag, adaptive-tempo, adaptive-reserve, adversarial-destabilization, strategy-persistence]
aliases: []
do_not_confuse: [adaptive-tempo, tempo]
---

The purposeful-side analog of adaptive tempo $\mathcal{T}$: the rate at which an agent acquires useful revisions to its strategy DAG $\Sigma_t$. Defined as the sum of per-edge observation rates $\nu_{ij}$, scaled by per-edge update gain $\eta_{\text{edge},ij}$ and identifiability coefficient $\iota_{ij} \in [0,1]$:

$$\mathcal{T}_\Sigma = \sum_{(i,j) \in E} \nu_{ij} \cdot \eta_{\text{edge},ij} \cdot \iota_{ij}$$

The $\iota_{ij}$ factor (from edge causal identifiability) is the key distinction from epistemic tempo: Regime A edges (genuine interventions, $\iota \approx 1$) contribute fully; Regime C edges (observation-only, $\iota \approx 0$) contribute essentially nothing.
An agent *cannot improve the parts of its strategy that it cannot test interventionally*.

AND-chains cause **depth-gated attenuation**: downstream edge rates decay geometrically with depth as each edge is tested only when all upstream edges succeed. OR-nodes cause
**exploration-gated allocation**: non-greedy arms are tested at a rate proportional to the exploration fraction. Both patterns produce the same lesson — aggregate $\mathcal T_\Sigma$
overstates effective strategic adaptation when correction capacity is heterogeneous across edges. The persistence condition is bottleneck-limited by the weakest edge.

Defined in [`#def-strategic-tempo`](../../01-aat-core/src/def-strategic-tempo.md).
