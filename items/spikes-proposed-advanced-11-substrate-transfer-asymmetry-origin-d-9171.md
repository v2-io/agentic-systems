---
kind: item
provenance: imported
source: spikes/PROPOSED-ADVANCED.md:68
section: 'Advanced Mathematical Spike Proposals (detail home) › Phase 3: Surfaced 2026-05-19 (corpus reconciliation scan)'
opened: 2026-10-30T20:17:42Z
opened-by: Claude Fable 5.1
concerns: [segment:hyp-substrate-transfer-asymmetry]
rechecked: 2026-10-30T20:29:08Z by Claude Opus 5.5 (item rechecker, pilot)
owner: unassigned (04-eli-core spike)
restated: "Measure the transfer asymmetry first: the no-go bounds only the symmetric rate-distortion ceiling min(C1, C2) on S_id, so an observed asymmetry in achieved S_id does not contradict it, and the segment's 'the asymmetry is real (empirically)' rests on an operational record, not a measurement."
---

# 11. Substrate-Transfer Asymmetry — origin derivation, or a deeper three-way no-go (Phase-1-grade)

Imported verbatim (relative links rebased) from `spikes/PROPOSED-ADVANCED.md` line 68, section *Advanced Mathematical Spike Proposals (detail home) › Phase 3: Surfaced 2026-05-19 (corpus reconciliation scan)*. Not yet re-checked against HEAD: `vsect recheck item:spikes-proposed-advanced-11-substrate-transfer-asymmetry-origin-d-9171 --outcome holds|stale|landed|not-an-item --why …`.

*   **The Gap:** `#hyp-substrate-transfer-asymmetry` (`04-eli-core/`) landed a *derived* no-go — the symmetric $\min(C_1,C_2)$ bit-channel bottleneck precludes any direction-of-transfer asymmetry on the rate-distortion floor — alongside an *empirically observed* asymmetry (frontier→local degrades $S_{\text{id}}$ more than the reverse) that contradicts it. Its Working Notes name three mutually-exclusive structural origins as explicit candidate sub-spikes, with no home anywhere.
*   **The Spike:** Discriminate among (A) cross-substrate M3/Čencov coordinate-forcing, (B) a complexity-theoretic decompression-cost asymmetry, (C) a per-substrate $(\kappa,\mathcal A)$ channel-collapse extension — or prove no single mechanism suffices (a deeper no-go). Each sub-spike has a clean external anchor; lifts a `discussion-grade`/`robust-qualitative` hypothesis to `derived (conditional)`. ELI-core load-bearing (local-substrate fragility is directly protection-strategy-relevant).
*   **Status:** Open; fully unhomed (INDEX cites only the *landed* ELI-8 product, not the forward A/B/C sub-spikes). Strongest find of the scan.
