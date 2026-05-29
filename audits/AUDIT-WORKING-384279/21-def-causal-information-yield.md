# 21 — def-causal-information-yield

*Type: definition. Status: exact. Depends: [der-action-selection, def-mismatch-signal].*

## Predictions vs evidence
Predicted: action-information measure using do-calculus. Found: $\text{CIY}(a; M) = \mathbb{E}_{a'\sim q}[D_{KL}(P(o \mid do(a), M) \| P(o \mid do(a'), M))]$ — expected KL between interventional outcome distributions. Plus the important methodological distinction CIY ≠ EIG (distinguishability vs learning-value).

## Math verification
- $\text{CIY} \geq 0$ by construction (expected KL is non-negative). ✓
- $\text{CIY} = 0$ for passive observers (no do-effect on outcomes). ✓
- $\text{CIY} > 0$ iff actions causally alter outcomes (Pearl Level 2). ✓
- The $\lambda$-weighting heuristic for the unified policy objective is honestly named as heuristic, not derived.

## Pearl-as-external convention restated (second articulation)
Line 27 again articulates the convention I tracked earlier: "$do(\cdot)$ operator is Pearl's standard intervention notation ... the AAT recapitulation lives at #def-pearl-causal-hierarchy in Part II Ch.2, where the framework deploys the hierarchy operationally." Two segments now articulate this — convention is becoming canonical-by-repetition.

## Prose-coherence
- CIY-vs-EIG distinction (line 35) is well-articulated and methodologically important.
- Open direction on proper EIG (line 41) is honest — names what would be a stronger formulation and what makes the current $\lambda$-weighted CIY surrogate tractable.
- Reference-distribution $q$ degree-of-freedom flagged (line 43); default = policy-induced.
- The adversarial mirror section (line 55) is a nice connection — same channel enables cooperation + deception; CIY can be positive in the strict sense even when the content is deceptive.

## Cross-segment consistency
Forward-refs `#def-pearl-causal-hierarchy`, `#disc-ciy-unified-objective`, `#form-information-bottleneck`, `#hyp-communication-gain`, `#result-structural-adaptation-necessity`, `#result-sector-condition-stability`, `#der-adversarial-destabilization`. All coherent.

## Watch list
- The "$\lambda \to 0$ when $U_M$ low" claim makes CIY behave like EIG. The $\lambda$ form is heuristic; need to verify when I reach `#disc-ciy-unified-objective`.

## Next-segment predictions
`#def-adaptive-tempo`. Will formalize $\mathcal{T} = \sum_k \nu^{(k)} \eta^{(k)*}$ as the central capacity variable. Per chapter intro this is the chapter's load-bearing object. Status likely robust-qualitative or empirical.

## Brief wandering
The CIY/EIG distinction is the kind of methodological precision that compounds. Frameworks that conflate "distinguishability" with "informativeness" produce exploration policies that probe meaninglessly in well-known regions. The framework's choice to be honest about this (CIY-as-surrogate-for-EIG with $\lambda$-uncertainty-gating) is honest *and* leaves room for the future EIG formulation it names as open.

The adversarial-mirror treatment is a nice bridge to Part III — same machinery, opposite sign of coupling.
