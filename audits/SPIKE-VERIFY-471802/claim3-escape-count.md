# Claim 3 — Escape count: three genuine escapes; "horizon extension" provably collapses into the interventional escape (not a fourth)

## What the spike claims (§6)

Neutral-drift proposed four escapes (loop-interventional / horizon-extended /
higher-moment / architecture-instrumented). Spike's resolution:
- (a) **Loop-interventional** — genuine; intervention excites a
  similarity-fiber direction the on-policy law never excites.
- (b) **Higher-moment / out-of-regime** — genuine **only outside** the
  linear-Gaussian sub-scope; **provably void inside it** (Gaussian
  innovation has no information beyond 2nd order).
- (c) **Architecture instrumentation (white-box)** — genuine; same kind as
  I2 escape (i).
- (d) **Horizon extension under the original policy** — **collapses into
  (a)**: passive longer-horizon data under the same policy is more samples
  of the *same law*; the no-go is about the *law*, not sample size.
- Honest count: **three** genuine escapes, not four.

## Independent assessment

### (d) collapses — SOUND, and it is the right resolution of the open question

The neutral-drift spike itself flagged this as **the** sharp open question
(line 346: "is the horizon-extended-observation escape (b) genuinely
distinct from the interventional escape (a)…?"; line 444: "I suspect they
overlap in practice; the formal question is whether passive observation at
long horizons under the agent's *original* policy is Level-1 or Level-2
data"). So the spike is answering a question the prior artifact explicitly
left open — not inventing one.

The argument is forced and correct:

- Claim 1 established the on-policy observation **law** is identical for
  $A,A'$ (similarity-related). A longer observation horizon under the
  **same policy** draws more i.i.d.-in-the-stationary-sense samples from
  that *same* law. Identical laws ⇒ no statistic, at any sample size,
  separates them (this is just: if $P_A=P_{A'}$ as measures on the
  observation path space restricted to the on-policy channel, then no
  measurable function of arbitrarily long samples distinguishes them — a
  triviality once Claim 1's law-identity holds).
- Therefore passive horizon-extension under the on-policy law is **Level-1
  data** in the Pearl sense (it is more of the same observational
  distribution), and the only way longer horizons help is if the extended
  horizon **leaves the current regime** — but a regime change under a fixed
  policy is an *exogenous* event, and observing across it is either (i) out-
  of-regime data (the (b) family) or (ii) effectively interventional in
  character (a regime switch acts like a $do$ on the operating point) → the
  (a) family. So (d) is **void in-regime** and **a special case of (a)/(b)
  out-of-regime**. Not an independent escape.

This is consistent with canon: `#der-loop-interventional-access`
(`status: exact`) line 23 partitions identification strength by Regime A/B/C
and is explicit that *passive observation-only* (Regime C) does not yield
clean $do$-estimates; horizon length is nowhere a substitute for
interventional character. The collapse is the correct reading of canon's
own Level-1/Level-2 distinction. **Confirmed; tier exact for the collapse.**

### (b) void in linear-Gaussian sub-scope — SOUND

A stationary Gaussian process is fully determined by its mean and
autocovariance (second-order). Higher moments carry no extra information.
So if $A,A'$ match at the innovation spectrum (Claim 1), all higher moments
match in the linear-Gaussian sub-scope ⇒ higher-moment observation adds
nothing **inside** the sub-scope. Outside (AAT's $\beta$ / nonlinear
sub-scope) the neutral-drift spike §3 + `#der-interaction-channel-
classification` Case 4 kurtosis diagnostic give genuine higher-moment
discrimination. The spike's "(b) is a genuinely distinct escape only outside
the linear-Gaussian sub-scope, provably void inside it" is a **correct sharp
scope statement**, not a hedge. Confirmed; tier exact for the void-inside,
robust-qualitative for the distinct-outside (it leans on the nonlinear-
sub-scope kurtosis machinery which is itself robust-qualitative).

### (a) interventional and (c) white-box are genuine and distinct — SOUND

- (a): an intervention on the agent's input is a $do$ that excites
  off-on-policy-manifold directions; $TFT^{-1}$ and $F$ respond differently
  to a probe applied in a *fixed external basis* (the interventional
  response map is **not** similarity-invariant — a fixed-basis input/probe
  breaks the orbit symmetry because the input matrix transforms as
  $B\mapsto TB$ but the probe is applied in the un-transformed coordinates).
  This is canon-anticipated: `#der-loop-interventional-access` line 68
  explicitly reserves *Mode 3 — observer-on-agent-input* for "the
  architecture-within-behavior-class layer currently under triage" — i.e.
  exactly Object B. So escape (a) is not invented; canon already names the
  mode. Sound; tier exact that it breaks the orbit degeneracy,
  robust-qualitative for the precise machinery mapping (inherits
  `#der-loop-interventional-access` which is exact, but the *Object-B
  application* mapping is robust-qualitative).
- (c): direct read of the update rule / internal state trivially breaks the
  black-box scope and is structurally I2-escape-(i)-like (instrument the
  latent). Distinct from (a)/(b) in *what the observer must possess*
  (white-box access vs. interventional capability vs. moment data). Sound.

### Count = 3 — SOUND given the above

(a), (b)-outside-sub-scope, (c) are genuinely distinct in *what the observer
must do/have*; (d) is not independent. Three ≥ 2 ⇒ the floor-test's
≥2-distinct-escapes criterion (E4) passes with margin. Confirmed.

One observation the spike could have made and didn't (not a defect, a
completeness note): inside the linear-Gaussian sub-scope, (b) is void, so
*within the exact sub-scope* the genuinely-distinct escapes are (a) and (c)
— **two**, which still satisfies E4 (≥2). The "three" count is the
*general*-scope count (with (b) live outside linear-Gaussian). The spike's
"three" is correct as a general statement; a careful landing should note
that the **exact-sub-scope** escape count is two (still ≥2, E4 still
passes). This does not weaken anything — E4 needs ≥2, and both the
sub-scope (2) and general (3) counts clear it — but it is the precise
statement.

## Verdict on Claim 3

**Confirmed.** The escape analysis is sound and correctly resolves the open
question the neutral-drift spike explicitly flagged:
- (d) horizon-extension collapses into (a)/(b) (void in-regime): **exact**.
- (b) void in linear-Gaussian sub-scope, distinct only outside: **exact
  for void-inside**, robust-qualitative for distinct-outside.
- (a), (c) genuine and distinct: sound; (a) is canon-anticipated as
  `#der-loop-interventional-access` Mode 3.
- Count = 3 general (= 2 within the exact linear-Gaussian sub-scope); E4
  (≥2 distinct escapes) **passes** either way.

No overclaim found. The only refinement: state that the *exact-sub-scope*
escape count is 2, the *general* count is 3 — both clear E4; the spike's
"three" is the general count and is correct, but the sub-scope number
should be stated alongside the exact-sub-scope no-go for precision.

Loci opened: `#der-loop-interventional-access` (lines 23, 62–68 — Regime
A/B/C + the three deployment modes incl. Mode 3 = Object B, `status:
exact`); neutral-drift spike lines 346, 444 (the open (b)-vs-(a) question
this resolves); `#der-interaction-channel-classification` Case-4 reference
(nonlinear-sub-scope kurtosis, not re-derived — robust-qualitative inherited).
