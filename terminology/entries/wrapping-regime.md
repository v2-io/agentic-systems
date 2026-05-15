---
slug: wrapping-regime
schema_version: 1
term: wrapping regime
name: Wrapping regime (W₀ / W₂ / W₁)
brief: Three-level hierarchy of structural commitment to directed separation in wrapper constructions, distinguished by where the separation lives — at the query boundary (W₁), at the write boundary (W₂), or absent (W₀).
layer: prose-symbol
status: canon
tags: [structural_concepts, composition]
source_type: asf
primary_source: 01-aat-core/src/der-class-coercion-via-wrapping.md
first_asf_mention: 01-aat-core/src/der-class-coercion-via-wrapping.md
see_also: [class-coercion, wrapper, directed-separation]
aliases: ["W₁", "W₂", "W₀", "strict wrapping", "partial wrapping", "output-structuring"]
do_not_confuse: []
---

The three regimes by which a wrapper construction can — or fails to — enforce directed separation:

- **W₁ (strict wrapping)** — the wrapper issues *separate* goal-blind ($q_M$) and goal-conditioned ($q_G$) calls to the underlying component per macro-step. Directed separation holds at the wrapper level *structurally*; the leakage rate is bounded above by the pretraining-distribution mutual information $\kappa_{W_1} \le I(A(q_M); G_W \mid q_M)$.

- **W₂ (partial wrapping / output-structuring)** — the wrapper issues *one* goal-conditioned call per macro-step carrying the full $(M_W, G_W)$ context, and parses the response into structurally typed update fields routing $M_W$ vs. $G_W$ updates. Structural separation lives at the *write boundary* but not at the *query boundary*; directed separation holds *behaviorally*, bounded by the component's compliance with the prompted instruction-to-separate. **No structural upper bound** on $\kappa_{W_2}$ — the bound is empirical and adversarially fragile.

- **W₀ (no wrapping)** — raw Class-3 component use, no scaffold. Directed separation does not hold; this is the Class-3 baseline.

The regime hierarchy refines the Class-1 cell of [`#der-directed-separation`](../../01-aat-core/src/der-directed-separation.md) with a *structural-vs-behavioral* sub-distinction: **Class-1-by-structure** (W₁ or natively goal-blind) has a derivable leakage bound; **Class-1-by-behavior** (W₂) has an empirical-only bound that depends on the component's instruction-following fidelity.

Most practical scaffolded-LLM frameworks (ReAct, Reflexion, MemGPT, BabyAGI, AutoGPT) implement W₂. PROPRIUM-as-implemented sits in W₂ with the auxilia hierarchy (per [`#def-auxilia-hierarchy`](../../04-eli/src/def-auxilia-hierarchy.md)) as the candidate constructive realization of W₁. Park et al.'s 2023 *Generative Agents* observation→memory step is the closest empirical instance of W₁ in published work.

Specified and contrasted in [`#der-class-coercion-via-wrapping`](../../01-aat-core/src/der-class-coercion-via-wrapping.md); logogenic-substrate specialization in [`#der-logogenic-as-wrapping`](../../03-logogenic-agents/src/der-logogenic-as-wrapping.md).
