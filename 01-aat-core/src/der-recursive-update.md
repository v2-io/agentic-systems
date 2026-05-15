---
slug: der-recursive-update
type: derived
status: conditional
depends:
  - form-agent-model
  - form-event-driven-dynamics
  - deriv-recursive-update
stage: claims-verified
---

# Derived: Recursive Update

Agent state updates (epistrophe — the corrective turning toward reality) must be recursive: the new model state is a function of the previous model state and the incoming event, not of the full interaction history. For finite agents this is computational necessity; for agents with unlimited computation it is the natural structure imposed by temporal ordering.

## Formal Expression

*[Derived (recursive-update, from temporal postulate and $M_t$ completeness)]*

**Event-driven update:**

$$M_{\tau^+} = f_M(M_{\tau^-}, e_\tau)$$

where:
- $M_{\tau^-}$ is the model state immediately before event $e_\tau$
- $M_{\tau^+}$ is the model state immediately after
- $f_M$ is the update function — it takes the current model and the new event, not the full history $\mathcal C_t$

**Between-event evolution:**

$$\frac{dM}{d\tau} = g_M(M_\tau)$$

Between events, the model evolves autonomously — internal reorganization, prediction generation, decay of transient states. The between-event dynamics depend only on the current model state, not on external input (which, by definition, arrives only at events).

## Epistemic Status

*Exact, with a partly definitional character.* The result follows from three constraints: temporal ordering (C1 — physical law), partial observability (C2 — scope definition), and state completeness (C3 — analytical commitment that $M_t$ summarizes everything the agent retains). C1 and C2 do genuine eliminative work; C3 is definitional — it cannot be "violated" because any violation is absorbed by expanding $M_t$. The Markov structure is therefore not discovered in the environment but chosen through the definition of $M_t$ as complete. This is not a weakness — it is the nature of the claim: recursive update is the only form consistent with C1 + C2 + the definition of $M_t$ as complete (see #deriv-recursive-update for the full argument and seven counterexample attacks). For finite agents, recursion is also *computational necessity*: re-processing the full history at each event is infeasible.

## Discussion

**Recursion as a consequence of completeness.** The recursive form is not an assumption bolted on — it follows from the definition of $M_t$ as complete. If $M_t$ were incomplete (if some relevant information lived outside $M_t$ in the raw history), then $f_M(M_{\tau^-}, e_\tau)$ would be insufficient and the agent would need to consult $\mathcal C_t$ directly. The sufficiency of the recursive form is precisely what #def-model-sufficiency measures: when $S(M_t) = 1$, the recursive update loses nothing.

**Between-event dynamics matter.** The autonomous evolution $g_M(M_\tau)$ is not merely filler between observations. It includes prediction generation (what the agent expects to see next), uncertainty growth (model confidence decaying over time without new data), and internal reorganization (consolidation, abstraction). In event-driven systems ( #form-event-driven-dynamics), the between-event interval is variable, making $g_M$ load-bearing for agents that must act or predict between observations. When the between-event dynamics are driven by replayed or internally-generated pseudo-events and the update objective is IB-gap reduction rather than one-step mismatch minimization, $g_M$ is operating in the *consolidation regime* per #form-consolidation-dynamics — a named regime with its own scope condition ($\nu_{\text{consol}} \ll \nu_{\text{online}}$) and its own necessity condition (sub-state factorization + bounded per-event budget). Consolidation is where the stability-plasticity feasibility window complements #schema-strategy-persistence's plasticity lower bound.

**Connection to the update gain.** The event-driven update $f_M(M_{\tau^-}, e_\tau)$ is where the gain principle ( #emp-update-gain) operates: $\eta^\ast$ determines how strongly $e_\tau$ shifts $M_t$ away from its prior value. The recursive form makes the gain's role explicit — it modulates the single-step correction.
