# Spike: family disagreement (2026-10-06)

**The question.** Where do the model families agree about which runs are sequences, and where don't they? Which sequences are model-sensitive, and which are (at least among frontier families) model-agnostic? And what does the disagreement rest on? Asked by Joseph before any planner term was built on disagreement: *"look at the data, and then we'll probably need to have a model-sensitive vs agnostic finding / parameter on found sequences, or possibly something else depending on what the data is actually showing, if anything"*.

**What happened.** Disagreement between families turned out to be mostly about whether to commit, at thresholds that belong to a mind and a question kind, not about what the sequence is. Frontier minds that commit agree on content 94–99% (0.94–0.99) of the time. The family-shaped effects are few and nameable. See `FINDINGS.md`.

**Where everything is:**
- `FINDINGS.md`: the findings;
- `proposed-integration-plan.md`: the agent's suggestions for the planner and the catalog;
- `debrief.md`: the agent's debrief to Joseph;
- `MAP.md`: the map written before any computing, with its expectations;
- `NOTES.md`: the timestamped working log, including the readings withdrawn;
- `de-novo-feedback-1.md`, `strengthening-1.md`: the first verification and the spike agent's answer to it;
- `prereg-flat-splits.json`, `prereg_round.py`, `prereg_check.py`, `prereg-result-1.md`: the pre-registered test (round `p001`) and its result;
- `de-novo-feedback-2.md`, `de-novo-2/`: the second verification, its scripts, and its competing model and prediction;
- `de-novo-feedback-3.md`, `de-novo-3/`: the third verification, its scripts and its timed p002 baseline;
- `strengthening-3.md`, `strengthening-3-logs/`: the spike agent's answer to the third verification;
- `de-novo-feedback-4.md`, `de-novo-4/`: the fourth verification;
- `snapshot/`: what rebuilds the spike's snapshot (`lib.py --from-manifest`);
- `strengthening-2.md`, `strengthening-2-logs/`: the spike agent's answer to the second verification (the sequence-level structure, the probing effects, no model calibrated on all checks);
- `prereg-third-minds.json`, `prereg2_gen.py`, `prereg_gen.py`: the second pre-registration (round `p002`, third minds) and the generators of both;
- `*.py`: the scripts, all loading through `lib.py`, which drops sealed answers first.

**Provenance.** The spike agent (Claude Opus 5.5) wrote `MAP.md`, `NOTES.md` and the scripts. The harness refused its writes of the report files, so the coordinating session landed `FINDINGS.md`, `proposed-integration-plan.md` and `debrief.md` unchanged from the agent's final report. The same write succeeded from the coordinating session, so the refusal was particular to the agent's session. **Timestamps:** `NOTES.md`'s section times (16:36 to 18:30) are the agent's estimates, not clock readings: it has no clock. By file times its scripts were written between 16:36 and 16:54 and the log last at 16:57, when it reported (for instance its "16:45" section uses `distance.py`, written at 16:39). **Status:** verified 2026-10-06 (`de-novo-feedback-1.md`): every scripted number reproduces; four headline readings don't hold as stated (the threshold model's fit depends on an arbitrary prior and over-predicts disagreement about twofold; content agreement is mostly agreement on the code chart, smaller but real off it; the chart tilt points at Sonnet *and* Haiku without thinking, not Sonnet alone; finding 5 re-expresses what finding 3 asserts). What stands is listed in its summary. The strengthening attempts it names are sent back to the spike agent; nothing is built on the threshold reading until they land and are checked.

**Strengthened** (`strengthening-1.md`, 17:15–17:35 by the clock, same snapshot, now rebuildable from `snapshot/`): a calibrated threshold model (a mixture with a criterion and a slope per mind and a familiarity term; single-answer disagreement, predicted out of sample, matches observation within 0.87–1.07). Under it, flat splits are borderline contexts, not settled ones, which withdraws the debrief's "asking again won't settle anything". Logit beats the catalog's Abbott model on cohere by about 640 nats held out. Gemini Pro's `▁` holds on the scan itself, and the familiarity effect is confirmed. **Pre-registered:** the flat-split reading predicts what the 43 Sonnet-continues / Grok-stops contexts do when asked again (`prereg-flat-splits.json`, committed before the test existed). The test is round `p001` (`prereg_round.py` builds it, `prereg_check.py` scores it). **Result** (`prereg-result-1.md`): Grok stopped again at 29/42 = 0.69, inside its band near the top; Sonnet continued again at 42/43 = 0.98, *above* its band [0.70–0.91]. So the model's "borderline, partly chance" reading holds for Grok's side, and Sonnet's continuing at these contexts is steadier than the model allows. Sheet size (one question per sheet in the test) moves stop rates by a few points in that direction, far less than Sonnet's departure. **Verified again** (`de-novo-feedback-2.md`, a second fresh session, with its scripts and a competing model in `de-novo-2/`). Every number in strengthening 1 reproduces. Logit beats Abbott on cohere, and Gemini Pro's `▁` holds. But the calibrated model has no mind × item term: every mind agrees with itself more than it predicts (Sonnet 40 disagreements against 71 predicted, Grok 163 against 217, Haiku without thinking 222 against 309), and that explains p001. So "flat splits are borderline, partly chance" is not supported. A competitor with a per-(item, mind) term fits better held out and on p001, and it is still miscalibrated. Sonnet's contiguity lean has a model-free form: it rejects 26% of non-contiguous runs that every other mind accepts, against 4–7% for the others. FINDINGS.md still states several withdrawn claims, and is due a rewrite.

**Strengthened again** (`strengthening-2.md`, 18:02–19:30 by the clock). No model the agent fitted is calibrated on every check at once; it says exactly where each fails. What the attempt found, held out in every fold: the largest mind-specific structure is at the level of sequences (a mind's lean across a sequence's contexts, about +1,500 nats beyond a shared sequence effect of about +2,300), not single contexts. Three effects of the study's own machinery bear on every reading: same-sequence sheet-mates (−0.70 logit on stopping, about 7% of continue answers), adaptive re-asking, and seed-targeted selection. `FINDINGS.md`, the integration plan and the debrief were rewritten by replacement (landed unchanged by the coordinating session, the harness again refusing the agent's writes). A second pre-registration (`prereg-third-minds.json`, committed before round `p002` existed) asks the 43 flat contexts of Opus and both Haikus. **Not yet independently verified.**

**Pre-registered test 2** (`prereg-result-2.md`, round `p002`): the 43 flat contexts asked of Opus and both Haikus. The fixed rule (a win needs a Bayes factor of 10 over each other model) couldn't report what the test found. Pairwise, the model without a mind × item term loses on Haiku without thinking by about 8,000 to 1. Haiku with thinking stopped 6 times against about 20 predicted by every model, mostly on contexts where it had no earlier answer, and a naive per-mind baseline beat all three models. About half of that miss is chart class, which no model sees (34 of the 43 contexts are chart walks).

**Verified a third time** (`de-novo-feedback-3.md`, `de-novo-3/`). Strengthening 2's numbers that the verifier re-ran reproduce, but several readings narrow:

- most of the "shared sequence effect" is a prior from what a context looks like (contiguous, monotone, blocks, length), which no item model had;
- the mind-specific lean is about +900 to +1,100 nats rather than +1,500, carried by Grok, Haiku without thinking and Gemini Flash, and none for Sonnet or Opus once chart class is in (Sonnet's is its chart lean);
- the unit is a Unicode block, not a sequence;
- half or more of the sheet-mate effect is selection (−0.70 → at most −0.32);
- FINDINGS §3 contradicts itself on the per-item interaction;
- three NOTES entries were corrupted by shell expansion;
- two coordinator times were false, now corrected here and in `prereg-result-2.md`.

Sent to the spike agent for its answer.

**Strengthened a third time** (`strengthening-3.md`, about 21:00). The verifier's reading holds and is quantified:

- what a context looks like (chart class, blocks, length) predicts continuing far better than anything per mind, mostly with one shared coefficient set;
- a mind's own lean on a Unicode block is real but small (+884 / +978 nats held out, about 0.01 per answer), mostly Grok's, Haiku-without-thinking's and Gemini Flash's;
- no sheet-mate format effect is shown within the same context and mind;
- part of Sonnet's "steadiness" was a modelling artifact (a narrow latent grid with Sonnet as anchor).

The clearest family difference is chart-walking: Opus and Sonnet keep walking the chart far more readily than Grok and Gemini. Best model: 10 of 38 calibration checks outside their bands, chiefly a Grok–Gemini affinity. `lib.load()` now refuses a snapshot that disagrees with its manifest. FINDINGS, plan and debrief were rewritten by replacement (landed unchanged). **Not yet independently verified.**

**Verified a fourth time** (`de-novo-feedback-4.md`).

- **One phenomenon.** Between the large Claude minds and Grok, the commit gap is chiefly whether to keep walking the code chart where no given order exists: +1.26 logit on contiguous runs with no given order, at most +0.52 elsewhere. Grok stops in 90% of those disagreements. "Grok stops sooner", the per-block lean, the flat splits and the chart-walk heading are largely that one fact.
- **The per-block lean.** For Grok and Gemini Flash it is chart-walk appetite per block, not a property of sequences; only Haiku without thinking's spans the block.
- **Recognition.** Claude and Grok show no run-specific disagreement in recognition (2,602 runs, z = +0.1), so found sequences look model-agnostic between them. Per run, nothing can be read yet.
- **The Abbott-to-logit gain.** Its ~640 nats are almost all earned on the shuffled controls (596 of 635). The verifier recommends the run-against-its-own-shuffles contrast, which catalog build 7 now uses.

Sent to the spike agent for a closing pass.

**Closed** (`strengthening-4.md`, about 21:35; the closing pass). In short:

- **Recognition.** Judged whole, Claude and Grok don't disagree about which runs are sequences beyond each mind's strictness and sharpness. Which runs are model-sensitive in recognition can't be read per run until cohere is re-asked within families.
- **Continuation.** The family difference is chart-walking where no given order exists: Sonnet and Opus keep walking; Grok and Gemini Flash stop.
- **Perception.** The clearest perceptual family effect is `▁` for Gemini.

FINDINGS, plan and debrief were rewritten by replacement (landed unchanged). Open threads are listed in the plan (item 7).
