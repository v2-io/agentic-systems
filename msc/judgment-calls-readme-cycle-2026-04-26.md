# Judgment-call log — doc pipeline cycle, 2026-04-26

Cycle: README refactor + composable doc pipeline + segment-level Findings + CLAUDE.md non-audit pointer block.

This log captures decisions made under autonomy after Joseph dropped off, so he can scan for anything that may warrant a different choice on his return. Nothing here is locked; each item invites reconsideration.

---

## Content / framing

### J-1. The six segments chosen for the Findings pilot

Picked: `#result-persistence-condition`, `#disc-additive-coordinate-forcing`, `#deriv-edge-update-natural-parameter`, `#deriv-bias-bound`, `#deriv-causal-ib-lmi`, `#result-contraction-template`.

Reasoning: aimed to span the catalog's distinctive surfaces (one Section I central inequality; one meta-segment; one update-layer Cauchy-FE instance; one recent conditional-theorem appendix; one recent matrix-form derivation; one Section III generalization). All six carry results that are either headline-novel (persistence condition) or have landed substantive content in recent cycles (the others).

What's missing that might also have warranted a Findings entry: `#der-loop-interventional-access` (feedback loop as Level 2 causal engine — the Pearl-hierarchy connection), `#result-sector-condition-stability` (the underlying Lyapunov result), `#deriv-strategic-composition` (Section III equilibrium-convergence framing), `#deriv-critical-mass-composition` (closed-form critical-mass), `#deriv-detection-latency` (the additive-coordinate-forcing-cascade-into-detection-latency result). These would all be reasonable next sweep targets.

**Worth reconsidering?** The pilot's selection skews toward recent (post-2026-04-22) landings. A Joseph-eye pass might prefer to add or substitute one of the older "convergent choice" results to validate the schema across a wider age range.

### J-2. The Findings schema (Novelty / Impact / For non-specialists)

Schema chosen: three labeled paragraphs, with epistemic tier inline in the Novelty line.

Alternatives considered:
- Novelty / Impact / Caveats / Connections (four fields) — more thorough but redundant with segment Discussion / Working Notes
- Novelty / For non-specialists (two fields) — too thin
- Single-paragraph format — loses the structural separation between "what is the claim" and "why it matters"

**Worth reconsidering?** The "Impact" paragraph in some entries (especially `#deriv-bias-bound`, `#result-contraction-template`) ran long. A future pass might tighten the schema to enforce a length cap, or split Impact into two beats (what it closes / what it unlocks).

### J-3. Tier choices

- `#result-persistence-condition` — *Exact* (segment status: exact; structural persistence is exact under stated assumptions per Prop A.1/A.1S).
- `#disc-additive-coordinate-forcing` — *Robust qualitative* (the segment is discussion-grade at meta-pattern level; individual instances have their own statuses).
- `#deriv-edge-update-natural-parameter` — *Conditional* (uniqueness theorem conditional on evidential-additivity axiom).
- `#deriv-bias-bound` — *Conditional* (theorem under named sub-scopes H1-H3 / H1+H4).
- `#deriv-causal-ib-lmi` — *Conditional* (derived under DARE-stabilizability + linear-Gaussian + steady-state info-form Kalman).
- `#result-contraction-template` — *Conditional* (template generalization conditional on (CT1)–(CT3) being verified per instance).

**Worth reconsidering?** `#disc-additive-coordinate-forcing`'s tier is "Robust qualitative" but the *individual instances* it points to are theorem-grade (Cauchy-FE / Čencov uniqueness). A more honest tier might be "Robust qualitative for the meta-pattern; instances are Conditional Exact."

### J-4. README §4 ("What ASF Is") framing

Lead with epistemic-architecture-as-distinctive-contribution per Bundle 1. Three structural moves named: scope-honesty as architecture; three meta-patterns; software as calibration laboratory. Closes with "the integration *is* the substrate; the epistemic architecture is what makes the integration distinctive."

**Worth reconsidering?** I omitted three of the seven elements from CLAUDE-2 §7's enumeration: agent-identity-as-token-level-commitment, derivation-audit tables, A2' sub-scope partition. They felt segment-level rather than README-level. A different judgment could include any of them.

### J-5. Specific phrasing in "For non-specialists" lines

The "For non-specialists" paragraphs are the most subjective part of each Findings entry. Some choices:
- `#result-persistence-condition`: used the "balance held just barely beneath a tipping point" metaphor to convey qualitative-not-quantitative breakdown.
- `#deriv-causal-ib-lmi`: framed the issue as "blank wall" — directly using the segment's own term.
- `#deriv-edge-update-natural-parameter`: introduced log-odds without prior framing.

**Worth reconsidering?** The non-specialist framings are a tone-and-target-audience question; Joseph's preference for which audiences (naive-curious / undergraduate-numerate / post-doc-other-field) sets the right level may differ from my default.

### J-6. Recent Progress depth

Default in `bin/extract-recent-progress` is `--n=3`. The 2026-04-25 entries are dense (5+ H3 narratives under one H2), so 3 narratives means the surfacing crosses dates only on quieter dates. For the current 2026-04-25 corpus, the 3 surfaced narratives are all from that same date.

**Worth reconsidering?** A different default (5? last-30-days?) would surface more or less. The cycle-narrative size also varies; some narratives are long enough that 3 is plenty, others are terse and 3 surfaces less.

### J-7. Known Issues content choices

The extractor pulls:
- Known Fragilities (currently from CLAUDE-2.md, which is transitional)
- PROPOSALS §B/§C/§D entry titles (full titles, dash-separated style)
- OUTLINE GAP rows from each component

**Worth reconsidering?** The PROPOSALS surfacing might be too much detail for README — 15 entries across §B/§C/§D is a lot. Could trim to §B-only ("Ready now") with §C/§D summarized. The Known Fragilities surfacing reads OK but is an audit-priming concern that I judged falls on the "scope-shape, not finding-prejudgment" side per Joseph's recommendation. He may judge differently.

---

## Structural decisions

### J-8. README.md replaced (not preview-only)

I generated the README from the pipeline and committed the replacement. The prior README's substantive content (full Lexicon, philosophical asides, anecdotal feedback) is preserved in archival partials at `doc/readme/src/_lexicon-full-archive.md` and `doc/readme/src/_anecdotal-feedback-archive.md`. The prior README is also recoverable from git history.

**Worth reconsidering?** A safer approach would have been to leave the prior README in place and write the generated version to `README-NEW.md` for review. I judged the pipeline credible enough (with 6 pilot Findings populating §10) that replacement was honest. If the new README's framing or specific content reads wrong, reverting to the prior is one `git checkout` away.

### J-9. Sunset of `01-aad-core/README.md`

Deleted (per proposal plan + Joseph's reasoning that per-part READMEs aren't natural waypoints). The other component directories (02/03/04) never had READMEs.

**Worth reconsidering?** The deleted file's preamble had some content overlapping with the OUTLINE preamble; nothing was lost. If a future pass wants per-component navigation aids, they should either go in the OUTLINE.md preamble (where they already are) or in a dedicated `INDEX.md` that's clearly indexes-and-not-content.

### J-10. CLAUDE.md "Reading and writing posture" subsection placement

Added as a new subsection under Working Conventions, after "Gate 2 must probe Discussion claims, not just derivations." Contained three paragraphs: scope-honesty preference; three-meta-segment lens; both-integration-and-architecture framing.

**Worth reconsidering?** The placement could equally well be at the start of Working Conventions (since it's a meta-rule about all the others) or as a separate top-level section. Current placement reads it as a peer of the other working conventions.

### J-11. Generated files committed (not gitignored)

`FINDINGS.md`, `_findings-summary.md`, `_recent-progress.md`, `_known-issues.md` are all committed with `<!-- AUTO-GENERATED -->` headers. This means GitHub renders the README correctly out of the box without anyone running the build step.

**Worth reconsidering?** The downside is noisier diffs when the underlying sources change (any CHANGELOG entry triggers a `_recent-progress.md` regeneration; any segment Findings edit triggers a `_findings-summary.md` and `FINDINGS.md` regeneration). The proposal's recommendation was to commit; I followed that. If diff noise becomes a real cost, gitignoring the generated files and adding a CI build step is one option; another is per-PR squash discipline that absorbs the regeneration into the substantive commit.

---

## Tooling decisions

### J-12. Liquid `PartialFileSystem` implementation

Custom file system class resolves `{% include "_name" %}` to `doc/readme/src/_name.md`. Loose validation (no enforcement of underscore-prefix). All partials in one `src/` directory regardless of hand-edited vs auto-generated.

**Worth reconsidering?** A separate `src/generated/` subdirectory could enforce the distinction more visibly. I judged the leading-underscore-plus-header-comment combination sufficient; future me may disagree.

### J-13. `extract-recent-progress` granularity

Surfaces full first paragraph of each H3 narrative, not first sentence. CHANGELOG narratives sometimes lead with a long first paragraph (the 2026-04-25 audit-extraction-batch entry has a single paragraph that includes a colon-then-list of commits). The README surfacing inherits whatever the CHANGELOG author wrote.

**Worth reconsidering?** A length cap (e.g., truncate at 600 chars + "…") would protect against very-long lead paragraphs but loses honesty. The current "what the CHANGELOG actually says" reading is honest at the cost of some unevenness.

### J-14. `extract-known-issues` Known Fragilities source

Looks at CLAUDE.md first, falls back to CLAUDE-2.md. Currently picks up CLAUDE-2.md (the items live there, not in CLAUDE.md). When CLAUDE-2 is sunset, the script's `KNOWN_FRAGILITIES_SOURCES` constant needs updating.

**Worth reconsidering?** A more robust approach would scan a wider set or accept a configurable source. I judged the explicit-source-list approach (with a maintenance comment in the script) better than implicit search.

### J-15. `bin/lint-readme` deferred

The proposal mentioned a `bin/lint-readme` for cross-checking link resolution and slug existence. I didn't write it this session. The `bin/build-readme --check` does drift detection (regenerated vs on-disk), but link-validity isn't checked.

**Worth reconsidering?** Probably should land before we rely heavily on the pipeline. Quick to write; deferred for triage when Joseph returns.

### J-16. Pre-commit hook (Layer 2) not installed

Per execution plan, deferred until friction shows up.

### J-17. CI integration (Layer 3) not addressed

The repo doesn't appear to have CI configured (no `.github/workflows/`). Worth adding `bin/build-readme --check` and `bin/refresh-all` to a minimal CI when the team adds CI.

---

## Process decisions

### J-18. Commit cadence

Six commits at natural boundaries: proposal commit; doc/ migration; doc/readme/ scaffolding; pipeline scripts + auditor README + FINDINGS stub; pilot Findings + regenerated README; CLAUDE.md updates + 01-aad-core/README sunset. Plus the CHANGELOG commit (this work). Each commit has a substantive multi-line message describing what landed and why.

### J-19. The CLAUDE.md commit slip

I composed a commit message describing both the 01-aad-core/README deletion AND CLAUDE.md updates, but only the deletion was staged. Caught immediately, made a follow-up commit. Lesson: `git status` before composing a multi-file commit message; or `git add -A` first when intent is to commit everything pending.

### J-20. Did not push to remote

Per Joseph's instruction. Branch is now ~7 commits ahead of origin/main locally.

### J-21. CLAUDE-2.md sunset deferred *(✓ resolved 2026-04-28, commit `614c2bf`)*

Per the proposal's execution plan: full sunset waits until segment-Findings sweep is far enough along that FINDINGS.md is the credible reference. Currently 6 pilot entries; the sweep is the next major Findings-related cycle.

**Resolution.** The 2026-04-27 catalog merge + Opus brainstorm pass + lower-confidence pull-back brought `msc/FINDINGS-RANKED-DRAFT.md` to ~58 numbered findings + cross-segment + meta-architectural sections — *de facto* the credible "what's settled" reference the proposal's gating condition required. The full segment-level Findings sweep (writing `## Findings` sections in each segment) is still pending and tracked in PRACTICA, but FINDINGS-RANKED-DRAFT is itself now load-bearing enough to host the architectural snapshot CLAUDE-2 used to provide. The 2026-04-28 cycle executed the sunset: CLAUDE-2 moved to `_obs/CLAUDE-2-superseded-2026-04-28.md`; content distributed; `bin/extract-known-issues` updated; live references in CLAUDE.md, TODO.md, and the README partials cleaned up. See CHANGELOG 2026-04-28 entry.

### J-22. Segment-Findings sweep deferred

Six pilot Findings landed hand-drafted. The sweep across remaining qualifying segments was not attempted this session — per the proposal plan, that's a separate cycle that benefits from Joseph's review of the pilot's tone and schema before scaling.

---

## What I deliberately did not touch

- TODO.md (active work items remain as-is; the doc-pipeline cycle's archive entry should land in TODO §Archive on a future cleanup pass)
- PROPOSALS.md (Bundle 1 status — partially addressed by this cycle; an update on which Bundle 1 elements landed and which remain would be a useful follow-up, but I judged it Joseph-decision territory rather than autonomous-execution)
- OUTLINE.md, FORMAT.md (no changes)
- Segment text outside the Findings sections (no edits to formal expressions or discussions)
- LEXICON.md, NOTATION.md (no changes)
- ref/, _obs/ (no changes)
- The msc/proposal-readme-refactor.md beyond the synthesis-prose decision (no further edits to the proposal once committed)

---

## Things that came up but weren't acted on

- **PROPOSALS.md needs a status update** for Bundle 1: the README rewrite is now landed, the OUTLINE preamble already had the auditor-safe reframe, and several other Bundle 1 elements are partially addressed. A "Bundle 1 status" mini-update would be useful housekeeping.
- **TODO.md `## Active — Pending-Review Spikes` cleanup** — several spikes there have landed; archival pass is overdue but out of scope for this cycle.
- **FORMAT.md should document the `## Findings` section** — currently FORMAT.md lists the segment cadence (frontmatter / Title / summary / Formal Expression / Epistemic Status / Discussion / Working Notes); adding Findings as the optional H2 between Discussion and Working Notes is needed before any sweep instructions can refer to FORMAT.md as authoritative.
- **`bin/lint-readme`** — flagged above (J-15). Quick win.
- **The `_obs/CLAUDE-2-superseded-2026-XX-XX.md` placeholder** — when CLAUDE-2 sunsets, the timestamp-stamped archive name needs choosing.
