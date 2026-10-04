# Plan — running the study's discovery loop for inter-family glyph intuition in LLMs

*2026-10-04, revised the same day. Claude Opus 5.5, at Joseph's request.*

*This is the current plan. It replaces the morning version (history: `04-joseph-questions.md`).*

*Earlier stages, kept as the record of how the view moved:*

- *`01-view-before-top.md`*
- *`02-after-v1-record.md`*
- *`03-after-top40.md`*

---

## 0. The object, in Joseph's words

> *"What unicode says is irrelevant, what ghostty or any typefaces say is irrelevant. I'm *still* simply asking you to figure out is inter-family intuition from LLMs."*

The object is the order LLM minds perceive among glyphs, **across glyph families as well as within them**, and how far that order is shared across LLM families.

- **Defined only by LLM answers.** No Unicode property (numeric value, name, block, codepoint) and no rendering measurement (ink, any typeface) is a reference, a feature, or an input channel. Unicode is used only to *enumerate* candidate glyphs.
- **Agreement across LLM families is the evidence.** It is what shows an ordering is an intuition rather than one model's quirk.
- **The co-equal object is unchanged.** How the measurement format and context add or remove order stays in scope as its own arm (§6).

"Round out the data" meant **the study's own recycling discovery loop** (`pilot/DESIGN-scale-up.md` §The loop). This plan is that loop, specified so that it cannot fall into the v1.0 failure mode. §1 says what that failure was.

## 1. What has to be different from v1.0

v1.0 asked about **1,885 distinct pairs over 1,406 glyphs**:

- That is **0.19%** of the possible pairs.
- The **median glyph was compared with 2 others**, and 59% with 2 or fewer.

The glyphs that carry the most magnitude were removed: every glyph used in any pilot stimulus (1,246 characters) and all ASCII, as held-out hygiene for a confirmation run.

The mixing that remained was random:

- **Uniform tail:** 286 of its 400 glyphs are letters of scripts.
- **"Seed-cross":** one glyph from each of three random records, out of hundreds spanning all of Unicode.

Random pairs almost never land on related families, so ⟂ correctly swallowed them. The informative middle, neighbouring families, was never sampled. The top-40 battery tested only adjacent steps of exact survey strings.

**Same-value pairs across dresses were essentially never asked.** Of the 1,885 pairs, three are same-value numeral pairs, and none of them sets two dresses of one digit against each other (counts in `04-joseph-questions.md`).

So the loop is specified around five requirements:

1. **No held-out exclusion during discovery.** Every survey glyph, every pilot glyph, ASCII, and every proposed rung is in the pool. Held-out pools belong to a later confirmation, if there is one.
2. **Density.** Each glyph in the active pool reaches **≥ 15 comparisons** before its place is read. The pilot's walks reached about 8; v1.0 reached 2.
3. **Neighbourhood-driven mixing.** Most comparisons go to glyphs that some mind has already related to it: a non-⟂ edge, a shared continuation proposal, or membership in the same generator lattice. A glyph's neighbourhood is what the minds say it is, never a block or a family label. Cross-family pairs are therefore the bulk, not the exception.
4. **The long tail never closes.** A fixed share of each round stays uniform, so discovery is never bounded by what is already known.
5. **Each mind's own arrangement is the datum.** No surveyor's string, and no Unicode order, is ever the reference.

## 2. The loop

Each round runs in this order:

1. **Walk.** Draw triads by fated mixture sampling:
   - **~60%** neighbourhood densification: within k hops in the current consensus graph, across loci;
   - **~25%** seed- or record-local;
   - **~15%** uniform tail.

   These are the pilot's walk2 proportions. Each triad is shown as its three pairs in both orders, with ⟂, ≈ and graded "more" available (the pilot's response set). Contested edges get ≥ 3 repetitions.
2. **Poset store.**
   - **Truth:** an append-only JSONL ledger per round.
   - **Index:** Postgres 18 (`psql-18`), as Joseph ruled.
   - **Contents:** per-mind directed edges kept only when both presentation orders agree; ⟂ boundaries; ≈ clusters, kept raw (≈ is not transitive); and a family-weighted consensus graph.
   - **Transitivity:** measured on order-stable edges only. The cyclic triad unit cannot otherwise tell cycles from slot preference.
3. **Frontier continuation.** Articulation-free continuation agents ("continue what it's doing; it may have no name; or decline") work at the ends of consensus chains and in the gaps between them. Proposals enter the pool with a lineage label.
4. **Salting.** Proposed rungs are validated by blind lookalike distractors placed at fated positions. This also covers the ambiguity raised in `03-after-top40.md`: a run a mind may simply have memorized as an alphabet is exposed when one rung is swapped for a lookalike.
5. **Accepted rungs re-enter the walk pool.**
6. **Emitted sequences go to whole-set reconstruction.**
   - **Each mind's own arrangement is the result,** reported with its partition (what went to EXTRA) and its coverage.
   - **Holistic candidates** (ordered as a set but not as pairs) go to length-graded continuation, which gives each one's onset length.
7. **Generator lattices are objects.** The pilot named braille, quadrants, sextants, hexagrams and the star weight × points grid. The digit dresses form one too: dress × value, sampled as a product grid, never as separate strings. Chains are sampled from each lattice, so the relation *between* parallel families is measured directly.

**Stop:** K consecutive rounds with no newly accepted rung. The uniform share keeps running throughout.

## 3. Panel per round

One mind per LLM family where possible:

- a Claude model (rotate Haiku, Sonnet and Opus across rounds);
- a Gemini;
- Grok;
- the local models.

Gemini is rate-limited and Codex returns on Nov 2, so the OpenAI frontier model joins after that. gpt-oss-20b is meanwhile the OpenAI-family entry, if it can be loaded.

Small models answer pairs mostly by slot. They join through answer log-probabilities in both orders if ollama or llama.cpp exposes them (unverified; a one-hour check), and otherwise are reported as a separate tier.

Sheet mode with both orders split across sheets for every mind, as in v1.0. Sheet pairing becomes a factor only in §6.

## 4. Seeds

Intake is every record in all seven surveys:

- 849 sequence records;
- 207 negatives;
- 13 generators;
- 12 equivalences, including `①⑴⒈`, the same-value-different-dress question Joseph is now asking;
- 27 morphs, 11 cyclic records and 12 questions.

Reading the files:

- **Field names.** Read `type` or `record_type`.
- **Surveyor label.** Normalize it (sonnet-survey-3's extraction says `sonnet-3`).
- **No filtering.** No strength or concordance filter. SEED-PRIORITY may order the first rounds' resources, as Joseph intended: seeds are loci, never data.

## 5. What the loop reports

- **The consensus graph.** Nodes are glyphs and edges are inter-mind-agreed orders. For each edge: the share of LLM families for which it holds, the smallest model for which it holds, and the ⟂ rate beside it.
- **Chains.** Maximal paths in that graph. A chain's universality is that of its weakest link.
- **Inter-family structure.** For each generator lattice, whether one family dimension orders consistently across the other dimension (dress order at every value), and whether a family step ever outweighs a value step. This is the direct form of Joseph's ①/⑴/❶/🯱 question.
- **Where minds agree with each other against the surveyor** (the `nɳɲŋ` pattern).
- **A generic order on arbitrary glyphs.** Noise sets drew the same order from several families. Fitted after the fact from the uniform-tail edges, it is a finding about these minds and the baseline that structure beyond it must exceed.

## 6. The co-equal arm: how format and context move the order

Once the graph has some stable structure, take a fixed sample of its edges: stable, contested, ⟂-heavy, and generic-order. Vary one factor at a time:

- **format:** forced, tie, ⟂;
- **pairing:** both orders on one sheet vs split;
- **context:** bare API, CLI, agent harness, harness with Joseph's global context;
- **wording;**
- **effort.**

This separates the bundle behind the pilot's "80%". It also asks whether the edges ⟂ suppresses are the ones the minds share: the clean-room reading found 83% cross-family agreement on them.

## 7. Removed from the morning plan, and why

These were removed because Joseph ruled typefaces and Unicode irrelevant:

- the rendered- and degraded-image channel, and its API-adapter decision;
- the Unicode-name channel;
- ink correlates;
- "pre-fixed functional sequences" as an intake stream. That stream came out of the signa analysis, whose lineage runs through the coordinator's priming, and Joseph has not asked for it.

These were folded into the loop rather than kept as separate pilots:

- the encoding-order control is now part of salting (§2.4);
- the generic scalar is now a report from the uniform share (§5).

## 8. Size, roughly

- **One round:** about 600 triads, so 3,600 presentations per mind. That is ~90 sheet calls per API mind per round, and hours of local compute.
- **Density:** a few rounds bring the active pool to ≥ 15 comparisons per glyph.
- **The rest scales with the number of rounds** before the frontier dries, which is the point of the stop rule.

## 9. Decisions for Joseph

1. **Magnitude or progression.** Is the consensus graph built on "more" alone, or also on "further along"? The loop can run either; the morning plan's question #1 still stands.
2. **Panel membership.** Which Claude, Gemini and local models count as the round's minds, and whether Glimmer joins on selected loci.
3. **Who builds and runs the loop.** I can build it from the existing runner (`harness/runner/`), which already does fated randomness, ledgers, isolated judges and parsing. The new parts are the mixture sampler, the poset store, the continuation and salting steps, and the round driver.
