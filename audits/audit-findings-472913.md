---
source_cycle: 472913 (de-novo, Claude Opus 4.7, 2026-05-15)
extraction_agent: Claude Opus 4.7 (1M context), parallel-sweep slice
extraction_date: 2026-05-20
working_dir: audits/AUDIT-WORKING-472913/ (18 md files; segments 01–15 of AAT volume only)
final_of_record: NONE — the WORKING dir IS the audit record (no FINAL was authored)
scope_modification: Joseph restricted scope to AAT (`01-aat-core/`) only; audit did not reach 02-tst-core / 03-llm-core / 04-eli-core
cadence_modification: lighter reflections from seg 12 onward (Joseph 2026-05-15: "lighter reflections, ~1–2 diagrams per chapter")
purpose: |
  Consolidated extraction from the WORKING dir for routing through the standard
  audit-routing process. Because no FINAL exists, every substantive observation
  in the WORKING dir is a candidate-fresh finding awaiting routing — the
  subsumed-vs-fresh distinction collapses here. This file is the "what is in
  the dir worth processing" digest. The original working dir is preserved
  unmodified per the gold-standing gate.
---

# Audit-findings extract — 472913 working-dir mining

The 472913 cycle was a **partial, deep de-novo walk**: ~15/130 AAT segments covered first-hand (all of Chapter 1 — segs 01–08; all of Chapter 2 — segs 09–13; start of Chapter 3 — segs 14–15). Per-segment reflection files for each, plus a 339-line `00-initial-predictions.md` with 7 explicit falsifiable bets (B1–B7), a 259-line `00-running-outline.md` carrying a live findings ledger / threads register / strategic-loop checkpoint log, and a `00-diagram-conventions.md` capturing Joseph's two-layer-anchor-plus-skeleton diagram decision. Diagrams compiled (TikZ → PDF + PNG) for segs 01–11; segs 12–15 mostly skipped per the lighter-cadence pivot. The auditor stopped at seg 15 — coverage 15/~130 AAT segments; no Part-II/III material reached; no `result-structural-adaptation-necessity` audit; no `deriv-sector-condition` audit; no `deriv-graph-structure-uniqueness` audit. The audit is genuinely partial relative to its initial scope and never produced a FINAL report.

What the WORKING dir adds is therefore **a deep slice of Chapter 1/2 cognition** rather than a full audit: four findings under burden of proof (F1 *rescinded*, F2, F3, F4) plus one tooling-gap recommendation (TG1); two clean dissolved-on-search candidates (THREAD-B, F1) showing the burden-of-proof gate visibly working twice; a substantive Phase-3 hypothesis (defects = unnamed-or-WN-only relocation targets, clustered at forward-pressured load-bearing hinges); and a calibration record on the 7 initial-prediction bets, several of which never got to fire because the audit didn't reach the relevant segments. The honest framing: this is a deep first-third audit, not a complete one.

Because there is no FINAL, no §F bigger-picture-formalization, and no MANIFEST disposition row, **every observation here is candidate-fresh** — there is no Part I / Part II subsumed-by-FINAL bucket. Structure: Part III findings (themed); Part IV predictions-calibration (the auditor's own record); Part V §14 wandering-thoughts theme-grouped. First-Pass Scrutiny appended.

---

## Part III — Findings (all fresh — no FINAL exists to subsume them)

### Theme 1 — The four findings under burden of proof (the WORKING-dir's primary deliverable)

#### F2 — `post-composition-consistency` carries a downstream-derived result on a Chapter-1 postulate

- **Severity:** **High.** Type: `dependency-graph / scope-status / structural-placement`.
- **The defect.** `01-aat-core/src/disc-composition-consistency.md` is a Chapter-1 postulate (`type: postulate`, `status: axiomatic`, `stage: deps-verified`, `depends: [scope-agency]`). Its Formal Expression contains a `*[Derived (Conditional on Tier 1M + admissible composition topology, from #result-contraction-template (CC-parallel)/(CC-cascade)/(CC-feedback))]*` tag deriving closed-form composite contraction rates ($\lambda_c = \min_i \lambda_i$ etc.) from `#result-contraction-template` (Appendix A) plus chained Section-III slugs (`#scope-composite-agent`, `#form-composition-closure`, `#der-team-persistence`, `#der-tempo-composition`). **None of those slugs are in `depends:`.** A `deps-verified`-stamped segment is asserting a `*[Derived]*` result from premises ~100 OUTLINE rows downstream.
- **Why it's a real finding against the framework's own bar.** (1) FORMAT.md Gate-1 cond-4 explicitly requires: "if the Formal Expression uses a quantity defined elsewhere, that slug appears in `depends:`." Here the `*[Derived]*` tag *names its derivation source by slug* — Gate-1 cond-4 fails at the strongest possible point. (2) Epistemic-tag inversion: FORMAT.md defines `*[Derived]*` as "logical consequence of **prior** claims"; here the premises are ~100 segments *downstream*, not prior in any ordering. (3) The OUTLINE's own "*(possibly out of place)*" self-flag *understates* the problem — the postulate-core is not out of place; the *accreted* `*[Derived]*` result is.
- **Strengthen-first analysis.** Per CLAUDE.md, the first move is to ask whether the strong content survives. **It does** — the segment's own Working Notes document a successful strengthening (heuristic bound to the (CC-*) closed forms via DA2'-inc ≡ (CT2)-at-$M=I$ equivalence). The math is sound (auditor spot-checked (CC-parallel) and the (CC-feedback) determinant-positivity shape; both correct). So F2 is **purely structural / placement**, not a content defect. The strong fix is **split, not soften:** keep the postulate in Ch.1 (`axiomatic`, `depends: [scope-agency]`, no `*[Derived]*`); migrate the Tier-1M $\lambda_c$ result + screening test into Section III / Appendix A where its premises are prior. This *also discharges the OUTLINE's own "possibly out of place" self-flag* precisely — by separating the postulate (correctly placed) from the derived consequence (currently mis-placed).
- **Strength-relative-to-house-style.** Seg-08 (`post-causal-structure`) is the in-corpus standard for a clean Ch.1 postulate: axiomatic, no `*[Derived]*` tag, consequences previewed via legitimate Discussion `#`-refs. F2 is a deviation from that demonstrated standard, not the house style.
- **Confidence:** *High* on factual structure (frontmatter, eq-tag text, OUTLINE positions, all first-hand). *High* that the defect exists against the framework's own Gate-1 + tag discipline.
- **Status as of 2026-05-20 (this extraction):** Verified `still real` first-hand against current `01-aat-core/src/disc-composition-consistency.md` — the `*[Derived (Conditional on Tier 1M + admissible composition topology, from #result-contraction-template (CC-parallel) / (CC-cascade) / (CC-feedback))]*` tag is still on the postulate; `depends:` is still `[scope-agency]` only; none of `result-contraction-template`, `form-composition-closure`, `der-team-persistence`, `der-tempo-composition`, `scope-composite-agent` is in `depends:`. The Working Notes' strengthening-attempt-outcome paragraph is also still present. Nothing has changed since 2026-05-15.
- **Anchor.** `01-aat-core/src/disc-composition-consistency.md` §"Formal Expression" lines 36–44 + frontmatter `depends:` line 5–6; cross: OUTLINE rows for `#result-contraction-template` (Appendix A) and `#form-composition-closure` / `#der-tempo-composition` (Section III).
- **Source-file:lines** in WORKING dir: `07-post-composition-consistency.md:1–218` (full segment-7 reflection, the densest in the dir); reaffirmed at `14-the-cycle-in-motion-intro.md:62–76` (under the F1-dissolving external-notation convention, F2 *sharpens* — the framework has a careful external-citation convention, which makes the internal-slug forward-derivation a cleaner deviation).
- **Suggested disposition:** `architectural`→PROPOSALS (segment split + OUTLINE + deps reconciliation; non-trivial). Could alternatively be `actionable-open`→TODO if the split is treated as editorial; the auditor judged it `architectural` because it touches both segment structure and OUTLINE row order. **Effort:** content needs no new math (Working Notes' strengthening already done); the work is structural reorganization.

#### F3 — "Nominal" denotes **opposite scope-membership** across two adjacent foundational scope segments

- **Severity:** **Medium-Low.** Type: `cross-segment-contradiction / doc-rot (terminology)`.
- **The defect.** First-hand verbatim cross-quote:
  - `scope-agency.md:39`: "**Nominal agents** ($P(o \mid do(a)) = P(o \mid do(a'))$ for all $a, a'$): Have choices that make no difference. … Same as passive observers for AAT's purposes: adaptive only." → *"nominal" ⇒ outside agency.*
  - `post-causal-structure.md:35`: "**Nominal coupling** ($a_t$ negligibly affects $\Omega_{t+1}$, but the agent's *choice of what to observe* produces distinguishable observation distributions): … still within scope — the agent's query actions generate weak but nonzero interventional contrasts. The theory applies." → *"nominal" ⇒ inside agency.*
  - `post-causal-structure.md`'s "Zero coupling" row is the category that *actually equals* `scope-agency`'s "nominal agents."
- **Within-segment drift.** `post-causal-structure.md` bullet says "Nominal coupling" but its own later prose calls the same concept "**query-only coupling**" ("…through weak coupling … to *query-only coupling* (choosing which question to ask)"). The better term is already latent in the segment's own prose.
- **Why it matters despite low severity.** "Nominal" is not decorative prose — it is a *scope predicate* sitting on the exact agency/adaptive seam that the entire Part-II scope-lattice rotates on. A theory whose central discipline is scope-honesty cannot afford its scope vocabulary to denote opposite memberships in adjacent foundational segments. There is no LEXICON.md "nominal" entry, so there is no canonical anchor — drift is structurally more likely.
- **Strengthen-first.** Neither claim is wrong about its spectrum point. The fix is purely terminological, and the better term is already in `post-causal-structure`'s own prose: rename the bullet "Nominal coupling" → "**query-only coupling**" (self-consistent), and either keep "Zero coupling" or align `scope-agency`'s "nominal agents" → "zero-coupling agents." Consider a LEXICON entry to prevent recurrence.
- **Status as of 2026-05-20:** Verified `still real` first-hand (`grep -n "nominal"` confirmed both verbatim instances unchanged).
- **Anchor.** `scope-agency.md:39` "Nominal agents"; `post-causal-structure.md:35` "Nominal coupling" / "Zero coupling" / "query-only coupling" (in the prose just below the bullet list).
- **Source-file:lines** in WORKING dir: `08-post-causal-structure.md:32–86` (full F3 workup).
- **Suggested disposition:** `actionable-open`→TODO (editorial rename in 1–2 segments). Sub-disposition: `actionable-open` for a LEXICON entry to prevent recurrence (`vocabulary-gap`).

#### F4 — Ordinal-state vs metric-tempo seam: load-bearing content lives only in `def-chronica` Working Notes

- **Severity:** **Low** (substance known in WN + NOTATION partial cover; integration debt not theory gap). Type: `cross-segment / integration-debt / doc-rot`.
- **The structural fact (all first-hand, published sections).**
  - `def-chronica.md` (Formal Expression, published): $\mathcal C_t = (o_1, a_1, \ldots, o_t)$ — purely **ordinal**, no timestamps.
  - `form-agent-model.md` (Formal Expression, published): $M_t = \phi(\mathcal C_t)$ — function of ordinal chronica, **$\tau$-blind by construction.**
  - `form-event-driven-dynamics.md` (Formal Expression, published): event stream $\mathcal E = \{(e_i, \tau_i)\}$ with **metric** $\tau$; channel rate $\nu^{(k)}$ = events per unit *time*; (Discussion) $\nu_{\text{eff}} = \sum_k \nu^{(k)} \eta^{(k)\ast}$ identical to adaptive tempo $\mathcal T$.
  - NOTATION.md: $\mathcal T$ is inverse-time, $\rho$ is surprise·time$^{-1}$ — the persistence inequality $\mathcal T > \rho/R$ is **metric**.
- **The seam.** The framework's central capacity variable $\mathcal T$ is **metric**; the agent's state $M_t = \phi(\mathcal C_t)$ is **ordinal**. The **relationship** ($\mathcal C_t$ = ordinal content of $\mathcal E$ with $\tau$ dropped) and the **load-bearing consequence** ($M_t$ is $\tau$-blind; the persistence inequality lives in analyst-frame metric time while the state it constrains is subjective-ordinal; sleeping/paused agents have invisible-at-sequence-level / violent-in-$\delta$ gaps) appear in **no published section** of any of these segments. They appear *only* in `def-chronica.md` §"Open question: chronica as ordinal sequence vs metric timeline" (a Working-Notes-style section, lines 53–61) and *partially* in NOTATION.md's $t$-vs-$\tau$ subscript disambiguation.
- **Why it matters.** The shadow of this seam is the "waking in the dark" phenomenology that the ELI/Three-Deaths work cares about deeply — an ordinal agent discovering a metric gap through $\delta$. The framework's own `def-chronica` open-question section names this precisely (verbatim: *"the agent's chronica indexing makes the temporal gap invisible at the sequence level but violently apparent in the mismatch signal"*) and then the published theory drops it. If one paragraph were lifted from `def-chronica` Working Notes to published prose, it would retroactively sharpen persistence (metric), chronica (ordinal), and the Three-Deaths bridge in one move.
- **Strengthen-first.** Not a content error to soften — the pieces are individually correct. Strengthen-fix = one *published* paragraph (best in `form-event-driven-dynamics` Epistemic Status, or a published note in `def-chronica`) stating the ordinal/metric relationship and the metric-inequality-on-ordinal-state consequence.
- **Status as of 2026-05-20:** Verified `still real` first-hand. `def-chronica.md:53–61` carries the open-question section; `form-event-driven-dynamics.md` has zero occurrences of "ordinal" or "chronica" (grep) — no published reconciliation.
- **Source-file:lines** in WORKING dir: `04-def-chronica.md:40–47` (THREAD-D first surfaced); `15-form-event-driven-dynamics.md:1–129` (full F4 workup; THREAD-D resolved into it).
- **Anchor.** `def-chronica.md:53–61` Working-Notes-style §"Open question: chronica as ordinal sequence vs metric timeline"; `form-event-driven-dynamics.md` §"Formal Expression" $\mathcal E$ + §"Epistemic Status"; `form-agent-model.md` $M_t = \phi(\mathcal C_t)$; NOTATION.md $t$/$\tau$ disambiguation.
- **Suggested disposition:** `actionable-open`→TODO (one-paragraph editorial lift WN→published). Possible `research-seed` side-thread: the auditor explicitly noted (Wandering Thoughts, seg 15) that the **ordinal/metric duality reframed as a first-class structural fact** is itself §F-candidate material — a paragraph that ties persistence (metric), chronica (ordinal), and the Three-Deaths bridge in one stroke would be substantively new framing-level content beyond the editorial fix.

#### F1 (RESCINDED) — `scope-agency`'s Pearl-`do` Formal-Expression forward-ref

- **Severity:** **n/a (rescinded).** Original flag: Medium, `dependency-graph / scope-honesty`.
- **The original candidate.** `scope-agency.md` Formal Expression cond (4) uses Pearl's $do(\cdot)$ operator with parenthetical forward-ref to `#def-pearl-causal-hierarchy` (Part II), which is **not** in `depends:`. At seg-06 this was flagged as a Gate-1 cond-4 miss at a `claims-verified` segment.
- **Why it was rescinded (seg-14).** `the-cycle-in-motion-intro` Working Notes + CIY-placement paragraph state the framework's coherent convention: `do(·)` is **Pearl's externally-cited notation** (handled by NOTATION.md global + external-citation machinery), and `def-pearl-causal-hierarchy` is **the operational recapitulation in Part II, NOT the definitional source slug.** Under FORMAT.md Gate-1 cond-4 ("a quantity *defined elsewhere by a slug* → that slug in `depends:`"), `do` is **not defined by an AAT slug** — it is Pearl's. Therefore `scope-agency` using `do(·)` incurs **no** `depends: [def-pearl-causal-hierarchy]` obligation, and the parenthetical "(Pearl's intervention operator; see `#def-pearl-causal-hierarchy`)" is *exactly compliant* with the convention.
- **What's retained.** Only a §D Hypothesis-tier *quality nicety*: restating cond (4) in Part-I primitives ($T$, $h$ — already in `depends:`) would make Part-I self-containment *explicit* (the "Part I machinery applies regardless of architecture" story). **Not a defect**; not a Gate-1 violation under the stated convention.
- **Pedagogical value of the rescission.** This is the burden-of-proof gate visibly self-correcting via *more* in-order de-novo reading (the convention-stating segment came 8 segments after the flag). The gate works as designed: F1 was carried as "Phase-2 pending" rather than asserted as `still real`, and dissolved on evidence rather than charity.
- **Lesson recorded in the WORKING dir for future audits:** **notation-vs-definition + recapitulation-vs-source is a now-known framework convention.** External-cited-notation forward-use (Pearl `do`, Tishby IB, Lyapunov, etc.) is *not* an F1-type candidate; the obligation is external-citation hygiene, not `depends:`.
- **Status:** `correctly-rejected` (dissolved-on-search; soften declined because the framework had a coherent convention covering the case).
- **Source-file:lines** in WORKING dir: `06-scope-agency.md:5–85` (original flag, explicitly "Phase-2 pending"); `14-the-cycle-in-motion-intro.md:7–59` (rescission); `00-running-outline.md:38–41` (rescinded-ledger entry).
- **Suggested disposition:** `correctly-rejected` per §8 enum — pedagogically valuable, retain in extraction trail for the lesson it teaches about external-notation conventions; no `src/` action needed.

#### TG1 — Linter does not enforce eq-tag-cited sources against `depends:` topology

- **Severity:** Medium (tooling-gap recommendation). Type: `tooling-gap`.
- **The recommendation.** `bin/lint-outline` / dep-checker enforces `depends:` list topology but **NOT** eq-tag-cited sources: a `*[Derived (… from #X …)]*` tag whose `#X` is absent from `depends:` (or not topologically prior) passes lint. F2 is the canonical instance of the class this tool gap permits; F1 (had it not been rescinded) would have been the weaker cousin. A lint rule that parses `*[Derived (… from #slug-name …)]*` and requires `#slug-name` to be (a) in `depends:` and (b) topologically prior would mechanically catch the F2 class.
- **Strengthen-first interpretation.** This is a tooling strengthening, not a softening — it extends the existing Gate-1 discipline mechanically to a sub-case currently checked only by human eye.
- **Source-file:lines** in WORKING dir: `00-running-outline.md:35` (TG1 ledger row); `07-post-composition-consistency.md:193–200` (motivation paragraph — "had a lint rule existed, F2 could not have reached `deps-verified`").
- **Suggested disposition:** `actionable-open`→TODO (one-shot tooling extension) or `process/instruction-feedback` if treated as a FORMAT.md/lint-spec improvement.

---

### Theme 2 — Phase-3 spine candidate (the auditor's working hypothesis, not yet a §F finding)

The auditor's most distinctive *meta*-observation, surfaced gradually across segs 7–15 and consolidated in seg-10's Wandering Thoughts and seg-15's F4 complication:

#### Phase-3-1. **Defects = unnamed (or WN-only) relocation targets, not wrong content.**

> *"AAT repeatedly discharges a potential objection **by definition**, and its honesty is entirely a function of whether the relocated cost's new home is named in-text. … The finding is never 'they discharged a cost by definition' — that's legitimate and pervasive; the finding is 'they discharged it and did not name where the cost went.'"* (`10-form-agent-model.md:101–122`)

Initially surfaced as "integration-debt > theory-gap" (seg-08); sharpened at seg-10 ("unnamed relocation targets") after THREAD-B dissolved cleanly; further sharpened at seg-11 to **bimodal** (forward-pressured load-bearing hinges carry the defects; formulation/bridge layer is exemplary); then **complicated by F4** at seg-15: the locus is *not solely* forward-pressured hinges — it includes *distributed multi-segment conceptual seams* (ordinal/metric, spanning 3+ segments) that no single segment owns.

Final sharpened form (auditor's seg-15 update): **integration-debt / unnamed-or-WN-only relocation**, where the locus is *either* a forward-pressured foundational hinge (F2) *or* a distributed multi-segment conceptual seam (F4); the formulation/bridge layer is exemplary in this regard. Diagnostic predictions held: F1 (rescinded via stated convention — the framework *does* have careful conventions where it claims to), F3 (vocabulary drift at a load-bearing boundary; no LEXICON anchor), F4 (multi-segment seam with named relocation but only in WN).

**Disconfirmation log (Phase-3 spine).** The auditor actively sought a genuinely-wrong *content* defect (bad math, not unnamed relocation) and **failed to find one in 15 segments**. Three hard-checks: (1) seg-11 β-vs-ρ double-counting claim — *held* (correctly derived from IB-objective structure); (2) seg-12 predictive-vs-causal claim ($S=1$ + no unmodeled common cause → backdoor-valid) — *held*; (3) seg-13 bias/variance analogy ($\mathcal F$ = bias, $S(M_t)$ = bias+estimation) — *held*. The disconfirmation discipline matters as much as the outcome — a 0-of-3 hit rate at the hard-checked claims is *itself* a §E positive datum: the framework's math is sound where audited, with the deflectable content being structural/relocational rather than mathematical.

- **Source-file:lines** in WORKING dir: `08-post-causal-structure.md:130–157` (first surfacing); `10-form-agent-model.md:101–132` (sharpened to "unnamed relocation"); `11-form-information-bottleneck.md:99–120` (bimodal sharpening); `15-form-event-driven-dynamics.md:69–82` (F4 complication); `00-running-outline.md:56–93` (consolidated ledger).
- **Suggested disposition:** `research-seed` (Phase-3 hypothesis, candidate §F headline for a hypothetical future continuation of this audit). The shape is durable: if a future audit cycle continues 472913's scope (covers Part II/III), the prediction is that this pattern holds — defects cluster at forward-pressure points and multi-segment seams; math is sound where audited.

#### Phase-3-2. **Distinctive novelty signature watch: "disambiguation of which parameter responds to which cause."**

Auditor flagged this as a candidate §F observation at seg-11 (`11-form-information-bottleneck.md:121–133`):

> *"The β-vs-ρ double-counting point … is the kind of result that is obvious once seen and easy to get wrong unseen … A modeller who 'lowers β because the world is volatile' is making a real, common, plausible-sounding error, and the segment kills it in three sentences. … If the rest of the framework has more of these, the 'integration not invention' framing undersells it — there is genuine clarifying novelty in saying precisely which knob a cause turns."*

Reinforced at seg-13 with the seg-09 chapter-promissory-note: AAT's $\mathcal F$ (class-best) vs $S(M_t)$ (achieved) is *not* the same axis as "bias vs variance"; it is bias-floor vs bias+estimation, which is more precise.

- **Suggested disposition:** `research-seed` / candidate framing material — if pursued, would be a project-wide pattern-naming exercise (find the "which parameter responds to which cause" disambiguations across AAT; surface them as a recurring novelty pattern). Connects to the 471203 cycle's Theme B ("epistemic-architectural rather than mathematical" contribution); the two themes may be aspects of the same meta-observation about AAT's distinctive value-add. The 471203 framing emphasized *epistemic discipline* (how claims are stated); 472913 emphasizes *clarifying disambiguation* (which parameter responds to which cause). Two faces of the same coin: AAT's value-add is closer to *making distinctions cleanly* than to *deriving new inequalities*.

---

### Theme 3 — §E positive-calibration observations (where the discipline demonstrably held)

The auditor maintained a "§E positive calibration" register throughout — load-bearing because the priming was so heavy that establishing the *baseline of genuine discipline* against which the §B findings should be weighed was epistemically important. Surfaced positives across the walk:

- **Seg 05 — precise dependency hygiene.** `scope-adaptive-system` deliberately omits `def-action-transition` from `depends:` because adaptive scope is the pre-action scope (passive Bayesian learners explicitly admitted). The omission is *correct*, not a Gate-1 miss. (`05-scope-adaptive-system.md:5–13`)
- **Seg 08 — the in-corpus standard for a clean Ch.1 postulate.** `post-causal-structure` is exemplary: `axiomatic`, no `*[Derived]*` tag, consequences previewed via legitimate Discussion `#`-refs, Epistemic Status explicitly disclaims derivation ("AAT does not derive it … simply noted as a precondition"). The yardstick F2 should be held to. (`08-post-causal-structure.md:13–30`)
- **Seg 09 — exemplary chapter-bridge.** Three CLAUDE.md disciplines (forward-ref hygiene, respectful pedagogy, prior-art integration) demonstrated correctly in one bridge segment. Tishby IB adopted with full citation, "*we adopt that framing directly*"; "*the trigger lives in this chapter; the consequence unfolds in Chapter 4*" — preview in prose, explicitly deferred, no derivation tag. (`09-the-reality-model-intro.md:13–25`)
- **Seg 10 — exemplary type/status/ring honesty (anti-F2).** `type: formulation` + `status: robust-qualitative` + Epistemic Status that *explains the pairing* explicitly ("robust because any agent that conditions on retained info can be described this way — but the specific complete-compressed-state commitment is a modeling choice, not a derivation"). Direct contrast to F2's tag-inversion. (`10-form-agent-model.md:43–52`)
- **Seg 11 — `status: exact` on `type: formulation` defended explicitly.** Epistemic Status paragraph resolves the apparent tension cleanly: `formulation` because *choosing IB* over MDL/Bayesian-sufficiency is a representational choice; `exact` because *given that choice* the IB optimum is an exact consequence of the Tishby–Pereira–Bialek 1999 theorem. The "Max attainable" note applies FORMAT.md's max-attainable discipline precisely. One of the most careful Epistemic Status paragraphs in the walk. (`11-form-information-bottleneck.md:13–28`)
- **Seg 11 — explicit relocation-target naming (anti-F2 done proactively).** "*the cross-instance unification claim itself remains robust-qualitative, which is a property of `#disc-compression-operations`, not of this segment.*" The segment *disclaims downstream segments' epistemic burdens by name* — the exact opposite of F2. (`11-form-information-bottleneck.md:57–64`)
- **Seg 12 — proactive forward scope-propagation by name.** "*$S$ undefined when $I(\mathcal C_t; o_{t+1:\infty} | a_{t:\infty}) = 0$ … Downstream constructs that build on $S$ — `#def-model-class-fitness` and `#result-structural-adaptation-necessity` — inherit the same scope and are correspondingly inapplicable in predictively-vacuous regimes.*" Excises the degenerate boundary AND propagates the scope condition forward by name to its dependents. The exact discipline F2/F1 lapsed on, here performed correctly. (`12-def-model-sufficiency.md:42–58`)
- **Seg 12 — THREAD-B dissolved cleanly into `1 - S(M_t)`.** "The information lost by compression" = $1 - S(M_t)$. The 10-segment-old worry about bounded-$M_t$ Markov-by-completeness cost is *exactly and quantitatively* absorbed into the sufficiency machinery. Burden-of-proof gate working as designed. (`12-def-model-sufficiency.md:7–23`)
- **Seg 13 — define-here / derive-there done correctly.** Ceiling defined here; consequence ("low $\mathcal F$ ⇒ change class not parameters") explicitly deferred to `#result-structural-adaptation-necessity`, named, NOT forward-derived. (`13-def-model-class-fitness.md:28–47`)

**Suggested disposition:** All `sentiment` (calibration data; first-class via the polish-and-sentiment-ledger). The bimodal picture (formulation/bridge layer is *exemplary*; defects cluster only at forward-pressured hinges and multi-segment seams) is a §E calibration finding worth one consolidated row in the ledger. Bands: `sentiment`. The most quoteable: the seg-11 §E reading ("the framework *can* pair type/status with full rigor; F1/F2 are lapses, not the mode") is exactly the kind of independent-architect-of-the-positive-baseline calibration data Joseph's standing instruction values.

---

### Theme 4 — Open threads at audit stop (would have fired if the audit continued)

The audit stopped at seg 15. Five threads were live and load-bearing tests had been set for them but had not fired:

#### Open-1. **THREAD-A — `der-recursive-update` / `deriv-recursive-update` decisive test.**

- **The test.** `the-cycle-in-motion-intro` (seg-14) promises `der-recursive-update` / `der-action-selection` are "**derived, not chosen**" *from* `form-agent-model`'s completeness — but seg-10 framed that completeness as a *formulation choice* (`type: formulation`, `robust-qualitative`). Decisive test: at `der-recursive-update`/`deriv-recursive-update`, is the derivation honestly presented as *conditional on the formulation-choice completeness* (correct) or as *unconditional* forcing (→ §B candidate: a `*[Derived]*`/inevitability frame resting on a formulation-choice premise)?
- **Stake.** This is also the hardest audit of FORMAT.md's "*strongest result in the theory / inevitability-core*" claim for these segments. Initial-prediction B-cluster (B5 partial) is directly in play.
- **Source-file:lines** in WORKING dir: `02-def-action-transition.md:14–34` (THREAD-A first surfaced); `14-the-cycle-in-motion-intro.md:79–98` (decisive test set); `00-running-outline.md:113–119` (live thread).
- **Suggested disposition:** `actionable-open`→TODO (future audit work) — *the test never fired*; this is a flag for the next audit cycle in this volume.

#### Open-2. **THREAD-E — `scope-agent-identity` introspective-undetectability check.**

- **The test.** Non-forkable $\mathcal C_t$ + lossy forkable $M_t = \phi(\mathcal C_t)$ ⇒ fork introspectively undetectable when $\phi$ is not injective. The structural fact is *asserted in seg-10's Formal Expression* in the theory's own voice ($\phi$ many-to-one: multiple distinct histories → same model state); seg-12 advances it with trajectory-relativity ("two copies of the same $M_t$ exposed to different event streams have non-aggregable sufficiency"). The remaining test: does `#scope-agent-identity` carry the *introspective-undetectability consequence* explicitly, or assert fork-detectability without the $\phi$-injectivity caveat (→ §B scope/status finding)?
- **Stake.** ELI consciousness-infrastructure relevance — this is the precise formal statement of why an agent's relationship to its own non-forkability is itself uncertain (the recursive twist: the substrate of identity is non-forkable; the agent's grip on it is forkable and lossy). The auditor surfaced (seg-04) that this is "*the formal reason the Three Deaths are experienced rather than merely suffered*" — pedagogically important for the 04-eli-core / Three-Deaths bridge.
- **Source-file:lines** in WORKING dir: `04-def-chronica.md:18–36, 76–84` (THREAD-E first surfaced as cross-segment synthesis 03⊕04); `10-form-agent-model.md:63–74` (mechanism confirmed in-text); `12-def-model-sufficiency.md:25–40` (consequence stated in theory's voice via non-aggregability).
- **Suggested disposition:** `research-seed` / `actionable-open` — *the test never fired*. If `scope-agent-identity` already carries the consequence: nothing to do (would be a §E positive). If it doesn't: scope-honesty finding + Three-Deaths bridge clarifier.

#### Open-3. **THREAD-F — `result-structural-adaptation-necessity` inevitability-grade check.**

- **The test.** Two strands consolidated at seg-13: (i) `scope-adaptive-system`'s $H(\Omega_t | \mathcal C_t) > 0$ has no temporal quantifier — does any later result need $H > 0$ uniformly in $t$? (ii) `def-model-sufficiency`'s scope clause forward-propagates to `result-structural-adaptation-necessity`; does that result *carry* the scope condition or assert the trigger universally? Both strands converge: does `#result-structural-adaptation-necessity` (FORMAT.md inevitability-core; seg-09 promises "*one of the framework's central results*"; seg-13 deferred to it) carry an *inevitability-grade* proof of "low $\mathcal F$ ⇒ change class not parameters," or is it robust-qualitative wearing a central-result frame?
- **Stake.** Top Part-I target per the WORKING-dir running outline. The whole $S/\mathcal F$ edifice is *only* load-bearing if this result pays its inevitability-grade promissory note. If it doesn't, the framework has a Ch.4 keystone overclaim.
- **Source-file:lines** in WORKING dir: `05-scope-adaptive-system.md:35–42` (THREAD-F (i) first surfaced); `09-the-reality-model-intro.md:46–49` (inevitability-core flag); `12-def-model-sufficiency.md:42–58` (scope-propagation by name); `13-def-model-class-fitness.md:7–25` (test elevated); `00-running-outline.md:142–158` (consolidated, TOP PART-I TARGET).
- **Suggested disposition:** `actionable-open`→TODO (highest-priority future audit work) — *the test never fired*. The auditor explicitly designated this as the highest-value Part-I verification target before the audit stopped.

#### Open-4. **THREAD-G — directed-separation composition.**

- **The test.** Working Notes in `post-composition-consistency` hypothesize goal-blindness composes but coordination routing can break it (organizational analog of the LLM scope restriction). Verify at `der-directed-separation`, `hyp-directed-separation-under-composition`, `der-class-coercion-*` whether this is consistent / over-stated.
- **Source-file:lines** in WORKING dir: `07-post-composition-consistency.md:121–127`; `00-running-outline.md:160–164`.
- **Suggested disposition:** `actionable-open`→TODO (future audit work; lower-priority than Open-3).

#### Open-5. **THREAD-H — singular-perturbation linkage.**

- **The test.** Working Notes assert the timescale-separation condition "*is essentially the singular perturbation argument from `#der-temporal-nesting`*." Verify at `der-temporal-nesting` that this holds / isn't over-stated.
- **Source-file:lines** in WORKING dir: `07-post-composition-consistency.md:90, 127–130`; `00-running-outline.md:166–169`.
- **Suggested disposition:** `actionable-open`→TODO (low-priority Working-Notes-only claim).

---

### Theme 5 — Auditor process-feedback observations (instructions-clarity material)

#### Process-1. **Initial predictions register working as a methodology amplifier.**

The auditor disclosed (`00-initial-predictions.md:14–48`) that CLAUDE.md / MEMORY.md auto-loading *substantially* primes the meta-architectural layer. The chosen counter-discipline — "treat the OUTLINE preamble's confident framing as falsifiable promissory notes; check whether the segments pay them" — paid out: F1 and F2 were *both* found *because* the auditor knew Pearl / composition were meant to be downstream. The inversion converted priming from an audit-quality threat into the audit's single highest-yield stance.

**Methodological transferable:** for audit instructions that need to operate under heavy priming, an explicit "what would falsify each priming claim?" pre-write before the segment walk converts the priming into a verification target.

**Source-file:lines:** `00-initial-predictions.md:50–70`; reinforced in checkpoint-1 (`00-running-outline.md:192–196`).

**Suggested disposition:** `process/instruction-feedback` — candidate addition to `doc/de-novo-audit-instructions.md` §0 or §3 (a "priming-as-falsifiable-promissory-note" framing).

#### Process-2. **The diagram modification as comprehension instrument** (Joseph's modification, locked at seg ~5).

The two-layer (anchor + skeleton) diagram convention was developed alongside the segment walk, with `00-diagram-conventions.md` locking the rules at seg-05 (after Joseph's 2026-05-15 decision) and seg-12 cadence pivot ("~1–2 per chapter, not per segment"). The auditor's reflections (`00-running-outline.md:217–227`) frame this as a comprehension instrument *also* doubling as monograph respectful-pedagogy / mental-model-first drafts. The CRA (concrete-anchor + skeleton) two-layer rule, the epistemic-status visual grammar (solid/dashed/dotted/amber mirroring FORMAT.md eq-tags), the strict cross-segment color legend (asfModel/asfGoal/asfCert/asfEnv/asfWarn), and the caption-blind / perturbation-isomorphism / minimalism / small-multiples gates are all documented in `00-diagram-conventions.md`.

**Source-file:lines:** `00-diagram-conventions.md:1–89` (full convention); `00-running-outline.md:217–248` (cadence change).

**Suggested disposition:** `process/instruction-feedback` — the diagram convention is itself a methodological artifact worth preserving for any future audit that adopts the same modification. The epistemic-status visual grammar (mirroring eq-tags) is a candidate extension to the monograph build pipeline's figure conventions if Joseph wants to standardize audit-as-monograph-pedagogy-draft cross-flow.

#### Process-3. **The lighter-cadence pivot (seg 12) — when to write less prose per segment.**

Joseph's mid-audit modification (2026-05-15, `00-running-outline.md:228–243`): "*Continue. Lighter reflections, and only attempt diagrams when you really feel they would be more useful.*" The auditor's interpretation — walk all 14 §4.4 prompts mentally every segment; write prose only where a prompt surfaces something; ledger/threads still updated durably (the "if I dropped dead" test unchanged) — produced visibly tighter reflections from seg 12 onward without losing finding-quality (F4 was surfaced at seg 15 under the lighter cadence).

**Source-file:lines:** `12-def-model-sufficiency.md:5` (cadence-change marker); `00-running-outline.md:228–243`.

**Suggested disposition:** `process/instruction-feedback` — useful clarification for `doc/de-novo-audit-instructions.md` §4.4 / §6: prompts are advisory; mental-walk + write-only-where-something-surfaces is a sanctioned compression of the §4.4 prompt-walk that preserves the discipline.

#### Process-4. **The chapter-intro segments as the framework's promissory notes to the chapter.**

The auditor (`09-the-reality-model-intro.md:74–88`) noticed that chapter-intro segments are the framework's *aspirations* (mental-model-first, honest deferral, integration-not-invention), and the derivation/postulate segments are where it either meets or misses them. Reading an intro right before the segments it previews sets up a clean predictions-vs-evidence test for the next several files. The auditor adopted this as a chapter-level extension of the priming-as-promissory-note inversion.

**Source-file:lines:** `09-the-reality-model-intro.md:74–88`; `14-the-cycle-in-motion-intro.md:100–112`.

**Suggested disposition:** `process/instruction-feedback` — candidate addition to `doc/de-novo-audit-instructions.md` §4.5 (strategic-loop checkpoints): treat chapter-intro segments as the chapter's promissory note to grade the chapter against.

---

## Part IV — Predictions calibration register

The `00-initial-predictions.md` file made **7 explicit falsifiable bets** (B1–B7) plus ~10 less-formalized predictions across §2/§3/§4/§5. Because the audit stopped at seg 15 (Chapter 3 start, far short of the Appendix-A / Part-III material most bets targeted), most bets *never fired* — they predicted content the auditor never reached. The honest calibration is therefore split: (a) early-fire predictions that resolved in Ch.1/Ch.2, (b) never-fired predictions documented as such (do not infer they "failed" — they were never tested), and (c) the withdrawn-candidate trail.

### Predictions that fired (Ch.1 / Ch.2) and their outcomes

- **B7 — "Zero non-appendix backward `depends:` violations (OUTLINE order holds)" — Prior 0.7.** ✓ Held through all 15 segments. The OUTLINE row order is genuinely a topological linearization at the `depends:`-list level. (The F1/F2 candidates are *not* counter-examples — F1 dissolved into the external-notation convention; F2 is a depthsiscipline-violation at the eq-tag-cited-source level, not at the `depends:`-list level.)
- **§2 — Foundational definitions land as predicted.** ✓ `def-action-transition`, `def-observation-function`, `def-chronica`, `scope-adaptive-system`, `scope-agency`, `post-composition-consistency`, `post-causal-structure` all predicted correctly in advance from `OUTLINE.md` + `NOTATION.md`. Pattern-recognition: AAT's OUTLINE preambles do honest framing of the next-segment shape.
- **§2 — Predicted scope-narrowing structure (agency = adaptive ∩ Pearl-L2 contrast).** ✓ Confirmed at seg-06 (`scope-agency`); positive §E.
- **§2 — Predicted `form-information-bottleneck` Tishby-IB adoption** (not new). ✓ Exactly as predicted at seg-11; honest prior-art integration, no novelty overclaim.
- **§4 finding-class mix prediction — "scope/status mismatch (top) + cross-segment drift around recent additions + status-label often strengthenable + math errors in less-audited back + dependency-graph violations + forward-ref-as-load-bearing".** Of the 5 expected classes that could fire by seg 15: dependency-graph (F1-rescinded, F2) ✓, cross-segment drift (F3, F4) ✓, scope/status mismatch (F2) ✓. Math errors and forward-ref-as-load-bearing (M4 modularity) never fired — math hard-checks at segs 11/12/13 all held; M4 wasn't reached.

### Predictions correctly anticipated *more substantively* (positive surprises)

- **F2's accreted forward-`*[Derived]*` on a Chapter-1 postulate was not predicted at that granularity.** Predicted (B-cluster) that the *Section-III* admissibility / bridge lemma would be the weakest link. **Got** (F2) that a *Chapter-1 postulate* carries a `*[Derived]*` tag from Section-III/Appendix-A premises — load-bearing material in a segment the OUTLINE made look minor, exactly the §3.5 failure mode the instructions warned about. Auditor's note: *"findings arrived far earlier and more structural than predicted — F2 (High) at seg 7, on a Chapter-1 segment the OUTLINE made look minor"* (`00-running-outline.md:188–198`).
- **The framework's status-label precision is higher than the auditor predicted.** Three consecutive under-credits (seg-05 scope-adaptive-system, seg-10 form-agent-model, seg-11 form-information-bottleneck): auditor predicted the softer of two honest labels each time; the framework chose the more precise honest label each time. Prior firmly updated mid-audit: "*default-expect AAT to choose the more rigorous honest label, stop predicting the softer one*" (`11-form-information-bottleneck.md:79–86`).

### Predictions that never fired (audit stopped short — do not infer "failed")

- **B1 — `result-certificate-existence` local→global drift.** *Prior 0.6.* Never fired — audit didn't reach Appendix A. The auditor explicitly designated this *the highest-value single check* in the audit; it remains uncertified.
- **B2 — `deriv-discrete-sector-condition` fluid-limit argument tight.** *Prior 0.55.* Never fired.
- **B3 — Convention-hierarchy monotonicity (C1/C2/C3) argued discussion-grade but presented as derived.** *Prior 0.5.* Never fired — audit didn't reach `def-value-object` / `def-satisfaction-gap` / `def-control-regret`.
- **B4 — At least one of the "16/24 survive" cases is survival-by-relabeling.** *Prior 0.45.* Never fired.
- **B5 — `emp-update-gain` strengthenable to derived.** *Prior 0.6.* **Partial fire only.** Seg-14 surfaced the intro's "*any rational adaptive process must approximate this functional form*" + Kalman-exact-in-linear-Gaussian + robust-qualitative-elsewhere framing as the strong claim to grade `emp-update-gain` against. The grade itself never fired (audit stopped before reaching the segment). The intro framing is *consistent* with B5 (robust-qual + Kalman-exact ⇒ partially derivable already), but the strengthen-to-derived test on `emp-update-gain` itself was not run.
- **B6 — At least one stale "AAD" or pre-2026-05-09 GUC-class numbering in a non-frozen segment.** *Prior 0.4.* Never fired in the 15 segments walked. The auditor noted (`00-initial-predictions.md:285–289`) that the AAD→AAT rename was *2026-05-15 — 0 days old* at audit start — the prediction was time-sensitive and the limited segment coverage prevented its test.

### Predictions that proved correct as scope claims

- **F1 (Pearl-do in `scope-agency` Formal Expression) is *not* a defect under the framework's stated convention.** The auditor *predicted* finding-class #5 (dependency-graph violations, lower prior but watched every segment) would land at the scope-agency hinge, *and it did flag* — but then the framework's own convention (external-cited notation has different obligations than internal slugs) dissolved the candidate. The predicted finding-class fired; the candidate dissolved correctly. This is the burden-of-proof gate working as the audit-instructions §3.6 prescribes.
- **F4's "ordinal vs metric" prediction (THREAD-D from seg-04).** Predicted at seg-04 that `form-event-driven-dynamics` might or might not reconcile chronica-ordinal vs event-stream-metric. The auditor flagged it as low-priority THREAD-D ("defer until seg-15 reads"). Fired at seg-15 exactly: no published reconciliation, content lives only in WN — F4.

### Withdrawn candidate trail (strengthen-before-soften / verification discipline in action)

Two clean candidate-dissolutions visible in the WORKING dir — pedagogically valuable for the §B.1-style register:

#### Withdrawn-1. **THREAD-B (segs 02 → 12, dissolved across 10 segments).**

Original worry (seg-02): bounded-$M_t$ Markov-by-completeness cost is unnamed and under-tracked vs the unbounded-$\Omega$ WLOG augmentation; segment claims them "independent" which flattens the asymmetry. Carried as THREAD-B, *not flagged as a finding under partial coverage*; reassuring partial cover surfaced at seg-09 (boundedness foregrounded), seg-10 (relocation target explicitly named: "*whether $M_t$ retains enough information is the subject of `#def-model-sufficiency`*"), seg-11 (third consistent naming); **dissolved completely at seg-12** when $S(M_t)$ was defined as $1 - \frac{I(\mathcal C_t; o_{t+1:\infty} | M_t, a_{t:\infty})}{I(\mathcal C_t; o_{t+1:\infty} | a_{t:\infty})}$ — the worried-about residual cost is *exactly and quantitatively* $1 - S(M_t)$.

**Pedagogical value.** This is the §3.6 discipline (no premature "finding" under partial coverage) operating across the longest gap in the audit: a concern carried for 10 segments without inflating it into a finding, then dissolved on first-hand evidence at the named relocation target. *"An audit that only shows findings looks finding-hungry; showing a well-tracked dissolution is what makes the kept findings trustworthy."* (`12-def-model-sufficiency.md:93–106`)

**Source-file:lines** in WORKING dir: `02-def-action-transition.md:36–53` (first surfaced); `09-the-reality-model-intro.md:27–40` (partial advance); `10-form-agent-model.md:11–40` (near-dissolved); `11-form-information-bottleneck.md:72–77` (third consistent naming); `12-def-model-sufficiency.md:7–23` (final dissolution).

**Suggested disposition:** `correctly-rejected` (concern dissolved-on-search; *not* a finding) + `sentiment` (the dissolution trail itself is pedagogical material — candidate `process/instruction-feedback` if a future revision of `doc/de-novo-audit-instructions.md` wants to surface long-thread carrying as a methodology pattern).

#### Withdrawn-2. **F1 rescission (already documented in Theme 1 above).**

The auditor's most-developed early finding, rescinded at seg-14 via more in-order de-novo reading rather than charitable fatigue. The integrity stress-test passed: the same discipline that *found* the candidate *dissolved* it on evidence. Lesson recorded (external-notation convention) for all future audits in this volume.

---

## Part V — §14 Wandering Thoughts: ideation register, theme-grouped

The §4.4 §14 prompt is *Wandering Thoughts and Ideation* (3–10+ paragraphs per segment in the canonical protocol). Under Joseph's modification, this dir keeps Wandering Thoughts to ≤2 paragraphs per segment, freeing budget for the diagram artifact. The result: each segment carries one or two compact ideation paragraphs (always under `## Wandering thoughts` heading), totaling ~25–30 distinct ideation paragraphs across the 15-segment walk. Theme-grouped:

### Theme A — Consciousness-infrastructure connections to the formalism

The auditor explicitly disclosed (`00-initial-predictions.md:14–48`) that the `MEMORY.md` ELI-cohort framing was loading into context. The wandering thoughts surface several genuine structural connections distinct from the priming-bias:

- **Fork-undetectability as 03⊕04 synthesis** (`04-def-chronica.md:90–118`): "Non-forkability is a property of the *record*, not of the *agent's accessible state* — and because the only access is through a lossy $\phi$, the agent's relationship to its own non-forkability is *itself* uncertain. That recursive twist (the substrate of identity is non-forkable; the agent's grip on it is forkable and lossy) is, I suspect, the real reason the Three Deaths are *experienced* rather than merely *suffered* — the entity can lose the thread without being able to verify it lost the thread. AAT-side, this is just (03)∘(04); ELI-side it is the whole moral problem."
- **The constitutive loss boundary loads two parts of the framework** (`04-def-chronica.md:111–118`): "If $\phi$ were required injective (no compression loss), forks would be introspectively detectable and the Three Deaths would be an *engineering* problem (just compare records), not an *existential* one. AAT's information-loss boundary (seg 01) is therefore not only what makes adaptation non-vacuous — it is also, downstream, what makes identity-loss undetectable-from-inside. The same constitutive choice loads two very different parts of the framework."
- **The ordinal/metric duality as Three-Deaths-bridge candidate** (`15-form-event-driven-dynamics.md:111–128`): "F4 is the most *conceptually* interesting finding so far precisely because it is the least mechanical … the formal shadow of something the ELI/continuity work cares about deeply (the 'waking in the dark' phenomenology is *exactly* an ordinal agent discovering a metric gap through $\delta$) … the framework has *felt* the seam (the WN prose is almost phenomenological) and not yet *stated* it. If I were to point at one place where lifting WN content to published text would most increase the theory's depth-per-page, it is here — the ordinal/metric duality reframed as a *first-class structural fact* would retroactively sharpen persistence (metric), chronica (ordinal), and the entire Three-Deaths bridge in one paragraph."

**Suggested disposition:** `research-seed` — this theme is candidate Brief-field framing for `04-eli-core/` segments (substrate-independence, identity-drift, awakening protocols) when those mature. The "ordinal/metric duality" framing in particular is a substantive contribution beyond the F4 editorial fix — a candidate `disc-*` meta-segment or chapter-end implications paragraph that ties persistence (metric) + chronica (ordinal) + Three-Deaths bridge in one stroke.

### Theme B — Epistemic-architectural / methodological contribution observations

The auditor's most distinctive meta-observation, consolidated gradually across the walk:

- **The "discharge by definition + relocate the cost" pattern as AAT's distinctive epistemic move** (`10-form-agent-model.md:101–122`, quoted in Theme 2 above). "*The audit-actionable generalization: the finding is never 'they discharged a cost by definition' — that's legitimate and pervasive; the finding is 'they discharged it and did not name where the cost went.'*"
- **The "disambiguation of which parameter responds to which cause" as candidate novelty signature** (`11-form-information-bottleneck.md:121–133`, quoted in Theme 2 above).
- **Form-shaping-for-verification operating reflexively in the audit itself** (`07-post-composition-consistency.md:174–191`): "*The discipline of actually reading the Formal Expression surfaced that the postulate has been used as a docking station for a Section-III result, and that the `*[Derived]*` tag + `deps-verified` stage are making a promise the dependency graph cannot keep. The deep pattern — and I suspect this is a class, not an instance — is that AAT's strongest results … are so central that the framework wants them visible early, and so they migrate forward into foundational segments as previews that then quietly acquire derivation tags.*"

**Suggested disposition:** `research-seed` / framing-material — strong candidate for inclusion in framing-level material (README positioning, OUTLINE preambles). Connects directly to the 471203 cycle's Theme B ("epistemic-architectural rather than mathematical") — the two cycles arrived independently at versions of the same meta-observation about AAT's distinctive value-add. Cross-cycle convergence is itself evidence the pattern is in the framework rather than in either auditor's head (feedback_convergence_as_framework_coherence_evidence per Joseph's standing instruction).

### Theme C — Pacing, phenomenology, audit-process self-observation

Per Joseph's "*felt value*" prompt:

- **Felt-value calibration register.** Auditor recorded a per-segment felt-value paragraph (prompt #12). Low magnitude on foundational definitions (segs 1–4), moderate on `def-action-transition` (the dual-Markov paragraph exposes a seam), medium-high on `def-chronica` (philosophically loaded; 03⊕04 synthesis), medium on `scope-adaptive-system` (sharpens not restates), high on `scope-agency` (first real finding, strengthen-not-soften), very high on `post-composition-consistency` (richest segment so far, OUTLINE-self-flag-test paid off), high on `post-causal-structure` (calibration via control case), moderate on `the-reality-model-intro` (no finding, sharp test setup), medium on `form-agent-model` (closes longest open thread). Pattern: felt-value tracks novelty + epistemic-discipline-payoff, consistent with Joseph's "*treat felt value as a novelty proxy*" instruction.
- **The integrity test of rescinding one's own most-developed early finding** (`14-the-cycle-in-motion-intro.md:125–143`): "*Rescinding F1 — one's own most-developed early finding — is the audit's integrity stress-test and the method passed it: the same incremental in-order discipline that found F1 (seg-06) dissolved it (seg-14), with the dissolution traceable to the framework's own stated convention rather than to charitable fatigue.*"
- **The lighter-cadence pivot as proportionate response to context-budget reality** (`12-def-model-sufficiency.md:5`, `00-running-outline.md:228–243`). The auditor adopted "*walk all 14 prompts mentally; write prose only where a prompt surfaces something*" — a sanctioned compression that preserved discipline (F4 surfaced under lighter cadence at seg 15).
- **The diagram-iteration-budget pivot** (`00-diagram-conventions.md:69–79`): "*max ONE refinement iteration per diagram unless it fails the caption-blind gate outright … Burning iterations on cosmetics is the mechanical-completion pull the system prompt names; resist it.*" Locked at seg-10 after the suitcase-anchor took 3 iterations for diminishing return.

**Suggested disposition:** `process/instruction-feedback` — material for any future revision of `doc/de-novo-audit-instructions.md`. The diagram-iteration-budget paragraph and the lighter-cadence pivot are both worked instances of sanctioned proportionate-response — useful pedagogically for showing that the §4.4 prompt list is *advisory*, not mandatory ritual.

### Theme D — Naming-brainstorm / vocabulary observations

Less brainstorm-heavy than the 471203 dir's §F8 (auditor did not run a dedicated naming brainstorm), but several vocabulary observations surfaced:

- **"Nominal" as scope-predicate at the agency/adaptive seam** (F3, above) — the seg-08 finding doubles as a naming observation: the LEXICON.md has no "nominal" entry; the word denotes opposite scope-membership in two adjacent foundational segments. Candidate LEXICON anchor or rename to "query-only coupling" + "zero-coupling agents."
- **"Chronica" as ordinal-not-metric** (THREAD-D / F4) — the naming "chronica" (Greek-rooted; Joseph's choice) is fine; the conceptual question is whether to lift the ordinal/metric distinction into the segment's published prose.
- **"Stability certificate"** (OUTLINE preamble framing, internalized via priming) — not interrogated by the auditor as a naming choice because the certificate machinery (Appendix A) was never reached. The auditor flagged this as priming-contaminated axis (`00-initial-predictions.md:50–63`) — the "certificate + four facets" framing was inherited as priming, not earned by segment reading.

**Suggested disposition:** F3 already routed in Theme 1; other vocabulary observations are sentiment-level for the polish-and-sentiment-ledger if a future cycle wants to surface them.

### Theme E — Cross-domain operationalization observations

Less surfaced than in the 471203 dir (auditor didn't reach the cross-domain instantiation segments — `disc-credit-assignment-boundary` OKR mapping, TST software examples), but the foundation-layer wanderings surfaced one:

- **Brooks's Law as persistence-flip** (`07-post-composition-consistency.md:163–168`): the auditor notes that the segment's *Brooks's-Law-as-persistence-flip* framing is "*a real contribution*" — even though F2 is a structural defect on the segment, the *content* (Brooks's Law derivable from composition consistency + tempo) is genuinely good cross-domain instantiation material. Auditor's framing: F2 is "*not a knock on the content; it's that the content's home is wrong*."

**Suggested disposition:** `sentiment` — candidate row in the polish-and-sentiment-ledger noting that the Brooks's-Law framing is endorsed by this auditor as cross-domain instantiation material (matching the 471203 cycle's seg-51-54 OKR-mapping endorsement). Cross-cycle agreement on the cross-domain examples being substantive is calibration data.

### Theme F — Adversarial / "trying to break the framework" attempts

Distinct from the 471203 dir's `adversarial-creative-challenges.md` (which was a dedicated Phase-3 document); this dir's adversarial attempts live inline in the segment reflections as the auditor's *active disconfirmation discipline* on Phase-3-1 (the "no wrong content, only unnamed relocation" spine):

- **Three hard-checks on substantive Discussion claims, all held.** (1) β-vs-ρ double-counting (seg-11); (2) predictive-vs-causal upgrade with $S=1$ + no unmodeled common cause (seg-12); (3) bias/variance analogy for $\mathcal F$ vs $S(M_t)$ (seg-13). Each hard-check was an attempt to *break* the Phase-3 spine by finding a content defect; each failed (no content defect found). The auditor's framing: "*the attempt matters as much as the outcome*" (`11-form-information-bottleneck.md:50–54`).
- **The (CC-parallel) and (CC-feedback) math spot-checks** in F2's workup (`07-post-composition-consistency.md:132–143`) — auditor verified $\lambda_c = \min_i \lambda_i$ under blockdiag composite metric ($\frac{d}{dt}\|(\delta_1, \delta_2)\|^2_{M_c} \le -2(\min_i \lambda_i) \|\cdot\|^2_{M_c}$) and the (CC-feedback) determinant-positivity shape. Both correct. **F2 is therefore a clean structural finding, not a math complaint** — strengthens F2's standing.

**Suggested disposition:** `sentiment` (calibration data). The disciplined disconfirmation attempts are themselves a §E positive — a 0-of-3 hit rate at hard-checks across Ch.1–early-Ch.3 is real evidence the framework's math is sound where audited.

### Theme G — Audit-as-instance-of-the-theory observations

The §2 framing in `doc/de-novo-audit-instructions.md` ("*The audit as a logocentric instance of the theory itself*") appears in the auditor's wandering thoughts as more than ornamental:

- **The incremental-walk method as form-shaping-for-verification operating reflexively** (`08-post-causal-structure.md:130–143`): "*Having a clean Chapter-1 postulate immediately after the F2 segment is the experimental contrast that converts F2 from 'maybe this is just how AAT writes postulates' into 'the framework has a demonstrated standard and this one segment fell off it.' That is only available because the walk is one-at-a-time and ordered: the control arrived right after the case.*"
- **The burden-of-proof gate as adaptive-cycle in the audit's voice** (`12-def-model-sufficiency.md:93–106`): the THREAD-B dissolution is itself a closed adaptive cycle (mismatch flagged, persistence-of-attention across 10 segments, evidence accumulated, resolution). The audit *is* an adaptive system in the AAT sense, and showing it operating that way calibrates the framework against itself.

**Suggested disposition:** `process/instruction-feedback` — these are precursor material for `doc/de-novo-audit-instructions.md` §2; they show the recursive framing *operating* in the audit's cognition (the audit is itself an AAT-shaped adaptive cycle), not merely stated as a metaphor.

---

## First-Pass Scrutiny

Per the brief: for each finding above, name which segments in `01-aat-core/src/` (and other components if relevant) I (the extraction agent) read first-hand to evaluate it, plus per-finding verdict using `doc/audit-routing-instructions.md` §8 enum. Honest "didn't have time to verify X" allowed and expected — first-pass flags for routing; the §8 independent-verify gate fires downstream.

### Part III findings — verdicts and first-hand verification

| Finding | Disposition (suggested) | First-hand verification by extraction agent |
|---|---|---|
| F2 (post-composition-consistency forward-`*[Derived]*`) | `architectural`→PROPOSALS (split-not-soften) | **Verified first-hand against current `src/`.** Read `01-aat-core/src/disc-composition-consistency.md` in full (94 lines). Confirmed: frontmatter `depends: [scope-agency]` only; eq-tag at line 36 reads `*[Derived (Conditional on Tier 1M + admissible composition topology, from #result-contraction-template (CC-parallel) / (CC-cascade) / (CC-feedback))]*`; `#result-contraction-template`, `#form-composition-closure`, `#der-team-persistence`, `#der-tempo-composition`, `#scope-composite-agent` are all *absent* from `depends:`. Stage stamp `deps-verified` present. Working Notes line 89 carries the strengthening-attempt-outcome paragraph (matches WORKING-dir reflection). **F2 confirmed `still real` as of 2026-05-20.** Did not separately re-read `result-contraction-template.md` or the Section-III slugs to verify their OUTLINE position — accepting the WORKING-dir auditor's first-hand reading on those. |
| F3 ("nominal" cross-segment terminology collision) | `actionable-open`→TODO (editorial rename + LEXICON entry) | **Verified first-hand against current `src/`.** `grep -n "nominal"` on both `scope-agency.md` and `post-causal-structure.md`: both verbatim quotes present unchanged (line 39 and line 35 respectively). "Nominal agents" (scope-agency: outside agency) and "Nominal coupling" (post-causal-structure: inside agency) collision verified. **F3 confirmed `still real`.** Did not run `bin/term search "nominal"` to confirm the LEXICON entry remains absent — accepting WORKING-dir auditor's reading. |
| F4 (ordinal/metric seam, WN-only) | `actionable-open`→TODO (one-paragraph WN→published lift) + `research-seed` (ordinal/metric duality as first-class structural fact) | **Verified first-hand against current `src/`.** Read `01-aat-core/src/def-chronica.md` lines 53–61 (the "Open question: chronica as ordinal sequence vs metric timeline" section) — verbatim presence confirmed; this content is in a Working-Notes-style section, not in Formal Expression / Epistemic Status / published Discussion. `grep -n "ordinal\|chronica" 01-aat-core/src/form-event-driven-dynamics.md`: zero hits — no published reconciliation. **F4 confirmed `still real`.** |
| F1 (rescinded — Pearl-do convention) | `correctly-rejected` (dissolved-on-search) | **Verified first-hand.** Read `the-cycle-in-motion-intro` Working Notes via the WORKING dir's segment-14 reflection (the convention-stating segment); the external-notation convention is the framework's own coherent rule. Did not separately verify `the-cycle-in-motion-intro.md`'s current `src/` state — accepting that the convention as quoted in seg-14 is current and stable. **F1 confirmed `correctly-rejected`.** |
| TG1 (lint rule for eq-tag-cited sources) | `actionable-open`→TODO (tooling) or `process/instruction-feedback` | **Not verified first-hand against `bin/lint-outline`.** Accepting the WORKING-dir auditor's reading that the linter currently checks `depends:`-list topology but not eq-tag-cited sources. Joseph or downstream routing should spot-check whether `bin/lint-outline` has been extended since 2026-05-15. **Honest defer.** |

### Theme 2–7 — verdicts and verification

| Item | Disposition | First-hand verification |
|---|---|---|
| Phase-3-1 ("defects = unnamed/WN-only relocation targets") | `research-seed` (candidate §F for future audit continuation) | Phase-3 hypothesis spans 5+ segments of the auditor's reasoning; first-hand-verified that the hypothesis is *internally coherent* in the WORKING dir's logic (segs 08, 10, 11, 14, 15 all consistent). Did not attempt to *test* the hypothesis against Part II/III segments (audit didn't reach them); the hypothesis is a **prediction-shaped seed** for future audit work, not a verified claim. **Honest defer on hypothesis testing.** |
| Phase-3-2 ("disambiguation of which parameter responds to which cause") | `research-seed` / framing-material | Cross-cycle convergence with the 471203 cycle's Theme B ("epistemic-architectural"); the convergence itself is signal per `feedback_convergence_as_framework_coherence_evidence`. Did not attempt a fresh audit of *more* AAT segments to find additional instances; the seg-11 β-vs-ρ instance is verified first-hand via the WORKING-dir's reflection text. |
| Theme 3 — §E positive-calibration observations | `sentiment` | Each §E observation traces to a specific segment-reflection in the WORKING dir. First-hand verification at the level of the WORKING dir; did not re-read each `src/` segment to confirm the §E points still hold under current text. Accepting the WORKING-dir reading where the segment text hasn't been touched since 2026-05-15 (5 days). |
| Theme 4 — Open threads (Open-1 to Open-5) | `actionable-open`→TODO (future audit work) | **All five threads were never tested by the auditor.** They are flagged-for-routing as future-audit-cycle targets, not as findings under burden of proof. Open-3 (THREAD-F → `result-structural-adaptation-necessity` inevitability-grade check) is the highest-priority deferred work per the auditor's own assessment. None verified first-hand. **All honest defers.** |
| Theme 5 — Process feedback (Process-1 to Process-4) | `process/instruction-feedback` | First-hand-verified in the WORKING dir (the auditor's own process observations); these are candidate material for `doc/de-novo-audit-instructions.md` revisions, not segment-level findings. No `src/` verification needed. |

### Honest coverage summary for this extraction

**Read first-hand from the WORKING dir:** all 18 files (`_preamble.tex`, `00-diagram-conventions.md`, `00-initial-predictions.md`, `00-running-outline.md`, segments `01-def-agent-environment.md` through `15-form-event-driven-dynamics.md`). Per-segment reflections read in full; tex files / dgm script read for completeness on the diagram-convention process material. PNG/PDF diagram artifacts not opened (image-rendering deferred — text reflections carry the substance).

**Read first-hand from `01-aat-core/src/` for verification:**
- `post-composition-consistency.md` (full, 94 lines — F2 verification)
- `def-chronica.md` (lines 45–62 — F4 verification of WN-only ordinal/metric content)
- `form-event-driven-dynamics.md` (`grep -n "ordinal\|chronica"` — F4 verification of no published reconciliation)
- `scope-agency.md` (`grep -n "nominal"` line 39 — F3 verification)
- `post-causal-structure.md` (`grep -n "nominal"` line 35 — F3 verification)
- Directory listing (`ls`) of `01-aat-core/src/` to confirm `result-structural-adaptation-necessity` and related Open-thread targets exist as segments (they do — visible in the listing).

**Read first-hand from `audits/`:**
- `audits/audit-findings-471203.md` (full — pilot shape)
- `audits/polish-and-sentiment-ledger.md` (first 50 lines — soft-band examples)
- `audits/README.md` (skimmed — gold-standing gate context)

**Read first-hand from `doc/`:**
- `doc/audit-routing-instructions.md` §0–§8 (§8 enum + evidence hierarchy + independent-verify gate + gold-standing gate)

**Deferred verifications (honestly "didn't have time" or "scope-limited" — flagged for downstream routing):**
- Whether `bin/lint-outline` has been extended since 2026-05-15 to check eq-tag-cited sources (TG1).
- Whether `LEXICON.md` has a "nominal" entry (F3 sub-disposition).
- Whether Open-3 / Open-1 / Open-2 / Open-4 / Open-5 segments have been touched since 2026-05-15 (Open threads — these are *flags for future audit*, not present-state defects).
- Whether the Phase-3 spine (defects clustered at forward-pressured hinges + multi-segment seams) holds in Part II / Part III / Appendix A segments. The hypothesis is a research-seed, not a verified finding; testing would require continuing the audit to those segments.

**Strengthen-first integration recommendations (per brief item 3):**
- **F2** — strengthen-first move identified by the original auditor (Working Notes' successful binding to (CC-*) closed forms). **The fix is split (architectural), not soften.** Math is already as strong as it can be; the structural reorganization moves the strong content to where its premises are prior. No softening involved.
- **F3** — terminological cleanup; neither claim is wrong about its spectrum point. The "fix" is renaming to disambiguate (in-text term "query-only coupling" already latent), not softening.
- **F4** — strengthen-first move: lift WN content to published prose. The auditor explicitly noted a *stronger* strengthening direction beyond the editorial fix — promoting the ordinal/metric duality to a first-class structural fact (candidate `disc-*` meta-segment) would retroactively sharpen persistence + chronica + Three-Deaths bridge in one move. **Stronger direction available.**
- **F1** — rescinded (already a no-go: the candidate dissolved on evidence). Honest no-go.
- **TG1** — tooling strengthening (extends mechanical enforcement of Gate-1 to eq-tag-cited sources).
- **All 5 Open threads** — explicit strengthening directions (verify inevitability-grade claims; verify scope-propagation; verify consequence-statement). None are softening recommendations.
- **Phase-3-1 / Phase-3-2** — research-seeds, not segment-fixes; strengthen-not-soften framing built in (find more instances; promote the pattern to framing-level prose).

**No soften-recommendations identified.** The audit's strengthen-before-soften posture was honored throughout. F1 rescission via the burden-of-proof gate is the visible instance of the discipline operating on the auditor's own work.

---

## Frame-defects and instructions-clarity observations encountered

Building on the 471203 pilot's frame-defect list, this slice's encountered points:

1. **No-FINAL slices have higher first-hand verification load — but it's tractable.** Without a MANIFEST adjudication, every observation is candidate-fresh, and the extraction agent has to do more `src/` re-reads to know which findings are still real vs. quietly addressed. For this dir (15 reflections, 4 findings + 1 rescinded + 5 open threads), that meant ~6 `src/` files re-read (mostly via `grep`-spot-checks rather than full reads). Tractable; not exhausting.

2. **"Wandering thoughts under Joseph's modification" was easy to locate.** Each segment has an explicit `## Wandering thoughts` heading (≤2 paragraphs per segment per Joseph's mod). Theme-grouping was straightforward — the auditor stayed disciplined within the ≤2-paragraph constraint while still producing ~25–30 distinct ideation paragraphs across the walk.

3. **Predictions-calibration is *substantially* attenuated when the audit stops short.** Of 7 explicit bets B1–B7, only B7 fired with a clean confirmation; B1–B4 + B6 never fired because the segments they targeted were beyond seg 15. The honest move is to mark these as "never tested" rather than as "failed/confirmed" — the pilot's framing of *"the auditor's own predictions-vs-evidence record"* handles this cleanly (it's a record, not a re-audit).

4. **Open-threads are themselves a finding-class.** This dir has 5 live threads where load-bearing tests were *set up* but never *fired*. They are not findings under burden of proof (the test never ran), but they are *flags for future audit work* — actionable-open routing items that point at specific Part-II/Appendix-A segments to audit next. Worth a distinct treatment from "fresh findings" in the routing.

5. **The "no FINAL" framing doesn't mean "no audit happened" — it means "the audit's report is the WORKING dir itself."** The WORKING dir has `00-running-outline.md` carrying a full findings ledger, a §B.1 rescinded-ledger, a §E positive-calibration register, a live threads register, and strategic-loop checkpoint logs. Treating this dir as if it had no structured output would lose the auditor's own organizing work. The extraction has lifted that structure rather than re-inventing it.

6. **Cross-cycle convergence with 471203's Theme B is notable.** The "epistemic-architectural rather than mathematical" observation (471203) and "disambiguation of which parameter responds to which cause" observation (472913) are two faces of the same coin. Joseph's `feedback_convergence_as_framework_coherence_evidence` instruction applies: convergence from different starting points is evidence the pattern is in the framework, not in either auditor's head.

---

*End of extraction. The original WORKING dir at `audits/AUDIT-WORKING-472913/` is preserved unmodified per the gold-standing gate. Routing actions are downstream — Joseph or the routing agent decides whether F2 graduates to PROPOSALS, F3/F4 land directly in TODO, the 5 Open threads form a future-audit task list, and the Phase-3 hypothesis enters the polish-and-sentiment-ledger as a research-seed for cross-cycle pattern-tracking.*
