# What the whys cite: findings

*2026-10-06, the independent session (Claude Opus 5.5). Read with `REPORT.md` (generated) under the rubric frozen in `RUBRIC.md` (lexicon `whys-rubric-v1`, committed before computing). Only Claude and Grok answer these kinds. Data: answers through c092–c093.*

## The classification, checked by eye

From the 20 fated samples per category in `REPORT.md`:

- **CHART: about 17 of 20 genuinely cite code points.** For example: "descends by one Unicode codepoint each step (33BE→33BD→…)", "U+1D376 down to U+1D372", "Consecutive Unicode codepoints in ascending order". The misses come from `\bblock` matching visual uses ("a solid braille block", "angular and blocky").
- **NAME: mostly right.** It also catches whys that name a Unicode block ("Spacing Modifier Letters block"); those count as CHART too, since the categories are multi-label.
- **LOOK: noisy, about 6 of 20 false.** "Look like an arbitrary mix", "*square*d Latin letters", "*appear* randomized". LOOK shares are an upper bound and shouldn't be read finely.

## 1. Self-report tracks behaviour

For forced picks at real contexts, here is the share where the picked glyph is ±1 code point from the last glyph shown, by what the reason cites:

| why cites | Claude | Grok |
|---|---|---|
| CHART | 0.56 (1,702) | 0.68 (163) |
| NAME, not CHART | 0.29 (817) | 0.22 (73) |
| LOOK, not CHART | 0.19 (2,468) | 0.15 (353) |
| none | 0.23 (1,118) | 0.16 (199) |

A reason citing the chart goes with a chart-adjacent pick two to four times as often as any other reason, in both families. At null contexts (random glyphs, where there is no run to continue) the CHART group is not more chart-adjacent: Claude 0.08 against 0.07–0.16. So the association belongs to real runs, as it should if the reasons report the basis.

**So a basis answer carries real signal about what a judgement rested on.** It isn't perfect: 44% of Claude's chart-citing picks weren't chart-adjacent, and some chart-adjacent picks cite only names. But it is evidence. Asking for it directly (Joseph's basis question) is worth a condition, and it can be validated against discriminator positions once those exist (CATALOG version 3).

## 2. Claude cites the chart about twice as often as Grok

Share of "yes, coherent" whys that cite the chart:

| run shown | Claude | Grok |
|---|---|---|
| real, contiguous code points | 0.38 (1,607) | 0.18 (610) |
| real, monotone | 0.22 (741) | 0.10 (347) |
| real, other | 0.09 (1,408) | 0.08 (665) |
| chart window | 0.41 (1,052) | 0.20 (405) |

On runs that walk the chart, Claude's reasons rest on the chart about twice as often as Grok's. On runs that don't, the two families are alike. This bears on Joseph's concern that the roster's Claude majority pulls the study toward "just do it like the codepoints had it". It also bears on the v2 audit's A3, which judged the question unsettled from the unassigned-code-point marker alone. On the whys, Claude is the more chart-reading family, wherever the run allows it.

## Not done here

- **No thinking text is saved** for Claude or Grok, only for Gemini through agy. A record of the reasoning would be stronger than a report about it. Capturing it is an adapter change.
- **Gemini** has answered none of these kinds yet.
- **Images.** The v2 auditor proposed showing glyphs as rendered images, so that the chart is removed by construction. Joseph, 2026-10-06: *"Image presentation isn't going to be applicable for our needs. It's an interesting image-perception-capability question that is completely orthogonal to the unicode-token-perception issue we are studying."* Out of scope.
