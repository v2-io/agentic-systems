# ACT: Agentic Cycle Theory

A first-principles mathematical theory of adaptive, purposeful agents operating
under uncertainty.

## What ACT Is

ACT unifies three aspects of agency that existing theories treat separately:

1. **Adaptive feedback dynamics** — how agents build and maintain models of
   reality under environmental change. Originally developed as Temporal
   Feedback Theory ([TFT](priors/tft/), now subsumed by ACT): mismatch
   signals, update gain via the uncertainty ratio principle, adaptive tempo,
   persistence conditions, adversarial dynamics.

2. **Purposeful agency** — how agents hold, pursue, and revise goals.
   Objectives (O_t) and strategy (Σ_t) are distinct formal objects.
   Strategy is formalized as a probabilistic causal DAG encoding the
   agent's theory of how its actions will produce goal-achievement. This
   is ACT's novel contribution.

3. **Shared intent** — how agents communicate purpose to enable coordinated
   action under uncertainty. Intent compression via the information bottleneck
   principle (the Auftragstaktik / directed opportunism insight).

The theory progresses from general adaptive systems through purposeful agency
and multi-agent dynamics to domain instantiations — particularly software
development and AI agents operating on code.

## Structure

**The theory lives in [`src/`](src/).** Each numbered file is one claim —
an axiom, definition, theorem, or hypothesis — with a sentence summary, formal
expression, and discussion. The claims build incrementally, like a proof.

**[`src/000-contents.md`](src/000-contents.md)** is the master outline: the
full argument in plain English with claim types and dependencies. Start there.

The structure follows **TST's cadence** (one claim per section, strictly
incremental) with **TFT's epistemic system** (equation-level tags, document-
level epistemic status paragraphs, explicit claim tiers). See TF-00 for the
full conventions.

Five sections scope progressively:
1. **Adaptive Systems Under Uncertainty** — the general case (from TFT)
2. **Purposeful Adaptive Systems** — adding objectives and strategy
3. **Coordinated and Adversarial Systems** — multiple agents
4. **Evolving Software Systems** — full TST arc regrounded in ACT
5. **Software-Grounded Agentic Systems** — AI agents, the recursive completion

## Key Results So Far

### Adaptive Systems (from TFT, now subsumed)

The formal backbone is Appendix A's Lyapunov/sector-condition analysis —
general, nonlinear, robust. The linear ODE (TF-11) is a useful worked example,
correct in its regime, not the general case.

- Uncertainty ratio principle: η* = U_M / (U_M + U_o) — validated
  empirically (52% mismatch reduction with Riccati-optimal gain)
- Persistence condition: T > ρ / ||δ_critical|| — robust across all
  correction functions tested
- Adversarial tempo advantage: **superlinear in all coupling-dominant
  regimes**, with the specific exponent depending on disturbance mechanism:
  - Deterministic drift: exponent = 2 (confirmed at 1.999)
  - Stochastic disturbances: exponent = 3/2
  - Non-coupling-dominant: exponent ≈ 1
- **Observation quality gates tempo advantage**: U_o collapses adversarial
  exponent from ~1.0 to ~0.2 — formally grounding Boyd's emphasis on Orient
  quality over raw OODA speed
- Structural adaptation necessity (Prop 10.1) — catastrophic breakdown observed
  at predicted threshold

### Purposeful Agency (exploratory)

Objectives (O_t) and strategy (Σ_t) are distinct formal objects. O_t is the
target state (simple). Σ_t is the probabilistic causal DAG from actions to
objectives (complex, the novel contribution).

- Intent DAG with AND/OR combination rules and single-parameter edges (p) —
  converged across three independent formalism attempts
- Orient cascade: observation → M_t update → Σ_t edge revision → feasibility
  check → possible O_t revision
- Compound probability decay: deep strategies are exponentially fragile (p^n)
- Observability as strategy enablement (not just verification)
- Directed separation: M_t dynamics independent; Σ_t depends on M_t

### Known Fragilities in Purposeful Agency Layer

- **Object model inconsistency.** Earlier docs use δ_goal = G_t − M_t (point
  subtraction) but Σ_t is a DAG. These are type-incompatible. Documents using
  point-valued G_t are superseded by the O_t / Σ_t framework.
- **Edge semantics exceed the update rule.** Edges claim interventional
  semantics but update from observational signals without identifiability.
  Exception: software, where genuine interventions are available.
- **Strategy ≠ intention.** Lacks commitment state, resource budget, temporal
  ordering. Gap between "strategy representation" and "intention theory."
- **DAG acyclicity.** An assumption, not forced by Pearl. Real control loops
  are cyclic; acyclicity holds only after time-unrolling.

## Status

This is a theory under active development. The `src/` directory contains the
current proof outline (~75 claims mapped, ~4 segment files written as examples
establishing the cadence). The adaptive systems foundation is well-grounded.
The purposeful agency layer has the most gaps. The software domain maps closely
from TST but needs regrounding with proper epistemic tags.

See [`src/000-contents.md`](src/000-contents.md) for the full outline.
See [PLANS.md](PLANS.md) for development roadmap.

## Repository Structure

```
act/
├── src/           The theory — numbered claim segments
│   ├── 000-contents.md   Master outline (start here)
│   ├── 010-*.md           Individual claims (axiom, definition, theorem, ...)
│   └── ...
├── ACT-01.md      Working docs from earlier chapter-style approach
├── ACT-03.md      (content being decomposed into src/ segments)
├── priors/
│   ├── tft/       TFT as git submodule (adaptive systems foundation)
│   └── tst/       TST as git submodule (software domain, needs regrading)
├── refs/          Reference papers (Hafez 2026, IBM 2025)
└── scratch/       Working documents
    ├── 00-founding-notes.md           Origin, architecture, positioning
    ├── 01-reference-catalog.md        Prior art catalog
    ├── 02-prior-art-assessment.md     Positioning vs Hafez, IBM, BDI, FEP
    ├── 03-goal-formalism-sketch.md    Early goal formalism (superseded)
    ├── 04-intent-dag-consolidated.md  Canonical intent DAG reference
    ├── track-a-intent-dag/            Intent DAG development (3 variants)
    └── track-b-nonlinear-sims/        Simulations + results (6 variants)
```

## Prior Art and Positioning

- **BDI** (Rao & Georgeff): Named the parts but has no dynamics. ACT provides
  the physiology.
- **Active Inference** (Friston): Unifies perception and action under free
  energy. ACT uses causal feedback dynamics — more transparent and measurable.
- **Hafez et al. 2026**: Bi-predictability metric. Complementary (P =
  architecture, mismatch = performance). The ΔH decomposition is novel.
- **IBM "Agentic AI Needs a Systems Theory" 2025**: Articulates the void ACT
  fills. Not a theory itself.
- **TST** (priors/tst/): Software domain. Gets full treatment in Section IV
  of the theory, regrounded in ACT's formal machinery.
- **agentic-tft** (../agentic-tft/): Bridge from TFT to AI agents. Contains
  cognitive loop spec, evaluation framework, crèche concept. Relevant to
  Section V.
