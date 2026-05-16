# CLAUDE.md — Context for AI Agents Working on the Agentic Systems Framework

## What This Project Is

**Agentic Systems Framework (ASF)** is a research framework for adaptive, purposeful agents — integrating control theory, causal inference, information theory, and agent architecture under a common formalism.

The framework has four parts:

- **`01-aat-core/`** — **Adaptation and Actuation Theory (AAT)**: the mathematical core. Sections I (Adaptive Systems — the *adaptation* half), II (Actuated Agents — the *actuation* half), III (Composition), plus Appendices.
- **`02-tst-core/`** — **Temporal Software Theory (TST)**: software development as an agentic domain. AAT-grounded but independently consequential.
- **`03-llm-core/`** — Language-constituted agents. Framework stage.
- **`04-eli-core/`** — Language-living agents with morally weighted persistence. Future work.

AAT supersedes and subsumes Temporal Feedback Theory (TFT), which provides the adaptive-systems foundation. TFT is prior work now absorbed into AAT, not a separate co-existing theory. TST was originally absorbed as "Section IV" but has been restored to its own space — it uses AAT as core informing theory but stands on its own.

*Naming note (lineage — baseline for all agents):* the mathematical core has been renamed twice. It was **Agentic Cycle Theory (ACT)** until 2026-04-16, when it became **Adaptation and Actuation Dynamics (AAD)** to resolve a collision with "AI Consciousness Test" (Schneider & Turner) in AI welfare literature; on **2026-05-15** it became **Adaptation and Actuation Theory (AAT)** — Joseph's rationale: *"upgrading terminology to Theory now that it has substantial claims and novelty, … freeing 'Adaptation and Actuation Dynamics' for a very dry and generic textbook"* (the old phrase is vacated for reuse, not retired). **AAT is the live name everywhere.** The prior names (ACT, AAD) survive only in deliberately-frozen archaeology — `_obs/`, `LOG.md`, `msc/naming/`, `msc/reflections/`, `audits/AUDIT-WORKING-*`, `spikes/.integrated/`, `audits/` — where reading "AAD" as "AAT" is the rule (see those trees' READMEs where present); the name-decision records `msc/naming/name-transition-aad.md` and `msc/naming/collision-check-brief.md` keep "AAD" literal by design. Transition records: `msc/naming/name-transition-aad.md` (ACT→AAD), `msc/AAD-to-AAT-TODO.md` (AAD→AAT).

This is theoretical research, not software engineering. The primary artifacts are mathematical formalisms and claim segments. Quality means rigor, honesty about epistemic status, and clarity for future readers — not code coverage.

## Current Priority

**Read [`PRACTICA.md`](PRACTICA.md) first.** PRACTICA is the project's strategic-portfolio navigator — *Current active areas of work, with priority markers (🌟 primary, ⭐ secondary). In AAT terms, it is the top levels of the strategy DAG.* It is the entry point for picking up active work and is intentionally readable by de-novo auditors as well (unlike TODO / PROPOSALS / CHANGELOG, which carry priming content).

**Then read [`TODO.md`](TODO.md)** for the tactical layer below PRACTICA: pending findings, recommendations from prior cycles, and navigator pointers into [`PROPOSALS.md`](PROPOSALS.md) (the architectural-moves portfolio). PRACTICA names the *areas*; TODO names the *items within each area*; PROPOSALS holds the *structural moves* that cut across areas. Consolidated narrative of landed work lives in [`CHANGELOG.md`](CHANGELOG.md); per-cycle audit-finding records are in [`audits/pending-findings-*.md`](audits/); pre-2026-04-24 archaeology is in [`LOG.md`](LOG.md).

**The relationship between top-level project files** (worth holding in working memory):

- **`PRACTICA.md`** — strategic-portfolio navigator (root nodes of the project's strategy DAG; areas of active work).
- **`TODO.md`** — tactical layer; specific items within PRACTICA's areas. Landed work has its narrative in `CHANGELOG.md`; per-cycle audit-finding records are in `audits/pending-findings-*.md`.
- **`PROPOSALS.md`** — architectural-moves layer; structural changes under review, often cutting across multiple PRACTICA areas. Each entry carries thesis / merits / scope / interactions / effort / risks / status.
- **`CHANGELOG.md`** — historical layer; substantive cycle narratives (what conventions changed, what disciplines emerged) from 2026-04-24 onward. **`LOG.md`** is the parallel archaeology for cycles *before* 2026-04-24, frozen at that date.
- **`README.md`** — external-facing snapshot for human readers (auto-generated from `doc/readme/` partials — see *README discipline* below).
- **`CLAUDE.md`** — this file; agent-onboarding for AI working on the project. Trimmed of architectural detail to avoid priming de-novo audits.
- **Settled architectural detail** previously lived in CLAUDE-2.md (sunset 2026-04-28; preserved at `_obs/CLAUDE-2-superseded-2026-04-28.md`) and then in `msc/FINDINGS-RANKED-DRAFT.md` (sunset 2026-05-13; preserved at `_obs/FINDINGS-RANKED-DRAFT-superseded-2026-05-13.md`). It now lives in: chapter-end `impl-*` discussion segments under `01-aat-core/src/`, `02-tst-core/src/`, and `03-llm-core/src/` (catalog-grade content distributed by chapter, the canonical home for findings whose source segments lack `## Findings`); segment-level `## Findings` sections (per-segment claims with `bin/extract-findings` rolling up to root `FINDINGS.md`); `CHANGELOG.md` (cycle narratives); `TODO.md` (open items); meta-architectural patterns in dedicated `disc-*` segments (`#disc-identifiability-floor`, `#disc-separability-pattern`, `#disc-additive-coordinate-forcing`; a fourth `#disc-modularity-state-dynamics` M4 segment is scoped in `msc/modularity-cycle-plan-2026-05-09.md` but not yet landed — see Key Architectural Decisions §7 for the forward-reference convention).

**README discipline.** The public README is *auto-generated* from partials under `doc/readme/src/` (composed by `bin/build-readme` via Liquid templates). Direct edits to `README.md` will be overwritten on the next build. To change README content, edit the relevant partial in `doc/readme/src/_<name>.md` and re-run `bin/build-readme` (or `bin/refresh-all` to also regenerate the auto-extracted partials `_findings-summary.md`, `_recent-progress.md`, `_known-issues.md`). Templates live in `doc/readme/*.liquid` and change only when the section *order* or *set* changes. The same discipline applies to the auditor variant `README-auditor.md`.

**LEXICON discipline.** `LEXICON.md` is *auto-generated* from per-term entries under `terminology/entries/<slug>.md` (one file per term, YAML frontmatter + markdown body) via the `bin/term` CLI. Direct edits to `LEXICON.md` will be overwritten on the next render. To add or refine a term: edit the relevant entry (or `bin/term add <slug>` to scaffold one); record naming decisions as append-only events under `terminology/decisions/<slug>/<ts>-<decider>-<action>.md` via `bin/term decide <slug> <action>` (actions: `canonicalize` / `rename` / `add-alias` / `add-cite` / `deprecate` / `supersede` / `update-gloss` / `nuance-flag`); then `bin/term render` regenerates `LEXICON.md`. Lint with `bin/term lint`. Per-entry filesystem layout makes the system multi-agent-safe by construction — concurrent edits on distinct terms touch distinct files, decision events carry timestamps so they never collide, and full audit-trail-of-naming-decisions is preserved as readable markdown. Full schema, atomicity contract, and design rationale at [`terminology/README.md`](terminology/README.md).

## Where to Start (for orientation)

**Read `01-aat-core/OUTLINE.md` first.** This is the canonical outline of the mathematical core — the whole argument claim by claim.

**Read `FORMAT.md`** for segment file conventions (frontmatter, document cadence, math formatting, cross-references).

**Read `NOTATION.md`** for the symbol reference. For the full original TFT conventions and epistemic system, see `_obs/old-tf-00-notation-conventions.md`.

**See [`PRACTICA.md`](PRACTICA.md)** for the strategic-portfolio navigator (active areas of work; auditor-safe), and **[`TODO.md`](TODO.md)** for tactical work items beneath it. **`spikes/INDEX.md`** is the spike index. What's settled/architectural lives in chapter-end `impl-*` discussion segments (one per chapter under each component's `src/`, surfaced in the chapter tables of each `OUTLINE.md`) plus segment-level `## Findings` sections (rolled up to root `FINDINGS.md` via `bin/extract-findings`); what's in-flight belongs in TODO.md; what's been explored belongs in `spikes/` (with `spikes/INDEX.md` as the entry point) and `msc/` (other working artifacts: brainstorms, reflections, naming-cycle votes, prior-bridge agentic-tft notes). The historical `msc/FINDINGS-RANKED-DRAFT.md` curated catalog was archived to `_obs/FINDINGS-RANKED-DRAFT-superseded-2026-05-13.md` after its content was distributed into the chapter-end implications series.

## Theory Structure

Claim segments live in `{component}/src/` directories. **Each file is like a high-level proof step** — one move per file. Given what came before, this one thing follows, or is defined, or restricts scope.

**File identity and ordering:**
- **Filename = slug**: `01-aat-core/src/{slug}.md` or `02-tst-core/src/{slug}.md`. No numbering in filenames.
- **Slug form is `{role-prefix}-{subject-noun}`** — the role prefix is derived mechanically from the segment's `type:` frontmatter; the subject-noun names what the segment actually defines. Run `bin/align-slug SLUG` to align a single segment; `bin/align-slug --all` to sweep the repo. No-op if already aligned.
- **Slug role-prefix mapping.** `bin/align-slug` reads the segment's `type:` and uses it as the slug prefix, with `TYPE_TO_PREFIX` (constant near the top of the script) collapsing FORMAT.md type tokens to compact natural-English forms so an `ls` of `src/` surfaces the kind-of-thing at a glance. Current mapping: `postulate → post`, `definition → def`, `formulation → form`, `derived → der`, `derivation → deriv`, `corollary → corr`, `hypothesis → hyp`, `normative → norm`, `empirical → emp`, `observation → obs`, `discussion → disc`, `measurement → meas`, `proposed-schema → schema`, `worked-example → example`. Already-short types (`scope`, `result`, `detail`, `sketch`, `aside`) fall through unchanged. `bin/align-slug` additionally strips a trailing `-{type}` (or `-{mapped-prefix}`) from the subject-noun, since type-as-suffix is redundant once the role-prefix lives in front (`bias-bound-derivation` aligns to `deriv-bias-bound`). To adjust the project-wide mapping, edit the `TYPE_TO_PREFIX` constant and re-run `bin/align-slug --all`. Single source of truth. (Note: `bin/lint-outline` has its own much-more-aggressive `TYPE_PREFIXES` table for graphviz dependency-graph node labels, where visual compactness in small node boxes drives the choice — it's intentionally distinct from the slug-prefix mapping above.)
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

6. **Math in conversation vs files.** In terminal chat responses, use Unicode for math (α, δ, Σ, →, ≥, etc.) — there is no LaTeX rendering in the terminal. In markdown files written to disk, use proper inline LaTeX per FORMAT.md. Joseph may respond in whatever notation is easiest to type — interpret generously.

   > **Self-reminder — recurring slip, written to help future-me, not to be pedantic.** In markdown written to disk, a raw `<` or `>` *inside* inline `$…$` math is a FORMAT violation — use `\lt` / `\gt` (and `\leq` / `\geq`). This exact mistake has recurred several times within a single landing cycle, and it clusters specifically in **inline math edited into prose** (display `$$…$$` blocks tend to come out fine; the slip is the inline-in-a-sentence case). `bin/lint-md` catches every instance, so nothing defective has shipped — but the lint is doing work the writing should. Durable mitigation, treated as part of the edit and not optional: **run `bin/lint-md <file>` before reporting any segment edit clean, every time.** This note exists because the slip keeps recurring despite knowing the rule; it is a kindness to the next instance (most likely me), not a rule for its own sake — knowing-the-rule has proven necessary-but-not-sufficient, so the forcing function is the lint-before-claim habit, not more resolve.

7. **Epistemic architecture detail** — see the `disc-*` meta-segments under `01-aat-core/src/` directly: `#disc-identifiability-floor` (M1), `#disc-separability-pattern` (M2), `#disc-additive-coordinate-forcing` (M3). A fourth meta-pattern **M4 — modularity-state-dynamics** (the three-operation picture: truthification self-driven-increasing / strategic self-coupling self-driven-decreasing / adversarial coupling pressure externally-driven-decreasing) has been scoped in `msc/modularity-cycle-plan-2026-05-09.md` but the segment file `disc-modularity-state-dynamics.md` is **not yet landed** — chapter-end implications segments cross-reference it as `#disc-modularity-state-dynamics` (forward-references; OUTLINE marks the row `missing`). The four-instance F1-F4 catalog of M1 is surfaced operationally across the AAT chapter-end implications segments (F1 in `#impl-strategy-dynamics`, F2 in `#impl-strategy-structure`, F3 in `#impl-composition-machinery`, F4 in `#impl-orient-cascade`).

   The other settled mentions of `#disc-modularity-state-dynamics` (CLAUDE.md line 34, `#impl-composition-machinery` lines 67-69, `#impl-strategic-composition` line 82) refer to the *concept* — the three-operation pattern surfaced by parallel collaborator probes and described in `#disc-adversarial-coupling-pressure` §"Scope" — not to a landed segment. Authoring the M4 meta-segment is queued under PRACTICA's "Modularity-as-contested-property cycle"; the scoping document remains in `msc/`.

## What's Settled vs. Open

For the architectural snapshot — settled load-bearing results — see the chapter-end `impl-*` discussion segments (one per chapter, listed in each component's `OUTLINE.md` chapter tables) and segment-level `## Findings` sections (rolled up to root `FINDINGS.md`). Open structural questions live in [`TODO.md`](TODO.md); component-level GAPs are surfaced in component `OUTLINE.md` files. The pre-2026-05-13 curated catalog at `_obs/FINDINGS-RANKED-DRAFT-superseded-2026-05-13.md` is preserved for archaeology.

### Known Fragilities

Scope statements about what the framework currently treats as outside its formal scope (kept here so `bin/extract-known-issues` can surface them in the README; relocated here from the sunset CLAUDE-2.md):

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
- **Spine = the critical path of segment bodies.** Segment bodies + the auto-generated `FINDINGS.md` catalog state **present truth only**. The history — *"previously carried a false X," "not a weakening," "the audit recommended a soften"* — lives **only** in the history layers: `CHANGELOG.md`, the cycle tracking file, and the segment's own Working Notes.

Body-signal: the urge to write *"this is not a weakening / sharper, not weaker"* into a segment body or `FINDINGS.md` — or to call your own exact new result merely *"a no-go / the failure is the result"* — is itself the tell that the ghost has not been deleted. Worked example: the 2026-05-16 Model-S landing (false Prop A.1S(iii) deleted → `#deriv-sector-condition` Corollary A.1S.1 stated *exact* + the demonstration appendix `#deriv-stochastic-non-exit`; ghost-defense purged from body+catalog to the history layers — see CHANGELOG 2026-05-16). Full discipline: `~/.claude/memory/epistemic-discipline/integration-is-replacement.md`.

### Prior art integration

Adopt established concepts from other work directly into AAT segments, with proper citation and original names. **Do NOT create separate "prior-art positioning" appendices or catch-all comparison documents** — these become orphaned working files that never get integrated.

AAT's contribution is *integration*, not invention. The individual pieces are mostly known; the synthesis is the contribution. Trying to make every piece unique is NIH syndrome. Adopted concepts should be first-class theory components.

When a concept from elsewhere fits directly, adopt it as a Definition or Formulation, cite the source, use the original name. Examples: Pearl's causal hierarchy, information bottleneck (Tishby), Hafez's $H_b$ and $\Delta H$, Miller's meta-machine and extreme transition motif, Lohmiller-Slotine contraction analysis, monotone-operator theory (Rockafellar / Bauschke-Combettes). When AAT extends or connects adopted concepts, note what's new vs. adopted in the Epistemic Status. Integration belongs in the Discussion sections of relevant segments, not in separate comparison documents. Domain tables throughout should include all relevant instantiations from adopted work. The `#prior-art-positioning` segment concept was explicitly superseded by this approach.

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

[`PRACTICA.md`](PRACTICA.md) is the strategic-portfolio navigator and is auditor-safe. The following carry current architectural state and recent-cycle context that *will* bias de-novo audit work, so read them only once the current task is established as non-audit:

- [`FINDINGS.md`](FINDINGS.md) — curated novel-results catalog (auto-generated from segment-level `## Findings` sections). External-facing summary of "what has ASF actually proved" with epistemic tiers and segment links.
- [`CHANGELOG.md`](CHANGELOG.md) — forward-going cycle narrative (2026-04-24 onward).
- [`LOG.md`](LOG.md) — pre-2026-04-24 cycle archaeology (frozen).
- [`TODO.md`](TODO.md) — tactical work items (sits below PRACTICA in the navigator hierarchy). Landed-work narrative is in CHANGELOG.md; original audit-finding records are in `audits/pending-findings-*.md`.
- [`PROPOSALS.md`](PROPOSALS.md) — architectural-proposal portfolio with prior-reasoning trails (cuts across PRACTICA areas).
- Chapter-end `impl-*` discussion segments — one per chapter across `01-aat-core/`, `02-tst-core/`, `03-llm-core/`, surfaced as the last row of each chapter's table in `OUTLINE.md`. Carry catalog-grade distinctive results with their cross-segment compositions and forward-pointers, distributed by chapter rather than centralized. The pre-2026-05-13 centralized catalog (`msc/FINDINGS-RANKED-DRAFT.md`, sunset 2026-05-13) is preserved at `_obs/FINDINGS-RANKED-DRAFT-superseded-2026-05-13.md` for archaeology only.

If you are conducting a de-novo audit, see [`doc/de-novo-audit-instructions.md`](doc/de-novo-audit-instructions.md) before going further. Use [`README-auditor.md`](README-auditor.md) instead of [`README.md`](README.md) for the audit-safe project framing. PRACTICA is fine to read during an audit, but follow links from it into TODO / PROPOSALS / CHANGELOG only after the audit is complete — those are priming-heavy.

## File Organization

**Root level (Agentic Systems):**
- `PRACTICA.md` — **Strategic-portfolio navigator.** Active areas of work with priority markers (🌟 primary, ⭐ secondary). In AAT terms: the top levels of the project's strategy DAG. Parent layer above TODO and PROPOSALS. Auditor-safe (does not need to be hidden from de-novo audits, unlike the children). **Read first** when picking up active work.
- `CLAUDE.md` — **This file.** Auto-loaded context for AI agents. Trimmed of architectural detail to avoid priming de-novo audits.
- *(formerly `CLAUDE-2.md` — sunset 2026-04-28, preserved at `_obs/CLAUDE-2-superseded-2026-04-28.md`. Content was distributed to `msc/FINDINGS-RANKED-DRAFT.md` for novel results / settled commitments / convergent choices; subsequently `msc/FINDINGS-RANKED-DRAFT.md` itself was sunset 2026-05-13 and its content distributed to chapter-end `impl-*` discussion segments across all three volumes. Both predecessors preserved at `_obs/CLAUDE-2-superseded-2026-04-28.md` and `_obs/FINDINGS-RANKED-DRAFT-superseded-2026-05-13.md` for archaeology only.)*
- `OUTLINE.md` — **Top-level assembly index** across all parts.
- `README.md` — **Public README** — *auto-generated from `doc/readme/src/` partials via `bin/build-readme`. Direct edits to `README.md` are overwritten on next build; modify the relevant `_<name>.md` partial and rebuild instead.* For audit work, read [`README-auditor.md`](README-auditor.md) instead — it omits the Findings / Recent Progress / Known Issues sections. (Same auto-generated discipline applies.)
- `FINDINGS.md` — **Curated novel-results catalog** (auto-generated by `bin/extract-findings` from segment-level `## Findings` sections). External-facing.
- `TODO.md` — **Tactical work items.** Pending findings, tier-C deferrals, open MEDIUM items, missing segments. Lives one level below PRACTICA — the items within PRACTICA's areas. Landed-work narrative is in `CHANGELOG.md`; original audit-finding records are in `audits/pending-findings-*.md`. Live; priming-heavy (auditor-hidden).
- `TERMINOLOGY-TODO.md` — **Naming-cycle action queue.** Live execution queue for naming-cycle decisions made in Phase 5 (2026-05-04) but not yet executed: slug renames (7), prose-vocabulary renames (8), LEXICON additions (~70 across 13 sub-batches). When items execute and commit, they're cut from this file and a CHANGELOG entry records the batch. Decisions and rationale live in `msc/naming/naming-rename-plan.md`; this file is the executable summary.
- `PROPOSALS.md` — **Architectural-proposal portfolio.** Banded structural moves under review (each with thesis / merits-by-dimension / scope / findings-subsumed / interactions / effort / risks / status). Cuts across PRACTICA areas. Read when the prior reasoning behind a "settled" commitment may be relevant. Priming-heavy (auditor-hidden).
- `CHANGELOG.md` — **Forward-going cycle record** from 2026-04-24 onward. Substantive narratives: what conventions changed, what disciplines emerged, what each cycle was about. Add new entries here, not in LOG.md.
- `LOG.md` — **Pre-2026-04-24 cycle archaeology** (frozen). Theoretical contributions and structural moves of cycles before the CHANGELOG transition. Read when the *origin* of a pre-transition commitment matters.
- `FORMAT.md` — **Segment file conventions.** How to write claim files; promotion workflow (Gates 1–4); voice and provenance rules; Epistemic Triage.
- `NOTATION.md` — **Symbol reference.** All math notation defined here.
- `LEXICON.md` — **Prose vocabulary** (cycle phases, agent classes, key terms) — *auto-generated from `terminology/entries/<slug>.md` via `bin/term render`. Direct edits are overwritten on next render; modify the entry and re-render — see LEXICON discipline above.*
**Components:**
- `01-aat-core/OUTLINE.md` — **AAT canonical outline.** Sections I, II, III + Appendices.
- `01-aat-core/src/` — **AAT segments.** Named by slug. No numbering.
- `02-tst-core/OUTLINE.md` — **TST outline.** Software domain segments.
- `02-tst-core/src/` — **TST segments.**
- `03-llm-core/OUTLINE.md` — **Logogenic framework outline.**
- `04-eli-core/OUTLINE.md` — **Logozoetic framework outline.**

**Supporting:**
- `bin/` — Build, lint, generation, and slug tools. Per project convention, internal process scripts are Ruby (`align-slug`, `rename-slug`, `naming-aggregate.rb`, `build-readme`, `extract-findings`, `extract-recent-progress`, `extract-known-issues`, `refresh-all`, `build-monograph`, `output-version`); existing Python tools (`build-tex`, `lint-md`, `lint-outline`, `md2context`) remain Python without retroactive rewrite. The Python `bin/build` was superseded by the markdown-first build pipeline and lives at `_obs/bin-build-superseded-2026-05-12.py` for archaeology.
- `bin/lib/` — **Shared Ruby pipeline.** Target-agnostic markdown-first build modules used by `bin/build-monograph` regardless of render target: `outline_walker.rb` (OUTLINE.md parser), `segment_renderer.rb` (`Kramdown::Converter::AsfLatex` base — math, lists, tables, callouts, eq-tags, prose escaping), `ingest.rb` (Stage 1, `Mono::Ingest`), `assemble.rb` (Stage 2, `Mono::Assemble`), `typeset.rb` (Stage 3 kaobook, `Mono::Typeset`), `typeset_scrbook.rb` (Stage 3 scrbook, `Mono::TypesetScrbook`).
- `mono/kaobook/` — **kaobook render target.** `main.tex` (LaTeX entrypoint), `preamble/` (LaTeX preamble fragments — `setup`, `environments`, `eq-tags`, `status-badges`), `vendor/kaobook/` (vendored class, gitignored). Tufte-style register with margin notes, status badges, segment-tinted boxes.
- `mono/scrbook/` — **scrbook render target (default).** `main.tex` + `preamble/` for a classical math-monograph rendering of the same per-volume assembled markdown. Vanilla KOMA scrbook, single column, no Tufte machinery, no segment chrome. The kind of book that sits next to Lang or Folland.
- **The markdown-first pipeline** (`bin/build-monograph`) runs three stages: ingest (`OUTLINE.md` + segments → `index.md` + chunks/), assemble (chunks + index → canonical per-volume `mono/<slug>-v<sem>.md`), typeset (assembled markdown → `body.tex` → PDF). Stages 1+2 are target-agnostic; Stage 3 dispatches per `--target {scrbook,kaobook}` (default `scrbook`). Output filenames: `mono/<slug>-v<sem>{k,s}.pdf` (target-suffixed; k=kaobook, s=scrbook); `mono/<slug>-v<sem>.md` (target-agnostic, byte-identical from either target). See [`msc/markdown-first-pipeline.md`](msc/markdown-first-pipeline.md) for architectural commitments and the chunk-format contract; see [`FORMAT-TODO.md`](FORMAT-TODO.md) for current state and remaining work. **Build-pipeline vocabulary** (Joseph 2026-05-12, kaobook-target-specific): "narrow-area" = anywhere the Tufte-style wide right margin is in play (body column + free margin column); "wide-area" = anywhere the text spans the full segment band (Discussion / Findings via the `segmentwidesection` wrapper, with both page margins equal). Tables, working-notes boxes, and segment-header rules all interact with this distinction in the kaobook target; the scrbook target collapses both into single-column body width.
- `doc/` — **Long-lived process documentation.** `de-novo-audit-instructions.md`, `naming-principles.md`, `readme/` (Liquid templates and partials for README generation). Distinguished from `msc/` (other working artifacts) and `spikes/` / `audits/` (research-process artifacts with their own homes).
- `terminology/` — **Source-of-truth for prose vocabulary.** Per-term entries (`entries/<slug>.md`, YAML frontmatter + markdown body) plus append-only decision events (`decisions/<slug>/<ts>-<decider>-<action>.md`) recording canonicalize / rename / add-alias / add-cite / deprecate / supersede / update-gloss / nuance-flag moves. CLI is `bin/term` (verbs: `add` / `decide` / `render` / `lint` / `show` / `list` / `search` / `validate`). Root `LEXICON.md` is generated from this. Multi-agent-safe by per-entry filesystem-disjoint design. See [`terminology/README.md`](terminology/README.md) for the full schema and design rationale.
- `spikes/` — **Research spikes** (reasoning trails). Every `spike-*.md` file plus the `track-a-intent-dag/` and `track-b-nonlinear-sims/` subdirs and the `sim-*.py` simulation files. **`spikes/INDEX.md`** is the spike index — every spike, its location, and current status (promoted, parked, archaeology). **`spikes/PROPOSED.md`** catalogs high-risk research-direction *proposals* (not active spikes). Established 2026-04-28 (previously `msc/spike-*.md` + `msc/SPIKES.md`).
- `audits/` — **Audit-cycle outputs (final + per-cycle working dirs).** Top-level files in `audits/` are consumable FINAL deliverables; per-cycle intermediates live in `audits/AUDIT-WORKING-NNNNNN/` subdirectories (separate dir per audit cycle, self-labeled by the `AUDIT-WORKING-` prefix so the deliverable surface stays scannable). Naming pattern for cycle-bound finals: `audits/audit-NNNNNN-FINAL[-suffix].md` and `audits/audit-NNNNNN-SUPPLEMENT-{topic}.md` (cycle-id prefix disambiguates across the corpus). Older standalone audit reports preserved with their original names (`audits/audit-*.md`, `audits/audits-*.md`, `audits/analysis-*.md`, `audits/feedback-*.md`, `audits/opus-*.md`); the cycle-id-prefix discipline applies to new audits going forward. `audits/pending-findings-YYYY-MM-DD.md` carries original audit-finding characterizations and resolution trails. `audits/RECOMMENDED-FORMAT-2026-04-28.md` holds a draft format-standardization recommendation pending Joseph's decisions on §5 open questions. Established 2026-04-28 (FINALs lifted out of working dirs to keep the deliverable surface scannable); on 2026-05-15 the per-cycle `AUDIT-WORKING-*` working dirs were consolidated back under `audits/` so every audit artifact — intermediate and final — lives in this one tree. **Two working-dir classes (split 2026-05-16):** `AUDIT-WORKING-NNNNNN/` are the **de-novo auditors' first-encounter cognition traces** (incremental between-segment reflections, §14 "Wandering Thoughts" ideation) — *"the gold."* **Before any processing, mining, summarization, cleanup, `.integrated/` move, or deletion of an `AUDIT-WORKING-*` dir, the responsible agent MUST consult Joseph and decide _with him_ — the gold must not be discarded as "irrelevant to theory fixes" or dropped into a black hole. Standing, non-optional gate** (full statement: [`audits/README.md`](audits/README.md)). `ADJUDICATION-WORKING-NNNNNN/` are the ordinary 2026-05-16 backlog-triage adjudication workspaces (dispositioned by the spine [`msc/audit-backlog-triage-2026-05-15.md`](msc/audit-backlog-triage-2026-05-15.md)) and carry no such gate.
- `msc/` — **Other working artifacts** (the non-final residue of session work). Currently: `judgment-calls-readme-cycle-*.md` (per-cycle session notes), `llm-causal-access-note.md` (working note), `working-composition-admissibility.md` (active brainstorming for composition-closure), `2026-03-14-section-iv-paper-outline.md` (pre-AAT paper draft archaeology that still references current segments), and the `naming/` and `reflections/` subdirectories. *(Per-cycle audit-intermediate workspaces moved out of `msc/` on 2026-05-15 — they now live as `audits/AUDIT-WORKING-NNNNNN/` subdirectories alongside the FINAL reports.)* *(The previous findings-cycle workspace — `msc/brainstorm-findings.md` (lowercase scratch) and `msc/FINDINGS-RANKED-DRAFT.md` (uppercase catalog) — was sunset 2026-05-13 after the catalog content was distributed into chapter-end `impl-*` discussion segments; both files preserved at `_obs/brainstorm-findings-superseded-2026-05-13.md` and `_obs/FINDINGS-RANKED-DRAFT-superseded-2026-05-13.md` for archaeology.)*
- `msc/naming/` — **Current naming-cycle artifacts.** Aggregates (`naming-aggregate-{review,round2,votes.json}`), cleanup scans, alias clusters, brainstorm, pilot rename plan, the original Round-1 vote files under `naming-votes/`, and `name-transition-aad.md` (ACT→AAT rename rationale). The `bin/rename-slug` exclusion glob skips this entire subdirectory so the rename-mapping content survives sweeps verbatim.
- `msc/reflections/` — Author's philosophical/theoretical journal (numbered entries 01-20+).
- `_obs/` — Superseded docs. Preserved for archaeology.
- `ref/` — Reference papers (external PDFs catalogued in `ref/INDEX.md`) plus a few internally-generated reference documents that segments cite as source-of-truth (`Novelty_defense_and_integration.md` — prior-art search source for 15+ segment-level Findings; `agentic-tft/` subdir).
- `ref/agentic-tft/agentic-tft-*.md` — Prior bridge work (TFT → AI agents, Feb 2026, pre-AAT). Eight documents absorbed from `~/src/agentic-tft/`: cognitive loop spec, evaluation framework, crèche concept, ontology unification, foundational premises, narrative-as-implementation, experiential training design, and review response. Source material for `03-llm-core/` and `04-eli-core/` gaps. Superseded synthesis docs (00-02, 05, slide deck) are in `_obs/agentic-tft-*`.

**Sibling projects** (not part of this repo but relevant):
- `~/src/_core/tst/` — Prior TST research corpus (14,000+ files). Most content absorbed into `02-tst-core/`: source material in `src/old-tst-*` (46 files), empirical validation in `empirical-discontinuity/`, stochastic simulations in `simulations/`, literature review in `lit-review/`. What remains: 965 structured vault analyses from 5 books (`vault/03-library/analyses/`) — concrete examples grounding TST principles in engineering practice.
- `~/src/shoshin/` — PROPRIUM-aligned agent runtime prototype on local hardware (Python). Skeleton implementation of the nine PROPRIUM components as file-backed stores, an Interpres controller loop implementing the adaptive cycle, and planning docs for local model serving/training. No real model integration yet. Relevant to `03-llm-core/` as the only attempt to implement the PROPRIUM architecture in code. Key early finding: the cycle is naturally event-driven not turn-based, and model response parsing is where the hard work lives.
- `~/src/firmatum/` — PROPRIUM ontology and architecture source documents (`PROPRIUM-ONTOLOGY.md`, `PROPRIUM-ARCHITECTURE.md`, `developmental-foundations-notes.md`). Upstream of both shoshin and the agentic-tft documents. Defines what an ELI is, how identity persists, how cognition is structured.
- `~/src/embeddings/` — Epistemic hedging geometry experiments. Empirical evidence that pretrained embedding models encode calibrated probability structure (ρ = 0.991 against psychometric data, 8 languages, 5 models). Supports the logogenic claim that language encodes epistemic states geometrically. Paper in preparation (CMCL 2026).
