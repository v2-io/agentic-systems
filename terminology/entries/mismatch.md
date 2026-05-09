---
slug: mismatch
schema_version: 1
term: mismatch
name: Mismatch
notation: "$\\delta$"
brief: The aporia signal — gap between model prediction and observation.
layer: prose-symbol
status: canon
tags: [core_quantities]
source_type: asf
primary_source: 01-aad-core/src/def-mismatch-signal.md
first_asf_mention: 01-aad-core/src/def-mismatch-signal.md
see_also: [aporia, update-gain, prolepsis, aisthesis]
aliases: ["mismatch signal"]
do_not_confuse: []
---

The signed difference between what the model predicted and what the world
delivered: $\delta_t = o_t - \hat{o}_t$. Substrate of the [aporia](aporia.md)
phase and input to the gain-weighted update of [epistrophe](epistrophe.md).
Everything subsequent in the cycle is processing this signal.

Defined in
[`#def-mismatch-signal`](../../01-aad-core/src/def-mismatch-signal.md).
