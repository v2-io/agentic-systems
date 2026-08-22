# INTEGRATION-CLEANUP-TODO.md

*Carrying-list for the pre-publication integration-and-cleanup pass (opened 2026-05-19→20). Remaining open set below. Landed-cycle narrative lives in CHANGELOG (2026-05-30 G2, 2026-06-02 SOP consolidation, 2026-07-16 F2/F3/D-2, and BIBLIOGRAPHY-TODO for the 2026-06-05 citation-discipline decision).*

## What this is and why it exists

This document carries the remainder of a substantial **integration-failure recovery**. The spike-recovery role exists *specifically* to thoroughly check each spike → integrate (land the knowledge self-contained in canon) → route the artifact to a terminal home. D-1 is ratified; the artifact-level duty (bulk-64 verification, sim/empirical routing, `.integrated/`/`.archived/` truth-claims) is closed — CHANGELOG 2026-07-16. What remains is citation-infrastructure tails (G3/F5), governing-doc residuals (G1/G5/F6), the sim/empirical *naming* in the spike on-ramp (G4; the `empirica/` registry itself exists), and Working-Note discipline remainders.

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

*(Ratification refinement R2: Working Notes are* intermediate *working notes and license whatever we want freely, but they are excluded from the monograph when built with the `--public` flag. **Verified 2026-08-22:** `CURRENT-VOL1.md` built `--public --split-appendices --compact-fields --emit-current 01` carries 0 Working Notes sections.)*

*(Ratification refinement R3, Joseph 2026-07-16: point 5's "never a local working path" means never an* unregistered *path. The `empirica/` registry (root-level, established 2026-07-16) travels with the Theory the way LEXICON/NOTATION do, so it is canon: `empirica:<experiment-slug>` references in segments are sanctioned canonical references, and at publication the experiment directories become the external archival objects point 5 requires — the citation form survives the transition. See `empirica/README.md` for the contract.)*

## Working-Note discipline — open remainders

The authoritative "What earns a Working Note" statement landed 2026-06-02 in [`doc/sop/format.sop.md`](doc/sop/format.sop.md) §"What earns a Working Note" (CHANGELOG 2026-06-02). Still open from that cycle:

- [ ] **Memory-layer narrowing (deferred to the global/memory pass).** The cross-project half of the original §6.2 decision: project `feedback_integration_is_replacement` / `feedback_spike_references_only_in_working_notes` and the global `~/.claude/` layer inherit the same narrowing there, not here.
- [ ] **Provisional thought (Joseph, hedged — now unblocked, awaiting his ratification).** *Every segment may assume its thinking-traces live in `{spikes,audits}/.integrated/`, so segments need no per-segment histories at all.* If this holds, WN backward-narration is redundant with a richer, addressable trace corpus. **Status 2026-07-16:** the blocker is gone — the bulk-64 is verified (ledger in `.integrated/`), the buckets re-sorted honestly, and the directories are permanent per the wipe-question resolution (CHANGELOG 2026-07-16). The principle is now *adoptable* if Joseph ratifies it; its consequence (WN backward-narration redundant with the addressable trace corpus) feeds the promotion-terminus/WN-drain decision in the valve.
- [ ] **No process for draining WN follow-ups (gap Joseph named).** A forward-pointer WN item has no defined route from "noted in a Working Note" to "actually picked up"; it can sit indefinitely with the WN as its sole record of obligation. **Proposed (2026-05-31 coherence pass, not yet adopted):** a WN future-work item is *routed to a real tracker* (TODO / PROPOSALS / PRACTICA / the audit cycle / `spikes/PROPOSED.md`) at the time it is written, and the WN then holds a *pointer* to that tracked obligation, never the sole obligation; plus a periodic WN-hygiene pass folded into existing tracker-touches. Full proposal: [`msc/wn-discipline-coherence-pass-2026-05-31.md`](msc/wn-discipline-coherence-pass-2026-05-31.md).

## Open findings (citation / amplifier class)

### F5 (remainder). Citation/bibliography infrastructure tails

The structural cause (no formal-citation infrastructure) is being fixed: the citation discipline is decided (2026-06-05, hybrid) and the build wiring landed — **current operating tracker: [`BIBLIOGRAPHY-TODO.md`](BIBLIOGRAPHY-TODO.md)**, which supersedes the older local-`.bib` / `bin/refs` framing where they conflict. Facts still relevant to the open tails (Relata-side analysis, 2026-05-19):

- The dominant Vol-1 form is scholarly inline prose (~281 author-year-ish tokens Vol-1; ~70 more Vols 2–4), not `[Author Year]` brackets; a mechanical regex→`\cite{}` conversion would catch ~9 and homogenize the monograph voice — segment migration is an author-judgment pass, per the decided discipline.
- `ref/` is 50 PDFs in a half-done renaming pass (27 bibkey-shaped filenames, 23 publisher-raw) + 13 `.md` notes.

### F6. CLAUDE.md as unreviewed amplifier (structural risk class)

Joseph's 2026-05-19 observation: *"I never even look at CLAUDE.md and that's where a lot of early minor decisions can magnify into large errors."* CLAUDE.md is the auto-loaded project-onboarding doc; every agent loads it and treats it as authoritative; Joseph does not routinely review it. A predecessor's exception there *silently overrides* a correct principle stated elsewhere in the same corpus and self-amplifies across every future session (worked instance: the `ref/Novelty_defense_and_integration.md` source-of-truth sanction, excised 2026-05-30). The structural lesson: **the auto-loaded onboarding/governing docs (CLAUDE.md foremost, then the SOPs and the README) are the maximal-blast-radius / minimal-human-oversight surface. They must be held to the *strictest* canon-cites-only-canon / honest-about-uncertainty / no-inherited-rationalization standard, reflexively, and reviewed at a human-visible cadence — or made derivable/auditable the way `LEXICON.md` and `README.md` are generated rather than hand-asserted.** The fix cannot rest on agent virtue: the next agent will inherit the exception as gospel.

## The work (open items)

### G1. Governing/onboarding docs — residual tails

- [ ] **`CLAUDE.md`** — full audit pass for other "minor decisions" of the same class as the excised `ref/` sanction (the 2026-05-19 session checked the obvious defect-shapes; the structural risk says periodic review is needed regardless).
- [ ] **`spikes/README.md`** — residual after the D-3 revise (bounded-guarantee callout done 2026-05-30; header updated 2026-07-16). Remainder: (a) confirm the cardinal-rule wording is final under the ratified principle (currently reads as clean binary — likely a no-op); (b) **R2** — the `--public` strip is now verified (2026-08-22 CURRENT-VOL1, 0 WN sections); still owed: a note in the WN clause that Working Notes are intermediate and stripped by `bin/build-monograph --public`; (c) ensure sim/empirical/experiment are *explicitly* named as spike-class (G4 overlap).
- [ ] **Project memory** `feedback_spike_references_only_in_working_notes.md` (out-of-repo, `~/.claude/projects/.../memory/`) — final pass to match the ratified principle; the 2026-05-19 update has the binary + defer-to-FORMAT but still carries some of the *need vs mention* framing latent.

### G3. Citation/bibliography discipline — remaining ASF-side tails

Discipline decided + build wiring landed 2026-06-05; **current operating tracker: [`BIBLIOGRAPHY-TODO.md`](BIBLIOGRAPHY-TODO.md)** (it supersedes anything here that conflicts). Still open:

- [ ] **Relata-side offers (paraphrased from the Relata agent's 2026-05-19 analysis, ranked, ~1 hr each, scoped):**
  1. `script/asf-ref-import.rb` — walk ASF's `ref/`, register the 27 bibkey-shaped PDFs via the existing `Relata::PdfRegistration` pipeline (creates entries from PDF metadata where absent; flags the 23 publisher-raw ones for ASF-side identification).
  2. Light spike: `extract-prose-refs <segment-dir>` — pull "Author (Year)" + nearby italics/em-dashes from Vol-1 segments into a candidate-list with relata-entry-match attempts. Observational only; lets Joseph and ASF agents *see* what an automated migration would and would not catch.
  3. Add the missing foundational entries to Relata (Sutton & Barto, Koller, Bishop, Da Costa, Hafez). Citation facts are in `ref/` already. *(Check against BIBLIOGRAPHY-TODO / relata state first — the 2026-06-04 bulk-import sweep may have covered these.)*
  4. The Relata agent explicitly recommends **NOT** doing any rewrite of ASF segments to convert prose references to `\cite{}` from the Relata side; that's voice/discipline territory, ASF-agent-with-Joseph work.
- [ ] ASF-side identification of the 23 publisher-raw `ref/` PDFs (only ASF agents know what those papers are; relata can surface DOI/title candidates via `Fingerprint.extract`, but the identification call is ASF's).
- [ ] **The Findings that still cite `ref/Novelty_defense_and_integration.md`.** Convert to either real external prior-art citations or self-contained statements. Still present 2026-08-22: 8 Search-Log hits in `FINDINGS.md` plus segment bodies (`der-directed-separation`, `der-causal-insufficiency-detection`, `deriv-causal-ib-exploration`, `deriv-causal-ib-lmi`, and four TST segments). Part of G2 *and* G3 — the discipline build is what makes the cleanup possible without leaving the Findings hanging.

### G4. Sim/empirical extension to the spike discipline

The `empirica/` registry exists (founded 2026-07-16; charter in `empirica/README.md`; track-b-nonlinear is the founding entry). Point 5 / R3 of the corrected principle already names the class. What remains is the *on-ramp wording* so a new spiker hits it:

- [ ] **`doc/sop/spikes.sop.md`** — explicitly name simulation / empirical-data-processing / experiment / benchmark work as **spike-class**, with the same integration duty: knowledge self-contained in canon; reproducibility artifact externally citable at publication; artifact cleaned to terminal home (`empirica/` when a canon segment leans on it). (Currently "empirical" appears only incidentally.)
- [ ] **`spikes/README.md`** — extend the spiker on-ramp to make clear "spike" includes sims/experiments, not just markdown derivations. ("Keep your stuff together" already permits a directory; the explicit naming is what's missing.)
- [ ] **obs-* empirical-program segments** — spot-check that they cite `empirica:<slug>` (or "to be published as supplement" in Working Notes) rather than a local working path. The F2 landing did this for the track-b consumers; this is the remainder sweep, not the founding.

### G5. Structural risk mitigation — CLAUDE.md as unreviewed amplifier

- [ ] **Periodic human-visible audit cadence for CLAUDE.md** — exactly *because* Joseph doesn't routinely read it and every agent loads it as authoritative. A predecessor's "minor" exception there is the maximum-blast-radius bug.
- [ ] **Consider deriving/generating portions of CLAUDE.md** the way `LEXICON.md` is generated from `terminology/entries/` and `README.md` from `doc/readme/src/`. A "minor early decision" cannot hide unsourced in a generated doc the same way it can in a hand-asserted one. Architectural question for Joseph.
- [ ] **Onboarding-doc reflexive standard:** the same canon-cites-only-canon / honest-uncertainty / no-inherited-rationalization rules apply *to the onboarding doc itself*. Contradictions within CLAUDE.md are §4.1-class defects to be caught and corrected with segment-level urgency.

## Notes for the next agent

1. **Do not race to small symptomatic patches.** The artifact-level recovery (F2/F3/G2) is closed; the remaining work is citation tails, onboarding-doc discipline, and the spike-on-ramp naming. Lint-gated, committed in honestly-scoped pieces.
2. **Lint must gate the commit, not run beside it.** Assert lint-clean as a precondition, not a hope.
3. **There is no wipe** — resolved 2026-07-16 (teaching hypothetical, mis-transcribed as a directive; CHANGELOG 2026-07-16). The directories are permanent. Do not resurrect the wipe from older documents that mention it as pending.
4. **The Relata partnership** is real, scoped, and offered; the 2026-06-05 D-citation decision unblocked most of it. Check `BIBLIOGRAPHY-TODO.md` and current relata state before re-doing anything.
5. **CLAUDE.md is the amplifier.** Whatever you encode there will be inherited as gospel by every future agent. Apply the strictest standard to that file in particular.
