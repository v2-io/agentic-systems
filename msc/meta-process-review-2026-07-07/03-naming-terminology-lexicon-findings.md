# Findings — Cluster 03: naming / terminology / lexicon

*Meta-process review, 2026-07-07. Claude Opus 4.8 (1M context). All counts verified firsthand against files/git/JSON on 2026-07-07 unless marked otherwise. Where a tracking doc's claim diverges from ground truth, both are given.*

## Headline

The naming/terminology infrastructure is **built and working**; the program is **stalled on Joseph-author decision throughput, not on tooling**. The last substantive naming-cycle activity was ~2026-05-10 to 2026-05-15 (C1–C4 terminology batches + LEXICON going live auto-generated). Since then: the terminology store's last decision event is 2026-05-11; the last entry-file commit is 2026-06-10 (and that one was segment-driven, not naming-cycle). C5–C13 (~40 already-*decided* canonicalize commitments) remain unexecuted. 506 of 629 R2 currents remain unrouted. Two reorgs (§F Continuity/Persistence; §E agent-spectrum tetrad) are blocked on Joseph. NOTATION→terminology migration is aspirational and unstarted.

The single most actionable fact: **C5–C13 are executable by an agent right now with no Joseph input** — the decisions were already made in the 2026-05-04 curation pass; only the entry-typing (`bin/term add` + `bin/term decide canonicalize` + `render`) is pending. It has sat one workflow away for ~2 months.

---

## (a) De-facto processes actually running (or that ran and stopped)

**P1 — `bin/term` append-only terminology store.** BUILT, WORKING, being fed until ~2026-05-11.
- 141 entry files in `terminology/entries/`; 108 slugs with decision-event dirs in `terminology/decisions/`; 108 decision event files total.
- Decision action breakdown: 96 `canonicalize`, 4 `rename`, 6 `weak`, 2 `gloss`.
- **Every decision event is `--by joseph`** (108/108). The `decider` field records the *authority* (Joseph), not the executing agent — a deliberate modeling choice. This means the audit trail cannot distinguish which agent typed which batch; it records only that Joseph authorized the canon.
- Last decision-event timestamp: **2026-05-11** (`worked-example`, `type-sketch`, etc.). Last entry-file *commit*: 2026-06-10 (`de56b9a`, multi-timescale-stability promotion — segment-driven, not a naming-cycle event).
- The design (`terminology/README.md`) is a genuinely considered trade study (sqlite vs per-entry YAML, decided 2026-05-08 in favor of YAML modeled on `~/src/neurips/refs/`). `safe_write` atomicity contract, permissive-extractor/strict-linter split, per-entry files for merge-conflict isolation. This is not scaffolding — it is finished infrastructure.

**P2 — LEXICON.md auto-generation.** LIVE and complete.
- LEXICON.md carries the `Auto-generated from terminology/entries/` marker (line 3). Went live as generated artifact at commit `868f72a` ("Naming Phase 6: LEXICON.md goes live as auto-generated artifact; 37 entries migrated"). Now renders 141 entries.
- `bin/term render`'s default destination is now `ROOT / "LEXICON.md"` (verified `bin/term:751`) — the migration-complete flip described in `terminology/README.md:191` has *happened in code but not in the doc* (see staleness §d).

**P3 — Manual canonicalize-curation pass (Joseph-author interactive routing).** RAN 2026-05-04, then STOPPED.
- Routed 103 of 118 candidates across 8 batches into `msc/naming/naming-rename-plan.md`; 13 deferred to `msc/naming/to-canonicalize.md`. This is the only routing pass that has ever run against the 629-current cohort. Sustainable rhythm was ~12 currents/batch (PRACTICA item 13).
- Downstream execution: §A slug renames (7/7) landed; §B prose-vocab renames (8/8, incl. the GUC Class 1/2/3 → Separated/Coupled/Partial bundle) landed 2026-05-09 on `guc-rename-2026-05-09`; C1–C4 terminology batches landed 2026-05-10 (commits `2f8e512` C1 29 entries, `d06236e` C2 5 Greek phases, `4f1f65d` C3, `59620d3` C4 58 FORMAT process-vocabulary entries, `7dd505b` C4g three-rings). C4's 58 process-vocabulary entries explain the bulk of the 141-entry population.

**P4 — R2 voting aggregator.** BUILT, RAN, cohort closed.
- `bin/naming-r2-aggregate.rb` produces three artifacts (`r2-aggregate-table.md` score-card, `r2-aggregate-detail.md`, `r2-patterns.md`). Landed 2026-05-01. Voting cohort (gemini-r2, opus-r2b/c, sonnet-r2b/c, codex-r2b) closed 2026-04-30. R1 folded as one synthetic voter. This is a completed sub-process; its *output* (629 scored currents) is the un-drained input to P3.

**P5 — Mechanical slug tooling.** WORKING, standing.
- `bin/align-slug` (role-prefix from `type:` frontmatter, `TYPE_TO_PREFIX` table) and `bin/rename-slug` are live and used. Two `bin/rename-slug` bugs are logged (TODO.md §"bin/rename-slug bugs"): #1 (hardcoded old dir) RESOLVED 2026-05-15; #2 (bare-filename markdown links not rewritten) still open, minor.

---

## (b) Aspirational processes the docs/SOPs intend but that are not running

**A1 — C5–C13 terminology canonicalize execution (~40 entries).** DECIDED, UNEXECUTED.
- Verified firsthand: of the C5–C13 terms, nearly all are MISSING as entry files. Checked ~35 terms; only `worked-example`, `communication-gain`, `update-gain` exist (landed via other batches). MISSING includes: `logostratum`, `temporal-software-theory`, `auftragstaktik`, `epistemic-shadow`, `extreme-transition-motif`, `logogenic`, `logozoetic`, `macro-step-ratio`, `matrix-exploration-bonus`, `trust-meta-model`, `deliberation-threshold`, `canonical-formulation`, `teleological-unity`, `system-availability`, `epistemic-opacity`, `agent-opacity`, `action-selection`, `causal-structure`, `multi-agent`, `equilibrium-convergence`, `feature`, and the C8 batch (`contraction-over-drift-principle`, `conceptual-alignment`, `edge-credence`, `purposeful-substate`, `task-terminal-stance`, `default-signal-function`, `strategy-description-length`, `transition-opacity`).
- The TERMINOLOGY-TODO checkboxes for C5–C13 are therefore **accurate** (genuinely unchecked = genuinely undone). The file frames itself as an "active execution queue," but nothing in §C has moved since C4 landed 2026-05-10 (~2 months).
- **These are canonicalize commitments already routed in the 2026-05-04 pass** — they need entry-typing, not decisions. Agent-executable now. (C7/C9 carry documented nuance flags, but those are recorded guidance, not open questions.)

**A2 — Routing the remaining 506 unrouted currents (PRACTICA item 13).** NOT STARTED beyond the initial 118.
- `master-list-curated.json` ground truth (parsed 2026-07-07): 629 currents; **123 marked, 506 UNROUTED** (`rename_status: None`). Marked breakdown: 56 canonicalized, 25 renamed, 10 canonicalized-greek-phase, 9 canonicalized-with-nuance, 9 canonicalized-compound, 5 canonicalized-adopted-standard, 5 canonicalized-format-layer, 4 excluded.
- PRACTICA estimates this at "~40+ batches, several months of evaluation passes." At the ~12/batch sustainable rate it is the single largest open item in the cluster and the one most dependent on Joseph-author bandwidth.

**A3 — NOTATION.md → terminology auto-generation.** ASPIRATIONAL, UNSTARTED.
- `bin/term` has NO `notation` render verb (verified: `cmd_add/show/list/search/decide/render/lint/validate` only — no `cmd_notation`). The `notation:` field IS reserved on entries and IS read into the LEXICON table column, but there is no `NOTATION.md` emitter.
- NOTATION.md remains hand-authored and is **non-authoritative by construction** (its own drift caveat; TODO.md §"Auto-derive NOTATION.md" and §"NOTATION migration to terminology system"). Bootstrap migration (catalog hand-authored rows → create/augment entries with `notation:` → switch to generation) has not begun. Marked lower priority than the LEXICON sweep.

**A4 — Greek-vocabulary prose discipline.** OPEN FINDING, unresolved.
- TODO.md §"Greek vocabulary prose discipline" (audit-471203, 2026-04-29): the Greek cycle vocab (chronica/prolepsis/aisthesis/aporia/epistrophe/praxis) appears at framing/lexicon level but segment-level math doesn't depend on the distinctions; README's "each Greek term names a distinction English flattens" is overclaimed against actual segment prose (authors fall back to flatter English, e.g. "mismatch" right after defining `aporia`). Two paths (tighten segments so the distinctions do work / soften README to honest scope), per-term per-segment judgment. Neither path has been executed. Note the tension: R1+R2 voters near-unanimously *defended* the Greek terms synoptically, but the incremental audit walk surfaced they don't do formal work — a genuine methodological disagreement between the voting process and the audit process, unresolved.

---

## (c) Emergent patterns from git history

**Pattern 1 — Compressed burst then silence.** The entire terminology-store buildout + C1–C4 execution + LEXICON-live happened in a tight window: infra commit `4e07097` (bin/term), Phase 6 live `868f72a`, C1–C4 all on 2026-05-10 within hours (`14:01` C1 → `19:30` C4g). Then near-total silence on naming-cycle work for ~2 months. This is the signature of a process gated on a scarce serial input (Joseph) rather than on parallelizable agent work: when the input was available, everything downstream fired fast; when it wasn't, nothing moved despite ready tooling.

**Pattern 2 — Decisions attributed to authority, executed by agents.** 108/108 decision events `--by joseph` regardless of which agent typed the batch. The append-only store faithfully records *what became canon and when* but deliberately does not record *which substrate executed it*. Consistent with the project's identity-not-substrate stance, and with the peer-voice culture (the agent is Joseph's hands, the decision is Joseph's).

**Pattern 3 — Renames chase upstream structural churn.** A large fraction of terminology git activity is *reactive* to bigger renames: AAD→AAT (`a3872db`, `9292417`, Stage 5/9b), dir harmonization `04-eli`→`04-eli-core` (`ce99ce6`), GUC class swap. The naming subsystem spends real effort keeping consistent with framework-level renames it doesn't originate. The `bin/rename-slug` bug #1 (hardcoded `04-logozoetic-agents`) is a fossil of exactly this — the tool silently skipped a renamed dir for a period.

**Pattern 4 — The Continuity reorg went sideways, not forward.** Commit `413e1c6` "merge Persistence + Continuity Stance into Continuity section" is the state the §F findings (2026-05-10, one day later) identify as *wrong*. Follow-ups `4161611` (add disc-continuity-stance segment + re-ground 5 stance entries) and `117c46f` (fix primary_source, note pending status) did grounding work but did **not** execute the §F recommendations (rename section Continuity→Persistence, split out Continuity Stance, move Moral Continuity to ELI). Net: partial motion, core reorg still blocked.

---

## (d) Stale / broken / abandoned things (concrete)

**S1 — Routing counts stale in prose.** TERMINOLOGY-TODO.md:5 and PRACTICA.md:87 both say "58 currents marked / ~511 unrouted." Ground truth in `master-list-curated.json`: **123 marked / 506 unrouted**. The JSON's *own* meta note also says "58/629 as of 2026-05-09" while its body carries 123 — even the JSON's summary lags its data. Undercount of routing progress by ~65 currents. (PRACTICA:87 also internally says "571 unrouted" then "511" in the same paragraph.)

**S2 — `terminology/README.md:191` stale on the staging default.** It says "Default destination is the staging path... Once migration is complete, change the default in `bin/term`'s `cmd_render` to `ROOT/'LEXICON.md'`." That flip has *already happened* (`bin/term:751` default = `ROOT / "LEXICON.md"`; LEXICON.md is live-generated). The README describes a pre-migration world.

**S3 — Continuity/Persistence taxonomy breakage still live.** LEXICON.md still renders `## Continuity` (line 46) with `### Continuity Stance` (48) and `### Persistence` (58) subgroups, PLUS a *duplicate* `### Persistence` (130) in the ELI section — the Moral Continuity dual-tag rendering §F flagged. The `continuity` entry still carries `subgroup: "Persistence"`, tag `continuity`, and notation `$\mathcal{C}_t$` (the collision with `chronica`'s `$\mathcal{C}_t$` §F named). All of §F's Breakage A and B are unremediated.

**S4 — Misleading mtimes on `msc/naming/` files.** `mini-lexicon-todo.md`, `naming-rename-plan.md`, `round-2-launch-prompt-v2.md`, and the `step-through-cycles/` dir show mtime 2026-07-02 08:54, but `git log` shows no content commits on/near that date (last real edits are much older). Almost certainly a checkout/branch touch, not editing activity. A next agent scanning by mtime would falsely read recent work here.

**S5 — TERMINOLOGY-TODO self-describes as "live execution queue" but is inert.** Nothing in §C–§F has moved since 2026-05-10. The `.integrated`-style discipline (remove rows when landed, CHANGELOG the batch) is documented but hasn't fired because no batches have landed. Not broken, but the "live" framing overstates current activity by ~2 months.

**S6 — `bin/rename-slug` bug #2 open.** Bare-filename `[text](OLD.md)` links not rewritten (TODO.md). Minor, graceful-failure class; flagged to land "before the next bulk slug-rename batch" which hasn't come.

---

## (e) Decisions genuinely blocked on Joseph

**J1 — The 13 held `to-canonicalize.md` rows (PRACTICA item 9).** Citability-fix specials (specification bound; epistemic-substate / purposeful-substate pair-row; "purpose"/"purposeful" register), Holling-collision adaptive-cycle handling, and — the one carrying `???` — **separability-triad-rung naming**: `separable core / structured repair / general open` vs Hintikka echo `definable / identifiable / non-identifiable` vs alternates (ties into `msc/separability-standalone-paper-proposal.md`). One-line context Joseph needs: *pick the three rung-names for the separability ladder; the Hintikka-echo triad is the leading candidate.*

**J2 — §F Continuity/Persistence reorg.** Explicitly gated: "This needs another opinion and a search of the relevant voting in `msc/naming/` before we take any action" (blocked since 2026-05-10, single Opus-4.7 corpus exploration). Bundled sub-decision: the Continuity-Stance *demotion* proposal (structural axis → deployment-level property) in `msc/domain-unification-2026-05-04/recommended-agent-ontology.md` / `msc/naming/mini-lexicon-todo.md` §13.11 — also pending second opinion. One-line context: *approve (or amend) the 5-step Persistence reorg + rule on whether Continuity Stance is a structural axis or a deployment-level property, after a second agent checks msc/naming voting artifacts.*

**J3 — §E agent-spectrum tetrad parallelism.** The interim `blind pursuer → blind seeker` swap (2026-05-17, overriding R2 decision #132 on new arguments) is in place, but the *full* four-name parallel set (`Reactive system` / `Blind seeker` / `Adaptive tracker` / `Actuated agent` mixes category-nouns and role-nouns) is deferred to a deliberate tetrad decision through `bin/term`. Joseph has a separate agent brainstorming option-sets. One-line context: *choose the four agent-spectrum quadrant names as one deliberately-parallel set (not another one-cell drive-by).*

**J4 — Greek-vocabulary path (A4).** Per-term, per-segment: tighten segment prose so each Greek distinction does formal work, vs soften the README claim to honest scope. Judgment call the audit surfaced but the voting cohort resisted. One-line context: *rule per Greek term whether the formalism earns the distinction (tighten segments) or it's pedagogical surface (soften README).*

*(J1–J4 are the calls that genuinely need Joseph. C5–C13, the 506-current routing mechanics, and NOTATION migration do NOT need him beyond the routing decisions already made / to be made in batches — the execution is agent-work.)*

---

## (f) Candidate meta-process definitions (raw material for a MECE hierarchy)

| # | Process | Trigger | Steps | Current health |
|---|---|---|---|---|
| MP-1 | **Terminology commitment** (`bin/term` store) | A name/term is decided canonical | `bin/term add <slug>` → populate frontmatter+body → `bin/term decide <slug> canonicalize --by joseph` → `bin/term render` → `bin/term lint` | **de-facto, healthy but idle.** Tool works; last fed 2026-05-11. Fed only when a decision arrives. |
| MP-2 | **Naming-cycle voting** (R1/R2 → aggregate) | Batch of unnamed/contested currents needs cross-architecture judgment | launch voter agents → `bin/naming-*-aggregate.rb` → score-card/detail/patterns artifacts | **complete/dormant.** Ran once (closed 2026-04-30); output (629 currents) is the undrained reservoir. |
| MP-3 | **Current routing** (curation pass) | Scored currents await disposition | read score-card batch (~12) → Joseph routes each to canonicalize/rename/add-alias/exclude/defer → record in `naming-rename-plan.md` + `master-list-curated.json` `rename_status` | **de-facto but STALLED.** Ran 2026-05-04 (118 of 629). 506 remain. The true bottleneck; gated on Joseph bandwidth. |
| MP-4 | **Decision execution** (routed → canon) | A routing decision exists but isn't in the store/segments yet | typing the entries (MP-1) + slug/prose sweeps (`bin/rename-slug`/`align-slug`) + CHANGELOG batch | **de-facto, STALLED at C5.** C1–C4 executed; C5–C13 (~40 already-routed entries) sit unexecuted, agent-doable now. |
| MP-5 | **Generated-view refresh** (LEXICON, future NOTATION) | Entries change | `bin/term render` (LEXICON: live); NOTATION: **no emitter exists** | **LEXICON: healthy/automated. NOTATION: aspirational/unstarted.** |
| MP-6 | **Taxonomy-consistency repair** (reorg/collision) | A corpus exploration finds a LEXICON/section taxonomy defect (e.g. §F) | findings doc → second-opinion gate → check `msc/naming/` voting → execute reorg | **broken/blocked.** §F stuck at the second-opinion gate since 2026-05-10; the one reorg attempt (`413e1c6`) went the wrong direction. |
| MP-7 | **Rename-propagation** (upstream churn → naming) | A framework-level rename (AAD→AAT, dir harmonize, GUC swap) | sweep slugs/prose/tags/formal-tags; update tools' hardcoded paths | **de-facto, reactive, mostly healthy.** Absorbs churn it doesn't originate; occasional fossils (rename-slug bug #1). |
| MP-8 | **Decision-surfacing** (the missing loop) | *should trigger:* Joseph has 20 min of routing bandwidth | *(does not exist)* — no mechanism hands Joseph a compact, context-reconstructed batch of the highest-leverage pending currents/decisions | **ABSENT.** This is the gap. MP-3 stalls because there is no MP-8 feeding it. Building it is the leverage-on-leverage move the whole review is about. |

---

## Cross-pollination / out-of-scope surfacings

- **The whole-review thesis is instantiated here cleanly.** This cluster is a worked example of "infrastructure ready, stalled on Joseph decision-throughput, no surfacing mechanism." MP-8 (decision-surfacing) is not naming-specific — every cluster with a "blocked on Joseph" queue needs the same thing. The naming program's 506-current reservoir + the `master-list-curated.json` `rename_status` schema is arguably the best *existing* substrate to prototype a general decision-surfacing/batching mechanism against, because the currents are already scored and structured.
- **`terminology/decisions/` is a reusable pattern for *any* Joseph-authority decision**, not just naming. Append-only, per-key, timestamped, `--by joseph`. If a project-wide "decisions Joseph made" ledger is wanted (the review's decision-routing concern), this store's design is the proven template.
- **NOTATION.md non-authoritative-by-construction is a live correctness risk** beyond naming: TODO flags the `ρ` gloss drifting from `#result-mismatch-decomposition`'s additive truth (2026-05-18). Symbol drift is a theory-correctness issue, not just a hygiene one; the NOTATION migration (A3) is filed as "lower priority" but its *absence* lets the reference file lie about the math.
- **The Greek-vocabulary finding (A4) is a genuine process-vs-process disagreement** worth flagging to whoever owns the epistemic-culture cluster: the naming *voting* process (synoptic, defended the Greek) and the *audit* process (incremental, found it doesn't do formal work) reached opposite verdicts on the same terms. That's a calibration signal about when to trust voting vs auditing, not just a naming call.

## Confidence

Firsthand-verified: entry/decision counts (`ls`/`find`), decision attribution and dates (filename parse), C5–C13 missing-entry status (per-term `test -f`), routing counts (JSON parse), `cmd_render` default and absent notation-verb (source read), LEXICON section state (grep), git-history dates/commits. NOT verified firsthand: the *quality/correctness* of the 108 canonicalize decisions themselves (I did not adjudicate whether each term is well-named); the full content of the R2 aggregator's scoring math; whether any of the 506 unrouted currents are secretly urgent (I sampled the status distribution, not each current). The July-2-mtime-is-not-real-edits claim is inferred from git-log absence, high-confidence but not proven (could be an uncommitted touch).
