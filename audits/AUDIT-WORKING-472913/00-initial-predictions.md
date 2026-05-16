# 00 — Initial Predictions

*De-novo audit cycle 472913. Auditor: Claude Opus 4.7 (1M context), Claude Code.
Written 2026-05-15, before reading any `src/` segment. Orientation reading
completed: top-level `OUTLINE.md`, `01-aat-core/OUTLINE.md`, `NOTATION.md`,
`FORMAT.md`, `LEXICON.md`. Scope (per Joseph's modifications): AAT volume only
(`01-aat-core/`); do not touch the 02/03/04 outlines or README/FINDINGS/etc.
until the AAT segments are done.*

---

## 0. Priming-bleed disclosure (read this first — it changes how to weight everything below)

This is the single most important calibration fact for this audit, so it goes first.

`CLAUDE.md` and the project `MEMORY.md` are **auto-loaded** by Claude Code into
my context before the audit began. I did not choose to read them; the harness
injects them. They are *substantially* priming-heavy for the meta-architectural
layer of this framework. Specifically, before reading a single segment I already
"know" (from CLAUDE.md / MEMORY.md):

- The GUC Class 1/2/3 (Separated / Partial / Coupled) partition and the
  2026-05-09 renumber, including the historical→current table.
- The four meta-patterns by name and one-line gloss: M1 identifiability-floor,
  M2 separability-pattern, M3 additive-coordinate-forcing, M4
  modularity-state-dynamics (M4 explicitly *not yet landed* — `disc-modularity-state-dynamics.md`
  is missing; cross-refs are forward-references).
- The "stability certificate" spine framing and its four-facet decomposition.
- "Directed separation is architectural, not parametric; κ-as-scalar is a
  category error."
- The named "genuinely novel results" from MEMORY.md: P3→Markov, acyclicity
  from temporal ordering, satisfaction-gap / control-regret split, $G_t$
  complexity bounded by $M_t$ capacity, feedback loop as Level-2 causal engine.
- The "Known Fragilities" list (missing commitment/resource/temporal DAG
  structure; directed-separation violated by goal-conditioned agents, addressed
  via the wrapping construction with W₁/W₂ leakage bounds).

On top of that, the **`01-aat-core/OUTLINE.md` preamble itself** ("Reading AAT
— the mental model first" / "— the precise structure" / "On mathematical
precision" / the Part II scope-lattice) is unusually priming-rich for an
auditor-safe document. It states the whole cross-sectional thesis (certificate
+ four facets), names which results are "headline," states which sections are
"most locked down" vs "open formulation," and pre-states the 16/24 survival
classification. The de-novo instructions explicitly bless reading the OUTLINE,
and Joseph explicitly directed me to it, so this is sanctioned — but it means
my judgment about *what is distinctive / load-bearing / novel* is **not
de-novo**. I am inheriting the framework's own self-assessment of its
architecture.

**The honest split, which I will hold throughout:**

- **Priming-contaminated axis** (discount my findings here heavily; they
  may just be re-confirming the framework's self-narrative): claims about
  which results are central, the meta-pattern architecture, the "what's
  novel" story, the certificate spine.
- **Still genuinely de-novo axis** (these findings retain weight): per-segment
  *math correctness* (I have read zero derivations), *cross-segment drift*
  around recent additions, *status-label accuracy* against actual derivation
  strength, *worked-example computation*, *dependency-graph / OUTLINE-order
  violations*, *whether the OUTLINE preamble's confident framing is actually
  cashed out in the segments it points to* (this last one is interesting —
  the priming itself becomes a verification target: does the segment deliver
  what the preamble advertises?).

A useful inversion: because I have been so heavily primed on the *story*, the
highest-value thing this audit can do is treat the story as a set of
**falsifiable promissory notes** and check whether the segments pay them.
"The OUTLINE says Part I is the most mathematically locked down" is a testable
claim about `deriv-sector-condition`, `result-persistence-condition`, etc., not
a fact I should accept.

---

## 1. Topology of the framework as I understand it

AAT is the mathematical core of Agentic Systems. One volume, three Parts plus
two appendix groups, walked in OUTLINE row order:

- **Part I — Adaptive Systems Under Uncertainty.** The general adaptive agent:
  agent/environment boundary, lossy observation, chronica, the reality model
  $M_t$ as compressed history, the cycle (Prolepsis→Aisthesis→Aporia→Epistrophe→Praxis),
  mismatch $\delta_t$, update gain $\eta^\ast$, adaptive tempo $\mathcal T$,
  and the persistence machinery (sector condition → Lyapunov → persistence
  condition $\alpha > \rho/R$). This is claimed to be the most rigorous part.
  ~30 segments incl. chapter intros.
- **Part II — Agentic Systems: Actuated Adaptation.** Adds objective $O_t$ and
  strategy $\Sigma_t$ ($G_t = (O_t,\Sigma_t)$, $X_t = (M_t,G_t)$). Directed
  separation (epistemic update goal-blind) as a *scope condition* gating which
  results apply. Pearl/Bareinboim causal hierarchy, the loop as a Level-2
  engine, the strategy DAG (AND/OR, single-parameter edges), the
  satisfaction-gap / control-regret diagnostic split, the orient cascade.
  Scope lattice: adaptive ⊃ agency ⊃ learning-agent ⊃ Class-1. ~35 segments.
- **Part III — Agentic Composites.** Composition closure (defect $\varepsilon^\ast$),
  team/adversarial persistence as signed coupling, unity dimensions,
  class-coercion-via-wrapping, strategic composition via potential/monotone
  games. Flagged in the preamble as depending on "admissibility choices that
  are formulated, not derived, and a bridge lemma that requires a contraction
  assumption beyond the stated admissibility constraints." ~25 segments + 4
  trailing population-dynamics GAPs.
- **Appendix A — Details.** The derivation-heavy backbone: `deriv-sector-condition`,
  `result-sector-persistence-template`, `result-certificate-existence`,
  discrete sector condition + fluid limit, `deriv-graph-structure-uniqueness`
  (the CMC/Markov derivation), the four meta-segments (M1/M2/M3 + the
  *missing* M4), the Class-3 bias-bound theorem, Fisher/Čencov coordinate-forcing
  derivations. This is where the OUTLINE says the real proofs live and where,
  per §3.5, structurally consequential material hides.
- **Appendix B — Operational Domains.** Worked examples: Kalman (exact),
  bandit (approximate), strategy DAG 3-arm bandit, L1 augmented DAG, CAM
  (missing). Per §5.1 these get math computed first-hand, not paraphrased.

Load-bearing structure (per the framework's own telling, hence
priming-contaminated): the equilibrium **stability certificate** as the single
cross-sectional object; existence ⟺ exponential stability via a converse-Lyapunov
argument (`result-certificate-existence`); the sector-persistence template as
the reusable Lyapunov engine instantiated ≥6 times; `deriv-graph-structure-uniqueness`
as the strongest genuinely-novel structural result; directed separation as the
scope hinge that the entire Part-II/III applicability story rotates on.

Integration story: AAT's claimed contribution is *integration not invention* —
control theory (Lyapunov/contraction/sector), causal inference (Pearl/Bareinboim/CMC),
information theory (IB/rate-distortion/Čencov), and agent architecture, unified
by the adaptive cycle as the unit of analysis. The distinctive overlay on top
of "integration" is the *epistemic-architecture* reading (scope-of-existence /
forced-identity / boundary / projection-behaviour).

## 2. Predictions about what each component contains (falsifiable)

**Part I.**
- `der-recursive-update` + `deriv-recursive-update`: a uniqueness argument
  ("three constraints → unique recursive form") with explicit counterexamples
  for dropping each constraint. **Prediction:** the three constraints will be
  something like (i) bounded memory / Markov-sufficiency, (ii) consistency
  under event reordering or associativity, (iii) some optimality/no-loss
  condition. I predict at least one constraint is doing more work than stated
  and is closer to a formulation choice than a forced constraint. Falsifiable:
  if all three are genuinely independent and each counterexample is tight, I'm
  wrong.
- `result-mismatch-decomposition`: bias/variance-style identity, $\delta$ =
  model-error + observation-noise, requiring GA-1 (fresh noise). **Prediction:**
  clean and correct; the only risk is the cross-term vanishing relying on
  GA-1 more strongly than the segment foregrounds (an independence assumption
  doing quiet work — candidate scope/status item).
- `result-sector-condition-stability` + `deriv-sector-condition`: Lyapunov
  $V = \tfrac12\lVert\delta\rVert^2$, $\dot V \le -\alpha\lVert\delta\rVert^2 + \rho\lVert\delta\rVert$,
  ultimate bound $R^\ast = \rho/\alpha$. **Prediction:** correct for the
  continuous Model-D case; the subtle spot is the discrete-time analog (DA2')
  needing the *extra* Lipschitz upper bound — I predict the OUTLINE's claim
  that this "closes GA-5 / the fluid-limit gap" is the single most fragile
  load-bearing junction in Part I and the place a sign/inequality-direction
  error is most likely to have survived. Flag `deriv-discrete-sector-condition`
  for first-hand math.
- `emp-update-gain`: $\eta^\ast = U_M/(U_M+U_o)$, Kalman-like. Tagged
  *empirical* — **prediction:** it is actually derivable (it's the scalar
  Bayesian posterior-precision weight) and the *empirical* tag is a
  conservative label; Appendix A's `deriv-fisher-local-update-gain` likely
  derives it. Potential status-label finding *in the strengthening direction*
  (the honest move per CLAUDE.md is to check whether it can be promoted, not
  whether the tag is "fine").

**Part II.**
- `der-directed-separation`: the hinge. **Prediction:** stated as
  Derived+Scope, `status: draft`. I predict the "derived" half is genuinely a
  *definitional consequence given the scope condition* (so the real content is
  the scope condition, not a theorem), and that the κ-quantified Class-2 case
  is the under-derived spot. Watch for: the OUTLINE preamble's confident "16/24
  survive exactly" not actually being cashed out segment-side, or being cashed
  out only in `result-section-ii-survival` with the per-result mapping thinner
  than advertised.
- `deriv-graph-structure-uniqueness`: 4 postulates + causal sufficiency →
  Markov-factorized DAG via CMC. **Prediction:** this is the crown jewel and
  also where the gap between "Cox-analog inevitability" framing and what is
  actually proved is most likely to be wide. I predict the CMC (Causal Markov
  Condition) is *invoked* (Pearl/Bareinboim) rather than derived, and the
  novel content is the claim that the four operational postulates *imply CMC's
  preconditions* — that implication is the thing to audit hardest.
- `def-satisfaction-gap` / `def-control-regret`: arithmetic once value objects
  defined; the insight is the *split*. **Prediction:** correct as arithmetic;
  the audit risk is the *convention hierarchy* (C1/C2/C3) being claimed to
  "lift the inferential force" with the monotonicity argument being weaker
  than asserted (a Discussion-grade claim wearing Derived clothing — exactly
  the Gate-2 failure mode CLAUDE.md names).

**Part III.**
- `form-composition-closure`: closure defect $\varepsilon^\ast$, a bridge
  lemma requiring a contraction assumption beyond admissibility. **Prediction
  (high-confidence, because the OUTLINE volunteers it):** the bridge lemma is
  the weakest load-bearing link in the whole volume. The honest audit move per
  CLAUDE.md is *not* "flag it as overclaimed" (it already self-flags) but to
  check whether the contraction assumption can be discharged from admissibility
  + something mild, i.e., attempt the strengthening.
- `der-class-coercion-via-wrapping` / `-in-composition`: the W₀/W₂/W₁ regime
  hierarchy; the formal route from Class-3 LLM components to Class-1 composites.
  **Prediction:** structurally clean; the soft spot is the *leakage-rate
  bound* — whether W₂'s "behavioral" bound is actually a bound or an estimate,
  and whether the pretraining-correlation residual is quantified or hand-waved.

**Appendix A.**
- `result-certificate-existence`: the converse-Lyapunov anchor. **Prediction:**
  this *is* a classical theorem (Lyapunov / Massera-type converse) recapitulated;
  novelty is the *recognition* that AAT's organizing slogan = this theorem.
  Risk: the local/linearized restriction ("Exact (linearized/local)") being
  silently dropped when the spine narrative ("contraction outpaces drift is a
  theorem not a vibe") is invoked downstream globally. **This is my single
  highest-prior cross-segment-drift prediction:** a local/linearized result
  used with global rhetorical force in preambles/impl segments.
- The meta-segments M1/M2/M3 present; **M4 `disc-modularity-state-dynamics`
  MISSING** (OUTLINE marks it `missing`). Cross-refs to `#disc-modularity-state-dynamics`
  from impl-segments and CLAUDE.md will be forward-references. **Prediction:**
  some impl segment cites it as though it carries weight it cannot, because the
  file does not exist — a forward-reference-as-load-bearing finding. (Need to
  confirm OUTLINE-position so this isn't a known/acknowledged gap; CLAUDE.md
  says the forward-ref convention is deliberate, so this likely lands in §D
  not §B.)

**Appendix B.**
- `example-kalman` (exact): **prediction:** the Kalman steady-state gain and
  the persistence condition will be claimed to instantiate exactly; the place
  to compute first-hand is whether $\eta^\ast = U_M/(U_M+U_o)$ matches the
  scalar Kalman gain $K = P^-/(P^-+R)$ with $P^-$, $R$ correctly identified —
  and whether the persistence condition's $\alpha$ maps to the correct
  Riccati/closed-loop rate (sign and which matrix).
- `worked-example-cam`: MISSING (Miller 2022 CAM). Acknowledged gap, likely §D.

## 3. Predictions about what's open

- The four trailing Part III GAPs (latent structural diversity, endogenous
  coupling, composition-transition motifs, computational thresholds) — openly
  marked, so §D/§E material not §B.
- M4 modularity-state-dynamics segment unwritten (acknowledged in CLAUDE.md).
- Part III admissibility + bridge lemma: open by self-admission.
- Class-2 (Partial) κ-quantified directed-separation: I predict this is the
  least-developed of the three GUC classes (Class-1 by construction, Class-3
  via bias-bound theorem, Class-2 "the analog … is open" per NOTATION's $f_M$
  row — already half-confirmed by NOTATION).
- `schema-strategy-persistence` is `proposed-schema` type — formal content
  pending by its own label.

## 4. Predictions about what's overclaimed (where framing may outrun math)

Ranked by my prior:

1. **`result-certificate-existence` local→global drift** (above). The OUTLINE
   preamble's "this is a theorem and not a vibe" is exactly the rhetorical
   register that, per the project's own epistemic discipline, should trigger
   verification. Highest-value single check in the audit.
2. **Convention-hierarchy monotonicity (C1<C2<C3 "inferential force").** I
   predict a Discussion-grade plausibility argument presented with Derived
   force. (Gate-2 canonical failure mode.)
3. **"16/24 survive exactly" survival classification.** Prediction: the
   *count* is real but at least one of the 16 is a survival-by-relabeling
   (the definition transfers because it's definitional, which is not the same
   as the *result* surviving). Worth a spot check of 2–3 of the 16.
4. **Sector condition GA-3 "derived from the gain principle when … directional
   fidelity (B1)".** NOTATION already says it "remains an independent
   assumption for non-gradient agents." Prediction: somewhere a result that
   needs GA-3 is stated with universal force while GA-3 only holds for the
   gradient sub-case — a scope-honesty/propagation finding.
5. **`der-tempo-composition` "Brooks's Law derived from closure"** (typed
   `Sketch` in OUTLINE — so likely honestly labeled; prediction: fine, but the
   sub-additivity inequality direction is a good first-hand check).

## 5. What I'd expect to be most novel and consequential (if it lives up)

- `deriv-graph-structure-uniqueness`: operational postulates → Markov DAG. If
  the postulates→CMC-preconditions implication is tight, this is the real
  contribution and is genuinely novel as a *derivation* (vs. assuming CMC).
- The satisfaction-gap / control-regret *orthogonal split* as a diagnostic —
  the value is the decomposition, and it's the kind of thing that is obvious
  once seen and hard to see, which is a good novelty signature.
- The sector-persistence template as a single Lyapunov engine reused ≥6×:
  consequential because economy-of-machinery *is* a contribution in an
  integration framework.
- Class-coercion-via-wrapping as a *constructive* truthification mechanism:
  if the leakage bound is real, this is the bridge that makes the whole
  03-llm-core/04-eli-core program formally legitimate. High consequence.

## 6. What kinds of findings I expect to surface

In rough expected-frequency order:
1. **Scope/status mismatch & local→global drift** (caveat in Working Notes or
   Epistemic Status, punchline universal in OUTLINE/impl/preamble). Highest
   expected count — the framework is large, fast-moving, and self-narrates
   confidently in framing prose.
2. **Cross-segment drift around recent additions** (GUC renumber 2026-05-09;
   AAT rename 2026-05-15 — *two days ago*; M4 forward-refs). The AAT→AAT
   rename being 24h old makes "historical-naming-statement" residue and
   stale cross-refs a live prediction.
3. **Status-label, often in the *strengthenable* direction** (empirical tags
   on derivable claims) — and per CLAUDE.md the correct write-up is "attempt
   strengthening," not "soften the label."
4. **Math**: sign / inequality-direction / which-matrix errors concentrated in
   the *less-audited back* (Appendix A Fisher/Čencov derivations, discrete
   sector, critical-mass composition) per §3.3's "front over-verified, back
   under-verified."
5. **Dependency-graph / OUTLINE-order violations**: a non-appendix backward
   pointer. Lower prior (the OUTLINE is actively linted) but exactly the
   §4.2 critical-finding class, so watched every segment.
6. **Forward-reference-as-load-bearing**: M4 and possibly others.

Specific falsifiable bets I will grade at the end:
- (B1) `result-certificate-existence` is local/linearized and at least one
  downstream framing uses it globally. *Prior: 0.6.*
- (B2) `deriv-discrete-sector-condition` has a tight, correct fluid-limit
  argument (no error). *Prior: 0.55 — i.e., I expect it's probably fine but
  it's the likeliest place for a real Part-I math error.*
- (B3) The convention hierarchy C1/C2/C3 monotonicity is argued
  discussion-grade but presented as derived somewhere. *Prior: 0.5.*
- (B4) At least one of the "16/24 survive" cases is survival-by-definitional-
  relabeling rather than result-survival. *Prior: 0.45.*
- (B5) `emp-update-gain` is strengthenable to derived (and Appendix A already
  effectively does it), making the `emp-` slug/tag a candidate for the
  strengthen-not-soften treatment. *Prior: 0.6.*
- (B6) At least one stale "AAD" or pre-2026-05-09 GUC-class numbering survives
  in a non-frozen AAT segment (rename was 2026-05-15). *Prior: 0.4.*
- (B7) Zero non-appendix backward `depends:` violations (OUTLINE order holds).
  *Prior: 0.7 that it holds.*

## 7. Process note on the diagram modification

Joseph's modification: keep Wandering Thoughts to ~2 paragraphs, then for each
segment design a diagram/illustration of the *new understanding* — iterate
TikZ `.tex` files (same basename as the reflection file) with the lualatex
harness, compile, inspect, iterate until it illuminates. I read this as: the
diagram is itself a comprehension instrument and a candidate pedagogical
artifact for the monograph's "respectful pedagogy / mental-model-first"
direction (cf. CLAUDE.md). The discipline I'll hold: the diagram must be
*isomorphic, not merely evocative* (the same standard CLAUDE.md sets for
Feynman-criterion analogs) — a reader perturbing the diagram should get
predictions that hold against the formalism. A pretty box-and-arrow that
doesn't carry load is worse than none. Several iterations / several distinct
visual idioms (not just node-graphs: phase portraits, commutative diagrams,
Hasse/lattice diagrams, contraction-funnel pictures, Venn/region diagrams,
timeline/cascade diagrams, before-after pairs) considered per segment.

---

*Predictions locked. I will grade B1–B7 explicitly in the FINAL §C/§E and
revisit this file at the §4.5 strategic-loop checkpoints (~every 10 segments).*
