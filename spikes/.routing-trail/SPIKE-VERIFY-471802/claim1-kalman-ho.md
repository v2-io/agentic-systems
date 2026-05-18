# Claim 1 — Kalman-Ho similarity-orbit no-go, independent re-derivation

## What the spike claims (§4)

> Two AAT agents whose linearized closed-loop residual dynamics are minimal
> state-space realizations $(F,\sigma_w)$ and $(F',\sigma_w')$ related by an
> invertible similarity $F'=TFT^{-1}$, $\sigma_w'\sigma_w'^\top =
> T\sigma_w\sigma_w^\top T^\top$. Then the stationary innovation process —
> hence every $(\alpha,R)$-summary, every moment of $\|\delta\|$, and the
> entire on-policy observation law — is identical for $A$ and $A'$. Exact in
> the linear-Gaussian / Kalman sub-scope.

## Constitutive bedrock (verified first-hand, not via spike)

`#deriv-sector-condition` (`status: exact`, line 212): the Model-S mismatch
SDE is $d\delta = -F(\mathcal T,\delta)\,dt + \sigma_w\,dW_t$, $W_t$ a
standard $n$-dim Wiener process. Canon's $F$ is the (generally nonlinear)
correction operator and the Itô-Lyapunov derivation (lines 216–238) uses
only the sector lower bound $\delta^\top F\ge\alpha\|\delta\|^2$. The
linear-Gaussian specialization $F(\mathcal T,\delta)=F\delta$ with constant
$F$ is a genuine **sub-scope restriction** (the spike labels it $\alpha_1$ /
Kalman and does not hide this). For a stationary residual we need $-F$
Hurwitz (eigenvalues of $F$ in the open right half-plane), which is exactly
the sector condition's regime ($\alpha>0$ for a linear operator forces
$\mathrm{sym}(F)\succ0$, hence $F$ has spectral abscissa controlling decay;
stationarity additionally needs $-F$ Hurwitz, a mild added assumption I make
explicit — the spike implicitly assumes it via "stationary innovation").

## Re-derivation from scratch

Linear-Gaussian residual process for agent $A$:
$$d\delta = -F\delta\,dt + \sigma_w\,dW_t,\qquad Q:=\sigma_w\sigma_w^\top\succeq0.$$

This is an Ornstein–Uhlenbeck process. With $-F$ Hurwitz it has a unique
Gaussian stationary law $\delta_\infty\sim\mathcal N(0,\Pi)$ where $\Pi$
solves the continuous Lyapunov equation
$$(-F)\Pi + \Pi(-F)^\top + Q = 0 \iff F\Pi + \Pi F^\top = Q.\tag{L}$$

(Note: the spike writes $F\Pi+\Pi F^\top+\sigma_w\sigma_w^\top=0$. Sign check:
for $dx=Ax\,dt+\sigma\,dW$ stationary covariance solves $A\Pi+\Pi A^\top+
\sigma\sigma^\top=0$. Here $A=-F$, giving $-F\Pi-\Pi F^\top+Q=0$, i.e.
$F\Pi+\Pi F^\top=Q$. **The spike's Lyapunov equation has a sign error**:
it writes $F\Pi+\Pi F^\top+\sigma_w\sigma_w^\top=0$, which would require
$\Pi\preceq0$ for $Q\succeq0$ — impossible for a covariance. The correct
equation is $F\Pi+\Pi F^\top=Q$ (equivalently $(-F)\Pi+\Pi(-F)^\top+Q=0$).
This is a **transcription slip in the spike's proof, not a defect in the
result** — see assessment below.)

### Transformation under similarity

Let $\delta' = T\delta$. Then from $d\delta=-F\delta\,dt+\sigma_w\,dW$:
$$d\delta' = T\,d\delta = -TFT^{-1}(T\delta)\,dt + T\sigma_w\,dW
           = -F'\delta'\,dt + \sigma_w'\,dW,$$
with $F'=TFT^{-1}$ and $\sigma_w'=T\sigma_w$ so $\sigma_w'\sigma_w'^\top =
T\sigma_w\sigma_w^\top T^\top = TQT^\top =: Q'$. **This is exactly the
spike's similarity pair**, and the derivation is forced (one line, change of
state variable). So agent $A'$ with realization $(F',\sigma_w')$ is the
*same residual process viewed in coordinates $\delta'=T\delta$.*

Stationary covariance of $A'$: $\Pi'$ solves $F'\Pi'+\Pi'F'^\top=Q'$.
Substituting $F'=TFT^{-1}$, $Q'=TQT^\top$ and the ansatz $\Pi'=T\Pi T^\top$:
$$TFT^{-1}\,T\Pi T^\top + T\Pi T^\top\,T^{-\top}F^\top T^\top
 = TF\Pi T^\top + T\Pi F^\top T^\top = T(F\Pi+\Pi F^\top)T^\top = TQT^\top=Q'.\ \checkmark$$
So $\Pi'=T\Pi T^\top$, **confirming the spike's transformation law**
$\Pi'=T\Pi T^\top$ exactly.

### What an on-policy summary-only observer sees

The decisive question is **what the observable actually is**. The spike's
result is correct *only if the observable is similarity-invariant*. Two
candidate observables, and they behave differently:

1. **Raw second moment $\mathbb E\|\delta\|^2=\operatorname{tr}\Pi$.** Under
   similarity $\operatorname{tr}\Pi' = \operatorname{tr}(T\Pi T^\top)\ne
   \operatorname{tr}\Pi$ in general. **The spike states this explicitly and
   correctly** ("$\mathbb E\|\delta\|^2=\operatorname{tr}\Pi$ is *not even
   similarity-invariant in general*"). So if the observer could see the raw
   internal residual $\delta$ in a *fixed external basis*, the two agents
   would be **distinguishable** — the orbit is not invisible to a
   basis-fixed second-moment.

2. **The innovation spectrum / transfer function.** The spike's actual claim
   is that the observable is the *innovation process* (equivalently the
   output spectral density), which is similarity-invariant. This is the
   classical Kalman-Ho fact: a minimal state-space realization
   $(A,B,C[,D])$ of a transfer function $H(s)=C(sI-A)^{-1}B$ is unique only
   up to $A\mapsto TAT^{-1}$, $B\mapsto TB$, $C\mapsto CT^{-1}$; the
   transfer function (hence the output spectrum, hence — for a Gaussian
   process — the entire output law) is invariant. Verified independently:
   $C'(sI-A')^{-1}B' = CT^{-1}(sI-TAT^{-1})^{-1}TB = CT^{-1}\,T(sI-A)^{-1}
   T^{-1}\,TB = C(sI-A)^{-1}B$. Forced, classical, correct.

**The load-bearing gap the spike glosses.** The spike's no-go is exact
**only under the added premise that the observer's channel is an output map
$y=C\delta$ (or a similarity-invariant functional of the residual), not the
raw residual $\delta$ in a fixed basis.** The spike asserts "every moment of
$\|\delta\|$ … is identical" — this is **false as stated** for the raw
residual (point 1: $\operatorname{tr}\Pi$ is not similarity-invariant, by
the spike's own admission two sentences later). It is true for the
*innovation/output* observable. The construction goes through iff the AAT
on-policy summary $(\alpha,R)$ is a function of similarity-invariants only.

Check that: $\alpha$ = the sector parameter = (in the linear case) governed
by the spectrum of $\mathrm{sym}(F)$ under the *agent's own* metric. The
eigenvalues of $F$ are similarity-invariant ($F'=TFT^{-1}$ is similar, same
spectrum) — so the **$\alpha$-spectrum (eigenvalues of $F$) is invariant**.
But $\mathrm{sym}(F)=\tfrac12(F+F^\top)$ is *congruence*-natural, not
similarity-natural: $\mathrm{sym}(TFT^{-1})\ne T\,\mathrm{sym}(F)\,T^{-1}$ in
general, and the sector parameter defined via $\delta^\top F\delta$ in a
**fixed** inner product is *not* similarity-invariant. It *is* invariant if
$\alpha$ is read off the closed-loop **spectrum / decay rate** (eigenvalues
of $F$) rather than a fixed-basis quadratic form. The neutral-drift spike
(line 319) is careful here: it states the orbit is "a finite-dimensional
manifold of **Jordan-form-preserving** architectural variations" — i.e. the
invariant is the Jordan form / spectrum, which is exactly the
similarity-invariant. That is the honest statement.

## Assessment

**The result is correct in its sharp form; the spike's stated form
overclaims by one clause and carries one transcription slip.**

- **Sound, forced, classical:** the similarity transformation $d\delta'=
  -F'\delta'dt+\sigma_w'dW$ with $\Pi'=T\Pi T^\top$; the transfer-function /
  output-spectrum invariance under $GL(n)$ similarity (Kalman 1963; Ho &
  Kalman 1966; Anderson & Moore 1979 §10.4 — the citations check out as the
  standard minimal-realization non-uniqueness result). For a Gaussian
  stationary output process the spectrum *is* the full law, so two
  similarity-related minimal realizations are **observationally identical at
  the output**. This half is exact and the spike earns it.

- **Overclaim (one clause):** "every moment of $\|\delta\|$ … is identical"
  is false for the **raw internal residual** $\delta$ in a fixed external
  basis (the spike itself shows $\operatorname{tr}\Pi$ is not
  similarity-invariant — internal contradiction within the boxed claim). The
  correct scoping is: identical for the **innovation/output** observable
  (and any similarity-invariant summary, which $(\alpha=\text{spectrum},R)$
  is, **provided** $\alpha$ and $R$ are read as spectral/decay-rate
  invariants — the Jordan-form-preserving framing the neutral-drift spike
  used, line 319). Under that correct scoping the no-go is exact. The
  AAT-specific content (the architectural d.o.f. is the similarity orbit,
  invisible at the output) is right.

- **Transcription slip (not load-bearing):** the spike's Lyapunov equation
  $F\Pi+\Pi F^\top+\sigma_w\sigma_w^\top=0$ has a sign error; the correct
  one is $F\Pi+\Pi F^\top=\sigma_w\sigma_w^\top$ (equivalently
  $(-F)\Pi+\Pi(-F)^\top+\sigma_w\sigma_w^\top=0$). The *transformation law*
  $\Pi'=T\Pi T^\top$ the spike then uses is correct under the corrected
  equation (verified above), so the conclusion is unaffected — but a landing
  agent copying the spike's display equation verbatim would import a
  sign-wrong Lyapunov equation into canon. **Flag for the landing plan.**

## Verdict on Claim 1

**Confirmed with required scoping correction.** The Kalman-Ho
similarity-orbit no-go is **genuinely exact in the linear-Gaussian / Kalman
sub-scope** when stated as: *similarity-related minimal residual
realizations are identical at the innovation/output observable and on every
similarity-invariant summary; the architectural degree of freedom (the
$GL(n)$ similarity fiber) is annihilated by the output map.* It is **not**
exact as the spike's boxed sentence literally reads (the "every moment of
$\|\delta\|$" clause is false for the raw residual and contradicts the
spike's own next sentence). Two defects, both repairable, neither fatal:
(i) drop/repair the "every moment of $\|\delta\|$" clause → "every
similarity-invariant summary, including the innovation spectrum and the
spectral $(\alpha,R)$"; (ii) fix the Lyapunov-equation sign.

**Tier:** exact-in-sub-scope **after** the scoping repair (matches the
spike's claimed tier *only once repaired*). As literally written: overclaimed.

Loci opened: `#deriv-sector-condition` (210–238, the Model-S SDE + Itô
derivation, `status: exact`); spike §4 + boxed claim; neutral-drift spike
lines 319, 344–346 (the Jordan-form-preserving / dual-anchor framing that
states it correctly).
