# PROPOSED — the spike-proposal index

A low-friction, optional repository for **spike-able ideas set down for later** (and their later disposition), across all three perspectives — *not* an exhaustive registry of every possible spike (see "Not a mandatory registry" below):

- **moonshot / cross-cutting / theory-edge** — detail in [`PROPOSED-ADVANCED.md`](PROPOSED-ADVANCED.md);
- **segment-perspective strengthenings** — detail stays in the relevant segment's Working Notes (the index links to it; the Working Note links back here — no duplication);
- **residual** (a real un-started spike, neither moonshot nor segment-tied) — detail in [`PROPOSED-MISC.md`](PROPOSED-MISC.md).

This file is a *navigator*, not detail. It is durable — it is **not** routed/moved like a spike — but "durable" governs *placement*, **not** *content-currency*.

**Not a mandatory registry — and deliberately so.** Spikes by convention are launchable by anyone for any reason with **no administrative friction beyond "go ahead and spike it in `spikes/`"**. This file does not change that. It is the trusted, low-friction place to *set down* a spike-able idea you don't have time to execute in the moment — a convenience, one of several parallel ways an idle agent can find work (the others, deliberately *not* routed through here: open **gaps / theory-edges** via the OUTLINE-GAP and `impl-*` layer; and scanning segment `type:`/Epistemic-Status for any segment **below its theoretical epistemic cap** — a `hypothesis` that could go empirical, a `conditional` that could shed a condition, a `discussion-grade` that could be derived — and just spiking the attempt). **Completeness is *not* required**: not every spike-able idea need have a row here, and no one is obligated to register one before spiking. The two disciplines that *do* bind (full statement in [`../doc/spike-routing.md`](../doc/spike-routing.md) §2-bis(3) + Refinement 10) are about keeping what *is* here trustworthy, not exhaustive:

1. **Freshness (no stale lies).** What is here stays true. A resolving spike sets its row to a terminal status + canon link at cycle-commit time (a stale "open" row for a landed direction is a navigator-level §4.1 lie); landed rows are **kept** (terminal status), not retired — the index doubles as a durable "where did this direction go" trail. New directions get added when convenient; the corpus *may* be periodically re-scanned, but a freshen is opportunistic, not a standing completeness obligation.
2. **Mutual link.** Where a segment Working-Note strengthening/spike-proposal comment *and* a row here describe the same effort, they link to each other (the row → its detail home; the WN comment → its tier). This is the disciplined part — it keeps the two views consistent — but it governs links between things that *are* tracked, not a duty to track everything. Efforts *owned elsewhere* (the §D.9 portfolio, ROUTING "Next actions", a live spike) are cross-referenced, not duplicated.

**Status vocabulary** (ad-hoc, descriptive, extend as needed): `proposed` (un-started) · `in-progress` · `interrupted` (started, set down) · `landed→#seg` · `split` (core landed, remainder open) · `reserved→home` (owned elsewhere) · `superseded` · `archived` (resolved as no-go, in canon). **Source**: `ADV` → PROPOSED-ADVANCED · `seg:<slug>` → that segment's Working Notes · `MISC` → PROPOSED-MISC · `xref:<home>` → owned elsewhere.

---

## Tier 1 — near-term / high-value (repair- or closure-shaped)

*Tentative sequence: #12 and Q1 are the cheapest closed-form wins; #11 is the highest-value (ELI-core, protection-strategy-relevant); #4-strengthening and #2-promotion are heavier.*

| Added | Name | Source | Description | Status | Updated | Details |
|---|---|---|---|---|---|---|
| 2026-05-19 | Substrate-transfer-asymmetry origin (or 3-way no-go) | seg:hyp-substrate-transfer-asymmetry | Discriminate A (M3/Čencov coordinate-forcing) / B (decompression-cost asymmetry) / C ($(\kappa,\mathcal A)$ channel-collapse) for the observed frontier→local $S_{\text{id}}$ asymmetry, or a deeper no-go; lifts a `discussion-grade` hypothesis to `derived` | proposed | 2026-05-19 | [ADV §Phase-3 #11](PROPOSED-ADVANCED.md) → WN of `04-eli-core/src/hyp-substrate-transfer-asymmetry.md` |
| 2026-05-19 | Effects-spiral eigenvalue condition — concrete agent classes | seg:deriv-strategic-composition | Derive the joint-Jacobian spectral-abscissa instability condition in closed form for two Beta-Bernoulli agents on a shared DAG and two coupled Kalman agents; upgrades `#der-adversarial-destabilization`'s Effects-Spiral from discussion-grade to `derived` | proposed | 2026-05-19 | [ADV §Phase-3 #12](PROPOSED-ADVANCED.md) → `deriv-strategic-composition:195` |
| 2026-05-19 | SCC-defect-constant tightness (A1 Q1) | seg:def-strategy-dag | Two-shared-node Beta-Bernoulli worked instance ($A\prec B$ vs $B\prec A$) deciding whether the $\lvert S\rvert\log 2$ ceiling is tight under non-deterministic intra-SCC coupling; lifts the strategy-DAG-composition law `conditional`→`exact` | proposed | 2026-05-19 | `def-strategy-dag` Working Notes ("Open (composition defect-constant tightness)") |
| 2026-04-25 | Mechanism-design impossibility — VCG/cardinal-utility strengthening | ADV | GS no-go core is in canon (candidate adjacent identifiability-floor instance); the §7 VCG / transferable-utility / Myerson-Satterthwaite strengthening is orphaned in `spike-alignment-impossibility.md` (strengthen-first-HEAVY; "must not be softened to done") | split | 2026-05-19 | [ADV #4](PROPOSED-ADVANCED.md) ; xref `spike-alignment-impossibility.md` |
| 2026-04-25 | Symbiogenesis bifurcation — promotion repair | ADV | Concept landed at `#hyp-symbiogenic-composition` (`robust-qualitative`); the specific repair — quadratic coordination term rigorously derived from MI loss in `#def-shared-intent`, promoting the saddle-node bifurcation to formal — is genuinely open | proposed | 2026-05-19 | [ADV #2](PROPOSED-ADVANCED.md) |
| 2026-05-19 | Modularity → strategic-asymmetry game theory | seg:disc-adversarial-coupling-pressure | Two-agent repeated game in own/opponent $\kappa_{\text{processing}}$; equilibrium predicting modularity arms races / asymmetric-advantage cascades / defensive-scaffolding incentives. Distinct from the scoping-only `spike-strategic-self-coupling.md` | proposed | 2026-05-19 | [ADV §Phase-3 #13](PROPOSED-ADVANCED.md) → `disc-adversarial-coupling-pressure:131` |
| 2026-05-22 | RGM-grounded promotion of `#sketch-multi-timescale-stability` (Friston 2025) | seg:sketch-multi-timescale-stability | Read Friston-Heins-Verbelen-Da Costa 2025 *Scale-free active inference* §3-5 (RG construction + scale-invariance proofs); map RGM's renormalization step onto AAT's template-stacking pattern; derive a multi-timescale sector-persistence template under RG-invariance; identify scope conditions. Direct supplier of formal machinery for PRACTICA cycle priority #3 — lifts `#sketch-multi-timescale-stability` from sketch to conditional-derived (or exact, depending on AAT-vs-RGM state-space alignment) | proposed | 2026-05-22 | [`spike-integration-reconciliation-2026-05-22/99-verdict.md` §5 Phase 7] → `#sketch-multi-timescale-stability` Working Notes |

## Tier 2 — exploratory / next-generation

*Tentative sequence: #9 is gated on #3 (transient-dependency) resolving first.*

| Added | Name | Source | Description | Status | Updated | Details |
|---|---|---|---|---|---|---|
| 2026-04-25 | Transient dependency amplification / logogenic Lipschitz | ADV | Feature-local effective dependency operator $J_F$ bounding a contribution to $L_A$; spike exists but author is self-blocked on the formal $J_F$ construction | interrupted | 2026-05-19 | [ADV #3](PROPOSED-ADVANCED.md) ; live `spike-transient-dependency-amplification.md` |
| 2026-05-19 | AAT ↔ replicator / evolutionary-game-dynamics correspondence | seg:deriv-strategic-composition | Characterize which AAT-native update rules induce strategic dynamics matching replicator; connect strategic composition to ESS theory (Sandholm 2010) | proposed | 2026-05-19 | [ADV §Phase-3 #14](PROPOSED-ADVANCED.md) → `deriv-strategic-composition:203` |
| 2026-05-19 | Mixture-support dynamics under the Orient cascade (A1 Q2) | seg:def-strategy-dag | Whether the L1′-mixture fallback's support can grow under cascade-driven shared-sub-order revision, or stays SCC-count-bounded | proposed | 2026-05-19 | `def-strategy-dag` Working Notes ("Open (mixture-support dynamics)") |
| 2026-04-25 | Mean-field-game limit for population dynamics | ADV | $N\to\infty$ AAT agents via MFG; Fokker-Planck-Kolmogorov ⊗ HJB for population $M_t$ density (Lasry-Lions; Huang-Malhamé-Caines) | proposed | 2026-05-19 | [ADV #7](PROPOSED-ADVANCED.md) |
| 2026-04-25 | Topology-dependent hallucination propagation (percolation) | ADV | Critical edge-reliability / checkpoint-coverage threshold $p_c$ for a hallucinated premise reaching a giant affected component | proposed (gated on #3) | 2026-05-19 | [ADV #9](PROPOSED-ADVANCED.md) |
| 2026-04-25 | Quantum causal DAGs for logogenic superposition | ADV | Density-matrix context state; self-attention as quantum-like interference across strategy branches; CIY via von Neumann entropy | proposed | 2026-05-19 | [ADV #10](PROPOSED-ADVANCED.md) |
| 2026-05-22 | Categorical-cybernetics first fit-check (Capucci 2022 + Smithe 2024) | ADV | First of a 3-5-spike sequence — *fit-check only*: does the parametrised-optic / selection-function framework actually align cleanly with AAT's existing composition machinery, or do they pull in incompatible directions? Specifically: does `#form-composition-closure` admit a parametrised-optic formulation? Honest scope: exploratory; recognition-tier landing is easy, substantive integration requires the spike sequence | proposed | 2026-05-22 | [ADV §Phase-3 #15](PROPOSED-ADVANCED.md) → `#form-composition-closure` Working Notes |

## Tier 3 — segment-perspective audit-judgments

| Added | Name | Source | Description | Status | Updated | Details |
|---|---|---|---|---|---|---|
| 2026-05-19 | `der-turnover` novelty-vs-subsumed (C10) | seg:der-turnover-information-recursion | Is R1/R2 a genuinely new $\mathcal A_D$ object or a bridge-lemma-resolvent instance? Test-not-assert; resolving "subsumed" demotes the segment to a worked instance | proposed | 2026-05-19 | `der-turnover-information-recursion:129` Working Note ; trail `RECONCILIATION.md` §4 |
| 2026-05-19 | $U_O$ → sector-constant (UO-mult) derivation | seg:result-unity-closure-mapping | Action-space inner-product analysis (action-coupling operator; LQR cross-actions ∝ target correlation; pin $\gamma_{\max}$ via the quadratic-objective Hessian + environment coupling gain) upgrading the (UO-mult) channel $\gamma(U_O)=-\gamma_{\max}U_O$ in `#deriv-critical-mass-composition` §5.2 from discussion-grade to derived | proposed | 2026-05-19 | `result-unity-closure-mapping` Working Notes ("$U_O$ → sector-constant pathway") |
| 2026-05-19 | Quantitative CLS instantiation of consolidation dynamics | seg:form-consolidation-dynamics | Work out (N1)+(N2) for a specific CLS-like architecture (sparse-conjunctive + distributed-overlapping at given capacity ratios), deriving the online-only no-go as a rate-distortion bound + a quantitative stability-upper-bound for the feasibility window | proposed | 2026-05-19 | `form-consolidation-dynamics` Working Notes ("Quantitative CLS instantiation") |
| 2026-05-19 | R2 detection-latency sharpening under model-class inadequacy | seg:deriv-update-detection-latency | Compute the common-mode bias as a function of `#result-mismatch-decomposition`'s model-error component, show it is $O(1)$ (not $O(\varepsilon)$) under directional misspecification, derive a convention-dependent detection latency (one-evening spike) | proposed | 2026-05-19 | `deriv-update-detection-latency` Working Notes ("R2 sharpening (model-class inadequacy)") |
| 2026-05-19 | Code-quality bistability — 2D dynamical formalization | seg:der-code-quality-as-observation-infrastructure | Formalize the strong-but-unformalized bifurcation claim via a 2D $(Q,\mathcal T)$ system $\dot Q=g(\mathcal T,Q)$; two attractors separated by a separatrix would make the vicious/virtuous-cycle claim a formal result (TST-side; spike or simulation) | proposed | 2026-05-19 | `der-code-quality-as-observation-infrastructure` Working Notes |
| 2026-05-19 | Adversarial adaptive-gain — meta-gain tempo-advantage analog | seg:deriv-adaptive-gain-dynamics | Derive the meta-gain-level adversarial-tempo-advantage condition ($\alpha_K T_{\text{dwell}}$ vs adversarial $K^\ast$ regime-switching rate); currently asserted "not derived here; adjacent spike" with the dwell-time repair of Case C failing under hostile regime-switching | proposed | 2026-05-19 | `deriv-adaptive-gain-dynamics` Working Notes ("Adversarial adaptive-gain") |

## Reserved / owned elsewhere (cross-ref — discoverable here, owned there)

*Listed for completeness (discipline 1); **not** owned by this index — the owning home is authoritative. Do not duplicate detail here.*

| Name | Owned by | Status |
|---|---|---|
| Object-B / Instance-4 / CL-2-heavy unification | [`../PROPOSALS.md`](../PROPOSALS.md) §D.9 + PRACTICA item 7 | reserved (Joseph) |
| CL-1 `#dissipativity-template` (passivity-composition + pid-a2prime + bridge §7.2) | `ROUTING.md` "Next actions" §2 / PROPOSALS §D.9 | queued-heavy |
| `spike-update-operator-sector` tractable landing | `ROUTING.md` "Next actions" §3 | regression-cleared, pending |
| Continuity §4.2 second-no-go (adversarially-correlated reinjection) | `der-identity-continuity-threshold:130` ; `der-resource-bounded-destabilization` WN ; `form-resource-budget` WN | reserved (Joseph) |
| `spike-strategic-self-coupling` (scoping/prior-art only — no results) | live `spikes/spike-strategic-self-coupling.md` ; INDEX 2026-05-09 | open-direction |

## Tier 4 — landed / terminal (historical register — kept, not retired)

| Added | Name | Description | Status | Updated |
|---|---|---|---|---|
| 2026-04-25 | Causal-IB LMI | The LMI-over-Fisher exploration repair | landed→`#deriv-causal-ib-lmi` | 2026-05-19 |
| 2026-04-25 | Message-passing credit assignment | EP / loopy-BP / Max-Sum + L1 floor; refuted mean-field-VMP core excluded | landed→`#disc-credit-assignment-boundary` | 2026-05-19 |
| 2026-04-25 | FEP as sub-optimal approximation | Conditional objective-comparison (not a dominance theorem); scope-honored | landed→`#disc-ciy-unified-objective` | 2026-05-19 |
| 2026-04-25 | Landauer / thermodynamic cost of $M_t$ preservation | $\dot R_{\min}\ge n\alpha/2$ nats/time Landauer-analog rate bound | landed→`#deriv-persistence-cost` | 2026-05-19 |

## Misc / process (PROPOSED-MISC)

| Added | Name | Source | Description | Status | Updated |
|---|---|---|---|---|---|
| 2026-05-19 | Reciprocal-link enforcement check | MISC | A `bin/` grep-check flagging WN strengthening/spike-proposal language lacking a `PROPOSED` back-link — the teeth for discipline 2 (dogfood: this is itself an indexed un-started effort) | proposed | 2026-05-19 |
| 2026-05-19 | Working-Note strengthening sweep | MISC | One-time corpus sweep adding index rows + reciprocal back-links for all WN strengthening comments not yet linked (beyond the known Q1/Q2/C10) | done (2026-05-19) | 2026-05-19 |

Detail for the two rows above: [`PROPOSED-MISC.md`](PROPOSED-MISC.md).
