---
slug: targeted
schema_version: 1
term: targeted
name: Targeted
brief: "A search log depth tier: specific venues, authors, or concepts were searched deliberately for this finding."
layer: framing-vocabulary
status: canon
tags: [findings_vocabulary]
seq: 22
subgroup: Search Log Depth Tiers
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [search-log-field, cursory, nominally-comprehensive]
aliases: []
do_not_confuse: [cursory, nominally-comprehensive]
---

`targeted` is the search log depth tier indicating that specific venues, authors, citation chains,
or conceptual areas were searched deliberately for this finding — going beyond a brief initial pass to follow the natural prior-art trail.

Targeted search is appropriate when the domain is well-understood enough that the natural search targets are known: if a result is related to Lyapunov stability, then the targeted search checks the relevant stability theory literature; if related to causal inference, then Pearl's work and its extensions are checked directly. The note in the Search Log should name what was targeted and why those targets were chosen.

`targeted` supports stronger novelty claims than `cursory`, but it remains weaker than
`nominally-comprehensive` (which uses automated comprehensive-search tools) and much weaker than
`comprehensive` (which reaches human-researcher depth with deliberate corner-case probing).

Defined in [`FORMAT.md`](../../FORMAT.md) §Findings — Field-by-field guidance — Search Log.
