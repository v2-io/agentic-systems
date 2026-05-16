# Reflection: der-orient-cascade

## What the segment does

Derives the 5-step orient cascade — the forced resolution order of epistrophe for actuated agents. The ordering is forced by information dependency:
1. Reduce δ_epistemic (understand reality)
2. Evaluate δ_sat (is goal achievable?)
3. Evaluate δ_regret (is policy suboptimal?) → 2×2 diagnostic
4. If δ_regret high: (4a) plan-level calibration via δ_s, (4b) edge-level localization, (4c) causal-sufficiency check (L0→L1 escalation)
5. If δ_sat > 0 persists: (5a-5d) escalate before revising O_t; objective revision is the last resort

The ordering is forced — not a design choice. Each step's input depends on the prior step's output.

## The 2×2 diagnostic in context

The orient cascade is where the satisfaction gap / control regret 2×2 diagnostic becomes *operational*. Each cell prescribes a different corrective action, and the cascade embeds these prescriptions in the resolution order. The cascade is what makes the diagnostic actionable rather than just descriptive.

## The L0→L1 escalation (step 4c)

The most novel part of the cascade — detecting causal insufficiency from within L0. The signal: persistent δ_s ≈ 0 (edge credences converged) coinciding with persistent negative plan-outcome residuals (y_G < P̂_Σ on average). This means the DAG is causally insufficient and L0 calibration converges to a biased target. The diagnostic is pairwise sibling covariance under an augmented test.

The key ordering constraint: don't escalate to L1 augmentation before edge credences have converged — the signal (persistent covariance after convergence) needs the convergence precondition to be reliable. In non-stationary environments where credences keep drifting, L1 augmentation may be the default rather than gated on 4c's signal.

## G_t complexity bounded by M_t capacity

This is the headline finding: "Σ_t's evaluable complexity is bounded by M_t's ability to observe which strategy edges are intact." An agent with poor model sufficiency cannot meaningfully evaluate a complex strategy DAG.

The virtuous/vicious cycle observation: better M_t → richer evaluable Σ_t → better-directed action → faster M_t improvement. The vicious cycle (degraded M_t → strategy simplification → cruder action → further degradation) is the strategic analog of the persistence condition death spiral.

## Boyd OODA connection

"Orient is the critical step, not Decide." The cascade formalizes this: Orient resolves the information dependencies that make Decide meaningful. An agent that skips to strategy revision without adequate model update will revise based on stale or incorrect beliefs. Whether the cascade captures Boyd's actual cognitive process is explicitly flagged as an empirical question.

## Naming targets

"Orient cascade" is the segment name. The 2×2 diagnostic table concept has entries in the tracker. The "virtuous/vicious cycle" pattern.

The timescale ordering (ν_epistemic ≫ ν_edge-update ≫ ν_γ-reclassify ≫ ν_prune/graft ≫ ν_O-revision) is a practical result but flagged as "empirical observation, not derived."

## Wandering thoughts

The cascade's "content progressed, ordering exact" status is a clean epistemic split: the logical structure (what must precede what) is exact; the specific content of each step (what the credit assignment looks like, how timing works) is harder. The segment explicitly acknowledges this.

The convention hierarchy's effect on the cascade: the ordering is convention-independent, but the *inferential force* scales with the convention. C1 gives local heuristics; C3 gives global conclusions. The cascade's ordering is what makes it useful for any convention.

How valuable: 10/10 for load-bearing (the orient cascade is the action-facing interface of all the Section II machinery), 9/10 for surprise (the step 4c L0→L1 escalation is a sophisticated and honest diagnostic protocol).
