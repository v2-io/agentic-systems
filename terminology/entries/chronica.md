---
slug: chronica
schema_version: 1
term: chronica
name: Chronica
notation: "$\\mathcal{C}_t$"
brief: The complete interaction history — the agent's non-forkable causal past.
layer: prose-symbol
status: canon
tags: [core_quantities]
source_type: asf
primary_source: 01-aat-core/src/def-chronica.md
first_asf_mention: 01-aat-core/src/def-chronica.md
see_also: [continuity, mismatch, prolepsis]
aliases: ["interaction history"]
do_not_confuse: []
---

The complete causal record of the agent's observations and actions:
$\mathcal{C}_t = (o_1, a_1, o_2, a_2, \ldots, a_{t-1}, o_t)$. Monotonically
growing, irreversible, and singular — events are added but never removed, and
the ordering reflects the physical fact that $a_{t-1}$ was selected before
$o_t$ arrived. Every model the agent ever holds must be constructed from this
sequence; everything the agent can know is downstream of $\mathcal{C}_t$. The
Greek-derived name avoids collision with $\mathcal{H}$ (Shannon entropy) in
speech and notation.

Defined in [`#def-chronica`](../../01-aat-core/src/def-chronica.md).
