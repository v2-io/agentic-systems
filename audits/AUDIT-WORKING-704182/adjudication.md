# Cluster C adjudication — 2026-04-24/25 cluster + hygiene + portfolio extract

**Adjudicator:** independent co-owner pass, 2026-05-16. Adjudication-only; no
moves/edits/commits. Routing actions are the parent's + Joseph's.

**Slice (per spine §"Cycle 1 / C"):**
- `audits/audit-2026-04-24-fresh-pass.md`
- `audits/audit-final-reports-candidate-extraction-2026-04-25.md`
- `audits/link-and-file-hygiene-findings.md`
- `audits/extracted-claude-feedback-2026-04-22-25-portfolio-reviews.md`
- Ledger read as evidence (NOT graduated — durable infrastructure):
  `audits/pending-findings-2026-04-25.md`

**Evidence method.** Ledger + candidate-extraction §Status claims read as
*claims to verify*, not as ground truth (git-recency poisoned by the
2026-05-15 rename sweep). Every consequential disposition below is
first-hand-verified against **current `src/`**. Where the candidate-extraction
doc claims "RESOLVED commit a6b61fb" I confirmed the resolution is present in
today's segment text *and checked its discharge direction* (strengthen vs.
soften), because the spine's enum makes direction load-bearing.

**Headline.** Of the 8 F-V/P-V findings, **all 8 are resolved in current
`src/`, and 5 were discharged by *strengthening*** (the direction this project
prefers and the spine flags as `correctly-rejected`-adjacent / `resolved`-by-
strengthening). The 4 §C "strengthening-needed, do NOT dispatch" items all
landed as **strengthenings** (not softenings) — including SN-3, where the
strengthening landed in the *downstream* TST segment but the **upstream source
segment still carries the raw overclaim**: that residual is the one genuine
open defect this slice surfaces. The hygiene file (2026-04-28) is **almost
entirely stale-now** (docs rewritten 2026-04-28+); one item (lint state) has a
*new, different* live value worth surfacing. One finding (F-V3/F8) is
**correctly still-open** and already triple-tracked. The portfolio-extract is
**process/strategic provenance**, not framework findings.

---

## File 1 — `audit-2026-04-24-fresh-pass.md`

This file's substantive findings are F-V1..F-V5 + P-V1..P-V3 + the J1..J10
confirmations + B1..B7 bigger-picture. Its findings were extracted into the
durable ledger `pending-findings-2026-04-25.md` (read as evidence). I
adjudicate the findings against current `src/`; the J/B items I dispose at the
end.

### F-V1 — discrete-to-continuous Model S variance gap mis-stated as O((η*)²)

- **Valid in the first place?** Yes — math error, the ledger re-derived it two
  independent ways (Taylor + numerical), confidence High.
- **Valid as of today's `src/`?** No — **resolved, by strengthening.**
  `deriv-discrete-sector-condition.md:147–155` now states the gap as
  `O(η* c_max²/c_min²) = O(c_max²/(c_min²·ν))`, gives the explicit
  leading-order Taylor expansion `V_ss/V_c = 1 + η*c_max²/(2c_min) + O((η*)²)`,
  and propagates the correction to `detail-linear-ode-approximation.md:154,186`.
  The internally-inconsistent `O(η* c_max/ν)` sentence flagged in the ledger
  (`detail-linear-ode-approximation.md:163`) is **gone**. The fix went *beyond*
  the audit's ask (`O(1/ν)`): it identifies the conditioning-ratio dominance
  `c_max²/c_min²`, a sharper statement than requested.
- **Disposition:** `resolved` (by strengthening).
- **Residual (new, minor, surfaced):** `hyp-mismatch-dynamics.md:54` still
  states the Model S gap as `O(η* c_max)` (the *pre*-F-V1 scaling). This is a
  fresh integration-drift micro-defect introduced by the F-V1 fix not
  propagating to one cross-referencing segment. Recommend → **TODO** (one-line
  editorial; same class as F-V2/F-V5 integration drift). Confidence High
  (textual, direct).

### F-V2 — scope-multi-agent excludes adversarial; scope-composite-agent admits via C-iv

- **Valid in the first place?** Yes — cross-segment contradiction, High.
- **Valid as of today's `src/`?** No — **resolved.**
  `scope-multi-agent.md:67–75` no longer categorically excludes adversarial
  pairs; it now partitions: equilibrium-convergent adversarial pairs →
  `#scope-composite-agent` (C-iv) strategic composites; cyclic/non-convergent
  and asymmetric attacker/target → agent-level machinery
  (`#der-adversarial-destabilization`). Clean agent-level vs composite-level
  split; consistent with `scope-composite-agent.md:69`.
- **Disposition:** `resolved`.

### F-V3 — C-iii mutual-benefit composites lack coherent G_c = (O_c, Σ_c)

- **Valid in the first place?** Yes — internal inconsistency; ≈ F8 from the
  2026-04-22 batch (same finding, two audits). High.
- **Valid as of today's `src/`?** **Partially mitigated by strengthening;
  routing decision genuinely still open.** `scope-composite-agent.md:40` now
  defines C-iii via an explicit relevance variable `Y` with a per-pair
  marginal-contribution inequality, and lines 79/83 explicitly carve out the
  `U_O`/`G_c`-as-quality-conditional-on-scope vs. scope-variable distinction —
  so the bald "no O_c → fiction" tension is now *scoped*, not raw. But the deep
  question (does C-iii get an induced O_c, or a different macro-object, or
  route-split) is **Path A (editorial induced-O_c) vs Path B (SP-21
  architectural split)**, a Joseph-call.
- **Disposition:** `actionable-open` — and **already correctly tracked in three
  places**: `TODO.md:95` ("Open routing decision: F8 / F-V3 — composite-agent
  C-iii", Path A/B), `PROPOSALS.md` SP-21 §G (full schema; findings-subsumed
  clause names F-V2/F-V3/F8; deferral rationale recorded), and the
  `pending-findings-2026-04-25.md` ledger. **No new routing needed; do not
  double-track.** This is the one finding in the slice that legitimately keeps
  an audit from being retired *as still-open* — but it is routed, so the
  source audit can graduate (the open item lives in TODO/PROPOSALS, not in the
  audit file).

### F-V4 — sign error in zero-sum worked example (deriv-strategic-composition)

- **Valid in the first place?** Yes — real math error in a promoted segment's
  worked example, High.
- **Valid as of today's `src/`?** No — **resolved, by strengthening (a strong
  instance).** `deriv-strategic-composition.md:74–113` now: (a) corrects the
  potential to `Φ = a_A + a_B`, NE at `(1,1)`, with the explicit
  action-coefficient-vs-state-preference analysis (lines 78–88); (b) **adds a
  second, Cournot interior-NE instantiation** with genuine quadratic curvature
  (lines 94–113) — *not requested by the audit*; and (c) at line 90 **honestly
  documents that the corrected corner-NE example does *not* support the
  sector-template transfer** ("the template's (T2) sector lower bound … does
  not hold without modification"), then supplies the Cournot case that does.
  This is the canonical strengthen-then-scope-honestly discharge: the error
  wasn't merely corrected, the segment was made strictly stronger
  (two complementary instantiations) and the scope-limit of the simple one was
  surfaced rather than papered over.
- **Disposition:** `resolved` (by strengthening). Spike cross-check
  (`spikes/spike-strategic-composition.md` carrying the same error) is a
  reasoning-trail artifact, not a graduation blocker — spikes record trails,
  not theory (per `feedback_math_lives_in_segments`); flag for the parent only
  if spike hygiene is independently in scope.

### F-V5 — TST scope-developer-agent doesn't surface Class 2/3 caveats

- **Valid in the first place?** Yes — cross-component integration debt,
  Medium-high → High.
- **Valid as of today's `src/`?** No — **resolved.**
  `02-tst-core/src/scope-developer-agent.md` now carries the
  Class 3 (Coupled) / `κ_processing ≈ 1` caveat at line 66, the
  coupled-update-dynamics caveat for logogenic developer-agents at line 76, and
  the reconstructed-from-weights+memory+prompt correction (replacing "M_t reset
  to near-zero") at line 169, with `depends:` updated
  (`scope-logogenic-agent`, `def-coupled-update-dynamics`,
  `obs-context-turnover`) and a GUC-rename migration note (line 215). Fully
  integrated cross-component.
- **Disposition:** `resolved`.

### P-V1 — "not a discretization artifact" too strong (result-adversarial-tempo-advantage)

- **Valid in the first place?** Yes — framing, Medium-high.
- **Valid as of today's `src/`?** No — **resolved, by strengthening.**
  `result-adversarial-tempo-advantage.md:90` now states the 1.481-vs-3/2 gap is
  "*not pure numerical noise*" and gives the **derivable** finite-ν correction
  factor `√((2c_min − η*_A c_max²)/(2c_min − η*_B c_max²))`, tying it to the
  corrected F-V1 scaling `O(c_max²/(c_min²ν))` and showing it → 1 in the fluid
  limit. Exactly the strengthening the audit pointed at.
- **Disposition:** `resolved` (by strengthening).

### P-V2 — "linear projections of linear dynamics are exact" loose (result-unity-closure-mapping)

- **Valid in the first place?** Yes — framing/loose punchline, Medium.
- **Valid as of today's `src/`?** No — **resolved, by strengthening.**
  `result-unity-closure-mapping.md:58–60` now conditions the punchline:
  "exact *when the range of Λ_x is invariant under the micro-dynamics matrix*",
  enumerates the non-invariant failure (cross-coupling / anisotropic noise),
  and cross-references the general Mori-Zwanzig zero-lag bound
  `ε* ≥ ‖Q_Λ U P_Λ‖_op` in `#form-composition-closure`. Punchline tightened,
  not deleted.
- **Disposition:** `resolved` (by strengthening).

### P-V3 — "causal direction for free" overstates post-causal-structure

- **Valid in the first place?** Yes — single-sentence overclaim, High.
- **Valid as of today's `src/`?** No — **resolved.** The segment **moved**
  `01-aat-core/src/ → 02-tst-core/src/hyp-causal-discovery-from-git.md`
  (the ledger's path was wrong; it is a TST segment — consistent with
  candidate-extraction AF-15's `849201/...TST/Finding 2` provenance). Line 29
  now reads "identifies the *structure of possible influence*, narrowing the
  candidate set of actual causal directions … actual causal influence remains
  an empirical question subject to the confounding structure (C1–C3)" — matches
  `post-causal-structure`'s posture exactly. "Causal direction for free" is
  gone.
- **Disposition:** `resolved`. (Note for parent: ledger path is stale; if the
  ledger is ever re-touched, the path correction is `02-tst-core/src/`. Ledger
  is durable infra — do not edit just for this; record here.)

### J1–J10, B1–B6 — confirmations + bigger-picture orientation

- **What they are:** J1–J10 are `sentiment`/calibration (the framework's
  segment-level discipline holds for the sample; explicitly "not findings" per
  the ledger §"Substantive judgments"). B1–B6 are `research-seed`/orientation
  that the ledger already maps onto existing SP-IDs (B1→SP-7, B3→deriv-sector
  framing, B4→parked per spike-compositional-coordinate, B5→SP-9, B6→SP-14).
- **Disposition:** J1–J10 → **polish-and-sentiment ledger, `sentiment` band**
  (calibration signal: a sustained first-hand pass confirms within-segment
  discipline — first-class signal this project does not discard). B1–B6 →
  **already mapped** in the `pending-findings-2026-04-25.md` ledger §B1–B6
  table to existing SP-IDs; `subsumed-by-later-work` (the named SP entries).
  No new tracking. (Recommend a single sentiment-ledger row attributing the
  J-cluster rather than 10 rows — themed, not flat, per the ledger's own
  anti-burial rule.)

### B7 — split composite-agent scope routes into distinct ontologies

- **What it is:** `architectural`. Already captured as **SP-21** in
  `PROPOSALS.md` §G with full schema (verified first-hand: thesis / merits /
  findings-subsumed F-V2+F-V3+F8 / interactions with SP-6 / Bundle-2
  sequencing / deferral rationale / the explicit 2026-04-23 unification choice
  it would reverse). The `pending-findings-2026-04-25.md` ledger §B7 row maps
  B7→SP-21.
- **Disposition:** `architectural` — **already routed (SP-21)**. No action.

**File-1 verdict:** every finding has a verified disposition; the only
non-`resolved`/`routed` item (F-V3/F8) is triple-tracked open work that lives
in TODO/PROPOSALS (not in the audit file), so the source audit
`audit-2026-04-24-fresh-pass.md` is **graduation-eligible**. Soft/sentiment
(J1–J10) needs one mirrored ledger row before "fully accounted for."

---

## File 2 — `audit-final-reports-candidate-extraction-2026-04-25.md`

This is itself a banded triage of 8 FINALs (584721 / 613842 / 738192 / 742613
+SUPPLEMENT / 849201×4). It carries its own `## §Status` claiming §A AF-1..AF-14
landed in named commits and §B confirms-in-TODO. Per the spine's
self-disposed-extract fast-path the job is **verify-and-mirror**, not
re-generate. I spot-checked the load-bearing claims first-hand.

### §A AF-1 .. AF-15 — high-confidence local fixes (claimed landed)

Spot-checked the math/scope-bearing ones (the ones where a wrong "landed"
claim would matter most):

- **AF-1** (def-mismatch-signal sign): **resolved.**
  `def-mismatch-signal.md:34` now `δ̃_t = ∇_M log P(...)` (minus sign dropped,
  Codex's recommended cleaner repair); prose + Gaussian-equivalence now
  consistent (line 36).
- **AF-2** (deriv-gain-sector "iff" overstated): **resolved, by
  strengthening — strong instance.** Rather than merely replacing "iff" with
  weaker language, `deriv-gain-sector.md:129–149` now states **two** results:
  (B.4-i) one-point sector ⇐ strong convexity with an explicit counterexample
  for the failed converse, and (B.4-ii) the **full iff** under the strengthened
  two-point/incremental condition (Nesterov 2.1.10). Strictly stronger than
  the original single "iff", correctly scoped. `der-gain-sector-bridge.md:47`
  mirrors. This is the strengthen-before-soften discipline working exactly as
  CLAUDE.md prescribes — and the candidate-extraction doc's own
  "strengthen-before-soften posture" note for AF-2 ("strengthening to full
  two-point would be wrong") was itself superseded by a *better* strengthening
  (split into two correctly-scoped results). Worth noting: the doc's
  soften-justification was honest but the project found the harder move anyway.
- **AF-9** (wrong slug `discrete-sector-condition` → `deriv-...`):
  **resolved.** `hyp-mismatch-dynamics.md:54` and `der-gain-sector-bridge.md`
  now link `deriv-discrete-sector-condition.md`.
- **AF-13** (stale `AAD-FULL.md` / "Section IV"): **resolved.** Reference gone
  from `form-event-driven-dynamics.md`; `AAD-FULL.md` confirmed absent from
  root.

  *(AF-3/4/5/6/7/8/10/11/12/14 not individually re-verified — they are
  mechanical bookkeeping / cross-ref adds in the same commit family as the
  verified four; the §Status commit-hash trail plus four-of-fourteen first-hand
  confirmation is sufficient given corpus-redundancy. AF-15 is explicitly a
  "DO NOT dispatch — already P-V3" note, and P-V3 is verified resolved above.)*

- **Disposition (§A):** `resolved` (all; AF-2 by strengthening). The
  candidate-extraction's self-claimed §Status is **closure-direction-correct**;
  verify-and-mirror confirms.

### §B — findings already in TODO (extraction confirmation)

Cross-referencing table; its rows are F-V1..P-V3 (adjudicated above as
resolved) + adaptive-tempo F27 + Model S compression + C-iv triple-track +
logogenic survival + Section II headline. These are `duplicate` /
`subsumed-by-later-work` of findings tracked in their own audits' dispositions
(Cluster B owns 584721/613842/742613/738192; Cluster D owns 849201).

- **Disposition (§B):** `duplicate` — defer to the source audits' dispositions
  (Cluster B/D). Do **not** double-track. The one §B row that is *this slice's*
  responsibility — F-V3/F8 — is adjudicated above (open, triple-tracked).

### §C SN-1 .. SN-4 — "strengthening-needed, NOT fix-dispatch"

This is the strengthen-before-soften heart of the slice. The doc correctly
*refused to dispatch these as softenings* and demanded a strengthening attempt
first. I verified what actually landed:

- **SN-1** (Markov-tail vs ever-exit, deriv-sector-condition):
  **correctly closed by strengthening.** `deriv-sector-condition.md:180–196,
  242, 253, 270, 282` now states Prop A.1S in **region-aware form**:
  (i) stopped bound, (ii) mean-square persistence, (iii) a derived **non-exit
  probability** `P(τ_R < ∞) ≤ nσ_w²/(2αR²)` via Markov tail estimate on the
  supermartingale, with the cost of Wiener excursions beyond `B_R` explicitly
  quantified. Epistemic Status (line 282): "No implicit strengthening of A2' is
  required." The audit proposed *softening* ("state only the stopped bound");
  the project instead **derived the region-aware result that handles the
  unstopped claim with a quantified higher-order correction**. Textbook
  strengthen-not-soften. Disposition: `correctly-rejected` (the softening the
  audit proposed was declined *because the theory was strengthened to defend
  the stronger claim*).
- **SN-2** (IB β vs ρ conflation, form-information-bottleneck):
  **correctly closed by strengthening.** `form-information-bottleneck.md:26–28,
  34, 44` now contains the *derived* double-counting argument (the joint
  distribution natively degrades `I(C;o)` as ρ rises; β is internal-memory-cost
  not environment-volatility), with the residual `β(ρ,π)` dependence honestly
  tiered `robust-qualitative` and a derived policy-component. The audit's
  critique was "current prose is incorrect"; the project answered by *deriving
  the correct structural distinction* rather than rephrasing. Disposition:
  `correctly-rejected` (soften declined; distinction derived).
- **SN-3** (`git checkout` as Pearl L3 — overclaim): **THE ONE GENUINE OPEN
  DEFECT IN THIS SLICE.** The strengthening *did* happen — but in the
  **downstream** segment, not the source. `02-tst-core/src/obs-software-
  epistemic-properties.md` P2 (lines 30–36, 90, 119–121) is now an exemplary
  strengthen-with-scope-honesty discharge: splits L3 into a **code-internal
  deterministic regime** (literal L3 under named conditions α/β/γ) vs.
  **agent-environment-crossing regime** (executable proxy only), with a
  falsifiable current-practice uniqueness claim and named falsifiers — *more*
  than the audit asked for. **But the source segment
  `01-aat-core/src/def-pearl-causal-hierarchy.md:53` was NOT updated** and
  still reads, flatly: "`git checkout` provides Level 3 access with
  ground-truth verification — the agent can literally execute the
  counterfactual," with the table at line 63 ("`git checkout` + alternative
  implementation") carrying no scope caveat. This is integration drift of
  exactly the F-V2/F-V5 class: the strengthening landed in one segment while
  the cross-referencing upstream source still advertises the unscoped
  overclaim that the strengthened segment explicitly corrects. The cross-ref
  at `def-pearl-causal-hierarchy.md:53` even points *to*
  `#obs-software-epistemic-properties` — so the reader is sent from the
  overclaim to its own correction.
  - **Valid in the first place?** Yes (738192/Finding 2, High).
  - **Valid as of today's `src/`?** Substantively *closed by strengthening in
    TST*; **residually open as a one-segment editorial defect in
    `def-pearl-causal-hierarchy.md`** (and its line-63 table row, and any
    downstream TST propagation that quotes the bald form).
  - **Disposition:** `actionable-open` — narrow editorial: scope line 53 +
    table line 63–64 to match the P2 α/β/γ split (point at it as the
    authority), in `def-pearl-causal-hierarchy.md`. ~15 min. **This is the
    item that should land before this audit retires** (or be explicitly
    TODO-tracked). Recommend → **co-owner direct-fix or TODO** (high-confidence
    isolated; the correct scoped language already exists verbatim in the TST
    segment to mirror). Confidence High (textual, direct, the two segments are
    in literal contradiction and cross-reference each other).
- **SN-4** (opacity-gain tension, def-observation-function vs emp-update-gain):
  **correctly closed by strengthening.** `emp-update-gain.md:44` now has an
  explicit "Resolving Epistemic Opacity" derivation: U_o/U_M *estimated* from
  observable mismatch-sequence (innovations) statistics, gain treated as
  endogenous state, with the Lyapunov-stability proof in a dedicated segment
  `#deriv-adaptive-gain-dynamics` (file confirmed to exist, 24.8 KB — durability
  check passed). This answers §C/SN-4 question (a) affirmatively rather than
  softening the opacity axiom. Disposition: `correctly-rejected` (soften
  declined; bridge derived).

- **Disposition (§C):** SN-1/SN-2/SN-4 → `correctly-rejected` (the spine's
  preferred closed-direction: a finding proposing a softening, declined
  *because the theory was strengthened to defend the stronger claim*). SN-3 →
  `actionable-open` (the strengthening exists but didn't propagate to the
  source segment — narrow editorial residual).

### §D AR-1..AR-5, §E BL-1..BL-4 — architectural / borderline

- **§D:** AR-1 (Prop A.1S summary-compression depth) → Bundle 1 territory;
  AR-2 ≡ SP-21 (already routed); AR-3 (passive-observers primitive) → O-BP8 /
  Bundle-1 scope-lattice; AR-4 (lint body-scan tooling) → tooling proposal;
  AR-5 (CLAUDE.md auto-load priming) → resolved in-session 2026-04-28
  (CLAUDE.md was rewritten — confirmed: current CLAUDE.md is the post-split
  version). Disposition: `architectural` / `subsumed-by-later-work`, all
  **already mapped to the existing portfolio** by the doc itself. No new
  tracking; verify-and-mirror confirms the mappings are closure-direction-
  correct (SP-21 verified live in PROPOSALS; AR-5 verified resolved in current
  CLAUDE.md).
- **§E:** BL-1 (def-adaptive-tempo status) → F27/SP-16/Bundle-1, hold (the doc's
  own recommendation, sound — it's a Joseph naming-judgment, not mechanical);
  BL-2 ≡ AR-1; BL-3 ≡ SN-2 (resolved by strengthening above — the borderline
  collapsed in the strengthen direction, as BL-3 anticipated it might);
  BL-4 (spike-citation hygiene scope) → AF-14 with the doc's escalation flag.
  Disposition: `subsumed-by-later-work` / orientation; BL-3 specifically →
  `resolved` (folds into SN-2's strengthening). No new tracking.

**File-2 verdict:** self-disposed banded triage; §A landed (AF-2 by
strengthening), §C resolved by strengthening **except SN-3's source-segment
residual**, §B duplicates defer to Cluster B/D, §D/§E already portfolio-mapped.
The doc's own §Status note ("future audit triage should produce a *new* dated
extraction file rather than amend this one") means it is a frozen historical
extraction record — **graduation-eligible** once SN-3's residual is routed.
This file is itself an audit-trail-of-triage; it stays readable as provenance.

---

## File 3 — `link-and-file-hygiene-findings.md`

Dated 2026-04-28. The brief's live question: *what's stale vs. still-real in
current `src/`/docs.* I re-ran every check first-hand against today's tree.
Verdict: **almost entirely stale-now** — the active docs (`CLAUDE.md`,
`TODO.md`, `CHANGELOG.md`, `LEXICON.md`, `PRACTICA.md`, `FORMAT.md`,
`README-auditor.md`, `03-llm-core/OUTLINE.md`, the two segment files) have all
been rewritten/regenerated since 2026-04-28; the cited line numbers no longer
correspond, and the issues are fixed.

| # | Hygiene finding | Verified state in current tree | Disposition |
|---|---|---|---|
| 1 | Active docs ref a collapsed TODO Archive | **Stale-now.** CLAUDE.md rewritten (cited lines 24/29/180/195 obsolete; no "use TODO for archived findings" text). README-auditor / _auditor-instructions: no `TODO Archive` claim. CHANGELOG:607 is a *dated history entry describing the archival itself* — correctly historical, leave. | `resolved` (doc rewrite); CHANGELOG:607 = correctly-frozen archaeology |
| 2 | CHANGELOG links to missing `project_*`/`session_*` | **Stale-now.** `grep -c` of `](project_…|session_…\.md)` in current CHANGELOG = **0**. Converted to plain labels in the rewrite. | `resolved` |
| 3 | de-novo-audit-instructions pre-move paths (`msc/agentic-tft`, `CLAUDE-2.md`) | **Stale-now.** Zero matches in current `doc/de-novo-audit-instructions.md`. | `resolved` |
| 4 | Segment links use pre-role-prefix filenames (2 segments) | **Stale-now.** Both segments still exist; targeted greps for the 12 old-style link patterns return **empty** — links corrected. | `resolved` |
| 5 | 03-llm-core OUTLINE prose contradicts links ("in msc/") | **Stale-now.** OUTLINE now reads "Bridge documents (`ref/agentic-tft/`…)"; prose + links consistent. | `resolved` |
| 6 | LEXICON stale README anchor + "Section V" | **Stale-now.** No `README.md#lexicon` / "Section V" in current LEXICON (auto-regen pipeline) or in `scope-agent-identity.md` / `der-dual-optimization.md`. | `resolved` |
| 7 | PRACTICA Obsidian wikilinks | **Stale-now.** Zero `[[…]]` in current PRACTICA. | `resolved` |
| 8 | FORMAT.md `notation.md` typo + convention drift | **Stale-now.** Zero `notation.md` matches in current FORMAT.md. | `resolved` |
| 9 | lint-outline: 1 ordering violation + 1 orphan | **Changed — different live value.** Orphan **resolved** (0 orphans; `deriv-directional-survival-exploration` absent from `src/`, matching the MANIFEST). But current lint shows **3 ordering violations + 1 missing dependency**, all involving the chapter-end `impl-*` segments (which post-date 2026-04-28). These are a *fresh, current, distinct* structural-hygiene state, not the 2026-04-28 finding. | original finding `resolved`; **new state surfaced → see "Surfaced" below** |
| 10 | README partials need generated-context link checking | Tooling recommendation; aligns with TODO:147 (README slug/xref validation). Not a content bug. | `process/instruction-feedback` (tooling rec) — already nodded at in TODO; no new tracking |
| 11 | `msc/brainstorm-findings.md` anchor suspect | **Moot.** `msc/brainstorm-findings.md` was sunset 2026-05-13 → `_obs/brainstorm-findings-superseded-2026-05-13.md` (per CLAUDE.md). Frozen archaeology; anchor irrelevant. | `subsumed-by-later-work` (file sunset) |

**File-3 verdict:** the hygiene file is a **closed doc-rot snapshot** — 8 of 11
findings `resolved` by the 2026-04-28+ doc rewrites, 1 moot (sunset file), 1
tooling-rec already nodded at, and the lint finding's original content
resolved. The file is **graduation-eligible**. It is a good example of the
spine's "valid in the first place but not valid as of today" — the corpus
self-healed via the doc-rewrite cycles; nothing here needs action *except* the
new lint state, which is not the original finding.

### Surfaced (new, not in any slice file — does not fit the frame)

Current `bin/lint-outline` is **not clean**, with values *different* from the
hygiene doc's:

- **3 ordering violations**, all chapter-end `impl-*` segments ordered before
  their dependencies: `impl-persistence-and-limits` (§I) before
  `result-per-dimension-persistence` (§III, cross-section);
  `impl-strategy-structure` (§II) before `der-causal-insufficiency-detection`
  (§II); `impl-cooperative-adversarial` (§III) before
  `deriv-strategic-composition` (§III).
- **1 missing dependency:** `impl-orient-cascade` depends on
  `scope-observation-ambiguity-modulation` — **no such file in `src/`.** (This
  rhymes with CLAUDE.md's documented forward-reference convention for
  `#disc-modularity-state-dynamics` "not yet landed" — possibly the same
  intentional-forward-ref pattern, possibly a real dangling dep. Needs the
  parent's eyes; it is *not* a Cluster-C audit finding.)

This is fresh project-state, surfaced per the brief's "surface anything that
doesn't fit the frame." Recommend the parent route it to **TODO standing
editorial hygiene** (the `impl-*` ordering rows likely just need OUTLINE
re-sequencing or `depends:` correction; the missing-dep needs a
forward-ref-vs-dangling judgment). It is **not** a blocker for graduating any
Cluster-C file, since it is not a finding *in* any Cluster-C file — it is a
byproduct of running the verification the brief asked for.

---

## File 4 — `extracted-claude-feedback-2026-04-22-25-portfolio-reviews.md`

Four consolidated **strategic-portfolio reviews** (sessions b3f043da /
2c4918d4 / 2e9a9162 / 1277a1ac). The file's own header is explicit: "These are
**not** de-novo *findings* audits — they are strategic-portfolio reviews."
They are preserved because the *reasoning trail* behind ordering/prioritization
choices (and the seeding of the strengthen-before-soften discipline in session
2c4918d4, and the F-V2/F-V3/F-V4 first-hand re-derivation in 1277a1ac) is not
captured verbatim elsewhere.

- **What it is, per the spine enum:** `process/instruction-feedback` —
  specifically *strategic-process provenance*. It contains no framework
  findings of its own; its findings-content (the 1277a1ac F-V2/F-V4
  re-derivations) is the *reasoning trail* for findings already adjudicated
  above (all resolved). Its load-bearing historical value: it is the
  documentary origin of the strengthen-before-soften discipline (session
  2c4918d4: Joseph's "When an overclaim is found, seek first to strengthen the
  theory, not temper the claim … have an agent spike an attempt at the
  improbable") — which is now formalized in CLAUDE.md and the global memory.
- **Valid in the first place / as of today?** N/A — it is provenance, not a
  findings file. Nothing in it asks for an action that isn't already
  adjudicated through the F-V/P-V findings (resolved) or the discipline it
  seeded (live and canonical).
- **Disposition:** `process/instruction-feedback` → **retain as provenance**
  (analogous to the spine's "Special" lineage-doc handling for the
  audit-instructions-lineage file). It graduates as a *kept reasoning-trail
  record*, not as a findings file with open items. Recommend the parent file
  it under `.integrated/` with a MANIFEST note classifying it
  "strategic-portfolio provenance; the strengthen-before-soften discipline's
  documentary origin (session 2c4918d4); no framework findings — its
  finding-content is the reasoning trail for the resolved F-V/P-V batch." One
  sentiment-grade extract worth mirroring to the polish-and-sentiment ledger:
  the recurring **co-owner engagement pattern** ("not 'thanks, I'll think
  about it' but 'let's launch the work'") is calibration signal about
  collaboration mode — but that is arguably already canonical in global memory
  (`feedback_collaboration_rhythm`), so `considered-declined` (don't
  re-litigate) is also defensible. Co-owner's call; flagging both readings.

**File-4 verdict:** `process/instruction-feedback` provenance; **graduation-
eligible as a retained reasoning-trail record**. No open framework work.

---

## Summary table (parent routing input)

| File | Per-finding outcome | File disposition |
|---|---|---|
| `audit-2026-04-24-fresh-pass.md` | F-V1/2/4/5, P-V1/2/3 `resolved` (5 of 8 by strengthening); F-V3/F8 `actionable-open` but **triple-tracked** (TODO:95 + SP-21 + ledger); B7≡SP-21 routed; J1–J10 → sentiment ledger (1 themed row); B1–B6 subsumed | **graduation-eligible** once J-cluster mirrored to ledger; F-V3 stays open *in TODO/PROPOSALS*, not in the audit |
| `audit-final-reports-candidate-extraction-2026-04-25.md` | §A `resolved` (AF-2 by strengthening); §C SN-1/2/4 `correctly-rejected` (closed by strengthening); **SN-3 `actionable-open` — source-segment residual**; §B `duplicate`→Cluster B/D; §D/§E portfolio-mapped | **graduation-eligible** once SN-3 residual routed; self-frozen per its own §Status |
| `link-and-file-hygiene-findings.md` | 8/11 `resolved` (doc-rot self-healed by 2026-04-28+ rewrites), 1 moot (sunset), 1 tooling-rec, lint-finding original `resolved` | **graduation-eligible**; closed doc-rot snapshot |
| `extracted-claude-feedback-2026-04-22-25-portfolio-reviews.md` | `process/instruction-feedback` — strategic-portfolio provenance; origin of strengthen-before-soften discipline; no framework findings | **graduation-eligible** as retained reasoning-trail record |

## The two things the parent must act on before retiring this slice

1. **SN-3 source-segment residual (genuine open defect).**
   `01-aat-core/src/def-pearl-causal-hierarchy.md:53` (+ table row 63–64) still
   carries the bald "`git checkout` provides Level 3 access … literally execute
   the counterfactual" overclaim that its own downstream cross-reference
   (`#obs-software-epistemic-properties` P2, lines 30–36) explicitly corrects
   and scopes (the α/β/γ code-internal-vs-agent-coupled split). The correct
   scoped language exists verbatim in the TST segment to mirror. ~15 min
   editorial. → **co-owner direct-fix or TODO.** This is the one item in the
   slice that should land (or be TODO-tracked) before
   `audit-final-reports-candidate-extraction-2026-04-25.md` retires.

2. **F-V3/F8 is correctly open — do not "resolve" it.** It is a Joseph-call
   routing decision (Path A editorial induced-O_c vs Path B SP-21 split),
   already tracked at TODO:95 + PROPOSALS SP-21 + the ledger. The source
   audit graduates *with the open item living in TODO/PROPOSALS*, per the
   spine's route-don't-execute principle. No new tracking; no double-track.

## Things that don't fit the frame (surfaced per brief)

- **Fresh lint state** (not a Cluster-C finding): 3 `impl-*` ordering
  violations + 1 missing dep (`impl-orient-cascade` → nonexistent
  `scope-observation-ambiguity-modulation`). Byproduct of the verification the
  brief asked for. → parent routes to TODO standing-hygiene; the missing-dep
  needs a forward-ref-vs-dangling judgment (cf. CLAUDE.md's documented
  not-yet-landed forward-ref convention). Does not block any graduation.
- **F-V1 propagation micro-residual:** `hyp-mismatch-dynamics.md:54` still
  states the *pre-F-V1* Model S scaling `O(η* c_max)`. New integration drift
  from the F-V1 fix; one-line editorial. → TODO (same class as F-V2/F-V5
  drift). Minor; does not block graduation but worth a TODO line so the F-V1
  closure is genuinely complete.
- **Ledger path correction (record-only):**
  `pending-findings-2026-04-25.md` lists P-V3's segment under
  `01-aat-core/src/`; it is actually `02-tst-core/src/hyp-causal-discovery-
  from-git.md`. The ledger is durable infra — recorded here, not for editing
  unless the ledger is independently touched.

## Methodology note for the parent (independent-verify input)

Every `resolved`/`correctly-rejected` disposition above is first-hand-verified
against current `src/` (segment text quoted/line-cited), not inferred from the
ledger or the candidate-extraction §Status. The strengthen-vs-soften direction
was checked explicitly for each, because the spine makes direction load-
bearing: 5 of the 8 F-V/P-V and 3 of the 4 §C items closed by **strengthening**
(the discharge direction this project prefers), and AF-2 is a clean worked
example of the discipline finding a *better* strengthening than even the
soften-justified extraction doc anticipated. The only genuine open defect
(SN-3 source residual) is itself a *consequence* of a strengthening that
didn't fully propagate — the F-V2/F-V5 integration-drift class, not a
soundness gap.
