---
slug: coherence-coupling-measurement
type: measurement
status: empirical
depends:
  - system-coupling
  - system-coherence
---

# Measurement: Coherence-Coupling Measurement

Software coherence and coupling can be measured from git history, enabling empirical evaluation of architectural quality.

## Formal Expression

*[Measurement (coherence-coupling-measurement)]*

An architectural quality metric can be constructed as:

$$Q = \frac{\sum_i \text{coherence}(m_i)}{\sum_{i \neq j} \text{coupling}(m_i, m_j)}$$

where #system-coherence and #system-coupling are estimated from historical commits:

1. **Coherence**: average proximity of changes within each module over observed commits
2. **Coupling**: frequency of commits touching multiple modules, yielding conditional probability estimates
3. **Quality ratio**: coherence / coupling (handling edge cases where coupling approaches zero)

## Epistemic Status

*Empirical.* The measurement procedure is well-defined given sufficient git history. The claim that the ratio captures "architectural quality" is an empirical hypothesis — it assumes that the high-coherence/low-coupling ideal (the classic software engineering principle) is the correct optimization target. Under AAD, this is motivated by #temporal-optimality: high coherence reduces per-feature comprehension cost, low coupling reduces per-feature changeset size. But the ratio form ($Q$) is one possible aggregation; others (weighted sum, geometric mean, per-module scores) might predict temporal outcomes better.

**Requirements**: sufficient historical data for statistical significance, stable module boundaries (or boundary-evolution tracking), and a representative feature distribution in the observed history.

## Discussion

**From opinion to measurement.** The measurement transforms architectural discussions from aesthetic judgment to empirical observation: "this refactoring increased our coherence-coupling ratio from 2.3 to 4.1 based on the last 100 commits." This is the measurement-driven approach that AAD enables in the software domain — the theory provides the quantities to measure and the reason they matter ( #temporal-optimality), and git provides the interventional data to estimate them.

**Feature-distribution sensitivity.** Both coherence and coupling are estimated from historical features. If the future feature distribution differs from the past, the estimates may not predict future architectural performance. This is the same sensitivity as #change-expectation-baseline's uniform-feature-rate assumption.

**Organizational reflection (Conway's Law).** *[Discussion — well-established observation, not derived within AAD.]* Per Conway's Law, the coupling structure of a codebase tends to mirror the communication structure of the organization that built it. This means the coupling matrix estimated from git history is simultaneously a measurement of architectural coupling *and* a proxy for organizational communication overhead. High coupling between modules owned by different teams predicts coordination costs — meetings, Slack threads, blocked pull requests — that are real development time not captured in the code itself.

This suggests a diagnostic: when measured coupling between team-owned modules is high, the response could be architectural (reduce the technical coupling), organizational (put the coupled modules under one team), or both. The #change-investment threshold applies: choose the response that minimizes total expected future time. Organizational restructuring has high upfront cost but can reduce coupling systemically; architectural decoupling has lower upfront cost but may address symptoms rather than causes.

*[Discussion — the organizational dimension is well-supported by prior work (Conway 1968; MacCormack, Baldwin & Rusnak 2006 on "hidden structure" in software). The formal connection — that coupling measurements from git history can predict organizational coordination costs — is an empirical claim that has been partially validated (see `lit-review/` materials on Design Rule Spaces and Propagation Cost) but not with TST's specific formulation.]*

**Coupling asymmetry.** *[Discussion — informative for diagnosis.]* The coupling measure $P(\text{change}(m_j) \mid \text{change}(m_i))$ is asymmetric: module A might frequently trigger changes to module B without the reverse being true. This asymmetry is informative — it often reveals dependency direction, interface ownership, and where abstraction boundaries are leaking. Symmetric coupling suggests mutual entanglement; asymmetric coupling suggests a dependency that could potentially be broken by improving the interface of the upstream module.

## Working Notes

- The ratio form privileges balance. A system with coherence = 100 and coupling = 50 gets $Q = 2$; a system with coherence = 10 and coupling = 5 also gets $Q = 2$. But the first system has higher absolute coupling, which means more cross-module work per feature. An additive form ($\alpha \cdot \text{coherence} - \beta \cdot \text{coupling}$) might be more useful for optimization, since it distinguishes absolute levels.
- Git commit granularity matters. If developers make large commits bundling unrelated changes, coupling estimates are inflated. If they make tiny commits splitting related changes, coherence estimates may be deflated. Atomic commits (one feature per commit) are the ideal data source, matching the #atomic-changeset definition.
- This measurement is a candidate for #causal-discovery-from-git — the co-change data is interventional (each commit is a developer's intervention), not merely observational. This gives the coupling estimates causal rather than merely correlational interpretation, which is stronger than typical software metrics.

*(Descended from TST T-10.)*
