# Reflection: §II AND/OR scope / strategy DAG / satisfaction gap / control regret (4 segments)

Covers `#scope-and-or`, `#def-strategy-dag`, `#def-satisfaction-gap`, `#def-control-regret`. **The strategy-DAG segment is the most substantive in §II so far** — it carries the Correlation Hierarchy (L0/L1/L1'/L2) as first-class content.

## Substantive observations

**(A) `#def-strategy-dag` is large and load-bearing.** Carries:
- DAG structure as derived from operational postulates + causal sufficiency (via `#deriv-graph-structure-uniqueness`'s CMC application)
- Acyclicity proved from temporal ordering (finite horizon)
- Single-parameter edges + AND/OR combination + status propagation algorithm
- **The Correlation Hierarchy: L0 (independence) / L1 (augmented DAG, strict prerequisites) / L1' (mixture form, soft facilitators) / L2 (full correlation)**
- The L1/L1' distinction is structurally important: strict prerequisites fold into the AND-prerequisite construction; soft facilitators require the mixture form. **L1' refuted under unobservable common cause** (Cramér-Rao floor / Fisher rank deficiency) — agent must augment $C$-observability or fall back to L0-on-marginals.
- Bias direction/magnitude table: AND-nodes underestimate by $+\rho$ (conservative); OR-nodes overestimate by $-\rho$ (optimistic). Same magnitude, opposite signs. Clean.

**(B) The two-gap diagnostic structure ($\delta_{\text{sat}}$ and $\delta_{\text{regret}}$) is well-handled.** The 2×2 cell map (capability limit / strategy problem / both / success) is genuinely useful. Each cell prescribes a distinct corrective action — exactly what makes the diagnostic actionable. Both segments explicitly contrast with active inference's EFE decomposition, which doesn't produce this disambiguation.

**(C) Convention-relativity propagation.** Both `#def-satisfaction-gap` and `#def-control-regret` honor the C1/C2/C3 convention from `#def-value-object`. Monotonicity hierarchies stated. **Good propagation discipline** — segments that depend on `#def-value-object` correctly inherit the convention-as-part-of-measurement framing.

**(D) Sun & Firestone 2020 "dark room" citation.** Cited in both `#def-satisfaction-gap` and `#def-control-regret`. The framework explicitly says "AAD's value-functional reformulation is AAD's own downstream architectural response to that diagnosis, not a move Sun & Firestone themselves propose." Honest credit positioning.

**(E) Cox 1946 + Jaynes 2003 cited** in `#def-strategy-dag`'s Epistemic Status for probability-from-desiderata. Standard and correct.

## Math verification

**Bias magnitudes (AND vs OR sibling-correlation):**
- AND: true $= \theta_1\theta_2 + \rho$; independence $= \theta_1\theta_2$; bias $= +\rho$ ✓
- OR: true $= 1 - (1-\theta_1)(1-\theta_2) - \rho$; independence $= 1 - (1-\theta_1)(1-\theta_2)$; bias $= -\rho$ ✓

The covariance enters with opposite signs — algebraically correct. AND-nodes benefit from positive correlation (joint success more likely than independence implies); OR-nodes suffer from positive correlation (the redundancy is illusory because failures cluster).

**Acyclicity from temporal ordering:** standard order-theoretic result. ✓

**Status propagation algorithm:** $O(|V| + |E|)$ topological-order forward pass. Correct.

## Voice violations

- `#scope-and-or`: no annotation
- `#def-strategy-dag`: no annotation (despite being large and substantive)
- `#def-satisfaction-gap`: no annotation
- `#def-control-regret`: no annotation

**Pattern observation:** the diff-voice violations cluster in the foundational §I segments. §II structural-content segments are mostly clean. Maybe this is because §II material is more recently written / promoted-from-spike and the discipline was actively enforced; §I material is older and inherited TFT-lineage notes.

## Felt value

**High magnitude on `#def-strategy-dag`.** The Correlation Hierarchy is the kind of structural-completeness move I find satisfying — the framework names L0 as tractable baseline, L1 as practical-for-strict-prerequisites, L1' as soft-facilitator extension with explicit identifiability boundary (refuted under unobservable common cause), and L2 as ideal/intractable. The four-level partition is honest about what's tractable and what isn't.

The 2×2 diagnostic cell map (sat × regret) is the kind of operational tool that justifies the "diagnostic core" framing of Section II. Each cell prescribes a different action — orient cascade.

## Continuing to next batch...

But first — Joseph asked how I'm feeling. Pausing the segment walk to address that directly.
