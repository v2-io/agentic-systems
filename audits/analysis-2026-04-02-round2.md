# AAD Core Review — Round 2 Integration (2026-04-02)

**Sources:** Codex round 2 (5 findings), fresh Claude instance (full review), plus the round 1 synthesis (`analysis-2026-04-02-synthesis.md`).

**What's already been done this session:** Tier 0 (metadata fixes, ordering, loop-interventional Q-learning fix), Tier 1 (persistence disambiguation, tempo redundancy caveat, canonical continuation convention, CIY segment move, passive-observer consistency, dependency fixes), Tier 2a (OR-node spike), and a Section II worked example.


## What's New in Round 2

### Convergence with Round 1

Both reviews confirm the round 1 findings:
- Section I's Lyapunov core is the strongest part
- The strategy-maintenance loop is incomplete (signal function, credit assignment, identifiability)
- The composition bridge lemma has a contraction gap
- The persistence disambiguation (our Tier 1a fix) is called "the cleanest and most defensible contribution" by Codex

### Genuinely New Findings

**1. The update-gain → sector-condition bridge (Claude, high priority)**

The theory's softest structural joint. The sector-condition-derivation ASSUMES GA-3 (the correction function satisfies the sector condition). But whether η*-based updates actually produce sector-satisfying dynamics is never derived — it is assumed. The entire quantitative prediction chain (persistence thresholds, adversarial scaling, adaptive reserve) flows through this unproven bridge.

The single-edge spike verifies this for Beta-Bernoulli (the correction IS exactly linear, so the sector condition holds trivially). But the general case — "does the uncertainty-ratio gain principle produce correction dynamics that satisfy the sector condition?" — is the real question, and it's open.

This is not in our round 1 synthesis. It should be.

**2. The do(.) notation bug in causal-hierarchy-requirement (Codex #2, quick fix)**

VERIFIED: Line 21 of causal-hierarchy-requirement.md writes `a_t = a` in ordinary conditioning. Value-object.md correctly writes `do(a_t = a)`. The formal expression drops the do(.) operator exactly where the theorem depends on it. The prose says it's an intervention, but the equation doesn't show it.

**3. Stale blocker in directed-separation-under-composition (Codex #5, quick fix)**

VERIFIED: Line 55 says admissibility constraints "remain placeholders." But composition-closure now has (A1)-(A4) and (P1)-(P3). The segment is stale — it makes the composition argument look less mature than it is.

**4. Scope split not clean enough (Codex #1)**

Our round 1 passive-observer fix (adding caveat paragraphs to scope-condition and agent-spectrum) doesn't go far enough. Codex wants a clean structural split: an *adaptive-core scope* (observations + model + uncertainty — includes passive trackers) and a narrower *agency scope* (adds causal effect — the full scope condition). Currently, "within AAD's scope" is ambiguous because both scopes exist in the same segment.

**5. "Forced graph structure" language still oscillates (Codex #3)**

The strategy-dag Discussion (line 95) says "DAG structure is *strongly motivated* by operational postulates, not *forced* in the mathematical sense." But other segments and the OUTLINE still use "forced" language. The acyclicity-is-proved / Markov-is-conditional distinction needs to be enforced more strictly.

**6. Loop interventional claim still too strong (Codex #4)**

Our Tier 0d fix narrowed the Q-learning example. But Codex says the opening claim and the "exact" status are still too strong. The loop generates "action-conditioned outcome data with potential interventional content" — not identified estimates of P(o|do(a)). The later regime machinery (A/B/C) is the right discipline, but the earlier claim should be softened.

**7. Additional epistemic label fixes (Claude)**

| Segment | Current | Issue | Recommended |
|---------|---------|-------|-------------|
| model-sufficiency | status: exact | Definitions are definitional, not "exact" | status: axiomatic |
| recursive-update | type: derived, status: exact | C3 is definitional, so the result is "exact given formulation" | Add qualifier in Epistemic Status |
| directed-separation | type: derived | More an architectural observation than a derivation | type: derived + scope (matches OUTLINE) |
| adversarial-destabilization | status: exact | T_A treated as exogenous — a strong simplification | status: conditional |

**8. Undefined load-bearing quantities (Claude)**

Three quantities are referenced heavily but have no formal definition segment:
- The mismatch transform `g`: used in update-gain's update rule and NOTATION.md
- Environment change rate `ρ`: half the persistence inequality
- Critical mismatch threshold `δ_critical`: now more prominent after the persistence disambiguation

**9. Orphaned formalism (Claude)**

- information-bottleneck: no downstream segment formally uses the IB objective. It provides conceptual framing only.
- Between-event dynamics g_M(M_τ): defined in recursive-update but never referenced elsewhere
- Multi-channel formalism (U_o^(k), ν^(k)): largely unused beyond the definition

**10. The fluid-limit bridging assumption (Claude, GA-5)**

The discrete-to-continuous gap. The mismatch ODE is valid when η* ≪ 1, but the regime where η* is NOT small (initialization, after structural change) is when predictions matter most. The error introduced by the fluid limit is never formally bounded.


## Priority Assessment: What to Do Next

### Quick Fixes (can do now, < 30 min total)

**QF1. Fix do(.) notation in causal-hierarchy-requirement.** One equation edit: `a_t = a` → `do(a_t = a)`.

**QF2. Fix stale blocker in directed-separation-under-composition.** Update line 55 to acknowledge that (A1)-(A4) and (P1)-(P3) are now specified. Change "remain placeholders" to "are specified in #form-composition-closure."

**QF3. Fix model-sufficiency status.** `exact` → `axiomatic` (it's a definition).

**QF4. Fix adversarial-destabilization status.** `exact` → `conditional` (T_A exogenous).

**QF5. Add qualifier to recursive-update Epistemic Status.** Note that the result is "exact conditional on the state-completeness formulation (C3)."

### Design Decisions (need Joseph's input)

**DD1. Scope architecture.** Codex wants a clean split into adaptive-core scope (passive trackers welcome) and agency scope (causal effect required). Three options:
- (a) Split scope-condition into two segments: `adaptive-scope` (conditions 1, 4 only) and `agency-scope` (adds conditions 2, 3)
- (b) Keep one segment but add a formal "scope levels" subsection distinguishing what requires which conditions
- (c) Leave as-is with the current caveat paragraphs (Codex says this isn't enough)

**DD2. Loop-interventional-access status.** Codex wants the "exact" status softened. Options:
- (a) Change status to `conditional` ("conditional on the identification conditions being met")
- (b) Keep `exact` but clarify the claim is about data CHARACTER (exact) not identified estimates (conditional)
- (c) Split the segment: the data-character claim is exact, the identification claim is regime-dependent

**DD3. "Forced" graph structure language audit.** How aggressively to demote — should strategy-dag's Discussion be rewritten, or just ensure consistency with the existing honest assessment in graph-structure-uniqueness?

### Medium-Priority Work (next session)

**MP1. The update-gain → sector-condition bridge.**
This is the most important new finding. The question: does the uncertainty-ratio gain principle produce correction dynamics satisfying GA-3? The single-edge spike showed it for Beta-Bernoulli (trivially, since the correction is exactly linear). A spike investigating whether this holds for:
- (a) Gaussian updates (Kalman gain → does the Kalman correction satisfy the sector condition?)
- (b) General exponential family updates
- (c) Approximate updates (gradient descent, variational)

The Kalman case should be tractable: the Kalman gain K produces correction F(δ) = Kδ, which is linear, so α = eigenvalue of K. This would extend the bridge to the theory's most important worked example.

**MP2. Formal definitions for ρ, δ_critical, and g.**
These are referenced everywhere but formally homeless. Either give them definition segments or consolidate them into a "core quantities" segment.

**MP3. Demote discussion-grade segments in Section III.**
unity-dimensions, shared-intent, auftragstaktik-principle carry structural weight beyond their epistemic status. Either formalize them or reduce how much the narrative leans on them.


## What Both Reviews Confirm About the Theory's State

The "three rings of rigor" framing from the Claude review is the sharpest characterization:
1. **Inevitability core** (~15 segments): Lyapunov stability, mismatch decomposition, acyclicity, orient-cascade ordering — these are real results
2. **Canonical formulations** (~20 segments): the DAG, IB, state lift, gain principle — well-motivated choices
3. **Empirical/heuristic enrichment** (~25 segments): adversarial exponents, gain heuristics, unity dimensions — testable claims

The theory's greatest risk (Claude): "the distance between its architectural ambition and its formal achievement." The honest epistemic labeling protects against overclaiming, but much of the agent-level machinery is sketch/hypothesis/discussion-grade.

The theory's greatest opportunity (Claude): "promoting segments from draft to candidate through convergent depth." The scaffolding is in place; the next phase is tightening, not expanding.

Both reviews independently recommend the same next steps:
1. Complete the strategy-revision loop (signal function, credit assignment)
2. Add a purposeful composite worked example
3. Tighten the update-gain → sector-condition bridge
4. Formalize the G_t complexity bound
5. Bound the fluid-limit approximation error


---

## Spike Results: The Gain → Sector Condition Bridge (2026-04-02)

Two spikes completed, investigating the theory's softest structural joint:

### Spike 1: Kalman Case (`spikes/spike-gain-sector-bridge.md`)

**Result:** For the Kalman filter, the sector condition is DERIVED, not assumed. The sector parameter α = K (scalar case) = η* exactly. The bridge holds because the correction is linear (F(e) = KHe) and KH has non-negative eigenvalues in the (P⁻)⁻¹-weighted inner product.

**Generalization:** The "Gain-to-Sector Bridge Theorem" — the gain-based update satisfies the sector condition whenever the mismatch transform g has **directional fidelity** (B1): δᵀg(δ) ≥ c‖δ‖². For optimal Bayesian updates, B1 holds by construction. Five failure modes precisely characterized: directional infidelity, gain collapse, nonlinear saturation, unobservable directions, model misspecification.

### Spike 2: Nonlinear / Gradient Descent Case (`spikes/spike-gain-sector-bridge-nonlinear.md`)

**Result:** For any gradient-based agent, GA-3 is **mathematically equivalent** to local strong convexity of the loss function. The equivalence is exact:

    α = η · μ,  where μ = λ_min(∇²L) is the strong convexity modulus
    R = radius of the largest ball where ∇²L remains positive definite

**Classification verified by simulation (6 experiments):**
- Quadratic loss: GA-3 global (R = ∞), α = η · λ_min(H)
- L2-regularized convex: GA-3 global, α ≥ η · λ
- Exponential family (natural params): GA-3 global, subsumes Beta-Bernoulli spike
- Unregularized logistic: GA-3 global but α → 0 at infinity
- Non-convex (mixtures, neural nets): GA-3 LOCAL only, R = basin of attraction
- Quasi-convex: technically local, α decays to zero

**Key insight:** The structural-adaptation trigger (#result-structural-adaptation-necessity) IS the loss landscape's inflection surface (basin boundary). When mismatch exceeds R, the agent has been pushed out of its convexity basin and needs structural change — exactly what the theory predicts.

### Combined Assessment

GA-3 transforms from "opaque global assumption" to "derivable conditional result":

    gain principle + directional fidelity (B1) →[derived]→ sector condition
    gradient descent + local strong convexity →[equivalent]→ sector condition

**Recommendation:** Keep GA-3 as a named assumption (it covers non-gradient agents too) but add a derivation note documenting the equivalence. The assumption is not eliminated but made transparent and verifiable.


## Promotion Plan: Gain-Sector Bridge → Segment

### Step 1: Write the segment (`01-aad-core/src/der-gain-sector-bridge.md`)

A new segment combining the results of both spikes:
- **Type:** derived
- **Status:** conditional (conditional on B1: directional fidelity, or equivalently, local strong convexity for gradient agents)
- **Depends:** update-gain, sector-condition-derivation, sector-condition-stability
- **Formal Expression:** The Gain-to-Sector Bridge Theorem (B1 + positive gain → sector condition with α = η* · c_min). The gradient equivalence as a corollary (α = η · μ for gradient agents).
- **Epistemic Status:** Conditional derivation. Exact for optimal Bayesian updates and gradient descent on strongly convex losses. Local for non-convex losses. Does not cover non-gradient agents.

### Step 2: Reclassify GA-3 in NOTATION.md

Change GA-3 from "Global Assumption" to:
> GA-3: Sector condition. Derived from the gain principle when the update rule has directional fidelity (B1); see #der-gain-sector-bridge. For gradient-based agents, equivalent to local strong convexity of the loss. Remains an independent assumption for non-gradient agents.

### Step 3: Update sector-condition-derivation.md

Add a note at the top of the Assumptions section: GA-3 is derivable from the gain principle under B1, not merely assumed. The Lyapunov proofs are unchanged — they operate downstream of GA-3 regardless of how it is established.

### Step 4: Update worked-example-kalman.md

Derive α from the Kalman gain (α = K = P⁻/(P⁻ + R_obs)) rather than reporting it "from data." This closes the worked example's last semi-empirical step.

### Step 5: Update persistence-condition.md

Add to Common Properties: "The α-T relationship is now grounded: for linear correction, α = T exactly; for gradient-based correction on strongly convex losses, α = η · μ where μ is the strong convexity modulus. The empirical observation that α is monotone in T is derived for these cases."

### Step 6: The weighted-norm subtlety

In the matrix Kalman case, the sector condition holds in the (P⁻)⁻¹-weighted norm, not Euclidean. For fully observable systems with bounded condition number κ(P⁻), the norms are equivalent up to κ(P⁻). Add a brief note to sector-condition-derivation.md acknowledging this: the Euclidean Lyapunov function V = ½‖δ‖² is sufficient for the scalar case and the well-conditioned matrix case; the weighted Lyapunov function V = ½eᵀ(P⁻)⁻¹e is the proper generalization.


## What This Unblocks

With the bridge formalized, Section I's promotion bottleneck shifts:

**Resolved by bridge:**
- GA-3 is no longer an opaque assumption — it's derivable for all well-designed agents
- The α-T relationship is grounded, not merely empirical
- The worked-example-kalman can be fully derived

**Remaining Section I bottlenecks:**
1. Formal definitions for ρ, δ_critical, and the mismatch transform g (quick — definitions, not derivations)
2. The fluid-limit bridging assumption GA-5 (real math — bounding the discrete-to-continuous error)
3. The scalar ODE imprecision (caveat paragraph, not a blocker)

**Section II bottleneck:** Signal function for edge revision (unblocks strategy loop closure)

**Section III bottleneck:** Purposeful composite worked example (validates admissibility machinery with G_t)


---

## Round 3 Integration (Codex + fresh Claude)

### Quick Fixes Done

1. **Dependency cycle** (Codex #7): gain-sector-derivation depended on gain-sector-bridge AND vice versa. Fixed by removing bridge from derivation's depends (the derivation backs the bridge, not vice versa).
2. **κ_processing conditioning** (Codex #4): I(G_t; M_{τ+} | e_τ) inflated by prior goal-model correlation. Fixed to I(G_t; M_{τ+} | e_τ, M_{τ-}) — measures extra goal information, net of what was already in the prior.
3. **Plan confidence marking** (Codex #8): worked-example-strategy marked P̂_Σ as "Exact" but strategy-dag says correlated failure makes it systematically overestimate. Fixed to "Exact (computation)" with caveat.

### New Issues Requiring Attention

**N1. Strategy persistence mismatch state gap (Codex #1).** The schema says the candidate mismatch is δ_strategic (from strategic-calibration — value-increment residuals). But the derivation appendix uses δ_k = p̂_k − θ_k (raw edge credence error). These are different quantities. The appendix validates a *surrogate* (Beta-Bernoulli edge error), not the *operational diagnostic* the theory exposes.

This is a real gap but not a fatal one — the derivation shows the sector-condition machinery *works* for strategy dynamics. The mapping from δ_strategic (value residuals) to edge-credence errors requires the credit-assignment machinery that is acknowledged as open. The honest framing: "sector conditions are verified for per-edge credence error; promotion to the operational diagnostic δ_strategic requires solving credit assignment."

**N2. Strategic persistence is instantaneous (Codex #2).** α_Σ = 1/(n+1) decreases with experience. The sector check is time-varying and local in time, not a fixed persistence bound. The gain-collapse analysis in the single-edge spike addresses this (the forgetting fix stabilizes α), but the surrounding prose sometimes reads as if persistence is a permanent property. Should be clarified: "persistence holds at any given experience level; the critical experience n* = R_Σ/ρ_Σ − 1 is the horizon where gain-collapse threatens."

**N3. Passive tracker scope (Codex #3, recurring).** Three rounds now. The caveat paragraphs aren't satisfying reviewers. Decision needed: formal scope split or accept the ambiguity.

**N4. Composition assumes AAD-shaped macro-agents (Codex #6).** The admissibility class (A1-A4) requires AAD state decomposition, macro mismatch, macro tempo, and sector-stable correction. This is a constrained representation test, not scale-invariance. Honest acknowledgment needed in composition-closure.

**N5. Team tempo should have redundancy as a first-class term (Codex #5).** We added the caveat but correlated observations are the *default* in multi-agent settings. The additive formula with a footnote caveat understates the issue.

### What Both Reviews Confirm (Steady State)

- Section I is strong, especially with the gain-sector bridge
- The satisfaction-gap / control-regret diagnostic is the cleanest §II contribution
- Strategy-revision loop remains the weakest formal chain
- 67 segments at draft, 0 past draft — promotion is the priority
- tempo-composition already correctly labeled "sketch" (both reviewers flagged it but the metadata was already right)

### Promotion Readiness

The updated FORMAT.md now has a formal four-gate promotion workflow. Both reviewers independently identified the same ~8 segments as closest to candidate:

1. sector-condition-derivation
2. recursive-update-derivation
3. mismatch-decomposition
4. chain-confidence-decay
5. satisfaction-gap + control-regret
6. worked-example-kalman
7. persistence-condition
8. gain-sector-bridge

These should be promoted in topological order per FORMAT.md. The dependency leaves (segments with no dependencies or only definitional dependencies) go first.
