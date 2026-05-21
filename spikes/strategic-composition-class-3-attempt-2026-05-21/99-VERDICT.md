---
spike: strategic-composition-class-3-attempt
file: 99-VERDICT
parent: 00-FRAMING.md
prior: 01-STRENGTHEN-ATTEMPTS, 02-REFRAME-INSIGHT
status: synthesis complete; Joseph-reserved decisions itemized
---

# Verdict — what the math yields, what is Joseph-reserved, what to do next

## §V.1 What the spike yields (present truth)

**(F1) Refutation of unconditional "strategic composition → Class 3."** The Cournot witness (§2 of `01-STRENGTHEN-ATTEMPTS.md`) is a partially-opposing-objectives composite with goal-blind routing and distinct substrates whose composite $f^c_M$ is structurally goal-blind in $G^c_t$. By `#der-directed-separation`'s formal $\kappa^c$ criterion, the Cournot composite is Class 1 (Separated) at the composite level. The unconditional "strategic composition forces Class 3" claim is **refuted**. Conditional Class 3 derivations (R1 — goal-dependent routing; R4 — shared substrate with $G^c$-shaped allocation) exist but their antecedents are not implied by strategic composition.

**(F2) The current "Class 2" claim does not survive its own audit.** §6 of `01-STRENGTHEN-ATTEMPTS.md`: the claim conflates *belief content* (Class 1 sub-agents' $M^{(i)}_t$ encoding goal-information about other agents' goals — a normal POMDP feature) with *processing pathway* (a $G^c \to f^c_M$ pathway bypassing $e^c_\tau$ — the actual Class 1/3 boundary). The formal criterion gives Class 1 at the composite level under goal-blind routing, with no Class 2 stepping-stone. The current "Class 2 (Partial) composite from Class 1 (Separated) sub-agents under partially-opposing objectives" claim is **not licensed by the criterion**.

**(F3) Three senses of "Class 2" circulate currently** — within-agent mixed pathway (the architectural sense per `#der-directed-separation` formal definition); composite-level partial coupling via cross-agent belief content (the conflated sense per `#deriv-strategic-composition` and the Composite-level inheritance paragraph in `#der-directed-separation`); separability-pattern Architecture-row middle tier "directed separation holds for identified submodules" (per `#disc-separability-pattern`). Treating these as one label has produced confusion at the composite-class-inheritance layer; clean separation is owed.

**(F4) Internal contradiction in `#impl-strategic-composition`** (00-FRAMING §1): the segment asserts "Class 3 (Coupled) composite" three times in §"Strategic composition lifts contraction to equilibrium" and once in Working Notes line 83, while its load-bearing source `#deriv-strategic-composition` asserts "Class 2 (Partial) composite." The 2026-05-09 GUC rename swap and `#deriv-strategic-composition`'s migration note both make clear the canonical pre-rename phrase "Class-1-subs → Class-3-composite (partially modular)" is now "Class 1 → Class 2 (Partial) composite." `#impl-strategic-composition` appears to be **GUC-rename residue** — the segment carried the pre-rename label "Class 3" through the 2026-05-09 sweep without swapping, and the post-rename Class 3 is *Coupled*, not partially modular. The implications segment has been *inflating* the framework's actual position since 2026-05-09 by accident.

**(F5) Type-mismatch between architectural-class criterion and strategic-composite macro-state** (§7.1): for strategic composites, $G^c_t = \mathcal E$ is a fixed-point object, not a perturbable state-variable; the $\kappa^c$ measure is type-mismatched (numerator and denominator both vanish at rational-expectations equilibrium; off-equilibrium the residual flow is action-channel-mediated and licensed). The architectural-class machinery was designed for state-variable $G$; strategic composites need different machinery on a different axis.

**(F6) The genuinely missing axis** (§7.2): what strategic composition shifts is **dynamic regime** (contraction-regime → equilibrium-regime under $\alpha'$ → cyclic-distributional-regime under $\beta'$), not architectural class. The framework already has most of this implicit in `#deriv-strategic-composition`'s $\alpha'/\beta'$ partition, in `#scope-composite-agent` route C-iv's distinction, in `#impl-strategic-composition`'s "contraction-to-equilibrium hand-off" language, and in `#disc-separability-pattern`'s Contraction ladder. **Surfacing the axis explicitly is reorganization, not new derivation** — most of the math already exists in the cited segments.

**(F7) The modular-safety implication survives reframed, on stronger ground.** `#impl-strategic-composition` §"Modular safety architectures fail under goal divergence" claims modular safety fails because the composite becomes Class 3 (Coupled). Under (F1)+(F6), the failure mechanism is dynamic-regime change — modular safety guarantees designed for contraction-regime composites do not transfer to equilibrium-regime composites (saddle-points, multi-equilibria, last-iterate non-convergence). This is *the same conclusion* reached via the *correct mechanism*, on stronger ground because dynamic-regime change is exactly what `#deriv-strategic-composition` derives, while architectural-class change was a label-error.

## §V.2 Recommended canon changes (the integration-is-replacement landing)

These are the actions that follow from §V.1's present-truth findings. They are listed by force-of-recommendation, with the reasoning trail for each. None overrides Joseph-reserved decisions in §V.3.

**(C1) Fix the inter-segment contradiction in `#impl-strategic-composition` — mandatory regardless of the reframe.** The three "Class 3 (Coupled)" occurrences in §"Strategic composition lifts contraction to equilibrium" and the one "Class-3-composite" in Working Notes finding-`#23` reference are GUC-rename residue. Two options for the literal fix:

- *Conservative fix (matches current canon as it stands):* swap "Class 3 (Coupled)" → "Class 2 (Partial)" in all four places. This preserves the current framework position while resolving the contradiction.
- *Truthful fix (matches what the math actually licenses, this spike's present truth):* delete the architectural-class claim entirely, replace with dynamic-regime language ("equilibrium-regime composite," "the composite admits equilibrium dynamics not contraction dynamics"). This implements (F1)+(F2)+(F6) directly.

The conservative fix is the minimum action; the truthful fix is the integration-is-replacement action. **Whichever fix is chosen, the implications segment must add a 2026-05-09 GUC migration note** identical-in-form to the ones already in `#deriv-strategic-composition`, `#der-directed-separation`, `#hyp-directed-separation-under-composition`, and the other involved segments. That note's absence in `#impl-strategic-composition` is the proximate reason the residue persisted.

**(C2) Pull back the "Class 2 (Partial) composite" claim in `#deriv-strategic-composition` Discussion §"Class-2-(Partial)-composite-from-Class-1-(Separated)-sub-agents" and in the Findings-style table row.** Per (F2), the claim is not licensed by the formal criterion. Replacement language (sketch):

> *Strategic composition does not by itself change architectural class at the composite level. Under goal-blind routing and distinct sub-agent substrates, a composite of Class 1 sub-agents with partially-opposing objectives remains Class 1 (Separated) at the composite level per `#hyp-directed-separation-under-composition` Case 1 — the criterion measures pathway-coupling, not belief-content. What strategic composition does change is the dynamic regime: from contraction-regime (under aligned objectives, scope routes C-i/ii/iii) to equilibrium-regime (under partially-opposing objectives, route C-iv with sub-scope $\alpha'$) or cyclic-distributional-regime (route C-iv with sub-scope $\beta'$). See §`<dynamic-regime-treatment>`.*

**(C3) Mirror (C2) in `#der-directed-separation` Discussion §"Composite-level class inheritance".** The current Composite-level-inheritance paragraph carries the same "Class 2 (Partial) composite from Class 1 (Separated) sub-agents" claim as `#deriv-strategic-composition`. Same revision applies.

**(C4) Clean up the "three senses of Class 2"** (F3). Audit `#disc-separability-pattern` row 3 ("Class 2 (Partial) — directed separation holds for identified submodules") for whether it is using "Class 2" in the architectural sense or in a separability-pattern-structured-repair sense. If the latter, distinguish vocabulary (e.g., "Architecture ladder structured-repair tier: within-agent partial pathway"). The composite-level-Class-2 sense (the one §6 refutes) should be removed from `#deriv-strategic-composition`, `#der-directed-separation`, and any other segments that picked it up.

**(C5) Surface the dynamic-regime axis explicitly** (F6). Two options:

- *Light-touch:* add a `#disc-dynamic-regime` paragraph to `#disc-separability-pattern` listing dynamic regime as the eighth ladder (contraction-regime as separable core, equilibrium-regime under $\alpha'$ as structured repair, cyclic-distributional under $\beta'$ as general open) and cross-reference `#deriv-strategic-composition` for the $\alpha'/\beta'$ derivation.
- *Full meta-segment:* land `#disc-dynamic-regime` as a peer of `#disc-separability-pattern` / `#disc-identifiability-floor` / `#disc-additive-coordinate-forcing` / forthcoming `#disc-modularity-state-dynamics`. The meta-segment would carry the contraction / equilibrium / cyclic-distributional partition as the primary content and would be the canonical reference for what strategic composition shifts.

The standalone-paper potential of `#disc-separability-pattern` (per its Working Notes) suggests meta-segments are first-class in AAT; the full meta-segment option is the natural landing for Axis B if the framework adopts the reframe.

**(C6) Land the architectural-class composite-inheritance table from §7.3 (B5)** somewhere — either as a new derived sub-section of `#hyp-directed-separation-under-composition` (promoting that hypothesis closer to derived along the routing-structure axis), or as a small derivation segment `#der-composite-class-inheritance`, or as a clean Discussion paragraph in `#der-directed-separation`. The table:

| Sub-agent class | Routing | Substrate | Composite class |
|---|---|---|---|
| Class 1 (Separated) | Goal-blind | Distinct | **Class 1 (Separated)** |
| Class 1 (Separated) | Goal-dependent | Distinct | **Class 3 (Coupled)** |
| Class 1 (Separated) | (any) | Shared with $G^c$-shaped allocation | **Class 3 (Coupled)** |
| Class 3 (Coupled) | (any) | (any) | **Class 3 (Coupled)** |
| Class 2 (Partial) | (any) | (any) | **Class 2 (Partial)** or **Class 3** |

This is the clean architectural-axis lift, independent of objective alignment. (Strategic-composition column is absent because the axis does not enter architectural classification.)

**(C7) `#impl-strategic-composition` §"Modular safety architectures fail under goal divergence" — preserve the conclusion, fix the mechanism.** The conclusion (modular safety architectures fail under goal divergence; the failure is structural; constitutional-AI red-teaming and mesa-optimizer formation are instantiations) is correct and load-bearing. The cited mechanism ("the composite is structurally Class 3 (Coupled)") is wrong per (F1). The correct mechanism (dynamic-regime change — equilibrium dynamics admit saddle-points, multi-equilibria, last-iterate non-convergence that contraction-regime guarantees rule out) gives the same conclusion on stronger ground. Re-derive the modular-safety implication from `#deriv-strategic-composition`'s $\alpha'/\beta'$ machinery directly.

## §V.3 Joseph-reserved decisions

Items §V.2 cannot decide without Joseph because they require taste-and-strategy calls that the math alone does not pin down.

**(J1) Conservative-fix vs truthful-fix for (C1).** The conservative fix preserves current canon by swapping "Class 3" → "Class 2" in the implications segment, leaving the underlying (F2)-refuted Class 2 claim in place. The truthful fix executes (C2)+(C3)+(C7) in the same cycle and replaces architectural-class language with dynamic-regime language across all affected segments. The truthful fix is larger scope but is what integration-is-replacement licenses given the math. Joseph's call.

**(J2) Light-touch vs full meta-segment for (C5).** The light-touch option preserves the current meta-segment landscape and folds Axis B into `#disc-separability-pattern`. The full meta-segment option introduces `#disc-dynamic-regime` as a peer meta-segment. The full meta-segment is more truthful (Axis B is genuinely distinct from the separability pattern's content; treating it as a row in a ladder mis-fits it), but adds another segment for de-novo readers to learn. Joseph's call on the segment-count vs structure-clarity tradeoff.

**(J3) The placement of the architectural-class composite-inheritance table (C6).** Three options listed; each carries different consequences for whether `#hyp-directed-separation-under-composition` graduates from hypothesis-grade (the current state) to derived (the natural promotion after (C6)). Joseph's call given the segment-promotion economics.

**(J4) Whether to file a follow-on spike for the shared-substrate (R4) machinery.** (R4) was sketched but not derived in full. A `spike-shared-substrate-class-3` would derive the Class 3 result formally for multi-LLM-on-shared-backbone systems and would tie back to `#der-class-coercion-via-wrapping` for the wrapping-construction implications. Worth doing if multi-LLM-system analysis becomes load-bearing for `03-llm-core/`; defer-able otherwise. Joseph's call.

**(J5) Whether the dynamic-regime axis should also produce a `disc-modularity-state-dynamics` interaction.** The four-operation modularity-state picture from `#disc-adversarial-coupling-pressure` (truthification / strategic self-coupling / adversarial coupling pressure) is on the *modularity* axis, not the dynamic-regime axis. They are different. But strategic composition is what `#impl-strategic-composition` originally tried to read as "goal divergence as modularity-decreasing operation." Per the reframe, goal divergence is not modularity-decreasing at the composite level (it does not change architectural class); it is *dynamic-regime-changing* (contraction → equilibrium). The relationship to the modularity-state picture wants thinking through. Joseph's call on whether to fold this into the queued `disc-modularity-state-dynamics` cycle or to keep separate.

## §V.4 Spike disposition

**Status: ACTIVE — math pushed, landing reached, Joseph-reserved decisions itemized.** Promotion to canon (any of C1–C7) is gated on Joseph's calls on J1–J5. The math content of §§2–6 and §7 is self-contained and verifiable; the Cournot witness in (F1), the conflation diagnosis in (F2), and the type-mismatch in (F5) are exact under the stated formal criterion of `#der-directed-separation`. The internal contradiction in (F4) is mechanical (a literal-text contradiction across segments) and verifiable in 60 seconds.

The strengthen-first attempt did *not* yield the Class 3 strengthening Joseph asked for. It yielded:
- A derived no-go on the unconditional Class 3 claim, with a constructive Cournot witness.
- A discovery that the current Class 2 claim is also under-licensed by the formal criterion.
- An inter-segment contradiction (GUC-rename residue) that has been mis-stating the framework's position for ~12 days.
- A genuine reframe (dynamic-regime axis as Axis B distinct from architectural Axis A) that captures what strategic composition does shift.

Per Joseph's brief — *"if attempts keep yielding neither, it usually means we're framing the question wrong or are missing some other aspect that you can start to find"* — the spike landed on the second of those: a missing axis the framework has been awkwardly fitting into the architectural-class axis. Whether this is the right reframe is Joseph's call (J1, J2 in particular); the math is robust to whichever call he makes on canon updates.

## §V.5 Bridge to `spikes/INDEX.md`

This spike should be indexed under the next-cycle `INDEX.md` update as:

> **`spike-strategic-composition-class-3-attempt-2026-05-21/`** — Strengthen-first attempt to derive Class 3 (Coupled) composite from strategic composition; refuted with Cournot witness; current Class 2 claim also under-licensed by formal criterion; inter-segment contradiction in `#impl-strategic-composition` flagged (GUC-rename residue); dynamic-regime axis surfaced as missing-axis reframe. Joseph-reserved decisions on canon update path. Status: ACTIVE.

Files:
- `00-FRAMING.md` — question, current state across segments, contradiction discovery.
- `01-STRENGTHEN-ATTEMPTS.md` — four route attempts (R1 direct cross-talk; R2 rational-expectations; R3 mutual-modeling recursion; R4 shared substrate) plus revisit of the current Class 2 claim.
- `02-REFRAME-INSIGHT.md` — type-mismatch, dynamic-regime axis as Axis B, what the reframe buys.
- `99-VERDICT.md` — this file.

Cross-references: `#deriv-strategic-composition`, `#impl-strategic-composition`, `#der-directed-separation`, `#hyp-directed-separation-under-composition`, `#der-class-coercion-via-wrapping`, `#disc-adversarial-coupling-pressure`, `#disc-separability-pattern`, `#scope-composite-agent`.
