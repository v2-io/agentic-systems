# SPIKE-WORKING-023198 — Adjudication (pilot slice)

Cycle: spike-routing 2026-05-17. Adjudicator: pilot agent.
Slice: `spikes/spike-c2-star-to-integrate.md`, `spikes/spike-operator-sector-unification.md`.
**Report only — no moves/edits/commits. Routing actions are the parent's.**
Independent-verify gate (audit-routing §8): every content-in-`src/` claim
below is first-hand `grep`/`Read`-verified and the loci are named so a
confirmer (≠ me) can re-check without trusting this summary.

---

## Spike 1 — `spike-operator-sector-unification.md`

### Disposition: `integrated-misfiled` → parent `git mv` to `spikes/.integrated/` (safe-mechanical)

**Not** `orphaned`. This is the higher-confidence of the two and the one
where the brief's counterintuitive reflex (strengthen-first) already
*happened*, by a successor spike, and won.

#### What the spike is

The C1 question: does one operator-sector primitive unify the ODE template,
the discrete update, the edge-update, and the composition map? The spike's
own honest verdict (§9, §11): **partial — "2-instance-plus-1-consequence",
not a 3-instance theorem; load-bearing gain is the α/β → operator-family
recast; recommendation: land content, DO NOT elevate to a fourth
meta-pattern unless O-BP10 surfaces at segment level.**

#### The decisive history (verified first-hand, not from the INDEX label)

The INDEX label is a convenience record and here it is actively
self-contradictory: line 64 calls `spikes/.integrated/spike-operator-sector-unification.md`
the "predecessor", but the file is still at `spikes/` top level (56 KB, the
`.integrated/` lookup for it returns nothing). The INDEX row at line 127
says "PENDING REVIEW". Neither is ground truth. What is ground truth:

The C1 spike's "do not elevate unless O-BP10 surfaces" gate was taken as a
**strengthening target**, not a stopping point. A successor *directory*
spike `spikes/.integrated/spike-operator-family-unification/` (6 files,
2026-05-14, **already archived**) pushed the question per Joseph's "push
until a revealing no-go or the unifying mechanism" and landed **strictly
stronger** content as canon — this is spike completion-state **(B)
strengthened past the claim** (audit-routing §3), plus a sharp **plural
no-go**.

#### Content-in-canon verification (the decisive test, first-hand)

The C1 spike's load-bearing claims are all present in `src/`, verified by
read, not by label:

| Spike §  | Load-bearing content | Canon locus (verified) |
|---|---|---|
| §1 operator-sector primitive (the (C) condition) | the SPD (C) inner-product sector condition, stated exactly | `01-aat-core/src/result-certificate-existence.md` lines 19–37, **status: exact** |
| §3 unifying theorem (Banach/Lyapunov + perturbation) | the Lyapunov-equivalence (1⇔2⇔3) + R0/R1/R2 strength ladder + full derivation | `result-certificate-existence.md` lines 29–61 |
| §4 α/β → operator-family recast (the spike's own "load-bearing" payoff) | the five sub-scope-α classes named as proximal / firmly-nonexpansive / cocoercive / strongly-monotone-gradient / linear-PD operator families | `deriv-sector-condition.md` Grounding paragraphs, explicitly cited from `result-sector-persistence-template.md:74` |
| §5 closure results + monotone-operator lineage | Rockafellar §24 / Bauschke-Combettes §§22–28; closure apparatus; the honest limits incl. Λ-doesn't-fit | `result-sector-persistence-template.md:70–74` |
| §9/§11 plural no-go (Λ not an endomorphism; identifiability-floor orthogonal; substance-vs-typography) | "the three obstructions are distinct — the plurality is the content" (Helmholtz / Sylvester / Mori–Zwanzig, each invariant under the others' freedoms) | `disc-stability-certificate.md` lines 52–62, 70, 76, 80 |

The successor also landed `result-certificate-existence.md` (`status:
exact`) and `disc-stability-certificate.md` (`discussion-grade`) as canon;
CHANGELOG 2026-05-14 carries the full cycle narrative with commit hashes
(`d46671e`, `b599c4a`, `98e1bb2`, `1f70a32`, `ff171f4`, `06ab601`). The
**plural no-go is canonized correctly** — it lives present-tense in
`disc-stability-certificate.md` ("Why the plurality of obstructions is a
feature"), not exiled to archaeology. This is the audit-routing §6
corrected-ghost discipline done right: the no-go *is* canon (5A), only the
project-autobiography is in CHANGELOG/Working-Notes.

**Nothing of value lives only in this spike.** The math is in canon, the
no-go is canon, and the spike's own verdict was honestly *exceeded* (not
softened) by the successor. The spike is now a pure reasoning-trail
predecessor.

#### Recommended routing

- **Parent action: `git mv spikes/spike-operator-sector-unification.md
  spikes/.integrated/`.** Safe-mechanical; the directory-label truth-claim
  ("load-bearing content present in canon") is satisfied and verified
  forward per `spike-routing.md` §5.
- **INDEX reconciliation (parent):** the line-127 "PENDING REVIEW" row and
  the line-64 "predecessor" reference are both stale — the predecessor is
  fully absorbed *and* its content verified, not merely "reviewed". Reconcile
  to `integrated-filed`. (Convenience-record correction, not a truth change.)
- **Landing-scope:** none. No landing needed — already landed (heavier and
  better than the spike proposed) by the 2026-05-14 successor cycle.

#### One flagged adjacency (not in my slice — surfacing, not actioning)

The sibling `spikes/spike-update-operator-sector.md` (top level, 46 KB,
INDEX line 120 "PENDING REVIEW", target `#update-operator-sector`) is
**not** in my slice and its disposition is genuinely different — I checked
and there is **no `update-operator` segment in `src/`**; only a
`deriv-fisher-whitened-update-rule.md` exists, and the `O-A2'`/`α_op`
markers do not appear in canon outside `deriv-sector-condition.md`. That
spike looks like a live `orphaned`-suspect (its specific O-A2' closed-form
α_op + log-additive sequential composition may not be in canon), and the
2026-05-14 CHANGELOG explicitly *decoupled* the Tier-2 backlog (incl.
update-operator) as "(γ)-hybrid triage, each lands at its own INDEX-stated
target". Routing it on the assumption "the operator family is done" would
be the exact label-trust failure this cycle exists to catch. Flag for a
fan-out agent's slice; do not fold into this one.

---

## Spike 2 — `spike-c2-star-to-integrate.md`

### Disposition: `live-or-open` (cross-repo, externally-blocked) — **NOT** `orphaned`, **NOT** auto-landed this cycle. Recommend Joseph-adjudicated.

This is the harder one and it is where I hit a genuine frame edge (see
Frame-diagnostic below).

#### What the spike is

A **scoping document**, by its own explicit terms: *"This spike does **not**
commit to substrate landing. It records what *would need to land* if the
paper's (C2★) framing survives review and is judged substrate-worthy. If
the paper retreats to a weaker claim, this spike documents what was
considered."* It is a cross-pollination spike whose source of truth is the
AIES 2026 paper at `~/src/behavioral-floor/` (the formal proof M1–M4 and
the four "Push attempts" live at
`~/src/behavioral-floor/spikes/spike-c2-star-formalization.md`, verified to
exist, 22 KB, 2026-05-14).

#### Liveness assessment (step-zero — `spike-routing.md` §1)

The tracker pre-flags this as a *liveness-check, fail-safe to hands-off*
(Group LIVE, "INDEX 2026-05-14 IN FLIGHT"). Signals:

- INDEX status (line 76): **"IN FLIGHT — scoping not yet acted on …
  Pending Joseph's promotion-routing call and the AIES paper's own
  settling."** That is an explicit open, non-terminal verdict naming *two*
  external gates (Joseph's call; the paper's review settling).
- The spike's content-state is **not** "completed, result real" (the
  `orphaned` predicate). The result it would carry is *owned by another
  repo's paper that is still in review*. Its M1–M4 proof is not even in
  this spike — it is in `~/src/behavioral-floor/`.
- `spike-routing.md` §1: "when genuinely unsure, treat as live — the cost
  of excluding a settled spike for one cycle is a re-look, the cost of
  disturbing a live one is real."

Verdict: **live-or-open / externally-blocked.** It stays in `spikes/`. Its
INDEX status already correctly reflects open/blocked. Not moved, not landed.

#### The real content question (and why it is genuinely orphaned-*adjacent*, not closed)

Distinct from the file's disposition: the spike documents a **real gap in
canon** that strengthen-first should not let slide silently. First-hand
verified: `der-loop-interventional-access.md:76` still carries *only* the
original cross-reference **assertion** — *"Goal-conditioned LLM policies
violate (C2) by construction"* — which is precisely the
assertion-not-a-derivation gap the spike's §"The gap" names. The (C2★)
operationalizable strengthening (the GC1/GC2/GC3 condition, the proposed
`#disc-identifiability-floor` Instance 3, the Mode-3) is **nowhere in
canon** (grep-verified across `01-aat-core/src`, `03-llm-core/src`,
`02-tst-core/src`).

So there *is* a live truth-gap. But — and this is the strengthen-first
discipline applied correctly, not dodged — the gap's resolution is **not a
spike-routing landing**. It is:

1. **Externally owned.** The strengthening (assertion → derivation) is the
   AIES paper's central novel move; the M1–M4 proof lives in
   `behavioral-floor`, in review. Landing it into AAT canon *now* would
   import an unsettled cross-repo result — the inverse of the
   primary-source discipline.
2. **A promotion-level decision Joseph explicitly reserved.** The spike's
   §"Outstanding questions" lists four unsettled choices (naming;
   promotion-level i/ii/iii/iv; quantitative scope; Class-2 treatment),
   and the INDEX says "Pending Joseph's promotion-routing call." This is
   structurally the `#disc-identifiability-floor`-Instance-3 /
   meta-segment-architecture kind of call that the project's own pattern
   (cf. the M4 §5.1 and the operator-family spine decisions) routes to
   Joseph, not to an adjudicating agent.

This is **not** the strengthen-first reflex being suppressed by
"externally blocked". The strengthening attempt *is already running* — in
`behavioral-floor`, with M1–M4 + four push-attempts. Spike-routing's job
here is to route the spike to its honest home (live/blocked) and surface
the canon-gap + the cross-repo coupling to Joseph, **not** to either
(a) land an unsettled result or (b) silently mark the spike done while
`der-loop-interventional-access:76` still only asserts what the paper
derives.

#### Recommended routing

- **Disposition: `live-or-open`.** Stays in `spikes/`. INDEX status
  unchanged (already correctly "IN FLIGHT — pending Joseph + paper
  settling"). **No `git mv`. No canon landing this cycle.**
- **Surface to Joseph (dir-spike-gold-gate-style batch item, even though
  it is a file-spike — see Frame-diagnostic):** the canon-gap is real and
  worth his eyes — `der-loop-interventional-access:76` currently *asserts*
  the (C2) violation that the AIES paper *derives* as (C2★). Decision he
  owns: (a) when behavioral-floor settles, who lands (C2★) into AAT and at
  what promotion-level (the spike's i/ii/iii/iv); (b) whether an interim
  honesty-touch to `:76` is warranted — softening the bare "by
  construction" assertion to flag it as the cross-paper bridge under
  derivation — *or* whether that is itself a premature soften that
  strengthen-first forbids until the paper settles. I lean: **no interim
  edit** — `:76` is a Working-Notes cross-reference, not a Formal/Status
  claim, and it points at a *paper that is deriving exactly this*; the
  honest move is to let the strengthening land whole, not to soften a
  pointer. But this is a judgment call inside a reserved-for-Joseph zone,
  so I surface rather than recommend-with-confidence.
- **Landing-scope (when unblocked):** *heavy* — touches
  `#der-loop-interventional-access` (new sub-section), a candidate new
  `#disc-identifiability-floor` Instance 3 + Mode 3, and a
  `#der-directed-separation` Working Note; cross-repo provenance; a CHANGELOG
  cross-substrate entry. This is integration-plan + PRACTICA-surfacing
  territory (`spike-routing.md` §4, audit-routing §4.3/§4.4), authored
  deliberately by whoever holds the behavioral-floor context — explicitly
  *not* an auto-land.

---

## Cross-cutting note for the parent

Both spikes confirm the tracker's central hard-won lesson empirically:
**the INDEX label was wrong/stale in both cases**, in opposite directions.
For spike 1 the label *understated* status ("PENDING REVIEW" / "predecessor"
when it is fully absorbed-and-verified, and self-contradictorily filed). For
spike 2 the label was *accurate* ("IN FLIGHT") but only because it encodes
an external block, not a content judgment. Neither was decidable from the
label; both required first-hand `src/` reads + the cross-repo check. The
decisive-test discipline earned its keep on a 2-spike sample.
