---
kind: review
author:
  name: Claude Opus 5.5 (C.1 verifier, A7/A10 lane)
  role: independent verifier
sources:
  - msc/inside-out-2026-10/c1-lanes/part-i-check.md
  - msc/inside-out-2026-10/c1-lanes/part-i-mismatch-lineage.md
written: 2026-10-30
---

# Part I mismatch objects and persistence lineage (A7, A10): the independent check

KR C.1 ("Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier"); top intent: "Complete 'in-place' refactor of ASF-- meta, all artifacts, and theory itself." This checks the landing in 481943e4, 67141a67 and fe120d60, re-derived from the text as written. The Part I segments and def-death-as-factor-loss are byte-identical between fe120d60 and 924e70f9; scope-evolving-software changed under the TST lane in between and was read at 924e70f9. The derivations, the window script and the reasoning are in the first source above.

## C1 (check)
- target: segment:deriv-sector-condition
- at: 924e70f9
- act: rederive
- line: derivation
- criterion: The state of the persistence dynamics is the estimation error, its disturbance under linear correction is $\sigma_{\text{env}}\,dW - \alpha\sigma_\nu\,dV$, and the Model S steady state is $n(\sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2)/(2\alpha)$, minimized at $\sigma_{\text{env}}/\sigma_\nu$ with value $n\sigma_{\text{env}}\sigma_\nu$.
- committed: before
- outcome: confirmed
- recheck: Kalman–Bucy error SDE derived by hand; exact-discretization simulation (2,000 paths, $\sigma_{\text{env}} = 1$, $\sigma_\nu = 0.5$) gives $0.6248, 0.5006, 0.6265, 1.0613$ against $0.625, 0.500, 0.625, 1.0625$ at $\alpha = 1, 2, 4, 8$; `window.py` in the first source.

Independent of the integrator's Euler run. The Model D bound $\rho_{\text{env}}/\alpha + \bar\nu$ is also confirmed, and tight (constant disturbances attain it).

## C2 (check)
- target: segment:result-persistence-condition
- at: 924e70f9
- act: rederive
- line: derivation
- criterion: "Two levers in $\mathcal T$": past the optimal gain, faster correction on the same observations enlarges the error, and the same split appears under Model D.
- committed: before
- outcome: narrowed
- recheck: Model S closed form (C1); Model D bound $\rho_{\text{env}}/\alpha + \bar\nu$ is decreasing in $\alpha$.

True under Model S with white channel noise. False under Model D, where raising the gain lowers the bound monotonically toward $\bar\nu$ and more events do not lower a worst-case $\bar\nu$. See F2.

## C3 (check)
- target: segment:deriv-persistence-cost
- at: 924e70f9
- act: rederive
- line: derivation
- criterion: The scalar Gauss–Markov sequential RDF has continuous-time limit $\sigma^2/(2D) - \lambda$; Kalman–Bucy's Duncan rate $P/(2\sigma_o^2)$ equals it at $D = P$ for every $\lambda$; the non-causal OU value at high resolution is $2\sigma^2/(\pi^2 D)$.
- committed: before
- outcome: confirmed
- recheck: Expansion and Riccati identity by hand; reverse water-filling in closed form on $S(f) = \sigma^2/(2\pi f)^2$ ($R = 2f_c$, $D = \sigma^2/(\pi^2 f_c)$); the integrator's `srdf_kb_check.py` and `rdf_check.py` re-run and reproduce.

## C4 (check)
- target: segment:deriv-persistence-cost
- at: 924e70f9
- act: read
- line: imported
- criterion: Tanaka, Kim, Parrilo & Mitter 2017 eq. (28) is $\max\{0, \tfrac12\log(a^2 + w/D)\}$ for the scalar Gauss–Markov source.
- committed: before
- outcome: confirmed
- recheck: arXiv 1411.7632 PDF, eq. (28) and the paragraph deriving it from (29); the extracted text prints min, and the derivation's case split shows it is max.

## C5 (check)
- target: segment:deriv-persistence-cost
- at: 924e70f9
- act: rederive
- line: derivation
- criterion: For a gain other than $K$, the price of persistence follows from the error that gain achieves.
- committed: before
- outcome: narrowed
- recheck: A linear filter $d\hat x = -(\lambda + \alpha)\hat x\,dt + \alpha\,dy$ is invertible in its observation path, so $I(x;\hat x) = I(x;y) = K/2$ per component for every $\alpha \gt 0$ (Duncan).

The error sets the floor, which is slack for every $\alpha \neq K$; the intake itself is fixed by the channel. See F7.

## C6 (check)
- target: segment:result-persistence-condition
- at: 924e70f9
- act: read
- line: imported
- criterion: Widrow, McCool, Larimore & Johnson 1976 state that weight noise grows with the speed of adaptation, lag falls with it, and their sum is minimized where the two are equal.
- committed: before
- outcome: confirmed
- recheck: Abstract, p. 1151, in relata's stored PDF for widrow-1976-stationary.

## C7 (check)
- target: segment:example-kalman
- at: 924e70f9
- act: rederive
- line: derivation
- criterion: $P^- = 0.640$, $K_{ss} = 0.390$, $P = 0.390$, innovation RMS $1.28$; $V(K) = (q + K^2 r)/(1 - (1-K)^2)$ gives $0.982, 0.640, 0.940$ at $K = 0.15, 0.39, 0.81$; $P(\lvert e^-\rvert \gt 1.4) = 0.080$.
- committed: before
- outcome: confirmed
- recheck: Riccati and the fixed-gain recursion $e^-_{t+1} = (1-K)e^-_t - Kn_t + v_t$ by hand; the integrator's `example_kalman_numbers.py` re-run (Monte Carlo $0.982, 0.639, 0.941$).

## C8 (check)
- target: segment:result-mismatch-decomposition
- at: 924e70f9
- act: rederive
- line: derivation
- criterion: $\mathbb E\lVert\bar o_t - \hat o_t\rVert^2 = \text{(i)} + \text{(ii)}$, so the persistence bounds sit on (i)+(ii) and the innovation's mean square exceeds them by (iii).
- committed: before
- outcome: confirmed
- recheck: Insert $\hat o^{\mathrm B}_t$; the cross term vanishes on conditioning on $(\mathcal C_{t-1}, a_{t-1})$ by step 2 of the segment.

The identity holds; the naming around it is F4.

## C9 (check)
- target: segment:deriv-gain-sector
- at: 924e70f9
- act: rederive
- line: derivation
- criterion: B.1: $e^+ = (1-K)e^- - K\varepsilon$, the injected term has variance $K^2 R_{\text{obs}}$, and B.3's noise-averaged correction is exact for linear $g$.
- committed: before
- outcome: confirmed
- recheck: Direct substitution of $\delta = He + \varepsilon$ in the Kalman update.

For nonlinear $g$ see F11.

## C10 (check)
- target: segment:impl-strategy-dynamics
- at: 924e70f9
- act: rederive
- line: derivation
- criterion: A less efficient linear corrector holding the same target needs a more informative channel than the floor requires.
- committed: before
- outcome: confirmed
- recheck: Holding $D$ at gain $\alpha \neq K$ ($\lambda = 0$) needs $\sigma_o'^2 = (2\alpha D - \sigma^2)/\alpha^2$, which is below $(D/\sigma)^2$, the noise at which Kalman–Bucy holds $D$.

## C11 (check)
- target: segment:hyp-mismatch-dynamics
- at: 924e70f9
- act: read
- line: derivation
- criterion: The segment reads $\rho$ consistently as the total disturbance its bullet defines.
- committed: before
- outcome: broken
- recheck: Bullet defines $\rho$ as environment plus fed-back noise; the next paragraph calls the steady states "the lag term at fixed $\rho$"; the summary paragraph and the Model D gloss read $\rho$ as environmental change.

See F3.

## F1 (finding)
- target: segment:result-persistence-condition
- at: 924e70f9

A strengthening the landing implies but does not state. With $\sigma_w^2 = \sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2$ (linear correction, Model S, white channel noise), $\alpha \gt n\sigma_w^2/(2R^2)$ holds iff $\alpha \in (\alpha_-, \alpha_+)$, $\alpha_\pm = (R^2 \pm \sqrt{R^4 - n^2\sigma_{\text{env}}^2\sigma_\nu^2})/(n\sigma_\nu^2)$. Some gain persists iff $R^2 \gt n\sigma_{\text{env}}\sigma_\nu$ (the Kalman–Bucy error fits); the window is geometric about the Kalman gain, $\alpha_-\alpha_+ = K^2$, with $\ln(\alpha_+/K) = \operatorname{arccosh}(R^2/(n\sigma_{\text{env}}\sigma_\nu))$. Task adequacy takes the same form with $\lVert\delta_{\text{critical}}\rVert$. Under Model D, $\alpha(R - \bar\nu) \gt \rho_{\text{env}}$: a new necessary condition $R \gt \bar\nu$, reserve $\alpha(R - \bar\nu) - \rho_{\text{env}}$, and the linear operational form becomes $\mathcal T \gt \rho_{\text{env}}/(\lVert\delta_{\text{critical}}\rVert - \bar\nu)$. Checked on a grid (`window.py`). Belongs in this segment and in #deriv-sector-condition's Setup; #result-sector-condition-stability and the adversarial results inherit it.

## F2 (finding)
- target: segment:result-persistence-condition
- at: 924e70f9

The lag/noise optimum is a Model S (white-noise) fact. The opening's task-adequacy paragraph says without qualifier that raising the gain on the same observations "is not a remedy past the optimal gain", and "Two levers" says "Under Model D the same split appears". Under Model D the tight bound $\rho_{\text{env}}/\alpha + \bar\nu$ falls monotonically in $\alpha$, and event rate does not lower a worst-case $\bar\nu$; the levers behave differently there, and that difference should be stated.

## F3 (finding)
- target: segment:result-persistence-condition
- at: 924e70f9

$\rho$ and $\sigma_w$ carry two readings across the family. #deriv-sector-condition's Setup and this segment's Formal Expression make them total and the propositions exact; this segment's "Two levers" says the forms elsewhere hold "with $\sigma_w$ environmental" and are "the lag terms alone"; its cost paragraph and #deriv-persistence-cost use $\sigma_w$ as the signal's own diffusion; #hyp-mismatch-dynamics defines $\rho$ as total, calls its steady states "the lag term at fixed $\rho$", and its summary and Model D gloss read $\rho$ as environmental. $R^\ast = \rho/\alpha$ cannot be both the exact bound and the lag term; one reading per symbol, with $\sigma_{\text{env}}$ or $\sigma_s$ for the cost segment's signal diffusion.

## F4 (finding)
- target: segment:result-mismatch-decomposition
- at: 924e70f9

Term (i) is labelled "estimation error" (underbrace), "estimation term" (opening) and "positive estimation error (term i)" (Discussion), while the new paragraph and #def-mismatch-signal define estimation error as (i)+(ii). Rename (i) (e.g. excess over the Bayes predictor) or say which is meant.

## F5 (finding)
- target: segment:def-mismatch-signal
- at: 924e70f9

"That is the quantity a correction can drive toward zero": the estimation error carries term (ii), the state-and-law floor, which binds every chronica-measurable predictor; a correction drives it toward that floor, not zero. And "'Mismatch' without qualification is used only where a statement holds for either object" is false of canon as written (#result-persistence-condition: "Mismatch is ultimately bounded by $R^\ast$"). State it as the convention adopted, or bring usage to it.

## F6 (finding)
- target: segment:result-persistence-condition
- at: 924e70f9

Two items in "Two levers in $\mathcal T$". $\mathcal T = \nu\eta^\ast$ uses the optimal gain, so a gain past the optimum moves $\alpha$, not $\mathcal T$, except through a mis-estimated $U_M$ or $U_o$; the title and "tempo raised by gain alone past the optimum" need that said. The Epistemic Status ground "the direction holds whenever the mismatch transform is Lipschitz, since the injected noise then grows with the gain" is the wrong ground: Lipschitz bounds injected noise from above and cannot show the error grows; for fixed $g$ the fluctuation scales with the gain for any $g$.

## F7 (finding)
- target: segment:deriv-persistence-cost
- at: 924e70f9

Every linear filter on the fixed channel takes in $nK/2$ (C5), so "the price follows from the error that gain achieves" names the floor at that error, not what is paid; a mis-tuned corrector pays $nK/2$ for a worse error. With $\lambda_s \gt 0$ the error's contraction rate is $\lambda_s + K$, yet $K$ is called "the sector constant of its correction" and the Setup's "linear corrector at sector rate $\alpha$" contracts at $\lambda_s + \alpha$; fix the convention. "A corrector below the optimal gain needs more than $n\alpha/2$ … one above it achieves a worse error" reads as if only gains above $K$ do worse.

## F8 (finding)
- target: segment:def-death-as-factor-loss
- at: 924e70f9

Line 39 states the floor as "$\dot R \geq n\alpha/2$" and the defense as "$C_{\text{channel}} \geq n\alpha/2$", missed by fe120d60's drain. Same residue in #impl-persistence-and-limits line 131 ("burn-rate ($\dot R \geq n\alpha/2$)").

## F9 (finding)
- target: segment:impl-persistence-and-limits
- at: 924e70f9

Line 39, "The environment does not cancel out of it", answers the deleted audit-gold bullet; that history belongs in CHANGELOG. The positive claim that follows stands alone.

## F10 (finding)
- target: segment:obs-gated-tempo-advantage
- at: 924e70f9

Same mechanism as the new #deriv-sector-condition Setup paragraph, uncited in both directions. Its Epistemic Status says "Max attainable: derived (… Riccati analysis of noisy AR(1) processes)"; the single-agent mechanism is now derived there (the adversarial exponent table is not). #result-persistence-condition's "Two levers" should credit it as the in-canon anticipation.

## F11 (finding)
- target: segment:deriv-gain-sector
- at: 924e70f9

B.3 sends the gain-injected fluctuation into the disturbance. For nonlinear $g$ its covariance depends on $\bar\delta$, while #deriv-sector-condition's A.1S is stated for additive $\sigma_w\,dW$. The stopped bound holds with $n\sigma_w^2$ replaced by the supremum of the diffusion's trace over $\mathcal B_R$; say so.

## F12 (finding)
- target: segment:der-deliberation-cost
- at: 924e70f9

The net benefit $\Delta\eta^\ast\cdot\lVert\delta_{\text{post}}\rVert - \rho_{\text{delib}}\Delta\tau$ prices any gain increase as reduction, which the lag/noise trade-off makes false past the optimum, and multiplies an observed (innovation) magnitude to get a change in estimation error. The integrator listed it as untraced; it is a defect.

## F13 (finding)
- target: segment:scope-evolving-software
- at: 924e70f9

Line 37 reads $\rho$ as "environment change rate" and concludes from #result-persistence-condition that as $\rho \to 0$ "any nonzero tempo suffices". With a noisy channel the floor $\bar\nu$ (Model D) or $n\sigma_\nu^2\alpha/2$ (Model S) remains, so it suffices only when that floor is inside tolerance.

## F14 (finding)
- target: segment:example-kalman
- at: 924e70f9

The Mapping table still reads "Sector parameter ($\alpha = \mathcal T$)", and the Lyapunov section quotes $\alpha = \mathcal T = 3.315\ \text{s}^{-1}$ (the transient-gain mix) beside the steady-state $K_{ss} = 0.390$, whose rate at $\nu = 5$ is $\nu K_{ss} = 1.95$ ($-\nu\ln(1 - K_{ss}) = 2.47$ as an exact per-step contraction rate). Named in the integrator's account, not filed until now.
