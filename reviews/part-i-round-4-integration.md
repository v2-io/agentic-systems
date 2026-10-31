---
kind: review
author:
  name: Claude Opus 5.5 (Part I round-4 integrator)
  role: integrator
sources:
  - msc/inside-out-2026-10/c1-lanes/part-i-round-4.md
  - msc/inside-out-2026-10/c1-lanes/part-i-check-3.md
written: 2026-10-30
---

# Part I round 4 (the round-3 check integrated; the threshold expansion to three terms; the posture Brief's escape claims): the integrator's re-derivations

KR C.1 ("Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier") and C.2 ("Strengthenings C1–C3 … are independently checked, then landed or refuted"), item C1, with MAP D9. Top intent: "Complete 'in-place' refactor of ASF-- meta, all artifacts, and theory itself." These are the checks this integrator ran before landing 49c7a263, 112f25c4, adf92eb8 and 53ec1963 (pre-rebase hashes), each by its own derivation, run or reading. The script is in the first source. The KR asks for an independent verifier after this.

## C1 (check)
- target: segment:deriv-sector-condition
- at: 53ec1963
- act: rederive
- line: derivation
- criterion: $\alpha\Phi(0)|_{\kappa_R = n/2} = \tfrac14(\ln n + \gamma_{\mathrm E}) + \sqrt\pi/(3\sqrt n) - 2/(9n) + O(n^{-3/2})$, by a tail bound beyond $m^{3/5}$, a uniform expansion of the series terms with error monomials $k^p/m^q$, $p/2 - q \leq -\tfrac32$, a Mellin contour shifted to $\operatorname{Re}s = -\tfrac32$ (residues $-\tfrac12\ln\varepsilon + \tfrac12\gamma_{\mathrm E}$ at $0$ and $\varepsilon/12$ at $-1$), Poisson summation and Euler–Maclaurin.
- committed: before
- outcome: confirmed
- recheck: By hand: the second-order sums reduce to $\sum e^{-k^2/(2m)}(-\tfrac{k}{8m^2} + \tfrac{k^5}{72m^4})$ after the $k^4/m^3$ terms cancel, giving $-\tfrac1{72m}$. Assembly gives $\tfrac{1}{24} - \tfrac14 - \tfrac{1}{72} = -\tfrac29$ per $m$, halved to $-\tfrac{2}{9n}$. Numerically, the series by ${}_2F_2$ and by log-space summation agree to $10^{-30}$ for $n \leq 10^4$. The residual after three terms, times $n^{3/2}$, is $0.125, 0.142, 0.148, 0.150, 0.151, 0.151$ at $n = 10 \ldots 10^6$. The Poisson identities hold to working precision at $m = 50, 500, 5000$.

The check (F5) proposed proving the $O(n^{-1})$ remainder. The same ingredients carried one order further give the $-2/9$ coefficient and bound the remainder at $O(n^{-3/2})$.

## C2 (check)
- target: segment:result-sector-condition-stability
- at: 53ec1963
- act: read-check
- line: discussion
- read: segment:result-sector-condition-stability, segment:deriv-sector-condition
- criterion: The "Two kinds of guarantee" paragraph says only what Prop A.1S-τ's cap paragraph supports about gain and time on a fixed channel: exponent capped at $K$, stay maximized below $K$ and decreasing past it, reachable stay bounded.
- committed: before
- outcome: confirmed
- recheck: Read against `#deriv-sector-condition`'s cap paragraph. A grep of all four volumes' bodies and fronts for "Kalman gain" found no other sentence that ties the stay to $K$ rather than to the error.

## C3 (check)
- target: segment:disc-constructive-impossibility-posture
- at: 53ec1963
- act: read-check
- line: discussion
- read: segment:disc-constructive-impossibility-posture, segment:der-causal-insufficiency-detection, segment:impl-causal-access
- criterion: Instance A: on-policy causal-insufficiency detection has five escape routes, (a)–(e), one per scope condition. Route (b), loop-interventional access with a pairwise sibling-covariance test, is the unique broadly-available one in that segment's defined sense; it is not the only escape.
- committed: before
- outcome: confirmed
- recheck: `#der-causal-insufficiency-detection` route table (:55–67) and its "AAT-canonical detector" sentence; `#impl-causal-access` :82 regression guard. The Brief's old "the loop is the only escape" was false.

## C4 (check)
- target: segment:disc-constructive-impossibility-posture
- at: 53ec1963
- act: read-check
- line: discussion
- read: segment:disc-constructive-impossibility-posture, segment:deriv-edge-credence-dynamics
- criterion: Instance B: under unobservable $C$ the per-condition rates become identifiable by observing $C$, or by running $K \geq 2$ children jointly under one $C$-realization; otherwise only the marginal is learnable.
- committed: before
- outcome: confirmed
- recheck: `#deriv-edge-credence-dynamics` §"Refuted Under Unobservable $C$", repair routes (i)–(iii), with (iii) a fallback that loses the decomposition. The Brief's old "observing the latent is the only escape" was false.

## C5 (check)
- target: segment:disc-constructive-impossibility-posture
- at: 53ec1963
- act: read-check
- line: discussion
- read: segment:disc-constructive-impossibility-posture, segment:disc-identifiability-floor, segment:deriv-critical-mass-composition
- criterion: Instance C: composite contraction from component data has five escapes, (a)–(e) of `#disc-identifiability-floor` Instance 3. Matched-tier shared structure, (b), is the one that gives the closed-form certificate.
- committed: before
- outcome: confirmed
- recheck: Instance 3's boundary characterization lists (a)–(e). `#deriv-critical-mass-composition` :180 calls (CM2) the unique broadly-available composition-contraction certificate "among the four escape routes"; it predates (e), the passive convergence-rate escape. The Brief's old "matched-tier shared metrics are the only escape" was false.

## C6 (check)
- target: segment:disc-constructive-impossibility-posture
- at: 53ec1963
- act: read-check
- line: discussion
- read: segment:disc-constructive-impossibility-posture, segment:deriv-sector-condition, segment:deriv-stochastic-non-exit
- criterion: Instance D: under additive non-degenerate stochastic forcing, pathwise-forever containment is unavailable at every correction strength, and the no-go is the result.
- committed: before
- outcome: confirmed
- recheck: Cor A.1S.1 and `#deriv-stochastic-non-exit`; the Brief's claim held and only gained "noise that keeps acting".

## C7 (check)
- target: segment:disc-constructive-impossibility-posture
- at: 53ec1963
- act: read-check
- line: discussion
- read: segment:disc-constructive-impossibility-posture, segment:deriv-evidence-allocation-ceiling
- criterion: Instance E: the ceiling $\rho_\Sigma \lt R_\Sigma/K$ holds under fixed allocation for every estimator in the averaging class $\mathcal C$ (weights set by the observation history, not by outcomes); it is not shown for every learning rule.
- committed: before
- outcome: confirmed
- recheck: EA.1's setup and proof, and Cor EA.2's supremum over allocations and $\mathcal C$. The open `question:ea1-beyond-averaging-estimators` is the unshown part. The Brief's old "whatever its learning rule" over-claimed.

## C8 (check)
- target: segment:disc-constructive-impossibility-posture
- at: 53ec1963
- act: read-check
- line: discussion
- read: segment:disc-constructive-impossibility-posture, segment:deriv-self-actuation-grounding, segment:deriv-reward-channel-learning-no-go
- criterion: Instances F and G are `conditional`, on three named premises and on (R1)–(R5) respectively; the segment tables seven instances.
- committed: before
- outcome: confirmed
- recheck: The two segments' frontmatter and Epistemic Status. The posture segment's Epistemic Status, Discussion and Novelty Claim had counted five.
