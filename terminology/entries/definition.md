---
slug: definition
schema_version: 1
term: definition
name: Definition
brief: "A segment type: introduces a quantity, object, or notation."
layer: framing-vocabulary
status: canon
tags: [segment_types]
seq: 2
subgroup: Core Claim Types
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [postulate, formulation, derived]
aliases: []
do_not_confuse: []
---

A `type: definition` segment introduces a new quantity, object, relation, or notation into the
framework. Definitions are not derived — they constitute the vocabulary that other segments use.
Equation-level tags on definitional equations use `*[Definition (slug)]*`.

Most definitions have a `status` of `axiomatic` (the definition is the thing — there is nothing
deeper to derive) or `exact` (once the quantities exist, this relationship follows mathematically).
A definition whose form is a representational choice rather than a mathematical necessity should
instead be typed `formulation`.

Defined in [`FORMAT.md`](../../FORMAT.md) §`type` — what kind of claim.
