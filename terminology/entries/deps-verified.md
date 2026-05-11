---
slug: deps-verified
schema_version: 1
term: deps-verified
name: Deps-Verified
brief: "A segment stage: all dependencies have been audited and confirmed correct — reached by passing Gate 1."
layer: framing-vocabulary
status: canon
tags: [process_vocabulary]
seq: 3
subgroup: Stages
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [draft, claims-verified, dependency-audit]
aliases: []
do_not_confuse: [claims-verified, draft]
---

`stage: deps-verified` indicates that the segment has passed Gate 1 (dependency audit): all
entries in its `depends:` list have been confirmed as existing segment files; each dependency is
genuine (not merely "related"); each referenced segment is itself at `deps-verified` or higher;
and no missing dependencies have been identified.

Reaching `deps-verified` does not mean the segment's content is correct — it means the foundation
(the dependency chain) is solid enough to evaluate the content. Gate 2 (content review) is the
next gate, producing `claims-verified`.

Segments should be promoted in topological order: leaves first, then their dependents. A segment
should not reach `claims-verified` while any of its dependencies is still at `draft`.

Defined in [`FORMAT.md`](../../FORMAT.md) §`stage` — development process state, and §Gate 1.
