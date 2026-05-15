---
slug: spike-operator-family-unification
type: spike
status: exploratory
created: 2026-05-14
depends:
  - result-sector-persistence-template
  - result-contraction-template
  - deriv-sector-condition
  - der-gain-sector-bridge
  - form-composition-closure
  - disc-identifiability-floor
  - disc-separability-pattern
  - disc-additive-coordinate-forcing
---

# Spike: Operator-Family Unification — the real-deal push

**This is the deep push of the C1 question.** The predecessor `spikes/.integrated/spike-operator-sector-unification.md` (2026-04-22) returned an honest *2-instance-plus-1-consequence* verdict and a prior co-owner recommendation "land content, DO NOT elevate to fourth meta-pattern." This spike does not accept that as the end. It pushes until either (a) a genuine unifying mechanism is uncovered and verified, or (b) the unification fails at a *precisely characterized boundary* whose no-go is itself the load-bearing result. Per `feedback_strengthen_before_soften` and the no-go-as-result discipline: push the math as far as it goes at every angle; a sharp no-go is a success, not a retreat.

## The question, sharpened

Joseph's framing (2026-05-14, paraphrased from the SP-22 exchange): is an operator-family meta-segment the *strongest thing for the theory*? My prior judgment was: not as SP-22 bundles it (nine heterogeneous Tier-2 spikes wearing a meta-segment costume), but there is a version — the **O-BP10-anchored four-axis quartet** — that would be among the strongest, gated on whether the projection-contraction restatement is *provably* equivalent to the persistence condition rather than typographically analogous.

So the real question is **not** "should we write `#operator-family-template`?" It is:

> **Is there a single object of which M1 (identifiability-floor), M2 (separability-pattern), M3 (additive-coordinate-forcing), and the operator-sector contraction mechanism are four faces — or do they sit on genuinely distinct axes, and if so what is the sharp obstruction to unifying them?**

The honest answer to *that* determines whether the meta-segment is a spine (strong) or a bin (weak).

## What counts as success

Three legitimate completion states (per `feedback_spike_agent_briefing`):

1. **Succeed-beyond-claim:** a single object is found of which the four meta-patterns are verified projections, and the unification is *forced* (not merely matched), making the operator-family segment the spine of AAD's cross-sectional structure.
2. **Succeed-at-claim:** the unification holds as a *viewpoint* (one object, multiple faces) but the faces are genuinely distinct because each names a different *failure mode* of that one object — still strong, but the meta-segment is "the spine M1/M2/M3 are failure-projections of," not a fourth parallel pattern.
3. **Sharp no-go:** the unification provably cannot hold; the obstruction is named with a structural mechanism (not "they're just different"). This is load-bearing — it tells future agents exactly why the four axes are irreducible.

All three are reportable wins. The failure mode to avoid is the *soft* retreat: "partial, 2+1, park it" without pushing each obstruction to a sharp statement.

## Prior-work map (gathered 2026-05-14 via memorata-search, scoped to `~/src/agentic-systems`)

The adjacent efforts, and what each already established:

- **`spikes/.integrated/spike-operator-sector-unification.md` (C1, 2026-04-22)** — the predecessor. Operator-sector primitive defined for endomorphisms `T: ℋ→ℋ` with single fixed point `x*`. Verdict: Instances A (ODE flow), B (discrete update), B' (edge update, Fisher-weighted), C' (composite macro-update) fit; **projection Λ does not fit** ("not an endomorphism; different spaces"). A2'/β recasts cleanly as Bauschke-Combettes operator-family classification. *The accepted frame constraint — endomorphism + single fixed point — is the seam this spike pushes.*
- **`spikes/spike-jacobian-b1-strengthening.md` §6 "Angle 5: (SOC) second-order-curvature axiom"** — directly adjacent to the curvature-unification line. Established: **(SOC) — the AAD metric = ∇²Φ at the operating point** — unifies Bayesian (Fisher), gradient (Hessian), Kalman ((P⁻)⁻¹), **but is "matched-coordinate adjacent," NOT uniqueness-theorem-forced.** Only Angle 3 (PI + Čencov) clears the additive-coordinate-forcing discipline, and *only for statistical-manifold agents*. The Lyapunov-metric cases (linear-Hurwitz-non-symmetric, PID-bounded-plant) have a metric **selected by plant dynamics, not objective curvature** — no Φ exists. **This is a verified counterexample to the naive "potential structure Φ is the unifying object" hypothesis. Respect it.**
- **`spikes/.integrated/spike-mori-zwanzig-composition.md` (2026-04-20)** — the projection-side prior result. MZ trajectory bound ε* ≥ C‖K‖ does NOT close (type mismatch: ε* per-step vs ‖K‖ trajectory-accumulation). What DOES close: the **zero-lag kernel bound ε* ≥ ‖Q_Λ U P_Λ‖_op** when the MZ-optimal closure f_c^MZ = P_Λ U P_Λ is not in 𝓜_adm. The memory kernel is the irreducible residue of projection.
- **`01-aat-core/src/result-unity-closure-mapping.md` Working Notes** — Koopman/MZ cross-check: the non-degenerate Kalman case exercises the zero-lag memory kernel K₀ with ‖K₀‖ scaling with |ΔK| (update-rule heterogeneity).
- **O-BP10** (PROPOSALS Bundle 1; naming-cycle candidate "contraction-over-drift principle") — *"an adaptive system is a projection whose contraction rate exceeds its target's drift rate."* Explicitly **not yet at segment level.** This spike's verification of (or no-go against) the O-BP10 equivalence is the keystone.
- **M3 `#disc-additive-coordinate-forcing`** self-describes as "layer-specific manifestations of a single geometric object" (exponential-family Legendre-Fenchel). The precedent that a strong meta-pattern is *one object, many faces* — the bar.

## The three attack lines (and why the naive one is already dead)

- **Attack 3 (curvature operator) — partially dead on arrival.** "The unifying object is the equilibrium curvature ∇²Φ; the four meta-patterns are its spectral facts." Jacobian-b1 §6.4 already falsifies the strong form: the Lyapunov-metric linear-Hurwitz-non-symmetric case is operator-sector *in the right metric* but has **no potential Φ** (the field is not a gradient). So ∇²Φ cannot be the unifying object — it doesn't exist widely enough. *Verification caught the plausible-but-false leg before assertion.* What survives this is the question: what is the object that is wider than a potential but still unifies?
- **Attack 1 (Mori-Zwanzig projection-as-operator).** Reframe Λ not as a between-spaces surjection but as the **idempotent projection operator P (P²=P) on the full space ℋ_micro** — which *is* an endomorphism, dissolving the C1 "category mismatch." Then ask: is ε* exactly the operator-defect of the MZ memory term Q U P? Prior result says the zero-lag kernel bound closes; push whether it is the *projection-side instance of the same obstruction* that kills Attack 3's potential structure on the dynamics side.
- **Attack 2 (set-valued / firmly-nonexpansive frame).** A projection is the resolvent J_A of A=∂ι_C and is firmly nonexpansive with a *fixed-point set* (its range), not a single fixed point. Generalize the C1 operator-sector primitive from "fixed point x*" to "closed convex equilibrium set." Untouched by prior work — the genuinely new push.

## The emerging spine hypothesis (to be verified or broken, not asserted)

Synthesizing the prior-work constraints: the unifying object cannot be a potential Φ (Lyapunov counterexample) and cannot be a single-fixed-point endomorphism (Λ). The candidate that survives both is the **equilibrium-Jacobian stability certificate**: by the converse-Lyapunov theorem, the linearization is Hurwitz **iff** there exists a quadratic metric in which the dynamics is strongly monotone (operator-sector). That metric exists *more widely* than a potential (it covers the Lyapunov-plant cases) and is an endomorphism-level object (no Λ category problem at the certificate level).

If this survives verification, the structure would be:

- **Spine:** AAD's dynamical core = the local spectral theory of the equilibrium Jacobian; operator-sector ⟺ "Hurwitz interior + Lyapunov-metric certificate."
- **M2 separability** = where the certificate *exists* (scope: Jacobian Hurwitz on the ball).
- **M3 additive-coordinate-forcing** = *which coordinate forces* the certificate — Čencov makes it unique (Fisher) only in the statistical sub-case; elsewhere matched, not forced.
- **M1 identifiability-floor** = the certificate's *boundary / rank-collapse* — Jacobian eigenvalue on the imaginary axis / curvature drops rank; the floor is the **boundary of the Hurwitz region** (a domain and its boundary are dual, definitionally not unifiable into one interior statement).
- **Composition** = whether *projection preserves* the certificate; the MZ memory kernel is exactly the obstruction (Hurwitzness not preserved under non-invariant-subspace projection).

That would be **completion-state 2 (succeed-at-claim)**: one object (the stability certificate), four faces, each face a distinct *failure mode* of the one object — and a sharp tri-faced no-go (non-forced certificate / boundary-not-interior / projection-destroys-certificate) as the load-bearing core. The deepest single statement would be the **integrability obstruction**: the non-gradient residue (dynamics side, Helmholtz) ≅ the memory kernel (composition side, Mori-Zwanzig) ≅ the rank-deficiency (identifiability side) — three faces of one failure-of-integrability.

**Status: hypothesis. Every leg below must be verified, not assumed.** The Lyapunov counterexample already shows the cost of asserting structural inevitability before checking. Files `01–`/`02–` push and test each leg; `99-verdict.md` synthesizes honestly to whichever of the three completion states the mathematics actually reaches.

## Leg ledger (to be discharged)

| # | Leg | Status |
|---|---|---|
| L1 | Operator-sector (one-point, at fixed pt) in *some* inner product ⟺ linearized Jacobian Hurwitz (converse-Lyapunov). One-point-vs-incremental gap (C1 §3.2) handled honestly. | open |
| L2 | The certificate metric is *forced* only in the Čencov sub-case; *matched* (existence-only) elsewhere — i.e., re-derive jacobian-b1 §6/§7 verdict as the M3-face statement, not re-litigate it. | open |
| L3 | M1 identifiability-floor ⟺ certificate boundary (Jacobian non-hyperbolic / curvature rank-drop). Test against the actual M1 instances (Bareinboim CHT, Cramér-Rao rank-1, Liberzon common-Lyapunov-nonexistence, Čencov). | open |
| L4 | Λ-projection no-go ⟺ MZ memory kernel = the certificate's non-preservation under projection; is it the *same* obstruction as L3's rank-drop (integrability)? | open |
| L5 | Synthesis: which completion state; is the operator-family segment a spine, a bin, or a sharp-no-go record; landing recommendation honest to the verdict. | open |
