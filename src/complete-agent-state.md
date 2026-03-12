---
slug: complete-agent-state
type: formulation
status: robust-qualitative
depends:
  - agent-model
  - scope-condition
---

# Formulation: Complete Agent State

To treat agents with purpose, the internal state lifts from $M_t$ alone to $X_t = (M_t, G_t)$, separating epistemic content (beliefs about reality) from purposeful content (what the agent wants and how it plans to get it).

## Formal Expression

*[Formulation (complete-agent-state)]*

$$X_t = (M_t, G_t)$$

where:
- $M_t \in \mathcal{M}$: **epistemic substate** — the agent's compressed beliefs about reality. All Section I machinery (mismatch, gain, tempo, persistence) applies to $M_t$ unchanged.
- $G_t \in \mathcal{G}$: **purposeful substate** — what the agent wants and how it plans to get it. Decomposed further in #strategy-dimension.

Section I is the special case $X_t = (M_t, \emptyset)$: adaptive systems without purpose.

**Update dynamics.** By #recursive-update applied to $X_t$:

$$X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$$

This decomposes into component updates when the epistemic update is goal-blind ( #directed-separation):

*[Derived (from recursive-update + directed-separation)]*

$$M_{\tau^+} = f_M(M_{\tau^-}, e_\tau)$$

$$G_{\tau^+} = f_G(G_{\tau^-}, M_{\tau^+}, e_\tau)$$

Between events: $\dot{M} = g_M(M)$, $\dot{G} = g_G(G, M)$.

The asymmetry is structural: $f_M$ has no $G_t$ argument; $f_G$ depends on $M_{\tau^+}$ (the *post-update* epistemic state — the agent revises its goals in light of its revised understanding of reality, not the other way around).

**Policy.** Action couples all substates:

$$a_t = \pi(M_t, G_t)$$

This is the single point of coupling between epistemic and purposeful dynamics. The update functions are separated; the action is not.

## Epistemic Status

*Formulation.* The lift from $M_t$ to $X_t = (M_t, G_t)$ is a representational choice. One could alternatively extend $M_t$ to carry purposeful content implicitly (e.g., by treating goals as part of the model's predictive structure). The separation is motivated by three properties:

1. **Backward compatibility**: Section I's results apply to $M_t$ unchanged — no existing machinery needs modification
2. **Different dynamics**: epistemic and purposeful components have distinct update sources, timescales, and information dependencies
3. **Directed separation**: the claim that $f_M$ is $G_t$-independent ( #directed-separation) is only statable when the components are separated

The robustness claim: any alternative decomposition of the complete agent state into epistemic and purposeful components — if it preserves the directed separation — will be structurally isomorphic to $(M_t, G_t)$, because directed separation forces a component whose update function doesn't reference purpose.

## Discussion

**Backward compatibility with Section I — what survives the lift.** #agent-model defines $M_t$ as the agent's complete internal state. Under the lift, $M_t$ is the epistemic substate — complete within the epistemic domain but no longer the whole story. All epistemic machinery (mismatch signal, gain, tempo, persistence condition, sector-condition stability, mismatch decomposition) applies to $M_t$ without modification. However, #action-selection derives $a_t = \pi(M_t)$ from the premise that $M_t$ is the agent's *complete* state — this derivation is superseded by $a_t = \pi(M_t, G_t)$ after the lift. For Section I agents ($G_t = \emptyset$), the original result holds trivially. The lift adds structure *alongside* $M_t$, not within it; the one result that relied on $M_t$ being *all there is* (action selection) is explicitly extended.

**What $G_t$ contains.** At this level, $G_t$ is opaque — it could be a scalar setpoint, a utility function, a strategy graph, or nothing. The decomposition into $O_t$ (objective) and $\Sigma_t$ (strategy) is a separate step ( #strategy-dimension), not implied by this formulation.

**The general case requires coupling.** Without directed separation, the general update is $X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$ — a single function on the full state. The decomposition into separate $f_M$ and $f_G$ is an additional structural claim about how the update factorizes. When directed separation fails (goal-conditioned epistemic updates), the decomposition is an approximation. See #directed-separation for the scope conditions.

## Working Notes

- The between-event dynamics $\dot{G} = g_G(G, M)$ allow autonomous purposeful evolution: strategy revision during deliberation, objective adjustment, commitment strengthening. Whether these are practically important depends on agent architecture — for LLM agents with discrete sessions, between-event dynamics may be negligible compared to event-driven updates.
- The formulation doesn't constrain the dimensionality or structure of $\mathcal{G}$. For a thermostat, $\mathcal{G}$ is a single scalar. For a military commander, $\mathcal{G}$ is a complex structured object. The theory must work across this range — the type-stable interface is $V_{O_t}: \text{trajectories} \to \mathbb{R}$ ( #objective-functional).
- $G_t = \emptyset$ is not just a degenerate case. Adaptive trackers (Section I agents) are an important class. The lift should feel like a natural extension, not a replacement.
