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

  Joseph's strategy-DAG example is the specimen of the question, not the scope. *Not started; waits on KR1.1.*

### O2 — The theory itself is correct and coherent

- **KR2.1** The statement layer says exactly what the algebra supports. Scope, quantifiers, standpoint and tier must match the warrant, chapter by chapter. Each chapter is checked by an independent reader, not by whoever made the repair. *Evidence that this is where truth leaks: audit 731548 found "statement-layer defects sitting on correct algebra." Not started.*
- **KR2.2** No canon statement contradicts another, checked across segments, not only within them. *Not started.*
- **KR2.3** Claims found overclaimed are strengthened before they are softened. Every refuted claim is replaced, not kept as a softened ghost. *Feeding it: F72, the independent re-derivation of `#deriv-strategic-persistence-hard-ceiling`. Queued; refused once by the subagent concurrency limit.*
- **KR2.4** External research the theory needs is integrated where it belongs, adopted with citation under its original names. *Known inputs:*
  - `ref/prior-art-analysis/agentic-systems-landscape-2026-08-22.md`, whose segment-level recommendations are verified unintegrated (LOG, 2026-10-30);
  - `ref/enrichment-candidates-2026-05-21.md`;
  - the 21 May prior-art analyses.

  *Not started.*
- **KR2.5** Terminology tells the truth. Where an agent-coined name stands in for a concept known under a standard academic name, adopt that name, or anchor the coinage to it and say why it differs. Joseph: agents *"fall into existing ASF terminology that was essentially named arbitrarily … sometimes not realizing they would be better to adopt standard academic terms even if from a different field."* *Not started; the naming-cycle backlog of 506 unrouted R2 currents is input, not the method.*

### O3 — Nothing true is stranded

- **KR3.1** ASF material elsewhere in the estate is mapped, with dates and example documents:
  - the papers;
  - aat-refactored and aat-v3;
  - agent-core, context-saliency, the AISI work, ai-risk-model, practica-dag, arch notes;
  - INFLUX/`.int` dirs.

  *Feeding it: (A) `influx-scout/`, Opus. Status: running.*
- **KR3.2** Live theory stranded inside asf is mapped: Working Notes, audit gold, spikes, `msc/`, trackers. *Feeding it: (A2) `internal-surfaces/`, Opus. Status: running.*
- **KR3.3** Each mapped item that bears on the theory is integrated into canon at honest tier, or set aside with its reason recorded where a future reader will find it. *Not started; waits on KR3.1, KR3.2 and O1, which decides what "bears on the theory" means.*

### O4 — The truth reaches a reader

- **KR4.1** A front door and an arc. A newcomer can learn what ASF claims, in what order, and how sure it is, without reconstructing it from 290 segments. *Not started.*
- **KR4.2** Comprehension is measured before and after, with fresh readers on the same chapters. A candidate instrument is the comprehension quiz from audit run 374162. *Not started.*
- **KR4.3** Generated surfaces (README, FINDINGS, LEXICON, CURRENT-VOL1) say only what canon now says. *Not started.*

### O5 — The machinery tells the truth about itself, and the system keeps it true

This is the "meta" in Joseph's goal. It earns its place only where it changes what a reader can trust. Joseph: *"Thoughts about this as a system in and of itself — a system of agentic truthification about agentic theory, is wholely worthy."*

- **KR5.1** How sure ASF is of each claim is recorded truthfully. Hand-set `status:` was measured to disagree with itself (census, 2026-09-29). It is replaced by declared inputs plus recorded checks, or another design that survives scrutiny. *Feeding it: `system/01-epistemic-machinery-in-place.md`, hypotheses H-a..H-d. Status: notes only.*
- **KR5.2** One live place to find what is open, and no residue that reads as live work. The trackers, PRACTICA's May priorities, and the July decision briefs are reconciled into what this effort actually runs on. *Partly fed:*
  - July decision briefs triaged (LOG);
  - `core.hooksPath` fixed.
- **KR5.3** The practices that kept truth here are written where agents meet them, and the ones that failed are changed. *Fed so far: standing notes in `doc/sop/agents.sop.md`.* *Candidates, not yet adopted:*
  - a receiver-side orientation for subagents (`~/src/arch/SUBAGENT-INSTRUCTIONS-notes.md`);
  - `SPIKE-PROMPT.template.md` for all spikes.
- **KR5.4** This file stays the true actuator. Every running piece of work maps to a KR here, and stale KRs are revised promptly. *Owner: lead coordinator.*

## Who is on what right now

*Joseph: "every subagent, subsubsubsubagent, and successor after a context compaction should know exactly what item they are focused on in that objectives tree." The lead keeps this table current. Agents launched by the agents below inherit their launcher's KR unless their brief names a narrower one, and should state it at the top of whatever they write.*

| Who | Launched | KR | Writes to |
|---|---|---|---|
| Lead coordinator (Claude Opus 5.5, session "asf-cleanup") | 2026-10-30 | KR5.4 (this file as actuator), plus coordination of all KRs | `LOG.md`, `INTENT.md`, `system/` |
| Owner review (Fable) and its subagents | 2026-10-30 ~11:30 MDT | KR1.1 | `owner-review/` |
| Influx scout (Opus) and its subagents | 2026-10-30 ~11:30 MDT | KR3.1 | `influx-scout/` |
| Internal-surfaces mapper (Opus) and its subagents | 2026-10-30 ~11:30 MDT | KR3.2 | `internal-surfaces/` |
| F72 verifier | queued | KR2.3 | `spikes/spike-strategic-persistence-hard-ceiling-convention-2026-05-31-verify-1.md` |

## How to use this file

- **Briefing an agent:** name the KR it feeds and quote the top intent. Point it here, and ask it to pass its KR down to any agent it launches.
- **After a context compaction:** read this file first and find your row. If your row is missing or stale, say so before continuing.
- **Doing work:** if what you're doing doesn't feed a KR, stop and say so. Maybe the KR is missing, and the finding belongs here. Maybe the work is drift.
- **Finding something that changes an objective:** that is the most valuable kind of finding. Send it to the lead, and it lands here as a revision.
- **Proposing your own KRs and sub-objectives.** This tree is set top-down *and* bottom-up. Joseph, 2026-10-30: *"like in OKR land among humans-- they are often top-down AND bottom-up decided-- a bit of give and take. I recommend giving agents the benefit of the doubt and letting them come up with their own KRs and possibly sub-objectives."* An agent that sees a better key result, or the sub-objectives its own work needs under the item it serves, proposes them. Write them at the top of its artifact or send them to the lead, and they get added here, credited to that agent. Where the lead thinks something is missing, it says so early and as a peer, in the form Joseph gave: *"oh, did you know about ___? I wonder if ___ would be a better approach? (but this isn't a prescription-- what have you already thought?)"*

## Change notes

- 2026-10-30, ~12:05 MDT, lead coordinator: first version. O1 is written first because the purpose review (Joseph's request) decides what the others mean. Expect a substantial revision when the owner review lands.
