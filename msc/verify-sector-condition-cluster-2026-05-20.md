---
title: Strict-form independent-verify — sector-condition cluster
date: 2026-05-20
posture: adjudicator (independent of prior spike agents and parent applying canon edits)
scope: three load-bearing math claims feeding the AAT pre-print
---

# Strict-Form Independent-Verify — Sector-Condition Cluster (2026-05-20)

## §1 Setup

This document is the strict-form independent verification of three load-bearing math claims in `01-aat-core/` that landed in the 451729 D.1 Phase 4 cycle (commits `9054e9f`, `351ed95`), required before the monograph pre-print citation by two AIES papers in the next 24 hours.

**Substrate read first-hand:**

- `01-aat-core/src/deriv-sector-condition.md` (Prop A.1, A.1S, Cor A.1S.1, stopping-time localization).
- `01-aat-core/src/deriv-stochastic-non-exit.md` (the Model-S no-go demonstration).
- `01-aat-core/src/deriv-strategic-persistence-hard-ceiling.md` (Prop C.1 + Prop C.2).
- `01-aat-core/src/schema-strategy-persistence.md` §Forgetting as Prerequisite.
- `01-aat-core/src/deriv-edge-credence-dynamics.md` Prop B.1 (the source $\alpha = 1/(n+1)$).
- `01-aat-core/src/form-sector-condition.md` (the A2' formulation).

**Posture.** Independent re-derivation of each claim from first principles, not paraphrase. Discrepancies are surfaced as canon-correction findings; confirmations as substrate for the pre-print. No canon edits or commits — only this verification file.

The three claims under verification:

1. **Corollary A.1S.1 Model-S half** ($P(\tau_R \lt \infty) = 1$ under additive stochastic forcing, for every $\alpha \gt 0$, $\sigma_w \gt 0$, and every $F$ under A2').
2. **Exact steady-state form** $\alpha_\Sigma^{\text{ss}} = (1-\lambda)/(2-\lambda)$ under discounted Beta-Bernoulli updates with forgetting rate $\lambda$.
3. **Hard ceiling** Prop C.2: $\sup_{\lambda \in [0,1]} (1-\lambda)/(2-\lambda) = 1/2$, achieved as $\lambda \to 0^+$; reachable persistence region is the open half-plane $\rho_\Sigma \lt R_\Sigma/2$.

---

## §2 Corollary A.1S.1 Model-S Half — Independent Re-Derivation

### §2.1 What needs to be re-derived

The Model-S half asserts that for the SDE

$$d\delta = -F(\mathcal T, \delta)\,dt + \sigma_w\,dW_t, \quad \delta(0) \in \mathcal B_R, \quad \sigma_w \gt 0,$$

with $W_t$ a standard $n$-dimensional Wiener process and (A2') $\delta^\top F \geq \alpha\lVert\delta\rVert^2$ on $\mathcal B_R$ (any locally bounded $F$ satisfying this), the first-exit time $\tau_R = \inf\{t : \lVert\delta(t)\rVert \gt R\}$ satisfies

$$P(\tau_R \lt \infty) = 1 \qquad \text{for every } \alpha \gt 0,\ \sigma_w \gt 0,\ F \text{ under (A2').}$$

I verify three sub-claims independently:

- (a) The supermartingale-route impossibility: no nonnegative supermartingale dominating $V = \tfrac12\lVert\delta\rVert^2$ can certify a horizon-independent $P(\tau_R \lt \infty) \leq c \lt 1$.
- (b) The general fact: a non-degenerate diffusion under any locally bounded drift exits any bounded region a.s. in finite time.
- (c) The OU scale-function argument as the linear-Gaussian benchmark instance.

### §2.2 Independent re-derivation of (a) — supermartingale-route impossibility

I work this without looking at the segment's algebra. Let $V(\delta) = \tfrac12\lVert\delta\rVert^2$. By Itô's formula on the SDE,

$$dV = \delta^\top(-F)\,dt + \delta^\top\sigma_w\,dW_t + \tfrac{1}{2}\,\sigma_w^2 \,n\,dt,$$

where the Itô-correction term comes from $\tfrac{1}{2}\operatorname{tr}(\sigma_w^2 I_n) = \tfrac{n}{2}\sigma_w^2$. (Double-checked: with $V = \tfrac12 \sum_i \delta_i^2$, $\partial_i V = \delta_i$, $\partial_i^2 V = 1$, diffusion matrix $\sigma_w^2 I_n$, so the Itô correction is $\tfrac12 \sigma_w^2 \sum_i 1 = \tfrac{n}{2}\sigma_w^2$. Confirmed.)

Using (A2') on $[0, \tau_R]$, $-\delta^\top F \leq -\alpha\lVert\delta\rVert^2 = -2\alpha V$. So on $[0, \tau_R]$:

$$dV \leq -2\alpha V\,dt + \tfrac{n}{2}\sigma_w^2\,dt + \delta^\top\sigma_w\,dW_t.$$

The strengthening attempt is to find some nonnegative process $S$, dominated by $V$ (or related to $V$), that is a supermartingale on $[0, \tau_R]$, so that Doob's / Ville's inequality bounds $P(\sup_{t \leq \tau_R} S_t \geq c)$ uniformly in horizon.

**Attempt 1: $V$ itself is not a supermartingale.** From the above, $dV$ has positive drift $\tfrac{n}{2}\sigma_w^2$ (the Itô correction) plus the inward $-2\alpha V$. Near the origin, where $V \approx 0$, the positive drift dominates and $V$ increases on average — not a supermartingale.

**Attempt 2: Exponential weighting.** Consider $G(t) = e^{2\alpha t} V(\delta(t))$. By product rule on $[0, \tau_R]$:

$$dG = e^{2\alpha t}[2\alpha V\,dt + dV] = e^{2\alpha t}\big[\underbrace{(2\alpha V - \delta^\top F)}_{\leq 0 \text{ by A2'}}\,dt + \tfrac{n}{2}\sigma_w^2\,dt + \delta^\top\sigma_w\,dW_t\big].$$

The first bracketed term is $\leq 0$ by A2' (since $\delta^\top F \geq \alpha\lVert\delta\rVert^2 = 2\alpha V$, hence $2\alpha V - \delta^\top F \leq 0$). The Itô term is mean-zero. But the $\tfrac n2 \sigma_w^2 e^{2\alpha t}\,dt$ contribution has strictly positive expected drift, growing exponentially — so $G$ is *not* a supermartingale either. The expected drift coefficient (after taking expectations of the bound) is

$$\frac{d}{dt}\mathbb E[G(t)] \leq \tfrac{n}{2}\sigma_w^2\,e^{2\alpha t},$$

which integrates to $\tfrac{n\sigma_w^2}{4\alpha}(e^{2\alpha t}-1)$ — strictly positive and unbounded in $t$.

**Attempt 3: Compensation.** Subtract the deterministic upper bound on the drift integral. Define

$$S(t) = e^{2\alpha(t\wedge\tau_R)} V(\delta_{t\wedge\tau_R}) - \frac{n\sigma_w^2}{4\alpha}\big(e^{2\alpha(t\wedge\tau_R)} - 1\big).$$

Then $dS \leq e^{2\alpha t}\delta^\top \sigma_w\,dW_t$ on $[0,\tau_R]$ (the positive drift is removed by the compensator). So $S$ is a supermartingale.

**The obstruction.** Ville's inequality requires $S \geq 0$ (nonnegative supermartingale). Is $S$ nonnegative?

$$S(t) \geq 0 \iff e^{2\alpha t} V(\delta(t)) \geq \frac{n\sigma_w^2}{4\alpha}(e^{2\alpha t}-1) \iff V(\delta(t)) \geq \frac{n\sigma_w^2}{4\alpha}\left(1 - e^{-2\alpha t}\right).$$

As $t \to \infty$, the right side tends to $n\sigma_w^2/(4\alpha)$. So $S$ is nonnegative *only if* $V(\delta(t)) \geq n\sigma_w^2/(4\alpha)$, i.e., $\lVert\delta(t)\rVert^2 \geq n\sigma_w^2/(2\alpha)$, i.e., $\lVert\delta(t)\rVert \geq \sigma_w\sqrt{n/(2\alpha)} = R^\ast_S$.

But the mean-square persistence condition (Prop A.1S(ii)) places the stationary RMS radius $R^\ast_S \lt R$ comfortably inside $\mathcal B_R$ — meaning the typical trajectory has $\lVert\delta\rVert \lt R^\ast_S$ much of the time, so $V \lt n\sigma_w^2/(4\alpha)$ much of the time, so $S \lt 0$ much of the time. **$S$ is sign-indefinite exactly on the persistence basin** — the very region where it would need to be a positive certificate. Ville's inequality is not applicable. The same obstruction blocks Doob's maximal inequality for nonnegative sub/supermartingales.

**Why no other compensator works.** Any nonnegative supermartingale dominating $V$ (or related to it) would need to absorb the Itô-correction positive drift. The Itô correction is *constant in $\delta$* and *non-vanishing* — it operates everywhere, not just near boundary. A compensator that subtracts off a deterministic growth term tracking $\tfrac n2 \sigma_w^2$ destroys nonnegativity at the persistence basin where $V$ itself is small. A multiplicative-in-$V$ compensator cannot work because $V$ vanishes at the origin while the Itô correction does not.

More structurally: a horizon-independent $P(\tau_R \lt \infty) \leq c \lt 1$ via gambler's-ruin / Lyapunov-exit machinery requires a bounded *harmonic* (or super-harmonic) function with strict variation across the boundary — for the additive-Brownian generator $\mathcal L = -F\cdot\nabla + \tfrac12 \sigma_w^2 \Delta$, the only bounded functions $h$ with $\mathcal L h \leq 0$ on a bounded region that extend smoothly are constants (this is the additive-noise consequence of recurrence; see (b) below). No certificate exists.

**Verdict on (a): CONFIRMED.** My re-derivation reproduces the same obstruction the segment names: the only naturally-compensated supermartingale $S$ is sign-indefinite exactly inside the persistence basin, and Ville/Doob both require nonnegativity. The obstruction is structural and not removable.

### §2.3 Independent re-derivation of (b) — almost-sure exit of non-degenerate diffusion

Claim: under $d\delta = b(\delta)\,dt + \sigma_w\,dW_t$ on $\mathbb R^n$ with $\sigma_w \gt 0$ and $b$ any locally bounded drift, the first exit time $\tau_R$ from any bounded region $\mathcal B_R$ satisfies $\tau_R \lt \infty$ a.s.

I work this from first principles. Two complementary routes:

**Route 1 (small-ball lower bound).** For any open ball $\mathcal B_R$ with $\delta(0) \in \mathcal B_R$, consider a time interval $[t, t+h]$. On this interval, by Itô,

$$\delta(t+h) - \delta(t) = \int_t^{t+h} b(\delta(s))\,ds + \sigma_w \big(W(t+h) - W(t)\big).$$

Since $\delta$ stays in some compact set on $[t, t+h] \cap [0, \tau_{2R}]$ a.s. by continuity, $b$ is bounded by some $M$ on that set. The drift contribution is at most $Mh$ in magnitude. The Wiener increment $\sigma_w(W(t+h)-W(t))$ is Gaussian $N(0, \sigma_w^2 h I_n)$, so for any direction $e \in \mathbb R^n$ with $\lVert e\rVert = 1$,

$$P\big(e^\top(W(t+h)-W(t)) \gt c\big) = P(Z \gt c/\sqrt h), \quad Z \sim N(0,1),$$

which is bounded below by some $p_0 \gt 0$ independent of $t$, for $c$ of order $\sqrt h$.

Pick $h$ small enough that $Mh \lt R/2$. Pick the direction $e = \delta(t)/\lVert\delta(t)\rVert$ (or any radially-outward direction). The Brownian increment in direction $e$ exceeds $\sigma_w \sqrt h \cdot 1$ with probability $p_0 \gt 0$ (standard Gaussian-tail constant). If $\sigma_w\sqrt h \gt R + Mh$ (say $h$ such that $\sigma_w\sqrt h = 2R$, achievable by picking $h$ large enough — but then $Mh$ also grows... let me be careful).

Better: pick $h$ small. On $[t, t+h]$, drift contributes at most $Mh = O(h)$, but Brownian increment scales as $O(\sqrt h)$. For small $h$, $\sqrt h \gg h$, so the Brownian increment dominates. Specifically, with $h$ small the probability that $\lVert W(t+h) - W(t)\rVert \gt R/\sigma_w$ is positive — Gaussian $N(0, h I_n)$ has unbounded support — but the probability shrinks to 0 as $h \to 0$.

Let me be more careful. Fix $h^\ast \gt 0$. The Brownian increment $W(t+h^\ast)-W(t)$ has Gaussian distribution $N(0, h^\ast I_n)$, so $\lVert W(t+h^\ast)-W(t)\rVert$ has positive density on $[0, \infty)$. In particular,

$$p_0 := \inf_{x \in \mathcal B_R} P_x\big(\lVert\delta(h^\ast)\rVert \gt R\big) \gt 0,$$

for any fixed $h^\ast \gt 0$ (since the drift correction is bounded by $\sup_{\mathcal B_{2R}} \lVert b\rVert \cdot h^\ast =: \bar b h^\ast$, and we can choose $h^\ast$ so that the Brownian increment of magnitude $\gt R + \bar b h^\ast$ has uniformly-positive probability).

Wait — there's a subtlety: the SDE solution might exit $\mathcal B_{2R}$ and the drift might not be locally bounded outside. Assume drift is globally locally bounded (true for any continuous $F$ on $\mathbb R^n$). Then the comparison works.

By the strong Markov property at $t, 2t, 3t, \ldots$ (with $t = h^\ast$), the events $A_k = \{\text{starting at time } kh^\ast \text{ from inside } \mathcal B_R, \text{the trajectory exits by time } (k+1)h^\ast\}$ each have probability $\geq p_0$ conditional on $\delta(kh^\ast) \in \mathcal B_R$. These are not independent, but by the strong Markov property,

$$P(\tau_R \gt Nh^\ast) \leq P(A_1^c \cap A_2^c \cap \cdots \cap A_N^c) \leq (1-p_0)^N \to 0.$$

So $P(\tau_R = \infty) = 0$, i.e., $\tau_R \lt \infty$ a.s. $\square$

**Route 2 (scale-function / harmonic-function argument).** For the linear-Gaussian (Ornstein-Uhlenbeck) instance $dX = -\alpha X\,dt + \sigma_w\,dW$ in $\mathbb R^1$, the scale function is

$$s(x) = \int_0^x \exp\left(\int_0^u \frac{2\alpha v}{\sigma_w^2}\,dv\right) du = \int_0^x \exp\left(\frac{\alpha u^2}{\sigma_w^2}\right) du.$$

The integrand grows like $e^{\alpha u^2/\sigma_w^2}$, so $s(\pm\infty) = \pm\infty$, meaning the scale function is unbounded in both directions. By Feller's classification (or directly: the natural scale process $s(X_t)$ is a continuous local martingale with unbounded support; it must visit every level a.s. by recurrence of 1D continuous local martingales of unbounded variation), $X_t$ visits every point of $\mathbb R$ a.s. — in particular, exits any bounded interval $(-R, R)$ a.s. in finite time. This is the explicit linear-Gaussian instance.

For general non-degenerate diffusions with locally bounded drift on $\mathbb R^n$, the same conclusion follows from Khasminskii ch. 3–4: the generator has no bounded non-constant harmonic functions, so by the optional-stopping argument no horizon-independent containment can hold; combined with Route 1's positive-probability-of-exit-per-unit-time argument, $\tau_R \lt \infty$ a.s.

**Verdict on (b): CONFIRMED.** Re-derived via small-ball-lower-bound + Borel-Cantelli-like argument under strong Markov; consistent with the scale-function route for the OU benchmark.

### §2.4 Independent re-derivation of (c) — OU scale function

Explicit: $dX = -\alpha X\,dt + \sigma_w\,dW$ on $\mathbb R$. The infinitesimal generator is

$$\mathcal L f = -\alpha x f'(x) + \tfrac12 \sigma_w^2 f''(x).$$

Scale function $s$ satisfies $\mathcal L s = 0$, i.e.,

$$\tfrac12 \sigma_w^2 s''(x) = \alpha x s'(x).$$

Setting $\phi = s'$: $\phi'/\phi = 2\alpha x / \sigma_w^2$, so $\phi(x) = \phi(0)\exp(\alpha x^2 / \sigma_w^2)$. Then

$$s(x) = s(0) + \phi(0) \int_0^x e^{\alpha u^2 / \sigma_w^2}\,du.$$

The integrand grows super-polynomially, so $s(\pm \infty) = \pm \infty$ (with appropriate sign of $\phi(0)$). By Feller's test for explosions / recurrence, the OU process is recurrent on $\mathbb R$, hence visits every level a.s.; in particular exits $(-R, R)$ a.s. in finite time.

**Connection to segment text.** Segment phrases this as: "the OU scale density $\propto e^{\alpha u^2/\sigma_w^2}$" — i.e., $s'(u) \propto e^{\alpha u^2/\sigma_w^2}$. Confirmed. The scale function is the *antiderivative* of this density, hence unbounded.

**Verdict on (c): CONFIRMED.** Matches the segment's claim exactly. The scale density formula and the unboundedness of $s$ both verify.

### §2.5 Comparison to segment text

The segment in `deriv-stochastic-non-exit.md` provides essentially the same three-pronged structure (lines 30–42):

- Lines 32–34: derives $dG$ for $G(t) = e^{2\alpha t} V$, identifying the positive exponentially-growing drift. ✓ Matches my Attempt 2.
- Lines 36–40: defines the compensated $S(t)$ and identifies the sign-indefiniteness condition $V \lt n\sigma_w^2/(4\alpha)$ (translated: $\lVert\delta\rVert \lt \sigma_w\sqrt{n/(2\alpha)} = R^\ast_S$). ✓ Matches my Attempt 3.
- Line 42: states the general (b) fact for any locally bounded drift, noting OU is the "explicit instance, not the basis." ✓ Matches my Route 1 reading.

One micro-observation worth surfacing: in my Attempt 3, the segment writes the persistence basin condition as "$V \lt n\sigma_w^2/(4\alpha)$." Let me double-check the constant. $V = \tfrac12\lVert\delta\rVert^2$ and $R^\ast_S = \sigma_w\sqrt{n/(2\alpha)}$ gives $V^\ast_S = \tfrac12 (R^\ast_S)^2 = \tfrac12 \cdot \sigma_w^2 n/(2\alpha) = n\sigma_w^2/(4\alpha)$. ✓ Constant confirmed.

The segment also notes that "under the mean-square persistence condition" $R^\ast_S \lt R$, the typical trajectory has $V \ll n\sigma_w^2/(4\alpha)$ — i.e., the basin where $S \lt 0$ is the *typical* region. ✓ This is the right framing: $S$ is sign-indefinite at the very location where positivity would be needed.

### §2.6 Verdict — Claim 1

**CONFIRMED (exact).** All three sub-claims (a) supermartingale-route impossibility, (b) general a.s. exit, (c) OU scale-function unboundedness independently re-derive to the same conclusions stated in `deriv-stochastic-non-exit.md` and Cor A.1S.1 of `deriv-sector-condition.md`. The exact dichotomy $P(\tau_R \lt \infty) \in \{0,1\}$ with the value selected by the disturbance model's support structure (bounded vs additive-stochastic) is sound.

The claim that this is $\alpha$-invariant — that no finite correction strength can convert $P(\tau_R \lt \infty)$ from $1$ to anything less — is also confirmed: A2' bounds $\delta^\top F$ from below, but does not make $F$ unbounded near $\partial\mathcal B_R$; a finite inward push cannot defeat a Brownian increment of arbitrary magnitude over any time interval. The Gaussian-tail-positive-probability argument in Route 1 is independent of the size of $\alpha$.

---

## §3 Exact Steady-State Form $\alpha_\Sigma^{\text{ss}} = (1-\lambda)/(2-\lambda)$ — Independent Re-Derivation

### §3.1 Source check — Prop B.1

From first-hand reading of `deriv-edge-credence-dynamics.md` lines 47–87:

Prop B.1 setup: one action $A$, one goal $G$, credence $\hat p$, true probability $\theta$, mismatch $\delta_\Sigma = \hat p - \theta$. Beta-Bernoulli update:

$$\Delta\hat p_k = \frac{y_k - \hat p_k}{n_k + 1}, \quad \eta_k = \frac{1}{n_k + 1}.$$

The expected update at $\hat p$ is $\mathbb E[\Delta\hat p] = (\theta - \hat p)/(n+1) = -\delta_\Sigma/(n+1)$. Identifying $F_\Sigma(\delta_\Sigma) = -\mathbb E[\Delta\delta_\Sigma] = \delta_\Sigma/(n+1)$ gives

$$\delta_\Sigma \cdot F_\Sigma(\delta_\Sigma) = \delta_\Sigma^2/(n+1) = \frac{1}{n+1}\lVert\delta_\Sigma\rVert^2,$$

i.e., $\alpha_\Sigma = 1/(n+1)$, with the bound tight (the correction is exactly linear).

**Verdict on the source:** Prop B.1 cleanly states $\alpha = 1/(n+1)$ for the canonical Beta-Bernoulli single-edge case. ✓

### §3.2 Independent derivation of the discounted-update fixed point

The discounted Beta-Bernoulli recurrence:

$$\alpha_k \mapsto \lambda \alpha_k + y_k, \qquad \beta_k \mapsto \lambda \beta_k + (1-y_k),$$

where $y_k \in \{0,1\}$ is the observation indicator and $\lambda \in (0,1)$ is the discount factor.

**Fixed point in expectation.** Taking expectations of the recurrence (with $\mathbb E[y_k] = \theta$ at the fixed point $\hat p = \theta$):

$$\alpha^\ast = \lambda \alpha^\ast + \theta \implies \alpha^\ast(1 - \lambda) = \theta \implies \alpha^\ast = \frac{\theta}{1-\lambda},$$

$$\beta^\ast = \lambda \beta^\ast + (1 - \theta) \implies \beta^\ast = \frac{1-\theta}{1-\lambda}.$$

Effective sample size:

$$n_{\text{eff}} = \alpha^\ast + \beta^\ast = \frac{\theta + (1-\theta)}{1-\lambda} = \frac{1}{1-\lambda}.$$

This is the standard "geometric series" effective-sample-size result: a unit-of-evidence per step, geometrically discounted, summing to $\sum_{k=0}^\infty \lambda^k = 1/(1-\lambda)$.

**Substituting into Prop B.1.** Prop B.1 gives $\alpha_\Sigma = 1/(n+1)$ where $n$ is the accumulated pseudo-count (the Beta posterior's total $\alpha + \beta$). At the discounted-update steady state, $n \to n_{\text{eff}} = 1/(1-\lambda)$:

$$\alpha_\Sigma^{\text{ss}} = \frac{1}{n_{\text{eff}} + 1} = \frac{1}{\frac{1}{1-\lambda} + 1} = \frac{1}{\frac{1 + (1-\lambda)}{1-\lambda}} = \frac{1-\lambda}{2-\lambda}.$$

Let me verify the algebra step-by-step:

- $1/(1-\lambda) + 1 = (1 + (1-\lambda))/(1-\lambda) = (2-\lambda)/(1-\lambda)$.
- Reciprocal: $(1-\lambda)/(2-\lambda)$.

✓ Algebra correct.

### §3.3 Sanity checks

- **At $\lambda = 0$ (no memory):** $\alpha_\Sigma^{\text{ss}} = 1/2$. Check: $n_{\text{eff}} = 1/(1-0) = 1$, and $\alpha_\Sigma = 1/(1+1) = 1/2$. ✓ Each new observation completely replaces the prior.
- **At $\lambda \to 1^-$ (no forgetting):** $\alpha_\Sigma^{\text{ss}} = (1-\lambda)/(2-\lambda) \to 0/1 = 0$. Check: $n_{\text{eff}} \to \infty$, and $\alpha_\Sigma = 1/(n+1) \to 0$. ✓ With infinite memory, gain collapses (matches the raw Bayesian $\alpha = 1/(n+1) \to 0$ asymptotic).
- **Slow-forgetting linear form $\alpha_\Sigma^{\text{ss}} \approx 1 - \lambda$.** Expand: $(1-\lambda)/(2-\lambda) = (1-\lambda) \cdot \frac{1}{2-\lambda}$. As $\lambda \to 1$, $1/(2-\lambda) \to 1$, so the leading-order term is $1-\lambda$. ✓
- **At $\lambda = 0.5$:** exact $= 0.5/1.5 = 1/3 \approx 0.333$; linear $= 0.5$. Overestimate by $50\%$. ✓ Matches segment's claim.
- **At $\lambda = 0.9$:** exact $= 0.1/1.1 = 1/11 \approx 0.0909$; linear $= 0.1$. Overestimate by $\approx 10\%$. ✓ Matches segment's claim.

### §3.4 Independent verification: a more careful look at the fixed-point convergence

The fixed-point-in-expectation derivation assumes the recurrence converges. Let me verify convergence rate.

The recurrence in expectation: let $a_t = \mathbb E[\alpha_t]$. Then $a_t = \lambda a_{t-1} + \theta$. This is a linear recurrence with solution

$$a_t = \lambda^t a_0 + \theta \cdot \frac{1-\lambda^t}{1-\lambda} \to \frac{\theta}{1-\lambda} \quad \text{as } t \to \infty.$$

Convergence is geometric at rate $\lambda$. Same for $b_t = \mathbb E[\beta_t]$. Adding: $n_t = a_t + b_t \to 1/(1-\lambda)$, also at rate $\lambda$. ✓ Convergence verified.

### §3.5 Comparison with segment text

The segment in `deriv-strategic-persistence-hard-ceiling.md` lines 32–46 gives the same Prop C.1 derivation. The schema segment `schema-strategy-persistence.md` lines 44–50 also states the same exact form. My re-derivation produces identical algebra and constants.

One careful observation: the segment text is correct in stating that the linear approximation $\alpha_\Sigma^{\text{ss}} \approx 1-\lambda$ is the leading-order expansion *as $\lambda \to 1$* (slow-forgetting limit). For small $\lambda$ (fast forgetting), the exact form $(1-\lambda)/(2-\lambda)$ is necessary; the linear form overstates by the factor $1/(2-\lambda)$, which is bounded above by $1$ at $\lambda = 1$ and bounded above by $1/2$ at $\lambda = 0$.

### §3.6 Verdict — Claim 2

**CONFIRMED (exact, under stated conditions).** The exact steady-state $\alpha_\Sigma^{\text{ss}} = (1-\lambda)/(2-\lambda)$ follows cleanly from:
1. Prop B.1's $\alpha_\Sigma = 1/(n+1)$ for the canonical Beta-Bernoulli case (verified first-hand from segment).
2. The discounted-update fixed-point $n_{\text{eff}} = 1/(1-\lambda)$ (re-derived independently).
3. Algebraic substitution.

All three steps are elementary and exact. The conditions are clean: Beta-Bernoulli edge dynamics, exponential forgetting with $\lambda \in (0,1)$, evaluation at the fixed-point $\hat p = \theta$.

The status `exact` is appropriate under those named conditions; uncertainty resides in whether the conditions hold (which mismatch state, which topology, whether exponential forgetting is the actual mechanism), not in the derivation.

---

## §4 Hard Ceiling Prop C.2 — Independent Re-Derivation

### §4.1 What needs to be re-derived

Prop C.2 asserts:

(i) The forgetting prerequisite for the schema's trajectory guarantee is $(1-\lambda)/(2-\lambda) \gt \rho_\Sigma/R_\Sigma$.

(ii) This is unsatisfiable for any $\lambda \in [0,1]$ when $\rho_\Sigma \geq R_\Sigma/2$.

(iii) $\sup_{\lambda \in [0,1]} \alpha_\Sigma^{\text{ss}}(\lambda) = 1/2$, achieved as $\lambda \to 0^+$ (or at $\lambda = 0$, depending on whether $\lambda = 0$ is in the domain).

(iv) The reachable persistence region is exactly the open half-plane $\rho_\Sigma \lt R_\Sigma/2$.

### §4.2 Independent re-derivation

Set $x = \rho_\Sigma/R_\Sigma$. The forgetting prerequisite is

$$f(\lambda) := \frac{1-\lambda}{2-\lambda} \gt x.$$

**Step 1: Monotonicity of $f$.** Differentiate:

$$f'(\lambda) = \frac{-(2-\lambda) - (1-\lambda)(-1)}{(2-\lambda)^2} = \frac{-(2-\lambda) + (1-\lambda)}{(2-\lambda)^2} = \frac{-1}{(2-\lambda)^2} \lt 0.$$

So $f$ is strictly decreasing on $[0, 1]$. ✓

**Step 2: Range of $f$ on $[0, 1]$.**

- $f(0) = 1/2$.
- $f(1) = 0/1 = 0$.

So $f$ maps $[0,1]$ continuously and strictly-decreasingly onto $[0, 1/2]$. ✓

**Step 3: Supremum.** $\sup_{\lambda \in [0,1]} f(\lambda) = f(0) = 1/2$. The supremum is achieved at $\lambda = 0$ (a maximum, not just a supremum, if the domain includes $\lambda = 0$).

Note: the segment phrasing "achieved as $\lambda \to 0^+$" suggests the canonical domain is $\lambda \in (0,1)$ (open interval). Both readings give $\sup = 1/2$; whether the boundary is achieved or only approached depends on the domain. The schema segment specifies $\lambda \in (0,1)$ open interval at line 44; Prop C.2 segment line 56 uses $\lambda \in [0,1]$ closed interval. Discrepancy noted but minor — see §4.4 below.

**Step 4: Solve for threshold $\lambda$ given $x$.** Set $f(\lambda) = x$:

$$\frac{1-\lambda}{2-\lambda} = x \implies 1 - \lambda = x(2-\lambda) \implies 1 - \lambda = 2x - x\lambda \implies \lambda(x - 1) = 2x - 1.$$

If $x \neq 1$:

$$\lambda = \frac{2x-1}{x-1} = \frac{1-2x}{1-x}.$$

(Multiplying numerator and denominator by $-1$.)

**Step 5: When does this have a solution in $[0,1]$?** For $\lambda \in [0,1)$ (we need denominator $1-x \gt 0$, i.e., $x \lt 1$, automatically the case for any meaningful disturbance ratio with $\rho_\Sigma \lt R_\Sigma$):

- $\lambda \geq 0$ iff $1 - 2x \geq 0$ (given $1-x \gt 0$), iff $x \leq 1/2$.
- $\lambda \lt 1$ iff $(1-2x) \lt (1-x)$, iff $-x \lt 0$, iff $x \gt 0$. Always true for nontrivial cases.

So the equation $f(\lambda) = x$ has a solution $\lambda \in [0,1)$ iff $x \leq 1/2$.

**Step 6: Strict inequality.** The forgetting prerequisite requires *strict* $f(\lambda) \gt x$. Since $f$ is strictly decreasing, $f(\lambda) \gt x$ iff $\lambda \lt \lambda^\ast$ where $\lambda^\ast = (1-2x)/(1-x)$ is the threshold solving $f(\lambda^\ast) = x$.

- For $x \lt 1/2$: $\lambda^\ast \gt 0$, so $\lambda \in [0, \lambda^\ast)$ admits strict satisfaction. Reachable.
- For $x = 1/2$: $\lambda^\ast = 0$, so $\lambda \lt 0$ would be required. No $\lambda \in [0,1)$ admits strict satisfaction. (Equality holds at $\lambda = 0$: $f(0) = 1/2 = x$, but not strict.)
- For $x \gt 1/2$: even $\lambda = 0$ gives $f(0) = 1/2 \lt x$. No $\lambda$ admits any satisfaction.

**Conclusion:** the schema's strict persistence prerequisite $\alpha_\Sigma^{\text{ss}} \gt x$ is satisfiable iff $x \lt 1/2$, i.e., $\rho_\Sigma \lt R_\Sigma/2$. The reachable region is exactly the open half-plane $\rho_\Sigma \lt R_\Sigma/2$. The boundary $\rho_\Sigma = R_\Sigma/2$ is unreachable (equality, not strict).

### §4.3 Comparison with segment text

The proof in `deriv-strategic-persistence-hard-ceiling.md` Prop C.2 (lines 53–70):

- The threshold-$\lambda$ formula $\lambda = (1-2x)/(1-x)$ is derived exactly as I did. ✓
- The condition $1 - 2x \gt 0 \iff x \lt 1/2$ for strict satisfaction. ✓
- At $x = 1/2$: $\lambda = 0$, giving $\alpha_\Sigma^{\text{ss}}(0) = (1-0)/(2-0) = 1/2 = x$ — equality, not strict. ✓
- For $x \gt 1/2$: no $\lambda \in [0,1]$ satisfies strict inequality. ✓
- Supremum $\sup_{\lambda \in [0,1]} = 1/2$ at $\lambda = 0$. ✓

The reachable-region statement on line 72 matches mine: "$\{(\rho_\Sigma, R_\Sigma) : \rho_\Sigma \lt R_\Sigma/2\}$" — open half-plane, boundary not in reachable region.

### §4.4 Minor observation: domain inconsistency between segments

The schema segment `schema-strategy-persistence.md` line 44 specifies $\lambda \in (0,1)$ (open interval — the standard adaptive-control convention where $\lambda = 0$ means no memory and $\lambda = 1$ means no forgetting).

The hard-ceiling segment `deriv-strategic-persistence-hard-ceiling.md` lines 50, 58, 60 use $\lambda \in [0,1]$ (closed interval), and explicitly evaluates $f(0) = 1/2$ as achievable.

This is a **micro-inconsistency** in domain specification: if $\lambda \in (0,1)$, then $\sup = 1/2$ is approached as $\lambda \to 0^+$ but not achieved. If $\lambda \in [0,1]$, then $\sup = 1/2$ is achieved at $\lambda = 0$ (a maximum).

The hard-ceiling segment itself phrases this consistently: line 60 says "supremum is sharp: $\sup = 1/2$ achieved as $\lambda \to 0^+$ (maximally aggressive forgetting — no memory)." This is a slightly hybrid phrasing — "achieved as $\lambda \to 0^+$" suggests open interval, but the proof on line 70 explicitly evaluates $f(0) = (1-0)/(2-0) = 1/2$ at $\lambda = 0$ exactly.

The mathematical content is unambiguous either way:
- If $\lambda \in (0,1)$: $\sup = 1/2$, not achieved; reachable region is open half-plane $\rho_\Sigma \lt R_\Sigma/2$.
- If $\lambda \in [0,1]$: $\sup = \max = 1/2$, achieved at $\lambda = 0$; reachable region is *still* open half-plane $\rho_\Sigma \lt R_\Sigma/2$ (because strict satisfaction $f(\lambda) \gt x$ is required, and equality at $\lambda = 0, x = 1/2$ is not strict).

The "open half-plane" reachability conclusion is robust to the domain question. The flag is **stylistic, not load-bearing.** Suggested polish (not required for pre-print correctness): make the domain convention consistent across the two segments — either both use $\lambda \in (0,1)$ with "supremum approached" framing, or both use $\lambda \in [0,1]$ with "maximum achieved at boundary" framing. The current hybrid is mildly distracting but mathematically harmless.

### §4.5 Verdict — Claim 3

**CONFIRMED (exact).** Prop C.2 is algebraically sound:

- $f(\lambda) = (1-\lambda)/(2-\lambda)$ is strictly decreasing on $[0,1]$ (derivative $-1/(2-\lambda)^2 \lt 0$, verified independently).
- $\sup_{\lambda \in [0,1]} f(\lambda) = 1/2$, at $\lambda = 0$ (or as $\lambda \to 0^+$ if domain is open).
- Forgetting prerequisite $f(\lambda) \gt \rho_\Sigma/R_\Sigma$ is satisfiable iff $\rho_\Sigma \lt R_\Sigma/2$.
- Reachable region is exactly the open half-plane $\rho_\Sigma \lt R_\Sigma/2$.

The hard ceiling at $\rho_\Sigma = R_\Sigma/2$ is structural — it does not depend on tuning of $\lambda$, and it does not depend on which of the schema's verified topologies (single-edge, two-edge AND, two-arm OR, mixed AND/OR) is in play, since all of them use the same canonical Beta-Bernoulli $\alpha = 1/(n+1)$ form at the per-edge level.

The minor domain inconsistency between schema and hard-ceiling segments is stylistic, not load-bearing.

---

## §5 Cascade-Check — Segment-to-Segment Integration

### §5.1 Does Cor A.1S.1 cite `#deriv-stochastic-non-exit` correctly?

Cor A.1S.1 in `deriv-sector-condition.md` lines 199–209 states the dichotomy $P(\tau_R \lt \infty) \in \{0, 1\}$. The Model-S half is stated in lines 205–207, with explicit pointer:

> "That the natural maximal-inequality route to a $P(\tau_R \lt \infty) \lt 1$ bound *cannot* exist — the question 'are you sure you can't just Doob/Ville this?' — is demonstrated in `#deriv-stochastic-non-exit`."

The demonstration in `deriv-stochastic-non-exit.md` is the correct target: it carries the supermartingale-route impossibility proof. ✓

The Findings section of `deriv-sector-condition.md` (line 271) additionally cross-references: "The Model-S half is the load-bearing proof step demonstrated at length in `#deriv-stochastic-non-exit`." ✓

The dependency chain is clean: A2' (in `form-sector-condition`) → Itô-Lyapunov + stopped Grönwall (Prop A.1S in `deriv-sector-condition`) → no-go demonstration (`deriv-stochastic-non-exit`) → categorical dichotomy (Cor A.1S.1 in `deriv-sector-condition`).

### §5.2 Does the schema cite `#deriv-strategic-persistence-hard-ceiling` correctly?

The schema `schema-strategy-persistence.md` lines 56–58 state the prerequisite inequality $(1-\lambda)/(2-\lambda) \gt \rho_\Sigma/R_\Sigma$ and add:

> "The hard ceiling at $\rho_\Sigma = R_\Sigma/2$ and the algebraic content of the steady-state form are derived self-contained in `#deriv-strategic-persistence-hard-ceiling` — a $\lambda$-independent structural cap on the schema's reachable persistence region under any exponential-forgetting design."

The target segment `deriv-strategic-persistence-hard-ceiling.md` correctly carries Prop C.1 (steady-state form) and Prop C.2 (hard ceiling) with depends-on `schema-strategy-persistence` and `deriv-edge-credence-dynamics`. ✓

The schema's Epistemic Status (line 77) explicitly defers to the hard-ceiling segment for the algebraic exactness:

> "Within these conditions the exact threshold $(1-\lambda)/(2-\lambda) \gt \rho_\Sigma/R_\Sigma$ and the hard ceiling at $\rho_\Sigma \ge R_\Sigma/2$ are algebraically exact — derived self-contained in `#deriv-strategic-persistence-hard-ceiling`."

The Findings Brief on line 119 also points correctly. ✓

### §5.3 Statement-form consistency check

Confirming the verbatim statements as listed in the task:

- **Cor A.1S.1 dichotomy form: $P(\tau_R \lt \infty) \in \{0, 1\}$** — 0 under Model D (pathwise containment) and 1 under Model S (certain region-exit). ✓ Line 205 of `deriv-sector-condition.md` states this exactly.

- **Schema exact threshold inequality**: $(1-\lambda)/(2-\lambda) \gt \rho_\Sigma/R_\Sigma$ as *the inequality*, not the bare form. ✓ Line 56 of `schema-strategy-persistence.md` states this exactly, with the algebraic rearrangement $\lambda \lt (R_\Sigma - 2\rho_\Sigma)/(R_\Sigma - \rho_\Sigma)$ for $\rho_\Sigma \lt R_\Sigma/2$.

- **Hard-ceiling Prop C.2 statement**: $\sup = 1/2$ at $\lambda \to 0^+$, with open half-plane $\rho_\Sigma \lt R_\Sigma/2$ as the reachable region. ✓ Lines 60, 62, 72 of `deriv-strategic-persistence-hard-ceiling.md` state this exactly.

### §5.4 Source-of-truth: Prop B.1 grounds the chain

The whole chain reduces to Prop B.1's $\alpha_\Sigma = 1/(n+1)$ as the source. From first-hand reading of `deriv-edge-credence-dynamics.md` lines 53–73, this is stated exactly and proved tightly (the correction is exactly linear, so the sector bound is sharp, not merely a lower bound). ✓

The chain $\alpha = 1/(n+1)$ → $n_{\text{eff}} = 1/(1-\lambda)$ → $\alpha_\Sigma^{\text{ss}} = (1-\lambda)/(2-\lambda)$ → hard ceiling at $\rho_\Sigma = R_\Sigma/2$ is sound at every step.

### §5.5 Cascade verdict

**Cascade integration: CLEAN.** All three load-bearing claims compose correctly:
- The dichotomy in Cor A.1S.1 cites `#deriv-stochastic-non-exit` correctly as the source of the Model-S no-go.
- The schema's threshold inequality cites `#deriv-strategic-persistence-hard-ceiling` correctly as the algebraic source.
- The hard-ceiling segment correctly grounds in Prop B.1 of `#deriv-edge-credence-dynamics` via Prop C.1 (steady-state $n_{\text{eff}}$ derivation).
- The verbatim statements match the task description.

The one minor stylistic flag is the domain-of-$\lambda$ phrasing inconsistency between schema ($\lambda \in (0,1)$ open) and hard-ceiling ($\lambda \in [0,1]$ closed). Mathematically harmless; cosmetically distracting if a reader notices. Not a blocker for pre-print.

---

## §6 Summary Verdict

| Claim | Verdict | Notes |
|---|---|---|
| **1.** Cor A.1S.1 Model-S half: $P(\tau_R \lt \infty) = 1$ under additive stochastic forcing, any $F$ under A2', any $\alpha, \sigma_w \gt 0$ | **CONFIRMED (exact)** | All three sub-claims (supermartingale-route impossibility, general a.s. exit, OU scale-function unboundedness) independently re-derive cleanly. Supermartingale obstruction is structural: only candidate compensated supermartingale $S$ is sign-indefinite exactly inside the persistence basin, where it would need to be positive. The general (b) fact follows from small-ball-positive-probability + strong Markov; OU benchmark via scale function confirmed. |
| **2.** Exact steady-state form $\alpha_\Sigma^{\text{ss}} = (1-\lambda)/(2-\lambda)$ | **CONFIRMED (exact)** | Three-step derivation: (i) Prop B.1 source $\alpha = 1/(n+1)$ verified first-hand; (ii) discounted-update fixed point $n_{\text{eff}} = 1/(1-\lambda)$ re-derived independently from the linear recurrence; (iii) algebraic substitution. All sanity checks pass ($\lambda=0$ gives $1/2$; $\lambda \to 1$ gives $0$; slow-forgetting linear approximation matches; quantitative overestimates at $\lambda = 0.5, 0.9$ match segment claims). |
| **3.** Hard ceiling Prop C.2: $\sup_\lambda (1-\lambda)/(2-\lambda) = 1/2$ at $\lambda = 0$; reachable region is open half-plane $\rho_\Sigma \lt R_\Sigma/2$ | **CONFIRMED (exact)** | $f(\lambda) = (1-\lambda)/(2-\lambda)$ is strictly decreasing (derivative $-1/(2-\lambda)^2$, verified). Range on $[0,1]$ is $[0, 1/2]$. Threshold $\lambda^\ast = (1-2x)/(1-x)$ solving $f(\lambda^\ast) = x$ is $\geq 0$ iff $x \leq 1/2$, $\gt 0$ iff $x \lt 1/2$. Strict satisfaction of prerequisite requires $x \lt 1/2$, i.e., $\rho_\Sigma \lt R_\Sigma/2$. Reachable region is open half-plane, boundary not included. Minor stylistic flag: schema specifies $\lambda \in (0,1)$ open, hard-ceiling segment uses $\lambda \in [0,1]$ closed — mathematically harmless inconsistency. |

**Cascade integration: CLEAN.** All segment-to-segment cross-references are accurate and the dependency chain composes correctly.

**Frame defects:** None of load-bearing significance.

- **Minor stylistic flag (not blocking pre-print):** Domain-of-$\lambda$ inconsistency between schema (open interval) and hard-ceiling segment (closed interval). The reachability conclusion (open half-plane $\rho_\Sigma \lt R_\Sigma/2$) is robust to either convention.
- **Pedagogical observation (not a defect):** The Itô-correction term $\tfrac{n}{2}\sigma_w^2$ in the dimension $n$ shows up across the cluster. A reader pursuing the Model-S no-go who has not internalized why this constant-in-$\delta$ term is the source of the obstruction (vs. the inward drift $-\alpha\lVert\delta\rVert^2$ which vanishes at the origin) might benefit from a sentence-level emphasis. Currently the segment names it correctly; this is just an "approachability-of-the-proof" observation, not a correctness one.

**Deferred-insufficient-substrate items:** None. All three claims have closed-form algebra that an independent agent can reproduce.

---

## §7 Substrate available for pre-print citation

The following statements are now adjudicator-CONFIRMED for cite-as-load-bearing in the pre-print:

1. **Corollary A.1S.1** (categorical containment dichotomy): $P(\tau_R \lt \infty) \in \{0, 1\}$, with the value selected by disturbance-model support structure (bounded vs additive-stochastic), and $\alpha$-invariant — correction strength cannot interpolate.

2. **The Model-S no-go signature** (`#deriv-stochastic-non-exit`): under additive stochastic forcing, no nonnegative supermartingale dominating $V$ certifies a horizon-independent $P(\tau_R \lt \infty) \lt 1$. The obstruction is structural (sign-indefiniteness of the natural compensated supermartingale on the persistence basin; equivalently, unbounded scale function ⇒ no non-constant bounded harmonic function for the additive-Brownian generator). Reusable as a diagnostic for any "stays-in-region-forever w.h.p." claim under additive non-degenerate forcing.

3. **The exact steady-state form** $\alpha_\Sigma^{\text{ss}} = (1-\lambda)/(2-\lambda)$ (Prop C.1) under discounted Beta-Bernoulli edge updates with exponential forgetting at rate $\lambda \in (0,1)$.

4. **The hard ceiling** (Prop C.2): $\sup_{\lambda} \alpha_\Sigma^{\text{ss}} = 1/2$; the schema's reachable persistence region under any $\lambda$ is exactly $\{\rho_\Sigma \lt R_\Sigma/2\}$. Above the ceiling, no exponential-forgetting design satisfies the schema's persistence prerequisite — a class-level no-go.

5. **The cascade** is sound: Prop B.1 ($\alpha = 1/(n+1)$) → Prop C.1 ($\alpha_\Sigma^{\text{ss}} = (1-\lambda)/(2-\lambda)$) → Prop C.2 (hard ceiling at $R_\Sigma/2$). Each step is verified independently; integration is clean.

Each of the four numbered substrate items is at the *exact* tier under stated conditions, in the framework's defeasible sense.
