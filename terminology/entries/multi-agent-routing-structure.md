---
slug: multi-agent-routing-structure
schema_version: 1
term: multi-agent routing structure
name: Multi-agent routing structure
notation: $R_t$
brief: Multi-agent communication infrastructure — topology $\mathcal N_t$ + protocol $c_t^{(j \to i)}$; the *routing*, not the *content*.
layer: prose-symbol
status: canon
tags: [composition, structural_concepts]
source_type: asf
primary_source: 01-aat-core/src/scope-multi-agent.md
first_asf_mention: 01-aat-core/src/scope-multi-agent.md
see_also: [communication-gain, unity-dimensions, composition-threshold, directed-separation]
aliases: ["routing structure"]
do_not_confuse:
  - "network routing (computer-networking term — packet forwarding, routing tables)"
internal_note: F1 batch citability fix (2026-05-04). Bare 'routing structure' is sanctioned in-segment shorthand after first compound-form introduction; cross-segment citation should use the full 'multi-agent routing structure' form.
---

The communication infrastructure of a multi-agent composite: who talks to whom (topology $\mathcal N_t$) and under what protocol ($c_t^{(j \to i)}$). The routing-vs-content distinction is load-bearing — the routing structure governs the *infrastructure* (which channels exist, what kind of information they carry), not the specific content of individual messages (which reflects each sender's state through their policy).

The **goal-blind routing** condition $\mathcal N_t \perp G_t^c$ and $c_t^{(j \to i)} \perp G_t^c$ is the structural condition that preserves directed separation at the composite level (per [`#hyp-directed-separation-under-composition`](../../01-aat-core/src/hyp-directed-separation-under-composition.md)). Goal-dependent routing — activating crisis channels, changing intelligence-sharing protocols based on mission, reassigning reporting chains based on objective — breaks composite directed separation.

Defined in [`#scope-multi-agent`](../../01-aat-core/src/scope-multi-agent.md).
