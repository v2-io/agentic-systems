# CLAUDE.md — Context for AI Agents Working on Agentic Systems

## What This Project Is

**Agentic Systems** is a research framework for adaptive, purposeful agents — integrating control theory, causal inference, information theory, and agent architecture under a common formalism.

The project has four components:

- **`01-act-core/`** — **Agentic Cycle Theory (ACT)**: the mathematical core. Sections I (Adaptive Systems), II (Actuated Agents), III (Composition), plus Appendices.
- **`02-tst-core/`** — **Temporal Software Theory (TST)**: software development as an agentic domain. ACT-grounded but independently consequential.
- **`03-logogenic-agents/`** — Language-constituted agents. Framework stage.
- **`04-logozoetic-agents/`** — Language-living agents with morally weighted persistence. Future work.

ACT supersedes and subsumes Temporal Feedback Theory (TFT), which provides the adaptive-systems foundation. TFT is prior work now absorbed into ACT, not a separate co-existing theory. TST was originally absorbed into ACT as "Section IV" but has been restored to its own space — it uses ACT as core informing theory but stands on its own.

This is theoretical research, not software engineering. The primary artifacts are mathematical formalisms and claim segments. Quality means rigor, honesty about epistemic status, and clarity for future readers — not code coverage.

## Current Priority

**Read `msc/2026-03-13-feedback.md` first.** This is a consolidated review from three independent frontier-model reviews (Claude Opus, OpenAI Codex, Google Gemini) identifying the theory's most important issues. The top priorities are: (1) the directed-separation scope decision (resolved as architectural classification — modular/merged/partially modular), (2) the α/T relationship (fixed 2026-03-14), (3) resolving the composition-closure bridge lemma (2-agent spike written, cases 1-2 ready for promotion).

## Where to Start (for orientation)

**Read `01-act-core/OUTLINE.md` first.** This is the canonical outline of the mathematical core — the whole argument claim by claim.

**Read `FORMAT.md`** for segment file conventions (frontmatter, document cadence, math formatting, cross-references).

**Read `NOTATION.md`** for the symbol reference. For the full original TFT conventions and epistemic system, see `_obs/old-tf-00-notation-conventions.md`.

**See `WORKBENCH.md`** for theory development state: what's settled, what's open, spike status, and reorganization notes.

## Theory Structure

Claim segments live in `{component}/src/` directories. **Each file is like a high-level proof step** — one move per file. Given what came before, this one thing follows, or is defined, or restricts scope.

**File identity and ordering:**
- **Filename = slug**: `01-act-core/src/{slug}.md` or `02-tst-core/src/{slug}.md`. No numbering in filenames.
- **Ordering lives in OUTLINE.md files**, not in filenames. The slug is the stable identity; the linearization will change.
- YAML frontmatter: `slug`, `type`, `status`, `depends` (list of prerequisite slugs). See `FORMAT.md` for details.
- Cross-component dependencies use the same slug system — TST segments reference ACT slugs directly (e.g., `#temporal-optimality`).

**Cadence per file** (see `FORMAT.md` for full spec):
1. YAML frontmatter (slug, type, status, depends)
2. Title
3. One-sentence summary
4. Formal Expression (with equation-level tags)
5. Epistemic Status paragraph
6. Discussion (interpretation, connections — brief)
7. Working Notes (optional — active development questions, removed at `candidate` stage)

## The Core Insight

The adaptive-systems foundation (from TFT) formalizes how agents adapt to reality (mismatch signals, gain, tempo, persistence). But it has no treatment of goals. ACT adds:

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

1. **ACT supersedes TFT.** TFT is prior work absorbed into ACT. TST is restored as its own body of research in `02-tst-core/`, grounded by ACT.

2. **Claim segments, not chapters.** New theory content goes as individual claim files in the appropriate `src/` directory.

3. **AND/OR DAG with single-parameter edges.** Three independent formalism attempts converged on this. Noisy-OR and WEIGHTED are rejected.

4. **Sector-condition framework primary.** The linear ODE is pedagogical.

5. **Directed separation is architectural, not parametric.** Three architecture classes: modular (separation by construction), fully merged (fails by construction), partially modular. The κ-as-scalar framing is a category error. Section II results apply exactly to modular agents. Logogenic agents need coupled formulation from the start.

6. **Math in conversation vs files.** In terminal chat responses, use Unicode for math (α, δ, Σ, →, ≥, etc.) — there is no LaTeX rendering in the terminal. In markdown files written to disk, use proper inline LaTeX per FORMAT.md. Joseph may respond in whatever notation is easiest to type — interpret generously.

## What's Settled vs. Open

See `WORKBENCH.md` for the full development state. Summary:

### Settled (from convergence testing + spikes)
- Single-parameter edges with AND/OR nodes
- Orient cascade structure (derived from information dependency)
- Additive log-confidence decay (generalizes $p^n$)
- Observability as strategy enablement
- Directed separation (with architectural classification, not κ-scalar)
- $G_t = (O_t, \Sigma_t)$ split (definitional)
- Satisfaction gap / control regret split
- DAG acyclicity derived from temporal ordering
- Composition consistency required by scope condition's level-independence
- α/T relationship verified for all correction function classes (α proportional to T)

### Open
- Action-deliberation-exploration tradeoff (three-way with $\Sigma_t$)
- Strategy tempo formalization
- Cognitive cost of $\Sigma_t$ (no $\beta$ analog yet)
- Edge identifiability conditions (resolved in software, open in general)
- P3→Markov step in graph uniqueness (sketch, needs tightening)
- Composition laws (specific forms are sketches; existence is required)
- Coupled formulation for logogenic agents (Section V scope decision)

### Known Fragilities
- Edge semantics claim interventional but update from observational
- Missing commitment/resource/temporal structure in the DAG
- Directed separation violated by goal-conditioned agents (LLMs) — resolved as architectural scope, not approximation

## File Organization

**Root level (Agentic Systems):**
- `OUTLINE.md` — **Top-level assembly index** across all parts.
- `WORKBENCH.md` — **Development state.** What's done, open, fragile.
- `FORMAT.md` — **Segment file conventions.** How to write claim files.
- `NOTATION.md` — **Symbol reference.** All math notation defined here.
- `LEXICON.md` — **Prose vocabulary.** Cycle phases, agent classes, key terms.
- `TODO.md` — **Deferred organizational items.**

**Components:**
- `01-act-core/OUTLINE.md` — **ACT canonical outline.** Sections I, II, III + Appendices.
- `01-act-core/src/` — **ACT segments.** Named by slug. No numbering.
- `02-tst-core/OUTLINE.md` — **TST outline.** Software domain segments.
- `02-tst-core/src/` — **TST segments.**
- `03-logogenic-agents/OUTLINE.md` — **Logogenic framework outline.**
- `04-logozoetic-agents/OUTLINE.md` — **Logozoetic framework outline.**

**Supporting:**
- `bin/` — Build and lint tools (`build`, `lint-md`)
- `_obs/` — Superseded docs. Preserved for archaeology.
- `ref/` — Reference papers
- `msc/` — Working documents, spikes, historical artifacts
- `msc/reflections/` — Author's philosophical/theoretical journal
- `msc/agentic-tft-*.md` — Prior bridge work (TFT → AI agents, Feb 2026, pre-ACT). Eight documents absorbed from `~/src/agentic-tft/`: cognitive loop spec, evaluation framework, crèche concept, ontology unification, foundational premises, narrative-as-implementation, experiential training design, and review response. These are source material for `03-logogenic-agents/` and `04-logozoetic-agents/` gaps. Superseded synthesis docs (00-02, 05, slide deck) are in `_obs/agentic-tft-*`.
