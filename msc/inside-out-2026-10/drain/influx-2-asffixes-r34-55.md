# Influx drain: sweep-2 reports R34–R55 (and their `ASF-FIXES` entries)

> **KR: G.2** in `../INTENT.md` (*stranded additions are landed at honest tier or set aside with a recorded reason*). Canon defects go to **C.1** (C.3 for contradictions between segments, C.4 for open strengthenings); terminology to **F.1/F.4**; citations to **F.2/F.3**. Top intent: *"Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself."* After a compaction, re-read `../INTENT.md`, then this file.

*Drain agent `drain-influx-2-asffixes-r34-55` (Opus 5.5), 2026-10-30, helper to `drain-influx-2-asffixes`, who folds this into `influx-2-asffixes.md`. Sources: `~/src/AISI-responses/influx/sweep-2-raw/report-34.md` … `report-55.md` (the same text as `IDEATION.md` from about line 2943) and their extractions in `ASF-FIXES-part3.md` (R34–R48, lines 6–241) and `ASF-FIXES-part4.md` (R49–R55).*

## Questions, with the reading I am proceeding on

*(none yet)*

## Method

- Each report is read whole from `report-NN.md`. The reports are written for an AISI reader; most of their content is ASF's own open edges restated as questions for the UK. For ASF, what matters per item is whether the ASF-side claim or gap is (a) a canon defect, (b) an open question or strengthening that ASF lacks a home for, or (c) already held somewhere. The AISI framing itself is not ASF material and is not drained here (that belongs to AISI-responses).
- Dispositions follow the lead's file: **IN** (in canon at HEAD, where), **DEFECT** (canon defect still present; item), **ADD** (true or worth having, absent; item at honest tier), **LEDGER** (already an open item; source added with `vsect raise`), **WN** (stated in a segment's Working Notes; the WN drain lanes own it), **MOOT** (overtaken), **ASIDE** (set aside, reason given).
- Canon is checked at asf `main`; before opening an item I check `vsect open segment:<slug>` and grep `items/`.

## Dispositions

Checked at asf `main` d058c25e (R34–R42). `PROPOSALS.md` and `spikes/PROPOSED*.md` no longer exist; their rows are ledger items (many under `items/imported/`, imported 2026-10-30 and not yet rechecked).

### R34 — `deriv-gain-sector`, `deriv-recursive-update`, `der-multi-timescale-stability`, `sketch-structural-adaptation-genericity`, `deriv-discrete-sector-condition`

- **Vector bound vs scalar bound read as a contradiction** (`deriv-discrete-sector-condition`, the only `ASF-FIXES` entry with a fix proposed). **LEDGER** `item:readers-ask-deriv-discrete-sector-condition` (H.4) states exactly this, at HEAD line numbers. Source raised.
- **"Structural adaptation is generic" is a probable overclaim** (R34 addendum, from `AUDIT-WORKING-374162/08`). **LEDGER** `item:structural-adaptation-genericity-bridge` (C.4), which already cites 374162/08, records that canon bodies were brought into line today, and names the two stale lines left in the sketch (:14, :20). R34's restatement for a reader, *is a repeated exit-and-return an ordinary excursion or the leading edge of a regime change, and is there a checkable criterion?*, is the observable form of the bridge question. Source raised with that form.
- **Jump-process extension of the stacking theorem** (`der-multi-timescale-stability` WN :128). **LEDGER** `item:outside-domains-that-meet-der-multi-timescale-st` (C.4, "this item is the spike") and `item:which-aat-structural-adaptation-mechanisms-satis` (B.1). R34 adds one reading neither item has: whether a monitored agent could *induce* a structural jump to leave the regime the certificate covers, so that capability growth and evasion look alike from outside. Hypothesis-grade, the report's own; raised onto the spike item.
- **"Slowing the outer loop does not restore stability when the fast loop has multiple equilibria"**, adaptive reserve $\eta\mu R-\rho$, Markov-as-boundary, and the Model S/D 0-or-1 dichotomy invariant to $\alpha$: **IN** (the segments' bodies and `#deriv-sector-condition` Cor A.1S.1). Nothing to open.
- **"Certificate voice" vs "behaviour voice", the most misquotable chain** (R34 addendum, from 374162/05). **IN**: `#impl-persistence-and-limits` WN :110 holds the six over-read chain statements with their licensed forms (374162 quiz batches 5–7); `#impl-cooperative-adversarial`:87 states the certificate-voice reading. It is Working-Note content, so the WN lanes own its fate.

### R35 — `detail-linear-ode-approximation`, `deriv-graph-structure-uniqueness`, `deriv-edge-credence-dynamics`, `deriv-strategic-persistence-hard-ceiling`, `deriv-strategy-cost-regret-bound`

- **The 1/2 ceiling is convention-dependent (SEG vs ALT1, F72).** **MOOT**: `5e621256` deleted `#deriv-strategic-persistence-hard-ceiling`; B.1F (gain exactly $1-\lambda$) and `#deriv-evidence-allocation-ceiling` replace it, and INTENT records F72 landed and checked. (Adjacent: `item:posture-floors-vs-reachability-caps` still lists the deleted slug among its concerns; not mine to change.)
- **DAG necessity is open (O-BP13).** **LEDGER** `item:proposals-c-1-o-bp13-cox-parallel-necessity-for-de-f4cf` (the slug is now `#deriv-graph-structure`, 471aa7ce). Source raised.
- **The `depends:` 2-cycle with `form-strategy-complexity-cost`** (TODO :265). **LEDGER** `item:todo-depends-conflates-logical-prerequisite-w-9868` (H.2). R35 only notes it did not check it; no raise.
- B.4's $\alpha=0$ under greedy OR-policy, reverse-KL forcing and Bretagnolle–Huber, B.3/B.7: **IN**. R35's correction of AISI-responses' own sweep item 17 belongs to AISI-responses: **ASIDE** here.

### R36 — `deriv-edge-update-natural-parameter`, `deriv-adaptive-gain-dynamics`, `internal-external-decomposition`, `deriv-update-detection-latency`, `disc-independence-audit`

- **The IDT-versus-reward detection gap (Hafez et al. 2026, 89% vs 44%) should widen with accumulated experience.** **LEDGER** `item:untested-catalog-predictions-for-e` (E.2) carries this prediction as its #3. Source raised.
- **Restoration is invisible to an exploration-free agent.** **IN**: `#der-severed-actuation-dynamics` Result 4 (:54–59) states it, including the fixed point under greedy policies. The report read it in the spike; it has since landed.
- **Adversarial adaptive gain (meta-gain tempo race).** **LEDGER** `item:spikes-proposed-adversarial-adaptive-gain-meta-gain-temp-06a0` (unassigned). Source raised.
- **Independence profile as an instrument (SP-16).** **LEDGER** `item:proposals-d-8-sp-16-independence-audit-as-empirica-ea97` (unassigned). Source raised.
- Log-odds uniqueness, the $\Omega((n_{\min}+1)/\varepsilon)$ latency floor, and the three-term internal–external split with its no-multiplicative-score no-go: **IN**.

### R37 — `disc-approximation-tiering`, `disc-compression-operations`, `deriv-observation-ambiguity-bias-bound`, `disc-partial-coupling-pathways`, `disc-w1-structural-bound-boundary`

- **Separate substrates are sufficient, not necessary, for the structural W₁ bound** (the C2′ realization spike). **IN**: `#def-auxilia-hierarchy`:86 now says so and adds that what separation buys is auditability (A11). `item:todo-def-auxilia-hierarchy-c2-realization-ove-564e` still reads as open; its recheck is the tracker lanes', and I note it here rather than act.
- **The leak past the C2′ boundary: flat or amplifying?** **IN** as an honest open statement (`#disc-w1-structural-bound-boundary`:49, "suggestive but not proven in general"), with the unregistered toy simulation already an item (`item:w1-boundary-toy-sim-unregistered`, F.3).
- **Capability pulls the leakage bound both ways: accuracy effect vs inference effect** (374162/10, Q/A b10-v.6). **LEDGER** `item:spikes-proposed-decomposed-empirical-estimator-accuracy-e63e` (E.1). Source raised with the 374162/10 locus, which the item lacks.
- **"For Class 2 LLM agents with strong goal-conditioning, $I$ may not be small"** (471203/62-63). **LEDGER** `item:bias-bound-lsi-constant-and-large-information-regime` (C.4). Source raised.
- The §5 record of two failed derivation routes: **IN**. `disc-approximation-tiering` and `disc-compression-operations` are organizational by their own account: nothing to drain.

### R38 — `der-belief-strategy-attractor`, `disc-dynamic-regime-axis`, `form-resource-budget`, `der-resource-bounded-destabilization`, `result-contraction-template`

- **The regenerative budget regime ($r_{\mathcal B}\gt0$): guarantee or postponement?** **WN** at `#der-resource-bounded-destabilization`:114 and `#form-resource-budget`:71, with no ledger item of its own. R38 believed the parallel to the identity-continuity barrier problem was undrawn; it is drawn (:114, "exactly parallel to the continuity-persistence barrier-reachability open problem"). What the ledger lacks is the join: `item:identity-continuity-threshold-open-edges` (C.4) part (a) is the same quasi-stationary-distribution / absorbed-chain survival question, so one spike can answer both. Raised onto that item, naming the resource-budget Working Notes as the second consumer.
- **Plan-coupled vs goal-coupled bias as a checkable diagnostic.** **LEDGER** `item:der-belief-strategy-attractor-conditional-run-th` (C.4). Source raised.
- `disc-dynamic-regime-axis`, `result-contraction-template`: **IN**; the report itself finds no ASF gap.

### R39 — `deriv-variational-sector-condition`, `deriv-l1-update-bias`, `der-architecture-noidentifiability`, `deriv-fisher-whitened-update-rule`, `deriv-regime-marginal-indistinguishability`

- **The confabulated Monte Carlo record in `deriv-l1-update-bias`.** **IN**: replaced by two real runs (:82–86) with a regression guard (:120).
- **SP-10 posterior-displacement template.** **LEDGER** (imported `proposals-e-2-sp-10-…`); R39 adds nothing.
- All five results as restated: **IN**.

### R40 — `deriv-strategy-proofness-impossibility`, `deriv-bilateral-trade-impossibility`, `deriv-social-welfare-aggregation-impossibility`, `deriv-fisher-local-update-gain`, `deriv-tempo-additivity`

- **Correlated monitors saturate; anti-correlated pairs compose super-additively.** **LEDGER** `item:correlated-monitors-saturate-at-a-floor-no-monit` (G.2). Source raised.
- **GS/MS/Arrow as a no-go for multi-agent alignment; Roberts 1979, Skalse 2022, and the cardinal escape from Arrow's IIA.** **LEDGER**: the ADV #16/#17/#18 items concern `#disc-implementation-impossibility`. R40's reading of #18, that score-based rather than rank-based monitor fusion is the practical form of the cardinal escape, is a concrete instance #18 lacks. Source raised onto #18.
- **Register note**: "designer-side impossibility, as distinct from an agent-side inference limit" is said only inside dense paragraphs, near-verbatim in all three. **ASIDE**: R40 itself calls it a register note, not a defect, and the segments do state the distinction; the H.4 reader-gap lanes can take it if a cold reader trips on it.
- AAT-1 tensor tempo: **LEDGER** (`item:todo-aat-1-tensor-adaptive-tempo-downstream-p-bbfe`); no raise.

### R41 — `deriv-matrix-persistence-condition`, `deriv-causal-ib-exploration`, `deriv-causal-ib-lmi`, `obs-authored-world-laboratory`, `obs-section-i-validation-simulations`

- **`#obs-section-i-validation-simulations` says its code is unreleased; it is in the tree.** **DEFECT**, new item (F.3). The body says the driver code "will be released as a citable code artifact at publication" (:52) and is "maintained as a reproducibility supplement to be released … at publication" (:84), and never cites `empirica:track-b-nonlinear`. Since `1d65587a` the suite is registered there (MANIFEST, RUNS, `sim1_*`, `sim2_*`, `variants/`), and `empirica/INDEX.md` lists this segment as a consumer. R41 relayed the canon sentence as a caveat ("currently unverifiable by an outside reader"), which is the harm: canon tells a reader the evidence is unavailable when it is one directory away.
- Per-coordinate checks can pass while the joint check fails; the blank-wall exploit and its LMI repair: **IN** (`#result-per-dimension-persistence`:148 already draws the AI-evaluation reading).
- `obs-authored-world-laboratory` dated 2026-07-16: **IN** as honestly dated. Whether its build-state line is stale belongs to the vivarium bridge, not this drain.

### R42 — `detail-operationalization`, `example-kalman`, `example-bandit`, `example-strategy`, `example-L1`

- **No end-to-end worked example (O-BP15).** **LEDGER** `item:proposals-c-2-o-bp15-comprehensive-minimal-proof-o-8a18`. Source raised.
- **A predicted, unlocated numeric slip in `example-kalman/bandit/strategy`.** **LEDGER** (imported `todo-next-de-novo-cycle-target-aat-part-ii-or-42d0`). Source raised: R42 read all three whole and did not re-derive, so the prediction is still untested.
- **`worked-example-cam` missing; the Moore-machine composed claim never checked piece by piece.** **LEDGER** `item:todo-aat-9-remaining-missing-stub-worked-exam-ad0e`. Source raised with R42's addition: the bridge from Moore machines to the computational class of an LLM agent is attempted nowhere.
- **$\rho_\Sigma$ cannot be estimated from observables (F28).** **LEDGER** `item:todo-f28-rho-sigma-operationalization-rho-sig-9829`. Source raised.
- **SP-30: `example-bandit` passes the scope predicate only by a silent hyperstate choice.** **IN**: A.1 landed; `#example-bandit`:42 now states why the drifting means are state under the invariance cut of `#scope-adaptive-system`, and the stationary variant.
- **`PROPOSALS.md` calls the examples `worked-example-*`.** **MOOT**: the file is gone.
- `example-L1`'s on-policy matched-world arithmetic: **IN**.

### R43 — `post-temporal-optimality`, `scope-evolving-software`, `obs-software-epistemic-properties`, `def-feature`

- **The CIY-optimal sequencing of probes across P3's channel table** and **"effective observability" under a reading-time budget** (P1 inspectable only in principle). **WN**: `#obs-software-epistemic-properties` Working Notes bullets 3 and 5 state both as open; the body's P3 consequence (:49) states the sequencing heuristic. No ledger item; the WN lanes own them. R43's AISI reading (missed vulnerabilities in a P1-inspectable codebase were present and unread, so detection under a review budget is an allocation problem) adds a use for the effective-observability formalization, not a different question.
- **Mechanism swap under shared randomness is invisible to behavioural testing** (`#deriv-mechanism-counterfactual-separation`). **IN** (exact). R43's reading onto unlearning and model-editing validation is AISI's to use.
- **"C-BP3" in SP-16 is a dangling label.** **LEDGER** (a cross-reference fault inside an imported item): no C-BP3 exists; the calibration-laboratory template is SP-3 in imported Bundle 1. Raised onto the SP-16 item so whoever rechecks it reads it right.
- **Code-quality bistability spike.** **LEDGER** `item:spikes-proposed-code-quality-bistability-2d-dynamical-fo-0dc9`. Raised once for R43, R46 and R47 together.

### R44 — `result-specification-bound`, `der-change-expectation-baseline`, `impl-foundations-features`

- **Channel capacity caps an LLM agent's tempo, $\mathcal T \le 2C_{\text{channel}}$** (a "belongs elsewhere" aside on `#deriv-persistence-cost`). **LEDGER** `item:llm-instantiations-from-01-audit-gold` (G.2) lists it as instantiation (6). Raised with R44's proposed test and the confound it guards (a channel-limited agent reads as cautious).
- **TST-7, an operational definition of "sufficient".** **LEDGER** `item:todo-tst-7-specification-bound-operational-su-4bd6` (unassigned). Raised with the incident-class reading (specification failure vs deviation under sufficient information).
- **Guessing under pressure: completions that pass surface tests at low $M_{\text{shared}}$** (from `AUDIT-WORKING-193847/74`'s Wandering Thoughts). **ASIDE** here: the audits drain read 193847/74 and disposed its finding (`drain/audits.md`, the 829314/05 + 193847/74 row); a reader's musing with no claim in canon to attach to. If it is ever wanted, its home is the TST-7 item.
- Austin (2001)'s deadline threshold: **IN** (`02-tst-core/lit-review/specification-bound-prior-art.md`).

### R45 — `scope-developer-agent`, `def-comprehension-time`, `def-implementation-time`, `der-dual-optimization`

- **Developer-tempo channels (obs / explore / probe) and what a git-only record can recover per channel** (`spikes/tst-ideas-cycle-2026-05-21/spike-developer-tempo-channels.md`; OUTLINE `--GAP--` row `#def-developer-tempo-channels`). **LEDGER** `item:the-2026-05-21-tst-spike-cycle-carries-four-deve` (G.2), whose part 1 is exactly this, with the estimator asymmetry as the honest result. Raised with R45's per-channel failure taxonomy (and R46 §D's independent finding).
- **TST-8 amortization factor.** **LEDGER** `item:todo-tst-8-turnover-multiplier-amortization-f-b626`; R45 adds nothing. No raise.
- Comprehension dominance under turnover: **IN**.

### R46 — `der-change-investment`, `der-code-quality-as-observation-infrastructure`, `impl-developer-agent`

- **An AI agent under time pressure truncates search rather than degrading from stress; can't-vs-won't as a log discriminator.** **WN**: `#der-code-quality-as-observation-infrastructure` Working Notes bullet 5 states the doubt. The discriminator experiment is the report's own and AISI-facing; I carried the ASF-relevant half (the form of $g(\mathcal T,Q)$ may differ for AI implementers) onto the bistability item.
- **Asymmetric loss-vs-recovery thresholds** (`audits/polish-and-sentiment-ledger.md` S6). **LEDGER** `item:persistence-hysteresis-hypothesis` (C.4) on `#result-persistence-condition`. Raised with the TST instance and R46's empirical test.
- **Bistability not demonstrated.** **LEDGER**, as under R43.
- **Missing `#def-developer-tempo-channels`.** **LEDGER**, as under R45.
- S26 (OUTLINE ordering nit): the audits drain owns the polish ledger's rows (`9491b73f`); not re-checked here.

### R47 — `hyp-conceptual-alignment`, `def-atomic-changeset`, `emp-changeset-size-principle`, `def-discontinuity-distance`

- **The empirical-discontinuity dataset ($\alpha\approx0.06$–$0.12$, $R^2\approx0.52$–$0.72$, human commits only).** **MOOT** as a description of canon: `02-tst-core/empirical-discontinuity/FINDINGS.md` is gone, and `#hyp-exponential-cognitive-load` now reports the one non-circular measurement (elapsed time between commits, three histories), which *disfavors* the count form (:35), with a regression guard that an estimated time cannot test the hypothesis (:87). The reports' reading was correct of the August state and is overtaken.
- **No AI-authored commit run; it should cross author type with dependency structure.** **LEDGER**: the count-vs-structure test is `question:does-per-commit-cost-grow-with-the-dependency-st`; the AI-substrate form is `item:ai-cognitive-load-step-shaped` (C.4). Raised onto the item (questions do not take `raise`).
- **Atomic, content-addressed commits as forensically decomposable records; does that generalize to non-code agent actions?** **IN** for the software claim (`#obs-software-epistemic-properties` P5, Empirical Claim; `item:tst-cheap-falsifiers-and-measurement-design` (c) holds the atomic-commit data-quality point). The generalization to tool calls and browser actions is AISI's question, not a gap in TST, which scopes itself to software: **ASIDE** here.
- **Bistability**: confirmed independently in R47's addendum; raised under R43.

### R48 — `der-change-proximity-principle`, `hyp-exponential-cognitive-load`, `impl-code-structure`

- **Checkpoint spacing $h\lt\log(1/\eta)/\log\Gamma$ and singular-subspace coverage** (`spikes/spike-transient-dependency-amplification.md`, interrupted on $\widehat J_F$). **LEDGER** `item:todo-transient-dependency-amplification-spike-441c` (G.2). Raised with R48's monitor-cadence reading. The ledger holds this one spike under three items (that one, `spikes-proposed-advanced-3-…-a826`, imported `spikes-proposed-transient-dependency-amplification-logog-5fe5`); I named all three in the raise rather than fold them myself.
- **Percolation of representation errors (ADV #9), gated on the above.** **LEDGER** (`spikes-proposed-advanced-9-…-b0b6` and its imported twin). R48 adds nothing beyond the gating; no raise.
- **Count vs dependency structure; $k\approx1.1$–$1.2$ from one atypical repository.** **MOOT/IN** as under R47: canon now says the count form is disfavored and states the structure form as the live candidate.
- **AI agents re-pay the comprehension cost every episode** (829314/09). **LEDGER**, carried onto `item:ai-cognitive-load-step-shaped` with R47.

### R49 — `def-system-coupling`, `def-system-coherence`, `meas-coherence-coupling`, `der-principled-decision-integration`

- **C4, the observer-effect (Goodhart) confounder: a git chronicle used for evaluation stops being an interventional record.** **ADD**, new item `item:a-fourth-confounder-class-for-hyp-causal-discove` (G.2). It sits only in `TST-IDEAS.md` §C2 (:115–127) and the forensic-mining spike (F1, F3); `#hyp-causal-discovery-from-git` lists C1–C3 and no C4 at HEAD, and `item:three-findings-of-the-2026-05-21-tst-forensic-mi` set the rest of F1–F21 aside as "reached `TST-IDEAS.md`", which is not canon. R49 and R50 found it independently. The item asks for the paragraph at discussion grade and for the source's stronger claim (a fresh M1 identifiability-floor instance) to be attempted before it is stated.
- **Does an AI agent's reasoning trace observe C3 (the developer's unrecorded knowledge state)?** **WN**: `#hyp-causal-discovery-from-git` WN bullet 4 already says a planning log "could serve as a partial record of $M_t$". R49/R50's test design and the trustworthiness worry are noted in the C4 item as related, not opened separately.
- **F17, co-change expected but absent ("bugs by omission").** **LEDGER** `item:three-findings-of-the-2026-05-21-tst-forensic-mi` part 2. Raised with R49's reading.
- **TST-4 naming discipline.** **LEDGER** `item:todo-tst-4-git-as-intervention-naming-discipl-936c` (F.1); no raise.
- Coupling, coherence and PDI as such: the report finds nothing there. Nothing to drain.

### R50 — `def-system-availability`, `scope-continuous-operation`, `hyp-causal-discovery-from-git`, `impl-system-measures`

- **C3 via reasoning traces; C4 Goodhart.** As under R49.
- **Developer time and user time added at an unstated 1:1 rate** (849201 gem Fresh-9). **LEDGER** `item:tst-user-developer-time-exchange-rate` (C.1), opened by another lane minutes before I checked (it was absent at my first grep). Raised.
- Availability as standard SRE in AAT vocabulary: **IN**; the report itself says so.

### R51 — `scope-logogenic-agent`, `scope-channel-collapse`, `def-coupled-update-dynamics`, `scope-observation-ambiguity-modulation`

- **$\kappa_{\text{eff}}=\kappa_{\text{processing}}\times\mathcal A(e_\tau)$: is the product form real, at what constants; ambiguity-stratified evaluation suites; the $\hat{\mathcal A}$ estimator.** **MOOT**: the Part II integration (C3, 253d2bca–279b2699) retired $\mathcal A$ and the product law; `#scope-observation-ambiguity-modulation` now carries a fixed-gain tilt hypothesis (:48–54) and a regression guard against restoring either (:129). Their successor is E.1's fixed-gain tilt test, as `item:untested-catalog-predictions-for-e` also records.
- **Goal-last prompt order as a test of the coupling mechanism** (829314/03 Wandering Thoughts). **LEDGER** with an addition: `#def-coupled-update-dynamics`:53 says goal-first placement "is the *mechanism* … it is why $\kappa_{\text{processing}}\approx1$", untagged and underived. A goal-last arm discriminates; but under causal masking the update's tokens still attend to goal and evidence together, so the sentence may name a contributor, not the mechanism. Raised onto `item:todo-loga-2-kappa-text-processing-approx-1-sc-b641` (E.1) with both cautions, rather than a new item, since that item owns the $\kappa\approx1$ claim the sentence explains.
- **Does channel collapse admit a gradient (multimodal, tool-using agents)?** **WN** at `#scope-channel-collapse`, and **LEDGER** `item:todo-loga-1-channel-collapse-scope-narrowing-1217` holds the scope narrowing; R51 adds nothing.
- **LOGA-1/2/3.** **LEDGER** (three items).
- **ADV #11, a per-substrate channel-collapse mechanism for substrate-transfer asymmetry.** **LEDGER** (`spikes-proposed-advanced-11-…-9171`, `substrate-transfer-asymmetry-two-halves-empirica`); R51 adds nothing.
- **SP-30 lists a downstream check of regime (i) in this segment.** **MOOT**: A.1 landed and C3 rewrote the segment's regimes.

## What was read whole, sampled, not reached

*(being written)*

## Adjacent findings

*(being written)*
