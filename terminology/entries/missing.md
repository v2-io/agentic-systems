---
slug: missing
schema_version: 1
term: missing
name: Missing
brief: "A segment stage: no segment file exists yet — the slot is claimed in OUTLINE.md but the file has not been written."
layer: framing-vocabulary
status: canon
tags: [process_vocabulary]
seq: 1
subgroup: Stages
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [draft, deps-verified, claims-verified, format-clean, candidate]
aliases: []
do_not_confuse: []
---

`stage: missing` is the starting point in the promotion ladder — a slot in `OUTLINE.md` (and the
theory's dependency graph) that does not yet have a corresponding segment file. Missing segments
are gaps the framework knows about: they appear in OUTLINE.md as claims the theory needs, but
the work of writing them has not yet happened.

Unlike all other stages, `missing` segments have no file in `src/`. They exist only as references
in OUTLINE.md. `bin/lint-outline` reports them as gaps. When a segment file is created (with
proper YAML frontmatter and at least a skeleton formal expression), it advances to `draft`.

There is no gate to advance from `missing` to `draft` — creating the file and beginning to fill
it is sufficient.

Defined in [`FORMAT.md`](../../FORMAT.md) §`stage` — development process state.
