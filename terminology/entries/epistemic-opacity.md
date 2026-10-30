---
slug: epistemic-opacity
schema_version: 1
term: epistemic opacity
name: Epistemic Opacity
brief: The agent may not know the observation law (the conditional law of each observation given state and action); an informational condition, not a phenomenological claim.
layer: framing-vocabulary
status: canon
tags: [structural_concepts]
source_type: asf
primary_source: 01-aat-core/src/def-observation-function.md
first_asf_mention: 01-aat-core/src/def-observation-function.md
see_also: [transition-opacity, agent-opacity]
aliases: []
do_not_confuse: [transition-opacity, agent-opacity]
---

The condition that the agent does not know the observation kernel exactly: the conditional law of each observation given the environment's state and the agent's prior action. Its unknown content is the observation component $\theta_h$ of the environment's law. Only the kernel is learnable; the pair (observation function, noise distribution) is not, because many such pairs induce the same kernel. Epistemic opacity is distinct from the state being partially observed: a Kalman filter has a partially observed state and a known observation law. **Scope caution (nuance-flagged at canonicalization):** in philosophy of mind, "epistemic opacity" carries phenomenology / qualia connotations that AAT does not adopt; AAT's meaning is strictly informational (what the agent does and does not know about its observation channel), not phenomenological.

Defined in [`#def-observation-function`](../../01-aat-core/src/def-observation-function.md). Together with [transition opacity](transition-opacity.md) and uncertainty about the state, it is one of the three typed components of the uncertainty the adaptive scope requires ([`#scope-adaptive-system`](../../01-aat-core/src/scope-adaptive-system.md)); none of the three is required on its own.
