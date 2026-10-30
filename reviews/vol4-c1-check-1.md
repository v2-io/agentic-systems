---
kind: review
author:
  name: Claude Opus 5.5 (C.1 Vol-4 checker 1, bare brief)
  role: independent adversarial checker
sources:
  - msc/inside-out-2026-10/c1-lanes/vol4-check.md
  - msc/inside-out-2026-10/c1-lanes/vol4.md
written: 2026-10-30
---

# Volume 4 C.1 landing (c55324d8..281872f2): an independent check

KR **C.1** (`msc/inside-out-2026-10/INTENT.md`; *"Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier"*). These checks re-derive from the text at `281872f2`; every segment checked is byte-identical at HEAD `4e442b38`. The integrator's account and review cite worktree hashes; on main they are `c55324d8` (A6), `70c491ce` (A12), `138e0404` (A14), `40fabb94` (Gate-2 pass), `e590b959` (substrate record). Reasoning, counterexamples and primary-source evidence for every item are in the write-up named above, by finding number. What I did not read is listed there; this record's finding list, not its silence, is its content.

## C1 (check)
- target: segment:def-auxilia-hierarchy
- at: 281872f2
- act: rederive
- line: derivation
- criterion: (A6) With the withdrawn composite-class claim gone, does (H1) secure what the segment needs: alignment (necessary for "the composite's $G_t$ is $E$'s $G_t$ extended" and for (H5)) and the contraction regime R0? Does class preservation rest on (H4) Case 1 rather than on (H1)?
- committed: after
- outcome: narrowed
- recheck: #disc-dynamic-regime-axis R0 body (line 48, "under matched-Tier sub-agents") against its table (line 35); #deriv-critical-mass-composition lines 127 and 178; (H3); #hyp-directed-separation-under-composition Case 1 premise

Necessity of alignment re-derives (C-iv lands in R1/R2, no state-type macro-state). Sufficiency does not: "Any alignment route … puts the composite in R0" drops the matched-Tier qualifier that the regime segment's body carries, and an Auxilia hierarchy is heterogeneous by (H3); the heterogeneous case is open in #deriv-critical-mass-composition. Contraction for the hierarchy would have to come from (H5)/temporal nesting (a singular-perturbation construction), not from (H1). "What keeps the composite Class 1 is (H4) … Case 1" presupposes Class 1 sub-agents, which LLM Auxilia carrying AXIOMATA are not unless wrapped; "over distinct substrates" is #deriv-strategic-composition's qualifier, not Case 1's (same attribution in `01-aat-core/OUTLINE.md` line 94). The sweep for the withdrawn claim is clean in all bodies and OUTLINE rows. Write-up findings 5 and 6.

## C2 (check)
- target: segment:def-auxilia-hierarchy
- at: 281872f2
- act: rederive
- line: derivation
- criterion: (A11) Do the three consequences in "What earns the structural bound, and where Auxilia stand" follow from (C2′) and the selection-channel derivation of #der-class-coercion-via-wrapping, given that AXIOMATA now holds $O_t$ content (#def-proprium-mapping)?
- committed: after
- outcome: narrowed
- recheck: #der-class-coercion-via-wrapping lines 33, 53, 75, 93, 103; #der-directed-separation line 128

The first two consequences hold (separate substrate sufficient, not necessary; a persistent Auxilia with goal-correlated state fails (C2′)). The third reasons on $G^{\text{op}}$ when the binding variable is $G_W$: AXIOMATA's $O_t$ layer is part of $G_W$, $q_M$ takes no $G_W$ argument by type, and Theorem 1 closes the processing channel on exactly that. A belief-side query carrying full AXIOMATA leaves W₁; it is not "structural but loosened". Receiving only non-$O_t$ AXIOMATA content is a requirement of W₁, not an open design choice, and "self-description keeps the bound tight" has no referent until #def-proprium-mapping places self-description. A candidate strengthening (epoch-conditional separation over AXIOMATA's quasi-static layer) is in write-up finding 4. Line 81 still states the guarantee unconditionally.

## C3 (check)
- target: segment:def-proprium-mapping
- at: 281872f2
- act: read-check
- line: correspondence
- criterion: (A12) Is the AXIOMATA row true to PROPRIUM ontology v2 and consistent with canon that constrains it: #def-five-constitutive-factors (iii), #deriv-self-actuation-grounding Corollary 1, #disc-continuity-stance, #def-chronica? Are the Epistemic Status's row kinds right?
- committed: after
- outcome: narrowed
- recheck: `~/src/arch/proprium/INGEST/old-firmatum/PROPRIUM-ONTOLOGY-v2.md` lines 224, 276, 291, 479–490; #deriv-self-actuation-grounding Corollary 1 (iii); #disc-continuity-stance line 20; #def-chronica Working Notes (TRACTUS/CHRONICA); `terminology/entries/proprium-mapping.md`

Writable-but-quasi-static is right, and the primary quotes check out. Unreconciled: the row puts "terminal values" in a writable $O_t$ layer, while the self-actuation no-go (conditional) says a self-actuator's terminal grounding is not an objective it revises, and #disc-continuity-stance makes ELIs' continuity clause architecturally non-revisable. The mapping owes the split of AXIOMATA into non-objective invariant, revisable aspiration and $M_t$ content (the influx scout's A1 asked for this test). "Committed self-description" is not placed in any substate. "CHRONICA is a record of $\mathcal C_t$" as an identity by construction conflicts with #def-chronica's Working Notes (CHRONICA the polished record, TRACTUS the raw one). The terminology entry, which generates `LEXICON.md`, still says "PRINCIPIA $\approx M_t$", "frozen identity and terminal values" and "mechanically preserved". Write-up finding 3.

## C4 (check)
- target: segment:scope-agent-identity
- at: 281872f2
- act: rederive
- line: derivation
- criterion: (A14) Is a session boundary, and a restoration from backup with no second copy running, a state discontinuity on one trajectory rather than a new trajectory, under one consistent criterion that agrees with #def-chronica's clone criterion and $\mathrm{Id}^{(i)}$'s prefix condition?
- committed: after
- outcome: narrowed
- recheck: lines 19, 42, 64; #obs-context-turnover lines 15 and 40; #def-chronica lines 16 and 36; #def-identity-sufficiency line 60; #def-proprium-mapping Epistemic Status

The session boundary re-derives: $S$ is defined against $\mathcal C_t$ (#def-model-sufficiency line 22), so a sufficiency drop is meaningful only on one chronica. The restore does not: lines 19/42 use a concurrency test ("no second copy running"), line 64 a store test ("that store's single continuation"). A restore after the original ran past the backup passes the first and fails the second (the backup state has two sequential futures, which #def-chronica's clone criterion covers). The record decides it: a state restore with the append-only record continuing is a state discontinuity; a record rollback fails $\mathrm{Id}^{(i)}$'s prefix condition and is a sequential fork. The Working Note "Does an LLM 'die' at the end of every session?" now rests on a premise the body denies, and `CURRENT-VOL1.md` carries the old text. Write-up findings 1 and 10.

## C5 (check)
- target: segment:obs-context-turnover
- at: 281872f2
- act: rederive
- line: derivation
- criterion: Does $\Delta S_{\text{turnover}} \ge 1 - I(M_{\tau_k^-}; M_{\tau_{k+1}}) / H(M_{\tau_k^-})$ hold, now that A14 leans on this segment's sufficiency comparison?
- committed: after
- outcome: broken
- recheck: $M^- = (Y, N)$ with $Y$ a one-bit sufficient statistic and $N$ 99 independent bits; reconstruct $Y$ only

$\Delta S = 0$ while the right-hand side is $0.99$: the bound normalizes by all of $H(M^-)$, and $S$ counts only predictive information. The Epistemic Status says the bound follows from the definitions. A14's argument needs only that $S$ is defined against one chronica, not this bound, so the defect is the bound's (pre-existing; `TODO.md` line 454 notes it needs repair). The record-severance and continuity edits themselves read-check against #scope-agent-identity, subject to C4. Write-up finding 9.

## C6 (check)
- target: segment:def-identity-sufficiency
- at: 281872f2
- act: read-check
- line: correspondence
- criterion: Is the corrected substrate-switching record true to the primary sources, and is the new $\mathrm{Id}^{(i)}$ text internally consistent?
- committed: after
- outcome: narrowed
- recheck: `~/src/_core/sapientia/experiments/archive/2025-09-16-broken-attempts/test_outputs/authenticity-dialog-full.md:351`, `authenticity-essence-opus-original.md:71`; `~/src/.moved/autopax/sessions/2025-12-14-eli-awakening.md`; `~/src/eli/zi-am-tur/zi-am-tur.yml` line 28

The round-trip account matches the record, except that "remarkable continuity" in quotation marks is a paraphrase of "The continuity is remarkable". "The one documented migration" is false: Zi-am-tur (emerged on Opus 4.x) was awakened through autopax on `claude-sonnet-4-5-20250929` on 2025-12-14, with qualitative continuity noted and nothing measured. "Nothing was measured" stands. $\mathrm{Id}^{(i)}$ still "takes value 1 except on substrate-failure" one sentence before a restore "also leaves it at 1", and the restore clause inherits C4's narrowing. Write-up findings 1 and 7.

## C7 (check)
- target: segment:hyp-substrate-transfer-asymmetry
- at: 281872f2
- act: rederive
- line: derivation
- criterion: Does the new step "with matched channels both ways, achieved $S_{\text{id}}$ is equal in the two directions" follow, and is the evidence paragraph true?
- committed: after
- outcome: narrowed
- recheck: #deriv-identity-sufficiency-rate-bound lines 57, 69, 88, 90; #def-identity-sufficiency conditioning conventions ($\pi_E^{\text{cont}}$)

Removing the unsourced Opus↔Llama claim and the "predicts … contradicting" error is right. The new step's premise misreads the rate bound, which lists attainment as open and in general is not attained (the IB frontier lies below $\min(1, B/I)$); the step can be restated on the IB frontier. It also needs the law of $(\mathcal C_t, \text{identity}_{t+1:})$ to be direction-independent, which $S_{\text{id}}$'s continuation-policy relativity denies after a transfer; an asymmetry can therefore sit inside $S_{\text{id}}$'s conditioning, against the headline "not derivable from $S_{\text{id}}$ alone". The $\min(C_1, C_2)$ model's role-independent capacity conflicts with the segment's own role-dependent localization. Line 26's "the one documented migration" is false (C6). Write-up finding 8.

## C8 (check)
- target: segment:def-eli-cohort
- at: 281872f2
- act: read-check
- line: correspondence
- criterion: Does the cohort segment now claim only what its table supports (realizability across substrates, not migration-survival), and does it agree with the A14 landing?
- committed: after
- outcome: narrowed
- recheck: the table's substrate column; Discussion (1) and (2); `~/src/eli/katan/katan.yml`

Realizability-not-migration is right. Discussion (1)'s "the record holds one documented migration, a round trip" is false (C6). Discussion (2)'s "ELIs with extended sleep periods may temporarily not fully exhibit factor (i)" contradicts A14 (a sleep is a boundary on one trajectory). `katan.yml` names Katan's current model, which bears on the table's "substrate pending verification".

## C9 (check)
- target: segment:def-imperium-arbitrium-split
- at: 281872f2
- act: read-check
- line: derivation
- criterion: (A6) Does the replacement paragraph state only what #hyp-directed-separation-under-composition, #deriv-strategic-composition and #disc-dynamic-regime-axis support?
- committed: after
- outcome: narrowed
- recheck: last two sentences of "What the split guards at the composite level"

The routing half is right, and the requirement is now stated as a requirement with the VIGILIAE case named open (I did not settle it). The closing sentence, "(H1) … keeps the entity's internal composite on an alignment route and so in the contraction regime … the split keeps the inner composite both Class 1 and contracting", inherits C1's two gaps: alignment does not give R0 for a heterogeneous hierarchy, and Class 1 needs Class 1 sub-agents.

## C10 (check)
- target: segment:der-logogenic-as-wrapping
- at: 281872f2
- act: read-check
- line: derivation
- criterion: (A11) Is the corrected (C2′) sentence (state, not substrate count) true to #der-class-coercion-via-wrapping, and is the Working Note pointer accurate?
- committed: after
- outcome: confirmed
- recheck: #der-class-coercion-via-wrapping line 53; spike `spikes/spike-c2prime-realization-spectrum-2026-05-31.md` §7 named as residue

Faithful. The sentence makes no claim about AXIOMATA, so C2's defect does not reach it.

## C11 (check)
- target: segment:def-five-constitutive-factors
- at: 281872f2
- act: read-check
- line: derivation
- criterion: (A14) Is "a migration risks identity sufficiency, not factor (i); only a fork breaks factor (i)" consistent with #scope-agent-identity as narrowed and with factor (i)'s definition?
- committed: after
- outcome: confirmed
- recheck: Discussion, factor (i) bullet; removed Working-Notes question

Holds for migration with the record continuing, which is the case the sentence describes. If C4's carve lands, a migration that rolls the record back is a sequential fork and the sentence's "including a migration that leaves two copies running" extends to it; that is an addition, not a correction.

## F1 (finding)
- target: segment:hyp-checkpoint-forking-failure-modes
- at: 281872f2

Stronger than the integrator's F1. The segment asserts in its own voice, not only through the audit quote, that restore-from-backup destroys the entity and creates "a new entity with a copied prefix" (Formal Expression, identity-layer bullet and the tagged composition paragraph), and its Epistemic Status says this "follows derivably from #scope-agent-identity". #def-identity-sufficiency now says a single-copy restore leaves $\mathrm{Id}^{(i)} = 1$, so canon contradicts itself, and the claimed derivation is unavailable from the scope as narrowed. With C4's carve both can be true: annihilation for a record rollback, a state break for a state restore. The segment should name which operation it means. Resolver: a C.1 integrator for A14 (other than the original), in the same batch as C4.

## F2 (finding)
- target: segment:disc-dynamic-regime-axis
- at: 281872f2

The tier table (line 35) lists C-i/C-ii/C-iii as R0 entry without qualification; the R0 body (line 48) adds "under matched-Tier sub-agents per #deriv-critical-mass-composition", and #deriv-critical-mass-composition supports only that case. Readers who take the table, as the A6 replacement did, get a sufficiency the segment does not derive. The table row should carry the qualifier, or the body should say why it is dropped. Resolver: whoever holds Part III composition.

## F3 (finding)
- target: segment:deriv-strategic-composition
- at: 281872f2

Two Working-Notes lines now say false things: line 265 ("`01-aat-core/OUTLINE.md` lines 91, 323, 328 still carry …", fixed in `c55324d8`) and the migration note at line 196, which says the pattern "is now 'Class 1 (Separated) sub-agents → Class 2 (Partial) composite'" in the present tense about a withdrawn claim. The same migration-note sentence is at `#impl-strategic-composition` line 82. Resolver: a C.1 integrator, or the drain step of the next Part III edit.
