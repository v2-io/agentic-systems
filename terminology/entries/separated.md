---
slug: separated
schema_version: 1
term: Separated
name: 'Class 1: Separated (GUC)'
brief: GUC Class-1 value; agent whose epistemic update $f_M$ takes no $G_t$ argument
  — directed separation holds by structural commitment.
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
- partial
- coupled
- class-coercion
- wrapping-regime
aliases:
- GUC-Separated
- Class 1
- Class-1 agent
do_not_confuse:
- modular (pre-2026-05-09 label for this same value; now retired as the GUC-axis label,
  though 'modular' remains in use for broader system-level modularity concepts)
seq: 1
---

**Class 1: Separated** is the cleanest value on the [Goal-Update Coupling Class](goal-update-coupling-class.md)
axis. A Separated agent's epistemic update $f_M$ is goal-blind by construction: it takes no $G_t$
argument, and the directed-separation condition of
[`#der-directed-separation`](../../01-aat-core/src/der-directed-separation.md) holds structurally.

The "by construction" qualifier matters. A Separated agent may be tightly integrated at the system
level — what distinguishes it is that the belief-update computation is architecturally forbidden from
reading the goal state, not merely that it happens to be well-behaved. This is the property that makes
Part II's theoretical results applicable without further qualification.

Separation can be implemented natively (the component is inherently goal-blind) or via W₁ wrapping
(the scaffold enforces the query boundary). W₂ wrapping achieves separation *behaviorally* — the
resulting composite is Class 1 by behavior rather than by structure, with a residual leakage rate that
lacks a derivable structural upper bound. See [wrapping-regime](wrapping-regime.md) for the structural
vs. behavioral sub-distinction.

Where Separated agents cannot be used directly (e.g., because the underlying component is a
goal-conditioned LLM — Class 3 Coupled), the [class-coercion](class-coercion.md) construction can
produce a Class-1-at-the-wrapper-level composite at a tempo cost.
