# PROPOSED — the spike-proposal index

The single discoverable register of **known un-started (or in-flight, or terminally-resolved) spike efforts**, across all three perspectives:

- **moonshot / cross-cutting / theory-edge** — detail in [`PROPOSED-ADVANCED.md`](PROPOSED-ADVANCED.md);
- **segment-perspective strengthenings** — detail stays in the relevant segment's Working Notes (the index links to it; the Working Note links back here — no duplication);
- **residual** (a real un-started spike, neither moonshot nor segment-tied) — detail in [`PROPOSED-MISC.md`](PROPOSED-MISC.md).

This file is a *navigator*, not detail. It is durable — it is **not** routed/moved like a spike — but "durable" governs *placement*, **not** *content-currency*: it is a standing navigator-reconciliation target. The disciplines (binding; full statement in [`../doc/spike-routing.md`](../doc/spike-routing.md) §2-bis(3) + Refinement 10):

1. **Completeness.** Every known un-started spike effort is represented by a row here. Efforts *owned elsewhere* (the Joseph-reserved §D.9 portfolio, ROUTING "Next actions", a live spike) are **cross-referenced, not duplicated** — the row points at the owning home so the effort is discoverable without a competing home.
2. **Reciprocal links.** Every segment Working-Note strengthening / spike-proposal comment links to its row's tier here; every row links to its detail home. A WN strengthening comment with no back-link is a discipline violation an audit grep should catch (`#sw-reciprocal-link-check`, MISC).
3. **Bidirectional reconciliation.** *Down*: a resolving spike sets its row to a terminal status + canon link at cycle-commit time (a stale "open" row for a landed direction is a navigator-level §4.1 lie). *Up*: the corpus is periodically re-scanned for newly-surfaced undone directions, which are added. Landed rows are **kept** (terminal status), not retired — this index doubles as the durable "every proposed direction and where it went" audit trail.

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

## Tier 3 — segment-perspective audit-judgments

| Added | Name | Source | Description | Status | Updated | Details |
|---|---|---|---|---|---|---|
| 2026-05-19 | `der-turnover` novelty-vs-subsumed (C10) | seg:der-turnover-information-recursion | Is R1/R2 a genuinely new $\mathcal A_D$ object or a bridge-lemma-resolvent instance? Test-not-assert; resolving "subsumed" demotes the segment to a worked instance | proposed | 2026-05-19 | `der-turnover-information-recursion:129` Working Note ; trail `RECONCILIATION.md` §4 |

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
| 2026-05-19 | Working-Note strengthening sweep | MISC | One-time corpus sweep adding index rows + reciprocal back-links for all WN strengthening comments not yet linked (beyond the known Q1/Q2/C10) | in-progress | 2026-05-19 |

Detail for the two rows above: [`PROPOSED-MISC.md`](PROPOSED-MISC.md).
