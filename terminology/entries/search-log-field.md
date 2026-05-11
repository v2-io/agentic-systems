---
slug: search-log-field
schema_version: 1
term: search log field
name: Search Log Field
brief: "The fifth field in a Findings entry — dated disclosure of what literature search has been conducted and at what depth tier."
layer: framing-vocabulary
status: canon
tags: [findings_vocabulary]
seq: 5
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [findings-section, related-work-field, not-conducted, cursory, targeted, nominally-comprehensive, comprehensive, intuition-only]
aliases: [search log]
do_not_confuse: [related-work-field]
---

The Search Log field is the fifth and final field in a `## Findings` entry. It carries dated
entries disclosing what literature search has been conducted and how. Each entry records: the date,
the search status (a depth tier), and a one-sentence note on what was searched and what was not.

Entries accumulate over time — older entries stay for traceability as searches deepen. The field
is the discipline that prevents `Claim novelty on...` from being hubris: a claim of novelty under
cursory search is honest about what it is; under comprehensive search, much stronger; under
intuition-only, weaker but better than implicit silence.

The depth tier vocabulary (from most to least thorough):
- `comprehensive` — pushed to human-researcher depth; multiple iterations, deliberate corner-case probing
- `nominally-comprehensive` — automated comprehensive-search tool (e.g., Undermind report); stronger than targeted, weaker than comprehensive
- `targeted` — specific venues/authors/concepts searched deliberately
- `cursory` — brief initial search
- `not-conducted` — no search yet
- `intuition-only` — author's pre-search instinct (valid and valuable when tagged honestly)

An *intuition entry* is explicitly permitted — what the author's pre-search instinct says about
where prior art might lie, which adjacent literatures would be natural targets. For AI agents,
this includes intuitions from training rather than active retrieval. Tagging as `intuition-only`
makes the source explicit. Intuition entries are valuable: they orient future searches and make
the agent's priors visible so they can be confirmed or refuted.

Defined in [`FORMAT.md`](../../FORMAT.md) §Findings — Field-by-field guidance — Search Log.
