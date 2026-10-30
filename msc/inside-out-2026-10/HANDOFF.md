# HANDOFF — for the lead coordinator's successor (after compaction or turnover)

**Feeds: KR5.4** (INTENT stays the true actuator) and Joseph's succession standard: *"ensuring that this continues to develop as a system so that when I compact the successor will be able to fill in their knowledge/context gaps without making things up — turnover quality improving rather than regressing each time."*

*Kept current by the lead at every checkpoint. If you are the successor: a compaction summary reads as knowledge, and it isn't. This file exists so you can tell what your predecessor actually read from what it was only told. Where the two differ, go read. Don't reconstruct.*

## Resume in this order

1. `INTENT.md`: find your row in "Who is on what", and the KR it names.
2. This file, whole: especially the read-ledger and the relayed-claims list.
3. `LOG.md`, the last few entries.
4. `README.md`: Joseph's words verbatim, plus measurements.
5. The memory file `project_inside_out_2026_10.md`. It loads automatically when a session starts in asf.

Agent handles for SendMessage live in the session, not in this repo. If you lost them in compaction, the peers' files under this directory are the record. A finished peer can be resumed only if you still have its handle.

## The lead's read-ledger

The ledger has four levels:

- **whole:** read in full, first-hand.
- **partial:** read in part; the part read is named.
- **relay:** known only from another agent's message or summary.
- **not read:** not opened.

Updated 2026-10-30 ~13:00 MDT.

**Read whole**

- *aat-v3:* `msc/00-orientation-log.md`, `msc/40-emerging-picture.md`, `msc/maps/aat-refactored.md`, `msc/maps/asf-audits-and-spikes.md`; and `msc/vsect/{README,model,vsect}.md`.
- *asf root:* `PRACTICA.md`, `JOSEPH-TODO.md`, `audits/STATUS.md`, `msc/decision-briefs-2026-07-15.md`.
- *external research:* `ref/prior-art-analysis/agentic-systems-landscape-2026-08-22.md`.
- *aat-refactored:* `~/src/aat-refactored/spikes/fresh-view-2026-09-29/census-findings.md`, and the opening of `~/src/aat-refactored/HANDOFF.md` (to "Do next").
- *arch:* `~/src/arch/SUBAGENT-INSTRUCTIONS-notes.md`.
- *this effort:* `internal-surfaces/00-cross-surface-map.md`.
- *orientation outputs:* `aspectus` of asf; `projects -cvvv`; `projects heatmap -c --triple`.
- *loaded as context:* `doc/sop/agents.sop.md` and `~/src/arch/AGENTIC-DELEGATION.md`.

**Partial**

- `~/src/arch/SPIKE-PROMPT.template.md`: every line, but cut at 400 characters, so long paragraphs were truncated. Read it whole before filling it.
- `ref/enrichment-candidates-2026-05-21.md`: first 25 lines.
- `ref/prior-art-analysis/00-impact-meta-summary.md`: first 25 lines.
- `02-tst-core/lit-review/next-research*.md`: first 25 lines of each.
- `msc/meta-process-review-*`: not opened, but cited inside other documents.
- segments: frontmatter counts only, plus targeted greps in `deriv-strategic-persistence-hard-ceiling` and `agents.sop.md:285`.

**Relay only (do not treat as known)**

- The owner review's findings, as given in its two chat messages. Its documents in `owner-review/` are **not yet read by the lead**.
- The influx scout's progress messages. Its documents are **not read**.
- Everything in the six per-surface maps under `internal-surfaces/`, beyond what the synthesis says.

**Not read**

- `owner-review/*`, `influx-scout/*`, and the six per-surface maps.
- aat-refactored's `scratch/PROPOSAL-2026-09-29-foundation-and-sops.md`.
- vsect's `core.md`, `storage.md`, `session-aat.md`, `open.md`.
- `CHANGELOG.md` (by design: it's a log, not a source).
- Almost all segment bodies.

## Claims now in INTENT.md that the lead has *not* verified

These came in through peers. They are labelled as relayed in INTENT, and should be verified at the primary before anything is built on them.

- The owner review's central finding: Part II's apparatus doesn't say what it claims about actual agents, or what would refute it.
- The May memos' standard-name citations reached only 6 segment bodies.
- `#scope-adaptive-system:18,45` excludes standard RL on a refuted rationale.
- `INTRODUCTION.md:27` overstates `#sketch-structural-adaptation-genericity`.
- Seven spike files point to a nonexistent "standing cycle".
- NeurIPS Paper 2's do-operator grounding.
- The 04-22 nineteen-minute appendix landings.

**Verified by the lead**, so you can rely on these:

- 246 segments; 44 `old-*` files; the commit split since 08-24; Working Notes counts.
- `core.hooksPath` was dead.
- The "Reading AAT" preamble was removed in `feccd0d2`.
- relata holdings for the survey's works.
- Richens is absent from `form-agent-model`; Virgo is absent from `der-directed-separation`.
- `deriv-strategic-persistence-hard-ceiling` still owes its re-derivation.

## Open threads

- **Running:** the owner review (KR1.1, Fable), the influx scout (KR3.1, Opus), and the F72 verifier (KR2.3, Opus). When each lands, read its documents whole *before* acting on anything it says.
- **Waiting on Joseph:** `msc/joseph-working-notes.md` is gitignored and was never committed, yet `#def-eli-cohort` WN and both 03/04 OUTLINE source lists cite it. This is a privacy call. A7 (splitting 04-eli-core into a private repo) stays his.
- **Next for the lead:** once the owner review lands, revise O1/INTENT from its documents. Then put KR1.2 (purpose) to Joseph as candidate statements side by side, with provenance, *not* one crowned answer. Then commission the KR3.3a small landings.

## System facts learned the hard way (2026-10-30)

- **Concurrency cap.** The harness caps the session at **20 concurrent subagents**. Peers that fan out early hold their slots until they drain, so prioritize slots by KR. O1 gates the rest.
- **Forks can't spawn subagents.** A fork-based fan-out gets no Sonnet sweeps.
- **The Opus safeguard.** Opus scouts reading the AISI cluster died on its "reasoning_extraction" safeguard. A transcript that trips it can't be resumed, and a Sonnet replacement is the workaround.
- **"report" in filenames.** The harness turns an artifact into a chat report if "report" appears anywhere in its filename.
- **Mid-run messages.** A background agent can message `main` mid-run (SendMessage; load it with ToolSearch). Peers in this effort have used it well.
- **zsh doesn't word-split unquoted variables.** For file lists, use `find … -print0 | xargs -0`.

## The lead's own known hazards (from its professio, calibrated by Joseph)

- **Knowing for real vs. keeping the tree true.** The two pull against each other. The failure seen so far is adopting peers' chat claims into INTENT faster than reading their documents. The remedy is the relay list above, kept honest, and reading before building.
- **INTENT.md is accreting evidence that belongs in the maps.** It should stay a scannable tree: objectives, KRs, what feeds each, and status. A successor may compress the evidence out, *with pointers to where it lives*, provided nothing is lost.
