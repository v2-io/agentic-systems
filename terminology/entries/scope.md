---
slug: scope
schema_version: 1
term: scope
name: Scope
brief: "A segment type: restricts or broadens the domain under discussion."
layer: framing-vocabulary
status: canon
tags: [segment_types]
seq: 3
subgroup: Core Claim Types
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [postulate, definition, formulation]
aliases: []
do_not_confuse: []
---

A `type: scope` segment explicitly marks a boundary: what the framework applies to, what it
excludes, or what conditions must hold for subsequent claims to be valid. Scope segments are
foundational bookkeeping — they prevent downstream claims from being read more broadly than
intended, and they license the use of certain simplifications or assumptions within their
stated boundary.

Scope segments often carry `status: axiomatic` or `status: exact` because the scope is a
stipulation rather than a derivation. A scope segment that asserts something falsifiable about
the world (e.g., "real software systems have property P") should instead be typed `empirical`
or `hypothesis`.

Defined in [`FORMAT.md`](../../FORMAT.md) §`type` — what kind of claim.
