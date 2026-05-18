# Spike: Strengthening Prop A.1S(iii) — the Model-S non-exit probability

**Status:** COMPLETE — verdict reached. Completion-state **(3): a sharp no-go,
plus a corrected-and-true statement that is itself a real structural result.**
**Locus:** `01-aat-core/src/deriv-sector-condition.md`, Proposition A.1S, part
**(iii) "Non-exit probability."**
**Date:** 2026-05-16.
**Discharge direction:** strengthening attempted *first* and *hard* (per
`~/.claude/memory/epistemic-discipline/strengthen-before-soften.md` and
`CLAUDE.md` §"Strengthen before softening"); the strengthening route the prior
peer adjudication asserted as "standard textbook, should not fail" was
**worked through and found to genuinely fail** — and *why* it fails is the
result. This is not a soften-by-default; it is a soften-direction reached only
after the strengthening was honestly exhausted, with the obstruction now named
structurally.

---

## 1. The locus and the defect (verified first-hand against current `src/`)

`deriv-sector-condition.md` Prop A.1S(iii) (segment line ~194) states, under
the mean-square persistence condition (ii):

> at steady state the Markov tail bound gives
> $P(\tau_R < \infty) \leq n\sigma_w^2/(2\alpha R^2)$

with $\tau_R = \inf\{t : \lVert\delta(t)\rVert > R\}$ (the **first-exit time**,
segment line ~180), and the Epistemic Status (line ~282) certifying A.1S
*exact* because "(iii) follows from a Markov tail estimate on the
supermartingale $V(\delta)$ … No implicit strengthening of A2' is required."
The proof paragraph (line ~242) gestures at "standard tail estimates on the
supermartingale $V(\delta(t))\mathbb{1}_{\{t\leq\tau_R\}}$."

`P(\tau_R < \infty)` is, by the segment's own definition of $\tau_R$, the
**infinite-horizon ever-exit probability**
$P\big(\sup_{t\geq 0}\lVert\delta(t)\rVert > R\big)$. A
Markov/Chebyshev inequality applied to the steady-state second moment bounds
the **fixed-time / stationary** tail $P(\lVert\delta(t)\rVert > R)$ at a fixed
$t$. These are different objects. The segment is internally inconsistent: the
statement and Epistemic Status assert an infinite-horizon bound; the proof and
the *actual* tool (Markov on a fixed-time moment) deliver only a fixed-time
bound. Two prior audits flagged exactly this:
`audit-742613-SUPPLEMENT-PHASE-2-TRIAGE.md` §2 and
`audit-613842-FINAL-2026-04-25.md` F2 (the latter framed as
"integration debt / scope-honesty drift"). Both recommended **softening**
(restate (iii) as a fixed-time / finite-horizon tail). The peer adjudication
at `audits/AUDIT-WORKING-628401/adjudication.md` §F2 rejected the soften and
asserted a strengthening was available and standard (Itô–Lyapunov
supermartingale → Doob/Ville maximal inequality → "a genuine infinite-horizon
bound … strictly the claim the segment is reaching for and is *stronger*").
This spike tests that strengthening claim by doing the mathematics, not
inheriting any framing.

---

## 2. The setup (verbatim from the segment)

SDE form (segment line ~202):

$$d\delta = -F(\mathcal{T},\delta)\,dt + \sigma_w\,dW_t,\qquad W_t \text{ standard } n\text{-dim Wiener.}$$

$V(\delta) = \tfrac12\lVert\delta\rVert^2$. A2' on $\mathcal B_R$ (segment
line ~56): $\delta^\top F \geq \alpha\lVert\delta\rVert^2 = 2\alpha V$ for
$\lVert\delta\rVert \leq R$. Itô (segment line ~210):

$$dV = \big(-\delta^\top F + \tfrac n2\sigma_w^2\big)\,dt + \delta^\top\sigma_w\,dW_t,$$

so on $\mathcal B_R$ the generator satisfies
$\mathcal L V = -\delta^\top F + \tfrac n2\sigma_w^2 \leq -2\alpha V + \tfrac n2\sigma_w^2$.
Parts (i) (stopped Grönwall bound) and (ii) (mean-square persistence
$R^\ast_S = \sigma_w\sqrt{n/(2\alpha)} < R$) are **correct and unaffected** —
the defect is localized to (iii) and its propagation into the summary table
(line ~253) and Epistemic Status (line ~282).

The linear / Ornstein–Uhlenbeck case ($F = \alpha\delta$, A2' global, sharp)
is used throughout §3 as the exact benchmark: it is the case the segment
itself calls out (line ~246, "For the linear case (Ornstein-Uhlenbeck), the
stationary distribution is Gaussian and exact tail probabilities are
available"), and a non-exit *bound* claimed under "(A2') alone" must hold in
particular for OU. Failure in OU is failure of the general claim.

---

## 3. The strengthening attempt — worked in full

### 3.1 Route A — naive Dynkin on $V$ (drop the decay term)

Dynkin on the stopped process over $[0, t\wedge\tau_R]$:

$$\mathbb E[V(\delta_{t\wedge\tau_R})] = V(\delta_0) + \mathbb E\!\!\int_0^{t\wedge\tau_R}\!\!\mathcal L V\,ds \leq V(\delta_0) + \mathbb E\!\!\int_0^{t\wedge\tau_R}\!\!\big(-2\alpha V + \tfrac n2\sigma_w^2\big)\,ds.$$

Paths are continuous (Brownian-driven diffusion), so on $\{\tau_R \leq t\}$
the process is *at the boundary*: $V(\delta_{\tau_R}) = R^2/2$, giving
$\mathbb E[V(\delta_{t\wedge\tau_R})] \geq \tfrac{R^2}{2}P(\tau_R \leq t)$.
Dropping $-2\alpha V \leq 0$:

$$P(\tau_R \leq t) \leq \frac{2V(\delta_0) + n\sigma_w^2\,t}{R^2}.$$

**Linear in $t$; $\to\infty$.** Useless as $t\to\infty$. This is the
*sound but non-uniform* Khasminskii additive first-exit bound; it does not
contradict (iii)'s false reading, it simply cannot support it. The decay term
must be *kept*, not dropped, for any hope of a uniform bound — Route B.

### 3.2 Route B — the exponential supermartingale (the peer's proposed route)

This is precisely the route the peer adjudication and the originating spike
(`spikes/.integrated/spike-disturbance-model-split.md:141`) reach for. Define
$G(t) = e^{2\alpha t}V(\delta(t))$. On $[0,\tau_R]$, by Itô + A2':

$$dG = e^{2\alpha t}\big[\underbrace{(2\alpha V - \delta^\top F)}_{\leq\,0\text{ on }\mathcal B_R}dt + \tfrac n2\sigma_w^2\,dt + \delta^\top\sigma_w\,dW_t\big] \;\leq\; e^{2\alpha t}\tfrac n2\sigma_w^2\,dt + e^{2\alpha t}\delta^\top\sigma_w\,dW_t.$$

**$G$ is not a supermartingale**: the $+\,e^{2\alpha t}\tfrac n2\sigma_w^2\,dt$
term has strictly positive drift that *grows exponentially*. Ville's
inequality (the only tool giving a genuine *time-uniform*
$P(\sup_{t\geq 0}\cdot)$ bound) requires a **nonnegative supermartingale**.
Try to remove the bad drift by compensation:

$$S(t) = e^{2\alpha(t\wedge\tau_R)}V(\delta_{t\wedge\tau_R}) - \frac{n\sigma_w^2}{4\alpha}\big(e^{2\alpha(t\wedge\tau_R)} - 1\big).$$

Then $dS \leq e^{2\alpha t}\delta^\top\sigma_w\,dW_t$ on $[0,\tau_R]$ — $S$
*is* a supermartingale. **But $S$ is not nonnegative**: the subtracted
$\tfrac{n\sigma_w^2}{4\alpha}(e^{2\alpha t}-1)$ term dominates
$e^{2\alpha t}V$ whenever $V(\delta(t)) < \tfrac{n\sigma_w^2}{4\alpha}$ — i.e.
exactly inside the persistence basin, which is *most of the time* under the
persistence condition (that is the whole point of (ii): the RMS radius
$R^\ast_S = \sigma_w\sqrt{n/2\alpha}$ sits well inside $\mathcal B_R$, so
$V \ll \tfrac{n\sigma_w^2}{4\alpha}$ typically). Ville's inequality **does not
apply to a sign-indefinite supermartingale.** Doob's *maximal* inequality
needs a nonnegative sub/supermartingale and likewise fails here. There is no
nonnegative supermartingale dominating $V$ with a finite expected initial
value that yields a horizon-independent exit bound, because for additive
non-degenerate Brownian forcing the scale function of the diffusion is
*unbounded* (the OU scale density $\propto e^{\alpha u^2/\sigma_w^2}$): the
only bounded harmonic functions on $\mathbb R^n$ for this generator are
constants, so the gambler's-ruin / Lyapunov-exit machinery cannot certify
"stays inside forever with positive probability." This is the structural
obstruction, named.

### 3.3 The obstruction is real, not an artifact — direct simulation

Exact 1-D OU benchmark $dX = -\alpha X\,dt + \sigma\,dW$ (segment's own linear
case; $n=1$; A2' global and sharp). Monte-Carlo over increasing horizons,
started *at the origin* (deep inside, the most favorable initial condition),
under the **mean-square persistence condition (ii) holding**
($R^\ast_S = \sigma\sqrt{1/2\alpha} < R$):

| $\alpha$ | $\sigma$ | $R$ | $R^\ast_S$ | (ii) | $T{=}50$ | $T{=}200$ | $T{=}800$ | $T{=}3200$ | seg. const $\tfrac{n\sigma^2}{2\alpha R^2}$ |
|---|---|---|---|---|---|---|---|---|---|
| 1.0 | 0.3 | 1.0 | 0.21 | holds | 0.002 | 0.010 | 0.030 | **0.114** | 0.045 |
| 0.5 | 0.2 | 0.8 | 0.20 | holds | 0.020 | 0.074 | 0.276 | **0.720** | 0.063 |
| 1.0 | 0.5 | 1.0 | 0.35 | holds | 0.781 | 0.998 | 1.000 | **1.000** | 0.125 |

(Independent re-runs with different seeds / step sizes reproduce these to
within Monte-Carlo error; longer-horizon probe of the third regime:
$P(\sup_{[0,T]}>R)$ marches $0.006\to0.039\to0.299\to0.856$ for
$T = 10,100,1000,5000$ at $(\alpha,\sigma,R)=(0.5,0.2,0.8)$.)

Three things are now established with the OU benchmark, which the general
"(A2') alone" claim must in particular satisfy:

1. **$P(\tau_R < \infty) = 1$.** The ever-exit probability climbs
   monotonically toward 1 with horizon, even started at the origin, even with
   (ii) comfortably satisfied. OU is positively recurrent on $\mathbb R$ with
   unbounded stationary support; it exits any finite ball a.s. in finite
   time. The audits' core mathematics is **fully correct**: the object
   `P(\tau_R < \infty)` the segment writes equals **1**, not
   $\leq n\sigma_w^2/(2\alpha R^2)$.

2. **The segment's constant $n\sigma_w^2/(2\alpha R^2)$ is not a valid
   time-uniform / sup-over-all-time bound either.** Row 1 at $T=3200$:
   simulated $0.114 > 0.045$. Row 2 already at $T=200$: $0.074 > 0.063$.
   Row 3 (persistence (ii) *holds*, $R^\ast_S = 0.35 < 1$): simulated
   $P(\sup>R)\approx 1.0 \gg 0.125$. The would-be strengthened object —
   $P(\sup_{t\geq 0}\lVert\delta\rVert > R)$ — is **not** bounded by the
   segment's constant, nor by any horizon-independent constant $< 1$.

3. **No horizon-independent non-exit bound $< 1$ exists for this class.**
   Holding the *worst* admissible regime fixed (persistence (ii) satisfied,
   start at origin), $P(\sup_{[0,T]}>R)\to 1$ as $T\to\infty$. A
   horizon-independent constant $C<1$ with
   $P(\sup_{t\geq 0}\lVert\delta\rVert>R)\leq C$ provably **cannot exist**
   under the segment's stated GA-2S (zero-mean additive noise with
   $\mathbb E\lVert w\rVert^2 = \sigma_w^2$, no decay-at-boundary, no
   invariant-domain structure). This is exactly the alternative the
   742613-SUPPLEMENT §2 last bullet anticipated ("If the intended claim is
   true non-exit, add much stronger hypotheses … Standard additive Brownian
   noise will not support it") — now confirmed by working the mathematics,
   not merely asserted.

### 3.4 Where the peer adjudication's framing was wrong

The peer adjudication §F2 asserted the supermartingale
$V(\delta_{t\wedge\tau_R})$ "yields, via Doob's / Ville's supermartingale
maximal inequality … a genuine infinite-horizon bound … *strictly the claim
the segment is reaching for and is stronger*," called it "a textbook-lemma
strengthening," and predicted "it should not [fail] — it is standard
Khasminskii." That prediction is **mathematically incorrect**. The peer's
own cited object, $V(\delta_{t\wedge\tau_R})$, is *not* a supermartingale
(its drift is $\mathcal L V = -\delta^\top F + \tfrac n2\sigma_w^2$, which is
**positive** whenever $V < \tfrac{n\sigma_w^2}{4\alpha}$ — i.e. typically,
under persistence). Doob/Ville require a nonnegative super/submartingale; the
only compensation that restores the supermartingale property
(subtracting the running noise inflow) destroys nonnegativity (§3.2). Ville
on a sign-indefinite process is not a valid inequality. Khasminskii ch. 5's
genuine first-exit theorem is the **additive** bound of §3.1
($\propto V(\delta_0) + ct$), which grows without bound in the horizon —
*not* a time-uniform bound. The peer correctly diagnosed the *defect* and
correctly invoked the strengthen-before-soften discipline; the peer's
specific *prediction that the strengthening succeeds* did not survive the
mathematics. This is itself the value of running the spike rather than
inheriting the adjudication's framing: the strengthen-before-soften
escalation path explicitly anticipates state (3) — "you can come back and say
exactly why it can't be done and what insight *that* result means."

---

## 4. What IS true and rigorous (the corrected statement — a real result)

The strengthening having been exhausted, the honest discharge is not a bare
"soften it." It is the precise, true, *structurally meaningful* trio of
statements — two of which the segment already proves correctly, one of which
is the corrected (iii):

**(i) Stopped second-moment bound — already correct.** For all $t\geq 0$,
$\mathbb E[\lVert\delta_{t\wedge\tau_R}\rVert^2] \leq \lVert\delta_0\rVert^2 e^{-2\alpha t} + n\sigma_w^2/(2\alpha)$.
Exact; the stopping-time localization is sound; keep verbatim.

**(ii) Mean-square persistence — already correct.**
$R^\ast_S := \sigma_w\sqrt{n/(2\alpha)} < R \iff \alpha > n\sigma_w^2/(2R^2)$
places the *RMS* radius inside $\mathcal B_R$. Exact; keep verbatim. Note its
true meaning, sharpened by this spike: (ii) controls the **typical scale**,
not a sample-path containment guarantee — under (ii) the process spends
*most* of its time well inside $\mathcal B_R$, but additive noise still drives
rare excursions out, with probability 1 over an unbounded horizon.

**(iii′) Fixed-time / stationary tail — the corrected, true statement.**
For each fixed $t$ (and in the $t\to\infty$ stationary limit, where it is
sharpest):

$$P\big(\lVert\delta(t)\rVert > R\big) \;\leq\; \frac{\mathbb E[\lVert\delta_{t\wedge\tau_R}\rVert^2]}{R^2} \;\xrightarrow[t\to\infty]{}\; \frac{n\sigma_w^2}{2\alpha R^2}.$$

This is Markov's inequality on the (stopped) second moment — **exactly and
only** what the originating spike `spike-disturbance-model-split.md:159`
established, and it labeled it correctly there ("Model S gives a probabilistic
guarantee (exceeds $R^\ast_S$ sometimes, stays within $R$ with high
probability)" — a *fixed-time* statement, contrasted explicitly against Model
D's "hard guarantee"). The exact OU stationary tail
($\mathrm{erfc}(R/\sqrt{2v})$, $v=\sigma^2/2\alpha$) is far below the Markov
constant in every tested case (e.g. $0.00006 \ll 0.0625$), confirming (iii′)
is sound and loose-but-correct. **The number $n\sigma_w^2/(2\alpha R^2)$ in
the segment is right; the probabilistic object $P(\tau_R<\infty)$ attached to
it is wrong.** The defect is one of *object*, not of *constant* — which is
why the repair is a re-statement of what the bound governs, not a change of
the bound.

**(iv) Optional finite-horizon Khasminskii bound — a genuine, honest
strengthening over a bare fixed-time tail.** If a sample-path (sup-over-an-
interval) statement is wanted, the sound and correct one is the additive
first-exit bound of §3.1:

$$P\Big(\sup_{0\leq s\leq T}\lVert\delta(s)\rVert > R\Big) \;\leq\; \frac{\lVert\delta_0\rVert^2 + n\sigma_w^2\,T}{R^2}.$$

This *is* stronger than (iii′) for the regime it is useful in (it controls
the whole path on $[0,T]$, not a single time-slice), is rigorous under
"(A2') alone," and is Khasminskii ch. 5 verbatim — so it honors the
strengthen-first discipline with a real (if horizon-bounded) gain. Its
honest limitation, stated plainly: the bound **grows linearly in $T$** and
is vacuous for $T \gtrsim R^2/(n\sigma_w^2)$. There is no "persists forever
with high probability" reading; the structural reason is §3.2 (no bounded
non-constant harmonic function for the additive-noise generator).

### 4.1 Why the corrected statement is itself a result, not a retreat

The obstruction is the **same structural fact** the segment's own Discussion
("Two disturbance models," line ~296) and Interpretation (line ~244) already
lean on, now made sharp at the sample-path level:

- **Model D (bounded disturbance, Prop A.1):** positive invariance of
  $\mathcal B_R$ is a **hard, pathwise** guarantee — once inside, never
  exits, *deterministically* (the boundary-inward argument, segment line
  ~142). $P(\tau_R<\infty)=0$ honestly.
- **Model S (stochastic disturbance, Prop A.1S):** there is **no** pathwise
  containment. $P(\tau_R<\infty)=1$. Only the *typical scale* (RMS radius)
  and *fixed-time tail* are controlled. The
  $1/\alpha$ vs $1/\sqrt\alpha$ scaling asymmetry the segment already
  emphasizes ("Correction is less effective against noise than against
  drift," line ~244) has a **qualitative companion the segment was missing**:
  Model D gives pathwise-forever containment; Model S structurally *cannot*.
  Additive stochastic forcing does not merely weaken the *rate* of
  containment — it removes the *kind* of guarantee available (pathwise →
  distributional). This is the deeper content of the "these are not
  approximations to each other — they capture structurally different
  environments" claim (segment line ~296), and it directly sharpens the
  hand-off into `#result-structural-adaptation-necessity`: under Model S,
  region-exit is not a measure-zero pathology to be assumed away but a
  **certain eventual event** — the structural-adaptation trigger is
  *generic*, not exceptional, in stochastic environments. That is a
  first-class framework statement, not a caveat.

So completion-state (3) here yields a *positive* contribution: the corrected
(iii′)+(iv), plus the Model-D-pathwise vs Model-S-distributional **kind-of-
guarantee dichotomy**, is a sharper and more honest result than the false
(iii) ever was — and it strengthens, not weakens, the Model D/S architecture
the segment is built on.

---

## 5. Verdict

**Completion-state (3): sharp no-go + corrected-and-true statement that is
itself a real structural result.**

- The strengthening route (infinite-horizon / sup-over-all-time non-exit
  bound via Doob/Ville on the Itô–Lyapunov supermartingale) — the route the
  peer adjudication asserted as standard and the project's discipline
  *required* be attempted first — was **worked in full and genuinely fails**,
  for a precise, structural reason (no nonnegative supermartingale dominates
  $V$; the additive-noise generator has no bounded non-constant harmonic
  function; the recurrent OU benchmark exits any ball a.s.). This is a
  documented dead-end: future agents should not re-attempt a Doob/Ville
  infinite-horizon bound for additive-Brownian Model S — it provably does
  not exist.
- The audits' *mathematical observation* (fixed-time Markov $\not\Rightarrow$
  infinite-horizon non-exit; $P(\tau_R<\infty)=1$) is **correct and now
  rigorously confirmed**.
- The audits' / SUPPLEMENT's *recommended repair direction* (restate (iii)
  as a fixed-time tail) turns out to be the **correct discharge** — but only
  *because* the strengthening was exhausted first, and it should land as the
  precise (iii′)+(iv)+§4.1 package (a structural result), **not** as a bare
  one-line soften. The peer adjudication was right to reject a naive
  pre-strengthening soften and right on the discipline; its specific
  prediction that the strengthening succeeds was wrong, and saying so
  cleanly is the honest move.

---

## 6. Recommended segment-level disposition for `deriv-sector-condition.md`

(Recommendation only — per the parent's staging discipline this spike does
**not** edit the segment, `spikes/INDEX.md`, or any tracking file.)

1. **Prop A.1S statement, part (iii) (line ~194).** Replace the
   `P(\tau_R < \infty) \leq n\sigma_w^2/(2\alpha R^2)` clause with the
   **fixed-time / stationary** statement (iii′):
   $P(\lVert\delta(t)\rVert > R) \leq n\sigma_w^2/(2\alpha R^2)$ for each
   fixed $t$ (sharpest in the stationary $t\to\infty$ limit). The constant is
   unchanged — only the probabilistic object it governs. Optionally add (iv),
   the finite-horizon Khasminskii sup-bound
   $P(\sup_{[0,T]}\lVert\delta\rVert>R)\leq(\lVert\delta_0\rVert^2+n\sigma_w^2 T)/R^2$,
   explicitly flagged as horizon-growing (the honest sample-path companion;
   this is the genuine strengthening that *does* survive, so it belongs in
   the record).

2. **Proof paragraph "Stopping-time localization" (line ~242).** Replace
   "For (iii), standard tail estimates on the supermartingale
   $V(\delta(t))\mathbb 1_{\{t\leq\tau_R\}}$ yield the non-exit probability"
   with the correct derivation: Markov on the stopped second moment gives
   the fixed-time tail (iii′); a one-line note that the *infinite-horizon*
   ever-exit probability is **1** under additive Brownian forcing (no
   nonnegative supermartingale dominates $V$; the generator has no bounded
   non-constant harmonic function — this dead-end is recorded in
   `spikes/spike-stochastic-non-exit-strengthening-2026-05-16.md`), so no
   $P(\tau_R<\infty)<1$ bound exists and none is claimed.

3. **Summary table row "A.1S" (line ~253) and the "What Is Derived" row
   (line ~270).** Drop "non-exit probability $\geq 1 - n\sigma_w^2/(2\alpha R^2)$";
   replace with "fixed-time tail $P(\lVert\delta(t)\rVert>R)\leq n\sigma_w^2/(2\alpha R^2)$
   (stationary-sharp); no infinite-horizon non-exit bound exists for additive
   Model S — pathwise containment is a Model-D-only guarantee."

4. **Epistemic Status (line ~282).** A.1S remains *exact* — but the exactness
   is of (i) the stopped bound, (ii) mean-square persistence, and (iii′) the
   fixed-time tail. Remove "the non-exit probability (iii) follows from a
   Markov tail estimate on the supermartingale $V(\delta)$"; replace with the
   honest statement that (iii′) is a fixed-time Markov tail and that Model S
   admits **no** pathwise-forever containment (contrast Model D's positive
   invariance), citing the Model-D/Model-S kind-of-guarantee dichotomy of §4.1
   as the substantive content. "No implicit strengthening of A2' is required"
   stays true and can remain.

5. **Discussion "Two disturbance models" (line ~296) — recommended
   addition (the result-bearing part).** Add the §4.1 dichotomy explicitly:
   Model D gives **pathwise** (deterministic, forever) containment via
   positive invariance; Model S structurally **cannot** — additive stochastic
   forcing changes the *kind* of guarantee (pathwise → distributional), not
   just its rate, and makes region-exit a *generic eventual event*, which
   sharpens (not caveats) the hand-off into
   `#result-structural-adaptation-necessity` (region-exit under Model S is
   certain over an unbounded horizon, so the structural-adaptation trigger is
   generic in stochastic environments, not exceptional). This is the
   first-class result the cycle produced; it should land as a Discussion
   addition (and is a candidate `## Findings` entry for the segment).

6. **Downstream propagation (the 613842-F2 "integration debt" concern).**
   The summary-layer over-compression flagged at
   `result-sector-persistence-template.md`, `result-sector-condition-stability.md`,
   `result-persistence-condition.md` should inherit (iii′)'s fixed-time
   framing once it lands — same one-object correction, not a re-derivation.
   This is routing for the parent, tracked under the 613842-F2 / 742613-§2
   ledger entries; the corrected (iii′) is what propagates.

**Audit-finding disposition (for the parent's MANIFEST / ledger):** the
742613-SUPPLEMENT §2 and 613842-F2 findings are **valid and resolved by this
spike** — resolution is the (iii′)+(iv)+§4.1 package, reached *after* the
strengthening was honestly exhausted (state 3), **not** a pre-strengthening
soften. The peer adjudication's "route to a strengthening spike, the
maximal-inequality route is the lead" recommendation was the correct process
call; its substantive prediction (the maximal-inequality strengthening
succeeds) is **disconfirmed** and should be recorded as such so it is not
re-attempted.

---

## 7. Reproducibility

Numerical claims (§3.3) are Euler–Maruyama Monte-Carlo on the exact 1-D OU
case (segment's own linear benchmark), 3–8k paths, $dt\in[0.002,0.02]$,
horizons to $T=5000$, multiple seeds; the qualitative conclusions
($P(\tau_R<\infty)=1$; no horizon-independent non-exit constant $<1$; segment
constant violated as a sup-bound) are seed- and step-robust and are anyway
*proved* analytically in §3.1–3.2 — the simulation is corroboration of a
structural fact, not the basis for it. The OU recurrence /
no-bounded-harmonic-function argument is classical (e.g. Khasminskii 2012
ch. 3–4; the additive-noise scale function
$s'(u)\propto e^{\alpha u^2/\sigma_w^2}$ is unbounded, so the diffusion is
recurrent on $\mathbb R^n$ and exits every bounded set a.s.).

## Working Notes / dead-ends recorded

- **Dead-end A (Route B, §3.2):** compensating $e^{2\alpha t}V$ to restore the
  supermartingale property destroys nonnegativity; Ville/Doob inapplicable.
  Do **not** re-attempt a Doob/Ville infinite-horizon non-exit bound for
  additive-Brownian Model S — it provably does not exist (no bounded
  non-constant harmonic function for the generator).
- **Dead-end B (Route A, §3.1):** the genuine Khasminskii first-exit bound is
  additive in the horizon ($\propto V_0 + ct$); sound but vacuous as
  $T\to\infty$. This is the *correct* sample-path statement (iv) and is the
  honest strengthening over a bare fixed-time tail — but it is not, and
  cannot be made, horizon-uniform.
- **Not pursued (out of scope, flagged for completeness):** a *non-exit*
  result is recoverable only by changing the *model*, not the proof — e.g.
  noise vanishing at the boundary (state-dependent $\sigma_w(\delta)$ with
  $\sigma_w(\partial\mathcal B_R)=0$), a reflecting/invariant domain, or
  heavy-damping-at-boundary (super-linear $F$ near $\partial\mathcal B_R$).
  These are *different GA-2S assumptions*, not strengthenings of the present
  proof, and the segment's stated GA-2S (constant-variance additive Wiener)
  excludes them. If the project ever wants a true pathwise non-exit theorem
  for Model S, that is a new segment under a strengthened disturbance model —
  a candidate forward research item, not a repair of this one. (This matches
  the 742613-SUPPLEMENT §2 third bullet's prediction exactly.)
