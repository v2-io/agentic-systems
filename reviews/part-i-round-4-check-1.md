---
kind: review
author:
  name: Claude Opus 5.5 (Part I round-4 checker)
  role: independent verifier
sources:
  - msc/inside-out-2026-10/c1-lanes/part-i-check-4.md
written: 2026-10-30
---

# Part I round 4 (the round-3 check integrated; the threshold expansion to three terms; the posture Brief's escape claims): the independent check

KR C.1 ("Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier") and C.2 ("Strengthenings C1–C3 … are independently checked, then landed or refuted"), item C1, with MAP D9. Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." This checks the landing merged at 387e71c0 (22015b33..40e772d6), read at 3d17de13. No file read here changed between 40e772d6 and 3d17de13 except an unrelated NOTATION row. Every number was recomputed by my own code, not the integrator's script; my script is in the source. The three-term expansion (C.2) is confirmed at the tier canon gives it. The findings are claims the round corrected that still stand elsewhere, one on a public surface (F1); a gain-buys-time sentence the round's sweep missed (F2); and residues in the posture segment.

## C1 (check)
- target: segment:deriv-sector-condition
- at: 3d17de13
- act: rederive
- line: derivation
- read: segment:deriv-sector-condition
- criterion: $\alpha\Phi(0)|_{\kappa_R=n/2} = \tfrac14(\ln n + \gamma_{\mathrm E}) + \sqrt\pi/(3\sqrt n) - 2/(9n) + O(n^{-3/2})$ follows from the four steps as written: the tail bound beyond $m^{3/5}$, the uniform expansion with every error monomial $k^p/m^q$ having $p/2 - q \leq -\tfrac32$, the Mellin shift to $\operatorname{Re}s = -\tfrac32$ with Poisson and Euler–Maclaurin, and the assembly; and the tier "remainder $O(n^{-3/2})$, bounded step by step" is honest.
- committed: before
- outcome: confirmed
- recheck: By hand, from the power sums: $-L_k = -\tfrac{k^2}{2m} + \tfrac{k}{2m} + \tfrac{k^3}{6m^2} - \tfrac{k^2}{4m^2} - \tfrac{k^4}{12m^3} + O(\tfrac{k}{m^2} + \tfrac{k^3}{m^3} + \tfrac{k^5}{m^4})$. On $k \leq m^{3/5}$, $k^3/m^2 \leq m^{-1/5}$ and $k^4/m^3 \leq m^{-3/5}$. Error monomials $(p,q)$ from $r$'s $O$, $\lvert g\rvert^3$, $\lvert gr\rvert$ and $r^2$: $(1,2), (3,3), (5,4), (7,5), (9,6), (4,4), (6,5), (8,6)$. All have $p \geq 1$ and $p/2 - q \leq -\tfrac32$. $\tfrac12g^2 + r = -\tfrac{k^2}{8m^2} + \tfrac{k^6}{72m^4}$, and $\int k^5e^{-\varepsilon k^2} = 8m^3$ gives $-\tfrac1{8m} + \tfrac1{9m} = -\tfrac1{72m}$. The residues are $-\tfrac12\ln\varepsilon + \tfrac12\gamma_{\mathrm E}$ at $0$ and $-\zeta(-1)\varepsilon = \varepsilon/12$ at $-1$, and no pole lies on $\operatorname{Re}s = -\tfrac32$. Assembly: $\tfrac1{24} - \tfrac14 - \tfrac1{72} = -\tfrac29$ per $m$, halved. The tier: each step's error is proved to be $O(m^{-3/2})$, with constants that exist but are not written out. That is the meaning of a derived asymptotic, and canon uses the integral or the series for rigorous statements.

## C2 (check)
- target: segment:deriv-sector-condition
- at: 3d17de13
- act: run
- line: derivation
- read: segment:deriv-sector-condition
- criterion: The numbers the round wrote or kept: threshold values $0.60 \ldots 1.89$; three terms $1.889704$ against exact $1.889709$ at $n = 1000$, and $0.885$ against $0.889$ at $n = 10$; residual times $n^{3/2}$ $0.125, 0.142, 0.148, 0.150, 0.151, 0.151$ at $n = 10 \ldots 10^6$; margin values $0.71, 1.57, 3.12, 12.0, 51.2$ at $n = 3$; doubling increments $1.01, 0.955, 7.5, 1.9, 1.20$.
- committed: before
- outcome: confirmed
- recheck: Own log-space series against an independent quadrature of $\int_0^1 t^{n-1}(e^{\kappa(1-t^2)}-1)/(1-t^2)\,dt$, 40 digits, agreeing to 10 digits: $0.5957, 0.6590, 0.7064, 0.7767, 0.8885, 1.0157, 1.2018, 1.3526, 1.8897085$; three terms $1.8897038$, $0.88456$; residual $\times n^{3/2}$ $0.1249, 0.1422, 0.1482, 0.1501, 0.1507, 0.1509$; margins $0.7064, 1.574, 3.124, 11.98, 51.24$; increments by `findroot` $1.012, 0.9548, 7.521, 1.945, 1.197$.

## C3 (check)
- target: segment:deriv-sector-condition
- at: 3d17de13
- act: read-check
- line: imported
- read: segment:deriv-sector-condition
- criterion: Grebenkov 2015 eqs. (75)–(76) are the Lemma's integral and its small-noise form, and state no series; Graczyk & Jakubowski 2008 is correctly marked as not read.
- committed: before
- outcome: confirmed
- recheck: arXiv:1411.3598 as served on 2026-10-30. (75) is $\tfrac{2}{\sigma_w^2}\int G/m$ under $D = \sigma_w^2/2$, $L = R$. (76) with $L^2/D = 2\kappa/\alpha$ is $\Gamma(n/2)e^{\kappa_R}/(2\alpha\kappa_R^{n/2})$. G&J was not reached (no HAL file). Guillaume, arXiv:2609.21685, surveys OU exit from a ball and does not quote G&J.

## C4 (check)
- target: segment:result-sector-condition-stability
- at: 3d17de13
- act: read-check
- line: derivation
- read: segment:result-sector-condition-stability, segment:deriv-sector-condition
- criterion: :61 says only what Prop A.1S-τ's cap paragraph supports: exponent capped at $K$, stay peaking below $K$ and falling past it, the reachable stay bounded, raised only by information, region or a slower world.
- committed: before
- outcome: confirmed
- recheck: Read against the cap paragraph of `#deriv-sector-condition` (the maximizer $0.31K$–$0.89K$, derivative $-\Phi(0)/K$ at $K$, the "What raises the cap" sentence).

## C5 (check)
- target: segment:result-persistence-condition
- at: 3d17de13
- act: read-check
- line: derivation
- read: segment:result-persistence-condition, segment:deriv-sector-condition
- criterion: INTRODUCTION headline 1 states the guarantee per disturbance model as `#result-persistence-condition`'s Brief does, and its "simplest correctors … driven out by a worst-case disturbance" is Lemma A.1N's class-level reading.
- committed: before
- outcome: confirmed
- recheck: Headline 1 (`01-aat-core/INTRODUCTION.md` :26) against the Brief (:156) and Lemma A.1N. Remark: the Brief also says that on a noisy channel the random-change condition is a window of gains, while the headline says "below which". With $\rho$ read as total disturbance (NOTATION's new gloss), the inequality contains the window.

## C6 (check)
- target: segment:disc-constructive-impossibility-posture
- at: 3d17de13
- act: read-check
- line: derivation
- read: segment:disc-constructive-impossibility-posture, segment:der-causal-insufficiency-detection, segment:deriv-edge-credence-dynamics, segment:disc-identifiability-floor, segment:deriv-critical-mass-composition, segment:deriv-sector-condition, segment:deriv-stochastic-non-exit, segment:deriv-evidence-allocation-ceiling
- criterion: The Findings Brief's escape statements for Instances B, C, D and E, and Instance A's five-route count, match their source derivations.
- committed: before
- outcome: confirmed
- recheck: B: repair routes (i)–(iii) of `#deriv-edge-credence-dynamics` §"Refuted Under Unobservable $C$". C: `#disc-identifiability-floor` Instance 3, escapes (a)–(e). D: Cor A.1S.1. E: `#deriv-evidence-allocation-ceiling` :70, :74 (fixed allocation, class $\mathcal C$, the open extensions). A: `#der-causal-insufficiency-detection` :19, :55–67. Instance A's description of the other routes is F3.

## C7 (check)
- target: segment:disc-constructive-impossibility-posture
- at: 3d17de13
- act: read-check
- line: derivation
- read: segment:disc-constructive-impossibility-posture, segment:deriv-self-actuation-grounding, segment:deriv-reward-channel-learning-no-go
- criterion: The segment tables seven instances and counts seven; F is `conditional` on three named premises and G on (R1)–(R5).
- committed: before
- outcome: confirmed
- recheck: Frontmatter `status: conditional` in both; `#deriv-self-actuation-grounding` :88 "three explicitly-named local premises"; `#deriv-reward-channel-learning-no-go` :55 "Conditional on (R1)–(R5)".

## C8 (check)
- target: segment:disc-constructive-impossibility-posture
- at: 3d17de13
- act: run
- line: derivation
- read: segment:disc-constructive-impossibility-posture
- criterion: The five added `depends:` entries and the one `OUTLINE-accepted.md` row leave `lint-outline` clean, and the accepted row is the only body-before-dependency case they create.
- committed: before
- outcome: confirmed
- recheck: `bin/lint-outline`: 0 ordering violations, 17 accepted; the other four new dependencies are Appendix (backmatter) segments, listed under "references proof in".

## F1 (finding)
- target: item:findings-brief-overclaim-on-public-surfaces-map
- at: 3d17de13

The item, "on public surfaces", was closed while `01-aat-core/OUTLINE.md` :332 (the Appendices' Layer 0, written in 5e621256 before the round) still makes each corrected claim in "impossible without" form. Detection "is impossible without loop-interventional access"; the mixture "is impossible without observing the latent"; composite contraction "is impossible without matched-tier shared metrics"; for $K$ alternatives "no update rule or forgetting rate keeps them calibrated", with "whatever the update rule" in the opening sentence. It also says "Five cleanly-fitting instances" and "names the unique broadly-available capability". :112 still gives the posture's second move as "name the escape (unique broadly-available framework machinery)". `README.md` :46, `README-auditor.md` :67 and their source `doc/readme/src/_position-and-lineage.md` :13 say of the identifiability-floor pattern "the unique escapes interventional machinery supplies", which is false for Instance 2, whose escapes are observability and joint observation. The closure is premature in the item's own terms. Supported form: Layer 0 restates the posture Brief as it now stands; :112 says "name the escapes"; the README line says "the escapes that interventional and observational machinery supply".

## F2 (finding)
- target: segment:deriv-stochastic-non-exit
- at: 3d17de13

:56: "so the certain event can be made as late as a lifetime requires, at a margin cost logarithmic in that lifetime, though not by raising the gain past the Kalman gain on a fixed channel." This is round-3 F1's shape. It implies that gain up to $K$ buys the time, but on a fixed channel the reachable stay is bounded over all gains and falls between its maximizer and $K$ (`#deriv-sector-condition`'s cap paragraph). The integration record's C2 recheck and the round-4 account both say a four-volume sweep found no other such sentence. Supported form: "… not by gain on a fixed channel, where the reachable stay is bounded and peaks below the Kalman gain".

## F3 (finding)
- target: segment:disc-constructive-impossibility-posture
- at: 3d17de13

The Brief, written in this round, says the loop's covariance test "is the one that needs only machinery the theory already requires; the others need domain capabilities." `#der-causal-insufficiency-detection` :156: "Routes (a) and (b) have explicit AAT scaffolding …; routes (c)–(e) depend on domain capability." Route (a), $\varepsilon$-exploration under SA3, needs no domain capability and gives partial detection. Supported form: the covariance test is the strong detector that needs only machinery the theory already requires; exploration alone gives partial detection; the other three need domain capabilities.

## F4 (finding)
- target: segment:disc-constructive-impossibility-posture
- at: 3d17de13

Row C's apparatus cell says (CM2)/(CM2-M) and `#scope-composite-agent` are "elevated to *unique composition-contraction certificate* under matched structure". The source (`#disc-identifiability-floor` Instance 3, consequence 1) says "the unique broadly-available R0-regime certificate under the matched-Tier structural escape (b)". The row's own escape cell lists a passivity certificate and a common contraction metric as other certificates. Dropping "broadly-available" turns the defined sense into "only". Related: `#impl-composition-machinery` :57 gives the label "unique broadly-available escape" to composite interventional access, while the floor segment gives it to (CM2) for the certificate and to composite loop access for the game-structure identifier.

## F5 (finding)
- target: segment:disc-constructive-impossibility-posture
- at: 3d17de13

The E over-claim the Brief dropped survives in two places in the same segment. Move 1: "a sharp supremum, over allocations and update rules". Row E apparatus: "past the ceiling no forgetting rate, exploration rate, or update rule helps". `#deriv-evidence-allocation-ceiling` :80 says "or update rule in $\mathcal C$", and :74 says drift-extrapolating estimators can lag less under constant drift. Supported form: over fixed allocations and averaging estimators; "no forgetting rate, exploration rate or averaging update helps". The source segment's own summaries at :15 and :88 carry the same unscoped phrasing (its Epistemic Status is scoped).

## F6 (finding)
- target: segment:disc-constructive-impossibility-posture
- at: 3d17de13

W-grade residues in the same segment:

- Impact and Related Work say "five independent audit cohort surfaces" and list six audits; the integrated spike says six.
- The Working Note "Dependency rationale" describes `depends:` as the spine plus "the three boundary-or-boundary-dual derivations". It now has eleven entries.
- Move 2's "distributional-and-instantaneous" contradicts row D's "distributional-and-finite-time". Prop A.1S-τ makes the latter the right one.
- The Epistemic Status's "five on data inference (A–E)" counts D, a containment guarantee under noise, as inference.
- The Working Notes use "Instance F" for the sector sub-scope $\alpha/\beta$ guard, a different object from the table's F.

## F7 (finding)
- target: segment:deriv-critical-mass-composition
- at: 3d17de13

:180 "Four structural escapes are named there". `#disc-identifiability-floor` Instance 3 lists five, (a)–(e), since (e), the passive convergence-rate escape, was added. The integrator flagged it and left it for its own line. Confirmed.

## F8 (finding)
- target: segment:disc-additive-coordinate-forcing
- at: 3d17de13

:96 says the identifiability floor names, for each no-go, "the unique escape available". Instance 1 has five routes and Instance 3 five escapes. The same stale restatement appears in:

- `#disc-anti-collapse` :16: the posture "names the unique escape".
- `#disc-identifiability-floor` :36 and `#impl-strategy-dynamics` :26, :42: the posture's move as "name the unique broadly-available escape", the wording the posture itself replaced with "name the escapes".
- `#form-consolidation-dynamics` :157: "consolidation as the unique escape" of a candidate instance, where I found no uniqueness derivation.

When the posture's second move changed, these restatements went stale.
