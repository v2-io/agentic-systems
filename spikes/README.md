# spikes/ — how to spike (and what happens after)

> [!note]
> **The 2026-05-19→20 reconsideration of this README is largely resolved (2026-05-30).** The corrected principle is now ratified (D-1) — the cardinal rule below states it: canon cites only canon and the published external world; Working Notes are by definition not canon. The bounded-guarantee callout further down was rewritten (D-3) from a predecessor's abdication into honest un-discharged integration debt: the 2026-05-12 bulk-64 must be verified, or consciously set down, before any wipe. Fully resolved 2026-07-16: the bulk-64 was verified per-spike and its unlanded content landed (`.integrated/VERIFICATION-2026-07-16.md`), the buckets re-sorted honestly, and the "wipe" dissolved — it was a teaching hypothetical, never a directive; both directories are permanent. Still open: the citation-infrastructure build (G3), tracked in [`../INTEGRATION-CLEANUP-TODO.md`](../INTEGRATION-CLEANUP-TODO.md).

This tree is the **research-spike corpus**: reasoning trails. A spike attacks one claim — pushing the math and the thinking as far as they go until the claim yields, or until it uncovers, with specificity, *why it cannot*. A spike that follows the procedure has a positive result **either way**: a no-go is as much a result as a strengthening, and it is present-tense canonical truth, not archaeology.

---

## If you're here to spike something (this is all you need)

**Go ahead.** You do not need permission, a ticket, a plan review, or any of the machinery further down. The convention is exactly: *spike it in `spikes/`.* Reading the recovery-team SOPs is **never** a precondition for spiking — it's for the cleanup crew and for heavy self-integration; you can spike excellently having read only this section.

- **Keep your stuff together.** One `spike-<subject>.md`, or one directory with sub-files if it grows into a cluster. Everything for this spike in that one place — so it can be picked up cold.
- **Say what you're attempting, and the context, early** (top of the file, or a `00-brief`). Write it for a stranger — possibly future-you — who has to pick this up with no memory of why. This one habit is the difference between an interruptible spike and a lost one.
- **Push.** Keep going until it yields or until you can say *precisely* why it can't. Try the improbable; try the angle that looks unlikely; revisit the assumptions you started with; follow the promising unexpected line even when it's not where you meant to go — unexpected destinations are often the real result. Resistance is usually the signal to push or reframe, **not** to abandon: a genuinely malformed spike is rarer than it feels in the moment, so reach for "set it down" slowly.
- **When you set it down, leave a result.** Unless you're actively chasing a better destination, end with a summary of what you found — a `RESULTS` file if it's a directory — *and* your proposed integration steps (or an `INTEGRATION` file). The summary is the signal that it is **no longer being actively worked**. If you stop *without* a result, say so where it's visible — "incomplete; last on X; next was going to be Y." An honest "not done" is worth far more than silence; silence is exactly what makes a spike expensive to recover later.
- **A no-go is a result — write it up like one.** If you found why the claim can't hold, that is canon-bound truth: state it, propose its integration like any other result. It does **not** get quietly dropped or sent to `.archived/` for "failing." Finding a sharp no-go is a success of the procedure.

**If you (or a peer) integrate the result into the canon yourselves** — get independent reviewers and attestations first (don't self-certify a canon landing), then clean up: move the spent spike to `.integrated/` (its load-bearing content, or its no-go, is now in the canon) or to `.archived/` (it had **no canon material** — pure verification/feedback scaffolding, or a spike that turned out genuinely malformed). `.archived/` is *not* where no-gos go; a no-go has canon material.

**The cardinal rule for any canon integration** — the one thing we really care about here:

1. The math **lands in the segment**, self-contained and in present-tense segment-voice.
2. **Working Notes are, by definition, not canon** — a free working attachment to the segment; that (plus CHANGELOG / the history layer) is the *only* place a spike (or audit / `msc/` / tracker) breadcrumb belongs — for *forward-work* content (per FORMAT.md §"What earns a Working Note"). Not-canon is not a license for vanity-changelog or unneeded breadcrumbs; a breadcrumb no future work needs pins the spike in place (§2-bis(2)). **Everything else in a segment is canon, and canon cites only canon** — zero references to any process artifact, *not* "none needed," *none*. (Which fields/sections exist, and which count as canon vs Working-Note, is FORMAT.md's + the build-pipeline's authority, not this README's — narrative and other segment types are canon too; the one spike-discipline-relevant line is Working-Notes-↛-canon. The separate "*need*, not *mention*" test is for spike-*archivability*, not this boundary.)
3. **A no-go is valid math** and lands as present-tense canon, not as nothing.

In short: *we don't throw valid math away (a no-go included); canon cites only canon; spike breadcrumbs live in Working Notes, which by definition aren't canon.*

**Optional, never required — the recovery team.** There is an agent (with help) that works the backlog of spikes sitting here but not yet integrated. You can make their job easier if you like: add your spike to [`INDEX.md`](INDEX.md), keep its row updated there (and in the [`PROPOSED*`](PROPOSED.md) files if it's listed there) while in progress, and list it in `.integrated/MANIFEST-<date>.md` once it's cleaned up. **None of this is required to spike** — it's a courtesy to the cleanup crew, not a tax on you. How that team thinks (no-go integration, the ghost discipline, strengthen-before-soften, the disposition states) lives in [`../doc/sop/spikes.sop.md`](../doc/sop/spikes.sop.md) + [`../doc/audit-routing-instructions.md`](../doc/audit-routing-instructions.md) — read it only for a heavy self-integration or out of curiosity.

---

## For the spike-recovery team (you do not need any of this to spike)

Everything below serves the cleanup crew and heavy self-integrations. It is preserved here deliberately — restructured below the line, not discarded (the cardinal rule, applied to this file itself).

**What lives here.** `spike-*.md` files and spike directories (reasoning trails; some directories are multi-file clusters); [`INDEX.md`](INDEX.md) — the spike index, every spike / location / current status (the status labels are a *convenience record, not ground truth* — see the routing docs' evidence hierarchy; durable, it stays); [`PROPOSED.md`](PROPOSED.md) — the 3-perspective spike-proposal index, a low-friction *optional* repository for spike-able ideas set down for later (detail in [`PROPOSED-ADVANCED.md`](PROPOSED-ADVANCED.md) / a segment's Working Notes / [`PROPOSED-MISC.md`](PROPOSED-MISC.md); two binding disciplines — *freshness* and the *mutual link* — explicitly **not** completeness; `../doc/sop/spikes.sop.md` §2-bis(3) + Refinement 10); `.integrated/` and `.archived/` (the two terminal homes, below); working subdirs, `sim-*.py`, figures.

### The two terminal homes are a truth-claim, not a filing convenience

A spike whose purpose is spent leaves the live tree (it is *not* retained in place — that breeds the "someone will get to it later" rot; cf. `audit-routing-instructions.md` §8 working-dir lifecycle). It goes to one of two homes, and **which one is a claim about the truth**:

- **`.integrated/`** — *this spike's load-bearing content is present in the canon* (a segment or appendix), or is itself the no-go the canon now states. Verified first-hand at routing time.
- **`.archived/`** — *consciously set down; the content is **not** in the canon, and here is why* (a one-line recorded reason; whether anything was salvaged first). Honest about not being integrated.

Collapsing these — sweeping a not-integrated spike into `.integrated/` to make it disappear — is the directory-level form of the label-lies-about-its-own-status error the integration discipline exists to prevent (`audit-routing-instructions.md` §5/§6).

> [!important]
> **The `.integrated/` guarantee is forward and per-cycle.** A spike files to `.integrated/` only after its content has been first-hand verified in the canon (the 2026-05-12 bulk move of 64 spikes, which predated that rule, was verified per-spike on 2026-07-16 — `.integrated/VERIFICATION-2026-07-16.md` — so the label is now true for every member). `.integrated/` and `.archived/` are permanent; there is no wipe.

### Live work is not routed

A spike whose authors are still in it is **not touched** by a routing cycle — the authors integrate their own work on their own completion. Liveness signals and the standing carve-outs are in [`../doc/sop/spikes.sop.md`](../doc/sop/spikes.sop.md) §1.

### The governing process

- [`../doc/sop/spikes.sop.md`](../doc/sop/spikes.sop.md) — the spike-specific delta (five-state disposition, directory-label honesty, the live-work exclusion, the lighter dir-spike gold gate, the PROPOSED freshness/mutual-link discipline).
- [`../doc/audit-routing-instructions.md`](../doc/audit-routing-instructions.md) — the **shared integration-routing core** (strengthen-first, the no-go protocol, the ghost discipline, the meta-stance). The spike doc defers into it; it is corpus-agnostic and already written about spikes.
- [`ROUTING.md`](ROUTING.md) — the live spike-routing tracker / rendezvous (partition, disposition ledger, log, the honest remaining state). Durable and **undated** — the routing *process* is ongoing, not a one-shot; it lives here in `spikes/`, **not** in `msc/` (delete-at-any-time scratch) and **not** in `audits/` (a different corpus). See `../doc/sop/spikes.sop.md` §5a for the full directory layout.
- [`.routing-trail/`](.routing-trail/) — frozen archaeology of the process: per-cycle adjudication / independent-verify / regression trails (`SPIKE-{WORKING,VERIFY,REGRESSION}-<id>/`). Preserved as written (its `README.md` carries the rosetta for pre-relocation paths); load-bearing conclusions are extracted to `ROUTING.md` + `.integrated/MANIFEST-*` + `CHANGELOG.md` + canon.

### Naming: read "AAD" here as "AAT"

As with `audits/`, this tree was deliberately not swept by the AAD→AAT rename (2026-05-15) — it is archival/low-churn and git preserves the as-written record. When you encounter **"AAD"** in any spike here, read it as **"AAT"**; the framework, sections, results, and segment slugs are unchanged — only the name moved. Canonical record of the rename: [`../CHANGELOG.md`](../CHANGELOG.md) and the *Naming note* in [`../CLAUDE.md`](../CLAUDE.md).
