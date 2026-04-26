---
slug: post-composition-consistency
type: postulate
status: axiomatic
depends:
  - scope-agency
stage: deps-verified
---

# Postulate: Composition Consistency

AAD's predictions must be compatible across levels of description. If a system $S$ and its decomposition $\{S_1, \ldots, S_n\}$ both satisfy the scope condition, the theory's claims at the $S$-level and at the $\{S_i\}$-level cannot contradict each other. This cross-level compatibility is a structural requirement for AAD's internal coherence — the scope condition does not restrict which level the theory applies to, so the theory must be level-invariant in its predictions.

The operational consequences — when a decomposed system actually behaves as a single composite agent, and which Section I/II results carry across decompositions — are *derived* from this postulate under specific conditions: the composition scope condition ( #scope-composite-agent, teleological alignment threshold) determines *which* groups are composites; the composition closure criterion ( #form-composition-closure, admissibility conditions (A1)-(A4) and bridge lemma) determines *how faithfully* macro-dynamics track micro-dynamics for those groups; and the tier-specific contraction assumption in the bridge lemma ( #form-composition-closure Epistemic Status) determines *which* composites admit the cleanest cross-level transfer of results.

## Formal Expression

*[Postulate (postulate-composition-consistency)]*

For any system $S$ satisfying the scope condition ( #scope-agency), and any decomposition of $S$ into subsystems $\{S_1, \ldots, S_n\}$ where each $S_i$ also satisfies the scope condition, AAD's predictions at the system level must be compatible with its predictions at the subsystem level. Specifically, composition laws must exist such that:

1. **Tempo composition**: $\mathcal T_S$ is expressible as a function of $\{\mathcal T_{S_i}\}$ and the coordination structure among them
2. **Persistence compatibility**: the system's persistence is derivable from the sub-agents' individual persistence conditions plus coordination structure
3. **Mismatch consistency**: $\delta_S$ is derivable from $\{\delta_{S_i}\}$ and their interaction structure

*[Structural consequence (derivation hierarchy)]*

Cross-level compatibility requires three successively more specific conditions, each with its own segment in Section III:

1. **Scope**: The decomposition is a *composite* (not merely a multi-agent system) when #scope-composite-agent is satisfied — teleological alignment via at least one of three disjunctive routes (shared objective, hierarchical derivation, or mutual benefit). Without scope-satisfaction via any route, level-compatibility is vacuous (composition quantities are not well-defined, so there is nothing to be consistent about).

2. **Admissibility**: Given a composite, its macro-dynamics are well-posed when the closure admissibility conditions (A1)-(A4) hold ( #form-composition-closure). These require AAD-shaped macro-state, macro-mismatch, macro-tempo, and sector-bounded correction at the composite level.

3. **Transfer of results**: Individual Section I/II results lift to the composite level through the bridge lemma in #form-composition-closure, which requires a *tier-specific contraction assumption* beyond (A4). For **Tier 1** agents (all Bayesian updaters on exponential families, linear correctors with positive-definite gain, gradient descent on strongly convex losses), the contraction holds and Section I results transfer exactly. For **Tier 2** agents (locally convex, nonlinear prediction models), transfer holds locally with factor degradation. For **Tier 3** agents (non-convex optimization, discontinuous corrections, non-mismatch-driven state), contraction must be verified per-domain and Section I results do not automatically lift.

*[Derived (Conditional on Tier 1M + admissible composition topology, from #result-contraction-template (CC-parallel) / (CC-cascade) / (CC-feedback))]*

**Composite contraction rate — closed form under Tier 1M.** When sub-agents satisfy the contraction-template preconditions (CT1)–(CT3) of #result-contraction-template (Tier 1M, equivalently Tier 1 of #form-composition-closure's bridge lemma under the DA2'-inc ≡ (CT2)-at-$M=I$ equivalence) and the composition topology falls under one of the closure cases of #result-contraction-template, the composite contraction rate $\lambda_c$ admits a closed-form lower bound:

- **Parallel composition** (CC-parallel): $\lambda_c = \min_i \lambda_i$ — the composite contraction rate equals the slowest sub-agent's, with composite metric $M_c = \mathrm{blockdiag}(M_1, M_2)$. Equivalently in timescale form, the composite relaxation time $\tau_c = 1/\lambda_c = \max_i \tau_i$ is bounded *below* by the slowest sub-agent's timescale.
- **Hierarchical / cascade** (CC-cascade): same bound, up to coupling-gain adjustment.
- **Negative-feedback heterogeneous** (CC-feedback) / (CM2-M): $(\lambda_1 - C_1)(\lambda_2 - C_2) \gt k_{12} k_{21}/4$ with feedback-loop gains $k_{ij}$ and coordination costs $C_i$ from #der-team-persistence.

Macro-level persistence then reduces to the standard persistence condition ( #result-persistence-condition) applied to the composite: $\alpha_c \gt \rho_{\text{eff}}/R_c$, with $\alpha_c$ bounded by the topology-specific result above and effective disturbance $\rho_{\text{eff}} = \rho_{\text{ext}} + \varepsilon^\ast \nu_c$ from #der-tempo-composition's bridge-lemma instantiation. Both Section I results (single-agent persistence) and the bridge-lemma's macro-tracking faithfulness flow from this single inequality. This is the formal counterpart to the screening test below: under Tier 1M the screening test is *derived*, not heuristic.

*[Heuristic (timescale separation — residual scope: Tier 2 / Tier 3)]*

**Practical screening test for composites outside Tier 1M.** Tier 2 sub-agents (extended-Kalman, locally-convex gradients, nonlinear prediction models) and Tier 3 sub-agents (non-convex optimization, discontinuous corrections, non-mismatch-driven state) do not in general carry the closed-form composite-rate bound above — the bridge-lemma contraction holds only locally with $\kappa(D\hat o)^2$ degradation (Tier 2) or must be verified per-domain (Tier 3). For these composites, the qualitative condition

$$\tau_{\text{eq}} \ll \tau_{\text{ext}}$$

— internal equilibration timescale (the time for sub-agents to approximately synchronize models and coordinate actions) short relative to external-dynamics timescale — remains a useful *discussion-grade screening test*. When it holds, composite description is plausibly well-posed; when it fails, composite description is plausibly broken. The screening test is the operational analog of the persistence condition ( #result-persistence-condition), but for Tier 2 / Tier 3 it does not entail the formal persistence condition without local-region or per-domain verification. Whether common organizational settings (software teams, military units) genuinely sit in Tier 1M or merely satisfy the heuristic without satisfying Tier 1M conditions is an empirical question, not a derived fact.

## Epistemic Status

*Axiomatic* for the meta-requirement (cross-level compatibility). The postulate itself is a structural requirement for AAD's internal consistency: if the scope condition doesn't restrict which level the theory applies to, the predictions must not contradict across levels.

The operational consequences decompose into three layers with distinct epistemic statuses:

- **Scope selection** ( #scope-composite-agent, robust-qualitative): which decompositions constitute composites. The scope condition is a disjunction of three qualitatively distinct routes (shared objective, hierarchical derivation, mutual benefit); whether they reduce to a common scalar threshold is open. Coverage of well-understood cases holds via the disjunction.

- **Admissibility of composite dynamics** ( #form-composition-closure, conditional): the (A1)-(A4) conditions are stated formally; the bridge lemma is conditional on the incremental sector bound (DA2'-inc), strictly stronger than (A4) alone.

- **Transfer of individual-agent results** (tier-dependent): Tier 1 composites transfer Section I/II results exactly; Tier 2 transfer with degraded factors; Tier 3 require per-domain verification. This is the sharpest scoping of "every result applies at every level" — it applies at every level *for Tier 1 composites*, degrades gracefully for Tier 2, and holds per-domain for Tier 3.

The composite contraction rate has two epistemic layers. **Tier 1M is derived (exact)**: under (CT1)–(CT3) on each sub-agent and an admissible composition topology, $\lambda_c$ admits the closed-form lower bound from #result-contraction-template's (CC-parallel) / (CC-cascade) / (CC-feedback) — the slowest-sub-agent / coupling-adjusted / heterogeneous (CM2-M) cases respectively. The screening condition $\tau_{\text{eq}} \ll \tau_{\text{ext}}$ is, in this regime, the formal persistence condition $\alpha_c \gt \rho_{\text{eff}}/R_c$ specialized to internal-vs-external rate balance — not heuristic. **Tier 2 and Tier 3 retain heuristic / discussion-grade status**: the closed-form composite rate does not transfer (Tier 2 with local degradation; Tier 3 per-domain), and $\tau_{\text{eq}} \ll \tau_{\text{ext}}$ remains a useful screening test without entailing macro-level persistence. The "small gap between screening and Tier 1M conditions in common settings" is an empirical claim about the population of real composites, not a derived fact.

## Discussion

**The same pattern as individual persistence.** The persistence condition says: there is a measurable threshold below which an individual agent's mismatch grows without bound and the agent degrades. Composition consistency says the same thing at the composite level: there is a measurable threshold below which the composite description breaks down. Under Tier 1M, the threshold is exact and closed-form — $\alpha_c \gt \rho_{\text{eff}}/R_c$ with $\alpha_c$ from (CC-parallel) / (CC-cascade) / (CC-feedback). Under Tier 2 / Tier 3, the threshold is only qualitatively captured by the screening ratio $\tau_{\text{eq}} / \tau_{\text{ext}}$ and exact transfer requires local-region or per-domain verification. The two-tier structure is the precise way "the theory applies broadly" — broadly under Tier 1M, qualitatively-with-conditions outside it.

**What this buys the theory.** With composition consistency stated early:
- Section I/II results lift to the composite level *for Tier 1 composites passing the composition scope condition*, with degraded-factor lift for Tier 2 and per-domain verification for Tier 3 — the three-layer decomposition above makes this precise rather than leaving "applies at every level" as an unbounded claim
- Section III becomes the study of *what happens near and beyond the threshold* — coordination overhead, unity dimensions, symbiogenic transitions, adversarial dynamics — rather than a separate multi-agent theory
- The formal test for composition validity ( #form-composition-closure) develops the rigorous version of the timescale condition, with the incremental sector bound identifying which agent classes admit the contraction needed for cross-level transfer; #result-contraction-template lifts that bound into a metric-aware framework where (CC-parallel) / (CC-cascade) / (CC-feedback) yield the topology-indexed closed forms cited above

**When composition fails.** The persistence condition $\alpha_c \gt \rho_{\text{eff}}/R_c$ (Tier 1M) — or its qualitative shadow $\tau_{\text{eq}} \ll \tau_{\text{ext}}$ (Tier 2 / Tier 3) — fails when:
- Internal coordination slows: $C_{\text{coord}}$ from #der-tempo-composition rises through coupling overhead, conflict, or bureaucratic process, depressing $\alpha_c$ below the threshold; equivalently, $\tau_{\text{eq}}$ stretches.
- External dynamics accelerate: $\rho_{\text{ext}}$ rises (adversary acts faster, market shifts, crisis compresses decision timescales); equivalently, $\tau_{\text{ext}}$ shortens.
- Both simultaneously (the classic organizational failure mode — internal friction increases while external demands intensify).

This is the formal analog of Brooks's Law: adding people to a late project increases $\varepsilon^\ast \nu_c$ in $\rho_{\text{eff}}$ ( #der-tempo-composition's coordination-overhead bound) and stretches $\tau_{\text{eq}}$ while $\rho_{\text{ext}}$ and $\tau_{\text{ext}}$ stay fixed (the deadline doesn't move). Under Tier 1M the mechanism is formal — eventually the persistence inequality flips. Under Tier 2 / Tier 3 the mechanism is qualitative. Whether the specific mechanism (coordination-overhead saturation crossing the persistence threshold) is the dominant cause of Brooks's Law in practice is an empirical question.

**The boundary is a modeling choice.** A development team is simultaneously: individual developers (each an AAD agent), the team (a composite AAD agent), and part of an organization (a sub-agent within a larger composite). The scope condition is satisfied at every level. Composition consistency ensures the theory doesn't give contradictory answers about observable quantities (e.g., whether the team persists) regardless of which boundary is chosen.

**What composition consistency does NOT say.** It does not specify the form of the composition laws — those are derived in Section III ( #der-tempo-composition). It does not say every decomposition is equally useful for analysis. And it does not require perfect internal coordination — only that internal equilibration is fast relative to external dynamics.

## Working Notes
- **Strengthening attempt — outcome.** The "macro-timescale bounded below by slowest sub-agent" claim was attacked via #result-contraction-template's compositional theorems before falling back to heuristic-only framing. Under Tier 1M (sub-agents satisfying (CT1)–(CT3) with metrics $M_i$, rates $\lambda_i$): (CC-parallel) yields $\lambda_c = \min_i \lambda_i$ exactly under blockdiag composite metric — the formal version of "composite is no faster than the slowest sub-agent"; (CC-cascade) yields the same bound up to coupling-gain adjustment; (CC-feedback) / (CM2-M) yields the heterogeneous closed-form inequality. No new math required — the strengthening is achieved by binding the postulate's heuristic to the existing (CC-*) closed forms via the DA2'-inc ≡ (CT2)-at-$M=I$ equivalence in #form-composition-closure. Tier 2 (local with $\kappa(D\hat o)^2$ degradation) and Tier 3 (per-domain) retain heuristic / discussion-grade screening; this residual is what the strengthening attempt could not eliminate.
- The timescale separation condition is essentially the singular perturbation argument from #der-temporal-nesting applied to composition: the fast internal dynamics approximately equilibrate, and the composite's behavior is described by the slow (external) dynamics on the equilibrium manifold. The formal connection should be made explicit when temporal-nesting is reviewed.
- Composition of directed separation: if each sub-agent's $f_M$ is $G_t$-independent, does the composite's $f_M^c$ remain $G_t^c$-independent? Hypothesis: goal-blindness composes, BUT coordination routing may break it — if which observations reach the composite depends on the shared objective, the composite's effective observation function is goal-dependent. This is the organizational analog of the LLM scope restriction in #der-directed-separation.
- The "atomic agent" question: if every agent is decomposable, where does it bottom out? At agents whose internal dynamics are not usefully described by AAD — below the level where observations, actions, and uncertainty exist, the scope condition fails and the recursion terminates.
- The relationship to holons (Koestler 1967): an AAD agent satisfying composition consistency is a holon — simultaneously a whole (analyzable as a single agent) and a part (decomposable into sub-agents). The term is occasionally useful but carries significant mystical baggage from later appropriations. Use sparingly.
