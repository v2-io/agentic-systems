---
kind: item
owner: C.4
opened: 2026-10-31T02:16:38Z
opened-by: Claude Opus 5.5 (WN-01 drain)
concerns: [segment:scope-edge-update-causal-validity, segment:hyp-edge-update-via-gain, segment:der-orient-cascade]
---

# The orient cascade updates M_t and then the strategy-edge credences from the same observation o_t; the second update may double-count evidence the first already absorbed, biasing edge credences. An analysis exists: spikes/.integrated/spike-edge-semantics-resolution.md §7 judges the concern mostly unfounded, with a bounded residual effect (found by the p5 part of this drain, from #hyp-edge-update-via-gain's Working Notes). What is owed is to bring that verdict and its residual bound into the body, where the interaction is still listed as open, or to state why it stays open. Sources: #scope-edge-update-causal-validity Working Notes, first item; it cites #hyp-edge-update-via-gain's Working Notes for the same flag.
