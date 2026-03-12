---
slug: system-coupling
type: definition
status: axiomatic
depends:
  - atomic-changeset
---

# Definition: System Coupling

The probability that a change to one module will require a change to another.

## Formal Expression

*[Definition (system-coupling)]*

$$\text{coupling}(m_i, m_j) = P(\text{change}(m_j) \mid \text{change}(m_i))$$

where $\text{change}(m)$ means module $m$ is part of the #atomic-changeset for some feature.

This is an empirical quantity — it is estimated from observed co-change patterns, not from static analysis of the code structure.

## Epistemic Status

Definitional. The conditional probability is a standard quantity. Its value for a given system is empirical, estimated from git history or similar records of co-change.

## Discussion

Coupling defined this way captures the *actual* change propagation in a system, which may differ from what static dependency analysis predicts. Two modules with no compile-time dependency can still be highly coupled if features routinely require changing both. Conversely, a module that imports another heavily may show low coupling if the interface is stable.

In ACT terms, coupling is a property of the environment's causal structure as experienced by the agent: changing module $i$ (an intervention) tends to require changing module $j$ (a consequence). This is genuinely causal, not just correlational — the agent performs $do(\text{change}(m_i))$ and observes whether $m_j$ must also change. Git history provides the interventional data ( #causal-discovery-from-git).

## Working Notes

- The definition is asymmetric: $P(\text{change}(m_j) \mid \text{change}(m_i))$ need not equal $P(\text{change}(m_i) \mid \text{change}(m_j))$. This asymmetry is informative — it reveals directional dependency.
- Coupling is feature-type-dependent. A module pair might be tightly coupled for UI features and uncoupled for backend features. The unconditional estimate from git history is an average over the historical feature distribution, which may not represent future features. This connects to the uniform-feature-rate assumption in #change-expectation-baseline.
- The interventional interpretation is stronger than correlational. If two modules always change in the same commit, that could be coupling OR could be convention (developer habit of bundling). Distinguishing requires looking at *whether the feature required both changes* vs. *whether the developer chose to include both*. Atomic commits help; large PRs hurt.

*(Descended from TST D-06.)*
