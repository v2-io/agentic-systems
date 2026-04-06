---
slug: scope-condition
type: scope
status: axiomatic
depends:
  - agent-environment
  - observation-function
  - action-transition
stage: claims-verified
---

# Scope: Scope Condition

ACT's scope is defined by progressive narrowing. The broadest applicable scope — any system that observes under uncertainty — supports Section I's adaptive machinery. Adding causal action unlocks the interventional and purposeful results of Sections II and III.

## Formal Expression

*[Definition (scope-condition)]*

### Adaptive scope (Section I)

$$\mathcal S_\text{adaptive} = \left\{(\text{Agent}, \Omega) \;:\; \mathcal O \neq \emptyset, \;\; H(\Omega_t \mid \mathcal C_t) \gt 0 \right\}$$

Two conditions:

1. **Observations exist**: $\mathcal O \neq \emptyset$ — the system has some perceptual channel to the environment ( #observation-function)
2. **Residual uncertainty persists**: $H(\Omega_t \mid \mathcal C_t) \gt 0$ — the environment is not fully determined by the interaction history

This is sufficient for the mismatch signal ( #mismatch-signal), update gain ( #update-gain), adaptive tempo ( #adaptive-tempo), the persistence condition ( #persistence-condition), and all of Section I's adaptive dynamics. A Kalman filter estimating a passive signal, a passive Bayesian learner, and any system that observes and updates a model under uncertainty are within this scope.

### Agency scope (Sections II and III)

$$\mathcal S_\text{agency} = \mathcal S_\text{adaptive} \;\cap\; \left\{(\text{Agent}, \Omega) \;:\; \lvert\mathcal A\rvert \geq 2, \;\; \exists\, a \neq a' \text{ s.t. } P(o \mid do(a)) \neq P(o \mid do(a')) \right\}$$

Two additional conditions, narrowing the adaptive scope:

3. **At least binary choice**: $\lvert\mathcal A\rvert \geq 2$ — the agent can choose between at least two actions ( #action-transition)
4. **At least one action has causal effect**: there exist distinct actions $a, a'$ whose interventional outcome distributions differ (where $do(\cdot)$ is Pearl's intervention operator; see #pearl-causal-hierarchy) — the agent's choices make a difference to what it can observe

These are required for the adaptive loop to generate interventional data ( #loop-interventional-access), for the causal hierarchy requirement ( #causal-hierarchy-requirement) to be well-posed, and for the purposeful-agent machinery of Section II ($O_t$, $\Sigma_t$, the orient cascade) to be non-vacuous. Section III's composition theory inherits this requirement.

## Epistemic Status

This is a *scope definition* — it draws the boundary around the systems each part of ACT addresses. The conditions are not derived; they are the minimal requirements for the associated machinery to be non-vacuous. The progressive structure reflects the theory's own architecture: Section I's adaptive results need only observations and uncertainty; Section II's purposeful results additionally need causal action.

## Discussion

**What is included.** The adaptive scope is broad: any system that observes under uncertainty. Passive Bayesian learners, Kalman filters (with or without control inputs), biological sensory systems. The agency scope narrows to systems whose actions make a causal difference: thermostats, Kalman filters with control inputs, RL agents, military commanders, software developers, AI agents with tool use. These are instances of the same formal framework at different points in the agent spectrum ( #agent-spectrum).

**What is excluded from both scopes.**

- **Closed-form systems** ($H(\Omega_t \mid \mathcal C_t) = 0$): When the agent has complete knowledge of the environment, there is no uncertainty to adapt to. Optimal control over known dynamics is a solved problem outside ACT's concerns.
- **Pure computation** ($\mathcal O = \emptyset$): A system with no observation channel — e.g., a mathematical proof engine operating on axioms alone — has no agent-environment boundary in ACT's sense.

**What is in adaptive scope but excluded from agency scope.**

- **Passive observers** ($\lvert\mathcal A\rvert \lt 2$): Can observe and model, but cannot intervene. Section I's adaptive machinery applies; the causal-information and purposeful-agent results do not.
- **Nominal agents** ($P(o \mid do(a)) = P(o \mid do(a'))$ for all $a, a'$): Have choices that make no difference. Can estimate but cannot learn causal structure. Same as passive observers for ACT's purposes: adaptive scope only.

**Why causal effect matters for the agency scope.** Binary choice ($\lvert\mathcal A\rvert \geq 2$) is necessary but not sufficient. Two actions that produce identical outcome distributions provide no interventional contrast — the agent cannot learn which action produces which effect because the effects are the same. The causal-effect condition ensures at least one meaningful contrast exists, which is what #loop-interventional-access needs to generate Level 2 data.
