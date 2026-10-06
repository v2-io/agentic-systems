# Spike: embeddings as tendrils (2026-10-05)

*Claude Opus 5.5, commissioned by the coordinating agent on Joseph's question. Joseph's plain-language summary is `debrief.md`. The demonstrated negatives, which he asked to have written up, are in `no-go.md`. This file is the full record. Nothing in the study's `data/` or `harness/` was written; harness modules were only imported, read-only.*

**Labels:** **[measured]** = computed here, with the script named. **[observed]** = read off examples, not counted. **[inference]** = my interpretation. **[partial]** = a run stopped before it finished.

## The question, and what it turned into

> *"each node that has any kind of edge reaching out with tendrils … probing the semantic network of LLMs … it might be meaningful to actually just use an embedding. Maybe not though, considering how poor local models seem to do with unicode."* — Joseph

As posed, the question was: do a glyph's neighbours in some embedding space predict the glyphs the frontier minds give as its sequence neighbours, better than codepoint order does? The use would be to steer the priority layer (concern 3); it would never be evidence.

Short answer [measured]:
- **Bare-glyph embeddings: no.** Most embedders can't even see most glyphs.
- **Embeddings of Unicode *names*: a little.** They add recall exactly where codepoint order fails, but plain name-word matching does nearly as well.
- **Codepoint order is far stronger than a "faint prior".** Part of the reason is a finding that matters beyond this spike (§4): when the minds don't know a glyph, they answer with the next code point.

## Reference sets: what "the minds' neighbours" means here

The spike uses three reference sets, each biased differently, because no single one is ground truth:

| set | what | size | known bias |
|---|---|---|---|
| **r011 first2** (headline) | Study what-comes-next / what-goes-between answers through r011. Per context, the glyphs that minds of **≥ 2 families** gave as their **first** choice. Between-items count for both gap neighbours. | 1,056 contexts | Contexts were built by the old planner, mostly along codepoint runs, so codepoint is favoured. |
| **survey** | The free surveys of 2026-08-25 (`data/surveys-v1/extracted`). Every consecutive pair a surveyor wrote, both directions. | 6,178 steps (1,360 written by ≥ 2 surveyors) | Surveyors swept Unicode *blocks*; claude and grok only. |
| **probe (fresh)** | **Prospective, made by this spike.** 135 glyphs never shown in the study (15 ASCII, 40 each of 2-, 3- and 4-byte; uniform within each byte-length stratum of the universe), each asked alone as a one-symbol what-comes-next item. The study's own sheet wording (`items.sheet_prompt`), sheets of 5, "none" offered. Minds: sonnet55, gemini38flash, grok46. Answers are in `probe/` only. | 135 glyphs, 100 with any first proposal | Small. Glyphs are sampled from the universe below, so ideographs are excluded. |

**Universe** ranked against: 25,362 glyphs. That is every assigned L/N/P/S code point in Unicode 16 (`derived/ucd16.json`, from Python 3.14), minus the large ideographic and syllabic repertoires (CJK unified, Hangul syllables, Tangut, Yi, cuneiform, Egyptian hieroglyphs, etc.), plus every glyph occurring in the study's data through r012. The study's old banned set `⟂ ⊥ ≈` is still excluded in `work/lib.py`. METHODOLOGY dropped that ban today, and it affects 3 glyphs.

**Metric.** For each context, rank the whole universe (context glyphs excluded) and find the best rank of any truth glyph. Reported are hit@k (some truth in the top k) and the share with rank 1. Strata:
- **cp-near**: some truth glyph is the node's ±1 code point.
- **cp-far**: otherwise. This is where a tendril other than codepoint could earn its keep.

## Rankers tried

- **cp**: codepoint distance, ties toward +1.
- **name**: Unicode-name word overlap.
- **name>cp+num**: name overlap, ties broken by codepoint distance, plus a bonus for Unicode numeric value ±1.
- **emb:MODEL__FORM**: cosine similarity, with three text forms:
  - **glyph**: the bare character;
  - **name**: the lower-cased Unicode name;
  - **both**.

  Models: all-minilm and bge-m3 (via ollama); Qwen3-Embedding 0.6B and 4B (sentence-transformers on MPS). Ties are broken at random, never by codepoint; a first draft did the latter and it inflated collapsed embeddings (see `work/rankers.py`).
- **llm:Qwen3-8B-node / -ctx**: a local LLM's next-glyph distribution after `Symbol sequence: <node>` or `Symbol sequence: <context>`, with byte tokens expanded into whole glyphs (`work/llm_next.py`). This one is directional and conditional, unlike any embedding.
- **mix:A|B**: A and B interleaved. Any one glyph's position is an upper bound, since duplicates are not removed.

## Results

### 1. Retrieval, r011 first2 [measured] (`work/eval_retrieval.py`, `derived/retrieval-r011-first2.json`)

Each cell gives hit@1 / hit@10 / hit@30.

| ranker | all (n = 1,056) | cp-far (n = 234) |
|---|---|---|
| cp | **0.740 / 0.854 / 0.894** | 0.013 / 0.342 / 0.521 |
| name>cp+num (no model) | 0.590 / 0.825 / 0.898 | 0.128 / 0.487 / 0.684 |
| emb all-minilm, name | 0.361 / 0.786 / 0.876 | 0.120 / **0.538 / 0.765** |
| emb bge-m3, name | 0.220 / 0.745 / 0.869 | 0.068 / 0.491 / 0.697 |
| emb Qwen3-Emb-0.6B, name | 0.189 / 0.711 / 0.843 | 0.107 / 0.436 / 0.654 |
| emb Qwen3-Emb-4B, glyph | 0.126 / 0.481 / 0.704 | 0.073 / 0.346 / 0.517 |
| emb Qwen3-Emb-0.6B, glyph | 0.079 / 0.372 / 0.586 | 0.081 / 0.278 / 0.457 |
| emb bge-m3, glyph | 0.078 / 0.172 / 0.271 | 0.043 / 0.145 / 0.244 |
| emb all-minilm, glyph | 0.012 / 0.023 / 0.032 | 0.026 / 0.051 / 0.068 |
| llm Qwen3-8B, node only | 0.129 / 0.704 / 0.835 | 0.060 / 0.346 / 0.585 |
| **mix cp \| all-minilm name** | **0.740 / 0.883 / 0.943** | 0.013 / 0.470 / 0.744 |
| mix cp \| name>cp+num | 0.740 / 0.884 / 0.926 | 0.013 / 0.474 / 0.667 |

The same ordering holds on the **survey** set (`--gt survey --truth first1`, n = 6,178, 1,758 cp-far):

| ranker | all | cp-far |
|---|---|---|
| cp | 0.634 / 0.803 / 0.855 | 0.005 / 0.309 / 0.490 |
| name>cp+num | 0.549 / 0.803 / 0.886 | 0.181 / 0.506 / 0.684 |
| all-minilm name | 0.368 / 0.773 / 0.861 | 0.137 / 0.536 / 0.721 |
| mix cp \| all-minilm name | 0.634 / 0.855 / **0.920** | 0.005 / 0.492 / 0.718 |

The same ordering holds on the **fresh probe** (`--gt probe --truth first1`, n = 100: 86 cp-near, 14 cp-far):

| ranker | hit@1 / hit@10 |
|---|---|
| cp | **0.84 / 0.94** |
| name>cp+num | 0.13 / 0.67 |
| all-minilm name | 0.13 / 0.46 |
| Qwen3-Emb-0.6B glyph | 0.08 / 0.25 |
| Qwen3-Emb-4B glyph | 0.07 / 0.28 |
| bge-m3 glyph | 0.01 / 0.09 |

Of the 14 cp-far probe glyphs, cp found 8 within its top 10 and the name methods 6. That is too few to rank them. Requiring a proposal agreed by ≥ 2 families (`--truth any2`, n = 52) gives the same picture.

**Context-aware local LLM [partial]** (`--only-in Qwen3-8B-ctx-r011`). The run was stopped at Joseph's request (see *Compute* below). The 184 contexts it covers are the earliest in file order, so this is **not a random sample** and the subset is harder for cp: cp hit@1 is 0.571 here against 0.740 overall. Cells are hit@1 / hit@10 / hit@30:

| ranker | all (n = 184) | cp-far (n = 59) |
|---|---|---|
| cp | 0.571 / 0.755 / 0.810 | 0.000 / 0.237 / 0.407 |
| name>cp+num | 0.440 / 0.750 / 0.848 | **0.186 / 0.542 / 0.695** |
| llm Qwen3-8B, context | 0.451 / 0.739 / 0.859 | **0.203** / 0.458 / 0.661 |
| mix cp \| llm context | 0.571 / 0.815 / 0.880 | 0.000 / 0.424 / 0.627 |
| mix cp \| all-minilm name | 0.571 / 0.804 / 0.880 | 0.000 / 0.390 / 0.627 |

On this subset, the context-aware LLM is the only cheap-to-query method roughly level with name matching where codepoint fails. It is not cheap to *run*: about an hour of GPU for under a thousand contexts on this machine.

### 2. Which kinds of glyphs [measured] (`work/breakdown.py`, hit@10, r011 first2)

| node kind | n | cp | name>cp+num | all-minilm name | Qwen-0.6B glyph | mix cp \| minilm name |
|---|---|---|---|---|---|---|
| numerals (N*) | 496 | 0.94 | 0.94 | 0.97 | 0.42 | 0.97 |
| other symbols (S*) | 233 | 0.90 | 0.80 | 0.67 | 0.30 | 0.89 |
| emoji and pictographs | 155 | 0.74 | 0.66 | 0.71 | 0.40 | 0.80 |
| letters (L*) | 104 | 0.63 | 0.68 | 0.44 | 0.35 | 0.65 |
| box, block, shape, braille | 46 | 0.74 | 0.70 | 0.52 | 0.30 | 0.80 |
| punctuation (P*) | 22 | 0.45 | 0.45 | 0.59 | 0.14 | 0.68 |

### 3. What codepoint misses, and why [measured + observed] (`work/classify_far.py`)

Of the 251 agreed first-choice neighbours more than one code point away (r011):

| relation | share | examples |
|---|---|---|
| Unicode names differ in one word | 55% | `⑳ → ㉑`, `③ ② ① → ⓪` |
| same block, names differ more | 28% | `Ⅰ ⅱ → Ⅲ`, `↖ ↑ → ↗`, `🏿 🏽 → 🏻` |
| other block, no shared name word | 7% | `🐓 🐤 🐣 → 🥚`, `‱ ‰ → %` |
| name with one word added | 6% | `■ → ◼`, `⑱ ⑲ ⑳ → ㉑` |
| other block, a shared name word | 4% | |

The 55% figure is inflated by two kinds of match. CJK ideographs' names differ only in their hex number, and emoji named "... FACE" match on that one word. Both are semantic matches dressed as name matches.

The survey set gives 37% / 31% / 16% / 9% / 7% for the same classes. What's left after cp plus names is semantic or visual:
- emoji (faces, vehicles, weather);
- CJK numerals and magnitudes (`十 百 千 万 億`);
- circle sizes, braille fills, box-drawing arcs.

### 4. Codepoint order leaks into the minds' answers [measured]

This is the finding with the widest reach.

**Fresh glyphs get code-chart answers.** On the fresh probe, when a mind proposes anything, its first proposal is the next code point 78% (claude), 79% (gemini) and 88% (grok) of the time (`work/family_cp.py`). Examples:
- `𐲇` OLD HUNGARIAN CAPITAL LETTER ED → `𐲈 𐲉 𐲊`;
- `🛊` GIRLS SYMBOL → `🛋 🛌 🛍` (couch, bed, shopping bags);
- `❵` MEDIUM RIGHT CURLY BRACKET ORNAMENT → `❶ ❷ ❸`;
- `𓄿` EGYPTIAN HIEROGLYPH G001 → `𓅀` (carry probe).

That is the code chart, not anything one could call perceiving those glyphs.

**The families differ in how often they answer** (`work/probe_strata.py`), not in what they answer:

| family | 4-byte glyphs answered | first proposal ±1 code point |
|---|---|---|
| claude | 60% | 57% |
| gemini | 35% | 30% |
| grok | 5% | 5% |

**Not a naive byte increment** (`work/carry_eval.py`, `probe-carry/`). In UTF-8, the code point after U+…3F needs a carry into an earlier byte. Thirty-five obscure letters at such boundaries (cp % 64 = 63) were compared with 33 mid-run controls from the same blocks. The +1 rates match: claude 0.29 against 0.33, gemini 0.14 against 0.18. **No** mind ever proposed the carry-free wrap (cp − 63). So the minds' successor answers come from knowing the chart, or from computing it correctly, not from incrementing a final byte [measured; n is small].

**At the end of a series the minds usually leave the chart correctly, but not always** (`work/series_ends.py`, r012 data):
- Correct: `⑳ → ㉑` (6/6 first proposals, all families), `³ → ⁴`, `⁹ → ⁸`, `Ⅿ → Ⅾ`.
- Follows the chart where the series has ended:
  - `Ⅻ → Ⅼ` (fifty) and `ⅻ → ⅼ` (claude);
  - `⚅` DIE FACE-6 → `⚆` WHITE CIRCLE WITH DOT RIGHT (claude);
  - `𝟡 → 𝟢` (double-struck nine → sans-serif zero, claude);
  - `🄊` DIGIT NINE COMMA → `🄋` (all families).

  The old pipeline's grown rows show the same thing: `ⅱ … ⅻ ⅼ` and `㈠ … ㈨ ㈪` in `data/standings/r011.md`.

[inference] Codepoint order is therefore not only Unicode's allocation, a scaffold outside the minds. It is also a **behaviour of the minds**, and family-dependent. That matters to concern 1 (probing validity) more than to this spike. If hot exploration seeds kernels from codepoint neighbours, it will mostly harvest the code charts of scripts the minds don't know, and those answers will be confirmed, by claude and gemini more than grok.

### 5. Triads [measured] (`work/eval_triads.py`)

**Middle prediction** (1,316 triads with a consensus middle; chance = 0.33):

| ranker | accuracy |
|---|---|
| cp (median code point) | **0.797** |
| name>cp+num | 0.755 |
| all-minilm name | 0.547 |
| bge-m3 glyph | 0.514 |
| Qwen-0.6B glyph | 0.467 |

**Yield**: does the triad's coherence predict that ≥ 2 families order it? (ROC AUC, 2,198 triads)

| ranker | AUC |
|---|---|
| cp | **0.792** |
| all-minilm name | 0.758 |
| Qwen-0.6B name | 0.731 |
| name>cp+num | 0.691 |

On the old planner's exploration triads (n = 205), every ranker sits at 0.84–0.85. On truly random "tail" triads, only 9 of 127 were ordered, too few to tell anything apart.

### 6. Joseph's line and axis hypotheses: no → `no-go.md`

The tests were:
- extrapolating along the line through two members, the parallelogram step, and a context's own mean step or first principal component;
- ordering a known set along its own best-fit axis;
- learning a linear view from the minds' answers and testing it on unseen Unicode blocks.

Each was compared with plain nearest-neighbour and with codepoint. None helps [measured]. Steps along perceived sequences are about as uncorrelated as steps between random glyphs: cos ≈ −0.4 against −0.5. The details and their scope are in `no-go.md`.

## What I'd suggest for the priority layer [inference, from the above]

1. **Keep codepoint as the base tendril, but tag it.** It is the best single predictor in every set. Because minds answer chart-order for glyphs they don't know (§4), an edge that is exactly ±1 code point on an unfamiliar script is weak evidence of perception. The study may want that recorded as its own tag (concern 1), and exploration may want to *spend less* on pure codepoint kernels, not more.
2. **Add Unicode-name siblings as a second channel, interleaved with codepoint.** It needs no model: name-word overlap plus a numeric-value ±1 bonus (`work/rankers.py: name_num_scores`). If an embedding is wanted anyway, a tiny one (all-minilm, 384-d) on the *names*, never the glyphs, adds a few points more where codepoint fails (cp-far hit@30 0.765 against 0.684). Interleaved, cp plus names lifts hit@30 on cp-far contexts from 0.52 to 0.67–0.74, at essentially no cost at the top (hit@1 unchanged, hit@3 0.807 against 0.808).
3. **Don't embed bare glyphs.** BERT- and XLM-R-family tokenizers map 71–93% of symbols to `[UNK]`. Byte-level embedders see every glyph but don't place sequence neighbours together (`no-go.md`).
4. **The well-formed question underneath.** In the continuation-first method (§4 of METHODOLOGY), the minds write their own continuations, so they generate their own tendrils for any node that's asked. A cheap tendril is needed only to *build contexts* for unvisited glyphs: a 2-glyph kernel, or the members of a triad or order check. For that, codepoint plus name siblings is enough, and the real exposure is the codepoint leak in §4. A local LLM with context is the only cheap proxy that tracks the minds' semantic jumps (emoji, words), and it costs GPU-hours.

## Compute (for the record)

What ran, in order:
1. **ollama embeddings**: all-minilm and bge-m3, 25k glyphs × 2 forms. ollama's `/api/embed` ran at about 25 texts/s, so bge-m3 took about 15 min per form.
2. **sentence-transformers on MPS**: Qwen3-Embedding 0.6B and 4B, about 3–4 min per form.
3. **Qwen3-8B on MPS**: node mode 29 min; context mode stopped part-way. This was the heavy part. Joseph saw the machine running hot for about an hour.
4. **Frontier calls for the two probes**: 41 sheets × 3 minds = 123 calls.

The local-LLM comparator went beyond the commission's "quick embedding" intent. It was my call, and I should have asked before starting a long GPU job. Everything was stopped on Joseph's message. Not run as a result:
- the 4B *name* form;
- the LLM on the fresh probe;
- the rest of the context-mode LLM.

## Gaps and things not done

- **Unihan definitions** (e.g. `kDefinition`, `kPrimaryNumeric`) would give CJK numerals a meaningful "name". Not tried.
- **embeddinggemma**: gated, untested. nomic-embed-text-v2-moe: untested.
- **Context-aware LLM**: partial, non-random subset (above).
- **Fresh probe**: 135 glyphs, one pass, one mind per family. The carry probe: 68 glyphs.
- **Ground truth is plural on purpose.** All three sets carry the minds' codepoint habit (§4), so "beats codepoint" is a high bar partly because the truth itself is codepoint-shaped.
- **No fitting.** The rankers have no fitted parameters except the learned probe in `no-go.md` §5. So no train/test split was needed, and r012 was used only to define the universe and the never-shown list.

## Files

- **`debrief.md`**: for Joseph. **`no-go.md`**: the demonstrated negatives.
- **`work/`**: all code. `run_all.sh` lists every step in the order run, with what was stopped.
  - Data: `extract.py`, `gt.py`, `gt_survey.py`, `probe.py`.
  - Rankers: `rankers.py`, `embed.py`, `embed_hf.py`, `llm_next.py`.
  - Evaluations: `eval_retrieval.py`, `eval_triads.py`, `eval_lines.py`, `eval_axis.py`, `probe_linear.py`.
  - Analyses: `tok_census.py`, `classify_far.py`, `family_cp.py`, `probe_strata.py`, `carry_eval.py`, `carry_test.py`, `series_ends.py`, `breakdown.py`.
- **`derived/`**: everything computed.
  - Extracted answers and reference sets: `answers-*.jsonl`, `gt-*.json`.
  - Inputs: `ucd16.json`, `Blocks-16.txt`, embeddings under `emb/` (large `.npy`; regenerable, so you may prefer not to commit them), LLM lists under `llm/`.
  - Result JSONs: `retrieval-*.json`, `triads-*.json`, `lines-*.json`, `axis.json`, `probe-linear.json`, `tok-census.json`.
- **`probe/`, `probe-carry/`**: this spike's frontier answers (raw ledgers with prompts) and the sampled glyphs.
- **`logs/`**: run logs.
