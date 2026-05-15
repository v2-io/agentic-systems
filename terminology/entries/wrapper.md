---
slug: wrapper
schema_version: 1
term: wrapper
name: Wrapper (over a primitive component)
brief: External scaffold around a primitive component $A$, maintaining explicit state $X_W = (M_W, G_W)$ updated through structurally distinct goal-blind and goal-conditioned query channels.
layer: prose-symbol
status: canon
tags: [structural_concepts, composition]
source_type: asf
primary_source: 01-aat-core/src/der-class-coercion-via-wrapping.md
first_asf_mention: 01-aat-core/src/der-class-coercion-via-wrapping.md
see_also: [class-coercion, wrapping-regime, directed-separation]
aliases: ["wrapping", "wrapping construction"]
do_not_confuse: []
---

The structural object that performs class coercion (see [`class-coercion`](class-coercion.md)) over a primitive component $A$. A wrapper $W$ has explicit external state $X_W = (M_W, G_W) \in \mathcal X_M \times \mathcal X_G$ and four type-signed update components: a *belief-side query selector* $q_M : \mathcal X_M \times \mathcal O_W \to \mathcal Q_A$ (no $G_W$ argument), a *strategy-side query selector* $q_G : \mathcal X_M \times \mathcal X_G \to \mathcal Q_A$ (may use $G_W$), a *belief-update map* $f_M$ (no $G_W$ argument), and a *strategy-update map* $f_G$ (may use $G_W$). The structural commitment that gives directed separation at the wrapper level is the absence of $G_W$ in the type signatures of $f_M$ and $q_M$.

Wrappers can be more elaborate than the bare-minimum form — multi-component typed $M_W$ (e.g., PROPRIUM's VERA / MEMORATA / CONSORTIA / PERCEPTA / CHRONICA), multi-layered typed $G_W$ (AXIOMATA / OPERATA / PRAXES), substrate-heterogeneous query handling (auxilia hierarchy at varying cost-tiers per [`#def-auxilia-hierarchy`](../../04-eli/src/def-auxilia-hierarchy.md)). The bare-minimum form is what the class-coercion theorem requires; the elaborations are domain-specific structure.

Defined and analyzed in [`#der-class-coercion-via-wrapping`](../../01-aat-core/src/der-class-coercion-via-wrapping.md).
