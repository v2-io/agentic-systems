---
source_cycle: 184930 (de-novo, auditor unknown; cycle ended at initial-predictions stage)
extraction_agent: Claude Opus 4.7 (1M context), parallel-sweep slice
extraction_date: 2026-05-20
working_dir: audits/AUDIT-WORKING-184930/ (1 file, 17 lines)
final_of_record: none — auditor wrote initial predictions and did not proceed to segment walk
status_kind: stub auditor cycle
purpose: |
  Extract the predictions register from the single-file working dir for routing
  through the standard audit-routing process. Because no segment walk happened,
  the predictions themselves are the gold — they are the calibration signal of
  what an external de-novo reader anticipated about the framework before
  opening any segment. Treated as implicit findings: each prediction is
  scrutinized first-pass against current `src/` for the segments it names.
---

# Audit-findings extract — 184930 working-dir mining

## Provenance and scope

The 184930 cycle is a **stub auditor cycle**: the WORKING dir contains exactly one file, `00-initial-predictions.md` (17 lines), with no per-segment reflections, no §14 wandering thoughts, no FINAL deliverable. The auditor wrote the §1–§3 protocol-mandated initial predictions (per `doc/de-novo-audit-instructions.md`) and the cycle ended there — apparently before any segment walk. No date is determinable from the file contents; the dir's six-digit ID is the only identifier.

What this dir contributes, despite the small surface, is non-trivial: the predictions register is itself a calibration signal — what does an external de-novo reader, given only README + OUTLINE + reference definitions, anticipate about the framework? Six themed predictions, ~7 sub-predictions, all falsifiable against current `src/`. This file extracts them as implicit findings and applies first-pass scrutiny.

---

## Part I — Predictions register (preserved verbatim, attributed)

The predictions, transcribed under the auditor's six headings. Each is given a P-id for cross-reference in Part II's scrutiny.

### Theme 1 — The math: forced vs. chosen

- **P1-forced.** "Section I (Adaptive Systems) appears to rely on solid control theory (Lyapunov stability, monotone operators) and basic information theory (Shannon entropy, predictive compression). The persistence condition ($\alpha > \rho/R$) will likely be a forced mathematical necessity derived directly from standard Lyapunov bounds under bounded disturbance."

- **P1-chosen.** "Section II's (Actuated Adaptation) formalization of strategy as a probabilistic causal DAG seems to be a strong representational choice (a formulation) rather than a mathematical inevitability. I expect the 'single-parameter edges' ($p_{ij}$) and the handling of the OR/AND logic to be elegant but ultimately a chosen approximation, not forced by fundamental physics."

### Theme 2 — Sleight-of-hand / overclaim potential

- **P2-ds.** "Directed Separation: the 'directed separation' concept (that epistemic update is goal-blind) is noted as holding 'by construction' for Class 1 agents. The theory acknowledges this fails for Class 2 (e.g., LLMs). However, I suspect that the boundary might be fuzzier in practice, and the application of Section II results to learning agents could inadvertently smuggle in Class 2 coupling under a Class 1 guise."

- **P2-ib.** "Information Bottleneck in Purposeful Agents: the application of the Information Bottleneck principle to non-epistemic state (e.g., shared intent in Section III or strategy DAGs in Section II) might stretch the standard IB bounds. I expect the formalization of 'deliberation cost' to potentially conflate information-theoretic processing time with wall-clock time in ways that aren't strictly mathematically isomorphic."

- **P2-comp.** "Composition Admissibility: Section III relies on 'contraction templates' and 'composition closure.' Given that the framework notes composition transition dynamics are an open gap, I predict the existing composition results rely on heavily constrained symmetric or cooperative assumptions that may not generalize robustly."

### Theme 3 — Software as a calibration lab

- **P3-tst.** "Temporal Software Theory (TST) using Git as literal interventional data is conceptually brilliant. However, I predict that mapping code changes (actions) to causal interventions ($do(a)$) might oversimplify the latent unobservable states in software development (e.g., developer mental models and off-band communication)."

### Overall closing prediction

- **P4-overall.** "Overall, the separation of epistemic strength (`exact` vs `heuristic` vs `discussion`) looks highly disciplined. I expect the core to be genuinely solid, but the transitional bridging — from mismatch ODEs to strategy DAGs — to be where the most scrutiny is needed."

---

## Part II — Calibration signal: what these predictions tell us about external first-encounter

Stepping back from per-prediction scrutiny: as a corpus, the predictions reveal an external reader's pre-segment-walk model of the framework. This is the kind of priming-window calibration data the audit protocol was designed to surface, and it is worth preserving as such *independent* of whether each prediction checks out:

- The reader correctly identified the **section-I / section-II forced-vs-chosen split** as the framework's main aesthetic seam. This matches the framework's own self-conception (Section I substantially derived; Section II formulation-heavy at the strategy-DAG layer).
- The reader correctly anticipated **directed separation as a structural seam where Class 2 / LLM material would create stress** — and correctly anticipated this would be flagged in the framework's own scope statements. This is the standard external-reader hit on the framework's most-disputed pivot.
- The reader's **IB-extending-beyond-epistemic-state** concern names a genuine extension surface (the survival-imperative IB / matrix-CIY upgrade applies IB machinery to action-conditional Fisher Information, not standard epistemic encoding) — but read against the framework's own treatment, the extension is constructively handled, not a sleight-of-hand. The prediction has correctly located a friction point, and the framework's response is substantive.
- The reader's **TST-git latent-state concern (C3 developer mental models)** maps *exactly* onto a confounder class the framework names verbatim — strong external-prior-meets-internal-honesty match. This particular prediction is a "match" not a "miss" because the framework demoted the claim from derived to discussion-grade for precisely this reason.
- The closing **"transitional bridging from mismatch ODEs to strategy DAGs is where scrutiny is needed"** observation is on-target: the bridge segments (`der-gain-sector-bridge`, `der-directed-separation`, the §II opening sequence) are repeatedly named in audit cycles as the load-bearing pivots. The 471203 pilot's "high-water marks" include exactly the gain-sector bridge.

**Net signal:** the framework is *legible* to a sympathetic external reader at the README+OUTLINE level — predictions track to actual segments and the framework's own self-conception more than they miss. The gaps that *do* exist (P2-ib processing-time vs wall-clock, P2-comp composition-admissibility scope, P4-overall mismatch-to-DAG transitional bridging) are gaps the framework already names internally. This is calibration evidence for the README-/OUTLINE-level framing-quality direction in CLAUDE.md's "respectful pedagogy" posture.

---

## Part III — First-pass scrutiny against current `src/`

Per-prediction verdict + segments read first-hand. First-pass is flag-for-routing, not graduation-grade; the §8 independent-verify gate fires downstream.

### P1-forced: persistence condition as Lyapunov necessity

**Segments read first-hand:** `01-aat-core/src/deriv-sector-condition.md` (head).

**Verdict:** `confirmed-stronger`.

The framework does derive persistence via Lyapunov, but under the **sector condition** — a *strictly more general* set of assumptions than the linear-ODE prediction. The motivation section names the move explicitly: *"A Lyapunov approach proves persistence and stability under much weaker assumptions: any correction dynamics satisfying qualitative monotonicity properties (the sector condition). The results below are strictly more general — the linear case is recovered where the sector bounds coincide."* The prediction anticipated linear-Lyapunov; the framework delivers nonlinear-Lyapunov-via-sector with the linear case as a recovery. Stronger than predicted, in the direction the framework's epistemic discipline would predict (strengthen-before-soften shaping the derivation register).

**Routing recommendation:** `soft-polish` / calibration-data — no action needed, but the strength-beyond-prediction is worth carrying as evidence the framework's framing-level material is doing what it claims at the substance level. Material for any future "external-reader calibration" pass.

### P1-chosen: strategy DAG as formulation choice with AND/OR single-parameter edges

**Segments read first-hand:** `01-aat-core/src/def-strategy-dag.md` (head + intro paragraphs).

**Verdict:** `confirmed` (with calibration refinement).

The framework explicitly carves the prediction's exact distinction: *"the DAG structure is not a modeling convenience but a consequence of operational requirements on any causally-reasoning bounded agent — at the level of sufficiency, not yet necessity. `#deriv-graph-structure-uniqueness` proves that directed temporal order plus probabilistic uncertainty plus causal sufficiency *suffice* for a DAG-with-Markov-factorization representation … What remains a formulation choice is the *parameterization within* the DAG structure: AND/OR combination with single-parameter edges is the AAT choice, motivated by parsimony and convergence across three independent formalism attempts, but alternative parameterizations (within the derived graphical structure) are legitimate research directions."*

The reader predicted the AND/OR + single-parameter as chosen; the framework says *graph structure is derived* (one level further down than the prediction located the chosen/forced boundary) *and the AND/OR parameterization is chosen*. The reader's prediction is correct about the parameterization layer, slightly off about where the chosen-vs-forced seam sits — the seam is one level deeper.

**Routing recommendation:** `soft-polish` — material for a framing-level "what's forced vs chosen" note in any future OUTLINE preamble or README expansion. The framework already has this content distributed across `def-strategy-dag.md` and `deriv-graph-structure-uniqueness`; surfacing it at the framing layer would close the gap this external reader's prediction located.

### P2-ds: directed separation boundary fuzziness; §II results smuggling Class 2 coupling

**Segments read first-hand:** `01-aat-core/src/der-directed-separation.md` (head); CLAUDE.md (Known Fragilities + GUC renaming note).

**Verdict:** `confirmed-stronger` (the concern is real, named, and resolved constructively).

The framework names this concern *verbatim* in the "Known Fragilities" section of CLAUDE.md: *"Directed separation violated by goal-conditioned agents at the component level (LLMs, GUC Class 3: Coupled) — addressed constructively via the wrapping construction (`#der-class-coercion-via-wrapping` and its logogenic specialization `#der-logogenic-as-wrapping`), which gives GUC Class 1 (Separated) status at the wrapper level by structural commitment of goal-blind belief-update queries, with leakage rate bounded structurally (W₁) or behaviorally (W₂)."*

The auditor's "smuggling Class 2 under Class 1 guise" prediction is exactly the failure mode the wrapping construction is engineered to prevent: the wrapper *structurally commits* to goal-blind belief-update queries, so the smuggling can no longer happen silently — any residual leakage is bounded by W₁ (structural) or W₂ (behavioral) and is *named* rather than hidden. The framework didn't just acknowledge the concern; it built the formal response. Note also the GUC class renumbering (2026-05-09): the auditor's "Class 2 = LLMs" maps to current GUC Class 3 (Coupled), per the CLAUDE.md table.

**Routing recommendation:** `soft-polish` / `subsumed-by-existing-machinery` — the wrapping construction is the disposition. Worth recording as external-reader-prediction calibration data: the framework's most-disputed pivot is the most-anticipated by external readers, and the framework has the formal response ready. No new routing action.

### P2-ib: IB stretched beyond epistemic state; deliberation-cost conflating processing time with wall-clock

**Segments read first-hand:** `01-aat-core/src/deriv-causal-ib-lmi.md` (head). Did not read `der-deliberation-cost.md` first-hand.

**Verdict:** `deferred` (partial first-pass; deeper read needed).

The auditor's prediction has two parts. **Part A (IB stretched):** the framework does extend IB machinery to action-conditional Fisher Information via the LMI form (`deriv-causal-ib-lmi.md`) — this *is* a non-standard application of IB (the action-conditional FIM as "matrix CIY" replacing scalar IB shadow-prices). The segment is honest about the move: it cites the "blank wall attack" the scalar form admits, and lifts to LMI to address it. Whether this constitutes "stretching IB bounds" in the sense the auditor anticipated would need a fuller read of the IB-bridging chain (`form-information-bottleneck` → `deriv-causal-ib-exploration` → `deriv-causal-ib-lmi`).

**Part B (deliberation-cost wall-clock conflation):** not directly verified first-hand. Would require reading `der-deliberation-cost.md` and tracing whether the cost-formalization keeps information-theoretic and wall-clock quantities clean.

**Routing recommendation:** `deferred-for-second-pass`. If the segment chain checks out, downgrade to `confirmed-with-framework-response`. If a real conflation is found in `der-deliberation-cost.md`, it is `actionable-open` — a candidate finding in its own right. Strengthen-first: any conflation found should be resolved by tightening the formal distinction, not by softening the deliberation-cost claim.

### P2-comp: composition results rely on symmetric/cooperative assumptions

**Segments read first-hand:** none of the composition segments first-hand on this pass; relied on CLAUDE.md's "Known Fragilities" summary and PROPOSALS pointers.

**Verdict:** `deferred` (would require reading `der-tempo-composition`, `der-team-persistence`, `deriv-critical-mass-composition`, `deriv-strategic-composition`, plus the open-composition-transition-dynamics treatment in `working-composition-admissibility.md`).

The auditor's prediction has two layers. **Layer 1:** existing composition results rely on heavily constrained assumptions — likely confirmed at a high level, because CLAUDE.md explicitly notes "composition transition dynamics are an open gap" and `msc/working-composition-admissibility.md` is named as active brainstorming. The prediction is correctly located; the framework names the gap. **Layer 2:** the constraint is specifically *symmetric or cooperative* — not verified first-hand. The composition machinery does include adversarial treatment (`der-adversarial-destabilization`, `der-agent-opacity`), which suggests the prediction's specific "symmetric/cooperative" framing may be incomplete.

**Routing recommendation:** `deferred-for-second-pass`. Honest deferral: a thorough check would require reading 5+ segments and the active brainstorming file. The prediction is *probably* correct at Layer 1 and *probably* miscalibrated at Layer 2. Strengthen-first: any composition-scope gaps surfaced by a deeper read should be addressed by extending the formal scope, not by softening the existing results.

### P3-tst: git-as-do(a) oversimplifies latent states (developer mental models, off-band communication)

**Segments read first-hand:** `02-tst-core/src/hyp-causal-discovery-from-git.md` (full read).

**Verdict:** `confirmed-stronger` (the framework names the predicted confounder verbatim).

The segment lists three confounder classes, the third of which is *exactly* the auditor's prediction: *"**C3. Developer knowledge state.** An experienced developer may change $A$ and $B$ together because they *know* (from their $M_t$) that both need updating, not because changing $A$ caused them to discover the need to change $B$. The co-change reflects the developer's causal model, not a causal process observed in the data. This is a selection effect: the developer's choice of what to include in a commit is conditioned on their private causal model, which is unobserved."*

Additionally: C1 (shared requirements) and C2 (convention-driven bundling) cover the "off-band communication" half of the prediction. The framework explicitly demotes the causal-discovery claim from derived to discussion-grade *for this reason*: *"the chain from git data to AAT quantities is entirely empirical … Max attainable: *empirical*. Even with perfect confounding adjustment and unlimited data, the claim that git-derived causal structure matches AAT's formal quantities would remain an empirical finding, not a derivation."* This is honest scope-narrowing operating exactly as the auditor's closing prediction (P4-overall) anticipated.

**Routing recommendation:** `subsumed-by-existing-machinery` / `soft-polish` — the framework's response is the C1/C2/C3 confounder taxonomy + the explicit "Max attainable: *empirical*" cap. Worth recording as an exemplar of the framework's epistemic discipline working as designed: a plausible derived claim is honestly demoted to hypothesis-grade for stated reasons that the external reader independently anticipated. Material for any future "scope-honesty operating in practice" framing-level case study.

### P4-overall: epistemic-tier discipline + mismatch-ODE → strategy-DAG transitional bridging as scrutiny site

**Segments touched indirectly via P1, P2-ds spot-checks.**

**Verdict:** `confirmed`.

The prediction has two parts. **Part A (epistemic discipline is real and disciplined):** confirmed by the spot-checks in P1-forced, P1-chosen, P3-tst — segment-level Epistemic Status sections cleanly distinguish exact / conditional / discussion / hypothesis tiers, and the C3-confounder-driven demotion in P3-tst is a worked example of the discipline operating. **Part B (mismatch-ODE → strategy-DAG bridging is the scrutiny site):** consistent with prior audit cycles. The 471203 pilot's per-segment trail (the gain-sector bridge as a "high-water mark," the `der-directed-separation` scope-condition discipline, the `def-strategy-dag` four-postulate stack) all sit at exactly this bridging seam. The reader has correctly located where the framework's load-bearing transitional work happens.

**Routing recommendation:** `soft-polish` / framing-material — the prediction's accurate location of the bridging seam is itself calibration evidence. The framework's existing `disc-*` meta-segments (`disc-identifiability-floor`, `disc-separability-pattern`, `disc-additive-coordinate-forcing`) and the planned M4 modularity-state-dynamics segment are the architectural answer to "where does the bridging happen, and how do we surface its discipline?" — this prediction is implicit endorsement that the meta-segments are positioned where an external reader expects scrutiny.

---

## Part IV — Summary of dispositions

| P-id | Verdict | Routing recommendation |
|---|---|---|
| P1-forced | confirmed-stronger | soft-polish / calibration-data |
| P1-chosen | confirmed | soft-polish (framing-layer surfacing) |
| P2-ds | confirmed-stronger | subsumed-by-wrapping-construction |
| P2-ib | deferred | second-pass read of IB-bridge chain + deliberation-cost |
| P2-comp | deferred | second-pass read of composition machinery + working-composition-admissibility |
| P3-tst | confirmed-stronger | subsumed-by-C3-confounder-treatment |
| P4-overall | confirmed | soft-polish / framing-material |

**Counts:** 4 confirmed-or-stronger first-pass · 2 deferred · 0 disconfirmed · 0 confirmed-weaker.

No structural issues surfaced that would point at a strengthen-before-soften no-go. The two deferred predictions are both at the "needs multi-segment read" tier; if pursued, the framework's response should be evaluated under strengthen-first (extend scope / sharpen formal distinction) rather than soften (downgrade claims).

---

## Part V — Frame defects / meta-observations

- **The auditor's framing is calibrated and respectful.** No frame defects to flag at the protocol level. The auditor used the §1–§3 initial-predictions step exactly as the protocol intended (genuinely falsifiable predictions, organized by themes, with closing meta-prediction about where scrutiny matters most).

- **Why the cycle ended is unclear.** No indication in the file of what happened after the predictions were written. Could be a context-end / session-loss, a switch to a different audit cycle, an auditor handoff. Worth recording so the AUDIT-WORKING dir's standing-gate disposition (per `doc/audit-routing-instructions.md` §8) can be decided with Joseph: this dir is *not* a "served-purpose working dir" in the sense that section uses — there is no served purpose to begin with, because no walk happened. The decision about whether to (a) keep as a calibration-signal artifact, (b) consolidate into a "stub-cycles" archive, (c) clear after extraction, sits with Joseph per the standing gate.

- **Calibration-signal value despite stub status.** The 7 predictions in this single file produce 4 confirmed-or-stronger matches against current `src/` — a higher hit-rate than would be expected from pure structural-shape inference. The framework is legible to external de-novo readers at the README+OUTLINE level in a way that predicts substance. This is the kind of evidence that the "respectful pedagogy" direction (CLAUDE.md) is already partially landing — and it suggests the framing-layer materials (README, OUTLINE preambles, `disc-*` meta-segments) are doing real work for external comprehension, not just internal organization.

- **No §14 wandering-thoughts, no per-segment trail.** This dir lacks the cognition-trace gold that 471203 and other longer-walked dirs carry. The extraction is therefore narrower than other slices will be; that is honest, not a failure of this slice.
