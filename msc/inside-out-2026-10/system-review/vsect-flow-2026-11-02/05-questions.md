**KR I.3 / I.4.** Part of `README.md`'s set.

# Questions the system is not asking

Each is a question the record could answer and no surface asks. The first four are where I would start; the rest are smaller or wait on the first four.

1. **Who recorded this check, relative to who wrote the text?** The actor is on every event as a typed name (74 distinct forms; 5 of 2,259 events carry a session); the author is on every `revise`; nothing compares them. The harness session id is available in every agent's shell and is the parent's for a subagent, so session-grain identity can be inferred today and subagent-grain cannot (`06-recommendations.md` §4a). The design's independence predicate (`core.md` §5.6) is unbuilt, and the dashboard prints self-recorded and independent evidence as one number. This is the question whose answer changes the most (`02-measures.md` §1–3).

2. **What did this check actually read?** `--read` exists; 56 of the 193 checks on one lapsed pair declared a read set, the rest default to the whole transitive basis. Every undeclared read set makes a future confirmer compare text the check never looked at. The confirm pass measured the cost: 117 of 120 comparisons were "this check reads nothing of that".

3. **What kind of work is this item, and what act closes it?** `kind: item` answers neither. A sample of 45 held items contains defects in a claim (a finding wearing an item's clothes), segments to author, derivations to attempt, citations to land, terminology entries, measurement protocols, tool and build tasks, process changes, and judgments that are not work at all ("commit X exists only on a branch nobody merged"). The verisectorium model individuates a kind by how it fails and what repairs it; by that test these are at least six kinds, and `close` is where the difference bites: a defect closes by a revision plus a check, an authoring task by a new record, a derivation by a review, a measurement by a run, a tool task by a commit elsewhere.

4. **What has been read for integration, and what has not?** No record kind holds it (`04-sunset.md`). The canary question ("was vivarium's `LEXICON.udon` read?") had to be answered by grep over drain prose, and was answered no, after the fact.

5. **Which open thing does a pending decision wait on?** `vsect open` is oldest-first over 1,926 rows; `next` is unbuilt. RC1 07 states the ordering principle (a gap's priority is the influence its closing exerts, priced by the decisions waiting on it) and the edge graph exists to compute a first approximation (how many records rest on the concerned one). Nothing ranks.

6. **Does the tree agree with the record?** Not asked by `vsect check` for `closed:`, `rechecked:`, `owner:`, or for the commit a `close` cites. 189 and 17 disagreements today.

7. **What did we decide, on what grounds, and what would reopen it?** Zero decision records, twelve process corrections in prose. The next lead inherits them as a reading, not as records with reopen conditions.

8. **How much did this round add, and how much did it settle?** Edit mass per revise is one diff away and nobody sees it before launching the next check (`03-loops.md`).

9. **Where did the answer to this question go?** 12 questions answered; whether the answer reached a segment body or only the `answer` event is not recorded. A question whose answer changed no record is a Working Note in another form.

10. **When does a check stop counting because of time, not text?** No eras, no clocks. Simulation checks carry no code version; a `run` recorded against `empirica/` code that later changes will hold forever.

11. **What is this costing per true correction?** 2,259 events, 510 commits, 54,000 lines of effort tree for eight canon corrections the Fable assessment could verify plus a backlog landed. No surface puts cost beside result, so "three to five times the necessary cost" (reflection 31) is a judgment, not a number the next sprint can beat.

12. **Is the thing "awaiting a second mind" worth a second mind?** 223 pairs wait; a confirmer at a root is asked whether a rewording is equivalent for every downstream use. The 4% hit rate says most are not worth a mind, and the three that were are the ones that matter. The question that separates them, "does any waiting check's criterion read the changed sentence?", is partly computable from the criterion text and the diff, and is not computed.

13. **Did the kinds earn their place?** RC1 10's founding questions (standing, speech-act, failure, instrument, dimensions, movers, ceiling, grain, certification) were never run on `item`, `question` or `review`. The ledger was founded in a day as the drains' landing zone; that was the right call for the day and the questions are still owed.
