# Family disagreement: findings

*The spike agent's findings, 2026-10-06 (Claude Opus 5.5), landed unchanged by the coordinating session from the agent's final report: the harness refused the agent's own write of this file. All numbers come from one snapshot of the answers taken at 16:36. The working log is `NOTES.md`, including the readings withdrawn along the way; the map written before any computing is `MAP.md`. Not yet independently verified.*

## Findings

**1. Where frontier minds commit, they agree on the content.**
- **Continue:** when two minds both continue a context, they write the same glyph 93–99% of the time, across families as much as within. Sonnet–Grok 0.940, Opus–Grok 0.954, Sonnet–Opus 0.957, Opus–Gemini Pro 0.987. Haiku without thinking is the exception, at 0.82–0.87.
- **Triads:** when both name a middle, it's the same middle 92–97% of the time.
- **Splits that repeat:** Sonnet and Grok each answered unanimously but differently in 9 of 870 contexts (1.0%). That's fewer than within Claude: Sonnet against Haiku without thinking, 4.0%.
- **At family level** (three or more answers per family): one content split in 467 questions, `■▤▦`.

**2. Most disagreement is about whether to commit, and that belongs to a mind and a question kind, not a family.** Commit means continue rather than stop, name a middle rather than "only two", or say yes.
- **Continue:** 74–90% of pairwise disagreements are about whether to continue at all.
- **Threshold model:** each mind gets one threshold, and each context one shared strength, estimated only from the other minds' answers. That model predicts every flat Sonnet-continues / Grok-stops split: 43 observed, 51 predicted (95% band 38–65).
- **The thresholds don't line up by family.** Grok stops most readily in continuation but is the most lenient on "is this coherent?". Gemini Flash is the readiest of all minds to name a triad middle; Gemini Pro is the least ready. Inhibit, the plain yes/no next-glyph question, shows almost no spread.
- **Gapped triads:** whether a gapped run like `③④⑦` "goes together" splits by mind, from Gemini Flash at 0.82 down to Grok at 0.46. Whenever any mind does name a middle, it's the code-point median 0.87–0.96 of the time.

**3. A few effects really are family-shaped, and each has a nameable basis.**
- **`▁` for both Gemini minds.** It's z = −19 for Flash and −3.9 for Pro. Nothing else among 2,388 glyph × mind cells comes close; the other ramp glyphs that looked affected were spillover from triads containing `▁`.
- **Claude's core minds favour code-point-contiguous whole runs** beyond what the other minds' recognition predicts. The logit offsets are Sonnet +3.1, Haiku without thinking +2.3, Opus +1.7, Grok +0.8, Gemini Flash +0.4. Two explanations fit and I couldn't separate them: leaning on the chart, or models favouring runs they wrote themselves (a known effect).
- **The behavioural chart test the whys spike asked for.** At contested `choose` positions (unsealed only), on the same 446 positions, Sonnet picks the chart's glyph 0.536 of the time and Grok 0.470, about three standard errors apart. Against its own controls, context moves Sonnet toward the chart; Grok, Gemini Flash and Opus move away. So the tilt is Sonnet's rather than Claude's, and it is much smaller than the two-to-one gap in what their reasons say.
- **Small differences of form or convention.** `億` against `亿`, `⑽` against `⑩`, styled `𝞦` against plain `Χ`, and whether the tarot knight belongs in the suit. Tested across all such contexts, every mind keeps the glyph's form 0.94–0.975 of the time, so form isn't the main axis.

**4. Family is a weak axis.** Sonnet and Opus are indistinguishable on continuation once noise is removed (D ≈ 0). Otherwise the odd one out on a task is a single mind: Sonnet on whole-run coherence, Grok on stopping, Gemini Flash on triads, Haiku without thinking on noise.

**5. A correction to the catalog's method.** The catalog's Abbott correction assumes a different response model from a logit threshold, so a plain difference in strictness shows up as a difference by chart class. That's how my first table made Sonnet look specifically weak on non-monotone runs. On the logit scale, the minds' slopes are nearly equal (0.82–1.16).

**Withdrawn along the way:**
- "Grok refuses chart walks through unfamiliar blocks." Across all contexts, Grok stops *less* where Sonnet's continuation is the chart's next glyph.
- The Abbott-based "Sonnet leans on the chart" reading, replaced as in point 5.

**Still open:**
- Self-preference against chart reliance, untestable on current data.
- `▁` tested outside triads: Gemini has no answers there, and it's paused until Saturday.
- Everything about Gemini on cohere and inhibit, where its data is thin.
- Triad repeats are correlated, which inflates the triad split counts.

## Literature

- [Cacioli 2026](https://arxiv.org/abs/2603.14893) applies signal-detection theory to LLMs: sensitivity and response bias separate, as here.
- [Panickssery, Bowman and Feng, NeurIPS 2024](https://arxiv.org/html/2404.13076v1) show models recognise and favour their own outputs, the confound I couldn't test.
- [TokSuite](https://arxiv.org/pdf/2512.20757) measures tokenizer effects on behaviour.
- I found nothing on cross-family perception of Unicode sequences.
