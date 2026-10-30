---
slug: estimation-error
schema_version: 1
term: estimation error
name: Estimation Error
notation: "$\\bar\\delta$"
brief: The gap between the model's prediction and the mean the world would deliver given its state and law — the object the persistence results bound; unobserved by the agent.
layer: prose-symbol
status: canon
tags: [core_quantities]
source_type: standard
primary_source: 01-aat-core/src/def-mismatch-signal.md
first_asf_mention: 01-aat-core/src/def-mismatch-signal.md
see_also: [mismatch, structural-persistence, persistence-cost]
aliases: ["tracking error"]
do_not_confuse: ["innovation (the observed mismatch signal, which adds channel noise)"]
---

$\bar\delta_t = \bar o_t - \hat o_t$, with $\bar o_t = \mathbb E[o_t \mid S_t, a_{t-1}]$; in a state-space model $\bar\delta_t = H e_t$ with $e_t = x_t - \hat x_t$. The observed [mismatch](mismatch.md) (the innovation) is the estimation error plus channel noise, $\delta_t = \bar\delta_t + (o_t - \bar o_t)$. The mismatch dynamics, the sector condition and the persistence results have the estimation error as their state; their disturbance includes the channel noise the correction feeds back, which is why the error is smallest at the optimal gain, not the largest. Standard name in estimation theory (Kalman filtering; Kailath 1968).

Defined in [`#def-mismatch-signal`](../../01-aat-core/src/def-mismatch-signal.md).
