# R2 Voting Cohort — Progress

**Generated:** 2026-04-30T17:30:36Z
**Voters discovered:** 4 (`codex-r2b`, `gemini-r2`, `opus-r2b`, `sonnet-r2b`)
**Targets per card:** 629
**Substantive-notes threshold:** ≥ 30 chars (tunable via `--notes-threshold=N`)

## At a glance

| voter | tgt voted | votes | top-picks | substantive | can-vote | gap | drift | seq max | off-scale |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| `codex-r2b` | 0 | 0 | 0 | – | – | – | – | – | – |
| `gemini-r2` | 66 | 69 | 67 | 65 (94%) | 110 | 36 | +8 | 112 | – |
| `opus-r2b` | 0 | 0 | 0 | – | – | – | – | – | – |
| `sonnet-r2b` | 0 | 0 | 0 | – | – | – | – | – | – |

*Columns:* `tgt voted` = unique targets with at least one voted candidate-row in the card (the ground truth); `votes` = total candidate-row votes (multiple per target possible); `top-picks` = rows marked as top-pick; `substantive` = rows whose notes column meets the threshold; `can-vote` and `gap` come from the tracker (gap = can-vote rows that haven't cast yet); `drift` = tracker's `voted=true` count minus card's `tgt voted` (positive = stale `voted=true` markers in tracker; negative = card has cast votes the tracker hasn't synced to yet — re-run `bin/naming-master-tracker` to resync); `seq max` = highest voting-sequence integer; `off-scale` = votes using R1's wider scale (+3 / -2 / -3) instead of R2's spec (+2 / +1 / -1).

## Cohort coverage

- **Targets with ≥1 voter:** 66 / 629 (10%)
- **Targets with ≥2 voters:** 0 / 629
- **Targets with ≥3 voters:** 0 / 629
- **Targets with ≥4 voters:** 0 / 629
- **Total candidate-row votes:** 69
- **Substantive votes (cohort-wide):** 65 (94%)
- **Off-scale residual:** 0 (R2 spec is +2/+1/-1; off-scale votes can be clamped at aggregation time but signal the R1-scale prior leaking through)

## Off-scale breakdown

- `codex-r2b`: clean (no off-scale votes)
- `gemini-r2`: clean (no off-scale votes)
- `opus-r2b`: clean (no off-scale votes)
- `sonnet-r2b`: clean (no off-scale votes)


## Vote-category distribution

| voter | rename | keep | canonicalize | add-alias | name-unnamed |
|---|--:|--:|--:|--:|--:|
| `codex-r2b` | 0 | 0 | 0 | 0 | 0 |
| `gemini-r2` | 5 | 47 | 7 | 5 | 5 |
| `opus-r2b` | 0 | 0 | 0 | 0 | 0 |
| `sonnet-r2b` | 0 | 0 | 0 | 0 | 0 |

## Quality signal — substantive-note distribution

| voter | total votes | substantive | empty-or-thin | sub-rate |
|---|--:|--:|--:|--:|
| `codex-r2b` | 0 | 0 | 0 | – |
| `gemini-r2` | 69 | 65 | 4 | 94% |
| `opus-r2b` | 0 | 0 | 0 | – |
| `sonnet-r2b` | 0 | 0 | 0 | – |

*Substantive-note rate is the headline depth-of-engagement signal — a +2 with substantive notes carries different aggregation weight than a +2 with no notes, regardless of identical face-value weight.*

