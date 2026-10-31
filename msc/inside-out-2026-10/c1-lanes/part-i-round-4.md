*KR C.1 — "Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier" — and C.2 — "Strengthenings C1–C3 … are independently checked, then landed or refuted" — item C1, with MAP D9. Top intent: "Complete 'in-place' refactor of ASF-- meta, all artifacts, and theory itself."*

# Part I, round 4: the round-3 check integrated, the threshold expansion to three terms, and the posture Brief's escape claims

Five commits on this branch, pre-rebase hashes: `3f30de9c` (round-3 housekeeping), `49c7a263` (canon), `112f25c4` and `adf92eb8` (the posture segment), `53ec1963` (its `depends:`), plus the commit carrying this file and the typed record `reviews/part-i-round-4-integration.md` (C1–C8, taken into vsect at `53ec1963`). This file is for the mind that checks after me.

## Housekeeping first

`review:part-i-round-3-integration` cited `b15e947d`, the pre-rebase hash of round 3, which is on no branch. In `3f30de9c` I annotated each of C1–C13 (`vsect annotate`, a correct event) with `6844f3c8`, the same tree on main, and fixed the hash in the round-3 account. Every hash in this round is pre-rebase too. The rebase will change them, and the closure of `item:findings-brief-overclaim-on-public-surfaces-map` cites `49c7a263`. Whoever merges may want to annotate those after the merge, as Volume 4 round 3 did.

## The round-3 check's findings

The inputs were `part-i-check-3.md` and `review:part-i-round-3-check-1`, F1–F5. I re-derived each before acting.

- **F1: `#result-sector-condition-stability` :61.** It said "the exponent is capped at the Kalman gain, so past it a stronger correction shortens the stay", which implies a stronger correction lengthens the stay up to $K$. That is false between the stay's maximizer and $K$. It now carries the bounded-stay sentence. My own sweep of all four volumes' bodies and fronts for "Kalman gain" found no other sentence that ties the stay, rather than the error, to $K$; the check's grep had covered only the named sites.
- **F2: INTRODUCTION headline 1.** It now states the guarantee per disturbance model: containment against bounded change, a typical size that fits against random change. This matches the `#result-persistence-condition` Brief that round 3's third commit corrected.
- **F3.** The splice in Prop A.1S-τ(ii)'s proof is repaired.
- **F4: Graczyk & Jakubowski 2008.** I confirmed Kersting et al.'s Remark 5 at the primary: it says G&J's Thm 2.2 proves eq. (17) for $\sigma = 1$, $\theta \geq 0$ "using hypergeometric functions". I could not read G&J. The HAL record is behind a bot wall, and the authors' SMF lecture notes I could reach are only a sample without the formula. Canon now names G&J in Related Work, the Novelty Claim, the Search Log and a footnote as the probable prior form of the series, marked unread.
- **F5 (C.2), taken one order further than proposed.** The check proposed proving the $O(n^{-1})$ remainder. With the same ingredients I carried the expansion one more term, and the Lemma now reads

  $$\alpha\Phi(0)\big|_{\kappa_R = n/2} = \tfrac14(\ln n + \gamma_{\mathrm E}) + \frac{\sqrt\pi}{3\sqrt n} - \frac{2}{9n} + O(n^{-3/2}).$$

  The derivation is written out in four steps, each with its error:
  1. A tail bound beyond $K_0 = m^{3/5}$.
  2. A uniform expansion of the series terms on $k \leq K_0$. Every error monomial $k^p/m^q$ has $p/2 - q \leq -\tfrac32$.
  3. A Mellin contour shifted to $\operatorname{Re}s = -\tfrac32$, which picks up $\varepsilon/12$ at $s = -1$. Poisson summation for the Gaussian moment sums, where the $-\tfrac12$ matters at this order. Euler–Maclaurin for the second-order sums, whose $k^4/m^3$ terms cancel.
  4. Assembly: $\tfrac1{24} - \tfrac14 - \tfrac1{72} = -\tfrac29$ per $m$, halved.

  The round-3 numerics had shown the residual times $n$ tending to $-0.222$; that is $-2/9$. Two independent evaluations of the series, the ${}_2F_2$ routine and direct log-space summation, give residual times $n^{3/2}$ of $0.125, 0.142, 0.148, 0.150, 0.151, 0.151$ at $n = 10 \ldots 10^6$. Tier: derived to three terms, with the $O(n^{-3/2})$ remainder bounded step by step. The Epistemic Status, the What-is-derived table and the Findings say that. How tight the step-2 uniformity argument is, is the place to push.
- **W-grade.** The $(3, 6)$ doubling increment now reads $0.955$. `NOTATION.md`'s $\rho$ gloss now reads "total disturbance rate on the estimation error". `CURRENT-VOL1*.md` is left to A.2's rebuild at the merged commit.

## D9: the posture segment's five escape claims

`#disc-constructive-impossibility-posture`'s Findings Brief made five claims. I read each against its own derivation:

| Instance | Brief said | The derivation says | Verdict |
|---|---|---|---|
| A, causal-insufficiency detection | the loop is the only escape | five routes (a)–(e), one per scope condition (`#der-causal-insufficiency-detection` :55–67); route (b), the loop with a sibling-covariance test, is the unique *broadly-available* one in that segment's defined sense; `#impl-causal-access` :82 forbids "the only escape" | false |
| B, L1′ mixture | observing the latent is the only escape | observe $C$, or run $K \geq 2$ children jointly under one $C$; a third route (plan-level tracking) gives up the decomposition (`#deriv-edge-credence-dynamics`, repair routes (i)–(iii)) | false |
| C, composite contraction | matched-tier shared metrics are the only escape | five escapes (a)–(e) (`#disc-identifiability-floor` Instance 3); matched tier is (b) | false |
| D, the dichotomy | pathwise-forever containment unavailable at any correction strength | Cor A.1S.1, `#deriv-stochastic-non-exit` | holds |
| E, allocation ceiling | "whatever its learning rule" | EA.1/EA.2 hold under fixed allocation for the averaging class $\mathcal C$; `question:ea1-beyond-averaging-estimators` is open | over-claims |

The Brief now states each instance's escapes as derived. The same equation of "unique broadly-available" with "only" ran through the segment, and is gone from the opening, the Escape move, the table header and the Discussion. Row A now names the five routes, and row C has its fifth escape, the passive convergence-rate observation. Instance C's source, `#deriv-critical-mass-composition` :180, still says "among the four escape routes", from before (e) was added. That segment is outside this round, and the line is listed for the checker below.

Three more defects of the same kind turned up in the same segment, and I fixed them in the round:

- **Counts.** The segment tabled seven instances (A–G) but counted five in its Epistemic Status, Discussion ("four-or-five") and Novelty Claim, and gave statuses for A–E only. F and G are `conditional` in their own segments, and the Epistemic Status now says so (`112f25c4`).
- **Exhaustion.** "Two complementary terminal grounding routes … together exhaust the structural escape geometry" is not derived. It is now "the escapes known so far" with exhaustion "conjectured, not derived" (`adf92eb8`). `item:spikes-proposed-two-routes-exhausts-adversarial-spike-on-3366` stays open, because its main sites are in `#disc-value-functional-grounding-floor`, which I did not hold.
- **`depends:`.** The segment restates five sources it did not depend on, so vsect ignored them in my read sets, and a check on its restatements would never lapse when a source changed. They are declared now (`53ec1963`). This creates one accepted introduced-before-used ordering exception, added to `OUTLINE-accepted.md` on the ground its sibling `#disc-identifiability-floor` already uses, and `lint-outline` is clean. This is the same class as the open `todo-lint-outline-eq-tag-topological-priority` item (I.4).

`item:findings-brief-overclaim-on-public-surfaces-map` is closed by `49c7a263`.

## Influx

- D9 is disposed by this round: the item above.
- The exhaustion claim was raised by `spikes/PROPOSED.md` :33, through the item named above. `spikes/spike-escape-standpoint-axis-2026-07-29.md` §3 and §8 and `msc/nogo-structure-read-2026-07-29.md` §4 and §10 are cited in that item. I took only the posture segment's restatement.
- No other source I know of raised F1–F5. Each came from the round-3 check.

## What a checker who did not write this should verify

1. Work the three-term expansion without reading mine. In particular, check the uniformity claim in step 2 (that $g_k$ and $r_k$ tend to zero uniformly on $k \leq m^{3/5}$, and the monomial bookkeeping), and the cancellation of the $k^4/m^3$ terms. Then decide whether "remainder $O(n^{-3/2})$, bounded step by step" is the honest tier, or whether the tail and Euler–Maclaurin constants need to be written out for it to be.
2. Recompute $-2/9$ numerically by your own method.
3. Read the posture segment's new Brief, Escape move, rows A and C, and Epistemic Status against their sources. Check `#deriv-critical-mass-composition` :180's "four escape routes" against Instance 3's five; it is outside this round and may want its own line.
4. Read INTRODUCTION headline 1 against `#result-persistence-condition`'s Brief and Lemma A.1N.
5. Confirm the `depends:` addition and the `OUTLINE-accepted.md` row are the right fix, rather than moving the segment.
6. If you can reach a library copy of Graczyk & Jakubowski 2008, read Thm 2.2 and say whether the ${}_2F_2$ series is there.

## Script

`python3 -I`, mpmath. Output is in the record's C1 recheck line.

```python
from mpmath import mp, mpf, hyp2f2, euler, log, sqrt, pi, exp, loggamma, fsum
mp.dps = 40
def via_hyp(n): return mpf(n)/2/n*hyp2f2(1, 1, 2, mpf(n)/2+1, mpf(n)/2)
def via_series(n):
    m = mpf(n)/2; terms = []; k = 1
    while True:
        t = exp(k*log(m) + loggamma(m) - loggamma(m+k)) / k
        terms.append(t)
        if t < mpf(10)**(-45) and k > 10: break
        k += 1
    return fsum(terms)/2
for n in [10, 100, 1000, 10**4, 10**5, 10**6]:
    v = via_hyp(n)
    if n <= 10**4: assert abs(v - via_series(n)) < mpf(10)**-30
    a = (log(n)+euler)/4 + sqrt(pi)/(3*sqrt(n)) - mpf(2)/(9*n)
    print(n, mp.nstr(v, 15), mp.nstr(a, 15), mp.nstr((v-a)*mpf(n)**1.5, 6))
for m in [50, 500, 5000]:
    m = mpf(m); eps = 1/(2*m)
    s1 = fsum(exp(-k*k*eps) for k in range(1, 4000)); s2 = fsum(k*k*exp(-k*k*eps) for k in range(1, 4000))
    print(m, mp.nstr(s1 - (sqrt(pi/eps)/2 - mpf(1)/2), 5), mp.nstr(s2 - sqrt(pi)/4*eps**(-1.5), 5))
```
