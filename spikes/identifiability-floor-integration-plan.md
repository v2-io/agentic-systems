# Integration Plan: Resolve the `#disc-identifiability-floor` Instance-4 Contradiction

*Plan author: Claude Opus 4.7 (1M context), 2026-05-21.
Mandate: clean disposition of the Object A vs Object B split that has been
Joseph-reserved since 2026-05-18.*

> This document is a plan, not a derivation. The math is settled
> (`spikes/spike-identifiability-floor-instance4-resolution-2026-05-18.md`,
> verified by `spikes/.routing-trail/SPIKE-VERIFY-471802/`). What remains
> is canon disposition: which segments need what edits, which spikes get
> what landed-notes, which TODO / PROPOSALS items retire, what the
> CHANGELOG entry should say. A subsequent agent can execute against this
> plan; this document is self-contained so the executor does not need to
> re-read the resolution spike in full.

---

## 0. The decision (already made; recorded here for the executor)

The contested `#disc-identifiability-floor` "Instance 4" slot always held
**two distinct objects under one ordinal**. The decision:

1. **Object A** (universal-$C$ under non-(PI) norms, currently in the
   Instance-4 slot): **deleted from `#disc-identifiability-floor` as a
   floor instance**, integration-is-replacement style. Its content is
   correctly classified as a *downstream theorem of `#disc-additive-
   coordinate-forcing`'s 4th primary instance* — exactly as the cited
   source segment `#deriv-observation-ambiguity-bias-bound:127` already
   states in canon. The meta-segment's stated home for the
   $C_{FR} = \sqrt{2}$ result is the **(PI) commitment's downstream
   consequence**, *not* a floor.

2. **Object B** (architecturally-distinct, behaviorally-identical agents
   unidentifiable from on-policy summary data; = the rho-recheck Regime-C
   confound = CL-2's heavy refinement = the neutral-drift spike's §8 / §10.1
   candidate): **installed as the genuine Instance 4** — the third member
   of the rank-collapse subclass, with the now-derived Kalman-Ho similarity-
   orbit no-go as the exact-sub-scope anchor.

3. **The Sylvester-mechanism Discussion is repaired** to read
   {Instance 1, Instance 2, Object B as Instance 4} as **rank-collapse via
   Sylvester** (at one remove — Sylvester forbids the *escape via
   reparameterization*, identically to Instance 2), and {Instance 3} as the
   distinct **projection / Schur-complement obstruction**. Three
   rank-collapse members, not two. Object A is not in this taxonomy at all.

4. **The CL-2 heavy Joseph-reserved refinement collapses into this same
   move.** The 2026-05-18 resolution spike §7 *proved* (not asserted) that
   the Regime-C confound and Object B are the same object viewed from the
   disturbance-statistic coordinate. Landing Object B as the genuine fourth
   floor simultaneously discharges CL-2's heavy refinement — one decision,
   not two.

5. **Each Instance entry will explicitly state why it is a floor** so a
   reader landing on the meta-segment can see what the classification
   means. Joseph's specific ask: articulate why Object A is **not** a
   floor in the language of the Instance discussion, not only in a
   demoted-and-buried footnote. The honest framing: the entry in
   `#disc-additive-coordinate-forcing` says explicitly that Object A
   *was previously misclassified* as a floor and *why* it does not
   satisfy the floor shape (see §4.b below).

---

## 1. What was found (compressed recap)

### 1.a Object A — why it is not a floor instance (three independent routes, all *exact*)

**Route 1: the external-theorem role is inverted.** Instances 1–3 each
import an external impossibility theorem whose statement *forbids* the
inferential task (CHT forbids L2 from L1; Cramér-Rao bound forbids exact
estimation under rank-deficient Fisher; common-Lyapunov-nonexistence
forbids composite-contraction from marginals). Object A's "external
theorem" is **Čencov 1982** — but Čencov is the *uniqueness theorem that
forces the escape*, not a theorem that forbids the task. A floor's
external theorem forbids; Object A's external theorem forces an escape's
uniqueness. **Opposite structural role.**

**Route 2: exactly one escape exists, and that count is mathematically
forced.** Object A's escape is "adopt (PI) + Fisher-Rao." Čencov's
uniqueness theorem *mathematically forbids* a second structurally
distinct escape from existing — uniqueness of the invariant metric is
the entire content. True floors require ≥2 distinct escapes carving an
*operational space* (Instance 1 has 5 named escape routes; Instance 2
has 3; Instance 3 has 4). Object A has a *forced point*, not a space.
**A uniqueness theorem on the escape side is logically incompatible
with the ≥2-distinct-escapes structure that defines a floor instance.**

**Route 3: consequence is re-use, not elevation.** A floor instance
*elevates new* machinery to load-bearing. Object A "elevates (PI)" —
but (PI) is *already* load-bearing as the 4th primary instance of
`#disc-additive-coordinate-forcing`. Object A *consumes* an existing
load-bearing role; it does not surface a new one. The $C_{FR} = \sqrt{2}$
bias bound is a *client* of the (PI)-forced Fisher-Rao metric, exactly as
`disc-additive-coordinate-forcing.md:56` already states ("the bias bound
… relies explicitly on the Fisher-Rao metric"). A client of a forced
coordinate is a **downstream theorem of the coordinate-forcing pattern**,
by the definitions of the two meta-patterns.

**Independent confirmation from canon-internal consistency.**
`disc-identifiability-floor.md`'s own Sylvester-mechanism Discussion
taxonomizes only three floors (rank-collapse {I1, I2} + projection {I3})
and explicitly says *"the floors do not share one mechanism."* It silently
excludes Object A from the mechanism taxonomy. Yet the Findings count
line and the Related-Work table list it as the fourth. **The segment
already contradicts itself**; the resolution removes the contradiction.

The source segment `#deriv-observation-ambiguity-bias-bound:127` *already
states in canon*: Object A "does not match the five-element test … the
honest position: this no-go is a **downstream theorem of the (PI)
commitment, not a new floor instance**." The category error was localized
entirely in `disc-identifiability-floor.md`.

### 1.b Object B — why it IS a genuine floor instance

**Setting.** Two AAT agents $A, A'$ on the same regime-restricted
trajectory, with identical sector-condition summary $(\alpha, R)$
(equivalently: identical ultimate-deviation statistics on
$\lVert\delta\rVert$ in that regime). Observer has on-policy, in-regime,
summary-only data. Question: can $A$ be distinguished from $A'$?

**External theorem (dual-anchor — same shape as Instance 1).**
- *Linear-Gaussian sub-scope (sharp anchor):* **Kalman 1963 / Ho-Kalman
  1966** canonical-form non-uniqueness — minimal state-space
  realizations sharing an innovation spectrum form a similarity-equivalence
  class (Anderson & Moore 1979 *Optimal Filtering* §10.4).
- *General sub-scope (robust-qualitative anchor):* **Bareinboim, Correa,
  Ibeling & Icard 2022** CHT at the agent-as-SCM layer (two SCMs over
  the agent's state space agreeing on Level-1 observation data,
  disagreeing on Level-2).

**The no-go (exact in the linear-Gaussian / Kalman sub-scope).**

> Let $A, A'$ be two AAT agents whose linearized closed-loop residual
> dynamics are minimal state-space realizations $(F, \sigma_w)$ and
> $(F', \sigma_w')$ related by an invertible similarity $F' = TFT^{-1}$,
> $\sigma_w' \sigma_w'^\top = T \sigma_w \sigma_w^\top T^\top$. Then the
> stationary innovation process — hence the $(\alpha, R)$-summary, the
> innovation spectrum, and the entire on-policy summary-restricted
> observation law — is **identical** for $A$ and $A'$.

*Proof sketch.* The innovation's stationary law is determined by
$(F, \sigma_w \sigma_w^\top)$ only through similarity-invariant
quantities (eigenvalues of $F$ = the $\alpha$-spectrum; the solution
$\Pi$ of the Lyapunov equation $F\Pi + \Pi F^\top + \sigma_w \sigma_w^\top = 0$
transforms as $\Pi' = T\Pi T^\top$; observables are spectrum-determined,
hence similarity-invariant). The architectural content (which internal
coordinates implement the correction) lives entirely in the similarity
orbit and is annihilated by the spectrum map. $\square$

**Mechanism (the critical question).** Object B's irreducibility:
- **NOT Sylvester for free.** The *generating* group action that
  produces the indistinguishable pair $(A, A')$ is state-space
  *similarity* $T(\cdot)T^{-1}$. Sylvester's law of inertia is a
  statement about metric *congruence* $S^\top(\cdot)S$. Different group
  actions, different invariants. The mandate's caution that a 4th
  instance "does not inherit Sylvester for free" is mathematically
  *exactly right*.
- **NOT a new mechanism either.** Object B reduces to Instance-2's
  Fisher-information null space along a structurally-forced
  indeterminacy manifold — with the manifold being the $GL(n)$
  similarity fiber instead of the mixture-indeterminacy manifold.
  Observation law factors through similarity-invariants ⟹ observed-
  Fisher is identically zero on the similarity fiber ⟹ same shape as
  Instance 2.
- **Therefore: Object B is a member of the rank-collapse subclass {I1,
  I2, B}**, with the additional structure that the rank-deficient
  direction is a *Lie-group fiber* rather than a single indeterminacy
  manifold. Sylvester's law forbids the *escape via reparameterization*
  identically to Instance 2 — Sylvester at one remove.

**Boundary characterization — three structurally distinct escapes.**
- **(a) Loop-interventional access** (`#der-loop-interventional-access`).
  $do(\cdot)$ perturbs along similarity-fiber directions that on-policy
  data never excites. The intervention generates Level-2 data; the
  no-go is Level-1-only.
- **(b) Higher-moment / out-of-regime observation.** In the nonlinear
  sub-scope (AAT's $\beta$), two agents matched at $(\alpha, R)$ and
  second-order generally differ at moments $\ge 3$. *Provably void in
  the linear-Gaussian sub-scope* (a Gaussian innovation has no
  information beyond second order) — a sharp scope statement, not a
  hedge.
- **(c) Architecture instrumentation.** Direct read of the update rule /
  internal state (white-box access). Same kind as Instance 2's "instrument
  the latent" escape.

(The neutral-drift spike proposed a fourth escape — *horizon extension under
the same policy* — which the resolution spike showed collapses into (a):
more samples of the same observation law cannot escape an annihilation of
the law itself. Three escapes, not four.)

**Strengthened consequence.** Object B elevates
`#der-loop-interventional-access` to a load-bearing role at the
*agent-internal* layer — the **third semantically distinct deployment
mode** of interventional access (after agent-self-intervention for
causal-sufficiency / Instance 1, and observer-on-sub-agent for
coupling-sign / Instance 3). The shared content is "Level-2 data breaks
a Level-1 degeneracy"; the distinct content is *which* degeneracy.

**Tier:** *exact* in the linear-Gaussian / Kalman sub-scope ($\alpha_1$);
*robust-qualitative* in the general sub-scope via CHT-at-agent-as-SCM.
**NOT flat exact** — carry the sub-scope/general boundary consistently.

**Fano vs Kalman-Ho.** The neutral-drift spike proposed Fano as the
anchor; the resolution spike demonstrated Fano *degenerates at $I = 0$*
(the similarity-orbit construction has $I(A; \text{obs}) = 0$ exactly,
so Fano gives the vacuous bound). **Kalman-Ho is the exact-population
anchor; Fano is the finite-sample refinement** (architectures close-but-
not-equal, $I > 0$ small) and remains honest open work.

### 1.c Identity: Regime-C confound ≡ Object B (proved, not asserted)

The resolution spike §7 derived (not asserted) that the conditional
$\mathcal M / \pi /$ cross split being confounded under Regime C *is*
Object B's no-go projected onto the disturbance-statistic coordinate.
$\Delta_{\text{agent}}^2$ is a functional of the agent's architecture
$(F, \sigma_w, \text{basis})$; attributing it to model-class-part vs
policy-part under on-policy summary-only data is asking exactly the
similarity-orbit identifiability question that §1.b answers in the
negative. **Regime A escape = interventional escape (a). Regime B escape
= a functional-form quotient of the orbit (escape family (b)/(c)).
Same no-go, same escapes, same mechanism.** This is the mathematical
identity that collapses the CL-2 heavy refinement and the Instance-4
question into one decision.

---

## 2. Repairs the math gate requires (CRITICAL — do not skip)

The spike-verify gate (`spikes/.routing-trail/SPIKE-VERIFY-471802/`,
confirmer ≠ author) cleared the resolution spike's math overall but
named three specific repairs the landing agent **must** apply. From
`PROPOSALS.md` §D.9:

1. **Overclaim on "every moment of $\lVert\delta\rVert$ identical."**
   The spike's boxed statement reads as if *every* moment of
   $\lVert\delta\rVert$ is identical for the similarity-related pair.
   True only for *innovation/output + similarity-invariant summaries*.
   $\mathbb E \lVert\delta\rVert^2 = \operatorname{tr}\Pi$ is **not**
   similarity-invariant in general ($\Pi' = T\Pi T^\top$ ⟹
   $\operatorname{tr}\Pi' = \operatorname{tr}(T\Pi T^\top) \ne
   \operatorname{tr}\Pi$ unless $T$ is orthogonal). The honest statement
   restricts the "identical" claim to *innovation spectrum and
   similarity-invariant summaries of it* — which is what the on-policy
   observer actually sees. Restate the boxed claim accordingly.

2. **Lyapunov-equation sign slip.** The spike displays the steady-state
   Lyapunov equation as one form; the conclusion survives but the
   display is sign-wrong. The standard form is
   $F\Pi + \Pi F^\top + \sigma_w \sigma_w^\top = 0$
   (with $F$ Hurwitz, sign convention $\dot\delta = -F\delta + \ldots$ ⟹
   the Lyapunov equation has the $+\sigma_w\sigma_w^\top$ source term and
   $= 0$ RHS). When the math lands in canon, the displayed equation must
   match the project's sign convention used in
   `#deriv-sector-condition` / `#result-sector-persistence-template`.
   (The conclusion — $\Pi' = T\Pi T^\top$ under similarity — is
   sign-independent and survives.)

3. **Sub-scope / general tier boundary must carry consistently.** Object
   B is *exact in the linear-Gaussian / Kalman sub-scope* and
   *robust-qualitative in general* via CHT-at-agent-as-SCM. The
   landing must not collapse this into "exact" — carry the tier
   boundary explicitly in the Instance 4 entry's *[Derived]* tag, in the
   Tier line, and in the Findings rollup. This is a *strengthen-before-
   soften tier-honesty pass*, not a downgrade.

These repairs are *load-bearing for present-truth accuracy* and are part
of the integration, not optional polish.

---

## 3. Changes by file

### 3.a `01-aat-core/src/disc-identifiability-floor.md` — major repair

**Remove (integration-is-replacement; no ghost-defense).**
- The entire "Instance 4 — Universal Information-to-Distance Constant
  under Non-(PI) Norms" block, including its `> [!warning]` KNOWN-
  DEFECTIVE banner.
- Object A from the Findings count ("four independently-derived
  results" — needs new accounting; see below).
- Object A's row in the Related Work table (currently row 4).
- Any other surface reference to Object A as a floor instance (grep the
  segment for "Universal Information-to-Distance" and "Object A" — there
  should be none after the repair).

**Install Object B as the new Instance 4** following the same structural
template as Instances 1–3 (Setting / External theorem / No-go /
Boundary characterization / Strengthened consequence / Tier). Content
sketched in §1.b above; the executor adapts to the segment's existing
voice and FORMAT compliance. Honest tier label: **Exact (linear-
Gaussian / Kalman sub-scope)** / **Robust qualitative (general, via
CHT-at-agent-as-SCM)** — explicit dual-tier, not flat. Apply the §2
repairs to the displayed math.

**Update the Sylvester-mechanism Discussion** (currently
`disc-identifiability-floor.md:150` area):
- The three-floor taxonomy {rank-collapse: I1, I2} + {composition: I3}
  becomes **{rank-collapse: I1, I2, B} + {composition: I3}** — three
  rank-collapse members, one composition member.
- Explain Object B's mechanism subtlety (the two group actions —
  similarity *generates* the indistinguishable pair; Sylvester forbids
  the *escape via reparameterization*, identically to Instance 2; the
  rank-deficient direction is a Lie-group fiber, the additional
  structure beyond Instance 2's mixture-indeterminacy manifold).
- The "the floors do not share one mechanism" sentence stays (it is still
  true — Sylvester for rank-collapse, projection for composition) but
  the parenthetical count updates to three-and-one.

**Update the Findings rollup** at the bottom of the segment:
- The Brief currently says "Across four independently-derived results
  (the fourth — Instance 4 — is contested and KNOWN-DEFECTIVE …)" —
  this becomes a clean "**Across four independently-derived results**"
  with the rank-collapse / projection breakdown updated to {I1, I2, I4}
  rank-collapse + {I3} projection.
- The Related Work table updates: drop the Object-A row entirely; add a
  new row for Object B citing Kalman 1963 + Ho-Kalman 1966 +
  Bareinboim-Correa-Ibeling-Icard 2022 (dual-anchor).

**Verify cross-references inbound to this segment.** Anywhere in canon
that says "Instance 4 of `#disc-identifiability-floor`" — confirm the new
referent (Object B) is the intended one. The honest expectation:
inbound references were typically about the floor-pattern in general or
about the genuine fourth floor (Object B), so most should be fine.
Exceptions: places that specifically cite the $C_{FR} = \sqrt{2}$ bias
bound *as* a floor instance need redirecting to
`#disc-additive-coordinate-forcing` (see 3.b).

### 3.b `01-aat-core/src/disc-additive-coordinate-forcing.md` — explicit absorption of Object A

The segment's existing "Downstream consequences of the (PI) commitment"
discussion already names Object A's content (the dimension-free bias bound
$C_{FR} = \sqrt{2}$ as a *client* of the (PI)-forced Fisher-Rao metric;
the heteroscedastic-normal counterexample under arbitrary parameter norms
as the no-go that motivates the (PI) scope-gate). The repair makes the
classification explicit and addresses Joseph's specific ask
(*articulate why Object A is not a floor instance in the language of the
discussion, not only in a buried footnote*).

**Add a paragraph** in the existing "Downstream consequences of the (PI)
commitment" area (currently around
`disc-additive-coordinate-forcing.md:54`) along these lines (the executor
adapts to segment voice):

> **Object A and the floor-vs-coordinate-forcing distinction.** The
> no-go "no universal information-to-distance constant exists under
> arbitrary parameter norms" — proved counter-example-grade in
> `#deriv-observation-ambiguity-bias-bound` §4 via the heteroscedastic-
> normal witness — is a member of the *coordinate-forcing family* (the
> (PI) commitment's downstream theorem), **not** a member of the
> *identifiability-floor family*. The structural distinction is sharp:
> a floor instance's external theorem *forbids* the inferential task and
> is escaped by ≥2 structurally distinct routes that elevate *new*
> AAT machinery to load-bearing. Object A's "external theorem" (Čencov
> 1982) *forces the escape's uniqueness* — opposite role; the escape
> count is *exactly one and mathematically forced* (Čencov's uniqueness
> of the invariant metric forbids a second distinct escape); and the
> consequence is *re-use* of (PI), already load-bearing as the 4th
> primary instance of this meta-pattern, not elevation of new
> machinery. The bias-bound theorem is therefore correctly classified
> here as a downstream consequence of (PI) + Čencov, not as an
> identifiability floor.

This paragraph:
- Names *why* Object A is not a floor in the operational language of the
  five-element floor test (external-theorem role / escape count /
  consequence type).
- Cites the source segment that has always classified it correctly
  (`#deriv-observation-ambiguity-bias-bound` §4).
- Lands a positive home for the no-go (the (PI) commitment's
  downstream-theorem cluster) so the content is not orphaned.

**No other changes** to `disc-additive-coordinate-forcing.md`.

### 3.c `01-aat-core/src/deriv-observation-ambiguity-bias-bound.md` — verify, do not edit

The source segment §4 is **already correct in canon** ("does not match
the five-element test … downstream theorem of the (PI) commitment, not
a new floor instance"). The repair is the meta-segment catching up to
its source, *not* changing this segment.

Verification step only: confirm that this segment's §4 cross-references
no longer point to `#disc-identifiability-floor` Instance 4 as a *home*
for the no-go (it can still reference the meta-segment for the
*distinction* discussion, but the home is `#disc-additive-coordinate-
forcing`). The executor's grep will surface the exact lines.

### 3.d Object B's math home — judgment call for the executor

Per `feedback_math_lives_in_segments` (math derived in a spike never
resides only in the spike; lands in an existing segment or in a new
appendix segment), the Object B similarity-orbit no-go needs a canonical
home beyond its summary in the Instance 4 entry of the meta-segment.

Two reasonable patterns; executor decides based on what fits AAT's
canonical structure:

**Pattern P (precedent): a dedicated supporting segment.**
Instances 1–3 each have a supporting segment carrying the full math:
- Instance 1 → `#der-causal-insufficiency-detection`
- Instance 2 → `#deriv-edge-credence-dynamics` Prop B.7
- Instance 3 → `#deriv-critical-mass-composition` + `#result-contraction-template`

Object B's supporting segment could be a new appendix segment
(`deriv-similarity-orbit-noidentifiability` or
`deriv-agent-opacity-from-similarity-orbit` — names are illustrative,
the executor picks per AAT slug discipline) carrying the §4-style
Kalman-Ho construction in full. The Instance 4 entry then summarizes
and cites it.

**Pattern Q (alternative): extend `#der-agent-opacity`.**
The spike §4 observes that "the AAT-specific content is the recognition
that the *architectural* degree of freedom AAT cares about —
`#der-agent-opacity`'s 'which internal mechanism' — *is* the similarity
orbit." `#der-agent-opacity` is a natural home for the structural
result. An extension paragraph + a formal-expression block could land
the construction there.

**Recommendation (peer-voice, executor decides):** check
`#der-agent-opacity` first — if it has room for a derivation block of
this size without overloading its core, Pattern Q is more economical.
Otherwise Pattern P with a fresh appendix segment. Either way, the
math lands in a `01-aat-core/src/` segment, not only in the meta-
segment's Instance 4 summary. Apply the §2 repairs (moment-claim
restriction; Lyapunov sign; sub-scope tier).

### 3.e `ref/prior-art-analysis/11-constructive-impossibility.md` — small update

The row-11 analysis I wrote on 2026-05-21 currently carries the
"three confirmed plus one contested" framing. After integration:
- The contested-Instance-4 caveat block can be removed (replaced by a
  brief historical note in the analysis Footnote / "Refresh" section
  noting that the contradiction was resolved by the 2026-05-18 spike
  and integrated 2026-MM-DD).
- The novelty scoring stays — Math = Some, Arch = High, Synth = High,
  Impact = High — these were honest about the three-confirmed
  position and Object B's addition strengthens the framework, not
  weakens it.

### 3.f `ref/prior-art-analysis/00-impact-meta-summary.md` — light update

The meta-summary's row-11 entry and the §3 convergent-meta-finding both
reference the "four instances (one KNOWN-DEFECTIVE)" framing. Update to
"four confirmed instances" with a brief mention that the Object A
relabeling was completed via the integration plan. The Joseph-reserved
flag for this row is now CLOSED.

---

## 4. Spike housekeeping

Per `audits/README.md` + `feedback_math_lives_in_segments`: spikes get
"integrated" notes after their content lands in canon, and move to
`.integrated/` once the integration is verified.

### 4.a `spike-identifiability-floor-instance4-resolution-2026-05-18.md`

The author of the resolution. After the integration:
- Add an "Integration trail" note at the top (or end) recording the
  CHANGELOG entry date + the canon segments where the content landed +
  the math-gate repairs applied.
- **Move to `spikes/.integrated/`** once canon edits commit clean.

The Fano finite-sample refinement is honestly open (§4 of the spike
calls this out); the integration note should preserve that as a
follow-on direction so it does not get lost.

### 4.b `spike-identifiability-floor-instance-triage-2026-04-24.md`

The triage that was right in direction but explicitly judgment-not-
derivation. After integration:
- Add an "Integration trail" note: triage Candidate-2 (Object B)
  upgraded to derived in canon; triage Candidate-3 (Object A) confirmed
  as not-a-floor and re-homed in `#disc-additive-coordinate-forcing`.
- **Move to `spikes/.integrated/`**.

### 4.c `spike-neutral-drift-endogenous-coupling-strengthening-2026-04-24.md`

Proposed Object B as sketch (§8 / §10.1). After integration:
- Add an "Integration trail" note: §8 sketch upgraded to derived in
  canon (Kalman-Ho closed-form supplied; mechanism reduction to
  Instance-2 / Sylvester-at-one-remove); §10.1 proposed Fano anchor
  retracted (Fano degenerates at $I = 0$; honest open as finite-sample
  refinement, not floor anchor).
- **Check before moving:** this spike has other content beyond the
  Object B proposal; the executor should verify the rest is also
  integrated or has its own routing. If not yet, leave the spike at
  `spikes/` root with the partial-integration note; move when fully
  discharged.

### 4.d `spike-rho-structure-recheck-2026-05-18.md`

The disturbance-side arrival at the same object. After integration:
- Add an "Integration trail" note: §3 Regime-C confound now derived in
  canon as Object B's projection onto the disturbance-statistic
  coordinate (= Instance 4 of `#disc-identifiability-floor`). The §7
  CL-2 linkage in the resolution spike is the proof.
- **Check before moving:** this spike also surfaced the LIGHT 2T identity
  (already landed in `#internal-external-decomposition` 2026-05-18 per
  TODO:147). If both the LIGHT and HEAVY parts are now discharged, the
  spike can move. Verify both pieces are integrated before moving.

### 4.e `spikes/.routing-trail/SPIKE-VERIFY-471802/`

The verification trail (5 claim files: claim1-kalman-ho /
claim2-mechanism-reduction / claim3-escape-count /
claim4-fano-degeneracy / claim5-cl2-linkage). Per audit-routing
discipline, this is the gate-trail — keep as-is in the routing-trail
directory; it provides the audit history.

---

## 5. TODO / PROPOSALS retirement

Move from TODO.md → CHANGELOG.md (integration-is-replacement: present
truth in canon; history in CHANGELOG).

### 5.a TODO.md items to retire

- **TODO line 143** (Kalman-Ho closed-form follow-up spike — distinct
  vs subsumed?): already marked RESOLVED 2026-05-18 in the file.
  After integration, this can be moved to CHANGELOG as fully discharged.

- **TODO line 147** (`#rho-decomposition` / CL-2 replacement —
  HEAVY Joseph-reserved refinement): the (a) LIGHT exact core is already
  landed (2026-05-18, per the existing entry). The (b) HEAVY refinement
  (the conditional $\mathcal M/\pi/\text{cross}$ split, Regime-C
  confound) is *discharged by the same integration that lands Object B*
  per §1.c above. After integration, this whole entry retires.

- **TODO line 441** (`spike-rho-factorization` + `spike-rho-additive-
  variance-strengthening-2026-04-24` paired — CL-2): the CL-2 cluster's
  heavy part is now integrated. Confirm the spike-rho-factorization
  no-go honesty-mark (`#internal-external-decomposition` status: false /
  KNOWN-FALSE banner) remained intact in canon — that mark is *separate*
  from Object A's removal and stays. If verified, retire this entry.

- **TODO line 455** (`spike-neutral-drift-endogenous-coupling-
  strengthening-2026-04-24` — Joseph-reserved batch / 4th-instance
  triage-contradiction): discharged by the integration that lands
  Object B. After integration, retire this entry.

The executor should re-grep TODO.md for any references to "Instance 4"
or "identifiability-floor" that this plan does not name explicitly — and
either retire them or surface them in the verification step.

### 5.b PROPOSALS.md §D.9 retirement

The reserved-decision entry (`PROPOSALS.md` §D.9 "RESERVED DECISION
(2026-05-18)") is *the durable queue entry* per its own text. After
integration:
- Mark it CLOSED (or move to a "historical decisions" section if
  PROPOSALS.md has one — check the file's existing convention).
- Cross-reference the CHANGELOG entry from the closure.

The §D.9 entry's exact wording is the gold-standard summary of what
was decided; preserve its content in CHANGELOG, not just a pointer.

### 5.c spike-routing tracker (`spikes/ROUTING.md`)

Update the per-spike disposition in `spikes/ROUTING.md` to reflect the
integration:
- `spike-identifiability-floor-instance4-resolution-2026-05-18` →
  integrated, moved to `.integrated/`.
- `spike-identifiability-floor-instance-triage-2026-04-24` →
  integrated, moved to `.integrated/`.
- `spike-neutral-drift-endogenous-coupling-strengthening-2026-04-24` →
  partial-or-full integration depending on §4.c verification.
- `spike-rho-structure-recheck-2026-05-18` → partial-or-full integration
  depending on §4.d verification.

---

## 6. CHANGELOG.md entry (draft)

Per CLAUDE.md convention: CHANGELOG carries cycle narratives forward
from 2026-04-24. Draft entry for the executor to refine to the actual
landing date:

```
## 2026-MM-DD — `#disc-identifiability-floor` Instance-4 Resolution

The contested Instance 4 of `#disc-identifiability-floor` (KNOWN-DEFECTIVE
since 2026-05-18) resolved by integrating the 2026-05-18 resolution
spike's verdict: the slot conflated two distinct objects under one
ordinal. **Object A** (universal-$C$ under non-(PI) norms) is not a
floor instance — opposite external-theorem role, single forced escape
(Čencov-uniqueness), consequence-as-re-use rather than elevation — and
is now correctly classified in `#disc-additive-coordinate-forcing` as a
downstream theorem of the (PI) commitment, exactly as
`#deriv-observation-ambiguity-bias-bound` §4 already stated. **Object B**
(architecturally-distinct, behaviorally-identical agents unidentifiable
from on-policy summary data) is the genuine fourth floor and landed as
the new Instance 4: dual-anchored on Kalman-Ho 1966 canonical-form
non-uniqueness (linear-Gaussian sub-scope, exact) and Bareinboim et al.
2022 CHT-at-agent-as-SCM (general, robust qualitative). Mechanism:
Object B reduces to Instance-2's Fisher-information null space along a
structurally-forced indeterminacy manifold (the manifold being the
$GL(n)$ similarity fiber); Sylvester forbids the escape via
reparameterization at one remove. Three rank-collapse subclass members
({I1, I2, I4}) via Sylvester; one composition member ({I3}) via
projection / Schur-complement. Three structurally distinct escapes
(loop-interventional / higher-moment-in-nonlinear-scope / white-box
instrumentation); the proposed fourth (horizon extension under same
policy) collapses into the interventional one. The Regime-C confound
(CL-2's heavy reserved refinement) was proved (resolution spike §7) to
be Object B projected onto the disturbance-statistic coordinate — same
no-go, same escapes, same mechanism — so this landing simultaneously
discharges CL-2's heavy refinement and the Joseph-reserved
neutral-drift batch (one decision, not three). Per the spike-verify
gate (`spikes/.routing-trail/SPIKE-VERIFY-471802`, confirmer ≠ author):
the boxed "every moment of $\lVert\delta\rVert$ identical" claim was
restricted to innovation/output + similarity-invariant summaries; a
displayed Lyapunov-equation sign was corrected to the standard form;
the sub-scope (exact, Kalman) vs general (robust-qualitative, CHT) tier
boundary is carried consistently in the new Instance 4 entry. The Fano
finite-sample refinement (architectures close-but-not-equal in
innovation spectrum) is honestly open as separate research, not
overclaimed as the floor anchor.

Files: `01-aat-core/src/disc-identifiability-floor.md` (Object A removed,
Object B installed as Instance 4, Sylvester taxonomy repaired, Findings
+ Related Work rolled up); `01-aat-core/src/disc-additive-coordinate-
forcing.md` (Object A explicitly absorbed as downstream consequence of
(PI), with the floor-vs-coordinate-forcing distinction articulated);
`01-aat-core/src/[Object B math home — see §3.d]` (Kalman-Ho construction
landed in canon, not only in the spike). Integrated spikes
(`.integrated/`): `spike-identifiability-floor-instance4-resolution-
2026-05-18.md`, `spike-identifiability-floor-instance-triage-
2026-04-24.md`, and (verify-then-move) `spike-neutral-drift-…-
2026-04-24.md` + `spike-rho-structure-recheck-2026-05-18.md`. TODO
discharges: 143, 147, 441, 455. PROPOSALS §D.9 closed.
```

The executor refines the entry to the actual landing details (segment
names chosen per §3.d, etc.) and the date of the canon commit.

---

## 7. Cross-reference sweep

After the canon edits commit but before the spikes move to `.integrated/`,
the executor runs a verification sweep:

1. `grep -rn "Instance 4" 01-aat-core/src/` — confirm all references now
   point to Object B (or to the meta-segment in general). Any reference
   to the $C_{FR} = \sqrt{2}$ bias bound *as* a floor instance is a
   regression and gets redirected.

2. `grep -rn "KNOWN-DEFECTIVE\|category error" 01-aat-core/src/
   ref/` — confirm the KNOWN-DEFECTIVE marker is removed from the
   meta-segment and that "category error" appears only in the
   coordinate-forcing absorption (or in the CHANGELOG history).

3. `grep -rn "Object A\|Object B" 01-aat-core/src/` — these labels were
   spike-internal; canon body should not carry them. (The CHANGELOG and
   spike-trails properly preserve the labels for history.)

4. `bin/lint-md 01-aat-core/src/disc-identifiability-floor.md
   01-aat-core/src/disc-additive-coordinate-forcing.md
   01-aat-core/src/[Object B math home]` — clean lint required.

5. `bin/lint-outline` — confirm the dependency graph remains consistent
   (Object B's home segment, if new, gets `depends:` declared
   correctly; the meta-segment's `depends:` list updates if a new
   supporting segment was added).

6. **Cross-volume sweep:** Object B-related themes also touch
   `03-llm-core/` (wrapping at the LLM substrate may produce similarity-
   orbit-style indistinguishabilities; cf. row 05 in the prior-art
   analyses). The executor checks if any LLM-core segment references the
   Instance 4 question — likely not at this snapshot, but worth a quick
   `grep -rn "Instance 4\|identifiability-floor" 03-llm-core/
   04-eli-core/ 02-tst-core/`.

---

## 8. Order of operations

1. **Pre-flight:** Joseph commits any prior canon-touching work
   (per `feedback_commit_before_canon_modifying_spike`) so the spike's
   diff is isolated.

2. **Land Object B's math** in `01-aat-core/src/` (§3.d — judgment
   call: new appendix segment vs extending `#der-agent-opacity`). This
   is the foundation; the meta-segment summarizes it.

3. **Update the meta-segment** `01-aat-core/src/disc-identifiability-
   floor.md` (§3.a — remove Object A, install Object B Instance 4 entry,
   repair Sylvester Discussion, update Findings + Related Work). Apply
   the §2 math-gate repairs to the displayed math.

4. **Update `disc-additive-coordinate-forcing.md`** (§3.b — add the
   Object A absorption paragraph with the floor-vs-coordinate-forcing
   distinction articulated).

5. **Run cross-reference sweep** (§7) — fix any inconsistencies.

6. **Run `bin/lint-md` and `bin/lint-outline`** — must be clean.

7. **Update prior-art-analysis row 11** (§3.e) and meta-summary (§3.f).

8. **Update TODO.md** to retire items 143, 147, 441, 455 (§5.a). Update
   PROPOSALS.md §D.9 to closed (§5.b). Update `spikes/ROUTING.md`
   (§5.c).

9. **Draft + land CHANGELOG entry** (§6).

10. **Commit canon edits** as a single coherent commit (or a small set
    of focused commits — math first, then meta-segment, then
    cross-segment touches, then analysis + meta-summary, then
    TODO/PROPOSALS/CHANGELOG).

11. **Spike housekeeping** (§4): add integration notes to the four
    spikes; move the fully-integrated ones to `spikes/.integrated/`
    (the verify-before-archive ones — neutral-drift and rho-recheck —
    only move once their other content is also verified discharged).

12. **Final verification:** re-grep for "Instance 4" / "KNOWN-DEFECTIVE"
    / Joseph-reserved Instance-4 references across the repo to confirm
    no residue.

---

## 9. Verification — done when?

The integration is *done* when all of the following hold:

- `disc-identifiability-floor.md` lists four clean instances (I1, I2, I3,
  I4 = Object B) with the Sylvester taxonomy {I1, I2, I4} + {I3}; no
  KNOWN-DEFECTIVE warnings; no references to Object A as a floor; Findings
  count says "four" cleanly; Related Work table has Object B's row with
  Kalman-Ho + CHT dual-anchor.
- `disc-additive-coordinate-forcing.md` has the Object A absorption
  paragraph naming the floor-vs-coordinate-forcing distinction explicitly.
- Object B's math has a canonical home in `01-aat-core/src/` (segment
  name + status decided by executor).
- The §2 math-gate repairs are applied (moment-claim restricted, Lyapunov
  sign matches canon convention, sub-scope tier boundary explicit).
- `bin/lint-md` and `bin/lint-outline` clean on all touched files.
- TODO.md items 143, 147, 441, 455 retired (moved to CHANGELOG).
- PROPOSALS.md §D.9 closed.
- `spikes/ROUTING.md` updated.
- CHANGELOG entry landed with the canon files committed.
- `ref/prior-art-analysis/11-constructive-impossibility.md` updated;
  `ref/prior-art-analysis/00-impact-meta-summary.md` updated.
- Spike housekeeping per §4: integration notes added; fully-discharged
  spikes moved to `.integrated/`; partial spikes left at `spikes/` root
  with notes.
- Cross-reference sweep (§7) clean.

---

## 10. Known residual work (honestly out of scope for this plan)

These are *real* follow-on directions surfaced by the resolution; they
are honestly open and should not be pulled into this integration.

- **Fano finite-sample refinement.** Architectures close-but-not-equal
  in innovation spectrum (where $I(A; \text{obs}) > 0$ small) admit a
  Fano-style bound — this is the *finite-sample* version of Object B's
  no-go, distinct from the *exact-population* Kalman-Ho anchor. Open
  research, not blocked by anything in this plan; left as a candidate
  spike for a future cycle.

- **Mechanism-design impossibility (Gibbard-Satterthwaite +
  Myerson-Satterthwaite + Arrow) as a separate Implementation-
  Impossibility meta-segment** (per row 14's flagged Joseph-reserved
  item, separate from this integration). The GS arm was tested in
  `spike-4th-identifiability-floor-instance-2026-05-20` and routed to
  `#disc-separability-pattern` general-open tier; M-S + Arrow remain
  Joseph-reserved for the broader Implementation-Impossibility question.
  Out of scope here.

- **The general non-Gaussian sub-scope no-go for Object B.** The
  resolution spike anchored the general case via CHT-at-agent-as-SCM
  (robust-qualitative). Upgrading the general case to exact-with-
  conditions is real research, honestly open, not blocked.

---

*End of plan. The math is settled; the structural-canon disposition is
above. A single agent can execute this; the work is bounded by §9.
Truth above completeness — apply the §2 math-gate repairs; do not
collapse the sub-scope tier boundary; preserve the present-truth
discipline (Object A is deleted from canon, not kept-softened-with-a-
pointer; its history lives in CHANGELOG / spike-integration-trails).*
