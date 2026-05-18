# SPIKE-WORKING-471639 — Adjudication (S2: operator-family coupled cluster)

Cycle: spike-routing 2026-05-17. Adjudicator: S2 fan-out agent (independent
confirmer for spike 1; fresh adjudicator for spike 2).
Slice: `spikes/spike-operator-sector-unification.md` (confirm/refute pilot
023198's `integrated-misfiled`), `spikes/spike-update-operator-sector.md`
(fresh adjudication; pilot-flagged `orphaned`-suspect).

**Report only — no moves/edits/commits. Routing actions are the parent's.**
Independent-verify gate (audit-routing §8): every content-in-`src/` claim
below is first-hand `grep`/`Read`/`git`-verified and the loci are named so
the parent can re-check without trusting this summary. I am **not** the
pilot; I opened every named locus myself and re-derived the call rather than
relaying 023198's summary (a confirm that trusts the summary is the exact
failure this gate exists to catch).

---

## Spike 1 — `spike-operator-sector-unification.md`

### Verdict: **CONFIRM pilot 023198. `integrated-misfiled`** → parent `git mv` to `spikes/.integrated/` (safe-mechanical).

Completion-state **(B) strengthened past the claim** (audit-routing §3): the
C1 spike's own honest verdict was "2-instance-plus-1-consequence, DO NOT
elevate unless O-BP10 surfaces at segment level" (§§9, 11, 11-tier-table).
That "unless" gate was taken as a **strengthening target** by the successor
directory spike `spikes/.integrated/spike-operator-family-unification/` (6
files, archived 2026-05-14), which pushed per Joseph's "push until a
revealing no-go or the unifying mechanism" and landed strictly stronger
content as canon. The pilot's account holds in full; I re-verified every
load-bearing claim independently.

#### Content-in-canon verification (first-hand, not the pilot's summary, not the INDEX label)

| C1 spike load-bearing content | Canon locus | Verified how |
|---|---|---|
| §1 operator-sector primitive — the (C) SPD inner-product sector condition | `01-aat-core/src/result-certificate-existence.md:19-37`, **`status: exact`** | `Read` full file: (C) condition stated at L21-23; 1⇔2⇔3 Lyapunov equivalence L29-37 |
| §3 unifying theorem (Banach/Lyapunov + perturbation) + the strength ladder | `result-certificate-existence.md:40-61` | `Read`: R0/R1/R2 strictly-ordered ladder table L45-51; full derivation L53-61 |
| §4 α/β → operator-family recast (**the spike's self-identified "load-bearing" payoff**) | `01-aat-core/src/deriv-sector-condition.md:84-94` | `grep`+read: five sub-scope-α families named (proximal/firmly-nonexpansive, cocoercive, strongly-monotone-gradient, natural-gradient-Fisher, linear-PD); Rockafellar §24 / Bauschke-Combettes §§22-28 lineage; β-list; honest-limits paragraph (Λ doesn't fit, identifiability-floor orthogonal) |
| §5 closure results + monotone-operator lineage + honest limits | `result-sector-persistence-template.md:70-74` | `sed` read L66-80: full "External mathematical lineage" subsection, specialization-not-generalization framing, Λ-doesn't-fit + three-of-five-metric-cases-theorem-imported + identifiability-orthogonal limits |
| §9/§11 plural no-go (the three obstructions distinct; each invariant under the others' freedoms) | `01-aat-core/src/disc-stability-certificate.md:52-62`, also 80, 92 | `Read` full file: Helmholtz–Hodge / Sylvester / Mori–Zwanzig as **irreducibly distinct**, "the plurality is the content," mutual-invariance stated as structural fact |

The successor also landed `result-certificate-existence.md` (`status:
exact`) and `disc-stability-certificate.md` (`discussion-grade`) as the
two-segment certificate spine. **The plural no-go is canonized correctly per
the audit-routing §6 corrected-ghost discipline**: it lives present-tense in
`disc-stability-certificate.md` ("Why the plurality of obstructions is a
feature," L80) as canon (5A) — *not* exiled to archaeology, and *not* in
project-autobiographical voice in the body (the "previously held / not a
weakening" history lives only in CHANGELOG and the segments' Working Notes,
L98 / L105). This is the over-rotation-corrected discipline done right.

#### Git provenance (the sharpest decisive-test instrument here — spike-routing §7 Refinement 2)

Pickaxe on the result-strings is **sweep-confounded** (the AAD→AAT rename
`9745397` rewrote them, so `git log -S` returns only the rename — recency
is poisoned exactly as the SOP warns). Provenance via the *commit chain*
is clean and decisive:

- `git log` on `result-certificate-existence.md` shows the landing chain in
  order: `303112e` *SPIKE: operator-family unification — the real-deal C1
  push, verdict reached* → `d46671e` *FINDINGS: identifiability-floor
  irreducibility is Sylvester's law* → `b599c4a` *SPINE: land
  #disc-stability-certificate* → `98e1bb2` *SPINE: split anchor into
  #result-certificate-existence* → `ff171f4` *O-BP10 landed; archive
  absorbed spike* → `06ab601` *DISCIPLINE: .integrated/ spikes absorbed —
  remove live Working-Note refs*. This is the 2026-05-14 successor cycle,
  exactly as CHANGELOG 2026-05-14 (L54-77) and INDEX L62-68 narrate, with
  commit hashes matching.
- `git log --all -- 'spikes/.integrated/spike-operator-sector-unification.md'`
  returns **empty**: the C1 spike file has *never* been committed under
  `.integrated/`. It was added by `1f68320` ("Gap A/B cycle") and has lived
  at `spikes/` top level the entire time. **This is the misfiling.** The
  INDEX line-64 "predecessor: `spikes/.integrated/spike-operator-sector-unification.md`"
  reference is therefore stale/wrong in a specific way: the absorbed
  predecessor is the **directory** spike `spike-operator-family-unification/`,
  not this file. The pilot caught this correctly.
- `grep "operator-sector primitive"` across all three component `src/` trees
  returns only `result-sector-persistence-template.md` and
  `deriv-sector-condition.md` — i.e. canon carries the *operator-family
  lineage* (the spike's payoff) but **not** the spike's tentative primitive
  verbatim. Canon adopted the stronger certificate framing instead. This is
  integration-is-replacement done correctly: the spike's content is not
  duplicated as a softened co-resident; it was *exceeded* and replaced.

**Nothing of value lives only in this spike.** The math is in canon, the
plural no-go is canon (present-tense, correctly de-autobiographized), and
the spike's own honest verdict was *exceeded* (state B), not softened. The
spike is now a pure reasoning-trail predecessor.

#### Recommended routing

- **Parent action: `git mv spikes/spike-operator-sector-unification.md
  spikes/.integrated/`.** Safe-mechanical. The `.integrated/` truth-claim
  ("load-bearing content present in canon") is satisfied and forward-verified
  per spike-routing §5.
- **INDEX reconciliation (parent, cycle close):** two stale references —
  line-127 "PENDING REVIEW" row and the line-64 "predecessor:
  `.integrated/spike-operator-sector-unification.md`" pointer (which should
  name the `spike-operator-family-unification/` *directory* as the absorbed
  predecessor, not this file). Reconcile this file's row to
  `integrated-filed`. Convenience-record correction, not a truth change.
- **Landing-scope: none.** Already landed — heavier and better than the
  spike proposed — by the 2026-05-14 successor cycle.

#### Confidence and the one residual the parent should eyeball

High confidence. The only thing I cannot fully close from inside this slice:
the INDEX line-64 "predecessor" pointer is *doubly* off — wrong path *and*
arguably wrong referent (it points at this file when the genuine absorbed
predecessor of the spine is the directory spike). That is an INDEX-hygiene
fix, not a truth-status question, and it does not change the `git mv`
disposition. Flagging it so the cycle-close INDEX reconciliation doesn't
just flip "PENDING REVIEW → integrated-filed" and leave the mis-pointed
"predecessor" line propagating a wrong cross-reference.

---

## Spike 2 — `spike-update-operator-sector.md`

### Verdict: **`orphaned`** — completed, result real (a genuine strengthening result *and* a sharp confirmed no-go), **not in canon**, only loosely backlinked as an open TODO/PROPOSALS target. The pilot's `orphaned`-suspect flag is **confirmed**. Landing is **real theory work, not mechanical** — and it is *tractable* (one α-list refresh + one no-go cross-ref), but a judgment call on landing form sits inside it; see below.

This is where the failure this whole cycle exists to catch is actually
present: a real, honestly-scoped strengthening result (the operator-level
sector condition on the log-odds credit-assignment iteration) **lives only
in the spike**.

#### What the spike is, and that its result is real

It recasts the log-odds credit-assignment update as a discrete dynamical
system and derives an A2'-analog operator sector condition `(O-A2')` on the
*update operator itself* (not the underlying plant), with:

- a closed-form sector constant
  `α_op^comp = min_k [1/(n_k+1)]·ι_k·(J_k²/‖J‖²)·σ'(λ*_k)` (§2.3), every
  factor structurally tied to an existing AAT quantity;
- an α-op/β-op sub-scope partition that *inherits structurally* from
  `#der-gain-sector-bridge`'s α/β (§3) — Bayesian/exp-family satisfy
  `(O-A2')` by construction; β fails unless correction-rotation is bounded;
- a discrete contraction theorem `(O-DA.1)` whose step-size condition
  **lifts structurally** (reduces to `α_op > 1/128`, always met in the
  identifiable regime) rather than being a separate tuning parameter (§5);
- parallel (weakest-link) and sequential (log-additive) composition sector
  constants (§6);
- a **sharp confirmed no-go** (§4.3): under unobservable-L1' common cause
  the marginalized Fisher is rank-1, so no sector-positive operator exists —
  `(O-A2')` breaks *structurally*, not gracefully. The spike correctly
  characterizes this as confirming `#disc-identifiability-floor` Instance 2
  *at the operator layer* (**not a new floor instance** — important: this is
  the integration-is-replacement-aware reading, not an over-claim of a 4th
  instance).

The spike's own §9.3/§9.4 self-assessment is honest: max attainable is
*conditional* (monotone-AND + regime-A + small-R linearization + the
evidential-additivity axiom), and it explicitly frames its §7 break-test
(four structural failure modes) as the honest scope boundary. This is
already strengthen-first done *inside* the spike — there is no soften to
resist; the spike took an implicit fact ("the log-odds update contracts
toward truth") and made it an operator-level sector condition with a
closed-form constant and a sharp break-test. The failure mode in play is the
*landing* failure, not a soften failure.

#### Strengthen-first check (the brief makes this non-optional — done, with a finding)

Per audit-routing §2 / the brief's counterintuitive reflex, before agreeing
spike-2 needs only a routine landing I checked whether a stronger statement
is available — specifically whether the **certificate spine that resolved
spike-1 already subsumes `(O-A2')`** (which would make spike-2
`subsumed-by-later-work`, not `orphaned`). First-hand:

- `grep` for `edge.update | credit.assignment | log.odds | T_edge | update
  operator` in `result-certificate-existence.md` and
  `disc-stability-certificate.md` → **empty**. The certificate spine
  instantiates the certificate on the *mismatch/error dynamics*; it does
  **not** instantiate the *credit-assignment edge-update operator*.
- The `deriv-sector-condition.md` α-family list (L86) names "Optimal
  Bayesian updates (Kalman, conjugate, exponential family) ≡ proximal /
  firmly nonexpansive" generically, but **not** the operator-level
  credit-assignment iteration with its closed-form `α_op` and the
  step-size-lifts-structurally result.

**Finding: `(O-A2')` is a genuine *additional instance* of the certificate
machinery (the operator-layer credit-assignment iteration), not redundant
with and not subsumed by the spike-1 successor.** So this is **not**
`subsumed-by-later-work`. It is `orphaned`. The strengthen-first reflex,
applied, *confirms* the orphan rather than dissolving it — the strengthening
already happened (in the spike) and the result is real and unsubsumed; what
is missing is the landing.

#### Content-in-canon verification (the decisive test, first-hand) — confirms NOT integrated

- **No `#update-operator-sector` / `#update-operator` segment exists**
  (`ls 01-aat-core/src/` filtered — none).
- `grep` for the spike's load-bearing names `(O-A2')`, `(O-DA2')`,
  `(O-DA.1)`, `α_op`, "operator-level sector" across `01-aat-core/src/`,
  `03-llm-core/src/`, `02-tst-core/src/` → **no hits for the spike's
  results**. The only hits are *unrelated*:
  `deriv-fisher-whitened-update-rule.md` (a distinct, narrower segment that
  landed from a *different* spike — `spike-fisher-whitened-update.md`, per
  its Working Notes L115 — addressing the Fisher-whitened *correction
  direction* under L1'/L2, topically adjacent to spike-2's §4 but **not**
  spike-2's central `(O-A2')`/`α_op`/`(O-DA.1)`/composition deliverable),
  and `result-unity-closure-mapping`/`def-unity-dimensions` using "update
  operator" generically for the structural-unity dimension.
- `disc-credit-assignment-boundary.md` — the spike's own §10.2 primary
  cross-ref-hook target — carries **no** `(O-A2')` / operator-level /
  Banach-contraction reference (grep empty). The spike's intended landing
  hook is unhooked.
- **Evidence hierarchy (spike-routing §7):** open `[ ]` backlinks exist —
  `TODO.md:447` (`spike-update-operator-sector` ... Tier 2),
  `PROPOSALS.md:249` and `PROPOSALS.md:266(iii)` ("PID A2' and
  update-operator-sector subsumed as α-list refreshes in
  `#deriv-sector-condition`"). Per §7, an open `[ ]` backlink is
  **sufficient evidence for NOT-integrated**. No integration-plan file
  exists. CHANGELOG 2026-05-14 L73 explicitly **decoupled** it: the SP-22
  resolution closed the *architectural* question (operator-sector is the
  cone interior, not a meta-pattern peer) but routed the Tier-2 backlog
  including `update-operator-sector` as **(γ)-hybrid triage — "each lands at
  its own INDEX-stated target, no longer gated"**. Decoupled-and-still-to-
  author is exactly `orphaned`, not `integrated`.

Triangulated three independent ways (no segment; no result-string in `src/`;
open backlink + explicit CHANGELOG decoupling) — the conclusion is not
label-trust, it is the decisive first-hand test.

#### Landing assessment: tractable, with one reserved-judgment seam

Per spike-routing §4, the adjudicator records the tractable-vs-heavy read;
the parent decides auto-land vs queue.

**My read: tractable, but it carries one form-decision the parent (or
Joseph) should make rather than an agent auto-landing.** Concretely, the
spike's §8 + PROPOSALS §266(iii) already converge on the landing shape:

1. **The α-list refresh (tractable, clear).** `(O-A2')`'s α-op/β-op
   partition lands as an *operator-layer α-list refresh in
   `#deriv-sector-condition`* — parallel to, and alongside, the
   already-landed mismatch-layer operator-family recast at
   `deriv-sector-condition.md:84-94`. This is the PROPOSALS §266(iii)
   route ("PID A2' and update-operator-sector subsumed as α-list
   refreshes"). It touches one segment's Grounding/Discussion region; it is
   the same *kind* of edit that already landed for the spike-1 successor's
   α-recast. Tractable.

2. **The no-go cross-ref (tractable, clear, and the part that must not be
   dropped).** Spike-2 §4.3's unobservable-L1' Cramér-Rao rank-1 break is a
   real no-go that **confirms `#disc-identifiability-floor` Instance 2 at
   the operator layer**. Per audit-routing §4/§6 a no-go is present-tense
   canonical truth, not archaeology — but here the spike is *honest that it
   is not a new instance*, so the correct landing is a **one-line
   confirming cross-ref in `#disc-identifiability-floor`** (Instance 2 also
   manifests at the credit-assignment-operator layer; the operator inherits
   the floor), not a new appendix. Proportionality (audit-routing §5B):
   small and local, a full appendix would be ceremony. This is the part
   most at risk of being lost if only the α-list refresh lands and the
   no-go is treated as "already covered by Instance 2" — it *is* covered as
   a *floor*, but the operator-layer *manifestation* is the spike's real
   added content and should be the cross-ref's substance.

3. **The reserved seam (why this is not pure auto-land).** The spike's §8
   offers three landing forms — (8.1) a new `#update-operator-sector`
   appendix, (8.2) a §7 extension of `#deriv-discrete-sector-condition`,
   (8.3) a unification segment. PROPOSALS §266(iii) picks the *fourth*
   option (α-list subsumption into `#deriv-sector-condition`), which post-
   dates the spike's §8 and reflects the SP-22 resolution (operator-sector
   is cone-interior, not a peer pattern). The spike's §8 self-recommendation
   (new appendix) is therefore *superseded by the SP-22 architectural
   decision* — but whether the final form is "α-list refresh in
   `#deriv-sector-condition`" vs. "short §7 in
   `#deriv-discrete-sector-condition`" vs. both is a placement judgment that
   interacts with how the mismatch-layer recast already sits in
   `#deriv-sector-condition`. This is not a framework-identity / cross-repo
   reserved call (it is *not* the spike-routing §6 Joseph-batch kind), but
   it is a "which segment does the operator-layer α-list live in, given the
   mismatch-layer one is already there" call that benefits from the parent's
   whole-corpus view rather than an agent picking unilaterally. **Net: land
   it this cycle (it is tractable and the cycle is not the taxonomy —
   spike-routing §4), but the parent makes the §266(iii)-vs-§8.2 placement
   call; do not auto-execute the spike's own superseded §8.1
   self-recommendation.**

Landing touch estimate (for the parent's auto-land/queue split): **one
segment edited substantively** (`#deriv-sector-condition` — an
operator-layer α-op/β-op sub-list paragraph, mirroring the existing
mismatch-layer recast), **one one-line cross-ref** added to
`#disc-identifiability-floor` (Instance 2 manifests at the operator layer),
and optionally **one cross-ref stub** in `#disc-credit-assignment-boundary`
(its default signal function is now an `(O-A2')`-satisfying operator — the
spike's §10.2 hook). No new appendix, no cascade, no new segment. This is
toward the tractable end — comparable in size to the spike-1 successor's
α-recast that already landed — but it is *substantive segment authoring*,
not a `git mv`. By spike-routing §4 it is auto-landable this cycle; I flag
the §266(iii)-vs-§8.2 placement as the one judgment seam the parent should
own.

#### Recommended routing

- **Disposition: `orphaned`.** Real strengthening result + sharp confirmed
  no-go, not in canon, only open-backlinked. Stays in `spikes/` until the
  landing lands; **not** `git mv` to `.integrated/` until content is
  verified in `src/` (spike-routing §5 forward guarantee).
- **Landing: tractable, this cycle** (spike-routing §4, "the cycle is not
  the taxonomy") — α-op/β-op sub-list refresh into `#deriv-sector-condition`
  + Instance-2-at-operator-layer cross-ref into
  `#disc-identifiability-floor` + (optional) `(O-A2')` hook into
  `#disc-credit-assignment-boundary`. **Parent owns the placement-form call**
  (PROPOSALS §266(iii) α-list-subsumption vs. the spike's superseded §8.1
  new-appendix self-rec — the architectural decision SP-22 already made the
  call: subsumption, not a new peer segment; the residual is *which*
  segment(s) host it). Not a Joseph-reserved framework-identity call; a
  parent whole-corpus-view call.
- **On commit:** close `TODO.md:447` and the `PROPOSALS.md:249`/`§266(iii)`
  open items; CHANGELOG entry records the (γ)-hybrid Tier-2 item landing at
  its INDEX-stated target (the decoupling at CHANGELOG L73 anticipated
  exactly this). Then the spike is `git mv` → `.integrated/` and INDEX
  L120 "PENDING REVIEW" reconciled.
- **One thing not to lose:** the no-go (§4.3). If the landing reduces to
  "just the α-list refresh" and the operator-layer manifestation of the
  identifiability floor is dropped as "Instance 2 already covers it," that
  is the integration-is-replacement failure in its subtle form — the floor
  is covered, but the *operator-layer manifestation* is spike-2's real
  added truth and must reach `#disc-identifiability-floor` as present-tense
  canon (one line is enough; audit-routing §5B proportionality), not stay
  spike-only.

---

## Cross-cutting note for the parent

1. **The slice's central lesson, re-confirmed empirically and in opposite
   directions** (matches the pilot's cross-cutting note from a disjoint
   2-spike sample — convergence is itself evidence the lesson is in the
   corpus, not in one agent's head): the INDEX label was misleading in both
   cases. Spike 1: label *understated* and was self-contradictory
   ("PENDING REVIEW" + a "predecessor" pointer to a `.integrated/` path the
   file never occupied) when the content is fully absorbed-and-verified.
   Spike 2: label "PENDING REVIEW" read as benign-pending when it is a
   genuine *orphan with real unsubsumed content*. Neither was decidable
   from the label; both required first-hand `src/` reads + git provenance +
   the strengthen-first subsumption check.

2. **Git *provenance* (commit chain) was the sharpest instrument for
   spike 1**, exactly as spike-routing §7 Refinement 2 predicts — and the
   pickaxe `-S` was confirmed sweep-poisoned (returned only the AAD→AAT
   rename). Recency useless; the *commit-message chain*
   (`303112e`→`06ab601`) decisive. The `git log --all --
   '.integrated/<file>'`-returns-empty test cleanly proved the file never
   lived under `.integrated/`, which is what makes "misfiled" the precise
   word and exposes the mis-pointed INDEX "predecessor" line.

3. **The sibling-coupling partition decision (pilot Refinement 1 → tracker)
   was load-bearing here.** These two spikes *are* the operator family;
   adjudicating spike 1 in isolation would have made it tempting to wave
   spike 2 through as "the operator family is done — the certificate spine
   landed." It is **not**: spike 2's `(O-A2')` is a genuine *additional
   instance* the certificate spine does not instantiate (verified by grep,
   not assumed). Keeping the coupled pair in one slice is what surfaced
   that the strengthen-first subsumption check was *required*, not
   optional, before calling spike 2's home.

4. **No frame defect to fold this cycle.** The S2 brief and the governing
   docs were sufficient and correctly predicted both the
   provenance-as-sharpest-instrument move and the strengthen-first-confirms-
   the-orphan outcome. One observation, not a defect: the brief's reflex
   ("a spike that looks like it wants softening gets strengthen-first") has
   a less-obvious dual that the docs *do* cover but is worth foregrounding
   for future fan-out agents — *a spike that already did its own
   strengthen-first honestly and landed at `conditional` is still an
   orphan-with-real-content if the result never reached canon*; the
   strengthen-first check there is not "should we soften?" but "did a later
   result subsume this?" (a `subsumed-by-later-work`-vs-`orphaned`
   discriminator). Spike 2 is the worked example. This is already implied
   by audit-routing §8's enum (`subsumed-by-later-work` "name the
   subsumer") + the strengthen-first reflex; surfacing it as a named
   discriminator in a future Refinement would help — flagging, not folding
   (the parent owns whether it earns a scar).
