# 08 - post-causal-structure

Segment: `01-aat-core/src/post-causal-structure.md` (`#post-causal-structure`)

Dependencies: `def-agent-environment`, `def-chronica`, both read. Dependency-order check passes.

## Segment Read

This segment postulates irreducible causal structure grounded in temporal ordering. The key claim is primitive: an event can cause another only if it temporally precedes it. AAD does not derive the arrow of time; it takes directed temporal order as a physical precondition for agents.

The segment also distinguishes causal structure from coupling strength. Strong, weak, nominal, and zero coupling differ in interventional richness, but temporal ordering remains. Zero coupling drops out of agency scope while remaining adaptive-scope if observation under uncertainty persists.

## Predictions Vs Evidence

I expected causal structure to arrive around Pearl machinery, but this segment rightly puts temporal causality before Pearl's hierarchy. The hierarchy will refine reasoning levels; this postulate installs the direction of possible influence.

The notable surprise is `nominal coupling`: actions may not materially affect $\Omega_{t+1}$, but choosing what to observe can still alter observation distributions. That term may be a later naming target, especially for queries and attention in logogenic/TST contexts.

## Cross-Segment Consistency

This segment coheres with `#def-chronica`: chronica is not a bag of events but an ordered causal record. It also clarifies `#scope-agency`: agency requires nonzero interventional contrast, which can come through action effects on the world or query-like effects on observations.

The segment references `#def-pearl-causal-hierarchy` and `#def-causal-information-yield` before they appear. Like the previous agency segment, this is understandable as forward orientation but means a first reader is seeing terms before formal definitions. For naming, I will wait on CIY until its defining segment.

## Naming Notes

`causal structure` is plain but appropriate for a foundational postulate. It names the broad thing: the agent-environment interaction has ordered possible influence. A more evocative name like "arrow of time" would be too narrow and physical; a Pearl-specific name would be too downstream.

`nominal coupling` feels less successful. The segment defines it as query/action choice affecting observation distributions while barely affecting world state. "Nominal" can sound like "in name only" or "negligible," but here the observation-choice effect is load-bearing. I will inspect the target if present; I may prefer query/attention-bound language once grounded here.

The coupling-strength ladder may deserve stable names if reused: strong coupling, weak coupling, nominal coupling, zero coupling. Those are readable, but the nominal case is the fragile one.

## What This Enables

This postulate enables recursive update direction, mismatch as retrospective, action as prospective, chronica monotonicity, and later CIY. It also prevents the feedback loop from being treated as an undirected correlation structure.

For naming, it reinforces the importance of words like `directed`, `retrospective`, and `prospective` when they appear later. Those are not prose flourishes; they descend from temporal asymmetry.

## Watchlist

- Whether `nominal coupling` survives in TST/logogenic contexts or gets renamed to query-bound agency/coupling.
- Whether downstream uses of Pearl levels preserve the distinction between primitive temporal causality and statistical/interventional causality.
- Whether "causal structure" becomes overloaded with graph/DAG structure later.

## Wandering Thoughts

This segment is conceptually simple and structurally deep. It says AAD starts in a world where time points one way. That is almost too obvious, but making it explicit pays off because it blocks future confusions: the agent's update cannot use future observations; mismatch compares past prediction to later contact; action aims forward.

The coupling ladder is also a good reminder that agency is not binary in ordinary intuition even if the scope boundary is binary formally. Weak scientific interventions, queries, and attention choices live near the boundary. The name for that boundary-adjacent region matters because it will shape how readers classify LLM prompts, tests, instrumentation, and low-impact actions.

`Causal structure` might feel generic, but the postulate is generic. It is the root, not a specialty term. If a name here were too distinctive, it might make a physical fact sound like an AAD invention.

The segment's future-facing CIY claim also makes me think "yield" may be a tricky word. The causal information available from an action is not merely information gained after the fact; it depends on distinguishability of interventional outcome distributions. I should carry that into the CIY segment.
