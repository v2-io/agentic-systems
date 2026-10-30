# INTENT — the objectives tree

Every piece of work in this effort feeds one key result (KR) below, and every agent at every depth, and every successor after compaction, knows which one. Work that feeds none is a red flag: either the tree is stale, a finding is unrecorded, or the work has drifted. Say so to the lead; don't resolve it silently. The tree is set top-down *and* bottom-up, so propose KRs under the item you serve. This file stays a tree. Evidence lives in the artifacts it points to, history lives in commit bodies and `CHANGELOG.md`, and nothing in this directory records finished work.

## Top intent

> Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself. — Joseph, 2026-10-30

This serves *"TRUTH about agency … discovered, surfaced, truthified, truthfully synthesized and crossed to the right applications, AND effectively communicated anew."* His full frame is in `README.md`.

**Done means** that ASF says what is true about agency, only what its warrant supports, in a form a newcomer can follow and check.

**Working thesis** (moderate confidence; tested under B.3): *an agent must stay in honest contact with a world it cannot fully see; the price of that contact rises with success and with purpose; and the limits of what it can know from inside are where other agents, witnesses and designers enter.* Source: `owner-review/00-review.md` §6.

Objectives A–H come from the owner review (`owner-review/00-review.md` §7, ranked; A and B come first because the rest are judged by them). Objective I is the system that keeps all of this true.

## A — The front door says only what the bodies support

- **A.1** `#scope-adaptive-system` carries the typed predicate $H(S_t\mid\mathcal C_t)\gt0$ with $S_t=(\Omega_t,\theta)$, or a defended alternative, and the GA registry names $\theta$. A cold reader checks the membership clauses on standard RL and on a Kalman filter. This also resolves the SP-30 brief. · *not started*
- **A.2** INTRODUCTION, the Part I and Part II fronts and the README partials agree on one headline list. Each headline sentence traces to a body sentence of the same register. · *not started*
- **A.3** No live segment lacks an Epistemic Status (29 do today, all in the `impl-*`/intro layer). · *not started*

## B — Every load-bearing claim says what kind of claim it is, about which agents, and what would refute it

- **B.1** Every load-bearing apparatus has a record giving register, population, an instance where it is true, an instance where it is false, a falsifier, and whether it has been instantiated. Part II comes first, `form-objective-functional` is the template, and someone other than the author checks each record. · *not started*
- **B.2** Part II's apparatus is retyped to what it is: directed separation as definition + classification + estimator; the strategy DAG as formulation with its real agent-claims collected; the cascade as a lemma plus a norm. · *not started*
- **B.3** The purpose statement is the working thesis or a tested replacement. Two tests apply: the anchors test (every B.1 record states its claim in the thesis's terms without strain) and the cold-reader test (H.3). The uncertainty is resolved, not routed to Joseph. · *not started*

## C — The theory is correct where it is known wrong, and stronger where strengthening was found

- **C.1** Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier. The defect lists are `owner-review/integrator-items.md` A1–A15, `internal-surfaces/00-cross-surface-map.md` §3 and `influx-scout/MAP.md` §3. · *started: the hard ceiling (F72) is replaced; the rest are not started*
- **C.2** Strengthenings C1–C3 (exit time, loop identification, allocation vs distortion coupling) are independently checked, then landed or refuted. · *not started*
- **C.3** A cross-segment contradiction scan reports no open contradictions among load-bearing segments. · *not started*

## D — The arc has an owner and a trigger

- **D.1** A standing step, triggered whenever a result lands in any `src/`, re-derives the anchors, Part prefaces and headline lists from the record. · *not started*
- **D.2** No file hands work to a "standing cycle" or to an integrator that was never launched (seven such hand-offs exist, and three Aug-24 spikes are waiting). · *not started*
- **D.3** Every front-matter sentence that restates a result carries that result's slug, so a diff can check it. · *not started*

## E — One quantity is measured on an agent the theory did not construct

- **E.1** $\hat\kappa_{\text{processing}}$ and $\hat{\mathcal A}$ are run on two or three LLM families, comparing $W_1$ with $W_2$, under `empirica/`'s RUNS contract. Volume 3's $\kappa\approx1$ becomes a measured value or a range. · *not started*
- **E.2** One Part I quantity is estimated on a real adaptive system, or INTRODUCTION stops claiming simulation validation. · *not started*

## F — The lineage and evidence that exist reach the bodies, faithfully

- **F.1** Every verdict in `owner-review/explorers/terminology.md` §2 is landed: standard name plus citation at first introduction, renames through `bin/term`. · *not started*
- **F.2** The external research already found is cited where it belongs, as instances and tests and not only as precedence. Sources: `ref/prior-art-analysis/`, the Aug-22 landscape survey, the `ext:` rows of `spikes/PROPOSED.md`, and `internal-surfaces/` §6. · *not started*
- **F.3** Whatever crosses the canon boundary, in either direction, is faithful to its source. That means canon's citations of papers and data, and papers' and notes' claims about canon (`influx-scout/MAP.md` D12, D13, D17). · *not started*
- **F.4** The naming SOP asks "does this already have a name elsewhere?" before Criterion 9, and every index family is declared once in `NOTATION.md`. · *not started*

## G — What was derived but never assembled is assembled

- **G.0** It is decided where argued, non-derived claims live (ASF segments or logos), before any of them lands. The input is Joseph's upstream-first principle of 2026-09-25. · *not started*
- **G.1** Two units are assembled at chapter grade, each with a B.1 record: the price-of-confidence thesis, and the four treatments of law. · *not started*
- **G.2** Stranded additions are landed at honest tier or set aside with a recorded reason. They are the coupled-agent spike claims, the AISI applied material, and the mapped influx (`influx-scout/MAP.md`, `internal-surfaces/`). · *not started*
- **G.3** Theory-bearing material that exists only uncommitted on disk gets a durable home before anything depends on it (`influx-scout/MAP.md` §5). · *not started*

## H — The reading surface is a spine, not a second text

- **H.1** Outline claim cells are one line each. Their paragraph content moves to the missing chapter intros or into bodies. · *not started*
- **H.2** Dependency graphs are regenerated on every build, or removed. The stage ladder leaves the outline display. Every OUTLINE row has a file or an honest mark, and every `old-*` file has a fate. · *not started*
- **H.3** Comprehension is measured before and after on the same chapters, with fresh readers. · *not started*

## I — The system keeps it true (the lead's part)

- **I.1** This tree stays true and lean, and every agent at every depth knows its KR. · *lead*
- **I.2** The checks fire without a person. A tracked `.githooks/` runs `md-press --check`, `bin/lint-outline`, `bin/check-links` and `bin/refresh-all --check` on every commit and refuses failures, after the existing debt is cleared (68 files, 10 outline violations). · *not started*
- **I.3** One open ledger, keyed by claim: every open item carries slug, kind, resolver and date, and every target resolves. The thirteen trackers, the index files, the proposal files, ROUTING and the decision briefs are folded into it or deleted. · *not started*
- **I.4** Standing is read from recorded checks, not typed: a checks ledger (slug, text hash, who, criterion, outcome), with a lint that flags a changed body whose last check is older. F72 is the first row. · *not started*
- **I.5** Working Notes carry forward pointers and regression guards only. Items are classified by kind and sent to their homes, and lifting audit gold into Working Notes stops. · *not started; seed in `internal-surfaces/wn-ledger-seed/`*
- **I.6** The always-loaded surface says only what tools cannot check. Tool-enforced rules leave the prose, derivable parts are generated, and every SOP passes md-press. A two-launch probe measures the effect rather than asserting it. · *not started*
- **I.7** Front surfaces are bound to the record: each restated sentence carries its slug, and a diff fails when the cited body has changed. · *not started*
- **I.8** The effort's own residue drains. Its map and review directories delete when their items are in canon or the I.3 ledger, and no new tracker file is created. · *not started*

Source for I.2–I.8: `system-review/00-system.md` §7. Its test for every mechanism is *does it fire without a person remembering?*

## Who is on what

| Who | KR | Writes to |
|---|---|---|
| Lead coordinator (Opus 5.5, session "asf-cleanup") | I, plus coordination | `INTENT.md`, `HANDOFF.md` |
| A.1 integrator (Opus): the typed epistemic target | A.1 | `#scope-adaptive-system`, the $\theta$ registry, and its dependents |
| C.1 integrator (Opus): the polytree theorem | C.1 (integrator-items A1, A9) | `#def-strategy-dag`, `#deriv-graph-structure-uniqueness`, `example-L1` |
| vsect MVP builder (Fable), with ASF as the first corpus | I.3, I.4 | `~/src/arch/firmatum/utils/vsect/` (or where it settles) |
| Hooks builder (Opus) | I.2 | `.githooks/`, the tool fixes, debt outside canon (canon after the integrators land) |

These are finished and on the line through the lead:

- the owner review (Fable) and its seven subagents;
- the system review (Fable);
- the influx scout;
- the internal-surfaces mapper;
- the F72 verifier;
- the F72 integrator.

## Using this file

- **Briefing an agent:** name its KR and quote the top intent. Ask it to pass its KR down to any agent it launches.
- **Writing an artifact:** put its KR at the top.
- **After a compaction:** read this file, then `HANDOFF.md`.
- **Revising the tree:** each KR stays one line plus its status and where its evidence lives. When a KR is met, its line goes and the history goes into the commit body.
