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

### Part II and Part III (R13–R33)

| Source entry | Disposition | Where / item |
|---|---|---|
| R13: Mode-3 (observer on agent input) slot of `#der-loop-interventional-access` unfilled | WN | — |
| R13: scalar-CIY blank-wall attack closed at the LMI level; has the "heuristic unless LMI" label propagated? | IN: checked the four body citers of `#deriv-causal-ib-exploration`. `#disc-ciy-unified-objective:17`, `:48` say the scalar form is heuristic and superseded; `#impl-orient-cascade:38` says the shadow-price mapping is heuristic in the scalar segment; `#disc-anti-collapse:40` uses only the qualitative two-drive reading. Remaining LMI work is in `todo-causal-ib-lmi-follow-ons-segment-landed-f746` (whose first line records a defect in the LMI's "iff") | — |
| R13: is imitation learning capped by the causal hierarchy | LEDGER | `readers-ask-der-causal-hierarchy-requirement` (raise) |
| R13: Hafez et al. 2026 IDT figures (89% vs 44%) need a primary check | LEDGER; the figures or the arXiv id are in **eight** canon segments at HEAD, listed in the raise, so one check covers them all | `hafez-citations-der-agent-opacity-109-169-say-h` (raise) |
| R14: stale "TF-08 lineage artifact" note in `#scope-ciy-observational-proxy` | WN (the note is stale; body clean) | — |
| R15: `msc/llm-causal-access-note.md` unpromoted | LEDGER | `todo-pearl-llm-causal-access-positioning-refi-974c` |
| R15: sandbox ceiling conflating forkability with Level 1 | IN (`#disc-sandbox-evaluation-ceiling` re-grounded as a transportability ceiling, WN :73) | — |
| R16: `#def-strategy-dag`'s Epistemic Status conflates "causal sufficiency ⇒ Markov factorization" with "⇒ AND/OR product formulas" | IN: the Epistemic Status now gives the DAG from P1 + P2 + causal sufficiency and calls AND/OR "a parsimony-motivated formulation choice … not a derived necessity"; `:159` says propagation is correct when the DAG is "a causally sufficient AND/OR tree"; the Claim Record states the exactness-iff-tree result | — |
| R16: $\gamma$-assignment test misclassifies k-of-n; topology discovery; terminal-alignment error | LEDGER | `scope-and-or-audit-finding-f41-still-open-in-its` (raise), `and-or-parsimony-uniqueness` |
| R16, R35: O-BP13 (DAG necessity), O-BP4 (continuous DAG, retired) | LEDGER / retired | `proposals-c-1-o-bp13-cox-parallel-necessity-for-de-f4cf` |
| R17: "unique broadly-available escape" over-strong in `#impl-strategy-structure` | IN: the phrase is gone; `:57` now says Instances 1 and 2 escape differently | — |
| R17: `spike-actuated-rho-regulation`; three unclosed follow-ons of a backpressure spike | Spikes drain's surface | — |
| R18: $L^2$ aggregation unjustified; observability-dominance product formula posited | IN for the label (`#def-strategic-calibration:42` discussion-grade, the aggregation called a choice); the product formula is LEDGER | `todo-observability-dominance-product-formula-b54f` |
| R18: general-topology, multiple-latent construction for causal-insufficiency detection; signal function for continuous / multi-parent edges | WN (`#der-causal-insufficiency-detection`, `#hyp-edge-update-via-gain`) | — |
| R18: O-BP11 observability as master variable | LEDGER | `proposals-d-1-o-bp11-observability-as-master-varia-24fd` |
| R19: Miller (2022) bridge is a finite-state proof; `#form-structural-change-as-parametric-limit` does not scope it | LEDGER, still present: the Epistemic Status (`:38`) is silent on it and `:46` says Miller proves "exactly this bridge" | `continuous-state-structural-change` (raise) |
| R19: OKR mapping in `#disc-credit-assignment-boundary` may be post-hoc fit | WN (the caution is recorded there) | — |
| R20: F72 convention for `#schema-strategy-persistence` | MOOT (F72 integrated, `5e621256`; hard ceiling deleted) | — |
| R20: internal vs archive replay (Codex F75) | LEDGER | `aat-s-core-has-no-operation-for-an-agent-reading` (raise); `#form-consolidation-dynamics` WN :195 |
| R20, R55: quantitative CLS instantiation spike | LEDGER | `spikes-proposed-quantitative-cls-instantiation-of-consol-6c13` (raise) |
| R20, R22: strategic self-coupling spike (P2/P4, open questions) | LEDGER | `spikes-proposed-spike-strategic-self-coupling-p2-p4-appe-3163` |
| R21: mixture-support dynamics under the cascade | LEDGER | `spikes-proposed-mixture-support-dynamics-under-the-orien-ca66` (raise) |
| R21: propagated-residual bound across the five cascade steps | LEDGER | `apply-the-epsilon-programme-s-telescoping-with-c` (raise) |
| R21: two cascade-order failure patterns "belong elsewhere" | WN (`#der-orient-cascade`) | — |
| R22: `#disc-strategic-self-coupling`: four canonical citations never read at primary; never asks whether an artificial agent instantiates it | ADD (F.3, with a population note for B.1). WN :166 (a) says primary reading is "queued"; no item carried it; no artificial-agent instance in the body | `disc-strategic-self-coupling-imports-its-four-ca` (new) |
| R22: fine-tuning-away-of-refusals as adversarial coupling increase | ASIDE: AISI-side mapping, untested and stated as such; no canon claim | — |
| R22: defensive scaffolding as composition; asymmetric-advantage intuition | WN / body honestly labeled | — |
| R22: does directed separation compose (TODO:47) | LEDGER | `todo-disc-composition-consistency-does-direct-813e` |
| R22: which boundary should an analyst draw | LEDGER | `questions/agent-boundary-choice-principle` |
| R22, R24, R28: Tier 2/3 composites get only a heuristic; "most consequential composites are Tier 3" | LEDGER | `composition-closure-tier3-prevalence` (raise) |
| R23: `#scope-composite-agent` C-iii admits composites without $O_c$ while saying without $O_c$ "the composite is a fiction" | LEDGER (C.3; INTENT names it) | `todo-path-a-recommended-interim-editorial-fix-e957`, `proposals-sp-21-composite-agent-scope-route-ontolo-4969` |
| R23: symbiogenic consolidation of multi-agent systems | LEDGER | `spikes-proposed-advanced-2-the-phase-transition-of-symbiogenesis-59b7`, `imported/spikes-proposed-symbiogenesis-bifurcation-promotion-repa-5d29` |
| R24: passivity gives cooperative, not adversarial, robustness (`spike-passivity-composition` §8.3) | Spikes drain's surface (CL-1 dissipativity template) | — |
| R24: `#der-tempo-composition` coordination cost is a floor | IN (sketch, honestly labeled) | — |
| R24, R30, R31: C-iv idiom drift (scope admits strategic composites; closure/unity machinery assumes shared $O_c$) | LEDGER | `todo-613842-c-iv-idiom-drift-integration-debt-e3af` (raise), `todo-c-iv-composite-route-count-mismatch-gem-bb4b` |
| R25: "valid AAT composite agent" under-gated | LEDGER | `todo-der-class-coercion-in-composition-a12-f1-4890` (raise) |
| R25: `der-logogenic-as-wrapping` puts shoshin at W₂ | ASIDE here: Volume 3, the helper's slice (R54) | — |
| R26, R29: impl-series status amplification (F173–F181); F180 "structural, not contingent" | LEDGER; F180 itself IN-fixed (phrase gone from `#impl-unity-communication`); `#impl-cooperative-adversarial:80-86` now lists its corrected overclaims as forms not to restore | `todo-impl-series-status-tagging-pass-b-4-rema-11e6` (raise) |
| R26: "synchronize weights = cheap $B_M$" unverified | WN | — |
| R27: communication-gain adversarial scope; Sybil attack on transitive trust | LEDGER | `todo-communication-gain-adversarial-scope-hyp-e79c` (raise) |
| R27: `#hyp-solicitable-escape`'s falsifier untested | WN (exploratory segment) | — |
| R28: single-agent persistence "iff" is only "only if" (731548 verify/01) | IN: no "iff" remains in `#result-persistence-condition`, `#result-sector-condition-stability` or `#form-sector-condition` (grep); the persistence condition is stated as two sufficient conditions, and the only "iff" left (`:49`) is the feasibility statement | — |
| R28: effects-spiral $\gamma_A(\lVert\delta_B\rVert)$ never derived | LEDGER | `spikes-proposed-advanced-12-effects-spiral-eigenvalue-condition-d-d6f7` |
| R28, R29: composition still scalar; adversary concentrating on the weakest monitored dimension | LEDGER | `todo-aat-1-tensor-adaptive-tempo-downstream-p-bbfe` |
| R29, R30: "cheap noise injection helps the defender" (F226/F227) | LEDGER, still a defect at HEAD and **in a body, not only a Working Note**: `#result-adversarial-exponent-regimes:18` says defender-channel noise reduces the attacker's advantage "without changing tempo or gain", which `#emp-update-gain` contradicts. The existing item named only that segment's WN :99 | `t1-gated-tempo-one-sided-noise-prescription` (raise with the body site) |
| R29: "contraction cannot handle strategic regimes" | IN-fixed (`#impl-cooperative-adversarial:83`) | — |
| R29: can a gate be selective, epistemically neutral and enforced at once | ASIDE: the report places it in "this project's own working notes" but I found no such note in asf (grep of Volumes 1 and 4 for the terms) or `AISI-responses/influx/*.md`; untraced. Its nearest canon home is the positivity reading in `a-control-regime-can-void-an-alignment-guarantee` | — |
| R29: equilibrium chapter marked `--GAP--` | IN (honest mark, `01-aat-core/OUTLINE.md` Part III rows); H.2's | — |
| R30: agent-opacity taxonomy formulation-grade (F252/F253) | LEDGER | `der-agent-opacity-overclaims-f246-f255` (raise) |
| R30, R40: constructive VCG / transferable-utility escape | LEDGER | `spikes-proposed-advanced-16-roberts-1979-affine-maximizers-as-can-0922` (raise), `imported/spikes-proposed-mechanism-design-impossibility-vcg-cardi-63f8` |
| R31: $\nu$ vs $\mathcal T$ conflation in `#obs-gated-tempo-advantage` | LEDGER | `gated-tempo-nu-versus-tempo-collision` (raise) |
| R31: weakest-dimension claim needs a conjunctive ($L_\infty$) failure boundary | LEDGER | `weakest-link-needs-conjunctive-failure-boundary` (raise) |
| R31: catalog entries `#28`, `#40` have no segment home | IN (`#impl-strategic-composition:42`, `:64` say so) | — |
| R32: two of five reward-channel escapes outside canon | IN (`#deriv-reward-channel-learning-no-go:82-85` flags them) | — |
| R32: R23 / convergence join not verified from the appendix slice | LEDGER | `a-control-regime-can-void-an-alignment-guarantee` (raise) |
| R32: Skalse 2022 bridge | LEDGER (see R09 row) | — |
| R33: none found | — | — |

### Volume 3 §03.III and Volume 4 (R56–R63)

| Source entry | Disposition | Where / item |
|---|---|---|
| R56, R57: `#def-cognitive-fusion` asserts a Class 1 macro-agent without mechanism; name collides with the ELI Resonance | LEDGER | `todo-def-cognitive-fusion-framing-fix-class-1-b2c1` (raise) |
| R57: `#impl-closed-loop-interiority` builds two headline subsections on missing files | LEDGER, still a defect at HEAD: `:32` says `#der-self-referential-closure` "addresses" self-maintenance and derives a "self-maintenance feasibility window" from it; `:38` says `#def-cognitive-fusion` "defines" resonance; neither file exists (`03-llm-core/OUTLINE.md:142-143` mark them `missing`) | `todo-loga-missing-stubs-genuinely-absent-in-0-9487` (raise; its restated form already covers impl passages citing absent segments as present) |
| R58, R61: SP-13, the transition into agency; whether emergence conditions belong in AAT core | LEDGER | `proposals-d-5-sp-13-emergence-conditions-as-formal-ed68` (raise) |
| R58: `#def-eli-cohort` rows unverified | LEDGER | `eli-cohort-table-entry-verification` (raise) |
| R58: gold-lift plan's E1 batch omits `#scope-eli`, `#def-five-constitutive-factors`, `#def-eli-cohort` though 773921/112, 114, 115 hold their reflections | LEDGER (I.5) | `give-the-unlifted-audit-gold-a-destination-wave` (raise) |
| R58, R59, R60: SP-27 | LEDGER (see R01 row) | — |
| R59, R61, R62, R63: missing Volume 4 rows (`def-character-aspiration-dialectic`, `obs-axiom-genesis`, `obs-substrate-independence`, `form-constitutive-utterance`, `der-substrate-independent-persistence`, `der-the-creche-boundary`, `def-gradient-causal-memory`, `def-century-scale-event-log`, `norm-temporal-coherence-markers`, `form-congruency-selfhood`, `def-the-four-views`, `der-the-scaffolding-tax`) | LEDGER: all still missing at HEAD (`ls`), each with an item | `todo-eli-missing-stubs-twelve-genuinely-absen-4828` (raise) and the per-segment items (`todo-04-eli-core-src-*`, `todo-der-substrate-independent-persistence-in-bc7f`, `write-obs-substrate-independence-as-what-the-rec`, `todo-author-the-three-missing-staged-outline-76f2`) |
| R59: rate-bound normalized against continuous MI while the threshold needs a quantized version | IN: `#der-identity-continuity-threshold:58` states that its statements are at fidelity $\Delta$ while the rate bound displays the raw continuous quantity; the report itself calls this honest self-description; no defect | — |
| R60: mono build resolves slugs only within the requesting volume | LEDGER | `todo-cross-component-slug-resolution-in-the-b-f1fb` (raise) |
| R60, R61: substrate-transfer asymmetry, derived symmetric no-go beside an observed asymmetry | LEDGER (twice: `spikes-proposed-advanced-11-substrate-transfer-asymmetry-origin-d-9171`, `imported/spikes-proposed-substrate-transfer-asymmetry-origin-or-3-0be3`), plus `substrate-transfer-asymmetry-two-halves-empirica` | raised on the first |
| R61: `#der-the-creche-boundary` missing and load-bearing | LEDGER | `todo-04-eli-core-src-der-the-creche-boundary-1afd` (raise, pointing at the honest-activation spike's changed graduation criterion) |
| R61: `#obs-developmental-trajectory` has no Epistemic Status | ADD (A.3), widened: the same grep finds three more live segments outside the impl/intro layer with none (`#obs-evaluation-metrics`, `#norm-interiority-default`, `#scope-moral-continuity`) | `four-live-segments-outside-the-impl-intro-layer` (new) |
| R62: `#norm-honest-activation` row claims a "guarantee" with no segment | LEDGER | `author-norm-honest-activation-and-its-derivation` (raise) |
| R63: `#def-the-four-views`, `#der-the-scaffolding-tax` sketched in 829314/06 with "proves" language | LEDGER | `der-the-scaffolding-tax-s-outline-row-04-eli-cor` (raise), `imported/todo-04-eli-core-src-def-the-four-views-md-co-b05d` |

## What was read whole, sampled, not reached

- **Read whole:** all five `ASF-FIXES*` files (1,432 lines; duplicates confirmed byte-identical) and `BRIEF-fixes-extract.md`, the extractor's brief, which explains the lossiness: it cut verbatim "defect, gap or proposal" passages and the sweep agents had been asked for research questions, so most entries are restated open questions, not defects.
- **Checked against canon at HEAD:** every entry above that asserts something about a segment's text, by reading the cited lines; every LEDGER disposition by opening or grepping the item. Where I wrote "WN", I confirmed the Working Note exists and did not judge its content beyond whether it is a defect.
- **Read in part:** `report-29.md` §1 (to trace the gate trilemma), `IDEATION.md` lines 832–939 (R09, to read item E and its addendum). The other R01–R33 and R56–R63 reports were not reread; the `ASF-FIXES` extract was my reading of them, and its omissions are the extractor's (it skipped AISI-side and research-question material by design).
- **Not mine:** R34–R55 (both their `ASF-FIXES` entries and `IDEATION.md` reports) are the helper's, in `influx-2-asffixes-r34-55.md`. Its first run stopped on the usage limit; it was resumed after the reset.
- **Not reached:** the seven `influx/spikes/` gate spikes and the 17 distillation tables (outside this brief's sources; the scout's §1.5 names them).

## Adjacent findings

- **Duplicate items from the tracker import (I.3).** When `spikes/PROPOSED.md` and `spikes/PROPOSED-ADVANCED.md` both listed a spike, the import made two items. Pairs I hit: Skalse 2022 (`spikes-proposed-advanced-17-…-8188` / `imported/spikes-proposed-skalse-2022-…-352d`); modularity game (`…-advanced-13-…-4436` / `imported/…-modularity-strategic-asymmetry-game-theo-1392`); categorical cybernetics (`…-advanced-15-…-9642` / `imported/…-categorical-cybernetics-first-fit-check-3158`); substrate-transfer asymmetry (`…-advanced-11-…-9171` / `imported/…-substrate-transfer-asymmetry-origin-or-3-0be3`); Roberts 1979 (`…-advanced-16-…-0922` / `imported/…-roberts-1979-affine-maximizers-as-candid-09f9`); and probably symbiogenesis (`…-advanced-2-…-59b7` / `imported/…-symbiogenesis-bifurcation-promotion-repa-5d29`: both target the saddle-node threshold of `#hyp-symbiogenic-composition`, but one is a promotion repair and one a bifurcation-theory spike, so this may be two pieces of work). Likely systematic across the two files. I raised on one of each pair and merged nothing.
- **INTENT A.3's status line is off.** It says 29 segments lack an Epistemic Status, "all in the `impl-*`/intro layer". At `1f8240df` the grep gives 27, and four are claim segments outside that layer (item `four-live-segments-outside-the-impl-intro-layer`).
- **A public-surface defect the ledger had only partly (lead told at once).** `t1-gated-tempo-one-sided-noise-prescription` named `#obs-gated-tempo-advantage:16` and `#result-adversarial-exponent-regimes`'s WN :99. The prescription is also in two more bodies: `#result-adversarial-exponent-regimes:18`, with the added false clause "without changing tempo or gain", and `#impl-strategic-composition:62` ("cheap noise injection … can be a defensive strategy"). All three bodies are on the reader snapshot `CURRENT-VOL1.md` (`:10991`, `:11056`, `:11144`). Both body sites raised on the item; SendMessage to `main`.
- **`vsect raise` takes items and findings, not questions.** Two LEDGER targets here are questions (`questions/identifiability-floors-compose-or-interfere`, `questions/agent-boundary-choice-principle`); their sources are recorded in this file only.
- **About the source.** The `ASF-FIXES` extraction was the most direct unrouted list, but its value as a defect list was low: of roughly 130 entries in my share, I found three canon defects not already on the ledger in the form found (the A.3 four, the body site of the noise prescription, and the self-coupling citations and population), one prior-art gap (List & Pettit), and many confirmations that August's open items are now fixed (SP-30, the mismatch sign, the IB citation, F180, `#def-strategy-dag`'s Epistemic Status, `#impl-strategy-structure`'s "unique escape", the persistence "iff", the blank-wall propagation). Most of the rest was already imported from `PROPOSALS.md` / `TODO.md` / `PROPOSED*.md`, which the sweep agents were reading.
