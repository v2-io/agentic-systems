*KR C.1 — "Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier" — and C.2 — "Strengthenings C1–C3 … are independently checked, then landed or refuted" — item C1. Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself."*

# Part I, round 3: the independent check

This checks the merge at `e6044566` (commits `6844f3c8`, `dcb18927`, `7734a100`, `bc1cdeeb`), read at `edead09c`. The typed record is `reviews/part-i-round-3-check-1.md`, and my scripts are `part-i-check-3.py` beside this file. I read the integrator's account and record before checking, and I re-derived or recomputed each claim without reusing the integrator's methods.

## Verdict

The landing holds. Every number canon now quotes reproduced, by methods other than the integrator's. I re-derived the threshold expansion by hand, and "derived to two terms" is its honest tier. The round-2 findings it set out to answer are answered in the text. What remains is small. One site of the gain-and-time defect was outside the round's reach. One INTRODUCTION headline kept the wording that the round's third commit corrected in the parallel Brief. A sentence in a proof was broken by a splice. A prior source for the series is named by a paper the integrator read and is cited nowhere. The tier of the expansion's remainder can go up. None of these touches the mathematics that landed.

## What I checked, and how

- **The series and the strengthening (F8, C.2).** I re-derived the series from the concavity identity by hand. I computed it by log-space summation, with no hypergeometric routine, against the $t$-form integral $\int_0^1 t^{n-1}(e^{\kappa_R(1-t^2)} - 1)/(1-t^2)\,dt$ rather than the integrator's $G/m$ form, at the same eight points: 15 digits agree. I worked the threshold expansion by hand without reading the integrator's derivation first. The log-product expansion matches. The Mellin double pole gives $\tfrac12\ln(2m) + \tfrac12\gamma_{\mathrm E}$; the bookkeeping is $\Gamma$'s $-\gamma_{\mathrm E}$ against $\zeta(1+2s)$'s $+\gamma_{\mathrm E}$, net $+\tfrac12\gamma_{\mathrm E}$. The two Gaussian sums give $(\tfrac12 + \tfrac16)\sqrt{\pi/2}\,m^{-1/2}$. My own numerics reproduce the residual sequences to the printed digits. The remainder order is provable from the same ingredients (F5 below).
- **Every other quoted number.** Threshold table, two-term values, margin values, the exact/asymptotic ratios, and the claim that the asymptotic over-estimates at $\kappa_R = n/4$ for each $n$ from 1 to 1000, which I checked at every $n$. Gain maximizers by grid search, not a bounded minimizer; they also approach $K$ ($0.96K$ at $\kappa_R(K) = 25$). Doubling increments by bisection: one prints as $0.96$ where the value is $0.9548$. The dip instance by a finite-difference solve of the radial boundary-value problem, converged at $3.5687$, against the integrator's quadrature of the Andronov–Vitt–Pontryagin formula. The non-exit table by Crank–Nicolson time-stepping, against the integrator's spectral solve: all twelve probabilities agree.
- **Primary.** I read Kersting et al. 2023 Theorem 4 and eq. (17) at arXiv:2208.04029. It is canon's integral under $\theta = \alpha$, $\sigma = \sigma_w$. I did not read Ikeda–Watanabe or Grebenkov; the integrator's reads of them stand on its record alone.
- **Algebra.** CT-S from $V = \xi^TM\xi$ at constant $M$: $c_{\text{Itô}} = 1$, invariance under $M \to kM$, and reduction to $\kappa_R \gt n/2$ at $M = I$. The CT2 ray-integration step for state-dependent $M$ is still unexamined. Also $\rho$ read as total in `#hyp-mismatch-dynamics`, giving $\rho_{\text{env}}/\mathcal T + \bar\nu$; $\alpha = \mathcal T$ only at the optimal gain, which follows from `#def-adaptive-tempo` defining $\mathcal T$ with $\eta^\ast$; the predictive floor $\operatorname{tr}(HP^-H^T)$; the deliberation threshold.
- **Sentences.** I read every changed gain-and-time sentence in the four places the account names. Then I grepped the four volumes, the READMEs, `FINDINGS.md`, `NOTATION.md` and `LEXICON.md` for the pre-round phrasings: "up to the Kalman gain", "loses bounded behavior", "computed trend", "$m_2^2$", "3.8×", "while certified", "directly measurable", "Mismatch injection rate", "capped at the Kalman gain" and "buys time". I read INTRODUCTION :50 against `#disc-ciy-unified-objective`'s active-inference paragraph. Every clause of :50 is carried there, and the removed "special case under three explicit restrictions" is not.
- **`#detail-operationalization`.** The line between what the recipes estimate (the innovation) and what they are stated for (the noiseless-channel case) is drawn truthfully. The deferral to `item:write-innovation-based-estimators-for-detail-ope` is honest, not a softening. The false sentence is gone, its replacement is true and scoped, and the estimators do not yet exist.
- **Mechanics.** `bin/refresh-all --check` is clean and `md-press` is clean on the changed files. `git diff b15e947d 6844f3c8` over every file the round touched is empty. The integrator's record and account cite `b15e947d`, the pre-rebase commit, which is no longer on any branch. Its checks therefore describe the landed text, but that hash is not reachable from `main` and may be garbage-collected. Citing `6844f3c8` would keep the evidence reachable. This is noted here only, since the record itself is not edited after `vsect take`.

## Findings

1. **A residual site of the gain-and-time defect** (record F1). `#result-sector-condition-stability` :61 reads "On a fixed noisy channel the exponent is capped at the Kalman gain, so past it a stronger correction shortens the stay." The implied converse, that up to $K$ a stronger correction lengthens the stay, is false between the stay's maximizer and $K$. The round-2 check's site list did not include this segment, and the round-3 grep covered only the four places named. The fix is the sentence the round wrote in `#impl-persistence-and-limits` :33.
2. **INTRODUCTION headline 1 says containment** (record F2). It reads "loses the guarantee that its error stays contained". Commit `7734a100` corrected exactly this wording in `#result-persistence-condition`'s Brief, because containment is Model D's. The headline names a Kalman filter among its instances, and headline 2, directly below, says no correction buys containment against stochastic disturbance. The account's "fixed the same way as the Brief" was true before the Brief changed again.
3. **A broken sentence in Prop A.1S-τ(ii)'s proof** (record F3), at :293: "… the affine comparison drift $n\sigma_w^2 - 2\alpha\xi$, Read at the primary, the theorem asks for …". This is a splice left over from replacing the "not read at the primary" clause.
4. **A probable prior form of the series** (record F4). Kersting's Remark 5, on the page the integrator read, says Graczyk & Jakubowski 2008 (Thm 2.2) express (17) "using hypergeometric functions". Canon never claims the series is new. Still, the Search Log line "neither of the last two states the series form" passes over the source Kersting points to, and per prior-art integration the Related Work row should name it as the probable prior form. Nobody in the chain has read it. HAL has a record for it and no file.
5. **A strengthening available** (record F5, C.2). The $O(n^{-1})$ remainder that canon labels "confirmed numerically" can be proved with what the derivation already uses. The Mellin contour shifts past $s = -1$. For $k \leq m^{2/3}$ the exponent error is uniformly $O(k^2/m^2 + k^4/m^3)$ while the exponent stays bounded, so each dropped term contributes $O(1/m)$. Poisson summation makes the Gaussian sums exact up to $-\tfrac12$ and exponentially small terms. The tail beyond $m^{2/3}$ is exponentially small. With those lines written, the label rises to "derived, remainder $O(n^{-1})$". The integrator's tier is accurate as it stands, but under-states what can be shown.

These are noted here only, not as separate record entries, since they are W-grade:

- `NOTATION.md` :243 still glosses $\rho$ as "Mismatch injection rate", while the round moved `#detail-operationalization` and `#hyp-mismatch-dynamics` to "total disturbance". The gloss is ambiguous rather than wrong.
- The $(3, 6)$ doubling increment prints as $0.96$; it is $0.955$.
- `CURRENT-VOL1*.md` still carries "up to the Kalman gain" five times. The account says it was not rebuilt, and it is a generated snapshot.

## Influx

Nothing here reopens the integrator's dispositions of D6, D7, D9 or D14. One addition for whoever drains the area: `#result-sector-condition-stability` (F1) is a summary-layer site of the same kind as A.2's front-door work, so it may already be on a list I did not find.

## What the record does in vsect

`reviews/part-i-round-3-check-1.md` is taken: C1–C16 are bound to the current versions, and F1–F5 are open. As the mind other than the reviser and the round-2 checker, I marked these findings answered by the round-3 revisions, each after reading it against the current text, with a `--why` that names the evidence:

- `review:part-i-round-2-check-1` F1–F13, F15 and F16, and its C16/finding and C17/finding.
- `review:part-i-mismatch-lineage-check-1#C11/finding`, the $\rho$ readings in `#hyp-mismatch-dynamics`.

Several stay open:

- That review's F3 is wider than `#hyp-mismatch-dynamics`. It also covers how `#deriv-persistence-cost` reads $\sigma_w$, which I did not check.
- F14 stays open because `#example-kalman` belongs to another lane.
- `review:part-i-round-2-integration#F2` stays open because Day 1983 and the heavy-tail sources are still unread.
- `question:the-front-door-sentences-say-gain-buys-time-only` was already closed when I reached it.

I confirmed 17 round-2 checks on `#deriv-sector-condition` (`review:part-i-round-2-check-1` C1–C9, `review:part-i-round-2-integration` C1–C7 and C9) and 2 on `#der-deliberation-cost`. In each case the confirmation is `for-checks`, limited to those checks: the round left the statements they read unchanged in content. I did not confirm the whole revision. That would have re-bound about forty checks from other lanes that rest on the segment, and I have no basis to vouch for them. The lapsed checks on `#def-mismatch-signal` lapsed because other lanes edited text it rests on, so they are not this round's to confirm.

## What I would do next, if wanted

F1–F3 are a few sentences each and want an integrator. I kept to the verifier's side, so I did not edit canon. If you would rather I take them, and someone else checks them afterward, I can. F5 is a short spike-sized write-up into the Lemma. F4 needs a library copy of Graczyk–Jakubowski.
