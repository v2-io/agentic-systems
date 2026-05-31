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

AAT's #der-deliberation-cost framework suggests a refinement: the functional form likely depends on the dependency structure of the scattered changes, not on the count of discontinuities alone. Independent changes across many files may cost linearly (each context switch is independent). Interacting changes across many files — where understanding the change in file A requires understanding the change in file B which requires understanding file C — may cost exponentially because the agent must hold multiple contexts simultaneously to reason about their interactions. The distinction is between parallel context-loading (linear) and nested context-dependency (potentially exponential).

## Discussion

**Why the hypothesis persists.** Despite lacking formal derivation, exponential cognitive load explains a robust observation: developers strongly prefer consolidated changes, and scattered changes feel *disproportionately* difficult. The hypothesis provides a quantitative framework for this observation. Whether the mechanism is truly exponential or merely superlinear, the qualitative implication is the same: reducing discontinuities has increasing marginal returns.

**Connection to AAT's deliberation cost.** The #der-deliberation-cost framework formalizes the cost of reasoning before acting. Context switches during implementation are a form of deliberation cost — the agent must reason about how changes in one location affect another. When the changes are independent, this deliberation is parallelizable (each change can be understood locally). When they interact, deliberation becomes sequential and potentially recursive: understanding change A requires understanding change B, which may require understanding change C. This recursive dependency structure is what could produce genuine exponential scaling.

**Discontinuity hierarchy.** *[Discussion — taxonomy, not derived.]* Not all discontinuities are equal. The cost per boundary crossing increases with the type of boundary:

1. *Lexical*: Symbol must be found elsewhere in the same file
2. *File*: Must open another file and load its context
3. *Module*: Must understand another module's conventions, invariants, and vocabulary
4. *Service*: Must understand another service's API, data model, and failure modes
5. *Network*: Must trace through network calls, serialization, and distributed state

Each level roughly doubles the context-loading cost (the $k$ factor increases with boundary type). This is a heuristic observation, not a measured result — the actual cost ratios are an empirical question. A first-pass git-history measurement (below) finds support for the exponential *form* at file/directory-level crossings, with a fitted per-discontinuity penalty $\alpha \approx 0.118$ ($k \approx 1.118$) for normal-scale development; whether the doubling-*per-boundary-type* heuristic holds is untested.

**A first-pass git-history measurement of $\alpha$.** *[Empirical Claim — heuristic tier; single-repository, estimated-time.]* A repository-mining study fits the four candidate functional forms — linear $T = T_{\text{base}} + \beta d$, exponential $T = T_{\text{base}}(1+\alpha)^d$, logarithmic, and power-law — against per-commit data. The corpus was $229$ commits from a single repository (the Sapientia project, documentation-heavy rather than code-heavy). For each commit the discontinuity score was computed as $d = (\text{file transitions}) + 2 \cdot (\text{directory transitions})$, and comprehension/implementation time was *estimated heuristically* from the commit's lines-changed and files-touched (not directly measured — there is no instrumented developer-time signal). The distribution is bimodal: $\approx 95\%$ of commits have $d \le 51$ while a $\approx 5\%$ tail of bulk/batch commits ($d \gt 100$, mass file additions) dominates the raw fit and is what makes a logarithmic form appear to win on the unfiltered data. Restricting to normal-scale development ($d \le 25$, $N = 205$), the exponential form fits best with $\alpha \approx 0.118$ ($k \approx 1.118$; $R^2 \approx 0.52$) — each discontinuity adding $\approx 11.8\%$ to the estimated time, so $5$ discontinuities give a $\approx 1.6\times$ multiplier and $20$ give $\approx 8.6\times$. At the wider $d \le 100$ window ($N = 218$) the exponential fit is stronger ($R^2 \approx 0.72$) but the fitted penalty is smaller ($\alpha \approx 0.063$), so the precise value of $\alpha$ is sensitive to the outlier-filtering window. The fitted $\alpha \in [0.06, 0.12]$ range sits inside the $0.1$–$0.3$ band that working-memory and context-switching cognitive-science estimates (Miller's $7\pm2$ chunks; Parnin-Rugaber interruption-recovery; Leroy attention-residue) would predict.

Honest tier: this is *heuristic* corroboration of the exponential *form*, not a validated value of $\alpha$. The binding limitations are (i) time was estimated from a LOC/files heuristic rather than measured, (ii) a single, atypical (documentation-heavy) repository, (iii) a modest $R^2 \approx 0.52$ in the cited normal-development window, and (iv) $\alpha$'s dependence on the filtering window. It supports treating the exponential form as the right first model and $k \approx 1.1$–$1.12$ as a plausible normal-development order of magnitude; it does not establish $\alpha$ to two significant figures, and it does not bear on the count-vs-dependency-structure question that is this hypothesis's central open issue.

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

- Provenance / reproducibility for the $\alpha \approx 0.118$ measurement reported in the Discussion: the repository-mining toolkit, the $229$-commit dataset, the per-subset fits ($d \le 25$ / $d \le 50$ / $d \le 100$ / all-data), and the outlier analysis live in `02-tst-core/empirical-discontinuity/` (`analyze_git_history.py`, `analyze_outliers.py`, `FINDINGS.md`, `METHODOLOGY.md`). The body states the measurement, its scope, and its honest tier self-contained; this is the reproducibility source, to be released as a citable code/data supplement at publication. The toolkit's framing references the legacy FP-012 first-principles label for this hypothesis.
- The key open question is empirical: does the cost scale with discontinuity *count* (as stated) or with discontinuity *dependency structure* (as AAT's deliberation-cost framework suggests)? These make different predictions: the count model says 10 independent scattered changes are as hard as 10 interdependent ones; the structure model says the independent case is much easier. This is testable.
- For AI agents, context-switch cost may have a different profile than for humans. LLMs can hold large contexts but may have difficulty with *deep* reasoning chains. This suggests the structure-dependent model (where chain depth matters more than context breadth) may be especially relevant for AI agents.
- If the exponential form holds, it has strong architectural implications: any design that reduces the number of boundary crossings for typical features is worth disproportionate investment. This amplifies #der-change-investment far beyond the linear model.
- TST's notation $k^{\text{discontinuities}}$ uses "discontinuities" loosely. A more precise formulation would count boundary crossings weighted by boundary type ( #def-discontinuity-distance), or better yet, measure the depth of the dependency chain among the scattered changes.
- A formal route from the count-vs-structure open question above to a structure-sensitive operator scaling is sketched in `spikes/spike-transient-dependency-amplification.md`: cost scales with the operator norm of a finite-horizon product $\lVert J_{F,d}\cdots J_{F,1}\rVert$ of feature-local Jacobians rather than with raw discontinuity count. The spike's affine sub-scope recovers $k^d$ as a uniform-per-block-gain special case (each discontinuity contributes the same $k$), which preserves this hypothesis as a scalar approximation while upgrading the underlying theory to dependency-structure-sensitive form. Promotion to a derived TST result is blocked on the spike's open obligations: formal $\widehat J_F$ construction from TST quantities, nonlinear-remainder bounds, cyclic-dependency treatment via SCC condensation, and empirical validation.
