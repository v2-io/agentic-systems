# R2 Voting Cohort — Progress

**Generated:** 2026-04-30T17:20:53Z
**Voters discovered:** 4 (`codex-r2`, `gemini-r2`, `opus-r2`, `sonnet-r2`)
**Targets per card:** 629
**Substantive-notes threshold:** ≥ 30 chars (tunable via `--notes-threshold=N`)

## At a glance

| voter | tgt voted | votes | top-picks | substantive | can-vote | gap | drift | seq max | off-scale |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| `codex-r2` | 629 | 794 | 629 | 12 (2%) | 629 | – | – | – | – |
| `gemini-r2` | 65 | 68 | 66 | 64 (94%) | 110 | 36 | +9 | 112 | – |
| `opus-r2` | 76 | 235 | 76 | 233 (99%) | 76 | – | – | – | 62 |
| `sonnet-r2` | 94 | 208 | 93 | 208 (100%) | 94 | – | – | – | 58 |

*Columns:* `tgt voted` = unique targets with at least one voted candidate-row in the card (the ground truth); `votes` = total candidate-row votes (multiple per target possible); `top-picks` = rows marked as top-pick; `substantive` = rows whose notes column meets the threshold; `can-vote` and `gap` come from the tracker (gap = can-vote rows that haven't cast yet); `drift` = tracker's `voted=true` count minus card's `tgt voted` (positive = stale `voted=true` markers in tracker; negative = card has cast votes the tracker hasn't synced to yet — re-run `bin/naming-master-tracker` to resync); `seq max` = highest voting-sequence integer; `off-scale` = votes using R1's wider scale (+3 / -2 / -3) instead of R2's spec (+2 / +1 / -1).

## Cohort coverage

- **Targets with ≥1 voter:** 629 / 629 (100%)
- **Targets with ≥2 voters:** 189 / 629
- **Targets with ≥3 voters:** 42 / 629
- **Targets with ≥4 voters:** 4 / 629
- **Total candidate-row votes:** 1305
- **Substantive votes (cohort-wide):** 517 (40%)
- **Off-scale residual:** 120 (R2 spec is +2/+1/-1; off-scale votes can be clamped at aggregation time but signal the R1-scale prior leaking through)

## Off-scale breakdown

- `codex-r2`: clean (no off-scale votes)
- `gemini-r2`: clean (no off-scale votes)
- `opus-r2`: 47 `+3`, 13 `-2`, 2 `-3`
- `sonnet-r2`: 58 `+3`

*Note:* the R2 card preamble specifies +2/+1/-1 only. R1 used a wider scale (+3/+2/+1/-1/-2/-3); voters trained on R1's scale will sometimes default back to it. The methodology document's §5 names this as a known failure mode.

## Vote-category distribution

| voter | rename | keep | canonicalize | add-alias | name-unnamed |
|---|--:|--:|--:|--:|--:|
| `codex-r2` | 208 | 272 | 44 | 71 | 199 |
| `gemini-r2` | 5 | 46 | 7 | 5 | 5 |
| `opus-r2` | 110 | 67 | 15 | 15 | 28 |
| `sonnet-r2` | 75 | 44 | 19 | 14 | 56 |

## Quality signal — substantive-note distribution

| voter | total votes | substantive | empty-or-thin | sub-rate |
|---|--:|--:|--:|--:|
| `codex-r2` | 794 | 12 | 782 | 2% |
| `gemini-r2` | 68 | 64 | 4 | 94% |
| `opus-r2` | 235 | 233 | 2 | 99% |
| `sonnet-r2` | 208 | 208 | 0 | 100% |

*Substantive-note rate is the headline depth-of-engagement signal — a +2 with substantive notes carries different aggregation weight than a +2 with no notes, regardless of identical face-value weight.*

