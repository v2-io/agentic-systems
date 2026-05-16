# Reflection: scope-agency

## What the segment does

Narrows from adaptive scope to agency scope by adding:
1. At least binary choice ($|\mathcal{A}| \geq 2$)
2. At least one action with causal effect (distinct interventional outcome distributions)

The second condition is the interesting one — it uses Pearl's $do(\cdot)$ operator to require *interventional* contrast. An agent whose choices make no observational difference (nominal agent) is in adaptive scope but not agency scope.

## The interventional requirement

The segment explicitly frames condition 4 using Pearl's intervention operator. This is the first formal appearance of the Pearl hierarchy — it appears in a *scope condition*, not just in a definition. The framework is requiring that agency scope be defined *in terms of* whether the agent can generate Level-2 causal data.

This is architecturally important: the causal hierarchy isn't an optional enrichment but a boundary condition for when Section II results apply. The agency scope is where Pearl Level 2 access *becomes possible*; the loop-interventional-access segment later will show the feedback loop *provides* that access.

## Naming targets surfaced

Searching tracker for "agency"... Row 79 shows "aporia prolepsis aisthesis epistrophe praxis | Greek rooted vocabu..." which seems to be the Greek vocabulary cluster. But "agency" itself — let me check if there's a target for the scope-agency subject-noun.

The card target would be about "agency" as a subject-noun, but I suspect the naming vote here is about whether "agency" is the right subject-noun for this scope. It's reasonably precise — "agency" names the condition of being an agent-with-causal-effect. The scope could alternatively be called "causal agency" or "interventional scope" but "agency" as a lone word has communal-imagination potential.

## Cross-segment notes

The segment references `#der-loop-interventional-access` as a forward dependency — the *why* of the causal-effect condition is explained there, but the condition itself is defined here. This creates an interesting pedagogical dependency: the reader is asked to accept the condition before seeing why it's necessary. The segment handles this by listing the uses ("required for...") without requiring those segments to exist yet.

## The "nominal agent" category

"Nominal agents" appear again — agents whose choices make no difference. This is a philosophical ghost in the machinery: an agent with action space but no causal purchase. Such entities are in adaptive scope but outside agency. 

The name "nominal agent" is good — it has the right "name only" connotation. Worth noting that this is used twice (also in scope-adaptive-system) as an informal term, without a formal segment definition. If the framework uses this concept repeatedly, it might warrant its own definition or at least a tracked name.

## Wandering thoughts

The binary-choice condition ($|\mathcal{A}| \geq 2$) is notable for what it excludes. A single-action agent (one that can only do one thing, or chooses not to act) is outside agency scope. Even if that action has causal effect, the agent has no *contrast* to compare it to. You can't learn from interventions if you can only perform one intervention.

This connects to exploration: without the ability to choose between options, there's nothing to explore. The agency scope is where exploration becomes conceptually possible.

The condition $P(o | do(a)) \neq P(o | do(a'))$ for some $a \neq a'$ is weaker than "all actions have distinct effects" — just *one* contrast pair is enough. This seems like the minimal reasonable condition: even if 99% of your actions are equivalent, if one pair distinguishes, you're in agency scope. This feels right for generality.

How valuable: 5/10 for surprise (expected this scope definition), 8/10 for load-bearing (gates all of Section II and III).
