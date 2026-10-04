# Plan — surfacing stable glyph sequences, measuring them, and finding out how universal they are

*2026-10-04. Claude Opus 5.5, at Joseph's request. This is the consolidated, current version.*

*How it was reached, in order:*

- *`01-view-before-top.md`: written and committed before opening any top-40 material or reading yesterday's interpretation;*
- *`02-after-v1-record.md`: after the v1.0 record and the clean-room reading;*
- *`03-after-top40.md`: after the top-40 material, with one new analysis of existing data.*

*Where this file and those disagree, this file is current. They are kept as the record of how the view moved. No judge calls were made for any of it.*

---

## 1. What counts as a result

**A sequence is stable to the degree its order survives a set of transformations, among a set of minds.** The transformations:

- resampling the same mind;
- presentation order;
- format (forced / tie / ⟂);
- unit (pair / set / continuation);
- context (bare API, CLI, agent harness, sheet);
- set composition (salt, neighbours);
- framing ("more" / "less" / "further along");
- input channel (glyph token / rendered image / degraded image).

The deliverable is a **catalog**. Each entry carries a *stability profile* across those transformations and a *universality profile* across minds. Both are reported **per adjacent link**, because the middle rungs are where a ladder fails while its ends hold. A chain is as stable, and as universal, as its weakest link.

"Top" lists become views of the catalog, each answering one stated question:

- the most universal links;
- ladders whose order survives image degradation (the immediacy view);
- order that holds in sets but not pairs and survives the encoding control (holistic candidates);
- places where minds agree with each other against the author.

No single rank recombines them.

Two findings from existing data shape everything below:

- **The edges ⟂ removes are shared across model families** (83% cross-family agreement on forced winners; chance 50%). So "manufactured" is not noise. It is a weaker ordering that is either felt below threshold or built by a heuristic every family shares. *(clean-room reading)*
- **Whole-set reconstruction is confounded with known encoding order.** 90 of the 117 top-40 survey sequences are codepoint runs. Among those frontier judges won't order pair by pair, contiguous runs are rebuilt exactly 84% of the time (Balinese vowels: pairwise 0.06, whole set 1.00), against 41% for non-contiguous ones. *(stage 3, `scripts/encoding_order_check.py`)*

## 2. Phase 0 — work on data already on disk (no judge calls)

1. **Build the loci.**
   - **Intake:** every sequence record from all seven surveys, plus capture-corrections. Read `type` or `record_type`, and normalize the surveyor label (sonnet-survey-3's extraction says `sonnet-3`).
   - **Grouping:** connect records that share glyphs. A locus's stimulus is the **union** of its records' glyphs; variants become natural salt instead of something to choose between.
   - **Splitting:** cap any locus that is too large to show whole (the numeric glyphs will form one giant component) at about 10 glyphs, by fated split. Overlapping sub-loci then stitch the pieces.
   - **The other record types join here, each in its role:** negatives as controls, questions as battery items, generators as lattice objects, morph and cyclic records for the set and continuation instruments.
2. **Re-score the 117 top-40 loci in this frame,** from their existing ledgers. The output per locus is each mind's own arrangement, its partition (kept vs EXTRA), coverage, and the contested rungs. Those rungs become the first targets for repeated presentations in Phase 2.
3. **Restate what the v1.0 data support,** from the clean-room reading, for Joseph to decide on MANIFEST wording. The changes I'd make:
   - transitivity measured on order-stable edges only;
   - gestalt reported with coverage and partition;
   - ⟂ reported as a judge's threshold in a context;
   - "manufactured" restated as a suppressed shared ordering.

## 3. Phase 1 — four small pilots, each deciding a branch of the design

| pilot | question | why it gates something | rough size |
|---|---|---|---|
| **A. Generic scalar** | Does each mind carry one latent glyph scalar (complexity / ink / "more-ness") under forced choice, and does it agree across families? | It is the null every candidate must beat. Noise sets drew the same order from several families, so a permutation null is too weak. If one scalar fits, the shared heuristic behind "manufactured" edges is measured, not guessed. | ~600 uniform-random pairs over ~120 glyphs, both orders, forced; 3 minds from 3 families |
| **B. Logit readout for local models** | Can ollama (0.34.4) or llama.cpp return answer log-probabilities in both orders, so slot bias cancels and nothing needs parsing? | Small models currently enter the data mostly through slot preference and parse failure. Without this they cannot be measured for universality, only as a parse statistic. | ~1 hour local; the conflict battery as reference |
| **C. Image channel, clean and degraded** | Does a multimodal frontier judge rebuild controls (dice, ramp, a digit run, two noise sets) from a rendered image? Does order survive blurring until glyph identity is lost? | Degraded-image survival is the closest operational form I can find of "the glyph *shows* more" against "*names* more". It also gives the ink correlate a channel in which ink can actually act. Needs an API adapter with image input, since the CLIs run with tools stripped. | ~30–60 calls, 2–3 fonts |
| **D. Encoding-order control** | Fill the 2 × 2 (magnitude / non-magnitude × contiguous / scattered). Swap one glyph of a contiguous run for its nearest off-run lookalike. | Decides whether whole-set success counts as magnitude evidence for any given locus. Without it, "holistic" and "known alphabet order" are the same measurement. | ~12 sets per cell, swap variants, 3 shuffles, 3–4 minds |

## 4. Phase 2 — the discovery loop (exploratory; loop until dry)

**Intake streams, each labelled by lineage (labels never enter confirmatory statistics):**

1. **Survey loci** (Phase 0). SEED-PRIORITY may order the work; no strength or concordance filter ever excludes a record.
2. **Prior-free generative discovery.**
   - Fated block-uniform single glyphs, or pairs, go to a mixed-family panel with articulation-free continuation: "if something comes next, continue it; it may have no name; otherwise decline".
   - Proposals that recur across families become loci.
   - The decline rate is itself the base rate the survey stream needs.
   - This is Joseph's "no prior information about the glyphs" route. It also relieves the pane-walking bias toward contiguous runs.
3. **Sequences fixed outside the study, before it, for a function.** This is signa's class: progress and sparkline glyph sets in widely used software, UI rating and severity scales, ladders declared in Unicode character names, weather-icon progressions. These are the only stimuli that control for "the study finds what its pickers saw".
4. **Recycled frontier.** Continuation proposals at both ends of stable chains, chains found in the pairwise graph, and absorptions found in salting.
5. **Controls:**
   - matched noise sets;
   - permuted candidates;
   - the encoding-order 2 × 2;
   - surveyor negatives.

**Measurement per locus:** the same battery whatever the source, so a candidate's origin cannot shape its test.

1. **Whole set.** 3 fated shuffles, with ⟂ and EXTRA available, plus the encoding control where the locus is a contiguous run. Record the mind's **own arrangement**, partition and coverage; τ against an author's order is secondary.
2. **Pairwise, targeted by the minds' arrangements.** Adjacent rungs in each mind's arrangement, plus pairs in dispute between minds. Both orders, in both **forced** (direction, including below threshold) and **⟂-available** (felt salience) formats. ≥ 3 reps per order on contested links: the conflict battery shows frontier judges are fully self-consistent over 2 orders × 3 reps on only 17–32 of 38 hard items.
3. **Continuation** from prefixes of length 2–5 in both directions. This gives the holistic onset length and proposals at the frontier.
4. **Salting** with fated lookalike distractors.
5. **Framing check on a subset.** "Less" should invert a real axis and not an answer prior; "further along?" separates succession from magnitude.

**Discovery panel** (affordable, one or two per family):

- a Claude model;
- a Gemini (rate-limited, so spread over days);
- Grok;
- local models through logit readout if Pilot B works: llama3.2-3b, gemma3-4b, mistral-7b, qwen2.5-3b;
- Glimmer 30B on selected loci, because it is slow.

**Stop rule:** K consecutive rounds with no new accepted rung (DESIGN-scale-up's loop-until-dry). The uniform-pair stream keeps running alongside as the standing denominator.

## 5. Phase 3 — the measurement-format factorial (the study's co-equal object)

A fixed reference set of ~40 links, chosen by fated rule from the discovery catalog across its kinds:

- strong;
- below threshold;
- explained by the generic scalar;
- holistic candidates;
- controls.

Vary one factor at a time from a clean base:

- **format:** forced / tie / ⟂;
- **unit:** pair with both orders on one sheet vs split across sheets; a non-cyclic triad; a set;
- **context:** bare API / CLI / Claude Code subagent / that subagent with Joseph's global context;
- **wording:** pilot vs v1.0, and with or without the axis words "magnitude, amount, intensity, size, value";
- **effort:** low vs high;
- **framing:** more / less / further along.

This takes apart the pilot-condition bundle that v1.0 could not separate: harness, context, wording, effort, sheet size, sheet pairing. It turns "the room changes how much order a mind reports" from one 1.6–1.85× contrast into a measured map.

## 6. Phase 4 — universality: register, then confirm

- **Freeze the catalog.** Register predictions about which links and chains hold, for which panel, and in which contexts.
- **Confirm** on a fresh fate, with at least one family absent from discovery. OpenAI's frontier model returns after Nov 2; gpt-oss-20b, Llama 70B and Glimmer are also candidates.
- **Statistics:**
  - per link, a family-weighted share of minds for which it holds, so four Claude models count as about one family;
  - the boundary: the smallest scale, and the contexts, where it stops holding;
  - per locus, agreement between minds' own arrangements, judged against the matched-noise null and the generic scalar, never against a uniform permutation null alone.
- **Human arm.** A small published page with a shared database, showing rendered glyphs for the whole-set and pair tasks. Joseph, Suzanna, whoever is willing. Even a few people place LLM universality beside human perception, and signa's seam (`═→⚬`) is a ready first item.

## 7. Parallel: tiers that ask nothing (open-weight models)

- **Likelihood.** Log-probability of a locus's permutations in a neutral frame. Confounded with string familiarity, so it is read beside the asked tiers as a measure of exposure.
- **Representation.** Linear "more" directions in hidden states and embeddings. Extend the qwen3-embedding probe (leave-one-family-out ρ ≈ +0.68) to the judges' own hidden states, with codepoint and token-geometry controls.

Read together, the tiers form a gradient of how much the instrument asks:

representation → likelihood → continuation → set → pair → articulated survey.

Where an order appears along that gradient is the most direct answer I can offer to "how does format manufacture or suppress order".

## 8. Provisional definitions (to register before Phase 4, after discovery has shaped them)

- **Link holds for a mind, in a context:**
  - forced direction consistent across both orders in ≥ 2 of 3 reps;
  - not contradicted by the mind's whole-set arrangement (it is adjacent, or ordered the same way, in the arrangement);
  - the link's ⟂-format commit rate reported beside it, not required.
- **Beyond generic:** the mind's generic scalar does not predict the link's direction, or predicts it with less confidence than observed. This is the excess a "specific axis" must show.
- **Holistic candidate:**
  - the whole-set order holds;
  - pairwise ⟂-heavy or inconsistent;
  - survives the encoding control;
  - not a known conventional sequence.
- **Chain:** a maximal path in the consensus DAG over a locus. Chain universality is the minimum over its links.

## 9. Rough scale (order of magnitude only)

- **Loci:** 849 survey records will probably give a few hundred loci, plus generative and functional-sequence loci.
- **API minds:** ~10–15 calls per locus per mind in sheet mode, so roughly 10⁴ calls over the API panel for discovery. Anthropic quota is fine. Gemini is rate-limited and spreads over days.
- **Local minds:** mostly hours of local compute.
- **Cost profile:** Phases 1 and 3 are small. Phase 2 is the bulk. Phase 4 is moderate.

## 10. Decisions for Joseph

1. **Is the object magnitude, or ordered progression more broadly?** The whole-set prompt already licenses "progression"; continuation and morphs go wider still. The plan measures both and reports them apart: pairwise "more" for magnitude, set and continuation for progression, with the encoding control separating ordinal knowledge from felt order. Which is primary when we say "stable sequence" is yours to set.
2. **The image channel needs a direct API adapter** for at least one multimodal family, because the CLI judges run with tools stripped. Acceptable?
3. **Human arm:** is it wanted, and who?
4. **Contexts in the universality claim.** Only clean API judges, or also agent harnesses? A harness run with your global context loaded carries private context, so its transcripts stay out of git, as in v1.0.
5. **Functional-sequence sources** for intake stream 3: which software and UI sets are fair game?
6. **Timing.** Wait for Codex (Nov 2) so an OpenAI frontier model is in the confirmation panel, or confirm without it and add it later?
7. **Status of `analysis/top40.*`.** I'd keep it as written, with a status line pointing to `03-after-top40.md`. Its data stay useful as discovery-tier measurement.
8. **MANIFEST restatement** (Phase 0, item 3): now, from the clean-room reading, or after Phase 0's re-scoring?

## 11. What this plan does not settle

- **Felt or shared heuristic.** Even with the generic scalar, an ordering that every family shares and that ⟂ suppresses may be felt below threshold, or may be constructed. The scalar can show *how much* of it one heuristic explains, not what it is like.
- **Shared training text.** Universality across LLMs may largely mean shared training text: Unicode charts, names, software usage. The plan tests this through the name, likelihood and encoding probes rather than removing it. A finding of "universal because everyone read the same chart" is still a finding about these minds.
- **Lens dependence of the generative stream.** Continuation prompts carry their own frame ("continue"). Every new framing obliges a re-walk; the pilot's lesson that pane verdicts depend on the lens applies to instruments too.
- **Not yet verified:** that ollama 0.34.4 exposes logprobs, and that an image-capable API path exists on this machine. Both are pilots, not assumptions.
