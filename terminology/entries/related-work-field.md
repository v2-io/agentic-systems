---
slug: related-work-field
schema_version: 1
term: related work field
name: Related Work Field
brief: "The fourth field in a Findings entry — one entry per prior work that bears on the finding, with citation, dates, relationship label, and a one-line note."
layer: framing-vocabulary
status: canon
tags: [findings_vocabulary]
seq: 4
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [findings-section, novelty-claim-field, search-log-field]
aliases: [related work]
do_not_confuse: [search-log-field]
---

The Related Work field is the fourth field in a `## Findings` entry. It carries the prior-art landscape for the finding — one entry per prior work, each with: (a) citation, (b) publication date, (c) date the project found the work, (d) a relationship label, and (e) a one-line note on the specific connection.

Two presentation forms are permitted:

**Bulleted form** — for simple prior-art landscapes (one to a handful of relevant priors, each bearing on the finding as a whole).

**Table form** — for richer landscapes where multiple aspects of the finding bear differently on different priors. Columns: ASF concern, prior-art language (with citation), relationship/positioning.

Established relationship labels include: *formal antecedent*, *conceptual precursor*,
*convergent independent*, *direct anticipation*, *partial anticipation*, *formalized by this finding*,
*verified by this finding*, *contradicted by this finding*, *empirical instantiation supporting / against*,
*adjacent literature*. The set is open-ended.

The Related Work field is the "receipts" that back the Novelty Claim field. A claim of novelty without Related Work is ungrounded — it may be true, but it isn't shown. Publication dates matter: something published after the project's derivation date cannot be a precursor.

Defined in [`FORMAT.md`](../../FORMAT.md) §Findings — Field-by-field guidance — Related Work.
