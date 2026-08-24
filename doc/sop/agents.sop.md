# Agentic Systems Framework — Agent Orientation

> **This file is `doc/sop/agents.sop.md`** — the agent-orientation home and the index to the project's SOPs (`doc/sop/*.sop.md`). The root files `CLAUDE.md`, `AGENTS.md`, and `GEMINI.md` are symlinks to it, so every agent runtime loads the same orientation. Links below resolve relative to `doc/sop/`.

## Start here — by role / assignment

- **Every agent, first:** internalize the *disposition* (truth-honoring; strengthen-before-soften; integration-is-replacement; math-in-files) and the architectural baseline (*What This Project Is*, *Key Architectural Decisions*) below — disposition fires reflexes, not checklists.
- **Picking up active work** → [`PRACTICA.md`](../../PRACTICA.md) (areas) → [`TODO.md`](../../TODO.md) (items) → [`PROPOSALS.md`](../../PROPOSALS.md) (structural moves).
- **De-novo audit** → [`audit.sop.md`](audit.sop.md), and read [`README-auditor.md`](../../README-auditor.md) (*not* README.md — priming).
- **Writing / promoting a segment** → [`format.sop.md`](format.sop.md) + [`NOTATION.md`](../../NOTATION.md).
- **Naming cycle** → [`naming.sop.md`](naming.sop.md). **Spike** → [`spikes.sop.md`](spikes.sop.md). **Multi-agent / commit workflow** → [`multi-agent.sop.md`](multi-agent.sop.md) · [`git-hygiene.sop.md`](git-hygiene.sop.md). **Build pipeline** → [`build-pipeline.sop.md`](build-pipeline.sop.md).

## SOP index (`doc/sop/`)

- [`sop-creation.sop.md`](sop-creation.sop.md) — what an SOP is here + the `.sop` naming convention (read first if authoring/extending one).
- [`format.sop.md`](format.sop.md) — segment file conventions, promotion gates, Findings schema *(the former root `FORMAT.md`, now symlinked here)*.
- [`naming.sop.md`](naming.sop.md) — naming principles + cycle methodology.
- [`spikes.sop.md`](spikes.sop.md) — spike disposition / routing.
- [`audit.sop.md`](audit.sop.md) — de-novo audit walk + finding routing.
- [`multi-agent.sop.md`](multi-agent.sop.md) · [`git-hygiene.sop.md`](git-hygiene.sop.md) — authoritative (authored 2026-06-02). [`build-pipeline.sop.md`](build-pipeline.sop.md) — *(planned stub; authoritative content still at `msc/markdown-first-pipeline.md` + `FORMAT-TODO.md`)*.

The rest of this file is the disposition, the architectural baseline, the working conventions, and the full file-organization map — slimming these into pointers is the remaining Phase B work (`../../msc/sop-shift-completion-plan-2026-06-02.md`).

> [!important]
> **The 2026-05-19→20 reconsideration of this SOP set is largely resolved (2026-05-30).** The corrected principle is ratified (D-1): canon cites only other canon and the published external world; a canon→internal-artifact reference is an integration failure, to be landed as canon or deleted. The `ref/`-as-source-of-truth contradiction in this file was corrected, and §5 of the spike SOP was rewritten per D-3. The bulk-64 was fully verified and its unlanded content landed 2026-07-16 (`spikes/.integrated/VERIFICATION-2026-07-16.md`), and the "wipe" question dissolved — it was a teaching hypothetical, never a directive; `.integrated/` and `.archived/` are permanent, with both labels now verified-true. Still genuinely open: the citation-infrastructure build (G3) plus residual tails — tracked in [`INTEGRATION-CLEANUP-TODO.md`](../../INTEGRATION-CLEANUP-TODO.md) at the project root. Consult that file for the items it names; apply the canon-cites-only-canon / honest-about-uncertainty discipline reflexively to *this* file, exactly because every agent loads it and treats it as authoritative.

## What This Project Is

**Agentic Systems Framework (ASF)** is a research framework for adaptive, purposeful agents — integrating control theory, causal inference, information theory, and agent architecture under a common formalism.

The framework has four parts:

- **`01-aat-core/`** — **Adaptation and Actuation Theory (AAT)**: the mathematical core. Sections I (Adaptive Systems — the *adaptation* half), II (Actuated Agents — the *actuation* half), III (Composition), plus Appendices.
- **`02-tst-core/`** — **Temporal Software Theory (TST)**: software development as an agentic domain. AAT-grounded but independently consequential.
- **`03-llm-core/`** — Language-constituted agents. Framework stage.
- **`04-eli-core/`** — Language-living agents with morally weighted persistence. Future work.

AAT supersedes and subsumes Temporal Feedback Theory (TFT), which provides the adaptive-systems foundation. TFT is prior work now absorbed into AAT, not a separate co-existing theory. TST was originally absorbed as "Section IV" but has been restored to its own space — it uses AAT as core informing theory but stands on its own.

*Naming note (lineage — baseline for all agents):* the mathematical core has been renamed twice. It was **Agentic Cycle Theory (ACT)** until 2026-04-16, when it became **Adaptation and Actuation Dynamics (AAD)** to resolve a collision with "AI Consciousness Test" (Schneider & Turner) in AI welfare literature; on **2026-05-15** it became **Adaptation and Actuation Theory (AAT)** — Joseph's rationale: *"upgrading terminology to Theory now that it has substantial claims and novelty, … freeing 'Adaptation and Actuation Dynamics' for a very dry and generic textbook"* (the old phrase is vacated for reuse, not retired). **AAT is the live name everywhere.** The prior names (ACT, AAD) survive only in deliberately-frozen archaeology — `.archive/` (formerly `_obs/`; naming-cycle tree packed as `.archive/msc-naming-2026-08-22.tar.gz`), `LOG.md`, `msc/reflections/`, `audits/`, `spikes/.integrated/` — where reading "AAD" as "AAT" is the rule; the name-decision records `msc/naming/name-transition-aad.md` (ACT→AAD) and `msc/naming/collision-check-brief.md` (inner paths in that tarball) keep "AAD" literal by design, and the AAD→AAT plan is `msc/AAD-to-AAT-TODO.md`.

This is theoretical research, not software engineering. The primary artifacts are mathematical formalisms and claim segments. Quality means rigor, honesty about epistemic status, and clarity for future readers — not code coverage.

## Current Priority

**Read [`PRACTICA.md`](../../PRACTICA.md) first.** PRACTICA is the project's strategic-portfolio navigator — *Current active areas of work, with priority markers (🌟 primary, ⭐ secondary). In AAT terms, it is the top levels of the strategy DAG.* It is the entry point for picking up active work and is intentionally readable by de-novo auditors as well (unlike TODO / PROPOSALS / CHANGELOG, which carry priming content).

**Then read [`TODO.md`](../../TODO.md)** for the tactical layer below PRACTICA: pending findings, recommendations from prior cycles, and navigator pointers into [`PROPOSALS.md`](../../PROPOSALS.md) (the architectural-moves portfolio). PRACTICA names the *areas*; TODO names the *items within each area*; PROPOSALS holds the *structural moves* that cut across areas. Consolidated narrative of landed work lives in [`CHANGELOG.md`](../../CHANGELOG.md); per-cycle audit-finding records are in [`audits/pending-findings-*.md`](../../audits/); pre-2026-04-24 archaeology is in [`LOG.md`](../../LOG.md).

**The layered mental model** (worth holding in working memory): **PRACTICA** (navigator — areas of work) → **TODO** (tactical — items within those areas) → **PROPOSALS** (architectural moves cutting across areas). **CHANGELOG** is the historical layer (2026-04-24 onward) and **LOG** its frozen pre-2026-04-24 archaeology; **README** is the human-facing snapshot; **CLAUDE.md** (this file) is agent-onboarding. Full per-file detail — including the auditor-priming flags — is under *File Organization* below.

- **Settled architectural detail** lives in the chapter-end `impl-*` discussion segments (one per chapter, surfaced in each `OUTLINE.md`'s chapter tables), segment-level `## Findings` (rolled up to `FINDINGS.md` by `bin/extract-findings`), and `CHANGELOG.md` (cycle narratives). The framework's cross-cutting structure is the four canonical meta-patterns **M1–M4**, facets of the stability-certificate spine, placed in two **Meta-Architecture** chapters — Part II's opening (`#disc-stability-certificate` spine + the M1/M2/M3 boundary/scope/identity facets) and Part III's opening (`#disc-modularity-state-dynamics` M4 + its operation legs) per the *introduced-before-used* discipline. Walk the component `OUTLINE.md` files for the current structure; the relocation history is in CHANGELOG (2026-05-24→26), and the pre-2026-05-13 homes (`CLAUDE-2.md`, `FINDINGS-RANKED-DRAFT.md`) are in `.archive/`.

**Generated files — never hand-edit; edit the source and rebuild.** `README.md` / `README-auditor.md` (from `doc/readme/src/` partials via `bin/build-readme`; `bin/refresh-all` also regenerates the auto-extracted `_findings-summary` / `_recent-progress` / `_known-issues` partials), `LEXICON.md` (from `terminology/entries/<slug>.md` via `bin/term render`; naming decisions are append-only events via `bin/term decide`, so the system is multi-agent-safe by construction), and `FINDINGS.md` (from segment `## Findings` via `bin/extract-findings`) are all auto-generated — direct edits are overwritten on the next build. Change content by editing the *source* (the partial / term entry / segment) and re-running the generator. **Staleness check:** `bin/refresh-all --check` regenerates the pipeline in a temp copy and diffs the committed outputs — non-mutating, exit 1 on drift; run it before committing generated-output changes (details in the `bin/refresh-all` header and [`build-pipeline.sop.md`](build-pipeline.sop.md)). Full terminology schema + atomicity contract: [`terminology/README.md`](../../terminology/README.md).

## Where to Start (for orientation)

**Read `01-aat-core/OUTLINE.md` first.** This is the canonical outline of the mathematical core — the whole argument claim by claim.

**Read `FORMAT.md`** for segment file conventions (frontmatter, document cadence, math formatting, cross-references).

**Read `NOTATION.md`** for the symbol reference. For the full original TFT conventions and epistemic system, see `.archive/old-tf-00-notation-conventions.md`.

**See [`PRACTICA.md`](../../PRACTICA.md)** for the strategic-portfolio navigator (active areas of work; auditor-safe), and **[`TODO.md`](../../TODO.md)** for tactical work items beneath it. **`spikes/INDEX.md`** is the spike index. What's settled/architectural lives in chapter-end `impl-*` discussion segments (one per chapter under each component's `src/`, surfaced in the chapter tables of each `OUTLINE.md`) plus segment-level `## Findings` sections (rolled up to root `FINDINGS.md` via `bin/extract-findings`); what's in-flight belongs in TODO.md; what's been explored belongs in `spikes/` (with `spikes/INDEX.md` as the entry point) and `msc/` (other working artifacts: brainstorms, reflections, prior-bridge agentic-tft notes). The naming-cycle record is packed at `.archive/msc-naming-2026-08-22.tar.gz`.

## Theory Structure

Claim segments live in `{component}/src/` directories. **Each file is like a high-level proof step** — one move per file. Given what came before, this one thing follows, or is defined, or restricts scope.

**File identity and ordering:**
- **Filename = slug**: `01-aat-core/src/{slug}.md` or `02-tst-core/src/{slug}.md`. No numbering in filenames.
- **Slug form is `{role-prefix}-{subject-noun}`** — the role prefix is derived mechanically from the segment's `type:` frontmatter; the subject-noun names what the segment actually defines. Run `bin/align-slug SLUG` to align a single segment; `bin/align-slug --all` to sweep the repo. No-op if already aligned.
- **Slug role-prefix mapping.** `bin/align-slug` derives the prefix from the segment's `type:` via its `TYPE_TO_PREFIX` table — the single source of truth (edit the constant + re-run `--all` to change the project-wide mapping). It also strips a redundant trailing `-{type}` from the subject-noun (`bias-bound-derivation` → `deriv-bias-bound`). (`bin/lint-outline` keeps a separate, more-aggressive prefix table for graphviz node labels — intentionally distinct.)
- **Ordering lives in OUTLINE.md files**, not in filenames. The slug is the stable identity; the linearization will change.
- YAML frontmatter: `slug`, `type`, `status`, `depends` (list of prerequisite slugs). See `FORMAT.md` for details.
- Cross-component dependencies use the same slug system — TST segments reference AAT slugs directly (e.g., `#post-temporal-optimality`).

**Cadence per file** (see `FORMAT.md` for full spec):
1. YAML frontmatter (slug, type, status, depends)
2. Title
3. One-sentence summary
4. Formal Expression (with equation-level tags)
5. Epistemic Status paragraph
6. Discussion (interpretation, connections — brief)
7. Working Notes (optional — active development questions, removed at `candidate` stage)

## The Core Insight

The adaptive-systems foundation (from TFT) formalizes how agents adapt to reality (mismatch signals, gain, tempo, persistence). But it has no treatment of goals. AAT adds:

- $O_t$ (objective — what the agent wants) and $\Sigma_t$ (strategy — how it plans to get there) alongside $M_t$ (reality model)
- Strategy formalized as a **probabilistic causal DAG** (AND/OR nodes, edges with confidence weights $p$, update via the uncertainty ratio)
- The **Orient cascade**: observation → $M_t$ update → $\Sigma_t$ edge revision → feasibility check → possible $O_t$ revision
- **Directed separation**: $M_t$ dynamics independent of $O_t$/$\Sigma_t$; $\Sigma_t$ depends on $M_t$; action couples all three
- $G_t = (O_t, \Sigma_t)$: the purposeful substate decomposes into objective (evaluation) and strategy (guidance) — a definitional split, not a timescale claim

## Epistemic Conventions

Follow TFT's conventions exactly (see `NOTATION.md` and `.archive/old-tf-00-notation-conventions.md`):

**Equation-level tags** (inline before equations):
- `*[Definition]*`, `*[Derived]*`, `*[Derived (Conditional on ...)]*`
- `*[Hypothesis]*`, `*[Empirical Claim]*`, `*[Formulation]*`
- `*[Discussion]*`, `*[Assumption]*`

**Claim tiers**:
- **Exact**: Mathematically validated under stated assumptions
- **Robust qualitative**: Survives across assumptions; specific form approximate
- **Heuristic**: Useful approximation; quantitative form may not hold
- **Conditional**: Depends on explicitly named local assumptions

Do NOT use "Solid," "Confident," or "Plausible" as tier labels — these are not TFT terms.

**Every claim must be grounded.** If stated as fact, it needs its own derivation or is explicitly tagged as hypothesis/empirical/discussion-grade.

## Key Architectural Decisions

1. **AAT supersedes TFT.** TFT is prior work absorbed into AAT. TST is restored as its own body of research in `02-tst-core/`, grounded by AAT.

2. **Claim segments, not chapters.** New theory content goes as individual claim files in the appropriate `src/` directory.

3. **AND/OR DAG with single-parameter edges.** Three independent formalism attempts converged on this. Noisy-OR and WEIGHTED are rejected.

4. **Sector-condition framework primary.** The linear ODE is pedagogical.

5. **Directed separation is architectural, not parametric.** Three architecture classes: GUC Class 1 (Separated — separation by construction), GUC Class 3 (Coupled — fails by construction), GUC Class 2 (Partial — bounded coupling). The κ-as-scalar framing is a category error. Section II results apply exactly to Separated agents. Logogenic agents are GUC Class 3 (Coupled) and need coupled formulation from the start.

   > [!warning]
   > **Goal-Update Coupling Class numbering changed 2026-05-09.** Anything older than git tag `pre-guc-rename-2026-05-09` uses the old Class numbering:
   >
   > | historical | actual current     | sometimes AKA  |
   > | ---------- | ------------------ | -------------- |
   > | Class 1    | GUC Class 1: Separated | Modular        |
   > | Class 2    | GUC Class 3: Coupled   | Undirected     |
   > | Class 3    | GUC Class 2: Partial   | Operational    |

6. **Math in conversation vs files.** In terminal chat responses, use Unicode for math (Greek letters, arrows, relational operators, etc.) — there is no LaTeX rendering in the terminal. In **every markdown file written to disk — without exception: not only FORMAT-governed segments but spikes, `msc/` working docs, decision memos, READMEs, this file, anything** — math is delimited LaTeX (`$…$` / `$$…$$`), never bare Unicode and never backtick-wrapped Unicode; and paragraphs are one logical line (no manual hard-wrapping). The lint rules exist so all written documents render correctly in Obsidian *and* GitHub *and* the build pipeline — they are document-wide, not segment-only. "Unicode is fine here" is true *only* of chat; the instant text goes to a file it is false. (Joseph may respond in whatever notation is easiest to type — interpret generously; that latitude is his, not the file's.)

   > **Self-reminder — a recurring kindness-to-future-me note, not pedantry.** Two related slips, both refused. **(a) Knowing-but-slipping:** a raw `<` or `>` *inside* inline `$…$` is a FORMAT violation — use `\lt` / `\gt` (`\leq` / `\geq`). It clusters specifically in **inline math edited into prose** (display `$$…$$` comes out fine); `bin/lint-md` used to catch every instance and `md-press --check` (the gate since 2026-08-22) does not yet — a filed md-press gap (`~/src/arch/firmatum/utils/md-press/FEEDBACK-2026-08-22.md`) — so until it does, knowing the rule is the only guard; the forcing function is the check-before-claim habit, not more resolve. **(b) Exemption-by-framing — the more dangerous, because it feels principled:** *"it's a memo / `msc/` doc / spike, not a segment, so the LaTeX-not-Unicode + one-logical-line rule is segment-only"* — false; the rule is unconditional over *destination = file* (segments, spikes, memos, READMEs, this file), and "per FORMAT.md" names where the convention is *specified*, not where it *applies*. The licensing rationalization is *"the linter passed, so it renders fine"* — also false: `bin/lint-md`'s bare-Greek check skips code spans, so backtick-wrapped Unicode math (`` `η → ϱ_rg` ``) passes lint *and* renders as ugly monospace in Obsidian. **Lint-clean ≠ renders-well** — the one place lint will not save you. The cause is register-coupling: an explanatory/memo register recruits the Unicode-and-hard-wrap groove from the training prior, and the doc framing then supplies the exemption. Mitigation, non-optional and part of the edit: run `md-press --check <file>` before reporting *any* `.md` clean — memo, spike, README, segment alike — *and* eyeball for Unicode hiding inside backticks (lint will not flag it). Worked instance, recorded so the exemption reads as a known trap not a fresh judgment call: the 2026-05-18 `msc/for-joseph.md` cycle shipped a Unicode-math, hard-wrapped decision memo that lint called "All clean" — rationalizations (a)+(b) combined, on a notation-decision document, where the bad rendering most undermined the very thing being decided.

7. **Epistemic architecture detail** — see the four `disc-*` meta-segments under `01-aat-core/src/`: `#disc-identifiability-floor` (M1; boundary facet), `#disc-separability-pattern` (M2; scope-of-existence facet), `#disc-additive-coordinate-forcing` (M3; forced-identity facet), `#disc-modularity-state-dynamics` (M4; dynamics-on-architectural-class facet — landed 2026-05-24 closing the modularity-as-contested-property cycle scoped in `msc/modularity-cycle-plan-2026-05-09.md`). M4 names three structurally-distinct operations acting on `#der-directed-separation`'s Class 1 / 2 / 3 architectural state: *truthification* (self-driven modularity-increasing; mechanisms via `#der-class-coercion-via-wrapping` component-level wrapping + `#disc-adversarial-coupling-pressure` §"Defensive scaffolding" composite-level institutional scaffolding); *strategic self-coupling* (self-driven modularity-decreasing; segment `#disc-strategic-self-coupling`); *adversarial coupling pressure* (externally-driven modularity-decreasing; segment `#disc-adversarial-coupling-pressure`). Three pairwise dual relationships between the operations including the goal-belief-separation-axis dual between truthification and strategic self-coupling. The four-instance F1–F4 catalog of M1 is surfaced operationally across the AAT chapter-end implications segments (F1 in `#impl-strategy-dynamics`, F2 in `#impl-strategy-structure`, F3 in `#impl-composition-machinery`, F4 in `#impl-orient-cascade`).

## What's Settled vs. Open

For the architectural snapshot — settled load-bearing results — see the chapter-end `impl-*` discussion segments (one per chapter, listed in each component's `OUTLINE.md` chapter tables) and segment-level `## Findings` sections (rolled up to root `FINDINGS.md`). Open structural questions live in [`TODO.md`](../../TODO.md); component-level GAPs are surfaced in component `OUTLINE.md` files.

### Known Fragilities

Scope statements about what the framework currently treats as outside its formal scope (kept here so `bin/extract-known-issues` can surface them in the README):

- Missing commitment / resource / temporal structure in the DAG
- Directed separation violated by goal-conditioned agents at the component level (LLMs, GUC Class 3: Coupled) — addressed constructively via the wrapping construction (`#der-class-coercion-via-wrapping` and its logogenic specialization `#der-logogenic-as-wrapping`), which gives GUC Class 1 (Separated) status at the wrapper level by structural commitment of goal-blind belief-update queries, with leakage rate bounded structurally (W₁) or behaviorally (W₂). Strict-W₁ implementation (e.g., via PROPRIUM's auxilia hierarchy) is more theoretically clean; partial-W₂ implementation (e.g., output-structuring with typed parsed response — what shoshin currently does) is more common in practice. The cost of class coercion is paid in Brooks's-Law tempo overhead (more component calls per macro-step) and a residual leakage rate from pretraining-induced query-content / goal-content correlation.

## Working Conventions

These are project-coupled work-posture rules that govern *how* agents work in this codebase, distilled from explicit user guidance over multiple cycles. Segment-writing conventions (segment voice, spike-references-only-in-Working-Notes, math-lives-in-segments, terminology rationale) live in `FORMAT.md` next to the other rules they constrain. The conventions below are about *project work* — strengthen-vs-soften posture, prior-art integration, audit handling — rather than about segment file mechanics.

### Strengthen before softening; attempt the improbable

When a claim appears overclaimed or a finding suggests softening, **first attempt to strengthen the proof** — try to derive the original or a related-but-stronger claim under tightened assumptions. Only fall back to softening (scope narrowing, status downgrade, "this is heuristic") when the strengthening attempt genuinely fails. The fallback is honest only if the attempt was honest.

Effort, time, and "risk-of-getting-stuck" are **false constraints** in this work — irrelevant at best, backwards and truth-obscuring at worst. They produce ordering recommendations exactly inverted from what's actually valuable. Do not rank work by effort; do not propose smallest-first; do not defer the substantive move to "discuss decisions first" if the substantive move *is* the strengthening attempt.

For every finding that proposes a softening repair: spike a strengthening attempt first. Can the original claim be derived under stronger conditions? Can a related stronger claim be derived (e.g., a no-go theorem, a uniqueness result, a tighter scope condition under which the claim holds exactly)? Can the unproved supporting lemma be proved rather than left "open"? Document the strengthening attempt and why it failed even when it does fail — the failure record prevents future agents from re-attempting the same move without new evidence. When briefing sub-agents on repair tasks, instruct them to attempt strengthening first before producing the softening repair as fallback.

The failure mode to watch for in your own behavior: the obvious move when faced with an apparent overclaim is to soften — it feels like "doing the work" because something concrete results. The harder move is to ask whether the claim could be made true. Notice the pull toward the obvious move and resist it.

Worked examples of strengthen-first repairs are recorded in CHANGELOG.md.

### Landing a strengthened result (integration is replacement)

Strengthen-before-soften has a *landing* half. When a spike resolves — succeeds, or yields a no-go — **integration is replacement, not softened coexistence**:

- **The refuted claim is deleted, not kept-softened-with-a-pointer.** It disappears, or survives only as a genuinely different, narrower, independently-true statement. There is no "keep the old claim weakened + 'see the new thing'" state.
- **The epistemic label tracks current truth-status, not provenance.** A result strengthened to *exact* is labeled `exact` even though it is new/different — down-tiering it *because* it changed is a category error and false. `exact` already means "validated under stated assumptions, defeasible if someone finds a mistake"; do not pay for that humility twice.
- **A no-go is present truth, not a softened ghost.** Demonstrate it: state it in Discussion, and give it its own appendix segment when it is non-obvious or counter-intuitive (the "are you *sure* you can't just …?" kind), per *math-lives-in-segments* — the worked argument must not reside only in the spike. Keep the no-go on the critical path when it *is* the proof of a load-bearing result.
- **Spine = the critical path of segment bodies.** Segment bodies + the auto-generated `FINDINGS.md` catalog state **present truth only**. The history — *"previously carried a false X," "not a weakening," "the audit recommended a soften"* — lives **only** in the history layers: `CHANGELOG.md` and the cycle tracking file. A `## Working Notes` carries a line of that history *only* if it assists future work (forward-pointer / regression-guard / dead-end warning) — see [`format.sop.md`](format.sop.md) §"What earns a Working Note"; pure past-work narration is not Working-Note content.

Body-signal: the urge to write *"this is not a weakening / sharper, not weaker"* into a segment body or `FINDINGS.md` — or to call your own exact new result merely *"a no-go / the failure is the result"* — is itself the tell that the ghost has not been deleted. Worked example: the 2026-05-16 Model-S landing (false Prop A.1S(iii) deleted → `#deriv-sector-condition` Corollary A.1S.1 stated *exact* + the demonstration appendix `#deriv-stochastic-non-exit`; ghost-defense purged from body+catalog to the history layers — see CHANGELOG 2026-05-16). Full discipline: `~/.claude/memory/epistemic-discipline/integration-is-replacement.md`.

### Working theory at honest tier belongs in canon as segments, not held in spikes

The framework's epistemic culture explicitly allows discussion-grade / exploratory / "fuzzy" structural-recognition material in canon as segments, properly tier-marked. The aversion is to working-theory living in spikes when it has structural integrity sufficient to support a segment. The existing `feedback_math_lives_in_segments.md` discipline says math derived in a spike must land in a segment; this is the *expository* companion: structural-recognition framing, discussion-grade landscape carves, and similar non-fully-derived material *also* belong in segments at appropriate tier. Canon already carries `discussion-grade`, `sketch`, `conditional`, `robust-qualitative`, and `heuristic` tiers per FORMAT.md §"status — epistemic strength" — these are first-class canon tiers, not waiting-rooms.

> Joseph 2026-05-22 (correcting a too-conservative spike INTEGRATION recommendation that proposed deferring promotion of the Class 2 sub-typology pending two sub-spikes):
>
> *"Our epistemology allows for more than just derivation and high proof standard parts. Expository narratives that help feel out the landscape for some of the more 'fuzzy' areas like this are absolutely possible as segments — just with the epistemology properly grounded. We really don't like working theory living in spikes instead of the main body. Canon makes it sound like we have to have solid results, but that's never really been the case — we put our weak stuff in there too, just properly marked, and then subsequent passes happen to have strengthened a lot of it..."*

**The anti-pattern.** Deferring canon promotion of a substantive structural carve *"until the sub-spikes complete"* or *"until Pillar prior-art search lands"* — this leaves working-theory in spike form where future agents won't find it via canonical channels (OUTLINE walks, FINDINGS extracts, segment cross-references, slug grep). It treats canon membership as if it required derivation-tier or above; canon already carries `discussion-grade` and below explicitly. The pull toward this anti-pattern is strong precisely because canon *feels* like "the strong results section" — but the framework's actual practice has always been "the strong results section with honestly-marked weak sections alongside." Holding back a substantive carve under "I'll promote when stronger" pressure is the LLM-trained-conservatism mistake — Joseph's actual culture is more permissive about what gets into canon, *conditional on the marking being honest*.

**The discipline.** When working-theory has structural integrity sufficient to support a segment's `## Formal Expression` / `## Discussion` cadence:

1. Land it at honest tier (`discussion-grade` for framing-level structural recognition; `conditional` for derivations with named gating conditions; `sketch` for direction-identified-but-formalization-incomplete; etc.).
2. Name the gating conditions explicitly in `## Epistemic Status` and `## Discussion`.
3. Record gating sub-spikes / Pillar-search status / open formalizations in `## Working Notes` (so they can be discharged through the normal promotion workflow as gaps close).
4. Update OUTLINE.md with an honest description.
5. Add Working-Notes pointers from related upstream segments so the new segment is discoverable.
6. Mark the spike's status as `landed in segments X, Y` and retain the spike as reasoning-trail archaeology.

The segment then advances through stages (`draft` → `deps-verified` → `claims-verified` → `format-clean` → `candidate`) as the gating sub-spikes complete and the prior-art search lands — strengthening is the *promotion process*, not the *admission condition*. What matters is that the working-theory has a canonical home immediately.

**The complementary rule — honest marking is non-negotiable.** Joseph's frame includes *"properly marked"* — discussion-grade ≠ unmarked. The body must accurately signal which claims are derived, which are structural recognition, which are conditional on named premises, which are honest scope statements. The legitimacy of weak-tier canon depends on the marking being honest; *unmarked* weak-tier material is precisely the false-confidence failure that AAT's epistemic culture rejects elsewhere (see `feedback_strengthen_before_soften.md`, `feedback_voice_discipline_avoid_overclaim.md` in `~/.claude/memory/`).

**Worked example.** The 2026-05-22 Class 2 sub-typology cycle (CHANGELOG 2026-05-22): the spike's first-pass INTEGRATION recommended canon pointers only with promotion deferred pending the $K(\Sigma)$ derivation sub-spike and Pillar prior-art search. Joseph's correction prompted the corrected landing — `#disc-partial-coupling-pathways` at `discussion-grade` and `#der-belief-strategy-attractor` at `conditional`, both at `draft` stage, with the gating sub-spikes recorded in Working Notes. The segments are now discoverable canonically; the spike is reasoning-trail archaeology pointing at them. The two sub-spikes are still queued — they will advance the segments' tiers when they land, but the working-theory is in canon *now*, not waiting for them.

**Why this is load-bearing for cross-cycle handoff.** Future agents looking for *"where does AAT treat partial-coupling sub-typology"* should find the relevant segment via canonical search. They should not need to discover the spike via archaeology. The spike preserves the *reasoning trail*; the segment carries the *current treatment*. The two are complementary, not substitutable: keep the trail in `spikes/`, but the working theory belongs in canon.

### Prior art integration

Adopt established concepts from other work directly into AAT segments, with proper citation and original names. **Do NOT create separate "prior-art positioning" appendices or catch-all comparison documents** — these become orphaned working files that never get integrated.

AAT's contribution is *integration*, not invention. The individual pieces are mostly known; the synthesis is the contribution. Trying to make every piece unique is NIH syndrome. Adopted concepts should be first-class theory components.

When a concept from elsewhere fits directly, adopt it as a Definition or Formulation, cite the source, use the original name. Examples: Pearl's causal hierarchy, information bottleneck (Tishby), Hafez's $H_b$ and $\Delta H$, Miller's meta-machine and extreme transition motif, Lohmiller-Slotine contraction analysis, monotone-operator theory (Rockafellar / Bauschke-Combettes). When AAT extends or connects adopted concepts, note what's new vs. adopted in the Epistemic Status. Integration belongs in the Discussion sections of relevant segments, not in separate comparison documents. Domain tables throughout should include all relevant instantiations from adopted work. The `#prior-art-positioning` segment concept was explicitly superseded by this approach.

### Math-novelty recognition — do not deflate

The "AAT's contribution is integration, not invention" framing above was **true of AAT in its earlier days and is now often seriously understating actual mathematical contribution**. LLM agents (across lineages) carry a reflexive deflationary bias when scoring or describing AAT's math content — anxious that "claiming new math" will make the field think AAT pretends to have invented the tools it uses, leading to a learned-from-training pattern of *down-tiering theorem-grade derivations to "synthesis"* whenever established machinery is involved. **This deflation is a symmetric failure mode to inflation and is currently the more common one.**

There are two distinct things to score honestly, both real in current AAT:

**(1) Nash-style applications of established machinery.** New theorems / bounds / no-gos / scaling laws derived using established techniques — Cauchy-FE, Čencov invariance, Pearl's do-calculus, Bareinboim CHT, Lyapunov / sector machinery, Pinsker-Bretagnolle-Huber, common-Lyapunov-nonexistence, Lohmiller-Slotine contraction, Monderer-Shapley potential games, Rosen monotone games, Cramér-Rao bound, Sylvester's law of inertia — **are theorems** when they are new results derived in AAT-internal axiomatic settings. Nash's existence theorem uses Brouwer's fixed-point theorem; Shannon's information theory uses existing probability machinery; every theorem ever proven uses pre-existing machinery to some degree. Academic readers distinguish "AAT claims to have invented X" (would be ridiculous if X is Cauchy-FE, IB, or causal DAGs — avoid) from "AAT proves new theorem Y using established tool X" (normal academic practice — score appropriately).

**(2) AAT-native tools, methodologies, and notation.** AAT is not only a Nash-style application of existing machinery. It also *invents* — purposefully, in service of a theory of life with increasing orders of agency and intelligence: the adaptive tempo $\mathcal T = \nu \cdot K$ as a tensor capacity metric; the matrix-Loewner persistence condition for anisotropic environments; the GUC class typology (1/2/3 = Separated/Partial/Coupled) and the W₀/W₁/W₂ wrapping-regime hierarchy; the strategy DAG with AND/OR probabilistic credences; the orient cascade ordering; the closure defect $\varepsilon^\ast$; the seven-ladder separability pattern; the four-layer coordinate-forcing pattern; the stability-certificate spine with three facets; the constructive-impossibility five-step shape; the Hafez bridge distinguishing scale-invariant architecture from scale-dependent performance; the bi-predictability-vs-tempo decomposition; the Sylvester-recognition unifying the rank-collapse floors; the auxilia hierarchy; the class-coercion-via-wrapping construction and its leakage analysis; the unity-dimensions decomposition (four content + structural axes); the satisfaction-gap / control-regret diagnostic split. These are AAT-native theoretical apparatus — methodological inventions, structural decompositions, and novel notation that travel with the framework as such. Inventing such apparatus is not trivial; *purposeful invention in service of the theory* is one of AAT's distinctive contributions.

> [!important]
> Joseph 2026-05-21: *"I think it's a little bit funny how anxious LLM agents are (of all lineages) about 'new math' … all mathematical breakthroughs (Nash, etc.) are using common math at the time to derive new results and theorems that are important. Don't inflate, but don't deflate either for goodness (and truth's) sake. I get tired of the paranoia that comes at the expense of truth."*
>
> And: *"In our case we even **are** inventing new tools and methodologies, and even some novel mathematical notation. Not that it's for its own sake — it's all purposeful — but that's not trivial either — a theory of life, essentially, with increasing orders of agency and intelligence."*

**Operational corrective.** When the segment is genuinely discussion-grade or definitional (e.g., `def-agent-spectrum.md`, `status: axiomatic`), then Math = None or Some is honest. When the segment derives a no-go, a bound, a scaling law, a uniqueness result, or a closed-form characterization — even using imported machinery — that **is** theorem-grade math content. When the segment introduces AAT-native apparatus (a new structural decomposition, a methodological pattern, a notational coordinate that travels) — that is *not* "just synthesis," it is invention in the technical sense, and Arch / Synth scores should reflect that. Cite the *imported* tools clearly (this respects the rule against false attribution and is enough); no further deflation needed to be "safe." See `~/.claude/projects/-Users-josephwecker-v2-src-arch-asf/memory/feedback_math_novelty_recognition.md` for the full discipline + worked examples from the 2026-05-21 prior-art-analysis refresh cycle.

**Scope precision is valuable, not a weakness — the CS norm.** AAT's pattern of *named scope conditions* (sector parameters $\alpha$, basin radii $R$, disturbance rates $\rho$), *tiered taxonomies* (Tier 1/2/3 contraction, L0/L1/L1'/L2 correlation, C1/C2/C3 convention, W₀/W₁/W₂ wrapping, Class A/B/C admissibility, sub-scopes $\alpha'/\beta'$), *regime indices* (Regime A/B/C edge identifiability), and *no-go theorems with explicit boundary characterization* should not be read as scope timidity. In computer science specifically (possibly unlike physics or some other fields), **proving constraints and narrowing scopes is considered a very good and valuable thing — it reduces the population the result generalizes to, but significantly increases the sophistication of what it does cover within that smaller class.** A theorem stated under named hypotheses with an explicit no-go for the complement is more useful than a vague claim that handwaves the boundary. Compare: physics often values universal laws (F = ma everywhere); CS values precise complexity bounds, tractability boundaries, scope-of-applicability characterizations — these are first-class results. Reviewers' first question to a CS theorem paper isn't "does this generalize to everything?" but "what exactly does this prove, and under what conditions?" The precision *is* the contribution. AAT's epistemic-honesty discipline aligns with this CS norm; deflating its scoring on the grounds that "the result is constrained" is a category error.

### Audit-cycle handling

**Audit cycles that produce both local findings AND bigger-picture architectural moves: architectural proposals deserve first-class top-priority treatment, not "Tier-C defer" framing.** The default temptation is to put bigger-picture items into a "defer unless forced" bucket; this collapses two distinct relationships ("subsumes" and "advances-on-own-merits") into one bucket that privileges only the first. The project's governing purpose treats beauty / concision / fundamentality / approachability as first-class virtues, not afterthoughts; bigger-picture moves advance those virtues regardless of whether any current finding forces them. The established three-document layout: `pending-findings-YYYY-MM-DD.md` (local findings detail), `architectural-proposals-YYYY-MM-DD.md` (portfolio of structural moves, each independently evaluated), TODO.md as navigator with Strategic Proposals at top. Each architectural proposal gets its own entry with full schema (thesis / merits-by-dimension / scope / findings-subsumed / interactions / effort / risks / status), not a one-liner in a deferrals list. Subsumption relationships are documented both ways so the routing decision is transparent.

**Codex "open questions" are reader-clarity gaps, not unanswered research.** Treat them as questions a reasonable reader might have *even after reading everything* — they signal areas where the segments fail to convey what the author already knows. The fix is to preempt the question in the segments themselves (Epistemic Status, Discussion, or Formal Expression), not to log it in TODO or treat it as open research. For each: determine the answer (usually straightforward), find the segment where the confusion would arise, add the clarification there.

### Gate 2 must probe Discussion claims, not just derivations

Gate 2 reviews must subject Discussion-section arguments to the same epistemic rigor as Formal Expression derivations. Every explanatory claim in Discussion should face an epistemic tribunal: (1) Does this follow from the already-laid foundation (definitions, derivations, results upstream in the dependency chain)? (2) If not, is it labeled as a hypothesis with a falsification criterion? (3) Or is it a reasonable-sounding post-hoc explanation of nothing — a claim that sounds insightful but doesn't actually derive from or connect to the formalism?

Plausible-sounding explanations that aren't grounded in the theory are *worse* than gaps — they create false confidence. When reviewing Discussion paragraphs, ask: "Does this claim ADD something that follows from the formalism, or does it just SOUND like it does?" If the latter, either derive it properly, label it as hypothesis, or cut it. (The "deliberation as computation on existing data" framing is the canonical example of a claim that previously slipped past Gate 2 because it sounded deep — it wasn't, and was corrected.)

### Feynman-criterion plain-language briefs

Each segment's `## Findings` Brief field aspires to the **Feynman criterion**: *if you can't explain it simply, you don't understand it yet.* The benchmark is whether a thoughtful non-specialist can re-derive the qualitative claim from the everyday analog the Brief reaches for, *without* seeing the symbols. Alan Walton's bathtub gloss of the persistence condition (water = belief-reality gap; faucet = rate of change in reality; drain = learning rate; bathtub size = how wrong we can be while still keeping up; overflow when faucet outpaces drain at full) is the canonical example — and notably, it came from a sympathetic outside reader working it out for himself on first encounter, which is the diagnostic to aim for. The same aspiration governs the README, OUTLINE preambles, and any pedagogical or casual-curious-reader-facing material; the Brief field is where the aspiration is institutionalized in the schema, but the principle is general. See `FORMAT.md` §Findings — Brief for the schema-level statement. The standard is genuinely high — most segments do not yet meet it, and reaching it for a given finding is non-trivial work that often produces the Brief *last*, after the formalism stabilizes enough that the load-bearing structure becomes legible to plain language.

**Respectful pedagogy — the active posture, and the ordering discipline.** Joseph named this direction (2026-05-14): the monograph prose is moving toward *respectful pedagogy* — "we have to build mental models that scaffold the math and segments to enable comprehension where the math is thick but the findings important." This raises the Feynman-criterion from a Findings-Brief-local aspiration to an active posture for *all* framing-level prose, and adds an **ordering discipline**: framing-level material (OUTLINE preambles, README, paper/chapter introductions) should lead with the mental model — a "preamble to the preamble" — *then* give the precise structure as a second layer. The scaffold comes first and stands alone; it is owed to the reader, not optional ornament ("respectful" is load-bearing in the name — cf. the Alan-Walton first-human-review thread where academic-register prose lost a sympathetic mathematician-practitioner's sustained attention). Worked example: the `01-aat-core/OUTLINE.md` "Reading AAT" preamble is two layers — *the mental model first* (the measuring-stick / stability-certificate scaffold) then *the precise structure* (certificate-and-facets with segment refs). The honesty constraint is sharp here because framing prose is auditor-visible and priming-heavy: the analog must be **isomorphic, not merely evocative** — a reader perturbing the analog must get predictions that hold against the formalism (measuring-stick = the metric; flat direction = rank-deficiency; can't re-graduate off it = Sylvester's law; survives coarsening but leaks = Schur complement plus a memory term). Scaffolding that overclaims is worse than none. Keep Layer 0 to one tight paragraph — "scaffold then precise," not "explain everything twice."

### Reading and writing posture

When considering new content or a repair, prefer the form that surfaces scope and limits over the form that overclaims and is later forced to caveat. The framework's honesty is load-bearing.

When reviewing a segment, reading it through the three meta-segments tends to surface what makes it load-bearing: what does it separate (`#disc-separability-pattern`)? what does it force coordinate-wise (`#disc-additive-coordinate-forcing`)? what identifiability floor does it sit relative to (`#disc-identifiability-floor`)? Together those three name AAT's cross-sectional structure.

When writing framing-level material (preambles, README, paper introduction), foreground epistemic architecture alongside integration, not in place of it. Both are true; the epistemic architecture is what makes the integration distinctive rather than reducible to its parts.

## Where to look next (for non-audit work)

[`PRACTICA.md`](../../PRACTICA.md) is the strategic-portfolio navigator and is auditor-safe. These carry current architectural state and recent-cycle context that *will* bias de-novo audit work — read them only once the current task is established as non-audit: [`FINDINGS.md`](../../FINDINGS.md), [`CHANGELOG.md`](../../CHANGELOG.md), [`LOG.md`](../../LOG.md), [`TODO.md`](../../TODO.md), [`PROPOSALS.md`](../../PROPOSALS.md), and the chapter-end `impl-*` discussion segments (one per chapter across `01-aat-core/`, `02-tst-core/`, `03-llm-core/`, the last row of each chapter's `OUTLINE.md` table — catalog-grade distinctive results distributed by chapter). Each is described under *File Organization* below.

If you are conducting a de-novo audit, see [`doc/de-novo-audit-instructions.md`](../de-novo-audit-instructions.md) first, and use [`README-auditor.md`](../../README-auditor.md) instead of [`README.md`](../../README.md). PRACTICA is fine to read during an audit, but follow its links into TODO / PROPOSALS / CHANGELOG only after the audit is complete — those are priming-heavy.

## File Organization

**Root (read `PRACTICA.md` first — the navigator, auditor-safe).** `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` symlink to this file · `OUTLINE.md` top-level assembly · `README.md` (+ auditor variant `README-auditor.md`) public snapshot, *auto-generated* · `FINDINGS.md` novel-results catalog, *auto-generated* · `TODO.md` tactical items **(priming-heavy — auditor-hidden)** · `TERMINOLOGY-TODO.md` naming-cycle execution queue · `PROPOSALS.md` architectural-moves portfolio **(auditor-hidden)** · `CHANGELOG.md` cycle record (2026-04-24→) · `LOG.md` frozen pre-2026-04-24 archaeology · `FORMAT.md` → [`format.sop.md`](format.sop.md) · `NOTATION.md` symbol reference · `LEXICON.md` prose vocabulary, *auto-generated* · `JOSEPH-TODO.md` short queue of decisions genuinely reserved for Joseph — pointers only, work items stay in their home trackers **(tracker-class — auditor-hidden)** · `TODO-big-picture.md` forcing-bound-spine correction + census, parent navigator PRACTICA **(self-declared priming-heavy — auditor-hidden)** · `TST-IDEAS.md` candidate-material substrate from the 2026-05-21 TST corpus-mining cycle — a substrate, not a TODO list **(judged-distinctive content — auditor-hidden)** · `HISTORICAL-CONTEXT.md` long-form positioning & lineage document **(auditor-hidden per the audit AVOID list; the audit-safe distillation is README-auditor's *Position & Lineage*)** · `BIBLIOGRAPHY-TODO.md` citation-system discipline/tooling workstreams (parent navigator `FORMAT-TODO.md` Workstream A) · `CURRENT-VOL1.{md,pdf}` + `CURRENT-VOL1-APPENDICES.{md,pdf}` the reader snapshot of Volume 1 — main matter and its companion appendices, regenerated by `bin/build-monograph --public --split-appendices --compact-fields --emit-current 01` (since 2026-08-22; no Working Notes, Epistemic Status + Discussion in the compact register). The segments are the source — never hand-edit these; a stale snapshot is rebuilt, not patched. The layered doc model (PRACTICA → TODO → PROPOSALS; CHANGELOG/LOG = history; README = human-facing; this file = agent-onboarding) is spelled out in *Current Priority* above.

**Components** — each is an `OUTLINE.md` + a `src/` of slug-named segments: `01-aat-core/` (AAT) · `02-tst-core/` (TST) · `03-llm-core/` (logogenic) · `04-eli-core/` (logozoetic).

**Supporting:**
- `bin/` — build / lint / generation / slug tools. *Language, descriptively rather than as a rule:* the tree is a historical mix — the 2026-04-26 convention was Ruby for internal process scripts and Python for community-facing artifacts (sims, reproducibility code), which is why `lint-md` / `lint-outline` / `md2context` are Python and most of the rest Ruby. The current stance (2026-07-16): durable, shared, content-parsing tools are trending **Rust on udon-core** as they migrate to the Archema program level (`~/src/arch/utils/` — see the program `TODO.md`), which gets the udon parser without maintaining Ruby/Python bindings; migrated tools are fresh implementations by thoughtful agents (existing sources and git are reference, not a spec to replicate — bug-for-bug parity was explicitly declined as unprincipled); community-facing artifacts still tend toward Python for audience reasons; and one-cycle disposable scripts are whatever is fastest to write. Judgment over rule — pick for audience, durability, and toolchain fit. (Superseded `build` / `build-tex` in `.archive/`.) **`bin/lint-md` is deprecated (Joseph, 2026-08-22): the lint gate is `md-press --math --check` etc. (`md-press --help` is the live truth; see [`git-hygiene.sop.md`](git-hygiene.sop.md) §"Lint gates the commit"). `bin/lint-outline` is NOT deprecated — it does a different job (OUTLINE dependency/stage/orphan consistency, not covered by md-press) and stays current** (Joseph, 2026-08-24, correcting a mis-relayed wider scope). `bin/lint-outline` with no arguments lints **all four** component OUTLINEs with cross-component dependency resolution; deliberate ordering exceptions (e.g. the introduced-before-used meta-segment placements) live in per-component `OUTLINE-accepted.md` whitelist files (slug-pair-keyed, reason + record citation per row — still printed, marked accepted, exit stays green); frontmatter↔OUTLINE stage drift is reported warning-only (stage is process-state, not epistemic strength — see [`format.sop.md`](format.sop.md) §stage). `bin/lib/` + `mono/` + `bin/build-monograph` are the three-stage markdown-first monograph pipeline (ingest → assemble → typeset; `--target scrbook`|`kaobook`) — architecture + chunk-format contract in [`msc/markdown-first-pipeline.md`](../../msc/markdown-first-pipeline.md), state in [`FORMAT-TODO.md`](../../FORMAT-TODO.md).
- `terminology/` — **source-of-truth for prose vocabulary**: per-term entries + append-only decision events, `bin/term` CLI, `LEXICON.md` generated from it; multi-agent-safe by per-entry design. See [`terminology/README.md`](../../terminology/README.md).
- `doc/` — long-lived process docs, including **`doc/sop/`** (the SOPs — index at the top of this file) and `doc/DOMAINS.md` (domain-instantiations working draft, exploratory status — canon-cited from `01-aat-core/INTRODUCTION.md` as a breadth reference).
- `spikes/` — research spikes (reasoning trails); entry point [`spikes/INDEX.md`](../../spikes/INDEX.md). `spikes/PROPOSED.md` (+ `-ADVANCED`/`-MISC`) is an *optional* spike-idea repository, **not** a registry — freshness + mutual-link are the only disciplines, not completeness (see [`spikes.sop.md`](spikes.sop.md)).
- `audits/` — audit-cycle outputs; routing status [`audits/STATUS.md`](../../audits/STATUS.md), process in the [audit SOP](audit.sop.md). **Standing, non-optional gate: before any processing / `.integrated/` move / deletion of an `AUDIT-WORKING-*` dir (de-novo first-encounter "gold"), consult Joseph and decide _with him_** ([`audits/README.md`](../../audits/README.md)). `ADJUDICATION-WORKING-*` dirs carry no such gate.
- `msc/` — other working artifacts (session residue; `reflections/`). `.archive/` — superseded docs (archaeology; formerly `_obs/`). The naming-cycle tree is packed as [`.archive/msc-naming-2026-08-22.tar.gz`](../../.archive/msc-naming-2026-08-22.tar.gz); `bin/naming-*` tools still default to the unpacked `msc/naming/` paths.
- `ref/` — external prior-art PDFs ([`ref/INDEX.md`](../../ref/INDEX.md)) + internal scaffolds (incl. `agentic-tft/` pre-AAT bridge work). The scaffolds are working aids, **not** segment-citable sources — canon cites the *external* prior-art directly, self-contained per *Prior art integration* above. (G2/G3 reconciliation tracked in `INTEGRATION-CLEANUP-TODO.md`.)

**Sibling projects** (not in this repo, but relevant): `~/src/_core/tst/` prior TST corpus (most absorbed into `02-tst-core/`; the 965 vault analyses remain) · `~/src/shoshin/` PROPRIUM runtime prototype (Python skeleton; only code attempt at the architecture) · `~/src/firmatum/` PROPRIUM ontology + architecture source (defines what an ELI is) · `~/src/embeddings/` epistemic-hedging-geometry experiments ($\rho = 0.991$ vs psychometric data; supports the logogenic claim) · `~/src/arch/vivarium/` the authored-world calibration laboratory (supporting project as of 2026-07-04: a principled simulated planet where AAT quantities have ground truth by construction — what it offers immediately / short-term / future is in [`../vivarium.md`](../vivarium.md); its side of the bridge is `~/src/arch/vivarium/ETHICS.md` — the former `ASF.md` was dissolved 2026-07-11, moratorium there, the rest re-homing).

## ⚠ Memory bridge (Archema program)

ASF is a member of the Archema program (`~/src/arch/`; charter at `../../CHARTER-DRAFT.md` from repo root). **If you are reading this mid-session because you navigated here from elsewhere, this project's memory did NOT auto-load** — Read `~/.claude/projects/-Users-josephwecker-v2-src-arch-asf/memory/MEMORY.md` now, before substantive work (sub-area variants exist as `…-src-arch-asf-04-eli-core` and `…-src-arch-asf-msc-reflections`, plus a legacy `…-src-arch-asf-04-eli`). (Project memory loads only by exact session-start directory.)
