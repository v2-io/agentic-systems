---
slug: exponential-cognitive-load
type: hypothesis
status: discussion-grade
depends:
  - change-proximity-principle
  - deliberation-cost
---

# Hypothesis: Exponential Cognitive Load

If context-switching compounds multiplicatively, implementation time grows exponentially with the number of boundary crossings (discontinuities) in a changeset.

## Formal Expression

*[Hypothesis (exponential-cognitive-load)]*

$$t_{\text{actual}} = t_{\text{baseline}} \times k^{\text{discontinuities}}$$

where $k \gt 1$ is the compounding factor per context switch.

Even modest values of $k$ (1.1 to 1.2) create substantial differences when compounded across many discontinuities.

## Epistemic Status

*Hypothesis.* TST states this carefully as a hypothesis requiring validation, and that caution is warranted. The actual relationship may be:
- Linear ($k = 1$ with additive cost per switch)
- Sub-exponential (diminishing marginal cost of additional switches)
- Exponential (as hypothesized)
- Dependent on the *structure* of dependencies between scattered changes

ACT's #deliberation-cost framework suggests a refinement: the functional form likely depends on the dependency structure of the scattered changes, not on the count of discontinuities alone. Independent changes across many files may cost linearly (each context switch is independent). Interacting changes across many files — where understanding the change in file A requires understanding the change in file B which requires understanding file C — may cost exponentially because the agent must hold multiple contexts simultaneously to reason about their interactions. The distinction is between parallel context-loading (linear) and nested context-dependency (potentially exponential).

## Discussion

**Why the hypothesis persists.** Despite lacking formal derivation, exponential cognitive load explains a robust observation: developers strongly prefer consolidated changes, and scattered changes feel *disproportionately* difficult. The hypothesis provides a quantitative framework for this observation. Whether the mechanism is truly exponential or merely superlinear, the qualitative implication is the same: reducing discontinuities has increasing marginal returns.

**Connection to ACT's deliberation cost.** The #deliberation-cost framework formalizes the cost of reasoning before acting. Context switches during implementation are a form of deliberation cost — the agent must reason about how changes in one location affect another. When the changes are independent, this deliberation is parallelizable (each change can be understood locally). When they interact, deliberation becomes sequential and potentially recursive: understanding change A requires understanding change B, which may require understanding change C. This recursive dependency structure is what could produce genuine exponential scaling.

## Working Notes

- The key open question is empirical: does the cost scale with discontinuity *count* (as stated) or with discontinuity *dependency structure* (as ACT's deliberation-cost framework suggests)? These make different predictions: the count model says 10 independent scattered changes are as hard as 10 interdependent ones; the structure model says the independent case is much easier. This is testable.
- For AI agents, context-switch cost may have a different profile than for humans. LLMs can hold large contexts but may have difficulty with *deep* reasoning chains. This suggests the structure-dependent model (where chain depth matters more than context breadth) may be especially relevant for AI agents.
- If the exponential form holds, it has strong architectural implications: any design that reduces the number of boundary crossings for typical features is worth disproportionate investment. This amplifies #change-investment far beyond the linear model.
- TST's notation $k^{\text{discontinuities}}$ uses "discontinuities" loosely. A more precise formulation would count boundary crossings weighted by boundary type ( #change-distance), or better yet, measure the depth of the dependency chain among the scattered changes.

*(Descended from TST H-09.1.)*
