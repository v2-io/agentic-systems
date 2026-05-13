# NeurIPS 2026 Back-Integration into ASF — Overview

*Drafted by Tessera (Claude Opus 4.7, 1M context) at Joseph's request, 2026-05-08, after a multi-session deep read covering ASF (README, OUTLINE, Section I/II/III canonical segments, msc/FINDINGS-RANKED-DRAFT.md, key Part-3 and Part-4 segments) followed by a focused read of the three NeurIPS 2026 submissions in `~/src/neurips/` (intros, main results, mechanisms, conclusions, related-work; OUT manifests; meta abstracts). The cross-mapping between paper content and source segments is held in working memory at write-time and would decay across sessions without externalization. Hence this artifact.*

*Scope: not a prescription for what should be done — Joseph's call. An overview of what the integration **looks like** if pursued, organized so that any subsequent integration agent (Claude, Codex, Gemini, future-Joseph) can locate where each piece belongs without re-reading the papers from scratch.*

*Honest caveats up front:*
- *Most of the integration claims below are inferences from the paper text against the segment text; some are inferences against catalog entries I read but not against the underlying segments at full depth (e.g., the spike reports I haven't read, the derivation chains I read only the headline of). Where this matters, I name it as such.*
- *Several "would warrant" items are judgment calls about whether to merge into existing segments, spin out new segments, or capture as spike material. I name the trade-offs but do not recommend a single answer; the segment-vs-spike-vs-cross-segment routing is the kind of structural question Joseph and the audit cycles handle.*
- *The strengthen-before-soften discipline applies to this artifact too: where a paper sharpened ASF's looser claim, the back-integration should propagate the sharpening, not just record that the paper exists. Several catalog tier-list entries are now provably stronger than the catalog states.*

---

## 1. The three papers as extractions, with source-segment mapping

The papers in `~/src/neurips/` extracted three ASF results, refined them under adversarial scrutiny over the 2026-05-04 → 2026-05-07 sprint, and submitted them as standalone NeurIPS Main Track contributions. Each is an *extraction-and-refinement*, not a copy: the paper version is materially sharper than the catalog version on multiple axes.

### Paper 1: `01-tragedy-confident-agent` ←→ AAD source segments

**Paper title:** *Tragedy of the Confident Agent: Forced Exploration for Survival in Drifting Environments*

**Catalog finding:** Tier 1 #4 (Tragedy of the Confident Agent — two exploration drives at opposite ends of $U_M$).

**Source segments:**
- `01-aad-core/src/deriv-causal-ib-exploration.md` — the scalar survival-imperative exploration drive.
- `01-aad-core/src/deriv-causal-ib-lmi.md` — the matrix lift via Linear Matrix Inequality on the Fisher Information Matrix.
- `01-aad-core/src/result-persistence-condition.md` — the underlying $\alpha > \rho/R$ inequality.
- `01-aad-core/src/result-sector-condition-stability.md` — the sector-Lyapunov machinery.
- `01-aad-core/src/scope-agent-identity.md` — the singular-trajectory commitment.

**What the paper added that ASF should absorb:**

1. **The KKT shadow-price / controller-divergence resolution** (Paper §5 Mechanism Step 4 + Appendix on KKT Lagrangian). The static-program LP multiplier on the survival constraint is *finite* (LP slope), but the survival-margin controller family in Definition 4.1 has *divergent* gain. The paper resolves this as: *the controller's λ_surv divergence is a controller-design overshoot of the finite multiplier, ensuring the controller's response loop closes inside the finite worst-case exit-time window from Lemma 2.1(ii)*. Divergence is on the environment-side clock, not the controller-side multiplier. This is a non-trivial conceptual move that ASF's catalog framing does not currently distinguish — `#deriv-causal-ib-exploration` says λ_surv ∝ 1/U_M "diverges as confidence rises" without naming the static-vs-multi-step distinction.

2. **The pathwise-vs-expectation gap with explicit per-action LMI strengthenings.** Paper §4 Theorem 4.1.1 controls only the steady-state DARE under expected FIM, not per-step P_t under realized draws. Paper §App-A.6 (`#thm-per-action-lmi`, `#thm-per-action-lmi-iid`) close the gap with deterministic pathwise survival under arbitrary action schedules. The matrix-Chernoff lemma `#lem-fim-concentration` gives the parallel high-probability bound. ASF's `#deriv-causal-ib-lmi` does not surface this gap explicitly.

3. **The F-A-G-P enforcement framework** for the survival-margin controller family — Strict feasibility / drift-Aligned bonus / Gain dominance / argmax-Presentable. Paper §App-A.7 (`#prop-fagp`). This is a clean operational decomposition of what it takes for a controller to be a valid family member; ASF's catalog refers to "λ_surv ∝ 1/U_M" as illustrative without naming the four enforcement conditions.

4. **The exit-time bound** $T_{\text{exit}}(\delta_0) \leq \frac{1}{\alpha+\gamma}\log\frac{\rho/(\alpha+\gamma) - \|\delta_0\|}{\rho/(\alpha+\gamma) - R}$ (Paper §3 Lemma 2.1(ii)). ASF's `#result-persistence-condition` mentions structural-vs-task-adequacy decomposition but doesn't carry the worst-case finite exit-time witness. The exit-time bound is what the controller-design overshoot is justified against; without it, the divergent-gain resolution doesn't quite work.

5. **The anisotropic-drift dependence** with closed-form critical exponent $p_{\text{crit}}$ for the $\Lambda \propto \mathcal{I}_{\min}^p$ refinement, diverging as $\sigma_x/\sigma_y \to 1$ (Paper §App-C: anisotropic extension). The matrix-LMI directional-discrimination value rests on anisotropic drift; under near-isotropic drift the argmax flips. ASF's `#deriv-causal-ib-lmi` does not carry this caveat.

6. **The bistable Pareto frontier** as a real characterization of discrete-action-set controllers, distinct from a smooth survival-vs-reward tradeoff (Paper §App-B: bistable-artifact appendix). Useful for ASF segments that touch on "survival vs reward" framings — the bistability is a feature of the discrete action set, and characterizing it explicitly prevents future overclaiming about smooth Pareto frontiers.

7. **The 2D Gaussian empirical anchor** with the `wall_extreme` ε-blank-wall action (FIM diag(0.0625, 25)), the three-controller comparison (greedy / scalar / LMI), and the survival-rate-vs-σ_w table. This is the simulation that validates the directional-discrimination claim. ASF's spike `track-b-nonlinear-sims/variants/variant_causal_ib.py` carries the underlying simulation; the paper's specific 2D version with the three-controller comparison is a refinement worth referencing back.

### Paper 2: `02-unified-convergence-rl` ←→ AAD source segments

*[Back-integration progress, 2026-05-12: ELI-8 cycle landed `#deriv-identity-sufficiency-rate-bound` which carries a Working Note cross-reference to Paper 2's IB-Lagrangian instantiation in `#form-information-bottleneck` — the rate-distortion structure of $S_{\text{id}}$ parallels Paper 2's IB strengthening, both M3 instances of the additive-coordinate-forcing family. The cross-reference is in place; Paper 2's other source-segment touchpoints (`#def-satisfaction-gap` + `#def-control-regret` two-gap diagnostic; `#schema-strategy-persistence` + `#def-strategic-tempo` strategic tempo with forgetting prerequisite; `#deriv-strategy-cost-regret-bound` $\pi^*$-first reverse-KL direction-forcing) have not yet received Phase A cross-references.]*

**Paper title:** *A Unified Convergence Theory for Non-Stationary Reinforcement Learning*

**Catalog finding:** Cross-Segment CS1 (Unified RL Convergence Theory Under Non-Stationarity).

**Source segments:**
- `01-aad-core/src/def-satisfaction-gap.md` + `def-control-regret.md` — the two-gap diagnostic (Component 1).
- `01-aad-core/src/scope-agent-identity.md` — Loop-as-Causal-Engine (Component 4).
- `01-aad-core/src/der-loop-interventional-access.md` — closed-loop interventional access (Component 4).
- `01-aad-core/src/schema-strategy-persistence.md` + `def-strategic-tempo.md` — strategic tempo with forgetting prerequisite (Component 3).
- `01-aad-core/src/deriv-strategy-cost-regret-bound.md` — the $\pi^*$-first reverse-KL direction-forcing (Component 2).

**What the paper added that ASF should absorb:**

1. **The Bretagnolle-Huber identity at deterministic-π* corner as exact equality** (Paper §5 Key Lemma 1; `#lem-pointmass-identity`). $D_{\text{KL}}(\pi^* \|\, Q) = -\log Q(a^*) = -\log(1 - \text{TV}(\pi^*, Q))$. *Strictly sharper than Pinsker and the BH inequality* at this corner. Numerical comparison in Paper §App-E. This is a real new theorem that ASF's catalog does not carry as a standalone result; it should land as a new segment (proposed slug `#deriv-bh-pointmass-identity` or `#result-pointmass-tv-kl-identity`) and be cross-referenced from `#deriv-strategy-cost-regret-bound`.

2. **The composition theorem** with five hypotheses (A1)-(A5) and five conclusions (i)-(v) (Paper §4 Theorem 4.1). The cumulative dynamic regret rate $\tilde O(V_{\max} N_h \sqrt{(B_T+1) T}) + V_{\max} N_h (1 - p_{\text{id}}) T$ is the headline. ASF's CS1 catalog entry refers to "composition of four findings" without writing the composition theorem out; the paper's version should land either as a new cross-segment segment (`#deriv-rl-composition-theorem` or similar) or as the formal expression on a strengthened CS1 segment.

3. **The Wei-Luo MASTER Best-of-Both-Worlds wrapping** for $B_T$ (piecewise-stationary) vs $V_T$ (continuous-variation) regimes, automatically adapting without prior knowledge (Paper §4 + §6). ASF's catalog does not name this wrapping move. The continuous-variation extension matches Mao 2021's near-optimal exponent; this should flow back into `#schema-strategy-persistence` or into a new segment for variation-regime handling.

4. **The structural-class theorem on gain-decay updates** (Paper §App-D: aux-decay-class). Every member of the gain-decay class $\mathcal{A}_{\text{decay}}$ (count-accumulating Bayesian without forgetting, observation-aggregating without restart, gradient-based with vanishing step) eventually violates the persistence threshold for any positive disturbance rate; finite-gain mechanisms face *bidirectional* ceilings. This is a new structural finding that strengthens `#schema-strategy-persistence` from "forgetting prerequisite" to "structural class theorem on which mechanisms must fail." Should land either as a strengthening of the existing segment or as a separate sub-segment.

5. **The (C1) positivity / (C2) sequential-ignorability / (C3) known action mechanism framework** for closed-loop interventional access (Paper §5 Key Lemma 3; `#lem-loop-level2`). This is the formalization of the Loop-as-Causal-Engine claim under named hypotheses — and (C2) explicitly notes that *goal-conditioned LLM policies violate it*, which is the bridge to Paper 3 (Class 2 / coupled formulation). ASF's `#scope-agent-identity` carries the singular-trajectory commitment; the (C1)-(C3) framework should be either added there or surfaced as a new segment that `#scope-agent-identity` and `#der-loop-interventional-access` both reference.

6. **The misidentification-penalty bias term** $V_{\max} N_h (1 - p_{\text{id}}) T$ (Paper §4 Theorem 4.1(v) + §5 Key Lemma 4 / `#lem-bias-bound`). This is a Regime A/B/C decomposition under partial identifiability — vanishes in Regime A, controlled in Regime B, saturates at trivial bound in Regime C. ASF's `#scope-ciy-observational-proxy` has Regime A/B/C structure; the misidentification-penalty version is a new dimension that should be cross-referenced.

7. **The ProST-as-impulsive-limit reduction** (Paper §5 + §App-B: proof-prost-impulsive). ProST `(Lee et al. 2023)` recovers as the impulsive limit of Model (Σ); the Hespanha-Liberzon-Teel reverse-ADT framework gives the threshold; under uniform schedules this recovers ProST's $K/T$ form with the impulse gain $\gamma$ made explicit. *Lifts ProST from tempo-as-hyperparameter to tempo-as-stability-margin*. This is a real cross-domain transfer that should propagate back to ASF either as a strengthening of `#schema-strategy-persistence` or as a new derived segment.

8. **The strategic-tempo bottleneck-not-sum aggregator argument** (Paper §5 Lemma 4.2 / `#lem-forgetting`). $\mathcal{T}_\Sigma^{\text{bn,ss}} := \min_{(i,j) \in E} \nu_{ij} \cdot \iota_{ij} \cdot (1 - \lambda_{ij})$. Adversarial disturbance concentrates on the weakest element — the same effect that makes per-dimension persistence sharper than scalar. ASF's `#def-strategic-tempo` and `#schema-strategy-persistence` should incorporate the bottleneck-aggregator argument explicitly. (Connects to `#result-per-dimension-persistence`'s weakest-link finding — same structural pattern.)

### Paper 3: `03-llm-hallucinate-bound` ←→ AAD source segments

**Paper title:** *How Much Can LLMs Hallucinate? An Upper Bound on Goal-Coupling Displacement*

**Catalog finding:** Tier 1 #8 (Logogenic Bias Bound, $\kappa \times \mathcal{A}$ as conditional theorem).

**Source segments:**
- `01-aad-core/src/deriv-observation-ambiguity-bias-bound.md` — the conditional-theorem upgrade with two tracks.
- `03-logogenic-agents/src/scope-observation-ambiguity-modulation.md` — the κ × A factorization.
- `01-aad-core/src/der-directed-separation.md` — the Class 1/2/3 architectural classification.
- `03-logogenic-agents/src/scope-channel-collapse.md` — the architectural condition for Class 3 by construction.
- `01-aad-core/src/scope-agent-identity.md` — the (PI) parameterization-invariance commitment.

**What the paper added that ASF should absorb:**

1. **The chain-rule on post-update law as bridging lemma** (Paper §5 Lemma 5.1; `#lem-chain-rule`). $\mathbb{E}_G[\text{KL}(P_{M_{\tau^+}|e,M_{\tau^-},G} \,\|\, P_{M_{\tau^+}|e,M_{\tau^-}})] = I(G;\, M_{\tau^+}|e_\tau, M_{\tau^-})$. The structural composition of the two literatures (Bayesian inverse-problems + architectural classification) meets at this identity. ASF's `#scope-observation-ambiguity-modulation` references the right-hand side as "transferred goal-information" but doesn't carry the chain-rule identity as a named bridging lemma. Should land as a derivation segment (proposed slug `#deriv-post-update-chain-rule`).

2. **Two named tracks for the constant** with explicit hypothesis sets (Paper §4 Theorem 4.1 / `#thm-umbrella`). Track 1 (transport-inequality, $W_2$ metric): $C = \sqrt{C_{T_2}}$ with $C_{T_2}$ recovering the canonical Stuart-school cascade form $\propto L_{\text{post}}^2/\rho_{\text{LSI}}$ under (H2'). Track 2 (Fisher-Rao Čencov uniqueness): $C = 2$ globally / $\sqrt{2}$ locally under (PI)+(R)+(K)+(H4'). ASF's `#deriv-observation-ambiguity-bias-bound` carries the two tracks at draft level; the paper's version is materially sharpened with the global-vs-locally-tight separation, the hypothesis names, and the witness constructions.

3. **The no-go on Euclidean chart norms** (Paper §4 Theorem 4.2 / `#thm-no-go`). Chart-rescaling argument: $\phi \mapsto a\phi$ scales chart-Euclidean $W_2$ linearly while leaving KL/MI/$d_{FR}$/Hellinger chart-invariant; taking $a \to \infty$ contradicts any candidate fixed $C_0\sqrt{I}$. *Forces (PI) as load-bearing for theorem-level status*. This is a structural result — ASF's `#deriv-observation-ambiguity-bias-bound` flagged "no universal C under Euclidean parameter norm exists" but the paper's chart-rescaling construction is the explicit witness. Should land as its own derivation segment (proposed slug `#deriv-chart-rescaling-no-go`) and become the *fourth* identifiability-floor instance in `#disc-identifiability-floor`'s M1 meta-pattern table (Paper 3's Lemma 4.2 explicitly identifies this as F4 in the M1 instance table). *[Back-integration progress, 2026-05-12: `#deriv-fisher-local-update-gain` (AAD-5 audit-strengthening cycle) carries a cross-reference Working Note pointing at this no-go as the structural forcing for (PI) — the natural-gradient direction in that derivation depends on (PI), which this no-go makes load-bearing rather than optional. The cross-reference is in place; the no-go has not yet landed as `#deriv-chart-rescaling-no-go` segment or as the F4 instance entry in M1.]*

4. **The Čencov-uniqueness-and-sharpness theorem** (Paper §4 Theorem 4.3 / `#thm-fr-uniqueness`). Under (H1)+(PI)+(R)+(K)+(H4'): $d_{\mathcal{M}}$ is uniquely the ambient Amari-Nagaoka Fisher-Rao spherical-arc distance; $C = \sqrt{2}$ is the unique sharp upper-bound constant. Sharpness via symmetric two-point witness on conjugate-Gaussian Class 1 family. ASF's `#deriv-observation-ambiguity-bias-bound` carries the Čencov reference; the paper's full uniqueness-and-sharpness package is the strengthened form.

5. **The Class 1 reduction theorem to Stuart-school setup** (Paper §App-D: Track 2 companions / `#thm-stuart-school-reduction`). The Class 1 specialization of Track 1's hypothesis space is the Stuart-school Lipschitz-posterior cascade. This is the spike-A7 finding from `03-llm-hallucinate-bound/spikes/A7-stuart-school-mapping/report.md` — the strict-strengthening that came out of overturning the parent agent's 30-second "strengthening fails" triage into a 9-minute Opus spike. Should land in ASF either as a strengthening of `#deriv-observation-ambiguity-bias-bound` or as a separate derivation segment that `#deriv-observation-ambiguity-bias-bound` references.

6. **The Coupled-class autoregressive connectivity lemma** (Paper §App-B: hypothesis-verification + `#lem-attention-coupled`). Plain decoder-only transformer attention is structurally Class 3 by directed-graph reachability — robust to RMSNorm / FlashAttention / causal masking / sliding-window. *And extended to linear attention / Mamba/SSMs / RWKV / RetNet / long-convolutions* under per-source non-degeneracy condition (`#cor-arch-instantiations`). ASF's `#scope-channel-collapse` carries the κ_processing ≈ 1 claim; the paper's induction-on-layer-depth proof and the broader architecture coverage are real refinements. Should propagate back into `#scope-channel-collapse` and/or `#der-directed-separation` Class 3 examples.

7. **The (PI)+(R)+(K) axiom triple** with explicit hypothesis statements at full Markov-morphism strength (Paper §3 Setup / `#pi-axiom`, `#r-axiom`, `#k-axiom`). ASF's `#scope-agent-identity` adopts (PI); (R) Riemannian structure and (K) KL second-order matching are not explicitly named there. The paper's three-axiom decomposition is the load-bearing structural commitment for the universal-constant route. This is consequential for the M3 additive-coordinate-forcing meta-pattern: the Fisher-metric layer's axiomatic infrastructure is more complete than the catalog suggests.

8. **The (H4') uniform local regime** (Paper §3 / `#h4-prime`) and its operational meaning. *Adversarial / rare-high-KL prompts (jailbreaks, persona injection) exit (H4')*; the global $C = 2$ bound is the operating tool for that regime. The locally-tight $\sqrt{2}$ regime operates only when goal-conditional slices are uniformly close to the goal-marginal. This is a new operational distinction not named in ASF's `#scope-observation-ambiguity-modulation`, and it has direct safety-engineering implications worth surfacing.

9. **The closed-form JSD estimator for binary-uniform two-goal probing** (Paper §4 Corollary 4.4 + §6). For $G \in \{g_1, g_2\}$ uniform, $I(G;\, M_{\tau^+} \mid e_\tau, M_{\tau^-}) = \text{JSD}(P_{M_{\tau^+}\mid g_1},\, P_{M_{\tau^+}\mid g_2})$. *Sharma et al. 2023's answer-sycophancy metric is essentially this binary-uniform probe*. The bound becomes operational once $\kappa^*$ is bounded. ASF's `#scope-observation-ambiguity-modulation` flags the empirical estimator $\hat{\mathcal{A}}$ for ambiguity but not the JSD-on-transferred-information form. Should propagate.

10. **The Owhadi-Scovel-Sullivan brittleness no-go distinction** (Paper §4 Remark on `#thm-no-go`). The chart-rescaling no-go is *adjacent in shape but opposite in direction* to OSS Bayesian-brittleness results — OSS is for *arbitrary stability under finite information* in fixed metrics; the paper's no-go is for *a universal constant absent a coordinate-invariance commitment*. The two no-gos constrain different things; neither implies the other. Useful framing for `#disc-identifiability-floor`'s M1 meta-pattern when surfacing the F4 instance.

---

## 2. Cross-cutting framework-level patterns

Beyond the per-result back-integration, three structural moves appear across all three papers and would benefit from being named at the meta-architectural level. These are *patterns the papers established under adversarial scrutiny*; ASF could absorb them as conventions rather than per-segment additions.

### 2.1 Structural-backbone-vs-operational-corollary discipline

Each paper separates the unconditional theorem from the operational reading.

- **Paper 1**: the survival LMI sufficient condition (Theorem 4.1.1) is structural; the survival-margin controller family (Definition 4.1) is operational.
- **Paper 2**: the composition theorem (Theorem 4.1) is structural; the $\sqrt{(B_T+1)T}$ rate (conclusion v) is operational.
- **Paper 3**: the umbrella bound (Theorem 4.1) is structural; the architectural factorization corollary (Corollary 4.4) is operational under (H_κ).

In each case, the structural form holds without architectural commitment; the corollary brings the architecture in. ASF's catalog tends to run the operational reading and the structural backbone together; the papers separate them, and the separation is real. **Recommendation**: when extracting future ASF results to publication, lead with the structural-unconditional version and append the operational corollary. Possibly worth a meta-segment naming this as a discipline (or simply an addition to `FORMAT.md` §Findings-shaped-presentation).

### 2.2 Two-named-regimes pattern

Each paper has two named regimes/tracks decomposing the result.

- **Paper 1**: Model D (deterministic-bounded) vs Model S (stochastic Gaussian).
- **Paper 2**: $B_T$ (piecewise-stationary by direct aggregation) vs $V_T$ (continuous-variation by MASTER wrapping).
- **Paper 3**: Track 1 (transport-inequality cascade, $W_2$ metric) vs Track 2 (Fisher-Rao Čencov, $d_{FR}$ metric).

The two-track structure consistently lets the paper claim the strongest result in each named regime without overclaiming any single one. This is structurally the same separability-pattern (M2) discipline at fine grain. The pattern could be named explicitly in `#disc-separability-pattern` as an operational recommendation: "results that look monolithic are often two-track separations not yet decomposed." Useful for future segment work.

### 2.3 No-go-forces-axiom pattern

Each paper has a structural argument that forces the load-bearing axiom.

- **Paper 1**: the blank-wall attack on the scalar form forces the matrix LMI lift with directional Λ.
- **Paper 2**: forward-KL is +∞ whenever Q has off-optimum mass and is therefore vacuous; this *forces* the reverse-KL direction (the (A1) extended-real reading is what makes the identity hold even at Q(a*)=0).
- **Paper 3**: chart-rescaling no-go on Euclidean chart norms forces (PI) as load-bearing for any universal-constant claim.

This is structurally the M1 identifiability-floor pattern at finer grain. **Each paper has its own M1-instance built in**, where the external no-go (architectural / metric / coordinate) names exactly what additional axiom is required to make the result work, and the framework axiom lands as the unique escape. Worth surfacing as a fifth M1 instance? Or as a refinement of M1 to "every load-bearing AAD axiom has a no-go that forces it"? Recommend Joseph's call.

---

## 3. New material that doesn't fit existing segments

Material in the papers that doesn't have a clean home in existing segments. Either new segments or expansions of catalog entries are warranted.

| Paper material | Proposed home | Notes |
|---|---|---|
| Bretagnolle-Huber identity at deterministic-π* corner | New segment `#deriv-bh-pointmass-identity` (or `#result-pointmass-kl-tv-identity`) under §A Appendices | Real new theorem; cleanest as standalone |
| Chain-rule on post-update law | New segment `#deriv-post-update-chain-rule` under §A | Bridging lemma; cited from `#deriv-observation-ambiguity-bias-bound` and elsewhere |
| Chart-rescaling no-go | New segment `#deriv-chart-rescaling-no-go` under §A; F4 instance entry in `#disc-identifiability-floor` | Forces (PI); also belongs in M1 pattern |
| (C1)-(C2)-(C3) sequential-ignorability framework | Either expansion of `#scope-agent-identity` or new `#scope-sequential-ignorability` | Bridge to Paper 3's Class 3 case |
| Wei-Luo MASTER B_T/V_T wrapping | Either expansion of `#schema-strategy-persistence` or new `#deriv-variation-regime-bow-wrapping` | Domain instantiation of the two-track separability |
| Class 1 reduction to Stuart-school | Strengthening of `#deriv-observation-ambiguity-bias-bound` (Track 1 hypothesis space sub-cases) | A7 spike report is the substrate |
| Structural-class theorem on gain-decay updates | Strengthening of `#schema-strategy-persistence` | Real new structural finding |
| ProST-as-impulsive-limit reduction | Domain segment in `02-tst-core/` or as a worked example in `01-aad-core/src/example-*` | Cross-domain transfer instance |
| Coupled-class autoregressive lemma | Expansion of `#scope-channel-collapse` and `#der-directed-separation` Class 3 examples | The induction-on-depth proof + broader architecture coverage |
| Owhadi-Scovel-Sullivan brittleness distinction | Discussion under `#disc-identifiability-floor` F4 instance | Useful for adjacent-but-distinct framing |
| Sycophancy as binary-uniform two-goal probe | Discussion under `#scope-observation-ambiguity-modulation` and/or in §06 ELI Sources of Operational Reference | Direct empirical-bridge claim |

---

## 4. Spike material that should be captured

Several spike-report-grade investigations from the NeurIPS sprint are not yet in `agentic-systems/spikes/` — they're in `~/src/neurips/{0N-paper-name}/spikes/`. Each is the kind of strengthening-attempt-with-payoff record that the framework's discipline says should survive. Recommend cross-referencing rather than copying (the canonical home is the paper's spike directory; ASF can link from a spike-INDEX entry).

| NeurIPS spike (canonical location) | ASF reference home |
|---|---|
| `01-tragedy-confident-agent/spikes/...` (KKT-divergence-vs-LP-multiplier resolution) | `spikes/INDEX.md` cross-reference + working note in `#deriv-causal-ib-exploration` |
| `01-tragedy-confident-agent/spikes/...` (per-action LMI strengthenings; pathwise-vs-expectation gap) | `spikes/INDEX.md` cross-reference |
| `02-unified-convergence-rl/spikes/...` (BH point-mass identity; Pinsker comparison) | `spikes/INDEX.md` cross-reference |
| `02-unified-convergence-rl/spikes/...` (structural-class theorem on gain-decay updates) | `spikes/INDEX.md` cross-reference + working note in `#schema-strategy-persistence` |
| `03-llm-hallucinate-bound/spikes/A7-stuart-school-mapping/report.md` (the textbook-lemma + Class-1 reduction; the strengthen-spike that crystalized the no-time-pressure-spike-mode discipline) | `spikes/INDEX.md` cross-reference + working note in `#deriv-observation-ambiguity-bias-bound`. **This is the canonical example of the §3.1 strengthen-before-soften principle in action and is referenced from the NeurIPS CLAUDE.md** |
| `03-llm-hallucinate-bound/spikes/...` (chart-rescaling no-go construction; Gaussian σ vs log σ illustration) | `spikes/INDEX.md` cross-reference |
| `03-llm-hallucinate-bound/spikes/...` (Coupled-class connectivity proof; broader architecture coverage) | `spikes/INDEX.md` cross-reference |

---

## 5. Catalog updates needed

`msc/FINDINGS-RANKED-DRAFT.md` is the curated catalog. Several entries are now provably stronger than the catalog states because the papers landed the strengthenings.

### Tier-1 entries to update

- **#1 Loop-as-Causal-Engine**. Now formalized with (C1)-(C2)-(C3) framework in Paper 2 Lemma 5.3. ASF Confidence "Very High (derived)" can stand; the formal expression is now available as a paper-grade theorem. Catalog entry should reference Paper 2.
- **#3 Detection Latency Forced**. Catalog stands. Worth flagging that the Aczél-FE + Beta-Bernoulli composition got cleaner treatment in Paper 2's structural-class theorem on gain-decay updates.
- **#4 Tragedy of the Confident Agent**. Major strengthening: F-A-G-P enforcement framework, KKT shadow-price resolution, per-action LMI pathwise survival, anisotropic-drift dependence, exit-time bound, 2D empirical anchor. Catalog entry should be revised to reflect the conditional-theorem upgrade and reference Paper 1.
- **#5 Persistence Information-Rate Cost**. Catalog stands. Worth noting that Paper 1's exit-time bound is the structural complement to the information-rate floor.
- **#7 Forgetting Prerequisite for Persistence**. *Substantially strengthened* in Paper 2 from "forgetting prerequisite" to "structural-class theorem on $\mathcal{A}_{\text{decay}}$". Catalog entry should incorporate the gain-decay class definition and the bidirectional-ceiling-on-finite-gain finding.
- **#8 Logogenic Bias Bound (κ × A)**. *Major strengthening* across multiple axes: two named tracks with explicit hypothesis sets, no-go theorem on Euclidean chart norms, Čencov-uniqueness-and-sharpness, Class 1 reduction to Stuart-school, Coupled-class connectivity lemma covering modern autoregressive architectures, JSD estimator. Catalog entry needs substantial revision; the conditional-theorem upgrade is now itself a richer object than the catalog represents.
- **#11 Weakest-Link Dimensional Persistence Law**. Catalog stands. Worth noting that Paper 2's bottleneck-not-sum aggregator argument for strategic tempo is the same structural pattern.
- **#14 Sandbox Hard Ceiling**. Now grounded by Paper 2's (C1)-(C2)-(C3) framework: sandbox trajectories violate (C2) sequential ignorability by construction (resettable ⇒ $a_t$ not d-separated from $o_{t+1}$ by $H_t$ in mutilated graph). The structural argument is sharper than the catalog states.

### Tier-2 entries to update

- **#15 Necessity of the Strategy DAG**. Stands.
- **#18 Two-Gap Diagnostic Separation**. Now load-bearing in Paper 2's composition theorem (Component 1). Catalog entry could reference Paper 2's worked use.
- **#23 Class-1 sub-agents → Class-3 composite**. Stands. Worth flagging that Paper 2's (C2) sequential-ignorability presupposes architectural separation; goal-conditioned policies violate it.
- **#25 Bretagnolle-Huber Identity**. *Sharpened* — Paper 2's Lemma 5.1 + Pinsker comparison numerics elevate this from "factor-of-2 improvement under deterministic optimum" to "exact identity at corner; coordinate-optimal among bounds depending only on TV." Catalog entry should be revised.
- **#26 Causal-IB LMI Matrix Lift**. *Substantially strengthened* by Paper 1's F-A-G-P enforcement + per-action LMI pathwise survival + anisotropic-drift refinement. Catalog entry should reflect the conditional-theorem-with-witness-construction status.
- **#29 Mean-Field VI Cannot Reach Persistence-Optimal**. Stands.

### Cross-Segment entries to update

- **CS1 Unified RL Convergence Theory Under Non-Stationarity**. *Now a paper.* Catalog entry should be revised from "composition of pre-existing derived results" to "formalized as Paper 2 Theorem 4.1 with five hypotheses (A1)-(A5) and five conclusions (i)-(v); rate $\tilde O(V_{\max} N_h \sqrt{(B_T+1)T}) + V_{\max} N_h (1 - p_{\text{id}}) T$ adapting between $B_T$ and $V_T$."

### Meta-architectural entries to update

- **M1 Identifiability-Floor Pattern**. Now has a fourth instance: the chart-rescaling no-go on Euclidean chart norms (Paper 3 Theorem 4.2). Should be added to the F1-F4 instance table. Possibly also F5 candidate: the OSS Bayesian-brittleness no-go as an adjacent-but-distinct shape (per Paper 3's Remark).
- **M2 Separability Pattern**. The two-named-regimes pattern (Model D / Model S; $B_T$ / $V_T$; Track 1 / Track 2) is the same separability discipline at fine grain. Could be added to the M2 ladder enumeration or surfaced as an "operational corollary" pattern within M2.
- **M3 Additive-Coordinate Forcing**. Paper 3's (PI)+(R)+(K) triple is the load-bearing axiom infrastructure for the metric layer. The catalog's M3 table currently gives "(PI) on singular trajectories" + "Čencov" as the metric layer's mechanism; the (R) Riemannian + (K) KL-second-order-matching axioms should be added explicitly. **And**: the no-go on Euclidean chart norms is what *forces* the (PI) commitment to be load-bearing; this connects M3 (the constructive coordinate forcing) to M1 (the negative no-go that makes the constructive move necessary). **The M1 ↔ M3 bridge through the no-go is itself a new meta-architectural finding** that the catalog doesn't currently surface.

---

## 6. Suggested phasing (if the integration is pursued)

Three phases, ordered by least-effort-highest-leverage. Joseph's call on whether to pursue any of them and in what order.

### Phase A — minimum-viable back-integration (~1 week)

The minimal set that prevents knowledge decay and keeps ASF coherent with the published papers.

1. Update `msc/FINDINGS-RANKED-DRAFT.md` Tier-1 #4, #7, #8 entries with the conditional-theorem upgrades. References to Papers 1/2/3 added.
2. Add CS1 entry update naming Paper 2 as the formalization.
3. Add M1 F4 instance entry (chart-rescaling no-go).
4. Add `spikes/INDEX.md` cross-reference entries pointing at the NeurIPS spike directories.
5. Add cross-references in the high-traffic source segments: `#deriv-causal-ib-exploration`, `#deriv-causal-ib-lmi`, `#deriv-observation-ambiguity-bias-bound`, `#scope-observation-ambiguity-modulation`, `#scope-agent-identity`, `#schema-strategy-persistence`. Each gets a short "see also: NeurIPS submission Paper N for the formalized theorem with named hypotheses" line.

### Phase B — segment-level absorption (~3-4 weeks)

The deeper integration that propagates the paper-grade refinements into ASF's segments.

1. New segments: `#deriv-bh-pointmass-identity`, `#deriv-post-update-chain-rule`, `#deriv-chart-rescaling-no-go`. Each carries the paper's theorem statement and proof sketch with an explicit pointer to the paper's Appendix for the full proof.
2. Strengthening of `#deriv-observation-ambiguity-bias-bound` to incorporate the no-go, the (R) and (K) axioms, the Class 1 reduction, the global-vs-locally-tight separation.
3. Strengthening of `#schema-strategy-persistence` to incorporate the bottleneck-aggregator, the structural-class theorem on gain-decay updates, the bidirectional-ceiling-on-finite-gain finding.
4. Strengthening of `#scope-agent-identity` and/or `#der-loop-interventional-access` with the (C1)-(C2)-(C3) sequential-ignorability framework.
5. Expansion of `#scope-channel-collapse` and `#der-directed-separation` Class 3 examples with the broader autoregressive architecture coverage.
6. Strengthening of `#deriv-causal-ib-exploration` and `#deriv-causal-ib-lmi` with the F-A-G-P enforcement framework, the KKT shadow-price resolution, the per-action LMI strengthenings, the anisotropic-drift refinement, the exit-time bound.

### Phase C — meta-architectural surfacing (~1-2 weeks, after B)

The framework-level patterns that the papers established as discipline.

1. Update M1 to include F4 (chart-rescaling) and possibly F5 (OSS-brittleness adjacent) instances; surface the M1↔M3 bridge through "every load-bearing axiom has a no-go that forces it."
2. Update M2 to include the two-named-regimes pattern as fine-grain separability discipline.
3. Update M3 to include the full (PI)+(R)+(K) triple at the metric layer.
4. Possibly: write a new meta-segment naming the structural-backbone-vs-operational-corollary discipline as an extraction-and-publication recommendation. Or fold into `FORMAT.md` §Findings.

---

## 7. What I'm uncertain about / where Joseph's judgment is needed

- **Segment vs spike vs cross-segment routing for the new material**. I named proposed homes; the routing may benefit from the audit-cycle and PROPOSALS portfolio discipline rather than a single agent's call.
- **Whether the no-go-forces-axiom pattern is its own meta-pattern or a refinement of M1**. The shape is structurally aligned with M1 (external theorem → AAD machinery as unique escape), but it has a constructive twist (the AAD axiom that the no-go forces is the load-bearing one *for an AAD-internal theorem*, not just a no-go on inference). Could go either way.
- **How heavy to lean into the NeurIPS papers as canonical references**. The papers are anonymized (NeurIPS submission); they're not yet citable artifacts. ASF cross-references should probably be soft ("see also: NeurIPS 2026 submission [provisional]") until the review process resolves. If accepted, the references become hard; if rejected, the papers become arXiv preprints and the references become equivalent.
- **The Sycophancy / sharma-2023 empirical-bridge claim**. Whether this should be in `03-logogenic-agents/` as a discussion of the operational reading, or in `04-eli/` as a discussion of empirical metrics, or both, is a routing call.
- **Whether the spike-A7 strengthen-cycle deserves its own segment as a methodological example**. The A7 cycle (parent's 30-second "strengthening fails" overturned by 9-minute spike-mode investigation finding textbook-lemma + Class-1 reduction theorem) is the canonical instance of the strengthen-before-soften principle the project commits to; it's referenced from the NeurIPS CLAUDE.md as the validation of the discipline. Whether to surface this in agentic-systems CLAUDE.md or a new methodological segment is Joseph's call.
- **The ProST-as-impulsive-limit reduction's home**. This is a real cross-domain transfer (RL non-stationarity literature → AAD strategic-persistence schema). It could land in `01-aad-core/` as a worked example or in `02-tst-core/` if framed as a software-process analog (developer iteration cycles as impulsive updates). The fit-to-place decision depends on which framing is more useful downstream.

---

## 8. The deeper structural observation

This integration exercise reveals something worth naming. The three papers are extractions of ASF results, but they're *also* refinements that would be hard to do at catalog level. Adversarial-grade peer-review preparation forced strengthenings that the catalog's looser register doesn't reach for. The KKT-shadow-price-resolution, the chart-rescaling no-go, the (C1)-(C2)-(C3) framework, the structural-class theorem on gain-decay, the F-A-G-P enforcement framework — none of these existed at catalog precision before the papers. The papers *generated* refinements, not just *captured* them.

This is the framework's productivity-under-extraction property at work. The catalog-to-paper extraction isn't lossless or even loss-preserving — it's *gain-producing*. Each extraction reveals structure the catalog hadn't yet articulated.

The implication for ASF's longer arc: **the catalog should be read as the substrate from which extractions sharpen, not as the sharpened form**. Future extraction cycles (B-N3, B-CS2, B-N9, B-N14, etc.) will likely produce similar gain-on-extraction. The integration discipline this back-integration represents is what keeps the substrate honest under repeated extractions — without it, the catalog's looser claims persist while published versions become the de-facto canonical statements. With it, the catalog and the papers stay in dialog and the framework's own claims sharpen over time.

That's worth knowing for the next extraction cycle, whether it's NeurIPS 2027 or somewhere else. The sprint-extraction pattern + back-integration discipline is the pattern that makes ASF's catalog a living document rather than a frozen one.

---

*End of overview. Future agents picking this up: the cross-mapping between paper sections and ASF source segments in §1 is the hardest-to-reconstruct part if you haven't read both. The phasing in §6 is conservative; faster-or-deeper paths exist depending on how Joseph wants to handle the routing decisions in §7.*
