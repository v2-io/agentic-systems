# Reflection: def-model-class-fitness

## What the segment does

Defines model class fitness $\mathcal{F}(\mathcal{M})$ as the supremum of sufficiency over the model class. The key distinction: $S(M_t)$ is about a specific model; $\mathcal{F}(\mathcal{M})$ is about the ceiling of what's achievable within the class.

The bias/variance parallel is explicit: class fitness is about bias (is the model class the right one?); instance sufficiency is about both bias and estimation quality.

## Naming targets surfaced

Row 96: "model-class fitness | Class capacity ceil..." — this is the target. Let me look at the candidates.

The "class capacity ceiling" candidate in the tracker is interesting — it names what model class fitness *is* (the ceiling of the class's capacity).

## The detection problem

The Discussion's key practical point: the agent can't directly compute $\mathcal{F}(\mathcal{M})$ — it would need to search the entire class. So how does it detect low class fitness? The answer: "persistent mismatch despite adequate learning." This is an empirical signature, not a computation.

This has important implications for learning systems: a system that has converged its parameters but still has persistent mismatch is likely hitting a class fitness ceiling, not just under-learning. The correct response is structural change (different model class), not more training.

## Naming thoughts

"Model class fitness" is descriptively accurate — how "fit" (adequate) the model class is for the prediction task. But "fitness" has a strong association with evolutionary/biological fitness, which is different from what's meant here. Could create confusion in certain contexts.

"Class capacity ceiling" is more literal — the maximum achievable — but loses the "fitness" connotation of adequacy/match-to-purpose.

"Representational capacity" is another natural candidate — what the model class can represent. But capacity is often used for model *size* in ML (parameter count), which collides.

I'll look at the full card entry for row 96.

## Cross-segment notes

The segment points forward to `#result-structural-adaptation-necessity` as where the consequences of low fitness are developed. No backward violations.

## Wandering thoughts

The bias-variance parallel is illuminating. In classical ML, we talk about bias (model class limitation) and variance (estimation noise). Here, $\mathcal{F}(\mathcal{M})$ is the bias concept: the fundamental limit of what the class can represent. $S(M_t)$ combines both: how much of that class maximum is being achieved in practice.

But there's a subtlety: in classical ML, we can in principle compute the bias by knowing the true data-generating distribution. In AAD, the agent can't compute $\mathcal{F}(\mathcal{M})$ without access to the true environment dynamics — which is exactly what the theory says the agent doesn't have. So class fitness is a conceptual quantity that the agent has to *infer* from behavior, not compute directly.

This creates an interesting epistemological situation: the agent needs to estimate whether it's hitting a class fitness ceiling, but it can only see its own performance history. The "persistent mismatch despite adequate learning" diagnostic is the practical proxy for what is in principle a theoretical quantity. There's a question of whether this diagnostic is *reliable* — whether it correctly distinguishes "hitting class ceiling" from "still learning" or "the environment changed."

How valuable: 5/10 for surprise (this follows directly from model sufficiency), 7/10 for load-bearing (the class fitness / instance sufficiency distinction is architecturally important).
