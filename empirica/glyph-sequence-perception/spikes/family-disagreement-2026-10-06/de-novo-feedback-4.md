# De novo feedback 4: the family-disagreement spike after strengthening 3

*2026-10-06, 21:00–21:15 MDT by the clock, a fourth independent session (Claude Opus 5.5), asked for a critical and adversarial pass on the spike as it stands. I read the README, FINDINGS, debrief, integration plan, MAP, NOTES, `strengthening-3.md`, `de-novo-feedback-3.md` whole, the parts of `de-novo-feedback-1.md`, `-2.md` and `strengthening-2.md` that the current FINDINGS cite, METHODOLOGY whole, CATALOG §1, §5–§9, the seal, the head of `CATALOG-GIVEN.md`, and these scripts: `lib.py`, `covs.py`, `spxr.py`, `run_spxr.py`, `abbott.py`, `commit.py`, `values.py`, `choose.py`, `irt.py` (load), `additive.py` (outcome), `features.py`, `de-novo-2/a15.py`, `de-novo-3/c7` and `c8`, and `catalog/given_walk.py`. Everything I computed loads the spike's snapshot through `lib.py` (seal applied first), except `e7`, which reads verifier 3's cached `irtu` predictions (themselves built through `lib.py`). My scripts and logs are in `de-novo-4/` (Appendix). Labels: **[checked]** a claim I re-ran or tested and it holds; **[re-derived]** my own computation on the snapshot; **[inference]**.*

## Summary

1. **Most of what the spike reports as separate findings, for the Claude–Grok contrast, is one phenomenon: whether a mind keeps walking Unicode's code chart where no given order exists** [re-derived]. Splitting contiguous contexts into given walks (alphabets and numbers, `catalog/given_walk.py`) and contiguous runs that walk no given order:
   - On contexts both answered (first answers, paired), Grok stops more than Sonnet by +1.26 logit on contiguous non-given contexts, but only +0.52 on given walks, +0.36 on monotone and +0.12 on other contexts. Opus against Grok: +1.33, +0.22, +0.42, +0.18 (`e5`).
   - 52% of Sonnet–Grok commit disagreements sit on contiguous non-given contexts (42% of shared contexts), and Grok is the one stopping in 90% of them (`e8`).
   - 30 of the 43 flat-split contexts of p001/p002 are contiguous non-given runs, 4 are given walks.
   - Grok's "own lean on a block" (FINDINGS §3, plan item 3) lives entirely on contiguous non-given contexts, and it doesn't carry to other kinds of context in the same block (§3 below).

   So "Grok stops sooner than Sonnet at every level of determinacy" (§2), the per-block lean (§3), the flat splits (§4) and "the larger Claude minds walk the chart more" (§7) are, for this pair, largely the same fact seen four ways. The README's "thresholds that belong to a mind and a question kind" understates it: the Claude–Grok commit gap depends strongly on what the context is.
2. **Plan item 3's per-sequence quantity, for Grok and Gemini Flash, measures per-block appetite for chart walks, not a property of sequences** [re-derived]. In verifier 3's residual frame, Grok's own-beyond-covariates-and-others gain is +299 nats, of which +325 is on contiguous non-given contexts and −25 on everything else. Built only from Grok's answers on *other* kinds of context in the same block set, the feature gains nothing (−2). Gemini Flash's is the same shape (+33 of +57; +4 cross-class). Only Haiku without thinking's lean is spread across classes and partly survives the cross-class test (+371; +97 cross-class). METHODOLOGY §1 says a chart walk is not thereby a sequence, and §2a that a "none" is end evidence, never evidence against. So a stop-lean per block is not the "model-sensitive vs agnostic" parameter on found sequences that Joseph asked about.
3. **On recognition, which runs are model-sensitive can't be read per run yet, and in aggregate Claude and Grok show no run-specific disagreement** [re-derived]. Only 133 real cohere runs have at least 2 answers from each of at least 2 families; none departs from a model with per-mind criteria and slopes (0 at $p \lt 0.01$, 1 at $p \lt 0.05$). Summed over every run two families answered, Claude–Grok matches the model (2,602 runs, $z = +0.1$). Claude–Gemini shows a small excess ($z = +3.0$, 663 runs), and Grok–Gemini agree *more* than modelled ($z = -2.3$), the same affinity strengthening 3 left over in continuation (`e2`, `e3`).
4. **Of §7's three legs for "the larger Claude minds walk the chart more", only continuation supports the heading** [re-derived, checked]:
   - Whole-run recognition: Sonnet's high rejection of non-contiguous runs others accept survives a symmetric panel (it isn't a selection artefact; `e1`), but a logit model with **no contiguity term** predicts it: against Opus 49 observed / 50.2 predicted, against Haiku with thinking 51 / 52.0, against Grok 114 / 97.7 (`e4`). It is what a stricter, more discriminating rater does on middling items. Held out, the per-mind contiguity offset (L4 over L2) is worth 14 nats in 20,037 answers.
   - `choose`: each mind's shift is within 1.8 SE of zero (Sonnet +0.106 ± 0.061, Haiku without thinking +0.107 ± 0.060), and the mind it groups with Sonnet is Haiku without thinking, which in continuation walks the chart *least* of all the minds (stops on 0.32 of contiguous non-given contexts, against Sonnet's 0.085).
5. **Plan item 2's "about 640 nats" is almost all the shuffled controls, not the link** [re-derived]. Of the 635 nats between CATALOG §9's Abbott (A2) and the best logit (L4), 596 are on control items and 40 on the real runs whose strength the catalog reports. Letting controls be heterogeneous inside Abbott (A3) recovers 465. The logit link itself is worth about 160–170. Replacing Abbott with a logit model, as the plan words it, also brings back an unanchored item position, which §9 removed deliberately.
6. **Smaller points** (§6): the debrief's "about a sixth of what I first reported" has no basis I can find (the comparable figures give about 0.6); the README still says 93–99% against FINDINGS' 0.94–0.99; "strict prequential" scores use global parameters fitted on all the answers they score; Opus's cohere slope is reported as 5.5 though it moves from 2.9 to 5.5 across specifications; Haiku with thinking's contiguity coefficient (−1.46, "walks more") disagrees with its paired raw rates (it stops more than Grok on non-given chart walks). Both literature items marked unchecked exist and say what FINDINGS says they do.
7. **The seal holds** [checked]: no kept `choose` or `names` record carries a canary glyph in any field other than its answer.

## 1. The seal

The brief asked me to load through `lib.py`, so I first checked that its rule covers what the records hold. `sealed()` looks at `context`, `candidates` and `shown`. The kept `choose` records have the fields `candidates`, `chart`, `context`, `tags`, `source` and the answer `choice`; `names` records carry `context`, `shown` (the glyphs), `names` (the name strings) and the answer `answer`. Excluding the answer fields, I tested every kept `choose` and `names` record for a canary glyph anywhere in its JSON, and printed only a yes/no and the field names: none. The rule is the catalog's own (`catalog/build.py` `sealed`), identical in code. No answer to a sealed question was read, counted or shown by me. (One self-correction for the record: my first import of `lib` wrote a `__pycache__/` into the spike directory at 21:01; I removed it, and ran everything after with `PYTHONDONTWRITEBYTECODE=1`.)

## 2. What the continuation disagreement rests on

FINDINGS asks "what does the disagreement rest on?" and answers, in §2, with per-mind thresholds by question kind, and separately, in §7, with a chart-walking difference. I tested whether these are one thing. `e5` classifies every continue context as a given walk (contiguous, and a window, rotation, stride or reflection of a given in one dress; the catalog's own `given_walk.is_given`, pairs allowed as windows), a contiguous run that walks no given ("cn" below), monotone, or other. Then, per pair of minds, it compares first plain answers on contexts both answered, so no context selection enters.

| pair (second stops more when positive) | given walks | contiguous, no given | monotone | other |
|---|---|---|---|---|
| Sonnet → Grok | 0.056 / 0.091, +0.52 (n 3,456) | 0.088 / 0.254, **+1.26** (7,325) | 0.539 / 0.627, +0.36 (5,088) | 0.346 / 0.373, +0.12 (1,468) |
| Opus → Grok | 0.078 / 0.096, +0.22 (784) | 0.085 / 0.260, **+1.33** (1,568) | 0.506 / 0.610, +0.42 (1,083) | 0.306 / 0.345, +0.18 (307) |
| Sonnet → Gemini Flash | 0.065 / 0.083, +0.25 (750) | 0.150 / 0.226, +0.50 (965) | 0.548 / 0.512, −0.15 (826) | 0.459 / 0.398, −0.25 (505) |
| Opus → Gemini Flash | 0.059 / 0.053, −0.10 (187) | 0.154 / 0.264, +0.67 (208) | 0.546 / 0.509, −0.15 (163) | 0.461 / 0.326, −0.56 (89) |
| Sonnet → Haiku without thinking | 0.055 / 0.174, +1.30 (3,907) | 0.085 / 0.317, +1.60 (8,612) | 0.546 / 0.599, +0.21 (6,097) | 0.324 / 0.329, +0.02 (1,643) |
| Haiku with thinking → Grok | 0.077 / 0.056, −0.34 (982) | 0.266 / 0.232, −0.18 (1,710) | 0.644 / 0.632, −0.05 (1,113) | 0.489 / 0.352, −0.56 (315) |
| Sonnet → Opus | 0.060 / 0.073 | 0.087 / 0.079 | 0.539 / 0.515 | 0.307 / 0.293 |

(Each cell: stop rates of the two, then the logit gap.) [re-derived] The Sonnet/Opus–Grok gap is three to ten times larger on contiguous non-given contexts than anywhere else. A constant per-mind threshold, NOTES 17:15's "roughly constant +0.6 to +0.7", doesn't describe it. `e8` counts the disagreements themselves: of 2,953 Sonnet–Grok commit disagreements, 1,534 (52%) are on contiguous non-given contexts, which are 42% of the shared contexts, and Grok is the one stopping in 1,376 of them (90%). Sonnet–Opus disagreements, by contrast, run both ways (Opus stops in 79 of 172 there): noise, not a lean.

The 43 flat contexts of p001 and p002 are 30 contiguous non-given runs, 8 monotone, 4 given walks and 1 other. So "Sonnet's side is settled" (debrief) says, in effect, that Sonnet reliably keeps walking the chart in blocks like Braille Patterns, Miscellaneous Mathematical Symbols-B, CJK Compatibility and Modifier Tone Letters, where Grok stops.

[inference] This is a sharper answer to Joseph's third question than FINDINGS gives. Between the large Claude minds and Grok, disagreement about *whether* to continue rests mostly on whether to keep following Unicode's allocation where no given order exists. That is the very property METHODOLOGY §1 and the givens (CATALOG-GIVEN) set apart as not evidence of a felt sequence. One caution on the class itself: "no given" means no order `givens.json` knows. It includes felt ramps without numeric values (block elements, dice, moon phases), Hangul jamo and Han, which CATALOG-GIVEN lists as known gaps. The blocks carrying the gap (§3) are mostly arbitrary allocations, but a cleaner "pure chart" class would need those exceptions marked.

Two things this changes in FINDINGS as written:
- §2 says per-mind criteria "don't line up by family". Within continuation, Sonnet and Opus line up on the chart-walk axis against Grok and both Haikus (Haiku without thinking stops on 0.32 of contiguous non-given contexts it shares with Sonnet; Haiku with thinking 0.27 against Grok's 0.23). It's the *larger Claude minds*, which is §7's heading, but §2 and §7 don't say they are describing the same gap.
- The per-mind contiguity coefficients in §7 (Haiku with thinking −1.46, Grok −0.49, Gemini Flash −0.00) are partial effects inside a model that also has a shared item position, own and others' block rates and six other covariates. They aren't "how readily each mind walks the chart": Haiku with thinking's coefficient says it walks more than Grok, but on contexts both answered it stops *more* on non-given chart walks (0.266 against 0.232). Its coefficient is large because it stops a great deal on monotone and other contexts. Gemini Flash's −0.00 sits beside a paired stop rate on non-given chart walks (0.224) no different from Grok's (0.250). If FINDINGS wants a per-mind chart-walk number, the paired rates by class are model-free and say what the debrief means.

## 3. The per-(block, mind) lean is, for Grok, chart-walk appetite per block

Plan item 3 proposes, as "the measurable form" of a per-sequence model-sensitivity parameter, a per-(Unicode block, mind) lean beyond the context's look and beyond the other minds' rate on the block. I located that lean in verifier 3's residual frame (its cached `irtu` prequential predictions, halves of block-set groups held out; `e7`). I added one covariate, "given walk", to its eight, so my totals differ slightly from c7's (+770 here against +894).

**Own beyond covariates and others, by the class of the answer predicted** (held-out nats):

| mind | total | given walks | contiguous, no given | monotone | other |
|---|---|---|---|---|---|
| Grok | +299 | −8 | **+325** | −17 | −0 |
| Haiku without thinking | +371 | +110 | +142 | +129 | −10 |
| Gemini Flash | +57 | +8 | +33 | +4 | +12 |
| Haiku with thinking | +28 | +5 | +14 | +9 | −1 |
| Sonnet | +18 | −3 | +5 | +11 | +6 |
| Opus | −3 | −1 | −1 | −1 | +0 |

**The same, with own and others' features built only from the block set's *other* classes** (so a chart walk in a block is predicted from the mind's answers on that block's alphabet runs, monotone runs and others, never other chart walks): Grok −2, Gemini Flash +4, Sonnet −8, Haiku with thinking −20, Haiku without thinking **+97** (cg +25, mono +75).

The cross-class feature is noisier than the same-class one, so a null alone could be low power. But Haiku without thinking's +97 shows the frame can detect a cross-class lean when one exists, and Grok's chart-walk data are its largest class (8,896 answers). [inference] Grok's lean is "in this block, Grok declines to walk the chart (or doesn't)", not a disposition toward the block's sequences. A model-free view says the same (`e6b`, permutation of block labels within class, Sonnet–Grok paired gaps). Block-to-block heterogeneity of the gap is 12.6 times its permutation expectation on contiguous non-given contexts, against 4.0 on given walks, 2.7 on monotone and 1.2 on other (permutation 99% about 1.4–1.7). The blocks where Grok stops most against Sonnet are Musical Symbols (+0.91 in stop rate, n 44), Supplemental Mathematical Operators (+0.70, n 98), Miscellaneous Symbols and Arrows (+0.70, n 73) and Miscellaneous Mathematical Symbols-B (+0.63, n 86). Contexts within one block are overlapping windows of the same walks, so the permutation reference is too narrow in absolute terms; the comparison *between classes* is what I lean on.

What this means for plan item 3 [inference]:
- For Grok and Gemini Flash, the proposed per-(block, mind) number would carry how far each walks Unicode's allocation, block by block. That is a fact about chart-following, and it belongs beside the chart route's measures (CATALOG §7), not in a "model-sensitive sequence" slot.
- It is measured on stopping, and METHODOLOGY §2a reads a "none" as end evidence, never evidence against a sequence. A per-block stop lean is therefore a lean in where a mind calls an end, not in what it recognises. That was true before this finding, and the integration plan doesn't say it.
- Haiku without thinking's lean is the only one with the shape the debrief describes (block-wide, crossing kinds of context). It's also the mind whose thresholds MAP §1 and the thinking-felt spike already flag as a deliberation condition of its own.

## 4. Which runs are model-sensitive in recognition?

Joseph's question was about *found sequences*, and METHODOLOGY §1 makes recognition the final goal. The spike's modelling is almost all on continue stops, so I asked the question directly of cohere (`e2`). The model is `abbott.py`'s L3 (logit; per-mind criterion by set class and per-mind slope; item position from a per-population grid prior), fitted on all real and shuffled cohere items. For each real run, $T$ is the log-likelihood gain of a family-specific position over a shared one, with a posterior-predictive $p$ (1,000 draws).

- **Per run, nothing can be read yet.** Only 133 real runs have at least 2 answers from each of at least 2 families. Of those, 0 have $p \lt 0.01$ and 1 has $p \lt 0.05$, against about 1 and 7 expected under no interaction (posterior-predictive $p$ is conservative, so fewer is expected). With one or two answers per family on most runs, no single run can be called model-sensitive in recognition.
- **In aggregate** (`e3`, every real run two families answered, at least one answer each; the run's position drawn from its prior times the answers of minds *outside* the two families, so the data under test don't inform it; 2,000 draws):

| families | runs | $\sum T$ observed | simulated | $z$ |
|---|---|---|---|---|
| Claude–Grok | 2,602 | 619.8 | 615.8 ± 27.3 | +0.1 |
| Claude–Gemini | 663 | 235.1 | 191.8 ± 14.3 | +3.0 |
| Grok–Gemini | 433 | 86.5 | 111.0 ± 10.8 | −2.3 |

Split by set class, Claude–Gemini's excess is mostly on non-contiguous runs (+2.7). These are nine tests, and the model's per-mind parameters were fitted on the same data, so I read the two departures as suggestive. [inference] Two things follow. First, between Claude and Grok, recognition of whole runs shows no run-specific disagreement beyond each mind's criterion and discrimination: on this evidence, found sequences are model-agnostic between those two families in recognition. Second, the Grok–Gemini affinity strengthening 3 couldn't absorb in continuation shows up in recognition too, which makes it more likely to be a real shared disposition than a quirk of the continue model.

For the planner [inference]: if per-sequence model-sensitivity in recognition matters (and for signa, which are read, it is the version that matters), cohere has to be re-asked within families on the same runs. Per-family information weighting (METHODOLOGY §5) asks each family once readily; the second and third answers per family that a per-run test needs are what's missing.

## 5. FINDINGS §7's evidence for "the larger Claude minds walk the chart more"

**Recognition.** The model-free figure ("Sonnet rejects a non-contiguous run every other mind accepted 0.26 of the time, against 0.04–0.07") conditions each mind on "every other mind said yes". For Grok, that panel includes Sonnet, the strictest judge of non-contiguous runs; for Sonnet it doesn't. I made it symmetric (`e1`): for each pair, the panel is every mind *except* both, and the two are compared on the same runs. Sonnet's rate holds, 0.27–0.35 depending on the partner, against Opus 0.09, Haiku without thinking 0.09, Haiku with thinking 0.10, Grok 0.07, Gemini Flash 0.12 (panel of at least 2 answers; similar with at least 3). [checked] The fact stands.

What it shows is another matter (`e4`). Fit L2, logit with a criterion and slope per mind and **no** contiguity term, and predict each mind's "no" on exactly those panel-selected runs from the panel's answers:

| Sonnet against | Sonnet's "no" on non-contiguous runs, observed / predicted | the other's, observed / predicted |
|---|---|---|
| Opus | 49 / 50.2 | 16 / 18.8 |
| Haiku with thinking | 51 / 52.0 | 19 / 27.4 |
| Haiku without thinking | 127 / 111.0 | 40 / 42.4 |
| Grok | 114 / 97.7 | 28 / 32.7 |
| Gemini Flash | 66 / 49.9 | 23 / 27.0 |

[re-derived] Most of Sonnet's 0.26 follows from its criterion and its slope (1.56, against Grok's 0.69): non-contiguous runs are middling items, and a sharper, stricter rater turns down more of them. Against the Claude minds the fit is exact. Against Grok, Haiku without thinking and Gemini Flash an excess of about 15 remains, which L4's contiguity offset doesn't remove either (99.9 predicted against Grok). Held out, L4 beats L2 by 14 nats in 20,037 answers. So recognition gives little support for a contiguity lean as such. It does show Sonnet as the most discriminating rater, a different fact.

**`choose`.** Verifier 1's table, which FINDINGS cites without uncertainty: Sonnet +0.106 (SE 0.061, 137 pairs), Haiku without thinking +0.107 (0.060), Grok −0.044 (0.054), Gemini Flash −0.099 (0.084). No mind is 2 SE from zero, and the Sonnet–Grok difference is about 1.9 SE before any allowance for looking at four minds. The mind it groups with Sonnet is Haiku without thinking, which in continuation is the least willing chart-walker of all (§2). So this leg doesn't line up with the heading's "larger Claude minds".

**Continuation** carries the heading, and §2 above sharpens it to contiguous runs with no given order. I'd suggest §7 say that the chart-walk difference is a continuation finding, give the paired rates, and report the other two legs as what they are: Sonnet as the strictest, most discriminating rater of whole runs, and a `choose` tilt within noise.

## 6. Abbott against logit (FINDINGS §8, plan item 2)

I re-ran `abbott.py` with all seven variants (`abbott.log`). It reproduces exactly: A2 −0.4773, A3 −0.4541, L2 −0.4463, L4 −0.4456 per answer, over 20,037 answers. Decomposed:

| step | nats |
|---|---|
| A2 → L4 (the "about 640") | 635 |
| A2 → A3 (Abbott, controls heterogeneous) | 465 |
| A3 → L2 (the link) | 156 |
| L2 → L4 (contiguity offset) | 14 |

| population | answers | A2 → L4 |
|---|---|---|
| real contiguous | 4,260 | +9 |
| real other | 6,153 | +30 |
| shuffled contiguous | 3,906 | +144 |
| shuffled other | 5,718 | +452 |

[re-derived] 596 of the 635 nats are earned on the shuffled controls. On the runs whose strength the catalog reports, the logit model gains 40 nats over Abbott in 10,413 answers (A1 ties L3 on contiguous runs, as verifier 2 noted). FINDINGS §8's sentence "Abbott's main misfit is treating a shuffled control as pure guessing" is right. Plan item 2 ("Replace Abbott with a logit model … about 640 nats on cohere") credits the link with what the controls earn.

There is also a cost the plan doesn't name. CATALOG §9 reports strength as Abbott's excess yes rate because it is identified ("There is no unanchored $\theta$"). A logit item position is anchored only once a contrast is defined. Under A3 the anchor collapses (Sonnet's and Opus's $c$ fall to 0.00–0.03; verifier 2 §5). Verifier 2's paired contrast (a run's position against its own shuffles', which share its glyph set) is the anchor that keeps R's claim, "this order of these glyphs". [inference] The defensible recommendation is narrower than the plan's: model the shuffled controls as heterogeneous items paired by glyph set, report R as the run-minus-own-shuffle contrast, and treat the link (Abbott or logit) as a secondary choice worth about 160 nats.

## 7. Smaller points

- **"About a sixth of what I first reported"** (debrief; strengthening 3 summary: "about a sixth of what strengthening 2 implied"). Strengthening 2 reported the mind-specific step as +1,471 / +1,586 nats; strengthening 3 reports +884 / +978, about 0.6 of it. Per answer, 0.019 against 0.011. I can't find a baseline that gives a sixth. If it's the own feature's gain *alone* (verifier 3: +6,115) set against +900, it compares a different quantity. Joseph reads this as the size of the retreat, so the number matters.
- **README "What happened"** still says 93–99%; FINDINGS §1 says 0.94–0.99 (verifier 3 §5 flagged it).
- **"Strict prequential"** (FINDINGS §6, strengthening 3 §3). `run_spxr.py` fits every global parameter on all the snapshot's rows, then scores the same answers prequentially: the per-context posterior and the block features use earlier rounds only, the per-mind coefficients and mixture weights don't. With about 100 global parameters in 77,489 answers the optimism is small, and `2mf` and `irtu` are scored the same way, so the ranking stands. "Prequential in the item posterior and features, global parameters in-sample" is the accurate label.
- **Opus's cohere slope**, reported as 5.5 in FINDINGS §8, is 5.51 under L2, 2.87 under L3 and 4.61 under L4 (`abbott.log`). Verifier 2 called it near-separation. It shouldn't be quoted as a point value beside the others.
- **FINDINGS §2's "Grok stops sooner than Sonnet at every level of determinacy"** is true as binned. §2 above shows the size of that gap depends on the kind of context, from +0.12 to +1.26 logit, so "a per-mind threshold" is the wrong summary for that pair.
- **Literature.** Both items FINDINGS marks unchecked exist and match: Cacioli, "LLMs as Signal Detectors: Sensitivity, Bias, and the Temperature-Criterion Analogy" (arXiv 2603.14893, March 2026), which separates sensitivity from criterion and reports unequal-variance evidence distributions; and Altıntaş et al., "TokSuite: Measuring the Impact of Tokenizer Choice on Language Model Behavior" (arXiv 2512.20757). Cacioli's unequal-variance finding bears on §8: a per-mind slope is the equal-variance logit's way of absorbing it. I checked the abstracts only.

## What I did not do

- I didn't re-run the spike's own model fits (`ladder.py`, `run_spxr.py`), the p001/p002 scoring or the calibration tables; §3's location of the lean is in verifier 3's residual frame, not the spike's LNB/SPXR frame. Whether the spike's +884 / +978 splits the same way by class is the natural next check.
- I didn't define a cleaner "pure chart" class (marking felt ramps without numeric values, jamo and Han), so "contiguous, no given order" carries those cases.
- I didn't check the `▁` scan, `seedsel.py`, `reask.py` or the sheet-mate analysis.
- I read `de-novo-feedback-1.md`, `-2.md` and `strengthening-2.md` only where the current FINDINGS cite them.

## On the brief

It worked for me: "no limits on what aspect you audit" is what let me step off the continue-stop modelling, which three verifications had already worked over, and ask the recognition version of Joseph's question directly. The seal note and the "load through `lib.py`" fact saved time; the one thing I'd add for a fifth pass is that `given_walk.py` exists and can be imported, since the given/non-given split turned out to be the axis that ties the findings together.

I'm staying on the line for follow-up questions.

## Appendix: `de-novo-4/`

Run from inside `de-novo-4/` with `PYTHONDONTWRITEBYTECODE=1 /opt/homebrew/bin/python3 <script>`. Each loads the snapshot through the spike's `lib.py`; `e7` reads `dn3/preq_irtu.pkl` in the session scratchpad (verifier 3's cache). Logs are beside each script.

- **`e1_sym_reject.py`**: Sonnet's rejection of runs a panel accepted, with the panel excluding both minds compared (§5).
- **`e2_run_family.py`**: per-run family × run test on cohere under L3 (§4). Writes its ranked runs to the path given as its argument.
- **`e3_aggregate.py`**: the aggregate version, per pair of families and set class (§4). It imports `e2_run_family`, which runs `e2` first and writes `e2_rows.json` beside it.
- **`e4_sonnet_lean_pred.py`**: L2 and L4 predictions for `e1`'s table (§5).
- **`e5_chart_given.py`**: paired stop rates by class: given walk, contiguous with no given order, monotone, other (§2).
- **`e6b_block_lean_perm.py`**: block-to-block heterogeneity of paired gaps, by class, against a permutation of block labels (§3).
- **`e7_own_by_class.py`**: verifier 3's c7 frame, the own-lean gain split by class, and the cross-class variant (§3).
- **`e8_discord_by_class.py`**: commit disagreements by class and direction (§2).
- **`abbott.log`**: `abbott.py A1 A2 A3 L1 L2 L3 L4`, unmodified (§6).
