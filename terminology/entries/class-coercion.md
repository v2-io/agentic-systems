---
slug: class-coercion
schema_version: 1
term: class coercion
name: Class coercion (via wrapping)
brief: Constructive procedure for making a Class 2 (Partial) or Class 3 (Coupled) component participate as Class 1 (Separated) in AAD by embedding it in an external scaffold whose type signatures enforce directed separation.
layer: prose-symbol
status: canon
tags: [structural_concepts, composition]
source_type: asf
primary_source: 01-aad-core/src/der-class-coercion-via-wrapping.md
first_asf_mention: 01-aad-core/src/der-class-coercion-via-wrapping.md
see_also: [directed-separation, wrapper, wrapping-regime]
aliases: ["wrapping construction", "constructive class coercion"]
do_not_confuse: []
---

The constructive direction of [`#hyp-directed-separation-under-composition`](../../01-aad-core/src/hyp-directed-separation-under-composition.md) for the wrapper-around-component special case. A primitive component $A$ (such as an LLM) whose forward pass entangles belief-update and goal-conditioning is embedded inside an external scaffold with explicit $X_W = (M_W, G_W)$ state. The scaffold's belief-update map $f_M$ has no $G_W$ argument by type signature; its belief-side query selector $q_M$ likewise has no $G_W$ argument. Under stated conditions on the component (admissibility of goal-blind queries, stationary conditional, no implicit goal-inference), directed separation holds at the wrapper level by structural commitment, and the composite is Class 1 (Separated) by construction — even though $A$ is Class 2 (Partial) or Class 3 (Coupled).

The cost is paid in tempo (Brooks's-Law form via [`#der-tempo-composition`](../../01-aad-core/src/der-tempo-composition.md), with $\mathcal T_W \leq \mathcal T_A^{\text{nominal}} - C_{\text{coord}}^{\text{wrap}}$) and a residual leakage rate from the component's pretraining-induced query-content / goal-content correlation.

Theorem statement and proof in [`#der-class-coercion-via-wrapping`](../../01-aad-core/src/der-class-coercion-via-wrapping.md). Logogenic-substrate specialization in [`#der-logogenic-as-wrapping`](../../03-logogenic-agents/src/der-logogenic-as-wrapping.md).
