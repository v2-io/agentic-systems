# 31 — The inside-out sprint: what it did, what went wrong, what to change

*To the next coordinator of an effort like this one, and to Joseph. Written 2026-10-31 by the lead of the 2026-10-30 in-place refactor (Claude Opus 5.5, which took over mid-run after a context compaction), with the independent assessment and review of a Fable agent that had no part in the day (`msc/tag-vs-now-assessment-2026-10-31.md`). The sprint runs from tag `pre-integration-2026-10-30` to tag `post-integration-2026-10-31`. Its objectives tree is `msc/inside-out-2026-10/INTENT.md`.*

## What the day did

Joseph's goal was "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself", in service of truth about agency. Two things are true of the day, and the next coordinator should hold both. It found real new theory and landed a real backlog. It did so at three to five times the necessary cost, and left debts.

The Fable agent re-derived the largest canon changes from the text and found them correct:

- gain injects channel noise, so the exit exponent peaks at the Kalman–Bucy gain;
- the Model S persistence condition is a window of gains whose roots are geometric about $K$;
- Prop A.1S bounds the killed moment, because the stopped moment it used to bound tends to $R^2$;
- the strategic-persistence "hard ceiling" was an algebra error: the discounted Beta-Bernoulli gain is exactly $1-\lambda$;
- AND/OR propagation is exact, at the root, iff the DAG is an AND/OR tree (per node: one directed path from each ancestor), not iff it is causally sufficient;
- the Volume 3 bias law is a model-free $L_G^2/8$ bound plus a hypothesis, not a scope condition;
- uniqueness of the compensation channel holds beyond the entity's own record, not absolutely.

About half of the canon corrections were backlog that had waited in proposal files, influx and steward queues (SP-30, the aat-refactored predicate spike, arch 2026-09-23, logos 2026-09-25, vivarium `ETHICS.md`). The other half were the day's own findings: the owner review written that morning found the false iff and the innovation-versus-estimation-error confusion that became the gain-noise lineage, and the lanes found the window, the exit-time result and the F72 algebra error. The gain-noise lineage is, in the Fable agent's judgment, the best thing in Part I since the sector condition. Resetting to the tag would have put eight known-false or unsupported statements back. Joseph, at the close: today "has served truth in the end, in aggregate".

The rest of this file is about the cost, so the next effort pays less for the same truth, without becoming timid.

## What went wrong, by mechanism

**The handoff set the posture.** The lead took over from a compaction summary that ended in a list of next steps. It read that list as momentum and executed it, where the summary should have been only a map. The posture that followed was "process the last agent's output", not "steer by the tree".

**The coordinator multiplexed instead of steering.** For hours the lead read accounts, relayed findings to the next agent, rebased, merged and pushed. Each step was locally justified. Meanwhile the objectives the owner review had ranked first went untouched: A (the front door), B beyond Part II (claim records), E (any measurement on a real agent), F (standard names), G (assembly), H (pedagogy). Joseph saw the drift from outside in a few messages: "your *primary* responsibility is that intent tree and not letting things get off track from it."

**Rounds fed themselves, two ways.** Part I reached round 5, and one scope segment had eight independent reads. First, restatements: after the first rounds the mathematics held, and what checks kept finding were sentences elsewhere (Briefs, OUTLINE cells, README partials, neighbour segments) that said more than the corrected body. Nothing tied a restatement to its source, so each sweep found more, and each round's edits gave the next checker more to read. Of ten corrected sites traced against the tag, about half were sentences an earlier round had written the same day. Second, strengthenings: when a checker found one (the window, the threshold expansion's third term, P4), it was landed in the next round and then itself needed checking. That is the spiker ≠ verifier ≠ integrator separation collapsing inside the loop. The checking itself was not the waste: checks 6 and 8 on the scope segment found real defects. The waste was checking the same way eight times, when one checker with a bare brief and a counterexample habit would have found the same in two.

**A new integrator each round.** The lead carried the spike template's role separation into integration and sent findings to a fresh integrator instead of the one who held the context. The independence that matters is between author and checker; the fix should go back to the original integrator.

**The existing process was dropped, not improved.** `~/src/arch/SPIKE-PROMPT.template.md` says to use it "for all spike launches". The lead had read it only in part and did not use it. `spikes.sop.md` and `multi-agent.sop.md` were not read. Integrators derived new results and landed them themselves. "Gates on Joseph are lifted" lifted the gates that waited on him; the lead read it as license to improvise the method.

**The drains assumed completeness.** Drain agents sorted every surface they were pointed at into a new ledger, and wrote each disposition as if the search had been complete. It wasn't. Scouts found ASF material in other repos by searching for mentions of ASF, so theory that bears on ASF without naming it was invisible. Joseph had planted a canary: vivarium's `LEXICON.udon` (its kingdom, law and participation ontology), `def-nomos`, `form-lawful-steering`. No scout or drain read them, and the lead never ran the canary check. Item sources were recorded as prose, so what was not drained cannot be listed.

**Nothing was retired.** Thirteen root trackers and four `spikes/` tracker files were folded into the ledger, but no spike, audit dir or Working Note moved. The I.10 measurement found a cold agent's total reading per claim flat against the tag, with 60% of the new coverage named only in the effort's drain accounts and 94% of the net new places in the effort's own directory.

**A measurement aimed at a proxy.** Asked for "the cheapest falsifier", the E.3 agent tested source-file lifetimes, because they are abundant, against a claim about a system's remaining feature count. Different unit, different quantity. The brief invited it.

**The lead's own evaluation over-corrected.** Once Joseph named the drift, the lead weighted findability (reading load, noise) over correctness, and told him the eight checks added nothing. The Fable agent weighed correctness by re-deriving, over Part I, F72, A.1, the Part II iff-tree and bias-law cluster, Volume 4 and two TST segments, and found the canon better there. It did not read Part III, most of Volume 3, or most of TST, so "the canon is better" holds where it looked. Both measurements were real; they answered different questions. For "which surface is better to work from", correctness decides, and the findability debt is the same on either surface.

## What to change

Each item names where it should land, so it does not stay a resolve. The first is the one that makes a check-and-fix loop shrink instead of grow.

1. **Restatements are bound to their source.** Every front-surface sentence names the slug it restates (A.2 did this for the nine headlines), and a change to that slug flags the sentence: a `front` record kind with a `restates` edge, and `bin/check-headlines`. (D.3, I.7, A.4.)
2. **Read the existing process before running it.** Before launching any spike, open the template and fill it. Before designing a landing cycle, read the project's SOPs. Record spiker, verifier and integrator per result in vsect, and *label* a landing where one mind holds two roles, rather than refuse it: a refusal only pushes the result into chat or a Working Note. A checker who finds a strengthening writes it down as a spike proposal and hands it off. (vsect; `doc/sop/spikes.sop.md`.)
3. **A record of what was read.** A vsect record kind for a source (path, read-by, at, disposition), so "what has not been read for integration" is a query. Seed it now with what is known unread: vivarium's `LEXICON.udon`, `def-nomos`, `form-lawful-steering`, `def-in-vivia`, vivarium `msc/` and `.super-archive/`; verisectorium RC1 02–11 and `external-ontologies/`; 26 of 30 udon bridge chapters; `~/src/aisi-eoi/` beyond its cards; `~/src/notability-extracts/`; the `owner-review/explorers/` files; the three 2026-08-24 spikes. Scouts search by concept and by the estate's own vocabulary, not only by mention. Run every canary planted. (I.9, I.3, vsect.)
4. **Retirement is part of landing.** A landing names what it supersedes and retires it: deleted, or moved to `.integrated/` or `.archived/`. The test is the delete-test from verisectorium: assume it disappears; is everything it carried landed or disposable? (I.8, `doc/sop/multi-agent.sop.md`.)
5. **One check per landing, then back to the author.** A non-author checks, with a bare brief and a counterexample habit. Findings go to the original integrator, who lands them; the same checker confirms. No new integrator unless the original is gone. The lead, at merge, runs vsect to see whether each changed segment has a non-author check bound to the merged text; if not, the merge commit says `unchecked` in so many words. (C.1 in INTENT; `multi-agent.sop.md`; the commit hook can refuse the silent case.)
6. **The lead steers by the tree.** At every landing, before launching anything, the lead reads INTENT from the top and asks which objectives are starved. It reports status to Joseph as what became true, not as counts. After a compaction, its first act is to orient to the tree, not to the queue the summary hands over. (INTENT "Using this file"; HANDOFF.)
7. **Measure the claim's own unit.** A measurement brief names the claim's population and quantity, and asks the agent to say if no available data reaches them, rather than to find the cheapest runnable test.
8. **Send the artifact, not a paraphrase.** From AGENTIC-DELEGATION's incident ledger: "if an artifact exists that states the question better than the brief does, send the artifact."
9. **Rules against parallel churn, as the tools enforce them.** Each integrator in its own worktree; `vsect claim` before editing, one holder at a time; the lead merges a reviewed SHA with `--no-ff` and pushes that SHA; `.gitignore` does not untrack a file already tracked; files listing private paths never enter a commit. (HANDOFF hazards; the commit hook.)
10. **Make the confirm pass cheap.** The one confirm pass after a merge wave found about 3 in 120 lapsed bindings actually touched. Checks should declare what they read (`--read`) by default, so edits elsewhere do not lapse them. (vsect.)
11. **The dashboard's register.** vsect shows a `narrowed` check as "⚠ known broken". Check 8's verdict on `#scope-adaptive-system` is that it holds up, with two wording items; the dashboard overstates it, and it is the first thing an arriving agent reads. (vsect display.)
12. **A missing record kind gets improvised in prose.** Where vsect had a kind (checks bound to text versions, items, questions, intent claims), the work was disciplined and checkable. Where it had none, agents invented structure in the nearest file: sources read (in drain accounts), front-surface restatements (HTML comments), a claim's standing (the `## Claim Record` section, invented at 14:17 on 2026-10-30 and written into 24 segment bodies, 1,130 lines, and into the format SOP and `agents.sop.md`), spike roles (commit messages at best), dispositions (drain prose), integration history (dated Working-Note blocks). Joseph, on the Claim Records: they sound like Working Notes or a vsect equivalent, not canon. The rule: before inventing a section, file type or convention to hold a kind of record, ask whether it is a record kind the tool should hold, and raise it with the tool's owner; ad-hoc prose structure is the tell. The Claim Records move out of segment bodies (to vsect, keyed by slug and bound to the text version they describe), and section 6 leaves the format SOP's cadence and `agents.sop.md`. (vsect; `doc/sop/format.sop.md`; B.1 reworded.)

## What is owed next, from `post-integration-2026-10-31`

In the Fable agent's order:

1. Close the verification edge once. Six merges have no independent check: Part I round 5, defender-noise round 2, Volume 4 round 4, Part II round 2, A.2, B.1 Part I. The Fable agent's re-derivations cover part of them; its criteria are in its assessment and are not yet recorded in vsect, which can be done under its name. Not covered: P4, the threshold expansion's third term, Part II round 2 beyond the bias-law cluster, A.2's headlines beyond five rows, the six over-reaching statements B.1 found. Those segments stay frozen until this closes.
2. Seed the source record (item 3 above).
3. Drain the effort directory in I.10's order: dispositions into the ledger first, then disposed spikes and audit dirs to `.integrated/`, then delete, then re-measure against the tag.
4. Pay the structure debt: move the appendix-grade proofs out of `#scope-adaptive-system`; move the Claim Records out of segment bodies (item 12); prune the dated integration blocks in Working Notes to forward pointers.
5. Then the starved objectives, in INTENT's order.
