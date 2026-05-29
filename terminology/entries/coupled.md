---
slug: coupled
schema_version: 1
term: Coupled
name: 'Class 3: Coupled (GUC)'
brief: GUC Class-3 value; agent whose epistemic update is irreducibly entangled with
  its goal state — directed separation fails by construction.
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
- partial
- class-coercion
aliases:
- GUC-Coupled
- Class 3
- Class-3 agent
do_not_confuse:
- fully merged (pre-2026-05-09 label for this same value, retired as GUC-axis label
  in the 2026-05-09 rename; Class 2 pre-rename)
- coupling (the abstract property — entanglement of $M_t$ and $G_t$ dynamics — of
  which this class is the extreme case)
- 'adversarial coupling pressure (a distinct concept about external pressure that
  drives agents toward the Coupled class; see #disc-adversarial-coupling-pressure)'
seq: 3
---

**Class 3: Coupled** is the most entangled value on the [Goal-Update Coupling Class](goal-update-coupling-class.md)
axis. A Coupled agent's epistemic update $f_M$ is irreducibly entangled with its goal state $G_t$:
directed separation fails by construction, not by parameter setting. No scalar $\kappa$ bounds the
leakage, because the entanglement is structural.

The canonical example is a goal-conditioned large language model (LLM), whose forward pass jointly
updates belief-relevant content and goal-relevant generation in a single fused computation. There is no
architectural boundary that makes the belief-update goal-blind; the model's pretraining and
prompt-conditioning couple them at a fundamental level. Logogenic agents (from
[`03-llm-core/`](../../03-llm-core/)) are constituted by such components and are
therefore Coupled at the component level.

Coupled agents can participate in Separated composites via the [class-coercion](class-coercion.md)
construction: a scaffold with explicit external state enforces directed separation at the wrapper level,
even though the underlying component remains Class 3. The cost is paid in tempo overhead and a residual
leakage rate.

Part II results from `#der-directed-separation` that depend on directed separation hold exactly for
Class 1 (Separated), hold approximately for Class 2 (Partial) with explicit bounds, and do not hold
in general for Class 3 (Coupled). The survival-classification table in `#result-section-ii-survival`
documents which results extend and which are blocked by Class-3 status.

*Semantic-reversal note.* Pre-2026-05-09, this value was numbered Class 2. After the 2026-05-09 rename
+ swap, it is Class 3. Anything older than git tag `pre-guc-rename-2026-05-09` that references
"Class 2" in the logogenic-agent or fully-merged context means what is now called Class 3: Coupled.
