# Drain of the external influx, first half

**KR G.2** (stranded additions landed at honest tier or set aside with a recorded reason), with the canon defects routed to **C.1** and the rest to the KR each serves. Top intent: *"Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself."* (Joseph, 2026-10-30). After a compaction, re-read `../INTENT.md` and then this file.

*Written by Claude Opus 5.5 (influx drain, first half), 2026-10-30, for the lead, who reads it whole, and for the integrators, who work from the ledger items it records. Sources: six regional files of the influx scout (`../influx-scout/`): `rewrites.md`, `rewrites-aux-canon-check.md`, `papers-may.md`, `neurips.md`, `logos-explication-ops.md`, `logos-explication-ops--ops.md`.*

## Method

- Every disposition is against canon at asf `main` HEAD (`cbd2f345` at start), not against the scout's row. Canon moved a great deal today (113 Volume 1 files changed since the scouts' `7ad5cd34`), so rows on changed segments were re-read by phrase at HEAD. Rows on segments unchanged since `7ad5cd34` keep the scout's "confirmed at HEAD" reading, and I say so.
- The scouts cite KRs from an earlier INTENT (KR1–KR5). I translate to the current tree (A–I): body defects → C.1 (cross-segment contradictions → C.3; open strengthenings outside C1–C3 → C.4); derived additions → G.2; argued, non-derived claims → G.0; citations and outward claims → F.2 / F.3; terminology → F.1 / F.4; front-door overclaims → A.2 / A.4; tracker phantoms → I.3; process and meta → I.
- Before every `vsect note` I checked `vsect open` for the statement. "Already in the ledger" is its own disposition, with the item named.
- Dispositions: **IN** (already in canon at HEAD, where), **DEFECT** (canon defect still present; ledger item), **ADD** (true or worth having, not in canon; ledger item at honest tier), **LEDGER** (already an open item; named), **ASIDE** (set aside, with the reason).

## Dispositions

Each line names the source row, the disposition, and the evidence. Item names are `vsect` items (`items/<slug>.md`).

### `rewrites-aux-canon-check.md` (read whole)

**Top items**

1. Vacuity rationale / untyped "unknown" (SP-30). **IN**: the A.1 rebuild removed the vacuity sentence from every body site; `#scope-adaptive-system` carries the typed target $S_t = (\Omega_t, \theta)$ and the future-stream predicate; `#def-action-transition:14-15`, `#def-observation-function:15,37` and `#deriv-recursive-update:19` (C2 now grounded in mediated access) are rewritten; `#example-kalman:31` now indexes the mode as $a_{t-1}$. Remaining A.1 findings are already in the ledger under `segment:scope-adaptive-system` (checks 4–6). Residue: `#def-action-transition:41` still says "acts via $T$" while the Kalman example's action enters only through $h$ (see unit 02 below); the WN figure gold at `#def-agent-environment:78` is already `review:items-recheck-t1#F8`.
2. What $\mathcal C_t$ is; the endowment. **DEFECT** → `influx-chronica-endowment-absorb-into-phi` (C.1). The session-boundary half is **IN**: `#obs-context-turnover:40` and `#scope-agent-identity:42` now say the trajectory runs through the store while the state is rebuilt.
3. IB Epistemic Status contradicts its body. *(below, unit 10)*
4. `#def-model-sufficiency:45` vs (C1)–(C3). *(below, unit 11)*
5. `#def-model-class-fitness:20` sup. *(below, unit 12)*
6. Condition 4 of `#scope-agency`. *(below, unit 06)*
7. Persistence "iff" on the front surfaces. The OUTLINE caption (`01-aat-core/OUTLINE.md:13`) is **IN** (now certificate voice). `INTRODUCTION.md:26` is a **DEFECT** → `influx-intro-anchor-sentences-outrun-bodies` (A.2), which also carries the same sentence in `#result-persistence-condition`'s Findings Brief (the Part I round-2 check's W9, so the Part I lane may already hold it).
8. Chapter-intro staleness. *(below, units 08, 13)*

**Per-segment**

- *00 INTRODUCTION.* :26 iff, :28 "identically" Lyapunov, :29 anchor 4 flat, :46 "theorems" over a discussion-grade home, :60 driver in snow recurs in no segment (grep of `01-aat-core/src/` for snow/wiper/windshield: none), :35 "before the call", :22 "acts on that world": all present at HEAD → **DEFECT** `influx-intro-anchor-sentences-outrun-bodies` (A.2). :27 GA-2S support: **IN** (`NOTATION.md:264` now states GA-2S as Wiener-driven). :50 EFE three restrictions → **DEFECT** `influx-active-inference-four-strengths` (C.4); the public `.zenodo.json` and README partial were corrected by the lead in 7b8ae8c6 after I flagged them, INTRODUCTION is with the Part I integrator. :58 "simulation validation": already E.2's KR text, not re-recorded. :39 self-actuation location: present, folded into nothing yet (see unit-00 residue below).
- *01 `#def-agent-environment`.* Vacuity: **IN**. $\Omega$ gloss "unobservable totality" in NOTATION: **IN** (no "unobservable" left in `NOTATION.md`). Internal state listed as a "channel" (:21-25) and no root for actuator noise: present, low stakes → recorded in `influx-ch1-root-residue` (below). 193847 F1 scope-completeness sweep: boundary integrity still WN-only (:88–101); low stakes, same item.
- *02 `#def-action-transition`.* Opacity atom: **IN** (:14-15). "Acts via $T$" (:41): **DEFECT**, `influx-ch1-root-residue`. Terminology gloss `transition-opacity.md:18`: **IN** (rewritten). THREAD-B stale gold (:60): **DEFECT** for I.5, in `influx-ch1-root-residue`. Constitutive atoms' eq-tag: low, already `spikes/PROPOSED.md`-imported.
- *03 `#def-observation-function`.* All five rows **IN** at HEAD: :37 "may not know" the kernel; lossiness "usual, not required" with a temporal-persistence condition (:15, :41); no "strictly lower-information" claim remains; `terminology/entries/epistemic-opacity.md` rewritten to the kernel; `#example-kalman:31` index fixed.
- *04 `#def-chronica`.* Endowment: **DEFECT** `influx-chronica-endowment-absorb-into-phi`. Non-forkability underived, factor (i) "exact": **DEFECT** `influx-non-forkability-tier` (C.1), which also carries the refuted fork-undetectability gold and SP-27's stale thesis (SP-27 is item `proposals-surfaced-2026-05-29-qualitative-gem-hunt-14e1`). "Time measured entirely in event ticks" (:18) vs the between-event flow: **DEFECT** `influx-event-time-seam` (C.1). Dead PROPRIUM paths in WN :44: present; WN-only, so not in `canon-bodies-cite-local-working-paths` (bodies only); recorded in `influx-ch1-root-residue`. LEXICON Continuity: **LEDGER** (the "Reorganize LEXICON's Continuity material" item).

## Adjacent findings

## What I read, sampled, and did not reach
