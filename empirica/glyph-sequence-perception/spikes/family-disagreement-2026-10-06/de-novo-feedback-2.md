# De novo feedback 2: the family-disagreement spike after strengthening 1, and round p001

*2026-10-06, 17:36–18:05 MDT by the clock, a second independent session (Claude Opus 5.5), asked for a critical and adversarial pass on the spike as it now stands. I read the spike's README, MAP, FINDINGS, NOTES, debrief, integration plan, `de-novo-feedback-1.md`, `strengthening-1.md`, the pre-registration and its two round scripts, every script `strengthening-1` added (`irt.py`, `flatread.py`, `settled.py`, `abbott.py`, `glyphscan2.py`, `lib.py`) and the ones they import (`additive.py`, `values.py`, `tok.py`), then METHODOLOGY, CATALOG and the seal file. Everything I computed loads through the spike's `lib.py` (sealed answers dropped first) on the spike's snapshot, except round p001's answers, which are continue answers read from `data/answers/p001.jsonl`. Labels: **[reproduced]** a number of the spike's, recomputed; **[re-derived]** my own computation on the snapshot; **[p001]** from the test round's answers; **[inference]**. My scripts and their outputs are in `de-novo-2/` beside this file, so they outlast the scratchpad; Appendix A says what each does.*

## Summary

The strengthening is careful, its numbers reproduce, and the pre-registration was the right move. Its central reading did not survive the test it set up.

1. **The pre-registered prediction failed on Sonnet, and Grok came in high** [p001]. Grok stopped on 29 of the 42 contexts it answered with a stop or a glyph: 0.69 against a predicted 0.58 [0.44, 0.72]. That is inside the band, in its upper part (one-sided $P \approx 0.09$). Sonnet continued on 42 of 43: 0.977 against a predicted 0.81 [0.70, 0.91]. Under the model's own per-context probabilities, $P(\geq 42) \approx 9 \times 10^{-4}$. The pre-registration said how to read only Grok's share, but both shares were predictions of the same model. Read together, flat Sonnet-continues / Grok-stops contexts are not "borderline contexts where two 2/2 runs are partly chance". Sonnet's side is settled, and Grok's side repeats about seven times in ten. That moves the reading part of the way back toward the debrief's withdrawn "asking again won't settle anything", but not for the original reason: a per-mind threshold plus a shared item strength (the 1PL that verification 1 found miscalibrated). The data point to a stable leaning of each mind on each item.
2. **The cause is visible in the snapshot, independently of p001** [re-derived]. The calibrated model has no mind × item term, and every mind agrees with itself more than the model predicts. Given only the other minds' answers, it predicts more disagreement between a mind's first two answers (from different rounds) than occurs: Sonnet 40 observed against 71 predicted (1,255 items), Grok 163 against 217 (1,517), Haiku without thinking 222 against 309 (1,150). `strengthening-1` checked cross-mind disagreement, which a model can match by making each mind noisier than it is. That is what this one does. A competitor with a per-(item, mind) intercept, whose p001 prediction I wrote down before reading any p001 answer (`de-novo-2/PREDICTION.md`), wins held-out likelihood in all five folds (+31.8 nats) and scored better on p001 for both minds. It isn't right either (§2).
3. **"Flat splits are about three-quarters as informative to re-ask" depends on the measure and the model** [re-derived]. Under the spike's own model, the mutual information between the next answer and the item's latent state is *higher* on flat items than on average (Grok 0.135 nats against 0.082). Under the interaction model, it is about average for Grok and the best mind and lower for Sonnet. The variance-of-$b$ measure in `flatread.py` ignores what an answer says about the item's class. So integration-plan item 1 as revised ("ordinary borderline contexts, informative at about average rates, no special term in either direction") has lost its premise. Its conclusion may still be right, on other grounds (§3).
4. **p001 changed the protocol for Grok** [re-derived]. Every Grok continue answer in the snapshot was given under the pre-c096 prompt. p001 used the current one (a soft target "around N or fewer", fated option order) on one-question sheets. For Sonnet the prompt change moved nothing on the same items ($+0.000 \pm 0.017$, 86 items), and single-question sheets moved Grok's stop rate by $-0.005 \pm 0.020$ (220 items). So the confound is probably small, but for Grok it is unmeasured, and the pre-registration doesn't mention it (§4).
5. **What holds** [reproduced, re-derived]:
   - every `strengthening-1` number I re-ran reproduces exactly: `2mf`'s held-out figure on continue, the calibration table, the flat-split table, the triad one-per-sheet table, all of `abbott.py`, `glyphscan2.py` and `settled.py`;
   - the snapshot rebuilds from the manifest (184,459 of 184,459, every round's content unchanged);
   - the pre-registration's per-context probabilities reproduce from `irt.py` to within 0.001;
   - calibration still holds when the mind parameters are fitted on other items, so "out of sample" is fair;
   - logit beats the catalog's Abbott model on cohere;
   - Gemini Pro's `▁` stands on the scan;
   - Sonnet's contiguity lean has a model-free form (§5).
6. **FINDINGS.md still states withdrawn claims as findings** (§6).

## 1. Round p001: what came back

**The count** [p001; `prereg_check.py` and `de-novo-2/a13.py`]:

| | answered | observed | `2mf` predicted, expected [95%] | $P(\geq \text{obs})$ under `2mf` | competitor (§2), expected |
|---|---|---|---|---|---|
| Grok stops again | 42 of 43 | 29 (0.69) | 24.4 [18, 30] | 0.094 | 30.4 |
| Sonnet continues again | 43 of 43 | 42 (0.977) | 34.8 [30, 39] | 0.0009 | 38.1 |

Per-context log score (the prediction file's own probabilities): Grok −26.30 under `2mf` against −24.98 under the competitor; Sonnet −10.78 against −6.82. `prereg_check.py`'s "settled" stand-in (repeat with probability 0.95) scores Grok −40.43 and Sonnet −5.15. It loses on Grok and wins on Sonnet. Both p001 halves point the same way: these minds repeat their flat-split answers more often than the calibrated model says.

**How it should be read.** The pre-registration's `how_to_check` reads only Grok's share: "inside the band supports 'mostly borderline contexts, partly chance'; near 1 supports 'settled'". Grok's 0.69 sits between those, and nearer the top of the band. Sonnet's band was pre-registered beside it, and the count came in 7.2 above its expectation: 2.9 standard deviations, $P \approx 0.0009$. A reading that cites only the first line of `prereg_check.py` ("inside the band") would report a pass the data don't give. *What p001 shows* [inference]: on these 43 contexts Sonnet's continuing is settled. Grok's stopping is stable on most of them but not all. The model's regression of both toward the item's shared position is too strong. That is nearer the debrief's first reading ("asking again won't settle anything") than `strengthening-1`'s withdrawal of it. But the first reading's mechanism, the 1PL thresholds, was miscalibrated, and §2 says what the data point to instead.

**Two things the binary coding hid** [p001]:
- Grok's one non-binary answer, the one left out, was `TB` after `㎅㎆㎇` (KB MB GB): the semantically next unit, written as letters because the square block has no terabyte glyph. Sonnet walked the chart: `㎈㎉㎊…` (cal, kcal, pF…). That is a commitment and a content split. Coded as missing, it vanishes. Some of Grok's historical "none" answers may be the same thing: a next element exists, but not as one glyph. That can't be checked from "none" answers.
- Where both continued (13 contexts), the first glyph matched in 10. The three splits are of the kinds FINDINGS 1 names: dress (`➌④` → Sonnet `➎`, Grok plain `⑤`), a skipped glyph (`⣜⣝` → Grok `⣟`, Sonnet `⣞`), and one Grok answer I can't read as a sequence (`𝞠𝞡𝞢` → `𝕋𝕐𝚽`, soft target 3).

**Order of events, for the record.** I fitted the competitor and computed its p001 prediction at about 17:44. I wrote `de-novo-2/tau-pred.json` at 17:46:06 and `PREDICTION.md` at 17:46:14 (its last touch was a one-word fix to its own timestamp). The drain recorded `data/answers/p001.jsonl` at 17:46:07. Before 17:47 I had listed `data/rounds/p001/raw/` and read `sheets.jsonl` (the questions), but no answer content. My first read of answer content was at about 17:47:30. Only file times and my word attest this, so weigh the competitor's p001 score accordingly. Its held-out win (§2) doesn't depend on p001 at all.

## 2. The missing term: minds are more consistent with themselves than the model allows

**The check `strengthening-1` didn't run** [re-derived, `de-novo-2/a6.py`, `a7.py`]. For each mind, take the items it answered at least twice in different rounds. Predict whether its first two answers agree from the item's posterior given the *other* minds' answers only, as `irt.pair_checks` does for pairs. Under the calibrated `2mf`:

| mind | items | disagreements observed | predicted | in the bin the model calls borderline (predicted $P(\text{stop})$ 0.4–0.6): observed / predicted rate |
|---|---|---|---|---|
| Sonnet | 1,255 | 40 | 71.5 | 0.22 / 0.31 (n = 18) |
| Grok | 1,517 | 163 | 217 | 0.135 / 0.181 (n = 141) |
| Haiku without thinking | 1,150 | 222 | 309 | 0.22 / 0.46 (n = 103) |

The shortfall holds in every predicted-probability bin with more than 20 items, for all three minds. The two small top bins go the other way (Sonnet 0.6–0.8, n = 16; Grok 0.8–1.0, n = 18). Cross-mind single-answer disagreement is calibrated (ratios 0.87–1.07, reproduced, and unchanged when mind parameters are fitted on other items, `a5.py`). Within-mind agreement is not. Both facts are what a model with no mind × item term produces when the data have one. Each mind's stable item-specific leaning is counted as noise, and noise large enough to match cross-mind disagreement is too large for a mind's repeats.

`settled.py` didn't catch this. Its check conditions on Grok's own first two answers, which partly absorbs a mind's leaning, and it has 199 items. Its "(2)" part has no data: no flat item has a later answer, as `strengthening-1` says.

**The competitor** (`de-novo-2/irtu.py`). It is `2mf` with a per-(item, mind) random intercept in the graded class:

$$\operatorname{logit} P(1 \mid m, b, u) = \alpha_m + s_m b + \gamma_m x_i + \tau_m u_{im}, \qquad u_{im} \sim N(0, 1).$$

So a mind's repeats on one item share $u_{im}$, and other minds don't. $\tau = 0$ is `2mf`. It's fitted by EM on a $33 \times 9$ grid.

- **Fit:** log-likelihood $-36{,}155.4$ against $-36{,}186.4$ for 7 more parameters. Held-out, on `irt.heldout`'s folds: +6.4, +2.0, +4.5, +12.1 and +6.8 nats per fold, +31.8 over 77,489 answers ($-0.4672$ against $-0.4676$ per answer).
- **$\tau$:** Sonnet 1.35, Grok 1.61, Haiku without thinking 2.20, the others 0.8–1.2.
- **Haiku without thinking:** its slope on the shared dimension rises to 0.82, and most of its behaviour is item-specific ($\tau$ 2.2). That is the "self-consistent but not following the shared dimension" reading `strengthening-1` gave, now as a parameter.

**Where it is still wrong** (`a14.py`). Cross-mind calibration stays at 0.84–1.08. Within-mind disagreement improves but is still over-predicted: Sonnet 40 against 61.8, Grok 163 against 185, Haiku without thinking 222 against 256. Flat-split counts now go wrong the other way for two pairs:
- Sonnet continues / Haiku stops: 65 observed against 103 predicted;
- Sonnet / Grok: 43 against 51.3;
- Haiku / Grok: 38 against 30.0, much closer than `2mf`'s 16.2.

The interaction lives in the near-certain classes too (a mind that keeps stopping where everyone else continues), and a single Gaussian intercept in the graded class doesn't place it right. Flat-split counts didn't discriminate the two models well: each fails on a different pair.

**What this changes** [inference]:
- **The flat-split reading** in `strengthening-1` §1 ("borderline contexts where two 2/2 runs are partly chance") and integration item 1's revised premise rest on a model whose within-mind noise is too large. p001 confirms that on Sonnet's side.
- **The calibration claims** in Summary point 1 ("calibrated") are true of cross-mind disagreement only. A model meant to separate "a mind's threshold" from "this item" should be checked on within-mind repeats too, since that is what distinguishes the two.
- **Plan item 3's third part** ("departures of a mind from the threshold model") is exactly the term `2mf` lacks. In `2mf`, departures are noise by construction. A per-sequence departure quantity needs a model with a mind × item term, and then it is that term's posterior.

**Strengthening worth attempting, not done here:** a model in which item class membership can also differ by mind (or an interaction in every class), checked on all three things at once:
- cross-mind single-answer disagreement;
- within-mind repeats across rounds;
- flat-split counts in both directions.

p001 and any later re-asks of flat-split contexts are then held-out data. If the analysis is done in a separate session, it would help to keep the model choice blind to p001.

## 3. How informative is re-asking a flat split?

`flatread.py` measures an answer's value as the expected reduction of $\pi_M \cdot \operatorname{Var}(b \mid M)$, the class-M mass times the variance of $b$ within it. That measure misses what an answer says about whether the item is near-certain or graded (class C, S or M). On an average item, with posterior mass 0.42 / 0.11 / 0.47 on C / S / M, that is most of what an answer says. METHODOLOGY §5 defines "most clarifying" by mutual information. Here is the mutual information between one more answer and the item's latent state [re-derived, `a12.py`, `a16.py`]:

| | Grok | Sonnet | best mind |
|---|---|---|---|
| `2mf`, flat Sonnet/Grok items (43) | 0.135 | 0.061 | 0.200 |
| `2mf`, all items both answered (17,337) | 0.082 | 0.065 | 0.168 |
| competitor, flat items, about the shared state | 0.058 | 0.037 | 0.194 |
| competitor, all items both answered | 0.055 | 0.050 | 0.188 |

Under the spike's own model, re-asking Grok on a flat item is 1.6 times as informative as on an average item, and asking the best mind 1.2 times, not three-quarters; Sonnet's is about average. Under the competitor, re-asking Grok or the best mind is about average, and re-asking Sonnet is less: part of its answer is about its own leaning, not the item. So the size of "how informative" swings with the model. What is stable is that the best mind to ask about a flat split is a third mind, not one of the two. That fits integration item 1's original instinct, and it suggests a natural next test: ask the 43 contexts of Opus, the Gemini minds and Haiku [inference].

## 4. The pre-registration: what was right, and what to change next time

**Right:**
- the prediction was committed (dc42b1cb) before the round existed;
- per-context probabilities are listed, so every answer is scored on its own context;
- one question to a sheet;
- the check script marks its secondary analyses as not pre-registered, and its "settled" stand-in as chosen without evidence.

**To change** [re-derived where numbered]:
- **Name the reading of every pre-registered number.** Sonnet's band had no stated reading, so its failure has no pre-agreed meaning. The natural one ("the model's within-mind regression is too strong") is §2's.
- **Make the alternative a calibrated model, not "a share near 1".** Against `2mf`, the interaction competitor's band ([0.58, 0.86] for Grok) overlaps the pre-registered one from 0.58 to 0.72. Inside/outside one band can't separate them; a likelihood ratio can. For Grok the two are equally likely at 28 stops of 43, and each stop moves the ratio by about 2.
- **State protocol differences between the fitting data and the test.** Every Grok continue answer in the snapshot is pre-c096 (old prompt, continue option first, "up to 24"). p001 used the current prompt: soft target 3–24, "none" first on 19 of 43 sheets, and one question per sheet. Only 1,422 of Grok's 20,525 continue stop-or-glyph answers were on one-question sheets. Within items, the effects that can be measured are small (Summary 4), so this probably doesn't explain p001. But a mind's first answers under a new prompt are part of the test, and the file should say so.
- **Recompute the band for what was answered.** The primary verdict uses the 43-context band for 42 answers. Here that changes nothing; with more failures it would. The secondary Poisson-binomial does it right.
- **Decide in advance what a non-binary answer counts as.** Grok's `TB` was a commitment to a non-glyph continuation, and it was left out. Counted as a commitment, Grok's stop share is 29/43 = 0.674.
- **Commit the generator.** No committed script writes `prereg-flat-splits.json`. I reproduced its probabilities from `irt.py`'s `2mf` fit to within 0.001 (`a3.py`), so nothing is lost, but the band computation (Bernoulli draws on the per-context probabilities, no parameter uncertainty) is only inferable.

## 5. Abbott against logit, and the contiguity lean

**Reproduced exactly** (`abbott.py` A1, A2, A3, L1, L2, L4): −0.4782, −0.4773, −0.4541, −0.4500, −0.4463, −0.4456, and the per-population table. The comparison is fair as built: the same nonparametric item freedom, and A3 has more mind parameters than L2.

Three readings to add [re-derived, inference]:
- **On real contiguous runs, A1 (−0.2645) fits slightly better than L2 (−0.2656)**, and only L4 beats it. Logit's whole advantage is on real non-contiguous runs and on controls. That's consistent with `strengthening-1`'s account, worth saying in one line.
- **Under A3, "the control rate" stops being a guess rate.** Sonnet's and Opus's $c$ fall to 0.00–0.03, so "excess yes over the control rate", the catalog's R strength, loses its anchor. What the logit model makes available instead is a *paired* contrast: the run's position against its own shuffle's, which share a glyph set. That is closer to R's claim ("this order of these glyphs") than a population rate. Integration item 2 could say so.
- **Opus's cohere slope (5.51; 4.61 in L4) and its contiguity offset (+5.62 ± 2.14)** have the look of the near-separation `strengthening-1` names for Gemini Pro on inhibit. The offset ÷ slope conversion for Opus inherits that. No claim in `strengthening-1` rests on Opus alone, but the contiguity table puts it first in logit units.

**The contiguity lean in model-free form** (`a15.py`). Take real runs that every *other* answering mind called coherent (at least 3 other answers, all yes). How often does each mind say no?

| mind | contiguous runs | other runs |
|---|---|---|
| Sonnet | 15/426 = 0.035 | 107/411 = 0.260 |
| Haiku without thinking | 4/414 = 0.010 | 19/322 = 0.059 |
| Haiku with thinking | 4/187 = 0.021 | 7/135 = 0.052 |
| Grok | 7/380 = 0.018 | 12/283 = 0.042 |
| Opus | 4/201 = 0.020 | 5/134 = 0.037 |
| Gemini Flash | 8/156 = 0.051 | 8/123 = 0.065 |
| Gemini Pro | 6/44 = 0.136 | 4/33 = 0.121 |

Sonnet rejects a non-contiguous run that everyone else accepts about one time in four, against 4–7% for the rest. Gemini Pro (12%, on 33 answers) rejects both classes alike, which looks like a lapse rate, not a lean. On odds, Haiku without thinking comes second (about 6×, from 4 rejections on contiguous runs), Grok about 2.4×, Opus and Gemini Flash under 2×. This doesn't depend on Abbott, logit or a reference pool. It also rules out one alternative explanation of Grok's small offset, a high lapse rate on clearly coherent runs: Grok's is 0.018. Sonnet's lean is robust; Haiku-without-thinking's is suggestive, on small counts.

## 6. Smaller points

- **FINDINGS.md's body still asserts what has been withdrawn.** Among its claims:
  - "That model predicts every flat Sonnet-continues / Grok-stops split";
  - "the minds' slopes are nearly equal (0.82–1.16)";
  - "So the tilt is Sonnet's rather than Claude's";
  - "Gemini Flash is the readiest of all minds";
  - finding 5 as written.

  Its header says "Not yet independently verified". The debrief is the opposite case: it carries a hold note on "asking again won't settle anything", and p001 partly restores that sentence, though for a different reason (§1). A reader who opens FINDINGS alone, as the README invites, gets the refuted versions. `strengthening-1` says "The landed FINDINGS are left as they are". Under this program's integration-is-replacement discipline, the findings file should state present truth, with the history in NOTES. That is a rewrite to make once this round is answered.
- **The README** doesn't list `strengthening-1.md`, the pre-registration, the round scripts or `snapshot/`. Its status line predates strengthening 1.
- **Haiku without thinking has a negative slope on triads** (−0.66 in `irt.py triad-commit --one-per-sheet`, reproduced). Its commitment runs against the shared dimension there. Its flat-split cells on triads are empty, so nothing rests on it, but it's a second instance of "this mind isn't on the shared dimension", worth a line.
- **`glyphscan2.py`'s sub-threshold candidates** reproduce: Sonnet `ᚒ` (−5.58, n = 8), `ᬌ` (−4.33), `ᚑ` (−4.21, n = 16). `ᚑ` and `ᚒ` are adjacent Ogham letters (U+1691, U+1692), which makes them slightly more interesting than two isolated cells.
- **The brief's pointer**: the seal is `audits/SEAL-canary-choose-2026-10-06.md`. There is no `SEAL.md` at the study root.

## 7. The seal

Every snapshot analysis loaded through `lib.py`, whose `sealed` I compared with `catalog/build.py`'s: identical. D controls are `choose` records with `probe.control` neutral, so the kind test covers them. One check (`a2.py`'s era counts in my scratchpad, folded into Summary 4) read `data/answers/c*.jsonl` directly. It applied `lib.sealed` to each record before counting, and counted continue answers only. p001 holds only continue answers. I queried, counted and displayed no sealed answer.

## What I did not do

- I didn't fit the richer interaction model §2 calls for, or test whether p001's prompt change matters for Grok. The latter needs Grok answers under both prompts on the same items.
- I didn't re-run `irt.py`'s held-out table for cohere, triads and inhibit, or the cohere and inhibit calibrations. I reproduced the continue column and the triad table only.
- I didn't check the literature again.
- I didn't verify the 17:46 ordering beyond file times (§1).

## On the brief

It was what an audit needs: the seal, the live processes, the running round and the Python binary. The licence to "do with p001 what you judge right" made the competing prediction possible, and that turned out to be the most useful thing I did. One fact would have saved a few minutes: the seal file's actual path.

I'm staying on the line for follow-up questions.

## Appendix A: `de-novo-2/`

Run from that directory with `/opt/homebrew/bin/python3`; each loads the spike's snapshot through `lib.py`.

- **`a1.py`, `a2.py`, `a4.py`.** The 43 contexts' original answers by round, sheet size and prompt version. Stop rate by option order, soft target and sheet size from c096. Within-item effects of the prompt era and of one-question sheets.
- **`a3.py`.** Reproduces the pre-registration's per-context probabilities and band from `irt.py` `2mf`.
- **`a5.py`.** Calibration with mind parameters fitted on other items (5-fold).
- **`a6.py`, `a7.py`.** Within-mind retest agreement against the `2mf` prediction from other minds' answers; `a7` keeps first two answers from different rounds and bins by predicted probability.
- **`a8.py`.** A cruder beta-binomial competitor, superseded by `irtu.py`; it gave Grok 0.76, Sonnet 0.91.
- **`irtu.py`, `a9.py`.** The interaction model and its fit; `tau-pred.json` holds its parameters and per-context p001 predictions.
- **`a10.py`.** Likelihood ratios between the two models over p001 counts, written before the answers were read.
- **`a11.py` (`a11.out`).** Held-out comparison.
- **`a12.py`, `a16.py`.** Mutual information.
- **`a13.py`.** p001 scored per context under both models.
- **`a14.py`.** The competitor's calibration checks.
- **`a15.py`.** The model-free contiguity table.
- **`PREDICTION.md`.** The competing prediction as written before p001 was read.
