# 13 — def-model-class-fitness

*Type: definition. Status: axiomatic. Depends: [def-model-sufficiency].*

## Predictions vs evidence
Predicted: $\mathcal{F}(\mathcal{M}) = \sup_{M \in \mathcal{M}} S(M_t \mid \ldots)$. Found: exactly that — supremum of sufficiency over the model class.

## Math verification
$\mathcal{F}(\mathcal{M}) = \sup_{M \in \mathcal{M}} S(M)$. ✓ Note: the segment writes $S(M)$ not $S(M_t)$ here — implicit that we're considering models as representational objects rather than as time-indexed states. Reasonable.

Structural inadequacy condition: $\mathcal{F}(\mathcal{M}) < 1 - \varepsilon$. Clean.

## Prose-coherence
Bias-vs-variance parallel (lines 12, 36) is the right pedagogical analog. The "agent cannot directly compute fitness" insight (lines 14, 38) — persistent mismatch despite adequate learning as the observable signature — is methodologically clean.

## Cross-segment consistency
Forward-ref to `#result-structural-adaptation-necessity` — Ch.4 segment. Will verify the structural-inadequacy-as-trigger relationship there.

## Watch list
- Trigger setup: when I reach #result-structural-adaptation-necessity, check that the $1 - \varepsilon$ threshold matches the segment's actual development of the result.

## Next-segment predictions
End of Ch.2. Ch.3 starts with `#the-cycle-in-motion-intro` (chapter intro). Then formal claims (form-event-driven-dynamics, der-recursive-update, der-action-selection, def-mismatch-signal, result-mismatch-decomposition, emp-update-gain, def-causal-information-yield, def-adaptive-tempo, hyp-mismatch-dynamics).

## What I'd change
Nothing. Clean segment.

## Brief wandering
**On the bias-variance parallel as pedagogical scaffolding.** Saying "class fitness = bias; instance sufficiency = bias + estimation quality" is exactly the kind of bridge that helps practitioners coming from ML. The framework's whole pedagogical strategy is to root each abstract object in a domain-familiar analog (Kalman filter, Brooks's Law, etc.), and this segment does it well.
