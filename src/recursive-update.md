---
slug: recursive-update
type: derived
status: exact
depends:
  - agent-model
  - event-driven-dynamics
  - recursive-update-derivation
---

# Derived: Recursive Update

Agent state updates must be recursive: the new model state is a function of the previous model state and the incoming event, not of the full interaction history. For finite agents this is computational necessity; for agents with unlimited computation it is the natural structure imposed by temporal ordering.

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

*Exact* under the assumption that $M_t$ is the complete epistemic substate ( #agent-model). If $M_t$ contains everything the agent retains from its history, then the update function needs only $M_t$ and the new event $e_\tau$ to produce $M_{t+1}$. The full history $\mathcal C_t$ is already summarized in $M_t$ by construction. For finite agents, recursion is *computational necessity*: re-processing the entire history at each event is infeasible. For agents with unlimited computation (e.g., an oracle that could re-derive $M_t$ from $\mathcal C_t$ at each step), recursion is still the natural structure but not strictly forced — the oracle could equivalently compute $\phi(\mathcal C_t \cup \{e_\tau\})$ directly. The unlimited-computation case is *discussion-grade*.

## Discussion

**Recursion as a consequence of completeness.** The recursive form is not an assumption bolted on — it follows from the definition of $M_t$ as complete. If $M_t$ were incomplete (if some relevant information lived outside $M_t$ in the raw history), then $f_M(M_{\tau^-}, e_\tau)$ would be insufficient and the agent would need to consult $\mathcal C_t$ directly. The sufficiency of the recursive form is precisely what #model-sufficiency measures: when $S(M_t) = 1$, the recursive update loses nothing.

**Between-event dynamics matter.** The autonomous evolution $g_M(M_\tau)$ is not merely filler between observations. It includes prediction generation (what the agent expects to see next), uncertainty growth (model confidence decaying over time without new data), and internal reorganization (consolidation, abstraction). In event-driven systems ( #event-driven-dynamics), the between-event interval is variable, making $g_M$ load-bearing for agents that must act or predict between observations.

**Connection to the update gain.** The event-driven update $f_M(M_{\tau^-}, e_\tau)$ is where the gain principle ( #update-gain) operates: $\eta^\ast$ determines how strongly $e_\tau$ shifts $M_t$ away from its prior value. The recursive form makes the gain's role explicit — it modulates the single-step correction.
