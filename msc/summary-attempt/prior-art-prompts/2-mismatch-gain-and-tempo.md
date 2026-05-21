Please conduct a deep prior-art search across academic literature. We are establishing scientific precedence for a theoretical framework of agency (AAT).

## The Core Idea / Claim
The agent adapts by decomposing its prediction mismatch into reducible (model error) and irreducible (observation noise) components. The optimal proportion of mismatch applied to correct the model is the ratio of model uncertainty to total uncertainty (an extension of the Kalman gain to non-linear/information-geometric spaces). Consequently, an agent's true capacity—its "Adaptive Tempo"—is a single metric defined as the product of its event rate (loop speed) and its update gain (information quality).

## Boundaries of the Claim
- Domain: Adaptive control theory, online learning, machine learning theory, information geometry.
- Assumptions: Systems with non-trivial noise where 100% update gain leads to overfitting.

## What Kind of Match Counts
- Formal mathematical decompositions of prediction error into epistemic (reducible) vs aleatoric (irreducible) parts used specifically for real-time agent adaptation.
- Generalizations of the Kalman gain (uncertainty ratio) to nonlinear, non-Gaussian, or natural gradient operators.
- Literature that defines a capacity metric mathematically identical or similar to "Adaptive Tempo": explicitly multiplying cycle speed by update quality/gain.

## What Would NOT Count
- Standard deep learning gradient descent papers that don't track uncertainty or distinguish error types.
- Purely hardware-based "clock speed" metrics that don't factor in the epistemological *quality* of the update.
- Generic Kalman filtering papers that just apply the filter to linear-Gaussian systems without extending the theory to general cognitive/agentic update limits.

## Known Anchors
- Kalman Filter / Extended Kalman Filter
- Fisher Information / Information Geometry (Amari)
- OODA loop formalizations (Boyd)
- Epistemic vs Aleatoric uncertainty in Deep Learning

## Search Scope
- Both close mathematical matches and broader conceptual predecessors.
- Strictly academic papers (no patents/IP).