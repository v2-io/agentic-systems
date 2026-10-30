---
slug: hyp-exponential-cognitive-load
type: hypothesis
status: discussion-grade
depends:
  - der-change-proximity-principle
  - der-deliberation-cost
stage: draft
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

AAT's #der-deliberation-cost framework suggests a refinement: the functional form likely depends on the dependency structure of the scattered changes, not on the count of discontinuities alone. Independent changes across many files may cost linearly (each context switch is independent). Interacting changes across many files — where understanding the change in file A requires understanding the change in file B which requires understanding file C — may cost exponentially because the agent must hold multiple contexts simultaneously to reason about their interactions. The distinction is between parallel context-loading (linear) and nested context-dependency (potentially exponential).

The one non-circular measurement available bears on the count form only, and disfavors it: at file and directory granularity, the elapsed time between a developer's consecutive commits rises with the number of crossings in the commit, but sublinearly, roughly as $(1+d)^{0.4}$ to $(1+d)^{0.7}$, and an exponential term in $d$ is indistinguishable from zero or negative once a power term is allowed (Discussion). That measurement is *heuristic* tier: inter-commit elapsed time is a proxy for implementation time, and the evidence comes from three repositories. The structure-dependent form is untested.

## Discussion

**Why the hypothesis persists.** Despite lacking formal derivation, exponential cognitive load explains a robust observation: developers strongly prefer consolidated changes, and scattered changes feel *disproportionately* difficult. The hypothesis provides a quantitative framework for this observation. If the cost is superlinear in the crossings, whether exponential or not, reducing discontinuities has increasing marginal returns. Counted crossings alone do not show that superlinearity in the measurement below, so the disproportion developers report, if it is real, has to come from something the count leaves out; the dependency structure among the changes is the candidate this segment's Epistemic Status names.

**Connection to AAT's deliberation cost.** The #der-deliberation-cost framework formalizes the cost of reasoning before acting. Context switches during implementation are a form of deliberation cost — the agent must reason about how changes in one location affect another. When the changes are independent, this deliberation is parallelizable (each change can be understood locally). When they interact, deliberation becomes sequential and potentially recursive: understanding change A requires understanding change B, which may require understanding change C. This recursive dependency structure is what could produce genuine exponential scaling.

**Discontinuity hierarchy.** *[Discussion — taxonomy, not derived.]* Not all discontinuities are equal. The cost per boundary crossing increases with the type of boundary:

1. *Lexical*: Symbol must be found elsewhere in the same file
2. *File*: Must open another file and load its context
3. *Module*: Must understand another module's conventions, invariants, and vocabulary
4. *Service*: Must understand another service's API, data model, and failure modes
5. *Network*: Must trace through network calls, serialization, and distributed state

Each level roughly doubles the context-loading cost (the $k$ factor increases with boundary type). This is a heuristic observation, not a measured result — the actual cost ratios are an empirical question. The measurement below treats file and directory crossings only, with directory crossings weighted twice; whether the doubling-*per-boundary-type* heuristic holds is untested.

**A git-history measurement of the count form.** *[Empirical Claim — heuristic tier; elapsed time between commits as the time measure.]* For each commit, the discontinuity score is $d = (\text{file transitions}) + 2 \cdot (\text{directory transitions})$ over its changed paths, and the time is the elapsed time since the same author's previous commit, kept when under a session cap of 60 to 480 minutes. Three histories with direct (not squash-merged) commits were measured: the 316-commit TST research corpus (one author), obsidian-linter (45 authors) and ink (156 authors), with $N$ = 256–849 commit pairs at $d \le 25$ depending on repository and cap. Three findings hold in all three, at every cap and with lines changed as a covariate:

1. Elapsed time rises with $d$: Spearman $\rho$ = 0.27–0.45, and $\rho$ = 0.10–0.37 after partialling out lines changed.
2. The rise is not exponential. In $\log T = c + a\,d + b\log(1+d)$, the exponential form predicts $a \gt 0$ with $b \approx 0$. The bootstrap 95% interval for $a$ contains zero or lies below it everywhere (obsidian-linter, 240-minute cap: $a = -0.075$, interval $[-0.141, -0.003]$), while $b$ is positive: 0.38–0.92 without the covariate, with intervals excluding zero in two of the three histories and reaching zero in ink at two of three caps.
3. Read as a power law, $T \propto (1+d)^{\beta}$ with $\beta$ between 0.4 and 0.7, so sublinear. Medians over gaps up to 24 hours, which the cap cannot distort, rise and then flatten in the two multi-author histories (obsidian-linter: 8.5, 22.8, 28.2, 71 and 70 minutes for $d$ = 0, 1–2, 3–5, 6–10 and 11–25). In the single-author corpus they keep rising through $d = 25$ and fall above it.

A single exponential forced onto the same data returns a per-discontinuity rate of 0.04 to 0.13, depending on the fitting method and the cap. That number is what any fit of the exponential to a curve that is concave on a log scale returns over a short range; it is not evidence for the form. Squash-merged histories (gemini-cli, codex) record merge cadence rather than work, and there $d$ barely predicts the gap ($\rho \approx 0.1$).

Limits: elapsed time between commits includes everything else the developer did and depends on how they chose to cut commits. It is a proxy for implementation time, not a measure of comprehension. The score counts crossings without regard to whether the changes depend on one another, so the measurement tests the count form only. The structure-dependent form in the Epistemic Status, under which interacting changes compound and independent ones do not, needs a measure of dependency among the changed locations, and it is untested. The result is consistent with that form's prediction that most commits, whose changes are largely independent, cost about additively or less. It is equally consistent with a world where nothing compounds.

**The comprehension-changeability tension.** *[Discussion — architecturally consequential.]* Conventional advice emphasizes small, focused units (functions, classes, modules) for changeability — changes are isolated, tests are targeted, coupling is reduced. But small units create comprehension discontinuities: understanding the flow requires jumping between many fragments. This creates a genuine tension:

- Fewer, larger units → fewer discontinuities → faster comprehension → but higher coupling, larger changesets
- Many small units → more discontinuities → slower comprehension → but lower coupling, smaller changesets

A resolution follows from #der-change-investment: the right balance depends on $\hat n_{\text{future}}$. For young code ($\hat n_{\text{future}}$ small), the comprehension cost of fragmentation is paid on every interaction but the changeability benefit is realized rarely — favor continuity. For mature, heavily-modified code ($\hat n_{\text{future}}$ large), the changeability benefit dominates — favor modularity. The crossover point is where the cumulative comprehension cost of fragmentation equals the cumulative changeset-size savings from isolation. This crossover is not derived but is testable: compare total development time for features implemented in consolidated vs. fragmented code at different change-history depths.

**Anti-patterns that create unnecessary discontinuities.** *[Discussion — pattern catalog, empirically grounded.]* Several common practices create discontinuities without corresponding changeability benefits:

- *Premature abstraction*: Extracting interfaces or abstract classes before the variation they're meant to accommodate has actually appeared. Creates discontinuities now for benefits that may never materialize.
- *Over-interfacing*: Placing interfaces between components that always change together. The interface adds a discontinuity but provides no isolation benefit since both sides change simultaneously.
- *Excessive indirection*: Chains of delegation (A calls B which calls C which calls D) where each hop requires the reader to find and understand the next link. The call depth is a direct measure of discontinuity count.
- *Naming minimalism*: Abbreviated or generic names (e.g., `mgr`, `svc`, `impl`) that force the reader to look at the implementation to understand what the component does, adding a discontinuity that a descriptive name would have eliminated.

These anti-patterns share a common structure: they optimize for a dimension (abstraction purity, interface coverage, code size) that is not part of the temporal optimization objective. Each can be diagnosed by asking: "Does this boundary crossing save future changeset size proportional to its comprehension cost?" When the answer is no, the discontinuity is pure overhead.

*[Discussion — the anti-pattern diagnosis question is a direct application of #der-change-investment to discontinuity creation. But "proportional to its comprehension cost" is informal — formalizing it requires a way to estimate per-discontinuity comprehension cost, which connects to the open empirical question about the $k$ value per boundary type.]*

## Working Notes

- Reproducibility for the Discussion's measurement: `02-tst-core/empirical-discontinuity/elapsed_time.py`, with the `git log` command and each history's HEAD in its header, and the toolkit's `README.md` for the full tables. To be released as a citable code/data supplement at publication.
- Regression guard: a time *estimated* from files and lines changed cannot test this hypothesis, because $d$ is built from the same files. Fitting such an estimate returns $\alpha \approx 0.12$ even when the estimate has no per-file term (`empirical-discontinuity/reproduce_estimate_fit.py`). Any future measurement needs a time that is not a function of the changeset's counts.
- The key open question is empirical: does the cost scale with discontinuity *count* (as stated) or with discontinuity *dependency structure* (as AAT's deliberation-cost framework suggests)? These make different predictions: the count model says 10 independent scattered changes are as hard as 10 interdependent ones; the structure model says the independent case is much easier. The count side is now measured, at heuristic tier, as sublinear (Discussion). The structure side needs a per-commit dependency measure among the changed locations, for example co-change coupling or static call/import edges between them, and a time measure closer to working time than inter-commit gaps, such as IDE or agent-session instrumentation.
- For AI agents, context-switch cost may have a different profile than for humans. LLMs can hold large contexts but may have difficulty with *deep* reasoning chains. This suggests the structure-dependent model (where chain depth matters more than context breadth) may be especially relevant for AI agents.
- If the exponential form holds, it has strong architectural implications: any design that reduces the number of boundary crossings for typical features is worth disproportionate investment. This amplifies #der-change-investment far beyond the linear model.
- TST's notation $k^{\text{discontinuities}}$ uses "discontinuities" loosely. A more precise formulation would count boundary crossings weighted by boundary type ( #def-discontinuity-distance), or better yet, measure the depth of the dependency chain among the scattered changes.
- A formal route from the count-vs-structure open question above to a structure-sensitive operator scaling is sketched in `spikes/spike-transient-dependency-amplification.md`: cost scales with the operator norm of a finite-horizon product $\lVert J_{F,d}\cdots J_{F,1}\rVert$ of feature-local Jacobians rather than with raw discontinuity count. The spike's affine sub-scope recovers $k^d$ as a uniform-per-block-gain special case (each discontinuity contributes the same $k$), which preserves this hypothesis as a scalar approximation while upgrading the underlying theory to dependency-structure-sensitive form. Promotion to a derived TST result is blocked on the spike's open obligations: formal $\widehat J_F$ construction from TST quantities, nonlinear-remainder bounds, cyclic-dependency treatment via SCC condensation, and empirical validation.
