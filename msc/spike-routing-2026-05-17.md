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

## Fan-out slices (launched 2026-05-17 e)

Sliced to keep coupled siblings together and reads deep (one agent per
slice, read/report-only → `audits/SPIKE-WORKING-<id>/`). LIVE excluded
entirely: `spike-self-actuation-grounding`, `spike-wf-strengthening`,
`spike-wf-class-scoping`, `visual/`.

- **S1 — 2026-04-24 strengthening cycle** (INDEX: TIER-1-LANDED;
  verify-in-canon): `bridge-lemma-nonlinear-strengthening-2026-04-24`,
  `fenchel-bregman-reframe-…-2026-04-24`,
  `identifiability-floor-instance-triage-2026-04-24`,
  `kl-to-state-distance-template-extraction-2026-04-24`,
  `neutral-drift-endogenous-coupling-strengthening-2026-04-24`,
  `rho-additive-variance-strengthening-2026-04-24`.
- **S2 — operator-family + pilot independent-verify** (confirmer ≠
  pilot): `spike-operator-sector-unification` (confirm/refute the pilot's
  `integrated-misfiled` against the named loci in
  `audits/SPIKE-WORKING-023198/`), `spike-update-operator-sector`
  (pilot-flagged `orphaned`-suspect).
- **S3 — composition / strategy / passivity**: `composition-gaps`,
  `composition-scaling-N`, `passivity-composition`,
  `strategy-dynamics-gaps`, `transient-dependency-amplification`,
  `pid-a2prime`.
- **S4 — adaptive / evidence / factorization (heavy)**:
  `active-inference-vs-aad`, `l1-evidence-axiom`,
  `jacobian-b1-strengthening`, `rho-factorization`,
  `stochastic-non-exit-strengthening-2026-05-16` (INDEX: LANDED state-3
  no-go — is the no-go canon per §5?).
- **S5 — small orphan-suspects + integration doc**:
  `alignment-impossibility`, `aporia-sub-agent-adversarial`,
  `fep-suboptimal-approximation`, `message-passing-credit-assignment`,
  `attention-governance`, `attention-causal-graphs`,
  `neurips-back-integration-2026-05-08`.
- **S6 — dir-spikes (lighter gold gate: read+recommend → Joseph batch) +
  liveness checks**: `class-coercion-wrapping/`,
  `spike-local-embedding-benchmark/`, `temporal-nesting-rg/`,
  `track-a-intent-dag/`, `track-b-nonlinear-sims/`; liveness-check
  `spike-language-as-causal-substrate/` and `spike-strategic-self-coupling`
  (if live → `live-or-open`, hands-off).

`spike-c2-star-to-integrate` already adjudicated (pilot → `live-or-open`).

## Coupled landing clusters (parent-owned; reconcile fan-out into these)

Cross-slice couplings surfaced by the sibling rule. The parent holds
these so independent slice-recommendations are **reconciled into one
landing**, never isolate-landed (three parallel half-segments of one
appendix is the `PROPOSALS.md:268` failure).

- **CL-1 — `#dissipativity-template` / SP-22 (γ)-hybrid bundle**
  (surfaced by S3, 2026-05-17). Members: `spike-passivity-composition`
  (heterogeneous-storage-function composition payoff + the
  `#dissipativity-template` appendix — Willems route), `spike-pid-a2prime`
  (the explicit $\alpha_{\text{PID}}$/B1 derivation, KYP route — same
  α/β-repartition territory), and the **S1-slice**
  `spike-bridge-lemma-nonlinear-strengthening-2026-04-24 §7.2` (targets
  the *same* appendix). SP-22's architectural gate was resolved
  2026-05-14, so this is straight authoring, not an architectural call —
  **one HEAVY landing, one integration-plan, one PRACTICA surface.**
  When S1/S4 report on `bridge-lemma`, fold into CL-1; do not isolate-land
  any member. (The §8 adversarial no-go from `spike-passivity-composition`
  is *already* canon at `result-contraction-template.md:148` — correctly;
  CL-1 is only the not-yet-landed heterogeneous-composition payoff.)

- **CL-2 — rho-decomposition / the §4.1 cardinal-violation cluster**
  (surfaced by S4, corroborated by S1, parent-verified first-hand
  2026-05-17). Members: `spike-rho-factorization` (the true no-go: (R-F)
  multiplicative ρ-factorization does **not** hold — additive-in-variance,
  not multiplicative-in-rate), `spike-rho-additive-variance-strengthening-2026-04-24`
  (**S1 slice** — the *completed strengthen-first successor*: the real
  derived (AV) theorem, only in the spike), and the segment
  `internal-external-decomposition` (was asserting the refuted split at
  `robust-qualitative`). The eventual replacement is a new
  `#rho-decomposition` appendix (absent today) + the no-go canonized +
  status up-tier of the corrected additive form + the §4.1-marked segment
  rewritten. **One HEAVY landing; carries a Joseph-reserved Instance-5
  decision → Joseph batch, not this cycle.** The mandatory honesty-mark
  (below) is *done now and is separate from* this landing.

### §4.1 honesty-mark — DONE & verified (2026-05-17)

The cardinal-sin case. `internal-external-decomposition` asserted the
refuted multiplicative ρ-split at `robust-qualitative` with **no
obstruction record in its entire git history** (pickaxe-confirmed).
Triply-converged (S4 primary-source+pickaxe / S1 corroboration / parent
first-hand read of segment + spike). Action taken, per audit-routing
§4.1/§4.2, *before* routing and separate from the heavy CL-2 landing:

- `01-aat-core/src/internal-external-decomposition.md`: `status:
  robust-qualitative → false`; prominent in-body `> [!warning]`
  known-broken banner (spike link + `TODO: FIXME` + CL-2/tracker
  pointer); content preserved-but-flagged (not blanket-deleted — §6
  precision; the corrected form is the reserved CL-2 landing, not written
  here).
- `01-aat-core/OUTLINE.md:357` (Appendix A row): description prefixed
  with the KNOWN-FALSE flag (the index was lying too).
- **Cascade closure verified empty**: zero segments list it in
  `depends:`; zero `#`-refs anywhere; only the OUTLINE row (now marked).
  No propagation. *(Verification-bug caught & corrected mid-pass: an
  earlier `grep -v` self-filter masked the OUTLINE row — re-checked
  clean. Recorded as a scar: filter your exclusions, then re-verify
  without them.)*
- Tooling: `lint-outline` clean (`status: false` is out-of-band by
  design, does not break the index); `lint-md` clean for the banner
  (3 residual emphasis-`_` issues are **pre-existing** in the refuted
  body — baseline-confirmed identical — deliberately not polished, the
  segment is queued for CL-2 replacement).
- First in-practice application of the audit-routing §4 transient no-go
  mark (no prior `status: false` precedent in the corpus). Worked
  cleanly; data point for the SOP.

## Joseph batch (reserved-decision items — assemble, do not auto-file)

Per `spike-routing.md` §6 (decision-type gate, ratified). Surface
together; each is a present-truth call Joseph reserved:

- **CL-2 Instance-5** — the rho-decomposition replacement landing
  (above); the §4.1 mark is done, the *replacement* is his.
- **identifiability-floor 4th-instance** (S1: `spike-identifiability-floor-instance-triage-2026-04-24`
  + `spike-neutral-drift §8/§10.1`) — a triage spike whose recommendation
  canon *partially inverted*: is `disc-identifiability-floor` Instance 4 a
  category error the triage caught, or is the triage the soften-shaped
  move? Present-truth call, laid side-by-side in SPIKE-WORKING-417303.
- **`spike-language-as-causal-substrate/` theoretical orphan** (S6) —
  Theorem-1 (discourse-act → Pearl L2, derivation-grade) lives only in
  the spike; landing is a reserved promotion call (new AAT appendix grade
  + Synthese cross-cite). Same family as the pilot's **C2★ gap**
  (`der-loop-interventional-access:76`) — show them together.
- **`spike-attention-governance` archived-vs-research-seed** (S5) — is
  finite-attention a missing postulate or an IB/temporal-nesting
  consequence? Truth-call, not a filing op.
- **`temporal-nesting-rg/` Moves B/C/D** (S6) — `integrated-misfiled` for
  its landed core, **but** hold the `git mv` for the Joseph batch: the
  B/C/D + temporal-nesting-Discussion decision he was owed
  (`class-coercion-wrapping/INTEGRATION-PLAN.md:221`, never adjudicated)
  rides with it; auto-filing silently drops it.

## Disposition ledger (running — the assembled safe subset)

Durable so the cycle survives interruption (if dropped here, future-me
executes the batch from this section). **No `git mv` until the durable
batch at the seam** (audit-routing §8: verification is pre-decisional;
MANIFEST + `git mv` + commit are the one durable batch, not piecemeal).

**VERIFIED — safe-mechanical `git mv` → `.integrated/` (durable batch):**

- `spike-operator-sector-unification` — pilot 023198 `integrated-misfiled`
  **independently confirmed by S2 (471639 ≠ pilot)**, every locus
  re-opened first-hand + git-provenance-proven never-filed. Completion (B).
  Cycle-close: also fix the INDEX:64 "predecessor" pointer (doubly wrong:
  path *and* referent — absorbed predecessor is the
  `spike-operator-family-unification/` dir, not this file).

**TRACTABLE landings — this cycle (parent authors, post-batch):**

- `spike-update-operator-sector` — `orphaned` (S2-confirmed pilot flag):
  real `(O-A2')` strengthening + a sharp confirmed no-go (§4.3
  unobservable-L1' Cramér-Rao rank-1 break), all spike-only,
  strengthen-first-checked as **not** `subsumed`. Landing: α-op/β-op
  sub-list refresh into `#deriv-sector-condition` (mirror the
  already-landed mismatch-layer recast) + cross-ref into
  `#disc-identifiability-floor` + optional `(O-A2')` hook into
  `#disc-credit-assignment-boundary`; no new appendix/cascade.
  *Parent-owned seam:* SP-22 already decided subsumption-not-new-peer
  (the spike's §8.1 new-appendix self-rec is superseded); the
  §266(iii)-vs-§8.2 placement is a whole-corpus call — parent decides at
  routing, not auto-exec. *Non-loss (integration-is-replacement):* the
  no-go's **operator-layer** manifestation must reach
  `#disc-identifiability-floor` as present-tense canon — covering it as
  "Instance 2 already" without the operator-layer line is the subtle
  replacement failure.

**`integrated-misfiled` (S3) — pending independent-verify before batch:**

- `spike-composition-gaps` (Gap 1 → `hyp-directed-separation-under-composition`;
  segment *sharper* than spike — excised Case-3 as category error;
  deferred residue tracked SP-17/SP-20; prov `d546cf4`).
- `spike-strategy-dynamics-gaps` (all four gaps landed; INDEX 2026-04-25
  "living artifacts" header wrong in the integrated direction; prov
  `9376b8f`).

**HEAVY → CL-1** (queue, not this cycle): `spike-passivity-composition`,
`spike-pid-a2prime` (+ S1 `bridge-lemma §7.2`) — see Coupled landing
clusters.

**`live-or-open` (no action):** `spike-transient-dependency-amplification`
(author self-blocked, INDEX correct), `spike-c2-star-to-integrate` (pilot,
cross-repo).

### S1 / S4 / S5 / S6 additions (detail in each SPIKE-WORKING-*/adjudication.md)

**`integrated-misfiled` — pending independent-verify, then durable batch:**

- S1: `spike-bridge-lemma-nonlinear-strengthening-2026-04-24` (§7.1 only —
  §7.2 is a CL-1 orphan strand), `spike-fenchel-bregman-reframe-…-2026-04-24`
  (both halves landed incl. the "Tier-3 reframe" INDEX:106 wrongly records
  unlanded).
- S4: `spike-stochastic-non-exit-strengthening-2026-05-16` (state-3 no-go
  *is* canon, textbook 5A — cascade-verified), `spike-active-inference-vs-aad`
  (G-BP2 landed, strengthened-past), `spike-l1-evidence-axiom`,
  `spike-jacobian-b1-strengthening` (both landed; INDEX understated).
- S5: `spike-fep-suboptimal-approximation`, `spike-message-passing-credit-assignment`
  (refuted core integrated-as-replacement, corrected result canon),
  `spike-attention-causal-graphs` (core via sibling commit `446c7a1`).
- S6: `class-coercion-wrapping/`, `track-b-nonlinear-sims/`,
  `track-a-intent-dag/` (mechanical, low-loss); `temporal-nesting-rg/`
  (**hold for Joseph batch** — see above).

**`orphaned` — HEAVY → CL-2 / Joseph batch:** `spike-rho-factorization`
(S4, the no-go), `spike-rho-additive-variance-strengthening-2026-04-24`
(S1, the (AV) successor). **`orphaned` — strengthen-first, HEAVY:**
`spike-alignment-impossibility` (S5 — bare GS no-go in canon but the §7
cardinal-utility/VCG strengthening is **nowhere**; must not be softened to
"done"). **`orphaned` — Joseph-reserved (triage-contradicted):**
`spike-identifiability-floor-instance-triage-2026-04-24`, `spike-neutral-drift…`
§8/§10.1 (S1).

**`live-or-open`:** `spike-kl-to-state-distance…-2026-04-24` (S1 — gate
landed, template correctly not, clients unmaterialized),
`spike-aporia-sub-agent-adversarial` (S5 — claims 2–3 open, SP-18),
`spike-strategic-self-coupling` (S6 — open direction),
`spike-local-embedding-benchmark/` (S6 — spec for an unbuilt tool;
partition hypothesis "sibling-repo" was wrong, it's ASF-internal),
`neurips-back-integration-2026-05-08` (S5 — a live back-integration
*plan*, the spike analog of `pending-findings-*`; stays; Phase B would
import in-review `~/src/neurips/` results — cross-repo-blocked per §3).
**Joseph-reserved:** `spike-language-as-causal-substrate/` theoretical
orphan, `spike-attention-governance` (S5/S6 — see Joseph batch).

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
  Checkpoint committed (`971d127`).
- **2026-05-17 (d)** — Joseph-directed SOP refinement: separate git
  *recency* (sweep-poisoned) from git *provenance* (valid, encouraged,
  non-destructive — pickaxe `-S`, `blame`, `log --follow`, dates in
  context; often the sharpest decisive-test instrument). Folded into
  `spike-routing.md` §7 + Refinement 2 **and** the shared core
  `audit-routing-instructions.md` §8 + its Refinement 2 (the shared
  core's first re-truthification from its second corpus — §7 meta-stance
  working as intended). Fan-out briefs to foreground git-provenance as a
  decisive-test tool (agents default to grep; pickaxe is sharper).
- **2026-05-17 (e)** — Six fan-out slices launched + all returned
  (SPIKE-WORKING-417303/S1, 471639/S2, 417739/S3, 111710/S4, 029307/S5,
  418736/S6). Dispositions in the ledger above; detail in each dir. The
  sibling-coupling refinement paid off twice cross-slice (CL-1 caught
  before three half-landings; CL-2 = the rho cluster split S1↔S4).
- **2026-05-17 (f)** — **§4.1 cardinal violation found and honesty-marked**
  (`internal-external-decomposition`; the rho no-go). Triply-converged,
  parent-verified first-hand, marked at both loci, cascade-verified empty,
  lint-clean, tooling-checked. See the §4.1 record above. The *replacement*
  is reserved (CL-2 / Joseph batch); the *mark* is done. This is the
  cardinal-sin case the cycle exists to catch — caught and discharged in
  the honest direction.

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
