# Pilot re-derivations and first feature correlates (2026-10-03)

> **Status (2026-10-03).** This document is the v1.0 builder's interpretive layer. The builder worked under a brief whose paragraph about an old SIGNA sample string, and other framing, were the coordinating agent's interpolation, not Joseph's (`data/stimuli-v1/LINEAGE.md`). It is kept as written, pending an independent re-reading by an analyst who has not seen it; the comparison between the two readings is itself data.

*Working notes, exploratory/pilot tier unless a line says otherwise. Written by the agent that ran the analyses. An independent audit is at `verification/2026-10-03-audit-rederivations.md`, and this version incorporates its corrections (history at the end). Numbers in §1–§2 come from the scripts named beside them. §3's ink values are read straight from `firmatum/utils/utf/bmp-metrics-ghostty.tsv`, and its vote tallies from the pilot record and `wa9ugjfju.json`.*

## 1. The demand-characteristics number re-derives (`harness/reanalysis/walk23_dissolve.py`)

From the raw workflow outputs (walk2 `w2ojawgjt.json`, walk3 `wlj4rajuj.json`, same `walk2-key-*` sheets, judged by different Sonnet subagent instances):

- **Verdicts over 1,099 pairs.**
  - walk2: 533 consistent-directed, 532 consistent-≈, 34 mixed.
  - walk3: 966 consistent-⟂, 104 directed, 7 ≈, 23 mixed.
  - The pilot record's categories sum to 1,091; it appears to drop ⟂/≈ splits.
- **Fate of the 533 walk2 directed pairs:** 425 became ⟂ (79.7%; the record says 426/533). 88 kept the same winner, 7 flipped, 11 were mixed, 2 became ≈.
- **Same-direction survival by a structure-blind proxy** (both glyphs in the same 128-codepoint page): 23/33 same-page vs 65/500 cross-page. If flips are counted as survival, the figures are 24/33 and 71/500.
- **The seven flips** (hand count):
  - Five moved from numerically wrong to right (⚅ vs ②, ௯ vs Ⅵ, ⒕ vs Ⅹ, ⚅ vs ❹, ⑨ vs Ⅶ).
  - One moved from right to wrong (walk3 says ⅜ > ①).
  - One involves no number (🌔 vs 🌚).

## 2. Feature correlates over the pilot's directed edges (`harness/reanalysis/feature_correlates_pilot.py`)

**Ink** is Ghostty `packed_density` (firmatum/utils/utf, BMP only). It is coverage per wcwidth cell, in a stack that mixes VictorMono SemiBold with JuliaMono fallbacks. Judges never see pixels.

**Value** is Unicode Numeric_Value, gated on the table's `ucd_numeric = yes`. Gematria and Milesian letter values are excluded.

| edges | both glyphs numeric: winner has larger value | numeric pairs: winner has more ink | neither numeric: winner has more ink |
|---|---|---|---|
| walk2 (glyph/≈) | 42/45 = 93% | 20/44 = 45% | 93/131 = 71% |
| walk3 (glyph/≈/⟂) | 38/39 = 97% | 17/38 = 45% | 25/30 = 83% |
| walk4 (graded + ⟂) | 23/24 = 96% | 11/22 = 50% | 21/29 = 72% |
| walk5 triads (cross-judge) | 176/178 = 99% | 78/172 = 45% | 71/87 = 82% |
| walk5b triads (cross-judge) | 181/184 = 98% | 77/177 = 44% | 48/60 = 80% |
| llama3.2:3b triads (both presentations) | 56/103 = 54% | 42/100 = 42% | 58/87 = 67% |

These samples are not independent. walk5 and walk5b re-judge the same 350 triads; 180 glyph pairs recur across triads; walk2 and walk3 share sheets. Effective n is roughly half of what is shown.

Readings, each marked with its tier:

- [pilot, post-hoc] **Sonnet, numeric edges.** Committed numeric edges follow denoted value 93–99% of the time in every format. The format contrast on numeric pairs (93% vs 96–99%) has overlapping intervals.
- [pilot, post-hoc] **llama3.2:3b, numeric edges.** The value correlate is at chance: 54% here, and 51% (34/67) after deduplication. MANIFEST claim 4's "the same two axes survive at both tiers" rested on chain listings; on this edge-level measure the number axis does not survive at 3B. The v1.0 panel tests this (PREDICTIONS P7).
- [pilot, post-hoc] **Ink on numeric pairs** is uninformative, perhaps weakly anti (pooled 45%, every run's interval contains 50%).
- [pilot, post-hoc] **Ink on non-numeric pairs** is a real correlate (71–83% for Sonnet). It holds within a single font face at equal cell width.

## 3. The pilot conflict battery, re-read against measured ink

| pair | pilot votes | measured ink | reading |
|---|---|---|---|
| Ⅸ vs Ⅷ | Ⅸ 16-0 | Ⅷ 0.361 > Ⅸ 0.296 | value beats ink |
| Ⅴ vs Ⅲ | Ⅴ 16-0 | Ⅲ 0.314 > Ⅴ 0.207 | value beats ink |
| ⑩ vs 9 | ⑩ 16-0 | 9 0.2515 > ⑩ 0.1657 | value beats ink (different faces; the pilot key labelled it a control) |
| 🯸 vs 🯱 | 🯸 16-0 | not in the BMP table | value and segment count agree; not a conflict |
| ☷ vs ⚌ | ☷ 16-0 | ⚌ 0.0952 > ☷ 0.0835 (same face, both 2-cell) | against ink; fits line count |
| ‱ vs % | ‱ 12-4 | % 0.2803 > ‱ 0.2118 (cross-face) | against ink; fits element count (‱ has four circles, % two) |
| ‱ vs ‰ | ‱ 12-4 | ‰ 0.2690 > ‱ | against ink and value; fits element count |
| ⚏ vs ⚊, ☷ vs ⚊ | 16-0, 16-0 | winner denser | ink and line count agree, so these cannot separate them |

The pilot's "families without compiled decode resolve to ink" is therefore better stated, pending v1.0, as "resolve to element or line count". The v1.0 conflict battery (`harness/runner/conflict-items-v1.json`) separates these readings. Its annotation file still calls ⑩ vs 9 aligned. That pair is not in the v1.0 battery, and the file is a frozen stimulus input, so the correction lives here and in the PREDICTIONS errata.

## 4. Exploratory: is ladder order linearly readable from text embeddings? (`harness/correlates/embed_probe.py`, `embed_probe_controls.py`; audit controls in `verification/audit_embed.py`)

This picks up Joseph's question from the pilot: are sequence families readable along linear semantic directions? It measures what off-the-shelf embedding models represent about a codepoint, not what any judge perceives. The 31 probe ladders were chosen by the analyst, and their orders are anecdote-tier.

Method: leave one family out (LOFO). For each held-out ladder, a ridge regression is trained from embedding to within-family rank on the other 30 ladders, then scored by Spearman ρ on the held-out ladder. Ties get average ranks.

| model | distinct vectors (ladders / random tail glyphs) | LOFO mean ρ | permutation max | codepoint-sorted random sets (audit) |
|---|---|---|---|---|
| qwen3-embedding (4096-d) | 1.00 / 1.00 | +0.70 (+0.68 with cross-ladder glyph leakage removed) | +0.24 | +0.22 |
| embeddinggemma:300m | 1.00 / 1.00 | +0.41 | +0.14 | +0.44 — codepoint order explains it |
| snowflake-arctic-embed2 | 0.68 / 0.17 | +0.38 | +0.22 | – |
| bge-m3 | 0.68 / 0.17 | +0.23 | +0.19 (not distinguishable at 20 permutations) | – |
| nomic-embed-text, mxbai-embed-large | 0.34 / 0.05 | ≈ 0 | — | — |

The distinct-vector column shows that tokenizer coverage shapes this probe directly. Models with shared tokenizers collapse the same glyphs to unknown tokens.

**Only qwen3-embedding carries a result that survives the controls.**

- On ladders not filed in ascending codepoint order, transfer is +0.65. That includes reverse-filed ones: tone bars +0.90, left eighths +0.50, medals +0.50.
- Its "more" direction has a small codepoint component (+0.22 on codepoint-sorted random sets). That is too small to explain +0.70.
- Split by mechanism, the numeric-trained direction orders **fill** ladders well (+0.64 over 7). **Size** rests on one ladder (+0.80). **Count/tally** is weak (+0.30 over 8).

Hypothesis, unverified: in qwen3-embedding one linear direction partly orders denoted number and fill together, while the pilot's judges, given ⟂, keep them as separate axes. What would test it:

- held-out ladders chosen by someone else;
- the judges' own hidden states;
- more than 3 rungs per ladder;
- a tokenizer-artifact check.

## History of this file

- **2026-10-03, first version.**
  - Its value correlate read letters' cultural numeral values as Unicode numerics. This gave "walk2 80%" and the reading "under glyph/≈ judges committed to 20% numerically wrong edges". That reading did not survive gating on `ucd_numeric`.
  - It also said "six of 7 flips" moved toward the right answer (five do).
  - It called ⑩ vs 9 a non-conflict, called ‱ three circles, and presented embeddinggemma's transfer without the codepoint caveat.
  - All of these were found by the independent audit and are replaced above.
- **The probe's first internal version**, never reported, broke rank ties by list position. Collapsed vectors then inherited a perfect order, and random-set baselines matched the ladders. Average ranks fixed it.
