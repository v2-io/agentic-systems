# Spike: Finding 13 — `#strategy-dag` L1-Default Narrowing

**Status:** Spike — proposed promotion-ready repair text for `01-aad-core/src/strategy-dag.md`.
**Date:** 2026-04-22
**Source finding:** `msc/pending-findings-2026-04-22.md` Finding 13 (lines 457–482).
**Companion material:** `msc/spike-L1-worked-example.md` (strict-vs-soft handling at line ~276); `01-aad-core/src/worked-example-L1.md` (already-published L1' treatment, lines 120–136); `msc/SPIKES.md` line 43.

---

## 1. Summary of the Repair

Finding 13 says the right caveats already live in `#strategy-dag` — Correlation Hierarchy paragraphs identify L1 as the sweet spot only for **strict-prerequisite** common causes (line 105), name **L1' (mixture form)** as the soft-facilitator regime (line 107), and acknowledge that formal transfer for L1' is open (line 118). The defect is not content but **placement and headline**: the segment's headline contract (line 20) and end-of-hierarchy default (line 122) generalize "use L1 by default" beyond the regime the segment actually supports. A reader who stops at the headline applies L1 to soft-facilitator cases — the opposite failure mode from L0.

The repair has three moves:

- **(M1)** Narrow line 20 ("Strategy-layer exactness contract") to scope L1's transfer guarantee to strict-prerequisite common causes, naming L1' (open) and direct L2 modeling for soft facilitators.
- **(M2)** Narrow line 122 (end-of-hierarchy default) symmetrically — the practical default depends on whether the binding common causes are strict prerequisites or soft facilitators.
- **(M3)** Promote the strict-vs-soft distinction structurally: insert a brief **Scope** sub-bullet inside the Formal Expression's Correlation Hierarchy table (after the L0/L1/L2 row block, before the L0 paragraph) so the regime split is visible to readers who only scan the formal layer.

The deep-discussion paragraphs at lines 105–118 stay essentially as-is — they already do the work; the issue is their being load-bearing material that the headline overrides. The Scope sub-bullet acts as a forward-pointer so the headline cannot be read in isolation.

L1' becomes a first-class label in the Correlation Hierarchy table (a fourth row), not a bullet buried in the L1 paragraph. This is consistent with `01-aad-core/src/worked-example-L1.md` lines 130–134 and `01-aad-core/src/approximation-tiering.md` line 34 already treating L1' as a named regime.

---

## 2. Proposed Revised Passages

### 2.1 Line 20 — Strategy-layer exactness contract

**Current (verbatim):**

> **Strategy-layer exactness contract.** All formal results in AAD's strategy layer — the sector condition transfer ( #strategic-dynamics-derivation, Prop B.5), the persistence schema ( #strategy-persistence-schema), the gradient-based credit assignment ( #credit-assignment-boundary) — are proved under **L0 (independence)**: causally sufficient DAGs with independent edge outcomes. **L1 (augmented DAG with explicit common-cause nodes) is the practical default in complex domains** where correlated failure is typical (adversarial, organizational, infrastructure-dependent settings). L0 formal results transfer exactly to correctly constructed L1 DAGs, because L1 restores causal sufficiency by construction. See the Correlation Hierarchy below for the full treatment.

**Proposed (verbatim):**

> **Strategy-layer exactness contract.** All formal results in AAD's strategy layer — the sector condition transfer ( #strategic-dynamics-derivation, Prop B.5), the persistence schema ( #strategy-persistence-schema), the gradient-based credit assignment ( #credit-assignment-boundary) — are proved under **L0 (independence)**: causally sufficient DAGs with independent edge outcomes. **L0 formal results transfer exactly to correctly constructed L1 DAGs *for strict-prerequisite common causes*** — common causes whose absence forces dependent children to fail ($\theta_{\text{child} \mid \neg C} \approx 0$), e.g. shared infrastructure, gating permissions, required resources. In this regime L1 (augmented DAG with explicit common-cause nodes) is the practical default for complex domains where correlated failure is typical (adversarial, organizational, infrastructure-dependent settings). **Soft-facilitator common causes** — those whose absence merely degrades success ($\theta_{\text{child} \mid \neg C} \gt 0$) — fall outside this transfer guarantee. They require **L1' (mixture form)**, for which the formal transfer through Prop B.5b has not been derived (open), or **direct L2 modeling** at exponential cost. See the Correlation Hierarchy below for the full treatment.

**Why this version.** Keeps the L0-results-transfer-to-L1 commitment but binds it to the regime where the transfer is actually proved. Names L1' and L2 directly so the reader knows which row of the hierarchy table soft facilitators belong to. The "open" qualifier is exact — `#strategic-dynamics-derivation` Prop B.6 covers L1 strict only; the corresponding L1' proposition does not exist.

---

### 2.2 Line 122 — End-of-hierarchy default

**Current (verbatim):**

> **The default assumption in complex environments should be L1, not L0.** Agents in adversarial, organizational, or infrastructure-dependent domains should expect correlated failure and invest in identifying common causes for explicit representation. L0 is appropriate for domains with genuinely independent risks (independent parallel experiments, diversified portfolios with low correlation) and as a computational stepping stone during strategy construction. Treating L0 as the default leads to systematic overconfidence — the agent believes it has more redundancy than it actually does (OR-nodes) or more fragility than it actually does (AND-nodes).

**Proposed (verbatim):**

> **The default assumption in complex environments should be L1 for strict-prerequisite common causes, L1' for soft facilitators — not L0 for either.** Agents in adversarial, organizational, or infrastructure-dependent domains should expect correlated failure, identify the common causes that bind, and **classify each as strict or soft** before choosing the augmentation. Strict prerequisites (shared infrastructure, gating permissions, required resources) are L1's regime: factor the common cause above the correlation it creates, and L0 formal results transfer losslessly. Soft facilitators (favorable conditions, supportive culture, enabling but non-essential resources) require L1' or — when the parametric cost of mixture form is itself prohibitive — explicit L2 conditioning over the relevant common-cause states. **Misclassifying a soft facilitator as a strict prerequisite is a real failure mode**, symmetric to L0's overestimation: the AND-prerequisite construction forces $P(\text{sub-plan} \mid \neg C) = 0$ and systematically *understates* success when $C$ is absent. L0 remains appropriate for domains with genuinely independent risks (independent parallel experiments, diversified portfolios with low correlation) and as a computational stepping stone during strategy construction. Treating L0 as the default leads to systematic overconfidence (illusory redundancy at OR-nodes, illusory fragility at AND-nodes); treating L1 as the default *for soft facilitators* leads to the symmetric understatement.

**Why this version.** The "L1 vs L0" headline becomes the regime-dependent statement the segment actually supports. The misclassification failure mode is named explicitly — it currently appears only as an aside at line 114 ("the opposite failure mode from L0's overestimation") and is easy to miss.

---

### 2.3 Correlation Hierarchy table (line 97–102) — promote L1' to a first-class row

**Current rows (verbatim):**

| Level | Model | When correct | $\hat P_\Sigma$ status | Computation |
|---|---|---|---|---|
| **L0: Independence** | AND/OR propagation as-is | Causally sufficient DAG (all common causes explicit) | Correct probability | $O(\lvert V\rvert + \lvert E\rvert)$ |
| **L1: Augmented DAG** | Common-cause nodes added explicitly; AND/OR propagation on augmented graph | Augmented DAG is causally sufficient | Correct for augmented graph | $O(\lvert V'\rvert + \lvert E'\rvert)$, larger graph |
| **L2: Full correlation** | Arbitrary joint failure distribution over edges | Always (but requires specifying the full joint) | Correct | Exponential in general |

**Proposed rows (verbatim):**

| Level | Model | When correct | $\hat P_\Sigma$ status | Computation |
|---|---|---|---|---|
| **L0: Independence** | AND/OR propagation as-is | Causally sufficient DAG (all common causes explicit) | Correct probability | $O(\lvert V\rvert + \lvert E\rvert)$ |
| **L1: Augmented DAG (strict prerequisites)** | Strict-prerequisite common-cause nodes added explicitly; AND/OR propagation on augmented graph | Augmented DAG is causally sufficient *and* every modeled common cause has $\theta_{\text{child} \mid \neg C} \approx 0$ | Correct for augmented graph | $O(\lvert V'\rvert + \lvert E'\rvert)$, larger graph |
| **L1': Mixture form (soft facilitators)** | Conditional sub-DAGs weighted by common-cause state: $\hat P_\Sigma = \theta_C \cdot P_\Sigma(G \mid C) + (1-\theta_C) \cdot P_\Sigma(G \mid \neg C)$ | Soft-facilitator common causes ($\theta_{\text{child} \mid \neg C} \gt 0$); per-edge credences split into $p_{ij \mid C}$, $p_{ij \mid \neg C}$ | Correct for the weighted combination; **formal transfer of L0 results through Prop B.5b is open** | $O(\lvert V'\rvert + \lvert E'\rvert)$ per common cause; doubles parametric footprint for affected edges |
| **L2: Full correlation** | Arbitrary joint failure distribution over edges | Always (but requires specifying the full joint) | Correct | Exponential in general |

**Scope sub-bullet** (insert immediately after the four-row table, before the L0 paragraph):

> *[Discussion (regime classification)]* **Choosing among L1, L1', and L2 requires classifying each common cause.** $\theta_{\text{child} \mid \neg C} \approx 0$ → L1 (factor above the correlation). $\theta_{\text{child} \mid \neg C} \gt 0$ → L1' (mixture form) or L2 (explicit conditioning). Strategies in mixed environments (some strict, some soft common causes) combine L1 factoring for the strict and L1' mixtures for the soft. Treating all common causes as strict prerequisites under L1 alone systematically *understates* success on soft-facilitator branches — the symmetric failure mode to L0's overestimation.

**Why this version.** Promotes L1' from a bullet inside the L1 discussion paragraph to a row in the table — it is already first-class in `#worked-example-L1` and `#approximation-tiering` line 34, so this aligns the canonical hierarchy presentation with the supporting segments. The Scope sub-bullet is the structural lift Finding 13 calls for: it puts the regime split inside the Formal Expression block where the headline reader will encounter it before the L0 paragraph, not buried in the L1 discussion paragraph 9 lines later.

The "formal transfer ... is open" status for L1' is honest — it is exactly what `#strategic-dynamics-derivation` line 513 says. No promotion of L1' beyond what the spike material supports.

---

## 3. Side-by-Side Diff Summary

| Location | Current direction | Proposed direction | Net change |
|---|---|---|---|
| Line 20 (headline contract) | "L1 is practical default in complex domains" + "L0 results transfer to L1" | "L0 results transfer to L1 *for strict prerequisites*"; soft facilitators → L1' (open) or L2 | Scope-narrows the headline; introduces L1' at first mention |
| Line 97–102 (hierarchy table) | Three rows (L0, L1, L2) | Four rows; L1 row gains "strict prerequisites" qualifier; L1' row added | Promotes L1' to first-class label |
| Insertion after table | (none) | Scope sub-bullet on regime classification | Strict-vs-soft visible inside Formal Expression |
| Line 105 (L1 sweet-spot paragraph) | unchanged | unchanged | Already correct; now the *expansion* of the headline rather than a buried caveat |
| Line 107 (L1' bullet) | unchanged in content | unchanged in content | Now backed by a table row, not introducing the term |
| Line 114 (gap statement) | unchanged | unchanged | Becomes consistent with revised line 122 |
| Line 118 (open formal transfer) | unchanged | unchanged | Now consistent with table-row "open" annotation |
| Line 122 (default statement) | "L1 not L0" | "L1 for strict, L1' for soft, not L0 for either" + named misclassification failure | Symmetric framing |

No edits proposed to: the Acyclicity, Single-parameter edges, Epistemic Status, Discussion, or Working Notes sections. The Discussion paragraph at line 164 (edge independence as consequence of causal sufficiency) and the L1 remedy paragraph at line 170 are unaffected by this narrowing — they describe what L1 augmentation does, which the revised headline still permits.

---

## 4. Cross-Segment Check

Segments that take "L1 by default" or reference the L0→L1 escalation. For each, whether the cross-reference remains correct after narrowing.

| Segment | Reference site | Reads "L1 by default"? | Status after narrowing |
|---|---|---|---|
| `#strategy-persistence-schema` | line 66 (Scope: $\delta_s$ at L0; L1 inherits) | No | **Correct as-is.** Says "for L1 (augmented DAG), the same persistence result applies to the augmented graph's $\hat P_\Sigma$" — silently means L1-strict (the case Prop B.6 actually covers). Recommend a clarifying parenthetical at next promotion: "(strict-prerequisite L1; L1' transfer is open)". Not blocking. |
| `#strategy-persistence-schema` | line 111 (Working note: B.6 confirms L1 transfer) | No | **Correct as-is.** B.6 is L1-strict by construction. |
| `#strategic-dynamics-derivation` | Prop B.6 (line 278), L0 comparison (327), summary table (343) | No | **Correct as-is.** Prop B.6 is explicitly the strict-prerequisite case (uses $\theta_{i \mid \neg C} = 0$). Already names L1' as the open extension at line 513. |
| `#orient-cascade` | Steps 4c, 5b, 5d (lines 48, 56, 60); line 71 commentary | No | **Correct as-is, but check.** Step 4c says "directs the agent to add common-cause nodes" — under the narrowing, this should read "and classify each as strict or soft, choosing L1 or L1' accordingly". One-line addition recommended at next pass. The escalation logic itself does not change. |
| `#strategic-calibration` | line 48 (Plan-confidence error scope) | No | **Correct as-is.** Already says "For L1 (augmented DAGs with explicit common-cause nodes), $\delta_s$ of the augmented graph tracks calibration within the augmented model, which is more accurate." Implicitly L1-strict; aligns with revised headline. |
| `#credit-assignment-boundary` | line 58 (L0 vs L1 interaction) | No | **Correct as-is.** Says "The principled fix is L1: add common-cause nodes to restore causal sufficiency, then apply gradient attribution to the augmented DAG." Recommend a clarifying parenthetical "(L1 for strict prerequisites; L1' for soft facilitators is the open generalization)" at next promotion. Not blocking. |
| `#causal-insufficiency-detection` | line 67ff (From Detection to L1 Construction) | Yes — implicitly | **Correct as-is, but check.** The 4-step procedure ends with "Restructure the DAG: factor $C$ above the correlated siblings ( #strategy-dag, L1 construction principle)." Under the narrowing this works *only* when $C$ is a strict prerequisite. If $C$ is soft, the agent should construct L1' instead. Recommend adding a Step 3a: "Classify $C$ as strict or soft. If strict, factor above ($\to$ L1). If soft, build mixture form ($\to$ L1'); see #worked-example-L1 §When Correct L1 Construction Is Not Possible." Not blocking but the sharpest cross-segment dependency. |
| `#independence-audit` | lines 47, 83, 120 | Yes — "L1 augmentation" as the named repair | **Correct as-is, but check.** Line 47: "Repair operation: L1 augmentation — add common-cause nodes and restructure the DAG so each common cause is factored *above* the correlation it creates." Under narrowing, this is the strict-prerequisite repair; soft facilitators need L1'. Recommend revising to "L1 augmentation (strict prerequisites) or L1' mixture form (soft facilitators)". Not blocking. |
| `#approximation-tiering` | lines 14, 34, 54, 71 | Mentions L0/L1/L2 trio | **Already aligned.** Line 34 row in the meta-table mentions "L1 is unbiased on augmented graph" without committing to the "default" framing. This segment never claims L1-as-default; it describes the tiering meta-pattern. Recommend the meta-table entry be updated to the four-tier hierarchy (L0/L1/L1'/L2) at next promotion to match the revised `#strategy-dag` table. Not blocking. |
| `#worked-example-L1` | lines 120–136 | No — already explicit | **Already aligned.** This segment is the canonical home of strict-vs-soft + L1' (lines 122, 130–134). The revised `#strategy-dag` headline now matches what this worked example already teaches. |
| `01-aad-core/OUTLINE.md` | line 165 (approximation-tiering description), 182 (worked-example-L1 description) | No | **Correct as-is.** Recommend changing line 165 from "L0/L1/L2" to "L0/L1/L1'/L2" once the table row is promoted; cosmetic. |
| `02-tst-core/src/*.md` | (none reference L1 default) | n/a | **No changes needed.** TST segments depend on `#strategy-dag` for DAG semantics, not for the correlation hierarchy. |

**Net cross-segment status.** No downstream segment is *broken* by the narrowing — all current references can be read as implicitly scoped to L1-strict, which is the case the underlying propositions actually cover. The narrowing surfaces five places where a one-line clarifying parenthetical would tighten the cross-reference: `#strategy-persistence-schema` (×2 sites), `#orient-cascade` (step 4c), `#causal-insufficiency-detection` (Step 3a insertion), `#credit-assignment-boundary` (line 58), and `#independence-audit` (line 47). All non-blocking; all queueable for next promotion of those segments.

---

## 5. L1' Labeling Status

After this repair:

- **L1' is a first-class label** in the Correlation Hierarchy table (row 3 of 4).
- **L1' is named in the headline contract** (line 20 revised) at the same depth as L0/L1/L2.
- **L1' is named in the default statement** (line 122 revised) as the soft-facilitator default.
- **L1' formal transfer status remains "open"** — explicitly tagged in the table row ("formal transfer of L0 results through Prop B.5b is open"), in the revised headline contract ("for which the formal transfer through Prop B.5b has not been derived (open)"), and consistent with `#strategic-dynamics-derivation` line 513 and `#worked-example-L1` line 134.
- **L1' is *not* promoted to "exact"** anywhere in this spike. The only formally derived L1 result is Prop B.6 for strict prerequisites; L1' inherits per-conditional-sub-plan sector parameters but the weighted-combination layer's transfer through B.5b is unverified.

This is consistent with the spike material (`msc/spike-L1-worked-example.md` does not derive L1' formally; `01-aad-core/src/worked-example-L1.md` line 134 explicitly notes the open status).

---

## 6. Open Questions for Joseph

1. **Insertion point for the Scope sub-bullet.** The proposal places it *immediately after* the L0/L1/L1'/L2 table and *before* the L0 explanation paragraph (currently line 103). Alternative: place it as a third paragraph inside line 20 (the exactness contract), so the headline block itself contains the regime classification. Tradeoff: the sub-bullet placement keeps the headline shorter but distributes the message; the in-headline placement is more emphatic but lengthens line 20 substantially. Preference?

2. **Should the Scope sub-bullet be `*[Discussion]*` or `*[Scope]*`?** I tagged it `*[Discussion (regime classification)]*` because it interprets the table rather than restricting domain. But the substantive content — "choosing among L1/L1'/L2 requires classifying each common cause" — has the flavor of a scope rule. `*[Scope]*` is not in FORMAT.md's enumerated equation tags; the closest options are `*[Discussion]*` or a new `*[Scope]*` tag (which `#and-or-scope` uses in its body). Confirm tag preference.

3. **Frontmatter status change?** Current `status: conditional`. The narrowing tightens the conditions under which L1's headline guarantee holds; the conditional status is unchanged. No frontmatter edit proposed. Confirm.

4. **Promotion of the cross-segment one-liners.** Five segments (above table) would benefit from a clarifying parenthetical at next promotion. Should this spike batch them into a "follow-on" finding, or leave them as latent items to be picked up when each segment is next touched? My read: leave as latent — they're not blocking and batching them risks expanding scope into Finding 1's territory.

5. **OUTLINE.md table cell.** Line 165 currently reads "Meta-pattern: L0/L1/L2, C1/C2/C3, Tier 1/2/3 as common structure". After this repair, should it become "L0/L1/L1'/L2"? My read: yes, but cosmetic; bundle with other OUTLINE touch-ups rather than as part of this finding's promotion.

6. **Naming: L1' vs L1.5.** `msc/SPIKES.md` line 43 says "L1.5 / L1' soft-facilitator case flagged as gap". The published segments (`#worked-example-L1`, `#strategic-dynamics-derivation`, `#approximation-tiering`) all use L1'. This spike sticks with L1'. Confirm SPIKES.md line 43 should be updated to drop "L1.5" at next pass.

7. **Misclassification failure mode — name it?** The revised line 122 names it descriptively ("treating all common causes as strict ... systematically *understates* success on soft-facilitator branches"). Worth a named diagnostic alongside L0's $+\rho$ overestimation? E.g., a "soft-facilitator suppression bias" with magnitude $-\theta_C \cdot P_\Sigma(G \mid \neg C) \cdot (1-\theta_C)$? That would be a Finding-1-adjacent move and is out of scope for this spike, but flagging it.

---

## 7. Effort and Confidence

**Effort delivered:** ~35 min, within the 30–45 min budget Finding 13 specifies.

**Confidence:** High that the revised text is faithful to the existing segment material and the spike corpus. The repair adds no new content not already present somewhere in the segment or in `#worked-example-L1`; it relocates and re-emphasizes. Risk is purely editorial (does the new headline read naturally, does the insertion point flow). Joseph should review the prose for cadence; the substantive narrowing is correct.

**Not in scope.** This spike does not touch Finding 1 (broader Correlation Hierarchy refactor), does not derive L1' formally, does not edit any segment file, does not edit cross-segment references beyond identifying them. All five cross-segment one-liners are latent items, not part of this delivery.
