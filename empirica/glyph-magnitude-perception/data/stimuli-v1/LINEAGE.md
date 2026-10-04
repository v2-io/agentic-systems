# Lineage of the v1.0 stimulus sets and runs (recorded 2026-10-03)

*Why this file exists.* The v1.0 builder (a Claude Opus 5.5 subagent) worked from a brief that quoted one sentence from Joseph: *"round out the data more and more"*. The rest of the brief was the coordinating agent's interpolation of his intent. That included a paragraph that:

- named the aspectus SIGNA age-column ladder `·╶╌╍━═⚬○◎◉⬤`, which Joseph has said is being discarded;
- offered two of the coordinator's own observations about it as "measured facts";
- invited findings bearing on choosing a column ladder.

Joseph had not asked for any of this. The labels below record, for each stimulus set and run family, whether its selection could have been shaped by that paragraph. No judge ever saw the paragraph or any framing from it: judges saw only the generic prompts in `protocol/PROTOCOL-v1.0.md`.

## Classes

- **A — fixed by rule or taken from the pilot.** The content was produced by a fated sampling rule or carried over from pilot materials. The builder wrote the rules, but chose no individual stimulus.
- **B — chosen by the builder.** Individual items or sets were hand-picked by the builder under the brief. They were picked in service of the pilot's claims, but the builder cannot rule out that the SIGNA glyph families coloured what was salient.
- **C — SIGNA-driven.** The set exists because of the coordinator's SIGNA paragraph.

## Stimulus files

| file | class | notes |
|---|---|---|
| `pool.json` | A | seed stratum: glyphs from survey sequence records, held out from the pilot (coverage defect: only 4 of 7 surveys; see PROTOCOL notes). Uniform tail: block-uniform fated draw. |
| `triads.jsonl` | A | fated from `pool.json`. SIGNA glyphs ◎ ⚬ occur in 16 presentations via survey records. |
| `format-pairs.jsonl` | A | pilot walk2 pairs (fated sample) plus fated fresh pairs |
| `pilotcond/` | A (stimuli); B (the arm's design) | the 160 pilot-replication pairs in the pilot's walk5b wording. The decision to run a pilot-condition arm was the builder's. |
| `conflict.jsonl` (from `harness/runner/conflict-items-v1.json`) | B | every item hand-built. Its measured-ink annotations use the Ghostty table in `firmatum/utils/utf/`. The builder found that table through the coordinator's SIGNA paragraph, which pointed to `utf/` for "rendering measurements". Items with ⬤ or ● (size vs count) are the ones most plausibly coloured by SIGNA's circle family; ⬤ also comes from the pilot's `·•●⬤`. |
| `holistic-pairs.jsonl`, `gestalt.jsonl` | mixed: A for dice, ramp, unfold, risebar, rotate4, drain (pilot) and the fated noise foils; B for the held-out candidates | the held-out candidates (elab-n/s/l/z, rings, rays, nest, dimension, stem, check, upper-eighths) were picked by the builder from survey records |
| `top40-candidates.json`, `top40-steps.jsonl`, `top40-gestalt.jsonl`, `top40b-*` | A | selected by a cross-surveyor concordance rule (written by the builder) answering Joseph's own top-40 request |
| `consumer-signa-pairs.jsonl`, `consumer-signa-gestalt.jsonl` | C | the SIGNA ladder as supplied by the coordinator's paragraph |

## Run-level notes

- **Feature route.** The ink feature (Ghostty `packed_density`) used across the analyses came by the route described under `conflict.jsonl`. Measuring ink as a feature correlate was independently sanctioned by Joseph in RECONCILIATION-QUEUE.md, 2026-08-25.
- **Glimmer.** The Muse Glimmer 30B run (suggested by Joseph; "key datapoints only") gave one of its three instrument slots to the SIGNA set. That allocation was class C.
- **Judge panel and opt-in.** The judge panel, and the scale of judge calls, rest on the coordinator's reading that Joseph's request was the opt-in for judge panels. Joseph has since ratified that reading, including the quota cost. The brief's line "token spend isn't the constraint" was the coordinator's.

## Joseph's post-hoc reframing (2026-10-03, his)

> *"we can essentially say that the 'old signa' sequence can be considered a plausible human-created sequence thrown in as a control, basically, to see just how unbiased the actual experiment results are … (It's not a full-on null-result control, but one that is a nuanced perspective anyway, or might be with the correct analysis)"*

The limits, recorded with the reframing:

- n = 1;
- the sequence was not randomly chosen;
- its control role was assigned after its data had been seen by the builder and the coordinator;
- it is monotone within each glyph family and arbitrary only at the family seams.

Its analysis as a control is to be specified, and run, by an analyst who has not seen the existing results.
