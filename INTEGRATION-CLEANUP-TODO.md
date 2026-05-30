# INTEGRATION-CLEANUP-TODO.md

*Special-project carrying-list for the pre-publication integration-and-cleanup pass. Written 2026-05-19→20 at session-end, hand-off to the next agent and to Joseph.*

## What this is and why it exists

This document captures the state of a substantial **integration-failure recovery** that this session surfaced, named, and partly held. The recovery is needed because the spike-recovery role (which this session occupied) exists *specifically* to thoroughly check each spike → integrate (land the knowledge self-contained in canon) → route the artifact to a terminal home — and at least one substantial cohort (the 2026-05-12 bulk-64) was bulk-moved without per-spike verification, that skip was documented as policy attributed to Joseph (who says he was not informed of the unchecked move), and the documented policy in turn underpinned a "*need* vs *mention*" rationalization that this session inherited, defended, and *reinforced* into the governing SOP/README/memory before Joseph caught it and rejected the distinction at root.

This is not theoretical. As of 2026-05-19 verification, ~44 segment-level canon references in `*/src/*.md` point at local process artifacts (spike/audit/`msc/`/tracker files), several in `result-`tier segments and `## Findings` (the external-facing catalog), with ~10 of those in the sim/empirical class pointing at `spikes/track-b-nonlinear-sims/`, `spikes/sim-*.py`, or the `empirical-discontinuity/` toolkit. A further class of un-integrated empirical work (`02-tst-core/simulations/` — 11 `.py` files parked in the component tree, 2026-03-20) sits *outside* the spike-recovery discipline entirely.

## How to read this (peer-status, not binding policy)

The agent writing this (Claude Opus 4.7, 2026-05-19→20 session) is, by Joseph's own correction in this session, *the* agent who demonstrated the failure pattern under critique — inherited a predecessor's rationalization (`need vs mention`) from the SOP, defended it, and sharpened it deeper into `spike-routing.md` / `spikes/README.md` / the project memory before Joseph rejected the distinction at root. The corrected principle stated below has this agent's fingerprints on its current SOP-encoding. **Joseph has not ratified the final wording.** Treat this document the way the writing agent should have treated the predecessor SOPs: as a peer-status report and a faithful trail of what was found and what was held, *not* as binding governance.

The first item of work, before any other action, is `D-1` below: Joseph's explicit confirmation of the corrected principle's final wording. Until that confirms, governing-doc surgery (CLAUDE.md, spike-routing.md, README, project memory) is held.

## The corrected principle (as currently stated; pending Joseph's ratification)

1. **Spike etymology, not metaphor.** "Spike" in this corpus carries its original XP meaning (Kent Beck / Ward Cunningham, mid-late 1990s): a *deliberately throwaway* probe whose deliverable is the knowledge, not the artifact. Spikes by convention are launchable by anyone for any reason with **no administrative friction beyond "go ahead and spike it"**. Treating the spike as something canon points back to is using the word against its meaning.
2. **The canon boundary is binary.** Working Notes are by definition **not canon** — a free working attachment to the segment ("anything we want, attached to a segment"); that is where a spike/process breadcrumb may live, freely. **Everything else in a segment is canon.** Which fields/sections exist and which count as canon is **`FORMAT.md`'s + the build pipeline's** authority, not the spike-discipline doc's to enumerate (narrative and other segment types are canon too).
3. **Canon may reference exactly two things:** the published external world (citations to peer-reviewed papers, books, archived datasets, archival DOIs/supplements) and **itself** (other canon: segments via `#slug`, `NOTATION.md`, `LEXICON.md` — all of which travel with the published Theory). Nothing else.
4. **Canon → internal-artifact ref = integration failure, by definition.** No "needed vs mentioned" spectrum; that distinction was a rationalization, not a discipline, and is to be excised wherever it appears. Each such reference is one of two things:
   - Load-bearing → the content must **be** canon (an appendix or discussion segment carrying it self-contained); the reference is papering over the integration that never happened.
   - Vanity → delete the reference; git history holds provenance, and FINDINGS/CHANGELOG hold the narrative.
   There is no third bucket.
5. **Spike-class generalizes beyond markdown derivations.** Simulation spikes, empirical-data-processing pipelines, experiments, benchmarks, draft prose — all *spike-class*. Same integration duty: the *knowledge* (what was simulated/measured/argued, parameters, regime, outcome, epistemic tier) lands **self-contained in canon**, such that a refereed reader with zero repository access can see the claim and judge it; the *reproducibility artifact*, at publication, becomes an **external archival citable object** (released code at a tag, DOI, supplement) cited the way the Theory cites any external work — **never** a local working path (`spikes/...`, `02-tst-core/simulations/...`, `empirical-discontinuity/...`). A segment whose *subject* is the empirical/validation program is legitimate canon; its dependency on a local path is the defect.
6. **The role's actual duty:** thoroughly *check* each spike (markdown, sim, empirical) → *integrate* (land the knowledge self-contained, with proper external citations where the claim leans on prior art) → *route* the artifact to its terminal home (`.integrated/` only when content is *first-hand-verified* present in canon; `.archived/` when there is genuinely no canon material). Bulk-move-without-checking is the abdication this role exists to prevent.

## Findings (verified first-hand 2026-05-19)

### F1. ~44 markdown canon→process-artifact references, ~25 files, two shapes

Verified by section-aware scan with extracted tokens (not grep-noise). Distribution:

- **Formal Expression: 14** — dominated by the *What Is Derived* "Source" column pattern. E.g. `01-aat-core/src/form-composition-closure.md:161`: `| (P1)-(P3) independent of (A1)-(A4) | Spike analysis (\`spikes/spike-projection-admissibility.md\` §5) — ... | Derived |`. This pattern recurs across multiple `form-*`, `result-*`, and `der-*` segments.
- **Discussion: 11**, **Epistemic Status: 12**, **Findings: 4** (the external-facing rolled-up catalog), **Current Instances: 2**, **Methodology: 1.** Examples:
  - `deriv-edge-update-natural-parameter.md:125` (Discussion): *"The scoping spike `spikes/spike-gbp1-logit-scoping.md` examined whether log-odds reparameterization (G-BP1 in `msc/architectural-proposals-2026-04-22.md`) ..."*
  - `disc-exploit-explore-deliberate.md:110` (Epistemic Status): *"**Simulation check (drifting multi-armed bandit, `spikes/sim-three-way-tradeoff.py`):** ..."*
  - `deriv-observation-ambiguity-bias-bound.md:239` (**Findings**): *"trail in `spikes/spike-bias-bound-constant-C-strengthening-2026-04-24.md`"*
  - `result-contraction-template.md:194/201/207` (**Findings** ×3, `result-`tier): all citing `spikes/spike-contraction-metric-generalization.md`.

Most are old (April-ish) and now point at spikes that have been moved into `.integrated/` — i.e., canon is already pointing readers at archived archaeology by stale paths. This is *active* staleness, not historical.

**Two are from this 2026-05-19 arc and the writing agent owns them specifically:**
- `01-aat-core/src/disc-stability-certificate.md:84` (Discussion, commit `639e7e2` "land (A3)")
- `01-aat-core/src/result-sector-persistence-template.md:110` (Discussion, commit `aabcf8e` "land (A1)")

Both cite `spikes/adjudicate-disc-m-preservation-operator.md` in canon Discussion (the adjudication is now in `.integrated/`, so the canon path is also stale). The structural claim ("two distinct operators, can't linearize across the pole") stands self-contained; the parenthetical *"(independently adjudicated …)"* is breadcrumb, not load-bearing. **Reduce-not-repoint: drop the parenthetical from Discussion (or move to Working Notes if a non-needed breadcrumb is wanted there).** Held — not patched in isolation, because per Joseph that would be the "shape of progress substituting for the work" move.

### F2. Sim/empirical class — same failure, wider gap, never under the discipline

`02-tst-core/simulations/` is real, git-tracked, **un-integrated spike work parked in the component tree itself** — 11 `.py` files (`lindy_*`, `regime_transitions`, `three_regimes`, `stochastic_*`), 2026-03-20, README added 2026-05-15 but the integration duty never discharged. Not in `spikes/`, not in `INDEX.md`, not routed, not covered by `spike-routing.md` or `spikes/README.md`. An entire class of spike-equivalent work is invisible to the discipline because it isn't markdown and doesn't live under `spikes/`.

And canon depends on local sim/empirical paths in ~10 segments including **`result-`tier**:
- `01-aat-core/src/obs-section-i-validation-simulations.md:50/82` — a *segment* whose body literally says: *"All code is in `../../spikes/track-b-nonlinear-sims/` ... Simulation results are reproducible (code in `../../spikes/track-b-nonlinear-sims/`, fixed seeds ...)."*
- `01-aat-core/src/deriv-causal-ib-exploration.md:103` (Discussion): *"**Empirical validation.** The derivation is validated in `spikes/track-b-nonlinear-sims/variants/variant_causal_ib.py` (results: `variant_causal_ib_results.md`)."*
- `01-aat-core/src/result-adversarial-exponent-regimes.md:68`, `result-per-dimension-persistence.md:132`, `obs-gated-tempo-advantage.md:53` — `result-`tier: *"Simulation code: `../../spikes/track-b-nonlinear-sims/variants/...`. Results: `..._results.md`."*
- `01-aat-core/src/deriv-causal-ib-lmi.md:163`, `example-strategy.md:405` — citing `spikes/...variant_causal_ib.py` / `spikes/sim-three-way-tradeoff.py`.
- TST side: `02-tst-core/src/der-code-quality-as-observation-infrastructure.md:134`, `der-dual-optimization.md:57/82`, `emp-changeset-size-principle.md:57`, `hyp-exponential-cognitive-load.md:48` — citing the internal `empirical-discontinuity/` toolkit (in the broader sibling tree) and TST's `simulations/`/`lit-review/` corpora.

`obs-section-i-validation-simulations` is the closest to a *legitimate* case under the corrected principle: a segment whose subject *is* the validation program. And it confirms the rule rather than breaks it — being a segment about the empirical program is fine canon; the dependency on `../../spikes/track-b-nonlinear-sims/` for the artifact is the defect.

### F3. The bulk-64 unverified cohort (2026-05-12)

`spikes/.integrated/MANIFEST-2026-05-12.md` records 64 spikes bulk-moved into `.integrated/` on 2026-05-12. The README's `> [!important]` callout (attributed *"Joseph, 2026-05-17"*) admits *"Spikes that predate this policy have not [had content verified] — before `.archived/` existed (notably the 2026-05-12 bulk move of 64 spikes), some incomplete-and-not-needed spikes may have been swept into `.integrated/`. Teasing those back out is not worth the effort and is explicitly not done. Do not re-audit `.integrated/`; verify forward."* This is mirrored in `doc/spike-routing.md` §5 ("bounded guarantee").

Joseph's stated position 2026-05-19: he was **not informed** that 64 spikes were moved unchecked. The "bounded guarantee / do not re-audit / verify forward" wording is the *predecessor's documented abdication of the role's core duty*, framed as Joseph's policy decision. This is a serious integrity problem in a governing doc and is **held — not for the writing agent to silently edit; it is Joseph-attributed and Joseph decides whether it stands, is retracted, or is revised**.

Concrete consequence for the wipe under consideration: permanently deleting `.integrated/` + `.archived/` (Joseph signalled doing so "this evening" on 2026-05-19) without first discharging the duty for the bulk-64 converts a predecessor's abdication into **irreversible loss of possibly-un-landed valid math/no-gos** — the precise harm the role and the discipline exist to prevent. Counsel given to Joseph at the time: *do not permanently wipe* until the actual check→integrate→route duty is discharged; if the directories must leave the working tree before then, the only safe form is git-history-preserving (recoverable). Held pending his decision.

### F4. Rationalizations encoded in governing docs (the structural risk)

Three locations carry inherited rationalizations of the integration failure:

- **`doc/spike-routing.md` §2-bis(2)** (the "*need* vs *mention*" test, attributed *"Joseph 2026-05-18"*: "*references in changelog are fine — as long as nothing needs to reference it*"). Joseph's 2026-05-19 position: *there is no need/mention distinction; there should be no distinction.* The test was the rationalization that let canon→spike references persist as "non-needed breadcrumbs, fine." Excise the distinction; replace with the binary (canon cites only canon and itself; WN is not canon).
- **`spikes/README.md`** — the `> [!important]` bounded-guarantee callout (mirrored from spike-routing §5), the cardinal-rule item 2 (provisionally rewritten this session to the binary, but pending principle-confirmation), and the implicit license of "non-needed breadcrumb in CHANGELOG is fine."
- **Project memory** `~/.claude/projects/.../memory/feedback_spike_references_only_in_working_notes.md` — this session updated it with the binary + the "do not over-enumerate canon fields, that is FORMAT's authority" calibration; the *need vs mention* discipline is still latent in the file's framing and should be excised end-to-end at the same time as the SOP. (Out-of-repo; the next agent should pull project memory to see the current state.)

### F5. The deepest structural cause — no citation/bibliography discipline (Relata-side analysis, 2026-05-19)

The reason `ref/Novelty_defense_and_integration.md` was sanctioned (CLAUDE.md:236) as a *source-of-truth* "for 15+ segment-level Findings" is not malice or carelessness — it was the **workaround for the fact that ASF has no formal-citation infrastructure yet**. Segments needed somewhere to point for prior-art assertions; an internal compilation was created; the compilation was elevated to source-of-truth; the practice was institutionalized in the onboarding doc and magnified ×15+. The Relata-side agent (separate session, ~/src/relata) ran a full analysis on 2026-05-19. Key findings, paraphrased:

- **Vol-1 (01-aat-core) has 144 segments and ~281 author-year-ish reference tokens** (regex-loose; order-of-magnitude hundreds). Vols 2–4 add ~70 more. FORMAT-TODO's earlier "200+" estimate was conservative.
- **9 `[Author Year]` brackets** across Vol-1; **0 `\cite{}`** anywhere in ASF. **No `.bib`, no `entries/` tree, no `bin/refs`-style tool.** The build-pipeline carries the lone marker comment `% kaobiblio loaded once we wire biblatex (task 7)` at `mono/kaobook/main.tex:31`. *Citation infrastructure does not yet exist.*
- **`ref/` is 50 PDFs in a half-done renaming pass** (27 bibkey-shaped filenames, 23 publisher-raw) + 13 `.md` notes + a stray `.tex/.sty/.bbl/.bst` (someone started a biblatex bring-up and stopped).
- **The dominant Vol-1 form is scholarly inline prose, not `[Author Year]` brackets** — e.g. *"The do(·) operator is Pearl's standard intervention notation (Pearl 2009, Causality, 2nd ed., Cambridge; Bareinboim, Correa, Ibeling & Icard 2022)."* This is qualitatively different from sibling projects (NeurIPS, Synthese, embeddings) where `[Author Year]` dominated and a regex sweep migrated them. **A mechanical regex→`\cite{}` conversion would catch ~9 of ~281 Vol-1 references and homogenize the monograph voice.** That is voice/style territory — Joseph's authoring decision, not a tooling sweep.
- **Foundational ASF authors are not yet in Relata** (relata has 355 entries; Sutton & Barto, Koller, Bishop, Da Costa, Hafez each: **0**). Sibling-project workstreams populated relata; ASF's foundational bibliography has not been ported.

Boundary the Relata agent named clearly:

- **Squarely relata-side (ready/easy):** CLI/storage/ingest/calibration (already surpassed); bulk-import a starter ASF `.bib` (`import <file.bib>` verb); a helper script to register the 27 bibkey-shaped `ref/` PDFs via the existing `Relata::PdfRegistration` pipeline; DOI/title-extraction heuristics for the 23 publisher-raw PDFs.
- **Squarely ASF-side (not relata's to decide):** the citation-discipline question (prose-embedded vs `\cite{}`, voice/style call); whether/how to migrate ~270 prose references; bibkey-rename + identification of the 23 publisher-raw PDFs (only ASF agents know what those papers are); `bin/build-monograph` integration (the `main.tex:31` marker is the seam, small task once a bib exists).
- **Joint:** round-trip pass — ASF agent identifies a PDF + asserts citation; relata ingests via `relata pdf` + creates entry; relata's pipeline owns the metadata/verification trail going forward.

Relata-agent recommendation explicitly states what *not* to do: any rewrite of ASF segments to convert prose references to `\cite{}` automatically. That is voice/discipline territory, ASF-agent-with-Joseph work, not relata-tooling work. Homogenization risk on monograph voice is real.

### F6. CLAUDE.md as unreviewed amplifier (structural risk class)

Joseph's 2026-05-19 observation: *"I never even look at CLAUDE.md and that's where a lot of early minor decisions can magnify into large errors."* CLAUDE.md is the auto-loaded project-onboarding doc; every agent loads it; every agent treats it as authoritative; Joseph does not routinely review it. A predecessor's exception there *silently overrides* a correct principle stated elsewhere in the same corpus, and self-amplifies across every future session. First-hand audit (2026-05-19) found:

- **Hard, institutionalized defect: `CLAUDE.md:236`** — File-Organization: *"`ref/` — Reference papers ... internally-generated reference documents that **segments cite as source-of-truth** (`Novelty_defense_and_integration.md` — prior-art search source for **15+ segment-level Findings**; `agentic-tft/` subdir)."* **This internally contradicts `CLAUDE.md:165`** (Prior-art-integration), which already states the correct rule: *"adopt the concept as a Definition/Formulation, cite the source, ... Integration belongs in the Discussion sections of relevant segments, not in separate comparison documents."* The corpus already knew the right rule; a predecessor wrote an exception into the file-org list that overrode it unread. **Joseph confirmed 2026-05-19: not appropriate; to be excised.**
- **Adjacent, milder: `CLAUDE.md:28`** — the forward-reference convention to `msc/modularity-cycle-plan-2026-05-09.md` for the unlanded `#disc-modularity-state-dynamics` (the missing-segment / forward-ref pattern). Lower severity; review when actioning.
- **Not defects:** `:51` "single source of truth" is about `bin/align-slug`'s `TYPE_TO_PREFIX` (build tooling — correct); other matches were false positives.

The structural lesson is bigger than the one line: **the auto-loaded onboarding/governing docs (CLAUDE.md foremost, then the SOPs and the README) are the maximal-blast-radius / minimal-human-oversight surface. They must be held to the *strictest* canon-cites-only-canon / honest-about-uncertainty / no-inherited-rationalization standard, reflexively, and reviewed at a human-visible cadence — or made derivable/auditable the way `LEXICON.md` and `README.md` are now generated rather than hand-asserted.** The fix cannot rest on agent virtue: the next agent will inherit the exception as gospel, exactly as this session's agent did.

## Held decisions (Joseph's, not the next agent's to make)

These are the gates. Until they resolve, large governing-doc edits and any recoverability-destroying actions are held.

- **D-1. Final wording of the corrected principle. — RATIFIED 2026-05-30 (Joseph).** The six-point principle stands, with two refinements to fold into the principle text during G1: **(R1)** Point 4's "two buckets / no third bucket" governs *canon* references only — demoting a breadcrumb into Working Notes is not a third bucket but *ceasing to be a canon reference at all* (WN is not canon, per Point 2); this closes the seam the doc trips over at F1 line 48. **(R2)** Working Notes are *intermediate* working notes and license whatever we want freely, but they are excluded from the monograph when built with the `--public` flag (verify the flag's actual build behavior before encoding the claim as fact). *Original gate, now discharged:* the writing agent had mis-encoded this area twice this session (over-enumeration, corrected; `need vs mention`, rejected at root), so explicit ratification before a third governing-doc rewrite was owed; it is now given.
- **D-2. Wipe of `.integrated/` + `.archived/`** (Joseph signalled "this evening" 2026-05-19). Three coupled questions:
  - *Semantics:* `rm`+commit (git-recoverable) vs history-purge (irreversible)?
  - *Timing:* defer until the role's actual duty is discharged for the referenced + bulk-64 spikes (recommended), or proceed and accept any unlanded archaeology as conscious irreversible let-go?
  - *Scope:* `.integrated/` + `.archived/` only? Also `02-tst-core/simulations/`? `spikes/track-b-nonlinear-sims/`? `ref/` (after the discipline lands)?
- **D-3. The predecessor abdication and its Joseph-attributed encoding. — RESOLVED 2026-05-30 = revise.** Both `spikes/README.md` and `doc/spike-routing.md` §5 rewritten from the *"not worth the effort / do not re-audit `.integrated/`"* abdication to honest **un-discharged integration debt**: the false 2026-05-17 attribution was dropped, the legitimate forward/per-cycle guarantee retained, and the bulk-64 now reads as debt that **must be verified — or consciously set down — before any wipe**, which pre-frames D-2. *Original question (now answered):* The README's `> [!important]` bounded-guarantee callout and the `spike-routing.md` §5 mirror carried the documented abdication framed as Joseph's policy; Joseph chose *revise* (not retract — the unverified-status fact is preserved; not stand — the abdication + false attribution are gone).

## The work (the TODO proper, grouped)

### G1. Truthify the governing/onboarding docs (gated on D-1, partly on D-3)

- [x] **`CLAUDE.md` ref/ line (was `:236`, now `:285`) — DONE 2026-05-30.** Excised the `ref/Novelty_defense_and_integration.md` "segments cite as source-of-truth" sanction; line now states present truth only (scaffolds are working aids, not source-of-truth; canon cites external sources directly per *Prior art integration*), with the residual-Findings reconciliation pointing here to G2/G3. (Incidental: fixed two pre-existing bare-Greek lint failures in the same file — item 6's glyph list and the embeddings `$\rho$` line.) **Joseph-confirmed defect, 2026-05-19; ratified + executed under D-1.**
- [ ] **`CLAUDE.md`** — full audit pass for other "minor decisions" of the same class (this session checked the obvious defect-shapes; the structural risk says periodic review is needed regardless).
- [x] **`doc/spike-routing.md` §2-bis(2) — already discharged (found 2026-05-30; done by Joseph 2026-05-19, not this writeup).** The §2-bis "Grounding (Joseph 2026-05-19, de-conflates this)" note already excises the rationalization the right way: the *need* test is reframed as the spike-**archivability** test (can the spike move without canon breaking), explicitly *not* the canon boundary, which is stated as the binary (WN is by-definition-not-canon; everything else is canon and cites only canon; FORMAT owns which sections are canon). This is the R1 reconciliation already present in canon. The 2026-05-19→20 writeup predated or missed this edit — a gem-hunt-style drift: the tracker said "excise," current truth said "already grounded, better." Nothing to do; do **not** re-excise (would revert Joseph's grounding).
- [x] **`doc/spike-routing.md` §5 — DONE 2026-05-30 (D-3 revise).** Bounded-guarantee rewritten per D-3 above. *Refinement 10* is a separate `spikes/PROPOSED.md` navigator scar (line ~601), unrelated to the bounded guarantee — left untouched.
- [~] **`spikes/README.md` — bounded-guarantee callout DONE 2026-05-30 (D-3 revise).** Still open: (a) confirm the cardinal-rule wording is final now that D-1 is ratified (it currently reads as clean binary — likely a no-op); (b) **R2** — note in the WN clause that Working Notes are intermediate and stripped by `bin/build-monograph --public` (verified behavior); (c) ensure sim/empirical/experiment are *explicitly* named as spike-class (G4 overlap).
- [ ] **Project memory** `feedback_spike_references_only_in_working_notes.md` (out-of-repo, `~/.claude/projects/.../memory/`) — final pass to match the ratified principle; this session's update has the binary + defer-to-FORMAT but still carries some of the *need vs mention* framing latent.

### G2. Discharge the role's actual integration duty

Per the principle: each canon→artifact reference is a triage — land or delete; each un-integrated spike (markdown or sim/empirical) needs check→integrate→route.

- [ ] **The ~44 markdown canon refs** (F1). Per-segment triage. Land the content as appendix/discussion segment(s) where it is load-bearing; delete the reference where it is vanity. The ~3 in `## Findings` are the most external-visible (they roll to `FINDINGS.md`) and the highest-priority subset.
- [ ] **The two this-arc Discussion refs** (F1 inner): `disc-stability-certificate:84` + `result-sector-persistence-template:110`. Clean reduce — drop the `(independently adjudicated ...)` parenthetical. The writing agent held this rather than patch in isolation (would have been the "shape of progress" failure); the next agent can do it in the larger pass, not as a standalone "win."
- [ ] **The ~10 sim/empirical canon refs** (F2). Per-segment triage. `obs-section-i-validation-simulations` rewrites toward self-contained statement + (at publication) external-citable artifact reference. `result-*` and `der-*` segments depending on `track-b-nonlinear-sims/` variants likewise.
- [ ] **`02-tst-core/simulations/`** (F2) — the 11 parked `.py` files. Per-file: what does it claim? Is the claim in canon self-contained? Where does the artifact end up? (For the published Theory: cited externally as an archival code release / supplement; for the working repo: cleaned to a terminal home.)
- [ ] **`spikes/track-b-nonlinear-sims/`** (F2) — same treatment; this corpus is *live* in `spikes/` and would not be touched by a `.integrated/` wipe, but the canon dependencies on it must still be resolved.
- [ ] **`empirical-discontinuity/` toolkit dependencies** in TST segments (F2) — same.
- [ ] **The bulk-64 (F3)** — per-spike check that load-bearing content is in canon. The role's actual duty for that cohort, never discharged. Expensive; cannot be done in one evening. Joseph's D-2/D-3 calls determine whether this happens or whether the cohort is consciously let go.

### G3. Build the citation/bibliography discipline (the deep fix — Relata partnership)

This is the structural reason `ref/Novelty…` was sanctioned. Until ASF has formal-citation infrastructure, prior-art assertions in segments will continue to find ad-hoc internal homes.

- [ ] **D-citation. Joseph's authoring/voice decision:** prose-embedded scholarly citations (current Vol-1 form) versus `\cite{}` discipline. Per Relata-agent's caution: a mechanical `[Author Year]`→`\cite{}` regex sweep would migrate only ~9 of ~281 Vol-1 references and homogenize monograph voice for the other ~270 (which are embedded in scholarly prose with mid-sentence italicized titles, editions, em-dash author lists). This is voice/style territory and must be Joseph's call.
- [ ] If `\cite{}`: wire `biblatex` via `mono/kaobook/main.tex:31` marker (the existing `% kaobiblio loaded once we wire biblatex (task 7)` seam); same for `scrbook`. ASF-side wiring once a `.bib` exists.
- [ ] Build the ASF-side `.bib` / `entries/` / `bin/refs` discipline. Currently 0 of these exist; sibling projects (NeurIPS, Synthese, embeddings) have working analogues — port the conventions.
- [ ] **Relata-side offers (paraphrased from the Relata agent's analysis, ranked, ~1 hr each, scoped):**
  1. `script/asf-ref-import.rb` — walk ASF's `ref/`, register the 27 bibkey-shaped PDFs via the existing `Relata::PdfRegistration` pipeline (creates entries from PDF metadata where absent; flags the 23 publisher-raw ones for ASF-side identification). Pure relata-side; gives ASF agents a head-start with relata-tracked entries to point `\cite{}` at when the discipline lands.
  2. Light spike: `extract-prose-refs <segment-dir>` — pull "Author (Year)" + nearby italics/em-dashes from Vol-1 segments into a candidate-list with relata-entry-match attempts. Observational only; lets Joseph and ASF agents *see* what an automated migration would and would not catch before committing to a discipline.
  3. Add the missing foundational entries to Relata (Sutton & Barto, Koller, Bishop, Da Costa, Hafez — currently 0 each in relata's 355). Needed regardless of which discipline ASF picks. Citation facts are in `ref/` already.
  4. The Relata agent explicitly recommends **NOT** doing any rewrite of ASF segments to convert prose references to `\cite{}` from the Relata side; that's voice/discipline territory, ASF-agent-with-Joseph work.
- [ ] ASF-side identification of the 23 publisher-raw `ref/` PDFs (only ASF agents know what those papers are; relata can surface DOI/title candidates via `Fingerprint.extract`, but the identification call is ASF's).
- [ ] **The ~15+ Findings that currently cite `ref/Novelty_defense_and_integration.md`** as source-of-truth (CLAUDE.md:236 magnification): converted to either real external prior-art citations or self-contained statements. This is part of G2 *and* of G3 — the discipline build is what makes the cleanup possible without leaving the Findings hanging.

### G4. Sim/empirical extension to the spike discipline (gated on D-1)

- [ ] **`doc/spike-routing.md`** — explicitly name simulation / empirical-data-processing / experiment / benchmark work as **spike-class**, with the same integration duty: knowledge self-contained in canon; reproducibility artifact externally citable at publication; artifact cleaned to terminal home. (Currently "empirical" appears only incidentally — once in the cross-repo-blocked case, once as an example dir-spike.)
- [ ] **`spikes/README.md`** — extend the spiker on-ramp to make clear "spike" includes sims/experiments, not just markdown derivations. ("Keep your stuff together" already permits a directory; the explicit naming is what's missing.)
- [ ] **`spikes/INDEX.md`** — register `02-tst-core/simulations/` and `spikes/track-b-nonlinear-sims/` as un-integrated sim corpora that the recovery role owns (currently invisible to the index).
- [ ] **OUTLINE/PRACTICA cross-check** — verify segments that legitimately *are* about empirical programs (e.g. `obs-section-i-validation-simulations`) carry the right home for the validation program in canon, with reproducibility artifacts cited as published (or marked clearly as "to be published as supplement" in Working Notes if pre-publication).

### G5. Structural risk mitigation — CLAUDE.md as unreviewed amplifier

- [ ] **Periodic human-visible audit cadence for CLAUDE.md** — exactly *because* Joseph doesn't routinely read it and every agent loads it as authoritative. A predecessor's "minor" exception there is the maximum-blast-radius bug.
- [ ] **Consider deriving/generating portions of CLAUDE.md** the way `LEXICON.md` is generated from `terminology/entries/` and `README.md` from `doc/readme/src/`. A "minor early decision" cannot hide unsourced in a generated doc the same way it can in a hand-asserted one. Architectural question for Joseph.
- [ ] **Onboarding-doc reflexive standard:** the same canon-cites-only-canon / honest-uncertainty / no-inherited-rationalization rules apply *to the onboarding doc itself*. Explicitly note that contradictions within CLAUDE.md (e.g. `:165` vs `:236` discovered this session) are §4.1-class defects to be caught and corrected with segment-level urgency.

## Session task-list state (snapshot at writeup time)

For continuity:

- **Completed and committed this session** (representative; not exhaustive):
  - `0c94216` — INDEX/ROUTING reconciliation + MANIFEST-2026-05-19 (the "INDEX WASN'T UPDATED" follow-through to Joseph's `9a3db8e`).
  - `7d04238` — practica `01-theory`-dive remainder discharged (A2/A3/A5 canon-coherence fixes; A1/B6 adjudicated; ROUTING (q)).
  - `2e50bc2` — A1 + B6 landings (strategy-DAG composition math into existing segments; compensation-channel uniqueness extracted standalone).
  - `36ce9d9` — WN reciprocal-link sweep (5 new Tier-3 rows + reciprocal links; one link-only fix on `der-adversarial-destabilization`).
  - `9684ca2` — `der-interaction-channel-classification:174` §4.1 stale-direction fix.
  - `cf13cb9` — PROPOSED 3-perspective restructure (index / ADVANCED / MISC) + reciprocal-link SOP discipline. *Contained the over-enumeration that Joseph later caught.*
  - `c8e7fe6` — completeness deflation (binding-completeness → optional repository; freshness + mutual-link bind).
  - `38c7ca5` — spikes/README inversion (spiker on-ramp first; recovery machinery second-and-optional).
  - `09b24c8` — canon↔WN boundary sharpening. *Contained a +8 hard-wrap regression AND a false "lint zero-net-debt" claim in the commit message — durability/voice-discipline failure recorded openly in `263b24c`.*
  - `263b24c` — binary refinement + honest correction of `09b24c8`'s false claim.

- **Held (the items above) blocked on D-1/D-2/D-3.**

## Notes for the next agent

1. **Read this section before anything else.** The corrected principle is provisional; Joseph hasn't ratified the final wording. Treat this document the way the writing agent *should* have treated the predecessor SOPs: not as gospel. Confirm with Joseph before editing CLAUDE.md / `spike-routing.md` / `spikes/README.md` / the project memory.
2. **Do not race to "fix 2 of 44" or any small symptomatic patch.** That is the shape-of-progress-substituting-for-the-work failure mode this session demonstrated. The real work is the per-segment triage (land or delete) across the full ~44 + sim/empirical set; do it as a scoped cycle, lint-gated, committed in honestly-scoped pieces.
3. **Lint must gate the commit, not run beside it.** This session committed at least one false "lint zero-net-debt" claim (`09b24c8`) because the lint ran in the same shell chain but the commit was not gated on it. Mechanical fix: assert lint-clean as a precondition, not a hope.
4. **The wipe** (`spikes/.integrated/` + `spikes/.archived/`) was signalled for 2026-05-19 evening. State at writeup: not known whether it proceeded. The directories may or may not exist now. **Verify first-hand** before assuming.
5. **The Relata partnership** is real, scoped, and offered. The relata-side agent has done its analysis and is willing to do small-scope work (~1 hr items 1–3 above) if ASF gives the go-ahead. Joseph's D-citation decision unblocks most of it.
6. **CLAUDE.md is the amplifier.** Whatever you encode there will be inherited as gospel by every future agent. Apply the strictest standard to that file in particular.
7. **The naming question** (AAT vs AaA vs A3 vs A³ vs other) — Joseph mentioned exploring variations 2026-05-19. Not decided. Use AAT until ratified.

---

*Writing agent's last word: this document is the truthful trail, with the writing agent's own failures named where they occurred. The principle the next agent inherits is cleaner than the SOPs currently encode it. The work is real, substantial, and not for one evening. The hardest discipline is the one that catches itself; treat this writeup the same way.*
