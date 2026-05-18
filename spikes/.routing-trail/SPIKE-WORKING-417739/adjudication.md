# SPIKE-WORKING-417739 — S3 slice adjudication (composition / strategy / passivity)

*Adjudicator: fan-out agent, 2026-05-17. Slice S3 of the spike-routing cycle
(`msc/spike-routing-2026-05-17.md`). Read-only deliverable: dispositions +
reasoning + tractable-vs-heavy reads. All routing actions (moves, edits,
commits, landings) are the parent's. Every content-in-canon claim below was
verified first-hand against `01-aat-core/src/` and cross-checked with git
pickaxe provenance; named loci are given so a confirmer ≠ adjudicator can
re-check without re-deriving.*

## Slice

| Spike | Disposition | Landing tractability if orphaned |
|---|---|---|
| `spike-composition-gaps.md` | **integrated-misfiled** (Gap 1) + **research-seed already in PROPOSALS** (Gap 1's $\mathcal L$, Gap 2) | n/a — nothing orphaned |
| `spike-strategy-dynamics-gaps.md` | **integrated-misfiled** | n/a — nothing orphaned |
| `spike-passivity-composition.md` | **orphaned (partial)** — substantive heterogeneous-composition + dissipativity-template math not in canon | **heavy** (new appendix; queue) |
| `spike-pid-a2prime.md` | **orphaned (partial)** — explicit-$\alpha_{\text{PID}}$ B1/KYP derivation referenced but not landed | **tractable-to-medium** (α-list refresh) — but coupled to passivity; queue together |
| `spike-transient-dependency-amplification.md` | **live-or-open** (author-self-blocked; cross-component, correctly spike-resident) | n/a — not orphaned, do not land |
| `spike-pid-a2prime` ↔ `spike-passivity-composition` ↔ `spike-bridge-lemma-nonlinear §7.2` | **coupled cluster** — see sibling-coupling flag below | one queued integration-plan, not three |

---

## 1. `spike-composition-gaps.md` → integrated-misfiled (Gap 1); Gap 2 + $\mathcal L$ are tracked research-seeds

**Date 2026-04-01. INDEX: "Working sketch … Surfaced SP-17."** A 2026-04-01
"sketch" (renamed from `msc/sketch-composition-gaps.md` 2026-04-28). Two gaps.

**Gap 1 (does goal-blindness survive composition?) — landed.** First-hand
verified: `01-aat-core/src/hyp-directed-separation-under-composition.md`
exists, is in `01-aat-core/OUTLINE.md` (Ch.2 row, `status: draft`/conditional),
and carries the spike's load-bearing content — the two-case structure
(fixed-routing preserves / goal-dependent routing breaks), tied explicitly to
`#der-directed-separation`'s architectural classification. The segment is
*sharper than the spike*: it collapses the spike's three cases to two and
**explicitly excises** the spike's Case 3 "emergent leakage" as a category
error ("An earlier draft of this segment conflated the two; this was caught by
external review" — `hyp-directed-separation-under-composition.md:77`). This is
strengthen-before-soften working correctly at landing time: the spike's weaker
three-case hypothesis was replaced, not softened-with-a-pointer. Provenance
(pickaxe, pre-sweep): `d546cf4 Begin to shore up directed separation gaps,
composition and strategy dynamics`. The INDEX label ("working sketch")
**understates** — this is the recurring both-directions-unreliable INDEX
pattern (pilot 023198 scar); the content *is* in canon.

**Gap 1's $\mathcal L_{G\to M}^c$ quantity — deliberately-not-in-canon, tracked.**
The spike's goal-information-leakage mutual-information quantity
$I(o_c; G_t^c \mid \Omega_t)$ is *named in the segment as deliberately
out-of-scope-for-this-segment* (`hyp-directed-separation-under-composition.md:77`:
"If this phenomenon deserves formalization (and it may … ) it should be its own
segment"), and is tracked as **SP-17** in `PROPOSALS.md:178` (Bundle 2,
Value +4, scoping question own-segment-vs-subsection open). This is the
honest "deliberately-not-in-canon, recorded" state — not orphaned. No loss of
truth: the quantity is well-defined, the segment says so, PROPOSALS owns the
decision.

**Gap 2 (which strategy edges to attack) — landed via a different, stronger
construction; residual tracked.** First-hand verified:
`der-agent-opacity.md:59,79,113,132` closes the `#adversarial-edge-targeting`
gap with a **16-cell emitter-recipient closed-form arg-max** (paired with
`#der-interaction-channel-classification`'s recipient-side four-regime
decomposition). This is a *stronger and structurally different* result than the
spike's heuristic four-factor vulnerability score $V_{ij} = c\cdot(1-\sigma)
\cdot\gamma\cdot(1/r)$ — which the spike itself flagged "hypothesis … first
pass." The spike's narrower DAG-redundancy/criticality-metric residue is
tracked as **SP-20** (`PROPOSALS.md:332`, "probably lands as extension rather
than standalone, Value +3"). Again the honest tracked state, not orphaned.

**Disposition: `integrated-misfiled`.** Gap 1's load-bearing content is in
canon (verified, named loci); Gap 1's $\mathcal L$ and Gap 2's residue are
deliberately-deferred and *tracked in PROPOSALS as live proposals* (SP-17,
SP-20) — that is a legitimate non-canon home, not leakage. Nothing of value
lives only in this spike. Recommend parent `git mv → .integrated/` with a
MANIFEST line: *Gap 1 → `#hyp-directed-separation-under-composition`
(sharper two-case form; Case-3 excised by external review); $\mathcal L$ →
SP-17; Gap 2 → `#der-agent-opacity` 16-cell arg-max + residue SP-20.*
INDEX row should be reconciled from "working sketch" to integrated-filed at
cycle close.

---

## 2. `spike-strategy-dynamics-gaps.md` → integrated-misfiled

**Date 2026-04-01. INDEX: "Working sketch … Surfaced SP-20."** Renamed from
`msc/sketch-strategy-dynamics-gaps.md` 2026-04-28. Four gaps. All four landed;
first-hand verified each:

- **Gap 1 (when observational edge updates yield valid causal semantics)** →
  `scope-edge-update-causal-validity.md`. Carries the spike's exact
  load-bearing content: the C1–C3 conditions, the three-regime table
  (intervention-rich / partial / observation-only), and the **identifiability
  coefficient $\iota_{ij}$** with the discounted gain $\eta^{\text{adj}} =
  \eta\cdot\iota_{ij}$ (`scope-edge-update-causal-validity.md:62-99`) and the
  unification with the observability gate
  ($\eta_{\text{eff}} = \frac{U_{\text{edge}}}{U_{\text{edge}}+U_{\text{obs}}}
  \cdot\iota_{ij}$, line 95). Provenance (pickaxe, pre-sweep):
  `9376b8f Resolve edge semantics tension: regime-indexed causal efficacy
  estimates`. The 2026-04-25 INDEX header's framing of these 2026-04-01
  sketches as merely "appropriately spike-resident living artifacts" is
  **wrong in the integrated direction** — the content landed.
- **Gap 2 (complexity cost / IB-MDL for DAGs)** →
  `form-strategy-complexity-cost.md` (status discussion-grade, the IB/MDL
  tradeoff, $C_{\text{rep}}\propto|V|+|E|$ + maintenance, $\beta_\Sigma$
  volatility dependence).
- **Gap 3 (strategic tempo)** → `def-strategic-tempo.md` (the
  $\mathcal T_\Sigma = \sum\nu_\Sigma\eta_\Sigma^\ast$ form, identifiability-
  weighted, gated by epistemic tempo).
- **Gap 4 (three-way exploit/explore/deliberate)** →
  `disc-exploit-explore-deliberate.md` (the three-mode allocation, cascade-
  ordering constraint).

**One genuine open flag — surface, do not block this disposition.**
`TODO.md:112` records that `spikes/spike-three-way-tradeoff.md` (S5 slice, *not*
mine — flag-don't-route per the sibling rule) flagged that
`#disc-exploit-explore-deliberate`'s two-stage decomposition and $\Delta
V_\Sigma$ approximation "are hand-waving. Segment may be substantially
rewritten." That is a **segment-quality open item already tracked in TODO**,
not spike-leakage from `spike-strategy-dynamics-gaps` — Gap 4's content *did*
land; whether it should be rewritten is a separate, tracked question owned by a
sibling spike outside my slice. Recording it here so the parent sees the
cross-slice coupling; the disposition of *this* spike is unaffected.

**Disposition: `integrated-misfiled`.** All four gaps' load-bearing content
verified in canon with named loci and pre-sweep provenance; the only residue
(SP-20 DAG-vulnerability metrics, the Gap-4-rewrite question) is tracked in
PROPOSALS/TODO. Nothing of value lives only in this spike. Recommend parent
`git mv → .integrated/`; MANIFEST line naming the four target segments;
INDEX reconcile to integrated-filed.

---

## 3. `spike-passivity-composition.md` → orphaned (partial) — HEAVY landing, queue

This is the real S3 finding. **INDEX line 122: "PENDING REVIEW."** Status
frontmatter: "substantive for α sub-scope; partial for β."

**What the canon already has (verified first-hand).**
`result-contraction-template.md` is a landed segment (in OUTLINE) that absorbed
the *contraction-metric* generalization route and **does** carry: the PID-with-
bounded-plant promotion from sub-scope β (`result-contraction-template.md:91`),
the topology-indexed closure (parallel / hierarchical / small-gain) generalizing
`#deriv-critical-mass-composition`, and — critically — the **adversarial
no-go**: the three-obstruction convergence (Slotine 2003 saddle-point;
**Khalil ch.6 Thm 6.4 passivity-universality**; Daskalakis 2018) bounding the
template to the cooperative half of Section III
(`result-contraction-template.md:148,152,201`). So the spike's §8.3 honest-limit
(passivity does not handle strategic adversaries — the storage-function
universal-quantifier argument) **is canon**, correctly, as a no-go inside
`#result-contraction-template`. That part is *not* orphaned.

**What is genuinely orphaned (verified absent).** The spike's *substantive
positive payoff* is **not** in canon:

- No `#dissipativity-template` segment exists (`ls 01-aat-core/src/ |
  grep dissip` → only `result-contraction-template.md` matches, and that is the
  *contraction* template, a sibling, not this content). Not in OUTLINE.
- The heterogeneous-storage-function composition theorems (§3: parallel
  $S_1+S_2$; negative-feedback $\mathcal L_2$-stability with **mismatched
  storage-function shapes** — Mahalanobis Kalman + plant-plus-integral PID),
  the §4 worked Kalman+PID-on-positive-real-plant example, the §2 storage-
  function table (Bregman for exp-family, loss-excess for gradient), and the
  §7 α/β/α″/α‴ repartition under the passivity lens — **none of this is in any
  segment.** `result-contraction-template` reaches heterogeneous composition
  via the *Lohmiller-Slotine contraction* route, which is a **different
  certificate** (differential-Lyapunov, not Willems storage-function /
  port-structure). The spike's distinctive cross-tradition synthesis (Amari
  information-geometric storage ⋈ Willems dissipativity) and the port-structure
  reading of Class 1/3/2 are not absorbed.

**This is exactly the canonical failure the cycle exists to catch**, and the
project already knows it: `CHANGELOG.md:169` explicitly names "the bridge-lemma
§7.2 passivity/dissipativity math ready for the `#dissipativity-template`
appendix" as LANDED-but-leakage, and `TODO.md:440-445` + `PROPOSALS.md:240-268`
(SP-22) carry an open "Tier-2 backlog cluster" with `spike-passivity-composition`
(B2) as a member. SP-22's *architectural* gate ("separate appendices vs unified
meta-segment vs subsumed") was **resolved 2026-05-14** to (γ)-hybrid
(`CHANGELOG.md:73`, `TODO.md:437`): this lands as its own `#dissipativity-template`
appendix, **no longer gated** — "straight authoring now." So the blocker is
gone; the work simply has not been done.

**Strengthen-before-soften check.** No softening is implicated here — the spike
is a *strengthening* product (it reaches heterogeneous Tier-3 composition that
`#deriv-critical-mass-composition` only reaches via the conservative weakest-
link bound). The §8 honest limits are real scope boundaries, correctly
canonized as a no-go in `#result-contraction-template`. The orphaned part is
positive math, not a soften. The strengthen-first reflex does not change the
disposition; it confirms the math is worth landing.

**Disposition: `orphaned` (partial — adversarial-limit no-go is canon; the
heterogeneous-composition + dissipativity-template positive payoff is not).
Landing is HEAVY → queue with an integration-plan, do not auto-land.**
Rationale for heavy: a new appendix segment (`#dissipativity-template`),
a Class 1/2/3 port-structure addition to `#der-directed-separation`, the
§7 α/β repartition touching `#deriv-sector-condition`'s sub-scope list, plus
the satellite cross-refs the spike's §9.3 enumerates (≈7 segments). This is
multi-segment authoring with a cascade, squarely the
"substantial-segment-authoring → written landing-plan + PRACTICA" branch of
`spike-routing.md §4`. Per the no-go-protocol §4.3 the plan filename is
`spikes/spike-passivity-composition-spike-integration-plan.md`. The spike stays
in `spikes/` (live-or-open at the routing level) until landed by its best-
context owner.

---

## 4. `spike-pid-a2prime.md` → orphaned (partial) — coupled to §3; queue together

**INDEX line 123: "PENDING REVIEW."** Status: "Draft. Derivation complete for
the linear-SPR-plant case…". This is a *real derivation* product (Posture line:
"Real derivation using classical positive-real / passivity machinery"), not a
scoping doc — its central move is recasting SPR-tuned-PID *as* an instance of
`#der-gain-sector-bridge`'s B1 directional-fidelity property, with an explicit
sector constant $\alpha_{\text{PID}} = \omega_c\sin(\varphi_m)/\kappa(P)$.

**What is in canon (verified).** `result-contraction-template.md:91` promotes
"PID with bounded plant nonlinearity under Lyapunov metric" from sub-scope β,
and *names* "SPR-tuned PID (phase margin as sector constant; see
`#der-gain-sector-bridge` Verified Instances)." So the *fact of* PID-promotion
exists in canon via the contraction route, **with a forward reference** to
`#der-gain-sector-bridge`'s Verified Instances table.

**What is orphaned (verified absent).** I checked `der-gain-sector-bridge.md`'s
referenced "Verified Instances" — the spike's §11/§13 explicitly note PID is
*absent* from that table (it lists Kalman / gradient / exponential-family), and
the spike's whole point is that this absence "misrepresents the theory's
scope." The explicit B1-form derivation, the $\alpha_{\text{PID}} =
\omega_c\sin\varphi_m/\kappa(P)$ constant in AAT parameters, the tuning-method ×
sub-scope table (ZN-aggressive→β, IMC/lambda/SIMC→α), the anti-windup
sector-embedding, the Lur'e/circle-Popov extension, the cascade-PID composition
instantiation, and the six honest scope-exclusions — **none of this is in
`#deriv-sector-condition`'s α-list or in `#der-gain-sector-bridge`.** A
forward-reference from `#result-contraction-template` to a Verified-Instances
table that does not contain the content is precisely *"a reference is not
integration"* (`spike-routing.md §2`). `TODO.md:445` carries
`spike-pid-a2prime` (B3) in the same Tier-2 backlog cluster; SP-22's (γ)-hybrid
resolution (`PROPOSALS.md:266 (iii)`) routes it as an **α-list refresh in
`#deriv-sector-condition`** — i.e., the spike's own "Option A minimal surgical
edit," which the spike argues is sufficient.

**Disposition: `orphaned` (partial). Landing is TRACTABLE-to-MEDIUM** — the
(γ)-hybrid target is "α-list refresh in `#deriv-sector-condition`" + a row in
`#der-gain-sector-bridge`'s Verified Instances table (the spike's Option A,
which it argues — credibly — is the minimum sufficient move and matches the
shape of the prior `spike-a2-prime-strengthening` landing that *is* in canon,
INDEX line 195). The spike's Option B (full `#pid-sector-derivation` appendix)
is the heavy stretch. **However: do not land in isolation.** PID promotion has
three independent routes (B1 Lyapunov-metric already partly in
`#result-contraction-template`; B2 passivity §3; B3 KYP this spike) — INDEX
line 123 itself flags "Three independent promotion routes converge (B1/B2/B3)
— strong evidence" and the passivity spike §7 *also* does the α/β repartition.
Landing B3's α-list refresh and B2's dissipativity-template separately risks
the "parallel half-segments covering overlapping territory" failure
`PROPOSALS.md:268` explicitly warns about. **Recommend the parent treat
`spike-pid-a2prime` + `spike-passivity-composition` + `spike-bridge-lemma-
nonlinear §7.2` as one coupled landing cluster with a single integration-plan**
(the α/β-repartition and the dissipativity-template are the same territory seen
from two routes). The α-list refresh is tractable *as a unit of that plan*, not
as a standalone auto-land this cycle.

---

## 5. `spike-transient-dependency-amplification.md` → live-or-open (do not land)

**INDEX line 60: "OPEN — self-blocked on formal construction."** Date
2026-04-25. Status line: "Exploratory mathematical bridge attempt. Exact only
under the linearized / affine sub-scope."

This one is correctly spike-resident and **must not be routed as orphaned**,
for three independent reasons:

1. **Author self-blocked, explicit terminal verdict says stay.** §9 "Recommended
   Moves": *"Keep the concept as a Working Note in
   `03-llm-core/src/result-coupled-diagnostic-framework.md`. Do not replace
   `#hyp-exponential-cognitive-load` yet … Treat a future
   `02-tst-core/src/der-transient-dependency-amplification.md` as blocked on a
   formal construction of $J_F$ and a proved checkpoint-coverage condition."*
   §8 enumerates six open items (canonical $E_F$/$J_{\pi,k}$ construction;
   nonlinear remainder bounds; cyclic dependencies; empirical validation;
   whether real LLM/tool loops implement the idealized $P_k$; lower bounds).
   This is the `live-or-open` cell of `spike-routing.md §3` ("incomplete and
   still needed"), not `orphaned`.

2. **The exact-in-sub-scope math is genuinely real but its landing is author-
   gated and cross-component.** Lemma 1 (sup of Lipschitz policy-values is
   Lipschitz), Corollary 1 (the affine-sub-scope operator-norm bound), Prop 1
   (branching transient-growth $(|g|\sqrt B)^d$), Lemma 2 (checkpoint
   product/recurrence), and the singular-subspace coverage condition are exact
   *within the stated affine sub-scope* — that is real content. But the spike
   itself routes it to a **Working Note**, not a segment, *pending* the formal
   $J_F$ construction; per `feedback_math_lives_in_segments` the obligation is
   to land good math — but the spike's honest position is that the *promotable*
   theorem (a software sub-scope with $\widehat J_F$ defined and a proved
   checkpoint-coverage condition) **does not exist yet**. There is no orphaned
   *finished* result; there is an in-progress bridge whose finished fragments
   are sub-scope-conditional lemmas the author has deliberately parked as a
   Working Note until the construction closes. Landing the fragments now would
   import an incomplete bridge into canon — the wrong move.

3. **Cross-component, target is `02-tst-core`/`03-llm-core` not my AAT slice.**
   The pressure point is `#result-coupled-diagnostic-framework` (03-llm-core);
   the future segment is `02-tst-core/src/der-transient-dependency-
   amplification.md`. Even if it were ready, routing it is not an S3-AAT
   adjudication call.

**Disposition: `live-or-open`. Stays in `spikes/`. INDEX status already
correct ("OPEN — self-blocked on formal construction"); no change.** Not
orphaned, not archived, no MANIFEST entry, no landing. The one positive note
for the parent: the spike's §6 "natural metric: the Fisher metric" observation
is *already cross-referenced correctly* — it cites
`#deriv-fisher-whitened-update-rule` and the 4th instance of
`#disc-additive-coordinate-forcing` as the AAT-internal forcing for the metric
choice; that connective tissue is sound and needs nothing.

---

## 6. Sibling-coupling flag (per `spike-routing.md` partition rule)

Adjudicating S3 forced a check of a spike **outside my slice** that is
load-bearing for two spikes in it. Per the cross-slice rule
(*flag-don't-route*):

- **`spike-bridge-lemma-nonlinear-strengthening-2026-04-24.md` (S1 slice).**
  INDEX line 100: §7.1 LANDED Tier-1; **§7.2 passivity/dissipativity route →
  Tier 2, INDEX-targeted at "new `#dissipativity-template` appendix + Class
  1/2/3 port-structure addition to `#der-directed-separation`"** — i.e., the
  *same target* as `spike-passivity-composition` (§3 above). `CHANGELOG.md:169`
  names "the bridge-lemma §7.2 passivity/dissipativity math" as the headline
  LANDED-but-leakage item. **These are not independent spikes for landing
  purposes** — §7.2 of the bridge-lemma spike and `spike-passivity-composition`
  converge on one `#dissipativity-template` appendix; `spike-pid-a2prime`'s
  α/β repartition is the same territory from the KYP route. The S1 adjudicator
  will see the bridge-lemma spike as "§7.1 landed" and could mis-route §7.2 as
  a minor tail. **Recommend the parent fold S1's §7.2-passivity finding,
  S3's `spike-passivity-composition`, and S3's `spike-pid-a2prime` into one
  coupled `#dissipativity-template` integration-plan** (this is precisely the
  SP-22 (γ)-hybrid bundle, `TODO.md:440-449`, `PROPOSALS.md:262-266`, with the
  architectural gate already resolved 2026-05-14). One plan, one PRACTICA
  surfacing, best done by one owner holding all three — not three parallel
  half-landings (the `PROPOSALS.md:268` failure mode).

---

## 7. Frame feedback (the brief invites this)

Two observations, offered as front-line confusion = re-truthification channel
(`audit-routing §7`), not as challenge:

**(a) The S3 slice is mostly already-tracked, and that is the cycle working,
not a null result.** Four of six spikes resolve to *tracked* states
(2 integrated-misfiled with PROPOSALS/TODO residue; 1 live-or-open;
the orphaned 2 are *already* in the SP-22 backlog with the architectural gate
resolved). The genuine actionable signal in S3 is narrow and specific: the
`#dissipativity-template` cluster is real orphaned math, the project knows it
(CHANGELOG/TODO/PROPOSALS all name it), the only thing missing is the authoring
— and SP-22's resolution already cleared the blocker. The cycle's value here is
**confirming the leakage is exactly where the project's own tracking says it
is** (a verification, per the evidence-hierarchy), plus the *coupling flag*
(don't land B2/B3/§7.2 separately) which was not previously explicit in one
place.

**(b) The sibling-coupling rule earned its keep mid-slice.** The partition put
`spike-passivity-composition` and `spike-pid-a2prime` together in S3 (good) but
their controlling sibling — bridge-lemma §7.2 — is in S1. Without checking
outside the slice I would have called `spike-pid-a2prime` a clean tractable
α-list auto-land. It is not: landing it without the passivity/bridge-lemma
cluster is the parallel-half-segments failure. This is the pilot-023198 scar
recurring in a second slice; it confirms the rule is load-bearing and suggests
the parent may want to **explicitly designate the `#dissipativity-template`
cluster as a single cross-slice landing unit before the S1 and S4 agents
report**, so three agents don't independently recommend three partial landings.

---

## Summary table for the parent (verified loci for confirmer ≠ adjudicator)

| Spike | State | Decisive loci (first-hand verified) | Action |
|---|---|---|---|
| composition-gaps | integrated-misfiled | Gap1 `hyp-directed-separation-under-composition.md` (in OUTLINE, :77 Case-3 excised); $\mathcal L$→`PROPOSALS.md:178` SP-17; Gap2 `der-agent-opacity.md:59,113`; residue `PROPOSALS.md:332` SP-20. Prov `d546cf4`. | `git mv → .integrated/`; MANIFEST; INDEX reconcile |
| strategy-dynamics-gaps | integrated-misfiled | G1 `scope-edge-update-causal-validity.md:62-99` ($\iota_{ij}$); G2 `form-strategy-complexity-cost.md`; G3 `def-strategic-tempo.md`; G4 `disc-exploit-explore-deliberate.md`. Prov `9376b8f`. TODO:112 Gap4-rewrite tracked (sibling spike). | `git mv → .integrated/`; MANIFEST; INDEX reconcile |
| passivity-composition | orphaned (partial) — HEAVY | Adversarial no-go IS canon `result-contraction-template.md:148,152,201`; heterogeneous-storage payoff + `#dissipativity-template` NOT in canon (no such segment; OUTLINE absent). `CHANGELOG.md:169`, `TODO.md:444`, SP-22 (γ)-resolved `CHANGELOG.md:73`. | queue: integration-plan + PRACTICA; stays in `spikes/` |
| pid-a2prime | orphaned (partial) — TRACTABLE but coupled | Promotion-fact in canon `result-contraction-template.md:91` (fwd-ref only); explicit $\alpha_{\text{PID}}$/B1 derivation NOT in `#deriv-sector-condition` α-list or `#der-gain-sector-bridge` Verified Instances. `TODO.md:445`. | queue *with* passivity cluster; don't isolate-land |
| transient-dependency-amplification | live-or-open | §9 author verdict = Working-Note-only, blocked on $J_F$; §8 six open items; cross-component (02/03). INDEX:60 already correct. | no action; stays; no MANIFEST |
| bridge-lemma §7.2 (S1, flagged not routed) | coupled sibling | INDEX:100 §7.2 → same `#dissipativity-template` target; `CHANGELOG.md:169` headline leakage | flag to parent: one cluster, one plan |

*End SPIKE-WORKING-417739 adjudication.*
