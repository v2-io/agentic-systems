# Map: what the study knows about family differences, where it is in tension, and what this spike adds

*2026-10-06 ~16:40 MDT, the family-disagreement spike (Claude Opus 5.5), written after reading METHODOLOGY, CATALOG, HANDOFF, MANIFEST, OBSERVATIONS, the SEAL, the planner audit, the whys-basis, contested-positions and reasoned-pass spikes, the embedding verifier's report, `core/minds.json`, and the catalog's `rates` table, and before computing anything about disagreement. Labels: **[read]** what a study document says (with its own tier); **[seen]** what I saw in the data or the catalog while orienting; **[guess]** my expectation, written down so it can be wrong.*

## 1. What the study already knows that bears on families

**The roster is uneven by construction** [read, `core/minds.json`]. Claude has two core minds (`sonnet55`, `haiku45nt`) and three thinking-condition variants; Grok has one core mind; Gemini has one core and one second mind. "Family" is the study's unit of universality, but the families differ in how many minds and which deliberation conditions they contribute.

**Coverage is uneven and not random** [read, HANDOFF; seen]. In the context-tree era (sealed answers and failed calls removed), Claude gave 56,628 continue answers, Grok 21,467, Gemini 5,163; for cohere 16,174 / 7,054 / 1,985; Gemini answered no ctx-era triads at all. Grok and Gemini drain newest rounds first and new kinds first, so the questions they answered are a selected subset. Gemini is paused until Saturday.

**Base rates differ, and the family label hides a split inside Claude** [read: BEST.md says Grok 0.39, Claude 0.21 on shuffles; seen in `catalog.rates`]. The shuffled-control "yes" rate per rater, by set class (contiguous / other): Sonnet 0.05 / 0.15, Opus 0.04 / 0.16, Haiku with thinking 0.12 / 0.25, **Haiku without thinking 0.29 / 0.37**, Grok 0.37 / 0.47, Gemini Flash 0.15 / 0.33, Gemini Pro 0.26 / 0.27. Haiku-without-thinking sits nearer Grok than Sonnet. So at least part of what reads as a Claude–Grok difference may be a difference between minds or deliberation conditions that happens to align with families because of who is on the roster.

**What families say differs** [read, whys-basis spike]: Claude's reasons cite code points about twice Grok's on chart-walking runs (0.38 against 0.18), the same on runs that don't walk the chart. That spike named the behavioural test that would show whether the judgements also *rest* on the chart differently: compare families at discriminator positions (`choose`). Those answers now exist (c095 on), and the unsealed ones are usable.

**One clean family-specific perceptual case** [read, OBSERVATIONS, supported observation]: both Gemini minds decline to place `▁` (U+2581) on the block-fill ramp (`▁▂` agreement 0/18 Flash, 3/18 Pro against 13–15/18 elsewhere), consistent with the SentencePiece word-boundary metasymbol. Mechanism unverified. The byte-level-BPE contrast was inconclusive and no byte-level family is on the roster.

**Chart-following has a family texture** [read, the embedding verifier, small n]: where alphabet and chart disagree, every family puts the alphabet first; the chart glyph appears as runner-up for Claude and Gemini, never for Grok. The unassigned-code-point marker per 1,000 continuations: Haiku-thinking 35, Gemini Pro 21, Gemini Flash 15, Sonnet 9, Grok 8, Opus 0 (METHODOLOGY §4). Note the order is by mind, and Claude's minds span the whole range.

**Thinking changes answers within one model** [read, thinking-felt spike]: Haiku on vs off agree 0.69–0.74 against 0.83–0.88 within either condition, changed in both directions, not toward the chart.

**The catalog combines families** [read, CATALOG §9]: weighted by discrimination on R's "other" class (Claude 0.31, Grok 0.26), raters within a family precision-weighted. BEST.md once used equal family weights; Joseph: equal weighting *"was never a goal so much as a choice given no other understanding."* The catalog stores per-family parts (`r_families`, `o_families`) [seen].

**The planner barely registers disagreement** [read, planner audit finding 3]: $I(k,n)$ is close to $1/(2(n+2))$ whatever the agreement, and families that disagree flatly weigh the same as families that agree.

## 2. Live tensions

1. **"Family" may not be the axis the disagreement lives on.** The control rates above suggest some of it lives on minds or deliberation conditions. If within-family spread is as large as between-family spread, "model-sensitive" would mean "mind-sensitive", and family as the unit of universality would need restating.
2. **Disagreement conflates things that call for different responses.** Sampling noise (more answers clarify it), response bias (a family says yes more: the controls absorb it), and stable perceptual difference (more answers make it *more* certain, and clarify nothing further). Only the last is a model-sensitive sequence in the sense Joseph means. The planner's question ("should disagreement weigh?") depends on which kind dominates.
3. **What families say versus what they do.** The whys show a two-to-one gap in chart citation. Whether the behaviour shows it too is unmeasured.
4. **Paired versus pooled.** Families answered different questions. Any comparison of raw family rates mixes item difficulty with family behaviour. The answers are paired by `qid` (the same question on the same sheet goes to each mind), so a within-question comparison is available and avoids the selection.
5. **CATALOG §9's family weights rest on R's "other" class.** If the disagreement turns out to be concentrated by sequence kind, a single weight per family may misstate it.
6. **Universality claims are mostly Claude-and-Grok claims.** Gemini answered few of the kinds where recognition is decided, and none since 16:08.

## 3. What this spike adds, as I see it now

- **A decomposition of disagreement**, per question kind, on paired questions: same mind re-asked (noise floor) against two minds of one family against two families. That says whether "family" is a real axis and how large it is beyond noise.
- **Disagreement that survives the noise floor, located**: which sequences, glyphs and question kinds carry it, and whether it is calibration (levels) or discrimination (ranking).
- **The behavioural chart test** the whys spike asked for, at unsealed `choose` positions, per family and per mind.
- **A scan for family-specific glyphs** like `▁`: glyphs where one family's answers depart from the others' far beyond noise, then tested out of sample.
- **What it means for the planner and the catalog**, from the above.

[guess] I expect the decomposition to show that most raw "family" disagreement on yes/no questions is calibration plus a mind-level deliberation axis, that the families agree closely on *which* runs are better than others, and that genuine family-specific perception exists but is concentrated in a small set of glyphs tied to tokenization or to rendering conventions. I may well be wrong, and the structure of this file is set so that the data can say so.
