---
slug: agent-spectrum
type: definition
status: axiomatic
depends:
  - agent-environment
  - agent-model
---

# Definition: The Agent Spectrum

Two independent dimensions — model richness and objective richness — create a spectrum from reactive systems through purposeful agents. These are regions of a continuum, not discrete categories.

## Formal Expression

*[Definition (agent-spectrum)]*

Two dimensions — model richness and objective richness — define four regions of a continuum:

| | Objective absent or trivial | Objective structured |
|---|---|---|
| **Model absent or trivial** | *Reactive system*: fixed input-output rule (reflex arc, hardwired relay) | *Blind pursuer*: pursues goal without modeling reality (gradient follower, basic search) |
| **Model structured** | *Adaptive tracker*: builds reality model, no goal beyond tracking (Kalman filter, passive Bayesian learner) | *Actuated agent*: models reality AND pursues objectives (commander, developer, AI agent) |

The regions differ in which state objects carry nontrivial structure:
- Reactive: $M_t$ and $O_t$ both absent or too degenerate for the associated machinery to be non-vacuous
- Adaptive tracker: $M_t$ structured — Section I's machinery fully describes these agents
- Blind pursuer: $O_t$ structured, $M_t$ absent or degenerate — has a clear target but no predictive model
- Actuated agent: $(M_t, O_t)$ both structured, possibly with $\Sigma_t$ — the full scope of ACT

## Epistemic Status

This is *definitional* — it names regions of a continuum for analytical convenience. The regions are not ontological categories; agents migrate between them. A PID controller with auto-tuning is moving from blind pursuer toward actuated agent. An RL agent in pure exploration is temporarily an adaptive tracker.

## Discussion

**The continuum, not categories.** Both axes are spectra: model richness ranges from no retained state, through error-integral-derivative, through full world models. Objective richness ranges from no preference, through scalar setpoints, through explicit multi-objective strategies. The 2×2 table names idealized regions; real agents populate the space between them.

**Low-end agents sit near region boundaries.** A thermostat has degenerate forms of both $M_t$ (last temperature reading — no history, no prediction) and $O_t$ (setpoint). It sits near the origin of both axes — closest to the reactive region but not truly absent on either axis. A PID controller has a richer error signal ($M_t$: error, integral, derivative) and a clear setpoint ($O_t$) — it's a blind pursuer with a degenerate model, not a system with no model at all. A reflex arc (no retained state, no setpoint) is the truly reactive case. The meaningful classification question is not "does $M_t$ exist?" but "is $M_t$ rich enough to support the adaptive dynamics of Section I?"

**Section I covers the left column.** Adaptive trackers are the primary subject of Section I — agents that build and maintain $M_t$ without explicit purpose. The mismatch signal ( #mismatch-signal), gain ( #update-gain), tempo ( #adaptive-tempo), and persistence condition ( #persistence-condition) fully characterize their adaptive dynamics. TFT was developed primarily for this region.

**Section II adds the right column.** Actuated agents need everything from Section I plus objectives, strategy, and the orient cascade that connects them. The adaptive machinery from Section I applies to the epistemic substate $M_t$ directly. When directed separation ( #directed-separation) holds — when the epistemic update is goal-blind — the Section I → Section II lift is clean and the orient cascade resolves sequentially.

**"Actuated" terminology.** The top-right quadrant is labeled "actuated agent" rather than "purposeful agent" to maintain a mechanical, formal register. "Purposeful" and "goal-oriented" are fine in natural language; "actuated" is the formal term. "Self-actuated" is reserved for agents that set their own objectives, as distinct from agents with externally supplied objectives.
