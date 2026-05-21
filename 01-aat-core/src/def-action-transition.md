---
slug: def-action-transition
type: definition
status: axiomatic
depends:
  - def-agent-environment
stage: deps-verified
---

# Definition: Action and Transition

The action channel is now formalized. The agent has an **action space** $\mathcal{A}$, and actions affect the environment through a possibly-stochastic **transition function** $T$: the next environment state is drawn from $T(\cdot \mid \Omega_t, a_t)$. Deterministic transitions are the special case where $T$ concentrates all mass on a single successor; stochasticity is permitted but not required. Crucially, the agent does *not* know $T$ exactly. Together with the lossy observation channel ( #def-observation-function), this completes the agent-environment loop: environment $\to$ observation $\to$ agent $\to$ action $\to$ next environment.

What makes action non-trivial is the combination of unknown observation function and unknown transition function. If $T$ were known, action selection would collapse to plain optimization over a known function; the joint opacity of $h$ and $T$ is what creates the need for adaptive behavior.

One subtle modeling commitment is surfaced: by writing the transition as Markov in $\Omega$ (only $\Omega_t$ and $a_t$ appear in the conditioning), the framework implicitly takes $\Omega$ to be the *sufficient state* for its own evolution — any non-Markov environment is absorbed by extending $\Omega$ to include enough history. This is the world-side analog of a parallel move the framework will make later for the agent's internal model ( #deriv-recursive-update Constraint C3): Markov properties here are commitments about the *breadth* of the named object, not structural claims about underlying dynamics.

## Formal Expression

*[Definition (action-transition)]*

The **action space** $\mathcal{A}$ is the set of actions available to the agent. Actions affect the environment via the transition function:

$$\Omega_{t+1} \sim T(\cdot \mid \Omega_t, a_t)$$

where:
- $T$ is the (possibly stochastic) transition function
- $\Omega_t$ is the current environment state
- $a_t \in \mathcal{A}$ is the agent's chosen action

*[Definition (transition opacity)]*

The agent does not know $T$ exactly.

## Epistemic Status

This is *definitional*. The transition function $T$ is a modeling device that captures how agent actions couple back into the environment. The stochasticity of $T$ is allowed but not required — deterministic transitions are the special case where $T$ places all mass on a single successor state. The claim that $T$ is unknown to the agent is constitutive of the uncertainty setting, paralleling the epistemic opacity of $h$ ( #def-observation-function).

## Discussion

**Closing the loop.** Together with #def-observation-function, this definition completes the agent-environment coupling: the agent observes via $h$ and acts via $T$. The loop $\Omega_t \xrightarrow{h} o_t \rightarrow \text{agent} \xrightarrow{a_t} \Omega_{t+1}$ is the fundamental structure that all subsequent claims build on.

**Uncertainty about $T$ is what makes action non-trivial.** If the agent knew $T$ exactly, action selection would reduce to optimization over a known function. The combination of unknown $h$ and unknown $T$ is what creates the need for adaptive behavior.

**Markov-of-$\Omega$ as a modeling commitment, not an empirical assumption.** The form $\Omega_{t+1} \sim T(\cdot \mid \Omega_t, a_t)$ is implicitly Markov in $\Omega$ — only the current $\Omega_t$ and $a_t$ appear in the conditioning. Without loss of generality, $\Omega$ is taken to be the *sufficient state* for its own evolution under $T$: any non-Markov environment is absorbed by extending $\Omega$ to include enough history to make future-state distribution depend only on current state and action. This is the world-side analog of the Markov-by-completeness move that #der-recursive-update makes for the agent-side state $M_t$ ( #deriv-recursive-update Constraint C3). The two are independent — Markov-of-$M_t$ is forced by *defining $M_t$ as complete*; Markov-of-$\Omega$ is forced by *defining $\Omega$ as the sufficient state*. Both are modeling commitments about the *breadth* of the named object, not structural assumptions about underlying world dynamics.
