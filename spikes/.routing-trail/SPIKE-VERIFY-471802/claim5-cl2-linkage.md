# Claim 5 — CL-2 §7 linkage: the rho Regime-C confound IS Object B projected onto the disturbance-statistic coordinate, derived from #result-mismatch-decomposition C3 (status: exact)

## What the spike claims (§7)

> "The M/π/cross split is confounded under Regime C" *is* Object B's no-go
> projected onto the disturbance-statistic coordinate. Derivation:
> $\Delta_{\text{agent}}^2$ is, by C3 (`#result-mismatch-decomposition`
> derivation step 3, `status: exact`), $\nu\,\mathbb E\|\hat o_t-\bar
> o_t\|^2$ — a functional of the model's predictive mean, i.e. of the
> agent's architecture $(F,\sigma_w,\text{basis})$. Splitting it into a
> model-class part and a policy part under Regime C is confounded *for
> exactly the reason §4 derives*: the architectural content lives in the
> similarity orbit, which the on-policy law annihilates. Regime A escapes =
> Object B escape (a) interventional; Regime B escapes = functional-form
> orbit-quotient (§6 (b)/(c)). Same no-go, same escapes, same mechanism.
> Tier: exact.

This is the load-bearing linkage for the unified disposition (collapsing
three navigator items into one). The mandate flags §7 as the most likely
place something is smuggled. I open C3 and the regime definitions and check
the projection step by step.

## Canon / sibling, first-hand

**C3 — `#result-mismatch-decomposition` (`status: exact`, derivation step
3, line 32):** under GA-1 (fresh-noise: $\varepsilon_t$ conditionally
independent of $\mathcal C_{t-1}$ given $(\Omega_t,a_{t-1})$),
$$\mathbb E\|\delta_t\|^2 = \underbrace{\mathbb E\|\hat o_t-\bar
o_t\|^2}_{\text{model error (reducible)}} + \underbrace{\mathbb E[\mathrm{
Var}(o_t\mid\Omega_t,a_{t-1})]}_{\text{obs noise (irreducible)}},$$
cross-term **exactly zero** by orthogonality ($\mathbb E[o_t-\bar o_t\mid
\Omega_t,a_{t-1},\mathcal C_{t-1}]=0$ by def of $\bar o_t$ + GA-1). Verified
first-hand; the derivation is a clean conditional-orthogonality argument,
genuinely `exact`. **No $\nu$ prefactor in canon** — the $\nu$ in the spike
comes from the **Model-S rate reading** $\rho^2:=\nu\,\mathbb E\|\delta\|^2$
(rho-recheck §3 line 248, "C3 × ν"), which is itself the Model-S convention
$\rho^2=\nu\sigma_\nu^2$ used in `#hyp-mismatch-dynamics`. So the
$\Delta_{\text{agent}}^2=\nu\,\mathbb E\|\hat o-\bar o\|^2$ identity is
**C3's reducible term, rate-lifted** — sound, and the spike attributes it
correctly to C3 (it does not claim canon has the $\nu$; it claims (2T) =
C3×ν, which the rho-recheck establishes as exact under GA-1 alone).

**Regime A/B/C — canon definitions, first-hand.**
`#der-loop-interventional-access` (`status: exact`) line 23: "strong in
Regime A (intervention-rich …), moderate in Regime B (partial
intervention), weak in Regime C (observation-only)". The strengthening
spike line 94: causal-mediation (Imai et al. 2010) gives "exact
identification under Regime A (intervention-based) and conditional
identification under Regime B (functional-form assumptions). **Regime C
leaves $\chi$ confounded with $\Delta_{\mathcal M}^2$ and $\Delta_\pi^2$.**"
The two Regime A/B/C usages **coincide**: A = interventional, B =
functional-form, C = on-policy/observation-only/confounded. This is not the
spike inventing a mapping — canon and the strengthening spike already use
the *same* trichotomy, and the rho-recheck's tiering table (line 296)
already states "under Regime C it is confounded — `#disc-identifiability-
floor` Instance, exactly." So the spike's §7 is *discharging an assertion
the navigator (TODO:147, PROPOSALS §D.9) and the rho-recheck already make*
("provably the same object"). The job is to check the proof, not the
novelty.

## Step-by-step audit of the §7 projection

The claimed identity: **{Regime-C confound of the $\Delta_{\mathcal
M}^2/\Delta_\pi^2/2\chi$ split}** $\equiv$ **{Object B's
on-policy-summary unidentifiability}** projected onto the
disturbance-statistic coordinate.

**Step A — what is being split.** The reducible term
$\Delta_{\text{agent}}^2=\nu\,\mathbb E\|\hat o_t-\bar o_t\|^2$. The
strengthening spike's three-way split writes it as $\Delta_{\mathcal
M}^2+\Delta_\pi^2+2\chi$, where $\chi$ is *defined as the residual that
balances the equation* (rho-recheck §3 line 280–283: $2\chi:=\Delta_{
\mathcal M}^2(\mu_\pi)-\Delta_{\mathcal M}^2(\mu_{\pi^\star(\mathcal M)})$ —
"vacuously exact … a definition, not a decomposition theorem"). So the
split into a *model-attributable* part and a *policy-attributable* part is
**an attribution problem**: given only $\Delta_{\text{agent}}^2$ (a
functional of $\hat o_t$, i.e. of the model's predictive mean, evaluated
along the $\pi$-induced distribution), can you say how much is "the model
class" vs. "the policy"? Verified: this is correctly characterized — the
single observable $\Delta_{\text{agent}}^2$ does not by itself separate
"$\hat o$ is bad" from "$\pi$ drove the state into regions where any $\hat
o$ in the class is bad." That is a textbook **mediation/confounding**
problem (policy mediates which states the model is evaluated on). Sound so
far.

**Step B — the architecture↔similarity-orbit identification.** §7's
load-bearing move: "the architectural content lives in the similarity orbit
(§4), which the on-policy law annihilates; you cannot attribute disturbance
to 'this architecture' vs. 'this policy' because the architecture is only
identified up to the orbit." **This is where I look hardest for a smuggle.**

- $\hat o_t$ is the model's predictive mean — a functional of the agent's
  realization $(F,\sigma_w,\text{basis})$ (in the linear-Gaussian
  sub-scope, $\hat o_t$ is the Kalman predictor, determined by the
  realization). Claim 1 (verified, with scoping) established the on-policy
  observation law — hence $\Delta_{\text{agent}}^2=\nu\mathbb E\|\hat
  o-\bar o\|^2$, a functional of the on-policy law — depends on the
  realization **only through the similarity-invariant base** (the orbit is
  annihilated by the output map). So $\Delta_{\text{agent}}^2$ is
  **constant along the similarity fiber**: two similarity-related agents
  $A,A'$ have *identical* $\Delta_{\text{agent}}^2$ at *identical* policy.
- Therefore the map (architecture-realization) $\mapsto
  \Delta_{\text{agent}}^2$ **factors through the orbit quotient**. The
  "model-class part" $\Delta_{\mathcal M}^2$ would need to be pinned to a
  *specific realization within the orbit* to be separated from the policy
  part — but on-policy summary data only sees the orbit. **This is a
  genuine, forced consequence of Claim 1**, not a smuggle: if Claim 1 holds
  (it does, with scoping), then $\Delta_{\text{agent}}^2$ is orbit-constant,
  and orbit-constancy is *exactly* the obstruction to the M/π attribution
  under on-policy data. The projection is real.

**Step C — "projected onto the disturbance-statistic coordinate".** Object
B is stated on the full on-policy observation law (the innovation/output
process). The Regime-C confound is stated on the scalar(ish)
$\Delta_{\text{agent}}^2$ (the reducible disturbance power). The claim that
the latter is the former *projected* onto the disturbance-statistic
coordinate: $\Delta_{\text{agent}}^2$ is a **specific functional** (a
second moment under the $\pi$-induced law) of the same on-policy
observation law Object B is about. A functional of an orbit-constant law is
orbit-constant; the M/π non-separability is the image, under that
functional, of the orbit-non-identifiability. So "projection" is the right
word: it is the same no-go pushed forward through the map (full on-policy
law) $\to$ (reducible disturbance power). **No new obstruction is
introduced by the projection**; if anything the projection can only *lose*
discriminating information (a functional cannot separate what the full law
cannot), so the confound on the projected coordinate is *implied by*
Object B, not independent of it. Sound. **This is the correct direction of
the implication** (Object B ⇒ Regime-C confound on the projection); the
spike states it as an identity ("IS Object B projected"), which is
defensible because the §7 claim is specifically about the *projected
coordinate*, where the two coincide. I would phrase it as "the Regime-C
confound on $\Delta_{\text{agent}}^2$ is the image of Object B's
orbit-non-identifiability under the disturbance-power functional" — which
is what the spike means and what it derives. Not smuggled.

**Step D — escape correspondence.** §7: Regime A escape = Object B escape
(a) interventional; Regime B escape = functional-form orbit-quotient (§6
(b)/(c)).
- Regime A (interventional, Imai mediation identified by intervention) ↔
  Object B escape (a) (loop-interventional access excites the orbit
  direction): **both are "supply $do$-data to break the on-policy
  degeneracy."** Canon's `#der-loop-interventional-access` Mode 3
  (observer-on-agent-input, line 68, reserved for "architecture-within-
  behavior-class layer") is *literally* this. Correspondence is sound and
  canon-anticipated.
- Regime B (functional-form assumptions identify $\chi$) ↔ §6 (b)/(c) (a
  functional-form / structural restriction that quotients the orbit):
  imposing functional-form structure on the model class restricts the orbit
  (picks a canonical realization / breaks the $GL(n)$ symmetry), which is
  the same as Object B's "restrict to a canonical form" escape. Sound,
  though softer (this is the robust-qualitative end — functional-form
  identification is conditional by nature, matching the rho-recheck's own
  "conditional" tier for the three-way split).

**Step E — is anything smuggled?** The candidate smuggles:
1. *Does §7 need the strengthening spike's vacuous three-way split to be
   non-vacuous?* No — §7 only needs (i) $\Delta_{\text{agent}}^2$ = C3's
   reducible term ×ν (exact, GA-1, verified) and (ii) Claim 1's
   orbit-constancy (verified, sub-scope-exact). It does **not** rely on the
   strengthening spike's "(AV) exact under (S1)–(S4)" (which the rho-recheck
   correctly demolishes as vacuous). Good — §7 is *not* parasitic on the
   refuted (AV) theorem; it rests on C3 (exact) + Claim 1. This is the key
   anti-smuggle check and it **passes**.
2. *Is the $\nu$-lift legitimate?* Yes — it is the Model-S convention
   $\rho^2:=\nu\,\mathbb E\|\delta\|^2$ already used in canon
   (`#hyp-mismatch-dynamics`); the rho-recheck §3 establishes (2T)=C3×ν as
   exact under GA-1 alone. Not smuggled.
3. *Does the projection introduce an obstruction Object B doesn't have?* No
   — a functional of an orbit-constant law is orbit-constant; the
   projection can only lose information, so the confound is *implied by*
   (not stronger than) Object B. The direction of implication is correct
   and conservative.

The one honest caveat (the spike states it): the **exact** tier holds in
the linear-Gaussian sub-scope (where Claim 1 is exact); in the general
sub-scope the linkage inherits the robust-qualitative tier of the
CHT-at-agent-as-SCM anchor. §7 labels itself "exact" — that is right
*for the projection step itself* (given Claim 1, the projection is a forced
functional-image argument, elementary), but the *whole linkage's* exactness
is sub-scope-bounded exactly as Object B is. The spike's §8 confidence
ladder does say "Regime-C confound ≡ Object B: exact (§7 derivation from
C3, a status:exact segment)" — I would refine: **the projection step is
exact; the linkage is exact-in-sub-scope / robust-qualitative-in-general,
inheriting Object B's own tiering** (since the linkage is only as strong as
the Object-B law-identity it projects). This is a tier-precision note, not
a refutation — the §7 *derivation* is valid; its exactness is correctly
sub-scope-bounded once you carry Object B's own scope through the
projection.

## Verdict on Claim 5

**Confirmed; the projection genuinely holds and nothing is smuggled.** The
load-bearing anti-smuggle check passes: §7 rests on C3 (`status: exact`,
verified first-hand) ×ν (legitimate Model-S convention) + Claim 1's
orbit-constancy — **not** on the refuted (AV) (S1)–(S4) theorem. The
projection is the conservative direction (Object B ⇒ Regime-C confound on
the disturbance-power functional; a functional cannot separate what the
full law cannot). The escape correspondence (Regime A ↔ interventional,
Regime B ↔ functional-form orbit-quotient) is sound and canon-anticipated
(`#der-loop-interventional-access` Mode 3, line 68). This discharges, with
an actual derivation, the "provably the same object" assertion the
navigator (TODO:147, PROPOSALS §D.9) and the rho-recheck (line 296) were
carrying as a claim.

**Tier refinement (not a refutation):** the §7 *projection step* is exact
(elementary functional-image argument given Claim 1). The *overall linkage's*
exactness is **sub-scope-bounded**, inheriting Object B's own
exact-in-linear-Gaussian / robust-qualitative-in-general tiering — because
the linkage is only as strong as the law-identity it projects. The spike's
flat "exact" for the linkage is one notch hot in the general sub-scope; it
is exact in the linear-Gaussian sub-scope. State it as "exact in sub-scope,
robust-qualitative in general, projection-step exact throughout."

Loci opened: `#result-mismatch-decomposition` (full, esp. derivation step 3
line 32, `status: exact`); `#der-loop-interventional-access` (line 23
Regime A/B/C, line 62–68 Mode 3, `status: exact`); rho-recheck §3 (lines
243–306, the (2T)=C3×ν exact core + the conditional three-way + the
Regime-C tiering row line 296); strengthening spike line 94 (Imai
Regime A/B/C definitions); TODO:147 + PROPOSALS §D.9/§D.9-STATUS (the
"provably same object" navigator assertion this discharges).
