# R2 Voting — Early Cohort (v1-prompt cards, paused)

What's here: the R2 voting cards and trackers from the **first cohort** of voters who walked the round under the v1 launch prompt — that is, *before* the methodology refinements landed (the workflow restatement prerequisite, the expected-course checklist, the explicit anti-pattern naming of R1's wider scale, and so on). The cards are paused, not abandoned: the votes inside them carry real signal we don't want to lose, and we'll figure out how to weigh them at aggregation time alongside the v2-methodology cohort.

Gemini's card is **not** here — Gemini transitioned smoothly into the v2 methodology mid-walk and stayed active in `msc/naming/round-2-cards/`. The three cards in this directory are voters where the v1-prompt failure modes shaped the output enough that mixing them with v2-methodology cards at face value would distort the aggregation signal.

## Per-voter notes

- **`opus-r2`** — 76 of 629 targets voted, 235 candidate-row votes, 99% with substantive notes. Engagement quality high within coverage. Off-scale issue: 47 `+3`, 13 `-2`, 2 `-3` votes (62 of 235 = 26%) using R1's wider scale instead of R2's `+2/+1/-1` spec. The agent's process notes explicitly rationalized the deviation as "a missing neutral-vote slot in the weight scale" — a documented case of training-prior overriding spec.
- **`sonnet-r2`** — 94 of 629 targets voted, 208 candidate-row votes, 100% substantive. Stalled at the 600s watchdog mid-batch (was about to fill targets 54-80 when the runtime killed the agent), so no closing process notes. 58 `+3` votes (~28% off-scale).
- **`codex-r2`** — 629 of 629 targets voted (full coverage), 794 candidate-row votes, **2% substantive**. The cleanest single demonstration of load-induced completion-shape we've seen: top-pick at +2 on every target with overwhelmingly empty notes. On-scale (no R1-leakage) but the engagement depth makes the votes nearly unweighted as evidence.

For the full diagnosis of the cohort's failure modes and the methodology refinements that followed, see [`msc/naming/handoff-2026-04-29-post-r2-launch.md`](../../handoff-2026-04-29-post-r2-launch.md) (the post-launch handoff is now archived; this snapshot stays here for archaeology) and [`doc/naming-cycle-methodology.md`](../../../../doc/naming-cycle-methodology.md) (the round-design corrections that landed in response).

## How to think about these at aggregation time

The progress-checker (`bin/naming-r2-progress`) only scans `msc/naming/round-2-cards/`, so these cards no longer show up in active monitoring. They're paused, not deleted.

When the aggregator gets built, it will face design choices about how to weight the v1-prompt cohort. A reasonable starting hypothesis:

- **`opus-r2` and `sonnet-r2`** — the high-engagement-low-coverage votes carry useful signal. Substance-weighted (notes ≥ threshold = full weight) they're roughly comparable to the v2 cohort's depth. Off-scale clamping (+3 → +2, -2/-3 → -1) recovers most of the intensity information; the wider-scale provenance can be preserved as a marker.
- **`codex-r2`** — the empty-noted majority is closer to noise than signal. Substance-weighting the codex card heavily down-weights its volume to the small minority where Codex did engage. The 12 substantive-noted votes might still be useful as input.

These are starting points for the aggregator design conversation, not commitments.

## What replaced these

After the methodology refinements landed, the new voter cohort uses different seeds (`{model}-r2b`) so their cards have different shuffles from the v1-prompt cohort. That keeps the two vote sets distinguishable in any future aggregation that wants to weight them differently.
