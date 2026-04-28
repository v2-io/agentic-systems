# Recommendation: Standardized Format for De Novo Audit Final Reports

> **Superseded 2026-04-28 (later in same session) by [`RECOMMENDED-FORMAT-2026-04-28-v2.md`](RECOMMENDED-FORMAT-2026-04-28-v2.md).** This v1 document surveyed about half the corpus (the AUDIT-WORKING-NNNNNN finals + a few meta-docs); after the corpus grew with 17 newly-extracted `extracted-*-feedback-*.md` files plus the audit-instructions-lineage transcript, a v2 sub-agent surveyed the full corpus and produced a substantially expanded recommendation. The v1 directional shape is preserved — single-file default, required front matter, five-element burden-of-proof schema, coverage statement — and v2 should be read as an evolution rather than a contradiction. Where v1 and v2 differ, follow v2. v1 retained for archaeology of how the recommendation evolved as the evidence base grew.

*Produced 2026-04-28 by a sub-agent surveying the audit corpus (`msc/AUDIT-WORKING-*/FINAL-*.md`, the older `audit-*.md` / `analysis-*.md` documents, the candidate-extraction meta-document, and `doc/de-novo-audit-instructions.md`). Awaiting Joseph's decisions on §5 open questions before any §11 content is added to `doc/de-novo-audit-instructions.md`.*

## 1. Headline

Across the eight final-reports in `audits/` (and the older `audit-*.md` / `analysis-*.md` styles preceding the AUDIT-WORKING-NNNNNN convention), the **substantive shape has actually converged** more than it might appear. What varies is mostly **section *names* and *ordering*, not section *content***. The per-finding format has nearly converged on the five-element burden-of-proof form already specified in `doc/de-novo-audit-instructions.md` §6, with one consistent extension (auditor-added severity / type / disposition fields) that should be promoted from de-facto into the spec.

The recommended format leans into the convergence rather than imposing a rigid template: **one required final-report file with a small set of required top-level sections, a required per-finding schema, and a required Coverage / "What I didn't read" honesty section**. Sub-component splits (`AUDIT-WORKING-849201`-style) should be allowed but governed by an explicit rule. The Phase-2 triangulation should be encouraged to live in a separate `SUPPLEMENT-PHASE-2-TRIAGE.md` so the de-novo report stays auditable as a de-novo artifact, with the corresponding triage triangulation kept distinct from first-encounter judgments.

## 2. Findings from corpus survey

### 2.1 What converged across the AUDIT-WORKING-NNNNNN finals

All five 2026-04-25 finals share a recognizable shape:

| Final report | Required section equivalent |
|---|---|
| `584721/FINAL-2026-04-25.md:1-7` | "Auditor / Status / Posture caveat" header |
| `613842/FINAL-2026-04-25.md:1-19` | "Scope and method" + "What I substantively read / did not fully read" |
| `738192/AUDIT-FINAL-738192.md:1-10` | "Overview" with auditor + date + initial-predictions reflection |
| `742613/FINAL-2026-04-25.md:1-30` | "Scope and Method / Coverage completed / Coverage not completed" |
| `849201/000-FINAL-AUDIT-REPORT.md:1-7` | "Introduction & Audit Posture" + "Audit Scope and Limitations" at end (§4) |

All five then have a **Findings under burden of proof** section, regardless of the section title. All five have some form of **bigger-picture / Section D / Phase 2 / Phase 3** at the end. The variation in *names* is cosmetic; the variation in *content* breaks down on three real axes (§2.2).

### 2.2 Real axes of variation

**(a) Per-finding schema density.** 742613 finds are densest (Status / Confidence / Type / Problematic passage / Counterevidence / Why-it-stands — see `742613/FINAL-2026-04-25.md:33-70` for Finding 1). 849201 finds are lightest (Observation / Critique / Diagnosis-via-msc/). 738192 (Gemini) finds are middle-density (Quote / Critique / Status). The five required burden-of-proof elements named in `doc/de-novo-audit-instructions.md:415-424` are present in 742613 and 584721 but **partially elided in 849201 and 738192** — both compress "counterevidence search" into "Diagnosis (via msc/)" or skip it; both omit explicit confidence levels (738192 uses "Status: Firm" instead).

**(b) Provenance specificity.** 738192 names "Gemini CLI" cleanly. 584721 names "Claude Opus 4.7 (1M context), the same agent that drafted/iterated msc/de-novo-audit-instructions.md" with a posture-caveat foregrounded. 849201 doesn't name the agent at all in the FINAL — you have to infer from `00-initial-predictions.md`. 613842 doesn't name the agent at all.

**(c) Phase-2 placement.** 742613 explicitly separates Phase 2 into `SUPPLEMENT-PHASE-2-TRIAGE.md` — a clean precedent. 584721 folds counterevidence into each finding and adds a triangulation-against-priming disclosure (Section B.4). 849201 mixes Phase 1 and Phase 2 inline ("Diagnosis (via msc/): Known but unfixed"). 613842 does Phase 2 inline per-finding, then has a separate "Integration-debt diagnosis via msc/" section. 738192 doesn't do Phase 2 at all.

### 2.3 Multi-file vs single-file finals

`AUDIT-WORKING-849201/` is the only example of the multi-file pattern (four files: `000-FINAL-AUDIT-REPORT.md` for §I+§II, plus `-SEC-III.md`, `-TST.md`, `-LOGOGENIC.md`). The split tracks the *theory's component structure* — one report per AAD section / TST / logogenic. This is genuinely useful when an audit covers all four components. The single-file pattern works when coverage is partial or AAD-centric. The split has one cost: there's no top-level summary spanning all four files, so a reader has to read all four to get the cross-component view. The naming `000-FINAL-AUDIT-REPORT-{COMPONENT}.md` is awkward — the leading `000` was likely chosen for sort-ordering, but the FORMAT.md slug discipline would prefer `FINAL-2026-04-25-aad-section-iii.md` style.

### 2.4 Initial-predictions discipline

Every AUDIT-WORKING-NNNNNN/ has a `00-initial-predictions.md`. The format varies wildly: 584721's is 60+ lines of detailed predictions plus an explicit "priming bleed disclosed up front" section; 742613's is meticulous about source-order discipline; 738192's is brief (~30 lines); 849201's is medium-length. The "priming bleed disclosed up front" pattern (`584721/00-initial-predictions.md:5-21`) is exemplary and should be lifted into the spec as required when bleed has occurred — but only one auditor did it.

### 2.5 Per-segment artifacts

The AUDIT-WORKING-NNNNNN/ reflection files vary from 25-line bullet-form (738192/01) to 25-line free-form prose (742613/01) to 35-line numbered-prompt-as-form (849201/01). The 849201/01-def-agent-environment.md example is closest to "form-fill" of the §4.4 prompts (the Aside in §4.4 specifically warns against this). The 742613/01 and 584721/-style reflections are more authentic free-form. Neither is wrong; the prescription should not force a sub-format here, but should warn against the form-fill pattern.

### 2.6 Disposition / routing language

This is the weakest area. None of the FINAL reports use a consistent vocabulary for "where should this finding go." Sample dispositions found:

- 742613 SUPPLEMENT introduces a five-tag triage vocabulary: **New / Known-unintegrated / Known-resolved / Tooling gap / Scope-status mismatch** (`SUPPLEMENT-PHASE-2-TRIAGE.md:177-186`). This is the strongest proposal in the corpus.
- 584721 uses ad-hoc severity tags: "Severity: mechanical / editorial", "doc-rot; cosmetic", "editorial".
- 849201 uses informal "Diagnosis: Known but unfixed / Known and accepted".
- 613842 distinguishes inline: "This is integration debt / definition-scope mismatch, not a deep missing theorem."

The candidate-extraction document (`audit-final-reports-candidate-extraction-2026-04-25.md`) shows what the *consumer* of these reports needs: an effort estimate, a strengthen-vs-soften posture flag, source-audit citations, target segment(s), and a fix sketch. None of the source FINALs surface those cleanly; they have to be reconstructed.

### 2.7 Burden-of-proof discipline visibility

`doc/de-novo-audit-instructions.md:412-424` is explicit that findings are "suspected" until verified at routing time. This shows up well in 742613 ("status: still real / confidence: high") and 584721 ("verdict: previously unsurfaced"). It shows up weakly in 849201, where "Finding 1: The Opacity-Gain Tension" reads as a confirmed real issue without explicit confidence calibration. 738192's "Status: Firm" deviates from the instruction's "high/medium/low" vocabulary.

### 2.8 Rescinded-findings transparency

Per CHANGELOG/LOG, rescinded-findings tables are valuable when present. **None of the five 2026-04-25 FINALs include a rescinded-findings list.** `audits/audits-2026-04-22-evening.md:12` explicitly preserves "rescinded-findings tables (each auditor lists candidate findings they checked and rescinded on in-segment counterevidence — the burden-of-proof signal that makes the surviving findings trustworthy)" — this is excellent practice that has *atrophied* under the AUDIT-WORKING-NNNNNN convention. The 584721 report has "What I am not reporting (visibility for the reader)" §B.4 which is the closest equivalent.

### 2.9 Older formats as drift baseline

The `analysis-2026-04-01.md`, `analysis-2026-04-02-*.md`, `audit-2026-04-24-fresh-pass.md`, `audits-2026-04-22-evening.md`, and `opus-audit-2026-04-21.md` documents predate the AUDIT-WORKING-NNNNNN convention. They are mostly single-file (`audit-2026-04-24-fresh-pass.md` is 63KB), multi-auditor consolidations (`audits-2026-04-22-evening.md` preserves Codex / Gemini / Opus transcripts verbatim with rescinded-findings), and include process-feedback alongside findings. The current AUDIT-WORKING-NNNNNN single-auditor pattern is **cleaner** than the older multi-auditor consolidations for primary input, but the older pattern's **rescinded-findings preservation** and **explicit attribution per finding** remain valuable disciplines.

## 3. Recommended format

Add the following content to `doc/de-novo-audit-instructions.md`, ideally as a new §11 ("Standardized format for the final report") immediately following §10. The wording below is content-recommendations; lift voice from existing instructions (peer-to-peer, advisory-not-mandatory) when integrating.

### 3.1 The single required deliverable

Every audit produces one primary deliverable: a markdown file at `audits/audit-NNNNNN-FINAL-YYYY-MM-DD.md` (or `audits/audit-NNNNNN-FINAL-YYYY-MM-DD-pass-N.md` for continuations). The cycle's intermediate workspace lives at `msc/AUDIT-WORKING-NNNNNN/` (lowercase-named files: predictions, per-segment reflections, running outline). Multi-file splits are permitted (see §3.6) but each split file must follow the same internal shape and the same `audit-NNNNNN-FINAL-{suffix}.md` location pattern. *(Convention updated 2026-04-28: FINALs lifted out of working dirs to keep `audits/` purely consumable.)*

### 3.2 Required top-level sections (in this order)

1. **Front matter** (3-6 lines, no heading; immediately follows title)
2. **§A. Scope and method** (or "Scope" — required even if brief)
3. **§B. Findings under burden of proof** (or "Findings" — required even when zero, in which case state explicitly per `doc/de-novo-audit-instructions.md:144-149`)
4. **§C. Coverage statement** ("What I read first-hand / What I did not read / Verification I did not run")
5. **§D. Bigger-picture observations** (or "Hypothesis-tier observations" — optional but encouraged; see §3.5)
6. **§E. Confirmation and what holds** (optional but encouraged — explicit "the framework's discipline holds in X, Y, Z")
7. **§F. Process feedback on the instructions** (optional)

Section names and numbering can vary; section *content* is what matters. Auditors who surface something that doesn't fit this shape should follow `doc/de-novo-audit-instructions.md:434` ("If you find something that doesn't fit the 'finding' form but seems worth surfacing... that's often the most valuable thing you can contribute") and add their own section.

### 3.3 Required front matter

```
**Auditor:** {model name} {(context-window note if relevant)}, {role caveats e.g. "also wrote part of this instructions file"}
**Date:** YYYY-MM-DD
**Status:** {Full | Partial — honestly framed | Continuation of #NNNNNN}
**Coverage summary:** {one-sentence: e.g. "AAD §I (all 30 segments) + §II rows 1–26; §III, all of TST, all of logogenic, and all Appendix B unread first-hand."}
**Priming bleed disclosure** (if applicable): {one or two sentences if CLAUDE.md / MEMORY.md / TODO.md content was already in context — see §3.4}
```

### 3.4 Required per-finding schema

Each finding must include the five elements from `doc/de-novo-audit-instructions.md:415-424` (problematic passage / counterevidence search / status determination / confidence / why-it-stands when status is "still real"), plus three additions that the corpus repeatedly used informally:

- **Type** — one of `{math error | sign error | scope/status mismatch | cross-segment contradiction | dependency-graph violation | integration debt | doc rot | citation error}`. The 742613 SUPPLEMENT vocabulary is a useful reference but not exhaustive.
- **Severity** — one of `{mechanical/editorial | scope-honesty | substantive | architectural}`. Severity is *not* the same as confidence; a high-confidence finding can be mechanical (depends-list violation), and a medium-confidence finding can be architectural (ontology strain).
- **Disposition (suggested)** — one of `{pending-findings | PROPOSALS-bundle | TODO direct | closed-as-already-caveated | Phase-2 triangulation needed}`. This is the auditor's *recommendation*, not a routing decision; the routing happens at consumer time.

The five-element form is *required*; the three additions are *strongly recommended* but auditors may suppress fields where they don't apply (e.g., a Section-D Hypothesis-tier observation doesn't need Severity).

### 3.5 Hypothesis-tier observations vs findings

Section D items must be marked clearly as `Hypothesis`-tier per the epistemic ladder (`doc/de-novo-audit-instructions.md:51`) and per `§6.1 Phase 3` framing (`doc/de-novo-audit-instructions.md:442`). 584721's Section D uses "**Hypothesis.** {claim}" prefix consistently — this is the standard to follow.

### 3.6 When multi-file splits are appropriate

Multi-file finals are appropriate when:

- Coverage spans three or more components (AAD core / TST / logogenic / logozoetic), AND
- Each component's audit is substantive enough to stand alone (more than ~5 findings or substantial Section D content)

Naming convention for multi-file: `audits/audit-NNNNNN-FINAL-{component-slug}.md` where `component-slug` is `aad-section-i`, `aad-section-ii`, `aad-section-iii`, `aad-appendix-a`, `tst`, `logogenic`, `logozoetic`. The leading `000-` prefix used in 849201 is **not** required and discouraged; the cycle-id prefix plus component slug suffices.

When splitting, also produce a top-level `audits/audit-NNNNNN-FINAL.md` containing only:

- The required front matter
- A pointer table to the split files
- Cross-component findings (findings that span multiple split files)
- An integrated bigger-picture / Section D if cross-cutting observations exist

This addresses the 849201 "no cross-component summary" gap.

### 3.7 Phase-2 triangulation — separate file

Phase-2 triangulation against `msc/` / `TODO.md` / `PROPOSALS.md` should live in a separate `SUPPLEMENT-PHASE-2-TRIAGE.md` (per 742613 precedent), *not* mixed inline into the de-novo FINAL. This keeps the de-novo report auditable as a fresh-encounter artifact, while the supplement carries the triage classifications.

The Phase-2 supplement should classify each finding using the 742613 vocabulary (`SUPPLEMENT-PHASE-2-TRIAGE.md:177-186`):

- **New** — no durable tracking found; add to pending-findings
- **Known-unintegrated** — correct idea exists elsewhere; source segment still wrong
- **Known-resolved** — source already fixed; finding is stale
- **Tooling gap** — source structurally OK under current tools, but audit exposed a class the tools don't check
- **Scope/status mismatch** — caveat exists in prose but not in Formal Expression / status / theorem statement

Lifting this vocabulary into the spec gives consumers (TODO/PROPOSALS routing agents) a stable mental model.

### 3.8 Rescinded-findings transparency — required when present

If during the audit you generated candidate findings that were rescinded on in-segment counterevidence (the §6 burden-of-proof gate genuinely working), include a `### What I am not reporting` subsection in §B with:

- Brief description of the candidate finding (one sentence each is fine)
- Why it didn't survive (segment text reference)

This is the discipline-confirmation signal. 584721 §B.4 is the model. Without it, the surviving findings are less trustworthy because the reader can't see the gate working.

### 3.9 Coverage statement (§C) — explicit format

The coverage section should answer four questions explicitly:

1. **Read first-hand** — list every segment slug, ideally grouped by component / appendix
2. **Not read first-hand** — list the slugs you didn't read (groupable)
3. **Verification not run** — what mathematical checks, citation checks, lint runs, sub-agent dispatches you skipped
4. **What this means** — one paragraph on the audit's standing (defensibility scope)

584721 §F is the strongest example. 742613's "Coverage completed / Coverage not completed" is also good. 849201's coverage statement (§4) is too brief — the reader can't tell how complete the audit is.

### 3.10 Confidence calibration vocabulary

Use the §6 vocabulary: `high / medium / low` with a one-clause reason. Avoid alternatives like "Firm" (738192) or omission (849201). When confidence depends on priming-content rather than first-hand verification, say so: "Confidence: medium-high — depends on CLAUDE-2.md priming being accurate that BH-identity replaced Pinsker as primary in `#deriv-strategy-cost-regret-bound`. Direct verification by reading `#deriv-strategy-cost-regret-bound` was deferred." (Lifted from `584721/FINAL-2026-04-25.md:100-101`.)

## 4. Migration considerations

**Don't retroactively reformat existing audits.** The five 2026-04-25 FINAL reports plus the older audits/analysis documents are historical record. Reformatting them would (a) waste effort on closed cycles; (b) erase the variation that this recommendation is partly justified by; (c) create false uniformity for documents that were genuine first-attempts.

The candidate-extraction document `audit-final-reports-candidate-extraction-2026-04-25.md` already serves the cross-audit consolidation role; that pattern (read all FINALs at once, extract canonical AF-NN identifiers, map to TODO/PROPOSALS) is the right way to handle format heterogeneity at consumption time.

**The format should evolve in pilot-then-sweep mode** (per `feedback_pilot_then_sweep_pattern`). The next 1-2 audits should follow this format and surface gaps; only after that do we consider whether to lift any of these recommendations into stricter requirements.

**One small backfill is worth considering:** add a one-paragraph attribution + status header to the four older AUDIT-WORKING-849201 split files. Each currently fails to name the agent in the FINAL itself. This is a 5-line addition per file, low-risk, makes the audits more useful as historical reference. Not required.

## 5. Open questions / judgment calls for Joseph

1. **The five-tag Phase-2 triage vocabulary.** Lifting it into the spec is the strongest individual recommendation. But it was authored by Codex in 742613 SUPPLEMENT and hasn't been used by other auditors yet. Worth piloting with one more audit before freezing? Or freeze now since the underlying distinction (new vs known-unintegrated vs known-resolved vs tooling gap vs scope-status mismatch) is real?

2. **Multi-file vs always-single-file.** I've recommended permitting both. The alternative is to require single-file always and accept that long audits produce 100KB+ FINALs. The 849201 split is genuinely readable per-component; the absence of a top-level cross-component summary is a real loss. My recommendation is "permit with discipline (top-level pointer + cross-cutting summary required when split)." Reasonable to disagree.

3. **Disposition field (§3.4).** I added it as "strongly recommended." It might be better as "required" — the candidate-extraction process clearly needs this signal and reconstructing it after the fact is wasteful. But auditors may legitimately not know the disposition (a fresh finding is "pending-findings" by default; the rest involves judgment about TODO vs PROPOSALS). Could go either way.

4. **The FINAL.md naming for partial/aborted audits.** Should this format also govern partial/aborted audits? The 738192 audit covers only Section I-early and Section II partially; the FINAL is short. Maybe an explicit "minimum viable audit final" specification would help — e.g., "even a 2-finding 1-section partial audit must include §A (scope) and §C (coverage), but §D-§F are optional." Worth adding?

5. **Per-segment reflection format.** I deliberately did *not* recommend a sub-format (§4.4 explicitly warns against forms). But the variation between 849201's prompt-fill style and 742613's prose style is large. Is some additional advisory text warranted, or does the existing §4.4 Aside cover it?

6. **The candidate-extraction document pattern.** `audit-final-reports-candidate-extraction-2026-04-25.md` is itself a useful artifact pattern (reads multiple FINALs, produces a canonical AF-NN list of local fixes). Should the de-novo-audit-instructions name it? Or is it consumer-side rather than audit-side and outside the scope of these instructions?

---

**Key files referenced:**

- `doc/de-novo-audit-instructions.md` (target file; do not modify until decisions land)
- `audits/audit-584721-FINAL-2026-04-25.md` (strongest worked example for §3.2-3.10 patterns)
- `audits/audit-742613-FINAL-2026-04-25.md` + `SUPPLEMENT-PHASE-2-TRIAGE.md` (densest per-finding schema; canonical Phase-2 separation)
- `msc/AUDIT-WORKING-849201/000-FINAL-AUDIT-REPORT*.md` (multi-file split precedent and its weaknesses)
- `audits/audit-738192-FINAL.md` (deviant naming; lighter-density finds)
- `audits/audit-613842-FINAL-2026-04-25.md` + `00-running-outline.md` (running-outline pattern transcribed cleanly)
- `audits/audit-final-reports-candidate-extraction-2026-04-25.md` (consumer-side need; AF-NN naming pattern; effort/strengthen-soften fields)
- `audits/audits-2026-04-22-evening.md` (rescinded-findings preservation discipline; pre-AUDIT-WORKING multi-auditor consolidation pattern)
- `audits/audit-2026-04-24-fresh-pass.md` (the "zero findings" → five-findings-after-cross-audit case; reading-mode-failures post-mortem worth modeling)
