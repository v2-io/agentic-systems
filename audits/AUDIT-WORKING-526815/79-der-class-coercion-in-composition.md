# 79 - der-class-coercion-in-composition

Source: `01-aat-core/src/der-class-coercion-in-composition.md`

## First-pass understanding

This segment takes the wrapper from the previous segment and asks whether it is not merely separated, but a valid AAT composite agent. It verifies AAT-shaped macro state, mismatch, tempo, and sector correction under wrapper-design constraints, then assigns the wrapper a persistence condition and a tempo cost.

The intended split is good: directed separation lives in the prior segment; composition-level inheritance lives here. The main issue is that `form-composition-closure` had more gates than A1-A4. A wrapper also needs composite scope and projection admissibility, and the proof here does not yet show those.

## Diagram attempt

I drew the wrapper-composition claim as a checklist of gates. This segment mainly fills the macro-dynamics gate `(A1)-(A4)`, while the scope and projection gates remain visible as required for the full "valid composite agent" conclusion.

## Findings and watches

- F132 candidate: the theorem says satisfying (A1)-(A4) makes the wrapper a valid AAT composite agent, but `form-composition-closure` also requires `scope-composite-agent` and admissible projections `(P1)-(P3)`. This segment verifies macro-dynamics admissibility, not the full composition-closure criterion.
- F133 candidate: the setup does not show that a wrapper over one primitive black-box component satisfies `scope-composite-agent`, which was defined over multiple purposeful sub-agents or a route to composite purpose. A wrapped component may be a single agent architecture or tool scaffold rather than a composite agent unless a scope route is supplied.
- F134 candidate: D-A4 transfers sector behavior from the Tier-1 belief-update map `f_M`, but (A4) in `form-composition-closure` concerns the macro correction dynamics for composite mismatch. Strategy updates, action policy, wrapper scheduling, and component response bias can affect the full closed loop; sector behavior of `f_M` alone is not sufficient without a coupling argument.
- F135 candidate: the persistence disturbance decomposition `rho_W = rho_ext + rho_int`, with `rho_int` bounded by response variance to goal-blind queries, omits systematic response bias, leakage, nonstationary component behavior, tool/retrieval state, and wrapper parsing errors. Variance is only one internal disturbance channel.
- F136 candidate: the tempo-cost formula mixes multiplicative and subtractive accounting. If the wrapper needs `K` component calls per macro-step and the component call rate is `nu_A`, then `nu_W = nu_A/K`; tempo should scale through the reduced event rate before any additional coordination-overhead subtraction. Writing `T_W <= T_A^nominal - C_coord^wrap` needs a definition of `C_coord^wrap` that includes or excludes the `1/K` rate loss.
- F137 soft candidate: this segment inherits the unresolved double-accounting issues from `der-tempo-composition`, so Brooks's-Law tempo-cost claims should be kept conditional on a cleaned-up tempo ledger.
- F138 soft candidate: the dependency list includes out-of-order proof homes (`deriv-sector-condition`, `result-sector-persistence-template`) and omits `scope-composite-agent` if composite-agent validity remains the title claim.
- Watch: the distinction between `epsilon_track`, `epsilon_coerce`, and `kappa` is excellent and should be preserved downstream.

## Local verdict

The segment proves a useful part of the claim: a disciplined wrapper can be AAT-shaped at the macro-dynamics level. The stronger "valid AAT composite agent" conclusion needs the missing scope and projection-admissibility gates, plus a full-loop sector argument rather than an `f_M`-only argument.
