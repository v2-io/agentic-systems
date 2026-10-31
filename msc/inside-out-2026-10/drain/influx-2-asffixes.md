# Influx drain: sweep-2 `ASF-FIXES*` and the unread reports R34–R55

> **KR: G.2** in `../INTENT.md` (*stranded additions are landed at honest tier or set aside with a recorded reason*). Canon defects go to **C.1** (C.3 for contradictions between segments, C.4 for open strengthenings); terminology to **F.1/F.4**; citations to **F.2/F.3**. Top intent: *"Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself."* After a compaction, re-read `../INTENT.md`, then this file.

*Drain agent `drain-influx-2-asffixes` (Opus 5.5), 2026-10-30, for the lead, who folds this into `influx-2.md`; integrators work from the ledger items it names. Sources: `~/src/AISI-responses/influx/sweep-2-raw/ASF-FIXES*.md` (five files, 1,432 lines) and the sweep's reports R34–R55 (`IDEATION.md`, about lines 2940–4400).*

## Questions, with the reading I am proceeding on

*(none yet)*

## Method

- `ASF-FIXES.md` (R01–R06, the extractor's summary), `ASF-FIXES-mine-01-16.md` (R01–R16), `ASF-FIXES-part2.md` (R17–R32), `ASF-FIXES-part3.md` (R33–R48), `ASF-FIXES-part4.md` (R49–R63) read whole. `part2.md` lines 436–472 (R05, R06) and `part3.md` lines 242–364 (R07–R11) are byte-identical copies of `mine-01-16.md` sections (checked with `diff`); counted once.
- No sweep agent actually edited asf: every "fixed" line in the five files says "none found" or "not edited". So there were no August edits whose survival needs checking; the work is the PROPOSED, TRACKED and UNRUN entries, and the open questions the reports restated.
- Many entries restate an open question already written in a segment's own Working Notes. Those are in canon (as Working Notes) and belong to the Working Notes drain lanes (I.5, `wn-*.md`); I record them as **WN** and open nothing, unless the report adds something the Working Note lacks.
- `PROPOSALS.md`, `TODO.md` and `spikes/PROPOSED*.md`, which the reports cite by line, were imported into the ledger (I.3). An entry those files carried is **LEDGER** with the item id, after I confirm the item exists.
- Every canon claim is checked at asf `main` (HEAD when checked is named per section). Before opening an item I checked `vsect open segment:<slug>` and grepped `items/` for the slug and key phrases.
- Dispositions: **IN** (in canon at HEAD, where), **DEFECT** (canon defect still present; item), **ADD** (true or worth having, absent; item at honest tier), **LEDGER** (already an open item; source added with `vsect raise`), **WN** (stated in a segment's Working Notes; WN drain's), **MOOT** (overtaken), **ASIDE** (set aside, reason given).
- Split: a helper (`drain-influx-2-asffixes-r34-55`) drains R34–R55 whole (both their `ASF-FIXES` entries and their `IDEATION.md` reports) into `influx-2-asffixes-r34-55.md`. I drain the `ASF-FIXES` entries of R01–R33 and R56–R63.

## Dispositions, R01–R33 and R56–R63

Checked at asf `main` `782342c2`–`1f8240df` (2026-10-30, evening). "WN :n" means the line of the segment's Working Notes at HEAD.

### Part I, Chapters 1–4 and Meta-Architecture I (R01–R12)

| Source entry | Disposition | Where / item |
|---|---|---|
| R01, R02, R42 item 5, R51: SP-30, fully observed state with unknown law wrongly excluded; `example-bandit`'s silent hyperstate choice | IN (A.1 landed today) | `#def-agent-environment:13`, `:39` (tabular RL inside); `#scope-adaptive-system:17`, `:19`, item (c) at `:50` (bandit and Q-learner in); `#example-bandit:42` now names state vs law under the invariance cut. SP-30 has no live item, as it should not |
| R01, R03, R08, R58, R59, R60: SP-27 fork/rollback introspective undetectability | LEDGER | `proposals-surfaced-2026-05-29-qualitative-gem-hunt-14e1` (SP-27) and `influx-non-forkability-tier`, which records that the mechanism as SP-27 states it ("lossiness") is refuted by 731548/05:12 and the conclusion survives in a stronger form. Source raised on both |
| R01: boundary one-way (Omega cannot write to the agent) as a second constitutive commitment | LEDGER | `boundary-integrity-second-constitutive-commitment` |
| R01: TRACTUS vs CHRONICA, two cross-attested records | LEDGER | `tractus-chronica-split-for-logogenic-implementation` |
| R01: $T$ "cannot be adversarial white noise", unnamed learnability assumption | WN (`#def-action-transition` WN :71). The extreme case is now answered in the body: `#scope-adaptive-system:19`'s third exclusion (a hidden state drawn afresh each step) puts white-noise worlds outside. What remains open is a rate, not membership; nothing to open | — |
| R01: equation tag `[Postulate]` vs `[Definition]` on `def-action-transition` / `def-observation-function` | LEDGER | `imported/spikes-proposed-equation-tag-vs-content-type-drift-for-o-9df0` |
| R01, R02: gold-lift coverage of Ch. 1; 308172 and 419628 are naming-vote audits | ASIDE: a coverage fact about August's lift, superseded by I.5 (lifting into Working Notes stops) and by `give-the-unlifted-audit-gold-a-destination-wave` | — |
| R01: `#form-information-bottleneck` `status: exact` mixing an exact imported theorem with a weaker sub-claim (613842) | LEDGER | `ib-exactness-deterministic-vs-kernel`, `influx-ib-beta-rho-and-exactness` |
| R02: "nominal agent" / "nominal coupling" collision | LEDGER, still present at HEAD (`#scope-agency:19`, WN :91) | `todo-nominal-denotes-opposite-scope-membershi-c7a1` (F.1) |
| R03: Tishby & Zaslavsky 2015 cited for "IB is the rate-distortion specialization of variational free energy" | Misattribution IN-fixed: `#form-information-bottleneck:56` now gives the variational bound to Alemi et al. 2017 and Tishby & Zaslavsky only the deep-learning instantiation. Two residues: WN :77 still asks for the check the body already made (stale; WN drain's), and the sentence's own claim, "the IB objective … is the rate-distortion specialization of the variational free energy", is stronger than the correspondence `:56` then describes ("related under the Markov-chain factorization"). Raised on the IB items | `influx-ib-beta-rho-and-exactness` (raise) |
| R03: Gate-1 stage inconsistency, `def-model-sufficiency` `deps-verified` depends on `form-information-bottleneck` `draft` | ASIDE: still true at HEAD, but stage gating is under reconsideration and the stage ladder is leaving the outline display (H.2); `bin/lint-outline` reports stage drift warning-only | — |
| R03: predictive sufficiency vs causal confusion (963715 gold); does `#def-value-object` deliver the back-door machinery `#def-model-sufficiency` promises (374162) | IN | `#def-model-sufficiency:16`, `:45` (predictive not causal; one-step interventional sufficiency at $X_t=(M_t,G_t)$; positivity); `#def-value-object:59` |
| R03: conservative policy trivially scores $S=1$; class-fitness discriminator reliability; context-window wall; policy-relativity of IB | WN (`#def-model-sufficiency`, `#def-model-class-fitness`, `#form-agent-model` Working Notes) | — |
| R04: score-function mismatch sign | IN, correct: `#def-mismatch-signal:15`, `:55` define $\tilde\delta_t = +\nabla_M \log P$, and `:15` says it coincides with $\delta_t$ up to scaling under Gaussian models, which is the $+$ sign ($\delta/\sigma^2$). No canon file uses the minus form (grep). WN :92 records auditors misquoting it; it asks only for a sentence the body already has, so the WN drain can retire it | — |
| R04: three readings of zero mismatch; action fluency; $g_M$ form; resolved items on `der-recursive-update` / `form-event-driven-dynamics` | IN (body) / WN | — |
| R04, R05, R19: R2 detection-latency sharpening under model-class inadequacy (unrun) | LEDGER | `spikes-proposed-r2-detection-latency-sharpening-under-mo-d44a` (raise) |
| R04, R05: correlated-channel tempo, echo-chamber penalty, anti-correlated superadditivity; real multi-channel A/B never run | IN (`#deriv-tempo-additivity`); the experiment is E-shaped | `untested-catalog-predictions-for-e` (raise) |
| R05: `emp-update-gain` open questions (no scalar $U_M$ for neural nets; matrix gain) | IN (body, named as open) | — |
| R06: three-way local indistinguishability (FM-5 / FM-2 / not converged); in-context LLM in the $\alpha/\beta$ sub-scope; meta-deliberation regress | WN / body open question | — |
| R07: `#def-mood` floor not pinned (mood-induced complacency) | IN: `#def-mood:30` has $g: \mathbb R \to [g_{\min}, g_{\max}]$ with $0 \lt g_{\min}$, and `:46` discharges MG-1 from it | — |
| R07: `#der-mood-timescale` derives mood as estimator, `#def-mood` uses it as modulator | WN :55 ("Open — mood-sets-gain composition"); part of the released mood follow-ons | `todo-mood-layer-prospective-mood-arc-released-9d91` (raise) |
| R07: `#result-persistence-condition` novelty at intuition-only search depth | IN: `:160` now states claim synthesis on the robust-control stability/performance split with citations; the primary check is open | `questions/robust-control-lineage-primary-check` |
| R08: quantitative loss floor for an incident-attribution merge target; replay as non-evidence in forensics | ASIDE: AISI applied questions; `#disc-sandbox-evaluation-ceiling` treats replay only as the evaluator's laboratory (`:23`, `:51`), which is correct for its scope, and no canon claim is wrong for lacking the forensic case | — |
| R08: intervention-cadence sweep (`#der-temporal-nesting` WN); residual-signature diagnostic (`#result-structural-adaptation-necessity` WN) | WN; both are untested predictions of the kind `untested-catalog-predictions-for-e` collects | raised there |
| R08: `spikes/temporal-nesting-rg/` | Spikes drain's surface (`drain/spikes*.md`) | — |
| R09: do the identifiability floors' escapes compose or interfere | LEDGER | `questions/identifiability-floors-compose-or-interfere` (a question; `vsect raise` takes items only, so the source is recorded here) |
| R09, R10: "two routes exhaust" adversarial spike on `#disc-value-functional-grounding-floor` | LEDGER | `spikes-proposed-two-routes-exhausts-adversarial-spike-on-3366` |
| R09, R40, R62: Skalse 2022 as cross-cluster bridge | LEDGER, but **two items for one thing**: `spikes-proposed-advanced-17-skalse-2022-reward-hacking-unhackabil-8188` and `imported/spikes-proposed-skalse-2022-reward-hacking-unhackability-352d` (same title). Flagged for the lead (I.3); not merged by me | both |
| R09, R40: judgment aggregation (List & Pettit 2002) absent; Arrow may be the wrong classical anchor | ADD (F.2): no canon file cites List & Pettit (grep `0*/src`) | `candidate-missing-prior-art-f-2-worth-having-not` |
| R09: BG2 Undermind-sourced citations still verification-deferred | LEDGER | `primary-source-verify-or-replace-with-read-sourc` |
| R09, R10, R13: SP-23 `#disc-theorem-import-architecture` | LEDGER | `proposals-sp-23-disc-theorem-import-architecture-f-a22e` |
| R10: escape-standpoint axis (SS1 labeling fix verified; SS3 peer-standpoint hypothesis unrun) | LEDGER via the spikes drain (`drain/spikes-c-coupling-llm.md`: partly landed `be61f9b`, four open pieces itemized, e.g. `disc-identifiability-floor-s-catalog-boundary-re`) | — |
| R10: cross-ladder monotonicity of the separability axes | WN (`#disc-separability-pattern`); no item, none opened (unattempted, no candidate claim to land) | — |
| R10: transfer of `#disc-constructive-impossibility-posture`'s negative results to a real control protocol | ASIDE: AISI applied mapping, no canon claim at stake | — |
| R10: Deutsch pointer | LEDGER | `todo-prior-art-pointer-to-investigate-deutsch-3a4a` |
| R11: bounded-signaling caveat in `#der-directed-separation` | IN (named in the body) | — |
| R11, R24: Case 1 of `#hyp-directed-separation-under-composition` needs goal-blind projection/aggregation too (F122) | LEDGER, still a defect at HEAD: the Case 1 bullets (body, "Case 1: Goal-blind routing") still conclude from processing + routing alone; WN :104 states the missing premise | `todo-disc-composition-consistency-does-direct-813e` (raise) |
| R11: measuring $\kappa_{\text{processing}}$ on a deployed model | E.1 owns it (INTENT) | — |
| R11: satisfaction threshold as the "can't stop" difference | LEDGER for the canon claim that rests on it | `bounded-objective-instrumental-step-underived` |
| R11: between-event drift of $G_t$ | WN (`#form-complete-agent-state`) | — |
| R11, R23, R52: SP-17 goal-information leakage $\mathcal L_{G\to M}^c$ | LEDGER | `goal-information-leakage-is-not-a-separation-failure`, `land-the-leakage-locus-result-of-spikes-spike-le` |
| R11, R22: modularity → strategic-asymmetry game | LEDGER, again **two items for one spike**: `spikes-proposed-advanced-13-game-theoretic-formalization-of-the-m-4436` and `imported/spikes-proposed-modularity-strategic-asymmetry-game-theo-1392` | both |
| R11, R25, R37: decomposed $\kappa$ estimator (accuracy vs goal inference) | LEDGER | `spikes-proposed-decomposed-empirical-estimator-accuracy-e63e` |
| R12: Smithe 2024 vs `#disc-continuity-stance` orthogonality | LEDGER (twice again: `spikes-proposed-advanced-15-categorical-cybernetics-re-grounding-9642`, `imported/spikes-proposed-categorical-cybernetics-first-fit-check-3158`) | both |
| R12, R55: SP-12 commitment / resource / temporal DAG | LEDGER | `proposals-d-4-sp-12-commitment-resource-temporal-d-1dea` |

*(R13 onward being written)*

## What was read whole, sampled, not reached

*(being written)*

## Adjacent findings

*(being written)*
