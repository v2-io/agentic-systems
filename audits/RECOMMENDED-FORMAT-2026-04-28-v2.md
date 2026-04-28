# Recommendation: Standardized Format for De Novo Audit Final Reports (v2)

*Produced 2026-04-28 by a sub-agent surveying the **full** audit corpus in `audits/` (formal-cycle FINALs, older standalone audits, pending-findings consumer-side docs, the link-and-file-hygiene exemplar, the candidate-extraction artifact, all `extracted-*-feedback-*.md` archaeology, and the audit-instructions-lineage session transcript). Supersedes [`RECOMMENDED-FORMAT-2026-04-28.md`](RECOMMENDED-FORMAT-2026-04-28.md) (v1, which surveyed only the AUDIT-WORKING-NNNNNN finals + a few meta-docs); v1 is preserved as historical context but the recommendations below should be the basis for the eventual `doc/de-novo-audit-instructions.md` §11. Awaiting Joseph's decisions on §6 open questions before any §11 content lands.*

---

## 0. Why a v2

V1's evidence base was narrow (about half the corpus): the five 2026-04-25 AUDIT-WORKING finals plus a few older `analysis-*.md` and `audit-2026-04-24-fresh-pass.md`. The broader corpus — 17 newly-extracted `extracted-*-feedback-*.md` files, four `pending-findings-YYYY-MM-DD.md` consumer-side resolution-trail records, the `link-and-file-hygiene-findings.md` exemplar (just-integrated, integrator-tested), the `audit-final-reports-candidate-extraction-2026-04-25.md` aggregator, and the full `extracted-claude-session-6da0db68-...` failure-and-recovery transcript — changes the shape of the recommendation:

1. **Convergence is broader than v1 thought.** Five-element burden-of-proof + file:line anchors + status/confidence vocabulary appear consistently across Codex, Gemini, Claude, and across several months. V1 noticed this in the AUDIT-WORKING finals; the broader corpus shows it's been the de-facto discipline since 2026-04-21.
2. **The consumer-side artifact (pending-findings) is at least as load-bearing as the audit FINAL.** V1 mentioned the candidate-extraction document but treated it as optional. The broader corpus shows that *every cycle Joseph cared about routing landed via a pending-findings doc, not via the FINAL alone*. The format should explicitly handle the FINAL → pending-findings → routing pipeline.
3. **There are at least five distinct *kinds* of audit, not one or three.** V1 grouped them implicitly. The broader corpus reveals enough variation that the spec should name the kinds and note which conventions apply to which.
4. **The Codex hygiene audit (`link-and-file-hygiene-findings.md`) is the strongest exemplar in the corpus** for integrator-friendly shape — and it's notably *not* in the AUDIT-WORKING-NNNNNN family. It's a one-off Codex pass, not a v2-instructions output. That matters: the integrator-friendly properties are *not* downstream of the AUDIT-WORKING protocol; they're consumer-driven content shape that auditors can produce regardless of intermediate-workspace discipline.
5. **The failure-and-recovery transcript** (`extracted-claude-session-6da0db68-...`, not a single audit but the full lineage of how the instructions came to exist) shows what the format is *protecting against*: Claude Opus's first pass produced "zero findings" via delegated comprehension and charitable reading; Gemini and Codex independent passes immediately surfaced 5+ findings; the auditor's "Reading-mode failures" post-mortem became the seed for `doc/de-novo-audit-instructions.md` itself. The format should make that failure mode harder to slip into.

The recommendation below is bigger than v1's; that's deliberate. The corpus is bigger than v1 saw, and the corresponding instructions should be specific enough to prevent the recurring failure modes the corpus documents.

## 1. Headline

**The format should optimize for the integrator's job, not the auditor's introspection.** The AUDIT-WORKING-NNNNNN protocol already separates intermediate-thinking artifacts (lowercase, in `msc/AUDIT-WORKING-NNNNNN/`) from output deliverables (ALL-CAPS, in `audits/`); the §11 spec should add a parallel discipline at the *content* level: the FINAL's structure should make the audit → tracking-file routing pipeline trivial.

Concretely: the FINAL should include (a) front-matter with auditor + scope + coverage state, (b) findings with file:line anchors and a per-finding consumer-recommendation field, (c) a Phase-2 triangulation classification (separate file or inline, but always present and with a fixed vocabulary), (d) a coverage statement honest about what was not read, (e) a rescinded-findings list (the burden-of-proof signal that builds reader trust), and (f) optional but encouraged Discussion of bigger-picture observations and process feedback.

This recommendation lifts established de-facto disciplines into spec, with one substantive addition (the audit-type tag), three substantive prescriptions (file:line discipline, Phase-2 vocabulary, rescinded-findings transparency), and one structural recommendation (the FINAL → pending-findings → routing pipeline as a documented artifact pattern, not just an emergent practice).

## 2. Findings from the broader corpus survey

### 2.1 Convergent best practices across the full corpus

These appear across 80%+ of disciplined audits in `audits/`, regardless of model, date, or audit type:

| Practice | Evidence across corpus |
|---|---|
| **Five-element burden-of-proof** (passage / counterevidence / status / confidence / why-it-stands) | Established as the canonical form in `doc/de-novo-audit-instructions.md` §6; visibly used in `audit-742613-FINAL`, `audit-584721-FINAL`, `audit-613842-FINAL`, `audit-738192-FINAL`, `audits-2026-04-22-evening.md` (all three sub-audits), `opus-audit-2026-04-21.md`, `audit-2026-04-24-fresh-pass.md`, `link-and-file-hygiene-findings.md` (in classification form), most `extracted-codex-feedback-*` files, several `extracted-claude-feedback-*` files |
| **file:line locator anchors** | Codex uses them religiously (every Codex finding in `extracted-codex-feedback-*` includes `path:line` references); Claude typically includes them when disciplined (`audit-2026-04-24-fresh-pass.md`, `extracted-claude-feedback-2026-04-22-bf945f78`); Gemini sometimes includes them (`audit-738192-FINAL.md` does at section level not line level); the integrator-friendly exemplar (`link-and-file-hygiene-findings.md`) tabulates them in dedicated columns |
| **`still real / already caveated / ambiguous` status vocabulary** | Originates in `doc/de-novo-audit-instructions.md` §6 step 3; visibly used in 742613, 584721, 613842, opus-audit-2026-04-21, audit-2026-04-24-fresh-pass, all three audits in audits-2026-04-22-evening; Codex uses "still real" most consistently; Gemini sometimes deviates ("Firm" in 738192) but the substantive intent matches |
| **`high / medium / low` confidence** | Standard in 584721, 613842, 742613, opus-audit-2026-04-21, all three audits in audits-2026-04-22-evening, all extracted Codex feedback; Gemini deviates ("100%" in extracted-audits-2026-04-25, "Firm" in 738192); Claude sometimes uses compounds ("medium-high"); cleaner is `high|medium|low` with a one-clause reason |
| **"What I read / what I did not read"** (coverage section) | 742613, 584721, 613842, audit-2026-04-24-fresh-pass, audit-849201-FINAL §4, audit-738192-FINAL (less formal); the integrator-friendly hygiene audit names "Checks Run" |
| **Cross-audit overlap maps / consolidated finding IDs** | Used in `pending-findings-2026-04-22.md` (Findings index table by source/severity/subsumption), `pending-findings-2026-04-23.md` (consolidated ID column showing which audits agreed), `pending-findings-2026-04-25.md` (similar), `audits-2026-04-22-evening.md` (cross-audit reconciliation in body); not used in single-auditor FINALs because they don't need it |
| **"Bigger picture" / "Process feedback" sections** | 742613 has both; 738192 has process feedback ("The instructions were excellent…"); 584721 §A is a process-feedback stress-test; opus-audit-2026-04-21 has bigger-picture observations; audit-849201-FINAL has §3 ("Structural Triumphs"); even the link-and-file-hygiene audit has "Recommended Fix Order" and "Verification Snapshot" sections at the end. *Bigger-picture is the norm, not the exception.* |

### 2.2 Variation that is real but not problematic

These vary across the corpus and the variation should be permitted, not standardized:

- **Section names and ordering.** Some audits use "Section A / B / C / D / E" (584721); some use "Findings / Other Observations / Process Feedback" (738192); some use numbered sections (849201). Section *content* matters; section *names* don't. The spec should describe required content, not enforce names.
- **Per-finding sub-structure.** 742613 finds are densest (Status / Confidence / Type / Problematic passage / Counterevidence / Why-it-stands as labeled bullets); 849201 finds are lightest (Observation / Critique / Diagnosis); 584721 finds are middle-density. The five-element form is required content; the visible sub-structure is auditor judgment.
- **Bigger-picture content.** Audit-849201-FINAL-LOGOGENIC's "Structural Triumphs" is a positive-content section celebrating what works; 584721's Section D is a Hypothesis-tier list; opus-audit-2026-04-21's "What I'd recommend" is repair-direction-focused. Different framings for the same kind of content.

### 2.3 Variation that is genuinely problematic and the spec should address

**Disposition vocabulary** is the single biggest gap. The auditors converge organically on similar concepts (still real / already caveated / ambiguous for *finding status*) but **diverge on *finding disposition*** — i.e., where the finding should land:
- 742613 SUPPLEMENT introduces the five-tag Phase-2 vocabulary explicitly: **New / Known-unintegrated / Known-resolved / Tooling gap / Scope-status mismatch**.
- 584721 uses ad-hoc severity tags: "Severity: mechanical / editorial / scope-honesty / substantive / architectural".
- 613842 uses inline diagnoses: "integration debt / definition-scope mismatch", "doc rot; cosmetic", "scope-honesty drift".
- audit-849201-FINAL labels findings as "Known but unfixed / Known and accepted".
- Codex feedback regularly distinguishes "still real / already caveated" status from a separate routing recommendation.

**The five-tag Phase-2 vocabulary subsumes most of these**, with one extension: severity (mechanical / editorial / substantive / architectural) is *orthogonal* to disposition (where the finding lands). Both should be present.

**file:line anchor discipline** varies dramatically. Codex's habits are exemplary; Gemini's are weakest; Claude is in between. The spec should make file:line anchors a strong requirement for every finding because the integrator's first action on receiving a finding is to look at the segment, and an anchor saves 30 seconds per finding × 50+ findings per cycle.

**Rescinded-findings transparency** is inconsistent. Models that use it well: 584721 §B.4 ("What I am not reporting"); audits-2026-04-22-evening Opus has a "Findings that DID NOT survive the burden-of-proof test" table; audit-2026-04-24-fresh-pass has "Reading-mode failures" post-mortem after the auditor missed five findings; Codex sometimes lists "non-findings worth saying explicitly" (extracted-codex-feedback-2026-04-21). Models where it's missing: 738192 (none); 742613 has it implicitly via "Other Observations" but the rescinded reasoning isn't tabulated; 849201 doesn't include it. **Without rescinded-findings, the reader cannot calibrate trust in the surviving findings** — and the broader corpus has the data to show this matters: the audits with rescinded tables consistently have higher integration confidence than those without.

### 2.4 The integrator-friendly exemplar (`link-and-file-hygiene-findings.md`)

This 2026-04-28 Codex hygiene audit is the strongest model in the corpus for integrator-side shape. Its structural moves:

1. **Executive summary** at the top stating the four high-value cleanup areas in one paragraph, so the integrator can prioritize routing in 30 seconds.
2. **"Checks Run"** section listing what tools were executed and what each surfaced — making the audit's evidentiary basis explicit.
3. **Per-finding header pattern**: each finding has a one-line **Classification** ("true stale active references", "true broken links in an active root doc", "stale current instructions", etc.), then a **table** with `file:line` columns when applicable, then a **Recommendation** paragraph.
4. **"Historical or Provenance References That Look OK"** section explicitly listing what the auditor *checked and decided not to flag*. This is rescinded-findings transparency for hygiene-grade work.
5. **"Recommended Fix Order"** numbered list at the end — the implicit candidate-extraction pre-built into the audit itself.
6. **"Verification Snapshot"** section at the very end naming exactly which tools confirmed which non-issues.

This is the post-finding consumer-side artifact pattern *embedded in the FINAL itself*. The candidate-extraction document (`audit-final-reports-candidate-extraction-2026-04-25.md`) does the same after-the-fact for multi-audit consolidation — but the hygiene audit shows that single-auditor FINALs can do it inline. **The spec should encourage this shape.**

### 2.5 The pending-findings docs are the actual routing artifact

Joseph's prior thoughts (in the task brief) noted that pending-findings docs are "arguably the most important evidence for what the integrator needs." The broader corpus confirms this strongly:

- `pending-findings-2026-04-22.md` opens with a resolution-status block crediting specific commits (`14a6095`, `b6134c2`, ...) for resolving Findings 1, 3, 5, 7, 10, 11, 13. The doc is *both* an audit-finding artifact *and* a tracking ledger.
- `pending-findings-2026-04-23.md` has a cross-audit overlap map that explicitly merges findings (Codex 1 + Opus C → F22; Gemini 1 → merged into F26; etc.).
- `pending-findings-2026-04-25.md` reverses the typical FINAL-then-pending pattern: the audit produced findings the auditor missed, and the pending-findings doc is where the verified-against-current-src catalog lives.

The pending-findings format converges on:
- Front-matter with cycle date, source audits, and a "Read alongside" pointer block
- A consolidated-ID overlap map as a table
- Per-finding entries with the same five-element form *plus* explicit landing-path / repair-direction / effort estimate
- "Subsumed by" cross-references to architectural proposals
- Resolution status updates retroactively added when findings land

**This format should be named in the spec, with a recommendation that auditors who want their work routed cleanly should produce — or be aware their output will be routed through — a pending-findings doc.** The auditor doesn't have to write it; an integrator agent typically does. But the FINAL's shape should make the integrator's job possible.

### 2.6 The five distinct audit types in the corpus

The corpus contains audits of substantively different kinds. Naming them helps clarify which conventions apply to which:

| Type | Example(s) | Distinctive properties |
|---|---|---|
| **A. Hygiene audit** | `link-and-file-hygiene-findings.md`; `extracted-codex-feedback-2026-04-28.md` | Tool-driven; mostly mechanical; very integrable; integrator-friendly shape comes naturally; no Phase-2 triangulation needed because there's no theory-state to triangulate against |
| **B. De-novo theory audit** | All 5 AUDIT-WORKING-NNNNNN finals; `opus-audit-2026-04-21.md`; `audit-2026-04-24-fresh-pass.md` | Substantive; segment-reading-driven; benefits from Phase-2 triangulation against `msc/`; full burden-of-proof discipline; coverage statement load-bearing |
| **C. Multi-pass batch / parallel triple** | `audits-2026-04-22-evening.md`; `extracted-audits-2026-04-22-morning.md`; `extracted-audits-2026-04-25.md` | Multiple auditors, same snapshot; cross-audit overlap is the load-bearing pattern; rescinded-findings preservation is exceptionally valuable here |
| **D. Relayed-feedback extraction** | All 17 `extracted-*-feedback-*.md` files; `feedback-2026-03.md` | Verbatim text Joseph passed on from external models; format is whatever the upstream model produced; the wrapper adds Context / Disposition / Verbatim sections |
| **E. Strategic portfolio review** | `extracted-claude-feedback-2026-04-22-25-portfolio-reviews.md` (4 sessions); the "Portfolio re-review" portions of the 6da0db68 lineage | Not a findings audit; ranking / ordering / prioritization guidance; produces session-level recommendations; doesn't fit the burden-of-proof form because the content isn't "is this claim true" but "what should we do next" |

**The spec should focus on Type B** (de-novo theory audits) because that's what the AUDIT-WORKING-NNNNNN protocol produces and that's what Joseph's task is targeted at. **Type A is similar enough** that the same conventions apply, with Phase-2 triangulation skipped and the file:line discipline easier to satisfy. **Type C** uses Type B's per-finding format; the cross-audit overlap map is the wrapper around individual Type B audits. **Type D** is "preserve verbatim", outside the spec's scope. **Type E** is a different kind of artifact that shouldn't follow this spec at all and should be explicitly excluded.

### 2.7 Older (pre-burden-of-proof-discipline) audits

The 04-02 / 04-03 / 04-06 batches (`analysis-2026-04-01.md`, `analysis-2026-04-02-comprehensive.md`, `audits-2026-04-22-evening.md`, etc.) predate the burden-of-proof discipline. They are looser, prose-shaped, and present findings as "ranked by severity" rather than "surviving counterevidence". This is the lineage from which the formal discipline emerged — the 2026-03-13 feedback doc, for instance, is a three-model consolidation pre-burden-of-proof; the 2026-04-06 analysis transitions to file:line anchors but not to "still real / already caveated"; the 2026-04-21 audits are the first to consistently apply the discipline.

**These older audits should not be retroactively reformatted** (per v1's recommendation, which I retain). But they're useful evidence for what the discipline added: cleaner routing, calibrated trust signals, and tractable cross-audit overlap. The discipline is real and worth preserving in the spec.

### 2.8 What the failure-and-recovery transcript adds

`extracted-claude-session-6da0db68-2026-04-24-audit-instructions-lineage.md` is the full conversation that produced `doc/de-novo-audit-instructions.md` itself. Reading it teaches what the format is *defending against*:

1. **Delegated comprehension** ("Let me dispatch parallel deep audits") → findings inherit sub-agent compression artifacts → no first-hand basis to defend any claim
2. **Charitable reading on worked examples** → the zero-sum sign error in `deriv-strategic-composition` (F-V4) was missed by the primary auditor who "confirmed the segment's framing was reasonable and moved on"
3. **Within-segment vs cross-segment discipline** → C-iv landing into `scope-composite-agent` without propagating to `scope-multi-agent` (F-V2) is exactly the integration-drift the within-segment discipline misses
4. **Sample bias toward "load-bearing centers"** → `deriv-discrete-sector-condition` skipped because it "felt appendix-grade" — but it's where F-V1 (the discrete-to-continuous variance gap math error) lived
5. **Premature "zero findings" as confirmation** → the auditor produced "zero findings" after partial coverage, until Gemini and Codex independent passes immediately found 5+

**These five anti-patterns are now §3.1–§3.7 of `doc/de-novo-audit-instructions.md`.** The format spec's job is to make these anti-patterns visible *in the FINAL itself* — i.e., the format should require auditor-disclosure of how they avoided each anti-pattern. The coverage statement, rescinded-findings list, math-verification subsection, and provenance specificity (single-auditor first-hand vs multi-pass with cross-checking) are the disclosures that make the failure modes harder to slip past.

The transcript itself should *not* be modeled — it's not a single audit, it's the failure-and-recovery arc. But it tells you what the format is for.

## 3. Recommended format

Add the following content to `doc/de-novo-audit-instructions.md`, ideally as a new §11 ("Standardized format for the final report") immediately following §10. The voice should match existing instructions (peer-to-peer, advisory-not-mandatory) when integrating; the recommendations below are content, not voice.

### 3.1 The single primary deliverable (and its destination)

Every audit produces one primary deliverable: a markdown file at `audits/audit-NNNNNN-FINAL-YYYY-MM-DD.md`. This is the location convention already specified in `doc/de-novo-audit-instructions.md` §"Before you begin" and §4.7; the §11 spec inherits it. Continuations use `-pass-2.md`, supplements use `-SUPPLEMENT-{topic}.md`, multi-file splits use `-FINAL-{component}.md` with a `-FINAL.md` coordinator.

The intermediate workspace lives at `msc/AUDIT-WORKING-NNNNNN/` with lowercase-named files (predictions, per-segment reflections, running outline). The §11 spec is for the FINAL only.

### 3.2 Required front matter

Every FINAL begins with a 5–8-line front-matter block (no heading; immediately follows title):

```
**Auditor:** {model name and version} {(context-window note if relevant)}, {role caveats e.g. "co-author of these instructions" / "fresh main session" / "running concurrent with NNNNNN"}
**Date:** YYYY-MM-DD
**Audit type:** {Hygiene | De-novo theory | Multi-pass batch | Targeted}
**Status:** {Full | Partial — honestly framed | Continuation of #NNNNNN}
**Coverage summary:** {one-sentence: e.g., "AAD §I (all 30 segments) + §II rows 1–26; §III, all of TST, all of logogenic, and all Appendix B unread first-hand."}
**Priming bleed disclosure** (if applicable): {one or two sentences if priming-heavy content was already in context — see §3.4}
**Phase 2 status:** {Not yet conducted | Conducted in §C of this report | Conducted in `audit-NNNNNN-SUPPLEMENT-PHASE-2-TRIAGE.md`}
```

The `Audit type` field is new and important: it tells the integrator which conventions apply (e.g., hygiene audits skip Phase 2 triangulation; multi-pass batches expect a cross-audit overlap map).

### 3.3 Required top-level sections

The following content is required (in any order, under any names; section *names* don't matter, section *content* does):

1. **Scope and method** — what was read, what tools were run, what discipline was applied. Required even if brief.
2. **Findings under burden of proof** — required, even when the count is zero (in which case state explicitly per `doc/de-novo-audit-instructions.md` §3.6 and include §3.7's rescinded-findings discipline).
3. **Coverage statement** — explicit list of what was read first-hand, what was not read, what verification was not run (`bin/lint-outline`, math re-derivation, citation web-verify, sub-agent dispatches, etc.), and what this means for the audit's standing.
4. **Rescinded findings / "what I am not reporting"** — see §3.7.

The following content is *required-or-explicit-omission* (i.e., either include or state that you considered and chose to omit):

5. **Phase 2 triangulation** — see §3.6.
6. **Bigger-picture / Hypothesis-tier observations** — see §3.5. If omitted, state why (e.g., "Hygiene audit; not applicable").
7. **"What holds" / confirmation** — see §3.5.
8. **Process feedback on the instructions** — optional but encouraged.

### 3.4 Required per-finding schema

Every finding must include the five elements from `doc/de-novo-audit-instructions.md` §6.1:

1. **Problematic passage** — quote the specific text, **with file:path:line anchors** (see §3.4.1 for the discipline)
2. **Counterevidence search** — what the rest of the framework says
3. **Status determination** — `still real | already caveated | ambiguous`
4. **Confidence level** — `high | medium | low` with a one-clause reason. (Avoid alternatives like "Firm" or "100%"; alignment with `high|medium|low` aids cross-audit overlap detection.)
5. **Why it still stands** *(only if status is "still real")* — one sentence

Plus three additions the corpus consistently uses (lift to required):

6. **Type** — one of `{math error | sign error | scope/status mismatch | cross-segment contradiction | dependency-graph violation | integration debt | doc rot | citation error | overclaim | other}`. The 742613 SUPPLEMENT vocabulary plus link-and-file-hygiene's Classification headers give this list; auditors may add types when needed.
7. **Severity** — one of `{mechanical/editorial | scope-honesty | substantive | architectural}`. Distinct from confidence: a high-confidence finding can be mechanical (depends-list violation) and a medium-confidence finding can be architectural (ontology strain).
8. **Disposition (suggested)** — see §3.6's five-tag vocabulary. The auditor's *recommendation* for routing, not a routing decision (which happens at consumer time).

Plus one addition the corpus uses inconsistently but which the integrator-friendly exemplar shows is high-leverage (lift to strongly recommended):

9. **Effort estimate** — one of `{trivial (≤15 min) | editorial (≤1 hr) | substantive (≤4 hr) | architectural (multi-session)}`. The candidate-extraction document already extracts this implicitly; making it per-finding metadata saves the consumer-side aggregator pass.

#### 3.4.1 file:line discipline

This is the single biggest integration enabler the corpus surfaces. The recommendation is strong:

- Every finding's "Problematic passage" entry includes `path:line` anchors (e.g., `01-aad-core/src/def-mismatch-signal.md:33`).
- "Counterevidence" and "Why it still stands" entries include `path:line` for the strongest mitigating passage(s).
- When a finding implicates multiple segments, list each with `path:line`.
- Tables with `file | line | issue` columns (per the link-and-file-hygiene exemplar) are encouraged for findings affecting many sites.

The justification: the integrator's first action on receiving a finding is to read the segment text. An anchor saves 30 seconds per finding × 50+ findings per cycle = ~25 minutes of integrator time that compounds across cycles. Codex auditors do this religiously, Claude auditors usually do it when disciplined, Gemini auditors often skip it — and the audits that skip it consistently take longer to integrate.

### 3.5 Hypothesis-tier observations and "what holds"

The corpus uses two complementary forms of bigger-picture content:

- **Hypothesis-tier observations** (584721 §D, 738192's "Other Observations", opus-audit-2026-04-21's "What I'd recommend", audit-2026-04-24-fresh-pass §B): things worth surfacing that don't fit the burden-of-proof finding form — generative observations, generalizations, simplifications, cross-domain connections. Mark each as `**Hypothesis.**` per `doc/de-novo-audit-instructions.md` §6.1 Phase 3 and the epistemic ladder (§1.1).
- **"What holds" / confirmation observations** (584721 §E, audit-849201-FINAL §3 "Structural Triumphs", audit-2026-04-24-fresh-pass §J1–J10): explicit "the framework's discipline holds in X, Y, Z". This is calibration data — a reader who sees "5 findings + 'these 12 things hold'" trusts the audit differently than one who sees just 5 findings.

Both are encouraged; both should be clearly marked. Hypothesis-tier observations are tagged at the `**Hypothesis.**` level per the epistemic ladder; "what holds" observations are tagged at `**Pattern.**` or `**Tested.**` level (`Pattern` for "consistent across the segments I read at depth"; `Tested` for "I ran the math first-hand on N worked examples and they passed").

Section names: "Bigger-picture observations" and "Confirmation and what holds" work; auditors who prefer different framings (e.g., 849201's "Structural Triumphs") are fine.

### 3.6 Phase 2 triangulation: the five-tag disposition vocabulary

After the de-novo pass, every finding should be classified using the vocabulary the 742613 SUPPLEMENT introduced and which subsumes the disposition labels other auditors used inconsistently:

- **New** — no durable tracking found in `TODO.md` / `PROPOSALS.md` / `CHANGELOG.md` / `msc/`; the finding is genuinely fresh; add to `audits/pending-findings-YYYY-MM-DD.md`.
- **Known-unintegrated** — the correct idea exists somewhere (`msc/` spike, prior `pending-findings`, segment Working Notes) but the source segment under audit is still wrong; integration is the issue, not the substance.
- **Known-resolved** — the source has been fixed (commit reference if findable); the audit finding is stale; report for transparency but not for action.
- **Tooling gap** — the source is structurally OK under current tools (`bin/lint-outline` etc.) but the audit exposed a class the tools don't check; the fix is a tooling addition.
- **Scope/status mismatch** — the caveat exists in prose (Working Notes, Discussion, Epistemic Status) but not in Formal Expression / status frontmatter / theorem statement; the fix is to lift the caveat into the load-bearing layer.

Plus an explicit allowed value `Unknown — needs human routing` for cases where the auditor genuinely doesn't know.

**Phase 2 placement.** Two precedents in the corpus:

- **Inline in §C of the FINAL** (613842): each finding gets a "Diagnosis" subsection naming the disposition. Compact; works for short audits.
- **Separate `SUPPLEMENT-PHASE-2-TRIAGE.md` file** (742613): a separate file with a triage-summary table at top and per-finding notes below. Cleaner separation; works for longer audits.

The spec recommends inline for ≤5 findings and separate-file for >5 findings, but either is fine. Required: every finding has a Phase-2 disposition before integration.

**Hygiene audits** (Audit type A) skip Phase-2 triangulation; their findings are either confirmed-by-tool or non-applicable. The front-matter "Phase 2 status: Not applicable (hygiene audit)" handles this.

### 3.7 Rescinded-findings transparency

If the audit's burden-of-proof gate fired (i.e., the auditor generated candidate findings that didn't survive in-segment counterevidence), include a **`### What I am not reporting` subsection** in the Findings section with:

- Brief description of each rescinded candidate (one sentence)
- The segment text reference (path:line) that caused the rescission
- Why it didn't survive (the strongest counter-passage or the math that didn't bear out)

If the auditor generated *zero* rescinded candidates, state that explicitly: *"The burden-of-proof gate did not fire during this audit; no rescinded candidates to report. Readers may take this as a calibration signal that {explanation: e.g., the auditor's predictions were unusually well-aligned with current src; or the coverage was narrow enough that few candidate-finding moments arose}."*

The transparency principle: the surviving findings are more trustworthy when the reader can see the gate working. Without rescinded-findings transparency, the reader cannot tell whether the audit produced 5 findings because the framework has 5 issues or because the auditor wasn't looking hard.

Models in the corpus:
- 584721 §B.4 ("What I am not reporting") — best example, explicit prose
- audits-2026-04-22-evening Opus's "Findings that DID NOT survive the burden-of-proof test" table — best for concise listing
- audit-2026-04-24-fresh-pass's "Reading-mode failures" — exemplary post-mortem when the gate failed (zero findings produced; auditor missed five)
- link-and-file-hygiene-findings.md's "Historical or Provenance References That Look OK" — hygiene-grade equivalent

The link-and-file-hygiene format (a tabulated list with brief why-not-flagged notes) is integrator-friendly and recommended.

### 3.8 Coverage statement

Per `doc/de-novo-audit-instructions.md` §9, the coverage section should explicitly answer:

1. **Read first-hand** — list every segment slug, ideally grouped by component / appendix
2. **Not read first-hand** — list the slugs you didn't read (groupable)
3. **Verification not run** — what mathematical checks, citation checks, lint runs, sub-agent dispatches you skipped (and *why* — was it scope, time, or judgment?)
4. **What this means for the audit's standing** — one paragraph on the audit's defensibility scope

584721 §F is the strongest model. 742613's "Coverage completed / Coverage not completed" structure is also good.

### 3.9 Multi-file splits

Multi-file FINALs are appropriate when an audit covers ≥3 components and each component's audit is substantive enough to stand alone (more than ~5 findings or substantial bigger-picture content per component). 849201 is the only corpus example.

Naming convention: `audits/audit-NNNNNN-FINAL-{component-slug}.md` where `component-slug` is `aad-section-i`, `aad-section-ii`, `aad-section-iii`, `aad-appendix-a`, `tst`, `logogenic`, `logozoetic`. The leading `000-` prefix used in 849201's `msc/AUDIT-WORKING-849201/000-FINAL-AUDIT-REPORT-...` was working-directory archaeology and **is not required** under the post-2026-04-28 lift-out convention; the cycle-id prefix plus component slug suffices.

When splitting, **a top-level `audits/audit-NNNNNN-FINAL.md` is required** (not optional) and must contain:

- The required front matter
- A pointer table to the split files
- Cross-component findings (findings that span multiple split files)
- An integrated bigger-picture / Section D if cross-cutting observations exist

This addresses the 849201 gap (no cross-component summary across the four split files; the reader has to read all four to get the cross-component view).

### 3.10 Partial audits — minimum viable shape

Partial audits are not failures (per `doc/de-novo-audit-instructions.md` §9). The minimum viable shape:

- §3.2 front matter with `Status: Partial — honestly framed` and explicit Coverage summary
- §3.3 sections 1–2 (Scope, Findings) — required
- §3.3 section 3 (Coverage) — required, with explicit list of what was deferred and why
- §3.3 section 4 (Rescinded findings) — required, even if the rescinded list is empty
- §3.6 Phase 2 — optional for partials; if omitted, state that
- §3.5 bigger-picture — optional for partials; if omitted, state that

The 738192 audit (5KB, 2 findings, AAD §I+§II partial coverage) is a clean example of a partial that satisfies the minimum.

### 3.11 The FINAL → pending-findings → routing pipeline

The corpus shows that audits land via a pipeline:

1. **Auditor produces FINAL** in `audits/audit-NNNNNN-FINAL-YYYY-MM-DD.md`
2. **Integrator (often a separate agent) produces `audits/pending-findings-YYYY-MM-DD.md`** consolidating findings across one or more FINAL(s) with:
   - Cross-audit overlap map (when multiple FINALs)
   - Consolidated finding IDs (F-V-NN, F-NN, AF-NN style)
   - Per-finding landing path: PR/commit ref / TODO entry / PROPOSALS subsumption
   - Effort estimate
   - Strengthen-vs-soften posture flag
3. **Tracking files updated** — TODO.md gets the new findings linked; PROPOSALS.md gets architectural moves; CHANGELOG.md gets cycle narrative when cycle closes; segment edits land via PR with commit refs back into pending-findings.

The §11 spec should *name* this pipeline so auditors understand where their findings will go, and so future integrators know what artifacts to produce. The auditor doesn't have to write the pending-findings doc, but the FINAL's shape (especially §3.4 per-finding schema with all 9 fields) should make the integrator's job mechanical.

### 3.12 Audit-type-specific notes

**Hygiene audits (Type A).** Skip Phase 2 triangulation; mark "Phase 2 status: Not applicable (hygiene audit)" in front matter. Use Classification headers per finding (per `link-and-file-hygiene-findings.md`). Tabulate file:line evidence for findings affecting many sites. Include a "Recommended Fix Order" section at the end. Include a "Verification Snapshot" naming exactly what tools confirmed which non-issues.

**De-novo theory audits (Type B).** Apply all of §3.2–§3.10 fully. The five 2026-04-25 AUDIT-WORKING finals are the canonical examples.

**Multi-pass batch / parallel triple (Type C).** Each individual auditor's contribution follows Type B. The wrapper document (per audits-2026-04-22-evening, extracted-audits-2026-04-22-morning) adds a cross-audit overlap section near the top, with consolidated finding IDs across audits. This is what `pending-findings-YYYY-MM-DD.md` does in the routing pipeline.

**Relayed-feedback extractions (Type D).** Outside §11's scope; these are archaeology of upstream-model output and follow whatever format the upstream model used. The wrapper convention (Context / Disposition / Verbatim) used by `extracted-*-feedback-*.md` files is independent of the audit format spec.

**Strategic portfolio reviews (Type E).** Outside §11's scope; these are not findings audits. The session output may inform pending-findings or PROPOSALS but is not itself an audit FINAL.

## 4. Migration considerations

**Don't retroactively reformat existing audits.** The five 2026-04-25 AUDIT-WORKING finals plus the older `analysis-*.md`, `audit-*.md`, and `extracted-*-feedback-*.md` documents are historical record. Reformatting would (a) waste effort on closed cycles, (b) erase the variation that documents the discipline's evolution, and (c) create false uniformity for documents that were genuine first-attempts under different conventions. v1's recommendation on this stands.

**Pilot then sweep, per the established project pattern.** The next 1–2 audits should follow §3 fully and surface gaps in the spec. The candidate-extraction discipline (§3.4 fields 6–9 plus §3.6 Phase-2 vocabulary plus §3.11 pipeline awareness) is the highest-leverage portion to pilot first; the remaining sections (file:line discipline, rescinded-findings transparency, coverage statement, audit-type tag) should follow naturally once auditors see the integrator-side benefit.

**Keep the pending-findings format documented separately.** The pending-findings docs use a sister format that should also be specified — but in a separate spec, since auditors don't write pending-findings, integrators do. A future `doc/pending-findings-format.md` would name: front matter (cycle date, source audits, read-alongside pointers); cross-audit overlap map structure; per-finding entry schema; resolution-status update conventions. **This is out of scope for §11 of `doc/de-novo-audit-instructions.md`**, but worth flagging as a parallel companion.

## 5. Worked examples

The corpus has clear exemplars for different scales / types. The spec should reference these:

| Spec property | Strongest exemplar |
|---|---|
| Required front matter (§3.2) | `audit-584721-FINAL-2026-04-25.md` lines 1–7 |
| Per-finding schema (§3.4) with full nine fields | `audit-742613-FINAL-2026-04-25.md` Findings 1–8 (closest in corpus); `link-and-file-hygiene-findings.md` Findings 1–10 (closest by integrator-friendly properties) |
| file:line discipline (§3.4.1) | `link-and-file-hygiene-findings.md` (tabulated); every Codex finding in `extracted-codex-feedback-*` (inline) |
| Hypothesis-tier observations (§3.5) | `audit-584721-FINAL-2026-04-25.md` §D.1–D.8 (uses `**Hypothesis.**` prefix consistently); `audit-2026-04-24-fresh-pass.md` §B1–B6 |
| "What holds" / confirmation (§3.5) | `audit-584721-FINAL-2026-04-25.md` §E.1–E.7; `audit-849201-FINAL-LOGOGENIC.md` §3 |
| Phase 2 triangulation inline (§3.6) | `audit-613842-FINAL-2026-04-25.md` "Integration-debt diagnosis via msc/" section |
| Phase 2 separate file (§3.6) | `audit-742613-SUPPLEMENT-PHASE-2-TRIAGE.md` (canonical) |
| Rescinded findings (§3.7) | `audit-584721-FINAL-2026-04-25.md` §B.4; `audits-2026-04-22-evening.md` Opus's "Findings that DID NOT survive" table; `audit-2026-04-24-fresh-pass.md` "Reading-mode failures" post-mortem (different shape: gate-failure debugging, not gate-success transparency) |
| Coverage statement (§3.8) | `audit-584721-FINAL-2026-04-25.md` §F; `audit-742613-FINAL-2026-04-25.md` "Coverage completed / Coverage not completed" |
| Multi-file split (§3.9) | `audit-849201-FINAL.md` + `-SEC-III.md` + `-TST.md` + `-LOGOGENIC.md` (precedent, with the gap that the spec fixes via required coordinator) |
| Partial-audit minimum (§3.10) | `audit-738192-FINAL.md` (Gemini, 5KB, 2 findings) |
| Pending-findings consumer artifact (§3.11) | `audits/pending-findings-2026-04-25.md` (consolidates 8+ findings across three audits with overlap map) |
| Hygiene-audit shape (§3.12 Type A) | `audits/link-and-file-hygiene-findings.md` (canonical) |

## 6. Open questions / judgment calls for Joseph

1. **The five-tag Phase 2 vocabulary (§3.6).** V1 raised this as "lift now or pilot once more". The broader corpus changes the picture: the underlying distinctions (new / known-unintegrated / known-resolved / tooling gap / scope-status mismatch) are *real* and the auditors converged on similar concepts under inconsistent labels. Lifting now is the right move — the labels exist organically; we're picking the cleanest authored form (Codex's, in 742613 SUPPLEMENT) and standardizing.

2. **The "Audit type" front-matter tag (§3.2).** New addition not in v1. The corpus contains five distinct audit types (§2.6) and the spec applies differently to each. Tagging in front matter is a small ask that saves the integrator real triage time. Reasonable to disagree if you think the spec should focus only on Type B and let the others remain implicit.

3. **file:line as required vs strongly recommended (§3.4.1).** V1 didn't address this; the broader corpus shows it's the single biggest integration enabler. I've recommended "strong requirement" but the spec's voice is advisory not directive — so it should read as "strongly recommended, with explicit caveats when omitted (e.g., 'I read these segments under §4.4 cadence and didn't capture line numbers; the integrator will need to reconstruct them')". Reasonable alternative: required-with-no-exceptions, since the cost of adding line numbers during the audit is much smaller than the integrator's cost of looking them up later.

4. **Required vs recommended (§3.3).** The spec distinguishes "required" (Scope/Findings/Coverage/Rescinded) from "required-or-explicit-omission" (Phase 2/Bigger-picture/What holds/Process feedback). Reasonable alternative: keep all four as "required" and let "Not applicable, because [reason]" be the standard explicit-omission form. The latter is cleaner; the former gives more auditor judgment.

5. **The pending-findings format (§3.11).** I've treated this as named-in-spec-but-out-of-scope (a parallel `doc/pending-findings-format.md` would handle it). Reasonable alternative: include a brief §3.11 sub-section naming the pending-findings shape (front matter / overlap map / per-finding entries / resolution updates) so the spec is self-contained. The downside is §11 grows; the upside is no orphaned half-spec.

6. **Hygiene audits as Type A (§3.12).** The spec treats hygiene audits as similar enough to de-novo theory audits that the same conventions apply with slight modifications. Reasonable alternative: hygiene audits are different enough (no Phase 2, tool-driven, no segment reading) that they deserve their own spec entirely. I lean toward keeping them in §11 because the convergent properties (file:line, classification headers, rescinded-findings transparency, fix-order recommendations) are the same — but reasonable to disagree.

7. **Strategic portfolio reviews and meta-audit transcripts (Type E and the lineage transcript).** I've explicitly excluded these from §11. Reasonable alternative: include a brief note acknowledging the format and pointing to where it should live (PROPOSALS-portfolio-review.md? SESSION-NOTES.md?). The corpus has at least four portfolio-review sessions (`extracted-claude-feedback-2026-04-22-25-portfolio-reviews.md`) and one substantial lineage transcript (`extracted-claude-session-6da0db68-...`) that are valuable artifacts but don't follow audit conventions. Joseph may want a separate companion spec for these.

8. **Confidence vocabulary harmonization (§3.4 step 4).** I've recommended `high|medium|low` with a one-clause reason. Gemini deviates ("Firm", "100%"); reasonable alternative is to allow any vocabulary as long as it maps cleanly to high/medium/low when consumed by the cross-audit overlap aggregator. The spec's voice is advisory so this is naturally soft, but worth explicit acknowledgment.

---

**Key files referenced (v2):**

Primary exemplars:
- `audits/link-and-file-hygiene-findings.md` (the integrator-friendly exemplar; closest single model for the §11 spec to encode)
- `audits/audit-584721-FINAL-2026-04-25.md` (strongest worked example for §3.2–§3.5, §3.7, §3.8 patterns)
- `audits/audit-742613-FINAL-2026-04-25.md` + `audit-742613-SUPPLEMENT-PHASE-2-TRIAGE.md` (densest per-finding schema; canonical Phase-2 separation; canonical disposition vocabulary)
- `audits/audit-final-reports-candidate-extraction-2026-04-25.md` (consumer-side aggregator; AF-NN naming pattern; effort/strengthen-soften fields)
- `audits/pending-findings-2026-04-22.md` / `2026-04-23.md` / `2026-04-25.md` (pending-findings format precedents — sister spec to §11)
- `audits/audits-2026-04-22-evening.md` (multi-pass batch with rescinded-findings preservation discipline; Opus's "Findings that DID NOT survive" table is the canonical rescinded-findings format)

Secondary exemplars:
- `audits/audit-613842-FINAL-2026-04-25.md` (substantial worked example with inline Phase-2)
- `audits/audit-738192-FINAL.md` (partial-audit minimum-viable example)
- `audits/audit-849201-FINAL.md` and split files (multi-file split precedent and its weaknesses)
- `audits/opus-audit-2026-04-21.md` (single-auditor extended; pre-AUDIT-WORKING but burden-of-proof discipline applied)
- `audits/audit-2026-04-24-fresh-pass.md` (the failure-and-recovery instance; "Reading-mode failures" is an exemplary post-mortem)

Archaeology / corpus extension:
- All `audits/extracted-codex-feedback-*.md` files (Codex's file:line discipline; relayed-feedback wrapper format)
- All `audits/extracted-claude-feedback-*.md` files (Claude variants; portfolio-review pattern in `-22-25-portfolio-reviews.md`)
- `audits/extracted-gemini-feedback-2026-04-26-27.md` (Gemini's schema-feedback contribution; novelty-defense framing)
- `audits/extracted-claude-session-6da0db68-2026-04-24-audit-instructions-lineage.md` (the failure-and-recovery transcript that produced `doc/de-novo-audit-instructions.md`; explicitly NOT a model for §11 format but the document it's protecting against)

Older lineage:
- `audits/2026-03-13-feedback.md`, `audits/2026-03-14-fresh-eyes-assessment.md` (pre-burden-of-proof discipline; looser prose-shaped reviews; useful as evidence for the discipline's evolution)
- `audits/analysis-2026-04-01.md`, `analysis-2026-04-02-comprehensive.md`, `analysis-2026-04-02-round2.md`, `analysis-2026-04-02-synthesis.md`, `analysis-2026-04-06.md` (transitional ACT-era; file:line emerging; "still real / already caveated" emerging)

Target file (do not modify):
- `doc/de-novo-audit-instructions.md` (target file for the eventual §11 incorporation; awaiting Joseph's decisions on §6 open questions)
