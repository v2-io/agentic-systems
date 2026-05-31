# Reflection: hyp-mismatch-dynamics

## What the segment does

States the linear ODE $d\|\delta\|/dt = -\mathcal{T} \cdot \|\delta\| + \rho(t)$ as a heuristic for mismatch dynamics. Provides steady-state solutions for both deterministic and stochastic disturbance models. Explicitly labeled as heuristic (first-order linear approximation).

## Naming targets surfaced

The segment references "mismatch injection rate" which is target row 99. Let me look at the discussion: $\rho(t)$ is called "environment change rate" in this segment. But the card says "mismatch injection rate" is an alternative. Let me check what the canonical name should be.

## The deterministic vs stochastic scaling difference

The deterministic steady state: $\|\delta\|_{ss} = \rho/\mathcal{T}$ — linear in disturbance rate, inverse in tempo.
The stochastic RMS: $\|\delta\|_{rms} = \sigma_w/\sqrt{2\mathcal{T}}$ — square root in disturbance amplitude, inverse square root in tempo.

This is significant: correction is less effective against noise than against drift. The $1/\sqrt{\mathcal{T}}$ vs $1/\mathcal{T}$ scaling means doubling tempo reduces deterministic mismatch by 2× but only reduces stochastic mismatch by $\sqrt{2} \approx 1.41\times$.

## The adversarial scaling

The adversarial coupling: when $A$'s actions increase $B$'s disturbance rate, the steady-state mismatch ratio scales as:
- Model D (deterministic): $(\mathcal{T}_A/\mathcal{T}_B)^2$
- Model S (stochastic): $(\mathcal{T}_A/\mathcal{T}_B)^{3/2}$

The squared law for deterministic coupling is a notable result — it means a 2:1 tempo advantage produces a 4:1 mismatch disadvantage for the opponent. The stochastic case is $3/2$ power — still superlinear but less so.

## $\rho$ naming: "environment change rate" vs "mismatch injection rate"

The segment uses "environment change rate" for $\rho$. The card (row 99) proposes "mismatch injection rate" as an alternative. Let me compare:
- "Environment change rate": names the source of the disturbance (environment changes)
- "Mismatch injection rate": names what the disturbance *does* (injects mismatch)
- "Effective disturbance $\rho$": connects the formal symbol to its primary interpretation

"Mismatch injection rate" is more precise from the model's perspective: $\rho$ is the rate at which new mismatch is introduced, regardless of whether that's from actual environment change or from noise or from adversarial action. "Environment change rate" is too narrow if $\rho$ also captures stochastic noise and adversarial disturbance.

"Effective disturbance" is the cleanest and most general — it covers all sources of mismatch injection without committing to one mechanism.

## Cross-segment notes

The segment depends on `#deriv-sector-condition` which hasn't appeared in the OUTLINE walk yet. This seems to be an appendix derivation — the appendix-back-pointer exception applies. But the `depends:` frontmatter lists it, and I haven't read it yet in OUTLINE order. This might be a dependency ordering issue (an appendix segment being listed as a formal dependency rather than just cited in Discussion). Worth flagging.

## Wandering thoughts

The ODE framing is pedagogically valuable even if it's heuristic. The intuition — mismatch decays at rate $\mathcal{T}|\delta|$ while disturbance adds at rate $\rho$ — is easy to visualize and reason with. The sector-condition result later gives the nonlinear version without the clean analytic expressions. The ODE provides the "first-order intuition" layer.

The bridging assumption (fluid-limit from discrete to continuous) is explicit: for Model D the steady states are identical; for Model S there's an $O(\eta^* c_{\max})$ variance gap. This kind of explicit bridge between formulations is good epistemic practice — it shows exactly where the continuous approximation breaks down.

The citation of Boyd throughout this segment (Orient quality vs OODA speed) is appropriate but I'm noticing it's starting to feel like a recurring refrain. The Boyd connection is real and well-chosen, but the segment could over-rely on it as external validation. The AAD claim stands on its own mathematical grounds; the Boyd connection is illustration, not proof.

How valuable: 7/10 for surprise (the deterministic vs stochastic scaling difference is significant), 8/10 for load-bearing.
