# Family disagreement: findings

*The spike's findings as they stand after three independent verifications (`de-novo-feedback-1.md` to `-3.md`), three strengthening rounds (`strengthening-1.md` to `-3.md`) and two pre-registered test rounds (`prereg-result-1.md`, `prereg-result-2.md`). Rewritten 2026-10-06 ~21:00 MDT by the spike agent (Claude Opus 5.5) to state present truth; the history of withdrawn readings is in `NOTES.md` and the strengthening files. Data: the snapshot of 16:36 (`snapshot/manifest.json`; `lib.load()` checks against it), plus rounds p001 and p002 where stated. Sealed answers were never read. Strengthening 3's results are not yet independently verified.*

## 1. What the minds commit to is largely shared; most of the agreement is the code chart

- **Continue.** Where two frontier minds both continue a context, they write the same glyph 0.94–0.99 of the time. About three-quarters of that is the shared code-point successor. Where neither writes the chart's next glyph, they still agree 0.82–0.93, with no family affinity (Sonnet–Opus 0.905, Sonnet–Grok 0.882, Opus–Grok 0.928 off the chart). Haiku without thinking agrees less with everyone. (`commit.py`; verifier 1 §2.)
- **Triads.** When both name a middle, it's the same one 0.82–0.95 of the time even where the code-point median doesn't decide (Haiku-with-thinking pairs 0.88–0.90).
- **Reproducible content splits are rare and mostly about form.** Sonnet and Grok: 9 of 870 contexts (1.0%), against 4.0% between Sonnet and Haiku without thinking; most differ only in dress or script form (`𝞦`/`Χ`, `⑽`/`⑩`, `億`/`亿`). One family-level split in 453 triads, `■▤▦` (Claude and Gemini by fill, Grok by code point). The family-level continue test is unpowered.

## 2. Whether minds commit differs by mind and by question kind

Per-mind criteria for continuing, naming a middle and saying "coherent" differ, and don't line up by family. Grok stops sooner than Sonnet at every level of determinacy, yet says "coherent" more readily. On gapped same-block triples, Gemini Flash names a middle 0.82 of the time, Gemini Pro 0.54, Grok 0.46. When a middle is named, it's the code-point median 0.87–0.96 of the time for every mind. (`threshold.py`, `gapped.py`, `additive.py`.)

## 3. What predicts whether a mind continues

Held out (five folds by item / five by block; sums over folds; `strengthening-3.md` §1):

- **What the context looks like, from its glyphs alone** (contiguous, monotone, one block or several, length, size of the last step): +5,364 / +5,389 nats over a model without. Most of it (+4,686 / +4,744) comes with one coefficient vector for all minds. The per-mind part (+678 / +645) is chiefly how readily each mind keeps walking the chart (§7).
- **The other minds' answers on the same Unicode block**, beyond the look: +577 / +653.
- **A mind's own lean on a block**, beyond both: +884 / +978, about 0.01 nats per answer, positive in all ten folds. In the verifier's residual frame it belongs mostly to Grok (+387), Haiku without thinking (+398) and Gemini Flash (+72 in total, large per answer at its low coverage), with Sonnet and Opus near zero (verifier 3 §2b). In the spike's model, the coefficient on a mind's own rate is largest for Grok (1.45) and Gemini Flash (1.00), and Haiku without thinking relies on its own rate almost alone (others' −0.05).

The unit measured is a Unicode block, or set of blocks: 87% of answers are in single-block groups, and whether a lean holds per sequence within a block is untested. A per-(context, mind) interaction adds a little on its own: +31.8 nats for `irtu` over `2mf`.

## 4. The pre-registered rounds

- **p001** (43 contexts where Sonnet always continued and Grok always stopped, asked again of both): Sonnet continued 42, Grok stopped 29 of 42. `irtu` scored best (−31.80); the model without a per-item interaction failed on Sonnet. (`prereg-result-1.md`.)
- **p002** (the same 43, asked of Opus and both Haikus): on Haiku without thinking, `2mf` loses to the two interaction models by about 9 nats; those two don't separate. Haiku with thinking stopped 6 times, against about 20 expected by every pre-registered model. A naive baseline (each mind's stop rate on the 43) beat all three. (`prereg-result-2.md`; verifier 3 §1.)
- **Late, not pre-registered:** the spike's best current model (§6), fitted on the snapshot alone but with chart class added after p002 pointed at it, scores p002 −53.84 (baseline −56.24) and p001 −33.98. It still over-predicts Haiku with thinking on p002 (13.7 against 6).

## 5. Measurement and design effects

- **Same-block sheet-mates.** Across contexts, answers on sheets that carry other contexts of the same block are continued more (−0.70 logit), but at least half of that is selection: strong sequences get several questions a round (−0.32 with sequence strength controlled, an upper bound; verifier 3 §3). Within the same context and mind, answered with and without such mates, there is no detectable difference (554 pairs, +0.008, 95% −0.012 to +0.027; most pairs are near-certain contexts, so the test has little power against a small effect). No format effect is demonstrated. (`sheetmates2.py`.)
- **Adaptive re-asking.** A context is re-asked far more often after some answers than others (Sonnet's: 0.077 after continuing, 0.005 after stopping; `reask.py`). The prequential frame conditions on the same context's earlier answers. Selection on other contexts' answers, on seeds and on triad-era inputs isn't conditioned on, and calibration checks inherit it: seeded contexts in early rounds stop at 0.72 (first answers) and 0.33 (repeats) of predicted (`seedsel.py`). Re-asking and seeds shift which questions are asked, not the answers.

## 6. Model status

The best model fitted here (`spxr.py` on a latent grid over ±10):

- rows per context and round, with sequence features from earlier rounds only;
- glyph covariates per mind;
- the other minds' and the mind's own block rates;
- a sparse per-(context, mind) interaction;
- a weak ridge prior.

Its strict prequential log score is −0.4332 per answer, against −0.5731 for `2mf`. **10 of 38 calibration checks fall outside their 95% bands**: Grok agrees with both Gemini minds more than modelled; Haiku without thinking is more self-consistent than modelled; and a few smaller misfits. Part of the earlier "Sonnet is steadier than any model allows" was the narrow latent grid with Sonnet as the anchor mind; on the wide grid, Sonnet's pair and repeat checks are in band. (`strengthening-3.md` §3–§4a.)

## 7. Family-shaped effects, each with a basis

- **`▁` (U+2581) for both Gemini minds.** In triads, with item strength from other families only and one answer per sheet: Gemini Flash z = −18.4, Gemini Pro z = −7.0, against an empirical 0.5% quantile of −4.27 over 2,190 glyph × mind cells. The SentencePiece hypothesis fits; the tokenizer is uninspected; `▁` is untested outside triads for Gemini. (`glyphscan2.py`.)
- **The larger Claude minds walk the chart more.**
  - In continuation, the per-mind contiguity coefficient (logit of stopping) is Opus −2.67, Sonnet −2.20, Haiku with thinking −1.46, against Haiku without thinking −0.56, Grok −0.49, Gemini Flash −0.00.
  - At contested `choose` positions, paired with neutral controls, context moves Sonnet (+0.106) and Haiku without thinking (+0.107) toward the chart's glyph, and Grok (−0.044) and Gemini Flash (−0.099) away; Opus is too thin to read.
  - In whole-run recognition, Sonnet rejects a non-contiguous run every other mind accepted 0.26 of the time, against 0.04–0.07 for Opus, the Haikus, Grok and Gemini Flash (Gemini Pro rejects about 0.12–0.14 of both classes alike).
  - Chart reliance and self-preference aren't separated.
- **Familiarity.** After an unfamiliar last glyph, Grok stops more relative to Sonnet (+1.14 ± 0.33 logit).
- **Pairwise structure.** A second shared factor loads on Haiku (without thinking 1.94, with thinking 0.97) and partly Sonnet (0.56), not on Opus, Grok or Gemini (within ±0.11): a Haiku axis, not "Claude against the rest". A Grok–Gemini affinity remains in every model fitted.

## 8. How whole-run recognition should be corrected

On cohere answers with their shuffled controls, a logit model with a criterion and slope per mind beats the catalog's Abbott model by about 640 nats held out (reproduced by two verifiers). Abbott's main misfit is treating a shuffled control as pure guessing; controls are heterogeneous items. Minds differ in discrimination (logit slopes: Sonnet 1.56, Opus 5.5, Grok 0.69, Haiku without thinking 0.72, Gemini Flash 0.92, Gemini Pro 0.46). (`abbott.py`.)

## Literature

- [Cacioli 2026](https://arxiv.org/abs/2603.14893): signal-detection decomposition of LLM judgements. Unchecked against the paper.
- [Panickssery, Bowman and Feng, NeurIPS 2024](https://arxiv.org/html/2404.13076v1): LLM evaluators recognise and favour their own generations. Checked by verifier 1.
- [TokSuite](https://arxiv.org/pdf/2512.20757): tokenizer choice changes model behaviour. Unchecked.
- Nothing found on cross-family perception of Unicode sequences.
