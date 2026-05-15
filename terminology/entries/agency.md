---
slug: agency
schema_version: 1
term: agency
name: Agency
notation:
brief: The scope narrowing from adaptive system to causal actor — requires at least binary choice and at least one action with a causal effect on observable outcomes.
layer: framing-vocabulary
status: canon
tags: [agent_classes, structural_concepts]
source_type: asf
primary_source: 01-aat-core/src/scope-agency.md
first_asf_mention: 01-aat-core/src/scope-agency.md
see_also: [adaptive-system, actuated-agent, composite-agent, directed-separation]
aliases: []
do_not_confuse: [adaptive-system]
---

AAT narrows from the adaptive scope ($\mathcal{S}_\text{adaptive}$: any system that observes
under residual uncertainty) to the **agency scope** by adding two conditions:

$$\mathcal{S}_\text{agency} = \mathcal{S}_\text{adaptive} \cap \left\{ |\mathcal{A}| \geq 2, \;\; \exists\, a \neq a' \text{ s.t. } P(o \mid do(a)) \neq P(o \mid do(a')) \right\}$$

Binary choice ($|\mathcal{A}| \geq 2$) is necessary but not sufficient: two actions with
identical outcome distributions provide no interventional contrast. The causal-effect condition
ensures at least one meaningful contrast exists — the condition that permits the adaptive loop
to generate interventional data and unlocks the purposeful-agent machinery of Sections II and III.

**What is included**: thermostats, Kalman filters with control inputs, RL agents, military
commanders, software developers, AI agents with tool use. **What is in adaptive scope but
excluded**: passive observers ($|\mathcal{A}| < 2$) and nominal agents (choices that make no
difference to outcome distributions).

Every downstream segment that asserts "the agent can act" depends on this scope. The
purposeful-agent machinery ($O_t$, $\Sigma_t$, orient cascade) and the composition theory are
non-vacuous only within agency scope.

Scope defined in [`#scope-agency`](../../01-aat-core/src/scope-agency.md).
