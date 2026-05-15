# 12 - def-model-sufficiency

Segment: `01-aat-core/src/def-model-sufficiency.md` (`#def-model-sufficiency`)

Dependencies: `form-agent-model`, `form-information-bottleneck`, `def-action-transition`, all read. Dependency-order check passes.

## Segment Read

This segment defines $S(M_t)$ as the fraction of predictive information retained by the model relative to the full chronica. The numerator is predictive information still available in $\mathcal C_t$ beyond $M_t$; the denominator is total predictive information in the full history. $S=1$ means sufficient statistic for prediction; $S=0$ means no predictive information retained.

The discussion is careful about what sufficiency is not: not accuracy, not causal validity, not policy-invariant, and not trajectory-invariant. This is a definition with many guardrails.

## Predictions Vs Evidence

I predicted model sufficiency would make the compression story operational. It does. The strongest nuance is the distinction between sufficiency and accuracy: a model can retain all predictive information available in a biased history and still be wrong about reality.

The trajectory-relativity paragraph is also stronger than I expected. It links model sufficiency back to chronica and identity: sufficiency is not a population property of a state object divorced from its causal history.

## Cross-Segment Consistency

This segment cleanly extends `#form-agent-model` and `#form-information-bottleneck`. It also preserves the Pearl hierarchy distinction from the previous segment: predictive sufficiency is Level 1 and does not imply Level 2 causal validity.

The forward reference to `#def-value-object` for backdoor/causal validity is downstream, but it is framed as a later condition rather than a prerequisite for defining $S$.

## Naming Notes

`model sufficiency` is strong and should be kept. It is technical but self-descriptive: how sufficient the model is relative to the prediction task.

This segment also grounds "trajectory-indexed sufficiency" as a possible named qualifier. If the tracker has a target for sufficiency against a single causal record, this segment supports it. The phrase is more precise than "personalized sufficiency" or "agent-relative sufficiency" because chronica's causal trajectory is the point.

The distinction "sufficiency vs accuracy" may be worth preserving in notes for future targets, but I do not expect a separate name unless the card explicitly has one.

## What This Enables

This enables model class fitness, structural adaptation necessity, and any later claims about context turnover or reconstructed model adequacy. It gives the framework a scalar way to talk about compression loss before truth/accuracy enters through mismatch.

For naming, it supports a family:

- `model sufficiency` for retained predictive information in the current model
- likely `model class fitness` for best achievable sufficiency in a model class
- `mismatch` or accuracy terms for truth-relative error

Those should not be conflated.

## Watchlist

- Candidates that rename sufficiency as accuracy or truth.
- Uses of $S(M_t)$ without policy or prediction-task context.
- Aggregated sufficiency claims across copied models without trajectory qualification.

## Wandering Thoughts

The definition is more subtle than the name suggests. "Sufficiency" in ordinary language can sound like adequacy in all respects. Here it is adequacy of compression for a prediction task, which is narrower. The segment does enough guardrail work that the name remains safe.

I particularly like the "not truth" distinction. An agent can compress its biased sensor history perfectly and still be wrong. That makes mismatch and sufficiency orthogonal in a useful way: one asks whether the compression retained what history knew; the other asks whether what it predicts survives contact.

The trajectory-relativity point makes chronica feel even more load-bearing. If two agents share $M_t$ but diverged in chronica, model sufficiency is not simply "same state, same score." The score is measured against the causal record that the state compressed. That is a strong reason to keep the `chronica` vocabulary.

For voting, I should be careful with names that imply sufficiency is a static property of $M_t$ alone. The notation $S(M_t)$ is compact, but the prose should often remind readers of policy/task/trajectory relativity.
