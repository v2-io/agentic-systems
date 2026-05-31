# Reflection: post-causal-structure

## What the segment does

Postulates that the agent-environment interaction has irreducible causal structure from temporal ordering. The key claim: "event A can be a cause of event B only if A temporally precedes B" — the most primitive notion of causality, weaker than statistical notions.

The segment then derives four structural consequences:
1. Model update is directed (depends on prior, not future events)
2. Mismatch is retrospective (prediction-before-vs-observation-after)
3. Action selection is prospective (influences future)
4. Chronica is monotonically growing

## Naming targets surfaced

Nothing obviously new in the tracker from this segment. The Greek vocabulary (chronica, etc.) is already handled. The concept of causal structure is central but probably not a voting target by itself.

Wait — let me check row 94: "extreme transition motif" — this is a concept from Miller's automata. Not directly related to this segment.

Row 89: "causal information yield | CIY..." — the segment introduces CIY as a concept but the formal definition is deferred to `#def-causal-information-yield`. I'll vote on that term when I read the defining segment.

## The strong/weak/nominal/zero coupling taxonomy

The segment introduces a four-level taxonomy of coupling strength:
- Strong coupling: rich interventional information
- Weak coupling: sparse interventional information
- Nominal coupling: agent's query actions generate weak contrasts
- Zero coupling: no Level 2 access, falls outside agency scope

This is an interesting intermediate case: "nominal coupling" where the agent's *choice of what to observe* generates weak interventional contrasts. So even an agent that can't manipulate the environment has some Level 2 access if it can choose which question to ask. This is the active observation case again.

## Cross-segment notes

The segment references `#def-causal-information-yield` and `#def-mismatch-signal` which come later in the OUTLINE. These are forward references in Discussion, acceptable since they're not in `depends:`.

## The "zero coupling" edge case

Zero coupling agents are "outside agency scope but within adaptive scope." This is a clean categorization: passive observers with no causal effect satisfy adaptive scope (they observe under uncertainty) but not agency scope (their choices make no difference). The temporal ordering still holds — their chronica is well-defined — but without interventional contrast, Sections II and III don't apply.

This raises an interesting question: can a passive Bayesian learner be described as having a "strategy" in the AAD sense? The answer from the scope conditions is no — strategy ($\Sigma_t$) requires agency scope. A purely passive observer can have a model ($M_t$) and even a goal ($O_t$) in some informal sense, but the complete agent state $X_t = (M_t, G_t)$ only makes sense when actions can make a difference.

## Wandering thoughts

The most primitive causality notion (temporal ordering) is prior to statistical notions. This is philosophically important — it means the theory doesn't rely on the probabilistic framework to ground causality. The temporal ordering is the bedrock; everything probabilistic is built on top.

There's an interesting contrast here with Pearl's framework, where causality is modeled through structural causal models (SCMs) independently of temporal ordering (you can have cyclic SCMs, which violate strict temporal precedence). AAD's more primitive grounding of causality in temporal ordering might create a tension with cyclic causal models. The segment doesn't address this, but it's worth noting.

The four consequences (directed, retrospective, prospective, monotonically growing) map beautifully onto the Greek cycle phases:
- Directed update → Epistrophe (turning toward)
- Retrospective mismatch → Aporia (the signal comes after the prediction)
- Prospective action → Praxis (acting to influence future)
- Monotonically growing chronica → the causal substrate for Prolepsis (the model built from history)

This mapping between the causal structure and the cycle phases is elegant. I wonder if it's made explicit anywhere in the theory — it would be a nice pedagogical connection.

How valuable: 5/10 for surprise, 7/10 for load-bearing. The temporal ordering claim is well-motivated but the four coupling levels and the philosophical grounding are the most valuable parts.
