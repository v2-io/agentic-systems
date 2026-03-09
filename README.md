# ACT: Agentic Cycle Theory

A first-principles mathematical theory of adaptive, purposeful agents operating
under uncertainty.

## What ACT Is

ACT unifies three aspects of agency that existing theories treat separately:

1. **Adaptive feedback dynamics** — how agents build and maintain models of
   reality under environmental change. Inherited from
   [Temporal Feedback Theory](priors/tft/) (TFT): mismatch signals, update
   gain via the uncertainty ratio principle, adaptive tempo, persistence
   conditions, adversarial dynamics.

2. **Purposeful agency** — how agents hold, pursue, and revise goals. Goals
   (G_t) are formalized as probabilistic causal DAGs encoding the agent's
   theory of how its actions will produce goal-achievement. This is ACT's
   novel contribution.

3. **Shared intent** — how agents communicate purpose to enable coordinated
   action under uncertainty. Intent compression via the information bottleneck
   principle (the Auftragstaktik / directed opportunism insight).

## Why ACT Exists

TFT provides a complete theory of adaptive systems — how agents learn about
and track reality. But it has no port. Its sole implicit goal is survival
(the persistence condition T > rho). ACT adds the compass: goals as
first-class objects with their own representation, mismatch signals, update
dynamics, and revision mechanisms.

> *"Ignoranti quem portum petat nullus suus ventus est."*
> ("If a man knows not to which port he sails, no wind is favorable.")
> — Seneca, *Epistulae Morales*, LXXI

## Theoretical Landscape

ACT covers a continuum from pure survival to deliberate purposeful agency:

- **Adaptive systems** (TFT's contribution): Agents that track reality.
  Mismatch, gain, tempo, persistence. The survival space.
- **Purposeful agents**: Adaptive systems that also aim. Objectives (O_t),
  strategy (Σ_t as probabilistic causal DAG), the Orient cascade where
  reality-understanding and intent interact.
- **Multi-agent dynamics**: Shared intent, intent decomposition across
  agents, adversarial targeting of strategy structure.

Domain instantiations (software, military, organizational, AI agents) apply
this machinery to specific settings. How the theory is ultimately organized
should emerge from the dependency structure of its claims.

## Key Results So Far

### From TFT (Part I)

The formal backbone is Appendix A's Lyapunov/sector-condition analysis —
general, nonlinear, robust. The linear ODE (TF-11) is a useful worked example,
correct in its regime, not the general case.

- Uncertainty ratio principle: eta* = U_M / (U_M + U_o) — validated
  empirically (52% mismatch reduction with Riccati-optimal gain)
- Persistence condition: T > rho / ||delta_critical|| — robust across all
  correction functions tested
- Adversarial tempo advantage: **superlinear in all regimes**, with the
  specific exponent depending on the disturbance mechanism:
  - Deterministic drift, coupling-dominant: exponent = 2 (confirmed at 1.999)
  - Stochastic disturbances, coupling-dominant: exponent = 3/2
  - Non-coupling-dominant: exponent ~ 1
- **Observation quality gates tempo advantage** ("fog of war"): U_o collapses
  adversarial exponent from ~1.0 to ~0.2 — formally grounding Boyd's emphasis
  on Orient quality over raw OODA speed
- Structural adaptation necessity (Prop 10.1) — catastrophic breakdown observed
  at predicted threshold

### From ACT Part II (exploratory)

Objectives (O_t) and strategy (Σ_t) are distinct formal objects. O_t is the
target state (simple). Σ_t is the probabilistic causal DAG from actions to
objectives (complex, the novel contribution).

- Intent DAG with AND/OR combination rules and single-parameter edges (p) —
  converged across three independent formalism attempts
- Orient cascade: observation -> M_t update -> Σ_t edge revision -> feasibility
  check -> possible O_t revision
- Compound probability decay: deep strategies are exponentially fragile (p^n)
- Observability as strategy enablement (not just verification)
- Directed separation: M_t dynamics independent; Σ_t depends on M_t

### From the Hafez Bridge (empirical)

Hafez's bi-predictability P and TFT's mismatch answer different questions:
- **P measures coupling architecture** (how tightly agent and environment are
  informationally coupled)
- **Mismatch measures coupling performance** (how well the agent is actually
  tracking reality)
- Agency costs coherence: P drops from 0.44 (passive) to 0.27 (active)
- P cannot detect adversarial dynamics (scale-invariant)
- **ΔH (forward/backward predictive asymmetry) is genuinely novel**: H_b =
  strategic legibility — how predictable your actions are from outcomes.
  No current TFT analog. Potentially important for adversarial multi-agent.

## Status

This is a theory under active development. The TFT foundation (Part I) is
well-structured and internally consistent. The purposeful agency extension
(Part II) is in exploratory sketch phase — the intent DAG formalism has been
developed through three independent convergence-tested approaches, but has
not been consolidated into a formal document sequence.

See [PLANS.md](PLANS.md) for the development roadmap.

## Repository Structure

```
act/
├── priors/
│   ├── tft/    TFT as git submodule (the adaptive systems foundation)
│   └── tst/    TST as git submodule (the software domain instantiation)
├── refs/       Reference papers (Hafez 2026, IBM 2025)
└── scratch/    Working documents
    ├── 00-founding-notes.md           Origin, architecture, positioning
    ├── 01-reference-catalog.md        Prior art catalog
    ├── 02-prior-art-assessment.md     Assessment of Hafez, IBM, FAST workshop
    ├── 03-goal-formalism-sketch.md    G_t math + DAG revision
    ├── track-a-intent-dag/            Intent DAG formalism (3 variants + priorities)
    └── track-b-nonlinear-sims/        Nonlinear dynamics simulations + results
```

## Prior Art and Positioning

- **BDI** (Rao & Georgeff): Named the parts (Belief, Desire, Intention) but
  has no dynamics. ACT provides the physiology.
- **Active Inference** (Friston): Unifies perception and action under free
  energy. ACT uses causal feedback dynamics — more transparent and measurable.
- **Hafez et al. 2026**: Bi-predictability metric. Empirically confirmed as
  complementary (P = architecture, mismatch = performance). The ΔH
  decomposition (strategic legibility) is novel and potentially useful for
  ACT's adversarial multi-agent work.
- **IBM "Agentic AI Needs a Systems Theory" 2025**: Articulates the void ACT
  fills. Not a theory itself.
