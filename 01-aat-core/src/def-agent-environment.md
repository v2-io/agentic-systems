---
slug: def-agent-environment
type: definition
status: axiomatic
depends: []
stage: deps-verified
---

# Definition: Agent-Environment Coupling

The framework begins by drawing the agent/environment boundary that the rest of the theory will be defined over. The **environment** is denoted $\Omega$ — the totality of state external to the agent — and is left deliberately underspecified: it may be continuous or discrete, stationary or non-stationary, deterministic or stochastic, benign or adversarial; it may itself contain other agents, physical systems, or software artifacts. The **agent-environment coupling** has three structural channels: a *perception channel* carrying observations from $\Omega$ to the agent, *internal state* held on the agent side (memory or model), and an *action channel* carrying the agent's actions back to $\Omega$. These name what the coupling *has* — not properties an agent must maximally exhibit. How richly each channel is exercised (whether the action channel carries causal contrast, how much residual uncertainty the perception channel leaves) is fixed downstream by specific scope conditions ( #scope-adaptive-system, #scope-agency), not by this definition. *Agent* is the umbrella term for the thing on the agent side of the coupling, whatever channels it exercises.

The constitutive commitment is the *information-loss boundary*: the agent cannot access $\Omega$ directly. All contact with the environment is mediated through lossy observation. This is not a simplifying assumption but a scope condition — systems with direct full-state access fall outside AAT's purview, because for them the entire adaptive machinery (mismatch signal, model maintenance, correction) becomes vacuous. The agent-environment decomposition is therefore not a truth-claim about the world but a modeling choice that delineates *what AAT analyzes*: systems facing genuine uncertainty about their environment.

## Formal Expression

*[Definition (agent-environment-coupling)]*

Let $\Omega$ denote the **environment**: the totality of state external to the agent. We make no assumptions about $\Omega$'s structure — it may be continuous or discrete, stationary or non-stationary, deterministic or stochastic, benign or adversarial.

The **agent-environment coupling** consists of three structural channels:

1. A **perception channel** carrying observations from $\Omega$ to the agent
2. **Internal state** held on the agent side (memory/model)
3. An **action channel** carrying the agent's actions to $\Omega$

These name what the coupling *has*, not properties an agent must exhibit to qualify. Whether the action channel is non-trivial ($\lvert\mathcal{A}\rvert \geq 2$), whether actions carry causal contrast, and what residual uncertainty the perception channel leaves ($H(\Omega_t \mid \mathcal{C}_t) \gt 0$) are fixed by the scope conditions that narrow this coupling into analyzable classes ( #scope-adaptive-system, #scope-agency) — not by the channel inventory above.

*[Definition (information-loss-boundary)]*

The agent cannot access $\Omega_t$ directly. All contact with the environment is mediated through lossy observation. This is the **constitutive commitment** that makes the coupling AAT's subject: a system with direct access to full environment state is outside AAT's scope ( #scope-adaptive-system), because for it the entire adaptive machinery (mismatch signal, model maintenance, correction) becomes vacuous.

## Epistemic Status

This is *definitional* — it establishes the coupling structure AAT analyzes, not a truth-claim about the world. The three channels describe what the agent-environment coupling consists of; the constitutive commitment is the information-loss boundary, which restricts AAT's scope to systems where the agent faces genuine uncertainty about its environment. What counts as an *agent* in a given analytical context — and which cascade tier it occupies — is fixed by the scope conditions that narrow this coupling, not by the channel inventory itself.

## Discussion

**Why information loss is constitutive.** An agent with perfect access to $\Omega_t$ has no need for a model, no mismatch signal, no adaptation. The entire adaptive machinery of Part I becomes vacuous. The information-loss boundary is what makes the theory non-trivial.

**Generality of $\Omega$.** The environment is deliberately underspecified. $\Omega$ may include other agents, physical systems, software artifacts, or any combination. The only structural commitment is that $\Omega$ is external to the agent and not fully accessible.

**"Agent" as umbrella term vs. cascade-tier label.** This segment uses *agent* as the umbrella technical term — the thing on the agent side of any agent-environment coupling, whatever channels it exercises. The framework reserves tier-specific labels for the *narrowings* of this coupling: an **Adaptive System** ( #scope-adaptive-system) is the coupling under a perception channel plus residual uncertainty; an **Agentic System** ( #scope-agency) adds causal-contrast action; an **Actuated Agent** ( #form-complete-agent-state) adds an explicit purposeful substate at the lift to $X_t = (M_t, G_t)$; a **Self-Actuated Agent** revises its own objective. These tiers — shown graphically in the scope-of-work figure ( #fig-scope-of-work) — are *specific inhabitants* of the umbrella: an Adaptive System *is* an agent (umbrella sense) satisfying the adaptive scope, even though the cascade earns the capitalized noun "Agent" only at the actuated lift and above. The umbrella/tier distinction is documented in the LEXICON's *agent* entry. It is orthogonal to the *agent spectrum* ( #def-agent-spectrum), which classifies agents along model-richness $\times$ objective-richness (reactive system / adaptive tracker / blind seeker / actuated agent) rather than along the scope cascade.
