# Modularity-as-Contested-Property Cycle: Integration Plan

**Status**: drafted 2026-05-09; pending Joseph's decision to execute.
**Origin**: emerged at the end of the class-coercion-wrapping integration cycle (`spikes/class-coercion-wrapping/INTEGRATION-PLAN.md`) when uncommitted parallel work — `01-aat-core/src/disc-adversarial-coupling-pressure.md` (drafted via different Opus instance during the same session) and `spikes/spike-strategic-self-coupling.md` (sister spike) — was inspected and found to converge structurally with the class-coercion construction.
**Posture**: clean theory and unification, integration content. The work is naming a meta-pattern that has emerged across multiple parallel collaborator probes; AAD's contribution is the recognition and integration, not novel content beyond what each segment carries.

---

## 1. The convergence finding (motivation)

Three pieces of work landed in the repo on 2026-05-09 from independent collaborator probes:

1. **`#der-class-coercion-via-wrapping`** (`01-aat-core/src/`, this Opus instance, integrated). Constructive route from Class-2/3 components to Class-1 composites via external scaffold; W₀/W₂/W₁ regime hierarchy; structural-vs-behavioral leakage bounds.

2. **`#disc-adversarial-coupling-pressure`** (`01-aat-core/src/`, parallel Opus instance, **drafted but unregistered in OUTLINE — orphan**). Adversarial pressure as the externally-driven force that drives target coupling; identity-binding / affect / sunk-cost mechanisms; directional diagnostic corruption; orient-cascade inversion; defensive scaffolding (peer review, prediction registers, etc.) as the composite-agent restoration move.

3. **`spikes/spike-strategic-self-coupling.md`** (parallel Opus instance, scope-defined). Sister spike for the *enabling* polarity of coupling — Schelling commitment devices, Ainslie willpower, Akerlof-Kranton identity economics, Frank emotions-as-commitment. The fixed-$\mathcal A$ assumption surfaced; structural extensions M1 ($\mathcal A(\kappa_t)$), M2 (enabling strategy edges), M3 (reversibility cost) named.

These three pieces were generated independently and converged on a **three-operation modularity-state-dynamics picture**:

| Operation | Driver | Effect on modularity | Primary segment / status |
|---|---|---|---|
| **Truthification** | self-driven | increases | (A) `#disc-adversarial-coupling-pressure` §"Defensive scaffolding as composition" — informal; (B) `#der-class-coercion-via-wrapping` — formal mechanism (wrapper-around-component). |
| **Strategic self-coupling** | self-driven | decreases (action-enabling) | spike-defined (`spike-strategic-self-coupling.md`); segment pending. |
| **Adversarial coupling pressure** | externally-driven | decreases (vulnerability) | `#disc-adversarial-coupling-pressure` (drafted, unregistered). |

The class-coercion construction is structurally a *truthification mechanism* — specifically, the rigorous formal version of what defensive scaffolding has been gesturing at. External scaffolding (peer review, prediction registers, double-entry bookkeeping, adversarial procedure, structured red-teaming) and internal wrapping (`#der-class-coercion-via-wrapping`) are two operational mechanisms of the same operation. The W₀/W₂/W₁ hierarchy is the *graded* characterization of how thoroughly the truthification has been applied.

## 2. The structural opportunity

A meta-segment naming the three-operation pattern would land cleanly alongside the existing M-section meta-patterns of `msc/FINDINGS-RANKED-DRAFT.md`:
- M1: identifiability-floor (`#disc-identifiability-floor`)
- M2: separability ladder (`#disc-separability-pattern`)
- M3: additive-coordinate-forcing (`#disc-additive-coordinate-forcing`)
- **M4 (proposed): modularity-state dynamics** — the three-operation pattern.

The pattern's shape:

> Modularity is a contested, cultivated, and constructed property — not a fixed architectural fact. Three operations act on the modularity state of an agent or composite: truthification (self-driven, increasing), strategic self-coupling (self-driven, decreasing, action-enabling), and adversarial coupling pressure (externally-driven, decreasing, vulnerability-creating). Defensive scaffolding (peer review, prediction registers, etc.) and the wrapping construction are two operational mechanisms of truthification. Each operation has dual relationships to the others (defensive scaffolding restores what adversarial pressure attacks; strategic self-coupling deliberately gives up what truthification cultivates). Static architectural classification (Class 1/2/3 from `#der-directed-separation`) is the *state space*; the modularity-state dynamics are the *operations* on it.

This is the recognition that ties together class coercion, defensive scaffolding, adversarial coupling pressure, and strategic self-coupling. It is also the moment when the recognition is most legible — all three operation legs have segment grounds within reach.

## 3. Cycle moves

Five concrete moves form the cycle. They are interdependent — each makes the others land more cleanly. The whole cycle should be one commit cluster, not five separate commits, because the cross-references and meta-segment legibility require all of them.

### Move 1: Register `#disc-adversarial-coupling-pressure` in OUTLINE

The segment is currently orphaned (lint-outline flags it as the only orphan in the project). It belongs in `01-aat-core/OUTLINE.md`. Two candidate placements:

(a) Under Section II as a discussion-grade adjunct to `#der-directed-separation` (it sits at the architecture-classification layer).
(b) **Recommended:** as a meta-segment alongside `#disc-separability-pattern` and `#disc-identifiability-floor` (it's a meta-pattern that cuts across Section II and Section III rather than a Section II result proper).

The segment's working notes flag this same routing question. (b) is the cleaner placement because the modularity-state-dynamics meta-segment (Move 4) will sit there, and adversarial-coupling-pressure is naturally one of its instantiations.

### Move 2: Discussion update to `#der-class-coercion-via-wrapping`

Add a paragraph in the Discussion section recognizing the wrapping construction as a *truthification mechanism* — the rigorous formal version of what defensive scaffolding (`#disc-adversarial-coupling-pressure` §"Defensive scaffolding as composition") has been gesturing at. Cross-reference both the adversarial-pressure segment and the (eventual) modularity-state-dynamics meta-segment.

The W₀/W₂/W₁ regime hierarchy should be cross-referenced as the graded characterization of truthification application.

### Move 3: Land `#disc-strategic-self-coupling` (the (P1) candidate from the spike)

Per `spikes/spike-strategic-self-coupling.md` §5, the (P1) primary segment is structurally parallel to `#disc-adversarial-coupling-pressure` — discussion-grade, mechanism table at top, sections on enabling polarity, strategic value, reversibility cost, asymmetric advantage, defensive-scaffolding analog as the truthification operation. Prior-art adoption per the discipline: Schelling 1960 *Strategy of Conflict* (commitment devices), Ainslie 1992/2001 (intertemporal bargaining / willpower), Akerlof-Kranton 2000/2010 (identity economics), Frank 1988 *Passions Within Reason* (emotions as commitment).

Open question to resolve in segment-drafting: the spike notes that $\mathcal A(\kappa_t)$ is plausibly *non-monotone* — initial coupling enables credibility-dependent actions; sustained over-coupling forecloses reality-dependent actions. The segment should probably state this honestly as an open question rather than committing to monotonicity prematurely.

### Move 4: Land `#disc-modularity-state-dynamics` as the meta-segment

Structure roughly parallel to `#disc-separability-pattern` and `#disc-identifiability-floor`:
- Setup: modularity as state, not architecture
- The three-operation table (with each operation's primary-segment pointer)
- Dual relationships (defense ↔ attack; cultivation ↔ surrender)
- Operational mechanisms across operations (defensive scaffolding *and* class-coercion-via-wrapping under truthification; identity-binding *and* affect *and* sunk-cost engineering under adversarial pressure; commitment-device *and* willpower *and* identity coupling under strategic self-coupling)
- Position in the M-section family alongside M1/M2/M3
- Honest scope: this is *recognition-and-integration* content, not novel derivation. The three-operation pattern is observable across propaganda research, behavioral economics, and the segments named above; AAD's contribution is naming its place in the framework's analytical surface.

Findings section worth landing if the segment promotes — the cross-segment finding ("modularity-as-contested-property is the structural axis across these segments") may be more citable than the per-segment findings.

### Move 5: Surface bounded-signaling assumption in `#der-directed-separation`

The `#disc-adversarial-coupling-pressure` working notes flag this as a back-pressure follow-on. Brief Discussion-section paragraph in `#der-directed-separation` naming the assumption: $G_t \to$ world only via $a_t = \pi(M_t, G_t)$ — that is, the channel from goal-state to the world runs only through action choice. The assumption fails operationally when behavioral leakage is rich relative to action coarseness (sophisticated $G_t$-inference from prosody, micro-behavior, attention patterns). Cross-reference `#disc-adversarial-coupling-pressure` for the adversarial-saturation case where this leakage is exploited.

## 4. Order of execution

1. **Read context first** (as Phase A of the previous cycle): re-read `#disc-adversarial-coupling-pressure.md` carefully; re-read the strategic-self-coupling spike; refresh `#disc-separability-pattern` and `#disc-identifiability-floor` to see how the existing M-section meta-segments are structured. ~30 min.

2. **Move 5 first** (smallest, opens the analytical surface). Brief Discussion paragraph in `#der-directed-separation`. ~15 min.

3. **Move 1** (register adversarial-pressure in OUTLINE). ~5 min.

4. **Move 2** (Discussion update to class-coercion segment). ~15 min.

5. **Move 3** (write the strategic-self-coupling segment from the spike). The spike is well-scoped; the writing is straightforward but the segment needs to be substantive. ~2-3 hours including prior-art review (Schelling, Ainslie, Akerlof-Kranton, Frank).

6. **Move 4** (write the meta-segment). This is the centerpiece move; it should be done last because it integrates Moves 1–3. ~2-3 hours.

7. **Verification**: lint-md, lint-outline, cross-reference resolution, OUTLINE consistency. ~15 min.

8. **CHANGELOG entry** for the cycle, naming the modularity-state-dynamics M-section addition and the convergence-from-parallel-collaborators framing as a discipline-reinforcement observation.

Estimated total: 1 day's focused work, possibly stretched across a day-and-a-half if the strategic-self-coupling segment requires substantive prior-art reading.

## 5. Decision points for Joseph

1. **Does the modularity-state-dynamics framing actually land for you as M4?** The three M-section meta-patterns are load-bearing for AAD's structural identity. Adding a fourth is structurally weighty. The pattern is real and the timing is good (all three operation legs within reach), but you may want to sit with it before committing.

2. **Where to register `#disc-adversarial-coupling-pressure` in OUTLINE.md?** (a) Section II adjunct to `#der-directed-separation` or (b) meta-segment alongside `#disc-separability-pattern` / `#disc-identifiability-floor`. Recommendation: (b), but it's your call.

3. **How much prior-art work in the strategic-self-coupling segment?** Schelling/Ainslie/Akerlof-Kranton/Frank are all canonical and worth citing. The question is whether to do real reading-and-distillation work for each (spike-grade), or to cite them with brief one-line characterizations (segment-grade with named follow-on for deeper integration). Recommendation: segment-grade now, deeper integration later if the segment becomes load-bearing for downstream work.

4. **Whether to bundle the naming refactor (Class 1/2/3 → Separated/Coupled/Partial swap) into this cycle.** PRACTICA flags the swap as the only remaining §B item; the new segments would benefit from getting the new vocabulary directly rather than retrofitting later. But the swap is its own substantive cycle (~7 segments + README + CLAUDE.md). Recommendation: probably *not* in the same cycle — the modularity work has its own coherence; the swap cleanup can happen separately and touch the new segments alongside the others.

5. **Whether to also address the multi-timescale stability promotion** (Move B from RG verdict). It's the highest-leverage standalone piece I named in the prior recommendation. It's *adjacent* to this cycle (modularity / persistence / template-stacking all relate) but doesn't directly require it. Recommendation: hold for the next cycle so this one stays focused.

## 6. What this cycle does *not* address (next-cycle items)

- **Multi-timescale stability promotion** — `#sketch-multi-timescale-stability` from sketch to derived via template-stacking + Tikhonov + Chen-Goldenfeld-Oono. Highest-leverage standalone piece for Section III.
- **Parts III/IV scope segment landings** — `scope-channel-collapse`, `scope-primitive-logogenic`, `scope-scaffolded-logogenic`, `scope-interiority-loop` are all flagged as missing or draft in `03-llm-core/OUTLINE.md`. Without them, the lattice has gaps.
- **Class-3 closure-defect dynamics analysis** — Move F from RG verdict; the order-parameter dynamics-side analysis to complement the structural W₀/W₂/W₁ taxonomy. Worth a separate spike when Parts III/IV maturation has progressed.
- **shoshin → W₁ engineering** — operational realization of strict wrapping for PROPRIUM via auxilia handling goal-blind queries. Engineering, not theory; queued for shoshin development.
- **Three Deaths formal grounding** — promote `#hyp-the-three-deaths` from hypothesis to derived (or honest scope) by grounding each death in AAD primitives. ELI-side priority.
- **Identity-through-substrate-transitions formal segment** — connecting `obs-substrate-independence`, `def-identity-sufficiency`, `def-five-constitutive-factors` to the persistence template across substrate changes. ELI-side priority.

## 7. Honest scope and posture

This cycle is *recognition-and-integration*, not novel derivation. The substantive content is in the four segments (existing class-coercion + adversarial-pressure + new strategic-self-coupling + new meta-segment); the cycle's contribution is naming the pattern explicitly and getting the cross-references aligned.

What makes it land cleanly *now* rather than later: the convergence finding from this conversation. Two Opus instances independently arriving at the modularity-state-dynamics pattern from different angles is structural evidence that the pattern is *in the framework* rather than in any one collaborator's head. Naming it explicitly while the recognition is fresh has higher leverage than waiting and recovering it later.

What it does not gain: any additional formal results. The three operations are characterized at discussion-grade; their formalization is downstream work. The meta-segment will be discussion-grade; promotion would require derivation of structural relationships between operations that are currently named informally.

The cycle's success criterion: future agents reading the framework cold can find `#disc-modularity-state-dynamics` and orient to the modularity-as-contested-property reading without having to reconstruct the convergence from scratch. That's the integration move.

---

## File index references

- `spikes/class-coercion-wrapping/00-brief.md` — spike track that landed `#der-class-coercion-via-wrapping`
- `spikes/class-coercion-wrapping/INTEGRATION-PLAN.md` — completed integration plan for that spike
- `spikes/class-coercion-wrapping/99-verdict.md` — verdict synthesis for that spike
- `spikes/spike-strategic-self-coupling.md` — sister spike defining (P1)–(P4) candidate segments
- `01-aat-core/src/disc-adversarial-coupling-pressure.md` — drafted, currently orphan in OUTLINE
- `01-aat-core/src/der-class-coercion-via-wrapping.md` — landed today
- `01-aat-core/src/der-directed-separation.md` — receives Move 5 update
- `01-aat-core/OUTLINE.md` — receives Moves 1 and 4 OUTLINE additions
- `msc/FINDINGS-RANKED-DRAFT.md` — receives M4 entry once Move 4 segment lands

This plan is self-contained for handoff: an agent picking it up cold should be able to execute it from this file, the spike directories, and the segment files referenced above.

---

## 8. Execution status (2026-05-14 partial-cycle landing)

A small follow-on cycle (2026-05-14) landed the three additive / low-architectural-commitment moves and deliberately deferred the two new-segment-authoring moves pending Joseph's §5.1 decision and the prior-art reading work required for Move 3.

### Landed in the 2026-05-14 cycle

- **Move 1** — already done 2026-05-09 per PRACTICA cycle priority item 2 marked [DONE]. `#disc-adversarial-coupling-pressure` registered in OUTLINE.md (placement (b) per the recommendation — meta-segment alongside `#disc-separability-pattern`/`#disc-identifiability-floor`).
- **Move 2** — *landed 2026-05-14.* Discussion subsection "Wrapping as a truthification mechanism" added to `#der-class-coercion-via-wrapping`, recognizing the wrapping construction as the rigorous formal version of what `#disc-adversarial-coupling-pressure` §"Defensive scaffolding as composition" gestures at informally. Cross-references the W₀/W₂/W₁ regime hierarchy as graded characterization of truthification application + the (queued) M4 meta-segment. Marked forward-reference per FORMAT.md.
- **Move 5** — *landed 2026-05-14.* Discussion paragraph "**Bounded-signaling assumption.**" added to `#der-directed-separation`. Names the assumption $G_t \to$ world only via $a_t = \pi(M_t, G_t)$, with operational-failure cases (behavioral leakage rich relative to action coarseness — prosody, micro-behavior, attention patterns, response latency). Cross-references `#disc-adversarial-coupling-pressure` for the adversarial-saturation case where this leakage is exploited.

### Deferred in the 2026-05-14 cycle: Moves 3 and 4

**Move 3 — `disc-strategic-self-coupling` segment authoring.** Deferred. Three substantive gates:

1. **Real prior-art reading work** required (per §5.3 recommendation): Schelling 1960 *Strategy of Conflict* (commitment devices), Ainslie 1992/2001 (intertemporal bargaining / willpower), Akerlof-Kranton 2000/2010 (identity economics), Frank 1988 *Passions Within Reason* (emotions as commitment). Even at segment-grade depth (one-line characterizations + citations), this is ~2-3 hours focused work, not 15-minute additive surgery.
2. **Non-monotonicity question.** The spike notes that $\mathcal{A}(\kappa_t)$ is plausibly non-monotone — initial coupling enables credibility-dependent actions; sustained over-coupling forecloses reality-dependent actions. Segment should state this honestly as an open question rather than committing to monotonicity prematurely. Working out the right framing requires substantive judgment, not a mechanical landing.
3. **Structural-parallelism with `#disc-adversarial-coupling-pressure`** requires reading that segment carefully and writing the sibling at matching grade, mechanism table, and rhetorical register. Spike §5 names (P1)–(P4) candidate products; (P1) is the primary segment, the others are appendix-grade companions.

**Move 4 — `disc-modularity-state-dynamics` meta-segment authoring.** Deferred. Three substantive gates:

1. **§5.1 decision-pending — Joseph's architectural commitment to M4.** The three M-section meta-patterns (M1 identifiability-floor / M2 separability-pattern / M3 additive-coordinate-forcing) are load-bearing for AAD's structural identity. Adding a fourth commits the framework to four meta-patterns as the canonical reading. The plan author flagged this deliberately as a sit-with-it-before-committing decision. The convergence finding (multiple Opus instances independently arriving at the modularity-state-dynamics pattern from different angles) is structural evidence that the pattern is *in the framework*, but committing to a fourth M-section label is a choice about AAD's analytical-surface vocabulary that wants Joseph's call.
2. **Move 4 depends on Move 3 landing first.** The meta-segment structurally needs to point at three primary segments — one per operation: truthification (instantiated in `#disc-adversarial-coupling-pressure` §"Defensive scaffolding" + `#der-class-coercion-via-wrapping` after Move 2), strategic self-coupling (Move 3 — not yet authored), adversarial coupling pressure (`#disc-adversarial-coupling-pressure`). Landing M4 standalone before Move 3 would create a meta-segment cross-referencing a sibling that doesn't exist.
3. **Recognition-and-integration posture** (per §7) — the meta-segment's value is *recognition* of the pattern explicitly. Recognition wants the three operation segments cleanly authored first, so the meta-segment integrates rather than over-asserts.

### Discipline observation surfaced en route

The 2026-05-14 cycle surfaced a **content-discipline issue** that the M4-related cross-references in `#impl-composition-machinery` (lines 67–69) and `#impl-strategic-composition` (line 82) read as if M4 is canonical — the segments describe what the M4 meta-segment "positions" and "names" without flagging that the segment file doesn't exist yet. CLAUDE.md's prior framing in §"Key Architectural Decisions" §7 listed `#disc-modularity-state-dynamics` alongside the other three M-sections "directly" without marking it queued. This is a case where the parallel-collaborator naming work was load-bearing enough that downstream cross-references treat the concept as canonical-by-reference, but the segment file itself never landed.

The 2026-05-14 cycle fixed CLAUDE.md to honestly reflect M4's pending status (matching OUTLINE.md's `missing` flag and PRACTICA's queued framing). The impl-segment forward-references remain valid per FORMAT.md — forward references are expected; the discipline that wants attention is that *content claims about a forward-referenced segment* (e.g., "the M4 meta-segment positions modularity as a contested property under three operations") read as if the segment is canonical. When Move 4 lands, those content claims become honest by-reference; until then, they are AAD's collective stance described by anticipation. Not a defect, but worth marking.

### What happens when the Moves 3 and 4 cycle lands

When Joseph green-lights the M4 architectural commitment and the prior-art reading work happens:

1. Authoring goes in plan-order: Move 3 first (substantive segment), then Move 4 (meta-segment that integrates Move 3 + the existing adversarial-coupling-pressure + the truthification mechanism that already lives across `#der-class-coercion-via-wrapping` and `#disc-adversarial-coupling-pressure` §"Defensive scaffolding").
2. The Move 2 + Move 5 landings from the 2026-05-14 cycle are *already-aligned* with what the meta-segment will reference — the truthification-mechanism subsection in `#der-class-coercion-via-wrapping` already cross-refs M4 as forward-reference, and the bounded-signaling assumption in `#der-directed-separation` is the structural assumption that the adversarial-pressure leg of M4 depends on.
3. Future CHANGELOG entry should note the partial-execution structure: the cycle splits naturally into a discipline-aware-additive sub-cycle (Moves 1, 2, 5; ~hour-scale) and a substantive-new-segments sub-cycle (Moves 3, 4; ~day-scale plus §5.1 decision gate).
