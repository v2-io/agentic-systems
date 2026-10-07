# Audit: planner stochastic-5, and the two commits it rests on

*2026-10-06, about 20:50–21:15. Claude Opus 5.5, de novo: I had not worked on this study before. Written for the coordinating session and Joseph, before the loop is restarted on stochastic-5. I read the earlier planner audits after my own first pass, for their format and to avoid repeating them.*

*What I read whole.* `METHODOLOGY.md`, `CATALOG.md`, the seal, `priority/plan.py`, the code diffs of `c5ecf912`, `059cdf04` and `e3fdfa1c`, `catalog/code_order.py`, the parts of `tree/tree.py` the commits touch (the loader, `estimate_vs`, `coherence`, `own_shuffles`, `as_sequence`), the parser and prompt code of `probe/probe.py`, and `run.py`'s plan, ask, record, drain and loop code. Of `HANDOFF.md`, the running-processes and recent sections. Of the generated pages, `CATALOG-VIEW.md`'s header and counts only.

*What I ran.* All from my scratchpad (`…/scratchpad/s5audit/`), writing nothing in the study:

- **Dry plans.** The planner in-process: stochastic-5 as committed, and stochastic-4 (`c5ecf912`, extracted whole into the scratchpad with `data/` linked), on the same answers (338,346 records, read at about 20:52) and seeds, for three dummy round ids `zs5a`–`zs5c`. In both, p003's records were the ones the current parser makes from its ledgers (see P4 for why the stored ones differ).
- **p003 re-parsed** from its ledgers with the current `probe.records`.
- **Catalog queries.** Build `b20261006_204928`, model `catalog-v5-build7`.
- **Tree computations.** `as_sequence` and `seq_rel` over every run asked whole; a simulation of the paired test under a null.

*The seal.* I read no `choose` or `names` answers. The dry plans read them in-process exactly as the planner does, through `blind()`; I counted the `choose` *questions* they drew, never answers. Everything else reads cohere, insert and remove answers, and catalog records built with sealed answers dropped.

*Files.* I wrote only this report. Bytecode writing was off for every run that imported study code.

Labels: **[measured]**, **[checked]** against the code, **[reasoned]**.

## The short answer

**Nothing in stochastic-5 corrupts answers, and its sizes, packing, determinism and seal handling are sound.** But two things should change before the restart, and one operational step goes with it:

- **P1. "Encoded" includes orders the study has measured minds don't read off the chart.** `code_order` counts any run monotone in code points, across blocks and at any length from 3. CATALOG §7a measured that chart order is at chance across three blocks. So the factor, and the view's exclusion, take in cross-block morph and count ladders this study looks for: `-=≡≣`, `=>→⇒⇛`, `.․‥…⁘⁙⁛`, `☆⭐🌟`, `<≪⋘⪢⫸`, `🌌☀🌍🐘🐜🦠`. They also take in `∣∥⫴`, what two minds left of Joseph's `˚˙·∣∥⫴` in p003. Within one block, they take in gapped runs that only D can judge, such as `-=>`, the opening of his founding ladder. For 3-glyph runs whose glyphs sit in three different blocks, the label fires at 0.39 against 1/3 by chance.
- **P3. Insert and remove are never asked of runs longer than 8 glyphs.** `Plan.add` has no length entry for them and falls back to the 2–8 limit for shown contexts. That leaves out 1,944 of the 4,219 candidate runs, Joseph's own `┉┈┄─━▬█▌▍` among them. The fix is one line.
- **P4. Restart the drains with the loop.** They still hold the 15:55 `probe.py`, which has no insert or remove prompt. A Gemini `no-lookup` re-ask rebuilds its prompt in the drain, so it would get the inhibit wording. Gemini is paused until Saturday about 13:50, so this is latent. Meanwhile the loop's record step, also on old code, rewrites `data/answers/p003.jsonl` every round as 64 "unparsed" records.

**P2** (which instruments the encoded factor should spare) belongs with P1's ruling. P5–P10 can follow.

**If you restart as is, nothing breaks.** For as many rounds as it runs, cross-block ladders get a tenth of their questions, and the instruments that could clear them get a quarter. Insert and remove see only short runs.

## P1. "Encoded" counts cross-block orders, and short runs at about chance

**The rule** [checked]. `code_order` returns "monotone" for any run of 3 or more glyphs whose code points rise or fall throughout. Blocks and gaps aren't considered. "Rotated" and "interleaved" have length guards against chance, "rotated" from 5 glyphs, as its comment explains: a random order of $n$ is a rotation of a monotone one with probability $2n/n!$. "Monotone" has no such guard. The rule is shared by the build (`CATALOG-VIEW.md` leaves out every recognised run it flags) and, from stochastic-5, by the planner (×0.1 wherever the given factor applies).

**What the study measured** (CATALOG §7a, `spikes/contested-positions-2026-10-06/`). Triad middles depart from the code-point median 0.13 of the time within one block, 0.20 for the lone glyph in two-block triples, and 0.69 across three blocks, which is chance. The catalog therefore counts the chart route only within a block. `code_order` doesn't.

**Chance, by length and block count** [measured over all 16,573 catalog records]:

| run | records | flagged encoded | a random order would be |
|---|---|---|---|
| 3 glyphs, three blocks | 314 | 0.389 | 1/3 |
| 3 glyphs, one block | 2,115 | 0.615 | 1/3 |
| 4 glyphs, four blocks | 65 | 0.215 | 1/12 |
| 4 glyphs, three blocks | 226 | 0.173 | 1/12 |

So across blocks, most 3-glyph flags are what any order would get. Longer cross-block runs are flagged above chance [reasoned]. Unicode allocated plain forms first and elaborated forms later (ASCII, then Latin-1, General Punctuation, Mathematical Operators, Miscellaneous Symbols, the emoji planes), so a ladder from plain to elaborate tends to climb in code points without anyone reading the chart.

**On the view** [measured, build `b20261006_204928`]. Of the recognised runs with no given relation, 1,381 are flagged encoded:

| kind | runs |
|---|---|
| contiguous in code points (a chart snippet) | 866 |
| one block, with gaps | 406 |
| two blocks | 84 |
| three or more blocks | 25 |

The 109 cross-block runs include `%‰‱`, `+⧺⧻`, `-=≡≣`, `-∼≋`, `-→↔`, `=>→⇒⇛`, `>→⇉⇶`, `|❘❙❚`, `_⎺⎻⎼⎽`, `.․‥…⁘⁙⁛`, `0⚀⚁⚂⚃⚄⚅`, `¼⅐⅑⅒`, `<≪⋘⪢⫸`, `⁎*∗★✭✶`, `☆⭐🌟`, `→⇒⇉⇛⇶⟹⟾⟿⤀`, `∘ₒᵒoO`, `Tᴛtₜᵗ𝑡𝕥`, `🌌☀🌍🐘🐜🦠` (interleaved: cosmos, sun, earth, elephant, ant, microbe). If cross-block runs weren't counted as encoded, the perceived list would grow from 336 to 445.

**In the plans** [measured, three dry rounds, non-control questions whose served run is 3+ glyphs and not a given walk; served run = the question's `seq`, else its own run]:

| served run | stochastic-4 | stochastic-5 |
|---|---|---|
| encoded, contiguous | 436 | 97 |
| encoded, one block with gaps | 277 | 73 |
| encoded, across blocks | 129 | 40 |
| all encoded | 842 of about 1,700 | 210 of about 1,665 |

My count differs from the commit's "167 → 53 of ~830", because it includes picks and every question that names its sequence. Both counts show about a fourfold cut.

**Joseph's own runs** [checked]: `-=>` monotone (all ASCII); `∣∥⫴` and `·∣∥⫴` monotone (two and three blocks); `▁▃▅▇` monotone. His four p003 runs and the two runs insertion produced from them are "none".

**What I'd suggest.** The definition is Joseph's to rule on, so here are three readings, each grounded in something measured:

1. **Contiguous only.** Runs whose glyphs are consecutive code points, in either direction, or rotated within one block. This is exactly the catalog's own "undiscriminable on the chart route" (no contested position), and it is what "snippets of the unicode panes" describes.
2. **One block.** Add gapped runs within one block, where §7a shows the chart pulls. Their gaps are contested positions, so D can test them (P2).
3. **As now**, but with the reasons above stated on the view.

I'd take 1 for the planner's factor and 1 or 2 for the view. In any case I'd drop cross-block runs from "encoded", since the study's own measurement says the chart isn't what minds use there. Either way, a 3-glyph monotone run is flagged at about chance outside a block, and that deserves a guard like the one "rotated" already has.

## P2. The exemption is narrower than its reason

**What's exempt.** The commit exempts lookalike, *"whose job is testing those runs"*. `view.py`'s own limits name two instruments that can separate a perceived order from a chart reading: lookalike substitution and the name-only question. CATALOG §7b adds D: at a contested position, a preference for the run's glyph over the chart's is *"the strongest evidence D gives"*.

**What the factor does to those instruments** [measured, three dry rounds]:

- **D.** `choose` questions at encoded runs fell from 91 to 24 of about 200. That covers steps of gapped monotone runs and splits whose context runs up the chart. I classified each question by its context plus the run's glyph, which approximates the claim the planner uses.
- **The name-only question.** It is under the factor too (`served=claim` for ordered runs). Its counts on encoded runs are small either way: 3 under stochastic-4, 4 now.

**The consequence** [reasoned]. The view leaves out encoded runs by `code_order` alone. So no measurement can take a run off the encoded list, and stochastic-5 also slows the measurements to a quarter or less, except lookalike, which reaches only runs with a confusable (454 of 1,203 monotone runs, per CATALOG §7b).

**What I'd suggest.**

- Exempt `choose` (steps and splits) and `names` along with lookalike: they're known-answer instruments for exactly this question, as G6 argued for lookalike.
- Alternatively, or as well, let the view keep an encoded run whose chart route is positive at a contested position. CATALOG §7c already computes that state.

## P3. Insert and remove are capped at 8 glyphs

**The cause** [checked]. `Plan.add` takes its length limits from `{"cohere": (3, MAX_RUN), "order": …, "names": …, "pick": (2, MAX_RUN)}.get(kind, (2, MAXK))`. Insert and remove aren't listed, so they get 2–8. `probe.question` accepts 3–24, and `fill_cands` offers runs up to 24. A longer run's unit is refused at `add`; in `Cands.draw` its claim is then exhausted and leaves the draw, silently.

**The effect.**

- **A direct test** [measured]: `P.add("insert", list("┉┈┄─━▬█▌▍"))` returns False; at 8 glyphs it returns True.
- **The dry rounds** [measured]: 92 insert and remove questions; the longest was 8 glyphs.
- **The candidates** [measured]: 1,944 of the 4,219 runs asked whole are 9–24 glyphs, roughly 40% of the stream's weight (relevance × the encoded factor, before information, which is the same for every unasked run).

So the long tail of the stream is a hard zero, against METHODOLOGY §5, and the run Joseph first asked about is in it.

**The fix.** Add `"insert": (3, PR.MAX_RUN), "remove": (3, PR.MAX_RUN)` to that table.

## P4. Old code in memory: the drains and the record step

**Who holds what** [checked, `ps` and `git log`].

| process | started | holds |
|---|---|---|
| Gemini drain | 16:08 | `probe.py` of `5ce36fa0` (15:55), the last commit to it before they started |
| Grok drain | 16:08 | the same |
| Grok generator drain | 17:20 | the same |
| loop | 20:39:51 | code from 15 s after `059cdf04`; its parser has no insert or remove, as its p003 records show |

**The drains.**

- **Base prompts are safe.** They come from the sheet (`s["prompt"]`), written at plan time.
- **A `no-lookup` re-ask isn't.** `ask_mind` rebuilds it with `PR.prompt(s, "no-lookup")`, in the drain's own module. The old `_lines` has no insert or remove branch, so it falls through to the inhibit wording: *"…then one candidate symbol … yes / no / can't tell"*, with no candidate shown. The answer would then parse as unparsed or "none", and the sheet would count as answered for that mind.
- **Only Gemini is exposed.** Re-asks follow tool attempts, and only Gemini has tools. Its three minds are paused until Saturday about 13:50 (`data/logs/paused.json`). So this bites only if the drains are still running old code then.
- `HANDOFF.md`'s restart note names only the loop.

**The record step.**

- **What it does.** `cmd_record_all` runs inside the loop and re-parses every round, test rounds included, with the in-memory parser.
- **What it has done** [measured]. `data/answers/p003.jsonl` (written 20:48) holds 64 records, all `unparsed`, reason `answer:`: they fell into the yes/no branch. Re-parsed from the ledgers with the current code, they reproduce the commit's p003 statements exactly.
- **The effect.** The catalog build, a subprocess on new code, reads those stale records until the loop restarts. They do no harm there, because nothing in the build uses insert or remove yet.
- **One more reason to restart.** Records parsed before `e3fdfa1c` carry no `where`, so the tree would count every insertion in them as "not found". Every record is re-parsed after the restart, so this goes away with it.

**What I'd suggest.** Restart the three drains with the loop. And add to `HANDOFF.md`'s restart note: everything that imports `probe`, which includes the drains, holds its code until restarted.

## P5. `seq_rel` ranks unmeasured runs above most measured ones

**The rule** [checked]. `seq_rel` gives a run whose own shuffles were never asked `UNRANKED_RELEVANCE` (0.5). Otherwise it applies the S-curve to the point difference $d$. That curve is centred at 0.5 with width 0.12, chosen for agreement lower bounds.

**The distribution** [measured, 4,219 runs asked whole]:

- 102 runs have no own shuffles.
- The rest have a median $d$ of about 0.33, which puts 69% of them below 0.5 relevance.
- That includes 936 of the 2,197 runs recognised as sequences.

So a run never controlled outranks most runs shown to be sequences. With 102 such runs, the effect on draws is modest.

**A smaller point.** `rel_of` uses the lower bound (the study's standard), while `seq_rel` uses the point difference.

**What I'd suggest.** Use the lower bound, and give unmeasured runs the curve's value at $d = 0$, or the median of measured runs, rather than its midpoint.

## P6. Recognition as a sequence: about 6.6% pass by chance

**What build 7 changed.** It brings the code in line with METHODOLOGY §2a and §4a: a run is recognised when its order beats its own shuffles. That is the right direction.

**The threshold is loose for a list this long.** The test is one-sided, at 90%, per run.

- **The null rate** [measured]. I simulated each run's own and shuffle answers under a common rate per family, at their actual counts. The null pass rate is 0.066 on average: 0.09 for runs with one own answer, 0.06–0.07 for 3–5.
- **What that means for the view** [reasoned]. Among the 1,541 measured runs that are neither given nor encoded, 1,205 fail. If those are mostly null, about 85 of the 336 on the perceived list are expected by chance.
- **Beside R** [measured]. 190 of the 336 also pass R at a Bayes factor ≥ 10. CATALOG §9 states certainty as a Bayes factor.

**What I'd suggest.** Either show the expected chance count on the view, or decide the paired contrast by a Bayes factor as §9 does for R. Sorting by the lower bound already puts the strongest first; it's the headline count that carries the chance share.

## P7. What insert and remove answers are evidence of

**Insertions fill code-point gaps** [measured, p003].

- **`▉▊▋`, the headline insertion (3 of 4 minds),** is U+2589–U+258B: exactly the code points between `█` U+2588 and `▌` U+258C.
- **`≈`** (U+2248) lies inside the span `∼` U+223C … `≋` U+224B.

**Where that leads** [reasoned]. Proposed runs become cohere candidates. `┉┈┄─━▬█▉▊▋▌▍` has code order "none", so if minds recognise it, it lands on the perceived list. This is a route by which chart-filled runs enter, and P1's rule can't see it.

**What I'd suggest.** Record, per insertion, whether the inserted glyphs are the exact code points between their neighbours, within that span, or outside it. That makes it a marker in CATALOG §7b's sense.

**Remove draws removals from shuffles more often than from runs** [measured, p003]: 11 of 16 shuffled answers against 6 of 16 on the runs. The planner uses remove's found share only for information, which is fine. But no reader should read it without its control. Insert's controls were quieter: 1 inside insertion in 16.

**Two smaller points.**

- An insertion at an end (an extension) counts as "not found" and isn't used as continuation evidence. It stays in the record, so nothing is lost.
- "Found" means inside insertions for insert, but any removal, ends included, for remove. That may be intended; it should be stated.

## P8. The seal and insert questions on canary runs

**Canary glyphs come up often** [measured]. 14 of the 92 insert and remove questions in the dry rounds touch canary glyphs, because block ramps are common runs. 20 candidate runs of 8 glyphs or fewer hold two or more canary glyphs; one holds the canary's `█🮆`.

**Why it matters** [reasoned]. An insertion between `█` and `🮆`, or between `▇` and `█`, says whether `▉` belongs there. That is the discriminator the seal protects, asked in another form. The seal's letter covers only `choose` and `names`. Its addendum extended it to `names` on these same grounds: *"knowing its answers would steer the name route's rules, which the freeze fixes"*.

**A question for Joseph.** Should insert and remove answers on runs holding canary glyphs be sealed too? That would mean blinding them in the planner and dropping them in readers, as with `names`. It costs little now and can't be done after they've been read.

## P9. "Given" means one thing on the view and another in the planner

- **On the view.** It leaves out any run with a given relation (`given_kind`). That includes dress runs, dress-windows and walks that change dress: 53 recognised runs that aren't given walks.
- **In the planner.** It applies `GIVEN_RELEVANCE` only to given walks (G1, one dress).
- **The ruling.** `HANDOFF.md` says Joseph hasn't confirmed G1. The view's change (`62992c16`) cites him: *"all the different encodings of essentially the same alphabet and digits ... a whole world that we can just call 'given'"*. One ruling should govern both, and the stochastic-5 commit's quote (*"Far too many resources spent ... on 'given' sequences"*) suggests it may be the wider one.

## P10. Documents and provenance

**METHODOLOGY §5 and CATALOG haven't been updated since 19:11** [checked]. They don't mention:

- build 6 (`paired`, `code_order`) or build 7 (recognised as a sequence);
- the insert and remove questions;
- stochastic-5.

**CATALOG's own text is out of date** in three places:

- §11 still says the view shows runs recognised by R, O or L with certainty, and leaves out given walks.
- The freeze list (§13) names neither `code_order.py` nor the paired rule, though the view now depends on both.
- METHODOLOGY §4a's table of tests has "missing rung" and "intruder"; insert and remove are close kin and could be mapped to them.

**Provenance** [checked]:

- The catalog manifest's code hashes don't include `catalog/code_order.py`, or `report/best.py`, both of which the build now imports.
- `plan.json` hashes the givens, but not `code_order.py`, which now moves the plan.

## Checked and found sound

- **Sizes** [measured]. Every other stream draws the same number of questions as under stochastic-4. Insert and remove add 36–52 questions a round, controls included. Explore's size differs by a fated re-draw (its factor is drawn after the two new streams), not by design: 144/198, 146/117, 124/149.
- **Packing** [measured]. The dry rounds' insert and remove questions pack into 53 sheets of at most 5, with no sheet holding a run beside its own shuffle. Every prompt is the insert or remove wording.
- **p003** [measured]. The commit's statements reproduce from the ledgers: insert `▉▊▋` (3/4) and `≈` (3/4), 0/4 on their shuffles; `˚˙·∣∥⫴` drew a removal from all four minds, `˚˙·` from 2; `_-∼≋` and `↑↗→↘↓` drew none.
- **`code_order` moved unchanged** [checked]. It is the same body, cached by tuple. The build's call passes a string, which tuples to the same glyphs.
- **Control rates** [reasoned]. Stochastic-5 asks far fewer contiguous-class controls, the drift G5 warned about. Since build 7, recognition compares each run with its own shuffles, so the shift no longer moves decisions; only `recognised_pooled` would feel it.
- **Determinism, pending keys, `blind()`** [checked]. Unchanged in kind. Insert and remove are keyed by orientation-free run in both `Pending` and the tree.
- **Runtime** [measured]. 42–51 s per dry plan, the same as stochastic-4.

## What I didn't do

- I didn't patch or test fixes for P1–P3.
- I didn't rebuild the catalog or the view under another encoded rule. The 445 in P1 is a count over the current build's records, not a rebuild.
- P6's chance count assumes the failing runs are mostly null; a label-permutation null would be firmer.
- I didn't compare which runs the lookalike and names/order streams pick under the new weights, beyond counts.
- I didn't look in `spikes/` beyond what CATALOG cites.

## On the brief

The brief gave me exactly the facts I couldn't have found: what is live and what isn't, the seal, the shared processes, and that `plan()` in-process writes nothing. Two things would have helped: that the drains also hold `probe.py` in memory, and that `data/answers/` for a test round is rewritten by the loop's in-memory parser. I found both, but either could have misled a dry run built on the stored records: p003 reads as all unparsed there.
