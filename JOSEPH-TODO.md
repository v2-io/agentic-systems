# JOSEPH-TODO — decisions and judgment routed to Joseph

> [!note]
> **What this is.** One queue of the open items that genuinely need Joseph's decision or taste — gathered here so they don't hide scattered through the trackers. Each entry states the decision, the lead's lean where there is one, and a pointer to where the full context lives. **Context is not duplicated here** (defer-don't-fork) — follow the pointer. Agent-actionable work stays in `TODO.md` / `PROPOSALS.md` / the cleanup trackers; this file is only the Joseph-gated subset.
>
> **Convention (for agents).** When you hit a fork that is genuinely Joseph's — taste, blast-radius, publication-path, or a "did this actually come from Joseph?" SOP question — add a one-line entry here pointing at the full context, and **proceed on everything not blocked by it.** Remove an entry when Joseph decides it (migrate the decision to the relevant tracker / CHANGELOG).
>
> Priming-heavy — auditor-hidden, like `TODO.md` / `PROPOSALS.md`.

## SOP consolidation (active work, June 2026)

- **WN-discipline coherence gate.** (a) **A vs B** — lead's lean **B** (single-source the Working-Notes discipline in FORMAT; the other ~5 sites reference it, not restate it). (b) **Scope** — project-only, or extend to the global `~/.claude/` layer where the rule also lives. → full inventory + sketched edits in [`msc/wn-discipline-coherence-pass-2026-05-31.md`](msc/wn-discipline-coherence-pass-2026-05-31.md) §6.
- **`doc/sop/` master index.** Build `doc/sop/sop.md`, or would it be too redundant with CLAUDE.md's index? Deferred by ratified decision #3 ("gather + order first; build the entrypoint later"). → [`doc/sop/sop-creation.sop.md`](doc/sop/sop-creation.sop.md), [`msc/sop-consolidation-design-2026-06-01.md`](msc/sop-consolidation-design-2026-06-01.md) (Ratified §3).
- **Global `~/.claude/` SOP pass — timing.** Project-layer is ratified first; the global CLAUDE.md is also overloaded and carries ASF-specific material to mine. When to run the successor pass. → `doc/sop/sop-creation.sop.md` §"Near-future work to mine".

## TODO-freshness flags (surfaced 2026-06-02 by bin/check-links)

- **NeurIPS back-integration TODO section** is framed as a one-shot 2026-05-08 queued plan, but the work is now a *standing proactive workstream* (the `project_neurips_backport_workstream` memory + CHANGELOG). Reframe/slim to a pointer — *not* delete (work is open)? → [`TODO.md`](TODO.md) §"NeurIPS 2026 back-integration overview".
- **`msc/domain-xfer-candidates.md`** (live — six open transfer questions) now points at the superseded `_obs/` catalog (repointed there for now); modernize its findings reference to the current home (`impl-*` segments + `FINDINGS.md`), and consider a freshness pass on the doc itself.
- **A full TODO-freshness pass.** `check-links` can't see a finished item that has no broken link; pruning landed items + migrating narrative to CHANGELOG (the prune-completed-from-trackers discipline) is worthwhile house-cleaning. Lead can take this — flag if you'd rather scope it yourself.

## Standing reserved decisions (carried from the cleanup trackers)

- **D-2 — bulk-64 `.integrated/` wipe.** Semantics (rm+commit vs history-purge), timing, scope. → [`INTEGRATION-CLEANUP-TODO.md`](INTEGRATION-CLEANUP-TODO.md).
- **G3 / D-citation — citation infrastructure.** Prose-embedded scholarly citations vs `\cite{}` discipline (the Relata agent recommends *not* auto-rewriting segments — voice territory). Publication-critical-path. → `INTEGRATION-CLEANUP-TODO.md` §G3, [`FORMAT-TODO.md`](FORMAT-TODO.md).
- **`#schema-strategy-persistence` hard-ceiling convention** — adjudication verdict B (name the convention, keep `status: exact`); your ratification. → [`NEXT-UP.md`](NEXT-UP.md) (commit `aedc72d`).
- **Two exploratory-spike findings** — the `#def-auxilia-hierarchy` necessity over-claim (separate-substrate is sufficient, not necessary) + the goal-flow-duality discussion-grade landing. → [`TODO.md`](TODO.md).
- **SP-27** — introspective-fork-undetectability, the Part-I ↔ Part-IV (moral-core) bridge: placement / framing. → [`PROPOSALS.md`](PROPOSALS.md).
- **SP-29** — `#disc-infrastructure-as-active-monitor` meta-segment candidate (gated: verify constituents first-hand + check `~/src/practica`). → [`PROPOSALS.md`](PROPOSALS.md).

## Prose / pedagogy (your taste is load-bearing)

- **Greek-vocabulary prose discipline.** Per term: tighten segment prose so the Greek distinction does real work, vs soften the README claim to honest scope. → [`TODO.md`](TODO.md) §"Greek vocabulary prose discipline".
- **README v2 pass.** Alan Walton's first-human read (found it "extremely academic"); the casual-curious-reader tier. → [`TODO.md`](TODO.md) §"README v2 pass".
