# INTENT — the objectives tree

Every piece of work in this effort feeds one key result (KR) below, and every agent at every depth, and every successor after compaction, knows which one. Work that feeds none is a red flag: either the tree is stale, a finding is unrecorded, or the work has drifted. Say so to the lead; don't resolve it silently. The tree is set top-down *and* bottom-up, so propose KRs under the item you serve. This file stays a tree. Evidence lives in the artifacts it points to, history lives in commit bodies and `CHANGELOG.md`, and nothing in this directory records finished work.

## Top intent

> Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself. — Joseph, 2026-10-30

This serves *"TRUTH about agency … discovered, surfaced, truthified, truthfully synthesized and crossed to the right applications, AND effectively communicated anew."* His full frame is in `README.md`.

**Done means** that ASF says what is true about agency, only what its warrant supports, in a form a newcomer can follow and check.

**Working thesis** (moderate confidence; tested under B.3): *an agent must stay in honest contact with a world it cannot fully see; the price of that contact rises with success and with purpose; and the limits of what it can know from inside are where other agents, witnesses and designers enter.* Source: `owner-review/00-review.md` §6.

Objectives A–H come from the owner review (`owner-review/00-review.md` §7, ranked; A and B come first because the rest are judged by them). Objective I is the system that keeps all of this true.

## A — The front door says only what the bodies support

- **A.1** `#scope-adaptive-system` carries the typed predicate $H(S_t\mid\mathcal C_t)\gt0$ with $S_t=(\Omega_t,\theta)$, or a defended alternative, and the GA registry names $\theta$. A cold reader checks the membership clauses on standard RL and on a Kalman filter. This also resolves the SP-30 brief. · *landed; the eighth independent read (`spikes/epistemic-target-ontology/17-check-8.md`) re-derived every membership item at 3d17de13 and found it holds. Owed an integrator: its F1 (a sufficient condition that settles continuous-state RL, the KR's own RL case) and F2–F5 (sentence and definition fixes in the scope, `#def-observation-function`, `#def-action-transition` and Prop 1(ii)). Open in the ledger: the tail-$\sigma$-field strengthening, the physical housing, the compute-relative extension, and where design ends and learning begins*
- **A.2** INTRODUCTION, the Part I and Part II fronts and the README partials agree on one headline list. Each headline sentence traces to a body sentence of the same register. · *landed at 327637ac: INTRODUCTION, the Part I front and the README partials carry nine headlines at their bodies' registers, each with its slugs (`a2-front-door/headline-trace.md`: 16 mismatches in 28 front sentences). The Part II preface (:80) is traced, not changed. Unchecked by a second mind. The mechanical half (a `front` record kind in vsect, `bin/check-headlines`) is specified, not built*
- **A.3** No live segment lacks an Epistemic Status (29 do today, all in the `impl-*`/intro layer). · *not started*
- **A.4** The Volume 2–4 prefaces and OUTLINE claim cells say only what their bodies support (A.2 covers Volume 1). · *not started; the overclaims the item re-checks found are in `items-recheck/t2-todo.md` §2*

## B — Every load-bearing claim says what kind of claim it is, about which agents, and what would refute it

- **B.1** Every load-bearing apparatus has a record giving register, population, an instance where it is true, an instance where it is false, a falsifier, and whether it has been instantiated. Part II comes first, `form-objective-functional` is the template, and someone other than the author checks each record. · *Part II's records landed and checked; Part I's persistence family (seven segments) has records at 327637ac, unchecked, with six over-reaching statements filed as items and not fixed; the rest of Part I and Part III have none*
- **B.2** Part II's apparatus is retyped to what it is: directed separation as definition + classification + estimator; the strategy DAG as formulation with its real agent-claims collected; the cascade as a lemma plus a norm. · *not started*
- **B.3** The purpose statement is the working thesis or a tested replacement. Two tests apply: the anchors test (every B.1 record states its claim in the thesis's terms without strain) and the cold-reader test (H.3). The uncertainty is resolved, not routed to Joseph. · *not started*

## C — The theory is correct where it is known wrong, and stronger where strengthening was found

- **C.1** Every verified defect is replaced, each by an integrator who re-ran the check and then by an independent verifier. The defect lists are `owner-review/integrator-items.md` A1–A15, `internal-surfaces/00-cross-surface-map.md` §3 and `influx-scout/MAP.md` §3. · *lanes stopped 2026-10-31 at Joseph's word; accounts in `c1-lanes/`. Part I round 5, defender-noise round 2, Volume 4 round 4 and Part II round 2 are merged without their checks. Of ten corrected sites traced against the tag, about half were sentences an earlier round wrote the same day. Several integrators derived and landed new results themselves (the threshold expansion's third term, P4, A.1's clause extensions), against the spike template's spiker ≠ verifier ≠ integrator separation*
  - **Integrator continuity** (Joseph, 2026-10-31). A checker is always a mind other than the author. The checker's findings go back to the original integrator; a new integrator only when the original is gone, briefed with its account
- **C.2** Strengthenings C1–C3 (exit time, loop identification, allocation vs distortion coupling) are independently checked, then landed or refuted. · *C1 landed and checked: the threshold drift is a derived three-term expansion, re-derived by hand by the round-4 checker. C2 and C3 landed and checked (`part-ii-check-1.md`); the Part II round-2 integration is running*
- **C.3** A cross-segment contradiction scan reports no open contradictions among load-bearing segments. · *not started; one found: `#scope-composite-agent` admits composites with no composite objective (routes C-iii, C-iv) while requiring one (:83), and eight segments rest on that gate (`items-recheck/q-proposals.md` §2.1)*
- **C.4** Part III and the open strengthenings outside C1–C3 have an owner: each held item under C is landed, refuted, or set aside with its reason recorded. Worked by cluster: strategy-DAG optimality; composition and closure; persistence extensions; the impossibility clusters; the coupling typology (the 01 Working Notes drain alone filed 74 items here, and the clusters show in their slugs). · *not started; the items are in the ledger, most `unassigned` today; inputs `items-recheck/q-proposals.md` §2, `t2-todo.md` §2*

## D — The arc has an owner and a trigger

- **D.1** A standing step, triggered whenever a result lands in any `src/`, re-derives the anchors, Part prefaces and headline lists from the record. · *not started*
- **D.2** No file hands work to a "standing cycle" or to an integrator that was never launched (seven such hand-offs exist, and three Aug-24 spikes are waiting). · *not started*
- **D.3** Every front-matter sentence that restates a result carries that result's slug, so a diff can check it. · *not started*

## E — One quantity is measured on an agent the theory did not construct

- **E.1** The fixed-gain tilt hypothesis of `#scope-observation-ambiguity-modulation` is tested on two or three LLM families, comparing $W_1$ with $W_2$, under `empirica/`'s RUNS contract: the processor gain $\lambda$ is estimated against outcome ground truth or a reference posterior at several levels of evidence sharpness, and whether it stays fixed is answered. $\hat\kappa_{\text{processing}}$ is reported beside it as a different quantity, so Volume 3's $\kappa\approx1$ becomes a measured value or a range. · *not started*
- **E.2** One Part I quantity is estimated on a real adaptive system, or INTRODUCTION stops claiming simulation validation. · *not started*
- **E.3** One of Volume 2's cheap falsifiers is run on a real codebase history (`item:tst-cheap-falsifiers-and-measurement-design`); the owner review ranks them the cheapest in the estate. · *a pre-registered survival analysis of source-file lifetimes in ten repositories ran (`e3-measurement/account.md`, `empirica/software-file-lifetimes/`). Its unit, a file's deletion, is not the claim's, a system's remaining feature count, so it tests nothing `#der-change-expectation-baseline` states. Not in canon; the KR is unmet*

## F — The lineage and evidence that exist reach the bodies, faithfully

- **F.1** Every verdict in `owner-review/explorers/terminology.md` §2 is landed: standard name plus citation at first introduction, renames through `bin/term`. · *not started*
- **F.2** The external research already found is cited where it belongs, as instances and tests and not only as precedence. Sources: `ref/prior-art-analysis/`, the Aug-22 landscape survey, the F.2 items in the vsect ledger, and `internal-surfaces/` §6. · *not started*
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
- **H.4** Pedagogy gold has a home with Joseph as test reader: a surface outside segment bodies, keyed by slug and chapter order, fed by first-encounter reflection gold, the in-order summaries and the quiz corpus, where each entry records whether Joseph has read it and whether it reached a body; the reader-clarity gaps auditors named ("Readers often ask") are answered in the bodies where they arise, not logged. · *not started; inventory on `item:pedagogy-home-for-lifted-audit-gold`, proposed bottom-up by the gold and audits drains*

## I — The system keeps it true (the lead's part)

- **I.1** This tree stays true and lean, and every agent at every depth knows its KR. · *lead. 85 open ledger items name no KR as owner (`vsect` dashboard): each is placed under a KR, a new KR is proposed for it, or it is set aside with its reason*
- **I.3** One open ledger, keyed by claim: every open item carries slug, kind, resolver and date, and every target resolves. The thirteen trackers, the index files, the proposal files, ROUTING and the decision briefs are folded into it or deleted. · *started: every imported tracker item is judged and twelve trackers are gone; TODO.md waits for I.5, PRACTICA.md for I.8*
- **I.9** Every backlog surface is drained into the ledger, one disposition per source item: the external influx (`influx-scout/` regional files and the two unscouted regions), `audits/`, live `spikes/`, Working Notes and `msc/`. Each item is already in canon, a ledger item under the KR it serves, or set aside with its reason. Each item drained is checked against every other surface (audits and their gold, adjacent Working Notes, spikes, `msc/`, the influx and its primaries); related material is disposed with it or joins the same ledger item, one item per thing with all its sources. Integrators take work from the ledger, and new findings attach to an existing item rather than duplicating it. · *drains ran over every surface they were pointed at; the dispositions rest on the scouts' rows, and nothing records which files were read. The planted canary failed: vivarium's `LEXICON.udon` (its kingdom, law and participation ontology, 690 lines) and its `def-nomos`, `form-lawful-steering`, `def-in-vivia` were never read by any scout or drain. Item sources are prose, not a queryable field, so what was not drained cannot be listed*
- **I.10** Signal rises against noise, measured. On a fixed sample of claims, count the live places outside the segment body and its ledger items where something about the claim is written (Working Notes items, spikes, audit files, `msc/`, influx), and how much of each a cold agent must read to learn what is known and what is open. Measure at the tag and after each drain wave. The aim, Joseph's: future agents should not spend hours working out whether a change supersedes what was written elsewhere or was ignorant of it. · *baseline taken (`i10-signal/measurement-2026-10-30.md`): a cold agent's total reading per claim is about the same at 5eee086c as at the tag (+0% / −3%, 244 claims); 60% of the new coverage is named only in `drain/`, nothing was retired, and 94% of net new places are this effort's own files. Not calibrated against real cold reads*
- **I.4** Standing is read from recorded checks, not typed: a checks ledger (slug, text hash, who, criterion, outcome), with a lint that flags a changed body whose last check is older. · *started: vsect records checks bound to their basis, shows lapses (and `✓~` where only an unread upstream changed), re-binds them by a second mind's `confirm` (scoped with `--checks`, or `--all` when the reach crosses segments), and carries intent claims. 148 rewordings await a second mind (247 lapsed checks); a confirmer pass follows the current merges*
- **I.5** Working Notes carry forward pointers and regression guards only. Items are classified by kind and sent to their homes, and lifting audit gold into Working Notes stops. · *not started; seed in `internal-surfaces/wn-ledger-seed/`*
- **I.6** The always-loaded surface says only what tools cannot check. Tool-enforced rules leave the prose, derivable parts are generated, and every SOP passes md-press. A two-launch probe measures the effect rather than asserting it. · *not started*
- **I.7** Front surfaces are bound to the record: each restated sentence carries its slug, and a diff fails when the cited body has changed. · *not started*
- **I.8** The effort's own residue drains. Its map and review directories delete when their items are in canon or the I.3 ledger, and no new tracker file is created. · *not started*

Source for I.3–I.8: `system-review/00-system.md` §7. Its test for every mechanism is *does it fire without a person remembering?*

## Who is on what

No agents are running. No new agents launch until Joseph says so (2026-10-31). Next: a review with him of everything since the tag, keep against mislead.

| Who | KR | Writes to |
|---|---|---|
| Lead coordinator (Opus 5.5) | I.1, and the review with Joseph | `INTENT.md`, `HANDOFF.md` |

## Using this file

- **Briefing an agent:** name its KR and quote the top intent. Ask it to pass its KR down to any agent it launches.
- **Writing an artifact:** put its KR at the top.
- **After a compaction:** read this file, then `HANDOFF.md`.
- **Revising the tree:** each KR stays one line plus its status and where its evidence lives. When a KR is met, its line goes and the history goes into the commit body.
