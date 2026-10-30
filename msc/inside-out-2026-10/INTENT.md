# INTENT — what this effort is for, and what each piece of work feeds

*The central reference for the in-place refactor of ASF. Every agent working in this effort should be able to name the key result (KR) their work feeds, and through it the objective and the top intent. **Work that feeds nothing here is a red flag** (Joseph, 2026-10-30): either this file is out of date, or findings haven't been recorded here, or the work has drifted. Whoever notices the mismatch says so to the lead coordinator (SendMessage to `main`, or in `LOG.md`). It is never silently resolved in either direction.*

*Maintained by the lead coordinator; revised as findings land. Every revision is dated in the change notes at the bottom. Joseph's words are quoted; everything else is the coordinator's current best statement, open to challenge by any agent.*

## Top intent

Joseph, 2026-10-30, verbatim:

> Goal set: Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself.

> This effort is to *serve TRUTH* -- not me, not "task-completion" or tidyness, not accomplishing a plan, not what sounds good or looks good--- TRUTH about agency. […] TRUTH is only served if it is discovered, surfaced, truthified, truthfully synthesized and crossed to the right applications, AND effectively communicated anew, with proper epistemology and real humility fully intact. […] We are to create something true, wise, strong, and beautiful-- inasmuch as strong, wise, and beautiful are the servants […] of TRUTH.

Read together, these give the test for "complete." **ASF says what is true about agency, only what its warrant supports, in a form a newcomer can follow and check.** The work is done in place, across the theory, every artifact around it, and the machinery that records how sure it is. Every objective below is one face of that test, and none is a goal in itself.

## Objectives and key results

*Status words below are hand-written by the coordinator as of the date shown. Per this effort's own system notes, treat them as claims to check, not as computed standing.*

### O1 — We know, and can say plainly, what the theory is trying to illuminate

Joseph's named pain: *"I don't even know what this theory is *trying* to illuminate"*, and the *"loss of clarity on what is being theorized — a lot of it is there, it's just not part of the overall arc and narrative."* Until O1 holds, every other objective risks polishing the wrong thing.

- **KR1.1** A highest-level owner review of ASF exists. It verifies everything it inherits, and names what the problems are and which are most fruitful to address. *Feeding it: (B) `owner-review/`, Fable, launched 2026-10-30. Status: running.*
- **KR1.2** A purpose statement for ASF as a whole and for each volume. Each says what question the part answers, about which class of agents, and what it predicts that could be checked. Drafted from the owner review, the uses the estate actually makes of ASF, and Joseph's words; then ratified, amended or overturned by Joseph. *Not started; waits on KR1.1.*
- **KR1.3** Every major body of results is placed on the arc. For each:
  - is it claimed universal, and for which class?
  - is it one model among several, and how does it map to concrete examples?
  - does it claim optimality, and for whom?
  - **what observation or construction would refute it?** This is a falsifier per body of results. It makes the other three checkable, and it hands the empirical program (vivarium, empirica) its targets.

  The falsifier question was proposed by the owner review (Fable), 2026-10-30, and adopted. Joseph's strategy-DAG example is the specimen of the question, not the scope. *Not started; waits on KR1.1.* The internal-surfaces map's §2 gives six clusters as inputs, as candidates and not verdicts:
  - what belief and goal are, and what separating them costs;
  - the typed epistemic target and the standpoint gap;
  - the strategy DAG, already partly answered in Working Notes;
  - the impossibility spine, re-carved;
  - Vol 4's spine sitting in Vol 1;
  - what each volume says it proves.

  Directed separation and the standpoint of the persistence condition are where "universal, for which class?" is already partly written.

### O2 — The theory itself is correct and coherent

- **KR2.1** The statement layer says exactly what the algebra supports. Scope, quantifiers, standpoint and tier must match the warrant, chapter by chapter. Each chapter is checked by an independent reader, not by whoever made the repair. *Evidence that this is where truth leaks: audit 731548 found "statement-layer defects sitting on correct algebra." Not started.*
- **KR2.2** No canon statement contradicts another, checked across segments, not only within them. *Not started.*
- **KR2.3** Claims found overclaimed are strengthened before they are softened. Every refuted claim is replaced, not kept as a softened ghost. *Feeding it: F72, the independent re-derivation of `#deriv-strategic-persistence-hard-ceiling`. Launched ~12:45 MDT after being refused once by the subagent concurrency limit.*
- **KR2.4** External research the theory needs is integrated where it belongs, adopted with citation under its original names. *Known inputs:*
  - `ref/prior-art-analysis/agentic-systems-landscape-2026-08-22.md`, whose segment-level recommendations are verified unintegrated (LOG, 2026-10-30);
  - `ref/enrichment-candidates-2026-05-21.md`;
  - the 21 May prior-art analyses.

  *Not started.*
- **KR2.5** Terminology tells the truth. Where an agent-coined name stands in for a concept known under a standard academic name, adopt that name, or anchor the coinage to it and say why it differs. Joseph: agents *"fall into existing ASF terminology that was essentially named arbitrarily … sometimes not realizing they would be better to adopt standard academic terms even if from a different field."* *Not started; the naming-cycle backlog of 506 unrouted R2 currents is input, not the method.* The owner review reports this as verified (not yet read by the lead). The May prior-art memos already name the standard neighbors:
  - the Separation Principle, for directed separation;
  - fault-tree common-cause failure, for the Correlation Hierarchy;
  - Gott/Lindy, for change-expectation.

  Those citations reached the bodies of only 6 segments. So much of KR2.5, and of KR2.4, is a landing sweep from existing memos, not new research.

### O3 — Nothing true is stranded

- **KR3.1** ASF material elsewhere in the estate is mapped, with dates and example documents:
  - the papers;
  - aat-refactored and aat-v3;
  - agent-core, context-saliency, the AISI work, ai-risk-model, practica-dag, arch notes;
  - INFLUX/`.int` dirs.

  *Feeding it: (A) `influx-scout/`, Opus. Status: running.*
- **KR3.2** Live theory stranded inside asf is mapped *and joined by slug, with each item's verify-state*, so that an integrator can go from a segment to everything bearing on it. Wording proposed by the internal-surfaces mapper. *Delivered 2026-10-30:* `internal-surfaces/00-cross-surface-map.md` plus six per-surface maps with slug tables, read whole by the lead. Re-runnable forms are prototyped there (`audit-gold-status.py`, `wn-ledger-seed/`).
- **KR3.3** Each mapped item that bears on the theory is integrated into canon at honest tier, or set aside with its reason recorded where a future reader will find it. Split by what blocks it, as the internal-surfaces map proposed. That map found the stall sits *downstream* of verification: verified, integration-ready work exists and nobody runs it.
  - **KR3.3a** The small, exact landings with work orders already written are landed. The list is in internal-surfaces §4, first list, and includes F72.
  - **KR3.3b** Each heavy landing gets an integrator distinct from its spiker and verifier, and lands or is set aside with a recorded reason. These include the decomposition cluster with the ε-programme, SP-30, the standpoint discipline with the reserve repair, honest activation, the no-go re-carve, and CL-1 (internal-surfaces §4, second list).
  - **KR3.3c** The backlog gated on Joseph, released today, is decided. Where a lead recommendation exists, it decides by default (internal-surfaces §4, third list).

  *Not started; waits partly on O1, which decides what "bears on the theory" means.*
- **KR3.4** The volumes' own completeness. Every OUTLINE row has a file or is honestly marked or removed. The 44 legacy `old-*` files under `src/` are each mapped to a live segment, a candidate, or a deliberate retirement. Proposed by the internal-surfaces mapper. TST (29 segments; its theory "several times its canon") and 03/04 (20 OUTLINE rows with no file) are where most is stranded. *Not started.*

### O4 — The truth reaches a reader

- **KR4.1** A front door and an arc. A newcomer can learn what ASF claims, in what order, and how sure it is, without reconstructing it from 246 segments. *Not started.*
- **KR4.2** Comprehension is measured before and after, with fresh readers on the same chapters. A candidate instrument is the comprehension quiz from audit run 374162. *Not started.*
- **KR4.3** Front surfaces say only what canon now says. That covers the generated ones (README, FINDINGS, LEXICON, CURRENT-VOL1) and, per the internal-surfaces map, the hand-written ones (`01-aat-core/INTRODUCTION.md`, `HISTORICAL-CONTEXT.md`, the README partials). The hand-written ones carry claims canon does not hold, and nothing signals when they go stale. *Not started.*

### O5 — The machinery tells the truth about itself, and the system keeps it true

This is the "meta" in Joseph's goal. It earns its place only where it changes what a reader can trust. Joseph: *"Thoughts about this as a system in and of itself — a system of agentic truthification about agentic theory, is wholely worthy."*

- **KR5.1** How sure ASF is of each claim is recorded truthfully. Hand-set `status:` was measured to disagree with itself (census, 2026-09-29). It is replaced by declared inputs plus recorded checks, or another design that survives scrutiny. *Feeding it: `system/01-epistemic-machinery-in-place.md`, hypotheses H-a..H-d. Status: notes only.*
- **KR5.2** One live place to find what is open, and no residue that reads as live work. The trackers, PRACTICA's May priorities, and the July decision briefs are reconciled into what this effort actually runs on. *Partly fed:*
  - July decision briefs triaged (LOG);
  - `core.hooksPath` fixed.

  One mechanical check, proposed by the internal-surfaces mapper: a disposition or routing target that doesn't resolve (a slug with no file, a backlog no tracker holds) is a defect a tool catches. Five strandings found today had that shape.
- **KR5.3** The practices that kept truth here are written where agents meet them, and the ones that failed are changed. *Fed so far: standing notes in `doc/sop/agents.sop.md`.* *Candidates, not yet adopted:*
  - a receiver-side orientation for subagents (`~/src/arch/SUBAGENT-INSTRUCTIONS-notes.md`);
  - `SPIKE-PROMPT.template.md` for all spikes.
- **KR5.5** Working Notes are *classified*, not drained. Proposed by the internal-surfaces mapper. Every WN item carries a kind and a status, so that the open frontier, the correctness backlog and the owed research become visible. Today they hold all of those in prose, plus influx index, pedagogy reservoir, regression memory and process history, without status or owner. Each kind has a different destination. This replaces the stuck "WN drain" question (decision brief A4). *Seed:* `internal-surfaces/wn-ledger-seed/`. *Not started.*
- **KR5.4** This file stays the true actuator. Every running piece of work maps to a KR here, and stale KRs are revised promptly. *Owner: lead coordinator.*

## Who is on what right now

*Joseph: "every subagent, subsubsubsubagent, and successor after a context compaction should know exactly what item they are focused on in that objectives tree." The lead keeps this table current. Agents launched by the agents below inherit their launcher's KR unless their brief names a narrower one, and should state it at the top of whatever they write.*

| Who | Launched | KR | Writes to |
|---|---|---|---|
| Lead coordinator (Claude Opus 5.5, session "asf-cleanup") | 2026-10-30 | KR5.4 (this file as actuator), plus coordination of all KRs | `LOG.md`, `INTENT.md`, `system/` |
| Owner review (Fable) and its subagents | 2026-10-30 ~11:30 MDT | KR1.1 | `owner-review/` |
| Influx scout (Opus) and its subagents | 2026-10-30 ~11:30 MDT | KR3.1 | `influx-scout/` |
| Internal-surfaces mapper (Opus) | 2026-10-30 ~11:30 MDT; **finished ~12:30** (on the line for follow-ups) | KR3.2 (delivered) | `internal-surfaces/` |
| F72 verifier (Opus) | 2026-10-30 ~12:45 MDT | KR2.3 (and KR3.3a) | `spikes/spike-strategic-persistence-hard-ceiling-convention-2026-05-31-verify-1.md` |

## How to use this file

- **Briefing an agent:** name the KR it feeds and quote the top intent. Point it here, and ask it to pass its KR down to any agent it launches.
- **After a context compaction:** read this file first and find your row. If your row is missing or stale, say so before continuing.
- **Doing work:** if what you're doing doesn't feed a KR, stop and say so. Maybe the KR is missing, and the finding belongs here. Maybe the work is drift.
- **Finding something that changes an objective:** that is the most valuable kind of finding. Send it to the lead, and it lands here as a revision.
- **Proposing your own KRs and sub-objectives.** This tree is set top-down *and* bottom-up. Joseph, 2026-10-30: *"like in OKR land among humans-- they are often top-down AND bottom-up decided-- a bit of give and take. I recommend giving agents the benefit of the doubt and letting them come up with their own KRs and possibly sub-objectives."* An agent that sees a better key result, or the sub-objectives its own work needs under the item it serves, proposes them. Write them at the top of its artifact or send them to the lead, and they get added here, credited to that agent. Where the lead thinks something is missing, it says so early and as a peer, in the form Joseph gave: *"oh, did you know about ___? I wonder if ___ would be a better approach? (but this isn't a prescription-- what have you already thought?)"*

## Change notes

- 2026-10-30, ~12:40 MDT: adopted all eight of the internal-surfaces map's proposals (its §0 list), each credited in place:
  - KR3.2 reframed and marked delivered;
  - KR3.3 split into 3.3a/b/c by what blocks it;
  - new KR3.4 (the volumes' own completeness);
  - new KR5.5 (classify Working Notes rather than drain them);
  - a resolvability check under KR5.2;
  - KR4.3 widened to the hand-written front surfaces;
  - O1 input clusters listed under KR1.3;
  - 290 corrected to 246 segments, re-verified by the lead.

  I adopted them because each is grounded in a named section of its map, which I read whole.

- 2026-10-30, ~12:20 MDT: adopted the owner review's proposed falsifier question into KR1.3. Added its verified note that KR2.4/KR2.5 are largely a landing sweep from existing May memos, to be confirmed when the lead reads the review whole.
- 2026-10-30, ~12:05 MDT, lead coordinator: first version. O1 is written first because the purpose review (Joseph's request) decides what the others mean. Expect a substantial revision when the owner review lands.
