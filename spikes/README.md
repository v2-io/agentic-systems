# spikes/ — orientation note

This tree is the **research-spike corpus**: reasoning trails. Each spike
attacks one claim — pushing the math and the thinking as far as they go
until the claim yields or until it uncovers, with specificity, why it
cannot. A spike that follows the procedure has a positive result *either
way*: a **no-go is as much a result as a strengthening succeeds**, and is
present-tense canonical truth, not archaeology.

What lives here:

- **`spike-*.md` files and spike directories** — individual reasoning
  trails (some directories are multi-file trail clusters).
- **`INDEX.md`** — the spike index: every spike, its location, current
  status. The status labels are a **convenience record, not ground
  truth** (see the routing docs' evidence hierarchy) — durable; it stays.
- **`PROPOSED.md`** — the **3-perspective spike-proposal index**: a low-friction, *optional* repository for spike-able ideas set down for later (not a mandatory registry — spikes launch friction-free by anyone anytime; it is one of several parallel work-finding avenues). Detail lives in one of three homes — [`PROPOSED-ADVANCED.md`](PROPOSED-ADVANCED.md) (moonshot/theory-edge), the relevant segment's Working Notes (segment-perspective strengthenings — linked, not duplicated), or [`PROPOSED-MISC.md`](PROPOSED-MISC.md) (residual; often near-empty by design). Durable — *placement* (not routed/moved like a spike), **not** content-currency. Two binding disciplines, both about keeping what *is* there trustworthy rather than exhaustive: **freshness** (no stale lies) and the **mutual link** (WN comment ↔ row, where both exist) — *not* completeness ([`../doc/spike-routing.md`](../doc/spike-routing.md) §2-bis(3) + Refinement 10). Durable ≠ frozen; trustworthy ≠ complete.
- **`.integrated/`** and **`.archived/`** — the two terminal homes for a
  spike whose purpose is spent (below).
- Working subdirs (`track-a-intent-dag/`, `track-b-nonlinear-sims/`, …),
  simulation artifacts (`sim-*.py`), and figures.

## The two terminal homes are a truth-claim, not a filing convenience

A spike whose purpose is spent leaves the live tree (it is *not* retained
in place — that breeds the "someone will get to it later" rot; cf.
`audit-routing-instructions.md` §8 working-dir lifecycle). It goes to one
of two homes, and **which one is a claim about the truth**:

- **`.integrated/`** — *this spike's load-bearing content is present in
  the canon* (a segment or appendix), or is itself the no-go that the
  canon now states. Verified first-hand at routing time.
- **`.archived/`** — *consciously set down; the content is **not** in the
  canon, and here is why* (a one-line recorded reason; whether anything
  was salvaged first). Honest about not being integrated.

Collapsing these — sweeping a not-integrated spike into `.integrated/` to
make it disappear — is the directory-level form of the
label-lies-about-its-own-status error the integration discipline exists
to prevent (`audit-routing-instructions.md` §5/§6).

> [!important]
> **The `.integrated/` guarantee is bounded — forward and per-cycle, not
> retroactive (Joseph, 2026-05-17).** Spikes that a *spike-routing cycle*
> files to `.integrated/` have had their content verified in the canon.
> Spikes that predate this policy have **not** — before `.archived/`
> existed (notably the **2026-05-12 bulk move of 64 spikes**), some
> incomplete-and-not-needed spikes may have been swept into `.integrated/`.
> Teasing those back out is not worth the effort and is explicitly **not
> done**. So: `.integrated/` membership is a verified truth-claim *for
> spikes routed under this policy*, and a best-effort historical record
> for everything moved before it. Do not re-audit `.integrated/`; verify
> forward.

## Live work is not routed

A spike whose authors are still in it is **not touched** by a routing
cycle — the authors integrate their own work on their own completion.
Liveness signals and the standing carve-outs are in
[`../doc/spike-routing.md`](../doc/spike-routing.md) §1.

## The governing process

- [`../doc/spike-routing.md`](../doc/spike-routing.md) — the spike-specific
  delta (five-state disposition, directory-label honesty, the live-work
  exclusion, the lighter dir-spike gold gate).
- [`../doc/audit-routing-instructions.md`](../doc/audit-routing-instructions.md)
  — the **shared integration-routing core** (strengthen-first, the no-go
  protocol, the ghost discipline, the meta-stance). The spike doc defers
  into it; it is corpus-agnostic and already written about spikes.
- [`ROUTING.md`](ROUTING.md) — the live spike-routing tracker /
  rendezvous (partition, disposition ledger, log, the honest remaining
  state). Durable and **undated** — the routing *process* is ongoing,
  not a one-shot; it lives here in `spikes/`, **not** in `msc/`
  (delete-at-any-time scratch) and **not** in `audits/` (a different
  corpus). See `../doc/spike-routing.md` §5a for the full directory
  layout.
- [`.routing-trail/`](.routing-trail/) — frozen archaeology of the
  process: per-cycle adjudication / independent-verify / regression
  trails (`SPIKE-{WORKING,VERIFY,REGRESSION}-<id>/`). Preserved as
  written (its `README.md` carries the rosetta for pre-relocation
  paths); load-bearing conclusions are extracted to `ROUTING.md` +
  `.integrated/MANIFEST-*` + `CHANGELOG.md` + canon.

## Naming: read "AAD" here as "AAT"

As with `audits/`, this tree was deliberately not swept by the
AAD→AAT rename (2026-05-15) — it is archival/low-churn and git preserves
the as-written record. When you encounter **"AAD"** in any spike here,
read it as **"AAT"**; the framework, sections, results, and segment slugs
are unchanged — only the name moved. Canonical record of the rename:
[`../CHANGELOG.md`](../CHANGELOG.md) and the *Naming note* in
[`../CLAUDE.md`](../CLAUDE.md).
