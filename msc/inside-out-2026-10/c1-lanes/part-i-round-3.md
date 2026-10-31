*KR C.1 — "Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier" — and C.2 — "Strengthenings C1–C3 … are independently checked, then landed or refuted" — item C1, with the round-2 check's findings. Top intent: "Complete 'in-place' refactor of ASF-- meta, all artifacts, and theory itself."*

# Part I, round 3: the round-2 check integrated, and the threshold drift derived

The landing is commit `6844f3c8` on main (segments, `FINDINGS.md`, vsect revisions; it was `b15e947d` before the rebase, the hash the typed record's checks cite, and each check is annotated in vsect with the rebased one), plus a second commit carrying this file, the typed record `reviews/part-i-round-3-integration.md` (taken into vsect: C1–C13), the new ledger item and one INTRODUCTION sentence the lead added mid-run. This file is for the mind that checks after me: what landed, what I re-derived, where I departed from the round-2 check, and how to check it without trusting me.

## What the inputs were

The round-2 check (`part-i-round-2-check.md`, `review:part-i-round-2-check-1`) re-derived the round-2 mathematics and found it sound. It found defects in the sentences that summarize it (D1–D5), in adjacent pre-existing text (P1–P6), and in wording (W1–W9). It also offered one strengthening: the leading term of the threshold drift. I read it whole, re-derived each item before acting on it, and wrote my own implementations of every number canon now quotes. The scripts are below. Two of the check's statements did not survive re-derivation as written (the "3.8×" mechanism and W3's scope), and one went further than the check did (the second asymptotic coefficient). These are under *Departures*.

## What landed

**`#deriv-sector-condition`.**

- *The strengthening (F8, C.2).* Lemma A.1S-τ.0 gains an exact series for the benchmark from the origin: $\alpha\Phi(0) = \tfrac12\sum_{k\geq1}\kappa_R^k/(k\,(n/2)_k) = (\kappa_R/n)\,{}_2F_2(1,1;2,\tfrac n2+1;\kappa_R)$. It comes from integrating the Lemma's own concavity identity and expanding termwise. It makes $\alpha\Phi(0)$ visibly a function of $(\kappa_R, n)$ alone, and it gives any checker a one-line recompute. From the series, "drifting upward like $\tfrac14\ln n + 0.15$ … a computed trend, not a derived asymptotic" is replaced by the derived two-term expansion $\tfrac14(\ln n + \gamma_{\mathrm E}) + \sqrt\pi/(3\sqrt n) + O(n^{-1})$. The derivation is in the Lemma: the product form of the terms, a Mellin residue for the Gaussian log-sum and Euler–Maclaurin for the correction. Tier: the series is exact. The two-term expansion is derived. That the remainder is $O(n^{-1})$ is the order of the neglected terms, and the numerics confirm it to $n = 10^6$; it is not proved. The Findings, Summary table, What-is-derived table and Epistemic Status say so.
- *Gain and time (D1/F1).* On a fixed channel the stay that tuning the gain can buy is bounded, peaks strictly below $K$ and falls monotonically past it. Every sentence that credited gain with time "up to the Kalman gain" is replaced: the summary, Cor A.1S.1, the cap paragraph, Discussion "Kind of guarantee", and the second Findings Result, Brief and Impact. The cap paragraph now gives the maximizer table, the checker's remark that $\kappa_R$ peaking at $K$ is the steady-state variance being smallest there, and the three things that do raise the cap: information, a larger certified region, or a slower environment.
- *D2/F2.* "Doubling costs about $\log 2$" now holds only for $\kappa_R \gg n/2$, and the exact increments near threshold are given. I did not carry the leading-order formula $\ln 2/(1 - n/(2\kappa_R))$, because near threshold at large $n$ it is itself wrong (18.0 against the exact 7.5 at $(100, 52)$).
- *D3/F3.* The dip instance is stated with its parameters. Its mean exit time is now exact, $3.57$, from the radial Andronov–Vitt–Pontryagin formula with its own drift, not a Monte Carlo number. That is $3.9$ times its floor benchmark and near the bulk-gain benchmark $3.80$.
- *D4/F4, W1, W2.* "At fixed disturbance" qualifiers are on the opening and the Brief. The killed moment is described as counted on paths still inside, not conditional on being inside, in four places across three segments. Markov on the unstopped moment is named as what is unavailable under a local sector condition.
- *W3 and (iv).* The Lemma's sentence on where the asymptotic errs, and (iv)'s "anti-conservative exactly near the threshold", are rewritten against computed ratios (*Departures*).
- *D5/F5.* I read Ikeda & Watanabe 1977 Thm 1.1 and Remark 1.1, Kersting et al. 2023 Thm 4, and Grebenkov 2015 eqs. (75)–(77) at the primary, against canon's transcription. All agree, and the "not read at the primary" sentences are replaced with what was read. A Search Log line records the reads. Day 1983 and the heavy-tail sources are still unread by anyone in the chain.
- *F6.* The GA-2S convention in Discussion. The `\Vertw` render bug at three sites, plus one more in `#deriv-matrix-persistence-condition`'s Working Notes.
- *F7.* The Working Note's ideation is restated at the narrowed strength: certificate loss is certain, and model-class change is open. "(iii′)" and "Three-Deaths" are gone, and the note points at `#def-death-as-factor-loss`'s continuity death.
- *The diff-voice item, this segment's half.* The Prop A.1S-τ Findings Impact no longer narrates "Replaces the stopped-moment bound that the earlier Prop A.1S(i) carried". It states the present truth: under a local sector condition the moment that decays is the killed one. The `#scope-observation-ambiguity-modulation` half is Part II's, so `item:diff-voice-in-present-truth-surfaces-scope-obser` stays open.

**`#result-persistence-condition`.** W1 at :17 and :43. W6: $\alpha = \mathcal T$ holds at the optimal gain, and a mis-tuned linear corrector has $\alpha \neq \mathcal T$. D1 at :98 and :130. W9: the Findings Brief no longer says the system "loses bounded behavior". It now says what the guarantee is under each disturbance model, with the Model S one stated as a typical size and a stay, not containment. Below threshold the guarantee is lost, and the simplest correctors can be pushed out by a worst-case disturbance. Under random channel noise the condition is a window. This Brief changed again in a third commit, after the advisor read it against Cor A.1S.1.

**`01-aat-core/INTRODUCTION.md`.** Headline 2 no longer says correction strength pushes exit "past any lifetime … up to the Kalman gain". Margin buys the time. Stronger correction supplies the margin against noise that does not grow with it, and on a fixed channel the reachable stay is bounded and peaks below $K$. Headline 1's "loses bounded behavior" is the same defect as the Brief, and I fixed it the same way. The round-2 integrator had assigned it to A.2. A.2 still owns the traceability of the headline list; I fixed the clause because nobody is on INTRODUCTION and a known-false clause should not wait for a rewrite. :50, at the lead's request mid-run: "its standard objective is recoverable here as a special case under three explicit restrictions" had no support in canon. `#disc-ciy-unified-objective` states a shared value-and-information shape, not shared content, and names two differences. The sentence now says exactly that, matching the lead's wording in 7b8ae8c6. The strengthening is `item:influx-active-inference-four-strengths` (C.4).

**`#impl-persistence-and-limits`.** D1 at :33 and in the misquotation row. "Its expected time is now known" became "has an explicit lower bound", since "now" was diff-voice.

**`#result-contraction-template` (P1/F9/C17).** The Itô constant is stated as $\sigma_\xi^2\operatorname{tr}(M + \ldots) \leq c_{\text{Itô}}\,n\sigma_\xi^2m_2$, with $c_{\text{Itô}} = 1$ at constant $M$. (CT-S-persist) is corrected from $m_2^2/m_1$ to $m_2/m_1$ and noted as invariant under rescaling the metric. CT3 uses the per-coordinate convention. Nothing downstream cites the old form; I grepped all four volumes and `NOTATION.md`.

**`#hyp-mismatch-dynamics` (P3/F10).** $\rho$ is read as total at :14, :16 and :38, and the Model D steady state is spelled out as lag plus floor.

**`#deriv-stochastic-non-exit` (P6/F12/C16).** The Monte Carlo table, which discrete monitoring biased low, is replaced by exact values from a spectral solve, with $\kappa_R$ and $\Phi(0)$ columns. The text says how they were computed.

**`#detail-operationalization` (P4/F11).** The question was whether this belonged to this round or a new item. I did both, on the merits. The false sentence ("mismatch magnitude is directly measurable from prediction-versus-observation residuals") and the false readings of what the recipes estimate could not stand while a fix waited; integration-is-replacement applies to the false claim even when the true one is owed. So the summary, the two Measurement Targets rows and a new paragraph now say three things. The recipes read the innovation, so they estimate properties of the innovation sequence, not the error's disturbance; for a well-tuned filter the innovation is white. They estimate $\rho$ and $\sigma_w$ as defined only for a noiseless channel, and the $\alpha$ and $R$ recipes share the dependence. And two general relations give the sound route: the mean-square identity, and the total disturbance computed from its primitives. Designing and verifying estimators from innovation data is new work, needing simulation against known parameters, and it feeds E.2. It is `item:write-innovation-based-estimators-for-detail-ope`, owner C.1 with E.2. The item names Mehra 1970's innovation-correlation method as a lead to read at the primary. I have not read it, so canon does not cite it.

**Smaller.** `#def-mismatch-signal` (W8): term (ii) for a linear-Gaussian model is $\operatorname{tr}(HP^-H^T)$, the predictive error, not the posterior $P$; "never to zero" became the decomposition's own condition. `#der-deliberation-cost` (W7): the threshold uses the realized error and equals the uncertainty-ratio gain only in expectation. `#result-sector-persistence-template` (W1). `01-aat-core/OUTLINE.md` caption (W5): for the tight corrector a worst-case drift defeats it; ordinary snowfall is not worst-case.

**Not edited, routed.** `#example-kalman` (F14/W4) is held by the A.1 round-5 integrator. I sent the lead two sentences: the continuous-time result applied to a discrete filter, and the feasibility citation that is really its discrete analog. The lead passed them on, and the finding stays open until that lane lands it.

## What I re-derived

All of C1–C13 in the typed record, by hand and with my own scripts: the series and its agreement with the Lemma's integral and with Kersting's (17); the two-term threshold asymptotic; the gain maximizers and the derivative at $K$; the doubling increments; the dip instance exactly; the asymptotic-over-exact ratios across $n$; the three primaries; CT-S from $V = \xi^TM\xi$ with the scale test; the non-exit table; the innovation identity and the total-disturbance algebra; the Kalman predictive floor; the deliberation threshold. Every number in the round-2 check that I used reproduced to its printed digits, apart from the corrections below.

## Departures from the round-2 check

- **The 3.8× (D3).** The check attributed the instance's number to the bulk-gain benchmark $\Phi_5(0) = 3.80$. Canon's "3.8×" was in fact the ratio to the floor benchmark $\Phi_2(0) = 0.92$, as the spike's column header says, and the two coincide by accident. The check's conclusion stands: wrong corrector named, no parameters. The exact value $3.57$ replaces the Monte Carlo, which gave $3.519 \pm 0.061$; the exact value is within one standard error of it.
- **W3 is wider than the check said.** The check gave an under-estimate at $(100, 40)$ against "over-estimates below threshold". Computed across $n$: at $\kappa_R = n/4$ the asymptotic over-estimates for every $n$ from 1 to 1000. At the threshold it over-estimates for $n \leq 5$ ($3.5$-fold at $n = 1$) and under-estimates beyond ($0.13$ at $n = 100$, $0.03$ at $n = 1000$). At large $n$ it is off by about a factor of two even at $\kappa_R = n$. So (iv)'s "anti-conservative exactly near the mean-square threshold" was right only for small $n$, and canon now says where.
- **F8's second coefficient is derived, not numerical.** The check left "about $0.59$, whether $\sqrt\pi/3$ I have not checked". The series gives it by a two-line expansion, and the numerics agree to four digits at $n = 10^6$. My route to the leading constant (Mellin on the series) is independent of the check's (Frullani on the integral). The remainder order is still numerical. The advisor I consulted suggested landing $\sqrt\pi/3$ only as an observed match. I landed it as derived because the expansion is written out in the segment and the next checker can test it directly. If that mind finds the expansion step unjustified, the right repair is to the derivation's error control, not to the coefficient.
- **The doubling formula.** The check's leading-order cost $\ln 2/(1 - n/(2\kappa_R))$ was not carried, for the reason above.

## Influx touched

The lead asked me to name any source that already raised something I touched, so a drain can mark it disposed.

- `influx-scout/MAP.md` D14 and `rewrites.md` §2.7 flag root-segment label disagreements, including `#def-mismatch-signal` being `axiomatic` but "definitional". I edited that segment for W8 only and left the label.
- D6 (aat-refactored's finite-horizon sufficiency and the sandwich lemma: the fitness trigger fires for every bounded agent) concerns `#def-model-sufficiency` and `#def-model-class-fitness`. It does not reach the trigger this round touches: the region-exit certificate of Prop A.1 / Cor A.1S.1 and its hand-off to `#sketch-structural-adaptation-genericity`. I made no change on D6's account. A reader joining the two should note that canon has two "structural-adaptation triggers": the certificate-loss one here and the fitness one D6 breaks.
- D7 lies outside this round's segments.
- D9: on the lead's message, I did not take `#disc-constructive-impossibility-posture`. Its Findings Brief makes five "only escape" claims, each to be checked against its derivation. That is a separate read from this round, and a checker of this round should not have to carry it. I am willing to take it as the next piece, from the drain's C.1 item, if the lead wants.
- No other edit here was raised by an influx source as far as I found. I checked `rewrites.md` §2 headings and §2.7's items against my segment list.

## What a checker who did not write this should verify

1. Re-derive the series from the concavity identity and recompute $\alpha\Phi(0)$ at two or three $(\kappa_R, n)$ against the Lemma's integral. Then work the threshold expansion without reading mine: the product $\prod_{j\lt k}(1 + j/m)^{-1}$ expanded to order $m^{-1/2}$ at $k \sim \sqrt m$, the Gaussian log-sum, and the tail bound for $k \gt m^{2/3}$. Decide whether "derived to two terms" is the honest tier.
2. Read every sentence I changed about gain and time (grep "Kalman gain" in `#deriv-sector-condition`, `#result-persistence-condition`, `#impl-persistence-and-limits`, INTRODUCTION headline 2). Ask whether any still credits gain on a fixed channel with time it cannot buy, or now under-credits gain at fixed noise.
3. Recompute the gain maximizers and the doubling increments ($n = 1, 3, 100$).
4. Check CT-S in `#result-contraction-template` from $V = \xi^TM\xi$, including that (CT-S-persist) reduces to $\kappa_R \gt n/2$ at $M = I$. The CT2 ray-integration step with state-dependent $M$ is still unexamined; the round-2 checker flagged it as loose.
5. Read the new paragraph in `#detail-operationalization`. Is the line between what the recipes estimate and what they are stated for drawn truthfully, and is the deferral to the item honest rather than a softening?
6. Read INTRODUCTION headlines 1 and 2 and :50 against the bodies they name.
7. Spot-check one primary read (Kersting (17) is the quickest: arXiv:2208.04029, p. 6).
8. Open findings from `review:part-i-round-2-check-1` that this landing answers, each for a mind other than its author to confirm: F1–F13, F15, F16, C16/finding, C17/finding. Also `review:part-i-round-2-integration#F2` in part (Day 1983 and the heavy-tail sources are still unread, so it cannot close whole), `review:part-i-mismatch-lineage-check-1#C11/finding` and F3 (the $\rho$ readings in `#hyp-mismatch-dynamics`), and `question:the-front-door-sentences-say-gain-buys-time-only`. F14 waits on `#example-kalman`. The lapsed checks on the revised segments are a second mind's to confirm. I classified my revisions as `redefined`, except `#result-sector-persistence-template` and `#deriv-matrix-persistence-condition`, which are `reworded`.

`CURRENT-VOL1*.md` was not rebuilt. `FINDINGS.md` was regenerated by `bin/refresh-all` in `6844f3c8`; the README outputs regenerated unchanged.

## Scripts

All run with `python3 -I` and need numpy, scipy and mpmath. The output that canon quotes is in the typed record's recheck lines.

```python
# a.py — the series against the Lemma's integral; the threshold asymptotic
from mpmath import mp, mpf, quad, gammainc, exp, hyp2f2, euler, log, sqrt, pi
mp.dps = 30
def aPhi0_int(k, n):   # Lemma: Phi(0)=(2/s^2) int_0^R G/m; alpha = s = 1, R = sqrt(k)
    R = sqrt(mpf(k)); nn = mpf(n)
    G = lambda u: mpf(1)/2*gammainc(nn/2, 0, u*u)
    f = lambda u: 0 if u == 0 else G(u)/(u**(nn-1)*exp(-u*u))
    return 2*quad(f, [0, R/2, R])
def aPhi0_hyp(k, n):
    return mpf(k)/n*hyp2f2(1, 1, 2, mpf(n)/2+1, k)
for n, k in [(1, .5), (2, 4), (3, 1.5), (3, 6), (10, 5), (20, 40), (100, 50)]:
    print("check", n, k, mp.nstr(aPhi0_int(k, n), 12), mp.nstr(aPhi0_hyp(k, n), 12))
for n in [1, 2, 3, 5, 10, 20, 50, 100, 1000, 10**4, 10**5, 10**6]:
    v = aPhi0_hyp(mpf(n)/2, n)
    a0 = (log(n)+euler)/4; a1 = sqrt(pi)/(3*sqrt(n))
    print(n, mp.nstr(v, 8), "res0*sqrt n", mp.nstr((v-a0)*sqrt(n), 6), "res1*n", mp.nstr((v-a0-a1)*n, 6))
```

```python
# b.py — gain maximizer, doubling cost, the non-exit table by spectral solve
import numpy as np
from mpmath import mp, mpf, hyp2f2, findroot
from scipy.optimize import minimize_scalar
from scipy.linalg import eigh_tridiagonal
mp.dps = 20
def aPhi0(k, n): return float(mpf(k)/n*hyp2f2(1, 1, 2, mpf(n)/2+1, k))
se, sn = 1.0, 0.5; K = se/sn
for n in [1, 3]:
    for R in [1.0, 1.5, 2.0, 3.0]:
        kap = lambda a: a*R*R/(se**2 + a*a*sn**2)
        r = minimize_scalar(lambda a: -aPhi0(kap(a), n)/a, bounds=(1e-3*K, 1.5*K), method='bounded', options={'xatol': 1e-7})
        print(n, R, kap(K), r.x/K, -r.fun, aPhi0(kap(K), n)/K)
R = 1.0; kap = lambda a: a*R*R/(se**2 + a*a*sn**2); P = lambda a: aPhi0(kap(a), 1)/a; h = 1e-5
print((P(K+h)-P(K-h))/(2*h), -P(K)/K)
for n, ks in [(3, [2.5, 6, 12]), (100, [52, 60, 80, 120])]:
    for k in ks:
        t = 2*aPhi0(k, n)
        x = float(findroot(lambda x: mpf(x)/n*hyp2f2(1, 1, 2, mpf(n)/2+1, x) - t, k+1.0))
        print(n, k, x-k)
def survival(a, s, R, Ts, N=4000):
    x = np.linspace(-R, R, N+2); hx = x[1]-x[0]; xi = x[1:-1]
    w = lambda y: np.exp(-a*y*y/s/s)
    wm, wp, wc = w(xi - hx/2), w(xi + hx/2), w(xi)
    c = (s*s/2)/hx**2
    lam, V = eigh_tridiagonal(-c*(wp+wm)/wc, c*wp[:-1]/np.sqrt(wc[:-1]*wc[1:]))
    d = np.sqrt(wc); coef = V.T @ d; j0 = np.argmin(np.abs(xi))
    return [1 - (V @ (np.exp(lam*T)*coef) / d)[j0] for T in Ts], -lam.max()
for a, s, R in [(1.0, 0.3, 1.0), (0.5, 0.2, 0.8), (1.0, 0.5, 1.0)]:
    ex, l1 = survival(a, s, R, [50, 200, 800, 3200]); Phi0 = aPhi0(a*R*R/s/s, 1)/a
    print(a, s, R, Phi0, 1/l1, [round(v, 3) for v in ex], [round(1-np.exp(-T/Phi0), 3) for T in [50, 200, 800, 3200]])
```

```python
# c.py — Gaussian log-sum; asymptotic/exact ratios; Kersting eq. (17)
from mpmath import mp, mpf, nsum, exp, log, euler, hyp2f2, gamma, inf, quad
mp.dps = 30
for eps in [mpf('1e-2'), mpf('1e-3'), mpf('1e-4')]:
    s = nsum(lambda k: exp(-k*k*eps)/k, [1, inf]); print(eps, s - (-log(eps)/2 + euler/2))
a = lambda k, n: mpf(k)/n*hyp2f2(1, 1, 2, mpf(n)/2+1, k)
s = lambda k, n: gamma(mpf(n)/2)/2*mpf(k)**(-mpf(n)/2)*exp(k)
for n in [1, 2, 3, 5, 10, 20, 50, 100, 1000]:
    print(n, [mp.nstr(s(k, n)/a(k, n), 3) for k in [n/4, n/2, n/2+2, n/2+5, n]])
for d, L in [(2, 2), (5, 3)]:   # theta = sigma = 1, so lambda = 1
    v = 2*quad(lambda z: z**(1-d)*exp(z*z)*quad(lambda t: t**(d-1)*exp(-t*t), [0, z]) if z > 0 else 0, [0, L])
    print(d, L, v, a(L*L, d))
```

```python
# d.py — exact mean exit time from the origin for a radial corrector F = g(r) delta
import numpy as np
from scipy.integrate import quad
def Phi0(g, n, s, R, brk):
    U = lambda u: quad(lambda r: g(r)*r, 0, u, points=[b for b in brk if b < u] or None, limit=400)[0]
    m = lambda u: u**(n-1)*np.exp(-2*U(u)/s/s)
    Gm = lambda u: quad(m, 0, u, points=[b for b in brk if b < u] or None, limit=400)[0]
    return 2/s/s*quad(lambda u: Gm(u)/m(u) if u > 0 else 0, 0, R, points=brk or None, limit=400)[0]
dip = lambda r: 2.0 if 0.485 <= r <= 0.515 else 5.0
print(Phi0(dip, 2, 1.0, 1.0, [0.485, 0.515]), Phi0(lambda r: 2.0, 2, 1.0, 1.0, []), Phi0(lambda r: 5.0, 2, 1.0, 1.0, []))
```
