# Reflection: #result-mismatch-decomposition

**Stage:** claims-verified. **Status:** exact. **Type:** result. **Depends:** [def-mismatch-signal, def-observation-function, def-action-transition, form-agent-model, scope-adaptive-system].

## Dependency check

All upstream. ✓

The equation tag `*[Derived (result-mismatch-decomposition, Prop 5.1 from TFT)]*` references TFT's Prop 5.1 in the from-clause. **This is *not* a diff-voice violation** — the from-clause is the standard place for source citations in equation tags. Different from the Discussion-section "(Descended from TF-XX)" pattern I've been tracking.

## Predictions vs evidence

Predicted bias-variance-style decomposition under GA-1. Got it: $\mathbb{E}[\|\delta_t\|^2] = \mathbb{E}[\|\hat o_t - \bar o_t\|^2] + \mathbb{E}[\text{Var}(o_t \mid \Omega_t, a_{t-1})]$.

The honest "**alignment assumption**" caveat in Discussion ("under an alignment assumption (the lost information affects the one-step conditional mean), this implies positive model error") is appropriately careful — without alignment, insufficiency need not imply positive one-step mean error.

## Cross-segment consistency

Forward-refs `#emp-update-gain`, `#def-model-sufficiency`. Discussion-grade.

No "(Descended from TF-XX)" annotation here.

## Math verification

Manual derivation:
- $\delta_t = (o_t - \bar o_t) + (\bar o_t - \hat o_t)$
- $\|\delta_t\|^2 = \|o_t - \bar o_t\|^2 + 2(o_t - \bar o_t)^T(\bar o_t - \hat o_t) + \|\bar o_t - \hat o_t\|^2$
- Cross-term: $\mathbb{E}[(o_t - \bar o_t) \mid \Omega_t, a_{t-1}] = 0$ by definition of $\bar o_t$. By GA-1 (fresh noise: $\varepsilon_t \perp \mathcal{C}_{t-1} \mid \Omega_t, a_{t-1}$), conditioning on $\mathcal{C}_{t-1}$ doesn't change this. Cross-term $\to 0$.
- $\mathbb{E}[\|\delta_t\|^2] = \mathbb{E}[\|o_t - \bar o_t\|^2] + \mathbb{E}[\|\bar o_t - \hat o_t\|^2]$
- First = observation noise; second = model error. ✓

Standard bias-variance under fresh-noise assumption. Correct.

The segment's note "This is orthogonality (uncorrelated), not independence" is a small piece of mathematical precision worth surfacing — the cross-term vanishing requires only zero conditional mean, not full independence.

## What direction next

`#emp-update-gain` — the update-gain principle, $\eta^\ast = U_M / (U_M + U_o)$ Kalman-style ratio.

## Errors to watch for

- The "alignment assumption" caveat. If downstream segments use $S(M_t) < 1 \Rightarrow$ positive model error without invoking alignment, that's drift.

## Predictions for next segments

`#emp-update-gain`: optimal gain as ratio of model uncertainty to total uncertainty: $\eta^\ast = U_M / (U_M + U_o)$. The Kalman case is the canonical exemplar.

## What would I change

Nothing structural. This is a clean result with honest caveats.

## Curious about

Whether the framework develops the score-function variant of the decomposition. The prediction-error decomposition $\delta_t = (o_t - \bar o_t) + (\bar o_t - \hat o_t)$ has a natural score-function counterpart (Fisher-info decomposition). If the framework needs it for non-vector observations, this segment may need a companion.

## What new knowledge does this enable

- The reducible/irreducible split as the structural foundation for understanding what gain *does* (separates model error from noise).
- The observation that "trying to eliminate all mismatch" is overfitting — gives a structural rationale for why aggressive learning rates fail in noisy environments.

## Should the audit process change

No.

## Outline changes for FINAL

No.

## Felt value

**Mid magnitude.** Clean result, well-derived, honest about the alignment caveat. Confirmatory rather than surprising — bias-variance decomposition is universally known — but the framework integrates it cleanly with its own machinery (sufficiency, gain).

## What the framework now potentially contributes

The reducible/irreducible split sets up the gain principle's role precisely: gain is the operator that separates signal from noise in the mismatch. Without this decomposition, the gain principle would be unmoored. With it, gain has a clear structural job.

## Wandering thoughts

This is a foundational result that the framework needs but doesn't claim to invent. The TF-citation in the equation tag (Prop 5.1 from TFT) is appropriate — TFT had this result; AAD inherits it cleanly.

A useful Brief-style gloss: "the model can chase its own predictions to perfect fit on observation noise, which is *worse* than partial fit on the true signal. The persistence-condition machinery uses this to derive *why* aggressive update gain fails in noisy environments." That's the substantive insight; the math is the proof.

Continuing to `#emp-update-gain`.
