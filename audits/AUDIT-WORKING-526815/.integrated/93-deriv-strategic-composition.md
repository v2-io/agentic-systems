# 93 - deriv-strategic-composition

Source: `01-aat-core/src/deriv-strategic-composition.md`

## First-pass understanding

This segment moves partially-opposing composites from contraction-to-shared-state into game/equilibrium language. The split is useful: potential/monotone games get point-equilibrium convergence and may inherit a sector-style constant; general games get weaker distributional convergence to CCE under no-regret learning. The Cournot worked example is the strongest local check because it actually supplies a quadratic potential with an interior equilibrium and a concrete joint curvature.

The overreach is in the general transfer language. A potential function is not enough by itself to give a sector inequality, unique convergence, or a basin around a chosen equilibrium. The sector-template transfer needs additional curvature/PL/strong-monotonicity and dynamic assumptions. Likewise, the VI and no-regret claims are standard but need their usual assumptions stated before being used as AAT scope guarantees.

## Diagram attempt

I drew the strategic-composition scope as a fork. Alpha-prime goes to potential/monotone games, but only the curved/strong cases feed a sector-style equilibrium persistence test. Beta-prime goes to CCE distributions, explicitly bypassing the sector template. A side warning marks the still-open bridge back to composition closure.

## Findings and watches

- F234 candidate: potential-game structure alone does not imply the displayed sector inequality `dPhi/dt >= alpha_joint ||grad Phi||^2` or convergence to a selected equilibrium. That needs a dynamic aligned with the potential plus curvature/gradient-domination or local strong stability assumptions.
- F235 candidate: "equilibrium stability follows from Phi's role as a joint Lyapunov function" is too broad. Increasing a potential can converge to local maxima, stationary saddles, boundary equilibria, or multiple equilibria depending on geometry and dynamics.
- F236 candidate: the sector-template transfer first sets `xi = gradient-of-potential` and then `xi = pi - pi*`. Those are different state variables unless a local Hessian/strong-convexity relation maps them.
- F237 candidate: VI existence is overstated as pure-strategy Nash existence for continuous compact-convex games with continuous payoffs. A VI solution corresponds to Nash under additional differentiability/concavity-in-own-strategy assumptions; continuity alone is not enough.
- F238 soft candidate: no-regret convergence to CCE needs finite or otherwise compact action sets, bounded losses/payoffs, and the right information/update protocol. State those assumptions before using the `O(1/sqrt T)` macro-state guarantee.
- F239 candidate: `deriv-strategic-composition` uses B1 directional fidelity and `der-gain-sector-bridge` in the alpha-prime proof but does not declare `der-gain-sector-bridge` as a dependency.
- F240 soft candidate: "contraction to shared truth is the `U_O = 1` special case" is conceptually useful but too simple. Shared objectives do not by themselves imply a unique shared truth, contraction, or closure-defect zero without the earlier composition and observability conditions.
- F241 candidate: the proposed C-iv scope route changes `scope-composite-agent` but is introduced here as a formulation choice. It should be routed back to the scope segment or clearly marked as proposed extension until incorporated.
- F242 candidate: the Class-1 sub-agents to Class-2 composite result depends on cross-checking `hyp-directed-separation-under-composition`, which is not declared as a dependency here and is explicitly listed as follow-up.
- F243 soft candidate: mechanism-design impossibility and active-inference claims are positioned as adjacent implications, but some prose ("fails here in a derivable way") outruns what this segment derives locally.
- F244 watch: the Cournot instantiation appears locally coherent and usefully separates the conceptual zero-sum corner example from the actual sector-template example.
- F245 watch: the bridge from strategic composition back to `form-composition-closure` remains open because the macro-description is an equilibrium statistic/distribution rather than a state trajectory.

## Local verdict

The alpha-prime/beta-prime split is a good architecture. The exact-transfer claim should be narrowed to games with enough curvature/monotonicity for a sector inequality, while general potential games and no-regret regimes remain weaker equilibrium-framing results.

