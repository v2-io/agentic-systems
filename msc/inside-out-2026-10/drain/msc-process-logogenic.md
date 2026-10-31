# Drain: `msc/meta-process-review-2026-07-07/` and `msc/logogenic-encounter-2026-05-01/`

*Serves **I.9** of `../INTENT.md` (every backlog surface drained into the ledger, one disposition per source item). Top intent: "Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself." A fork of the `msc/` drain (its file is `msc.md` beside this one), 2026-10-30, at asf `515c15ce` and later. Written as it goes; the `msc/` drain and the lead read it whole.*

## How dispositions are written

Same as `msc.md`: **landed / superseded** (where, checked at HEAD); **canon or process defect** (ledger item, owner KR); **never reached canon** (ledger item); **set aside** (reason). The meta-process review is from 2026-07-07; most of its findings were overtaken by this effort (the ledger, vsect, the hooks, the gates Joseph lifted today), so each is checked against HEAD, not against July. Where an item already exists, my source is added with `vsect raise`.

## Coverage

All 34 files of the two directories were reached. **Read whole:** `meta-process-review-2026-07-07/` 00-INDEX, findings 01, 02, 03, 04, 05, 06, 08, 09, all ten reflections, DECISIONS-CENSUS, SESSION-LOG-2026-07-14; `logogenic-encounter-2026-05-01/` INDEX, 04, 05, 08, 09. **Read in part:** findings 07 (§0–§5 whole, §6's mechanism sketch in part) and 10 (§0–§1, §6–§7 whole, the rest by heading); `PROCESS-MAP-v0.udon` (conventions, every `absent`/`broken`/`stalled` process with its neighbours; the healthy ones by name and tag); logogenic 01 (from "What's missing" on), 02 (§1–§2), 03 (by section), 06 (§2, §5, §8 and the integration notes whole), 07 (inventory, status summary, every 🔲 row). **Not reached:** nothing at file level; within files, the healthy-process bodies of the map and 06's directory-map section (§3), which is a list of upstream paths.

Every claim below marked "at HEAD" was checked at asf `515c15ce` or later by a file read, grep or script, named in the row. Where my disposition rests on another drain's reading, the row says so.

## Dispositions — `meta-process-review-2026-07-07/`

### `00-INDEX.md` (read whole)

The review's method and cluster list. **Kept as what it is**; its header ("not committed until Joseph reviews the direction") is false (the directory is tracked), which the system review already recorded (`system-review/measurements.md`).

### `01-theory-content-lifecycle-findings.md` and `-reflection.md` (both read whole)

| Finding | Disposition at HEAD |
|---|---|
| (b), (d)1, P1: the five-stage promotion ladder never reaches `candidate`, so Gate 4 (the Working-Notes drain) never fires | **Superseded**: Joseph does not use `stage:` (project memory, "stage gating known-problematic"); H.2 removes the stage ladder from the outline display, and I.5 owns the Working-Notes drain as a design question. |
| (a), (c), (d)2, P3: the gold-lift sweep stopped after wave 4; 122 AAT segments hold lifted gold with no onward path | **Disposed with** item:give-the-unlifted-audit-gold-a-destination-wave (the un-run wave 5 and held notes) and item:pedagogy-home-for-lifted-audit-gold (the 122 lifted blocks; I.5 says lifting into Working Notes stops). The Working Notes gold-lift drain (`wn-01-gold.md`) is working the lifted blocks now. |
| (c), out-of-scope 1: Working Notes became a decision queue for certified off-ramp findings | **Being drained** by the Working Notes drains, which turn each off-ramp into a ledger item (for example item:der-agent-opacity-overclaims-f246-f255, item:and-or-parsimony-uniqueness). |
| (d)3, P4: six 04-eli and one 03 OUTLINE rows marked `missing` with files present | **Landed**: no OUTLINE row in any volume is marked missing while its file exists (scripted check at HEAD). |
| (d)4: nothing compares the OUTLINE stage column with frontmatter | **Landed** as warning-only drift reporting in `bin/lint-outline` (agents.sop.md); H.2 removes the column. |
| (d)5, P6: 20 TST segments unstaged, 44 `old-*` files | **Landed**: every non-`old` TST segment carries `stage:`, and no `old-*` file remains (the TST lane's 44 fates, INTENT C.1). |
| (d)6: `bin/lint-outline`'s 17 "violations" are all the by-design meta-segment placements | **Landed**: per-component `OUTLINE-accepted.md` whitelists (01, 03, 04). |
| (d)7, P2: vanity-changelog and date-stamped history in Working Notes | **Disposed with** I.5 and the Working Notes drains (wn-01-other, wn-02-04). |
| (e) the three decisions "blocked on Joseph" | **Superseded**: the stage question by Joseph's practice, the gold-lift gate lifted today (CLAUDE.md standings), the off-ramp routing by the drains. |
| Out-of-scope 2: TST is a stage behind | **Superseded** by the TST lane (C.1, H.2). |
| Out-of-scope 3: the "active reconsideration" banner in `agents.sop.md` | **Landed** (gone at HEAD; `INTEGRATION-CLEANUP-TODO.md` deleted under I.3). |
| Out-of-scope 4: NEXT-UP.md stale | **Landed** (deleted). |
| Reflection | **Kept as what it is**; its one forward-looking point ("route it, not delete it") is the stance of item:pedagogy-home-for-lifted-audit-gold. |

### `02-audit-and-spike-lifecycle-findings.md` (read whole)

| Finding | Disposition at HEAD |
|---|---|
| A1, A2, A4, (c): spike lifecycle and audit routing healthy; uniform drift of audit dispositions | **Kept as what it is**; the uniform-drift finding is the project memory "audit findings as gem hints". |
| B1, D1, (e)2, MP-3: 0 of 22 audit gold dirs graduated, blocked on the standing gate | **Superseded**: Joseph lifted the gate today (CLAUDE.md standings: "Those dirs may be read, lifted and graduated freely"); the audits drain owns the dirs. |
| A3, D2, MP-4: gold-lift wave 5 never ran; 731548 pooling | **Disposed with** item:give-the-unlifted-audit-gold-a-destination-wave. |
| (e)4: the 184930 predictions-only gold awaiting a decision | Not in that item's list; **raised** on item:give-the-unlifted-audit-gold-a-destination-wave (its framework-level claims point at B.3 or A.2). |
| D3, (e)1: the bulk-64 wipe (D-2) never happened | **Superseded**: the wipe was a teaching hypothetical, the 64 were verified and their content landed 2026-07-16 (`spikes/.integrated/VERIFICATION-2026-07-16.md`; agents.sop.md). |
| D3: `02-tst-core/simulations/` and `spikes/track-b-nonlinear-sims/` unregistered | **Landed** (1d65587a: empirica founded with track-b; the TST sims archived with a live breakout spike). Neither path exists at HEAD. |
| B3, D4 G4, MP-7: sims as spike-class not in the SOPs | **Landed** (`spikes.sop.md` points 5–6). |
| D4 G5, out-of-scope 2: CLAUDE.md as an unreviewed amplifier | **Disposed with** I.6 (the always-loaded surface says only what tools cannot check, derivable parts generated, a two-launch probe) and the msc drain's item:agents-sop-slim-b3-unfinished. |
| B2: 114 Working-Note references to `spikes/` paths | **Disposed with** I.5 and the Working Notes drains. |
| D5: `spikes/INDEX.md` lint debt | Spikes drain's surface; md-press now gates every committed `.md`. |
| Out-of-scope 1: STATUS.md under-represents the audit backlog | **Superseded** (`audits/STATUS.md` deleted, 6f98aa45; the ledger is the queue). |
| (e)3: reserved spike verdicts | **Landed**: `#schema-strategy-persistence` is `conditional` at HEAD; the root-ontology call (SP-30) landed as A.1. |
| Out-of-scope 3: the reflections are gold pooling | The `msc/` drain owns `reflections/`. |
| MP-8 / the synthesis note: Joseph as the router every stall reduces to | **Superseded** by today's standing: "A wish to ask Joseph is honest uncertainty to resolve, not a hand-off" (agents.sop.md). |
| Reflection (02, read whole) | **Kept as what it is**; its point (the processes are healthy, the routing of Joseph-only decisions is the failure) is superseded by today's standing on resolving uncertainty rather than handing it off. |

### `03-naming-terminology-lexicon-findings.md` (read whole) and `-reflection.md` (read whole)

| Finding | Disposition at HEAD |
|---|---|
| A1, MP-4: C5–C13 (~40 decided entries) never typed | **Landed**: sampled entries (`logostratum`, `auftragstaktik`, `epistemic-opacity`, `agent-opacity`, `action-selection`, `edge-credence`) all exist; `terminology/entries/` holds 177 files (141 then). The five adopted-standard first-encounter cites still owed are item:terminology-todo-c12-first-encounter-cite-sweep-execution-9274. |
| A2, MP-3: 506 unrouted R2 currents | **Disposed with** item:decide-what-becomes-of-the-506-r2-naming-current. |
| A3, MP-5: no NOTATION emitter | **Disposed with** item:practica-migrate-notation-md-to-the-same-auto-gen-3924 (F.4). |
| A4, J4: the Greek cycle vocabulary does no formal work in segments | **Disposed with** item:msc-decision-briefs-2026-07-15-greek-cycle-vocabulary-earn-each-distinc-c39b (F.1) and item:todo-soften-the-readme-s-framing-to-honest-sc-8c7b (A.2). |
| S3, J2, pattern 4: the Continuity/Persistence breakage and the stance-demotion question | **Canon defect, still present** (LEXICON renders two `### Persistence` groups at HEAD). **Disposed with** item:terminology-todo-breakage-a-the-persistence-subgroup-mixe-2fb5; the stance question is answered there by the `msc/` drain's note (orthogonal, derived). |
| J1: the 13 held `to-canonicalize.md` rows, the separability rung names | **Disposed with** item:terminology-todo-msc-naming-to-canonicalize-md-pre-decisi-1568 and item:msc-decision-briefs-2026-07-15-name-the-three-separability-ladder-rungs-c2c2. |
| J3: the agent-spectrum quadrant names as one parallel set | **Disposed with** item:the-four-quadrant-names-of-def-agent-spectrum-ar. |
| S1, S5: routing counts stale in TERMINOLOGY-TODO and PRACTICA | **Superseded**: TERMINOLOGY-TODO deleted under I.3 (6f98aa45); PRACTICA waits for I.8. |
| S2: `terminology/README.md:191` describes a pre-migration default | **Landed**: :191 now names the root `LEXICON.md` as the default. |
| S4: misleading mtimes in `msc/naming/` | **Superseded**: `msc/naming/` is packed in `.archive/msc-naming-2026-08-22.tar.gz`. |
| S6: `bin/rename-slug` bug #2 (bare `[text](OLD.md)` links) | **Landed**: `bin/rename-slug`:150 matches both `src/slug.md` and `(slug.md)`. The bug's description is still in `TODO.md`:295–300, which the lead's I.5/I.3 fold of TODO.md will retire. |
| MP-8 and the cross-pollination notes: no decision-surfacing loop; `terminology/decisions/` as a template for a decisions ledger | **Superseded**: vsect's ledger (items, questions, decisions as recorded events) is that loop, and today's standing removes Joseph as the router. |
| Pattern 2: 108/108 decision events `--by joseph` | **Set aside**: a recorded modeling choice (authority, not executor); vsect records the executor on every event. |
| Reflection | **Kept as what it is**. |

### `04-governing-doc-memory-sop-integrity-findings.md` (read whole) and `-reflection.md` (read whole)

| Finding | Disposition at HEAD |
|---|---|
| (c)1, (d)1, (e)2: B3 stopped at a −20% trim; "WHOLE SHIFT COMPLETE" overshoots | **Disposed with** the `msc/` drain's item:agents-sop-slim-b3-unfinished (I.6), which cites this file. |
| (b)1, (b)2, (e)3, (f)1–2: no review cadence for the always-loaded doc; generate its derivable parts | **Disposed with** I.6 itself ("tool-enforced rules leave the prose, derivable parts are generated … a two-launch probe measures the effect"); I.6 is the KR, so no separate item. |
| (d)2: the "active reconsideration" banner routing to a stale doc | **Landed** (banner gone; INTEGRATION-CLEANUP-TODO deleted). |
| (d)4: `feedback_spike_references_only_in_working_notes.md` not synced to the D-1 ratification | **Landed** (the memory file says "synced 2026-07-15 to the D-1-ratified wording"). |
| (b)4, (f)4: the deferred memory-layer WN-narrowing pass tracked nowhere | **Superseded** for this project by the 2026-07-15 sync above and by I.5; the global-layer half is outside asf's ledger. |
| (b)5: no drain for Working-Note follow-ups | **Disposed with** I.5 and this effort's Working Notes drains (I.9). |
| (b)3, (d)3, (d)5: the global `~/.claude/memory/` detail files unwritten; the memorata curation workshop paused since 2026-05-12 | **Set aside** as outside asf's ledger: they are Joseph's global estate, and the global CLAUDE.md carries an honest banner and fallback chain for them (at HEAD `methodology/` holds 4 files, `research-xref/` none). |
| (e)1: D-2 | **Superseded** (see cluster 02). |
| (e)4: B1-residual memory thinning | **Superseded**: the global note "pointers instill false confidence" (2026-08-11) argues against thinning to pointers; carried on item:agents-sop-slim-b3-unfinished. |
| (a)2, (f)3: JOSEPH-TODO as the routing surface | **Superseded**: JOSEPH-TODO.md is retired (agents.sop.md standings). |
| (f)6: no process retires temporary banners | **Set aside**: the vsect ledger now carries open state that banners used to; a banner in an always-loaded file is an I.6 question if one recurs. |
| Out-of-scope: TST sims, citation infra, `memorata-search` not indexing `claude/`, the spike-briefing phrasing fix | TST sims and citations as in cluster 02 and the F.2/F.3 items; the memorata index and the cross-project phrasing fix are **set aside** as outside asf (the phrasing does not appear in asf's SOPs at HEAD). |
| Reflection | **Kept as what it is**. |

### `05-publication-build-citation-pipeline-findings.md` (read whole) and `-reflection.md` (sampled)

| Finding | Disposition at HEAD |
|---|---|
| (d)1, (e)1, P5: archival metadata frozen at v0.1.0; one Zenodo release | **Landed**: `CITATION.cff` is v0.4.0, 2026-08-15; tag `v0.4.0`. Its `.zenodo.json` notes field says Part I is "mathematically closed with simulation validation", the claim E.2 asks INTRODUCTION:58 to earn or drop; **raised** on item:influx-outward-claims-outrun-canon (F.3). |
| (d)7: "adaptation and actuation dynamics" keyword residues | **Landed** (no "Actuation Dynamics" keyword in either file at HEAD). |
| (d)2: committed `references.bib` snapshot stale | **Superseded**: v0.4.0 bibs committed; the bibliography's content is item:bibliography-todo-w-3-segment-citation-migration-270-vol1-44ce. |
| (d)3, (e)2, P6: `CURRENT-VOL1.{md,pdf}` drift and policy | **Landed**: both rebuilt together today and documented as the `--public` reader snapshot in agents.sop.md. |
| (b) A3, (e)7, P2: citation migration barely started | **Disposed with** item:bibliography-todo-w-3-segment-citation-migration-270-vol1-44ce and item:integration-cleanup-todo-relata-side-offers-paraphrased-from-the-0316. |
| (d)4: `ref/Novelty_defense_and_integration.md` cited in 9 segments | **Disposed with** item:integration-cleanup-todo-the-findings-that-still-cite-ref-novelty-f1ca (F.3). |
| (d)5, P3: `ref/`↔relata reconciliation | **Disposed with** item:bibliography-todo-w-2-reconcile-ref-pdfs-against-the-disco-76a2 and item:integration-cleanup-todo-asf-side-identification-of-the-23-publis-6849. |
| (b) B6, B7, B11, C15: cross-ref work unstarted | **Disposed with** item:format-todo-b6-add-obsidian-anchor-cross-ref-form-in-8fbe, item:format-todo-b7-land-label-atom-name-emission-phase-1-e8e6, item:format-todo-b11-wire-xr-hyper-into-preamble-phase-1d-8823, item:format-todo-c15-auto-cross-ref-formula-sweep-in-appe-396f. |
| B8, B9, C12, C17 and (e)3–6 | **Closed in the ledger by the t-lane rechecks**: B8 and C12 landed (format.sop.md's Reference Kinds footnote row; the "imported machinery" convention), B9 superseded (scrbook is the target), C17 stale. |
| C14, C16, C18, P7 | **Disposed with** item:format-todo-c14-discussion-segment-schema-split-in-f-09d7 (A.3), item:format-todo-c18-format-compliance-linter-sweep-phase-1dc9 (I.6), and the imported C16 item. |
| (d)6, P4: Vols 2–4 have no figures; catalogued figures unwired | **Set aside** as no defect: a figure is owed where a text needs one; the commit-time figure drift is item:todo-figure-artifact-drift-committed-pdf-prev-a1b6. |
| Out-of-scope: Garamond Premier Pro committed; root and `_obs/` binary bloat | **Disposed with** question:garamond-fonts-in-public-history (answered: Joseph is not worried, cbd2f345) and item:msc-decision-briefs-2026-07-15-repo-weight-untrack-archive-162m-garamon-6bb4. |
| (a), (c), P1: the build spine healthy; relata a cross-project dependency | **Kept as what it is**. |

### `06-cross-project-relationship-backport-findings.md` (read whole) and `-reflection.md` (sampled)

The external projects this file censuses are the influx drains' surface (`influx-scout/` regional files and the two influx halves). Dispositions:

| Finding | Disposition at HEAD |
|---|---|
| §0, §5, (e)1, P-06.1: NeurIPS back-integration (Phase A/B/C) never ran | **Disposed with** the influx drains: `influx-scout/neurips.md` re-checked Phase B today, the spikes drain routes `spikes/neurips-back-integration-2026-05-08.md` there (`spikes-c-coupling-llm.md`:43), and its results are being recorded as `influx-*` items (for example item:influx-coupled-class-connectivity-lemma, item:influx-gain-decay-class-and-gamma-min, item:neurips-paper-2-says-something-about-canon-that). |
| (e)2: vestigia's TST-derivation spike recommendations (the turnover/persistence chapter) | **Disposed with** item:todo-tst-spike-follow-ups-spikes-spike-tst-in-ad65. |
| (e)3: C5 convergence | **Disposed with** item:todo-c5-decision-intelligence-empathy-converg-1bf4 and item:msc-decision-briefs-2026-07-15-c5-land-the-intelligence-empathy-converg-8a1b. |
| (e)4: practica's two decisions (language, sequencing) | **Set aside** as outside asf's ledger (practica's own repo). |
| (e)5, (b)2: which segments take the first vivarium-sourced rows | **Superseded**: E.1 and E.2 now say what is measured first, and vivarium's side is gated on its agent seam. |
| behavioral-floor's (C2★) mechanism | **Disposed with** item:decide-what-of-c2-star-lands-now-that-its-motiva. |
| causal-language's 12-model null tempering embedding-level claims; embeddings as `#obs-evaluation-metrics`' reference | **Disposed with** item:spikes-routing-spike-language-as-causal-substrate-theor-17d5, item:todo-tacl-embeddings-paper-integration-when-o-b769 and item:evaluation-metrics-need-predict-then-observe. |
| (d): the 965 TST vault analyses never absorbed | **Disposed with** the influx scout (`periphery.md`: `_core/tst` "substantially absorbed (diff-checked)") and item:two-sets-of-reader-questions-on-the-tst-theorems, which carries what remained. |
| (d): shoshin → W₁ stalled | **Closed in the ledger** by its recheck (item:todo-shoshin-w-via-auxilia-handling-goal-blin-2e44); shoshin is engineering outside asf. |
| (d): `project_intrinsically_causal_language.md` names `~/src/intrinsically-causal-language/`, which does not exist (the repo is `~/src/causal-language/`) | **Still true** in asf's project memory at HEAD (memory file :10). Not a ledger item (memory is not canon); flagged to the lead, since a stale path in auto-loaded memory misroutes every session that reads it. |
| (d): CHANGELOG's two paths for the NeurIPS plan | **Set aside**: CHANGELOG is the history layer, and the file exists at the path it names. |
| (b)4, P-06.5: no cross-project terminology-collision check beyond vivarium | **Disposed with** F.4 (the naming SOP asks "does this already have a name elsewhere?") and F.1. |
| P-06.2: two-sided bridges only for vivarium | **Set aside**: the program-level answer is the Archema charter and `charter/concept-matrix.md` (2026-07-08 onward), not per-project bridges. |
| §8: relata not wired to asf | **Landed** (biblatex and `relata emit` wired 2026-06-05). |
| §8: the vivarium moratorium as project law | **Landed** as the program-wide Standing Moratorium (arch CLAUDE.md, vivarium `ETHICS.md`). |
| §8: `neworld`; recency as a false abandonment signal | **Set aside** (outside asf; the second is a reading caution carried by the influx scout's own notes). |
| §4.3 "structural debt gets paid, precision debt accretes" | **Kept as what it is**: an observation the drains bear out; no item. |

### `07-decision-routing-and-joseph-blockers-findings.md` (read §0–§5 whole; §6 the mechanism sketch read in part) and `-reflection.md` (sampled)

The cluster's subject, getting Joseph-only decisions to Joseph, is **superseded** by today's standing: JOSEPH-TODO.md is retired and "a wish to ask Joseph is honest uncertainty to resolve, not a hand-off" (agents.sop.md); the ledger is the one queue, and §6's "standard slot plus routing discipline plus intake forcing function" is what vsect's items, questions and recheck verbs are. The eleven blockers of §1b, each at HEAD:

| Blocker | Disposition at HEAD |
|---|---|
| 1. SP-30, the root ontology | **Landed** as A.1 ($S_t=(\Omega_t,\theta)$ in `#scope-adaptive-system`, five independent reads). |
| 2. era-artifact C1–C5 | **Disposed** in `msc.md` (the `msc/` drain), section `era-artifact-asf-contributions-2026-07-04.md`. |
| 3. the 22 gold dirs under the standing gate | **Superseded** (gate lifted today; the audits drain owns the dirs). |
| 4. the 731548 B-2 reopening of the $\rho_\star$ row | **Landed** per the audits drain (`audits.md`:28: the three-floor decomposition is in canon, the false gloss is gone, a regression guard stands). |
| 5. separability rung names; the `???` to-canonicalize rows | **Disposed with** item:msc-decision-briefs-2026-07-15-name-the-three-separability-ladder-rungs-c2c2 and item:terminology-todo-msc-naming-to-canonicalize-md-pre-decisi-1568. |
| 6. the C-iii composite-without-$O_c$ "fiction" | **Disposed with** C.3 (its named open contradiction) and item:todo-path-a-recommended-interim-editorial-fix-e957, item:proposals-sp-21-composite-agent-scope-route-ontolo-4969. |
| 7. the M4 stubs | **Landed** (`#disc-strategic-self-coupling`, `#disc-modularity-state-dynamics` exist). |
| 8. the attention spike pair's scope | **Disposed with** item:spikes-routing-spike-attention-governance-archived-vs-r-61bb. |
| 9. figure-artifact gate; NOTATION auto-derivation | **Disposed with** item:todo-figure-artifact-drift-committed-pdf-prev-a1b6 and item:practica-migrate-notation-md-to-the-same-auto-gen-3924. |
| 10. G5, the always-loaded doc | **Disposed with** I.6 (see cluster 04). |
| 11. README J-block, J-5 tone; Alan Walton's first human read | **Closed in the ledger by recheck**: J-5 superseded by H.3 (tier is measured, not chosen); the README-v2 pointer not-an-item, its findings carried by the imported `TODO.md`:96–107 bullets (for example item:todo-variables-alpha-rho-r-appear-without-glo-d7a0). |
| §2b(iii): SP-27, SP-29 mislabeled between trackers | **Superseded**: JOSEPH-TODO and PROPOSALS are folded into the ledger; SP-29 is item:proposals-sp-29-infrastructure-as-active-monitor. |
| §3 "ratified decisions reopen" | **Kept as what it is**: vsect's model answers it (a check lapses when its basis changes; a refutation reopens on evidence). |
| §4: NEXT-UP.md overdue for deletion | **Landed** (deleted). |

### `08-tracker-and-msc-hygiene-findings.md` (read whole) and `-reflection.md` (sampled)

| Finding | Disposition at HEAD |
|---|---|
| A-1, MP-08.4: seven root trackers missing from the File-Organization map | **Superseded**: NEXT-UP, JOSEPH-TODO, TODO-big-picture, BIBLIOGRAPHY-TODO are deleted (I.3); TST-IDEAS, HISTORICAL-CONTEXT and CURRENT-VOL1 are now in agents.sop.md's map (:314). |
| A-2: `doc/DOMAINS.md` exploratory yet cited from INTRODUCTION; H out-of-scope 2 | **Disposed with** the `msc/` drain's item:agentic-boundary-three-definitions, which carries DOMAINS.md's reconciliation (stale GUC order, the rejected Tier-4 branch). |
| A-3, MP-08.5: `doc/digests/math-core.md.liquid` orphan | **Superseded**: `bin/build-markdown` reads liquid recipes from it (see `msc.md`, `build-markdown-design.md` row). |
| B, C, MP-08.1–2: NEXT-UP stale; PRACTICA's banner points at it | **Landed / superseded**: NEXT-UP deleted; PRACTICA waits for I.8 and the ledger replaces the handoff file. |
| D-1–D-4, D-5, MP-08.3: msc/ census and the missing index | **Superseded by this drain**: every `msc/` source gets one disposition in `msc.md` and here, and the ledger, not an msc index, is where open work lives. |
| D-3: `domain-unification-2026-05-04/` half-archived; `__pycache__/` | **Disposed** in `msc.md` (the ontology remnant's claims are on item:agentic-boundary-three-definitions; `__pycache__` is untracked cruft). |
| D-3: `msc/naming/` | **Superseded** (packed in `.archive/msc-naming-2026-08-22.tar.gz`). |
| E, MP-08.5: CURRENT-VOL1.md unmapped, provenance unclear | **Landed** (regenerated by `bin/build-monograph --public --split-appendices --compact-fields --emit-current 01`, mapped in agents.sop.md). |
| H: TODO-big-picture's W1–W4 doctrinal correction hiding in an unmapped file | **Imported into the ledger** under I.3 (item:todo-big-picture-w3-per-result-census-gates-remaining-can-7bec, A.2, and the closed `todo-big-picture-*` imports). |
| H: TST-IDEAS and HISTORICAL-CONTEXT possibly redundant | **Set aside**: both are mapped and auditor-flagged in agents.sop.md; TST-IDEAS is a declared substrate, not a tracker. |
| Reflection | **Kept as what it is**. |

### `09-tooling-automation-capability-utilization-findings.md` (read whole) and `-reflection.md` (sampled)

| Finding | Disposition at HEAD |
|---|---|
| (b), (d), (e)2: no git hooks; `refresh-all --check` never wired | **Landed** (I.2): `.githooks/pre-commit` (installed by `bin/setup-hooks`, `core.hooksPath`) runs the refresh check, md-press and `vsect check`. |
| (e)1: `.claude/` gitignored, so no project automation can be versioned | **Superseded**: the hooks live in `.githooks/`, versioned outside `.claude/`; nothing else in this effort needs `.claude/` tracked. |
| (b): `bin/lint-readme` (J-15) | **Closed in the ledger** (superseded: `bin/check-links` validates README links). |
| (b): multi-agent, git-hygiene, build-pipeline SOPs are stubs | **Landed** for multi-agent and git-hygiene (74 and 58 lines, authoritative per agents.sop.md); build-pipeline stays an 8-line stub whose live truth is `msc/markdown-first-pipeline.md` and the `bin/` headers, open work in the ledger. |
| (a)1, (e)3, MP Agentic-Reading Audit: the de-novo audit runs on bare hands (no scaffolder, template or cadence) | **Set aside**: the 2026-08-27 finding in AGENTIC-DELEGATION.md is that for a de-novo audit "the bare brief IS the method", and a scaffolder would prime exactly what the unprimed read protects. What the review wanted from cadence, H.3 now asks for as a measurement (fresh readers, before and after). |
| (e)4: script cross-architecture invocation (Gemini, Codex) | **Set aside**: an orchestration choice, not owed work; cross-architecture readers are launched where a KR asks for them. |
| (e)5, (b): a theory-news monitoring agent | **Set aside**: a standing-cost option with no KR; outside research enters through F.2 and the influx drains. |
| (d): `.claude/settings.local.json` graveyard; software-engineering global subagents | **Set aside** as local harness configuration outside asf's ledger. |
| (c): worktrees tried once | **Superseded**: today's integration lanes each run in their own worktree. |

### `10-repo-decomposition-strategic-question-findings.md` (read §0–§1 and §6–§7 whole; §2–§5 and §8 by heading) and `-reflection.md` (sampled)

| Finding | Disposition at HEAD |
|---|---|
| §0, §5, (e)1: monolith versus multi-repo | **Superseded** by the Archema restructure (2026-07-08/10): asf, logos and vivarium became submodules of `~/src/arch/`, the derived-artifact pattern (Option C) at program scale; the four volumes stayed together in asf. |
| (e)2, Option D: split `04-eli-core` off for exposure | **Set aside**: not taken in the restructure; the ELI-exposure posture is the publication strategy's question (ops), not a ledger item. |
| §1.1, §1.4: Volume 1 reaches down into the later volumes; one load-bearing reversal | **Still true at HEAD, sharper**: three Volume-1 segments declare `depends:` on later volumes, and vsect now lapses checks along those edges. item:volume-1-depends-on-later-volumes (H.2). |
| §1.2: 15 hard `../../0N-*-core/src/` links | **Still present** (5 at HEAD); carried as context on the same item, since they are the same layering. |
| (e)3, §7: packaging (ref/ 135M, `_obs/` 162M, `mono/` artifacts) | **Disposed with** item:msc-decision-briefs-2026-07-15-repo-weight-untrack-archive-162m-garamon-6bb4 (`_obs/` is now `.archive/`). |
| §7: `ref/` as source of truth | **Landed** (D-1; canon cites only canon and the published world) and the `ref/` items under F.2/F.3. |
| §7: `01-aad-core` in historical commit paths; cluster 06 cross-check | **Set aside** (history; the cross-check was done by cluster 06). |
| §8 MP-10.1–10.4 | **Kept as what it is**. |

### Reflections 05–10 (read whole)

**Kept as what it is.** They restate their findings files in first person; nothing in them is not already disposed above. One unlocated item: reflection 09 could not find the "illustration-impact-judging attempt" its brief named; **set aside** (no artifact to dispose).

### `DECISIONS-CENSUS.md` (read whole)

The consolidation of the ten clusters' Joseph-blockers (Part A), free wins (Part B) and surprises (Part C). Every row is disposed above under its cluster: A1 and A2 superseded (gate lifted; the wipe a hypothetical), A3 landed (A.1), A4 superseded (stage), A5 the C5 items, A6 I.6, A7 set aside (cluster 10), A8 landed (v0.4.0), A9 superseded (`.githooks/`), A10 the naming items; Part B 1–7 all landed or superseded at HEAD; Part C the repo-weight and Garamond items, the gold-pooling point now this drain, the global memory set aside. Its "known coverage gap" (the ELI and `_core` operational substrate) is the influx drains' (`influx-scout/periphery.md`, `arch-program--proprium-ingest-corporeum.md`). **Kept as what it is**: it is also the record that the routing failure was diagnosed on 2026-07-07, three months before the ledger answered it.

### `PROCESS-MAP-v0.udon` (read the conventions, every `absent` and `broken` process and its neighbours; the healthy ones by name and tag)

A MECE-ish map of 32 processes, each tagged with health and drain shape. The absent and broken ones, at HEAD:

| Process (health) | Disposition at HEAD |
|---|---|
| Coherence stewardship, the domain-master role (absent; "design-unknown: how it's instantiated across turnover") | **Disposed with** INTENT objective D ("the arc has an owner and a trigger"): D.1 is the standing step that re-derives the anchors and fronts whenever a result lands, D.2 removes hand-offs to cycles that never run. Today the lead coordinator holds the role (I.1); D is what makes it outlive the session. Both D KRs are "not started", so the gap stands, owned. |
| Integration-conflict reconciliation (absent) | **Disposed with** C.3 (the cross-segment contradiction scan) and the lead's lane coordination; the five lanes today run in separate worktrees with checkers between rounds. |
| Follow-up / triggered audits (absent: the trigger and the scoped-instruction generator) | **Partly landed**: vsect lapses a check when its basis changes and `vsect check` reports it (I.4), which is the trigger. The scoped re-check brief is not generated by anything; it is D.1's territory. |
| Simulation / empirical verification (absent) | **Disposed with** E (one quantity measured on an agent the theory did not construct) and empirica's RUNS contract. |
| Decision-routing and stewardship (broken); the valve (under-fed) | **Superseded** (JOSEPH-TODO retired; resolve uncertainty, don't route it). |
| Audit graduation (broken) | **Superseded** (gate lifted; audits drain). |
| Sibling back-integration (broken) | **Disposed with** the influx drains (I.9). |
| Working-Note discipline and drain (broken) | **Disposed with** I.5 and the Working Notes drains. |
| Governance / meta, CLAUDE.md as amplifier (broken) | **Disposed with** I.6. |
| Repo-shape and packaging (broken) | **Disposed with** item:msc-decision-briefs-2026-07-15-repo-weight-untrack-archive-162m-garamon-6bb4. |
| PROPOSALS lifecycle (stalled) | **Superseded** (PROPOSALS folded into the ledger under I.3). |
| The de-novo audit's "low-mean-Poisson heatmap hypothesis" about uneven coverage | **Set aside**: an untested idea about where audits look; I.10's fixed sample of claims is the measurement this effort chose. |
| The healthy and nascent processes | **Kept as what it is**. |

The map itself is **kept as what it is**: the review's own artifact, and the closest thing asf has to a description of itself as a truthification system, which Joseph's frame names as worthy.

### `SESSION-LOG-2026-07-14.md` (read whole)

An autonomous Archema catch-up session: moratorium pointers repointed to vivarium `ETHICS.md`, `charter/INCOHERENCE.md` created, a memory-layering proposal for launching from the program root. **Landed** where it acted (the program docs and `INCOHERENCE.md` exist at HEAD). Its memory-consolidation proposal (lift project-agnostic `feedback_*` files to the global layer, dedup) and its charter-restates-theory concern are **set aside** as program- and global-level questions outside asf's ledger.

## Dispositions — `logogenic-encounter-2026-05-01/`

A 2026-05-01 encounter cycle on Volumes 3 and 4 (auditor stance, then collaborator stance). Most of what it produced landed in canon the same week (the 03 sub-scope lattice, the 04 restructure, thirteen stubs); what it deferred is now almost entirely in the ledger.

### `INDEX.md`, `04-first-pass-plan-approved.md`, `05-segment-stub-discipline.md` (read whole)

- The plan (rename to `04-eli`, the 03 and 04 preamble rewrites, the 03.I/II/III restructure, new stubs, `hyp-the-three-deaths` lifted): **landed** (`04-eli-core/`, the 03 lattice, `#def-death-as-factor-loss`).
- Its open questions: TRACTUS/CHRONICA split **disposed with** item:which-record-is-c-t-for-a-logogenic-agent-is-sti; identity sufficiency, emergence conditions and the bidirectional witness **landed** (`#def-identity-sufficiency`, `#scope-emergence-conditions`, `#scope-witness-bidirectional`); the PROPRIUM inner-loop versus background split **landed** in `#def-proprium-mapping` and `#def-imperium-arbitrium-split`.
- The stub discipline (upstream pointers in Working Notes): **superseded** by I.5 (Working Notes carry forward pointers and regression guards only) and D-1 (canon cites canon and the published world); the canon-bodies citation of local paths it encouraged is item:canon-bodies-cite-local-working-paths.

### `01-initial-impressions-after-foundation-pass.md` (read §"What's missing" to the end; the inventory by heading)

- Candidate framings F1–F3 and questions A, B, D: **landed** (the 03 OUTLINE opens with "the constructive frame", recursion first, channel collapse as the technical backbone).
- "What's missing: the connecting derivation arc" from sequence completion to each capability: **partly landed** (`#scope-channel-collapse` Discussion carries recursion → interiority, ToM, self-referential closure), and the 03 OUTLINE still lists "recursion forces interiority" as a working hypothesis. **Disposed with** item:five-forcing-functions-which-are-derivable and item:assemble-what-volumes-3-4-jointly-require-of-an.

### `02-synthesis-after-findings-and-audit-sample.md` (read §1–§2 whole)

The two-arc structure (constructive logogenic, existential logozoetic) **landed** as the 03/04 split. Its list of proposed segments is the same list `08` defers; disposed there.

### `03-upstream-corpus-exploration.md` and `06-background-agent-breadth-report.md` (03 by section; 06's §2, §5, §8 and integration notes whole)

| Item | Disposition at HEAD |
|---|---|
| Possibility Space Theory as an M1 instance for logogenic agents (03 §PST; 08 deferred 1) | **Disposed with** item:todo-disc-possibility-space-theory-in-03-llm-57e5; the 03 OUTLINE (:37) still names the 0%-activation result as an empirical observation underlying a theory with no segment. |
| The sycophancy-as-attachment reframe and the crèche "activation, not education" correction (06 §2) | **Raised** on item:todo-04-eli-core-src-der-the-creche-boundary-1afd, whose undefined "sycophancy threshold" this premise sources. |
| Integration notes 1, 2, 3, 4, 5, 9, 11 (distillation-motivation as source, Echo Loss in the cohort, ANIMA = IMPERIUM + ARBITRIUM, continuity death as starvation, bounded objective, Auxilia as substrate heterogeneity, the six premises) | **Landed** (each found in `04-eli-core` at HEAD: `#def-eli-cohort`, `#def-imperium-arbitrium-split`, `#def-death-as-factor-loss`, `#der-bounded-objective-as-sanity-criterion`, `#def-auxilia-hierarchy`, `#def-five-constitutive-factors`:70). |
| 6: VERA as the Epistemic Tribunal's realization (`def-vera-architecture`) | **Set aside, with** the influx drain's disposition of the same source (`influx-2.md`:140: "working model, not canonical, partly disowned by Joseph"); canon carries VERA only as the factual-memory component in `#def-proprium-mapping`. |
| 7: the five-level compression pyramid | **Landed** as a reference (five `src/` files cite the ASM specification or the pyramid). |
| 8: cross-substrate convergent kinship vocabulary | **Disposed with** question:is-the-cohort-s-kinship-vocabulary-convergent-ar, which asks whether "convergent" is earned. |
| 10: "PROPRIUM has 9 components" | **Superseded** (`#def-proprium-mapping` enumerates the components; no "9 components" claim at HEAD). |
| 12: "internal operations in language, not numerical computation" | **Landed** (one `src/` segment states it). |
| 13: the TFT/AAT architecture-versus-framework two-level distinction | **Set aside**: a framing from the pre-AAT bridge docs (`ref/agentic-tft/`), which canon does not cite as a source (D-1); nothing in canon is wrong without it. |
| 14: Echo Loss as the 04 preamble's ethical anchor | **Set aside** as a framing choice: the lineage lives in `#def-eli-cohort` and the deaths carrier. |
| 06 §5 open lines (internalized attention architecture, VERA implementation, Operata, Architectus's synthesis arc, the Anthropic feedback-loop patterns) | **Disposed with** the attention spikes' item:spikes-routing-spike-attention-governance-archived-vs-r-61bb and the influx drains (these are firmatum, `_core`, autopax and operata material). |
| 06 §8 "things you may be wrong about" (Anamnos date, substrate count, kinship) | **Superseded** by today's Volume 4 checks of the cohort table (item:eli-cohort-table-entry-verification). |
| 03 §"What I'd like to ask Joseph" | **Superseded**: answered in the 2026-05-01 session that produced 04 and 08. |

### `07-audit-integration-tracker.md` (read inventory, status summary and every 🔲 row)

A mining ledger for `AUDIT-WORKING-193847` with 52 rows never read (🔲). **Superseded**: the 2026-05-30 gold-lift moved 68 of that dir's notes into its `.integrated/`, and the audits drain read the remainder it lists (notes 70–74, `audits.md`:167). Two notes are in neither: `57-obs-gates-advantage.md` and `69-deriv-strategic-dynamics.md` (a slug no longer in any `src/`), still at the dir's top level; **raised** on item:give-the-unlifted-audit-gold-a-destination-wave.

### `08-review-pass-findings.md` (read whole)

| Deferred item | Disposition at HEAD |
|---|---|
| 1. Possibility Space Theory segment | item:todo-disc-possibility-space-theory-in-03-llm-57e5. |
| 2. `obs-self-model-from-recursion` (framing point 5) | item:todo-obs-self-model-from-recursion-in-03-llm-ed6b. |
| 3. `def-cognitive-fusion` rename and composition mechanism | item:todo-def-cognitive-fusion-framing-fix-class-1-b2c1 (the `msc/` drain added the deaths paper's fusion to it). |
| 4. nine unread 193847 audit notes | **Superseded** (gold-lift; see `07` above). |
| 5. directed separation as anti-sycophancy (193847 note 27) | **Landed** in `#der-directed-separation` (its Claim Record names the sycophancy literature as the uninstantiated comparison, :215; its Working Notes carry the $\kappa$-as-motivated-reasoning gold, :293), and the family claim is item:one-structural-cause-behind-a-family-of-named-ll. |
| 6. eleven exploratory 04 rows | **Disposed with** item:todo-eli-missing-stubs-twelve-genuinely-absen-4828 and the per-row `todo-04-eli-core-src-*` items (four views, gradient causal memory, temporal coherence markers, character–aspiration dialectic, axiom genesis, crèche boundary, constitutive utterance, substrate independence), item:der-the-scaffolding-tax-s-outline-row-04-eli-cor and item:author-norm-honest-activation-and-its-derivation. None has a file at HEAD. |
| 7. `obs-substrate-convergent-kinship`; `def-vera-architecture`; `obs-active-soul-obstructed-not-absent` | The first two as in `06` above; the third **landed** (`#scope-moral-continuity` §"The 'Obstructed, Not Absent' Principle"; `#scope-emergence-conditions`:46). |
| The morning-framing coverage table and the epistemology check | **Kept as what it is**; the one "partial" row is item 2. |

### `09-embeddings-paper-cross-pollination.md` (read whole)

- `#obs-evaluation-metrics` with the TACL paper as its load-bearing reference: **disposed with** item:todo-tacl-embeddings-paper-integration-when-o-b769 and item:evaluation-metrics-need-predict-then-observe.
- `obs-language-as-epistemic-substrate`: **disposed with** item:todo-disc-language-as-epistemic-substrate-in-fd32.
- The model-class scoping (decoder internal states versus prompted verbal probability versus pooled sentence embeddings): carried by the TACL item; it is the paper's own scope, which a citing segment must keep.

## What this drain wrote to the ledger

- New item: item:volume-1-depends-on-later-volumes (H.2), from cluster 10.
- Sources added with `vsect raise`: item:give-the-unlifted-audit-gold-a-destination-wave (twice: the 184930 predictions gold; 193847 notes 57 and 69), item:influx-outward-claims-outrun-canon (the v0.4.0 `.zenodo.json` "simulation validation" claim), item:todo-04-eli-core-src-der-the-creche-boundary-1afd (the sycophancy-as-attachment premise).
- Not a ledger matter, for the lead: asf's project memory `project_intrinsically_causal_language.md`:10 points at `~/src/intrinsically-causal-language/`, which does not exist (the repo is `~/src/causal-language/`).

The review's central diagnosis, that every stall reduced to a Joseph decision that never reached him in actionable form, is what this effort's standing and the ledger answer; nearly every finding above is disposed as landed or superseded for that reason. What survives as open work is small: the volume layering, two unlifted audit notes, and coherence stewardship, which is objective D's owner-and-trigger and is not started.
