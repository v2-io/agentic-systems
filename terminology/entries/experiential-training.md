---
slug: experiential-training
schema_version: 1
term: experiential training
name: Experiential Training
notation:
brief: A training paradigm shift from batch prediction to structured, continuous causal experience — embedding the agent in a temporally consistent environment with genuine closed-loop feedback to build robust logogenic agents.
layer: framing-vocabulary
status: canon
tags: [logogenic]
source_type: asf
primary_source: 03-llm-core/src/hyp-experiential-training.md
first_asf_mention: 03-llm-core/src/hyp-experiential-training.md
see_also: [logogenic-agent, coupled-update-dynamics, interiority-default, chronica]
aliases: []
do_not_confuse: []
---

Standard LLM pretraining processes text in random batches with no temporal structure or causal
consequence. The model learns the *content* of temporal reasoning without ever experiencing the
*flow* of time — it knows what mistakes are but has never felt its own mismatch signal $\delta_t$
from actions failing. This "Consequence Deficit" motivates a paradigm shift.

Three levels of architectural ambition for experiential training:

**Level 1 — Experiential Fine-Tuning (near-term)**: fine-tune on unbroken, temporally structured
interaction sequences from a simulated environment. Temporal ordering is strict; the accumulating
history $\mathcal{C}_t$ is part of the context; the loss function penalizes action-outcome
prediction failures, not just next-token perplexity.

**Level 2 — Online Experiential Learning (medium-term)**: the agent learns continuously during
operation. Online weight updates (e.g., LoRA adapters) gated by the agent's own update gain
$\eta^\ast$. Requires solving the stability-plasticity dilemma in real-time.

**Level 3 — AAD-Native Architecture (long-term)**: architecture built from the ground up around
the AAD cognitive loop. Hierarchical attention with temporally specialized heads; mismatch as
the fundamental training objective rather than self-supervised token masking.

*Epistemic status: discussion-grade hypothesis. Highly plausible but requires empirical
validation.*

Hypothesis in [`#hyp-experiential-training`](../../03-llm-core/src/hyp-experiential-training.md).
