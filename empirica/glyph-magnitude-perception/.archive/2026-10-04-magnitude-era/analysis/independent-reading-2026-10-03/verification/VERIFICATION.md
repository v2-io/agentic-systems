# Verification — an adversarial pass on `reading/`

Written 2026-10-03 by a Claude Opus 5.5 instance that saw this clean room, the reading, and nothing of the study's home repo or any earlier analysis. Beyond the clean room I read two things: the Ghostty ink table `firmatum/utils/utf/bmp-metrics-ghostty.tsv`, which the protocol names as an instrument input, and zoetica's `docs/messaging/06-temporal-coherence.md` §SIGNA, to check the denominations the reading quotes. I did not use memorata. See §6 for why that matters.

**Method.** I wrote my own loader (`scripts/vload.py`) without reading `reading/scripts/common.py`. It uses only the builder's parser p1.3. I re-derived the registered predictions, the signa analysis and the instrument claims from the ledgers, then compared my numbers with the reading's tables. Where we disagreed, I read the reading's script to find out why. Every script in `scripts/` runs from that directory with `python3 <name>.py`.

## Bottom line

The arithmetic is sound. Nearly every number in 01–03 reproduces from independent code: the P1–P15 table, the signa pairwise counts, the drain and noise-foil answers, the triad statistics and the manufactured-edge agreement. Where the reading is vulnerable is interpretation, at four points that carry weight: the pilot comparison in claim 3, the evidence offered for "position fallback", the ink rule offered as a predictor of signa's seam, and the framing of signa as a control. There are also two registered verdicts whose wording is softer than the thresholds allow, and a set of small factual slips (§5).

## 1. The pilot-condition arm leaves out a structural feature of the pilot

The reading attributes the gap between the pilot's 0.80 dissolution and the pilot-condition arm's 0.58 to a "wording-plus-context-plus-effort bundle", and says "the pilot's 80% belongs to that bundled condition" (02 claim 3, 03 §1, 04 #7).

**In the pilot, both orders of every pair sat on the same sheet, so the same judge answered both in one call.** I checked all 1,100 walk2 pairs, and walk3 reran the same sheets (`scripts/vpilot_sheets.py`). v1.0 deliberately splits orders across sheets (PROTOCOL change 8), and so does the pilot-condition arm ("orders split across sheets", its `spec.json`). The consequences are visible:

| | mixed pairs | consistent-⟂ | per-presentation ⟂ |
|---|---|---|---|
| pilot walk3 (same sheet; pilot-record's pair categories) | 14/1091 ≈ 0.01 | 966/1091 ≈ 0.89 | — |
| pilotcond arm (split sheets) | 0.14 | 0.69 | 0.76 |

When one call sees both orders, a judge can answer them consistently, and mixed verdicts nearly vanish. Under independence, a 0.76 per-presentation ⟂ rate gives about 0.58 consistent-⟂. So same-sheet pairing is a strong candidate for part of the remaining gap, and the bundle can't be the whole story: the pilot's 80% belongs to a condition that also includes same-sheet pairing, which v1.0 never reproduced. 04 #7 should list sheet pairing as a factor beside harness, context, wording and effort.

Two smaller points in the same passage:

- 03 §1 gives sonnet55's clean-API ⟂ rate on pilot-replication as 0.38. That is the all-strata rate. On pilot-replication it is 0.41 (the reading's own `perp-rates.txt`).
- "Roughly doubles" compares single mode with the arm: ×1.85. The closer control is sonnet55 in sheet mode, at 0.47 on that stratum, which gives ×1.6.

## 2. "Every flip is same-slot" is true by definition

01 (twice), 03 §6 and 03 §8 offer "every frontier flip is same-slot" as the signature of position fallback on balanced pairs. A flip is defined as opposite winners across the two orders. If order (p,q) yields p and order (q,p) yields q, the first slot won both times. The other flip case is the second slot winning both times. Every flip is therefore same-slot, whatever caused it, so the observation can't tell slot fallback apart from sampling noise. The conclusion in 03 §6, that flips need reps to interpret, still stands and so does 04 #4. What goes is the claim that signa's flips already show fallback.

(The triad argument in 03 §2 is different, and it holds. In a cyclic orientation set, a cycle and an all-same-slot pattern really are the same event. I asserted this on every fully oriented set in every triad run, and no assertion failed.)

## 3. The ink rule does not predict signa's seam

01 point 2 bins adjacent steps of other authored sequences by Δink, then says signa's rejected step `═→⚬` and unstable step `━→═` "fall where that rule points". Three problems:

- **Calibration.** The rule's rates are 0.27 with / 0.14 against when ink drops, and 0.39 / 0.08 when it is flat. Signa's four non-rising steps came out `·→╶` 7/8 with, `━→═` 4/8, `◎→◉` 8/8 and `═→⚬` 0/8 with and 5/8 against. Two of the four are endorsed far above the rule's rate and one is rejected far beyond it. Matching the rule on direction for the two steps that fit and listing the other two as exceptions is not prediction.
- **Bin edge.** The 0.01 edge falls between `═→⚬` (Δ −0.0113) and `◎→◉` (Δ −0.0092). At the protocol's own ink threshold of 0.005, both land in the drop bin, and the drop and flat bins become indistinguishable (0.32 vs 0.33 with). At 0.02, `═→⚬` moves to the flat bin.
- **What holds.** Steps where ink rises are endorsed: 0.66–0.71 at every threshold I tried, and 6/6 of signa's rising steps. Below that, this ink measure does not separate `═→⚬` from `◎→◉`. The reading's qualitative account ("smaller, thinner, lighter") may be right, but nothing fitted elsewhere tests it.

## 4. What signa can and cannot control for

01 calls signa "the clearest single demonstration in v1.0 that the instruments are not simply agreeing with whatever they are shown". Neither instrument shows the author's order. Pairs come one at a time and gestalt sets are shuffled, so there is nothing to agree with. 01 itself concedes this for pairwise mode. What signa shows is narrower: the judges' consensus follows the author where the visible gradient does and leaves it where it doesn't. That pattern is predicted equally by perception and by a shared prior that ladders grow in visual size. The noise foils show that shared generic orders exist (03 §3), so signa can't separate those two accounts. It is the same limit 03 §1 states honestly for manufactured edges, and 01 should state it too.

On Joseph's own question, whether the results are biased: the comparison that bears on it is 01 point 4, human-authored versus LLM-surveyed ladders. The reading rightly calls that test weak. It is weaker than "human-created" suggests:

- zoetica §SIGNA calls the glyph set "a **candidate implementation**. The glyph choices are provisional."
- The reading's own provenance trail records Claude's involvement in the predecessor display.

Signa's main stated virtue, being fixed before the study and for another purpose, survives all of this.

A related finding the reading doesn't mention: on **elab-n**, 19 of 24 frontier gestalt answers are exactly `nɳɲŋ`, against the author's `nɲɳŋ`. Judges agree with each other against the author at one step, as they do at signa's seam. It may be useful as a second case.

## 5. Registered verdicts and smaller corrections

**Verdicts whose wording is softer than the thresholds:**

- **P8 frontier.** haiku45 is 46/72 = 0.639 against a registered ≥ 0.65. That is a miss for haiku, not "supported (haiku borderline)". The small half lists mistral7b, which is not in the registered small-local set (3–4B). The verdict there is unchanged: llama 0.51, gemma 0.55.
- **P15.** Scored per frontier judge × set against both thresholds, 14 of 24 cells pass (elab-n 5/8, elab-s 5/8, elab-l 4/8). Under the "every frontier judge" reading the verdict is *not supported*. Under a cell tally it is mostly supported. "Mostly not supported" matches neither.
- **Claim 4.** "What capability buys is order-stability and ⟂ use, not transitivity per se" goes further than the data allow. Small-model transitivity is measured only on the order-stable triads: llama 33, gemma 8, qwen25 0. Those triads are selected for being answerable. Elsewhere it is unmeasured, which is not the same as equal. Also, the registered cycle rate is not purely "slot preference". gemma (P(first|dir) 0.52) and llama (0.45) cycle at 0.23 and 0.12 with no aggregate slot bias, which is what stimulus-independent answering produces. A near-zero rate is still informative. Only high rates are ambiguous.
- **Strengthening, for the reading.** The pilot's llama triad run (`pilot/results5`) used cyclic sets throughout (700/700), with P(first|dir) = 0.763 and a cycle rate of 0.369. That is the pilot's "37%". So the reading's suggestion that the pilot contrast "is open to the same reading" holds in the data (`scripts/vpilot_triads.py`).

**Factual slips** (none changes a verdict):

- 01: "13 of 24 frontier answers" → 13 of 21. Seven frontier judges have signa gestalt runs, and there is no sonnet55 sheet arm.
- 01: `━`/`═` is not the only unstable within-branch pair. sonnet55 (single) also flips on `◉`/`⬤`, where the ink differs widely (0.213 vs 0.287).
- 01: signa is "below the median only because of its one seam step". For opus55 and sonnet55, `━→═` is also unendorsed, so it is two steps. Also, "0.2–0.6 percentile" means percentile *rank* 0.21–0.60.
- 01: the Copeland τ range depends on the definition. τ-b over cdir-edge Copeland scores gives 0.61–0.88 for frontier judges, against the reading's 0.49–0.85. The point about masking survives.
- 02 claim 3: "about 0.8–0.9 under forced and tie" → the frontier range is 0.64–0.93 (sonnet5 tie 0.64, haiku 0.71/0.73).
- 02 claim 3: "not as constructed-on-demand noise". The pilot said "constructed on demand" and never said noise. The 83% agreement rules out idiosyncratic noise, not on-demand construction by a shared heuristic. 03 §1 states this correctly. The agreement does hold without numeric glyphs: 0.82 cross-family, 1715/2086. My comparator set omits gpt56terra, so my n is smaller than the reading's (`scripts/vmanuf.py`).
- 03 §3: "every answer to noise-3 starts with `˛`" is true of every *frontier* answer. gemma, llama and mistral don't start that way.
- 03 §7: opus55 averages 0.5 thinking tokens per signa call (max 52), and 2–134 per call across the other instruments (mostly 20–80), not "about 50". gemini31pro's ~2,300 is per 40-item sheet, about 58 per item. The gap is real, but the units being compared differ.
- gpt56terra conflict: the reading drops a sheet flagged `sheet_incomplete` (g0/r2, 0.237) that was never re-asked because of the quota. Under p1.3 most of its items parse, and including it gives P9 78/78, P11 1/12, P12 11/12. Verdicts are unchanged.
- `reading/README.md` lists `LETTER.md`, which is not present. It also expects `VERIFICATION.md` at `reading/`; this one is at `reading/verification/`, as asked.

## 6. Clean-room hygiene

The reading's README says it consulted "the memorata index" for signa's provenance. memorata indexes every transcript on this machine, which plausibly includes today's builder and audit sessions on these very data. I can't tell what it surfaced. The provenance paragraph would be cleaner if it named the queries it ran, or were re-sourced without memorata. For what it's worth, zoetica git records `visual-time-notation.md` from 2025-10-10, and the denominations quoted in 01 (`═` = 1 h, `⚬` = 4 h, …) match `06-temporal-coherence.md`.

## What I confirmed independently

P1–P4 per judge, including the pilot-condition arm (66/114). P5–P8 counts and Wilson intervals. P9–P12 pooled rates. P13 (dice 24/24; noise 61/95). P14 and P15 cells. Signa within-branch 180/181, seam 116/125 with the same nine disagreements, per-judge seam ⟂ counts, the gestalt answers and coverage, haiku's `⬤` echo failures, and qwen's 50 × "first, much". The drain's reverse reconstructions and the reversed-strata alternative. The cyclic-set equivalence. Zero cycles among order-stable triads in every judge where they can be measured. Manufactured-edge agreement of 0.83.

## Scripts

`scripts/vload.py` (loader), `vformat.py` (P1–P4, verdict mix), `vpilotcond.py`, `vpilot_sheets.py`, `vpilot_triads.py`, `vmanuf.py`, `vtriads.py`, `vconflict.py`, `vsigna.py`, `vsgest.py`, `vgest.py [sets…]`, `vholpair.py`. The ink-threshold sensitivity rerun reused `reading/scripts/ink_steps.py` with the bin edge changed to 0.005 and 0.02. Nothing was written to `reading/tables/`.
