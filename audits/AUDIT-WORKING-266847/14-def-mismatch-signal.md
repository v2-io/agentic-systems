# Reflection: def-mismatch-signal

## What the segment does

Defines the mismatch signal $\delta_t = o_t - \hat{o}_t$ (prediction error) as the primary signal driving adaptation. Also defines the score-function mismatch for probabilistic models. The key philosophical framing: mismatch as "aporia" — productive perplexity that is generative.

## Naming targets surfaced

The mismatch signal is named here — "mismatch" or "aporia" or "prediction error." The segment doesn't appear to be a direct voting target in my card (let me check). Searching tracker for "mismatch"... 

Row 32: "[Concept] The cumulative prediction error that an agent has tolerated without updating its model | Mismatch accumulati..." — not the mismatch signal itself, but accumulated mismatch.

Row 99: "mismatch injection rate ($\rho$) | Mismatch injection r..." — $\rho$ is the disturbance rate, not the signal itself.

The mismatch signal ($\delta_t$) is probably not a naming target in its own right — it's already named and the Greek term "aporia" is established for the cycle phase. But there might be related targets.

## The zero-aporia ambiguity

The Discussion's most important practical insight: $\delta_t \approx 0$ doesn't mean the model is adequate. Three interpretations:
1. Model genuinely reflects reality (desirable)
2. Confirmation bias (agent only observes what model predicts well)
3. Observation channel too noisy to detect model errors

This tripartite distinction is valuable for diagnosing systems. "An agent without aporia is an agent that has stopped adapting — but silence can mean peace or deafness." This is a good line.

## The score-function generalization

The extension to score-function mismatch $\tilde{\delta}_t = \nabla_M \log P(o_t | M_{t-1}, a_{t-1})$ is mathematically elegant — it lives in the model's tangent space, pointing toward higher likelihood. Under Gaussian models, it coincides with $\delta_t$ up to scaling.

This generalization is important for modern probabilistic models (transformers, Gaussian processes) where the prediction is a distribution, not a point. The score function is the natural gradient direction.

## Cross-segment notes

The segment references `#result-persistence-condition`, `#result-sector-condition-stability`, and `#result-mismatch-decomposition` — all downstream. No violations.

## Naming thoughts for the mismatch concept

"Mismatch" is a good name — it's plain English, evocative, and self-descriptive. "Prediction error" is the ML term-of-art. "Aporia" is the Greek cycle phase name.

The relationship between these three names is interesting: "mismatch" is the formal name for $\delta_t$; "aporia" is the cycle phase name for *the experience of* mismatch; "prediction error" is the ML synonym. The framework distinguishes them usefully.

## Wandering thoughts

The Mahalanobis distance normalization is noted casually in Discussion: $\|\delta_t\|_\Sigma = \sqrt{\delta_t^T \Sigma^{-1} \delta_t}$ maps prediction error to dimensionless surprise-equivalent units. This is technically important for the subsequent mismatch dynamics (the dynamics should be in consistent units), but it's handled as a notational aside rather than a formal requirement. 

For the persistence condition to be dimensionally consistent, the mismatch norm must be comparable to the correction rate $\alpha$ and disturbance rate $\rho$. The Mahalanobis normalization is what ensures this — without it, the persistence condition would be mixing units. Worth flagging that this normalization is load-bearing for the dynamics even though it's stated informally.

The "active testing" pointer to CIY is interesting — the mismatch signal is not just a passive indicator but can be deliberately provoked through CIY-maximizing actions. This connects the observation-driven and action-driven aspects of adaptation.

How valuable: 5/10 for surprise (mismatch signal is expected), 8/10 for load-bearing (all subsequent dynamics depend on this definition).
