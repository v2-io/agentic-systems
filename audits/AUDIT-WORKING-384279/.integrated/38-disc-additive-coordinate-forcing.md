# 38 — disc-additive-coordinate-forcing (M3, forced-identity facet)

*Type: discussion. Status: discussion-grade. Stage: draft. Depends: [der-chain-confidence-decay, deriv-strategy-cost-regret-bound, deriv-edge-update-natural-parameter].*

## Predictions vs evidence
Predicted: 1-anchor-plus-3-theorem structure forcing coordinates. Found: that, plus a deeper unification — **the four layers are layer-specific manifestations of a single geometric object** (exponential-family Legendre-Fenchel geometry).

## Math verification
Five-element Legendre-Fenchel structure (line 22-29) correctly characterized:
1. Convex potential (negative entropy on $\Delta^{n-1}$)
2. Fenchel conjugate (log-partition function)
3. Primal-dual correspondence (softmax / log-odds map)
4. Bregman divergence (reverse-KL)
5. Riemannian metric (Fisher information = Hessian of dual potential $\nabla^2\phi^*$)

Standard information-geometry. ✓

Four-layer table (line 40-44) correctly maps:
- Chain → log-probability (Cauchy-FE)
- Divergence → reverse-KL (Cauchy-FE)
- Update → log-odds (Cauchy-FE)
- Metric → Fisher (Čencov 1982)

All forced via uniqueness theorems on AAT-internal axioms. Consistent with `#scope-agent-identity`'s (PI) axiom and `#der-gain-sector-bridge`'s Fisher-metric upgrade.

## The floor-vs-coordinate-forcing distinction (line 58-64) — methodologically important

The heteroscedastic-Gaussian no-go ($C \to +\infty$ under arbitrary parameter norms) is correctly classified as a **downstream theorem of the (PI) commitment**, not as an identifiability-floor instance. Three structural differences:
1. **External-theorem role:** floor = theorem-forbids-task; coordinate-forcing = theorem-forces-uniqueness-of-escape.
2. **Escape count:** floor = ≥2 structurally distinct escapes; coordinate-forcing = exactly 1 escape (uniqueness is the content).
3. **Consequence:** floor elevates new machinery to load-bearing; coordinate-forcing re-uses already-load-bearing commitment.

This is the kind of careful structural distinction that prevents classification errors downstream. **Worth noting positively in §E.**

## Cross-segment consistency
Forward-refs `#der-chain-confidence-decay`, `#deriv-strategy-cost-regret-bound`, `#deriv-edge-update-natural-parameter`, `#der-gain-sector-bridge`, `#deriv-observation-ambiguity-bias-bound`, `#disc-identifiability-floor`, `#disc-stability-certificate`. Coherent.

The (PI) axiom is consistent across:
- `#scope-agent-identity` (introduces (PI) on singular trajectories)
- `#der-gain-sector-bridge` (uses (PI)+Čencov to upgrade Fisher-metric-natively)
- This segment (catalogs (PI) as the metric-layer instance of the four-layer pattern)

Cross-segment consistency holds.

## Prose-coherence — strong
- The "previously appeared as 1-anchor-plus-3-theorem" framing (line 13) acknowledges historical landing; the "deeper structural reality" is the four-layer unification.
- "The convergence across independent axioms is itself the meta-pattern's substance — not a byproduct to be compressed into a single axiom" (line 50) — explicit methodological commitment.
- Adjacent cases that share the shape but not the forcing structure (Lyapunov quadratic, variance-additive, IB Lagrangian) cleanly distinguished. Avoids over-claiming reach.

## Watch list
- Lyapunov quadratic reclassification (line 70-73) — "the coordinate is *chosen* (via converse-Lyapunov existence), not uniquely *forced* by an AAT-internally-motivated additivity axiom." Methodologically precise.

## Next-segment predictions
`#disc-constructive-impossibility-posture`. Style claim — three-move discipline (name the floor / name the escape / treat the no-go as apparatus). Will catalog the constructive-impossibility instances across the three clusters (identifiability-floor / value-functional-grounding-floor / implementation-impossibility).

## Brief wandering

**On the four-layer Legendre-Fenchel unification.** This is one of the framework's most ambitious structural recognitions. The claim that AAT's four separately-motivated coordinate forcings (chain, divergence, update, metric) all probe the same exponential-family geometry — and that the convergence across independent axioms is the substance — is methodologically rich. The framework is essentially saying: "we didn't design these to all force the same geometry; the geometry showed up four times because the framework's commitments imply it."

**On the floor-vs-forcing taxonomy.** The three-element distinction (external-theorem role / escape count / consequence) is precise and falsifiable. Future segments classifying a no-go can run the test and place it correctly. The heteroscedastic-Gaussian example is a clean worked instance — looks like a floor, fails the three-element test, lands correctly as a downstream theorem of (PI). Good methodological model.
