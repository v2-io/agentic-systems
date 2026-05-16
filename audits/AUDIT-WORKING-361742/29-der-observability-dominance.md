# Reflection: der-observability-dominance

**Segment:** `#der-observability-dominance`

## What this does

Derives: when σ_v → 0 for any node on a strategy path, η_edge → 0 (from the update-gain uncertainty ratio). The edges are frozen at their prior. The path is "epistemically dead." Observability dominates nominal confidence in determining which strategies are epistemically alive.

The quantitative content from deriv-strategic-dynamics:
- Observable intermediate B: each edge gets independent Bayesian updates. Weakest-link sector parameter. Evidence-starvation attenuates downstream edges by ∏θ_j.
- Unobservable intermediate B: per-edge identification FAILS ENTIRELY. Agent is forced to plan-level aggregation. Can know the plan is failing but cannot localize which step needs revision.

The absorbing-state structure: once investment operates through unobservable nodes, frozen beliefs → no mismatch signal → no reason to revise → agent cannot learn AND cannot recognize it cannot learn. Exit requires external shock, proactive observability investment, or another agent.

## Naming relevance

**Row 170 (observability dominance)**: The segment fully confirms the name. "Dominance" is technically precise — it's not metaphorical, it's that observability determines the gain, which determines the update rate, which determines whether a belief is alive or dead. The "dominance" is mechanistic not rhetorical. Strong keep.

"Epistemic freezing" (the rename candidate) describes a CONSEQUENCE, not the mechanism. The mechanism is that observability determines gain (observability dominates the update equation). Freezing is what happens; dominance is why. The mechanism-name is the right name for a mechanism segment.

**Row 405 (unnamed concept — epistemic dead zone)**: This segment is the source for the "epistemically dead path" vocabulary. The card has multiple candidates:
- "Epistemic dead zone": geometric (region of DAG) + operational (no signal reaches it). Strong.
- "Epistemic shadow": visual metaphor — paths in shadow of an unobservable node. Also good.
- "Observability dead zone": extension of observability dominance. Works but the "epistemically" form is more precise.
- "Observability frontier": useful for instrumentation discussions but describes the BOUNDARY, not the REGION.
- "Feedback-starved branch": too specific (assumes branches not general paths).
- "Unobservable strategy subgraph": descriptive but inert.

My reading: "Epistemic dead zone" is strongest because (a) "dead zone" is the standard English metaphor for a region where signals don't penetrate (radio dead zones), (b) the qualifier "epistemic" precisely scopes it to knowledge-updating rather than physical signal, (c) it pairs structurally with "identifiability floor" and "causal-insufficiency detection" as impossibility-class results.

**Row 626 (observability investment)**: The segment provides the economic content for observability investment — the quantified improvement in α_Σ from making an intermediate node observable is the difference between plan-level and per-edge sector parameters. "Observability investment" is confirmed as the right name: you invest in observability (tempo cost, engineering effort) to gain persistence margin.

"Epistemic instrumenting" is an alternative — captures the physical action (adding sensor/monitor). But "investment" is better because it carries the economic tradeoff (the tradeoff IS economic — cost of instrumentation vs persistence gain), while "instrumenting" sounds like a software engineering operation.

## New concepts surfaced

**Observability-adjusted confidence conf_obs(P) = conf(P)·obs(P)**: Named quantity. Probably doesn't need its own row — it's the vehicle for the derivation not a standalone concept.

**Epistemically dead path**: Key vocabulary from this segment. Row 405 handles the dead-zone name-unnamed.

**Plan-level aggregation (vs per-edge identification)**: Named distinction. When intermediates are unobservable, the agent is forced to plan-level aggregation. This is distinct from the credit-assignment problem — it's that per-edge identification is impossible (not just hard).

## Status

Robust-qualitative. The mechanism is solid; the specific functional form (conf_obs = conf·obs) is first-order. The qualitative prediction (low observability → frozen beliefs → ineffective strategy) is robust.
