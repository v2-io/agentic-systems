---
slug: not-conducted
schema_version: 1
term: not-conducted
name: Not-Conducted
brief: "A search log depth tier: no literature search has been performed for this finding yet."
layer: framing-vocabulary
status: canon
tags: [findings_vocabulary]
seq: 20
subgroup: Search Log Depth Tiers
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [search-log-field, cursory, intuition-only]
aliases: []
do_not_confuse: [intuition-only, cursory]
---

`not-conducted` is the search log depth tier indicating that no literature search has been
performed for this finding yet. It is used as the status in a Search Log entry when the honest
state is that search work remains to be done.

Using `not-conducted` explicitly is better than omitting the Search Log entry: it signals to
future agents and reviewers that search is outstanding and what specific domain or question is
the natural target. The Search Log entry should still contain a note on where search should focus
when it is conducted.

The tier ordering from most to least thorough: `comprehensive` → `nominally-comprehensive` →
`targeted` → `cursory` → `not-conducted` / `intuition-only` (roughly co-equal at the bottom).
`not-conducted` indicates absence of search; `intuition-only` indicates the author's trained
instinct before search.

Defined in [`FORMAT.md`](../../FORMAT.md) §Findings — Field-by-field guidance — Search Log.
