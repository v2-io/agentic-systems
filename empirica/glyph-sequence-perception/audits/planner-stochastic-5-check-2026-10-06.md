# Check: planner stochastic-5's fixes against its audit

*2026-10-06, about 21:20–21:45. Claude Opus 5.5, the author of `planner-stochastic-5-2026-10-06.md`. Not de novo: I checked commit `df46b365` against my own findings, and against the coordinator's account of what it did with each one. Written for the coordinator before the loop and drains restart, and for Joseph.*

*What I read and ran.* I read the code diff of `df46b365` (`catalog/code_order.py`, `catalog/given_walk.py`, `priority/plan.py`, `probe/probe.py`, `report/view.py`, `catalog/build.py`), the seal's new addendum, and the changed lines of `METHODOLOGY.md` and `CATALOG.md`. I then ran four things, all from the shared scratchpad (`…/scratchpad/s5audit/`):

- **Dry plans.** Three planners in-process, on the same answers (341,397 records, read at about 21:25) and the same three dummy round ids as before: the committed planner, stochastic-5 as audited (`e3fdfa1c`), and stochastic-4 (`c5ecf912`). Each was extracted whole with `data/` linked, and each read p003 as the current parser records it.
- **Probes of `code_order` and `given_walk`.** Hand-picked runs, a search of every numeric code point for the new branch's failure case, and a simulation of the new rules' chance rates.
- **The p003 ledgers,** re-parsed for the `fill` marker.
- **Catalog queries.** The current build, `b20261006_210904`, whose `code_order.py` hash matches the file on disk.

*The seal.* As before, I read no `choose` or `names` answers. The dry plans read them in-process through `blind()`.

*Files.* I wrote only this check. Bytecode writing was off.

Labels: **[measured]**, **[checked]** against the code, **[reasoned]**.

## The short answer

**I see nothing that should hold the restart.** P1, P2, P3, P5, P7, P8 and P10 do what the audit asked, and P6 is handled as the coordinator described. Together with P4's step (loop and drains restarted together), it is ready.

**One ruling for Joseph comes with P9.** Giving every given relation the factor reverses G1 in the planner. It turns away questions about dress order at equal value, which is Joseph's own `①` vs `⑴` vs `❶` vs `🯱` question (C3). I suggested making the view and the planner agree; I didn't foresee this consequence, and it's his to confirm.

**Four smaller things, none blocking:**

- the new "rotated" rule is looser than its comment says (C1);
- `seq_rel` on the lower bound sits mostly at its floor (C2);
- explore still uses the old given test (C4);
- a few documents and labels still lag (C5).

## Each finding against the fix

| finding | fix | check |
|---|---|---|
| P1 encoded included cross-block orders | encoded = consecutive code points (any blocks), or monotone / rotated / interleaved within one block | **resolved** [measured]. Every cross-block example in the audit is now "none". So are Joseph's p003 runs and their insertions, and `∣∥⫴`. `-=>` (one block) is still encoded, as the coordinator says. In the dry plans, questions serving cross-block runs that the old rule flagged went from 30 to 205 over three rounds (148 under stochastic-4); questions serving runs that are encoded under the new rule, from 743 under stochastic-4 to 239. The view's perceived orders are 445 |
| P2 the exemption was too narrow | `choose` and `names` exempt (`encoded=False`) | **resolved** [measured]. `choose` questions at runs that are encoded under the new rule: 71 under stochastic-4, 15 as audited, 69 now. The view-side exception wasn't added, so a run that D shows is perceived stays off the perceived list. That is a choice the coordinator stated |
| P3 insert / remove capped at 8 | `(3, MAX_RUN)` in `Plan.add` | **resolved** [measured]. 34 of 136 insert and remove questions in the dry rounds are 9–24 glyphs |
| P4 old code in memory | loop and drains to restart together; p003 re-recorded | **to do at the restart**. The loop's record step will re-parse p003 then |
| P5 `seq_rel` scale | 90% lower bound; unmeasured runs at `scurve(0)` | **resolved as asked**, but see C2 |
| P6 chance passes | the view states the expected count (about 100 of 445) | **as described** [checked]. The arithmetic is right (1,854 tested, 1,409 failed, null rate 0.066), and the rate is labelled as a simulation |
| P7 insertions fill code-point gaps | inside insertions carry `fill` | **resolved** [measured]. p003: the three `▉▊▋` are `chart-gap`, the three `≈` `within-span`, Opus's `.` `outside`. Descending gaps work too. `fill` is also set on removals, where it means whether the removed glyphs lay within their neighbours' span. That is harmless, but worth a word wherever `removed` is described |
| P8 seal | insert / remove off runs holding canary glyphs; the p003 exposure recorded; Joseph to rule | **resolved for the planner** [measured]: 0 canary-touching insert / remove questions in the dry rounds (12 as audited). The runs the p003 insertions proposed (`┉┈┄─━▬█▉▊▋▌▍`) still enter the cohere stream as candidates. Cohere isn't sealed, but whether answers derived from that exposure should feed questions belongs in the same ruling |
| P9 "given" differed between view and planner | any given relation takes the given factor; number lines in mixed dress became a relation | **consistent now**, with C3 for Joseph. Questions serving a relation that isn't a given walk: 79 under stochastic-4, 16 now [measured] |
| P10 documents, provenance | METHODOLOGY §4 / §5, CATALOG §11 / §13 and build notes; hashes | **mostly resolved**, see C5 [checked]. The manifest hashes `code_order.py`, `best.py` and `probe.py`; `plan.json` hashes `code_order.py` |

**Sizes** [measured]: 1176 / 955 / 1194 questions in the three dry rounds, against 1177 / 889 / 1170 under stochastic-4. The difference is insert, remove and explore's re-drawn size, as before. Runtime is 41–49 s.

**The new number-line branch in `given_walk`** can't fail on current data [measured]. It calls `min()` over the run's number givens, which would raise if every glyph with a numeric value sat only in alphabet givens. A search of every code point found none. If `givens.json` is regenerated, that's worth remembering.

## C1. The new "rotated" is looser than its comment

**The rule** [checked]. "Rotated" now accepts two monotone pieces joined at the run's extreme code points. Its comment still gives the chance rate of an exact rotation, $2n/n!$. But the rule doesn't require the pieces' ranges to be separate, so `3 9 | 1 5 7` passes, and that isn't a rotation of anything.

**Its chance rate** [measured, 20,000 random orders of one-block glyphs that are never consecutive]:

| glyphs | "rotated" | an exact rotation |
|---|---|---|
| 5 | 0.134 | 0.067 |
| 6 | 0.044 | 0.014 |

All encoded labels together come to 0.15 at 5 glyphs and 0.10 at 6.

**In the catalog** [measured]: only 19 records are "rotated" by the new rule and not by an exact rotation, and none of them is recognised and outside a given. So the effect today is small.

**The fix**, unless the looser rule was meant: require all of one piece to lie beyond all of the other (`max(y) < min(x)` when rising), which is exactly a rotation. The same applies to the halves of an interleave.

## C2. `seq_rel` on the lower bound mostly sits at the curve's floor

**The distribution** [measured, 4,219 runs asked whole]. The S-curve is centred at 0.5 with width 0.12. Lower bounds of the paired difference rarely reach 0.4. So:

- 47% of measured runs sit at the floor, 0.065;
- recognised runs range 0.07–0.28 (deciles), against 0.065 for runs that aren't.

The preference for runs recognised as sequences is now a factor of about 1–4. Before the fix it was about 10. Nothing is wrong in kind: the weight is soft, and the curve's numbers were chosen without evidence.

**What I'd suggest** [reasoned]. If the intent is that a run clearly recognised as a sequence draws several times more insert, remove and lookalike questions than one that isn't, centre the curve near the lower bounds that occur (about 0.2), or use ranks.

## C3. P9 turns away Joseph's dress-order question

**What changed** [checked, measured]. With any given relation taking the factor, dress runs and dress sets weigh 0.1 again: `①⑴❶🯱`, `1¹①𝟏`, `2➋3➌4➍`, the accent forms `óôõ`, and the number lines `0ⅠⅡⅢ` and `1𝟐3𝟒𝟓`.

**Why that matters.** The stochastic-4 audit's G1 exempted them, partly because `data/seeds/digit-dresses.jsonl` holds Joseph's question, *"are the digit families ordered relative to one another, e.g. ① vs ⑴ vs ❶ vs 🯱 at equal value?"*. The set and order questions that would answer it are now at 0.1.

**Two readings.**

- Joseph's *"all the different encodings of essentially the same alphabet and digits ... a whole world that we can just call 'given'"* supports the change.
- His own question supports an exception for dress *order*.

`HANDOFF.md` records that he hasn't confirmed G1 either way, so this is one ruling.

## C4. Explore still uses the old given test

`explore()` keeps a pair along a given with probability `GIVEN_RELEVANCE` only when it is a given *walk* (`GW.is_given`). Everywhere else in the planner any relation now counts [checked]. Pairs only relate as windows (`①⑴` has no relation), so the difference is small. It is one line to make the two agree.

## C5. What still lags

- **CATALOG's header** still says builds 0–5.
- **CATALOG §11's first rule** still reads *"Only recognised runs appear: R, O or L beyond its contrast with certainty. Given walks don't"*. The italic note added below it says otherwise: recognised as a sequence, and any given relation.
- **The model label.** The catalog's model is still `catalog-v5-build7`, though `code_order` and `given_walk` changed the view's groups under it (perceived orders 336 → 445). The code hashes in the manifest tell the builds apart, but a reader going by the model label can't. Calling it build 8 would.

## What I didn't do

- I didn't patch or test the C1 or C4 fixes.
- I didn't recompute P6's null rate under the new grouping. The rate depends on answer counts, not on the encoded rule, so the 0.066 should carry over.
- I didn't read the rest of the METHODOLOGY and CATALOG diffs beyond the lines named above.
