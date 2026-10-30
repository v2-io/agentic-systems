---
kind: item
provenance: imported
source: PROPOSALS.md:172
section: PROPOSALS — Architectural Portfolio › §D. Later — needs investigation-first scoping or upstream maturation
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
concerns: [segment:def-strategy-dimension, segment:def-strategy-dag, segment:def-satisfaction-gap, segment:deriv-strategic-composition]
rechecked: 2026-10-30T21:30:34Z by Claude Opus 5.5 (item rechecker, q-proposals lane)
owner: unassigned
restated: 'Extend the strategy DAG with a commitment state (considering vs committed, per Bratman / Rao-Georgeff; #def-strategy-dimension:97) and temporal structure (deadlines, durations); per-path resources are a third, separate leg, distinct from #form-resource-budget''s actuation-energy budget.'
---

# D.4 SP-12 — Commitment / resource / temporal DAG extensions

Imported verbatim (relative links rebased) from `PROPOSALS.md` line 172, section *PROPOSALS — Architectural Portfolio › §D. Later — needs investigation-first scoping or upstream maturation*. Not yet re-checked against HEAD: `vsect recheck item:proposals-d-4-sp-12-commitment-resource-temporal-d-1dea --outcome holds|stale|landed|not-an-item --why …`.


Newly surfaced in 2026-04-24 audit. Currently named in CLAUDE.md "Known Fragilities" but homeless in portfolio. Three dimensions the strategy DAG omits: **(a) commitment state** (BDI-style desire $D_t$ / committed intent $I_t$ split per Bratman / Rao-Georgeff); **(b) resource budgets** per path; **(c) temporal structure** (deadlines, durations, synchronization).

**Composes with O-BP12** (resource budget $B_t$ as master variable): SP-12 is the DAG-structure side; O-BP12 is the cost-allocation side. Together could provide the full bounded-rationality apparatus. **Composes with SP-11** (commitment state matters for composition-monotonicity — "we agreed" vs. "we committed" distinction).

**Medium-large effort** (multi-segment extension, requires spike). **Primary aspect: completeness. Secondary: reach (unlocks logogenic/Section-III work).** **Value: +6.**

**Independence: medium.** Touches `#def-strategy-dimension`, `#def-strategy-dag`, `#def-satisfaction-gap`, possibly `#deriv-strategic-composition`. Conflicts with any concurrent strategy-layer work, especially O-BP4 (retired but referenced) and any Section II strategy-DAG edits. New commitment-state object is mostly additive; existing semantics preserved. Safe to parallelize with Section I / III work and with Bundle 1 framing work.

Also (influx drain, second half, 2026-10-30): the commitment leg has an outside reading worth starting from. `~/src/agent-core/tools/asf-transcribe/some-notes.md` (a dialog with Joseph, 2026-10-07) finds that canon models when to stop *gathering* (#der-deliberation-cost, CIY, the survival imperative, under which certainty is never a stopping condition) but not when to *commit*: commitment as a state is DP-3 of `.archive/04-intent-dag-consolidated.md`, still open as #def-strategy-dimension's Working Note ("the formalism doesn't distinguish 'considering' from 'executing'"); irreversibility appears in prose only. A commit criterion needs value of waiting and cost of waiting (both in canon) plus irreversibility-weighted cost of error and option value (neither), which is optimal stopping and real options, to be adopted under their own names with citation. A Discussion-grade point that could land on its own in #der-directed-separation: Joseph's "simultaneously decisive and epistemologically humble" is coherent in AAT because of directed separation (commit at credence 0.6 and keep believing 0.6), while a coupled agent inflates belief to justify the act. The same dialog explains why nodes are binary (credences attach to propositions; predicates make nodes checkable; "binarization is itself a decisiveness device"). Relayed in `msc/inside-out-2026-10/influx-scout/agent-core.md` §2.C and P3. No AAT-internal derivation exists yet, so spike before landing above discussion-grade.

Also raised in (WN-01 drain, 2026-10-30, Claude Opus 5.5): #def-strategy-dimension Working Notes 'Commitment state' (D_t desire vs I_t committed intent; open for Part III, where shared desire vs shared commitment may be load-bearing) and 'Resource budget' (per-action costs and capacity constraints for resource-constrained agents).

Also raised in (2026-10-30, audits drain): `audits/AUDIT-WORKING-471203/adversarial-creative-challenges.md` Challenge 8 (no formal commitment phase between deliberation and execution; "AAD has $\delta_{\text{deliberation}}$ but no $\delta_{\text{commitment}}$"), Missing 3 (commitments are neither preferences in $O_t$ nor paths in $\Sigma_t$ but constraints with a cost to break; a fourth $G_t$ component) and Missing 8 (actions are atomic events: no action in progress, interrupted, or hardening as resources are committed). Claude, 2026-04-28. Still open six months on: `#disc-strategic-self-coupling` treats commitment as coupling bought for credibility but supplies no state variable, and the 2026-10-07 strategy-DAG engineering work recorded commitment/decisiveness as open (project memory `project_strategy_dag_engineering_2026_10_07.md`). B.2's retyping of the strategy DAG is the place to decide whether commitment belongs to the agent-claims or to one model among several.
