*KR C.1: "Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier." Items A7 and A10. Top intent: "Complete 'in-place' refactor of ASF-- meta, all artifacts, and theory itself."*

# Part I mismatch lineage: the independent check

This is the verifier's write-up for the landing in 481943e4, 67141a67 and fe120d60 (account: `part-i-mismatch-lineage.md` beside this file). The typed checks and findings are in `reviews/part-i-mismatch-lineage-check-1.md`, taken into vsect. Every segment cited below is byte-identical between fe120d60 and 924e70f9, the commit the record binds to.

## What holds

The rename is right and the central re-derivation is right. The state of the persistence dynamics is the estimation error $\bar\delta = \bar o - \hat o$, not the innovation. For a linear corrector on a random-walk signal, $d\bar\delta = -\alpha\bar\delta\,dt + \sigma_{\text{env}}\,dW - \alpha\sigma_\nu\,dV$, whose stationary variance is $n(\sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2)/(2\alpha)$, minimized at the Kalman–Bucy gain $\sigma_{\text{env}}/\sigma_\nu$ with value $n\sigma_{\text{env}}\sigma_\nu$. I re-simulated it with an exact (not Euler) discretization and 2,000 paths: $0.6248, 0.5006, 0.6265, 1.0613$ against $0.625, 0.500, 0.625, 1.0625$ at $\alpha = 1, 2, 4, 8$ ($\sigma_{\text{env}} = 1$, $\sigma_\nu = 0.5$). The discrete Kalman step $e^+ = (1-K)e^- - K\varepsilon$ injects variance $K^2 r$. The decomposition identity $\mathbb E\lVert\bar\delta\rVert^2 = \text{(i)} + \text{(ii)}$ holds (cross term vanishes on conditioning on the history).

The persistence-cost rewrite is right as a lower bound. I read Tanaka, Kim, Parrilo & Mitter at the primary (arXiv 1411.7632 PDF): eq. (28) is $R_{\text{SRD}}(D) = \max\{0, \tfrac12\log(a^2 + w/D)\}$ (the extracted text garbles max as min; the derivation just below it, "$\tfrac12\log(a^2 + w/D)$ if $1 - w/D \leq a^2$, while it is 0 if …", fixes it). The expansion to $\sigma^2/(2D) - \lambda$, Duncan's $P/(2\sigma_o^2)$, and the Riccati identity $P/(2\sigma_o^2) = \sigma^2/(2P) - \lambda$ all check by hand. The non-causal value $2\sigma^2/(\pi^2 D)$ checks by closed-form reverse water-filling on $S(f) = \sigma^2/(2\pi f)^2$: cutoff $f_c$ gives $R = 2f_c$ and $D = \sigma^2/(\pi^2 f_c)$. The integrator's scripts reproduce their stated outputs; `srdf_kb_check.py` evaluates the bound at $D = P$, so it checks the limit, not the attainment, and I count my hand derivation as the independent check.

The A10 lineage is right. The Widrow et al. 1976 abstract, read in relata's stored PDF, says the weight noise is "proportional to the speed of adaptation", the lag contribution "inversely proportional to the speed of adaptation", and "the sum of the misadjustments can be minimized by choosing the speed of adaptation to make equal the two contributions". The `#impl-strategy-dynamics` reversal in fe120d60 is also right: holding a target $D$ with gain $\alpha \neq K$ requires a channel noise $\sigma_o'$ with $\sigma_o'^2 = (2\alpha D - \sigma^2)/\alpha^2$, which is below $D/\sigma$, the noise at which Kalman–Bucy holds $D$; the channel must be more informative.

## The main thing still open: A7 changed the shape of the persistence condition, and the segments state only the reading

The landing applied "the disturbance depends on the gain" to how $R^\ast$ and its scalings are read. It did not apply it to the condition. Once $\sigma_w^2 = \sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2$, the mean-square persistence condition $\alpha \gt n\sigma_w^2/(2R^2)$ is a quadratic in $\alpha$:

$$n\sigma_\nu^2\alpha^2 - 2R^2\alpha + n\sigma_{\text{env}}^2 \lt 0 \iff \alpha \in (\alpha_-, \alpha_+), \qquad \alpha_\pm = \frac{R^2 \pm \sqrt{R^4 - n^2\sigma_{\text{env}}^2\sigma_\nu^2}}{n\sigma_\nu^2}$$

Three exact consequences (linear correction, Model S, white channel noise):

1. **Feasibility.** Some gain persists if and only if $R^2 \gt n\sigma_{\text{env}}\sigma_\nu$: the Kalman–Bucy error must fit inside the region. If it does not, no gain persists in mean square, however the agent is tuned.
2. **A window, not a threshold.** Persistence holds for gains in an interval. Too low is the familiar failure; too high is a new one: the agent's own correction injects enough channel noise to leave the region.
3. **The window is geometric about the Kalman gain.** $\alpha_-\alpha_+ = \sigma_{\text{env}}^2/\sigma_\nu^2 = K^2$, and $\ln(\alpha_+/K) = \operatorname{arccosh}\!\big(R^2/(n\sigma_{\text{env}}\sigma_\nu)\big)$. The ratio of the region to the optimal error sets how far, in log-gain, an agent can be mis-tuned and still persist.

Checked on a grid (`window.py` below) at $R^2/(n\sigma_{\text{env}}\sigma_\nu) = 1.2, 2, 6$: the analytic window matches the grid to four places, $\alpha_-\alpha_+ = K^2$, and the log half-width equals the arccosh. At ratios $0.8$ and $1$ there is no window. The same algebra applies to task adequacy with $\lVert\delta_{\text{critical}}\rVert$ in place of $R$.

Under Model D with channel noise bounded by $\bar\nu$, $\alpha R \gt \rho_{\text{env}} + \alpha\bar\nu$ becomes $\alpha(R - \bar\nu) \gt \rho_{\text{env}}$. That needs $R \gt \bar\nu$, a condition no gain can meet otherwise, and then gives a plain lower threshold $\rho_{\text{env}}/(R - \bar\nu)$ with no upper end. The adaptive reserve of Prop A.2 becomes $\alpha(R - \bar\nu) - \rho_{\text{env}}$. The linear operational form "most downstream applications cite", $\mathcal T \gt \rho/\lVert\delta_{\text{critical}}\rVert$, becomes $\mathcal T \gt \rho_{\text{env}}/(\lVert\delta_{\text{critical}}\rVert - \bar\nu)$ and needs $\lVert\delta_{\text{critical}}\rVert \gt \bar\nu$.

This is a strengthening of `#result-persistence-condition` (and of `#deriv-sector-condition`'s Setup paragraph), at the same tier, and is where I think the integrator's lane should go next. It also changes how the adversarial results should be re-derived: pushing an opponent's gain up can push it out of its window from above.

## Model D has no optimum

Under Model D the bound $R^\ast = \rho_{\text{env}}/\alpha + \bar\nu$ is tight (constant $w_{\text{env}} = \rho_{\text{env}}$ and constant $\nu = -\bar\nu$ attain it) and decreasing in $\alpha$. A worst-case bounded noise is tracked to amplitude $\bar\nu$, never amplified, and more events do not lower a worst-case $\bar\nu$. So under Model D the gain lever helps monotonically (toward $\bar\nu$) and the information lever does nothing. The U-shape is a property of broadband (white) channel noise, which a stronger correction passes to the error at variance growing with $\alpha$. `#result-persistence-condition` says "Raising the gain on the same observations is not a remedy past the optimal gain" without a model qualifier (opening, task-adequacy paragraph), and "Under Model D the same split appears" in "Two levers". Both should be Model S statements, with Model D's different picture stated.

## Other findings, in brief

- **One symbol, two readings.** `#deriv-sector-condition` Setup says $\rho$ and $\sigma_w$ are total (environment plus injected noise) and the propositions are exact for them. `#result-persistence-condition` line 31 agrees, but its "Two levers" says the forms elsewhere hold "with $\sigma_w$ environmental" and are "the lag terms alone"; its cost paragraph (line 134) and `#deriv-persistence-cost` use $\sigma_w$ as the signal's own diffusion. `#hyp-mismatch-dynamics` defines $\rho$ as total in its bullet, then says the steady states "describe the lag term at fixed $\rho$", and its summary paragraph and Model D gloss still read $\rho$ as environmental change. Whichever reading is chosen, $R^\ast = \rho/\alpha$ cannot be both the exact bound and the lag term.
- **"Two levers in $\mathcal T$" is two levers in $\alpha$.** $\mathcal T = \nu\eta^\ast$ is defined with the optimal (uncertainty-ratio) gain. A gain past the optimum moves the correction rate $\alpha$, not $\mathcal T$; it is reachable as a $\mathcal T$-change only through a mis-estimated $U_M$ or $U_o$ (the segment's own "for a Bayes-optimal agent the gain is already at that point" half-says this). Either retitle, or say the gain lever is miscalibration.
- **The Lipschitz sentence.** "For nonlinear correction, the direction holds whenever the mismatch transform is Lipschitz, since the injected noise then grows with the gain." Lipschitz bounds the injected noise from above; it cannot show the error grows. For fixed $g$ the fluctuation scales exactly with the gain whatever $g$ is, and a U-shape follows in a small-error linearization; the sentence's ground is the wrong one.
- **Information intake does not depend on the gain.** For a linear filter $d\hat x = -(\lambda + \alpha)\hat x\,dt + \alpha\,dy$, the path of $\hat x$ determines the path of $y$, so $I(x; \hat x) = I(x; y)$, which Duncan gives as $K/2$ per component for every $\alpha \gt 0$. Every linear corrector on that channel takes in the same rate; a mis-tuned one gets a worse error for it. `#deriv-persistence-cost`'s "the price follows from the error that gain achieves" is the floor at that error, slack for every $\alpha \neq K$, not what is paid. Also there: with $\lambda_s \gt 0$ the contraction rate of the error is $\lambda_s + K$, while the segment calls $K$ "the sector constant of its correction" and the Setup speaks of "a linear corrector at sector rate $\alpha$" whose contraction is $\lambda_s + \alpha$; and "a corrector below the optimal gain needs more than $n\alpha/2$ … one above it achieves a worse error" reads as if only one side has the worse error.
- **Term (i) is called estimation error.** In `#result-mismatch-decomposition`, the underbrace on (i), the opening "estimation term", and "positive estimation error (term i)" all name (i), while the new paragraph and `#def-mismatch-signal` define estimation error as (i)+(ii).
- **`#def-mismatch-signal` overstates two things.** "That is the quantity a correction can drive toward zero" ignores term (ii): the state-and-law floor binds the estimation error of every chronica-measurable predictor (the Kalman error $P$ is that floor at the optimum). And "'Mismatch' without qualification is used only where a statement holds for either object" is false of canon as written; `#result-persistence-condition` alone says "Mismatch is ultimately bounded by $R^\ast$" unqualified.
- **`#obs-gated-tempo-advantage` is the same mechanism, in canon, uncited both ways.** Its Epistemic Status says "Max attainable: derived (the mechanism is analytically tractable via Riccati analysis of noisy AR(1) processes)". The new Setup paragraph is that derivation for the single agent; the adversarial exponent table is not derived by it.
- **`#der-deliberation-cost` contradicts the trade-off.** Its net benefit $\Delta\eta^\ast\cdot\lVert\delta_{\text{post}}\rVert - \rho_{\text{delib}}\Delta\tau$ prices any gain increase as pure reduction, which "Two levers" says is false past the optimum, and multiplies by an observed (innovation) magnitude to get a change in estimation error. The integrator flagged it as untraced; it is a real defect.
- **State-dependent injected noise.** For nonlinear $g$ the gain-injected fluctuation has a covariance that depends on $\bar\delta$. A.1S is stated for additive $\sigma_w\,dW$. The stopped bound still holds with $n\sigma_w^2$ replaced by the supremum over $\mathcal B_R$ of the diffusion's trace; `#deriv-gain-sector` B.3's "belongs to the disturbance" should say so.
- **Restatements the drain missed.** `#def-death-as-factor-loss` (Vol 4, line 39) states "$\dot R \geq n\alpha/2$" and "$C_{\text{channel}} \geq n\alpha/2$" as the floor, twice. `#impl-persistence-and-limits` line 131 says "burn-rate ($\dot R \geq n\alpha/2$)". `#scope-evolving-software` (TST) reads $\rho$ as "environment change rate" and concludes "any nonzero tempo suffices"; with a noisy channel, $\rho_{\text{env}} \to 0$ leaves the floor $\bar\nu$, so it suffices only if $\bar\nu \lt \lVert\delta_{\text{critical}}\rVert$.
- **A ghost.** `#impl-persistence-and-limits` line 39: "The environment does not cancel out of it" answers the deleted audit-gold bullet. The positive claim after it can stand alone.
- **`#example-kalman`.** The Mapping table still says "Sector parameter ($\alpha = \mathcal T$)", and the Lyapunov section gives $3.315\ \text{s}^{-1}$ (the transient mix) beside the steady-state $K_{ss} = 0.390$; at $\nu = 5$ the steady-state rate is $\nu K_{ss} = 1.95$ (or $-\nu\ln(1-K_{ss}) = 2.47$ as an exact per-step contraction rate). The integrator named this but did not file it; it is filed now.

## Scripts

Each runs with `python3 -I` and needs numpy.

### `window.py`

```python
"""Independent check (verifier): Model S mean-square persistence with gain-injected
channel noise is a window in alpha, geometric about the Kalman-Bucy gain.
Error SDE (linear corrector, random-walk signal): de = -a e dt + s dW - a o dV.
Exact discretisation used (not Euler), so it is independent of kb_check.py."""
import numpy as np
rng = np.random.default_rng(7)
s, o, n = 1.0, 0.5, 1
K = s / o; P = s * o
def ss_var(a): return n * (s*s + a*a*o*o) / (2*a)
def sim(a, dt=2e-3, N=60000, M=2000):
    phi = np.exp(-a*dt); qv = (s*s + a*a*o*o) * (1 - phi*phi) / (2*a)
    e = np.zeros(M); acc = 0.0; c = 0
    for i in range(N):
        e = phi*e + np.sqrt(qv)*rng.standard_normal(M)
        if i > N//5: acc += np.mean(e*e); c += 1
    return acc/c
for a in [0.5*K, K, 2*K, 4*K]:
    print(f"a={a:.2f}  closed={ss_var(a):.4f}  sim={sim(a):.4f}")
for R2 in [0.4, 0.5, 0.6, 1.0, 3.0]:
    disc = R2*R2 - (n*s*o)**2
    if disc <= 0:
        print(f"R^2={R2}: no alpha persists (R^2 <= n s o = {n*s*o})"); continue
    lo = (R2 - np.sqrt(disc))/(n*o*o); hi = (R2 + np.sqrt(disc))/(n*o*o)
    grid = np.linspace(0.01, 60, 200000); ok = grid[ss_var(grid) < R2]
    print(f"R^2={R2}: window ({lo:.4f}, {hi:.4f}); grid ({ok.min():.4f}, {ok.max():.4f}); lo*hi={lo*hi:.4f} K^2={K*K:.4f}; log-halfwidth={np.log(hi/K):.4f} arccosh(R^2/(n s o))={np.arccosh(R2/(n*s*o)):.4f}")
```

Output: closed $0.6250, 0.5000, 0.6250, 1.0625$ against simulated $0.6248, 0.5006, 0.6265, 1.0613$; no window at $R^2 = 0.4, 0.5$; windows $(1.0734, 3.7266)$, $(0.5359, 7.4641)$, $(0.1678, 23.8322)$ at $R^2 = 0.6, 1, 3$, each with $\alpha_-\alpha_+ = 4 = K^2$ and log half-width equal to the arccosh.
