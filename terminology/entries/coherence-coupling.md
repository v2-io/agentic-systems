---
slug: coherence-coupling
schema_version: 1
term: coherence coupling
name: Coherence-Coupling
notation: "$Q$"
brief: An empirical architectural quality ratio derived from git history — coherence (intra-module change proximity) over coupling (inter-module co-change frequency) — grounding the classic software engineering principle in measurable data.
layer: prose-symbol
status: canon
tags: [core_quantities]
source_type: asf
primary_source: 02-tst-core/src/meas-coherence-coupling.md
first_asf_mention: 02-tst-core/src/meas-coherence-coupling.md
see_also: [atomic-changeset, temporal-optimality, developer-agent, continuous-operation]
aliases: []
do_not_confuse: []
---

An architectural quality metric computed from git history:

$$Q = \frac{\sum_i \text{coherence}(m_i)}{\sum_{i \neq j} \text{coupling}(m_i, m_j)}$$

where coherence is the average proximity of changes within each module over observed commits,
and coupling is the frequency of commits touching multiple modules (yielding conditional
probability estimates of co-change). Under temporal optimality: high coherence reduces
per-feature comprehension cost; low coupling reduces per-feature changeset size.

**From opinion to measurement**: the ratio transforms architectural discussions from aesthetic
judgment to empirical observation. Git commits are developer interventions in Pearl's sense,
so the underlying data is interventional — in favorable regimes (atomic commits, asymmetric
co-change patterns), the coupling estimate captures genuine causal structure, not mere
co-occurrence.

**Organizational reflection (Conway's Law)**: the coupling matrix estimated from git history
simultaneously measures architectural coupling and proxies organizational communication overhead.
High coupling between team-owned modules predicts coordination costs not captured in the code itself.

**Coupling asymmetry** is informative: $P(\text{change}(m_j) \mid \text{change}(m_i))$ is
asymmetric. Asymmetric coupling suggests a dependency that could be broken by improving the
upstream interface; symmetric coupling suggests mutual entanglement.

Measurement defined in [`#meas-coherence-coupling`](../../02-tst-core/src/meas-coherence-coupling.md).
