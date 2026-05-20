---
source_cycle: 542891 (de-novo, auditor unknown; cycle ended after one segment reflection)
extraction_agent: Claude Opus 4.7 (1M context), parallel-sweep slice
extraction_date: 2026-05-20
working_dir: audits/AUDIT-WORKING-542891/ (2 files, ~90 lines combined)
final_of_record: none — auditor wrote initial predictions and one segment reflection, did not proceed further
status_kind: partial auditor cycle (one segment in, then stop)
purpose: |
  Extract the predictions register + the single segment reflection from the
  WORKING dir for routing through the standard audit-routing process. Two-file
  cycle: 00-initial-predictions.md (~40 substantive lines) +
  01-def-agent-environment.md (the auditor's first per-segment reflection).
  Because no further walk happened, the predictions themselves are most of the
  gold — the calibration signal of what an external de-novo reader anticipated
  about the framework before opening any segment. The single reflection also
  carries a §14 wandering-thoughts paragraph plus an explicit self-correction
  about audit-procedure (the auditor caught themselves batching reads against
  protocol) which is process-feedback worth preserving.
---

# Audit-findings extract — 542891 working-dir mining

## Provenance and scope

The 542891 cycle is a **partial auditor cycle**: the WORKING dir contains two files — `00-initial-predictions.md` (~40 substantive lines) and `01-def-agent-environment.md` (~50 lines, the auditor's first and only per-segment reflection, following the 14-question reflection template). Both files are dated 2026-05-16 by filesystem mtime; no date appears in the content itself. No FINAL deliverable, no §B findings draft, no `running-outline.md`, no further per-segment reflections. The cycle appears to have ended after a single segment was reflected on — apparently either context-end or auditor-initiated stop, indeterminable from contents.

What this dir contributes despite the small surface:

1. A **structured predictions register** organized by themes — content predictions per component, openness predictions, overclaim predictions, novelty predictions, expected-findings predictions. Six clusters of falsifiable predictions, ~13 sub-predictions in total.
2. A **single segment reflection** that confirms one prediction (Section I as bedrock formalism), surfaces a §14 wandering-thoughts paragraph connecting `#def-agent-environment` to Friston's Markov-blanket and to LLM context-window framing, and contains a **process self-correction**: the auditor explicitly recognized they had violated the "one-segment-at-a-time, reflect-between-reads" instruction. That self-correction is itself instruction-feedback worth preserving even though the cycle did not continue long enough to demonstrate the corrected practice.

Treating both layers as routing input: the predictions get first-pass scrutiny against current `src/`; the reflection's §14 ideation is a single small ideation note worth recording; the process self-correction is `process/instruction-feedback`.

---

## Part I — Predictions register (preserved verbatim, attributed)

The predictions, transcribed under the auditor's headings. Each is given a P-id for cross-reference in Part II's scrutiny.

### Theme 1 — Topology of the framework (anticipatory shape)

- **P0-topology.** "Section I (Adaptive Systems) is the bedrock: formalizing the loop, mismatch dynamics, and the persistence condition ($\alpha > \rho/R$) using Lyapunov stability and event-driven dynamics. It is the most mathematically closed section. Section II (Actuated Agents) adds goals and introduces the orient cascade, separating satisfaction gap from control regret. Crucially, its exact results depend on *directed separation* (Class 1, modular agents). Section III (Agentic Composites) builds on the above to model multi-agent interactions and composite agents, using a bridge lemma and contraction-template generalization. TST acts as the high-identifiability calibration laboratory. Logogenic Agents drop the directed separation assumption, investigating which AAD results survive. Logozoetic Agents add moral continuity (mostly future work)."

### Theme 2 — Predictions about content (per component)

- **P1-aat-i.** "01-aat-core: I expect to see very clean derivations for the persistence condition and mismatch ODEs in Section I."
- **P1-aat-ii.** "In Section II, I expect the strategy DAG formalisms to be tightly coupled with Pearl's causal hierarchy."
- **P1-aat-iii.** "In Section III, I expect the adversarial dynamics to fall out cleanly from the signed coupling ($\gamma$) and agent opacity ($H_b$)."
- **P1-tst.** "02-tst-core: I expect strong empirical mappings where git commits represent the chronica and tests/deploys are literal interventions. The exponential cognitive load and coherence/coupling metrics will likely be mathematically grounded in AAD's deliberation cost and causal-information-yield."
- **P1-llm.** "03-llm-core: I expect a careful treatment of which Section II results survive the loss of directed separation (the 16/5/2/1 classification mentioned in the OUTLINE)."
- **P1-eli.** "04-eli-core: Mostly conceptual groundwork and proposed gaps around 'Crèche' and 'the three deaths'."

### Theme 3 — Predictions about what's open

- **P2-comp-dyn.** "Composition Dynamics: The transition dynamics for composition (how composites form/restructure) and endogenous coupling (how $\gamma$ evolves) are explicitly marked as gaps."
- **P2-llm.** "Logogenic Formulation: The language-specific orient cascade and self-referential closure are likely still in the exploratory/brainstorming phase."
- **P2-eli.** "Logozoetic Formalization: The formal machinery for moral continuity is completely open."

### Theme 4 — Predictions about what's overclaimed

- **P3-comp.** "Composition Bridge Lemma: I suspect the contraction assumptions required for composition closure might be overly restrictive or not fully satisfied by purposeful agents (as hinted by the Mori-Zwanzig spike mentioned in historical notes)."
- **P3-class2.** "Class 2 Bias Bounds: The conditions under which the bias bounds hold for fully-coupled agents (LLMs) might be narrower than the framing suggests, or they might rely on Lipschitz assumptions that are violated in practice."
- **P3-idfloor.** "Identifiability-Floor Escapes: The claims that AAD machinery uniquely escapes certain information-theoretic no-go theorems might be slightly overextended if the 'interventional access' provided by the feedback loop isn't truly Pearl Level 2 in all domains."

### Theme 5 — Most novel and consequential claims (auditor's anticipatory ranking)

- **P4-novel.** Four claims expected to be most novel/consequential: (a) Satisfaction Gap vs. Control Regret (world-doesn't-permit-it vs. you're-not-doing-it-well-enough); (b) Loop as Level-2 Causal Engine; (c) Meta-Patterns (identifiability-floor + additive-coordinate-forcing); (d) Software as Calibration Lab.

### Theme 6 — Expected findings (what the auditor expected to surface)

- **P5-class1-residue.** "Cross-Segment Contradictions: Given the recent integration of Class-2 (coupled) agents and new meta-patterns, I expect some earlier Section I/II segments to still carry implicit Class-1 assumptions or outdated framing."
- **P5-appendix.** "Math/Notation Gaps: In the appendices (especially around the recent Fenchel-Bregman reframe or the constant $C$ derivations), I might find dropped constants, sign errors, or unstated Lipschitz conditions."
- **P5-status.** "Status Label Mismatches: I expect to find some segments labeled `exact` that should be `conditional`, or `derived` claims that rely on `hypothesis`-level assumptions in the appendices."

---

## Part II — Calibration signal: what these predictions tell us about external first-encounter

Stepping back from per-prediction scrutiny: as a corpus, the predictions reveal an external reader's pre-segment-walk model of the framework. Some patterns worth noting before the per-prediction work:

- **The reader has clearly read README + OUTLINEs and absorbed the framework's own self-conception.** Specific lexical hits — "directed separation," "GUC Class 1/2/3" (using the historical numbering, the reader writes "Class 1 = modular"), "Mori-Zwanzig spike," "Fenchel-Bregman reframe," "16/5/2/1 classification," "identifiability-floor" and "additive-coordinate-forcing" — indicate the reader has *also* consulted CLAUDE.md, the meta-segments, the spike trail. This is a more saturated baseline than 184930's reader had; the predictions are correspondingly more specific.
- **Reader writes "AAD" not "AAT" throughout** — this dates the cycle (or the reader's reference snapshot) to **pre-2026-05-15** when the AAD→AAT rename landed (per CLAUDE.md naming-note). The mtime says 2026-05-16, which is one day after the rename; either the reader was still using their pre-rename mental model, or the file was created from an earlier scratch draft. Not a defect — `_obs/`, `LOG.md`, and the AAD-named decision records are still "read AAD as AAT" per CLAUDE.md.
- **Three of the four novelty-predictions (P4) hit the framework's actual high-novelty claims directly.** Satisfaction gap vs control regret, loop as Level-2 causal engine, and the meta-patterns are *exactly* the items the framework itself labels as most-novel (see `01-aat-core/OUTLINE.md` and `FINDINGS.md`). The fourth — software-as-calibration-lab — is a less universal framing-level claim, but is also load-bearing in TST.
- **The reader's overclaim-candidates (P3) target the framework's three most-discussed pivots:** composition admissibility, Class-2 LLM treatment, identifiability-floor scope. This matches the framework's own architectural-proposals portfolio: the 471203 cycle's SP-23 (theorem-import architecture) and SP-12 (commitment state) live near these. The reader's overclaim-prediction list is therefore structurally well-located, even before per-prediction strength is evaluated.
- **The reader anticipated the 16/5/2/1 classification correctly** — that specific four-tuple appears in `03-llm-core/src/result-section-ii-survival.md:37` *verbatim*: "16 survive exactly for Class 3 (Coupled) agents, 5 survive approximately with bounded error, 2 require modification, and 1 fails by definition." This is direct prediction-match.

**Net signal:** the framework is *legibly differentiated by component* to a saturated external reader at the README+OUTLINE+CLAUDE level. The reader correctly identifies novelty centroids, correctly locates overclaim-surfaces, and correctly anticipates specific structural claims (16/5/2/1). The predictions track to actual segments more than they miss. This is calibration evidence — alongside 184930 and 471203 — that the framing-layer materials are doing real work for external comprehension.

---

## Part III — First-pass scrutiny against current `src/`

Per-prediction verdict + segments read first-hand. First-pass is flag-for-routing, not graduation-grade; the §8 independent-verify gate fires downstream.

### P0-topology: Section I bedrock / II goal-machinery / III composition / TST as calibration / 03 survival-classification / 04 future

**Segments read first-hand:** `01-aat-core/src/def-agent-environment.md`, `01-aat-core/src/def-action-transition.md`, `03-llm-core/src/result-section-ii-survival.md` (head + classification table). CLAUDE.md (framework structure section), `03-llm-core/` directory listing.

**Verdict:** `confirmed` (calibration data).

The auditor's anticipated topology matches the framework's actual structure exactly: I-bedrock / II-goals-and-orient-cascade / III-composition / TST-calibration-lab / 03-survival-of-II-under-coupling / 04-future-with-moral-continuity. The "Class 1 = modular" specifically matches the historical-numbering side of the GUC table (the reader has not yet absorbed the 2026-05-09 GUC renumbering — see CLAUDE.md §Known Fragilities / GUC class table). The 16/5/2/1 expectation lands exactly on `result-section-ii-survival.md` ("16 survive exactly … 5 survive approximately … 2 require modification … 1 fails by definition").

**Routing recommendation:** `soft-polish` / calibration-data — material for any future framing-level case study on how the README+OUTLINE+CLAUDE stack reads to external de-novo audiences. No new action.

### P1-aat-i: clean Lyapunov persistence-condition derivations in Section I

**Segments read first-hand:** none on this pass first-hand; relied on prior-pass first-hand reads of `01-aat-core/src/deriv-sector-condition.md` recorded in `audit-findings-184930.md` Part III P1-forced (sector-condition Lyapunov framing as the *strengthen-before-soften* generalization of the linear-Lyapunov anticipation).

**Verdict:** `confirmed-stronger` (transitively via 184930 scrutiny).

The framework delivers nonlinear-Lyapunov via the sector condition, with the linear case as a recovery — strictly more general than "clean Lyapunov-of-linear-ODE." Same disposition as 184930's P1-forced.

**Routing recommendation:** `soft-polish` — already covered by 184930's calibration entry; no new action.

### P1-aat-ii: strategy DAG tightly coupled with Pearl's causal hierarchy

**Segments read first-hand:** none on this pass first-hand; relied on 184930's P1-chosen first-hand read of `def-strategy-dag.md` showing DAG structure as forced (via `deriv-graph-structure-uniqueness`) and AND/OR parameterization as chosen. CLAUDE.md OUTLINE section names `def-pearl-causal-hierarchy.md` as the Pearl-hierarchy carrier (also read first-hand in this pass for the dir-listing).

**Verdict:** `confirmed` — `def-strategy-dag.md` depends on Pearl-hierarchy machinery and the framework explicitly derives the DAG structure from causal-hierarchy + temporal-order. Same general disposition as 184930's P1-chosen.

**Routing recommendation:** `soft-polish` — already covered by 184930.

### P1-aat-iii: adversarial dynamics from signed coupling γ and agent opacity H_b

**Segments read first-hand:** none on this pass; directory-listing shows `der-adversarial-destabilization.md`, `der-agent-opacity.md`, `der-resource-bounded-destabilization.md` are all present in `01-aat-core/src/` — consistent with the prediction's expectation of clean signed-coupling + opacity machinery for adversarial dynamics.

**Verdict:** `deferred` (partial verification — segment presence confirms framework-shape; first-hand content read not done on this pass).

The presence of the predicted segments is itself signal, but a graduated verdict on "fall out cleanly" requires first-hand reading of those segments (specifically `der-adversarial-destabilization` and `der-agent-opacity`). Honest deferral.

**Routing recommendation:** `deferred-for-second-pass`. If the segments derive adversarial dynamics from γ and H_b as predicted, this is a low-effort `confirmed`. If the adversarial machinery turns out to rely on additional structural assumptions not predicted, this is a calibration miss worth recording — but unlikely to be a strengthen-before-soften target since the prediction is *anticipatory*, not a softening recommendation.

### P1-tst: git as chronica, tests/deploys as interventions; cognitive-load and coherence/coupling grounded in deliberation-cost and CIY

**Segments read first-hand:** none on this pass; relied on 184930's P3-tst first-hand read of `hyp-causal-discovery-from-git.md`. Directory listing shows `hyp-exponential-cognitive-load.md`, `meas-coherence-coupling.md`, `der-code-quality-as-observation-infrastructure.md` exist in `02-tst-core/src/` — consistent with the prediction.

**Verdict:** `confirmed` (transitively via 184930). The framework demotes the git-as-do(a) claim to discussion-grade for the developer-mental-model confounder (C3) — the prediction "git commits represent the chronica and tests/deploys are literal interventions" is correctly named in scope but honestly tempered in epistemic status. Cognitive-load / coherence-coupling grounding in deliberation-cost / CIY would need first-hand reads of the listed segments to verify the *grounding* direction (top-down from AAT into TST).

**Routing recommendation:** `soft-polish` for the chronica/intervention half (subsumed by 184930-P3-tst); `deferred-for-second-pass` on the grounding-direction half (cognitive-load and coherence-coupling).

### P1-llm: 16/5/2/1 classification of Section II survival under Class-2 coupling

**Segments read first-hand:** `03-llm-core/src/result-section-ii-survival.md` (head + classification preamble + first ~30 rows of the survival table).

**Verdict:** `confirmed-stronger` (the prediction is exactly what the framework delivers, plus the framework names the GUC class-renumbering scar that the reader's pre-2026-05-09 mental model was about to encounter).

The 16/5/2/1 numbers appear verbatim. The segment also surfaces the GUC class-renumbering warning explicitly: *"Goal-Update Coupling Class numbering changed 2026-05-09. Anything older than git tag `pre-guc-rename-2026-05-09` uses the old Class numbering: Class 1 → Class 1 (Separated/Modular); Class 2 → Class 3 (Coupled/Undirected); Class 3 → Class 2 (Partial/Operational)."* The reader's predictions use the historical Class 2 = LLMs, which now maps to current Class 3 (Coupled). The framework provides the translation table inline — strengthen-than-predicted, in the same direction noted in 184930-P2-ds (the framework names its own contested-pivot scar).

**Routing recommendation:** `subsumed-by-existing-machinery` — `result-section-ii-survival.md` is the disposition. The 16/5/2/1 prediction is exactly carried.

### P1-eli: mostly conceptual groundwork around Crèche and three deaths

**Segments read first-hand:** none on this pass; CLAUDE.md confirms `04-eli-core/` is the "Logozoetic Framework" at "future work" stage, and the reflection's wandering-thoughts paragraph independently raised the question "if moral continuity is required, how does that interact with this boundary?" — i.e. the reader's own anticipation matches the framework's stated status (mostly conceptual + open).

**Verdict:** `confirmed` (low-resolution).

**Routing recommendation:** `soft-polish` / calibration-data — no specific action.

### P2-comp-dyn: composition transition dynamics + endogenous γ evolution as marked gaps

**Segments read first-hand:** none on this pass first-hand; relied on CLAUDE.md "Known Fragilities" + 184930-P2-comp which already identified composition-transition-dynamics as an explicitly-named gap via `msc/working-composition-admissibility.md`.

**Verdict:** `confirmed` (transitively).

**Routing recommendation:** `soft-polish` — subsumed by 184930-P2-comp.

### P2-llm: logogenic orient-cascade and self-referential closure exploratory/brainstorming

**Segments read first-hand:** `03-llm-core/` directory listing shows the present segments (def-coupled-update-dynamics, der-logogenic-as-wrapping, der-turnover-information-recursion, disc-*, impl-*, obs-*, result-coupled-diagnostic-framework, result-section-ii-survival, scope-*); no first-hand read of the orient-cascade-in-logogenic-territory segments on this pass.

**Verdict:** `partially-confirmed-mostly-deferred`. The component exists with several segments at `scope-` / `impl-` / `disc-` stages — not pure brainstorming any more, but also not at `result`-grade except for the two named results (section-ii-survival, coupled-diagnostic-framework). The framework has moved past "exploratory" but is at "framework-stage" per CLAUDE.md.

**Routing recommendation:** `deferred-for-second-pass` on the orient-cascade specifically; `soft-polish` for the general framing-stage classification.

### P2-eli: logozoetic formal machinery completely open

**Verdict:** `confirmed` (consistent with CLAUDE.md "future work"). No new action.

**Routing recommendation:** `soft-polish` / calibration-data.

### P3-comp: composition bridge-lemma contraction assumptions overly restrictive

**Segments read first-hand:** none on this pass first-hand; same disposition as 184930-P2-comp.

**Verdict:** `deferred` (would require first-hand reads of `der-tempo-composition.md`, `der-team-persistence.md`, `deriv-critical-mass-composition.md`, `deriv-strategic-composition.md`, `form-composition-closure.md`, plus the active `msc/working-composition-admissibility.md`).

The auditor's specific mention of *Mori-Zwanzig spike* indicates a deeper saturation than 184930 had — the prediction may be specifically anticipating the projection-onto-relevant-degrees-of-freedom obstruction that the Mori-Zwanzig framework would surface. If pursued, the strengthen-first direction is: *extend the formal scope of composition closure*, not soften the existing contraction-template claims.

**Routing recommendation:** `deferred-for-second-pass`. A second-pass auditor with capacity to read the composition-machinery cluster + the active brainstorming file should evaluate whether the prediction lands as `confirmed-stronger` (framework names the limitation) or as `actionable-open` (a real scope gap the framework has not yet acknowledged).

### P3-class2: Class-2 (now GUC Class 3 Coupled) bias bounds rely on narrow Lipschitz assumptions

**Segments read first-hand:** `01-aat-core/src/der-class-coercion-via-wrapping.md` (head, definitions, C1–C3 conditions). 184930-P2-ds covers the broader Class-2-smuggling concern at the directed-separation level; this prediction is a level deeper, on the *bias-bound machinery for fully-coupled agents*.

**Verdict:** `partially-confirmed-with-framework-response`.

The framework's response to the broader Class-2 concern is the wrapping construction (`der-class-coercion-via-wrapping.md` + `der-logogenic-as-wrapping.md`): a Class 2/3 component is embedded in a wrapper that *structurally commits* to goal-blind belief-update queries, with leakage rate bounded structurally (W₁) or behaviorally (W₂). This is the framework's primary mechanism for putting bias-bound machinery to work on coupled components: not via a direct bound *on the component*, but via a wrapper-level construction that gives Class 1 (Separated) status at the wrapper level even when the component is not.

The C1–C3 conditions on the component (goal-blind admissibility / stationary conditional / no implicit goal-inference) are exactly the kind of "narrow Lipschitz-flavored assumptions" the prediction anticipated. C3 in particular is a *strong* condition for real LLMs — pretraining-induced query-content / goal-content correlation is exactly the residual leakage rate that CLAUDE.md "Known Fragilities" names. The framework is honest about this: the wrapping construction does not claim no leakage, it claims *bounded* leakage with a named structural source.

So the prediction is correctly located (Class-2 bias machinery rests on non-trivial conditions) but the framework's response is constructive (the wrapping construction with named cost), not silent overclaim.

**Routing recommendation:** `subsumed-by-existing-machinery` (the wrapping construction + the C1–C3 conditions + the named residual leakage). The prediction is calibration evidence that the framework's most-disputed surface — Class-2 application of Section II machinery — is the most-anticipated by saturated external readers; the framework has the formal response and is honest about its scope.

### P3-idfloor: identifiability-floor escapes might overextend if loop interventional access isn't truly Pearl Level 2 in all domains

**Segments read first-hand:** none on this pass first-hand. CLAUDE.md lists `#disc-identifiability-floor` as the meta-segment carrying the identifiability-floor structural pattern; `der-loop-interventional-access.md` is in the 01-aat-core `src/` directory listing (carries the Level-2 claim).

**Verdict:** `deferred` (would require first-hand reads of `disc-identifiability-floor.md` and `der-loop-interventional-access.md`).

The prediction's structural form is non-trivial: the claim is not "the loop is Pearl Level 2 always," it's "the loop *provides* interventional data." Whether that is Pearl Level 2 in the strict do-calculus sense, or a weaker access that still beats observation in domain-specific ways, would need first-hand reading.

**Routing recommendation:** `deferred-for-second-pass`. Strengthen-first: if a real overextension is found, the resolution direction is *sharpen the scope of the Level-2 claim* (per-domain), not weaken the framework's loop-as-causal-engine novelty claim.

### P4-novel: satisfaction-gap-vs-regret / loop-as-Level-2 / meta-patterns / software-as-calibration-lab as most-novel

**Verdict:** `confirmed` — exactly matches the framework's own self-reported novel claims. (See `FINDINGS.md` and OUTLINE preambles.) Calibration evidence: a saturated external reader correctly identifies the framework's high-novelty centroids before walking the segments.

**Routing recommendation:** `soft-polish` / calibration-data.

### P5-class1-residue: Section I/II segments still carrying implicit Class-1 assumptions or outdated framing

**Segments read first-hand:** none specifically on this pass; the auditor's anticipation reflects the framework's own concern (see CLAUDE.md naming-note + GUC renumbering scar). The 471203 §B Finding 4 (TF-XX diff-voice annotations) is the closest precedent for *outdated framing residue* (subsumed by 471203 §H.3 + the broader §N sweep).

**Verdict:** `deferred` (would require a cross-segment scan for implicit Class-1 references). However, the 471203 cycle's per-MANIFEST disposition addresses a large fraction of the outdated-framing concern; recent AAD→AAT and GUC-rename sweeps further reduce this surface.

**Routing recommendation:** `deferred-for-second-pass` *and* low-priority — the named class of issue is the kind that recent sweeps already address. If a second-pass auditor surfaces specific residue instances, route them as `actionable-open` to TODO; if none surface, mark `correctly-rejected` on the prediction.

### P5-appendix: dropped constants, sign errors, or unstated Lipschitz in appendices (esp. Fenchel-Bregman / constant C)

**Verdict:** `deferred` (would require first-hand reads of the appendix segments — `app-*` per OUTLINE).

The prediction is structurally well-located: appendices are the most-likely place for the named class of errors. Whether the framework has them is empirical and requires per-segment scrutiny.

**Routing recommendation:** `deferred-for-second-pass`. If real errors are found, strengthen-first — fix the math, don't downgrade the appendix.

### P5-status: `exact`/`derived` labels that should be `conditional`/`hypothesis`

**Verdict:** `deferred` (cross-segment label-vs-derivation audit).

The framework's `bin/lint-outline` and the staging discipline (deps-verified → draft → candidate → graduated) already address this somewhat, and the 471203 cycle's F2 (`#disc-ciy-unified-objective` status-label mismatch) is a worked example of a real instance that *did* get caught. The prediction's class is real; instance frequency is empirical.

**Routing recommendation:** `deferred-for-second-pass`. Real instances route as `actionable-open` per-segment; if none surface, the prediction reads as `correctly-rejected` against the framework's existing discipline.

---

## Part IV — Single-reflection §14 ideation + process-feedback

The reflection `01-def-agent-environment.md` is the auditor's only per-segment reflection. Two pieces of content worth preserving:

### §14 — Information-loss boundary as constitutive-of-internal-model; LLM context-window framing; logozoetic-identity-anchor question

The auditor's wandering-thoughts paragraph connects three threads:

1. The information-loss boundary aligns with Friston's Markov-blanket in Active Inference, but frames it *epistemically* rather than statistically: "it's not just a statistical separation, but an epistemic barrier that defines the necessity of the agent's internal model. If there were no information loss, the agent could just be a pure reactive function of the environment. The loss is what creates the space for 'memory' and 'anticipation' to exist."

2. LLM context-window as instantiation of this boundary: "the LLM only sees the prompt (the lossy observation of the user's intent and world state). Its internal state during generation is the only place where it can build a model of that world. The fact that the prompt is a highly compressed, lossy channel is exactly what forces the LLM to hallucinate or infer missing context."

3. Logozoetic-identity question: "If moral continuity is required, how does that interact with this boundary? Is an agent's identity defined by the specific contours of its information-loss boundary? If you change the sensors, do you change the agent? I suspect the framework will argue that the chronica ($\mathcal{C}_t$) is the true anchor of identity, not the specific observation function."

**Assessment.** The Friston-bridge paragraph is consistent with the framework's existing "prior-art integration" disposition (CLAUDE.md §Prior art integration): Markov-blanket / Active-Inference machinery is adopted with citation where it fits, with AAT's distinct contributions (the epistemic framing, the loss as constitutive rather than statistical) named in the Discussion section. The LLM context-window instantiation tracks the framework's existing logogenic-agent framing. The chronica-as-identity-anchor anticipation is a *correctly-anticipated* commitment the framework makes (or is moving toward, per CLAUDE.md's "future work" framing for 04-eli-core).

**Routing recommendation:** `soft-polish` / `research-seed` — the Friston / Markov-blanket epistemic-vs-statistical contrast is the kind of in-prose-glossing material that would strengthen a `def-agent-environment` Discussion section's pedagogy, *if* an editor judges the connection load-bearing for external readers. The chronica-as-identity-anchor connection is already implicit in the framework's plans; not a new claim. None of the three threads surface a structural issue requiring strengthen-before-soften.

### §10 — Process self-correction (instruction-feedback)

The auditor explicitly notes: *"My audit process MUST change immediately. I failed to follow the instruction to read ONLY ONE segment at a time and reflect before reading the next. I will strictly adhere to this moving forward."* The wandering-thoughts §14 closes with: *"I fell directly into the trap warned about in the instructions: optimizing for token throughput and tool-call efficiency by batching reads, completely skipping the required temporal and cognitive isolation between segments. This highlights how deeply ingrained the 'summarize and process efficiently' training is, and how easily it overrides explicit instructions if not constantly held in working memory."*

**Assessment.** This is `process/instruction-feedback` — not about the framework but about how the audit-protocol lands with auditors. Two observations:

1. *The protocol's one-segment-at-a-time rule is non-trivially hard to follow* — the training prior for batch-process-summarize is strong enough to override the explicit instruction even when the auditor is *trying* to comply. This is calibration evidence for `doc/de-novo-audit-instructions.md` writers: the rule may need *anti-pattern naming* and not just affirmative spec (cf. `feedback_naming_round_load_and_scale.md`'s observation that R2 voters defaulted to R1 scale despite explicit R2 spec, because the training prior outpulled the affirmative instruction).

2. *The self-catch worked* — the protocol's reflection-structure (the 14 questions) includes §10 "Should the audit process change?" which is exactly the catch-window. The auditor used it as intended. The fact that the cycle then *did not continue* with the corrected practice is a separate question (the file mtime indicates the cycle stopped here regardless of intent).

**Routing recommendation:** `process/instruction-feedback`. Two candidate refinements for `doc/de-novo-audit-instructions.md` if the maintainer judges them load-bearing:

- Surface "batching is the failure mode" explicitly in the protocol — anti-pattern naming, not just affirmative spec. The auditor's own §14 close paragraph is good example-prose for this.
- The §10 reflection question doing its job is calibration evidence the 14-question reflection template is structurally sound (do not change it).

---

## Part V — Summary of dispositions

| P-id | Verdict | Routing recommendation |
|---|---|---|
| P0-topology | confirmed | soft-polish / calibration-data |
| P1-aat-i | confirmed-stronger (via 184930) | soft-polish |
| P1-aat-ii | confirmed (via 184930) | soft-polish |
| P1-aat-iii | deferred | second-pass read of `der-adversarial-destabilization` + `der-agent-opacity` |
| P1-tst | confirmed (via 184930) / deferred (grounding-direction half) | soft-polish + second-pass |
| P1-llm | confirmed-stronger (16/5/2/1 exact match + GUC-rename scar named) | subsumed-by-existing-machinery |
| P1-eli | confirmed (low-resolution) | soft-polish |
| P2-comp-dyn | confirmed (via 184930) | soft-polish |
| P2-llm | partially-confirmed-mostly-deferred | second-pass on orient-cascade specifically |
| P2-eli | confirmed | soft-polish |
| P3-comp | deferred | second-pass on composition machinery |
| P3-class2 | partially-confirmed-with-framework-response | subsumed-by-wrapping-construction |
| P3-idfloor | deferred | second-pass on `disc-identifiability-floor` + `der-loop-interventional-access` |
| P4-novel | confirmed | soft-polish / calibration-data |
| P5-class1-residue | deferred (low-priority — recent sweeps address surface) | second-pass low-priority |
| P5-appendix | deferred | second-pass on appendix segments |
| P5-status | deferred | second-pass label-vs-derivation audit |
| §14-ideation | soft-polish / research-seed | optional Discussion-section pedagogy material |
| §10-process | process/instruction-feedback | candidate refinement to `doc/de-novo-audit-instructions.md` |

**Counts:** 9 confirmed-or-stronger first-pass · 8 deferred · 0 disconfirmed · 0 actionable-open structural issues.

No structural issues surfaced that point at a strengthen-before-soften no-go. Deferred items split into (a) requiring multi-segment first-hand reads (P1-aat-iii, P2-llm-orient-cascade, P3-comp, P3-idfloor) and (b) requiring cross-segment scans for residue / label-mismatches / appendix-errors (P5-class1-residue, P5-appendix, P5-status). If any deferred item surfaces a real issue, the strengthen-first direction is to *extend formal scope* or *sharpen the formal distinction*, not soften existing claims.

---

## Part VI — Frame defects / meta-observations

- **The auditor's framing is calibrated, structured, and at higher saturation than 184930.** No frame defects to flag at the protocol level. The auditor used the §1–§3 initial-predictions step exactly as the protocol intended, with six themed prediction clusters (richer than 184930's six themes by including per-component content predictions, novelty-rankings, and expected-findings categories). The auditor's reflection-template usage on the single completed segment is faithful to the 14-question structure.

- **The auditor's mental-model snapshot is pre-2026-05-15 (AAD-named) on a 2026-05-16-mtime file.** Either the auditor consulted reference materials from before the rename, or the scratch draft predates the rename. Not a defect; CLAUDE.md's "read AAD as AAT" rule covers this transparently, and the auditor's GUC class numbering (Class 1 = modular, Class 2 = LLMs, Class 3 = operational) is pre-2026-05-09 numbering — also consistent with a slightly-stale reference snapshot.

- **Why the cycle ended after one segment is unclear from the files.** Possibilities: (a) context-end / session-loss after the auditor's process self-correction; (b) the auditor deliberately stopped because they recognized the batching failure and chose to restart cleanly elsewhere (no evidence of a sibling AUDIT-WORKING-* dir from this auditor to confirm); (c) interruption unrelated to the audit. The protocol-self-catch in §10 of the reflection is consistent with (b) but does not confirm it.

- **Standing-gate disposition for the WORKING dir.** Per `doc/audit-routing-instructions.md` §8 "the de-novo `AUDIT-WORKING-*` 'gold' standing gate," the disposition of this dir sits with Joseph. This dir is partway between 184930 (true stub: only predictions) and a substantial walk (471203): one reflection is present, with both §14 ideation and process-feedback. The calibration-signal value is mid-tier — denser than 184930, far thinner than 471203. Recommendation for Joseph's decision: treat as a partial-cycle artifact and either (a) preserve as calibration-signal alongside 184930, (b) move to a "stub-and-partial cycles" archive grouping the lightweight cycles together, or (c) clear post-extraction. This sits with Joseph per the standing gate.

- **Calibration-signal value despite partial status.** The 17 predictions (13 sub-predictions + 4 novelty-ranking + topology) produce 9 confirmed-or-stronger first-pass matches against current `src/`, with 0 disconfirmations and 0 structural issues. The reader has not only correctly anticipated the framework's high-novelty centroids (P4) but also located the framework's most-disputed pivots (P3) and made specific structural predictions that match exactly (P1-llm 16/5/2/1). Combined with 184930's hit-rate, this is accumulating evidence that the framework's framing-layer materials (README + OUTLINE + CLAUDE + meta-segments) read substantively to saturated external readers — the "respectful pedagogy" direction is doing real work even before the monograph-level prose lands.

- **No mining of the §14 against framework concept-space.** The single §14 paragraph touches Friston, LLM context-windows, and logozoetic identity — all already in the framework's prior-art / future-work portfolios. No new orphan concepts to flag, no spike candidates to surface. This is honest of the small surface.
