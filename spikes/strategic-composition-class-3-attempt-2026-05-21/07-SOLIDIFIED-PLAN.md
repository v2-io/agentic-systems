---
spike: strategic-composition-class-3-attempt
file: 07-SOLIDIFIED-PLAN
parent: 00-FRAMING.md
prior: 05-INTEGRATION-PLAN
status: solidified — Joseph approved recommendations 2026-05-21; this is the executable plan
purpose: clean execution sequence with resolved decisions baked in; the reasoning lives in 05-INTEGRATION-PLAN.md
---

# Solidified plan — what gets executed

`05-INTEGRATION-PLAN.md` is the reasoning artifact (decision tree with branches, conditionals on background spikes, recommendation-grade Joseph-reserved decisions). This file is the executable solidification after Joseph's 2026-05-21 approval of the recommendations. It carries no branches and no recommendations — only the actions to be taken, in the order to take them, with the open items that remain Joseph-reserved itemized at the end.

## §S.1 Resolved decisions (Joseph 2026-05-21)

| Decision | Resolution | Source |
|---|---|---|
| **(J1)** Phase 1 fix style | **Conservative (1a)** — swap "Class 3" → "Class 2" + migration note in `#impl-strategic-composition` first; truthful work happens in Phase 4 | `05-INTEGRATION-PLAN.md` §I.7 recommendation |
| **(J2)** Light-touch vs full meta-segment | **Defer** to Phase 6 gate; ascend if `#disc-modularity-state-dynamics` lands | §I.7 recommendation |
| **(J3)** Architectural-class composite-inheritance table placement | **Discussion paragraph in `#der-directed-separation`** initially; upgrade later | §I.7 recommendation |
| **(J4)** Shared-substrate spike | **Defer** unless multi-LLM-system analysis becomes load-bearing for `03-llm-core/` | §I.7 recommendation |
| **(J5)** Modularity-state-dynamics interaction segment | **Defer** until both `#disc-modularity-state-dynamics` and `#disc-dynamic-regime-axis` are stable | §I.7 recommendation |
| **(J6)** Phase 1 vs Phase 4 ordering | **Phase 1(1a) immediately, Phase 4 later** — canon never in contradictory state | §I.7 recommendation |
| **(J8)** Spike Instance-6-alternate-framing | **Moot** — BG2 returned with content (scope-extension), not no-go | §I.12 resolution |
| **(J10)** New segment vs appendix extension for witness math | **New segment `#deriv-regime-marginal-indistinguishability`** per BG2 recommendation | §I.12 recommendation |

## §S.2 Open decisions remaining Joseph-reserved (no recommendation to approve)

These had no recommendation in §I.7 — they are genuine open trajectory decisions for Joseph alone.

| Decision | Status | Note |
|---|---|---|
| **(J7)** Standalone-paper trajectory | Open | Phase 7 does not execute without explicit Joseph go. Per `05-INTEGRATION-PLAN.md` §I.11, this now requires the §C.3 derivation spike (J9) to land first to be competitive. |
| **(J9)** Schedule the §C.3 derivation spike | Open | Would derive `03-DYNAMIC-REGIME-AXIS.md` §C.3 cost-asymmetry with a structural-distance metric. Prerequisite for J7. Estimated 2 cycles. |

## §S.3 Execution sequence

Numbered actions in execution order. Each action is a discrete unit suitable for a single commit cycle. Cycle estimates per action are nominal — the actual cycle granularity Joseph runs is his to determine.

### Phase 0 — Commit the spike body (immediate, before canon work begins)

**(P0.1)** Commit the strategic-composition-class-3-attempt spike directory contents as one commit:
- `spikes/strategic-composition-class-3-attempt-2026-05-21/00-FRAMING.md`
- `01-STRENGTHEN-ATTEMPTS.md`
- `02-REFRAME-INSIGHT.md`
- `03-DYNAMIC-REGIME-AXIS.md`
- `04-MATURITY-CHECK.md`
- `05-INTEGRATION-PLAN.md`
- `06-PILLAR-PRIOR-ART.md`
- `07-SOLIDIFIED-PLAN.md` (this file)
- `99-VERDICT.md`

Commit message: spike-completion narrative covering Cournot witness, GUC-rename-residue discovery, dynamic-regime axis surfacing, Pillar verdicts (BG1), broadened-Instance-3 finding (BG2), and the solidified plan.

**(P0.2)** Commit the sibling BG2 spike: `spikes/spike-identifiability-floor-instance-6-2026-05-21.md` as its own commit.

**(P0.3)** Update `spikes/INDEX.md` with the new spike-directory entry per the §V.5 INDEX skeleton from `99-VERDICT.md` (modified to reflect BG2 outcome being scope-extension rather than new instance). Commit as INDEX-update.

Pre-commit verification: confirm `git status` is clean before P0.1 (working tree should be clean — only the spike directory and the sibling spike are new). Confirm `bin/lint-md` passes on all eight spike files plus the sibling spike file.

### Phase 1 — Foundation fix (conservative, immediate after Phase 0)

**(P1.1)** Edit `01-aat-core/src/impl-strategic-composition.md`:
- Replace "Class 3 (Coupled)" → "Class 2 (Partial)" in the three occurrences in §"Strategic composition lifts contraction to equilibrium".
- Replace "Class-3-composite" → "Class 2 (Partial) composite" in Working Notes line 83 (finding `#23` reference).
- Add 2026-05-09 GUC migration note in Working Notes, identical-in-form to the notes in `#deriv-strategic-composition` / `#der-directed-separation`.

**(P1.2)** Commit as a single commit with message identifying the GUC-rename-residue fix and pointing at the spike for the discovery trail.

**(P1.3)** Run `bin/lint-md 01-aat-core/src/impl-strategic-composition.md` before commit. Run `bin/lint-outline 01-aat-core/OUTLINE.md` if it exists as a sanity check on cross-references.

Outcome: canon is no longer internally contradictory. Estimated cycle: 0.2.

### Phase 2(b) — Draft `#disc-dynamic-regime-axis` segment (integration framing)

**(P2.1)** Author `01-aat-core/src/disc-dynamic-regime-axis.md`:

Required content per BG1 verdict + §I.11 specification:
- **Frontmatter:** type `discussion`, status `discussion-grade`. Depends: `scope-composite-agent`, `deriv-strategic-composition`, `form-composition-closure`, `result-sector-persistence-template`, `deriv-critical-mass-composition`, `der-team-persistence`, `hyp-symbiogenic-composition`, `disc-separability-pattern`.
- **Open with integration framing.** State explicitly that the four-tier partition is consolidation of prior-art classifications under AAT-internal vocabulary; cite the six required prior-art works.
- **§B four-tier formal definition** from `03-DYNAMIC-REGIME-AXIS.md`.
- **§C derivable content** narrowed to the three AAT-specific contribution loci: §C.1 macro-state-type / regime structural identity for finite $N$ (with R3 as boundary case); §C.3 cost-asymmetry framing (argumentation-grade — derivation deferred to J9 spike); §H.5 candidate floor (referencing the broadened Instance 3 per Phase 3).
- **§F mapping table** as the integration-internal-to-AAT layer.
- **§G cross-axis interactions** (Axis A × Axis B independence; wrapping-construction regime-independence; alignment-work architectural-class-independence).
- **`## Findings`** with Brief at draft Feynman-criterion bar — the bathtub-equivalent for dynamic-regime needs one cycle of refinement.
- **`## Working Notes`** flagging the J7 paper trajectory and the J9 §C.3 derivation prerequisite.

Required citations to land before commit (verify primary sources where any specific theorem-number is invoked, per the generative-citations-invented discipline):
- Candogan, Menache, Ozdaglar, Parrilo 2011 — "Flows and Decompositions of Games: Harmonic and Potential Games," *Math. of OR* 36:474–503.
- Letcher, Balduzzi, Racanière, Martens, Foerster, Tuyls, Graepel 2019 — "Differentiable Game Mechanics," JMLR 20:1–40.
- Sandholm 2010 — *Population Games and Evolutionary Dynamics*, MIT Press.
- Hofbauer, Sigmund 1998 — *Evolutionary Games and Population Dynamics*, Cambridge.
- Omidshafiei, Papadimitriou, Piliouras, Tuyls, Rowland, Lespiau, Czarnecki, Lanctot, Perolat, Munos 2019 — "$\alpha$-Rank: Multi-Agent Evaluation by Evolution," *Sci. Rep.* 9:9937.
- Papadimitriou, Piliouras 2019 — "Game Dynamics as the Meaning of a Game," *SIGecom Exch.* 16(2):53–63.

**(P2.2)** Add segment to `01-aat-core/OUTLINE.md` at appropriate position (probably alongside `#disc-separability-pattern` / `#disc-identifiability-floor` / `#disc-additive-coordinate-forcing`).

**(P2.3)** Run `bin/lint-md 01-aat-core/src/disc-dynamic-regime-axis.md`, `bin/lint-outline 01-aat-core/OUTLINE.md`, `bin/extract-findings` to verify the Findings rolls up cleanly to root `FINDINGS.md`.

**(P2.4)** Commit as a single commit with the new segment + OUTLINE update.

Estimated cycle: 1.2.

### Phase 3(c) — Broaden Instance 3 + new appendix segment

**(P3.1)** Edit `01-aat-core/src/disc-identifiability-floor.md`:
- Broaden Instance 3's no-go statement from "coupling-sign bit unidentifiability" to "coupling-topology bit (sign + potential-existence + game-structure class) unidentifiability."
- Update Instance 3's escape menu: keep the existing four escapes (interventional access on coupling topology / matched Tier at composite level / passivity certificate / common contraction metric) and **add escape (e): composite-level convergence-rate-class observation** — passive distinguishability of R2 from {R0, R1} via exponential-vs-polynomial convergence rate.
- Add strengthened consequence: `#deriv-strategic-composition`'s sub-scope $\alpha'/\beta'$ partition is the unique broadly-available R1-vs-R2 regime classifier under escape (e).
- Add migration note in Working Notes: "Instance 3 scope broadened 2026-05-XX from coupling-sign bit to coupling-topology bit per `spikes/spike-identifiability-floor-instance-6-2026-05-21.md`. Old scope is a strict subset of new scope; downstream cross-references remain valid."

**(P3.2)** Author new segment `01-aat-core/src/deriv-regime-marginal-indistinguishability.md`:
- Type `derivation`, status `conditional`-with-`exact`-core (the symmetric-matched-Tier-1-scalar witness is exact).
- Depends: `deriv-strategic-composition`, `deriv-critical-mass-composition`, `disc-identifiability-floor`, `result-sector-persistence-template`.
- Formal Expression: the §3.3 witness math from BG2's spike — R0 (shared-objective contraction) vs R1 (Cournot with parameter-matched marginal mean + variance) cross-regime indistinguishability under marginal-Fisher rank-collapse on the topology coordinate. Plus R0 vs R2 (matching-pennies under aggregation) witness. Both via Liberzon 2003 anchor + Sylvester-at-one-remove rank-collapse mechanism.
- `## Findings` carrying the strengthened-Instance-3 consequence.

**(P3.3)** Add to `01-aat-core/OUTLINE.md` Appendix section.

**(P3.4)** Run lint + extract-findings.

**(P3.5)** Commit as a single commit covering both the Instance 3 broadening and the new appendix segment (they are tightly coupled — the appendix is the witness, the Instance 3 broadening is the meta-segment scope reflection).

**(P3.6)** Archive `spikes/spike-identifiability-floor-instance-6-2026-05-21.md` to `spikes/.integrated/` per the existing `.integrated/MANIFEST-YYYY-MM-DD.md` convention. Same commit or separate.

Estimated cycle: 1.0.

### A4 — Second-pass Undermind for revised T4 target (sub-cycle)

**(A4.1)** Run Undermind / targeted prior-art search for:
- Switched-system identifiability literature for *negative* results on coupling-topology-bit identification (Liberzon-2003-adjacent).
- Convergence-rate-class as regime classifier — any prior-art naming of escape (e).

**(A4.2)** Record findings as `spikes/spike-second-pass-undermind-instance-3-broadening-2026-XX-XX.md` (single file). If the search clears the broadening as not-previously-stated-in-this-form, the strengthened Instance 3 remains as landed. If the search finds substantial prior art, the strengthened-consequence framing tightens to adoption-with-citation.

**(A4.3)** Update Instance 3 in canon if A4.2 surfaces consequential prior art; commit if any update.

Estimated cycle: 0.3.

### Phase 4 — Truthful-fix cascade

**(P4.1) `#deriv-strategic-composition` revisions (per `99-VERDICT.md` (C2)).** Pull back the "Class 2 (Partial) composite" claim in Discussion §"Class-2-(Partial)-composite-from-Class-1-(Separated)-sub-agents" and in the Findings-style table row. Replace with the dynamic-regime axis language (R0 → R1 transition; macro-state-type change; no architectural-class change without additional conditions). Add cross-reference to `#disc-dynamic-regime-axis`. Update Working Notes. Update the sub-scope $\alpha'/\beta'$ paragraph with cross-reference to broadened Instance 3's R1-vs-R2 classifier strengthened-consequence.

**(P4.2) `#der-directed-separation` revisions (per (C3)+(C6) J3 resolution).** Pull back the Discussion §"Composite-level class inheritance" "Class 2 (Partial) composite" claim. Replace with the correct composite-class-inheritance content as a Discussion paragraph (per J3 resolution — Discussion paragraph in this segment is the initial home for the inheritance table from `02-REFRAME-INSIGHT.md` §7.3 (B5)). Add cross-reference to `#disc-dynamic-regime-axis`.

**(P4.3) `#impl-strategic-composition` re-derivation (per (C7)).** The Phase 1 conservative fix did the literal Class 3 → Class 2 swap. Now re-derive the §"Modular safety architectures fail under goal divergence" implication using the regime-axis mechanism (R0 → R1 transition; saddle-Nash; multi-equilibrium; last-iterate non-convergence). Replace the architectural-class-change mechanism with the regime-change mechanism. Preserve the conclusion (modular safety fails under goal divergence; constitutional AI red-teaming; mesa-optimizer formation as empirical instantiations).

**(P4.4) `#disc-separability-pattern` cleanup (per (C4)).** Audit row 3 ("Class 2 (Partial) — directed separation holds for identified submodules") for which sense of "Class 2" is meant. If structured-repair-tier-vocabulary use rather than architectural-class, rename to avoid ambiguity. Add dynamic-regime axis as 8th row: R0 separable core / R1 structured repair (under augmented Lyapunov — potential/monotone) / R2 + R3 general open. Cross-reference `#disc-dynamic-regime-axis`.

**(P4.5) `#scope-composite-agent` Working Notes update.** Resolve the first Working Notes bullet "Whether a common scalar exists across the alignment routes" in the negative — the four scope routes correspond to regime-tier entry conditions on the dynamic-regime axis, not to a continuous spectrum on a single scalar. Cross-reference `#disc-dynamic-regime-axis`.

**(P4.6) Cross-reference audit per R-Reg-6.** Grep for segments cross-referencing Instance 3 in its narrower form. Likely affected: `#deriv-critical-mass-composition` (Instance 3's source instance), `#scope-composite-agent` (Instance 3 enabling-condition language), `#impl-strategic-composition` (Instance 3 operationalization). Verify the broadening doesn't change downstream reasoning. Update language where needed.

**(P4.7) Commit batching.** One commit per segment touched, batched in 2–3 commits if multiple segments land in the same pass.

Estimated cycle: 2.5 (including the audit work).

### Phase 5 — Cross-segment ripple

**(P5.1)** Grep across `01-aat-core/src/` for "Class 2 composite", "Class 3 composite", "partially-opposing objectives", "strategic composition" — surface the full ripple set.

**(P5.2)** Light annotations (cross-reference to `#disc-dynamic-regime-axis`): `#form-composition-closure`, `#result-sector-persistence-template`, `#deriv-critical-mass-composition`, `#der-team-persistence`, `#hyp-symbiogenic-composition`, `#disc-separability-pattern` Contraction-ladder row.

**(P5.3)** Substantive annotations already done in Phase 4 (`#deriv-strategic-composition`, `#impl-strategic-composition`).

**(P5.4)** Cross-segment consistency audit at close: verify the regime-axis language used in the five core touched segments (`#deriv-strategic-composition`, `#der-directed-separation`, `#impl-strategic-composition`, `#hyp-directed-separation-under-composition`, `#disc-dynamic-regime-axis`) matches across all five. The §F mapping table in `03-DYNAMIC-REGIME-AXIS.md` is the consistency reference.

**(P5.5) Commit batching.** One commit per segment-family.

Estimated cycle: 1.0.

### Phase 6 — Meta-segment promotion (gated)

**Gate:** `#disc-modularity-state-dynamics` lands (currently queued per the four-meta-segment plan; see `CLAUDE.md` Key Architectural Decisions §7 forward-reference convention).

**(P6.1)** Upgrade `#disc-dynamic-regime-axis` status to meta-segment-grade (whatever the peer meta-segments carry — currently `discussion-grade` but with explicit meta-segment positioning).

**(P6.2)** Add complementarity statement with broadened `#disc-identifiability-floor` Instance 3 — Instance 3 (broadened) is the negative-half complementarity for both the Contraction ladder and the dynamic-regime four-tier ladder. This is the cleaner-than-anticipated complementarity landing per §I.12 (BG2 resolution).

**(P6.3)** Add parallel-pattern observation with `#disc-modularity-state-dynamics` — the three-operation parallel across Axis A and Axis B per `03-DYNAMIC-REGIME-AXIS.md` §G.

**(P6.4)** Add meta-pattern cross-references to the other meta-segments (`#disc-separability-pattern`, `#disc-identifiability-floor`, `#disc-additive-coordinate-forcing`, `#disc-modularity-state-dynamics`) per the existing four-meta-segment cross-reference pattern.

**(P6.5)** Commit as a single commit with the upgrade + cross-references.

Estimated cycle: 1.0 (plus wait time on `#disc-modularity-state-dynamics`).

### Joseph-reserved tail

**(J7 + J9)** Standalone-paper trajectory and the prerequisite §C.3 derivation spike. Not executed until Joseph greenlights. Estimated 2.0 cycles for the §C.3 derivation spike if J9 is greenlit; additional cycles for the paper authoring on top of that.

## §S.4 Total cycle estimate (executable scope)

| Phase | Cycles | Cumulative |
|---|---|---|
| Phase 0 (spike commit) | 0.1 | 0.1 |
| Phase 1 (foundation fix) | 0.2 | 0.3 |
| Phase 2(b) (segment authoring) | 1.2 | 1.5 |
| Phase 3(c) (Instance 3 broaden + new appendix) | 1.0 | 2.5 |
| A4 (second-pass Undermind) | 0.3 | 2.8 |
| Phase 4 (truthful-fix cascade) | 2.5 | 5.3 |
| Phase 5 (cross-segment ripple) | 1.0 | 6.3 |
| Phase 6 (meta-segment, wait-gated on `#disc-modularity-state-dynamics`) | 1.0 + wait | 7.3 + wait |

**Total executable scope: ~7.3 cycles plus wait time on `#disc-modularity-state-dynamics`.**

Joseph-reserved tail (J7 + J9) adds ≥2 cycles if greenlit.

## §S.5 What to confirm before P0.1 fires

This file is solidified but the *execution* — actually firing P0.1 to commit the spike body, then P1.1 to start modifying canon — is a separate decision. The plan is in place; the trigger is Joseph's.

Three confirmations recommended before P0.1:

- **Joseph reads `07-SOLIDIFIED-PLAN.md` (this file)** and confirms the resolved decisions (§S.1) reflect his intent on J1, J2, J3, J4, J5, J6, J10. The recommendations were broadly approved; the per-decision specifics here are the concrete operationalization that follows from the approval.
- **Joseph confirms the commit-cadence** matches his preference. The plan assumes one commit per phase-subaction (with some batching in Phases 4–5 where multiple segments land in the same cycle). If Joseph wants tighter granularity (per-file commits) or looser (one commit per phase), the action items don't change but the commit boundaries do.
- **Joseph confirms execution start point.** Three options: (a) fire P0.1 now and run through Phase 5 in sequence; (b) fire P0.1 + P0.2 + P0.3 now (spike commits) and pause for review before P1.1 (canon modification starts); (c) defer all execution pending Joseph's separate go-ahead per phase.

## §S.6 One-paragraph executive

Joseph approved the recommendations 2026-05-21. The solidified plan resolves seven of the ten Joseph-reserved decisions per the recommendations in the integration plan, leaves two genuinely-open (J7 paper, J9 §C.3 derivation spike), and marks one moot (J8). Phase 0 commits the spike body. Phase 1 fixes the GUC-rename residue in `#impl-strategic-composition` conservatively. Phase 2(b) drafts `#disc-dynamic-regime-axis` as a discussion-grade segment with prior-art integration framing per BG1's Pillar verdict (cite Candogan-Ozdaglar-Parrilo 2011, Letcher-Balduzzi 2019, plus four others). Phase 3(c) broadens `#disc-identifiability-floor` Instance 3 scope from coupling-sign bit to coupling-topology bit per BG2's scope-extension finding, plus lands a new appendix segment `#deriv-regime-marginal-indistinguishability` carrying the witness math. A4 runs a second-pass Undermind for the broadened Instance 3 scope. Phase 4 executes the truthful-fix cascade across `#deriv-strategic-composition`, `#der-directed-separation`, `#impl-strategic-composition`, `#disc-separability-pattern`, `#scope-composite-agent` with a cross-reference audit. Phase 5 ripples the axis-surfacing across ten+ remaining segments. Phase 6 promotes `#disc-dynamic-regime-axis` to meta-segment status, gated on `#disc-modularity-state-dynamics` landing. Total executable scope is ~7.3 cycles plus wait time. The kebab is plated; the only question left is when to put it on the table.

## §S.7 Execution status (live — updated 2026-05-22)

| Phase | Status | Commit(s) | Notes |
|---|---|---|---|
| Phase 0 — spike commit + executor handoff | ✅ Completed | `3e81a33` (NEXT-UP §5 + INDEX), `47ffe76` (spike body, Joseph) | Pre-cycle commits done before P0.1 fired |
| Phase 1 — GUC-residue conservative fix | ✅ Completed | `0884e12` | 6 occurrences swapped; 2 correct refs preserved; migration note added |
| Phase 2(b) — `#disc-dynamic-regime-axis` segment | ✅ Completed | `a492739` | Discussion-grade landing with 6 prior-art citations + §F mapping + §G cross-axis interactions + Findings |
| Phase 3(c) — Instance 3 broadening + new appendix | ✅ Completed | `5760694` | `#disc-identifiability-floor` Instance 3 broadened (coupling-topology bit + escape (e) + 4th strengthened consequence); `#deriv-regime-marginal-indistinguishability` new appendix; BG2 spike archived to `.integrated/` |
| A4 — Second-pass Undermind for broadened Instance 3 | ✅ Completed | `085c246` | BG2 report at `ref/Unidentifiability_and_rate_class_prior_art.md`; verdict: no exact hit on either Q1 or Q2 but rich near-miss landscape; verification-deferred footnote `[^bg2-2026-05-21]` added at 12+ citation points across 3 segments; segment-voice violation in strengthened consequence #4 corrected; Hamdan 2000 journal-name slip caught + corrected |
| Phase 4 — Truthful-fix cascade | ✅ Completed | `6a21669` | 7 segments touched: `#deriv-strategic-composition` (Class 2 pullback), `#der-directed-separation` (axis-decomposed inheritance table per J3), `#impl-strategic-composition` (modular-safety mechanism re-derivation), `#disc-separability-pattern` (8th ladder for dynamic regime), `#scope-composite-agent` (common-scalar Working Note resolved), `#disc-identifiability-floor` (7→8 ladder ref), `#der-loop-interventional-access` (Composite-layer broadening) |
| Phase 5 — Cross-segment ripple + Track E catalog | ✅ Completed | `05f2654`, `ffda862`, `3e67a5e` | 8 segments + Row 14 catalog rewrite + 6-segment Track E surface-back with `[^cat-2026-05-22]` verification-deferred footnotes (catalog citations from rows 05, 08, 14) |
| Phase 6 — Meta-segment promotion | 🟡 **GATED on Track D** (`#disc-modularity-state-dynamics`) | — | Independent cycle per CLAUDE.md Key Architectural Decisions §7 and `msc/modularity-cycle-plan-2026-05-09.md`. Not in executor's launch scope per (T7) tactical decision. Track A Phase 6 will pick up when Track D lands. |

**Joseph-reserved tail (J7 + J9):** Still genuinely open per §S.2. No executor action; needs explicit go.

**Primary-source verification spike (cross-cluster):** Queued across 9 segments. Two footnote classes: `[^bg2-2026-05-21]` (BG2 raw Undermind synthesis, weaker support) and `[^cat-2026-05-22]` (Track E catalog, prior Pillar-style search support but executor-unverified). Verification targets in load-bearing order specified in each segment's Working Notes. Needs Joseph's go.

**Track A complete except for Phase 6's Track D gate.** Subsequent tracks per `spikes/NEXT-UP.md` §3: Track B (implementation-impossibility meta-segment), Track C (meta-segments-before-instances narrative sweep), Track E remaining (rows 05/08/11/21 catalog dissolution — per Joseph's 2026-05-22 throwaway framing).
