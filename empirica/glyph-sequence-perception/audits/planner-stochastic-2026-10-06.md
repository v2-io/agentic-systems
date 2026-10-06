# Audit: the stochastic planner, `priority/plan.py` at `5ce36fa0`

*2026-10-06, Claude Opus 5.5, de novo: I hadn't seen the planner or this study before. Written for the session that will next change the planner, and for Joseph. `priority/plan.py` was byte-identical at `5ce36fa0` and in the working tree while I worked. Commit `64c9e8d0` (16:14, landed during the audit) changed `pending()` only; finding 5 covers it. I read the file whole, along with `probe/probe.py`, `tree/tree.py`, `run.py`, `core/fate.py`, METHODOLOGY (all of it, §5 most closely), the relevant parts of CATALOG, and the seal. I changed no file but this one and touched no process. Everything I ran ran in-process from my scratchpad with bytecode writes off, so nothing was written into the study tree. It ran against the answers on disk at about 16:10 (289,341 records, 969 seeds), with round id `c999`, the commit's own dry-run setting. It reproduces the commit's 1,050 questions. It gives 118 re-asks where the commit message gives 136, presumably because the answers on disk have changed since. The candidate pools match `c102/plan.json` exactly; c102 is the first round this planner drew. One planner call takes about 175 s.*

*The seal. I read no `choose` or `names` answer. Wherever a number below involves the choose, choose-control or names streams, every candidate or question whose context, pair or set contains a canary glyph (`▁ ▂ ▃ ▄ ▅ ▆ ▇ █ 🮆 🮅 🮄 ▀ 🮃 🮂 ▔ ▉`) was dropped before anything was computed or printed. Finding 7 is about the seal itself.*

Labels: **[measured]** on the current data, **[checked]** against the code, **[reasoned]**.

## The short answer

The mechanics are sound:

- **The information function is right.** It is the mutual information between one more yes/no answer and a $\mathrm{Beta}(k + \tfrac12,\, n - k + \tfrac12)$ share, and `psi` matches a reference digamma to $10^{-11}$ [checked].
- **The draw is right.** Efraimidis–Spirakis keys are drawn correctly [checked].
- **Every draw is fated.** The dry run reproduces the commit's question count and c102's candidate pools [measured].
- **The pending bookkeeping is close to exact** [measured, finding 5].
- **The identity keys line up.** Each stream's identity key matches the key `Pending` builds for the same question kind [checked].

The new principle (*"stochastic probing, weight toward where it will be most clarifying"*) is only partly realised. The most consequential findings are these:

1. **A bug: manifested cycles are asked as sequence ends, at $5\times$** [measured]. `tree.sequences()` relabels a wrap stop to `"cycle (manifested)"`, but the planner tests only `stop.startswith("wrap→")`, so it treats these stops as ends. 124 cycles give 1,064 contexts labelled `end`, which is 10% of all end weight. 173 of them show the whole period, against METHODOLOGY §4's no-spoiling rule. The heaviest candidate in the entire continue pool (weight 4.54) is the whole moon-phase period `🌔 🌕 🌖 🌗 🌘 🌑 🌒 🌓`.
2. **Within a stream, the draw follows how many candidates each source enumerates, not how clarifying they are** [measured]. Most candidates have never been asked, so their information sits at its 0.92 ceiling, and several sources sit at relevance 1.0 whatever their strength. The weights end up nearly flat:
   - In cohere, the tree's own walks carry 2.7% of the weight. The triad era's grown rows carry 38%, and runs carried by written answers 41%.
   - In inhibit, skip tests carry 82%. Recognition of the reasoned pass's candidates, which METHODOLOGY §4 calls "the test that matters", got 1 of 36 draws.
3. **"Information" here is close to 1/n, and agreement barely moves it** [measured]. At n = 10, a 5/10 split weighs 0.043 and a unanimous 10/10 weighs 0.033. Two families that disagree flatly weigh the same as two that agree. Whether that is what "most clarifying" should mean is a question for Joseph. Options are below.
4. **Hard zeros remain, against §5's "no hard zeros"** [measured]:
   - 4,543 of 23,241 shown continue contexts (20%) are in no candidate source;
   - 735 of 2,367 answered inhibit pairs (31%) aren't either;
   - the reflection at a sequence's own end is never a candidate;
   - 34 wrapped ends get no end or cycle question.

   The first three can't be re-asked by any route [measured, checked]. For the wrapped ends I checked the code only.

The rest of this report gives smaller defects, the seal question, and what I'd change (I changed nothing).

---

## 1. Manifested cycles are asked as ends (bug)

`continue_cands` [checked]:

```python
if stop.startswith("wrap→"):
    ... cycle probe ...
    continue
for k in range(2, min(MAXK, len(run)) + 1):
    put(run[-k:], rel * PARAMS["END_RELEVANCE"], "end", ...)
```

`tree.sequences()` rewrites a wrap stop to `"cycle (manifested)"` when the sequence is a manifested cycle, so that stop falls through to the end loop. On the current tree [measured]:

- The stops are end 1,408, open 757, **cycle (manifested) 229**, wrap with a period of at least 4 distinct glyphs 74, other 70, wrap with fewer than 4 distinct 25, cap 12, and wrap whose glyph lies outside the split piece 9.
- The 124 manifested-cycle sequences (periods 4 to 12) put **1,064 contexts in the pool labelled `end`, at $5\times$**. That is 10.4% of all end weight.
- **173 of those contexts show the whole period.** Answers there are repetition, by `tree.manifest()`'s own rule, so they test nothing about closure. They also can't extend a sequence that has no end, which is the reason ends get $5\times$.

What I'd change: test `stop.startswith("wrap→") or stop.startswith("cycle")`. For a manifested cycle the period is the whole run, which the cycle-probe branch already handles.

A related gap: wrap stops with fewer than 4 distinct glyphs (25), or whose glyph lies outside the piece (9), get no end question at all. Their own end context isn't a k\* or "inside" context either, because the wrapping step is filtered out of the piece's steps. Many of these look like a turnaround (`7 8 9 → 8`). That is what reflection is meant to study, and finding 4 covers it.

## 2. The draw follows enumeration size

Per stream [measured; choose and names without canary candidates]:

| stream | unique pool | effective $N$ $= (\sum w)^2/\sum w^2$ | median / max weight | where the weight sits |
|---|---|---|---|---|
| continue | 79,975 | 90,336 (over 149,371 puts) | 0.89 / 4.54 | inside 52%, end 22%, k\* 13%, lengthen 11% |
| inhibit | 7,604 | 7,746 | 0.84 / 0.92 | skip tests 82%, branch 10%, written 5%, reasoned 3.5% |
| cohere | 18,849 | 29,002 | 0.91 / 1.31 | written 41%, grown rows 38%, pick branches 8%, asked 6%, **walks 2.7%** |
| choose | 9,382 | 12,025 | 0.921 / 0.921 | steps 83%, splits 17% |
| order | 4,517 | 5,835 | 0.81 / 1.38 | runs 57%, walks 25%, asked 11% |
| pick | 7,170 | 6,054 | 0.47 / 0.92 | roots 54%, branches 42% |

Two facts produce this [reasoned, from the code and the table]:

- **The information term sits at its ceiling for anything unasked.** That is $3 \times 0.307 = 0.921$ nats, summed over the three families. In choose, the median candidate *is* the ceiling. Most candidates are unasked, so information doesn't separate them.
- **Several sources carry a constant relevance of 1.0, the top of the S-curve's range.** These are the grown rows, "every run asked before", seeds, choose splits, and choose positions taken from any run ever asked whole. Only walks (and written runs and branches) are scaled by strength.

So a source's share of the draw is roughly its share of the enumeration. What that means for c102's shape [measured, dry run]:

- **Cohere:** 42 grown rows, 36 written runs, 26 pick branches and **5 walks** were drawn. METHODOLOGY §5 says relevance makes "stable sequences squared away first". In cohere the tree's walks are the smallest source. Of the 4,905 distinct grown rows, each gets 1.0, though the rows carry `weakest` and `stability` fields that could set it.
- **Inhibit:** 28 skip tests, 4 branch runners-up, 3 written-momentum candidates and **1 reasoned candidate** were drawn. Skip tests are enumerated at every step of every sequence; reasoned candidates exist only where the reasoner answered.
- **Continue:** "inside" contexts (every length, at every interior glyph, both ways) are 61% of the puts and take 66 of 189 draws. Ends, with the $5\times$ multiplier, take 63.

This may be acceptable as a first version, but it is a different principle from the one stated. If the intent is that effort goes where a question clarifies most, the unit that relevance attaches to probably shouldn't be the individual question. Options [reasoned; for whoever owns the change]:

- **(a) Draw in two stages.** Draw the claim first (a sequence, a link, a run, an instrument position) by relevance times the information still available about it, then draw a question within it. A sequence with 300 enumerated contexts then gets no more effort than one with 30 merely for being long.
- **(b) Spread a source's relevance over its candidates.** For example, divide a sequence's relevance by the number of its contexts in the stream. That is cruder, but it fits the current structure.
- **(c) Give unranked sources a stated relevance.** The grown rows' own `weakest`, a seed's provenance, or simply the S-curve's midpoint, entered in `PARAMS`, in place of the ceiling.

## 3. What the information term measures

For one family, $I(k, n)$ [measured, from `plan.info`]:

| $n$ | $k = n/2$ | $k = 0.75n$ | $k = n$ |
|---|---|---|---|
| 1 | 0.193 | 0.189 | 0.176 |
| 3 | 0.110 | 0.107 | 0.091 |
| 10 | 0.043 | 0.043 | 0.033 |
| 20 | 0.023 | 0.023 | 0.017 |
| 100 | 0.0049 | 0.0049 | 0.0036 |

For moderate $n$ it is close to $1/(2(n+2))$ whatever the agreement. A unanimous share is down-weighted by at most about 30%. The docstring's *"about 1/(2n) once n answers agree"*, and METHODOLOGY's *"falls like 1/(2n) as answers agree"*, read as though agreement drives the fall. Mostly it is $n$ that does. Two further properties [checked]:

- **Families that disagree aren't preferred.** `counts_top` takes the pooled top answer and sums each family's own term. A context where Claude names `x` 10/10 and Grok names `y` 10/10 weighs about what one where both name `x` does. Yet a split between families is what the study's per-family reading most needs clarified.
- **Yes/no questions ignore their control.** The cohere and inhibit terms are about the yes share alone. The study reads that share against a control, so the control's $n$ also bounds what an answer can clarify.

The function is a defensible measure of "precision of a share". "Most clarifying" can mean more than that. If it should, there are options in increasing ambition [reasoned]:

- add a term for disagreement between families (a Jensen–Shannon divergence between the families' posterior means);
- use the expected information about the quantity the catalog actually reads: a share against 0.5, or a run's yes share against its control;
- once the catalog's model is frozen, weight by the expected change in its reading.

This is the most consequential design choice in the planner and the one I'd least presume to make. It is for Joseph.

## 4. Hard zeros

§5: *"No hard zeros in the planner. A rule that never asks something can never learn it was wrong."* Cohere, order, names, triad and pick each include "every one asked before" as a source. Continue and inhibit don't [checked], and the consequence is [measured]:

- **Continue: 4,543 of 23,241 shown contexts (20%) can never be asked again.**
  - **What was answered there.** 3,936 of them have "none" as their top answer, 584 a glyph and 23 something other than a glyph.
  - **Their size.** Most are 2-glyph contexts (3,324), with 3–4 answers each.
  - **How they were first asked.** Their records were mostly first asked as exploration (10,033), sequence ends (4,786) or seed steps (1,119).

  One shown "none" from each family closes a context for good unless some walk passes through it later.
- **Inhibit: 735 of 2,367 answered pairs (31%) can never be asked again.** A pair is a candidate only while its source still generates it. When a runner-up, a skip position or a reasoned candidate changes, the pair drops out.
- **Reflection:** `reflection_cands` turns back only at interior glyphs ($i \leq \mathrm{len}(g) - 2$) and in one orientation. So the reflection at the sequence's own end, `… g[-3] g[-2] g[-1] g[-2]`, is never a candidate. METHODOLOGY §3 names "whether an end behaves as a line (it reflects) or as a cycle (it wraps)" as one of the two things reflection can test.
- **Wrapped ends** without a cycle probe (34): see finding 1.

What I'd change: add "every context / pair asked before" sources to continue and inhibit, at a stated relevance (in `PARAMS`). Add the end turnaround, and the reverse orientation, to reflection.

The residual cuts in `explore` (`seqs[:200]` and $\mathrm{rank} \geq 0.9$ decide which glyphs count as settled for the one-in-two redraw) are soft in effect. They are still fixed numbers outside `PARAMS`.

## 5. Pending answers

`Pending` is a good idea, and its count is close to exact. Counted per round, sheet and mind, the backlog is Gemini 38,860, Grok 10,568 and Claude 2,562; the planner's own count is 38,755 / 10,563 / 2,399 [measured; canary choose and names questions left out]. Two small errors explain the gap [checked]:

- records from void rounds subtract from the same question's live copies;
- a sheet re-asked as `no-lookup` yields two records (1,581 such entries), so it subtracts twice.

Both would go away if pending were computed per (round, sheet, mind), which is the comparison I ran.

The larger issue is dynamic [measured, reasoned]. Gemini's pending answers number **about 1,000 per round for c006–c027 and c080–c091**: those rounds are essentially unanswered by Gemini, and 23,357 of its pending answers are continue questions. Its drain runs `--newest-first`, with continue last in `--kinds-first`, and each new round adds about 1,100 Gemini assignments. So those answers will plausibly never arrive.

The planner still counts each of them as an expected answer. For a context with one Gemini answer pending, Gemini's term drops from 0.307 to 0.193. The weight of every context asked in those rounds is suppressed by about a fifth to a third. Yet a re-ask is the only route by which Gemini will answer them, because its drain will reach a new round's copy and not the old one.

What I'd change: give pending answers a horizon. One way is to count a family's pending answer only while its round is within the drain's observed reach (rounds behind the newest that the family has answered recently). Another is to discount each pending answer by the drain's measured completion rate for that round's age.

`lookalike_cands` counts no pending answers at all [checked]. That is a smaller inconsistency.

**Since `64c9e8d0` (16:14).** A mind listed in `data/logs/paused.json` with a future time has none of its assignments counted as pending. All three Gemini minds are listed there now, until about 2026-10-10 13:50. That removes the stale expectation for as long as the pause lasts. It also creates the opposite effect [reasoned]:

- For four days, every context Gemini hasn't answered keeps Gemini's full unasked term (0.307), and no answer from Claude or Grok can reduce it.
- So the planner leans toward exactly the contexts Gemini lacks, though only Claude and Grok can answer them. They will re-ask those contexts, repeatedly, of the other two families.
- When the pause ends, the backlog above counts again.

What I'd change: while a family can't answer at all, drop its term from `info_fams` instead of treating it as unasked. Keep a horizon on pending answers for the general case. A smaller point: if only one mind of a family is paused, that mind's records still subtract from the family's other assignments.

## 6. Order answers of "none" are invisible to the planner (bug)

`Tree` stores order answers only when the outcome is `lines` [checked]. So `order_counts` counts neither "none" nor unparsed answers. On the current data [measured]:

- ctx-era order outcomes are 1,138 lines and 512 none;
- triad-era outcomes are 5,700 lines and 1,024 none;
- **453 of 1,637 asked sets have answers but no `lines`**.

Those 453 sets sit at the ceiling of 0.92 forever, and they're absent from the "asked" source. Elsewhere $n$ is undercounted. `names_counts` does count none and unparsed, so the two set questions are read differently.

What I'd change: give `order_counts` every answered order record, as `names_counts` has. That probably means a new `Tree` index (by shown set, all outcomes) and not a change to `orders`, which other readers use.

## 7. The seal

The seal says *"No read-off reads `choose` answers today (`report/best.py` and `run.py`), so nothing surfaces them by accident."* That is still true of read-offs. But since `5ce36fa0` the planner reads them [checked]:

- `choose_cands` weights each position by `Tr.choose`;
- `choose_control_cands` weights by `Tr.choose_ctl`;
- names candidates are weighted by `names_counts(T)`.

All of these include canary positions and sets.

**What escapes.** Weights aren't written anywhere. The questions drawn are written to `questions.jsonl`, which is committed. So how often a given canary position is re-asked is a function, through $I(k, n)$, of its sealed answers.

**How much escapes.** Very little [reasoned, from finding 3]:

- $I$ is symmetric in $k \leftrightarrow n-k$, so the direction of a preference doesn't affect the weight at all;
- the strength of a preference shifts the weight by at most about 30%;
- the planner's draw noise is far larger than either.

Still, someone who tabulated canary re-ask counts over many rounds would be reading a faint shadow of the answers.

What I'd change: for any choose, choose-control or names candidate that touches a canary glyph, compute information from $n$ alone (`info(n/2, n)` per family). That closes the channel at no cost. Add a line to the SEAL file saying the planner reads these answers and how they're neutralised. This finding is the seal-holder's to weigh. I'm reporting it, not ruling on it.

## 8. Smaller things

- **Docstrings contradict the code on uncontested choose positions** [checked]. `contested()` says *"The planner asks uncontested positions too, at lower relevance"* and `choose_cands` says *"uncontested ones at lower relevance"*. The module docstring and METHODOLOGY §5 say *"on equal terms"*, and the code gives them equal terms.
- **`PICK_NULL_EVERY` is unused.** It is listed in `PARAMS`, and so written into every `plan.json` as though it were in effect. The null's size comes from `BASE["pick-null"]`, jittered independently of `pick`, so the ratio of nulls to real picks varies from round to round (c102: 41 to 194).
- **"Every number named here is listed in PARAMS" isn't so** [checked]. Outside it:
  - the 1.0 relevances of the unranked sources;
  - `BRANCH_*`;
  - `explore`'s 200, 0.9, one-in-two redraw and thirds;
  - the even near/far split for decoys;
  - `MAXK`, `FRESH_TIERS` and `BASE`.

  `plan.json` records only `PARAMS`, so `BASE` and the branch curve can change without a trace in the round's record.
- **A round's draw can't be reproduced afterwards** [reasoned]. It is fated given its inputs, but the inputs aren't recorded: the drains keep appending to old rounds' ledgers. A digest of the answer IDs read (with their count) in `plan.json` would make "why was this asked" answerable later.
- **`--budget 700` is no longer a count.** `BASE` sums to 925 at budget 700, and c102 drew 1,113 questions [measured]. It is a scale now; the name and the CLI help could say so.
- **The mix between streams is inherited.** `BASE` is the mean of c096–c100, rounds drawn by the greedy planner the commit retires. Within a stream everything is now weighted; between streams, the old allocation stands, plus jitter. That is the largest allocation decision in a round, so it is worth stating as a choice to revisit. It's also stated in the docstring: I'm not saying it's hidden. Exploration's base is 11% of the round; Joseph's quote in §5 says 15%, and METHODOLOGY says "about 10%".
- **Lookalike substitutions change every round** [checked, measured]. The swap position and glyph are fated by round, so each re-ask substitutes differently. Their answers are pooled by `of` for information, which matches the catalog's run-level count. So far, every one of the 120 runs asked has exactly one substitution. CATALOG §12 still describes the source as "recognised runs (yes share $\geq 0.5$)"; the planner now uses a soft S-curve.
- **`stats["reasks"]` undercounts** [checked]. It matches by `qid`, and a cohere run shown in the other orientation gets a new `qid`.
- **Round 1000** [checked]. `glob("c[0-9][0-9][0-9]")` in `plan.py` (pending, `asked_before`) and in `run.py` (`ctx_rounds`) doesn't match `c1000`. String comparison also puts `c1000` before `c101`. At about 100 rounds in two days, that's a few weeks out. Outside this audit's file, but the loop would stall there.
- **Cyclic grown rows are asked as linear runs.** `counts_yes_run` calls `Tr.coherence(g)` without `cyclic`, so the information term doesn't pool answers to their rotations [checked].

## What I didn't do

- I didn't run a sensitivity analysis of `PARAMS`.
- I didn't check `explore`'s seed-bump weights against the seed file's `bump` field.
- I didn't audit `probe.py`, `tree.py` or `run.py` beyond what the planner touches. The `run.py` change committed at 16:08 (`c6085914`, limit pauses) didn't touch anything the planner calls.
- The canary-free aggregates in finding 2 cover choose and names candidates whose answers, if any, I didn't see. Their weights entered only as sums.

Treat the findings above, not this list, as the audit's content. A defect not mentioned here hasn't been ruled out.

## On the brief

The brief suited the work. Its two facts (the loop reloads `plan.py` on restart; the seal's scope) were exactly what I couldn't have seen, and both shaped how I worked. I ran the planner in-process from outside the tree, and filtered sealed streams before computing anything. If a follow-up is useful, findings 1, 4 and 6 are mechanical fixes I could draft as a patch in the scratchpad for review, without touching the live file.
