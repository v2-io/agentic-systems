---
slug: scope-agency
type: scope
status: axiomatic
depends:
  - scope-adaptive-system
  - def-action-transition
stage: claims-verified
---

# Scope: Agency

The agency scope narrows AAD's adaptive scope ( #scope-adaptive-system) to systems whose actions carry Pearl-level-2 causal contrast — distinct actions produce distinct interventional outcome distributions. This is the scope required for Sections II (purposeful agents) and III (composition); every segment that relies on the agent acting-with-effect depends on it.

## Formal Expression

*[Scope (scope-agency)]*

$$\mathcal S_\text{agency} = \mathcal S_\text{adaptive} \;\cap\; \left\{(\text{Agent}, \Omega) \;:\; \lvert\mathcal A\rvert \geq 2, \;\; \exists\, a \neq a' \text{ s.t. } P(o \mid do(a)) \neq P(o \mid do(a')) \right\}$$

Two conditions added to those of #scope-adaptive-system:

3. **At least binary choice**: $\lvert\mathcal A\rvert \geq 2$ — the agent can choose between at least two actions ( #def-action-transition)
4. **At least one action has causal effect**: there exist distinct actions $a, a'$ whose interventional outcome distributions differ (where $do(\cdot)$ is Pearl's intervention operator; see #def-pearl-causal-hierarchy) — the agent's choices make a difference to what it can observe

These are required for the adaptive loop to generate interventional data ( #der-loop-interventional-access), for the causal hierarchy requirement ( #der-causal-hierarchy-requirement) to be well-posed, and for the purposeful-agent machinery of Section II ($O_t$, $\Sigma_t$, the orient cascade) to be non-vacuous. Section III's composition theory inherits this requirement.

## Epistemic Status

*Axiomatic.* This is a scope definition — it names the boundary around systems whose behavior can be analyzed with Section II/III machinery. The conditions are not derived; they are the minimal additions to $\mathcal S_\text{adaptive}$ under which interventional data exist at all.

## Discussion

**What is included.** Systems whose actions make a causal difference: thermostats, Kalman filters with control inputs, RL agents, military commanders, software developers, AI agents with tool use. These are instances of the same formal framework at different points in the agent spectrum ( #def-agent-spectrum).

**What is in adaptive scope but excluded from agency.**

- **Passive observers** ($\lvert\mathcal A\rvert \lt 2$): Can observe and model, but cannot intervene. #scope-adaptive-system applies; the causal-information and purposeful-agent results do not.
- **Nominal agents** ($P(o \mid do(a)) = P(o \mid do(a'))$ for all $a, a'$): Have choices that make no difference. Can estimate but cannot learn causal structure. Same as passive observers for AAD's purposes: adaptive only.

**Why causal effect matters.** Binary choice ($\lvert\mathcal A\rvert \geq 2$) is necessary but not sufficient. Two actions that produce identical outcome distributions provide no interventional contrast — the agent cannot learn which action produces which effect because the effects are the same. The causal-effect condition ensures at least one meaningful contrast exists, which is what #der-loop-interventional-access needs to generate Level 2 data.

**Relationship to downstream segments.** Every segment that relies on the agent acting-with-effect depends on this scope: purposeful-agent machinery ($O_t$, $\Sigma_t$, orient cascade) in Section II; composition machinery (sub-agents acting jointly) in Section III. Downstream segments reference `#scope-agency` when they assert "the agent can act" as a prerequisite.
