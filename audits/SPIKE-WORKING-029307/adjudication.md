# SPIKE-WORKING-029307 — Adjudication (Slice S5)

*Adjudicator: fan-out agent, 2026-05-17. Slice S5 — small orphan-suspects +
the NeurIPS back-integration doc. Read/report-only; no moves/edits/commits.
Every content-in-canon claim below is first-hand-verified against current
`src/` with named loci, and where it was the sharpest instrument, git
provenance (`-S` pickaxe, `--follow`, `--diff-filter=A`, dates in context)
was used per `doc/spike-routing.md` §7 / audit-routing §8.*

Governing frame: `doc/spike-routing.md` (five-state disposition §3, evidence
hierarchy §7, landing-scope §4) + `doc/audit-routing-instructions.md`
(strengthen-first §2, four completion-states §3, no-go protocol §4, ghost
discipline §5/§6).

---

## Summary table

| Spike | State | Recommended home | Landing |
|---|---|---|---|
| `spike-alignment-impossibility.md` | **orphaned (partial)** — core no-go in canon; the VCG/TU **strengthening** is the real open work | core no-go: already canon (`#disc-identifiability-floor`, `#deriv-strategic-composition`); VCG-escape: strengthen-first spike | **heavy** (a strengthening attempt, not a transcription) — queue with integration-plan |
| `spike-aporia-sub-agent-adversarial.md` | **orphaned (claim 1 only) / live-or-open (claims 2–3)** | claim 1 substance already canon (`#def-unity-dimensions`); claims 2–3 correctly tracked as SP-18 / INDEX | none this cycle — correctly parked; recommend INDEX wording fix |
| `spike-fep-suboptimal-approximation.md` | **integrated-misfiled** | `#disc-ciy-unified-objective` (lines 58, 64, 66) — the exact landing the spike asked for | safe-mechanical `git mv` → `.integrated/` after independent-verify |
| `spike-message-passing-credit-assignment.md` | **integrated-misfiled** | `#disc-credit-assignment-boundary` (line 130 + 87 + 95) — corrected taxonomy co-authored with the spike | safe-mechanical `git mv` → `.integrated/` after independent-verify |
| `spike-attention-governance.md` | **orphaned (residual self-flagged speculative) / archived-candidate** | core insight already canon via sibling; residual is gestural by the spike's own §10 | none — Joseph-adjudicated archived-vs-parked call (it's a reserved judgment) |
| `spike-attention-causal-graphs.md` | **integrated-misfiled (load-bearing core) + speculative residual** | core (Version 4 / "Implications for κ") is canon at `#der-directed-separation` | safe-mechanical `git mv` candidate, but **see coupling flag** — adjudicate with `spike-attention-governance` as a pair |
| `neurips-back-integration-2026-05-08.md` | **not a claim-spike — live-or-open (integration-tracking doc, partially executed)** | stays in place; it is its own tracker, Phase A item 5 landed, B/C open | none — it is an active integration plan, not a spike to retire; INDEX path is stale |

The two genuinely-hard ones are `spike-alignment-impossibility` (where the
real theory work — the VCG strengthening — has *not* been done and the spike's
own §7 "forward-pass repair" is a strengthen-first target, not a transcription
job) and the `neurips-back-integration` doc (which is not a spike at all and
should not be processed under spike-retire mechanics).

---

## 1. `spike-alignment-impossibility.md` — orphaned (partial); the open work is a strengthening, not a landing

**State: orphaned, but the orphaned part is a strengthen-first target.**

Provenance (decisive): the spike was created 2026-04-25 (`73f43a0`). The
`#disc-identifiability-floor` "Mechanism-Design Impossibility (candidate 4th
instance)" block and the `#deriv-strategic-composition` §Discussion
mechanism-design paragraph were both already present at the 2026-04-24
role-prefix sweep (`e6adf9e`) — i.e. **the day before the spike**. So the
canon's no-go instance is *not* downstream of this spike; they are parallel.

**What is in canon (first-hand-verified):**

- `01-aat-core/src/disc-identifiability-floor.md:120-128` — full
  Gibbard-Satterthwaite + Myerson-Satterthwaite + Arrow treatment, in the
  exact meta-pattern shape (setting → external theorem → no-go → boundary
  characterization → strengthened-consequence), explicitly naming
  `#deriv-strategic-composition`'s sub-scope α′ potential-game conditions as
  the AAT-machinery escape. Tagged **"Candidate fourth instance … Open."**
- `01-aat-core/src/deriv-strategic-composition.md:179` (Discussion), `:184`,
  `:197` (Working Notes) — same no-go, "candidate adjacent-floor instances
  of `#disc-identifiability-floor`", "Flagged for future follow-up spike;
  not derived in this segment."

So the spike's **core no-go** (GS structurally forbids non-dictatorial
alignment protocols under U_O < 1) is present-tense canonical truth, properly
scoped as a *candidate* (not-yet-derived) instance with escape routes named.
That part is integrated — and was integrated independently of this spike.

**What is NOT in canon — and why this is the strengthen-first heart of it:**

The spike's §7 "Adversarial Critique & Forward-Pass Repair" is the load-bearing
content and it is *not* a transcription job. The critique (GS is ordinal;
AAT objectives are cardinal V_O → ℝ; with transferable utility, VCG mechanisms
restore strategy-proof alignment and the impossibility *vanishes*) is a real
defeater of the bare no-go. The spike's forward-pass repair turns it into a
**prescriptive engineering result**: heterogeneous multi-agent AI systems must
carry a computable transferable currency (compute tokens / API budget /
context) for VCG side-payments, *else* GS holds and deception (Regime E-IV via
`#der-agent-opacity`) is mathematically guaranteed.

This is exactly the strengthen-before-soften shape (audit-routing §2/§3): an
apparent no-go, when pushed, becomes a **stronger conditional result with a
named escape and an engineering prescription** — completion-state (B)
"strengthened past the claim." The canon currently carries only the *bare*
no-go-as-candidate and lists "full mechanism-design derivation (VCG,
Bayesian-Nash)" as future work (`#deriv-strategic-composition:158` Working
Notes, `:197`). Verified: VCG/side-payment/transferable-utility appears
**nowhere** in `01-aat-core/src`, `03-llm-core/src`, `02-tst-core/src` except
that one Working-Note future-work line. The cardinal-vs-ordinal escape — the
single most important thing the spike found — is **not** in canon.

**Disposition.** `orphaned`. The open content is a **strengthening attempt**,
not a safe-mechanical landing: working out the VCG/TU escape, the
Bayes-Nash relaxation, and which AAT machinery the escapes operationalize, to
land Instance 4 properly (per `#disc-identifiability-floor:122` "would require
a dedicated formalization of the AAT-machinery escape route"). This is
**heavy** — a new derivation segment (or a substantial `#deriv-strategic-
composition` strengthening) plus the M1 Instance-4 promotion in
`#disc-identifiability-floor`. Per spike-routing §4 it gets a written
integration-plan surfaced in PRACTICA, done deliberately. It is **not**
auto-landable and must not be softened to "the no-go is already in canon, done"
— that would discharge the inconsistency in the wrong direction (the spike's
whole §7 point is that the bare no-go is *false* once you allow cardinal
utility + TU; canon's "candidate instance, open" framing is honest only
because it is explicitly not-yet-derived, but the strengthening is the
cargo).

Cross-check, no contradiction: the spike's body §4 still presents the bare
no-go as the headline and only reaches the cardinal-utility defeater in §7;
an agent skimming §1–§6 would mis-route this as "no-go in canon, integrated-
filed." The first-hand read of §7 is what flips it to orphaned-strengthening.
This is the INDEX-label-unreliable / read-the-whole-thing scar in live form
(INDEX:57 says "OPEN — substantive no-go", which understates it — the open
thing is a *strengthening*, not the no-go).

## 2. `spike-aporia-sub-agent-adversarial.md` — orphaned (claim 1) / correctly-parked (claims 2–3)

Self-labeled "Brainstorm, not even hypothesis." Three formal claims if the
conjecture holds:

1. **Teleological unity is axis-dependent; scalar U_O is a projection of a
   richer per-dimension structure.** **In canon, and sharper than the spike
   conjectured.** `01-aat-core/src/def-unity-dimensions.md:42` ("$+1$ …
   $-1$ … per objective dimension"), `:113` (the
   cooperative-on-quality / competitive-on-resources example —
   structurally identical to the spike's "adversarial on one axis, aligned
   on another"), and the *settled* refinement at `:22`, `:44`, `:116` that
   composite scope is a four-route disjunction, **not** a scalar U_O
   threshold, and that "whether the three alignment routes reduce to a
   single scalar is not established." The spike's "single scalar U_O would
   need to be recognized as a projection of a richer per-dimension
   structure" is realized — independently; this is convergence-as-coherence-
   evidence, not a debt owed to the spike.
2. **Adversarial-tempo-advantage applies internally to a composite's
   sub-agents.** **Not in canon.** First-hand: `result-adversarial-tempo-
   advantage.md` has no internal/sub-agent application (grep for
   internal/sub-agent/aporia/within-composite: empty). Genuinely open.
3. **Theory-of-mind gates productive internal aporia; ties to logozoetic
   qualifying properties.** Not in canon; `04-eli-core/` is explicitly
   future-work.

**Disposition.** Claim 1's substance is canon (no debt). Claims 2–3 are
genuinely open and **already correctly tracked**: `PROPOSALS.md` SP-18
(brainstorm-grade, "Load-bearing for `04-eli-core/` and Section III
adversarial/cooperative integration … Reopen when logozoetic work matures.
Value +3 to +5") and `spikes/INDEX.md:216`. This is **`live-or-open` for the
open claims** — incomplete and still needed, properly parked with a tracked
home — and there is no orphaned residue to land. The spike stays in
`spikes/`. No cycle action.

*Recommend (flag, don't route — wording):* INDEX:216 and SP-18 read fine, but
neither records that claim 1 is now superseded-by-canon. A one-line
breadcrumb ("the per-dimension/projection claim is settled in
`#def-unity-dimensions`; SP-18's open content is claims 2–3 only") would keep
a future agent from re-deriving claim 1. History-layer note, not a body edit.

## 3. `spike-fep-suboptimal-approximation.md` — integrated-misfiled

The spike's own §5 named its best landing: *"a small Discussion addendum in
`#disc-ciy-unified-objective` noting that EFE-like objectives are recovered
under specific restrictions (preferences-as-priors, scalar epistemic price);
do not promote as a dominance theorem."* That landing **exists** and is
faithful (first-hand-verified):

- `01-aat-core/src/disc-ciy-unified-objective.md:58` — dark-room bypass via
  the Survival Imperative (= spike Assumption 1, "Dark Room Collapse").
- `:64` — full EFE pragmatic/epistemic decomposition, structural isomorphism
  ($Q_O$ ≈ pragmatic, CIY ≈ epistemic) **with the two substantive
  differences named**: preferences-not-as-priors (= spike Assumption 1) and
  causal-not-associational information / Level 2 vs Level 1 (= spike
  Assumption 3), with the dark-room critique (Sun & Firestone 2020) cited.
- `:66` — the regret-bound / KL-direction route that makes the point
  *without* claiming strict suboptimality — exactly the spike's
  "do not promote as a dominance theorem; claiming EFE strictly suboptimal
  is an overreach."

Provenance: the segment's "dark-room is bypassed" / "pragmatic value"
content entered at `e39c17b`/`73f43a0` (2026-04-25, the causal-IB and
spike-intake commits) — co-temporal with the spike, and the spike explicitly
said to "wait for the causal-IB LMI work to settle." Causal-IB has since
settled (`#deriv-causal-ib-exploration`, `#deriv-causal-ib-lmi` are canon),
and the landing the spike scoped is present and correct.

The only spike element not mirrored is Assumption 2 (scalar/isotropic Λ
epistemic-pricing as the EFE recovery condition). Per integration-is-
replacement and the spike's own self-limitation, this is **not** a gap: the
spike explicitly recommended *against* promoting the formal three-assumption
EFE-recovery derivation; the segment correctly carries the *result*
(structural-isomorphism-with-named-differences) at Discussion grade and
declines the dominance-theorem the spike warned off. Nothing true lives only
in the spike.

**Disposition.** `integrated-misfiled`. Content in canon, spike still at
`spikes/` top level. Safe-mechanical `git mv` → `.integrated/` after the
independent-verify (confirmer ≠ adjudicator) spot-checks `:58/:64/:66`.
**Tractable / no landing work.** INDEX:58 ("OPEN — author-flagged 'small
Discussion addendum' target … would land later after causal-IB settles") is
**stale** — causal-IB settled and it landed; reconcile to `integrated-filed`
at cycle close.

## 4. `spike-message-passing-credit-assignment.md` — integrated-misfiled

Provenance is decisive and clean: the spike **and** the corrected Level-2
taxonomy in `#disc-credit-assignment-boundary` were introduced in the **same
commit `73f43a0` (2026-04-25)** (pickaxe on "Expectation Propagation (EP)"
and "loopy BP or max-sum" both resolve to `73f43a0`). They were co-authored:
the spike is the reasoning trail (including the mean-field VMP dead-end and
its §6 self-refutation), and the segment carries the *corrected result*.

What the spike actually establishes, once its own §6 adversarial critique is
applied (mean-field VMP is catastrophic on deterministic AND/OR gates →
forward-pass repair to EP / Max-Sum / loopy-BP on factor graphs preserving
AND/OR as exact potentials), is **in canon** (first-hand-verified):

- `01-aat-core/src/disc-credit-assignment-boundary.md:95` — the #P-hardness
  result, anchored *more sharply* than the spike (Shapley-over-AND/OR-game,
  Deng-Papadimitriou 1994 #P-completeness), with the exact-vs-approximate
  caveat.
- `:87` — tree-DAG / observable-leaves exact-BP case (= spike's correct
  sub-case).
- `:130` — the full corrected Level-2 taxonomy: exact BP on tree/polytree,
  **loopy BP or max-sum for MAP-style diagnosis, Expectation Propagation
  (EP) for approximate marginals, and structured variational methods only
  where common-cause structure is explicitly modeled.** This is precisely the
  spike's §6 forward-pass repair *and* its §4 mean-field-floor finding (the
  "structured variational only where common-cause is explicitly modeled"
  caveat is the spike's L1-correlation floor). Mean-field VMP is correctly
  *excluded* — i.e. the spike's refuted §3 core is integrated-as-replacement,
  not integrated-as-ghost.
- `:148` — the theory-vs-engineering framing (requirement is theory,
  implementation is engineering) generalizing the spike's "explicit limits"
  point.

The only thing not in canon is a **full standalone derivation** appendix
(`#deriv-factor-graph-credit-assignment`). But the spike *itself* flags that
as requiring a rewrite (mean-field → loopy-BP/EP) before promotion, and
INDEX:59 records exactly this ("flagged for rewrite before promotion …
Discussion-level coverage exists in `#disc-credit-assignment-boundary` …
the full derivation is queued"). Per *math-lives-in-segments* the question is
whether real true math lives **only** in the spike: it does not — the
load-bearing *result* (correct algorithm selection by DAG class + epistemic
bounds + the mean-field-breaks-on-L1 floor) is in the segment at the
honest Discussion grade. The un-landed appendix is an *optional strengthening*
(Discussion-grade → derived-grade), not orphaned truth.

**Disposition.** `integrated-misfiled`. Safe-mechanical `git mv` →
`.integrated/` after independent-verify of `:87/:95/:130`. **Tractable / no
forced landing.** Note for the parent: the queued full-derivation appendix is
a legitimate *optional* strengthening to record in TODO/PRACTICA if not
already (it is — INDEX:59 "the full derivation is queued"); moving the spike
to `.integrated/` does not lose it because the queue entry is independent.

## 5–6. The two attention spikes (`spike-attention-governance.md`, `spike-attention-causal-graphs.md`) — coupled; adjudicate as a pair

Provenance (decisive): both attention spikes **and** the
`spike-kappa-topology-insight.md` that landed `#der-directed-separation` were
created in the **same commit `446c7a1` (2026-03-14, "Brainstorm the kappa
idea and LQR etc.")** — one overnight session, three sibling artifacts.

**The load-bearing core IS in canon.** The most consequential structural
claim across the two attention spikes — `spike-attention-causal-graphs`
Version 4 + "Implications for the κ Problem" (lines 284–426): *directed
separation is architecture-dependent not universal, because epistrophic-intent
and strategic-intent either share processing infrastructure (merged →
fails; transformer attention is the canonical merged case) or are separate
(modular → holds); κ is not a parameter of f_M but the topology of the
processing graph; characterize which topologies admit separation rather than
parameterize a perturbation expansion* — **is fully canonical** at
`01-aat-core/src/der-directed-separation.md:57-63, :77, :85, :89, :120, :146`
(Class 1/2/3 architectural classification; κ_processing as
distribution-dependent diagnostic for Class 2; transformer-LLM-attention =
Class 3 "fails by construction"; "Why the classification is not a smooth
parameter"). First-hand-verified. `:120` explicitly credits the *sibling*
`spikes/spike-kappa-topology-insight.md` (now `.integrated/`) as the
promoted source. The attention spikes reached the same insight from the
fighter-pilot/attention-governance angle; the core landed via the sibling —
convergence-as-coherence-evidence, and the truth is not spike-only.

**The residual is self-flagged speculative and is NOT in canon.** Both
spikes' distinctive additive proposals — finite-attention as a first-class
constraint alongside finite-observation/action, sentinel CIY (exploitation /
exploration / sentinel split), severity = δ × ∂Σ/∂M as a product signal,
multi-frequency self-composition (primary/sentinel/strategic loops), the
attention-allocation-belongs-in-Σ_t move, severity-proportional response /
POSIX mapping — are **not** in canon. Verified: grep for finite-attention /
sentinel / attention-governance / startle / multi-frequency / severity-
proportional across all three `src/` trees returns only
`der-directed-separation.md` (the line-40/42/127 *goal-directed-sensing*
mentions, which are the directed-separation selection/processing distinction,
**not** the spike's attention-governance machinery). `der-temporal-nesting`
carries singular-perturbation timescale-stratification but **not** the
spike's sentinel-loop / attention-reallocation content. And
`spike-attention-governance` self-labels in its own §10 + closing line:
*"the most speculative of the three overnight spikes … the formal content is
thin … the multi-frequency loop structure is gestural — it needs either a
formal model or a concrete example to evaluate,"* with explicit open
questions (is finite-attention already captured by IB? is severity-
proportional response already implied by ∂Σ/∂M × δ? is multi-frequency
derivable from `#der-temporal-nesting`?).

**Disposition — and why this is a Joseph-reserved call, not auto-file.**
`spike-attention-causal-graphs` is, on the load-bearing core,
`integrated-misfiled` (Version 4 / κ-implications → `#der-directed-
separation`). But its residual (the 5-version causal-graph ideation,
"What I Notice Is Missing", the dual-control/LQG-separation-failure-as-causal-
graph framing) is exactly the kind of cross-domain first-encounter ideation
the dir-spike gold gate exists to protect — and `spike-attention-governance`
is *almost entirely* residual of that kind (its core already in canon via the
sibling; its body is the speculative governance architecture). Filing
`spike-attention-governance` to `.integrated/` would assert "load-bearing
content present in canon" — **true for its κ-core but false for its actual
body**, which is the unintegrated speculative layer. Filing it to
`.archived/` would assert "consciously set down, not in canon" — closer, but
it is *not dead*: §10's open questions are live research seeds (the
finite-attention-as-IB-consequence question especially), and INDEX:205 keeps
both as "Exploratory; not yet promoted."

Per `doc/spike-routing.md` §6 (the gate's operative axis is
**decision-type, not artifact-shape** — "route to the Joseph batch anything
whose resolution requires a decision Joseph reserved, file or dir"): the
archived-vs-parked-vs-research-seed call on `spike-attention-governance` is a
**truth-claim about the theory's needs** (is finite-attention a real missing
postulate or an IB consequence? is multi-frequency-loops a `#der-temporal-
nesting` corollary or genuinely additional?) — that is a reserved judgment,
not an agent auto-file. **Recommendation to Joseph batch:**

- `spike-attention-causal-graphs.md`: core `integrated-misfiled` (→
  `.integrated/`, `#der-directed-separation` is the home); recommend a
  one-line INDEX:205 update recording that the Version-4 / κ-topology core
  is canon and only the multi-version ideation residual is exploratory.
  *Coupling caveat:* its residual and `spike-attention-governance`'s residual
  are the same overnight ideation cluster — if `governance` is parked rather
  than filed, consider keeping `causal-graphs` visible too for one cycle so
  the pair is read together. This is why I am **flagging, not routing** the
  pair.
- `spike-attention-governance.md`: **Joseph-reserved.** My read: it is
  *not* `integrated-misfiled` (body is unintegrated speculation) and *not*
  cleanly `archived` (live research seeds). Closest honest bucket is
  **`live-or-open` as a research-seed** — but whether finite-attention earns
  a postulate, or is an IB/temporal-nesting consequence, is the reserved
  truth-call. Recommend it go in the dir-spike-style Joseph batch with this
  framing, not auto-filed by the parent.

## 7. `neurips-back-integration-2026-05-08.md` — NOT a claim-spike; an active integration tracker, partially executed

This is the §S5 "adjudicate what it actually is" item. **It is not a
claim-spike and must not be retired under spike-retire mechanics.** It is an
*integration overview / back-integration plan* authored by Tessera 2026-05-08
(`30f2dce`) — created **in `msc/`**, later moved to `spikes/` (the no-op
content move in `c1c80a9`, "Consolidate audit working dirs … repoint live
references"; `git log --follow --diff-filter=A` confirms original path
`msc/neurips-back-integration-2026-05-08.md`). It is structurally the
spike-routing analog of `pending-findings-*.md` ledgers / `spikes/INDEX.md` —
a **durable plan/tracker that stays**, not a unit of investigation to
dispose.

**Is its content in canon?** Partially, and it is *honestly self-tracked*:

- §6 progress note (verified against git `b2440d3`, `61d53ea`): **Phase A
  item 5 landed** — 13 source segments carry NeurIPS cross-reference Working
  Notes (Paper 1 → `deriv-causal-ib-exploration`/`-lmi`; Paper 2 → six
  segments incl. `der-loop-interventional-access`, `schema-strategy-
  persistence`; Paper 3 → `deriv-observation-ambiguity-bias-bound`,
  `der-directed-separation`, `scope-channel-collapse`, `scope-observation-
  ambiguity-modulation`; multi-paper → `scope-agent-identity`). Spot-checked:
  `#disc-identifiability-floor:92-99` Instance 4 carries the Paper-3
  chart-rescaling-no-go cross-reference and the back-integration-progress
  marker — consistent with the doc's inline progress claims.
- Phase A items 1–4 (catalog updates, INDEX cross-refs) and Phases B
  (segment-level absorption — new segments `#deriv-bh-pointmass-identity`,
  `#deriv-post-update-chain-rule`, `#deriv-chart-rescaling-no-go`; the
  substantive strengthenings) and C (meta-architectural M1/M2/M3 surfacing)
  are **open**, and the doc *says so*, with the Joseph-directed re-scope
  noted (catalog updates deferred until after segment-level absorption;
  `msc/FINDINGS-RANKED-DRAFT.md` is scratch not canon — itself since sunset).

**The real truth-loss risk here is the opposite of an orphaned spike.** The
doc contains, in §1, the highest-value not-yet-reconstructable artifact: the
paper-section ↔ ASF-source-segment cross-mapping for three NeurIPS
submissions, with §1 item-level notes on **strengthenings the papers
generated that ASF has not yet absorbed** (KKT shadow-price resolution,
per-action LMI pathwise survival, F-A-G-P enforcement, the BH point-mass
*exact identity*, the structural-class theorem on gain-decay updates, the
chart-rescaling no-go, the (C1)-(C2)-(C3) sequential-ignorability framework,
the Class-1→Stuart-school reduction, the Coupled-class autoregressive
connectivity lemma). Several are **completion-state (B) "strengthened past
the claim" results that currently live only in `~/src/neurips/` paper
appendices** — i.e. the math-lives-only-outside-canon failure, one repo over.
The doc's §8 names this precisely ("the catalog should be read as the
substrate from which extractions sharpen, not as the sharpened form … without
[back-integration] the catalog's looser claims persist while published
versions become the de-facto canonical statements").

**Disposition.** `live-or-open` — **stays in place; not routed, not retired,
not moved.** It is an active, partially-executed integration plan; Phase A.5
landed, Phases A1-4/B/C are real open theory work (multiple heavy segment-
authoring landings + a strengthen-first absorption per §2.3 "no-go-forces-
axiom"). Per spike-routing §1/§3 a still-needed incomplete plan is
`live-or-open`. Two flags for the parent (flag-don't-route — these touch
reserved calls and cross-repo source-of-truth):

1. **INDEX path is stale.** `spikes/INDEX.md:35` references
   `msc/neurips-back-integration-2026-05-08.md`; the file is at
   `spikes/neurips-back-integration-2026-05-08.md`. The *status* claim
   ("stays queued and is progress-marked inline") is accurate; only the path
   is wrong. Recommend reconcile at cycle close (and decide deliberately
   whether the doc's home is `spikes/` or `msc/` — it is a back-integration
   *plan*, closer to `msc/` working-artifact than to a `spike-*`; but it is
   surfaced from INDEX and CHANGELOG, so the rename must repoint backlinks —
   a parent action, not mine).
2. **Cross-repo source-of-truth (spike-routing §3 decision rule).** Phase B's
   new-segment landings (`#deriv-bh-pointmass-identity` etc.) would import
   results whose current source-of-truth is `~/src/neurips/` papers **in
   review** (anonymized, not yet citable — the doc's §7 flags this). Per the
   §3 rule, segment-level absorption that hard-binds those results is
   premature until the papers settle; the cross-reference Working Notes
   (Phase A.5, landed) are the correct current state. This is the same shape
   as pilot 023198's `spike-c2-star`. Recommend Phase B stays queued behind
   the paper review outcome — a Joseph/owner call, surfaced not actioned.

---

## Independent-verify handoff (confirmer ≠ adjudicator)

Load-bearing content-in-`src/` claims a confirmer should primary-source
spot-check before any `git mv`:

- **FEP → integrated-misfiled:** `disc-ciy-unified-objective.md:58, :64, :66`
  carry the dark-room-bypass + EFE-isomorphism-with-two-named-differences +
  no-dominance-theorem treatment the spike §5 scoped. (If confirmed:
  safe `git mv` → `.integrated/`; reconcile INDEX:58 stale "OPEN".)
- **Message-passing → integrated-misfiled:**
  `disc-credit-assignment-boundary.md:130` carries the corrected
  EP/loopy-BP/structured-variational taxonomy (mean-field correctly
  *excluded*) + `:95` #P-hardness + `:87` tree-BP. Same-commit co-authorship
  (`73f43a0`) supports integration-as-replacement, not ghost.
- **attention-causal-graphs core → integrated-misfiled:**
  `der-directed-separation.md:57-63, :85, :89, :146` carry the
  architecture-dependent Class 1/2/3 / κ-as-topology result =
  spike Version 4 + "Implications for κ". (Coupling caveat applies — do not
  `git mv` until the attention pair is adjudicated together; see §5–6.)
- **alignment-impossibility core-in-canon (but spike stays orphaned):**
  `disc-identifiability-floor.md:120-128` + `deriv-strategic-
  composition.md:179` carry the bare GS/MS/Arrow no-go as candidate-instance.
  Confirm **also** that VCG/transferable-utility is absent everywhere except
  `deriv-strategic-composition.md:158` (future-work Working Note) — that
  absence is what keeps the spike `orphaned` (strengthening open), not
  `integrated`.

## What I'd flag about the frame (asked for)

The frame held well. Three observations, not objections:

1. **The five-state grid has no clean cell for "core landed independently,
   spike's real payload is an un-attempted strengthening."** `spike-alignment-
   impossibility` is neither `integrated` (its §7 cardinal-utility defeater is
   not in canon) nor plain `orphaned` (the *bare* no-go *is* in canon, via a
   parallel path). The honest disposition is "orphaned **as a strengthen-
   first target**" — the open work is a §2/§3 strengthening attempt, not a
   transcription. Pilot 023198's Refinement 1 added a cross-repo cell;
   this is a *different* missing cell (core-already-canon-via-parallel-path +
   strengthening-still-owed). Recommend a §3 note: when the no-go/result is
   already canon but the spike's adversarial-critique/forward-pass-repair
   section names an un-attempted strengthening, the disposition is
   `orphaned`-strengthening (heavy; integration-plan + PRACTICA), and the
   reflex to call it "integrated, done" is the soften-disguised-as-routing
   the whole protocol exists to catch.

2. **The integration-doc-in-the-spike-slice is a category the spike-retire
   mechanics actively mis-handle.** `neurips-back-integration` *looks* like a
   42KB orphan but is a durable partially-executed tracker (the
   `pending-findings-*` / INDEX analog). The brief correctly told me to
   "adjudicate what it actually is" — surfacing the answer (it stays, it is
   not a spike) is the right move, but a future fan-out agent handed a
   similar doc without that instruction could `git mv` it to `.integrated/`
   on the "content partially in canon" hypothesis and bury an active
   strengthen-first plan whose real content (the §1 cross-mapping + the
   un-absorbed paper-grade strengthenings) lives one repo over. Recommend
   `doc/spike-routing.md` §1/§3 explicitly name "integration/back-integration
   plan" as a `live-or-open` durable-artifact class alongside INDEX/PROPOSED,
   not a routable unit.

3. **Convergence creates a benign "ghost-shaped but not a ghost" pattern.**
   Three of my seven (aporia claim 1, both attention spikes' core) have their
   load-bearing content in canon via an *independent parallel derivation*,
   not via this spike. That is convergence-as-coherence-evidence, and the
   correct disposition is integrated/parked **without** any "this spike's
   content was absorbed" history note in the segment — the segment owes this
   spike nothing; writing a provenance breadcrumb *into the segment* would be
   the autobiographical-voice-in-canon failure (§5/§6). The breadcrumb (if
   any) belongs only in INDEX/Working-Notes. I have kept all such notes in
   this adjudication / recommended them for INDEX, never for segment bodies.
