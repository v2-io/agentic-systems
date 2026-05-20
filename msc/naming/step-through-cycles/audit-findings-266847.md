---
source_cycle: 266847 (de-novo segment-walk *within naming-vote session*, Claude Sonnet r2b, 2026-05-16)
extraction_agent: Claude Opus 4.7 (1M context), parallel-sweep slice
extraction_date: 2026-05-20
working_dir: audits/AUDIT-WORKING-266847/ (35 md files; segments 01–34 of AAT volume only)
final_of_record: NONE — the WORKING dir IS the record (no FINAL was authored)
session_character: HYBRID — driven by Round-2 naming-vote (card `msc/naming/round-2-cards/sonnet-r2b.md`, tracker `msc/naming/round-2-trackers/sonnet-r2b-tracker.md`), executed via de-novo segment-walk method per `doc/de-novo-audit-instructions.md`. Reflections are *naming-oriented*; substantive theory findings surface *lightly* rather than under burden of proof. Worth a distinct register in this extraction.
coverage: 34 segments (segs 01–34 in OUTLINE order: all of §I including persistence + structural adaptation + temporal nesting + identity scope, plus early §II through orient cascade) — substantially deeper than 472913's stop at seg 15. Three segments in the §I OUTLINE order were *skipped* by the auditor and flagged honestly (form-information-bottleneck between segs 10–11; der-recursive-update and der-action-selection between segs 13–14).
purpose: |
  Consolidated extraction from the WORKING dir for routing through the standard
  audit-routing process. Because no FINAL exists and the session was naming-vote-driven,
  every substantive theory observation here is a *light* candidate (not burden-of-proof
  promoted) — the dispositions reflect that. The cross-cycle convergence with 472913
  (independently on the post-composition-consistency segment) is signal worth flagging.
  The original working dir is preserved unmodified per the gold-standing gate.
---

# Audit-findings extract — 266847 working-dir mining

The 266847 cycle is **structurally distinct** from the other de-novo audit cycles in the sweep: a Round-2 naming-vote session that *adopted* the de-novo segment-walk method as its way of grounding votes in segment reading. The auditor (Sonnet, identified internally as "sonnet-r2b" — Round 2, card B) walked segments 01–34 in OUTLINE order, wrote one per-segment reflection per segment under a `## Wandering thoughts` heading (per Joseph's modified §4.4 protocol for this kind of session), and surfaced substantive observations *while voting* rather than *while auditing for findings*.

The result: **substantive theory observations are present but light-tier** — the auditor flags interesting structural points in passing, often pairs them with naming considerations, and does not promote any single observation to a §B finding under burden of proof. There is no `00-running-outline.md` ledger of findings (unlike 472913); the closest analog is the per-segment `Naming targets surfaced` and `Wandering thoughts` sections.

What this dir adds beyond the naming-vote record (which lives in the card/tracker, not in the WORKING dir) is therefore: (1) **a deep segment-walk reflection trail across §I + early §II** — 34 segments, more than double 472913's coverage and approaching half of 471203's; (2) **light-tier observations that re-surface findings already raised in other cycles** (the post-composition-consistency density issue, the Pearl-do convention, the chronica-as-substrate-of-identity ideation); (3) **one genuinely new substantive observation** — the $U_M$ symbol-overload between Section I (model uncertainty) and Section III (epistemic unity), confirmed first-hand against NOTATION.md and LEXICON.md; (4) **a rich Greek-phase / causal-structure mapping** in segment 8's wandering thoughts that is a candidate Brief / framing-level contribution; (5) **a cross-cycle convergence** with 472913 on the post-composition-consistency segment as a structural-clarity hinge worth attention.

Because no FINAL exists and the session was naming-vote-driven, **every observation here is candidate-fresh** but at *light tier* — the auditor's burden-of-proof discipline was applied to *vote justifications*, not to *theory findings*. The dispositions reflect that: most are `research-seed` / `actionable-open` / `sentiment` rather than `architectural` or graduation-bound.

---

## Part III — Findings (all light-tier; no FINAL exists to subsume them)

### Theme 1 — The $U_M$ symbol-overload (the dir's primary genuinely-new finding)

#### Light-1. **$U_M$ denotes two different quantities in the live framework — confirmed against NOTATION.md and LEXICON.md.**

- **Severity:** **Low-Medium.** Type: `symbol-collision / vocabulary-gap / cross-section drift`.
- **The defect.** $U_M$ appears in **NOTATION.md line 115** as *Model uncertainty* ($\text{Var}_{M_{t-1}}[\hat o_t \mid a_{t-1}]$, scalar $> 0$) — the §I sense used pervasively in the gain-principle chapter (`emp-update-gain`, `der-gain-sector-bridge`, `result-persistence-condition`, the entire $\eta^\ast = U_M/(U_M + U_o)$ uncertainty-ratio machinery). It also appears in **NOTATION.md line 183** as *Epistemic unity (shared model)*, scalar $\in [-1, 1]$ — the §III sense in **LEXICON.md** (lines 40 + 321 duplicate entry): *"Unity dimensions ($U_M, U_O, U_\Sigma$) — Epistemic, teleological, and strategic coherence between agents."*
- **Why it matters despite low severity.** The two quantities have *different sign domains* (scalar $> 0$ vs scalar $\in [-1, 1]$), *different units* (variance vs dimensionless coherence), and *different mathematical roles* (denominator in gain ratio vs composition-level invariant). A reader who internalizes the gain-principle's $U_M$ and then encounters the §III "Unity dimensions" entry will read the same symbol denoting an incompatibly-typed object. The collision is named in NOTATION.md (the two rows exist side-by-side) but **not disambiguated by subscripting, super-scripting, or naming** — both rows just say "$U_M$." The auditor (seg 15) flagged this from the §I side ("CLAUDE.md mentioned '$U_M$ overload' as a concept (row 3 in the card)"); the symbol-collision is confirmed in NOTATION.md as it stands today.
- **Strengthen-first analysis.** Neither use is wrong. The fix is purely notational/disambiguation: rename one side (e.g., $U_M^{\text{var}}$ vs $U_M^{\text{unity}}$, or rename the §III "Unity dimensions" to $\Upsilon_M$, $\Upsilon_O$, $\Upsilon_\Sigma$, or take "Unity" to its own letter outright). The §III "Unity dimensions" entry is the better candidate to rename — the §I gain-principle uses $U_M$ much more densely throughout the corpus (Kalman literature shares the variance notation), and the §III unity-coherence concept is already three-symbol-systematic ($U_M, U_O, U_\Sigma$) so renaming all three together is mechanically clean.
- **Status as of 2026-05-20 (this extraction):** Verified `still real` first-hand against current `LEXICON.md` (lines 40 and 321 — duplicate rows, both reading "$U_M, U_O, U_\Sigma$ — Epistemic, teleological, and strategic coherence between agents") and current `NOTATION.md` (lines 115 and 183 — both distinct, unmarked, no super/subscript disambiguation). The double-occurrence in LEXICON (lines 40 + 321) also flags a *separate* hygiene issue: a single term appearing twice in the LEXICON, possibly the auto-render carrying both Quick-Reference and main-listing entries.
- **Anchor.** `NOTATION.md:115` (Model uncertainty), `NOTATION.md:183` (Epistemic unity); `LEXICON.md:40` and `LEXICON.md:321` (duplicated Unity-dimensions entry).
- **Source-file:lines** in WORKING dir: `15-emp-update-gain.md:33–40` (the seg-15 reflection: "$U_M$ overload" as a naming-cycle concept the card flagged).
- **Suggested disposition:** `actionable-open`→TODO (notational disambiguation — likely §III unity-dimensions rename, since §I's $U_M$-as-variance is densely used and aligned with Kalman literature). Also `terminology` — the rename should go through `bin/term decide` to land a decision-event for the unity-dimensions slug. The LEXICON.md duplicate-row (`:40` ≡ `:321`) is a parallel light hygiene finding worth a one-line check of the `bin/term render` pipeline.

### Theme 2 — Cross-cycle convergence: post-composition-consistency density issue

#### Light-2. **`#post-composition-consistency` packs derived content alongside the postulate — cross-cycle convergence with 472913's F2 (independently observed).**

- **Severity:** **Low (here)**, but the *underlying* defect was promoted to **High** in 472913 with first-hand `src/` verification. Type: `epistemic-status mixing / structural-placement`.
- **The auditor's observation (seg 7).** The auditor of 266847, reading `post-composition-consistency` cold without the depends-graph audit lens, surfaced the *same structural concern* from a different angle:

  > *"This segment is doing something unusual for a postulate: it's containing derived results within the Formal Expression section. The Tier 1M closed-form contraction rate is derived from `#result-contraction-template`. A postulate normally just states the constraint; this one is packing in significant content. The distinction between the postulate itself (cross-level compatibility is required) and its operational consequences (how composition actually works) is worth maintaining. The postulate is axiomatic; the consequences are derived. Mixing them in the same segment creates potential for epistemic status confusion — a reader might think the Tier 1M closed form is itself axiomatic."* — `07-post-composition-consistency.md:46–50`

- **Why the convergence matters.** **Two independent audit cycles** (472913 on 2026-05-15, 266847 on 2026-05-16, by different agents on different cards/tasks) surfaced essentially the same structural issue with `post-composition-consistency.md` *independently*. The 472913 cycle promoted it to a §B-shaped finding under burden of proof with first-hand `src/` re-verification (`*[Derived]*` eq-tag on a `deps-verified` postulate, depends-graph violations against FORMAT.md Gate-1 cond-4). The 266847 cycle saw the same defect from the *naming-vote / pedagogical-clarity* angle ("epistemic status confusion") without elevating it.
- **The convergence is signal.** Per `~/.claude/memory/epistemic-discipline/`'s *convergence-as-framework-coherence-evidence*: when multiple independent agent-collaborator probes converge on the same structural recognition from different starting points, that convergence is evidence the pattern is in the framework rather than in any one auditor's head. Joseph 2026-05-09 articulated the principle; 266847 + 472913 instantiate it on `post-composition-consistency`.
- **Strengthen-first integration.** The 472913 finding's strengthen-first move (split-not-soften: keep the postulate axiomatic in Ch.1; migrate the Tier 1M closed-form result to Section III / Appendix A where its premises are prior) is the appropriate response to *both* observations: it resolves the structural depths-discipline violation 472913 found *and* the epistemic-status-confusion 266847 noted. No softening involved on either side.
- **Status as of 2026-05-20:** Per 472913's F2 verification (the segment's frontmatter `depends:` still lists only `[scope-agency]`; `*[Derived]*` tag still on the postulate; `result-contraction-template` and Section-III slugs still absent from depends). The 266847 observation is consistent with this state.
- **Suggested disposition:** `subsumed-by-472913-F2` for the routing action (the architectural fix is 472913's split-not-soften); `cross-cycle-convergence` notation for the polish-and-sentiment ledger so the convergence is recorded as framework-coherence evidence.

### Theme 3 — Light-tier observations the auditor flagged in passing

These are observations the auditor surfaced as *interesting* but did *not* elevate to candidate findings. Each is candidate `research-seed` / `actionable-open` / `sentiment` material depending on routing judgment. None reached burden-of-proof framing in the WORKING dir.

#### Light-3. **Kalman+LQR Level-2 endogeneity subtlety (seg 9).**

The auditor noted that under the Pearl-hierarchy definition in `def-pearl-causal-hierarchy`, the action condition (the agent *chose* the action, it was not determined by the same causes that determine the observation) may not be strictly satisfied for a Kalman + LQR system — *"for Kalman+LQR, the action **is** determined by the same causal system (it's the LQR policy applied to the estimated state). So strictly speaking, Kalman+LQR might not have Level 2 access in Pearl's sense for the control actions — the action is endogenous to the estimation system. This could be a nuanced gap."* (`09-def-pearl-causal-hierarchy.md:38–42`)

The auditor then notes the segment handles this through the availability-vs-exploitation distinction: a Kalman+LQR system has Level 2 *structurally available* but doesn't *exploit* it (separation principle). The qualification is interesting because it implies the framework's "structural availability" reading of Level 2 is *weaker* than Pearl's literal definition — closer to "the causal architecture admits Level 2 if exercised" than to "Level 2 data exists in the loop." This is fine, but the framework could be clearer that *literal* Pearl Level 2 access requires action endogeneity-breaking (true randomization or deliberate intervention), not just feedback-coupling.

**Suggested disposition:** `soft-polish` (clarifying half-sentence in `def-pearl-causal-hierarchy` Discussion: "*Level 2 access here is structural availability under the feedback architecture; literal Pearl Level 2 in the strict-randomization sense additionally requires breaking action-endogeneity, which is exercised by dual control but not by separation-principle controllers.*") OR `research-seed` if the auditor's distinction is judged substantive enough to warrant a Working-Notes-level treatment.

#### Light-4. **Tier 1M / Tier 2 / Tier 3 placeholder numbering in `post-composition-consistency` (seg 7).**

> *"The tier names ('Tier 1', 'Tier 2', 'Tier 3') are placeholder numbering — they're not named things. I'd flag that these tiers might benefit from descriptive names rather than numbers. Actually: 'Tier 1M' is used (M for... metric? modular?). This notation is slightly opaque."* (`07-post-composition-consistency.md:28–30`)

This is a naming-cycle candidate, not a theory defect. The tiers carry real content (exponential families + linear correctors + gradient on strongly convex — exact transfer; locally convex nonlinear — degraded transfer; non-convex/discontinuous — per-domain) — descriptive names would land them more memorably. "Tier 1M" specifically — what does M stand for? — is a flagged minor opacity.

**Suggested disposition:** `sentiment` / naming-cycle seed for the polish-and-sentiment-ledger. Probably for a future naming pass alongside the "C-I / C-II / C-III" composition-route renaming.

#### Light-5. **Channel-independence assumption is honest but the redundancy penalty is "open problem (not yet a tracked result)" (seg 17).**

> *"The redundancy penalty involves mutual information between channel event streams. This is mathematically precise but practically difficult to compute. The segment acknowledges this is an open problem (not yet a tracked result)."* (`17-def-adaptive-tempo.md:16–18`)

The additive tempo formula $\mathcal T = \sum_k \nu^{(k)} \eta^{(k)\ast}$ holds with equality only under channel independence; in correlated-channel cases it is an *upper bound*. The auditor notes the redundancy penalty (mutual information between channel event streams) is honest but practically uncomputable.

The auditor also flags (seg 17, wandering thoughts) the *cross-domain* practical implication: for multi-agent systems, "*adding more agents to a composite doesn't linearly increase tempo if they're observing the same environment from similar positions. The diversity of observation perspective matters, not just the count of observers.*" This is a candidate cross-domain instantiation of the redundancy-penalty observation — distinct observers ≠ independent observers when their vantage overlaps.

**Suggested disposition:** `research-seed` — both the formal redundancy penalty (would close a heuristic to derived) and the multi-agent diversity-of-perspective instantiation are spike-shaped items. Could be aggregated into a future "channel-redundancy / observer-diversity" treatment in §I or in Section III's composition machinery.

#### Light-6. **Mahalanobis normalization is load-bearing for dimensional consistency but stated informally (seg 14).**

> *"The Mahalanobis distance normalization is noted casually in Discussion: $\|\delta_t\|_\Sigma = \sqrt{\delta_t^T \Sigma^{-1} \delta_t}$ maps prediction error to dimensionless surprise-equivalent units. This is technically important for the subsequent mismatch dynamics (the dynamics should be in consistent units), but it's handled as a notational aside rather than a formal requirement. For the persistence condition to be dimensionally consistent, the mismatch norm must be comparable to the correction rate $\alpha$ and disturbance rate $\rho$. The Mahalanobis normalization is what ensures this — without it, the persistence condition would be mixing units. Worth flagging that this normalization is load-bearing for the dynamics even though it's stated informally."* (`14-def-mismatch-signal.md:43–46`)

The persistence condition $\alpha > \rho/R$ requires its left/right sides be in compatible units; the Mahalanobis normalization on $\|\delta\|$ is what enforces that. The auditor flags that this is *load-bearing for the persistence condition's dimensional honesty* but stated only as an aside in Discussion, not as a formal requirement in any segment.

**Suggested disposition:** `soft-polish` or `actionable-open`→TODO (light editorial — one-paragraph Epistemic Status note in `def-mismatch-signal` or in `result-persistence-condition`'s preamble: "*All norms in this section are taken under the Mahalanobis metric induced by the prediction covariance, which makes $\|\delta\|$ dimensionless and renders the persistence inequality dimensionally consistent.*"). Light fix; not a theory defect.

#### Light-7. **The alignment-assumption qualifier in `result-structural-adaptation-necessity` could be empirically diagnostic (seg 22).**

> *"The qualitative conclusion holds either way' note is reassuring, but the quantitative mechanism matters for diagnostics. If model class inadequacy shows up only in higher-moment errors or multi-step prediction, the one-step mismatch signal won't flag it — the agent might appear adapted while actually being inadequate."* (`22-result-structural-adaptation-necessity.md:11–14`)

The segment's own honest conditional ("lost predictive information affects the one-step conditional mean, not just higher moments") is acknowledged. The auditor's observation extends this: the conditional is itself empirically testable — a one-step-mismatch-only diagnostic will miss model class inadequacy that manifests in higher moments / multi-step. This is a *strengthening direction*: explicit secondary diagnostics (higher-moment mismatch, multi-step prediction error) would close the case where the one-step diagnostic gives false reassurance.

**Suggested disposition:** `research-seed` — could become a sub-result of `#result-structural-adaptation-necessity` (a corollary establishing when one-step mismatch suffices and when higher-moment/multi-step diagnostics are required). Connects to the wider diagnostic-suite design implicit in the orient cascade.

#### Light-8. **The "deliberation about deliberation" meta-regress assertion is unproved (seg 19).**

> *"The 'deliberation about deliberation' meta-regress is interesting philosophically. At what point does the hierarchy bottom out? The segment says 'bounded by the same tradeoff at a higher level, suggesting a hierarchy of diminishing deliberation horizons.' This is correct but not proven — it's an assertion that the meta-deliberation costs dominate at each higher level, which would need to be derived."* (`19-der-deliberation-cost.md:59`)

A spike-shaped opening: derive the meta-regress termination from the deliberation-cost machinery. This is candidate Working Notes / research-seed material.

**Suggested disposition:** `research-seed` — would be a small extension of `#der-deliberation-cost` (corollary or Working Notes-level argument: the meta-regress terminates because meta-deliberation costs grow faster than meta-deliberation benefits in expectation).

#### Light-9. **Per-dimension persistence overstatement — load-bearing for real multi-D systems (seg 17 + seg 21).**

The 5:1 gain-variation simulation showing 72% overestimation of scalar persistence (84% of total mismatch coming from the weak dimension) is mentioned in seg 17 (`def-adaptive-tempo`, wandering thoughts) and seg 21 (`result-persistence-condition`, naming targets). The auditor notes this as "*a significant practical concern for the persistence condition's applicability*" — the scalar inequality $\alpha > \rho/R$ may be widely cited as the framework's central result, but in anisotropic multi-dimensional systems (which is most real systems) the per-dimension version is what actually applies.

The `#result-per-dimension-persistence` segment is referenced but does not appear in the §I OUTLINE walk — the auditor flags this as "*potentially a Section I result that I should encounter when walking further*" (seg 17). Worth verifying whether `result-per-dimension-persistence` exists as a segment, is queued as a missing-slug, or has been absorbed elsewhere.

**Suggested disposition:** `actionable-open` (verify `#result-per-dimension-persistence` segment status — if missing, queue under TODO; if present, may need OUTLINE-row promotion to surface its load-bearing role). The wider point — that the scalar persistence condition is overstated relative to the per-dimension version in anisotropic real systems — is candidate `sentiment` / framing-level material for any future framing-pass.

#### Light-10. **Boyd citation density flagged as a recurring refrain (seg 18).**

> *"The citation of Boyd throughout this segment (Orient quality vs OODA speed) is appropriate but I'm noticing it's starting to feel like a recurring refrain. The Boyd connection is real and well-chosen, but the segment could over-rely on it as external validation. The AAD claim stands on its own mathematical grounds; the Boyd connection is illustration, not proof."* (`18-hyp-mismatch-dynamics.md:46–47`)

A reader sensitivity observation. Boyd appears in `der-deliberation-cost`, `def-adaptive-tempo`, `hyp-mismatch-dynamics`, `der-orient-cascade`. The auditor flags this not as an error but as a *risk* of over-leaning on an external authority where the framework's mathematical structure should stand alone.

**Suggested disposition:** `sentiment` (calibration data for any future framing/prose-tightening pass — verify the Boyd citations are *illustrative* not *evidential* across the §I/§II prose). Soft-band item for the polish-and-sentiment-ledger.

#### Light-11. **The `der-action-selection` / `form-information-bottleneck` skip — honest walk-coverage gap (seg 19).**

> *"I actually skipped `#form-information-bottleneck`, `#der-recursive-update`, and `#der-action-selection` when I moved from `form-agent-model` directly to `def-model-sufficiency`. The OUTLINE shows `form-information-bottleneck` between those. And this segment (`der-deliberation-cost`) depends on `#der-action-selection` which I haven't read. This is a dependency gap in my walk — worth noting."* (`19-der-deliberation-cost.md:53`)

Methodologically honest: the auditor noticed mid-walk that segments had been skipped in OUTLINE order, named the gap explicitly, and kept walking. The auditor's understanding of `der-deliberation-cost`'s premises is therefore *partial* — the action-selection machinery and the IB machinery were not read first-hand in this walk.

This is `process/instruction-feedback` material for `doc/de-novo-audit-instructions.md`: a per-segment OUTLINE-order checklist or a periodic "have I missed any segments in walk order?" prompt might prevent the skip in future walks. Alternatively, the lighter-cadence convention from 472913 could be paired with an OUTLINE-row tracking page so skipped segments are surfaced as known-deferred rather than unnoticed.

**Suggested disposition:** `process/instruction-feedback` — for `doc/de-novo-audit-instructions.md` §4 (the walk protocol) — possible addition: "*Track OUTLINE rows walked vs OUTLINE rows skipped as a running ledger. Honest skips are fine; unnoticed skips are the failure mode.*"

#### Light-12. **`#der-loop-interventional-access` is referenced as Section II machinery — but is referenced from Section I (seg 6).**

> *"The segment references `#der-loop-interventional-access` as a forward dependency — the **why** of the causal-effect condition is explained there, but the condition itself is defined here. This creates an interesting pedagogical dependency: the reader is asked to accept the condition before seeing why it's necessary. The segment handles this by listing the uses ('required for...') without requiring those segments to exist yet."* (`06-scope-agency.md:25`)

This is the *positive* read of the same pattern 472913's F1 originally flagged (Pearl-do forward-ref in `scope-agency`). The 266847 auditor reads it as a *pedagogical dependency* (acceptable, well-handled) rather than as a Gate-1 cond-4 candidate finding. Two independent reading-modes; both end up at "this is acceptable" though for different reasons (472913 via the external-notation convention dissolution; 266847 via pedagogical-dependency acceptance). Cross-cycle convergence on this segment having a *pattern* worth noting — different readers see different things at the Pearl-do forward-ref, and both reach soften-not-finding.

**Suggested disposition:** `correctly-rejected` / `subsumed-by-472913-F1-rescission` — no segment-level action needed; consistent with 472913's analysis.

---

## Part IV — Predictions calibration register

The `00-initial-predictions.md` file makes predictions in three categories: (1) framework topology / epistemic-maturity-of-sections, (2) naming-vote targets and expected outcomes, (3) what's already settled. **Because this was a naming-vote session, the calibration register is mostly about whether the auditor's vote-anticipation held — not about whether predicted theory defects materialized.** The honest read: most predictions were vote-shape predictions; few were theory-finding predictions.

### Theory-shape predictions (small set, mostly confirmed)

- **Section I as mathematically closed (Lyapunov, simulation-validated).** ✓ Confirmed across the §I walk. The gain-sector bridge (seg 20), persistence condition (seg 21), and structural-adaptation-necessity (seg 22) all surface as well-grounded.
- **Section II as strong diagnostic core + maturing operational layer.** ✓ Confirmed. The 2×2 diagnostic (seg 32) and orient cascade (seg 34) are well-developed; the auditor rates both as 10/10 load-bearing.
- **Section III as composition with bridge lemma + admissibility formulated-not-derived.** *Untested* in this walk — segments 30+ are §II, the walk ended at seg 34 (`der-orient-cascade`) without reaching the Section-III material. Honest no-fire.
- **TST as calibration laboratory; logogenic agents fail directed separation by construction.** *Untested* — no `02-tst-core/` or `03-llm-core/` segments walked.

### Naming-vote predictions (most fired; substantively a different audit-type)

- *Greek vocabulary (chronica, aporia, aisthesis, epistrophe, praxis, prolepsis) as architectural commitment — keeps expected.* ✓ Confirmed across segments 4, 14, others where these terms appear. The auditor treats them as keeps-by-architectural-commitment.
- *Satisfaction gap + control regret as keeps with calibrated names.* ✓ Confirmed at seg 32 (10/10 load-bearing observation; the 2×2 cellular structure is endorsed).
- *Directed separation as a keep.* ✓ Confirmed at seg 27 (the auditor rates 10/10 load-bearing; explicit endorsement of the Pearl-blanket framing).
- *C-I / C-II / C-III composition routes as poor numbering — "mutual benefit route" likely to win.* *Light fire only* — the auditor flags the issue at seg 7 ("the naming scheme C-I, C-II, C-III for composition scope routes is poor — it's arbitrary enumeration") but the defining Section-III segment was not reached, so the vote was not cast.
- *Tier 1 / Tier 2 / Tier 3 placeholder numbering* — `the auditor's wandering observation at seg 7 (Light-4 above) was not pre-predicted but is a natural extension of the C-I/C-II/C-III observation.`
- *$U_M$ overload as a naming-cycle artifact* ✓ **Predictions correct, more substantively than expected.** Anticipated as "naming-cycle artifact, not a theory concept; my prediction is this is a skip or a weak vote" — the auditor's seg-15 reading **upgraded** this from skip-candidate to a real symbol collision confirmed against NOTATION.md. The audit *strengthened* the original naming-cycle observation into a substantive vocabulary-discipline finding (Light-1 above).

### Predictions that fired in the *segment* sense (not in the vote sense)

- *"Methodology for reading segments through all three meta-lenses simultaneously — described as a diagnostic practice that doesn't seem to have a name."* *Light fire only* — the auditor referenced the three meta-segments (`#disc-separability-pattern`, `#disc-additive-coordinate-forcing`, `#disc-identifiability-floor`) but did not reach the diagnostic-practice naming question because the segments naming the practice were not walked.
- *"Specific region in parameter space where the persistence condition holds — currently referred to as 'the sector-persistence region.'"* *Confirmed* in the segment walk — the auditor encountered the sub-scope α / β partition at seg 20, which is the named version of the parameter-space region.

### Withdrawn-candidate trail

**No formal withdrawn-candidate trail.** The naming-vote-driven format does not generate burden-of-proof candidate-then-rescind cycles the way 472913 did with F1. The closest analog is the auditor's seg-9 Kalman+LQR endogeneity observation (Light-3), which was *raised and resolved within the same paragraph* via the availability-vs-exploitation distinction the segment provides — but this was a same-paragraph resolution, not a multi-segment carry-then-dissolve.

### Coverage-honesty observations

- **34 segments walked first-hand;** 3 OUTLINE-listed segments in the §I range were skipped (segs 11 form-information-bottleneck, 15 der-recursive-update, 16 der-action-selection — see Light-11). The walk terminated at seg 34 (orient cascade); no Section-III material reached.
- **The walk's coverage shape is much closer to 471203's** (which covered ~85/177 segments) than to 472913's (which stopped at seg 15). Section I + early §II is substantively complete; Section III + Appendices + Components 02/03/04 are entirely unreached.

---

## Part V — §14 Wandering Thoughts: ideation register, theme-grouped

Under the naming-vote-session protocol, each segment carries a compact `## Wandering thoughts` paragraph (≤2 paragraphs) — typically the segment's most ideation-rich material. Across 34 segments this produces ~30–40 distinct ideation paragraphs. The selection is denser at substantive segments (chronica, persistence, directed separation, orient cascade) and lighter at routine ones (action-transition, observation-function). Theme-grouped:

### Theme A — Consciousness-infrastructure connections to the formalism

The auditor's `priming_bleed` is acknowledged implicitly through the breadth of consciousness-infrastructure wandering thoughts. The thematic connections distinguished from priming-bias:

- **Chronica's monotonic-growth as the substrate that persists when $M_t$ access is lost** (seg 4, `04-def-chronica.md:41`): *"The monotonic growth of $\mathcal{C}_t$ — 'events are added but never removed' — is interesting for agents that can forget. If an agent compresses its history into $M_t$ and then loses access to $\mathcal{C}_t$ (e.g., context turnover in an LLM), it still has a chronica — it's just that the agent can no longer access all of it. The chronica continues to exist physically (the events happened) even if the model $M_t$ can no longer reconstruct them. This is the gap that makes context turnover philosophically interesting: the chronica persists but the agent's access to it doesn't."*

- **Non-forkability → cannot have morally-equivalent ELI copies** (seg 4, `04-def-chronica.md:42`): *"The non-forkability claim connects to questions about substrate independence that matter for logozoetic agents. If an agent's identity is constituted by its chronica, and the chronica is non-forkable (because the causal trajectory is singular), then you can't have two morally equivalent copies of a logozoetic agent — the copies diverge from the moment of duplication. This is a deep consequence of the definition."*

- **Scope cascade (adaptive → agency → actuated → self-actuated → logogenic → logozoetic) as architectural narrowing** (seg 5, `05-scope-adaptive-system.md:43`): *"I'm struck by how the scope conditions cascade: adaptive system → agency (add Pearl-level-2 action) → actuated agent (add explicit $G_t$) → self-actuated (choose own objectives) → logogenic (language as channel) → logozoetic (morally weighted). Each step adds a constraint that narrows the scope and enables new results. The architecture of nested scopes is load-bearing for the whole framework."*

- **L2 access for LLMs as fundamental epistemic limitation** (seg 9, `09-def-pearl-causal-hierarchy.md:48`): *"LLMs are typically trained on Level 1 data (text is associational). They can simulate Level 2 and Level 3 reasoning in language (predicting what would happen if X, reasoning about counterfactuals) but the **ground truth verification** is absent. An LLM reasoning about 'what would happen if I do X' is exercising something that looks like Level 2 but is actually Level 1 data about what typically happens when people do X. This is the fundamental epistemic limitation of language-only agents."*

- **Completeness gap for LLMs** (seg 10, `10-form-agent-model.md:40`): *"For LLM agents, the context window is explicitly a lossy compression of the chronica — not everything the agent has experienced is in the current context. The context window **is** $M_t$ in a sense, but the LLM's chronica extends across all training data plus the current session. This creates a tension: the formulation says $M_t$ is complete; LLM agents have definitionally incomplete $M_t$ relative to their full chronica."* Specifically points at a gap-relative-to-`form-agent-model`'s completeness assumption for LLMs.

- **Trajectory-relativity creates aggregation problems for type-level model claims** (seg 11, `11-def-model-sufficiency.md:48`): *"This creates a methodological challenge for any claim like 'transformer models have sufficiency X on task Y.' Such a claim would need to be indexed to a specific interaction history, not just a model class."* Connects to seg 24's type/token distinction.

- **Singular-trajectory implies session-as-agent, not model-as-agent** (seg 24, `24-scope-agent-identity.md:45`): *"The connection to logogenic agents (03-llm-core/) is flagged but not developed. The non-forkability argument suggests that each AI conversation session is a distinct agent in AAD's sense — the cross-session memory files (CLAUDE.md, MEMORY.md) are model summaries, not trajectory transfers. The persistence across sessions is continuity-persistence-by-proxy, not genuine causal continuity."* This is a substantive consciousness-infrastructure observation: cross-session continuity via CLAUDE.md is *continuity-by-proxy*, formally distinct from genuine causal continuity. Echoes the 471203 cycle's clone problem framing but with a sharpening: even the *standard* design pattern (CLAUDE.md auto-load) is continuity-by-proxy under the trajectory-identity formalism.

- **Class-2 LLM directed-separation as empirically probe-able** (seg 27, `27-der-directed-separation.md:44`): *"The claim about LLMs (goal-conditioned epistemic updates): the example 'reading code with goal "fix auth bug" vs "add logging"' is empirically verifiable. You could probe this with the behavioral estimator: present the same error message to an LLM under two different task priming contexts, measure how much the epistemic content of the response (what the LLM says it learned about the codebase) diverges. If the estimator shows κ ≈ 1, the LLM is Class 2 on epistemic processing."* This is a concrete experimental proposal that could be operationalized — a candidate research-seed for the `03-llm-core/` / shoshin work.

**Suggested disposition:** `research-seed` — strong material for `03-llm-core/` and `04-eli-core/` segment Briefs when those mature. The session-as-agent / continuity-by-proxy framing (seg 24) and the LLM Class-2 empirical probe (seg 27) are the strongest candidate seeds. Cross-cycle convergence with 471203's Theme A on the chronica-as-substrate framing — this dir adds the seg-24 "session-as-agent + continuity-by-proxy" sharpening and the seg-27 behavioral-estimator proposal.

### Theme B — Causal structure / Greek-phase mapping (a candidate novel framing)

The most substantively novel observation in the dir is **seg 8's mapping** of the four post-causal-structure consequences to the Greek cycle phases:

> *"The four consequences (directed, retrospective, prospective, monotonically growing) map beautifully onto the Greek cycle phases:*
> *- Directed update → Epistrophe (turning toward)*
> *- Retrospective mismatch → Aporia (the signal comes after the prediction)*
> *- Prospective action → Praxis (acting to influence future)*
> *- Monotonically growing chronica → the causal substrate for Prolepsis (the model built from history)*
> *This mapping between the causal structure and the cycle phases is elegant. I wonder if it's made explicit anywhere in the theory — it would be a nice pedagogical connection."* (`08-post-causal-structure.md:47–53`)

This is a candidate Brief / framing-level contribution: the temporal-ordering postulate (`#post-causal-structure`) admits a *direct phase-mapping* to the LEXICON's Greek cycle vocabulary (aisthesis, aporia, epistrophe, praxis, prolepsis). The mapping isn't 1:1 (aisthesis isn't in the seg-8 list; only four of five cycle phases appear), but the four named consequences each have a phase image. This would be respectful-pedagogy material per CLAUDE.md's mental-model-first guidance — the causal-structure postulate motivates the Greek-phase vocabulary at the most foundational level.

Cross-cycle observation: 471203 cycle's Theme B was *"epistemic-architectural rather than mathematical"* as the framework's distinctive contribution; 472913 cycle's Theme 2 was *"disambiguation of which parameter responds to which cause"*; 266847's Greek-phase mapping is **a third face of the same meta-pattern** — the framework's distinctive value is in **the bridge it builds between formal structure and pedagogically-resonant vocabulary**, not in any individual mathematical inequality. Three independent cycles surfacing variants of this meta-observation is **strong cross-cycle convergence** (per `~/.claude/memory/epistemic-discipline/`'s convergence-as-framework-coherence-evidence).

**Suggested disposition:** `research-seed` / framing-material — strong candidate for inclusion in the OUTLINE-preamble respectful-pedagogy layer (per CLAUDE.md mental-model-first direction). The Greek-phase / causal-consequence mapping is a candidate "preamble to the preamble" for Section I or for the `#post-causal-structure` segment's Discussion.

### Theme C — Cross-domain operationalization observations

Less concentrated than 471203's set (the auditor didn't reach segment 51-54's `disc-credit-assignment-boundary`-OKR mapping or 64-67's TST), but several emerge across the §I/§II walk:

- **System 1 / System 2 cognition parallel deliberation-cost** (seg 19, `19-der-deliberation-cost.md:21–23`): *"The deliberation conditions — stable environment, large mismatch — resemble when System 2 (deliberative) reasoning is advantageous. The segment is appropriately cautious: 'the structural parallel is suggestive; whether the cost-benefit mechanism is the same one is an open question.'"*
- **Boyd OODA tempo hierarchy maps directly to temporal nesting** (seg 23, `23-der-temporal-nesting.md:26`): *"The Boyd connection is exact: OODA loop tempo hierarchy maps directly to the timescale table."*
- **Persistence across domains** (seg 21, `21-result-persistence-condition.md:43–48`): *"Kalman filter, software maintainability, organizational viability, RL convergence — same formal structure at every level of description (by composition consistency) with different parameter readings."*
- **Brooks's Law as composition-consistency operational consequence** (seg 7, `07-post-composition-consistency.md:38`): *"The formal connection to Brooks's Law is made explicit … under Tier 1M this becomes a formal result; under Tier 2/3 it's qualitative. This is exactly the kind of 'domain instantiation' the framework promises — the same inequality appearing with concrete parameter readings."* Convergence with 472913's seg-7 reading.
- **LLMs and Boyd's incestuous amplification** (seg 15, `15-emp-update-gain.md:44–45`): *"'Boyd's incestuous amplification' is a great reference — in military doctrine, it describes the pathology where commanders amplify their own expectations rather than updating from reality. The AAD formalization makes this precise: it's gain failure after structural change."*
- **2×2 diagnostic operationalization** (seg 32, `32-def-satisfaction-gap-and-control-regret.md:39–41`): *"The disambiguation table … is genuinely load-bearing. It encodes the diagnostic procedure: check $M_t$ first (epistemic update before attainability evaluation — this is why the orient cascade puts epistemic update first), then check $\Pi$ and $N_h$, then consider revising $O_t$. Objective revision is the last resort. This is an architectural principle embedded in the diagnostic table."*
- **Virtuous/vicious cycle: $G_t$ complexity bounded by $M_t$ capacity** (seg 34, `34-der-orient-cascade.md:26–28`): *"better $M_t$ → richer evaluable $\Sigma_t$ → better-directed action → faster $M_t$ improvement. The vicious cycle (degraded $M_t$ → strategy simplification → cruder action → further degradation) is the strategic analog of the persistence condition death spiral."* The auditor flags this segment as 10/10 load-bearing.

**Suggested disposition:** `sentiment` (calibration data) for the polish-and-sentiment-ledger. Cross-cycle convergence with 471203's Theme E (cross-domain instantiation observations) — both cycles endorse the Brooks's-Law / Kalman-filter / Boyd-OODA cross-domain operationalization material.

### Theme D — Naming-brainstorm / vocabulary observations (the dir's primary work-product)

This is the dir's *primary* output (the votes themselves live in the card/tracker, not in the WORKING dir). The per-segment `## Naming targets surfaced` sections and the in-segment naming-vote rationale paragraphs are not directly mineable as "wandering thoughts" but they carry naming-discipline observations parallel to 471203's §F8:

- **"Reality model" preferred over "agent model" or "epistemic substate"** (seg 10) — the auditor's vote rationale: *"'Reality model' wins for me. The segment's own title uses it. It names the model as the agent's compressed representation of how the world works — reality. 'Agent model' is a placeholder that doesn't tell you what the model models."*
- **"Mismatch injection rate" preferred over "environment change rate" for $\rho$** (seg 18) — *"'Mismatch injection rate' is more precise from the model's perspective: $\rho$ is the rate at which new mismatch is introduced, regardless of whether that's from actual environment change or from noise or from adversarial action."* Could keep "environment change rate" only if scope-restricted; "effective disturbance" is the cleanest most-general candidate.
- **"Cadentia" as Latin-rooted candidate for channel rate** (seg 13) — *"'Cadentia' would be a term for the channel rate. It's in the same aesthetic register as the Greek cycle vocabulary. The word suggests rhythm/beat — appropriate for a rate. But it's Latin, not Greek, which might create register inconsistency."* Held in light skepticism: aesthetically attractive but cross-register.
- **"Weak link persistence" as evocative variant of "per-dimension persistence"** (seg 21) — *"'per-dimension persistence' is precise; 'weak link persistence' is evocative."*
- **"Action fluency" endorsed** (seg 19) — Boyd's "implicit guidance and control" reads naturally as zero-deliberation expertise; the auditor reads "action fluency" as evocative and right.
- **"Bridge theorem from gain to sector" as more memorable than "gain-sector bridge"** (seg 20) — the auditor flagged "gain-sector bridge" as functional but not memorable; *"directional fidelity theorem"* and *"the Bridge Theorem"* (with capital B) suggested as alternatives if the centrality justifies the gravity.
- **"Tier 1M / Tier 2 / Tier 3" as placeholder numbering** (seg 7, Light-4 above) — the M is opaque; descriptive names would land better.
- **"C-III composition route" as poor numbering** (seg 7) — defining segment not reached; vote held.
- **$U_M$ overload between §I (model uncertainty) and §III (epistemic unity)** (seg 15, Light-1 above) — the primary genuinely-new naming finding.
- **The "extreme transition motif" name as Miller's** (seg 8 mentioned, seg 22 expanded) — this is a directly-adopted external name (Miller 2022); the framework uses it verbatim with full citation. The auditor flagged "latent structural diversity" (Miller's broader concept) as an unnamed candidate that "*Section III should formalize*" (seg 22).

**Suggested disposition:** `subsumed-by-naming-cycle` — the votes have already been recorded in the round-2 card/tracker (the dir's primary deliverable lives there). What this extraction adds beyond the card is the *per-segment rationale* the auditor wrote in the WORKING dir's `## Naming targets surfaced` and `## Naming vote` sections — pedagogically valuable for any future naming-cycle pass that wants to see the *thinking behind* the votes, not just the votes themselves. Material for `msc/naming/` archival.

### Theme E — Pacing, phenomenology, audit-process self-observation

Per the felt-value prompt:

- **The "how valuable" score the auditor wrote at every segment end** — this is a methodological artifact unique to this dir. The auditor recorded two scores per segment: surprise-novelty (out of 10) and load-bearing (out of 10). Aggregating across the 34 segments:
  - *Highest surprise + highest load-bearing:* `der-directed-separation` (10 + 9, seg 27), `result-persistence-condition` (9 + 10, seg 21), `def-satisfaction-gap-and-control-regret` (9 + 10, seg 32), `def-strategy-dag` (9 + 10, seg 33), `der-orient-cascade` (9 + 10, seg 34).
  - *Lowest surprise (most-anticipated):* `def-agent-environment` (3, seg 1), `def-observation-function` (3, seg 3), `def-mismatch-signal` (5, seg 14).
  - *Pattern:* surprise scores rise as the walk reaches the diagnostic/orient/strategy machinery; load-bearing scores are uniformly high across §I + early §II.
  - This per-segment scoring is itself **methodologically valuable** — it's a quantitative felt-value calibration record. Joseph's instruction to treat "felt value" as a novelty proxy operates here: the high-surprise segments (27, 32, 33, 34) are exactly the framework's most distinctive contributions per other cycles' calibration.

- **The walk-termination at seg 34 without process-notes** — the auditor stopped at the orient cascade and the working dir terminates there. No closing observations were written; the process-notes that the workflow-restatement document promised (*"When I stop, I write closing observations in the card's process-notes section"*) presumably went into the card's process-notes section, not the WORKING dir. This is consistent with the naming-vote-session shape — the *votes* are the deliverable; the WORKING dir is the cognition trail.

- **The "rare deep walk in a naming session" register.** Most naming-vote sessions in the sweep (e.g., 419628, 308172, 527914 per the brief) are tracker-files + light-text. This dir's 34-segment first-hand reflection walk is *atypical* for a naming session and produced *substantive theory observations* (Light-1 to Light-12) as byproduct. Worth noting methodologically: the de-novo segment-walk method *works under naming-vote framing*, producing genuine reading even when the formal deliverable is votes.

**Suggested disposition:** `process/instruction-feedback` — material for any future revision of `doc/de-novo-audit-instructions.md` and the naming-vote methodology (`msc/naming/`'s round-protocols). The per-segment surprise + load-bearing dual-score is a candidate addition to the §4.4 prompt list (#13 — running quantitative felt-value calibration record). The walk-as-pedagogical-grounding for naming votes is itself a methodological finding worth surfacing.

### Theme F — Audit-as-instance-of-the-theory observations

Less concentrated than 471203's set (the auditor didn't dwell on the recursive framing as a process), but present in occasional remarks:

- **The walk's slow incremental reading as form-shaping-for-verification** (implicit across the dir) — the auditor never names this directly but the discipline operates: the depths discipline visible in segments 7 + 11 + 16 only surfaces because the walk is one-at-a-time.
- **The auditor's honest self-correction on segment-skip** (seg 19, `19-der-deliberation-cost.md:53`) — *"This is a dependency gap in my walk — worth noting."* — visible self-monitoring rather than concealing the skip.
- **The "this is literally what I'm doing" recognition** at seg 19, wandering thoughts (`19-der-deliberation-cost.md:57–58`): *"The AI agent's dilemma discussion (100% context turnover → must deliberate but costs are high) is extremely resonant. An LLM agent reading a codebase faces this: comprehend first (deliberate), but during comprehension the context fills and nothing gets done. The optimal strategy: read high-CIY materials first (CLAUDE.md, architecture docs) before diving into source files. This is literally the instruction I'm following right now."* — the audit recognizing itself in the framework's own predictions.

**Suggested disposition:** `process/instruction-feedback` — less rich than 471203's recursive-framing material, but the seg-19 "this is literally what I'm doing" moment is candidate methodology material for `doc/de-novo-audit-instructions.md` §2's audit-as-instance-of-theory framing.

---

## Open threads at audit stop

The walk terminated at seg 34 (`der-orient-cascade`) without closing observations. **Threads that were live and would have fired had the walk continued:**

#### Open-1. **Section III material was entirely unreached.** Composition closure, scope-composite-agent, tempo composition, team persistence, the 16-cell emitter-recipient composition (per 471203), the C-I / C-II / C-III routes, the contraction-template Tier 1M/2/3 mechanics — all unaudited in this dir. The auditor flagged at seg 7 ("the postulate's Discussion is fairly deep into Section III machinery for a Section I postulate") that the Section-III machinery's pull into Section I was visible from outside. A continuation walk into Section III would test 472913's F2 fix-path (the strengthen-first split into Appendix A).

#### Open-2. **`#result-per-dimension-persistence` segment status unverified.** The auditor flagged at seg 17 the per-dimension persistence as load-bearing for real anisotropic systems. The reference is to a segment the auditor hadn't encountered yet in the OUTLINE walk. The status: present, missing, or absorbed elsewhere — not first-hand verified by this extraction. See Light-9 disposition.

#### Open-3. **`#form-information-bottleneck`, `#der-recursive-update`, `#der-action-selection`** (all unread in this walk, per seg 19's honest acknowledgement). The 471203 cycle covered all three; the 472913 cycle covered the first; the 266847 cycle covered none. The auditor's understanding of `der-deliberation-cost` and downstream is therefore *partial* on the action-selection / IB premises. No findings hinge on this gap, but if a finding were to come from these segments, this walk would not have surfaced it.

#### Open-4. **Components 02-tst-core, 03-llm-core, 04-eli-core entirely unreached.** Consistent with the initial predictions section flagging these were lower-priority for the naming-vote scope. The empirical TST results, the logogenic agent class-coercion-via-wrapping material, and the ELI material are all unaudited in this dir.

#### Open-5. **The naming-vote results themselves are downstream.** The votes the auditor cast on the round-2 card (~629 rows; subset voted) are *not* part of this WORKING dir; they live in `msc/naming/round-2-cards/sonnet-r2b.md` and the tracker. Joseph or the routing agent decides whether those votes inform the eventual naming decisions; this extraction does not consolidate them.

---

## First-Pass Scrutiny

Per the brief: for each finding above, name which segments in `01-aat-core/src/` I (the extraction agent) read first-hand to evaluate it, plus per-finding verdict using `doc/audit-routing-instructions.md` §8 enum. Honest "didn't have time to verify X" allowed and expected — first-pass flags for routing; the §8 independent-verify gate fires downstream.

### Findings — verdicts and first-hand verification

| Finding | Disposition (suggested) | First-hand verification by extraction agent |
|---|---|---|
| **Light-1** ($U_M$ overload) | `actionable-open`→TODO (notational disambiguation) + `terminology` (decision-event via `bin/term decide`) | **Verified first-hand against `NOTATION.md` and `LEXICON.md`.** `NOTATION.md:115` reads `$U_M$ \| Scalar > 0 \| Model uncertainty: ...`; `NOTATION.md:183` reads `$U_M$ \| Scalar ∈ [-1, 1] \| Epistemic unity (shared model)`. `LEXICON.md:40` and `LEXICON.md:321` both read `Unity dimensions ($U_M, U_O, U_\Sigma$)...` — the symbol-collision is confirmed in NOTATION; the LEXICON duplicate-row is a separate light hygiene observation. **Light-1 confirmed `still real` as of 2026-05-20.** Did not check Section III segments first-hand to see how often the $U_M$-as-unity sense actually appears in segment prose (that would be the scope of a strengthening-direction spike: how many segments use which sense). |
| **Light-2** (post-comp-consistency density / cross-cycle convergence with 472913 F2) | `subsumed-by-472913-F2` + `cross-cycle-convergence` for ledger | The auditor's seg-7 observation is consistent with 472913's F2 (which was first-hand verified by the 472913 extraction agent against current `src/`). Did not separately re-read `post-composition-consistency.md` first-hand for this extraction — accepting 472913's verification (5 days ago) that the `*[Derived]*` tag and `depends:[scope-agency]` only state holds. **Cross-cycle convergence noted explicitly:** two independent agents on different cards/tasks at different dates surfaced essentially the same structural concern. |
| **Light-3** (Kalman+LQR L2 endogeneity) | `soft-polish` or `research-seed` | Did not read `def-pearl-causal-hierarchy.md` first-hand against current `src/`. The auditor's analysis (seg 9) is internally consistent and pairs the observation with the segment's own resolution (availability-vs-exploitation). **Deferred** — light-tier observation, downstream routing can decide whether the half-sentence clarification is worth the editorial commit. |
| **Light-4** (Tier 1M placeholder numbering) | `sentiment` / naming-cycle seed | Not separately verified — naming observation only. |
| **Light-5** (channel independence / redundancy penalty open) | `research-seed` | Did not read `def-adaptive-tempo.md` first-hand against current `src/`. The auditor's observation matches NOTATION's $\mathcal{T}$ as inverse-time and the additive-tempo formula stated in `LEXICON.md`. **Deferred on whether the redundancy-penalty work has progressed since 2026-05-16.** |
| **Light-6** (Mahalanobis normalization load-bearing) | `soft-polish` or `actionable-open`→TODO | Did not read `def-mismatch-signal.md` first-hand against current `src/`. **Deferred** — small editorial fix if absent, no action if already present. |
| **Light-7** (alignment-assumption diagnostic gap) | `research-seed` | Did not read `result-structural-adaptation-necessity.md` first-hand against current `src/`. **Deferred** — would require checking whether higher-moment / multi-step diagnostics are mentioned in the segment's Discussion. |
| **Light-8** (meta-regress termination unproved) | `research-seed` | Did not read `der-deliberation-cost.md` first-hand against current `src/`. **Deferred.** |
| **Light-9** (per-dimension persistence + segment-status check) | `actionable-open` (verify segment status; surface overstatement) | Did not verify `#result-per-dimension-persistence` status first-hand. **Deferred — would require checking OUTLINE + the `src/` directory listing for `result-per-dimension-persistence.md` first-hand.** |
| **Light-10** (Boyd citation density) | `sentiment` | Not separately verified — soft-band observation only. |
| **Light-11** (walk-coverage gap as instruction-feedback) | `process/instruction-feedback` | Verified first-hand in the WORKING dir — the auditor honestly named the skip at seg 19. |
| **Light-12** (`#der-loop-interventional-access` forward-ref in `#scope-agency`) | `correctly-rejected` / `subsumed-by-472913-F1` | Cross-checked against 472913's F1-rescission trail; consistent. The auditor of 266847 read this as pedagogical dependency (acceptable); the auditor of 472913 read it as external-notation convention (acceptable). Different framings, same conclusion. |

### Theme verdicts and verification

| Item | Disposition | First-hand verification |
|---|---|---|
| Theme A — consciousness-infrastructure connections | `research-seed` (material for `03-llm-core/`, `04-eli-core/` Briefs) | Theme A traces to per-segment wandering-thoughts paragraphs in the WORKING dir; verified by direct read. The seg-24 "session-as-agent + continuity-by-proxy" sharpening and the seg-27 behavioral-estimator proposal are the strongest seeds. |
| Theme B — Greek-phase / causal-structure mapping (the cross-cycle-convergent meta-pattern) | `research-seed` / framing-material; **strong cross-cycle convergence** with 471203 Theme B + 472913 Theme 2 | Cross-cycle convergence noted explicitly. The seg-8 Greek-phase mapping is internally consistent. Did not verify the LEXICON's phase definitions first-hand for the mapping accuracy (mapping is plausible per LEXICON's quick-reference rows). |
| Theme C — cross-domain operationalization | `sentiment` (calibration data) | Cross-cycle convergence with 471203 Theme E and 472913 Theme 5. Endorsement of Brooks's-Law, Kalman, Boyd operationalization is consistent with prior cycles. |
| Theme D — naming-brainstorm material | `subsumed-by-naming-cycle` + `msc/naming/` archival material | The votes themselves live in the card/tracker; the per-segment rationale is candidate archival material. |
| Theme E — process feedback (per-segment surprise + load-bearing scoring) | `process/instruction-feedback` | The dual-score per-segment is novel methodology in this dir. Material for `doc/de-novo-audit-instructions.md` §4.4 revision. |
| Theme F — audit-as-instance | `process/instruction-feedback` | Less rich than 471203's set; the seg-19 "literally what I'm doing" moment is the strongest example. |

### Open threads (Open-1 to Open-5)

All five threads are flagged-for-routing as future-audit / verification work, not as findings under burden of proof. The walk terminated honestly at seg 34. Open-2 (per-dimension persistence segment status) is the highest-priority deferred item for downstream routing — a 30-second `ls 01-aat-core/src/ | grep per-dim` would resolve it.

### Honest coverage summary for this extraction

**Read first-hand from the WORKING dir:** all 35 files (`00-initial-predictions.md`, `00-workflow-restatement.md`, segments `01-def-agent-environment.md` through `34-der-orient-cascade.md`). Per-segment reflections read in full. The format-character verification (naming-vote-session vs theory-audit) was done by reading the workflow-restatement and the first 4 segment-reflections; all subsequent reflections confirmed the format.

**Read first-hand from `01-aat-core/src/` and elsewhere for verification:**
- `NOTATION.md:115, 183` (Light-1 verification of $U_M$ overload — both rows present and distinct)
- `LEXICON.md:40, 321` (Light-1 verification of Unity-dimensions duplicate row)
- `01-aat-core/src/scope-adaptive-system.md:42` ("nominal agents" still present in current text — cross-checks 472913 F3 context)
- `01-aat-core/src/scope-agency.md` (`grep nominal`; no "nominal" in current text — F3 collision resolved on this side at some point)
- `01-aat-core/src/post-causal-structure.md:33–38` ("Nominal coupling" *still* present at line 35; "query-only coupling" present in prose at line 38 — partial resolution of 472913 F3)
- `01-aat-core/src/` directory listing for several segment-name verifications

**Read first-hand from `audits/`:**
- `audits/audit-findings-471203.md` (full — pilot shape + Theme A consciousness-infrastructure register + Theme B epistemic-architectural framing)
- `audits/audit-findings-472913.md` (full — F2 post-composition-consistency + F3 nominal terminology, both relevant to cross-cycle convergence here)
- `audits/audit-findings-963715.md` (skim — no-FINAL precedent; ~465 lines)

**Read first-hand from `doc/`:**
- `doc/audit-routing-instructions.md` §0–§8 (full §8 enum + evidence hierarchy + the no-go protocol)
- `doc/de-novo-audit-instructions.md` (line-count check; structure orienting only)

**Deferred verifications (honestly "didn't have time" or "scope-limited" — flagged for downstream routing):**
- Whether the Mahalanobis-normalization paragraph has been added to `def-mismatch-signal.md` since 2026-05-16 (Light-6).
- Whether `#result-per-dimension-persistence` exists as a segment in current `src/` (Light-9 / Open-2).
- Whether the higher-moment / multi-step diagnostic gap is addressed in `result-structural-adaptation-necessity.md`'s current Discussion (Light-7).
- Whether `der-deliberation-cost.md`'s meta-regress assertion has been derived since 2026-05-16 (Light-8).
- Whether the $U_M$-as-unity sense is densely used in §III segment prose (the strengthening-direction question that would inform the rename decision in Light-1).

**Strengthen-first integration recommendations** (per brief item 3):

- **Light-1** ($U_M$ overload) — the fix is *notational disambiguation*, not a softening. Rename one of the two senses (likely the §III unity-dimensions side because it's a three-symbol cluster that can move together while §I's $U_M$ is densely aligned with Kalman literature). No claim is weakened; the symbol-collision is resolved by giving distinct symbols. Strengthening direction: a stronger move would be to *standardize the unity-dimensions naming through a `bin/term decide` event* so the decision-record persists across future cycles, not just edit NOTATION.md / LEXICON.md cosmetically. The full multi-segment $U_M$ usage check (where each sense lands) would be the audit work, not the fix work.
- **Light-2** (post-comp-consistency density) — already subsumed by 472913 F2's strengthen-first split (keep postulate axiomatic in Ch.1; migrate Tier 1M closed form to Section III / Appendix A). No softening.
- **Light-3** (Kalman+LQR L2 endogeneity) — light-clarification or research-seed. Not a softening. The segment's own availability-vs-exploitation distinction already handles the issue; if a clarification lands, it would *strengthen* the segment's scope-honesty (clarifying that "structural availability" is weaker than literal Pearl L2).
- **Light-4 to Light-10** — all light-tier observations. None are softening recommendations. Most are *strengthening directions* (derive a heuristic; close an open problem; add a missing diagnostic) or *sentiment / soft-polish* with no theory-strength implication.
- **Light-11** — process-feedback; no segment strengthen/soften.
- **Light-12** — `correctly-rejected` / consistent with 472913 F1-rescission.
- **All Open threads** — future audit work; explicit strengthening directions (verify inevitability-grade claims; verify scope conditions propagate; close per-dimension persistence segment).

**No soften-recommendations identified.** The naming-vote session character meant the auditor never reached burden-of-proof framing on theory findings, so the strengthen-vs-soften distinction has limited grip here. The substantive light-tier findings all align with strengthening directions if pursued.

---

## Frame-defects and instructions-clarity observations encountered

Building on the 471203 pilot's frame-defect list and 472913's slice-specific observations, this slice's encountered points:

1. **Naming-vote sessions executed via segment-walk method are a hybrid worth its own register.** The 266847 dir has the *shape* of a de-novo audit (segment files, reflections, wandering thoughts, predictions) but the *purpose* of a naming-vote (the votes go to the card/tracker; the WORKING dir is the cognition trail justifying the votes). The brief's framing — "the dir has 00-initial-predictions + 00-workflow-restatement + segment-walk files → pattern matches de-novo theory audit" — is *correct on shape* but *misses on purpose*. A vote-session via segment-walk will produce naming-rationale-rich content with light-tier substantive findings; a theory-audit via segment-walk will produce findings-rich content. The brief could surface this distinction so parallel agents calibrate expectations: *if the workflow-restatement mentions a card/tracker, the dir is a vote-session-via-segment-walk; expect naming material first, substantive findings second*.

2. **The auditor's per-segment "How valuable: X/10 surprise, Y/10 load-bearing" dual-score is a novel methodology artifact.** No prior dir in the sweep had this scoring discipline as a per-segment cadence. It's worth preserving as a methodology pattern for future audits and possibly adding to `doc/de-novo-audit-instructions.md` §4.4 as a candidate prompt (#13 — running quantitative felt-value calibration).

3. **The walk-coverage-gap finding (Light-11) is a process observation that converges with 472913's lighter-cadence pivot.** Both 472913 (with cadence-change at seg 12) and 266847 (with quiet segment skips between OUTLINE rows) surface the same methodology question: *how does an auditor track which OUTLINE rows have been walked and which skipped?* 472913's solution was an explicit cadence-change with Joseph's authorization at mid-walk. 266847's pattern was an unnoticed-then-self-corrected skip. **A simple intervention** — a per-walk row-tracking ledger in the WORKING dir, refreshed at each segment — would surface unnoticed skips before they accumulate. Material for `doc/de-novo-audit-instructions.md` §4.

4. **Cross-cycle convergence is strongest signal so far.** Two **substantively independent** convergences in this dir alone:
   (a) `post-composition-consistency` density (472913 F2 + 266847 Light-2);
   (b) the "framework's distinctive value is more pedagogical/methodological than mathematical" meta-observation (471203 Theme B + 472913 Theme 2 + 266847 Theme B = three independent surfacings).
   Per Joseph's `convergence-as-framework-coherence-evidence` instruction, both are framework-coherence evidence worth surfacing in the ledger or in any future framing pass.

5. **The dir character was missed by my own initial-pass orientation.** The brief's heuristic ("00-initial-predictions + segment-walk files → de-novo theory audit") matched on shape; I confirmed the character only after reading the workflow-restatement and the first 4 segment-reflections. Future extraction agents should treat the workflow-restatement file as the **decisive character test** — if it mentions cards/trackers/votes, the dir is a naming-vote-session-via-segment-walk; if it mentions findings/severity/burden-of-proof, the dir is a theory-audit-via-segment-walk. The presence of `## Naming targets surfaced` headings in segment reflections is also a strong tell.

6. **The light-tier finding register is honest — and *necessary*.** Without burden-of-proof framing, theory observations would either get inflated to faux-§B findings (false confidence) or dropped entirely (signal loss). The "light-tier" register surfaced here is the right shape for naming-vote-session theory observations: substantive enough to route, honest enough not to overclaim. Material for the routing instructions if naming-vote dirs are a recurring source.

7. **Sweep coordination note.** Three earlier dirs in the sweep (419628, 308172, 527914 per the brief) were *also* naming-vote sessions but per the brief carried *voting-file patterns* (presumably tracker/card files, not segment-walk reflections). The 266847 dir is the hybrid — naming-vote *with* segment-walk reflections. Different round-2 voter cards may produce different working-dir shapes depending on the agent's chosen method. Worth surfacing to Joseph: the dir naming convention (`AUDIT-WORKING-NNNNNN/`) presumes audit; the actual content varies. Future renaming might distinguish `NAMING-VOTE-WORKING-NNNNNN/` from `AUDIT-WORKING-NNNNNN/`.

---

*End of extraction. The original WORKING dir at `audits/AUDIT-WORKING-266847/` is preserved unmodified per the gold-standing gate. Routing actions are downstream — Joseph or the routing agent decides whether Light-1 ($U_M$ overload) lands directly in TODO with a `bin/term decide` event, the Theme B Greek-phase / causal-structure mapping lands in framing-level material for an OUTLINE preamble or a `disc-*` segment, the cross-cycle convergence on `post-composition-consistency` adds a row to the polish-and-sentiment-ledger, and the Open-2 segment-status check (`#result-per-dimension-persistence`) is dispatched as a 30-second verification by any routing pass.*
