---
kind: item
owner: C.1
opened: 2026-10-30T23:26:33Z
opened-by: drain-wn-01-gold-opus-5.5
concerns: [segment:def-shared-intent, segment:hyp-auftragstaktik-principle]
---

# #def-shared-intent's Formal Expression still carries four of the five formalization defects that AUDIT-WORKING-526815 raised (F157-F161), re-read at HEAD 86489b0b. (F157) line 26 optimizes argmin over a representation G_s, while IB optimizes over an encoder p(G_s | G_full); the deterministic-encoder ambiguity is the one #form-information-bottleneck carried (526815 F3). (F159) line 28 says high beta approaches 'full model sharing', but the source is the purposeful state (O_t, Sigma_t), not M_t, so it is full purposeful-state sharing. (F160) line 30 calls the shared intent the 'minimal sufficient statistic', which the IB tradeoff at a chosen beta does not give; exact minimal sufficiency needs a sufficiency constraint or the beta -> infinity limit. (F161) the 'purpose before plans before models' ordering (line 34) is flagged there as more robust than the formulation, but nothing derives it from the objective without assumptions about entropy, change rate and relevance. (F158) the relevance variable a_t^coordinated is too narrow, per the gold Follow-up item in the same Working Notes. #hyp-auftragstaktik-principle inherits these (526815 F166). Strengthen first: specify the encoder and relevance variable so the minimal-sufficiency statement becomes a limit theorem, before narrowing the words. Sources: #def-shared-intent Working Notes 'Off-ramp' block (line 79) and gold Follow-up; audits/audit-findings-526815.md:258.
