# HANDOFF — for the lead's successor

What only the lead knows: what it has actually read, what it holds only on another agent's word, and what is in flight. Findings are not restated here; they live in the documents named below. Updated at every checkpoint (last: 2026-10-30 ~13:20 MDT).

## Resume

Read `INTENT.md`, then this file. Joseph's governing words are in `README.md`. For history, read the commit bodies (`git log` on `msc/inside-out-2026-10/` and canon). The SendMessage handles for running agents live in the session, not here. If they're lost, the agents' directories are the record.

## Read-ledger

**Read whole by the lead**

- *This effort*
  - `internal-surfaces/00-cross-surface-map.md`
  - `influx-scout/MAP.md`. Its regional files are for integrators and are not read by the lead.
  - `owner-review/00-review.md` (final v2), `owner-review/integrator-items.md`
  - `owner-review/history/{2026-03-04,2026-05,2026-06-10}.md`
  - `spikes/spike-strategic-persistence-hard-ceiling-convention-2026-05-31-verify-1.md`. Its central gain claim was re-run by the lead.
- *asf*
  - `PRACTICA.md`
  - `audits/STATUS.md`
  - `msc/decision-briefs-2026-07-15.md`
  - `ref/prior-art-analysis/agentic-systems-landscape-2026-08-22.md`
  - `doc/sop/agents.sop.md`
- *aat-v3*
  - `msc/00-orientation-log.md`
  - `msc/40-emerging-picture.md`
  - `msc/maps/aat-refactored.md`
  - `msc/maps/asf-audits-and-spikes.md`
  - `msc/vsect/{README,model,vsect}.md`
- *aat-refactored*
  - `spikes/fresh-view-2026-09-29/census-findings.md`
  - `HANDOFF.md`, through "Do next"
- *arch*
  - `SUBAGENT-INSTRUCTIONS-notes.md`
  - `AGENTIC-DELEGATION.md`

**Partial**

- `~/src/arch/SPIKE-PROMPT.template.md`: lines were cut at 400 characters. Read it whole before filling it.
- The first ~25 lines only of each of these:
  - `ref/enrichment-candidates-2026-05-21.md`
  - `ref/prior-art-analysis/00-impact-meta-summary.md`
  - `02-tst-core/lit-review/next-research*.md`

**Held only on another agent's word**

- Explorer findings the owner review relayed in its messages. The explorer files themselves are unread.
- Everything in `influx-scout/MAP.md` that is relayed from regional scouts. Only its `[coordinator-verified]` rows were checked at HEAD.

**Not read**

- `owner-review/explorers/*`, `owner-review/verified-at-HEAD.md`. The review carries their claims with its own verification rows; read the explorer files themselves before landing anything from them.
- `influx-scout/` regional files
- the six per-surface maps in `internal-surfaces/`
- aat-refactored's `scratch/PROPOSAL-2026-09-29-foundation-and-sops.md`
- vsect's `core`, `storage`, `session-aat`, `open`
- almost every segment body
- `CHANGELOG.md`: a log, not a source

**Verified by the lead at the primary**

- The segment and file counts in `README.md` (246 segments, 44 `old-*` files, the commit split, WN counts).
- `core.hooksPath` was dead.
- The "Reading AAT" preamble was removed in `feccd0d2`.
- relata holdings and segment uptake for the landscape survey's key works.

## In flight

- **Running.** Read each agent's final documents whole before acting on anything it says.
  - F72 integrator (KR2.3/3.3a): it commits but doesn't push; the lead reviews the diff, then pushes.
- **Waiting on Joseph: nothing.** Resolve uncertainty rather than route it. Two items that used to wait on him now sit in KR3.3a:
  - Canon citing the gitignored `msc/joseph-working-notes.md`. Lift any theory content those citations need into canon, then remove the citations.
  - The 08-22 cleanup items.
- **Next for the lead.**
  1. When the F72 integrator lands, review its diff, push, and update CHANGELOG.
  2. Then take a beat (see the rhythm below): nothing running; rethink objective I, the system, from the top.
  3. After the beat, launch A and B first. A Fable focused on the system, the counterpart to the theory review, is a candidate for I.
- **Joseph's word needed (deletion needs his confirmation):** the NeurIPS scout published its map as a private claude.ai artifact without being asked (https://claude.ai/artifact/AWfAyP5UyNCcu4GFqp5CWE). Should it be deleted?

## The lead's rhythm

Joseph: *"regularly take a beat-- let all agents finalize so you have some quiet time, and rethink from the very top w/ the highest level ideation and thinking... To keep you from becoming task-oriented and missing the big picture of the *system* in service of *truth*."*

At each beat, nothing is running. The lead re-reads INTENT from the top intent down. It asks what the system (the machinery, the clutter, the methodology, the tools) needs in order to serve truth. Only then does it launch the next work. Healing the system is the lead's part, done with agents, possibly including a Fable focused on the system as the owner review was focused on the theory.

## The lead's known hazards

- **Building on relay.** Agents' chat claims get adopted faster than their documents get read. Read first, then build.
- **Intent bloat.** INTENT accretes evidence, credits and history. Joseph: *"It will get bloated and if it is not corrected immediately, it will be just yet another thing to integrate."* Correct it at the moment it bloats.
- **Narrative regeneration.** Summaries written from memory drift from the record. That is why this file only points.
- **Breadcrumbs.** History and finished items accumulate in working files because writing them feels safe. Joseph: *"It does [do harm]. That's what changelog is for."* Nothing in this directory records what is finished.
