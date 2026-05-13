# Spike: Finding 10 — `#form-information-bottleneck` status repair

**Date:** 2026-04-22
**Source finding:** `audits/pending-findings-2026-04-22.md` Finding 10 (lines 367–389)
**Target segment:** `01-aad-core/src/form-information-bottleneck.md`
**Downstream consumer:** `01-aad-core/src/disc-compression-operations.md`
**Effort:** ~15 min (smallest item in the 2026-04-22 batch)
**Status of this spike:** ready for Joseph's review; no segment edits made.

## 1. Problem in one sentence

`#form-information-bottleneck` is currently labeled `status: discussion-grade` and described as "a *formulation*," but `#disc-compression-operations` now leans on it as a rigorous rate-distortion fixed point — the (P1) admissibility derivation is explicitly "the Lagrangian-dual of IB" via Cover & Thomas §I.12–13. The status undersells what the theory actually depends on.

## 2. Tier-vocabulary mapping

The finding doc proposed the label "exact formulation (external theorem: Tishby et al. 1999)." That phrase does not exist verbatim in `FORMAT.md`. Mapping options against `FORMAT.md`'s `status` enumeration (`axiomatic`, `exact`, `robust-qualitative`, `heuristic`, `conditional`, `empirical`, `discussion-grade`, `sketch`):

| Candidate | Fit | Reasoning |
|---|---|---|
| `exact` | **Best fit** | "Mathematically validated under stated assumptions." Tishby–Pereira–Bialek 1999 is a published theorem; the IB optimum and its rate-distortion duality are established under the standard assumptions (finite alphabets / well-defined mutual informations, the Markov chain $Y - X - T$). The segment imports the result and binds it to AAD objects ($\mathcal C_t$, $M_t$, future observations). That is exactly what `exact` is for: a mathematical statement holding under explicit assumptions. |
| `axiomatic` | Plausible second | Used in `#def-pearl-causal-hierarchy` for the imported Bareinboim et al. hierarchy. "Axiomatic" can read as "we accept this as foundational input from outside the theory." But the connotation is *foundational to AAD*; IB is not foundational to AAD's chain in the same way the causal hierarchy is — IB is a *characterization* of optimal compressions, not a postulate the theory rests on. `exact` is closer. |
| `conditional` | Wrong | Implies dependence on AAD-local assumptions that need verification per use site. The IB theorem's assumptions are general and do not require per-site recheck. |
| `discussion-grade` | Wrong (current) | "Argued qualitatively or by analogy, not derived." Misrepresents what IB is. |
| Custom label "exact (external)" | Not recommended | The vocabulary already accommodates this case via `exact`. Adding a tag would be a parallel system. The right place to mark "this is external" is the Epistemic Status prose, not a new status enum value. |

**Recommendation: `status: exact`**, with the Epistemic Status paragraph carrying the "external theorem, applied to AAD" qualifier in prose. Precedent: `#der-causal-hierarchy-requirement` is `type: derived, status: exact` and its derivation rides on the imported Bareinboim hierarchy — the import is acknowledged in prose, the status reflects the resulting epistemic strength.

**Type field.** Currently `type: formulation`. Per `FORMAT.md`, `formulation` means "Representational or modeling choice (could be different)" — the implication being that other formulations would also fit. Once the segment is reframed as the application of an external theorem to AAD's $(\mathcal C_t, M_t, o_{t+1:\infty})$ binding, the *binding* is a formulation choice but the *theorem* is not. Two reasonable framings:

- **Keep `type: formulation`.** Honest: AAD chooses to characterize $\phi^\ast$ via IB rather than via, e.g., MDL or a Bayesian sufficiency criterion. The choice of compression-trade-off framework is representational. The theorem is then external machinery the formulation invokes.
- **Change to `type: definition`.** The segment defines $\phi^\ast$ for AAD via the IB optimum; treating it as a defining equation for "optimal AAD compression" is also defensible.

Recommend **keep `type: formulation`** — the segment is choosing IB as the lens, not defining $M_t$ (which is defined elsewhere in `#form-agent-model`). The status upgrade carries the load; the type stays.

## 3. Proposed new frontmatter (full block)

```yaml
---
slug: information-bottleneck
type: formulation
status: exact
depends:
  - form-agent-model
stage: deps-verified
---
```

Only `status` changes (`discussion-grade` → `exact`). `type`, `depends`, and `stage` are unchanged.

Note on stage: the segment is currently `deps-verified`. A status change is a content-level edit, not a dependency change, but Gate 2 (claims-verified) involves a label audit — so this very change is the kind of thing Gate 2 catches. Strictly speaking the segment remains at `deps-verified`; this spike's edit is the kind of correction that pushes it toward `claims-verified` rather than away from it.

## 4. Proposed new Epistemic Status section

Replace the existing single paragraph with:

> *Exact, applied external theorem.* The IB optimum and its rate-distortion characterization are an external result (Tishby, Pereira & Bialek 1999, "The information bottleneck method," *Proc. 37th Allerton*; with the rate-distortion / Lagrangian-dual reading standard, see Cover & Thomas §I.12–13). This segment is *not* a novel formulation: it is an exact statement of that theorem under AAD's binding $X = \mathcal C_t$, $T = M_t$, $Y = o_{t+1:\infty} \mid a_{t:\infty}$, with the Markov chain $Y - X - T$ holding by construction (the model state has access to history but not directly to future observations). The choice to characterize the optimal compression $\phi^\ast$ via IB rather than via, e.g., MDL or a Bayesian-sufficiency criterion is a *representational choice* (hence `type: formulation`); given that choice, the form of $\phi^\ast$ and its trade-off structure are exact consequences of the imported theorem.
>
> What this segment is *not* a claim about: how actual agents compute their models. No agent explicitly solves the IB optimization (variational IB in deep-learning practice is a parametric approximation). The segment characterizes the optimum, not the procedure. The trade-off parameter $\beta$'s dependence on environmental volatility $\rho$ and policy $\pi$ stated in the Formal Expression is at a different epistemic tier — the qualitative direction (volatile favors compression, stable favors retention) is *robust-qualitative* across agent classes; specific functional forms are not derived here.
>
> Max attainable: *exact* for the IB-as-applied-theorem core (already at ceiling); *robust-qualitative* for the $\beta(\rho, \pi)$ dependence claims. The downstream use in `#disc-compression-operations` — treating IB as the shared shape of four AAD compression operations and deriving (P1) as the IB Lagrangian-dual — relies on this segment's exact reading; the cross-instance unification claim itself remains *robust-qualitative*, which is a property of `#disc-compression-operations`, not of this segment.

This rewrite (a) names the external theorem and citation explicitly, (b) names the AAD binding ($X, T, Y$) so the reader can see what is imported vs. supplied, (c) preserves the existing honest disclaimer that no agent literally solves IB, (d) flags the tier difference between the IB core and the volatility-dependent-$\beta$ discussion, and (e) makes explicit that `#disc-compression-operations` is what now leans on the exact reading.

## 5. Vocabulary-mapping verdict

The project's `FORMAT.md` vocabulary is sufficient — no extension needed. `exact` cleanly covers "mathematically validated theorem, even when imported from outside." The "external theorem" qualifier belongs in prose (Epistemic Status section), not in a new status enum value. Precedent: `#der-causal-hierarchy-requirement` (type: derived, status: exact) uses the same pattern — relies on the imported Bareinboim et al. hierarchy, named in prose.

The one alternative worth flagging for Joseph: if a future architectural pass identifies a *systematic* class of "imported external results," a small vocabulary extension (e.g., a `provenance: internal | external` field orthogonal to `status`) would let the project surface that distinction at the index level without watering down `status`. Not recommended *for this spike* — would be over-elaboration on a 15-min item — but worth keeping in the audit-cycle backlog if the cross-segment scan in §6 turns up enough cases to make it worthwhile.

## 6. Cross-segment scan: other candidates for the same external-theorem-vs-internal-derivation distinction

Segments that grep'd as referencing external machinery (Pearl, Bareinboim, Tishby, Cover & Thomas, Chechik) and whose status labels deserve a similar look in a future pass. **Not fixing here — flagging only.**

| Segment | Current frontmatter | External machinery invoked | Pass-flag rationale |
|---|---|---|---|
| `#def-pearl-causal-hierarchy` | type: definition, status: axiomatic | Pearl/Bareinboim three-level causal hierarchy | Already uses `axiomatic` to mark "imported foundation." Reasonable; possibly worth aligning the convention with the IB fix (use `exact` + prose qualifier instead of `axiomatic`?). Not urgent. |
| `#der-causal-hierarchy-requirement` | type: derived, status: exact | Application of Bareinboim et al. to $Q_O$ evaluation | Already `exact`. Confirms the precedent the IB fix follows. Likely fine; verify the Epistemic Status prose names the import explicitly (parity with the proposed IB rewrite). |
| `#deriv-graph-structure-uniqueness` | type: derivation, status: conditional | Causal Markov Condition theorem (P3 → Markov) | Currently `conditional` — appropriate, since the result is conditional on causal sufficiency. The external-theorem reliance is honest in the existing prose. Probably no change; worth reviewing alongside the IB pass for consistency. |
| `#disc-compression-operations` | type: discussion, status: robust-qualitative | Cover & Thomas §I.12–13 (rate-distortion duality), Chechik et al. 2005 (Gaussian IB) | Status is honest about the unification claim being robust-qualitative; the (P1) Lagrangian-dual derivation embedded in the segment is `derived`-grade per its inline tag. Possibly worth promoting the (P1) sub-derivation to its own segment with `type: derived, status: exact` so the exact result is not buried inside a robust-qualitative parent. |
| `#def-strategy-dag`, `#form-strategy-complexity-cost` | (not inspected in detail this pass) | MDL / coding-theoretic bounds | Cross-flag: if the IB fix lands, a parallel pass on `#form-strategy-complexity-cost`'s DL-vs-$I$ relationship in the Epistemic Status would maintain symmetry across the four IB instances. |
| `#result-unity-closure-mapping` | (not inspected) | Rate-distortion / Gaussian IB (Chechik et al.) | Working Notes on Gaussian IB frontier derivation are deferred (see `#disc-compression-operations` Working Notes). When promoted, would be in the same family as the IB fix. |

**Pattern across candidates.** The project mostly handles imported external results well by using internal status tiers (`exact`, `axiomatic`, `conditional`) plus prose qualifiers naming the citation. The IB segment is the visible outlier where the prose under-claims. No systemic vocabulary problem identified — the convention is "use the standard tier; name the import in prose."

## 7. Independence from O-BP2

The finding doc notes Finding 10 would be subsumed by O-BP2 (four compressions as one hierarchy). **Confirmed: the local fix is independently correct and can be applied now without waiting for O-BP2.**

Reasoning:

- **The fix is a label-accuracy correction**, not a structural commitment. It says "IB is an exact applied external theorem," which is true regardless of whether AAD eventually adopts a single compression-as-hierarchy framing or keeps four parallel instances.
- **Under O-BP2 (if adopted)**, IB would still be the "shared shape" of the unified hierarchy. Its status as `exact` would carry through — the hierarchy framing changes the *role* IB plays (one shared shape vs. four parallel instances), not the *epistemic status* of IB itself.
- **Under O-BP2 not being adopted**, the four-instance presentation continues; `#disc-compression-operations` continues to use IB as the (P1) anchor; the status correction prevents the labeling drift the finding identifies.
- **No risk of churn.** The frontmatter delta is one field. The Epistemic Status rewrite is local and does not anticipate any structural decision. If O-BP2 lands later and rewrites the segment more deeply, this prose is easy to absorb.
- **Cost of waiting.** While the segment carries `discussion-grade`, the audit-trail asymmetry in §6 risks compounding: a reader noticing that `#disc-compression-operations`'s (P1) derivation depends on a "discussion-grade" upstream might either overestimate the upstream's strength (incorrectly accepting the derivation as more solid than the chain supports) or underestimate the chain (incorrectly weakening (P1)'s status). Both are avoidable by the local fix.

The finding's "subsumed by O-BP2" note is correct as a portfolio observation but does not argue for waiting. The local fix is strictly better-than-status-quo and orthogonal to the architectural decision.

## 8. Summary of deliverables for Joseph

1. **Frontmatter change:** one line, `status: discussion-grade` → `status: exact`.
2. **Epistemic Status rewrite:** three-paragraph replacement (text in §4 above).
3. **No other edits to `#form-information-bottleneck`** — Formal Expression and Discussion are unaffected; the volatility-dependent-$\beta$ discussion is appropriately left as-is and tier-flagged in the new Epistemic Status.
4. **No edits to `#disc-compression-operations`** — its existing Epistemic Status correctly labels the shared-shape claim discussion-grade and the (P1) derivation as derived; the upstream fix removes the labeling tension without requiring downstream changes.
5. **Cross-segment flags** in §6 for a possible future consistency pass.

If approved, this is a single-segment edit. If Joseph wants to pull in any of §6's flagged segments for a synchronized "external-theorem labeling" pass, that becomes a small batched cycle rather than a single-file fix — still well under an hour total.
