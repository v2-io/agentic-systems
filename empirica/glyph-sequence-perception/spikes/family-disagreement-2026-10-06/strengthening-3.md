# Strengthening 3: answering the third verification

*2026-10-06, 19:47–21:00 MDT by the clock (`date`), the spike agent (Claude Opus 5.5), answering `de-novo-feedback-3.md`. Same snapshot (`snapshot/manifest.json`); rounds p001 and p002 where stated. Before starting I knew p002's per-mind results from the coordinator's message and the verifier's report, including the chart-class reading. Everything p002-related below is therefore a **late test**, not a pre-registered one: the covariates were added because p002 pointed at them. Labels: **[measured]**, **[inference]**, **[open]**.*

## Summary

1. **The verifier's central point holds inside my own model** [measured]. Give the item models glyph covariates computed from the context alone, and most of what strengthening 2 called a "shared sequence effect" turns out to be a prior over unseen contexts from what they look like. Held out (sums over five folds, by item / by block):
   - covariates: **+5,364 / +5,389** nats over no covariates; +4,686 / +4,744 of it with one coefficient vector shared by all minds;
   - others' sequence rate beyond the covariates: +577 / +653;
   - **the mind's own sequence rate beyond both: +884 / +978**, positive in all ten folds.

   That matches the verifier's +894 from a different frame. The mind-specific per-block lean is real, about 0.6 of what strengthening 2 reported for it (+1,471 / +1,586) once the context's own look is accounted for; the shared part shrinks far more. For scale, it is about 0.01 nats per answer.
2. **The sheet-mate effect isn't demonstrated** [measured]. Within the same context and the same mind, answered both with and without same-sequence sheet-mates (554 pairs), the stop share differs by +0.008 (95% −0.012 to +0.027). With the verifier's finding that at least half of the −0.70 logit was selection, no format effect is shown. Most of the paired contexts are near-certain, so the test has little power against a modest logit effect.
3. **The best model now** (on the wide grid of §4a) fits rows (one per context and round) with each row's sequence features computed from earlier rounds only, so it is fitted with the features it predicts with. It adds glyph covariates per mind, the composition-free others' rate, the own rate, a sparse per-(context, mind) interaction and a weak ridge prior. Its prequential log score (each context's posterior and features from earlier rounds; the global parameters fitted on all answers, so slightly optimistic, as for every model compared) is **−0.4332 per answer**, against −0.4485 for covariates alone, −0.5211 for strengthening 2's block-set model and −0.5731 for `2mf`. **It is still not calibrated on every check** (10 of 38 outside their bands on the wide grid, 16 on the narrow one); §4 and §4a say which.
4. **p002, late** [measured]:
   - this model scores −53.84 on the wide grid (−56.60 on the narrow one); the covariate-only model −59.57;
   - the verifier's naive baseline scores −56.24, and the pre-registered models −61.73 (block-set), −62.65 (`irtu`) and −75.18 (`2mf`).

   So glyph covariates and the wide grid take the fitted models from well behind the baseline to ahead of it. Haiku with thinking is still over-predicted: 13.7 stops expected against 6.

   **p001, late:** −33.98 on the wide grid, against `irtu`'s −31.80. Sonnet's steadiness on the flat contexts is still slightly under-predicted (4.8 stops expected against 1).
5. **Chart walks, per mind** [measured]. Contiguity coefficients (logit of stopping, best model on the wide grid; the narrow grid's are within 0.4 and in the same order): Opus −2.67, Sonnet −2.20, Haiku with thinking −1.46, Haiku without thinking −0.56, Grok −0.49, Gemini Flash −0.00, Gemini Pro −1.43 (thin). The larger Claude minds keep walking the chart far more than Grok or Gemini Flash. This is the chart lean FINDINGS §6 names, seen in continuation.
6. **Corrections made** [measured]:
   - the three NOTES entries corrupted by shell expansion are restored (10 values; a dated note says how);
   - `lib.load()` now checks the snapshot pickle against the manifest, and rebuilds from the manifest, never silently from current files;
   - FINDINGS' contradiction and the overstatements the verifier lists are corrected in the replacement text sent with this report.

## 1. The held-out ladder

`ladder.py` adds `covs.py`'s glyph covariates (contiguous, monotone, one block, number of blocks, length and its square, log size of the last step) and the composition-free others' feature to `spx.py`'s sparse-interaction model. Each variant goes through both fold schemes of strengthening 2, with at most 300 EM iterations. Log score per answer, with the sum over folds:

| variant | by item | by block |
|---|---|---|
| base (no covariates, no sequence features) | −0.4677 (−36,242) | −0.4729 (−36,647) |
| covariates, one vector for all minds | −0.4072 (−31,556) | −0.4117 (−31,902) |
| covariates, a vector per mind | −0.3985 (−30,878) | −0.4034 (−31,257) |
| + others' sequence rate (composition-free) | −0.3910 (−30,302) | −0.3949 (−30,604) |
| **+ own sequence rate** | **−0.3796 (−29,418)** | **−0.3823 (−29,626)** |
| same, others' rate pooled as in strengthening 2 | −0.3793 (−29,392) | −0.3819 (−29,594) |
| no covariates; others' (composition-free) + own | −0.4200 (−32,545) | −0.4217 (−32,677) |

Steps in nats (by item / by block): covariates +5,364 / +5,389, of which per-mind vectors +678 / +645; others' rate beyond covariates +577 / +653; **own rate beyond covariates and others' +884 / +978**. Per fold, the own step is +157, +164, +184, +155, +223 by item and +115, +274, +271, +219, +99 by block. Once covariates are in, composition-free against pooled others' makes no material difference (25–32 nats, in the pooled version's favour).

**Convergence.** The full model's folds converged by tolerance at 160–220 iterations. Several of the simpler variants stopped at the 300 cap, as the verifier found for strengthening 2's folds. The step sizes are consistent fold by fold, so the cap doesn't change the ordering. That is an inference from the fold table, not a convergence proof.

**What the own rate is, read off the best model's coefficients** (row-level fit; `lam` own rate, `kap` others'): Sonnet 0.51 / 0.44, Opus 0.77 / 1.12, Haiku without thinking 0.80 / −0.06, Haiku with thinking 0.60 / 0.57, Grok 1.47 / −0.03, Gemini Flash 1.00 / 0.07, Gemini Pro 0.01 / 1.95 (thin). Grok, Gemini Flash and Haiku without thinking lean on their own record across a block and almost not at all on the others'. That agrees with the verifier's per-mind split (Grok +387, Haiku without thinking +398, Gemini Flash +72 in total, which is large per answer at its low coverage; Sonnet and Opus near zero). The unit is a Unicode block, or set of blocks; whether the lean holds per sequence within a block is untested (verifier 3 §2d).

## 2. Sheet-mates, within items

`sheetmates2.py`: for each (context, mind) answered at least once on a sheet *with* another context of the same block set and at least once *without*, the stop share with mates minus without. Sequence strength is fixed by construction.

| | pairs | mean difference | 95% (bootstrap) | + / − / 0 |
|---|---|---|---|---|
| Sonnet | 169 | +0.000 | −0.018 to +0.018 | 1 / 1 / 167 |
| Grok | 237 | −0.003 | −0.028 to +0.022 | 12 / 10 / 215 |
| Haiku without thinking | 132 | +0.038 | −0.030 to +0.106 | 13 / 8 / 111 |
| all minds | 554 | +0.008 | −0.012 to +0.027 | 26 / 19 / 509 |

[inference] No sheet-mate effect is detectable within items. With verifier 3 §3 (−0.70 shrinking to −0.32 once sequence strength is controlled), what strengthening 2 called a format effect is mostly selection. A small format effect isn't ruled out: 509 of the 554 pairs are near-certain contexts, where even a real logit effect hardly moves the share.

## 3. The model fitted with the features it is used with

Strengthening 2's feature models were fitted with sequence features from all rounds and scored with features from earlier rounds only. That mismatch made the fits over-rely on the features (seen in strengthening 2's own same-round pair checks, over-predicted almost everywhere). `spxr.py` fits on rows (one per context and round), with each row's features from earlier rounds only (`lnb_prefix.py`, composition-free), the per-context shared position and sparse interaction, and a ridge prior $N(0, 3^2)$ on every per-mind coefficient. The ridge keeps Gemini Pro finite: without it, its slope reached 17.6 and its predictions became NaN under separation.

| | prequential log score per answer (item posterior and features from earlier rounds; global parameters in-sample) | checks outside band (of 38) | p001 | p002 |
|---|---|---|---|---|
| `2mf` (strengthening 2) | −0.5731 | 11 (of fewer checks) | −37.08 | −75.18 |
| `irtu` | −0.5727 | 6 | **−31.80** | −62.65 |
| block-set model (strengthening 2) | −0.5211 | 21 | −34.65 | −61.73 |
| covariates only, row-fitted | −0.4485 | 17 | −35.49 | −59.57 |
| covariates + others + own, row-fitted | −0.4332 | 16 | −34.97 | −56.60 |
| **the same on the wide grid (§4a)** | **−0.4332** | **10** | −33.98 | **−53.84** |
| naive baseline (verifier 3) | — | — | — | **−56.24** |

(The `2mf` / `irtu` check counts are from strengthening 2's report, which had no same-round pair checks for them in that table; their pair checks in `strengthening-2-logs/preq2.log` add 4–5 more outside.)

## 4. What still fails, and the wide-grid test

The best model's remaining misfits (prequential checks, 16 of 38):

- **Sonnet is more self-consistent than modelled**: flips 40 against 64.9 predicted; flat-type flips 33 against 47.3; repeat stops 34 against 55.4.
- **Sonnet agrees with every partner more than modelled** in same-round pairs: Opus 425 against 502, Grok 3,027 against 3,214, Haiku without thinking 5,247 against 5,446.
- Haiku without thinking's flips are over-predicted (222 against 276).
- Grok–Gemini Flash agree more than modelled (465 against 568).
- Haiku without thinking–Grok agree less (4,798 against 4,677).

Every Sonnet misfit points the same way: Sonnet is more deterministic than the model allows. Sonnet is the anchor (slope 1), and the shared position is integrated on a grid over $[-5, 5]$, so Sonnet's logit can't pass ±5 while minds with slope 2.4 reach ±12. The grid could therefore cap Sonnet's certainty. Test: the same model on a grid over $[-10, 10]$ (81 points).

### 4a. The wide grid (`SPX_GRID=wide run_spxr.py cov_oth_own`)

The grid was the obstacle for Sonnet. On $[-10, 10]$ the prequential log score is unchanged (−0.4332 per answer), but calibration changes where it should:

- **Every same-round pair involving Sonnet falls inside its band:** Opus 425 / 436.8, Grok 3,027 / 3,009.6, Haiku without thinking 5,247 / 5,294.9, Gemini Flash 487 / 484.5.
- **Sonnet's repeats:** stops 34 / 46.0 [34–58] and flat-type flips 33 / 40.7 [31–51] fall inside their bands; overall flips 40 / 52.5 [41–65] are just outside.
- **Checks outside band: 10 of 38** (16 on the narrow grid).
- **Late test rounds:** p001 −33.98 (Sonnet −7.51, Grok −26.46); **p002 −53.84, ahead of the naive baseline's −56.24**. By mind: Opus −14.66, Haiku without thinking −20.40, Haiku with thinking −18.78. Haiku with thinking is still over-predicted, 13.7 stops expected against 6; the baseline still wins that mind (−16.90).

[inference] Part of "Sonnet is steadier than any model allows" (strengthening 2 §4, `prereg-result-1.md`) was my anchoring: with Sonnet as the scale (slope 1) and the shared position on $[-5, 5]$, the model couldn't make Sonnet as certain as it is. The held-out ladder (§1) used the narrow grid and wasn't re-run on the wide one.

**What remains (10 checks)**, as a pattern:

- **Grok agrees with both Gemini minds more than modelled** (Gemini Flash 465 / 576.4, Gemini Pro 97 / 116.9), and Haiku with thinking with Gemini Flash (194 / 237.1).
- **Haiku without thinking is more self-consistent than modelled** (flips 222 / 273.6; flat-type 142 / 175.3), agrees less with Grok (4,798 / 4,674.1), and differs less from Haiku with thinking than modelled (1,039 / 1,108.7).
- Haiku with thinking's first-answer stops (1,629 / 1,683.6) and Grok's repeat stops (322 / 349.3) are slightly off.

The Grok–Gemini affinity is the one pairwise structure no model here has absorbed. It is a candidate for a second shared dimension fitted together with the covariates, which wasn't attempted.

## 5. Corrections and replies to the verifier's smaller points

- **NOTES corruption** (verifier 3 §5): restored by replacing the expansion `3569JNRXghkl` with `$-` in 10 places; a dated correction entry says how. Later entries avoid shell expansion.
- **`lib.load()`** (verifier 3 §5): it checks the pickle's record count against the manifest, and if the pickle is missing it rebuilds from the manifest's answer IDs, not from the current files. `--refresh` remains the deliberate rebuild.
- **FINDINGS §3's contradiction** (verifier 3 §2e): "a per-item mind interaction alone gains nothing held out" was true of `lnb.py`'s unconverged no-feature variant, not of `irtu` (+31.8). The replacement text says which model each figure belongs to.
- **Units** (verifier 3 §5): the sequence-feature gains are totals over 77,489 answers; per answer they are about 0.01 nats. The replacement text says so.
- **"Shift answers"** (verifier 3 §4): of the three things the debrief named, only the sheet is a candidate for shifting an answer, and §2 finds no within-item effect. Re-asking and seed targeting shift which questions are asked. The replacement debrief says so.
- **The prequential frame** (verifier 3 §4): it conditions on the same context's earlier answers. Selection on other contexts' answers (sequence relevance), seeds and triad-era inputs isn't conditioned on, and calibration checks inherit it. Agreed; the replacement FINDINGS narrows the claim.
- **The p002 reading rule** (verifier 3 §1): agreed. Pairwise ratios, a stated reading for every band, and a naive reference model belong in any next pre-registration.
- **`prereg_round.py`'s `list(c["context"])` fallback** (verifier 3 §5): it is the coordinator's script. Contexts should be carried as glyph lists (`context_glyphs`) wherever a variation selector could occur.

## 6. What this changes [inference]

- **The per-sequence quantity** (integration item 3). Its measurable form is a per-(Unicode block, mind) lean beyond the context's look and beyond the other minds' rate on that block, worth about +900 nats held out in total. It is carried mostly by Grok, Haiku without thinking and Gemini Flash. Sonnet's and Opus's differences from the others are mostly how readily they walk the chart, which is a per-mind response to a glyph covariate, not a block lean. With a median of two contexts per group, a catalog number would need its interval more than its point value.
- **Planner.** The strongest single lever on how settled a context is turns out to be what the context looks like (chart class, length, blocks), shared across minds. A per-mind response to those features, chiefly contiguity, is where the families differ most clearly.
- **Calibration** remains the unmet bar, now narrower: on the wide grid, Sonnet's determinism and its pairwise agreement are held. What is left is a Grok–Gemini affinity and Haiku without thinking's own consistency.

## Files added

`covs.py`, `ladder.py`, `cov_score.py`, `spxr.py`, `run_spxr.py`, `sheetmates2.py`; `spx.py` gained covariates, `own` and `sparse` switches, `RowAdapterC` and an optional wide grid (`SPX_GRID=wide`); `lnb.py` and `lnb_prefix.py` gained a composition-free others' feature; `lib.py` the manifest guard. Logs and per-fold results are in `strengthening-3-logs/`.
