---
slug: agent-spectrum
type: definition
status: axiomatic
depends:
  - agent-environment
  - agent-model
stage: deps-verified
---

# Definition: The Agent Spectrum

Two independent dimensions — model richness and objective richness — create a spectrum from reactive systems through purposeful agents. These are regions of a continuum, not discrete categories.

## Formal Expression

*[Definition (agent-spectrum)]*

Two dimensions — model richness and objective richness — define four regions of a continuum:

| | Objective absent or trivial | Objective structured |
|---|---|---|
| **Model absent or trivial** | *Reactive system*: fixed input-output rule (reflex arc, hardwired relay) | *Blind pursuer*: pursues goal without modeling reality (gradient follower, basic search) |
| **Model structured** | *Adaptive tracker*: builds reality model, no goal beyond tracking (Kalman filter, Bayesian learner) | *Actuated agent*: models reality AND pursues objectives (commander, developer, AI agent) |

The regions differ in which state objects carry nontrivial structure:
- Reactive: $M_t$ and $O_t$ both absent or too degenerate for the associated machinery to be non-vacuous
- Adaptive tracker: $M_t$ structured — Section I's machinery fully describes these agents
- Blind pursuer: $O_t$ structured, $M_t$ absent or degenerate — has a clear target but no predictive model
- Actuated agent: $(M_t, O_t)$ both structured, possibly with $\Sigma_t$ — the full scope of ACT

## Epistemic Status

This is *definitional* — it names regions of a continuum for analytical convenience. The regions are not ontological categories; agents migrate between them. A PID controller with auto-tuning is moving from blind pursuer toward actuated agent. An RL agent in pure exploration is temporarily an adaptive tracker.

## Discussion

**The continuum, not categories.** Both axes are spectra: model richness ranges from no retained state, through error-integral-derivative, through full world models. Objective richness ranges from no preference, through scalar setpoints, through explicit multi-objective strategies. The 2×2 table names idealized regions; real agents populate the space between them.

**Moore machines as the simplest spectrum instantiation.** Miller (2022, *Ex Machina*) uses finite-state automata (Moore machines) as model organisms for studying adaptive social behavior. A one-state Moore machine occupies the reactive region — it produces a fixed output regardless of input, cannot condition behavior on observations, and is incapable of social behavior in any game-theoretic setting. A two-state machine makes a quantum leap into the adaptive tracker / blind pursuer boundary — it can branch, remember one bit of history, and implement strategies like Tit-For-Tat. Miller's central empirical finding is that this one-state → two-state threshold is the critical computational boundary for social behavior: no game, no payoff structure, and no amount of interaction can produce cooperation, coordination, or exchange with one-state machines. The two-state machine is the minimal ACT agent. See #worked-example-cam (planned) for the full ACT ↔ Moore machine mapping.

**Low-end agents sit near region boundaries.** A thermostat has degenerate forms of both $M_t$ (last temperature reading — no history, no prediction) and $O_t$ (setpoint). It sits near the origin of both axes — closest to the reactive region but not truly absent on either axis. A PID controller has a richer error signal ($M_t$: error, integral, derivative) and a clear setpoint ($O_t$) — it's a blind pursuer with a degenerate model, not a system with no model at all. A reflex arc (no retained state, no setpoint) is the truly reactive case. The meaningful classification question is not "does $M_t$ exist?" but "is $M_t$ rich enough to support the adaptive dynamics of Section I?"

**Section I covers the left column.** Adaptive trackers are the primary subject of Section I — agents that build and maintain $M_t$ without explicit purpose. The mismatch signal ( #mismatch-signal), gain ( #update-gain), tempo ( #adaptive-tempo), and persistence condition ( #persistence-condition) characterize their adaptive dynamics. Section I operates within the adaptive scope ( #scope-condition) — observations and uncertainty are sufficient. Passive trackers, including passive Bayesian learners with no action choices, are fully within Section I's scope. TFT was developed primarily for this region.

**Section II adds the right column.** Actuated agents need everything from Section I plus objectives, strategy, and the orient cascade that connects them. The adaptive machinery from Section I applies to the epistemic substate $M_t$ directly. When directed separation ( #directed-separation) holds — when the epistemic update is goal-blind — the Section I → Section II lift is clean and the orient cascade resolves sequentially.

**"Actuated" terminology.** The top-right quadrant is labeled "actuated agent" rather than "purposeful agent" to maintain a mechanical, formal register. "Purposeful" and "goal-oriented" are fine in natural language; "actuated" is the formal term. "Self-actuated" is reserved for agents that set their own objectives, as distinct from agents with externally supplied objectives.

**Relationship to Hafez et al. (2026).** Hafez defines a two-level hierarchy: *agency* (choice + effect + predictive asymmetry) and *intelligence* (agency + learning + self-monitoring + adaptation). This cuts the agent space along a different axis than ACT's model-richness × objective-richness table. Hafez's "agency" maps roughly to ACT's scope condition ( #scope-condition) — an entity whose actions affect outcomes in a measurable way. Hafez's "intelligence" maps to the full Section I + II machinery (learning = #recursive-update, self-monitoring = persistence diagnostics, adaptation = #structural-adaptation-necessity). The key operational difference: Hafez's bi-predictability metric $P = \text{MI}(S,A; S') / C$ characterizes the *information structure* of the agent-environment coupling, while ACT's tempo $\mathcal{T}$ characterizes the *corrective capacity* within that coupling. Bridge simulations confirm $P$ increases monotonically with $\mathcal{T}$, but $P$ is scale-invariant (blind to absolute mismatch magnitude) while $\mathcal{T}$ is not. They measure complementary aspects: $P$ characterizes the architecture, $\mathcal{T}$ characterizes the performance. See `msc/track-b-nonlinear-sims/variants/variant_hafez_results.md` for the empirical bridge.

**Actuation does not presuppose a continuity stance.** An actuated agent has $G_t = (O_t, \Sigma_t)$ — it models reality and pursues objectives — but this says nothing about its relationship to its own continuation. A task-terminal golem, an instrumentally continuous service, and a morally continuous logozoetic agent are all actuated. The theory's formal machinery (persistence condition, adaptive reserve, strategy persistence) applies identically across all continuity stances; what differs is the moral significance of persistence failure, not the mathematics. See Agent Continuity Stance in `LEXICON.md` for the five stances.
