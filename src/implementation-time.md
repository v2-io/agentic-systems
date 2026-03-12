---
slug: implementation-time
type: definition
status: axiomatic
depends:
  - feature-definition
  - comprehension-time
---

# Definition: Implementation Time

The time from first surviving change to complete feature.

## Formal Expression

*[Definition (implementation-time)]*

For a feature $F$ ( #feature-definition) applied to system $S$:

$$t_{\text{impl}}(F, S) = \text{time from first surviving modification to feature completion}$$

This includes:
- Writing and modifying code
- Local testing and validation
- Addressing immediate issues discovered during implementation

By construction, the total feature time decomposes:

$$\text{time}(F) = t_{\text{comp}}(F, S) + t_{\text{impl}}(F, S)$$

## Epistemic Status

Definitional. The decomposition of feature time into comprehension + implementation is a partition — together they cover the full duration, and the boundary is defined by #comprehension-time.

## Discussion

**Implementation time is what most metrics measure.** Cycle time, velocity, lines-per-hour — these track implementation. But #dual-optimization shows that optimizing implementation time alone is insufficient; comprehension time often dominates, especially under turnover.

**Under AI-assisted development, implementation time approaches zero for well-specified features.** This is the regime where #specification-bound becomes binding — the implementation is fast, but the specification (which is part of comprehension) is the bottleneck.

## Working Notes

- The clean decomposition time(F) = t_comp + t_impl assumes these are sequential. In practice they overlap (exploratory implementation as part of comprehension). The decomposition is still useful as an accounting identity, but measurements will be approximate.
- Should this definition explicitly reference #action-selection? Implementation is the phase where the agent is primarily acting rather than observing — high action rate, lower exploration.

*(Descended from TST D-03.)*
