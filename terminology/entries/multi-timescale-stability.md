---
slug: multi-timescale-stability
schema_version: 1
term: multi timescale stability
name: Multi-Timescale Stability
notation:
brief: When adaptive processes operate at N nested timescales, the composite is stable when each level satisfies the sector-persistence template with interconnection terms added to its effective disturbance; the required timescale separation is a closed-form threshold (derived, Model D, premise-conditional).
layer: framing-vocabulary
status: canon
tags: [structural_concepts]
source_type: asf
primary_source: 01-aat-core/src/der-multi-timescale-stability.md
first_asf_mention: 01-aat-core/src/der-multi-timescale-stability.md
see_also: [adaptive-gain-dynamics, sector-condition, adaptive-system, structural-persistence]
aliases: []
do_not_confuse: []
---

The temporal nesting constraint from AAT (faster adaptive processes must be much faster than slower ones: $\nu_{n+1} \ll \nu_n$) has a derived stability-theoretic foundation. When $N$ adaptive processes operate at nested timescales, each level instantiates the sector-persistence template with two interconnection terms added to its effective disturbance — the settled residue of the level below, and the target-drag of the moving level above — and the composite is stable when every level's persistence condition holds against its total effective disturbance.

The required timescale separation is a closed-form threshold, not merely a heuristic: $\epsilon \lt \epsilon_{\max} = \Delta\rho^\ast / (L_h v^{\max})$ — the faster level's adaptive reserve divided by the rate at which the slower level drags the faster level's target. When violated, the faster level's transients contaminate the slower level's dynamics (and vice versa through the residue term), destabilizing the composite. Micromanagement and catastrophic forgetting are the two conditions of the theorem violated separately.

**LLM systems** involve many parallel adaptive processes — pretraining, fine-tuning, LoRA adaptation, in-context learning, retrieval/RAG, tool-use feedback, within-generation attention — without clean boundaries between "parametric" and "structural." The $N$-timescale framework accommodates this naturally: stability requires only that adjacent timescales satisfy the per-level conditions, regardless of how many levels exist.

*Scope:* derived (Model D, exact under named premises) for dynamics admitting a Lipschitz quasi-steady-state manifold with per-level sector conditions; discrete/jump structural adaptation and the stochastic (Model S) stacking remain open.

Derived in [`#der-multi-timescale-stability`](../../01-aat-core/src/der-multi-timescale-stability.md) (promoted from sketch 2026-06-10).
