# ACT-01: Scope — Agents Under Uncertainty

This theory applies to any system consisting of an **agent** coupled to an **environment** through **observation** and **action** channels, where the environment is not fully observable and may change over time. ACT formalizes how such agents adapt to reality, pursue goals, and coordinate with other agents — a continuum from pure survival to deliberate purposeful agency.

## Definitions

**Environment** (Ω): The totality of state external to the agent. We make no assumptions about Ω's structure — it may be continuous or discrete, stationary or non-stationary, deterministic or stochastic, benign or adversarial.

**Agent**: An entity that (1) receives observations from the environment, (2) maintains some internal state, and (3) produces actions that affect the environment. The agent cannot access Ω directly — its observations are necessarily lossy. This is constitutive: the theory applies where the agent-environment boundary entails information loss.

**Observation space** (O): The set of possible observations. Each is a lossy, possibly noisy function of environment state and (optionally) the agent's prior action:

*[Definition (observation-function)]*
$$o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$$

where h is the observation function and ε_t represents noise or limits of perception. When the observation mechanism is action-independent, the simpler form o_t = h(Ω_t, ε_t) is recovered.

**Action space** (A): The set of actions available to the agent:

*[Definition]*
$$\Omega_{t+1} \sim T(\cdot \mid \Omega_t, a_t)$$

where T is the (possibly stochastic) transition function.

**Uncertainty**: The agent knows neither h nor T exactly. These are part of what the agent must approximate.

## Formal Scope

*[Scope Definition]*
$$\mathcal{S}_{\text{ACT}} = \{(\text{Agent}, \Omega) : \mathcal{O} \neq \emptyset, \; |\mathcal{A}| \geq 2, \; H(\Omega_t \mid \mathcal{C}_t) \gt 0 \}$$

The theory applies wherever there is an agent that observes, acts with at least a binary choice, and faces residual uncertainty about its environment. The action-space requirement (|A| ≥ 2) ensures the agent has at least one interventional contrast — the minimal condition for causal learning (ACT-02) and exploration (ACT-09).

## The Agent Spectrum

Not all agents within this scope are the same. Two independent dimensions create a spectrum:

**Does the agent maintain an internal model of reality?** Some agents build and update a compressed representation M_t of how the world works. Others operate from fixed rules without updating.

**Does the agent pursue an objective?** Some agents have an explicit or implicit target state O_t they're trying to reach, and may maintain a strategy Σ_t for getting there. Others merely track reality without aiming at anything.

These two dimensions define four quadrants:

| | No objective (O_t absent) | Has objective (O_t present) |
|---|---|---|
| **No model (M_t absent)** | *Reactive system*: Fixed feedback rule. Thermostat, reflex arc. | *Blind pursuer*: Pursues goal without modeling reality. PID controller, gradient follower. |
| **Has model (M_t present)** | *Adaptive tracker*: Builds reality model but has no goal beyond tracking. Kalman filter, passive Bayesian learner. | *Purposeful agent*: Models reality AND pursues objectives. Commander, developer, AI agent. |

**The reactive system** (bottom-left): operates within ACT's scope (it observes, acts, faces uncertainty) but uses none of ACT's machinery beyond the basic feedback structure. It has neither model to update nor goal to pursue. The thermostat is the canonical example.

**The adaptive tracker** (top-left): builds and maintains a model M_t but has no explicit purpose beyond tracking reality. The Kalman filter is the canonical example — it minimizes estimation error but has no goal state. ACT's adaptive-systems machinery (mismatch, gain, tempo, persistence) fully describes these agents. TFT, which ACT subsumes, was primarily developed for this quadrant.

**The blind pursuer** (bottom-right): has a goal (setpoint r_t) but no reality model — it reacts to the gap between desired and actual state without modeling the underlying dynamics. The PID controller is the canonical example. It has O_t (setpoint) and computes δ_objective = r_t − y_t, but its "model" is just the error signal itself, with no prediction or understanding of the plant.

**The purposeful agent** (top-right): both models reality (M_t) and pursues objectives (O_t) through strategy (Σ_t). This is the full scope of ACT. The military commander, the software developer, the AI agent working on a codebase — all inhabit this quadrant. They need to understand reality (what is?) and pursue purpose (what should be?), and these two concerns interact: understanding informs strategy, and strategy directs what to observe.

### The Spectrum Is a Continuum

These quadrants are not discrete categories but regions of a continuum.
A PID controller with auto-tuning is migrating from blind pursuer toward purposeful agent (it's building a rudimentary model). An RL agent in pure exploration is temporarily an adaptive tracker (gathering information without exploiting). The boundaries are analytical distinctions, not ontological walls.

### Survival Requires Strategy in Non-Trivial Environments

Even the "survival" case (no explicit objective beyond persisting) requires strategy — and thus O_t and Σ_t — once the environment demands multi-step responses. An organism that must evade a predator, navigate to food, and return to shelter is executing a strategy DAG even if its "goal" is merely to continue existing. ACT's persistence condition (ACT-07) is necessary but not sufficient for agency in any environment that requires sequential, coordinated action.

## Domain Examples

| Domain | Agent | Quadrant | M_t | O_t / Σ_t |
|--------|-------|----------|-----|-----------|
| Home heating | Thermostat | Reactive | — | — |
| State estimation | Kalman filter | Adaptive tracker | State estimate + covariance | — |
| Process control | PID controller | Blind pursuer | — | Setpoint r_t |
| Optimal control | LQG (Kalman + LQR) | Purposeful (simple) | State estimate | Quadratic cost objective |
| Reinforcement learning | RL agent | Purposeful | Value function / world model | Reward maximization |
| Software development | Developer | Purposeful | Mental model of codebase | Feature/fix objectives, strategy |
| Military operations | Commander | Purposeful | Intelligence picture | Mission objective, operational plan |
| Organizational management | Executive | Purposeful | Market/org understanding | Strategic goals, initiatives |
| AI assistant | LLM agent | Purposeful | Context window contents | Task objective, approach |
| Immune system | Adaptive immunity | Adaptive tracker | Antibody repertoire | — (or implicit: eliminate non-self) |
| Scientific community | Research field | Purposeful | Current theory + evidence | Understanding / prediction goals |

### Software as an ACT Domain

Software development has properties that make it an unusually rich domain instantiation:

1. **The environment is fully inspectable** — partial observability comes from cognitive bandwidth, not physics.
2. **Level 3 counterfactuals are executable** — git checkout + replay gives ground-truth alternative histories.
3. **The causal DAG is partially explicit** — import graphs, type systems, dependency declarations.
4. **History is perfectly recorded** — git as complete, immutable chronica.
5. **Multiple agents interact through a shared versioned artifact** — multi-agent coupling made concrete.
6. **Observation channel quality is under agent control** — code quality IS observation infrastructure. Well-written code = low U_o for future readers. This creates a second-order feedback loop unique to software.

These properties make software a natural domain for validating ACT and for developing the theory's domain instantiation machinery. The temporal optimization target (minimize comprehension + implementation time under repeated handoff) provides a principled objective function, grounded by the information-theoretic specification bound (ACT-02 of domain instantiation) and the Bayesian change-expectation baseline.

## Why This Scope

This includes: thermostats, PID controllers, robots, organisms, RL agents, organizations, militaries, immune systems, scientific communities, developers, AI agents.

This excludes:
- **Pure mathematical structures** — no environment, no uncertainty
- **Closed-form systems** — fully observable, fully deterministic
- **Passive observers** — |A| = 0 (no actions at all; Bayesian inference without action falls outside scope)
- **Single-action agents** — |A| = 1 (no interventional contrast)

## Note on Temporal Indexing

The index t is used for notational convenience. The theory's primary formulation is **event-driven** (ACT-04): observations and actions occur as events in continuous time at potentially different and variable rates. The discrete notation t = 1, 2, ... is the special case where events arrive at uniform intervals on a single channel.
