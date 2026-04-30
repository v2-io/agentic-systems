---
slug: hyp-exponential-cognitive-load
type: hypothesis
status: discussion-grade
depends:
  - der-change-proximity-principle
  - der-deliberation-cost
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

AAD's #der-deliberation-cost framework suggests a refinement: the functional form likely depends on the dependency structure of the scattered changes, not on the count of discontinuities alone. Independent changes across many files may cost linearly (each context switch is independent). Interacting changes across many files — where understanding the change in file A requires understanding the change in file B which requires understanding file C — may cost exponentially because the agent must hold multiple contexts simultaneously to reason about their interactions. The distinction is between parallel context-loading (linear) and nested context-dependency (potentially exponential).

## Discussion

**Why the hypothesis persists.** Despite lacking formal derivation, exponential cognitive load explains a robust observation: developers strongly prefer consolidated changes, and scattered changes feel *disproportionately* difficult. The hypothesis provides a quantitative framework for this observation. Whether the mechanism is truly exponential or merely superlinear, the qualitative implication is the same: reducing discontinuities has increasing marginal returns.

**Connection to AAD's deliberation cost.** The #der-deliberation-cost framework formalizes the cost of reasoning before acting. Context switches during implementation are a form of deliberation cost — the agent must reason about how changes in one location affect another. When the changes are independent, this deliberation is parallelizable (each change can be understood locally). When they interact, deliberation becomes sequential and potentially recursive: understanding change A requires understanding change B, which may require understanding change C. This recursive dependency structure is what could produce genuine exponential scaling.

**Discontinuity hierarchy.** *[Discussion — taxonomy, not derived.]* Not all discontinuities are equal. The cost per boundary crossing increases with the type of boundary:

1. *Lexical*: Symbol must be found elsewhere in the same file
2. *File*: Must open another file and load its context
3. *Module*: Must understand another module's conventions, invariants, and vocabulary
4. *Service*: Must understand another service's API, data model, and failure modes
5. *Network*: Must trace through network calls, serialization, and distributed state

Each level roughly doubles the context-loading cost (the $k$ factor increases with boundary type). This is a heuristic observation, not a measured result — the actual cost ratios are an empirical question. The `empirical-discontinuity/` toolkit validates the exponential form for file-level crossings with $\alpha \approx 0.118$ ($k \approx 1.118$) for normal development. Whether the doubling-per-level heuristic holds is untested.

**The comprehension-changeability tension.** *[Discussion — architecturally consequential.]* Conventional advice emphasizes small, focused units (functions, classes, modules) for changeability — changes are isolated, tests are targeted, coupling is reduced. But small units create comprehension discontinuities: understanding the flow requires jumping between many fragments. This creates a genuine tension:

- Fewer, larger units → fewer discontinuities → faster comprehension → but higher coupling, larger changesets
- Many small units → more discontinuities → slower comprehension → but lower coupling, smaller changesets

A resolution follows from #der-change-investment: the right balance depends on $\hat{n}_{\text{future}}$. For young code ($\hat{n}_{\text{future}}$ small), the comprehension cost of fragmentation is paid on every interaction but the changeability benefit is realized rarely — favor continuity. For mature, heavily-modified code ($\hat{n}_{\text{future}}$ large), the changeability benefit dominates — favor modularity. The crossover point is where the cumulative comprehension cost of fragmentation equals the cumulative changeset-size savings from isolation. This crossover is not derived but is testable: compare total development time for features implemented in consolidated vs. fragmented code at different change-history depths.

**Anti-patterns that create unnecessary discontinuities.** *[Discussion — pattern catalog, empirically grounded.]* Several common practices create discontinuities without corresponding changeability benefits:

- *Premature abstraction*: Extracting interfaces or abstract classes before the variation they're meant to accommodate has actually appeared. Creates discontinuities now for benefits that may never materialize.
- *Over-interfacing*: Placing interfaces between components that always change together. The interface adds a discontinuity but provides no isolation benefit since both sides change simultaneously.
- *Excessive indirection*: Chains of delegation (A calls B which calls C which calls D) where each hop requires the reader to find and understand the next link. The call depth is a direct measure of discontinuity count.
- *Naming minimalism*: Abbreviated or generic names (e.g., `mgr`, `svc`, `impl`) that force the reader to look at the implementation to understand what the component does, adding a discontinuity that a descriptive name would have eliminated.

These anti-patterns share a common structure: they optimize for a dimension (abstraction purity, interface coverage, code size) that is not part of the temporal optimization objective. Each can be diagnosed by asking: "Does this boundary crossing save future changeset size proportional to its comprehension cost?" When the answer is no, the discontinuity is pure overhead.

*[Discussion — the anti-pattern diagnosis question is a direct application of #der-change-investment to discontinuity creation. But "proportional to its comprehension cost" is informal — formalizing it requires a way to estimate per-discontinuity comprehension cost, which connects to the open empirical question about the $k$ value per boundary type.]*

## Working Notes

- The key open question is empirical: does the cost scale with discontinuity *count* (as stated) or with discontinuity *dependency structure* (as AAD's deliberation-cost framework suggests)? These make different predictions: the count model says 10 independent scattered changes are as hard as 10 interdependent ones; the structure model says the independent case is much easier. This is testable.
- For AI agents, context-switch cost may have a different profile than for humans. LLMs can hold large contexts but may have difficulty with *deep* reasoning chains. This suggests the structure-dependent model (where chain depth matters more than context breadth) may be especially relevant for AI agents.
- If the exponential form holds, it has strong architectural implications: any design that reduces the number of boundary crossings for typical features is worth disproportionate investment. This amplifies #der-change-investment far beyond the linear model.
- TST's notation $k^{\text{discontinuities}}$ uses "discontinuities" loosely. A more precise formulation would count boundary crossings weighted by boundary type ( #def-change-distance), or better yet, measure the depth of the dependency chain among the scattered changes.
- A formal route from the count-vs-structure open question above to a structure-sensitive operator scaling is sketched in `spikes/spike-transient-dependency-amplification.md`: cost scales with the operator norm of a finite-horizon product $\lVert J_{F,d}\cdots J_{F,1}\rVert$ of feature-local Jacobians rather than with raw discontinuity count. The spike's affine sub-scope recovers $k^d$ as a uniform-per-block-gain special case (each discontinuity contributes the same $k$), which preserves this hypothesis as a scalar approximation while upgrading the underlying theory to dependency-structure-sensitive form. Promotion to a derived TST result is blocked on the spike's open obligations: formal $\widehat J_F$ construction from TST quantities, nonlinear-remainder bounds, cyclic-dependency treatment via SCC condensation, and empirical validation.
