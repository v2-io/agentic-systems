# SPIKE-REGRESSION-014997 — provenance recheck of the 10 `.integrated/` file-spikes

*Read-only forensics. Question is NOT "is the content present?" (the
`SPIKE-VERIFY-*` passes already established presence first-hand at named
`src/` loci). Question is the orthogonal `doc/spike-routing.md` §2a axis:
**is the in-canon content the post-correction current truth, or a
pre-correction spike form sitting on top of a fix that should have
superseded it (a regression-restoration)?** Instruments per §2a / audit-
routing §8: pickaxe `git log -S'<result-string>' -- '*/src/*'` for an
**add-then-delete-then-re-add** of the result string; `git log --follow`
on the locus against the CHANGELOG.md/LOG.md correction timeline; the
`audits/pending-findings-*` trail. No moves/edits/commits.*

---

## Headline

**All ten: CLEAN (no regression).** Every one of the ten carries its
**post-correction** truth in canon; none is a pre-correction spike form
restored over a fix. In every case where a refuted/overreaching/naive form
*could* have regressed in, the pickaxe against all `src/` is **empty** —
the wrong form **never entered canon at all**, so there is no
add-then-delete to re-invert. The corrected forms' histories are clean
strengthening progressions (landing → naming/cleanup → rename-sweep), never
a re-add after a fix.

The cycle's one genuine §4.1 canon-lie — `internal-external-decomposition`
(the multiplicative-ρ-factorization split) — was independently caught and
honesty-marked (`status: false`, KNOWN-FALSE banner) by the parent cycle.
It traces to the **`orphaned`** `spike-rho-factorization`, which is **NOT
one of these ten**. Verified separate: it is not a `depends:` of, nor a
locus of, any of the ten. No regression among the ten is entangled with it.

| # | Spike | Verdict | Decisive provenance evidence |
|---|---|---|---|
| 1 | operator-sector-unification | **CLEAN** | tentative operator-sector *primitive Definition* never entered canon (`-S'AAT/AAD operator-sector condition'` ⇒ empty; the one `9745397` hit is a 0-line rename-sweep false-positive). Corrected certificate-spine in canon (`result-certificate-existence` `status: exact`). INDEX:127 "DO NOT elevate to 4th meta-pattern" honored. |
| 2 | fenchel-bregman-reframe-additive-coordinate-forcing-2026-04-24 | **CLEAN** | naive over-unified "collapse to a single axiom" form never in canon (`-S'single unifying axiom'` / `-S'collapse.*single axiom'` ⇒ empty). The axiom-independence guard is in canon verbatim (`disc-additive-coordinate-forcing.md:50`). |
| 3 | composition-gaps | **CLEAN** | refuted "Case 3 emergent-goal-conditioning as a directed-separation case" excised as a category error and named separate (`hyp-directed-separation-under-composition.md:77`). Substantive commit `d546cf4` landed the *already-corrected* two-case form; no add-then-re-add. |
| 4 | strategy-dynamics-gaps | **CLEAN** | all 4 gap segments substantive; Gap 2 in canon is the *strengthened-past* regret-bound-derived form (`form-strategy-complexity-cost.md:38,48`); the superseded forward-KL / Shannon-MI form is named only as history in Epistemic Status (`:137`), not asserted as canon. |
| 5 | stochastic-non-exit-strengthening-2026-05-16 | **CLEAN — no-go IS current truth** | the false interpolating `P(τ_R<∞) ≤ nσ²/(2αR²)` is NOT in canon; canon holds the no-go (`deriv-sector-condition.md:198,264-268`, Cor A.1S.1 `status: exact`). `-S'Markov tail on the supermartingale'` ⇒ only the single landing commit `3d582e9` (the phrase appears once, in Working-Notes history describing the prior false claim). No commit after `3d582e9` re-adds the false bound. The no-go is not later superseded. |
| 6 | active-inference-vs-aad | **CLEAN** | refuted "EFE strictly suboptimal / dominance theorem" never in canon (`-S'strictly suboptimal'` / `-S'EFE is suboptimal'` ⇒ empty). Canon carries the strengthened-past regret-bound-derived KL direction (`form-strategy-complexity-cost.md:58`). |
| 7 | l1-evidence-axiom | **CLEAN** | corrected "generalization-in-scope, **not a new primary instance**, absorbed into Instance 2" is in canon verbatim (`deriv-edge-update-natural-parameter.md:135`). Did NOT inflate the instance count — `disc-identifiability-floor` still carries exactly **4** instances (`:138,:172`); no spurious Instance 5. |
| 8 | jacobian-b1-strengthening | **CLEAN** | honest mixed-lift in canon: only 2 statistical metric-α₂ cases AAT-internally forced; the 3 theorem-imported cases explicitly labeled "no AAT-internal axiom forces the coordinate" (`result-contraction-template.md:89-91,132`). The not-taken heredity/strong-option axiom is absent — no false upgrade regressed in. |
| 9 | fep-suboptimal-approximation | **CLEAN** | refuted "EFE strictly suboptimal / promote as dominance" never in canon (`-S'strictly suboptimal'` / `-S'dominance theorem'` against `disc-ciy-unified-objective.md` ⇒ empty). Canon carries "convergence at the shared-shape level — not unified content" + the regret-bound route (`disc-ciy-unified-objective.md:58,64,66`). Spike Assumption 2, which the spike itself said not to promote, correctly absent. |
| 10 | message-passing-credit-assignment | **CLEAN — refuted core stayed excluded** | the refuted mean-field-VMP core **never entered any canon segment**: `-S'Variational Message Passing'` and `-S'mean-field VMP'` against `*/src/*` ⇒ **empty**. `disc-credit-assignment-boundary.md` contains zero `mean-field`/`VMP` hits. Only the §6 forward-pass repair (EP / loopy-BP / max-sum / structured-variational-only-where-common-cause) is in canon (`:130`). A thing never in canon cannot have been silently restored — no add-then-delete, no regression. |

---

## 1. operator-sector-unification — CLEAN

**Regression hypothesis tested:** the spike's own §20 verdict is the
honest *2-instance-plus-1-consequence / "DO NOT elevate to a 3-instance
symmetric theorem"*; its Definition 1 operator-sector primitive is flagged
**"tentative"**. CHANGELOG:58 records that the successor
`spike-operator-family-unification/` push found the "seductive single
mechanism, which **verification broke**" and instead landed the
**certificate-spine** (completion-state B). Risk: canon regressed to the
broken tentative primitive because it "looks cleaner" than the
certificate-equivalence.

**Forensics.**
- Corrected truth IS in canon: `result-certificate-existence.md`
  (`status: exact`, L34-37 the operator-sector ⟺ exponential-stability
  equivalence, certificate as converse-Lyapunov witness);
  `disc-stability-certificate.md` (the four-facet spine).
- `git log -S'AAT operator-sector condition' -- 01-aat-core/src/*` ⇒
  **empty**; `-S'AAD operator-sector condition'` ⇒ **empty**. The spike's
  tentative *primitive Definition* never entered canon.
- The one `9745397` pickaxe hit on the bare phrase "operator-sector
  primitive" is a **rename-sweep false positive**: `git show 9745397
  --stat` shows the touched segments (`disc-stability-certificate.md`,
  `result-certificate-existence.md`, etc.) with **0 line changes** (pure
  dir/slug rename). The phrase "operator-sector primitive" in *current*
  canon (`result-sector-persistence-template.md:74`,
  `deriv-sector-condition.md:94`) appears only as a **negative scope
  statement** ("the coarse-graining projection Λ does **not** fit the
  operator-sector primitive") — the spike's honest limit, i.e. the
  corrected truth, not the broken seductive form.
- `result-certificate-existence` history is a clean spine progression
  (`98e1bb2` split anchor → `ff171f4` O-BP10 landed/archive absorbed spike
  → `06ab601` discipline cleanup → renames). No re-add of a tentative
  primitive after the certificate landing.
- INDEX:127 co-owner recommendation "land content, **DO NOT elevate to
  fourth meta-pattern**" is honored: canon carries the certificate as one
  object with four facets, not a fourth peer meta-pattern.

Completion-state (B) landed correctly; no regression.

## 2. fenchel-bregman-reframe-… — CLEAN

**Regression hypothesis:** the spike (§7.1) carries an explicit
**"do-not-over-unify" guard** — the four-layer convergence must NOT be
compressed into a single axiom. CHANGELOG:101 / LOG records the *naive
Path-7 reframe* "under-unifies by collapsing axiom independence." Risk:
the naive over-unified (single-axiom) reframe regressed into canon because
it reads cleaner than "four independent axioms converging."

**Forensics.**
- Canon carries the guard **verbatim** (`disc-additive-coordinate-forcing.md:50`):
  *"The convergence across independent axioms is itself the meta-pattern's
  substance — not a byproduct to be compressed into a single axiom."*
- `-S'single unifying axiom'` and `-S'collapse.*single axiom'` against the
  segment ⇒ **empty**. The over-unified form never entered canon; no
  add-then-delete.
- History is a clean strengthening progression (`7456ec3` SP-2 landing →
  `1f68320` Gap A/B 4th instance → `2627684`/`104b777` Findings →
  `1f70a32` SP-22 cleanup → renames). Canon at L126 even *strengthened
  past* the spike (the composition-layer honest scope-exit).

No regression.

## 3. composition-gaps — CLEAN

**Regression hypothesis:** the spike presents *Case 3 "emergent
goal-conditioning"* **in its body** as a substantive directed-separation
case with an L_{G→M} leakage term. The verify pass (SPIKE-VERIFY-504612 §2)
records canon is *sharper* — Case 3 excised as a category error caught by
external review. Risk: the spike-body Case-3-as-DS-case regressed back in.

**Forensics.**
- Canon carries the corrected truth
  (`hyp-directed-separation-under-composition.md:77`): goal-information
  leakage is *"a separate phenomenon … NOT a directed-separation issue …
  An earlier draft of this segment conflated the two; this was caught by
  external review."* Leakage tracked separately as SP-17.
- `git log -S'Case 3' --follow` on the segment shows the substantive
  landing commit `d546cf4` ("Begin to shore up directed separation
  gaps…") — the segment landed *already in the corrected two-case form*.
  All other commits touching "Case 3" are rename sweeps (`9745397`,
  `e9d1dfa` GUC, `6aae978`, `e6adf9e`, `3aa9e74`, `29ab7f8`). There is
  **no** commit that added Case-3-as-DS-case and a later one re-adding it.

The spike was integrated *as-replacement* (the sharper form), not as the
spike body. No regression.

## 4. strategy-dynamics-gaps — CLEAN

**Regression hypothesis:** the spike's Gap-2 form is hypothesis-grade
Shannon-MI; the V-medium predecessor (`a14682e`) used forward-KL, a known
degeneracy. Risk: a pre-correction (Shannon-MI or forward-KL) form
regressed over the strengthened-past regret-bound-derived form.

**Forensics.**
- All 4 gap segments exist substantive
  (`scope-edge-update-causal-validity` `conditional`,
  `form-strategy-complexity-cost`, `def-strategic-tempo` `conditional`,
  `disc-exploit-explore-deliberate`). Their `discussion-grade` statuses
  are honest, not regressions.
- Gap 2 canon is the strengthened-past form
  (`form-strategy-complexity-cost.md:38` `[Formulation (… KL-direction
  strengthened by regret bound)]`, `:48` the regret-bound derivation).
- The superseded forward-KL / Shannon-MI form is named **only as history
  in Epistemic Status** (`:137`: *"closes the direction ambiguity that the
  earlier V-medium move (commit a14682e) left open … the initial V-medium
  form used forward-KL … a structurally identical degeneracy"*). History
  in the right layer; canon asserts only the corrected form.
- Histories linear (`5c467cb`/`9aab0cc`/`dd77e06` substantive, then
  renames). No add-then-delete.

No regression.

## 5. stochastic-non-exit-strengthening-2026-05-16 — CLEAN; the no-go IS current truth

**Special-care item (parent flag):** confirm the no-go is itself the
current truth, not later superseded; confirm the false interpolating bound
did not regress back over the fix.

**Forensics (the decisive one).**
- The false claim — the prior Prop A.1S(iii) *infinite-horizon*
  `P(τ_R<∞) ≤ nσ²/(2αR²)` — is **NOT in canon**.
  `deriv-sector-condition.md:198` states explicitly: *"there is no
  P(τ_R<∞)<1 bound, and none is claimed."* Cor A.1S.1 (`:264-268`) is the
  `{0,1}` containment dichotomy, `status: exact`. The `{0,1}` dichotomy is
  load-bearing canon, the no-go appendix `#deriv-stochastic-non-exit`
  exists and is its own `exact` derivation. This matches CHANGELOG:34
  exactly.
- Pickaxe `-S'Markov tail on the supermartingale' --
  deriv-sector-condition.md` ⇒ **only `3d582e9`** ("Land Model-S non-exit
  strengthening (completion-state 3)"). The phrase appears once — at the
  landing point, **in the Working-Notes history layer** (`:354`)
  describing what the *prior false claim was*. It is not, and was never
  re-introduced as, a canonical assertion.
- `git log 3d582e9..HEAD -- deriv-sector-condition.md` = `4172866`
  (ghost-voice demote), `716ea89` (add no-go appendix), `b3d5b6b`
  (honesty-cleanup present-truth), `19ad7b6` (name Cor A.1S.1). Every
  post-landing commit moves *toward* present-truth-only; **none re-adds
  the false interpolating bound.** No add-then-delete-then-re-add.
- The no-go is not later superseded: `status: exact` on Cor A.1S.1
  currently; the Working-Notes (`:346,:354`) record the dead-end as
  do-not-re-attempt; CHANGELOG:34 confirms "Documented dead-end … do not
  re-attempt." The 628401 strengthening-will-succeed prediction is
  recorded *disconfirmed*, exactly per audit-routing §3 calibration.
- pending-findings trail: 742613-SUPPLEMENT §2 and 613842-F2 recommended
  the *soften*; strengthen-before-soften was honored (the strengthening
  was worked in full first, failed structurally → the no-go). Discharge
  direction correct.

The no-go is canon, textbook 5A, cascade-closed (verified by
SPIKE-VERIFY-504612 at `result-sector-persistence-template.md:90`). No
regression; the no-go is the current truth.

## 6. active-inference-vs-aad — CLEAN

**Regression hypothesis:** the refuted overreach is "EFE strictly
suboptimal" framed as an AAT dominance theorem. Risk: it regressed into
canon.

**Forensics.**
- `-S'strictly suboptimal'` and `-S'EFE is suboptimal'` against `*/src/*`
  ⇒ **empty**. The overreach never entered canon.
- Canon carries the corrected strengthened-past form
  (`form-strategy-complexity-cost.md:58`): the variational form is
  borrowed, KL direction *derived* from an internal regret-bound argument,
  *"without committing to AI's preferences-as-priors encoding … or to
  expected free energy as master objective."*

No regression.

## 7. l1-evidence-axiom — CLEAN

**Regression hypothesis:** the corrected truth is "generalization-in-scope,
**not** a new primary instance; absorbed into Instance 2 via dual-route
convergence." Risk: a "new primary instance" overclaim regressed in (which
would *also* corrupt the instance count that the parent's out-of-slice
`spike-rho-factorization` Instance-5 framing depends on).

**Forensics.**
- Canon carries the corrected truth verbatim
  (`deriv-edge-update-natural-parameter.md:135`): *"This is a
  **generalization-in-scope** of the theorem above, **not a new primary
  instance** … two independent analytical routes … converge on the same
  unobservable-C structural floor, strengthening Instance 2."*
- `disc-identifiability-floor.md:138` and `:172` confirm the segment
  carries **exactly four** instances; the l1-evidence dual-obstruction is
  absorbed *into* Instance 2, no Instance 5 spuriously added. The instance
  count is intact (this is the SPIKE-VERIFY-504612 §5 cross-slice
  concern — confirmed clean from the regression axis too).

Label-tracks-truth applied correctly (a generalization labeled a
generalization). No regression.

## 8. jacobian-b1-strengthening — CLEAN

**Regression hypothesis:** the spike's honest result is a *mixed lift* —
only 2 of 5 metric-α₂ cases AAT-internally forced; 3 remain
theorem-imported; the heredity/strong-option axiom (Angle 1) is **NOT
taken**. Risk: the 3 theorem-imported cases falsely upgraded to
AAT-internal, or heredity adopted as an axiom, because "all 5 forced"
reads cleaner than the honest no-lift.

**Forensics.**
- Canon carries the honest mixed-lift
  (`result-contraction-template.md:83-91,132`): only information-metric
  Kalman and Fisher exp-family "AAT-internally forced under (PI)/Čencov";
  Hessian (`:89`), Lyapunov-linear (`:90`), Lyapunov-PID (`:91`) each
  explicitly *"Theorem-imported … no AAT-internal axiom forces the …
  coordinate."* L132 restates the partition cleanly.
- No segment asserts heredity as an adopted axiom (the not-taken Angle 1).
  No false upgrade regressed in.

No regression.

## 9. fep-suboptimal-approximation — CLEAN

**Regression hypothesis:** the spike (§4/§5) flags "claiming EFE strictly
suboptimal is an overreach; do **not** promote as a dominance theorem."
Risk: the dominance/strictly-suboptimal form regressed into
`disc-ciy-unified-objective`.

**Forensics.**
- `-S'strictly suboptimal'` and `-S'dominance theorem'` against
  `disc-ciy-unified-objective.md` ⇒ **empty**. The overreach never
  entered canon.
- Canon carries the corrected truth (`disc-ciy-unified-objective.md:58`:
  *"convergence is at the shared-shape level … not unified content"*;
  `:66`: *"via decision-theoretic regret bound on Q_O rather than via
  free-energy-gradient flow … does not depend on the priors-as-preferences
  encoding"*). Dark-room bypass via Survival Imperative (`:58`).
- History a clean strengthening progression (`e39c17b` Causal-IB drive →
  `1bffa60` Bretagnolle-Huber propagation → renames). Spike Assumption 2,
  which the spike *itself* recommended against promoting, correctly
  absent.

No regression.

## 10. message-passing-credit-assignment — CLEAN; refuted core stayed excluded

**Special-care item (parent flag):** the spike's §3-5 mean-field-VMP core
is *refuted by the spike's own §6*; it was meant to be **excluded
as-replacement**, with only the §6 forward-pass repair (EP / loopy-BP /
max-sum, AND/OR preserved as exact potentials) in canon. Confirm it didn't
regress back in.

**Forensics (the decisive one).**
- `git log -S'Variational Message Passing' -- '*/src/*'` ⇒ **empty**.
  `git log -S'mean-field VMP' -- '*/src/*'` ⇒ **empty**. The refuted
  mean-field-VMP core **never entered any canon segment**. A form that was
  never in canon cannot have been silently restored — there is no
  add-then-delete and no regression-restoration possible.
- `disc-credit-assignment-boundary.md` contains **zero** `mean-field` /
  `VMP` / `Variational Message Passing` hits. Line 130 carries exactly the
  §6 corrected form: *"exact Belief Propagation (BP) on tree or polytree
  cases, loopy BP or max-sum for MAP-style diagnosis, Expectation
  Propagation (EP) for approximate marginals, and structured variational
  methods only where common-cause structure is explicitly modeled."* The
  trailing clause is precisely the spike's L1-correlation floor.
- The corrected line's pickaxe lands on `9745397` (AAD→AAT rename sweep —
  recency-poisoned, as `doc/spike-routing.md` §7 warns). The decisive test
  here is content-presence-first-hand (met) plus the *exclusion* pickaxe
  (met: the wrong form is verifiably absent across all 4 `src/` trees).
  The segment history shows no commit that removed an EP/loopy-BP form and
  substituted a mean-field one.
- pending-findings-2026-04-22 Finding 2 (unbounded-gradient in
  credit-assignment, related lineage) — not the same defect; the
  mean-field-VMP exclusion is independent and clean.

Integrated as-replacement exactly per integration-is-replacement. No
regression.

---

## Cross-cutting confirmations

1. **The cycle's one real §4.1 canon-lie is NOT among the ten.**
   `internal-external-decomposition` (the refuted multiplicative-ρ split,
   `status: false` + KNOWN-FALSE banner) was independently caught and
   honesty-marked by the parent this cycle. It traces to the **`orphaned`**
   `spike-rho-factorization` and the `orphaned`
   `spike-rho-additive-variance-strengthening-2026-04-24` (the (AV)
   successor) — **none of these is one of my ten**. Verified: the
   §4.1-marked segment is not a `depends:` of, nor a locus of, any of the
   ten. No regression among the ten is entangled with the ρ cluster.

2. **The recency-poisoning pattern held exactly as the SOP predicts.**
   Where pickaxe landed on `9745397`/`08b6f40` (AAD→AAT) or `e6adf9e`
   (role-prefix) or `e9d1dfa` (GUC) the recency is sweep-poisoned and was
   discounted; the decisive instrument was first-hand content-presence
   plus the **exclusion pickaxe** (proving the wrong form is *absent* from
   all `src/`), which is sweep-immune (a string that is nowhere now and
   has no add-commit was never there). Un-poisoned cycle-commits
   (`3d582e9`, `d546cf4`, `b76ee67`) corroborated where they survived.

3. **The integration-is-replacement discipline was applied correctly
   across all ten.** In every flagged case the refuted/naive/overreach
   form was *deleted-or-never-admitted*, not kept-softened-with-a-pointer;
   the project-history ("previously asserted X", "the audit recommended a
   soften", "V-medium left the direction open") lives **only** in the
   history layers (Working Notes / Epistemic Status / CHANGELOG), never in
   the canonical claim. Four of the ten landed *stronger* than the spike
   and are labeled by current truth-status, not down-tiered for being new.

---

## Frame note (offered, not a refute)

The frame is right and the instruments are the sharp ones. One observation
worth surfacing: for the *regression axis specifically*, the **exclusion
pickaxe** (`-S'<refuted-string>' -- '*/src/*'` returning **empty** ⇒ the
wrong form *never entered canon*) turned out to be the single most decisive
instrument here, and it is **sweep-immune** in a way the add-then-delete
pickaxe is not. The §2a "add-then-delete is the red flag" framing implicitly
assumes the wrong form *did* land once. In practice, for spikes whose own
body carried the later-refuted form (5, 6, 9, 10 — and the broken primitive
in 1), the strongest clean verdict came not from finding-and-reading a
deleting commit but from proving the refuted string has **no add-commit at
all** across `src/`. That is a *stronger* clean signal than "added then
correctly deleted" (which still leaves a regression window); it means
integration-is-replacement was honored *at landing*, not as a later
cleanup. Suggest §2a name the exclusion-pickaxe (`empty add-set ⇒
never-admitted ⇒ regression-impossible`) as a first-class clean disposition
alongside "found the deleting commit, read why" — it is the cheaper and
sharper test when the spike's own body is the locus of the refuted form,
and it sidesteps rename-sweep recency-poisoning entirely.

---

*Read-only. No segments, spikes, INDEX, MANIFEST, moves, or commits were
touched. A confirmed regression would be a §4.1-class canon-lie for the
parent to mark; none was found among these ten.*
