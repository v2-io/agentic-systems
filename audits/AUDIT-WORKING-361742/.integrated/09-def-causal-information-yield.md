# Reflection: def-causal-information-yield

**Segment:** `#def-causal-information-yield`

## What this does

Defines CIY as expected KL divergence between interventional outcome distributions: how distinguishable this action is from alternatives. Epistemic status is exact for the definition, discussion-grade for the CIY↔EIG approximation relationship.

The CIY vs. EIG distinction is load-bearing: CIY measures distinguishability (different distributions), EIG measures learning value (what the agent gains given its current uncertainty). They approximately coincide when U_M is high and diverge when U_M is low. The λ-weighting in the unified policy objective partially compensates — it suppresses CIY when the agent is already certain — but this compensation is heuristic, not derived.

## Naming relevance

Row 167: "causal information yield" vs alternatives. This is a coined term for a mathematically defined quantity. Let me assess:

- "Causal information yield" is the right name. "Yield" captures what I want — productive output from causal action. "Causal" is load-bearing (specifically interventional, not observational). The CIY abbreviation is clean.
- "Action-distinguishability" is what it literally measures, but that would be a less precise rename — it drops the information-theory framing. "Action-distinguishability" is an informal gloss, not a better name.
- "Interventional information gain" would collide with EIG (expected information gain), and the segment explicitly distinguishes CIY from EIG. Using "gain" for both would be confusing.
- "Causal info yield" (abbreviated) is just a shortened form — acceptable alias.

## New naming targets surfaced

**Query actions**: The segment has a full discussion of "query actions" as a qualitatively distinct action class (accessing external models). Tracker row would be for this concept. Checking whether it appears — "query actions" is used multiple times.

**Adversarial mirror / deception**: "The adversarial mirror: deception and model corruption" is a section header. This might be in the tracker.

**Grafting**: "incorporating external representational structure rather than building it de novo ('grafting')" — this is a named concept in the discussion. Needs to be voted on.

## What's excellent here

The EIG vs. CIY distinction is philosophically honest. The Discussion explicitly says the λ compensation "is heuristic (the λ form is not derived)." This is exactly the epistemic discipline the project requires. It also surfaces the "open direction" — proper EIG formulation — as an open research question rather than claiming it's settled.

The reference distribution dependence is correctly surfaced: CIY values are not comparable across different q choices. This is load-bearing for calibration.

## Wandering thoughts

The query-actions discussion implies a significant difference between probe-observe cycles and knowledge-transfer cycles. This maps to the TST cycle: most of software development IS querying external models (documentation, colleagues, StackOverflow). The "pre-compressed information" point is particularly good — you get the compressed output but face translation cost when frameworks don't align.

The adversarial mirror pointing to Lyapunov framing is a cross-segment dependency — the Lyapunov treatment is in sector-condition-stability. The coupling coefficient γ_A is the trust-weighted channel through which deception enters the dynamics. This is a non-trivial finding: deception-as-adversarial-disturbance gives it formal treatment.
