# Reflection: def-model-sufficiency

## What the segment does

Defines model sufficiency $S(M_t)$ as the fraction of predictive information retained by the model, with formal expression as a conditional mutual information ratio. Key moves:
1. Well-definedness clause (denominator > 0)
2. Boundary values (0, 1, partial)
3. Important Discussion notes about what sufficiency is NOT (causal validity, accuracy)

The well-definedness clause is careful and well-motivated: "predictive sufficiency is a property of a prediction task, and there is no prediction task to be sufficient for" in vacuous regimes.

## Naming targets surfaced

Row 68: "model sufficiency | Predictive informat..." — this is the defining segment for model sufficiency. I can vote on this now.

Let me check the card.

The candidate "Predictive information retention" sounds like a longer-form version of "model sufficiency." Let me look at the actual card entry.

## The sufficiency vs. accuracy distinction

This is subtle and important: a model can be sufficient ($S=1$) while being systematically *wrong* (biased observations). Sufficiency measures information retention (Level 1 completeness), not truth. The mismatch signal measures accuracy — a different concept.

This distinction has implications for the theory: you can have a model that perfectly retains all the predictive information in a biased dataset while still making poor predictions. The model is doing its job (compressing the history); the history itself is the problem.

## The causal validity gap

The Discussion raises something important: $S(M_t) = 1$ is *not sufficient* for Level 2 causal validity. A model that retains all predictive information (Level 1) may still fail at Level 2 queries ($P(o | do(a), M_t)$) unless the backdoor criterion is satisfied. The segment is careful to say "nearly sufficient" for agents with deterministic policies, with the remaining requirement being "no unmodeled external factor influences both action selection and outcomes."

This is the confounding problem in causal inference: observational sufficiency doesn't guarantee interventional validity. The segment is honest about this.

## The policy-relativity issue

$S(M_t)$ depends on which policy generates the future action sequence. An aggressive policy visits states the model can't predict; a conservative policy stays in the region the model knows well. This means sufficiency is not a property of the model alone — it's a property of the model-policy pair. This is an important caveat that has practical implications for model evaluation.

## Naming vote thoughts

"Model sufficiency" is clean and standard — it's the information-theoretic term of art. The candidate "Predictive information retention" is more descriptive but verbose. In prose, "the model's predictive information retention" would be unwieldy compared to "model sufficiency."

However, "model sufficiency" has a technical meaning in statistics (a sufficient statistic for a parameter family) that's related but not identical to this use. The potential for confusion with statistical sufficiency is low but non-zero.

Keep "model sufficiency" — it names the right concept and is the most concise form. The information-theoretic grounding is explained in the segment.

## Wandering thoughts

The trajectory-relativity clause is philosophically significant: $S(M_t)$ is indexed to *this agent's* specific chronica, not to a model-state equivalence class. Two copies of the same model exposed to different event streams have different sufficiency values measured against their own histories. This directly connects to the non-forkability of the chronica: there is no "the sufficiency of this model" — only "the sufficiency of this model relative to this trajectory."

This creates a methodological challenge for any claim like "transformer models have sufficiency X on task Y." Such a claim would need to be indexed to a specific interaction history, not just a model class. The policy-relativity and trajectory-relativity together make $S$ a complex quantity to aggregate across agents.

The scope-agent-identity connection (trajectory-indexed sufficiency) is explicitly noted: "AAD applies to agents instantiated on singular causal trajectories, and sufficiency is trajectory-indexed accordingly." This is the kind of cross-segment connection that makes the framework internally coherent.

How valuable: 6/10 for surprise (the causal validity gap and policy-relativity discussions are more nuanced than I expected), 8/10 for load-bearing.
