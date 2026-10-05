# OBSERVATIONS — a running log of what the rounds show, as it shows it

*Append-only, newest last. Each entry gives the evidence, its tier and its status. Entries are hypotheses until a later round tests them, and nothing here is a claim (MANIFEST holds claims). How the rounds were run is in `RUNS.md`; the per-round fits and reports are in `data/rounds/`; the ranked list is `STANDINGS.md`.*

---

## 2026-10-04 · `▁` (U+2581) behaves like a word-boundary marker for Gemini Flash, not like the bottom rung of the fill ramp

**How it came up.** Joseph asked about #3 of the r002 standings, `▂ ▁ ▃ ▄ ▅ ▆ █ ▇`. Its end pairs are swapped from the ramp `▁▂▃▄▅▆▇█`. Then he added: *"I know some models use the 10% (or something) as a word-separator or something…"* In SentencePiece tokenizers (Gemini/Gemma, Llama 2 and others), U+2581 LOWER ONE EIGHTH BLOCK is the metasymbol that marks a word boundary.

**First finding: the swap was not evidence.** Through r002, no question had shown `▁` together with `▂`, nor `▇` together with `█`. Their order inside that candidate was the fit's arbitrary choice, and nothing contradicted it. The standings now show such **untested links** and discount them (`harness/seq/standings.py`, commit db72b619). 17 of the 107 r002 candidates had at least one. The queue was already testing these links in r003, through order items over the whole ramp and the triad `▁▂▄`.

**Second finding: `▁` is excluded by Gemini Flash.** The evidence is every answer through r003 on triples made only of ramp glyphs. These are triple observations, with order answers weighted by w(k).

| mind | sets (4+), no `▁`: ramp order | sets with `▁`: what happens to `▁` | triads with `▁` |
|---|---|---|---|
| gemini38flash | 1.00 | **left out 96%** (8 of 8 order answers put `▁` in extra) | left out 50%, ramp order 30%, ⟂ 20% |
| grok46 | 1.00 | ramp order 1.00 | ramp order 1.00 |
| sonnet55 | 1.00 | ramp order 1.00 | ramp order 0.90, `▁` left out 0.10 |
| haiku45 | 0.97 | ramp order 1.00 | ramp order 0.90 |
| opus55 | 1.00 | ramp order 0.85 | 1.00 (n = 2) |
| gemini31pro | 1.00 (n = 2) | — | ramp order 0.50, left out 0.25, ⟂ 0.25 (n = 4) |

Gemini Flash echoes `▁` without trouble: no answer showing it went unparsed. It sometimes orders it (`▁ ▓ █` in r002 and r003). Shown with four or more ramp glyphs, it consistently treats `▁` as not belonging.

**Reading.** The SentencePiece account fits, but it is a hypothesis, not a measurement:

- The Gemini tokenizer was not inspected.
- The counts are small: 8 order answers, 10 triad observations.
- Gemini 3.1 Pro is too thin to say anything.

If it holds, it is a real fact about how these minds perceive the glyph: the token arrives as a word-boundary marker. It is not an artifact to remove. It is also a clean instance of the study's co-equal object: the substrate shaping the order a mind reports.

**What would test it:**

- **More Gemini answers on `▁`-containing ramp items.** Seeded below; the queue also has them.
- **The same probe on a byte-level-BPE family.** GPT-2-style tokenizers use `Ġ` (U+0120) for a space and `Ċ` (U+010A) for a newline, so the prediction is that those minds treat `Ġ`/`Ċ` specially and `▁` normally.
- **A look at the tokenizers themselves**, where they are inspectable: Gemma for Gemini's family; Glimmer through llama.cpp's `/tokenize`.

**Status:** hypothesis, seeded for testing. Seed: `data/seeds/tokenizer-markers.jsonl`.

---

## 2026-10-04 · Two of the r002 standings' sequences rested on untested links

**#3** is `▂ ▁ ▃ ▄ ▅ ▆ █ ▇` (above). **#59** is `: · ∶ ⁝ ⁞`.

- **What was asked.** The colon had been asked in exactly one triple, `: ⁝ ⁞`. That triple was shown three times, across r001 and r003, to four minds. Ten of the twelve answers put `⁝` in the middle, the order of rising dot count (2, 3, 4).
- **What was never asked.** No question had shown `:` with `·` or with `∶`. The fit put the colon at the bottom arbitrarily.
- **What the glyphs suggest.** `:` has two dots, like `∶` (RATIO), so it most likely sits level with `∶`, above `·`. That is untested.
- **Fixes, made the same evening:**
  - the standings list untested links and discount them;
  - support counts only cold-started annealing chains, since warm chains inherit the previous fit and had made an untested ordering look settled (support 1.00);
  - a dots-and-colons seed (`data/seeds/dots.jsonl`) puts the near-identical pairs (`:`/`∶`, `·`/`⋅`) in front of the minds. That tests the tie option, which has had little use so far.

**Status:** both are fit artifacts, now flagged; the seeds are queued.

---

## 2026-10-04 · The first fix for untested links was partial; the standings now rank only supported pieces

Joseph: *"I thought you said you already fixed that bug?"* He had. Two things still let untested structure into the ranked list:

- **The discount was proportional.** #59 had one untested link out of four, so it kept 75% of its score and stayed ranked.
- **The support fix applies only to new fits.** STANDINGS.md was still built from the r002 fit.

**The rule now** (`harness/seq/standings.py`):

- Every candidate is **split at its unsupported links** before ranking. A link is supported only when some triple inside the candidate holding both of its glyphs was answered in the candidate's order by at least two answers and a majority.
- A tie inside a step needs the same support, from tie answers. Otherwise the tie is cut out on its own.
- Only supported pieces of three or more glyphs are ranked.
- The splits are listed under the table as open questions for the queue.

At r003, 21 of 147 candidates were split. Among them:

- `· : ∶ ⁝ ⁞` became `·` | `:` | `∶ ⁝ ⁞`;
- the Roman-and-fraction chain lost its unwitnessed cross-family ties `Ⅿ=⅙` and `⅓=ↂ`.

**What survived as a real tie: `9=𝟵`** (plain nine and MATHEMATICAL SANS-SERIF BOLD DIGIT NINE). This bears on Joseph's digit-dress question.

- **In order items:** shown with other digits, Gemini Flash, Grok, Opus and Sonnet placed `9` and `𝟵` at the same step, as tie answers in their own order lines, for each of the digits 0, 1, 4, 5, 6 and 8 shown beside them.
- **In a triad beside an unrelated glyph** (Ethiopic `ላ`): every mind answered "only `9` and `𝟵` go together".
- **Haiku** mostly answered ⟂ or "two" instead.
- **Reading:** a dress of the same digit read as the same step, by four of the five frontier minds. This is anecdote tier: one digit, one dress, one round's sets.

**Status:** the fix is in place. The `9=𝟵` tie is a candidate observation for the digit-dress lattice seed to extend.

---

## 2026-10-04 · Probe r003p: the ramp's ends, tested directly

The probe was Joseph's ask: *"get additional data points so we have a good spread, and especially get the other end of the sequence sorted out."* It asked all 56 triads of `▁▂▃▄▅▆▇█`, each in all three Latin rotations, plus 9 order items in two shuffles each, of every API mind. Report: `data/rounds/r003p/probe-report.md`. Gemini 3.1 Pro had answered 29 of its 59 sheets when this entry was first written. All six minds completed later that evening; the figures below are from the complete probe.

**The top end (`▇█`) is not swapped for anyone.** Answers agreeing with the ramp order on triads holding both `▇` and `█`:

| mind | `▇█` agreement |
|---|---|
| Gemini Flash | 18/18 |
| Sonnet | 17/18 |
| Opus | 16/18 |
| Haiku | 16/18 |
| Gemini Pro | 15/18 |
| Grok | 12/18 |

Grok's misses on that link are "only two go together" answers, not reversals. The r002 swap was the fit's arbitrary placement on an untested link, as recorded above.

**The bottom end splits by family, and the split matches the tokenizer hypothesis.** Agreement on the `▁▂` link:

| mind | `▁▂` agreement |
|---|---|
| Sonnet | 15/18 |
| Opus | 15/18 |
| Haiku | 14/18 |
| Grok | 13/18 |
| **Gemini Pro** | **3/18** |
| **Gemini Flash** | **0/18** |

Gemini Flash leaves `▁` out of 81% of the triads that hold it. In every one of its 11 order answers on probe sets containing `▁`, it orders the rest of the ramp and puts `▁` in extra, for example `▂ ▃ ▄ ▅ ▆ ▇ █ · extra: ▁`. Gemini Pro leaves `▁` out of 51% of the triads that hold it. Claude and Grok leave it out of 6% or less.

**Reading.** Both Gemini minds, and only they, decline to place U+2581 on the fill ramp. That is the prediction if their (SentencePiece) tokenizer delivers it as a word-boundary metasymbol. The prediction is now confirmed in direction, with substantial n: 168 triad answers each for Gemini Flash and Gemini Pro, plus Gemini Flash's 11 order answers. It is still a behavioural inference: the tokenizer itself has not been inspected.

**The byte-level-BPE contrast (`Ġ Ċ G g ĉ`) is inconclusive.** Every mind mostly answers "only two go together" on these, with no family-specific pattern. There is no byte-level-BPE family on the roster yet to compare (OpenAI joins after Nov 2).

**Status:** the `▁` finding is a supported observation across the Gemini family, mechanism hypothesized. The `▇█` question is closed: no swap.

