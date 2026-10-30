---
kind: item
provenance: imported
source: PROPOSALS.md:152
section: PROPOSALS — Architectural Portfolio › §D. Later — needs investigation-first scoping or upstream maturation
owner: ""
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
concerns: [segment:der-architecture-noidentifiability, segment:disc-identifiability-floor, segment:hyp-directed-separation-under-composition, segment:der-agent-opacity, segment:der-interaction-channel-classification, segment:scope-composite-agent]
---

# D.2 Section III completion — upstream pieces (see Bundle 2)

Imported verbatim (relative links rebased) from `PROPOSALS.md` line 152, section *PROPOSALS — Architectural Portfolio › §D. Later — needs investigation-first scoping or upstream maturation*. Not yet re-checked against HEAD: `vsect recheck item:proposals-d-2-section-iii-completion-upstream-piec-e28d --outcome holds|stale|landed|not-an-item --why …`.


**O-BP16 population-level Lyapunov dynamics** — residual work: Kalman-Ho closed-form follow-up spike (queued); possibly `#population-dynamics` or `#latent-structural-diversity` segment (1–2 sessions if residual content warrants). Instance 4 is already `#der-architecture-noidentifiability` in `#disc-identifiability-floor` — do not re-queue it here. **Updated total: 1–2 sessions.**

External literature rich: Moran model, replicator-Fokker-Planck (Traulsen-Claussen-Hauert 2008), Kullback-Leibler as Lyapunov for ESS (Baez 2014), Baez-Pollard 2016. Directly reusable under prior-art-integration convention.

**SP-17 goal-information-leakage $\mathcal L_{G \to M}^c = I(o_c; G_t^c \mid \Omega_t)$** — surfaced in 2026-04-24 audit as the *deferred residue* of the goal-contamination formalization (the composition-gaps spike is integrated 2026-05-17; SP-17 is its still-open residue, not resolved by the filing — CHANGELOG 2026-05-17). Makes $\mathcal{L}$ a first-class AAT quantity; gives Case 3 (emergent goal-conditioning under Class 3 (Coupled)-composition boundary) a quantitative handle rather than a qualitative case-distinction. Scoping question: own segment vs. subsection of `#hyp-directed-separation-under-composition`? **1–2 sessions.** **Value: +4.** **Independence: high** if new segment; **medium** if landed as subsection (conflicts with any concurrent `#hyp-directed-separation-under-composition` work).

**O-BP16 independence: medium.** New segment + cross-refs to existing Section III segments (`#der-agent-opacity`, `#der-interaction-channel-classification`, `#disc-identifiability-floor`). Light touches only; safe to parallelize with non-Section-III work. Conflicts with O-BP9 if both edit `#scope-composite-agent` concurrently.
