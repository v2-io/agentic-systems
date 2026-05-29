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

This segment names AAT's broadest scope — the set of systems to which all of Part I's machinery applies. A system is in the **adaptive scope** if it satisfies two minimal conditions: it has some perceptual channel to its environment (a non-empty observation space, $\mathcal{O} \neq \emptyset$), and there is residual uncertainty about the environment given the full interaction history so far (the conditional entropy $H(\Omega_t \mid \mathcal{C}_t)$ is strictly positive).

These two conditions are the minimal requirements for the framework's adaptive machinery to be non-vacuous. They are sufficient to support the mismatch signal ( #def-mismatch-signal), the update-gain analysis ( #emp-update-gain), the adaptive-tempo construct ( #def-adaptive-tempo), the persistence condition ( #result-persistence-condition), and all of Part I's dynamics. Concrete inhabitants include Kalman filters estimating passive signals, passive Bayesian learners, and biological sensory systems — none of which need to *act* on their environment for Part I's results to apply to them.

What is excluded clarifies what the scope is doing. A system with full knowledge of the environment ($H(\Omega_t \mid \mathcal{C}_t) = 0$) is a closed-form optimal-control problem outside AAT's concerns. A system with no observation channel at all ($\mathcal{O} = \emptyset$ — e.g., a pure mathematical-proof engine working from axioms) has no agent-environment boundary in AAT's sense. Both edge cases sit *outside* the framework.

The scope is the broadest member of a cascade. Narrowing it by adding the requirement that the agent's actions carry Pearl-level-2 causal contrast — distinct actions yield distinct interventional distributions — produces the agency scope ( #scope-agency) and unlocks the interventional and purposeful results of Parts II and III. Adaptive-scope systems that fail the contrast condition are *passive observers* (no choice) or *nominal agents* (choices with no causal effect); for them, Part I's machinery applies but the later causal and purposeful results do not.

## Formal Expression

*[Scope (scope-adaptive-system)]*

$$\mathcal{S}_\text{adaptive} = \left\{(\text{Agent}, \Omega) \;:\; \mathcal{O} \neq \emptyset, \;\; H(\Omega_t \mid \mathcal{C}_t) \gt 0 \right\}$$

Two conditions:

1. **Observations exist**: $\mathcal{O} \neq \emptyset$ — the system has some perceptual channel to the environment ( #def-observation-function)
2. **Residual uncertainty persists**: $H(\Omega_t \mid \mathcal{C}_t) \gt 0$ — the environment is not fully determined by the interaction history

This is sufficient for the mismatch signal ( #def-mismatch-signal), update gain ( #emp-update-gain), adaptive tempo ( #def-adaptive-tempo), the persistence condition ( #result-persistence-condition), and all of Part I's adaptive dynamics. A Kalman filter estimating a passive signal, a passive Bayesian learner, and any system that observes and updates a model under uncertainty are within this scope.

## Epistemic Status

*Axiomatic.* This is a scope definition — it draws the boundary around the systems Part I addresses. The two conditions are not derived; they are the minimal requirements for the adaptive machinery to be non-vacuous.

## Discussion

**What is included.** Any system that observes under uncertainty. Passive Bayesian learners, Kalman filters (with or without control inputs), biological sensory systems. These are Part I's subjects — instances that build $M_t$ through mismatch-driven updates without necessarily acting to influence their environment.

**What is excluded.**

- **Closed-form systems** ($H(\Omega_t \mid \mathcal{C}_t) = 0$): When the agent has complete knowledge of the environment, there is no uncertainty to adapt to. Optimal control over known dynamics is a solved problem outside AAT's concerns.
- **Pure computation** ($\mathcal{O} = \emptyset$): A system with no observation channel — e.g., a mathematical proof engine operating on axioms alone — has no agent-environment boundary in AAT's sense.

**Narrowing to agency.** Adding causal action unlocks the interventional and purposeful results of Parts II and III. The agency scope ( #scope-agency) is the intersection of $\mathcal{S}_\text{adaptive}$ with the condition that actions carry Pearl-level-2 contrast: distinct actions produce distinct interventional outcome distributions. Adaptive-scope systems that remain outside agency are *passive observers* (no choice) or *nominal agents* (choices with no causal effect); for both, Part I's machinery applies but the causal-information and purposeful-agent results do not.
