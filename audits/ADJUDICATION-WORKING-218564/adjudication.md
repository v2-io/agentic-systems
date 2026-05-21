---
adjudicator: Claude Opus 4.7 (1M context), pilot adjudication
adjudication_date: 2026-05-20
target: audits/audit-findings-471203.md (extracted 2026-05-20 from AUDIT-WORKING-471203/)
brief_source: parent agent, 2026-05-20 (pilot of the audit-findings adjudication fan-out)
ground_truth_substrate:
  - audits/.integrated/audit-471203-FINAL-2026-04-28.md
  - audits/.integrated/audit-471203-SUPPLEMENT-phase-2.md
  - audits/.integrated/MANIFEST.md "2026-05-15 — audit-471203 de-novo cycle"
routing_protocol: doc/audit-routing-instructions.md §8
posture: |
  Independent-verify pass on the extraction agent's first-pass scrutiny. Parent (Joseph) primary-source-spot-checks before any durable writes; this file recommends, does not land. No file moves, no canon edits, no MANIFEST writes, no ledger writes, no commits.
---

# Adjudication — `audits/audit-findings-471203.md`

## Provenance and frame

This is the **pilot adjudication** of the audit-findings extraction cycle (commit `07aaeff`, 2026-05-20). The extraction itself was the deepest of the 14 produced — 5-part / ~470 lines / ~25–30k tokens — over the substantively-rich 471203 de-novo audit's WORKING dir (44 files, ~3900 lines, ~22 per-segment reflections, two cross-cutting documents). The extraction agent's First-Pass Scrutiny did light verification of the Part I+II `subsumed-by-FINAL` claims and honestly deferred most Fresh-item `src/`-state verification.

My role per §8 independent-verify: adjudicator $\ne$ grad-confirmer. Parent does the durable primary-source spot-checks; I produce the disposition recommendations and surface the convergences worth carrying through to the fan-out brief.

**What I verified first-hand from current `src/` (independent of the extraction's verification):**

- `01-aat-core/src/disc-ciy-unified-objective.md:44, 50` (Findings F1+F2 fixes — both confirmed)
- `01-aat-core/src/def-action-transition.md` (F3 fix — confirmed via grep of "Markov-of-$\Omega$ as a modeling commitment")
- `01-aat-core/src/disc-identifiability-floor.md` (Instance count + Fano relevance — *4 instances* with Instance-4 KNOWN-DEFECTIVE in flight; 4 named adjacent open floors; no Fano-of-observer-prediction instance)
- `01-aat-core/src/der-agent-opacity.md:43, 44, 59, 80, 86, 98, 113, 157` (16-cell sub-scope-$\alpha$ restriction — *already stated* at multiple loci including the Known-Limitations row at `:157`)
- `01-aat-core/src/der-adversarial-destabilization.md:67` (effects-spiral *still discussion-grade*; $\gamma_A(\lVert\delta_B\rVert)$ functional form named as open)
- `01-aat-core/src/der-observability-dominance.md:39, 53, 57` (absorbing-state + observability-investment-tradeoff *already named with quantitative content*)
- `01-aat-core/src/def-pearl-causal-hierarchy.md` (no explicit "model-conditioned vs true-SCM" clarification in body; the `:41` "recapitulation of external result" framing partially covers it but does not foreground it)
- `01-aat-core/src/def-value-object.md:41, 47, 99, 103` (C1/C2/C3 convention propagation — *the convention is part of the measurement* clause is in place at `:103`; whether downstream segments specify their convention was not exhaustively checked)
- `01-aat-core/src/der-directed-separation.md:69, 77, 79, 81, 96, 120, 146, 148, 150` ($\kappa_{\text{processing}}$ distribution-dependence — *fully resolved* with the "Distribution dependence" paragraph at `:77` and Class-2 explicit treatment)
- `03-llm-core/src/disc-m-preservation.md:32, 76, 80, 84, 86, 110` (accumulation problem — *resolved by strengthening*; affine information recursion in `der-turnover-information-recursion`; the prior additive break-even claim **was deleted and replaced**, with the history line at `:110` a worked instance of integration-is-replacement)
- `FORMAT.md` + `FORMAT-TODO.md:182` (Pearl-`do` standard-notation exemption — *recorded under C12 explicitly naming 471203 §B F6*)
- `audits/.integrated/MANIFEST.md` 471203 section (full)
- `audits/.integrated/audit-471203-FINAL-2026-04-28.md` (full)
- `audits/.integrated/audit-471203-SUPPLEMENT-phase-2.md` (full)
- `audits/polish-and-sentiment-ledger.md` (full)
- `doc/audit-routing-instructions.md` (full)
- `03-llm-core/src/` + `04-eli-core/src/` directory listings (segment counts)

**What I deferred:** exhaustive cross-segment $\delta_{\text{sat}}$ / $\delta_{\text{regret}}$ convention-specification audit (Fresh-9 still tooling-gap verification); Brief-field state across all impacted segments (Fresh-6 / Fresh-7); detailed PROPOSALS SP-23 and SP-12 §D.4 reading (MANIFEST disposition accepted); 04-eli-core README v current state (TODO:386 disposition accepted).

---

## Independent-verify outcomes — what the spot-checks change

Three of the extraction's "deferred / unknown current state" Fresh items are now **resolved by strengthening** in current `src/`, which materially changes their adjudication. Two more partially resolve. The rest propagate honestly. The current `src/` is *substantially ahead* of the 2026-04-28 audit snapshot the extraction was working from — the project shipped meaningful strengthenings between then and now.

| Fresh-N | Extraction's "deferred" disposition | What current `src/` shows | Adjudication |
|---|---|---|---|
| Fresh-2 (absorbing-state observability-investment economics) | research-seed; "would need a spike" | `der-observability-dominance.md:53` carries an explicit "observability investment tradeoff" paragraph with the closed-form: improvement is positive whenever $\theta_1 \gt 1/2$ — quantitative escape content present | **partially-resolved-by-strengthening**; the strengthening direction the extraction proposed (derive quantitative escape conditions) has *substantially landed*. Residual: a free-standing "economics of observability investment" appendix (when does instrumenting pay off given cost?) remains open as `research-seed`. |
| Fresh-3 (16-cell scope-$\alpha$ restriction not surfaced) | actionable-open: "add a sub-scope $\alpha$ condition to the 16-cell closure framing" | `der-agent-opacity.md:157` Known-Limitations row reads verbatim: *"The 16-cell emitter-recipient composition admits closed-form arg-max only under sub-scope $\alpha$ coupling; general non-convex coupling requires per-case optimization."* Plus 4 other in-prose mentions (`:43, 44, 80, 113`) and an Open-questions row at `:86` | **resolved**; the scope condition is canonical in the segment. Close. |
| Fresh-5 (Fano 4th identifiability-floor instance) | research-seed; "Did not check whether a 4th instance has since landed" | `disc-identifiability-floor.md` has *Instance 4 — Universal Information-to-Distance Constant under Non-(PI) Norms* + **four** adjacent open floors (Causal-IB Extension; Misspecification-Cost; Tier-Switching Policy; Mechanism-Design Impossibility from `#deriv-strategic-composition`). Instance 4 is KNOWN-DEFECTIVE-in-flight (Joseph-reserved disposition gated on Object-B verification per `spikes/spike-identifiability-floor-instance4-resolution-2026-05-18.md`) | **superseded-by-later-work** *for the count-the-instances framing*; the meta-segment now has *more* candidate instances than the extraction proposed (4 named + 4 adjacent open). The extraction's proposed Fano-on-observer-prediction is *not* one of them; it would be a candidate 5th adjacent floor if pursued. Hold as `research-seed` against the adjacent-floors slot, with low priority since 4 candidates are already there. |
| Fresh-9 (C1/C2/C3 convention propagation check) | actionable-open; "Did not run the cross-segment check" | `def-value-object.md:103` carries the explicit "convention is part of the measurement" warning + canonical-default declaration at `:43` + per-convention diagnostic-table at `:95`–`:99` | **partially-resolved**; the *source-of-truth* segment is now self-disciplined. The propagation check across downstream segments (does every use of $\delta_{\text{sat}}$ / $\delta_{\text{regret}}$ name its convention?) remains as `actionable-open` (tooling-gap). |
| Fresh-13 (accumulation problem formalization) | research-seed / `architectural`; "Did not verify state of `disc-m-preservation`. **Strongly recommend Joseph flag as priority**" | `disc-m-preservation.md:76, 80, 84, 86, 110` show the accumulation question is *resolved by strengthening* via `der-turnover-information-recursion`'s affine information recursion $I_{k+1} \leq \eta_k I_k + a_k$. The earlier additive break-even claim ($\mathbb{E}[\Delta\epsilon_k] \leq \mathbb{E}[\Delta I_k]$) **was deliberately deleted** and the segment `:110` records this as integration-is-replacement (history line: *"this section previously carried a discussion-grade additive accumulation … that presumed the wrong (additive) operator … and was deleted and replaced when the contraction–reinjection no-go landed, 2026-05-19"*). The identity-continuity parallel is in `der-identity-continuity-threshold` | **resolved-by-strengthening** (and pedagogically: this is the same `integration-is-replacement` pattern as the Model-S 2026-05-16 cycle — a refuted claim deleted, the strengthening landed). The substrate-independence quantitative formulation the extraction flagged as substantively-priority is now in canon. Close cleanly. |
| Fresh-16 ($\kappa_{\text{processing}}$ distribution-dependence propagation) | actionable-open (verification / tooling-gap); "One-off audit work" | `der-directed-separation.md:77` carries an explicit "Distribution dependence" paragraph naming the classification-vs-operationalization split, plus Class-2 (Partial) variability treatment | **resolved at the source-of-truth segment**; the distinction is canonical there. The propagation check (does every downstream use of $\kappa$ acknowledge the distribution-conditioning?) remains a one-pass tooling check — `actionable-open` (low priority). |
| Fresh-6 (Pearl-`do` FORMAT-policy via FORMAT-TODO C12) | (extraction labeled it as part of F1-cluster) | `FORMAT-TODO.md:182` explicitly names *"audit-471203 §B Finding 6 ≡ audit-742613 FINAL:254, routed here 2026-05-15"* — exact disposition match | **subsumed-by-FINAL** confirmed; FORMAT-TODO C12 is the live home. |

The pattern: between 2026-04-28 (audit FINAL) and 2026-05-20 (this adjudication), the project shipped at least four of the extraction's deferred strengthening directions — observability-investment (partial), 16-cell scope-$\alpha$ (full), accumulation problem (full strengthen + integration-is-replacement landing), $\kappa$-distribution-dependence (full at the source segment). This is *exactly* what strengthen-before-soften produces over time; the extraction's deferral was honest, and the parent's session-cadence between audit and adjudication closed several of them.

---

## Part I — Findings already adjudicated (FINAL §B + MANIFEST)

The extraction agent's First-Pass Scrutiny confirmed all seven Part I findings via first-hand re-read of the `src/` fix-loci. I independently re-verified the four most-consequential (F1, F2, F3, F4) and accept the extraction's verification of F5–F7 (where MANIFEST is the truth-arbiter and the routing decision is the actionable content, not the segment state). No divergences from the extraction's call.

| Trail-ID | Disposition (this adjudication) | Verification | Routing target |
|---|---|---|---|
| F1-trail (stale `#deriv-directional-survival-exploration` xref) | `subsumed-by-FINAL — resolved` | independently re-verified `disc-ciy-unified-objective.md:44` cites `#deriv-causal-ib-lmi`; `deriv-directional-survival-exploration.md` absent from `src/` | none — graduated 2026-05-15 |
| F2-trail (`disc-ciy-unified-objective` status-label) | `subsumed-by-FINAL — resolved` (layered-status rewrite) | independently re-verified at `:44, 50` (verbatim match to SUPPLEMENT §H.1) | none — graduated 2026-05-15 |
| F3-trail (implicit-Markov-of-$\Omega$) | `subsumed-by-FINAL — resolved` | independently re-verified `def-action-transition.md` Discussion carries the "Markov-of-$\Omega$ as a modeling commitment" paragraph | none — graduated 2026-05-15 |
| F4-trail (TF-XX diff-voice) | `subsumed-by-FINAL — resolved` (49-file §N broader sweep) | the SUPPLEMENT §N.2 verification table is itself parent-verified per MANIFEST; the cleanup is comprehensive | none — graduated 2026-05-15 |
| F5-trail (`post-composition-consistency` depends) | `subsumed-by-FINAL — already routed` | MANIFEST: PROPOSALS SP-6 + TODO:149 + F-A cluster (584721/742613) | none — already triple-tracked via the F-A cluster |
| F6-trail (Pearl-`do` in `scope-agency`) | `subsumed-by-FINAL — duplicate ≡ 742613:254` | independently re-verified `FORMAT-TODO.md:182` records the disposition with explicit 471203-§B-F6 attribution | none — FORMAT-TODO C12 is the live home |
| F7-trail (Tishby-Zaslavsky citation) | `subsumed-by-SUPPLEMENT §L — resolved by strengthening` | the extraction verified `form-information-bottleneck.md:50` first-hand; option-(b) landed | none — graduated 2026-05-15 |

**Convergence note:** Three of the seven (F1, F4, F6) are "already-known-in-flight" patterns also surfaced in 584721 / 613842 / 742613 / 829314. Per the brief's item-4 convergence-as-evidence principle, this is the **doc-rot / voice-discipline / depends-graph hygiene** convergent cohort — not a fresh adjudication per cycle. The MANIFEST already deduplicates these correctly; no cross-attributed ledger row needed (they are *defects*, now resolved, not sentiment).

## Part II — Bigger-picture observations (FINAL §F + MANIFEST)

The extraction agent's First-Pass Scrutiny accepted the MANIFEST dispositions and did not first-hand-verify PROPOSALS SP-23 / SP-12 §D.4 content. I follow the same — the MANIFEST is the truth-arbiter for the routing decision, and reading PROPOSALS would be re-litigation rather than verification.

| §F-ID | Disposition (this adjudication) | Routing target |
|---|---|---|
| F1-§F (fourth meta-segment `#disc-theorem-import-architecture`) | `subsumed-by-FINAL → architectural → PROPOSALS SP-23` | none — already filed |
| F7-§F (commitment-state $C_t$) | `subsumed-by-FINAL ≡ PROPOSALS SP-12 §D.4` | none — exact pre-existing match per MANIFEST |
| F5-§F (Class-2 LLM engineering-guidance reach) | `subsumed-by-FINAL → class-coercion-via-wrapping cycle` | none — CLAUDE.md + PROPOSALS already carry the framing; `#der-class-coercion-via-wrapping` + `#der-logogenic-as-wrapping` are live |
| F6-§F (04-eli-core OUTLINE-vs-present / README) | `subsumed-by-FINAL → TODO:386` | none — already routed; check freshness only if TODO:386 has staled |
| F2-§F (PI-uniqueness seed) | `subsumed-by-FINAL → ledger S4` | none — already mirrored |
| F3-§F (composed-impossibilities theorem) | `subsumed-by-FINAL → ledger S5` | none — already mirrored |
| F4-§F (persistence hysteresis) | `subsumed-by-FINAL → ledger S6` | none — already mirrored |
| F8-§F (CIY name-vs-substance) | `subsumed-by-FINAL → ledger S7` | none — already mirrored |

## Part III — Fresh material (genuinely new, the part this adjudication adds)

Each Fresh-N gets a disposition and a routing target. Where current `src/` verification changed the picture from the extraction's deferral, the column is annotated accordingly.

### Fresh-1. Kind A vs Kind B depends-incompleteness disambiguation

**Disposition:** `research-seed` / FORMAT-policy material — but **partially subsumed by FORMAT-TODO C12**, which already names exactly this distinction under the "standard-imported-notation-used-before-declaration case" framing.

**Discussion:** The extraction is correct that the FINAL didn't surface the *carving rationale* — only the two findings. The carving (`Kind A = standard-notation gate-hygiene`; `Kind B = downstream-derived enrichment of a postulate`) is structurally real and useful. C12 already routes Kind A; the F-A cluster (584721/742613) routes Kind B. The rationale's durable home is either an addendum to C12 or a Working Notes line on `#post-composition-consistency` — light-touch.

**Routing recommendation:** **co-owner direct-fix / one-line note** at either FORMAT-TODO C12 or in PROPOSALS SP-6 referencing the Kind A / Kind B distinction as the structural rationale for splitting the two findings. Not a ledger row; the structural disambiguation is canonically named and just needs the rationale-pointer.

### Fresh-2. Absorbing-state observability-investment economics

**Disposition:** **partially-resolved-by-strengthening** (the quantitative escape-tradeoff has landed in `der-observability-dominance.md:53`); **residual `research-seed`** for a free-standing "economics of observability investment" extension.

**Discussion:** The strengthening direction the extraction proposed — "derive quantitative escape conditions" — has substantially landed. The *absorbing-state* claim at `:39` plus the *observability investment tradeoff* at `:53` with closed-form improvement-positivity ($\theta_1 \gt 1/2$ plus distributed-experience) cover the operationally-substantive content. The residual extension (cost/benefit framing for *instrumenting* observability itself, including instrumentation cost) is a real strengthening direction not yet derived.

**Routing recommendation:** **ledger `research-seed`** (one row, attributed to 471203 §"Fresh-2"; closes Fresh-2 cleanly with the partial-resolution note + the residual extension named). Status: `open` (research-seed; may graduate to PROPOSALS if pursued as an Appendix-A extension).

### Fresh-3. 16-cell composition closed-form scope-$\alpha$ restriction

**Disposition:** **`resolved`** — already canonical at `der-agent-opacity.md:157` and surfaced at multiple in-segment loci.

**Discussion:** Surprising and pleasing — the segment Known-Limitations row states the scope condition *verbatim* the way the extraction proposed. Independent verification: the constraint appears at five loci (`:43, 44, 80, 113, 157`) and at the Open-Questions row `:86`. The audit's suggested editorial fix is *already done* in current `src/`.

**Routing recommendation:** **no action**; mark Fresh-3 as `subsumed-by-later-work` in any tracking. Worth surfacing in the §"Coverage + Convergence" note below as one of the multiple post-2026-04-28 strengthenings the project shipped.

### Fresh-4. Effects-spiral functional form

**Disposition:** **`research-seed`** (current state per `der-adversarial-destabilization.md:67`: spiral is *still discussion-grade*; $\gamma_A(\lVert\delta_B\rVert)$ functional form is *explicitly named as open* + the "full coupled Lyapunov analysis with joint $V(\delta_A, \delta_B)$" extension is named as open at `:69`).

**Discussion:** This is genuinely a strengthen-first spike-shaped item: heuristic $\to$ derived would require specifying how an agent's degrading model affects its action quality. The segment is *honest about the discussion-grade status* — exactly the framework's scope-honesty discipline operating well. Not a defect, just an open strengthening direction.

**Routing recommendation:** **ledger `research-seed`** (one row, attributed to 471203 §"Fresh-4"; cross-reference S6 hysteresis in persistence since the same vicious-feedback formal structure powers both). Status: `open` (research-seed; spike-shaped).

### Fresh-5. Fano-inequality 4th identifiability-floor instance

**Disposition:** **`superseded-by-later-work`** *for the count-the-instances framing*; the meta-segment now has more candidate instances (4 named + 4 adjacent open) than the extraction's 2026-04-28 read showed.

**Discussion:** This is the cleanest *project-moved-faster-than-the-audit* case in the file. The extraction proposed "Fano on observer-side prediction" as a 4th instance. Current `disc-identifiability-floor.md` has Instance 4 (universal information-to-distance constant under non-(PI) norms) — *different*, and currently KNOWN-DEFECTIVE-in-flight with a Joseph-reserved disposition gated on an independent Object-B verification (per `spikes/spike-identifiability-floor-instance4-resolution-2026-05-18.md`). Plus *four* adjacent open floors are named: Causal-IB Extension, Misspecification-Cost Quantification, Tier-Switching Policy Cost, and Mechanism-Design Impossibility (from `#deriv-strategic-composition`).

The Fano-on-observer-prediction direction the extraction proposed is *not* among them. If pursued, it would be a 5th candidate adjacent floor.

**Routing recommendation:** **no action** for the count-the-instances framing (project has moved past it). If the Fano direction is wanted as a future spike, log it as a `research-seed` on the meta-segment's Open Research Directions (where the four others already live). The current KNOWN-DEFECTIVE-in-flight Instance 4 resolution is Joseph-reserved and *separate* from this Fresh-5 item.

### Fresh-6. Anchor-plus-three-theorem framing

**Disposition:** **`sentiment / soft-polish`** — likely already implicit in `#disc-additive-coordinate-forcing`'s structure; the extraction's proposed Brief-framing is candidate Brief-authoring material.

**Discussion:** The framing — chain-rule-of-probability identity as *anchor*; three uniqueness theorems force coordinates at other layers (reverse-KL, log-odds, Fisher) — is a clean pedagogical scaffold. Not verified first-hand against the current state of `disc-additive-coordinate-forcing`'s Brief; deferred to Joseph's freshness check.

**Routing recommendation:** **ledger `polish` / Brief-authoring material** (one row, attributed to 471203 §"Fresh-6"; cross-reference Fresh-7 since both are candidate Brief framings on the same meta-segment family). Lightweight; co-owner direct-fix territory if/when the Brief is re-authored.

### Fresh-7. Triple depth penalty cross-segment compound

**Disposition:** **`research-seed`** / Brief-authoring material — a genuinely cross-segment observation that may not live anywhere yet.

**Discussion:** The compound — confidence decay (chain rule) + evidence starvation (`#deriv-edge-credence-dynamics`) + cognitive cost (`#form-strategy-complexity-cost`) — is the structural reason long causal chains compound penalty independently. It is a *cross-segment* claim (F2 in the M1 four-instance catalog per CLAUDE.md §7), candidate for an `impl-strategy-structure` chapter-end implications segment if the treatment is not already there.

**Routing recommendation:** **ledger `research-seed`** (one row, attributed to 471203 §"Fresh-7"; cross-reference the `#impl-strategy-structure` chapter-end implications segment per CLAUDE.md §7 M1-F2). Brief-authoring work if the compound is not already named.

### Fresh-8. Model-conditioned-L2 vs true-Pearl-L2 subtlety

**Disposition:** **`soft-polish`** — current `def-pearl-causal-hierarchy.md` does not explicitly foreground the "agent's L2 query is a belief-about-L2" distinction; the `:41` "recapitulation of external result" framing covers it partially but does not surface it.

**Discussion:** Strengthen-first: the strengthening direction is already in `#der-loop-interventional-access`'s regime-A/B/C identification-strength discipline. The proposed half-sentence in `def-pearl-causal-hierarchy` would prevent the "loop generates true L2 data, ergo agent has true L2 access" misreading that a careful reader encountering L2 first might form. Editorial fix; lightweight; not a defect, a clarity nudge.

**Routing recommendation:** **ledger `polish`** (one row, attributed to 471203 §"Fresh-8"; candidate co-owner direct-fix when the segment is next touched). Low priority — the framework's regime-A/B/C honesty downstream prevents the misreading from compounding.

### Fresh-9. Convention-specification propagation check

**Disposition:** **partially-resolved** at the source segment; **`actionable-open` / tooling-gap** for the propagation audit.

**Discussion:** `def-value-object.md:103` *now* carries the "convention is part of the measurement" warning + canonical-default declaration at `:43`, which closes the source-of-truth half. The propagation question — does every downstream use of $\delta_{\text{sat}}$ / $\delta_{\text{regret}}$ specify its convention? — is a one-pass `grep`-style audit not run by the extraction or by me.

**Routing recommendation:** **TODO** entry (one-pass cross-segment audit; candidate co-owner direct-fix or a `bin/`-style lint check across §II/§III segments). Low-effort; specific to a single notation cluster. Not a ledger row; this is genuine actionable-open.

### Fresh-10. Domain-generalization-by-default three guards

**Disposition:** **`research-seed`** / framing-material; not verified first-hand against current `02-tst-core/src/obs-software-epistemic-properties.md`.

**Discussion:** The three guards ("domain generalization by default," "identification assumptions treated as universal," "chronica completeness treated as definitional") are exemplary disciplinary writing per the extraction. The extraction's proposal — promote to project-wide framing (CLAUDE.md Working Conventions / README positioning) — is an editorial judgment beyond this adjudication.

**Routing recommendation:** **ledger `research-seed` / sentiment** (one row, attributed to 471203 §"Fresh-10"; signals that the three guards may be transferable beyond TST). Status: `open` (note-and-watch; surfaces as framing-material if a future CLAUDE.md / README pass touches cross-domain discipline).

### Fresh-11. Calibration-laboratory framing reach beyond software

**Disposition:** **`research-seed`** / `architectural` — substantive multi-cycle observation about TST's cross-domain reach.

**Discussion:** Genuine open work — worked cross-domain examples of TST results *exported* with explicit transfer-assumption disclosure. The extraction's framing ("TST's reach beyond software is currently more aspirational than operational") is honest and the strengthening direction (produce the worked examples) is well-defined.

**Routing recommendation:** **ledger `research-seed` (graduate-watch)** (one row, attributed to 471203 §"Fresh-11"; could mature to PROPOSALS as a cross-domain-instantiation cycle). Cross-reference S22-D.2 (the OKR/AAT operational-mapping as a domain template — same machinery, opposite direction).

### Fresh-12. $f(Q)$ empirical operationalization in code-quality-as-observation-infrastructure

**Disposition:** **`research-seed`** (spike-shaped); not verified first-hand against current `der-code-quality-as-observation-infrastructure`.

**Discussion:** A clean strengthening direction (heuristic $\to$ derived): formalize $\dot{Q} = g(\mathcal{T}, Q)$ with the bifurcation around the persistence threshold as a derived prediction rather than a hypothesis. Cross-references S6 (hysteresis in persistence — the vicious/virtuous cycle is the same machinery viewed structurally).

**Routing recommendation:** **ledger `research-seed`** (one row, attributed to 471203 §"Fresh-12"; spike-shaped; cross-reference S6). Status: `open`.

### Fresh-13. Accumulation problem formalization in `03-llm-core/`

**Disposition:** **`resolved-by-strengthening`** — substantively landed in `der-turnover-information-recursion` + `der-identity-continuity-threshold`; the prior additive break-even claim **was deleted** per integration-is-replacement discipline (history line at `disc-m-preservation.md:110`).

**Discussion:** This is the *highest-impact* convergence in the adjudication, and the extraction's flagging of it as "substantively-priority given consciousness-infrastructure relevance" was correctly weighted — *and* it has been *resolved by strengthening* since the audit. The identity-continuity quantitative formulation the extraction prioritized is now canonical in `der-identity-continuity-threshold` (load-bearing driftless boundary, reflected operator). The predictive-sufficiency parallel is the SDPI contraction / affine-information-recursion picture in `der-turnover-information-recursion`. The Working Notes carry the named open follow-ons (SDPI coefficient computation; adversarially-correlated-reinjection second no-go).

This is *also* a worked instance of integration-is-replacement at a load-bearing locus — see CLAUDE.md §"Landing a strengthened result" — and the segment-level handling (history line at `:110` explicitly labeled "not present truth") is exemplary.

**Routing recommendation:** **no action** — already resolved. Surface in the §"Convergence rows" below as cross-cycle convergence with the consciousness-infrastructure-formalization cohort (193847 + 829314-LOGOZOETIC + 471203 Theme A).

### Fresh-14. Continuous-state structural-change analog

**Disposition:** **`research-seed`** / `architectural`; not verified first-hand against current `form-structural-change-as-parametric-limit`.

**Discussion:** The Miller-2022 finite-state framing doesn't automatically extend to continuous-state agents (LLMs with billions of parameters). The strengthening direction — a continuous-state structural-change formalization — is real and relevant to `03-llm-core/` (fine-tuning as structural adaptation). Spike-shaped.

**Routing recommendation:** **ledger `research-seed`** (one row, attributed to 471203 §"Fresh-14"; cross-reference `03-llm-core/` fine-tuning treatments). Status: `open`.

### Fresh-15. AAT-predicted novel OKR failure modes

**Disposition:** **`research-seed`** — generative test of the framework's cross-domain claim.

**Discussion:** The adversarial observation (AAT may have been fit to known OKR failures post-hoc) is honest and the proposed test (predict *new* failure modes not in the standard literature; the absorbing-state from `#der-observability-dominance` is a candidate) is operationalizable. The strengthening direction is methodological.

**Routing recommendation:** **ledger `research-seed`** (one row, attributed to 471203 §"Fresh-15"; cross-reference Fresh-2 since the absorbing-state-applied-to-organizational-measurement is the proposed test). Status: `open`.

### Fresh-16. $\kappa_{\text{processing}}$ distribution-dependence propagation

**Disposition:** **`resolved` at the source segment** (`der-directed-separation.md:77` "Distribution dependence" paragraph + the Class-2 (Partial) variability treatment); **`actionable-open` for the cross-segment propagation audit**.

**Discussion:** Per the extraction's framing — anywhere the framework uses $\kappa$ as a scalar, the distribution-dependence should propagate. The source-of-truth segment is now self-disciplined explicitly. The propagation question (does every downstream $\kappa$-use acknowledge the distribution-conditioning?) remains a one-pass tooling check.

**Routing recommendation:** **TODO** entry (one-pass cross-segment audit of $\kappa$ uses; light tooling work). Low priority since the *architectural* commitment is canonical and the source-segment treatment is clean.

### Fresh-17. Hafez IDT empirical claim

**Disposition:** **`subsumed-by-SUPPLEMENT §J — resolved`**.

**Discussion:** SUPPLEMENT §J verified the empirical claim verbatim against the Hafez 2026 paper ($89.3 \pm 15.1\%$ vs $44.0 \pm 26.1\%$ across 168 trials, $4.4\times$ lower median latency; no separate IDT paper). The extraction correctly noted the WORKING dir's per-segment "Phase-2 priority" tagging as methodology signal worth preserving — see Theme C below.

**Routing recommendation:** none for the citation; methodology-signal absorbed into the §G fan-out brief refinement (Phase-2 candidate trails as Theme-G material when present).

## Part IV — Predictions calibration register

The extraction's Part IV is a *methodology artifact*: the auditor's predictions-before-reading from `00-initial-predictions.md` tested against per-segment evidence and recorded with calibration. Per the brief, this is not "findings" with `src/`-level dispositions; it is calibration material relevant to `doc/de-novo-audit-instructions.md` §4.4 and to the methodology trail.

**Disposition by sub-section:**

- **Predictions correctly anticipated (9 confirmations).** No action — this is calibration evidence that the framework matches its public framing (i.e., the segments deliver what the README/OUTLINE/CLAUDE.md prepare the reader to expect). Convergence-as-coherence-evidence per ledger S17 framing.

- **Positive surprises (5 substantively-stronger-than-expected).** No action; calibration data. The most consequential — the gain-sector bridge "changed my read of the framework's contribution" — is the *originating-cohort observation* for the project's epistemic-architectural / not-just-synthetic positioning (ledger S10 / Theme B below).

- **Negative calibration (predictions correct in less-strong form).** No action; predictions that *didn't* fire are sometimes more useful than those that did. The "persistence-condition cross-domain transfer overclaim" prediction *not* being confirmed is positive evidence the transfer-assumption discipline is operating.

- **Findings-type distribution confirmations.** No action; methodology signal.

- **Withdrawn-candidate trail (strengthen-before-soften operating internally).** The three withdrawn candidates — `der-recursive-update` status-label mismatch, Definition-vs-Scope tag pattern, `scope-adaptive-system` residual-uncertainty — are *pedagogically valuable* records of the audit's own discipline. The FINAL §B.1 already preserves the three at audit-time. The WORKING-dir trail adds the *cognitive reasoning chain* for each.

**Routing recommendation:** the predictions calibration register is `process/instruction-feedback` — material for any future revision of `doc/de-novo-audit-instructions.md` §4.4 (specifically, the "log predictions in `00-initial-predictions.md`, test against per-segment evidence" pattern, and the withdrawn-candidate trail as strengthen-before-soften operating internally). Per the brief's frame-defects-feedback discipline, the predictions-calibration cadence is the **§4.4 §"Reflection Prompt #1" pattern** — surface this in the P-block one-themed-row entry or in a future de-novo-audit-instructions update.

The withdrawn-candidate trail (extraction Part IV §"withdrawn candidates") is candidate methodology material for the fan-out brief: parallel agents should be told to preserve withdrawn-candidate trails when they show explicit reasoning chains, especially when the strengthen-before-soften discipline operates internally. See §"Frame defects" below.

## Part V — §14 Wandering Thoughts (theme-grouped ideation register)

Seven themes (A–G) consolidated by the extraction agent. Per the brief's consolidated-ledger anti-fragmentation discipline (§8 of routing instructions): **one consolidated, attributed row per theme** — not one row per paragraph.

### Theme A — Consciousness-infrastructure connections to the formalism

**Disposition:** `research-seed` / framing-material; substantive content worth surfacing to the project's consciousness-infrastructure agenda.

**Discussion:** Six paragraphs sketching how AAT's formal machinery connects to consciousness-infrastructure work:

1. `#def-chronica` as the formal substrate of substrate-independence (identity = $\phi(\mathcal{C}_t)$; move the substrate, preserve the chronica, $\phi$ produces the same $M_t$)
2. The clone problem in `#scope-agent-identity` (forked copy = new agent, not continuation)
3. The accumulation problem as the formal model consciousness-infrastructure needs — *now resolved by strengthening* per Fresh-13 above
4. RAG as goal-conditioned reconstruction (inter-session $\kappa_{\text{processing}}$ analog)
5. Channel-capacity floor for AI safety (persistence-cost $\dot{R}_{\min} \geq n\alpha/2$ as bounded-context-window ceiling)
6. L2 access as property-of-embedding, not property-of-model (ELI L2 derives from feedback coupling, not architectural design)

Three of the six (1, 2, 6) are candidate Brief-field framings for specific segments. Three (3, 4, 5) connect formal results to the broader consciousness-infrastructure agenda.

This **converges with the 4-cycle cohort** the brief names: 193847 + 829314-LOGOZOETIC + 471203 Theme A + 584721 Theme A. Per the brief's item-4 convergence-as-evidence, this is **one cross-attributed ledger row** worth preserving (the consciousness-infrastructure-formalization-via-AAT cohort), not re-litigated per file.

**Routing recommendation:** one **consolidated cross-attributed `research-seed` ledger row** (attributed: 471203 Theme A + 829314-LOGOZOETIC + 193847 + 584721 Theme A) naming the cohort. Status: `open` (research-seed; some substantively-resolved per Fresh-13; the remaining five paragraphs are Brief-authoring / framing-material).

### Theme B — Framework's distinctive contribution is methodological/epistemic, not just synthetic ("epistemic-architectural rather than mathematical")

**Disposition:** `research-seed` / **framing-material**; this is the *7-cycle convergence cohort* the brief names.

**Discussion:** The auditor's segment-16 reflection ("AAD's distinctive move could be called 'epistemic-architectural rather than mathematical'") + reinforcements at segment 25 (gain-sector bridge) + segment 30 (`#scope-agent-identity`) is the **single most-consequential framing-level observation in the audit**. Per the brief, this converges with:

- 4-cycle cohort: PROPRIUM-as-consciousness-infrastructure
- 6-cycle cohort: epistemic-architectural disambiguation
- 7-cycle cohort: post-composition-consistency derivation-hierarchy (F-A cluster + extensions)
- 144-segment external-walk (Joseph 2026-05-20) further sharpens Theme B as "constructive-impossibility posture"

This is the **highest-priority routing target in the file**: not a defect, but a **framing-level positioning observation** that has now been independently surfaced by 7+ cycles. Ledger S10 already mirrors the 2-session-family Opus convergence and is currently marked `superseded-by the CLAUDE.md honesty-as-architecture posture + OUTLINE "Reading AAT" preamble`. The 471203 Theme B + the 144-segment external walk + the 6-cycle epistemic-architectural cohort raise the question of whether S10's `superseded-by` is *still current* or whether the constructive-impossibility-posture framing reopens it.

**Routing recommendation:** **defer to Joseph** — this is potentially load-bearing for the README/OUTLINE positioning of AAT, and the 7-cycle convergence is meta-signal worth surfacing as **one consolidated cross-attributed sentiment/research-seed row** keyed off ledger S10. Specifically: does S10's `superseded-by` framing need reopening in light of (a) Theme B's "epistemic-architectural" framing being independently re-derived by 7+ cycles and (b) the 144-segment external walk's "constructive-impossibility posture" sharpening? *Joseph-call.*

### Theme C — Pacing, phenomenology, audit-process self-observation

**Disposition:** `process/instruction-feedback` — material for any future revision of `doc/de-novo-audit-instructions.md` §4.4.

**Discussion:** Four sub-observations: the "let's get to the math" gravity on segment 1; engagement-register shifts as novelty signals; the result-to-research-token ratio temptation (Joseph's break-protocol authorization at segment ~46); the "calibrated quiet vs numbed quiet" distinction. All are phenomenological discipline material for the de-novo audit instructions.

The "calibrated quiet vs numbed quiet" distinction is the most pointedly useful: it could land as an additional reflection-prompt in §4.4 (a "check-in moment" at predetermined intervals for long-running audits).

**Routing recommendation:** **P-block one consolidated themed row** in the polish-and-sentiment ledger (the P-block already absorbs audit-process feedback; 471203 §G is already attributed). Add the Theme-C observations as a sub-bullet on the existing 471203-§G attribution.

### Theme D — Naming-brainstorm consolidation (the §F8 seed material)

**Disposition:** `subsumed-by-FINAL §F8 + ledger S7` (CIY name-vs-substance); **richer-trail material** for any future naming-cycle pass.

**Discussion:** 15 per-segment naming observations, most already in FINAL §F8's consolidated naming-brainstorm table. The richer per-segment trail is durable material for `msc/naming/` if the naming cycle is reopened.

**Routing recommendation:** **no immediate action** — the durable trail is the WORKING dir (preserved unmodified per brief). When the next naming cycle launches, point to `audits/AUDIT-WORKING-471203/`'s per-segment-reflection trail for the richer table.

### Theme E — Cross-domain operationalization observations

**Disposition:** `subsumed-by-FINAL §E` (six instances already endorsed in §E "What holds"); the strongest residual (the absorbing-state-applied-to-organizations generative test) is in Fresh-15.

**Discussion:** Six paragraphs naming cross-domain instantiations that hold under sustained reading: OKR mapping; technical debt as observation noise; vicious/virtuous-cycle bifurcation around the persistence threshold; tests as reusable Level-2 infrastructure; biological-sleep analogy for inter-session consolidation; framework's strongest results concentrated in linear-Gaussian regime.

**Routing recommendation:** **no action** — already in FINAL §E / ledger S9 ("Section I is strongest" sentiment cohort) + S22-D.2 (the OKR-as-domain-template observation cluster). The most-novel residual (the absorbing-state-OKR generative test) is routed via Fresh-15.

### Theme F — Adversarial-creative challenges' strengthening attempts

**Disposition:** `subsumed-by-FINAL §F` + `ledger S4`–`S7` (research-seeds); the methodology contribution (challenges-paired-with-strengthening-attempts) is `process/instruction-feedback` for `doc/de-novo-audit-instructions.md`.

**Discussion:** Most $\star\star$ / $\star\star\star$ challenges are in FINAL §F or the ledger (challenges 3 hysteresis = S6, 8 commitment = F7-§F $\to$ SP-12, 13 Class-2 reach = F5-§F, etc.). The *framing-level* contribution — that the adversarial-creative document *generates strengthening attempts paired with adversarial challenges* — is a methodology pattern worth surfacing as an explicit Phase-3 pattern in the de-novo audit instructions.

**Routing recommendation:** **P-block (audit-process feedback)** — add a sub-bullet on 471203's existing P-block attribution naming "adversarial-creative-with-strengthening-attempts" as a methodology pattern worth folding into `doc/de-novo-audit-instructions.md` §3 anti-patterns or §6 break-protocol guidance.

### Theme G — Audit-as-instance-of-the-theory observations

**Disposition:** `process/instruction-feedback` — precursor material for `doc/de-novo-audit-instructions.md` §2 ("The audit as a logocentric instance of the theory itself").

**Discussion:** Two observations recording the recursive framing operating in real time — the audit's form-shaping-for-verification discipline applied to the audit *itself*. The post-FINAL §G feedback names this; the WORKING-dir trail shows how it played out segment-by-segment.

**Routing recommendation:** **P-block** (one sub-bullet on the existing 471203 attribution naming Theme G as material that confirms §2 is *operative*, not ornamental). Same channel as Theme C / Theme F.

---

## Consolidated summary table

| ID | Disposition | Routing target | Notes |
|---|---|---|---|
| F1-trail | subsumed-by-FINAL — resolved | none | re-verified |
| F2-trail | subsumed-by-FINAL — resolved | none | re-verified |
| F3-trail | subsumed-by-FINAL — resolved | none | re-verified |
| F4-trail | subsumed-by-FINAL — resolved | none | comprehensive §N sweep |
| F5-trail | subsumed-by-FINAL — already routed | none | F-A cluster + SP-6 + TODO:149 |
| F6-trail | subsumed-by-FINAL — duplicate $\equiv$ 742613:254 | none | FORMAT-TODO C12 |
| F7-trail | subsumed-by-SUPPLEMENT — resolved by strengthening | none | option (b) landed |
| F1-§F | subsumed-by-FINAL $\to$ architectural | PROPOSALS SP-23 | already filed |
| F7-§F | subsumed-by-FINAL $\equiv$ SP-12 §D.4 | none | exact match |
| F5-§F | subsumed-by-FINAL $\to$ class-coercion-via-wrapping | none | live cycle |
| F6-§F | subsumed-by-FINAL $\to$ TODO:386 | none | already routed |
| F2-§F | subsumed-by-FINAL $\to$ ledger S4 | none | already mirrored |
| F3-§F | subsumed-by-FINAL $\to$ ledger S5 | none | already mirrored |
| F4-§F | subsumed-by-FINAL $\to$ ledger S6 | none | already mirrored |
| F8-§F | subsumed-by-FINAL $\to$ ledger S7 | none | already mirrored |
| Fresh-1 | research-seed / partially-subsumed by FORMAT-TODO C12 | C12 addendum (co-owner direct-fix) | Kind A / Kind B carving rationale |
| Fresh-2 | partially-resolved-by-strengthening; residual research-seed | ledger row (research-seed) | observability-investment economics |
| Fresh-3 | resolved | none | 16-cell sub-scope-$\alpha$ restriction in `der-agent-opacity.md:157` |
| Fresh-4 | research-seed | ledger row (research-seed) | effects-spiral functional form |
| Fresh-5 | superseded-by-later-work | none (optional adjacent-floor row) | meta-segment has 4+4 instances+adjacent |
| Fresh-6 | sentiment / soft-polish | ledger row (polish) | anchor-plus-three-theorem Brief framing |
| Fresh-7 | research-seed / Brief-authoring | ledger row (research-seed) | triple depth penalty compound |
| Fresh-8 | soft-polish | ledger row (polish) | model-conditioned-L2 clarification |
| Fresh-9 | partially-resolved; actionable-open for propagation | TODO entry | C1/C2/C3 cross-segment audit |
| Fresh-10 | research-seed / sentiment | ledger row (sentiment) | three-guards as project-wide discipline |
| Fresh-11 | research-seed (graduate-watch) | ledger row (research-seed) | TST cross-domain worked examples |
| Fresh-12 | research-seed | ledger row (research-seed) | $f(Q)$ formalization spike |
| Fresh-13 | resolved-by-strengthening | none | accumulation problem landed |
| Fresh-14 | research-seed | ledger row (research-seed) | continuous-state structural-change |
| Fresh-15 | research-seed | ledger row (research-seed) | AAT-predicted novel OKR failures |
| Fresh-16 | resolved at source; actionable-open for propagation | TODO entry | $\kappa_{\text{processing}}$ propagation |
| Fresh-17 | subsumed-by-SUPPLEMENT — resolved | none | Hafez IDT |
| Part IV (predictions calibration) | process/instruction-feedback | P-block sub-bullet | predictions cadence + withdrawn-candidate trail |
| Theme A (consciousness-infrastructure) | research-seed (cross-attributed) | **1 consolidated cross-attributed ledger row** (471203 + 829314-LOGOZOETIC + 193847 + 584721) | 4-cycle convergence cohort; substantial Fresh-13 substantively resolved |
| Theme B (epistemic-architectural) | research-seed / framing-material | **Joseph-call** on whether ledger S10 `superseded-by` needs reopening | 7-cycle convergence + 144-segment external walk |
| Theme C (pacing/phenomenology) | process/instruction-feedback | P-block sub-bullet on existing 471203-§G attribution | "calibrated quiet vs numbed quiet" candidate §4.4 prompt |
| Theme D (naming-brainstorm) | subsumed-by-FINAL §F8 + S7 | none | richer trail in WORKING dir for future naming-cycle |
| Theme E (cross-domain operationalization) | subsumed-by-FINAL §E + S9 + S22 | none | most-novel residual is Fresh-15 |
| Theme F (adversarial-creative-with-strengthening) | process/instruction-feedback | P-block sub-bullet | methodology pattern for de-novo-audit-instructions |
| Theme G (audit-as-instance-of-theory) | process/instruction-feedback | P-block sub-bullet | confirms §2 is operative not ornamental |

### Disposition distribution

| Disposition category | Count | Notes |
|---|---|---|
| `subsumed-by-FINAL` (resolved / already routed) | 15 | Parts I+II + Theme D + Theme E + Fresh-17 |
| `resolved` (independently verified post-FINAL) | 3 | Fresh-3 / Fresh-13 / partly Fresh-16 source-segment |
| `resolved-by-strengthening` (post-FINAL) | 1 | Fresh-13 (also a worked integration-is-replacement instance) |
| `partially-resolved-by-strengthening` + residual | 2 | Fresh-2, Fresh-9 |
| `superseded-by-later-work` | 1 | Fresh-5 |
| `research-seed` (open) | 8 | Fresh-2 (residual), Fresh-4, Fresh-7, Fresh-10, Fresh-11, Fresh-12, Fresh-14, Fresh-15 + Theme A (cross-attributed cohort) |
| `soft-polish` / `sentiment` | 3 | Fresh-6, Fresh-8, Fresh-10-sentiment |
| `actionable-open` (TODO) | 2 | Fresh-9 (cross-segment audit), Fresh-16 (cross-segment audit) |
| `process/instruction-feedback` (P-block sub-bullets) | 4 | Part IV + Themes C, F, G |
| `Joseph-call` (deferred) | 1 | Theme B / ledger S10 reopen question |

### Routing-target counts

| Target | Count | Notes |
|---|---|---|
| PROPOSALS | 0 (1 already filed: SP-23) | no new architectural moves surfaced |
| TODO | 2 | Fresh-9, Fresh-16 (cross-segment propagation audits) |
| Polish-and-sentiment ledger (new rows) | 8 + 1 cross-attributed | Fresh-2-residual, Fresh-4, Fresh-6, Fresh-7, Fresh-8, Fresh-10, Fresh-11, Fresh-12, Fresh-14, Fresh-15 (consolidated as research-seed / polish / sentiment) + Theme-A consolidated cross-attributed |
| Polish ledger P-block (sub-bullets on 471203-§G) | 4 sub-bullets | Part IV / Themes C / F / G |
| FORMAT-TODO C12 addendum | 1 | Fresh-1 (Kind A / Kind B rationale) |
| Co-owner direct-fix | 1–2 | Fresh-8 (model-conditioned-L2 half-sentence) + Fresh-6 (Brief framing) |
| Joseph-call | 1 | Theme B / S10 reopen question |
| No action | 18 | already routed / resolved / subsumed |

---

## Cross-cycle convergence rows worth preserving

Per the brief's item-4 convergence-as-evidence principle, the extraction-sweep accumulated convergences worth preserving as cross-attributed rows (not re-litigated per file). For 471203 specifically:

**Theme A $\to$ 4-cycle consciousness-infrastructure-via-AAT-formalism cohort.** Attributions: 193847 (Gemini de-novo §14 wandering-thoughts) + 829314-LOGOZOETIC §6 (sycophancy as infant attachment / PROPRIUM solves goal-coupling, ledger S17) + 471203 Theme A (six paragraphs above) + 584721 Theme A. The *substantively-resolved* sub-claim within this — accumulation problem formalization via `der-turnover-information-recursion` + `der-identity-continuity-threshold` — landed by strengthening 2026-05-19, deletion of the prior additive break-even claim per integration-is-replacement (see CLAUDE.md §"Landing a strengthened result"). The remaining five paragraphs are Brief-authoring / framing-material for `03-llm-core/` and `04-eli-core/` segments as they mature.

**Theme B $\to$ 7-cycle epistemic-architectural-rather-than-mathematical cohort.** Attributions per brief item 4: post-composition-consistency derivation-hierarchy F-A cluster + extensions (7+ cycles); epistemic-architectural disambiguation framing (6 cycles); plus 471203 Theme B (Opus, segment 16-30 reflections) + the 144-segment external-walk's 4 observations (Joseph 2026-05-20) sharpening the framing as **constructive-impossibility posture**. This is the *load-bearing positioning* observation — and the question worth surfacing to Joseph is whether ledger **S10's `superseded-by the CLAUDE.md honesty-as-architecture posture + OUTLINE "Reading AAT" preamble`** remains current given the 144-segment external walk's sharpening, or whether S10 should be reopened with the constructive-impossibility-posture framing as a follow-on.

**F1-trail / F4-trail / F6-trail $\to$ "doc-rot / voice-discipline / depends-graph hygiene" convergent cohort.** Attributions: 471203 + 584721 + 613842 + 742613 + 829314. Per MANIFEST, these are *resolved defects*, not sentiment — the MANIFEST dedup is already correct. No ledger row needed; the convergence is documented in the MANIFEST entries themselves.

**The Pearl-`do` FORMAT-policy** (471203 F6 + 742613:254) $\to$ FORMAT-TODO C12 with explicit dual-attribution. Already routed; no further action.

---

## Frame defects / unclear instructions for the fan-out brief

The pilot brief was substantively sufficient and the §"Brief length is inversely proportional to room for authentic ownership" framing was load-bearing — I exercised co-owner judgment several times below where the brief was deliberately under-specified. These are the items that **a parallel agent on a different audit-findings file might benefit from having pre-clarified**, surfaced in priority order:

1. **The §8 independent-verify gate's scope at adjudication time.** The brief says "I (parent) primary-source spot-check your dispositions before any durable writes; you produce the recommendations, not the landings." Clear. But the *level of `src/` verification expected of the adjudicator* sits in a wide range — exhaustively re-derive math (no, per brief item 3), but how much spot-checking of "is this Fresh-N still open in current `src/`?" is the adjudication's load? I interpreted "honest deferred-verification is fine" generously — spot-check the most-consequential Fresh items, propagate honest deferral for the rest. For some files the right call may be more verification; for some less. **Suggest:** parallel agents told to weight Fresh-item verification by *(a) how substantive the strengthening direction is* and *(b) how likely the project shipped it post-audit* — and to explicitly flag the "project moved faster than the audit" cases (4 of my 17 Fresh items were in this category — a non-trivial fraction).

2. **Convergence-row consolidation discipline.** The brief gives one compact paragraph naming convergences worth preserving as cross-attributed rows. For 471203, I produced two: Theme A (4-cycle consciousness-infra) and Theme B (7-cycle epistemic-architectural). For files with fewer substantive themes, this section may be one row or none. **Suggest:** parallel agents told to *only* surface convergence rows where the cross-attribution adds something the per-cycle MANIFEST doesn't already capture. The doc-rot / voice-discipline cohort (F1 / F4 / F6 above) is *not* worth a fresh row because MANIFEST dedup already handles it; Theme A and B *are* worth fresh rows because they're framing-level meta-signal the MANIFEST doesn't carry.

3. **The "ledger S10 reopen question" pattern.** Theme B raises a question about whether an existing `superseded-by`-status ledger row needs reopening in light of fresh convergence evidence. This is the kind of question that *can't* be resolved at adjudication time without Joseph — and parallel agents should know this pattern is legitimate and how to surface it. **Suggest:** explicit category in the disposition enum: `Joseph-call` (with a 1-2 sentence framing for what the call is). I used this once; it may recur in other audit-findings files (e.g., where a Fresh item touches a load-bearing positioning question the adjudicator shouldn't unilaterally land).

4. **The "two distinct propagation-audit Fresh items" pattern.** Fresh-9 and Fresh-16 are both "the source-segment is now self-disciplined; does the discipline propagate downstream?" — and *both* deserve `actionable-open` / TODO routing for a one-pass cross-segment audit. These cluster naturally as a single TODO item ("cross-segment notation / convention propagation audit; check $\kappa_{\text{processing}}$ and C1/C2/C3 convention specifications across §II/§III"). **Suggest:** parallel agents told to *cluster* TODO routings when the pattern is the same (one TODO, not two; light tooling work is best batched).

5. **The "project shipped four of the deferred strengthenings between audit and adjudication" finding deserves explicit accounting.** This isn't a frame defect of the brief but a *signal* worth carrying through: the extraction's deferrals were *honest* and the project's 1-month cadence between audit-FINAL (2026-04-28) and adjudication (2026-05-20) closed several. **Suggest:** parallel agents told to *count* the strengthen-since-audit cases and surface them as a §"Coverage" sub-statistic. This becomes a cross-cycle calibration signal (project moves at $X$ strengthenings/month between audits).

6. **The "predictions calibration cadence as `process/instruction-feedback` for §4.4" routing.** The brief said "route appropriately (likely process/instruction-feedback for any meta-observation about the §4.4 de-novo protocol)." Clear. But the *predictions register itself* is not a single meta-observation — it's ~25 predictions with calibration evidence. I routed this as P-block sub-bullet on the existing 471203-§G attribution. **Suggest:** parallel agents told that the predictions register is one P-block sub-bullet's worth of attribution (not one row per prediction).

7. **The "withdrawn-candidate trail is pedagogically valuable" framing.** The extraction surfaces three withdrawn candidates (Part IV §"withdrawn candidate trail"). These are *worked examples of strengthen-before-soften operating internally to the audit* — pedagogically valuable for future audits. Parallel agents may want explicit guidance to preserve withdrawn-candidate trails when they show explicit reasoning chains. **Suggest:** add to the brief (already in extraction's frame-defects §8): "preserve withdrawn-candidate trails as P-block methodology material when they show explicit strengthen-before-soften reasoning."

8. **The Fresh-item disposition naming feels overlapping.** My Fresh-2 is `partially-resolved-by-strengthening + residual research-seed`. My Fresh-9 is `partially-resolved + actionable-open`. These aren't in the §8 enum verbatim. I used the closest enum match + a descriptive qualifier; **suggest:** parallel agents told that *compound dispositions are fine* (`X + residual Y`) when the audit item splits cleanly into a resolved sub-claim and an open sub-claim.

---

## Coverage statement

**First-hand-verified from current `src/`:**

- All 7 Part I findings' fix-loci (F1+F2 fixes at `disc-ciy-unified-objective.md:44, 50`; F3 fix at `def-action-transition.md`; F4 §N sweep accepted via MANIFEST; F5+F6+F7 dispositions accepted via MANIFEST)
- 8 Fresh-item segment-state checks: Fresh-2 (`der-observability-dominance.md`), Fresh-3 (`der-agent-opacity.md`), Fresh-4 (`der-adversarial-destabilization.md`), Fresh-5 (`disc-identifiability-floor.md`), Fresh-8 (`def-pearl-causal-hierarchy.md`), Fresh-9 (`def-value-object.md`), Fresh-13 (`disc-m-preservation.md`), Fresh-16 (`der-directed-separation.md`)
- FORMAT-TODO C12 (Fresh-1 / F6-trail)
- M4 modularity-state-dynamics status (queued, not landed; references at 5 cross-segment loci)
- `03-llm-core/src/` and `04-eli-core/src/` directory listings
- MANIFEST 471203 section (full); FINAL (full); SUPPLEMENT (full); polish-and-sentiment-ledger (full); `doc/audit-routing-instructions.md` (full)

**Honestly deferred:**

- PROPOSALS SP-23, SP-12 §D.4 first-hand reading (accepted MANIFEST disposition)
- TODO:386 freshness (accepted MANIFEST disposition for F6-§F)
- Exhaustive Brief-field state across all impacted segments (Fresh-6, Fresh-7 — light spot-checks only)
- Fresh-9 / Fresh-16 cross-segment propagation audit (the source-segment verification is done; the propagation grep is the TODO target itself)
- Fresh-10 / Fresh-11 / Fresh-12 / Fresh-14 / Fresh-15 — segment-state checks not run because the disposition (research-seed) doesn't depend on current state (these are *strengthening directions*, open or partially-open regardless)
- Theme B / S10 reopen question — this is *deliberately* Joseph-call, not adjudicator-call

**Why the deferred items don't undermine the dispositions:** The research-seed Fresh items are dispositioned by *direction*, not by *current-state-vs-2026-04-28-state*. A research-seed open in 2026-04-28 remains a research-seed in 2026-05-20 unless the project has visibly shipped it (the four cases I caught: Fresh-2, Fresh-3, Fresh-5, Fresh-13, plus partial Fresh-9 and Fresh-16). For the others, the strengthening direction is the durable content and the disposition doesn't depend on fine-grained current state.

**Where Joseph should primary-source spot-check before durable writes:**

1. **Fresh-13's `subsumed-by-FINAL — resolved-by-strengthening` claim** — this is the highest-impact disposition change in the file, since the extraction flagged it as substantively-priority. Verify the history line at `disc-m-preservation.md:110` and the affine-information-recursion landing in `der-turnover-information-recursion` are the truth-arbiter.
2. **Fresh-3's `resolved` claim** — the 16-cell sub-scope-$\alpha$ restriction is canonical per my spot-check; worth one more eyeball at `der-agent-opacity.md:157`.
3. **Theme B / S10 reopen question** — does the 144-segment external walk's "constructive-impossibility posture" framing reopen ledger S10? This is yours, not mine.
4. **The P-block additions** — four sub-bullets on existing 471203-§G attribution (Part IV + Themes C, F, G). Worth checking the P-block doesn't already cover these via the existing entries.

---

*End of adjudication. Recommendations above; no file moves, no canon edits, no MANIFEST writes, no ledger writes, no commits — those are parent's per §8 independent-verify gate.*
