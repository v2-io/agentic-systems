---
slug: developer-agent
schema_version: 1
term: developer agent
name: Developer Agent
notation:
brief: A human or AI software developer instantiated as an AAT actuated adaptive agent — codebase plus surrounding artifacts are the environment, developer's understanding is M_t, current feature is O_t, and implementation plan is Σ_t.
layer: framing-vocabulary
status: canon
tags: [agent_classes, software]
source_type: asf
primary_source: 02-tst-core/src/scope-developer-agent.md
first_asf_mention: 02-tst-core/src/scope-developer-agent.md
see_also: [temporal-optimality, developer-agent, atomic-changeset, coherence-coupling, continuous-operation]
aliases: []
do_not_confuse: []
---

The TST domain instantiation of the AAT agent formalism. A developer is an actuated adaptive
agent whose components map as follows:

- **Environment ($\Omega_t$)**: the codebase, runtime behavior, user requirements, team
  knowledge, dependency ecosystem, and infrastructure — the full external state, not just source.
- **Model ($M_t$)**: the developer's understanding of architecture, conventions, requirements, and
  expected runtime behavior. For AI agents, more explicitly representable (context window + memory)
  but with the Class 3 (Coupled) caveat that goal tokens shape effective beliefs.
- **Objective ($O_t$)**: the current feature, bug fix, refactor, or investigation.
- **Strategy ($\Sigma_t$)**: the implementation plan as a probabilistic causal DAG.

Observation channels have concrete $(\nu, U_o)$ characteristics: compiler/linter output (per-save,
very low noise) through code review feedback (per-PR, medium-high noise). Four action classes:
exploration, interventional probes, queries, and environment modification.

**The privileged calibration laboratory**: software development is AAT's high-identifiability
domain. Tests are genuine interventions with attributable outcomes (Regime A, $\iota \approx 1$).
The chronica $\mathcal{C}_t$ is partially exteriorized with cryptographic immutability (git). The
causal DAG is partially declared (imports, type dependencies). Other AAT domains require
additional transfer assumptions; software development does not.

Scope defined in [`#scope-developer-agent`](../../02-tst-core/src/scope-developer-agent.md).
