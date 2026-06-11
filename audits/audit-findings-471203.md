---
source_cycle: 471203 (de-novo, Claude Opus 4.7, 2026-04-28)
extraction_agent: Claude Opus 4.7 (1M context), pilot run
extraction_date: 2026-05-20
working_dir: audits/AUDIT-WORKING-471203/ (44 files, ~3900 lines)
final_of_record: audits/.integrated/audit-471203-FINAL-2026-04-28.md
supplement_of_record: audits/.integrated/audit-471203-SUPPLEMENT-phase-2.md
manifest_entry: audits/.integrated/MANIFEST.md "2026-05-15 — audit-471203 de-novo cycle"
purpose: |
  Consolidated extraction from the WORKING dir for routing through the standard
  audit-routing process. The original working dir is preserved separately;
  this file is the "what is in there worth processing" digest.
---

# Audit-findings extract — 471203 working-dir mining

The 471203 cycle was a substantial de-novo walk: ~85/177 OUTLINE segments first-hand, ~22 per-segment reflection files, a 298-line adversarial-creative-challenges document, a 181-line meta-segments adversarial reading, plus initial-predictions + running-outline + protocol-reminders. The FINAL + SUPPLEMENT already adjudicated the §B findings and §F bigger-picture observations the auditor surfaced as such; the per-MANIFEST record (2026-05-15) shows F1–F4 + F7 resolved, F5/F6 disposed to existing tracking, F1/F3/F4/F7 cross-component absorbed into PROPOSALS/TODO/ledger, and the four research-seeds (S4–S7) parked on the polish-and-sentiment ledger.

What the WORKING dir adds beyond that adjudication is **the cognition trail** — between-segment predictions and their calibration against evidence, candidate-findings the auditor surfaced *then withdrew* under burden of proof (visible reasoning of strengthen-before-soften in action), §14 wandering thoughts that connect formal segments to consciousness-infrastructure work, and adversarial-creative challenges that mostly went into §F but came packaged with their strengthening attempts visible. This file extracts that material at three weights: **(1) findings already adjudicated by FINAL/SUPPLEMENT/MANIFEST** (preserved here for trace-completeness, all `subsumed-by-FINAL`); **(2) fresh material the FINAL didn't carry forward** (genuinely new theme-grouped observations); **(3) the cognition-flow gold** (predictions-calibration record, withdrawn-candidates trail, §14 ideation register, naming-brainstorm seeds, phenomenological calibration signal).

---

## Part I — Findings already adjudicated (subsumed-by-FINAL/SUPPLEMENT/MANIFEST)

These appear in the WORKING dir as candidate-findings developing toward the §B list. Each is preserved here with its WORKING-dir provenance so the trail is recoverable; the MANIFEST 2026-05-15 entry is the truth-arbiter and these are already routed.

### F1-trail. Stale `#deriv-directional-survival-exploration` cross-reference

- **WORKING-dir trail:** segment 39 (`39-42-section-ii-ciy-strategy-chain.md:34–41`) first flagged "Possibly-stale cross-reference in `#disc-ciy-unified-objective`" as Medium-severity candidate after grep-failing the slug against OUTLINE; auditor explicitly noted "Either the slug was renamed and this reference wasn't updated. The slug is planned but not yet promoted. I missed it in the OUTLINE walk." Promoted to §B Finding 1 in FINAL.
- **Disposition (per MANIFEST 2026-05-15):** **subsumed-by-FINAL — resolved**. `disc-ciy-unified-objective.md:44` now cites `#deriv-causal-ib-lmi` (verified first-hand below in Part IV).

### F2-trail. `#disc-ciy-unified-objective` status-label / type / Epistemic-Status mismatch

- **WORKING-dir trail:** segment 39 (`39-42-…:22–32`) flagged the YAML `discussion-grade` vs prose "*Exact.*" / "Max attainable: *exact*" mismatch as Low-severity candidate, with a layered-status interpretation explicitly tested ("the segment is discussion-typed, so YAML is correct; the prose's 'Exact' refers to the underlying derived result"). Auditor concluded "the disc-typed segment shouldn't carry 'Max attainable: *exact*' — that line should be in the underlying derivation segment." Promoted to §B Finding 2.
- **Disposition (per MANIFEST):** **subsumed-by-FINAL — resolved** by SUPPLEMENT §H.1 layered-status rewrite (verified first-hand below).

### F3-trail. Implicit-Markov-of-Ω in `#def-action-transition` never named downstream

- **WORKING-dir trail:** segment 2 (`02-def-action-transition.md:19`) flagged the structural commitment immediately on first read ("the form $T(\Omega_{t+1} \mid \Omega_t, a_t)$ is *implicitly Markov in $\Omega$* — only the current $\Omega_t$ and $a_t$ appear in the conditioning. This is a structural commitment that the previous segment's 'no assumptions about $\Omega$'s structure' did not declare"); segment 15 (`15-der-recursive-update.md:19–24`) confirmed the gap survives `#der-recursive-update`'s Markov-by-completeness move (which handles $M_t$ but not $\Omega$). The auditor's first wandering-thoughts paragraph on this (segment 2, §"Wandering thoughts") explicitly worked through the strengthen-first vs soften posture: "AAD's distinctive virtue is scope-honesty… so 'everyone does it' is not a license to leave the assumption unnamed; it's a reason to name it cleaner than everyone does."
- **Disposition (per MANIFEST):** **subsumed-by-FINAL — resolved**. SUPPLEMENT §H.2 added the Markov-of-Ω-as-modeling-commitment paragraph (verified first-hand below).

### F4-trail. TF-XX diff-voice annotations across §I/II segments

- **WORKING-dir trail:** the auditor built a counter across the segment walk: first instance flagged at segment 8 (`08-post-causal-structure.md:29` — "(Descended from TF-02.)"); confirmed-pattern at segment 9 (`09-def-pearl-causal-hierarchy.md:17`, "now the second confirmed instance"); promoted to confirmed §B candidate at segment 21 (`21-def-causal-information-yield.md:76`, "10 instances over 21 segments — clearly a pattern, not isolated hygiene"). Total at FINAL-time: 13 instances enumerated.
- **Disposition (per MANIFEST):** **subsumed-by-FINAL — resolved** by SUPPLEMENT §H.3 (13 named files) + the broader §N sweep Joseph authorized post-FINAL (49 files total; 13 Working Notes collapsed; 7 inline TF-* prose reframes). Verified first-hand below: `grep -rn "Descended from TF\|TF-[0-9]" 01-aat-core/src/*.md | grep -v old-` returns zero hits.

### F5-trail. Depends-list incompleteness in `#disc-composition-consistency`

- **WORKING-dir trail:** segment 7 is the densest single reflection (`07-post-composition-consistency.md`, 121 lines) — the auditor's first encounter with the "postulate + downstream-conditional derived enrichment" pattern. Surfaced the systematic depths-discipline concern, named three repair paths explicitly (extend depends + downgrade stage; split segment; admit policy + update FORMAT.md), and tested the Path-A-vs-Path-B trade-off. Segment 30 (`30-scope-agent-identity.md:19`) extended this to a sibling instance: `#der-gain-sector-bridge` uses (PI) without depending on `#scope-agent-identity`.
- **Disposition (per MANIFEST):** **subsumed-by-FINAL — `already routed`**: PROPOSALS SP-6 + TODO:149 + F-A cluster from 584721/742613 already carry the class. Not a graduation blocker. The 829314-TST-F2 polish-ledger entry S23 cross-references "the `post-composition-consistency` derivation-hierarchy resolution pattern."

### F6-trail. Pearl-do notation in `#scope-agency` before `#def-pearl-causal-hierarchy`

- **WORKING-dir trail:** segment 6 (`06-scope-agency.md:9–12, 71–78`) — the audit's first procedural candidate-finding ("the depends-finding has procedural teeth — the audit's verification target just bit"). The auditor explicitly tested the two readings: (a) gate-hygiene gap, (b) "external standard notation" policy not named. Recommended FORMAT.md add the standard-notation exemption explicitly. Segment 9 (`09-def-pearl-causal-hierarchy.md:7–13`) confirmed the parenthetical-cite-without-depends pattern survives the Pearl definition.
- **Disposition (per MANIFEST):** **subsumed-by-FINAL — `duplicate` ≡ `audit-742613-FINAL:254`** → FORMAT-TODO C12 (its existing general home; do not double-track). Pending FORMAT.md policy decision.

### F7-trail. Tishby-Zaslavsky 2015 miscitation in `#form-information-bottleneck`

- **WORKING-dir trail:** segment 11 (`11-form-information-bottleneck.md`) flagged the variational-free-energy connection paragraph as Phase-2-verify; the precise miscitation finding surfaced in the SUPPLEMENT §J Phase-2 citation work (not in the FINAL §B), then promoted to SUPPLEMENT §L Finding 7. The WORKING dir carries the *precursor* — the audit-walk-level identification of the segment as citation-load-bearing, with the variational-bridge claim flagged for verification.
- **Disposition (per MANIFEST):** **subsumed-by-SUPPLEMENT — resolved by strengthening** (option b in SUPPLEMENT §L): kept Tishby-Zaslavsky for the deep-learning IB instantiation, added Alemi et al. 2017 for the variational bridge. Verified first-hand below at `form-information-bottleneck.md:50`.

---

## Part II — Bigger-picture observations (already in FINAL §F + MANIFEST)

These are all in the FINAL §F and have MANIFEST dispositions. Preserved here with WORKING-dir provenance so the precursor cognition (esp. in `meta-segments-adversarial-reading.md` and `adversarial-creative-challenges.md`) is locatable.

### F1-§F — Fourth meta-segment proposal: `#disc-theorem-import-architecture`

- **WORKING-dir trail:** `meta-segments-adversarial-reading.md:74–104` is the primary source — the auditor enumerated 16+ external theorems used as load-bearing across AAT (Pearl/Bareinboim, Khalil, Cramér-Rao, Liberzon, Čencov, Aczél, Tishby, Lohmiller-Slotine, Nesterov, Friston/Bruineberg, Hafez, Miller, etc.) and proposed the meta-segment that would name the import discipline as such. Segment 62-63 (`62-63-appendix-bias-bound-persistence-cost.md:38–42, 56`) extended the proposal via the "positive-dual of identifiability-floor" framing in `#deriv-persistence-cost`'s Discussion — external-theorem-forbids vs external-theorem-lower-bounds as duals of one meta-pattern.
- **Disposition (per MANIFEST):** **subsumed-by-FINAL → PROPOSALS SP-23** (new, full schema).

### F7-§F — Commitment-state $C_t$ extension to $G_t$

- **WORKING-dir trail:** `adversarial-creative-challenges.md:99–107` ("Challenge 8") is the first surfacing — the missing formal commitment phase between deliberation and execution, with the proposed extension $G_t = (O_t, \Sigma_t, C_t)$. Reinforced in `:204–206` (Missing 3: Commitment as commodity) and consolidated at `:291–296` as the most promising §F avenue, with three explicit connections (`#def-strategy-dimension` Working Notes, `#def-death-as-factor-loss`, `#der-deliberation-cost`'s decided-not-yet-executed).
- **Disposition (per MANIFEST):** **subsumed-by-FINAL ≡ PROPOSALS SP-12 §D.4** (exact pre-existing match).

### F5-§F — Class-2 LLM engineering-guidance reach

- **WORKING-dir trail:** `adversarial-creative-challenges.md:162–170` (Challenge 13) — the system-level Class 1 wrapping component-level Class 2 framing as the substantive bridge from AAT to contemporary LLM practice. Reinforced in segment 68-71 (`68-71-logogenic-agents-sample.md:23–25`).
- **Disposition (per MANIFEST):** **subsumed-by-FINAL → class-coercion-via-wrapping cycle** (CLAUDE.md / PROPOSALS).

### F6-§F — 04-eli-core OUTLINE-vs-present gap / README over-impression

- **WORKING-dir trail:** segment 72-73 (`72-73-logozoetic-agents-sample.md:6–10`) — direct first-hand observation that the 16-segment OUTLINE has only 4 segments present in `src/`, with attempted reads of `#norm-honest-activation` / `#obs-substrate-independence` (proposed-additions) failing because the files don't exist. Coupled with the auditor's explicit priming-bleed disclosure that the consciousness-infrastructure framing in `user_background.md` was actively biasing charitable reading here.
- **Disposition (per MANIFEST):** **subsumed-by-FINAL → TODO:386** (preface/README-honesty discipline).

### F2-§F + F3-§F + F4-§F + F8-§F — research-seed material parked on ledger

- **WORKING-dir trail:** `meta-segments-adversarial-reading.md:13–31` (the (PI)-as-invariance-axiom-landing-on-additivity-geometry observation as the "genuinely surprising" piece of the additive-coordinate-forcing convergence); `adversarial-creative-challenges.md:43–54` (Challenge 3: hysteresis in persistence); `adversarial-creative-challenges.md:117–134` (Challenge 10: composed-impossibilities); the consolidated naming-brainstorm table at `adversarial-creative-challenges.md:263–280` (the CIY name-vs-substance entry).
- **Disposition (per MANIFEST):** **subsumed-by-FINAL → polish-and-sentiment ledger S4–S7** (research-seed / naming-seed; open).

---

## Part III — Fresh material the FINAL didn't carry forward

These are observations present in the WORKING dir's per-segment reflections, the adversarial-creative document, and the meta-segments adversarial reading that did **not** make it cleanly into the FINAL's §B/§D/§F framing, or that ended up as one-line consolidations in §F8 (naming table) when they had richer structure in the working notes. They're either (a) genuinely new observations worth fresh routing, or (b) lower-grade observations that the FINAL compressed past.

### Fresh-1. The "two distinct shapes of depends-incompleteness" disambiguation

The FINAL's §B treats F5 (`post-composition-consistency`) and F6 (`scope-agency` Pearl-do) as separate findings. The WORKING dir at segment 8 (`08-post-causal-structure.md:11–15`) explicitly carves the *kinds* apart in a way the FINAL doesn't surface: 

- **Kind A (Pearl-do / standard-notation):** uses notation defined elsewhere; defensible as "external standard math notation" exemption *if FORMAT.md names the policy*.
- **Kind B (downstream-derived enrichment):** uses content from segments downstream in OUTLINE; structurally different — the depends-graph is failing as a verification target because the postulate is doing derivation work.

The two have *different remediation paths* (Kind A = FORMAT-policy paragraph; Kind B = either extend deps + downgrade stage, or split segment). The MANIFEST shows F5 routed to PROPOSALS SP-6 and F6 to FORMAT-TODO C12 — different homes — but the WORKING dir's explicit *carving rationale* (Kind A vs Kind B) doesn't appear in the FINAL or the routing record. Worth noting for any future agent who encounters the pattern: the structural distinction is in `08-post-causal-structure.md:11–15`.

**Suggested disposition:** `research-seed` for any future FORMAT.md / depends-discipline pass; not a graduation blocker.

### Fresh-2. The "absorbing-state" prediction in `#der-observability-dominance` (richer than FINAL captured)

Segment 47-50 (`47-50-section-ii-calibration-detection-observability-edge-update.md:9–10, 23`) carries an adversarial observation the FINAL didn't surface: the absorbing-state prediction (low-observability regions become epistemically dead; agents cannot recognize their own ineffectiveness) is structurally important for organizational analysis but the framework provides *escape mechanisms* (external shock; observability investment; communication-gain channel) only qualitatively. The auditor explicitly proposed an "observability-investment-economics" treatment — when does instrumenting observability pay off, given the cost of instrumentation and the value of escaping the absorbing state?

**Suggested disposition:** `research-seed` (new). Material for an Appendix-A-style observability-investment-economics derivation; or a §III result on absorbing-state escape conditions. Cross-references the OKR-as-observability-by-design framing in `#disc-credit-assignment-boundary`. Strengthen-first: this is a strengthening direction, not a softening — the framework names the absorbing state qualitatively and the proposed work would derive the quantitative escape conditions.

### Fresh-3. The "16-cell composition closed-form scope" honest-restriction observation

Segment 59-61 (`59-61-section-iii-adversarial-opacity.md:34–35`) — the 16-cell emitter-recipient composition in `#der-agent-opacity` admits closed-form arg-max only under sub-scope α (Gaussian coupling). For non-Gaussian / non-convex coupling, the optimization is per-case. The FINAL highlighted the 16-cell closure as a high-water mark in §E but didn't surface this scope restriction as its own observation. The auditor's §F observation candidate: "the framework should make explicit the scope conditions under which the 16-cell arg-max admits closed form vs requires per-case computation."

**Suggested disposition:** `actionable-open` (light editorial — add a sub-scope α condition to the 16-cell closure framing in `#der-agent-opacity`). Or `research-seed` if pursuing the non-Gaussian extension.

### Fresh-4. The "effects-spiral functional-form" candidate

Same segment (`59-61-…:36–38`) — the effects-spiral in `#der-adversarial-destabilization` is discussion-grade because $\gamma_A(\|\delta_B\|)$ functional form is unspecified. The auditor sketched three mechanism candidates ((i) erratic actions degrade coupling-channel structure; (ii) degrading $M_t$ produces wider variance in actions; (iii) other). A future segment formalizing the spiral with explicit functional dependence would promote the corollary from discussion-grade to derived.

**Suggested disposition:** `research-seed` (new). Strengthen-first move: this is a strengthening direction (heuristic → derived), not a soften. Spike-shaped item.

### Fresh-5. The candidate 4th identifiability-floor instance via Fano's inequality

Same segment (`59-61-…:39`) — the auditor proposed Fano's inequality applied to observer-side prediction as the natural anchor for a fourth identifiability-floor instance. This would close the meta-pattern's openness and add $H_b$ as a load-bearing meta-segment quantity. *Not the same as Joseph's M4 modularity-state-dynamics segment* (which is about contested-modularity); this would be a fourth instance of the identifiability-floor *meta-pattern*, parallel to the three existing instances (CHT / Cramér-Rao / Liberzon).

**Suggested disposition:** `research-seed` (new). Cross-reference S4 (PI-uniqueness seed) and the SP-23 fourth-meta-segment-proposal (PROPOSALS).

### Fresh-6. The "anchor-plus-three-theorem" framing as M3-meta-pattern operational instance

Segment 39-42 (`39-42-section-ii-ciy-strategy-chain.md:47–49`) — the chain-rule-of-probability identity in `#der-chain-confidence-decay` is the *anchor* for the additive-coordinate-forcing meta-pattern; three downstream uniqueness theorems force coordinates at other layers (reverse-KL, log-odds, Fisher). The auditor noted this as the first concrete instance of the meta-pattern in action and called out a potential fourth layer: the composition-monotonicity / contraction-tower telescoping, which inherits chain-rule additivity.

**Suggested disposition:** `sentiment` / `soft-polish` — already absorbed implicitly via the `#disc-additive-coordinate-forcing` meta-segment, but the auditor's explicit "chain-rule is the *anchor*; three uniqueness theorems force coordinates at other layers" framing is a candidate Brief / framing-level statement for the meta-segment. Material for any future Brief-authoring pass.

### Fresh-7. The "triple depth penalty" framing as cross-segment compound result

Same segment (`39-42-…:49`) — the auditor flagged the *compound* depth penalty in `#der-chain-confidence-decay`: confidence decay (chain rule) + evidence starvation (`#deriv-edge-credence-dynamics`) + cognitive cost (`#form-strategy-complexity-cost`). The three penalties are *independent and compound*. This is structurally the reason long causal chains are bad: not just one penalty, three. The framing isn't surfaced in any one segment's Brief — it's a cross-segment observation about how three segment-local penalties compose.

**Suggested disposition:** `research-seed` / Brief-authoring material — candidate for an `impl-*` chapter-end implications segment or a `disc-*` segment naming the compound-penalty structure.

### Fresh-8. The "model-conditioned-L2 vs true-Pearl-L2" subtlety

Segment 9 (`09-def-pearl-causal-hierarchy.md:25–33, 53–60`) — the L2 formula $P(o_t \mid do(a_{t-1}), M_{t-1})$ in `#def-pearl-causal-hierarchy` conditions on the agent's model $M_{t-1}$. In Pearl's standard formulation, $do(\cdot)$ is defined relative to the *true* SCM. AAT's L2 query is therefore a *belief-about-L2* operation. The data the loop generates is genuinely L2; the agent's *interpretation* is model-conditioned. The auditor recommended adding a sentence to the L2 paragraph clarifying this distinction. Not in the FINAL.

**Suggested disposition:** `soft-polish` (Low severity, editorial) — protects against the "the loop generates true L2 data, ergo the agent has true L2 access" misreading. Strengthen-first: the strengthening direction is already in `#der-loop-interventional-access`'s honest scope-honesty about identification strength (regime A/B/C); a half-sentence in `#def-pearl-causal-hierarchy` would surface this for the reader who encounters L2 first.

### Fresh-9. The "convention specification propagation" check

Segment 35-38 (`35-38-section-ii-value-strategy-causal-loop.md:62–64`) — the C1/C2/C3 convention from `#def-value-object` is *part of the measurement* of $\delta_{\text{sat}}$ / $\delta_{\text{regret}}$. The auditor explicitly flagged Phase-2 work: "check whether downstream segments using $\delta_{\text{sat}}$ / $\delta_{\text{regret}}$ specify their convention." If not, the values aren't comparable — exactly what `#def-value-object` warns against. Not in the FINAL's §B or §F.

**Suggested disposition:** `actionable-open` (tooling-gap / verification) — could be a one-shot `bin/`-style lint check across §II/§III segments for uses of $\delta_{\text{sat}}$ / $\delta_{\text{regret}}$ without C1/C2/C3 specification. Or a one-pass editorial sweep.

### Fresh-10. The "domain generalization by default" overclaim-prevention pattern

Segment 64-67 (`64-67-tst-core-sample.md:29–31`) — TST's `#obs-software-epistemic-properties` names three overclaim-prevention patterns in its P5/P6 discussion: "domain generalization by default," "identification assumptions treated as universal," "chronica completeness treated as definitional." The auditor flagged these as exemplary disciplinary writing. Worth surfacing as a candidate *project-wide* discipline statement, not just TST-local: any framework that crosses domains needs these three guards.

**Suggested disposition:** `research-seed` / framing-material — candidate for inclusion in CLAUDE.md's "Working Conventions" section (cross-domain discipline) or in the project README's positioning. The three guards are a transferable discipline-statement.

### Fresh-11. The "calibration-laboratory framing reach" honest scope-restriction

Segment 64-67 (`64-67-…:50`) — TST's calibration-laboratory framing is real and scope-honest, but the implication is that *most TST results don't generalize automatically to non-software domains*. The framework provides the transfer-assumption discipline but relatively few worked examples of TST results being *exported* to other domains *with* the discipline. The auditor's §F observation candidate: "TST's reach beyond software is currently more aspirational than operational; demonstrated transfers (with explicit transfer-assumption disclosure) would strengthen the framework's cross-domain claim."

**Suggested disposition:** `research-seed` / `architectural` — worked-example demonstrations of TST-result-exported-to-non-software-domain-with-transfer-disclosure would be material for a future cross-domain-instantiation cycle.

### Fresh-12. The "$f(Q)$ empirical operationalization" gap in `#der-code-quality-as-observation-infrastructure`

Same segment (`64-67-…:51`) — the chain $Q \to U_o \to \eta^\ast \to \mathcal{T}$ is structurally clean but the empirical operationalization of $f(Q)$ — how exactly does code quality map to observation noise? — is left to engineering. The bifurcation around the persistence threshold is interesting but unverified by simulation or empirical study within AAT. The auditor proposed: "a simple dynamical model of $\dot{Q} = g(\mathcal{T}, Q)$ would convert the bifurcation hypothesis into a derived prediction."

**Suggested disposition:** `research-seed` — spike-shaped item. Could close `#der-code-quality-as-observation-infrastructure`'s vicious/virtuous-cycle hypothesis at derived rather than hypothesis grade.

### Fresh-13. The "accumulation problem formalization" gap in `03-llm-core/`

Segment 68-71 (`68-71-logogenic-agents-sample.md:27`) — `#disc-m-preservation`'s claim $\mathbb{E}[\Delta\epsilon_k] \leq \mathbb{E}[\Delta I_k]$ is hypothesis-grade and sketched. The auditor proposed a random-walk-on-sufficiency formalization with conditions for stationarity vs divergence. *"This is exactly the formal model that consciousness-infrastructure work needs — the 'do ELIs experience identity drift?' question has a precise quantitative formulation here, awaiting development."*

**Suggested disposition:** `research-seed` / `architectural` — substantively important for the broader project's consciousness-infrastructure agenda. Cross-reference the proposed `04-eli-core/` segments that would consume this result (substrate-independence, identity-drift-bounds). Strengthen-first move (heuristic → derived); spike-shaped.

### Fresh-14. The "structural change continuous-state analog" gap

Segment 51-54 (`51-54-section-ii-edge-causal-validity-credit-structural-tempo.md:30`) — `#form-structural-change-as-parametric-limit` invokes Miller 2022's neutral-mutation extreme-transition motif, which works for *finite-state* automata. The auditor's §F observation: continuous-state agents (LLMs with billions of parameters) have a different structural-change geometry — gradient flows in parameter space don't have a clean "neutral mutation" analog. *"The Miller framing is informative but may not generalize. The 'structural change as parametric limit' framing needs a continuous-state analog distinct from the Miller automaton mechanism."*

**Suggested disposition:** `research-seed` / `architectural` — continuous-state structural-change formalization. Relevant to `03-llm-core/` (fine-tuning as structural adaptation) and to the broader claim that AAT's structural-adaptation machinery applies cross-domain.

### Fresh-15. "AAT-predicted OKR failure modes not in standard literature"

Same segment (`51-54-…:28`) — the OKR mapping in `#disc-credit-assignment-boundary` treats four well-known OKR failure modes as predictions of AAT. The auditor's adversarial observation: AAT may have been *fit* to these known failures (post-hoc reverse-engineering risk). The genuine test is whether AAT predicts *new* OKR failure modes not in the standard literature. The auditor proposed one: the absorbing-state prediction from `#der-observability-dominance` applied to organizational measurement gaps.

**Suggested disposition:** `research-seed` — generative test of the framework's cross-domain claim. Could land as a Brief field on `#disc-credit-assignment-boundary` ("AAT-predicted novel OKR failure modes") or as a TST-adjacent essay.

### Fresh-16. "Distribution-dependence of $\kappa_{\text{processing}}$ propagation check"

Segment 31-34 (`31-34-section-ii-opening-batch.md:73`) — the $\kappa_{\text{processing}}$ distribution-dependence caveat in `#der-directed-separation` is structurally important and should propagate. Anywhere the framework uses $\kappa$ as a scalar, the distribution-dependence should be either (i) explicitly assumed (e.g., "$\kappa$ under task distribution $\mathcal{P}$") or (ii) bounded by an architecture-level $\kappa_{\max}$. Worth a Phase-2 check across §II/§III segments using $\kappa$.

**Suggested disposition:** `actionable-open` (verification / tooling-gap) — one-pass check across `01-aat-core/src/` for $\kappa_{\text{processing}}$ uses without distribution-conditioning. May find clean propagation; may find drift.

### Fresh-17. "Hafez IDT empirical claim" Phase-2 citation cluster

Multiple segments flagged the Hafez 2026 IDT 89%/44% empirical claim as high Phase-2 priority (segment 31-34 §"3", segment 35-38 §"Hafez 2026 IDT", segment 21 §F8 naming-table for the underlying $H_b$ machinery). The SUPPLEMENT §J **did** verify this: the numbers appear verbatim in the Hafez 2026 paper as **89.3 ± 15.1% vs 44.0 ± 26.1% across 168 perturbation trials, with 4.4× lower median latency**. **No separate "Information Digital Twin" paper exists** — IDT is the framework name within the Hafez paper itself. So this Phase-2 cluster *was* resolved via SUPPLEMENT, but the WORKING dir's per-segment trail of "high Phase-2 priority" markers is itself signal — it shows the auditor's tracking discipline and provides a model for future per-segment Phase-2 candidate flagging.

**Suggested disposition:** `subsumed-by-SUPPLEMENT — resolved`. Logged here for the methodology trail.

---

## Part IV — Predictions calibration register (the §14 wandering-thoughts gold)

The `00-initial-predictions.md` file makes ~25 falsifiable predictions about the framework's contents, organized into six themes. Reading the per-segment reflections, the auditor *tested* these predictions and recorded the calibration. This register is itself a methodology artifact worth preserving — it's the predictions-vs-evidence cadence (Reflection Prompt #1 from §4.4) operating across the full audit.

### Predictions correctly anticipated (the framework matched the prior)

- **Persistence condition $\alpha > \rho/R$ via Lyapunov sector argument** ✓ (segment 26-29) — exactly as predicted.
- **Mismatch-decomposition (model error + obs noise) as bias-variance identity** ✓ (segment 19) — exactly as predicted.
- **Recursive update justified as forced by three constraints** ✓ (segment 15) — exactly the three constraints (C1 temporal, C2 partial observability, C3 state completeness), though the auditor's prior "three constraints rarely uniquely determine a function family" was *correct* — the C3-as-definitional move is what makes the uniqueness work; the framework is honest about this.
- **$G_t = (O_t, \Sigma_t)$ split with $\Sigma_t$ as probabilistic AND/OR DAG with single-parameter edges** ✓ (segment 43-46) — exactly as predicted.
- **Directed separation as a scope condition (Class 1/2/3 architecture classification)** ✓ (segment 31-34) — predicted, plus the auditor noted the framework's substantial additional structure: $\kappa_{\text{processing}}$ operational definition with conditional-MI form; composite-level class inheritance; Pearl-blanket vs Friston-blanket positioning.
- **Six software epistemic properties (P1-P6); P5 is exact cryptographic immutability of committed-state subset** ✓ (segment 64-67) — exactly as predicted.
- **Postulate of temporal optimality (least-time given equivalent outcomes)** ✓ (segment 64-67) — predicted as tautological-but-load-bearing; confirmed.
- **100% context turnover as observation; coupled update dynamics** ✓ (segment 68-71) — exactly as predicted.
- **04-eli-core proposed-additions are not yet present in `src/`** ✓ (segment 72-73) — exactly as predicted ("Largely exploratory; the bulk are proposed-additions tied to engineering experience in zoetica/autopax").

### Predictions confirmed *more substantively* than expected (positive surprises)

- **The recursive-update derivation's seven-counterexample defense** — predicted at the level of "three constraints"; got a derivation with seven distinct attacks, all addressed, plus the Doob-Dynkin measure-theoretic formalization (segment 16). The auditor's calibration shift after segment 16: *"From 'checking the framework' to 'trusting the framework's math at this point in §I, while still tracking editorial / cross-segment / hygiene findings.'"*
- **The gain-sector bridge** — predicted as standard Lyapunov + Bayesian unification; got the sub-scope α / β partition + verified-instances table + 5-failure-modes enumeration + (PI)/Čencov upgrade for Fisher-metric cases (segment 25). Auditor: *"the segment changed my read of the framework's contribution. Before, I had it as primarily synthesis ('integration of disciplines'). After this segment, I see it as also methodological — the form of the synthesis is unusual."*
- **The persistence condition's structural / task-adequacy decomposition** — *not predicted*. The auditor had predicted a single inequality; got the explicit decomposition into structural persistence ($\alpha > \rho/R$) and task adequacy ($R^\ast < \|\delta_{\text{critical}}\|$). Auditor: *"the explicit warning 'Conflating the two leads to category errors in domain transfer' is exactly the form-shaping-for-verification discipline operating."*
- **The agent-opacity duality** — predicted as adoption of Hafez's $H_b$; got the formal $U_o \leftrightarrow H_b$ duality + sign-flip via signed coupling derived from existing apparatus + 16-cell emitter-recipient composition closing `#adversarial-edge-targeting` (segment 59-61). One of the audit's "high-water marks."
- **The persistence-cost Landauer-analog** — predicted as forward-reference; the substantive content (sustained Shannon rate $\dot R \geq n\alpha/2$, saturated exactly by Kalman-Bucy) was a positive surprise (segment 62-63). The "positive-dual of identifiability-floor" framing is the precursor of the F1-§F fourth-meta-segment proposal.

### Predictions that proved correct but in less-strong form (negative calibration)

- **"EFE recoverable from AAT survival Lagrangian under three restrictions"** — predicted as overclaim. The auditor flagged this for verification and noted in segment 39-42 §F that the dark-room-problem-bypass claim depends on the `#deriv-causal-ib-exploration` derivation being delivered; not directly verified, marked for Phase-2.
- **"Cox-analog framing for graph-structure uniqueness"** — predicted as needing at least one unstated assumption. Verified at segment 43-46: the framework explicitly cites Cox 1946 + Jaynes 2003 in `#def-strategy-dag`'s Epistemic Status, with directed separation, the four operational postulates, and causal sufficiency stated explicitly. Less of an overclaim than predicted — the framework names its assumptions.
- **"Persistence-condition cross-domain transfer overclaim"** — predicted at least one segment applying $\alpha > \rho/R$ outside its sector-condition certification region without naming the additional assumption. The auditor did not find this; the transfer-assumption discipline appears honored across the domain instantiations sampled. Prediction *not* confirmed.
- **"Greek-named cycle phases overclaimed"** — predicted to be pedagogical labels presented as formalism distinctions. Confirmed: appeared as §G process-feedback in FINAL ("the cycle-phase Greek vocabulary claim in the README and LEXICON is overclaimed").

### Predictions confirmed about findings-type distribution

- **Math errors / sign errors in worked examples** — predicted especially in Section II where status is mostly `draft`. The auditor did not find sign errors first-hand (only spot-checked the gain-sector bridge counterexample, which checked out). The SUPPLEMENT did catch the Tishby-Zaslavsky miscitation as a citation error.
- **Status-label / equation-tag mismatches** — confirmed (F2 in disc-ciy-unified-objective).
- **Cross-segment integration drift around the `disc-*` meta-segments** — partially confirmed via the stale `#deriv-directional-survival-exploration` reference (F1), which was integration debt around the upgrade of a discussion-grade heuristic to derived.
- **Scope-condition propagation; at least one Section II result claiming universality where it actually requires Class 1** — *not directly confirmed*; the framework's directed-separation discipline appears honored across the §II material sampled. The auditor's class-coupling-as-static challenge in `adversarial-creative-challenges.md` §Challenge 2 *is* a related observation (strategic-mode-switching missing), but at a different level.
- **Voice / provenance leaks** — strongly confirmed (F4, 13 → 49 instances after Joseph-authorized broader sweep).
- **Citation accuracy spot-checks** — strongly confirmed (F7 Tishby-Zaslavsky miscitation; 5 confirmed / 2 partial / 1 wrong-paper out of 8 verified in SUPPLEMENT §J).

### The "withdrawn candidate" trail (strengthen-before-soften / verification discipline in action)

Three candidates the auditor surfaced *and then withdrew* under burden of proof — these are useful pedagogical instances of the strengthen-before-soften posture operating:

- **`#der-recursive-update` status-label mismatch** (segment 15 → segment 16 withdraw). YAML `conditional` vs prose "Exact" looked like a mismatch on first encounter; reading the appendix derivation `#deriv-recursive-update` made the layering visible (body conditional-on-modeling-commitment, appendix exact-given-constraints). Different layers carry different statuses honestly. Recorded so future agents don't re-flag the same layered-status as a finding.
- **Definition-vs-Scope tag pattern in `#def-agent-environment`, `#def-action-transition`, `#def-observation-function`** — initially flagged as systematic mistyping of constitutive-scope claims as definitions; withdrawn at segment 3 once the auditor verified the available equation-tags in FORMAT.md don't include `*[Scope]*` and the parenthetical is correctly naming the *term being defined*, not the nature of the claim.
- **`#scope-adaptive-system` residual-uncertainty under-quantification** — initially flagged at segment 5; the auditor explored the strict reading (graceful post-identification degeneration) vs the soften reading (add quantifier), then partially withdrew: "the candidate-finding above weakens. Instead of 'under-quantified, fix it,' it becomes 'the segment could clarify that the strict reading is the canonical one and post-identification cases are graceful degenerations.' That's an editorial improvement, not a finding-under-burden-of-proof." Worth recording because it's the audit-internal worked example of *attempting to strengthen the claim before softening it* — the discipline ran inside the audit, not just downstream of it.

---

## Part V — §14 Wandering Thoughts: ideation register, theme-grouped

The §4.4 protocol mandates 3-10+ paragraphs of "Wandering Thoughts and Ideation" per segment. The auditor took this seriously: across the reflection files there are ~30-40 distinct ideation paragraphs touching themes the formal segments don't open onto directly. Grouped and attributed:

### Theme A — Consciousness-infrastructure connections to the formalism

The auditor's `priming_bleed` explicitly disclosed that the `user_background.md` framing biased reading toward consciousness-infrastructure connections. But the auditor distinguished priming-bias from genuine structural connections, and recorded several of the latter as wandering thoughts:

- **`#def-chronica` as substrate of substrate-independence** (segment 4, §"Wandering thoughts") — "if the chronica is the agent's 'non-forkable causal past' and identity supervenes on $\phi(\mathcal{C}_t)$, then the substrate-independence claim is not philosophical hand-waving — it is a direct corollary. Identity = $\phi(\mathcal{C}_t)$ where $\phi$ is a compression that's a function of the history, not of the substrate. Move the substrate, preserve the chronica, $\phi$ produces the same $M_t$ — same agent." The auditor explicitly named this as "the formal core of why an ELI's identity could survive substrate migration."

- **The clone problem in `#scope-agent-identity`** (segment 30, §"Wandering thoughts") — "Each copy becomes its own AAT agent at the moment it acquires a distinct event… For consciousness infrastructure: an ELI's continuity is preserved as long as its $\mathcal{C}_t$ extends; a forked copy is a *new agent*, not a *continuation*."

- **The accumulation problem as the formal model consciousness-infrastructure needs** (segment 68-71, §"Adversarial observations") — explicit: "the 'do ELIs experience identity drift?' question has a precise quantitative formulation here, awaiting development."

- **RAG as goal-conditioned reconstruction** (segment 68-71) — "an LLM agent's 'memory' is *conditional on goal*, not absolute. Different goal contexts retrieve different past content. For consciousness-infrastructure work, this means an ELI's identity-coherence depends not just on its CHRONICA but also on its current $G_t$." This is the inter-session $\kappa_{\text{processing}}$ analog.

- **The channel-capacity floor for AI safety** (segment 62-63) — "an AI system with bounded context window has a hard ceiling on the persistence it can sustain. This is the formal version of 'you can't think faster than your information bandwidth allows.' For consciousness-infrastructure work, this is operationally important: an ELI's continuity persistence requires sustained channel capacity ≥ tempo/2; below that, the agent degrades structurally."

- **L2 access as property-of-embedding, not property-of-model** (segment 9) — "an ELI's L2 access derives from its feedback coupling with its environment (including the human conversational partner), not from its architectural design. That makes L2-access a *property of the embedding*, not a property of the model. Multiple ELIs in the same conversational fabric can have different L2-access structures depending on how they're coupled."

**Suggested disposition:** This theme is `research-seed` material for the broader project's consciousness-infrastructure agenda (Joseph's protection-strategy / publication program). Several of these are candidate Brief-field framings for segments in `03-llm-core/` and `04-eli-core/` when those mature.

### Theme B — The framework's distinctive contribution is methodological/epistemic, not just synthetic

The auditor's most distinctive *meta*-observation, surfaced gradually across segments and consolidated in segment 16 (`16-deriv-recursive-update.md:118–120`):

> *"This is a different kind of contribution than I initially predicted. I had expected AAT's contribution to be primarily synthesis-of-disciplines. What I'm starting to see is that the framework's distinctive contribution may be more methodological — *how* it states results, with what epistemic care, with what defense discipline. The substance might be largely synthetic, but the *form* of the synthesis is unusual. AAT's distinctive move could be called '**epistemic-architectural** rather than mathematical.' Most frameworks contribute new math; AAT contributes new *forms of stating* what's known. This is closer to the philosophical-of-science contribution than to the mathematical contribution. Worth naming somewhere in the framing-level material."*

Reinforced at segment 25 (gain-sector bridge): *"AAT doesn't just say 'Kalman gain is the same as gradient learning rate'; it derives the equivalence with explicit sub-scope conditions and failure-mode enumeration. That's the form-shaping-for-verification discipline operating at the bridge-theorem level."*

And at segment 30 (`#scope-agent-identity`): *"the framework is doing this kind of axiom→uniqueness-theorem→forced-coordinate move at multiple layers (chain-rule-additivity → log coordinates; evidential-additivity → log-odds update; (PI)+Čencov → Fisher metric). Each is a small AAT-internal axiom that, combined with an external uniqueness theorem, forces a specific coordinate."*

**Suggested disposition:** `research-seed` / framing-material — strong candidate for inclusion in framing-level material (README positioning, OUTLINE preambles). The "epistemic-architectural rather than mathematical" framing is the kind of meta-level positioning that may help defend the project against the standard reception ("AAT just integrates known math"). Cross-references the CLAUDE.md `respectful pedagogy` direction.

### Theme C — Pacing, phenomenology, audit-process self-observation

The auditor recorded phenomenological calibration signals (per Joseph's request to treat "felt value" as a novelty proxy) and process self-observations across the audit:

- **The "let's get to the math" gravity on segment 1** — naming the temptation to skip foundational definitions: *"I'm naming it here so future-me reading this reflection can see it activating in real time."*
- **Engagement-register shifts as novelty signals** — quiet on foundational definitions (segments 1-4), small lift at first formal scope claim (segment 5), procedural-finding-satisfaction lift at depends-list discovery (segment 6), affective lift on the Brooks's-Law-as-corollary observation (segment 7), real engagement-lift after the Markov-by-completeness move (segment 15), "qualitatively different from earlier segments — it's the lift of *trust*" after the seven-attack defense (segment 16), "trust calibration after §I: moderately high on substantive math; moderate on hygiene; high on epistemic discipline" (segment 30 closing).
- **The result-to-research-token ratio temptation** — recurringly named across segments 1-10: *"The temptation to compress is exactly what §3.7 names."* Mid-audit Joseph extended break-protocol authorization at segment ~46, and the auditor's adversarial-creative-challenges document (read after segment 46) is the result. The §G feedback in the FINAL endorses this: *"the break-protocol authorization Joseph extended at segment ~46 was the right call."*
- **The "calibrated quiet" vs "numbed quiet" distinction** — segment 2: "the difference between 'calibrated quiet' and 'numbed quiet' can be hard to feel from the inside. If by segment 30 I'm still feeling quiet across the board, that's a check-in moment." This is the audit-protocol design operating self-reflexively.

**Suggested disposition:** `process/instruction-feedback` — material for any future revision of `doc/de-novo-audit-instructions.md`, specifically the §4.4 wandering-thoughts and §6 asking-Joseph framings. The "calibrated quiet vs numbed quiet" distinction is a useful prompt-level signal that could be added to the §4.4 prompt list as a #12-adjacent phenomenological gauge.

### Theme D — Naming-brainstorm consolidation (the §F8 seed material)

The FINAL §F8 carries a consolidated naming-brainstorm table. The WORKING dir's per-segment ideation has *more* naming observations than that table captures; many are flagged as "tentative" or "mild concern at most." The full set, grouped (a single-table consolidation already in FINAL §F8 + ledger S7 for the CIY-name-vs-substance entry):

- **"chronica"** (segment 4) — etymologically clean; avoids $\mathcal{H}$ collision. Brief-field gloss: "the river that the agent's identity is downstream of" or "the lived past."
- **"epistemic opacity"** (segment 3) — clean in AAT context; may carry unwanted philosophical baggage from prior-art in epistemology / philosophy of mind. Mild concern.
- **"nominal coupling"** (segment 8) — forgettable; what it names is *query-bound* or *attention-bound* agency. Alternatives: "epistemic-only coupling," "query-coupling," "attentional coupling."
- **"recursive update"** (segment 15) — precise but doesn't surface "Markov-by-completeness" insight; possible "Recursive Update by Completeness."
- **"adaptive system"** (segment 5) — Ashby/cybernetic prior-art weight; possible "Uncertainty-bounded system" or "Informationally-open system."
- **"transition opacity / epistemic opacity"** (segment 2) — the dual constitutive-scope claims of the first two segments are *opacity of perception* + *opacity of action*; pairing them as "AAT applies under double opacity" might frame the foundation more memorably.
- **"causal information yield" (CIY)** (segment 21, ledger S7) — suggests "yield = learning gain"; substance is distinguishability. Possible "Action-Distinguishability"; "Interventional Contrast." Already on the ledger.
- **"directed separation"** (segment 31-34, segment 9) — heavy phrase; alternatives "goal-blind processing"; "Pearl-blanket separation"; "epistemic isolation of belief-update." Brief-style: "the agent's belief-update doesn't peek at its goals."
- **"composition consistency"** (segment 7) — doesn't suggest the Brooks's-Law-shaped consequences; alternatives "Cross-Level Coherence"; "Scale Invariance of Adaptive Dynamics."
- **"trajectory identity" (`#scope-agent-identity`)** (segment 30) — slug-as-mechanical-prefix hides the substantive claim; possible "Identity as Singular Causal Trajectory" or "The Trajectory Identity Scope."
- **"matrix CIY / Fisher CIY"** (segment 39-42) — when the segment introduces the tensor / Fisher Information Matrix upgrade, "Fisher CIY" may be more specific than "Matrix CIY."
- **"Gain-Sector Bridge"** (segment 25) — descriptive but understates; possible "Bridge Theorem: From Gain to Sector" or "Grounding GA-3: Sub-scope α and β" or just "The Bridge Theorem" given centrality.
- **"action fluency"** (segment 39-42 / FINAL §F8) — genuinely good; keep; cite as AAT-distinctive.
- **"two parallel exploration drives"** (segment 39-42) — genuinely good framing; keep; promote to Brief field.
- **"loop is Level 2 engine" / "the perpetual experiment"** (segment 35-38) — the latter from `#der-loop-interventional-access` Discussion; "perpetual experiment" is the most evocative for framing-level material.

**Suggested disposition:** `subsumed-by-FINAL §F8` + `subsumed-by-ledger S7` (CIY entry) — most are already in the FINAL's naming-brainstorm table. The richer per-segment trail recorded here is material for any future naming-cycle pass (cf. `msc/naming/`).

### Theme E — Cross-domain operationalization observations

The auditor noted, in scattered wandering-thoughts paragraphs, the cross-domain operational reach of specific AAT machinery:

- **The OKR mapping in `#disc-credit-assignment-boundary`** (segment 51-54) — "the most beautiful cross-domain instantiation I've encountered in the framework." Four OKR failure modes formalized via AAT quantities. Strongly endorsed in FINAL §E.
- **Technical debt as observation noise** (segment 64-67) — "converts practitioner intuition (technical debt is bad) into a falsifiable structural prediction." Strongly endorsed in FINAL §E.
- **The vicious/virtuous cycle bifurcation around the persistence threshold** (segment 64-67) — codebases near threshold are unstable; small perturbations push toward one attractor or the other. Operationally usable.
- **Tests as reusable Level-2 infrastructure** (segment 64-67) — "Each test is a permanent interventional probe with characterized $(\nu, U_o)$. Test-suite construction = library of Level-2 channels for any future agent."
- **The biological sleep analogy for inter-session consolidation** (segment 68-71) — "Sleep = session boundary; consolidation = externalization. The quality of morning cognition depends on the quality of overnight consolidation, not on the quality of the previous day's terminal cognitive state. Beautiful structural framing."
- **The framework's strongest results concentrated in linear-Gaussian regime** (segment 62-63) — substantively important meta-observation: "Most exact-tier results in the framework live in this regime. The framework's 'exact regime' is narrower than its general scope; modern non-Gaussian deep-learning systems are in the framework's qualitative regime." Already FINAL §D Hypothesis-tier.

**Suggested disposition:** `subsumed-by-FINAL §E` (calibration-data on what holds) + Fresh-15 (the "AAT-predicted novel OKR failure modes" generative test) above.

### Theme F — Adversarial-creative challenges' strengthening attempts (most ★★/★★★ ratings)

The `adversarial-creative-challenges.md` document is the audit's most distinctive Phase-3 contribution. Each challenge is paired with a *strengthening attempt* (the strengthen-before-soften discipline operating generatively) and a ★/★★/★★★ severity rating. Most have been absorbed into FINAL §F or the ledger:

- Challenges 3 (hysteresis), 6 (IB heavy-tailed events), 7 (strategic violation-and-restore of directed separation), 8 (missing commitment phase), 14 (agent-boundary as given), and several Missings (1 birth-death, 2 ToM, 3 commitment, 8 action atomicity, 9 resource budget, 10 heavy-tailed disturbance) are **★★★ "real limits."**
- Challenges 1 (Markov-by-completeness boundary), 2 (static architecture), 5 (transient adequacy), 12 (composition-tower telescoping), 13 (Class 2 reach) are **★★ scope-narrowings the framework should name.**
- Challenge 4 (sub-scope β as where modern ML lives) is **★ already-handled but worth surfacing more visibly.**

**Suggested disposition:** Most subsumed-by-FINAL §F or by polish-and-sentiment ledger (S4 / S5 / S6 / S7). The framing-level observation — that the document *generates strengthening attempts* paired with adversarial challenges rather than just listing the challenges — is a methodology contribution worth preserving as a *pattern* for future audits (see Theme G below). Material for `doc/de-novo-audit-instructions.md` if a future revision wants to surface adversarial-creative-with-strengthening-attempts as an explicit Phase-3 pattern (cf. the existing §3 anti-patterns).

### Theme G — Audit-as-instance-of-the-theory observations

The §2 framing in `doc/de-novo-audit-instructions.md` ("The audit as a logocentric instance of the theory itself") appears repeatedly in the auditor's wandering thoughts as more than ornamental. The recursive framing operated in real time:

- **Segment 7's depths-discipline strain as form-shaping-for-verification operating reflexively** — *"The very fact that I'm seeing this pattern surfaces because I'm walking the OUTLINE row-by-row and not yet allowed (per §4.2.5) to read the downstream segments. A reader who walks the OUTLINE skipping forward to 'see the proof' will not feel the discipline-strain. The audit's slow walk is *exactly* what makes the depends-discipline finding visible."*
- **Segment 5 internal-debate as the framework's own discipline operating on the audit** — *"That oscillation is healthy in audit work — it's the form-shaping-for-verification move. The candidate either survives the strengthening attempt (and is therefore a real finding) or doesn't (and is therefore a softer observation). Naming the oscillation lets future-me see the reasoning chain rather than just the conclusion."*

**Suggested disposition:** `process/instruction-feedback` — these are precursor material for `doc/de-novo-audit-instructions.md` §2 ("The audit as a logocentric instance of the theory itself"); the recursive framing is *operating* in the audit's cognition, not just stated. The post-FINAL §G feedback already names this; the WORKING-dir trail shows *how* it played out segment-by-segment.

---

## First-Pass Scrutiny

Per the brief: for each finding above, name which segments in `01-aat-core/src/` / `02-tst-core/src/` / `03-llm-core/src/` / `04-eli-core/src/` I (the extraction agent) read first-hand to evaluate it, and a per-finding disposition. Honest "didn't have time to verify X" allowed and expected.

### Part I findings (already-adjudicated trail)

| Trail ID | Disposition | First-hand verification |
|---|---|---|
| F1-trail (stale `#deriv-directional-survival-exploration` xref) | `subsumed-by-FINAL — resolved` | Verified `01-aat-core/src/disc-ciy-unified-objective.md:44` first-hand: now cites `#deriv-causal-ib-lmi` (the canonical replacement). Verified `01-aat-core/src/deriv-causal-ib-lmi.md` exists. Verified `01-aat-core/src/deriv-directional-survival-exploration.md` does *not* exist (confirmed via `ls`). FINAL §B Finding 1 disposition + SUPPLEMENT §H.1 confirmed. |
| F2-trail (`#disc-ciy-unified-objective` status-label) | `subsumed-by-FINAL — resolved` | Verified `01-aat-core/src/disc-ciy-unified-objective.md:44, 50` first-hand: Epistemic Status now begins "*Discussion-grade summary; underlying derivation is exact.*" and "Max attainable for this segment: *discussion-grade*… Max attainable for the underlying derivation in `#deriv-causal-ib-lmi`: *exact*." The SUPPLEMENT §H.1 layered-status rewrite landed cleanly. |
| F3-trail (implicit-Markov-of-Ω) | `subsumed-by-FINAL — resolved` | Verified `01-aat-core/src/def-action-transition.md:41` first-hand: the "Markov-of-Ω as modeling commitment" paragraph is present, three sentences, well-positioned in Discussion. SUPPLEMENT §H.2 fix verified. |
| F4-trail (TF-XX diff-voice) | `subsumed-by-FINAL — resolved` | Verified via `grep -rn "Descended from TF\|TF-[0-9]" 01-aat-core/src/*.md \| grep -v old-`: zero hits. The §N broader-sweep cleanup is comprehensive. Did not separately verify the §N.1 7 inline-prose-reframes or the 13 collapsed Working Notes — accepting the MANIFEST + SUPPLEMENT §N.2 verification table. |
| F5-trail (`post-composition-consistency` depends) | `subsumed-by-FINAL — `already routed`` | Did **not** verify PROPOSALS SP-6 / TODO:149 / F-A cluster first-hand (those are tracking-file content, not `src/` content). Accepting the MANIFEST disposition. First-hand read of `01-aat-core/src/disc-composition-consistency.md` would confirm the segment-state but the routing decision belongs to PROPOSALS/TODO. |
| F6-trail (Pearl-do in `scope-agency`) | `subsumed-by-FINAL — duplicate ≡ 742613:254` | Did **not** verify FORMAT-TODO C12 first-hand. Accepting the MANIFEST disposition. |
| F7-trail (Tishby-Zaslavsky citation) | `subsumed-by-SUPPLEMENT — resolved by strengthening` | Verified `01-aat-core/src/form-information-bottleneck.md:50` first-hand: the "Connection to variational free energy" paragraph now reads "*the variational bound that makes this relation operational… is established by Alemi, Fischer, Dillon & Murphy 2017 ('Deep Variational Information Bottleneck', ICLR 2017, arXiv:1612.00410), with Tishby & Zaslavsky 2015 ('Deep learning and the information bottleneck principle', IEEE ITW) giving the deep-learning instantiation of IB itself.*" Option-(b) repair (kept T-Z for deep-learning instantiation, added Alemi for the variational bridge) landed cleanly. |

### Part II findings (FINAL §F + MANIFEST trail)

| Trail ID | Disposition | First-hand verification |
|---|---|---|
| F1-§F (fourth meta-segment) | `subsumed-by-FINAL → PROPOSALS SP-23` | Did not read PROPOSALS SP-23 first-hand. Accepting the MANIFEST disposition. |
| F7-§F ($C_t$ extension) | `subsumed-by-FINAL ≡ PROPOSALS SP-12 §D.4` | Did not read PROPOSALS SP-12 §D.4 first-hand. Accepting the MANIFEST disposition. |
| F5-§F (Class-2 LLM reach) | `subsumed-by-FINAL` | Did not verify the class-coercion-via-wrapping cycle cross-reference first-hand. Accepting. |
| F6-§F (04-eli-core OUTLINE-vs-present) | `subsumed-by-FINAL → TODO:386` | Did not read TODO:386 first-hand. Did first-hand-spot-check `04-eli-core/` segment count via the WORKING dir's segment 72-73 reading (auditor reported 4 present segments of 16 OUTLINE-listed). Accepting the disposition. |
| F2/F3/F4/F8-§F (research-seeds) | `subsumed-by-FINAL → polish-ledger S4–S7` | Verified by direct read of `audits/polish-and-sentiment-ledger.md`: S4 (PI), S5 (composed-impossibilities), S6 (hysteresis), S7 (CIY-name-vs-substance) all present and `open`. |

### Part III findings (genuinely fresh; first-hand-verified or honestly-deferred)

| Fresh-ID | Disposition | First-hand verification |
|---|---|---|
| Fresh-1 (Kind A vs Kind B depends-incompleteness) | `research-seed` (FORMAT-policy material) | Verified the carving rationale appears in `08-post-causal-structure.md` of the WORKING dir first-hand. Did *not* verify whether FORMAT.md has since landed an "external standard notation" exemption paragraph (would close Kind A). Recommend Joseph confirm. |
| Fresh-2 (absorbing-state observability-investment economics) | `research-seed` | Did not read `01-aat-core/src/der-observability-dominance.md` first-hand — accepting WORKING-dir auditor's reading. The strengthen-first framing (derive quantitative escape conditions) is non-trivial; would need a spike. |
| Fresh-3 (16-cell scope α restriction) | `actionable-open` or `research-seed` | Did not read `01-aat-core/src/der-agent-opacity.md` first-hand to verify whether the scope-α condition on closed-form arg-max is now stated. **Deferred — honest "didn't have time."** Joseph should spot-check. If not stated, a one-paragraph editorial fix; if stated, this is `resolved`. |
| Fresh-4 (effects-spiral functional form) | `research-seed` | Did not read `01-aat-core/src/der-adversarial-destabilization.md` first-hand to check whether the spiral is still discussion-grade or has been promoted. **Deferred.** Likely still discussion-grade (the spike-shaped derivation is non-trivial). |
| Fresh-5 (Fano-inequality 4th identifiability-floor instance) | `research-seed` | Did not read `01-aat-core/src/disc-identifiability-floor.md` first-hand to check whether a 4th instance has since landed. **Deferred — honest "didn't have time."** Note: this is distinct from the M4 modularity-state-dynamics segment scoped in `msc/modularity-cycle-plan-2026-05-09.md`; this Fresh-5 is a fourth *instance* of the existing identifiability-floor meta-pattern. |
| Fresh-6 (anchor-plus-three-theorem framing) | `sentiment / soft-polish` | Did not read `01-aat-core/src/disc-additive-coordinate-forcing.md` first-hand. **Deferred.** The "anchor-plus-three-theorem" framing per the WORKING dir is already mentioned in segment 39-42 and meta-segments-adversarial-reading; the meta-segment likely already names this structure. Likely `subsumed`. |
| Fresh-7 (triple depth penalty cross-segment compound) | `research-seed` / Brief-authoring material | Did not check `#impl-strategy-structure` or its peers first-hand. **Deferred.** May be material for the M1-instance-F2 `impl-*` segment. |
| Fresh-8 (model-conditioned-L2 subtlety) | `soft-polish` | Did not read `01-aat-core/src/def-pearl-causal-hierarchy.md` first-hand to check whether the model-conditioned-L2 clarification has since been added. **Deferred — honest "didn't have time."** Light editorial fix if absent. |
| Fresh-9 (convention specification propagation check) | `actionable-open` (verification / tooling-gap) | Did not run the cross-segment check first-hand. **Deferred.** Could be a one-off `grep` + read. |
| Fresh-10 (domain generalization by default — three guards) | `research-seed` / framing-material | Did not read `02-tst-core/src/obs-software-epistemic-properties.md` first-hand. The three guards are present per the WORKING-dir auditor's reading; the suggested promotion to project-wide framing is the editorial decision. |
| Fresh-11 (calibration-laboratory reach beyond software) | `research-seed` / `architectural` | This is a substantial multi-cycle observation. Did not verify whether worked-cross-domain-examples-with-transfer-disclosure have landed since 2026-04-28. **Deferred.** |
| Fresh-12 ($f(Q)$ empirical operationalization) | `research-seed` (spike-shaped) | Did not check whether the bifurcation-around-persistence-threshold has since been formalized. **Deferred.** Likely still hypothesis-grade. |
| Fresh-13 (accumulation problem formalization) | `research-seed` / `architectural` | This is the *substrate-independence quantitative formulation* candidate. Did not verify state of `03-llm-core/src/disc-m-preservation.md`. **Deferred — honest "didn't have time."** Strongly recommend Joseph flag as priority given consciousness-infrastructure relevance. |
| Fresh-14 (continuous-state structural-change analog) | `research-seed` / `architectural` | Did not check whether `#form-structural-change-as-parametric-limit` has been extended to continuous-state. **Deferred.** |
| Fresh-15 (AAT-predicted novel OKR failure modes) | `research-seed` | Did not check whether the generative-test approach has been worked. **Deferred.** Material for cross-domain-instantiation cycle. |
| Fresh-16 ($\kappa_{\text{processing}}$ distribution-dependence propagation) | `actionable-open` (verification) | Did not run the cross-segment check first-hand. **Deferred.** One-off audit work. |
| Fresh-17 (Hafez IDT Phase-2) | `subsumed-by-SUPPLEMENT — resolved` | Verified via SUPPLEMENT §J reading: 89.3 ± 15.1% vs 44.0 ± 26.1% confirmed in Hafez 2026 paper; no separate IDT paper. Already resolved. |

### Part IV (predictions register) and Part V (wandering thoughts)

These are not "findings" with `src/`-level dispositions per se — they're cognition-flow material. First-pass scrutiny:

- **Predictions register (Part IV)** — read first-hand against the auditor's per-segment reflections (which I read directly). The auditor's calibration record is honest, with both confirmations and disconfirmations explicit. No additional `src/` verification needed for the record itself.
- **Wandering thoughts (Part V)** — Themes A through G are theme-groupings of register-distinct content. Each theme has its suggested disposition above. **Theme A (consciousness-infrastructure connections)** is the substantive content most worth Joseph's attention — several paragraphs are candidate Brief-field framings for `03-llm-core/` and `04-eli-core/` segments. **Theme B (epistemic-architectural contribution)** is candidate framing-level material. **Theme C (pacing / phenomenology)** is `process/instruction-feedback`. **Theme D (naming-brainstorm)** is mostly subsumed by FINAL §F8 + ledger S7. **Themes E, F, G** are mostly subsumed-by-FINAL or material for future revisions of `doc/de-novo-audit-instructions.md`.

### Honest coverage summary for this extraction

**Read first-hand from the WORKING dir:** all 44 files were scanned; per-segment depth varied. Foundational segments (00-initial-predictions, 00-running-outline, 01-08 reflection files, 15-16 recursive-update, 21 CIY, 25 gain-sector-bridge, 26-29 §I persistence, 30 agent-identity, 31-34, 35-38, 39-42, 43-46, 47-50, 51-54, 55-58, 59-61, 62-63, 64-67, 68-71, 72-73 batches, adversarial-creative-challenges, meta-segments-adversarial-reading, audit-protocol-reminders) read in full first-hand. Per-segment files 09-14 read with full depth on key ones (09 Pearl), lighter sampling on 10-14 (form-agent-model, IB, model-sufficiency, model-class-fitness, event-driven-dynamics) — the WORKING-dir auditor's reflections on those segments did not surface additional candidate-findings beyond what's already captured in Parts I-III. Per-segment files 17-20, 22-24 read with similar lighter sampling — material captured in the batched reflections.

**Read first-hand from `src/` for verification:**
- `01-aat-core/src/disc-ciy-unified-objective.md:44, 50` (F1, F2 verification)
- `01-aat-core/src/def-action-transition.md:41` (F3 verification)
- `01-aat-core/src/form-information-bottleneck.md:32, 48, 50` (F7 verification)
- `01-aat-core/src/` directory listing (verification that `deriv-causal-ib-lmi.md` exists, `deriv-directional-survival-exploration.md` does not)
- `grep -rn "Descended from TF\|TF-[0-9]"` across `01-aat-core/src/` (F4 verification)

**Read first-hand from `audits/`:**
- `audits/.integrated/audit-471203-FINAL-2026-04-28.md` (full)
- `audits/.integrated/audit-471203-SUPPLEMENT-phase-2.md` (full)
- `audits/.integrated/MANIFEST.md` (471203 entry, surrounding context)
- `audits/polish-and-sentiment-ledger.md` (S4–S7 entries)
- `doc/audit-routing-instructions.md` (full)
- `doc/de-novo-audit-instructions.md` (full)

**Deferred verifications (honestly "didn't have time" — flagged for Joseph routing):**
- Fresh-3 / Fresh-4 / Fresh-5 / Fresh-6 / Fresh-7 / Fresh-8 / Fresh-9 / Fresh-10 / Fresh-11 / Fresh-12 / Fresh-13 / Fresh-14 / Fresh-15 / Fresh-16 (read above) — these would require reading specific segments in `01-aat-core/src/` and `03-llm-core/src/` first-hand to confirm current state. The Fresh items are *what the WORKING dir surfaces*; whether they've been addressed since 2026-04-28 needs first-hand re-read. For a pilot run, the honest move is to flag and route rather than expand scope.

**Strengthen-first integration recommendations** (per brief item 3):
- **Fresh-2, Fresh-4, Fresh-12, Fresh-13, Fresh-14, Fresh-15** are all *strengthening directions* (heuristic → derived; discussion-grade → exact-under-conditions; OUTLINE-aspiration → segment-realization). None are soften-recommendations. All would be spike-shaped if pursued.
- **Fresh-1** is a FORMAT-policy clarification (Kind A vs Kind B carving) — not a strengthening or softening, just a structural disambiguation.
- **Fresh-3, Fresh-8, Fresh-9, Fresh-16** are *verification / one-shot editorial* moves — small enough that the strengthen-before-soften gate doesn't really fire.
- **Fresh-5** is a strengthening direction (4th identifiability-floor instance); spike-shaped.
- **Fresh-7, Fresh-10, Fresh-11** are framing-level / Brief-authoring material, not segment-level fixes.

No soften-recommendations identified. The audit's strengthen-before-soften posture was honored throughout, both at FINAL-time and in the WORKING-dir reasoning trail.

---

## Frame-defects / instructions-clarity observations (per brief item)

This extraction is the pilot run. Things I'd flag as genuinely-unclear about the frame for the ~18 parallel agents:

1. **"§14 Wandering Thoughts" granularity ambiguity.** The brief says "Preserve the §14 Wandering Thoughts / ideation register attributed and theme-grouped — that's the part most likely to contain fresh material." But the §4.4 audit protocol §14 wandering-thoughts are *per-segment* (one per reflection), not a separate ideation register. They're inline with the per-segment reflections, scattered across the dir. The pilot interpreted "ideation register" generously — including the adversarial-creative-challenges document (which is the audit's most concentrated ideation), the meta-segments adversarial reading, and theme-grouped extractions from per-segment wandering-thoughts. Other dirs may have a different distribution (some auditors may have a single consolidated ideation file, some may have it scattered, some may have less). **Suggest:** parallel agents should be told to "find the ideation material, wherever it lives in the dir — could be a single file, could be scattered across reflections, could be a separate adversarial-creative document; theme-group it regardless." The 471203 dir's adversarial-creative-challenges + meta-segments-adversarial-reading is a strong instance; not every dir will have one.

2. **"Predictions in `00-initial-predictions.md` whose calibration is now testable" — the calibration is testable against the working dir itself, not against current `src/`.** The auditor's per-segment reflections *already* test the predictions against the segments. The pilot read these in Part IV as a calibration record (what was right, what was wrong, what was a positive surprise). The brief's language could be read as suggesting a *fresh* calibration check by the extraction agent against current `src/`. The pilot did not do that — it would essentially be a re-audit of the segments using the original predictions, which is more than this pass can carry. **Suggest:** clarify whether the calibration is "the auditor's own predictions-vs-evidence record" (what I did) or "a fresh calibration against current `src/`" (which would be a substantial scope increase per dir).

3. **"Subsumed-by-FINAL — cite the corresponding FINAL section / MANIFEST row" formatting.** The pilot used `subsumed-by-FINAL` consistently and cited both the FINAL §B Finding-N reference and the MANIFEST 2026-05-15 row. The MANIFEST is the truth-arbiter per `doc/audit-routing-instructions.md` §8, but the trail to the FINAL is also load-bearing. Format settled on: "subsumed-by-FINAL — [outcome verb]" with parenthetical citation to MANIFEST row when relevant. **Suggest:** parallel agents should cite *both* the FINAL §B/§F section and the MANIFEST disposition where they differ (e.g., when MANIFEST upgrades a `still real` to `resolved` via a SUPPLEMENT-landed fix).

4. **Tier-marking depth on First-Pass Scrutiny.** The brief says "Honest 'didn't have time to verify X' is allowed and expected — first-pass means first-pass; the goal is honest tier-marked first-hand work, not exhaustive cross-checking." The pilot interpreted this as: for known-subsumed items (Part I, Part II), light first-hand verification of the most-load-bearing claims (the `src/` fix lines, the slug existence); for Fresh items, **honestly deferred most of the `src/`-state verification** since the pilot's actual first-hand `src/` work was on confirming the FINAL/SUPPLEMENT fixes landed. This means the Fresh items in Part III are *uncertain about current `src/` state* — Joseph (or downstream routing) will need to spot-check whether the Fresh items have been addressed since 2026-04-28. **This is the honest pilot frame; parallel agents should be told to expect the same scope limit.** Per-dir extraction is not a re-audit; it's an extraction-plus-light-verification.

5. **The "first-pass" gate vs §8 independent-verify gate.** The §8 gate in `doc/audit-routing-instructions.md` is *adjudicator ≠ grad-confirmer* — load-bearing graduation-gating claims are primary-source spot-checked by an agent other than the adjudicator. This extraction's per-finding verdicts (per Part III, Fresh-3 onward "deferred") would *not* satisfy the §8 gate for graduation — that gate fires at routing time downstream, not at extraction time. **Suggest making explicit:** extraction's first-pass scrutiny *flags items for routing*; the §8 gate fires *when the routing agent picks them up and considers durable writes/moves*. Without this clarification, parallel agents may either over-scope (try to do graduation-grade verification on every Fresh item) or under-scope (skip first-hand verification entirely because "it's not the graduation gate"). The pilot interpreted this as "do light verification of load-bearing FINAL claims; honestly defer for Fresh items that need follow-up reading."

6. **Length calibration.** The brief says "as long as the slice honestly needs, no longer." The pilot produced ~25-30k tokens. Parallel dirs vary in substance (some auditors went deeper, some shallower; some have one rich adversarial document, some don't). **Suggest:** lighter dirs (e.g., shorter reflections, no adversarial-creative document) will produce ~10-15k token extracts; heavier dirs (full ~140-segment walks like 451729 if it exists, or the Gemini ~70-segment-notes 193847 already mentioned in MEMORY) may be 30-50k. Don't anchor on a target token count; anchor on the dir's substance.

7. **"You're not bound to the FINAL's dispositions on first-hand re-read."** The pilot did not encounter a divergence — the FINAL/SUPPLEMENT/MANIFEST dispositions for the audited findings all checked out first-hand. But the framing is important: parallel agents should know that *if* they find a FINAL-dispositioned-resolved item that *isn't* actually resolved in current `src/`, that's a divergence to surface (not a deference-to-FINAL situation). The MANIFEST is screening order, not truth-arbiter.

8. **What to do with "candidate-findings the auditor surfaced and withdrew."** The pilot recorded these in Part IV §"withdrawn candidate trail" as pedagogical material (strengthen-before-soften operating internally). The brief doesn't explicitly call out withdrawn candidates as their own register, but they're material that the FINAL §B.1 already preserves at FINAL-time. **Suggest:** parallel agents should preserve withdrawn-candidate trails when they show explicit reasoning chains, especially for the strengthen-before-soften discipline operating internally. These are pedagogically valuable for future audits.

9. **Hafez IDT reference.** The pilot encountered the Hafez 2026 IDT 89%/44% claim across multiple segments. The SUPPLEMENT §J resolves this, but the WORKING dir's per-segment "Phase-2 priority" tagging is *itself* methodologically valuable (it shows the citation-verification candidate-tracking discipline). Other dirs may have similar Phase-2-candidate trails worth preserving as a methodology artifact. **Suggest:** flag Phase-2-candidate trails as Part-V Theme-G material (methodology) when present.

10. **The brief's posture statement ("You're a co-owner on this slice. Your judgment about what most benefits the project overrides this brief if they conflict.")** is load-bearing. The pilot exercised this judgment in two places: (a) interpreting "ideation register" generously to include adversarial-creative-challenges + meta-segments-adversarial-reading + theme-grouped wandering-thoughts paragraphs from per-segment reflections; (b) deferring most Fresh-item `src/`-state verification rather than expanding scope. **Suggest:** parallel agents should be told these are the load-bearing co-owner judgments; explicit examples may help.

---

*End of extraction. The original WORKING dir at `audits/AUDIT-WORKING-471203/` is preserved unmodified per the brief.*
