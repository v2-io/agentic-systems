# Consolidated polish-and-sentiment ledger — PRE-DECISIONAL DRAFT

> **Status: working draft, not yet applied.** This is the *design* of the
> single consolidated soft-findings pass across clusters A–E (per the
> anti-fragmentation rule: one curated cross-cluster pass, themed and
> deduplicated — never per-cluster as each graduates, which re-buries the
> signal). It locks nothing in: `audits/polish-and-sentiment-ledger.md` is
> untouched until the post-gate durable batch. Rows continue from the live
> ledger's max **S7**. Numbering is thematic, not cluster-order — the
> thematic grouping *is* the anti-fragmentation structure.
>
> Breadcrumb only. If this session ends, the next instance inherits the
> synthesis here; the authoritative policy is `doc/audit-routing-instructions.md`.

---

## A. Dedup map (the cross-cluster collisions — done once, here, on purpose)

The recurring signals that *must not* become one row per file:

- **"Epistemic honesty / conservatism is extraordinary — best in this
  space."** Recurs in essentially every reviewer across the whole corpus:
  Cluster E's 2026-03/04 broad-review cohort (~10 independent Opus/Codex/
  Gemini reads), Cluster D's 849201 confirmation-class variants, 738192's
  process praise, scattered Codex passes. → **one** attributed row (**S16**),
  not per-file.
- **"Section I is the strongest; the lift into agency/composition is where
  rigor thins"** + the specific positive (satisfaction-gap/control-regret
  split, acyclicity-from-temporal-ordering = "the most genuinely useful
  original formalization / real theory not vocabulary"). Cluster A traced it
  across Codex 04-01/02×3/03×2/06×3 + Opus echo. → **one** row (**S9**).
- **"The framework's honesty is load-bearing / the epistemic architecture
  is the most novel contribution (more than the integration narrative)."**
  Cluster A (Opus 6d858f28 closing + 3546217a BP-6) **and** Cluster B
  (audits-2026-04-22-evening Opus closing-observation) — same session-family
  observation, *and it landed* (it is now the CLAUDE.md honesty-as-
  architecture posture + the OUTLINE "Reading AAT" preamble). → **one** row
  (**S10**), status `superseded-by` the landed posture, attributed to both.
- **Cox-necessity for graph-structure-uniqueness reachable.** Cluster A
  (extracted-claude-04-22-6d858f28 §BP-E) **and** Cluster B (opus-2026-04-21
  synthesis "Cox-parallel necessity direction"). → **one** row (**S14**),
  attributed to both, strengthen-direction graduate-watch.
- **Audit-process / instruction-set feedback.** Recurs across 471203 §G
  (pilot-routed), 584721 §A.1–A.4, 742613 process-feedback, 613842 process-
  feedback. → **one** consolidated themed block (**P-block**, below), not
  4+ rows. The 742613 Phase-2-triage-vocabulary sub-item is specifically
  `superseded-by` this program's routing-tracker enum (it is that enum's
  ancestor) — recorded so it does not read as still-open.
- **Convergence-as-coherence-evidence.** The opacity-gain ≥3-cycle
  convergence (849201-F1 / extracted-gemini-2026-04-26-27 / AUDIT-WORKING-742613
  flag) is a **MANIFEST headline**, *not* a ledger row (per Cluster D). The
  829314-LOGOZOETIC §6 + 849201 confirmation-class "independent reader
  re-derived the developmental-trajectory / goal-blind-routing / strengthen-
  first spine" → **one** sentiment/convergence row (**S17**).

Not mirrored, by design (recorded so they are not silently re-dropped):

- O-BP\* / C-BP1 architectural intuitions → already routed to
  `architectural-proposals-2026-04-22.md` / the three landed meta-segments.
  Mirroring would double-track. (S13 captures only the *un-adopted residue*.)
- The 12-obligation bridge-spike roadmap → already housed in
  `spike-transient-dependency-amplification.md` + `spikes/INDEX.md` + the
  TODO spike-audit triage. A ledger row would re-bury, not preserve.
- Codex/Joseph rule-formation exchanges (04-03 Codex-open-questions rule;
  04-06 no-shortcuts/false-constraints rule) → `process/instruction-feedback`
  that *already landed in CLAUDE.md*. Their value is **provenance**, carried
  in the MANIFEST entry ("primary source for CLAUDE.md Working Convention
  X"), not a ledger row.
- 738192-F2 line-53 recap-precision nudge → **resolved by SN-3** (commits
  `3072667`/`2666eca`; `def-pearl-causal-hierarchy:53` is now scoped, parent-
  verified). *Not* an open soft-polish row — closed; note in MANIFEST.
- 849201-FINAL Finding 2 (CIY≠EIG verified-still-honest) → redundant with
  **S7** (CIY name-vs-substance); skip per Cluster D's own guidance.
- F-V3/F8 (composite-agent C-iii) → correctly-open, triple-tracked
  (TODO:95 + PROPOSALS SP-21 §G + ledger). Stays there; **not** a ledger row.
- Cluster C lint-state (3 ordering + 1 missing-dep) + the
  `hyp-mismatch-dynamics:54` item → **standing-hygiene TODO**, not ledger.
  *Correction to the inherited frame:* the `:54` item is **mischaracterized**
  as an "F-V1 micro-residual." Primary source: line 54 already reads
  `O(η* c_max)` — linear in η\*, i.e. already correct in η\*-order (the F-V1
  fix *was* the η\*-power, (η\*)²→η\*). It differs from canonical
  `deriv-discrete-sector-condition`'s `O(η* c_max²/c_min²)` only in the
  *prefactor*, at explicit `*Heuristic.*` tier, with a live pointer to the
  sharper segment. **Plausibly a no-op**; at most an optional precision-nudge.
  Do not churn a correct segment. (Surfaced as a Cluster-C-frame correction;
  not a ledger item.)

---

## B. Proposed rows (continuing from S7)

### considered-declined (the reason is the payload — must not be silently re-dropped)

| # | Finding (attributed) | Source | Status |
|---|---|---|---|
| **S8** | **POMDP-collapse family.** Four declined Gemini big-picture moves: (1) abandon continuous-time ODE/SDE, treat software as discrete MDP/POMDP; (2) "action as observation" belief-MDP collapse, replacing CIY with Bellman VOI; (3) technical-debt = mutual information between code lexical structure and domain model; (4) sub-agent composition = MARL with communication costs. **Declined, reason = payload:** the continuous-time bridge is load-bearing for the Lyapunov/sector-condition machinery (it is *what* the persistence theorems are stated over); the action-vs-observation distinction is precisely what makes `#der-loop-interventional-access` non-trivial (collapsing it erases the Level-2 contrast); CIY is retained because the regret-bounded objective needs interventional-distinguishability, not VOI. Recurs as an attractive simplification — recorded so an unaware future agent does not re-litigate from scratch. | extracted-audits-2026-04-25 (Gemini big-picture) [Cluster A] | noted (declined-with-reason; revisit only if the continuous-time bridge is independently shown non-load-bearing) |
| **S15** | **Per-segment "derived / chosen / assumed" table + single minimal-viability worked example.** Opus (6d858f28 §G) named two disproportionately-valuable presentational moves. Partially superseded: per-segment `## Findings` + the FORMAT discipline move toward the first; worked examples exist but scoped. Residual = the *uniform* per-segment table, **deliberately not universal** (uniform-table cost vs. epistemic-legibility trade-off recorded so it is not silently re-litigated). | extracted-claude-04-22-6d858f28 §BP-G [Cluster A] | noted (considered; partially superseded by the `## Findings` schema + FORMAT.md) |
| **S18** | **Sidecar `meta/` parallel-directory pattern** (829314-core-F6 Appendix A Rec 3). Declined, reason = payload: the project adopted in-file database-entry segments + build-time stripping (the markdown-first monograph pipeline + FORMAT schema + `bin/extract-findings`) instead; parallel `meta/` dirs were rejected to avoid slug-split drift. Recorded so a future auditor seeing raw-segment "bloat" does not re-propose the sidecar. | audit-829314-FINAL-core §F6 / Appendix A [Cluster D] | noted (declined-with-reason; the bloat concern itself is `subsumed-by-later-work` — the markdown-first pipeline) |
| **S19** | **Co-owner engagement pattern as a recordable signal** ("not 'thanks, I'll think about it' but 'let's launch the work'"). Real calibration signal, but **already canonical** in global memory (`feedback_collaboration_rhythm`). Recorded as declined-for-ledger (not re-litigated) rather than duplicated. | extracted-claude-feedback-2026-04-22-25-portfolio-reviews [Cluster C] | noted (declined-with-reason; already canonical in global memory) |

### sentiment / calibration (one row per recurring signal — never per file)

| # | Finding (attributed) | Source | Status |
|---|---|---|---|
| **S9** | **Stable cross-pass external read: "Section I is the strongest; the lift into agency/composition is where rigor thins"** — plus the specific positive: the satisfaction-gap / control-regret split and acyclicity-from-temporal-ordering are repeatedly named "the most genuinely useful original formalization" / "real theory, not just vocabulary." Independently and repeatedly stated. Calibration: the asymmetry is real and externally legible; the named-strongest results are the ones to lead with publicly. | extracted-codex 2026-04-01/02/03/06; extracted-audits-2026-04-21 [Cluster A]; echoed in E cohort | noted (converges with the publication-kernel strategy already in ops) |
| **S10** | **"The framework's honesty is load-bearing; the epistemic architecture is the most-novel contribution, more than the integration narrative."** Independent Opus arrival, two session-families. **It landed** — now the CLAUDE.md honesty-as-architecture posture + the OUTLINE "Reading AAT" preamble. | extracted-claude-04-22-6d858f28/3546217a [Cluster A]; audits-2026-04-22-evening Opus closing [Cluster B] | superseded-by the CLAUDE.md honesty-as-architecture posture + OUTLINE preamble |
| **S16** | **Recurring qualitative calibration: the epistemic honesty / conservatism is extraordinary — repeatedly named the best the reviewer has encountered in this space.** Recurs across ~10 independent Opus/Codex/Gemini reads in the 2026-03/04 broad-review cohort, the 849201 confirmation-class variants, and 738192's de-novo-instruction praise. One attributed cohort row (per the ledger's own anti-reburial rule); the richest/most-attributed instances are the 04-02 deep-reviews + 4-06. | E 2026-03/04 cohort; D 849201; 738192 [Clusters E/D/B] | noted (sentiment; the honesty axis is the externally-legible distinctive — converges with S10) |
| **S17** | **Convergence-as-coherence-evidence: an architecturally-independent cold reader independently re-derived load-bearing structure.** 829314-LOGOZOETIC §6 ("sycophancy is infant attachment", "PROPRIUM solves goal-coupling" → maps onto landed `obs-developmental-trajectory` / η\* infant-attachment / `def-imperium-arbitrium-split`); 849201 confirmation-class re-derived the strengthen-first spine (forgetting prerequisite, causal-insufficiency no-go, incremental-sector-bound necessity, ambiguity-bounded bias law) reading cold. Per `feedback_convergence_as_framework_coherence_evidence`, independent convergence on the same structure is stronger evidence than single-agent elaboration. | 829314-LOGOZOETIC §6; 849201-FINAL/-LOGOGENIC/-SEC-III/-TST [Cluster D] | noted (convergence-evidence; one cohort row, not per-variant) |
| **S20** | **Within-segment epistemic discipline holds under a sustained first-hand pass** (J1–J10): a sustained de-novo read confirms consistent labeling / no discussion-outruns-formal-status drift in the sample. First-class calibration (the project does not discard "no defects = nothing to record"). | audit-2026-04-24-fresh-pass §J1–J10 [Cluster C] | noted (sentiment/calibration) |
| **S21** | **De-novo-audit-instruction design is landing** ("predictions-before-reading forced verification mode"; "OUTLINE-first effective"; "instructions are excellent"). Calibration that the de-novo instruction set works with fresh independent agents. | audit-738192-FINAL process feedback [Cluster B] | noted (sentiment) |

### research-seed (graduate-watch flagged where a concrete derivable target exists)

| # | Finding (attributed) | Source | Status |
|---|---|---|---|
| **S11** | **Tier-3 prevalence in practical composites.** Composition-closure bridge lemma is proved (Tier 1) for an estimation-flavored class; the weakest-link bound makes any composite with one rule-based/non-convex component Tier-3. Sharp true observation: "the central transferability result is unavailable in exactly the regime where composition is most empirically interesting." Concrete target: characterize/bound the practical-composite fraction that is Tier-3, **or** reframe composition-closure explicitly as "exact for a narrow estimation-flavored class; structural template otherwise." | extracted-claude-04-22-3546217a §Finding D [Cluster A] | open (research-seed; **graduate-watch** — strong PROPOSALS candidate) |
| **S12** | **4c sibling-covariance test sensitivity bound.** The orient-cascade step-4c causal-sufficiency check is the unique broadly-available L0→L1 escalation diagnostic, but its practical sensitivity is flagged open and degrades exactly in the adversarial / fast-drifting regimes where causal-insufficiency detection matters most. Concrete target: derive an SNR / effective-sample-size bound for the covariance test at convergence and surface it in the cascade, not only the sister segment. | extracted-claude-04-22-3546217a §Finding E (+ bf945f78/6d858f28 F5 / pending-2026-04-22 F11 residual) [Cluster A] | open (research-seed) |
| **S13** | **Un-adopted residue of the 04-22 Opus bigger-picture.** After O-BP\*/C-BP1 + the three meta-segments landed, three structural intuitions remain un-closed: (a) DAG-Boolean → continuous strategy layer (graded parent influences for soft facilitators); (b) the orient cascade is itself an adaptive cycle (recursive AAT-applies-at-every-level); (c) agent-identity promoted from discussion-grade scope to an architectural postulate. Speculative; none forced by a current finding. | extracted-audits-04-22-morning / -bf945f78 / -3546217a Opus big-picture [Cluster A] | open (research-seed) |
| **S14** | **Cox-necessity for graph-structure-uniqueness is plausibly reachable** via Lauritzen's characterization of Markov properties on graph classes — would elevate `#deriv-graph-structure-uniqueness` from sufficiency-only to a full Cox-style necessary-and-sufficient theorem. A *strengthen-direction* seed. | extracted-claude-04-22-6d858f28 §BP-E [Cluster A]; opus-2026-04-21 synthesis "Cox-parallel necessity" [Cluster B] | open (research-seed; strengthen-direction, **graduate-watch**) |
| **S22** | **584721 §D framework-scope observations.** D.1 six-mechanism shallow-plan convergence (natural `#disc-separability-pattern` extension); D.2 OKR/AAT operational-mapping as a domain template (approachability/Feynman); D.3 **correction-capacity-collapse unification** (gain-collapse / catastrophic-forgetting / detection-latency / stability-myopia as one pathology) — *strongest*; **overlaps M4 modularity-state-dynamics + `#disc-correction-capacity-collapse`** → check against the M4 cycle before any PROPOSALS filing (possible subsume); D.6 type/token distinction foregrounded in `03-llm-core`; D.8 seven-attack discipline as a FORMAT convention for inevitability-core segments. | audit-584721-FINAL §D [Cluster B] | open (research-seed; D.3 graduate-watch *pending M4 subsume-check*) |
| **S23** | **TST axiom-vs-derived-status class** (829314-TST-F2): apply the `post-composition-consistency` derivation-hierarchy resolution pattern to TST `scope-*` files that house derived consequences under `axiomatic` status. Class-level decision governs (SP-6 / 471203 §B F5 / F-A cluster); graduates into SP-6's scope if/when that class-fix executes. | audit-829314-FINAL-TST §F2 [Cluster D] | open (research-seed; cross-ref SP-6 — not an open defect, the class decision governs) |
| **S24** | **k-of-n vs DL(Σ) parsimony — attempt the representability / no-go.** Under DL(Σ) penalty + AND/OR completeness, are k-of-n strategies representable within budget B? Scope already logged honestly in `scope-and-or` Working Notes 58–59 + `#deriv-graph-structure-uniqueness` open agenda. The *strengthen-first* move is to attempt the no-go, not to soften. | audit-829314-FINAL-TST §F5 [Cluster D] | open (research-seed; graduates to PROPOSALS if the no-go is attempted) |
| **S25** | **451729 open-theory soft set.** §F.3 `form-consolidation-dynamics` stability-plasticity *upper* bound is open (only half the feasibility window derived) — genuine open-theory, self-labeled in-segment, recurs as a known half-open window. §F.2 Correlation-Hierarchy (L0/L1/L1′/L2) underused as a pedagogical tool; a standalone exposition would raise accessibility. §D.2 `result-unity-closure-mapping` joint (U_O,U_Σ)→ε_a f₁/g "mechanical extensions not fully computed" (lowest weight; may stay an in-segment scope note). §F.1 README/OUTLINE preambles could give the practically-actionable diagnostics equal billing with the integration framing (rhymes with **S2** + the respectful-pedagogy CLAUDE.md direction). | audit-451729-FINAL-2026-05-10 §F.1–F.3 / §D.2 [Cluster E] | open (research-seed; F.3 is the durable open-theory one — must not be silently re-dropped) |

### soft-polish (small, high-confidence; some are candidate co-owner direct-fixes)

| # | Finding (attributed) | Source | Status |
|---|---|---|---|
| **S26** | **OUTLINE topological-order pass** — merged: `der-agent-opacity` before `der-interaction-channel-classification` (829314-core-F3); `scope-ciy-observational-proxy` proxying `#def-causal-information-yield` before linear order (core-F4); `der-code-quality-as-observation-infrastructure` placed after files referencing it (TST-F4). All OUTLINE-linearization, not dependency-graph, defects; `bin/lint-outline` is the mechanism. One row, not three. | audit-829314-FINAL core-F3/F4 + TST-F4 [Cluster D] | open (polish; one consolidated OUTLINE-order nudge) |
| **S27** | `def-action-transition` forward-references "epistemic opacity" / `#def-observation-function` before declared. Honest forward-pointer prose by design (FORMAT sanctions forward `#slug` refs); `depends:` correctly minimal. At most a one-clause forward-ref courtesy gloss. | audit-829314-FINAL-core §F2 [Cluster D] | open (polish; low priority — segment is structurally sound as-is) |
| **S28** | `schema-strategy-persistence` uses $\alpha_\Sigma \approx 1-\lambda$ without noting the exact $(1-\lambda)/(2-\lambda)$ form (≈33% error at λ≈0.5); "worth a sentence in Epistemic Status." High-confidence isolated — parent may prefer a direct micro-fix over a ledger row. | audit-451729-FINAL §D.3 [Cluster E] | open (polish; candidate co-owner direct-fix) |
| **S29** | 584721 §D.4 (forced/matched/adopted coordinate tabulation in `#disc-additive-coordinate-forcing`) + §D.7 (diagnostic-CIY four-axis propagation to `#disc-exploit-explore-deliberate`). Small editorial scope-honesty / propagation passes; candidate co-owner direct-fixes. | audit-584721-FINAL §D.4/D.7 [Cluster B] | open (polish; candidate co-owner direct-fixes) |

### P-block — audit-process / instruction-set feedback (one consolidated themed entry, NOT per-file)

> Not framework findings; themed separately so they do not pollute framework
> tracking. Attributed sources: **471203 §G** (pilot-routed), **584721
> §A.1–A.4** (§4.4 cadence-failure 3/3-first-runs lesson; CLAUDE.md/MEMORY.md
> auto-load priming; OUTLINE-linearization refinement; prompt-12/13
> expansion), **742613** (partial-pass protocol; appendix-exception
> tightening; explicit CLAUDE.md↔TODO conflict override; machine-check
> helper; "consider writing" too soft; **Phase-2 triage vocabulary**),
> **613842** (SCC/cycle-handling clause; CLAUDE.md-bleed; appendix
> example-findings-as-historical-calibration; component-local-lint caveat),
> **829314 §8 ×variants** (formalize the v2 "Effort estimate" with a
> complexity metric).
>
> Two specific dispositions inside the block:
> - The **742613 Phase-2 triage vocabulary** (new / known-unintegrated /
>   known-resolved / tooling-gap / scope-status-mismatch) is the **direct
>   ancestor of this program's routing-tracker disposition enum** →
>   `superseded-by` the enum (record as absorbed, **not open**).
> - The **829314 §8 v2 "Effort estimate"** recommendation is `superseded-by`
>   the routing-tracker enum's per-finding classification (note-and-close).
>
> Status: themed, consolidated, attributed; the durable instruction-
> improvement signal (the §4.4-cadence and CLAUDE.md-bleed lessons) is the
> high-value part the project historically discarded — preserved here, not
> dumped in TODO.

---

## C. MANIFEST-routing notes (not ledger rows — flagged here so they are not lost)

- **A's stale 04-28 disposition:** `extracted-codex-feedback-2026-04-28`
  says "Pending"; primary-source-verified resolved (`bin/naming-aggregate.rb`
  defaults + `doc/naming-principles.md` ref). MANIFEST writes the
  **corrected (resolved)** disposition, *not* "Pending".
- **bf945f78 non-independence:** `extracted-claude-feedback-2026-04-22-bf945f78`
  *is* the Opus pass inside `extracted-audits-2026-04-22-morning` — same
  audit, not independent corroboration. MANIFEST records the relationship
  (the convergence-as-evidence discipline only holds for *independent*
  probes).
- **No SUPPLEMENT for 829314 / 849201** (contra a since-corrected spine
  generalization that held only for 471203). Their durable evidence is the
  FINAL's own inline Phase-2 + first-hand `src/` re-read. MANIFEST says so
  explicitly so a future verifier does not hunt a non-existent SUPPLEMENT.
- **193847 ≠ 829314:** the encounter tracker
  `msc/logogenic-encounter-2026-05-01/07-audit-integration-tracker.md`
  tracks audit-id 193847, not 829314 (coincidental digit overlap). Not a
  829314 integration record.
- **Opacity-gain ≥3-cycle convergence** (849201-F1 / extracted-gemini-2026-04-26-27
  / AUDIT-WORKING-742613 flag → one shared `deriv-adaptive-gain-dynamics`
  strengthening) is the Cluster-D **MANIFEST strengthen-first headline**,
  stated once, not re-litigated three times.
- **April-01/02 consolidation chain** (04-01 → 04-01-remaining →
  04-02-{synthesis,round2} → 04-02-comprehensive) is a nested-revision
  lineage → **one grouped MANIFEST entry** with a shared redundancy table,
  not 13 near-identical per-file justifications. `analysis-2026-04-02-synthesis`
  is a curated/raw pair with the deep-reviews extract (same content, *not*
  `diff`-duplicates) — note, do not double-count as independent signal.
- **Lineage doc embeds Cluster-C findings:** `extracted-claude-session-…-audit-instructions-lineage`
  is provenance (retain-as-history) but physically contains the
  2026-04-24-fresh-pass Tier-A/B/C audit whose findings are
  `pending-findings-2026-04-25`'s (Cluster C). De-dup at routing; do not
  track the same findings from two clusters.
- **451729 stays OPEN** on its single residual D.1 (already first-class in
  TODO §2026-05-10 — routed, not homeless). Its soft items are S25/S28
  above; once D.1 is dispositioned, 451729 retires as *fully accounted for*.
- Files #9/#10 (`extracted-codex-feedback-2026-04-03` / `-04-06`) are
  **primary sources for live CLAUDE.md Working Conventions** (Codex-open-
  questions-are-reader-clarity-gaps; no-shortcuts/false-constraints/
  strengthen-before-soften). MANIFEST notes the provenance value so the
  lineage survives graduation; `extracted-codex-feedback-2026-04-26-bridge-spike`
  graduates as `research-trail / provenance`, **not** ledger-routed.

---

*End pre-decisional draft. Inputs: the five cluster `adjudication.md`
deliverables (ADJUDICATION-WORKING-{704218 A, 628401 B, 704182 C, 714206 D,
472914 E}) + parent primary-source verification. Authoritative process:
`doc/audit-routing-instructions.md`. Durable write deferred to the post-gate
batch.*
