---
slug: changeset-size-principle
type: empirical
status: empirical
depends:
  - atomic-changeset
  - implementation-time
  - comprehension-time
---

# Changeset Size Principle

Implementation time is proportional to the size of the atomic changeset.

## Formal Expression

*[Empirical Claim (changeset-size-principle)]*

$$t_{\text{impl}}(F) \propto |\text{changeset}(F)|$$

where $|\text{changeset}|$ measures lines changed, files touched, or modules affected (see #atomic-changeset), excluding generated code.

### Corollary: Comprehension Follows Changeset Size

*[Hypothesis (comprehension-follows-changeset)]*

$$t_{\text{comp}}(F) \propto |\text{changeset}(F)|$$

Understanding a feature that touched 20 files requires comprehending 20 contexts. This creates a double penalty for unnecessarily large changesets: both implementation time and comprehension time scale with size. Architecture that minimizes changeset size for typical features thus optimizes both dimensions of #dual-optimization simultaneously.

## Epistemic Status

*Empirical.* The implementation-time proportionality is nearly tautological — more changes take more time. Its strength is as a simplifying assumption that enables quantitative reasoning: if you can estimate changeset size, you can estimate implementation time. The proportionality constant is codebase-specific and not derived.

The comprehension corollary is a *hypothesis* — weaker than the implementation claim. Comprehension cost depends not just on how many files are touched but on how complex each context is and how they relate to each other. The proportionality is a useful first approximation that likely holds across orders of magnitude (1 file vs 100 files) but may break down for fine comparisons (15 files vs 18 files). The #change-proximity-principle addresses the structure-dependent component that changeset size alone misses.

## Discussion

**Architecture as temporal optimization.** The principle suggests a mechanism for why architecture matters: good architecture minimizes *future* changeset sizes, not current ones. A refactoring that touches 15 files now but ensures future features touch only 1 file (instead of 3) is justified when the savings exceed the cost — which is precisely the #change-investment threshold. This reframes architectural decisions as temporal investments, though the reduction to changeset size captures only one dimension of architectural quality.

**Connection to ACT.** The changeset is the observable trace of the agent's intervention in the environment. Changeset size is a proxy for the *scope* of the intervention. Larger interventions require more of the agent's time (both to plan and to execute), which is the implementation-time proportionality. They also require more of the *next* agent's time to comprehend (the corollary), which matters under the turnover multiplier in #dual-optimization.

## Working Notes

- The proportionality hides important structure. A 100-line change in one file and 10 one-line changes across 10 files have similar $|\text{changeset}|$ but very different costs. The proximity principle ( #change-proximity-principle) captures this difference. The size principle is the first-order term; proximity is the correction.
- "Lines changed" vs "files touched" vs "modules affected" are different measures that may give different proportionality constants. Which measure best predicts time? This is an empirical question with practical implications for estimation and for evaluating architectures.
- The comprehension corollary assumes roughly equal per-context comprehension cost. In practice, some files are much harder to understand than others. A single change in a complex state machine may cost more comprehension time than changes across 10 simple CRUD endpoints. #conceptual-alignment captures part of this — well-aligned modules are cheaper to comprehend per unit.

*(Descended from TST T-08, C-08.1.)*
