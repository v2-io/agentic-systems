# SPIKE-VERIFY-471802 — Independent-verify gate on the Object-B substantive mathematics

**Spike under gate:** `spikes/spike-identifiability-floor-instance4-resolution-2026-05-18.md`
**Scope:** Object-B claims only (1–5). Object A (category error) is out of
scope — already independently confirmed from canon self-contradiction and
honesty-marked (`disc-identifiability-floor.md` lines 94–95, commit a7d6119).
**Posture:** strengthen-before-soften; §0 — truth re-derived against
canon-exact segments is the arbiter; the spike is a proxy interrogated, not
obeyed. Read-only; canon disposition is Joseph-reserved.
**I did not write the spike.**

---

## Bottom line

The spike's Object-B core is **substantively sound and is genuine new
mathematics the prior artifacts lacked** — but it is **not uniformly
"exact" as the spike's confidence ladder states.** Four of five claims
confirm with at most a tier-precision refinement; one (Claim 1, the
load-bearing construction) is **correct in its sharp form but overclaimed
as literally written, plus carries a transcription sign-slip.** No claim
refutes; no smuggle found in the load-bearing §7 linkage. The framing is
right. The corrections are repairs to a true result, not softenings of a
false one — strengthen-before-soften is satisfied (the result stands; the
loose clause is what gets tightened).

**Regression axis (§2a, mandatory, exclusion-pickaxe — Refinement 6):
CLEAR.** `git log -S` over `*/src/*` for every Object-B load-bearing string
(`similarity orbit`, `Kalman-Ho`, `Ho-Kalman`, `similarity-orbit`,
`similarity fiber`, `GL(n) similarity`, `TFT^{-1}`) returns **empty** — the
wrong-or-strong form *never entered canon at all* ⇒ regression-impossible.
The only `src/` hit for the Object-B vocabulary is this cycle's
honesty-mark banner (a7d6119), not a prior landing. Object B is a genuine
**orphan-side** derivation, not a forbidden regression-restoration.

---

## Per-claim ladder (with loci opened)

| # | Claim | Verdict | Tier (mine) vs spike's |
|---|---|---|---|
| 1 | Kalman-Ho similarity-orbit no-go, exact in linear-Gaussian sub-scope | **Confirmed with required scoping repair** | spike: exact-in-sub-scope. **Mine: exact-in-sub-scope *only after* repair**; as literally written, **overclaimed** (the "every moment of $\|\delta\|$" clause is false for the raw residual & self-contradicts the spike's own next sentence) + a Lyapunov-equation **sign slip** |
| 2 | Mechanism reduction: similarity-not-congruence; reduces to Instance-2 Fisher-null; 3rd member of rank-collapse {I1,I2,B} | **Confirmed in load-bearing core** | spike: exact throughout. **Mine: (1) exact; (2) exact-in-structure; (3) escape-irreducibility-=-Sylvester-"identical-to-I2" is robust-qualitative not exact (one notch hot); membership in {I1,I2,B} exact; (4) "repairs taxonomy" is a sound consequence but a Joseph-reserved disposition statement, not math** |
| 3 | Three genuine escapes; horizon-extension collapses into interventional | **Confirmed, no overclaim** | spike: exact for collapses. **Mine: agree exact** for (d)-collapse & (b)-void-inside; refinement: exact-sub-scope count is **2**, general count **3** — both clear E4 (≥2) |
| 4 | Fano anchor degenerates to vacuous at $I=0$; Kalman-Ho is the exact floor, Fano the finite-sample refinement | **Confirmed, exact** | spike: exact. **Mine: agree exact** — $I=0$ is a forced one-line consequence of Claim 1's law-identity; a properly *demonstrated* no-go; canon never committed to Fano (`#der-agent-opacity` l.156 "Open") |
| 5 | Regime-C confound IS Object B projected onto the disturbance-statistic coordinate, derived from C3 (`status: exact`) | **Confirmed; projection holds; nothing smuggled** | spike: exact. **Mine: projection-step exact; overall-linkage exact-in-sub-scope / robust-qualitative-in-general** (inherits Object B's own scope through the projection). The key anti-smuggle check passes: §7 rests on C3×ν + Claim 1, **not** on the refuted (AV) (S1)–(S4) theorem |

---

## The two concrete defects a landing must fix (Claim 1)

These are repairs to a true result; flag them in any landing plan.

1. **Overclaimed clause.** The boxed §4 claim says the stationary innovation
   process "hence every $(\alpha,R)$-summary, **every moment of
   $\|\delta\|$**, and the entire on-policy observation law — is identical."
   The "every moment of $\|\delta\|$" sub-clause is **false for the raw
   internal residual in a fixed external basis**: $\mathbb E\|\delta\|^2=
   \operatorname{tr}\Pi$ and $\operatorname{tr}(T\Pi T^\top)\ne
   \operatorname{tr}\Pi$ — and the spike *itself states this two sentences
   later* ("$\mathbb E\|\delta\|^2=\operatorname{tr}\Pi$ is not even
   similarity-invariant in general"). The claim is true for the
   **innovation/output observable** and any **similarity-invariant**
   summary. Correct scoping (the neutral-drift spike, line 319, already had
   it right): "identical at the innovation spectrum and on every
   similarity-invariant summary; the architectural d.o.f. = the $GL(n)$
   orbit, annihilated by the output map. $(\alpha,R)$ enters as the
   *spectral* / decay-rate invariant (Jordan-form-preserving), not a
   fixed-basis quadratic form." Under that scoping the no-go is genuinely
   exact-in-sub-scope.

2. **Lyapunov-equation sign slip.** The spike writes $F\Pi+\Pi F^\top+
   \sigma_w\sigma_w^\top=0$. For a covariance ($\Pi\succeq0$, $Q=\sigma_w
   \sigma_w^\top\succeq0$) this is sign-inconsistent. Correct equation:
   $F\Pi+\Pi F^\top=\sigma_w\sigma_w^\top$ (equivalently $(-F)\Pi+\Pi(-F)
   ^\top+\sigma_w\sigma_w^\top=0$, since the OU drift is $-F$). The
   *transformation law* $\Pi'=T\Pi T^\top$ the spike uses is correct under
   the corrected equation (re-verified). Conclusion unaffected, but a
   landing agent copying the display verbatim would import a sign-wrong
   Lyapunov equation into canon.

Neither defect touches the load-bearing recognition (the architectural
d.o.f. is the similarity orbit, invisible at the output; mechanism = I2
Fisher-null; Fano vacuous at $I=0$; Regime-C confound = the projection).
The result survives; the clause and the sign are what get tightened — the
strengthen-before-soften shape (a true result with a loose statement, not a
false claim to soften).

---

## What is genuinely new (the gate's actual question)

The mandate: confirm/refute "the new math the prior artifacts lacked."

- **Claim 1's closed-form construction** *is* new relative to canon and the
  siblings: the neutral-drift spike (lines 344–346, 392, 444) **explicitly
  deferred it** ("standard … but the tie to neutral drift needs laying
  out"; "non-trivial spike. Natural follow-up"); the triage was a
  Discussion-grade judgment, not a derivation. The verify-spike does supply
  the construction — correctly, modulo the two repairs above. Not stranded
  elsewhere (exclusion-pickaxe empty).
- **Claim 2's mechanism reduction** (Object B = Instance-2 Fisher-null
  along the $GL(n)$ fiber, *not* Sylvester-for-free, *not* new) is the
  genuine sharpening — the neutral-drift spike only reached
  "Jordan-form-preserving manifold" (line 319) without naming the
  mechanism. Sound; one strength-label (escape-irreducibility = I2
  "identically/exact") should read robust-qualitative.
- **Claim 5's projection** discharges, with an actual C3-grounded
  derivation, the "provably the same object" assertion the navigator
  (TODO:147, PROPOSALS §D.9) and the rho-recheck (line 296) were carrying
  as an unproved claim. The anti-smuggle check (does it lean on the refuted
  (AV) theorem? — no, it rests on C3 exact + Claim 1) passes.

The mandate's caution ("a 4th instance does not inherit Sylvester for
free") is **mathematically correct and the spike honors it** (Claim 2 (1):
generating action is similarity, not congruence — exact). The mandate's
"same object" linkage (CL-2) is **confirmed at the mathematical level**
(Claim 5), sub-scope-bounded.

---

## Framing assessment (mandate: "if the framing is wrong, say so")

The framing is **right**. The two-objects-under-one-ordinal resolution is
the correct shape; Object A out-of-scope-here and already-marked is correct
handling; Object B as a genuine floor with exact-in-Kalman-sub-scope /
robust-qualitative-general tiering, Instance-2 mechanism, three escapes,
Fano-as-finite-sample is a coherent and (with the Claim-1 repairs) sound
package. The single framing-level refinement: the spike's §8 confidence
ladder presents Object B's linkage and mechanism as flatly "exact"; the
honest ladder is **exact-in-linear-Gaussian-sub-scope, robust-qualitative-
in-general**, carried *consistently* through Claims 1, 2(3), and 5 (each
inherits the sub-scope boundary from Claim 1's law-identity). That is a
tier-honesty tightening, not a reframing — and it is exactly the
strengthen-before-soften posture: the result is real and strong; what is
owed is precise scope-marking, not a downgrade.

## Disposition signal (Joseph-reserved — not executed)

Object B is an `orphaned` (genuine, never-landed, regression-cleared)
substantive result. Per spike-routing §4 its landing is **substantial
segment-authoring** (a new appendix-grade no-go + the meta-segment
Sylvester-taxonomy repair + the CL-2 collapse), not a safe-mechanical move
→ written landing-plan + PRACTICA surfacing, Joseph-reserved (as the spike's
§9 already states). The independent-verify result: **the construction is
sound enough to land, conditional on the two Claim-1 repairs and the
tier-honesty pass (Object-B linkage/mechanism = exact-in-sub-scope /
robust-qualitative-general, not flat exact).** The canon disposition
(relabel Instance 4, install Object B, the CL-2 collapse of TODO:147 /
TODO:453 / the Instance-4 contradiction into one decision) remains
Joseph-reserved and is now *gated-clear on the math* with those repairs.
