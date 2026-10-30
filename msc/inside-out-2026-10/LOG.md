# LOG — inside-out-2026-10

*Dated trail, newest at the bottom. Written by whichever agent acts; each entry names its author-role. Times come from `date`, not felt time.*

## 2026-10-30 — lead coordinator (Claude Opus 5.5, session "asf-cleanup")

- **Orientation (minor, by request):** `aspectus` on asf, `projects -cvvv`, and `projects heatmap -c --triple`, all read whole. Found the AAT rewrite lineage outside asf: `aat-refactored` (the memory's `aat-reboot` path was stale, now corrected) and `aat-v3`. Read aat-v3's `msc/00-orientation-log.md`, `msc/40-emerging-picture.md`, `msc/maps/aat-refactored.md` and `msc/maps/asf-audits-and-spikes.md` whole, plus asf `PRACTICA.md`, `JOSEPH-TODO.md` and `audits/STATUS.md`.
- **Tagged** `pre-integration-2026-10-30` in asf (`4ee2b895`) and arch (`9b4be9d`) and pushed both. arch's working tree carried others' uncommitted work (udon submodule, context-saliency notes, vivarium); the tag covers committed state only, and nothing else was touched.
- **Plan** settled with Joseph in plan mode; the plan file is outside the repo at `~/.claude/plans/refactored-sprouting-summit.md`. Phase 0 answers are recorded verbatim in `README.md`. A correction I made to my own first draft, kept here because it's the kind of drift this effort exists to avoid: plan v1 made "every backlog item has a disposition" its headline acceptance test. That was tidiness standing in for truth. Joseph's frame put it right.
- **Goal set by Joseph (verbatim):** "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." What "complete" means in truth-and-clarity terms, not tidiness, gets articulated once the owner review and the two maps land.
- **Launching three peers in parallel:**
  - (A) an Opus influx scout across the drive, writing in `influx-scout/`;
  - (A2) an Opus mapper of the influx surfaces inside asf, writing in `internal-surfaces/`;
  - (B) a Fable highest-level owner review, writing in `owner-review/`.

  Each may spawn its own subagents. All write only in their own dir; the lead commits.
- **Standing notes for this effort** written into `doc/sop/agents.sop.md` (which `CLAUDE.md`/`AGENTS.md`/`GEMINI.md` symlink to), per Joseph. They cover the goal, the frame, lifted gates, push authorization, whole git messages, CHANGELOG-as-log, `memorata-search --no-rerank`, `relata`, web search, and the orchestration protocol.
- **External-research lists** (Joseph: "a list in there somewhere (or several places) that talks about external research that needs to be integrated"). Found so far:
  - `ref/prior-art-analysis/agentic-systems-landscape-2026-08-22.md`. A 46-verdict, source-verified survey written as a letter to Joseph. It names results that belong *in* segments: Richens et al. 2025 (competence implies a world model, the converse of `#form-agent-model`); Baltieri and Suzuki (a do-surgery objection to `#scope-agency`); an H_b definition mismatch with Hafez in `#der-agent-opacity`; the Eslami–Yu delay/dwell budget as a candidate strengthening of `#result-persistence-condition`; Jørgensen–Weichwald–Hammond non-emergence for composites. It also names the computational-mechanics/coalgebra cluster (Baltieri, Virgo, Rosas, Boyd) as the M_t side's living peers. Its follow-ups sit as unattempted `proposed` rows in `spikes/PROPOSED.md`.
  - `ref/enrichment-candidates-2026-05-21.md`.
  - `ref/prior-art-analysis/00-impact-meta-summary.md` and 21 per-topic analyses.
  - `02-tst-core/lit-review/next-research*.md` (TST agendas, April).

  There are probably more. Passed as context to the owner-review and internal-surfaces peers.
