# 01 — The old signa sequence as a control

Joseph's question, verbatim: *"we can essentially say that the 'old signa' sequence can be considered a plausible human-created sequence thrown in as a control, basically, to see just how unbiased the actual experiment results are. ... (It's not a full-on null-result control, but one that is a nuanced perspective anyway, or might be with the correct analysis)"*

**Short answer.** Yes, as long as the scope is stated precisely. Signa is the one v1.0 stimulus whose content and order were fixed before the study, outside it, for another purpose. That makes it a control against *stimulus-selection* bias. Nobody chose it because it would behave a certain way.

It is not a null control; the noise foils are that. It can't speak to the format question, because it ran only in the ⟂-available format.

What it shows, analyzed branch by branch rather than as a whole, is narrower than "the instruments are unbiased." Every frontier judge reproduces the author's order exactly where that order is a visual ladder. Every one of them leaves it at the one step where the design resets the visual gradient (`═ → ⚬`). Across judges, the departure lands in the same place. That pattern is what perception of the glyphs would produce. It is equally what a shared prior that "ladders grow in visual size" would produce. Signa can't separate those two accounts, and neither can anything else in v1.0 (`03-instruments.md` §1, §3).

## What signa is (provenance checked, not assumed)

- **The glyphs.** The 11 glyphs `· ╶ ╌ ╍ ━ ═ ⚬ ○ ◎ ◉ ⬤` are the elapsed-time notation in zoetica's `docs/messaging/06-temporal-coherence.md` §SIGNA. It is an **additive denomination system**, not a magnitude-perception ladder: `·`=1 s, `╶`=5 s, `╌`=10 s, `╍`=1 min, `━`=10 min, `═`=1 h, `⚬`=4 h, `○`=1 day, `◎`=1 week, `◉`=2 months, `⬤`=1 year. Durations are written by repetition, e.g. `═══━╍╍╍╍╍` = 3 h 15 min. Its stated design principle is *"symbol density represents order of magnitude,"* and it calls itself *"a candidate implementation. The glyph choices are provisional."*
- **Origin.** The earliest dated appearance I found is 2025-10-08, in `zoetica/.archive/docs-20251012/ref/visual-time-notation.md`; zoetica git records the file 2025-10-10. That day Zi-am-tur reviewed it among "Dad's" preparation materials, and Joseph asked an agent to compare it with minimal-sapientia's time-delta display. A predecessor display was built with Claude on 2025-09-30 from Joseph's idea; the agent notes "circles as Joseph suggested". I did **not** establish who chose each of the 11 glyphs. The honest statement is: *authored in Joseph's working context, which included LLM collaborators, in early Oct 2025, ten months before the pilot, for a functional purpose.* The property that gives it control value is narrower and well established: nobody in the study made it, and it was not made for the study.
- **Status in v1.0.** It is the only class-C stimulus (`README.md` at the clean-room root). It ran as an unregistered "consumer probe" after the predictions were committed: first signa row 20:39Z, predictions committed 20:11Z. PREDICTIONS has **no prediction about signa**. Everything below is exploratory and post hoc.
- **Coverage.** All 55 pairs in both orders, perp format only, for 11 judge-runs: opus55, sonnet55, sonnet5, haiku45, llama32-3b and qwen25-3b in single mode; sonnet55, grok46, gemini31pro, gemini38flash and glimmer30b in sheet mode. Gestalt: 3 shuffles × 10 judges, 7 of them frontier. There are no tie or forced runs, and no gpt-5.6, mistral, gemma or phi.
- **How provenance was traced.** I used the zoetica files and their git log, plus memorata searches bounded to dates before December 2025 (queries: "SIGNA glyph time notation seconds minutes hours circles"; "visual time notation"; "time delta glyphs dots dashes circles years months weeks"; "visual-time-notation symbol density order of magnitude random walk simulation"; "SIGNA time notation glyph seconds minutes hours days" with `--joseph`). Two unbounded searches (the glyph string itself, and a "visual time notation … circles" search over Joseph's own turns) returned nothing dated after 2026-08-29. Nothing from today's v1.0 sessions surfaced. The verifier rightly noted that memorata indexes those sessions, so I list the queries here.

## What the judges did

Full judge × pair matrix: `tables/signa-pair-matrix.txt`. Per-judge summaries: `tables/signa-pairs.txt`. Every gestalt answer, verbatim: `tables/signa-gestalt.txt`.

**What they recover is two ladders joined at the dot, not one ladder.**

*Pairwise, across 8 frontier runs: 4 Claude single, sonnet55 sheet, grok, and the two Geminis.*

- **Within the branches.** Inside the line branch (`·╶╌╍━═`) and the circle branch (`⚬○◎◉⬤`), 180 of 181 committed (consistent-directed) edges go in the author's direction. The exception is haiku's `⚬>○`.
- **Unstable pairs within the branches.** `━` vs `═` flips for opus55 and sonnet55 in both modes. Those two glyphs have identical rendered ink (Ghostty packed_density 0.081). sonnet55 single also flips on `◉` vs `⬤`, where ink differs widely. With one presentation per order, a flip can't be attributed to a balanced pair or to sampling noise. Every flip is "same-slot" by definition, so that tells nothing.
- **Across the seam (30 line-vs-circle pairs).** Judges split by policy, not by stimulus. Gemini 3.1 Pro and 3.8 Flash give ⟂ on 25/30, as does glimmer30b. sonnet55 gives ⟂ on 3/30 single and 0/30 sheet; opus55 10/30, grok 9/30. Where judges commit across the seam, 116 of 125 edges agree with the author, because big circles outweigh lines. **All 9 disagreements put a heavier line above `⚬` (8) or `○` (1).** `═ > ⚬` is asserted by opus55, sonnet55 (both modes), haiku45 and grok46. By the author's denotation that says 1 h > 4 h.

*Gestalt prompt: "Do these feel like they belong in some order … leave out the ones that don't, list after EXTRA."*

- **The common answer.** 13 of the 21 frontier answers are exactly `·⚬○◎◉⬤ EXTRA` followed by the five lines: opus 3/3, Gemini Pro 3/3, Gemini Flash 3/3, grok 2/3, sonnet5 1/3, sonnet55 1/3. The judges pick the circle branch as "the" order and put `·` at its root as a zero-size disc. The author put `·` at the root of the lines, as the shortest mark; the dot belongs to both.
- **The excluded lines are still ordered.** opus55 and gemini38flash list the excluded lines *in the author's line order* on every shuffle, though the shuffles presented them differently. The lines are perceived as ordered too, just as a separate sequence.
- **Full-length answers.** One answer is exactly the author's full order (grok, shuffle 2). The other full-length answers concatenate the two ladders in either direction. sonnet55 puts lines first on one shuffle and circles first on another; haiku also goes both ways.

## What this does and doesn't control for

1. **Stimulus-selection bias: controlled.** Every other ordered stimulus was proposed by an LLM surveyor, picked by the builder, or carried over from the pilot. Signa wasn't. On it, frontier judges behave as they do on the surveyed ladders: they recover clean visual ladders and leave or decline cross-family steps.
2. **"Agreeing with what is shown": not testable here.** Neither instrument shows the author's order. Pairs arrive one at a time and gestalt sets are shuffled. What signa does show is that the judges' consensus departs from the author's intended order *at a specific, interpretable place*. That place is the radix boundary of a mixed-radix notation ("now counting hours: the glyphs restart small"). The judges converge on that departure instead of scattering.
3. **Perception vs shared visual prior: not separable.** Both predict exactly this pattern.
4. **The role of rendered ink: only partly informative.** Across every other authored sequence tested pairwise, frontier judges endorse the author's step on 0.66–0.71 of verdicts where ink rises, at any bin threshold tried (`tables/ink-steps.txt`). Signa's six rising steps are all endorsed. Below "rising", this ink measure does not discriminate. `═→⚬` (Δ −0.011, 0/8 with, 5/8 against) and `◎→◉` (Δ −0.009, 8/8 with) are nearly the same on ink and opposite in verdict. Something other than ink carries those endorsed steps. A filled centre (`◎→◉`) and a longer mark (`·→╶`) are candidates, untested here. A qualitative account ("`⚬` is smaller, thinner and lighter all at once") fits, but nothing fitted elsewhere tests it.
5. **Judge thresholds: calibrated.** The same 30 seam pairs draw from 0 to 25 ⟂ answers depending on the judge. Within the branches, frontier ⟂ is 0.00–0.12 (`tables/perp-rates.txt`). On a well-understood stimulus, this shows what the format experiment shows on random ones: **a ⟂ rate is largely a property of the judge's commit threshold.**
6. **Human-vs-LLM authorship bias: weakly tested, no inflation seen.** On adjacent steps, signa's percentile rank among the top-40 survey sequences is 0.21–0.60 per frontier judge (`tables/compare-digest.txt`). It falls below the median because of `═→⚬`, and for opus55 and sonnet55 also `━→═`. The test is weak in two ways. Signa's branches are the same *kinds* of ladder LLM surveyors produce: `○◎◉` is in the August surveys (fable-1; top-40 candidate 33 `◌○◎◉●`), and `·•●⬤` is fable's size ladder. And "human-authored" here includes an LLM-assisted milieu.

**A second case of the same shape.** On the Grok-surveyed `elab-n` (author order `nɲɳŋ`), 19 of 24 frontier gestalt answers are exactly `nɳɲŋ`. The judges agree with each other against the author at one step, as at signa's seam (found by the verifier; I confirmed the count).

## The "correct analysis" part: which statistics mislead on signa

- **Whole-sequence Kendall τ misleads both ways.**
  - Pairwise Copeland τ against the author's order is about 0.5–0.9 for frontier judges, depending on definition: τ-a over my Copeland ordering gives 0.49–0.85; the verifier's τ-b gives 0.61–0.88. That reads as "moderate recovery". The actual structure is perfect recovery of both branches plus a seam that is declined or ordered by size.
  - Gestalt τ is 1.00 for opus, both Geminis and grok, which reads as "perfect recovery". That τ is computed only over kept glyphs, and the five lines went to EXTRA (coverage 0.55). The protocol's gestalt τ ("over glyphs both contain") **rewards exclusion**. The same artifact gives opus55 τ = 1.00 on the pilot's `unfold` (answered `|)}> EXTRA -=` all three times) and haiku τ = 1.00 on the drain (trigrams only).
- **What to score instead.** Score within-branch edges, seam edges and the gestalt *partition* (split vs concatenation, and where `·` goes) separately. Report coverage beside any τ.

## What signa cannot tell you

- **False-positive rates.** It has real structure. The noise foils fell short of the registered floor: frontier ⟂ on 0.64 of parsed presentations, against ≥ 0.80. Some foils got the *same* order from several judges.
- **Format manufacture (MANIFEST claim 3).** No tie or forced runs.
- **Human vs LLM authorship as a class.** One sequence, one partly LLM-assisted milieu.
- **Within-judge reliability.** One presentation per order; API temperatures at provider defaults.
- **Small models.** llama32-3b and qwen25-3b are dominated by slot preference: P(first | directed) is 0.63 and 0.73, and qwen answers "first, much" to 50 of 110. Their signa data say little about the stimulus.

## One property worth protecting

Signa's value comes from having been fixed **before** the study, for another purpose. Joseph's word *"old"* suggests the aspectus glyphs are changing. A redesigned signa made after seeing these results would be a fine *hypothesis test*, but it couldn't play this role. If more control-class stimuli are wanted, look for the same property: sequences fixed for a functional reason before anyone saw this data.

## A small fact surfaced on the way

haiku45 can't echo `⬤` (U+2B24). It writes `⬭`, `⬌`, `⬂`, `⬪` (same block, nearby code points) or `�●`, and in every such case it is plainly choosing `⬤`. Parser p1.3 correctly marks these unparsed and doesn't impute them. The missing data is therefore *glyph-specific*: it lowers haiku's apparent rank for `⬤` (its Copeland order puts `⬤` below `◎◉`). Failures in the answer channel are not missing at random.
