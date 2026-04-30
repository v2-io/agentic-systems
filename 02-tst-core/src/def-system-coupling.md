---
slug: def-system-coupling
type: definition
status: axiomatic
depends:
  - def-atomic-changeset
---

# Definition: System Coupling

The probability that a change to one module will require a change to another.

## Formal Expression

*[Definition (system-coupling)]*

$$\text{coupling}(m_i, m_j) = P(\text{change}(m_j) \mid \text{change}(m_i))$$

where $\text{change}(m)$ means module $m$ is part of the #def-atomic-changeset for some feature.

This is an empirical quantity — it is estimated from observed co-change patterns, not from static analysis of the code structure.

## Epistemic Status

Definitional. The conditional probability is a standard quantity. Its value for a given system is empirical, estimated from git history or similar records of co-change.

## Discussion

Coupling defined this way captures the *actual* change propagation in a system, which may differ from what static dependency analysis predicts. Two modules with no compile-time dependency can still be highly coupled if features routinely require changing both. Conversely, a module that imports another heavily may show low coupling if the interface is stable.

In AAD terms, coupling targets a property of the environment's causal structure as experienced by the agent: changing module $i$ (an intervention) tends to require changing module $j$ (a consequence). Two claims need to be distinguished — the first is secure, the second conditional:

**Secured: individual commits are interventions.** Developers performing code changes are executing genuine $do$-operations on the codebase ( #obs-software-epistemic-properties, P3). Each commit is an intervention in Pearl's sense, and git records the intervention-outcome pair (which module changed, which subsequent changes followed). This is not in dispute ( #hyp-causal-discovery-from-git Epistemic Status).

**Conditional: aggregated co-change estimates are causal.** Whether $P(\text{change}(m_j) \mid \text{change}(m_i))$ estimated from git history approximates the true causal effect $P(\text{change}(m_j) \mid do(\text{change}(m_i)))$ depends on the confounder regime ( #hyp-causal-discovery-from-git identifies three classes of confounders: shared requirements, convention-driven bundling, developer knowledge state). The causal interpretation is strongest in specific regimes:

- **Atomic commits with explicit feature scope**: feature-scoped atomic commits isolate the interventional signal from bundling confounders.
- **Asymmetric co-change frequency**: $P(j \mid i) \gg P(i \mid j)$ survives common-cause confounding (which would produce symmetric co-change), giving evidence of directed causal linkage $i \to j$.
- **Intervention contrast**: commits changing $i$ without $j$ vs. with $j$, conditioned on available confounders, provide weak-but-nonzero interventional contrast.

Outside these regimes, the coupling estimate is better interpreted as a descriptive statistic of co-change — still useful for prediction, but not a secured causal parameter. See #hyp-causal-discovery-from-git for the full regime analysis and the research program for strengthening the causal interpretation via confounder adjustment.

## Working Notes

- The definition is asymmetric: $P(\text{change}(m_j) \mid \text{change}(m_i))$ need not equal $P(\text{change}(m_i) \mid \text{change}(m_j))$. This asymmetry is informative — it reveals directional dependency.
- Coupling is feature-type-dependent. A module pair might be tightly coupled for UI features and uncoupled for backend features. The unconditional estimate from git history is an average over the historical feature distribution, which may not represent future features. This connects to the uniform-feature-rate assumption in #der-change-expectation-baseline.
- The interventional interpretation is stronger than correlational. If two modules always change in the same commit, that could be coupling OR could be convention (developer habit of bundling). Distinguishing requires looking at *whether the feature required both changes* vs. *whether the developer chose to include both*. Atomic commits help; large PRs hurt.
