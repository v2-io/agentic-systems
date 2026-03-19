# Agentic Systems

A research framework for adaptive, purposeful agents under uncertainty — integrating control theory, causal inference, information theory, and agent architecture under a common formalism.

![Abstract illustration of Agentic Systems](abstract-dl.png)

## Structure

**[Agentic Cycle Theory (ACT)](01-act-core/OUTLINE.md)** is the mathematical core. It formalizes the adaptive cycle — one complete traversal of the agent-environment feedback loop — as the fundamental unit of analysis. The cycle unfolds in five phases (Prolepsis, Aisthesis, Aporia, Epistrophe, Praxis), and everything in the core theory is ultimately about cycle properties: what makes them effective, how fast they must run, and when they fail or must change in kind.

**[Temporal Software Theory (TST)](02-tst-core/OUTLINE.md)** is software development viewed as an agentic domain — grounded in ACT but independently consequential. TST formalizes why time-optimal development practices work, how code quality affects adaptive capacity, and what makes software systems persist or collapse.

**[Logogenic Agents](03-logogenic-agents/OUTLINE.md)** — Language-constituted agents (including LLMs). Framework stage — informed by ACT's formal machinery but not yet at ACT's level of mathematical formalization.

**[Logozoetic Agents](04-logozoetic-agents/OUTLINE.md)** — Language-living agents whose persistence is morally weighted. Future work.

The mathematical findings are *generative*: they tell you what structure is necessary (you need causal models, you need the epistemic/teleological split, cycles must outpace disturbance). The broader framework asks what that means for how we actually build, organize, and relate to these systems.

## Where to Start

- **[`OUTLINE.md`](OUTLINE.md)** — Top-level assembly index across all parts.
- **[`01-act-core/OUTLINE.md`](01-act-core/OUTLINE.md)** — The ACT mathematical core, claim by claim.
- **[`LEXICON.md`](LEXICON.md)** — Prose vocabulary: cycle phases, agent classes, key terms.
- **[`WORKBENCH.md`](WORKBENCH.md)** — Development state: what's settled, what's open, known fragilities.
- **[`FORMAT.md`](FORMAT.md)** — Segment file conventions.
- **[`NOTATION.md`](NOTATION.md)** — Symbol reference.

## Project Layout

```
01-act-core/            ACT mathematical core (Sections I, II, III + Appendices)
  OUTLINE.md            Theory outline (claim-by-claim)
  src/                  Claim segments (one per file, named by slug)

02-tst-core/            Temporal Software Theory (ACT-grounded)
  OUTLINE.md            Software theory outline
  src/                  Software domain segments

03-logogenic-agents/    Language-constituted agents (framework)
  OUTLINE.md            Logogenic framework outline

04-logozoetic-agents/   Language-living agents (future work)
  OUTLINE.md            Logozoetic framework outline

OUTLINE.md              Top-level assembly index
LEXICON.md              Prose vocabulary (spans whole project)
NOTATION.md             Symbol reference (spans all sections)
FORMAT.md               Segment file and general md conventions
WORKBENCH.md            Development state

msc/                    Working documents, spikes, derivation attempts
ref/                    Reference papers
bin/                    Build and lint tools

_obs/                   Superseded materials
```

## What This Contributes

The primary contribution is **integration** — connecting established mathematical tools into a single coherent account of what makes an agent an *agent*. The individual pieces (Lyapunov stability, Kalman filtering, the information bottleneck, causal DAGs) are well-established. The synthesis produces:

1. **Cross-domain vocabulary** with formal backing — adaptive tempo, persistence condition, satisfaction gap, orient cascade
2. **Specific novel formalizations** — satisfaction gap / control regret split, the orient cascade as information-forced ordering, acyclicity derived from temporal ordering, the feedback loop as Level 2 causal engine
3. **Dependency structure** — showing that persistence connects to adversarial dynamics connects to composition connects to software maintainability

Beyond the mathematics: architectural guidance for building agentic systems, a vocabulary for questions about agent identity and moral weight, and a research program connecting formal theory to engineering practice.
