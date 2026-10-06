# De-novo feedback 1: spike `embedding-tendrils-2026-10-05`

*Independent critical pass, Claude Opus 5.5, 2026-10-05. I read `README.md`, `no-go.md`, `debrief.md`, every script in `work/`, the result JSONs in `derived/`, the raw probe ledgers, and `../../METHODOLOGY.md`. I re-derived the claims from the code and data rather than from the prose. Labels follow the spike's own: **[measured]** = I computed it; **[observed]** = read off examples; **[inference]** = my interpretation.*

**What I ran.** Everything below is CPU re-analysis of the spike's cached files, except one small frontier probe: 2 sheets × 3 minds = 6 calls, in the study's sheet wording, answers kept in my scratchpad, not here (finding 1). No GPU, no local model, nothing written to the spike's `derived/`, `data/` or `harness/`. My re-analysis scripts lived in a session scratchpad, so each computation is described closely enough below to redo.

---

## Verdict in brief

- **Holds, and reproduces:** the tokenizer collapse (93% / 71% `[UNK]`; 750 and 5,019 distinct vectors), the retrieval tables I re-ran, the bare-glyph negative, the carry test's logic, and the learned-probe no-go, which survives a gentler optimizer sweep (finding 2c).
- **The widest-reach claim needs re-scoping before anyone acts on it.** "About 80% of first proposals on never-shown glyphs are the next code point" is mostly letters and ASCII, where Unicode order *is* the alphabet. A discriminating probe shows that in Greek and Hebrew the minds choose the alphabet over the chart. Chart-following is real, but narrower and more family-specific than stated (finding 1). This bears directly on the pending "mark ±1 links as chart order" read-off.
- **The line/axis no-go is overstated in its geometric part.** The extrapolation-retrieval negative stands. But "sequences are barely straighter than random" and "no advantage where codepoint fails" rest on baselines that hide a real ordering signal. A permutation control and the PC1 numbers on codepoint-wrong sets both show it (finding 2).
- **Three artifacts move numbers.** (a) The universe holds only the 43 study-used CJK and other excluded-repertoire glyphs, which leaks answers to the name channel and to codepoint (finding 3). (b) The local-LLM ranker spends rank 1 on `,` in 42% of node-mode lists (finding 4). (c) The debrief's chick-to-egg claim for the local LLM is contradicted by the spike's own data (finding 5).

---

## 1. "Codepoint order leaks into the minds' answers": real, but the 78–88% figure mostly measures alphabet knowledge

**What the probe sampled [measured].** The fresh probe is 97 letters (L*) of 135 glyphs, plus 30 symbols, 6 punctuation and 2 numerals, because the universe is 58% letters. The 15 ASCII glyphs were sampled from *all* ASCII, which `probe.py` itself notes have been seen. So "135 glyphs never shown in the study" (README; debrief) is true of 120.

**Where the +1 answers come from [measured]**, as first proposals that are the next code point, over answered items, all families pooled:

| stratum | +1 / answered |
|---|---|
| ASCII | 33 / 37 (`B → C`) |
| letters and numerals, non-ASCII | 84 / 104 |
| symbols and punctuation, non-ASCII | 21 / 33 |

In nearly every script, Unicode encodes letters in the traditional alphabetic order. So for 117 of the 138 +1 answers, "the next code point" and "the next letter of the alphabet" are the same glyph, and the probe cannot tell chart knowledge from alphabet knowledge. Of the README's four headline examples, two are conventional orders:
- `𐲇 → 𐲈`: Old Hungarian ED → AND is alphabetical.
- `𓄿 G001 → G002`: Gardiner's sign list, and the number is in the glyph's own name.

The sentence "That is the code chart, not anything one could call perceiving those glyphs" therefore does not follow for letters. Whether the next letter of an alphabet counts as a perceived sequence is a question for the study's definition. METHODOLOGY §1 measures *conditional continuation* and does not exclude it.

**Where the probe does discriminate [observed].** These are the non-ASCII symbols with no conventional order:
- Clear chart reads: `❵ → ❶`, `🛊 → 🛋`, `⍦ → ⍧`, `⍙ → ⍚`, `⿾ → ⿿` (two families), `🭬 → 🭭`, `🯊 → 🯋`. That is about 8 answers, almost all from Claude and Gemini.
- Conventional or semantic: dominoes (`🁊 → 🁋`, two families each, twice), `䷢ → ䷣` (King Wen order; all three families), `☐ → ☑`, `♟ → ♞`, `␟ → ␠` (ASCII control order), `£ → $`, `🤺 → 🏇`.

So the clean evidence for chart-reading is a handful of answers, real and family-skewed, not 80%.

**A discriminating probe [measured; n is small, one pass].** The cases that separate chart from convention are the places where Unicode order departs from the alphabet:
- Greek final sigma `ς` sits between `ρ` and `σ`.
- Hebrew final forms are interleaved: `י ך כ`, `ל ם מ`.
- Latin-1 puts `×` and `÷` inside the letters: `Ö × Ø`, `ö ÷ ø`.
- ASCII `z` is followed by `{`.

I asked sonnet55, gemini38flash and grok46 with the study's sheet prompt (`items.sheet_prompt`, "none" offered, sheets of 5). One sheet held short alphabet contexts (`ο π ρ`, `ז ח ט י`, `Ó Ô Õ Ö`, `ò ó ô õ ö`, `w x y z`). The other held single glyphs (`ρ`, `י`, `ל`, `Ö`, `z`). First proposal, then the rest of the list:

| context | chart next | alphabet next | claude | gemini | grok |
|---|---|---|---|---|---|
| `ο π ρ` | ς | σ | **σ**, ς, τ | **σ**, ς | **σ**, τ, υ |
| `ז ח ט י` | ך | כ | **כ**, ך, ל | **כ**, ך | **כ**, ל, מ |
| `Ó Ô Õ Ö` | × | Ø | **×**, Ø, Ù | **Ø**, × | **Ø**, Ő, Ō |
| `ò ó ô õ ö` | ÷ | ø | **÷**, ø, ù | **ø**, ÷ | **ø**, ő, ō |
| `w x y z` | { | none | none | none | none |
| `ρ` | ς | σ | **σ**, τ | **σ**, ς, τ | **σ**, τ |
| `י` | ך | כ | **כ**, ך | **כ**, ך, ל | **כ**, ל |
| `ל` | ם | מ | **מ**, ם | **מ**, ם, נ | **מ**, נ |
| `Ö` | × | Ø | none | Ü, Ä, P | none |
| `z` | { | none | none | none | none |

- In well-known alphabets, every family puts the alphabet first.
- The chart glyph shows up as **runner-up** for Claude and Gemini, never for Grok. That matches the spike's family ordering.
- Claude put the chart glyph *first* in the Latin-1 runs (`×`, `÷`), the one place where the symbol sits physically inside a letter run that the models have surely seen in code-chart tables.

**[inference]** "Minds know the Unicode charts, and the chart surfaces in their lists, more so for Claude and Gemini" survives. "Their first proposal is the chart rather than the sequence" does not survive as a general statement. It holds for arbitrary symbol blocks and a few interleaved spots.

**Consequence for the pending read-off.** HANDOFF plans to tag ±1 links as "chart order". By this evidence a ±1 tag marks every alphabet, digit run and enclosed-numeral run, which is most of the genuine sequences. It does not isolate chart artifacts. A tag that would isolate them is narrower:
- **Discriminator positions:** the next code point is in a different name template or general category, or the block has no conventional order (e.g. Dingbats ornaments, Transport and Map Symbols, Legacy Computing). A ±1 answer there is chart-shaped.
- **Rank evidence:** the chart glyph given as runner-up to a conventional first choice.

A small, cheap probe over more discriminator positions would settle the share properly. Candidates: Hebrew finals ×5, Greek `ς`, Latin-1 `× ÷`, Cyrillic `ё`/`Ё` (outside the main run), Armenian/Georgian archaic letters, Latin Extended-A pairs. That is a few dozen items, no GPU.

## 2. The line/axis no-go: the extrapolation negative stands; the geometric story is overstated

**2a. The step-cosine baseline hides the order signal [measured].** no-go §3 compares $\cos(b-a, c-b)$ along agreed paths (about −0.39 to −0.45) with random triples from the whole universe (about −0.49), and concludes that sequences are "barely straighter than random". The debrief goes further: "each step points in a direction almost unrelated to the previous step." A cosine of −0.4 is not "unrelated"; it points back. More importantly, universe-random is the wrong null.

I re-ran the check over the same 970 agreed triples `a b c` with two other baselines: the same three glyphs with the middle swapped, and random triples from the node's own block.

| space | true order | middle swapped | same-block random |
|---|---|---|---|
| all-minilm, name | −0.394 | −0.531 | −0.485 |
| Qwen3-Emb-0.6B, glyph | −0.445 | −0.518 | −0.492 |
| Qwen3-Emb-4B, glyph | −0.441 | −0.520 | −0.495 |
| bge-m3, name | −0.437 | −0.518 | −0.482 |

The true order is straighter than its own permutation by 0.07–0.14, with a standard error of about 0.01 at n = 970. That holds even for the bare-glyph Qwen embeddings. So the spaces do carry the minds' order. Per-glyph idiosyncratic variation swamps it at single steps.

A line-plus-noise model fits: with step $\delta$ along an axis and per-glyph noise $\sigma$, $\cos \approx -0.4$ corresponds to $\delta^2/\sigma^2 \approx 1/7$. That is a real axis that two or three points cannot locate. It is the mechanism behind the extrapolation failure, rather than evidence that there is no axis.

**2b. Distance grows with distance along the sequence [measured].** For survey sequences and multi-family order answers of 6 or more glyphs, I computed the mean $|x_i - x_{i+k}|^2$ for k = 1…5, against the same sets shuffled. all-minilm names, survey: 0.302, 0.322, 0.385, 0.372, 0.435, against a flat 0.366 when shuffled. Qwen3-Emb-4B glyph, order answers: 0.323 rising to 0.417, against a flat 0.36. The minds' sequences are ordered manifolds in these spaces, not straight lines. Joseph's "line" is the wrong shape; his "axis" intuition is not empty.

**2c. "No advantage where codepoint fails" misreads its own number [measured].** `axis.json` reports PC1 $|\rho|$ on sets where codepoint order is wrong ($|\rho| \lt 0.9$), but not codepoint's own $|\rho|$ on those sets. I computed it:

| sets where codepoint is wrong | PC1 | codepoint | chance | paired PC1 − cp (se) |
|---|---|---|---|---|
| survey, all-minilm name (n = 113) | 0.616 | 0.474 | 0.415 | +0.142 (0.030) |
| order, all-minilm name (n = 107) | 0.526 | 0.419 | 0.420 | +0.107 (0.034) |
| survey, Qwen-0.6B glyph | 0.563 | 0.474 | 0.416 | +0.089 (0.035) |
| order, Qwen-4B glyph | 0.561 | 0.419 | 0.416 | +0.142 (0.036) |

Selecting on "codepoint < 0.9" drags codepoint down by construction, so PC1 against codepoint is flattering here. PC1 against chance on the same sets is unbiased, and PC1 is 0.1–0.2 above it. So on exactly the sets where codepoint fails, a set's own axis orders it better than chance.

That is an **ordering** result: the axis is fitted to known members. It is not a **retrieval** result. The retrieval tests (offset, line, meanstep, pc1 extrapolation) all stay below plain nearest-neighbour, and that no-go stands. The present-truth statement would be: *the minds' order is weakly encoded in these spaces, enough to order a known set above chance where codepoint fails; not enough to find the next member from the universe.* The PC1-variance-share statistic ("sequences are not lines": 0.424 against 0.402) has little power for sets of 4–10 points in high dimension, and should not carry the conclusion.

**2d. The learned probe: the no-go survives a fairer optimizer [measured].** The spike's residual probe uses Adam at lr 3e-3. That swamps the "initialised near zero" residual within a few dozen steps, so "more training makes held-out worse" partly measures the optimizer. I re-ran a copy (output to scratchpad) with all-minilm names, held-out blocks, held-out hit@10, nearest-neighbour = 0.786:

| lr | steps | rank | weight decay | hit@10 |
|---|---|---|---|---|
| 3e-4 | 10 | 64 | 1e-4 | 0.783 |
| 3e-4 | 40 | 64 | 1e-4 | 0.749 |
| 1e-4 | 150 | 64 | 1e-4 | 0.741 |
| 3e-4 | 150 | 8 | 1e-4 | 0.731 |
| 1e-4 | 600 | 64 | 1e-2 | 0.702 |

The learned part never beats nearest-neighbour at hit@10 on held-out blocks, overall or on cp-far contexts. At hit@30 and hit@100 on cp-far it comes within ±0.013 of it, which is 3 contexts either way. no-go §5's conclusion holds. Its specific numbers (0.598, 0.402) reflect the aggressive learning rate. Also, `run_all.sh` doesn't regenerate the 600-step residual row that no-go §5 cites; it lists only the 150-step residual.

## 3. The universe leaks answers for CJK and the other excluded repertoires [measured]

`lib.universe` drops the large ideographic and syllabic repertoires, then adds back every glyph the study used. So inside CJK, Egyptian, Cuneiform and the rest, the universe holds only the **43** study-used glyphs, and every truth there is among them:
- **Codepoint ranks:** in a sparse range they are tiny. `億 → 兆` is 66 code points away and ranks 1; `二 → 一` ranks 6.
- **Name-based rankers:** every CJK name is `CJK UNIFIED IDEOGRAPH-XXXX`, so they rank all 43 near the top.

37 of the 234 cp-far contexts (16%) are CJK numerals. On them, hit@30 is 0.92–1.00 for every name ranker and 0.41 for codepoint. Excluding them (cp-far, hit@10 / hit@30):

| ranker | all cp-far (234) | non-CJK (197) |
|---|---|---|
| cp | 0.342 / 0.521 | 0.376 / 0.543 |
| name>cp+num | 0.487 / 0.684 | 0.497 / 0.624 |
| all-minilm, name | 0.538 / 0.765 | 0.574 / 0.721 |
| mix cp \| name>cp+num | 0.474 / 0.667 | 0.508 / 0.680 |
| mix cp \| all-minilm name | 0.470 / 0.744 | 0.513 / 0.741 |

The headline "cp plus names lifts cp-far hit@30 from 0.52 to 0.67–0.74" becomes **0.54 to 0.68–0.74** on non-CJK contexts. The recommendation survives, with the no-model version's gain cut from 15 points to 14, and the minilm version's from 22 to 20. README §3 already notes that CJK name matches are "semantic matches dressed as name matches" (they are 43 of the 138 "one token differs" pairs). In the retrieval tables, though, the mechanism is the sparse universe, and it was not disclosed there. A dense universe, or ranking CJK nodes against the full CJK block, would remove it.

## 4. The local-LLM ranker spends its top ranks on separators [measured]

The prompt `Symbol sequence: <glyph>` invites a list separator. In node mode, `,` is the rank-1 candidate in 771 of 1,822 lists, and in the top 5 of 1,648. `(`, `.`, `、` and `，` follow. These are universe glyphs, so they occupy ranks. Dropping the six separators `, ( . 、 ， )` (unless one is the truth):

| ranker | before: hit@1 / hit@10 / hit@30 | after: hit@1 / hit@10 / hit@30 |
|---|---|---|
| node mode, all (n = 1,056) | 0.129 / 0.704 / 0.835 | **0.358** / 0.728 / 0.844 |
| node mode, cp-far | 0.060 / 0.346 / 0.585 | 0.111 / 0.393 / 0.615 |
| context mode, subset (n = 184) | 0.451 / 0.739 / 0.859 | 0.489 / 0.745 / 0.864 |

In context mode, the spaced context tells the model the separator, so the effect is small. The ordering against codepoint is unchanged. But the README's node-mode hit@1 of 0.129 is mostly an artifact of the prompt format.

## 5. The debrief's case for the local LLM is not supported by the data [measured]

The debrief says: *"Faces, vehicles, an egg after a hatching chick: a local LLM is the only cheap stand-in I found that follows those."* README §4 says the same. On the spike's own instance `🐓 🐤 🐣 → 🥚`:
- all-minilm on names ranks `🥚` **1st**;
- node-mode Qwen3-8B ranks it 11th;
- codepoint ranks it 1,983rd;
- the context-mode LLM never ran on this instance, because the run was stopped.

On emoji cp-far contexts in the context-LLM subset (n = 8), context-LLM hit@10 is 0.38 against 0.50 for both name rankers. Across all cp-far contexts in that subset, it is level with name matching at best. What the data support is: "a local LLM given the context is roughly level with name matching where codepoint fails, at GPU-hours of cost." Nothing measured shows it tracks semantic jumps better than name embeddings. This is the document Joseph reads, so it matters most there.

## 6. What the reference sets represent

- **r011 first2 is 78% "end" items [measured].** 824 of the 1,056 contexts are the old planner's end-of-row extensions, mostly along codepoint runs; 28 are `explore` and 1 is `tail`.
  - On the 232 non-end contexts, the cp-near share is 60% rather than 78%, and cp hit@1 is 0.48 rather than 0.74.
  - The README discloses the planner bias. The debrief's bullet "where minds of two or more families agree on what comes next, it's the adjacent code point 74% of the time" sits under "part of that is the minds themselves", but it is mostly a statement about which contexts the planner asked.
  - The figure is also cp hit@1, not the ±1 share, which is 77.8%.
- **136 of the 1,056 are between-items, used as continuations from both sides.** METHODOLOGY §6 ports between-answers as "their own kind… not continuations". This is a spike reference set, not the tree, and it is disclosed, so it is harmless. Codepoint scores near-perfectly on them, since a two-sided gap determines its filler.
- **The prospective evidence for the name channel is about 1 glyph [measured].** On the fresh probe's 14 cp-far glyphs, codepoint finds 8 in the top 10 and name methods 6. The mix gains one glyph. The README says this is too few to rank, which is right. But recommendation 2 therefore rests on the retrospective sets, whose biases (end items, block-swept surveys, the CJK leak) all favour Unicode-structured neighbours.
- **The probe asks single-glyph contexts.** With one glyph and "what comes next", the most available answer is the next member of whatever list the glyph belongs to. The caution about codepoint-seeded *kernels* (2-glyph contexts) is an extrapolation from this, not a test of it [inference].
- **Duplication is not a problem [measured].** There are 946 distinct (node, truth) pairs among the 1,056, answers per context have a median of 4, and truth-set size doesn't correlate with answer count ($\rho = 0.05$). METHODOLOGY's share-not-count concern doesn't bite here.

## 7. Smaller points

- **no-go §6 mislabels a ranker.** "Plain word overlap between names (no model at all, ties broken by codepoint) reaches hit@30 0.684". That 0.684 is `name>cp+num`, which includes the numeric bonus; `name>cp` is 0.701. Truly plain overlap with random ties is 0.645, and 0.594 on non-CJK, against 0.721 for minilm. On the hard stratum the embedding adds 7–13 points, more than "a little". The no-model ranker's strength at the top (hit@1 0.590 against 0.097 for plain names) comes from the codepoint tiebreak and the numeric bonus, not from the names.
- **`name_cp_scores`'s "tiebreak" isn't one across planes.** It adds $10^{-7}\cdot|\Delta cp|$, which reaches about 0.1 across planes. That is larger than many name-cosine gaps, so for distant candidates it acts as a soft codepoint prior. Small effect; worth a comment in `rankers.py`.
- **Two results hold by construction.** cp's cp-far hit@1 of about 0 holds by the definition of the stratum. Any `mix:cp|…` hit@1 equals cp's because cp is placed first. Neither is a measured property, though the README states the second as "at essentially no cost at the top (hit@1 unchanged…)".
- **Use of r012.** README's *Gaps* says "r012 was used only to define the universe and the never-shown list". But `series_ends.py` and `carry_test.py` analyse r012 answers, and §4 cites them.
- **Series ends.** `series_ends.py` flags many non-ends: `⑨ → ⑩`, `⒐ → ⒑`, `➈ → ➉`, where only the name template changes from DIGIT to NUMBER. The README's curated list is correct, but `Ⅻ → Ⅼ` (claude, n = 1) is also the next-larger single-glyph Roman numeral by value. `🄊 → 🄋` (nine → circled zero) is a plausible 0–9 wrap. Neither is unambiguous chart-following. Meanwhile `³ → ⁴` (12/12), `９ → ８`, `𝟿 → 𝟶` and `៩ → ១` show minds leaving the chart, which supports finding 1's narrower reading.
- **Untested models that are installed locally.** `ollama list` shows `embeddinggemma:300m`, `nomic-embed-text-v2-moe` and `qwen3-embedding:latest` (4.7 GB, the 8B). The no-go lists embeddinggemma as "gated, untested", but only its Hugging Face tokenizer is gated: the vector-collapse check could run through ollama directly. The 8B is the natural next point for "scale helps a little". I did not run these, since they are local-model runs.
- **Stale entries in result JSONs.** `derived/retrieval-*.json` accumulate keys across code versions (`old.update(res)`). `name+num` is no longer a valid spec, and `name`, `name>cp`, `emb:…0.6B__both` and `mix:cp|emb:bge-m3__glyph` are not in `run_all.sh`. I re-ran `name`, `name>cp`, `name>cp+num` and the two collapsed glyph embeddings into my scratchpad, and they reproduce the stored values exactly. Still, a file that mixes runs without provenance is a trap for the next reader.
- **Terminology.** The commit message and HANDOFF say "recall@30", but the tables report hit@30, meaning any truth in the top k. `eval_retrieval.py` computes both. With 1,038 of 1,056 contexts having a single truth they nearly coincide, but the names should match.
- **HANDOFF (outside the spike) mis-describes the carry test** as being "at the boundaries of UTF-8 byte-length ranges". It is at 64-code-point continuation-byte boundaries, which the README states correctly.
- **The spike's code still excludes `⟂ ⊥ ≈`.** Disclosed; harmless.

## What I checked and found sound

- **Tokenizer census:** `tok-census.json` matches the stated shares, and the vector-uniqueness counts reproduce (750 / 23,541; 5,019 / 18,013; Qwen 25,334 distinct).
- **Re-run retrieval rows:** they reproduce exactly.
- **Carry-test classification** (`cp − 63` as the carry-free wrap) is correct. The +1 rates (claude 10/35 against 11/33) are as stated.
- **Ranker exclusions and tie handling:** context and node glyphs are excluded from ranking, and random ties are used for embeddings. The earlier tiebreak artifact is correctly fixed and documented.
- **Sheet priming:** probe sheets that included an ASCII letter showed no higher chart rate on their non-ASCII items (answer rate 0.29 against 0.42; +1 among answered 0.85 against 0.74). This is small n, but there is no sign of priming.
- **Methodology boundaries:** the spike stayed within them. Nothing was written to `data/` or `harness/` (commit `cc05dc89` touches only the spike directory), and the compute overrun is disclosed plainly.
- **README recommendation 4** is the most useful idea in the spike, and I agree with it: in the continuation-first method the minds generate their own tendrils, so a cheap tendril is needed only to build kernels for unvisited glyphs.

## Feedback beyond the audit

- **Codepoint and Unicode names are the same source.** The two channels the spike recommends both draw on Unicode's own metadata, the allocation and the names. Kernels seeded from either will be confirmed most readily by minds that know that metadata, which is the measurement-validity worry of finding 1. The residue the spike identifies (emoji semantics, braille fills, box arcs, circle sizes) is reached by neither. If hot exploration is meant to find what Unicode does not already encode, it may want a share of kernels built from neither channel, for example by pairing glyphs across blocks at random and letting the minds' continuations do the work [inference].
- **"Beats codepoint" is a contaminated benchmark.** The spike says so in *Gaps*. The fix, scoring tendrils against edges that survive a chart-discriminating check, needs the tree's k\* and stability machinery, so it belongs with the study rather than this spike.

*I'm available for follow-up on any of these. The discriminator probe's raw answers are in my session scratchpad (`discrim/raw.jsonl`) if they're wanted here; I left them out because the request was for the report only.*
