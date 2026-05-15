---
slug: prolepsis
schema_version: 1
term: prolepsis
name: Prolepsis (Πρόληψις) (anticipation)
notation: "$\\hat{o}_t$"
brief: "The model's active anticipation: $\\hat{o}_t = \\mathbb{E}[o_t \\mid M_{t-1}, a_{t-1}]$."
layer: framing-vocabulary
status: canon
tags: [cycle_phases, greek_vocabulary]
source_type: external
primary_source: "Greek philosophical vocabulary (Stoic / Epicurean: anticipatory grasp)"
first_asf_mention: 01-aat-core/src/form-agent-model.md
see_also: [aisthesis, aporia, epistrophe, praxis]
aliases: ["πρόληψις"]
do_not_confuse: []
---

The first phase of the adaptive cycle: the model emits a forecast before reality
arrives. Etymologically Greek for "anticipation" or "preconception" — what one
already grasps in advance. Formally: $\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1},
a_{t-1}]$, the expected observation conditional on the prior model and last
action.

See [`#form-agent-model`](../../01-aat-core/src/form-agent-model.md) for the
model that issues the prediction.
