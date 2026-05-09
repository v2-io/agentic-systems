---
slug: model-class-fitness
schema_version: 1
term: model class fitness
name: Model class fitness
notation: "$\\mathcal{F}$"
brief: Best achievable sufficiency within the model class ($\mathcal{F} \in [0,1]$).
layer: prose-symbol
status: canon
tags: [core_quantities]
source_type: asf
primary_source: 01-aad-core/src/def-model-class-fitness.md
first_asf_mention: 01-aad-core/src/def-model-class-fitness.md
see_also: [model-sufficiency, structural-adaptation]
aliases: []
do_not_confuse: []
---

The supremum of achievable [model sufficiency](model-sufficiency.md) over all
parameterizations within the current model class. $\mathcal{F} < 1$ signals a
class-expressivity ceiling — no amount of parameter learning can do better
without [structural adaptation](structural-adaptation.md) (changing the class).

Defined in
[`#def-model-class-fitness`](../../01-aad-core/src/def-model-class-fitness.md).
