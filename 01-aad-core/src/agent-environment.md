---
slug: agent-environment
type: definition
status: axiomatic
depends: []
stage: deps-verified
---

# Definition: Agent-Environment Coupling

An agent is an entity that receives observations from an environment, maintains internal state, and produces actions that affect the environment. The agent cannot access the environment directly — observations are necessarily lossy. This boundary condition is constitutive: the theory applies where the agent-environment boundary entails information loss.

## Formal Expression

*[Definition (agent-environment)]*

Let $\Omega$ denote the **environment**: the totality of state external to the agent. We make no assumptions about $\Omega$'s structure — it may be continuous or discrete, stationary or non-stationary, deterministic or stochastic, benign or adversarial.

An **agent** is an entity satisfying three conditions:

1. It receives observations from $\Omega$ (perception channel)
2. It maintains internal state (memory/model)
3. It produces actions that affect $\Omega$ (action channel)

*[Definition (information-loss-boundary)]*

The agent cannot access $\Omega_t$ directly. All contact with the environment is mediated through lossy observation. This is not a simplifying assumption — it is a scope condition. Systems where the agent has direct access to full environment state are outside ACT's scope ( #scope-condition).

## Epistemic Status

This is *definitional* — it establishes the conceptual framework, not a truth-claim. The agent-environment decomposition is a modeling choice that delineates what ACT analyzes. The information-loss boundary is the constitutive commitment: it restricts ACT's scope to systems where the agent faces genuine uncertainty about its environment.

## Discussion

**Why information loss is constitutive.** An agent with perfect access to $\Omega_t$ has no need for a model, no mismatch signal, no adaptation. The entire adaptive machinery of Section I becomes vacuous. The information-loss boundary is what makes the theory non-trivial.

**Generality of $\Omega$.** The environment is deliberately underspecified. $\Omega$ may include other agents, physical systems, software artifacts, or any combination. The only structural commitment is that $\Omega$ is external to the agent and not fully accessible.
