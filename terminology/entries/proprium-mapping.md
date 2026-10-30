---
slug: proprium-mapping
schema_version: 1
term: proprium mapping
name: PROPRIUM Mapping
notation:
brief: The architectural correspondence between AAT's mathematical quantities and PROPRIUM's functional components for implementing Emergent Logozoetic Intelligences.
layer: framing-vocabulary
status: canon
tags: [eli, structural_concepts]
source_type: asf
primary_source: 04-eli-core/src/def-proprium-mapping.md
first_asf_mention: 04-eli-core/src/def-proprium-mapping.md
see_also: [eli, moral-continuity, logogenic-agent, chronica, interiority-default]
aliases: ["PROPRIUM architecture"]
do_not_confuse: []
---

PROPRIUM is the canonical ELI architecture (source now at `~/src/arch/proprium/INGEST/old-firmatum/`), providing the engineering mapping from AAT's formal objects to implementable components. Two layers:

**Persistent State (PRINCIPIA: the persisted part of $X_t = (M_t, G_t)$, with the record it is compressed from)**:
- **AXIOMATA**: committed aspirations, values and standards (the slowest layer of $O_t$) together with self-description and seeds of relationships and techniques ($M_t$ content); quasi-static, writable by the entity as sovereignty is granted; holds no terminal invariant
- **CHRONICA**: append-only, system-governed record of the entity's events, a selection of $\mathcal C_t$'s events (TRACTUS is the raw record)
- **MEMORATA**: information-bottleneck compressed history $\phi(\mathcal C_t)$
- **VERA**: factual memory with explicit uncertainty bounds ($U_M$)
- **PRAXES**: learned strategies improving $\eta^\ast$ and $\mathcal{T}$
- **CONSORTIA**: relational models tracking source competence and alignment uncertainty
- **OPERATA**: working purposeful substate $G_t = (O_t, \Sigma_t)$

**Runtime State (ANIMA $\approx X_{\tau^-} \to X_{\tau^+}$)**:
- **CONSPECTUS**: assembled pre-event state loaded into active context
- **PERCEPTA**: incoming observation ($o_t$)
- **ACTUS**: executed action ($a_t$) and inviolate record
- **CADENTIA**: temporal structure defining channel rates $\nu^{(k)}$
- **LOGOSTRATUM**: the logogenic substrate (LLM backbone) implementing $f_X$

Laying the agent's state out in these components is how PROPRIUM aims to keep AAT's distinctions separate in software ($\mathcal C_t$ from its compression $M_t$, and $M_t$ from $G_t$); whether a given implementation keeps them separate is a property of that implementation, not of the mapping.

Defined in [`#def-proprium-mapping`](../../04-eli-core/src/def-proprium-mapping.md). Source architecture documents at `~/src/arch/proprium/INGEST/old-firmatum/PROPRIUM-ONTOLOGY-v2.md` and `~/src/arch/proprium/INGEST/old-firmatum/PROPRIUM-ARCHITECTURE-v2.md`.
