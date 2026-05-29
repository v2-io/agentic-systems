# Gem-hunt adjudication — audit 738192

*Adjudicator: Claude Opus 4.8 (1M), 2026-05-29. Report-only — no canon edits/moves/commits.*
*Source slice: `audits/audit-findings-738192.md` (itself the FINAL extraction of the 738192 de-novo cycle — Gemini CLI, 2026-04-25). Gold dir `audits/AUDIT-WORKING-738192/` present (4 files, ~12 KB); NOT opened — under the separate consult-Joseph gate. Worked only from the FINAL extraction per brief.*

## TL;DR

This audit is small and **already fully mined**. Both FINAL findings (F1 IB-$\beta$/$\rho$ conflation, F2 `git checkout` L3 misclassification) are landed-by-strengthening and verified-in-canon by the extraction agent. The process feedback is on the ledger as S21. The one item the extraction agent honestly *deferred* — Fresh-1, the Tier-1-transfer-exact watch-item — I verified first-hand against current canon, and it is **comprehensively answered**: it is not a research-seed, it is `subsumed-by-canon`. There is **no un-captured theory gem** in this slice. The honest, fully-successful outcome here is "already in canon/ledger, here are the loci," plus a corrected disposition on Fresh-1.

---

## (A) Ready-to-land gems

**None.** Nothing in this slice carries content that would have to be re-derived later and is not already present (and stronger) in canon.

## (B) Research-seeds

**None.** The single candidate research-seed (Fresh-1) is dissolved on first-hand inspection — see "Corrected dispositions" below. Recording a strengthening spike here would be manufacturing a gem; the strengthening the auditor implicitly wanted is already done in canon.

---

## Already-routed, verified correct (no action)

### F1 — IB trade-off parameter $\beta$ conflated with environment volatility $\rho$
- **Disposition:** `subsumed-by-FINAL — resolved by strengthening` (MANIFEST 2026-05-16, Cluster B). Confirmed correct.
- **Locus (first-hand):** `01-aat-core/src/form-information-bottleneck.md` — the double-counting paragraph is present and explicit; the qualitative direction (volatile favors compression, stable favors retention) is retired to `robust-qualitative` tier with the *exact* IB-as-applied core kept separate. The fix did the harder work (distinguish joint-distribution-native mechanism from cost-of-memory preference adjustment) rather than deleting the suspect claim. Strengthen-first landed cleanly.
- **Not a gem:** the *content* is in canon and stronger than the audit's framing.

### F2 — `git checkout` misclassified as Pearl Level 3
- **Disposition:** `subsumed-by-FINAL — resolved by strengthening` (MANIFEST Cluster B; SN-3 landed `3072667`/`2666eca`). Confirmed correct.
- **Loci (first-hand):** `01-aat-core/src/def-pearl-causal-hierarchy.md:53,63` (literal L3 scoped to code-internal deterministic counterfactuals via the (α/β/γ) conjunction + named falsifiers; domain table updated) and `02-tst-core/src/obs-software-epistemic-properties.md:30–34,119` (canonical P2 with four named falsifier classes + regime-boundary). The *configurational-not-necessary* framing is materially stronger than the soften ("git checkout is just L2") would have been — it preserves the genuine structural distinctive.
- **Not a gem:** in canon, stronger.

### Process feedback (de-novo-instruction design)
- **Disposition:** `subsumed-by-ledger S21` (sentiment row, "De-novo-audit-instruction design is landing"). Confirmed present at `audits/polish-and-sentiment-ledger.md:57`. Not theory content; correctly routed.

### Predictions register (Part IV) + Wandering Thoughts (Part V)
- 2 of ~12 predictions tested first-hand by the audit (both became F1/F2); 10 untested due to early audit stop. The untested 10 graduate into nothing routable *from this audit* — several name questions the broader cohort/PRACTICA already tracks ($N$-agent composition scaling; $\rho_\Sigma$ operationalization; scope-propagation into Section III). No fresh content.
- Five of seven wandering-thoughts themes blank; the two non-blank (cross-segment-burden = Fresh-1; methodology-self-observation = S21) are accounted for. No ideation gem.

---

## Corrected disposition (a previously-suggested disposition that is now wrong against canon)

### Fresh-1 — "Tier-1 transfers exactly" watch-item on `post-composition-consistency`

- **Extraction-agent disposition:** `research-seed` — "Section III composition-closure stress-test against GUC Class 1 transfer claims," with an explicit honest deferral ("did NOT read the segment first-hand; did NOT check whether F-A cluster / SP-6 / TODO:149 / 471203-F5 already covers it").
- **Corrected disposition (first-hand):** **`subsumed-by-canon` — the watch-item is comprehensively and specifically answered.** It is not a live research-seed.
- **What the auditor worried about (verbatim trail):** whether the Tier-1 "Section I/II results transfer *exactly*" claim "is genuinely exact or if it requires unstated assumptions (like perfect communication or zero latency)," and that the claim "places a massive burden on `#form-composition-closure`."
- **Why it is answered — named loci (read first-hand):**
  - **The "unstated assumption" is now a *stated, named, proved-strictly-stronger* condition.** `form-composition-closure.md:26,149,170–172,200–206`: Tier-1 transfer is explicitly conditional on the **incremental sector bound (DA2'-inc / strong monotonicity)**, which is proved *strictly stronger than (A4)* via an **exhibited counterexample** — "oscillatory corrections that are globally inward-pointing but locally non-monotone" (`:172` row "Proved"; `:200` Epistemic Status; spike `spike-bridge-lemma-contraction.md` §4.1). That counterexample *is* the "are you sure Tier-1 transfers exactly?" stress-test the auditor wanted to run — already run, with the boundary characterized.
  - **The Tier-1 = "exactly" / Tier-2 = "local degradation" / Tier-3 = "per-domain" taxonomy is the honest scoping of "applies at every level."** `disc-composition-consistency.md:44,74,76` states it as exactly that ("the sharpest scoping of 'every result applies at every level' — it applies at every level *for Tier 1 composites*, degrades gracefully for Tier 2, and holds per-domain for Tier 3"). The "massive burden on `#form-composition-closure`" the auditor flagged is discharged: the burden is carried by the named (A1)–(A4) + (P1)–(P3) + DA2'-inc apparatus, with a Working-Notes strengthening-attempt record at `disc-composition-consistency.md:99`.
  - **The auditor's specific "perfect communication / zero latency" worry is the closure-defect / coordination-cost machinery.** `form-composition-closure.md:20–28` (closure defect $\varepsilon^\ast$ as the irreducible cost of imperfect composition, entering the composite persistence inequality as effective disturbance) and `disc-composition-consistency.md:52,54,87–92` (coordination costs $C_i$, $\rho_{\text{eff}} = \rho_{\text{ext}} + \varepsilon^\ast\nu_c$, Brooks's-Law instantiation). Imperfect communication/latency does not silently break exactness — it shows up quantitatively as $\varepsilon^\ast$ and coordination overhead against the composite's own persistence threshold.
  - **The strengthen-first move the auditor's framing implied is already done.** `disc-composition-consistency.md:48–54,99`: the heuristic "macro-timescale bounded below by slowest sub-agent" was *attacked and bound to closed forms* — (CC-parallel) $\lambda_c=\min_i\lambda_i$ *exact* under blockdiag metric, (CC-cascade) same up to coupling-gain, (CC-feedback)/(CM2-M) heterogeneous closed-form inequality — via the DA2'-inc ≡ (CT2)-at-$M=I$ equivalence in `#result-contraction-template`. Tier-2/3 residual is what the attempt honestly could not eliminate, and is marked heuristic/discussion-grade.
- **Naming note (confirms staleness, not freshness):** the audit's "Tier 1/2/3 *agents*" is pre-2026-05-09 GUC numbering; the live canon "Tier 1/2/3" in these composition segments is the **contraction-quality** tier (T1 global / T2 local / T3 per-domain), a *different* axis from GUC class. The extraction agent's worry that "Tier 1" needed translation to "GUC Class 1" is itself a sign the watch-item was reasoning at one remove from the segments; in canon the relevant tier is the contraction tier, and it is fully built.
- **Sibling-tracking cross-check (per the extraction agent's deferred question):** even setting aside the direct answer above, the broader composition-closure program (471203-F5 → PROPOSALS SP-6 + TODO:149 + F-A cluster; $N$-agent scaling re-typed/resolved per `form-composition-closure.md:185,192` and CHANGELOG 2026-05-19) covers the consumer-side concern. So Fresh-1 is doubly closed: directly by the DA2'-inc apparatus, and via existing tracking.
- **Hard-constraint check (would we have to re-derive this later?):** No. The math the watch-item gestured at — the precise condition under which Tier-1 transfer is exact, and what breaks it — is *in canon, derived, with the boundary counterexample exhibited*. Nothing here would need re-derivation.

---

## Valueless / superseded in this slice

- The Part I "findings-already-adjudicated trail" (F1-trail, F2-trail) is trace-completeness archaeology — correctly preserved, nothing to land.
- Predictions Part IV / Wandering-Thoughts Part V: faithful to a short audit; no theory content beyond what is routed.

## Summary judgment

Careful, complete, and negative on new gems: **0 ready-to-land, 0 research-seeds.** The slice's two findings and its sentiment are correctly routed and verified-stronger in canon. The lone open item (Fresh-1) was over-classified as a research-seed at extraction time and is in fact `subsumed-by-canon`; the specific strengthening it pointed at (exact-transfer conditions + the breaking counterexample) is already derived in `form-composition-closure.md` / `disc-composition-consistency.md`. This is the "every audit's flagship had drifted out from under its label" pattern operating in the *benign* direction — a deferred research-seed that, on first-hand reading, is already closed. Landings/verification remain Joseph's; the gold dir was not touched.
