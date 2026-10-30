# INTENT — the objectives tree

Every piece of work in this effort feeds one key result (KR) below, and every agent at every depth, and every successor after compaction, knows which one. Work that feeds none is a red flag: the tree is stale, a finding is unrecorded, or the work has drifted. Say so to the lead; don't resolve it silently. The tree is set top-down *and* bottom-up: propose KRs and sub-objectives under the item you serve. This file stays a tree. Evidence lives in the artifacts it points to. History lives in commit bodies and `CHANGELOG.md`. Nothing in this directory records finished work.

## Top intent

> Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself. — Joseph, 2026-10-30

In service of *"TRUTH about agency … discovered, surfaced, truthified, truthfully synthesized and crossed to the right applications, AND effectively communicated anew."* His full frame is in `README.md`.

**Done means:** ASF says what is true about agency, only what its warrant supports, in a form a newcomer can follow and check.

## O1 — We can say plainly what the theory is trying to illuminate

*First, because it decides what the rest mean.*

- **KR1.1** An owner-level review names the theory's actual centre, its problems, and the most fruitful ones to address. Everything it inherits is verified. · *running* · `owner-review/`
- **KR1.2** A purpose statement for ASF and for each volume: what question it answers, about which agents, and what checkable prediction it makes. It is drafted from the evidence, starting from the plain statements readers have already made, and the uncertainty is resolved, not routed. · *waits on 1.1; inputs in `owner-review/00-review.md` §6 and `influx-scout/MAP.md` §4*
- **KR1.3** Each body of results is placed on the arc: universal or one model among several, for which class of agents, what it claims is optimal, **and what would refute it**. · *waits on 1.1; inputs in `internal-surfaces/00-cross-surface-map.md` §2*
  - **KR1.3a** Every segment declares its register: a fact about the formalism, a description of real agents, or a design or optimality claim. Any claim of the second or third kind names the real systems that meet its hypotheses, an instance, and a refuting observation. *Context:* "exact" means only that the proof is valid, and readers hear it as "true of agents". · *proposed by the owner review's explorers*

## O2 — The theory is correct and coherent

- **KR2.1** Statements say exactly what their warrant supports (scope, quantifiers, standpoint, tier), front-door surfaces first. Each chapter is checked by a reader other than its repairer. · *not started; defect list in `internal-surfaces/` §3*
- **KR2.2** No canon statement contradicts another. · *not started*
- **KR2.3** Overclaims are strengthened before they are softened; refuted claims are replaced, not kept as ghosts. · *F72: ceiling refuted (verify-1); integrator landing it*
- **KR2.4** External research the theory needs is adopted where it belongs, with citation, under its original names. · *not started; lists indexed in `internal-surfaces/` §6*
- **KR2.5** Where a standard academic term exists, it replaces or anchors the coinage. · *not started*
- **KR2.6** Whatever crosses the canon boundary, in either direction, is faithful to its source: canon's citations of papers and data, and papers' and notes' claims about canon. · *not started; instances in `influx-scout/MAP.md` §3 (D12, D13, D17)*

## O3 — Nothing true is stranded

- **KR3.0** Where argued, non-derived claims live (ASF segments or logos) is decided before KR3.3 lands any of them. The input is Joseph's upstream-first principle of 2026-09-25 (`~/src/arch/logos/msc/dialog-2026-09-25-revision-orientation.md`). · *not started*
- **KR3.1** ASF material elsewhere in the estate is mapped, with dates and example documents. · *delivered, except `aisi-eoi` and `notability-extracts`* · `influx-scout/MAP.md`
- **KR3.2** Material stranded inside asf is mapped and joined by slug, with verify-state. · *delivered* · `internal-surfaces/`
- **KR3.3** Each mapped *addition* that bears on the theory is integrated at honest tier, or set aside with a recorded reason. Canon defects found by mapping go to O2. · *not started*
  - 3.3a: small landings that already have work orders;
  - 3.3b: heavy landings, each with its own integrator;
  - 3.3c: the July decision briefs, resolved on the merits (`msc/decision-briefs-2026-07-15.md`; each brief is deleted when decided).
- **KR3.4** Every OUTLINE row has a file or an honest mark, and every legacy `old-*` file has a fate. · *not started*
- **KR3.5** Theory-bearing material that exists only uncommitted on disk gets a durable home before integration depends on it. · *not started; list in `influx-scout/MAP.md` §5*

## O4 — The truth reaches a reader

- **KR4.1** A front door and an arc that a newcomer can follow. · *not started*
- **KR4.2** Comprehension is measured before and after, with fresh readers. · *not started*
- **KR4.3** Every front surface says only what canon says, generated and hand-written alike. · *not started*

## O5 — The machinery tells the truth about itself

- **KR5.1** The record of how sure ASF is of each claim is truthful: declared inputs plus recorded checks, not hand-set labels. · *notes* · `system/01-…`
- **KR5.2** One live place to find what is open, and no residue that reads as live: routing targets that don't resolve, and hand-offs to cycles that don't exist. · *partly*
- **KR5.3** The practices that keep truth are written where agents meet them. · *ongoing* · `doc/sop/agents.sop.md`
- **KR5.4** This tree stays true and lean. · *lead*
- **KR5.5** Working Notes are classified by kind and status, not drained. · *not started; seed in `internal-surfaces/wn-ledger-seed/`*
- **KR5.6** The arc has an owner: when a result lands, the anchors it changes are updated, with a trigger. · *not started*

## Who is on what

| Who | KR | Writes to |
|---|---|---|
| Lead coordinator (Opus 5.5, session "asf-cleanup") | 5.4, plus coordination | `INTENT.md`, `HANDOFF.md`, `system/` |
| Owner review (Fable) and its subagents | 1.1 | `owner-review/` |
| F72 integrator (Opus) | 2.3, 3.3a | canon: the hard-ceiling carriers listed in verify-1 §7 |

Finished and on the line for follow-ups: the internal-surfaces mapper (KR3.2), the influx scout (KR3.1), and the F72 verifier (KR2.3).

## Using this file

- **Briefing an agent:** name its KR and quote the top intent. Ask it to pass its KR down to any agent it launches.
- **Writing an artifact:** put its KR at the top.
- **After a compaction:** read this file, then `HANDOFF.md`.
- **Revising the tree:** keep each KR to one line plus its status and where it lives. When a KR is met, its line goes, and the history goes into the commit body.
