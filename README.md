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

### From TFT (Part I — solid)
- Uncertainty ratio principle: eta* = U_M / (U_M + U_o)
- Persistence condition: T > rho / ||delta_critical||
- Adversarial tempo advantage (qualitatively superlinear; see caveat below)
- Structural adaptation necessity (Prop 10.1)

### From ACT Part II (exploratory)
- Intent DAG with AND/OR combination rules and single-parameter edges (p)
- Orient cascade: observation -> M_t update -> G_t edge revision -> feasibility
  check -> goal revision
- Compound probability decay: deep strategies are exponentially fragile (p^n)
- Observability as strategy enablement (not just verification)
- Directed separation: M_t dynamics independent; G_t depends on M_t

### From Simulations (empirical)
- **Corollary 11.2's squared tempo advantage (exponent = 2) does not hold at
  realistic discrete-time parameters.** Actual exponent is ~1.0-1.3. The
  squared law is a coupling-dominant, continuous-time limit. Qualitative
  superlinearity is robust; the specific exponent requires regime specification.
- Saturating nonlinearity slightly *increases* the effective exponent
  (counterintuitive).

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
- **Hafez et al. 2026**: Bi-predictability metric. Complementary diagnostic,
  not competing. Shares the goal/intent gap.
- **IBM "Agentic AI Needs a Systems Theory" 2025**: Articulates the void ACT
  fills. Not a theory itself.
