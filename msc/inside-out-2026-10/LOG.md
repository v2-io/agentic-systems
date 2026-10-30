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
- **relata state for the survey's key works** (measured 11:50 MDT). relata works from the asf checkout; the library has 2,787 entries, and `relata cited 01-aat-core` resolves segment citations.
  - In relata: `richens-2025-general`, `virgo-2025-good`, `hafez-2026-mathematical`.
  - Absent from relata: Baltieri & Suzuki; Eslami & Yu; Jørgensen, Weichwald & Hammond; Meulemans et al. (embedded AIXI); Miehling et al. 2025 (searched by name, title and arXiv id; only `README.md` mentions it).
  - Segment uptake. Richens is mentioned in `def-agent-spectrum`, `impl-causal-access` and `scope-eli`, but **not** in `form-agent-model`, where the survey says its converse result belongs. Virgo is mentioned only in `def-agent-spectrum` and `scope-eli`, **not** in `der-directed-separation`. So the survey's segment-level recommendations are confirmed unintegrated.
- **Joseph, mid-morning, on subagents** (now in `agents.sop.md`): no "report" anywhere in a subagent's artifact filename; the launcher reads the full document and never acts on the chat summary. Sent the filename correction to all three peers.
- **Decision briefs of 2026-07-15** (`msc/decision-briefs-2026-07-15.md`, read whole). With Joseph's gates lifted, these are this effort's to decide on the merits. One exception: A7, splitting 04-eli-core into a private repo, is a strategic-exposure call that stays his. Decided now: **`core.hooksPath` unset.** It pointed at `~/src/agentic-systems/.git/hooks`, which no longer exists, so every git hook was silently inert. No real hooks existed anywhere, so nothing was lost. The entry is removed from `JOSEPH-TODO.md`. Whether to add a pre-push `bin/refresh-all --check` hook is left for the tooling phase. The rest wait for the owner review, so they're decided in light of what the theory is for: F72, A1, A4, A6, the Findings/naming coupling, SP-30, C5, the orderings, and the names.
- **Queued: F72 independent re-derivation** of `#deriv-strategic-persistence-hard-ceiling` against `spikes/spike-strategic-persistence-hard-ceiling-convention-2026-05-31.md`. The segment itself says it is "owed before any further status elevation." It gets a bare verifier brief, written to `spikes/…-verify-1.md`. The launch was refused at 11:5x MDT because the harness's 20-concurrent-subagent limit was full: the three peers are running their own subagents. It launches when slots free up.
- **~12:05 MDT: `INTENT.md` created as the central actuator** at Joseph's direction. He gave his reason as "the more clear you are on the high-level intent and sub-items … the more things will naturally flow in the right directions and the right things will bubble up." It holds the top intent, five objectives (O1–O5) with key results, what currently feeds each, and a "Who is on what" table. Joseph's rules, now standings in `agents.sop.md`: work that feeds no KR is a red flag, and every agent at any depth, and any successor after compaction, knows its exact KR. The three peers were told their KRs (1.1, 3.1, 3.2), invited to ask mid-run via SendMessage to `main` (the pattern from `~/src/arch/SUBAGENT-INSTRUCTIONS-notes.md`, read whole), and asked to pass their KR to their own subagents.
- **~12:30 MDT: the internal-surfaces map (KR3.2) landed.** The lead read `internal-surfaces/00-cross-surface-map.md` whole; the six per-surface maps are for integrators, to be read per slug when landing.
  - **Re-verified by the lead:** 246 real segments, not 290 (44 legacy `old-*` files under `src/`). About 377 of the commits since 08-24 touch only the glyph study. The Working Notes counts stand (167 + 28 + 21 + 19 = 235 segments; the legacy files carry none).
  - **Adopted:** all eight of its INTENT proposals (see INTENT change notes).
  - **Its O1 material, held as candidates until the owner review lands:**
    - belief and goal, with the cost of separating them;
    - SP-30 and the standpoint gap;
    - the strategy DAG, proven sufficient, not necessary, despite its "uniqueness" slug;
    - the no-go re-carve;
    - Vol 4's spine sitting in Vol 1;
    - no single answer to "what does this volume prove".
  - **Its system finding:** spikes and audits produce verified, ready-to-land work, and the integration stage never runs. "Routed" meant a destination was written down, not that it exists.
  - **Two calls it says stay Joseph's even today.** Both stay with him: the first is personal and private material, the second is wording the plan reserves to his voice.
    - `msc/joseph-working-notes.md` is gitignored, yet canon and the 03/04 OUTLINEs cite it. Commit it, move it, or drop the citations?
    - The honest-activation spike reserves two wording choices for him.
- **~13:00 MDT: `HANDOFF.md` created**, at Joseph's prompting that turnover quality must *improve* with each compaction rather than regress. It carries:
  - a resume order;
  - the lead's read-ledger (whole / partial / relay / not read);
  - every claim in INTENT that the lead has not verified;
  - open threads;
  - system facts learned today;
  - the lead's known hazards.

  It is updated at each checkpoint.
- **The lead's professio, recalibrated with Joseph (~13:00 MDT).** The first version (morning) named the pull toward fast draining as the hardest thing. Joseph named two harder ones, and having watched the last hour, I agree:
  - **Balance.** *Knowing something for real* (reading whole, asking, going deep) has to be balanced against *keeping the intent tree true and well-guided*. The failure I've already shown is adopting peers' chat claims into INTENT faster than I read their documents; labeling them as relayed was honest but is not the same as knowing.
  - **Succession.** The system has to develop so that a successor can fill its gaps without making things up.

  What I commit to:
  - read a peer's documents before building on its claims;
  - keep INTENT a scannable tree rather than an evidence store;
  - keep HANDOFF's read-ledger honest at every checkpoint, especially about my own relays.

  Joseph's word for the whole of it: *"be wise."*
- **First system note**: `system/01-epistemic-machinery-in-place.md`, on the meta layer, hypotheses H-a..H-d.
