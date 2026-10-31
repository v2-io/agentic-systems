# I.10 baseline: tag `pre-integration-2026-10-30` against `5eee086c`

*KR **I.10** of `../INTENT.md`: "Signal rises against noise, measured." Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." (Joseph, 2026-10-30). Measured by Claude Opus 5.5 on 2026-10-30 (MDT). The method, and what every term below means, is in `METHOD.md`. The numbers come from `data/sample-2026-10-30-*.tsv` and `data/census-2026-10-30-claims.tsv` and are reproduced by the commands in METHOD's *Rerun*.*

## What it found

The drains made what is written about a claim more *findable*. They did not make it smaller, and most of the gain is held in files due for deletion.

1. **Places grew; places named nowhere halved.** Across all 244 claims, live places outside body and ledger rose from 13,954 to 17,514 (+26%). The places nothing points to fell from 12,396 (89% of places) to 6,094 (35%). Before the drains, a cold agent finding a spike or an audit that mentioned a claim had no record saying what it was to the claim. Now about two places in three are named by a ledger record or a drain account.
2. **Most of that coverage is in the drain accounts, not the ledger.** 4,572 places (26%) are named by a ledger record about the claim; 6,828 more (39%) only by a file in `drain/`. The drains put owed work in the ledger, but kept *canon*, *superseded* and *set aside*, and the walk record of every audit and spike, only in their own accounts. I.8 says those accounts delete when their items are in canon or the ledger. If they go as they stand, the D column becomes U, and the durable gain is the strict column below:

   | 244 claims, words | tag | HEAD, strict (ledger only) | HEAD, with drain accounts |
   |---|---|---|---|
   | must-read noise, block unit | 2,710,580 | 2,358,768 (−13%) | 1,177,008 (−57%) |
   | must-read noise, section unit | 11,634,282 | 11,883,574 (+2%) | 6,190,580 (−47%) |
   | total reading (signal + must-read), block | 3,189,327 | 3,404,408 (+7%) | 2,222,648 (−30%) |
   | total reading, section | 12,113,029 | 13,101,758 (+8%) | 7,408,764 (−39%) |
   | signal share, block | 0.15 | 0.31 | 0.47 |
   | signal share, section | 0.04 | 0.09 | 0.16 |

   On the strict reading, a cold agent that does full diligence reads more today than at the tag. On the with-drain reading, it reads about a third less, but only while `drain/` exists and only if it knows to look there.
3. **Nothing was retired, so noise fell only by being labelled.** Audits mentioning sampled claims: 756 → 756. Influx: constant by construction. Other segments' Working Notes: 214 → 219. Own Working Notes, census-wide: 176,130 → 176,676 words. The only places removed are the trackers and proposal files the ledger absorbed (I.3: `PROPOSED*.md`, `ROUTING.md`, the root `*-TODO.md` files). The drains disposed each source item but retired no audit, spike, influx file or Working Note, so a grep still lands on every one. Two levers would cut the noise itself: I.5's Working-Notes cleanup, and moving fully disposed sources (spikes, whole audit dirs) into `.integrated/` or `.archived/`, the location-as-label convention agents already honor.
4. **The effort's own writing is most of the new noise.** Of the net +3,560 places, 3,355 (94%) are files under `msc/inside-out-2026-10/`. The rest is the effort's own spikes. In the pooled sample, `spikes/` gained 93 places and lost 13: every new one is in a 2026-10-30 spike or check (`epistemic-target-ontology/` 05–17, the loop-identification, allocation-vs-distortion and exit-time spikes), and every lost one is a folded tracker. Of the 690 effort-residue places in the pooled sample, 380 are named by nothing:
   - 188 are drain accounts, which cannot account for themselves;
   - the other 192 are lane accounts (`c1-lanes/` 101), `internal-surfaces/` (36), `owner-review/explorers/` (21), `items-recheck/` (16) and the rest of `owner-review/`.

   These are what I.8 has to dispose of.
5. **Signal grew too, but partly by getting longer.** Bodies grew 13% (478,747 → 539,268 words, census) as the C.1 integrations landed. The ledger added about 506k words of record mentions. Signal share therefore rises even where a reader's total load does not, which is why the total-reading rows above are the better headline. Of 2,703 ledger records that mention a claim, 1,441 (53%) are keyed to it. The other half are invisible to `vsect open segment:<slug>` and visible only to grep. 13 of 244 claims have no keyed record at all.

**The fixed sample agrees with the census.** On the 30 random claims, signal share in block units is 0.16 at the tag and 0.30 (strict) or 0.46 (with drain) at HEAD; places named nowhere go from 1,388 to 716. The 16 purposive claims (MAP §3's targets) start noisier (median 64 places against 34) and move the same way. Full tables: `python3 -I summarize.py data/sample-2026-10-30`.

## What the measure gets wrong

The brief asked to hear this as much as the number. In order of how much I think it matters:

1. **"Named" is not "disposed".** L and D record that some text names the place, at the granularity the records cite: a path, a directory, or an audit's six-digit id. A spot check of eight marks found them working as defined but showed the gap. One was a drain account section heading that names `AUDIT-WORKING-628417/` as walked, while the place was a file in it about `#def-model-sufficiency`. The heading says the audit was read, not what it says about that claim. Before the fix recorded in METHOD, drain files also counted as accounting for one another. So both coverage columns are upper bounds on how many places a reader can safely skip. A truer measure would key each disposition to (source location, claim). That record does not exist anywhere today, which is itself the finding in 2.
2. **The reading units are uncalibrated.** Block and section differ by a factor of four to six, and the true cost of deciding "does this supersede, or is it superseded?" is somewhere between, probably nearer section for spikes, where the conclusion sits at the end, and nearer block for drain tables. The way to calibrate is to give cold agents a claim at each snapshot, log what they open and how long they take, and compare. That was the plan before Joseph asked for no more agents in this session. It is the first thing left (below). Until then, I report only conclusions that hold in both units: coverage up; strict must-read about flat; noise volume up; the gain lives in `drain/`.
3. **Slug grep cannot see paraphrase.** The influx scouts found that the papers which developed canon's math carry single-digit slug hits. So the influx's 1,120 places are a floor, and its 58% unaccounted share probably understates the true residue. The same blindness hides restatements without a slug (A.2's and D.3's territory). Wherever restated material carries no slug, this measure under-counts noise.
4. **Words are not truth.** A body that grew because it now states its premises honestly scores as "more signal". A ledger record that is wrong scores the same as one that is right. The measure tracks findability and reading load, not correctness. Correctness is C's and I.4's.
5. **The influx is today's disk at both ends.** That is fair for the comparison, because the drains did not edit other repos, but the "tag" influx includes files written after the tag. Influx numbers move only through accounting.
6. **The class line is a judgment.** Front surfaces, other segments' bodies, the history layer and anything under `.integrated/`/`.archived/` are reported but not counted as noise. Counting front and other-body would put A.2's restatement problem into this number. The columns are in the data for whoever wants that view.

## Proposals for the tree (bottom-up)

- **For I.8, a precondition.** Before `drain/` deletes, each per-source disposition must move to where a reader of that source or that claim meets it: a `vsect raise` onto the claim's item; the source moved to `.integrated/`/`.archived/`; or, for set-aside Working-Note items, their deletion under I.5. Otherwise this measure's with-drain gain reverts to the strict column. The test: re-run, and the strict and with-drain columns converge without the U count rising.
- **For I.10 itself.** "After each drain wave" no longer applies, since the drains finished before the baseline. Re-measure after I.5, after I.8, and after any `.integrated/` move of audits or spikes, and track the strict total-reading row as the headline, beside U.

## What is left

- **Calibration.** Run cold-agent reads on two or three sample claims at the tag (a `git worktree add` of it) and at HEAD, and compare what they open and decide with the block and section estimates. This was not run because no agents were allowed this session.
- **Concept-level influx coverage** for a few purposive claims, which would bound how far point 3 under-counts.
- **A per-claim disposition key.** If I.3 or I.8 adopts one, change `measure.py`'s L test to use it in place of path-naming, and re-measure the tag in the same run.
- **Privacy, for whoever pushes.** `data/sample-2026-10-30-places.tsv` lists file paths in private repos (`agent-core`, `neurips-reviews-responses`, `aisi-eoi`, `notability-extracts` and others), with counts only and no content. asf's remote is public. Drop the file before pushing if the paths themselves are sensitive; it regenerates.
