# Claim 2 — Mechanism reduction: Object B is the Instance-2 mechanism, not Sylvester-for-free, not new; third member of rank-collapse {I1,I2,B}

## What the spike claims (§5)

1. Object B's *generating* group action is similarity $F\mapsto TFT^{-1}$,
   **not** Fisher congruence $\mathcal G\mapsto S^\top\mathcal G S$ — so it
   does **not** inherit Sylvester for free (the mandate's caution is right).
2. It is **not a new mechanism** either: the on-policy observation law
   factors through similarity-invariants, so the observation-channel Fisher
   information, as a form on the full realization manifold, is **rank-
   deficient — identically zero on the similarity-fiber tangent
   distribution**. That is *exactly* Instance 2's structure (Fisher null
   space along a structurally-forced indeterminacy manifold).
3. Its *escape*-irreducibility **is** Sylvester at one remove, identically
   to Instance 2 — so Object B is **mechanistically a member of the
   rank-collapse subclass {I1,I2,B}**, with the extra structure that the
   null direction is a Lie-group fiber.
4. This **repairs** canon's three-floor Sylvester taxonomy.

## Canon checked first-hand

**Instance 2 (`#deriv-edge-credence-dynamics` Prop B.7, lines 437–443,
`[Derived (cramer-rao-floor)]`):** Fisher info of the mixture
$\mu_j=\theta_C\theta_{j\mid C}+(1-\theta_C)\theta_{j\mid\neg C}$ at truth is
$$\mathcal F(\phi)=\frac{1}{\mu_j(1-\mu_j)}uu^\top,\quad
u=(\Delta_j,\theta_C,1-\theta_C),\ \Delta_j=p_{j\mid C}-p_{j\mid\neg C}.$$
Rank-1; **two-dimensional null space** = perturbations along the
indeterminacy manifold $\{\hat\phi:\hat\theta_C\hat p_{\mid C}+(1-\hat\theta_C)
\hat p_{\mid\neg C}=\mu_j\}$ — directions unobservable from a single binary
signal. Verified: this is genuinely a *Fisher-information rank-deficiency
along a structurally-forced indeterminacy manifold* (the manifold is the
mixture's level set; the channel cannot resolve within it).

**Sylvester-mechanism Discussion (`#disc-identifiability-floor` line 153):**
the rank-collapse subclass {I1 structurally, I2 cleanly} is irreducible
because the agent's only representational freedom is *coordinate/metric
change*, which acts on the information operator by **congruence**
$\mathcal G\mapsto S^\top\mathcal G S$, and **Sylvester's law of inertia**
fixes the zero-eigenvalue count under congruence. Instance 3 (composition)
is a *different* obstruction (non-invertible projection → Schur/memory
kernel). Canon explicitly states "the floors do not share one mechanism."

## Independent assessment of the four sub-claims

### (1) Generating action is similarity, not congruence — CONFIRMED

$F'=TFT^{-1}$ is a **similarity** action ($T(\cdot)T^{-1}$). Fisher
congruence is $S^\top(\cdot)S$. These are distinct group actions on
distinct objects (similarity acts on the *dynamics operator* $F$;
congruence acts on the *information/metric form* $\mathcal G$). Sylvester's
law is a statement about the congruence action on a symmetric form. So a
similarity-generated indistinguishability does **not** directly inherit
Sylvester. **The spike's sub-claim (1) and the mandate's caution are
mathematically correct.** No overclaim here.

### (2) Reduction to Instance-2 Fisher-null structure — CONFIRMED IN STRUCTURE, with a scoping nuance

The argument: parameterize the agent's realization manifold $\mathcal R$,
fibered over the transfer-function (= observable) manifold $\mathcal B$ by
the similarity group $GL(n)$ (the realization-to-transfer-function bundle —
this is the standard systems-theory picture: minimal realizations of a
fixed transfer function form a single $GL(n)$-orbit). By Claim 1, the
on-policy observation law depends on the realization $\theta\in\mathcal R$
**only through the base point** (the similarity-invariant transfer
function / output spectrum). Therefore the Fisher information of the
on-policy observation channel, pulled back to $\mathcal R$, satisfies:
$$\mathcal I_{\mathrm{obs}}(\theta)[v,v]=0\quad\text{for every }v\in
T_\theta(\text{fiber})=\mathfrak{gl}(n)\text{-orbit direction},$$
because the log-likelihood is constant along the fiber (the law does not
move), so its score vanishes there, so the Fisher form is identically zero
on the entire fiber-tangent distribution.

This is **structurally identical to Instance 2**: a Fisher form that is
rank-deficient, with the null space = the tangent of a *structurally-forced
indeterminacy manifold*. In I2 the manifold is the mixture level set
$\{\hat\theta_C\hat p_{\mid C}+(1-\hat\theta_C)\hat p_{\mid\neg C}=\mu_j\}$;
in Object B it is the $GL(n)$ similarity fiber. **The reduction holds**: the
mechanism *kind* is the same — channel-restricted score with a structural
null space — and it is **not a new mechanism**. The spike's central
mechanistic recognition is sound and is the genuine sharpening (the
neutral-drift spike, line 319, only got as far as "finite-dimensional
manifold of Jordan-form-preserving variations" without naming it as the
Fisher-null/Instance-2 mechanism).

**Nuance the spike states but I want to underline:** the I2 null space is
**2-dimensional within a finite-dimensional parameter vector**; the Object-B
null space is the tangent of a **Lie-group fiber** ($\dim$ generically up to
$n^2$, minus the realization's symmetry/centralizer). The spike does flag
this ("the rank-deficient direction is a Lie-group fiber rather than a
single indeterminacy manifold"). So "same mechanism" is accurate at the
*structural* level (Fisher-null-along-forced-manifold) but the manifold's
*geometry* is richer (a group orbit, not a level set). This is correctly
disclosed, not smuggled — the spike does not overclaim identity, it claims
*same mechanism kind, richer manifold*. Accept.

### (3) Escape-irreducibility IS Sylvester at one remove — PARTIALLY SOUND, MILD OVERREACH

The spike's move: distinguish the **generating** action (similarity $GL(n)$,
makes it a floor — not Sylvester) from the **escape** action (the agent
trying to *reparameterize its observation model* to refill the
rank-deficient observed-Fisher — this is congruence on the observed-Fisher,
hence Sylvester forbids it, exactly as Instance 2). Conclusion: Object B is
"mechanistically a member of the rank-collapse subclass {I1,I2,B}."

Assessment: the **escape-side** statement — "no reparameterization of the
observation model refills a rank-deficient observed-Fisher, by Sylvester" —
is correct *as a generic statement about rank-deficient Fisher forms* and is
genuinely the same escape-irreducibility argument I2 uses. So classifying
Object B with I1/I2 in a **rank-collapse subclass by escape-mechanism** is
defensible and is the right structural home.

However, two cautions where the spike reaches slightly past what is forced:

- **The "one remove" is doing real work and the spike states it almost as
  if free.** For I2, the *same* information operator that is rank-deficient
  is the one congruence acts on — Sylvester applies *directly*. For Object
  B, the rank-deficiency is generated by the similarity orbit (a different
  action on a different object), and the Sylvester argument applies to a
  *separate* hypothetical (an agent trying to reparameterize the observed
  Fisher). These are genuinely linked but the linkage is "both end up as
  rank-deficiency-of-a-Fisher-form, and rank-deficiency-of-a-Fisher-form is
  Sylvester-irreducible under reparameterization." That is true but it is a
  **weaker** unification than I2's (where it is one operator, one action).
  The spike's own framing ("at one remove", "with the *additional*
  structure") does disclose this. I would tier the **escape-irreducibility
  = Sylvester** sub-claim as **robust-qualitative**, not exact: it is the
  correct mechanism, but "Object B's escape-irreducibility is *literally*
  the I2 Sylvester argument" requires the extra step that the relevant
  escape really is observation-model reparameterization (and not, e.g.,
  enlarging the channel — which *is* an escape and is rank-augmentation,
  consistent with the picture, but shows the escape set is not a pure
  congruence orbit). The structural classification {I1,I2,B} is sound; the
  "exact, identical to I2" strength label is one notch hot.

### (4) "Repairs canon's Sylvester taxonomy" — SOUND AS A CONSEQUENCE, but it is a canon-disposition claim, not a math claim

If (2)–(3) hold, then canon's Discussion (which taxonomizes rank-collapse =
{I1,I2}, composition = {I3}, and silently omits the 4th) would, on the
corrected picture, read rank-collapse = {I1,I2,B}, composition = {I3}, with
Object A *not in the taxonomy at all*. That is a coherent and correct
*consequence* of the mechanism reduction. But "repairs canon" is a routing/
disposition statement (Joseph-reserved per the mandate and §9 of the spike);
mathematically the load-bearing content is just (2)+(3): **Object B's
mechanism is the I2 Fisher-null kind, so it belongs with the rank-collapse
subclass.** That much is sound (with (3) at robust-qualitative).

## Verdict on Claim 2

**Confirmed in its load-bearing core; one strength-label is one notch hot.**

- (1) similarity ≠ congruence, not Sylvester-for-free: **exact**, agrees
  with the mandate's caution. No overclaim.
- (2) reduces to the Instance-2 Fisher-null mechanism (channel-restricted
  score, structural null space along a forced manifold; here the $GL(n)$
  fiber): **exact in structure**, correctly disclosing that the manifold is
  a Lie-group orbit rather than a level set. This is the genuine sharpening;
  it is sound and is *not* in canon yet (canon's I2 calc is the rank-1
  mixture; the lift to the similarity fiber is new and correct).
- (3) escape-irreducibility = Sylvester "at one remove, identically to I2":
  **robust-qualitative, not exact** — the mechanism kind is right and the
  rank-collapse classification {I1,I2,B} is the correct structural home, but
  the I2 analogy is *one operator/one action* whereas Object B is
  *generated by similarity, escape-blocked by congruence-on-a-different-
  form*; calling that "identical to I2" and "exact" is a mild overreach. The
  honest tier for the classification-into-rank-collapse is exact; for the
  "literally the I2 Sylvester argument" it is robust-qualitative.
- (4) "repairs the taxonomy": sound as a consequence, but it is a
  Joseph-reserved canon-disposition statement, not additional mathematics.

Net: the mechanism reduction is **not Sylvester-for-free (correct), not a
new mechanism (correct), Instance-2-kind (correct)** — the spike's headline
is right and is the valuable content. The single calibration note: the
"exact / identical to Instance 2" label on the escape-irreducibility step
should be **robust-qualitative**; the structural membership in {I1,I2,B} is
exact.

Loci opened: `#deriv-edge-credence-dynamics` Prop B.7 (437–443, the rank-1
Fisher calc, `[Derived]`); `#disc-identifiability-floor` Discussion line 153
+ Findings line 190–196 (the Sylvester-mechanism statement, discussion-grade
meta with exact per-instance content); spike §5; neutral-drift spike line
319 (Jordan-form-preserving framing — the pre-sharpening state).
