---
slug: def-agent-environment
type: definition
status: axiomatic
depends: []
stage: deps-verified
---

# Definition: Agent-Environment Coupling

The framework begins by drawing the agent/environment boundary that the rest of the theory will be defined over. The **environment** is denoted $\Omega$ — the totality of state external to the agent — and is left deliberately underspecified: it may be continuous or discrete, stationary or non-stationary, deterministic or stochastic, benign or adversarial; it may itself contain other agents, physical systems, or software artifacts. An **agent** is anything that satisfies three conditions: it receives observations from $\Omega$ (a perception channel), it maintains internal state (memory or model), and it produces actions that affect $\Omega$ (an action channel).

The constitutive commitment is the *information-loss boundary*: the agent cannot access $\Omega$ directly. All contact with the environment is mediated through lossy observation. This is not a simplifying assumption but a scope condition — systems with direct full-state access fall outside AAT's purview, because for them the entire adaptive machinery (mismatch signal, model maintenance, correction) becomes vacuous. The agent-environment decomposition is therefore not a truth-claim about the world but a modeling choice that delineates *what AAT analyzes*: systems facing genuine uncertainty about their environment.

## Formal Expression

*[Definition (agent-environment)]*

Let $\Omega$ denote the **environment**: the totality of state external to the agent. We make no assumptions about $\Omega$'s structure — it may be continuous or discrete, stationary or non-stationary, deterministic or stochastic, benign or adversarial.

An **agent** is an entity satisfying three conditions:

1. It receives observations from $\Omega$ (perception channel)
2. It maintains internal state (memory/model)
3. It produces actions that affect $\Omega$ (action channel)

*[Definition (information-loss-boundary)]*

The agent cannot access $\Omega_t$ directly. All contact with the environment is mediated through lossy observation. This is not a simplifying assumption — it is a scope condition. Systems where the agent has direct access to full environment state are outside AAT's scope ( #scope-adaptive-system).

## Epistemic Status

This is *definitional* — it establishes the conceptual framework, not a truth-claim. The agent-environment decomposition is a modeling choice that delineates what AAT analyzes. The information-loss boundary is the constitutive commitment: it restricts AAT's scope to systems where the agent faces genuine uncertainty about its environment.

## Discussion

**Why information loss is constitutive.** An agent with perfect access to $\Omega_t$ has no need for a model, no mismatch signal, no adaptation. The entire adaptive machinery of Part I becomes vacuous. The information-loss boundary is what makes the theory non-trivial.

**Generality of $\Omega$.** The environment is deliberately underspecified. $\Omega$ may include other agents, physical systems, software artifacts, or any combination. The only structural commitment is that $\Omega$ is external to the agent and not fully accessible.
