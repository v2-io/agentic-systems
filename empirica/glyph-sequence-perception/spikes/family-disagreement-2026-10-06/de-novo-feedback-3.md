# De novo feedback 3: the family-disagreement spike after strengthening 2, and round p002

*2026-10-06, 19:28–19:58 MDT by the clock, a third independent session (Claude Opus 5.5), asked for a critical and adversarial pass on the spike as it stands. I read the README, FINDINGS, debrief, integration plan, `strengthening-2.md`, `de-novo-feedback-2.md`, NOTES, `prereg-third-minds.json` and `prereg-result-2.md` (which landed while I worked), METHODOLOGY whole and CATALOG §1–§12, and these scripts: `lib.py`, `irt.py`, `lnb.py`, `fit_lnb.py`, `fold_lnb.py`, `grouping.py`, `blockresid.py`, `preq.py`, `checks2.py`, `sheetmates.py`, `seedsel.py`, `reask.py`, `twof.py`, `run_twof.py`, `prereg2_gen.py`, `prereg2_check.py` and the diff to `prereg_round.py`. I did not read `de-novo-feedback-1.md`, `strengthening-1.md` or `MAP.md`. Everything I computed loads the spike's snapshot through `lib.py` (seal applied first), except round p002's answers, which are continue answers read from `data/answers/p002.jsonl`. My scripts are in `de-novo-3/` beside this file (Appendix A). Labels: **[reproduced]**, **[re-derived]** (my computation on the snapshot), **[p002]**, **[inference]**, **[post hoc]** (computed after I had read p002's answers).*

## Summary

1. **On p002, a naive baseline beats all three pre-registered models, and the reason isn't "a mind's own record on the context"** [p002]. Before reading any p002 answer I wrote a competing prediction (`de-novo-3/PREDICTION-p002.md`, 19:31:19; `p002.jsonl` was recorded at 19:31:43): each mind's stop rate pooled over the 43 flat contexts, nothing fitted. Summed log score over the three minds: baseline −56.24, `lnb` −61.73, `irtu` −62.65, `2mf` −75.18. The whole margin is Haiku with thinking, and it sits on the 30 contexts where that mind had **no** earlier answer: there it stopped 3 times, the models expected about 14, and the baseline beats the best model by 10.0 nats. On the 13 contexts where it did have a record, the baseline doesn't beat the models. So `prereg-result-2.md`'s reading ("its own history on these contexts does") explains 13 of the 43 contexts, not the failure. Its other mechanism is wrong as stated: none of `2mf`, `irtu` or `lnb` has a second dimension, so none can pull through the Haiku axis. Computed post hoc, the spike's two-factor model (the Haiku axis) still expects 18.1 stops for Haiku with thinking. Part of it, at least [inference]: 34 of the 43 flat contexts are contiguous chart walks, and Haiku with thinking stops on 0.195 of contiguous contexts in the snapshot, against 0.34 overall. The models never see that a context is a chart walk. Chart class alone takes the expectation from about 20 to about 12, not to 6.
2. **The fixed reading rule could not report the result the test was built to find** [p002]. A model "wins" only if it beats *each* other model by $\log 10$. The pre-registration itself noted that `irtu` and `lnb` nearly coincide, so neither could ever win, and `2mf` losing by 9 nats on Haiku without thinking is reported as "not discriminating". Pairwise ratios (which the file also asks for, and `prereg-result-2.md` does give) are the reading that carries information here.
3. **The largest structure missing from the item models is properties of the context computable from its glyphs, and it is mostly shared by the minds** [re-derived]. In a residual frame (Appendix A, `c7`, `c8`), a few glyph covariates (contiguous, monotone, one block, number of blocks, length, unfamiliar last glyph, size of the last step) gain +9,204 nats held out over `irtu`'s prequential predictions. One coefficient vector for all minds gets +8,639 of that. The block-set group features of strengthening 2 gain +5,279 in the same frame. The spike's model comparisons never gave an item model a covariate besides familiarity, so its "+2,300 shared sequence effect" is measured against models with a cold prior for every unseen context.
4. **A mind-specific lean on a block does exist, but it is smaller than stated, it belongs mostly to Grok and Haiku without thinking, and Sonnet's share is its chart lean** [re-derived]:
   - With the other minds' feature taken as per-mind residuals, which removes differences in which minds answered a block, the mind's own block feature adds about +1,100 nats beyond it (strengthening 2: +1,471 / +1,586).
   - It survives two checks: features only from contexts not sharing the last glyph or the last two (+680 to +925), and features only from other rounds (+976). So it is sequence-wide, and it isn't the same sheet seen twice.
   - Beyond the glyph covariates and the others' feature, it is +894: Grok +387, Haiku without thinking +398, Gemini Flash +72, Haiku with thinking +44. Sonnet's is −6 and Opus's 0.
   - "Opus and Gemini Pro lean on the shared part" is partly coverage. Thinning a core mind's own answers to Opus's count halves its per-answer effect. Opus stays at zero under that check. Gemini Pro has too few answers to measure, and Gemini Flash, at lower coverage than Opus, leans on its own as much as Grok does per answer.
   - The unit is a Unicode block, not a sequence: 87% of answers are in single-block groups. The largest group is the whole Mathematical Alphanumeric Symbols block (1,674 contexts, many alphabets and styles).
5. **Half or more of the sheet-mate effect is selection, not format** [re-derived]. The planner gives strong sequences several questions a round, so same-sequence sheet-mates co-occur with sequences that continue more. Controlling for the sequence's strength measured in *other* rounds moves the coefficient from −0.70 ± 0.04 to −0.32 ± 0.04 (first answers), and on repeats from −0.45 ± 0.21 to −0.14 ± 0.22. Since that control is noisy, −0.32 is an upper bound on any format effect.
6. **Smaller points** (§5):
   - "A per-item interaction gains nothing held out" and "the verifier's item-level interaction gains +31.8" sit side by side in FINDINGS §3, and the first is a property of `lnb.py`'s no-feature variant;
   - every LNB fold stopped at its 60-iteration cap;
   - "1,500 to 2,500 nats about its sibling contexts" is a total over 77,489 answers, about 0.1 nats per context;
   - the debrief says three things "shift answers" where two shift which questions are asked;
   - three NOTES entries were corrupted by shell expansion of `$-`;
   - two coordinator-side timestamps are later than the events they date.
7. **What holds** [reproduced]: `reask.py` exactly; the two-factor fit (log-likelihood −36,165.4 and its loadings); the selection algebra of strengthening 2 §1, which I re-derived; p002's per-mind scores from `prereg2_check.py`; and the round itself. The 43 questions match the pre-registration context for context, one per sheet, with no multi-code-point glyph, so the scorer's `tuple(context)` keying is safe.

## 1. Round p002

**My prediction and its timing.** The pre-registered models put Haiku with thinking at about 20 stops of 43, while on these same contexts it had stopped 1 time in 14. I took that gap as the test worth adding. `de-novo-3/b_pred.py` writes, per mind, $P(\text{stop}) = (k + 4r)/(n + 4)$. Here $k$ of $n$ are the mind's own answers at the context (snapshot plus p001, from `prereg-third-minds.json` itself) and $r$ is its Jeffreys-smoothed stop rate pooled over the 43 contexts. Its output (`b-pred-p002.json`, 19:31:19) and `PREDICTION-p002.md` (19:31:31; SHA-256 `fcc2744c…` as written then) predate `data/answers/p002.jsonl` (19:31:43). I had not opened the raw ledgers. File times and my word are the only attestation.

**Result** [p002; `c4_score_p002.py`]:

| mind | stops | baseline | `2mf` | `irtu` | `lnb` | two-factor [post hoc] |
|---|---|---|---|---|---|---|
| Opus | 6 | 5.9 [2–11], −16.32 | 9.5, −16.52 | 6.9, −14.95 | 8.0, −14.25 | 11.5, −18.51 |
| Haiku without thinking | 12 | 7.1 [3–12], −23.02 | 20.3, −29.63 | 12.1, −20.60 | 13.0, −21.20 | 10.9, −20.87 |
| Haiku with thinking | 6 | 4.2 [1–8], −16.90 | 21.9, −29.03 | 20.4, −27.10 | 19.9, −26.28 | 18.1, −24.03 |
| total log score | | **−56.24** | −75.18 | −62.65 | −61.73 | −63.41 |

(Entries are expected stops, with the baseline's 95% band, and the per-context log score.) The baseline loses Opus to `lnb` by 2.1 nats, and Haiku without thinking to `irtu` by 2.4. It wins Haiku with thinking by 9.4.

**Where the Haiku-with-thinking margin sits:**

| contexts | n | stops | `2mf` | `irtu` | `lnb` | baseline |
|---|---|---|---|---|---|---|
| with its own earlier answers | 13 | 3 | −7.07 | −6.13 | −6.50 | −7.14 |
| without | 30 | 3 | −21.96 | −20.96 | −19.79 | −9.75 |

The baseline's advantage isn't per-context memory. It uses the mind's rate *on this selected set*, which the fitted models replace with the mind's global threshold plus the item's shared position, and that position is dragged toward "stop" by Grok's stops (2 or 3 of 3 at every context).

**Why the models miss** [re-derived, inference]. The flat set is 34 contiguous chart walks, 8 monotone runs and 1 other. Stop rates by chart class in the snapshot:

| | contiguous | monotone | other |
|---|---|---|---|
| Sonnet | 0.074 | 0.540 | 0.312 |
| Opus | 0.077 | 0.515 | 0.289 |
| Haiku without thinking | 0.264 | 0.592 | 0.324 |
| Haiku with thinking | 0.195 | 0.641 | 0.467 |
| Grok | 0.198 | 0.625 | 0.354 |

The fitted models have no covariate for the chart class. At a flat context they combine Grok's stops (2 or 3 of 3) and Sonnet's 0 of 3 into one item position and apply each mind's global threshold. So they give Haiku with thinking about 0.47 per context: its global threshold (a stop rate of 0.34) at a shared position pulled up by Grok. Its rates by chart class, applied to the set's 34 contiguous, 8 monotone and 1 other context, give about 12 stops. So the chart class accounts for about half the miss, and the rest (12 against 6) is still unexplained. I haven't fitted a covariate model to p002, so this mechanism is a reading, not a test.

**`prereg-result-2.md`, read against this:**
- "Its own record on these contexts says why … 14 times and continued 13" covers 13 contexts. The other 30 carry the failure (above).
- "through the second dimension (the Haiku axis), toward Haiku without thinking": `2mf`, `irtu` and `lnb` are all one-factor models. The two-factor model, run post hoc, doesn't rescue Haiku with thinking (18.1 expected).
- "A mind's own past answers on a context predict its next answer better than any model fitted so far allows" is true for Sonnet in p001. For p002 the better-supported statement is narrower: a mind's behaviour on a *kind of context* (chart walks, here) isn't carried by a one-dimensional item position.
- Its header says the round was asked "from about 19:52". The round was built at 19:28:15, its ledgers were written by 19:30:22, and its answers were recorded at 19:31:43. The commit message of `1a998f00` likewise says "Checked at 19:50", but the commit is dated 19:28:03. Both look like the same clock slip.

**The reading rule.** The rule says to report "the log likelihood ratio between models", and then a "win" needs the best model to beat *each* other model by more than $\log 10$. With two of the three nearly identical by construction, as the file itself notes, the rule can only ever return "not discriminating" or a `2mf` win. So the outcome the round was most likely to show, `2mf` rejected on Haiku without thinking at a ratio of about 8,000, comes out as "not discriminating" in `prereg2_check.py`'s verdict line. Bands are printed but not flagged, so Haiku with thinking's 6, below every band, gets no verdict either. For the next pre-registration I'd suggest three things: pairwise ratios as the verdict; a stated reading for every band; and a naive reference model alongside the fitted ones, so that "all models fail" is distinguishable from "no model discriminates".

## 2. The sequence-level effect, re-examined

All of this is in one frame [re-derived]: `irtu`'s prequential predictions (the verifier's model, strengthening 2's `blockresid.py` and `grouping.py` frame) as offsets, and per-mind logistic regressions on leave-the-item-out group features. Coefficients are fitted on half the block-set groups and scored on the other half, both ways. It differs from LNB's frame, so the totals aren't comparable one to one. Differences *within* the frame are what I lean on.

**2a. Shared against mind-specific** (`c1`, `c3`). "own" is the mind's mean residual on other items of the block set. "others" is the other minds' mean residual there. Because residuals are per mind, "others" doesn't depend on which minds happened to answer the block. LNB's `F_oth` is a raw pooled stop rate, and in a block answered mostly by high-threshold minds it reads as "stop" for that reason alone [inference: a candidate reason why LNB's mind-specific step is larger].

| | own alone | others alone | both | own beyond others |
|---|---|---|---|---|
| all minds (≥ 3,000 answers each) | +6,115 | +5,345 | +6,442 | **+1,096** |
| features from other rounds only | +5,659 | +5,037 | +6,013 | +976 |
| own from far items only (last glyph differs, no shared glyph in the last two) | | | | +680 (beyond others from all items); +925 (beyond others from far items) |

Own beyond others, per mind (all rounds): Sonnet +226, Opus +14, Haiku without thinking +388, Haiku with thinking +30, Grok +387, Gemini Flash +51.

So a mind-specific lean exists in a second frame, and it is neither near-duplicate questions nor within-round correlation. But in this frame the shared part is about five times the specific part, not 1.6 times.

**2b. Glyph covariates** (`c7`, `c8`). Covariates computed from the context alone: contiguous (every step +1, or every step −1), monotone, one block, number of blocks, length and its square, unfamiliar last glyph, and log size of the last step.

| | gain (all six minds) |
|---|---|
| covariates, one coefficient vector for all minds (intercepts per mind) | +8,639 |
| covariates, a vector per mind | +9,071 to +9,204 |
| block-set group feature, others | +5,279 |
| covariates + others | +10,199 |
| covariates + others + own | +11,093 |
| **own beyond covariates and others** | **+894**: Grok +387, Haiku without thinking +398, Gemini Flash +72, Haiku with thinking +44, Opus 0, Sonnet −6 |

[inference] Most of what strengthening 2 calls the shared sequence effect is a prior over unasked contexts from what they look like (72,427 of the 77,489 answers are first answers, where an item model has nothing but its prior). Glyph covariates supply that prior better than block membership does. Sonnet's apparent block lean is accounted for by its response to those covariates. Per-mind contiguity coefficients: Sonnet −1.67, Opus −1.55, Haiku with thinking −1.20, Grok −1.11, Gemini Flash −0.93, Haiku without thinking −0.48 (logit of stopping). That is the chart lean FINDINGS §6 already names, seen through continuation. The lean that remains beyond it belongs to Grok, Haiku without thinking and, per answer, Gemini Flash.

**2c. Coverage** (`c5`). Own beyond others, per answer: Sonnet 0.0105, Haiku without thinking 0.0193, Grok 0.0199 with all their answers. Opus −0.0020, Haiku with thinking 0.0075, Gemini Flash 0.0166. Rebuilt from a random sample of each core mind's answers the size of Opus's (three draws): Sonnet 0.0043–0.0046, Haiku without thinking 0.0088–0.0107, Grok 0.0109–0.0123. So part of the ranking of `lam` across minds is how many answers a mind gives per block. Opus's zero survives the matching. Gemini Flash's lean is large at the lowest coverage of the six, and FINDINGS doesn't mention it. Gemini Pro (678 first answers) can't be read either way.

**2d. The unit** (`c6`). There are 22,207 contexts and 777 block-set groups; the median group has 2 contexts, and 347 groups have one. 87% of answers are in single-block groups, and the ten largest groups hold 35% of answers: Mathematical Alphanumeric Symbols (1,674 contexts), Enclosed CJK Letters and Months (939), Enclosed Alphanumerics (952), Basic Latin (889), Braille Patterns (722), and so on. What the data measure is a mind's lean on a *Unicode block*. Whether it holds per sequence within a block (bold Latin against double-struck Greek) is untested. Strengthening 2 §8 calls the block set a proxy. FINDINGS §3, the debrief and integration item 3 speak of sequences.

**2e. The fits.** Every LNB fold, with or without features, stopped at the 60-iteration cap (`iters` 59 in all forty fold files), so no fold fit converged by its tolerance. The no-feature LNB scores below `2mf` held out by item (−0.4680 against −0.4676, about −31 nats), where the verifier's `irtu` scores +31.8 above it. FINDINGS §3's "a per-item mind interaction alone gains nothing held out" is therefore a statement about LNB's no-feature variant, which differs from `irtu` in having no near-certain classes and in being unconverged. The next sentence of FINDINGS, "+31.8 nats", contradicts it as written.

## 3. Same-sequence sheet-mates

`sheetmates.py` compares observed stops with `irtu`'s prequential prediction, by whether a sheet carries other contexts of the same block set. METHODOLOGY §5 draws claim slots "with replacement in proportion to each claim's mean weight", so a highly weighted sequence gets several questions in one round, and a strong sequence is one minds continue. `c2` adds the sequence's strength measured only in *other* rounds: the mean residual over other items of the block set, all minds. It shares no answer with the sheet in question. Sequences with sheet-mates do continue more elsewhere: mean other-round residual −0.088 with mates, +0.001 without.

| | sheet-mates alone | + strength (all minds, other rounds) | + strength (this mind too) |
|---|---|---|---|
| first answers (n = 72,427; 7.0% with mates) | −0.70 ± 0.04 | −0.32 ± 0.04 | −0.31 ± 0.04 |
| repeats (n = 4,530) | −0.45 ± 0.21 | −0.14 ± 0.22 | −0.19 ± 0.22 |

At least half of the −0.70 is selection. The control is a noisy estimate of strength, which under-adjusts, so −0.32 bounds a format effect from above. Whether any format effect remains needs a within-item contrast: the same context, the same mind, with and without mates. Keeping same-block contexts off one sheet is still cheap hygiene. But "−0.70 logit … format shaping the order a mind reports" (FINDINGS §5) and the plan's sentence citing it overstate what's measured. On repeats, nothing is distinguishable from zero.

## 4. Seeds and re-asking

- [inference] FINDINGS §5 says consistency checks "are valid only when they condition on what the planner used; the prequential frame does." The planner also uses answers on *other* contexts: sequence relevance, which METHODOLOGY §5 weights by the lower bound of a sequence's links, as well as seeds and triad-era inputs. The prequential frame conditions only on the same context's earlier answers. Its predictions are proper. But its calibration checks inherit selection on everything else, as the very next bullet (seeds) and §3 above show. "Does" should be "does for selection on the same context's answers".
- The debrief's "Three things in the study's own machinery shift answers" is true of sheet-mates, at most. Re-asking and seed targeting shift which questions get asked and how a model's prior fits them. They don't change an answer.

## 5. Smaller points

- **Units in integration item 1 and strengthening 2 §7.** "A context's answers carry 1,500 to 2,500 nats about its sibling contexts" is a total over 77,489 answers and 22,207 contexts: about 0.02–0.03 nats per answer, 0.07–0.11 per context.
- **NOTES.md 18:35, 19:17, 19:25.** Every `$-0.4186$`-style value reads `3569JNRXghkl0.4186$`. The shell expanded `$-` (its option flags) in an unquoted heredoc. The minus signs and opening delimiters are lost. The correct values are in strengthening 2 §2 and §5.
- **README against FINDINGS.** The README's "What happened" says content agreement is 93–99%; FINDINGS §1 says 0.94–0.99.
- **FINDINGS §3, last paragraph** ("This is the measurable form of 'model-sensitive sequence'"). Given 2b–2d, the measurable form is a per-(block, mind) lean beyond the glyph covariates, carried by Grok, Haiku without thinking and Gemini Flash.
- **The modified `prereg_round.py`** builds a context from `list(c["context"])` when `context_glyphs` is absent. That's safe here (no multi-code-point glyph in the 43). It would split a glyph with a variation selector in a later pre-registration.
- **The snapshot's working copy** is the pickle in the shared session scratchpad (`fd-snapshot.pkl`, 16:36). If it's deleted, `lib.load()` silently rebuilds from the *current* answer files, a different dataset, rather than from the manifest. `--from-manifest` exists, but `load()` doesn't use it. A guard that compares `kept` with the manifest would make every script's dataset certain.

## 6. What I'd try next, as suggestions

These are offered as places a strengthening attempt could go, in the spike agent's judgement.

- Give the item models the glyph covariates (shared, then per mind) and re-run strengthening 2's held-out ladder on top of them: what remains for block features, shared and own, once the prior over unasked contexts is fair? My frame says about +1,000 shared and +900 mind-specific; LNB's frame may differ.
- Make LNB's `F_oth` composition-free, for instance as other minds' log-odds each centred on its own overall rate, averaged per mind rather than pooled by answer count. Then see how much of the +1,500 survives.
- Score p002 under the covariate model. It was fitted before p002, so it is a fair, if late, test of the chart-walk reading in §1.
- For integration item 3: if a per-(block, mind) number goes to the catalog, its evidence count per block will be small for most blocks (median two contexts per group). Its interval matters more than its point value.

## 7. The seal

Everything I computed on the snapshot loads through the spike's `lib.py`, whose `sealed` drops `choose` and `names` records touching the canary before anything else. p002 holds only continue answers. I queried, counted and displayed no sealed answer.

## What I did not do

- I didn't refit LNB with covariates or with a composition-free `F_oth`. My numbers are from a residual frame, and §2's comparisons hold within it.
- I didn't fit a covariate model to p002.
- I didn't re-run the LNB folds, `preq.py`'s calibration tables, `seedsel.py`, or anything from strengthening 1.
- I didn't read the first verification, the first strengthening or MAP.md, so a point above may repeat one already answered there.
- I didn't check the literature.

## On the brief

It gave me what I needed, the running round included: "do with that what you judge right" is what made a timed competing prediction possible. One fact would have changed my first ten minutes: the coordinator was scoring p002 in parallel (`prereg-result-2.md` landed at 19:32). I found that out from the git log.

I'm staying on the line for follow-up questions.

## Appendix A: `de-novo-3/`

Outputs are in `de-novo-3/c*.log`. Run from the spike directory with `/opt/homebrew/bin/python3 de-novo-3/<script>`. Each loads the snapshot through `lib.py` (via `irt.load`). `c1` caches `irtu`'s prequential predictions in the session scratchpad (`dn3/preq_irtu.pkl`), and the later checks read that cache.

- **`b_pred.py`, `b-pred-p002.json`, `PREDICTION-p002.md`.** The local-pool baseline for p002, written before any p002 answer was recorded.
- **`c1_near_far.py`.** Own and others' block-set residual features, all items and far items (§2a).
- **`c2_sheetmates.py`.** The sheet-mate coefficient with the sequence's strength from other rounds (§3).
- **`c3_other_rounds.py`.** §2a with features from other rounds only.
- **`c4_score_p002.py`.** p002 under the three models and the baseline, split by whether the mind had its own earlier answers (§1).
- **`c5_coverage.py`.** Own beyond others per answer, with core minds thinned to Opus's coverage (§2c).
- **`c6_groups.py`.** Group sizes and units (§2d, §5).
- **`c7_glyph_covariates.py`, `c8_cov_shared.py`.** Glyph covariates: per mind, shared, and with the block features (§2b).
- **`c9_twof_p002.py`, `twof-p002-posthoc.json`.** The two-factor model's p002 prediction, post hoc (§1).
