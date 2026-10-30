---
slug: mismatch
schema_version: 1
term: mismatch
name: Mismatch
notation: "$\\delta$"
brief: The aporia signal — gap between model prediction and observation; the innovation of estimation theory.
layer: prose-symbol
status: canon
tags: [core_quantities]
source_type: asf
primary_source: 01-aat-core/src/def-mismatch-signal.md
first_asf_mention: 01-aat-core/src/def-mismatch-signal.md
see_also: [aporia, update-gain, prolepsis, aisthesis, estimation-error]
aliases: ["mismatch signal", "innovation"]
do_not_confuse: ["estimation error (the unobserved gap to the world's conditional mean, which the persistence results bound)"]
---

The signed difference between what the model predicted and what the world delivered: $\delta_t = o_t - \hat o_t$. Substrate of the [aporia](aporia.md) phase and input to the gain-weighted update of [epistrophe](epistrophe.md). Everything subsequent in the cycle is processing this signal. Its standard name is the **innovation** (Kailath 1968). It is the [estimation error](estimation-error.md) plus channel noise; the agent observes it, its mean square cannot be driven below the channel-noise floor, and the persistence results are about the estimation error, not about it.

Defined in [`#def-mismatch-signal`](../../01-aat-core/src/def-mismatch-signal.md).
