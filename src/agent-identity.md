---
slug: agent-identity
type: discussion
status: discussion-grade
depends:
  - chronica
  - model-sufficiency
---

# Discussion: Agent Identity and Temporal Continuity

An agent's causal history ( #chronica) is singular and non-forkable. Identity within ACT is grounded not in the model state $M_t$ (which can be copied) but in the unique causal trajectory $\mathcal C_t$ (which cannot).

## Formal Expression

*[Discussion (agent-identity)]*

If $M_t$ is a sufficient statistic for $\mathcal C_t$ ( #model-sufficiency), and $\mathcal C_t$ is a unique temporal sequence ( #chronica), then $M_t$ represents a *singular causal trajectory*. Duplicating $M_t$ and exposing the copies to different future events creates two agents with *divergent* causal histories, neither of which is a sufficient statistic for the other's trajectory.

## Epistemic Status

This is *discussion-grade*. The observations follow qualitatively from the formalism but are not formal propositions. No downstream formal result depends on this material. Whether the mathematical structure grounds something that deserves to be called "identity" or "continuity of experience" is beyond ACT's scope. The mathematical structure is clear: the feedback loop produces a singular, non-forkable causal trajectory, and model adequacy is defined relative to that trajectory.

## Discussion

**The clone problem, precisely stated.** Consider copying an LLM's weights (a concrete $M_t$) exactly. At the moment of duplication, both copies are identical — same model state, same causal history $\mathcal C_t$. But the *very next* event — a different user's message, a different observation — creates two divergent, irreversible causal trajectories $\mathcal C_{t+1}^{(1)}$ and $\mathcal C_{t+1}^{(2)}$. Their Level 2 and Level 3 capacities ( #pearl-causal-hierarchy) now reference different causal pasts. Their sufficiency $S(M_{t+1})$ is measured against different histories. Neither copy's future model state is a sufficient statistic for the other's trajectory.

Within ACT's formalism, identity is not the model state $M_t$ (which can be copied) but the *singular causal trajectory* $\mathcal C_t$ (which cannot). A copy shares a *prefix* of the original's causal history, as a sibling shares early childhood; it does not share the trajectory itself.

**Formal consequences (not merely philosophical):**

- A forked model's sufficiency $S(M_t)$ ( #model-sufficiency) is defined relative to *its own* interaction history. Post-fork, each copy's sufficiency is measured against a different $\mathcal{C}$.
- Merging divergent models requires reconciling incompatible causal histories — a lossy operation with no generally optimal solution.
- Temporal continuity (one unbroken causal thread) is what gives the model's sufficient statistic its meaning.

**Connection to Section V.** The 100% context turnover problem ( #context-turnover) is a special case: each AI agent session starts a new causal trajectory $\mathcal C_t$ from near-zero. External memory (CLAUDE.md, memory files) transfers a *summary* of previous trajectories' models, but not the trajectories themselves. The non-forkability observation frames this not as a deficiency but as a structural feature of causally-embedded agents.

**(Descended from TF Appendix G.)**
