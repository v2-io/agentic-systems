# Findings — cluster 04: governing-doc / memory / SOP integrity

*2026-07-07. The integrity of the auto-loaded governing layer: the maximal-blast-radius, minimal-oversight surface. All file states, sizes, dates, and commits verified firsthand; where I relayed a tracking-doc claim I mark it as such.*

## Scope recap

The layer every agent auto-loads and treats as authoritative, plus the substrate it distills from:

- `doc/sop/agents.sop.md` (== `CLAUDE.md` == `AGENTS.md` == `GEMINI.md`, all symlinks — confirmed via `ls -la`) and the rest of `doc/sop/*.sop.md`.
- `INTEGRATION-CLEANUP-TODO.md` §F/§G (the self-diagnosis this slice largely exists to check).
- Project auto-memory: `~/.claude/projects/-Users-josephwecker-v2-src-agentic-systems/memory/` (MEMORY.md + 96 `feedback_*`/`project_*` files).
- Global layer: `~/.claude/CLAUDE.md` (symlink into `~/src/memorata/claude/`) + `~/.claude/memory/`.
- The curator's workshop: `~/src/memorata/memory-curation/`.

---

## (a) De-facto processes actually running

1. **Single onboarding surface via symlink.** `CLAUDE.md`/`AGENTS.md`/`GEMINI.md` are all symlinks to `doc/sop/agents.sop.md` (verified). Every runtime loads the same 51,860-byte file. This is a *real, working* de-facto process and a good one — one edit, all runtimes. It is also precisely why a defect there has maximal blast radius (F6).

2. **`JOSEPH-TODO.md` as decision-routing surface — HEALTHY, and the most important positive finding in this slice.** A curated short-list of calls that are *genuinely* Joseph's, with an explicit earn-your-place convention: irreversible / publication-voice / cross-project blast-radius / "did this actually come from Joseph?". Everything else defaults-and-proceeds. Last touched Jul 2. It currently holds exactly one live genuinely-Joseph item (D-2, the bulk-64 `.integrated/` wipe) plus a "lead will default-and-proceed" section. This *is* the decision-routing mechanism the whole meta-review is trying to build — it exists and works. Its gap is coverage (see (e), (d)).

3. **Auto-generated governing artifacts.** `README.md`/`README-auditor.md` (via `bin/build-readme` + `extract-findings`/`extract-known-issues`/`extract-recent-progress`), `LEXICON.md` (via `bin/term`), `FINDINGS.md` (via `bin/extract-findings`) are generated-not-hand-edited. This pattern is live and healthy — and it is the proven capability that makes the F6/G5 "generate portions of the governing doc" idea concrete rather than speculative (see (e)).

4. **Project auto-memory is actively curated — the healthiest memory layer.** MEMORY.md updated Jul 4 (14,712 bytes); a `MEMORY.md.bak` at 34,696 bytes from Jun 2 shows it was deliberately re-thinned (index-line compaction, the B1-residual option-(c) budget lever). New principle files land as work surfaces them (e.g. `feedback_delegate_weeds_lead_stays_at_synthesis.md`, Jun 1; `project_audit_731548_part1_final.md`, Jul 3). This layer tracks the hot path.

5. **`check-links` gates SOP moves.** The SOP-shift used a symlink-aliasing convention with `bin/check-links` as the integrity gate; commits report "check-links green." De-facto working link-integrity discipline for the governing docs.

---

## (b) Aspirational processes the docs/SOPs intend (but that are not de-facto running)

1. **Periodic human-visible review cadence for the governing doc (G5, item 1) — NOT RUNNING.** INTEGRATION-CLEANUP §F6 diagnoses CLAUDE.md as "the auto-loaded onboarding/governing doc; every agent loads it; every agent treats it as authoritative; Joseph does not routinely review it" and prescribes a "periodic human-visible audit cadence." No such cadence exists. The G5 checklist items are all unchecked. The one hard defect that motivated the diagnosis (the `ref/`-as-source-of-truth line) was fixed as a one-off (G1 first item, 2026-05-30), but the *full audit pass* for other same-class defects (G1 second item) was never done and the *cadence* was never instituted.

2. **Generating portions of the governing doc the way LEXICON/README are (G5, item 2) — OPEN, but now concretely feasible.** Flagged as "an architectural question for Joseph." The tooling pattern it points at already exists and is proven (item (a)3 above). Not decided, not attempted.

3. **The global `~/.claude/memory/` detail-file build — STALLED mid-arc.** The global CLAUDE.md index prescribes ~63 detail files across three clusters; the filesystem shows them unwritten: `methodology/` 0 files (28 planned), `research-xref/` 0 files (25 planned), `references/` 1 file of 10 planned (only `psql-18`). The three *authored* clusters are complete: `joseph/` 6, `epistemic-discipline/` 20, `collaboration/` 16. The global CLAUDE.md's "Detail-file state" banner is *honest* about this ("indexed below but not yet written… the index line *is* the current carrier") and gives a fallback chain — so this is an honestly-flagged aspirational-not-yet-de-facto state, not a hidden defect. But the build-state banner was explicitly designed to be *removed when the files are populated* (per memorata HANDOFF.md), and it is still there, because they never were.

4. **The deferred global/memory WN-narrowing pass — INTENDED, DEFERRED, NOW EFFECTIVELY UNTRACKED.** INTEGRATION-CLEANUP's §"Developing discipline" LANDED-2026-06-02 note explicitly defers "the memory-layer carriers — project `feedback_integration_is_replacement` / `feedback_spike_references_only_in_working_notes` and the global `~/.claude/` layer — inherit the same narrowing there, not here." The sop-shift plan calls it "the only deliberately-deferred slice… out of this project-scoped shift." JOSEPH-TODO says this pass "lives in `TODO.md`." It does **not** — `grep -in "global.*memory|~/.claude|SOP pass|memory pass"` over `TODO.md` (117 KB, Jul 4) returns nothing. So a pass that three separate governing docs point to as "tracked elsewhere" is tracked *nowhere* in the repo trackers. It survives only as prose mentions in the two TODO docs. (See (e).)

5. **Draining Working-Note follow-ups into a real tracker (INTEGRATION-CLEANUP §"Developing discipline" pt 6) — PROPOSED, not instituted.** Joseph named the gap ("there is no process for draining WN follow-ups"); a mechanism was proposed 2026-05-31; no evidence it became a running discipline.

---

## (c) Emergent patterns from git history

1. **The SOP shift was two-phased and the mechanical half is genuinely done; the judgment half is partial.** Commit trail (`git log -- doc/sop/`): `048c852` skeleton → interments (`305c541` naming, `20a82e7` spikes, `038e2ed` format, `05e57f5` audit pair) → `4d5b1be` make agents.sop.md the home + symlinks → `42ac834` B1 orphan SOPs → `f4258a0` B2 WN single-source → `ba35d3b` B3 slim → `5115226` "SOP shift complete." Phase A (interment) is clean and complete. Phase B3 (the "value" slim) was executed as a **-20% trim** (`ba35d3b`: 64,341 → 51,528 bytes, +15/−46 lines), with a deliberate judgment call — visible in the commit message — to *keep* math-novelty / Feynman / prior-art / reading-posture as disposition rather than demote them. That is a defensible call. What was **not** done: (a) the plan's stated B3 target of "roughly halve," and (b) updating agents.sop.md's own line 22, which still reads "slimming these into pointers is the remaining Phase B work." See (d)1 — this is the live inconsistency.

2. **The integration-cleanup arc: honest, self-implicating, and only partly discharged.** INTEGRATION-CLEANUP-TODO's own git trail (`f1e01eb` capture → `aba5763` G1 progress → `56ac93f` G2 cycle-close → `361c258`/`8815345` citation) shows real discharge of the *reference* half (G2 reference-cleanup done `9099e58` 2026-05-30; G3 citation infra wired 2026-06-05) while the *structural* half (G5 cadence, G4 sim/empirical extension, F3 bulk-64) stays open. The document is a model of honest breadcrumb discipline — the writing agent names its own failures — but it is now ~7 weeks old and itself partly stale (many `[x]` items done since), which makes it a partly-stale doc that other docs point readers to "before treating any guideline as binding."

3. **Staleness tracks distance from the working tree, cleanly.** Project auto-memory (in the hot path): Jul 4. agents.sop.md (loaded every session): Jul 4-adjacent edits. The memorata workshop (never in the daily tree): frozen at 2026-05-12, every single file. This is a clean gradient, not random rot — the layers that get touched incidentally stay fresh; the layer that needs a *dedicated pass* stopped the moment the dedicated pass ended.

4. **Commit messages as the real record.** `9842619` "flag memory-thinning as a cross-project decision," `ba35d3b`'s body explaining *why* it kept the disposition sections — the reasoning that isn't in any tracker lives in the commit bodies. Consistent with the orientation note that git history is an under-read primary source here.

---

## (d) Stale / broken / abandoned things, concretely

1. **LIVE INCONSISTENCY (low severity, high symbolism): "WHOLE SHIFT COMPLETE" vs agents.sop.md line 22.** `msc/sop-shift-completion-plan-2026-06-02.md` top banner: "✓ WHOLE SHIFT COMPLETE 2026-06-02. Phase A… + Phase B (B1…, B2…, B3 agents.sop.md slim) all landed." Same file's body, B3 section: "Remaining, after B1/B2 settle the homes: demote the body's procedure *restatements* to pointers. Target: roughly halve the body." agents.sop.md line 22 (live, HEAD): "slimming these into pointers is the remaining Phase B work." The file still carries all seven Working-Conventions procedural subsections (verified `grep`: Strengthen / Landing / Working-theory / Prior-art / **Math-novelty** / **Audit-cycle handling** / **Gate 2** / **Feynman** / Reading-posture, lines 158–265) plus the full File-Organization map. So the completion claim overshoots the file's own self-description. **This is the F6 failure class occurring inside the file that defines F6.** The clean fix is a decision, not surgery: either (i) accept the -20% slim as the intended end-state and update line 22 + the plan to say so, or (ii) finish the demotion to the "roughly halve" target. Genuinely Joseph-or-lead taste (what counts as reflex-firing disposition vs step-by-step procedure).

2. **The "under active reconsideration (2026-05-19→20)" banner (agents.sop.md line 25) — HONEST but stale-reading and routes to a stale doc.** It is *not* contradicted by "SOP shift complete" (different thread — see (f)). Its named example (the `ref/` source-of-truth contradiction) *was* fixed (grep confirms the File-Organization line no longer sanctions `ref/Novelty_defense…` as source-of-truth; only the legitimate terminology source-of-truth line remains). But: (a) it is dated as if hot (7 weeks old); (b) it instructs readers to "Read [INTEGRATION-CLEANUP-TODO] before treating any specific guideline here as binding," and that target is itself now partly stale — a drift-compounding pointer (stale doc routing to stale doc).

3. **memorata memory-curation workshop — ABANDONED mid-arc, ~8 weeks.** Every file frozen 2026-05-12 (`README.md`, `HANDOFF.md`, `_timeline-signals.md` all 2026-05-12 21:36; cluster files earlier same day). HANDOFF.md is an honest in-flight handoff listing what remains: ~63 unwritten detail files, upstream-source fixes flagged-not-landed (the spike-agent-briefing "three-completion-states" phrasing correction never propagated back to `~/src/agentic-systems`, neurips, and the neurips memory), and an entire un-entered next phase (essays, session transcripts, synthese substrate, the segment corpus). This is exactly Joseph's "got somewhere but wasn't done." Not broken — *paused* — but the pause is now long enough that it reads as abandoned, and the global CLAUDE.md's fallback chain silently depends on it as fallback layer 2.

4. **`feedback_spike_references_only_in_working_notes.md` (project memory) — STALE relative to a ratified principle.** INTEGRATION-CLEANUP G1's last item: "Project memory `feedback_spike_references_only_in_working_notes.md` — final pass to match the ratified principle; this session's update has the binary… but still carries some of the *need vs mention* framing latent." The principle was **ratified 2026-05-30** (D-1). The file's mtime is **2026-05-19** — it has not been touched since, so the post-ratification reconciliation never happened. Concrete, verifiable staleness in the auto-loaded memory layer: the file still latently carries the `need vs mention` framing Joseph rejected at root.

5. **Global `~/.claude/memory/` — 63 promised detail files never authored** (see (b)3). `methodology/` and `research-xref/` are entirely empty directories that the global index treats as populated (with an honest fallback banner). The banner that was designed to be temporary is now ~8 weeks permanent.

---

## (e) Decisions genuinely blocked on Joseph

1. **D-2 — the bulk-64 `.integrated/` wipe.** The one item correctly sitting in JOSEPH-TODO. Irreversible-class: discharge the integration debt (per-spike check that load-bearing content reached canon) vs. consciously set it down; plus semantics (rm+commit / git-recoverable vs history-purge), timing, scope (`.integrated/`+`.archived/` only, or also `02-tst-core/simulations/`, `track-b-nonlinear-sims/`, `ref/`). Cross-cluster note: this overlaps the spike/audit-integrity slice; flagging so it is not double-counted.

2. **The agents.sop.md slim end-state ((d)1).** Is the -20% trim the intended end-state (update line 22 + the plan to match), or is the "roughly halve" demotion still owed? This is a taste call about what is disposition (reflex-firing, keep) vs procedure (step-by-step, demote) — the exact judgment the sop-creation SOP flags as needing a thinking agent. One-line context Joseph needs: *"B3 stopped at −20% with a call to keep math-novelty/Feynman/prior-art as disposition; the plan said 'halve' and line 22 still says 'remaining' — ratify the −20% as done, or finish the demotion?"*

3. **G5 — how to keep the maximal-blast-radius file honest going forward.** Two coupled sub-decisions, both Joseph's because they are governance-design: (a) institute a periodic human-visible review cadence for agents.sop.md; (b) whether to *generate* portions of it (the README/LEXICON/`bin/term` tooling makes this feasible now). One-line context: *"the F6 self-diagnosis is 7 weeks old and unactioned; the one hard defect it named was fixed but the cadence/generation mitigation — the actual fix, since it can't rest on agent virtue — was never decided."*

4. **B1-residual — global-memory thinning (three options).** Flagged in JOSEPH-TODO's lineage and the sop-shift plan: (a) gut the project `feedback_*.md` bodies to SOP-pointers; (b) retain bodies + add "authoritative → SOP" banner + tighten MEMORY.md index lines (recommended, lossless); (c) leave, just tighten index lines. Cross-project blast-radius (the global CLAUDE.md treats these as its fallback substrate), so genuinely Joseph's. Note the *budget* lever is index-line length, not body size — (b)/(c) still deliver it, and MEMORY.md was already re-thinned Jul 4, suggesting (c) is de-facto the path taken.

---

## (f) Candidate meta-process definitions (raw material for a MECE hierarchy)

Format: **name** — trigger → steps — *current health*.

1. **Governing-doc integrity review** — trigger: N weeks elapsed, or any edit to agents.sop.md / the SOPs. Steps: audit for canon-cites-only-canon violations, internal contradictions, stale self-references, inherited rationalizations; route defects to fix, taste-calls to JOSEPH-TODO. — *Health: **broken/aspirational.** Prescribed in F6/G5; no cadence exists; the one run (2026-05-19) was reactive, not periodic, and left its own banner+line-22 inconsistency behind.*

2. **Governing-doc generation** — trigger: a governing-doc section is mechanically derivable from a source-of-truth. Steps: identify derivable sections (project map, SOP index, known-fragilities), move them behind a generator, regenerate on build. — *Health: **aspirational**, but feasible-now — the README/LEXICON/FINDINGS generators prove the pattern; unapplied to agents.sop.md.*

3. **Joseph-decision routing** — trigger: an agent hits a call that is irreversible / publication-voice / cross-project / provenance-uncertain. Steps: add a pointer-entry to JOSEPH-TODO (context, not duplication); default-and-proceed on everything else; remove when decided. — *Health: **de-facto, healthy** — the standout working process in this slice. Gap: no mechanism guarantees a deferred item actually reaches a tracker (the global-memory pass claims to live in TODO.md and doesn't).*

4. **Deferred-work tracking / anti-orphaning** — trigger: a cycle defers a slice out of scope. Steps: land the deferred slice as a real tracker entry (TODO/PROPOSALS/JOSEPH-TODO), not a prose aside; the deferring doc holds a pointer. — *Health: **broken** — the global/memory WN-narrowing pass is deferred by three docs and tracked by none; the same anti-pattern the WN-drain proposal (INTEGRATION-CLEANUP pt 6) names, recurring one layer up.*

5. **Memory-layer curation** — trigger: enough new principle-substrate accrues, or a ratified principle supersedes a memory's framing. Steps: distill into project `feedback_*.md`, sync MEMORY.md index, propagate to global layer + workshop. — *Health: **mixed** — project layer de-facto healthy and fresh; the ratification-sync sub-process is broken (feedback_spike_references stale since before its own principle was ratified); the global/workshop layer is stalled/abandoned since 2026-05-12.*

6. **Banner / build-state lifecycle** — trigger: a temporary banner is placed (in-flight state, reconsideration, build-state). Steps: banner names the open state + fallback; banner is *removed* when the state closes. — *Health: **broken** — both the global CLAUDE.md build-state banner (designed removable-on-population, still up ~8 weeks) and the agents.sop.md reconsideration banner (honest but stale-dated, routing to a stale doc) show banners outliving a clean removal trigger. No process owns banner retirement.*

---

## Out-of-scope surfacings (passing back)

- **`02-tst-core/simulations/` — 11 un-integrated `.py` files parked in the component tree since 2026-03-20**, outside the spike discipline entirely (INTEGRATION-CLEANUP F2). Belongs to the spike/audit-integrity slice, but flagging: an entire class of spike-equivalent work is invisible to `spikes/INDEX.md`. Coupled to D-2 scope.
- **Citation/bibliography infrastructure (G3)** landed its architecture 2026-06-05 (relata `emit` → `references.bib`, biblatex wired) but the ASF-side foundational-bibliography port and the 23 publisher-raw `ref/` PDF identifications remain open. Relevant to any publication-track slice.
- **`memorata-search` does not index `claude/` or `memory-curation/`** (per HANDOFF.md `sources.toml skip_dirs`) — so the memory substrate is not semantically searchable by the tool Joseph uses to search everything else. Small, but relevant to any "make the memory legible" work.
- **The upstream spike-agent-briefing phrasing fix** (impoverished "find the fundamental reason no such claim is provable" vs Joseph's richer original) is flagged in the workshop but never propagated to `~/src/agentic-systems` / neurips source files — a small cross-project truth-drift worth landing whenever those files are next touched.
