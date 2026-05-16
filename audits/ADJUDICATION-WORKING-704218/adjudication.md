# Cluster A adjudication — self-disposed extracts (verify-and-mirror)

**Adjudicator:** fan-out agent (Cluster A), 2026-05-16
**Slice:** 13 `extracted-*` files, all carrying their own `## Disposition`.
**Method:** read every file in full; spot-checked the load-bearing dispositions
first-hand against current `src/` (slug-renamed corpus — segments now carry
role-prefixes, e.g. `der-causal-insufficiency-detection.md`,
`deriv-discrete-sector-condition.md`); confirmed ledger existence and
direction-correctness; treated `git`-recency as poisoned per the spine.
**Constraint honored:** report-only. No moves, edits, commits, or
segment/tracking-file changes. Routing/graduation is the parent's.

**Headline:** all 13 files' stated dispositions are **closure-direction-correct**
against today's `src/`. The dominant closure mode in this slice is
*resolved-by-strengthening*, exactly as the spine predicts for the math-heavy
ledgered cycles — and it is visibly so in the current segments, not merely
asserted in the extracts. **One disposition is stale-but-not-wrong**
(`extracted-codex-feedback-2026-04-28`: its three items are now *resolved*, the
file says "pending"); this is the only place where the file's word differs from
`src/`, and it differs in the *safe* direction (more closed than claimed). All
13 are **graduate** recommendations, with the 04-28 staleness noted for the
parent to reflect in the MANIFEST entry rather than treated as a blocker.

Soft / sentiment / declined / research-seed signal to mirror into the ledger is
collected in the final section (proposed rows **S8–S15**, numbering continues
from the current S7; parent assigns final numbers).

---

## Evidence spot-checks performed (the load-bearing ones)

These are the verifications that, had they failed, would have made a stated
disposition *wrong* rather than merely re-stated. All passed in the
strengthen-direction.

1. **2026-04-25 Gemini F1 (discrete→continuous Model S variance gap mis-stated
   as `O((η*)²)`).** Current `deriv-discrete-sector-condition.md:147–155,171,185`
   states the gap is `O(η* c_max²/c_min²) = O(c_max²/(c_min²ν))` — i.e. `O(η*)`,
   exactly Gemini's correction — *with the full Taylor-expansion derivation
   Gemini asked for* and an explicit sentence naming why the old `O((η*)²)` was
   the error ("inverting the leading `2η*c_min` … produces an `O(η*)`
   asymptotic gap"). `detail-linear-ode-approximation.md:154,171,186` carries
   the consistent statement. **Resolved by strengthening; ledger
   `pending-findings-2026-04-25.md` F-V1 is the durable record (exists,
   first-hand-verified there too).**

2. **2026-04-25 Gemini F2 (AR(1) exponent / simulation 1.481 vs 3/2 dismissed).**
   `result-adversarial-tempo-advantage.md:90` now states the 0.019 gap is *not*
   numerical noise but a **derived finite-ν correction factor**, proportional to
   `√((2c_min−η*_A c_max²)/(2c_min−η*_B c_max²))` — the *exact form Gemini
   predicted*. `result-adversarial-exponent-regimes.md:30,49` keeps "(simulation:
   1.481)" with the exponents now derived (validation, not foundation).
   **Resolved by strengthening.** The 04-25 extract's disposition is precise.

3. **2026-04-21 Gemini F1 (tempo-composition dimensional mismatch).**
   `der-tempo-composition.md:61,68,73–74` now divides `ε*ν_c` by
   `‖δ_critical‖`, units `[time⁻¹]`, under a "Consequences (dimensionally
   correct)" header — precisely the distance-normalization Gemini flagged as
   missing. **Resolved by strengthening.** `pending-findings-2026-04-21.md`
   exists and marks Finding A (temporal coarse-graining, Option-3 per-macro-step)
   and Finding B (observation-ambiguity) **RESOLVED 2026-04-22**; the extract's
   disposition matches the ledger verbatim.

4. **2026-04-21 Gemini F2 / 2026-04-22-morning Gemini F1 (Prop B.5/B.3a
   Bayesian-marginal contradiction; unbounded gradient updates on
   probabilities).** Both auditor findings asked for *softening/repair* (add a
   link function, clip, swap to gradient attribution). The project instead
   **strengthened**: there is now a dedicated derivation segment
   `deriv-edge-update-natural-parameter.md` — *"Log-Odds as the **Unique**
   Additive-Evidence Parameterization for Edge Credences"* (a uniqueness
   theorem, strictly stronger than "use logits"), plus
   `deriv-fisher-whitened-update-rule.md`, `deriv-l1-update-bias.md`,
   `der-chain-confidence-decay.md`. This is the canonical strengthen-before-
   soften shape and is exactly why the spine warns Cluster A to expect
   `correctly-rejected` / `resolved-by-strengthening` in the math-heavy
   ledgered cycles even though this slice is "extracts."

5. **2026-04-22 post-strengthening-evening (6d858f28) Finding 1 (KL-form
   "non-degeneracy" claim misleading; deterministic-π* makes reverse-KL
   `+∞`).** `form-strategy-complexity-cost.md:44–58,137` now **derives the KL
   direction** (π*-first) from a regret-bound + Pinsker argument, *and* invokes
   a uniqueness theorem (Hobson 1969; Csiszár; Aczél-Daróczy 1975) selecting
   reverse-KL uniquely among f-divergences. The segment itself records the
   lineage: V-medium (commit `a14682e`) introduced forward-KL → the audit
   caught the parallel degeneracy → strengthened to π*-first with a uniqueness
   theorem. **Resolved by strengthening.** `pending-findings-2026-04-22.md`
   (64 KB, comprehensive) is the durable ledger for all three Claude-feedback
   extracts; Finding 3 ≡ this item, marked RESOLVED-by-G-BP2; the segment
   strengthens past even that.

6. **Codex 04-02/04-03 (Q_O conditioning-vs-intervention; passive-observer
   scope contradiction).** `def-value-object.md:27,29,33` now uses
   `do(a_t = a)` explicitly with interventional-vs-conditioning prose and a
   Class-3 degradation caveat. `scope-adaptive-system.md:14,27,35,42` resolves
   the passive-observer contradiction via the clean two-tier split Codex's
   "open questions" pointed at (`#scope-adaptive-system` outer scope *including*
   passive Kalman/Bayesian learners; `#scope-agency` the intervention-bearing
   restriction). The "Codex open questions = reader-clarity gaps, preempt in
   segments" rule the 04-03 extract documents Joseph forming was itself applied.
   **Resolved.**

7. **Codex 04-06 #4 ("actually finish the proof — not the lazy
   reframing/demotion").** `deriv-graph-structure-uniqueness.md` now *proves*
   P3→Markov under causal sufficiency via the CMC (Spirtes-Glymour-Scheines
   Thm 3.4; Pearl Thm 1.4.1), with P3 *derived as a consequence* rather than
   postulated; the necessity gap (the full Cox parallel) is honestly scoped as
   open. This is a genuine strengthening, matching the 04-07 re-check's
   verdict (only causal-sufficiency mixed-messaging residual + observable-
   intermediates header persisted past that cycle — both editorial). **Resolved
   by strengthening.**

8. **Codex 04-28 hygiene re-check.** `bin/naming-aggregate.rb` now defaults
   `votes_dir: 'msc/naming/naming-votes'` (line 604/616–617) and refers to
   `doc/naming-principles.md` (lines 7,483) — both items **resolved**. Item 3's
   file `msc/naming/naming-pilot-rename-plan.md` no longer exists at that path
   (naming workspace reorganized). The extract's disposition says "Pending …
   don't appear to have been addressed yet" — **stale; all three are now
   closed.** Safe-direction staleness (more closed than the file claims).

9. **Codex 04-26 bridge spike.** `spikes/spike-transient-dependency-
   amplification.md` is catalogued in `spikes/INDEX.md:42` as **OPEN —
   self-blocked on formal construction**, Group V open-active-research per the
   TODO spike-audit triage. The extract's disposition (12 obligations = a
   roadmap if it moves toward promotion; provenance preserved) is correct:
   this is correctly an *open spike*, not an audit finding requiring closure.
   "Math lives in segments, not spikes" is respected — the spike records the
   reasoning trail and the obligations; nothing is overclaimed as landed.

---

## File-by-file

### 1. `extracted-audits-2026-04-21.md` — GRADUATE

Codex×3 + Gemini×2 passes (TST decision-integration, git-as-causal,
composition-consistency overgeneralization, Level-3-replay, tempo dimensional
mismatch, Prop B.5/B.3a, L1/L2 norm mixing, adversarial Model D/S, unity
fifth-axis, soft-facilitator L1, temporal coarse-graining).

- **Disposition direction:** correct. Two findings became
  `pending-findings-2026-04-21.md` Findings A & B (both RESOLVED 2026-04-22 —
  verified §3 above). The rest fed the 2026-04-22 cycle and recur in
  `pending-findings-2026-04-22.md` (composition-consistency overgeneralization,
  Prop B.5, L1/L2 mixing, Model D/S, soft-facilitator all appear there as
  tracked findings) — `subsumed-by-later-work` into the 04-22 ledger, named.
- **Strengthen-direction confirmed:** Prop B.5/B.3a → log-odds uniqueness
  theorem (§4); tempo dimensional mismatch → distance-normalized form (§3).
- **Soft/sentiment to mirror:** Codex's "the strongest 20% gets buried" framing
  and "satisfaction-gap/control-regret split is the most genuinely useful
  original formalization" → ledger (sentiment/calibration). The "abandon
  continuous-time / POMDP-collapse" cousins live in the 04-25 file (see #3).
- **Recommendation:** graduate. Durable record = `pending-findings-2026-04-21`
  (stays) + `pending-findings-2026-04-22` (stays). This extract is the
  verbatim-preservation companion; its value is the un-flattened auditor
  reasoning trail, correctly preserved.

### 2. `extracted-audits-2026-04-22-morning.md` — GRADUATE

Triple de-novo (Codex/Gemini/Opus), 15:13–15:16Z. Became Findings 1–11 in
`pending-findings-2026-04-22.md`; bigger-picture → `architectural-proposals-
2026-04-22.md` (G-BP1/2, O-BP1–6+).

- **Disposition direction:** correct and ledger-anchored. Ledger lines 5–13
  show Findings 1/3/5/7/10/11/13 RESOLVED with the strengthen-predecessor /
  strengthen-final spike pairs explicitly named (the canonical pattern). Opus's
  "sector-persistence template is the real theory" → became the
  separability/identifiability/forcing meta-segment organizing principle
  (`disc-separability-pattern.md`, `disc-identifiability-floor.md`,
  `disc-additive-coordinate-forcing.md` all present in `src/`). Gemini F1
  (unbounded gradient) resolved by strengthening (§4).
- **Soft/sentiment to mirror:** Gemini's "Bigger Picture" (natural-parameter
  unification / variational-FE reframe / Fisher-collapse) — partially *adopted*
  (the natural-parameter line literally became `deriv-edge-update-natural-
  parameter`), partially still research-seed-grade. Opus's six structural
  intuitions are tracked as O-BP* in the proposals file → those are
  `architectural`, already routed; the *un-adopted residue* (DAG-Boolean→
  continuous; orient-cascade-as-adaptive-cycle; identity-as-architectural-
  postulate) is research-seed → ledger.
- **Recommendation:** graduate. Note for parent: this extract's bigger-picture
  sections are the lineage source for the three landed meta-segments — its
  archaeological value is high; the MANIFEST entry should say "bigger-picture →
  O-BP*/G-BP* (architectural, routed); meta-segment lineage preserved."

### 3. `extracted-audits-2026-04-25.md` — GRADUATE

Gemini+Codex paired pass. Gemini F1/F2 = exact math errors (verified resolved-
by-strengthening, §2 above). Codex F1–F5 (C-iv adversarial-composite cross-seg
contradiction, C-iii vs G_c, zero-sum sign error in strategic-composition, git
timestamps overstating causal direction, TST developer-agent vs logogenic).

- **Disposition direction:** correct. Math findings → `pending-findings-2026-
  04-25.md` F-V1/F-V4/F-V5 (ledger exists, first-hand-verified there). The
  Gemini big-picture proposals (abandon continuous-time; action-as-observation
  POMDP collapse; technical-debt-as-mutual-information; MARL-as-composition)
  are correctly characterized as **considered-declined-with-reason** — the
  extract states the reason precisely ("the continuous-time bridge IS load-
  bearing for Lyapunov analysis; the action-vs-observation distinction IS what
  makes loop-interventional-access non-trivial"). This is exactly the band the
  ledger exists to protect; it must not be silently re-dropped.
- **Soft/sentiment to mirror:** the four declined big-picture proposals →
  ledger `considered-declined` (reason = payload). Codex's "announce the object
  first and the certificate second … more beautiful and more trustworthy"
  closing → sentiment/calibration (it converges with the OUTLINE "Reading AAT"
  preamble discipline already in CLAUDE.md).
- **Recommendation:** graduate. The declined-with-reason payload is the
  highest-value soft signal in this slice — strongly recommend the ledger row
  carry the *full* reason, not a summary, since it's a recurring temptation
  (POMDP-collapse is an attractive simplification an unaware future agent would
  re-propose).

### 4. `extracted-claude-feedback-2026-04-22-6d858f28.md` — GRADUATE

Post-strengthening-evening Opus (2nd of three 04-22 Claude sessions).
Findings: KL-form non-degeneracy misleading (F1); developer-as-act-agent
exact-status (F2, ≡ TODO Finding 14); identifiability-floor self-contradictory
tier labels (F3, drafting artifact).

- **Disposition direction:** correct. F1 resolved-by-strengthening (§5,
  decisive: the segment now *derives* direction + uniqueness theorem, strictly
  past the auditor's softening menu). F2 was already-tracked (ledger Finding
  14 / TODO) — `duplicate`/already-routed. F3 is a self-flagged drafting
  artifact on the meta-pattern status label — low-stakes; the meta-segment
  `disc-identifiability-floor.md` exists and the spine's three-meta-segment
  architecture stabilized, so the "self-contradictory tier labels" concern is
  `subsumed-by-later-work` (the meta-segment was re-authored as part of the
  M1/M2/M3 cycle).
- **Soft/sentiment to mirror:** the closing "the framework's honesty is
  *load-bearing* … deserves a first-class place in the top-level outline" →
  sentiment/calibration (this *did* land — it's now the CLAUDE.md "honesty as
  load-bearing architecture" posture and the OUTLINE preamble). Bigger-picture
  A–G: A (projection-defect unification), E (Cox necessity reachable), G
  (per-segment derived/chosen/assumed table) are research-seeds; B/C/F overlap
  the already-routed O-BP* / meta-segment work.
- **Recommendation:** graduate. F3 is the only soft spot — flag for parent as
  "self-flagged drafting artifact, subsumed by the M1 meta-segment re-author;
  not an open defect."

### 5. `extracted-claude-feedback-2026-04-22-3546217a.md` — GRADUATE

Third 04-22 Claude session (19:52Z, post-strengthening). Six findings A–F
*distinct from the other two sessions* (ρ_Σ unmeasurable threshold; update-rule
heterogeneity as independent closure-defect axis; stacked Class-1 ∩ learning-
agent scope; bridge-lemma Tier-3 prevalence uncharacterized; orient-cascade 4c
SNR; "DAG is forced" overstatement). Plus bigger-picture 1–7.

- **Disposition direction:** correct, and this is the most archaeologically
  load-bearing of the three Claude extracts (its own Disposition section
  honestly says Findings B–F "not surfaced in any existing audits/msc/segment
  file"). Finding A (ρ_Σ) was preserved as the F28-territory note in
  `msc/AUDIT-WORKING-584721/` — that's the 584721 cycle (Cluster B's slice),
  so Finding A is **cross-referenced into a Cluster-B-owned ledger**; correct
  not to double-track here. Findings B (two-axis closure), C (scope layering),
  D (Tier-3 prevalence), E (4c SNR), F (DAG-forced framing): B/C/F are
  framing/integration-debt items that recur in the 04-22 ledger's
  scope-layering and unity-dimensions findings (`subsumed`); D (Tier-3
  prevalence) and E (4c SNR sensitivity bound) are genuine **research-seeds**
  not closed anywhere — these are the real residue.
- **Strengthen-direction note:** the spine's bite applies here. Finding F
  ("DAG is forced" overstates) is *correctly-rejected-adjacent*: the project's
  response was to *prove* P3→Markov under causal sufficiency (§7), strengthening
  the claim while honestly scoping the necessity gap — not softening "forced"
  to "motivated." `deriv-graph-structure-uniqueness.md:15,17` is now exemplary
  on exactly this asymmetry. Finding F is closed in the strengthen direction.
- **Soft/sentiment to mirror:** Finding D (Tier-3 prevalence in practical
  composites) and Finding E (4c covariance-test sensitivity bound) →
  research-seed (both have a concrete derivable target: "characterize fraction
  of practical composites that are Tier-3"; "derive SNR bound for the sibling-
  covariance test at convergence"). Bigger-picture 4 (two-tier "Reader's Path"
  presentation), 5 (composition-closure may be over-engineered), 6 (most-novel-
  contribution-isn't-where-claimed → epistemic architecture), 7 (dual-edged
  identifiability-floor) → research-seed / considered. Note: BP-6 *did* land
  (it's the CLAUDE.md "epistemic architecture is what makes the integration
  distinctive" posture) → that one is sentiment/superseded-by-landed-posture.
- **Recommendation:** graduate. **Surface to parent:** Findings D and E are the
  most substantive un-closed items in the entire Cluster-A slice. They are not
  defects (the segments honestly flag both as open), but they are genuine
  research-seeds that no later ledger closes — they deserve ledger rows that
  *graduate-watch* (D especially: "composition theory's central transferability
  result is unavailable in exactly the regime where composition is most
  interesting" is a sharp, true, and structurally important observation that
  could mature into a PROPOSALS entry).

### 6. `extracted-claude-feedback-2026-04-22-bf945f78.md` — GRADUATE

First 04-22 Claude session (15:00Z, *pre*-strengthening). Opus F1–F5 (= the
"Opus F1–F5" batch in `pending-findings-2026-04-22.md`) + bigger-picture 1–7.

- **Disposition direction:** correct and fully ledger-anchored. F1 (L0 residual
  on-policy) = ledger Finding 1 RESOLVED via no-go strengthening (the ledger
  explicitly names `spike-finding-1-l0-residual-repair.md` [softening
  predecessor] vs `spike-finding-1-strengthening.md` [the strengthening that
  landed] — canonical pattern). F3 (Section II preamble understates survival)
  = ledger Finding 9 → O-BP1. F4 (IB status mismatch) = Finding 10 RESOLVED
  (discussion-grade → exact-applied-external-theorem). F5 (4c convergence) =
  Finding 11 PARTIALLY RESOLVED, compounded with F1. F2 (C-iii vs A1) = Finding
  8, tracked. **This extract's content is near-identical to bf945f78's findings
  also appearing verbatim in 6d858f28's "morning audit" cross-references** —
  expected (Joseph ran the same prompt thrice); not a double-track problem
  because the ledger consolidates them.
- **Note on near-duplication with file #2 (extracted-audits-2026-04-22-morning):**
  bf945f78 *is* the Opus pass inside the 04-22-morning triple. File #2 carries
  the Codex+Gemini+Opus triple in one doc; this file is the standalone verbatim
  Opus session transcript with full reasoning trail + the rescinded-findings
  table + msc cross-check. Per the spine's `duplicate` discipline: not a
  verbatim repeat — it's the *fuller* source (file #2's Opus section is the
  same audit; this preserves the un-abridged version incl. the
  "spike needs the same repair as the segment" integration-debt callout). Both
  graduate; the MANIFEST should note the relationship so they aren't read as
  independent corroboration.
- **Soft/sentiment to mirror:** bigger-picture 1–7 substantially overlap file
  #2's Opus bigger-picture (same session family) → mirror once, attributed to
  the 04-22 Opus pass, not twice.
- **Recommendation:** graduate. Flag the file#2/file#6 same-audit relationship
  for the parent's MANIFEST entry (epistemic-independence hygiene: three
  *prompts* on 04-22, but bf945f78 and the 04-22-morning Opus section are one
  audit).

### 7. `extracted-codex-feedback-2026-04-01.md` — GRADUATE

First fresh Codex pass post-restructure (ACT-era slugs `01-act-core`). Six
findings (directed-separation scope / composition theorem debt / strategy-DAG
not forced / CIY not hard-core / git overclaims causal / convergence risk) +
"What I Would Do Next".

- **Disposition direction:** correct. Pre-ledger (no `pending-findings`);
  disposition rests on first-hand re-read + corpus-redundancy, per evidence
  hierarchy tier 4. Every finding recurs in the ledgered 04-02/03/06/22/25
  cycles and is closed there: composition bridge-lemma (→ ledgered, the
  contraction-assumption tiering landed), strategy-DAG forcing (→ proved under
  causal sufficiency, §7), CIY (→ CIY→LMI strengthening, tracked in 471203
  cycle per MANIFEST), git-as-causal (→ `pending-findings-2026-04-22` Finding
  7 RESOLVED, `C_t^commit` added to NOTATION). `subsumed-by-later-work`,
  subsumers named. The "strongest 20% buried under unfinished 80%" convergence
  risk is process-feedback, not a framework defect.
- **Soft/sentiment to mirror:** "the satisfaction-gap / control-regret split is
  the most genuinely useful original formalization in the repo" + "simulation
  work looks serious rather than decorative … good scientific discipline" →
  sentiment/calibration (recurring across multiple Codex passes — a stable
  external read worth recording once). "What I Would Do Next" #1 (write the
  Section-I-kernel paper first) → this matured into the publication-program
  strategy; `considered`/superseded-by-landed-strategy.
- **Recommendation:** graduate. Old (pre-ledger) but every substantive finding
  is corpus-redundant and closed in a ledgered successor; safety net holds.

### 8. `extracted-codex-feedback-2026-04-02.md` — GRADUATE

Heavy-feedback day, ≥5 Codex passes (CIY mis-spec, Q_O conditioning-vs-
intervention, strategy-maintenance loop incompleteness, composition bridge,
scope contradictions, per-dimension-persistence regime mixing, passive-observer
contradiction, persistence dual-sense conflation).

- **Disposition direction:** correct. Disposition says these drove the
  04-02→04-06 strengthening cycle and most were marked Resolved by
  `analysis-2026-04-02-comprehensive.md`. Verified first-hand: Q_O do-operator
  (§6 — `def-value-object.md:27` uses `do(a_t=a)`), passive-observer scope
  (§6 — `scope-adaptive-system.md` two-tier split), persistence dual-sense
  (the `persistence-condition`/structural-vs-task-adequacy split is now a
  named distinction — recurs and closed in later ledgered cycles),
  P3→Markov (§7). All `resolved`, several by strengthening.
- **Soft/sentiment to mirror:** the recurring "Section I is the strongest part;
  the lift into agency/composition is where it gets less secure" assessment
  (appears in nearly every Codex pass 04-01 through 04-22) → sentiment, mirror
  *once* as a stable cross-pass external calibration signal, not per-file.
- **Recommendation:** graduate. Note: this file is large (5 batches) and is the
  richest single archaeology of the 04-02→06 strengthening cycle's *input*;
  archaeological value high, all findings closed in successors.

### 9. `extracted-codex-feedback-2026-04-03.md` — GRADUATE

Two Codex passes. **Historically pivotal**: this is the file where Joseph forms
the enduring rule *"Codex open questions = reader-clarity gaps, not unanswered
research"* (now in CLAUDE.md Working Conventions) and the "neither pedantic nor
face-value" posture.

- **Disposition direction:** correct. Findings (δ_s vs δ_strategic confusion,
  value-object causal-validity smuggling, composition gateway prematurity,
  loop-Level-2 over-universalization, team-persistence double-counting,
  predictive-vs-causal collapse) all drove the next strengthening cycle and
  recur/close in ledgered successors. Spot-checked: value-object causal-validity
  is now an explicit, scoped subsection with the Class-3 caveat
  (`def-value-object.md:31–39`) — exactly the "separate the causal-validity
  discussion into its own conditional segment" open-question, preempted in
  the segment per the rule this very file births. Self-demonstrating closure.
- **Process/instruction-feedback:** the rule-formation exchange is **not a
  framework finding** — it's `process/instruction-feedback` that *already
  landed in CLAUDE.md*. Recommend the MANIFEST entry explicitly note this
  file's provenance value (it is the primary source for a live working
  convention); it should graduate *with that note*, not be read as ordinary
  findings archaeology.
- **Soft/sentiment to mirror:** none beyond the stable Section-I-strongest
  signal (already mirrored once, #8).
- **Recommendation:** graduate, with the rule-provenance note.

### 10. `extracted-codex-feedback-2026-04-06.md` — GRADUATE

Three passes across 04-06/07, including the 04-07 *re-check* (same Codex agent
re-reviews progress — itself archaeology of how external review tightens a
theory across short cycles). Contains the canonical "no shortcuts / no implicit
resource constraint" Joseph statement (now a CLAUDE.md working convention).

- **Disposition direction:** correct and unusually well-evidenced *by the
  extract itself*: the 04-07 re-check is a built-in verification — Codex
  confirms loop-access, orient-cascade, composition-closure all materially
  improved and downgrades them, keeping only causal-sufficiency mixed-messaging
  + observable-intermediates header as residual. First-hand check (§7):
  `deriv-graph-structure-uniqueness.md` now *proves* P3→Markov under causal
  sufficiency (the strengthening Joseph explicitly demanded — "actually finish
  the proof, not the lazy reframing"), and the residual mixed-messaging is
  scoped honestly. `resolved-by-strengthening`; the two 04-07 residuals are
  editorial and recur in the ledgered 04-22+ cycles.
- **Process/instruction-feedback:** the "no shortcuts / not value-per-___"
  statement is the canonical strengthen-before-soften / false-constraints
  source — `process/instruction-feedback`, already landed in CLAUDE.md.
  MANIFEST entry should note provenance value.
- **Soft/sentiment to mirror:** "those feel like real theory, not just
  vocabulary" (re persistence machinery, satisfaction-gap/regret split,
  acyclicity-from-temporal-ordering, regime-sensitive adversarial exponents) →
  sentiment/calibration.
- **Recommendation:** graduate, with the no-shortcuts-rule provenance note.
  The 04-07 re-check makes this one of the better-evidenced pre-ledger files.

### 11. `extracted-codex-feedback-2026-04-22-r2.md` — GRADUATE

Second 04-22 Codex pass. Findings = `Codex r2 F1–F5` in
`pending-findings-2026-04-22.md` (ledger lines 47–50). Bigger Picture seeded
**C-BP1** (three-layer claim separation: defined / causally-valid /
operationally-extractable) → became the three meta-segments.

- **Disposition direction:** correct and ledger-anchored. F1 (L0 residual) →
  resolved (commit `14a6095`). F3 (L1-as-default overgeneralization) →
  resolved (commit `4d050c8`, Prop B.7 + Cramér-Rao — a *strengthening*: the
  auditor said "the headline overgeneralizes," the project derived B.7 to make
  the strong claim *true* for observable-C and *refuted* it for unobservable-C
  rather than just softening the headline). F2/F4/F5 → C-BP1/C-BP4/C-BP3
  (`architectural`, routed to the proposals portfolio). The C-BP1 three-layer
  pattern is now load-bearing across `disc-identifiability-floor` /
  `disc-separability-pattern` / `disc-additive-coordinate-forcing` (all in
  `src/`).
- **Soft/sentiment to mirror:** the four Bigger-Picture moves — three are
  `architectural` and *already routed* (C-BP1 landed as the meta-segment
  framework; C-BP3 software-as-calibration-laboratory landed in TST framing;
  claim-level-vs-segment-level status partially adopted via the per-claim
  Findings schema). The *un-fully-adopted* residue ("move from segment-level
  to claim-level statuses everywhere") is research-seed/considered → ledger.
- **Recommendation:** graduate. High architectural-lineage value (C-BP1 → the
  three meta-segments); MANIFEST entry should credit the lineage.

### 12. `extracted-codex-feedback-2026-04-26-bridge-spike.md` — GRADUATE

Codex's substantive mathematical contribution to
`spike-transient-dependency-amplification` (Gemini-started, Codex-rebuilt) +
12 remaining-obligations roadmap + Joseph's provenance note.

- **Disposition direction:** correct. This is **not an audit-findings file** —
  it is a spike-contribution + obligations roadmap + provenance record. The
  spike is correctly OPEN in `spikes/INDEX.md:42` (Group V open-active-
  research, "self-blocked on formal construction"). The 12 obligations are the
  roadmap-if-promoted, not findings requiring closure. Provenance (Gemini
  initiated → Codex overwrote/rebuilt, can't reference Gemini's originals) is
  preserved here and is the *only* place it is — archaeologically load-bearing.
  Respects "math lives in segments, not spikes" (nothing overclaimed as
  landed) and "spike-references-only-in-Working-Notes".
- **Soft/sentiment to mirror:** none (this is a research-trail artifact, not
  soft-finding signal). The 12-obligation roadmap itself is research-seed-grade
  but it is *already housed* in the spike + `spikes/INDEX.md` + the referenced
  TODO triage groups — mirroring to the ledger would duplicate, not preserve.
  Recommend: do **not** create a ledger row; the spike INDEX entry is its
  durable home. The MANIFEST entry should explicitly record the
  Gemini→Codex provenance so it survives the file's graduation.
- **Recommendation:** graduate, classified `research-trail / provenance`, with
  the provenance note carried into the MANIFEST. This is the one file in the
  slice that is *not* findings-shaped — flagging it so the parent doesn't
  ledger-route it by reflex.

### 13. `extracted-codex-feedback-2026-04-28.md` — GRADUATE (with staleness note)

Targeted post-cleanup Codex re-check. Three residual stale-default / stale-path
items in `bin/naming-aggregate.rb` and `msc/naming/naming-pilot-rename-plan.md`.

- **Disposition direction:** the *file's stated disposition is stale*. It says
  "Pending — these three items … don't appear to have been addressed yet
  (verifying would require a current `bin/naming-aggregate.rb` inspection,
  beyond the scope of this archaeological extraction)." I performed that
  inspection (§8): **all three are now resolved** — `bin/naming-aggregate.rb`
  defaults to `msc/naming/naming-votes` and refers to `doc/naming-principles.md`;
  item 3's file no longer exists at the cited path. This is the one file where
  the stated disposition diverges from `src/` — but it diverges in the **safe
  direction** (more closed than the file claims), so it is *not* a
  closure-direction error; it is a freshness lag the extract itself flagged as
  unverified.
- **Classification:** `process/instruction-feedback` (build-tooling hygiene,
  not framework) — all `resolved`.
- **Recommendation:** graduate. **Surface to parent (this is the brief's
  "where a stated disposition turns out stale, that itself is the finding"
  case):** the MANIFEST entry should record the disposition as *resolved*, not
  *pending* — i.e. the parent should write the corrected disposition into the
  MANIFEST rather than mirror the file's "Pending" text. No `src/` action
  needed (already done); the only action is not propagating the stale "Pending"
  into the audit trail.

---

## Soft / sentiment / declined / research-seed → proposed ledger rows

Numbering continues from current ledger max **S7**. Parent assigns final
numbers and does the actual ledger edit (report-only here). Deduplicated and
themed per the ledger's anti-reburial discipline — the recurring "Section I
strongest" cross-pass signal is mirrored **once** (S9), not per-file.

| Proposed # | Band | Finding (attributed) | Source audit(s) | Suggested status |
|---|------|----------------------|-----------------|--------|
| S8 | considered-declined | **POMDP-collapse family.** Four Gemini big-picture proposals: (1) abandon continuous-time ODE/SDE, treat software as discrete MDP/POMDP; (2) "action as observation" belief-MDP collapse replacing CIY with Bellman VOI; (3) technical-debt = mutual-information between code lexical structure and domain model; (4) sub-agent composition = MARL with communication costs. **Declined with reason (the payload — must not be silently re-proposed):** the continuous-time bridge is load-bearing for the Lyapunov/sector-condition machinery (it is *what* the persistence theorems are stated over); the action-vs-observation distinction is precisely what makes `#der-loop-interventional-access` non-trivial (collapsing it erases the Level-2 contrast); CIY is retained because the regret-bounded objective needs the interventional-distinguishability quantity, not VOI. POMDP-unification recurs as an attractive simplification — recorded so an unaware future agent doesn't re-litigate it from scratch. | extracted-audits-2026-04-25 (Gemini big-picture) | noted (declined-with-reason; revisit only if the continuous-time bridge is ever independently shown non-load-bearing) |
| S9 | sentiment | **Stable cross-pass external calibration: "Section I is the strongest; the lift into agency/composition is where rigor thins."** Independently and repeatedly stated by Codex (04-01, 04-02 ×3, 04-03 ×2, 04-06 ×3) and echoed by Opus. Plus the specific positive: the satisfaction-gap / control-regret split and acyclicity-from-temporal-ordering are repeatedly named as "the most genuinely useful original formalization" / "real theory, not just vocabulary." Calibration signal: the asymmetry is real and externally legible; the named-strongest results are the ones to lead with publicly. | extracted-codex-feedback-2026-04-01/02/03/06; extracted-audits-2026-04-21 | noted (sentiment; converges with the publication-kernel strategy already in ops) |
| S10 | sentiment | **"The framework's honesty is load-bearing" + "epistemic architecture is the most novel contribution, more than the integration narrative."** Opus, 6d858f28 closing observation + 3546217a big-picture #6. Calibration signal: *this landed* — it is now the CLAUDE.md "honesty as load-bearing architecture" posture and the OUTLINE "Reading AAT" framing. Recording as superseded-by-landed-posture so the audit retires as fully accounted. | extracted-claude-feedback-2026-04-22-6d858f28; -3546217a | superseded-by the CLAUDE.md honesty-as-architecture posture + OUTLINE preamble |
| S11 | research-seed | **Tier-3 prevalence in practical composites.** The composition-closure bridge lemma is proved (Tier 1) for an estimation-flavored class; the weakest-link bound makes any composite with one rule-based/non-convex component Tier-3 ("verify per-domain"). The frequency with which Tier-3 binds in practical composites (most human teams, most multi-LLM systems) is uncharacterized, and the sharp true observation is "the central transferability result is unavailable in exactly the regime where composition is most empirically interesting." Concrete derivable target: characterize / bound the practical-composite fraction that is Tier-3, or reframe composition-closure explicitly as "exact for a narrow estimation-flavored class; structural template otherwise." | extracted-claude-feedback-2026-04-22-3546217a §Finding D | open (research-seed; **graduate-watch** — strong candidate to mature into a PROPOSALS entry) |
| S12 | research-seed | **4c sibling-covariance test sensitivity bound.** The orient-cascade step-4c causal-sufficiency check is the unique broadly-available L0→L1 escalation diagnostic (backed by the no-go), but its practical sensitivity ("how cleanly the agent separates sibling-covariance signal from edge-credence noise at convergence") is flagged open and degrades exactly in adversarial / fast-drifting regimes where causal-insufficiency detection matters most. Concrete target: derive an SNR / effective-sample-size bound for the covariance test at convergence and surface it in the cascade, not only the sister segment. | extracted-claude-feedback-2026-04-22-3546217a §Finding E (and bf945f78/6d858f28 Finding 5 / ledger Finding 11, residual) | open (research-seed) |
| S13 | research-seed | **Un-adopted residue of the 04-22 Opus bigger-picture.** After O-BP*/G-BP* and the three meta-segments landed, three structural intuitions remain un-closed: (a) DAG-Boolean → continuous strategy layer (graded parent influences would handle soft facilitators natively); (b) the orient cascade is itself an adaptive cycle (recursive AAT-applies-at-every-level formulation unifying deliberation / cascade / composition); (c) agent-identity promoted from discussion-grade scope to an architectural postulate ("AAT applies to agents on singular causal trajectories"). Speculative; each is a coherent direction, none forced by a current finding. | extracted-audits-2026-04-22-morning; -bf945f78; -3546217a (Opus big-picture) | open (research-seed) |
| S14 | research-seed | **(b) Cox-necessity for graph-structure-uniqueness is plausibly reachable.** `deriv-graph-structure-uniqueness` is sufficiency-only and honestly scopes the gap; the necessity direction (no non-DAG structure — factor graphs, junction trees, chain graphs — satisfies P1–P4 + causal sufficiency) is suggested reachable via Lauritzen's characterization of Markov properties on graph classes. Would elevate the result from "must-if-sufficient-via-this-route" to a full Cox-style necessary-and-sufficient theorem. | extracted-claude-feedback-2026-04-22-6d858f28 §big-picture E | open (research-seed; this is a strengthen-direction seed — graduate-watch) |
| S15 | considered | **Per-segment "derived / chosen / assumed" table + minimal-viability worked example.** Opus (6d858f28 §G) named two disproportionately-valuable presentational moves: a compact derived-vs-chosen-vs-assumed table in every derivation-type segment (the `#graph-structure-uniqueness` one is "the clearest epistemic signal in the repo"), and a single worked example instantiating every Section I/II quantity concretely. Partially addressed (per-segment `## Findings` + FORMAT discipline move toward the first; worked examples exist but scoped). Recording so the trade-off (uniform-table cost vs. epistemic-legibility) is not silently re-litigated. | extracted-claude-feedback-2026-04-22-6d858f28 §big-picture G | noted (considered; partially superseded by the `## Findings` schema + FORMAT.md; residual = the uniform per-segment table, deliberately not universal) |

**Not mirrored, by design (with reason):**
- The 04-22 Opus six structural intuitions that became O-BP1–O-BP6 and the
  C-BP1 three-layer pattern → these are `architectural` and *already routed*
  to `architectural-proposals-2026-04-22.md` / the three landed meta-segments.
  Mirroring them to the ledger would double-track; the ledger row would
  duplicate a PROPOSALS-grade item. (S13/S14 capture only the *un-adopted
  residue*.)
- The 12-obligation bridge-spike roadmap (file #12) → already housed in
  `spike-transient-dependency-amplification.md` + `spikes/INDEX.md` + the
  TODO spike-audit triage groups. A ledger row would re-bury, not preserve.
- Codex/Joseph rule-formation exchanges (files #9, #10) → `process/
  instruction-feedback` that *already landed in CLAUDE.md* (Codex-open-
  questions rule; no-shortcuts/false-constraints rule). Not soft-findings;
  their value is provenance, carried in the MANIFEST entry, not the ledger.

---

## Things that don't fit the frame (surfaced per brief)

1. **`extracted-codex-feedback-2026-04-28.md` stale "Pending" disposition.**
   The brief's explicit case: a stated disposition that turns out stale against
   today's state *is itself the finding*. All three items are resolved; the
   file says pending. Safe-direction (more-closed-than-claimed), so not a
   closure-direction error — but the parent should write the *corrected*
   disposition into the MANIFEST, not mirror the file's "Pending" text. This
   is the single actionable adjudication-level correction in the slice.

2. **File #6 (bf945f78) and file #2 (extracted-audits-2026-04-22-morning) are
   the same audit, not independent corroboration.** bf945f78 *is* the Opus
   pass inside the 04-22-morning triple; file #2's Opus section is the
   abridged form, file #6 the un-abridged transcript. Both should graduate,
   but the MANIFEST should record the relationship so a future reader doesn't
   count them as two independent Opus reads of the same snapshot (epistemic-
   independence hygiene — the project cares about this; cf. the
   convergence-as-evidence discipline, which only holds for *independent*
   probes).

3. **Files #9 and #10 are primary sources for live CLAUDE.md working
   conventions** (Codex-open-questions-are-reader-clarity-gaps;
   no-shortcuts/false-constraints/strengthen-before-soften). They graduate as
   findings archaeology, but their higher value is provenance. Recommend the
   MANIFEST entries explicitly note "primary source for CLAUDE.md Working
   Convention X" so the lineage survives the file leaving the active backlog.

4. **File #12 is not findings-shaped.** It is a spike-contribution +
   obligations-roadmap + provenance record. It graduates as `research-trail /
   provenance`, *not* via the ledger or TODO. Flagged so the parent doesn't
   reflex-route the 12 obligations into TODO (they are already in the spike +
   INDEX + the TODO spike-audit triage; re-routing would re-bury).

5. **The strongest un-closed substantive residue in the entire Cluster-A
   slice is 3546217a Findings D and E** (Tier-3 prevalence; 4c covariance-test
   sensitivity bound) → proposed S11/S12, both graduate-watch. Neither is a
   defect (the segments honestly flag both open); both are research-seeds the
   project would benefit from holding *visibly* rather than letting evaporate
   when these extracts retire. S11 in particular ("central transferability
   result unavailable exactly where composition is most interesting") is a
   sharp, true, structurally important observation — a strong PROPOSALS
   candidate if it matures.

6. **Strengthen-before-soften is visibly the dominant closure mode here, and
   it is real in `src/`, not asserted in the extracts.** The three sharpest
   instances — log-odds uniqueness theorem (vs. "add a link function"),
   π*-first KL derived + uniqueness theorem (vs. "reverse the direction or
   acknowledge"), P3→Markov proved under causal sufficiency (vs. "demote
   'forced' to 'motivated'") — are each cases where an auditor offered a
   softening menu and the project instead made the strong claim *true* under
   stated conditions, often producing a *stronger* result (a uniqueness
   theorem) than the original assertion aspired to. Per the spine and
   `strengthen-before-soften.md`: these findings are **correctly closed**, and
   any future reader of these extracts who sees "the auditor said X is broken"
   should be pointed at the strengthened segment, not led to reopen X.
