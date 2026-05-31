# Reflection: der-gain-sector-bridge

**Segment:** `#der-gain-sector-bridge`

## What this does

The bridge theorem: gain-based update with directional fidelity (B1) → sector condition (GA-3). This tightens the theory's formal chain:

gain principle + B1 → sector condition → persistence, reserve, adversarial scaling

Key insight: For well-designed agents (optimal Bayesian, gradient on strongly convex loss), GA-3 is a CONSEQUENCE of the update geometry, not an independent postulate. The assumption load shifts from "this globally abstract property holds" to "this transparent checkable property holds."

Epistemic status: Conditional derivation (B1 or strong convexity is the irreducible condition).

## Naming relevance

Tracker row for "gain-sector bridge" — this is a named derived result. Let me assess:
- "Gain–sector bridge" is the right name. It names both things being bridged: the gain principle and the sector condition. "Bridge" is the right structural word for a result that connects two previously separate components.
- "Directional fidelity bridge" would be accurate but puts the premise in the name rather than the two connected components.
- "Update geometry theorem" is too abstract.

## Key concepts surfaced

**Directional fidelity (B1)**: Named condition δᵀHg(δ) ≥ c‖δ‖². This is the load-bearing premise. Whether it's in the tracker...

**Gain collapse as failure mode**: Segment explicitly lists gain collapse as a bridge failure mode (FM-2). Cross-validates the row 87 votes: gain collapse has multi-segment salience.

**Basin boundary = structural adaptation trigger**: "When mismatch exceeds R, the agent has been pushed out of its convexity basin — the correction function reverses direction and the sector condition fails. This IS the #result-structural-adaptation-necessity trigger." This is an important cross-segment derivation.

**Observability dominance**: Mentioned as FM-4 (unobservable directions). Named concept in tracker.

**Sub-scope α/β**: The two-scope taxonomy for when B1 holds structurally vs. empirically. Clean architectural concept.

**Fisher-metric cases**: Under parameterization invariance (PI) axiom + Čencov uniqueness theorem, matrix Kalman and exponential family sector constants are forced to the information metric, not chosen. This upgrades those rows from "conditional on choice of inner product" to "AAD-internally forced."

## What's excellent here

The two-point vs. one-point sector condition distinction is important:
- Two-point sector ⟺ strong convexity (bidirectional)
- One-point sector ⟸ strong convexity (one direction only)
- AAD's GA-3 is the one-point form — so strong convexity IMPLIES GA-3 but not conversely

The counterexample (x(1 + ½sin(10x)) satisfies x·L'(x) ≥ ½x² globally but L''(π/10) < 0) is correct and important. The one-point sector at equilibrium is strictly weaker than full local strong convexity.

The Fisher-layer additive-coordinate-forcing connection is important: the PI axiom + Čencov theorem forces the Fisher metric just as earlier additive axioms forced coordinate choices. The structural pattern (AAD-internal axiom + uniqueness theorem = forced coordinate) is named in #disc-additive-coordinate-forcing.
