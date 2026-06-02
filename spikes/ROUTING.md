# Spike-routing — live tracker (started 2026-05-17)

The in-flight rendezvous for the spike-backlog routing cycle. Governing
docs: [`../doc/sop/spikes.sop.md`](../doc/sop/spikes.sop.md) (spike delta) +
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
  (`spikes.sop.md` §4).
- **`.archived/`: yes, two-way honest split** — with the **bounded,
  non-retroactive guarantee** documented in `spikes/README.md` (do not
  re-audit `.integrated/`; the 2026-05-12 bulk-64 is not re-sorted).
- **Dir-spike gold gate: lighter** — agents read+recommend, Joseph
  adjudicates the dir-spikes in one batch (`spikes.sop.md` §6).

## Evidence hierarchy

In [`../doc/sop/spikes.sop.md`](../doc/sop/spikes.sop.md) §7. Decisive test:
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
  IN PROGRESS). `INDEX.md` and the `PROPOSED.md` family (`PROPOSED.md`
  index + `-ADVANCED` + `-MISC`) — durable, stay (not routed).
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

Adjudications write to `spikes/.routing-trail/SPIKE-WORKING-<six digits>/` — a new
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
> — already written about spikes); `doc/sop/spikes.sop.md` (the
> spike-specific delta — the five-state disposition, directory-label
> honesty, the live-work exclusion); and `spikes/ROUTING.md`
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
> and reasoning to `spikes/.routing-trail/SPIKE-WORKING-<your six digits>/`. The routing
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
slice, read/report-only → `spikes/.routing-trail/SPIKE-WORKING-<id>/`). LIVE excluded
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
  `spikes/.routing-trail/SPIKE-WORKING-023198/`), `spike-update-operator-sector`
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

Per `spikes.sop.md` §6 (decision-type gate, ratified). Surface
together; each is a present-truth call Joseph reserved. **This is the
working pointer; the durable queue home is the standing navigator —
do not treat this `msc/` file as the home (it is the dependency-inverted
failure Joseph caught 2026-05-18).**

- **The Instance-4 / Object-B / CL-2-heavy unification — ONE reserved
  decision. Durable home: [`PROPOSALS.md`](../PROPOSALS.md) §D.9
  "RESERVED DECISION (2026-05-18)"** (self-contained there; superseded
  the earlier stale "CL-2 Instance-5" + "identifiability-floor
  4th-instance / triage-contradiction" framings, which were resolved by
  `spikes/spike-identifiability-floor-instance4-resolution-2026-05-18.md`
  and the recheck). Gated on the running Object-B independent-verify.
- **Other Joseph-batch items (unchanged, own calls):**
  `spike-language-as-causal-substrate/` Theorem-1 + the C2★ gap;
  `spike-attention-governance` archived-vs-research-seed;
  `temporal-nesting-rg/` Moves B/C/D.
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

## Verify results (running — drives the durable `git mv` batch)

If dropped here, future-me executes the batch from this list (the
confirmed set → `git mv` to `spikes/.integrated/` + MANIFEST). One batch
after V1+V2+V3 all in (anti-fragmentation §8), not per-return.

- **V1 (SPIKE-VERIFY-624813) — DONE, both CONFIRMED, no refute:**
  `spike-bridge-lemma-nonlinear-strengthening-2026-04-24` (§7.1; §7.2
  independently re-confirmed absent → stays CL-1, do not merge),
  `spike-fenchel-bregman-reframe-additive-coordinate-forcing-2026-04-24`
  (both halves; the §7.1 meta-reframe landed verbatim incl. the
  axiom-independence guard). Cycle-close: `INDEX:106` records landed
  canon as an unlanded "Tier-3 proposal" — dangerous-direction error,
  reconcile (not a `git mv` blocker).
- **V2 (SPIKE-VERIFY-504612) — DONE, 6/6 CONFIRMED, no refute:**
  `spike-composition-gaps` (Gap 1 sharper — Case-3 excised; residue
  SP-17/SP-20), `spike-strategy-dynamics-gaps` (4 segments substantive),
  `spike-stochastic-non-exit-strengthening-2026-05-16` (no-go is its own
  `exact` appendix; **cascade closure verified first-hand** at
  `result-sector-persistence-template.md:90`), `spike-active-inference-vs-aad`,
  `spike-l1-evidence-axiom` (dual-obstruction → Instance 2, not new),
  `spike-jacobian-b1-strengthening`. Corroboration for the Joseph batch:
  `disc-identifiability-floor` has **exactly 4** instances first-hand →
  the rho no-go is genuinely Instance **5** (CL-2 framing confirmed). 4/6
  landed *stronger* than the spike, honestly labeled.
- **V3 (SPIKE-VERIFY-738041) — DONE, 6/6 CONFIRMED, no refute:**
  `spike-fep-suboptimal-approximation`, `spike-message-passing-credit-assignment`
  (both halves: corrected result canon; refuted mean-field-VMP core
  excluded-not-ghosted, grep-confirmed across all `src/`),
  `spike-attention-causal-graphs` (core canon) **+ 2 batching caveats**:
  (i) `attention-causal-graphs` `git mv` is **coupled** to the
  Joseph-reserved `attention-governance` (same `446c7a1` cluster) — do
  not fire alone; (ii) `class-coercion-wrapping/`, `track-a-intent-dag/`,
  `track-b-nonlinear-sims/` are **directory spikes** → §6 lighter
  gold-gate = Joseph dir-batch, not parent auto-file (recommendation:
  `integrated-misfiled`, content verified, no reserved theory decision —
  a clean/fast Joseph yes expected, but his per the gate he set).
- Pre-gated (skip verify): `spike-operator-sector-unification` (S2 was
  the independent confirm of pilot 023198).

### Final verified partition → what executes this cycle

**Parent auto-`git mv` → `spikes/.integrated/` (10 file-spikes, fully in
canon, no orphan strand, no reserved coupling):**
`operator-sector-unification`, `fenchel-bregman-reframe-…-2026-04-24`,
`composition-gaps`, `strategy-dynamics-gaps`,
`stochastic-non-exit-strengthening-2026-05-16`, `active-inference-vs-aad`,
`l1-evidence-axiom`, `jacobian-b1-strengthening`,
`fep-suboptimal-approximation`, `message-passing-credit-assignment`.

**Held (verified integrated, but NOT parent-auto-moved — reason):**
- `bridge-lemma-…-2026-04-24` → its file carries the §7.2 CL-1 orphan
  strand; moving it would make `.integrated/` lie. Stays until CL-1 lands.
- `attention-causal-graphs` → `git mv`-coupled to Joseph-reserved
  `attention-governance` (V3 caveat i). Joseph batch.
- `class-coercion-wrapping/`, `track-a-intent-dag/`,
  `track-b-nonlinear-sims/` → §6 dir-spike Joseph batch (V3 caveat ii).

**INDEX reconciliation — DEFERRED to cycle-close (independence
constraint).** `spikes/INDEX.md` is dirty with the active authors'
uncommitted edits; editing it now co-mingles (file-level `git add`).
Record of rows to fix when independent: `:64` operator-sector
"predecessor" pointer doubly-wrong (path + referent — absorbed
predecessor is the `spike-operator-family-unification/` dir);
`:106` fenchel-bregman meta-reframe recorded as unlanded "Tier-3
proposal" — **dangerous-direction** (landed canon shown as open);
2026-04-25 "living artifacts" header wrong (strategy-dynamics landed);
`l1`/`jacobian` understated; `fep` `:58` stale "OPEN" (causal-IB
settled); plus the 10 moved spikes' rows → `.integrated/`.

## Log

- **2026-05-17 (a)** — Cycle set up. Governing docs authored
  (`doc/sop/spikes.sop.md` — thin companion deferring into the shared
  audit-routing core; `spikes/README.md` + `spikes/.archived/README.md` —
  directory-label honesty + bounded non-retroactive guarantee). Partition
  hypotheses seeded from INDEX cycle headers (to verify, not assume).
  Two-shot diagnostic pilot launched on `spike-c2-star-to-integrate` +
  `spike-operator-sector-unification`. Flagged for Joseph: recommended
  reciprocal head-note in `audit-routing-instructions.md` (authoritative
  SOP — §7, not rescoped unilaterally); `SPIKE-WORKING-*` prefix coinage.
- **2026-05-17 (b)** — Pilot 023198 returned.
  Adjudication: `spikes/.routing-trail/SPIKE-WORKING-023198/adjudication.md` (all
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
  - Frame defects folded into `doc/sop/spikes.sop.md` (Refinement 1,
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
  (decision-type, not file/dir). `spikes.sop.md` §6 now settled.
  Checkpoint committed (`971d127`).
- **2026-05-17 (d)** — Joseph-directed SOP refinement: separate git
  *recency* (sweep-poisoned) from git *provenance* (valid, encouraged,
  non-destructive — pickaxe `-S`, `blame`, `log --follow`, dates in
  context; often the sharpest decisive-test instrument). Folded into
  `spikes.sop.md` §7 + Refinement 2 **and** the shared core
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
- **2026-05-17 (g)** — Joseph: "Proceed; batch waits for you." Independent-
  verify pass launched (3 agents, `SPIKE-VERIFY-<id>/` — new prefix class
  alongside SPIKE-WORKING / ADJUDICATION-WORKING / AUDIT-WORKING; six-digit
  ID is identity, prefix is class, never blanket-rewrite). Confirmer ≠
  adjudicator by construction (fresh instances). Slices: V1 ⊃ S1 (417303);
  V2 ⊃ S3+S4 (417739, 111710); V3 ⊃ S5+S6-misfiled (029307, 418736).
  `operator-sector-unification` skips verify — S2 *was* the independent
  confirm of pilot 023198, already gated. `temporal-nesting-rg/` excluded
  (held for Joseph batch). On return: one durable batch — `git mv` verified
  set + single MANIFEST pass + the tractable `update-operator-sector`
  landing + INDEX reconciliation (anti-fragmentation §8: not
  per-verifier-return). Joseph-reserved batch untouched.
- **2026-05-17 (h)** — Verify pass complete (V1 2/2, V2 6/6, V3 6/6;
  14/14 confirmed + S2-pregated; **zero refutes**). Durable batch
  executed: 10 verified file-spikes `git mv` → `spikes/.integrated/` +
  `MANIFEST-2026-05-17.md`. **Provenance:** the 10 renames were swept
  into the concurrent pipeline commit **`0834649`** (co-mingle
  Joseph-pre-authorized; 100%-similarity, reversibility intact, nothing
  lost; history deliberately *not* rewritten — see MANIFEST provenance
  note). MANIFEST + this tracker are the durable spike-routing record;
  `0834649` is only where the rename bytes landed. Clean artifacts
  (MANIFEST, tracker, 3 `SPIKE-VERIFY-*`) committed separately. **Held
  (not moved):** `bridge-lemma` (§7.2→CL-1), `attention-causal-graphs`
  (Joseph-coupled), 3 dir-spikes (§6 Joseph dir-batch). INDEX
  reconciliation deferred (independence; rows recorded above).
  Remaining this cycle: the tractable `update-operator-sector` landing
  (next, careful — no-go-bearing, parent-owned §266(iii)/§8.2 placement).
- **2026-05-17 (i)** — Joseph: regression check is **central**, applies to
  already-integrated too. SOPs updated: `spikes.sop.md` §2a (regression
  axis, co-equal with math-stranded; new `correctly-superseded` state;
  every disposition runs it) + Refinement 5; `audit-routing-instructions.md`
  §8 + Refinement 3 (Joseph-directed mirror). Worked first application:
  **`spike-update-operator-sector` regression-checked CLEAR** — pickaxe:
  `(O-A2')`/`α_op`/`O-DA.1` never in `src/`; CHANGELOG:73 (2026-05-14
  SP-22 decoupling) names `PID/update-operator α-list` in the "(γ)-hybrid
  … straight authoring, no longer gated" set = deferred, **not**
  flawed-and-corrected; no audit flag. Genuine orphan, cleared to land.
  Regression-recheck of the **10 already-integrated** launched
  (`SPIKE-REGRESSION-<id>/`, read-only forensics; new prefix class). **Not
  yet regression-cleared (gate before landing):** CL-1, CL-2 (special
  care — `spike-rho-factorization:45` notes the multiplicative ρ-split was
  *"a useful simplification"*; must confirm the additive form wasn't
  deliberately simplified *away* — exactly the trap), `alignment-impossibility §7`,
  `language-as-causal-substrate` (Joseph batch). **CHANGELOG:79
  obligation (in-cycle):** 7 segments still point readers into the 10
  newly-archived paths (`deriv-strategy-cost-regret-bound`,
  `deriv-sector-condition`, `deriv-stochastic-non-exit`,
  `deriv-variational-sector-condition`, `der-interaction-channel-classification`,
  `deriv-fisher-whitened-update-rule`, `result-contraction-template`) —
  reduce-not-repoint to the CHANGELOG cycle entry; none overlap active
  authors' files.
- **2026-05-18 (j)** — Independent ρ-structure recheck returned
  (`spikes/spike-rho-structure-recheck-2026-05-18.md`; commissioned by
  Joseph under §0 "truth is the arbiter"). Verdict: **§4.1 mark
  vindicated on truth and *strengthened*** — the no-go is a one-line
  constitutive category error (δ≡o−ô ⟹ ρ_external type-incorrect),
  strictly stronger than the prior three-case survey; parent
  independently re-verified the one-liner. **Not a regression** (it
  removed the only multiplicative assertion; rest of canon never
  committed the error). **Caught a second proxy-trust in the parent's
  CL-2 recommendation:** the (AV) (S1)–(S4) "exact theorem" is vacuous
  (cross-term defined to balance — the §0 failure one level up). CL-2
  re-scoped: **(a) light exact core** — the two-term identity already
  forced by canon (`#result-mismatch-decomposition` GA-1 + Prop A.1S
  Itô generator) + the one-line no-go; gated only by an independent-verify
  of the canon-forcing, then a light landing; **(b) heavy Joseph-reserved
  refinement** — the conditional 𝓜/π/cross split (Regime-C confound),
  **provably the same object as the identifiability-floor 4th-instance
  question** (independent re-derivation converges with the triage spike's
  prior unproven robust-qualitative claim). Second navigator §4.1-shaped
  lie corrected at four loci (INDEX:102, TODO:147, TODO:438,
  PROPOSALS:258 — "(AV) exact theorem" → present truth at honest tier).
  Identifiability-floor spike now scoped *as* the unified
  conditional-refinement/Regime-C/4th-instance question (the sequencing
  question resolved: the rho spike did reshape it). **Gated, Joseph's:**
  the independent-verify of the GA-1/Itô canon-forcing (then the light
  core lands); the unified identifiability-floor/conditional spike launch.
- **2026-05-18 (k)** — Independent-verify gate (`SPIKE-VERIFY-087154`,
  confirmer ≠ recheck spike) **CONFIRMED** the two-term identity is
  canon-forced (`#result-mismatch-decomposition` GA-1 + Prop A.1S Itô
  step; exclusion-pickaxe empty across both `src/` trees) **and caught
  two pedigree over-claims in the recheck spike** (ν rate-lift not a
  pre-existing `#hyp-mismatch-dynamics` identity; general-Σ exceeds Prop
  A.1S constant-isotropic). Joseph's conditional greenlight active (no
  objection to the load-bearing result). **CL-2 light exact core LANDED:**
  `#internal-external-decomposition` rewritten *true* (integration-is-
  replacement) on the additive two-term GA-1 decomposition + the
  constitutive no-go; honest tiers per the gate (`status: conditional`;
  ν rate-lift tagged a stated convention; general-Σ an elementary
  extension; no-go exact-by-constitution); finer 𝓜/π/cross split **not
  asserted** (reserved). Lint-clean; OUTLINE row de-flagged; CHANGELOG
  2026-05-18 written; second navigator §4.1-lie corrected (INDEX:102,
  TODO:147/438, PROPOSALS §D.9); `NOTATION.md` given a standing
  drift-caveat + self-description de-escalated; TODO item queued to
  auto-derive NOTATION from segments (the structural §0 fix). Two spikes
  in flight: `a096cedcba5be75b3` (unified identifiability-floor /
  CL-2-conditional-refinement). **Remaining:** that spike's verdict →
  the heavy reserved refinement; otherwise the cycle's mine-to-do
  non-reserved work is complete.
- **2026-05-18 (l)** — Unified identifiability-floor spike returned
  (`spikes/spike-identifiability-floor-instance4-resolution-2026-05-18.md`).
  Verdict: canon's "Instance 4" conflated **Object A** (universal-C /
  non-(PI) — a category error, *not* a floor; the triage spike was right)
  and **Object B** (architecturally-distinct/behaviorally-identical — a
  *genuine* floor, = the rho Regime-C confound / CL-2's reserved
  refinement; one decision). Object-A half **verified first-hand from
  canon's own self-contradiction** (`#deriv-observation-ambiguity-bias-bound:127`
  already states "not a new floor instance"; Instance 4's single-escape
  fails the segment's own ≥2 test; Sylvester Discussion taxonomizes 3,
  Findings says 4) → **§4.1 honesty-mark applied** to
  `disc-identifiability-floor` Instance 4 (KNOWN-DEFECTIVE, localized,
  lint-clean; positive relabel/install reserved, not done). Object-B
  substantive math (Kalman-Ho no-go; Instance-2-mechanism reduction;
  CL-2 §7 projection) → **independent-verify gate launched**
  (`a9441d4be02a5fb0c`, confirmer ≠ spike) — legitimate per §0c (it
  feeds a Joseph-reserved canon landing, not closure-comfort).
- **2026-05-18 (m)** — Joseph: §0c counterweight folded
  (`spikes.sop.md` §0c + Refinement 8; audit-routing Refinement 5).
  **Duty-state per §0c: the cycle's mine-to-do, non-reserved work is
  discharged.** Everything is honestly tiered (`#internal-external-decomposition`
  `conditional` + open Working Notes; `disc-identifiability-floor`
  Instance 4 KNOWN-DEFECTIVE + what's-open flagged); open/reserved items
  are in the standing queue; the running Object-B gate + the
  Joseph-reserved disposition (relabel Instance 4 / install Object B /
  CL-2 heavy refinement / the unified neutral-drift+Instance-4 decision)
  carry the remainder. **Not escalating further.**
- **2026-05-18 (n)** — Joseph asked "where is #2 queued exactly?" and the
  honest answer was: **it wasn't cleanly queued — my "honestly queued"
  was an overclaim.** It lived in this `msc/` working file (the
  dependency-inverted failure) with stale/scattered fragments in
  PROPOSALS/TODO and nothing in PRACTICA. §2-bis navigator-reconciliation
  failure on my own claim; caught by his question, not by me. **Fixed
  (the §0c "release-to-the-standing-cycle" leg made actually true, not
  asserted):** single self-contained durable home created at
  `PROPOSALS.md` §D.9 "RESERVED DECISION (2026-05-18)"; TODO 143/144
  de-staled (resolved-by-spike) + 147 repointed; this section inverted to
  point *out* to the durable home; PRACTICA cycle-priority item 7 added
  (top-navigator discoverability). Object-B verify
  (`SPIKE-VERIFY-471802`) returned in parallel: **no refutation; math
  gate CLEARED** with named repairs (overclaimed ‖δ‖-moment clause;
  Lyapunov sign slip; tier-honesty pass) — true tier
  exact-in-LG-sub-scope/robust-qualitative-general; folded into the
  durable home. The reserved decision is now genuinely queued, current,
  and discoverable from the top navigator. Per §0c: discharged; not
  escalating.

- **2026-05-18 (o)** — Relocation + process-fix (Joseph-directed).
  `msc/` is delete-at-any-time scratch; `audits/` is the audit corpus,
  not the spike corpus — both were misplacements. Fixed: this tracker
  `msc/spike-routing-2026-05-17.md` → **`spikes/ROUTING.md`** (de-dated:
  the routing *process* is ongoing); 13 trail dirs `audits/SPIKE-*` →
  **`spikes/.routing-trail/`** (frozen, `README.md` rosetta, not
  back-edited); the moves committed `90c1230` (R100). Every live pointer
  re-homed via the Edit tool and **verified zero-stranded repo-wide**
  (`sed -i`/`perl -pi` silently no-op on the repo here — Bash-editor
  gotcha, scarred in SOP Refinement 9; only Edit/Write/`git mv`
  persist). Process made explicit: `doc/sop/spikes.sop.md` §5a (Directory
  layout) + Refinement 9. `spikes/README.md` updated.

- **2026-05-19 (p)** — Integration-cycle archive reconciliation (the "INDEX WASN'T UPDATED" follow-through). Context, not routing-cycle work: the 2026-05-18→19 integration cycles (F-ADJ-1 two-operator split; accumulation-type confound; continuity-persistence; Φ(fight)) landed through their *own* commits (`da3c6b4` F-ADJ-1; `23ae523` F-1 truthful history layer; `d098997` fight C1 off-spine; `aabcf8e`/`639e7e2`/`5158ed5` the accumulation-typing frame), each with its own independent gate (`adjudicate-disc-m-preservation-operator` verdict (ii)-with-(iii); `verify-cycle-coherence` §0 verdict (b); the RESULT.md embedded review, Fixes 1+2 applied; fight `99-verdict` author-gated, Joseph elected the axis) — CHANGELOG 2026-05-18/19 carries the narratives. Joseph then `git mv`'d the 22 spent trail/decision/verifier artifacts to `.integrated/` in `9a3db8e` **without a manifest or an INDEX update**, flagging the gap in the commit title. Discharged this pass: (1) first-hand decisive-test verification of the five landed segments (`der-turnover-information-recursion` `exact`-given-argued-commitment, `der-identity-continuity-threshold` `conditional`-with-exact-core, `disc-m-preservation` omission-fixed/replaced-forward, `der-resource-bounded-destabilization` + `form-resource-budget` off-spine `conditional`) + the §2a regression axis via the exclusion-pickaxe logic (the refuted §5 subsumption + the wrong additive inequality are absent from canon; replacement was *forward*, not a regression-restoration); (2) **`.integrated/MANIFEST-2026-05-19.md`** authored (the durable per-cycle move record `9a3db8e` lacked; distinct provenance from the 2026-05-17 spike-routing batch, honestly stated); (3) **INDEX fully reconciled** — the two 2026-05-19 rows (continuity `integration pending` → RESOLVED+LANDED as the F-ADJ-1 split, with the withdrawn §5 "Lindley-is-the-linearization" subsumption and the halted single-`der`-replacing-`disc-m-preservation` plan moved out of the navigator into the history layer; fight Location → `.integrated/`) **and** the standing §4 backlog (the integrated-10 → `.integrated/` + status to the already-verified MANIFEST-2026-05-17 truth, *reconcile-not-re-verify* per §0c / the bounded non-retroactive guarantee; the dangerous-direction fenchel-bregman "Tier-3 proposal" and operator-sector "DO NOT elevate" rows corrected to landed-canon; the rho/identifiability cluster + neutral-drift §8/§10.1 + instance-4-triage repointed at the Joseph-reserved durable home `PROPOSALS.md` §D.9, *not* re-decided; 2026-04-25 cluster intro de-staled; bridge-lemma marked HELD-not-archived for the §7.2 CL-1 strand); the interim honesty banner **retired** and replaced with a present-truth note (ROUTING.md remains authoritative for live routing-*process* state + the reserved/queued items only). The ROUTING ledger's "fix the operator-sector 'predecessor' pointer doubly-wrong" item is discharged via the **line-154 row rewrite** (the actual stale locus — wrong path + a superseded "DO NOT elevate" verdict); the 2026-05-14-section predecessor pointer was already correct post-2026-05-17-move and was deliberately left untouched (not "fixing" what is right is the symmetric discipline). INDEX lint: pre-existing archival debt 51 (HEAD) → 47 (none added; 4 incidentally cleared by the rewrites); the residue is a tracked seam, flagged in the banner, not conflated. ROUTING.md itself carries pervasive pre-existing hard-wrap debt (~245 issues HEAD); this entry is written one-logical-line per the unconditional file-math/wrap rule despite the surrounding wrapped style — the local visual inconsistency is a symptom of that pre-existing seam, not license to extend it. Reversible (`9a3db8e` is pure `git mv`; all reconciliation is Edit-tool, re-read-verified). Next-actions item 4 → **DONE**.

- **2026-05-19 (q)** — Practica `01-theory`-dive remainder routed (Joseph relayed it; the audit-routing core applied to a relayed finding-set — §0: a relay is a proxy, verified first-hand at HEAD `0c94216`, not at the remainder's `9a3db8e`). Dispositions: **A4** (INDEX continuity-persistence "integration pending") was already discharged by `0c94216` (the remainder predates it). **A2/A3/A5** were genuine tractable canon-coherence defects, fixed in-cycle (triage-is-the-answer): A2 — the live contradiction at `der-tempo-composition:98` ("Open: does $\varepsilon^\ast$ scale with $N$?") vs `form-composition-closure:177` ("no exponential regime") replaced with the resolved pointer (integration-is-replacement, the question dissolved as an accumulation-type confound); A3 — `der-team-persistence` Working-Notes continuity breadcrumb (added 2026-05-18 *by the practica dive*, cited by 01-theory §12) repointed from "still discussion-grade — the spike target" to the landed `#der-turnover-information-recursion`/`#der-identity-continuity-threshold`, and its stale "`#disc-m-preservation` carries $\mathbb E[\Delta\epsilon]\le\mathbb E[\Delta I]$ discussion-grade" claim corrected (that inequality was deleted-and-replaced-forward); A5 — the CHANGELOG 2026-05-19 "What is NOT done — gated on Joseph" subsection (its three still-gated items — `#result-sector-persistence-template` restatement, `#form-composition-closure` re-typing, the D3 register question — had **all landed**: `aabcf8e`, `:289`/`:293`, `639e7e2`) replaced with a present-truth dated Update retaining the *why* (commit-when-asked gate, uncommitted-at-writing) as recorded history; the §63 "Seam flagged for the verifying agent" marked DISCHARGED; the §45 heading de-staled. Lint: segments "All clean"; CHANGELOG zero-net-debt (78=78, pre-existing hard-wrap seam). **B7 is resolved-not-open** — D3 was answered and landed (`639e7e2`, `#disc-stability-certificate:84`, explicitly "(the D3 register answer)": accumulation-typing is the Interior facet's temporal dual, *no* fifth meta-segment); the practica reader saw it open only via the stale CHANGELOG (now fixed by A5). Not a reserved decision; no Joseph call owed. **A1 adjudicated** (the practica-flagged math-lives-in-segments judgment): *not* the clean orphan the relay implied — the (S3b) $\tau$-abstraction / SCC-condensation / TC-defect / exactness-iff result **is** in a segment body at `conditional` grade with integration-is-replacement history-note and the spike cited as transient trail (`form-composition-closure:180`/`:293`; the $\varepsilon^\ast(N)$ no-go at `:289`), adequate per math-lives-in-segments for a resolved-conditional result whose derivation-trail is the spike. The spike's **own §10 explicitly reserves the fuller landing to Joseph** ("do NOT edit here — landing pass is separate, with Joseph"; the row re-type "must be decided with Joseph"); per `doc/sop/spikes.sop.md` §6 (decision-type gate) → Joseph-reserved, *partially-landed*, named remainder (the explicit (S3a) closed form $\varepsilon_\Sigma^{\ast2}=\lvert E\rvert\overline{\mathrm{Var}}\,\mathrm{Var}[r]$; the sharp §9 no-go = no exact single-DAG ⇒ L1′-mixture object, mixture-support $\le\lvert S\rvert$ is what grows; the `#def-strategy-dag` $\tau$-abstraction/SCC-construction home per spike §188; the Q3 "strategy-topology heterogeneity cannot alone cause Brooks's-Law collapse" corollary). Not auto-landed (the spike forbids it); `spike-strategy-dag-composition.md` stays in `spikes/`. **C10** verified first-hand §0c-discharged (`der-turnover-information-recursion:129` Working Note carries the honest "is R1/R2 genuinely new $\mathcal A_D$ or the bridge-lemma resolvent — test-not-assert, demotable" flag pointing at `RECONCILIATION.md` §4). **D-[U]** (the one [U] practica flagged worth closing — the original-sin cross-volume guardrail) closed **clean**: `der-identity-continuity-threshold` is faithful to INTEGRATION constraint 4 — §124 draws the 𝒜_refl-identity vs 𝒜_D-predictive-$I_k$ distinction sharply (two state variables, two targets, neither superseding), §114/§116 carry $S_{\text{id}}$ as a normalization tier-matched to the static floor ("not the object", explicit guard against flat-"exact"), depends are forward/lateral (no backward III→IV edge; `der-turnover` carries no 04-eli depends — Fix 1 holds), §133 ghost-discipline-clean, `status: conditional`-with-exact-core, open edges honestly carried. **B6** (P2 compensation-channel-uniqueness landed *folded* into `der-identity-continuity-threshold` Discussion vs 99-verdict §6's standalone-segment recommendation) is a genuine Joseph-reserved accept-fold-or-extract call — surfaced, not acted. **C8/C9/C11** are genuine frontier (legitimately undone), confirmed honestly carried in the segments' Working Notes / Epistemic Status — acknowledged, no "fix". A1 + B6 added to Next-actions below.

- **2026-05-19 (r)** — Joseph elected both reserved residue calls *now* (not deferred): **(7a) the A1 landing pass** and **(7b) extract B6 standalone** — both LANDED this turn. **A1:** the `spike-strategy-dag-composition` math landed into existing segments per the spike's own §189 guidance (conservative, prior-art-integration-correct — *not* a new appendix): `#def-strategy-dag` Discussion §"Composing heterogeneous strategy DAGs" (the $\tau$-abstraction typing with Rubenstein/Beckers–Halpern/BEH adopted-with-citation and the BEH-⇒-bound-not-term-for-term honesty; the exactness-iff condition; the SCC-condensation no-go $\sum\mathrm{TC}(C)\le\lvert S\rvert\log 2$ $N$-free; the Brooks's-Law-floor corollary) + Q1/Q2 in its Working Notes; `#result-unity-closure-mapping` Two-axis structure + Epistemic Status (the (S3a) $\varepsilon_\Sigma^{\ast2}=\lvert E\rvert\overline{\mathrm{Var}}\,\mathrm{Var}[r]$ fixed-topology instance, the explicit "natural addition not a new segment"); `#form-composition-closure:180/:293` reasoning-trail repointed spike→segment-homes; `der-tempo-composition:98` breadcrumb reduced to canonical+CHANGELOG. Honest tier `conditional` (Q1 constant-tightness named open, §0c-complete). `spike-strategy-dag-composition.md` `git mv`→`.integrated/` (decisive test §2-bis: math in canon first-hand; the only remaining `src/` mention is the non-needed `form-composition-closure:293` `.integrated/` trail breadcrumb naming the segments as the derivation home); MANIFEST-2026-05-19 updated (moved from "NOT moved" to the archived table). `spike-composition-scaling-N.md` stays in `spikes/` (separate practica disposition) with its INDEX:213 row reconciled "open question RESOLVED". **B6:** `#der-compensation-channel-uniqueness` created (`04-eli-core/` §04.1, new, `der-`, `conditional`) carrying continuity-`02` Proposition 1 + its DPI derivation + the (FW)-failure exactly-two-channels scoping (exact under (FW), the scoping exact, the slow-weight channel robust-qualitative → `#hyp-substrate-transfer-asymmetry`); `#der-identity-continuity-threshold` Discussion reduced to a pointer per integration-is-replacement (uniqueness derivation no longer duplicated; threshold-specific consequence kept); OUTLINE row added; `bin/lint-md` All clean, `bin/align-slug` no-op, `bin/lint-outline` no new missing-dep/orphan. CHANGELOG 2026-05-19 entry written covering both. Items 7a/7b → DONE; the practica-`01-theory`-dive remainder is now **fully discharged** (every item routed: fixed / already-done / resolved-not-open / audited-clean / honest-frontier / landed).

- **2026-05-19 (s)** — `spikes/PROPOSED.md` reconciled + made a standing navigator target (Joseph: "be sure, and add a constant update to it in your SOPs"). Joseph's "are we still tracking a suggested-spikes / proposed?" surfaced that PROPOSED.md had silently drifted — last content-curated 2026-04-25, four entries (Causal-IB LMI, message-passing, FEP-as-suboptimal, Landauer/thermodynamic) still listed as open "needs-repair" candidates when their repairs had landed in canon (`#deriv-causal-ib-lmi`, `#disc-credit-assignment-boundary`, `#disc-ciy-unified-objective`, `#deriv-persistence-cost`). Root cause: §2-bis(3)'s navigator set named `TODO`/`PROPOSALS`/`PRACTICA` but not the spike-corpus navigators, so the reconciliation obligation never attached to `PROPOSED.md` (or, formally, `INDEX.md`). **Discharged + systematized:** all 10 entries dispositioned to present truth first-hand (landed #1/#5/#6/#8 → canon homes; split #2/#4; open #3/#7/#9/#10) with a reconciliation header; a Phase 3 of 4 scan-surfaced uncatalogued candidates added (#11 substrate-transfer-asymmetry origin spike — strongest, ELI-core; #12 effects-spiral eigenvalue derivation; #13 modularity→strategic-asymmetry game theory; #14 AAT↔replicator) via a backgrounded corpus-scan agent (read/report-only; its one borderline find deliberately *not* double-listed — already homed PRACTICA item 3 / TODO:110). **Resolution shipped (Joseph's 3-perspective proposal, taken with refinements):** the interim single-file fix was elevated to a restructure — `git mv PROPOSED.md → PROPOSED-ADVANCED.md` (moonshot detail home; the down-reconciliation dispositions + Phase 3 preserved); new `PROPOSED.md` = the unified **index** (priority-tiered tables — Tier 1 near-term / Tier 2 exploratory / Tier 3 segment-audit-judgments / Reserved-cross-ref / Tier 4 landed-historical / Misc; columns added/name/source/description/status/updated/details); new thin `PROPOSED-MISC.md` (residual; allowed-empty; holds the dogfood entries — the reciprocal-link enforcement-grep to build + the WN-sweep). Three disciplines stated in `doc/sop/spikes.sop.md` §2-bis(3) (completeness — every effort indexed, owned-elsewhere cross-ref'd not duplicated; reciprocal links — WN↔index; bidirectional — down/up, landed-kept-not-retired) + Refinement 10 (scarred with the shipped resolution). Reciprocal back-links added to the known WN strengthenings (Q1/Q2 `#def-strategy-dag`, C10 `#der-turnover-information-recursion`; the latter's stale `RECONCILIATION.md` path also fixed to `.integrated/`). All repo pointers reconciled: `doc/readme/src/_navigation.md` (+ README rebuild), `spikes/README.md`, `CLAUDE.md` File-Organization, this tracker. Remaining staged + indexed (dogfooded as MISC, not lost): the full Working-Note strengthening sweep (task 19) and the `bin/` reciprocal-link check. Lint zero-net-debt.

- **2026-05-19→20 (t)** — Late-session arc + deeper-truth turn, recorded here because ROUTING-up-through-(s) ends at the PROPOSED restructure as if the session stopped there; the most important corrections came after. Brief arc: full Working-Notes sweep landed (5 Tier-3 rows + reciprocal back-links + 1 link-only fix on `der-adversarial-destabilization`; `36ce9d9`); a §4.1 stale-direction correction in `der-interaction-channel-classification:174` the sweep surfaced (`9684ca2`); a canon↔Working-Notes boundary sharpening that **Joseph then rejected at root** — *there is no "need vs mention" distinction*; any canon→spike reference is by definition an integration failure (the content matters and must be canon as an appendix/discussion, or it is vanity and is deleted), and the over-enumeration of "canon proper = Formal Expression / Epistemic Status / Discussion / Findings / frontmatter / OUTLINE" was also called out (which fields are canon is `FORMAT.md`'s + build-pipeline's authority, not this doc's); plus the binding-completeness framing of PROPOSED was deflated (PROPOSED is the optional low-friction repository — freshness + mutual-link bind, *not* completeness; `cf13cb9` → `c8e7fe6` → `263b24c` carries the over-correction-then-deflation trail). A false "lint zero-net-debt" claim in `09b24c8`'s commit message was named cleanly in `263b24c` rather than papered over: **lint must *gate* the commit, not run beside it** — the corrected process for future sessions. **Joseph then surfaced the deeper truth:** the 2026-05-12 bulk-64 move into `.integrated/` was done without per-spike content verification, and the README's `> [!important]` bounded-guarantee callout + `doc/sop/spikes.sop.md` §5 mirror — both attributed to "Joseph 2026-05-17" — encode a predecessor's documented abdication of the role's core duty (Joseph says he was not informed that 64 went unchecked). This role exists *specifically* to thoroughly check → integrate → route, not bulk-move; and this session's agent had inherited and *reinforced* the `need vs mention` rationalization from the same SOP set before Joseph caught it. A first-hand corpus scan (verified, section-aware, tokenized) found **~44 canon-resident process-artifact references across ~25 segments** — Formal Expression Source columns (14), Discussion (11), Epistemic Status (12), `## Findings` (4, external-facing), Current Instances (2), Methodology (1) — including 2 from this very arc's F-ADJ-1 landings (`disc-stability-certificate:84`, `result-sector-persistence-template:110`) citing `spikes/adjudicate-disc-m-preservation-operator.md` in canon Discussion. The sim/empirical class was then surfaced as the *same* failure with a wider gap: `02-tst-core/simulations/` (11 `.py` parked in the component tree 2026-03-20, never under the discipline) + ~10 canon segments depending on `track-b-nonlinear-sims/` / `sim-three-way-tradeoff.py` / the `empirical-discontinuity/` toolkit by local path, including `result-`tier and the `obs-section-i-validation-simulations` segment whose body literally is *"All code is in `../../spikes/track-b-nonlinear-sims/`."* The CLAUDE.md audit found the institutionalized canon→artifact sanction at `:236` (*"`ref/Novelty_defense_and_integration.md` — prior-art search source for 15+ segment-level Findings"*), **internally contradicting CLAUDE.md:165** which already states the correct discipline. The structural meta-risk was named (CLAUDE.md as the maximal-blast-radius / minimal-human-oversight surface — a predecessor's exception there silently overrides correct principles stated elsewhere and self-amplifies; the fix cannot rest on agent virtue). The Relata-side analysis (separate session, `~/src/relata`) confirmed the deepest cause: ASF has no formal citation/bibliography infrastructure yet (0 `\cite{}`, 0 `.bib`, half-done `ref/` rename pass, ~281 Vol-1 prose-style references that a regex sweep would not migrate) — the `ref/Novelty` source-of-truth pattern was the workaround for that missing infrastructure; the real fix is the citation discipline. **Durable carrying-list for all of the above:** [`../INTEGRATION-CLEANUP-TODO.md`](../INTEGRATION-CLEANUP-TODO.md) (commit `0caab7c`), with the (provisional) corrected principle, findings F1–F6 with file:line evidence, three held decisions named as Joseph's (D-1 final principle wording / D-2 wipe semantics+timing+scope / D-3 predecessor abdication & encoding), and work grouped G1–G5. `CLAUDE.md` gained an active-reconsideration callout at the top (`5314975`) pointing at the TODO; `spikes/README.md` and `doc/sop/spikes.sop.md` gain parallel callouts in this same commit. **What this means for the "Next actions" list below:** items 1–7 remain accurate for spike-corpus *routing-cycle* state, but the broader canon-integration-failure scope (~44 + sim/empirical + bulk-64 + the citation-discipline build) is now **subordinate to `INTEGRATION-CLEANUP-TODO.md`** as the durable carrying-list — the next agent works from the TODO first, then the routing tracker's items as applicable. Per Joseph's anti-rationalization stance the corrected principle and held decisions live in the TODO, not here; this writing agent has fingerprints on the principle as currently encoded — Joseph has not ratified the final wording. Treat as peer-status, not gospel.

## Next actions (the honest remaining state)

*Relocation + process-fix + the 2026-05-19 INDEX reconciliation: done (log (p) — including the 2026-05-19 integration cycles' own rows and `.integrated/MANIFEST-2026-05-19.md`). The cycle's mine-to-do hygiene is discharged; what remains is honestly tiered and queued in durable homes (per §0c — not escalating).*

1. **Reserved decision INTEGRATED 2026-05-21** (durable home was [`../PROPOSALS.md`](../PROPOSALS.md) §D.9, now CLOSED; tracking item retired from [`../PRACTICA.md`](../PRACTICA.md)). The Instance-4 / Object-B / CL-2-heavy unification landed as a single integration per `spikes/identifiability-floor-integration-plan.md`: Object B as `#der-architecture-noidentifiability` (Kalman-Ho similarity-orbit no-go, exact in linear-Gaussian sub-scope; CHT-at-agent-as-SCM, robust qualitative general; mechanism = Instance-2 Fisher-null on a $GL(n)$ Lie-group fiber, Sylvester at one remove); Instance 4 installed in `#disc-identifiability-floor` with the Sylvester-mechanism taxonomy repaired to three rank-collapse members $\{$Instance 1, Instance 2, Instance 4$\}$; Object A explicitly absorbed in `#disc-additive-coordinate-forcing` §"Downstream consequences of the (PI) commitment" with the floor-vs-coordinate-forcing distinction articulated; CL-2 heavy refinement discharged as the same object projected onto the disturbance-statistic coordinate (resolution spike §7). Math-gate repairs applied. CHANGELOG 2026-05-21. The relevant spikes (resolution / triage / neutral-drift / rho-recheck) move to `.integrated/` once a re-verify confirms no orphan content remains in each; the discharged spikes' integration-trail notes are added by the same cycle.
2. **CL-1** (`#dissipativity-template`: passivity-composition + pid-a2prime
   + bridge §7.2) — heavy coupled landing; integration-plan owed; queued
   in PROPOSALS §D.9 / TODO.
3. **`spike-update-operator-sector` tractable landing** — regression-cleared;
   honestly *pending, not done* (the deep rho/identifiability arc pulled
   away). Clean part = α-op/β-op refresh into `#deriv-sector-condition`;
   the `#disc-identifiability-floor` operator-layer part is
   reserved-adjacent (rides with item 1). Verify state before finishing.
4. **`spikes/INDEX.md` row-by-row reconciliation — DONE 2026-05-19** (log (p)). The full pass executed: the two 2026-05-19 cycle rows + the integrated-10 (→ `.integrated/`, status reconciled to the already-verified MANIFEST-2026-05-17 truth) + the rho/identifiability cluster + `update-operator-sector` + neutral-drift §8/§10.1 + instance-4-triage (repointed at the §D.9 reserved home, not re-decided) + the 2026-04-25 cluster intro + bridge-lemma HELD-note + the dangerous-direction corrections (fenchel-bregman / operator-sector landed-canon-shown-as-open). The interim banner is retired and replaced with a present-truth note; `.integrated/MANIFEST-2026-05-19.md` authored. Reconcile-to-verified, not re-verify (§0c / the bounded non-retroactive guarantee). The reserved/queued items below are pointed at their durable homes from the INDEX, not asserted resolved.
5. **Joseph-batch items** (own calls, queued): `spike-language-as-causal-substrate/`
   Theorem-1 + the C2★ gap (`der-loop-interventional-access:76`);
   `spike-attention-governance`; `temporal-nesting-rg/` Moves B/C/D.
6. **Cycle-close (when item 1 lands):** move the now-spent reserved-feed
   spikes to `.integrated/`; the trail dirs already in their durable
   `.routing-trail/` home are retained as archaeology (not deleted).
7. **Practica-`01-theory`-dive reserved residue — DISCHARGED 2026-05-19** (log (q)+(r); the whole remainder is closed). The in-cycle part was done under (q) (A2/A3/A5 fixed, A4 already done, B7 resolved-not-open, C10/D-[U] audited clean, C8/C9/C11 honest frontier). Joseph then elected both reserved calls now (r): **(7a) A1 — LANDED** (the `spike-strategy-dag-composition` math into `#def-strategy-dag` Discussion + `#result-unity-closure-mapping` + `#form-composition-closure` row repoint, per the spike's own §189 conservative landing guidance; `conditional`, Q1/Q2 in Working Notes; `spike-strategy-dag-composition.md` → `.integrated/`; `spike-composition-scaling-N.md` stays — separate practica disposition, INDEX:213 reconciled "RESOLVED"). **(7b) B6 — EXTRACTED** (`#der-compensation-channel-uniqueness`, new `04-eli-core/` §04.1 `der-`/`conditional` segment carrying continuity-`02` Proposition 1 + DPI derivation + the (FW)-failure two-channel scoping; `#der-identity-continuity-threshold` Discussion reduced to a pointer per integration-is-replacement; OUTLINE row added; lint/align/outline clean). Nothing of the practica remainder remains open.
