---
slug: atomic-changeset
schema_version: 1
term: atomic changeset
name: Atomic Changeset
notation: "$\\text{changeset}(F)$"
brief: The complete diff — source, schema, config, tests, infrastructure — between codebase states before and after a feature is fully implemented.
layer: prose-symbol
status: canon
tags: [core_quantities]
source_type: asf
primary_source: 02-tst-core/src/def-atomic-changeset.md
first_asf_mention: 02-tst-core/src/def-atomic-changeset.md
see_also: [atomic-changeset, temporal-optimality, developer-agent, coherence-coupling]
aliases: []
do_not_confuse: []
---

For feature $F$ applied to system $S$:

$$\text{changeset}(F) = S_{\text{after}} \ominus S_{\text{before}}$$

where $\ominus$ is the human- or agent-authored diff, excluding build artifacts, generated code,
and automated reformatting. "Codebase" crosses all architectural boundaries: source code, schemas,
configuration, infrastructure-as-code, tests, API contracts, deployment pipelines, monitoring.
If it must change to deliver the feature, it is part of the changeset.

The changeset is the observable trace of an implementation decision — the software analog of action $a_t$ in the general agent formalism. Changeset *size* (lines changed, files touched,
modules affected) is what temporal-optimality-driven TST claims operate on. The exclusion of generated artifacts is a pragmatic convention aligned with measuring the decisions the agent actually makes, not amplification effects.

Defined in [`#def-atomic-changeset`](../../02-tst-core/src/def-atomic-changeset.md).
