# Proposed integration plan (suggestions, not a work order)

*The spike agent's proposals, revised 2026-10-06 ~19:30 MDT after two verifications and two strengthening rounds. The findings they rest on are in `FINDINGS.md`; the reasoning is in `strengthening-2.md` §7.*

1. **Planner: no disagreement term.** A flat split's Sonnet side is settled; its Grok side repeats about seven times in ten; a third mind is the more informative question (verifier 2 §3). Two changes with stronger support:
   - **Treat the sequence as what an answer informs.** A context's answers carry 1,500 to 2,500 nats about its sibling contexts, held out, so "how settled" belongs to sequences, not to contexts one at a time.
   - **Keep contexts of one sequence off a shared sheet**, as the probe already does for cohere and `choose`, or tag the sheet and model it. Same-sequence sheet-mates move continue answers by −0.70 logit.
2. **Catalog combination rule (§9).** Replace Abbott with a logit model with a criterion and slope per mind and kind, with shuffled controls as heterogeneous items; it wins by about 640 nats on cohere (three reproductions). Weights between minds then come from fitted slopes. For continue evidence, model each mind's reading of a sequence at the sequence level.
3. **The per-sequence quantity Joseph anticipated.** For each sequence and mind: the mind's own propensity on that sequence against the other minds' there, with its evidence count. This is the largest mind-specific structure found. Before it becomes a catalog number it needs (a) a calibrated home model (none yet passes every check), (b) seed votes and sheet composition modelled or removed, and (c) a principled unit for "the sequence" (the block set is a proxy). Alongside it, list content splits (both minds commit, differently), read off the chart.
4. **Universality** is read on content and on the sequence-level propensity, never on raw yes or stop counts.
5. **Probe design.** Tag seed-targeted questions, and keep them apart (or model them) when consistency is read: selection on seeds isn't ignorable for models that don't see the seeds.
6. **On Saturday:** Gemini questions that test `▁` outside triads.
7. **Round p002** (`prereg-third-minds.json`): the 43 flat contexts asked of Opus and both Haikus, scored by per-mind log score between three models.
