# ACT Core Review — Round 2 Integration (2026-04-02)

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

Our round 1 passive-observer fix (adding caveat paragraphs to scope-condition and agent-spectrum) doesn't go far enough. Codex wants a clean structural split: an *adaptive-core scope* (observations + model + uncertainty — includes passive trackers) and a narrower *agency scope* (adds causal effect — the full scope condition). Currently, "within ACT's scope" is ambiguous because both scopes exist in the same segment.

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

**QF2. Fix stale blocker in directed-separation-under-composition.** Update line 55 to acknowledge that (A1)-(A4) and (P1)-(P3) are now specified. Change "remain placeholders" to "are specified in #composition-closure."

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
