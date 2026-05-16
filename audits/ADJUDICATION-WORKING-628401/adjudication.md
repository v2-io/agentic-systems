# Adjudication — Cluster B (math-heavy ledgered cycles)

**Adjudicator:** Claude Opus 4.7 (1M context), fan-out agent (Cluster B)
**Date:** 2026-05-16
**Working dir:** `audits/AUDIT-WORKING-628401/`
**Slice:** `audit-584721-FINAL-2026-04-25.md`, `audit-613842-FINAL-2026-04-25.md`,
`audit-742613-FINAL-2026-04-25.md` + `audit-742613-SUPPLEMENT-PHASE-2-TRIAGE.md`,
`opus-audit-2026-04-21.md`, `audits-2026-04-22-evening.md`, `audit-738192-FINAL.md`
**Ledgers read as evidence (durable — not graduated, not edited):**
`pending-findings-2026-04-21.md`, `-2026-04-22.md`, `-2026-04-23.md`

**Standing rule applied:** route, don't execute. Disposition = *where each
finding belongs*, not *whether we did what it asked*. Strengthen-before-soften
is live and this slice is exactly where it bites — math-heavy cycles where the
discharge direction matters. No segment / tracking file edited; every
consequential and every still-open finding verified **first-hand against
current `01-aat-core/src/` and `03-llm-core/src/`** (git-recency poisoned by the
2026-05-15 rename sweep — I read the files, ran `bin/lint-outline`, not the log).

---

## Headline

**This slice is overwhelmingly closed *in the right direction*, and the
direction is the project's signature one: the math-heavy auditor findings were
discharged by *strengthening the theory*, not by softening claims to match a
weaker delivery.** Of ~30 distinct findings across 7 files:

- **~25 resolved**, the large majority **by strengthening** (the discharge this
  project prefers) — several visibly delivering *more* than the audit asked
  (uniqueness theorems, no-go boundary results, new theory routes).
- **1 genuinely actionable-open**, verified live in current `src/` today:
  the Model-S `P(τ_R < ∞)` ever-exit conflation (742613 F2 / 613842 F2) —
  a real math defect where the ledger's *recorded recommendation is a
  soften* and the correct discharge is a *strengthening* (maximal-inequality
  route). This is the slice's key surfacing. (The `git checkout`-as-L3
  finding, 738192 F2, initially read as live from the
  `def-pearl-causal-hierarchy` recap line but is **resolved by
  strengthening** in the canonical TST segment — see §6; cross-component
  verification was load-bearing there. A one-word recap-precision nudge
  remains as optional soft-polish.)
- **1 partial-residual, routed** (adaptive-tempo `status: exact` vs.
  overcounting — 742613 F4 / 613842 F1 / Gemini-evening F3): substantially
  mitigated by strengthening (matrix-Loewner form now canonical), narrow
  frontmatter/formal-layer residue, already backlinked at TODO:395 /
  TODO:126.
- The rest: **subsumed**, **duplicate** (cross-file), **correctly-rejected /
  scope-honest**, or **soft / bigger-picture → polish-and-sentiment ledger**.

The strengthen-before-soften reframe had **maximum bite here** and the project
*passed it repeatedly*. The dominant pattern across opus-2026-04-21,
742613, and the evening batch is precisely the canonical one in
`strengthen-before-soften.md`: an auditor flags an inconsistency between a
strong claim and what a segment delivers; the project does **not** word-swap
the claim weaker — it derives the segment up to (and past) the claim. The
single live math defect (A) is the one place that discharge has *not yet*
happened — and the ledger's recorded recommendation for it is a soften, which
is the wrong direction and is flagged below as the slice's most important
surfacing.

---

## File-by-file, finding-by-finding

### 1. `audit-584721-FINAL-2026-04-25.md`

Three finding-clusters (§B). The §A items are audit-instruction stress-test
(process-feedback), §D is bigger-picture (Hypothesis-tier), §E is confirmation.

#### B.1 — Finding F-A (depends-list incomplete vs Formal-Expression-uses; 7 instances F-A0..F-A6)
- **Valid in the first place?** Yes — verifiable mechanical FORMAT.md Gate-1
  violations, audit characterized them precisely.
- **Valid as of today? NO — RESOLVED, comprehensively.** First-hand frontmatter
  check of all 7:
  - F-A0 `def-observation-function`: `depends: [def-agent-environment,
    **def-action-transition**]` — root-cause fix landed.
  - F-A1 `scope-adaptive-system`: `depends: [..., **def-chronica**]` — landed.
  - F-A4 `form-event-driven-dynamics`: `depends: [..., **form-agent-model**]` —
    landed.
  - F-A2 `form-information-bottleneck`, F-A3 `def-model-sufficiency`,
    F-A5 `def-mismatch-signal`, F-A6 `result-mismatch-decomposition`: all
    carry `def-action-transition` (transitive propagation from F-A0 done).
  - `bin/lint-outline`: **0 ordering violations, 0 missing dependencies, 0
    orphans** (current run). The audit's own pattern-level recommendation
    (a depends-graph lint) is in place and clean.
- **What it really is:** defect (Gate-1 bookkeeping drift), **resolved by
  extending the discipline to cover the gap** — the project's signature
  closure, not a softening.
- **Route:** `resolved` — MANIFEST note "F-A0..F-A6 all carry the flagged
  dependency; lint-outline clean." No blocker.

#### B.2 — Finding F-D (incomplete propagation of the 2026-04-24 BH-identity upgrade; F-D1, F-D2)
- **Valid in the first place?** Yes (medium-high; the audit itself flagged its
  CLAUDE-2.md-priming dependency and deferred first-hand verification).
- **Valid as of today? NO — RESOLVED *by strengthening*.** First-hand:
  - F-D1 `disc-ciy-unified-objective.md:66`: now states the Bretagnolle-Huber
    identity holds *exactly* under deterministic π\*, gives the tight regret
    bound **and a matching lower bound** `Δ_min(1 − e^{−D_KL})` the audit did
    not ask for; Pinsker explicitly retained as the correct loose
    stochastic-π\* form.
  - F-D2 `form-strategy-complexity-cost.md:141`: BH-identity now "the primary
    form"; Pinsker retained *with documented IB-shape-alignment trade-off*.
- **What it really is:** integration-debt finding, discharged past the ask
  (lower bound added). Canonical strengthen-first shape.
- **Route:** `resolved` (by strengthening) — MANIFEST note.

#### B.3 — Finding F-B1 (low-confidence: stale "Section IV" / `AAD-FULL.md` ref in `form-event-driven-dynamics`)
- **Valid in the first place?** Candidate, auditor-flagged medium-low,
  unverified by them.
- **Valid as of today?** I checked `form-event-driven-dynamics.md` first-hand:
  no `AAD-FULL.md` and no "Section IV" reference present in the current
  segment (the segment was rewritten; the doc-rot reference is gone). `grep`
  confirms no `AAD-FULL` anywhere in `01-aat-core/src/`.
- **What it really is:** doc-rot candidate, **resolved** (reference no longer
  exists; the AAD→AAT-era rewrites cleared it).
- **Route:** `resolved` — MANIFEST note "stale ref absent from current
  segment."

#### §A.1–A.4 — Instructions stress-test (4 items)
Not framework findings. Feedback on the *de-novo audit instructions* (the
§4.4 cadence-failure 3/3-first-runs lesson; auto-load priming structural
problem; OUTLINE-linearization refinement; prompt-12/13 expansion). High-value
durable instruction-improvement signal — the kind the spine warns is
historically discarded.
- **Route:** `process/instruction-feedback` → polish-and-sentiment ledger,
  themed *audit-process / instruction improvements*, attributed 584721 §A.
  (Cross-note: 471203 §G and 742613/613842 process-feedback land in the same
  theme — dedupe there; the §4.4-cadence and CLAUDE.md-bleed lessons recur
  across 4 of this slice's files and 471203, so the theme entry should be
  *consolidated*, not 4 separate rows.)

#### §D.1–D.8 — Bigger-picture (Hypothesis-tier; 8 items)
All auditor-marked Hypothesis. Triage:
- **D.1** six-mechanism shallow-plan convergence → **research-seed** (ledger;
  PROPOSALS-candidate if a consolidating meta-observation is pursued — natural
  `#disc-separability-pattern` extension).
- **D.2** OKR/AAT operational-mapping as a *template* for other domains →
  **research-seed** (ledger; this is a concrete approachability/Feynman move,
  flag as PROPOSALS-candidate-if-pursued).
- **D.3** correction-capacity-collapse unification (gain-collapse /
  catastrophic-forgetting / detection-latency / stability-myopia as one
  pathology) → **research-seed** (ledger); strong candidate — note it
  *overlaps* the M4 modularity-state-dynamics territory and the
  `#disc-correction-capacity-collapse` shape; surface to parent as
  possibly-already-in-PROPOSALS-orbit.
- **D.4** forced/matched/adopted coordinate tabulation in
  `#disc-additive-coordinate-forcing` → **soft-polish** (ledger; small,
  high-confidence, strengthens an existing meta-segment's scope-honesty —
  candidate co-owner direct-fix, parent's call).
- **D.5** CLAUDE.md/MEMORY.md auto-load = structural Claude-Code-native
  problem → `process/instruction-feedback` (ledger; dup of §A.2 — fold).
- **D.6** type/token distinction foregrounded in `03-llm-core` →
  **research-seed** (ledger; concrete, PROPOSALS-candidate-if-pursued).
- **D.7** diagnostic-CIY four-axis propagation to
  `#disc-exploit-explore-deliberate` → **soft-polish** (ledger; editorial
  propagation pass, candidate direct-fix).
- **D.8** seven-attack discipline as a FORMAT.md convention for
  inevitability-core segments → **research-seed / process** (ledger; FORMAT
  convention candidate).
- **Route (all §D):** polish-and-sentiment ledger, themed *framework-scope
  observations / research-seeds* attributed 584721 §D. None rises to a
  standalone PROPOSALS schema entry unattempted; D.1/D.3 are the strongest
  PROPOSALS-candidates-if-pursued and D.3 should be checked against the M4
  cycle before filing (possible subsume).

**584721 graduation readiness:** all framework findings closed-in-the-right-
direction (F-A resolved, F-D resolved-by-strengthening, F-B1 resolved). §A/§D
→ ledger. **Ready to graduate** once §A/§D mirrored to ledger. No live blocker.

---

### 2. `audit-742613-FINAL-2026-04-25.md` + `-SUPPLEMENT-PHASE-2-TRIAGE.md`

Codex partial Section-I de-novo, 8 findings. The SUPPLEMENT *is* this cycle's
resolution ledger (per-finding Phase-2 triage vocabulary + recommended
repairs). I re-verified every finding against current `src/`; the SUPPLEMENT's
*classifications* were directionally right but **its recommended repairs were
soften-direction for F2/F3/F4 — and the project (correctly) did not take them
for F3; for F2 nothing landed and the soften is still the recorded
recommendation, which is the slice's key surfacing (see §"Live items").**

#### F1 — Score-function mismatch reversed sign (`def-mismatch-signal`)
- **Valid in the first place?** Yes — high-confidence, clean Gaussian
  counter-derivation (likelihood-increasing direction is `+∇log P`, segment
  had `−∇log P`). SUPPLEMENT classed it "likely new / not durably tracked."
- **Valid as of today? NO — RESOLVED.** `def-mismatch-signal.md:34` now reads
  `\tilde{\delta}_t = \nabla_M \log P(o_t | M_{t-1}, a_{t-1})` (minus sign
  removed), line 36 "points in the direction the model should move to increase
  the likelihood … Under Gaussian models, they coincide up to scaling" — now
  internally consistent. Exactly the SUPPLEMENT §1 repair.
- **What it really is:** genuine local math bug, **resolved** (sign corrected;
  this is a correctness fix, the honest discharge — there is no "stronger"
  claim to reach for, the segment was simply wrong and is now right).
- **Route:** `resolved` — MANIFEST note.

#### F2 — Model-S local stochastic persistence: fixed-time tail ⇏ ever-exit probability (`deriv-sector-condition`, propagated to `result-sector-persistence-template`, `result-persistence-condition`)
- **Valid in the first place?** Yes — **high confidence, mathematically
  correct.** For OU/Brownian-driven `dδ = −αδ dt + σ dW`, the stationary law
  has unbounded support, so `P(τ_R < ∞) = 1` for any finite `R` — the
  process exits any finite ball a.s. in finite time. Markov's inequality
  bounds the *fixed-time / stationary* tail `P(‖δ(t)‖ > R)`, **not** the
  infinite-horizon first-exit probability.
- **Valid as of today? YES — STILL LIVE, NOT FIXED.** First-hand,
  `deriv-sector-condition.md`:
  - line 194 (iii): literally `$P(\tau_R \lt \infty) \leq n\sigma_w^2/
    (2\alpha R^2)$` — the exact false object.
  - line 242 proof: *"For (iii), standard tail estimates on the supermartingale
    $V(\delta(t))\mathbb 1_{\{t\le\tau_R\}}$ yield the non-exit probability."*
    — this is the conflation, asserted as proved.
  - line 253, 270, 282 (summary table + Epistemic Status): repeat
    "non-exit probability ≥ 1 − nσ²/(2αR²)" and call A.1S **exact** with
    "no implicit strengthening of A2' required."
  No active TODO/PROPOSALS backlink (`grep` clean for A.1S / ever-exit /
  742613 / 613842 in TODO + PROPOSALS).
- **What it really is:** **defect — actionable-open.** The notation
  `P(τ_R < ∞)` denotes the ever-exit probability; the segment claims it is
  bounded `< 1`; that is false under the segment's own stated OU/Brownian
  model. The *stopped bound* (i) and the *mean-square persistence* (ii) are
  fine — the defect is localized to (iii) and its propagation into the
  summary segments and the "exact" status claim.
- **Strengthen-before-soften ruling (the slice's crux).** The
  742613-SUPPLEMENT §2 and the parallel 613842-F2 both recommend a
  **softening**: "replace `P(τ_R < ∞)` with a fixed-time / stationary /
  finite-horizon probability," or "frame `R_S* < R` as a typical-scale
  condition rather than an infinite-horizon persistence guarantee." Per
  `strengthen-before-soften.md`, the strengthening attempt must be made
  *first* and on the evidence it is *available and standard*: the quantity
  the segment actually wants — "the agent stays within the sector region
  with high probability over all time" — is bounded by a **maximal
  inequality**, not by the (false) first-exit-via-Markov route. The
  Itô-Lyapunov supermartingale `V(δ_{t∧τ_R})` already in the proof yields,
  via Doob's / Ville's supermartingale maximal inequality (equivalently
  Khasminskii 2012 ch. 5's stochastic-stability theorem, *which the segment
  already cites*), a genuine infinite-horizon bound of the form
  `P(sup_{t≥0} ‖δ(t)‖ > R) ≤ (V(δ(0)) + drift-integral) / (R²/2)` — i.e.
  the *sup over all time* exit probability is bounded, which is *strictly
  the claim the segment is reaching for* and is *stronger* than any
  fixed-time restatement. This is a textbook-lemma strengthening (the
  citation is already in the file), exactly the
  `strengthen-before-soften.md` §"Escalation path" pattern where the
  obstruction dissolves under spike-mode attention. **The soften recorded
  in the ledger is the wrong discharge direction and should not be
  ratified.** Recommended: parent routes this to a strengthening spike
  (not TODO-as-soften, not the SUPPLEMENT's restatement). If the maximal-
  inequality strengthening fails (it should not — it is standard Khasminskii),
  the honest fallback is the SUPPLEMENT's fixed-time restatement *with the
  failure documented*.
- **Route:** `actionable-open` → **strengthening spike** (parent/Joseph;
  high-capacity, peer-voiced, three-completion-states brief; the maximal-
  inequality route is the lead). This is the one finding in the slice where
  the recorded resolution recommendation is anti-methodology and the
  surfacing matters. It does **not** block 742613-FINAL's graduation as a
  *file* (the finding is captured here with its correct discharge direction,
  and the FINAL+SUPPLEMENT are the durable ledger), but it must be carried
  forward as an open strengthening item, not closed.

#### F3 — Gradient "equivalence" overstates one-point sector as local strong convexity (`deriv-gain-sector`, `der-gain-sector-bridge`)
- **Valid in the first place?** Yes — high confidence; the auditor's
  `L'(x)=x(1+½sin 10x)` counterexample is correct (one-point sector at M\*
  ⇏ all-pairs strong monotonicity). SUPPLEMENT classed "known distinction,
  unrepaired offender."
- **Valid as of today? NO — RESOLVED *by strengthening*.**
  `der-gain-sector-bridge.md:85` now reads: local strong convexity is
  *sufficient* for B1 and **bidirectionally equivalent to the two-point /
  incremental sector condition (DA2'-inc)** — "The reverse implication
  B1 ⇒ strong convexity does *not* hold without the two-point upgrade: the
  one-point sector at M\* is strictly weaker … (counterexample in Prop B.4)."
  The false unconditional iff was not word-swapped weaker — it was replaced
  with a *sharper, correct* characterization that names exactly which
  condition the iff *does* hold against (DA2'-inc) and embeds the
  counterexample. The secondary Poisson-Fisher global-bound implication
  (742613 F3 "secondary") is addressed by the sub-scope α/β partition now
  carried in `deriv-sector-condition.md:278` and the natural-parameter
  treatment.
- **What it really is:** strengthen-first success — soften-candidate became a
  precise bidirectional-against-the-right-condition theorem + retained
  counterexample.
- **Route:** `resolved` (by strengthening) — MANIFEST note.

#### F4 — Adaptive tempo `status: exact` while segment says additive formula overcounts (`def-adaptive-tempo`)
- **Valid in the first place?** Yes — high confidence; frontmatter/formal-layer
  vs. prose-caveat mismatch is real. (≡ 613842 F1, ≡ Gemini-evening F3, ≡
  pending-2026-04-23 F27 visibility-only — a 4-way cross-audit convergence.)
- **Valid as of today? PARTIALLY — substantially mitigated by strengthening;
  narrow residue remains.** First-hand `def-adaptive-tempo.md`:
  - Frontmatter line 4 **still `status: exact`**; the additive scalar
    `T = Σ_k ν^(k)η^(k)*` is still the primary Formal Expression. The
    specific mismatch the auditors named *persists at the frontmatter/formal
    layer*.
  - **But:** the segment is now substantially strengthened *around* it —
    line 44 "Scope of scalar vs. tensor forms" (scalar exact only in
    isotropic / shared-eigenbasis / nonredundant-channel case); the
    **tensor / matrix-Loewner form is now derived as the canonical sharper
    object** (`#deriv-matrix-persistence-condition`, with the scalar as its
    "diagonal-axis-aligned special case" and an explicit "where
    per-coordinate is unsafe" clause); line 58 redundancy-penalty with the
    `I(e^{(1)};e^{(2)}|M)` form; line 64 per-dimension with the empirical
    72%-overestimate confirmation.
  - **Backlinked, routed:** TODO:395 "AAT-1 tensor adaptive tempo downstream
    promotion" (open, names the exact remaining promotion set) and TODO:126
    (tensor tempo for the LMI). Line 44 explicitly says "follow-on cycle item
    flagged in TODO.md."
- **What it really is:** the *substance* was discharged by strengthening (the
  general object is now the matrix-Loewner form, the scalar is explicitly its
  special case); the *residue* is a narrow status-tag honesty item — either
  `status: exact` is defensible *as the scoped special case* and a one-line
  Epistemic-Status sentence makes that explicit, or the `T_add`/`T_nominal`
  rename the ledgers proposed. This is **not** a strengthen-vs-soften case
  any more (the strengthening happened); it is residual frontmatter hygiene
  on a segment whose body is now correct and whose downstream promotion is
  tracked.
- **Route:** `actionable-open (narrow, routed)` — the substantive part is
  `resolved-by-strengthening`; the frontmatter/formal-layer residue is
  already carried at **TODO:395 / TODO:126** (live backlinks). MANIFEST note:
  "substance resolved via matrix-Loewner canonicalization; residual status-tag
  item tracked at TODO:395/126 — not a graduation blocker." Co-owner *could*
  apply the one-line Epistemic-Status scoping sentence as a high-confidence
  direct-fix (parent's call), but it is not required for file graduation.

#### F5 — `a_t = π(M_t)` exact only for narrower state convention (`der-action-selection`)
- **Valid in the first place?** Yes (medium-high). SUPPLEMENT: "known
  supersession, integration debt."
- **Valid as of today? NO — RESOLVED *by strengthening (unification)*.**
  `der-action-selection.md:19-33`: exact statement now framed as "Action is a
  function of the agent's complete internal state," with `a_t = π(M_t)` the
  explicit "Section I instantiation `G_t = ∅`" and the Section II lift to
  `π(M_t, G_t)` "exact within Section II scope **by the same completeness
  argument** applied to the lifted state `X_t`." The SUPPLEMENT's recommended
  repair was a *downgrade/conditionalize*; the project instead **unified both
  scopes under one completeness argument** — the stronger discharge (one
  argument, two instantiations) rather than two scoped claims.
- **Route:** `resolved` (by strengthening) — MANIFEST note.

#### F6 — Early Section-I order is not a clean dependency linearization (multiple sub-items incl. `scope-agency` Pearl-`do` before declaration; wrong `discrete-sector-condition.md` links)
- **Valid in the first place?** Yes (high) — mix of body-level hidden deps,
  wrong slug links, downstream-machinery-in-Formal-Expression. SUPPLEMENT:
  "mixed: tooling gap + prior-noted fragments."
- **Valid as of today? Largely RESOLVED; one general-policy residue +
  cross-file duplicate.** `bin/lint-outline` is **clean** (0 violations, 0
  missing deps, 27 intentional backmatter refs) — the frontmatter-graph
  sub-items are closed. The `scope-agency.md:19` Pearl-`do`-before-
  `def-pearl-causal-hierarchy` sub-item is the **exact same finding as
  471203 §B F6**, which the pilot already routed: it is `≡
  audit-742613-FINAL:254` and was recorded under **FORMAT-TODO C12** (the
  standard-notation-exemption / depends-policy question's existing home) on
  2026-05-15. The wrong-link sub-items (`discrete-sector-condition.md` vs
  `deriv-discrete-sector-condition.md`) — `grep` shows the live segments now
  use the correct slugs; lint-clean corroborates.
- **What it really is:** mostly `resolved` (lint-clean); the residual
  *FORMAT standard-notation-exemption policy* question is **already homed at
  FORMAT-TODO C12** (per pilot 583046's routing of the identical 471203 F6 /
  742613:254). This is the item the pilot flagged in its §3.4 as "no tracked
  home" — it *now has one* (C12); confirm C12 still carries it.
- **Route:** `resolved` for the mechanical sub-items; the policy residue is
  `duplicate` of 471203 F6 / 742613:254 → defer to its FORMAT-TODO C12 home,
  do not double-track. MANIFEST note.

#### F7 — Adaptive-system primitives action-coupled while adaptive scope includes passive observers (`def-agent-environment` vs `scope-adaptive-system`)
- **Valid in the first place?** Yes (medium-high) — terminology/primitive
  tension. SUPPLEMENT: "known conceptual tension, integration debt"; also
  seen in `AUDIT-WORKING-584721/01-section-i-leaves.md:19`.
- **Valid as of today? Conceptually addressed in-prose; primitive-naming
  residue is scope-honest, not a defect.** `scope-adaptive-system` Discussion
  + `post-causal-structure:36-38` + `def-agent-spectrum:44` explicitly admit
  passive observers / zero-coupling systems into Section I scope and *name
  the tension*. The primitive `def-agent-environment` still uses
  action-affecting "agent" language — but this is now a *named, scoped*
  modeling choice (action channel optional/degenerate, stated in the
  downstream segments), not a hidden contradiction. This is the project's
  scope-honesty discipline working, not an open bug.
- **What it really is:** `correctly-rejected / scope-honest` for the
  defect framing; the "introduce a neutral primitive" suggestion is a
  **soft-polish / research-seed** (a real concision/clarity nudge, not a
  correctness gap).
- **Route:** the defect reading is closed (scope-honest, in-prose); the
  primitive-rename idea → polish-and-sentiment ledger (`considered` —
  *terminology-cleanup nudge, declined-as-defect, retained as concision
  seed*). MANIFEST note.

#### F8 — Model-sufficiency undefined when denominator (total predictive info) is zero (`def-model-sufficiency`)
- **Valid in the first place?** Yes (medium). SUPPLEMENT: "likely new local
  well-definedness gap."
- **Valid as of today? NO — RESOLVED.** `def-model-sufficiency.md:26` now
  carries an explicit **"Well-definedness."** clause: `S(M_t)` defined when
  `I(C_t; o_{t+1:∞} | a_{t:∞}) > 0`; the "undefined in predictively-vacuous
  regimes" convention chosen (the SUPPLEMENT's cleaner of two options), with
  downstream inheritance (`def-model-class-fitness`,
  `result-structural-adaptation-necessity`) explicitly noted, and the
  rationale in Epistemic Status (line 35). Exactly the SUPPLEMENT §8 repair,
  with downstream propagation added.
- **Route:** `resolved` — MANIFEST note.

#### 742613 process-feedback (§"Process Feedback on the Instructions", §"Phase 2 Process Feedback", §"Recommended Next Work")
Partial-pass protocol; appendix-exception tightening (proof- vs meta-pattern-
vs downstream-non-appendix); explicit CLAUDE.md-TODO-conflict override; machine-
check helper; "consider writing" too soft. The Phase-2 triage vocabulary
(new / known-unintegrated / known-resolved / tooling-gap / scope-status-
mismatch) is a *durable methodological contribution* — it is in fact the
ancestor of the current spine's disposition enum.
- **Route:** `process/instruction-feedback` → polish-and-sentiment ledger,
  themed *audit-process / instruction improvements*, attributed 742613. The
  triage-vocabulary item specifically should be noted as **already absorbed**
  into `msc/audit-backlog-triage-2026-05-15.md`'s enum (mark `superseded-by`
  the spine enum, not open).

**742613 graduation readiness:** F1/F3/F5/F8 resolved (F3/F5 by
strengthening); F4 substance resolved + residue routed (TODO:395/126); F6
mechanical-resolved + policy-residue homed at FORMAT-TODO C12 (≡471203 F6);
F7 scope-honest-closed + seed→ledger. **F2 is the one finding carried open
as a strengthening item** (correct discharge = maximal-inequality spike, NOT
the SUPPLEMENT's recorded soften). The FINAL+SUPPLEMENT are themselves the
durable ledger and stay as the audit-trail record; the *file* can graduate
with F2 recorded in MANIFEST as `actionable-open → strengthening spike
(maximal-inequality route; SUPPLEMENT's soften recommendation explicitly
NOT ratified)`. Recommend parent treats F2 as the priority strengthening
item out of this whole slice.

---

### 3. `audit-613842-FINAL-2026-04-25.md`

Codex partial de-novo (Section I persistence + II lift + III composition +
logogenic). 3 findings (F1–F3). **Substantial overlap with 742613 — F1≡742613
F4, F2≡742613 F2.** Disposition follows the 742613 adjudications (don't
double-track) except where 613842 adds independent signal.

#### F1 — `def-adaptive-tempo` unrestricted additive scalar later demoted to upper bound
- **Duplicate of 742613 F4** (near-verbatim; same segment, same passage, same
  diagnosis "integration debt / definition-scope mismatch"). 613842 adds the
  cross-ref `pending-findings-2026-04-23.md:164` historical-tracking pointer.
- **Route:** `duplicate` → defer to 742613 F4 disposition (substance
  resolved-by-strengthening via matrix-Loewner; residue at TODO:395/126).
  MANIFEST note "613842 F1 ≡ 742613 F4."

#### F2 — Model-S persistence summary-layer over-compresses Prop A.1S region-awareness
- **Same underlying segment-state as 742613 F2** but **613842 frames it
  *weaker*** — as "summary-layer over-compression / scope-honesty drift … not
  a flaw in Prop A.1S itself … repair stops one layer too early." **This
  under-characterizes the defect.** First-hand, the false object
  `P(τ_R < ∞) ≤ nσ²/(2αR²)` is *in Prop A.1S (iii) itself* (line 194) and its
  proof (line 242), not merely in downstream summaries — 742613 F2's sharper
  reading (it is a genuine ever-exit/fixed-time conflation, not just
  compression) is the correct one.
- **What it really is:** `duplicate-of-742613-F2` *with a softer (and less
  accurate) characterization*. Per strengthen-before-soften, when two audits
  characterize the same issue at different strengths, the **stronger/more
  precise reading governs the disposition** (the weaker framing is exactly
  the "summary compression, not a flaw" softening the methodology warns
  against). Defer to 742613 F2's `actionable-open → strengthening spike`.
- **Route:** `duplicate` → 742613 F2 disposition (the *stronger*
  characterization). MANIFEST note: "613842 F2 ≡ 742613 F2; 742613's
  precise reading (ever-exit conflation in Prop A.1S itself, not summary
  compression) governs — 613842's 'summary-layer compression' framing
  under-characterizes and is itself a soften the methodology flags."

#### F3 — C-iv strategic-composite route only partially integrated; closure-defect bridge open (hybrid: integration-debt + theory-open)
- **Valid in the first place?** Yes (high) — the auditor's "most interesting
  finding," correctly diagnosed as hybrid (integration-debt + a genuine
  theory-open component: the closure-defect ontology doesn't fit
  equilibrium-statistic composites). Echoed at 613842's own bigger-picture
  §F3 and `pending-findings-2026-04-25.md:109` (SP-21).
- **Valid as of today? NO — RESOLVED, and the theory-open component closed
  by *new theory* (third-completion-state strengthening).** First-hand:
  - `deriv-strategic-composition.md` is now a full segment that **reframes
    the question** (line 20: "the correct primitive is fixed-point existence
    and stability, *not* Lyapunov contraction on a shared state … Contraction
    to shared truth is a `U_O=1` special case; strategic composition is the
    `U_O<1` companion regime"), **derives the α′-transfer** of the
    sector-persistence template to the equilibrium layer under potential
    (Monderer-Shapley) / monotone (Rosen) games via the (SC-1)/(SC-2)/(SC-3)
    decomposition, with **honest β′ scope exit** (VI existence-only / CCE
    set-convergence) for non-potential non-monotone games.
  - `scope-composite-agent.md` now carries (C-iv) as a first-class fourth
    route (lines 46–69) with its own operationalization; the
    three-route/disjunction language is consistent across
    `def-unity-dimensions` (the older "three-route" framing the audit flagged
    at `:19,:40` is superseded).
  - The "still open closure-defect bridge" the audit found at
    `deriv-strategic-composition.md:119,135,175` is resolved by the
    recognition that it was **the wrong bridge to seek** — strategic
    composites get equilibrium-convergence machinery, not closure-defect
    contraction. This is precisely `strengthen-before-soften.md`'s
    third-completion-state: the obstruction *was* the discovery, and it
    produced a different provable claim (the α′ equilibrium-layer transfer)
    from the boundary.
- **What it really is:** the integration-debt half `resolved`; the
  theory-open half closed by **new theory** (the strengthen-discharge in its
  deepest form — a no-such-bridge boundary result that yielded a different,
  cleaner theorem family). SP-21 (the architectural restructure the audit
  pointed at) is *subsumed* by the landed `deriv-strategic-composition` /
  (C-iv) work — parent should verify SP-21's PROPOSALS status reflects this
  (likely `→ landed` / closeable).
- **Route:** `resolved (by strengthening — third-completion-state)`;
  cross-ref: confirm **SP-21** in PROPOSALS is marked subsumed/landed by the
  C-iv + `deriv-strategic-composition` cycle (parent action — surfacing, not
  a graduation blocker for 613842 itself).

#### 613842 bigger-picture (§"Bigger-picture assessment", §"Non-findings worth saying explicitly") + §"Process feedback"
- "Non-findings worth saying explicitly" (old TST↔logogenic concern doesn't
  survive; strategic-composition sign error repaired; discrete-time
  variance-gap repaired) → **sentiment / calibration** (ledger; valuable
  *don't-re-import-from-historical-msc* signal — exactly the
  considered-and-verified-clear register).
- Bigger-picture ("framework cleaner if it stops making every composite route
  share one macro-object/theorem-family") → **research-seed**, but **note it
  is now substantially actioned** by the (C-iv) split — mark `superseded-by`
  the landed strategic-composition work, not open.
- Process feedback (SCC/cycle-handling clause; CLAUDE.md-bleed; appendix
  example-findings-as-historical-calibration; component-local-lint caveat) →
  `process/instruction-feedback` (ledger; SCC-handling clause is a concrete
  durable instruction improvement).

**613842 graduation readiness:** F1/F2 are duplicates deferring to 742613's
dispositions (F2 → the open strengthening item; tracked there, not here).
F3 resolved-by-strengthening. Bigger-picture/process → ledger.
**Ready to graduate** with F1/F2 recorded as `duplicate → 742613` and F3
`resolved`; the only carried-open math item (Model-S) lives under 742613 F2,
not double-tracked here.

---

### 4. `opus-audit-2026-04-21.md`

Opus de-novo of `01-aat-core/`. 4 findings + "Candidates that dissolved" +
"Cross-cutting pattern" + "Bigger-picture synthesis". This is the **purest
strengthen-before-soften exhibit in the slice** — its own §"Cross-cutting
pattern" *names the exact methodology principle*: "the spikes consistently
make stronger, sharper claims than the segments they promoted to" (= the
canonical `strengthen-before-soften.md` shape). Every one of its 4 findings
was discharged by *restoring/strengthening to the spike-strength claim*.

Ledger evidence: `pending-findings-2026-04-21.md:98` records "opus-audit-
2026-04-21.md is the master audit that drove the 2026-04-21 work. Its
findings §1–4 … are all addressed in the segments. §6 is embodied in
`#result-sector-persistence-template`. §7 (G_t single object) and §8
(continuous convention hierarchy) are deferred as foundational moves."

#### Finding 1 — Orient cascade "default operational signal" (δ_s/L0) biased by construction; no causal-sufficiency gate
- **Valid in the first place?** Yes (high). Ledger: addressed.
- **Valid as of today? NO — RESOLVED *by strengthening, over-delivered*.**
  `der-orient-cascade.md` now has a full **step 4c "Causal-sufficiency check
  (L0→L1 escalation)"** (line 48) — the exact gate the audit asked to thread
  in — *plus* a dedicated **"Practical sensitivity"** paragraph (line 50)
  that also folds in the *later* compound concerns (F11 on-policy / F31
  non-stationary signal-to-noise), step 4a now explicitly states the L0/Φ
  bias, and Epistemic Status (line 87) tier-stratifies every step. The audit
  asked for a gate; the project delivered the gate + the no-go-uniqueness
  framing + the non-stationary caveat + full tier-stratification.
- **Route:** `resolved` (by strengthening) — MANIFEST note.

#### Finding 2 — Strategic persistence schema parallels epistemic only under experience-discounting, not stated as prerequisite (`schema-strategy-persistence`)
- **Valid in the first place?** Yes — **"Very high" confidence**; the audit's
  sharpest line: "the spike's strongest and cleanest constraint was *weakened
  during promotion*" (the literal `strengthen-before-soften.md` failure mode).
- **Valid as of today? NO — RESOLVED *by strengthening (restoration past the
  ask)*.** `schema-strategy-persistence.md` now has a dedicated
  **"### Forgetting as Prerequisite"** section (line 34) `*[Formulation
  (forgetting-prerequisite)]*` with the exact steady-state
  `α_Σ^ss = (1−λ)/(2−λ)`, the leading-order `≈ 1−λ` *with quantified
  approximation error at λ=0.5/0.9*, and the full prerequisite
  `λ < (R_Σ − 2ρ_Σ)/(R_Σ − ρ_Σ)` (line 56) — promoted into the segment's own
  Formal Expression and foregrounded in the opening (line 15). The spike's
  weakened constraint was *restored and derived further*. This is the
  canonical strengthen-discharge.
- **Route:** `resolved` (by strengthening) — MANIFEST note. (Cross-ref: the
  `ρ_Σ`-unmeasurability *deeper* question is `pending-2026-04-23 F28`, a
  *different* finding, correctly outside this slice's ledger and tracked
  there — not reopened here.)

#### Finding 3 — Composition scope presents undefined scalar threshold `U_O`/`ε_comp`; unified framing weaker than the three-route disjunction the spike defended
- **Valid in the first place?** Yes (medium-high). Ledger: addressed.
- **Valid as of today? NO — RESOLVED *by strengthening + supersession*.**
  `scope-composite-agent.md` removed the unified-scalar overclaim (line 58:
  "routes are *not* shown to reduce to a common scalar threshold … Each route
  carries its own operationalization"; line 75 states the reduction is open
  and the disjunctive form is chosen *because no reduction is demonstrated*),
  the `U_O` dual-role honesty is explicit (lines 83, 65), **and** the
  territory was *expanded* with the new (C-iv) equilibrium route. The audit
  asked to "walk back to the three-route disjunction"; the project walked it
  back *and* added a fourth derived route + machinery.
- **Route:** `resolved` (by strengthening — soften-candidate discharged via
  strengthen + new theory) — MANIFEST note.

#### Finding 4 — `ι_ij` defined as first-class edge property but operational machinery ignores it
- **Valid in the first place?** Yes (high). Ledger: addressed.
- **Valid as of today? NO — RESOLVED *by strengthening*.**
  `def-strategic-tempo.md:22` now defines `T_Σ = Σ ν_ij·η_edge,ij·ι_ij` as
  the **primary** definition (the spike-strength `T_Σ^eff` form the audit said
  hadn't propagated), with the Regime A/B/C contribution table (line 32), the
  operational statement "An agent cannot improve the parts of its strategy it
  cannot test interventionally" (line 38), and the per-edge persistence
  condition carrying ι (line 84). Exactly the audit's three-step repair, at
  spike strength.
- **Route:** `resolved` (by strengthening) — MANIFEST note.

#### "Candidates that dissolved" (7) + "Cross-cutting pattern" + "Bigger-picture synthesis" (7 moves)
- Dissolved-candidates: auditor self-rescinded under burden-of-proof — **no
  routing needed**; record in MANIFEST that the auditor self-disposed (Class-2
  scope restriction, bridge-lemma-beyond-A4, adversarial coupling model,
  additive scalar tempo, unity-dimension independence, CMC/P3, composite
  tempo dual-definition).
- "Cross-cutting pattern" (spike-stronger-than-segment, post-promotion-pass
  recommendation) → **process/methodology seed → ledger**, *and* note it is
  the empirical ancestor of the project's now-codified
  `strengthen-before-soften` discipline (mark as a *validated-and-absorbed*
  observation, not open). High-value calibration signal: this is a
  contemporaneous independent rediscovery of the project's core methodology.
- Bigger-picture synthesis (sector-template factoring; IB-unification;
  causal-sufficiency-to-cascade; Cox-parallel for graph-uniqueness;
  persistence/destabilization single statement; G_t single-object;
  continuous convention hierarchy) → several are **landed** (sector-template
  = `#result-sector-persistence-template` per ledger §6; causal-sufficiency
  = Finding 1 resolved; IB-unification = `#disc-compression-operations`).
  The §7 (G_t single object) and §8 (continuous convention hierarchy) are
  **explicitly ledger-deferred as foundational moves** — these are
  `architectural / research-seed`, and the ledger already records the
  deferral. Route the still-live ones (Cox-parallel necessity direction;
  persistence/destabilization single-statement) → polish-and-sentiment
  ledger *research-seeds*; mark the landed ones `superseded-by` their landing
  segments; note §7/§8 are *ledger-tracked deferrals* (not homeless).
- **Route (synthesis):** ledger *research-seeds* for the unlanded;
  MANIFEST notes the landed ones with their landing segments; §7/§8 →
  point at `pending-findings-2026-04-21.md:98` as their existing
  deferral-record (don't re-file).

**opus-2026-04-21 graduation readiness:** all 4 findings
**resolved-by-strengthening** (this file is the slice's cleanest
strengthen-first exhibit and the ledger corroborates §1–4 + §6 addressed,
§7–8 deferred-with-record). Dissolved-candidates self-disposed. Synthesis →
ledger / superseded-by-landings. **Ready to graduate.**

---

### 5. `audits-2026-04-22-evening.md`

Three post-strengthening-cycle de-novo audits (Codex / Gemini / Opus),
verbatim transcripts. This file's *own* purpose-statement says it feeds
`pending-findings-2026-04-22.md` "Post-strengthening evening batch"
(Findings 16–21), `architectural-proposals-2026-04-22.md` (O-BP8–O-BP16),
TODO, and CLAUDE.md §7. **It is therefore already-routed-by-construction**
into the 2026-04-22 ledger (F16–F21) — that ledger (read as evidence) records
their resolution status. My job is verify-the-ledger-disposition-is-closure-
direction-correct against current `src/`, not re-generate.

Verification against `pending-findings-2026-04-22.md` "Post-strengthening
evening batch" + current `src/`:

#### Codex (4 findings) — F22-precursors / scope-lattice / C-iii / coupled-diagnostic
- Codex-1 (Section II headline scope broader than theorem scope) ≡ ledger
  trajectory toward **F22/F30** (2026-04-23) and **F-V** family — *known
  scope-visibility finding*, the canonical recurring one. Current `src/`:
  `scope-composite-agent` / `der-causal-hierarchy-requirement` /
  `der-directed-separation` carry the stacked narrowings explicitly; the
  *repo-entry* (README/OUTLINE) framing is the residual, tracked through the
  scope-lattice line (O-BP8 / pending-2026-04-23 F22/F30). **subsumed** by
  the later-tracked scope-lattice work — defer to F22/F30 disposition (later
  ledgered cycle, Cluster C's 2026-04-25 territory). Not this file's to
  carry.
- Codex-2 (timescale heuristic vs proof) ≡ **pending-2026-04-22 Finding 6**
  ("Composition timescale heuristic outruns bridge conditions") and
  TODO:466 — *already ledgered, routed*. subsumed.
- Codex-3 ((C-iii) doesn't supply composite `O_c`) ≡ **pending-2026-04-22
  Finding 8** + resolved by the **(C-iv) / `deriv-strategic-composition`**
  landing (which restructured the route system — the audit's "(C-iii) under-
  specification" is addressed by the route-system rework). subsumed by the
  613842-F3 strengthening (same cycle).
- Codex-4 (coupled-diagnostic operational-computability overclaim) ≡
  **pending-2026-04-22 Finding 17** + **pending-2026-04-23 F25** — *already
  ledgered*; subsumed by the C-BP1 three-layer-separation track. subsumed.

#### Gemini (5 findings + 3 integration + big-picture)
- Gemini-1 (L1 repair lacks formal persistence guarantees) ≡
  **pending-2026-04-22 Finding 18** + Gemini-evening F1. **RESOLVED by
  strengthening** — verified first-hand: `example-L1.md:134` now derives
  L1' sector-condition as **Prop B.7** (five-way gating `α_{L1'}`, strict-
  prerequisite reduction to B.6) *and* the Cramér-Rao **no-go** under
  unobservable C with 3 named repair routes. Soften-candidate → proposition
  + boundary no-go. resolved (by strengthening).
- Gemini-2 (additive communication gain naive to adversarial game theory) ≡
  Gemini-evening F2. **RESOLVED as scope-honest / correctly-bounded.**
  First-hand `hyp-communication-gain.md`: now `*Hypothesis.*`-tiered; line 33
  states the auditor's exact concern in-segment ("does not model the
  *attacker's* optimization over the defender's trust dynamics"); line 55
  names where game theory enters; line 57 a considered future split. The
  boundary is named in-segment at hypothesis tier — the project's signature
  scope-honesty move, *and* it interlocks with the now-landed (C-iv) /
  `deriv-strategic-composition` equilibrium machinery. `correctly-rejected`
  as a defect (it is a scope-honest hypothesis-tier limitation, not an open
  bug); the future-split idea → ledger research-seed.
- Gemini-3 (logogenic bias bound unproven) ≡ **pending-2026-04-22 Finding
  19** + 2026-04-21 Finding B resolution + Gemini-evening F3. **RESOLVED by
  strengthening** — first-hand `result-section-ii-survival.md:118`: tighter
  MI form `≤ C·κ·I(G;Ω|e,M)` now primary; constant `C` *derived 2026-04-24*
  under two named sub-scope tracks (transport-inequality / Fisher-Rao);
  "order-of-magnitude guidance" upgraded to "conditional theorem." Past the
  ask. resolved (by strengthening).
- Gemini-4 (causal sufficiency necessity unproven) — auditor itself marked
  **"Already Caveated"** (text lowers claim to sufficiency). `correctly-
  rejected` (auditor self-disposed) — ≡ pending-2026-04-23 rejection-set
  ("Pinsker / causal-sufficiency / etc. — already adequately caveated").
- Gemini-5 (composition-closure contraction assumption) — auditor marked
  **"Already Caveated/Resolved"** (Tier 1/2/3 classification). `correctly-
  rejected` (auditor self-disposed).
- Gemini integration items + big-picture (continuous-parameterization;
  M_t/Σ_t-as-projections; population-Lyapunov; natural-parameters) →
  research-seeds → ledger; *several landed* (natural-parameter /
  log-odds work is in the BH-identity + `deriv-edge-update-natural-parameter`
  territory) — mark landed ones `superseded-by`; the population-Lyapunov
  and continuous-parameterization ones are the live research-seeds
  (continuous-parameterization ≡ opus-2026-04-21 §8 = ledger-deferred
  foundational move — point at that record).

#### Opus (3 findings + dissolved + big-picture + closing observation)
- Opus-F1 (KL-form "non-degeneracy" misleading — forward-KL infinite under
  deterministic π\*) ≡ **pending-2026-04-22 Finding 20** (severity-high,
  "introduced by the V-medium move"). **RESOLVED by strengthening — the
  slice's second-strongest strengthen-first exhibit.** First-hand
  `form-strategy-complexity-cost.md:137`: the forward-KL degeneracy was not
  merely reversed — the π\*-first reverse-KL is now **derived** as forced by
  a regret-bound argument *plus a uniqueness theorem* (chain-rule additivity
  axiom uniquely selects reverse-KL among f-divergences; Hobson 1969 /
  Csiszár 1991 / Aczél-Daróczy 1975), with secondary characterizations
  marked convergent-not-independent. A soften-candidate ("acknowledge the
  deterministic case needs smoothing") became a *uniqueness result*. This is
  the textbook strengthen-discharge. resolved (by strengthening).
- Opus-F2 (`scope-developer-agent` `status: exact` vs internal labels) ≡
  **pending-2026-04-22 Finding 14** — *already ledgered* (TODO Finding 14).
  Cross-component (`02-tst-core/`) — outside this slice's `01-aat-core`
  first-hand remit, but the finding is durably tracked. subsumed by
  pending-2026-04-22 Finding 14 / its TODO home; defer (TST-cluster /
  Cluster-C-or-D territory). Not this file's to carry.
- Opus-F3 (`#disc-identifiability-floor` frontmatter vs internal text
  three-way status label) ≡ **pending-2026-04-22 Finding 21** (severity-low,
  drafting artifact, "introduced by commit b91493c"). *Already ledgered.*
  subsumed — defer to pending-2026-04-22 F21 disposition. (Spot-note: this
  is a 10-min frontmatter cleanup; if F21 is still open in TODO it is a
  clean co-owner direct-fix candidate — surface to parent, don't re-file.)
- Opus dissolved-candidates (7) — auditor self-disposed; MANIFEST note only.
- Opus big-picture A–G + "closing observation" (honesty is load-bearing) →
  the **"closing observation"** is high-value **sentiment/calibration**
  (independent Opus arrival at "the framework's conservatism is its
  architectural principle" = the project's core thesis, surfaced by a
  fresh reader — exactly the first-class sentiment the spine protects).
  A–G synthesis: sector-template-as-center / four-ladders-as-one /
  observability-as-master-variable / resource-budget-variable /
  Cox-parallel / Section-III-pull-up / per-segment-derived-vs-chosen-table
  → research-seeds → ledger; several converge with 584721 §D and
  opus-2026-04-21 synthesis (dedupe in the ledger — *the
  observability-as-master-variable and four-ladders-as-one seeds recur
  across 3 of this slice's files*; one consolidated attributed row each,
  not 3).
- **Route (whole file):** **self-routing-by-construction into the
  2026-04-22 ledger** (F16–F21) — this is a `verify-and-mirror` file, not a
  generate file. Dispositions verified closure-direction-correct against
  current `src/`: the strengthen-first ones (Gemini-1, Gemini-3, Opus-F1)
  **landed by strengthening**; the scope ones subsumed/ledgered; the
  rejections auditor-self-disposed; big-picture/sentiment → ledger. **Ready
  to graduate** as a verified-and-mirrored transcript file (its findings
  live in `pending-findings-2026-04-22.md` F16–F21, which stays as durable
  ledger).

---

### 6. `audit-738192-FINAL.md`

Gemini CLI de-novo, 2 findings + process feedback. Short, sharp, two
*specific math/epistemic* claims.

#### Finding 1 — IB `β` parameter conflated with environment volatility `ρ` (`form-information-bottleneck`)
- **Valid in the first place?** Yes — **"Firm"** (Gemini); the auditor's
  double-counting argument is mathematically correct (volatility natively
  degrades `I(C_t; o_{t+1:∞})`; the optimal `φ*` discards stale info even at
  constant β; claiming β *must* be lowered double-counts).
- **Valid as of today? NO — RESOLVED *by strengthening (correctness
  adoption)*.** First-hand `form-information-bottleneck.md:26-28`: a dedicated
  subsection **"Dependence on volatility (The β vs ρ distinction)"** now
  states it would be "a double-counting error" to claim β must be lowered
  when ρ is high, explains the joint distribution natively handles it, and
  re-scopes β to "the agent's *internal cost of memory* or *computational
  capacity*, not changes in environmental volatility." This is the auditor's
  correction adopted essentially verbatim-in-spirit — a correctness
  strengthening of the segment.
- **Route:** `resolved` (by strengthening — the segment was corrected to the
  auditor's mathematically-correct reading) — MANIFEST note.

#### Finding 2 — `git checkout` misclassified as Level-3 counterfactual (`def-pearl-causal-hierarchy`)
- **Valid in the first place?** Yes — **"Firm"** (Gemini); the critique is
  conceptually correct under Pearl's strict definitions: `git checkout`
  resets *codebase* state but not the environment / developer-mind / clock /
  external dependencies; it is a *highly reproducible Level-2 intervention*,
  approaching Level-3 only in a deterministic-stateless test environment.
- **Valid as of today? NO — RESOLVED *by strengthening (canonical segment),
  with a borderline-polish recap residue*.** First-hand, the **canonical
  home** `02-tst-core/src/obs-software-epistemic-properties.md` (P2) now
  carries *exactly the auditor's correction, made into a named scoped
  regime*:
  - line 30: "**P2. Executable counterfactuals (scoped Level 3 access).**
    … literal Pearl Level 3 … for a specific and well-defined class:
    **code-internal counterfactuals with deterministic outcomes.**"
  - line 32: "This literal Level 3 access *fails* for a complementary class:
    **counterfactuals crossing the agent-environment boundary** … For this
    second class, `git checkout` is a strong executable **proxy, not literal
    Level 3**." — the auditor's precise argument (env/developer/clock not
    reset), adopted.
  - line 119: explicit **(a)/(b)/(c) regime-boundary conditions** under which
    literal L3 holds vs. degrades to proxy. This is the strengthen-first
    discharge: the overclaim was replaced with a *named scoped regime +
    failure-class characterization*, stronger and more useful than either
    the original claim or a deletion — precisely the move the audit's "it's
    L2-not-L3" finding should produce.
  - The `def-pearl-causal-hierarchy.md:53` line the auditor anchored is now
    a **brief illustrative recap that explicitly cross-references
    `#obs-software-epistemic-properties`** (where the scoped treatment
    lives) — the short-form-deferring-to-the-canonical-scoped-segment
    pattern, not an independent overclaim. (`old-tst-via-tft-readme.md:24`
    carries the old strong phrasing but is a frozen `old-tst-*` archaeology
    file per CLAUDE.md — absorbed source material, not live theory; out of
    scope.)
- **What it really is:** `resolved` (by strengthening — the canonical
  segment now carries the auditor's correction as a scoped regime + the
  (a)/(b)/(c) conditions + the explicit failure-class). The remaining
  `def-pearl-causal-hierarchy.md:53` recap is a **borderline soft-polish**:
  it could carry the word "scoped" for full first-encounter precision (the
  scoped treatment is one cross-ref hop away, so a reader is not stranded,
  but the recap reads slightly stronger than the canonical segment on a
  scan). Not a live defect; the substance is discharged.
- **Route:** `resolved` (by strengthening) — MANIFEST note "738192 F2:
  resolved in canonical `#obs-software-epistemic-properties` P2 via scoped-
  Level-3 regime + (a/b/c) boundary; the audit's exact correction adopted
  and strengthened past it." The line-53 recap-precision nudge →
  polish-and-sentiment ledger (`soft-polish`: "add 'scoped' to the
  `def-pearl-causal-hierarchy` git-checkout recap for scan-level precision;
  canonical scoped treatment already at `#obs-software-epistemic-properties`
  P2" — optional co-owner micro-fix, parent's call). **Not a graduation
  blocker.** This corrects my initial first-hand read (the recap line alone
  looked live until the canonical TST segment was checked — the
  cross-component verification was load-bearing here).

#### 738192 process feedback
"Instructions are excellent … predictions-before-reading forced verification
mode … OUTLINE-first effective." Pure positive **sentiment / calibration**
on the de-novo instructions.
- **Route:** `sentiment` → polish-and-sentiment ledger (noted; calibration
  signal that the de-novo-audit-instruction design is landing with a
  fresh independent agent).

---

## Live items extracted from this slice (the short, decision-relevant list)

Everything in the slice is accounted for. What is *actually still open* /
*decision-relevant for the parent*:

1. **Model-S `P(τ_R < ∞)` ever-exit conflation** — `deriv-sector-condition.md`
   lines 194 / 242 / 253 / 270 / 282 (Prop A.1S (iii) + proof + summary table
   + Epistemic Status), propagated to `result-sector-persistence-template`
   / `result-persistence-condition`. **742613 F2 (precise reading) governs;
   613842 F2 is the same issue softer-and-less-accurately characterized.**
   The defect is real and live as of today; the ledger's recorded
   recommendation is a **soften** (restate as fixed-time/stationary), which
   per `strengthen-before-soften.md` is the **wrong discharge direction**.
   The strengthening route is *available and standard*: a maximal-inequality
   bound on `P(sup_{t≥0}‖δ‖ > R)` via the Itô-Lyapunov supermartingale
   already in the proof (Doob/Ville; equivalently Khasminskii 2012 ch. 5,
   *already cited in the segment*) gives the genuine infinite-horizon
   "stays in region w.h.p." statement the segment wants — *stronger* than
   the fixed-time restatement. **Recommended: route to a high-capacity
   strengthening spike (three-completion-states brief, maximal-inequality
   lead); do NOT ratify the SUPPLEMENT's soften.** This is the single most
   important surfacing in the slice — it is the one place the math-heavy
   discharge has not yet happened *and* the recorded recommendation points
   the wrong way.

2. **(Resolved — recorded for completeness, *not* an open item)**
   `git checkout`-as-Level-3 (738192 F2). The canonical
   `#obs-software-epistemic-properties` P2 carries the auditor's correction
   as a scoped regime + (a)/(b)/(c) boundary — resolved-by-strengthening.
   Only a one-word recap-precision nudge on `def-pearl-causal-hierarchy:53`
   remains (optional soft-polish → ledger). Listed here only so the
   parent does not re-derive it as live from the recap line alone — the
   cross-component (TST) check is what closes it.

3. **`def-adaptive-tempo` `status: exact` frontmatter/formal-layer residue**
   (742613 F4 / 613842 F1 / Gemini-evening F3 — 4-way convergent). Substance
   resolved-by-strengthening (matrix-Loewner canonical, scalar = explicit
   special case); narrow residue is the status tag + primary-formula layer.
   **Already routed** — live backlinks at TODO:395 ("AAT-1 tensor adaptive
   tempo downstream promotion") and TODO:126. Not a graduation blocker; a
   one-line Epistemic-Status scoping sentence is an optional co-owner
   direct-fix (parent's call). Do **not** re-file in TODO (already there).

4. **(Surfacing, not a blocker) SP-21 status** — 613842 F3's architectural
   restructure (distinct macro-objects per composite route) is **subsumed**
   by the landed (C-iv) + `deriv-strategic-composition` work. Parent should
   verify PROPOSALS SP-21 is marked subsumed/landed so it doesn't read as
   still-open.

5. **(Surfacing, not a blocker) FORMAT standard-notation-exemption policy**
   (742613 F6 residue ≡ 471203 F6 ≡ 742613:254). Pilot 583046 §3.4 flagged
   it as homeless; it was subsequently homed at **FORMAT-TODO C12**
   (2026-05-15). Confirm C12 still carries it; do not double-track from
   this slice.

Everything else: **resolved** (the large majority **by strengthening** — the
discharge this project prefers, several past the audit's ask),
**subsumed-by-later-work**, **duplicate** (cross-file, deferred to the
governing audit's disposition — note: when two audits characterize the same
issue at different strengths, the **stronger/more precise reading governs**,
per methodology), **correctly-rejected / scope-honest** (auditor self-disposed
or the limit is named in-segment at hypothesis tier), or **soft / bigger-
picture / process** → polish-and-sentiment ledger (themed, attributed,
deduped — several research-seeds and the audit-process feedback recur across
3–5 files of this slice and should land as consolidated attributed rows, not
per-file duplicates; mark landed bigger-picture moves `superseded-by` their
landing segments; mark the opus-2026-04-21 "spike-stronger-than-segment"
cross-cutting-pattern as the *validated-and-absorbed* empirical ancestor of
the project's now-codified strengthen-before-soften discipline).

---

## Graduation readiness (per file, for the parent's routing)

| File | Disposition summary | Ready to graduate? |
|---|---|---|
| `audit-584721-FINAL` | F-A resolved; F-D resolved-by-strengthening; F-B1 resolved; §A/§D → ledger | **Yes**, once §A/§D mirrored to ledger. No live blocker. |
| `audit-742613-FINAL` + `-SUPPLEMENT` | F1/F3/F5/F8 resolved (F3/F5 by strengthening); F4 substance resolved + residue at TODO:395/126; F6 mech-resolved + policy≡471203-F6@C12; F7 scope-honest-closed; **F2 carried open → strengthening spike (NOT the SUPPLEMENT's soften)** | **Yes** as a file (F2 recorded in MANIFEST as actionable-open with correct discharge direction; SUPPLEMENT is the durable ledger). F2 must travel forward as the priority strengthening item. |
| `audit-613842-FINAL` | F1≡742613-F4, F2≡742613-F2 (stronger reading governs) — duplicates; F3 resolved-by-strengthening (3rd-completion-state); big-picture/process → ledger | **Yes**; F1/F2 `duplicate→742613`, F3 `resolved`. No double-tracked open item. |
| `opus-audit-2026-04-21` | All 4 **resolved-by-strengthening** (slice's cleanest exhibit; ledger corroborates §1–4+§6 addressed, §7–8 deferred-with-record); dissolved self-disposed; synthesis → ledger | **Yes.** |
| `audits-2026-04-22-evening` | Verify-and-mirror file; routes by construction into `pending-2026-04-22` F16–F21; strengthen-first ones (Gemini-1/3, Opus-F1) **landed by strengthening**; scope ones subsumed/ledgered; rejections auditor-self-disposed | **Yes** as verified-and-mirrored transcript (findings live in the durable 2026-04-22 ledger). |
| `audit-738192-FINAL` | F1 resolved-by-strengthening; F2 **resolved-by-strengthening** in canonical `#obs-software-epistemic-properties` P2 (scoped-L3 regime + a/b/c boundary); one-word recap-precision nudge → ledger soft-polish; process feedback → ledger sentiment | **Yes.** No live blocker. |

**The four `pending-findings-2026-04-2{1,2,3}.md`** were read as evidence
only — durable ledgers/infrastructure, **not** adjudicated, **not**
graduated, **not** proposed for any move (per brief). They corroborated the
first-hand `src/` verifications throughout.

---

## Frame notes (candid — for the spine, not blocking)

**(a) The duplicate-strength rule needs to be explicit in the enum.** 613842
F2 and 742613 F2 are the same issue, but 613842 frames it as "summary-layer
over-compression, not a flaw in the proposition" — a *softer and less
accurate* characterization that is itself an instance of the
`strengthen-before-soften.md` "summary compression, not a flaw" softening.
When two audits' characterizations differ in strength, the **stronger/more
precise reading must govern the disposition** — otherwise `duplicate →
defer-to-other-audit` can silently route to the weaker reading and lose the
real defect. Recommend the spine's `duplicate` enum entry state: *defer to
the governing audit's disposition, where "governing" = the more precise
characterization, not the chronologically-first or the one that happens to
be adjudicated first.* This is a real signal-loss risk the slice surfaced.

**(b) Ledger-recorded "recommended repair" is not a disposition and can be
anti-methodology.** The 742613-SUPPLEMENT and 613842 both *recommend a
soften* for the Model-S finding. A naive verify-and-mirror of the
SUPPLEMENT's disposition would ratify the soften and close the finding in
the *wrong direction*. The evidence hierarchy puts `pending-findings-*` /
SUPPLEMENT ledgers at tier-1 — but tier-1 is authoritative for *what each
finding's status is*, **not** for *what the correct repair direction is*.
The strengthen-before-soften discipline overrides a ledger-recorded soften
recommendation. Recommend the spine note explicitly: *ledger
"recommended-repair" fields are auditor/triage suggestions, not bindings;
strengthen-before-soften governs the discharge direction regardless of what
the ledger recommended, especially in the math-heavy cycles.* (This is the
single most consequential frame observation from the slice.)

**(c) Strengthen-before-soften bite was high here and the project passed —
loudly.** The brief predicted the genuine strengthen-rejections concentrate
in this slice. They do, and the *resolved* outcomes overwhelmingly show the
project *did the strengthening* (BH-identity + lower bound; reverse-KL
uniqueness theorem; one-point-sector bidirectional-against-DA2'-inc +
counterexample; forgetting-prerequisite restored-and-derived; (C-iv) new
route; L1' Prop B.7 + Cramér-Rao no-go; bias-bound constant derived under
two tracks; completeness-argument unification). `opus-audit-2026-04-21`'s
own §"Cross-cutting pattern" *names the methodology* ("spikes consistently
make stronger claims than the segments they promoted to") — it is a
contemporaneous independent rediscovery of the project's core discipline,
which is itself strong calibration signal worth preserving as such (not
discarding as process-noise). The one exception (Model-S F2) is the
exception that proves the rule: it is the single math finding where the
strengthening was *not yet* done and the ledger pointed at a soften — i.e.
exactly the failure mode the discipline exists to catch, caught here.

**(d) `audits-2026-04-22-evening.md` is a self-routing transcript species.**
Like the pilot's "self-disposed extract" observation, this file *declares
its own routing targets* in its purpose statement (feeds pending-2026-04-22
F16–F21 + architectural-proposals + TODO + CLAUDE.md §7). It is a
verify-and-mirror, not a generate, file — and its findings are *already in
the durable 2026-04-22 ledger*. The spine's self-disposed-extract fast-path
should be widened to cover "transcript files that declare their downstream
ledger targets in a purpose header" — several `audits-*-evening`-style and
`extracted-*` files share this shape.

— Claude Opus 4.7 (1M context), Cluster B fan-out adjudicator, 2026-05-16
