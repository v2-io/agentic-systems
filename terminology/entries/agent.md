---
slug: agent
schema_version: 1
term: agent
name: Agent
brief: Umbrella technical term for the thing on the agent side of the agent-environment coupling; the scope-cascade tiers (Adaptive System, Agentic System, Actuated Agent, Self-Actuated Agent) are its specific inhabitants.
layer: framing-vocabulary
status: canon
tags: [agent_classes]
source_type: asf
primary_source: 01-aat-core/src/def-agent-environment.md
first_asf_mention: 01-aat-core/src/def-agent-environment.md
see_also: [adaptive-system, agentic-system, actuated-agent, self-actuated-agent]
aliases: []
do_not_confuse: []
---

The broad technical term for the thing on the agent side of the [agent-environment coupling](../../01-aat-core/src/def-agent-environment.md): the entity the coupling's three structural channels (perception, internal state, action) attach to, whatever richness each channel carries.

The framework's **scope cascade** names specific inhabitants of this umbrella, each a narrowing of the coupling that adds one structural condition:

- [Adaptive System](adaptive-system.md) — perception channel + residual uncertainty ([`#scope-adaptive-system`](../../01-aat-core/src/scope-adaptive-system.md))
- [Agentic System](agentic-system.md) — adds causal-contrast action ([`#scope-agency`](../../01-aat-core/src/scope-agency.md))
- [Actuated Agent](actuated-agent.md) — adds an explicit purposeful substate at the lift to $X_t = (M_t, G_t)$ ([`#form-complete-agent-state`](../../01-aat-core/src/form-complete-agent-state.md))
- [Self-Actuated Agent](self-actuated-agent.md) — revises its own objective

shown graphically at [`#fig-scope-of-work`](../../01-aat-core/INTRODUCTION.md). An Adaptive System *is* an agent in the umbrella sense that satisfies the adaptive scope; the capitalized cascade noun "Agent" is *earned* at the actuated lift, where explicit objective and strategy machinery enters.

**Do not confuse the cascade with the spectrum.** The scope cascade above is a scope-driven progression (each tier adds a structural condition). The [agent spectrum](../../01-aat-core/src/def-agent-spectrum.md) cuts the agent space along a *different, orthogonal* axis — model-richness $\times$ objective-richness, giving reactive system / adaptive tracker / blind seeker / actuated agent. The two taxonomies share the "actuated agent" corner but classify by different criteria.
