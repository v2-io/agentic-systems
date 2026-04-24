---
slug: postulate-composition-consistency
type: postulate
status: axiomatic
depends:
  - scope-agency
stage: deps-verified
---

# Postulate: Composition Consistency

AAD's predictions must be compatible across levels of description. If a system $S$ and its decomposition $\{S_1, \ldots, S_n\}$ both satisfy the scope condition, the theory's claims at the $S$-level and at the $\{S_i\}$-level cannot contradict each other. This cross-level compatibility is a structural requirement for AAD's internal coherence — the scope condition does not restrict which level the theory applies to, so the theory must be level-invariant in its predictions.

The operational consequences — when a decomposed system actually behaves as a single composite agent, and which Section I/II results carry across decompositions — are *derived* from this postulate under specific conditions: the composition scope condition ( #scope-composite-agent, teleological alignment threshold) determines *which* groups are composites; the composition closure criterion ( #composition-closure, admissibility conditions (A1)-(A4) and bridge lemma) determines *how faithfully* macro-dynamics track micro-dynamics for those groups; and the tier-specific contraction assumption in the bridge lemma ( #composition-closure Epistemic Status) determines *which* composites admit the cleanest cross-level transfer of results.

## Formal Expression

*[Postulate (postulate-composition-consistency)]*

For any system $S$ satisfying the scope condition ( #scope-agency), and any decomposition of $S$ into subsystems $\{S_1, \ldots, S_n\}$ where each $S_i$ also satisfies the scope condition, AAD's predictions at the system level must be compatible with its predictions at the subsystem level. Specifically, composition laws must exist such that:

1. **Tempo composition**: $\mathcal T_S$ is expressible as a function of $\{\mathcal T_{S_i}\}$ and the coordination structure among them
2. **Persistence compatibility**: the system's persistence is derivable from the sub-agents' individual persistence conditions plus coordination structure
3. **Mismatch consistency**: $\delta_S$ is derivable from $\{\delta_{S_i}\}$ and their interaction structure

*[Structural consequence (derivation hierarchy)]*

Cross-level compatibility requires three successively more specific conditions, each with its own segment in Section III:

1. **Scope**: The decomposition is a *composite* (not merely a multi-agent system) when #scope-composite-agent is satisfied — teleological alignment via at least one of three disjunctive routes (shared objective, hierarchical derivation, or mutual benefit). Without scope-satisfaction via any route, level-compatibility is vacuous (composition quantities are not well-defined, so there is nothing to be consistent about).

2. **Admissibility**: Given a composite, its macro-dynamics are well-posed when the closure admissibility conditions (A1)-(A4) hold ( #composition-closure). These require AAD-shaped macro-state, macro-mismatch, macro-tempo, and sector-bounded correction at the composite level.

3. **Transfer of results**: Individual Section I/II results lift to the composite level through the bridge lemma in #composition-closure, which requires a *tier-specific contraction assumption* beyond (A4). For **Tier 1** agents (all Bayesian updaters on exponential families, linear correctors with positive-definite gain, gradient descent on strongly convex losses), the contraction holds and Section I results transfer exactly. For **Tier 2** agents (locally convex, nonlinear prediction models), transfer holds locally with factor degradation. For **Tier 3** agents (non-convex optimization, discontinuous corrections, non-mismatch-driven state), contraction must be verified per-domain and Section I results do not automatically lift.

*[Heuristic (timescale separation)]*

**Timescale separation as a practical screening test.** When internal equilibration timescale $\tau_{\text{eq}}$ — the time for sub-agents to approximately synchronize models and coordinate actions — is short relative to the external dynamics timescale $\tau_{\text{ext}}$:

$$\tau_{\text{eq}} \ll \tau_{\text{ext}}$$

the composite description is likely well-posed. This is a *heuristic sufficient condition* — not a theorem, but a reliable practical test: domain examples (software team on daily standups vs. weekly deadlines; military squad on voice vs. minutes-scale engagement) suggest the threshold is easily satisfied in common organizational settings. The heuristic is the operational analog of the persistence condition ( #persistence-condition): just as an individual agent requires correction faster than disturbance, a composite requires internal coordination faster than external change. The formal theorem corresponding to this heuristic requires the composition-closure bridge lemma with its tier-specific contraction assumption; the heuristic is usable in practice without the theorem because the gap between "passes timescale separation" and "meets Tier 1 conditions" is small in common settings.

## Epistemic Status

*Axiomatic* for the meta-requirement (cross-level compatibility). The postulate itself is a structural requirement for AAD's internal consistency: if the scope condition doesn't restrict which level the theory applies to, the predictions must not contradict across levels.

The operational consequences decompose into three layers with distinct epistemic statuses:

- **Scope selection** ( #scope-composite-agent, robust-qualitative): which decompositions constitute composites. The scope condition is a disjunction of three qualitatively distinct routes (shared objective, hierarchical derivation, mutual benefit); whether they reduce to a common scalar threshold is open. Coverage of well-understood cases holds via the disjunction.

- **Admissibility of composite dynamics** ( #composition-closure, conditional): the (A1)-(A4) conditions are stated formally; the bridge lemma is conditional on the incremental sector bound (DA2'-inc), strictly stronger than (A4) alone.

- **Transfer of individual-agent results** (tier-dependent): Tier 1 composites transfer Section I/II results exactly; Tier 2 transfer with degraded factors; Tier 3 require per-domain verification. This is the sharpest scoping of "every result applies at every level" — it applies at every level *for Tier 1 composites*, degrades gracefully for Tier 2, and holds per-domain for Tier 3.

The timescale separation heuristic is a practical screening condition whose formal counterpart sits in Tier 1 of the #composition-closure bridge lemma. It is usable without proving the theorem in full because common organizational settings satisfy both the heuristic and the Tier 1 conditions.

## Discussion

**The same pattern as individual persistence.** The persistence condition says: there is a measurable threshold below which an individual agent's mismatch grows without bound and the agent degrades. Composition consistency says the same thing at the composite level: there is a measurable threshold ($\tau_{\text{eq}} / \tau_{\text{ext}}$, or more precisely the tier-specific contraction factor from #composition-closure) below which the composite description breaks down. In both cases, most competent agents are comfortably above the threshold — the theory applies broadly, and the edge cases are where it gets interesting.

**What this buys the theory.** With composition consistency stated early:
- Section I/II results lift to the composite level *for Tier 1 composites passing the composition scope condition*, with degraded-factor lift for Tier 2 and per-domain verification for Tier 3 — the three-layer decomposition above makes this precise rather than leaving "applies at every level" as an unbounded claim
- Section III becomes the study of *what happens near and beyond the threshold* — coordination overhead, unity dimensions, symbiogenic transitions, adversarial dynamics — rather than a separate multi-agent theory
- The formal test for composition validity ( #composition-closure) develops the rigorous version of the timescale condition, with the incremental sector bound identifying which agent classes admit the contraction needed for cross-level transfer

**When composition fails.** The timescale condition fails when:
- Internal coordination slows (communication overhead scales poorly, conflicts consume attention, bureaucratic process)
- External dynamics accelerate (adversary acts faster, market shifts, crisis compresses decision timescales)
- Both simultaneously (the classic organizational failure mode — internal friction increases while external demands intensify)

This is the formal analog of Brooks's Law: adding people to a late project increases $\tau_{\text{eq}}$ (more coordination) while $\tau_{\text{ext}}$ stays fixed (the deadline doesn't move). Eventually $\tau_{\text{eq}}$ exceeds $\tau_{\text{ext}}$ and the composite ceases to function as a coherent agent. The model captures the same structural pattern; whether the specific mechanism (timescale crossing) is the actual cause of Brooks's Law is an empirical question.

**The boundary is a modeling choice.** A development team is simultaneously: individual developers (each an AAD agent), the team (a composite AAD agent), and part of an organization (a sub-agent within a larger composite). The scope condition is satisfied at every level. Composition consistency ensures the theory doesn't give contradictory answers about observable quantities (e.g., whether the team persists) regardless of which boundary is chosen.

**What composition consistency does NOT say.** It does not specify the form of the composition laws — those are derived in Section III ( #tempo-composition). It does not say every decomposition is equally useful for analysis. And it does not require perfect internal coordination — only that internal equilibration is fast relative to external dynamics.

## Working Notes
- The timescale separation condition is essentially the singular perturbation argument from #temporal-nesting applied to composition: the fast internal dynamics approximately equilibrate, and the composite's behavior is described by the slow (external) dynamics on the equilibrium manifold. The formal connection should be made explicit when temporal-nesting is reviewed.
- Composition of directed separation: if each sub-agent's $f_M$ is $G_t$-independent, does the composite's $f_M^c$ remain $G_t^c$-independent? Hypothesis: goal-blindness composes, BUT coordination routing may break it — if which observations reach the composite depends on the shared objective, the composite's effective observation function is goal-dependent. This is the organizational analog of the LLM scope restriction in #directed-separation.
- The "atomic agent" question: if every agent is decomposable, where does it bottom out? At agents whose internal dynamics are not usefully described by AAD — below the level where observations, actions, and uncertainty exist, the scope condition fails and the recursion terminates.
- The relationship to holons (Koestler 1967): an AAD agent satisfying composition consistency is a holon — simultaneously a whole (analyzable as a single agent) and a part (decomposable into sub-agents). The term is occasionally useful but carries significant mystical baggage from later appropriations. Use sparingly.
