---
slug: draft
schema_version: 1
term: draft
name: Draft
brief: "A segment stage: first AAD-formatted version written, not yet reviewed through any gate."
layer: framing-vocabulary
status: canon
tags: [process_vocabulary]
seq: 2
subgroup: Stages
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [missing, deps-verified, dependency-audit]
aliases: []
do_not_confuse: [missing, deps-verified]
---

`stage: draft` indicates that the segment has been written in the AAD FORMAT — it has proper YAML
frontmatter, a Formal Expression, an Epistemic Status section, and a Discussion section — but has
not yet been reviewed through any of the four promotion gates.

A draft segment may have significant issues: dependencies might be wrong or incomplete, derivations
might be incorrect, epistemic labels might not match the actual claim strength, and notation might
not match NOTATION.md. These issues are expected at `draft` stage — that is what the promotion
gates are for.

A segment returns to `draft` (from any higher stage) when: a dependency is revised in a way that
affects the segment's claims; an error is found in a derivation; the scope changes; or external
review identifies an issue not caught in the original promotion. Downgrade is to `draft`, not to
an intermediate stage, because the issue may have cascading effects that require re-review from
the start.

Defined in [`FORMAT.md`](../../FORMAT.md) §`stage` — development process state.
