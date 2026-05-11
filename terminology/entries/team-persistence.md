---
slug: team-persistence
schema_version: 1
term: team persistence
name: Team Persistence
notation:
brief: Multi-agent extension of the persistence condition — teams persist where individuals cannot through communication (shared observations) and cooperative action (reduced disturbance).
layer: framing-vocabulary
status: canon
tags: [structural_concepts, core_quantities]
source_type: asf
primary_source: 01-aad-core/src/der-team-persistence.md
first_asf_mention: 01-aad-core/src/der-team-persistence.md
see_also: [adversarial-destabilization, adaptive-reserve, adaptive-tempo, strategic-tempo, structural-persistence]
aliases: []
do_not_confuse: []
---

The multi-agent instantiation of the sector-persistence template: sub-agent $i$ persists iff its
effective disturbance rate $\rho_i^{\text{eff}}$ relative to its correction capacity $\alpha_i$
stays within reserve $R_i$. The distinctive content is the **disturbance decomposition**:

$$\rho_i = \rho_{i,\text{env}} + \sum_{j \in \mathcal{A}_i} \gamma_{j\to i}^{\text{adv}}\mathcal{T}_j - \sum_{j \in \mathcal{C}_i} \gamma_{j\to i}^{\text{coop}}\mathcal{T}_j$$

Two physically distinct cooperative mechanisms enter at different points:
- **Communication tempo**: allies share observations, raising $\mathcal{T}_i$ (the epistemic side).
- **Cooperative action**: allies act in the shared environment to reduce $\rho_i$ at its source (the disturbance side).

A single cooperative event contributes through exactly one mechanism — counting it in both
would double-count the benefit. This is the cooperative counterpart of
[adversarial destabilization](adversarial-destabilization.md), which uses the same signed
$\gamma$ coupling structure but with positive sign. Three levers for team persistence: raise
individual correction efficiency $\alpha_i$, increase cooperative disturbance reduction, or
reduce adversarial coupling.

Derived in [`#der-team-persistence`](../../01-aad-core/src/der-team-persistence.md).
