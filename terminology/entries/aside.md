---
slug: aside
schema_version: 1
term: aside
name: Aside
brief: "A segment type: tangential observation or connection — informative but not load-bearing for the theory."
layer: framing-vocabulary
status: canon
tags: [segment_types]
seq: 19
subgroup: Structural and Discursive
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [detail, type-discussion, observation]
aliases: []
do_not_confuse: [detail, type-discussion]
---

A `type: aside` segment carries a tangential observation, connection, or historical note that
enriches the reader's picture of the framework without being load-bearing for any downstream
claim. No other segment should `depends:` on an `aside` — if it is a genuine dependency, the
content should be promoted to a type that carries formal weight.

Asides are useful for: noting connections to adjacent literatures that inform but don't ground the
claim; historical context; observations from implementation experience; and similar content that
would interrupt the main argument if inserted inline but is worth preserving somewhere accessible.

The distinction from `type: detail` is load-bearing: `detail` content is technically required to
use or implement a parent claim; `aside` content is optional enrichment.

Defined in [`FORMAT.md`](../../FORMAT.md) §`type` — what kind of claim.
