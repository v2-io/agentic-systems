# No-go results: glyph embeddings, lines and axes

*Spike `embedding-tendrils-2026-10-05`, written at Joseph's request (mid-spike, 2026-10-05): "Be sure and write up the no-go results if my hypotheses are wrong … It's important information about the unicode training on these embed models." Every number below was produced by a script in `work/` and can be regenerated with the command named next to it. Labels: **[measured]** = computed here from data; **[observed]** = read off examples, not counted; **[inference]** = my explanation of a measurement, not itself measured.*

The reference set everywhere, unless stated otherwise, is "r011 first2". It holds the study's what-comes-next and what-goes-between answers through r011, restricted to a glyph that minds of **two or more families** gave as their **first** choice: 1,056 contexts. The universe ranked against is 25,362 glyphs: every assigned L/N/P/S code point in Unicode 16, minus the large ideographic and syllabic repertoires, plus every glyph that occurs in the study's data. The details are in `README.md`.

---

## 1. Most embedding models cannot see most glyphs at all [measured]

A glyph that tokenizes to `[UNK]` gets the same input as every other unknown glyph, so no embedding of the bare glyph can place it anywhere in particular. This is a property of the tokenizer, settled before any training could help. `work/tok_census.py` → `derived/tok-census.json`:

| tokenizer family | models (ollama names) | glyphs → `[UNK]` |
|---|---|---|
| BERT WordPiece | all-minilm; nomic-embed-text v1.5; bge-large, used as the proxy for mxbai-embed-large | **93%** |
| XLM-RoBERTa SentencePiece | bge-m3; paraphrase-multilingual; snowflake-arctic-embed2 | **71%** |
| byte-level BPE | Qwen3-Embedding (0.6B, 4B, 8B), granite-embedding | 0% (every glyph is visible, as 1–4 byte pieces) |

Not checked: embeddinggemma (its tokenizer is gated on Hugging Face) and nomic-embed-text-v2-moe. The proxies are named as such above.

The collapse shows in the vectors themselves, not only the tokenizers [measured]:
- **all-minilm**: the 25,362 glyphs produce only 750 distinct vectors. One vector is shared by **23,541** glyphs.
- **bge-m3**: 5,019 distinct vectors. One is shared by **18,013** glyphs.

Joseph's remark that "local models do poorly with unicode" is literally true at the input layer for every BERT- and XLM-R-based embedder on this machine.

## 2. Where glyphs are visible, their embeddings still don't place sequence neighbours near each other [measured]

The question asked of each glyph `q` is where the minds' agreed next glyph lands when the universe is ranked by similarity to `q`. Context glyphs are excluded, and ties are broken at random. (A first draft broke ties by codepoint, which let a collapsed embedding borrow codepoint's skill. That artifact was caught and removed: `work/rankers.py`, header note.)

| ranker (r011 first2, n = 1,056) | hit@1 | hit@10 | hit@30 |
|---|---|---|---|
| codepoint distance | **0.740** | **0.854** | **0.894** |
| Qwen3-Embedding-4B, bare glyph | 0.126 | 0.481 | 0.704 |
| Qwen3-Embedding-0.6B, bare glyph | 0.079 | 0.372 | 0.586 |
| bge-m3, bare glyph | 0.078 | 0.172 | 0.271 |
| all-minilm, bare glyph | 0.012 | 0.023 | 0.032 |

`work/eval_retrieval.py cp emb:…` → `derived/retrieval-r011-first2.json`.

**Scale helps a little, but not enough to matter.** Going from Qwen3-Embedding-0.6B to 4B lifts the bare glyph from hit@10 0.37 to 0.48. The 4B model is still far below codepoint order, and below a tiny model embedding the glyph's *name*: all-minilm on names reaches 0.786.

The embeddings also don't win on the 234 contexts where the agreed next glyph is *not* a codepoint neighbour, the cases an embedding was hoped to rescue. At hit@10:

| ranker | hit@10 |
|---|---|
| codepoint | 0.342 |
| Qwen3-Embedding-4B (glyph) | 0.346 |
| Qwen3-Embedding-0.6B (glyph) | 0.278 |
| bge-m3 (glyph) | 0.145 |

The same ordering holds on two other reference sets:
- **The free surveys of 2026-08-25**: 6,178 written steps.
- **A prospective probe**: 135 never-shown glyphs, put to sonnet55, gemini38flash and grok46 in the study's own sheet wording.

On the prospective probe (hit@1):

| ranker | hit@1 |
|---|---|
| codepoint | 0.84 |
| Qwen3-Embedding-0.6B (glyph) | 0.08 |
| Qwen3-Embedding-4B (glyph) | 0.07 |
| bge-m3 (glyph) | 0.01 |

## 3. Joseph's line hypothesis: "a line through any two code points … intersects with other code-points" — no [measured]

`work/eval_lines.py` → `derived/lines-r011-first2.json`. For the 957 contexts with at least two glyphs (`… p q → next`), the universe was ranked by five methods:

- **nn**: plain cosine to `q`.
- **offset**: cosine to `q + (q − p)`, the analogy or parallelogram step.
- **line**: distance to the ray `q + s(q − p)` for s in [0.5, 3], i.e. a line through the two glyphs, ahead of `q`.
- **meanstep**: cosine to `q` plus the mean step of the whole context (contexts of 3 or more glyphs, so "a handful of known ones").
- **pc1**: one step along the context's own first principal component.

**Offset and line score below plain nearest-neighbour in every space and text form tested.** Meanstep and pc1 can only be measured on the 670 contexts with 3 or more glyphs. They are below nearest-neighbour everywhere except all-minilm on names, where meanstep is within about one point of it. Hit@10:

| space | nn | offset | line | meanstep | pc1 |
|---|---|---|---|---|---|
| all-minilm, name | 0.795 | 0.750 | 0.773 | 0.807* | 0.794* |
| bge-m3, name | 0.754 | 0.413 | 0.577 | 0.636* | 0.628* |
| Qwen3-Emb-0.6B, name | 0.716 | 0.474 | 0.588 | 0.630* | 0.604* |
| Qwen3-Emb-0.6B, glyph | 0.380 | 0.223 | 0.287 | 0.322* | 0.303* |
| *codepoint, for comparison* | 0.871 (cp) | 0.819 (cp-offset, `2q − p`) | | | |

\* Measured on the 670-context subset with 3 or more glyphs, so not strictly comparable with the column to its left. The one cell above nn (all-minilm meanstep 0.807) is within the noise of that subset change.

**Why the line fails** [measured]: the direct geometry check. Along agreed paths `a b c`, the cosine between the step vectors `(b − a)` and `(c − b)` is about −0.39 to −0.45 in every space. A straight line would give +1. Random glyph triples give −0.49 to −0.50 in the same spaces (for bge-m3 glyph, −0.25 against −0.26, because of the collapse). So perceived sequences are barely straighter than random triples. Each step mostly points back toward the cloud the glyphs sit in, not onward.

## 4. The axis hypothesis: "those codepoints ordering on that axis would be the sequence order" — weak at best [measured]

`work/eval_axis.py` → `derived/axis.json`. The test takes sets that minds themselves ordered:
- **409 survey sequences** of 4 or more glyphs;
- **573 order answers**: a scrambled set put into a single line identically, up to reversal, by two or more families.

Each set's members were projected on the set's *own* first principal component. That is the most favourable version of the hypothesis, because the axis is fitted to the very glyphs it must order. The resulting order was compared to the minds' order by |Spearman ρ| (direction is free).

| space | survey: PC1 | survey: codepoint | survey: random order | order answers: PC1 | order answers: codepoint | order answers: random order |
|---|---|---|---|---|---|---|
| all-minilm, name | 0.642 | **0.855** | 0.366 | 0.671 | **0.891** | 0.420 |
| bge-m3, name | 0.655 | 0.855 | 0.365 | 0.665 | 0.891 | 0.392 |
| Qwen3-Emb-0.6B, name | 0.551 | 0.855 | 0.385 | 0.573 | 0.891 | 0.391 |
| Qwen3-Emb-0.6B, glyph | 0.560 | 0.855 | 0.372 | 0.557 | 0.891 | 0.397 |
| bge-m3, glyph | 0.503 | 0.855 | 0.380 | 0.601 | 0.891 | 0.400 |

- **Above chance, far below codepoint.** The fitted axis orders sets better than chance, but far worse than plain codepoint order. It beats codepoint on only 9–16% of sets.
- **No advantage where codepoint fails.** On the sets where codepoint order is itself wrong (|ρ| < 0.9; 113 survey sets, 107 order sets), PC1 reaches |ρ| ≈ 0.49–0.67. That is about where it sits everywhere, so the axis gives no special purchase on exactly the cases where it was needed.
- **Sequences are not lines.** The share of a set's variance on its PC1 equals that of random same-size sets drawn from the same Unicode blocks (e.g. 0.424 against 0.402, and 0.426 against 0.431). The minds' sequences are no more line-like in these spaces than any handful of glyphs from the same block.

A first draft reported bge-m3 glyph PC1 at 0.76. That came from a stable sort keeping tied (collapsed) vectors in their listed order, which is the true order. Ties are now broken at random, and the draft figure is void.

## 5. Strengthening attempt: a *learned* linear view, trained on the minds' answers — also no [measured]

The raw spaces might not hold sequences on lines, while some linear projection of them would. To test that, `work/probe_linear.py` learns a rank-64 bilinear successor score, `s(q, x) = (A e_q)·(B e_x)`, by softmax over the whole universe:
- **Training data**: 6,842 node → first-proposal pairs, from r011 plus the surveys.
- **Test**: held-out **Unicode blocks** (5-fold split by the node's block), so the probe has to generalize to regions it never saw, as tendrils would.

On all-minilm name embeddings (held-out hit@10):

| model | hit@10 |
|---|---|
| plain nearest-neighbour | 0.786 |
| learned, from scratch | 0.342 |
| learned as a residual on nearest-neighbour, 150 steps | 0.598 |
| learned as a residual on nearest-neighbour, 600 steps | 0.402 |
| *codepoint* | *0.854* |

**More training makes held-out blocks worse.** What the probe learns is block-specific and does not transfer. *Scope of this no-go:* it covers one architecture (low-rank bilinear), one embedding, and about 7k training pairs. A non-linear model, or far more data, is not excluded by it [inference: the falling held-out curve suggests the transferable signal in these spaces is small, but that is not proven].

## 6. What did carry signal, for contrast [measured]

The useful information in the "name" embeddings is the **Unicode name**, not the glyph. On the 234 codepoint-far contexts, plain word overlap between names (no model at all, ties broken by codepoint) reaches hit@30 0.684; all-minilm on names reaches 0.765. So the embedding adds a little on top of the names' own words, and the names do most of the work. Details are in `README.md`.

## What this means for the embed models' Unicode training [inference]

- **A tokenizer floor.** For BERT- and XLM-R-family embedders, most symbols never reach the network. Training can't fix that, and nothing downstream should be read as "the model's view of the glyph".
- **A different objective.** Byte-level embedders (Qwen3-Embedding) see every glyph, but their training rewards *text* similarity between passages. That gives no reason for `②` to sit "between" `①` and `③`, or for steps along a sequence to be parallel, and the measurements show neither.
- **The words carry it.** Descriptions of glyphs in words (Unicode names) are what these models were trained on, and that is where the sequence signal lives for them.
