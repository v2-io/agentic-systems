---
slug: nominally-comprehensive
schema_version: 1
term: nominally-comprehensive
name: Nominally-Comprehensive
brief: "A search log depth tier: an automated comprehensive-search tool (e.g., Undermind report) was used — broader than targeted, less deep than comprehensive."
layer: framing-vocabulary
status: canon
tags: [findings_vocabulary]
seq: 23
subgroup: Search Log Depth Tiers
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [search-log-field, targeted, comprehensive]
aliases: []
do_not_confuse: [targeted, comprehensive]
---

`nominally-comprehensive` is the search log depth tier for searches conducted with automated
comprehensive-search tools — Undermind reports and similar systems that survey literature broadly
across many venues and citation networks. These tools cover more ground than a human researcher
doing targeted search, but do not reach the depth that a domain expert with deliberate
corner-case probing would call truly comprehensive.

The tier is stronger than `targeted` and weaker than `comprehensive`. When a finding has been
through a pillar-level prior-art defense (e.g., an Undermind report), the Search Log entry
references the defense document and tags the depth `nominally-comprehensive` rather than
`comprehensive` — the honest position is that automation has broad coverage but not expert depth.

The qualifier "nominally" is important: it signals that the search has the form of comprehensive
coverage without the guarantee of human expert judgment. Future search work can upgrade the tier
to `comprehensive` by adding deliberate follow-up targeting the gaps the automated tool's summary
indicates.

Defined in [`FORMAT.md`](../../FORMAT.md) §Findings — Field-by-field guidance — Search Log.
