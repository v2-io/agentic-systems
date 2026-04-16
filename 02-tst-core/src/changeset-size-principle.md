---
slug: changeset-size-principle
type: empirical
status: empirical
depends:
  - atomic-changeset
  - implementation-time
  - comprehension-time
---

# Empirical: Changeset Size Principle

Implementation time is proportional to the size of the atomic changeset.

## Formal Expression

*[Empirical Claim (changeset-size-principle)]*

$$t_{\text{impl}}(F) \propto \lvert\text{changeset}(F)\rvert$$

where $\lvert\text{changeset}\rvert$ measures lines changed, files touched, or modules affected (see #atomic-changeset), excluding generated code.

### Corollary: Comprehension Follows Changeset Size

*[Hypothesis (comprehension-follows-changeset)]*

$$t_{\text{comp}}(F) \propto \lvert\text{changeset}(F)\rvert$$

Understanding a feature that touched 20 files requires comprehending 20 contexts. This creates a double penalty for unnecessarily large changesets: both implementation time and comprehension time scale with size. Architecture that minimizes changeset size for typical features thus optimizes both dimensions of #dual-optimization simultaneously.

## Epistemic Status

*Empirical.* The implementation-time proportionality is nearly tautological — more changes take more time. Its strength is as a simplifying assumption that enables quantitative reasoning: if you can estimate changeset size, you can estimate implementation time. The proportionality constant is codebase-specific and not derived.

The comprehension corollary is a *hypothesis* — weaker than the implementation claim. Comprehension cost depends not just on how many files are touched but on how complex each context is and how they relate to each other. The proportionality is a useful first approximation that likely holds across orders of magnitude (1 file vs 100 files) but may break down for fine comparisons (15 files vs 18 files). The #change-proximity-principle addresses the structure-dependent component that changeset size alone misses.

## Discussion

**Architecture as temporal optimization.** The principle suggests a mechanism for why architecture matters: good architecture minimizes *future* changeset sizes, not current ones. A refactoring that touches 15 files now but ensures future features touch only 1 file (instead of 3) is justified when the savings exceed the cost — which is precisely the #change-investment threshold. This reframes architectural decisions as temporal investments, though the reduction to changeset size captures only one dimension of architectural quality.

**Connection to AAD.** The changeset is the observable trace of the agent's intervention in the environment. Changeset size is a proxy for the *scope* of the intervention. Larger interventions require more of the agent's time (both to plan and to execute), which is the implementation-time proportionality. They also require more of the *next* agent's time to comprehend (the corollary), which matters under the turnover multiplier in #dual-optimization.

**Architectural patterns that reduce future changeset size.** *[Discussion — the principle's practical force lies in predicting changeset size from architecture.]*

Patterns that tend to reduce changeset size for typical features:
- *Centralized configuration*: changing a behavior requires modifying one location instead of many scattered constants
- *Well-defined interfaces*: changes behind an interface don't propagate to callers
- *Domain-aligned module boundaries* ( #conceptual-alignment): features map to single modules rather than scattering across many

Patterns that tend to increase changeset size:
- *Scattered magic numbers/strings*: every behavior change requires a multi-site hunt
- *Leaky abstractions*: callers depend on implementation details, so internal changes cascade outward
- *Cross-cutting concerns without infrastructure*: logging, auth, or error-handling code duplicated across modules rather than centralized

*[Discussion — these patterns are well-established in software engineering practice. The contribution of the changeset-size principle is not identifying them but explaining *why* they matter: they determine the proportionality constant between features and implementation time. Whether a pattern is "good" reduces to whether it shrinks future changesets for probable features.]*

**Historical validation via git.** *[Discussion — empirical approach, partially operationalized.]* The proportionality is testable from git history: for a given codebase, measure changeset size (lines, files, or modules) and correlate with implementation time (commit-to-merge duration, or gap between first and last commit in a feature branch). The `empirical-discontinuity/` toolkit demonstrates this approach for discontinuity counting; extending it to changeset size would test the proportionality directly. Prior work on change-impact analysis (MacCormack et al. 2006, "Propagation Cost") provides related empirical methodology.

## Working Notes

- The proportionality hides important structure. A 100-line change in one file and 10 one-line changes across 10 files have similar $\lvert\text{changeset}\rvert$ but very different costs. The proximity principle ( #change-proximity-principle) captures this difference. The size principle is the first-order term; proximity is the correction.
- "Lines changed" vs "files touched" vs "modules affected" are different measures that may give different proportionality constants. Which measure best predicts time? This is an empirical question with practical implications for estimation and for evaluating architectures.
- The comprehension corollary assumes roughly equal per-context comprehension cost. In practice, some files are much harder to understand than others. A single change in a complex state machine may cost more comprehension time than changes across 10 simple CRUD endpoints. #conceptual-alignment captures part of this — well-aligned modules are cheaper to comprehend per unit.

*(Descended from TST T-08, C-08.1.)*
