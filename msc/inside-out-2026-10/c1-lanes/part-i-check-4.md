*KR C.1 — "Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier" — and C.2 — "Strengthenings C1–C3 … are independently checked, then landed or refuted" — item C1, with MAP D9. Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself."*

# Part I round 4: the independent check

This checks the landing merged at `387e71c0` (commits `22015b33`..`40e772d6`), read at `3d17de13`. Between `40e772d6` and `3d17de13` the only change to any file read here is an unrelated `NOTATION.md` row ($\pi_0$), so the checks bind to the landed text. The typed record is `reviews/part-i-round-4-check-1.md`. I wrote my own code for every number below and did not run the integrator's script; my script is at the end.

**Verdict.** The mathematics that landed holds: I worked the three-term threshold expansion by hand and confirmed it, and every number the round touched agrees with my own computation. The corrections to `#disc-constructive-impossibility-posture` hold as far as they go. The findings are about what the round left standing. The one that changes a decision is that `01-aat-core/OUTLINE.md` :332, the Appendices' Layer 0 paragraph, still states, on a reading surface, each of the claims the round found false. `item:findings-brief-overclaim-on-public-surfaces-map` (D9) was closed with that paragraph unchanged. Second, the integrator's claim that a sweep of all four volumes found no other gain-buys-time sentence does not hold: `#deriv-stochastic-non-exit` :56 has one.

## What I checked, and how

### The threshold expansion (C.2), by hand

With $m = n/2 = \kappa_R$, the series is $\tfrac12\sum_k c_k$ with $c_k = \tfrac1k e^{-L_k}$ and $L_k = \sum_{j \lt k}\log(1 + j/m)$. I expanded $L_k$ from the power sums myself: $-L_k = -\tfrac{k^2}{2m} + \tfrac{k}{2m} + \tfrac{k^3}{6m^2} - \tfrac{k^2}{4m^2} + \tfrac{k}{12m^2} - \tfrac{k^4}{12m^3} + \tfrac{k^3}{6m^3} + \tfrac{k^5}{20m^4} + \ldots$, which is the segment's $g_k$ and $r_k$, with the segment's $O(\cdot)$ absorbing the rest. The higher log-series terms give monomials $k^{p+1}/m^p$, $p \geq 4$, each dominated by $k^5/m^4$ on $k \leq m$.

Step 2's uniformity: on $k \leq K_0 = m^{3/5}$, $k^3/m^2 \leq m^{-1/5}$, $k^4/m^3 \leq m^{-3/5}$ and $k^5/m^4 \leq m^{-1}$, so $g_k$ and $r_k$ tend to zero uniformly. Write $a = k/m$, $b = k^3/m^2$, $c = k^2/m^2$, $d = k^4/m^3$. The error monomials $(p, q)$ are: from $r_k$'s $O(\cdot)$, $(1,2)$, $(3,3)$, $(5,4)$; from $\lvert g\rvert^3$, $a^3$ $(3,3)$, $a^2b$ $(5,4)$, $ab^2$ $(7,5)$, $b^3$ $(9,6)$; from $\lvert gr\rvert$, $ac$ $(3,3)$, $bc$ $(5,4)$, $ad$ $(5,4)$, $bd$ $(7,5)$; from $r^2$, $c^2$ $(4,4)$, $cd$ $(6,5)$, $d^2$ $(8,6)$. Every one has $p/2 - q \leq -\tfrac32$ and $p \geq 1$. For $p \geq 1$, $\sum_k \tfrac1k e^{-k^2/(2m)}k^p \leq \sum_k k^{p-1}e^{-k^2/(2m)} = O(m^{p/2})$, so each contributes $O(m^{-3/2})$. The bookkeeping is complete.

The cancellation: $\tfrac12 g_k^2 = \tfrac{k^2}{8m^2} + \tfrac{k^4}{12m^3} + \tfrac{k^6}{72m^4}$, and adding $r_k$'s $-\tfrac{k^2}{4m^2} - \tfrac{k^4}{12m^3}$ gives $-\tfrac{k^2}{8m^2} + \tfrac{k^6}{72m^4}$. Divided by $k$, the second-order sum is $-\tfrac{1}{8m^2}\sum k e^{-\varepsilon k^2} + \tfrac{1}{72m^4}\sum k^5e^{-\varepsilon k^2}$. With $\int_0^\infty k e^{-\varepsilon k^2}dk = 1/(2\varepsilon) = m$ and $\int_0^\infty k^5e^{-\varepsilon k^2}dk = 1/\varepsilon^3 = 8m^3$ (Euler–Maclaurin corrections $O(1)$, so $O(m^{-2})$ after the prefactors), it is $-\tfrac{1}{8m} + \tfrac{1}{9m} = -\tfrac{1}{72m}$.

The Mellin residues: with $\Gamma(s) = s^{-1} - \gamma_{\mathrm E} + \ldots$, $\zeta(1+2s) = (2s)^{-1} + \gamma_{\mathrm E} + \ldots$ and $\varepsilon^{-s} = 1 - s\ln\varepsilon + \ldots$, the $s^{-1}$ coefficient at the double pole is $-\tfrac12\ln\varepsilon + \tfrac12\gamma_{\mathrm E}$. At $s = -1$, $\operatorname{Res}\Gamma = -1$ and $\zeta(-1) = -\tfrac1{12}$, so the residue is $\varepsilon/12$. The line $\operatorname{Re}s = -\tfrac32$ meets no pole, since $\Gamma(-\tfrac32)$ is finite and $\zeta(-2) = 0$. The first-order sums are $\tfrac{1}{2m}(\tfrac12\sqrt{2\pi m} - \tfrac12) = \tfrac{\sqrt{2\pi}}{4\sqrt m} - \tfrac{1}{4m}$, by Poisson, and $\tfrac{1}{6m^2}\cdot\tfrac{\sqrt\pi}{4}(2m)^{3/2} = \tfrac{\sqrt{2\pi}}{12\sqrt m}$. Assembly: $\tfrac{1}{24} - \tfrac14 - \tfrac{1}{72} = -\tfrac{16}{72} = -\tfrac29$ per $m$, and $\tfrac{\sqrt{2\pi}}{4} + \tfrac{\sqrt{2\pi}}{12} = \tfrac{\sqrt{2\pi}}{3}$. Halving with $2m = n$ gives $\tfrac{\sqrt\pi}{3\sqrt n} - \tfrac{2}{9n}$. Step 1's tail bound holds: $\log(1+x) \geq x\log 2 \geq x/2$ on $[0, 1]$, the $K_0 \lt k \leq m$ terms sum to at most $m\,e^{-(m^{1/5} - 1)/4}$, and beyond $m$ the terms fall geometrically.

**On the tier**, which the integrator asked a checker to decide: "derived to three terms with the $O(n^{-3/2})$ remainder bounded" is honest. Each step's error is proved to be of that order, with constants that exist but are not written out. That is what $O(\cdot)$ means in a derived asymptotic, and the numerics fill in the constant ($\approx 0.151$). Writing the constants out would make the expansion usable as a bound at a given $n$. Nothing in canon uses it that way: the rigorous statements use the integral or the series, as the Lemma says. I would not change the wording.

### The numbers

My own log-space summation of the series and an independent quadrature of $\int_0^1 t^{n-1}(e^{\kappa(1-t^2)} - 1)/(1-t^2)\,dt$ (40 digits) agree to 10 digits at every threshold point. Threshold values for $n = 1, 2, 3, 5, 10, 20, 50, 100, 1000$: $0.5957, 0.6590, 0.7064, 0.7767, 0.8885, 1.0157, 1.2018, 1.3526, 1.889709$. Three terms at $n = 1000$: $1.889704$; at $n = 10$: $0.8846 \to 0.885$ against $0.8885 \to 0.889$. The residual after three terms, times $n^{3/2}$: $0.1249, 0.1422, 0.1482, 0.1501, 0.1507, 0.1509$ at $n = 10 \ldots 10^6$. A wrong $1/n$ coefficient would make this grow like $\sqrt n$; it converges. Margin values at $n = 3$: $0.7064, 1.574, 3.124, 11.98, 51.24$. The $\kappa_R$ increments that double $\alpha\Phi(0)$, by root-finding on the series: $1.012, 0.9548, 7.521, 1.945, 1.197$, so the $(3, 6)$ value $0.955$ is right.

### Prior sources

I read Grebenkov 2015 (arXiv:1411.3598) at eqs. (75)–(76). Eq. (75) is the Lemma's integral, under $D = \sigma_w^2/2$ and $L = R$. With $L^2/D = 2\kappa/\alpha$, (76), $\langle\tau\rangle \simeq L^2\Gamma(d/2)e^{\kappa}/(4D\kappa^{1+d/2})$, becomes $\Gamma(n/2)e^{\kappa_R}/(2\alpha\kappa_R^{n/2})$, the Lemma's small-noise form. It states no series, so canon's "neither … states the series form" holds for Grebenkov. **Graczyk & Jakubowski 2008 is still unread by anyone in the chain.** The HAL record has no file I could reach. The one recent paper I found that surveys OU exit from a ball (Guillaume, arXiv:2609.21685) describes Grebenkov's and Kersting's results and does not quote G&J. Canon's "probable prior form … not read" is the honest state.

### The other round-4 changes

- `#result-sector-condition-stability` :61 now says what the derivation's cap paragraph supports: the exponent is capped at $K$, the stay peaks below $K$ and falls past it, and only information, region or a slower world raises the bound.
- INTRODUCTION headline 1 states the guarantee per disturbance model, as `#result-persistence-condition`'s Brief does. Its "the simplest correctors can then be driven out by a worst-case disturbance" is the Brief's sentence and Lemma A.1N's class-level reading. One residual difference: the Brief also says that on a noisy channel the random-change condition is a window of gains, while the headline still says "below which". Headline 2 covers the channel for time but not for the condition. I record this as a remark, not a finding, because the headline's inequality, with $\rho$ read as total disturbance as `NOTATION.md` now glosses it, already contains the window.
- The posture's `depends:` addition and the `OUTLINE-accepted.md` row are the right fix rather than moving the segment. Four of the five new dependencies are Appendix segments, which `lint-outline` treats as backmatter. The one body-before-dependency case is `#der-causal-insufficiency-detection`, and it rests on the same introduced-before-used ground as `#disc-identifiability-floor`'s rows. `bin/lint-outline` reports 0 violations and 17 accepted.
- The posture's Brief claims for B, C, D and E, the seven-instance count, and F and G being `conditional` (on three premises and on (R1)–(R5)) all match their sources.
- `bin/refresh-all --check` says the generated outputs are current, and `md-press -q` is clean on every file the round touched.

## Findings

**F1 — the Appendices' Layer 0 still makes the corrected claims; D9's closure is premature.** `01-aat-core/OUTLINE.md` :332 (written in `5e621256`, the same day, before the round) reads: detecting an unobserved common cause "is impossible without loop-interventional access"; identifying the mixture "is impossible without observing the latent"; composite contraction "is impossible without matched-tier shared metrics"; and, for $K$ alternatives, "no update rule or forgetting rate keeps them calibrated", with "whatever the update rule" in its opening sentence. It also says "Five cleanly-fitting instances" and "names the unique broadly-available capability". These are, in "impossible without" form, the three false only-escape claims, the E over-claim and the instance count that round 4 corrected in the posture Brief. :112 describes the posture's second move as "name the escape (unique broadly-available framework machinery)", the wording the round replaced with "name the escapes". The front door says of the identifiability-floor pattern "the unique escapes interventional machinery supplies" (`README.md` :46, `README-auditor.md` :67, source `doc/readme/src/_position-and-lineage.md` :13). That is false for Instance 2, whose escapes are observability and joint observation, not intervention. D9 is titled "on public surfaces" and named only FINDINGS and CURRENT-VOL1. These copies were outside its list and inside its title. I have not edited them. My recommendation is to reopen the item or open a new one owned by C.1, also feeding A (the front door).

**F2 — a gain-buys-time sentence the sweep missed.** `#deriv-stochastic-non-exit` :56: "so the certain event can be made as late as a lifetime requires, at a margin cost logarithmic in that lifetime, though not by raising the gain past the Kalman gain on a fixed channel." This is round-3 F1's shape. It implies that gain up to $K$ buys the needed time, but on a fixed channel the stay is bounded over all gains and already falls between its maximizer and $K$. "As late as a lifetime requires" is true at fixed $\sigma_w$, or by information, region or a slower world, and not by gain on a fixed channel. The account and the integration record's C2 recheck say a four-volume sweep found no other such sentence. A grep for sentences that join "Kalman" with "stay", "exit" or $\kappa_R$ finds this one. The segment is a dependency of the posture segment. Supported form: "… not by gain on a fixed channel, where the reachable stay is bounded and peaks below the Kalman gain".

**F3 — the new Brief misstates Instance A's other routes.** The posture Brief now says the loop's covariance test "is the one that needs only machinery the theory already requires; the others need domain capabilities." `#der-causal-insufficiency-detection` :156: "Routes (a) and (b) have explicit AAT scaffolding …; routes (c)–(e) depend on domain capability." Route (a), $\varepsilon$-exploration under SA3, needs no domain capability. It gives partial detection. Supported form: "… the strong detector that needs only machinery the theory already requires; exploration alone gives partial detection, and the other three need domain capabilities." Small, but it is a false sentence written in the round.

**F4 — row C's apparatus cell keeps an only-claim.** "(CM2) / (CM2-M) and `#scope-composite-agent` elevated to *unique composition-contraction certificate* under matched structure." The source (`#disc-identifiability-floor` Instance 3, consequence 1) says "the unique broadly-available R0-regime certificate under the matched-Tier structural escape (b)". The row's own escape cell lists a passivity certificate and a common contraction metric as other certificates. Dropping "broadly-available" turns the defined sense into "the only one", which is the equation the round removed elsewhere in the segment. `impl-composition-machinery` :57 separately names composite interventional access as Instance 3's "unique broadly-available escape", while the floor segment gives that label to (CM2) for the certificate and to composite loop access for the game-structure identifier. One label covers two different things.

**F5 — the E over-claim survives in two places in the same segment.** Move 1 calls the evidence-allocation floor "a sharp supremum, over allocations and update rules". EA.2's supremum is over fixed allocations and the averaging class $\mathcal C$. Row E's apparatus cell says "past the ceiling no forgetting rate, exploration rate, or update rule helps". The source (`#deriv-evidence-allocation-ceiling` :80) says "no forgetting rate, exploration rate, or update rule *in $\mathcal C$*", and its :74 says drift-extrapolating estimators can lag less. The Brief was corrected and these two were not. The source segment's own summary at :15 ("so the update mechanism cannot remove it") and :88 ("the update rule does not change it") carry the same unscoped phrasing. Its Epistemic Status scopes it correctly.

**F6 — smaller residues in the posture segment (W-grade).**

- Impact and Related Work say "five independent audit cohort surfaces" and list six audits (471203, 472913, 266847, 361742, 526815, 584721). The integrated spike says "six audit surfaces".
- The Working Note "Dependency rationale" still describes `depends:` as the spine plus "the three boundary-or-boundary-dual derivations". After `7e6080d5` the list has eleven entries.
- Move 2 says the Model-S substitution is "distributional-and-instantaneous", while row D says "distributional-and-finite-time". Since Prop A.1S-τ, the substitute includes finite-time and expected-time statements, so "instantaneous" is wrong.
- The Epistemic Status counts "five on data inference (A–E)". D is a containment guarantee under noise, not an inference; the segment's own cluster list calls D and E analogs.
- The Working Notes use "Instance F" for the sector sub-scope $\alpha/\beta$ guard, a different object from the table's F (`#deriv-self-actuation-grounding`).

**F7 — confirmed: `#deriv-critical-mass-composition` :180 says "Four structural escapes are named there".** `#disc-identifiability-floor` Instance 3 lists five, (a)–(e). The integrator flagged it and left it for its own line.

**F8 — other restatements of the posture or floor as "the unique escape" (influx, outside the round).**

- `#disc-additive-coordinate-forcing` :96 says the identifiability floor names "the unique escape available".
- `#disc-anti-collapse` :16 says the posture "names the unique escape".
- `#disc-identifiability-floor` :36 and `#impl-strategy-dynamics` :26, :42 state the posture's move as "name the unique broadly-available escape". That is true in the defined sense, but it is the move-2 wording the posture itself replaced.
- `#form-consolidation-dynamics` :157 calls consolidation "the unique escape" of a candidate instance, with no derivation of uniqueness that I found.

Integration is replacement: when the posture's second move changed, these restatements became stale.

## For I.4

At `3d17de13`, `vsect read segment:disc-constructive-impossibility-posture` shows each of the integrator's six checks with the ↻ mark and "upstream changed, not read by this check". It names five segments (`#def-observation-function`, `#der-interaction-channel-classification`, `#hyp-communication-gain`, `#result-adversarial-tempo-advantage`, `#scope-adaptive-system`). None of them is a source the checks restate. They come in through the eleven-item `depends:` chain. `vsect take --help` says a declared `read:` set turns such changes into "upstream changed, not read" rather than a lapse, but the dashboard prints the glyph its legend gives for "lapsed". I did not work out which is meant. A reader of the dashboard will take these checks as lapsed. My checks carry their own `read:` lists.

## On the brief

The brief was right for this job. It named the KRs and the commits, left the account optional, and asked for a verdict without pre-answering one. I read the commit messages first and the account only after my own pass on the math and the posture. Its "what a checker should verify" list did not narrow what I looked at. F1 came from asking where else the posture's claims are restated, not from the list.

## Script

`python3`, mpmath, 40 digits. The series is summed in log space; the integral is a separate quadrature; the doubling increments come from `findroot` on the series.

```python
import mpmath as mp
mp.mp.dps = 40
def aPhi_series(kap, n):
    s = mp.mpf(0); k = 1; logt = mp.mpf(0); m = mp.mpf(n)/2
    while True:
        logt += mp.log(kap) - mp.log(m + k - 1)
        t = mp.e**logt / k; s += t
        if k > 10 and t < mp.mpf(10)**(-45)*s: break
        k += 1
    return s/2
def aPhi_int(kap, n):
    f = lambda t: t**(n-1)*mp.expm1(kap*(1-t**2))/(1-t**2) if t < 1 else t**(n-1)*kap
    return mp.quad(f, [0, 0.5, 0.9, 0.99, 1])
def three(n):
    return (mp.log(n)+mp.euler)/4 + mp.sqrt(mp.pi)/(3*mp.sqrt(n)) - mp.mpf(2)/(9*n)
for n in [1, 2, 3, 5, 10, 20, 50, 100, 1000]:
    print(n, aPhi_series(mp.mpf(n)/2, n), aPhi_int(mp.mpf(n)/2, n), three(n))
for e in range(1, 7):
    n = 10**e; a = aPhi_series(mp.mpf(n)/2, n)
    print(n, (a - three(n))*mp.mpf(n)**1.5)
print([aPhi_series(mp.mpf(1.5)+d, 3) for d in [0, 1, 2, 4, 6]])
for n, k in [(3, 2.5), (3, 6), (100, 52), (100, 80), (100, 120)]:
    g0 = aPhi_series(mp.mpf(k), n)
    print(n, k, mp.findroot(lambda d: aPhi_series(mp.mpf(k)+d, n) - 2*g0, 1.0))
```
