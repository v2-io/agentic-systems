# RG-0b — Prior-Art Search: AAT-as-RG, IB-as-RG, FEP-as-RG

**Status**: complete (first pass)
**Date**: 2026-05-09
**Brief**: `00-brief.md` §5 RG-0b
**Author**: delegated prior-art sub-agent

## 0. Scope and method

This document supports `00-brief.md` §6 decision criterion (b): *"Prior-art search shows AAT-specific content beyond known IB-as-RG / FEP-as-RG analogies."* The hypothesis under test is that (A1)–(A4) of `#form-composition-closure` collectively express a renormalization-group fixed-point requirement, with $\varepsilon^*$ as flow distance from the AAT form-fixed-point.

I read `00-brief.md` and the existing project prior-art reports (`ref/Novelty_defense_and_integration.md`, `ref/Prior_art_for_unified_agency_theories.md`, `ref/separability-ladder-prior-art-report.md`). Neither prior report covers RG / coarse-graining / form-preservation under scale; the relevant sections of `Novelty_defense_and_integration.md` (Pillar III "composite agency and ε*-coordination", Markov-blanket sub-section) note only that Kirchhoff 2018 and Parr/da Costa/Friston 2019 give *conceptual* hierarchical nesting without a coarse-graining error bound, and explicitly observe that "the closest mathematical cousins to the Bridge Lemma live elsewhere."

Then six question-by-question web searches, six follow-on searches, two paper-level fetches (Friston 2019 *J. Theor. Biol.* "On Markov blankets and hierarchical self-organisation"; Friston 2025 *Front. Network Physiology* "From pixels to planning: scale-free active inference"; Mehta–Schwab 2014 arXiv abstract; the Gaussian-IB-NPRG paper). PDFs of the longer Friston papers were not fully extractable; I worked from abstracts, the Frontiers HTML, and high-quality citing summaries.

Verdict tiers used below:
- **Substantial overlap** — the prior work covers our content; we must cite and either differentiate or absorb.
- **Adjacent** — same neighborhood, different load-bearing structure; cite generously.
- **Background only** — known machinery we adopt without claim of novelty.
- **Likely novel** — no clear prior art surfaced; double-check before claiming.

The headline finding (give it now so the rest of the document is read in light of it): **the IB-as-RG and FEP-as-RG threads are not just adjacent — they are *substantially overlapping* with the framing's load-bearing core.** Friston (2019) formalizes recursive Markov-blanket coarse-graining as RG and explicitly states form-preservation as the renormalization criterion. Friston, Da Costa, et al. (2025, *Frontiers in Network Physiology*) extend this to active inference with explicit RG-flow framing and an explicit form-conservation requirement. Form-preserving coarse-graining of active-inference dynamics is established prior art, not AAT-distinctive. The AAT-specific content lives elsewhere (Q4 directed-separation-as-order-parameter, Q5 the explicit closure-defect bridge bound, Q3 the (O, Σ) recursion against a strategy-DAG with a definitional split). Verdict: **V2** (adjacent literature exists; AAT-specific structural content appears novel within that frame).

---

## 1. IB-as-RG literature

**Q1.** *How developed is the IB-as-RG thread? Does it cover (a) coarse-graining as projection, (b) form-preservation of the IB Lagrangian under flow, (c) anything resembling the AAT-shape-preserved-under-Λ requirement?*

### Key works (chronological)

**Mehta & Schwab (2014).** "An exact mapping between the Variational Renormalization Group and Deep Learning." arXiv:1410.3831. Constructs an explicit map between Kadanoff's variational RG and stacked RBMs, using the nearest-neighbor Ising model as a worked example. This is the seed paper that re-opened the IB-RG conversation in the deep-learning era.
- **What it gives us:** rigorous worked instance of "coarse-graining as projection" (RBM hidden layer = block-spin transformation). Treats RG as a flow on parameter space, with the Ising fixed-point structure preserved across layers.
- **What it doesn't give us:** no agent-architecture content; no objective/strategy decomposition; no perception-action / sensory-motor structure. The RG is over field-theoretic configurations, not over agents.

**Tishby (2019, APS March Meeting).** "The renormalization group and information bottleneck: a unified framework." Verbal talk; framing only — but the framing names exactly the bridge: RG produces a reduced description with accurate macroscopic behavior; IB determines the optimal balance between accurately conveyed features and irrelevant complexity; both are coarse-graining operations and they admit a unified description. (Citation: APS-MAR19-F66.7.)

**Kline & Palmer (2022).** "Gaussian Information Bottleneck and the Non-Perturbative Renormalization Group." *Entropy / Phys. Rev. Research* (PMC8967309). The most rigorous work in this thread. Establishes:
- A precise mapping: IB's coarsening map P_β(x̃|x) = soft-cutoff NPRG schemes, with β ↔ RG cutoff scale.
- **A semigroup composition rule** for Gaussian IB coarsenings: β₂ ∘ β₁ = β₂β₁/(β₂+β₁−1), with rescaling factor b(β) = β/(β−1) multiplying under composition. This is the form-preservation result for the IB Lagrangian — successive IB coarsenings compose into larger IB coarsenings (closed under composition).
- Soft-cutoff NPRG ↔ IB regulator R_β^(IB) ∝ diag(α_i²(β)).
- **Honest limits in the paper:** "we have not identified yet what the analogous 'model space' is in the context of IB" — fixed-point analysis (with critical exponents) is *not* developed. The form-preservation is shown; the universality-class structure that would license a full RG analysis is not.

**Gordon, Bañuls, et al. (2021) and follow-ups.** "Optimal Renormalization Group Transformation from Information Theory." *Phys. Rev. X* 10, 011037. Treats the IB-relevance criterion as the *optimal* RG choice — i.e., the RG transformation that minimizes lost information about a relevance variable. Not about agents; about Ising models and physical systems.

**Kotani, Saremi, et al. (2022, APS March Meeting).** "Information Bottleneck for Data-driven Renormalization without Locality." Extends IB-RG framing to non-local lattices.

### Verdict for Q1

Substantial prior art on the IB ↔ RG mapping itself. The semigroup composition rule (Kline & Palmer) is the closest thing in the literature to a *form-preservation theorem* for an information-theoretic Lagrangian under coarse-graining. **AAT's (P1) Lagrangian-dual update inherits this structure for free.** The RG-fixed-point treatment of the IB Lagrangian is thus background, not AAT-novel — we should cite Kline & Palmer for the semigroup result and Mehta-Schwab for the field-theoretic seed.

What is *not* in this literature: any treatment of an action loop, a strategy, a goal, or a sensorimotor partition. The coarse-graining is over relevance-encoding random variables, not over agents-with-objectives. The AAT-distinctive load (closure of the *agent* form, not just the IB form) is not preempted here.

- Coarse-graining as projection: ✓ established (Mehta-Schwab).
- IB-Lagrangian form-preservation under flow: ✓ established for Gaussian case (Kline & Palmer); semigroup result is the cleanest analog of "AAT shape preserved under Λ."
- Anything matching AAT-shape-preserved (with O, Σ, ε* structure): ✗ — AAT's form is richer than the IB Lagrangian.

Sources:
- [Mehta-Schwab 2014 arXiv:1410.3831](https://arxiv.org/abs/1410.3831)
- [Kline & Palmer (Gaussian IB and NPRG), PMC8967309](https://pmc.ncbi.nlm.nih.gov/articles/PMC8967309/)
- [Tishby APS 2019 abstract](https://ui.adsabs.harvard.edu/abs/2019APS..MARF66007T/abstract)
- [Gordon et al. 2020, Phys. Rev. X 10, 011037](https://link.aps.org/doi/10.1103/PhysRevX.10.011037)

---

## 2. FEP-as-RG literature

**Q2.** *Has anyone formalized "active inference's form is preserved under coarse-graining"? Any RG fixed-point treatment of Markov-blanket nesting?*

This is the literature with the strongest preemption pressure on the AAT-as-RG framing.

### Key works

**Friston (2019).** *J. Theor. Biol.*, "On Markov blankets and hierarchical self-organisation" (with Heins, Da Costa, Parr). The load-bearing claim: any random dynamical system with sparse coupling and an implicit Markov-blanket partition is **renormalizable** — and the recursion of Markov-blanket-bearing systems can be formalized via the RG that emerges from grouping/coarse-graining operators on Markov blankets.

The paper explicitly states (per cited summaries — I could not extract the PDF directly, see §0 caveat):
- A working definition of renormalization rests on three things: (i) vectors of random variables, (ii) a coarse-graining operation, and (iii) a requirement that the operation does not change the functional form of the Lagrangian to within a multiplicative constant.
- Markov-blanket recursion is shown in simulation: ensembles of cells with blankets self-organize into multicellular structures that themselves carry Markov blankets (Eq. 5: f_μ(s,a,μ) = (Q_μ − Γ_μ)∇_μ F and f_a(s,a,μ) = (Q_a − Γ_a)∇_a F — same gradient-descent functional form across scales).
- Explicit claim: "the same basic (Bayesian or variational) mechanics emerge in a scale-free fashion at different levels."

**This is the central preemption.** The AAT framing's mapping table — coarse-graining = Λ; form-preservation = (A1)–(A4); AAT-form-preservation under Λ — has a direct ancestor in Friston 2019, where the form-preservation is for free-energy gradient dynamics rather than for AAT-form. The functional move ("the macro-system must itself be an X-agent, where X-form is preserved by coarse-graining") is *not* novel to AAT; Friston established it for FEP/active-inference six years earlier.

**Friston, Heins, Verbelen, Da Costa et al. (2025).** *Frontiers in Network Physiology*, "From pixels to planning: scale-free active inference." This is the most directly load-bearing paper. The opening claim:

> "The renormalization group requires that the functional form of the dynamics (e.g., belief updating) is conserved over levels or scales."

(Located in the introduction.) The paper develops "renormalising generative models" (RGMs) as discrete-state-space models that *by construction* are scale-invariant — the message-passing updates have identical functional form across hierarchical levels, with only parameter values changing. Explicit framing in their introduction: "Any random dynamical system with sparse coupling and an implicit Markov blanket partition is renormalizable." (Verbatim quote, per the Frontiers HTML.)

Beyond form-preservation, the 2025 paper:
- Notes that scale transformations entail a coarse-graining that **induces a separation of temporal scales**, with belief updating slowing at higher levels — i.e., the macro-tempo separation that AAT's K_c parameter encodes. **This directly preempts the AAT claim that K_c → ∞ corresponds to the RG fixed-point regime.**
- Discusses fixed points in the variational sense: "The expressions in Figure 2 are effectively the fixed points (i.e., minima) of variational free energy." But this is fixed-point-of-the-flow (steady state of belief), not fixed-point-under-RG-coarse-graining; the 2025 paper does not push the latter to a critical-exponent / order-parameter framework.
- Notes a perception-action-like segregation under temporal RG: "The separation into predictive posteriors over states and paths has a clear homology with the segregation of processing in the visual cortical hierarchy." This is described as an *emergent* dorsal-ventral / what-vs-where segregation, not as a designed structural condition. It is the closest thing in this literature to "directed separation under coarse-graining."

**Hesp, Ramstead, Constant, Badcock, Kirchhoff, Friston (2019).** "A Multi-scale View of the Emergent Complexity of Life: A Free-Energy Proposal" (chapter in *Evolution, Development and Complexity*). Develops the multi-scale FEP framing: blankets recursively across scales (cells → organs → organisms → eco-niches), with the same FEP dynamics at each scale. Conceptual rather than RG-formal — does not develop the explicit coarse-graining operator.

**Ramstead, Kirchhoff, Constant, Friston (2021).** "Multiscale integration: beyond internalism and externalism." *Synthese*. Formalizes that the "particular statistical form and specific partitioning rule that governs the Markov blanket allows for the assembly of larger and larger Markov blankets" because they "recapitulate the statistical form" at higher scales. This is form-preservation of the *blanket structure* (as opposed to the Lagrangian) under aggregation, but framed philosophically rather than as RG.

**Kirchhoff, Parr, Palacios, Friston, Kiverstein (2018).** "The Markov blankets of life: autonomy, active inference and the free energy principle." J. R. Soc. Interface. The paper that established "blankets all the way down / all the way up." Already present in `ref/`. Conceptual and statistical; Friston 2019 is what added the RG operator.

**Parr, Da Costa, Friston (2019).** "Markov blankets, information geometry and stochastic thermodynamics." Phil. Trans. R. Soc. A. Already in `ref/`. Foundational for the variational thermodynamic frame; not the RG paper per se.

**Friston (2019, arXiv:1906.10184).** "A free energy principle for a particular physics." Already in `ref/`. The canonical Bayesian-mechanics monograph. Includes the recursive-blanket framing and the "implicit renormalization group that furnishes a particular perspective on quantum, statistical and classical mechanics" — i.e., the *physics* version of the form-preservation claim. Highly relevant; should be cited as the substrate work.

### What is and isn't in the FEP-RG literature

**What is established (and therefore not AAT-novel):**
- "Active-inference's form is preserved under coarse-graining" — yes, Friston 2019 *J. Theor. Biol.* and Friston et al. 2025 RGM.
- "Markov-blanket-bearing systems are renormalizable, modulo a sparse-coupling assumption" — yes, Friston 2019.
- "Coarse-graining induces temporal-scale separation; belief updating slows at higher scales" — yes, Friston et al. 2025. **This directly mirrors AAT's $\nu_{n+1} \ll \nu_n$ and the K_c regime.**
- "Recursive Markov-blanket nesting (blankets-of-blankets)" — yes, Kirchhoff 2018 and follow-ups.
- "Functional-form invariance as the renormalization criterion" — yes, Friston 2019 *J. Theor. Biol.* states this as a definition.

**What is *not* in the FEP-RG literature (and therefore where AAT-distinctive content can land):**
- A *fixed-point error bound* characterizing distance from the form-preserved ideal as a measurable defect (AAT's ε* and the bridge lemma). The closest analog — Friston 2025 RGM's expected-free-energy gating of update acceptance — is a halting condition, not a flow-distance measure.
- An order-parameter classification of *modularity / directed-separation classes* under coarse-graining (modular / partial / merged → stable / marginal / unstable fixed-point types). The FEP-RG literature treats Markov-blanket presence as binary (system is renormalizable iff sparsely coupled) and does not develop the order-parameter view. The closest hint in the literature is the "sparse coupling" condition itself, which functions as an implicit binary version — but not as a graded order parameter with critical-exponent structure. **This is where the AAT-distinctive Q4 result lives.**
- An explicit treatment of an *objective-strategy* (O, Σ) decomposition that is itself recursive — sub-objectives at sub-strategy nodes. FEP has a single thing (free energy) playing both roles; AAT's definitional split between O (evaluation) and Σ (guidance) gives the recursion a different formal handle than what the FEP-RG literature provides.
- An explicit *closure-defect bridge lemma* with the form $\lim\|e_m\| \leq \varepsilon^* \nu_c / \alpha_c$ — i.e., a coarse-graining error bound stated as a control-theoretic predictive-loss. The 2026-04-21 audit finding (cited in `Novelty_defense_and_integration.md`) is correct: "no Markov-blanket paper proves the kind of control-theoretic Bridge Lemma described in ASF."

### Verdict for Q2

**Substantial overlap.** The form-preservation framing for active-inference under coarse-graining is established prior art (Friston 2019, Friston et al. 2025). AAT must cite generously and cannot claim the form-preservation move as novel.

The AAT-specific load-bearing content within this overlap is: (i) the closure-defect bridge lemma quantifying flow-distance from the fixed point; (ii) the directed-separation order-parameter classification; (iii) the (O, Σ) recursion against a strategy-DAG with a definitional split between objective and strategy. None of these surfaced in the FEP-RG searches.

Sources:
- [Friston et al. 2019, *J. Theor. Biol.* (PMC7284313)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7284313/)
- [Friston et al. 2025, *Front. Network Physiology* (HTML)](https://www.frontiersin.org/journals/network-physiology/articles/10.3389/fnetp.2025.1521963/full)
- [Friston et al. 2025, arXiv:2407.20292 (PDF)](https://arxiv.org/abs/2407.20292)
- [Hesp et al. 2019 multi-scale FEP](https://philarchive.org/rec/KIRAMV)
- [Ramstead et al. 2021 multi-scale integration](https://link.springer.com/article/10.1007/s11229-019-02115-x)

---

## 3. Agent architecture as RG / self-similar / fractal

**Q3.** *"Renormalization group" + "agent architecture", "self-similar agency", "fractal agents", "scale-invariant agency", "hierarchical agent RG". Does Kirchhoff 2018 hierarchical-blanket nesting include RG-flow content?*

### Findings split into two clusters

**Cluster A — Active-inference hierarchical agency.** This is the same cluster as §2; the RG-flow content lives in Friston 2019 *J. Theor. Biol.* and Friston et al. 2025 RGM. Kirchhoff et al. 2018 "Markov blankets of life" itself stops at "blankets contain blankets" — its hierarchy claim is statistical and conceptual, not RG-flow. The RG operator was added later by Friston 2019.

**Cluster B — "Fractal" / self-similar agentic LLMs and other recent informal work.** A distinct cluster of mostly-non-academic work over 2023–2026:
- "The Fractal Nature of Agentic LLMs: The Next Evolution in Artificial Intelligence" (Pablo Torre, Medium, 2024). Conceptual essay. Three-level L1/L2/L3 hierarchy (foundation models → agent networks → meta-architectures) presented as fractal. No formal RG content; not a peer-reviewed source.
- "Fractal Flux AGI II" (McPhetridge, Medium / PhilArchive, 2025). Speculative framework; not research-grade.
- "From Fractal Geometry to Fractal Cognition" (Frontiers in Fractal Geometry, 2025). Cognitive-science review of recursive hierarchical embedding (RHE) — about how minds *represent* fractals, not about agent-architecture-as-RG.
- "Self-similarity and recursion as default modes in human cognition" (Martins, *Frontiers in Psychology* / *Cortex* 2014). Cognitive-science framing; not RG.
- TinyAGI's "fractals" GitHub (2024-2026). Engineering tool that runs a self-similar tree of subtasks in worktrees. Practical, not theoretical.

This cluster is informal, mostly opinion-and-essay-grade, and does not carry RG-flow mathematical content. Citing it would be a courtesy at best; differentiating from it is straightforward (none of these establish form-preservation under a coarse-graining operator with a fixed-point analysis).

### Verdict for Q3

For *formal* "agent architecture as RG" content: the only credible thread is the FEP-RG one already covered in §2. The "fractal agent" / "self-similar agentic LLM" cluster is informal and does not preempt formal claims. Kirchhoff 2018 has the recursive-blanket structure but does not include the RG operator; the operator was added by Friston 2019.

**Adjacent, no formal preemption** outside the FEP-RG thread already covered. The AAT-specific (O, Σ) recursion against a *formal* DAG with explicit type structure — checked by RG-0c against `#def-strategy-dimension` — has no surfaced equivalent.

Sources:
- [Kirchhoff et al. 2018 (rsif)](https://royalsocietypublishing.org/rsif/article/15/138/20170792/35768/The-Markov-blankets-of-life-autonomy-active)
- (informal cluster — not citing individually)

---

## 4. Modularity as RG order parameter

**Q4.** *Has anyone treated agent modularity (factorability / separability / decomposability) as an order parameter under coarse-graining?*

This is the question I expected most preemption pressure on; the result is the opposite.

### Findings

**Cluster A — Categorical / compositional treatments of separability** (Capucci, Smithe, Baez, Spivak, etc.). T. S. C. Smithe's "Structured Active Inference" (arXiv:2406.07577, 2024) casts active inference as systems-on-an-interface using categorical systems theory; the Markov blanket becomes a compositional abstraction of an interface, and agents are 'controllers' for their generative models. Capucci, Gavranović, Hedges et al. on para-categorical lenses and parametric maps are in the same neighborhood. **What this cluster gives us:** rigorous compositional structure for nesting. **What it doesn't:** the categorical machinery is not framed as an RG flow, and modularity is treated as either present or not (the morphism either factors through an interface or it doesn't), not as a graded order parameter under coarse-graining.

**Cluster B — Factorised / structured active inference.** "Factorised Active Inference for Strategic Multi-Agent Interactions" (arXiv:2411.07362, 2024). Treats factorisation of generative models as an architectural choice; not as an order parameter under coarse-graining. The factorisation is *given* and the dynamics studied; the inverse question (under what conditions does factorisation survive coarse-graining?) is not posed.

**Cluster C — Network-criticality / phase-transition treatments of modularity.** "Influence of topology on the critical behavior of hierarchical modular neuronal networks" (Comm. Phys., 2025). Modular sparse architectures sustain criticality more robustly than fully connected ones — i.e., modularity matters for criticality. But this is criticality of the dynamics on a fixed network, not modularity-as-order-parameter under a coarse-graining flow. The paper's "modularity" is a network-structural feature, not a property that flows under RG.

**Cluster D — MDP-homomorphism / approximate-aggregation literature.** Ravindran & Barto's algebraic approach to abstraction in RL (2004 and follow-ups), Taylor-Precup-Panangaden bounding performance loss in approximate MDP homomorphisms (2008), Abel et al. value-preserving state-action abstractions (2020), Congeduti-Mey-Oliehoek loss bounds for approximate influence-based abstraction (2020 — already cited as \[Con20\] in `Novelty_defense_and_integration.md`). Subramanian-Mahajan approximate information states (2020 — already cited as \[Sub20\]). Continuous MDP homomorphisms with policy-gradient (NeurIPS 2022). **What this cluster gives us:** rigorous error bounds for control under coarse-graining — exactly the bridge-lemma neighborhood. **What it doesn't:** the abstraction relation is taken as given; the question of whether the homomorphism property is preserved under iteration (i.e., is the abstraction an RG fixed point?) is not posed in this literature. Modularity / factorisation is also not an order parameter — it's a property the abstraction has or doesn't.

**Cluster E — Symmetry-breaking treatments of separability.** Fields, Glazebrook, et al. "Representing Measurement as a Thermodynamic Symmetry Breaking" (Symmetry, 2020): allocating bits to system identification breaks two symmetries via two separability constraints. Closer in spirit to the order-parameter framing — separability emerges/breaks across a transition. But the construction is for measurement-vs-system, not perception-vs-action under hierarchical aggregation.

### What does *not* appear in the literature

I could not find any work that does all three:
1. Treats modularity / separability of an agent as a measurable order parameter (a graded quantity, not a binary).
2. Studies its flow under a coarse-graining / aggregation operator.
3. Classifies the resulting fixed-point types (stable / marginal / unstable) as architectural classes.

The directed-separation classification from `#der-directed-separation` (modular / partial / merged) — when reframed as RG fixed-point types — appears to have no clear prior-art equivalent. **This is the strongest AAT-distinctive piece in the RG framing.**

### Verdict for Q4

**Adjacent literature exists; the AAT-specific structural content (modularity as flow-graded order parameter classifying fixed-point types) appears novel.** The MDP-homomorphism literature (Cluster D) is the closest mathematical neighbor on the bridge-lemma side; Friston 2019 is the closest on the form-preservation side. Neither develops the order-parameter view. The path is to cite Cluster D for control-theoretic abstraction-bounds (already in `Novelty_defense_and_integration.md`) and to position the AAT directed-separation order-parameter as the synthesis-step adding the order-parameter view to that established machinery.

Genuine novelty here is conditional on RG-0a Case-B confirming the predicted K_c-invariance for heterogeneous gains (the "relevant operator" prediction). Without that simulation result, the order-parameter framing is suggestive rather than load-bearing.

Sources:
- [Smithe 2024 Structured Active Inference (arXiv:2406.07577)](https://arxiv.org/abs/2406.07577)
- [Factorised Active Inference (arXiv:2411.07362)](https://arxiv.org/html/2411.07362v1)
- [Ravindran 2004 thesis (algebraic RL abstraction)](https://all.cs.umass.edu/pubs/2004/ravindran_thesis04.pdf)
- [Abel et al. 2020 value-preserving abstractions](http://proceedings.mlr.press/v108/abel20a/abel20a.pdf)
- [Hierarchical modular neuronal networks 2025](https://www.nature.com/articles/s42005-025-02074-5)

---

## 5. Approximate dynamical homomorphism + composition as RG fixed-point

**Q5.** *ASF's bridge lemma is in this neighborhood. Has this been treated as an RG fixed-point condition for compositional control?*

### Findings

**Direct neighbor in control theory:** Tabuada, Pappas, Girard et al. — "Hierarchical control system design using approximate simulation" (Automatica, 2009); follow-ups on simulation-function-based hierarchical control with bounded error. Provides the cleanest control-theoretic version of "abstract system tracks concrete system within ε" — i.e., AAT's bridge lemma in different vocabulary. **Form-preservation under iteration is *not* explicitly studied;** the simulation function is constructed once, not iterated as a flow.

**Coarse-graining for control equivalence (Liu, Slotine, Barabási et al., 2024).** "Coarse-graining Complex Networks for Control Equivalence" (arXiv:2312.07421). Algorithm produces a coarse-grained network with control-equivalence: optimal control values for the original network can be recovered from the aggregated one. **Closer to AAT-style closure than the simulation-function literature;** the macro-input enters the coarse-grained network such that each macro-state preserves the sum of corresponding original-network states. But again: not framed as an RG flow with iteration / fixed-point analysis.

**MDP-homomorphism cluster (Ravindran-Barto, Taylor-Precup-Panangaden, Abel, etc. — see Q4).** Treats homomorphism approximately, with predictive-loss bounds — but iteration of the abstraction is not foregrounded as RG flow. The closest item in spirit: Abel et al.'s "value-preserving state-action abstractions" treats abstraction-quality as graded, but composing abstractions is not analyzed.

**Categorical / lens-based treatments (Capucci, Smithe).** Composition is the central operation; admissibility of nested abstractions is treated structurally. Form-preservation under composition is *built in* (composition of lenses is again a lens); fixed-point analysis under iteration is not explicit.

### Verdict for Q5

**Adjacent literature exists, but the RG-fixed-point framing of the bridge lemma is not in the literature.** The control-theoretic neighbors (simulation functions, coarse-graining for control equivalence, MDP homomorphisms) provide the right vocabulary for the bridge lemma as a single coarse-graining error bound, and AAT should cite them — but they do not iterate the abstraction as a flow nor pose the fixed-point question. Categorical work (lenses, structured active inference) builds in compositional form-preservation but does not provide the error-bound / order-parameter machinery.

The AAT-specific content here is the *combination*: a control-theoretic predictive-loss bound (from the homomorphism / simulation-function tradition) framed as flow-distance from the form-preserved ideal (from the FEP-RG / IB-RG tradition), with the form-preservation requirement made explicit as (A1)–(A4). Each ingredient has prior art; the synthesis appears not to.

Sources:
- [Tabuada-Pappas hierarchical simulation control (Automatica 2009)](https://www.sciencedirect.com/science/article/abs/pii/S0005109808004731)
- [Coarse-graining for control equivalence (arXiv:2312.07421)](https://arxiv.org/html/2312.07421)
- [Taylor-Precup-Panangaden 2008 NIPS bounding loss in approximate MDP homomorphisms](https://proceedings.neurips.cc/paper/2008)
- [Abel et al. 2020 value-preserving abstractions](http://proceedings.mlr.press/v108/abel20a/abel20a.pdf)

---

## 6. Singular perturbation + RG

**Q6.** *AAT uses Tikhonov-style timescale separation. Has anyone connected singular perturbation to RG flow for adaptive systems specifically?*

### Findings

**Established mathematical connection.** Chen, Goldenfeld, Oono (1994, 1996) — "Renormalization group and singular perturbations: Multiple scales, boundary layers, and reductive perturbation theory." *Phys. Rev. E* 54, 376. **Foundational paper.** Establishes that the RG method *is* a unified singular-perturbation method that subsumes:
- the averaging method
- the multiple time-scale method
- (hyper)normal forms theory
- center-manifold reduction
- geometric singular-perturbation method
- phase-reduction methods

**Cited follow-ups:**
- Chiba 2009, "Extension and Unification of Singular Perturbation Methods for ODEs Based on the Renormalization Group Method" (SIAM J. Appl. Dyn. Syst. 8, 1066). Extends the framework, shows the RG equation derives the slow-manifold reduction.
- Petropoulos & Giona (2018), "Singular perturbed renormalization group theory and its application to highly oscillatory problems."
- Multiple papers on stochastic singular perturbation + RG.

**For control specifically:** "Multi-time scale control and optimization via averaging and singular perturbation theory: From ODEs to hybrid dynamical systems" (Naidu et al., 2023) — the standard control-theoretic survey. Treats singular perturbation as a tool for hierarchical control synthesis; does not invoke RG.

### Verdict for Q6

**Background, well-established.** The Chen-Goldenfeld-Oono identification of RG with singular-perturbation theory is canonical mathematics that AAT inherits for free. The Tikhonov timescale-separation in `#der-temporal-nesting` and the K_c → ∞ regime in `#form-composition-closure` map directly onto the slow-manifold reduction that RG-theory shows is one face of singular perturbation.

**No specific preemption for AAT;** these are tools. Citation discipline: cite Chen-Goldenfeld-Oono 1994 as the canonical RG-singular-perturbation bridge and note that AAT's nested-loop temporal structure inherits this machinery via Tikhonov.

What this *suggests* (but does not require): the K_c → ∞ regime, in which AAT's macro-system becomes a clean composite agent, is structurally the slow-manifold limit of a singular-perturbation problem. RG-0a Case A's prediction of exponential decay in K_c with rate λ = 1 − α/ν is exactly the kind of irrelevant-operator decay that singular-perturbation-RG analysis predicts for transient corrections to the slow manifold. **This is not a coincidence; it's a structural reason the RG framing is plausible.** But the connection is tools-level, not novelty-claim-level.

Sources:
- [Chen, Goldenfeld, Oono 1996 *Phys. Rev. E* 54, 376](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.54.376)
- [Chiba 2009 SIAM J. Appl. Dyn. Syst.](https://ui.adsabs.harvard.edu/abs/2009SJADS...8.1066C/abstract)
- [Naidu et al. 2023 multi-time scale control survey](https://www.sciencedirect.com/science/article/pii/S1367578823000901)

---

## 7. Cross-checks against existing project prior-art reports

**`ref/Novelty_defense_and_integration.md`.** Pillar III (composite agency / ε*-coordination): explicitly notes that "the search did not uncover a Markov blanket paper that proves the kind of control-theoretic Bridge Lemma described in ASF." The Markov-blanket papers \[Par19, Kir18\] are flagged as conceptual hierarchy, not coarse-graining error bounds. \[Sub20\] approximate-information-states is flagged as the closest mathematical cousin but "not framed as composite agency or organizational closure." This is consistent with my §2/§5 verdicts.

**`ref/Prior_art_for_unified_agency_theories.md`.** Lists the FEP / Markov-blanket cluster (\[Fri19\] Bayesian mechanics, \[Par19\] info-geometry, \[Kir18\] blankets-of-life) but does not separately catalogue the RG-flow / form-preservation thread (Friston 2019 *J. Theor. Biol.* / Friston 2025 RGM). **This is a real gap — the existing report under-represents the FEP-RG literature** because the prior search was scoped on "unified agency theories" not "scale-free / coarse-graining". The RGM 2025 paper in particular postdates that report's cutoff.

**`ref/separability-ladder-prior-art-report.md`.** Did not surface in the standalone-paper proposal as covering RG-style framing of separability. (Per `feedback_separability_ladder_paper.md`: Hintikka 1991 is the historical anchor for separability; Undermind sweep verified novel for the standalone-separability-ladder result.) Separability-as-RG-order-parameter does not appear in this report either.

### Implication

**The existing project prior-art reports under-represent the FEP-RG / scale-free-active-inference thread.** If this RG framing proceeds, `Novelty_defense_and_integration.md` should be updated (or supplemented) to include Friston 2019 *J. Theor. Biol.* and Friston et al. 2025 RGM as substrate works whose form-preservation framing AAT adopts (per AAT's prior-art-integration discipline) and whose specific results AAT differentiates from on (i) bridge-lemma-as-flow-distance, (ii) directed-separation-as-order-parameter, (iii) (O, Σ) recursion against a typed strategy DAG.

---

## 8. Bottom-line verdict for §5 of the brief

**Verdict: V2 — Adjacent literature exists, must cite generously, AAT-specific structural content appears novel.**

Decomposed:

**What is preempted (must adopt + cite, cannot claim as AAT novelty):**
- The form-preservation requirement as the renormalization criterion — Friston 2019 *J. Theor. Biol.* states this verbatim.
- Active-inference / Markov-blanket dynamics as form-preserved under coarse-graining — Friston 2019 + Friston 2025 RGM.
- The IB Lagrangian as form-preserved under iteration via a semigroup composition — Kline & Palmer 2022 (Gaussian case).
- RG as the framework subsuming singular-perturbation timescale-separation — Chen-Goldenfeld-Oono 1996.
- "Recursive Markov blankets all the way down" — Kirchhoff 2018.
- Coarse-graining inducing temporal-scale separation (slowed belief-updating at higher scales) — Friston 2025 RGM. **This directly mirrors AAT's $\nu_{n+1} \ll \nu_n$ and the K_c regime; we cannot claim that mapping as novel.**

**What appears AAT-distinctive within this frame:**
- (i) The closure-defect bridge lemma as a *control-theoretic predictive-loss bound* on flow-distance from the AAT form-fixed-point. The FEP-RG literature lacks this; the MDP-homomorphism / simulation-function literature has bounds but does not iterate the abstraction as flow. AAT's combination is the synthesis-step.
- (ii) Directed-separation classes (modular / partial / merged) as RG-fixed-point types (stable / marginal / unstable) — i.e., **modularity as a graded order parameter under the coarse-graining flow.** Q4 search found no equivalent. This is the strongest AAT-distinctive piece, *conditional on RG-0a Case B confirming the predicted K_c-invariance for heterogeneous gains.*
- (iii) The (O, Σ) recursion against a typed strategy DAG (`#def-strategy-dimension`, `#def-strategy-dag`). FEP-RG has a single quantity (free energy) playing both objective and strategy roles; AAT's definitional split between O (evaluation) and Σ (guidance) gives this a different formal handle than the FEP-RG literature's recursive-blankets-of-blankets. The fractal-agent informal cluster has nothing rigorous here; the categorical-structured-active-inference cluster has compositional structure but not the explicit O/Σ split. RG-0c is the right gate to test this against the formal definitions.

**What this means operationally for the spike track:**

1. **The framing is real, but its load-bearing AAT content is narrower than first hoped.** The form-preservation move and the RG-as-coarse-graining mapping are not AAT-novel; they're adopted from Friston 2019 / Friston 2025 / Kline-Palmer 2022 / Chen-Goldenfeld-Oono 1996. AAT's contribution is the *synthesis with control-theoretic bridge bounds and an order-parameter view of modularity*, plus the (O, Σ) recursion specific to AAT's strategy-DAG formalism.

2. **§6 decision criterion (b) is satisfied conditionally.** "Prior-art search shows AAT-specific content beyond known IB-as-RG / FEP-as-RG analogies" — yes, on Q4 (modularity-as-order-parameter) and on the bridge-lemma-as-flow-distance synthesis. But this is *conditional* on RG-0a Case B confirming the predicted K_c-invariance; without that simulation result, the order-parameter framing is suggestive rather than load-bearing. The verdict therefore depends on RG-0a, which is the load-bearing math by design.

3. **The framing should not be presented as "AAT is the RG of agency" with implied first-mover novelty.** It should be presented as "AAT inherits the form-preservation framing from the FEP-RG / IB-RG / singular-perturbation-RG thread, and contributes (i) a control-theoretic bridge-lemma quantification, (ii) a directed-separation order-parameter classification, (iii) an (O, Σ) recursion against a typed strategy DAG." This is per AAT's prior-art integration discipline (`CLAUDE.md` §Prior art integration: "AAT's contribution is integration, not invention").

4. **Recommended citation discipline if RG framing proceeds (RG-1..4):**
   - Cite Friston 2019 *J. Theor. Biol.* and Friston et al. 2025 RGM (Frontiers in Network Physiology) as the substrate works for FEP form-preservation under coarse-graining.
   - Cite Mehta-Schwab 2014 and Kline-Palmer 2022 for IB-as-RG.
   - Cite Chen-Goldenfeld-Oono 1996 and Chiba 2009 for the singular-perturbation–RG identification.
   - Cite Kirchhoff 2018 (already in `ref/`) for recursive-blanket structure.
   - Cite Tabuada-Pappas approximate-simulation hierarchical control and the MDP-homomorphism cluster (Ravindran-Barto, Taylor-Precup-Panangaden, Abel) as the control-theoretic bridge-lemma neighbors.
   - In `Novelty_defense_and_integration.md`: add a sub-pillar "form-preservation under coarse-graining" under Pillar III, with the Friston 2019 / 2025 anchor. The existing report under-represents this thread.

5. **Framing-failure scenarios (drop the framing if these are realized):**
   - RG-0a Case B does not show K_c-invariance → the order-parameter framing collapses; what remains is just "AAT's form-preservation matches Friston's", which is true but adds nothing beyond restating Friston 2019.
   - RG-0c reveals (O, Σ) recursion is *not* well-formed against `#def-strategy-dimension` (e.g., internal Σ-nodes don't legitimately carry sub-objectives) → the third AAT-distinctive piece is gone; only (i) and (ii) remain.
   - Both fail → drop the framing, keep only the simpler "nested cycles via template instantiation" result per `00-brief.md` §6.

6. **Spot-check pointer for §5 of the brief.** The single most important paper to read in full is **Friston, Heins, Verbelen, Da Costa et al. (2025), "From pixels to planning: scale-free active inference," *Frontiers in Network Physiology* 7:1521963**. Its introduction states the RG form-preservation requirement explicitly; its Algorithm 1 implements RG via blocking transformations on Dirichlet parameters; its discussion of temporal-scale separation under coarse-graining is the most direct preemption of the "K_c regime as RG fixed-point" mapping. If RG-1..4 proceed, this is the paper to differentiate from in the segment-level Discussion section, not just cite.

   Section to look at first (per `00-brief.md`'s standard for spot-checkability): Introduction, paragraphs around the "implicit RG flow rests on the inclusion of dynamics in the generative model" claim and the "renormalization group requires that the functional form of the dynamics is conserved" sentence. Then Algorithm 1 for the blocking-transformation construction. Then the worked example (video compression) for the dorsal-ventral-segregation-under-RG point that mirrors directed-separation-under-coarse-graining.

---

## File index

- This file: `02-prior-art-rg-ib-fep.md`
- Brief: `00-brief.md`
- Load-bearing math (in progress, separate sub-task): `01-rg-0a-two-kalman-Kc-extension.md`
- (O, Σ) recursion check (gated on RG-0a positive): `03-rg-0c-strategy-recursion.md`
- Synthesis: `99-verdict.md`

## Sources (all)

- [Mehta & Schwab 2014, arXiv:1410.3831](https://arxiv.org/abs/1410.3831)
- [Tishby APS March Meeting 2019 abstract](https://ui.adsabs.harvard.edu/abs/2019APS..MARF66007T/abstract)
- [Kline & Palmer 2022 (Gaussian IB and NPRG)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8967309/)
- [Gordon et al. 2020, Phys. Rev. X 10, 011037](https://link.aps.org/doi/10.1103/PhysRevX.10.011037)
- [Friston et al. 2019, *J. Theor. Biol.*, On Markov blankets and hierarchical self-organisation](https://pmc.ncbi.nlm.nih.gov/articles/PMC7284313/)
- [Friston et al. 2025, *Frontiers in Network Physiology*, From pixels to planning: scale-free active inference](https://www.frontiersin.org/journals/network-physiology/articles/10.3389/fnetp.2025.1521963/full)
- [Friston et al. 2025, arXiv:2407.20292 (PDF)](https://arxiv.org/abs/2407.20292)
- [Friston 2019, A free energy principle for a particular physics, arXiv:1906.10184](https://arxiv.org/abs/1906.10184)
- [Hesp, Ramstead, Constant, Badcock, Kirchhoff, Friston 2019, A Multi-scale View of the Emergent Complexity of Life](https://philarchive.org/rec/KIRAMV)
- [Ramstead, Kirchhoff, Constant, Friston 2021, Multiscale integration: beyond internalism and externalism, *Synthese*](https://link.springer.com/article/10.1007/s11229-019-02115-x)
- [Kirchhoff, Parr, Palacios, Friston, Kiverstein 2018, Markov blankets of life, J. R. Soc. Interface](https://royalsocietypublishing.org/rsif/article/15/138/20170792)
- [Parr, Da Costa, Friston 2019, Markov blankets, information geometry and stochastic thermodynamics, Phil. Trans. R. Soc. A](https://royalsocietypublishing.org/doi/abs/10.1098/rsta.2019.0159)
- [Smithe 2024, Structured Active Inference, arXiv:2406.07577](https://arxiv.org/abs/2406.07577)
- [Factorised Active Inference 2024, arXiv:2411.07362](https://arxiv.org/html/2411.07362v1)
- [Ravindran 2004 thesis, Algebraic approach to abstraction in RL](https://all.cs.umass.edu/pubs/2004/ravindran_thesis04.pdf)
- [Abel et al. 2020, Value-preserving state-action abstractions](http://proceedings.mlr.press/v108/abel20a/abel20a.pdf)
- [Tabuada-Pappas 2009, Hierarchical control via approximate simulation, Automatica](https://www.sciencedirect.com/science/article/abs/pii/S0005109808004731)
- [Liu et al. 2024, Coarse-graining for control equivalence, arXiv:2312.07421](https://arxiv.org/html/2312.07421)
- [Chen, Goldenfeld, Oono 1996, RG and singular perturbations, *Phys. Rev. E* 54, 376](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.54.376)
- [Chiba 2009, Extension and unification of singular-perturbation methods via RG, SIAM J. Appl. Dyn. Syst.](https://ui.adsabs.harvard.edu/abs/2009SJADS...8.1066C/abstract)
- [Naidu et al. 2023, Multi-time scale control survey](https://www.sciencedirect.com/science/article/pii/S1367578823000901)
- [Hierarchical modular neuronal networks 2025, Comm. Phys.](https://www.nature.com/articles/s42005-025-02074-5)
