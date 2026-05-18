# SPIKE-WORKING-417303 — Adjudication: S1 (the 2026-04-24 strengthening cycle)

*Adjudicator: fan-out agent, slice S1. Read/report-only — no moves, edits, commits,
or segment changes performed. All content-in-canon claims below are first-hand-verified
against `01-aat-core/src/` with named loci so a confirmer (≠ adjudicator) can re-check
without re-deriving. Decisive test per `doc/spike-routing.md` §2/§7: load-bearing
content present in a `src/` segment, verified first-hand — INDEX label is a hypothesis.*

Slice (6 file-spikes, all `spikes/*-2026-04-24.md`):

1. `spike-bridge-lemma-nonlinear-strengthening-2026-04-24.md`
2. `spike-fenchel-bregman-reframe-additive-coordinate-forcing-2026-04-24.md`
3. `spike-identifiability-floor-instance-triage-2026-04-24.md`
4. `spike-kl-to-state-distance-template-extraction-2026-04-24.md`
5. `spike-neutral-drift-endogenous-coupling-strengthening-2026-04-24.md`
6. `spike-rho-additive-variance-strengthening-2026-04-24.md`

---

## 0. The headline, before the per-spike detail

The INDEX cycle header calls this cycle **"TIER 1 LANDED"** — but the *per-spike status
column the header itself points to* already says, accurately, that only a fraction
landed Tier 1 and the rest are Tier-2/3 (i.e. **not landed**). So the slice's hypothesis
("S1 = TIER-1-LANDED, verify-in-canon") is, on its own INDEX text, wrong as a uniform
label. The real question per spike is binary: *is this spike's load-bearing content in
`src/`?* The answer splits the six cleanly:

| Spike | Disposition | One-line reason |
|---|---|---|
| bridge-lemma | **`integrated-misfiled`** (§7.1 only) **+ residual `orphaned` (§7.2)** | §7.1 minimal fully in canon, first-hand verified; §7.2 passivity route is real, promotable, **nowhere in `src/`**; §7.3 honest defer |
| fenchel-bregman | **`integrated-misfiled`** | Both halves landed — §6.3 *and* the full meta-reframe — INDEX is *understated* (says reframe is unlanded Tier-3; it is canon) |
| identifiability-floor-triage | **`orphaned` (analytic judgment) — Joseph-reserved** | A *routing-recommendation* spike; its recommendation was **partly not followed and partly inverted in canon**; the judgment lives only in the spike |
| kl-to-state-distance | **`live-or-open`** (architectural proposal, clients not yet materialized) | Explicitly contingent recommendation; gate (`#deriv-observation-ambiguity-bias-bound`) landed but the template did not, by design |
| neutral-drift | **mostly `integrated-filed`-adjacent + one `orphaned` strand** | Conclusion-level content absorbed via the sibling `spike-neutral-drift-lyapunov`; the §A cross-covariance γ-estimator and §10.1 fourth-floor-instance are **not** in canon |
| rho-additive-variance | **`orphaned` — real derived theorem + real no-go, NOT in canon** | The (AV) theorem, the (S1)–(S4) conditions, the no-go, the sub-regime catalog — none landed; `#internal-external-decomposition` is still `robust-qualitative` with none of this content. **This is the canonical failure the cycle exists to catch.** |

The two that need real attention are **rho-additive-variance** (orphaned math + orphaned
no-go) and **identifiability-floor-triage** (orphaned routing judgment that was
*diverged from* in canon, in a way that is itself a present-truth question). The
bridge-lemma §7.2 passivity strand is a third, smaller orphan.

A sibling-coupling flag (per `doc/spike-routing.md` §6 / tracker partition): three of
these six are tightly coupled to **`spike-bias-bound-constant-C-strengthening-2026-04-24`**
(already under `.integrated/`, *not in this slice*). It is the gate for kl-to-state-distance
and the source of what actually became Instance 4. I do **not** route it (flag-don't-route);
its disposition is sound (`#deriv-observation-ambiguity-bias-bound` is in `src/`,
first-hand verified) but the triage spike's verdict says the *use* it was put to
(promoting Candidate 3 to a floor instance) contradicts the triage's own
recommendation — see §3 below. That tension is the load-bearing thing in this slice
and is a Joseph-reserved call.

---

## 1. `spike-bridge-lemma-nonlinear-strengthening-2026-04-24.md`

**Completion-state:** (A) strengthened-to-claim for the cooperative-smooth half +
(C) two sharp no-gos (N1 Lipschitz floor; N2 adversarial three-obstruction). Honest
defers for the non-statistical-metric / adaptive-metric residuals. A genuinely strong
spike.

**Disposition: `integrated-misfiled` for the §7.1-minimal content; a residual
`orphaned` strand for §7.2 (passivity / Class-1-2-3 port-structure).** §7.3 (iISS
Tier-2M) is an honest, correctly-deferred Tier-3 — `live-or-open`-equivalent, not a
loss.

**§7.1 minimal — IN CANON, first-hand verified:**

- *DA2'-inc ≡ (CT2)-at-$M=I$ structural-transparency lift, Euclidean metric-α₁
  reclassified theorem-import → AAT-internally-derived:*
  `result-contraction-template.md` lines **75, 77, 83, 130, 132, 170, 176, 186, 188,
  197 (Rockafellar-Wets/Nesterov monotone-operator identity, named explicitly),
  212**; `der-gain-sector-bridge.md` and `form-composition-closure.md` carry the
  cross-side. This is *exactly* the spike's §3 content, landed with the spike's
  citation chain.
- *N1 non-smooth/rule-based Lipschitz-floor no-go:* `deriv-sector-condition.md:96`
  — present as *[Derived, status: exact scope-exit statement]*, with the spike's
  exact counterexample ($F(\delta)=\alpha\delta$ for $|\delta|<1$, $+\mathrm{sign}(\delta)$
  for $|\delta|\ge 1$, $f_c$ jumps by $\eta^\ast$) and the van der
  Schaft-Schumacher / Di Bernardo external apparatus. Textbook 5A/5B no-go landing
  done right.
- *N2 adversarial three-obstruction convergence:* `result-contraction-template.md`
  lines **144–152** (the three obstructions itemized: Slotine 2003 saddle-point;
  passivity-universality; Daskalakis 2018 last-iterate), **186, 201, 207**, plus a
  chapter-level surfacing at `impl-cooperative-adversarial.md:49`. Routed to
  `#deriv-strategic-composition` as the spike recommended.

Provenance note: `git log -S` lands on `9745397` (the AAD→AAT rename sweep) — that is
**recency, which is sweep-poisoned** (`doc/spike-routing.md` §7). The decisive evidence
is *content-present*, which is confirmed; corroborated by `git show --stat b76ee67`
("2026-04-24 pressure-point cycle: Tier 1 landing"), which touches exactly
`contraction-template`, `composition-closure`, `sector-condition-derivation`,
`loop-interventional-access`, `strategy-cost-regret-bound` + new `bias-bound-derivation`
— precisely the §7.1-minimal surface and no more.

**§7.2 passivity / dissipativity route — NOT in canon (the orphaned strand):**

- No `#dissipativity-template` segment exists (`ls 01-aat-core/src/` — absent).
- No Class-1/2/3 **port-structure / clean-ports / leaky-ports / Willems-storage**
  reading in `der-directed-separation.md` (grep: absent; the file's Class-1/2/3
  content is the *modularity/κ* reading, not the passivity-port reading).
- The only passivity mentions in canon (`impl-cooperative-adversarial.md:49`,
  `result-contraction-template.md`) are the **N2 negative** use
  ("passivity-universality *fails* for adversarial inputs") — i.e. the no-go, already
  counted. The **constructive** §7.2 result (heterogeneous Kalman + PID-on-positive-real-plant
  is $\mathcal L_2$-stable via Willems + Khalil Thm 6.4; the storage-function table;
  the Class-1/2/3 port reading of `#der-directed-separation`) is real, the spike rates
  it *promotion-ready / derived / textbook*, and it **lives only in this spike and in
  its predecessor `spike-passivity-composition.md`**. INDEX itself labels this "Tier 2"
  (not landed) — INDEX is *accurate* here.

  This is a genuine orphan: real math (it composes three textbook results — Willems
  1972 + Khalil 2002 Thm 6.4 + Anderson-Moore — into an AAT-relevant heterogeneous-
  composition closure, plus the novel Class-1/2/3 port-structure observation) that
  closes the *specific* Kalman+PID case Gemini's pressure point named, and is not in
  `src/`. **Tractability: moderate-heavy.** Per the spike's own §7.2: one new appendix
  (~200 lines) `#dissipativity-template` + two paragraph-scale edits
  (`#deriv-critical-mass-composition` Working Notes; `#der-directed-separation`
  Discussion port-structure reading). The math is done in the spike and in
  `spike-passivity-composition.md`; the work is segment-authoring, not derivation. It
  is **not** "tractable/clear auto-land" — it is a written-landing-plan + PRACTICA
  item per `doc/spike-routing.md` §4 (substantial segment-authoring).

**Recommended routing:**
- The §7.1 content is fully integrated → the file-spike's *primary* purpose is served;
  it is `integrated-misfiled` and can `git mv → .integrated/` **after** the §7.2 orphan
  is captured so it is not lost on the move (the spike is the only durable home of the
  port-structure observation, which is *novel*, not just textbook-composition).
- The §7.2 strand is `orphaned` and should get a written landing-plan
  (`spikes/spike-bridge-lemma-nonlinear-strengthening-2026-04-24-spike-integration-plan.md`
  or folded with the `spike-passivity-composition.md` landing, since they are the same
  result) surfaced in PRACTICA. **Sibling flag:** `spike-passivity-composition.md`
  (2026-04-22, *outside this slice*) is the actual primary home of the §7.2 math;
  this spike adds only the Class-1/2/3 port reading on top. They must land together
  or the port reading is double-orphaned. Flag-don't-route the sibling.

---

## 2. `spike-fenchel-bregman-reframe-additive-coordinate-forcing-2026-04-24.md`

**Completion-state:** (B) strengthened-past — the spike was asked whether Path 7's
duality observation should reframe `#additive-coordinate-forcing`; it produced a
sharper structural description than either Path 7 or the prior framing (Reframe A with
axiom-independence preserved), all content verified textbook-exact.

**Disposition: `integrated-misfiled`. INDEX is *understated* here — both halves
landed, not just §6.3.**

INDEX line 106 says: "Local identification LANDED Tier 1 (`#deriv-strategy-cost-regret-bound`
§6.3); **Full meta-segment reframe → Tier 3 architectural proposal**" — i.e. INDEX
claims the reframe did *not* land. First-hand check refutes this in the
**non-optimistic** direction (the rarer, more dangerous INDEX error — a *true*
landing recorded as un-landed, which would cause a real result to be re-litigated):

- *§6.3 Bregman-Fenchel dual-pair identification:* `deriv-strategy-cost-regret-bound.md`
  lines **180–196** — present as *[Derived (bregman-fenchel-dual-pair, exact;
  standard Legendre-Fenchel)]*, §6.3 heading verbatim ("Bregman-Fenchel
  identification: reverse-KL and log-odds as dual coordinates"), negative-entropy
  potential / log-partition conjugate / softmax / log-odds-ratio / reverse-KL Bregman
  identity, identification with `#deriv-edge-update-natural-parameter`, Amari-Nagaoka
  / Bregman 1967 citations. Exactly the spike's §1.
- *The full meta-segment reframe (Reframe A — "one geometric object / four
  layer-specific manifestations / Legendre-Fenchel geometry"):* **landed in
  `disc-additive-coordinate-forcing.md`**, lines **14–18** ("these four layers are
  layer-specific manifestations of a single geometric object: the exponential-family
  Legendre-Fenchel structure"), **22** (Amari-Nagaoka / Bregman / Rockafellar /
  Bauschke-Combettes), **32–50** (the four-manifestation table + "convergence across
  independent axioms is itself the meta-pattern's substance — not a byproduct to be
  compressed into a single axiom" — the spike's §7.2 axiom-independence guard,
  verbatim in spirit), **74** (IB reclassified as adjacent / imported provenance),
  **78** (the principled candidate-filter the spike's §8 designed), **84, 108**. This
  is the spike's §7.1/§7.3 reframe, *landed essentially in full*, including the
  spike's central "do not over-unify" guard.

So the spike is fully integrated (both the local identification and the architectural
reframe). The remaining spike-only items (Gaussian-case walkthrough §9.2; the
speculative second parallel meta-pattern for (AV) §8.1; PDF-verification of Amari-Nagaoka
theorem-number granularity §9.2) are **honest open follow-ons flagged in the spike's
own Working Notes**, not orphaned load-bearing content.

**Recommended routing:** `integrated-misfiled` → `git mv → .integrated/`.
**Independent-verify gate (required, `doc/audit-routing-instructions.md` §8):** the
load-bearing claim is "the full reframe landed in `disc-additive-coordinate-forcing.md`,
not just §6.3" — a confirmer ≠ me should open `disc-additive-coordinate-forcing.md:14-84`
and `deriv-strategy-cost-regret-bound.md:180-196` directly. **Also flag for the parent:
the INDEX row 106 is stale/understated and should be reconciled to "fully landed" at
cycle close** — leaving it saying "Tier 3 architectural proposal (unlanded)" invites a
future agent to re-open a closed, canonical result (a real cost, the inverse of the
usual optimistic-INDEX error).

---

## 3. `spike-identifiability-floor-instance-triage-2026-04-24.md`

**Completion-state:** This is **not a math spike** — it is a *routing/triage*
recommendation spike (its own line 3: "Research / analytic spike. Not canon. No
segment files modified."). Its load-bearing content is *judgment*: the five-element
test, the four-candidate verdicts, the subsumption structure, the layer taxonomy, the
bounded-capacity criterion. The "math lives in segments" rule does not apply (there is
no derived math here); the analog question per `doc/spike-routing.md` is whether the
*decision the spike reached* is reflected in canon or is orphaned.

**Disposition: `orphaned` — and specifically a Joseph-reserved decision, because
canon *diverged from* the spike's central recommendation, and reconciling that
divergence is a present-truth question about `#disc-identifiability-floor`, not a
filing question.** Per `doc/spike-routing.md` §6 (ratified axis: route any
reserved-decision spike, file or dir, to the Joseph batch — *route more to Joseph,
never auto-file a reserved-judgment call*).

What the spike recommended vs. what is in `disc-identifiability-floor.md` (first-hand,
the file as of today):

| Triage recommendation | Canon state (first-hand) | Verdict |
|---|---|---|
| **Candidate 2 (agent-internal architecture / Kalman-Ho) → genuine Instance 4, the *primary* (Priority-1) move; completes the 3-mode `#der-loop-interventional-access` chain** | **Absent.** No Kalman-Ho / agent-internal-architecture floor instance. `der-loop-interventional-access.md:62-68` has the Modes-of-deployment subsection with **Mode 1 + Mode 2 landed** and **Mode 3 (observer-on-agent-input) explicitly flagged "not promoted, under triage"** | Recommendation **not followed**; the spike's headline move is orphaned |
| **Candidate 3 (universal-$C$ / constant-C) → NOT a floor instance; redirect to `#deriv-observation-ambiguity-bias-bound` as a downstream theorem (fails E4: single escape)** | **Inverted.** `disc-identifiability-floor.md:92` = **Instance 4 — "Universal Information-to-Distance Constant under Non-(PI) Norms"** — i.e. Candidate 3 *did* land as a floor instance, the exact move the triage spike argued against | Canon **contradicts** the spike's reasoned verdict |
| Candidate 4 (mechanism-design) → genuine Instance 5 under broad reading | `disc-identifiability-floor.md:122` — present as **"Candidate fourth instance ... Open"**, *not* promoted to a full instance | Recommendation not (yet) followed; honestly held open |
| Candidate 1 (ρ-factorization) → sub-statement of Candidate 2 at disturbance-statistic projection, lands with `#rho-decomposition` | `#rho-decomposition` never landed (see §6 below); no sub-statement exists | Orphaned-with-its-parent |
| Three-mode `#der-loop-interventional-access` articulation (pattern real, mechanism semantically distinct per layer) | `der-loop-interventional-access.md:62-68` — **landed**, including the explicit "Mode 3 not promoted but the pattern-level regularity is worth naming" honesty | Recommendation **followed** (this part is canon, done well) |

The net: **the triage spike's actual analytic conclusion is half-orphaned and
half-contradicted by canon.** Specifically — the bias-bound spike (in `.integrated/`,
not my slice) promoted Candidate 3 to Instance 4 of `#disc-identifiability-floor`; this
triage spike, run as a strengthen-first follow-up *specifically to adjudicate the
Instance-4 traffic jam*, concluded with reasons (the five-element test, E4
single-escape failure, the "consumes not introduces" observation the bias-bound spike
itself made) that **Candidate 3 is not a floor instance**. One of these two is wrong
in present canon. This is not a filing decision — it is a "does
`#disc-identifiability-floor` Instance 4 belong there at all, or is it a category
error the triage caught?" decision. That is squarely a Joseph-reserved
framework-identity call (structurally the M4 §5.1 / meta-segment-scope kind named in
`doc/spike-routing.md` §6).

**Strengthen-before-soften check (`doc/audit-routing-instructions.md` §2):** I am not
asserting the triage is right and canon is wrong, nor the reverse. The triage's
argument is *robust-qualitative by its own labels* and rests on a reviewer-heuristic
five-element test (the spike says so: "Tier of the test itself: Discussion-grade").
The bias-bound spike's landing is *exact* (the heteroscedastic-normal counterexample
is constructive). It is entirely possible the right resolution is "Instance 4 stays
(it is a true no-go with a real escape) **and** the triage's E4-single-escape
objection is itself the soften-shaped move" — i.e. the triage may have talked itself
into demoting a true floor on a heuristic-test technicality, which would be exactly
the failure `doc/audit-routing-instructions.md` §0 names. I flag the *tension*; I do
not resolve it. The honest move is to surface it to Joseph with both spikes' arguments
laid side by side, not to auto-file the triage as "integrated" (it is not) nor
auto-act on its recommendation (canon already went the other way, deliberately or
not, and we do not know which).

**Recommended routing:** `orphaned` → **Joseph batch** (reserved-decision file-spike,
`doc/spike-routing.md` §6). The spike stays in `spikes/` until adjudicated *with* him.
The deliverable he needs is the two-column table above + the question: *is
`#disc-identifiability-floor` Instance 4 (= Candidate 3) correctly a floor instance,
or did the triage correctly find it is not — and where did Candidate 2 (the triage's
actual Priority-1) go?* **Tractability if the triage is upheld: heavy** (it would mean
re-working Instance 4 out of `disc-identifiability-floor.md` into
`#deriv-observation-ambiguity-bias-bound` as a downstream theorem, + promoting the
agent-internal Kalman-Ho instance — a cascade touching the meta-segment, the
bias-bound segment, and `der-loop-interventional-access`). **If Instance 4 is upheld
as-is: light** (the spike retires as a superseded recommendation, recorded in the
history layer). Either way it is a present-truth call about a meta-segment, not a
filing op.

---

## 4. `spike-kl-to-state-distance-template-extraction-2026-04-24.md`

**Completion-state:** (B-ish) — an architectural-proposal spike. It explicitly does
not derive math; it surveys clients and recommends Option B (a narrow
`#posterior-displacement-template`) *contingent on* (i) `#deriv-observation-ambiguity-bias-bound`
landing and (ii) ≥1 of three forward-looking clients materializing, with Option C
(no extraction) named as the honest fallback if they do not.

**Disposition: `live-or-open` — a complete scoping/proposal doc whose realization is
deliberately contingent and whose contingency is not yet met.** This is the cleanest
case in the slice and maps directly onto `doc/spike-routing.md` §3's architectural-
proposal pattern + §4 (heavy landing → written plan, not auto-land).

First-hand:
- The gate, `#deriv-observation-ambiguity-bias-bound`, **exists** in
  `01-aat-core/src/` (verified) — so contingency (i) is met.
- `#posterior-displacement-template` / `#transport-posterior-template` /
  `#information-displacement-template`: **none exist** (grep absent). The template did
  not land — *correctly*, because the spike conditions it on ≥1 forward-looking client
  (causal-IB / misspecification-cost / composition-scope-robustness) materializing,
  and all three are still "open" in CLAUDE.md §Open / `#disc-identifiability-floor`'s
  adjacent-floors list (verified: `disc-identifiability-floor.md:166, 210` still list
  them as candidate/open).
- `#deriv-variational-sector-condition` exists; the spike's recommended "adjacent
  family member" repositioning of it is not landed — also correctly contingent.

This is **not** `orphaned`: there is no real-and-true math or no-go sitting only in the
spike. The spike's *content* is the recommendation + a template-skeleton; the
recommendation is honestly contingent and the contingency (a forward-looking client
being actually pursued) is a *future-work bet*, not present truth being lost. Landing
it now would be premature template-extraction the spike itself argues against (Option B
"is *not* the right move ... if the three forward-looking clients are unlikely to
materialize").

**Recommended routing:** `live-or-open` — stays in `spikes/`. It is a standing
architectural proposal, the spike analog of a PROPOSALS.md entry. **Recommend (for the
parent, not done here):** surface it as a one-line PROPOSALS / PRACTICA pointer ("if
causal-IB or misspecification-cost is taken up, `#posterior-displacement-template`
extraction is pre-scoped here") so the bet is visible and the spike is not silently
lost — but it is **not** routed, moved, or archived this cycle. It is the
"`live-or-open`: incomplete-by-design, still needed" cell.

---

## 5. `spike-neutral-drift-endogenous-coupling-strengthening-2026-04-24.md`

**Completion-state:** Mixed — (A) partial strengthening (§A γ-from-cross-covariance in
matched-symmetric-Tier-1; §F regime-histogram filter-signature confirmation), (C) one
honest no-go (adversarially-constructed neutral drift matching all accessible channels
is provably invisible — a real scope limit), (D-ish) several "pattern established,
Instance-N tightening deferred" strands. The spike is careful and honestly labels its
own ceilings.

**Disposition: split — conclusion-level content is `integrated-filed`-adjacent (via
the sibling `spike-neutral-drift-lyapunov`, already `.integrated/`); two strands are
genuinely `orphaned`.**

First-hand:
- INDEX line 180: the *sibling* `spike-neutral-drift-lyapunov.md` (already in
  `.integrated/`) records that the load-bearing conclusion — *"AAT's sector condition
  defines an equivalence class over correction functions; Miller's motif depends on
  architectural variation within that class"* (latent structural diversity) + the
  endogenous-γ companion claim — **landed in `#result-structural-adaptation-necessity`
  Discussion + a five-segment gap-acknowledgment list**. I confirmed the *claim* that
  this is the canonical home is asserted by INDEX; the **decisive first-hand check of
  `#result-structural-adaptation-necessity` is OUTSIDE my slice's six files and I did
  not open it** — flagging this as a verification item for the confirmer / the
  neutral-drift-lyapunov adjudication, not asserting it verified. Within my slice's
  remit: the *2026-04-24* spike's relationship to that landing is "its conclusion is
  the same conclusion the sibling spike already routed."
- **Orphaned strand 1 — §A/§10.4 cross-covariance γ-estimator.** The spike derives
  $C_{12} = -\tfrac{\gamma\mathcal T}{2(\alpha-C)}\sigma_w^2 I + O(\gamma^2)$
  (*[Derived, conditional on Tier-1 matched-symmetric Model S]*) — a concrete,
  sign-preserving, closed-form estimator that *operationalizes Instance 3 escape (b)
  quantitatively*. `deriv-critical-mass-composition.md:180` references Instance 3
  escape (b) — but only the *pre-existing* "(CM2) is the unique broadly-available
  certificate" framing; **the cross-covariance Lyapunov-equation estimator itself is
  not present** (grep: no `C_{12}`, no cross-covariance γ-estimator, no Lyapunov-
  equation derivation in the segment). This is real derived math (standard Lyapunov
  algebra, the spike rates it *derived/exact-in-scope*) that lives only in the spike.
  **Tractability: tractable-moderate** — per the spike's §10.4 it is one Discussion
  subsection or derivation-audit-table addendum in `#deriv-critical-mass-composition`;
  "the derivation is standard Lyapunov algebra; the segment placement and framing are
  the main work." Borderline auto-landable but it is a *new derived result* (not a
  textbook restatement), so per `doc/audit-routing-instructions.md` §8 wording-class
  caution it should go through a written micro-plan + external eye, not silent
  auto-land.
- **Orphaned strand 2 — §8/§10.1 candidate fourth floor instance (agent-internal /
  Kalman-Ho).** Same content as the triage spike's Candidate 2 (§3 above). Not in
  canon. This is the *coupled-sibling* of the triage spike — the triage spike adjudicates
  exactly this candidate. They must be considered together (the triage is the
  adjudication of this spike's headline §10.1). **Routes with the triage spike to the
  Joseph batch** — flag-don't-route as an independent item; it is the same reserved
  decision.
- The §10.2 (agent-opacity observer-filtration neutral-drift scope note) and §10.3
  (sector-template fluctuation-structure note): **not in canon** (grep: no "neutral
  drift" / "Phase-1-regime-restricted" / fluctuation-architecture-discrimination
  content in `der-agent-opacity.md` or the persistence-template). These are
  paragraph-scale Discussion addenda the spike rates "low load-bearing"; they are
  minor orphans that land naturally *with* strand 1/2 if those land, or are honestly
  recorded as deliberately-not-in-canon if the fourth-instance decision goes against
  promotion.

**Recommended routing:** the spike is **not** cleanly filable this cycle. Its
conclusion-level content is integrated via the sibling; its §A estimator is a
tractable orphan (small written plan + external eye → `#deriv-critical-mass-composition`);
its §8/§10.1 fourth-instance strand is the *same* Joseph-reserved decision as the
triage spike and must be batched with it. Recommend: **keep in `spikes/` pending the
Joseph fourth-instance batch**; once that resolves, the §A estimator lands (or is
recorded declined) and the spike retires. Do not `.integrated/`-file it now — that
would assert the §A math is in canon, which is false.

---

## 6. `spike-rho-additive-variance-strengthening-2026-04-24.md`

**Completion-state:** (A) strengthened-to + (B) strengthened-past + (C) a no-go. The
strongest *math* spike in the slice: it promotes the prior spike's qualitative (R-V)
reframe to a **derived theorem (AV)** under named conditions (S1)–(S4) with an
information-geometric Pythagorean derivation; locates three regime-typed sub-cases
where multiplicative is native (MC / LD / PID); derives a **sharp no-go theorem** for
rate-domain multiplicative factorization; and honestly places (AV) as an
*adjacent-family member* of `#disc-additive-coordinate-forcing` (Bienaymé, not
Cauchy-FE) rather than over-promoting it.

**Disposition: `orphaned`. This is the canonical failure the cycle exists to catch —
real, true, derived math AND a real no-go, living only in the spike.**

First-hand, exhaustively:
- **`#rho-decomposition` / `#disturbance-decomposition`: does not exist** (`ls
  01-aat-core/src/`). The spike's primary recommended landing (§8.1, "strong
  recommendation", a new Section-I appendix housing §§2–6) **never landed**.
- **`#internal-external-decomposition.md` exists but is `status: robust-qualitative`
  and contains none of the spike's content.** Grep for `variance-additive`, `(AV)`,
  `(S1)`–`(S4)`, `Bienaymé`, `Pythagorean`, `no-go`, `multiplicative cascade`,
  `rho-decomposition` returns **only the frontmatter `status:` line** — i.e. zero
  matches for the actual content. The 2026-04-23 cycle promoted the *coarse
  log-additive* (R-V) form to this segment at robust-qualitative; the 2026-04-24
  spike's whole point is that (R-V) should be **replaced by the derived (AV)
  theorem** and the segment up-tiered under (S1)–(S4) — `doc/audit-routing-instructions.md`
  §4.6/§5 "integration is replacement". That replacement **did not happen**. The
  segment still carries the weaker form the spike superseded.
- The no-go (§4: under (N1)–(N3) no three-factor multiplicative $\rho^2$ for generic
  sub-scope-α; the spike rates it *discussion-grade, ~1 page of Kalman algebra to
  exact*) is **not in canon anywhere**. Not in `#disc-identifiability-floor` (the
  spike's §8.3/§4.3 recommended it as a candidate Instance 4 — but Instance 4 there is
  the *constant-C* one, §3 above; the rho no-go is absent), not in
  `#internal-external-decomposition`, not in `#disc-separability-pattern`.
- The §8.4 recommended adjacent-case addition to `disc-additive-coordinate-forcing.md`
  (variance-additive ρ as Bienaymé-forced adjacent family, parallel to Lyapunov):
  **absent** — the adjacent-cases section there (line 74) lists IB / Lyapunov only,
  not the variance-additive case.
- The §8.5 seventh-ladder refinement of `#disc-separability-pattern` (internal-external
  mediation ladder, Imai-et-al mediation-analysis framing of Regime A/B/C): **absent**
  — `disc-separability-pattern.md` is at **six ladders** (line 31 "six ladders", line
  39 the Identification-regime row is Regime A/B/C but generic, no internal-external
  $\chi$-mediation refinement; note line 45 says "seven distinct sources" — a stale
  internal inconsistency in that segment, orthogonal to this spike).

INDEX line 102 labels this **"Tier 2 — ready for promotion as new `#rho-decomposition`
appendix ... Unblocks deferred `#internal-external-decomposition`."** INDEX is, here,
*accurately reporting that this did not land* (Tier 2 = not landed). The failure is not
a mislabel — it is that **a Tier-2 result with a real derived theorem and a real no-go
has sat un-landed since 2026-04-24**, and `#internal-external-decomposition` is the
*parent spike's promoted segment that this spike was written to unblock and strengthen*
— it is carrying the weaker pre-strengthening form while the strengthened theorem sits
in the spike. That is precisely "the meat of the math (or a no-go) was left only in the
spike ... orphaned by busy-ness" (tracker, "The job").

**Strengthen-before-soften posture:** there is nothing to soften here — the spike
*already did* the strengthening (qualitative → derived theorem; produced the no-go).
The integration failure is the missing landing, not a missing strengthening attempt.
This is the post-strengthening *integration-is-replacement* half
(`doc/audit-routing-instructions.md` §4.6/§5/§6): the (AV) theorem should *replace* the
(R-V) form in `#internal-external-decomposition` (or land as `#rho-decomposition` with
`#internal-external-decomposition` re-pointed to it), and the no-go should be present-
tense canon (its own appendix or a `#disc-identifiability-floor`/Discussion statement,
per §5/§6 ghost-forms — it is a "competent reader would assume we missed it" no-go, so
5A/5B, *canon, not archaeology*).

**Recommended routing:** `orphaned`, **heavy landing → written integration-plan +
PRACTICA** (`doc/spike-routing.md` §4; `doc/audit-routing-instructions.md` §4.3/§4.4).
Scope of the landing the parent must size:
1. New `#rho-decomposition` appendix (the spike's §§2–6 are written content;
   status `conditional`: exact under (S1)–(S4), robust-qualitative outside) — OR
   in-place replacement of `#internal-external-decomposition`'s (R-V) with (AV) +
   up-tier. The spike recommends the new appendix; that choice is a Joseph/parent
   call.
2. The no-go as present-tense canon (appendix or Discussion, 5A/5B).
3. Cascade touches: `#internal-external-decomposition` (replace/repoint),
   `#disc-additive-coordinate-forcing` §8.4 adjacent-case row,
   `#disc-separability-pattern` ladder refinement,
   `#deriv-critical-mass-composition` / `#result-sector-persistence-template` /
   `#der-interaction-channel-classification` composition notes.
This is **heavy** (a new appendix + a status up-tier + a cascade of 4–5 segment
touches + a no-go appendix). It is best done by an agent holding the spike's context
— ideally as a deliberate landing cycle, not folded into routing. The §4.2 no-go
"~1 page of Kalman algebra to exact" is a real, scoped sub-task inside that plan.
**Sibling flag:** the parent `spike-rho-factorization.md` (predecessor, INDEX line
150, "PARTIALLY ABSORBED") and `spike-internal-external-decomposition.md` (the
deferred parent the §8.6 promotion-path targets) are coupled and *outside this
slice* — the landing plan must reconcile all three (rho-factorization = the
obstruction record; this spike = the strengthened replacement; internal-external =
the segment that consumes it). Flag-don't-route the siblings.

---

## 7. Frame feedback (per the brief's invitation)

Two things, offered as front-line confusion = re-truthification channel
(`doc/audit-routing-instructions.md` §7), not as challenge:

**(a) The slice label "S1 = TIER-1-LANDED, verify-in-canon" set the wrong prior, and
the spike-routing frame's own decisive-test discipline is what corrected it — working
exactly as designed.** The INDEX cycle *header* says TIER-1-LANDED; the per-spike
*status column under that header* says, accurately, "§7.1 LANDED / §7.2 Tier 2 / §7.3
Tier 3", "Tier 2 — ready for promotion", "Triage complete; moves Tier 2/3", etc. The
header is the convenience record; the column is closer to ground truth; and the column
is *itself* a hypothesis that the first-hand read either confirmed (bridge-lemma §7.1;
neutral-drift conclusion-via-sibling), refuted-optimistically (nothing here
overclaimed), or **refuted in the rarer dangerous direction (fenchel-bregman: a fully-
landed reframe recorded as an *un*landed Tier-3 proposal)**. The pilot scar
(`doc/spike-routing.md` Refinement 1: "the convenience-label is unreliable in *both*
directions, not only the optimistic one") held precisely. No frame change needed; this
is a confirming data point for that scar, and I'd recommend the parent record
fenchel-bregman as a second worked instance of the both-directions unreliability
(the first, in the pilot, was spike 2's *external-block* encoding; this one is a
*true-landing-recorded-as-unlanded*, a distinct sub-shape worth the scar).

**(b) The `identifiability-floor-triage` case exposes a frame gap worth a refinement:
`doc/spike-routing.md` §3's five states have no clean cell for a *routing/triage
spike whose recommendation canon partially followed and partially inverted*.** It is
not `orphaned` in the "math lives only in the spike" sense (there is no math). It is
not `integrated` (the recommendation was not followed). It is not `archived` (the
judgment is live and the inversion may be a real error in canon). I routed it to
`orphaned → Joseph-reserved` by analogy (the *judgment* is the orphaned load-bearing
content, and resolving the canon-divergence is a reserved present-truth call), but
the fit is by extension, not by the table. **Recommend a §3 refinement (Joseph-
directed, scarred):** add or sharpen a state for *meta/triage spikes* — their
"integration" test is "is the *decision* reflected in canon?", and a *contradicted*
decision is a present-truth flag (route to Joseph), not a filing op. This is the
spike analog of `doc/audit-routing-instructions.md` §4's "the no-go collapses *two*
things — the claim *and* the auditor's fix": here a triage spike can collapse two
things — its recommendation *and* whatever canon did instead — and the divergence is
the signal, not noise to file away. Flagged for the parent to fold or decline per the
§7 meta-stance (I do not rescope the SOP unilaterally).

**(c) Smaller:** the brief foregrounded git-provenance as a decisive-test instrument
(Refinement 2). In this slice it was *confirmatory but not decisive* — `git log -S`
landed every probe on the AAD→AAT sweep `9745397` (recency, poisoned, as warned);
`git show --stat b76ee67` (the named cycle commit) was the genuinely useful provenance
move (it bounded *what the 2026-04-24 theory landing actually touched*, which
corroborated the content-presence reads and, by *absence*, confirmed `#rho-decomposition`
et al. never landed in that cycle). Net: for this corpus the sharpest instrument was
**`git show --stat` on the cycle's own named landing commit**, more than pickaxe-`-S`.
Offered as a data point for the §7 evidence-hierarchy, not a correction.

---

## 8. Summary table for the parent (routing actions are the parent's)

| Spike | State (`doc/spike-routing.md` §3) | Action the parent must take | Tractable/heavy |
|---|---|---|---|
| bridge-lemma | `integrated-misfiled` (§7.1) **+ `orphaned` (§7.2)** | `git mv → .integrated/` **only after** §7.2 captured; §7.2 → written landing-plan + PRACTICA, **co-land with sibling `spike-passivity-composition.md`** | §7.1 done; §7.2 **heavy** (new appendix) |
| fenchel-bregman | `integrated-misfiled` (fully — both halves) | independent-verify the "full reframe landed" claim (`disc-additive-coordinate-forcing.md:14-84`), then `git mv → .integrated/`; **reconcile stale INDEX row 106 to "fully landed"** | n/a (done) |
| identifiability-floor-triage | `orphaned` — **Joseph-reserved decision** | Joseph batch: present the recommendation-vs-canon divergence table (§3); the question is whether Instance 4 (=Candidate 3) belongs, and where Candidate 2 went | heavy if triage upheld; light if Instance 4 upheld |
| kl-to-state-distance | `live-or-open` (contingent architectural proposal) | stays in `spikes/`; surface as a PROPOSALS/PRACTICA one-liner so the bet is visible; **not** moved/archived | n/a (not landed by design) |
| neutral-drift | split: conclusion integrated-via-sibling; §A estimator `orphaned`; §8/§10.1 = same Joseph-reserved decision as triage | keep in `spikes/` pending the Joseph fourth-instance batch; §A estimator → small written plan + external eye → `#deriv-critical-mass-composition` once batch resolves | §A **tractable-moderate**; §10.1 = triage's heaviness |
| rho-additive-variance | `orphaned` — **the canonical catch: real theorem + real no-go, only in spike** | written integration-plan + PRACTICA; heavy landing best by context-holding agent; reconcile siblings (`spike-rho-factorization`, `spike-internal-external-decomposition`) | **heavy** (new appendix + status up-tier + 4–5-segment cascade + no-go appendix) |

**Verification items I could not close from inside the slice (for the confirmer /
parent), explicitly flagged not-asserted:**
- neutral-drift's conclusion-level landing in `#result-structural-adaptation-necessity`
  Discussion + the five-segment gap list — asserted by INDEX line 180 (via the
  `.integrated/` sibling `spike-neutral-drift-lyapunov`); **not opened first-hand by
  me** (outside the six slice files). Should be confirmed when the
  `spike-neutral-drift-lyapunov` disposition is checked.
- The independent-verify gate (adjudicator ≠ confirmer) applies to every
  `content-in-canon` claim above; the named loci are given precisely so a confirmer
  re-reads the `src/` source, not this summary.

*No segment files, spikes, MANIFEST entries, moves, or commits were made. Read/report
only, per the delegation design.*
