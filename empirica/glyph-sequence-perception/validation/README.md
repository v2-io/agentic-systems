# validation/ — checks of the harness before and around the real rounds

These are copies of runs that were first made in a session scratch directory on 2026-10-04 and moved here the same evening. Joseph asked for it: *"make sure you aren't tracking things in your scratchpad instead of the empirica directory — the methodology and intermediate tracking things are important parts of the story."*

## synthetic/ — the loop against planted truth (PLAN.md §8, step 5)

Each run is `python3 harness/seq/round.py --data <dir> loop N --synth` against `synth.world_default()` and `synth.minds_default()`:

- **The world:** six planted sequences.
  - **A:** ①…⑧.
  - **C:** ▁…▇.
  - **D:** ○◔◑◕●, holistic: perceived in sets, not in triads.
  - **E:** ⚀…⚅, with a tie.
  - **F:** ⑴⑵⑶⑤⑷⑸⑹, which shares the bridge glyph ⑤ with A.
  - **B:** ❶…❻, never seeded.
  - Plus 160 distractors.
- **The minds:** four synthetic minds in three families, with planted slot bias, ⟂-propensity and guessing.

Each `validate-rNNN.txt` is `harness/seq/validate.py` on the run's last completed fit. It was re-run when the runs were moved here.

| run | code it ran on (asf commit) | what it showed |
|---|---|---|
| `synth1` | before 120ac49d: the first harness, no connectivity penalty | One round. The fit's main candidate interleaved four planted sequences (30 glyphs). The likelihood alone cannot object to interleaving, which preserves every within-sequence relation. That is why the witnessed-connectivity penalty exists. The 30-glyph fit is **not preserved**: the run's `fit.json` and `report.md` were overwritten by a short re-analysis made while profiling, after the penalty was added (1 chain, 600 iterations). |
| `synth2` | 120ac49d: connectivity penalty, any single answer counts as a witness | A, C and D fully recovered by r002. One splice: C and E interleaved (`⚀▃⚁⚃⚂▅⚄▇⚅`), knit together by a noisy mind's answers. That is why witnesses need ≥ 2 consistent answers and a majority. Stopped during r003, when the next fix landed. |
| `synth3` | 980cf770: witness rule ≥ 2 and majority | A, C, D and E fully recovered by r003. No splices. Holistic signature on D (s3 ≈ 0.1, s4 0.5–0.97). F at 4 of 7 glyphs; B not found. |
| `synth4` | fdcbd921: structure fitted before nuisance; ε prior; restarts from seeds | Same recovery as synth3. |
| `synth5` | da173935: strict witness (ties only by tie answers); deterministic prune | Same recovery. |
| `synth6` | 345ff38e: triple perception = max over candidates holding it | **The validation of the code the real rounds ran on.** A, C, D and E fully recovered with order agreement 1.00, F at 6 of 7, no splices, D's holistic signature recovered, B not found. |

**The limit these runs show.** A sequence that is never seeded is not found within 4 rounds. Only the uniform share of each round searches the ⟂ space unaided, which is the cost seeds exist to save.

**The model's slot-bias estimate is weak.** The fitted `beta` stays near 0.5 for every mind. Read slot bias from the model-free rotation table in each round's `report.md`. That table found the planted slot-biased mind in every run.

## shakedown-2026-10-04/ — first contact with the real minds

A dry-run init and round-0 plan was made with the then-current code (120ac49d). Two sheets each went to sonnet55, haiku45, grok46, gemini38flash and glimmer30b-sheet, to check that every mind can answer the new sheet format and that the parser reads it. All five answered all their sheets. These answers are **not** part of the study's evidence: the round-0 plan in `data/rounds/r000/` was drawn independently.
