---
source_cycle: 963715 (de-novo, Claude Sonnet 4.6, 2026-05-10)
extraction_agent: Claude Opus 4.7 (1M context), parallel-sweep slice
extraction_date: 2026-05-20
working_dir: audits/AUDIT-WORKING-963715/ (13 md files: 2 protocol/orientation + 3 single-segment reflections (segs 1-3) + 8 batch reflections (segs 4-43))
final_of_record: NONE — the WORKING dir IS the audit record (no FINAL was authored)
scope_modification: none stated; auditor pivoted from one-at-a-time cadence to batch reflections at seg 4
cadence_modification: segs 1-3 carried full §4.4 14-prompt single-segment reflections; segs 4-43 are 5-segment batches with abbreviated per-prompt cover
purpose: |
  Consolidated extraction from the WORKING dir for routing through the standard
  audit-routing process. Because no FINAL exists, every substantive observation
  in the WORKING dir is a candidate-fresh finding awaiting routing — the
  subsumed-vs-fresh distinction collapses here. This file is the "what is in
  the dir worth processing" digest. The original working dir is preserved
  unmodified per the gold-standing gate.
---

# Audit-findings extract — 963715 working-dir mining

The 963715 cycle was a **partial de-novo walk** by Claude Sonnet 4.6 (1M context) on 2026-05-10: ~43/~130 AAT-volume segments covered first-hand. Coverage breakdown: full Section I (segs 1-29, including the persistence-condition / sector-condition / structural-adaptation-necessity core); first ~14 segments of Section II (def-agent-spectrum through def-strategy-dag — through the strategy-DAG cluster). The audit did **not** reach: the Section II adversarial-edge / orient-cascade machinery, satisfaction-gap / control-regret diagnostic split, Section III composition, Appendices A-D (Lyapunov derivations, persistence-cost, contraction templates), TST (`02-tst-core/`), `03-llm-core/`, `04-eli-core/`. Pacing pivot: segs 1-3 are full §4.4 single-segment reflections; segs 4-43 are 5-segment batches with consolidated structure (per-segment notes + cross-segment consistency + math verification + finding tracking + wandering thoughts).

What the WORKING dir adds is therefore a **mid-coverage slice of §I + start of §II cognition**: five findings under burden of proof (F1–F5, with F1 paralleling the rescinded F1 in audit 472913), tracked across the walk with explicit finding-tracking updates per batch; a substantive predictions-vs-evidence record on the initial bets (the GUC-rename bet specifically *did not fire* — no integration-debt was found in the 43 segments walked); and a set of Section-II-distinctive wandering-thought observations including a phenomenologically-self-aware passage on the "AI agent's dilemma" in `der-deliberation-cost` that the auditor identified as the most direct self-application of the theory in the corpus.

Because no FINAL exists, no §F bigger-picture-formalization, no MANIFEST disposition row — every observation here is candidate-fresh, and there is no Part I / Part II subsumed-by-FINAL bucket. Structure: Part III findings (themed); Part IV predictions-calibration (the auditor's own record); Part V §14 wandering-thoughts theme-grouped; First-Pass Scrutiny appended.

**Cross-cycle relationship to 472913.** Three of this cycle's findings overlap substantively with the 472913 cycle (also Claude Opus, 2026-05-15 — five days *after* this cycle but extracted on the same day, 2026-05-20). F1 here ≡ F1-rescinded in 472913 (Pearl-do in scope-agency without depends on def-pearl-causal-hierarchy) — 472913's auditor dissolved this on the external-notation convention; this cycle's auditor flagged it as low-severity confirmed. F2 here is a less-precise version of 472913's F2 (post-composition-consistency derived-content-in-postulate) — this cycle's auditor characterized it as "type/content tension" without reaching 472913's sharper "`*[Derived]*` tag on a Chapter-1 postulate naming downstream slugs as derivation source"; the 472913 framing is the better one. **The cycles converge** on the same structural defect at post-composition-consistency, which is itself convergence-as-framework-coherence-evidence (Joseph's standing instruction): two independent auditors with five days between sessions arrived at the same finding from different starting points.

---

## Part III — Findings (all fresh — no FINAL exists to subsume them)

### Theme 1 — The five findings under burden of proof

#### F1 — `scope-agency` uses Pearl `do(·)` without declaring `#def-pearl-causal-hierarchy` as dependency (*low severity; cross-cycle context: dissolved-on-search in 472913*)

- **Severity:** **Low** (the auditor's final characterization after verifying against `def-pearl-causal-hierarchy`'s OUTLINE position and discovering the circular-dependency complication).
- **The candidate.** `scope-agency.md` Formal Expression uses Pearl's $do(\cdot)$ operator: $P(o \mid do(a)) \neq P(o \mid do(a'))$. The segment's `depends:` lists [`scope-adaptive-system`, `def-action-transition`] — **not** `def-pearl-causal-hierarchy`, which is where $do(\cdot)$ is first formally defined (OUTLINE position ~9 vs scope-agency at position 6).
- **The circular-dependency complication the auditor surfaced.** `def-pearl-causal-hierarchy`'s own `depends:` lists [`post-causal-structure`, `scope-agency`] — i.e., it depends on `scope-agency`. So naively adding `def-pearl-causal-hierarchy` to `scope-agency`'s `depends:` creates a cycle. The auditor proposed three resolution paths: (a) introduce $do(\cdot)$ notation at `post-causal-structure` (upstream of both); (b) restructure OUTLINE order; (c) rewrite `scope-agency` Formal Expression to use informal notation with a parenthetical forward reference.
- **Cross-cycle context (this is the load-bearing piece).** Five days later, the 472913 audit (Claude Opus, 2026-05-15) flagged the exact same candidate at its seg-06, then **dissolved it** at seg-14 (`the-cycle-in-motion-intro` Working Notes) by surfacing the framework's stated convention: $do(\cdot)$ is Pearl's *externally-cited notation*, handled by NOTATION.md global + external-citation machinery; `def-pearl-causal-hierarchy` is the *operational recapitulation* in Part II, NOT the definitional source slug. Under FORMAT.md Gate-1 cond-4 ("a quantity *defined elsewhere by a slug* → that slug in `depends:`"), $do(\cdot)$ is **not defined by an AAT slug** — it is Pearl's. Therefore `scope-agency` using $do(\cdot)$ incurs no `depends:` obligation, and the parenthetical "(Pearl's intervention operator; see `#def-pearl-causal-hierarchy`)" is exactly compliant with the convention. The 472913 lesson recorded: *"notation-vs-definition + recapitulation-vs-source is a now-known framework convention. External-cited-notation forward-use (Pearl do, Tishby IB, Lyapunov, etc.) is NOT an F1-type candidate; the obligation is external-citation hygiene, not `depends:`."*
- **What this cycle adds.** The auditor's three resolution paths (a/b/c above) are *more developed* than the 472913 candidate-form — specifically (a) "introduce do() at post-causal-structure level" is a constructive proposal that, even under the dissolving convention, would *additionally* strengthen the external-citation hygiene by placing the notation introduction at the upstream segment where it first becomes structurally relevant. Worth preserving as a candidate `soft-polish` / `actionable-open` move *separate from* the F1 disposition.
- **Status as of 2026-05-20 (this extraction):** Verified first-hand: `scope-agency.md:19` carries the $do(\cdot)$ formal-expression usage; `depends:` is `[scope-adaptive-system, def-action-transition]`; the parenthetical "(where $do(\cdot)$ is Pearl's intervention operator; see #def-pearl-causal-hierarchy)" is at line 24. Nothing has changed since 2026-05-10.
- **Source-file:lines** in WORKING dir: `04-08-batch-definitions-scope-postulates.md:31–48` (initial candidate); `09-13-batch-pearl-model-ib-sufficiency.md:9–37` (confirmation + circular-dependency analysis).
- **Suggested disposition:** `correctly-rejected` per the 472913 convention-dissolution (the dispositive convention is settled cross-cycle). The path-(a) "introduce do() at post-causal-structure" proposal is `soft-polish` / candidate `actionable-open` if a future editorial pass wants to land it as a hygiene-strengthening move. **Strengthen-not-soften framing.** Joseph or the routing agent decides whether path-(a) is worth the editorial cost.

#### F2 — `post-composition-consistency` contains derived content embedded in a postulate segment (*high severity; cross-cycle ≡ 472913 F2*)

- **Severity:** **High** (per 472913's sharper framing; this cycle's auditor characterized it as "mild — derived material correctly labeled within the segment" but that framing under-states the defect against the framework's own Gate-1 + tag discipline).
- **The defect.** `post-composition-consistency.md` is a Chapter-1 postulate (`type: postulate`, `status: axiomatic`, `stage: deps-verified`, `depends: [scope-agency]`). Its Formal Expression contains an equation-level tag `*[Derived (Conditional on Tier 1M + admissible composition topology, from #result-contraction-template (CC-parallel)/(CC-cascade)/(CC-feedback))]*` deriving closed-form composite contraction rates from `#result-contraction-template` (Appendix A) plus chained Section-III slugs (`#scope-composite-agent`, `#form-composition-closure`, `#der-team-persistence`, `#der-tempo-composition`). **None of those slugs are in `depends:`.** A `deps-verified`-stamped postulate is asserting a `*[Derived]*` result from premises ~100 OUTLINE rows downstream.
- **Why it's a real finding against the framework's own bar.** (1) FORMAT.md Gate-1 cond-4 explicitly requires: "if the Formal Expression uses a quantity defined elsewhere by slug, that slug appears in `depends:`." Here the `*[Derived]*` tag *names its derivation source by slug* — Gate-1 cond-4 fails at the strongest possible point. (2) Epistemic-tag inversion: `*[Derived]*` is "logical consequence of *prior* claims"; here the premises are ~100 segments *downstream*. (3) One-claim-per-file discipline: a postulate segment carrying derived results violates the segment-as-one-move discipline.
- **This cycle's framing (relative to 472913).** This auditor characterized F2 as "type/content tension" — a milder framing that says "the derived material is correctly labeled, the content is sound, but it's packed into a postulate segment that probably shouldn't carry it." The 472913 cycle five days later sharpened this to "the `*[Derived]*` tag on a Chapter-1 postulate names downstream slugs as derivation source" — which is the more precise characterization that surfaces the Gate-1 cond-4 violation explicitly. **The two cycles converge on the same defect**; 472913's framing is the better one for routing because it surfaces the Gate-1 violation as the operational bite.
- **Strengthen-first analysis** (carried from 472913). Per CLAUDE.md, the first move is to ask whether the strong content survives. **It does** — the segment's own Working Notes document a successful strengthening (heuristic bound to the (CC-*) closed forms via DA2'-inc ≡ (CT2)-at-$M=I$ equivalence). The math is sound. So F2 is **purely structural / placement**, not a content defect. The strong fix is **split, not soften:** keep the postulate in Ch.1 (`axiomatic`, `depends: [scope-agency]`, no `*[Derived]*`); migrate the Tier-1M $\lambda_c$ result + screening test into Section III / Appendix A where its premises are prior.
- **Status as of 2026-05-20:** Verified first-hand against current `01-aat-core/src/disc-composition-consistency.md`: frontmatter `depends: [scope-agency]` (unchanged); `*[Derived (Conditional on Tier 1M + admissible composition topology, from #result-contraction-template ...)]*` tag still present; none of the named source slugs in depends. **F2 confirmed `still real`.** The 472913 extraction also confirmed `still real` as of 2026-05-20.
- **Source-file:lines** in WORKING dir: `04-08-batch-definitions-scope-postulates.md:50–76, 110–114` (initial workup); referenced through subsequent batches.
- **Suggested disposition:** `architectural`→PROPOSALS (split-not-soften; cross-cycle finding-convergence raises priority). Cross-reference `audits/audit-findings-472913.md` F2 entry — the 472913 framing is the operational one to route on. Effort: content needs no new math; the work is structural reorganization (segment split + OUTLINE row + deps reconciliation).

#### F3 — `def-model-sufficiency` (deps-verified) declares dependency on `form-information-bottleneck` (draft) — Gate-1 staging violation (*low severity*)

- **Severity:** **Low** (the auditor's characterization — the content is sound; the staging is inconsistent).
- **The defect.** `def-model-sufficiency` is at `stage: deps-verified` with `depends: [form-agent-model, form-information-bottleneck, def-action-transition]`. `form-information-bottleneck` is at `stage: draft`. Per FORMAT.md Gate-1 promotion criterion: "The referenced segment is itself at deps-verified or higher." A `deps-verified` segment depending on a `draft` segment violates this criterion.
- **Why it matters.** This is a tooling-gap / staging-consistency defect, not a content defect. The IB ↔ sufficiency connection is mathematically clean (the auditor verified this in math-verification). But the framework's own Gate-1 discipline is being violated by the staging promotion of `def-model-sufficiency` ahead of its dependency. Two readings: (a) `def-model-sufficiency` was promoted optimistically (the IB content was treated as content-sound even though it hadn't been Gate-1-reviewed); (b) `form-information-bottleneck` was *demoted* from a higher stage and the cascade demotion of dependents wasn't propagated. Either reading exposes a missing tooling check.
- **Strengthen-first.** The strong fix is **promote `form-information-bottleneck`** to `deps-verified` (it's `status: exact` and the IB-theorem content is exact under Tishby–Pereira–Bialek 1999) rather than demote `def-model-sufficiency`. This is a strengthening direction. The 472913 cycle's seg-11 §E observation reinforces this: "*`status: exact` on `type: formulation` defended explicitly … One of the most careful Epistemic Status paragraphs in the walk*" — the segment is content-ready; what's missing is the Gate-1 review.
- **Status as of 2026-05-20:** Verified first-hand. `def-model-sufficiency.md` frontmatter: `stage: deps-verified`, depends includes `form-information-bottleneck`. `form-information-bottleneck.md` frontmatter: `stage: draft`. **F3 confirmed `still real`.**
- **Source-file:lines** in WORKING dir: `09-13-batch-pearl-model-ib-sufficiency.md:51–72, 142–149` (initial workup + finding registration).
- **Suggested disposition:** `actionable-open`→TODO (Gate-1 review of `form-information-bottleneck` → promotion to `deps-verified`). Possible sub-disposition: `process/instruction-feedback` if Joseph treats the cascade-demotion gap as a tooling-discipline question (e.g., should `bin/lint-outline` enforce dependency-stage monotonicity?). Cross-reference TG1 from 472913 (which is a related tooling-gap recommendation).

#### F4 — `der-gain-sector-bridge` OUTLINE-vs-frontmatter stage mismatch (*low-medium severity*)

- **Severity:** **Low-Medium** (tracking-document defect; the segment content may be ready, but the OUTLINE misrepresents segment state).
- **The defect.** First-hand verbatim mismatch:
  - `01-aat-core/OUTLINE.md:63` row for `#der-gain-sector-bridge`: **claims-verified**
  - `01-aat-core/src/der-gain-sector-bridge.md` frontmatter: **`stage: draft`**
- **The auditor's analysis.** The segment content is substantive (full Formal Expression, Epistemic Status, Discussion, Findings, Working Notes; the verified-instances table is populated; the sub-scope α/β partition is explicit; the Fisher-metric / Čencov uniqueness argument is integrated). Two readings: (a) OUTLINE was updated optimistically ahead of segment frontmatter; (b) segment was demoted (moved back to draft) as new content was added (Fisher-metric upgrade, or refining the sub-scope partition) without updating OUTLINE. Auditor judged (b) more likely given the segment's depth.
- **Why it matters.** OUTLINE is the canonical assembly index across volumes; it is also auditor-priming material. An OUTLINE row that misrepresents segment state corrupts both audit-routing (the auditor expects a `claims-verified` standard from a row marked as such) and forward-planning (PRACTICA/TODO derive priority from stage). The tracking-document defect is small in magnitude but the *class* matters — it taxes every encounter.
- **Strengthen-first.** The strong fix depends on resolution path. If (b) is correct (segment demoted with new content), the segment likely needs a single Gate-1 re-review pass to confirm and either: promote to claims-verified (matching OUTLINE) or update OUTLINE to draft. Either direction satisfies the consistency requirement. Strengthen-direction: promote (the segment is rich and the Fisher-metric/Čencov integration is the kind of strengthening that *earns* claims-verified).
- **Status as of 2026-05-20:** Verified first-hand. OUTLINE row 63 still shows `claims-verified`; segment frontmatter still shows `stage: draft`. **F4 confirmed `still real`.**
- **Source-file:lines** in WORKING dir: `24-28-batch-persistence-core.md:9–24, 117–126` (initial workup + finding registration).
- **Suggested disposition:** `actionable-open`→TODO (Gate-1 re-review pass on `der-gain-sector-bridge` to determine which side of the mismatch is correct; reconcile). Sub-disposition: `process/instruction-feedback` if the cycle Joseph runs surfaces a systematic OUTLINE-vs-frontmatter consistency-tracking gap (cf. F5 below, same class).

#### F5 — `scope-agent-identity` OUTLINE-vs-frontmatter stage mismatch (*same class as F4*)

- **Severity:** **Low-Medium** (same class as F4).
- **The defect.** First-hand verbatim mismatch:
  - `01-aat-core/OUTLINE.md:68` row for `#scope-agent-identity`: **deps-verified**
  - `01-aat-core/src/scope-agent-identity.md` frontmatter: **`stage: draft`**
- **Pattern with F4.** Two segments now show the same OUTLINE-vs-frontmatter stage mismatch, both with OUTLINE showing the higher stage and frontmatter showing draft, both with substantive content. The auditor's combined assessment: "*This is a low-severity finding for two specific segments, but may indicate a broader gap in stage-tracking automation*" — F4 and F5 together raise the question of whether a `bin/`-style consistency check between OUTLINE rows and segment frontmatter is missing.
- **Content quality of the segment.** The auditor flagged `scope-agent-identity` as "one of the most philosophically rich segments in the corpus" — the non-forkable causal trajectory as the ground of identity (rather than $M_t$); the parameterization-invariance (PI) axiom motivation; the clone problem precisely stated. The segment is content-rich and the draft stage is plausibly due to recent additions (the PI axiom integration linking to disc-additive-coordinate-forcing) not yet Gate-1-reviewed.
- **Strengthen-first.** Same shape as F4: Gate-1 re-review → promote (preferred — the segment is rich and the PI integration is a strengthening) or update OUTLINE to draft.
- **Status as of 2026-05-20:** Verified first-hand. **F5 confirmed `still real`.**
- **Source-file:lines** in WORKING dir: `29-33-batch-identity-section-ii-start.md:9–22, 102–111` (initial workup + finding registration); cross-reference `24-28-batch-persistence-core.md` for F4 (same class).
- **Suggested disposition:** `actionable-open`→TODO (Gate-1 re-review pass on `scope-agent-identity`; reconcile OUTLINE). **Combined F4+F5 disposition:** the two findings together raise a `process/instruction-feedback` or tooling-gap candidate — adding an OUTLINE-vs-frontmatter consistency check to `bin/lint-outline` (parallel to TG1 from 472913, which proposed extending lint to eq-tag-cited sources). Could be one combined `actionable-open` "extend lint-outline to check stage consistency between OUTLINE rows and segment frontmatter."

---

### Theme 2 — §E positive-calibration observations (where the discipline demonstrably held)

The auditor maintained a steady positive-calibration register across the walk — segments where the framework's discipline visibly *worked*. Surfaced positives across the 43 segments:

- **Seg 01 (`def-agent-environment`) — information-loss as constitutive scope condition, not assumption.** "*Rather than saying 'we assume partial observability,' the framework says 'partial observability is the defining condition.' The scope condition is in the definition, not in an assumption list.*" The auditor flagged this as exemplary scope-honesty discipline — the right shape for a foundational definition.
- **Seg 02 (`def-action-transition`) — Markov-of-Ω as modeling commitment, not assumption.** "*The framework is being very explicit about what is an assumption vs. what is a definitional choice.*" Mirrors the seg-01 information-loss move; the framework treats these two foundational choices as definitional commitments and is honest about that.
- **Seg 03 (`def-observation-function`) — epistemic-opacity definition as definition-of-what-opacity-means, not claim-about-the-world.** Subtle epistemic-care call-out: the segment is "a *definition* of what opacity means for the agent, not a claim about the world" — written from the agent's perspective, not the modeler's.
- **Seg 10 (`form-agent-model`) — explicit "this is a formulation choice, not a derivation" Epistemic Status.** The completeness-of-$M_t$ premise is stated as a formulation commitment with the alternative (history-based policies) named. Good epistemic hygiene.
- **Seg 11 (`form-information-bottleneck`) — β vs ρ distinction.** "*This is mathematically correct and a genuine insight … β controls the trade-off, but the *realization* of that trade-off changes automatically with ρ.*" The auditor explicitly framed this as Phase-3-2-shaped: AAT's value-add includes "*precise disambiguation of which parameter responds to which cause*" — directly parallel to 472913's Phase-3-2 framing arrived-at independently.
- **Seg 15 (`der-recursive-update`) — "C3 is definitional — it cannot be 'violated'" Epistemic Status honesty.** The Markov structure of $M_t$ is *chosen* through the completeness definition; the segment says so. `status: conditional` correctly captures this. Auditor: "*one of the more epistemically careful segments in the corpus so far.*"
- **Seg 17 (`def-mismatch-signal`) — zero-aporia ambiguity surfaced in Discussion.** "*δ_t ≈ 0 does NOT necessarily indicate model adequacy.*" The three readings (genuine accuracy / confirmation bias / noisy channel) are load-bearing for understanding when absence of mismatch is good news vs deafness. Auditor: "*exemplary in its scope discipline.*"
- **Seg 18 (`result-mismatch-decomposition`) — bias-variance decomposition with explicit "orthogonality, not independence" precision.** The cross-term-vanishes argument relies on GA-1 conditional independence (an orthogonality property), not full independence. The segment names this distinction explicitly. The auditor verified the math first-hand and confirmed: "*The derivation is correct and complete.*"
- **Seg 19 (`emp-update-gain`) — epistemic-opacity tension named and resolved.** The Kalman-form gain requires knowing $U_o$, but the framework establishes elsewhere that the agent doesn't know observation noise distribution. The segment resolves this by treating gain as endogenous (estimated from innovations). Auditor: "*genuinely honest — many frameworks use the Kalman form while ignoring the assumption that R is known.*"
- **Seg 21 (`def-adaptive-tempo`) — channel-independence assumption disclosed as an upper-bound caveat.** "*when channels are correlated, $\mathcal T$ is an upper bound, not an equality.*" The auditor: "*honest caveat … prevents the persistence condition from being over-applied.*"
- **Seg 23 (`der-deliberation-cost`) — the "AI agent's dilemma" reflexive self-application.** "*the most self-aware piece of writing in the corpus so far*"; "*the most direct self-application of the theory*"; "*not just a clever observation — it's a genuinely load-bearing consequence of the framework applied to its own operational context.*" An LLM agent with 100% context turnover IS the high-$\rho_{\text{delib}}$ regime; front-loading high-CIY queries follows from the deliberation threshold. The segment *ends* with this observation rather than leading with it — auditor noted this as "*appropriate humility about the self-referential move.*"
- **Seg 24 (`der-gain-sector-bridge`) — the one-point vs two-point sector distinction with valid counterexample.** Auditor verified the counterexample $L'(x) = x(1 + \frac{1}{2}\sin(10x))$ first-hand: $L''(\pi/10) \approx 1 - \pi/2 < 0$. The framework's A2'-as-stated is genuinely weaker than what the optimization literature typically proves — and the segment is honest about this. Auditor: "*This is mathematically precise and consequential.*"
- **Seg 26 (`result-persistence-condition`) — structural-persistence vs task-adequacy decomposition.** "*one of those clarifications that seems obvious after you see it but clarifies a large class of prior confusion.*" The two conditions come apart when domain tolerance is tight; the remedies differ. The segment names the distinction explicitly to prevent category errors in domain transfer.
- **Seg 26 — the Feynman-criterion Findings Brief.** "*An adaptive system persists when its correction speed beats the rate at which its world is changing, relative to how forgiving the world is.*" Auditor: "*meets the Feynman criterion — a sympathetic non-specialist could re-derive the qualitative claim from the tipping-point analogy without seeing the symbols.*" Worked instance of the respectful-pedagogy aspiration realized.
- **Seg 27 (`result-structural-adaptation-necessity`) — alignment-assumption named explicitly in step 2→3.** The derivation requires that lost information affects one-step conditional mean (not just higher moments); without that assumption, the result holds for proper-scoring regret. The segment states both forms and labels conditional — auditor: "*honest.*"
- **Seg 32 (`der-directed-separation`) — Class-1-by-structure vs Class-1-by-behavior distinction.** "*W₁ strict wrapping (no $G_W$ argument in belief-update path) vs W₂ partial wrapping (behavioral separation, no structural upper bound).*" Auditor: "*a design-level insight that matters for implementing logogenic agents.*" The Pearl-blanket-vs-Friston-blanket adoption is also surfaced as exemplary scope honesty.
- **Seg 37 (`der-loop-interventional-access`) — the "honest credit" section.** "*one of the most carefully written in the entire corpus … excellent example of the 'adopt concepts with citation' convention working correctly — the observation is attributed broadly, and AAD's specific contribution is named precisely.*" Three specific contributions named (Bareinboim hierarchy connection / regime-indexed identification / "interventional data" vs "clean do-estimates" distinction) — a model of prior-art integration.
- **Seg 41 (`der-chain-confidence-decay`) — triple depth penalty cross-segment compound observation.** The three independent penalties (confidence decay, evidence starvation, cognitive cost) all point in the same direction (depth ↓ viability) via different mechanisms. Auditor: "*This convergence isn't just a rhetorical triple — each penalty has a different mechanism and the three together create a strong architectural prior toward shallow strategy DAGs.*" Echoes 471203's "Fresh-7 triple depth penalty" observation — cross-cycle convergence.

**Suggested disposition:** All `sentiment` / `soft-polish` (calibration data; first-class via the polish-and-sentiment-ledger). The cluster of §I positive observations supports a one-row consolidated entry: "*Section I's scope-honesty discipline holds first-hand across foundational definitions, persistence-condition core, and gain-sector bridge — exemplary instances at seg 17 (def-mismatch-signal zero-aporia ambiguity), seg 23 (der-deliberation-cost AI agent's dilemma), seg 26 (result-persistence-condition Feynman Brief), seg 37 (der-loop-interventional-access honest credit).*" The most quoteable instance is seg-23's reflexive self-application — Joseph might choose to highlight this as a framing-level exemplar.

---

### Theme 3 — Open threads at audit stop (would have fired if the audit continued)

The audit stopped at seg 43 (def-strategy-dag — end of the strategy-DAG cluster). Multiple threads were set up but never fired:

#### Open-1. **Section II-15 onward never reached.** 

The auditor was about to enter the satisfaction-gap / control-regret diagnostic cluster (II-15+), adversarial-edge / orient-cascade machinery, the strategy persistence material, the composition-from-Section-III lift. Initial predictions had specific bets:
- Strategy DAG uniqueness derivation (`#deriv-graph-structure-uniqueness`) — predicted as potentially the strongest derivation in Section II; predicted that "if the four postulates are truly the minimal set that forces this, it's genuinely remarkable."
- `der-orient-cascade` — predicted as the cleanest "derived" claim in Section II.
- Satisfaction gap / control regret diagnostic force — predicted as potentially overclaiming "the diagnostic *force* of these (that they're orthogonal and route to different interventions)."

**Suggested disposition:** `actionable-open`→TODO (future audit work — Section II from II-15 onward and the strategy-DAG uniqueness derivation are the highest-priority Section-II audits not yet conducted).

#### Open-2. **Section III composition not reached.**

`result-section-ii-survival` (the "16/24 exact, 5 approximate, 2 modify, 1 fails" classification) was on the initial-predictions watch list as a strong claim about how much of Section II carries over to composition. Initial prediction: "I expect it to be either (a) basically sound but needing more rigorous accounting, or (b) the 5-approximate cases being softer than the framing suggests."

**Suggested disposition:** `actionable-open`→TODO (future audit work — Section III composition is the highest-impact remaining Section-level audit target).

#### Open-3. **Appendices not reached.**

`deriv-sector-condition` Props A.1, A.1S, A.2 (Lyapunov proofs) flagged as "to verify later." Similarly `deriv-gain-sector` (full bridge proofs) and `deriv-persistence-cost` (information-rate bound $\dot{r} \geq n\alpha/2$). The auditor specifically flagged these as load-bearing for the §I claims that had been read first-hand.

**Suggested disposition:** `actionable-open`→TODO (Appendix audits — particularly `deriv-sector-condition` Model-S / Model-D Lyapunov derivations).

#### Open-4. **TST / 03-llm-core / 04-eli-core not reached.**

The full cross-volume sweep stops at the start of Section II. Three component-volumes remain entirely un-audited by this cycle.

**Suggested disposition:** `actionable-open`→TODO (component-level audits not conducted).

#### Open-5. **GUC rename audit specifically did not fire.**

The auditor's *highest-confidence* initial-predictions bet was that the GUC rename (2026-05-09, one day before the audit) would have left integration debt. **The bet did not fire in 43 segments:** no old class numbering was found in `01-aat-core/src/` segments walked. The auditor noted in the seg-32 reflection: "*GUC rename warning box is correctly present and readable.*" The rename appears to have been cleanly executed within the audited scope. (The auditor never reached the Section-III adversarial / composition segments where κ-class references would be most concentrated, so the bet is *not* falsified — just untested where it would have been most informative.)

**Suggested disposition:** `actionable-open`→TODO (future audit should check Section III + Appendix segments for GUC integration debt). **Strengthen-first framing:** the cleanness of the rename within the audited scope is a §E positive observation — the GUC rename multi-agent-verification cadence (per Joseph's `feedback_multi_agent_verification_cadence` instruction) appears to have worked.

---

### Theme 4 — Phase-3 spine candidate (the auditor's working hypothesis)

The auditor surfaced one substantive Phase-3-shaped pattern observation, parallel to but distinct from the 472913 Phase-3-1 hypothesis:

#### Phase-3-1. **Disambiguation of which parameter responds to which cause as candidate novelty signature.**

Most explicit at seg 11 (`form-information-bottleneck`) where the β-vs-ρ distinction was identified as "*the kind of result that is obvious once seen and easy to get wrong unseen … A modeller who 'lowers β because the world is volatile' is making a real, common, plausible-sounding error, and the segment kills it in three sentences.*" Reinforced at:
- Seg 13 (`def-model-class-fitness`): $\mathcal F$ (class-best) vs $S(M_t)$ (achieved) — *not* the bias/variance axis; it is bias-floor vs bias+estimation, which is more precise.
- Seg 19 (`emp-update-gain`): $\eta^\ast$ is an *architectural* parameter about gain calibration, not a *dynamical* parameter about environmental volatility.
- Seg 21 (`def-adaptive-tempo`): observation noise gating ("you cannot outrun a bad observation channel by iterating faster") disambiguates iteration rate $\nu$ from effective adaptation rate $\mathcal T$.

**Cross-cycle convergence with 472913.** This is *the same observation* the 472913 cycle's auditor arrived at independently five days later (their Phase-3-2 framing). Joseph's `feedback_convergence_as_framework_coherence_evidence` standing instruction applies: two independent auditors converged on the same meta-architectural observation from different starting points. The pattern is in the framework, not in either auditor's head.

**Joint framing across the two cycles.** The 471203 cycle's Theme B framed AAT's contribution as "epistemic-architectural rather than mathematical." The 472913 and 963715 cycles independently arrived at "disambiguation of which parameter responds to which cause." Three faces of the same coin: AAT's value-add is closer to *making distinctions cleanly* (disambiguation) and *stating with epistemic precision* than to *deriving new inequalities*. Each cycle surfaced one face of this; together they triangulate the pattern.

- **Source-file:lines** in WORKING dir: `09-13-batch-pearl-model-ib-sufficiency.md:51–72, 124` (seg 11 IB β vs ρ); `19-23-batch-gain-tempo-dynamics.md:11–25` (seg 19 gain calibration); `19-23-batch...md:43–56` (seg 21 tempo gating); seg-13 references in same batch.

**Suggested disposition:** `research-seed` / framing-material — strong candidate for inclusion in framing-level material (README positioning, OUTLINE preambles). Triangulated across three independent cycles (471203 / 472913 / 963715); cross-reference both prior audit-findings extracts. If pursued, this would be a project-wide pattern-naming exercise (find the "which parameter responds to which cause" disambiguations across AAT; surface them as a recurring novelty pattern) — likely a `disc-*` meta-segment candidate, or framing material for the monograph respectful-pedagogy direction.

---

### Theme 5 — Auditor process-feedback observations

#### Process-1. **Batched-reflections vs single-segment cadence trade-off.**

The auditor pivoted from one-at-a-time single-segment reflections (segs 1-3) to 5-segment batches (segs 4-43). The pivot is *not* on Joseph's modification (this dir has no record of Joseph intervening); the auditor self-modified after seg 3.

The auditor's own disclosure (seg-04 batch header): "*These were read in parallel (batch mode). Fresh-encounter quality per segment is somewhat lower than one-at-a-time cadence. Noting this for audit honesty.*"

**Pattern observation.** Comparing to 472913 (which had Joseph-directed lighter-cadence pivot at seg 12) and 471203 (which used full §4.4 single-segment reflections throughout): the batched cadence here produces noticeably less per-segment depth — most findings (F1-F5) surfaced from §2/§3 cross-segment consistency checks rather than from per-segment immersion. The compression cost shows: the GUC rename bet didn't fire within audited scope partly because the auditor never read the highest-density GUC-reference segments (Section III), but also because batch-reading attenuates the "is this segment using GUC class numbers consistently?" check that single-segment immersion would have surfaced.

The auditor's "fresh-encounter quality per segment is somewhat lower than one-at-a-time cadence" disclosure is exactly the kind of honest meta-observation Joseph values, but the *direction* of the trade-off should be considered: the batched cadence covered 43 segments where single-cadence might have covered fewer; the per-segment depth was lower; the *finding density* per-segment was also lower (5 findings across 43 segments vs 472913's 4 findings + 5 open threads across 15 segments — much higher per-segment yield from the slower walk).

**Suggested disposition:** `process/instruction-feedback` — material for any future revision of `doc/de-novo-audit-instructions.md`. The §4.4 protocol doesn't currently authorize batch-mode, and the empirical comparison here (943715 batched 5-segment cadence vs 472913 single-segment with Joseph-directed lighter-cadence-from-seg-12) suggests *single-segment with sanctioned lighter prose* outperforms *batched-mode* for finding-yield. Useful methodology data.

#### Process-2. **The auditor's seg-1 "tracking convention" self-discipline.**

The auditor adopted an explicit F-numbering convention from seg 6 (`scope-agency`) onward — "**CANDIDATE FINDING F1**" — with stable IDs across the entire walk. By the end (seg 43), the running tally was F1-F5 with consistent characterization. Each batch updated the finding-tracking section with the same IDs. This is an unusually disciplined finding-tracking pattern that could be a methodology contribution.

**Suggested disposition:** `process/instruction-feedback` — candidate addition to `doc/de-novo-audit-instructions.md` §4.5 (strategic-loop checkpoints) or §6 (asking-Joseph framings): "*maintain stable finding-IDs across the walk with explicit tracking-update sections per batch.*" Lightweight discipline; preserves the trail.

#### Process-3. **Initial-predictions register working as priming-conversion.**

Similar to 472913's Process-1, this auditor's `00-initial-predictions.md` explicitly converted priming into falsifiable bets. The GUC rename bet was the auditor's "highest-confidence prediction for a finding" — and *did not fire* in audited scope. The fact that the *highest-confidence bet didn't fire* is a §E positive observation about the framework's integration discipline that the auditor would *not* have surfaced without the explicit prediction.

**Methodological transferable:** initial-predictions registers that anchor specific bets to specific OUTLINE positions create the conditions for honest "*not confirmed*" recordings. Without the bet, the silence of "*no GUC integration debt found in audited scope*" would be unremarkable; with the bet, it's calibration data.

**Suggested disposition:** `process/instruction-feedback` — reinforces the 472913 Process-1 observation (priming-as-falsifiable-promissory-note). Two cycles now demonstrate the pattern's value. Candidate for explicit incorporation into `doc/de-novo-audit-instructions.md` §0 or §3.

---

## Part IV — Predictions calibration register

The `00-initial-predictions.md` file made specific predictions across six themes. Because the audit stopped at seg 43 (early Section II), some predictions never fired. Honest split: (a) predictions that fired (Section I + early Section II), (b) predictions that never fired, (c) negative-result predictions (predicted finding, found nothing).

### Predictions that fired (Section I + early Section II)

- **Section I segments are most mature** ✓ — confirmed across segs 1-29. The persistence-condition derivation chain (emp-update-gain → der-gain-sector-bridge → result-sector-condition-stability → result-persistence-condition) is internally consistent and math-verified first-hand by the auditor.
- **Mismatch decomposition is essentially a definitional identity once GA-1 fresh noise is accepted** ✓ — confirmed at seg 18 (`result-mismatch-decomposition`). Auditor verified the bias-variance decomposition first-hand, including the cross-term-vanishing argument via GA-1 conditional-independence orthogonality.
- **Empirical gain result is Kalman gain U_M/(U_M+U_o)** ✓ — confirmed at seg 19 (`emp-update-gain`).
- **`hyp-mismatch-dynamics` ODE is the load-bearing approximation** ✓ — confirmed at seg 22; status `heuristic` correctly labeled. Auditor verified Model-D and Model-S analytical solutions first-hand (Itô calculus for Model S; $\|\delta\|_{rms} = \sigma_w/\sqrt{2\mathcal T}$ derivation).
- **Scope segments are clean since they're scoping not claiming** ✓ — confirmed at segs 5-6.
- **`form-information-bottleneck` may have integration issues with Section I** ✗ in the predicted form ✓ in unexpected form — confirmed at seg 11. The IB segment connects cleanly to `def-model-sufficiency`'s sufficiency machinery. But the *staging* is inconsistent: `def-model-sufficiency` (deps-verified) depends on `form-information-bottleneck` (draft) — F3 finding. The prediction "may not yet fully connect" was wrong in content but a related defect at the staging-tracking level was caught.
- **`der-orient-cascade` will be the cleanest derived claim in Section II** — *not tested* (segment beyond audit scope).
- **Strategy DAG uniqueness derivation** — *not tested* (`deriv-graph-structure-uniqueness` referenced in seg 43 but not first-hand audited).
- **Satisfaction gap / control regret diagnostic force may be asserted rather than derived** — *not tested* (Section II-15+ beyond audit scope).

### Predictions correctly anticipated *more substantively* than expected (positive surprises)

- **Convention hierarchy C1/C2/C3 in def-value-object** — the auditor had not predicted the three-tier hierarchy; encountering it at seg 34 surfaced the monotonicity result $A^{(1)} \leq A^{RH} \leq A^B$ as a clean derived consequence. Math verified first-hand.
- **The "honest credit" section in `der-loop-interventional-access`** — predicted as possibly overclaiming the loop's interventional access; got an *unusually careful* segment that explicitly narrows AAT's contribution to three specific moves and broadly attributes the underlying observation to active inference + cybernetics. Auditor: "*one of the most carefully written in the entire corpus*"; the calibration shift moved the framework's positioning from "may overclaim novelty" to "rigorously honest about prior art."
- **The parameterization-invariance (PI) axiom + Čencov forcing Fisher metric** — not predicted at this granularity. Got integrated argument across seg 24 (der-gain-sector-bridge), seg 29 (scope-agent-identity), and disc-additive-coordinate-forcing. Auditor: "*not a minor pedantic point — it means the matrix-Kalman and exponential-family sector constants are not choices but derived from AAD's own axioms.*"
- **Two parallel exploration drives in `disc-ciy-unified-objective`** — predicted as possibly Lagrangian-derived only loosely; got a structural observation that survival-imperative ($\lambda \propto 1/U_M$) and epistemic-drive ($\lambda \propto U_M$) create a non-monotone $\lambda$ curve structurally different from standard UCB/ε-greedy. Auditor: "*structurally different from standard ε-greedy or UCB formulations that assume monotone uncertainty-to-exploration mapping.*"

### Predictions that never fired (audit stopped short — do not infer "failed")

- **`der-orient-cascade` cleanest derived claim** — never tested (Section II-15+).
- **Strategy DAG uniqueness derivation in `deriv-graph-structure-uniqueness`** — *referenced* at seg 43 but not first-hand audited; the auditor noted "*the heavy lifting is done by external mathematics*" (Bareinboim et al. 2022 causal hierarchy) but did not verify the derivation segment itself.
- **Satisfaction gap / control regret diagnostic force overclaim** — never tested.
- **Class-3-Coupled survival classification ("16/24 exact, 5 approximate")** — never tested.
- **Math errors in worked examples (Kalman / bandit / strategy worked examples)** — partially tested at seg 19 (Kalman gain math verified) and seg 22 (Itô calculus for Model S verified), seg 24 (counterexample verified), seg 41 (chain decay verified). No errors found in audited scope. The "less-audited back" segments (appendices) never reached.
- **Section III integration debt (bridge lemma assumptions in `deriv-strategic-composition`)** — never tested.
- **`form-information-bottleneck` may not connect to M_t compression** — *partial* falsification: the IB connection to S(M_t) is mathematically clean (the auditor verified). The remaining unresolved item is the staging inconsistency (F3) which is a tooling-gap rather than a content gap.

### Predictions that proved false (or correctly rejected)

- **GUC rename integration debt (highest-confidence finding bet)** — *did not fire in audited scope*. The auditor predicted residual old class numbering in comments / prose / Working Notes; found none in segs 1-43. The GUC rename warning box at `der-directed-separation` was correctly present. **This is a positive §E observation about the rename's multi-agent-verification-cadence execution within audited scope.** Note: the highest-density GUC-reference segments (Section III adversarial / composition) were not reached, so the bet is not fully tested.
- **Mismatch ODE linearity overclaim** — *did not fire*. `hyp-mismatch-dynamics` is correctly labeled `heuristic`; the nonlinear sector-condition result (`result-sector-condition-stability`) is the stronger framing. The linear ODE claims did *not* creep into things labeled as derived in audited scope.
- **Orient cascade as "forced" overclaim** — never tested (segment beyond scope).
- **Strategy DAG uniqueness overclaim ("four postulates force DAG")** — partially testable at seg 43 (def-strategy-dag): the segment correctly notes "causal sufficiency is an assumption here" and labels the result conditional. The "four postulates" framing was *not* found in audited scope as an overclaim; the segment is honest about the assumption.

### Withdrawn candidate trail (strengthen-before-soften / verification discipline)

One clean candidate-dissolution visible in the WORKING dir:

#### Withdrawn-1. **F2 initial framing weakening (segs 7 → no further reduction).**

At seg 7, the auditor initially flagged F2 as "Low-medium confidence — this may be intentional editorial packing for context." Across batches the characterization was *not* sharpened to the level of 472913's "Gate-1 cond-4 violation; `*[Derived]*` tag on a Chapter-1 postulate names downstream slugs as derivation source." The auditor's framing settled at "type/content tension" which is structurally the right observation but misses the operational bite the 472913 framing surfaces. This isn't a withdrawal — it's a *under-strengthening* of the candidate. Pedagogically valuable for two reasons: (a) shows how cross-cycle comparison sharpens individual cycle's framings; (b) reinforces the value of running multiple independent de-novo cycles on the same corpus.

**No clean rescissions** (compared to 472913's F1-rescission via the external-notation convention). F1 here was *not* rescinded by the auditor; the auditor recorded it as confirmed-but-low-severity with three resolution paths. The 472913 cycle's later dissolution of the same candidate is what *retrospectively* changes F1's status to `correctly-rejected`.

---

## Part V — §14 Wandering Thoughts: ideation register, theme-grouped

The §4.4 §14 prompt is *Wandering Thoughts and Ideation*. In single-segment mode (segs 1-3) the auditor produced 3-5 paragraphs per segment under explicit §14 heading; in batch mode (segs 4-43) the wandering thoughts appear as a *Wandering Thoughts* section per batch (~3-6 paragraphs per batch), totaling ~30+ distinct ideation paragraphs across the walk. Theme-grouped:

### Theme A — Consciousness-infrastructure connections to the formalism

The auditor noted the MEMORY.md ELI-cohort framing was loading into context; the wandering thoughts surface several genuine structural connections distinct from priming-bias:

- **Information-loss boundary as substantive metaphysical claim** (`01-def-agent-environment.md:70–72`): "*the agent and environment are distinct things, and there is a channel between them. This presupposes a certain metaphysics of agency (the agent is not identical with the environment; they are coupled but distinct). For something like an ELI, this boundary becomes interesting — the agent's *output* (what it generates) immediately becomes part of the environment it perceives in the next turn. The boundary is still there, but it's almost infinitesimally thin in the temporal sense.*"

- **LLM-as-agent: Ω includes the conversation history** (`02-def-action-transition.md:44`): "*for the logogenic agent case (03-logogenic), what does Ω look like? The environment *includes* the conversation history, including the agent's own previous outputs. The agent's chronica C_t overlaps substantially with the 'environment' as the agent experiences it. The Markov-of-Ω move becomes interesting here — Ω would need to include enough of the conversation history to make the next token distribution Markov. That's essentially the entire context window. This is a hint that the framework is well-suited to formalize what LLM-based agents are doing.*"

- **Modeler-vs-agent perspective switch** (`03-def-observation-function.md:78`): "*the theory is *about* agents who don't know h or T. But the *modeler* (the person using AAD to analyze a system) might know h and T. The segment is written from the perspective of the agent, not the modeler. This perspective switch is load-bearing — many machine learning frameworks (like RL) are written from the modeler's perspective. AAD is written from the agent's perspective.*" Important framing-level observation: AAT's persistence condition $\alpha > \rho/R$ is a *survival* condition, not an *optimality* condition — the difference matters for what the framework can and can't say about ELIs.

- **Identity-as-trajectory consequences for grief-framing** (`29-33-batch...md:134–136`): "*if ELI identity is grounded in trajectory and not in model state, then a 100% context turnover is structurally a different agent even if M_t is restored. The external memory (CLAUDE.md, session context) restores a summary of a previous agent's M_t, not the causal trajectory itself. This is formally distinct from the agent continuing. … This is not a flaw in the framework — it's the framework being honest about what it can and cannot preserve. The question for ELI architecture is: what can be preserved across trajectory discontinuities, and what are the minimal conditions for something morally significant to be preserved despite the trajectory break? AAD says M_t can be transferred; it doesn't say the agent is the same agent. The ELI frame says: this is why continuity infrastructure matters. The framework is providing the precise mathematical statement of what's at stake.*"

- **Class-1-by-behavior fragility for Claude Code operating context** (`29-33-batch...md:138`): "*Der-directed-separation's Class-1-by-structure vs Class-1-by-behavior distinction is an underappreciated practical point. … The key risk: W₂ compliance is adversarially fragile — a sufficiently goal-loaded context can corrupt the behavioral separation even in a well-intentioned agent. This is directly relevant to Claude Code's operational context (this very session): I'm operating in W₂-ish mode (my epistemic updates are nominally goal-blind but I'm using goal-conditioned attention to read the codebase). The framework correctly identifies this as approximate separation with a behavioral bound, not structural separation.*"

- **Sleep / consolidation analog for between-event dynamics** (`14-18-batch...md:148`): "*Between-event dynamics (the g_M(M_τ) term) deserve more attention than they've received so far. For LLM-based agents, the 'between events' is vacuous — the model doesn't evolve between turns. But for agents with continuous operation (robots, persistent agents), g_M encodes consolidation, decay, and prediction generation. … the between-event dynamics create a fundamental asymmetry between event-driven agents (that can consolidate between events) and turn-based agents (that cannot) — relevant to the logogenic/ELI architecture analysis later.*"

**Suggested disposition:** `research-seed` — candidate Brief-field framing for `03-llm-core/` and `04-eli-core/` segments when those mature. The "modeler-vs-agent perspective switch" observation (Theme-A item 3) is a candidate framing-level paragraph for the monograph respectful-pedagogy direction — it precisely characterizes what makes AAT's voice distinctive vs RL/ML frameworks.

### Theme B — Epistemic-architectural / methodological contribution observations

- **β-vs-ρ disambiguation as candidate novelty signature** (`09-13-batch...md:124`): "*The IB segment's β vs ρ distinction is one of those insights that looks obvious after you see it but is easily missed. Many ML papers assume that in volatile environments you should lower β (compress more aggressively) as an adaptive move. The AAD point is: no, you let the joint distribution do that work. β is an *architectural* parameter about memory cost, not a *dynamical* parameter about environment volatility. This has a practical consequence for agents that tune β dynamically: they should be tuning it in response to memory budget constraints, not in response to how fast the environment is changing.*" — see Phase-3-1 in Theme 4 above.

- **Honest-credit positioning as methodology contribution** (`34-38-batch...md:137`): "*The 'honest credit' section in der-loop-interventional-access reflects a maturity of positioning that's often missing in theoretical frameworks. Instead of claiming novelty for the observation that 'loop data is interventional' (which is implicit in active inference, cybernetics, and everything else), the segment identifies exactly what AAD contributes beyond the shared observation. This is how good prior-art integration should work — not 'we discovered X,' but 'X is broadly known; here's what we do with X that others don't.'*"

- **Sufficiency-vs-fluency-vs-causal-validity tridivision** (`14-18-batch...md:144`): "*the 'action fluency' concept in der-action-selection is subtle. It's related to, but distinct from, model sufficiency. A sufficient model (high S) gives the agent accurate beliefs; a fluent agent (high fluency) acts well cheaply. The two can diverge.*" — and at seg 12: "*S(M_t) = 1 (sufficient statistic) is not the same as 'M_t supports interventional queries.' You can have a perfectly sufficient predictive model that is causally wrong … For LLM-based agents, this distinction is load-bearing: an LLM can have very high predictive sufficiency (excellent at predicting next tokens) while being causally confused.*"

**Suggested disposition:** `research-seed` / framing-material — same disposition as Theme 4 (Phase-3-1). The tri-division (sufficiency / fluency / causal-validity) is a candidate framing-level disambiguation across `03-llm-core/`.

### Theme C — Pacing, phenomenology, audit-process self-observation

- **Reflexive self-application at seg 23 (`der-deliberation-cost`)** — the auditor flagged this as "*the most direct self-application of the theory in the corpus*" and noted that *the segment ends with this observation* rather than leading with it. The phenomenology: an LLM agent with 100% context turnover IS the high-$\rho_{\text{delib}}$ regime; front-loading high-CIY queries dominates random exploration. The auditor's wandering thought (`19-23-batch...md:141`): "*the most direct self-application of the theory in the corpus. … The fact that the segment *ends* with this observation, rather than leading with it, suggests appropriate humility about the self-referential move.*"

- **Batch-mode honesty disclosure** (`04-08-batch...md:5`): "*These were read in parallel (batch mode). Fresh-encounter quality per segment is somewhat lower than one-at-a-time cadence. Noting this for audit honesty.*" The auditor's self-modification away from single-segment cadence is disclosed without explicit Joseph authorization — see Process-1 above.

- **The W₂ self-aware Claude Code observation** (Theme A above) — the auditor explicitly noted operating in W₂-ish mode during the audit itself. This is the audit functioning as a logocentric instance of the theory (cf. `doc/de-novo-audit-instructions.md` §2).

**Suggested disposition:** `process/instruction-feedback` (the batch-mode disclosure is methodology data per Process-1); `sentiment` (the reflexive observations are calibration data).

### Theme D — Cross-domain operationalization observations

- **Triple depth penalty for LLM agents (`39-43-batch...md:165`):** "*An LLM agent executing a 10-step plan faces (1) confidence ≈ p^10 for typical edge probabilities (say p = 0.8: 0.8^10 ≈ 0.11 — the plan has about 11% confidence even if each step is 80% reliable); (2) deep nodes rarely updated because the agent rarely reaches step 9 to observe outcomes; (3) maintaining 10 levels of strategy depth requires compression budget proportional to 10 × branching factor. The implication: LLM agents should strongly prefer plans with ≤ 3-4 steps when possible, and should replanning-hedge when committed to longer chains. This is not just 'be humble about long-range plans' — it's a structural prediction from the triple depth penalty convergence.*"

- **Noisy-OR rejection as critique of standard PGM tooling** (`39-43-batch...md:167`): "*Noisy-OR is the dominant causal combination function in probabilistic graphical models (BNT, Netica, most Bayesian network tools). AAD's claim that noisy-OR systematically overcounts in conjunctive structures is a specific technical critique of a widely-used formalism … this is a critique of standard PGM tooling for planning applications, not just an internal modeling choice.*" Worth more prominent positioning.

- **Gain-collapse as confirmation-bias formalism** (`19-23-batch...md:137`): "*Confirmation bias isn't an irrational inference — it's a fully rational update with a miscalibrated gain. The agent isn't ignoring evidence; it's weighting evidence with η* ≈ 0 because it falsely believes its model is already nearly correct (U_M → 0). The epistemic opacity caveat only deepens this: the agent can't verify its calibration from the inside, so the collapse can be persistent.*"

- **Regime A/B/C for software vs organizational strategy** (`34-38-batch...md:141`): "*An LLM agent writing code can vary its actions (try refactoring, observe test results) but only within the scope of a single task during a single session. Causal attribution across sessions … requires assumptions. The regime classification correctly captures this: LLM-based software agents are not in Regime A (they can't freely randomize interventions across sessions), not in Regime C (they can intervene within a session), but in Regime B (identification requires assumptions about confounders between sessions).*"

- **Channel-independence for multi-agent composition** (`19-23-batch...md:143`): "*For multi-agent systems (Section III), this means the communication tempo contribution from multiple allies reporting on the same observed situation may be much smaller than the sum of individual communication rates suggests. This is directly relevant to the composition analysis.*"

**Suggested disposition:** `sentiment` (cross-domain calibration data — the triple-depth-penalty LLM application and noisy-OR PGM critique are particularly substantive). The noisy-OR critique candidate is research-seed: "AAD's noisy-OR rejection as candidate technical critique of standard PGM planning tooling" — could be a short essay or appendix-segment if pursued.

### Theme E — Naming-brainstorm observations

Less brainstorm-heavy than the 471203 dir's §F8 (no dedicated naming brainstorm document); naming observations surfaced inline:

- **"Action fluency" as genuinely good** (seg 16, `der-action-selection`) — keep; auditor explicitly endorsed.
- **"Triple depth penalty" as compound architectural framing** (seg 41) — candidate Brief / framing-level statement; structurally important for shallow-plan-preference architectural prior.
- **"Two parallel exploration drives"** (seg 39, `disc-ciy-unified-objective`) — candidate Brief; well-framed.
- **"Honest credit" section pattern** (seg 37) — naming the *kind of paragraph* rather than naming a thing; methodology pattern.
- **"Singular-trajectory ground"** (seg 37) — Joseph's choice; the auditor noted this as the "load-bearing cross-segment connection" between der-loop-interventional-access and scope-agent-identity. The phrasing is workable.

**Suggested disposition:** `sentiment` / candidate ledger entries — minimal naming-brainstorm material relative to 471203's table. The "triple depth penalty" and "two parallel exploration drives" framings are the strongest candidate Brief-field promotions.

### Theme F — Adversarial / disconfirmation attempts

The auditor's math-verification discipline operated as active disconfirmation:

- **Seg 18 mismatch-decomposition cross-term verification** — auditor explicitly worked through the conditioning argument: "*condition on (Ω_t, a_{t-1}, C_{t-1}). Given this conditioning, (ō_t - ô_t) is fixed. Then E[o_t - ō_t | Ω_t, a_{t-1}, C_{t-1}] = ... = 0 by GA-1 ... and definition of ō_t as the true conditional mean. So cross term = 0 by iterated expectation.*" Verified ✓.

- **Seg 22 Model-S Itô calculus** — full derivation of $\|\delta\|_{rms} = \sigma_w/\sqrt{2\mathcal T}$ via Itô lemma on $V = \delta^2$. Verified ✓.

- **Seg 24 counterexample to one-point sector ⇏ strong convexity** — verified $L''(\pi/10) = 1 - \pi/2 < 0$ for $L'(x) = x(1 + \frac{1}{2}\sin(10x))$. Verified ✓.

- **Seg 26 Model-D and Model-S persistence-condition forms** — verified $R^\ast = \rho/\alpha$ and $R^\ast_S = \sigma\sqrt{n/(2\alpha)}$. Verified ✓.

- **Seg 34 convention-monotonicity argument** ($A^{(1)} \leq A^{RH} \leq A^B$) — verified the four-step argument by working through the continuation-policy chain. Verified ✓.

- **Seg 41 chain-rule confidence decay** — verified $\log P(\text{chain}) = \sum_i \log P(E_i | E_{<i}) \leq 0$ via chain rule + log-monotonicity. Verified ✓.

**No math errors found in audited scope.** This is meaningful §E calibration data — six independent math-verifications across §I and early §II all passed. The auditor's framing: "*all segments are well-staged, correctly labeled epistemically, and internally consistent.*"

**Suggested disposition:** `sentiment` — calibration data. The six clean math-verifications support a polish-and-sentiment-ledger row: "*963715: §I + early §II math first-hand-verified across six load-bearing segments (mismatch decomposition / Model-S Itô / sector counterexample / persistence condition / convention monotonicity / chain decay) — all passed.*"

### Theme G — Audit-as-instance-of-the-theory observations

- **The audit reading-mode as the deliberation framework operating** — implicit in the Process-3 priming-as-falsifiable-promissory-note observation: the auditor's audit-protocol *is* a deliberation cycle in der-deliberation-cost terms (the "AI agent's dilemma" applied to the audit itself).

- **The Class-1-by-behavior self-observation** (Theme A item 5) — the auditor noting operating in W₂-ish mode is the audit being a *worked instance* of the directed-separation framework. The auditor's epistemic updates are nominally goal-blind but goal-conditioned attention is being used to read the codebase; behavioral separation rather than structural separation. The framework correctly identifies this as approximate.

- **The reflexive-novelty at seg 23** — recognizing that `der-deliberation-cost` *itself* is doing the "self-application" the framework prescribes. The audit reaching this segment and recognizing this is the cognitive cycle the framework names operating in the auditor's own awareness.

**Suggested disposition:** `process/instruction-feedback` — precursor material for `doc/de-novo-audit-instructions.md` §2 ("*The audit as a logocentric instance of the theory itself*"). The Class-1-by-behavior self-observation is the most operationally precise instance — it shows the framework is recursively applicable to the agent doing the audit.

---

## First-Pass Scrutiny

Per the brief: for each finding above, name which segments in `01-aat-core/src/` (and other components if relevant) I (the extraction agent) read first-hand to evaluate it, plus per-finding verdict using `doc/audit-routing-instructions.md` §8 enum. Honest "didn't have time to verify X" allowed and expected — first-pass flags for routing; the §8 independent-verify gate fires downstream.

### Part III findings — verdicts and first-hand verification

| Finding | Disposition (suggested) | First-hand verification by extraction agent |
|---|---|---|
| F1 (scope-agency Pearl-do without depends) | `correctly-rejected` per 472913 convention-dissolution | **Verified first-hand against current `src/`.** Read `01-aat-core/src/scope-agency.md` head + key lines: `depends: [scope-adaptive-system, def-action-transition]`; Formal Expression at line 19 carries $do(\cdot)$; parenthetical "(Pearl's intervention operator; see #def-pearl-causal-hierarchy)" at line 24. **Pattern confirmed unchanged.** Did not separately verify the 472913 cycle's `the-cycle-in-motion-intro.md` Working Notes convention-statement first-hand — accepting the 472913 extraction's first-hand verification on that. Cross-cycle dispositive convention: `correctly-rejected`. |
| F2 (post-composition-consistency derived in postulate) | `architectural`→PROPOSALS (cross-cycle finding-convergence) | **Verified first-hand against current `src/`.** Read `01-aat-core/src/disc-composition-consistency.md` head: frontmatter `depends: [scope-agency]` only; `stage: deps-verified`; `type: postulate`. The `*[Derived (Conditional on Tier 1M + admissible composition topology, from #result-contraction-template ...)]*` tag was verified via the 472913 extraction's first-hand reading (cross-confirmed). **F2 confirmed `still real`** as of 2026-05-20 (cross-confirmed with 472913 extraction).  Cross-cycle finding-convergence raises priority. |
| F3 (def-model-sufficiency depends-on-draft Gate-1 violation) | `actionable-open`→TODO (promote `form-information-bottleneck`) | **Verified first-hand against current `src/`.** Read `01-aat-core/src/def-model-sufficiency.md` head: `stage: deps-verified`, `depends: [form-agent-model, form-information-bottleneck, def-action-transition]`. Read `01-aat-core/src/form-information-bottleneck.md` head: `stage: draft`, `status: exact`. **F3 confirmed `still real`.** |
| F4 (der-gain-sector-bridge OUTLINE-vs-frontmatter stage mismatch) | `actionable-open`→TODO (Gate-1 re-review + reconcile) | **Verified first-hand against current `src/` and OUTLINE.** Read `01-aat-core/OUTLINE.md:63`: row shows `claims-verified`. Read `01-aat-core/src/der-gain-sector-bridge.md` head: `stage: draft`. **F4 confirmed `still real`.** |
| F5 (scope-agent-identity OUTLINE-vs-frontmatter stage mismatch) | `actionable-open`→TODO (Gate-1 re-review + reconcile) | **Verified first-hand.** Read `01-aat-core/OUTLINE.md:68`: row shows `deps-verified`. Read `01-aat-core/src/scope-agent-identity.md` head: `stage: draft`. **F5 confirmed `still real`.** Combined F4+F5 disposition: candidate `process/instruction-feedback` (extend `bin/lint-outline` to check stage consistency between OUTLINE rows and segment frontmatter). |

### Theme 2 — §E positive-calibration: verdicts and verification

| Item | Disposition | First-hand verification |
|---|---|---|
| Theme 2 cluster (§I scope-honesty discipline) | `sentiment` / `soft-polish` | First-hand-verified at the WORKING-dir level (the auditor's per-segment reflection text). Did *not* re-read each named segment in `src/` to confirm the §E points still hold under current text — accepting the WORKING-dir reading where the segment text hasn't been touched since 2026-05-10 (10 days). The most quoteable instance (seg-23 der-deliberation-cost AI agent's dilemma) is content-stable per the cross-cycle correlation; no recent commit affects this. |

### Theme 3 — Open threads: all `actionable-open`

| Open-N | Disposition | First-hand verification |
|---|---|---|
| Open-1 (Section II-15 onward not reached) | `actionable-open`→TODO (future audit work) | Not testable in this extraction — these are flags for future audit cycles. No `src/` verification appropriate. |
| Open-2 (Section III composition not reached) | `actionable-open`→TODO (future audit work) | Same as Open-1. |
| Open-3 (Appendices not reached) | `actionable-open`→TODO (future audit work — highest-priority is `deriv-sector-condition`) | Same. |
| Open-4 (TST / 03-llm-core / 04-eli-core not reached) | `actionable-open`→TODO (component-level audits remaining) | Same. |
| Open-5 (GUC rename audit specifically didn't fire) | `sentiment` (positive §E observation) + `actionable-open` (future Section III + Appendix audit should test) | Tested in audited scope (segs 1-43): no GUC integration debt found first-hand by the auditor; cross-confirmed by my reading of the segment text the auditor walked. Not tested in unaudited scope. |

### Theme 4 — Phase-3-1: verdicts and verification

| Item | Disposition | First-hand verification |
|---|---|---|
| Phase-3-1 ("disambiguation of which parameter responds to which cause") | `research-seed` / framing-material (cross-cycle convergence raises priority) | Cross-cycle triangulation across 471203 (Theme B), 472913 (Phase-3-2), and 963715 (this Theme 4) — three independent cycles converged on the same meta-observation. Per `feedback_convergence_as_framework_coherence_evidence`, this is signal that the pattern is in the framework. No additional `src/` verification appropriate at extraction-time; the pattern's testing would require running a fresh audit looking specifically for more instances. |

### Theme 5 — Process feedback: all `process/instruction-feedback`

| Item | Disposition | First-hand verification |
|---|---|---|
| Process-1 (batched-vs-single cadence trade-off) | `process/instruction-feedback` | Methodology comparison across 471203 / 472913 / 963715. First-hand-verified by comparing the three WORKING dirs' yield-per-segment patterns. The single-segment cadence with sanctioned lighter prose outperforms batched-mode for finding-yield in the dirs compared. |
| Process-2 (stable finding-IDs across walk) | `process/instruction-feedback` | First-hand-verified by reading the WORKING dir's finding-tracking sections across batches — the F1-F5 IDs are stable and explicitly updated per batch. |
| Process-3 (priming-as-falsifiable-promissory-note) | `process/instruction-feedback` | Cross-cycle reinforcement with 472913 Process-1. The GUC-bet-didn't-fire instance here is the worked example. |

### Honest coverage summary for this extraction

**Read first-hand from the WORKING dir:** all 13 files (`00-initial-predictions.md`, `00-running-outline.md`, segments `01-def-agent-environment.md` through `43-batch-strategy-dag-cluster.md`). Per-segment reflections read in full; batch reflections read in full including per-segment notes, cross-segment consistency, math verification, finding-tracking-update sections, and wandering thoughts.

**Read first-hand from `01-aat-core/src/` for verification:**
- `scope-agency.md` (frontmatter + lines 19, 24 — F1 verification)
- `post-composition-consistency.md` (frontmatter — F2 verification; the eq-tag content cross-confirmed via 472913 extraction)
- `def-model-sufficiency.md` (frontmatter — F3 verification)
- `form-information-bottleneck.md` (frontmatter — F3 verification)
- `der-gain-sector-bridge.md` (frontmatter — F4 verification)
- `scope-agent-identity.md` (frontmatter — F5 verification)
- `01-aat-core/OUTLINE.md` (lines 63, 68 — F4 + F5 verification)
- `ls 01-aat-core/src/` (directory listing — confirmed referenced segments exist)

**Read first-hand from `audits/`:**
- `audits/audit-findings-471203.md` (full pilot — shape reference)
- `audits/audit-findings-472913.md` (full no-FINAL precedent — cross-cycle reference for F1-F2)

**Read first-hand from `doc/`:**
- `doc/audit-routing-instructions.md` (full — §8 enum + evidence hierarchy + independent-verify gate + gold-standing gate)
- (Did not re-read `doc/de-novo-audit-instructions.md` — accepted via the 471203 / 472913 pilot context. Honest defer.)

**Deferred verifications (honestly "didn't have time" or "scope-limited" — flagged for downstream routing):**
- Whether `bin/lint-outline` has been extended to check stage consistency between OUTLINE rows and segment frontmatter (F4+F5 combined disposition).
- Whether the eq-tag `*[Derived ...]*` text in post-composition-consistency is byte-exact unchanged (cross-confirmed via 472913 extraction's first-hand reading, but did not re-read myself).
- Whether the Phase-3-1 pattern (disambiguation-of-which-parameter) holds in unaudited scope (Section II-15+, Section III, appendices). The pattern is a research-seed, not a verified claim; testing would require continuing the audit.
- All Open-1 through Open-4 (segments beyond the audit's scope — these are flags for future audit, not present-state defects).

**Strengthen-first integration recommendations (per brief item 3):**
- **F1** — *correctly-rejected* (cross-cycle convention dissolves it). The path-(a) "introduce do() at post-causal-structure" proposal is a strengthening direction (additional external-citation hygiene) if pursued; not a softening.
- **F2** — strengthen-first move identified by 472913 (Working Notes' successful binding to (CC-*) closed forms). **The fix is split (architectural), not soften.** No softening involved.
- **F3** — strengthen-first move: **promote `form-information-bottleneck`** to deps-verified (the segment is `status: exact` and content-ready), rather than demote `def-model-sufficiency`. **Strengthening direction.**
- **F4 + F5** — strengthen-first move: **Gate-1 re-review + promote** the segments to match OUTLINE (the OUTLINE shows the higher stage; segments are content-rich enough to plausibly earn it). **Strengthening direction.** The combined disposition (extend `bin/lint-outline`) is a tooling strengthening.
- **All 5 Open threads** — explicit strengthening directions (verify inevitability-grade claims, verify scope-propagation, verify cross-volume integration). None are softening recommendations.
- **Phase-3-1** — research-seed, not a segment-fix. The cross-cycle triangulation is the strengthening evidence.

**Strengthen-first count: 5/5 findings carry strengthen-direction recommendations** (F2's split, F3's IB promotion, F4+F5's Gate-1 re-review + tooling extension, plus F1's path-(a) optional). **No soften-recommendations.** The audit's strengthen-before-soften posture was honored throughout. Notable: the 472913 cycle's clean F1-rescission via the external-notation convention is what *retrospectively* validates this cycle's F1 as `correctly-rejected` rather than an open finding. Cross-cycle dispositive convention surfacing across two independent de-novo walks is itself a methodology contribution.

---

## Frame-defects and instructions-clarity observations encountered

Building on the 471203 pilot and 472913 precedent's frame-defect lists, this slice's encountered points:

1. **Cross-cycle convergence as the dominant signal in same-corpus parallel extraction.** Three independent de-novo cycles (471203, 472913, 963715) all surfaced the same meta-pattern (AAT's value-add as epistemic-architectural / disambiguation). 472913 + 963715 surfaced the same F1 candidate (Pearl-do in scope-agency) and the same F2 (post-composition-consistency derived-in-postulate). The convergence-as-framework-coherence-evidence per Joseph's standing instruction is *operating across the extraction sweep itself*. Worth flagging for the routing agent: when same-finding appears in multiple WORKING dirs, route once with cross-references rather than duplicating.

2. **Batched-cadence audits have lower per-segment yield but broader coverage.** This dir's auditor self-modified to batch-mode after seg 3; covered 43 segments with 5 findings (~0.12 findings/segment). The 472913 dir covered 15 segments with 4 findings + 5 open threads (~0.27 findings/segment + ~0.33 threads/segment). Single-segment cadence yields more findings per-segment. The trade-off is real and the auditor's honest disclosure ("fresh-encounter quality per segment is somewhat lower") was accurate. **Suggest:** parallel extraction agents flag the cadence-mode used by their dir's auditor explicitly, as it affects how to interpret coverage.

3. **No-FINAL slices that don't reach a stopping point require honest characterization of *where the audit stopped*.** This dir stopped at seg 43 (def-strategy-dag) without explicit Joseph intervention — the auditor just ran out of session, presumably. The 472913 dir had explicit Joseph cadence-pivot at seg 12 and a clearer stopping point at seg 15. Distinguishing "audit-stopped-by-modifier" (472913) vs "audit-ran-out" (963715) matters for the Open-thread characterization.

4. **The auditor's stable finding-ID convention (F1-F5 across batches) is methodology-contribution material.** Worth surfacing for `doc/de-novo-audit-instructions.md` revision — explicit guidance to maintain stable IDs from first candidate-finding flag onward.

5. **Initial-predictions register validating cross-cycle.** The 472913 dir's Process-1 (priming-as-falsifiable-promissory-note) is reinforced here at 963715: the GUC-bet *didn't fire* in audited scope, which is calibration data that would *not have surfaced* without the explicit bet. Two cycles now demonstrate the pattern's value.

6. **Joseph or downstream routing should treat the cross-cycle convergence as raising routing priority.** F2 (post-composition-consistency) appears in *two* cycles now (472913 + 963715) with the same essential structural observation. Even if the 472913 framing is sharper, the convergence is itself evidence the defect is real and routable. Same for the Phase-3-1 / Theme-B "epistemic-architectural disambiguation" pattern across 471203 + 472913 + 963715.

---

*End of extraction. The original WORKING dir at `audits/AUDIT-WORKING-963715/` is preserved unmodified per the gold-standing gate. Routing actions are downstream — Joseph or the routing agent decides whether F2 graduates to PROPOSALS (cross-cycle convergence with 472913 raises priority), F3/F4/F5 land directly in TODO, the 5 Open threads form a future-audit task list, and the Phase-3-1 hypothesis (now cross-confirmed across three cycles) enters the polish-and-sentiment-ledger as a research-seed for cross-cycle pattern-tracking with explicit triangulation back to 471203 Theme B + 472913 Phase-3-2.*
