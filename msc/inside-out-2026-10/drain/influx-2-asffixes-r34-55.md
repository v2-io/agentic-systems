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

## What was read whole, sampled, not reached

*(being written)*

## Adjacent findings

*(being written)*
