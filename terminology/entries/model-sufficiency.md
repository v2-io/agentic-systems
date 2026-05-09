---
slug: model-sufficiency
schema_version: 1
term: model sufficiency
name: Model sufficiency
notation: "$S$"
brief: How well the current model captures predictive information ($S \in [0,1]$).
layer: prose-symbol
status: canon
tags: [core_quantities]
source_type: asf
primary_source: 01-aad-core/src/def-model-sufficiency.md
first_asf_mention: 01-aad-core/src/def-model-sufficiency.md
see_also: [model-class-fitness, mismatch, update-gain]
aliases: []
do_not_confuse: []
---

A normalized scalar in $[0,1]$ that quantifies how much of the available
predictive information the agent's current $M_t$ actually captures. $S = 1$ is
exact prediction; $S = 0$ is no better than chance. Bounded above by the
[model class fitness](model-class-fitness.md) $\mathcal{F}$ — even an optimal
fit within the class cannot exceed the class's expressive ceiling.

Defined in
[`#def-model-sufficiency`](../../01-aad-core/src/def-model-sufficiency.md).
