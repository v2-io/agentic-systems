---
kind: item
owner: C.1
opened: 2026-10-30T23:27:14Z
opened-by: drain-wn-01-gold-opus-5.5
concerns: [segment:result-per-dimension-persistence, segment:impl-persistence-and-limits]
---

# #result-per-dimension-persistence's weakest-link law (Brief line 110; lines 14 and 74) holds only for a conjunctive failure boundary, and that geometry is not stated (checked at HEAD 86489b0b). 'The weak dimension is the bottleneck ... regardless of performance on strong dimensions' is rigorous when survival requires every |delta_k| < c_k, a hypercube boundary governed by L_inf. Under a smooth L_2 boundary on V_O, strength on one dimension can compensate for weakness on another: the worked example's ||delta||_L2 = 0.785 (line 96) survives an L_2 < 1 boundary. Strengthen first by stating the failure-boundary geometry as a named hypothesis: under conjunctive (L_inf) survival the law is exact and justifies the 'specialists compose better' close; under L_2 the per-dimension condition is sufficient but not necessary. #impl-persistence-and-limits Working Notes line 96 inherits this. The TST reading of the matrix-Loewner condition as 'the weakest channel is the bottleneck' (item:tst-canon-reads-the-matrix-loewner-persistence-c) is a related but different defect in Volume 2 (channels mistaken for directions); whoever lands either should check the other's 'weakest is the bottleneck' wording. Source: the segment's Working Notes Off-ramp (line 165), Gemini AUDIT-WORKING-193847 poke; 526815 did not reach this segment.

Also raised in (WN-01 drain, 2026-10-30, Claude Opus 5.5): #impl-persistence-and-limits Working Notes 'Open — failure-boundary geometry for the weakest-link claim' (its §3 inherits the geometry).
