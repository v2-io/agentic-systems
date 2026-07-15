---
slug: observation
schema_version: 1
term: observation
name: Observation
brief: "A segment type: finding from simulation or empirical investigation — more specific than a generalization."
layer: framing-vocabulary
status: canon
tags: [segment_types]
seq: 12
subgroup: Empirical and Interpretive
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [type-empirical, hypothesis, measurement]
aliases: []
do_not_confuse: [type-empirical, measurement]
---

A `type: observation` segment records a specific finding from simulation, experiment, or empirical investigation — a concrete data point rather than a generalization. Where `type: empirical` states a pattern supported across data, `type: observation` records what was found in a particular run,
study, or dataset.

Observations ground the more abstract empirical claims and hypotheses. They carry the data provenance that empirical claims summarize. A segment of this type typically includes the specific conditions of the investigation (simulation parameters, dataset, method) so that the observation can be evaluated and replicated.

Defined in [`FORMAT.md`](../../FORMAT.md) §`type` — what kind of claim.
