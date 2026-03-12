---
slug: composition-consistency
type: axiom
status: first-principled
depends:
  - scope-condition
---

# Composition Consistency

ACT's predictions must be compatible across levels of description. If a system satisfies the scope condition and can be decomposed into subsystems that each independently satisfy the scope condition, the theory's predictions at the system level must not contradict its predictions at the subsystem level.

## Formal Expression

*[Axiom (composition-consistency)]*

For any system $S$ satisfying the scope condition ( #scope-condition), and any decomposition of $S$ into subsystems $\{S_1, \ldots, S_n\}$ where each $S_i$ also satisfies the scope condition:

1. **Tempo composition**: $\mathcal{T}_S$ must be expressible as a function of $\{\mathcal{T}_{S_i}\}$ and the coordination structure among them
2. **Persistence compatibility**: If $S$ persists ($\mathcal{T}_S > \rho_S / \|\delta_{\text{critical}}^S\|$), this must be derivable from the sub-agents' individual persistence conditions plus coordination structure
3. **Mismatch consistency**: $\delta_S$ must be derivable from $\{\delta_{S_i}\}$ and their interaction structure

"Compatible" means: the predictions at different levels may concern different quantities (different levels see different observables), but they must not give contradictory answers about shared observables. The choice of boundary is a modeling decision, not a physical fact — the same physical system is being described.

## Epistemic Status

*First-principled.* This is a structural requirement for ACT's internal consistency, not a claim about the world. If the scope condition ( #scope-condition) does not restrict which level of description the theory applies to — and it does not — then the theory must give non-contradictory answers regardless of where the agent boundary is drawn. A theory whose predictions depend on an arbitrary modeling choice (where to draw the boundary) would undermine its own claims to generality.

The axiom is analogous to the requirement in physics that laws hold across scales. The specific *composition laws* that satisfy this requirement are formulation choices (Section III); the *requirement* that such laws exist is not.

## Discussion

**Why this is an axiom, not a derived result.** The argument that ACT must be consistent across levels is compelling — it follows from the scope condition's level-independence. But it is not a *derivation* in the mathematical sense. It is a coherence requirement on the theory itself: we demand this property because a theory that lacks it is defective. We state it as an axiom so that every subsequent result is automatically understood to hold at every level of composition.

**What this buys the theory.** With composition consistency stated early:
- All Section I and II results (persistence, gain, tempo, mismatch decomposition, orient cascade) hold at every level of composition without re-derivation
- Section III becomes the study of *imperfect composition* — what happens when the coordination structure introduces friction — rather than a separate multi-agent theory
- The formal test for valid composition ( #composition-closure) operationalizes this axiom's requirement

**The boundary is a modeling choice.** A development team is simultaneously: individual developers (each an ACT agent), the team (a composite ACT agent), and part of an organization (a sub-agent within a larger composite). The scope condition is satisfied at every level. Composition consistency ensures the theory doesn't give contradictory answers about observable quantities (e.g., whether the team persists) regardless of which boundary is chosen.

**What composition consistency does NOT say.** It does not say the composition laws take any particular form. The specific relationship between $\mathcal{T}_S$ and $\{\mathcal{T}_{S_i}\}$ is derived in Section III ( #tempo-composition). It does not say the subsystems must be "well-behaved" — composition consistency holds even for adversarial sub-agents (where the coordination structure works against the composite). It does not say every decomposition is equally useful for analysis.

## Working Notes
- The relationship to holons (Koestler 1967): an ACT agent satisfying composition consistency is a holon — simultaneously a whole (analyzable as a single agent) and a part (decomposable into sub-agents). The term is occasionally useful but carries significant mystical baggage from later appropriations. Use sparingly.
- Composition of directed separation: if each sub-agent's $f_M$ is $G_t$-independent, does the composite's $f_M^c$ remain $G_t^c$-independent? Hypothesis: goal-blindness composes, BUT coordination routing may break it — if which observations reach the composite depends on the shared objective, the composite's effective observation function is goal-dependent. This is the organizational analog of the LLM scope restriction in #directed-separation.
- The "atomic agent" question: if every agent is decomposable, where does it bottom out? At agents whose internal dynamics are not usefully described by ACT — below the level where observations, actions, and uncertainty exist, the scope condition fails and the recursion terminates.
