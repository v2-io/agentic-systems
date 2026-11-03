**KR I.3 / I.4.** Part of `README.md`'s set.

# Signal-to-noise measures that can be defended, with today's values

A measure is defensible here if it is computed from recorded acts, says what a reader may conclude from it, and has a known way of misleading. Each entry below gives all three. Values are at `2aa995e5`; the scripts in `scripts/` compute them.

| # | Measure | Today | What it tells |
|---|---|---|---|
| 1 | Independent-check yield: share of checks by a mind other than the author that broke or narrowed something | 114 / 266 = 43% | how much a bare-brief check is still finding |
| 2 | Self-check yield: the same for the author's own checks | 3 / 222 = 1.4% (0 of 116 `rederive`) | how little an author's own record says about defects |
| 3 | Blend: share of the dashboard's "confirmed" that is self-recorded | 219 / 371 = 59% | how much of the displayed evidence is the author's word |
| 4 | Lapse precision: `not-equivalent` among confirmed pairs | 3 / 77 = 4% (3 of about 120 bindings) | how many of the strict rule's alarms were true |
| 5 | Import precision: imported tracker lines that survived re-check | 174 / 371 = 47% | the trackers' truth rate; by file, from 80% (TODO) to near 0 (index rows) |
| 6 | Re-find rate: a drain's find already in the ledger | 377 / (377 + 428) = 47% | how much of a drain is duplication |
| 7 | Closure yield: items closed `done` over items opened | 18 / 858 = 2% | throughput; two days old |
| 8 | Finding closure: findings answered over placed | 131 / 313 = 42% | the same for findings |
| 9 | Keyedness: open items naming at least one record | 551 / 661 = 83% | I.3's "keyed by claim" |
| 10 | Owner coverage: open items naming a KR | 546 / 631 = 87% | I.1's "every item has a KR" |
| 11 | Ledger inflation: `vsect open` rows over distinct things | 1,926 / 1,213 = 1.6 | what the first screen overstates |
| 12 | Sprint self-reference: findings placed on text written in the sprint | at least 269 / 313 = 86% | how much the loop fed itself (`03-loops.md`) |
| 13 | Tree-record disagreement: files whose frontmatter contradicts the trail | 189 items; 17 dead commit citations | what `vsect check` is not checking |

A fourteenth that I would print beside these: correction rate, 135 `correct` events over 2,259 (6%). It is not noise; it is actors fixing their own `--why` text under time pressure, and it is the cheapest available estimate of how carefully the why-fields were written.

## How each misleads

1. **Independent yield.** It counts a checker briefed to find; a flat 43% can mean the text keeps having defects or that adversarial checkers always find something. The confirm pass gives the control: of its 36 judgments, 3 were real, so a second mind asked to *compare* rather than to *find* produces near zero. Read the yield together with edit mass (`03-loops.md`); a high yield on shrinking edits is convergence, on growing edits it is the loop.
2. **Self-check yield.** The 3 that broke were `run` and `read-check`, not `rederive`: an author re-running a simulation can catch a wrong number, and the F72 integrator's exact simulation is evidence. The honest statement is narrower: an author's own re-derivation of the author's own derivation has, in this record, never found anything. Keep self-recorded runs as reproducibility on their own rung; stop counting self-recorded re-derivations as evidence on the derivation line.
3. **Blend.** It is a property of the display, not the store; the events carry the actor. The fix is a column.
4. **Lapse precision.** Low precision is the strict basis rule doing what it says, and the three true positives (the `def-auxilia-hierarchy` argument that changed under C1; the `(h′)` counterexample replaced) were exactly the ones a weaker rule would have missed. 13 of the 36 pairs were pure Claim Record insertions, a grain artifact; without them precision is 3 of 23. The measure argues for scoping (`--read`) and for grain, not for a looser rule.
5. **Import precision.** `holds` counts a real item with a wrong frame as signal; the pilot found six of sixteen `holds` misframed ("promote" where the work is "author"; "contradicts" where it should be "bounds"), which is why `--restate` exists. And `not-an-item` was mostly the importer's unit, not the trackers' judgment (BIBLIOGRAPHY's how-to sections; PRACTICA's navigation checkboxes), so the number measures the import as much as the trackers.
6. **Re-find rate.** A raise can be a wrong match, and a drain that did not look raises nothing. Half of the drains' finds being already present is also what "point every lane at the influx rows first" predicts, so a high rate here is partly the ledger working.
7. **Closure yield.** Meaningless at two days except as a baseline; it becomes the measure when the next phase starts closing. If it stays near 2% after a landing wave, the items are not shaped to close (`06-recommendations.md` §3).
8. **Finding closure.** Only one exit exists (answered by revision, confirmed by a second mind); with `dispose-finding` unused, a wrong finding cannot leave, so 42% understates how many findings were dealt with.
9. **Keyedness.** An item that concerns a segment is findable by slug; an item that concerns "(the store)" may be right to (a build task is not about a claim). Report the unkeyed count beside what kind of item it is; today the kind is not recorded, so this measure cannot be split.
10. **Owner coverage.** A KR id in the owner field says a key result owns it, not that anyone will do it; INTENT's table has one agent. It measures placement in the tree, which is I.1's job and nothing more.
11. **Inflation.** Repeating an item under each record it concerns is a defensible display for "what is open about X"; the defect is the header and the mixing of kinds, not the repetition.
12. **Sprint self-reference.** A version counts as sprint-written if any part of the segment changed, so a finding about a sentence that existed at the tag is counted if a Claim Record was inserted above it. The retrospective's sentence-level figure (about half of ten corrected sites) and this version-level floor are different quantities. In the other direction the figure is a floor: in 4 of 8 segments I spot-checked, the earliest version vsect ever saw already differed from the tag, so some "pre-sprint" checks were on sprint text too.
13. **Tree-record disagreement.** Zero would mean the files agree with the trail, not that the trail is right.

## Which three I would put on the dashboard

Independent-check yield (1), self-recorded share (3) and edit mass per round (`03-loops.md`). Together they say whether the loop is converging and whether the evidence shown is anyone's but the author's. The rest belong in `vsect check --strict` (13), in `vsect open`'s header (11), or in a cycle-close report (5–8).
