# Influx drain, second half

> **KR: G.2** in `../INTENT.md` (*stranded additions are landed at honest tier or set aside with a recorded reason*). Canon defects found here are routed to **C.1** (C.3 for contradictions between segments, C.4 for open strengthenings), argued and non-derived material to **G.0**, the strategy apparatus to **B.2**, terminology to **F.1/F.4**, citations to **F.2/F.3**. Top intent: *"Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself."* After a compaction, re-read `../INTENT.md`, then this file.

*Drain agent (Opus 5.5), 2026-10-30, for the lead (who reads this whole) and the integrators (who work from the ledger items it records). Sources: the influx scout's regional files `agent-core.md`, `agent-core-memory.md`, `agent-core-rest.md`, `arch-program.md`, `arch-program--proprium-ingest-corporeum.md`, `firmatum-vivarium.md`, `aisi-risk-notability.md`, `aisi-risk-notability--rest.md`, `periphery.md` (all in `../influx-scout/`).*

## Method

- Every disposition is checked against canon at asf `main` (`cbd2f345` when I started), not against the scout's row. The scouts checked at `5ade664d` (2026-08-24); about 270 commits landed today, and several defect sites had moved or been fixed.
- Before each item I checked `vsect open segment:<slug>` and grepped `items/` for the slug and key phrases. Where an item already existed I appended this drain's source to it (an "Also (influx drain, second half)" paragraph) instead of opening a twin.
- Following Joseph's instruction relayed by the lead, each item cites every source bearing on the same claim that I found (other regional files, canon Working Notes, audits, the sibling drain's regions), so the owners of those surfaces can mark their source "disposed with item:<id>".
- Item ids are the `items/<slug>.md` filenames. `--by drain-influx-2`.
- Dispositions: **IN** (in canon at HEAD, where), **DEFECT** (canon defect still present; item), **ADD** (true or worth having, not in canon; item at honest tier), **LEDGER** (already an open item; source appended), **MOOT** (overtaken by a landing today), **ASIDE** (set aside, with the reason).
- Helpers: one reads agent-core's seven unread `memory/research/` notes (`influx-2-memory-research.md`), one drains `firmatum-vivarium.md` and vivarium's `msc/` (`influx-2-firmatum.md`). A third, for `arch-program*`, was refused by the session's concurrency cap, so I am draining those myself.

## Dispositions per source item

### agent-core (`agent-core.md`, `agent-core-memory.md`, `agent-core-rest.md`)

| Source item | Disposition | Item / where |
|---|---|---|
| §4.6 / MAP D9: Brief "the loop is the only escape" in `#disc-constructive-impossibility-posture`, copied to `FINDINGS.md:222`, `CURRENT-VOL1.md:3442` | DEFECT (public surface; lead told at once, routed to the Part I round-3 lane) | `findings-brief-overclaim-on-public-surfaces-map` (C.1) |
| §4.1–4.2 / MAP D8: `#impl-strategy-dynamics:42` calls scope conditions (S1)–(S5) "boundary routes"; `:44` "shared escape mechanism" vs `#impl-strategy-structure:72` guard (2) | DEFECT, both present at HEAD | `impl-strategy-dynamics-contradicts-its-own-sourc` (C.1) |
| §4.3, §4.5: "load-bearing / structural requirement for recovering Part II persistence guarantees" in `#impl-scaffolded-logogenic:28` and its origin `#scope-scaffolded-logogenic:30`, against `#impl-orient-cascade:74`; with P16 (harness-velocity scaffold stratification) as the honest replacement, and memory B6 (the "REM sleep has a Shannon floor" type mismatch) in the same segment | DEFECT + ADD, one item | `the-scaffolding-overclaim-in-volume-3-its-origin` (C.1) |
| §4.7 / memory B1: $\lambda$ for log-odds and retention in one derivation; five-plus meanings; `NOTATION.md` lists one | DEFECT | `lambda-names-at-least-five-objects-in-canon-and` (F.4) |
| §4.8 / memory B2: CLS fast/slow swapped in (N1) | DEFECT (line 57 now) | `form-consolidation-dynamics-n1-assigns-the-store` (C.1) |
| memory A1, B7: body of `#form-consolidation-dynamics` asserts what its F74–F77 Working Note rejects; never cites `#der-multi-timescale-stability`; two catastrophic-forgetting accounts | DEFECT, with the strengthen route | `form-consolidation-dynamics-s-body-still-asserts` (C.1) |
| §4.4: hard-ceiling convention spike | MOOT: the hard ceiling was deleted by F72 (`5e621256`) | — |
| §2.B P5 / memory B5 / MAP D4: compensation-channel overreach, retrieval channel, generator drift | DEFECT, joined with arch 09-23 and logos 09-25 L1a | `der-compensation-channel-uniqueness-overreaches` (C.1) |
| P15 / memory B4 / §6 / P7 (theory half): no record-read operation in AAT's core | ADD (formulation, nothing derived) | `aat-s-core-has-no-operation-for-an-agent-reading` (G.2) |
| memory C1: `#def-mismatch-signal` normalizes by observation noise, `#form-composition-closure:318` by innovation covariance | DEFECT (C.3) | `def-mismatch-signal-normalizes-surprise-by-the-w` (C.3) |
| P1 / §5: what kind of claim each strategy-DAG segment makes; ascribed vs stored $\Sigma_t$ | ADD | `say-at-the-front-of-the-strategy-chapters-what-k` (B.2) |
| P2: type/token gap | ADD (gap in canon) | `the-strategy-dag-s-acyclicity-and-its-credence-l` (B.2) |
| P3: commitment state and commit criterion | LEDGER: appended to `proposals-d-4-sp-12-commitment-resource-temporal-d-1dea` | — |
| P8: objective vs terminal revision | DEFECT (conflation; motivating instance contested) | `form-structural-change-as-parametric-limit-s-ope` (C.1) |
| P4 + P9: explanation-dissolved aporia; node status as observation vs declaration | ADD (observation tier) | `what-registered-a-mismatch-and-what-settled-a-no` (G.2) |
| P10 + P14: channel typing; thinking as summary; typed harness channel | ADD (discussion-grade) | `why-a-chat-trained-llm-is-class-3-has-a-sharper` (G.2) |
| P13 (B2): forgetting as necessity vs latent diversity vs prerequisite | DEFECT (C.3) | `three-canon-passages-on-forgetting-point-differe` (C.3) |
| P13 (`#scope-agent-identity` vs `#obs-context-turnover`) | IN: `#scope-agent-identity:42` now states "*Not* excluded: a state discontinuity on one trajectory ... a session boundary" | — |

*(continuing)*

## What was read whole, sampled, not reached

*(being written)*

## Adjacent findings

*(being written)*
