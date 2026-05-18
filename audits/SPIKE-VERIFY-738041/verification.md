# SPIKE-VERIFY-738041 — Independent-verify gate (V3 ⊃ S5 + S6-misfiled)

*Confirmer ≠ adjudicator (fresh instance). 2026-05-17. Gate per
`doc/audit-routing-instructions.md` §8 + `doc/spike-routing.md` §7. Decisive
test applied throughout: load-bearing content opened **first-hand in `src/`**
(named loci read, not the INDEX label, not the adjudication's summary); git
provenance via pickaxe `-S` / `--follow --diff-filter=A` used where it was the
sharpest non-destructive instrument. No moves/edits/commits — the durable
batch is the parent's.*

Slice verified:
- `audits/SPIKE-WORKING-029307/adjudication.md` (S5) — the **three
  `integrated-misfiled` items only**: `spike-fep-suboptimal-approximation`,
  `spike-message-passing-credit-assignment`, `spike-attention-causal-graphs`.
  (The S5 `orphaned` / `live-or-open` / Joseph-reserved items —
  `spike-alignment-impossibility`, `spike-aporia-sub-agent-adversarial`,
  `spike-attention-governance`, `neurips-back-integration` — are **out of this
  gate's scope** by the parent's brief; not re-adjudicated here.)
- `audits/SPIKE-WORKING-418736/adjudication.md` (S6) — the **three
  `integrated-misfiled` directory spikes only**: `class-coercion-wrapping/`,
  `track-a-intent-dag/`, `track-b-nonlinear-sims/`. (`temporal-nesting-rg/`
  deliberately held for a separate Joseph batch — excluded.
  `spike-language-as-causal-substrate/`, `spike-local-embedding-benchmark/`,
  `spike-strategic-self-coupling.md` are not `integrated-misfiled` — out of
  scope.)

---

## Verdict summary

| Spike | Adjudicated | Verify verdict | Decisive-test loci opened first-hand |
|---|---|---|---|
| `spike-fep-suboptimal-approximation` | integrated-misfiled | **CONFIRM** | `disc-ciy-unified-objective.md:58, :64, :66`; provenance `73f43a0`/`e39c17b` |
| `spike-message-passing-credit-assignment` | integrated-misfiled (refuted core integrated-as-replacement; corrected result canon) | **CONFIRM — both halves** | `disc-credit-assignment-boundary.md:87, :95, :130`; mean-field-VMP grep across 4 `src/` trees; provenance `73f43a0` |
| `spike-attention-causal-graphs` | integrated-misfiled on core, **coupled-flag** (not unconditional `git mv`) | **CONFIRM (content) + concur with coupling caveat** | `der-directed-separation.md:57, :59-63, :77, :85, :89, :120, :146`; residual-absence grep; sibling provenance `446c7a1` |
| `class-coercion-wrapping/` | integrated-misfiled | **CONFIRM** | `der-class-coercion-via-wrapping.md` (Thm1/2, C1-C3, W₀/W₂/W₁ `:87-93`), `der-class-coercion-in-composition.md`, `der-logogenic-as-wrapping.md`, `def-auxilia-hierarchy.md:80`; 4 §4.2 cross-refs; Working-Notes-only spike cite `:157`; bifurcation `758cd89` |
| `track-b-nonlinear-sims/` | integrated-misfiled | **CONFIRM** | `result-adversarial-tempo-advantage.md:26-38 (Model D b=2), :40-54 (Model S b=3/2), :56-66 (regime table), :70-74 (exact-conditional), :90 (finite-ν)` |
| `track-a-intent-dag/` | integrated-misfiled (archaeology) | **CONFIRM** | `00-intent-dag-formalism.md` header; INDEX:163; `_obs/04-intent-dag-consolidated.md` present; `def-strategy-dag.md`/`def-shared-intent.md` canonical |

**No refutes.** All six content-claims hold under first-hand `src/`
verification. Two non-blocking caveats carried forward (below) — both are
*concurrences with the adjudicators' own flags*, not refutes, and neither
changes a disposition; they constrain how the parent batches the `git mv`s.

---

## 1. `spike-fep-suboptimal-approximation` — CONFIRM `integrated-misfiled`

Spike §5 named its own best landing: a small Discussion addendum in
`#disc-ciy-unified-objective` (EFE-like objectives recovered under specific
restrictions; **do not promote as a dominance theorem**). Verified first-hand
that this landing exists and is faithful:

- `disc-ciy-unified-objective.md:58` — "The dark-room problem is bypassed
  entirely by the Survival Imperative: exploration is not driven by
  preferences-as-priors, but by the literal physical boundaries of the
  Lyapunov sector constraint." = spike Assumption 1 (Dark Room Collapse).
- `:64` — full EFE pragmatic/epistemic decomposition; structural isomorphism
  ($Q_O$ ≈ pragmatic, CIY ≈ epistemic) **with the two substantive differences
  named**: causal-not-associational (Level 2 vs Level 1 = spike Assumption 3)
  and preferences-not-as-priors with the satisfaction-gap distinction (= spike
  Assumption 1); dark-room critique (Sun & Firestone 2020) cited;
  "convergence is at the shared-shape level … not unified content."
- `:66` — the regret-bound / KL-direction route makes the point **without**
  claiming strict suboptimality ("via decision-theoretic regret bound on
  $Q_O$ rather than via free-energy-gradient flow") = the spike's §4/§5
  "claiming EFE strictly suboptimal is an overreach."

Provenance: spike created `73f43a0` (2026-04-25); the dark-room-bypass content
entered `disc-ciy-unified-objective.md` in `e39c17b` (2026-04-25, "Causal-IB
exploration drive") — co-temporal with the spike-intake. The causal-IB LMI
work the spike said to "wait for" has settled (`deriv-causal-ib-lmi.md`,
`deriv-causal-ib-exploration.md` both present, `status: conditional`;
`disc-ciy-unified-objective.md:44` says "now been formally derived as the
exact Lagrangian relaxation of the LMI").

Spike Assumption 2 (scalar/isotropic Λ epistemic-pricing) is the only element
not mirrored — and the spike **itself** recommended against promoting the
formal three-assumption derivation. Per integration-is-replacement, this is
correctly not a gap; nothing true lives only in the spike.

**Verdict: CONFIRM.** INDEX:58 stale ("OPEN — … land later after causal-IB
settles"); reconcile to `integrated-filed` at cycle close.

## 2. `spike-message-passing-credit-assignment` — CONFIRM (both halves of the subtlety)

This was the flagged one. The subtlety: the spike's **refuted core**
(mean-field VMP for AND/OR-DAG credit assignment, §3-5) is claimed
integrated-**as-replacement** (i.e. canon correctly *excludes* it, does not
ghost it in), while the **corrected result** (the §6 forward-pass repair:
EP / Max-Sum / loopy-BP on factor graphs preserving AND/OR as exact
potentials) is claimed canon. Both halves verified independently:

**Corrected result is canon** (`disc-credit-assignment-boundary.md`):
- `:130` — "Useful Level 2 factor-graph approximations include: exact Belief
  Propagation (BP) on tree or polytree cases, **loopy BP or max-sum for
  MAP-style diagnosis, Expectation Propagation (EP) for approximate
  marginals**, and **structured variational methods only where common-cause
  structure is explicitly modeled**." This is precisely the spike's §6
  forward-pass repair *and* the §4 mean-field-floor finding (the
  structured-variational-only-where-common-cause caveat is the spike's
  L1-correlation floor).
- `:95` — #P-hardness anchored *more sharply* than the spike
  (Shapley-over-AND/OR-game, Deng-Papadimitriou 1994 #P-completeness,
  exact-vs-approximate caveat).
- `:87` — tree-DAG / observable-leaves exact-BP case (= spike's correct
  sub-case).

**Refuted core is integrated-as-replacement, not ghosted** — verified by
grepping all four `src/` trees for `mean-field` / `variational message
passing` / `VMP`. The only hits are *unrelated contexts*: mean-field **VI**
for the variational-inference *sector condition / persistence*
(`deriv-variational-sector-condition.md`, `impl-strategy-dynamics.md` — a
different topic, KL-budget agents) and mean-field **games** ($N\to\infty$
population limit, `deriv-strategic-composition.md`). **No canon segment
endorses mean-field VMP for AND/OR-DAG credit assignment.** The
credit-assignment segment's Level-2 list (`:130`) deliberately omits
mean-field VMP and admits *structured* variational methods only with the
common-cause caveat — i.e. the spike's §3 refuted core is excluded by
replacement, exactly as claimed. Not a softened ghost.

Provenance is decisive and clean: pickaxe on `"Expectation Propagation (EP)"`
and `"loopy BP or max-sum"` both resolve to `73f43a0` — the **same commit**
that created the spike (`git log --follow --diff-filter=A`). Co-authored:
spike = reasoning trail (incl. its own §6 self-refutation of mean-field VMP);
segment = corrected result.

The only thing not in canon is a full standalone derivation appendix — which
the spike *itself* flags as requiring a mean-field→loopy-BP/EP rewrite before
promotion, and which INDEX:59 records as queued. Per math-lives-in-segments
the test is whether real true math lives *only* in the spike: it does not.
The un-landed appendix is an optional strengthening, not orphaned truth.

**Verdict: CONFIRM, both halves.**

## 3. `spike-attention-causal-graphs` — CONFIRM (content) + concur with the coupling caveat

**Load-bearing core IS canon (verified first-hand).** Spike Version 4 +
"Implications for κ" (lines 205-300, 414-426: directed separation is
architecture-dependent not universal; κ is the *topology of the processing
graph* not a parameter of f_M; characterize which topologies admit separation
rather than parameterize a perturbation; κ_processing as a diagnostic) maps
exactly onto `der-directed-separation.md`:
- `:57` "Whether directed separation holds is determined by the agent's
  **processing topology** … a structural property of the architecture, not a
  tunable parameter."
- `:59-63` Class 1/2/3 (Separated/Partial/Coupled) table; **transformer LLM
  attention** = canonical Class 3 "Fails by construction" = spike's merged
  case.
- `:77` κ_processing as distribution-dependent Class-2 diagnostic;
  "classification is the primary tool; operationalization is a diagnostic" =
  spike's "κ_processing would then be a DIAGNOSTIC."
- `:85` "Why the classification is not a smooth parameter … replaces an
  earlier κ-as-scalar framing."
- `:89, :120, :146` carried at robust-qualitative grade; `:120` explicitly
  credits the *sibling* `spikes/spike-kappa-topology-insight.md` (now
  `.integrated/`) as the promoted source.

Sibling provenance verified: `spike-attention-causal-graphs`,
`spike-attention-governance`, and `spike-kappa-topology-insight` all created
in the same commit `446c7a1` (2026-03-14, "Brainstorm the kappa idea …"),
one overnight session. `spike-kappa-topology-insight.md` is now correctly
under `.integrated/`. The core landed via that sibling — convergence, not a
debt the segment owes this spike (pickaxe on `der-directed-separation.md` is
sweep-poisoned by the AAD→AAT rename; recency uninformative, content
verified-present, decisive test passed).

**Residual is genuinely NOT in canon (verified).** Grepped all four `src/`
trees for finite-attention / sentinel / multi-frequency /
severity-proportional / startle / attention-governance / attention-budget:
**zero** matches. The one "attention allocation" hit
(`der-directed-separation.md:42`) is the directed-separation
selection-vs-processing distinction, **not** the spike's
attention-governance machinery — exactly as the adjudication stated. So the
misfiled call is sound on the content axis (core canonical, residual absent
and self-flagged speculative + cross-domain ideation).

**Concurrence (not a refute), carried for the parent.** The adjudication does
**not** route this for an unconditional `git mv`: it explicitly couples
`spike-attention-causal-graphs` with `spike-attention-governance`
(Joseph-reserved, out of this gate's scope) — the two spikes' residuals are
the same `446c7a1` overnight ideation cluster, and S5 says "flagging, not
routing the pair." My independent read confirms the *content* claim
(`integrated-misfiled` on the core is correct) **and** concurs with the
coupling caveat: the `git mv` for `spike-attention-causal-graphs` should
**not** fire independently of the Joseph-reserved `spike-attention-governance`
decision. CONFIRM-with-caveat, not a blank-check confirm.

## 4. `class-coercion-wrapping/` — CONFIRM `integrated-misfiled`

`99-verdict.md` §4.1-4.5 / §7 recommended landing path verified executed
first-hand:
- `der-class-coercion-via-wrapping.md` (`status: conditional`) — Theorem 1
  (exact, C1-C3, full conditional-independence proof `:67`), Theorem 2
  (approximate, C3→leakage-bound, data-processing-inequality proof `:81`),
  the **W₀/W₂/W₁ leakage hierarchy table `:87-93`** with the structural bound
  $\kappa_{W_1} \le I(A(q_M); G_W \mid q_M)$. Every load-bearing claim from
  `01-theorem-statement.md` / `03-leakage.md` present.
- `der-class-coercion-in-composition.md` (`status: conditional`) — the §4.1
  bifurcation, confirmed by commit `758cd89` "Refactor: bifurcate
  der-class-coercion-via-wrapping into two derivations."
- `der-logogenic-as-wrapping.md` (`03-llm-core/`, `conditional`) — §4.3
  logogenic specialization.
- `def-auxilia-hierarchy.md:80` (`04-eli-core/`, `sketch`) — §4.4
  auxilia-as-W₁ cross-reference.
- §4.2 cross-refs verified integrated: `der-directed-separation`,
  `hyp-directed-separation-under-composition`, `form-composition-closure`,
  `der-tempo-composition` all reference the result.
- Segment-voice discipline clean: spike cited **only** in Working Notes at
  `der-class-coercion-via-wrapping.md:157` ("Reasoning-trail provenance"),
  not as backing for promoted content.

Only non-canon content = the deliberately-deferred sub-spikes E (tempo
accounting) and G (quantitative LLM bounds), honestly recorded as future work
in `99-verdict.md §5` with explicit "these deferrals do not block the verdict
because…". Correctly-recorded not-in-canon, not orphaned truth.

**Verdict: CONFIRM.** (Directory spike — per `spike-routing.md` §6 the parent
surfaces in the Joseph batch rather than auto-files; the *content* claim is
verified sound and carries no Joseph-reserved theory decision.
`INTEGRATION-PLAN.md` travels with the dir.)

## 5. `track-b-nonlinear-sims/` — CONFIRM `integrated-misfiled`

Strengthen-before-soften exemplar. Original sim2 exponent ~1.05 (surface
no-go vs Cor 11.2); `variants/variant_ab_results.md` shows it was a
coupling-mechanism artifact (noise-variance vs deterministic-drift ρ); Variant
A confirmed b→2.000 coupling-dominant **and** surfaced Model S b=3/2.
Verified landed first-hand in `result-adversarial-tempo-advantage.md`
(`status: conditional`):
- `:26-38` Model D, b=2; `:40-54` Model S, b=3/2 (+ "Why 3/2 not 2"
  mechanism); `:56-66` regime-dependence table with coupling-dominant
  qualifier carried as load-bearing; `:70-74` both coupling-dominant
  exponents *exact* conditional on disturbance model; `:90` the 0.019
  simulation gap explained by a derivable finite-ν correction (= the
  variant_ab finding). Sim validation cross-referenced `:66`/`:72` to
  `#result-adversarial-exponent-regimes`.

`sim*.py`/`.npz`/`.png` are reproducibility provenance; nothing of the
simulations' truth is spike-only.

**Verdict: CONFIRM.** No reserved decision.

## 6. `track-a-intent-dag/` — CONFIRM `integrated-misfiled` (archaeology)

`00-intent-dag-formalism.md` header verified: "First formal sketch of the
core novel object in AAT", March 2026, depends TF-00…TF-11 — pre-AAT genesis
trail. INDEX:163 verified: consolidated form `_obs/04-intent-dag-consolidated.md`
"converged into the strategy-DAG segments (`#def-strategy-dag` etc.).
**Archaeology** — moved to `_obs/` 2026-04-28." Verified first-hand:
`_obs/04-intent-dag-consolidated.md` present; canonical
`def-strategy-dag.md` + `def-shared-intent.md` exist in `01-aat-core/src/`
(chosen formalism *is* canonical). `01-conference-paper-review.md` is a
finished negative prior-art screen; `02`/`03`/`04` are superseded
alternatives whose chosen path is canonical. Nothing orphaned on the math
axis.

**Verdict: CONFIRM.** Genesis archaeology; consolidated form already
`_obs/`-archived; chosen formalism canonical. (Directory spike — §6 Joseph
batch for the *filing*; the cross-domain genesis-provenance value is the
reason the dir-spike gold gate protects it, but no Joseph-reserved *theory*
decision attaches; mechanical otherwise.)

---

## Caveats carried for the parent (concurrences, not refutes; non-blocking)

1. **`spike-attention-causal-graphs` `git mv` is coupled** to the
   Joseph-reserved `spike-attention-governance` decision (same `446c7a1`
   overnight residual cluster). Content-claim CONFIRMED; do **not** fire its
   `git mv` independently of resolving the governance spike. This restates the
   S5 adjudicator's own "flagging, not routing the pair" — surfaced here so
   it is not lost crossing the gate.

2. **`class-coercion-wrapping/` and `track-a-intent-dag/` are directory
   spikes.** Their content-claims are CONFIRMED sound, but per
   `spike-routing.md` §6 (lighter dir-spike gold gate) the *filing decision*
   is read-and-recommend → Joseph batch, not parent auto-file. Neither
   carries a Joseph-reserved *theory* decision (unlike the excluded
   `temporal-nesting-rg/`), so the recommendation is a clean
   `integrated-misfiled`; only the dir-spike batch-routing convention gates
   the actual `git mv`.

## Method note (gate honesty)

Every CONFIRM rests on opening the named `src/` locus and reading the
content, plus an independent grep/pickaxe where it sharpened the test (the
mean-field-VMP exclusion check and the attention-residual-absence check were
*adversarial* — run to try to refute, returned clean). Provenance was used as
the §7-sanctioned non-destructive instrument: `--follow --diff-filter=A` for
spike-creation, pickaxe `-S` for content-entry, with sweep-poisoned recency
explicitly discounted (the AAD→AAT rename rewrites slugs/paths; recency says
nothing — content-presence is the decisive test and it was met in all six).
No disposition was reached by trusting the INDEX label or the adjudication's
own summary.
