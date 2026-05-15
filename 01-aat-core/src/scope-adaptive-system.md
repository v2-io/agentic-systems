---
slug: scope-adaptive-system
type: scope
status: axiomatic
depends:
  - def-agent-environment
  - def-observation-function
  - def-chronica
stage: claims-verified
---

# Scope: Adaptive System

AAD's broadest scope: any system that observes an uncertain environment supports Section I's adaptive machinery. Adding causal action narrows to the agency scope ( #scope-agency); this segment names the outer scope from which agency is a restriction.

## Formal Expression

*[Scope (scope-adaptive-system)]*

$$\mathcal S_\text{adaptive} = \left\{(\text{Agent}, \Omega) \;:\; \mathcal O \neq \emptyset, \;\; H(\Omega_t \mid \mathcal C_t) \gt 0 \right\}$$

Two conditions:

1. **Observations exist**: $\mathcal O \neq \emptyset$ — the system has some perceptual channel to the environment ( #def-observation-function)
2. **Residual uncertainty persists**: $H(\Omega_t \mid \mathcal C_t) \gt 0$ — the environment is not fully determined by the interaction history

This is sufficient for the mismatch signal ( #def-mismatch-signal), update gain ( #emp-update-gain), adaptive tempo ( #def-adaptive-tempo), the persistence condition ( #result-persistence-condition), and all of Section I's adaptive dynamics. A Kalman filter estimating a passive signal, a passive Bayesian learner, and any system that observes and updates a model under uncertainty are within this scope.

## Epistemic Status

*Axiomatic.* This is a scope definition — it draws the boundary around the systems Section I addresses. The two conditions are not derived; they are the minimal requirements for the adaptive machinery to be non-vacuous.

## Discussion

**What is included.** Any system that observes under uncertainty. Passive Bayesian learners, Kalman filters (with or without control inputs), biological sensory systems. These are Section I's subjects — instances that build $M_t$ through mismatch-driven updates without necessarily acting to influence their environment.

**What is excluded.**

- **Closed-form systems** ($H(\Omega_t \mid \mathcal C_t) = 0$): When the agent has complete knowledge of the environment, there is no uncertainty to adapt to. Optimal control over known dynamics is a solved problem outside AAD's concerns.
- **Pure computation** ($\mathcal O = \emptyset$): A system with no observation channel — e.g., a mathematical proof engine operating on axioms alone — has no agent-environment boundary in AAD's sense.

**Narrowing to agency.** Adding causal action unlocks the interventional and purposeful results of Sections II and III. The agency scope ( #scope-agency) is the intersection of $\mathcal S_\text{adaptive}$ with the condition that actions carry Pearl-level-2 contrast: distinct actions produce distinct interventional outcome distributions. Adaptive-scope systems that remain outside agency are *passive observers* (no choice) or *nominal agents* (choices with no causal effect); for both, Section I's machinery applies but the causal-information and purposeful-agent results do not.
