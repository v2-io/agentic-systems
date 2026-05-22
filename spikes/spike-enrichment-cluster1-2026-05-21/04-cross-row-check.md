# §1 cluster — L4 cross-row check

*Tests the synthesis's L4 claim (line 92): "If both passes succeed and the cross-row check (against rows 03/10/14/17 of the prior-art-analysis CSVs) lands, then we have not just a new rung — we have the precise mathematical content that explains why AAT's tools converge across rows." Test: do these four rows actually reduce to the same underlying object?*

## What rows 03/10/14/17 are

Verified directly from `ref/prior-art-analysis/`:

- **Row 03 — Lyapunov persistence bounds.** Target claim: AAT's sector condition $\xi^T F(\xi) \ge \alpha \Vert\xi\Vert^2$ + the Model D ($1/\alpha$) vs Model S ($1/\sqrt\alpha$) scaling dichotomy + information-rate floors. The home segment is `#result-sector-persistence-template` + `#deriv-sector-condition`. **Mathematical object: AAT's stability certificate at R0-strict.**
- **Row 10 — Adversarial tempo and panic.** Target claim: signed-coupling unification (cooperation = adversariality with opposite sign on $\gamma$), Models D/S destabilization thresholds, superlinear adversarial scaling $b=2$ vs $b=3/2$, Effects-Spiral, resource-bounded destabilization, four-regime recipient classification. The home segment is `#der-adversarial-destabilization` + `#result-adversarial-tempo-advantage`. **Mathematical object: the *negation* of the persistence inequality with coupling-amplified disturbance — same certificate, viewed in the failure direction.**
- **Row 14 — Composition under goal divergence (strategic composition).** Target claim: when objectives partially oppose, the composition primitive is fixed-point existence/stability rather than Lyapunov contraction; sub-scope $\alpha'$ (potential / monotone games) recovers the template via the joint potential's gradient; sub-scope $\beta'$ (general games) gets only set-convergence to CCE. Home segment `#deriv-strategic-composition`. **Mathematical object: the certificate viewed at the *joint* level, with the symmetric-vs-antisymmetric structure of the joint Jacobian determining which sub-scope applies.**
- **Row 17 — Credit assignment boundary.** Target claim: persistence is credit-assignment-free (transfers from per-edge credence to plan-level mismatch via Prop B.5 of `#deriv-edge-credence-dynamics`), three independent intractability barriers (#P-hard / info-underdetermination / posterior correlation), four-level hierarchy of credit-assignment quality. Home segment `#disc-credit-assignment-boundary`. **Mathematical object: the *transfer of the certificate from one state coordinate to another* via a Jacobian — and the rank/observability conditions under which the transfer is or is not full-rank.**

## The cross-row claim under test

The synthesis's L4 hypothesis is that these four rows are facts about the same object — the certificate cone with its Helmholtz $S+A$ decomposition. Let me test this object-by-object:

### Row 03 ↔ certificate object

**Trivially yes** — Row 03 *is* the certificate object's home, at the R0-strict rung. The sector inequality $\xi^T F(\xi) \ge \alpha\Vert\xi\Vert^2$ is the AAT-internal form of the linearized certificate inequality in Euclidean metric ($\mathcal M = I$, equivalent at the linearized level to $J + J^\top \succeq 2\alpha I$); the Model D / Model S split is the disturbance-side decomposition that turns the certificate into a quantitative ultimate-bound result. Helmholtz $S/A$ does not appear directly in Row 03 because at R0-strict the symmetric part $S$ is what carries the contraction; the antisymmetric part $A$ is silently present (any non-symmetric $J$ has nonzero $A$ — the contraction depends only on $S$).

### Row 10 ↔ certificate object

**Yes, in the *destabilization* direction.** Row 10's content is *the same certificate inequality with coupling-amplified disturbance, viewed at its negation*: $B$ destabilizes when $\alpha_B R_B \lt \rho_{B,\text{base}} + \gamma_A \mathcal T_A$ — the persistence threshold of the template fails. This is *the same certificate object*, evaluated at the boundary where it stops working. The Effects-Spiral is the same boundary, locally non-linear-coupling driven; the joint-Jacobian eigenvalue formulation in `#deriv-strategic-composition` is the *symmetric-part-vs-antisymmetric-part* shift: $\mathrm{Re}(\lambda_{\max}(J_{\mathrm{joint}})) \gt 0$ is *the symmetric part $S$ has positive eigenvalue* (an unstable mode of $S$). The Helmholtz decomposition's $S$ component carries the *instability* direction; the $A$ component cycles around it but neither stabilizes nor destabilizes.

### Row 14 ↔ certificate object

**Yes, with the Helmholtz decomposition load-bearing.** Row 14's sub-scope $\alpha'$ = potential/monotone games = $J_{\mathrm{joint}} \succeq 0$ with $A_{\mathrm{joint}} = 0$ (potential case) or $S_{\mathrm{joint}} \succ 0$ (monotone case with possibly nonzero $A$). Sub-scope $\beta'$ = general games = mixed $S + A$. The boundary between them is *precisely* the question of whether the joint Jacobian's $S$-component has the structure that supports the template (positive-definite) or only structure that supports set-convergence (no metric exists making it strictly monotone). This is exactly Letcher 2019's decomposition applied at the *composite* level: $\alpha'$ is the AAT cycle in which the strict-positive $S$ component certifies R0-strict at the composite layer; $\beta'$ is the cycle in which $S$ fails to be positive-definite and only the recurrence/CCE structure remains. **Sub-scope $\alpha'$ ↔ R0-strict at composite layer; sub-scope $\beta'$ ↔ R0-loss at composite layer, with the recurrent dynamics being the analog of Conley's chain-recurrent set.**

This is the *strongest* cross-row tie. Sub-scope $\alpha'$/$\beta'$ in `#deriv-strategic-composition` is literally the AAT-internal name for the Helmholtz $S/A$ decomposition seen from one side (which scope are we in), and the R0-strict/R0-loss split is the same decomposition seen from the other (which dynamic regime do we get).

### Row 17 ↔ certificate object

**Yes, but at a different facet.** Row 17 is about the *transfer* of the certificate from per-edge credence to plan-level mismatch via $J = \nabla_p P_\Sigma$ — Prop B.5 of `#deriv-edge-credence-dynamics`. The sector condition transfers iff $J$ has bounded condition / appropriate rank; it fails to transfer in the directions where $J$ is rank-deficient (the credit-assignment underdetermination barrier). This is *the same certificate object*, but at the **boundary** facet of `#disc-stability-certificate` — the M1 boundary. The intractability barriers (#P-hard, info-underdetermination, posterior correlation) are three distinct mechanisms by which the per-edge → plan-level transfer can fail.

So Row 17 sits primarily on the **M1 boundary facet** of the certificate, with the Sylvester-mechanism (`#disc-identifiability-floor`) governing when the transfer drops rank. It is connected to R0-loss only weakly — the credit-assignment problem is about *which $\mathcal M$* (a forced-identity / M3 question via `#disc-additive-coordinate-forcing`) and *whether $\mathcal M$ stays full-rank* (a boundary / M1 question), not about whether $\kappa \gt 0$ (which is the R0-strict-vs-R0-loss question).

## What the cross-row check actually shows

**The synthesis's L4 hypothesis is partially correct but more nuanced than stated.**

The four rows are facts about the **same object — the stability certificate** — but they sit on **different facets** of `#disc-stability-certificate`'s spine:

| Row | Facet | What it is at that facet |
|---|---|---|
| 03 | Interior (R0-strict sub-region) | The contraction template; AAT-internal home of the certificate |
| 10 | Interior (boundary between R0-strict and "no certificate") | The negation of persistence under coupling — destabilization is the certificate failing |
| 14 | Interior, both sub-regions ($S+A$ decomposition) | The composite-layer split: $\alpha'$ ↔ R0-strict-composite; $\beta'$ ↔ R0-loss-composite |
| 17 | Boundary (M1) | Per-edge → plan-level certificate transfer; rank-collapse via Sylvester |

The Helmholtz $S + A$ decomposition does load-bear across rows 03/10/14 — it is the mathematical core of the regime distinction (R0-strict vs R0-loss; $\alpha'$ vs $\beta'$; persistence vs destabilization at the joint Jacobian). Row 17 connects through a different mechanism (the M1 boundary).

## L4 verdict: a *qualified* yes

**The synthesis's L4 hypothesis is correct in this qualified form:** rows 03/10/14 share the *same* underlying mathematical object — the certificate with its Helmholtz $S/A$ structure — and the R0-strict/R0-loss rung extension (proved in §02) gives the unifying vocabulary. Row 17 is part of the same spine (certificate boundary, M1 facet) but via the boundary mechanism (Sylvester) rather than the interior mechanism (Helmholtz).

**What this means for AAT's framing:**

1. The cross-row recognition is a *real* finding about the framework's internal structure. The four rows are not "four independent pillars that happen to use overlapping math" — they are three different views of the certificate's interior ($S/A$ decomposition direction) plus one view of the certificate's boundary.

2. The L4 *finding-class* claim — that the cross-row convergence is itself a *theorem about AAT* — is supportable, but the theorem is **more specific than "rows 03/10/14/17 are secretly the same"**. It is:

> **The Helmholtz $S/A$ decomposition of the linearized certificate's Hermitian-part is the unifying structure across AAT's interior cross-sectional content (rows 03 / 10 / 14 — persistence, adversarial destabilization, strategic composition). The strict-versus-loss split is the same decomposition seen from the rate side (R0-strict ↔ $S \succ 0$ dominant; R0-loss ↔ $S = 0$ pure-$A$). The M1 boundary (rank collapse via Sylvester) is a structurally separate facet (rows 17 — credit-assignment).**

This is a sharper, AAT-internal statement than the synthesis offered.

3. The *cross-row* unification belongs in `#disc-stability-certificate` (the spine) as a refinement of the four-facet table — specifically, the **Interior facet** subdivides into the $S$-component-dominant region (R0-strict) and the $A$-component-dominant region (R0-loss), with the Helmholtz decomposition naming the structure inside the Interior. This is L5 territory; see `05-fifth-facet-test.md`.

## What does NOT survive of the L4 claim

- The synthesis's casual reading of "row 17 secretly the same" — row 17 is on a *different facet* (M1 boundary). It is connected at the framework level (it is a facet of the same spine) but its mathematical mechanism (Sylvester rank-collapse) is **distinct** from the interior mechanism (Helmholtz $S/A$). Per `#disc-stability-certificate`'s own "the three obstructions are distinct — the plurality is the content" section (line 52), claiming row 17 is "the same as" rows 03/10/14 would erase exactly the plurality the spine's distinctness-of-obstructions argument established.
- Therefore the L4 finding-class should be **scoped to rows 03/10/14** — three of the four flagged rows, plus possibly other interior-facet rows (worth checking: rows 04 structural adaptation, 08 composite agency, 15 persistence stance). The fourth flagged row (17) is *connected* but as a different facet, not the same object.

## Recommendation for the verdict

L4 lands as a **refinement of the synthesis claim**, not as a defeat or as a full landing:
- The cross-row unification is real for rows 03/10/14 and adds a structural refinement of `#disc-stability-certificate`'s Interior facet (the Helmholtz $S/A$ decomposition is the AAT-internal name for the strict/loss split, and the certificate-interior is best read as a 2-component decomposition rather than a featureless interior).
- Row 17 is connected through the spine but via the M1 boundary facet, not via the Interior. Saying "rows 03/10/14/17 are secretly the same" overreaches — saying "rows 03/10/14 are facets of the certificate interior under Helmholtz $S/A$; row 17 is a facet of the certificate boundary under Sylvester rank-collapse; both are facets of the same spine" is honest.

L5 question: does this refinement of the Interior facet justify a fifth facet for the spine? Tested in `05-fifth-facet-test.md`.
