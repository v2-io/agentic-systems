---
source_cycle: 738192 (de-novo, Gemini CLI, 2026-04-25)
extraction_agent: Claude Opus 4.7 (1M context), parallel-sweep run
extraction_date: 2026-05-20
working_dir: audits/AUDIT-WORKING-738192/ (4 files, 4 small reflections)
final_of_record: audits/.integrated/audit-738192-FINAL.md
manifest_entry: audits/.integrated/MANIFEST.md "2026-05-16 — Cluster B: math-heavy ledgered"
ledger_entry: audits/polish-and-sentiment-ledger.md S21 (sentiment — process feedback)
purpose: |
  Consolidated extraction from the WORKING dir for routing through the standard
  audit-routing process. The original working dir is preserved separately;
  this file is the "what is in there worth processing" digest.
---

# Audit-findings extract — 738192 working-dir mining

The 738192 cycle was a compact, math-targeted de-novo walk by **Gemini CLI** on 2026-04-25. The dir contains only four files (`00-initial-predictions.md`, `00-running-outline.md`, `01-reflections-section-I-early.md`, `02-reflections-IB-volatility.md`) and the FINAL itself carries exactly two findings (F1 IB-$\beta$-vs-$\rho$ conflation; F2 `git checkout` misclassified as Level 3) plus process feedback. The MANIFEST 2026-05-16 disposed both as **resolved by strengthening** under Cluster B, and the process-feedback rolled to ledger S21 as a sentiment row.

What the WORKING dir adds *beyond* the FINAL's adjudication is light: it is the genuine cognition trail for two findings that were already promoted at FINAL-time. The auditor surfaced both finds in their first reflection passes (the L3 finding mid-segment-9 in the first reflection file; the IB-$\beta$ finding in the second reflection file's first read of `form-information-bottleneck`), and stopped recording explicit per-segment reflections after that — likely because the audit's deliverable was already in shape and there was no further substantive surfacing in the Section II/III material. Notably, the dir contains **no separate Phase-2 or Phase-3 file**, no adversarial-creative document, no consolidated wandering-thoughts register. The §14 wandering-thoughts cadence appears in tiny inline form in the two reflection files only.

This is the smallest extraction in the sweep so far — the substance does not pad. Three weights: **(1) findings already adjudicated by FINAL/MANIFEST** (preserved here for trace-completeness, both `subsumed-by-FINAL — resolved by strengthening`); **(2) a single fresh observation** not carried into the FINAL (the auditor's `post-composition-consistency` Tier-1-transfer-exact watch-item flag, which never produced a finding because the walk stopped at end-of-Section-I-early); **(3) thin §14 wandering-thoughts plus initial-predictions calibration plus the process-feedback that became S21**.

---

## Part I — Findings already adjudicated (subsumed-by-FINAL/MANIFEST)

These appear in the WORKING dir as candidate-findings developing toward the FINAL §F1/§F2 list. Each is preserved here with its WORKING-dir provenance so the trail is recoverable; the MANIFEST 2026-05-16 entry is the truth-arbiter and these are already routed.

### F1-trail. IB $\beta$ parameter conflated with environment volatility $\rho$

- **WORKING-dir trail:** `02-reflections-IB-volatility.md:10–27` (the entire body of the second reflection file). Auditor's reasoning is unusually clean: quotes the segment, writes out the IB Lagrangian, locates the double-counting (volatility is *already* captured by the mutual-information terms via the joint distribution, so adjusting $\beta$ in response to $\rho$ is double-counting), and labels the mismatch as "epistemic mismatch: claimed as robust-qualitative but it is mathematically confused." The diagnostic — "the structural dependence on $\rho$ happens inside the expectation of the mutual information, not via $\beta$" — is the load-bearing sentence and identical to the FINAL §F1's framing. Auditor pre-staged the finding in `00-running-outline.md:12–15` as Finding 1.
- **Disposition (per MANIFEST 2026-05-16, Cluster B row "738192-F1/F2 resolved, the majority by strengthening"):** **`subsumed-by-FINAL — resolved by strengthening`**.
- **Verification (first-hand, current `src/`):** `01-aat-core/src/form-information-bottleneck.md:26–28` now reads "*It is tempting to claim that the trade-off parameter $\beta$ must be actively lowered… However, this is a double-counting error… The optimal $\phi^\ast$ will automatically discard this useless old information even if the agent's preference parameter $\beta$ remains completely constant. Therefore, adjusting $\beta$ reflects changes in the agent's internal cost of memory or computational capacity, not changes in environmental volatility.*" Strengthen-direction landed cleanly: the segment now names the double-counting explicitly *and* preserves the qualitative direction at the appropriate epistemic tier (`form-information-bottleneck.md:34` — "the qualitative direction (volatile favors compression, stable favors retention) is *robust-qualitative* across agent classes; specific functional forms are not derived here"). The fix did the harder work — distinguishing the structural mechanism (joint-distribution-mediated, native) from the agent's preference adjustment (cost-of-memory adjustment) — rather than just deleting the suspect paragraph. Cleanly resolved.

### F2-trail. `git checkout` misclassified as Level 3 counterfactual

- **WORKING-dir trail:** `01-reflections-section-I-early.md:23–27` (Section "4. Specific Finding / Concern: Level 3 Counterfactuals in Software"). Auditor's reasoning: Pearl's L3 is $P(y_{x'} \mid x, y)$, requiring rewinding to time $t$; `git checkout` resets *codebase state* but not *environment state* (developer's mind, external deps, time itself). Explicit acknowledgement of the strengthening direction: "I should see if `02-tst-core/src/obs-software-epistemic-properties.md` nuances this. If it doesn't, this is a finding." Promoted at `00-running-outline.md:17–20` as Finding 2. Note the auditor *did* test the strengthening direction explicitly (would TST's P2 already carry the scope condition?) — strengthen-before-soften discipline operating internally to the audit.
- **Disposition (per MANIFEST):** **`subsumed-by-FINAL — resolved by strengthening`**. The MANIFEST Cluster-B row cites the resolution method explicitly: "`git checkout` scoped-L3 regime in the canonical TST segment, SN-3 landed `3072667`/`2666eca`" (the SN-3 reference cross-links to Cluster-C's `2026-05-16` entry for `audit-2026-04-24-fresh-pass`; the same fix resolves both audits, hence the MANIFEST-noted parent co-owner direct-fix).
- **Verification (first-hand, current `src/`):**
  - `01-aat-core/src/def-pearl-causal-hierarchy.md:53` now scopes literal Level 3 to "*code-internal counterfactuals with deterministic outcomes*" via the ($\alpha$) deterministic-outcome / ($\beta$) cost-commensurate-replay / ($\gamma$) content-addressed-immutable conjunction — establishing the *configurational* (not metaphysical) uniqueness with named falsifiers. The domain table at `:63` was updated: software developer's L3 entry now reads "*literal for code-internal deterministic counterfactuals; proxy across the agent–environment boundary*."
  - `02-tst-core/src/obs-software-epistemic-properties.md:30–34` carries the full canonical P2 statement with the (α/β/γ) conjunction and the four named falsifier classes (formal-verification environments, simulated systems / digital twins, reproducible lab/robotics, blockchain). P2 §"Regime boundary" at `:119` makes the (a)/(b)/(c) conditions explicit at Working-Notes-grade.
  - Strengthen-direction landed cleanly: the framework now *both* keeps the literal-L3 claim where it genuinely holds (code-internal deterministic regime) *and* names the regime boundary precisely (the three conjunctive conditions plus the named falsifiers showing the uniqueness is configurational, not necessary). This is materially stronger than the bald 2026-04-25 claim *and* materially stronger than a simple soften would have been ("`git checkout` is just Level 2" would have lost the genuine structural distinctive that the auditor's own framing acknowledged). Strengthen-before-soften won here.

---

## Part II — Bigger-picture observations (none surfaced as §F in FINAL)

The 738192 FINAL has no §F-style "bigger-picture pondering" section. The auditor's `00-running-outline.md:27–30` reserves a "Phase 3 — Bigger-picture pondering" header that was never populated — the audit stopped after Section I early reflections, and no Phase-2 (`msc/` triangulation) or Phase-3 (synthesis) work was executed. The FINAL's only non-finding content is the brief process-feedback section endorsing the de-novo-audit-instructions design.

**Disposition:** The process-feedback content is **subsumed-by-ledger S21** (sentiment row, "De-novo-audit-instruction design is landing"; cited content: "predictions-before-reading forced verification mode"; "OUTLINE-first effective"; "instructions are excellent"). No outstanding §F-level observations to route.

---

## Part III — Fresh material the FINAL didn't carry forward

Only one observation in the WORKING dir wasn't carried into the FINAL or to the ledger. The dir's brevity makes this single-item fresh part honest — there is not more to find here.

### Fresh-1. The `post-composition-consistency` Tier-1-transfer-exact watch-item

- **WORKING-dir provenance:** `01-reflections-section-I-early.md:17–18` (Section "2. Cross-segment consistency"):

  > *"`post-composition-consistency.md` references Tier 1/2/3 agents and the composition bridge lemma. It states that for Tier 1, Section I/II results transfer exactly. This places a massive burden on `#form-composition-closure`. I need to watch closely when I read Section III to see if this transfer is genuinely exact or if it requires unstated assumptions (like perfect communication or zero latency)."*

- **Observation:** the auditor flagged a structural watch-item — *whether the Tier-1 "transfers exactly" claim in `post-composition-consistency` is honored by the composition machinery in Section III without unstated assumptions* — but never tested it because the audit stopped after Section I-early reflections. The audit walked far enough to surface the watch-item but not far enough to either confirm or refute it. The watch-item rhymes with concerns surfaced by other audits in the broader cohort (per the MANIFEST, **F5-trail (471203) `post-composition-consistency` depends** is `subsumed-by-FINAL — already routed` to PROPOSALS SP-6 + TODO:149 + F-A cluster from 584721/742613), but it is not strictly the same shape — 471203's concern was about the postulate's depends-list incompleteness *internal* to the postulate's own derivation work; this is about whether the *consumers* in Section III honor the postulate's Tier-1 transfer claim without unstated assumptions. The two are sibling concerns but ask different questions.
- **Naming/lineage note:** "Tier 1/2/3 agents" was the **pre-2026-05-09 numbering** for what is now **GUC Class 1 (Separated) / Class 2 (Partial, formerly Class 3 Operational) / Class 3 (Coupled, formerly Class 2 Undirected)** per the CLAUDE.md §"Goal-Update Coupling Class numbering changed 2026-05-09" warning. The watch-item is unchanged in substance — does the framework's composition machinery honor GUC Class 1 transfer-exactness without unstated assumptions? — but a follow-on should translate "Tier 1" → "GUC Class 1 (Separated)" before consuming the WORKING-dir text verbatim.
- **Strengthen-first framing:** the strengthen direction (if pursued) is to attempt a *no-go* under realistic communication / latency assumptions: identify the smallest set of additional assumptions that breaks Tier-1 transfer exactness, and either prove transfer-exactness is robust to their absence or surface the specific failure modes. The audit didn't reach this, but the watch-item is well-formed enough to spike. Softening (relabeling Tier-1 transfer as "approximately exact") would be the fallback only after the strengthening attempt honestly failed.
- **Suggested disposition:** `research-seed` — Section III composition-closure stress-test against GUC Class 1 transfer claims. Cross-reference 471203 F5 / SP-6 / TODO:149 / F-A cluster (sibling concerns on `post-composition-consistency`'s derivation hierarchy); cross-reference the broader composition-closure work tracked under PRACTICA. Not a graduation blocker.
- **Caveat on weight:** this is one paragraph of watchful-pre-reading-not-yet-tested cognition in a dir that produced no Section III work first-hand. The weight is light — it's an idea-seed, not an audit-tested observation. If the broader cohort has already covered this ground (likely, given F-A cluster activity), then this is `subsumed-by-existing-tracking` rather than genuinely fresh.

---

## Part IV — Predictions calibration register

The `00-initial-predictions.md` file makes ~12 falsifiable predictions across topology / contents / openness / overclaim-risk / novelty / findings-type. Because the audit stopped after Section I-early reflections, the calibration record is **partial** — most predictions were never tested against evidence in the WORKING-dir reflections.

### Predictions tested (in the two reflection files)

- **"Section I will brush over the exact mechanics of continuous vs discrete event arrivals"** — *not confirmed.* Auditor's first-reflection notes: "the formulation is very clean. The `scope-agency` and `scope-adaptive-system` segments are very precise in their inclusion/exclusion criteria." (`01-reflections-section-I-early.md:14–15`). The auditor explicitly downgraded this prediction by observing the framework's discipline.
- **"Math errors or sign errors in the appendices"** — *not surfaced by this audit.* Audit stopped before appendices. Open prediction.
- **"Epistemic status mismatches: claims labeled as `exact` or `derived` that actually hinge on `heuristic` assumptions or unverified hypotheses"** — *partially confirmed via F1.* The IB-volatility paragraph was labeled `robust-qualitative` but the auditor found the *underlying mechanism* mathematically confused, not just qualitatively softer than the label admitted. So the prediction is in the right zone (label-vs-status mismatch), but the F1 instance is about *mathematical confusion* not about *label-vs-content tier mismatch* — overlapping but distinct. Worth noting: the FINAL §F1 framing converges with the auditor's "epistemic mismatch" diagnostic, but the resolution-by-strengthening preserves the qualitative claim at the correct tier rather than just downgrading the label. The strengthening-by-mechanism-clarification move sharpens the prediction's diagnostic.
- **"Section II's claims about updating strategy edges based on mismatch might overclaim what can be observationally identified without explicit interventions"** — *not tested* (audit stopped before Section II edge-update segments).
- **"`git checkout` overclaim about counterfactual access"** — *confirmed via F2* (though the prediction wasn't named in `00-initial-predictions.md` as such — the L3-overclaim category falls under the audit's general "Causal Identifiability" overclaim-risk theme at `00-initial-predictions.md:25`).

### Predictions untested (audit stopped early)

- "**Scope Propagation:** directed separation will not be consistently carried forward into Section III or all the appendices" — untested. Other audits in the broader cohort have probed this (e.g., 471203 §F3, the modularity-state-dynamics cycle); 738192's audit did not reach the test.
- "**Causal Identifiability:** Section II's strategy-edge-updating overclaims" — untested.
- "**Discrete-to-Continuous Bridge:** fluid limit assumptions (GA-5) glossed over" — untested.
- "**Class 2 (LLM) coupling-of-epistemic-and-purposeful is the most fragile section**" — untested.
- "**$N$-agent scaling in composition (beyond dyads) is open**" — untested. (Confirmed open in broader project state via PRACTICA + spike-composition-scaling-N work; not from this audit.)
- "**Concrete operationalization of strategic disturbance ($\rho_\Sigma$) is open**" — untested.
- "**The connection between persistence conditions and IB as unified metric is the most novel and consequential**" — untested directly, though the audit's encounter with IB material in the F1 work is *adjacent* — auditor read the IB Lagrangian and applied standard IB theory cleanly to flag the conflation. The framework's IB use was rigorous-enough that the auditor's prediction (IB-as-novel-piece) gets *indirect* support: the auditor would have surfaced more problems had the IB usage been sloppy in ways beyond the volatility conflation.
- "**Composition bridge lemma relies on contraction assumptions violated in adversarial/chaotic coupling regimes**" — untested. The auditor's Fresh-1 watch-item (Tier-1-transfer-exactness with unstated assumptions) is the precursor that *would* have been tested in a Phase-2 walk.

### Withdrawn-candidate trail

None. The audit was short enough that no candidate-finding was surfaced-then-withdrawn under burden of proof. The L3 finding in `01-reflections-section-I-early.md:23–27` was explicitly hedged ("I should see if `02-tst-core/src/obs-software-epistemic-properties.md` nuances this") — the auditor *did* test the strengthening direction conceptually before promoting the finding to the running outline (`00-running-outline.md:17–20`). Whether the test was actually executed by reading `02-tst-core/src/obs-software-epistemic-properties.md` is unclear from the WORKING-dir record; the FINAL doesn't cite that segment, suggesting the auditor promoted the finding without verifying TST's nuance — which the post-FINAL strengthening fix (SN-3 landed `3072667`/`2666eca`) ultimately *added* the nuance the auditor's framing implicitly called for. So the audit-as-instance-of-the-theory operated correctly: surface the finding under burden of proof; downstream verification + strengthening close it cleanly.

### Predictions-vs-evidence summary

The calibration record is *thin*: only 2 of ~12 predictions tested first-hand by this audit. Of the 2 tested, both produced findings that landed in the FINAL and were resolved by strengthening. The auditor's `00-initial-predictions.md` framing was diagnostic-quality — the IB-volatility finding hit the "epistemic-status-mismatch" prediction zone; the L3 finding hit the "causal-identifiability-overclaim" prediction zone. The audit demonstrated that the predictions-before-reading methodology *works* on the small sample executed — `S21`'s ledger sentiment ("predictions-before-reading forced verification mode") is the auditor's own correct calibration of their methodology. The fact that 10/12 predictions went untested is a function of audit scope, not of methodology.

---

## Part V — §14 Wandering Thoughts: ideation register, theme-grouped

**Framing note:** Per `doc/de-novo-audit-instructions.md` §4.4, the §14 wandering-thoughts cadence is a *per-segment* prompt, scattered inline with reflections. For this dir specifically, the audit predates the elaborated §4.4 numbered-prompt structure visible in heavier audits like 471203 — 738192's reflection files use a small section-numbered structure (1. Predictions vs Evidence / 2. Cross-segment consistency / 3. Math verification / 4. Specific Finding / 5. What errors to watch for / 6. Next steps) rather than the §4.4 ten-prompt structure. The wandering-thoughts content in this dir is consequently sparse — there's a §"5. What errors should I watch for?" item in `01-reflections-section-I-early.md` and a §"3. Next steps" in `02-reflections-IB-volatility.md`, both procedural rather than wandering-thoughts ideation.

Three small ideation-shaped paragraphs are extractable; they're light, theme-grouped below.

### Theme A — Cross-segment-burden observation (Fresh-1's precursor framing)

`01-reflections-section-I-early.md:17–18` (already extracted as Fresh-1) carries the auditor's only paragraph approaching cross-segment ideation: the "Tier 1 transfer places a massive burden on `#form-composition-closure`" observation. This is a *structural* observation (X claim Y places burden Z on segment W) rather than a wandering-thoughts-from-segment-content observation, but it is the closest thing this dir has to consciousness-infrastructure-style or epistemic-architectural-style ideation.

**Suggested disposition:** already routed as Fresh-1 above. Not a separate ideation item.

### Theme B — Audit-as-instance-of-the-theory (self-aware methodology paragraph)

The FINAL's process-feedback section reads:

> *"The instructions in `de-novo-audit-instructions.md` are excellent. They successfully forced me out of 'charitable reading mode' (where an LLM naturally assumes the text is correct and tries to summarize or align with it) and into 'verification mode.' By requiring me to write out predictions before reading the core claims, I established a critical baseline that made it much easier to spot when the text strayed into double-counting or overclaiming. The suggestion to read the `OUTLINE.md` files first to understand the topology before diving into the mathematical core was very effective."*

This is the audit's only meta-observation about its own methodology — the methodology working as designed. It rhymes with the 471203 §G feedback and is structurally Theme G ("audit-as-instance-of-the-theory") material from the pilot. The auditor describes the predictions-before-reading mechanism explicitly: it forced verification mode, which made the conflation visible.

**Suggested disposition:** **subsumed-by-ledger S21** (sentiment row). The content is already on the ledger; the per-instance trail here is `process/instruction-feedback` if a future revision of `doc/de-novo-audit-instructions.md` wants worked examples of how the predictions-first methodology lands.

### Theme C — Consciousness-infrastructure connections

None. The 738192 audit did not engage with `04-eli-core/`, `03-llm-core/`, or `chronica`-related substrate material. The auditor's reading-frame was mathematics-and-overclaim-detection, not consciousness-infrastructure. The dir contains zero paragraphs of this theme.

### Theme D — Naming brainstorm

None. No naming observations in the WORKING dir; the audit's reading was substance-targeted, not surface-form-targeted.

### Theme E — Cross-domain operationalization

None substantive. The L3 finding (F2) is *adjacent* — it engages with the software-as-calibration-laboratory framing — but the auditor's framing was overclaim-detection ("`git checkout` falls short of true L3") not operationalization-extension. The downstream strengthening fix *did* sharpen the cross-domain framing (the (α/β/γ) conjunction with named falsifiers makes the framework's cross-domain position more defensible), but that's the project's response, not the WORKING dir's contribution.

### Theme F — Adversarial-creative challenges with strengthening attempts

None. The WORKING dir has no analogue of 471203's `adversarial-creative-challenges.md`. The audit was short enough that no adversarial-creative document was authored.

### Theme G — Phenomenology / process self-observation

Minimal. The FINAL's process-feedback paragraph (Theme B above) is the only meta-observation. No within-audit phenomenological calibration register (no engagement-shifts logged; no "calibrated quiet vs numbed quiet" distinction; no break-protocol entries).

### Wandering-thoughts theme summary

Of the seven themes the pilot validated (consciousness-infrastructure, epistemic-architectural contribution, pacing/phenomenology, naming-brainstorm, cross-domain operationalization, adversarial-creative-strengthening, audit-as-instance-of-the-theory), this audit produced *one substantive theme* (Theme G — audit-as-instance-of-the-theory, already on the ledger as S21) and one *thin* theme (Theme A — cross-segment-burden observation, already promoted as Fresh-1). The other five themes are blank. This is the right outcome given audit scope; it does not reflect a deficit in the auditor's work — the audit produced exactly what its scope warranted, two clean findings and clear methodology endorsement.

---

## First-Pass Scrutiny

Per the brief: for each finding above, name which segments in `01-aat-core/src/` / `02-tst-core/src/` / `03-llm-core/src/` / `04-eli-core/src/` I (the extraction agent) read first-hand to evaluate it, and a per-finding disposition. Honest "didn't have time to verify X" allowed and expected.

### Part I findings (already-adjudicated trail)

| Trail ID | Disposition | First-hand verification |
|---|---|---|
| F1-trail (IB-$\beta$-vs-$\rho$ conflation) | `subsumed-by-FINAL — resolved by strengthening` | Verified `01-aat-core/src/form-information-bottleneck.md:17–28, 34, 50` first-hand: the double-counting paragraph is now present and explicit ("It is tempting to claim… However, this is a double-counting error… The optimal $\phi^\ast$ will automatically discard this useless old information even if the agent's preference parameter $\beta$ remains completely constant"); the qualitative-direction claim is correctly retired to the `robust-qualitative` tier at `:34`; the segment Epistemic Status block clearly distinguishes the *exact* IB-as-applied-theorem core from the *robust-qualitative* $\beta(\rho, \pi)$ dependence claims. Strengthen-first landed; cleanly resolved. |
| F2-trail (`git checkout` L3 misclassification) | `subsumed-by-FINAL — resolved by strengthening` | Verified `01-aat-core/src/def-pearl-causal-hierarchy.md:53` first-hand: literal L3 now scoped to "*code-internal counterfactuals with deterministic outcomes*" with the (α/β/γ) conjunction and named falsifiers; domain table at `:63` updated. Verified `02-tst-core/src/obs-software-epistemic-properties.md:30–34, 119` first-hand: canonical P2 statement with the three conjunctive conditions and four named falsifier classes (formal-verification environments, simulated systems / digital twins, reproducible lab/robotics, blockchain), plus the Working-Notes-grade (a)/(b)/(c) regime-boundary breakdown. Strengthen-first landed materially stronger than soften would have; the *configurational not necessary* framing with named falsifiers is the distinctive sharpening. Cleanly resolved. |

### Part II (no §F findings)

No Part II items to verify — the FINAL has no §F section. Process-feedback is ledger S21 (`subsumed-by-ledger`).

### Part III findings (fresh; first-hand-verified or honestly-deferred)

| Fresh-ID | Disposition | First-hand verification |
|---|---|---|
| Fresh-1 (Tier-1-transfer-exact watch-item from `post-composition-consistency`) | `research-seed` (composition-closure stress-test against GUC Class 1 transfer claims) | Read the WORKING-dir paragraph first-hand (`01-reflections-section-I-early.md:17–18`). Did **not** read `01-aat-core/src/disc-composition-consistency.md` first-hand to verify current Tier-1-transfer claim language. Did **not** check whether the F-A cluster / SP-6 / TODO:149 / 471203-F5 routing already covers this specific sibling concern. **Deferred — honest "didn't have time."** Joseph or downstream routing should spot-check whether the watch-item is genuinely fresh or subsumed-by-existing-tracking. Translation needed before consumption: "Tier 1" → "GUC Class 1 (Separated)" per CLAUDE.md naming-change note 2026-05-09. |

### Part IV (predictions register) and Part V (wandering thoughts)

These are not "findings" with `src/`-level dispositions per se — they're cognition-flow material. First-pass scrutiny:

- **Predictions register (Part IV)** — read first-hand from `00-initial-predictions.md` and the two reflection files. Calibration record is honest but partial (2/12 predictions tested, 10 untested due to audit scope). No additional `src/` verification needed for the record itself; the untested 10 don't graduate into anything routable from this audit alone.
- **Wandering thoughts (Part V)** — five of seven pilot themes are blank for this audit. The two non-blank themes (Theme A — cross-segment-burden, already Fresh-1; Theme B — methodology-self-observation, already ledger S21) are accounted for. No new ideation items to route from this dir.

### Honest coverage summary for this extraction

**Read first-hand from the WORKING dir:** all 4 files in full (`00-initial-predictions.md`, `00-running-outline.md`, `01-reflections-section-I-early.md`, `02-reflections-IB-volatility.md`). Total dir size ~12 KB — every paragraph read.

**Read first-hand from `src/` for verification:**
- `01-aat-core/src/form-information-bottleneck.md:17–28, 34, 50` (F1 verification — double-counting paragraph, tier-distinction in Epistemic Status, variational-bridge connection)
- `01-aat-core/src/def-pearl-causal-hierarchy.md:11–13, 33–53, 63` (F2 verification — scoped-L3 framing, three conjunctive conditions inline, domain table)
- `02-tst-core/src/obs-software-epistemic-properties.md:30–34, 119` (F2 verification on TST side — canonical P2 statement, regime-boundary Working Notes)

**Read first-hand from `audits/`:**
- `audits/.integrated/audit-738192-FINAL.md` (full — both findings + process-feedback)
- `audits/.integrated/MANIFEST.md` (Cluster B entry 2026-05-16, 738192 row + adjacent cluster context including SN-3 cross-reference to Cluster C)
- `audits/polish-and-sentiment-ledger.md` (S21 row + S16 cohort-row context — both reference 738192)
- `audits/audit-findings-471203.md` (pilot — full extraction, used as shape-template)

**Read first-hand from governance docs:**
- `CLAUDE.md`, `doc/audit-routing-instructions.md` (§2–§5, §8), `doc/de-novo-audit-instructions.md` (§4.4 reflection-prompt structure for Theme-Part V framing)

**Deferred verifications (honestly "didn't have time" — flagged for Joseph routing):**
- Fresh-1: did not read `post-composition-consistency.md` first-hand; did not cross-check whether the Tier-1-transfer-as-Section-III-burden concern is already covered by the F-A cluster / SP-6 / TODO:149 / 471203-F5 routing. Recommend Joseph or downstream routing decide whether this is genuinely fresh or `subsumed-by-existing-tracking`.

### Strengthen-first integration recommendations (per brief item 3)

- **F1, F2** are both *retrospective* — already resolved by strengthening per the MANIFEST. The strengthening directions chosen (preserve the qualitative claim at the correct tier rather than delete the paragraph; scope the L3 regime via (α/β/γ) conjunction with named falsifiers rather than demote to L2) are materially stronger than soften would have been. This is the canonical worked example of the discipline operating: the audit surfaced two clean findings; the project's response strengthened in both cases rather than softening; the outcomes preserve framework distinctives that softening would have lost.
- **Fresh-1** (if genuinely fresh and not subsumed) is a *strengthening direction*: attempt a no-go on Tier-1-transfer-exactness under realistic communication/latency assumptions, or prove robustness. Spike-shaped. The fallback (relabel as "approximately exact") is the soften — but the strengthen-first attempt should fire first.

No soften-recommendations identified anywhere in the WORKING dir. The audit's posture was clean.

---

## Frame-defects / instructions-clarity observations

None encountered with the extraction frame on this slice. The pilot's frame transferred cleanly. Two observations specific to this dir's character (small dir, short audit) that may be useful for the parent agent's calibration of the sweep:

1. **Dir size correlates with substance, not just length.** This dir produced 4 files / ~12 KB and the FINAL produced 2 findings + process feedback. The extraction is correspondingly short (~8-9K tokens vs the pilot's ~25-30K). The brief's "anchor on the dir's substance, not a target" framing is correct; this extraction does not pad to look fuller than the substance is. Heavier dirs (heavier walks, longer reflections, separate adversarial-creative documents) will be 2-3× this length.

2. **§14 wandering-thoughts thinness is itself a fact about the audit.** This dir lacks the §4.4 ten-prompt cadence visible in pilot 471203. The reflection files use a smaller section-numbered structure (predictions / cross-segment / math / specific finding / errors-to-watch / next steps) — six small headers rather than ten reflection prompts. This may be because the `de-novo-audit-instructions.md` document had different (less elaborated) reflection-prompt structure at 2026-04-25 than at the later cycles; it may also be the auditor (Gemini CLI) executing a compressed version of the cadence. Either way, the thinness is faithful to the actual audit-product, not an extraction-side compression. Themes C, D, E, F (consciousness-infrastructure, naming, cross-domain operationalization, adversarial-creative) being blank for this dir is not a defect but a reading of what was actually produced.

---

*End of extraction. The original WORKING dir at `audits/AUDIT-WORKING-738192/` is preserved unmodified per the brief.*
