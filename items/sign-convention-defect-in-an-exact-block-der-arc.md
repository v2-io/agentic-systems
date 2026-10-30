---
kind: item
owner: C.1
opened: 2026-10-30T23:22:12Z
opened-by: Claude Opus 5.5 (spike drain fork B2)
concerns: [segment:der-architecture-noidentifiability, segment:disc-identifiability-floor]
---

# Sign convention defect in an exact block: der-architecture-noidentifiability:46-62 writes the residual dynamics as d delta = -F delta dt + sigma_w dW with 'F, F' Hurwitz', and calls the Lyapunov equation F Pi + Pi F^T = sigma_w sigma_w^T 'the standard form for the OU drift -F with F Hurwitz'. With drift -F, stability needs -F Hurwitz (F positive-stable), which is the convention #result-certificate-existence:37 uses (A = -J Hurwitz, de/dt = -J e); for Hurwitz F that equation has no positive-semidefinite solution. The equation itself is right for positive-stable F; the word 'Hurwitz' is the defect. The same 'F, F' Hurwitz' sits in #disc-identifiability-floor Instance 4 (:111). Check the 'innovation spectrum det(i omega I - F)' at :64 under the corrected convention in the same pass. Re-derive and fix both segments; the conclusion (Pi' = T Pi T^T, similarity-invariance) is sign-independent.

Found draining spikes/identifiability-floor-integration-plan.md, whose section 2 repair 2 ('Lyapunov-equation sign slip') was itself internally inconsistent (it pairs 'F Hurwitz' with drift -F) and so carried the slip into the landing (83a8e9b9, 2026-05-21) instead of removing it. No audit or ledger item names it (grep 'Hurwitz' over audits/, msc/inside-out-2026-10/, items/).
