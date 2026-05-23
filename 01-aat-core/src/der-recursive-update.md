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

The first major *derived* result of the volume: the model update function must be recursive. Each new model state $M_{\tau^+}$ depends only on the previous model state $M_{\tau^-}$ and the incoming event $e_\tau$ — not on the full chronica. The result follows from three constraints already in place: the temporal-ordering postulate ( #post-causal-structure — the model at time $t$ can only depend on prior events), the partial-observability scope ( #def-observation-function — the agent has no direct access to the environment beyond events), and the completeness commitment in the model formulation ( #form-agent-model — $M_t$ summarizes everything the agent retains). Together these force the update into the recursive form; the appendix derivation ( #deriv-recursive-update) works through seven counterexample attacks to confirm there is no escape from this form once the three constraints are accepted.

The epistemic character of this result is honest. Temporal ordering is a physical postulate and partial observability is a scope condition, but the completeness commitment is *definitional* — it cannot be "violated" because any apparent violation is absorbed by expanding $M_t$. The Markov structure of the update is therefore not discovered in the environment but chosen through the definition of $M_t$ as complete. This is not a weakness; it is the precise character of the claim. For finite agents recursion is forced by *computational realism* as well: re-processing the full history at each event is infeasible.

The formulation also surfaces **between-event dynamics** — autonomous evolution of the model state during the gaps between observation arrivals — as load-bearing rather than filler. These include prediction generation (anticipating the next observation), uncertainty growth (confidence decay over time without new data), and internal reorganization (consolidation, abstraction). When between-event dynamics are driven by replayed or internally-generated pseudo-events and the objective is information-bottleneck-gap reduction rather than one-step mismatch minimization, the framework names this the *consolidation regime* ( #form-consolidation-dynamics) — a separate operating mode with its own scope condition ($\nu_{\text{consol}} \ll \nu_{\text{online}}$) and its own necessity condition.

## Formal Expression

*[Derived (recursive-update, from temporal postulate and $M_t$ completeness)]*

**Event-driven update:**

$$M_{\tau^+} = f_M(M_{\tau^-}, e_\tau)$$

where:
- $M_{\tau^-}$ is the model state immediately before event $e_\tau$
- $M_{\tau^+}$ is the model state immediately after
- $f_M$ is the update function — it takes the current model and the new event, not the full history $\mathcal{C}_t$

**Between-event evolution:**

$$\frac{dM}{d\tau} = g_M(M_\tau)$$

Between events, the model evolves autonomously — internal reorganization, prediction generation, decay of transient states. The between-event dynamics depend only on the current model state, not on external input (which, by definition, arrives only at events).

## Epistemic Status

*Exact, with a partly definitional character.* The result follows from three constraints: temporal ordering (C1 — physical law), partial observability (C2 — scope definition), and state completeness (C3 — analytical commitment that $M_t$ summarizes everything the agent retains). C1 and C2 do genuine eliminative work; C3 is definitional — it cannot be "violated" because any violation is absorbed by expanding $M_t$. The Markov structure is therefore not discovered in the environment but chosen through the definition of $M_t$ as complete. This is not a weakness — it is the nature of the claim: recursive update is the only form consistent with C1 + C2 + the definition of $M_t$ as complete (see #deriv-recursive-update for the full argument and seven counterexample attacks). For finite agents, recursion is also *computational necessity*: re-processing the full history at each event is infeasible.

## Discussion

**Recursion as a consequence of completeness.** The recursive form is not an assumption bolted on — it follows from the definition of $M_t$ as complete. If $M_t$ were incomplete (if some relevant information lived outside $M_t$ in the raw history), then $f_M(M_{\tau^-}, e_\tau)$ would be insufficient and the agent would need to consult $\mathcal{C}_t$ directly. The sufficiency of the recursive form is precisely what #def-model-sufficiency measures: when $S(M_t) = 1$, the recursive update loses nothing.

**Between-event dynamics matter.** The autonomous evolution $g_M(M_\tau)$ is not merely filler between observations. It includes prediction generation (what the agent expects to see next), uncertainty growth (model confidence decaying over time without new data), and internal reorganization (consolidation, abstraction). In event-driven systems ( #form-event-driven-dynamics), the between-event interval is variable, making $g_M$ load-bearing for agents that must act or predict between observations. When the between-event dynamics are driven by replayed or internally-generated pseudo-events and the update objective is IB-gap reduction rather than one-step mismatch minimization, $g_M$ is operating in the *consolidation regime* per #form-consolidation-dynamics — a named regime with its own scope condition ($\nu_{\text{consol}} \ll \nu_{\text{online}}$) and its own necessity condition (sub-state factorization + bounded per-event budget). Consolidation is where the stability-plasticity feasibility window complements #schema-strategy-persistence's plasticity lower bound.

**Connection to the update gain.** The event-driven update $f_M(M_{\tau^-}, e_\tau)$ is where the gain principle ( #emp-update-gain) operates: $\eta^\ast$ determines how strongly $e_\tau$ shifts $M_t$ away from its prior value. The recursive form makes the gain's role explicit — it modulates the single-step correction.
