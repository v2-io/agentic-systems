# Spike-routing — live tracker (started 2026-05-17)

The in-flight rendezvous for the spike-backlog routing cycle. Governing
docs: [`../doc/spike-routing.md`](../doc/spike-routing.md) (spike delta) +
[`../doc/audit-routing-instructions.md`](../doc/audit-routing-instructions.md)
(shared integration-routing core). This file holds *cycle state*, not
governing content — partition hypotheses, the state machine, the
delegation design, the log, and the gated next-actions.

> Term discipline (inherited from audit-routing §8): this is the
> **routing tracker**, not "the spine." "Spine" is reserved for the
> theory's critical path.

## The job (Joseph's framing, 2026-05-17)

Route everything in `spikes/` so we know which spikes are and are not
properly integrated into the theory canon. The recurring failure: *the
meat of the math (or a no-go) was left only in the spike — sometimes
referenced from a segment, sometimes not.* Positive results (every
correctly-run spike has one, **no-gos included**) got orphaned by
busy-ness; some are fully accounted for but never moved; some are
incomplete and not needed. The deliverable is each spike *where its truth
belongs*, with the safe subset executed in the same cycle (the cycle is
not the taxonomy).

Joseph's decisions binding this cycle:

- **Landing scope: hybrid.** Auto-land the tractable, queue the heavy
  (`spike-routing.md` §4).
- **`.archived/`: yes, two-way honest split** — with the **bounded,
  non-retroactive guarantee** documented in `spikes/README.md` (do not
  re-audit `.integrated/`; the 2026-05-12 bulk-64 is not re-sorted).
- **Dir-spike gold gate: lighter** — agents read+recommend, Joseph
  adjudicates the dir-spikes in one batch (`spike-routing.md` §6).

## Evidence hierarchy

In [`../doc/spike-routing.md`](../doc/spike-routing.md) §7. Decisive test:
load-bearing content in `src/`, verified first-hand. INDEX label = a
hypothesis, never sufficient for *integrated*. `git`-recency poisoned by
three sweeps.

## Partition (hypotheses — to be VERIFIED, not assumed)

29 top-level `spike-*.md` + 7 working subdirs + loose files. ~81 already
under `.integrated/` (+ a `MANIFEST-2026-05-12.md`). Grouped by *what
evidence is expected to govern disposition*; status starts `unexamined`.
Derived from `INDEX.md` cycle headers — the headers are the hypothesis
source, not the verdict.

- **Group LIVE (step-zero exclude).** `spike-self-actuation-grounding.md`,
  `spike-wf-strengthening.md` (INDEX 2026-05-17, P1–P4 blocked,
  Joseph-affirmed active); `visual/` (INDEX 2026-05-15 ACTIVE).
  *Liveness-check first, fail-safe to hands-off:* `spike-c2-star-to-integrate.md`
  (INDEX 2026-05-14 "IN FLIGHT"), `spike-language-as-causal-substrate/`
  (2026-05-13 IN PROGRESS), `spike-strategic-self-coupling.md` (2026-05-09
  IN PROGRESS). `INDEX.md`, `PROPOSED.md` — durable, stay (not routed).
- **Group LANDED-CLAIMED.** INDEX says LANDED/PROMOTED/VERDICT → *expected*
  `integrated`; the label is the hypothesis, content-in-`src/` is the
  test. The 2026-04-22/23 "ALL PROMOTED", 2026-04-23 brainstorm "ALL SEVEN
  PROMOTED", 2026-04-23 Gap A/B "PROMOTIONS LANDED", 2026-04-24 Gemini
  "TIER 1 LANDED" (the `*-2026-04-24` strengthening spikes),
  `spike-stochastic-non-exit-strengthening-2026-05-16` (Model-S, state-3
  no-go LANDED), the operator-family "VERDICT REACHED" pair
  (`spike-operator-sector-unification.md`, `spike-update-operator-sector.md`),
  the 2026-05-12 five-stage cycle.
- **Group BULK-2026-05-12.** The ~81 already under `.integrated/` (+
  MANIFEST). Hypothesis: `integrated-filed`. Job: **sample-verify**
  content-in-canon for a representative subset + record the bounded-guarantee
  caveat; **not** an exhaustive re-audit (Joseph's non-retroactive call).
- **Group ORPHAN-SUSPECT.** Top-level `spike-*.md` not inside a
  LANDED-claimed cycle and INDEX-silent or open. Primary work; first-hand:
  result real? in canon / referenced-only / nowhere? tractable vs heavy
  landing? Includes (hypothesis only) `spike-alignment-impossibility`,
  `spike-fep-suboptimal-approximation`, `spike-*-gaps`
  (composition/strategy-dynamics), `spike-message-passing-credit-assignment`,
  `spike-transient-dependency-amplification`, the `*-strengthening-2026-04-24`
  set if not LANDED, `neurips-back-integration-2026-05-08.md` (42KB
  integration doc — check disposition).
- **Group DIR (lighter gold gate — Joseph batch).** `class-coercion-wrapping/`
  (likely `integrated-misfiled` — `#der-class-coercion-via-wrapping`
  landed), `spike-local-embedding-benchmark/` (likely belongs to the
  `~/src/intrinsically-causal-language/` sibling, not `.integrated/`),
  `track-a-intent-dag/`, `track-b-nonlinear-sims/`, `temporal-nesting-rg/`,
  `spike-language-as-causal-substrate/` (also liveness-check).
- **Loose.** `sim-three-way-tradeoff.py` (53KB sim — disposition follows
  its parent spike's), `neurips-back-integration-2026-05-08.md` (see
  ORPHAN-SUSPECT).

**Sibling-coupling (pilot 023198 refinement).** Tightly-coupled spike
clusters go in **one fan-out slice**, not split — split slices mis-route
a sibling an agent assumes is "done with the family." Known cluster: the
operator-family — `spike-operator-sector-unification` (pilot:
`integrated-misfiled`), `spike-update-operator-sector` (pilot-flagged:
`orphaned`-suspect, no `#update-operator` segment), and the archived
`spike-operator-family-unification/` (the strengthener that landed
`result-certificate-existence`). A sibling surfaced from *outside* a
slice is **flag-don't-route**.

## State machine (per spike)

`unexamined → adjudicated (state + recommended home, reasoning written)
→ verified (independent primary-source spot-check of the content-in-src
claim, by an agent other than the adjudicator) → {integrated | archived |
live-or-open} (MANIFEST entry + git mv) | queued (heavy landing →
integration-plan + PRACTICA)`. Reversible until the durable batch
(MANIFEST write + `git mv`). Independent-verify gate is in the state
machine, per audit-routing §8.

## Delegation design

Parent (me, with Joseph) owns: the partition, primary-source spot-checks,
all routing **actions** (`git mv`, `.archived/` moves, MANIFEST entries,
tractable canon landings, queuing heavy landings, commits), and the
dir-spike batch surfaced for Joseph. Agents own: first-hand per-spike
adjudication + recommended disposition + tractable-vs-heavy assessment —
**report only, no moves/edits/commits/segment-changes** (constrain by
framing since Bash can't be withheld from a reasoning agent; verify state
after — audit-routing §8, `feedback_subagent_destructive_action`).

Adjudications write to `audits/SPIKE-WORKING-<six digits>/` — a new
working-dir class alongside `AUDIT-WORKING-*` (de-novo cognition) and
`ADJUDICATION-WORKING-*` (audit-backlog triage). *Directory-prefix
invariant (convention SOP, silent-corruption risk): the six-digit ID is
identity, the prefix is the class; never blanket-rewrite one prefix to
another.* Coined this cycle — recorded here so it is not silent.

Cadence: **two-shot pilot first** (one agent on a representative slice,
also reporting what about the frame was unclear → refines this tracker →
fresh fan-out on the refined frame; the pilot's *output refines the
prompt*, it is not fed to the fan-out agents). Then parallel fan-out by
group, independent-verify pass, parent routes + moves + commits per batch;
dir-spikes batched for Joseph.

### Pilot brief (authored deliberately, second-pass-disciplined; launched as-is)

> You're a co-owner helping route this theory project's spike backlog. The
> standard: every spike ends up *where it belongs* — its real content
> either present in the canon (a segment/appendix), or itself a no-go the
> canon now states, or honestly recorded as deliberately-not-in-canon —
> so the spike can be retired without losing truth. The failure this
> exists to catch: math or a no-go that is real and true but lives only
> in the spike (sometimes referenced from a segment, sometimes not — a
> reference is not integration).
>
> Orient on `CLAUDE.md`; `doc/audit-routing-instructions.md` (the shared
> integration-routing core — strengthen-before-soften §2, the four spike
> completion-states §3, the no-go protocol §4, the ghost discipline §5/§6
> — already written about spikes); `doc/spike-routing.md` (the
> spike-specific delta — the five-state disposition, directory-label
> honesty, the live-work exclusion); and `msc/spike-routing-2026-05-17.md`
> (this tracker — the partition hypotheses, and the one piece of hard-won
> project context worth foregrounding: the decisive test for "integrated"
> is the content verified first-hand in `src/`, *not* the INDEX status
> label, which this project has repeatedly found to be a convenience
> record rather than ground truth; and the live, counterintuitive reflex
> — a spike that looks like it wants softening gets a strengthening
> attempt first, because most strengthenings succeed and the rest become
> no-gos worth more than the soften).
>
> Slice for you: `spikes/spike-c2-star-to-integrate.md` and
> `spikes/spike-operator-sector-unification.md`. Write your adjudication
> and reasoning to `audits/SPIKE-WORKING-<your six digits>/`. The routing
> actions — moves, edits, commits, canon landings — are the parent's;
> your deliverable is the adjudication and your judgment about where each
> belongs and why.
>
> Your judgment may exceed mine and you'll meet context I can't see from
> here; "what most benefits the project" overrides "what conforms to this
> brief." This is also a frame-diagnostic run: when you reach the point
> where you know what you'll do — or hit what's genuinely unclear or
> underspecified about the frame, or a better way to help I haven't
> anticipated — stop and report back. What you surface refines the brief
> before more agents run.

## Log

- **2026-05-17 (a)** — Cycle set up. Governing docs authored
  (`doc/spike-routing.md` — thin companion deferring into the shared
  audit-routing core; `spikes/README.md` + `spikes/.archived/README.md` —
  directory-label honesty + bounded non-retroactive guarantee). Partition
  hypotheses seeded from INDEX cycle headers (to verify, not assume).
  Two-shot diagnostic pilot launched on `spike-c2-star-to-integrate` +
  `spike-operator-sector-unification`. Flagged for Joseph: recommended
  reciprocal head-note in `audit-routing-instructions.md` (authoritative
  SOP — §7, not rescoped unilaterally); `SPIKE-WORKING-*` prefix coinage.
- **2026-05-17 (b)** — Pilot 023198 returned.
  Adjudication: `audits/SPIKE-WORKING-023198/adjudication.md` (all
  content-in-canon claims first-hand-verified with named loci for a
  confirmer ≠ pilot).
  - **`spike-operator-sector-unification` → `integrated-misfiled`.**
    Completion-state (B) strengthened-past: the successor
    `spike-operator-family-unification/` [already archived] took its
    O-BP10 gate as a strengthening target → `result-certificate-existence.md`
    (`status: exact`) + `disc-stability-certificate.md`; the plural no-go
    is canonized. Every load-bearing claim verified present in `src/`;
    nothing spike-only. INDEX entry stale/self-contradictory (calls a
    top-level file its own `.integrated/` "predecessor") — reconcile to
    `integrated-filed` at cycle close. *Pending independent-verify
    (confirmer ≠ pilot) before `git mv`.*
  - **`spike-c2-star-to-integrate` → `live-or-open` (cross-repo,
    externally-blocked).** Source-of-truth proof in
    `~/src/behavioral-floor/` (AIES paper, in review). Stays put; no
    landing this cycle. Real canon gap **surfaced for Joseph, not
    actioned**: `der-loop-interventional-access:76` still only *asserts*
    the (C2) violation the external paper *derives* as (C2★); promotion
    level is a reserved call and the strengthening is already running
    externally.
  - Frame defects folded into `doc/spike-routing.md` (Refinement 1,
    scarred): cross-repo decision rule (§3); Joseph-batch axis =
    reserved-decision-type, not file/dir (§6, safe-direction pending
    Joseph ratification); sibling-cluster slicing (partition, below).
    Confirmed, no change: the first-hand decisive-test read is
    non-optional — the INDEX label was wrong in **both** pilot cases, in
    opposite directions.
  - **`spike-update-operator-sector.md`** flagged by the pilot
    (sibling-spillover, outside slice): genuine `orphaned`-suspect — no
    `#update-operator` segment exists; 2026-05-14 CHANGELOG decoupled it
    as live "(γ)-hybrid triage". Captured for the operator-family slice;
    flag-don't-route until adjudicated in that slice.
- **2026-05-17 (c)** — Joseph ratified the gold-gate axis evolution
  (decision-type, not file/dir). `spike-routing.md` §6 now settled.
  Checkpoint committed; fan-out next.

## Next actions (gated; the cycle is not the taxonomy)

1. ~~Pilot returns → fold frame defects~~ **done (2026-05-17 b)** —
   Refinement 1 scarred into `doc/spike-routing.md`.
2. *Surfaced for Joseph:* (a) gold-gate axis evolution — **ratified
   2026-05-17**, now settled in `spike-routing.md` §6 (route any
   reserved-decision spike, file or dir, to the Joseph batch);
   (b) the C2★ canon gap at `der-loop-interventional-access:76` — his
   reserved promotion-level call, externally blocked; non-blocking,
   awaits the paper settling.
3. Launch fresh fan-out by partition group (operator-family as one
   coupled slice) → independent-verify pass (confirmer ≠ adjudicator;
   first pending item: the pilot's `spike-operator-sector-unification`
   `integrated-misfiled` claim).
4. Parent executes the safe subset **this cycle**: `integrated-misfiled`
   `git mv`s, tractable landings, `.archived/` moves with recorded reasons.
5. Heavy landings → integration-plan + PRACTICA surfacing.
6. Dir-spikes (+ reserved-decision file-spikes) → one batch for Joseph.
7. MANIFEST updated; `spikes/INDEX.md` reconciled to post-cycle truth.
