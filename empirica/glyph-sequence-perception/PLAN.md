# PLAN — stochastic discovery of glyph sequences

*2026-10-04, revised the same day. Claude Opus 5.5, for Joseph.*

*Built from:*

- *Joseph's direction today;*
- *his 08-25 turns in the pilot session;*
- *`pilot/pilot-record.md` and `pilot/DESIGN-scale-up.md`, with its addenda;*
- *`data/surveys-v1/RECONCILIATION-QUEUE.md`.*

*The method extraction from those sources is `.archive/2026-10-04-magnitude-era/harness/walk-r1-stopped/METHOD.md`. Earlier data and plans are in `.archive/`.*

---

## 0. The object

> *"Magnitude is no longer a 'critical' factor — neither is which way is 'up' — just sequencing."*
>
> *"There's going to be some level of simulated annealing to find other minima."*
>
> *"There should be intermediate analysis runs … that help recalibrate the stochastic slope."* — Joseph, 2026-10-04

**A sequence** is a set of glyphs placed in a linear order, where an order and its reverse count as the same sequence. Two glyphs may sit at the same step, and no axis needs a name. Sequences may cross, so one glyph can belong to several.

**What the study produces** is the set of sequences that LLM minds perceive, with how strongly each LLM family perceives each one.

**The centre of gravity is the emergent sequences** inferred from many small judgments. Survey records and other seeds only decide where to look first. That saves the tokens of searching the enormous ⟂ space blind. Seeds are not data.

## 1. Terminology

I had used **panel** for the set of judging minds, as in a "judge panel". From your message, you use it for one generated task. To avoid the clash I've stopped using the word. The terms below are used everywhere else; tell me if you'd like different words.

| term | meaning |
|---|---|
| **glyph** | one codepoint shown as a symbol |
| **item** | one task about a fixed set of glyphs. Kinds: **triad**, **order**, **next**, **between** (§3) |
| **presentation** | one rendering of an item with its fated randomization: glyph positions, option order, offered options. An item usually has several presentations |
| **sheet** | the presentations sent in one call, as one prompt with one JSON answer |
| **call** | one stateless request to one mind |
| **mind** | one model under one configuration, e.g. claude-sonnet-5-5 at low effort through an isolated CLI |
| **family** | the LLM family a mind belongs to (Claude, Grok, Gemini, Llama, …). Universality is measured across families |
| **roster** | the minds a round's sheets go to (my former "panel") |
| **round** | one draw from the queue, its calls, and the analysis pass that follows |
| **queue** | pending items, each with a priority and the reason for it |
| **evidence** | every parsed answer, stored per mind |
| **candidate** | a hypothesized sequence in the current model (§2) |
| **seed** | a starting point: a survey record or a `data/seeds/` entry. It generates items, and its order is never evidence |

## 2. From first principles: evidence, inference, and why chains longer than three matter

### What a sequence implies at the smallest scale

**A linear order on n glyphs is exactly its betweenness relations:** for every three glyphs in it, which one is in the middle. An order and its reverse imply the same relations, so betweenness carries no direction. That is why the triad is the atomic probe for this object. A pair carries nothing about sequencing once direction is gone.

**What a triad answer tells us:**

- **an order, "a b c":** the three lie on one sequence, with b between;
- **"only these two go together":** two lie on a common sequence and the third doesn't, an undirected co-membership;
- **⟂:** no shared sequence.

### Why triads are not enough on their own

Three things can't be seen in triads, and each is why longer chains matter.

1. **Splices.**
   - *The problem.* A glyph can belong to two sequences, like ⑩ in the circled digits and in the dresses of ten. Local triads can then be true while the chain they suggest is false. The pilot's forced-choice walks produced exactly such chains: `ᚂ③🟌❹⑩🟥9`.
   - *The check.* For a candidate a–b–c–d–…, a real sequence also implies its **long-range triples**, such as (a, c, e) or (a, d, g). Testing a sample of long-range triples, from both ends across the middle, is what separates a sequence from a splice. If the long-range triples fail, the candidate splits at the bridge glyph.
2. **Holistic orders.** The pilot found orders that appear only when four or more glyphs are present (`-=>})|`, the risebar). For those, triads come back ⟂ or noisy. **Order items** show 4–8 glyphs at once to see them.
3. **Growth.** Triads only test glyphs already in the pool. New members come from minds proposing what comes next, or between, given a stretch of a candidate. The pilot found continuation needs about four glyphs of context before holistic orders continue reliably.

### The model the evidence is fitted to

**The state.** The state is a set Σ of candidate sequences. Candidates may share glyphs, contain ties, and appear in either orientation. Each mind m and candidate σ also has a **perception strength** s(m, σ) between 0 and 1: how reliably m perceives σ.

**Answer probabilities.** Under Σ, each answer kind has a probability:

- **Triad answer.** Take the sequences that contain the triad's glyphs:
  - if one contains all three, an order with that sequence's middle (several such sequences give a mixture);
  - else, if one contains two, "only these two";
  - else ⟂;

  each passed through the mind's perception strength and its nuisance parameters: ⟂-propensity, guess rate, and slot bias (the tendency to name the glyph shown in the middle, or to keep the shown order).
- **Order answer.** Each line the mind writes should be the restriction of some σ to the shown glyphs. EXTRA means glyphs on no perceived σ shared with the others.
- **Next/between answers** are not likelihood evidence. They are proposals: new glyphs and new items, which enter the evidence only once triads and orders test them.

**Fitting.** Σ, s and the nuisance parameters are fitted to maximize the likelihood minus a description-length penalty, which charges for every candidate and every member so that Σ doesn't grow to fit noise.

- Σ is fitted by **simulated annealing**, with these moves:
  - insert or delete a glyph;
  - swap neighbours;
  - reverse a segment;
  - tie or untie two neighbours;
  - split a candidate, or merge two;
  - spawn a candidate from a strongly supported triad;
  - drop a candidate.
- The rest is fitted in closed form, or by EM, given Σ.
- **Distinct minima** come from restarts and a tabu on minima already found. They are kept as alternative explanations; the drain's several linearizations are the case in point.
- **Running at T > 0** gives *posterior samples* of Σ. The spread across samples is the uncertainty that drives the next round's queue.

**Three constraints the validation and the first real rounds showed are necessary.** Each fixes a way the fit could explain the answers with structure nobody perceived:

1. **A sequence claim must be witnessed as one piece.** Triples answered in the candidate's order at least twice, and by at least half of their answers, are linked when they share two glyphs. Every separately witnessed piece beyond one costs heavily.
   - *Why:* interleaving two sequences preserves every within-sequence relation, so the likelihood alone cannot object. A splice through a single bridge glyph also breaks the chain.
   - *Where seen:* the first synthetic run, and real r000.
   - *How strict:* a tie is witnessed only by tie answers. Ties across families had served as a loophole.
2. **A mind perceives a triple through a sequence:** perception of a triple is the maximum over the candidates holding it, not a compounding of them. Otherwise overlapping or restated candidates raise the likelihood (seen on real r001).
3. **Structure first, noise second.** Each mind's nuisance parameters are held at their defaults for the first half of each anneal, under a mild prior against a mind being mostly noise. Otherwise an empty model settles into "every answer is noise" (seen on real r000).

**Universality** is then read directly from the fit: σ is universal to the degree that s(m, σ) is high across families. The same fit reports, per link, which families see it.

## 3. The item kinds

### The mix: kernel growth (since 2026-10-04 evening)

Joseph's model, adopted with four amendments:

> *"various minds start to find a sequence — call it a sequence of three glyphs. The priority is then to extend that sequence to the right and to the left as far as they will go while still spending time looking for other 'kernels' from which to explore … square away the most obvious and stable (empirically) sequences"* — and *"15% of our effort was always 'hot' — exploring the space for more kernels … based on bumps from the original seed."*

**Established sequences** are the supported pieces of the fit's candidates: every link and tie witnessed by two or more in-order answers, and a majority (`model.supported_pieces`). Each carries a stability score: support × U × √(family coverage), the same measure as the standings.

**Every round splits its items concurrently** (`squeue.GROW`):

| share | what | how |
|---|---|---|
| ≥ 15%, ~20% planned | **hot exploration** | One stochastic draw over the whole pool. Glyphs are weighted 1, or by their seed's bump; half the items come from one seed's neighbourhood. A third are sets of 4–6 glyphs, so holistic kernels (invisible to triads) can be found. Absorbs any share the other categories can't fill. |
| ~45% | **extension** at both ends of every established sequence that is still open, most stable first, drawn nearly greedily (T = 0.1; exploration stays at T = 1) | `next` items (20% of the round: the most direct extension question, one presentation each; outward context of 3–5 glyphs); triads (20%) testing what lies beyond the end's last two glyphs, in this order of preference: what the minds proposed there, then what seeds write there, then co-occurring glyphs; an order window with the top proposal; `between` items inside the sequence. **Diminishing returns:** priority × 1/(1 + effort already spent at that end / 8), so many kernels grow in parallel and no single ladder takes the budget. **An end closes** once it has ≥ 6 next-answers, ≥ 70% of them none, and every proposal made at it has been tested (≥ 3 answers). |
| ~5% | **branching** | Triads holding a mid-sequence glyph, its neighbour, and an outside glyph it co-occurs with. These find other sequences crossing this one (the digit-dress kind of question), which ends alone never reach. |
| ~30% | **squaring away** | Support items for every unsupported link and unwitnessed tie (~15%); order windows; long-range splice checks. |
| ≤ 15% of presentations | **Latin-rotation follow-ups** | Triads inside established sequences first, then triads two or more minds ordered, plus a small ⟂-recheck share. |

**My four amendments to Joseph's model**, each explained to him:

1. diminishing returns on extension;
2. a branch share;
3. sets inside the exploration;
4. exploration absorbs unused share early on.

**What it replaced.** Ranking items by disagreement between posterior samples ("BALD") is no longer used. It never surfaced untested links, because warm-started samples inherit the same arbitrary choices. Measured on r002–r003, it had left extension under 10% and rotation follow-ups at 40–50% of every round.

**Cost** is counted in presentations:

- a new triad gets one presentation; its two other rotations come later, as follow-ups;
- an order item gets 2 shuffles;
- next and between items get 1 presentation each.

### What each looks like

*These are illustrations. The exact wording, and the order of independent sentences, are permuted per sheet. One kind per sheet, because the instructions differ. **A sheet holds 1–5 presentations** (Joseph, 2026-10-04: "only get one -- five (at most). Otherwise we have to put the turn number in the data and try to remove it as a confounder later"); each sheet's size is a fated draw from 1–5, and both the size and each presentation's position are recorded. Items from different sources are interleaved.*

**triad**:

```
Each item below shows three symbols.
For each item, answer with one of:
  - all three, written in the sequence they seem to form (either end first)
  - just two, if only two of them seem to go together
  - ⟂, if they don't seem to go in any sequence
[when offered] Join symbols that seem to be the same step with "=".
⟂ is expected often and is fully valuable. First impressions; judge each item on its own.
Copy each symbol exactly, or write #1, #2, #3 for its position in the item.

{"id":0,"s":["⑴","❶","①"]}
{"id":1,"s":["▃","𐤨","▆"]}
…
Reply with JSON only: {"answers":[{"id":0,"seq":["①","⑴","❶"]},{"id":1,"two":["▃","▆"]},{"id":2,"none":true}, …]}
```

**order**, k = 4–8:

```
Each item shows a set of symbols in scrambled order.
For each item: if some of them seem to go in a sequence, write that sequence (either end first).
If you see more than one separate sequence, give each one.
List symbols that belong to none under "extra". If none of them form a sequence, answer ⟂.
[when offered] Join symbols that seem to be the same step with "=".
[when offered] Write "…" where a step seems to be missing.

{"id":0,"s":["░","▫","▓","█","▒"]}
Reply: {"answers":[{"id":0,"seqs":[["░","▒","▓","█"]],"extra":["▫"]}, …]}
```

**next**:

```
Each item shows symbols in a sequence. If something seems to come next after the last symbol,
give up to three candidates, most fitting first. It may have no name. If nothing comes next, answer none.

{"id":0,"s":["☰","☱","☳"]}
Reply: {"answers":[{"id":0,"next":["☷"]}, …]}
```

**between:** the same as next, but showing two glyphs with a gap, and asking what goes between them.

### What is randomized, and which parameters are random

*All of it is fated: `seed = H(protocol ‖ purpose ‖ object)`.*

| | triad | order | next / between |
|---|---|---|---|
| **glyph display order** | Latin rotation over 3 presentations: each glyph in the middle slot once, leading end random | ≥ 2 independent shuffles | the sequence direction shown is random; prefix length 2–5 (next) |
| **⟂ / none offered** | 90% of presentations; 10% forced, without ⟂ or the "two" option | 90%; 10% forced, without ⟂ or EXTRA | always: "none" is the generative ⟂ |
| **tie "=" offered** | 50% | 50% | — |
| **gap "…" offered** | — | 50% | — |
| **"two go together" offered** | always, except in forced presentations | (EXTRA plays this role) | — |
| **multiple sequences allowed** | — | always | — |
| **salt** | — | when built from a candidate: 0–2 interlopers drawn from the co-membership neighbourhood | — |
| **candidates requested** | — | — | up to 3 (fixed) |
| **where repeat presentations go** | same sheet or split across sheets, 50/50 per item; a same-sheet item gets enough other items beside it that its presentations are never adjacent | same, 50/50 | — |
| **option order and instruction-sentence order** | permuted per sheet | permuted per sheet | permuted per sheet |
| **item order on the sheet** | shuffled, with an item's presentations never adjacent | same | same |
| **sheet size** | 1–5, fated per sheet | 1–5 | 1–5 |

**Why each random parameter exists:**

- **⟂ is withheld in 10% of presentations** to measure the co-equal object: how much order the format manufactures, and whether what ⟂ suppresses is shared across families. The clean-room reading found it was (83%).
- **Tie and gap are offered half the time** so that their effect on answers is measurable, while their data still accrue.
- **No confidence rating.** Consistency across presentations — the same middle 3/3, or 2/3 — is the behavioural measure of how clearly an order comes through. I'd rather measure it than ask for it. The felt quantity that does earn a place is the **gap** "…": it says where rungs are missing, and so where between items should go.
- **No axis words, ever:** no "magnitude", "amount", "size" or "value". The articulation filter (memory) is why.
- **Fixed for every presentation:** the system prompt (one neutral line), isolation, and effort. Model id and thinking tokens are recorded per call.

## 4. Seeds: decomposed, then they fade

A seed is a starting point. It is broken into primitive items the moment it enters:

- **its glyphs** join the pool;
- **adjacent triads** along its written order;
- **a sample of long-range triads;**
- **one order item:** a window of up to 8 glyphs, shuffled;
- **next items** from both ends;
- **an annealing restart point.**

Each generated item carries the seed's id in its lineage, as metadata.

After that, a seed has **no standing** in the model. Its written order is never evidence and never a reference. If the triads support it, a candidate like it emerges; if not, nothing remains. The priority bump on its items is spent once those items have been answered.

A `lattice` seed (the digit dress × value grid) is just a triad generator. It samples triples along each factor (same value with different dresses; same dress with different values) and mixed across them.

`data/seeds/` is the dropspot for new seeds as they come up in analysis and ideation. The survey records are already seeds.

## 5. A round, and the analysis between rounds

1. **Draw** items from the queue. Sampling is fated, P ∝ exp(priority / T), and the queue snapshot is recorded.
2. **Build sheets** (§3).
3. **Send** the sheets to the roster and append to the ledgers. Re-ask sheets that fail or are incomplete; the raw answers are kept.
4. **Analysis pass:**
   - **parse;** report unparsed and echo-failure rates per mind and per glyph (they aren't missing at random);
   - **re-fit the model (§2):** anneal, warm-started from the last round, with fresh restarts. This also re-estimates each mind's nuisance parameters, and so its slot bias. Where a bias is large, that mind's next sheets lean harder on the rotations that cancel it;
   - **take posterior samples** at T > 0;
   - **find the unsupported links.** For every candidate, list its links and ties that no witnessed triple supports yet: two or more answers in the candidate's order, and a majority. These become **support items**, a dedicated category of about 20% of each round, with a floor of 10% (Joseph, 2026-10-04: the standings' untested links show *"what kind of sheets need higher priority"*).
     - *Triads* pair the two glyphs of the link with each neighbour.
     - *Order windows* span the gap.
     - *Priority:* highest when the two glyphs have never been asked together.

     A warm-started fit cannot surface these through posterior disagreement, because every warm chain inherits the same arbitrary choice.
   - **recalibrate the slope.** An item's priority is its expected information for the minds it would go to: the disagreement among posterior samples about its answer. Then:
     - settled structure gets less sampling;
     - contested links, splits between families, and splice tests get more;
     - candidates whose ends are still growing get more next and between items;
     - the kind mix in §3 shifts toward whichever kinds produced the most information per token last round, within the floors;
   - **round report:** new, merged, split and dropped candidates; per-family strengths; the new allocation, with reasons.
5. **Cool T,** or reheat it when new structure appears. Repeat.

**Stop rule:** K rounds with no new accepted glyph and no change in Σ beyond a threshold (the 08-25 "loop until dry"). The uniform floor keeps running throughout.

## 6. Storage

**Truth** is append-only JSONL in `data/`:

- `items/`: items with their lineage;
- `presentations/`: each presentation's fated factors;
- `raw/<round>/<mind>/ledger.jsonl`: verbatim prompts and answers;
- `queue/`: snapshots per round;
- `fits/`: each round's Σ samples, parameters and report.

**Index:** Postgres 18, database `empirica_glyph_sequence` (pgvector; the 1,235 survey records are already in), with views per mind of triad outcomes, order lines, co-membership and proposals. It is rebuildable from `data/` at any time.

## 7. Roster

**Core** (Joseph, 2026-10-04: Glimmer over llama, and Haiku in), fixed so each mind's evidence accumulates:

- Claude Sonnet 5.5 and Claude Haiku 4.5: two Claude minds, so universality is family-weighted;
- Grok 4.6;
- Gemini 3.8 Flash;
- Meta Muse Glimmer 30B, locally through llama.cpp (`harness/core/glimmer-server.sh`). About 30–75 s per sheet.

**Second minds:** a fated ~20% of each round's sheets also go to Opus 5.5 and Gemini 3.1 Pro, to measure spread within a family. OpenAI's frontier model joins the core after Nov 2.

**Round size:** small early, so recalibration runs often. Round 0 is ~300 presentations, which is ~100 calls per core mind. Rounds grow as T cools.

The registry is `harness/core/minds.json`.

## 8. Build order

Each step is committed and checked before the next.

1. **`harness/core/`:** judge adapters and fated seeds, copied from the archive.
2. **Item builders and parsers** for triad, order, next and between, with unit tests on crafted answers, including adversarial ones: echo mismatch, `#n` position answers, ties, two sequences, a glyph answered twice.
3. **Storage and ingest.**
4. **Queue, sampler and sheet builder,** with a check that a rebuild is byte-identical.
5. **The model and the annealer (§2),** validated on **synthetic minds** with planted sequences (crossings, ties, a holistic one, a splice trap) and planted biases (slot, ⟂-propensity, guessing). Planted structure must be recovered and planted biases estimated before any real call.
6. **Round 0** with you. Then rounds.

## 9. Decisions so far (2026-10-04)

- **Primitive:** triad as the workhorse; order, next and between around it; pairs dropped.
- **Seeds:** decomposed and fading, as in §4. The dropspot is `data/seeds/`.
- **Roster and round size:** my lean, as in §7.
- **Database:** `empirica_glyph_sequence`, built.
- **Name:** `glyph-sequence-perception`.
- **Index:** `empirica/INDEX.md` updated.
