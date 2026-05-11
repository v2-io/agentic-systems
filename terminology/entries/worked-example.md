---
slug: worked-example
schema_version: 1
term: worked example
name: Worked Example
brief: "A segment type: end-to-end domain instantiation validating the theory chain in a concrete case."
layer: framing-vocabulary
status: canon
tags: [segment_types]
seq: 16
subgroup: Structural and Discursive
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [observation, measurement, result]
aliases: []
do_not_confuse: [observation, measurement]
---

A `type: worked-example` segment walks through a complete instantiation of the theory in a
concrete domain — e.g., the bandit problem, Kalman filtering, L1 regularization — showing how the
abstract framework maps onto real quantities in a real setting. The example validates that the
theory chain is coherent in the particular domain, catching errors that purely formal arguments
might miss.

Worked examples typically do not carry a `## Findings` section — their contribution is pedagogical
and validating rather than novel. They are the content that exhausts itself in demonstrating their
parent result's instantiation. (FORMAT.md notes: "worked examples whose content is exhausted by
the parent result they instantiate all typically lack a Findings section.")

Named examples use paired vocabulary: a worked example's slug takes the form `#example-{domain}`
(e.g., `#example-bandit`, `#example-kalman`), and the prose form is "worked example {domain}"
(e.g., "worked example bandit").

Defined in [`FORMAT.md`](../../FORMAT.md) §`type` — what kind of claim.
