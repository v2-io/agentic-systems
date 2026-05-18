# Independent-Verify Gate — ρ two-term identity / additivity claim

*SPIKE-VERIFY-087154. Read-only. Adjudicator ≠ spike author. The question:
do `#result-mismatch-decomposition` (GA-1) and `#deriv-sector-condition`
(Prop A.1S) actually force the two-term identity (2T) and the additivity,
as the recheck spike `spike-rho-structure-recheck-2026-05-18.md` claims —
or not? Settled by re-reading the canon segments first-hand, not the
spike's paraphrase (spike-routing §0).*

## Verdict in one line

**CONFIRM, with one bounded scope-correction the parent must carry into
the landing.** The two load-bearing claims hold against canon as the
recheck spike states them — but the spike's §4 *generalizes Prop A.1S
beyond what the segment establishes* (constant isotropic σ_w → arbitrary
state/model/policy-dependent Σ(δ,t)), and that generalization is an
unstated extension, not "verbatim re-reading" of a `status: exact`
segment. The core additivity and (2T) survive this correction intact;
the over-statement is in the *strength of the canon-pedigree the spike
claims for the general-Σ form*, not in the additivity conclusion itself.

## Loci opened first-hand (not via the spike's paraphrase)

- `01-aat-core/src/result-mismatch-decomposition.md` — full, incl. the
  GA-1 derivation step 3.
- `01-aat-core/src/deriv-sector-condition.md` — full, incl. Prop A.1S
  Itô step (lines 210–252), the "What Is Derived vs Chosen" table, and
  Corollary A.1S.1.
- `01-aat-core/src/hyp-mismatch-dynamics.md` — full (to test the spike's
  rate-lift provenance claim).
- `NOTATION.md` — ρ / w / σ_w / GA-2 / GA-2S rows.
- Structural sanity-check: `der-team-persistence`, `der-tempo-composition`,
  `der-adversarial-destabilization`, `deriv-critical-mass-composition`,
  `result-sector-persistence-template` (instantiation table, all 6 rows).
- Exclusion pickaxe across `01-aat-core/src/*.md` + `02-tst-core/src/*.md`
  for any environment-factor × agent-factor product form.

---

## Claim 1 — does `#result-mismatch-decomposition` (GA-1) force the
two-term identity? **CONFIRMED, exactly as claimed.**

The segment's Formal Expression is, `status: exact`:

  E‖δ_t‖² = E‖ô_t − ō_t‖²  +  E[Var(o_t | Ω_t, a_{t-1})]
            └ model error (reducible) ┘   └ obs noise (irreducible) ┘

Derivation step 3 (read verbatim): the cross term vanishes by GA-1
(ε_t conditionally independent of 𝒞_{t-1} given (Ω_t, a_{t-1})), and the
segment is explicit it is **orthogonality (uncorrelated), not
independence** — exactly the strength the spike's §3 claims ("not
approximately, not under (S1)–(S4)"). GA-1 is *already canon* (it is the
assumption this `status: exact` segment runs on), so the spike's central
claim — that the exact two-term split needs **only GA-1, none of
(S1)–(S4), no information geometry** — is faithful to the segment. The
spike does not overstate what `#result-mismatch-decomposition`
establishes; if anything its §3 is *exactly* the segment, rate-lifted.

GA-1 is not "weaker than claimed": the spike claims orthogonality-not-
independence and that is precisely what the derivation delivers. The
two-term form does not smuggle anything at the squared-mismatch level —
it *is* the canon identity.

### The one genuine gap on Claim 1 — the rate-lift, ν·E‖δ‖² = ρ²

The spike moves from the *per-step squared-mismatch* identity to a
*rate-level* ρ² by asserting (spike §2, §3):

  > "Multiply by the event rate ν … ρ² := ν·E‖δ_t‖² (this is exactly the
  >  Model-S reading ρ² = ν·σ_ν² used in `#hyp-mismatch-dynamics`)."

I opened `#hyp-mismatch-dynamics` to check this provenance claim
first-hand. **It is not in that segment.** `#hyp-mismatch-dynamics`
contains d‖δ‖/dt = −𝒯‖δ‖ + ρ(t) and the steady states ‖δ‖_ss = ρ/𝒯,
‖δ‖_rms = σ_w/√(2𝒯). There is **no** ρ² = ν·E‖δ‖² (nor ρ² = ν·σ_ν²)
identity anywhere in it. NOTATION confirms ρ / σ_w are the magnitude of
the *forcing term w* (the disturbance injected into δ̇), not a
rate-scaled functional of the *mismatch δ itself*. So the spike's
parenthetical "exactly … used in `#hyp-mismatch-dynamics`" is a
provenance overclaim of precisely the kind spike-routing §0 names
("'verified against <artifact>' is proxy in verification's clothing").

This does **not** refute (2T)'s additivity — additivity is a property of
the *operator applied to E‖δ‖²* and is preserved under multiplication by
any positive scalar ν, however ν is defined. It does mean: the *exact-
tier, canon-forced* object the gate can certify is the **per-step**
identity E‖δ‖² = (irreducible) + (reducible), GA-1, no caveat. The
*rate-level* ρ² = ν·E‖δ‖² rests on an event-rate bridge that is **not a
stated canon identity** in the segments the spike cites. For the
parent's landing this is a scope flag, not a defeater: land (2T) as the
GA-1 per-step identity (bullet-proof, canon-exact) and treat the
ν-multiplication as the standard fluid-limit rate convention
(`#hyp-mismatch-dynamics`'s ODE *is* a per-event fluid limit, line 54),
stated as a convention, not asserted as a pre-existing canon equation.

---

## Claim 2 — does `#deriv-sector-condition` (Prop A.1S) force the
additivity (Itô-generator linear in Σ)? **CONFIRMED for the canon
form; the spike's general-Σ extension is beyond what the segment
establishes.**

Prop A.1S proof, read verbatim (lines 212–228):

  d δ = −F dt + σ_w dW_t
  dV  = δᵀ(−F) dt + δᵀ σ_w dW_t + ½ σ_w² n dt
  (last term = ½ tr(σ_w² I_n) = (n/2) σ_w²; the Itô integral has zero
   expectation)

The spike §4 paraphrase — "the disturbance enters the certificate
dynamics **only** through the quadratic-variation term ½σ_w²n dt … the
drift cross-term δᵀσ_w dW_t is a zero-mean martingale increment and
contributes nothing in expectation" — is an **accurate, faithful**
reading of these exact lines. The structural conclusion that the
disturbance reaches the Lyapunov certificate **only** through the trace
of the diffusion covariance, additively, is correct and is what the
`status: exact` segment proves. So far: confirmed, not refuted.

### The bounded over-claim (the valuable part of running this gate)

The spike §4 then states the additivity is forced "with **no
independence** … Σ(δ,t) can be an **arbitrary state-dependent, model-
dependent, policy-dependent diffusion matrix**; the generator is *still*
linear in it" and frames the whole of §4 as a "**verbatim** re-reading
of `#deriv-sector-condition` Prop A.1S … already at `status: exact`."

Checked against the segment: **canon Prop A.1S uses a constant scalar
σ_w with isotropic diffusion Σ = σ_w² I_n** (line 212 SDE; line 222
tr(σ_w² I_n); the whole proof carries σ_w² as a constant through the
Grönwall step). The segment's own "Derived vs Chosen" table and
Epistemic Status scope the `exact` claim to *this* setup. The
**general state/model/policy-dependent Σ(δ,t)** case is **not derived in
the segment.** It is true mathematics (Itô's generator
ℒ = b·∇ + ½ tr(Σ∇²) is linear in Σ, and tr is additive over any
decomposition of Σ regardless of off-diagonals — elementary), but it is
the spike *extending* canon, not *reading* it. Calling it a "verbatim
re-reading of a `status: exact` segment" lends the general-Σ form a
canon pedigree the segment does not confer.

**Why this is a scope-correction, not a refutation.** The additivity
*conclusion the gate exists to certify* — that ρ does **not** factor
multiplicatively, that effective disturbance composes additively in the
rate/variance coordinate — holds at the canon (constant-σ_w) tier
already, and the general-Σ argument, while not in canon, is elementary
and correct on its own terms. The defect is **epistemic-labeling**: the
general-Σ statement should land tagged for what it is — an elementary
extension (Itô-generator linearity), `exact` *as mathematics* but **not
"already canon via `#deriv-sector-condition`"** — exactly the
integration-is-replacement / voice-discipline distinction. If the parent
lands §4 as the spike frames it ("verbatim, already `status: exact`"),
canon will assert a strength of pedigree it does not have. The honest
landing: the constant-σ_w additivity is canon-exact (Prop A.1S
verbatim); the general-Σ additivity is an exact elementary extension
*stated as such*, not laundered through Prop A.1S's `status: exact`
label.

---

## Structural sanity-check — is every live ρ^eff/ρ_ξ definition
additive (a sum, never env-factor × agent-factor product)?
**CONFIRMED, and stronger than the spike claims.**

`#result-sector-persistence-template`'s instantiation table, all six rows,
read first-hand:

| Segment | Effective ρ_ξ | Form |
|---|---|---|
| #result-persistence-condition | ρ | atomic |
| #schema-strategy-persistence | ρ_Σ | atomic (edge-invalidation rate) |
| #der-team-persistence | ρ_{i,env} + Σγ^adv 𝒯 − Σγ^coop 𝒯 | **sum** |
| #form-composition-closure | ε* ν_c | atomic (a product *rate×defect*, not env×agent) |
| #der-tempo-composition | ρ_ext + ε* ν_c | **sum** |
| #der-adversarial-destabilization | ρ_{B,base} + γ_A 𝒯_A | **sum** |
| #deriv-critical-mass-composition (C1) | ρ + γ𝒯 | **sum** |

Every decomposed effective disturbance is a **sum**. Zero instances of
an environment-factor × agent-factor product. The spike's C4 claim
("six additive, zero multiplicative") is accurate.

**Exclusion pickaxe (spike-routing §7 / Refinement 6 — the sharpest
clean signal).** `git`-grep-class search across `01-aat-core/src/*.md`
+ `02-tst-core/src/*.md` for any ρ_ext · f(ℳ) · g(π) product form
returns **empty**. The multiplicative form has **never existed in
canon** — not "added then corrected away," but never present. This is
sweep-immune and is the strongest possible regression-clean signal: the
parent's `status: false` mark on `#internal-external-decomposition`
removed the *only* place the multiplicative reading was ever asserted,
and re-landing it would *introduce* a category error the rest of canon
never committed (consistent with the spike's §6 and its regression-axis
clearance).

---

## Direct answers to the gate's framed sub-questions

- **GA-1 weaker than claimed?** No. The segment delivers orthogonality-
  not-independence exactly; the two-term per-step identity is canon-exact
  under GA-1 alone. Not a gap.
- **Itô argument needs an assumption not stated?** Yes — but bounded.
  The *canon* Prop A.1S is constant-isotropic σ_w² I_n. The spike's
  *general state/model/policy-dependent Σ(δ,t)* additivity is not derived
  in the segment; it is an elementary extension presented as a "verbatim"
  re-reading of a `status: exact` result. The mathematics is correct;
  the canon-pedigree claim is over-stated. Land it tagged as an
  extension, not as Prop A.1S verbatim.
- **Two-term form smuggles something?** Only the *rate-lift*
  ν·E‖δ‖² = ρ². The additive *split* smuggles nothing (it is the canon
  identity). The ν-bridge is asserted as canon ("used in
  `#hyp-mismatch-dynamics`") and is **not** in that segment — a
  provenance overclaim. The fix is presentational (state ν as the
  fluid-limit rate convention), not a defeater of additivity.

## Is the question itself mis-framed?

No — the gate's framing is sound and it caught exactly what it was built
to catch. One refinement worth surfacing to the parent: the gate asked
"confirm or refute the two-term identity *and that additivity*." Those
are two claims with **different canon pedigrees**, and the honest answer
is *split*: the additivity / no-multiplicative conclusion is rock-solid
and canon-forced at the constant-σ_w tier; the *exact, fully-general,
already-canon* phrasing the spike reaches for over-states the pedigree
on two sub-steps (the ν rate-lift; the general-Σ extension). A flat
"confirm" would have laundered those over-claims into canon under this
gate's authority — which is the §0 failure one level up. So: **confirm
the load-bearing conclusion; refuse the two pedigree over-claims; the
parent lands (2T)+§4 with those two items tagged for what they actually
are.**

## What the parent should carry into the landing

1. (2T) **per-step** identity E‖δ‖² = irreducible + reducible: land as
   **canon-exact under GA-1**, citing `#result-mismatch-decomposition`
   verbatim. Bullet-proof.
2. The **rate-level** ρ² = ν·E‖δ‖²: land the ν-multiplication as the
   **stated fluid-limit rate convention** (`#hyp-mismatch-dynamics` is a
   per-event fluid limit), **not** as a pre-existing canon identity.
   Delete the spike's "exactly … used in `#hyp-mismatch-dynamics`"
   provenance phrasing — it is false to that segment.
3. Constant-σ_w additivity (no multiplicative factorization): land as
   **canon-exact**, `#deriv-sector-condition` Prop A.1S verbatim.
4. General state/model/policy-dependent Σ(δ,t) additivity: land as an
   **elementary extension** (Itô-generator linearity in Σ; tr additive
   over any decomposition), `exact` *as mathematics*, **explicitly not**
   "already canon via Prop A.1S." Do not inherit Prop A.1S's
   `status: exact` label for the general case.
5. The multiplicative-no-go and the regression clearance: **confirmed
   independently** here — exclusion pickaxe empty across both `src/`
   trees; the parent's `status: false` mark is correct and not a
   regression.

Net: the canon landing the parent gates on this result may **proceed**,
with items 2 and 4 tagged at their true epistemic pedigree rather than
at the elevated pedigree the recheck spike's prose claims for them.
