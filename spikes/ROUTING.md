# Spike-routing — live tracker (started 2026-05-17)

The in-flight rendezvous for the spike-backlog routing cycle. Governing docs: [`../doc/sop/spikes.sop.md`](../doc/sop/spikes.sop.md) (the spike-specific SOP) + [`../doc/audit-routing-instructions.md`](../doc/audit-routing-instructions.md) (shared integration-routing core). This file holds *cycle state*, not governing content.

> Term discipline (inherited from audit-routing §8): this is the **routing tracker**, not "the spine." "Spine" is reserved for the theory's critical path.

> Pruned to live state 2026-07-15 (Joseph's done-items-out-of-trackers directive). The 2026-05-17→19 routing-cycle log, partition, fan-out/verify ledgers, and executed dispositions were removed; their narratives live in CHANGELOG (2026-05-17, 2026-05-18, 2026-05-19, 2026-05-21), the MANIFESTs (`.integrated/MANIFEST-2026-05-17.md`, `-2026-05-19.md`), and the frozen trails under `spikes/.routing-trail/`.

## The job (Joseph's framing, 2026-05-17)

Route everything in `spikes/` so we know which spikes are and are not properly integrated into the theory canon. The recurring failure: *the meat of the math (or a no-go) was left only in the spike — sometimes referenced from a segment, sometimes not.* Positive results (every correctly-run spike has one, **no-gos included**) got orphaned by busy-ness; some are fully accounted for but never moved; some are incomplete and not needed. The deliverable is each spike *where its truth belongs*, with the safe subset executed in the same cycle (the cycle is not the taxonomy).

Joseph's decisions binding this cycle:

- **Landing scope: hybrid.** Auto-land the tractable, queue the heavy (`spikes.sop.md` §4).
- **`.archived/`: yes, two-way honest split** — with the **bounded, non-retroactive guarantee** documented in `spikes/README.md` (do not re-audit `.integrated/`; the 2026-05-12 bulk-64 is not re-sorted).
- **Dir-spike gold gate: lighter** — agents read+recommend, Joseph adjudicates the dir-spikes in one batch (`spikes.sop.md` §6).

## Evidence hierarchy

In [`../doc/sop/spikes.sop.md`](../doc/sop/spikes.sop.md) §7. Decisive test: load-bearing content in `src/`, verified first-hand. INDEX label = a hypothesis, never sufficient for *integrated*. `git`-recency poisoned by three sweeps (git *provenance* — pickaxe / blame / `log --follow` — is the sharpest non-destructive instrument).

## State machine (per spike)

`unexamined → adjudicated (state + recommended home, reasoning written) → verified (independent primary-source spot-check of the content-in-src claim, by an agent other than the adjudicator) → {integrated | archived | live-or-open} (MANIFEST entry + git mv) | queued (heavy landing → integration-plan + PRACTICA)`. Reversible until the durable batch (MANIFEST write + `git mv`). Independent-verify gate is in the state machine, per audit-routing §8.

## Delegation design

Parent (with Joseph) owns: the partition, primary-source spot-checks, all routing **actions** (`git mv`, `.archived/` moves, MANIFEST entries, tractable canon landings, queuing heavy landings, commits), and the dir-spike batch surfaced for Joseph. Agents own: first-hand per-spike adjudication + recommended disposition + tractable-vs-heavy assessment — **report only, no moves/edits/commits/segment-changes** (constrain by framing since Bash can't be withheld from a reasoning agent; verify state after — audit-routing §8, `feedback_subagent_destructive_action`).

Adjudications write to `spikes/.routing-trail/SPIKE-WORKING-<six digits>/` — a working-dir class alongside `AUDIT-WORKING-*` (de-novo cognition) and `ADJUDICATION-WORKING-*` (audit-backlog triage). *Directory-prefix invariant (convention SOP, silent-corruption risk): the six-digit ID is identity, the prefix is the class; never blanket-rewrite one prefix to another.*

## Coupled landing clusters (parent-owned; reconcile recommendations into these)

Cross-slice couplings surfaced by the sibling rule. The parent holds these so independent recommendations are **reconciled into one landing**, never isolate-landed (three parallel half-segments of one appendix is the `PROPOSALS.md:268` failure).

- **CL-1 — `#dissipativity-template` / SP-22 ($\gamma$)-hybrid bundle** (surfaced 2026-05-17). Members: `spike-passivity-composition` (heterogeneous-storage-function composition payoff + the `#dissipativity-template` appendix — Willems route), `spike-pid-a2prime` (the explicit $\alpha_{\text{PID}}$/B1 derivation, KYP route — same $\alpha$/$\beta$-repartition territory), and `spike-bridge-lemma-nonlinear-strengthening-2026-04-24` §7.2 (targets the *same* appendix; the spike file's §7.1 is verified integrated but the file is HELD out of `.integrated/` until CL-1 lands, so the directory doesn't lie). SP-22's architectural gate was resolved 2026-05-14, so this is straight authoring, not an architectural call — **one HEAVY landing, one integration-plan, one PRACTICA surface.** Do not isolate-land any member. (The §8 adversarial no-go from `spike-passivity-composition` is *already* canon at `result-contraction-template.md:148` — correctly; CL-1 is only the not-yet-landed heterogeneous-composition payoff.)

## Joseph batch (reserved-decision items — assemble, do not auto-file)

Per `spikes.sop.md` §6 (decision-type gate, ratified). Surface together; each is a present-truth call Joseph reserved.

- **`spike-language-as-causal-substrate/` theoretical orphan** — Theorem-1 (discourse-act → Pearl L2, derivation-grade) lives only in the spike; landing is a reserved promotion call (new AAT appendix grade + Synthese cross-cite). Same family as the **C2★ gap** (`der-loop-interventional-access:76` still only *asserts* the (C2) violation the external `~/src/behavioral-floor/` AIES paper *derives* as (C2★)) — show them together.
- **`spike-attention-governance` archived-vs-research-seed** — is finite-attention a missing postulate or an IB/temporal-nesting consequence? Truth-call, not a filing op. `spike-attention-causal-graphs` is verified integrated but its `git mv` is **coupled** to this decision (same `446c7a1` cluster) — do not fire alone.
- **`temporal-nesting-rg/` Moves B/C/D** — `integrated-misfiled` for its landed core, **but** hold the `git mv` for the Joseph batch: the B/C/D + temporal-nesting-Discussion decision he was owed (`class-coercion-wrapping/INTEGRATION-PLAN.md:221`, never adjudicated) rides with it; auto-filing silently drops it.
- **Dir-spike batch (§6 lighter gold-gate — read+recommend done, his call):** `class-coercion-wrapping/`, `track-a-intent-dag/`, `track-b-nonlinear-sims (→ empirica/track-b-nonlinear 2026-07-16)/` — verified `integrated-misfiled`, content in canon, no reserved theory decision; a clean/fast yes expected, but his per the gate he set.

## Next actions (the honest remaining state)

1. **CL-1** (`#dissipativity-template`: passivity-composition + pid-a2prime + bridge §7.2) — heavy coupled landing; integration-plan owed; queued in PROPOSALS §D.9 / TODO. Not yet regression-cleared (gate before landing, per `spikes.sop.md` §2a).
2. **`spike-update-operator-sector` tractable landing** — regression-cleared 2026-05-17; honestly *pending, not done*. Clean part = $\alpha_{\text{op}}$/$\beta_{\text{op}}$ sub-list refresh into `#deriv-sector-condition` (mirror the already-landed mismatch-layer recast) + cross-ref into `#disc-identifiability-floor`; no new appendix/cascade. *Non-loss (integration-is-replacement):* the §4.3 no-go's **operator-layer** manifestation must reach `#disc-identifiability-floor` as present-tense canon — covering it as "Instance 2 already" without the operator-layer line is the subtle replacement failure. The §266(iii)-vs-§8.2 placement is a whole-corpus call — parent decides at landing. Verify state before finishing.
3. **Joseph-batch items** (above) — assembled, untouched.
4. **Cycle-close spike moves (2026-08-22 drain, first-hand).** `spike-rho-factorization` **filed** (no-go first-hand in `#internal-external-decomposition`; MANIFEST-2026-08-22). **Held, not filed:** `spike-rho-additive-variance-strengthening-2026-04-24` — `#rho-decomposition` (the AV-theorem appendix it recommended) **never existed**; distinctive payload is `orphaned`, heavy landing, not a filing op. `spike-neutral-drift-endogenous-coupling-strengthening-2026-04-24` — §8/§10.1 in canon; remainder beyond that thread still lives only in the spike (its own header says so); held. (The resolution / triage / rho-recheck feed spikes were already moved.)

## Broader scope — subordinate carrying-list

The 2026-05-19→20 deeper-truth turn (canon-resident process-artifact references; the sim/empirical class; the unverified 2026-05-12 bulk-64; the missing citation infrastructure) is carried durably in [`../INTEGRATION-CLEANUP-TODO.md`](../INTEGRATION-CLEANUP-TODO.md) — the next agent works from that TODO first, then this tracker's items as applicable. Status as of 2026-07-14 (CHANGELOG): D-1 ratified 2026-05-30; open remainder D-2 / bulk-64 + G3.
