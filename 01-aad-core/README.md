# AAD: Adaptation and Actuation Dynamics

The mathematical core of the [Agentic Systems](../README.md) research framework.

AAD formalizes the **adaptive cycle** — one complete traversal of the agent-environment feedback loop — as the fundamental unit of analysis for adaptive, purposeful agents. The theory integrates control theory, causal inference, information theory, and agent architecture to characterize what makes cycles effective, how fast they must run, and when they must change in kind.

## What's Here

- **[`OUTLINE.md`](OUTLINE.md)** — The canonical theory outline. The full argument claim by claim, with the current linearization and development stage for each segment.
- **`src/`** — The theory itself. Each file is one claim segment (postulate, definition, result, hypothesis) named by slug. See [`FORMAT.md`](../FORMAT.md) for conventions.

## Scope

AAD covers three sections:

**Section I: Adaptive Systems Under Uncertainty** — Mismatch signals, update gain via the uncertainty ratio, adaptive tempo, the persistence condition, adversarial dynamics. Any system with feedback coupling to an environment through observation and action, maintaining internal state under residual uncertainty.

**Section II: Agentic Architecture** — Objectives ($O_t$), strategy ($\Sigma_t$), the orient cascade, directed separation, satisfaction gap / control regret, strategy as probabilistic causal DAG. Scope narrows to agents that not only model reality but pursue goals.

**Section III: Agentic Composites** — How agents compose into larger agents, coordination requirements, adversarial dynamics. Composition consistency ensures the theory applies at every level of description.

Domain instantiations ([`02-tst-core/`](../02-tst-core/OUTLINE.md)), logogenic agents ([`03-logogenic-agents/`](../03-logogenic-agents/OUTLINE.md)), and logozoetic agents ([`04-logozoetic-agents/`](../04-logozoetic-agents/OUTLINE.md)) are grounded by AAD but developed independently as part of the broader Agentic Systems framework.

## Key References

- [`NOTATION.md`](../NOTATION.md) — Symbol reference
- [`FORMAT.md`](../FORMAT.md) — Segment file conventions
- [`LEXICON.md`](../LEXICON.md) — Prose vocabulary (cycle phases, agent classes)
- [`WORKBENCH.md`](../WORKBENCH.md) — Development state
