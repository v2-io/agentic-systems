*KR C.1 — "Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier" — and C.2 — "Strengthenings C1–C3 … are independently checked, then landed or refuted" — item C1 (expected exit time under Model S), with owner-review item A3 and the round-2 findings on A7. Top intent: "Complete 'in-place' refactor of ASF-- meta, all artifacts, and theory itself."*

# Part I, round 2: the exit time lands, the stopped bound goes, the Model S condition becomes a window

The landing is commit `a728475f` on branch `worktree-agent-a8c84d68550584c49`; its body lists every file and claim touched. My re-derivations are typed in `reviews/part-i-round-2-integration.md` (taken into vsect). This file is for the mind that checks after me: what landed, what I re-derived, what I declined, and how to check it without trusting me.

## What the inputs were, and what re-derivation found

Three bodies of checked work met on the same Part I segments: the A7/A10 landing (the persistence state is the estimation error; its disturbance carries gain-injected channel noise), its independent check (the Model S condition is a window in the gain; Model D has no optimum; fourteen findings), and the C1 exit-time spike with its de novo feedback (Prop A.1S(i) false under (ii); the spike's result replaces it; two corollaries wrong; the exponent capped at the Kalman gain). I read all of them whole and re-derived each claim I landed. Every one of the checkers' central claims survived re-derivation. Two of their phrasings did not, and canon carries the corrected form:

- "Tenure is capped at the Kalman gain" is true of the *exponent* $\kappa_R(\alpha) = \alpha R^2/(\sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2)$, which peaks at $K$. The expected stay itself, $\Phi(0) = g(\kappa_R)/\alpha$, is maximized strictly *below* $K$ (its log-derivative at $K$ is $-1/K$); what is exact is that past $K$ it falls monotonically. At $n = 1$, $\sigma_{\text{env}} = 1$, $\sigma_\nu = 0.5$, $R = 1$: $\Phi(0) = 1.07$ at $0.5K$ against $0.72$ at $K$.
- The spike's Corollary 4, "an agent that satisfies the condition with no margin typically leaves within one correction time," is about the benchmark; the licensed statement is about the guarantee (the condition certifies no more than about one correction time of stay). The verifier said so, and canon says it that way. The threshold values drift like $\tfrac14\ln n$ (0.60 at $n = 1$, 1.89 at $n = 1000$), so "order one in every dimension" is replaced by the computed trend.

## What landed

**`#deriv-sector-condition`.** Prop A.1S is restated: (i) is the *killed* second-moment bound $\mathbb E[\lVert\delta_t\rVert^2;\ \tau_R \gt t]$; (ii) certifies the scale while certified and, via the new proposition, about one correction time of stay at threshold; (iii) is the stationary tail under a *global* sector condition and the composed region-aware tail under a local one; (iv) stays, derived from the exact stopped identity without the decay term. Hypothesis (S) (measurable, locally bounded $F$; a weak solution) is stated. The false stopped-with-decay bound is named false, with the three-line argument and the Monte Carlo, and a regression guard in Working Notes replaces both the "(iii′)/(iv)/dichotomy provenance" note and the off-ramp "RESOLVED — do not re-open" bullet. New **Prop A.1S-τ** carries Lemma A.1S-τ.0 (the OU benchmark in closed form, its small-noise asymptotic, the threshold table), the mean comparison with equality under radial tightness, stochastic domination (self-contained proof; Ikeda–Watanabe cited as the published route, marked not read at the primary), the lifetime bound (shown tighter than (iv) from every start), the tenure-indexed condition with a rigorous elementary form (the asymptotic form named as an asymptotic only, with the counterexample), what (ii) certifies, the Kalman-gain cap, and the scope lines. The spike's Corollary 2.1 is not carried (its moment sentence is false; Theorem 2 covers the moments). A second Findings entry and footnotes for Kersting, Grebenkov and Ikeda–Watanabe are added. The "structural adaptation is generic" clause is narrowed to "loss of the parametric certificate is generic; whether it forces model-class change is `#sketch-structural-adaptation-genericity`'s open question" in every restatement (summary, Cor A.1S.1, Discussion, Findings Brief and Impact), and likewise in `#deriv-stochastic-non-exit` and `#impl-persistence-and-limits`.

**Convention.** $\sigma_w$ is the per-coordinate intensity of the *total* disturbance, so $\mathbb E\lVert w\rVert^2 = n\sigma_w^2$ per unit time and every Model S formula in canon reads as written. Landed in `NOTATION.md` (GA-2S; the $\rho$ and $w$ rows), the Prop A.1S statement, and `#result-sector-condition-stability` (its WN ambiguity bullet deleted as finished). The exit exponent is registered as $\kappa_R$, distinct from $\kappa_{\text{processing}}$ and $\kappa(P^-)$.

**`#result-persistence-condition`.** The Model S condition is stated as a window $\alpha \in (\alpha_-, \alpha_+)$, feasible iff the Kalman error fits inside the region, geometric about $K$, with the Model D form $\alpha(R - \bar\nu) \gt \rho_{\text{env}}$ and its new necessary condition $R \gt \bar\nu$. "Two levers in $\mathcal T$" is retitled "Gain and information are different levers": $\mathcal T$ is defined at the optimal gain, so a gain past it is miscalibration moving $\alpha$, not $\mathcal T$; the Model D picture (bound monotone toward $\bar\nu$; event rate does nothing to the worst case) is stated as different; the Lipschitz ground is replaced by B.3's gain-scaling of the injected fluctuation; `#obs-gated-tempo-advantage` is credited as the in-canon anticipation. One reading per symbol: $\rho$, $\sigma_w$ are total throughout and the environmental part is the lag term. The linear operational form with bounded channel noise, "Mismatch is ultimately bounded" → "the estimation error", the Findings Impact and Novelty Claim updated.

**One reading per symbol elsewhere.** `#hyp-mismatch-dynamics` reads $\rho$ as total with the lag term named. `#deriv-persistence-cost` renames its signal diffusion $\sigma_w \to \sigma_{\text{env}}$ and channel noise $\sigma_o \to \sigma_\nu$ (25 and 14 sites), states the contraction $\lambda_s + K$, and replaces "the price follows from the error that gain achieves" with the Duncan argument: every linear filter on the channel takes in $nK/2$; the floor at a mis-tuned filter's error is slack. Quoting lines in `#impl-persistence-and-limits`, `#def-death-as-factor-loss` (the $n\alpha/2$ floor now in its general form, twice) and `#result-persistence-condition` follow.

**The rest of the drain.** `#result-contraction-template` CT-S → killed moment, the stopped form named false, exit-time comparison not transferred to weighted metrics; `#result-sector-persistence-template` §"On Prop A.1S region-awareness"; `#result-sector-condition-stability` §"Two kinds of guarantee" (now three: scale, tail, time); `#deriv-stochastic-non-exit` (:14, :34, :44 "well inside" → $P(\chi^2_n \lt n) \in (0.5, 0.69)$, :52, :56, the table column label, the Findings Impact, the WN provenance → regression guard); `#def-mismatch-signal` (a correction drives the error to the state-and-law floor, not zero; the "mismatch" convention stated as adopted); `#result-mismatch-decomposition` (term (i) renamed "excess over the Bayes predictor"; estimation error is (i)+(ii)); `#deriv-gain-sector` B.3 (state-dependent injected noise for nonlinear $g$); `#der-deliberation-cost` (a derived paragraph: the benefit term is about the estimation error and improvement toward the optimal gain; one-step derivation); `#example-kalman` (steady-state tempo $1.95\ \text{s}^{-1}$ beside the transient $3.315$; low-mode steady state; Mapping row; Model S structural trigger $R^2 \lt P^-$; deliberation reads the estimation error; the Kalman-gain remark); `#result-adversarial-tempo-advantage` (scope condition for the $3/2$ law under self-injected noise) and `#result-adversarial-exponent-regimes` (pointer); `#scope-evolving-software` (:37, the channel floor); `#der-multi-timescale-stability`, `#disc-constructive-impossibility-posture`, `#sketch-structural-adaptation-genericity`, `#der-gain-sector-bridge` (pointers); `01-aat-core/OUTLINE.md` (two rows). `01-aat-core/INTRODUCTION.md` headline 2 is rewritten as "Containment Dichotomy, with a clock," with slugs (A3; the lead confirmed this sentence is this lane's), and the `01-aat-core/OUTLINE.md:13` figure caption no longer states the agent-level iff that Lemma A.1N refutes (A3's third part). `#impl-orient-cascade` :58 and the OUTLINE row for `#deriv-persistence-cost` follow the $\sigma_{\text{env}}$ rename. The spike's README records what landed and what was not carried.

## What I re-derived

Everything in `reviews/part-i-round-2-integration.md` C1–C13, by hand and, where a number is quoted in canon, by the scripts below: the killed bound and the falsity of the stopped one (own exact-discretization Monte Carlo); Theorem (i) and (ii) step by step; the Lemma's integral and the threshold table (own mpmath implementation; matches the spike and the verifier to four digits); the Corollary 5 counterexample; the elementary tenure bound (derivation and ratios, all below one and tending to one); concavity of $\Phi$ in $r^2$ and the domination of (iv); the window algebra against a grid; the exponent cap and the tenure maximizer; the Duncan intake argument; the one-step deliberation derivation; the example's Riccati numbers; the adversarial scope algebra.

## Declined, narrowed, or left open, and why

- **Adversarial regimes under $\sigma_w(\alpha)$** (`question:model-s-total-disturbance-downstream`, narrowed, not closed). I landed the condition the fixed-$\sigma$ derivation needs (coupling noise dominates each agent's self-injected noise) and the observation that it fails for a gain-raised tempo ratio above about $\gamma_B/\sigma_{\nu,A}$. The full regime map, and whether pushing a target's gain out of its window from above is its own regime, are not derived. The per-dimension, matrix-Loewner and discrete Model S results are exact at fixed disturbance; their reading changes and they are not re-derived.
- **Ikeda–Watanabe 1977, Kersting 2023, Grebenkov 2015, Day 1983, heavy-tail sources**: not read at the primary by anyone in the chain (Project Euclid and relata did not return the Ikeda–Watanabe text); each is marked so in canon, and nothing rests on the unread one because the self-contained proof is the basis.
- **Anisotropic noise**: the verifier's time-change sketch is noted as not landed; it wants its own verifier.
- **The $\bar\delta$ symbol sweep** (`question:persistence-family-delta-symbol`): untouched, as the lane before me chose; each Setup declares its $\delta$.
- **Robust-control primary check** (`question:robust-control-lineage-primary-check`): not mine; untouched.
- **`#def-mood`**: not traced to either mismatch object; the lane before me flagged it and so do I.
- **The front door's headline 1** (":26 one inequality and not an analogy among three"): A3's other half; it is A.2's and I left it.

Two questions are answered in vsect: `example-kalman-structural-adaptation-model-d` (the Model S trigger is feasibility: $R^2 \lt P^-$ means no gain persists), and `model-s-total-disturbance-downstream` is answered with the narrowing above and left reopenable.

## Open findings this landing answers

A finding closes in vsect only when a mind other than its author confirms it answered, so these stay open until you do. From `review:c1-exit-time-verify-1`: C1/finding (Prop A.1S(i) false under (ii)). From `review:part-i-mismatch-lineage-check-1`: C2/finding and F2 (Model D qualifier), C5/finding and F7 (persistence-cost intake), C11/finding and F3 (one reading per symbol), F1 (the window), F4 (term (i)), F5 (`#def-mismatch-signal`), F6 (levers; Lipschitz), F8 ($n\alpha/2$ restatements), F9 (the ghost), F10 (`#obs-gated-tempo-advantage`), F11 (B.3), F12 (`#der-deliberation-cost`), F13 (`#scope-evolving-software`), F14 (`#example-kalman`). Also the coordinator's question on CT-S (43cbc693) and `question:example-kalman-structural-adaptation-model-d` (answered). The lapsed checks of `review:part-i-mismatch-lineage-check-1` and `-integration` on the edited segments lapsed because the text changed; `vsect confirm` on each is the second mind's call, not mine.

## What a checker who did not write this should verify

1. Re-derive Prop A.1S(i) from Itô on $e^{2\alpha s}V$ and confirm that the stopped moment cannot be bounded this way: run `recheck.py` §5 or the verifier's Euler script, or argue it from Cor A.1S.1 in three lines. Then read every sentence of the new Prop A.1S against its neighbours (Cor A.1S.1, the Summary table, Epistemic Status, Discussion, Findings) for a surviving "stopped bound" reading.
2. Re-derive Theorem (ii)'s radial comparison without reading mine, in particular the touching case at exit and the polarity step for $n \geq 2$. If you can read Ikeda–Watanabe 1977 Thm 1.1 at the primary, say whether the squared-radius application is as the scan transcribed it.
3. Re-derive the elementary tenure bound (Prop A.1S-τ(iv)) and the claim that it is below $\Phi(0)$ for all $s \in (0, \kappa_R)$; `recheck.py` §3.
4. Check the exponent-cap paragraph: that $\Phi(0) = g(\kappa_R, n)/\alpha$ with $g$ increasing (scale $u = Rv$), that the tenure maximizer is below $K$, and that canon nowhere says tenure is *maximized* at $K$.
5. Read the window paragraph in `#result-persistence-condition` and `recheck.py` §4; then read "Gain and information are different levers" and ask whether the Model D sentences say only what the tight bound $\rho_{\text{env}}/\alpha + \bar\nu$ supports.
6. Check the Duncan argument in `#deriv-persistence-cost`: that the filter equation is invertible in the observation path for every $\alpha \gt 0$, and that nothing in the segment still says a mis-tuned filter *pays* the floor at its error.
7. Grep for the phrases the drain replaced (`stopped bound`, `stationary-sharp`, `iii′`, `Two levers in`, `generic, not exceptional`) and for $n\alpha/2$ stated as the floor for a non-optimal agent; a grep is not a reading, so other phrasings may remain. `CURRENT-VOL1*.md` are generated snapshots and were not rebuilt.
8. Read INTRODUCTION headline 2 against Prop A.1S-τ and `#sketch-structural-adaptation-genericity`: is every clause supported by a body sentence it names?

## Scripts

`recheck.py` runs with `python3 -I` and needs numpy, scipy and mpmath. Its output is reproduced below the script. Sections: (1) $\alpha\Phi(0)$ at $\kappa_R = n/2$; (2) the Corollary 5 counterexample; (3) the elementary bound's ratio to exact; (4) the window against a grid; (5) stopped vs killed moment, exact OU discretization; (6) the exponent cap and $\Phi(0)$ across $\alpha$.

```python
import numpy as np
from mpmath import mp, mpf, quad, gammainc, gamma, exp, log, sqrt, inf

mp.dps = 30

def Phi0(alpha, n, s, R):
    """Lemma A.1S-tau.0: Phi(0) = (2/s^2) int_0^R G(u)/m(u) du."""
    a = mpf(alpha); nn = mpf(n); ss = mpf(s); RR = mpf(R)
    def G(u):
        return mpf(1)/2 * (ss**2/a)**(nn/2) * gammainc(nn/2, 0, a*u**2/ss**2)
    def integrand(u):
        if u == 0:
            return mpf(0)
        m = u**(nn-1) * exp(-a*u**2/ss**2)
        return G(u)/m
    return (2/ss**2) * quad(integrand, [0, RR])

def S4_bound(alpha, n, s, R, svals=None):
    k = mpf(alpha)*mpf(R)**2/mpf(s)**2
    nn = mpf(n)
    if 2*k <= nn-1:
        return None
    best = mpf(0)
    if svals is None:
        svals = [k*f for f in np.linspace(0.02, 0.98, 49)]
    for sv in svals:
        sv = mpf(sv)
        P = gammainc(nn/2, 0, sv)/gamma(nn/2)
        val = gamma(nn/2)/(2*mpf(alpha)) * k**(-nn/2) * exp(k) * P * (2*k/(2*k-nn+1)) * (1 - (k/sv)**((nn-1)/2) * exp(-(k-sv)))
        if val > best:
            best = val
    return best

print("== (1) alpha*Phi(0) at kappa = n/2 (sigma_w = R = 1) ==")
for n in [1, 2, 3, 5, 10, 20, 50, 100, 1000]:
    k = n/2
    v = k*Phi0(k, n, 1, 1)
    print(f"n={n:5d}  alpha*Phi(0)={float(v):.4f}   minus 0.25 ln n = {float(v) - 0.25*np.log(n):.4f}")
print("n=3 margin:", [round(float(k*Phi0(k,3,1,1)),3) for k in [1.5,2.5,3.5,5.5,7.5]])

print("\n== (2) Corollary 5 asymptotic condition is not sufficient ==")
n, alpha, R, s, L, eps = 2, 1.0, 1.0, 10.0, 1.0, 0.02
k = alpha*R**2/s**2
lhs = k - (n/2)*np.log(k); rhs = np.log(2*alpha*L/(eps*float(gamma(n/2))))
print(f"kappa={k}: LHS={lhs:.3f} >= RHS={rhs:.3f}: {lhs>=rhs}; exact Phi(0)={float(Phi0(alpha,n,s,R)):.5f} vs needed {L/eps}")

print("\n== (3) elementary bound / exact ==")
for n, ks in [(1,[2,4,8,16]), (2,[4,8,16]), (20,[20,40,80]), (100,[75,100,200])]:
    print(f"n={n}:", [(k, round(float(S4_bound(k,n,1,1)/Phi0(k,n,1,1)),4)) for k in ks])

print("\n== (4) window ==")
s_env, s_nu, nn = 1.0, 0.5, 1
K = s_env/s_nu
def ssv(a): return nn*(s_env**2 + a*a*s_nu**2)/(2*a)
for R2 in [0.4, 0.5, 0.6, 1.0, 3.0]:
    disc = R2**2 - (nn*s_env*s_nu)**2
    if disc <= 0:
        print(f"R^2={R2}: no window"); continue
    lo = (R2 - np.sqrt(disc))/(nn*s_nu**2); hi = (R2 + np.sqrt(disc))/(nn*s_nu**2)
    g = np.linspace(0.01, 80, 400000); ok = g[ssv(g) < R2]
    print(f"R^2={R2}: analytic ({lo:.4f},{hi:.4f}) grid ({ok.min():.4f},{ok.max():.4f}) lo*hi={lo*hi:.4f} ln(hi/K)={np.log(hi/K):.4f} arccosh={np.arccosh(R2/(nn*s_env*s_nu)):.4f}")

print("\n== (5) stopped vs killed moment, exact OU step ==")
rng = np.random.default_rng(3)
n, a, s, R, dt, N = 2, 2.0, 1.0, 1.0, 5e-4, 8000
x = np.zeros((N, n)); stop = np.zeros(N, bool); cps = [0.25, 0.5, 1.0, 2.0, 4.0]; i = 0
phi = np.exp(-a*dt); q = np.sqrt(s*s*(1-phi*phi)/(2*a))
for kstep in range(1, int(4/dt)+2):
    act = ~stop; xa = x[act]
    xa = phi*xa + q*rng.standard_normal(xa.shape); x[act] = xa
    out = (xa*xa).sum(1) > R*R; idx = np.where(act)[0][out]
    x[idx] *= R/np.sqrt((x[idx]**2).sum(1))[:, None]; stop[idx] = True
    t = kstep*dt
    if i < len(cps) and t >= cps[i]-1e-12:
        r2 = (x*x).sum(1)
        print(f"t={t:.2f} stopped={r2.mean():.3f} would-be bound={n*s*s/(2*a):.3f} P(tau<=t)={stop.mean():.3f} killed={(r2*~stop).mean():.3f} (i) bound={n*s*s/(2*a)*(1-np.exp(-2*a*t)):.3f}")
        i += 1

print("\n== (6) kappa_R(alpha) peaks at K; Phi(0) across alpha, n=1 ==")
s_env, s_nu, R = 1.0, 0.5, 1.0; K = s_env/s_nu
ag = np.linspace(0.05, 20, 200000); kap = ag*R**2/(s_env**2 + ag**2*s_nu**2)
print(f"argmax alpha={ag[kap.argmax()]:.3f} (K={K}), kappa_max={kap.max():.4f} vs {R**2/(2*s_env*s_nu):.4f}")
for al in [0.5*K, 0.8*K, K, 1.25*K, 2*K]:
    sw = np.sqrt(s_env**2 + al**2*s_nu**2)
    print(f"alpha={al:.2f}: kappa={al*R**2/sw**2:.3f} Phi(0)={float(Phi0(al,1,sw,R)):.4f}")
```

Output, 2026-10-30:

```text
== (1) ==
n=    1  alpha*Phi(0)=0.5957   minus 0.25 ln n = 0.5957
n=    2  alpha*Phi(0)=0.6590   minus 0.25 ln n = 0.4857
n=    3  alpha*Phi(0)=0.7064   minus 0.25 ln n = 0.4318
n=    5  alpha*Phi(0)=0.7767   minus 0.25 ln n = 0.3744
n=   10  alpha*Phi(0)=0.8885   minus 0.25 ln n = 0.3129
n=   20  alpha*Phi(0)=1.0157   minus 0.25 ln n = 0.2668
n=   50  alpha*Phi(0)=1.2018   minus 0.25 ln n = 0.2238
n=  100  alpha*Phi(0)=1.3526   minus 0.25 ln n = 0.2013
n= 1000  alpha*Phi(0)=1.8897   minus 0.25 ln n = 0.1628
n=3 margin: [0.706, 1.574, 3.124, 11.978, 51.237]
== (2) ==
kappa=0.01: LHS=4.615 >= RHS=4.605: True; exact Phi(0)=0.00501 vs needed 50.0
== (3) ==
n=1: [(2, 0.5719), (4, 0.7429), (8, 0.9088), (16, 0.9661)]
n=2: [(4, 0.6176), (8, 0.8685), (16, 0.9618)]
n=20: [(20, 0.6886), (40, 0.9714), (80, 0.9908)]
n=100: [(75, 0.8016), (100, 0.9681), (200, 0.9944)]
== (4) ==
R^2=0.4: no window
R^2=0.5: no window
R^2=0.6: analytic (1.0734,3.7266) grid (1.0735,3.7265) lo*hi=4.0000 ln(hi/K)=0.6224 arccosh=0.6224
R^2=1.0: analytic (0.5359,7.4641) grid (0.5359,7.4641) lo*hi=4.0000 ln(hi/K)=1.3170 arccosh=1.3170
R^2=3.0: analytic (0.1678,23.8322) grid (0.1680,23.8321) lo*hi=4.0000 ln(hi/K)=2.4779 arccosh=2.4779
== (5) ==
t=0.25 stopped=0.327 would-be bound=0.500 P(tau<=t)=0.107 killed=0.220 (i) bound=0.316
t=0.50 stopped=0.510 would-be bound=0.500 P(tau<=t)=0.339 killed=0.172 (i) bound=0.432
t=1.00 stopped=0.738 would-be bound=0.500 P(tau<=t)=0.645 killed=0.094 (i) bound=0.491
t=2.00 stopped=0.930 would-be bound=0.500 P(tau<=t)=0.904 killed=0.026 (i) bound=0.500
t=4.00 stopped=0.995 would-be bound=0.500 P(tau<=t)=0.993 killed=0.002 (i) bound=0.500
== (6) ==
argmax alpha=2.000 (K=2.0), kappa_max=1.0000 vs 1.0000
alpha=1.00: kappa=0.800 Phi(0)=1.0679
alpha=1.60: kappa=0.976 Phi(0)=0.8726
alpha=2.00: kappa=1.000 Phi(0)=0.7226
alpha=2.50: kappa=0.976 Phi(0)=0.5585
alpha=4.00: kappa=0.800 Phi(0)=0.2670
```
