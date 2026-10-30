---
kind: item
owner: F.2
opened: 2026-10-30T23:27:51Z
opened-by: drain-influx-2
concerns: [segment:scope-channel-collapse, segment:der-directed-separation]
---

# External literature that bears on measuring directed separation in LLMs, for E.1's design and for #scope-channel-collapse's kappa_processing ~ 1 premise, gathered by the context-saliency dossier and never cited in canon: Arghal et al., 'A Behavioural and Representational Evaluation of Goal-Directedness in Language Model Agents' (arXiv 2602.08964v2, ICML 2026): cognitive-map decode accuracy falls ~75% to ~60% from pre- to post-reasoning (representational capacity shifting off world state; the authors do not frame it as coupling), 57.9% of 'suboptimal' actions were optimal given the model's own decoded beliefs (behavioral irrationality measures conflate belief and goal processing), single-layer patching was ineffective, nonlinear probes recover world structure (~75%) where linear ones do not (39%). The dossier's residue: nothing located holds the world fixed, perturbs only the goal, and outputs a coupling coefficient, which is exactly E.1's measurement. Methodological walls it lists: non-identifiability and non-surjectivity of steering vectors (arXiv 2602.06801, 2604.09839) and probe failure under distribution shift (arXiv 2605.27958). Verify against the primaries before citing (the dossier marks these [fetched by sweep] or [snippet]; its §9 has a verification table, and all 23 priority papers are in relata). Source: ~/src/arch/msc/context-saliency/dossier-2026-08-28.md §5.2 (lines 126-145); relayed in msc/inside-out-2026-10/influx-scout/arch-program.md §1.3, §13 row 21.
