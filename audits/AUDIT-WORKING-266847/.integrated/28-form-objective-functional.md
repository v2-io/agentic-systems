# Reflection: form-objective-functional

## What the segment does

Defines O_t as the component of G_t that evaluates trajectories, with V_O_t: trajectories → ℝ as its sole interface. The real-valued codomain is a genuine restriction grounded in three arguments: revealed preference (choosing implies scalarization), approximation (most multi-objective problems admit scalarization), and timescale separation (conflicts resolved at slower timescale).

## The scalar comparability restriction

The Epistemic Status is unusually careful here: "The real-valued codomain is a genuine restriction, not a neutral naming." The three grounding arguments are honest — particularly the revealed-preference argument: an agent that acts has implicitly scalarized, so V_O_t makes the implicit explicit. The Pareto / vector-valued extension case is acknowledged and scoped: structural results survive (orient cascade, strategy DAG, directed separation), diagnostic results degrade (satisfaction gap, control regret become qualitative).

## The clean separation O_t / Σ_t / M_t

The "what O_t is NOT" paragraph is cleanly organized:
- O_t evaluates (is this trajectory satisfactory?)
- Σ_t guides (which action sequence produces satisfactory trajectories?)
- M_t believes (what is true about the world?)

The chess player example: simple objective (win), complex strategy (how to win). The three things answer different questions and carry different information. This is the section's definitional split.

## The satisfaction threshold

V_O_t^min is a parameter of the objective (encodes domain success criteria), not a theory output. Point targets and constraint sets define it directly; utility-maximizing objectives may not. When it exists, it enables the satisfaction gap diagnostic — the gap between the best achievable trajectory and the minimum acceptable one.

## Naming targets surfaced

The segment introduces "objective functional" and "value functional" (V_O_t). The "satisfaction threshold" concept. The scalar comparability commitment.

Looking in the tracker for these...

## Wandering thoughts

The AND-node workaround for compound objectives (each constraint becomes a terminal node with its own scalar satisfaction test) is a clean device. It defers the incommensurability problem to the strategy DAG structure rather than to the objective functional. Whether this works for genuinely incommensurable objectives is flagged as open.

The timescale ordering ν_O ≪ ν_Σ ≪ ν_M is labeled "empirical observation, not a derived result." This is honest — it's an empirically grounded ordering that would need to be derived from domain-specific dynamics to be formal. The temporal nesting result covers the structural version of this claim.

How valuable: 6/10 for surprise, 8/10 for load-bearing (objective functional is Section II's evaluation foundation).
