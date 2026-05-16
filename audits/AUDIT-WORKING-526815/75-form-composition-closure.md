# 75 - form-composition-closure

Source: `01-aat-core/src/form-composition-closure.md`

## First-pass understanding

This segment gives the first real composition certificate. A group is representable as a macro-agent when a projection from micro-trajectories to macro-state approximately commutes with AAT-shaped macro-dynamics. The closure defect `epsilon*` measures the best achievable state/action/observation mismatch over admissible macro-dynamics and admissible projections, with an explicit macro/micro timescale ratio `K_c`.

The segment is careful about what is chosen versus derived. The admissibility gates are formulation choices; the bridge lemma is conditional on incremental contraction beyond the one-point sector condition. The strongest local idea is the commutative-square picture: composition is not a vibe or an interface boundary, but a bounded-loss coarse-graining with an AAT-shaped macro loop.

## Diagram attempt

I drew the criterion as an approximate commuting square: true micro dynamics run across the top, projection runs down, macro dynamics run across the bottom, and the closure defect is the failure of the square to close. I added side gates for projection admissibility and macro-agent admissibility, then a bridge arrow from per-step defect to bounded trajectory error under incremental contraction.

## Findings and watches

- F108 candidate: this segment says closure applies to composites satisfying at least one of the three alignment routes, but `scope-composite-agent` now has four routes including C-iv strategic-equilibrium composites. Either closure excludes C-iv, or it needs a version whose macro-state is equilibrium-relative rather than objective-relative.
- F109 candidate: A1 requires `X_c=(M_c,G_c)` and the prose says non-scope systems have ill-defined `G_c=(O_c,Sigma_c)`. This inherits the C-iv typing issue: strategic composites do not necessarily have a shared `O_c`, so the closure formalism should state whether it is only for alignment composites or how `G_c` is generalized for strategic composites.
- F110 candidate: `epsilon*` combines `epsilon_x`, `epsilon_a`, and `epsilon_o` in one norm even though state, action, and observation errors live in different spaces and units. The segment later says norms are load-bearing, but the definition needs scaling/weighting conventions before thresholds like `epsilon* < alpha_c R_c / nu_c` are meaningful.
- F111 candidate: the component defects are evaluated over true micro-trajectories using true micro observation/action windows. This is a teacher-forced one-step closure test, not a free macro rollout. The bridge lemma can connect this to trajectory error only under the stated contraction assumptions and should also keep action/observation rollout consistency explicit.
- F112 candidate: P1 conditions on the aggregate action window over the same macro-step whose observation window is being predicted. If that action window includes within-step actions not available at the macro-boundary, the predictive-information condition is post-hoc rather than decision-time. It needs an information-set convention.
- F113 soft candidate: P3 strict dimensionality reduction conflicts with the meta-machine example if the product automaton is counted as exact composition. The product machine is exact but not reductive; it should be classified as exact representation, while closure-as-abstraction requires a smaller minimized machine or another P3-satisfying projection.
- F114 candidate: P2 says the Lipschitz projection yields a trajectory-error bound `L * epsilon* / alpha_c`, while the bridge lemma states `epsilon* nu_c / alpha_c`. These may be different measurement conventions, but the text should align them: macro-space tracking error, micro-space lifted error, and rate-scaled disturbance are distinct quantities.
- F115 candidate: the segment depends on and imports several future or external proof homes (`deriv-sector-condition`, `result-sector-persistence-template`, `der-temporal-nesting`, `deriv-critical-mass-composition`, `result-contraction-template`, multiple spikes and audits). It is clear about many conditional statuses, but local proof credit should be limited to the formulation and already-read dependencies.
- Watch: `epsilon* = 0` diagnosing representability rather than optimality is a strong and useful distinction. Keep that separation in later team/adversarial results.

## Local verdict

This is the strongest Part III segment so far. The core certificate is coherent, but it needs route typing and norm/information-set conventions tightened before downstream results can safely use `epsilon*` as a single scalar gate.
