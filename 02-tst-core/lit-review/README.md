# TST literature review

These files are the 2025 literature review and paper analyses from TST's prior corpus (`v2-io/temporal-software-theory`, `planning/lit-review/`). They were written against TST's earlier numbering, so they cite principles as `FP-xxx` (v0.1) or `T-xx` (v0.3). The table below decodes those labels to the live segments in `02-tst-core/src/`. The analyses are research inputs, not canon. Several quote constants that canon does not support, such as the $\alpha \approx 0.2$ discontinuity penalty, which `#hyp-exponential-cognitive-load` now treats on measured evidence.

| v0.1 | v0.3 | Name | Live segment |
|---|---|---|---|
| FP-001 | T-01 | Time optimality | `#post-temporal-optimality` |
| FP-002 | T-02 | Implementation-time lower bound (speed limit) | `#result-specification-bound` |
| — | T-03 | Evolving-systems scope | `#scope-evolving-software` |
| FP-003 | T-04 | Change-expectation baseline (Lindy) | `#der-change-expectation-baseline` |
| FP-007 | T-05 | Dual optimization | `#der-dual-optimization` |
| FP-004 | T-06 | Change investment | `#der-change-investment` |
| FP-005 | T-07 | Conceptual alignment | `#hyp-conceptual-alignment` |
| FP-006 | T-08 | Domain tracking | `#hyp-conceptual-alignment` (realignment corollary, refactoring priority) |
| FP-008 | T-09 | Changeset size | `#emp-changeset-size-principle` |
| FP-009 | T-10 | Change proximity | `#der-change-proximity-principle` |
| FP-010 | T-11 | Coherence-coupling measure | `#meas-coherence-coupling` |
| FP-011 | T-12 | Comprehension-proximity correlation | `#der-change-proximity-principle` (reading locality) |
| FP-012 | T-13 | Comprehension continuity | `#hyp-exponential-cognitive-load` |
| FP-013 | T-14 | Principled decision integration | `#der-principled-decision-integration` |
| — | T-15 | Continuous operation under perturbation | `#scope-continuous-operation` |
| DEF-001 | D-01 | Feature | `#def-feature` |
| DEF-002 | D-02 | Atomic changeset | `#def-atomic-changeset` |
| — | D-03 | Comprehension time | `#def-comprehension-time` |
| — | D-04 | Implementation time | `#def-implementation-time` |
| — | D-05 | Change distance | `#def-discontinuity-distance` |
| — | D-06 | System coupling | `#def-system-coupling` |
| — | D-07 | System coherence | `#def-system-coherence` |
| — | D-08 | System availability | `#def-system-availability` |

Some 2025 synthesis documents use a third, 14-theorem numbering, in which T-01 to T-13 are FP-001 to FP-013 renamed and T-14 is continuous operation. A bare "T-07" therefore means dual optimization there and conceptual alignment in v0.3, so read their theorem names rather than their numbers. The original theorem and definition files are in the `temporal-software-theory` repository under `vault/02-theory/`.
