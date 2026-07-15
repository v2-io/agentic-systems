---
slug: exponential-cognitive-load
schema_version: 1
term: exponential cognitive load
name: Exponential cognitive load
notation: ""
brief: Hypothesis that implementation time grows exponentially with the number of discontinuities in a changeset.
layer: framing-vocabulary
status: weak
tags: [structural_concepts]
source_type: asf
primary_source: 02-tst-core/src/hyp-exponential-cognitive-load.md
first_asf_mention: 02-tst-core/src/hyp-exponential-cognitive-load.md
see_also: [atomic-changeset, coherence-coupling]
aliases: []
do_not_confuse: []
---

If context-switching compounds multiplicatively, implementation time scales as
$t_{\text{actual}} = t_{\text{baseline}} \times k^{\text{discontinuities}}$
where $k \gt 1$ is the compounding factor per boundary crossing. Even modest $k$
(1.1–1.2) create large differences at scale. The relationship may instead be linear, sub-exponential, or structure-dependent — TST states this explicitly as a hypothesis requiring validation.

Status `weak`: low vote count (2 votes / 2 architectures) and the term is hypothetical even within TST. Tracking the name while the empirical picture develops.

See [`#hyp-exponential-cognitive-load`](../../02-tst-core/src/hyp-exponential-cognitive-load.md).
