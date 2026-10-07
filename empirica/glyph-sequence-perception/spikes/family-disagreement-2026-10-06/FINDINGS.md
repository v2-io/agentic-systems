# Family disagreement: findings

*The spike's findings after four independent verifications (`de-novo-feedback-1.md` to `-4.md`), four strengthening rounds (`strengthening-1.md` to `-4.md`, the last a closing pass) and two pre-registered test rounds (`prereg-result-1.md`, `-2.md`). Rewritten 2026-10-06 ~21:35 MDT by the spike agent (Claude Opus 5.5) to state present truth; the history of withdrawn readings is in `NOTES.md` and the strengthening files. Data: the snapshot of 16:36 (`snapshot/manifest.json`; `lib.load()` checks against it), plus rounds p001 and p002 where stated. Sealed answers were never read.*

## The short answer

- **Recognising whole runs as sequences:** on the evidence so far, Claude and Grok don't disagree beyond each mind's strictness and sharpness (§4).
- **Continuing a run:** the large Claude minds (Sonnet, Opus) and Grok disagree chiefly about one thing: whether to keep walking Unicode's code chart where the run follows no given order. The Claude minds keep walking; Grok, and Gemini Flash with it, stop (§2).

METHODOLOGY §1 sets chart walks apart as not evidence of a felt sequence, and §2a reads a "none" as end evidence, never as evidence against. So the family difference found is in chart-following and in where an end is called, not in which sequences are perceived. The clearest perceptual family effect is `▁` for both Gemini minds (§8).

## 1. What the minds commit to is largely shared; most of the agreement is the code chart

- **Continue.** Where two frontier minds both continue a context, they write the same glyph 0.94–0.99 of the time; about three-quarters of that is the shared code-point successor. Where neither writes the chart's next glyph, they still agree 0.82–0.93, with no family affinity (off the chart: Sonnet–Opus 0.905, Sonnet–Grok 0.882, Opus–Grok 0.928). (`commit.py`; verifier 1 §2.)
- **Triads.** When both name a middle, it's the same one 0.82–0.95 of the time even where the code-point median doesn't decide.
- **Reproducible content splits are rare and mostly about form.** Sonnet and Grok: 9 of 870 contexts (1.0%), mostly dress or script form (`𝞦`/`Χ`, `⑽`/`⑩`, `億`/`亿`). One family-level split in 453 triads, `■▤▦` (Claude and Gemini by fill, Grok by code point).

## 2. What the disagreement about whether to continue rests on

On first answers to contexts both minds answered, stop rates and the logit gap by kind of context (given walks: windows of an alphabet or number order in one dress, `catalog/given_walk.py`; verifier 4, `de-novo-4/e5.log`):

| pair | contiguous, no given order | given walks | monotone | other |
|---|---|---|---|---|
| Sonnet → Grok | 0.088 → 0.254, **+1.26** | +0.52 | +0.36 | +0.12 |
| Opus → Grok | 0.085 → 0.260, **+1.33** | +0.22 | +0.42 | +0.18 |
| Sonnet → Gemini Flash | 0.150 → 0.226, +0.50 | +0.25 | −0.15 | −0.25 |
| Grok → Gemini Flash | 0.250 → 0.224, −0.14 | −0.03 | −0.42 | −0.36 |
| Sonnet → Haiku without thinking | +1.60 | +1.30 | +0.21 | +0.02 |
| Sonnet → Opus | −0.10 | +0.21 | −0.09 | −0.07 |

- **Where the disagreements fall.** 52% of Sonnet–Grok commit disagreements fall on contiguous runs with no given order (42% of shared contexts), and Grok is the one stopping in 90% of them. 30 of the 43 flat contexts of p001/p002 are such runs.
- **The split on this axis** is {Sonnet, Opus} against {Grok, Gemini Flash}. Haiku without thinking stops more than Sonnet everywhere, given walks included: a general difference, not a chart one.
- **Other question kinds** have their own per-mind criteria too. Grok says "coherent" more readily than Sonnet. On gapped same-block triples, Gemini Flash names a middle 0.82 of the time, Gemini Pro 0.54, Grok 0.46. When a middle is named, it's the code-point median 0.87–0.96 of the time for every mind. (`gapped.py`, `additive.py`.)
- **Familiarity.** After an unfamiliar last glyph, Grok stops more relative to Sonnet (+1.14 ± 0.33 logit; `strengthening-1.md`). [inference] This is likely the same chart-walk gap seen through token counts, since obscure blocks are where chart walks without a given order live. Untested.

## 3. What predicts whether a mind continues

Held out (five folds by item / five by block, sums; `strengthening-3.md` §1):

- **What the context looks like, from its glyphs alone** (contiguous, monotone, one block or several, length, size of the last step): +5,364 / +5,389 nats over a model without. +4,686 / +4,744 of it comes with one coefficient vector for all minds.
- **The other minds' answers on the same Unicode block**, beyond the look: +577 / +653.
- **A mind's own lean on a block**, beyond both: +884 / +978, about 0.01 nats per answer, positive in all ten folds. In verifier 4's frame, Grok's lean lives entirely on chart walks with no given order (+325 of +299 nats) and doesn't carry across kinds of context (−2). Gemini Flash's has the same shape. Haiku without thinking's is block-wide and partly cross-class (+371, +97 cross-class). Sonnet's and Opus's are about zero (`de-novo-4/e7.log`). For Grok and Gemini Flash, then, the per-block lean is appetite for walking the chart, block by block.

The unit is a Unicode block, or set of blocks; whether a lean holds per sequence within a block is untested.

## 4. Recognition: which runs are model-sensitive?

- **In aggregate** (`de-novo-4/e3.log`): summed over every run two families judged, a family-specific run position adds nothing for Claude–Grok (2,602 runs, $z = +0.1$). It shows a small excess for Claude–Gemini ($z = +3.0$, 663 runs, mostly non-contiguous) and *more* agreement than modelled for Grok–Gemini ($z = -2.3$, 433 runs). These are nine tests on parameters fitted to the same data, so the two departures are suggestive.
- **Per run, nothing can be read yet.** Only 133 runs have at least two answers from each of two families, and none departs from the model at $p \lt 0.01$.
- **Sonnet is the strictest and most discriminating rater of whole runs** (logit slope 1.56 against Grok's 0.69). It rejects a non-contiguous run that a panel of other minds accepted 0.27–0.35 of the time, against 0.07–0.12 for the others (symmetric panels). A model with per-mind criterion and slope and no contiguity term predicts that exactly against the Claude minds (Opus 49 observed / 50.2 predicted; Haiku with thinking 51 / 52.0). An excess of about 15 remains against Grok, Gemini Flash and Haiku without thinking (114 / 97.7; 66 / 49.9; 127 / 111.0) (`de-novo-4/e4.log`).

## 5. The pre-registered rounds

- **p001** (43 contexts where Sonnet always continued and Grok always stopped, asked again of both): Sonnet continued 42, Grok stopped 29 of 42. `irtu` scored best (−31.80). (`prereg-result-1.md`.)
- **p002** (the same 43, asked of Opus and both Haikus): on Haiku without thinking, the model without a per-item interaction loses to the two interaction models by about 9 nats. Haiku with thinking stopped 6 times, against about 20 expected by every pre-registered model. A naive baseline beat all three. (`prereg-result-2.md`.)
- **Late, not pre-registered:** the best current model (§7) scores p002 −53.84 (baseline −56.24) and p001 −33.98. Chart class was added after p002 pointed at it. It still over-predicts Haiku with thinking (13.7 against 6).

## 6. Measurement and design effects

- **Same-block sheet-mates.** Across contexts, answers on sheets that carry other contexts of the same block are continued more (−0.70 logit). At least half of that is selection: strong sequences get several questions a round (−0.32 with sequence strength controlled, an upper bound; verifier 3). Within the same context and mind, there's no detectable difference (554 pairs, +0.008, 95% −0.012 to +0.027; most pairs are near-certain, so a small effect isn't ruled out). No format effect is demonstrated. (`sheetmates2.py`.)
- **Adaptive re-asking and seeds.** A context is re-asked far more often after some answers than others (Sonnet's: 0.077 after continuing, 0.005 after stopping; `reask.py`). The planner also targets seeded contexts. These shift which questions are asked, not the answers. Checks of consistency condition on the same context's earlier answers; selection on other contexts, on seeds and on triad-era inputs isn't conditioned on, and the calibration checks inherit it (`seedsel.py`).

## 7. Model status

The best model fitted here (`spxr.py`, latent grid over ±10):

- rows per context and round, with block features from earlier rounds;
- glyph covariates per mind;
- the other minds' and the mind's own block rates;
- a sparse per-(context, mind) interaction;
- a weak ridge prior.

Its prequential log score is −0.4332 per answer, against −0.5731 for `2mf`. That score uses each context's posterior and features from earlier rounds, with the global parameters fitted on all answers, the same for every model compared. **10 of 38 calibration checks fall outside their 95% bands**: chiefly a Grok–Gemini affinity, and Haiku without thinking's own consistency. Part of the earlier "Sonnet is steadier than any model allows" was the narrow latent grid with Sonnet as the anchor mind. (`strengthening-3.md` §3–§4a.)

## 8. Family-shaped effects, each with a basis

- **`▁` (U+2581) for both Gemini minds.** In triads, with item strength from other families only and one answer per sheet: Gemini Flash z = −18.4, Gemini Pro z = −7.0, against an empirical 0.5% quantile of −4.27 over 2,190 glyph × mind cells. The SentencePiece hypothesis fits; the tokenizer is uninspected; `▁` is untested outside triads for Gemini. (`glyphscan2.py`.)
- **Chart walks without a given order** (§2): Sonnet and Opus keep walking; Grok and Gemini Flash stop. This is a continuation finding.
- **At contested `choose` positions**, paired with neutral controls, the shifts toward the chart's glyph are within noise: Sonnet +0.106 ± 0.061, Haiku without thinking +0.107 ± 0.060, Grok −0.044 ± 0.054, Gemini Flash −0.099 ± 0.084.
- **Pairwise structure.** A second shared factor loads on Haiku (without thinking 1.94, with thinking 0.97) and partly Sonnet (0.56), not on Opus, Grok or Gemini: a Haiku axis. Grok and the Gemini minds agree more than any model fitted allows, in continuation and in recognition.

## 9. How whole-run recognition should be corrected

On cohere answers with their shuffled controls, a logit model with a criterion and slope per mind beats CATALOG §9's Abbott model by about 635 nats held out. Of those, 596 are earned on the shuffled controls (treating a control as pure guessing is the misfit; controls are heterogeneous items); on the real runs whose strength the catalog reports, about 40. The link itself (Abbott against logit, both with heterogeneous controls) is worth about 160. Minds differ in discrimination (logit slopes: Sonnet 1.56, Grok 0.69, Haiku without thinking 0.72, Gemini Flash 0.92, Gemini Pro 0.46; Opus 2.9–5.5 depending on specification, near separation). (`abbott.py`; verifier 4 §6.)

## Literature

- [Cacioli 2026](https://arxiv.org/abs/2603.14893): signal-detection decomposition of LLM judgements into sensitivity and criterion, with unequal-variance evidence distributions (abstract checked, verifier 4).
- [Panickssery, Bowman and Feng, NeurIPS 2024](https://arxiv.org/html/2404.13076v1): LLM evaluators recognise and favour their own generations (checked, verifier 1).
- [TokSuite (Altıntaş et al.)](https://arxiv.org/abs/2512.20757): tokenizer choice changes model behaviour (abstract checked, verifier 4).
- Nothing found on cross-family perception of Unicode sequences.
