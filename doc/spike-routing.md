# Spike-Routing — the spike-specific companion

*The durable governing content for routing the `spikes/` corpus. This is
deliberately **thin**: spike-routing and audit-routing are the **same
problem** — take a unit of investigation, decide what is and is not true
(in the first place, and as of today's `src/`), and route it to where its
truth belongs without losing signal. The hard-won core of that protocol —
the strengthen-first reflex, the four completion-states, the no-go
protocol, the ghost-forms, the over-rotation correction, the meta-stance,
the independent-verify gate — already lives, **written about spikes**, in
[`audit-routing-instructions.md`](audit-routing-instructions.md). This file
adds only the spike-specific delta and defers everything shared into that
doc.*

> Status: **current ops, unscarred.** This is a first authoring, validated
> only by analogy to the exercised audit cycle. It has no scars yet; it
> will earn them on first contact. Front-line confusion against anything
> here is the re-truthification channel (audit-routing §7), not noise —
> and refinements to the *shared* core land in `audit-routing-instructions.md`
> (scarred per its §9), not forked here.

---

## 0. Why a companion and not a fork

`audit-routing-instructions.md` §0 — *"the job is not to do what the audit
said — the job is to take each finding, decide what is and is not valid …
and route it to the right home"* — generalizes to spikes verbatim. Its §3
already enumerates the four spike completion-states; its §4 is the spike
no-go protocol; §5/§6 are the spike ghost discipline. Duplicating that
content here would (a) parallel existing infrastructure instead of
extending it, and (b) fork a hard-won protocol so two copies could drift —
the worse failure, because the no-go protocol is the part that must never
drift. **The shared core is corpus-agnostic; spike-routing is its second
corpus.** Running it here is expected to *refine* that core; those
refinements land there.

> **RECOMMEND, flagged for Joseph — not done unilaterally.** A reciprocal
> one-line head-note in `audit-routing-instructions.md` acknowledging that
> its core also governs spike-routing would close the loop honestly. That
> doc is an authoritative, Joseph-attested SOP; its own §7 says the lead
> agent does not silently rescope it. So the deference here is
> one-directional (safe — it asserts nothing about the other doc) until
> Joseph adds or declines the reciprocal note.

---

## 1. Step-zero: live work is out of scope

Before any disposition, identify and **exclude** spikes whose authors are
still in them. A spike-routing cycle does not touch live investigation —
the authors integrate their own work, on their own completion.

Liveness signals (any one is enough; when genuinely unsure, treat as
live — the cost of excluding a settled spike for one cycle is a re-look,
the cost of disturbing a live one is real):

- `spikes/INDEX.md` status of `ACTIVE` / `IN FLIGHT` / `IN PROGRESS`, or a
  recent `blocked` with an open follow-on.
- A `msc/` working artifact dated within the cycle that references the
  spike as ongoing.
- Recent mtime *and* an open (non-terminal) verdict in the spike itself.

Seed exclusion for the 2026-05-17 cycle (Joseph-affirmed): the
self-actuation / WF-strengthening pair (`spike-self-actuation-grounding.md`,
`spike-wf-strengthening.md`) and `spikes/visual/` (INDEX: ACTIVE).
`spikes/INDEX.md` and `spikes/PROPOSED.md` are durable index/proposal
catalogs — they **stay** (the spike analog of the `pending-findings-*.md`
ledgers staying), they are not routed.

---

## 2. The unit, and the canonical failure this exists to catch

The unit is a spike (a `spike-*.md` file, or a spike directory).

The failure: **math or a no-go that is real and true but lives only in the
spike** — sometimes referenced from a segment's Working Notes, sometimes
not referenced at all. *A reference is not integration.* Per
`~/.claude/memory/...feedback_math_lives_in_segments.md` and
audit-routing §4: good math derived in a spike never resides only in the
spike; it lands in a segment or (more often) a new appendix. A no-go is
present-tense canonical truth (audit-routing §6), not archaeology.

**The decisive test for "integrated":** the load-bearing content appears
in a `src/` segment or appendix, **verified first-hand** — not the INDEX
label, not a Working-Notes pointer from a segment, not an agent summary.

---

## 3. The five-state disposition

Every in-scope spike resolves to exactly one. (Joseph supplied roughly
these as "initial thoughts, non-MECE, refine"; this is the refinement —
cut it back if it has over-built.)

| State | Means | Disposition |
|---|---|---|
| `integrated-filed` | content in canon **and** already under `.integrated/` | none — but **sample-verify** (the 2026-05-12 bulk move of 64 was not per-spike content-verified; the label is a hypothesis, see §5) |
| `integrated-misfiled` | content in canon, spike still in `spikes/` top level | spot-check content-in-`src/`, then parent `git mv` → `.integrated/` (safe-mechanical; independent-verified per audit-routing §8) |
| `orphaned` | completed, result real (**success or no-go**), **not in canon, or only referenced** | the primary work — strengthen-first then the §4 landing protocol; landing-scope per §4 below |
| `archived` | incomplete **and** not needed | parent `git mv` → `.archived/` with a one-line recorded reason (why set down; whether anything is worth salvaging first) |
| `live-or-open` | incomplete and still needed, or step-zero live work | stays in `spikes/`; INDEX status reflects open/blocked; not moved |

The hard ones are `orphaned` (where the actual theory work is) and the
`archived`-vs-`live-or-open` judgment (a truth-claim about the theory's
*needs* — when an agent cannot settle it from the material, it is a
Joseph-adjudicated call, not a guess).

**Cross-repo / externally-blocked decision rule (pilot 023198,
2026-05-17 — scarred below).** A spike can be *complete as a
scoping/derivation doc with a real result* whose **source-of-truth lives
in another repo's unsettled artifact** (e.g. a paper in review). That is
**not** `orphaned` — landing it would import an unsettled cross-repo
result, the exact inverse of primary-source discipline. Rule: *if the
result's source-of-truth is another repo's unsettled artifact, the spike
is `live-or-open` regardless of how complete the local scoping looks;
surface the canon-gap for the owner, do not land.* This recurs —
cross-pollination spikes from the paper portfolio are a known category.

---

## 4. Landing-scope policy (Joseph 2026-05-17 — hybrid)

When a spike is `orphaned` and its result must reach canon:

- **Safe-mechanical moves and tractable/clear landings execute *this
  cycle*.** Per the triage-is-the-answer discipline: the cycle is not the
  taxonomy. The safe subset is not queued for "next housekeeping" — it is
  executed in the cycle that produced the disposition.
- **Substantial segment-authoring landings get a written landing-plan**
  (`spikes/<slug>-spike-integration-plan.md`, audit-routing §4.3) surfaced
  in `PRACTICA.md` (§4.4), and are done deliberately — often best by the
  spike's own authors, who hold the context.

"Tractable" vs "heavy" is itself a judgment the adjudicating agent records
with its disposition (what would the landing touch? one segment's
Discussion, or a new appendix + cascade?). The parent decides the
auto-land/queue split from that.

---

## 5. Directory-label honesty (and its bounded guarantee)

`.integrated/` is a **truth-claim**: *this spike's load-bearing content is
present in canon.* `.archived/` is a distinct honest bucket: *consciously
set down; not in canon; reason recorded.* The two are **not
interchangeable** — collapsing them is the directory-level form of the
label-lies-about-status error that audit-routing §5/§6 spends pages
preventing.

**Bounded guarantee (Joseph 2026-05-17), stated in `spikes/README.md` so
the claim is honestly scoped rather than silently overclaimed:** the
guarantee is **forward and per-cycle**. Spikes a spike-routing cycle files
to `.integrated/` have had their content verified in canon. Pre-policy
residents have **not** — before `.archived/` existed (notably the
2026-05-12 bulk move of 64), some incomplete-and-not-needed spikes may
have been swept to `.integrated/`, and teasing them back out is not worth
the effort. So: *do not retroactively re-audit `.integrated/`*; verify
forward, and let the README carry the caveat.

---

## 6. The dir-spike gold gate (lighter — Joseph 2026-05-17)

File-spikes: agents adjudicate → parent independent-verifies → parent
moves.

Directory-spikes (reasoning-trail clusters — `track-a-intent-dag/`,
`track-b-nonlinear-sims/`, `temporal-nesting-rg/`,
`spike-language-as-causal-substrate/`, `class-coercion-wrapping/`,
`spike-local-embedding-benchmark/`, …): agents may **read and recommend**
a disposition; the disposition is **Joseph-adjudicated in one batch**, not
auto-filed.

Rationale: nothing is ever deleted (both buckets *preserve*; only the live
tree changes), so the audit "summarized into oblivion" risk largely does
not apply here — but dir-spikes carry cross-domain ideation whose value is
orthogonal to "is the math in canon," and a one-batch human read is cheap
insurance. This is **lighter** than the `AUDIT-WORKING-*` standing gate
(`audits/README.md`), which forbids any processing before consult; here
agents may read and recommend, and Joseph adjudicates the batch.

**The axis that actually gates the Joseph batch is decision-type, not
artifact-shape (pilot 023198 — ratified by Joseph 2026-05-17).** The
dir-spike gate above is preserved. But a *file*-spike can also carry a
Joseph-reserved decision — a framework-identity / cross-repo /
promotion-level call (structurally the M4 §5.1 / operator-family-spine
kind). The operative criterion: *route to the Joseph batch anything whose
resolution requires a decision Joseph reserved, file or dir.* This only
ever routes **more** to Joseph (never auto-files something that needed
him); it sharpens, not weakens, the intent behind the "lighter gate"
decision (don't let agents auto-file reserved-judgment calls).

---

## 7. Evidence hierarchy, and the un-trusted label

Decreasing reliability:

1. The spike's own terminal verdict / `## Independent Audit` section, **plus
   a first-hand grep of its load-bearing result-name/claim against `src/`
   and a read of the segment it should live in.** This is decisive.
2. `INDEX.md` cycle-header status — sufficient evidence for **NOT**-integrated
   (an `open`/`blocked`/`IN PROGRESS` label is enough to keep a spike out of
   `.integrated/`); a `LANDED`/`PROMOTED`/`VERDICT` label is a **hypothesis
   to verify**, never sufficient on its own.
3. `CHANGELOG.md` cycle narratives.
4. `TODO.md` / `PROPOSALS.md` / `PRACTICA.md` backlinks (open `[ ]` is
   sufficient for not-integrated; *absence is not* sufficient for
   integrated).

`git`-recency is **poisoned** for this corpus — the AAD→AAT sweep
(2026-05-15), the role-prefix sweep (2026-04-24), and the 2026-05-12
bulk move all rewrote large swaths. Use verdicts and `src/`, not the log.
The INDEX label is the *convenience record*, not ground truth — exactly
as the audit cycle learned its audit-id→ledger mapping was unreliable and
had to be primary-source-verified.

---

## 8. What this defers to `audit-routing-instructions.md`

Everything shared. Specifically: the strengthen-first reflex (§2); the
four completion-states — strengthened-to / -past / no-go / strengthen-failed
(§3); the no-go protocol — `FALSE`-mark, cascade closure, integration
plan, PRACTICA surfacing, then route (§4); the ghost-forms and the
over-rotation correction — *the no-go is canon, not a ghost to exile;
only redundant project-autobiography is demoted to the history layer*
(§5/§6); the meta-stance — this filter is itself unpurified, lead agent
holds the meta-question (§7); route-don't-execute, the disposition enum,
the independent-verify gate (adjudicator ≠ confirmer), the working-dir
lifecycle, the directory-prefix invariant (§8); and the
phenomenology-is-load-bearing voice discipline (§9).

Read that document. This one only says what is *different* about spikes.

---

*Living document. Started 2026-05-17. Iterate as the process is
exercised; record each refinement's scar so the next reader inherits the
reason, not just the rule — this file inherits audit-routing §9's stance
about itself.*

*Refinement 1 (2026-05-17, diagnostic pilot 023198 —
`spike-operator-sector-unification` + `spike-c2-star-to-integrate`).
Three frame defects caught before any fan-out, folded above: (1) no clean
cell for cross-repo / externally-blocked spikes → §3 decision rule
(`spike-c2-star` is `live-or-open` because its proof's source-of-truth is
`~/src/behavioral-floor/`'s in-review paper, not because it is
incomplete); (2) the Joseph-batch gate keyed on file-vs-dir when the
load-bearing axis is reserved-decision-type → §6 criterion
(safe-direction, pending ratification); (3) tightly-coupled sibling
spikes are mis-routable when split across fan-out slices — adjudicating
`spike-operator-sector-unification` forced a check of
`spike-update-operator-sector` (a genuine `orphaned`-suspect, not in
slice), which an agent trusting "the operator family is done" would
mis-route → partition keeps sibling clusters in one slice, siblings
surfaced from outside a slice are flag-don't-route. Confirmed, no change:
the first-hand decisive-test read is non-optional — the INDEX label was
wrong in **both** pilot cases, in **opposite** directions (understated
for spike 1, accurate only by encoding an external block for spike 2).
The transferable scar: the convenience-label is unreliable in both
directions, not only the optimistic one; the first-hand read is budgeted
as mandatory every fan-out slice, not as a spot-check.*
