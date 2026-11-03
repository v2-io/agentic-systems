**KR I.3 and I.4** (one open ledger keyed by claim; standing read from recorded checks, not typed) under the top intent *"Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself."* (Joseph, 2026-10-30).

# vsect and the flows of work through it, read from the record

*Claude Fable 5.1, 2026-11-02, at asf `2aa995e5`. Written for the lead (Claude Opus 5.5) planning the next phase, and for Joseph. Nothing outside this directory was changed. Every number here was computed from `.vsect/events/`, `items/`, `questions/`, `reviews/` and git by the scripts in `scripts/`; the few taken from someone else's account say so.*

## What this is

Joseph asked what the kinds in vsect are now, how things flow through them, which have parts out of sync or carry two different flows into one document, what signal-to-noise measures would be defensible, what questions are not being asked, what the flow for retiring cruft is, and whether vsect could output the whole thing as a state machine and what that would show. This directory answers those in order, from the trail rather than from the design documents, and then says what I would change.

## The short answer

1. The record is in better shape than the files around it. Every verdict vsect computes reproduces from the events, and the one-day sprint left a trail dense enough that the flows can be read off it directly (`01-flows.md`). The two places the tree and the record disagree are both commit seams, not state bugs: 189 imported items are closed in the record and open in their files because the lanes committed the event files and not the item files vsect wrote; and 17 of 18 `close --by-commit` citations name commits that no ref reaches any more.
2. The strongest signal-to-noise cut in the store is not between kinds but between who recorded a check and who wrote the text. Integrator-recorded re-derivations: 116 confirmed, 0 broken, 0 narrowed. Independent re-derivations: 88 confirmed, 22 broken, 43 narrowed. The dashboard blends the two, and 59% of its "confirmed" count is self-recorded (`02-measures.md`).
3. The feedback loop Joseph suspected is measurable and its gain was above one. At least 86% of findings were placed on text written during the sprint; independent checks kept finding something at a flat rate of roughly one in four across every round; and the most-checked segments grew by 1.5x to 2.5x over the rounds, never shrinking. Each round added more text than the next round could clear (`03-loops.md`).
4. `kind: item` is the fused kind the verisectorium model names as a pathology: a random sample of 45 shows at least six distinct repair profiles behind one word, and the ledger has closed 18 of 858 items as `done`. The cost of the fusion has not arrived yet because closing has barely begun; it arrives at `close`, where the kinds differ (`01-flows.md` §3, `06-recommendations.md` §3).
5. The flow for retiring cruft exists for items and findings and does not exist for sources. The design's influx crossing (`cross`, with integrated / rejected / needs-review / skipped) was not built, so 23 drain files invented it in prose, and 60% of the ledger's coverage of claims lives only there (`04-sunset.md`).
6. Yes, vsect should output the state machine, and it can: the trail already carries every transition. I built it in `scripts/fsm.py` and the result is in `01-flows.md`. What it shows is the stocks (467 noted items never touched again, 182 open findings, 336 lapsed checks) and the one cycle with gain above one (`06-recommendations.md` §7).

## Reading order

- `01-flows.md`: the kinds as declared and as used; the empirical state machine with counts; the sources, sinks and stocks; the documents that carry two flows; the out-of-sync list, each with its cause verified.
- `02-measures.md`: thirteen candidate signal-to-noise measures, each with today's value, what it tells, and a case where it misleads.
- `03-loops.md`: the reinforcement loop, measured four ways, with what would make the reading wrong.
- `04-sunset.md`: what the retirement flow is today, what it lacks, and the disposition state set a source record would need.
- `05-questions.md`: the questions the system is not asking.
- `06-recommendations.md`: what I would change, in order, each with its refuter; the verdicts on `kind: item`, on the state-machine output, and on the second-coordinator idea.
- `debrief.md`: the same for Joseph, in plain words.
- `scripts/`: `census.py`, `census2.py`, `census3.py`, `fsm.py`. Run from the asf root as `python3 -I scripts/<name>.py .`; `census3.py` also takes the path of a `vsect open --format json` dump.

## Method, and what I did not do

I read whole: the effort's README, INTENT, HANDOFF and `system-review/00-system.md`; the sprint retrospective (reflection 31) and the Fable tag-vs-now assessment; the vsect tool README; the design's `README`, `model`, `vsect`, `core`, `storage` and `open`; RC1's charter, `02`, `04`, `07`, `08` and `09`; the items-recheck pilot and the confirm pass account; the I.10 measurement; `drain/aisi-eoi-notability.md`; the spikes SOP §0–0b and the routing SOP §3–4. I read the vsect source where a verdict depended on it (`verbs.rs` for `recheck`, `close` and `mark_closed`; `state.rs` for holding, lapse and item state; `norm.rs`; `record.rs` for the hashed text). I ran every verb's read form and the scripts.

Not read: the other 22 drain files beyond their disposition vocabulary; the lane accounts under `c1-lanes/`; the influx scout's regional files; RC1 `01`, `03`, `06`, `10`, `11`; `session-aat.md`; `verisect-and-ldocs.md` beyond its headings; vivarium's instance of the pattern. `memorata-search` returned nothing for the queries I tried on Joseph's recent words about vsect, so his words here are the ones the lead relayed verbatim. I launched no agents.

The sprint ran for one day under one regime (parallel lanes, a lead merging). Every rate below is a frequency over that day, not a property of the tool; where I say "probability" I mean that.
