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

This is the first explicit narrowing in the volume's cascade of scope conditions. The **agency scope** restricts the adaptive scope ( #scope-adaptive-system) to systems whose actions carry Pearl-level-2 causal contrast — that is, at least two actions exist whose *interventional* outcome distributions differ. Two conditions are added: the action space has at least binary cardinality ($\lvert\mathcal{A}\rvert \geq 2$ — the agent can choose), and at least one pair of distinct actions has measurably different interventional consequences (the choices make a difference).

Why the contrast condition matters and binary choice alone is insufficient: if two available actions yield identical outcome distributions, an agent gains no interventional contrast from preferring one over the other — it cannot learn which action produces which effect, because the effects coincide. The Pearl-level-2 contrast condition ( #def-pearl-causal-hierarchy) guarantees at least one meaningful interventional difference, which is precisely what #der-loop-interventional-access needs to convert the feedback loop into a source of causal data.

The agency scope is the minimum required for Sections II (purposeful agents) and III (composition). Everything that relies on the agent acting-with-effect — the objective $O_t$, the strategy $\Sigma_t$, the orient cascade, the composition machinery — descends from this scope. Inhabitants include thermostats, Kalman filters with control inputs, reinforcement-learning agents, military commanders, software developers, and AI agents with tool use; all are instances of the same formal framework distinguished only by where they sit on the agent spectrum ( #def-agent-spectrum).

Two failure modes are explicitly outside agency but inside the adaptive scope: *passive observers* (action space too small to matter, $\lvert\mathcal{A}\rvert \lt 2$) and *nominal agents* (choices exist but produce no measurable interventional difference). For these, all of Section I's machinery applies, but Sections II and III do not — they can model, but they cannot learn causal structure or rationally plan against it.

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
- **Nominal agents** ($P(o \mid do(a)) = P(o \mid do(a'))$ for all $a, a'$): Have choices that make no difference. Can estimate but cannot learn causal structure. Same as passive observers for AAT's purposes: adaptive only.

**Why causal effect matters.** Binary choice ($\lvert\mathcal A\rvert \geq 2$) is necessary but not sufficient. Two actions that produce identical outcome distributions provide no interventional contrast — the agent cannot learn which action produces which effect because the effects are the same. The causal-effect condition ensures at least one meaningful contrast exists, which is what #der-loop-interventional-access needs to generate Level 2 data.

**Relationship to downstream segments.** Every segment that relies on the agent acting-with-effect depends on this scope: purposeful-agent machinery ($O_t$, $\Sigma_t$, orient cascade) in Section II; composition machinery (sub-agents acting jointly) in Section III. Downstream segments reference `#scope-agency` when they assert "the agent can act" as a prerequisite.
