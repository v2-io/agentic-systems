*Objective **I** of `../INTENT.md`. Companion to `00-system.md`: every count cited there, with the command that produced it. Run 2026-10-30 at asf HEAD `5b6cdee5` from the repo root unless a path says otherwise. This file deletes with its companion.*

# Measurements behind the system review

## Mass: theory versus the record around it

`for d in $(git ls-files | cut -d/ -f1 | sort -u); do echo "$d $(git ls-files "$d" | grep '\.md$' | xargs cat | wc -l)"; done` (tracked markdown lines by top-level directory):

| Directory | md lines | What it is |
|---|---|---|
| `01-aat-core` | 25,301 | theory + OUTLINE (173 live segments) |
| `02-tst-core` | 25,955 | 29 live segments ≈ 3.5k lines; `old-tst-*` 7,739; `lit-review/` ≈ 14.4k |
| `03-llm-core` | 2,235 | 23 live segments |
| `04-eli-core` | 2,166 | 22 live segments |
| `audits` | 80,291 | 1,557 files; 24 `AUDIT-WORKING-*` dirs |
| `spikes` | 80,649 | 382 files |
| `.archive` | 51,037 | |
| `empirica` | 34,421 | 5,141 files, almost all the halted glyph study |
| `msc` | 25,443 | 375 files |
| `terminology` | 6,234 | |
| `doc` | 5,226 | of which `doc/sop/` 2,947 |
| root trackers | ≈ 2,100 | TODO 525 · PROPOSALS 442 · FORMAT-TODO 225 · BIBLIOGRAPHY-TODO 185 · PRACTICA 121 · TERMINOLOGY-TODO 104 · INTEGRATION-CLEANUP-TODO 86 · TODO-big-picture 64 · TST-IDEAS 450 |
| `CHANGELOG.md` | 1,527 | |

Live segments: 246 (`*/src/*.md` minus `old-*`), 30,627 lines; `## Working Notes` present in 236, totalling 5,284 lines (17% of segment text). The script:

```python
import glob, os, re
tot = n = segs = allL = 0
for vol in ['01-aat-core', '02-tst-core', '03-llm-core', '04-eli-core']:
    for f in glob.glob(f'{vol}/src/*.md'):
        if os.path.basename(f).startswith('old-'):
            continue
        t = open(f).read()
        segs += 1
        allL += len(t.splitlines())
        m = re.search(r'^## Working Notes\s*\n(.*?)(?=^## |\Z)', t, re.S | re.M)
        if m:
            n += 1
            tot += len(m.group(1).splitlines())
print(segs, n, tot, allL, round(100 * tot / allL))
```

Record outside the theory trees (audits + spikes + msc + .archive + doc + terminology + trackers + CHANGELOG): ≈ 253k lines against ≈ 25k lines of segment body (segments minus Working Notes), about ten to one.

## Activity

`git log --since=M-01 --until=M-31 --format=%h | wc -l`, then the same with `-- '0*/src/*.md'` (theory) and with the governing set `doc bin TODO.md PROPOSALS.md PRACTICA.md FORMAT-TODO.md INTEGRATION-CLEANUP-TODO.md BIBLIOGRAPHY-TODO.md TERMINOLOGY-TODO.md CLAUDE.md spikes/INDEX.md spikes/ROUTING.md audits/STATUS.md`; distinct `Claude-Session:` trailers per month.

| Month | commits | theory src | governing | sessions |
|---|---|---|---|---|
| 2026-03 | 111 | 2 | 28 | 0 |
| 2026-04 | 317 | 153 | 119 | 0 |
| 2026-05 | 527 | 203 | 233 | 0 |
| 2026-06 | 49 | 12 | 29 | 1 |
| 2026-07 | 80 | 34 | 47 | 9 |
| 2026-08 | 85 | 23 | 25 | 4 |
| 2026-09 | 7 | 0 | 0 | 2 |
| 2026-10 | 421 | 2 | 10 | 6 |

Theory-tree commits after 2026-08-24: two, both today (`5e621256`, `97179f6f`, the F72 landing). Of October's 421 commits, 398 are the glyph study (relayed from `internal-surfaces/00-cross-surface-map.md` §1; my own count of commits touching only `empirica/glyph-sequence-perception/` was not re-run). The session trailer was adopted mid-year, so the 0s in April and May are absence of the trailer, not absence of sessions.

Trailers across all 1,587 commits (`git log --format=%B | grep -cE '^Role:'` etc.): `Role:` 24 · `Claude-Session:` 573 · `Co-Authored-By:` 1,386. Committer identity: one (`git shortlog -sn HEAD`: 1,586 Joseph A Wecker, 1 Claude Opus 4.7).

## Checks: which exist, which run, what they say today

- `bin/check-links` → `886 doc-nav links across 1610 files all resolve`, exit 0.
- `bin/refresh-all --check` → `All generated outputs are current`, exit 0 (FINDINGS.md, README.md, README-auditor.md, three readme partials).
- `bin/lint-outline` (all four volumes) → exit 1. 01: 1 ordering violation (`impl-persistence-and-limits` → `result-per-dimension-persistence`, open since 2026-05-22), 16 accepted, 71 backmatter refs, 0 missing deps. 03: 5 ordering violations, 5 missing dependencies (`der-self-referential-closure`, `def-cognitive-fusion`, `obs-backward-inference-empathy`, `form-structured-rich-context`, `der-active-salience-management`), 30 outline rows for 23 files. 04: 4 ordering violations, 35 rows for 22 files. The ten ordering violations are the same ten `msc/decision-briefs-2026-07-15.md` listed on 2026-07-15. Stage distribution across 246: draft 203 (131+22+22+… per volume output), unknown 21.
- Outline rows marked `missing` whose file exists (grep of the `missing` cells against `src/`): `03-llm-core: scope-observation-ambiguity-modulation`; `04-eli-core: def-identity-sufficiency`, `der-identity-continuity-threshold`.
- `md-press -q --no-math --no-log *.md 0*/src/*.md 0*/OUTLINE.md doc/sop/*.md doc/sop/*/*.md spikes/*.md audits/*.md` → exit 1, 68 files would change: 12 root trackers and generated files (incl. `FORMAT.md`, `NOTATION.md`, `LEXICON.md`, `FINDINGS.md`, `CURRENT-VOL1*.md`), 11 live `01-aat-core` segments, 11 `old-tst-*`, 2 in 03, 3 in 04, `01-aat-core/OUTLINE.md`, **8 of the 13 SOP files** (`build-pipeline`, `format`, `git-hygiene`, `multi-agent`, `naming`, `sop-creation`, `spikes`, `audit.sop/routing`), 14 spikes, 7 audit files. The command reproduces the list. The SOP count was re-run at hand-off (12:49 MDT, after another agent had edited `format.sop.md` in the working tree): the same eight.
- Hooks: `git config core.hooksPath` is empty; `.git/hooks` holds only samples; no `.githooks/` has existed in history (`git log --all -- .githooks` is empty). `CHANGELOG.md` 2026-10-30 records that `core.hooksPath` pointed at a retired path until today, so no hook has run since that path was retired; whether any ran before is not recoverable from the repo.
- `.claude/` is gitignored (`.gitignore:7`); it holds `settings.local.json` and `worktrees/` only.

## The status field (the census, and what I re-checked)

Source: `~/src/aat-refactored/spikes/fresh-view-2026-09-29/census-findings.md` (Opus 5.5, at asf `a3db02e`). I did not re-run its scripts; the F1 counts match the frontmatter counts the lead took this morning (`../README.md`), and no theory tree changed between `a3db02e` and today except F72. Its findings I rely on: 32 in-place `status:` changes in seven months; a review's four rulings committed as four different values (0 of 4); `der-recursive-update` flipped exact → conditional → exact over an unchanged Epistemic Status; an audit-flagged overclaim took 80 days to reach the field; the one refutation got `status: false`, outside the vocabulary; securing acts (re-derivation, independent verification, ratification) appear in prose in 4 of 25 sampled sections and in the frontmatter never; $H(\text{status} \mid \text{type}) = 1.22$ bits of $H(\text{status}) = 2.45$; definitions spread over seven status values.

## Trackers

Open checkboxes (`grep -c '^\s*- \[ \]'`): TODO 42 · PRACTICA 38 · INTEGRATION-CLEANUP-TODO 15 · FORMAT-TODO 14 · TERMINOLOGY-TODO 2 · TODO-big-picture 1 · PROPOSALS 0 · TST-IDEAS 0. Checked boxes anywhere: 0. TODO's "Last reconciled" line: 2026-08-22. Date stamps in TODO by month: 2026-04 ×26, 05 ×94, 06 ×9, 07 ×14, 08 ×14.

Slug references (`#slug-name` tokens) that name no file in any `src/`, per tracker: TODO 15 of 94; PROPOSALS 11 of 76; `spikes/INDEX.md` 15 of 149; TST-IDEAS 15 of 34; PRACTICA 1 of 4; `spikes/ROUTING.md` 2 of 6; `spikes/PROPOSED.md` 2 of 30. Two kinds are mixed in those numbers and the script does not separate them: planned segments that FORMAT says may be forward-referenced (`def-cognitive-fusion`, `der-wrapper-persistence-condition`, …) and stale names of segments that were renamed or never created (`additive-coordinate-forcing`, `separability-ladder`, `sector-condition`, `dissipativity-template`, `rho-decomposition`, `posterior-displacement-template`, `deriv-strategic-persistence-hard-ceiling`, deleted today). A path-resolution pass in the same script was run repo-root-relative, so its counts overstate for files that use paths relative to their own directory (`spikes/INDEX.md`, `audits/STATUS.md`); I do not cite them.

Gate words outside the history layers (`grep -rlE "Joseph-reserved|awaiting go-ahead|external-eye gate|awaiting Joseph|Joseph batch"`, excluding `.integrated`, `.archived`, `.routing-trail`, `.archive/`, CHANGELOG, this effort's directory, the July review and the gem-hunt trail): 26 files.

Hand-offs to "the standing cycle" (`grep -rl "standing cycle"`, same exclusions): 10 files, resolved by reading each line:

| File | What is handed off | Does the named destination hold it |
|---|---|---|
| `spikes/spike-partition-isolation-criterion-2026-07-28.md:388` | three TST landing recommendations, "the landing calls are Joseph's" | no tracker row; `spikes/INDEX.md:48` repeats the hand-off |
| `spikes/spike-tst-independent-derivations-2026-07-04.md:138` | a candidate 02-tst-core cluster, "each needs its own derivation-or-adoption pass" | `TODO.md` §2026-07-04 names the spike; no item per candidate |
| `spikes/spike-prospective-mood-two-channel-borrowing-2026-06-17.md:90` | "Open remainder (released to the standing cycle)" | nothing names it outside INDEX row 88 |
| `spikes/spike-honest-activation-2026-09-23/03-derivations.md:135` | the escape condition in closed form | not in INDEX at all (the spike has no row) |
| `spikes/INDEX.md:48,64,88` | the three above, restated | the INDEX is the destination it points at |
| `msc/deaths-grounding-plan-2026-06-10.md:30,39` | the derivation remainder and the norm segment | `TODO.md` §"Deaths taxonomy" carries the items; that section is dated 2026-06-17 and untouched since |
| `msc/wn-discipline-coherence-pass-2026-05-31.md:44` | the proposal that WN items be routed at write time | proposed 2026-05-31, "not yet adopted" per `INTEGRATION-CLEANUP-TODO.md` |
| `doc/sop/spikes.sop.md` §0c, `doc/sop/audit.sop/routing.sop.md` Refinement 5 | the definition of the standing cycle: "TODO / PROPOSALS / the audit cycle / the Joseph-reserved queue" | the queue is retired (`JOSEPH-TODO.md` deleted today); the audit cycle has no trigger; TODO is unreconciled since 2026-08-22 |

The phrase names a set of trackers, and the trackers are where items go to wait. Nothing reads them on a schedule; the last reconciliation of TODO (2026-08-22) was two days before the last theory commit before today (`5ade664d`, 2026-08-24).

## The auto-loaded surface

`wc -l`: global `~/.claude/CLAUDE.md` 812 · `~/src/CLAUDE.md` 3 (imports) · `~/src/arch/AGENTIC-DELEGATION.md` 227 · `~/src/arch/CLAUDE.md` 28 · `doc/sop/agents.sop.md` 326 (= `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`) · project `MEMORY.md` 138. Total loaded into every asf session before a word of work: 1,534 lines. On demand: `doc/sop/` 2,947 lines, of which `format.sop.md` 611, `audit.sop/de-novo.sop.md` 702, `audit.sop/routing.sop.md` 409, `spikes.sop.md` 355 (its last 90 lines are ten appended "Refinement" paragraphs).

## The self-reviews of the system, in order

- 2026-03-14 — project memory of the `act` repo: "too much generative breadth, not enough convergent depth"; proposed a 3:1 promote-to-create ratio (relayed from `influx-scout/MAP.md` §9).
- 2026-05-19→20 — `INTEGRATION-CLEANUP-TODO.md` opened (the canon-cites-only-canon principle; F6 "CLAUDE.md as unreviewed amplifier", still open).
- 2026-06-01→02 — `msc/sop-consolidation-design-2026-06-01.md`; `doc/sop/` created.
- 2026-07-07 — `msc/meta-process-review-2026-07-07/`: ten agents, `PROCESS-MAP-v0.udon` (every process tagged by health), `DECISIONS-CENSUS.md`. Header: "Working artifact; not committed until Joseph reviews the direction." It is tracked.
- 2026-07-15 — `msc/decision-briefs-2026-07-15.md`, the valve: ten briefs; the trackers map found almost none decided in 3.5 months.
- 2026-07-22, 08-14, 09-29, 10-28 — outside asf: udon's TST-extension memo, verisectorium, aat-refactored's census, aat-v3's `vsect` (relayed, `influx-scout/MAP.md` §6).
- 2026-10-30 — `owner-review/00-review.md` §4, `internal-surfaces/00-cross-surface-map.md` §8, `influx-scout/MAP.md` §6, `system/01-epistemic-machinery-in-place.md`, and this.

## One landing, measured as a process (F72, today)

Files: `spikes/spike-strategic-persistence-hard-ceiling-convention-2026-05-31-verify-1.md` (161 lines) and `…-verify-1-integration-notes.md` (60 lines); three commits; two new propositions, one deleted segment, one new segment, edits at 12 sites in one meta-segment, OUTLINE, TODO, INDEX, CHANGELOG. The verifier re-derived from the recurrence as written and found the May verification had "checked the formula against itself"; the integrator re-derived the allocation cap by a second route and ran an exact mean-lag simulation; the notes record who checked which section, where the work order undercounted carriers (12 sites, not 3), and what was deliberately not changed. The record of those checks exists only in the two spike files; no segment or field says the landing was re-derived by two agents.
