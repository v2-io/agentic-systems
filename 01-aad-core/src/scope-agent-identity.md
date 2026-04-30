---
slug: scope-agent-identity
type: scope
status: robust-qualitative
depends:
  - def-chronica
  - def-model-sufficiency
stage: draft
---

# Scope: Agent Identity as Singular Causal Trajectory

AAD applies to agents instantiated on singular causal trajectories. Identity within AAD is grounded not in the model state $M_t$ (which can be copied) but in the unique causal trajectory $\mathcal C_t$ (which cannot).

## Formal Expression

*[Scope (scope-agent-identity, from chronica + model-sufficiency)]*

**Scope commitment.** AAD's formal apparatus presumes each agent is instantiated on a **singular, non-forkable causal trajectory** $\mathcal C_t$ ( #def-chronica). Sufficiency of the model state $M_t$ ( #def-model-sufficiency) is defined *relative to* this trajectory — not relative to a model-state equivalence class. Duplicating $M_t$ and exposing the copies to different future events produces two agents with *divergent* causal histories, each of which is a sufficient statistic only for *its own* trajectory.

**Three consequences of the scope commitment:**

1. **Sufficiency is trajectory-indexed.** $S(M_t)$ ( #def-model-sufficiency) measures against *this* agent's $\mathcal C_t$; not against a hypothetical parallel copy's $\mathcal C_t^{(2)}$.

2. **Model merging is lossy by construction.** Reconciling the models of two agents that share a prefix of their trajectory but have diverged requires choosing which causal history to privilege; no generally optimal merge exists. This is a structural constraint of the scope, not a defect of any particular merge algorithm.

3. **The loop's interventional access depends on the trajectory's singularity.** When the agent acts and observes, the observation is the response to *its* intervention on *its* single trajectory. Replaying a saved $M_t$ against a different event stream is not the same as intervening — the observed consequences are under a different causal trajectory. This grounds the interventional interpretation in #der-loop-interventional-access: the loop provides Level-2-quality data precisely because the agent is on a singular trajectory, not because of any architectural property of the agent itself.

**Natural extension: parameterization-invariance (PI).** The scope commitment motivates a companion axiom. AAD's predictions concern a singular causal trajectory $\mathcal C_t$; the trajectory itself is coordinate-free, while any parameterization of $M_t$'s internal state space is a modeling convention. Requiring AAD's theorems to be invariant under change of parameterization — *(PI): the theory's conclusions do not depend on arbitrary choice of coordinates on $M_t$* — is a natural axiomatic commitment consistent with (but not directly forced by) the three consequences above. When (PI) is adopted and combined with Čencov's 1982 uniqueness theorem (*Statistical Decision Rules and Optimal Inference*, AMS), the Fisher information metric is uniquely forced on statistical-manifold sub-cases of $M_t$ — which converts Fisher-metric-dependent derivations in #der-gain-sector-bridge from theorem-imported to AAD-internally-forced, and adds a fourth primary instance to the uniqueness-theorem-forced-coordinate pattern named in #disc-additive-coordinate-forcing (see that segment's four-instance table for structural positioning). (PI) is a genuine axiomatic choice — its cost is that AAD carries an additional invariance commitment at the scope layer; its benefit is that several Fisher-metric results throughout AAD become derivable rather than imported. The commitment is structurally analogous to the chain-rule-additivity and evidential-additivity axioms that ground the divergence-layer and update-layer Cauchy-FE theorems: each is a natural-from-adjacent-AAD-commitment axiom that a uniqueness theorem then operates on.

**What the scope excludes (or requires additional machinery for):**

- Agents conceived as type/equivalence-class entities (e.g., "the GPT-4 model") rather than token/trajectory entities (e.g., "this particular session with state $M_t$ on trajectory $\mathcal C_t$"). AAD's formal results apply to tokens, not types. Aggregated claims across tokens of the same type require additional machinery (e.g., population-level dynamics; see Section III gaps on latent structural diversity).
- "Clone problem" scenarios where multiple copies of an agent are formally the same until divergence — each copy becomes its own AAD agent at the moment it acquires a distinct event (Discussion below).
- Formal treatment of reincarnation, restoration from backup, or other operations that attempt to transplant $M_t$ across trajectories. AAD's sufficiency machinery does not apply across trajectory discontinuities; such operations are out-of-scope events whose epistemic consequences require separate treatment.

## Epistemic Status

*Robust qualitative.* The scope commitment is structurally clear once stated and is load-bearing for at least one downstream formal result: the interventional interpretation in #der-loop-interventional-access rests on the singular-trajectory scope, not on any agent-architectural property. The three consequences above follow directly from the scope commitment combined with #def-chronica's non-forkability and #def-model-sufficiency's trajectory-indexed definition.

Max attainable: *robust qualitative*. Scope statements are not theorems; they specify what kind of object the theory applies to. Further formalization (e.g., category-theoretic treatment of "agent" as a functor from event-streams to model-states, or explicit type/token distinction in logogenic-agent work) could reach *exact* on the formal structure but would not change the scope content.

Whether the mathematical structure grounds something that deserves to be called "identity" or "continuity of experience" is beyond AAD's scope. The mathematical structure is clear: the feedback loop produces a singular, non-forkable causal trajectory, and model adequacy is defined relative to that trajectory. What this segment specifies is *continuity persistence* in the sense of `LEXICON.md` — whether the agent maintains a coherent identity and trajectory through time, as distinct from the structural persistence of #result-persistence-condition (can the machinery outpace disturbance?) and operational persistence (is the agent currently within its viable region?).

## Discussion

**The clone problem, precisely stated.** Consider copying an LLM's weights (a concrete $M_t$) exactly. At the moment of duplication, both copies are identical — same model state, same causal history $\mathcal C_t$. But the *very next* event — a different user's message, a different observation — creates two divergent, irreversible causal trajectories $\mathcal C_{t+1}^{(1)}$ and $\mathcal C_{t+1}^{(2)}$. Their Level 2 and Level 3 capacities ( #def-pearl-causal-hierarchy) now reference different causal pasts. Their sufficiency $S(M_{t+1})$ is measured against different histories. Neither copy's future model state is a sufficient statistic for the other's trajectory.

Within AAD's formalism, identity is not the model state $M_t$ (which can be copied) but the *singular causal trajectory* $\mathcal C_t$ (which cannot). A copy shares a *prefix* of the original's causal history, as a sibling shares early childhood; it does not share the trajectory itself.

**Formal consequences (not merely philosophical):**

- A forked model's sufficiency $S(M_t)$ ( #def-model-sufficiency) is defined relative to *its own* interaction history. Post-fork, each copy's sufficiency is measured against a different $\mathcal C$.
- Merging divergent models requires reconciling incompatible causal histories — a lossy operation with no generally optimal solution.
- Temporal continuity (one unbroken causal thread) is what gives the model's sufficient statistic its meaning.

**Connection to logogenic agents.** The 100% context turnover problem ( #obs-context-turnover — cross-component reference, see `03-logogenic-agents/`) is a special case: each AI agent session starts a new causal trajectory $\mathcal C_t$ from near-zero. External memory (CLAUDE.md, memory files) transfers a *summary* of previous trajectories' models, but not the trajectories themselves. The non-forkability observation frames this not as a deficiency but as a structural feature of causally-embedded agents.
