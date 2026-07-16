---
slug: default-signal-function
schema_version: 1
term: default signal function
name: Default Signal Function
brief: The gradient-attribution credit-assignment scheme satisfying directional fidelity, stated in the log-odds coordinate.
layer: framing-vocabulary
status: canon
tags: [structural_concepts]
source_type: asf
primary_source: 01-aat-core/src/disc-credit-assignment-boundary.md
first_asf_mention: 01-aat-core/src/disc-credit-assignment-boundary.md
see_also: [edge-credence, credit-assignment-boundary]
aliases: []
do_not_confuse: []
---

The framework's concrete Level-1 credit-assignment scheme: a gradient-attribution signal function satisfying *directional fidelity* (the expected update for each edge points toward the true credence), stated natively in the log-odds coordinate $\lambda_k = \log(p_k/(1-p_k))$. Persistence is robust to approximation — a sloppy but directionally correct signal function still yields bounded strategic mismatch. The theory provides the structural requirements and this default; specific implementations are engineering.

Presented in [`#disc-credit-assignment-boundary`](../../01-aat-core/src/disc-credit-assignment-boundary.md); candidate scheme in [`#hyp-edge-update-via-gain`](../../01-aat-core/src/hyp-edge-update-via-gain.md).
