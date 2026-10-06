# Check: planner stochastic-2 against the audit of stochastic-1

*2026-10-06, Claude Opus 5.5, the author of `planner-stochastic-2026-10-06.md`. This isn't de novo: I came to stochastic-2 knowing my own findings, and much of what it does is what I suggested, so I've looked hardest where my suggestions were taken. Written for the coordinating session before the planner's next change, and for Joseph if he wants it. I changed no file but this one and touched no process.*

*What I read and ran.*

- **Read whole:** `priority/plan.py` at `34398d6f` (the working tree matches), and the diffs to `run.py`, `report/best.py` and `tree/tree.py`.
- **Ran:** the planner in-process from my scratchpad with bytecode writes off, against the answers on disk at about 16:40, with round id `c999`.
- **Gemini:** all three minds were paused, so the active families were Claude and Grok, as live.
- **Simulation:** the claim-stage inclusion probabilities below come from 300–400 fated draws, each with its own seed, over the candidates a real dry run built.

*The seal.* As before, any choose, choose-control or names candidate touching a canary glyph was dropped before I computed or printed anything. I counted one thing on question metadata only (no answers): which D-control questions have a canary glyph in their neutral context.

Labels: **[measured]**, **[checked]** against the code, **[reasoned]**.

## The short answer

Stochastic-2 resolves findings 5, 6 and most of 8 by construction, and fixes 1 and 7 for the cases the audit named. Its two-stage draw does what finding 2 asked [measured]:

- ends take 94 of 170 continue draws, up from 63 of 189;
- recognition of reasoned candidates takes 11 of 42 inhibit draws, up from 1 of 36;
- grown rows take 17 of 76 primary cohere draws, down from 42 of 130.

What it trades, and what's new:

1. **The off-sequence claim makes re-asks a hard zero in practice** [measured]. All 4,674 off-sequence continue contexts form one claim, drawn in about 0.25% of rounds; drawn, it yields one question. That's about one re-ask of a given context per two million rounds. For inhibit (766 pairs), 0 of 400 simulated rounds drew it. One claim also makes each item rarer as the class grows: the enumeration-dependence of finding 2, turned upside down. My judgment is that this is too rare to count as "reachable". Per-item claims at a stated relevance would cost a known share; numbers are below.
2. **Breadth-first, with far more claims than draws, caps every sequence at one continue question a round, and flattens across sequences** [measured]. The strongest groups of sequences are drawn in about 20–28% of rounds; the weakest in 4–7%. "Square away the most obvious and stable first" is now weak. One change would keep the enumeration-independence and allow concentration: draw claim *slots* with replacement.
3. **Claims are grouped unevenly across streams** [measured, checked]. "Asked before" items are one claim each in triad, pick, order, names and cohere, at relevance 0.5. In continue and inhibit they are one claim *together*, at 0.05. Walk triads are grouped by sequence, so asked triads, each alone, went from 1 of 10 triad draws to 6 of 12.
4. **Finding 1 has a residue** [measured]. 38 whole periods of manifested cycles are still on-sequence candidates, 8 of them labelled `end` at $5\times$. They come in through *other* sequences that contain the period, such as the linear walk `➚↑↖←↙↓↘→↗`, which contains the whole eight-arrow cycle.
5. **Smaller:**
   - The seal has one D-control edge (1 of 173 asked).
   - `ACTIVE` is computed from the core roster only, not per stream.
   - The answer digest hashes record IDs, which don't pin record content.
   - Newly found 3–5-glyph kernels are the least-drawn sequences. That isn't new; `rank`'s $\min(1, \text{walked}/4)$ does it in both versions, against Joseph's extend-first rule.

On your departures: the mean as the claim weight was the one I expected to bite, and it doesn't (finding 2 below). The 0.5 midpoint is a sound neutral choice. The off-sequence claim is the one I'd revisit.

---

## Finding by finding

| # | audit finding | stochastic-2 | status |
|---|---|---|---|
| 1 | manifested cycles asked as ends at $5\times$ | both sides of a cycle get cycle probes only | **resolved on the cycle's own sequence**; 38 whole periods remain through other sequences (below) |
| 2 | draw follows enumeration size | two-stage draw by claim, breadth first; unranked sources at 0.5 | **resolved as stated**; traded for a per-sequence cap and uneven grouping (below) |
| 3 | information is about $1/n$ | unchanged; docstring now says so | Joseph's, as agreed |
| 4 | hard zeros | every context and pair asked before is a candidate; reflection at the end, both ways | **reflection resolved**; the re-asks are reachable in name only (below) |
| 5 | pending: stale backlog, bookkeeping | per-assignment matching, a 12-round horizon, paused families left out | **resolved**; one edge (below) |
| 6 | order "none" answers invisible | `order_counts` reads every lines and none answer | **resolved** [checked]; the 453 sets are now in the "asked" source |
| 7 | the planner weighted by sealed answers | `blind()`: canary-touching choose, choose-control and names candidates weighted by $n$ alone | **resolved for positions and sets**; one D-control edge (below) |
| 8 | smaller things | see below | **mostly resolved** |

### 1. The residue

`continue_cands` now treats a sequence whose stop is `cycle (manifested)` as having no end on either side. No end candidate comes from a cycle's own sequence, and its probes show less than a period [measured, checked].

But a manifested cycle's period can lie inside another sequence. That happens when a walk passes through the cycle's glyphs in rotation order and stops elsewhere: `➚↑↖←↙↓↘→↗` (stops `open` and `wrap→↑`) contains the whole eight-arrow period `↗ → ↘ ↓ ↙ ← ↖ ↑`. On-sequence candidates showing a whole period [measured]:

| label | count |
|---|---|
| inside | 16 |
| end, at $5\times$ | 8 |
| lengthen | 7 |
| kstar | 4 |
| replicate | 3 |
| **total** | **38** |

What I'd change: make "shows a whole period of a manifested cycle, in any rotation" a validity rule in `put()`, whatever the claim. METHODOLOGY §4's no-spoiling rule is about the question asked, not the sequence that proposed it, and the module already lets validity refuse.

c102 and c103 were planned with the original bug. From my reading of `tree.manifest()`, nothing needs cleaning up: answers to a whole shown period are recorded as ordinary continuations, and they can't count as manifestations. They spent budget; they didn't corrupt the tree.

### 2. What the two-stage draw does

**What it was meant to do, it does** [measured, dry run, canary-free]:

| stream | stochastic-1 | stochastic-2 |
|---|---|---|
| continue: ends | 63 / 189 | 94 / 170 |
| continue: inside | 66 / 189 | 35 / 170 |
| inhibit: reasoned recognition | 1 / 36 | 11 / 42 |
| inhibit: skip tests | 28 / 36 | 24 / 42 |
| cohere: grown rows | 42 / 130 | 17 / 76 |
| choose: splits | 10 / 46 | 16 / 37 |

**The mean as the claim weight.** I expected the mean to bury long, well-asked sequences, whose many re-asked contexts would dilute a fresh end. It doesn't. I simulated how often each sequence's claim is drawn in a round, by length and by whether it has an open end, with the claim weighted by its mean (as built) and, for comparison, by its maximum unit [measured]:

| sequences | number | units per claim | $P$(drawn), mean | $P$(drawn), max |
|---|---|---|---|---|
| open end, 3–5 glyphs | 523 | 5 | 0.071 | 0.044 |
| open end, 6–10 | 36 | 41 | 0.207 | 0.200 |
| open end, 11–24 | 50 | 159 | 0.205 | 0.280 |
| open end, 25+ | 21 | 402 | 0.188 | 0.278 |
| no open end, 3–5 | 215 | 9 | 0.102 | 0.080 |
| no open end, 6–10 | 201 | 43 | 0.199 | 0.186 |
| no open end, 11–24 | 163 | 130 | 0.203 | 0.258 |
| no open end, 25+ | 86 | 323 | 0.191 | 0.270 |

The mean and the max differ by little. So I'd keep the mean: it is the more defensible of the two against enumeration.

**The trade: a cap and a flattening** [measured, reasoned]. Continue has 1,295 sequence claims and draws about 170 questions. Each drawn claim gives its best unit before any gives a second, so a round is about 170 distinct claims with one question each. Second units essentially never happen. As a result:

- **No sequence gets more than one continue question a round.** The groups above are each drawn in at most about a fifth to a quarter of rounds, the strongest included. A sequence's k\* ladder, or its lengthening test, now takes many rounds to complete.
- **The spread across sequences is narrow:** about $3\times$ between the least- and most-drawn groups (0.07 to 0.21). Under stochastic-1, a strong sequence with fresh contexts could take several questions in one round.

Breadth first is what keeps enumeration out. But "the most obvious and stable sequences squared away first" now holds only weakly.

What would keep both [reasoned]: draw claim *slots* with replacement, each slot with probability proportional to the claim's weight (the mean), and give each slot that claim's next unit. A heavy claim then gets several questions in a round in proportion to its weight, and a long one gets no more than a short one of the same weight. Its expected share is set by its weight alone. You could also cap a claim's slots per round at a stated number, if one sequence swallowing a round is a concern.

**Grouping is uneven across streams** [checked, measured]. Which items share a claim:

| stream | grouped by sequence or run | "asked before" items |
|---|---|---|
| continue, inhibit | sequence | **one claim for all**, at REL_FLOOR 0.05 |
| triad | sequence (walk triples) | one claim each, at 0.5 |
| pick | sequence (both directions of a root) | one claim each (branches too), at 0.5 |
| order, names | run (its windows) | one claim each, at 0.5 |
| cohere, lookalike, reasoned | none: every unit is its own claim | one claim each, at 0.5 |

**What the unevenness does.** In triad, walk triples became about 1,200 sequence claims, while 3,153 asked triads each stand alone. So asked triads went from 1 of 10 draws to 6 of 12. In cohere, a long run's windows are separate claims, though they test overlapping glyphs; in order and names they are one.

**The pattern I'd suggest.** One rule across streams: group units that measure the same thing, give unranked sources 0.5, and give each off-sequence item a claim of its own at a stated relevance (next section).

**Cohere's walks** take 2 of 76 primary draws, down from 5 of 130. In the audit I attributed the walks' small share to enumeration and the 1.0 ceiling. With the ceiling gone, most of what remains is information: the walks have mostly been asked whole already. I no longer read it as a defect.

### 4. Off-sequence re-asks

The contexts and pairs a sequence no longer serves are one claim, `OFF_SEQUENCE`, at REL_FLOOR, in continue and in inhibit. Measured:

| | continue | inhibit |
|---|---|---|
| units in the claim | 4,674 | 766 |
| claim's mean weight | 0.0154 | 0.0150 |
| median sequence claim's mean weight | 0.405 | 0.296 |
| $P$(claim drawn in a round) | 0.0025 | 0 in 400 |
| per item, per round (when drawn, one unit) | about $5 \times 10^{-7}$ | below that |
| if each item were its own claim at 0.05: share of draws | 10.5% (about 18 of 170) | 2.5% (about 1 of 42) |
| the same at relevance 0.01 | about 2.3% (about 4 of 170) | about 0.5% |

The coordinator asked whether this is too rare. I think it is, for two reasons:

- **The rate doesn't reach Joseph's long tail.** At one re-ask of a given context per two million rounds, the floor exists in the code but not in the data. His long tail ("most improbable things to sneak in still") is about individual items.
- **It shrinks as the class grows.** With one claim, each item's chance falls as $1/N$ in the number of off-sequence items, so the more contexts fall off sequences, the less any of them is re-asked. That is the dependence on enumeration size that finding 2 removed, turned upside down.

What I'd change: one claim per item. If 10% of continue is more than wanted, add a stated parameter for off-sequence relevance (0.01 gives about 2%) in place of pooling them. The cost then is a known share, chosen in the open.

The 34 wrapped ends without an end question from the audit fall into this class, so they inherit its rate.

**Reflection is resolved** [checked]: the turnaround at the sequence's own end, in both orientations. The candidates doubled, from 12,538 to 25,308, in 771 claims.

### 5. Pending answers

- **Bookkeeping.** Pending is now counted per (round, sheet, question, mind), so the void-round and `no-lookup` errors are gone by construction.
- **The 12-round horizon** turns the stale Gemini backlog back into re-ask candidates once it ages out, which was the intent.
- **Paused families.** A family whose core minds are all paused is dropped from the information (`ACTIVE`), so it's no longer a constant bonus [checked].

One edge [checked, reasoned]: `ACTIVE` is computed from `roster.core`. The pick stream is answered by `roster.generators`, and the reasoned stream by `roster.reasoners`. HANDOFF at 16:08 described exactly the case this misses: Gemini's generator tier paused while its core mind was not. In that state Gemini counts as active in the pick stream, though no Gemini mind could answer a pick, and the old constant bonus returns there. It's moot while all three are paused. What I'd change: compute the active families per stream, from the roster that answers it.

### 7. The seal

`blind()` gives canary-touching choose positions, D-control pairs and names sets the weight $n$ alone would give, so no sealed answer can steer what they're asked [checked]. One edge remains [measured on questions only, reasoned]:

- **The leak.** D-control counts are keyed by pair and pooled over the neutral contexts the pair was asked after. `fresh_glyph` draws from ranges that include Block Elements and Symbols for Legacy Computing, so a neutral context can hold a canary glyph. The seal covers any choose answer whose *context* holds one. Of the 173 D controls asked so far, 1 has a canary glyph in its neutral context and none in its pair. Its answers, if any, enter its pair's count unblinded.
- **The fix.** Reject canary glyphs when drawing neutral contexts. That also stops new sealed answers being created there. For the one already asked, blind its pair, or leave out answers whose context touches the canary; filtering by context reads no answer content.

### 8. Smaller things

- **Resolved** [checked]:
  - the docstrings (uncontested positions on equal terms);
  - `PICK_NULL_EVERY` (now sets the null's size from the picks drawn);
  - `PARAMS`, `BASE` and the branch curve, recorded in `plan.json`, with `explore`'s soft numbers stated as outside them;
  - `budget` described as a scale;
  - rounds matched and sorted by number in `plan.py`, `run.py`, `best.py` and `tree.py` (no three-digit glob is left in the study's live Python);
  - cyclic grown rows pooling their rotations when asked whole;
  - exploration at 15% of a round before jitter (86 of 852 in this dry run, after jitter).
- **The answer digest doesn't pin what was read** [checked, reasoned]. It hashes the sorted answer IDs. An ID is a hash of round, sheet, mind, question and variant, so a record can change content under the same ID. A sheet whose calls all failed becomes an answer when a drain later succeeds; a limit doesn't use up attempts. Seeds aren't in the digest. Hashing each record's content (or the sorted record lines), with the seed list, would make "why was this asked" answerable.
- **Not changed, and not needed now:**
  - `stats["reasks"]` still matches by `qid`, so it misses cohere runs shown the other way round;
  - CATALOG §12 still says lookalike draws from "recognised runs (yes share $\geq 0.5$)".

## New, not caused by either version

**Newly found kernels are the least-drawn sequences** [measured, checked]. The 523 open-ended sequences of 3–5 glyphs are drawn in about 7% of rounds, the lowest of any group. The cause is `rank` ($\text{mean agreement} \times \min(1, \text{walked}/4)$), which the relevance S-curve reads: a 3-glyph kernel has walked one step, so it ranks at most 0.25, which gives relevance about 0.15. Joseph's rule is the reverse: *"various minds start to find a sequence — call it a sequence of three glyphs. The priority is then to extend that sequence to the right and to the left as far as they will go"*. `walked/4` rewards having been walked; in the walk it is a reasonable confidence factor. As the planner's relevance it puts new kernels last. Their ends already carry $5\times$, but within a claim that's drawn rarely.

What I'd consider: relevance from mean agreement alone, with the walk's length kept out of it. That is, the strength of the links found so far, not how many there are. That's a change to what "relevance" means, so it may be Joseph's to confirm.

## What I didn't check

- I didn't rerun the stochastic-1 comparison on today's answers; its column is my audit's dry run from about 16:10.
- I didn't check `explore` beyond the share.
- I didn't look at how stochastic-2's c104 actually came out.
- The inclusion probabilities are simulations of the claim stage only. A drawn claim whose units all fail validation yields nothing, and the next claim is used.

Treat the findings above, not this list, as the check's content.
