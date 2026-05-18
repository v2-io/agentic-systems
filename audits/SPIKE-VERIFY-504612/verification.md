# SPIKE-VERIFY-504612 — independent-verify gate, S3+S4 `integrated-misfiled` slice

*Confirmer ≠ adjudicator (fresh instance, did not do the SPIKE-WORKING-417739
or -111710 adjudications). Gate per `doc/audit-routing-instructions.md` §8 +
`doc/spike-routing.md` §2/§7. Decisive test applied throughout: load-bearing
content opened first-hand in `01-aat-core/src/` (and the spike itself), not
the INDEX label and not the adjudication's own summary. Git provenance not
needed as the deciding instrument here — every claimed locus was present and
substantive on direct read; provenance would only have been invoked had a
locus been thin/absent. No moves, edits, or commits — the durable batch is
the parent's.*

## Verdict table

| Spike | Adjudication | My verdict | Loci I opened first-hand |
|---|---|---|---|
| `spike-stochastic-non-exit-strengthening-2026-05-16` | integrated-misfiled (state-3 no-go *is* canon, cascade closed) | **CONFIRM** | `deriv-stochastic-non-exit.md` (whole), `deriv-sector-condition.md` Prop A.1S/(iii′)/(iv)/Cor A.1S.1, `result-sector-persistence-template.md:90` |
| `spike-composition-gaps` | integrated-misfiled (Gap1 sharper; residue→SP-17/SP-20) | **CONFIRM** | spike (whole), `hyp-directed-separation-under-composition.md` (whole), `der-agent-opacity.md` 16-cell arg-max, `PROPOSALS.md` SP-17/SP-20 |
| `spike-strategy-dynamics-gaps` | integrated-misfiled (all 4 gaps landed) | **CONFIRM** | spike (whole), `scope-edge-update-causal-validity.md`, `form-strategy-complexity-cost.md`, `def-strategic-tempo.md`, `disc-exploit-explore-deliberate.md` |
| `spike-active-inference-vs-aad` | integrated-misfiled (G-BP2 V-medium landed; doc = reference catalog) | **CONFIRM** | spike (verdict/recs), `form-strategy-complexity-cost.md:42-69,137` |
| `spike-l1-evidence-axiom` | integrated-misfiled (minimal landing done) | **CONFIRM** | `deriv-edge-update-natural-parameter.md:135` + Findings, `disc-identifiability-floor.md` Instance 2 |
| `spike-jacobian-b1-strengthening` | integrated-misfiled (moderate landing done) | **CONFIRM** | `form-composition-closure.md:210`, `result-contraction-template.md:79-91`, `der-gain-sector-bridge.md:108-115`, `disc-additive-coordinate-forcing.md:44` |

**All six confirmed.** No refute. I reached for the refute (the brief is
right that it is the valuable outcome and the conviction-of-fine is the
failure the gate catches) — the load-bearing content is genuinely present,
genuinely covers what each spike carried, and in four of six is *stronger
than the spike*, labelled honestly per integration-is-replacement.

---

## 1. `spike-stochastic-non-exit-strengthening-2026-05-16` — CONFIRM (opened fully, per the brief)

This is the one the brief flagged as load-bearing ("the state-3 no-go *is*
canon with cascade closure"). I opened the spike in full and all three
claimed loci.

- **The no-go is canon as its own appendix, not a reference.**
  `deriv-stochastic-non-exit.md` is a dedicated `status: exact` derivation
  segment (depends: `deriv-sector-condition`,
  `result-sector-condition-stability`,
  `result-structural-adaptation-necessity`). It carries the spike's §3.2
  obstruction *verbatim-in-substance*: the $G(t)=e^{2\alpha t}V$
  non-supermartingale, the sign-indefinite compensated $S(t)$ (negative
  exactly inside the persistence basin), the unbounded-scale-function /
  no-non-constant-bounded-harmonic-function obstruction, and the general
  $P(\tau_R<\infty)=1$ argument for *any* $F$ under (A2') (not OU-scoped —
  OU is the explicit instance). The simulation table (spike §3.3) is
  reproduced. This is the math living in a segment, not the spike — the
  exact failure the cycle exists to catch is *absent here*.
- **The corrected positive statements are canon.**
  `deriv-sector-condition.md`: (iii′) fixed-time tail at lines 194-198
  (constant unchanged, object corrected — exactly the spike's §4 (iii′));
  (iv) finite-horizon Khasminskii sup-bound; **Corollary A.1S.1** (lines
  258-268) the containment dichotomy $P(\tau_R<\infty)\in\{0,1\}$,
  `status: exact`, "new exact result", with full `## Findings` entry
  (326-346); proof paragraph (252) corrected to point at
  `#deriv-stochastic-non-exit`; Epistemic Status (306) reconciled;
  Discussion §"Kind of guarantee" (322) landed; both summary-table rows
  (275-276, 293-294) corrected. The spike's §6 six-point recommended
  disposition is landed point-for-point.
- **Cascade closure verified first-hand at the named locus.**
  `result-sector-persistence-template.md:90` ("On Prop A.1S
  region-awareness"): "Model S provides a distributional / fixed-time
  guarantee, not pathwise-forever containment (which is a Model-D-only
  guarantee); template instantiations inherit that kind-of-guarantee
  distinction, not an infinite-horizon non-exit bound." This is the
  613842-F2 integration-debt propagation, landed — the dependent of the
  corrected claim carries the correction, not the stale framing.
- **Ghost discipline correctly applied.** Body + `## Findings` state
  present truth only; the project-autobiography ("previously asserted
  $P(\tau_R<\infty)\leq…$", the 628401-prediction-disconfirmed record)
  lives in Working Notes (`deriv-stochastic-non-exit.md:87`,
  `deriv-sector-condition.md:354-356`) — not in the canonical claim.

Nothing of value lives only in the spike (its dead-end record is canonized
as the reusable no-go signature in `deriv-stochastic-non-exit.md` Epistemic
Status + Findings). Safe-mechanical `git mv` → `.integrated/` warranted.

## 2. `spike-composition-gaps` — CONFIRM

- **Gap 1** → `hyp-directed-separation-under-composition.md` (exists,
  `status: conditional`, correct `depends:`). Genuinely *sharper* than the
  spike: the spike's three-case structure (with Case 3 "emergent
  goal-conditioning" and the $\mathcal L_{G\to M}^c$ leakage term presented
  *in the body* as a substantive case) is collapsed to two cases, and
  Case 3 is **explicitly excised as a category error** (line 77: "An
  earlier draft of this segment conflated the two; this was caught by
  external review" — the leakage MI is named as a *separate phenomenon*
  that "should be its own segment", not a directed-separation case). This
  is strengthen-before-soften applied at landing (weaker hypothesis
  *replaced*, not softened-with-a-pointer). Confirmed exactly as the
  adjudication described.
- **Gap 1's $\mathcal L$** → tracked live as SP-17 (`PROPOSALS.md:178`,
  Value +4, scoping question own-segment-vs-subsection open). Honest
  deliberately-not-in-canon home, not leakage.
- **Gap 2** → `der-agent-opacity.md:52-59,78-79,95,113,132`: the 16-cell
  emitter-recipient closed-form arg-max closing `#adversarial-edge-targeting`
  — a *stronger and structurally different* result than the spike's
  heuristic four-factor $V_{ij}$ (which the spike itself flagged
  "hypothesis ... first pass"). Residue tracked SP-20 (`PROPOSALS.md:332`,
  Value +3). *(Minor: the adjudication's prose/table cite
  `der-agent-opacity.md:59,79,113,132`; the decisive content is across
  52-59/78-79/95/113/132 — the two anchor lines it named, :59 and :113,
  are both correct first-hand. Locus citation is accurate to intent; no
  defect.)*

Nothing of value lives only in the spike.

## 3. `spike-strategy-dynamics-gaps` — CONFIRM

All four gap segments exist with substantive content (not stubs:
171/111/183 lines for gaps 2/3/4 plus the gap-1 segment), correct
frontmatter and `depends:`:

- **Gap 1** → `scope-edge-update-causal-validity.md` (`status: conditional`).
  Verified at the *exact* loci the adjudication named: `:62`
  $\eta^{\text{adj}}=\eta\cdot\iota_{ij}$; `:95` the combined
  $\eta_{\text{eff}} = \frac{U_{\text{edge}}}{U_{\text{edge}}+U_{\text{obs}}}\cdot\iota_{ij}$
  unification with the observability gate; C1-C3 + three-regime table
  upstream. The spike's Gap-1 load-bearing content landed faithfully.
- **Gap 2** → `form-strategy-complexity-cost.md` (IB/MDL tradeoff,
  $C_{\text{rep}}$, $\beta_\Sigma$ volatility dependence). *Strengthened
  past the spike*: the spike's hypothesis-grade Shannon-MI form was
  replaced by a regret-bound-*derived* KL-direction objective with a
  uniqueness theorem (`#deriv-strategy-cost-regret-bound` §6.1).
- **Gap 3** → `def-strategic-tempo.md` ($\mathcal T_\Sigma=\sum\nu_\Sigma\eta_\Sigma^\ast$,
  depth-gated/exploration-gated cases, epistemic-tempo gating).
- **Gap 4** → `disc-exploit-explore-deliberate.md` (three-mode allocation,
  two-stage decomposition, cascade ordering, dominance regimes).

Residue (SP-20; the Gap-4-rewrite question at `TODO.md:112`) is a
separate, tracked segment-quality item owned by a sibling spike outside
this slice — not leakage from *this* spike (whose Gap-4 content *did*
land). Disposition unaffected. INDEX 2026-04-25 "living artifacts" header
is wrong in the integrated direction (the recurring
both-directions-unreliable pattern).

## 4. `spike-active-inference-vs-aad` — CONFIRM

The operative G-BP2 recommendation (pursue V-medium; refuse V-strong) is
fully landed in `form-strategy-complexity-cost.md:42-69`: the variational
form $\Sigma_t^\ast=\arg\min[I(\mathcal C_t;\Sigma_t)+\beta_\Sigma D_{\mathrm{KL}}(\pi^\ast\Vert Q_{\Sigma_t})]$,
the Pinsker/regret-bound KL-direction derivation, the explicit "analog of
variational free energy in active inference (Friston 2017; Da Costa 2020;
Parr & Pezzulo 2022) **without** committing to preferences-as-priors or
EFE-as-master" framing. *Strengthened past the spike* (spike left KL
direction as a selection; canon derives it via the regret bound +
`#deriv-strategy-cost-regret-bound` uniqueness theorem). The spike is a
scoping/positioning document whose actionable content is discharged;
remaining value is a durable positioning reference catalog (the
spike-routing §1 "INDEX/PROPOSED stay, not routed" analog at the
spike-content level — here, the *recommendation* is discharged, the
catalog is what files). No canon work owed. Confirmed.

## 5. `spike-l1-evidence-axiom` — CONFIRM

`deriv-edge-update-natural-parameter.md:135` carries the spike's
load-bearing content faithfully: observable-$C$ → $(2K+1)$-dim vector
log-odds via per-factor Aczél, *explicitly labeled
"generalization-in-scope ... not a new primary instance"*; unobservable-$C$
→ soft-EM responsibility nonlinearity makes block-additivity structurally
inconsistent; explicit dual-route convergence with
`#disc-identifiability-floor` Instance 2's Cramér-Rao rank-1 obstruction,
framed as the "structural, not analytical-artifact" strengthening.
`disc-identifiability-floor.md:52-67,138` carries Instance 2 with the
Sylvester's-law unification; the l1-evidence dual-obstruction is absorbed
*into* Instance 2 (not a separate instance) exactly as the spike
recommended. Epistemic register correct (no over-claim of a new theorem —
integration-is-replacement label-tracks-truth applied: a generalization is
labelled a generalization). Confirmed.

*Cross-slice note (flag, not in my remit): `disc-identifiability-floor.md`
lines 138/164/166 state the segment has exactly **four** instances,
Instance 4 = (PI)/Čencov. This is internally consistent with the S4
adjudication's separate claim (for `spike-rho-factorization`, NOT in my
slice) that a rho-no-go floor instance would be Instance 5. My slice's
`l1-evidence` correctly sits inside Instance 2, no instance added — clean.
Surfacing only because the instance count is load-bearing for the
out-of-slice rho item the parent is already tracking.*

## 6. `spike-jacobian-b1-strengthening` — CONFIRM

All four named loci opened first-hand and present:

- `form-composition-closure.md:210` — the DA2'-inc ≡ (CT2) at $M=I$
  transparency note (cf. Rockafellar & Wets 1998), Angle 2, no new axiom.
- `result-contraction-template.md:79-91` — metric-α₁ "Euclidean metric,
  AAT-internally derived via DA2'-inc ≡ (CT2) with M=I" partition; the
  non-statistical metric-α₂ cases (Hessian, Lyapunov-linear-Hurwitz,
  PID-bounded-plant) each explicitly "Theorem-imported (... no AAT-internal
  axiom forces the ... coordinate)" — the spike's honest no-lift for 3 of
  5 cases, labelled honestly.
- `der-gain-sector-bridge.md:108-115` — the "Fisher-metric cases under
  parameterization-invariance" block: (PI) extending `#scope-agent-identity`,
  Čencov 1982 forcing the Fisher metric uniquely, the two statistical
  metric-α₂ cases upgraded from derived-conditional-on-inner-product to
  derived-AAT-internally-forced (Angle 3).
- `disc-additive-coordinate-forcing.md:44` — the "Metric" row
  (PI / Čencov / Fisher metric) as a primary layer, *strengthened past*
  the spike into the four-layer Chain/Divergence/Update/Metric
  unification.

Angle 1 (heredity / strong option) correctly NOT taken — no segment
asserts heredity as an adopted axiom; it remains an open architectural
question (the adjudication flags it as a Joseph-reserved PROPOSALS item,
separate from filing the spike — out of my verify remit, noted as
consistent with what I read). Confirmed.

---

## Gate outcome

Six `integrated-misfiled` adjudications, all **CONFIRMED** by first-hand
read of the actual `src/` loci (and the spikes themselves where the no-go /
landing claim was load-bearing). The decisive test was satisfied in every
case: the load-bearing content is in a segment/appendix, present and
substantive, covering what the spike carried; four of six are *stronger
than the spike*, labelled honestly per integration-is-replacement; ghost
discipline is correctly applied in the one no-go case. No content found
thinner than claimed; no reference-masquerading-as-integration; no payload
strand missing; the stochastic-non-exit cascade is genuinely closed at the
named dependent.

The parent's safe-mechanical `git mv` → `.integrated/` (single durable
batch, INDEX reconciliation at cycle close) is warranted for all six on the
strength of this independent verification. One minor, non-blocking locus-
citation slack noted for `spike-composition-gaps` Gap 2 (adjudication cited
:59,79,113,132; decisive content spans 52-59/78-79/95/113/132 — anchors
correct, no defect). The out-of-slice instance-count consistency note (§5)
is surfaced for the parent's already-tracked rho item, not a refute of
anything in this slice.

*End SPIKE-VERIFY-504612.*
