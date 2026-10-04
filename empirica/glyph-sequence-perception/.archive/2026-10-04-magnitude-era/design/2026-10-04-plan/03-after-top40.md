# 03 — The top-40 material, read after my plan was written

*Written after stages 1 and 2 were committed (d09b2fdf, 77a7afed). Read for this stage:*

- *`analysis/top40.md`;*
- *`harness/top40/candidates.py` and `score.py`;*
- *`analysis/views/ordering-distances-2026-10-04.md` and `orderings.py`;*
- *the `compare-*` tables and the head of `compare.py` in the clean-room reading.*

*New numbers come from `scripts/encoding_order_check.py` (in this directory). It reads the existing v1.0 ledgers through the builder's parser p1.3, unchanged, and made no judge calls. The table of record types and per-surveyor counts came from a one-off count I ran in the shell; I did not keep that as a script.*

## My stage-1 predictions, scored

| prediction (stage 1) | outcome |
|---|---|
| The list is dominated by sequences salient to Claude-family minds | **Not confirmed as I put it.** grok-1 supports 84 of the 117 candidates, so this set is not a Claude-only consensus. What dominates is narrower: **22 of the top 40 consist entirely of glyphs with a Unicode numeric value.** They are the denoted-number families: circled, Roman, script digits, fractions, superscripts. That is a different and sharper problem (below). |
| Shared cores suppressed by the choice of variant | **Confirmed.** `▫░▒▓█` sits at #31. Only 2 of 12 frontier whole-set answers keep it intact, both from haiku. The other ten put `▫` in EXTRA and order `░▒▓█`, with every judge family represented. The core `░▒▓█` was never tested alone. `→⇒⇉⇛⇶` (rebuilt exactly in 0.25 of answers), `⬞▫◽□◻⬜` and `□▤▦◫▩■` (0.00) show the same pattern: a contested rung, chosen with the variant, drags down a sequence whose core is stable. |
| Agreement looks high | **Confirmed.** On the step score, the frontier saturates. In the whole-set task, frontier judges rebuild nearly every candidate exactly; most cells in the ordering-distance view are `0·0`. The next finding is why that number says less than it seems to. |

## The finding: whole-set reconstruction is confounded with encoding order

**90 of the 117 candidates are written in codepoint order** (ascending or descending). That follows from how the surveys were made: each surveyor walked Unicode panes in codepoint order with the `unicode-group` tool, so the runs they wrote down are mostly contiguous runs of the chart.

The gestalt prompt asks whether glyphs "belong in some order (any kind of more/less, **progression**, or motion)". A mind that knows an alphabet or a block's encoding order is answering correctly when it gives that order. So for contiguous runs, a whole-set reconstruction cannot tell magnitude from known sequence.

The sharpest test is the sequences frontier judges *will not* order pair by pair (strict step score < 0.5):

| | k | mean pairwise strict | rebuilt exactly as written |
|---|---|---|---|
| written order = codepoint order | 15 | 0.30 | **0.84** |
| written order ≠ codepoint order | 5 | 0.29 | 0.41 |

- **Rebuilt whole despite almost no pairwise "more" (all contiguous runs):**

  | sequence | strict | rebuilt exactly |
  |---|---|---|
  | Balinese vowels `ᬇᬈᬉᬊᬋᬌᬍᬎᬑᬒ` | 0.06 | 1.00 |
  | trigrams `☷☶☵☴☳☲☱☰` (as reversed codepoint order) | 0.12 | 0.92 |
  | `ℵℶℷℸ` | 0.33 | 0.92 |
  | Ogham `ᚆᚇᚈᚉᚊ` | 0.43 | 0.92 |
  | `♩♪♫♬` | 0.44 | 1.00 |

- **Where written order and codepoint order disagree and the magnitude is strong, judges follow the magnitude.** `⓪①…⑩`, `⁰¹²³…`, `⅛¼⅜½…` and `一二三…十` are rebuilt in the written order every time and in codepoint order never. So judges are not blindly sorting by codepoint. They use encoding or conventional order where magnitude is weak or absent. Where the instrument allows "progression", that is a reasonable answer to give.

**What this does to the record.** The pilot's "holistic" signature is "pairwise ⟂, recovered from the whole set". It now has a simpler competitor: *known ordinal sequence, no felt magnitude*. The two are confounded for any contiguous run.

- **Where the competitor fails: `-=>})|` and the risebar.** Neither is a codepoint run, and neither is a conventional sequence. They remain the real holistic candidates.
- **Ogham is a mixed case.** The rungs are visibly 1–5 strokes, and the run is also contiguous and alphabetic. The current data cannot split it.

This is the codepoint-proximity concern from stage 1, item "Hazards", in a stronger form than I had guessed. The fix is a 2 × 2 that existing stimuli do not fill:

| | contiguous run | codepoint-scattered |
|---|---|---|
| **magnitude ladder** | many | few |
| **non-magnitude ordinal run** (alphabets, syllabaries) | some | rare |

Both missing cells need stimuli. The non-magnitude cells need ordinal runs with no magnitude reading: six consecutive Cherokee letters, Yi syllables, or the Balinese vowels again. The scattered magnitude cell needs more ladders whose codepoints scatter. These are exactly the specimens Joseph asked surveyors for on 08-25 ("I would love magnitude sequences … that have scattered codepoints").

A third variant is cheap and directly diagnostic: **present contiguous runs with one glyph swapped for its nearest off-run lookalike.** Encoding knowledge breaks on the swap; a felt axis does not.

## Why the top-40 is not a principled answer to its own question

In order of how much each matters, as I judge it:

1. **The rank measures decodability.**
   - **What tops it.** Over half of the top 40 is denoted number. Recoverable pairwise order is what the score ranks, and numerals are maximally recoverable.
   - **What is missing.** The study's own second axis. Joseph's mid-survey note on 08-25 was that digits are among the *weaker* magnitude glyphs, because the order has to be looked up rather than seen. Immediacy is not in the ranking at all.
   - **The result.** A list where "names more" outranks "shows more". `○◔◑◕●` is at #43 and `▫░▒▓█` at #31, both below `٠١٢٣٤٥٦٧٨٩`.
2. **The candidate rule decides what can be found.**
   - Only `sequence` records of 3–12 glyphs are eligible.
   - Batch b needs support from ≥ 2 surveyors.
   - Any record containing `≈` is dropped.
   - Greedy suppression at Jaccard ≥ 0.34, longest record winning ties.

   Together these exclude, by construction:
   - all 27 morph records (Grok's hinge `•o⊃)}|{(⊂o•`, Joseph's unfold);
   - the 13 generator records (braille and sextant lattices) as lattices;
   - the 207 negatives, the 12 questions and the 11 cyclic records;
   - almost every single-surveyor find;
   - `-∼≈≋`.

   The axis-less, holistic side of the study, which Joseph treated as central, cannot appear in the list.
3. **Only the author's adjacent steps are tested.** Each surveyor's linearization is presupposed. An alternative order, or a rung that belongs elsewhere, can only show up as a failed step, never as a found order. The elab-n case makes this concrete: the judges agree on `nɳɲŋ`, the step score puts the sequence last, and the view ranks it 117th of 117.
4. **No baseline and no format variation.**
   - It is single-format: ⟂ and ≈ are always available.
   - There is one presentation per order and only 2 shuffles.
   - Nothing compares it with matched noise sets, nor with the encoding-order control above.
5. **Short ladders reach 1.00 more easily.** Six of the top ten have 3–4 rungs. Direction was also chosen post hoc per judge in the builder's score; the coordinator's view later fixed it per sequence.
6. **The panel and its weighting.** There are six frontier judges (3 Anthropic, 2 Google, 1 xAI). Small models enter only through answer channels dominated by slot preference.

**What the material is still good for.** The data are honest and reusable.

- **As discovery-tier measurement:** 117 survey loci, measured by six frontier minds, both orders, plus whole-set answers.
- **As a selection guide:** the contested rungs it exposes are good targets for repetitions in the next round.
- **As evidence of selection bias:** the 77% contiguity rate is itself a measurement of what pane-walking surveys select.

## How stages 1 and 2 change

- **Gestalt cannot be the set-level gate on its own.** Every locus needs the encoding-order control (the swap variant, or a scattered presentation) before a whole-set success counts as magnitude. "Holistic" is claimed only where the order survives that control and is not a known conventional sequence.
- **The channel test (stage 1) is messier than I wrote.** Unicode names often state the amount outright (`LOWER ONE EIGHTH BLOCK`). A rendered image of `⑤` can be read as text and then decoded. So the name channel and the clean-image channel each mix routes. The informative channel is a **degraded image**: blurred or low-resolution until identity is unreadable but mass remains. Order that survives degradation is carried by mass. Denoted order dies there. That is the closest operational form of Joseph's "the glyph *shows* more" against "the glyph *names* more" that I can see for a mind with vision. For the text-token channel itself, immediacy still needs the pilot's indirect evidence: small-model logit readouts, conflict arbitration, and gaps between low and high effort.
- **Intake from the surveys is all 849 sequence records, plus the record types the top-40 rule never touched.** Negatives become controls. Questions become battery items. Generators are measured *as lattices*: chains sampled from them, and whether minds find any chain at all. Morphs and cyclic records go to the whole-set and continuation instruments, which are the only ones that can see them. A small data-hygiene note for whoever builds intake: the sonnet-survey-3 extraction labels its surveyor `sonnet-3` instead of the ratified file-basename form.
- **A "top" list becomes a family of views, each answering one question.** Examples: the most universal links across minds and contexts; ladders that survive image degradation, which is the immediacy view; sequences with order in sets but not pairs that survive the encoding control, which are the holistic candidates; and sequences where minds agree with one another against their author. A single rank would recombine those questions under weights nobody chose.
