# Check: planner stochastic-3 against the check of stochastic-2

*2026-10-06, Claude Opus 5.5, the author of the audit of stochastic-1 and of the check of stochastic-2. Not de novo: most of what stochastic-3 changes is what I suggested, and I've looked hardest at those changes. Written for the coordinating session before stochastic-3 goes live, and for Joseph if he wants it. I changed no file but this one, touched no process, and didn't look in `spikes/family-disagreement-2026-10-06/`.*

*What I read and ran.*

- **Read whole:** the diff `34398d6f..c32fdfbc` of `priority/plan.py`. The working tree matches `c32fdfbc`; no other file changed.
- **Ran:** the planner in-process from my scratchpad with bytecode writes off, against the answers on disk at about 16:50, with round id `c999`.
- **Gemini:** paused, so the active families came out as Claude and Grok, and Claude alone for the reasoned stream.
- **Slot counts:** from a copy of `Cands.draw` with logging added and the logic unchanged.

*The seal.* As before, choose, choose-control and names results are left out of everything below, apart from one count of answered choose positions with every canary-touching position excluded first.

Labels: **[measured]**, **[checked]** against the code, **[reasoned]**.

## The short answer

I found no defect that should hold stochastic-3 back from going live. Every change does what the check asked:

- **Slots are drawn with replacement**, so the one-question cap is gone.
- **Off-sequence items are each their own claim.** In continue they come up at about the rate the check estimated: 2 of 170 here.
- **No context showing a whole period was drawn**; one was refused.
- **The D-control edge of the seal is closed** from both sides.
- **Active families are counted per stream**: picks see Claude and Grok, the reasoner Claude.
- **The digest covers record content and seeds.**

There is one trade I'd want decided, and it is Joseph's as much as anyone's. **Relevance from raw mean agreement saturates, and it rewards thin evidence.**

- 69% of sequences now sit at relevance $\geq 0.85$; under `rank` it was 37%.
- 60 of 170 continue questions go to 3–5-glyph sequences whose every link rests on at most 2 answers.
- Information already favours those, because they have few answers. So relevance and information now pull the same way, and "the most obvious and stable sequences squared away first" no longer has a lever.

The walked/4 problem was real. This change replaces putting new kernels last with putting thinly evidenced ones near the top. The S-curve's narrow width (0.12) is half the cause.

Smaller:

- The drawing-with-replacement mechanism allows concentration, but the weights hardly produce it: the heaviest continue claim expects 0.41 slots a round.
- "Every stream" re-ask coverage misses the reasoned stream: 204 of 951 answered contexts can't be re-asked.
- The no-spoiling rule on pick contexts is a judgment call, not a validity rule. It cost nothing this round.

---

## What's resolved

| from the check | stochastic-3 | status |
|---|---|---|
| off-sequence re-asks pooled into one claim | each its own claim at `OFF_SEQUENCE_RELEVANCE` 0.01 | **resolved** [measured]: 2 of 170 continue draws, 0 of 42 inhibit (expected about 0.2 a round) |
| breadth first: one question per sequence a round | claim slots drawn with replacement | **resolved as a mechanism** [checked]; see "Concentration" below |
| uneven grouping across streams | asked triads, sets and pick contexts at 0.01, each its own claim; runs asked whole at 0.5 as runs | **resolved** for those streams [checked]; reasoned not covered (below) |
| 38 whole periods through other sequences | validity: no continue or pick context shows a whole manifested period, any rotation or direction | **resolved** [measured]: 1 refused (a reasoned context), none drawn |
| D control after a canary-holding neutral context | neutral contexts exclude canary glyphs; tainted pairs found from questions and weighted by $n$ | **resolved** [checked]; the taint is read from `questions.jsonl`, never from answers |
| `ACTIVE` from the core roster only | per stream, from the roster that answers it | **resolved** [measured]: pick → claude, grok; reasoned → claude |
| digest over IDs | over every record's content and the seeds | **resolved** [checked]; it adds about 20 s to a plan (191 s here) |
| kernels drawn least (`walked/4`) | relevance from the sequence's mean agreement | **resolved, and traded** (next section) |

The spoiling check matches every rotation and both directions against the canonical periods in `T.cycles` [checked]. Bouncing-spinner periods repeat glyphs, so they can never appear whole in a context; nothing is lost by not matching them.

## The trade: relevance from mean agreement

Relevance across the 1,292 sequences [measured]:

| relevance (rounded) | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| `rank` (stochastic-2) | 433 | 150 | 66 | 56 | 52 | 12 | 22 | 49 | 116 | 359 |
| mean agreement (stochastic-3) | 16 | 19 | 1 | 14 | 193 | 15 | 27 | 143 | 314 | 573 |

Two things cause the bunching at the top [reasoned, checked]:

- **The observed share isn't shrunk.** A link named by the one answer its context has received has agreement 1.0, the same as one named 20 times out of 20. Among the sequences at relevance $\geq 0.9$, 42 of 3–5 glyphs rest on at most 2 answers per step, and 2 on seed votes alone.
- **The S-curve is narrow.** At midpoint 0.5 and width 0.12, any agreement above about 0.75 is already within 10% of the ceiling. `rank`'s $\min(1, \text{walked}/4)$ was, in effect, what spread the curve's input; without it, little does.

Where the continue draw went, by sequence length and how many answers support its links [measured]:

| | questions (of 170) |
|---|---|
| 3–5 glyphs, every step $\leq 2$ answers | 60 |
| 3–5 glyphs, more | 48 |
| 6+ glyphs, every step $\leq 2$ answers | 1 |
| 6+ glyphs, more | 59 |
| off-sequence | 2 |

That's roughly in proportion to how many sequences of each kind exist, so the draw is close to flat across sequences.

Information already sends questions toward thinly answered contexts. With relevance now high for them as well, the one term that was meant to separate "stable" from "new" doesn't. So Joseph's two rules no longer have anything weighing them against each other:

- *"extend that sequence to the right and to the left as far as they will go"*;
- *"square away the most obvious and stable (empirically) sequences"*.

Options [reasoned]; which one fits is Joseph's call:

- **Relevance on the lower bound of agreement**, the study's own one standard (METHODOLOGY §2a, `tree.estimate`). The values below assume both families answered, each giving the counts shown:

  | each family's answers | relevance |
  |---|---|
  | 1 of 1 | about 0.57 |
  | 2 of 2 | about 0.81 |
  | 10 of 10 | about 0.97 |

  A strongly evidenced kernel ranks high, whatever its length. A single-answer one ranks in the middle, and information still sends questions to it. This keeps the walked/4 fix.
- **A wider S-curve** (for example width 0.25), so agreement between 0.6 and 0.95 stays distinguishable. It's simpler, but it shrinks nothing.
- **Leave it.** If extending kernels is meant to dominate for now, the current behaviour does that. I'd then state it in METHODOLOGY §5, since "stable sequences squared away first" no longer describes it.

## Concentration

Drawing with replacement removes the cap [checked]. How far it concentrates depends on how much claim weights differ, and they don't differ much [measured]:

- **The heaviest claims expect less than one slot a round.** The heaviest continue sequence claim expects 0.41 slots a round. In inhibit, cohere and pick, the heaviest claim expects 0.01–0.04.
- **Hardly any claim gets two questions.** The most any claim got here was 2 continue questions; your dry run saw 3, on slightly different answers.

So a strong sequence can take several questions in a round, but in expectation none does. That's no fault of the mechanism; it reflects the weights. With the relevance trade above, the weights are flatter than before. If "squared away first" should have teeth, the lever is the spread of relevance, not the draw.

A minor point [checked]: a claim's weight stays the mean of all its units after its heaviest unit has been asked. A sequence claim lifted by its $5\times$ ends keeps that lift for the rest of the round, though its remaining units are inside contexts. At under one slot per claim in expectation, this hardly matters.

## Smaller things

- **Re-ask coverage isn't "every stream"** [measured]. Streams with no asked-before source:

  | stream | answered | can't be re-asked |
  |---|---|---|
  | reasoned | 951 | 204 |
  | choose (canary positions excluded) | 491 | 2 |
  | reflection | 989 | 2 |

  The reasoned gap is the only sizeable one: contexts whose sequence end has moved or stopped being a felt end. Re-asking those may be worth little, but it's the same kind of hard zero as finding 4. Either add an asked-before source at `OFF_SEQUENCE_RELEVANCE`, or narrow the commit's and docstring's "every stream".
- **No-spoiling on pick contexts is a judgment call** [reasoned]. For continue, METHODOLOGY §4 makes it a rule: a repeat must be the mind's own. A pick is a forced creative extension. Shown a manifested cycle whole, "repeat it" is one answer, and the other branches (a cycle's tendrils) are what the generator is for. It cost nothing this round (no pick context refused), so it's only the principle. I'd keep the rule for continue and leave picks to Joseph, or to whoever owns §4a.
- **The off-sequence rate is as estimated** [measured]. 2 of 170 continue draws were off-sequence, about the 2% the parameter's comment gives; 0 of 42 inhibit, against an expected 0.2 a round.
- **Not addressed, as you said:** CATALOG §12's wording and `reasks` by `qid`.

## What I didn't check

- I didn't recompute the tables of the check of stochastic-2 under stochastic-3. The comparisons above are between dry runs about 40 minutes apart; a few rounds' answers had arrived in between.
- I didn't time stochastic-3 against a round's length.
- I didn't look at c104 or later, which stochastic-2 drew.

Treat the findings above, not this list, as the check's content.
