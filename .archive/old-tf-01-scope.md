# TF-01: Scope — Adaptive Agents Under Uncertainty (Scope Definition)

This theory applies to any system consisting of an **agent** coupled to an **environment** through **observation** and **action** channels, where the environment is not fully observable and may change over time. This is the setting formalized by the POMDP literature[^kaelbling1998], generalized beyond MDP reward structure.

## Definitions

**Environment** ($\Omega$): The totality of state external to the agent. We make no assumptions about $\Omega$'s structure — it may be continuous or discrete, stationary or non-stationary, deterministic or stochastic, benign or adversarial.

**Agent**: An entity that (1) receives observations from the environment, (2) maintains some internal state, and (3) produces actions that affect the environment. The agent cannot access $\Omega$ directly — its observations are necessarily lossy (formalized below). This is a constitutive feature of the scope: the theory applies to systems where the agent-environment boundary entails information loss.

**Observation space** ($\mathcal{O}$): The set of possible observations available to the agent. Each observation is a lossy, possibly noisy function of the environment state and (optionally) the agent's prior action:

*[Definition (observation-function)]*
$$o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$$

where $h$ is the observation function and $\varepsilon_t$ represents noise or limits of perception. The action-dependence captures systems where the agent's choice affects not only the environment state (through $T$) but also the *observation mechanism* — which sensor to use, what question to ask, where to direct attention. When the observation mechanism is action-independent, the simpler form $o_t = h(\Omega_t, \varepsilon_t)$ is recovered as a special case.

**Action space** ($\mathcal{A}$): The set of actions available to the agent. Each action affects the environment:

*[Definition]*
$$\Omega_{t+1} \sim T(\cdot \mid \Omega_t, a_t)$$

where $T$ is the (possibly stochastic) transition function.

**Uncertainty**: The agent knows neither $h$ nor $T$ exactly. These are part of what the agent must approximate.

## Formal Scope

*[Scope Definition (scope-condition)]*
$$\mathcal{S}_{\text{TFT}} = \{(Agent, \Omega) : \mathcal{O} \neq \emptyset, \; |\mathcal{A}| \geq 2, \; H(\Omega_t \mid \mathcal{C}_t) \gt 0 \}$$

where $\mathcal C_t = (o_1, a_1, o_2, a_2, \ldots, a_{t-1}, o_t)$ is the full interaction history (formalized in TF-02). The theory applies wherever there is an agent that observes, acts with at least a binary choice, and faces residual uncertainty[^shannon1948] about its environment. The action-space requirement ($|\mathcal{A}| \geq 2$) ensures the agent has at least one interventional contrast — the minimal condition for CIY (TF-08), Level 2 epistemic access (TF-02), and the exploration-exploitation framework (TF-08) to be non-trivially applicable. The final condition — that uncertainty persists even given the complete action-observation history — is constitutive: if the agent could fully determine $\Omega$ from its history alone, the problem would be trivial.

## Why This Scope

This includes: thermostats, PID controllers, robots, organisms, RL agents, organizations, militaries, immune systems, scientific communities.

This excludes:
- **Pure mathematical structures** — no environment, no uncertainty
- **Closed-form systems** — fully observable, fully deterministic ($H(\Omega_t \mid \mathcal C_t) = 0$)
- **Passive observers** — $|\mathcal{A}| = 0$ (no actions at all). Bayesian inference without action falls outside scope; the model (TF-03), mismatch (TF-05), and update gain (TF-06) apply to passive learning, but the action-dependent results are trivially void.
- **Single-action agents** — $|\mathcal{A}| = 1$. An agent with only one available action satisfies the coupling requirement of TF-01 but gains nothing from TFT's action-dependent machinery: CIY is trivially zero (no interventional contrast), Level 2 epistemic access is unavailable, and the exploration-exploitation framework (TF-08) is void. The theory's passive-applicable results (TF-03, TF-05, TF-06) apply as in the passive observer case.

## Note on Temporal Indexing

The index $t$ is used for notational convenience. The theory's primary formulation is **event-driven** (see TF-04): observations and actions occur as events in continuous time at potentially different and variable rates. The discrete notation $t = 1, 2, \ldots$ is the special case where events arrive at uniform intervals on a single channel.

---

[^kaelbling1998]: Kaelbling, L. P., Littman, M. L., & Cassandra, A. R. (1998). "Planning and acting in partially observable stochastic domains." *Artificial Intelligence*, 101(1–2), 99–134.
[^shannon1948]: Shannon, C. E. (1948). "A Mathematical Theory of Communication." *Bell System Technical Journal*, 27(3), 379–423.
