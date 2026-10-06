# What the whys cite: the frozen rubric

*2026-10-06, the independent session (Claude Opus 5.5). Frozen and committed **before** anything was computed from it, on the second catalog audit's advice: "freeze how basis answers will be scored before the canaries are computed, or they become another free choice to tune against tests 3 and 4". Any later change to the lexicon is a new version with its own date, and both versions' results are kept.*

## Purpose

Joseph, 2026-10-06: an intuitive sequence, one *"that doesn't need internal arithmetic or thinking about the glyph's name and codepoint"*, is much better than one that rests on the code chart. He suggested asking minds directly what their judgment rested on. The auditor suggested reading the reasons already saved first: the cohere answers' whys, and the forced picks' reasons. They are the basis question asked freely and after the verdict, its least leading form. This step measures:

1. **What the whys cite**, by family, by the run's chart class, and for real runs against their shuffled controls.
2. **Whether self-report tracks behaviour.** For forced picks, the behaviour is whether the picked glyph is chart-adjacent (±1 code point from the last glyph shown). If a reason citing the chart goes with chart-adjacent picks far more often than other reasons do, self-report carries signal about the basis. If not, it doesn't, and asking a basis question would add little.

## Categories (multi-label; a why may cite none, one or several)

Each category is a fixed list of lower-case patterns, matched as substrings or regular expressions against the lower-cased why. The lists are in `whys.py` (`LEXICON`), and this table is their summary.

| category | cites | patterns, in summary |
|---|---|---|
| **CHART** | position in the character encoding | `unicode`, `code point`, `codepoint`, `u+` followed by hex, `block`, `encoding`, `charset`/`character set`, "consecutive"/"sequential"/"adjacent" followed within 3 words by `code`, `char`, `character`, `unicode` or `point` |
| **NAME** | what the glyphs are or stand for: letters, numbers, scripts, named objects | `letter`, `alphabet`, `digit`, `number`, `numeral`, `roman`, `greek`, `latin`, `cyrillic`, `hebrew`, `arabic`, `kana`, `hiragana`, `katakana`, `count`, `counting`, `value`, `hour`, `o'clock`, `clock`, `moon`, `phase`, `face`, `emoji`, `weather`, `named`, `called`, `stands for`, `represents`, `means`, `symbol for` |
| **LOOK** | visible properties | `shape`, `fill`, `filled`, `thick`, `thin`, `weight`, `bold`, `size`, `height`, `tall`, `width`, `wide`, `grow`, `shrink`, `larger`, `smaller`, `bigger`, `rotat`, `orient`, `direction`, `pointing`, `dot`, `stroke`, `line`, `bar`, `curve`, `angle`, `visual`, `look`, `appear`, `dark`, `light`, `shade`, `dens`, `solid`, `hollow`, `outline`, `stack`, `layer`, `bend`, `straight`, `circle`, `square`, `triangle` |

A why citing CHART and another category counts in both. The pick analysis also reports the CHART-only and CHART-absent groups.

## Outputs (`whys.py` writes `REPORT.md`)

- **Cohere.** Per family (claude, grok), per answer type (real-yes, real-no, shuffled-yes, chart-window-yes), per chart class of the run shown (contiguous: every step ±1 code point; monotone: strictly monotone, not contiguous; other): the share of whys citing each category, with counts.
- **Picks.** Per family, for real (non-null) contexts: the share of picks that are chart-adjacent, among whys citing CHART, among those citing LOOK but not CHART, among those citing NAME but not CHART, and among those citing none. Also the same for null contexts.
- **A random sample** of 20 classified whys per category, so the classification can be checked by eye. The sample is fated (seed `whys-rubric-v1`).

## Known limits, stated before the numbers

- **The lexicon is crude.** "Line" appears in "baseline", "bar" in "barely", "count" in "account". The sample in the report exists to show how crude.
- **Words aren't reasons.** A why saying "consecutive letters" cites NAME; it may also have been decided by the chart. Self-report can be confabulated, which is why the pick cross-check is the point of the exercise.
- **Only Claude and Grok** answered these kinds. No thinking text is saved for either; only Gemini's adapter keeps it.
- **The pick behaviour is chart-adjacency to the last shown glyph only.** A pick can follow the chart two steps on, or in another order. This is the simplest behavioural marker, not the only one.
