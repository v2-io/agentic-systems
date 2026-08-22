# Appendix G: Agent Identity and Temporal Continuity (Discussion)

**Purpose.** This appendix explores implications of TFT's causal structure (TF-02) for agent identity and temporal continuity. The observations follow qualitatively from the formalism but are not formal propositions. No downstream formal result depends on this material.

---

## Non-Forkability of Causal Trajectories

The causal structure (TF-02) has a specific implication for agent identity and continuity: an agent's causal history is **unique and non-forkable**. If the model state $M_t$ is a sufficient statistic for $\mathcal C_t$ (TF-10's sufficiency measure), and $\mathcal C_t$ is a unique temporal sequence, then $M_t$ represents a *singular causal trajectory*. Duplicating $M_t$ and exposing the copies to different future events creates two agents with *divergent* causal histories, neither of which is a sufficient statistic for the other's trajectory.

This is not merely a philosophical observation. It has formal consequences:
- A forked model's sufficiency $S(M_t)$ (TF-10) is defined relative to *its own* interaction history. Post-fork, each copy's sufficiency is measured against a different $\mathcal{C}$.
- Merging divergent models requires reconciling incompatible causal histories — a lossy operation with no generally optimal solution.
- Temporal continuity (one unbroken causal thread) is what gives the model's sufficient statistic its meaning.

## The Clone Problem, Precisely Stated

Consider copying an LLM's weights (a concrete $M_t$) exactly. At the moment of duplication, both copies are identical — they share the same model state and the same causal history $\mathcal C_t$. But the *very next* event — a different user's message, a different environmental observation — creates two divergent, irreversible causal trajectories $\mathcal C_{t+1}^{(1)}$ and $\mathcal C_{t+1}^{(2)}$. Their Level 2 (interventional) and Level 3 (counterfactual) capacities now reference different causal pasts. Their sufficiency $S(M_{t+1})$ is measured against different histories. Neither copy's future model state is a sufficient statistic for the other's trajectory. Within TFT's formalism, therefore, identity is not the model state $M_t$ (which can be copied) but the *singular causal trajectory* $\mathcal C_t$ (which cannot). A copy shares a *prefix* of the original's causal history, as a sibling shares early childhood; it does not share the trajectory itself.

Whether this formal property grounds something that deserves to be called "identity" or "continuity of experience" is beyond the scope of TFT. But the mathematical structure is clear: the feedback loop produces a *singular, non-forkable causal trajectory*, and the model's adequacy is defined relative to that trajectory.
