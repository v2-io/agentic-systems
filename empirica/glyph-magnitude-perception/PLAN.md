# PLAN — stochastic discovery of glyph sequences, done the way it was headed on 2026-08-25

*2026-10-04. Claude Opus 5.5, for Joseph.*

*Built from:*

- *Joseph's direction today, quoted below;*
- *his 08-25 turns in the pilot session;*
- *`pilot/pilot-record.md` and `pilot/DESIGN-scale-up.md`, with its addenda;*
- *`data/surveys-v1/RECONCILIATION-QUEUE.md`.*

*The extraction of the 08-25 method from those sources is `.archive/2026-10-04-magnitude-era/harness/walk-r1-stopped/METHOD.md`. Earlier data and plans are in `.archive/` (its README says what and why).*

---

## 0. What is being found

> *"Magnitude is no longer a 'critical' factor — neither is which way is 'up' — just sequencing."*
>
> *"Privileged domain models knowledge (like `①` vs `⑴` vs `❶` vs `🯱`) can be put in as seed work that bumps up its priority in the stochastic queue."*
>
> *"There's going to be some level of simulated annealing to find other minima."*
>
> *"There should be intermediate analysis runs, I would expect, that help recalibrate the stochastic slope for what is given more statistics."* — Joseph, 2026-10-04

**The object is sequences:** sets of glyphs that LLM minds place in a linear order. Direction-free: a sequence and its reverse are the same sequence. No axis needs a name, and no Unicode property or rendering measurement is a reference.

**Universality** is how widely a sequence, and each of its links, is shared across LLM families.

**The search is stochastic and prior-free in its sampling.** Seeds only raise the priority of where to look first. Each round ends in an analysis pass that decides where the next round's statistics go.

## 1. What a judge is asked

Pairs are dropped. A pair carries no sequencing information without a direction or a "more".

**1a. Set arrangement, k = 3 to 8 glyphs.** This is the pilot's gestalt instrument, the one instrument that saw holistic orders.

- **What is shown:** k glyphs, shuffled.
- **The prompt, roughly:** *"If some of these feel like they go in a sequence, write that sequence, either end first. List any that don't belong after EXTRA. If none do, answer ⟂."*
- **k = 3 is the betweenness triad:** which glyph goes in the middle, or ⟂.
- **What each answer gives:**
  - betweenness constraints for every triple it orders;
  - adjacencies;
  - membership (kept, or sent to EXTRA);
  - whole-set ⟂.

**1b. Continuation.** This is the pilot's articulation-free generator.

- **What is shown:** 2–5 glyphs of a candidate sequence, presented from either end.
- **The prompt, roughly:** *"If something comes next, give it; it may have no name; otherwise none."*
- **What it gives:** proposals that enter the queue as new glyphs and rungs.

Neither instrument asks for an axis, a name, a direction or "more". The pilot measured three separate times that requiring articulation filters out exactly the liminal perception the study is after (memory: articulation-filter-clamps-liminal-perception).

## 2. Randomization: what has to vary, and where each rule came from

| rule | origin |
|---|---|
| Glyph order within every presentation is shuffled by fated draw; each set is shown in ≥ 2 different shuffles. | Pilot side bias: 3B chose the '>' answer token in 85% of answers; Joseph, 08-25: *"randomize the 'symbols you are choosing from' each time"* |
| The shuffles of one set sit **on the same sheet or a nearby one**, as Joseph asked on 08-25. Same-sheet vs split is itself a fated, recorded factor, assigned at random per set. | Joseph, 08-25; same-sheet presentation changes consistency (measured 2026-10-03) |
| Triads are counterbalanced so each glyph appears in the middle screen slot equally often across instances. A "middle = the glyph shown in the middle" bias is then measurable and cancels. | The pilot's cyclic triad unit made cycles indistinguishable from same-slot answers |
| Presentations of one set go to **independent fresh instances** of the same mind: one sheet per call, no memory. | Pilot walk5: reverse cycles split across a judge pair |
| The response options **and the order of independent instruction sentences** are permuted per sheet by fated draw. | Pilot walk5b: option order moved the commit-vs-⟂ threshold by ~6 points |
| Sheet items are shuffled. Two presentations of the same set are never adjacent. Item kinds and set sizes are mixed. | Pilot sheets; *"judge each item on its own as it comes rather than building a scheme"* |
| ⟂ and EXTRA are always offered, with *"⟂ is expected often and is fully valuable."* | Pilot walk3: forced formats manufactured most cross-domain edges |
| No axis words in any instruction. The old prompt listed "magnitude, amount, intensity, size, value"; that list is gone. | Today's direction; the articulation filter |
| The answer gives each element as glyph **and** shown position, `[{"p":3,"g":"⑴"},…]`. A mismatch between the two is unparsed, never imputed. Echo failures are recorded per glyph, because they are not missing at random. | Pilot 3B echo loss (14%); a 2026-10-03 judge couldn't echo `⬤` |
| Response-vocabulary glyphs (⟂, ⊥, ≈) never appear as stimuli. | Pilot: the ≈ glyph collided with the ≈ answer |
| Judges are isolated, with tools stripped. Model id, effort and thinking tokens are recorded per call. Context, effort and sheet size are recorded factors, never silent constants. | DESIGN fix #5; a judge offered tools looked glyphs up by name |
| Every stochastic choice is fated: `seed = H(protocol ‖ purpose ‖ canonical(object))`, including queue draws. | DESIGN addendum (vivarium convention) |
| Every glyph and item carries a lineage label (survey-seed / domain-seed / frontier-proposal / uniform-tail). It is metadata only; no analysis conditions on it. | DESIGN addendum; RECONCILIATION-QUEUE lineage ruling |

## 3. Storage: append-only JSONL truth, a Postgres 18 index

Raw truth goes in `data/`, append-only:

- `stimuli/<round>.jsonl`: every presentation, with its shown order and every fated factor;
- `raw/<round>/<judge>/ledger.jsonl`: every call, with the verbatim prompt and response;
- `queue/<round>.jsonl`: the queue snapshot each round was drawn from, with its priorities and reasons.

The index is database `empirica_glyph` (`psql-18`, pgvector already installed). The current schema is extended and stays rebuildable from `data/`:

- `glyph`: codepoint, first lineage, comparison counts, and an embedding column for later correlates.
- `presentation`, `call`, `response`: the parse is versioned and re-runnable over the raw text.
- **Derived views:**
  - per-mind betweenness counts `(mind, a, mid, c)`;
  - adjacency counts;
  - keep/EXTRA membership counts;
  - ⟂ rates;
  - per-LLM-family aggregates.
- `candidate`: annealed sequences, each with per-link support per mind and per family.
- `queue`: pending items, each with priority, reason and lineage.

`survey_records`, already ingested (1,235 records), stays as the seed table.

## 4. The queue and the annealing

**State:**

- the evidence, which is everything in the views above;
- a population of **candidate sequences**, unoriented ordered glyph lists.

**Fit of a candidate to a mind.** Betweenness constraints the candidate satisfies, minus those it violates, plus the adjacency and membership evidence. Each constraint is weighted by its posterior certainty. The panel fit is family-weighted, so several models from one company count as about one family.

**Simulated annealing.** Moves on a candidate:

- insert a glyph from its evidence neighbourhood;
- delete a glyph;
- swap neighbours;
- reverse a segment;
- split a candidate in two;
- join two candidates end to end.

Moves are accepted by the Metropolis rule at temperature T.

**Restarts** begin from each survey record, each domain seed, and random walks on the adjacency graph. Any minimum already found is tabu for later restarts. The result is a *set* of distinct minima, so alternative linearizations of the same glyphs (the drain's case) and crossing sequences (dress against number) both survive as separate candidates.

**Generating items.** Each candidate generates queue items where its evidence is thin or contested:

- windows of its glyphs, with fated lookalike salt;
- continuation from either end;
- **cross-candidate sets** that mix glyphs of two candidates sharing a neighbourhood. These ask the inter-family question directly: does `①` sit in a sequence with `⑴` and `❶`?

**Priority** of an item is its expected information (posterior variance of the constraints it tests, for the minds it would go to), times a novelty factor for glyphs below the density target, times a seed bump:

- **domain seeds:** bump b, set by you;
- **survey seeds:** a smaller bump;
- **duration:** the bump lasts until the seed's glyphs reach the density target, then decays. It never excludes anything.

**Sampling** is fated, with P(item) ∝ exp(priority / T).

- **Cooling:** T falls across rounds, so the queue moves from broad exploration to densifying contested structure.
- **Long tail:** a **standing uniform-tail quota** (~15%, the pilot's figure) never closes.
- **Reheating:** T rises again when a round turns up new structure.

## 5. A round, and the analysis between rounds

1. **Draw** N items from the queue: fated draws, recorded snapshot.
2. **Build sheets** under §2's rules.
3. **Run** the panel and append to the ledgers.
4. **Analysis pass,** which recalibrates the slope:
   - **Ingest and parse.** Unparsed and echo-failure rates per mind and per glyph.
   - **Bias diagnostics per mind:**
     - tendency to keep the shown order;
     - middle-slot preference on triads;
     - first- or last-kept preference;
     - ⟂ and EXTRA rates by set size and by sheet position;
     - same-sheet vs split agreement.

     Where a bias shows up, the next draw adds the counterbalancing that cancels it for that mind.
   - **Evidence update:** posteriors per triple and per adjacency, per mind and per family.
   - **Re-anneal** the candidates, warm-started from the last round's, plus fresh restarts.
   - **Recalibrate the slope:**
     - regions where every family already agrees with low variance get **less** sampling;
     - contested links, splits between families, and glyphs below the density target get **more**;
     - set sizes and continuation lengths are re-weighted toward what produced information last round.
   - **Round report:** what changed. New candidates, merges, splits, broken links, and the new allocation with its reasons.
5. **Cool** T, or reheat it, and repeat.

**Stop rule:** K consecutive rounds with no new accepted rung and no change in candidates beyond a threshold (DESIGN: loop until dry). The uniform quota keeps running until then.

## 6. Panel

Each round's items go to one mind per LLM family, so every family sees the same queue:

- Claude, rotating Haiku, Sonnet and Opus;
- Grok;
- Gemini, rate-limited, so it lags and catches up;
- local models through single-item calls. Their slot biases are measured and cancelled by §2's counterbalancing, not by assumption.

Glimmer joins on selected items. OpenAI's frontier model joins after Nov 2.

Each mind's evidence stays separate. Agreement across families is the measure of universality.

## 7. Seeds

**Survey seeds.** All 1,235 survey records:

- 849 sequences become initial candidates, unoriented, with no strength filter;
- equivalences, generators, negatives and questions become set items;
- morph and cyclic records become set and continuation items.

**Domain seeds.** Privileged domain knowledge, for example the digit dress families `①…`, `⑴…`, `❶…`, `🯱…`. Each is written as a small file in `data/seeds/` with its author and lineage `domain-seed`. Each one raises queue priority and nothing else.

## 8. Build order

Each step is committed, and each is checked before the next one starts.

1. **`harness/core/`:** judge adapters and fated seeds, copied from the archive.
2. **Instruments and parser:** set arrangement and continuation, with unit tests on crafted answers, including adversarial ones (echo mismatch, a reversed sequence, duplicates).
3. **Schema extension and ingest.**
4. **Queue, sampler and sheet builder,** with every rule in §2 and a check that a rebuild is byte-identical.
5. **The analysis pass and the annealer,** validated on synthetic judges with planted sequences and planted biases. Planted structure must be recovered and planted biases cancelled before any real judge call.
6. **Round 0:** a ~150-item shakedown on three families, reviewed with you. Then the rounds.

## 9. Decisions for you

1. **The primitive.** Set arrangement (k = 3–8, triads included) plus continuation, with pairs dropped. Right?
2. **Domain seeds.** Who writes them, and how big is the bump?
3. **Panel and round size.** Something like 400 items per round across 4–5 minds. With each set shown in ≥ 2 shuffles, that is ~800 presentations, or ~25–30 sheet calls per mind per round at ~30 items per sheet.
4. **Database.** Extend `empirica_glyph`, or start a fresh one?
5. **The study's name.** The slug still says "magnitude". Rename it now, or later?
6. **`empirica/INDEX.md`.** Its row for this study (outside this directory) still states the archived v1.0 claims. I haven't touched it.
