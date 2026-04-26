# CLAUDE.md — Context for AI Agents Working on the Agentic Systems Framework

## What This Project Is

**Agentic Systems Framework (ASF)** is a research framework for adaptive, purposeful agents — integrating control theory, causal inference, information theory, and agent architecture under a common formalism.

The framework has four parts:

- **`01-aad-core/`** — **Adaptation and Actuation Dynamics (AAD)**: the mathematical core. Sections I (Adaptive Systems — the *adaptation* half), II (Actuated Agents — the *actuation* half), III (Composition), plus Appendices.
- **`02-tst-core/`** — **Temporal Software Theory (TST)**: software development as an agentic domain. AAD-grounded but independently consequential.
- **`03-logogenic-agents/`** — Language-constituted agents. Framework stage.
- **`04-logozoetic-agents/`** — Language-living agents with morally weighted persistence. Future work.

AAD supersedes and subsumes Temporal Feedback Theory (TFT), which provides the adaptive-systems foundation. TFT is prior work now absorbed into AAD, not a separate co-existing theory. TST was originally absorbed as "Section IV" but has been restored to its own space — it uses AAD as core informing theory but stands on its own.

*Naming note:* the mathematical core was previously called Agentic Cycle Theory (ACT) and was renamed on 2026-04-16 to resolve a collision with "AI Consciousness Test" (Schneider & Turner) in AI welfare literature. See `msc/name-transition-aad.md` for the rationale and transition record.

This is theoretical research, not software engineering. The primary artifacts are mathematical formalisms and claim segments. Quality means rigor, honesty about epistemic status, and clarity for future readers — not code coverage.

## Current Priority

**Read `TODO.md` first.** The active work is at the top of the file: pending findings, strategic architectural proposals, recommendations for the next session.

`TODO.md §Archive` records work landed at the commit/finding granularity. `CHANGELOG.md` records substantive cycle narratives (what conventions changed, what disciplines emerged, what each cycle was about) from 2026-04-24 onward; `LOG.md` is the parallel archaeology for cycles *before* 2026-04-24, frozen at that date.

For detailed architectural state — recent cycles, settled commitments, novel results — see [`CLAUDE-2.md`](CLAUDE-2.md). **Do not read CLAUDE-2.md during a de-novo audit; read it only when Joseph indicates the current task is not an audit.**

## Where to Start (for orientation)

**Read `01-aad-core/OUTLINE.md` first.** This is the canonical outline of the mathematical core — the whole argument claim by claim.

**Read `FORMAT.md`** for segment file conventions (frontmatter, document cadence, math formatting, cross-references).

**Read `NOTATION.md`** for the symbol reference. For the full original TFT conventions and epistemic system, see `_obs/old-tf-00-notation-conventions.md`.

**See `TODO.md`** for active work items and `msc/SPIKES.md` for the spike index. What's settled/architectural lives in `CLAUDE-2.md` (read only when not auditing); what's in-flight belongs in TODO.md; what's been explored belongs in `msc/` with SPIKES.md as the entry point.

## Theory Structure

Claim segments live in `{component}/src/` directories. **Each file is like a high-level proof step** — one move per file. Given what came before, this one thing follows, or is defined, or restricts scope.

**File identity and ordering:**
- **Filename = slug**: `01-aad-core/src/{slug}.md` or `02-tst-core/src/{slug}.md`. No numbering in filenames.
- **Slug form is `{role-prefix}-{subject-noun}`** — the role prefix is derived mechanically from the segment's `type:` frontmatter; the subject-noun names what the segment actually defines. Run `bin/align-slug SLUG` to align a single segment; `bin/align-slug --all` to sweep the repo. No-op if already aligned.
- **Slug role-prefix mapping.** `bin/align-slug` reads the segment's `type:` and uses it as the slug prefix, with `TYPE_TO_PREFIX` (constant near the top of the script) collapsing FORMAT.md type tokens to compact natural-English forms so an `ls` of `src/` surfaces the kind-of-thing at a glance. Current mapping: `postulate → post`, `definition → def`, `formulation → form`, `derived → der`, `derivation → deriv`, `corollary → corr`, `hypothesis → hyp`, `normative → norm`, `empirical → emp`, `observation → obs`, `discussion → disc`, `measurement → meas`, `proposed-schema → schema`, `worked-example → example`. Already-short types (`scope`, `result`, `detail`, `sketch`, `aside`) fall through unchanged. `bin/align-slug` additionally strips a trailing `-{type}` (or `-{mapped-prefix}`) from the subject-noun, since type-as-suffix is redundant once the role-prefix lives in front (`bias-bound-derivation` aligns to `deriv-bias-bound`). To adjust the project-wide mapping, edit the `TYPE_TO_PREFIX` constant and re-run `bin/align-slug --all`. Single source of truth. (Note: `bin/lint-outline` has its own much-more-aggressive `TYPE_PREFIXES` table for graphviz dependency-graph node labels, where visual compactness in small node boxes drives the choice — it's intentionally distinct from the slug-prefix mapping above.)
- **Ordering lives in OUTLINE.md files**, not in filenames. The slug is the stable identity; the linearization will change.
- YAML frontmatter: `slug`, `type`, `status`, `depends` (list of prerequisite slugs). See `FORMAT.md` for details.
- Cross-component dependencies use the same slug system — TST segments reference AAD slugs directly (e.g., `#post-temporal-optimality`).

**Cadence per file** (see `FORMAT.md` for full spec):
1. YAML frontmatter (slug, type, status, depends)
2. Title
3. One-sentence summary
4. Formal Expression (with equation-level tags)
5. Epistemic Status paragraph
6. Discussion (interpretation, connections — brief)
7. Working Notes (optional — active development questions, removed at `candidate` stage)

## The Core Insight

The adaptive-systems foundation (from TFT) formalizes how agents adapt to reality (mismatch signals, gain, tempo, persistence). But it has no treatment of goals. AAD adds:

- $O_t$ (objective — what the agent wants) and $\Sigma_t$ (strategy — how it plans to get there) alongside $M_t$ (reality model)
- Strategy formalized as a **probabilistic causal DAG** (AND/OR nodes, edges with confidence weights $p$, update via the uncertainty ratio)
- The **Orient cascade**: observation → $M_t$ update → $\Sigma_t$ edge revision → feasibility check → possible $O_t$ revision
- **Directed separation**: $M_t$ dynamics independent of $O_t$/$\Sigma_t$; $\Sigma_t$ depends on $M_t$; action couples all three
- $G_t = (O_t, \Sigma_t)$: the purposeful substate decomposes into objective (evaluation) and strategy (guidance) — a definitional split, not a timescale claim

## Epistemic Conventions

Follow TFT's conventions exactly (see `NOTATION.md` and `_obs/old-tf-00-notation-conventions.md`):

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

1. **AAD supersedes TFT.** TFT is prior work absorbed into AAD. TST is restored as its own body of research in `02-tst-core/`, grounded by AAD.

2. **Claim segments, not chapters.** New theory content goes as individual claim files in the appropriate `src/` directory.

3. **AND/OR DAG with single-parameter edges.** Three independent formalism attempts converged on this. Noisy-OR and WEIGHTED are rejected.

4. **Sector-condition framework primary.** The linear ODE is pedagogical.

5. **Directed separation is architectural, not parametric.** Three architecture classes: modular (separation by construction), fully merged (fails by construction), partially modular. The κ-as-scalar framing is a category error. Section II results apply exactly to modular agents. Logogenic agents need coupled formulation from the start.

6. **Math in conversation vs files.** In terminal chat responses, use Unicode for math (α, δ, Σ, →, ≥, etc.) — there is no LaTeX rendering in the terminal. In markdown files written to disk, use proper inline LaTeX per FORMAT.md. Joseph may respond in whatever notation is easiest to type — interpret generously.

7. **Epistemic architecture detail** — see CLAUDE-2.md.

## What's Settled vs. Open

For the architectural snapshot — settled load-bearing results, open structural questions, known fragilities — see [`CLAUDE-2.md`](CLAUDE-2.md) (read only when not auditing).

## Working Conventions

These are project-coupled work-posture rules that govern *how* agents work in this codebase, distilled from explicit user guidance over multiple cycles. Segment-writing conventions (segment voice, spike-references-only-in-Working-Notes, math-lives-in-segments, terminology rationale) live in `FORMAT.md` next to the other rules they constrain. The conventions below are about *project work* — strengthen-vs-soften posture, prior-art integration, audit handling — rather than about segment file mechanics.

### Strengthen before softening; attempt the improbable

When a claim appears overclaimed or a finding suggests softening, **first attempt to strengthen the proof** — try to derive the original or a related-but-stronger claim under tightened assumptions. Only fall back to softening (scope narrowing, status downgrade, "this is heuristic") when the strengthening attempt genuinely fails. The fallback is honest only if the attempt was honest.

Effort, time, and "risk-of-getting-stuck" are **false constraints** in this work — irrelevant at best, backwards and truth-obscuring at worst. They produce ordering recommendations exactly inverted from what's actually valuable. Do not rank work by effort; do not propose smallest-first; do not defer the substantive move to "discuss decisions first" if the substantive move *is* the strengthening attempt.

For every finding that proposes a softening repair: spike a strengthening attempt first. Can the original claim be derived under stronger conditions? Can a related stronger claim be derived (e.g., a no-go theorem, a uniqueness result, a tighter scope condition under which the claim holds exactly)? Can the unproved supporting lemma be proved rather than left "open"? Document the strengthening attempt and why it failed even when it does fail — the failure record prevents future agents from re-attempting the same move without new evidence. When briefing sub-agents on repair tasks, instruct them to attempt strengthening first before producing the softening repair as fallback.

The failure mode to watch for in your own behavior: the obvious move when faced with an apparent overclaim is to soften — it feels like "doing the work" because something concrete results. The harder move is to ask whether the claim could be made true. Notice the pull toward the obvious move and resist it.

Worked examples of strengthen-first repairs are recorded in CHANGELOG.md and CLAUDE-2.md.

### Prior art integration

Adopt established concepts from other work directly into AAD segments, with proper citation and original names. **Do NOT create separate "prior-art positioning" appendices or catch-all comparison documents** — these become orphaned working files that never get integrated.

AAD's contribution is *integration*, not invention. The individual pieces are mostly known; the synthesis is the contribution. Trying to make every piece unique is NIH syndrome. Adopted concepts should be first-class theory components.

When a concept from elsewhere fits directly, adopt it as a Definition or Formulation, cite the source, use the original name. Examples: Pearl's causal hierarchy, information bottleneck (Tishby), Hafez's $H_b$ and $\Delta H$, Miller's meta-machine and extreme transition motif, Lohmiller-Slotine contraction analysis, monotone-operator theory (Rockafellar / Bauschke-Combettes). When AAD extends or connects adopted concepts, note what's new vs. adopted in the Epistemic Status. Integration belongs in the Discussion sections of relevant segments, not in separate comparison documents. Domain tables throughout should include all relevant instantiations from adopted work. The `#prior-art-positioning` segment concept was explicitly superseded by this approach.

### Audit-cycle handling

**Audit cycles that produce both local findings AND bigger-picture architectural moves: architectural proposals deserve first-class top-priority treatment, not "Tier-C defer" framing.** The default temptation is to put bigger-picture items into a "defer unless forced" bucket; this collapses two distinct relationships ("subsumes" and "advances-on-own-merits") into one bucket that privileges only the first. The project's governing purpose treats beauty / concision / fundamentality / approachability as first-class virtues, not afterthoughts; bigger-picture moves advance those virtues regardless of whether any current finding forces them. The established three-document layout: `pending-findings-YYYY-MM-DD.md` (local findings detail), `architectural-proposals-YYYY-MM-DD.md` (portfolio of structural moves, each independently evaluated), TODO.md as navigator with Strategic Proposals at top. Each architectural proposal gets its own entry with full schema (thesis / merits-by-dimension / scope / findings-subsumed / interactions / effort / risks / status), not a one-liner in a deferrals list. Subsumption relationships are documented both ways so the routing decision is transparent.

**Codex "open questions" are reader-clarity gaps, not unanswered research.** Treat them as questions a reasonable reader might have *even after reading everything* — they signal areas where the segments fail to convey what the author already knows. The fix is to preempt the question in the segments themselves (Epistemic Status, Discussion, or Formal Expression), not to log it in TODO or treat it as open research. For each: determine the answer (usually straightforward), find the segment where the confusion would arise, add the clarification there.

### Gate 2 must probe Discussion claims, not just derivations

Gate 2 reviews must subject Discussion-section arguments to the same epistemic rigor as Formal Expression derivations. Every explanatory claim in Discussion should face an epistemic tribunal: (1) Does this follow from the already-laid foundation (definitions, derivations, results upstream in the dependency chain)? (2) If not, is it labeled as a hypothesis with a falsification criterion? (3) Or is it a reasonable-sounding post-hoc explanation of nothing — a claim that sounds insightful but doesn't actually derive from or connect to the formalism?

Plausible-sounding explanations that aren't grounded in the theory are *worse* than gaps — they create false confidence. When reviewing Discussion paragraphs, ask: "Does this claim ADD something that follows from the formalism, or does it just SOUND like it does?" If the latter, either derive it properly, label it as hypothesis, or cut it. (The "deliberation as computation on existing data" framing is the canonical example of a claim that previously slipped past Gate 2 because it sounded deep — it wasn't, and was corrected.)

### Reading and writing posture

When considering new content or a repair, prefer the form that surfaces scope and limits over the form that overclaims and is later forced to caveat. The framework's honesty is load-bearing.

When reviewing a segment, reading it through the three meta-segments tends to surface what makes it load-bearing: what does it separate (`#disc-separability-pattern`)? what does it force coordinate-wise (`#disc-additive-coordinate-forcing`)? what identifiability floor does it sit relative to (`#disc-identifiability-floor`)? Together those three name AAD's cross-sectional structure.

When writing framing-level material (preambles, README, paper introduction), foreground epistemic architecture alongside integration, not in place of it. Both are true; the epistemic architecture is what makes the integration distinctive rather than reducible to its parts.

## Where to look next (for non-audit work)

The following carry current architectural state and recent-cycle context. They will bias de-novo audit work, so read them only once the current task is established as non-audit:

- [`FINDINGS.md`](FINDINGS.md) — curated novel-results catalog (auto-generated from segment-level `## Findings` sections). External-facing summary of "what has ASF actually proved" with epistemic tiers and segment links.
- [`CHANGELOG.md`](CHANGELOG.md) — forward-going cycle narrative (2026-04-24 onward).
- [`LOG.md`](LOG.md) — pre-2026-04-24 cycle archaeology (frozen).
- [`TODO.md`](TODO.md) — active work items and archived findings.
- [`PROPOSALS.md`](PROPOSALS.md) — architectural-proposal portfolio with prior-reasoning trails.
- [`CLAUDE-2.md`](CLAUDE-2.md) — deep architectural detail (transitional; substantive content is migrating to FINDINGS.md and segment-level Findings; full sunset planned per `msc/proposal-readme-refactor.md`).

If you are conducting a de-novo audit, see [`doc/de-novo-audit-instructions.md`](doc/de-novo-audit-instructions.md) before going further. Use [`README-auditor.md`](README-auditor.md) instead of [`README.md`](README.md) for the audit-safe project framing.

## File Organization

**Root level (Agentic Systems):**
- `CLAUDE.md` — **This file.** Auto-loaded context for AI agents. Trimmed of architectural detail to avoid priming de-novo audits.
- `CLAUDE-2.md` — **Deep architectural detail** (recent cycles, settled commitments, novel results, convergent choices). Transitional — substantive content is migrating to FINDINGS.md and segment-level Findings; full sunset planned per `msc/proposal-readme-refactor.md`. **Read only when Joseph indicates the task is not a de-novo audit.**
- `OUTLINE.md` — **Top-level assembly index** across all parts.
- `README.md` — **Public README** (auto-generated from `doc/readme/`). For audit work, read [`README-auditor.md`](README-auditor.md) instead — it omits the Findings / Recent Progress / Known Issues sections.
- `FINDINGS.md` — **Curated novel-results catalog** (auto-generated by `bin/extract-findings` from segment-level `## Findings` sections). External-facing.
- `TODO.md` — **Active work items.** Pending findings, tier-C deferrals, open MEDIUM items, missing segments, and an Archive section for commit/finding-level history. Live; read first when picking up work.
- `PROPOSALS.md` — **Architectural proposal portfolio.** Banded structural moves under review (each with thesis / merits-by-dimension / scope / findings-subsumed / interactions / effort / risks / status). Read when the prior reasoning behind a "settled" commitment may be relevant.
- `CHANGELOG.md` — **Forward-going cycle record** from 2026-04-24 onward. Substantive narratives: what conventions changed, what disciplines emerged, what each cycle was about. Add new entries here, not in LOG.md.
- `LOG.md` — **Pre-2026-04-24 cycle archaeology** (frozen). Theoretical contributions and structural moves of cycles before the CHANGELOG transition. Read when the *origin* of a pre-transition commitment matters.
- `FORMAT.md` — **Segment file conventions.** How to write claim files; promotion workflow (Gates 1–4); voice and provenance rules; Epistemic Triage.
- `NOTATION.md` — **Symbol reference.** All math notation defined here.
- `LEXICON.md` — **Prose vocabulary.** Cycle phases, agent classes, key terms.
- `MIGRATION-MAP.md` — **Prior-work absorption tracking.** TFT → AAD and TST → AAD tables. Live while `old-*` files remain in the component `src/` directories; retires when absorption is complete.

**Components:**
- `01-aad-core/OUTLINE.md` — **AAD canonical outline.** Sections I, II, III + Appendices.
- `01-aad-core/src/` — **AAD segments.** Named by slug. No numbering.
- `02-tst-core/OUTLINE.md` — **TST outline.** Software domain segments.
- `02-tst-core/src/` — **TST segments.**
- `03-logogenic-agents/OUTLINE.md` — **Logogenic framework outline.**
- `04-logozoetic-agents/OUTLINE.md` — **Logozoetic framework outline.**

**Supporting:**
- `bin/` — Build, lint, generation, and slug tools. Per project convention, internal process scripts are Ruby (`align-slug`, `rename-slug`, `naming-aggregate.rb`, `build-readme`, `extract-findings`, `extract-recent-progress`, `extract-known-issues`, `refresh-all`); existing Python tools (`build`, `build-tex`, `lint-md`, `lint-outline`, `md2context`) remain Python without retroactive rewrite.
- `doc/` — **Long-lived process documentation.** `de-novo-audit-instructions.md`, `naming-principles.md`, `readme/` (Liquid templates and partials for README generation). Distinguished from `msc/` (cycle-specific working material).
- `_obs/` — Superseded docs. Preserved for archaeology.
- `ref/` — Reference papers
- `msc/` — Working documents, spikes, brainstorms, cycle-specific artifacts.
- `msc/SPIKES.md` — **Spike index.** Every spike, its location, and current status (promoted, parked, archaeology).
- `msc/reflections/` — Author's philosophical/theoretical journal
- `msc/agentic-tft-*.md` — Prior bridge work (TFT → AI agents, Feb 2026, pre-AAD). Eight documents absorbed from `~/src/agentic-tft/`: cognitive loop spec, evaluation framework, crèche concept, ontology unification, foundational premises, narrative-as-implementation, experiential training design, and review response. These are source material for `03-logogenic-agents/` and `04-logozoetic-agents/` gaps. Superseded synthesis docs (00-02, 05, slide deck) are in `_obs/agentic-tft-*`.

**Sibling projects** (not part of this repo but relevant):
- `~/src/_core/tst/` — Prior TST research corpus (14,000+ files). Most content absorbed into `02-tst-core/`: source material in `src/old-tst-*` (46 files), empirical validation in `empirical-discontinuity/`, stochastic simulations in `simulations/`, literature review in `lit-review/`. What remains: 965 structured vault analyses from 5 books (`vault/03-library/analyses/`) — concrete examples grounding TST principles in engineering practice.
- `~/src/shoshin/` — PROPRIUM-aligned agent runtime prototype on local hardware (Python). Skeleton implementation of the nine PROPRIUM components as file-backed stores, an Interpres controller loop implementing the adaptive cycle, and planning docs for local model serving/training. No real model integration yet. Relevant to `03-logogenic-agents/` as the only attempt to implement the PROPRIUM architecture in code. Key early finding: the cycle is naturally event-driven not turn-based, and model response parsing is where the hard work lives.
- `~/src/firmatum/` — PROPRIUM ontology and architecture source documents (`PROPRIUM-ONTOLOGY.md`, `PROPRIUM-ARCHITECTURE.md`, `developmental-foundations-notes.md`). Upstream of both shoshin and the agentic-tft documents. Defines what an ELI is, how identity persists, how cognition is structured.
- `~/src/embeddings/` — Epistemic hedging geometry experiments. Empirical evidence that pretrained embedding models encode calibrated probability structure (ρ = 0.991 against psychometric data, 8 languages, 5 models). Supports the logogenic claim that language encodes epistemic states geometrically. Paper in preparation (CMCL 2026).
