# Spike-Routing — the spike-specific companion

> [!note]
> **The 2026-05-19→20 reconsideration of this SOP is largely resolved (2026-05-30).** The corrected principle is ratified (D-1): canon cites only other canon and the published external world; Working Notes are by definition not canon; a canon→internal-artifact reference is an integration failure, to be landed as canon or deleted. §5's bounded-guarantee was rewritten per D-3 — from a documented abdication ("do not re-audit `.integrated/`") to honest *un-discharged integration debt* (the 2026-05-12 bulk-64 must be verified, or consciously set down, before any wipe), with the false attribution dropped. §2-bis(2)'s "*need* vs *mention*" test was found already-grounded — Joseph reframed it 2026-05-19 as the spike-*archivability* test, not the canon boundary; nothing to re-excise. Still genuinely open: the bulk-64 / the `.integrated`+`.archived` wipe (D-2) and the citation-infrastructure build (G3) — both tracked in [`../INTEGRATION-CLEANUP-TODO.md`](../INTEGRATION-CLEANUP-TODO.md).

*The durable governing content for routing the `spikes/` corpus. This is deliberately **thin**: spike-routing and audit-routing are the **same problem** — take a unit of investigation, decide what is and is not true
(in the first place, and as of today's `src/`), and route it to where its truth belongs without losing signal. The hard-won core of that protocol —
the strengthen-first reflex, the four completion-states, the no-go protocol, the ghost-forms, the over-rotation correction, the meta-stance,
the independent-verify gate — already lives, **written about spikes**, in
[`audit-routing-instructions.md`](audit-routing-instructions.md). This file adds only the spike-specific delta and defers everything shared into that doc.*

> Status: **current ops, unscarred.** This is a first authoring, validated
> only by analogy to the exercised audit cycle. It has no scars yet; it
> will earn them on first contact. Front-line confusion against anything
> here is the re-truthification channel (audit-routing §7), not noise —
> and refinements to the *shared* core land in `audit-routing-instructions.md`
> (scarred per its §9), not forked here.

---

## 0. The core principle — truth is the arbiter; everything else is a proxy (Joseph 2026-05-18)

**This governs every section below it.** The job is to get the
*theory's truth* right. Provenance, git history, CHANGELOG, the INDEX label, `NOTATION.md`, the spike's own framing, the segment's own assertion, audit findings, agent consensus, even the convergence of multiple independent agents — **all of these are mild proxies for truth,
and every one of them drifts.** They are useful for *locating* a question and *cheap-screening* it; they never *settle* it. A question is settled only by the mathematics, re-derived independently far enough to stand on constitutive structure (definitions that make the core cohere) +
forced identities + elementary steps — *not* on what any artifact says.

Two concrete, recurring traps this names:

- **`NOTATION.md` is a lagging index.** Spike findings and new segments routinely fail to update it; the live theory drifts away from it. "The notation defines X as Y" is *not* evidence that X *is* Y — it is at most evidence about a document that may be stale. Never cite it as authority; at most as corroboration explicitly marked non-load-bearing.
- **"Verified against \<artifact\>" is proxy in verification's clothes.**
  Tagging a step `[Verified]` because a document *says* it does not make it verified — it verifies the document, not the truth. The tell: a
  `[Verified]` whose object is "what file F asserts" rather than "the derivation holds." (Worked instance, 2026-05-18: a ρ-factorization judgment leaned on "NOTATION defines $\rho$ as a single primitive" tagged
  *verified*; the real argument rested on the constitutive meaning of mismatch + the Kalman innovation identity + algebra, and was *stronger*
  once the NOTATION proxy was deleted. Joseph: *"you have to care about the theory's TRUTH more than anything else — provenance and things like that are only mild proxies."*)

The decisive-test (§2), the regression axis (§2a), the independent-verify gate, strengthen-before-soften — all of these are
**proxy-discipline**: machinery for not fooling ourselves with the cheaper proxies. They serve §0; when any of them is in tension with re-derived truth, truth wins and the proxy-rule is the thing that gets re-truthified.

### §0c. Honest incompleteness is a complete discharge — the counterweight to §0 (Joseph 2026-05-18)

§0 and the gates, taken without this, drive a **verification-regress**:
every gate spawns another, nothing is ever released, and an honest
"not yet" feels like failure. It is not. **The gates exist to prevent false confidence, never to forbid honest incompleteness.** Duty is discharged — fully — when, *at the current level of understanding*:

1. the artifact carries its **honest tier** (status downgrade /
   `conditional` / `discussion-grade` / a KNOWN-DEFECTIVE mark — whatever is true), not an inflated one;
2. its **Working Notes state precisely what is unresolved and what would resolve it**; and
3. the open remainder is **released to the standing cycle** (TODO /
   PROPOSALS / the audit cycle / the Joseph-reserved queue).

Then **stop.** You do not have to drive every thread to closed-form exact resolution in real time, and you must not keep escalating verification depth past the point where the artifact is completely honest.
Strengthen-before-soften means *attempt* the strong result — it does
**not** mean you may not honestly land at "conditional; here is exactly what is open"; that honest landing *is* the discipline succeeding. A self-check that you are regressing rather than discharging: you are launching another gate not because canon would otherwise *lie* but because an honest lower tier feels insufficient. It is sufficient.
(Joseph 2026-05-18: *"it is ok to mark something with a lower epistemic value, note in the working notes that it needs additional work, and let the wider audit-cycling pick it up. As long as it is completely honest as per our current level of understanding, your duty has been dispatched."*) The remaining live gate is legitimate only when an artifact would *assert false confidence* without it (a canon landing, a status elevation) — not as a precondition for *releasing an honestly lower-tiered* item.

---

## 0b. Why a companion and not a fork

`audit-routing-instructions.md` §0 — *"the job is not to do what the audit said — the job is to take each finding, decide what is and is not valid …
and route it to the right home"* — generalizes to spikes verbatim. Its §3 already enumerates the four spike completion-states; its §4 is the spike no-go protocol; §5/§6 are the spike ghost discipline. Duplicating that content here would (a) parallel existing infrastructure instead of extending it, and (b) fork a hard-won protocol so two copies could drift —
the worse failure, because the no-go protocol is the part that must never drift. **The shared core is corpus-agnostic; spike-routing is its second corpus.** Running it here is expected to *refine* that core; those refinements land there.

> **RECOMMEND, flagged for Joseph — not done unilaterally.** A reciprocal
> one-line head-note in `audit-routing-instructions.md` acknowledging that
> its core also governs spike-routing would close the loop honestly. That
> doc is an authoritative, Joseph-attested SOP; its own §7 says the lead
> agent does not silently rescope it. So the deference here is
> one-directional (safe — it asserts nothing about the other doc) until
> Joseph adds or declines the reciprocal note.

---

## 1. Step-zero: live work is out of scope

Before any disposition, identify and **exclude** spikes whose authors are still in them. A spike-routing cycle does not touch live investigation —
the authors integrate their own work, on their own completion.

Liveness signals (any one is enough; when genuinely unsure, treat as live — the cost of excluding a settled spike for one cycle is a re-look,
the cost of disturbing a live one is real):

- `spikes/INDEX.md` status of `ACTIVE` / `IN FLIGHT` / `IN PROGRESS`, or a recent `blocked` with an open follow-on.
- A `msc/` working artifact dated within the cycle that references the spike as ongoing.
- Recent mtime *and* an open (non-terminal) verdict in the spike itself.

Seed exclusion for the 2026-05-17 cycle (Joseph-affirmed): the self-actuation / WF-strengthening pair (`spike-self-actuation-grounding.md`,
`spike-wf-strengthening.md`) and `spikes/visual/` (INDEX: ACTIVE).
`spikes/INDEX.md` and the `spikes/PROPOSED.md` family (`PROPOSED.md` index + `PROPOSED-ADVANCED.md` + `PROPOSED-MISC.md`) are durable index/proposal navigators — they **stay** (the spike analog of the `pending-findings-*.md` ledgers staying), they are not routed (placement only — §2-bis(3) governs their content-currency).

---

## 2. The unit, and the canonical failure this exists to catch

The unit is a spike (a `spike-*.md` file, or a spike directory).

The failure: **math or a no-go that is real and true but lives only in the spike** — sometimes referenced from a segment's Working Notes, sometimes not referenced at all. *A reference is not integration.* Per
`~/.claude/memory/...feedback_math_lives_in_segments.md` and audit-routing §4: good math derived in a spike never resides only in the spike; it lands in a segment or (more often) a new appendix. A no-go is present-tense canonical truth (audit-routing §6), not archaeology.

**The decisive test for "integrated":** the load-bearing content appears in a `src/` segment or appendix, **verified first-hand** — not the INDEX label, not a Working-Notes pointer from a segment, not an agent summary.

### 2-bis. "Fully integrated" is a three-part completion criterion (Joseph 2026-05-18)

A spike is not `integrated` (and must not be filed to `.integrated/`)
until **all three** hold — partial satisfaction is the looks-done-but-isn't trap:

1. **Content present in canon**, verified first-hand (the decisive test above) — and provenance-clean (§2a regression axis: it is the post-correction truth, not a regressed restoration).
2. **Nothing *needs* to reference the spike anywhere.** No segment /
   OUTLINE / `depends:` sends a reader to the spike to understand canon.
   A *non-needed* breadcrumb in CHANGELOG / a tracker is fine — the test is *need*, not *mention* (Joseph 2026-05-18: "references in changelog are fine — as long as nothing **needs** to reference it"). **Grounding (Joseph 2026-05-19, de-conflates this): the *need* test is the spike-*archivability* test (can the spike move without canon breaking); it is *not* the canon boundary, which is simply binary — Working Notes are *by definition not canon* (a free attachment to the segment; that, plus CHANGELOG / the history layer, is *why* a breadcrumb there is fine — not because it is "non-needed" but because it is not canon at all), and everything else is canon and cites only canon. Which fields/sections exist, and which are canon vs Working-Note, is FORMAT.md's + the build-pipeline's authority — not this doc's to enumerate (narrative and other segment types are canon too); the only spike-discipline-relevant line is Working-Notes-↛-canon. So the grep below is about canon: a Working-Notes / CHANGELOG hit is a non-issue by construction; any other in-segment spike reference is a category error regardless of whether it is "needed."** After any archive batch: `grep -rl 'spike-<slug>'` across `*/src/` + OUTLINE;
   **reduce-not-repoint** every hit to the live canonical home (the CHANGELOG cycle entry, or the segment where the math now lives);
   surface any genuine open content the pointer was hiding into the segment's own Working Notes. (CHANGELOG:79 / `feedback_spike_references_only_in_working_notes` pt 5.)
3. **The navigator is reconciled.** `TODO.md` / `PROPOSALS.md` /
   `PRACTICA.md` **and the spike-corpus navigators `spikes/INDEX.md` and
   `spikes/PROPOSED.md`** — items that the integration resolves are
   **closed at cycle-commit time, not deferred** (triage-is-the-answer);
   items it *advances but doesn't close* are updated with the new disposition + spike-routing cross-ref; a navigator entry that still says "partially landed in #X" when #X is now `status: false`/superseded is a navigator-level §4.1 lie and is corrected with the same urgency as a segment one. "Find more info" cuts both ways — a navigator item may
   *resolve* the spike or *reopen* it.

   `spikes/PROPOSED.md` is the **3-perspective spike-proposal index** (moonshot/theory-edge detail in `PROPOSED-ADVANCED.md`; segment-perspective strengthenings keep their detail in the segment's Working Note; residual in `PROPOSED-MISC.md`), a low-friction *optional* repository, **not a mandatory registry** — spikes launch friction-free by anyone anytime, completeness is explicitly *not* required, and it is one of several parallel work-finding avenues (the others deliberately tracker-free: open gaps/theory-edges; the below-epistemic-cap segment scan). Two disciplines bind, both about keeping what *is* there trustworthy rather than exhaustive: **(freshness)** what is there stays true — a resolving spike sets its row to a terminal status + canon link at cycle-commit time (a stale "open" row for a landed direction is a navigator-level §4.1 lie), landed rows kept-not-retired as the audit trail; re-scans are opportunistic, not a standing completeness obligation; **(mutual link)** where a segment Working-Note strengthening/spike-proposal comment *and* a row both describe one effort they reciprocally link (row→detail-home, WN→tier) — the `sw-reciprocal-link-check` grep (PROPOSED-MISC, to build) is the teeth for *that consistency*, not for a duty to register everything; efforts owned elsewhere (§D.9, ROUTING) are cross-referenced, not duplicated. "Durable; it stays" governs *placement* (these files are not routed/moved like spikes) — **not** content-currency, and **not** an obligation to be complete. Scar: Refinement 10.

The archive batch (the `git mv` + MANIFEST) is the *start* of completion,
not the end; (2) and (3) are not "next housekeeping," they are part of the same cycle that moved the file.

### 2a. The regression axis — central to every disposition (Joseph 2026-05-17)

There is a **second canonical failure**, co-equal with the first and just as much the reason this cycle exists: **re-introducing a deliberately-corrected-away result because it "looks better."** Joseph's scenario: *a spike is fully integrated → an audit finds a flaw → the theory is fixed → and then we put the spike result back because it looks cleaner.* The corrected theory is **usually messier** than the clean-but-wrong claim it replaced (it carries a no-go, a scope-narrowing,
a caveat — truth is uglier than the aspiration), so the spike *will* look better. **"It looks better" is the body-signal**, exactly as in strengthen-before-soften — this is its reverse-direction sibling, and the enforcement teeth of integration-is-replacement (a refuted claim is
*deleted*; a spike carrying it must never be re-landed, and canon must not silently drift back to it).

"Absent from canon" and "present in canon" each have **two provenance-distinct causes that look identical from the spike's side**,
and the regression investigation is the **mandatory, central** step that tells them apart — run on *every* disposition, not just orphans:

- **Orphan side (before landing):** *never-landed-and-valid* (true orphan → land) **vs.** *landed-then-deliberately-corrected-away*
  (`correctly-superseded` → it goes to `.integrated/`/`.archived/` with the supersession recorded; **re-landing is a forbidden regression**).
- **Integrated side (when confirming `integrated-*`):** the in-canon content is the *current corrected truth* **vs.** a *regression-
  restoration* of a superseded spike form sitting on top of a later fix.
  Verifying *presence* is not enough — verify the present version's
  **provenance is post-correction and consistent with it.**

**The investigation (non-optional, on every spike):** pickaxe
`git log -S'<result-string>' -- '*/src/*'` (an add-*then-delete* is the red flag — find the deleting commit and read *why*); `git log`/`blame`
on the candidate/landed locus against the **CHANGELOG.md / LOG.md**
correction timeline; **audits/** + `pending-findings-*.md` for a finding that flawed it. The question is never "is it in canon?" alone — it is
"is canon's current state, here, the *post-correction* truth, and would this spike's content *regress* it?" If corrected-away: disposition is
`correctly-superseded`, never `orphaned`; if a prior integration *was* a regression-restoration, that is a §4.1-class canon-lie to honesty-mark.

---

## 3. The five-state disposition

Every in-scope spike resolves to exactly one. (Joseph supplied roughly these as "initial thoughts, non-MECE, refine"; this is the refinement —
cut it back if it has over-built.)

| State | Means | Disposition |
|---|---|---|
| `integrated-filed` | content in canon **and** already under `.integrated/` | none — but **sample-verify** (the 2026-05-12 bulk move of 64 was not per-spike content-verified; the label is a hypothesis, see §5) |
| `integrated-misfiled` | content in canon, spike still in `spikes/` top level | spot-check content-in-`src/`, then parent `git mv` → `.integrated/` (safe-mechanical; independent-verified per audit-routing §8) |
| `orphaned` | completed, result real (**success or no-go**), **not in canon, or only referenced** | **run the §2a regression investigation first** (never-landed vs. corrected-away); only then strengthen-first + the §4 landing protocol; landing-scope per §4 |
| `correctly-superseded` | result *was* effectively in canon then deliberately corrected/no-go'd away (§2a regression investigation positive) | **do not re-land** — `.integrated/` (or `.archived/`) with the superseding correction recorded; re-landing is a regression |
| `archived` | incomplete **and** not needed | parent `git mv` → `.archived/` with a one-line recorded reason (why set down; whether anything is worth salvaging first) |
| `live-or-open` | incomplete and still needed, or step-zero live work | stays in `spikes/`; INDEX status reflects open/blocked; not moved |

The hard ones are `orphaned` (where the actual theory work is) and the
`archived`-vs-`live-or-open` judgment (a truth-claim about the theory's
*needs* — when an agent cannot settle it from the material, it is a Joseph-adjudicated call, not a guess).

**Cross-repo / externally-blocked decision rule (pilot 023198,
2026-05-17 — scarred below).** A spike can be *complete as a scoping/derivation doc with a real result* whose **source-of-truth lives in another repo's unsettled artifact** (e.g. a paper in review). That is
**not** `orphaned` — landing it would import an unsettled cross-repo result, the exact inverse of primary-source discipline. Rule: *if the result's source-of-truth is another repo's unsettled artifact, the spike is `live-or-open` regardless of how complete the local scoping looks;
surface the canon-gap for the owner, do not land.* This recurs —
cross-pollination spikes from the paper portfolio are a known category.

---

## 4. Landing-scope policy (Joseph 2026-05-17 — hybrid)

When a spike is `orphaned` and its result must reach canon:

- **Safe-mechanical moves and tractable/clear landings execute *this cycle*.** Per the triage-is-the-answer discipline: the cycle is not the taxonomy. The safe subset is not queued for "next housekeeping" — it is executed in the cycle that produced the disposition.
- **Substantial segment-authoring landings get a written landing-plan**
  (`spikes/<slug>-spike-integration-plan.md`, audit-routing §4.3) surfaced in `PRACTICA.md` (§4.4), and are done deliberately — often best by the spike's own authors, who hold the context.

"Tractable" vs "heavy" is itself a judgment the adjudicating agent records with its disposition (what would the landing touch? one segment's Discussion, or a new appendix + cascade?). The parent decides the auto-land/queue split from that.

---

## 5. Directory-label honesty (and its bounded guarantee)

`.integrated/` is a **truth-claim**: *this spike's load-bearing content is present in canon.* `.archived/` is a distinct honest bucket: *consciously set down; not in canon; reason recorded.* The two are **not interchangeable** — collapsing them is the directory-level form of the label-lies-about-status error that audit-routing §5/§6 spends pages preventing.

**Bounded guarantee, stated in `spikes/README.md` so the claim is honestly scoped rather than silently overclaimed:** the guarantee is **forward and per-cycle**. Spikes a spike-routing cycle files to `.integrated/` have had their content verified in canon. Pre-policy residents have **not** — before `.archived/` existed (notably the 2026-05-12 bulk move of 64), some were swept to `.integrated/` *without per-spike verification*. That is **known, un-discharged integration debt** (`../INTEGRATION-CLEANUP-TODO.md` G2/F3), **not** a "do not re-audit" license: the bulk-64 must be checked — or consciously, explicitly set down — before `.integrated/` is ever wiped (the D-2 wipe question turns on exactly this). Until then, treat pre-policy `.integrated/` membership as an *unverified* record; verify forward, and discharge the bulk-64 through the recovery pass.

### 5a. Directory layout — where everything lives (Joseph-directed, 2026-05-18)

Spike-routing artifacts live under `spikes/` (the corpus they act on) —
**never** under `audits/` (a different corpus) and **never** under
`msc/` (delete-at-any-time scratch). Canonical homes:

| Artifact | Home | Notes |
|---|---|---|
| Governing SOP (this file) | `doc/spike-routing.md` | long-lived process doc; parallels `doc/audit-routing-instructions.md` |
| Live cycle tracker / rendezvous | **`spikes/ROUTING.md`** | **undated** — the routing *process* is ongoing, not a one-shot; durable, *not* `msc/`; parallels `spikes/INDEX.md` |
| Per-cycle move manifest | `spikes/.integrated/MANIFEST-<date>.md` | dated is correct here — it records one specific batch move |
| Adjudication / verify / regression trails | **`spikes/.routing-trail/SPIKE-{WORKING,VERIFY,REGRESSION}-<id>/`** | dot-prefixed (keeps `ls spikes/` scannable); six-digit ID = identity, prefix = class — never blanket-rewrite a prefix; frozen-as-written, not back-edited; preserved (not deleted/summarized) once conclusions are in the durable layer |
| Integrated / archived spikes | `spikes/.integrated/` · `spikes/.archived/` | the two terminal homes (§5) |

The trail dirs and the tracker are **not** "audit" artifacts even though spike-routing *defers into* `audit-routing-instructions.md` for the shared protocol — sharing the protocol is not sharing the corpus.
`spikes/.routing-trail/README.md` carries the rosetta for any trail written before this layout was fixed (read old `audits/SPIKE-…` /
`msc/spike-routing-<date>.md` mentions as the homes above).

---

## 6. The dir-spike gold gate (lighter — Joseph 2026-05-17)

File-spikes: agents adjudicate → parent independent-verifies → parent moves.

Directory-spikes (reasoning-trail clusters — `track-a-intent-dag/`,
`track-b-nonlinear-sims/`, `temporal-nesting-rg/`,
`spike-language-as-causal-substrate/`, `class-coercion-wrapping/`,
`spike-local-embedding-benchmark/`, …): agents may **read and recommend**
a disposition; the disposition is **Joseph-adjudicated in one batch**, not auto-filed.

Rationale: nothing is ever deleted (both buckets *preserve*; only the live tree changes), so the audit "summarized into oblivion" risk largely does not apply here — but dir-spikes carry cross-domain ideation whose value is orthogonal to "is the math in canon," and a one-batch human read is cheap insurance. This is **lighter** than the `AUDIT-WORKING-*` standing gate
(`audits/README.md`), which forbids any processing before consult; here agents may read and recommend, and Joseph adjudicates the batch.

**The axis that actually gates the Joseph batch is decision-type, not artifact-shape (pilot 023198 — ratified by Joseph 2026-05-17).** The dir-spike gate above is preserved. But a *file*-spike can also carry a Joseph-reserved decision — a framework-identity / cross-repo /
promotion-level call (structurally the M4 §5.1 / operator-family-spine kind). The operative criterion: *route to the Joseph batch anything whose resolution requires a decision Joseph reserved, file or dir.* This only ever routes **more** to Joseph (never auto-files something that needed him); it sharpens, not weakens, the intent behind the "lighter gate"
decision (don't let agents auto-file reserved-judgment calls).

---

## 7. Evidence hierarchy, and the un-trusted label

Decreasing reliability:

1. The spike's own terminal verdict / `## Independent Audit` section, **plus a first-hand grep of its load-bearing result-name/claim against `src/`
   and a read of the segment it should live in.** This is decisive.
2. `INDEX.md` cycle-header status — sufficient evidence for **NOT**-integrated
   (an `open`/`blocked`/`IN PROGRESS` label is enough to keep a spike out of
   `.integrated/`); a `LANDED`/`PROMOTED`/`VERDICT` label is a **hypothesis to verify**, never sufficient on its own.
3. `CHANGELOG.md` cycle narratives.
4. `TODO.md` / `PROPOSALS.md` / `PRACTICA.md` backlinks (open `[ ]` is sufficient for not-integrated; *absence is not* sufficient for integrated).

**On git (Joseph 2026-05-17 — refinement 2): separate *recency* from
*provenance*.** Raw `git`-recency as a proxy for *integrated-status* is
**poisoned** for this corpus — the AAD→AAT sweep (2026-05-15), the role-prefix sweep (2026-04-24), and the 2026-05-12 bulk move all rewrote large swaths, so "recently touched" says nothing about whether content landed in canon. But **git *provenance* investigation is a valid,
encouraged, non-destructive technique here** — often the sharpest instrument for the decisive test: `git log -S'<result name / equation /
slug>' -- '*/src/'` (pickaxe — when, and whether, a spike's load-bearing string actually entered a segment), `git blame` on the segment locus,
`git log --follow` across the renames, and dates *read in context*
(spike-written vs. content-added-to-`src/`). Use it freely; just don't let a sweep-poisoned *recency ordering* stand in for the content check.
The INDEX label is the *convenience record*, not ground truth — exactly as the audit cycle learned its audit-id→ledger mapping was unreliable and had to be primary-source-verified.

---

## 8. What this defers to `audit-routing-instructions.md`

Everything shared. Specifically: the strengthen-first reflex (§2); the four completion-states — strengthened-to / -past / no-go / strengthen-failed
(§3); the no-go protocol — `FALSE`-mark, cascade closure, integration plan, PRACTICA surfacing, then route (§4); the ghost-forms and the over-rotation correction — *the no-go is canon, not a ghost to exile;
only redundant project-autobiography is demoted to the history layer*
(§5/§6); the meta-stance — this filter is itself unpurified, lead agent holds the meta-question (§7); route-don't-execute, the disposition enum,
the independent-verify gate (adjudicator ≠ confirmer), the working-dir lifecycle, the directory-prefix invariant (§8); and the phenomenology-is-load-bearing voice discipline (§9).

Read that document. This one only says what is *different* about spikes.

---

*Living document. Started 2026-05-17. Iterate as the process is exercised; record each refinement's scar so the next reader inherits the reason, not just the rule — this file inherits audit-routing §9's stance about itself.*

*Refinement 1 (2026-05-17, diagnostic pilot 023198 —
`spike-operator-sector-unification` + `spike-c2-star-to-integrate`).
Three frame defects caught before any fan-out, folded above: (1) no clean cell for cross-repo / externally-blocked spikes → §3 decision rule
(`spike-c2-star` is `live-or-open` because its proof's source-of-truth is
`~/src/behavioral-floor/`'s in-review paper, not because it is incomplete); (2) the Joseph-batch gate keyed on file-vs-dir when the load-bearing axis is reserved-decision-type → §6 criterion
(safe-direction, pending ratification); (3) tightly-coupled sibling spikes are mis-routable when split across fan-out slices — adjudicating
`spike-operator-sector-unification` forced a check of
`spike-update-operator-sector` (a genuine `orphaned`-suspect, not in slice), which an agent trusting "the operator family is done" would mis-route → partition keeps sibling clusters in one slice, siblings surfaced from outside a slice are flag-don't-route. Confirmed, no change:
the first-hand decisive-test read is non-optional — the INDEX label was wrong in **both** pilot cases, in **opposite** directions (understated for spike 1, accurate only by encoding an external block for spike 2).
The transferable scar: the convenience-label is unreliable in both directions, not only the optimistic one; the first-hand read is budgeted as mandatory every fan-out slice, not as a spot-check.*

*Refinement 2 (2026-05-17, Joseph-directed). The "git is poisoned"
framing inherited from audit-routing §8 was too blunt and risked suppressing a powerful investigative technique. Corrected in §7:
sweep-poisoned **recency-as-status-proxy** is the only poisoned thing;
**git provenance investigation** — pickaxe `-S` for when/whether a result-string entered `src/`, `blame`, `log --follow` across the renames, dates read in context — is valid, encouraged, and non-destructive, and is frequently the sharpest decisive-test instrument. The shared core carries the same correction (audit-routing
§8, Joseph-directed). Transferable: a blanket "don't trust X" inherited from another corpus can over-suppress; check whether the real defect is narrower (here it is *recency ordering*, not *git*).*

*Refinement 3 (2026-05-17, fan-out S2 — worked example
`spike-update-operator-sector`). The strengthen-first reflex has a spike-specific **dual** worth foregrounding. Audit-routing §2/§4 frames strengthen-first as "an auditor proposes a soften → try to strengthen first." But a spike commonly **already did its own honest strengthen-first internally and landed at `conditional`** (a legitimate terminal state, not a soften to undo). When such a spike never reached canon, the live question is **not** "should we soften / re-strengthen?" — it is the
`subsumed-by-later-work` **vs** `orphaned` discriminator: did a successor genuinely absorb the result, or is it stranded? Run that check explicitly
(grep the successor for the spike's load-bearing object; confirm absorption, don't assume it). Calling a self-conditional spike "done"
because "its honesty is intact" is the spike-corpus form of the soften-as-routing the protocol exists to catch.*

*Refinement 4 (2026-05-17, fan-out S1 + S5 + S6 — independent triple convergence, which per the convergence-as-coherence discipline is strong signal the gap is in the frame, not one agent's head). Two linked defects:*

*(a) `live-or-open` is **overloaded**. It is silently carrying at least five dispositions that route very differently: **live-author** (stays silently, hands-off), **open-direction** (stays silently), **spec-for-
queued-work** (stays, is a durable tracker), **cross-repo-blocked** (stays;
surface the canon-gap to the owner — §3), and **reserved-decision** (must go to the Joseph batch **loudly**, §6). A future agent reading
"live-or-open" as uniformly "ignore" will silently drop a reserved-decision orphan. Tag the sub-disposition explicitly: `live-or-open
{live-author | open-direction | spec-for-queued | cross-repo-blocked |
reserved-decision}`. The reserved-decision and cross-repo-blocked cases
**can co-fire on one spike** (e.g. an empirical half correctly cross-repo-
homed while the theoretical half is a reserved orphan — `spike-language-as-causal-substrate`):
the orphan loss-signal must not be muted by the "blocked on Joseph"
framing.*

*(b) The **parallel-path-landed-but-payload-orphaned** shape. A spike's core can be in canon via an **independent/parallel** derivation (a sibling overnight commit; a same-day co-author) while the spike's **distinctive payload** — a strengthening it alone carries, or a triage recommendation canon *contradicted* — never landed. This is neither plain `integrated`
nor plain `orphaned`; the reflex to file it `integrated` ("the core's in canon, done") is soften-as-routing. Handled as a **recognition rule under
`orphaned`** (not a sixth state — taxonomy bloat is the §1 anti-pattern):
*if the spike's core is in canon via a parallel path, the orphan is the spike's distinctive payload; route on the payload, not the core.* A triage spike whose recommendation canon contradicted is a present-truth signal →
Joseph batch, never a filing op.*

*Refinement 5 (2026-05-17, Joseph-directed — a **pre-emptive** scar:
articulated from foresight, before it bit, which is the cheapest kind to inherit). The regression failure — re-landing a corrected-away result because it "looks better," or confirming an `integrated-*` that is actually a regression-restoration over a fix — is elevated from a side note to a **central investigative axis** (§2a), co-equal with math-stranded-in-spike, run on **every** disposition including the already-integrated. First worked application passed cleanly:
`spike-update-operator-sector` regression-checked CLEAR — pickaxe shows
`(O-A2')`/`α_op`/`O-DA.1` never in `src/`; CHANGELOG:73's 2026-05-14 SP-22 decoupling names the `PID/update-operator α-list` explicitly in the
"($\gamma$)-hybrid … straight authoring, no longer gated" set (deferred, **not**
flawed-and-corrected); no audit flags it. Genuine orphan, cleared. The shared core carries the same elevation (audit-routing §8 + its Refinement
3, Joseph-directed). Transferable: when an integration "looks better"
than canon, that aesthetic pull *is* the trigger to run the provenance investigation — canon is probably the corrected-uglier-truer version.*

*Refinement 6 (2026-05-18, regression-recheck agent SPIKE-REGRESSION-014997
— all 10 already-integrated cleared, no regression). The sharpest §2a instrument is the **exclusion pickaxe**, not the add-then-delete one:
`git log -S'<the refuted/superseded form>' -- '*/src/*'` returning
**empty** proves the wrong form *never entered canon at all* ⇒
regression-impossible, replacement-was-honored-at-landing. §2a's
"add-then-delete is the red flag" implicitly assumes the wrong form landed once and was later cleaned up; but for the common case where a spike's *own body* carried the later-refuted form, "no add-commit for the refuted string, ever" is a **stronger** clean signal than "added then correctly deleted" (it proves replacement-at-landing, not after-the-fact cleanup) **and** it is **sweep-immune** — an empty result cannot be poisoned by the AAD→AAT / role-prefix rename sweeps, where add-then-delete recency can. Operative order for the regression axis: run the exclusion pickaxe on the refuted form first; empty ⇒ clean (regression-impossible);
only non-empty escalates to the add-then-delete / CHANGELOG-timeline investigation. This is a first-class clean disposition, not a fallback.*

*Refinement 7 (2026-05-18, Joseph-directed — a near-miss caught, not a post-mortem). "Fully integrated" was being treated as content-in-canon + no-needed-references; the **navigator reconciliation**
(`TODO.md` / `PROPOSALS.md` / `PRACTICA.md` items the integration resolves or advances) was not an explicit completion part and was about to be left to "next housekeeping" — the exact triage-is-the-answer failure. Elevated to part (3) of the §2-bis three-part criterion. The sharp tell this surfaced: a navigator entry still asserting
*"`spike-rho-factorization` partially landed in
`#internal-external-decomposition`"* (PROPOSALS §D.9, TODO Group I) when that segment is now `status: false` — a **navigator-level §4.1 lie**,
corrected with segment-level urgency. Transferable: the `git mv` +
MANIFEST *feels* like completion (a durable artifact shipped); it is the
*start*. Run the navigator grep (`grep -niE '<spike-slugs>|SP-<ids>'
TODO.md PROPOSALS.md PRACTICA.md`) as a mandatory cycle-close step, and close/correct in the same commit — closed items are closed at cycle-commit time, not catalogued for later.*

*Refinement 8 (2026-05-18, Joseph-directed — the counterweight, added while the gate-machinery was visibly deep). §0c. The elaborate real-time verification layering (recheck → gate → §4.1 mark → spike →
gate → …) is good, but it invites a regress where honest incompleteness is mistaken for unfinished duty. Stated explicitly: honest-tier +
Working-Notes-says-what's-open + release-to-the-standing-cycle is a
*complete* discharge; do not escalate verification past honesty. The scar this pre-empts: future-me reading §0 and never releasing anything.
The self-check is in §0c (am I launching a gate because canon would
*lie*, or because an honest lower tier feels insufficient?). The remaining live Object-B gate is legitimate by that test — it feeds a canon landing / status elevation, not merely my own closure-comfort.*

*Refinement 9 (2026-05-18, Joseph-directed — a placement scar, caught late). The original (never-written) convention put the trail dirs in
`audits/` (extended by "spike-routing is the same problem as audit-routing" — but sharing a *protocol* is not sharing a *corpus*;
the artifacts of routing the spike corpus are not audits) and the live tracker in dated `msc/` (`msc/spike-routing-2026-05-17.md`) — and
`msc/` is delete-at-any-time scratch, no place for the cycle's durable rendezvous. Both were misplacements, and worse, the convention was only
*implicit* (in the tracker + my practice), so the SOP couldn't catch it. Corrected: §5a now states the layout explicitly; tracker →
`spikes/ROUTING.md` (de-dated — the process is ongoing); 13 trail dirs
→ `spikes/.routing-trail/` (frozen, rosetta'd, not back-edited); every live pointer re-homed and verified zero-stranded. Transferable: an
*implicit* convention is one the SOP cannot defend — write the layout down, in the governing doc, the first time, not after a tree fills with misplaced dirs. Also the environmental gotcha that masked this for two attempts: Bash in-place stream editors (`sed -i`, `perl -pi`) silently no-op on the repo here; only the Edit/Write tools and `git mv` persist
— verify file edits by re-reading, never by the editor's exit status.*

*Refinement 10 (2026-05-19, Joseph-caught — a navigator that drifted because the SOP did not name it). `spikes/PROPOSED.md` (the spike-proposals catalog) had silently drifted: last content-curated 2026-04-25, with at least four entries (Causal-IB LMI, message-passing credit-assignment, FEP-as-suboptimal, Landauer/thermodynamic-cost) still presented as open candidates "requiring repair" when their repairs had landed in canon — the exact navigator-level §4.1 lie §2-bis(3) exists to catch, but §2-bis(3) named only `TODO.md`/`PROPOSALS.md`/`PRACTICA.md`, not the spike-corpus navigators, so the obligation never attached to it. Caught not by the SOP but by Joseph's question "are we still tracking a suggested-spikes / proposed or something?" — and his follow-up directive: "be sure, and add a constant update to it in your SOPs." Corrected: §2-bis(3) now names `spikes/INDEX.md` and `spikes/PROPOSED.md` explicitly and states the bidirectional reconciliation (down on spike-resolution, up via periodic corpus scan). The 2026-05-19 one-time reconciliation discharged the accumulated drift (10 entries dispositioned; a Phase 3 of 4 scan-surfaced candidates added; one borderline candidate deliberately not double-listed because it was already homed in PRACTICA/TODO). Transferable scar: "durable; it stays" said of a catalog means it is not *routed/moved*, never that it is *frozen* — a durable navigator still accrues drift in both directions, and the completion criterion must name every navigator it governs or the governance silently exempts the unnamed ones. The shared core's §2-bis is not forked; this spike-specific delta (PROPOSED.md is a spike-corpus artifact) lands here, per §0b. **Resolution shipped 2026-05-19 (Joseph's 3-perspective proposal, taken with refinements):** the interim "name PROPOSED.md in §2-bis(3)" was elevated to a restructure — `PROPOSED.md` became the unified *index* (priority-tiered tables; added/name/source/description/status/updated/details columns), the original catalog `git mv`'d to `PROPOSED-ADVANCED.md` (moonshot detail home, down-reconciliation dispositions preserved), `PROPOSED-MISC.md` created (residual; allowed-empty); segment-perspective strengthenings keep detail in the Working Note with a reciprocal back-link; completeness made real by cross-referencing (not duplicating) efforts owned in §D.9/ROUTING; the enforcement-grep itself indexed as a MISC dogfood entry. Refinement transferable beyond this instance: when a navigator drifts because the SOP under-named it, the durable fix is usually structural (split index from detail so what *is* tracked can be kept fresh and the detail has an unambiguous home), not just adding the name to a list. **Calibration (Joseph 2026-05-19, immediately after — the over-correction caught before it set):** the first cut of this fix made "Completeness — every known un-started effort has a row" a *binding* discipline. That over-reached and was deflated the same day. Spikes are launchable by anyone for any reason with **no administrative friction beyond "go ahead and spike it"**; a binding-completeness registry reimports exactly the friction the spike convention exists to forbid. The disciplines that bind are **freshness** (what is there stays true — the §4.1 / no-stale-lies part) and the **mutual link** (consistency between a WN comment and its row *where both exist*) — *not* completeness. PROPOSED is the optional, low-friction set-it-down-here place and **one of several parallel work-finding avenues** (peers, none privileged): open gaps/theory-edges (OUTLINE-GAP / `impl-*`), and the below-epistemic-cap segment scan (a `hypothesis`→empirical, a `conditional`→condition-dropped, a `discussion-grade`→derived) — both deliberately tracker-free. Meta-scar for the next steward: a reconciliation instinct that is correct for a *lying* navigator (fix it with teeth) becomes wrong when applied to a *low-friction convenience* (don't systematize it into a duty); the tell is when "keep it honest" silently becomes "keep it exhaustive."*
