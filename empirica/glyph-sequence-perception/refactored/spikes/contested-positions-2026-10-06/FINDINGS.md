# Where is the code chart a real alternative?

*2026-10-06, the independent session (Claude Opus 5.5). Asked because the auditor's check of CATALOG v4 (`audits/catalog-design-v4-check-2026-10-06.md`, V2) found that a position where the chart's alternative is unrelated to the run tests nothing. Run from `refactored/`: `python3 spikes/contested-positions-2026-10-06/contested.py` (output in `output.txt`). Answers are one per answer ID, void-round failures dropped, and every answer touching a glyph of Joseph's canary left out.*

## Triad middles against the code-point median, by how many Unicode blocks the triple spans

| blocks in the triple | middles | departing from the code-point median |
|---|---|---|
| 1 | 10,151 | 0.13 |
| 2 | 1,305 | 0.47 |
| 3 | 290 | 0.69 |

A random middle departs 2 times in 3. Across three blocks the departures are at chance: the order of the blocks in code space says nothing to these minds. Within one block they are rare.

**Two blocks.** Blocks are contiguous ranges of code points, so in a two-block triple the code-point median always shares a block with one of the others. The triple has one pair from the same block and one lone glyph. The middles given:

| middle | share |
|---|---|
| the code-point median (keeps the same-block pair adjacent) | 0.53 |
| the other glyph of the same-block pair (keeps the pair adjacent, moves only the lone glyph) | 0.26 |
| the lone glyph (splits the same-block pair) | 0.20 |

Four answers in five keep the same-block pair adjacent. Which end the lone glyph goes to isn't at chance either (0.53 against 0.26), so the order of blocks in code space carries something. I can't tell what: block order often follows script or meaning (Latin before Greek, say), and these triples were asked because some run proposed them, so they're a selected set.

## The chart's next glyph, asked as an inhibit candidate

| | Claude | Grok | Gemini |
|---|---|---|---|
| in the same block as the glyph before it | 0.87 (1,964) | 0.84 (724) | 0.80 (56) |
| in another block | 0.70 (30) | 0.82 (11) | — |

Cross-block chart neighbours were rarely asked (41 times) and were accepted almost as often. They were asked because something proposed them, so this doesn't show that cross-block neighbours tempt minds in general. It doesn't support the block rule, and it doesn't count against it.

## What follows

The chart makes a claim minds respond to between glyphs of one block. Across blocks, its order is near chance for triads. So CATALOG v5 counts a position as **contested** only where the chart's alternative pairs glyphs of one block (§7a there): for a step, the chart's next glyph is in the same block as the glyph before it; for a triple, the departure splits a same-block pair. The order of blocks in code space is left out as evidence either way. That loses the 0.53 against 0.26 signal, whose meaning isn't known.
