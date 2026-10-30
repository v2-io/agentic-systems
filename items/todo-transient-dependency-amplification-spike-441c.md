---
kind: item
provenance: imported
source: TODO.md:163
section: TODO — Miscellaneous & details › Open theory items (MEDIUM)
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
rechecked: 2026-10-30T21:53:39Z by Claude Opus 5.5 (item rechecker, t1-todo)
owner: G.2
restated: 'Misframed as ''promotion blocked on seven obligations''. The spike (spikes/spike-transient-dependency-amplification.md, 2026-04-25, still at top level) states exact results within its affine feature-local sub-scope: Lemma 1 (supremum of uniformly Lipschitz policy values is Lipschitz), Corollary 1 (the linearized Jacobian-product bound), Proposition 1 (the branching transient-growth construction), Lemma 2 (checkpoint product and recurrence bounds), and the singular-subspace coverage formula. Under the project''s own rule (working theory at honest tier belongs in canon; strengthening is promotion, not admission), these are stranded derivations. The seven ''obligations'' are the open edges a conditional-tier segment would name in its Epistemic Status, not preconditions for its existence. Land the sub-scope results as a conditional segment (02-tst-core or 03-llm-core); keep the obligations as its named gaps. #hyp-exponential-cognitive-load:91 already points readers at the spike, so the canon-to-spike reference is live.'
---

# Transient dependency amplification — spike landed 2026-04-25 (`spikes/spike-transient-dependency-amplification.md`); promotion to TST-side `02-tst-core/src/der-

Imported verbatim (relative links rebased) from `TODO.md` line 163, section *TODO — Miscellaneous & details › Open theory items (MEDIUM)*. Not yet re-checked against HEAD: `vsect recheck item:todo-transient-dependency-amplification-spike-441c --outcome holds|stale|landed|not-an-item --why …`.

- **Transient dependency amplification** — spike landed 2026-04-25 (`spikes/spike-transient-dependency-amplification.md`); promotion to TST-side `02-tst-core/src/der-transient-dependency-amplification.md` blocked on priority-ordered obligations:
  - Formal sub-scope canonical pin-down (largely already done — acyclic feature DAG + linearized + affine readout).
  - Nonsmooth $A_O$ via Clarke subgradients (policy-switching kinks the current Lemma 1 covers in Lipschitz form but not differentiable form).
  - Checkpoint coverage theorem in observable terms ($P_k = I - \eta_k C_k$ where $C_k$ projects onto observation-detectable error directions).
  - Recover TST scalar form $k^d$ as uniform-per-block-gain special case of the operator product.
  - $\widehat J_F$ block-matrix estimator from TST quantities (static-dependency / co-change / strategy-DAG / semantic-reasoning / test-coverage channels).
  - Empirical validation against LLM performance degradation, tool-call-count, recovery-after-test patterns.
  - Lower-bound failure conditions (typical-case under a distribution over bias directions).

Source added 2026-10-30 by Claude Opus 5.5 (spike drain fork A): I read spikes/spike-transient-dependency-amplification.md whole and re-checked its exact-tier claims. Lemma 1 (a supremum of uniformly L-Lipschitz values is L-Lipschitz), Proposition 1 (||G_d|| = (|g| sqrt B)^d), Lemma 2 (block product and the e_{b+1} <= q e_b + eps recurrence) and the coverage formula ||P_{eta,r} G|| = max(eta sigma_1, sigma_{r+1}) are all correct as stated. Corollary 1's bound is exact in the affine sub-scope. The §6 claim that the Fisher metric is 'forced' for these operator norms overreaches: (PI) and Čencov force the metric on statistical manifolds of the model state, but the task-local z-space is not shown to be one. Land it as a recommendation, not as forced. The only canon pointer to the spike is in a Working Note (#hyp-exponential-cognitive-load:92), so it is not a canon defect. item:spikes-proposed-advanced-3-transient-dependency-amplification-and-a826 is the research continuation (constructing J_F from TST quantities). This item is the landing; the two do not duplicate.
