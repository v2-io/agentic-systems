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

