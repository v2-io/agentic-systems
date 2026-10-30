---
kind: item
provenance: imported
source: PROPOSALS.md:278
section: PROPOSALS — Architectural Portfolio › §G. Newly surfaced in 2026-04-24 consolidation audit
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
concerns: [segment:form-composition-closure, segment:deriv-strategic-composition, segment:result-unity-closure-mapping, segment:der-team-persistence, segment:deriv-critical-mass-composition, segment:disc-composition-consistency, segment:hyp-symbiogenic-composition, segment:scope-composite-agent, segment:def-unity-dimensions]
rechecked: 2026-10-30T21:30:36Z by Claude Opus 5.5 (item rechecker, q-proposals lane)
owner: unassigned
restated: 'Resolve #scope-composite-agent''s internal contradiction (its justification at :83 requires a well-defined O_c; routes C-iii and C-iv admit composites without one) either by deriving an induced O_c for each route or by splitting the routes into distinct composite ontologies with their own theorem families; eight dependent segments rest on the choice.'
---

# SP-21 — Composite-agent scope-route ontology split

Imported verbatim (relative links rebased) from `PROPOSALS.md` line 278, section *PROPOSALS — Architectural Portfolio › §G. Newly surfaced in 2026-04-24 consolidation audit*. Not yet re-checked against HEAD: `vsect recheck item:proposals-sp-21-composite-agent-scope-route-ontolo-4969 --outcome holds|stale|landed|not-an-item --why …`.


**Source:** 2026-04-24 fresh-pass audit (B7 in `audits/audit-2026-04-24-fresh-pass.md`; extracted into `audits/pending-findings-2026-04-25.md`).

**Decision needed from Joseph before scoping execution.** This proposal would *reverse* a deliberate architectural choice made 2026-04-22/23 — see "What this proposal reverses" below. Routing it correctly is more important than executing it quickly.

**Thesis.** Treat the four composite-agent scope routes (C-i shared-objective / C-ii hierarchical-decomposition / C-iii mutual-benefit / C-iv equilibrium-convergent) as **distinct composite ontologies**, each with its own macro-object structure and theorem family, rather than as four disjuncts of a single unified scope condition.

**Argument.** Each route presupposes a different macro-object:
- **C-i / C-ii (alignment composites):** macro-object is shared-objective composite with $X_c = (M_c, G_c)$ and a coherent $O_c$. `#form-composition-closure`'s machinery applies cleanly.
- **C-iii (mutual-benefit composites):** macro-object is *not* an explicit-objective composite — it's a coalition or stable cooperation regime around a relevance variable $Y$. The macro-state machinery is unspecified (this is the F-V3 / F8 inconsistency: line 79 of `scope-composite-agent.md` admits that without $O_c$ the composite is "a fiction").
- **C-iv (strategic composites):** macro-object is *not* a state-tracking object — it's an equilibrium statistic over joint policy. `#deriv-strategic-composition` rightly reaches for game-theoretic primitives instead of Lyapunov-on-shared-state. Composition-closure's macro-state requirement still applies textually.

The current single-disjunction form papers over the fact that C-iv composites require equilibrium-theoretic primitives, C-iii composites require coalition-theoretic primitives, and only C-i / C-ii fit the original AAT-shaped macro-state. Splitting would let each composite type carry its own theorem family (Lyapunov-on-shared-state for C-i/C-ii; relevance-variable-induced or coalition machinery for C-iii; equilibrium-theoretic for C-iv) without having to make every Section III result route-conditional.

**Findings subsumed (if executed).** F-V2 (cross-segment contradiction in `scope-multi-agent` adversarial-pair exclusion); F-V3 / F8 (C-iii vs $G_c = (O_c, \Sigma_c)$ requirement). Both have narrow editorial fixes available without SP-21; the editorial fixes are recommended as Path A interim moves regardless of whether SP-21 is executed.

**What this proposal reverses (CRITICAL CONTEXT).** The unified disjunctive form is recent (2026-04-22/23) and was an *explicit* architectural choice with stated reasoning, not a default that drifted in:

- **The unification logic** (`scope-composite-agent.md` Discussion §"Why this is a scope condition, not merely a quality metric"): "Making this a scope condition resolves the category issue: composition applies where $G_c$ is well-defined." All four routes answer the same question — "Is there a well-defined composite-level structure that makes the group a meaningful agent rather than a projection artifact?" — so they unify under a single scope gate. The four routes give qualitatively distinct answers to "what does it mean for $G_c$ to be well-defined?"
- **The C-iv inclusion choice** (`spikes/spike-strategic-composition.md` lines 99–108): "Whether this distinction is worth surfacing as a formal scope addition, or whether strategic composites are better handled as a separate Section III segment parallel to `#form-composition-closure`, is one of this spike's landing decisions. **Preferred reading: treat as a different type within the same scope condition, via (C-iv).** Reason: the composite is still a coherent object with a joint persistence story; calling it 'not a composite' overclaims the alignment requirement." This is the explicit decision SP-21 would reverse.
- **The "no-reduction-to-scalar" honesty.** The disjunction form was chosen because no single scalar (like $U_O$) reduces all four to a unified threshold; the disjunction "captures at least one of these qualitatively distinct mechanisms applies" without forcing premature reduction. Splitting would replace this with four parallel scope conditions, each with its own operationalization.

If SP-21 lands, the framework loses the "one scope gate, multiple qualitative routes" framing that the 2026-04-23 cycle deliberately chose. Whether that loss is worth the cleaner per-route theorem families is the architectural decision Joseph needs to weigh.

**Downstream rework (from prior-art audit, 2026-04-25).** Eight segments depend on the unified disjunctive form:
1. `#form-composition-closure` — admissibility (A1)–(A4) and bridge lemma assume scope-satisfaction via *any* route; would need per-route admissibility variants or explicit condition-dependence.
2. `#result-unity-closure-mapping` — rate-distortion curves "conditional on at least one of three disjunctive routes"; would need parallel instantiations.
3. `#der-team-persistence` — derived assuming "one of (C-i)–(C-iii)"; C-iv excluded; would need explicit route-conditioning.
4. `#deriv-critical-mass-composition` — (CM4) makes scope-satisfaction a conjunct in composite persistence; would need route enumeration.
5. `#deriv-strategic-composition` — explicitly references "(C-iv)" as a route within the disjunction; would need rewrite to "strategic-composition scope condition" parallel.
6. `#disc-composition-consistency` — foundational postulate uses unified gate; would fracture into "which groups satisfy C-i? C-ii? C-iii? C-iv?"
7. `#hyp-symbiogenic-composition` — explicitly states symbiogenesis "crosses the #scope-composite-agent from below" via route (C-ii); would become route-specific.
8. `#def-unity-dimensions` — scope note presumes disjunction; would need per-route operationalization story.

This is non-trivial cross-segment rework — call it 4–6 sessions if pursued as a coordinated split, vs ~45–60 min for the F-V3 narrow editorial fix (Path A) which preserves the unified form.

**Interactions with other proposals.**
- **SP-6 (composition-closure consolidation)** in Bundle 2 is adjacent — SP-6 is about scope-narrowing within `#form-composition-closure`'s claims; SP-21 is about restructuring the *upstream* scope condition. SP-21 would change what SP-6 needs to consolidate. If both pursued, SP-21 first.
- **O-BP9 (typed admissibility for composition)** in Bundle 2 — explicitly proposes route-typed admissibility (model-only / goal-bearing / strategy-bearing). SP-21 is adjacent: O-BP9 splits *admissibility-by-quantity-bearing-type*; SP-21 splits *scope-by-route-ontology*. They could compose (each route gets its own admissibility-typing; or admissibility-typing replaces route-splitting). Worth resolving relationship before scoping either.
- **Bundle 2 (Section III completion)** — SP-21 would restructure how Bundle 2's pieces interlock. Bundle 2's current sequencing (SP-11 → SP-6-residue → O-BP9 → O-BP16 + SP-17) presumes the unified scope condition; SP-21 inserted at the front would change that sequence.

**Effort.** Substantial. 4–6 sessions for the segment restructure across 8 dependents. Plus a scoping spike to resolve the SP-21 vs O-BP9 relationship.

**Risks.**
1. *Loss of the unification reasoning.* The current form's "single scope gate, four qualitative routes" is structurally informative — it asserts that "well-defined composite-level structure" is one question with multiple acceptable answers. Splitting fragments this assertion.
2. *F-V3 editorial fix may suffice.* If C-iii's induced-$O_c$ structure is made explicit (Path A in F-V3 landing), the most pressing inconsistency dissolves without architectural restructure. Whether the C-iv strategic-composite case still motivates SP-21 after Path A is open.
3. *Post-Bundle-2 reassessment.* Section III is in active flux; a structural decision now risks being made on a still-evolving substrate. Better to land Bundle 2's existing pieces first and re-evaluate SP-21 against the matured Section III structure.

**Status: Open architectural decision.**

**Recommendation:** Defer SP-21 execution. Land F-V2 and F-V3 editorial fixes (Path A: cross-segment edit + C-iii induced-$O_c$ via relevance variable $Y$) which clear the immediate contradictions without architectural restructure. Re-evaluate SP-21 after Bundle 2 (Section III completion) lands, when the route-specific theorem families are visible enough to judge whether the unification framing is helpful or limiting. If at re-evaluation the answer is still "split," the work is more legible than now and the rework cost is concentrated on a more stable substrate.

**Value if eventually executed:** +3 to +5 framework / +4 paper. Cleaner per-route theorem families; explicit route-typed macro-objects. Loss of the "one well-defined-ness question, four routes" framing is real but possibly worth it once Section III matures.

**Independence.** **Low.** Touches the foundational scope segment plus eight downstream load-bearing segments; cannot parallelize with most Section III work; conflicts with Bundle 2's current sequencing.
