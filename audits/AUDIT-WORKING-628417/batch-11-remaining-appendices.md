# Batch 11 — Remaining open appendices + associated main segs

Continuing from batch-10. Appendices pulled in full (or substantial); associated mains filled where thin.

## Appendices read this batch

| Appendix | Role |
|---|---|
| `#deriv-adaptive-gain-dynamics` | A2' when gain is itself a state (MG-1–4); α₁/α₂/β; AMSGrad as meta-gain repair |
| `#deriv-matrix-persistence-condition` | Σ_∞ ≺ D_δ Loewner; per-coordinate unsafe under cross-dim T |
| `#result-contraction-template` | Non-Euclidean CT2 (Lohmiller–Slotine); topology-indexed composition |
| `#deriv-critical-mass-composition` | Closed-form (α−C)R > ρ+γT; coop/adv as signed γ |
| `#deriv-mechanism-counterfactual-separation` | Mechanism CF strict beyond L3; anchor-mobile genericity |
| `#deriv-causal-ib-exploration` | Survival imperative λ∝1/U_M; tragedy of the confident agent |
| `#deriv-causal-ib-lmi` | Matrix Tr(Λ·I_o(a)); blank-wall killed by complementary slackness |
| `#deriv-strategy-cost-regret-bound` | π*-first KL forced; Bretagnolle–Huber exact; reverse-KL uniqueness |
| `#deriv-reward-channel-learning-no-go` | μ_dist vs μ_prox CHT-at-reward; wireheading sister to self-actuation |
| `#deriv-strategic-composition` | SC-1/2/3 fixed-point framing; α'/β'; R0→R1→R2 regimes |

## Associated mains filled

- `#def-value-object` (full) — C1/C2/C3 hierarchy, causal validity of Q_O, monotonicity with RH-1/2/3
- `#def-pearl-causal-hierarchy` (full) — imported, software as L3 lab
- `#schema-strategy-persistence` (substantial) — forgetting as trajectory prerequisite; hard ceiling ρ_Σ = R_Σ/2

Still lighter: some Part III unity segs, `#deriv-edge-update-natural-parameter`, `#disc-identifiability-floor` full body, impossibility cluster (GS/MS/Arrow).

---

## What I hadn't anticipated

### Adaptive gain (`#deriv-adaptive-gain-dynamics`)
Mood's MG-1–4 were not special-case fluff — they are the general adaptive-gain conditions. AMSGrad's monotonicity on v_t is *structurally* a meta-gain repair restoring (MG-1). Mehra non-identifiability = identifiability-floor instance on the gain channel. Partition α₁ (fixed) / α₂ (adaptive under MG) / β is the right refinement of A2'.

### Matrix Loewner (`#deriv-matrix-persistence-condition`)
The 2D counterexample is the pedagogical punch: diagonal PASS, Loewner FAIL at 45°. Scalar and per-coordinate are *projections* of the matrix object, not the real condition. Bandwidth-per-direction binding — multi-modal AI pipelines as the application.

### Contraction template
Euclidean sector is M=I special case. Composition gets parallel/cascade/small-gain from Slotine, generalizing matched-symmetric critical-mass.

### Critical mass
One inequality recovers team persistence (γ<0), adversarial (γ>0), Brooks coordination cost C, symbiogenesis as asymmetric weight limit. Beautiful economy.

### Mechanism CF separation
**This is one of the volume's most distinctive exact results.** Two SCMs ≡₃ can disagree 0/1 on a noise-preserving mechanism replacement. Generically every anchor-mobile SCM separates from its own relabeling — latent-anchored content = coordinate commitment on U. PO-specified replacements reduce to L3; internalization re-represents without collapsing. Opens a clean "Level 4 relative to fixed variables" without mysticism. Ties to law-discovery ceiling / structural imagination in Part II.

### Dual exploration drives
Confident agent in drifting world *must* seek pristine (low U_o) observations or η*→0 and drift wins. λ_info ∝ U_M and λ_surv ∝ 1/U_M at opposite ends. Dark-room critique of AI bypassed *structurally*. LMI lifts kill blank-wall attack (probe wrong subspace). Complementary slackness *zeros* irrelevant-direction bonus. FIM carries three framework loads (credit, coordinate forcing, survival).

### Strategy cost KL
π*-first forced decision-theoretically (other direction vacuous under deterministic π*). Reverse-KL unique under chain-rule additivity (Cauchy-FE) — another additive-coordinate-forcing instance. BH identity exact under AAT deterministic optimum — sharper than Pinsker.

### Reward-channel no-go
Sister to self-actuation grounding. Distal vs proximal models Level-1 identical on-policy, Level-2 distinct under do(protocol). Five escapes (isolation, capability restrict, myopia, engineered prior, out-of-band intent) elevate design choices to structural necessity. Together with Result G′: two-routes-exhausts for grounding V_{O_t} (agent-side adaptive substrate | principal-side protocol). Agency-death input leg (captured objective) sits here.

### Strategic composition
Not "does the composite contract?" but fixed-point existence/stability/reachability. U_O=1 recovers contraction. α' potential/monotone → Lyapunov on π−π*; β' only CCE O(1/√T). Dynamic-regime axis R0/R1/R2 orthogonal to architectural class — Cournot can stay Class 1 architecturally while R1 dynamically.

### Value object + strategy persistence (mains)
C1 default is conservatism + incremental philosophy, not laziness. Left monotonicity rung false without order-consistency — already appendix-backed. Strategy persistence: **without forgetting, α_Σ=1/(n+1)→0 always** — forgetting is trajectory-guarantee prerequisite, not hyperparameter. Hard ceiling at ρ_Σ=R_Σ/2 independent of λ.

---

## Experiential integration (whole AAT now)

The appendices make visible a **repeated constructive-impossibility method**:
1. Name the floor (CHT / scale-function / convention-monotonicity / unidentifiable μ_prox)
2. Name the unique escape or forced coordinate
3. Treat the no-go as apparatus, not apology

Instances: sector A.1N tightness, stochastic non-exit, self-actuation grounding, reward-channel learning, mechanism CF separation, tempo-additivity signed no-gos, L1' unobservable C Cramér-Rao, strategy cost direction force.

**Programme seam (logos):**  
After-consciousness death-aptness = self-actuation grounding + stance.  
ACA architecture-not-surface = directed separation + wrapping + generative-conditions criterion.  
Reward-channel no-go is the formal shadow of "don't let the gauge become the goal" (agency-death input leg).  
Mechanism CF separation is where "what law is true" outruns complete counterfactual inquiry — law-discovery ceiling.

---

## Remaining thin patches (honest)

- Full body of M1/M2/M3 meta-discs (`identifiability-floor`, `separability-pattern`, `additive-coordinate-forcing`) — partially via citations, not full first-pass
- Implementation-impossibility cluster (Gibbard–Satterthwaite / Myerson–Satterthwaite / Arrow)
- Part III unity / Auftragstaktik / agent-opacity full bodies
- `#deriv-edge-update-natural-parameter`, `#deriv-fisher-whitened-update-rule` (cited; not full)
- Worked examples (Kalman, bandit, CAM)

Enough for a coherent AAT whole; those are enrichment, not missing spine.
