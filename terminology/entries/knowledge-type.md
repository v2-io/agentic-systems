---
slug: knowledge-type
schema_version: 1
term: knowledge type
name: Knowledge Type
brief: Agent-ontology axis distinguishing Static (causal mapping fixed at design time) from Learning (acquires or refines interventional structure during operation).
layer: framing-vocabulary
status: canon
tags: [agent_classes, ontology]
source_type: asf
primary_source: doc/DOMAINS.md
first_asf_mention: doc/DOMAINS.md
see_also: [adaptive-system, agentic-system]
aliases: []
do_not_confuse:
  - "online/offline (carries deployment-context baggage; not the AAD-canonical axis name)"
  - "fixed/adaptive (overloads with Tier 1 *Adaptive system* class)"
internal_note: Activation tier deferred pending broader four-axis ontology review at `msc/domain-unification-2026-05-04/`. The axis-name commitment lands independently of activation-tier.
---

The agent-ontology axis that names *what kind of knowledge* an agent carries — at the right level of abstraction. Two values:

- **Static** — the agent's causal mapping is fixed at design time and does not change during operation. Examples: pre-compiled controllers (PID, LQR), hardcoded reactive policies, fixed-architecture supervised models in inference mode.
- **Learning** — the agent acquires or refines interventional structure during operation. Examples: most RL agents, online supervised systems, agents whose interventional structure updates from feedback.

Already in use across [`doc/DOMAINS.md`](../../doc/DOMAINS.md)'s mapping table; this entry elevates the axis from working-table convention to canonical project vocabulary. The two attribute names (Static / Learning) are concise, antonymous, and avoid loading false familiarity from "online/offline" (deployment-context baggage) or "fixed/adaptive" (overloads with the Tier 1 *Adaptive system* class).

Activation tier — at which agent-spectrum tier the axis becomes definitionally relevant — is under separate review in [`msc/domain-unification-2026-05-04/recommended-agent-ontology.md`](../../msc/domain-unification-2026-05-04/recommended-agent-ontology.md); the current draft activates Knowledge Type at Tier 2 with refinements allowing it at Tier 3+ as well. The naming commitment here lands independently of that activation-tier ratification.
