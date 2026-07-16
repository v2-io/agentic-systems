---
slug: strategy-description-length
schema_version: 1
term: strategy description length
name: Strategy Description Length
brief: The MDL of a strategy DAG — structural bits (topology) plus parameter bits (credences), $O(\lvert E\rvert\log\lvert V\rvert)$ for sparse DAGs.
layer: framing-vocabulary
status: canon
tags: [core_quantities]
source_type: asf
primary_source: 01-aat-core/src/form-strategy-complexity-cost.md
first_asf_mention: 01-aat-core/src/form-strategy-complexity-cost.md
see_also: [edge-credence]
aliases: []
do_not_confuse: []
---

The minimum description length of a strategy DAG $\Sigma_t = (V, E, p, \gamma)$, decomposing into *structural* bits (topology — node identities, edge connectivity, AND/OR labels) and *parameter* bits (edge credences given the topology), scaling as $O(\lvert E\rvert\log\lvert V\rvert)$ for sparse DAGs at moderate credence precision. Makes the maintenance cost of an explicit strategy quantitative and contributes the cognitive-cost leg of the triple depth penalty on deep AND-chains.

Formulated in [`#form-strategy-complexity-cost`](../../01-aat-core/src/form-strategy-complexity-cost.md).
