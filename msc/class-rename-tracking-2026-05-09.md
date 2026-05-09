# Class Rename Tracking — 2026-05-09

Live state file for the Class 1/2/3 → Separated/Coupled/Partial rename + Class 2 ↔ 3 swap. Branch: `guc-rename-2026-05-09`. Authoritative plan: [`msc/class-rename-execution-plan-2026-05-09.md`](class-rename-execution-plan-2026-05-09.md).

**Update this file as work lands.** Newer agents / batches reference the finished rows so coordination stays clean.

## State machine

| State | Meaning |
|---|---|
| `untouched` | Initial state — file not yet edited in this rename. |
| `modified` | Rename surgery applied (or warning callout placed, for callout-only files). The Notes column says what was done. |
| `verified` | A second agent or fresh-context read has checked the modification is correct. The state machine's terminus. |
| `regenerated` | Auto-generated file picked up changes from upstream sources (LEXICON via `bin/term render`; README* via `bin/build-readme`; FINDINGS via `bin/extract-findings`). Equivalent to `modified` for downstream-rebuild files. |

**Rules:** verification is by an agent *other than* the modifying agent (or by fresh-context read after a session boundary). Verification checks: (a) the rename + swap was applied correctly with no semantic-reversal corruption; (b) bare-property prose forms aren't ambiguous against adjacent-coupling concepts in that segment; (c) migration-note added to Working Notes if the segment's Class-N reference changed semantic meaning; (d) no broken cross-references.

## Counts as of 2026-05-09 fresh grep

Counts are rough Class-N occurrences (regex `Class[ -]?[123]\b|fully.merged|partially.modular`). Heaviest-touch is `der-directed-separation` (32). Use as triage-and-effort heuristic, not as a checksum.

---

## Phase 1 — terminology entries (create new + update existing)

| File | Count | Status | Notes |
|---|---:|---|---|
| `terminology/entries/goal-update-coupling-class.md` | — | verified | **Create.** Axis entry. Frontmatter + body + see_also to `directed-separation`, `class-coercion`. Per execution plan §5 Phase 1. [modified by sonnet 2026-05-09; verified by opus 2026-05-09: created axis entry with GUC three-value table, meta-pattern alignment note, κ_processing operationalization, Class-1-by-structure-vs-behavior note] |
| `terminology/entries/separated.md` | — | verified | **Create.** Per-value entry. (Optional per Joseph's call — axis-only entry may suffice; revisit if scaffolding feels heavy.) [modified by sonnet 2026-05-09; verified by opus 2026-05-09: created per-value entry defining Class 1: Separated with structural-vs-behavioral sub-distinction and class-coercion cross-ref] |
| `terminology/entries/coupled.md` | — | verified | **Create.** Per-value entry. [modified by sonnet 2026-05-09; verified by opus 2026-05-09: created per-value entry defining Class 3: Coupled; includes semantic-reversal note (pre-rename was Class 2)] |
| `terminology/entries/partial.md` | — | verified | **Create.** Per-value entry. [modified by sonnet 2026-05-09; verified by opus 2026-05-09: created per-value entry defining Class 2: Partial; includes semantic-reversal note (pre-rename was Class 3)] |
| `terminology/entries/directed-separation.md` | — | verified | **Update gloss.** Existing entry; refresh body + see_also for new vocabulary. [modified by sonnet 2026-05-09; verified by opus 2026-05-09: updated body to use Class 1 (Separated) / Class 3 (Coupled) / Class 2 (Partial) vocabulary; added goal-update-coupling-class, separated, partial, coupled to see_also] |
| `bin/term decide` events under `terminology/decisions/{goal-update-coupling-class,separated,coupled,partial}/` | — | verified | Record decisions per execution plan §5 Phase 1. Audit trail for the rename + swap. [modified by sonnet 2026-05-09; verified by opus 2026-05-09: five decisions recorded — canonicalize for goal-update-coupling-class; rename for separated/partial/coupled; update-gloss for directed-separation] |
| `LEXICON.md` | 2 | verified | **Regenerate** via `bin/term render --output LEXICON.md --force` after Phase 1 entries land. (Auto-regenerated; do not edit directly.) [modified by sonnet 2026-05-09; verified by opus 2026-05-09: rendered via `bin/term render`; LEXICON.md already carried auto-generated marker so clobber-guard passed; all four GUC entries appear in Agent Classes + Structural Concepts sections] |

---

## Phase 2 — 01-aad-core canonical segments (heaviest batch)

| File | Count | Status | Notes |
|---|---:|---|---|
| `01-aad-core/src/der-directed-separation.md` | **32** | verified | ⭐ **Canonical home.** Architectural-classification table reorders (Class 2 ↔ 3 swap) + property-name additions; κ-operationalization paragraph; Pearl-blanket discussion; "Class-1 by structure vs. by behavior" subsection; composite-level inheritance (logogenic = Class 2 → Class 3); Implications for theory scope; Findings table. **Place warning callout** at top of architectural-classification subsection. **Joseph's recommended target #2** (after LEXICON entries). [modified by sonnet 2026-05-09: table reordered (Class 2 ↔ 3 swap), all 32 Class-N refs renamed/swapped (Class 2 fully-merged→Class 3 Coupled, Class 3 partially-modular→Class 2 Partial, Class 1 Modular→Class 1 Separated); warning callout placed at top of Architectural classification subsection; migration note added to Working Notes; composite-inheritance subsection semantic-reversal verified; W₁/W₂ regime letters and class-A/B/C admissibility letters untouched] [verified by opus 2026-05-09: composite-inheritance subsection correct (Class 1 sub-agents → Class 2 Partial composite via strategic composition; Class 3 Coupled sub-agents → Class 3 Coupled composite; logogenic inheritance preserved); Pearl-blanket Class 3 scope exit correct; Findings heading "Explicit Class-3 Scope Exit" correct; warning callout placed per plan §6; migration note in Working Notes per plan §5 Phase 2; "modular topology"/"modular stages" left as broader-concept usage per §4a disambiguation; W₁/W₂ regime letters + Class A/B/C admissibility letters untouched as intended] |
| `01-aad-core/src/disc-adversarial-coupling-pressure.md` | 10 | verified | Landed today. Uses old vocabulary. Read carefully — segment is *about* coupling pressure on modularity, so Class-N references mix with the segment's central content. Migration note. [modified by sonnet 2026-05-09: 10 GUC Class-N refs renamed/swapped; "toward Class 2 (fully merged)" → "toward Class 3 (Coupled)"; "Class-2 coupled formulation" → "Class 3 (Coupled) formulation"; "Class-3 architecture (partially modular)" → "Class 2 (Partial) architecture"; "Class-2 bias bound" → "Class 3 (Coupled) bias bound"; "Class-1-sub-agents → Class-3-composite" → "Class 1 (Separated) sub-agents → Class 2 (Partial) composite"; broader coupling-pressure / adversarial-coupling vocabulary left unchanged per §4a; migration note added to Working Notes] [verified by opus 2026-05-09: all 10 semantic reversals correct; "coupling pressure" / "adversarial coupling" / "GUC-Coupled agent" register-mixed prose reads cleanly per §4a (bare "Coupled" never appears alone in this segment to avoid collision with the central "coupling pressure" concept); structured-repair tier mapping (Class 2 Partial = defensive composite) consistent with disc-separability-pattern row; Findings Brief uses "Separated agent (Class 1)" / "Coupled agents (Class 3)" pairing — clean] |
| `01-aad-core/src/der-class-coercion-via-wrapping.md` | 9 | verified | Landed today. Heavy interplay with W₀/W₂/W₁ regime hierarchy and class-A/B/C admissibility partition (regime/admissibility *independent of* GUC rename — disambiguate during read). Migration note. [modified by sonnet 2026-05-09: 9 GUC Class-N refs renamed/swapped; W₀/W₁/W₂ regime-regime letters UNTOUCHED; Class A/B/C admissibility letters UNTOUCHED; "Class-2 or Class-3 component" intro → "Class 2 (Partial) or Class 3 (Coupled) component"; W₀ row expanded to "Class 2 (Partial) or Class 3 (Coupled) component"; "Class 2 exit" → "Class 3 (Coupled) exit"; "Class-3 LLMs" (old vocab internally inconsistent — LLMs are fully merged; post-rename semantically correct) → "Class 3 (Coupled) LLMs"; migration note added to Working Notes] [verified by opus 2026-05-09: three-axis disambiguation (GUC / W-regime / Class A-B-C) preserved correctly; W₀ row expansion is conceptually correct (old "Raw Class-3 component" was ambiguous since W₀ should cover the full non-Class-1 union; expansion to "Class 2 (Partial) or Class 3 (Coupled)" makes the regime hierarchy coherent); "Class-3 LLMs" finding is real — pre-rename text was internally inconsistent with der-directed-separation's canonical Class 2 = LLMs assignment; rename incidentally fixed the bug; migration note documents all three axes + the bug-fix transparently] |
| `01-aad-core/src/deriv-observation-ambiguity-bias-bound.md` | 9 | verified | Currently styled "Class-2 ambiguity bias bound" → becomes "Class-3 (Coupled) ambiguity bias bound" given the swap. Verify any slug-related references, segment H1, and bibliography-style mentions. Migration note. [modified by sonnet 2026-05-09: 9 GUC Class-N refs renamed/swapped; claim now "Class 3 (Coupled) ambiguity bias bound"; "Class-2 (fully-coupled) agents" → "Class 3 (Coupled) agents"; "Class-1 (modular)" → "Class 1 (Separated)"; "Class 2 fully-coupled, κ≈1" → "Class 3 (Coupled), κ≈1"; "Class 3 partially-modular" → "Class 2 (Partial)"; all 9 occurrences handled; migration note added to Working Notes; external citations NOT updated — see report for list] [verified by opus 2026-05-09: H1 + Findings heading are class-agnostic (no rename needed); body claims correctly reframe to "Class 3 (Coupled) agents in logogenic-agents scope"; semantic reversal correctly applied throughout (was "Class-2 fully-coupled κ≈1" — now "Class 3 (Coupled) κ≈1" matches der-directed-separation's κ-operationalization); citation list captured by sonnet covers OUTLINE.md, disc-identifiability-floor, NOTATION, plus 6 logogenic + 1 ELI segments — these will pick up the new claim name during their respective phase rewrites] |
| `01-aad-core/src/disc-independence-audit.md` | 5 | verified | Migration note if Class 2/3 referenced. [modified by sonnet 2026-05-09: 5 GUC Class-N refs renamed/swapped under Assumption 1 (directed separation): "Class 1 (modular)" → Class 1 (Separated); "Class 2 (fully merged)" → Class 3 (Coupled); "Class 3 (partially modular)" → Class 2 (Partial); "Class 2 agents require coupled formulation" → Class 3 (Coupled); empirical-audit Working Note "Class 2" LLM failure → Class 3 Coupled. C1/C2/C3 value-convention hierarchy reference (Discussion line 120) correctly left unchanged — different taxonomy. Migration note added to Working Notes.] [verified by opus 2026-05-09: Assumption 1 block updated consistently across failure-regime / diagnostic-signal / repair-operation; C1/C2/C3 disambiguation correct (different taxonomy from GUC); Empirical-audit Working Note correctly distinguishes "directed separation ~holds (Separated)" for software agents vs. "fails structurally (Class 3 Coupled)" for LLMs] |
| `01-aad-core/src/der-interaction-channel-classification.md` | 4 | verified | Migration note if applicable. [modified by sonnet 2026-05-09: 4 GUC Class-N refs renamed/swapped: Epistemic Status "Class 1 (modular)" → Class 1 (Separated); "Class 2 (fully merged) recipients" → Class 3 (Coupled); "Class 3 (partially modular) recipients" → Class 2 (Partial); What-Is-Derived table "Class 3 approximation / Class 1 goal-blind-update" → Class 2 (Partial) / Class 1 (Separated). The four recipient-side regimes (I/II-a/II-b/III) are signal-processing vocabulary, not GUC classes — untouched. Migration note added to Working Notes.] [verified by opus 2026-05-09: 4 GUC swaps correct; recipient-side four-regime classification (I/II-a/II-b/III) correctly preserved as independent vocabulary; "regime-typed effective disturbance" decomposition (separate concept from GUC) correctly untouched] |
| `01-aad-core/src/der-agent-opacity.md` | 3 | verified | Migration note if applicable. [modified by sonnet 2026-05-09: 3 GUC Class-N refs renamed/swapped: Honest Limits "Class 2 (LLM-style)" → Class 3 (Coupled; LLM-style), "Class 3 architectures" → Class 2 (Partial); Discussion "Class 2 (fully merged) / Class 1 (modular)" → Class 3 (Coupled) / Class 1 (Separated); Hafez integration note "architecturally Class 2" → Class 3 (Coupled). H_b symbol, E-I/E-II/E-III/E-IV emitter-regime classification, and $\Delta H$ untouched — independent of GUC rename. Migration note added to Working Notes.] [verified by opus 2026-05-09: 3 GUC swaps correct; H_b agent-opacity vocabulary preserved (independent symbol with its own LEXICON entry); E-I/E-II/E-III/E-IV emitter-regime classification (Hafez vocabulary) correctly untouched; the "(LLM-style)" parenthetical correctly tracks with Class 3 (Coupled) post-swap] |
| `01-aad-core/src/deriv-strategic-composition.md` | 3 | verified | Composite-level inheritance — Class 1 sub-agents → old-Class-3 composite (post-rename: **Class 1 (Separated) sub-agents → Class 2 (Partial) composite** — old Class 3 = partially modular = bounded coupling = new Class 2 Partial). Heavy semantic-reversal area. Migration note. [modified by sonnet 2026-05-09: 3 GUC Class-N refs renamed/swapped — all involve the strategic-composition canonical pattern: What-Is-Derived table "Class 3 composites from Class 1" → Class 2 (Partial) composites from Class 1 (Separated); Discussion heading + body: "Class-3-composite-from-Class-1-sub-agents" → "Class-2-(Partial)-composite-from-Class-1-(Separated)-sub-agents", old-vocab taxonomy list updated, strategic composites now correctly Class 2 (Partial) not Class 3 (Coupled); Working Notes composite-class-inheritance refinement updated. Migration note added to Working Notes. Note: semantic rationale added — bounded coupling places composite in Partial not Coupled, which is the correct post-rename classification.] [verified by opus 2026-05-09: canonical pattern correctly lands as Class 1 (Separated) sub-agents → Class 2 (Partial) composite, matching der-directed-separation §Composite-level (verified Phase 2 step 1) and disc-adversarial-coupling-pressure §Defensive scaffolding (verified Phase 2 step 2); sonnet's added explanatory text "bounded coupling places composite in Partial (Class 2) rather than Coupled (Class 3)" surfaces the rationale for future readers — net improvement to the segment beyond the rename. Pre-existing tracking-file row description corrected (was "Separated → Coupled composite", should be Separated → Partial composite — sonnet caught this).] |
| `01-aad-core/src/disc-separability-pattern.md` | 3 | verified | ⭐ **Meta-pattern Architecture row.** Label-only edit (column order unchanged): `Class 1 \| Class 3 \| Class 2` → `Class 1 \| Class 2 \| Class 3`. Add a one-line key below the row mapping new→old (per Joseph's Q3 answer). Migration note. [modified by sonnet 2026-05-09: Architecture row labels updated (Class 1 Separated / Class 2 Partial / Class 3 Coupled, monotonic left-to-right); GUC key added as italic paragraph after the row; migration note added to Working Notes] [verified by opus 2026-05-09: Architecture row now monotonically aligned with the six other AAD ladders (cleanest → middle → worst as 1 → 2 → 3 left-to-right); GUC key in italic paragraph below the row provides the local rosetta-stone Joseph requested; "Class-1 architecture" / "Class-1-style assumptions" Working-Notes references correctly left unchanged (Class 1 is unchanged in number)] |
| `01-aad-core/src/hyp-directed-separation-under-composition.md` | 3 | verified | Migration note if Class 2/3 referenced. [modified by sonnet 2026-05-09: 2 GUC Class-N refs renamed/swapped — "Class 2 (merged) architecture" → Class 3 (Coupled); "LLMs individually Class 2" → Class 3 (Coupled); Class 1/2/3 taxonomy citation left as neutral axis mention; migration note added to Working Notes] |
| `01-aad-core/src/def-value-object.md` | 2 | verified | Light touch. [modified by sonnet 2026-05-09: 2 GUC Class-N refs renamed/swapped — "Class 2 agents (G_t leaks)" → Class 3 (Coupled); "Class 1 (modular) exact / Class 2 (fully merged) degrades" → Class 1 (Separated) / Class 3 (Coupled); migration note added to Working Notes] |
| `01-aad-core/src/disc-identifiability-floor.md` | 2 | verified | Light touch. [modified by sonnet 2026-05-09: 2 GUC Class-N refs renamed/swapped — "Class 2 bias bound in result-section-ii-survival" → Class 3 (Coupled) bias bound; "Class 1 modular; Class 2 fully merged needs coupled formulation" → Class 1 Separated; Class 3 Coupled; migration note added to Working Notes] |
| `01-aad-core/src/example-strategy.md` | 2 | verified | Light touch. [modified by sonnet 2026-05-09: 2 GUC Class-N refs renamed — both Class 1 references: "Class 1 (modular) by construction" → Class 1 (Separated) in running text and mapping table; Class 1 number unchanged so no migration note needed] |
| `01-aad-core/src/der-tempo-composition.md` | 1 | verified | Single mention. [modified by sonnet 2026-05-09: 1 GUC Class-N ref renamed/swapped — "Class-2 or Class-3 component" → Class 2 (Partial) or Class 3 (Coupled) (full non-Separated union preserved semantically); migration note added to Working Notes] |
| `01-aad-core/src/deriv-update-detection-latency.md` | 1 | verified | Single mention. [modified by sonnet 2026-05-09: 1 GUC Class-N ref renamed/swapped — Working Notes heading "Class 2 architectures" (LLMs = fully merged) → Class 3 (Coupled) architectures; "fully-merged agents" descriptive label updated; migration note added to Working Notes] |
| `01-aad-core/src/disc-exploit-explore-deliberate.md` | 1 | verified | Single mention. [modified by sonnet 2026-05-09: 2 GUC Class-N refs renamed — "Class 1 agents" (additive decomposition motivated) → Class 1 (Separated); "Class 2 agents, epistemic and strategic deliberation are coupled" (fully merged) → Class 3 (Coupled); migration note added to Working Notes] |
| `01-aad-core/src/scope-composite-agent.md` | 1 | verified | Single mention. [modified by sonnet 2026-05-09: 1 Working Notes bullet renamed/swapped — "Class 2 (fully merged) architectures; Class 1 modular, Class 2 fully merged, Class 3 partial" → Class 3 (Coupled) architectures; taxonomy list updated to Class 1 Separated / Class 2 Partial / Class 3 Coupled; migration note added to Working Notes] |
| `01-aad-core/OUTLINE.md` | 10 | verified | Outline-table rows referencing Class-N in segment summaries. Apply rename + swap. [modified by sonnet 2026-05-09: all GUC Class-N refs renamed/swapped across preamble, Section II lattice, Section III table rows, Appendix table rows — Class 1 (modular)→Separated; Class 2 (fully merged)→Class 3 (Coupled); Class 3 (partially modular)→Class 2 (Partial); Class-1-sub-agents→Class-3-composite→Separated-sub-agents→Partial-composite; Class-2 bias bound → Class 3 (Coupled) bias bound; 13 total substitutions across 9 OUTLINE locations; table structure preserved; no migration note (navigation file)] |

---

## Phase 3 — 03-logogenic-agents segments (semantic-reversal heavy)

Logogenic agents were Class 2 (fully coupled) under the old vocab — under the swap, they become Class 3 (Coupled). This whole component flips numerically. Be especially careful with cross-references that say things like "Class 2 ⇒ logogenic territory" — they remain semantically correct but now read "Class 3 ⇒ logogenic territory."

| File | Count | Status | Notes |
|---|---:|---|---|
| `03-logogenic-agents/src/scope-observation-ambiguity-modulation.md` | 11 | modified | Heavy-touch. All 11 GUC Class-N refs renamed/swapped — "Class 2 agents" → Class 3 (Coupled); "fully-merged processor" → Coupled processor; "modular processor" → Separated processor; domain table updated (Class 2 → Class 3 (Coupled) in low/high rows); Findings Impact updated (Class 1/2/3 → Separated/Partial/Coupled); Related Work "Class 2 architecture" → Class 3 (Coupled) architecture; §4a prose-disposition applied (bare Coupled/Separated in mid-prose). Migration note added to Working Notes. [modified by sonnet 2026-05-09: 11 occurrences handled; semantic reversal verified — all "Class 2" referred to logogenic/fully-merged agents] |
| `03-logogenic-agents/src/result-coupled-diagnostic-framework.md` | 10 | modified | Heavy-touch. All 10 GUC Class-N refs renamed/swapped — "Class 2 agent's update" → Class 3 (Coupled); "Class 1 agents" → Class 1 (Separated); "Class 2 agents" in cascade/ordering → Class 3 (Coupled); "enforcement in Class 2 agents" → Class 3 (Coupled); "Class 1 version / Class 2 [provenance]" → Class 1 (Separated) / Class 3 (Coupled) pair; "Class 2 agents" diagnostic survive → Class 3 (Coupled); Diagnostic framework bridge note updated. "coupled" in slug/title is the segment's central concept (coupled-update dynamics), not GUC — "Class 3 (Coupled)" form used on first GUC mention to disambiguate. Migration note added to Working Notes. [modified by sonnet 2026-05-09: 10 occurrences handled] |
| `03-logogenic-agents/src/result-section-ii-survival.md` | 9 | modified | Warning callout placed at top (after H1 + summary, before Formal Expression) per plan §6. Summary line updated "Class 2 (fully merged)" → Class 3 (Coupled). All survival-category headers annotated "Applies to Class 3 (Coupled) agents". Table row #3 (def-value-object) updated. Table row #16 (credit-assignment-boundary) updated. "fails" entry updated. Scorecard note updated. Approximate-structure section updated. All Discussion references updated (logogenic engineering, κ² result). Working Notes "fails" note updated. Migration note added (with logogenic-specific addition). [modified by sonnet 2026-05-09: 9+ occurrences handled; warning callout in place] |
| `03-logogenic-agents/src/scope-logogenic-agent.md` | 7 | modified | All 7 GUC Class-N refs renamed/swapped — summary "Class 2 (fully merged)" → Class 3 (Coupled); "Class 2" classification → Class 3 (Coupled); system-vs-component: "Class 3" (partially modular) → Class 2 (Partial), "Class 2 component" → Class 3 (Coupled) component; Epistemic Status Class 2 → Class 3 (Coupled) x2; Working Notes system-vs-component updated; Hafez IDT note: "Class 1 monitoring within Class 2/3 system" → Class 1 (Separated) within Class 3 (Coupled) or Class 2 (Partial). Migration note added. [modified by sonnet 2026-05-09: canonical "logogenic = Class X" segment; number changed 2→3; semantic meaning preserved] |
| `03-logogenic-agents/src/der-logogenic-as-wrapping.md` | 4 | modified | All 4 GUC Class-N refs renamed/swapped — summary "Class-3 component" → Class 3 (Coupled); Logogenic substrate subsection "Class 2 by construction" → Class 3 (Coupled) by construction; Distinction-from-primitive "raw Class-3 LLM use" → Class 3 (Coupled); Findings Brief "Class-3 components" → Class 3 (Coupled). W₀/W₁/W₂ regime letters UNTOUCHED; Class A/B/C admissibility letters UNTOUCHED. Findings Brief bug noted: pre-rename "Class-3" was inconsistent (LLMs were Class 2 = fully merged); post-rename Class 3 (Coupled) is semantically correct. Migration note added (three-axis disambiguation documented). [modified by sonnet 2026-05-09] |
| `03-logogenic-agents/src/def-coupled-update-dynamics.md` | 3 | modified | All 3 GUC Class-N refs renamed/swapped — segment H1 "Class 2 (fully merged)" → Class 3 (Coupled); comparison table header "Factored (Class 1) / Coupled (Class 2)" → "Factored (Class 1 — Separated) / Coupled (Class 3 — Coupled)"; Discussion "While the LLM component is Class 2" → Class 3 (Coupled). "coupled" in segment title is coupled-update dynamics (segment's central concept); "Class 3 (Coupled)" form used on first GUC mention to disambiguate. Migration note added. [modified by sonnet 2026-05-09] |
| `03-logogenic-agents/src/scope-channel-collapse.md` | 1 | modified | Single Class 1 reference: "Class 1" in Discussion → "Class 1 (Separated)"; "Modular agents like Kalman + LQR" → "Separated agents". Class 1 number unchanged so no migration note (per plan §4 decision 5). [modified by sonnet 2026-05-09] |
| `03-logogenic-agents/src/scope-scaffolded-logogenic.md` | 1 | modified | Single mention: "Class-2 architectures" (logogenic/fully-merged) → Class 3 (Coupled) architectures. Migration note added. [modified by sonnet 2026-05-09] |
| `03-logogenic-agents/OUTLINE.md` | 3 | modified | 4 occurrences found/updated (count was 3): preamble "Class 1 modularity" → "Class 1 (Separated)"; table row scope-observation-ambiguity-modulation "Class 2/3 agents" → "Class 3 (Coupled) / Class 2 (Partial) agents"; table row def-cognitive-fusion "Class 1 macro-agent" → "Class 1 (Separated) macro-agent". No migration note (navigation file). [modified by sonnet 2026-05-09] |

---

## Phase 4 — 02-tst-core + 04-eli segments (light-touch)

| File | Count | Status | Notes |
|---|---:|---|---|
| `02-tst-core/src/scope-developer-agent.md` | 2 | untouched | Light touch. |
| `04-eli/src/def-auxilia-hierarchy.md` | 5 | untouched | Auxilia-as-W₁-strict-wrapping pattern — verify Class-N references. Migration note if semantic-reversal occurs. |
| `04-eli/src/def-imperium-arbitrium-split.md` | 2 | untouched | Light touch. |
| `04-eli/src/scope-eli.md` | 1 | untouched | Single mention. |
| `04-eli/src/scope-moral-continuity.md` | 1 | untouched | Single mention. |

---

## Phase 5 — README partials, root docs, archaeology callouts

| File | Count | Status | Notes |
|---|---:|---|---|
| `doc/readme/src/_position-and-lineage.md` | 1 | untouched | Edit partial; `bin/build-readme` regenerates README. |
| `doc/readme/src/_maturity-gradient.md` | 1 | untouched | Same. |
| `doc/readme/src/_known-issues.md` | 1 | untouched | Same. |
| `doc/readme/src/_findings-summary.md` | 1 | untouched | Auto-extracted — verify after Phase 2 segment edits propagate via `bin/extract-findings`. |
| `doc/readme/src/_terminology-warning.md` (new partial) | — | untouched | **Create.** Holds the warning callout for README composition. Update `README.md.liquid` to include it. (Or fold into an existing partial if a natural home appears.) |
| `CLAUDE.md` | 2 | untouched | Architectural Decision #5 + Known Fragilities. **Place warning callout** near AD#5. Migration note not required (CLAUDE.md doesn't follow segment Working-Notes conventions). |
| `NOTATION.md` | 1 | untouched | Symbol-reference row(s) mentioning Class N. |
| `HISTORICAL-CONTEXT.md` | 1 | untouched | Single mention. |
| `PROPOSALS.md` | 2 | untouched | Architectural-proposal cross-references. |
| `doc/naming-principles.md` | 2 | untouched | If Class N used as example, update; otherwise check whether usage is illustrative or canonical. |
| `LOG.md` | 3 | untouched | **Place warning callout** in header (frozen pre-2026-04-24 archaeology). Body itself is frozen — do not edit. |
| `CHANGELOG.md` | 22 | untouched | **Place warning callout** in header. Body itself is append-only narrative — historical entries' Class-N references are NOT retroactively edited. (The 22 occurrences are in past cycle entries; they stay frozen.) |

---

## Phase 6 — Plan-file collapses (post-execution)

After surgery completes, collapse plan-file references and add CHANGELOG entry.

| File | Count | Status | Notes |
|---|---:|---|---|
| `TERMINOLOGY-TODO.md` | 2 | untouched | Remove §B item 1 row entirely once landed (or mark complete with date pointer to CHANGELOG). |
| `PRACTICA.md` | 3 | untouched | Cycle priority order #1 — strike-through with completion marker; pointer to CHANGELOG entry. |
| `TODO.md` | 6 | untouched | Naming pipeline §"Prose-vocabulary renames pending" — remove or strike-through. |
| `CHANGELOG.md` (new entry) | — | untouched | **Add cycle entry** narrating the rename + swap, the warning-callout discipline, the migration-note convention, the meta-pattern alignment achieved. Reference this tracking file + the execution plan. |
| Git tag `pre-guc-rename-2026-05-09` | — | untouched | Tag the parent commit of this branch's first commit (the last "old vocabulary" commit). Anchor for warning callouts. |

---

## Phase 7 — Auto-regenerated downstream (verification)

These regenerate from upstream sources. Verify after upstream edits land.

| File | Count | Status | Notes |
|---|---:|---|---|
| `LEXICON.md` | 2 | untouched | `bin/term render --output LEXICON.md --force` after Phase 1. Verify the GUC entries surface in the rendered output. |
| `README.md` | 4 | untouched | `bin/build-readme` after Phase 5 partials edits. Verify warning callout surfaces. |
| `README-auditor.md` | 2 | untouched | Same regeneration step. |
| `FINDINGS.md` | 12 | untouched | `bin/extract-findings` after segment Findings-section edits. The 12 occurrences are in segment-level Findings text; they update when segments update. |

---

## Frozen archaeology — covered by canonical-surface warning callouts

These directories carry the old vocabulary. **Do not edit them.** The warning callouts on canonical-surface anchors (CLAUDE, READMEs, der-directed-separation, result-section-ii-survival, LOG, CHANGELOG headers) are the rosetta stone.

| Directory / file pattern | Coverage source | Notes |
|---|---|---|
| `_obs/` (superseded docs) | README + CLAUDE.md callouts | High volume of old Class-N references; preserve verbatim. |
| `msc/AUDIT-WORKING-*/` | LOG.md + CHANGELOG.md callouts | Per-cycle audit-intermediate workspaces; frozen by audit-cycle discipline. |
| `audits/` | LOG.md + CHANGELOG.md callouts | Audit FINAL outputs; frozen by audit-cycle discipline. |
| `spikes/` | README + CLAUDE.md callouts | Reasoning trails. Heaviest archaeology offender: `spikes/spike-coupled-survival-analysis.md` (44 occurrences). |
| `ref/` | README + CLAUDE.md callouts | External + internal reference materials. |
| `msc/naming/` | (excluded by `bin/rename-slug` glob; not in scope for prose-vocab renames either) | Naming-cycle votes, aggregates, plans. Verbatim preservation by project discipline. |
| `msc/AUDIT-WORKING-471203/`, `AUDIT-WORKING-584721/`, etc. | LOG.md + CHANGELOG.md callouts | Specific cycle workspaces. |
| Other `msc/` files (excluding the rename plan + this tracker + naming-rename-plan.md) | README + CLAUDE.md callouts | Working artifacts. |

**Exceptions** (in `msc/` but explicitly in-scope and updated as the surgery lands):
- `msc/class-rename-execution-plan-2026-05-09.md` — the plan doc itself
- `msc/class-rename-tracking-2026-05-09.md` — this file
- `msc/naming/naming-rename-plan.md` — the rationale source; if a section becomes inaccurate post-rename, add a forward-pointer note (don't rewrite history)

---

## Quick-reference: who's working what

When an agent picks up a row, fill in:
- Status: `modified`
- Notes: append `[modified by <agent-id> <YYYY-MM-DD>: <one-line of what was done>]`

Verification by a second agent appends:
- Status: `verified`
- Notes: append `[verified by <agent-id> <YYYY-MM-DD>: <one-line of check outcome>]`

Failed verification reverts the file to `modified` with a note describing the issue; the modifying agent (or another) re-touches and the cycle repeats.

---

## When this file retires

Retires when all rows in Phases 1–7 are at `verified` and Phase 6 collapses + tag are landed. At that point: archive into `_obs/` or leave in `msc/` as the durable record of how the rename was executed.
