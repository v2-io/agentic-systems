# 08 — tracker-and-msc-hygiene — findings

*2026-07-07. Cluster: the tracker ecology + working-artifact (msc/) hygiene. Verified firsthand against git and the filesystem, not relayed from tracking files. Where I write "the doc says X vs X is true now," the gap is the point.*

---

## 0. Scope recap

Two objects: (1) the **root tracker ecology** — how PRACTICA / TODO / PROPOSALS / CHANGELOG / LOG and the *other* root trackers not in the File-Organization map actually compose and stay (or fail to stay) current; (2) **`msc/` hygiene** — census + triage of ~30 top-level files and ~6 subdirs (live vs archaeology vs should-be-`_obs`). Joseph explicitly added the msc/ cleanup.

---

## A. The full tracker set — what exists, recency, and File-Org coverage

Root-level `*.md` trackers, with last-commit date (verified via `git log -1`) and whether `doc/sop/agents.sop.md` §File-Organization names them:

| Tracker | Last commit | In File-Org map? | Role |
|---|---|---|---|
| `PRACTICA.md` | 2026-06-30 | yes (navigator, auditor-safe) | strategy DAG top levels |
| `TODO.md` | 2026-07-04 | yes (priming-heavy, auditor-hidden) | tactical items (22 `##` sections) |
| `PROPOSALS.md` | 2026-07-04 | yes (auditor-hidden) | architectural moves |
| `CHANGELOG.md` | 2026-07-03 | yes | cycle narrative (2026-04-24→); 379 KB |
| `LOG.md` | 2026-05-15 | yes | frozen pre-2026-04-24 archaeology (correctly frozen) |
| `TERMINOLOGY-TODO.md` | 2026-06-18 | yes | naming-cycle queue |
| `FORMAT-TODO.md` | 2026-06-05 | yes (via bin/ mention) | pipeline state |
| `INTEGRATION-CLEANUP-TODO.md` | 2026-06-05 | yes (banner + 2 refs) | the big cleanup |
| **`NEXT-UP.md`** | **2026-06-30** | **NO** | transient handoff — see §C |
| **`JOSEPH-TODO.md`** | 2026-06-05 | **NO** | Joseph-decision routing |
| **`TODO-big-picture.md`** | 2026-06-04 | **NO** | forcing-bound-spine correction plan |
| **`TST-IDEAS.md`** | 2026-05-21 | **NO** | 59 KB TST idea dump |
| **`HISTORICAL-CONTEXT.md`** | 2026-05-17 | **NO** | lineage narrative |
| **`BIBLIOGRAPHY-TODO.md`** | 2026-06-05 | **NO** | citation debt |
| **`CURRENT-VOL1.md`** | 2026-07-02 | **NO** | 3.0 MB monograph snapshot (see §E) |
| `README.md` / `README-auditor.md` / `FINDINGS.md` / `LEXICON.md` / `NOTATION.md` / `OUTLINE.md` | — | yes | (generated / reference; out of my slice) |

**Finding A-1 (aspirational vs de-facto gap in the File-Org map itself).** The File-Organization section of `agents.sop.md` — the map every agent loads as authoritative — is **itself an incomplete tracker of the trackers.** Seven live-or-semi-live root trackers are absent from it: `NEXT-UP`, `JOSEPH-TODO`, `TODO-big-picture`, `TST-IDEAS`, `HISTORICAL-CONTEXT`, `BIBLIOGRAPHY-TODO`, and the 3 MB `CURRENT-VOL1.md`. This is the "untracked-by-the-tracker trackers" pattern named in my brief, confirmed. A fresh agent following the map will not learn these exist. `JOSEPH-TODO.md` is the most consequential omission — it is the decision-routing file this whole review is trying to strengthen, and the governing doc doesn't point at it.

**Finding A-2 (`doc/DOMAINS.md` is fresh and semi-canonical, not stale).** My brief listed `doc/DOMAINS.md` as a candidate orphan. It is not: last commit **2026-07-03**, and it is referenced from **canon** (`01-aat-core/INTRODUCTION.md`) and from `terminology/` entries. It is a live domain-instantiation lattice. Its only defect is the same as A-1: absent from the File-Org map despite being cited by the Introduction. Reclassify from "orphan" to "load-bearing-but-unmapped."

**Finding A-3 (`doc/digests/math-core.md.liquid` — genuine orphan).** Last touched 2026-05-20, a single `.liquid` template in an otherwise-empty `doc/digests/`. It is the one build-template survivor of the abandoned `build-markdown-design.md` line (see §D-2). No live pipeline doc references it. Candidate for `_obs/` or deletion.

---

## B. The layered model — does it compose as documented? (mostly yes)

The CLAUDE.md/agents.sop.md layered mental model is **PRACTICA (areas) → TODO (items) → PROPOSALS (structural moves); CHANGELOG/LOG = history; README = human; CLAUDE.md = onboarding.**

Verified de-facto: this holds. PRACTICA's headers (`⭐Theory`, `🌟 Findings`, `Ops`, `Names & Lexicon`, `Misc`) are genuine area buckets with priority markers, and it correctly bare-links into TODO/PROPOSALS/FORMAT-TODO/TODO-big-picture rather than duplicating content. TODO is genuinely tactical (22 sections). PROPOSALS carries the SP-NN structural moves. CHANGELOG is a real dated narrative that the transient files defer to ("full narrative in CHANGELOG") — and that deference is *honored*, not just claimed: the NEXT-UP entries do point into CHANGELOG for detail. The spine is healthy.

**The one composition defect:** PRACTICA (auditor-safe, 2026-06-30) opens with a "Live handoff (transient): read NEXT-UP.md first" banner. That banner routes the reader into a file that is now stale (§C), and PRACTICA itself was last touched in the same 2026-06-30 commit (`6f5b066`) — i.e., PRACTICA has not been refreshed across the entire 07-03/07-04 arc either. The navigator's top-of-file pointer is aimed at a stale target.

---

## C. NEXT-UP.md — the transient-handoff drain discipline is broken (the headline)

`NEXT-UP.md` self-describes (line 4): *"Transient pointer, not a navigator … This file only names what is hot so a compaction or fresh session resumes momentum. **Delete once the queue drains.**"*

**Finding C-1 (stale by an entire work arc — verified).** NEXT-UP is dated/committed **2026-06-30** (`6f5b066`). Since then, `git log --since=2026-06-30` shows a dense **07-03 and 07-04 work arc** that NEXT-UP does not mention at all:
- Audit 731548 landings (B-1…B-4, mood MG-discharge) — 07-03
- The **epistemic-target-ontology spike** opened (`76ac5c4`), GA-1 asymmetry verified (`82c9bcc`) — 07-04
- **vivarium** entering as calibration laboratory (`137f8aa`) — 07-04
- The **law-stratum** decomposition (`ef656e3`, `6989bc7`) — 07-04
- The **TST 21-independent-derivations spike** (`8c50590`) — 07-04
- The **era-artifact / C5 convergence routing** addenda (`4ef5ead`, `a75c2ef`, `7c65b66`) — 07-04

This is exactly the ground the orientation letter calls "the freshest." NEXT-UP's "what is hot" section is a snapshot from *before the hottest work*. Its newest "Landed since" entry is 2026-06-17 (mood/agency-death). The file that exists to let a fresh session resume momentum would actively mislead one now.

**Finding C-2 (the drain discipline has a working precedent — so this is regression, not absence).** An *earlier* `NEXT-UP.md` lived at `spikes/NEXT-UP.md` as the strategic-composition cluster navigator. It was **retired correctly on 2026-05-25**: `git mv` to `spikes/.integrated/NEXT-UP-archived-2026-05-25.md`, a per-cycle `MANIFEST-2026-05-25-NEXT-UP.md`, residuals migrated to their proper homes (J7 → ops/papers/deferred, J9 → spikes/PROPOSED), and a full CHANGELOG narrative (2026-05-25) documenting "what replaces NEXT-UP as a navigator." That is the drain discipline executed cleanly. The capability is proven. The *current* root NEXT-UP.md is not being held to the standard its own predecessor met — the discipline exists but is not being *run* on the live instance.

**Finding C-3 (why it decays — the diagnostic).** Updating a transient handoff is unrewarded relative to doing the next real work, and *draining* it (deciding "this arc is closed, archive the pointer") requires the standing to declare a cluster done — which in practice is Joseph's. So the file rots at exactly the cadence the review names: the bandwidth bottleneck, made visible on the one artifact meant to relieve it.

---

## D. msc/ census + triage (~30 top-level files, 6 subdirs)

Method: `git log -1` recency per file + a cross-reference grep (how many tracked `.md` files outside msc/ name it, excluding this review). Reference count is a *liveness hint* but noisy — CHANGELOG/LOG mentions are legitimately archival, so `refs>0` does not mean "live," but `refs:0` is a strong orphan signal.

### D-1. Live / current working docs (keep in place)
Touched 2026-06 or 07, or high active-reference count:
- `era-artifact-asf-contributions-2026-07-04.md` (07-04, refs 3) — the C5/convergence routing hub, actively cited by the newest commits.
- `modularity-cycle-plan-2026-05-09.md` (06-11, **refs 22**) — heavily referenced, still live.
- `deaths-grounding-plan-2026-06-10.md` (06-11, refs 6), `mood-layer-sovereignty-carve-2026-06-17.md` (06-17, refs 6) — recent-cycle plans still referenced from NEXT-UP/TODO/CHANGELOG.
- `sop-consolidation-design-2026-06-01.md`, `sop-shift-completion-plan-2026-06-02.md`, `wn-discipline-coherence-pass-2026-05-31.md`, `domain-xfer-candidates.md`, `451729-d1-gate-verification-2026-05-20.md` — all touched 06-02, cited from live trackers.
- `markdown-first-pipeline.md` (refs 5) — the **live** monograph-pipeline design, named in agents.sop.md §File-Org. Keep.
- `working-composition-admissibility.md` (**refs 18**) — high reference; likely load-bearing composition spike. Keep pending cluster-01/02 judgment.

### D-2. Archaeology — completed cycles, no "done" event ever fired (candidate `_obs/`)
May-or-earlier, low live reference, cycle demonstrably closed:
- **AAT rename cluster:** `AAD-to-AAT-TODO.md`, `class-rename-execution-plan-2026-05-09.md`, `class-rename-tracking-2026-05-09.md` — the renames (AAD→AAT 05-15; GUC class renumber 05-09) are **done**; these are execution logs. High refs are historical (CHANGELOG/CLAUDE lineage notes). Archaeology.
- **three-move-shape pair** (2026-05-08 ×2) — novelty/refinement analysis; one is `refs:0`. Completed exploration.
- **audit-routing drafts** (`audit-routing-consolidated-ledger-draft-2026-05-16.md`, `audit-routing-microfix-and-manifest-draft-2026-05-16.md` — the latter `refs:0`, header says "PRE-DECISIONAL DRAFT, not applied") — superseded by the landed `doc/sop/audit.sop/routing.sop.md`. Archaeology.
- **`build-markdown-design.md`** (`refs:0`, header "design, pre-implementation") — superseded by `markdown-first-pipeline.md`; not referenced by any live pipeline doc. Its orphan template `doc/digests/math-core.md.liquid` (§A-3) is the residue. Archaeology.
- `figure-pipeline-buildout-2026-05-18.md`, `scope-of-work-ontology-and-figure-2026-05-17.md`, `handoff-2026-05-01.md`, `judgment-calls-readme-cycle-2026-04-26.md`, `role-encounter-plan.md`, `llm-causal-access-note.md`, `separability-standalone-paper-proposal.md`, `verify-sector-condition-cluster-2026-05-20.md`, `verify-strategy-cost-cluster-2026-05-20.md`, `2026-03-14-section-iv-paper-outline.md` — completed-cycle residue. (`separability-standalone-paper-proposal` has a live sibling proposal noted in MEMORY — confirm before moving; the *proposal* may still be open even if this draft is superseded.)

### D-3. Subdirectories
- **`summary-attempt/` — 194 files, last touched 2026-05-20.** A full sequential monograph-assembly attempt (000…). Superseded by the `CURRENT-VOL1.md` / markdown-first pipeline. This is the single largest archaeology mass in msc/. Strong `_obs/` candidate.
- **`reflections/` — 28 files, live/growing.** Author's-voice instance journal; entry 28 was written today (untracked). This is a *deliberately accreting* series, not archaeology. Keep. (Note: it is genuinely a different *kind* of artifact from the rest of msc/ — see D-5.)
- **`naming/` — 30 files, last 2026-06-02.** R1/R2 naming-cohort working set (master-lists, votes, handoffs, `_archive/`). Belongs to cluster-03's domain; as *hygiene*, it is a semi-closed cycle with its own internal `_archive/` — reasonably kept, but the R2 cohort close (`handoff-2026-04-30-cohort-close.md`) suggests most is archaeology.
- **`logogenic-encounter-2026-05-01/` — 10 files + INDEX, last 2026-06-11.** Has its own INDEX.md; touched recently. Semi-live encounter record. Keep pending cluster-04 judgment.
- **`domain-unification-2026-05-04/` — 1 file** (`recommended-agent-ontology.md`). The process-notes companion already lives in `_obs/2026-05-04-domain-unification-process-notes.md` — so the cycle was *partially* archived and this remnant was left behind. Finish the move.
- **`__pycache__/` — 1 stray `.pyc`** (`spike-causal-ib-sim.cpython-313.pyc`, dated 2026-04-25, untracked/gitignored). Pure build cruft from a spike sim run. Delete.

### D-4. Rough split
Of 30 top-level msc/ files, ~9 are live (D-1) and ~21 are completed-cycle archaeology (D-2). Add `summary-attempt/` (194) and most of `naming/` and the split is heavily archaeology-by-volume. **Nothing is broken or on fire** — this is undischarged closed-cycle residue, not active mess.

### D-5. `msc/` has no index or census (structural gap)
There is no `msc/README.md` or `msc/INDEX.md` (the closest match, `judgment-calls-readme-cycle-2026-04-26.md`, is about the README build cycle, not an msc index). So msc/ is an undifferentiated bag mixing three *different kinds* of artifact — live cycle plans, dead cycle residue, and the growing author-journal (`reflections/`) — with no marker of which is which. An agent cannot tell live from dead without the git-archaeology pass I just did. This is the root cause of the archaeology accumulation: no home-vs-archive convention *within* msc/, and no owner-trigger to sweep.

---

## E. `CURRENT-VOL1.md` — 3 MB tracked monograph snapshot, unmapped, provenance unclear
Root-level, 3.0 MB, tracked, last commit 2026-07-02, only referenced from CHANGELOG. No generator reference found in `bin/`, `markdown-first-pipeline.md`, or `FORMAT-TODO.md`. It reads as a hand-placed full-monograph assembly ("AAT: Adaptation & Actuation Theory"). Open question for Joseph: is this a generated build output (should it be gitignored / in a build dir, not committed at root?) or a hand-maintained canonical snapshot (should it be in the File-Org map)? Either way, a 3 MB unmapped artifact at repo root is a hygiene smell.

---

## F. The six lenses (summary)

**(a) De-facto processes actually running.** The PRACTICA→TODO→PROPOSALS→CHANGELOG spine is genuinely maintained and composes as documented. CHANGELOG is a real, dense, dated narrative. Cross-references between trackers are honored (transient files defer to CHANGELOG and do so accurately). Live msc/ cycle-plans are well-kept.

**(b) Aspirational (docs/SOPs intend).** The File-Org map in agents.sop.md is meant to be *the* map of the tracker set — but it omits 7 live/semi-live root trackers (A-1) and DOMAINS.md (A-2). NEXT-UP intends a "delete-once-drained" transient discipline (C). MEMORY's `feedback_prune_completed_from_trackers.md` intends forward-trackers to be pruned and narrative pushed to CHANGELOG — the CHANGELOG half happens; the *pruning* half is where decay concentrates.

**(c) Emergent (git history).** The 2026-05-25 `spikes/NEXT-UP` retirement (git mv + manifest + CHANGELOG) is a clean, repeatable **drain ritual** that emerged and worked once — then wasn't re-run on the current NEXT-UP (C-2). The `domain-unification` split (process-notes → `_obs/`, ontology-remnant left in msc/) shows the *partial-archive* failure mode: cycles get half-swept when the sweep is interrupted. `_obs/` (108 entries) is the established archaeology home and is used — but reached inconsistently.

**(d) Stale / broken / abandoned (concrete).** NEXT-UP stale by the 07-03/04 arc (C-1). PRACTICA's top banner points at it (B). ~21 msc/ top-level files + `summary-attempt/` (194) are undischarged archaeology (D). `doc/digests/math-core.md.liquid` orphan (A-3). `msc/__pycache__/` stray (.pyc). `domain-unification-2026-05-04/` half-archived remnant. Three `refs:0` msc drafts (D-2). `CURRENT-VOL1.md` unmapped 3 MB (E).

**(e) Blocked on Joseph.** (1) Drain-vs-refresh NEXT-UP — needs the standing to declare the 06/07 arc's clusters closed. (2) `CURRENT-VOL1.md` disposition (generated-and-gitignore vs canonical-and-map). (3) Bulk `_obs/` sweep of the ~21 archaeology files + `summary-attempt/` — an agent *can* do this mechanically, but the "is this cycle really done?" call per file is a judgment Joseph is currently the only holder of (this is the same shape as D-2 in the audit cluster). (4) Whether `separability-standalone-paper-proposal` is a closed draft or a still-open proposal.

**(f) Candidate meta-processes.** See §G.

---

## G. Candidate meta-process definitions (raw material for the MECE map)

**MP-08.1 — Tracker-currency maintenance.**
- *Trigger:* a work arc lands (commit to canon/spikes) that changes "what is hot" or closes a cluster.
- *Steps:* update PRACTICA area status → prune the closed item from its forward-tracker → push narrative to CHANGELOG → refresh (or drain) NEXT-UP.
- *Current health:* **mixed.** CHANGELOG-narrative and TODO/PROPOSALS steps run reliably; the **NEXT-UP refresh/drain step is broken** (C); PRACTICA refresh lags (B).

**MP-08.2 — Transient-handoff drain ritual.**
- *Trigger:* a transient navigator's queue empties (its cluster's work is all landed).
- *Steps:* `git mv` to `.integrated/`/`_obs/`, write a per-cycle MANIFEST, migrate residuals to permanent homes, CHANGELOG entry naming what replaces it.
- *Current health:* **proven-then-abandoned.** Executed cleanly once (`spikes/NEXT-UP` 2026-05-25); not re-run on root `NEXT-UP.md` (C-2). The ritual is documented-by-example in CHANGELOG but not lifted into an SOP, so re-running it depends on an agent rediscovering the precedent.

**MP-08.3 — msc/ working-artifact lifecycle (cycle-plan → archive).**
- *Trigger:* a working-cycle plan's cycle completes.
- *Steps:* mark the doc landed → move to `_obs/` (or leave with a "SUPERSEDED" banner) → ensure any companion notes move *together* (avoid the domain-unification half-split).
- *Current health:* **de-facto absent.** No convention, no msc/ index (D-5); archaeology accumulates because the archive step has no trigger and no owner but Joseph. `_obs/` exists and is used, but reached ad hoc.

**MP-08.4 — Governing-doc / File-Org map currency.**
- *Trigger:* a new root tracker is created, or one is retired.
- *Steps:* add/remove it from agents.sop.md §File-Organization with its role + auditor-visibility flag.
- *Current health:* **stale.** 7 trackers + DOMAINS.md live outside the map (A-1/A-2). This is the *meta*-tracker (the map of maps) drifting from ground truth — the highest-leverage single fix, because every agent loads it.

**MP-08.5 — Build-artifact placement discipline.**
- *Trigger:* a generated artifact (monograph snapshot, digest template, pyc) is produced.
- *Steps:* decide committed-canonical (→ map it) vs build-output (→ gitignore / build dir).
- *Current health:* **unsettled.** `CURRENT-VOL1.md` (3 MB, unmapped, E), the `.liquid` orphan (A-3), and the stray `.pyc` (D-3) are all instances of a generated thing landing wherever the tool left it.

---

## H. Out-of-scope surfacings (pass back)
- **JOSEPH-TODO.md efficacy (cluster 07's slice, but I touched it):** it is well-designed (short, pointer-only, explicit "only-you" convention) and *reasonably current* (2026-06-05) — but it is **absent from the File-Org map** (A-1), so the decision-routing file the review wants to strengthen is itself undiscoverable via the governing doc. Cheap, high-leverage fix.
- **DOMAINS.md is canon-cited but exploratory-tagged** ("STATUS: Working draft, exploratory" in its header) while `01-aat-core/INTRODUCTION.md` links it. A working-draft cited from canon is a tier-honesty question for the theory-content cluster (01).
- **`TODO-big-picture.md`** carries a live, unlanded doctrinal correction (W1–W4: the forcing-bound-spine / stop-deflating register work), with W1 flagged "doctrinal — flag to Joseph before landing." It is stale (2026-06-04) and priming-heavy and *not* in the File-Org map — real pending work hiding in an unmapped file. Relevant to cluster 01 (epistemic culture) and cluster 07 (Joseph-blocked).
- **`TST-IDEAS.md` (59 KB, 2026-05-21)** and **`HISTORICAL-CONTEXT.md` (2026-05-17)** are large unmapped root files that have not moved in ~7 weeks. TST-IDEAS overlaps cluster-02's "TST idea backlog"; HISTORICAL-CONTEXT overlaps the lineage narrative already in CLAUDE.md/LOG — possible redundancy to reconcile.

---

## I. Confidence
Tier: **high** on the concrete/verifiable claims (recency dates, File-Org omissions, NEXT-UP staleness, the 05-25 drain precedent, msc/ census counts — all checked firsthand against git and the filesystem). **Medium** on liveness judgments for individual msc/ files where I inferred "archaeology" from recency + reference-pattern without reading each file in full (D-2 list — the *disposition* calls are Joseph's; I verified the *signals*, not the closure). **Not verified:** whether `CURRENT-VOL1.md` is generated or hand-maintained (E, open question); whether `separability-standalone-paper-proposal` is a closed draft or open proposal (I flagged it rather than assumed).
