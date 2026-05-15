---
slug: goal-update-coupling-class
schema_version: 1
term: Goal-Update Coupling Class
name: Goal-Update Coupling Class (GUC Class)
brief: Three-value axis measuring the degree to which an agent's epistemic update is entangled with its goal state; the architectural property that directed separation quantifies.
layer: framing-vocabulary
status: canon
tags: [structural_concepts, agent_classes]
source_type: asf
primary_source: 01-aat-core/src/der-directed-separation.md
first_asf_mention: 01-aat-core/src/der-directed-separation.md
see_also: [directed-separation, class-coercion, wrapping-regime, separated, partial, coupled]
aliases: ["GUC Class", "GUC axis"]
do_not_confuse:
  - "wrapping regime (W₀/W₁/W₂) — a finer sub-classification within the Class-1 Separated cell, not a separate axis"
  - "Knowledge Type axis (Static/Learning) — a distinct agent-ontology axis"
---

The **Goal-Update Coupling Class** (GUC Class) is the axis that the directed-separation condition of
[`#der-directed-separation`](../../01-aat-core/src/der-directed-separation.md) measures. It names how
much an agent's epistemic update $f_M$ is entangled with its goal state $G_t$ — a structural
property, not a parametric quantity to be tuned.

Three values, running cleanest → middle → worst (aligned with the numbering convention across all six
AAT taxonomy ladders; see the meta-pattern at
[`#disc-separability-pattern`](../../01-aat-core/src/disc-separability-pattern.md)):

| Class | Name | Property |
|---|---|---|
| **Class 1** | **Separated** | Directed separation by construction; $f_M$ takes no $G_t$ argument. Goal-blind epistemic update is a structural commitment, not a behavioral hope. |
| **Class 2** | **Partial** | Coupling present but bounded; $\kappa_{\text{processing}} \in (0, \kappa_{\max})$. Directed separation is approximated with a computable residual leakage rate. |
| **Class 3** | **Coupled** | Directed separation fails by construction; $f_M$ is irreducibly entangled with $G_t$ (as in goal-conditioned LLMs). |

**Meta-pattern alignment.** The three GUC values correspond exactly to the separable-core / structured-repair / general-open columns in `#disc-separability-pattern`'s six-ladder meta-table:
Class 1 = separable core, Class 2 = structured repair, Class 3 = general open. This alignment is why
the Class 2 ↔ 3 numbering swap (2026-05-09) was executed — Architecture was the only outlier in the
six-ladder table; the swap eliminates the outlier status. Original decision record:
`msc/naming/naming-rename-plan.md` lines 92–116; execution plan:
`msc/class-rename-execution-plan-2026-05-09.md`.

**Quantitative operationalization.** In engineered systems, $\kappa_{\text{processing}}$ (defined in
`#der-directed-separation`) is the parameter that places a component on the Class-1 / Class-2 /
Class-3 scale. Class-1 agents have $\kappa_{\text{processing}} = 0$ by construction; Class-2 agents
have $\kappa_{\text{processing}} \in (0, \kappa_{\max})$ with a derivable bound; Class-3 agents have
no structural upper bound on $\kappa_{\text{processing}}$. In biological systems the classification is
pattern-attributable rather than analytically derived.

**Class-1 by structure vs. by behavior.** A Class-1 Separated agent may achieve directed separation
either structurally (W₁ wrapping — query boundary enforces goal-blindness) or behaviorally (W₂
wrapping — goal-blindness is a prompted instruction, not a type constraint). The
[wrapping-regime](wrapping-regime.md) entry refines this sub-distinction. The
[class-coercion](class-coercion.md) entry describes the constructive procedure for making a Class-2 or
Class-3 component participate as Class-1 at the wrapper level.
