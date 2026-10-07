# Family disagreement: findings

*The spike's findings as they stand after two independent verifications (`de-novo-feedback-1.md`, `de-novo-feedback-2.md`), two strengthening rounds (`strengthening-1.md`, `strengthening-2.md`) and one pre-registered test round (`prereg-result-1.md`). Rewritten 2026-10-06 ~19:30 MDT by the spike agent (Claude Opus 5.5) to state present truth: readings withdrawn along the way, and why, are in `NOTES.md` and the strengthening files, not here. Data: the snapshot of 16:36 (`snapshot/manifest.json`; rebuild with `python3 lib.py --from-manifest`), plus round p001 where stated. Sealed answers were never read. The findings below from strengthening 2 are not yet independently verified.*

## 1. What the minds commit to is largely shared; most of the agreement is the code chart

- **Continue.** Where two frontier minds both continue a context, they write the same glyph 0.94–0.99 of the time. About three-quarters of that is the shared code-point successor. Where neither writes the chart's next glyph, they still agree 0.82–0.93. There's no family affinity in that agreement: on contexts Sonnet, Opus and Grok all continued, off the chart, Sonnet–Opus 0.905, Sonnet–Grok 0.882, Opus–Grok 0.928. Haiku without thinking agrees less with everyone (0.82–0.87 overall). (`commit.py`; verifier 1 §2.)
- **Triads.** When both minds name a middle, it's the same one 0.82–0.95 of the time even where the code-point median doesn't decide; Haiku-with-thinking pairs come lower (0.88–0.90).
- **Reproducible content splits are rare and mostly about form.** Sonnet and Grok each committed at least twice, unanimously and differently, on 9 of 870 contexts (1.0%), against 4.0% between Sonnet and Haiku without thinking. Most share the abstract next element and differ in its dress or script form (`𝞦`/`Χ`, `⑽`/`⑩`, `億`/`亿`). Family-level splits (three or more answers per family): one in 453 triads, `■▤▦`, where Claude and Gemini order by fill and Grok by code point. The family-level continue test is unpowered (14 contexts).

## 2. Whether minds commit differs by mind and by question kind

Per-mind criteria for continuing, naming a middle and saying "coherent" differ, and don't line up by family. Grok stops sooner than Sonnet at every level of determinacy, yet says "coherent" more readily. Gemini Flash names a middle on gapped same-block triples 0.82 of the time, Gemini Pro 0.54, Grok 0.46. Inhibit shows little spread. When a middle is named, it's the code-point median 0.87–0.96 of the time for every mind. (`threshold.py`, `gapped.py`, `additive.py`.)

## 3. The largest mind-specific structure is at the level of sequences

A context's answers are predicted far better from other contexts of the same sequence (taken as the set of Unicode blocks the context spans) than from the context alone. Held out, in all five folds of two fold schemes (by item; by block):

- a shared sequence effect: about +2,300 to +2,500 nats over the best item-level model;
- a **mind-specific sequence effect** on top of it: **about +1,500 to +1,600 nats**.

A per-item mind interaction alone gains nothing held out. The verifier's item-level interaction model gains +31.8 nats in total. (`strengthening-2.md` §2.)

**What it is** [inference]: each mind has its own propensity to continue or stop *on a given sequence*, consistent across that sequence's contexts, beyond what the sequence's shared strength and the other minds predict. Grok and Haiku without thinking lean hardest on their own sequence-level behaviour, Opus and Gemini Pro on the shared part. This is the measurable form of "model-sensitive sequence" in this data.

## 4. Flat splits: the Sonnet side is settled, the Grok side mostly

At the 43 contexts where Sonnet continued every time and Grok stopped every time, each was asked once more (round p001, pre-registered). Sonnet continued 42 of 43, more steadily than any model fitted here allows. Grok stopped again 29 of 42. The verifier's model with a per-item mind interaction predicted p001 best (log score −31.80, against −34.65 for the sequence model and −37.08 for the model without interaction). So a flat split isn't a borderline context answered by chance, and it isn't uniformly settled either: Sonnet's side is near-certain, Grok's repeats about seven times in ten. (`prereg-result-1.md`; `strengthening-2.md` §4.)

## 5. Measurement and design effects that bear on every reading

- **Same-sequence sheet-mates.** A continue question on a sheet that also carries other contexts of the same sequence is continued far more often than predicted: stops at 0.59–0.60 of predicted on first answers, −0.70 ± 0.04 logit. That is format shaping the order a mind reports, about 7% of continue answers. (`sheetmates.py`.)
- **Adaptive re-asking.** A context is re-asked far more often after some answers than others (Sonnet's: 0.077 of the time after it continued, 0.005 after it stopped). Consistency checks are valid only when they condition on what the planner used; the prequential frame does. (`reask.py`, `preq.py`.)
- **Selection on information outside a model.** The planner targeted seeded contexts, which continue-only models don't see; there, early-round stops are 0.72 (first answers) and 0.33 (repeats) of predicted. (`seedsel.py`.)
- **No model fitted here is calibrated on all checks** at once (cross-mind, within-mind repeats, flat splits, same-round pairs). The causes found are listed above. An early-round remainder is unexplained. (`strengthening-2.md` §3.)

## 6. Family-shaped effects, each with a basis

- **`▁` (U+2581) for both Gemini minds.** In triads, with each item's strength estimated from other families only and one answer per sheet: Gemini Flash z = −18.4, Gemini Pro z = −7.0. The empirical 0.5% quantile over 2,190 glyph × mind cells is −4.27. The SentencePiece word-boundary hypothesis fits; the tokenizer itself is uninspected, and `▁` hasn't been tested outside triads for Gemini (no data). (`glyphscan2.py`.)
- **A chart lean in Sonnet and Haiku without thinking.**
  - At contested `choose` positions, paired with neutral controls, context moves Sonnet (+0.106) and Haiku without thinking (+0.107) toward the chart's glyph, and Grok (−0.044) and Gemini Flash (−0.099) away from it; Opus's data are too thin (9 pairs).
  - In whole-run recognition, Sonnet rejects a non-contiguous run that every other mind accepted 0.26 of the time, against 0.04–0.07 for Opus, the Haikus, Grok and Gemini Flash (Gemini Pro rejects about 0.12–0.14 of both classes alike).
  - A per-mind offset for real contiguous runs improves held-out fit; Grok's is the smallest.
  - Chart reliance and self-preference (favouring runs a mind wrote) are not separated. (Verifier 1 §3; verifier 2 §5; `strengthening-1.md` §2.)
- **Familiarity.** After an unfamiliar last glyph (more than one token in two public byte-level vocabularies), Grok stops more relative to Sonnet, +1.14 ± 0.33 logit. In item units Grok, Gemini Pro and Opus sit together, against Sonnet and Haiku with thinking. (`strengthening-1.md` §3.)
- **A second shared dimension is a Haiku axis, not "Claude against the rest".** Its loadings are Haiku without thinking 1.94, Haiku with thinking 0.97, Sonnet 0.56, and Opus, Grok and both Gemini minds within ±0.11. It adds about 93 nats held out. Beyond it, small affinities remain between Sonnet and Opus, and between Grok and Gemini Flash. (`twof.py`.)

## 7. How whole-run recognition should be corrected

On cohere answers with their shuffled controls, a logit model with a criterion and slope per mind beats the catalog's Abbott model by about 640 nats held out (reproduced by both verifiers). The Abbott model's main misfit is treating a shuffled control as pure guessing: controls are heterogeneous items. Minds differ in discrimination (logit slopes: Sonnet 1.56, Opus 5.5, Grok 0.69, Haiku without thinking 0.72, Gemini Flash 0.92, Gemini Pro 0.46). (`abbott.py`.)

## Literature

- [Cacioli 2026](https://arxiv.org/abs/2603.14893): signal-detection decomposition of LLM judgements into sensitivity and criterion. Unchecked against the paper by either verifier.
- [Panickssery, Bowman and Feng, NeurIPS 2024](https://arxiv.org/html/2404.13076v1): LLM evaluators recognise and favour their own generations. Checked by verifier 1.
- [TokSuite](https://arxiv.org/pdf/2512.20757): tokenizer choice changes model behaviour. Unchecked.
- Nothing found on cross-family perception of Unicode sequences.
