# 18 — def-mismatch-signal

*Type: definition. Status: axiomatic. Depends: [form-agent-model, def-observation-function, def-action-transition].*

## Predictions vs evidence
Predicted: $\delta_t = o_t - \hat o_t$ with score-function variant. Found: exactly that, plus the **zero-aporia ambiguity** discussion (three readings of small $\delta$: model-right / confirmation-bias / channel-too-noisy).

## Math verification
- $\delta_t = o_t - \hat o_t$ with $\hat o_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$. ✓
- Score-function: $\tilde\delta_t = \nabla_M \log P(o_t \mid M_{t-1}, a_{t-1})$, lives in $T_M\mathcal{M}$. ✓
- Mahalanobis normalization: $\|\delta_t\|_\Sigma = \sqrt{\delta_t^T \Sigma^{-1} \delta_t}$. Correct for converting physical units to surprise-equivalent. ✓

## Prose-coherence
The zero-aporia ambiguity is well-articulated — names the three readings clearly and uses the "silence can mean peace or deafness" framing as a sharp pedagogical anchor. Strong.

## Cross-segment consistency
Forward-refs `#result-persistence-condition`, `#result-sector-condition-stability`, `#result-mismatch-decomposition`, `#def-causal-information-yield`, `#emp-update-gain`. All coherent.

## Watch list
- $g$ transform type-overloading: $\mathcal{O} \to T_M\mathcal{M}$ (prediction-error case) and $T_M\mathcal{M} \to T_M\mathcal{M}$ (score-function case). Context disambiguates; not a finding.

## Next-segment predictions
`#result-mismatch-decomposition`. Will decompose $\delta_t$ into reducible (model error) + irreducible (observation noise) parts. Probably exact. The irreducible noise floor is methodologically important for setting "structural ceiling" claims.

## Brief wandering
The "zero-aporia ambiguity" point is one of those small methodological gems that the framework should — and apparently does — reuse. Active testing as a response to ambiguity-of-silence is a deep idea: the agent doesn't know if it's right or just inadvertently uninformed, and the resolution is to deliberately probe. This is exactly the role CIY will play.
