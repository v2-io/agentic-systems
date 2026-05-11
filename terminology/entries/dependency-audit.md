---
slug: dependency-audit
schema_version: 1
term: dependency audit
name: Dependency Audit
brief: "Gate 1: verifies that all `depends:` entries exist, are genuine, and are themselves at deps-verified or higher. Produces stage: deps-verified."
layer: framing-vocabulary
status: canon
tags: [process_vocabulary]
seq: 11
subgroup: Gates
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [deps-verified, draft, content-review]
aliases: [gate 1]
do_not_confuse: [content-review, mechanical-review]
---

The dependency audit is Gate 1 in the segment promotion workflow — the first of four named gates a
segment passes through before reaching `candidate`. Passing the dependency audit advances a segment
from `draft` to `deps-verified`.

The gate has four completion criteria (all must be met):
1. Every slug in `depends:` exists as a segment file.
2. Each dependency is genuine — the segment uses the referenced segment's definitions, results, or scope conditions, not merely "related to" it.
3. Each referenced segment is itself at `deps-verified` or higher (topological promotion order).
4. No missing dependencies — if the Formal Expression uses a quantity defined elsewhere, that slug appears in `depends:`.

Failing any criterion returns the segment to `draft` with a specific note about which dependency
is missing, spurious, or insufficiently promoted. The gate is a precondition for Gate 2 (content
review) — verifying content correctness presupposes the foundation (the dependency chain) is solid.

See [`FORMAT.md`](../../FORMAT.md) §Gate 1.
