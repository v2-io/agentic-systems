# Findings — cluster 02: audit-and-spike-lifecycle

*Meta-process review, 2026-07-07. All counts and states verified first-hand against the working tree and git history on this date, not relayed from trackers. Where a tracker claim and the tree disagree, both are reported.*

## Headline

The audit and spike *lifecycles* are healthy and genuinely enacted. What is broken is the **terminal stage** (audit graduation / working-dir clearing) and its influx-companion (the gold-lift), both of which depend on a Joseph-only gate that has been released once and then only partway. Net effect: **0 of 22 `AUDIT-WORKING-*` gold dirs have graduated**, the gold-lift sweep **stalled after 17 of ~25 batches on 2026-05-31 and has not moved in ~5 weeks**, and the single decision that would unblock the largest cleanup (**D-2, the bulk-64 wipe**) is the only item on `JOSEPH-TODO.md`'s "needs your decision" list and is **untouched — `.integrated/` (127 entries) and `.archived/` still exist; the 2026-05-19 wipe never happened**.

---

## (a) De-facto processes actually running — and their health

### A1. Spike lifecycle — HEALTHY (de-facto, well-exercised)

Trigger: any question needing exploration (friction-free launch — "go ahead and spike it").
Observed steps, all present in recent spikes: launch → explore/derive → **independent refute-verification** → land self-contained in canon at honest tier (integration-is-replacement) → set spike status `LANDED`/`EXPLORATORY`/`ACTIVE` → file to `spikes/.integrated/` with a dated MANIFEST, or keep live.

Evidence it is real, not aspirational (all first-hand from `spikes/INDEX.md` + segment state + git):
- `spike-mood-timescale-matching-2026-06-17` → **LANDED** in `#der-mood-timescale`; the strong "mood time-constant *matches* environment autocorrelation" slogan was **refuted and replaced** by a derived square-root scaling law — integration-is-replacement enacted, not narrated (commit `857db06`).
- `spike-w1-leakage-vacuity-2026-05-31` → the circular/vacuous $W_1$ bound was replaced by the corrected selection-channel bound plus a no-go appendix `#disc-w1-structural-bound-boundary` (commit `fbcb36a`) — a no-go landed as *present-tense canon*, per routing.sop §4/§6.
- Every recent spike carries an "**Independently refute-verified**" record (mood, captured-objective, multi-timescale, severed-actuation). The verify-cadence discipline is live.

Current live spike: `spikes/epistemic-target-ontology/` (5 files, last touched 2026-07-04, commit `7939df0`) — the active workshop reshaping PROPOSALS SP-30 (typed target $S_t=(\Omega_t,\theta)$), gated on GA-1 verification (now VERIFIED per `82c9bcc`) + Joseph's root-ontology call.

### A2. Audit finding-routing — HEALTHY at routing, BLOCKED at graduation

Trigger: a de-novo audit lands as `audit-<id>-FINAL-<date>.md`.
Steps: per-finding **strengthen-first** disposition (route, don't execute) → `audits/STATUS.md` row → findings routed to canon / TODO / PROPOSALS / the polish-and-sentiment ledger.

The *routing* half works: `audit-731548-FINAL-2026-07-02` (the newest, Fable-5 de-novo) was routed 2026-07-03 with Tier-1 executed (B-1/B-2/B-4 landed; B-3 → SP-30; mood MG-discharge done — CHANGELOG 2026-07-03). The strengthen-first inversion is genuinely applied (B-1 "strengthen-by-split" gated on a *second* independent re-derivation which refuted necessity by fresh construction).

The *graduation* half does not work — see (d) D1.

### A3. Gold-lift (incidental-gold routing) — STALLED mid-sweep

Trigger (per routing.sop §8): should be a **standing prompt step** — lift each audit's §14 "Wandering Thoughts" gold into per-segment `## Working Notes` **soon after the audit lands, so it does not pool**.
Ran hard 2026-05-30→31 under an explicit Joseph-agreed gate-release (`gold-lift-sweep-2026-05-30.md`): batches A1–A17 committed (commits `598631e`…`46168fa`), **122 AAT-core segments** now carry an "Incidental audit gold" Working Note (verified: `grep -rln "Incidental audit gold"` = 122, all in `01-aat-core/src`).

Then it stopped. Verified stall: **0** gold WN in `02-tst-core/src`, `03-llm-core/src`, `04-eli-core/src`. The planned wave 5 (A18–A21 App-A remainder + TST T1–T2 + logogenic L1–L2 + logozoetic E1–E2 + the end-of-sweep batched/paired-note reconciliation) **never ran**; the tracker's last line still reads "**Next — wave 5**" as if live. Last gold-lift commit: 2026-05-31 13:34. This is the clearest single abandoned-mid-flight process in the cluster (~5 weeks stale). It is also actively pooling: `AUDIT-WORKING-731548` has **38 top-level reflection notes and no `.integrated/` subdir** — gold-lift for it "not started" (STATUS.md confirms), exactly the pooling §8 exists to prevent.

### A4. Gem-hunt (audit re-mining) — HEALTHY but one-time; its meta-finding is durable

Trigger: under-mined audit-findings files (zero ledger / zero MANIFEST hits).
A 2026-05-29 qualitative pass mined 12 audits across two waves (STATUS.md §"Gem-hunt cycle"), each read first-hand against current canon, each gem parent-verified before landing. Real output: two math errors fixed (`f8d9151`), two headline gems → SP-26/SP-27, seeds → ledger S34–S41.
The durable meta-finding: **every one of the 12 audits' flagship findings had already been resolved by a later cycle** — "uniform drift," the central confirmation that *audit dispositions are drifted proxies* and the value is the incidental gold, not the certified findings. This is load-bearing for how the whole audit corpus should be read (see feedback-audit-findings-as-gem-hints).

---

## (b) Aspirational processes the docs/SOPs intend (but that aren't fully running)

### B1. Audit *graduation* — intended, effectively never happens

STATUS.md and routing.sop define "routed" vs "graduated" precisely: an audit graduates (git-mv to `.integrated/` + MANIFEST) only when every finding has a **verified** disposition **and** — for de-novo audits — the **gold-dir standing gate is settled with Joseph**. In practice **0 of 22 `AUDIT-WORKING-*` dirs have graduated** (none has an empty top level; all but 731548 have a `.integrated/` subdir holding *filed* per-segment notes, but every one still retains batch-reflection notes held per the deferral rule). The gate is the binding constraint (see (e)).

### B2. Spike three-part "fully integrated" criterion — partially honored

`spikes.sop.md` §2-bis: a spike is `integrated` only when (1) content in canon first-hand-verified, (2) **nothing *needs* to reference the spike**, (3) navigators reconciled. Part (1) is well-honored. Part (2) is where debt sits: **114 Working-Note references to `spikes/` paths across `src/`** (verified: 0 in canon sections, 114 in Working Notes). Canon-cites-only-canon *is* honored — the binary holds. But per the WN-discipline (INTEGRATION-CLEANUP §"developing discipline" pt 3), an *unneeded* WN spike-ref "pins the spike in place" and blocks archivability. Many of the 114 are legitimate forward-pointers (PROPOSED.md-indexed open items) or point at already-`.integrated/` archaeology (harmless), but the set has not been swept for the archivability-blocking subset.

### B3. Sim/empirical spike-class integration — intended, not built

INTEGRATION-CLEANUP corrected-principle pt 5 declares sims/experiments/benchmarks **spike-class** with the same integration duty. G4 would encode this in the SOPs and register the un-integrated sim corpora. **All of G4 is open** (see (d) D3).

---

## (c) Emergent patterns from git history

1. **Audit findings as stale hints, not a to-do list.** The gem-hunt's uniform-drift result (A4) is an *emergent* discovery — it was not the SOP's premise; it fell out of doing the pass. It has since been elevated to a memory principle. This is the corpus learning that its own audit dispositions decay.
2. **Gold-lift as a distinct workstream** emerged from recognizing that the §14 Wandering Thoughts are *orthogonal* to theory-fix triage and the more valuable, more perishable output — hence the separate "gold" vocabulary, the standing gate, and the dedicated sweep. (commit `338e262` opens the tracker.)
3. **Verify-against-current-canon-first, mandated by being burned.** During wave 3 the gold-lift found two "ready fixes" (Prop B.4 subscript, Landauer coefficient) that were **already fixed** by earlier commits (`9270aec`, 2026-05-12). That near-miss is *why* the consolidated strengthen-first queue header now mandates verify-first (gold-lift tracker 2026-05-31 entry). Drift again.
4. **Strengthen-first genuinely inverts naive ordering, repeatedly** — B-1 (731548), Model-S, W1-leakage, value-object convention-monotonicity all landed as *stronger scoped theorems or no-gos* where an auditor proposed a soften. The pattern is dense in CHANGELOG and the spike MANIFESTs.
5. **The routing SOPs are scarred living documents** — `routing.sop.md` carries 5 dated refinements, `spikes.sop.md` carries 10, each recording a specific near-miss. This is a healthy self-correcting-process signature, rare in the wider repo.

---

## (d) Stale / broken / abandoned — concretely

**D1. Audit graduation is universally stalled.** 0/22 `AUDIT-WORKING-*` graduated. Per-dir top-level note counts (verified 2026-07-07): 451729=18, 471203=18, 472913=17, 527914=17, 849201=21, 773921=33, **731548=38 (no `.integrated/`)**, plus 15 others with 2–11. STATUS.md's "Open / in-flight" table lists only **4** audits (731548, 773921, 384279, 451729) because it tracks *FINAL-report routing*, not *gold-dir graduation* — so the 12 gem-hunt audits + others whose gold dirs sit ungraduated are **invisible to the live status table**. Representational gap worth closing.

**D2. Gold-lift sweep abandoned after A17** (A3 above). Wave 5 never ran; TST/logogenic/logozoetic have 0 gold WN; 731548's 38 notes are pooling. Tracker still says "Next — wave 5."

**D3. The bulk-64 wipe (D-2) never happened; the corpora it concerns are unchanged.**
- `spikes/.integrated/` still holds **127 entries**; `spikes/.archived/` still exists (1 README). The 2026-05-19-evening wipe Joseph signalled did **not** occur. So the un-discharged bulk-64 integration debt (`MANIFEST-2026-05-12.md`: 64 spikes bulk-moved without per-spike content verification) is still live and still un-verified.
- `02-tst-core/simulations/` — **11 `.py` files, dated 2026-03-20, still parked in the component tree**, still **not registered in `spikes/INDEX.md`** (verified: grep count 0), still outside the spike discipline entirely. INTEGRATION-CLEANUP G2 item for it is unchecked.
- `spikes/track-b-nonlinear-sims/` — canon dependencies were resolved 2026-05-30, but its own terminal home remains open (INTEGRATION-CLEANUP G2 marks it `[~]`).

**D4. INTEGRATION-CLEANUP-TODO — half-done, half-abandoned.**
- Done (verified by the claims + spot-checks): G1 governing-doc truthification (CLAUDE.md ref-line excised; §2-bis(2) regrounded; §5 D-3-revised); the G2 *reference* half (canon→artifact refs — verified 0 in canon sections today); G3 citation discipline (BIBLIOGRAPHY-TODO, relata `emit`, biblatex wired 2026-06-05).
- Open/abandoned: G2 *corpora* half (bulk-64, tst simulations, track-b terminal home — D3); **all of G4** (sim spike-class SOP additions; INDEX registration of the two sim corpora); **all of G5** (CLAUDE.md-as-unreviewed-amplifier — periodic human-visible audit cadence, generate-portions-of-CLAUDE.md). G5 is a project-wide governance risk parked with no owner.

**D5. `spikes/INDEX.md` carries stated, un-retired lint debt** — the 2026-05-19 note records "47 issues after this pass; 51 on HEAD," explicitly left as "a tracked seam." Plus INDEX updates are self-described as "informal … the authoritative state is always the spike file itself." The 182 KB INDEX is a convenience record, correctly de-authoritized, but drifting by design.

---

## (e) Decisions genuinely blocked on Joseph

1. **D-2 — the bulk-64 `.integrated/` wipe.** The *only* item on `JOSEPH-TODO.md` "needs your decision." Three coupled sub-calls: *discharge the integration debt vs. consciously set it down*; *semantics* (rm+commit, git-recoverable, vs history-purge, irreversible); *scope* (`.integrated/`+`.archived/` only, or also `02-tst-core/simulations/`, `track-b-nonlinear-sims/`, `ref/`). One-line context it needs: "64 spikes were bulk-filed to `.integrated/` in May 2026 without per-spike content verification; before we ever delete `.integrated/` we either verify those 64 landed in canon or you consciously accept the risk of losing any un-landed valid math." This has sat since 2026-05-19.

2. **The de-novo gold-dir standing gate — for all 22 `AUDIT-WORKING-*` dirs.** `audits/README.md` makes it a *standing, non-optional* gate: before any processing / `.integrated/` move / deletion of a gold dir, the agent must "consult Joseph and decide *with* him." It has been released exactly once (the 2026-05-30 gold-lift, and only for the lift, not for graduation). Until Joseph decides the disposition of the gold, **no routed audit can graduate** — this is the structural cause of D1. One-line context: "22 de-novo audit 'gold' dirs (first-encounter cognition / Wandering Thoughts) are routed but can't be cleared out of the live tree until you decide what happens to the gold — lift-then-archive, keep-in-place, or something else."

3. **Reserved spike verdicts awaiting the gate** (lower stakes; JOSEPH-TODO says lead will default-and-proceed on some): `#schema-strategy-persistence` hard-ceiling (spike drafted verdict B — "name the convention, keep `status: exact`"; JOSEPH-TODO now delegates this to the lead); the `epistemic-target-ontology` root-ontology call (SP-30 reshape + typed-target adoption).

4. **The `184930` predictions-doc gold disposition** — flagged "JOSEPH-DECISION pending" in the gold-lift tracker (whole-framework framing, no per-segment anchor; not part of the per-segment sweep).

---

## (f) Candidate meta-process definitions (raw material for a MECE hierarchy)

Each: name / trigger / steps / current health.

| # | Name | Trigger | Steps | Health |
|---|------|---------|-------|--------|
| MP-1 | **Spike lifecycle** | Any question needing exploration (friction-free) | launch → explore/derive → independent refute-verify → land self-contained in canon at honest tier → status-label → file `.integrated/` (MANIFEST) or keep live | **de-facto / healthy** |
| MP-2 | **Audit finding-routing** | De-novo audit lands as FINAL | per-finding strengthen-first disposition (route, don't execute) → STATUS.md row → canon / TODO / PROPOSALS / ledger | **mixed** (routing healthy; graduation blocked) |
| MP-3 | **Audit graduation / working-dir clearing** | All findings verified-closed | verify dispositions + settle gold dir *with Joseph* → git-mv to `.integrated/` + MANIFEST | **broken / stalled** (0/22; gate never released for graduation) |
| MP-4 | **Gold-lift (incidental-gold routing)** | Audit lands (should be *prompt*, standing) | per-segment lift §14 gold → segment `## Working Notes` → file source-note to per-dir `.integrated/` → dir graduates when empty | **stalled / abandoned mid-sweep** (A17, 2026-05-31; 731548 pooling) |
| MP-5 | **Gem-hunt (audit re-mining)** | Under-mined audit backlog | read findings vs current canon → mine fresh gems → parent-verify first-hand → route (never archive math we'd recreate) | **healthy but one-time**; durable meta-finding (uniform drift) |
| MP-6 | **Integration-debt recovery** (INTEGRATION-CLEANUP) | 2026-05-19 discovery of unverified bulk-move + canon→artifact refs | truthify governing docs → discharge reference debt → build citation discipline → extend to sim class → mitigate CLAUDE.md amplifier | **mixed** (G1/G2-ref/G3 done; G2-corpora/G4/G5 open/abandoned) |
| MP-7 | **Sim/empirical spike integration** | A simulation/experiment produces a claim | (intended) land the *knowledge* self-contained in canon; artifact → externally-citable at publication; register + route the artifact | **broken / not built** (11 tst `.py` un-integrated since Mar 2026; no SOP coverage) |
| MP-8 | **Reserved-decision routing to Joseph** | A spike/audit disposition needs an irreversible / framework-identity / publication call | tag it → JOSEPH-TODO / gold gate / PROPOSALS reserved | **partial** — the *naming* works (JOSEPH-TODO exists, gates are explicit); the *reaching-Joseph-in-actionable-form* is where items stall (D-2 sat 7 weeks) |

The MECE tension to flag for the synthesizer: MP-3 and MP-4 are two faces of one thing (draining a served-purpose working dir), split only by which *kind* of content is being drained (certified findings vs gold); MP-8 is not really a lifecycle process but the *cross-cutting* routing layer whose failure is this review's whole subject. A clean hierarchy might make MP-8 the parent and MP-1..MP-7 its children, since every stall in MP-2..MP-7 reduces to a Joseph-decision that hasn't been routed actionably.

---

## Out-of-scope surfacings (passed back deliberately)

- **STATUS.md under-represents the true audit backlog.** Its "Open/in-flight" table shows 4 audits; there are 22 ungraduated gold dirs. A reader trusting the table would conclude the audit backlog is nearly clear. Worth a "gold-dir graduation" column or a companion table.
- **CLAUDE.md-as-unreviewed-amplifier (INTEGRATION-CLEANUP F6/G5)** is a project-wide governance risk, not cluster-02-local: the auto-loaded onboarding doc every agent treats as gospel, that Joseph does not routinely read, with a demonstrated case of a predecessor's exception silently overriding a correct principle. G5's proposed mitigations (periodic human-visible cadence; generate portions the way LEXICON.md is generated) are unowned. This deserves a cluster of its own in the synthesis.
- **The gold pools faster than it drains, and this review adds to it.** `msc/reflections/` (36 reflections incl. #28) *is* the 731548 gold awaiting lift; the meta-review is generating more. Any "map the meta-processes" output should itself have a drain defined, or it becomes the next un-lifted pool.
- **The citation/bibliography discipline (G3 / BIBLIOGRAPHY-TODO) is largely done** (relata `emit` → `references.bib`, biblatex wired) — good news relevant to the publication-track clusters; the remaining ASF-side work is author-judgment segment migration, not tooling.
