# INTEGRATION-CLEANUP-TODO.md

*Carrying-list for the pre-publication integration-and-cleanup pass (opened 2026-05-19→20). Pruned to the open set 2026-07-15; landed-cycle narrative lives in CHANGELOG (2026-05-30 "Canon→artifact reference integration §G2", 2026-06-02 "SOP consolidation", and the BIBLIOGRAPHY-TODO.md header for the 2026-06-05 citation-discipline decision).*

## What this is and why it exists

This document carries the remainder of a substantial **integration-failure recovery**. The spike-recovery role exists *specifically* to thoroughly check each spike → integrate (land the knowledge self-contained in canon) → route the artifact to a terminal home — and at least one substantial cohort (the 2026-05-12 bulk-64) was bulk-moved into `spikes/.integrated/` without per-spike verification. The governing-doc rationalizations that grew around that skip have been excised (D-1 ratified, D-3 revised, G1/G2 reference-cleanup executed — see CHANGELOG); what remains is the un-discharged artifact-level duty: the bulk-64 itself, the un-integrated sim/empirical corpora, and the citation-infrastructure tails.

## The corrected principle (RATIFIED 2026-05-30, Joseph — D-1)

1. **Spike etymology, not metaphor.** "Spike" in this corpus carries its original XP meaning (Kent Beck / Ward Cunningham, mid-late 1990s): a *deliberately throwaway* probe whose deliverable is the knowledge, not the artifact. Spikes by convention are launchable by anyone for any reason with **no administrative friction beyond "go ahead and spike it"**. Treating the spike as something canon points back to is using the word against its meaning.
2. **The canon boundary is binary.** Working Notes are by definition **not canon** — a free working attachment to the segment ("anything we want, attached to a segment"); that is where a spike/process breadcrumb may live, freely. **Everything else in a segment is canon.** Which fields/sections exist and which count as canon is **`FORMAT.md`'s + the build pipeline's** authority, not the spike-discipline doc's to enumerate (narrative and other segment types are canon too).
3. **Canon may reference exactly two things:** the published external world (citations to peer-reviewed papers, books, archived datasets, archival DOIs/supplements) and **itself** (other canon: segments via `#slug`, `NOTATION.md`, `LEXICON.md` — all of which travel with the published Theory). Nothing else.
4. **Canon → internal-artifact ref = integration failure, by definition.** No "needed vs mentioned" spectrum; that distinction was a rationalization, not a discipline. Each such reference is one of two things:
   - Load-bearing → the content must **be** canon (an appendix or discussion segment carrying it self-contained); the reference is papering over the integration that never happened.
   - Vanity → delete the reference; git history holds provenance, and FINDINGS/CHANGELOG hold the narrative.
   There is no third bucket. *(Ratification refinement R1: this two-bucket rule governs* canon *references only — demoting a breadcrumb into Working Notes is not a third bucket but ceasing to be a canon reference at all, since WN is not canon per Point 2.)*
5. **Spike-class generalizes beyond markdown derivations.** Simulation spikes, empirical-data-processing pipelines, experiments, benchmarks, draft prose — all *spike-class*. Same integration duty: the *knowledge* (what was simulated/measured/argued, parameters, regime, outcome, epistemic tier) lands **self-contained in canon**, such that a refereed reader with zero repository access can see the claim and judge it; the *reproducibility artifact*, at publication, becomes an **external archival citable object** (released code at a tag, DOI, supplement) cited the way the Theory cites any external work — **never** a local working path (`spikes/...`, `02-tst-core/simulations/...`, `empirical-discontinuity/...`). A segment whose *subject* is the empirical/validation program is legitimate canon; its dependency on a local path is the defect.
6. **The role's actual duty:** thoroughly *check* each spike (markdown, sim, empirical) → *integrate* (land the knowledge self-contained, with proper external citations where the claim leans on prior art) → *route* the artifact to its terminal home (`.integrated/` only when content is *first-hand-verified* present in canon; `.archived/` when there is genuinely no canon material). Bulk-move-without-checking is the abdication this role exists to prevent.

*(Ratification refinement R2: Working Notes are* intermediate *working notes and license whatever we want freely, but they are excluded from the monograph when built with the `--public` flag — verify the flag's actual build behavior before encoding the claim as fact.)*

## Working-Note discipline — open remainders

The authoritative "What earns a Working Note" statement landed 2026-06-02 in [`doc/sop/format.sop.md`](doc/sop/format.sop.md) §"What earns a Working Note" (CHANGELOG 2026-06-02). Still open from that cycle:

- [ ] **Memory-layer narrowing (deferred to the global/memory pass).** The cross-project half of the original §6.2 decision: project `feedback_integration_is_replacement` / `feedback_spike_references_only_in_working_notes` and the global `~/.claude/` layer inherit the same narrowing there, not here.
- [ ] **Provisional thought coupled to D-2 (Joseph, hedged — hold as provisional).** *Every segment may assume its thinking-traces live in `{spikes,audits}/.integrated/`, so segments need no per-segment histories at all.* If this holds, WN backward-narration is redundant with a richer, addressable trace corpus. **Why it is "not yet":** it rests on `.integrated/` being trustworthy, which the un-discharged bulk-64 (D-2 / F3 / G2) currently undermines — `.integrated/` membership is an *unverified* record for everything moved before the per-cycle-verification policy. Until the bulk-64 is verified or consciously set down, segments cannot safely assume their traces are recoverable from `.integrated/`.
- [ ] **No process for draining WN follow-ups (gap Joseph named).** A forward-pointer WN item has no defined route from "noted in a Working Note" to "actually picked up"; it can sit indefinitely with the WN as its sole record of obligation. **Proposed (2026-05-31 coherence pass, not yet adopted):** a WN future-work item is *routed to a real tracker* (TODO / PROPOSALS / PRACTICA / the audit cycle / `spikes/PROPOSED.md`) at the time it is written, and the WN then holds a *pointer* to that tracked obligation, never the sole obligation; plus a periodic WN-hygiene pass folded into existing tracker-touches. Full proposal: [`msc/wn-discipline-coherence-pass-2026-05-31.md`](msc/wn-discipline-coherence-pass-2026-05-31.md).

## Open findings (verified first-hand 2026-05-19; canon-reference halves discharged 2026-05-30)

### F2 (remainder). Un-integrated sim/empirical corpora

The ~10 canon references to sim/empirical paths were resolved 2026-05-30 (CHANGELOG); the *corpora themselves* still lack terminal homes:

- **`02-tst-core/simulations/`** — real, git-tracked, un-integrated spike work parked in the component tree itself: 11 `.py` files (`lindy_*`, `regime_transitions`, `three_regimes`, `stochastic_*`), 2026-03-20, README added 2026-05-15 but the integration duty never discharged. Not in `spikes/`, not in `INDEX.md`, not routed, not covered by `doc/sop/spikes.sop.md` or `spikes/README.md` — an entire class of spike-equivalent work invisible to the discipline because it isn't markdown and doesn't live under `spikes/`.
- **`spikes/track-b-nonlinear-sims/`** — live in `spikes/`; canon dependencies on it were resolved 2026-05-30, but its own check→integrate→route terminal home remains open.

### F3. The bulk-64 cohort — **verify duty DISCHARGED 2026-07-16**

The per-spike verification the 2026-05-12 bulk move skipped has been executed: every one of the 64 spikes read and checked against canon segment *content* (not slug mentions), with every claimed-unlanded item independently challenged by a refute-first second agent. Result: **54 landed / 6 partially-landed / 3 superseded / 1 nothing-to-land**; 21 confirmed-unlanded items across 10 spikes (2 high-value). Durable per-spike ledger: [`spikes/.integrated/VERIFICATION-2026-07-16.md`](spikes/.integrated/VERIFICATION-2026-07-16.md). `.integrated/` membership is now a **verified** record for the bulk-64; the confirmed-unlanded items are queued in `TODO.md` §"Bulk-64 unlanded content" and are the only remaining content-loss exposure — they must land (or be consciously declined) before any wipe deletes their carrier spikes. D-2's timing question accordingly simplifies: after those ~10 spikes' items are dispositioned, a git-recoverable `rm`+commit loses nothing unverified.

### F5 (remainder). Citation/bibliography infrastructure tails

The structural cause (no formal-citation infrastructure) is being fixed: the citation discipline is decided (2026-06-05, hybrid) and the build wiring landed — **current operating tracker: [`BIBLIOGRAPHY-TODO.md`](BIBLIOGRAPHY-TODO.md)**, which supersedes the older local-`.bib` / `bin/refs` framing where they conflict. Facts still relevant to the open tails (Relata-side analysis, 2026-05-19):

- The dominant Vol-1 form is scholarly inline prose (~281 author-year-ish tokens Vol-1; ~70 more Vols 2–4), not `[Author Year]` brackets; a mechanical regex→`\cite{}` conversion would catch ~9 and homogenize the monograph voice — segment migration is an author-judgment pass, per the decided discipline.
- `ref/` is 50 PDFs in a half-done renaming pass (27 bibkey-shaped filenames, 23 publisher-raw) + 13 `.md` notes.

### F6. CLAUDE.md as unreviewed amplifier (structural risk class)

Joseph's 2026-05-19 observation: *"I never even look at CLAUDE.md and that's where a lot of early minor decisions can magnify into large errors."* CLAUDE.md is the auto-loaded project-onboarding doc; every agent loads it and treats it as authoritative; Joseph does not routinely review it. A predecessor's exception there *silently overrides* a correct principle stated elsewhere in the same corpus and self-amplifies across every future session (worked instance: the `ref/Novelty_defense_and_integration.md` source-of-truth sanction, excised 2026-05-30). The structural lesson: **the auto-loaded onboarding/governing docs (CLAUDE.md foremost, then the SOPs and the README) are the maximal-blast-radius / minimal-human-oversight surface. They must be held to the *strictest* canon-cites-only-canon / honest-about-uncertainty / no-inherited-rationalization standard, reflexively, and reviewed at a human-visible cadence — or made derivable/auditable the way `LEXICON.md` and `README.md` are generated rather than hand-asserted.** The fix cannot rest on agent virtue: the next agent will inherit the exception as gospel.

## Held decision (Joseph's, not the next agent's to make)

- **D-2. Wipe of `.integrated/` + `.archived/`** (Joseph signalled "this evening" 2026-05-19; still not executed as of 2026-07-15 — both directories present). Three coupled questions:
  - *Semantics:* `rm`+commit (git-recoverable) vs history-purge (irreversible)?
  - *Timing:* defer until the role's actual duty is discharged for the referenced + bulk-64 spikes (recommended), or proceed and accept any unlanded archaeology as conscious irreversible let-go?
  - *Scope:* `.integrated/` + `.archived/` only? Also `02-tst-core/simulations/`? `spikes/track-b-nonlinear-sims/`? `ref/` (after the discipline lands)?

## The work (open items)

### G1. Governing/onboarding docs — residual tails

- [ ] **`CLAUDE.md`** — full audit pass for other "minor decisions" of the same class as the excised `ref/` sanction (the 2026-05-19 session checked the obvious defect-shapes; the structural risk says periodic review is needed regardless).
- [ ] **`spikes/README.md`** — residual after the D-3 revise (bounded-guarantee callout done 2026-05-30): (a) confirm the cardinal-rule wording is final under the ratified principle (currently reads as clean binary — likely a no-op); (b) **R2** — note in the WN clause that Working Notes are intermediate and stripped by `bin/build-monograph --public` (verify the flag's behavior first); (c) ensure sim/empirical/experiment are *explicitly* named as spike-class (G4 overlap).
- [ ] **Project memory** `feedback_spike_references_only_in_working_notes.md` (out-of-repo, `~/.claude/projects/.../memory/`) — final pass to match the ratified principle; the 2026-05-19 update has the binary + defer-to-FORMAT but still carries some of the *need vs mention* framing latent.

### G2. Discharge the role's actual integration duty — remainder

The *reference* half of G2 (every canon→internal-artifact reference across the four volumes) was discharged 2026-05-30 (commit `9099e58`; CHANGELOG 2026-05-30). What remains is the un-integrated artifact *corpora* terminal homes and the bulk-64:

- [ ] **`02-tst-core/simulations/`** (F2) — the 11 parked `.py` files. Per-file: what does it claim? Is the claim in canon self-contained? Where does the artifact end up? (For the published Theory: cited externally as an archival code release / supplement; for the working repo: cleaned to a terminal home.)
- [ ] **`spikes/track-b-nonlinear-sims/`** (F2) — same treatment; the corpus's own terminal home. This corpus is *live* in `spikes/` and would not be touched by a `.integrated/` wipe.
- [ ] **The bulk-64 (F3) — verify-pass done 2026-07-16 (see F3 above); remaining: land or decline the 21 confirmed-unlanded items** (queued in `TODO.md` §"Bulk-64 unlanded content"; ledger in `spikes/.integrated/VERIFICATION-2026-07-16.md`).

### G3. Citation/bibliography discipline — remaining ASF-side tails

Discipline decided + build wiring landed 2026-06-05; **current operating tracker: [`BIBLIOGRAPHY-TODO.md`](BIBLIOGRAPHY-TODO.md)** (it supersedes anything here that conflicts). Still open:

- [ ] **Relata-side offers (paraphrased from the Relata agent's 2026-05-19 analysis, ranked, ~1 hr each, scoped):**
  1. `script/asf-ref-import.rb` — walk ASF's `ref/`, register the 27 bibkey-shaped PDFs via the existing `Relata::PdfRegistration` pipeline (creates entries from PDF metadata where absent; flags the 23 publisher-raw ones for ASF-side identification).
  2. Light spike: `extract-prose-refs <segment-dir>` — pull "Author (Year)" + nearby italics/em-dashes from Vol-1 segments into a candidate-list with relata-entry-match attempts. Observational only; lets Joseph and ASF agents *see* what an automated migration would and would not catch.
  3. Add the missing foundational entries to Relata (Sutton & Barto, Koller, Bishop, Da Costa, Hafez). Citation facts are in `ref/` already. *(Check against BIBLIOGRAPHY-TODO / relata state first — the 2026-06-04 bulk-import sweep may have covered these.)*
  4. The Relata agent explicitly recommends **NOT** doing any rewrite of ASF segments to convert prose references to `\cite{}` from the Relata side; that's voice/discipline territory, ASF-agent-with-Joseph work.
- [ ] ASF-side identification of the 23 publisher-raw `ref/` PDFs (only ASF agents know what those papers are; relata can surface DOI/title candidates via `Fingerprint.extract`, but the identification call is ASF's).
- [ ] **The ~15+ Findings that formerly cited `ref/Novelty_defense_and_integration.md`** as source-of-truth: converted to either real external prior-art citations or self-contained statements. Part of G2 *and* G3 — the discipline build is what makes the cleanup possible without leaving the Findings hanging. *(Verify current state against the 2026-05-30 G2 sweep before starting — some or all may already be discharged.)*

### G4. Sim/empirical extension to the spike discipline

- [ ] **`doc/sop/spikes.sop.md`** — explicitly name simulation / empirical-data-processing / experiment / benchmark work as **spike-class**, with the same integration duty: knowledge self-contained in canon; reproducibility artifact externally citable at publication; artifact cleaned to terminal home. (Currently "empirical" appears only incidentally — once in the cross-repo-blocked case, once as an example dir-spike.)
- [ ] **`spikes/README.md`** — extend the spiker on-ramp to make clear "spike" includes sims/experiments, not just markdown derivations. ("Keep your stuff together" already permits a directory; the explicit naming is what's missing.)
- [ ] **`spikes/INDEX.md`** — register `02-tst-core/simulations/` and `spikes/track-b-nonlinear-sims/` as un-integrated sim corpora that the recovery role owns (currently invisible to the index).
- [ ] **OUTLINE/PRACTICA cross-check** — verify segments that legitimately *are* about empirical programs (e.g. `obs-section-i-validation-simulations`) carry the right home for the validation program in canon, with reproducibility artifacts cited as published (or marked clearly as "to be published as supplement" in Working Notes if pre-publication).

### G5. Structural risk mitigation — CLAUDE.md as unreviewed amplifier

- [ ] **Periodic human-visible audit cadence for CLAUDE.md** — exactly *because* Joseph doesn't routinely read it and every agent loads it as authoritative. A predecessor's "minor" exception there is the maximum-blast-radius bug.
- [ ] **Consider deriving/generating portions of CLAUDE.md** the way `LEXICON.md` is generated from `terminology/entries/` and `README.md` from `doc/readme/src/`. A "minor early decision" cannot hide unsourced in a generated doc the same way it can in a hand-asserted one. Architectural question for Joseph.
- [ ] **Onboarding-doc reflexive standard:** the same canon-cites-only-canon / honest-uncertainty / no-inherited-rationalization rules apply *to the onboarding doc itself*. Contradictions within CLAUDE.md are §4.1-class defects to be caught and corrected with segment-level urgency.

## Notes for the next agent

1. **Do not race to small symptomatic patches.** The real work is scoped cycles (corpus triage, bulk-64 verification), lint-gated, committed in honestly-scoped pieces — not "the shape of progress substituting for the work."
2. **Lint must gate the commit, not run beside it.** Assert lint-clean as a precondition, not a hope.
3. **The wipe (D-2) has not proceeded** — `spikes/.integrated/` + `spikes/.archived/` verified present 2026-07-15. Re-verify first-hand before assuming either way.
4. **The Relata partnership** is real, scoped, and offered; the 2026-06-05 D-citation decision unblocked most of it. Check `BIBLIOGRAPHY-TODO.md` and current relata state before re-doing anything.
5. **CLAUDE.md is the amplifier.** Whatever you encode there will be inherited as gospel by every future agent. Apply the strictest standard to that file in particular.
