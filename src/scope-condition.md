---
slug: scope-condition
type: scope
status: axiomatic
depends:
  - agent-environment
  - observation-function
  - action-transition
---

# Scope: Scope Condition

ACT applies wherever there is an agent that observes, acts with at least a binary choice, and faces residual uncertainty about its environment.

## Formal Expression

*[Definition (scope-condition)]*

$$\mathcal{S}_{\text{ACT}} = \left\{(\text{Agent}, \Omega) \;:\; \mathcal{O} \neq \emptyset, \;\; \lvert\mathcal{A}\rvert \geq 2, \;\; H(\Omega_t \mid \mathcal{C}_t) \gt 0 \right\}$$

Three conditions jointly define ACT's domain:

1. **Observations exist**: $\mathcal{O} \neq \emptyset$ — the agent has some perceptual channel to the environment ( #observation-function)
2. **At least binary choice**: $\lvert\mathcal{A}\rvert \geq 2$ — the agent can choose between at least two actions ( #action-transition)
3. **Residual uncertainty persists**: $H(\Omega_t \mid \mathcal C_t) \gt 0$ — the environment is not fully determined by the interaction history

## Epistemic Status

This is a *scope definition* — it draws the boundary around the systems ACT addresses. The three conditions are not derived; they are the minimal requirements for the adaptive machinery that follows to be non-vacuous. The action-space requirement ($\lvert\mathcal{A}\rvert \geq 2$) is the most substantive choice: it ensures at least one interventional contrast, which is the minimal condition for causal learning and exploration.

## Discussion

**What is included.** The scope is deliberately broad. It encompasses thermostats (minimal agent, binary action), Kalman filters (continuous observation, parametric model), military commanders (rich model, explicit strategy), software developers (epistemic agents modifying their own observation infrastructure), and AI agents (100% context turnover, same formal structure). These are not analogies — they are instances of the same formal framework at different points in the agent spectrum ( #agent-spectrum).

**What is excluded.** Three classes fall outside ACT's scope:

- **Passive observers** ($\lvert\mathcal{A}\rvert \lt 2$): An entity that observes but cannot act has no interventional contrast and cannot learn causal structure. It can correlate but not intervene.
- **Closed-form systems** ($H(\Omega_t \mid \mathcal C_t) = 0$): When the agent has complete knowledge of the environment, there is no uncertainty to adapt to. Optimal control over known dynamics is a solved problem outside ACT's concerns.
- **Pure computation** ($\mathcal{O} = \emptyset$): A system with no observation channel — e.g., a mathematical proof engine operating on axioms alone — has no agent-environment boundary in ACT's sense.

**Why $\lvert\mathcal{A}\rvert \geq 2$.** A single available action eliminates choice, and with it the possibility of interventional contrast. The agent cannot compare outcomes under different actions, which is the minimal requirement for Level 2 causal reasoning ( #pearl-causal-hierarchy). Binary choice is sufficient: a single A/B contrast supports causal learning.
