# Sub-Spike D: Coercion-ε* vs. Fidelity-ε* Disambiguation

**Status**: clarification. Brief.
**Date**: 2026-05-09
**Depends on**: `01-theorem-statement.md`, `#form-composition-closure` (the bridge lemma).

---

## 1. The two readings

The closure-defect $\varepsilon^*$ from `#form-composition-closure` is defined as the infimum, over admissible projections and macro-dynamics, of a per-macro-step prediction-error norm. The bridge lemma reads it as a *fidelity* measure: how well the macro-dynamics tracks the micro-dynamics under the chosen projection.

In the wrapping construction, the macro-dynamics deliberately *coerces* the underlying component into a different (Class-1-shaped) behavior than the component would exhibit on its own. The wrapping construction is in some sense the *opposite* of fidelity-preservation — it's making the macro-system *not* track the component's native dynamics in the goal-conditioning direction.

This needs disambiguation.

## 2. The two quantities

**$\varepsilon^*_\text{track}$ — the standard fidelity quantity.** Per `#form-composition-closure`:

$$\varepsilon^*_\text{track} = \inf_{\Lambda, (\pi_c, E_c, f_c)}\, \mathbb{E}_\tau\big[\, \big\| \Lambda_x(X_{\text{micro}, mK_c}) - f_c(\Lambda_x(X_{\text{micro}, (m-1)K_c}), \Lambda_o(\cdot)) \big\| \,\big]$$

This measures how well the macro-dynamics predicts the projection of the next micro-state given the projection of the previous micro-state and the aggregated observation window. *Lower is better.* $\varepsilon^*_\text{track} = 0$ means the macro is a perfect compression of the micro.

**$\varepsilon^*_\text{coerce}$ — the wrapping-specific quantity.** Define:

$$\varepsilon^*_\text{coerce} = \mathbb{E}_\tau\big[\, \big\| f_W(X_W, o_W; A(q_M), A(q_G)) - A^\text{native}(X_\text{init}, o_W) \big\| \,\big]$$

where $A^\text{native}$ denotes the underlying component's native (un-wrapped) behavior, given the same input as the wrapper produced. This measures how *different* the wrapper's behavior is from running $A$ directly. *Higher means more aggressive coercion.*

For a wrapper that does nothing (passes through $A$'s output unchanged), $\varepsilon^*_\text{coerce} = 0$ and the wrapping has accomplished nothing. For a wrapper that maximally coerces $A$ into Class-1 shape, $\varepsilon^*_\text{coerce}$ measures how much the underlying behavior had to change to enforce the structural separation.

## 3. The two quantities measure different things

- $\varepsilon^*_\text{track}$ is about projection compression: can the macro-state plus a coarse-graining-aware prediction reproduce the projected micro-trajectory? Used in `#form-composition-closure`'s bridge lemma to bound the trajectory error of the macro-system under the persistence template.

- $\varepsilon^*_\text{coerce}$ is about behavioral divergence: how different is the wrapper's behavior from the unwrapped component? Used to measure the *cost* of structural separation. In some sense, the coercion is the *purpose* of the wrapping — we *want* the wrapper to differ from the unwrapped component in the goal-conditioning direction (otherwise the wrapper hasn't separated anything).

## 4. The relationship

$\varepsilon^*_\text{track}$ and $\varepsilon^*_\text{coerce}$ are not the same quantity, but they are related:

$$\varepsilon^*_\text{track} \le \varepsilon^*_\text{coerce} + \varepsilon_\text{micro-projection}$$

where $\varepsilon_\text{micro-projection}$ is the irreducible compression error from projecting $A$'s state into $X_W$ (independent of any coercion). Heuristically: the wrapper-vs-truth error is bounded by wrapper-vs-component plus component-vs-truth.

This bound is loose. A wrapper that aggressively coerces $A$ into Class-1 shape (large $\varepsilon^*_\text{coerce}$) can still have low $\varepsilon^*_\text{track}$ if the coercion is *toward* what the projection needs.

## 5. Which quantity to use where

For AAT's existing machinery:
- The **persistence template** (`#result-sector-persistence-template`) at wrapper level uses $\varepsilon^*_\text{track}$. The bridge-lemma bound $\lim\|e_m\| \le \varepsilon^*_\text{track} \nu_W / \alpha_W$ governs the wrapper's tracking accuracy of the projected micro-system.
- The **wrapping cost analysis** uses $\varepsilon^*_\text{coerce}$. This is a measure of how much the wrapper changes the system; high coercion may be the design intent (forcing Class-1 status).
- The **leakage analysis** (sub-spike C) uses neither — leakage is bounded by mutual-information / KL-divergence in the response distribution, not by trajectory error.

## 6. Naming and segment-level practice

Recommendation for downstream segment work:

- Continue using $\varepsilon^*$ in `#form-composition-closure` and the bridge lemma for the standard tracking quantity. Add a Discussion clarification: in the wrapping construction, this is $\varepsilon^*_\text{track}$.
- Introduce $\varepsilon^*_\text{coerce}$ as new vocabulary in any wrapping-specific segment, with the explicit definition above. Mark it clearly as a *different quantity from the bridge lemma's $\varepsilon^*$*.
- Use $\kappa_\text{W₁}$ / $\kappa_\text{W₂}$ from sub-spike C for leakage rates — these are KL-divergence quantities, not trajectory-error quantities, and the distinction is structural.

The three quantities — $\varepsilon^*_\text{track}$ (trajectory), $\varepsilon^*_\text{coerce}$ (behavior), $\kappa$ (information leakage) — should each have their own bound and their own role. Conflating any two would propagate confusion in segment-level work.

## 7. Honest scope

This sub-spike is a definitional clarification, not a new derivation. Both $\varepsilon^*_\text{track}$ and $\varepsilon^*_\text{coerce}$ inherit their per-quantity bounds from the existing bridge-lemma machinery and the wrapping construction's data-processing inequality respectively. The clarification's value is *preventing confusion* in downstream segment work where the wrapping construction's $\varepsilon^*$ might otherwise be conflated with the bridge lemma's.

---

## File index

- This file: `04-epsilon-semantics.md`
- Brief: `00-brief.md`
- Theorem: `01-theorem-statement.md`
- Leakage: `03-leakage.md`
- Tempo cost (next): `05-tempo-cost.md`
