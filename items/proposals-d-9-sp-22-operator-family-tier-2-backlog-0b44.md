---
kind: item
provenance: imported
source: PROPOSALS.md:220
section: PROPOSALS — Architectural Portfolio › §D. Later — needs investigation-first scoping or upstream maturation
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
concerns: [segment:result-certificate-existence, segment:disc-stability-certificate, segment:der-directed-separation]
rechecked: 2026-10-30T21:30:35Z by Claude Opus 5.5 (item rechecker, q-proposals lane)
owner: unassigned
---

# D.9 SP-22 — Operator-family Tier-2 backlog: residual CL-1 landing

Imported verbatim (relative links rebased) from `PROPOSALS.md` line 220, section *PROPOSALS — Architectural Portfolio › §D. Later — needs investigation-first scoping or upstream maturation*. Not yet re-checked against HEAD: `vsect recheck item:proposals-d-9-sp-22-operator-family-tier-2-backlog-0b44 --outcome holds|stale|landed|not-an-item --why …`.


*(Surfaced 2026-05-12 from the spike-audit triage. The architectural question — separate appendices vs. unified operator-family meta-segment vs. hybrid — was **resolved 2026-05-14**: no operator-family meta-pattern exists; the genuine unification landed as `#result-certificate-existence` + `#disc-stability-certificate`, and the backlog went to per-spike ($\gamma$)-hybrid triage. The backlog was then dispositioned by the 2026-05-17/18 spike-routing cycle, and the reserved Instance-4 / Object-B / CL-2-heavy decision closed 2026-05-21. Narrative: CHANGELOG 2026-05-14 / -17 / -18 / -21; per-spike routing detail in `spikes/ROUTING.md` + `spikes/.integrated/MANIFEST-2026-05-17.md`.)*

**Residual open work — CL-1, one coupled `#dissipativity-template` landing** (one integration-plan, *not* three half-segments — the sibling-coupling catch): `spike-passivity-composition` (Willems passivity for heterogeneous Kalman+PID composition) + `spike-pid-a2prime` (PID A2' via SPR/KYP positive-real; explicit $\alpha_{\text{PID}}$) + `spike-bridge-lemma-nonlinear-strengthening-2026-04-24` §7.2 passivity / dissipativity. Target: `#dissipativity-template` appendix + Class 1/2/3 port-structure addition to `#der-directed-separation`. Heavy; queued. Coordinate with SP-15 (§D.7, template-family naming — the `#dissipativity-template` would be the trio's third member).

**Independence: medium.** Touches `01-aat-core/src/` appendix territory + `#der-directed-separation`; serialize with any concurrent sector/template work.

---
