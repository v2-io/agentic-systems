---
source_cycle: 613842 (de-novo, 2026-04-25)
extraction_agent: Claude Opus 4.7 (1M context), sweep run
extraction_date: 2026-05-20
working_dir: audits/AUDIT-WORKING-613842/ (10 files, 927 lines)
final_of_record: audits/.integrated/audit-613842-FINAL-2026-04-25.md
manifest_entry: audits/.integrated/MANIFEST.md "2026-05-16 — Cluster B: math-heavy ledgered"
durable_ledger: audits/pending-findings-2026-04-23.md
purpose: |
  Consolidated extraction from the WORKING dir for routing through the
  standard audit-routing process. The original WORKING dir is preserved
  separately; this file is the "what is in there worth processing" digest.
  613842 is part of the cluster where the strengthen-before-soften discipline
  had maximum bite — F2 (Model-S non-exit) is the cluster's defining worked
  example: the audit asked to soften, the project instead spiked
  strengthening and landed a no-go (Cor A.1S.1 + #deriv-stochastic-non-exit).
---

# Audit-findings extract — 613842 working-dir mining

The 613842 cycle is a **small, focused, math-heavy** de-novo walk: 10 files, ~927 lines, partial-but-substantial coverage centered on Section I's persistence/mismatch/tempo chain, the Section II agency lift, and the Section III composition cluster. The auditor wrote tightly disciplined burden-of-proof reasoning trails and stayed *honestly partial* about coverage (skipping much of the Appendix-A pass, several Section III later segments, most of TST end-to-end, and the external-theorem verification pass). The cycle landed exactly three findings — F1 (`def-adaptive-tempo` definition-scope mismatch), F2 (Model-S persistence summary over-compression), F3 (C-iv strategic-composite route partial integration) — all three triple-validated against `msc/` and `audits/`, all three classified as integration-debt-with-known-repair-paths rather than as deep theory gaps.

What sets this WORKING dir apart from larger ones (193847 / 471203) is **the discipline of the cognition trail itself**: every candidate-finding shows explicit counterevidence-search, `msc/`-triangulation, status-determination, and confidence-naming before reaching the FINAL. The trail is dense rather than wide. The F2 trail in particular is the pedagogically valuable centerpiece — the audit asked for downstream summary-layer caveating, the project instead pursued an honest strengthening attempt and converged on a **no-go theorem** as the truer landing. The strengthen-before-soften discipline operating exactly as designed.

Per MANIFEST 2026-05-16 (Cluster B), all three findings are dispositioned:

- **613842-F2 ≡ 742613-F2** — *resolved by strengthening-then-no-go* (state 3). Cor A.1S.1 + `#deriv-stochastic-non-exit` landed; cascade verified clean. Spike: `spikes/spike-stochastic-non-exit-strengthening-2026-05-16.md`; CHANGELOG 2026-05-16.
- **613842-F1 ≡ 742613-F4** — *substance resolved by strengthening* (matrix-Loewner canonical; scalar = special case); narrow frontmatter/status residue tracked TODO:395/126 — *not a graduation blocker*.
- **613842-F3** — `actionable-open` via F-V3/F8 dispositions (TODO:95 + PROPOSALS SP-21 §G + ledger); same substantive concern, **triple-tracked** under the F-V3/F8 cluster name. The 613842 framing of the issue is a sharper articulation of the same hybrid integration-debt / theory-open structure.

This file extracts the WORKING dir's gold at three weights: **(1) findings already adjudicated in MANIFEST** (preserved with WORKING-dir provenance and the strengthen-before-soften reasoning trail for F2 made fully visible); **(2) fresh material the FINAL didn't carry forward** (a small, focused set — this dir is dense rather than wide); **(3) cognition-flow material** (predictions-vs-evidence calibration, withdrawn-candidates trail, process feedback to the audit instructions).

---

## Part I — Findings already adjudicated (subsumed-by-FINAL/MANIFEST)

### F1-trail. `#def-adaptive-tempo` defines an unrestricted additive scalar that the same segment later demotes to an upper bound

**WORKING-dir trail (where the finding crystallized):**

- First flagged in `02-sector-chain.md:25-52` as the "first substantial concern" of the audit — "this is currently the strongest issue in the audit so far." The auditor laid out three resolution possibilities (sub-scope restriction; upper-bound surrogate; later-segment repair); resolution path unknown at the time of surfacing.
- Continued tracking through `03-discrete-and-persistence.md:46-51`: "the presence of the caveat downstream also increases pressure on `#def-adaptive-tempo` itself: if later results have to remind readers that the base formula overcounts under correlation, the base segment likely needs narrower scope or a different formal definition." First cross-segment reinforcement.
- Defended-in-burden-of-proof form in `07-finding-verification.md:7-42` (Candidate F1): problematic passage at `def-adaptive-tempo.md:19, 44-48`; counterevidence search lists `der-team-persistence.md:32` + `result-persistence-condition.md:99` propagating the same caveat honestly; `disc-independence-audit.md:59` records the repair operation explicitly; `audits/pending-findings-2026-04-23.md:164` (line was actually different) already logs the concern.
- Final classification (WORKING-dir): **integration debt / definition-scope mismatch**, not deep theory gap. "The corpus knows the caveat, but the main definition still reads stronger than the repair."
- Promoted to FINAL §F1 with the same five-element burden-of-proof structure, **High confidence**.

**Disposition (per MANIFEST 2026-05-16 Cluster B + first-hand verification below):**

**`subsumed-by-FINAL` — substance resolved by strengthening; narrow residue tracked.** First-hand-verified `01-aat-core/src/def-adaptive-tempo.md` reads, line 19 (the unrestricted additive scalar still appears as the primary formal expression), but is now followed by lines 28–38 introducing the **tensor extension under Fisher-local invariance regime** as the canonical matrix-Loewner object, with the scalar form derived as the shared-eigenbasis collapse. Line 44 (Epistemic Status) explicitly states "*The scalar form is exact in the isotropic / shared-eigenbasis / nonredundant-channel case*… The tensor form is the natural object under anisotropic gains, Fisher-whitened updates, LMI causal-IB, and per-dimension persistence — regimes where scalar tempo overestimates effective adaptation along weak dimensions." Line 58 (Discussion §"Channel independence assumption") keeps the redundancy-penalty acknowledgment intact. Line 63 (Discussion §"Scalar vs. vector tempo") points to `#deriv-matrix-persistence-condition` as the canonical form, with the per-coordinate form as its diagonal-axis-aligned special case.

The substance is resolved: the matrix-Loewner / tensor form is the canonical object, the scalar form is its shared-eigenbasis collapse, and the segment names this dichotomy explicitly. What remains is a narrow frontmatter / status-tag question — should the frontmatter `status: exact` carry an explicit scope-tag noting that exactness is on the tensor object and the scalar is the special case? This is the residue tracked at TODO:395/126 per the MANIFEST and is **not a graduation blocker**.

**Strengthen-before-soften posture verification:** The audit asked for "either scope the equality definition explicitly to channel independence, or rename the additive scalar as an upper-bound surrogate" — both *softenings*. The project's resolution is **strictly stronger**: the matrix-Loewner / tensor form covers the general anisotropic / correlated case as the canonical object; the scalar is no longer the load-bearing primary, it is the shared-eigenbasis collapse special case. The substance is honored, the surface is honored, and the project landed past what the audit asked for. Worked instance of strengthen-before-soften.

### F2-trail. The Model-S persistence summary layer compresses away Prop A.1S's region-awareness *(the strengthen-before-soften canonical worked example)*

**WORKING-dir trail (where the finding crystallized):**

- First flagged in `03-discrete-and-persistence.md:22-46` as "Model S template compression." The auditor named the structural compression at three downstream sites (`#result-sector-persistence-template`, `#result-sector-condition-stability`, `#result-persistence-condition`) and explicitly laid out three verification steps before promotion: (1) quote exact appendix statement with line references; (2) check whether downstream Epistemic Status or Discussion counts as adequate caveating; (3) verify whether any other segment reintroduces the stopped-process qualification before operational claims.
- Defended-in-burden-of-proof form in `07-finding-verification.md:44-82` (Candidate F2): problematic passages at `deriv-sector-condition.md:184-194` (Prop A.1S region-aware form: stopped bound + mean-square persistence condition + non-exit estimate) vs `result-sector-persistence-template.md:47-49` / `result-sector-condition-stability.md:41` / `result-persistence-condition.md:27-29` (cleaner global-looking summary statements).
- Counterevidence search noted `result-sector-persistence-template.md:90` already gestures back to region-awareness ("Model S case uses the region-aware form"); the auditor classified this as **insufficient repair**, not as fully resolving the propagation.
- `msc/` diagnosis: `spikes/INDEX.md:107` and `spikes/spike-a2-prime-strengthening.md:142-143` show the project had *consciously chosen* to lift region-awareness into Prop A.1S but leave downstream consumer summaries largely unchanged. The audit's judgment differed: "I think the current repair stops one layer too early."
- Final classification (WORKING-dir): **integration debt / scope-honesty drift**, not flaw in Prop A.1S itself. **High / medium-high confidence.**
- Promoted to FINAL §F2 with diagnosis paragraph: "My audit judgment differs from the prior `msc/` judgment only on propagation depth: I think the current repair stops one layer too early."

**Audit's proposed remediation (the softening ask):**

The FINAL recommends increasing propagation depth — pushing the region-aware caveats further downstream into the summary segments' Formal Expression sections, not just their Epistemic Status / Discussion paragraphs. This is a **softening recommendation**: more caveat, more visibly, in more places.

**Project response — the strengthen-before-soften move:**

Rather than execute the audit's propagation-depth soften, the project (per MANIFEST 2026-05-16 + CHANGELOG 2026-05-16 + `spikes/spike-stochastic-non-exit-strengthening-2026-05-16.md`) attempted to **strengthen the underlying theorem itself**. The strengthening question: *can the infinite-horizon non-exit object (the cleanest form the downstream summaries were reaching for) be proved at all under Model S?*

The strengthening attempt — honest, well-documented in the spike file (`.integrated/` per MANIFEST) — **failed structurally**. The result was a **no-go theorem**: under additive stochastic forcing, $P(\tau_R \lt \infty) = 1$ for every correction strength $\alpha$ and every $\sigma_w \gt 0$, and the natural maximal-inequality route (Ville/Doob on an Itô–Lyapunov supermartingale) provably *cannot* certify any horizon-independent non-exit bound. The infinite-horizon containment object the audit (and the downstream summaries) implicitly reached for **does not exist mathematically**.

**The landing — replacement, not softened coexistence:**

Per the *integration-is-replacement* discipline (CLAUDE.md §"Landing a strengthened result"), the resolution landed as:

1. **Prop A.1S restructured** to remove the (now-known-false) infinite-horizon ever-exit claim. Current state (`deriv-sector-condition.md:180-206` first-hand-verified): the proposition statement is region-aware with **four sub-results**:
   - (i) **Stopped bound** — Grönwall on $\mathbb{E}[\lVert\delta(t \wedge \tau_R)\rVert^2]$.
   - (ii) **Mean-square persistence condition** — $R^\ast_S \lt R$ iff $\alpha \gt n\sigma_w^2/(2R^2)$.
   - (iii′) **Fixed-time tail** — $P(\lVert\delta(t)\rVert \gt R) \leq \mathbb{E}[\lVert\delta(t\wedge\tau_R)\rVert^2] / R^2$, stationary-sharp $\to n\sigma_w^2/(2\alpha R^2)$.
   - (iv) **Finite-horizon sample-path bound** — additive first-exit bound rigorous under (A2') alone, vacuous for $T \gtrsim R^2/(n\sigma_w^2)$, consistent with $P(\tau_R \lt \infty) = 1$.
   - Plus explicit prose at line 198: "*This is not an infinite-horizon containment statement: under additive Brownian forcing the diffusion is recurrent on $\mathbb{R}^n$… so $P(\tau_R \lt \infty) = 1$ over an unbounded horizon — there is no $P(\tau_R \lt \infty) \lt 1$ bound, and none is claimed.*"

2. **Corollary A.1S.1 (Disturbance-Model Containment Dichotomy)** landed as a **new exact result** (`deriv-sector-condition.md:258-268` first-hand-verified): $P(\tau_R \lt \infty)$ is exactly the two-point set $\{0, 1\}$ — 0 under Model D (positive invariance, Prop A.1), 1 under Model S (a.s. exit of a non-degenerate diffusion), **$\alpha$-invariant**, the value selected by the disturbance model's support structure rather than by correction strength. Corollary's Discussion (line 268): "*This sharpens the hand-off into #result-structural-adaptation-necessity — in any genuinely stochastic environment region-exit is a certain eventual event, so the structural-adaptation trigger is generic, not exceptional, for a sufficiently long-lived agent.*"

3. **`#deriv-stochastic-non-exit`** landed as the **Model-S no-go appendix** (verified to exist first-hand at `01-aat-core/src/deriv-stochastic-non-exit.md`, header read: *"Under additive stochastic forcing there is no finite bound on the infinite-horizon first-exit probability — $P(\tau_R \lt \infty) = 1$ for every correction strength — and the natural maximal-inequality route to one provably cannot exist; this is the load-bearing proof step behind Prop A.1S(iii′)/(iv) and the Model-S half of Corollary A.1S.1."*). The no-go is **demonstrated** (not just stated) — the "are you sure you can't just Doob/Ville this?" question is answered as part of the proof. **Status: exact**, **stage: draft**.

4. **Body + FINDINGS-catalog state present truth only.** The body of `deriv-sector-condition.md` no longer carries the audit-asked-for "Model S(iii) for the infinite-horizon ever-exit object with stronger caveats" softened ghost. It states the **new exact result** (Corollary A.1S.1) cleanly, names the no-go as a result in its own right (the dichotomy is itself the contribution), and the falsified ever-exit object has been **deleted** rather than kept-softened-with-a-pointer. The history (*"previously carried a false infinite-horizon ever-exit claim; the audit recommended a soften; the project pursued strengthening and found a no-go"*) lives **only** in CHANGELOG 2026-05-16 / `spikes/.integrated/spike-stochastic-non-exit-strengthening-2026-05-16.md` / Working Notes of the segment.

**Cascade verified clean** (per MANIFEST + verifiable from segment depends-graph): every dependent consumer (e.g., `result-sector-persistence-template`, `result-sector-condition-stability`, `result-persistence-condition`) now consumes the stopped bound / mean-square threshold / fixed-time tail — *not* the falsified infinite-horizon ever-exit object. The falsified object is propagated nowhere.

**Disposition (per MANIFEST 2026-05-16 Cluster B):**

**`subsumed-by-MANIFEST` — resolved by strengthening-then-no-go (state 3 per `doc/audit-routing-instructions.md` §8 enumerator).** The audit-asked softening was replaced with a no-go theorem that is **strictly stronger** than what the audit aimed at: not just "the summary segments need more caveat," but "the cleanest form of the object the summary segments were reaching for *cannot exist*, and the dichotomy is itself the result." The Model-S no-go is present truth on the spine (Cor A.1S.1 is in the result table at `deriv-sector-condition.md:276`), demonstrated where non-obvious (`#deriv-stochastic-non-exit` appendix), and clean on every dependent path. The discipline operated exactly as CLAUDE.md describes: refuted claim deleted, label tracks current truth-status (`exact`, not down-tiered for being new), no-go demonstrated as present truth not softened ghost.

**Pedagogical value (the reason this trail warrants detail):**

F2's trail is the **cluster B canonical worked example** of strengthen-before-soften. Three teaching moments in it:

- **The audit's "softer" recommendation was correct on its own terms** — the downstream summary segments did under-caveat the region-awareness. The audit was not wrong to flag this. It was just not as strong as the underlying theorem could be made.
- **The strengthening attempt is what surfaces the no-go**, not the softening attempt. Had the project executed the audit's recommendation directly (push more caveats downstream), the no-go would have remained hidden — the audit's repair would have been mathematically *non-monotonic* (more visible caveats around an object that cannot exist in its hoped-for form). The strengthen-first move pulled the underlying impossibility into view.
- **The no-go is itself a positive result** — the dichotomy $P(\tau_R \lt \infty) \in \{0, 1\}$ with the value selected by disturbance-model support structure is *new*, *exact*, and *operationally important* (it sharpens the structural-adaptation trigger from "exceptional" to "generic" for sufficiently long-lived agents). What looked like a softening-job was really a *missing exact theorem* — visible only after attempting to strengthen.

This trail is durable evidence-material for the strengthen-before-soften discipline's onboarding documentation (`~/.claude/memory/epistemic-discipline/strengthen-before-soften.md`, `~/.claude/memory/epistemic-discipline/integration-is-replacement.md`). The 2026-05-16 cycle landing log + this WORKING-dir trail together are the worked example named in the global-memory file.

### F3-trail. The new C-iv strategic-composite route is only partially integrated, and some downstream composition machinery still overstates what it covers

**WORKING-dir trail (where the finding crystallized):**

- First flagged in `06-composition-cross-component.md:14-32` ("Where the pressure shows"): `#scope-composite-agent` admits route (C-iv) and `#scope-multi-agent` distinguishes strategic from alignment composites, but `#form-composition-closure` still says "the three alignment routes" + ties meaningful composite status to well-defined $G_c = (O_c, \Sigma_c)$; `#def-unity-dimensions` still describes scope as a three-route disjunction; and `#deriv-strategic-composition:119, 135, 175` explicitly says the bridge from strategic composition to closure-defect machinery remains open.
- Defended-in-burden-of-proof form in `07-finding-verification.md:84-133` (Candidate F3): all six load-bearing line references quoted; counterevidence search lists the partial-propagation positives (#scope-composite-agent has route C-iv; #scope-multi-agent distinguishes; #deriv-strategic-composition is candid about open bridge); `msc/` diagnosis triangulates to `spikes/spike-strategic-composition.md:443` (open-bridge restatement) + `spikes/spike-bridge-lemma-nonlinear-strengthening-2026-04-24.md:297` (adversarial/strategic regime structurally outside contraction-template bridge) + `audits/pending-findings-2026-04-25.md:109` (SP-21 architectural restructure option).
- Final classification (WORKING-dir + FINAL): **hybrid — integration debt + theory-open component**. *"This is the most interesting finding of the pass because it is **not** just stale wording and **not** just an unproven theorem. It is a hybrid: integration debt where route-count / scope language / downstream references still reflect the older alignment-only frame; theory-open component where the closure-defect ontology genuinely does not yet fit equilibrium-statistic composites cleanly."* **High confidence.**

**Cross-cycle resonance (the reason the audit calls this "the most interesting finding"):**

The 613842 audit-finding is structurally identical to F-V3 / F8 (surfaced independently in audit 742613 + the 2026-04-22 batch). The MANIFEST 2026-05-16 Cluster C row reads: *"F-V3 / F8 (composite-agent C-iii) — `actionable-open` but **triple-tracked** (TODO:95 + PROPOSALS SP-21 §G + ledger). Graduates with the open item living in TODO/PROPOSALS, not double-tracked."* Triple-source convergence on the same hybrid issue is itself a framework-coherence signal.

Note one cross-cycle dedup subtlety: 613842-F3 names the **C-iv (strategic / equilibrium-convergent)** route as the place where composition-closure machinery overstates its scope; F-V3/F8 names the **C-iii (mutual-benefit / induced-$O_c$)** route as the locus of the same integration tension. They are *different routes within the same scope-composite-agent disjunction*, but the structural shape is identical (route admitted in the scope segment; downstream composition machinery still presumes shared-$O_c$ ontology). Both feed the same TODO:95 / SP-21 routing. The 613842 framing of the C-iv case is a sharper specification of the same hybrid pattern — both C-iii and C-iv require non-Lyapunov-on-shared-state machinery that the closure-defect segments don't yet provide.

**Disposition (per MANIFEST 2026-05-16 Cluster C + first-hand verification below):**

**`subsumed-by-MANIFEST` — `actionable-open` (triple-tracked).** The substantive disposition lives at TODO:95–104 ("Open routing decision: F8 / F-V3 — composite-agent C-iii") + PROPOSALS SP-21 §G ("Strategic-composite route as distinct theorem family"). The 613842-F3 framing of the C-iv side of this is **not separately tracked** but is **subsumed by the SP-21 framing**: PROPOSALS:359-366 explicitly treats C-iii and C-iv as parallel route-types each requiring distinct theorem families. The Path A interim editorial fix (PROPOSALS:404 — narrow editorial fixes for C-iii induced-$O_c$ and the cross-segment closure-defect references) addresses both flavors of the same integration tension.

**First-hand verification (current `src/` state):**

- `01-aat-core/src/scope-composite-agent.md` — verified at TODO:95: line 79 ("composite is 'a fiction'") still stands as live language; the F-V3 narrow editorial fix has not yet been executed. C-iv (line 46-63 per audit) is still admitted formally with the equilibrium-structure framing.
- `01-aat-core/src/form-composition-closure.md` — F3-trail-implied state ("three alignment routes" + $G_c = (O_c, \Sigma_c)$ well-definedness as scope condition) — accepting the audit's reading; did not separately verify the current segment text.
- PROPOSALS SP-21 (PROPOSALS:357-407 read first-hand) — proposal is comprehensive: explicit per-route theorem-family analysis, two-path recommendation (Path A narrow editorial fix interim + SP-21 architectural split deferred), and the §G "Recommendation: Defer SP-21 execution" landing is current.
- TODO:95-104 — present, live, names Path A as recommended interim. Not yet executed.

The 613842 cycle's contribution here is *clarifying which side of the C-iii vs C-iv distinction* is the more pressing pressure point — the audit's framing argues that the C-iv equilibrium-statistic case is structurally further from the closure-defect ontology than the C-iii relevance-variable / induced-$O_c$ case (PROPOSALS:363-366 corroborates this; the C-iv macro-object "is *not* a state-tracking object — it's an equilibrium statistic over joint policy"). This sub-distinction *within* the F-V3/F8 cluster is the WORKING-dir's incremental contribution and is **already captured** in PROPOSALS SP-21 §G.

---

## Part II — Bigger-picture observations (FINAL §"Bigger-picture assessment" + process feedback)

The FINAL has a `Bigger-picture assessment` section and a `Process feedback` section but no separate §F numbered bigger-picture findings list (unlike 471203). The substantive observations from those FINAL sections, with WORKING-dir provenance:

### BP1. The framework's strongest characteristic is local caveating discipline

WORKING-dir provenance: distributed across reflection files — `01-section-i-foundations.md:42-46` (mixed-tier honest-on-`#emp-update-gain`), `02-sector-chain.md:65-72` (`#deriv-sector-condition` and `#der-gain-sector-bridge` "stronger segments than my pre-read suspicion"), `05-agency-lift.md:50-54` (`#der-directed-separation` honesty about Class 1 / 2 scope), `05-agency-lift.md:64-72` (`#def-value-object` carefully distinguishing exact-vs-conditional, and `#form-complete-agent-state` explicitly self-correcting), `06-composition-cross-component.md:36-46` (TST/logogenic developer-agent honesty positive surprise).

**Disposition:** `subsumed-by-FINAL §"Where the framework felt strongest"` — the FINAL synthesizes the per-segment observations into the project-wide "discipline of local caveating in the best segments" framing. No separate routing needed.

### BP2. Section III is the clearest "over-ambitious relative to current segment set" area

WORKING-dir provenance: `06-composition-cross-component.md:14-32` (the C-iv integration pressure), and the FINAL §"Where the framework still feels over-ambitious relative to its current segment set" extends this with explicit list (aligned composites / mutual-benefit / strategic-equilibrium / closure-defect / contraction-bridge / signed-coupling) and the auditor's strongest bigger-picture hypothesis: *"the framework may become cleaner if it stops trying to make every composite route share the same macro-object and theorem family."*

**Disposition:** `subsumed-by-FINAL` → **routed via PROPOSALS SP-21** which is exactly the architectural restructure the auditor's bigger-picture hypothesis would produce. SP-21 is currently `defer` per PROPOSALS:404 with Path A editorial fixes as interim. The 613842-FINAL bigger-picture is **the WORKING-dir source** for one of SP-21's three independent triangulating sources (the others being 742613-F-V3 / 2026-04-22 batch F8).

### BP3. Pattern: weaknesses concentrate at "the seams" — recent additions, summary compression, ontology strain

WORKING-dir provenance: explicit synthesis in FINAL §"Where the framework felt strongest" closing paragraphs:

> *"This matters because it changes the shape of the audit: most of what I found was not 'segment says something reckless that the next paragraph denies.' The problems clustered more in: summary compression; cross-segment propagation around recent additions; ontology strain where one theorem family is being asked to cover more than it cleanly can."*

This is a *pattern* across F1 / F2 / F3 — each is a different instance of a common shape (definitional-scope drift, summary-compression drift, route-vs-machinery drift). Substantively important for any audit-methodology meta-commentary.

**Disposition:** `process/instruction-feedback` — material for any future revision of `doc/de-novo-audit-instructions.md` framing of "what kinds of findings to expect at maturity." Cross-references the 471203 cycle's similar synthesis (different concrete findings, same general pattern: most defects cluster at integration seams of recent moves, not at theoretical foundations).

### BP4. Some appendix-example findings from `doc/de-novo-audit-instructions.md` no longer survive current `src/`

WORKING-dir provenance: `06-composition-cross-component.md:36-46` (TST/logogenic propagation concern no longer live; `scope-developer-agent` now explicitly depends on `#scope-logogenic-agent` + `#def-coupled-update-dynamics` + `#obs-context-turnover`), plus FINAL §"Non-findings worth saying explicitly" extends this:
- "old TST↔logogenic propagation concern does not survive burden of proof"
- "strategic-composition sign error example appears repaired and documented as repaired"
- "discrete-time variance-gap issue cited in the instruction appendix also appears repaired in current `src`"

**Disposition:** `process/instruction-feedback` — *high-value* observation. The FINAL §"Process feedback" point 3 ("Mark Appendix A's example findings as historical calibration, not presumed-live examples") is the explicit recommendation. Marking the appendix examples as "calibration-history, may be repaired" rather than as live presumed examples would protect the de-novo audit posture itself. **Light editorial fix to `doc/de-novo-audit-instructions.md` Appendix A.**

### BP5. SCC / cycle-handling clause needed in audit instructions

WORKING-dir provenance: `00-reading-order-notes.md:5-48` documents the corpus-wide dependency analysis (142 active segments, 0 missing dependencies, 1 SCC of size 7 around the strategic-tempo cluster), and the auditor's manual break policy. Reinforced in FINAL §"Process feedback" point 1.

**Disposition:** `process/instruction-feedback` — `actionable-open` for `doc/de-novo-audit-instructions.md` revision. The break-policy recipe (read conceptual / weaker-status nodes first; read supporting derivations second; revisit and judge whether the cycle is honest support or frontmatter-design debt) is a transferable methodology contribution.

### BP6. `CLAUDE.md` bleed problem on de-novo posture

WORKING-dir provenance: `00-initial-predictions.md:6-13` explicitly logs the spoiler contamination from `CLAUDE.md` substantive architectural content. Reinforced in FINAL §"Process feedback" point 2.

**Disposition:** `process/instruction-feedback` — `actionable-open`. The auditor proposes two paths (write first half of `00-initial-predictions.md` before reading `CLAUDE.md`; or read `CLAUDE.md` but explicitly log the bleed immediately). Worth a `doc/de-novo-audit-instructions.md` revision adding either or both as explicit guidance. Note this is also consistent with CLAUDE.md's own header callout (the active-reconsideration callout from the 2026-05-19→20 cycle): the bleed problem is now structurally acknowledged in CLAUDE.md itself, though the audit-instructions side of the same problem may not yet be fully addressed.

### BP7. Component-local outline linting misreads cross-component dependencies

WORKING-dir provenance: `00-reading-order-notes.md:51-60` (component-local `bin/lint-outline` reports cross-component references as missing dependencies — corpus-wide dependency analysis is the authoritative graph). Reinforced in FINAL §"Process feedback" point 4.

**Disposition:** `process/instruction-feedback` — `actionable-open`. Either the audit-instructions should explicitly say "prefer corpus-wide dependency analysis when available" or `bin/lint-outline` should grow a cross-component-aware mode. Probably the former is faster.

---

## Part III — Fresh material the FINAL didn't carry forward

This dir is **dense, not wide**. The auditor stayed close to the three findings under burden of proof and did not generate a wide adversarial-creative seed corpus (unlike the 471203 / 193847 dirs). The fresh material is correspondingly thin. The genuinely-new observations the FINAL didn't carry forward as their own findings:

### Fresh-1. `#form-information-bottleneck` mixed-tier compression as Section I editorial-improvement candidate

`01-section-i-foundations.md:23-30, 49-51, 67-76` — the IB segment carries an exact imported theorem core + a robust-qualitative volatility-claim subclaim in the same file, with `status: exact` flattening both into one tier. The auditor's specific proposed move: **split the segment into (1) the exact imported IB statement as a pure formulation segment, and (2) the volatility / policy-relativity discussion as either a companion discussion segment or a visibly lower-tier subsection.**

The auditor explicitly classified this as a "soft" observation: *"That mixed epistemic register is honest in prose but still slightly tense at the frontmatter level (`status: exact` on a segment whose own Epistemic Status paragraph contains a weaker subclaim)."* Not promoted to a defended finding in the FINAL because the local prose-level honesty is adequate — only the frontmatter aggregation is slightly tense.

**Suggested disposition:** `soft-polish` (editorial improvement). Strengthen-before-soften check: is there a strengthening direction available? Possibly — if the volatility-with-policy claims can be derived under named conditions, the second tier promotes rather than separates. That would be a richer move than the audit's proposed split. Not spike-shaped urgent work; candidate for the next IB-area cycle.

### Fresh-2. `#def-model-sufficiency` may be over-dependent on `#form-information-bottleneck` in its frontmatter

`01-section-i-foundations.md:38-40` — the auditor's "watchpoint": *"`#def-model-sufficiency` seems semantically more independent from IB than its frontmatter suggests. The definition of a retained-predictive-information fraction does not appear to require `#form-information-bottleneck`; IB motivates why this quantity matters, but the quantity itself looks definable without first committing to the IB optimum."*

This is a *dependency-discipline* observation — the depends-list may include a motivational reference where logical dependence does not actually hold. Distinct from Kind A / Kind B depends-incompleteness (the 471203 Fresh-1 carving): this is the *converse* issue — depends-list listing something the segment doesn't logically need.

**Suggested disposition:** `actionable-open` (verification / one-shot editorial). Light first-hand re-read of `def-model-sufficiency.md` would confirm or refute. If the dependency is purely motivational, the depends-list entry should either drop or be reclassified (the FORMAT.md `depends` field is for logical dependence, not citation-strength).

### Fresh-3. `#post-causal-structure` may be doing more than the postulate names

`02-sector-chain.md:59-62` — *"`#post-causal-structure` is broader than a pure time-ordering postulate. The later Discussion starts shading toward weighting update rules by action-contingent informativeness. That is plausible, but it is more than the primitive time-arrow claim named in the postulate."*

The auditor explicitly notes this as "*Not a finding yet, just a place where interpretation may be doing extra work beyond the formal core.*" The Discussion may have absorbed downstream content that should live in a derived segment rather than in the postulate's interpretation paragraphs.

**Suggested disposition:** `soft-polish` / candidate for review during the next Section-I cycle. Worth a fresh-eyes pass: is the Discussion content a *consequence* (and belongs in a `der-*` segment) or is it *clarifying scope* (and is correctly here)? The distinction matters for the segment's role-prefix purity per the subject-noun-slug-naming discipline.

### Fresh-4. `#der-action-selection`'s candidate-finding-then-resolution as a worked example

`04-update-action-structure.md:20-44` first surfaces `a_t = π(M_t)` as a candidate finding — the auditor reads it as overclaiming general AAD action-selection law when the segment's own Discussion later admits the lift to $π(M_t, G_t)$ for actuated agents.

`05-agency-lift.md:23-44` then **withdraws the candidate** under burden of proof: `#form-complete-agent-state` explicitly says the earlier derivation is superseded after the lift to $(M_t, G_t)$. The audit reclassifies as **integration debt / first-encounter miscue, not missing theoretical resolution**, and concludes the issue should not be reported because the repair exists in current `src/`.

This is a *fully worked* internal candidate-withdrawal trail — predicting what `05-agency-lift` would find before reading it, then verifying that the prediction held. Material for the predictions-calibration register (Part IV).

**Suggested disposition:** `subsumed-by-audit-process` — not a defect, but a candidate for the predictions register. The withdrawal trail also has a secondary value: it suggests that **the first-encounter reader experience of `#der-action-selection` is misleading even though the framework's repair exists later.** If the segment's Formal Expression doesn't itself signal that the law generalizes (or doesn't itself link forward to `#form-complete-agent-state`), then the *miscue* is itself a small editorial issue. Light editorial check: does `#der-action-selection` Formal Expression / Epistemic Status carry a forward-pointer to `#form-complete-agent-state`?

### Fresh-5. The 7-segment strategic-tempo SCC is itself diagnostic

`00-reading-order-notes.md:18-28` — the SCC has seven members: `#def-strategic-tempo`, `#form-strategy-complexity-cost`, `#hyp-edge-update-via-gain`, `#scope-edge-update-causal-validity`, `#deriv-edge-credence-dynamics`, `#deriv-edge-update-natural-parameter`, `#deriv-strategy-cost-regret-bound`. The fact that the active corpus does not admit a strict global topological order is a *signal*, not just a process inconvenience — it suggests the strategic-tempo cluster's frontmatter declarations may not match the cluster's actual logical structure.

The auditor's frame is process-level ("a process-level issue because `msc/de-novo-audit-instructions.md` assumes such an order can be honored mechanically") but there's a substantive question underneath: *is the SCC the framework's actual logical structure (and the depends-graph is honest but cyclic), or is the SCC frontmatter design debt (where some `depends:` entries should drop or be re-routed)?*

**Suggested disposition:** `research-seed` — worth a focused spike. The strategic-tempo cluster is a load-bearing structural unit of §II; understanding whether its cyclic depends-structure is a feature (the seven segments genuinely co-define each other) or a bug (frontmatter overstates the cycle) is non-trivial diagnostic work. Could be a 30-60 minute spike to walk the depends-edges and decide whether each is logical or motivational.

### Fresh-6. The "prediction at burden-of-proof revisit" methodology pattern

The auditor consistently structures candidate-finding work as: (1) flag in the per-segment reflection with watchpoint framing and three-resolution-possibilities; (2) verify in subsequent segment reflections; (3) defend or withdraw under burden of proof in `07-finding-verification.md`. The trail is unusually clean — three findings raised, three findings carried through, three findings landed in the FINAL with confidence-named (one High, one High/medium-high, one High).

This is methodologically distinctive — the 613842 cycle is much smaller than 471203 but the *per-finding* discipline is tighter. Worth surfacing as a transferable audit pattern: **the three-stage progression (watchpoint → cross-segment verification → burden-of-proof defense) is a clean unit, and the size of the WORKING dir scales with the *number of stages run*, not with the *number of segments read*.**

**Suggested disposition:** `process/instruction-feedback` — material for the `doc/de-novo-audit-instructions.md` revision. Could land as either a paragraph in §4.4 (suggesting the three-stage progression) or as an explicit pattern callout in §3 (where existing anti-patterns live). The strength-of-conviction-naming + early-and-late-stage classification + `msc/` triangulation as a *unit* are the methodology contribution.

---

## Part IV — Predictions calibration register

The `00-initial-predictions.md` file makes a structured set of falsifiable predictions organized by component (§I / §II / §III / appendices) + by overclaim-risk-zone + by finding-type-distribution. The per-segment reflections and `07-finding-verification.md` test these predictions against evidence. The calibration record:

### Predictions correctly anticipated

- **Section I cleanest layer (boundary / observation / transition / chronica)** ✓ (`01-section-i-foundations.md`) — "The primitive definitions are short, legible, and mutually supportive. No immediate contradiction has surfaced."
- **`#deriv-sector-condition` more careful than casual outline reading suggests** ✓ (`02-sector-chain.md`) — "It is explicit about what is proved, what is assumed, and where AAD is importing standard mathematics rather than claiming novelty."
- **Section II strategy-DAG / edge-confidence / orient cascade as pressure points** ✓ (`05-agency-lift.md`) — directed-separation is honest; strategy-DAG appears well-scoped. The pressure showed up *at composition* rather than at strategy-DAG itself.
- **Section III as richest finding territory** ✓ — F3 is the most architecturally interesting of the three findings; the C-iv route-vs-machinery gap is exactly the "tension between scope segments and downstream composition segments" predicted.
- **Closure/contraction story relies on stronger assumption than surrounding narrative advertises** ✓ — closure-defect machinery presumes shared-$O_c$; the auditor caught this via F3.
- **`#disc-independence-audit` matters later** ✓ — predicted in `02-sector-chain.md:88-89` ("I also now expect `#disc-independence-audit` to matter later, because the tempo definition already appears to need exactly the kind of dependence-aware repair that such a segment would discuss"). Verified in `07-finding-verification.md:39` — `disc-independence-audit.md:59` is exactly the `msc/`-side repair the auditor expected.
- **Logogenic component honest about being framework-stage rather than theorem-stage** ✓ — `06-composition-cross-component.md:36-46` "*surprisingly disciplined about what survives exactly versus only approximately*."
- **04-eli-core no technical findings (no segments)** ✓ — confirmed.
- **At least one repair already in current `src/` that the audit instructions still treat as live** ✓ — confirmed three of them (TST/logogenic, strategic-composition sign error, discrete-time variance-gap).

### Predictions confirmed with adjusted shape (calibration shifts)

- **Discrete-time pedagogical segment math slip** — predicted at `#hyp-mismatch-dynamics`, `#deriv-discrete-sector-condition`, or `#detail-linear-ode-approximation`. *Not confirmed at those specific locations*; the auditor explicitly notes (`03-discrete-and-persistence.md:13-17`) that the appendix example they expected to fail (the `O((\eta^\ast)^2)` claim) appears already repaired — "prior suspicion weakened, verification deferred." What surfaced instead: **the Model-S summary-compression issue (F2) — different layer of the same family of risks.** Direction-right, location-wrong.
- **`#form-information-bottleneck` overclaim** — predicted (`00-initial-predictions.md:64-69`). Softened on read (`01-section-i-foundations.md:23-30`): the segment is "careful to distinguish 'applied external theorem' from AAD-internal novelty" but still carries a slight mixed-tier tension. **Direction-right but at editorial-not-foundational severity.** See Fresh-1.
- **Section III worked example with concrete math mistake** — predicted (`00-initial-predictions.md:106`). *Not confirmed*; the strategic-composition sign error from the audit-instruction appendix is repaired in current `src/`. Direction reasonable, but the specific shape (worked-example math mistake) didn't survive the burden-of-proof bar in this pass — the auditor explicitly did not deep-verify Section III worked examples.

### Predictions that proved correct on direction but in mixed form

- **At least one downstream Section II / TST / logogenic segment implicitly talks as if orient cascade remains exact for Class 2 architectures** — predicted (`00-initial-predictions.md:75-79`). **Not confirmed.** TST `#scope-developer-agent` honors the coupled-update caveat; the audit found the directed-separation discipline honored across the §II / §III material sampled. Prediction *not* confirmed at the audit's resolution.
- **Status-label mismatches in segments whose Formal Expression is cleaner than their actual inferential force** — predicted as one of the most likely finding-types. Confirmed at frontmatter level for F1 (`status: exact` on segment whose body downgrades to upper-bound under correlation). Lighter forms (Fresh-1, Fresh-2) also touch this. Direction-right.
- **Cross-segment drift around recent scope additions** — predicted as most likely finding-type. Confirmed by F1 (matrix-Loewner addition not fully propagated to scalar-form caveats), F2 (region-aware A.1S not fully propagated to summary layer), F3 (C-iv addition not fully propagated to closure-defect machinery). **All three findings are instances of this pattern.** Direction-strongly-right.

### Predictions calibration: the predictive shape

The auditor's predictive shape clusters into:

- **Component-level accuracy** — predictions about *what kind* of issue each component would have were strongly accurate (§I: occasional quantitative slips or mixed-tier; §II: scope-honesty drift; §III: ontology strain).
- **Specific-locus accuracy** — predictions about *which exact segments* would fail were less accurate. The audit found issues in adjacent locations more often than at the named segments. This is structurally expected: the framework's audit-resistance is uneven, and predictions can name the right class without identifying the exact instance.
- **Type-distribution accuracy** — the predicted finding-types ("cross-segment drift around recent scope additions"; "status-label mismatches"; "integration debt between AAD core, TST, and logogenic segments") were largely accurate as *types*. The two predicted finding-types that didn't surface (worked-example math mistakes; citation-verification issues) were ones the auditor explicitly deferred verifying in this pass.

### Withdrawn-candidate trail (strengthen-before-soften / verification discipline internal to the audit)

One worked example of internal candidate-withdrawal:

- **`#der-action-selection` $a_t = π(M_t)$ overclaim** — surfaced as one of the strongest candidate findings in `04-update-action-structure.md:20-44`, then **withdrawn** in `05-agency-lift.md:23-44` after reading `#form-complete-agent-state` (which explicitly supersedes the earlier derivation). Reclassified as **integration debt / first-encounter miscue, not missing theoretical resolution**, and *deliberately not reported* in the FINAL because the repair exists in current `src/`. Worth recording because it shows the audit-internal discipline of "predict → test → resolve before promoting" operating cleanly. (See Fresh-4 above for the residual editorial-improvement question that survived the withdrawal.)

---

## Part V — Wandering thoughts / methodology observations

This WORKING dir does **not** carry a §14 "Wandering Thoughts and Ideation" register in the explicit sense the 471203 cycle did. The reflection files are tightly-focused per-batch summaries; the ideation is short, instrumental ("Predictions for next segments"), and embedded inside the burden-of-proof reasoning rather than separated out as its own register.

What does carry methodological signal is the **process discipline itself**. The themes the auditor's reflection-prose surfaces, distilled:

### Theme A — The three-stage finding-progression as a unit of audit work

`01-07.md` together demonstrate a clean three-stage progression for each finding: (1) per-segment-batch *watchpoint* with three-resolution-possibilities scaffolding; (2) cross-segment verification in subsequent reflections; (3) burden-of-proof defense in `07-finding-verification.md` with the five-element structure (Problematic passage / Counterevidence search / Status determination / Confidence / Why it still stands) + `msc/` diagnosis. The three-stage progression is the *audit's unit of work* — and the dir's size scales with the number of stages run, not the number of segments read.

**Suggested disposition:** `process/instruction-feedback` (Fresh-6 above). Material for `doc/de-novo-audit-instructions.md` §4.4 revision or §3 explicit pattern callout.

### Theme B — Counterevidence search as the load-bearing audit discipline

Each `07-finding-verification.md` candidate carries an explicit **Counterevidence search** step before the status determination. The 613842 auditor does not just flag candidates — they actively look for evidence *against* their own candidate-finding before promoting it. For F1: the segment self-caveats, downstream segments propagate the caveat honestly, the auditor judges the propagation insufficient (which is *why* the candidate survives). For F2: the appendix is honest, the template gestures back to region-awareness, the auditor judges the propagation one-layer-shallow. For F3: the scope segment has the C-iv route, the strategic-composition segment is candid about the open bridge, the auditor judges the closure-defect machinery still in the older idiom.

The discipline is **not** "find what's wrong"; it's "find what survives counterevidence search." This is exactly the burden-of-proof posture `doc/audit-routing-instructions.md` §8 enforces downstream — but the 613842 WORKING dir applies it *at the candidate-promotion stage*, not just at the routing stage.

**Suggested disposition:** `process/instruction-feedback` — material for explicit callout in either `doc/de-novo-audit-instructions.md` (counterevidence-search as expected per-finding step) or `doc/audit-routing-instructions.md` (recognizing that some audit cycles already apply the burden-of-proof bar internally, which affects downstream routing weight). The 613842 cycle's findings carried into MANIFEST with relatively high disposition-confidence partly because the burden-of-proof work was already done in the WORKING dir.

### Theme C — `msc/`-as-triangulation, not as-source-of-truth

Each finding's `msc/` diagnosis section is careful to distinguish "*the corpus already knows this*" (F1 + F3 — explicit prior tracking) from "*the corpus made a deliberate-but-too-shallow propagation choice*" (F2 — the auditor differs from the prior `msc/` judgment, not from ignorance). This nuance is important: `msc/` triangulation can either confirm the finding by surfacing existing tracking, *or* sharpen the finding by surfacing a deliberate-but-disputable choice the project has made. Both are legitimate.

**Suggested disposition:** `process/instruction-feedback` — `msc/`-triangulation distinction worth surfacing in audit-instructions. Both directions of triangulation are valuable; conflating them under "`msc/` confirms the issue" loses information.

### Theme D — The honest-partial-coverage disclosure as audit-quality signal

`audit-613842-FINAL §"What I did not fully read"` is a *substantial* honest-partial disclosure: full Appendix A pass missing, several Section III later machinery segments missing, most of TST end-to-end missing, separate external-theorem verification pass missing. The honest disclosure makes the FINAL's confidence claims *more credible*, not less: when the auditor says "High confidence" on F1/F2/F3, the reader knows exactly what scope of work backed that confidence.

This is itself a form of the framework's **scope-honesty discipline operating reflexively on the audit's own work**. Worth surfacing as a pattern.

**Suggested disposition:** `process/instruction-feedback` — material for `doc/de-novo-audit-instructions.md` framing of partial-coverage disclosures. The honest-partial-coverage callout is a strength to surface and encourage, not a weakness to apologize for.

---

## First-Pass Scrutiny

Per the brief: for each finding above, name which segments in `01-aat-core/src/` / `02-tst-core/src/` / `03-llm-core/src/` / `04-eli-core/src/` *I* (extraction agent) read first-hand. Per-finding disposition using `doc/audit-routing-instructions.md` §8 enum. Honest "deferred" allowed.

### Part I findings (already-adjudicated trail)

| Trail ID | Disposition | First-hand verification |
|---|---|---|
| F1-trail (`#def-adaptive-tempo` definition-scope) | `subsumed-by-FINAL — substance resolved by strengthening; narrow residue tracked TODO:395/126` | **First-hand verified** `01-aat-core/src/def-adaptive-tempo.md` lines 1-65: line 19 (the unrestricted additive scalar primary form) still appears; lines 28-38 (tensor extension under Fisher-local invariance regime as canonical) landed; line 44 Epistemic Status explicitly names the scalar-form-as-shared-eigenbasis-collapse-special-case; lines 58 + 63 carry the channel-independence and scalar-vs-vector caveats, with line 63 explicitly pointing to `#deriv-matrix-persistence-condition` as the canonical form. Substance resolved by strengthening (matrix-Loewner canonical, scalar = special case). Per MANIFEST 2026-05-16 Cluster B. |
| F2-trail (Model-S persistence summary compression) | `subsumed-by-MANIFEST — resolved by strengthening-then-no-go` (state 3) | **First-hand verified extensively** — this is the load-bearing trail. Read `01-aat-core/src/deriv-sector-condition.md:180-308` first-hand: Prop A.1S statement now four-sub-result region-aware form (i) stopped bound, (ii) mean-square persistence, (iii′) fixed-time tail (stationary-sharp), (iv) finite-horizon sample-path bound; explicit prose at line 198 names the no-go; Corollary A.1S.1 (containment dichotomy) at lines 258-268 stated as **new exact result** with $\alpha$-invariant 2-point set $\{0,1\}$ landing; Summary of Results table at line 276 includes Cor A.1S.1 row; What Is Derived vs Chosen table at line 294 carries Cor A.1S.1 as "**Proved** — new exact result." Read `01-aat-core/src/deriv-stochastic-non-exit.md` lines 1-30 first-hand: header states the no-go cleanly, Theorem (Model-S no-go) stated *[Derived]* with the full no-existence-of-supermartingale-route-to-bound clause, "Why the natural route cannot work" subsection states *"The route a careful reader reaches for first is a time-uniform maximal inequality (Ville / Doob) on an Itô–Lyapunov supermartingale — the same instinct that makes the fixed-time mean-square bound (Prop A.1S(i)) succeed. It fails, and the failure is structural, not a matter of a missing trick."* The strengthen-before-soften discipline operated correctly downstream — the audit's softening recommendation was replaced with a strengthening attempt that yielded a no-go theorem, the no-go is demonstrated as present truth (not softened ghost), and the cascade is clean. |
| F3-trail (C-iv strategic-composite route partial integration) | `subsumed-by-MANIFEST → triple-tracked via TODO:95 + PROPOSALS SP-21 §G + ledger` (actionable-open) | **First-hand verified PROPOSALS SP-21 §G** at PROPOSALS:357-407: comprehensive proposal, four-route theorem-family analysis explicitly treats C-iv as equilibrium-statistic-over-joint-policy (not state-tracking object), recommends Path A narrow editorial fix + defer SP-21 architectural restructure. **First-hand verified TODO:95-104**: open routing decision present, Path A recommended interim, Path B/SP-21 marked deferred. Did **not** separately verify current text of `01-aat-core/src/form-composition-closure.md`, `01-aat-core/src/def-unity-dimensions.md`, `01-aat-core/src/deriv-strategic-composition.md` — accepting WORKING-dir auditor's first-hand reading + the FINAL's verification; the routing tracking captures the substantive disposition. |

### Part II findings (bigger-picture observations)

| Trail ID | Disposition | First-hand verification |
|---|---|---|
| BP1 (local caveating discipline as strongest characteristic) | `subsumed-by-FINAL — synthesis observation, no routing needed` | Accepting FINAL synthesis directly. The first-hand verification I *did* do (Cor A.1S.1 + non-exit appendix; `def-adaptive-tempo` tensor extension; PROPOSALS SP-21) gives independent confirmation of the local-caveating-discipline pattern. |
| BP2 (Section III over-ambitious; SP-21 hypothesis) | `subsumed-by-PROPOSALS SP-21 §G` (deferred) | First-hand verified SP-21 is comprehensive; the bigger-picture hypothesis lands as the architectural-restructure option. |
| BP3 (weaknesses cluster at seams) | `process/instruction-feedback` | No `src/` verification needed; cross-cycle pattern observation. |
| BP4 (audit-instructions appendix examples no longer live) | `process/instruction-feedback — actionable-open` | Did not separately verify `02-tst-core/src/scope-developer-agent.md`'s current depends/distinctions (accepting WORKING-dir reading); the discrete-time variance-gap and strategic-composition sign error verifications would require re-reading the relevant appendix segments. **Deferred — light editorial work on `doc/de-novo-audit-instructions.md` Appendix A.** |
| BP5 (SCC / cycle-handling clause in instructions) | `process/instruction-feedback — actionable-open` | The corpus-wide dependency analysis is a methodology contribution. Did not separately re-run the 142-segment dependency walk. **Deferred — short editorial work on `doc/de-novo-audit-instructions.md` §4 or §5.** |
| BP6 (CLAUDE.md bleed problem) | `process/instruction-feedback — actionable-open` | The active-reconsideration callout at the top of CLAUDE.md (added in the 2026-05-19→20 cycle per the repo's recent commits) partially addresses this from the CLAUDE.md side. The audit-instructions side may still need its own callout. **Deferred — short editorial check + possible matched-pair update.** |
| BP7 (component-local outline linting misreads cross-component) | `process/instruction-feedback — actionable-open` | `bin/lint-outline` behavior verified at the component-local level (the WORKING-dir auditor's reading is consistent with the existing tool behavior). **Deferred — either audit-instructions revision or `bin/lint-outline` enhancement.** |

### Part III findings (genuinely fresh)

| Fresh-ID | Disposition | First-hand verification |
|---|---|---|
| Fresh-1 (`#form-information-bottleneck` mixed-tier compression) | `soft-polish` — possibly `research-seed` if strengthening direction explored | Did not separately re-read `01-aat-core/src/form-information-bottleneck.md` — accepting WORKING-dir reading. Light editorial fix or richer strengthening attempt is the choice; not a graduation blocker. **Deferred — minor editorial work.** |
| Fresh-2 (`#def-model-sufficiency` over-dependent on IB in frontmatter) | `actionable-open` (verification / one-shot editorial) | Did not separately re-read `01-aat-core/src/def-model-sufficiency.md` to confirm depends-list current state. **Deferred — light editorial check.** |
| Fresh-3 (`#post-causal-structure` doing more than the postulate names) | `soft-polish` — candidate for next §I cycle review | Did not separately re-read `01-aat-core/src/post-causal-structure.md`. **Deferred — fresh-eyes pass during next §I cycle.** |
| Fresh-4 (`#der-action-selection` first-encounter miscue) | `subsumed-by-audit-process` + possible `soft-polish` (forward-pointer to `#form-complete-agent-state`) | Did not separately re-read `01-aat-core/src/der-action-selection.md` to confirm whether it currently carries the forward-pointer. **Deferred — light editorial check.** |
| Fresh-5 (7-segment strategic-tempo SCC as substantive signal) | `research-seed` (focused 30-60 min spike) | Did not separately re-walk the SCC's depends-edges. The SCC is durable infrastructure (still present per `00-reading-order-notes.md`). **Deferred — spike-shaped.** |
| Fresh-6 (three-stage finding-progression methodology pattern) | `process/instruction-feedback` | No `src/` verification needed. Material for `doc/de-novo-audit-instructions.md` revision. |

### Part IV (predictions register) and Part V (wandering thoughts)

Not "findings" with `src/`-level dispositions — cognition-flow material:

- **Predictions register (Part IV)** — read first-hand against the auditor's per-segment reflections. The auditor's calibration record is honest: most direction-level predictions confirmed; some specific-locus predictions adjacent-but-not-exact; a few predicted finding-types not confirmed because the auditor explicitly deferred verifying them. No additional `src/` verification needed for the record itself.
- **Wandering thoughts / methodology (Part V)** — Themes A through D are methodology observations. **All four are `process/instruction-feedback`** — material for `doc/de-novo-audit-instructions.md` revision (especially Themes A, B) and `doc/audit-routing-instructions.md` revision (especially Theme C). Theme D (honest-partial-coverage disclosure) is a strength to surface and encourage.

### Honest coverage summary for this extraction

**Read first-hand from the WORKING dir:** all 10 files (927 lines) read in full first-hand. The dir is small enough that full-coverage was easy.

**Read first-hand from `src/` for verification:**

- `01-aat-core/src/def-adaptive-tempo.md` lines 1-65 (F1 verification — tensor extension landed, scalar-form-as-special-case framing landed, scope language landed)
- `01-aat-core/src/deriv-sector-condition.md` lines 180-308 (F2 verification extensively — Prop A.1S region-aware four-sub-result form, Cor A.1S.1 dichotomy as new exact result, Summary table + Derived-vs-Chosen table both updated)
- `01-aat-core/src/deriv-stochastic-non-exit.md` lines 1-30 (F2 no-go appendix verification — exists, Theorem stated, "why the natural route cannot work" subsection present)
- Did **not** separately verify F3-implied current text of `form-composition-closure.md` / `def-unity-dimensions.md` / `deriv-strategic-composition.md` — accepting the routing layer (PROPOSALS SP-21 §G + TODO:95) as the appropriate venue for substance.

**Read first-hand from `audits/`:**

- `audits/.integrated/audit-613842-FINAL-2026-04-25.md` (full)
- `audits/.integrated/MANIFEST.md` (Cluster B + Cluster C sections containing 613842 dispositions, plus surrounding context)
- `audits/audit-findings-471203.md` (pilot — full read for shape)
- `audits/polish-and-sentiment-ledger.md` (spot-checks for 613842-relevant entries; none specific to this cycle's findings)
- `audits/pending-findings-2026-04-23.md` (lines 156-175 for F1 substrate)

**Read first-hand from project-root:**

- `TODO.md:95-104` (F3 / F-V3 / F8 cluster open routing decision)
- `PROPOSALS.md:52-62, 359-407` (SP-21 / F3 architectural restructure proposal + bundle-2 cross-reference)

**Deferred verifications (honestly "didn't have time" — flagged for downstream routing):**

- Fresh-1 / Fresh-2 / Fresh-3 / Fresh-4 — each would require a re-read of one specific Section I segment. The judgments are light-editorial; the cycle of reading + verifying would not change the disposition (`soft-polish` or `actionable-open`).
- Fresh-5 — focused spike-shaped verification work (re-walk the 7-segment SCC's depends-edges with explicit logical-vs-motivational judgment per edge). Genuinely deferred.
- BP4 / BP5 / BP6 / BP7 — `doc/de-novo-audit-instructions.md` revision work, deferred to downstream routing.

**Strengthen-first integration recommendations** (per brief item 3):

- **F1 is the worked example of strengthen-before-soften's quieter form** — the audit asked for "scope or rename"; the project landed the matrix-Loewner / tensor canonical form, with the scalar as its shared-eigenbasis collapse special case. *Substance strictly stronger* than what the audit asked.
- **F2 is the worked example of strengthen-before-soften's headline form** — the audit asked for downstream summary-layer caveating; the project pursued strengthening, hit a no-go, and the no-go landed as a new exact result (Cor A.1S.1) + dedicated appendix (`#deriv-stochastic-non-exit`). The cycle is documented in CHANGELOG 2026-05-16 and is the canonical worked example named in global-memory `~/.claude/memory/epistemic-discipline/integration-is-replacement.md`. **No softening was performed; the falsified ever-exit object was deleted; the no-go is demonstrated as present truth.** The integration-is-replacement discipline operated exactly as designed.
- **F3 is the worked example of "actionable-open with strengthening-direction still on the table"** — Path A (narrow editorial fix) is the soften-equivalent interim; Path B / SP-21 (architectural restructure giving each route its own theorem family) is the strengthening direction. The current state is `defer SP-21 + execute Path A`, which honors strengthen-first by *keeping the strengthening direction live in PROPOSALS rather than collapsing to Path A* — but Path A still hasn't executed. Per integration-is-replacement, when Path A lands it should *delete* the cross-segment contradictions rather than soften them with cross-references back to the original framing.
- **Fresh-1 (IB mixed-tier)** offers a *strengthening* path (derive the volatility-with-policy claims under named conditions) richer than the soft-polish-only path (just separate the tiers). Worth noting in the next IB cycle that both moves are available.
- **Fresh-5 (SCC as substantive signal)** is a strengthening-direction observation — the SCC may name actual logical structure (and the framework would strengthen by either acknowledging the cycle as a feature or finding a non-cyclic factoring). Not a softening question.
- **BP4 / BP5 / BP6 / BP7** are documentation-layer fixes — strengthen-first doesn't fire strongly there.

No soften-recommendations identified that weren't replaced with strengthening-direction work. The audit's strengthen-before-soften posture was honored throughout, both at FINAL-time (the auditor classified each finding by *kind of issue* and left routing open) and downstream (F1 + F2 resolved by strengthening; F3 keeping strengthening on the table via SP-21 deferred).

---

## Frame-defects / instructions-clarity observations (per brief item)

The 471203 pilot raised ten frame-defect observations. The 613842 dir is small enough that fewer come up, and the pilot's observations cover most of them. The 613842-specific additions:

1. **Per-dir density-vs-breadth variation.** 613842 is **dense, not wide** — 10 files, 3 findings, ~927 lines, each finding triple-stage-disciplined. 471203 was the opposite — 44 files, 7 §B findings + 8 §F observations + adversarial-creative-challenges + meta-segments-adversarial-reading, ~3900 lines, more breadth, less per-finding depth. Both shapes are legitimate audit work. **Suggest:** parallel extraction agents should be prepared for both shapes — dense-narrow dirs produce shorter Part III (fresh material) sections because the auditor stayed close to the burden-of-proof bar, and that's not a defect of the dir.

2. **F2-style strengthen-before-soften trails warrant disproportionate treatment.** The brief flags this for 613842 specifically. The judgment is correct — the F2 cycle is **the** worked example of strengthen-before-soften operating downstream of an audit's softening recommendation. Treating F2 with deeper treatment (full reasoning trail, first-hand verification of both the no-go appendix and the rewritten proposition, integration-is-replacement discipline check) is *proportional to its pedagogical value*. The brief's instruction to do this was the right call.

3. **The MANIFEST's dedup rule is itself signal.** The MANIFEST 2026-05-16 Cluster B row reads: *"613842-F2 ≡ 742613-F2 — same segment-state; the precise ever-exit-conflation reading governs the dedup."* This is sharper-than-typical dedup language — it names *what made the dedup possible* (the precise ever-exit-conflation reading from 742613-F2 + the matched segment-state from 613842-F2 = same finding). Per `doc/audit-routing-instructions.md`, dedup like this should preserve both source citations even when the substantive disposition is shared. **Suggest:** parallel extraction agents should preserve cross-cycle dedup signals where they exist; the MANIFEST is the primary venue but the per-cycle extraction file should reference the dedup explicitly (as I've done in F2-trail above and in F3-trail's "cross-cycle resonance").

4. **The "actionable-open" disposition has a specific failure mode worth naming.** F3 is `actionable-open` (triple-tracked TODO:95 + PROPOSALS SP-21 §G + ledger) but the Path A narrow editorial fix has not yet executed. There is a real risk that `actionable-open` dispositions get *forgotten* — the routing fired correctly, but the routed work doesn't. **Suggest:** parallel extraction agents should explicitly check `actionable-open` items against current `src/` to see whether the routed work has landed since the disposition was made. For 613842-F3, the Path A fix has not yet landed — line 79 of `scope-composite-agent.md` ("composite is 'a fiction'") still stands per TODO:95. Surfacing this here as a *standing item check*, not a divergence.

5. **The "honest deferred" pattern from the pilot worked.** For Fresh-1 / Fresh-2 / Fresh-3 / Fresh-4 / Fresh-5, I deferred specific `01-aat-core/src/` re-reads rather than expanding scope. The pilot's framing of this as "extraction's first-pass scrutiny flags items for routing; the §8 gate fires when routing agent picks them up" is operationally correct — this extraction's job is consolidation, not re-audit. The pilot's frame-defect observation #4 is fully validated here.

6. **The "process feedback" weight in this dir is unusually high.** Of the 7 bigger-picture observations and the 4 wandering-thoughts themes, **most are `process/instruction-feedback`** — material for `doc/de-novo-audit-instructions.md` and `doc/audit-routing-instructions.md` revisions rather than for theory or `src/` changes. The 613842 cycle was *highly* informative for the audit instructions themselves; this is consistent with the cycle being a tight, well-disciplined audit operating against a slightly noisy instruction set. **Suggest:** parallel extraction agents should be alert to dirs where the process-feedback density is high — those are the dirs whose primary contribution is methodology refinement rather than theory refinement, and they deserve their own routing channel (toward instructions-revision tasks rather than theory-revision tasks).

---

*End of extraction. The original WORKING dir at `audits/AUDIT-WORKING-613842/` is preserved unmodified per the brief.*
