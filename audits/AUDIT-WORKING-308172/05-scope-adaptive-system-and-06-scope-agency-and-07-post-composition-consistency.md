# 05/06/07 — scope-adaptive-system, scope-agency, post-composition-consistency

Three foundational scope/postulate segments. The pattern is clear: AAD declares a hierarchy of nested scopes, with sharp operational tests at each level.

## scope-adaptive-system

Two conditions: $\mathcal O \neq \emptyset$ and $H(\Omega_t \mid \mathcal C_t) > 0$. Anything that observes under uncertainty.

Voted +2 keep on the slug. The pilot's canonical illustration of subject-noun-first naming. Names what's in scope by what the scope delineates.

## scope-agency

Adds two conditions to scope-adaptive-system: $|\mathcal{A}| \geq 2$ AND $\exists\, a \neq a'$ with $P(o \mid do(a)) \neq P(o \mid do(a'))$.

The Pearl-L2-contrast operational definition is sharp. Voted +2 keep.

## post-composition-consistency

The structural postulate: AAD's predictions must be compatible across levels of description. The segment carries an enormous amount of derived material — Tier 1/2/3, contraction-rate closed forms, composite contraction template instantiations, etc.

Voted +2 keep on `composition consistency`. Strong rejection (-1 each) of holon, scale-invariance, scale-invariance-of-adaptive-dynamics, cross-level-coherence — they over-claim, under-claim, or import baggage.

## Reflections

**#2 cross-segment consistency.** The composition postulate is a structural-coherence requirement, not a derived theorem. Section III then *derives* the operational consequences (Tier 1M closed-form composite rate, Tier 2 with degradation, Tier 3 per-domain). This separation of axiomatic-meta-claim from derived-operational-content is exactly the kind of move I'd want to see — the framework names what is forced by structural coherence vs what falls out as theorem under that coherence.

**#5 Errors to watch for.** Future segments may invoke "composition" without specifying the tier. The segment is meticulous about this — Tier 1M (exact closed form), Tier 2 (degraded), Tier 3 (per-domain). If a downstream segment writes "by composition consistency, X" without naming the tier, that's drift. Watch.

**#13 Field contribution.** The framework's response to the holon question — "we treat composition as a structural-coherence postulate, derive what follows, and acknowledge tier-dependent transfer" — is sharper than most multi-scale-systems literature. Most "holon" / "scale-free" / "fractal" framings claim more (full self-similarity); AAD claims less and proves more. If this becomes legible to systems-theory readers, the methodological move alone is publishable.

**#14 Wandering.**

The Tier 1/2/3 framing is doing a lot of unspoken work in the corpus. It looks like a generic disclaimer ("results may not lift exactly") but it actually corresponds to specific algebraic conditions: Tier 1M is exponential-family Bayesian on convex losses with positive-definite gain — basically Kalman, gradient descent on quadratic loss, exact-Bayes. Tier 2 is local convexity with degraded factors. Tier 3 is everything else.

The Working Notes call out the strengthening attempt and its outcome: "macro-timescale bounded below by slowest sub-agent" got tied to (CC-parallel) closed-form $\lambda_c = \min_i \lambda_i$ via the contraction-template results. This is exactly the strengthen-before-soften discipline the project's CLAUDE.md describes. The fallback (heuristic for Tier 2/3) is preserved as the residual that the strengthening genuinely couldn't eliminate. Good.

The Brooks's Law gloss is interesting: $\varepsilon^\ast \nu_c$ rising in $\rho_{\text{eff}}$ as people are added stretches $\tau_{\text{eq}}$ while $\rho_{\text{ext}}$ and $\tau_{\text{ext}}$ stay fixed (the deadline doesn't move). The persistence inequality flips. This is the kind of formal substrate that lets a software-engineering folk-theorem be derived rather than asserted, which is the whole point of TST as the "calibration laboratory."
