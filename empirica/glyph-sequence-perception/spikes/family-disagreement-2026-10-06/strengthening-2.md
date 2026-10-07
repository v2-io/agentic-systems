# Strengthening 2: answering the second verification

*2026-10-06, 18:02–19:30 MDT by the clock (`date`), the spike agent (Claude Opus 5.5), answering `de-novo-feedback-2.md` and `prereg-result-1.md`. Same snapshot as before (`snapshot/manifest.json`), plus round p001 where stated. The model-choice criterion was written into NOTES at 18:03, before any fit. I knew p001's aggregate counts from the coordinator's message, but no per-context answer until after model choice (NOTES, 19:17). Labels: **[measured]**, **[inference]**, **[open]**; a reading I predicted and that failed is marked **[failed]**.*

## Summary

The verifier asked for a threshold model that is right, not just better, calibrated on cross-mind disagreement, within-mind repeats and flat splits at once. **I didn't get one.** No model I fitted passes all the checks. The attempt did change what is known:

1. **The study's adaptive design matters for every check of consistency** [measured]. A context is re-asked far more often after some answers than others: Sonnet's in a later round 0.077 of the time after it continued, 0.005 after it stopped (Grok 0.107 / 0.035, Haiku without thinking 0.077 / 0.023). A check that predicts a mind's repeats without conditioning on its own first answer compares against the wrong population. The valid frame is prequential: predict each answer from everything answered in earlier rounds, since that is all the planner used. Conditioned this way, `2mf` still over-predicts flips for every mind (Sonnet 40 against 59.2, Grok 163 against 233.8, Haiku without thinking 222 against 295.2). **The verifier's conclusion holds:** a mind × item term is missing.
2. **The largest missing structure is at the level of sequences, not contexts** [measured]. A context's answers are predicted far better once other contexts of the same sequence are known. Taking the set of Unicode blocks a context spans as the unit, the gains held out, each in all five folds, are:
   - a shared sequence effect: about +2,300 to +2,500 nats over `2mf`;
   - a **mind-specific** sequence effect on top of it: **about +1,500 to +1,600 nats**.

   For scale, the verifier's per-item interaction gained +31.8 nats. A per-item interaction on its own (Gaussian or sparse) gains nothing held out. Under strict prequential scoring, with features from earlier rounds only, the sequence model beats the item-level models by about 4,000 nats.
3. **What remains miscalibrated has identifiable causes, several on the measurement side** [measured]:
   - **Same-sequence sheet-mates.** A question on a sheet that also carries other contexts of the same sequence is continued far more often than any model predicts: stops 0.59–0.60 of predicted on first answers, logit −0.70 ± 0.04. This is a probing effect (METHODOLOGY concern 1).
   - **Seed votes.** The planner targeted contexts with seed votes, and the continue models never see them. In early rounds, seeded first answers stop 0.72 of predicted and seeded repeats 0.33.
   - An unexplained remainder in early rounds (unseeded repeats 0.70).
   - Feature models over-predict same-round disagreement between minds: the shared component is too weak.
4. **Round p001, scored per context after model choice** [measured]: `irtu` −31.80, the block-set model −34.65, `2mf` −37.08 (log score, both minds). The model best on the snapshot is not best on these 43 flat contexts. **Every model under-predicts Sonnet's steadiness there** (42 of 43 continued; `irtu` expected 38.1, the block-set model 35.7).
5. **A second shared factor is a Haiku axis, not a family axis** [measured]. Pairwise residuals under one factor look family-shaped (within-Claude and within-{Grok, Gemini} pairs agree more than predicted, Claude–Gemini pairs less). A second factor's loadings are Haiku without thinking 1.94, Haiku with thinking 0.97, Sonnet 0.56, and Opus 0.04, Grok 0.04, Gemini Flash 0.11, Gemini Pro −0.11. It groups the Haiku model, partly Sonnet, and not Opus.
6. **Loose ends.** `prereg_gen.py` regenerates `prereg-flat-splits.json` with every field identical apart from the write time and git head. FINDINGS.md is rewritten by replacement, with the history in NOTES. A third-mind pre-registration is generated (`prereg-third-minds.json`, §6).

## 1. Selection, and the checks that survive it

**The selection** [measured, `reask.py`]:

| mind | re-asked in a later round after continuing | after stopping |
|---|---|---|
| Sonnet | 1,231 / 16,024 = 0.077 | 24 / 4,986 = 0.005 |
| Grok | 1,288 / 12,059 = 0.107 | 229 / 6,461 = 0.035 |
| Haiku without thinking | 973 / 12,702 = 0.077 | 177 / 7,640 = 0.023 |

Among items selected on the first answer, disagreement between a mind's first two answers is $E[p(1-p)] \cdot (c_0 + c_1) / (c_1 E[p] + c_0 E[1 - p])$, not $2E[p(1-p)]$, when re-asking happens with rates $c_y$ after answer $y$. With Sonnet's rates and its overall stop rate of about 0.24, that is about 0.69 of $2E[p(1-p)]$. So `de-novo-feedback-2.md` §2's within-mind table (Sonnet 40 against 71.5 predicted) overstates the misfit. The conclusion it draws is right anyway.

**Selection-robust checks** (`checks2.py`; a mind's second answer predicted given its first and every other mind's answers; flat splits as "both second answers repeat the first"):

| | `2mf` | `irtu` | beta-binomial (`bb.py`) |
|---|---|---|---|
| within-mind flips, Sonnet: obs / pred [95%] | 40 / 59.2 [47–72] | 40 / 49.3 [38–62] | 40 / 45.6 [34–58] |
| Grok | 163 / 233.8 [209–257] | 163 / 194.9 [171–217] | 163 / 187.7 [164–209] |
| Haiku without thinking | 222 / 295.2 [270–321] | 222 / 240.6 [215–265] | 222 / 232.6 [207–257] |
| flat Sonnet-continues / Grok-stops, both repeat | 44 / 37.6 [28–48] | 44 / 54.3 [43–66] | 44 / 58.9 [48–70] |
| checks outside band (of 16) | 6 | 3 | 5 |

The beta-binomial (`bb.py`: each mind's propensity on an item drawn around the shared mean with its own concentration) fits within-mind consistency better than `irtu` but over-predicts flat splits. To be as self-consistent as observed, minds must be near-certain per item, and then they come out too independent of one another.

**Prequential** (`preq.py`: each answer predicted from earlier rounds only). This exposed a misfit no earlier check had shown: every model over-predicts stops on *repeat* answers, concentrated in rounds c001–c027. Under `irtu`: Sonnet 16 against 29.4 and Grok 58 against 110.7 there; Grok 264 against 274.9 in c028–c095. §3 traces where it comes from.

## 2. The sequence is the unit

**A residual test first** (`blockresid.py`, `grouping.py`). Using `irtu` prequential residuals, leaving the item out, does a mind's mean residual on *other* contexts in the same group predict its answer here? Held-out gains (nats; groups split in halves for fitting and scoring), by grouping:

| grouping | Sonnet | Opus | Haiku without thinking | Haiku with thinking | Grok | Gemini Flash |
|---|---|---|---|---|---|---|
| last glyph | +1,036 | +99 | +307 | +150 | +1,318 | +170 |
| last two glyphs (set) | +1,417 | +110 | +359 | +116 | +1,592 | +157 |
| block of the last glyph | +712 | +90 | +759 | +253 | +1,079 | +157 |
| **set of blocks spanned** | **+2,017** | +270 | **+1,384** | +370 | **+1,876** | +189 |

**The model** (`lnb.py`): a nonparametric shared position per context, a per-(context, mind) Gaussian intercept, and two leave-the-context-out offsets: the mind's own stop rate on other contexts of the same block set, and the other minds' rate there. Held-out log-likelihood per answer (`fold_lnb.py`; by item: `irt.heldout`'s folds; by block: folds over the block of the last glyph, never training on a test block):

| model | by item | by block |
|---|---|---|
| `2mf` | −0.4676 | −0.4730 |
| no features (shared position + per-item intercept) | −0.4680 | −0.4732 |
| SPX, no features (sparse per-item interaction, `spx.py`) | −0.4679 | −0.4731 |
| others' sequence rate only | −0.4376 | −0.4404 |
| **others' and own sequence rate** | **−0.4186** | **−0.4200** |
| SPX + both rates | −0.4187 | −0.4202 |

Each step is positive in all five folds of both schemes. The mind-specific step (others' rate only → both) is +1,471 nats by item and +1,586 by block. With features from earlier rounds only (`lnb_prefix.py`), the prequential log score is −0.5211 per answer, against −0.5731 (`2mf`) and −0.5727 (`irtu`).

Fitted coefficients (block-set model, all data; `lam` own sequence rate, `kap` others'): Sonnet 1.36 / 0.77, Opus 0.97 / 2.25, Haiku without thinking 1.66 / 0.23, Haiku with thinking 0.82 / 1.44, Grok 1.88 / 0.91, Gemini Flash 0.86 / 1.26, Gemini Pro 0.25 / 2.38. Grok and Haiku without thinking lean hardest on their own behaviour across a sequence; Opus and Gemini Pro on others'.

**A fitting artifact found and fixed.** A first fit lost Sonnet's per-item intercept to $\tau = 0$, where the gradient in $\tau$ is exactly zero. Updating $\log\tau$ with a floor fixed the trap, but the fitted $\tau$ still falls toward 0.05: with sequence features present, the likelihood doesn't want a Gaussian per-item term for Sonnet. Held-out figures were unchanged by the fix.

## 3. What is still wrong, and why [measured]

Strict prequential calibration of the block-set model: 21 of 38 checks fall outside their 95% bands (SPX: 23 of 38). Two patterns:

- **Same-round pairs** disagree less than predicted for most pairs (Sonnet–Grok 3,027 against 3,408; Grok–Gemini Flash 465 against 613). With features, the per-mind terms make minds more independent than they are.
- **Repeat answers** stop less than predicted (Sonnet 34 against 69.8). **[failed]** I predicted in writing (NOTES, 18:35) that the sequence features would close this gap. They made Sonnet's worse.

Three contributors, each tested (`sheetmates.py`, `seedsel.py`, `irtu` prequential; stops observed / predicted):

| | first answers, c001–c027 | repeats, c001–c027 | first, c028+ | repeats, c028+ |
|---|---|---|---|---|
| same-sequence sheet-mates | 611 / 1,027.8 (0.59) | 6 / 19.7 (0.30) | 295 / 489.0 (0.60) | 34 / 31.7 (1.07) |
| no such sheet-mates | 14,671 / 14,192.8 (1.03) | 200 / 294.3 (0.68) | 7,297 / 7,179.7 (1.02) | 319 / 345.3 (0.92) |
| context has a seed vote | 1,550 / 2,143.2 (0.72) | 13 / 39.8 (0.33) | 88 / 82.8 (1.06) | 9 / 11.2 (0.80) |
| no seed vote | 13,732 / 13,077.4 (1.05) | 193 / 274.1 (0.70) | 7,504 / 7,585.9 (0.99) | 344 / 365.8 (0.94) |

- **Sheet-mates** of the same sequence lower stopping by −0.70 ± 0.04 logit on first answers (−0.45 ± 0.21 on repeats). A mind that sees the sequence elsewhere on its sheet continues it. This is a format effect, the study's co-equal object, and it touches about 7% of continue answers.
- **Seed votes** are information the planner used and the continue models don't have. Selection on them isn't ignorable for these models.
- **The remainder** (early unseeded repeats 0.70) is unexplained. [inference] The likeliest source is other planner inputs outside the continue model (the ported triad-era answers). Untested.
- **A tested-and-not-supported hypothesis.** That Sonnet's excess steadiness is arithmetic on contiguous chart walks: its flips under `irtu` are 0.75 of predicted on contiguous contexts, 0.83 on monotone and 0.34 (1 against 3) on others. Spread, not specific.

## 4. Round p001

Scored per context after model choice (`p001score.py`):

| | Grok stops (29 of 42) | Sonnet continues (42 of 43) | total log score |
|---|---|---|---|
| `2mf` (pre-registered) | expected 24.4 [18–30]; $P(\geq 29)$ 0.094; −26.30 | 34.8 [30–39]; $P(\geq 42)$ 0.0009; −10.78 | −37.08 |
| `irtu` (verifier) | 30.4 [25–36]; 0.746; −24.98 | 38.1 [34–42]; 0.035; −6.82 | **−31.80** |
| block-set model | 25.9 [20–32]; 0.197; −25.32 | 35.7 [31–40]; 0.0028; −9.33 | −34.65 |

**Reading** [inference]. On the flat contexts, Sonnet's continuing is settled, more than any model here allows. Grok's stopping repeats about seven times in ten, as `irtu` predicts. The block-set model loses on p001 because its fit gave Sonnet almost no per-item steadiness: the sequence term took that variance across the whole dataset. At flat contexts, where Sonnet departs from the others, per-item steadiness is what counts. So both kinds of structure are real, and no single model here holds both in the right proportions.

Under these models, then, "a flat split is settled" is half right, not a rule: Sonnet's side yes, Grok's side mostly. What the planner should do with that follows in §7.

## 5. Is there a family axis? [measured]

Pairwise same-round disagreements, observed over predicted, one factor without features (`twof.py`):

- **below 1:** Sonnet–Opus 0.85, Haiku with–without thinking 0.91, Grok–Gemini Flash 0.88, Grok–Gemini Pro 0.92, Gemini Flash–Pro 0.90;
- **above 1:** Opus–Gemini Flash 1.21, Haiku without thinking–Gemini Pro 1.17, Haiku without thinking–Gemini Flash 1.09, Haiku without thinking–Grok 1.06, Sonnet–Gemini Flash 1.06.

That pattern is what a family axis would produce. A second shared factor tests it directly. Its loadings (sign fixed by Sonnet ≥ 0):

| Sonnet | Opus | Haiku without thinking | Haiku with thinking | Grok | Gemini Flash | Gemini Pro |
|---|---|---|---|---|---|---|
| +0.56 | +0.04 | +1.94 | +0.97 | +0.04 | +0.11 | −0.11 |

In-sample the log-likelihood improves by 98 for 7 parameters; held out by item, $-0.4671$ against $-0.4683$ per answer for one factor, about +93 nats. Same-round pairs outside their bands fall from 7 to 4. The four left are themselves family-shaped: Sonnet–Opus agree more than predicted (0.82), as do Grok–Gemini Flash (0.91) and Sonnet–Haiku with thinking (0.93); Opus–Gemini Flash agree less (1.22). The variants with block-set features were stopped unfinished. [inference] The second dimension is the Haiku model (in both conditions) and partly Sonnet. Opus sits with Grok and the Gemini minds. So it isn't "Claude against the rest". Beyond it, a smaller residual affinity remains between the two large Claude minds, and between Grok and Gemini Flash. The nearest description is "the two Claude core minds", and of those mostly Haiku. Whether that reflects model size, the core minds' answering every sheet, or something else isn't settled here.

## 6. A third-mind pre-registration (proposed round p002)

`prereg-third-minds.json` (generated by `prereg2_gen.py`): the 43 flat contexts, each once more as a plain continue question on a one-question sheet, asked of Opus, Haiku without thinking and Haiku with thinking. Gemini is paused until Saturday. Each model's P(stop) per context and mind, conditioned on the snapshot and p001.

| expected stops of 43 (95%) | `2mf` | `irtu` | block-set model |
|---|---|---|---|
| Opus | 9.5 [5–15] | 6.9 [3–11] | 8.0 [3–13] |
| Haiku without thinking | 20.3 [14–27] | 12.1 [7–18] | 13.0 [8–19] |
| Haiku with thinking | 21.9 [16–28] | 20.4 [14–27] | 19.9 [14–26] |

**Reading, fixed in the file.** Per mind, a per-context log score for each model. A model "wins" a mind when it beats each other model by more than $\log 10$; otherwise the result doesn't discriminate. Counts are reported against the bands. Haiku without thinking is where `2mf` and the interaction models differ most. `irtu` and the block-set model nearly coincide in count everywhere, so only the per-context likelihood can separate them. **Caveats:**

- None of the three models is calibrated on all checks.
- The block-set model is uncalibrated, and p001 favoured `irtu`.
- Opus's and the Haikus' first answers under one-question sheets and the current prompt are part of the test. The sheet-size effect measured in `prereg-result-1.md` is a few points.

## 7. What this changes for the integration plan [inference]

- **Item 1 (planner).** No disagreement term. Two better-founded changes instead:
  - Treat the **sequence**, not the context, as what an answer informs, since a context's answers carry about 1,500 to 2,500 nats of information about its siblings.
  - **Keep contexts of one sequence off a shared sheet** (as the probe already does for cohere and `choose`), or tag and model it: same-sequence sheet-mates move stopping by −0.70 logit.

  A flat split's Sonnet side needs no re-asking; its Grok side repeats about seventy percent of the time. Asking a third mind is more informative than asking either again, as the verifier found.
- **Item 2 (catalog combination rule).** Logit against Abbott on cohere stands (three reproductions). For continue, a mind's reading of a sequence is better modelled at the sequence level than per context.
- **Item 3 (per-sequence quantity).** It now has a concrete, held-out-supported form: for each sequence and mind, the mind's own propensity on that sequence against the other minds' (the `lam` term's posterior), with its evidence count. It is the largest mind-specific structure found. It still needs a calibrated home model, and seed and sheet effects removed, before it is a catalog number.

## 8. Limits and open

- No model is calibrated on all checks; §3 lists the causes found and the remainder.
- The block-set unit is a proxy for "the sequence". Contexts of one walk span the same block set, but so do unrelated contexts in a big block.
- The sequence features are leave-the-context-out rates, not latent per-sequence effects. A crossed random-effects model (mind × sequence) would be the principled version and wasn't fitted.
- Seeds, sheet-mates and triad-era planner inputs aren't in any model.
- Gemini's coverage is thin throughout (and absent since 16:08).
- Fits were capped at 60 EM iterations in the folds and 150 on all data; the all-data block-set model was checked to have converged (last 40 iterations: +2.5 log-likelihood in total).

## Files added

`bb.py`, `checks.py`, `checks2.py`, `preq.py`, `lnb.py`, `lnb_prefix.py`, `spx.py`, `twof.py`, `fit_bb.py`, `fit_lnb.py`, `fold_lnb.py`, `run_checks2.py`, `run_preq.py`, `run_preq2.py`, `run_preq3.py`, `run_preq4.py`, `run_spx.py`, `run_twof.py`, `blockresid.py`, `grouping.py`, `sheetmates.py`, `seedsel.py`, `p001score.py`, `reask.py`, `prereg_gen.py`, `prereg2_gen.py`, `prereg-third-minds.json`. Run logs and per-fold held-out results are copied into `strengthening-2-logs/` (the selection-robust and grouping outputs, which ran in the foreground, are reproducible from their scripts).
