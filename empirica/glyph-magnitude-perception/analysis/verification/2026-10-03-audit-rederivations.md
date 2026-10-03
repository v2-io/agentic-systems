# Audit: pilot re-derivations and correlates (2026-10-03)

*Independent critical pass over `analysis/2026-10-03-pilot-rederivations-and-correlates.md` (hereafter "the doc") and the four scripts it names. The auditor is a Claude Opus 5.5 agent with no part in writing the doc or the scripts. I had read access to everything and wrote only inside `analysis/verification/`. I checked numbers against the raw judgment files, the feature tables, the pilot record, and the cached embeddings, not against the doc's own account of them.*

*The three audit scripts in this directory are written from scratch. None imports the doc's scripts, so where they agree with the doc, that agreement is evidence and not a repeat of the same code. `audit_walk23.py` covers §1. `audit_correlates.py` covers §2 and adds a `--ucd` flag for the corrected value source. `audit_embed.py` covers §4 and reads the embedding cache read-only. Each runs from any directory with `python3 <path>`.*

## What matters most

1. **The doc's "UCD numeric value" is not the UCD Numeric_Value. Both the walk2 value-correlate and the reading built on it are artifacts of this.** `feature_correlates_pilot.py` takes `numeric_value` from `unicode-axes.tsv` without checking that table's own `ucd_numeric` column. 232 rows have a value but `ucd_numeric = no`: Hebrew gematria (א=1 … ט=9), Greek Milesian (α=1 … ι=10, Μ=40), and similar. Of the 13 walk2 edges the doc counts as "numerically wrong", 10 are a digit beating a Hebrew or Greek letter (④>ה, 3>ז, 4>θ, ½>η, Ⅲ>ח, …). Judges who read ה as a letter are not making numeric errors. With values gated on `ucd_numeric = yes`, walk2 is **42/45 = 93% [82%, 98%]**, not 51/64 = 80%. The 3 genuine walk2 errors (Ⅵ>௯, Ⅶ>⑨, Ⅹ>⒕) are exactly three of the seven pairs that flipped to the correct direction in walk3. So the doc's reading that under glyph/≈ "the same judges committed to 20% numerically wrong edges" does not hold. The format contrast on numeric pairs is 93% vs 97–99%, and the intervals overlap. Corrected numbers for every row are in the table under §2.

   The same reading code is in `harness/runner/analyze_v1.py` (lines 28–37). PROTOCOL-v1.0 defines the value-correlate as edges where "both glyphs carry a UCD numeric value", so this code departs from the frozen protocol. Gating on `ucd_numeric` would bring the code into line with what was registered; it would not change the registration. In the v1.0 stimuli the practical effect is small. Only 2 of 46 both-"numeric" format pairs, both in the pilot-replication stratum, are letter-contaminated, and no triad pairs are. This touches P4 a little and P7 not at all. The bias does run in P4's favour, though: forced format commits on digit-vs-letter pairs and they score as "wrong", while the ⟂ format tends to dissolve them. The comment at line 38 ("same Unicode 14 data") is inaccurate for the BMP table.

2. **⑩ vs 9 is a value-over-ink conflict by the doc's own measurement, not a non-conflict.** Measured `packed_density` is 9 = 0.2515 and ⑩ = 0.1657, so ink favours 9, value favours ⑩, and judges chose ⑩ 16-0. The doc's "value and ink agree" for this pair has no measured source. The pilot's own key file labels it differently again: `conflict-key.json` calls ⑩/9 an "enclosure-vs-value control". The error has spread to three places: PREDICTIONS-v1.0 (committed), `conflict-items-v1.json` (`why_this_battery`), and the decision to leave ⑩/9 out of the v1.0 battery. One caveat applies to every cross-font ink comparison: 9 renders in VictorMono SemiBold and ⑩ in JuliaMono Regular. For **🯸 vs 🯱** the doc's conclusion is right. Seven segments against two means ink and value agree. But these are astral glyphs with no row in the BMP table, so this is a segment-count argument, not "measured ink". `conflict-items-v1.json` marks astral ink as "est"; the doc's §3, headed "re-read against measured ink", does not.

3. **"Six of the 7 flips moved from numerically wrong to numerically right" should read five of seven.** The seven flips are 🌚→🌔, ②→⚅, Ⅵ→௯, Ⅹ→⒕, ①→⅜, ❹→⚅, Ⅶ→⑨. Treating dice as denoting their pip count, five go wrong→right, one goes right→wrong (⅜>①, which the doc names), and one (🌚 vs 🌔) involves no number at all. It may be an illumination-vs-ink reversal, since 🌚 is the darker glyph. Two of the five also rest on ⚅, which has no UCD value, so §1 here uses a different value notion from §2. PREDICTIONS-v1.0 repeats "6 moved". The pattern itself (flips move toward the coherent reading) survives with the count corrected. The count does not.

Everything else in the doc re-derived, or needs only a wording or uncertainty change. Details follow.

## §1. Demand-characteristics re-derivation: re-derives, with one count error and one ambiguity

Independent parse (`audit_walk23.py`):

| claim in doc | re-derived | status |
|---|---|---|
| walk2 533 dir / 532 ≈ / 34 mixed over 1,099 pairs | same. The sheets hold **1,100** unique pairs (verified, no duplicates); one is unparseable because both answers are "③", which is not in the pair. | holds; "1,099" means parseable pairs |
| walk3 966 ⟂ / 104 dir / 7 ≈ / 23 mixed | same, over 1,100 pairs | holds |
| "record says 14 inconsistent … ⟂/≈ splits count as mixed here" | walk3 mixed = 14 glyph/⟂ + **9 ⟂/≈**. The record's categories (966+104+7+14) sum to **1,091**, which is 9 short of 1,100. | the doc's explanation is now verified: the record dropped the 9 ⟂/≈ splits from every category. The doc can drop "unexplained". |
| 425/533 → ⟂ (record 426) | 425; the 11 mixed are all glyph/⟂ | holds; the record's +1 is still unexplained |
| 88 same / 7 flipped / 11 mixed / 2 ≈ | same | holds |
| survival 24/33 same-page vs 71/500 cross-page | same, but "survival" here counts the 7 flips as surviving. Same-direction survival is **23/33 vs 65/500**. | define "survival" in the text; the effect is unchanged |
| 6 of 7 flips wrong→right | 5 of 7 (see item 3 above) | **does not hold as written** |

The fallback substring match in `walk23_dissolve.py` (line 32) never changes an outcome: walk2 has two non-exact answers and walk3 none. `block()` contains a dead `import subprocess`. The record's "93% winner-stable" (88/95) is consistent with this parse.

## §2. Feature correlates: the table's arithmetic reproduces, the value column's label does not

My own edge extraction reproduces every cell of the doc's table exactly. These parts check out:

- **The triad judge mapping.** The script assumes triad *t* went to chunks 2(*t* mod 6) and 2(*t* mod 6)+1 in reversed orientation. All 2,100 key presentations obey this.
- **The 3B "both presentations" edges.** They come from stateless temperature-0 calls with per-item option permutation. Of the 403 consistent edges, 56 rest on a response that echoed both glyphs, where `probe5.py` took the first one. Excluding those 56 gives a value-correlate of 54% (51/95), still chance.
- **The ink correlate is not a cross-font artifact in aggregate.** It holds within a single font face at equal cell width: walk2 29/32, walk5 34/42, walk5b 24/32, 3B 24/39. This strengthens the doc's claim. The doc should still say that `packed_density` is coverage per wcwidth cell, so it is not total ink for 2-cell glyphs, and that the font stack mixes VictorMono SemiBold with JuliaMono Regular fallbacks. ‱ vs % is one cross-face comparison of this kind.

Corrected value column (`audit_correlates.py --ucd`), with 95% Wilson intervals:

| edges | value-correlate as in doc | value-correlate, `ucd_numeric = yes` | numeric pairs: ink-winner rate (UCD) | neither numeric: ink |
|---|---|---|---|---|
| walk2 | 51/64 = 80% | **42/45 = 93% [82, 98]** | 20/44 = 45% | 93/131 = 71% |
| walk3 | 39/40 = 98% | 38/39 = 97% [87, 100] | 17/38 = 45% | 25/30 = 83% |
| walk4 | 25/28 = 89% | 23/24 = 96% [80, 99] | 11/22 = 50% | 21/29 = 72% |
| walk5 | 178/180 = 99% | 176/178 = 99% [96, 100] | 78/172 = 45% | 71/87 = 82% |
| walk5b | 181/184 = 98% | 181/184 = 98% [95, 99] | 77/177 = 44% | 48/60 = 80% |
| llama3.2:3b | 60/108 = 56% | 56/103 = 54% [45, 64] | 42/100 = 42% | 58/87 = 67% |

The doc's readings, re-checked against this:

- **"For Sonnet, denoted value is a near-perfect correlate … once ⟂ is available": still true.** The contrast clause ("under the glyph/≈ format the same judges committed to 20% numerically wrong edges") is not; see item 1. Also, walk2 and walk3 are the same sheets judged by different Sonnet subagent instances, not the same judges.
- **"For llama3.2:3b, the value correlate is at chance": holds** under either value source and after deduplication (34/67 = 51%).
- **"Among numeric pairs, ink is anti-informative (44–52%)": overstated.** Every run's interval contains 50%. Pooling the Sonnet runs gives 203/453 = 45% [40%, 49%], but the pooled runs are not independent (walk5/5b re-use the same triads; walk2/3 the same sheets). The data support "uninformative, perhaps weakly anti", not "anti-informative".
- **Two things the table hides.**
  - **Non-independence.** walk5 and walk5b are the same 350 triads re-run, not two replications. Within the triad runs the 1,050 pair-slots contain only 775 unique glyph pairs, so 180 pairs recur across triads. Deduplicated, walk5's numeric edges are 99/100 rather than 178/180. The rates stand; the effective n is about half what is shown.
  - **Selective ranges in PREDICTIONS-v1.0.** "98–99% under ⟂-bearing formats (walk3/5/5b)" and "ink 80–83%" both leave out walk4, which is also ⟂-bearing (89% value, 71% ink). Under the corrected value source walk4 is 96%, so the omission happens not to matter for value. It does matter for ink.

## §3. Conflict battery re-read

Measured ink and vote tallies, checked against `bmp-metrics-ghostty.tsv`, `conflict-sheet.json`, and the raw output `wa9ugjfju.json` (8 judges × 2 orders):

| pair | votes (verified) | measured ink | doc's statement | audit |
|---|---|---|---|---|
| ☷ vs ⚌ | ☷ 16-0 | ⚌ 0.0952 > ☷ 0.0835 (same face, both 2-cell) | against ink | **holds** |
| ‱ vs % | ‱ 12-4 | % 0.2803 (VictorMono) > ‱ 0.2118 (JuliaMono) | against ink | holds as measured, but this is a cross-face comparison |
| ‱ vs ‰ | ‱ 12-4 | ‰ 0.2690 > ‱ | not discussed | the same element-count reading fits; value and ink both favour ‰ |
| Ⅸ vs Ⅷ, Ⅴ vs Ⅲ | 16-0, 16-0 | 0.296 < 0.361; 0.207 < 0.314 | genuine value-over-ink | **holds** (values match to 3 d.p.) |
| ⑩ vs 9 | ⑩ 16-0 | 9 0.2515 > ⑩ 0.1657 | "value and ink agree" | **does not hold**: it is a conflict (item 2 above) |
| 🯸 vs 🯱 | 🯸 16-0 | not in the BMP table | "value and ink agree" | right, by segment count; not measured |
| ⚏ vs ⚊, ☷ vs ⚊ | 16-0, 16-0 | ⚏ 0.0677 > ⚊ 0.0476; ☷ 0.0835 > ⚊ | not discussed | ink and line count both favour the winner and yang count opposes it, so neither item separates ink from line count |

There is also a factual slip: "three circles vs two" for ‱ vs %. ‱ (PER TEN THOUSAND SIGN) has **four** circles. The JuliaMono raster at `.rasters/4x/packed/20/2031.png` confirms this; three circles is ‰. The element-count reading is unaffected.

§3 names no script, although the doc's header says "every number here is produced by a script in this tree; the script is named beside it". The ink values come straight from the TSV in `firmatum/utils/utf`, the votes from the pilot record, and §1's "six of 7" is a hand count. The header promise does not hold for §3 or for that §1 count.

## §4. Embedding probe: numbers reproduce; the qwen3 result survives two new controls, embeddinggemma's does not

My independent ridge and Spearman implementation, run on the cached vectors, reproduces qwen3-embedding's LOFO mean ρ (+0.697). It also reproduces every entry in the table and every control value the doc quotes: +0.65 on the 9 ladders not filed in ascending codepoint order; tone bars 0.90; left eighths and medals 0.50; numeric→non-numeric +0.51; non-numeric→numeric +0.62. `audit_embed.py` adds three checks:

- **Leakage.** Two glyphs belong to two ladders each: █ (lower-eighths, shade) and ● (pie, disc-size). When one of those ladders is held out, its glyph is still in training with a rank label. Removing held-out glyphs from training moves qwen3 from +0.697 to **+0.680** (pie drops 0.70→0.40, disc-size 1.0→0.8). The effect is small, but the reported number is slightly inflated.
- **A direct codepoint test (new).** I trained the ladder "more" direction on all 31 ladders, then scored it on 500 random uniform-tail glyph sets sorted by codepoint. These sets have no magnitude, so any ordering comes from codepoint.
  - **qwen3:** mean ρ = +0.22 (sd 0.47). The prediction correlates +0.26 with codepoint across the 200 tail glyphs. So qwen3's direction carries a codepoint-correlated component (possibly block identity rather than bytes), but it is too small to explain +0.70, or +0.65 on non-ascending ladders.
  - **embeddinggemma:** mean ρ = **+0.44** on codepoint-sorted random sets, and its LOFO on non-ascending ladders falls to +0.22 (from +0.49 on ascending ones, per the doc's own controls JSON). For embeddinggemma, codepoint is a sufficient explanation. The table row "+0.41" should carry that caveat, or the doc should say plainly that only qwen3 survives the controls.
- **Which mechanisms the numeric-trained direction actually orders (qwen3).** The doc's "non-numeric" side lumps fill, size and count together, and includes dice, which denote numbers. Split by mechanism:
  - fill: +0.64 over 7 ladders (pie and sovereign at 0)
  - size: +0.80, from a single ladder (disc-size)
  - count/tally: **+0.30** over 8 ladders; three of them (tally-lines, dots-vert, volume) are at −0.5

  The hypothesis "a single linear direction partly orders denoted number, fill, size and count together" is supported for number and fill. Size rests on one 4-rung ladder, and count is the weakest leg.

Smaller points:

- The probe's T1 test (PC1 within each family) is computed but not reported. Its random-set baseline has p95 = 1.0, which makes it uninformative by design, so leaving it out is defensible; the doc could say so.
- Identical distinct-vector fractions for bge-m3 and snowflake (0.68/0.17), and for nomic and mxbai (0.34/0.05), are consistent with shared tokenizers collapsing the same glyphs to unknown tokens. That is direct evidence that tokenizer coverage shapes this probe, which bears on the doc's last untested item ("not a tokenizer artifact").
- With 20 permutations the smallest attainable p is about 1/21. bge-m3's +0.23 against a permutation max of +0.19 is not distinguishable from the null at that resolution.
- The control's NUMERIC set includes si-length (unit prefixes, not numeral notation) and excludes dice (which denote numbers). This makes little difference to the means.

## Other things checked along the way

- **Registration timing holds.** PREDICTIONS-v1.0 was committed in 026cfb56 at 20:11:37 UTC. The first non-shakedown ledger row is 20:11:59 UTC (`triads-perp-single-sonnet5`). The claim "registered before any confirmation run" holds, by 22 seconds.
- **Provenance of the quoted Joseph question in §4.** `RECONCILIATION-QUEUE.md` (2026-08-25 ruling) names "the linear-semantic-vector question", which corroborates it. I could not check the docstring's verbatim quote against a transcript, because `memorata-search` timed out on ollama, which the campaign may be keeping busy. I did not restart ollama.
- **MANIFEST claim 3 still says 426/533** (re-derived 425) and claim 5 still counts ⑩>9 and 🯸>🯱 as value-over-ink evidence. Both are queued for whoever revises the claims; I made no edits.
- **Concurrent edits.** While I worked, `analyze_v1.py`, `run.py` and `judges-v1.json` changed in the working tree. Someone else is active there; the change to `analyze_v1.py` does not touch the value source.

## Suggested repairs, for whoever owns the doc

- **Value source.** In `feature_correlates_pilot.py` and `analyze_v1.py`, gate on `ucd_numeric == yes`, matching PROTOCOL-v1.0. If gematria or Milesian values are wanted, report them as a separate, labelled correlate.
- **Doc and PREDICTIONS-v1.0 text.** Replace the walk2 80% and its reading, the "6 of 7", the ⑩/9 non-conflict, and the circle count. PREDICTIONS is a registration record, so its correction belongs in its history layer and should not rewrite the committed file. The predictions themselves do not depend on these sentences.
- **Uncertainty.** Report intervals on deduplicated pairs, and say that walk5/5b, and walk2/3, are not independent.
- **§4 scope.** Present §4's positive result as qwen3-only, with embeddinggemma noted as codepoint-explainable. Consider adding the codepoint-sorted random-set control to `embed_probe_controls.py`; it costs nothing because the tail embeddings are already cached.

## Scope and limits of this audit

I did not:

- re-run `embed_probe.py` against ollama; I worked from its cache and JSON outputs;
- audit the v1.0 run data (`data/runs-v1/`) or any v1.0 result;
- inspect rasters beyond ‱.

The ink measurements themselves (the `firmatum/utils/utf` pipeline) are taken as given. The doc's absences are not covered by this report: what it does not claim, I did not test.

On the doc as a piece of work: its candour is real. It names the first embedding bug, labels its own tiers, and says it is not independent. That candour made the checks above fast. The three substantive errors share one shape: a value or ink property was asserted for a glyph without being looked up, and a correct-looking shape stood in for the lookup.
