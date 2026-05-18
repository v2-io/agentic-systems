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
- **`PROPOSED.md`** — high-risk research-direction *proposals* (not active
  spikes). Durable; it stays.
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
- The current cycle's live tracker is named
  `msc/spike-routing-<date>.md` (the in-flight rendezvous: partition,
  state machine, log).

## Naming: read "AAD" here as "AAT"

As with `audits/`, this tree was deliberately not swept by the
AAD→AAT rename (2026-05-15) — it is archival/low-churn and git preserves
the as-written record. When you encounter **"AAD"** in any spike here,
read it as **"AAT"**; the framework, sections, results, and segment slugs
are unchanged — only the name moved. Canonical record of the rename:
[`../CHANGELOG.md`](../CHANGELOG.md) and the *Naming note* in
[`../CLAUDE.md`](../CLAUDE.md).
