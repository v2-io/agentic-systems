# The reasoned pass: what its answers contain, and what they're evidence of

*2026-10-06, the independent session (Claude Opus 5.5). Joseph: "don't decide how to adjudicate them or what information they actually give us until you've actually looked at a representative body of them. Then do the right thing. For all you know they make predictions on intuitiveness (or lack thereof) etc." This file is that look, and the decision that follows from it. Data: rounds through c094.*

## What there is

- **1,800 records** from `sonnet55r` (Sonnet with thinking, prompted to reason, with utf-mcp's read-only lookup tools). By outcome: 1,040 failed calls (nearly all from the void rounds), 388 "none", 364 continuations, 8 other.
- **Where it was asked.** At the felt ends of the best-ranked sequences, where first-impression answers say "none" (METHODOLOGY §4).
- **What a record holds.** The continuation, and the ledger's log of its tool calls. No written reasoning: the prompt asks for JSON only, and Claude's thinking text isn't saved.
- **Lookups.** 117 of 274 answered sheets made real lookups (212 calls): 186 `range` (list the characters in a code-point range), 22 `identify`, 2 `blocks`, 2 `search`. The rest of the logged events are protocol messages from the MCP handshake.

A fated sample of 40 answers was read by eye (`reasoned-sample` seed).

## What it shows

**1. Its continuations are chart walks.**

- **The first glyph.** 287 of 364 continuations (79%) begin with the ±1 code-point neighbour, usually followed by 12 glyphs on from there.
- **Meaning is ignored.** They cross into the next block regardless:
  - chess `♖ ♕ ♔` → zodiac `♓ ♒ ♑ …`;
  - quadrant blocks `▘ ▗ ▖` → `▕ ▔ ▓ ▒ ░ …`;
  - circled numerals `㊃ … ㊉` → `㊊ ㊋ …`, the circled ideographs for the days of the week.
- **The lookups go with the walks.** These lookups are actions recorded before the answer, not explanations written after it.

  | sheet | chart-adjacent | other continuation | "none" |
  |---|---|---|---|
  | with a `range` lookup (308 answers) | 0.50 | 0.10 | 0.40 |
  | without (444 answers) | 0.30 | 0.10 | 0.60 |

**2. More than half say "none", at the ends of complete sets:** digits at 0, Greek at α, Thai and Arabic-Indic digits at 0. 295 of the 388 sit at contexts first-impression minds were never shown exactly; 89 at contexts where they also said "none"; 4 where they continued.

**3. A fifth are not chart walks, and they are the interesting ones.**

- `P R T V X Z` → `B D F H J L N`: the step-two alphabet, wrapping round.
- `ⓗ … ⓐ` → `Ⓩ …`: turning from lower case to capitals.

**4. First-impression minds accept the chart continuations when asked.**

| | Claude | Grok |
|---|---|---|
| the reasoned candidate is the chart neighbour | 0.84 (517 of 612) | 0.84 (196 of 233) |
| the reasoned candidate isn't | 0.69 (116 of 167) | 0.77 (51 of 66) |
| near decoys | 0.03 | 0.005 |

Even nonsensical ones get accepted: `♓` after `♖ ♕ ♔` drew Grok 1/1 and Claude 1/2. Near decoys sit 3 to 48 code points away, so they never test chart adjacency itself. The link-recognition part as designed (CATALOG v2, L-near) therefore can't tell a felt continuation from the chart's next glyph at a sequence's end.

## What they are evidence of: the decision

Joseph's guess holds, in the negative direction. The reasoned answers predict *non-intuitiveness*.

- **Chart-reachability: their main signal.**
  - **The marker.** A continuation the reasoned mind reached by listing a code-point range, at a point where first-impression minds stopped, is reachable by arithmetic and was not felt there. That is a recorded basis, stronger than any stated reason, and it marks the link "chart-reached" in the catalog.
  - **How it is weighed.** It is not evidence that the link is felt. If first-impression minds then recognise it, that recognition has to be checked at a discriminator position (the `choose` question, chart neighbour against an alternative) before it counts as intuitive.
- **Ends, at the rational tier.** A reasoned "none", given leave to look things up and continue, is a deliberate judgement that the run ends there. It counts as evidence of an end.
- **Candidates.** All reasoned continuations are candidates for whole-run recognition, never confirmation. The non-chart ones (21%, such as `P R T V X Z` → `B D F …`) are rational candidates and the most interesting.
- **Not evidence of a felt link.** Reasoned continuations never count toward the intuitive tier. In the rational tier they count only where they are not chart walks.

This replaces METHODOLOGY §4's flat "kept apart … never confirm a link" with a role grounded in what the answers contain. It also exposes a design flaw: L-near's control (near decoys) doesn't cover chart adjacency. A link's recognition at a sequence's end needs a chart-neighbour control, which the `choose` question provides.

## Limits

- **One mind.** Every reasoned answer is Sonnet's.
- **Sheet-level lookups.** The lookup log belongs to the sheet, not the item. "With a `range` lookup" means the sheet had one, which isn't always the item's.
- **Few samples of some answers.** Recognition counts for single candidates are small (1–3 answers), so the table pools them.
