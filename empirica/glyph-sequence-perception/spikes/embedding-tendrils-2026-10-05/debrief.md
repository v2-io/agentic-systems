# Debrief: glyphs and embeddings

*Joseph, this is what turned out to be true, in plain terms. The numbers and how they were obtained are in `README.md`. The negative results you asked to have written up are in `no-go.md`. Each finding below is labelled with how I know it.*

**1. Most embedding models never see the glyph.** *(measured)*

Before any training comes in, the tokenizer decides. For the BERT-style embedders on this machine (all-minilm, nomic-embed-text, mxbai and bge-large), **93%** of the 25,000 symbols I tested become the same "unknown" token. For the multilingual XLM-R ones (bge-m3, paraphrase-multilingual, snowflake-arctic-embed2) it's **71%**. In all-minilm, 23,541 different glyphs come out as one identical vector.

So "local models do poorly with Unicode" is, for these models, literally true at the front door. Only byte-level models (the Qwen3-Embedding family, granite-embedding) see every glyph, and even they place sequence neighbours poorly. The 4B is somewhat better than the 0.6B, and both are far behind plain codepoint order.

**2. What these models do know about a glyph is its name.** *(measured)*

Embedding the Unicode name ("circled number twenty one") rather than the glyph works much better. But simply matching the words of the names, with no model at all, does almost as well. The signal is in the names, which people wrote; the embedding adds a little on top.

Names help exactly where codepoint order breaks: a series that continues in another Unicode block. `⑳` is followed by `㉑` thousands of code points away, `³` by `⁴`, and `⓪` sits far from `①`.

**3. Your line and axis idea: I tested it, and it doesn't hold in these spaces.** *(measured)*

The tests were:
- a line through two members of a sequence;
- the "parallelogram" step;
- extrapolating along the best-fit axis of a handful of known members;
- ordering a known set along its own best-fit axis;
- training a linear view on the minds' own answers and testing it on unseen Unicode blocks.

None of these beat plain nearest-neighbour, and none came close to codepoint order. The clearest sign is geometric. Walking along a sequence the minds agree on, each step points in a direction almost unrelated to the previous step: about as unrelated as steps between random glyphs. Sequences are not lines in these spaces. So the hypothesis came out false, at least for the models tested. `no-go.md` has the scope; one model architecture and about 7,000 training pairs don't exclude everything.

**4. Codepoint order is not a faint prior. It is the strongest single predictor I found, and part of that is the minds themselves.** *(measured)*

- **Study answers.** Where minds of two or more families agree on what comes next, it's the adjacent code point 74% of the time.
- **Fresh glyphs.** I showed 135 glyphs the study had never used, one at a time, to Sonnet, Gemini and Grok, in the study's own wording. When they answered at all, they gave the next code point about 80% of the time. That includes glyphs nobody could be said to perceive as a sequence:
  - an Egyptian hieroglyph "followed by" the next hieroglyph in the chart;
  - GIRLS SYMBOL `🛊` "followed by" couch, bed and shopping bags `🛋 🛌 🛍`;
  - a curly-bracket ornament `❵` "followed by" `❶ ❷ ❸`.

  They are reading the Unicode chart.
- **Not a tokenizer trick.** At UTF-8 byte boundaries, they still give the correct next code point and never the naive byte wrap-around (a small test of 68 glyphs).
- **The families differ in willingness, not in kind.** For the obscurest glyphs, Claude answers chart-order about 57% of the time, Gemini about 30%, and Grok almost always says "none" (5%).
- **At the end of a well-known series the minds leave the chart correctly** (`⑳ → ㉑`, every family). At less-known ends they follow it: `Ⅻ` → `Ⅼ` (fifty), and the sixth die face `⚅` → a circle with a dot `⚆`.

*(inference)* This matters for the study beyond embeddings. A "sequence" the minds confirm on an unfamiliar script may be knowledge of Unicode's tables rather than perception of the glyphs. And it is family-dependent. If exploration seeds kernels from codepoint neighbours, it will mostly harvest code charts, and Claude and Gemini will confirm them.

**5. What I'd use for choosing what to probe.** *(inference from 1–4)*

- **Codepoint neighbours, tagged.** They are the base tendril; tag them so chart-order answers can be weighed separately.
- **Unicode-name siblings, interleaved with codepoint.** This needs no model. Together they find 67–74% of the cases codepoint misses within the top 30, against 52% for codepoint alone, and lose essentially nothing at the top.
- **No embeddings of bare glyphs.**
- **A local LLM given the context, if semantic jumps matter.** Faces, vehicles, an egg after a hatching chick: a local LLM is the only cheap stand-in I found that follows those, but it costs GPU-hours. That is what heated the machine, not the embedding models.

What remains after codepoint and names is semantic or visual: emoji, CJK numerals, circle sizes, braille fills. That is the part only the minds themselves will find.
