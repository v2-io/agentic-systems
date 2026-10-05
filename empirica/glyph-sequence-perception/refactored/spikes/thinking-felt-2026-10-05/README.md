# Felt vs reasoned: Claude with thinking off (2026-10-05)

*A small probe by the independent session (Claude Opus 5.5), run before c002. Code: `probe.py`. Raw answers, verbatim: `raw/`. Numbers: `report.md`. Not independently verified.*

## Why

Joseph, 2026-10-05: the study's goal is *"the truth about viable 'felt-like' character sequences, which will be used … to build signa to help models better perceive certain information channels instead of numbers that require reasoned arithmetic"*. He added a caveat: *"it will sometimes take quite a bit of reasoning to discover the candidate sequences/branches/etc. that can be felt without much reasoning"*, which he likened to *"recognition vs retrieval"*. The minds deliberate very differently. Median thinking tokens per sheet in c001:

| mind | thinking tokens |
|---|---|
| Gemini Flash | 0 |
| Opus | ~260 |
| Sonnet | ~500 |
| Grok | ~900 |
| Gemini Pro | ~2,400 |
| Haiku | ~5,100 |

And the Claude judges were inheriting `MAX_THINKING_TOKENS=31000` from Joseph's shell. That was unrecorded, and almost certainly true of the whole triad era as well.

## What was done

- 30 c001 sheets (102 items), fated sample, prompts verbatim.
- sonnet55 and haiku45 asked twice with `MAX_THINKING_TOKENS=0` (**off**) and once more with 31000 (**on**).
- Compared with each other and with the original c001 answer (on #0). The measure is the first glyph written, or "none".

## What was found [measured; n = 102 items, one sample of sheets]

**Sonnet 5.5 is not reached by this lever.** It thought a median 618 tokens with the budget at 0 and 613 at 31000. So its "off" is not off, and its agreements (0.96–0.99) are effectively on against on. No CLI flag found turns Sonnet's thinking off; `--effort` bottoms out at `low`. Grok's bottoms out at `low` too (`none` and `minimal` are rejected).

**Haiku is reached** (0 thinking tokens; 2.4 s against 56 s), **and thinking changes its answers beyond its own noise:**

| comparison | same first answer |
|---|---|
| on vs on (c001 vs retest) | 0.83 |
| off vs off (retest) | 0.88 |
| on vs off (two pairings) | 0.69, 0.74 |

**Thinking does not make Haiku more chart-bound.** The share of first glyphs that are the ±1 code point is 0.96 on and 0.94 off. "None" is 0.23 on and 0.24 off.

**The differences run both ways, and they show what each condition is good for** [observed]:
- Without thinking, Haiku sometimes continues where thinking stopped: `㏠ ㏡ → ㏢`, `🃳 🃲 🃱 → 🃰`, `🔉 🔊 → 🔈`.
- Without thinking, it also drops obvious runs (`Q R → none`, `八 九 → none`, `t s → none`) and slips (`⑼ ⑽ ⑾ ⑿ → ⑽`, `⑧ … ① → ⑨`). That is a small model being terse or careless, not evidence that a sequence isn't felt.

## Reading [inference]

Thinking-off Haiku is closer to recognition, and it is a noisier instrument. For signa, the evidence that matters is a link that survives both conditions, and that holds across families whose deliberation differs. Gemini Flash (0 thinking) and Grok (~900) bracket it. No single condition is the truth.

## What changed because of it (c002 on)

- **Thinking budgets are set per mind** in `core/minds.json` and recorded in every ledger row: 31000 for sonnet55, opus55 and haiku45, continuing the condition of all earlier data.
- **`haiku45nt` (budget 0) is core; `haiku45` (budget 31000) is a second mind (share 0.2).** Every sheet gets a recognition-condition Claude answer at ~1/50th of Haiku's former cost, and the reasoned condition stays sampled, so the switch can be measured. This was the independent session's call while Joseph was away. It is reversible in `minds.json`.

## Not done

- **A Sonnet off condition:** no lever found.
- **More sheets, and Opus.**
- **Tree-level analysis:** which links survive both conditions, per family. That wants the tree's machinery and more c002+ data.
