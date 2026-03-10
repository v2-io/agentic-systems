# CLAUDE.md — Context for AI Agents Working on ACT

## What This Project Is

ACT (Agentic Cycle Theory) is a first-principles mathematical theory of
adaptive, purposeful agents. It supersedes and subsumes Temporal Feedback
Theory (TFT, in priors/tft/), which provides the adaptive-systems
foundation. TFT is prior work now absorbed into ACT, not a separate
co-existing theory.

This is theoretical research, not software engineering. The primary artifacts
are mathematical formalisms and claim segments. Quality means rigor, honesty
about epistemic status, and clarity for future readers — not code coverage.

## Where to Start

**Read `src/000-contents.md` first.** This is the master outline — the whole
argument in plain English. It maps ~75 claims across five sections, shows
what's written, and marks gaps honestly.

**Read `priors/tft/TF-00.md`** for the notation conventions and epistemic
system that ACT adopts.

## Theory Structure

The theory lives in `src/` as numbered claim segments. Each file is one
claim following **TST's cadence** (one claim per section, sentence summary,
formal expression, discussion) with **TFT's epistemic system** (equation-
level tags, document-level epistemic status paragraphs, claim tiers).

- Numbered by 10s to allow insertion (010, 020, ..., 530, ...)
- YAML frontmatter with `slug` field for stable cross-referencing
- References use `#slug-name` tags, NOT file numbers
- Five sections scope progressively: I. Adaptive Systems, II. Purposeful
  Adaptive Systems, III. Coordinated/Adversarial, IV. Evolving Software,
  V. Software-Grounded Agentic Systems

## The Core Insight

The adaptive-systems foundation (from TFT) formalizes how agents adapt to
reality (mismatch signals, gain, tempo, persistence). But it has no
treatment of goals. ACT adds:

- **O_t** (objective — what the agent wants) and **Σ_t** (strategy — how
  it plans to get there) alongside **M_t** (reality model)
- Strategy formalized as a **probabilistic causal DAG** (AND/OR nodes,
  edges with confidence weights p, update via the uncertainty ratio)
- The **Orient cascade**: observation → M_t update → Σ_t edge revision →
  feasibility check → possible O_t revision
- **Directed separation**: M_t dynamics independent of O_t/Σ_t; Σ_t
  depends on M_t; action couples all three
- The O_t / Σ_t distinction supersedes earlier docs using "G_t" for both

## Epistemic Conventions

Follow TFT's conventions exactly (see priors/tft/TF-00.md):

**Equation-level tags** (inline before equations):
- `*[Definition]*`, `*[Derived]*`, `*[Derived (Conditional on ...)]*`
- `*[Hypothesis]*`, `*[Empirical Claim]*`, `*[Formulation]*`
- `*[Discussion]*`, `*[Assumption]*`

**Document-level Epistemic Status paragraph** at the top of each segment,
explaining what's derived vs hypothesized vs discussion-grade. Example:
"The threshold's *existence* is *robust qualitative*. The quantitative form
is *exact* under assumptions GA-2, GA-3."

**Claim tiers** (from TF-00's Claim Registry):
- **Exact**: Mathematically validated under stated assumptions
- **Robust qualitative**: Survives across assumptions; specific form approximate
- **Heuristic**: Useful approximation; quantitative form may not hold
- **Conditional**: Depends on explicitly named local assumptions

Do NOT use "Solid," "Confident," or "Plausible" as tier labels — these are
not TFT terms.

**Every claim must be grounded.** If stated as fact, it needs its own
derivation or is explicitly tagged as hypothesis/empirical/discussion-grade.
Do not let ungrounded assertions transfer from TST uncritically.

## Key Architectural Decisions

1. **ACT supersedes TFT.** Don't modify priors/tft/ documents. Don't treat
   TFT as a separate co-existing theory.

2. **Claim segments, not chapters.** New theory content goes in `src/` as
   individual claim files, not in ACT-01/ACT-03 style chapter documents.

3. **AND/OR DAG with single-parameter edges.** Three independent formalism
   attempts converged on this. Noisy-OR and WEIGHTED are rejected.

4. **Sector-condition framework primary.** The linear ODE is pedagogical.

5. **TST gets full treatment in Section IV.** Not just domain table rows.
   T-01 (temporal optimality) is generalized as ACT's first axiom (#010).

## What's Settled vs. Open

### Settled (from convergence testing)
- Single-parameter edges with AND/OR nodes
- Orient cascade structure
- Compound probability decay (depth fragility)
- Observability as strategy enablement
- Directed separation
- O_t / Σ_t split (not G_t)

### Open (see Section II gaps in contents)
- Three-mismatch-type interaction ordering
- Action-deliberation-exploration tradeoff
- Strategy tempo formalization
- Cognitive cost of Σ_t (no β analog yet)
- Edge identifiability conditions
- Multi-agent intent propagation

### Known Fragilities
- Object model type error (point δ_goal vs DAG Σ_t — superseded docs exist)
- Edge semantics claim interventional but update from observational
- Missing commitment/resource/temporal structure in the DAG
- DAG acyclicity is an assumption, not forced

## Simulation Findings

The track-b simulations (scratch/track-b-nonlinear-sims/) validated and
refined specific claims:

- Cor. 11.2's exponent = 2 under deterministic drift (confirmed: 1.999)
- Under stochastic disturbances, exponent = 1.5 (not 2.0)
- Observation noise collapses adversarial exponent from ~1.0 to ~0.2
- Per-dimension persistence exact (scalar overestimates by 72%)
- TF-06's gain principle empirically validated (52% reduction)

## File Organization

- `src/` — **The theory.** Numbered claim segments. Start here.
- `ACT-01.md`, `ACT-03.md` — Earlier chapter-style working docs (being
  decomposed into src/ segments; don't extend these)
- `priors/tft/` — TFT submodule (read-only reference)
- `priors/tst/` — TST submodule (read-only; content regrounded in src/)
- `refs/` — Reference papers
- `scratch/` — Working documents, historical artifacts
  - `04-intent-dag-consolidated.md` — Canonical intent DAG reference
  - `track-a-intent-dag/` — DAG formalism variants (historical)
  - `track-b-nonlinear-sims/` — Simulation code and results
- `../agentic-tft/` — Prior bridge work: TFT → AI agents. Docs 10-14
  relevant to Section V.
