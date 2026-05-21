# Spike: The True Structure of the Effective Disturbance Rate $\rho$ — Independent Re-derivation

> [!note]
> **Integration trail (2026-05-21):** §3 Regime-C confound now derived in canon as `#der-architecture-noidentifiability`'s no-go projected onto the disturbance-statistic coordinate — the §7 CL-2 linkage in the 2026-05-18 resolution spike supplied the projection proof (`#result-mismatch-decomposition` C3, $\Delta_{\text{agent}}^2$ as a functional of the agent's architecture; on-policy summary-only data confounds the model-class/policy split for exactly the similarity-orbit reason). The LIGHT exact core (two-term identity already forced by canon; one-line constitutive no-go) was previously landed in `#internal-external-decomposition` (CHANGELOG 2026-05-18); the HEAVY conditional 𝓜/π/cross refinement is now also discharged — same no-go, same escapes (Regime A interventional = `#der-architecture-noidentifiability` escape (a); Regime B functional-form = orbit-quotient, family (b)/(c)). PROPOSALS §D.9 CLOSED. CHANGELOG 2026-05-21. **Both LIGHT and HEAVY parts now discharged; spike eligible for `.integrated/` move once a re-verify confirms no orphan content remains in other sections.**

*Started 2026-05-18. Research spike. Not canon. Truth-establishing only;
routing/landing is a separate parent call (this spike does not move or edit
segments).*

**Mandate.** Settle, by re-derived mathematics resting on constitutive
structure + forced identities + elementary steps, what the *true* structure
of the effective disturbance / innovation rate $\rho$ in AAT is: does it
decompose multiplicatively $\rho = \rho_{\text{ext}}\cdot f(\mathcal M)\cdot
g(\pi)$, additively-in-variance $\sigma_\nu^2 = \sigma_{\text{opt}}^2 +
\Delta(\mathcal M) + \Delta(\pi)$, or something else, and under exactly what
conditions. Inputs interrogated (not obeyed): `spike-rho-factorization.md`
(an existing no-go), `spike-rho-additive-variance-strengthening-2026-04-24.md`
(a claimed *exact* (AV) theorem under (S1)–(S4)), and a parent agent's
`status: false` §4.1 mark on `01-aat-core/src/internal-external-decomposition.md`.

**Posture.** Strengthen-before-soften: try hardest to make the multiplicative
form *true* before concluding it cannot be; do not assert the
additive-variance form exact unless it derives exactly under explicitly
stated conditions; a no-go is as much a result as a success and must be
demonstrable, not asserted.

---

## 0. Verdict up front (then the work)

**The framing in both prior spikes is partially wrong, and correcting it
changes the answer.** They frame the contest as *multiplicative-in-rate*
($\rho = \rho_{\text{ext}} f g$) **vs.** *additive-in-variance* ($\rho^2 =
\rho_\star^2 + \Delta_{\mathcal M}^2 + \Delta_\pi^2 + \text{cross}$), and
declare additive-in-variance the winner under conditions (S1)–(S4). Both
horns are mis-pinned:

1. **The multiplicative no-go is real, sharper than stated, and I give the
   exact corrected form** — but it is a no-go about a *category error*, not
   a near-miss. $\rho_{\text{external}}$ as an agent-independent scalar is
   not under-derived; it is **not a well-formed object of the theory at
   all**, because the constitutive definition $\delta = o - \hat o$ makes
   $\rho$ a functional of the predictor. This is provable in one line from
   `#def-mismatch-signal` + `#result-mismatch-decomposition`, and it does
   not need three worked cases. The three cases in
   `spike-rho-factorization.md` are not wrong but they are *over-built and
   attack the weaker target*; the constitutive argument is the real no-go
   and it is **stronger and shorter**.

2. **The claimed *exact* (AV) theorem is not exact — it is exact only for a
   *degenerate* split, and the prior spike's own (S1)–(S4) do not deliver
   what it claims.** The honest exact statement is a **two-term**
   decomposition $\rho^2 = \rho_\star^2(\text{ref},\pi) +
   \Delta_{\text{agent}}^2$ that is forced by the live theory's own
   constitutive identity (`#result-mismatch-decomposition` lifted to the
   rate level under the same fresh-noise assumption already in canon — GA-1).
   The *three*-way split $\Delta_{\mathcal M}^2 + \Delta_\pi^2 + 2\chi$ is
   **not** exact under (S1)–(S4): (S3) (exponential-family /
   Pythagorean-projection) is doing the load-bearing work, and even granted
   it, $\Delta_{\mathcal M}^2$ and $\Delta_\pi^2$ are *not* separately
   identified — the prior spike's Step 4 silently re-absorbs the
   non-orthogonality into $\chi$ and then calls the identity "exact." It is
   exact as a *definition of $\chi$ by difference*, which is vacuous, not as
   a *decomposition*. This is the same "plausibility dressed as
   verification" shape the routing doc §0 warns about, one level up.

3. **The deepest result is structural and is *already in canon*, unrecognized
   as the answer to this question.** The live theory does not use a single
   $\rho$ that "admits a multiplicative reading or not." It uses
   $\rho_\xi$ — *effective* disturbance — and **every place the live theory
   decomposes $\rho_\xi$, it decomposes it additively in the rate/variance
   coordinate**, by forced identity, never multiplicatively
   (`#result-sector-persistence-template` instantiation table; `#der-team-
   persistence`; `#der-tempo-composition`; `#der-adversarial-destabilization`;
   `#deriv-critical-mass-composition`). The additive coordinate is not
   *chosen* and it is not merely "Bienaymé"; it is **forced by the Itô
   generator** of the Model-S mismatch SDE that is already canon in
   `#deriv-sector-condition`. That is a *fourth, cleaner* characterization
   than any of (R-F)/(R-V)/(R-KL), and it makes the multiplicative question
   not "false" but **type-incorrect**: $\rho$ is the square root of an
   additive quadratic-variation functional; asking it to factor
   multiplicatively is asking $\sqrt{\,\cdot\,}$ of a sum to be a product.

4. **Strengthen-first did find one regime where a multiplicative form is not
   merely "native to classical probability" but *forced by AAT's own
   structure*: the strategic layer.** `#deriv-edge-update-natural-parameter`'s
   log-odds coordinate gives a *genuinely AAT-internal* multiplicative
   structure for $\rho_\Sigma$ (strategic disturbance) — but it is
   multiplicative *per edge in (rate × per-event variance)*, and additive
   *across edges*, exactly mirroring the additive-by-Itô-generator pattern.
   This is the one place the multiplicative intuition has real AAT teeth,
   and it is **still not** $\rho_{\text{ext}}\cdot f(\mathcal M)\cdot g(\pi)$.
   The prior spikes saw this (their §4) but mis-filed it as "not specific
   to AAT"; under the live `#deriv-edge-update-natural-parameter` it *is*
   AAT-structural. This is a strengthening the prior no-go missed.

**On the parent's `status: false` mark.** It is **correct and not a
regression** — the segment was asserting the refuted multiplicative split as
canon. But the segment's KNOWN-FALSE banner and the navigator (TODO:147,
TODO:438, PROPOSALS §D.9) describe the replacement as "(AV) variance-additive
theorem under (S1)–(S4)" — i.e. they queue the *non-exact three-way (AV)* as
the corrected truth. **That is a second, subtler §4.1-class problem**: the
replacement-of-record is itself not exact as stated. The corrected truth is
the *two-term* identity in §3 below (exact, by GA-1, no (S1)–(S4) needed) plus
the *additive-by-Itô-generator* structural statement in §4 (exact, already
canon). The three-way $\mathcal M$/$\pi$ split is *conditional*, not exact,
and its honest home is mediation analysis (Regime A/B), exactly as the
identifiability-floor pattern already says — not a clean theorem under
(S1)–(S4).

Confidence: **exact** for §2 (the category-error no-go) and §3 (the two-term
identity), each one-step from canon; **exact** for §4 (the
additive-by-generator statement is a re-reading of `#deriv-sector-condition`
already at `status: exact`); **robust-qualitative** for §5 (the strategic-layer
multiplicative sub-structure — it is forced per-edge but the cross-edge
aggregation's independence is a modeling assumption); **conditional** for the
three-way split being anything more than a definition-by-difference.

---

## 1. Locating the question on constitutive structure

Per routing §0, the only thing that settles this is re-derived mathematics
on constitutive structure. The constitutive facts (read first-hand from
`src/`, not from the spikes or NOTATION):

**C1 — what $\delta$ is (`#def-mismatch-signal`, `status: axiomatic`).**
$\hat o_t = \mathbb E[o_t \mid M_{t-1}, a_{t-1}]$ and $\delta_t = o_t - \hat
o_t$. This is *definitional*: the residual the model does not predict.
"Given any model that predicts and any observation that arrives, their
difference exists. The mismatch signal is not an additional assumption."

**C2 — what enters the persistence machinery (`#deriv-sector-condition`,
`status: exact`).** The mismatch evolves by
$$\frac{d\delta}{dt} = -F(\mathcal T,\delta) + w(t),\qquad
\text{Model S: } d\delta = -F(\mathcal T,\delta)\,dt + \sigma_w\,dW_t,$$
with $\|w(t)\|\le\rho$ (Model D) or $\mathbb E\|w(t)\|^2=\sigma_w^2$ (Model S).
$\rho$ / $\sigma_w$ is the *disturbance* — the forcing term on the residual.

**C3 — the exact instantaneous identity (`#result-mismatch-decomposition`,
`status: exact`).** Under the fresh-noise assumption **GA-1** ($\varepsilon_t$
conditionally independent of $\mathcal C_{t-1}$ given $(\Omega_t,a_{t-1})$),
which is *already canon*:
$$\mathbb E[\|\delta_t\|^2]
= \underbrace{\mathbb E[\|\hat o_t - \bar o_t\|^2]}_{\text{model error (reducible)}}
+ \underbrace{\mathbb E[\operatorname{Var}(o_t\mid\Omega_t,a_{t-1})]}_{\text{obs noise (irreducible)}},\qquad
\bar o_t = \mathbb E[o_t\mid\Omega_t,a_{t-1}].$$
The cross term vanishes *by orthogonality*, derived in canon, not assumed
here.

**C4 — how the live theory actually uses the disturbance
(`#result-sector-persistence-template`, `status: exact`, instantiation
table).** Every persistence-flavored result instantiates the *same* Lyapunov
argument with its own "effective disturbance" $\rho_\xi$, and in **every**
instantiation that decomposes it, the decomposition is **additive** in the
rate coordinate:
- `#der-team-persistence`: $\rho_i^{\text{eff}} = \rho_{i,\text{env}}
  + \sum_j\gamma^{\text{adv}}_{j\to i}\mathcal T_j
  - \sum_j\gamma^{\text{coop}}_{j\to i}\mathcal T_j$
- `#der-tempo-composition`: $\rho_{\text{ext}} + \varepsilon^\star\nu_c$
- `#der-adversarial-destabilization`: $\rho_{B,\text{base}}+\gamma_A\mathcal T_A$
- `#deriv-critical-mass-composition`: $(\alpha-C)R \gt \rho+\gamma\mathcal T$

This is the live theory's *own* answer to "how does effective disturbance
decompose," and it is unanimous and additive. No segment anywhere writes
$\rho_\xi$ as a product of an environment factor and agent factors. The
multiplicative form has **no instance in canon**; the additive form has
**six**.

These four facts already settle most of the question. The prior spikes did
not lean on C4 at all — they treated the question as open and worked it from
scratch through Kalman/Beta-Bernoulli/OU. That is the over-build: the live
theory had already committed.

---

## 2. The multiplicative no-go is a *category error*, provable in one step
(stronger than the prior three-case argument)

**Claim (no-go, exact).** Under C1 + C3 (both canon), there is no
agent-independent scalar $\rho_{\text{external}}$ such that
$\rho^2 = \rho_{\text{external}}^2\cdot f(\mathcal M)\cdot g(\pi)$ with
$\rho_{\text{external}}^2$ a property of the environment alone and $f,g$
properties of the model class and policy alone.

**Derivation (one step, by contradiction on the constitutive definition).**
By C3, $\mathbb E\|\delta_t\|^2 = \mathbb E\|\hat o_t-\bar o_t\|^2 +
\mathbb E[\operatorname{Var}(o_t\mid\Omega_t,a_{t-1})]$. Multiply by the event
rate $\nu$ to get the rate-level disturbance power
$\rho^2 := \nu\,\mathbb E\|\delta_t\|^2$ (this is exactly the Model-S reading
$\rho^2 = \nu\sigma_\nu^2$ used in `#hyp-mismatch-dynamics`). Then
$$\rho^2 = \underbrace{\nu\,\mathbb E\|\hat o_t-\bar o_t\|^2}_{=:A,\ \text{depends on }\hat o_t,\text{ hence on }\mathcal M}
\;+\;
\underbrace{\nu\,\mathbb E[\operatorname{Var}(o_t\mid\Omega_t,a_{t-1})]}_{=:B,\ \text{depends on env and on }a_{t-1}\text{ hence }\pi}.$$
$A$ is identically zero iff $\hat o_t = \bar o_t$ for (almost) all $t$ — i.e.
iff the model's predictive mean equals the *true* conditional mean. So $A$ is
a strictly positive functional of $\mathcal M$ whenever the model is
misspecified, and $A\to 0$ as $\mathcal M\to\mathcal M_{\text{opt}}$.

Now suppose for contradiction the product form holds:
$\rho^2 = \rho_{\text{ext}}^2 f(\mathcal M) g(\pi)$ with
$\rho_{\text{ext}}^2$ independent of $\mathcal M$. Take the limit
$\mathcal M\to\mathcal M_{\text{opt}}$ at fixed environment and fixed $\pi$.
On the additive side, $A\to 0$, so $\rho^2\to B = \nu\,\mathbb E[\operatorname{Var}]$,
a **strictly positive** environment/policy quantity (positive whenever
observation noise is non-degenerate — C3 says exactly this). On the product
side, $\mathcal M\to\mathcal M_{\text{opt}}$ drives $f(\mathcal M)\to f_{\max}$
(a constant), so $\rho^2\to\rho_{\text{ext}}^2 f_{\max} g(\pi)$. For these to
agree for **all** environments simultaneously we would need
$\rho_{\text{ext}}^2 = B/(f_{\max} g(\pi))$ — but $B$ varies with the
environment's *observation-noise* structure while, in any other environment
with the *same* $\rho_{\text{ext}}$ (whatever that scalar is supposed to be)
but different process-vs-observation noise split, $B$ differs. A single
scalar $\rho_{\text{ext}}^2$ cannot equal $B/(f_{\max}g(\pi))$ across
environments that share it by hypothesis but differ in their
noise-decomposition. **Contradiction.** $\square$

**Why this is stronger than the prior spike's argument.** The prior spike
(`spike-rho-factorization.md` §§3–5) ran three structured cases (Kalman,
Beta-Bernoulli, controlled OU) to exhibit the failure *empirically per case*.
That is genuinely more work and *weaker*: it shows the product fails *in
those cases*, inviting "but maybe another case…". The argument above shows
the product fails **from the constitutive definition of $\delta$ alone**: the
moment you define $\delta = o-\hat o$, the disturbance power inherits a
$+\,A(\mathcal M)$ term that vanishes with model quality, and *no* scalar
"environmental volatility" can carry a term that disappears when the
**agent** improves. The environment did not change; the agent did. The prior
spike's own §2 ("$\rho$ is agent-conditional… $\rho_{\text{external}}$ is not
well-defined without a reference agent") *states* this — and then under-uses
it, going on to three cases instead of closing in one line. **Per
strengthen-before-soften's landing half: the no-go's worked argument is this
one-step constitutive contradiction, not the three-case survey.** The survey
is reasoning-trail, not the proof.

**This is not a near-miss to be repaired by tightening $\rho_{\text{ext}}$.**
The object $\rho_{\text{external}}$ "the environment's volatility,
agent-independent" is not under-specified — it is **not a function of the
right variables**. By C1 it *cannot* be agent-independent because $\delta$ is
defined *through* $\hat o$. Asking for it is a category error, the same way
asking for "the residual of a regression, independent of the regressors" is.
The honest replacement is not a better factorization; it is the *two-term
identity that is actually exact*, next.

---

## 3. The exact corrected form: a *two-term* identity, forced by GA-1
(not the three-way (AV) the navigator queues)

**Claim (exact, no (S1)–(S4) needed).** Under GA-1 (already canon — the same
fresh-noise assumption `#result-mismatch-decomposition` runs on) and the
Model-S reading $\rho^2 := \nu\,\mathbb E\|\delta_t\|^2$:
$$\boxed{\;\rho^2 \;=\; \rho_\star^2(\text{env};\pi)\;+\;\Delta_{\text{agent}}^2(\mathcal M;\pi,\text{env})\;}\tag{2T}$$
where
- $\rho_\star^2(\text{env};\pi) := \nu\,\mathbb E[\operatorname{Var}(o_t\mid
  \Omega_t,a_{t-1})]$ — the **irreducible** rate: the disturbance power even
  the Bayes-optimal predictor cannot remove, *evaluated along the
  $\pi$-induced state/action distribution*. Positive whenever observation
  noise is non-degenerate (C3).
- $\Delta_{\text{agent}}^2(\mathcal M;\pi,\text{env}) := \nu\,\mathbb
  E\|\hat o_t-\bar o_t\|^2$ — the **reducible** rate: the squared gap between
  the model's predictive mean and the true conditional mean, $\ge 0$, zero
  iff the model is correctly specified on the realized distribution.

**Derivation.** Immediate from C3 × $\nu$. The cross term is *exactly* zero —
not approximately, not under (S1)–(S4) — by the orthogonality already proved
in `#result-mismatch-decomposition`'s derivation step 3 (GA-1). $\square$

**Status: exact**, and strictly stronger than the prior spike's "(R-V) is
supported by bias-variance decomposition" hand-wave *and* than the
strengthening spike's "(AV) exact under (S1)–(S4)" — because (2T) needs
**none** of (S1)–(S4). It rests only on GA-1, which AAT already assumes for
`#result-mismatch-decomposition` (a `status: exact` segment). The prior
strengthening spike reached for Amari–Nagaoka Pythagorean projection (its S3)
to get a *three*-way split; the two-way split needs no information geometry
at all — it is the canon mismatch identity, rate-lifted.

**Why the three-way split is *not* exact (the buried defect).** The
strengthening spike's (AV),
$\rho^2 = \rho_\star^2 + \Delta_{\mathcal M}^2 + \Delta_\pi^2 + 2\chi$,
splits the single reducible term $\Delta_{\text{agent}}^2$ into a
model-attributable part, a policy-attributable part, and a cross term. Its
Step 4 *defines* $2\chi := \Delta_{\mathcal M}^2(\mu_\pi) -
\Delta_{\mathcal M}^2(\mu_{\pi^\star(\mathcal M)})$ — i.e. $\chi$ is defined
as exactly the discrepancy that makes the equation balance. An identity that
holds because one of its terms is *defined as the residual that makes it
hold* is **vacuously exact** (it is the statement $X = a + b + (X-a-b)$). It
is not a decomposition theorem; it is a definition. The spike then writes
"**Each term is derived; (AV) holds exactly under (S1)–(S4). $\square$**" —
this is the routing §0 failure mode one level up: a definitional rearrangement
asserted with theorem-weight. Granting (S3) gives the *interpretation* of
$\chi$ as a state-distribution mediation term (Imai et al. 2010) and gives
Pythagorean orthogonality *only when the model class is e-flat and the policy
shift is along an m-geodesic* — which is exactly the structured case, not the
general one. So the honest tiering is:

| Form | Status | Conditions |
|---|---|---|
| (2T) two-term: $\rho^2 = \rho_\star^2 + \Delta_{\text{agent}}^2$ | **exact** | GA-1 only (already canon) |
| three-way $\rho_\star^2 + \Delta_{\mathcal M}^2 + \Delta_\pi^2 + 2\chi$ | **conditional** | $\chi$ identified only under Regime A (interventional) or Regime B (functional-form); under Regime C it is confounded — `#disc-identifiability-floor` Instance, exactly |
| multiplicative $\rho_{\text{ext}}^2 f g$ | **false** (category error) | none — §2 |

This is the integration-is-replacement discipline applied to the *prior
spike's own claim*: its "(AV) exact under (S1)–(S4)" should be **deleted and
replaced** by "(2T) exact under GA-1; the finer $\mathcal M$/$\pi$ split is
conditional (mediation, Regime A/B), confounded under Regime C." The
navigator (TODO:147 "(AV) variance-additive theorem"; PROPOSALS §D.9 "the
variance-additive (AV) successor theorem under (S1)-(S4)") currently records
the *conditional* thing as the exact corrected truth. That is the second
§4.1-shaped issue flagged in §0.4 — surfaced here for the parent, not edited.

---

## 4. The deepest result: the additive coordinate is *forced by the Itô
generator*, and it is already canon (this is the real answer)

The prior strengthening spike spent its §5 asking whether the additive
coordinate is "forced by a Cauchy functional equation" (→ a fourth
`#disc-additive-coordinate-forcing` primary instance) and concluded "no, it's
just Bienaymé's identity, adjacent like the Lyapunov quadratic." That
conclusion is correct *as far as it goes* but it **misses the actual forcing
mechanism, which is sharper and is already proved in canon**.

**Claim (exact — a re-reading of `#deriv-sector-condition`, `status:
exact`).** In Model S the mismatch obeys $d\delta = -F\,dt + \sigma_w\,dW_t$.
Apply Itô to $V=\tfrac12\|\delta\|^2$ — *this is canon, `#deriv-sector-
condition` Prop A.1S, verbatim*:
$$dV = \delta^\top(-F)\,dt + \delta^\top\sigma_w\,dW_t + \tfrac12\sigma_w^2 n\,dt.$$
The disturbance enters the *certificate dynamics* **only** through the
quadratic-variation term $\tfrac12\sigma_w^2 n\,dt$ — i.e. through
$\sigma_w^2$, additively, as the trace of the diffusion's instantaneous
covariance. The drift cross-term $\delta^\top\sigma_w\,dW_t$ is a zero-mean
martingale increment and contributes nothing in expectation
(`#deriv-sector-condition` says exactly this). Therefore the *only* way the
environment, the model, and the policy can affect the persistence-relevant
disturbance is through their contribution to the **instantaneous covariance
of the innovation**, and instantaneous covariances of the residual's driving
noise **add** — this is not Bienaymé as an external identity, it is the Itô
generator: the second-order term of the generator $\mathcal L =
b\cdot\nabla + \tfrac12\operatorname{tr}(\Sigma\nabla^2)$ is **linear in
$\Sigma$**. Linearity of the generator in the diffusion matrix is the
forcing. $\square$

**This is *stronger* than "Bienaymé / adjacent like Lyapunov."** Bienaymé
("variances of independent things add") needs an independence hypothesis the
prior spikes correctly worried about (model and policy are *not*
independent — §5 of `spike-rho-factorization`). The Itô-generator argument
needs **no independence**: $\Sigma(\delta,t)$ can be an arbitrary
state-dependent, model-dependent, policy-dependent diffusion matrix; the
generator is *still* linear in it, so whatever $\Sigma$ decomposes into
(however correlated the pieces), the *persistence-relevant scalar* is
$\operatorname{tr}\Sigma$, which is additive over **any** additive
decomposition of $\Sigma$ — correlated or not. The correlations live inside
the off-diagonal of each piece and *never reach the certificate*, because
$V=\tfrac12\|\delta\|^2$ only sees the trace. So:

> The multiplicative question is **type-incorrect**, definitively. $\rho$ is
> (the square root of $\nu$ times) the trace of an instantaneous covariance
> the Lyapunov certificate integrates. Covariances enter the certificate
> additively because the Itô generator is linear in the diffusion matrix.
> Asking $\rho$ to factor as $\rho_{\text{ext}}\cdot f\cdot g$ is asking
> $\sqrt{\operatorname{tr}(\Sigma_1+\Sigma_2+\dots)}$ to equal a product —
> false for the same reason $\sqrt{a+b}\ne\sqrt a\sqrt b$, but now with the
> additive structure *derived from the canonical certificate dynamics*, not
> posited.

This also explains, structurally, **why the live theory's six effective-
disturbance instantiations (C4) are all additive**: they are all the *same*
Itô/Lyapunov certificate (`#result-sector-persistence-template`) with
different $\Sigma$-contributions, and the certificate is linear in $\Sigma$.
Team coupling, tempo closure-defect, adversarial coupling, critical-mass —
each adds a covariance contribution to the residual's driving noise and the
certificate sums their traces. The additive form is not a modeling choice
repeated six times; it is **one forced consequence of the canonical Model-S
certificate, instantiated six times**. That is a genuinely load-bearing
structural recognition the prior spikes did not reach because they never
used C4.

**Placement w.r.t. `#disc-additive-coordinate-forcing`.** The prior
strengthening spike's "adjacent family member, not a Cauchy-FE primary
instance" verdict survives but is *under-stated*. It is adjacent to the
Lyapunov-quadratic case **for the same reason** and *by the same mechanism*:
the quadratic coordinate is matched to the certificate, and the certificate's
generator is linear in $\Sigma$. So the right statement is not "adjacent
because Bienaymé" but "**the same adjacency as the Lyapunov quadratic,
because it *is* the Lyapunov quadratic's generator term**." This tightens the
meta-segment's taxonomy rather than just adding a row.

---

## 5. Strengthen-first: the one place a multiplicative form has real AAT
teeth — the strategic layer (a strengthening the prior no-go mis-filed)

Mandate: try hardest to make multiplicative *true* under tightened
assumptions before concluding it cannot be. The honest finding:

**In the epistemic layer ($\delta = o-\hat o$): no.** §2 and §4 close this
definitively — type-incorrect, not under-derived.

**In the strategic layer ($\delta_\Sigma$, edge-credence): a real
AAT-internal multiplicative structure exists per-edge, additive across
edges.** `#deriv-edge-update-natural-parameter` (canon) gives the log-odds
update $\lambda^{\text{post}}_{ij}=\lambda^{\text{prior}}_{ij}+\ell(y)$. The
per-edge strategic-disturbance rate is, by the same Itô/quadratic-variation
reading applied to the *log-odds* coordinate:
$$\rho_{\Sigma,e}^2 \;=\; \underbrace{\nu_{\text{edge},\pi}(e)}_{\text{policy: visit rate}}\;\cdot\;\underbrace{p^\star_e(1-p^\star_e)\,\ell_{0,e}^2}_{\text{environment: per-event innovation variance at true }p^\star}.$$
This **is** a forced two-factor product (rate × per-event variance) and the
rate factor *is* a pure policy quantity ($\nu_{\text{edge},\pi}$, which edges
$\pi$ visits and how often — forced by `#post-causal-structure`'s temporal
ordering) while the variance factor *is* a pure environment quantity
($p^\star$). The prior spikes saw this (their §4.2–4.3) and dismissed it as
"structural to any additive-Poisson-driven innovation, not specific to AAT."
**That dismissal is wrong under the live theory.** It *is* AAT-structural:
`#deriv-edge-update-natural-parameter` is the segment that forces the log-odds
coordinate (a `#disc-additive-coordinate-forcing` *primary* instance — the
update layer), and on that forced coordinate the per-edge disturbance
*necessarily* takes the rate×variance product form. The multiplicativity is
inherited from a coordinate AAT itself forces, not borrowed from generic
probability.

But — and this is why it is still **not** $\rho_{\text{ext}}fg$ — the
aggregate over the strategy DAG is
$$\rho_\Sigma^2 = \sum_{e\in E}\nu_{\text{edge},\pi}(e)\,p^\star_e(1-p^\star_e)\,\ell_{0,e}^2,$$
**additive across edges** (the Itô-generator linearity of §4 again: each edge
contributes a covariance term; the certificate sums traces). So even the one
layer with forced multiplicativity has it *only per-component*, with
**additive aggregation** — the exact same shape as §4. There is no model
factor $f(\mathcal M)$ at all at the per-edge level (the Bernoulli innovation
is model-free given $p^\star$); $\mathcal M$ enters only through *which* DAG
the agent maintains, i.e. through the *set of edges*, i.e. additively in the
sum's support. The three-factor product is not recoverable even here.

**Net of strengthen-first:** the strongest true multiplicative statement AAT
can make is the *per-edge strategic* one, $\rho_{\Sigma,e}^2 =
(\text{policy rate})\times(\text{env per-event variance})$, forced by the
log-odds coordinate AAT itself forces. It is a real result and the prior
spikes under-credited it. It does **not** rescue
$\rho=\rho_{\text{ext}}f(\mathcal M)g(\pi)$ and does not contradict §2/§4 —
it confirms the pattern (multiplicative per-component, additive across
components, with the aggregation forced by the certificate generator).

**Other strengthen-first probes, honestly closed:**
- *Poisson rare-event cascade (prior spike's (MC)).* Re-examined: it factors
  because it *posits* three independent Bernoulli thinning gates (MC-2). That
  independence is the §2 category error in disguise — the "model gate" being
  independent of the "policy gate" is exactly the
  $f(\mathcal M)\!\perp\!g(\pi)$ assumption the live theory's `#der-team-
  persistence`/§5-of-prior-spike coupling refutes. (MC) is not a regime where
  the multiplicative form is *true of AAT's $\rho$*; it is a regime where a
  *different, independence-stipulated* object factors. Not a rescue.
- *Large-deviation tail (prior spike's (LD)).* Correct but it is a statement
  about *tail probabilities of an additive-in-variance $\rho$*, not about
  $\rho$ itself; rate functions add under inf-convolution → tail probs
  multiply. This is consistent with §4 (additive variance) and is not a
  rate-coordinate multiplicative factorization. Confirmed, not a rescue.
- *Multiplicative-noise SDE (geometric/stochastic-vol).* Re-derived: the
  log-coordinate moves it back to additive (§4 applies in the log chart).
  Confirmed: a coordinate-choice observation, consistent with the
  `#disc-additive-coordinate-forcing` pattern, not a rescue.

---

## 6. Is $\delta = o-\hat o$ genuinely load-bearing across the adaptive core
(so $\rho$ *is* the effective innovation rate)? — Yes, decisively

The mandate flags a constitutive sub-question: is the predictive residual
genuinely load-bearing such that $\rho$ *is* the effective innovation rate,
or does the live theory use $\rho$ in some way admitting a multiplicative
reading?

**Answer: $\delta = o-\hat o$ is maximally load-bearing, and the live theory
uses $\rho$ in exactly the way that *forbids* a multiplicative reading.**
Evidence, all first-hand from canon:

1. `#def-mismatch-signal` is `status: axiomatic` and explicitly definitional:
   the residual is "not an additional assumption but a consequence of having
   a predictive model." Everything downstream (`#result-persistence-
   condition`, `#result-sector-condition-stability`, `#result-mismatch-
   decomposition`, the whole `#result-sector-persistence-template` family)
   `depends:` on it transitively. There is no live formulation of $\rho$ that
   is *not* the forcing on this residual.
2. The Model-S SDE $d\delta=-F\,dt+\sigma_w\,dW_t$ is the canonical object of
   `#deriv-sector-condition` (`status: exact`). $\sigma_w$ / $\rho$ is *by
   construction* the innovation driving the residual — the Itô term. There is
   no second, environment-only $\rho$ anywhere in `src/`.
3. The persistence-template table (C4) shows the live theory's *consistent*
   move is to write effective disturbance as `env term + coupling/closure
   terms`, additive. A multiplicative reading would require *some* segment to
   write $\rho_\xi = (\text{env})\times(\text{agent})$; **none does** (grep of
   `src/` confirms: every $\rho^{\text{eff}}$/$\rho_\xi$ definition is a
   sum). The "multiplicative reading" the mandate asks me to check for
   *does not exist in the live theory*; it existed only in the now-`status:
   false` `#internal-external-decomposition` and in the two spikes.

So the mandate's disjunction resolves cleanly: the residual is load-bearing,
$\rho$ *is* the effective innovation rate (the trace of the residual's
driving covariance, ×$\nu$), and the live theory uses it additively. The
parent's `status: false` mark removed the *only* place a multiplicative
reading was asserted. That mark is **correct, and a fortiori not a
regression** — restoring the multiplicative split would re-introduce a
category error the rest of canon never committed.

---

## 7. Verdict, conditions, confidence (on the epistemic ladder)

**The true structure of $\rho$:**

> $\rho^2 = \nu\,\mathbb E\|\delta_t\|^2$ is, by the canonical Model-S
> certificate, $\nu$ times the trace of the instantaneous covariance of the
> predictive residual's driving noise. It decomposes **additively in the
> rate/variance coordinate**, exactly two terms at the exact tier
> ($\rho_\star^2(\text{env};\pi) + \Delta_{\text{agent}}^2(\mathcal M;
> \pi,\text{env})$, forced by GA-1), with a finer $\mathcal M$/$\pi$/cross
> split that is **conditional** (identified under Regime A/B by mediation
> analysis, confounded under Regime C — an `#disc-identifiability-floor`
> instance). It does **not** decompose multiplicatively in rate; the
> multiplicative form is not "unproven" but **type-incorrect** by the
> constitutive definition of $\delta$ and by the Itô-generator linearity of
> the canonical certificate. The single layer with a forced multiplicative
> sub-structure is the *strategic* one (per-edge rate×variance on the
> AAT-forced log-odds coordinate), and it too aggregates **additively**
> across edges. The additive coordinate is *forced* (by the generator's
> linearity in the diffusion matrix), not chosen and not merely Bienaymé.

**Exact conditions:**
- (2T) two-term identity: **exact** under GA-1 (fresh-noise), which is
  *already canon* for `#result-mismatch-decomposition`. No (S1)–(S4),
  no information geometry, no independence.
- Multiplicative no-go: **exact**, unconditional, from C1+C3 (one-step
  contradiction, §2) and independently from the Itô-generator type argument
  (§4).
- Three-way $\mathcal M$/$\pi$/cross split: **conditional** — exact only as a
  definition-by-difference (vacuous); substantively identified only under
  Regime A (interventional) or Regime B (functional-form mediation
  assumptions). Confounded under Regime C. (S3) exponential-family is what
  the prior spike's "exact" was silently resting on.
- Strategic per-edge multiplicativity: **robust-qualitative** — the per-edge
  rate×variance product is forced by the log-odds coordinate; the cross-edge
  *independence* used to call the aggregate "clean" is a modeling assumption,
  so the aggregate is additive-with-possible-cross-edge-correlation (still
  additive in the trace by §4, but the per-edge factorization's
  independence across edges is not forced).

**Three legitimate outcomes, which obtained:** the mandate named (a) rescue
multiplicative (→ parent's mark is a regression), (b) sharper no-go + exact
corrected form + conditions, (c) deeper/different no-go or precise open
boundary. **Outcome (b) and (c) jointly.** (b): a sharper no-go (category
error, one step, §2) *with* the exact corrected form ((2T), §3) and its
precise conditions (§7). (c): the deeper structural result — the additive
coordinate is forced by the canonical certificate's Itô generator and is
already canon six times over (§4); the multiplicative question is
type-incorrect, not merely false. Outcome (a) did **not** obtain: the
parent's `status: false` mark is correct and not a regression (§6).

**Confidence (epistemic ladder, AAT tiers):**
- §2 no-go: **exact** (one-step contradiction from `status:axiomatic`
  `#def-mismatch-signal` + `status:exact` `#result-mismatch-decomposition`).
- §3 (2T) identity: **exact** (C3 × $\nu$ under GA-1, already canon).
- §4 forced-additive-by-generator: **exact** (verbatim re-reading of
  `status:exact` `#deriv-sector-condition` Prop A.1S; the linearity of the
  Itô generator in $\Sigma$ is elementary and unconditional).
- §3 three-way split is conditional / §5 strategic multiplicativity is
  robust-qualitative: as tabled.

Honest residual uncertainty: the *interpretation* of $\Delta_{\text{agent}}^2$
into mediation components (Regime A/B identification) is real research
(Imai-style), not closed here — but that is exactly the
`#disc-identifiability-floor` pattern and should be *stated as such*, not
presented as a clean (S1)–(S4) theorem. My confidence that the
**replacement-of-record should be (2T)+§4, not three-way (AV)**, is high; my
confidence in the *exact* status of (2T) and the no-go is as high as the
canon segments they rest on.

---

## 8. Notes for the parent (routing/landing is the parent's call, not done here)

1. **The parent's `status: false` mark on `#internal-external-decomposition`
   is correct and not a regression.** No action needed there except that the
   *replacement* description in the navigator is itself imprecise (next item).

2. **Second §4.1-shaped issue, surfaced not fixed:** TODO:147, TODO:438,
   PROPOSALS §D.9, and `spikes/INDEX.md:102` all describe the corrected
   replacement as the "(AV) variance-additive **theorem** under (S1)–(S4)"
   and route it as heavy landing **CL-2**. Per §3 above, the *exact* corrected
   truth is the **two-term** identity (GA-1 only, no (S1)–(S4)) plus the
   already-canon Itô-generator structural statement (§4); the three-way
   $\mathcal M$/$\pi$/cross (AV) is **conditional**, not exact, and its honest
   home is the `#disc-identifiability-floor` pattern (mediation, Regime A/B),
   not a standalone (S1)–(S4) theorem. The navigator currently records a
   conditional result as the exact replacement — the same shape of error,
   one level up. This is a parent/Joseph call (it touches the CL-2 landing
   plan and a Joseph-reserved Instance-5 decision); flagged, not edited.

3. **The landing is *lighter* than CL-2 currently assumes for the exact
   core.** (2T) and §4 are one-step consequences of `status:exact` /
   `status:axiomatic` segments already in canon — they do not need
   Amari–Nagaoka projection machinery or (S1)–(S4). If/when the parent lands
   `#rho-decomposition`, the *exact* spine is short; the heavy/Joseph-reserved
   part is only the conditional mediation refinement and the
   identifiability-floor Instance classification. Splitting "exact core
   (light)" from "conditional refinement (heavy, Joseph-reserved)" may
   simplify CL-2.

4. **`spike-rho-factorization.md` and `spike-rho-additive-variance-
   strengthening-2026-04-24.md` disposition recommendation (parent decides):**
   both are *correct in their no-go diagnosis* but *over-built and imprecise
   in their positive claims* — the first runs three cases where one
   constitutive step suffices; the second asserts a conditional three-way
   split as an exact (S1)–(S4) theorem. The reasoning trails are valuable
   (the (MC)/(LD) sub-regime analysis, the Amari–Nagaoka interpretation of
   $\chi$) and should be preserved as trail, but **the load-bearing math that
   should reach canon is (2T)+§4+§5-strategic, not (AV)-as-exact-theorem.**
   This is an integration-is-replacement situation: the prior spikes' "(AV)
   exact under (S1)–(S4)" should be *replaced* (deleted, not softened-with-a-
   pointer) by "(2T) exact under GA-1; three-way conditional under Regime
   A/B." Recommended disposition: keep both spikes `live-or-open` /
   parent-batch (they carry a Joseph-reserved Instance decision and the
   corrected replacement differs from what their own verdicts state — exactly
   the §2a regression-axis / parallel-path-payload shape the routing doc
   flags). Do **not** file them `.integrated` against the old (AV) framing.

5. **Strengthening the prior no-go missed (credit where due):** the
   *strategic-layer per-edge multiplicativity forced by the log-odds
   coordinate* (§5) is a real AAT-internal result the prior spikes
   under-credited as "generic probability." If `#rho-decomposition` lands, a
   subsection noting that the *only* AAT-forced multiplicative structure is
   per-edge-strategic-on-the-forced-log-odds-coordinate (and that it too
   aggregates additively) is worth including — it is the precise, honest
   answer to "is there *any* regime where multiplicative is AAT-true," and it
   ties `#deriv-edge-update-natural-parameter` (a forced-coordinate primary
   instance) to the disturbance question.

---

## 9. Reasoning-trail appendix (what I checked, in order, and the dead ends)

1. Read routing §0 — internalized: truth is arbiter, NOTATION/spikes/segment
   text/prior-agent-marks all drift, settle by re-derived math on
   constitutive structure.
2. Read both ρ spikes + the `status:false` segment + the parent
   internal-external spike head. Logged their claims as *proxies to test*,
   not authority.
3. Read constitutive primaries first-hand: `#def-mismatch-signal`
   (axiomatic), `#hyp-mismatch-dynamics`, `#result-mismatch-decomposition`
   (exact), `#result-sector-condition-stability` (exact),
   `#result-sector-persistence-template` (exact),
   `#deriv-sector-condition` (exact), NOTATION ρ/w rows.
4. **Key recognition (C4):** the persistence-template instantiation table
   already answers "how does effective disturbance decompose" — unanimously
   additive, six instances, zero multiplicative. The prior spikes never used
   this; that is the over-build.
5. Derived §2 (one-step category-error no-go) from C1+C3. Checked it is
   *stronger* than the three-case survey (it closes the "maybe another case"
   gap the survey leaves open).
6. Derived §3 (2T) from C3×ν under GA-1; checked the prior strengthening
   spike's three-way "exact under (S1)–(S4)" — found its Step 4 defines
   $\chi$ by difference (vacuous-exact); concluded three-way is conditional,
   not exact. (This is a real defect in the prior spike, surfaced honestly.)
7. Derived §4 (additive forced by Itô generator) by re-reading
   `#deriv-sector-condition` Prop A.1S verbatim — the disturbance enters the
   certificate only via $\tfrac12\sigma_w^2 n\,dt$; generator linear in
   $\Sigma$ ⇒ additive over *any* decomposition, no independence needed.
   This strictly strengthens the prior spike's "Bienaymé/adjacent" framing.
8. Strengthen-first probes (§5): epistemic layer — no (type-incorrect);
   strategic layer — *yes per-edge*, forced by the AAT-forced log-odds
   coordinate, but additive across edges (prior spikes mis-filed this as
   "generic"). (MC)/(LD)/multiplicative-noise re-examined and closed as
   non-rescues with reasons.
9. Confirmed the constitutive sub-question (§6): residual is maximally
   load-bearing; grep-confirmed every live $\rho^{\text{eff}}$ definition in
   `src/` is a sum; no multiplicative reading exists in the live theory.
10. Dead ends / not chased: finite-sample concentration for the term
    estimates (real but orthogonal — population identity is the question
    asked); the Regime-A/B mediation identification (real research, correctly
    *not* closed here — flagged as the identifiability-floor pattern, which
    is its honest home, rather than over-claimed).

---

*End of spike. Verdict: the multiplicative factorization is type-incorrect
(not merely unproven) by the constitutive definition of mismatch and by the
Itô-generator linearity of the canonical Model-S certificate; the exact
corrected form is the two-term GA-1 identity (2T) plus the already-canon
additive-by-generator structure; the three-way $\mathcal M$/$\pi$ split is
conditional (identifiability-floor / mediation), not the exact (S1)–(S4)
theorem the navigator records; the one AAT-forced multiplicative structure is
per-edge strategic on the forced log-odds coordinate and it too aggregates
additively. The parent's `status:false` mark is correct and not a regression;
a second, subtler §4.1-shaped issue (the navigator queuing a conditional
result as the exact replacement) is surfaced for the parent, not edited.*
