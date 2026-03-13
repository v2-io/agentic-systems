---
slug: chronica
type: definition
status: axiomatic
depends:
  - agent-environment
  - observation-function
  - action-transition
---

# Definition: Chronica

The interaction history $\mathcal C_t$ is the complete, singular causal record of the agent's observations and actions. Everything the agent can ever know must be constructed from this sequence.

## Formal Expression

*[Definition (chronica)]*

$$\mathcal{C}_t = (o_1, a_1, o_2, a_2, \ldots, a_{t-1}, o_t)$$

The ordering is not a notational convenience. It reflects an irreversible physical fact: $a_{t-1}$ was selected before $o_t$ was received. The agent could not have used $o_t$ to select $a_{t-1}$.

$\mathcal C_t$ is monotonically growing — events are added but never removed. It is the agent's *only* raw material for constructing a model ( #agent-model).

## Epistemic Status

This is *definitional*. The chronica names an object that exists by construction in any system satisfying #agent-environment: the temporal sequence of all agent-environment interactions. The term "chronica" (from Greek χρονικά, "records of time") avoids collision with $\mathcal{H}$ (Shannon entropy) in speech and notation.

## Discussion

**The chronica is singular and non-forkable.** Because the temporal ordering is irreversible, $\mathcal C_t$ represents a unique causal trajectory. Duplicating an agent's state and exposing the copies to different future events creates two agents with divergent chronica, neither of which is a sufficient statistic for the other's trajectory. See #agent-identity for the full development of this observation.

**Relationship to the model.** The model $M_t = \phi(\mathcal C_t)$ ( #agent-model) is a compression of the chronica. How much of $\mathcal C_t$'s predictive information survives compression is measured by model sufficiency ( #model-sufficiency).
