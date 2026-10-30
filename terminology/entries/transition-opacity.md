---
slug: transition-opacity
schema_version: 1
term: transition opacity
name: Transition Opacity
brief: The agent may not know the transition law $T$ exactly; the transition component $\theta_T$ of the environment's law.
layer: framing-vocabulary
status: canon
tags: [structural_concepts]
source_type: asf
primary_source: 01-aat-core/src/def-action-transition.md
first_asf_mention: 01-aat-core/src/def-action-transition.md
see_also: [epistemic-opacity]
aliases: []
do_not_confuse: [epistemic-opacity, agent-opacity]
---

The condition that the agent does not know the transition kernel $T$ exactly; its unknown content is the transition component $\theta_T$ of the environment's law. It is one of the typed components of the uncertainty the adaptive scope requires, and it is not required on its own. A Kalman filter knows its transition law and is in scope through its hidden state; a tabular reinforcement learner reads its state exactly and is in scope through its unknown transition law. A known state leaves nothing to filter, a known law leaves nothing to learn, and only both together leave nothing to adapt to.

Defined in [`#def-action-transition`](../../01-aat-core/src/def-action-transition.md); the typed target is in [`#scope-adaptive-system`](../../01-aat-core/src/scope-adaptive-system.md).
