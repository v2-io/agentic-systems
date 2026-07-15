---
slug: composite-agent
schema_version: 1
term: composite agent
name: Composite Agent
notation:
brief: A set of agency-satisfying sub-agents that constitutes a single coherent actor — the scope condition requiring sufficient teleological alignment to define a composite objective.
layer: framing-vocabulary
status: canon
tags: [agent_classes, structural_concepts]
source_type: asf
primary_source: 01-aat-core/src/scope-composite-agent.md
first_asf_mention: 01-aat-core/src/scope-composite-agent.md
see_also: [agency, adaptive-system, team-persistence, directed-separation]
aliases: []
do_not_confuse: [multi-agent-routing-structure]
---

A set of sub-agents each satisfying [agency](agency.md) constitutes a composite agent when their objectives exhibit sufficient teleological alignment to define a coherent composite purpose $O_c$. Without this condition, they form a multi-agent system that may still be analyzed — but the composition machinery (closure defect, team persistence, composite tempo)
does not apply because $G_c = (O_c, \Sigma_c)$ is ill-defined.

Four routes qualify a group for composite-agent status (any one is sufficient):

- **(C-i) Shared composite objective**: sub-agents are $\epsilon$-compatible with $O_c$-optimal policies.
- **(C-ii) Hierarchical derivation**: sub-objectives $\{O_i\}$ derive from a parent $O_c$ by structure-preserving decomposition (military chain of command, corporate hierarchy).
- **(C-iii) Mutual-benefit alignment**: joint actions raise expected value of some relevance variable $Y$ above non-cooperation baseline for each sub-agent.
- **(C-iv) Equilibrium-convergent strategic interaction**: coupled best-response dynamics converge to (or cycle within the support of) a Nash / correlated / coarse-correlated equilibrium — covering partially-opposing objectives via structural convergence.

Routes (C-i)–(C-iii) are progressively weaker; (C-iv) covers strategic composites with partially opposing objectives. This parallels the single-agent scopes: before asking whether a composite persists, check that it is a composite.

Scope defined in [`#scope-composite-agent`](../../01-aat-core/src/scope-composite-agent.md).
