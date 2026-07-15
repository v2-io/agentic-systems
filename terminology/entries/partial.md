---
slug: partial
schema_version: 1
term: Partial
name: 'Class 2: Partial (GUC)'
brief: GUC Class-2 value; agent with bounded goal-update coupling — directed separation is approximated with a computable residual leakage rate $\kappa_{\text{processing}} \in (0, \kappa_{\max})$.
layer: framing-vocabulary
status: canon
tags:
- structural_concepts
- agent_classes
source_type: asf
primary_source: 01-aat-core/src/der-directed-separation.md
first_asf_mention: 01-aat-core/src/der-directed-separation.md
see_also:
- goal-update-coupling-class
- directed-separation
- separated
- coupled
- class-coercion
- wrapping-regime
aliases:
- GUC-Partial
- Class 2
- Class-2 agent
do_not_confuse:
- partially modular (pre-2026-05-09 label for this same value, retired as GUC-axis
  label in the 2026-05-09 rename; Class 3 pre-rename)
- partial wrapping / W₂ (a wrapping-regime value describing how structural separation
  is implemented, not directly a GUC class label — though W₂ composites fall in the
  Class-1-by-behavior cell, not Class 2)
- partial information (information-theoretic concept; no GUC-axis connection)
seq: 2
---

**Class 2: Partial** is the middle value on the [Goal-Update Coupling Class](goal-update-coupling-class.md)
axis — the "structured repair" cell in the meta-pattern table of
[`#disc-separability-pattern`](../../01-aat-core/src/disc-separability-pattern.md). A Partial agent has bounded goal-update coupling: $\kappa_{\text{processing}} \in (0, \kappa_{\max})$, where
$\kappa_{\text{processing}}$ is defined in
[`#der-directed-separation`](../../01-aat-core/src/der-directed-separation.md) as the processing coupling coefficient. The bound is computable, making the residual leakage rate formally tractable.

Partial agents violate directed separation, but not irreducibly. The coupling is present and measurable. Part II results that depend on directed separation apply approximately rather than exactly, with the degree of approximation quantified by $\kappa_{\text{processing}}$. The observation-ambiguity bias-bound derivation
(`#deriv-observation-ambiguity-bias-bound`) characterizes the Class 3 (Coupled) extreme at
$\kappa_{\text{processing}} \to 1$; the Class 2 case sits in the bounded interior of the
$\kappa$ range.

In biological systems, Class-2 classification is pattern-attributable — there is no closed-form
$\kappa_{\text{processing}}$ accessible from the outside, but the pattern of bounded, structured coupling is recognizable.

*Semantic-reversal note.* Pre-2026-05-09, this value was numbered Class 3. After the 2026-05-09 rename
+ swap, it is Class 2. Anything older than git tag `pre-guc-rename-2026-05-09` that references
"Class 3" in a partially-modular or bounded-coupling context means what is now called Class 2: Partial.
