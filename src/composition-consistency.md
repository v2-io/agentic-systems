---
slug: composition-consistency
type: postulate
status: axiomatic
depends:
  - scope-condition
---

# Postulate: Composition Consistency

ACT applies at every level of description where the scope condition is met. A team of agents is itself an agent; a department of teams is itself an agent. The theory's predictions at each level must be compatible — and they are, under a condition analogous to the persistence threshold: the composite's internal coordination must be fast relative to the external dynamics it faces.

## Formal Expression

*[Postulate (composition-consistency)]*

For any system $S$ satisfying the scope condition ( #scope-condition), and any decomposition of $S$ into subsystems $\{S_1, \ldots, S_n\}$ where each $S_i$ also satisfies the scope condition, ACT's predictions at the system level must be compatible with its predictions at the subsystem level. Specifically, composition laws must exist such that:

1. **Tempo composition**: $\mathcal T_S$ is expressible as a function of $\{\mathcal T_{S_i}\}$ and the coordination structure among them
2. **Persistence compatibility**: the system's persistence is derivable from the sub-agents' individual persistence conditions plus coordination structure
3. **Mismatch consistency**: $\delta_S$ is derivable from $\{\delta_{S_i}\}$ and their interaction structure

*[Sufficient Condition (composition-validity)]*

**Timescale separation condition.** A group of sub-agents behaves as a valid composite agent when its internal equilibration timescale $\tau_{\text{eq}}$ — the time for sub-agents to approximately synchronize models and coordinate actions — is short relative to the external dynamics timescale $\tau_{\text{ext}}$ — the time for the environment to change significantly from the macro-agent's perspective:

$$\tau_{\text{eq}} \ll \tau_{\text{ext}}$$

When this holds, the internal dynamics have approximately settled by the time the next external challenge arrives, and the composite's macro-state is predictive of its macro-behavior. This is the composition analog of the persistence condition ( #persistence-condition): just as an individual agent requires $\mathcal{T} \gt \rho / \Vert\delta_{\text{critical}}\Vert$ to maintain bounded mismatch, a composite agent requires fast internal coordination to maintain a coherent macro-description.

Most functioning groups easily satisfy this condition. A software team with daily standups and shared CI ($\tau_{\text{eq}} \sim$ hours) facing weekly feature deadlines ($\tau_{\text{ext}} \sim$ weeks) is comfortably a valid composite. A military squad communicating by voice ($\tau_{\text{eq}} \sim$ seconds) in a tactical situation evolving over minutes is clearly a single agent. The theory applies broadly; the interesting questions arise near the threshold.

## Epistemic Status

*Axiomatic.* The meta-requirement (cross-level compatibility) is a structural requirement for ACT's internal consistency — if the scope condition doesn't restrict which level the theory applies to, the predictions must not contradict across levels. The timescale separation condition is stated here as a sufficient condition for practical composition; its formal derivation requires the composition closure criterion ( #composition-closure) and the tempo composition inequality ( #tempo-composition) developed in Section III. The condition is not yet proved; it is stated early because it is intuitive, likely correct, and gives readers an immediate practical test.

## Discussion

**The same pattern as individual persistence.** The persistence condition says: there is a measurable threshold below which an individual agent's mismatch grows without bound and the agent degrades. Composition consistency says the same thing at the composite level: there is a measurable threshold ($\tau_{\text{eq}} / \tau_{\text{ext}}$) below which the composite description breaks down. In both cases, most competent agents are comfortably above the threshold — the theory applies broadly, and the edge cases are where it gets interesting.

**What this buys the theory.** With composition consistency stated early:
- Every subsequent result (persistence, gain, tempo, mismatch decomposition, orient cascade) is understood to apply at every level of composition where the timescale condition holds
- Section III becomes the study of *what happens near and beyond the threshold* — coordination overhead, unity dimensions, adversarial dynamics — rather than a separate multi-agent theory
- The formal test for composition validity ( #composition-closure) provides the rigorous version of the timescale condition

**When composition fails.** The timescale condition fails when:
- Internal coordination slows (communication overhead scales poorly, conflicts consume attention, bureaucratic process)
- External dynamics accelerate (adversary acts faster, market shifts, crisis compresses decision timescales)
- Both simultaneously (the classic organizational failure mode — internal friction increases while external demands intensify)

This is the formal analog of Brooks's Law: adding people to a late project increases $\tau_{\text{eq}}$ (more coordination) while $\tau_{\text{ext}}$ stays fixed (the deadline doesn't move). Eventually $\tau_{\text{eq}}$ exceeds $\tau_{\text{ext}}$ and the composite ceases to function as a coherent agent. The model captures the same structural pattern; whether the specific mechanism (timescale crossing) is the actual cause of Brooks's Law is an empirical question.

**The boundary is a modeling choice.** A development team is simultaneously: individual developers (each an ACT agent), the team (a composite ACT agent), and part of an organization (a sub-agent within a larger composite). The scope condition is satisfied at every level. Composition consistency ensures the theory doesn't give contradictory answers about observable quantities (e.g., whether the team persists) regardless of which boundary is chosen.

**What composition consistency does NOT say.** It does not specify the form of the composition laws — those are derived in Section III ( #tempo-composition). It does not say every decomposition is equally useful for analysis. And it does not require perfect internal coordination — only that internal equilibration is fast relative to external dynamics.

## Working Notes
- The timescale separation condition is essentially the singular perturbation argument from #temporal-nesting applied to composition: the fast internal dynamics approximately equilibrate, and the composite's behavior is described by the slow (external) dynamics on the equilibrium manifold. The formal connection should be made explicit when temporal-nesting is reviewed.
- Composition of directed separation: if each sub-agent's $f_M$ is $G_t$-independent, does the composite's $f_M^c$ remain $G_t^c$-independent? Hypothesis: goal-blindness composes, BUT coordination routing may break it — if which observations reach the composite depends on the shared objective, the composite's effective observation function is goal-dependent. This is the organizational analog of the LLM scope restriction in #directed-separation.
- The "atomic agent" question: if every agent is decomposable, where does it bottom out? At agents whose internal dynamics are not usefully described by ACT — below the level where observations, actions, and uncertainty exist, the scope condition fails and the recursion terminates.
- The relationship to holons (Koestler 1967): an ACT agent satisfying composition consistency is a holon — simultaneously a whole (analyzable as a single agent) and a part (decomposable into sub-agents). The term is occasionally useful but carries significant mystical baggage from later appropriations. Use sparingly.
