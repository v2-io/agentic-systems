# S4 spike-routing adjudication — adaptive / evidence / factorization slice

*Working dir `SPIKE-WORKING-111710` (file-spike adjudication class — agents
read+recommend; routing actions are the parent's). Slice S4 of the
2026-05-17 spike-routing cycle. Governing: `doc/spike-routing.md` +
`doc/audit-routing-instructions.md`. Decisive test applied throughout:
load-bearing content verified first-hand in `01-aat-core/src/`, INDEX label
treated only as a hypothesis. Git provenance used as a decisive-test
instrument where the content question was sharp (pickaxe `-S`, `log
--follow`).*

---

## One-line dispositions

| Spike | Disposition | Landing tractability |
|---|---|---|
| `spike-stochastic-non-exit-strengthening-2026-05-16.md` | **integrated-misfiled** | n/a — already canon |
| `spike-rho-factorization.md` | **orphaned** (a real no-go, *not* in canon; canon actively asserts the refuted form) | **heavy** — paired sibling landing; needs Joseph-reserved decision |
| `spike-active-inference-vs-aad.md` | **integrated-misfiled** (as a reference document; G-BP2 V-medium landed) | n/a — recommendation content is canon; doc is a durable reference catalog |
| `spike-l1-evidence-axiom.md` | **integrated-misfiled** | n/a — already canon |
| `spike-jacobian-b1-strengthening.md` | **integrated-misfiled** | n/a — moderate landing already done |

The headline finding is `spike-rho-factorization`: a true no-go whose canon
segment **still asserts the refuted multiplicative form with no obstruction
record anywhere** — the §4.1 "segment lies about itself" failure, one of the
two failures this whole cycle exists to catch. Detail in §2 below; it is the
one item in this slice that is not safe-mechanical and is flagged for the
parent + Joseph.

---

## 1. `spike-stochastic-non-exit-strengthening-2026-05-16` → integrated-misfiled

**INDEX hypothesis:** LANDED, completion-state 3. **Verdict: confirmed,
first-hand. Fully canon.** The brief's live question — "is the no-go actually
canon per spike-routing §5 / audit-routing §5–§6?" — answers cleanly **yes**,
and it is the textbook 5A handling (no-go as its own appendix), done right.

Verified in `01-aat-core/src/`:

- **`deriv-stochastic-non-exit.md`** — a dedicated 91-line `status: exact`
  appendix segment carrying the full worked no-go: the $G(t)=e^{2\alpha
  t}V$ non-supermartingale, the sign-indefiniteness of the compensated $S(t)$,
  the unbounded-scale-function / no-bounded-non-constant-harmonic-function
  obstruction, and the general $P(\tau_R<\infty)=1$ argument. This is the
  spike's §3.1–§3.2 mathematics landed verbatim-in-substance as canon. It is
  *the proof step*, on the critical path, exactly as audit-routing §4.6 / §5(A)
  prescribes for a load-bearing no-go.
- **`deriv-sector-condition.md`** — Prop A.1S corrected to (iii′) fixed-time
  tail (constant unchanged, object corrected) + (iv) finite-horizon
  Khasminskii sup-bound; **Corollary A.1S.1** (the containment dichotomy
  $P(\tau_R<\infty)\in\{0,1\}$, `status: exact`, "new exact result"); the
  Epistemic Status sentence reconciled; the Discussion "kind-of-guarantee"
  dichotomy; a full `## Findings` entry with Brief/Impact/Novelty.
- **Cascade closure verified** (audit-routing §4.2's mandatory dependent
  check): `result-sector-persistence-template.md:90` carries the corrected
  fixed-time / distributional framing — the downstream 613842-F2
  "integration-debt" propagation the spike specified is landed. No un-marked
  dependent of the corrected claim was found.

**Ghost discipline (audit-routing §5/§6) is correctly applied.** The segment
bodies + `## Findings` state present truth only; the project-autobiography
("the framework previously held a false interpolating non-exit bound", the
628401-prediction-disconfirmed record) lives in the segment's *provenance
notes* and `## Findings` history bullets, not in the canonical claim — which
is the corrected post-2026-05-16 handling of exactly the
`deriv-sector-condition.md:294` ghost the audit-routing §6 worked example
calls out. I checked the Summary-table row and the Epistemic-Status sentence:
both are clean of ghost-defense; the no-go is stated as present-tense domain
truth ("there is no $P(\tau_R<\infty)<1$ bound, and none is claimed").

**Disposition: `integrated-misfiled`.** Content fully in canon, verified
first-hand; the spike file is still at `spikes/` top level. Safe-mechanical:
parent independent-verifies the named loci (a confirmer ≠ me opens
`deriv-stochastic-non-exit.md` + `deriv-sector-condition.md` Cor A.1S.1), then
`git mv` → `.integrated/`. Reconcile the INDEX row from "LANDED" to
`integrated-filed` at cycle close. **Nothing of value lives only in the
spike** — its dead-end record ("do not re-attempt Doob/Ville") is also
canonized as the reusable no-go signature in `deriv-stochastic-non-exit.md`
Epistemic Status and the `## Findings` Working-Notes bullet of
`deriv-sector-condition.md`.

---

## 2. `spike-rho-factorization` → ORPHANED (the load-bearing finding of this slice)

**INDEX hypothesis (line 150):** "PARTIALLY ABSORBED — obstruction-record
reflected in `#internal-external-decomposition` Working Notes (Path 1
rationale)." **Verdict: the INDEX label is false in both directions, and the
canon is currently lying about itself.** This is the failure
`doc/spike-routing.md` §2 and `audit-routing` §4.1 exist to catch: a true
no-go that lives only in the spike, *and* a canon segment that asserts the
refuted positive form as if derived.

### 2.1 What the spike actually established (real, true, completion-state C/no-go)

`spike-rho-factorization.md` (Spike H, 2026-04-22) attacked the working
hypothesis $\rho = \rho_{\text{external}}\cdot f(\mathcal M)\cdot g(\pi)$
(R-F). Worked three structured cases end-to-end (scalar linear-Gaussian
Kalman; Beta-Bernoulli edge; controlled OU+LQR) + a Cauchy-FE forcing attempt
+ a sub-scope-α restriction. Outcome **(C): honest obstruction**. The result
is real and sharp: (R-F) is *not derivable* from AAT primitives; worse, it
*misrepresents* the native structure, which is variance-additive ($\rho^2 =
\rho^2_{\text{irr}} + \Delta^2_{\mathcal M} + \Delta^2_\pi + \text{cross}$,
(R-V)) — Kalman innovation is $P^\ast + r$ not $P^\ast\cdot r$; $\rho$ is
agent-conditional, $\rho_{\text{external}}$ is not well-posed without a
reference agent; $f$ and $g$ are not independent (entangle at source); no
AAT-internal additivity axiom motivates $\log\rho$ decomposition. This is a
genuine no-go with strong instructive residue — precisely the audit-routing
§5(A) "an approach a competent reader would assume we simply missed if we did
not address it" kind.

### 2.2 The canon does not state this no-go — it asserts the refuted form

First-hand read of `01-aat-core/src/internal-external-decomposition.md`
(`status: robust-qualitative`, 42 lines, the segment the parent spike was
promoted into per commit `8f9a3ca`):

- **Line 29:** "By expanding α (tempo × gain × fidelity), ρ (**volatility ×
  policy benignity × model expressiveness**), and ν …" — this is the (R-F)
  multiplicative split, stated as a derivation step.
- **Lines 35 / 39:** $\mathcal V_E$ uses $-\log\rho_{\text{external}}$;
  $\mathcal V_I$ uses $-\log f(\mathcal M) - \log g(\pi)$ — the exact three
  refuted factors, presented as the segment's "Full Decomposition", with no
  scope flag, no conditional tag, no obstruction note.
- **There are no Working Notes in the segment at all.** The INDEX claim that
  the obstruction-record is "reflected in `#internal-external-decomposition`
  Working Notes (Path 1 rationale)" is false against current `src/`.

**Git provenance (decisive-test instrument, audit-routing §8 / spike-routing
§7).** `git log --follow` on the segment: only two commits — `8f9a3ca`
(creation, "promote several recent spike findings") and `9745397` (the
AAD→AAT rename sweep). Pickaxe `git log -S'variance-additive'`,
`-S'Path 1'`, `-S'rho-factorization'`, `-S'(AV)'` against the segment path:
**all empty** — the obstruction record / Path-1 rationale / variance-additive
reframe *never entered the segment*, not in the current state and not at any
point in history. The INDEX label is not stale-from-a-later-edit; it was
never true. (This is exactly the spike-routing §7 lesson: the convenience
label is unreliable in *both* directions; only the first-hand `src/` read +
provenance settles it.)

So the present state is the audit-routing §4.1 cardinal violation: a segment
that *asserts a positive form a project spike proved false*, with the
disproof living only in `spikes/spike-rho-factorization.md` (referenced from
nowhere in the segment — and "a reference is not integration" anyway).
`status: robust-qualitative` is itself an over-claim here: the fine
multiplicative decomposition is, by the spike's own worked verdict,
*not derivable* (heuristic at best, false as stated).

### 2.3 The sibling structure (flag-don't-route — coupled, partly outside this slice)

This is a **tightly-coupled spike cluster** and the partition split it across
slices (the spike-routing §"sibling-coupling" failure mode). Flagging, not
routing, the out-of-slice members:

- `spike-rho-factorization.md` (mine, S4) — the no-go (outcome C).
- `spike-rho-additive-variance-strengthening-2026-04-24.md` (**S1's slice,
  not mine** — but read first-hand here because it is load-bearing for this
  one). This is the strengthen-first successor: it took the spike's (R-V)
  reframe and **strengthened it to a derived theorem (AV) under named
  sub-scope conditions (S1)–(S4)** via Amari–Nagaoka Pythagorean projection,
  plus a *sharp rate-domain multiplicative no-go*, plus a sub-regime catalog
  (Poisson-cascade / large-deviation / PID). Its own §8.6/§10 recommendation:
  land `#rho-decomposition` appendix, then promote
  `#internal-external-decomposition` — replace (R-F) with (AV), downgrade the
  fine decomposition robust-qualitative → conditional, *preserve the coarse
  $\mathcal V = \log\lVert\delta_{\text{crit}}\rVert - \log\rho + \log\alpha$
  at exact* (unaffected).

This is the strengthen-before-soften arc *completed in the spike layer but
never landed in canon*. The honest discharge here is **not** soften — the
strengthening already succeeded (it is the (AV) theorem); what is missing is
the *landing*. Per the integration-is-replacement discipline: the false
multiplicative split should be **replaced** by (AV) (the derived theorem) +
the rate-domain no-go stated as present-tense canon, not kept-as-is and not
kept-softened-with-a-pointer.

**Backlog corroboration (evidence hierarchy: open `[ ]` ⟹ NOT-integrated).**
`TODO.md:438` and `:480` track the `#rho-decomposition` appendix as an open
`[ ]` "(γ)-hybrid backlog landing … straight authoring now"; `PROPOSALS.md`
§D.9 (SP-22) lists the rho pair explicitly as Tier-2-ready, architecture
resolved 2026-05-14, *landing still owed*. `#disc-identifiability-floor` has
exactly four instances and Instance 4 is the (PI)/Čencov universal-constant
no-go — **not** the rho no-go; the successor spike's "land as Instance 4"
recommendation has not happened (the slot was taken by a different result; if
the rho no-go lands as a floor instance it would be Instance 5, an open
decision). No `#rho-decomposition` / `#disturbance-decomposition` segment
exists anywhere in `src/` (verified by slug grep).

### 2.4 Disposition and landing read

**`spike-rho-factorization` → `orphaned`.** Its no-go is real, true, and
*not in canon* — and canon actively asserts the refuted positive form. Two
obligations, in order (audit-routing §4):

1. **The segment must stop lying about itself (§4.1 invariant — this is the
   urgent half, not the landing).** `internal-external-decomposition.md`
   currently presents the refuted (R-F) multiplicative split as a derivation
   step at `robust-qualitative`. At minimum, before the heavy landing, the
   fine multiplicative decomposition (lines 29, 35, 39) must be marked
   not-derived / scope-flagged so a reader is not misled for the duration of
   the (substantial) repair. **Per the staging discipline this adjudication
   does not edit the segment** — flagging the §4.1 obligation for the parent
   as the priority action, ahead of the spike move itself. The coarse
   decomposition ($\mathcal V = \log\lVert\delta_{\text{crit}}\rVert -
   \log\rho + \log\alpha$, line 25) is unaffected and stays exact.
2. **The landing is HEAVY, and carries a Joseph-reserved decision.** It is
   the paired `#rho-decomposition` appendix authoring (the (AV) theorem +
   sub-regime catalog + the rate-domain no-go), plus the
   `#internal-external-decomposition` rewrite (replace R-F with AV, retier
   the fine part, preserve the coarse), plus a reserved call on whether the
   rate-domain no-go becomes `#disc-identifiability-floor` **Instance 5**
   (adding an instance to a meta-segment is the structural / promotion-level
   kind of decision spike-routing §6 routes to the Joseph batch). This is
   *not* auto-landable this cycle: it is substantial segment-authoring
   touching a new appendix + a meta-segment + an existing derivation +
   cascade, exactly the `spike-routing.md` §4 "written landing-plan,
   PRACTICA-surfaced, done deliberately (best by the spike's own
   context-holders)" case. Recommended: parent writes
   `spikes/rho-decomposition-spike-integration-plan.md` (audit-routing §4.3),
   surfaces it in PRACTICA (§4.4), and routes the Instance-5 question to the
   Joseph batch. The spike itself stays in `spikes/` (live-for-landing, not
   archived) until the landing completes — both rho spikes move to
   `.integrated/` together when `#rho-decomposition` lands, as one coupled
   sibling unit.

This is the one item in S4 that "most benefits the project" by being
surfaced loudly rather than filed: the canon has carried a refuted
multiplicative factorization at `robust-qualitative` since `8f9a3ca`, with
the disproof *and* its completed strengthening both sitting unintegrated in
the spike layer. The INDEX's "PARTIALLY ABSORBED / reflected in Working
Notes" is the convenience label that masked it.

---

## 3. `spike-active-inference-vs-aad` → integrated-misfiled (as a reference document)

**INDEX hypothesis (line 194):** "The reference document for AAT's
positioning relative to Active Inference" — not labeled LANDED/PROMOTED; framed
as a standing positioning catalog. **Verdict: the operative recommendation
(G-BP2 V-medium) is fully landed in canon; the document's residual value is as
a durable reference catalog, like `PROPOSED.md` / `INDEX.md` — it is not
`orphaned`.**

This spike is a *scoping / positioning* document, not a math spike. Its
load-bearing deliverable was the **G-BP2 tier-strength verdict: pursue
V-medium** (variational form of the strategy-cost objective; selective
Discussion-level cross-references; refuse V-strong). Verified first-hand:

- **`form-strategy-complexity-cost.md`** carries the V-medium move *in full*:
  the variational form $\Sigma_t^\ast = \arg\min[I(\mathcal C_t;\Sigma_t) +
  \beta_\Sigma D_{\mathrm{KL}}(\pi^\ast\Vert Q_{\Sigma_t})]$, the
  Pinsker/regret-bound KL-direction derivation, the explicit "analog of
  variational free energy in active inference (Friston … 2017; Da Costa …
  2020; Parr & Pezzulo 2022) **without** committing to preferences-as-priors
  or EFE-as-master" framing, and the Shannon-zero degeneracy (Gemini Finding
  2) resolved by construction. This is §E.6 of the spike, landed — and
  *strengthened past* the spike (the spike left the KL direction as a
  selection; canon now *derives* it via the regret bound, with the
  `deriv-strategy-cost-regret-bound.md` appendix carrying the uniqueness
  theorem). Completion-state (B), strengthened-past, in the canon already.
- The §C/§D positioning content (Bruineberg/Aguilera/active-inference
  refusals and distinctive-claim framing) is distributed across ≥10 segments
  (`der-directed-separation`, `der-loop-interventional-access`,
  `deriv-causal-ib-*`, `deriv-observation-ambiguity-bias-bound`, etc.) and
  `ref/Novelty_defense_and_integration.md`, per the spike's §I action 3 and
  the project's prior-art-integration rule (no orphaned positioning
  appendix).

**Disposition: `integrated-misfiled`.** The actionable content is canon. The
remaining document is a *reference catalog* (the 28-row mapping, 12-question
reviewer Q&A, §H underclaim/overlap notes) whose value is forward-looking
paper-writing support — the spike-routing §1 analog of "INDEX/PROPOSED stay,
they are not routed." Recommended: parent `git mv` → `.integrated/` (its
recommendation is discharged), and the INDEX row updated to note "G-BP2
V-medium landed in `#form-strategy-complexity-cost`; retained as the AAT↔AI
positioning reference." No canon work owed. (Minor non-blocking note for
whoever next does paper-prep: the spike's §H "underclaim" items — persistence
template's broader-validity-vs-FEP, directed-separation as scope-honest
Markov-blanket — are framing recommendations for paper introductions, not
canon gaps; they belong in the polish/sentiment ledger or a paper-prep TODO,
not re-opened as theory work. Flagging, not routing.)

---

## 4. `spike-l1-evidence-axiom` → integrated-misfiled

**INDEX hypothesis (line 117):** "PENDING REVIEW … Minimal landing: Block
Structure subsection in `#deriv-edge-update-natural-parameter`." **Verdict:
the minimal landing is DONE. Confirmed first-hand. Fully canon.** (INDEX
label understated — the spike-routing §7 "label wrong in the optimistic
direction too" case: it says PENDING but the recommended landing is present.)

The spike's own honest bottom line was that it produced **no new theorem**:
observable-$C$ block-additivity is a per-factor application of the existing
Aczél result (a generalization-in-scope of
`#deriv-edge-update-natural-parameter`, *not* a third primary instance of
`#disc-additive-coordinate-forcing`); unobservable-$C$ is a structural
inconsistency that *confirms* `#disc-identifiability-floor` Instance 2 at a
second analytical layer (dual-obstruction strengthening, *not* a new
instance); the ρ-interpolation conjecture is refuted. Its §8.5 recommended
decision was the **minimal landing**: a Block-Structure subsection in
`#deriv-edge-update-natural-parameter` + a cross-ref note in
`#disc-identifiability-floor` Instance 2.

Verified in `01-aat-core/src/deriv-edge-update-natural-parameter.md:135` —
the **"Block-structured evidential additivity under L1' correlated
evidence"** paragraph is present and carries the spike's load-bearing
content faithfully: observable-$C$ → $(2K+1)$-dim vector log-odds via
per-factor Aczél, *explicitly labeled "generalization-in-scope … not a new
primary instance"*; unobservable-$C$ → soft-EM responsibility nonlinearity
makes the block-additivity axiom structurally inconsistent; the explicit
convergence with `#disc-identifiability-floor` Instance 2's Cramér-Rao
rank-1 obstruction, framed as the dual-route "structural, not
analytical-artifact" strengthening. This is exactly the spike's §2.3 Case
A/Case B + §6.2 takeaway, landed at the correct epistemic register (no
over-claim of a new theorem — the integration-is-replacement label-tracks-truth
discipline applied correctly: a generalization is labeled a generalization).

`#disc-identifiability-floor` (read first-hand) carries Instance 2 with the
Sylvester's-law unification and the cross-route framing; the l1-evidence
dual-obstruction is consistent with and absorbed into that Instance-2
treatment (it did not need a separate instance — the spike said so, and canon
honors that).

**Disposition: `integrated-misfiled`.** Content in canon, verified
first-hand; spike still at `spikes/` top level. Safe-mechanical: parent
independent-verifies `deriv-edge-update-natural-parameter.md:135` + the
Instance-2 cross-ref, then `git mv` → `.integrated/`; INDEX row reconciled
from "PENDING REVIEW" to `integrated-filed`. The spike's §8 "deferred
quaternary landing" (block-coordinate signal function for
`#disc-credit-assignment-boundary`) is an *open follow-on* the spike itself
scoped as not-yet-needed — it belongs in TODO/Working-Notes as a forward
item, **not** a reason to keep this spike live (the math that was ready to
land, landed; the deferred item is genuinely future work, audit-routing
§"actionable-open"). Flagging for the parent: confirm a TODO line exists for
the `#disc-credit-assignment-boundary` block-coordinate follow-on so it is
not lost when the spike files; if absent, that one line is the only
actionable residue and is parent-tractable (not heavy).

---

## 5. `spike-jacobian-b1-strengthening` → integrated-misfiled

**INDEX hypothesis (line 116):** "PENDING REVIEW … three landing options
(minimal / moderate / strong)." **Verdict: the moderate landing (adopt PI +
Čencov as a primary instance + the DA2'-inc≡(CT2) transparency note) is DONE.
Confirmed first-hand. Fully canon.** Again the INDEX label understates (says
PENDING; the moderate landing is present and the strong/heredity option is
correctly *not* taken — it remains an open architectural question, which is
the honest state).

The spike's (L2) mixed-lift verdict had three pieces; all three are reflected
correctly in canon at the right epistemic register:

- **Angle 2 — DA2'-inc ≡ (CT2) at M=I (transparency win, no new axiom).**
  `form-composition-closure.md:210` carries the explicit "The Jacobian-level
  observation … incremental sector bound (DA2'-inc) … mathematically
  equivalent to the contraction-metric condition (CT2) … at $M=I$ …
  (cf. Rockafellar & Wets 1998)" note, pointing to `#result-contraction-template`.
  `result-contraction-template.md:75–100` carries the metric-α₁ "Euclidean
  metric, **AAT-internally derived via DA2'-inc ≡ (CT2) with M=I**" partition
  — the Euclidean cases lifted with no new commitment, exactly Angle 2.
- **Angle 3 — (PI) + Čencov, the only angle clearing the
  1-anchor-2-theorem discipline.** `der-gain-sector-bridge.md:108–115`
  carries the "Fisher-metric cases under parameterization-invariance" block:
  (PI) named as extending `#scope-agent-identity`, Čencov 1982 forcing the
  Fisher metric uniquely, the two statistical metric-α₂ cases (matrix-Kalman
  information metric, exp-family Fisher metric) upgraded from
  *derived-conditional-on-inner-product* to *derived (AAT-internally
  forced)*. **`disc-additive-coordinate-forcing.md` carries it as a primary
  layer** (the "Metric" row, line 44: "Parameterization-invariance (PI) …
  Čencov-invariance (Čencov 1982) … Fisher information metric") — the spike's
  candidate "fourth primary instance" landed, and was even *strengthened
  past* the spike into the Legendre–Fenchel four-layer unification (the
  meta-segment now frames all four layers, PI included, as manifestations of
  one exponential-family geometric object). Completion-state (B),
  strengthened-past.
- **Non-statistical metric-α₂ stays theorem-imported, honestly labeled.**
  `result-contraction-template.md:89–91`: Hessian-metric, Lyapunov-linear-Hurwitz,
  PID-bounded-plant each explicitly "Theorem-imported (… no AAT-internal
  axiom forces the … coordinate)". This is the spike's honest no-lift for
  three of five cases, landed as honest labeling — integration-is-replacement
  applied correctly (the label tracks truth-status, not aspiration).
- **Angle 1 — heredity / strong option correctly NOT taken.** No segment
  asserts heredity as an adopted axiom; it remains an open architectural
  question (TODO/PROPOSALS territory). The spike explicitly framed strong as
  a load-bearing architectural decision, not a mathematical necessity; canon
  honestly leaves it open. This is the right state, not a gap.

Also verified: the dependent appendix `deriv-strategy-cost-regret-bound.md`
exists (it carries the §6.1 uniqueness theorem the V-medium and
additive-coordinate-forcing work both cite). `result-contraction-template.md`
exists as the segment the spike's R1 anticipated.

**Disposition: `integrated-misfiled`.** Moderate landing complete, verified
first-hand; spike still at `spikes/` top level. Safe-mechanical: parent
independent-verifies the four named loci
(`form-composition-closure.md:210`, `result-contraction-template.md:79–91`,
`der-gain-sector-bridge.md:108–115`,
`disc-additive-coordinate-forcing.md:44`), then `git mv` → `.integrated/`;
INDEX row reconciled to `integrated-filed`. **Open follow-on, not a
keep-live reason:** the *strong* option (adopt heredity as a strengthening of
`#post-composition-consistency`, promoting (CM2-M) heterogeneous composites)
is a genuine open architectural decision the spike scoped — it is a
Joseph-reserved / PROPOSALS-level item (a framework-scope decision: heredity
would push Tier 2/3 agents formally out-of-scope). Flagging for the parent:
this is the only non-filed residue, and it is a *reserved-decision* item, not
auto-landable — recommend it be confirmed present in PROPOSALS (the spike's
§11.3 is its scoping) and routed to the Joseph batch as a decision, separate
from filing the spike. The spike files on the strength of the moderate
landing being complete; the strong option's open-ness is tracked in
PROPOSALS, not in spike-liveness.

---

## 6. Summary for the parent (actions are the parent's; this is the read)

| Spike | Disposition | Parent action | Independent-verify loci (confirmer ≠ me) |
|---|---|---|---|
| stochastic-non-exit | integrated-misfiled | verify → `git mv .integrated/`; INDEX→filed | `deriv-stochastic-non-exit.md` (whole); `deriv-sector-condition.md` Cor A.1S.1 (~L276/294) + cascade `result-sector-persistence-template.md:90` |
| **rho-factorization** | **orphaned** | **(a)** §4.1: flag/scope-mark the false (R-F) split in `internal-external-decomposition.md:29,35,39` *before* anything else; **(b)** write `spikes/rho-decomposition-spike-integration-plan.md`, surface in PRACTICA; **(c)** route the Instance-5 question to Joseph batch; **(d)** keep BOTH rho spikes in `spikes/` (coupled unit) until `#rho-decomposition` lands | `internal-external-decomposition.md` (whole, 42 ll — confirm no Working Notes / no obstruction record); pickaxe `-S'variance-additive'`/`-S'Path 1'` on the segment path (confirm empty); `TODO.md:438,480`; `#disc-identifiability-floor` instance count (=4) |
| active-inference | integrated-misfiled (reference doc) | verify → `git mv .integrated/`; INDEX row: "G-BP2 V-medium landed; retained as AAT↔AI positioning reference" | `form-strategy-complexity-cost.md:42–69,137` |
| l1-evidence | integrated-misfiled | verify → `git mv .integrated/`; INDEX→filed; confirm a TODO line for the `#disc-credit-assignment-boundary` block-coordinate follow-on | `deriv-edge-update-natural-parameter.md:135` + `#disc-identifiability-floor` Instance 2 cross-ref |
| jacobian-b1 | integrated-misfiled | verify → `git mv .integrated/`; INDEX→filed; confirm PROPOSALS carries the open *strong/heredity* decision (route to Joseph batch as a decision, not a spike) | `form-composition-closure.md:210`; `result-contraction-template.md:79–91`; `der-gain-sector-bridge.md:108–115`; `disc-additive-coordinate-forcing.md:44` |

**Slice headline.** Four of five are clean `integrated-misfiled` —
content first-hand-verified in canon (three of them at the right
epistemic register; two, active-inference and jacobian-b1, *strengthened past*
the spike, which canon labels correctly). The INDEX was wrong in the
*optimistic-understating* direction for l1-evidence and jacobian-b1 ("PENDING"
when landed) — the mirror of the pilot's lesson, confirming the first-hand
read is non-optional in both directions.

**The one that matters: `rho-factorization` is `orphaned` and the canon is
lying about itself.** A true no-go (and its *completed* strengthen-first
successor, the (AV) theorem) sits unintegrated while
`internal-external-decomposition.md` asserts the refuted multiplicative
$\rho = \rho_{\text{external}}\cdot f(\mathcal M)\cdot g(\pi)$ at
`robust-qualitative` with **no obstruction record anywhere** — and the INDEX's
"PARTIALLY ABSORBED / reflected in Working Notes" is a convenience label that
is false against `src/` and against the entire git history. The §4.1
"segment must not lie about itself" obligation is the priority action and is
*not* the same as the (heavy, Joseph-reserved) landing. This is flagged
loudly per the brief's "what most benefits the project overrides conformance"
— it is the failure the whole cycle exists to catch, found live in my slice.

**Frame note (re-truthification channel, audit-routing §7 / spike-routing
§intro).** The S4 partition kept the rho *no-go* (this slice) split from its
rho *strengthening successor* (S1's slice). The sibling-coupling refinement
already in the tracker covered the operator-family; the **rho-factorization
↔ rho-additive-variance pair is a second instance of the same coupled-sibling
shape** and should be added to the partition's known-clusters list so a
future fan-out does not adjudicate one without the other. An agent given only
`spike-rho-factorization` and trusting "the rho work resolved into
variance-additive" (the INDEX framing) would mis-route it to
`integrated`/`subsumed` — exactly the pilot-023198 failure mode, recurring.
Surfacing, not routing.
