---
slug: type-empirical
schema_version: 1
term: type-empirical
name: Empirical (segment type)
brief: "A segment type: generalization supported by data or simulation, not fully derived from the formalism."
layer: framing-vocabulary
status: canon
tags: [segment_types]
seq: 11
subgroup: Empirical and Interpretive
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [hypothesis, observation, measurement, status-empirical]
aliases: [empirical]
do_not_confuse: [status-empirical, hypothesis, observation]
---

A `type: empirical` segment states a generalization that is supported by data, simulation, or
practical observation, but whose formal derivation from the AAD axioms is either absent or
impossible in principle (because the claim is fundamentally about how the world behaves, not what
the formalism forces).

The slug `type-empirical` distinguishes this as a *segment type* value from [`status-empirical`](status-empirical.md),
which is a *frontmatter status* value. Both exist; they are used differently.
A `type: empirical` segment often carries `status: empirical`, but can also carry `status: heuristic`
if the data support is informal or limited.

Equation-level tags use `*[Empirical Claim]*` to mark empirical equations inline.

Defined in [`FORMAT.md`](../../FORMAT.md) §`type` — what kind of claim.
