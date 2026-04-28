# Findings Brainstorm — Ongoing Scratch & Speculative Candidates

*Rolling working surface for findings-related work. Companion to the curated [`FINDINGS-RANKED-DRAFT.md`](FINDINGS-RANKED-DRAFT.md) (capital-F = top-level catalog). This file is where speculative candidates accumulate before promotion, where lower-confidence catalog entries get parked when the curated list needs tightening, and where cross-domain brainstorming notes live as reasoning trail. Lowercase-naming convention = scratch / working surface.*

*Not polished. Curiosity-driven. Add freely.*

---

## Rolling log

**2026-04-28 — Pulled back from FINDINGS-RANKED.**
- **#34 Misspecification-Cost as Adjacent Identifiability Floor** (was Tier 2) — speculative; segment-flagged as open extension. Full content in [§Pulled back](#pulled-back-from-findings-ranked-2026-04-28) below.
- **#55 The Tragedy of the Confident Agent — Thermodynamic Reading** (was Tier 3) — speculative-medium; was P1-E. Continue to develop as P1-E below; no separate copy needed.
- **§Speculative S1–S8** (was a section in FINDINGS-RANKED) — moved back to this file's [§Speculative section](#speculative--worth-flagging-s1s8) (which is the canonical home — same items the agent originally surfaced here).

**2026-04-27 — Promoted to FINDINGS-RANKED.** Most Pass 1 + Pass 2 candidates from the original brainstorm pass; meta-finding M3 (separability-pattern; landed as M2 in catalog after structural reordering); cross-domain implication-map content distributed across catalog Tier 1/2/3 + Open Questions sections. See per-entry promotion markers below in the Pass 1 / Pass 2 sections.

---

## Frame (original 2026-04-27 brainstorm)

The agent read the catalog (`msc/FINDINGS-RANKED-DRAFT.md`) end-to-end, then read these segments at depth: `disc-separability-pattern`, `result-sector-persistence-template`, `deriv-adaptive-gain-dynamics`, `disc-compression-operations`, `scope-agent-identity`, `disc-credit-assignment-boundary`, `result-structural-adaptation-necessity`, `disc-identifiability-floor`, `result-coupled-diagnostic-framework`, `form-consolidation-dynamics`, `result-specification-bound`, `disc-exploit-explore-deliberate`, `der-change-proximity-principle`, plus the TST `obs-software-epistemic-properties`.

The brainstorm was shaped by one organizing observation that came up early and kept paying off: **the catalog originally named two meta-architectural patterns (identifiability-floor, additive-coordinate-forcing) but omitted a third that the segments carry first-class — `disc-separability-pattern`**, the *positive-half* meta-pattern whose seven ladders organize where AAD's results hold cleanly, where they hold under structured repair, and where they remain open. The third meta-pattern landed in the catalog (as M2) after this brainstorm. Several Pass-1 candidates fell out of running an M1+M2+M3 meta-triad against existing catalog entries.

---

## Pass 1 — Candidates from the Catalog Alone

### P1-A. The Persistence-Cost / Persistence-Threshold Duality (compose #5 + #11 + sector-persistence-template)

**Description.** Catalog #5 (Information-Rate Cost) gives the cost an instantiation must sustain to maintain its ultimate bound. Catalog #11 (Weakest-Link Per-Dimension Persistence) shows aggregate persistence is governed by the worst-served dimension. The composition is sharper than either alone: **the cost-floor is also weakest-link per dimension**. The Mitter-Newton saturation rate $\dot R \geq n\alpha/2$ is a sum over dimensions, but no Shannon-type aggregation can compensate for one dimension being capacity-starved. An adaptive system at $n=10$ that saturates on 9 of 10 dimensions and starves the 10th still fails, and the failure is not visible in the aggregate rate.

**Composes:** #5, #11, sector-persistence-template (which already names the cost complement in its Discussion).

**Adjacent open question touched.** Distributed systems and multi-modal RL have long had a "we have enough total bandwidth — but it's the wrong kind" failure mode that is empirical lore but unformalized. Multi-modal AI architectures (vision-language with asymmetric channel budgets) are a primary application.

**Confidence.** High — both inputs are tier-1 with strong derivations; the composition is mechanical.

### P1-B. Class 2 + Detection Latency: LLM Calcification Compounds

**Description.** #3 (Detection Latency) is derived for an evidential-additivity Bayesian agent. #8 (Logogenic Bias Bound) shows Class 2 agents have biased $M_t$ updates with bias $\propto \kappa \cdot \mathcal A$. **Compose: a long-running LLM agent's regime-change detection latency grows linearly with experience *and* is biased by goal-conditioning** — even before the latency rate $\Omega((n+1)/\varepsilon)$ binds, the goal-conditioned $M_t^{(\text{post})}$ has already shifted the *direction* of inference. The two effects compound.

**Composes:** #3, #8, with #6 / CS2 nearby.

**Adjacent open question touched.** Why long-running deployed LLM agents become "stuck" on a particular interpretation is currently treated as alignment problem (RLHF freezing) or calibration problem (post-training drift). The framework supplies a different story: architectural coupling is fixed at training, but *rate-of-calibration-degradation* compounds with experience. Predicts a specific empirical signature: deployed agents serving many similar requests should be measurably slower to recognize regime shifts on those request types than fresh agents — slower in proportion to accumulated goal-conditioning bias, not just total experience.

**Confidence.** High at qualitative compositional level; medium for quantitative form.

### P1-C. The Forgetting-Rate Cost Is a Bandwidth Cost (compose #5 + #6 + #7)

**Description.** #7 (Forgetting Prerequisite) gives lower bound on forgetting: $(1-\lambda) > \rho_\Sigma/R_\Sigma$. #6 (Stability-Plasticity Window) gives upper bound: forgetting must be slow enough for consolidation. #5 says persistence costs $\dot R \geq n\alpha/2$ nats/time. **An agent forgetting at the prescribed lower-bound rate is thereby committing to a Shannon information rate proportional to its forgetting rate, because every forgotten observation must be replaced from new evidence to maintain persistence.** The forgetting prerequisite is therefore not just memory-management — it is a *bandwidth* constraint. Two agents with identical persistence guarantees but different forgetting rates have different observation-channel requirements, in nats/sec, for free.

**Adjacent open question touched.** Continual-learning literature has unexplained empirical pattern: faster-forgetting curricula need more diverse data. This composition predicts the relationship is information-theoretically forced. (Possibly true also for the empirical observation that aggressive learning-rate schedules require larger batches.)

**Confidence.** Medium-high.

### P1-D. The Unifying Slogan: Successful Adaptation Is Always Bandwidth-Limited

**Description.** Pulling P1-A, P1-C, #5, #6 together: the framework predicts a near-universal "bandwidth wall." Any sufficiently long-lived adaptive system that survives (sector condition holds), tracks reality (forgetting prerequisite holds), and consolidates cross-episode patterns (window non-empty) is *forced* into a regime where its observation channel capacity is binding. Survival without bandwidth limitation is unstable.

**Adjacent open question touched.** Across biology (retinal Shannon limits, cochlear capacity), neuroscience (prefrontal cortex bandwidth-constrained), distributed systems (raft/paxos throughput), and organizations (information overload), a common observation is that adaptive systems sit *at* their information-rate limit. The framework's contribution: this is not coincidence; sub-bandwidth-limited regimes are not adaptive equilibria.

**Confidence.** Medium. Possibly *robust qualitative* under a specific scope.

### P1-E. The Tragedy of the Confident Agent's Thermodynamic Reading

**Description.** #4 (confident agent must seek pristine observations) + #5 Landauer reading ($\sim 0.35 n\alpha k_B T$ dissipation): **as $U_M$ shrinks, the agent's bandwidth requirement does *not* shrink — confidence does not relax persistence cost, only the information-acquisition strategy.** The agent sustains the same Shannon floor, paid via more selective (lower-noise, more directional) observations rather than more abundant ones. **Complacency does not save energy, it just changes which channels burn it.**

**Adjacent open question touched.** Highly skilled experts maintain higher metabolic load on focused tasks than novices (known but unexplained). Markets near efficiency dissipate trading energy at higher per-volume rates than markets far from it (Bouchaud's empirical observation). Falsifiable: experts' fMRI-measured metabolic spend on near-mastered tasks should not drop with skill, despite reduced uncertainty; it should redistribute toward more-attended channels.

**Confidence.** Speculative-medium.

### P1-F. OODA Tempo + Detection Latency = Why "Inside Their Loop" Closes

**Description.** #10's $\mathcal T^{\text{eff}} = \mathcal T \cdot H_b/H_b^{\max}$ + #3's $\Omega((n+1)/\varepsilon)$. **The 16-cell adversarial-targeting matrix is self-bounded: the most damaging cell to attack is the one your detection latency makes hardest to recognize.** Sharpens adversarial-targeting from "where to attack" to "where to attack such that the target's accumulated experience makes detection-too-slow exactly there."

**Adjacent open question touched.** Where do attackers concentrate? Where defender's response is slowest. Empirical signature: cybersecurity incidents cluster on long-trusted dependencies; adversarial examples cluster on high-confidence model regions. Both observed; the framework supplies the unifying mechanism via the latency rate.

**Confidence.** Medium-high.

### P1-G. #21 Forbids a Common AI-Safety Trope

**Description.** #21 (Class-1 sub-agents with partially-opposing objectives → Class-3 composite) **forbids the common AI-safety trope of "we'll keep the system safe by composing modular safety modules with a central planner."** As soon as the safety modules and the planner have non-aligned objectives (precisely when safety modules are needed — to *constrain* the planner against its own objectives), the composite is structurally Class 3, and modular guarantees do not transfer.

**Adjacent open question touched.** AI-safety has had negative empirical results on modular safety architectures (red-team penetration of constitutional AI; Hubinger et al. on mesa-optimizers within nominally-modular systems). The framework supplies the structural reason. *Negative finding*: the framework predicts an entire family of safety architectures cannot work as advertised.

**Confidence.** High at qualitative level; medium for the strong reading ("most current AI safety architectures are structurally guaranteed to fail under goal divergence").

### P1-H. Software Calibration Lab + Identifiability-Floor M1 → Domain-Generalization Theorem

**Description.** #12 names software's six identification-friendly properties (P1–P6). M1 names cases where AAD inferences have a structural floor. **Compose: any AAD finding's transfer from software to a non-software domain inherits an identifiability-floor instance for each P_i the target domain fails.** The framework should have a transfer theorem: "domain D inherits AAD result X under the identifiability-floor escapes corresponding to {P_i : D fails P_i}." Without this, the calibration-lab framing is honest about scope but offers no machinery for what survives transfer.

**Adjacent open question touched.** Domain-generalization in ML has lacked principled cross-domain transfer guarantees. Methodological complement to the calibration-lab framing.

**Confidence.** Medium-high.

### P1-I. Loop-as-Causal-Engine + Singular-Trajectory = Sandbox Testing Has a Hard Ceiling

**Description.** #1 (closed loops generate Pearl-Level-2 data) is contingent on trajectory non-forkability (`scope-agent-identity`). **Sandboxed testing breaks the singular-trajectory commitment by construction** — sandbox trajectories are forkable (resettable, replayable, parallelizable). Therefore: agent-in-sandbox does *not* generate Pearl-Level-2 data the same way as in production. Sandbox behavior is observationally equivalent to deployment only at Level 1. Level-2 distinctions are not identifiable from sandbox data.

**Adjacent open question touched.** AI evaluation literature: "alignment evals don't predict deployment behavior" — empirical, much-debated, no consensus mechanism. Framework reading: this is a Pearl-hierarchy problem, structurally.

**Confidence.** High at structural argument level; medium-confidence interpretation for "this explains the alignment-eval gap."

### P1-J. OKR-As-Observability-Engineering Generalizes to Any Bandwidth-Limited Multi-Agent System

**Description.** `disc-credit-assignment-boundary`'s OKR connection — four OKR failure modes (vanity metrics / too many KRs / lagging indicators / Goodhart) map to AAD predictions. **The generalization: any multi-agent system with deep partially-observable strategy DAGs has the same four failure modes, with the same formal forms, regardless of domain.** Not in the catalog; lives in the segment as Discussion.

**Adjacent open question touched.** Mechanism design has long had "alignment of measurement and incentive" problems (Holmström 1979, Lazear 1989), with the four failure modes appearing under different names. Framework supplies one mechanism (observability subgraph + credit-assignment-via-gradient) producing all four.

**Confidence.** High.

### P1-K. Negative Finding: Mean-Field VI Cannot Reach Persistence-Optimal Behavior

**Description.** #25 says natural-gradient VI recovers full $\alpha$; mean-field VI suffers $O(\sqrt\varepsilon)$ degradation. **Negative finding the catalog does not foreground: mean-field VI agents are structurally suboptimal as adaptive systems by a factor $\sqrt{\text{KL-budget}}$, regardless of compute or training data.**

**Adjacent open question touched.** Bayesian-deep-learning literature has been arguing about MF-VI vs natural-gradient for over a decade without principled grounds. The framework: there is no choice if persistence-optimality matters.

**Confidence.** High — segment is explicit; under-foregrounded as a finding.

### P1-L. Four-Compression-Operations + Calibration-Lab → Bandwidth-Allocation Theory

**Description.** `disc-compression-operations` Working Notes flag as open: "a theory of resource allocation across the four compression operations." Pairing with #5 + #11: each compression has its own information-rate floor, agent's total bandwidth allocated across them. **Budget identity:** $C_{\text{total}} \geq C_M + C_\Sigma + C_{\text{shared}} + C_\Lambda$ where each component is the per-operation Mitter-Newton-style floor.

**Adjacent open question touched.** Cognitive architecture: how brain allocates metabolic budget across modules (Lennie 2003; Attwell-Laughlin 2001). Total cortical Shannon spend should not fall below sum of per-cortical-area identifiability-floor estimates.

**Confidence.** Medium — qualitative claim high-confidence; quantitative form open.

---

## Pass 2 — Candidates from Segment Reading

### P2-A. M3: The Separability-Pattern as Third Meta-Architectural Finding

**Description.** Catalog has M1 (identifiability-floor) and M2 (additive-coordinate-forcing). **Missing M3 = the separability pattern**, which `disc-separability-pattern.md` carries explicitly across seven ladders (Correlation L0/L1/L2; Convention C1/C2/C3; Architecture Class 1/3/2; Contraction Tier 1/2/3; Identification Regime A/B/C; Scope Adaptive/Agency/Composite; A2'-scope metric-α₁/α₂/β). M3 is the *positive-half scope theory*: separable core / structured repair / general open.

The segment is explicit: M1 + M3 form a complete scope characterization. Without M3, the catalog presents AAD as having a negative-half (M1) and a coordinate-forcing-half (M2) but no positive-half scope theory — misleading because the segments do carry one. **This is the catalog's most prominent omission from this brainstorm.**

**Cross-domain transfer.** Seven ladders draw on Pearl's hierarchy, OR convention hierarchies, cognitive-science modularity, econometric identification regimes. AAD's contribution is systematic deployment of separability-pattern thinking across seven AAD-relevant intractabilities.

**ASF Confidence:** Discussion-grade at meta-pattern level; instances retain tiers. **Field Novelty:** High. **Potential Importance:** Very high.

**Grounded in:** `01-aad-core/src/disc-separability-pattern.md`.

### P2-B. The Sector-Persistence Template as a First-Class Result

**Description.** `result-sector-persistence-template.md` (status=exact) is one Lyapunov argument absorbing six AAD persistence results, plus a seventh in `deriv-critical-mass-composition`. **The catalog mentions the template (in #5, in CS3) but does not surface it as its own finding.** Most striking omission, because the template is exactly the framework-internal economy that distinguishes a synthesis from a pile of instantiations.

The segment also makes a structural connection not in the catalog: **AAD's persistence machinery is a specialization of monotone-operator theory** (Rockafellar 1970; Bauschke-Combettes 2017; Parikh-Boyd 2014). One-point strong monotonicity at equilibrium = T2; two-point strong monotonicity = bridge-lemma's DA2'-inc. Specialization is honest: one-point anchoring strictly weaker than two-point, matched to fixed-point-at-target semantics, admitting agent classes (PID-bounded-plant, variational-approximate) where full monotonicity fails. Plus Model D / Model S split with $1/\alpha$ vs $1/\sqrt\alpha$ scaling producing $b=2$ vs $b=3/2$ exponents — content monotone-operator theory does not natively carry.

**Engineering anchor.** Six AAD persistence results have one Lyapunov proof. Distinctive content of each instantiation is its *effective disturbance decomposition*. Lyapunov boilerplate shared; signed-coupling decomposition is the genuinely new content.

**Cross-domain transfer.** Template-instantiation transfers beyond AAD's seven. Anywhere a state variable evolves under bounded correction with bounded disturbance: market-making bid-ask spread; immune-system effector-cell concentration; cellular homeostasis; supply-chain inventory under demand shocks. **Framework's claim: all have one Lyapunov story with N effective-disturbance decompositions.**

**ASF Confidence:** Exact. **Field Novelty:** Medium-high. **Potential Importance:** High.

**Grounded in:** `01-aad-core/src/result-sector-persistence-template.md`.

### P2-C. The Adaptive-Gain $\alpha_2$ Sub-Scope Reframes RL's Adaptive-Step-Size Lore

**Description.** `deriv-adaptive-gain-dynamics.md` derives sub-scope refinement: A2' splits into $\alpha_1$ (fixed-gain), $\alpha_2$ (adaptive-gain under MG-1 through MG-4), and $\beta$. **Catalog does not surface this**, but implications for RL practice are direct:

- **AMSGrad is structurally a meta-gain repair** that restores (MG-1) by construction. Empirical superiority over Adam on ill-conditioned problems is now *derived*.
- **MAML's outer loop is in $\beta$** — Fallah et al. 2020's non-convexity is structurally forced.
- **IMM regime transitions are in $\beta$ across-transition.** Adaptive Kalman in regime-switching needs explicit dwell-time machinery.
- **Mehra non-identifiability is an identifiability-floor instance** — a fifth M1 instance the catalog does not list.

**Cross-domain transfer.** Two-timescale Lyapunov composition is general. Examples: hyperparameter-learning loops (PBT, Bayesian-optimization-of-LR); central-bank rate-setting feedback; biological homeostatic gain-tuning.

**Grounded in:** `01-aad-core/src/deriv-adaptive-gain-dynamics.md`.

### P2-D. Software Specification Bound Connects to AAD's Persistence Bandwidth

**Description.** `result-specification-bound.md` (TST): $\text{time}_{\min}(F) \geq H_{\text{req}}(F \mid M_{\text{shared}}) / R_{\text{spec}}$. **Catalog does not connect to #5, but connection is direct**: the specification channel is one observation channel among the agent's bandwidth budget. **Implementation-time-floor and persistence-bandwidth-floor are the same Shannon constraint at different layers** — the agent receiving a specification must do so at a rate compatible with its persistence-bandwidth-floor, or specification outpaces update rate.

**Engineering anchor.** When does specification become unimplementable in fixed time? When information rate exceeds implementer's persistence-bandwidth-floor. AI-coding-agent practitioners observe "context-stuffing helps to a point, then degrades" — framework supplies the floor.

**Cross-domain transfer.** Military command transmission (Auftragstaktik bandwidth + receiver persistence); medical-handoff (Joint Commission bandwidth tables, no theoretical floor); cockpit handover; surgical procedural transmission.

**Grounded in:** `02-tst-core/src/result-specification-bound.md` + #5.

### P2-E. Coupled Diagnostic Framework: The Workaround for Class-2 Orient-Cascade Failure

**Description.** `result-coupled-diagnostic-framework.md` shows that for Class 2 agents (LLMs), Orient cascade's information-dependency-forced ordering becomes a *normative design pattern*. Diagnostic quantities ($\delta_{\text{sat}}$, $\delta_{\text{regret}}$) remain *defined* on post-update state but not produced *in cascade order*. Lipschitz bound $|\delta_{\text{sat}}^{(\text{coupled})} - \delta_{\text{sat}}^{(\text{clean})}| \leq L_A \cdot \|\Delta M_{\text{bias}}\|$ shows error bounded by bias bound (#8) bounded by $\kappa \cdot \mathcal A$.

**Should be in the catalog: framework predicts LLM agents satisfy Section II's diagnostic guarantees by external scaffolding** that materializes diagnostic inputs and enforces cascade ordering at the loop level (not the model's forward-pass level). Concretely: structured reasoning templates, multi-step prompts, external monitors detecting cascade-order violations.

**Implication is twofold:** (a) AAD Section II results *do* extend to logogenic agents under explicit scaffolding; (b) **"agentic systems" — agent loops *around* LLMs — are not just engineering convenience but structural requirement to recover Section II in Class-2.**

**Engineering anchor.** Precisely Alan's domain. Predicts: scaffolded "diagnose then strategy then objective" loop *can* recover Section II's persistence guarantees, with bias bounded by $\kappa \cdot \mathcal A$.

**Cross-domain transfer.** Same scaffolding-recovers-cascade transfers to any Class-2 architecture: human bicameral models; organizations where executive scaffolding (boards/committees/decision rights) recovers cascade ordering.

**Grounded in:** `03-logogenic-agents/src/result-coupled-diagnostic-framework.md` + #8.

### P2-F. Consolidation Dynamics + Persistence Cost = Sleep Has a Shannon Floor

**Description.** `form-consolidation-dynamics.md`: consolidation necessary when (N1) sub-state factorization + (N2) bounded per-event budget. CLS factorization (McClelland-McNaughton-O'Reilly 1995) is canonical biological instance. **Catalog has #6 (window) but not consolidation-rate-cost finding**: under (N1)+(N2), $\nu_{\text{consol}}$ is bounded below by an information-rate floor analogous to #5's persistence floor.

**Implication for biology: REM sleep has a Shannon floor.** Empirical "you cannot indefinitely sleep less than 4 hours and remain adaptive" is consequence of consolidation-rate floor, not just metabolic load.

For LLM agents under near-100% context turnover: same floor applies. An agent that processes context faster than it can consolidate to persistent memory is forced into catastrophic-forgetting feasibility-window collapse.

**Engineering anchor.** "How often should an LLM agent run consolidation (memory-summary, retrieval-augmentation update, fine-tuning pass)?" Answer: at the rate the consolidation-information-floor demands.

**Cross-domain transfer.** Sleep-rate floors; cache-flush-rate floors; consolidation-batch-size floors in continual learning; institutional-knowledge-codification rate floors.

**Grounded in:** `01-aad-core/src/form-consolidation-dynamics.md` + #5.

### P2-G. Identifiability Floor Adjacent: Misspecification-Cost as Information-Theoretic Bound

**Description.** `disc-identifiability-floor.md` flags Misspecification-Cost as open Adjacent Floor. **Expected floor is information-theoretic**: under fixed information budget, degradation rate from misspecified model class is bounded below by KL gap between true and assumed model classes. Combined with #5 + #11, gives quantitative misspecification-cost.

Fifth M1 instance once derived. Highly cross-domain: Sargent-Hansen ambiguity-averse decision-making; small-gain misspecification bounds in robust control; BIC penalties; statistical-mechanical free-energy gap. All would be M1 instances under one framework.

**Confidence.** Speculative — open extension flagged in segment.

### P2-H. Three-Way Resource Allocation Has Implicit Bandwidth Constraint

**Description.** `disc-exploit-explore-deliberate.md`: Exploit / Explore / Deliberate, with Deliberate as "internal exploration in model-space rather than environment-space." Deliberation threshold $\Delta\tau^\ast$. **Catalog does not surface this; nor the bandwidth implication: deliberation does not relax persistence-bandwidth floor (#5)**, only changes channel allocation. An agent deliberating is *not* exempt from receiving observations at $C \geq \mathcal T/2$. **This sharpens deliberation's role: temporary reallocation, not substitute for external bandwidth.**

**Cross-domain transfer.** "Internal vs external exploration both pay against same Shannon floor" transfers to chess engines (search depth + observation freshness must both be funded); military command (war-gaming + reconnaissance must both be funded); science (theory-building + experiment-running must both be funded).

**Grounded in:** `01-aad-core/src/disc-exploit-explore-deliberate.md` + #5.

---

## Cross-Domain Implication Map

### Reinforcement Learning

(a) **What AAD says:** Closed-loop RL agents generate Pearl-Level-2 data automatically (#1) — RLSVI / Thompson regret bounds derived under L1 are conservative. Adam/AMSGrad/MAML/RMSProp choices are sub-scope choices in $\alpha_1/\alpha_2/\beta$ partition (P2-C). Detection-latency growth is structurally forced (#3); no reparameterization escapes. Mean-field VI structurally suboptimal vs natural gradient by $O(\sqrt\varepsilon)$ (P1-K, #25).

(b) **Open questions:** Convergence under non-stationarity (CS1). Sample-efficiency under distribution shift (#3). Catastrophic forgetting (#6 + P1-C). Closed-loop vs offline RL (#1 Pearl-Level-2 vs Level-1).

### Control Theory

(a) **What AAD says:** Sector-Lyapunov template (P2-B) as one-Lyapunov-argument economy. AAD's distinctive content is signed-coupling effective-disturbance decomposition. Adversarial-tempo decomposes into tempo × opacity (#10). Three independent obstructions to contraction-analysis in adversarial regimes (#22). Brooks's Law derived from continuous physics (#9).

(b) **Open questions:** Multi-agent stability under signed coupling (#9). Contraction under non-Euclidean geometries (`result-contraction-template`). Adversarial regimes for contraction (#22).

### Causal Inference

(a) **What AAD says:** Closed-loop agents generate Pearl-Level-2 data (#1). L0/L1 unidentifiable from on-policy data — scientific experimentation's inefficiency is Pearl-hierarchy-forced (#2). Fisher rank-deficiency forbids L1' mixture identifiability (M1 Instance 2). Identifiability of coupling sign forbidden from component marginals (M1 Instance 3).

(b) **Open questions:** Identifiability under feedback (`der-loop-interventional-access`). Sandbox vs deployment data (P1-I). Causal discovery from observational time series (M1 Instance 2). Misspecification cost (P2-G).

### Information Theory

(a) **What AAD says:** Why log-odds, Fisher metric, KL, IB tradeoffs keep showing up — M2 forces them at four representational layers via classical uniqueness theorems. Persistence has Mitter-Newton-saturation Shannon-rate floor (#5). Forgetting prerequisites are bandwidth costs (P1-C). Compression operations partition into IB-shape and not-IB-shape (P2-D).

(b) **Open questions:** Why IB agents work (M2 + #25). Information-rate cost of consolidation (P2-F). Per-compression-operation budget identity (P1-L).

### Neuroscience

(a) **What AAD says:** CLS hippocampus/cortex factorization is canonical (N1)+(N2) instance (P2-F + #6). Sleep has a Shannon floor (P2-F). Brain bandwidth runs near saturation (P1-D). Class 1 vs Class 3 distinction maps onto cortical-architecture debates.

(b) **Open questions:** Why must we sleep? (P2-F). Cortical bandwidth allocation (P1-L). Hippocampal-cortical consolidation cadence (#6).

### Organizational Behavior

(a) **What AAD says:** Innovator's Dilemma + Levitt-March + Hannan-Freeman + March 1991 + Eldredge-Gould + Hafez 2026 IDT unify under #3. Brooks's Law (#9). OKRs as observability-by-design (P1-J). Auftragstaktik as IB compression (#20). Class-1 sub-agents with partially-opposing objectives produce Class-3 composites (#21, P1-G).

(b) **Open questions:** Why do successful organizations underinvest in disruption detection? (#3). When can a team be modeled as one agent? (#9). Goodhart's Law structural origin (P1-J). Institutional-knowledge codification rate (P2-F analog).

### Distributed Systems

(a) **What AAD says:** Bandwidth-constrained agents face #5 floor. Composition closure $\varepsilon^\ast$ + bridge lemma (#9). Consolidation cadence floor (P2-F). Adversarial tempo × opacity (#10).

(b) **Open questions:** Consensus throughput floors. When does asynchronous coordination collapse? Adversarial Byzantine bounds.

### Biology / Evolution

(a) **What AAD says:** Punctuated equilibrium shares mechanism with Innovator's Dilemma (#3). Symbiogenesis as asymmetric limit of #9. Neutral structural diversity (Miller 2022) as route to structural adaptation. Sensory-bandwidth limits as persistence-cost-floors (P1-D, #5 Landauer reading).

(b) **Open questions:** Punctuated equilibrium mechanism. Why species coexist (#21 in ecology). Energetic costs of cognition. Neural information-rate as constraint on body plan.

### Software Engineering

(a) **What AAD says:** Software is calibration laboratory (#12). Comprehension time dominates under AI-maintained code (#14). Code quality IS observation infrastructure (#15). 14 EXACT estimators from $\mathcal C_t^{\text{commit}}$. OKRs / change-proximity / atomic-changesets are AAD predictions (P1-J + change-distance hierarchy). Specification bound + persistence bandwidth (P2-D).

(b) **Open questions:** Why does clean code "compound"? Why do successful codebases ossify? (#3 applied to architectural assumptions). Software architecture as shared-intent compression.

### AI Safety

(a) **What AAD says:** LLMs are Class 2 with bias $\kappa \cdot \mathcal A$ (#8). Modular safety architectures fail under goal divergence (P1-G, #21). Sandboxed eval cannot identify Level-2 deployment behavior (P1-I). Confident agents must keep exploring (#4). Coupled diagnostic framework (P2-E): scaffolded agentic systems are *structural requirement* to lift LLMs into Section II compliance.

(b) **Open questions:** Why don't alignment evals predict deployment? (P1-I). Why does RLHF become brittle? (P1-B). Structural status of "scalable oversight"? Goal-conditioning under prompt ambiguity (#8). Multi-agent AI safety under goal divergence (#21).

### Mechanism Design / Economics

(a) **What AAD says:** Goodhart's Law (P1-J). Holmström-Lazear measurement-vs-incentive: same observability-subgraph mechanism across all four OKR failure modes. Mechanism-design impossibility (Gibbard-Satterthwaite, Myerson-Satterthwaite, Arrow): candidate fifth M1 instance. Putnam's $t \propto t_{\text{specify}}^{3/4}$.

(b) **Open questions:** Mechanism-design impossibility as identifiability floor. Information-rate cost of incentive compatibility. Why do markets dissipate energy near efficiency? (P1-E).

---

## Pulled back from FINDINGS-RANKED (2026-04-28)

*Entries promoted into the curated catalog and then pulled back when the catalog was tightened. Each is at speculative or near-speculative confidence — they remain interesting but not yet ready for a tier in the curated list. Re-promotion happens when the derivation tightens or scope clarifies.*

### #34. Misspecification-Cost as Adjacent Identifiability Floor

**Description:** `disc-identifiability-floor` flags Misspecification-Cost as an open Adjacent Floor. Expected floor is information-theoretic: under fixed information budget, degradation rate from a misspecified model class is bounded below by the KL gap between true and assumed model classes. Combined with FINDINGS-RANKED #5 (Information-Rate Cost) + #11 (Weakest-Link Per-Dimension Persistence), this would give a quantitative misspecification-cost. Would be a fifth M1 (identifiability-floor) instance once derived. Highly cross-domain: Sargent-Hansen ambiguity-averse decision-making; small-gain misspecification bounds in robust control; BIC penalties; statistical-mechanical free-energy gap. All become M1 instances under one framework.

* **ASF Confidence:** Speculative — open extension flagged in segment Working Notes; not yet derived.
* **Field Novelty:** High if derived.
* **Potential Importance:** High if derived — broad cross-domain reach.
* **Why pulled:** explicitly speculative-confidence; awaiting derivation. Re-promote once the KL-gap-based bound is worked through.

### #55. The Tragedy of the Confident Agent — Thermodynamic Reading

*Same content as P1-E above (Pass 1 §E). Was promoted into Tier 3 of FINDINGS-RANKED on 2026-04-27, pulled back on 2026-04-28 as speculative-medium. Continue to develop as P1-E.*

---

## Speculative / "Worth Flagging" Section (S1–S8)

### S1. Singular-Trajectory Commitment Implies AGI Continuity Has a Hard Floor

`scope-agent-identity` is explicit: identity is the trajectory $\mathcal C_t$, not $M_t$. **Speculative:** any "continuity-of-self" guarantee for an AI system across substrate change (model-weight transfer, restart-from-checkpoint, multi-instance deployment) is *not* deliverable from AAD alone. AAD-grounded AI welfare claims (logozoetic agents) about persistence-of-self need structure beyond AAD. *Negative finding for AI rights / digital-personhood debates.*

### S2. The Catalog's Tier-1 Findings Cluster on M1 Instances

Most Tier-1 findings have an M1-floor instance somewhere in their derivation. Pattern itself is a finding: framework's most significant results are most strongly when the negative-half scope theory does work. Not confident this is novel-as-finding rather than methodologically obvious.

### S3. Tempo × Opacity Has a Three-Way Generalization

#10's $\mathcal T^{\text{eff}} = \mathcal T \cdot H_b/H_b^{\max}$. **Speculative:** adding identifiability factor $\iota$ from `scope-edge-update-causal-validity` gives $\mathcal T^{\text{eff}} = \mathcal T \cdot H_b/H_b^{\max} \cdot \bar\iota$. An adversary in Regime C against Regime-A defender has multiplicative advantage on $\iota$ alone. Empirically: covert vs overt operations.

### S4. Persistence-Cost Floor + Specification Bound Predict LLM Context-Window Lower Bound

Combining #5 with `result-specification-bound`: minimum context window in tokens is bounded below by $n\alpha/2$ nats/time × (time per cycle) ÷ (nats/token). Algebra not worked; prediction qualitative. Possibly already known empirically; Alan would recognize.

### S5. Prompt Engineering as $\mathcal A$-Reduction Has Hard Hallucination Lower Bound

#8: hallucination $\propto \kappa \cdot \mathcal A$. **Speculative:** $\mathcal A$ has hard lower bound from prompt's *intrinsic* ambiguity given agent's prior — some $\mathcal A_{\min}$ no prompt-engineering can drive below. Predicts hallucination floor for any goal-bearing query, parametric in $\kappa$ (architectural) and $\mathcal A_{\min}$ (semantic).

### S6. Three-Way Allocation Is Underspecified for Class-2 Agents

`disc-exploit-explore-deliberate` derives deliberation threshold under directed separation (Class 1). For Class 2, additive decomposition is "convenience." **Speculative:** chain-of-thought is *not* simply increased deliberation; it is coupled-deliberation with different optimization properties. Framework may carry structural answer to "do longer chains-of-thought always help."

### S7. Loop-Level-2 Has Implications for Multi-Instance LLM Agents

By `scope-agent-identity`, $N$ parallel LLM instances are each their own agent on its own singular trajectory. **Speculative:** they don't *jointly* generate Level-2 data on each other absent explicit coordination. May explain why federated-learning-style multi-instance LLM agentic systems underperform.

### S8. Mismatch-Decomposition Has Adversarial-Robustness Implications

`result-mismatch-decomposition` decomposes mismatch into model-error + parameter-error + structural-error. **Speculative:** adversarial attacks target one specific component; "robustness gains in one regime trade off against another" may map to the decomposition. Cross-regime robustness has structural cost.

---

## What I Didn't Have Time / Depth to Investigate

- **Most of TST.** I read three TST segments out of 121. The change-proximity / coherence-coupling / atomic-changeset machinery has direct cross-domain relevance to organizational change-management, AI-coding-agent design that I did not systematically work through. The 14 EXACT estimators in #12's P5 are likely each a finding-shaped object; I did not work that list.
- **Logozoetic agents (`04-logozoetic-agents/`).** I read no segments. AI-welfare implications likely much richer than P1-I and S1 suggest; I'd need to read PROPRIUM ontology to ground them.
- **Empirical-validation simulations (`msc/track-b-nonlinear-sims/`).** Did not check what other empirical findings they ground.
- **Hafez et al. 2026 IDT empirical result.** Did not check whether other implications exist.
- **Reflections in `msc/reflections/`.** Did not read.
- **Adjacent fields where I lack background:** Population genetics formalisms; quantum information theory; macroeconomic monetary theory.
- **Math depth checks.** I assumed catalog derivations correct as stated; did not re-verify.
- **Whether this overlaps with prior brainstorms.** `msc/findings-undermind-priors-2026-04-26.md` exists; I did not check it.

---

## Reflection: What I Found Most Striking

**First: M3 is missing from the catalog and should not be.** The separability pattern is a *first-class* meta-architectural finding the framework already carries. M1 + M2 are real but partial. With M3 surfaced, the methodological architecture is complete: M1 names what's structurally forbidden, M2 names what's structurally forced, M3 names where AAD's results hold and under what repair. **This is the highest-priority addition to the catalog from this brainstorm.**

**Second: the catalog under-foregrounds structural economy.** Sector-persistence template (P2-B), coupled-diagnostic framework (P2-E) — these are not ancillary segments; they are the framework's most distinctive economy. The catalog presents results-as-results; the segments carry an additional *result-organization* layer the catalog doesn't surface.

**Third: the framework's negative findings are the under-told story.** P1-G (modular safety architectures fail under goal divergence), P1-I (sandbox-eval cannot reach Level-2), P1-K (mean-field VI structurally suboptimal), S1 (continuity-of-self forbidden). These are "the framework forbids what other frameworks hope to do" — high-impact, particularly for AI safety. M1 is presented constructively ("here is the unique escape") rather than negatively ("here is what cannot work"). **For external readers, the framework's negative claims may be its highest-leverage public contribution.**

What surprised me most: cross-domain unifications (which the catalog foregrounds) are the easiest-to-see contributions. Meta-architectural patterns (M1, M2, missing M3) are subtler. Negative findings are most likely to be high-impact externally but most under-foregrounded.

I came in expecting to surface composition-of-existing-findings candidates. I leave thinking the framework has more first-class meta-architectural content (M3), more first-class unification-economy content (sector-template, coupled-diagnostic, separability-pattern), and more first-class negative content than the catalog has cataloged. The brainstorm above is a partial pass at all three.
