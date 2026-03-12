---
slug: system-coherence
type: definition
status: axiomatic
depends:
  - change-distance
---

# Definition: System Coherence

The expected proximity of changes within a module.

## Formal Expression

*[Definition (system-coherence)]*

$$\text{coherence}(m) = E[\text{proximity}(\text{changes within } m)]$$

where proximity is the inverse of #change-distance:

$$\text{proximity}(c_i, c_j) = \frac{1}{d(c_i, c_j)}$$

A highly coherent module concentrates its changes — when a feature touches the module, the changes tend to be close together. A low-coherence module scatters changes across its internal structure.

## Epistemic Status

Definitional. Coherence is the dual of #system-coupling: coupling measures change propagation *between* modules, coherence measures change locality *within* modules. Both are empirical, estimated from observed change patterns.

## Discussion

Coherence captures whether a module's internal organization matches its usage patterns. A module with high coherence groups code that changes together, so features that touch the module require understanding only a localized portion. This reduces the $M_t$ construction cost ( #comprehension-time) for the agent.

The classic "high cohesion, low coupling" principle in software engineering is the conjunction of high #system-coherence and low #system-coupling. ACT provides the *why*: high coherence reduces per-feature comprehension cost (fewer context switches), low coupling reduces per-feature changeset size (fewer modules touched). Both minimize total time under #temporal-optimality.

## Working Notes

- The proximity measure in the definition uses #change-distance, which is a discrete hierarchy. This means coherence is somewhat coarse-grained. A module where all changes happen in the same file has high coherence; one where they span many files has low coherence. Finer-grained measurement would require a continuous distance metric.
- Coherence is relative to the feature distribution. A module might appear coherent for historical features but incoherent for future ones if the product direction changes. This is the same feature-distribution sensitivity as #system-coupling.

*(Descended from TST D-07.)*
