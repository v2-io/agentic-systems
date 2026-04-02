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

ACT applies wherever there is an agent that observes, acts with genuine causal effect on its environment, and faces residual uncertainty.

## Formal Expression

*[Definition (scope-condition)]*

$$\mathcal S_\text{ACT} = \left\{(\text{Agent}, \Omega) \;:\; \mathcal O \neq \emptyset, \;\; \lvert\mathcal A\rvert \geq 2, \;\; \exists\, a \neq a' \text{ s.t. } P(o \mid do(a)) \neq P(o \mid do(a')), \;\; H(\Omega_t \mid \mathcal C_t) \gt 0 \right\}$$

Four conditions jointly define ACT's domain:

1. **Observations exist**: $\mathcal O \neq \emptyset$ — the agent has some perceptual channel to the environment ( #observation-function)
2. **At least binary choice**: $\lvert\mathcal A\rvert \geq 2$ — the agent can choose between at least two actions ( #action-transition)
3. **At least one action has causal effect**: there exist distinct actions $a, a'$ whose interventional outcome distributions differ (where $do(\cdot)$ is Pearl's intervention operator; see #pearl-causal-hierarchy) — the agent's choices make a difference to what it can observe. This is the minimal condition for the adaptive loop to generate interventional data ( #loop-interventional-access)
4. **Residual uncertainty persists**: $H(\Omega_t \mid \mathcal C_t) \gt 0$ — the environment is not fully determined by the interaction history

## Epistemic Status

This is a *scope definition* — it draws the boundary around the systems ACT addresses. The four conditions are not derived; they are the minimal requirements for the adaptive machinery that follows to be non-vacuous. Condition 3 (causal effect) is the most substantive addition: it ensures the agent's actions generate genuine interventional data, making the loop a Level 2 engine ( #loop-interventional-access) and the causal hierarchy requirement ( #causal-hierarchy-requirement) well-posed. An agent with nominal actions that have no causal effect on observations is formally outside ACT's scope — the theory is about agency, not passive estimation.

## Discussion

**What is included.** The scope is broad but not vacuous. It encompasses thermostats (minimal agent, binary action with causal effect on temperature), Kalman filters with control inputs (continuous observation, parametric model, actions affect state), military commanders (rich model, explicit strategy, actions shape the battlespace), software developers (epistemic agents modifying their own observation infrastructure through code changes), and AI agents with tool use (100% context turnover, actions affect the environment through tool calls). These are not analogies — they are instances of the same formal framework at different points in the agent spectrum ( #agent-spectrum).

**What is excluded.** Four classes fall outside ACT's scope:

- **Passive observers** ($\lvert\mathcal A\rvert \lt 2$): An entity that observes but cannot act has no interventional contrast and cannot learn causal structure. It can correlate but not intervene. Note: Section I's adaptive machinery (mismatch, gain, tempo, persistence) still applies to passive trackers — the mismatch signal, update gain, and persistence condition do not require causal effect. What passive observers lack is access to the causal-information results (CIY, #loop-interventional-access) that require interventional contrast.
- **Nominal agents** ($P(o \mid do(a)) = P(o \mid do(a'))$ for all $a, a'$): An entity with multiple actions that all produce the same outcome distribution has choices that make no difference. Its actions are nominal, not causal. The adaptive loop generates no interventional information. Such systems can estimate (Bayesian filtering) but cannot learn causal structure or usefully plan. ACT is a theory of agency; agency requires that choices matter.
- **Closed-form systems** ($H(\Omega_t \mid \mathcal C_t) = 0$): When the agent has complete knowledge of the environment, there is no uncertainty to adapt to. Optimal control over known dynamics is a solved problem outside ACT's concerns.
- **Pure computation** ($\mathcal O = \emptyset$): A system with no observation channel — e.g., a mathematical proof engine operating on axioms alone — has no agent-environment boundary in ACT's sense.

**Why causal effect matters.** Binary choice ($\lvert\mathcal A\rvert \geq 2$) is necessary but not sufficient. Two actions that produce identical outcome distributions provide no interventional contrast — the agent cannot learn which action produces which effect because the effects are the same. The causal-effect condition (condition 3) ensures at least one meaningful contrast exists, which is what #loop-interventional-access needs to generate Level 2 data. A Kalman filter with a control input (actions affect the state) is in full scope; a Kalman filter estimating a passive signal (no control input) is in scope for the adaptive machinery (Section I's mismatch, gain, tempo, persistence results apply) but outside scope for the causal-information results that require interventional contrast.
