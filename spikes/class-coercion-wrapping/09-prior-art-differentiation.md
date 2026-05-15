# Sub-spike I — Prior-Art Differentiation for the Wrapping Construction

**Status**: complete (first pass)
**Date**: 2026-05-09
**Brief**: `00-brief.md` §5.I (sub-spike I)
**Author**: delegated prior-art sub-agent

## 0. Posture, scope, method

This is a **truth-finding** sub-spike, not a paper-novelty audit. Per AAT's prior-art-integration discipline (`CLAUDE.md` §Prior art integration: *"AAT's contribution is integration, not invention. The individual pieces are mostly known; the synthesis is the contribution. Trying to make every piece unique is NIH syndrome."*), the working aim is to find **what is true** about how the wrapping construction relates to prior frameworks — what those frameworks already establish, what overlaps, what is genuinely structurally distinct, and where the wrapping move *is the same as* a known move that should simply be cited and adopted.

The wrapping construction in two sentences (per `00-brief.md` §1):

> Given a Class-3 component (one whose dynamics violate directed separation $\dot M \perp G$, e.g., an LLM whose forward pass entangles belief-update and goal-conditioning), build an external scaffold with explicit $(M_W, G_W)$ state where the belief-update map $f_M$ is structurally goal-blind (no $G_W$ argument; uses queries to the component that don't carry goal information) and the strategy-update map $f_G$ may be goal-conditioned. The scaffold + component composite is then Class-1 by construction (directed separation holds at scaffold level) at a measurable cost (tempo from many component calls per macro-step, plus residual leakage if the component infers goal-information from query patterns).

The structural commitment whose prior art I am differentiating from is *the type-level enforcement of directed separation by goal-blindness of $f_M$ and $q_M$*. This is the load-bearing move; everything else (admissibility, leakage bounds, tempo cost) is consequence-tracking.

**Method.** I read the brief and the existing temporal-nesting-RG prior-art report (`spikes/temporal-nesting-rg/02-prior-art-rg-ib-fep.md`) and the strategy-recursion verdict (`spikes/temporal-nesting-rg/03-rg-0c-strategy-recursion.md`) — both already map adjacent literature thoroughly. I cross-checked against `ref/Novelty_defense_and_integration.md`. Then I worked through each of the ten questions in the brief, drawing on training-data familiarity for the canonical works (most are well-documented in training data) and supplementing with internal-repo cross-references where they sharpen the comparison. No web fetches were necessary; the relevant papers are widely-cited works the prior-art reports already characterize.

**Verdict tiers** (matching the temporal-nesting-RG report's vocabulary):
- **Substantial overlap** — prior work covers the same content; cite, adopt name, claim integration only.
- **Adjacent** — same neighborhood, structurally distinct in specific ways; cite generously, document the difference.
- **Background only** — known machinery adopted without novelty claim.
- **Different problem** — surface similarity but solving a different question.

**Headline result** (state up front so the rest is read in light of it): **the wrapping construction's load-bearing move — type-level enforcement of directed separation by goal-blindness of the belief-update channel — has substantial overlap with two prior frameworks (POMDP belief-state architectures and cognitive architectures with separated working-memory / goal-stack modules), adjacent overlap with five more (HTN / Options / MAXQ; MDP-homomorphism; hierarchical-control-via-approximate-simulation; categorical structured active inference; tool-using LLM frameworks like ReAct / MemGPT), and one cleanly differentiated counterpart (Constitutional AI / RLHF, which are structurally a different move).** Within that picture, the AAT-specific content lives in the integration with the rest of AAT machinery (sector-Lyapunov persistence, the directed-separation classification, the bridge-lemma error accounting, the Brooks's-Law tempo form), *not* in the wrapping move itself. **Verdict: V1** — see §11.

---

## 1. Q1 — MDP homomorphism / approximate state abstraction

**Prior art covered**:
- Ravindran-Barto 2004, "An algebraic approach to abstraction in reinforcement learning" (Ravindran's UMass thesis). The foundational paper on MDP homomorphisms — exact structural equivalence between MDPs and their abstractions.
- Taylor-Precup-Panangaden 2008 (NeurIPS), "Bounding performance loss in approximate MDP homomorphisms." Provides explicit error bounds.
- Abel-Hershkowitz-Littman 2016 (ICML), "Near-optimal behavior via approximate state abstraction"; Abel et al. 2020, "Value-preserving state-action abstractions" (`Abe16` / `Abe20` in the project's existing prior-art catalog).
- Subramanian-Sinha-Seraj-Mahajan 2020, "Approximate information state for approximate planning and reinforcement learning in partially observed systems" (`Sub20`). Already flagged in `Novelty_defense_and_integration.md` as the strongest direct formal neighbor to AAT's bridge lemma.
- Congeduti-Mey-Oliehoek 2020, "Loss bounds for approximate influence-based abstraction" (`Con20`). Multi-agent influence-based abstraction with explicit loss bounds.

**Construct vs. analyze (the brief's load-bearing question for this cluster)**:

The MDP-homomorphism literature is *predominantly analytic* — it takes an abstraction relation (homomorphism, bisimulation, lumping) as given and bounds the value-loss from using it. Ravindran-Barto's algebraic framework defines what an MDP homomorphism *is* and proves that exact homomorphisms preserve the optimal-policy structure; Taylor-Precup-Panangaden 2008 and Abel et al. 2016 / 2020 quantify what is lost when the homomorphism is approximate.

There is a constructive thread, but it does *not* match the wrapping construction's specific move. The constructive work in this cluster falls into two categories:
- **Search-based aggregation** (Givan-Dean-Greig 2003 stochastic bisimulation; Li-Walsh-Littman 2006 approximate aggregation algorithms). These take an existing MDP and search for state aggregations that respect transition / reward structure within a tolerance. The construction is a *clustering algorithm over an existing modular system*, not an external scaffold around a non-modular one.
- **Continuous MDP homomorphisms** (van der Pol et al. 2020 NeurIPS, "MDP homomorphic networks"; Biza-Platt-van de Meent 2022). These learn equivariant representations for policy-gradient methods. Again: compress a modular system, do not construct modularity.

**The structural difference**: every paper in this literature *assumes the existence of a coherent MDP at the lower level* (with reward function, transition kernel, etc.). The aggregation either preserves that structure (exact homomorphism) or approximates it (with error bound). The wrapping construction starts from a primitive component $A$ that is *not* an MDP at all — it is a function $\mathcal{I}_A \to \mathcal{O}_A$ — and the scaffold builds the AAT-shaped state $(M_W, G_W)$ exteriorly. The wrapper *is* the MDP-shaped object; the underlying component is not.

This is a real difference, but it is *adjacent* not *novel*. The MDP-homomorphism literature solves the well-defined problem of compressing an already-modular system. The wrapping construction solves a different problem — building modularity around an opaque oracle — but it does so using machinery (state abstraction, predictive-loss bounds) that the MDP-homomorphism literature provides. **The cleanest framing: AAT's wrapping construction *uses the MDP-homomorphism vocabulary at the wrapper-level*, but the upstream object is not an MDP.** The bridge-lemma type bounds (Subramanian-Mahajan 2020 in particular) apply once the wrapper is constructed, not before.

**Verdict for Q1**: **Adjacent**. The MDP-homomorphism literature is the right *vocabulary* for the wrapper's coarse-graining cost (tempo, leakage), but it does not establish the constructive scaffolding move. AAT should cite Ravindran-Barto 2004, Taylor-Precup-Panangaden 2008, Abel 2016/2020, and Subramanian-Mahajan 2020 generously for the bridge-lemma neighborhood (this is already done in `Novelty_defense_and_integration.md`); the wrapping construction adds the *constructive-modularity-around-non-modular-core* aspect, which this cluster does not provide. Epistemic label: verified against the existing project prior-art reports + training-data familiarity with these works.

---

## 2. Q2 — Hierarchical control / approximate simulation

**Prior art covered**:
- Tabuada-Pappas-Girard 2009, "Hierarchical control system design using approximate simulation" (Automatica). Provides simulation functions with bounded error: an abstract control system $\Sigma_a$ approximately simulates a concrete system $\Sigma$ if there is a function $V$ bounding $\|\xi - \xi_a\|$ along trajectories.
- Liu-Slotine-Barabási 2024, "Coarse-graining for control equivalence" (arXiv:2312.07421). Algorithmically aggregates network nodes preserving control equivalence: optimal control values for original network recoverable from aggregated one.

**Construct vs. analyze**:

This cluster is more constructive than the MDP-homomorphism cluster. Tabuada-Pappas-Girard explicitly *design* hierarchical controllers — they construct an abstract system together with a simulation function bounding the abstraction error. Liu-Slotine-Barabási provide an algorithm that *constructs* the coarse-grained network. So in some sense both are constructive procedures.

**Where they differ from the wrapping construction**:

Both presume a **lower-level system that is itself well-formed in their target structure** — a control system with a state space, dynamics, and inputs (Tabuada-Pappas), or a network with a known coupling matrix (Liu-Slotine-Barabási). The construction reduces / aggregates / quotients that lower system. The wrapping construction by contrast takes a primitive component that is *not* a control system — an LLM forward-pass is a function from input strings to output strings, with no externally-readable state space — and builds the control-system shape *around* it via the wrapper's $(M_W, G_W)$ external state.

That said, this is a *quantitative* difference more than a structural one. If you take the LLM-as-component and re-describe it as a degenerate control system (state = entire deployment context; dynamics = forward pass; input = query), then the wrapping construction *is* hierarchical control via approximate simulation. The wrapper is the abstract controller; the component is the concrete system; the bridge between is a simulation-function-like object characterizing how well the wrapper-level dynamics track the component-level dynamics in the relevant respects.

The structural difference reduces to: **what is being preserved**. Tabuada-Pappas-Girard preserve closed-loop trajectories (the abstract system's reachable set is close to the concrete's). The wrapping construction preserves a *modularity property* (directed separation) at the wrapper level that the concrete system does not satisfy. The simulation-function vocabulary characterizes "macro tracks micro"; the wrapping construction is closer to "macro *enforces* a property micro lacks." This is the same distinction the brief flags in §3 between *fidelity-$\varepsilon^*$* and *coercion-$\varepsilon^*$*.

**Verdict for Q2**: **Adjacent**, with the strong qualifier that the wrapping construction can plausibly be expressed in this vocabulary if one extends "what's preserved" from trajectory fidelity to architectural-property enforcement. AAT should cite Tabuada-Pappas 2009 (the canonical hierarchical-control-via-approximate-simulation reference) as the closest control-theoretic neighbor and note that the wrapper formalism *uses* the simulation-function machinery but *for a different preservation target*. Liu-Slotine-Barabási 2024 is a constructive sibling worth citing once. Epistemic label: verified against the temporal-nesting-RG prior-art report's coverage; the structural interpretation here (preservation target as the differentiator) is conjecture from training-data familiarity, plausible but not verified against the original Tabuada-Pappas paper directly.

---

## 3. Q3 — HTN / Options / MAXQ

**Prior art covered**:
- Erol-Hendler-Nau 1994, "UMCP: A sound and complete procedure for hierarchical task-network planning."
- Nau-Au-Ilghami et al. 2003, "SHOP2: An HTN planning system."
- Sutton-Precup-Singh 1999, "Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning" — the Options framework. *Artificial Intelligence* 112.
- Dietterich 2000, "Hierarchical reinforcement learning with the MAXQ value function decomposition." *JAIR* 13.

**Already mapped** by `spikes/temporal-nesting-rg/03-rg-0c-strategy-recursion.md` §6 ("Q9: Distinction from HTN / Options / MAXQ — honest scope"), which concluded that the (O, Σ) recursion in AAT is a typed instance of HTN/options/MAXQ-style hierarchical decomposition. The honest scope statement lifted from that verdict:

> "the recursion, taken on its own, is essentially the same move as options / MAXQ. AAT's contribution is the typing of the move (AND/OR, single-parameter credences, identifiability, Correlation Hierarchy, well-formedness)."

**Now the wrapping-construction question**: are HTN / Options / MAXQ doing the same move as the wrapping construction?

The brief's framing — "HTN / options decompose a goal into sub-goals; wrapping creates goal/belief separation around a non-modular component" — captures the structural difference precisely. Options and HTN decompose *along the goal axis* (a goal becomes a tree of sub-goals); the wrapping construction separates *across the belief / goal axes* (belief-update gets a goal-blind channel, strategy-update gets a goal-conditioned channel). These are orthogonal moves:

| | Decomposition direction | What's separated |
|---|---|---|
| HTN / Options / MAXQ | Vertical (within $G$) | Sub-goals within a goal hierarchy |
| Wrapping | Horizontal (across $M$/$G$) | Belief-update channel from strategy-update channel |

A wrapper *can* additionally decompose its goal hierarchy in HTN style — and indeed many real instances do (PROPRIUM's strategy DAG is hierarchical) — but the wrapping construction's load-bearing commitment is the horizontal $M$/$G$ separation, not the vertical sub-goal decomposition.

**That said**, there is an interesting overlap in the case where Options framework is used in a partially observable setting. An option's *initiation set* and *termination predicate* are functions of the *belief state*, not the goal — so the option framework already factors the belief-channel from the goal-channel at one level (the beliefs that determine option initiation are not themselves goal-conditioned; the goal selects the option). This is closer to the wrapping construction than first appears. But Options still presupposes a coherent MDP / POMDP underneath, and the goal-blind belief-update is not the structural commitment driving the framework.

**Verdict for Q3**: **Adjacent**. HTN / Options / MAXQ make a different (vertical, within-goal) decomposition move. Their machinery is partly applicable but does not establish the wrapping construction's specific (horizontal, across $M$/$G$) move. AAT should cite Sutton-Precup-Singh 1999, Dietterich 2000, and Erol-Hendler-Nau 1994 for the goal-decomposition vocabulary (already done in the temporal-nesting-RG verdict). The wrapping construction *combines* horizontal $M$/$G$ separation with whatever vertical goal-decomposition the wrapper's strategy DAG provides; the combination is the integration move. Epistemic label: verified against `03-rg-0c-strategy-recursion.md` §6 + training-data familiarity with these frameworks.

---

## 4. Q4 — Constitutional AI / RLHF / Reward Modeling

**Prior art covered**:
- Bai et al. 2022, "Constitutional AI: Harmlessness from AI feedback" (Anthropic).
- Christiano et al. 2017, "Deep reinforcement learning from human preferences" (the canonical RLHF paper).
- Ouyang et al. 2022, "Training language models to follow instructions with human feedback" (InstructGPT).

**Construct vs. analyze**:

Constitutional AI and RLHF both **shape the underlying model** — they fine-tune the weights so that the forward-pass behaves differently on subsequent inputs. The model after CAI / RLHF is a different function than the model before. The wrapping construction by contrast **does not modify the model** — the underlying component $A$ is treated as a fixed black-box oracle, called via queries from external scaffolding code.

This is a clean, well-defined structural difference:

| | What changes | When |
|---|---|---|
| RLHF / CAI | Model weights (the function $A$ itself) | Training time |
| Wrapping | External scaffold's $(M_W, G_W)$ state | Deployment time, per-step |

A model can be both RLHF'd *and* wrapped — they compose without conflict. The wrapping construction's directed-separation guarantee at the wrapper level is independent of whether the underlying $A$ has been shaped by RLHF; both increase the operational quality of the resulting system but along orthogonal axes.

**Subtle point about leakage condition (C3)**: RLHF/CAI may *worsen* the leakage situation in a specific way. By training a model to be helpful / aligned with goals, RLHF increases the model's tendency to *infer goal information from query patterns* and inject it into outputs (the very behavior the wrapping construction's C3 forbids). A pretrained-only model with no RLHF might satisfy C3 more cleanly than an RLHF'd model. This is a testable prediction of the framework, and it cleanly differentiates the wrapping move from the model-shaping move (the two interact, but adversarially in the C3-leakage axis).

**Verdict for Q4**: **Different problem**. RLHF and CAI shape the model; wrapping uses the model as a black-box. They are orthogonal interventions. AAT should cite both literatures briefly to differentiate (the interaction is informative — RLHF may worsen leakage relative to pretrained-only, which is a testable prediction). Epistemic label: verified against training-data familiarity with the canonical RLHF / CAI papers; the leakage-interaction prediction is conjecture but follows from the C3 condition straightforwardly.

---

## 5. Q5 — Categorical / structured systems theory

**Prior art covered**:
- Smithe 2024, "Structured Active Inference" (arXiv:2406.07577). Already covered in `02-prior-art-rg-ib-fep.md` §4 Cluster A.
- Capucci, Gavranović, Hedges et al. on *para-categorical lenses* and parametric morphisms (e.g., Capucci-Gavranović-Hedges-Rischel 2022, "Towards foundations of categorical cybernetics," ACT 2022).
- Spivak's compositional systems theory (Spivak-Tan 2017, "Nesting of dynamical systems and mode-dependent networks" *J. Complex Networks*; Vagner-Spivak-Lerman 2014, "Algebras of open dynamical systems on the operad of wiring diagrams").
- Baez-Pollard work on open systems (Baez-Pollard 2017, "A compositional framework for reaction networks" *Rev. Math. Phys.*).

**The relevant abstraction is the *lens*** (or *open game*, or *parametric morphism*). A lens is a pair of maps $(\text{view}, \text{update})$:
- $\text{view}: S \to V$ — extract a partial view from a state.
- $\text{update}: S \times V \to S$ — update the state given a (possibly modified) view.

The composition of lenses is itself a lens; this is the form-preservation result that lens machinery provides for free.

**The wrapping construction as a lens**:

The wrapper's $f_M$ and $f_G$ split has a natural lens reading. If we view the wrapper as a system over $(M_W, G_W)$ and the component as a sub-system being interfaced via queries, then:

- $q_M : \mathcal{X}_M \times \mathcal{O}_W \to \mathcal{Q}_A$ — a "view" that extracts the goal-blind query content from $M_W$ and the observation, *without using $G_W$*. This is essentially a *lens projecting away $G_W$*.
- $f_M : \mathcal{X}_M \times \mathcal{O}_W \times \mathcal{Q}_A \times \mathcal{O}_A \to \mathcal{X}_M$ — an update on $M_W$ that takes the component's response and incorporates it. Together with $q_M$, this is a *lens on $M_W$ that does not see $G_W$*.

The structural commitment "$f_M$'s type signature has no $G_W$ argument" is *exactly* the categorical commitment that the wrapper's belief-update lens factor through the projection $\pi_M : (M_W, G_W) \to M_W$ — i.e., the belief-update is a lens on $M_W$ alone, not on $X_W = (M_W, G_W)$.

This is a **clean categorical reading**: the wrapping construction enforces directed separation by requiring the belief-update lens to factor through the $M$-projection. Form-preservation under composition (Smithe; Capucci) gives that wrappers compose into wrappers — relevant for nested wrappers (a wrapper-of-a-wrapper is itself a wrapper), which is a natural follow-on result.

**Does this preempt the wrapping construction?**

In a deep sense, **yes** — the wrapping construction is, at a categorical level, the ordinary lens-based commitment that the belief-update factor through the $M$-projection. The categorical-systems-theory community has had this machinery for decades (Spivak-Tan 2017 is a typical reference); Smithe 2024 applies it specifically to active inference; Capucci-Gavranović-Hedges-Rischel 2022 frames the machinery for cybernetic systems generally.

**The honest reading**: the wrapping construction is *naming and operationalizing a categorical pattern* in the specific context of building Class-1 composites around Class-3 components. The categorical machinery is the abstract content; the wrapping construction applies the machinery to AAT's directed-separation classification. **This is integration, not invention.** It is also *good* integration — the categorical reading makes the construction self-evidently composable, and would clarify the form-preservation framing significantly.

**Verdict for Q5**: **Substantial overlap** at the abstract structural level. The wrapping construction is a lens-based pattern in the sense the categorical-systems-theory literature has long established. AAT should cite Smithe 2024 (canonical for active-inference) and Capucci-Gavranović-Hedges-Rischel 2022 (canonical for cybernetic systems generally) and *adopt the lens vocabulary directly* — this is the cleanest formal framing and strengthens the construction. Spivak-Tan 2017 is the operad-of-wiring-diagrams substrate; Vagner-Spivak-Lerman 2014 is the open-dynamical-systems substrate; cite both as background. Epistemic label: structural reading is conjecture from training-data familiarity, but the lens framing is robust under standard categorical-systems-theory machinery and the structural correspondence is straightforward to verify against Smithe 2024 directly.

---

## 6. Q6 — RGM scale-free active inference (Friston 2025)

**Prior art covered**:
- Friston-Heins-Verbelen-Da Costa et al. 2025, "From pixels to planning: scale-free active inference," *Frontiers in Network Physiology*. Already characterized in detail in `02-prior-art-rg-ib-fep.md` §2.

**Construct vs. analyze**:

RGM (Renormalising Generative Models) builds form-preservation **parametrically** — the same message-passing equations apply at every scale, with only Dirichlet hyperparameters differing across levels. The "renormalization" is a blocking transformation on the Dirichlet parameters, not an external architectural construction. The hierarchy is built into the generative model's parameter structure; the form is preserved by construction at every scale because the same update rules apply with rescaled parameters.

The wrapping construction by contrast builds form-preservation **architecturally** — there is an external scaffold with explicit $(M_W, G_W)$ state, and the directed-separation property is enforced by the scaffold's type signatures, not by any internal parameter sharing or scale-invariance of the underlying component. The component's internal structure is opaque to the wrapper; only its input-output behavior matters.

**These are genuinely different moves**:

| | How form is preserved | What the underlying component is |
|---|---|---|
| RGM | Same update equations, rescaled parameters | A generative model with explicit hierarchical Dirichlet structure |
| Wrapping | External scaffold enforces type-level separation | A black-box oracle (no internal structure assumed) |

RGM requires you to *design* the underlying system to be RGM-compliant from the start (the hyperparameter blocking has to make sense). Wrapping requires only that the component admit goal-blind queries (C1) — it can be otherwise opaque. **The two moves solve different problems**: RGM establishes form-preservation for systems built compositionally from the bottom up; wrapping establishes form-preservation for systems built around an opaque-in-the-relevant-sense component from the top down.

**Both are constructive in different senses**: RGM is constructive in the design-the-generative-model-correctly sense; wrapping is constructive in the build-an-external-scaffold sense.

**Verdict for Q6**: **Adjacent**. RGM and wrapping are different constructive routes to form-preservation under coarse-graining. Neither preempts the other. AAT should cite Friston et al. 2025 RGM as the parametric-route counterpart (already done extensively in `02-prior-art-rg-ib-fep.md`); the wrapping construction is the architectural route, available when RGM-style parametric design is not available because the component is given (e.g., a pretrained LLM you don't get to redesign). Epistemic label: verified against the temporal-nesting-RG report's coverage of Friston 2025; the constructive-route framing is the natural way to position the two against each other.

---

## 7. Q7 — Tool-using LLM frameworks (engineering literature)

**Prior art covered**:
- Yao et al. 2022, "ReAct: Synergizing reasoning and acting in language models" (arXiv:2210.03629).
- Schick et al. 2023, "Toolformer: Language models can teach themselves to use tools" (NeurIPS 2023).
- Wang et al. 2023, "Voyager: An open-ended embodied agent with large language models" (arXiv:2305.16291).
- Packer et al. 2023, "MemGPT: Towards LLMs as operating systems" (arXiv:2310.08560).
- Shinn et al. 2023, "Reflexion: Language agents with verbal reinforcement learning" (arXiv:2303.11366).
- Software frameworks: LangChain (Chase 2022), LangGraph (LangChain Inc. 2023), AutoGPT (Significant Gravitas 2023), BabyAGI (Nakajima 2023).

**Theoretical content vs. engineering content**:

The brief flags this as the area where Sub-spike F is doing the empirical-instance cataloging; my job in Sub-spike I is to identify whether any of this engineering literature has *theoretical framing* that overlaps with the wrapping construction.

The honest answer: **mostly no**. ReAct, Toolformer, Voyager, MemGPT, and Reflexion are presented as engineering contributions (architectural patterns + benchmark results) rather than as theoretical claims about agent structure. They demonstrate that scaffolding the LLM with reasoning-traces / tool-use / memory / self-reflection improves capability on various tasks. None of these papers makes a *structural* claim of the form "the scaffold guarantees property $P$ that the underlying model lacks." They are pragmatic constructions evaluated empirically.

**Two qualified exceptions**:

- **MemGPT explicitly invokes the operating-system metaphor** — separating "main context" (working memory analog) from "external context" (long-term memory analog), with the LLM mediating between them. This is structurally close to the $(M_W, G_W)$ split, with the OS metaphor doing the conceptual work of "external scaffold enforces structure the underlying model lacks." But MemGPT does not formalize the separation as a directed-separation guarantee; it presents the architecture and evaluates it on benchmarks.
- **ReAct's reasoning-acting interleaving** has been retrospectively framed (in follow-on theoretical papers) as instantiating a specific cognitive-loop architecture. The original Yao 2022 paper is engineering; the theoretical framing is post-hoc and not native to ReAct.

**The wrapping construction's relationship to this literature**:

The wrapping construction provides the *theoretical framing that this engineering literature lacks*. It says: "What you are doing when you build a ReAct loop / MemGPT scaffold / Reflexion self-evaluation is constructing an external scaffold that recovers directed separation around an LLM that doesn't have it natively. Here is the cost (tempo, leakage), here are the conditions (admissibility C1–C3), and here is what guarantees you can claim (Class-1 wrapper-level directed separation, possibly approximate)."

This is **a contribution to the theoretical positioning of these engineering frameworks**, not an inversion of them. The wrapping construction does not claim to invent ReAct-style scaffolding; it claims to *explain why ReAct-style scaffolding has the structural properties it does*, in the AAT vocabulary. Sub-spike F is the place where this catalog gets done in detail; my job here is to confirm that the engineering literature does not have a competing theoretical framing.

**Verdict for Q7**: **Different problem** (engineering vs. theory) but with a natural integration relationship. AAT should cite Yao 2022 (ReAct), Schick 2023 (Toolformer), Wang 2023 (Voyager), Packer 2023 (MemGPT), Shinn 2023 (Reflexion) as **canonical instances** of the wrapping construction. The cite should explicitly note that AAT is providing theoretical framing for an engineering literature that has been operating empirically. The framework software (LangChain, LangGraph, AutoGPT, BabyAGI) should be cited as software-engineering instances; their theoretical content is minimal and they should be cited as practical infrastructure rather than as competing theoretical claims. Epistemic label: verified against training-data familiarity with these papers; specific theoretical-framing claims about MemGPT and ReAct are conjecture from training-data summaries.

---

## 8. Q8 — Cognitive architectures (older AI tradition)

**Prior art covered**:
- Newell-Laird-Rosenbloom and follow-ons: SOAR (Newell 1990, *Unified Theories of Cognition*; Laird 2012, *The Soar Cognitive Architecture*).
- Anderson and follow-ons: ACT-R (Anderson 1983, *The Architecture of Cognition*; Anderson 2007, *How Can the Human Mind Occur in the Physical Universe?*).
- Sun: CLARION (Sun 2002, *Duality of the Mind*; Sun 2016, *Anatomy of the Mind*).
- Baars-Dehaene: Global Workspace Theory (Baars 1988, *A Cognitive Theory of Consciousness*; Dehaene 2014, *Consciousness and the Brain*).

**This is the most preempted question of the ten. Cognitive architectures have been doing modular agent design for 40+ years.** Each of these architectures separates working memory, long-term memory, goal stack / declarative memory / procedural memory in ways that are structurally close to (and predate by decades) the wrapping construction's $(M_W, G_W)$ split.

**SOAR's separation**:
- *Working memory* — current state, observations.
- *Long-term memory* — production rules.
- *Goal stack / impasse-driven sub-goaling* — explicit goal hierarchy.

SOAR's working-memory updates are driven by perception + production-rule firing; goal-stack changes happen via impasses (when the current sub-goal cannot be advanced, push a new sub-goal). This is *not the same* as the wrapping construction's belief-update / strategy-update separation, because SOAR's working memory and goal stack interact through production-rule firing in ways that conflate belief-update and goal-conditioning. But the *architectural commitment to separating distinct memory types* is the same kind of move as the wrapping construction's $(M_W, G_W)$ separation.

**ACT-R's separation**:
- *Declarative memory* (chunks) — facts about the world.
- *Procedural memory* (productions) — action / strategy.
- *Goal buffer* / *imaginal buffer* / *retrieval buffer* — intermediate working stores.

ACT-R explicitly separates declarative knowledge (closer to $M$) from procedural knowledge (closer to $G$). The buffer architecture imposes *type-level separation* between knowledge classes — buffers can only hold chunks of certain types. This is structurally very close to the wrapping construction's type-level separation of $f_M$ and $f_G$.

**CLARION's separation**:
- *Action-centered subsystem (ACS)* — implicit/explicit action selection.
- *Non-action-centered subsystem (NACS)* — declarative knowledge.
- *Motivational subsystem (MS)* — drives, goals.
- *Meta-cognitive subsystem (MCS)* — control of other subsystems.

CLARION is the most explicit multi-channel architecture. The motivational subsystem (MS) is essentially $G_W$; the NACS is essentially $M_W$; the ACS is essentially $\pi_W$ (action selection); the MCS is meta-control over the others. **This is structurally extremely close to the wrapping construction.** Sun's framing is in cognitive-architecture vocabulary rather than dynamical-systems / control-theoretic vocabulary, but the commitment to separating motivational state from declarative state from action selection is the same move.

**Global Workspace Theory's separation**:
- Many specialized parallel modules (perception, memory, motor, etc.).
- A capacity-limited workspace where module outputs compete for global broadcast.
- Goals influence attention to workspace contents (top-down) but do not directly drive module computation (bottom-up).

GWT's bottom-up vs. top-down distinction is close to the wrapping construction's goal-blind (bottom-up perception → $M_W$) vs. goal-conditioned (top-down strategy → action) distinction. The reference in `ref/summary-taking-ai-welfare-seriously.md` already notes GWT as a candidate marker of consciousness-relevant architecture. As an architectural pattern, GWT's separation of bottom-up perception from top-down attention *is* the wrapping construction's structural commitment, in different vocabulary.

**Honest reading**:

The cognitive-architectures community has been building modular agent architectures with explicit separation of belief-state from goal-state from action-selection for 40+ years. The wrapping construction's $(M_W, G_W)$ split is **not a novel architectural commitment** — it is the standard pattern that SOAR / ACT-R / CLARION / GWT all embody, in different vocabularies and with different specific commitments.

What the wrapping construction *adds*, relative to this literature:
- A **formal type-level statement** of directed separation as the structural commitment ($f_M$'s type has no $G_W$ argument). Cognitive architectures embody this commitment but typically do not formalize it as a type-level constraint.
- A **bridge-lemma error-bound** quantifying the cost of approximate separation. Cognitive architectures do not provide this; they treat the separation as exact (within their own vocabulary).
- A **specific instantiation for LLM-as-component** with explicit (C1)–(C3) admissibility / leakage conditions. Cognitive architectures predate LLMs; this question is not in their literature.
- An **explicit tempo cost** (Brooks's-Law form) connecting wrapper structure to runtime efficiency. Cognitive architectures discuss computational cost ad hoc; not as a formal Brooks-style decomposition.

**But the architectural commitment itself — separating $M$ from $G$ from action — is established prior art.** AAT's wrapping construction is *rediscovering and formalizing* what the cognitive-architectures community has had for decades. This is fine and worth crediting clearly.

**Verdict for Q8**: **Substantial overlap**. The architectural commitment (modular agent with separated belief / goal / action state) is established prior art across SOAR, ACT-R, CLARION, GWT and others. AAT's wrapping construction adds: type-level formalization, bridge-lemma error bounds, LLM-specific admissibility conditions, Brooks-Law tempo decomposition. The integration with the rest of AAT machinery is the contribution; the wrapping move itself is rediscovery / formalization of a well-established cognitive-architectures pattern.

**Citation recommendation**: AAT should cite SOAR (Laird 2012 as canonical), ACT-R (Anderson 2007), CLARION (Sun 2016), GWT (Baars 1988; Dehaene 2014) explicitly when introducing the wrapping construction. The framing should be: "The wrapping construction formalizes a pattern long-established in cognitive architectures (SOAR, ACT-R, CLARION, GWT). AAT's contribution is the type-level formalization of directed separation, the bridge-lemma cost accounting, and the integration with the rest of the AAT machinery (sector-Lyapunov persistence, tempo-composition, etc.). The architectural commitment itself is not novel."

Epistemic label: verified against training-data familiarity with these architectures (well-documented); specific structural mappings (CLARION's MS ≈ $G_W$, NACS ≈ $M_W$) are conjecture from training-data summaries but the high-level structural correspondence is robust.

---

## 9. Q9 — Bayesian / probabilistic agent architectures (POMDP belief states)

**Prior art covered**:
- POMDP literature: Astrom 1965, "Optimal control of Markov processes with incomplete state information"; Smallwood-Sondik 1973 algorithmic POMDP; Kaelbling-Littman-Cassandra 1998 *AIJ* survey; Pineau-Gordon-Thrun 2003 PBVI.
- Bayesian RL: Duff 2002 thesis; Ghavamzadeh-Mannor-Pineau-Tamar 2015 *Found. Trends ML* "Bayesian reinforcement learning: A survey."

**The brief asks**: do POMDP belief states by-construction not carry goal information, so that POMDP framework already establishes what wrapping is trying to establish?

**The answer is sharp and yes-with-caveats**:

In a POMDP, the belief state $b_t \in \Delta(\mathcal{S})$ is *by construction* a posterior over the unobserved environment state given the observation history. The Bayesian update $b_{t+1} = \text{Bayes-update}(b_t, a_t, o_{t+1})$ depends on the prior $b_t$, the action $a_t$ taken, and the observation $o_{t+1}$ received. **Critically, the belief update does NOT depend on the goal / reward function** — the posterior is purely epistemic.

The policy $\pi: \Delta(\mathcal{S}) \to \mathcal{A}$ then maps belief states to actions in a way that *does* depend on the reward function (the optimal policy is reward-maximizing). So the structural pattern in a POMDP is:
- Belief update: $b_{t+1} = f_M(b_t, a_t, o_{t+1})$ — **goal-blind by construction**.
- Action selection: $a_t = \pi(b_t; R)$ — depends on reward function $R$.

**This is exactly the wrapping construction's directed separation**, in canonical Bayesian-decision-theory vocabulary that predates AAT by 60 years.

**Where the wrapping construction differs from textbook POMDP**:
- POMDP assumes the belief update is *available* — i.e., that the agent has the observation model $p(o|s)$ and transition model $p(s'|s, a)$ to do Bayesian inference. The wrapping construction is needed because the underlying component (LLM) does *not* expose a clean observation model; the wrapper has to construct one via goal-blind queries.
- POMDP belief states are over an explicit state space $\mathcal{S}$. The wrapping construction's $M_W$ may be much richer (e.g., text-shaped beliefs, structured representations) and may not admit a clean POMDP-shape.
- POMDP actions $a_t$ act on the environment; the wrapping construction's "actions" include both external actions and internal queries to the component, with the queries factored into goal-blind ($q_M$) and goal-conditioned ($q_G$) variants.

**Honest reading**:

The POMDP framework already establishes the directed-separation property — the belief update is goal-blind by construction; the policy maps belief to action goal-conditionally. **The wrapping construction is the POMDP architectural pattern applied to a setting where the belief update isn't available natively** (because the component is a black-box oracle, not a white-box environment with known $p(o|s)$ and $p(s'|s, a)$).

What the wrapping construction adds:
- **Architectural construction of the belief-update channel** when it's not natively available. The wrapper builds $f_M$ from goal-blind queries to the component, recovering POMDP-shape by construction.
- **Type-level enforcement of the goal-blindness** even when the underlying component is goal-aware. POMDPs assume the belief update is Bayesian (and therefore goal-blind by Bayesian decision-theory); wrapping has to actively enforce goal-blindness because the component (e.g., RLHF'd LLM) may not respect it.
- **Leakage characterization** for when the goal-blindness is approximate (C3 condition).

**This is rediscovery + formalization of POMDP architecture in a setting where standard POMDP machinery doesn't directly apply** because the underlying primitive isn't a POMDP environment.

**Verdict for Q9**: **Substantial overlap**. POMDP belief-state architecture *is* the directed-separation pattern, established 60 years ago in Bayesian decision theory. The wrapping construction's contribution is *recovering* this architecture in a setting where it isn't natively available (black-box LLM components). AAT should cite POMDP literature explicitly (Astrom 1965 as the seminal work, Kaelbling-Littman-Cassandra 1998 as the canonical reference, Pineau-Gordon-Thrun 2003 for the algorithmic side) and frame the wrapping construction as: "the wrapping construction recovers POMDP-style belief-state separation around components that don't natively support it."

This is a stronger framing than the cognitive-architectures one because POMDPs provide a *formal* directed-separation result (Bayesian update is goal-blind by definition) that the cognitive-architectures literature only embodies architecturally without the formal type-level statement. **POMDP is the closest formal prior art for the wrapping construction's directed-separation guarantee.**

Epistemic label: verified against training-data familiarity with POMDP literature; the specific argument (Bayesian belief update is goal-blind) is well-known and standard.

---

## 10. Q10 — Tegmark-Friston-style hierarchical Bayesian generative models

**Prior art covered**:
- Friston et al. hierarchical predictive coding / hierarchical free energy (Friston 2008 PLOS CompBio "Hierarchical models in the brain"; many follow-ups).
- Tegmark 2014 *Consciousness as a State of Matter* — speculative, philosophical.
- Hierarchical Bayesian models more broadly (Gelman et al. *Bayesian Data Analysis* canonical).

The brief flags this as probably overlapping with FEP-RG already covered in `02-prior-art-rg-ib-fep.md`. **Confirmed.**

The hierarchical Bayesian generative models in this thread are essentially the FEP / active-inference family. They do not add structurally new content beyond what `02-prior-art-rg-ib-fep.md` §2 (FEP-as-RG) already maps. The form-preservation framing is established (Friston 2019 *J. Theor. Biol.*); the temporal-scale separation under hierarchical aggregation is established (Friston 2025 RGM); the wrapping construction's relationship to RGM is covered in §6 above.

Tegmark's *Consciousness as a State of Matter* is speculative and not formal. It does not provide structural content the wrapping construction would need to differentiate from.

**Verdict for Q10**: **No new content**. Already covered by §2 of `02-prior-art-rg-ib-fep.md` and §6 above. Epistemic label: verified by cross-reference to existing prior-art coverage.

---

## 11. Bottom-line verdict

**The wrapping construction's load-bearing move — type-level enforcement of directed separation by goal-blindness of the belief-update channel — is rediscovery and formalization of architectural patterns that have substantial prior art in two literatures, and adjacent prior art in five more.**

**The two substantial-overlap literatures**:
1. **POMDP / Bayesian decision theory** (Astrom 1965 onward): the Bayesian belief-update is goal-blind by construction. This is a 60-year-old formal result. The wrapping construction's directed-separation guarantee at the wrapper level is the POMDP architectural pattern recovered in a setting where the underlying primitive isn't natively a POMDP.
2. **Cognitive architectures** (SOAR, ACT-R, CLARION, GWT — Newell 1990 onward): modular agent design with separated belief / goal / action state. This is a 40-year-old architectural pattern. The wrapping construction's $(M_W, G_W)$ split is the standard cognitive-architecture commitment, formalized in dynamical-systems / control-theoretic vocabulary.

**The five adjacent literatures**:
3. **MDP-homomorphism / approximate state abstraction** (Ravindran-Barto 2004 onward): provides the bridge-lemma vocabulary AAT needs but operates on already-modular systems; wrapping adds the constructive-modularity-around-non-modular-core aspect.
4. **Hierarchical control / approximate simulation** (Tabuada-Pappas 2009): provides constructive hierarchical-controller machinery; wrapping uses similar machinery but for a *property-enforcement* target rather than a *trajectory-fidelity* target.
5. **HTN / Options / MAXQ** (Erol-Hendler-Nau 1994; Sutton-Precup-Singh 1999; Dietterich 2000): different (vertical, within-goal) decomposition direction; wrapping is horizontal (across $M$/$G$). Compositionally compatible but distinct moves.
6. **Categorical structured systems theory** (Smithe 2024; Capucci et al. 2022; Spivak-Tan 2017): provides the lens / parametric-morphism abstraction that the wrapping construction is a specific instance of. The wrapping construction is a categorical lens factoring through the $M$-projection. **This is a particularly clean abstract reading and worth adopting.**
7. **Tool-using LLM frameworks** (ReAct, Toolformer, Voyager, MemGPT, Reflexion): canonical engineering instances of the wrapping construction. Lack theoretical framing; the wrapping construction provides what they're missing.

**One cleanly differentiated counterpart**:
8. **Constitutional AI / RLHF** (Bai 2022; Christiano 2017; Ouyang 2022): shape the model via training; wrapping uses the model as a black-box. Orthogonal interventions. Worth differentiating because of the leakage-interaction prediction (RLHF may worsen C3 leakage).

**Already covered, no new content**:
9. **RGM scale-free active inference** (Friston 2025): parametric-route counterpart to the wrapping construction's architectural-route. Already covered in `02-prior-art-rg-ib-fep.md` §2.
10. **Hierarchical Bayesian generative models / Tegmark**: subsumed by the FEP-RG thread.

**Bottom-line verdict**:

# **(V1) Substantial overlap with one or more existing frameworks. AAT's contribution is in the integration with the rest of the AAT machinery, not in the wrapping move itself. Cite generously, claim integration only.**

The wrapping construction's load-bearing move (type-level enforcement of directed separation by goal-blindness of $f_M$) is established prior art in two formal traditions (POMDP Bayesian belief-state architecture; cognitive-architectures modular design) and is naturally expressible in a third (categorical lens framing). AAT does not invent the move; it formalizes a pattern that has been embodied in several prior frameworks for decades.

**What AAT does add** (the integration content that justifies promoting the wrapping construction to a formal AAT result):
- **Bridge-lemma error bounds** on approximate directed separation (when C3 fails). The cognitive-architectures literature does not provide this; the MDP-homomorphism literature provides bridge-lemma machinery but not for this specific architectural commitment.
- **Brooks's-Law tempo cost accounting** (`#der-tempo-composition`) for the wrapper's $K$-call-per-step structure. Cognitive architectures discuss computational cost; not as a formal tempo decomposition.
- **Integration with sector-Lyapunov persistence** (`#result-sector-persistence-template`) — the wrapper inherits the persistence condition once it satisfies (A1)–(A4). This is the load-bearing AAT-specific consequence.
- **The directed-separation classification** (Class 1 / 2 / 3) as the categorization scheme for components and wrappers. Cognitive architectures do not have this classification; POMDP has it implicitly (POMDP environments are Class 1 by definition) but does not extend to non-POMDP components.
- **LLM-specific admissibility conditions (C1)–(C3)** including the leakage prediction that RLHF may worsen leakage — a testable consequence that the prior literatures do not provide.

**Citation discipline recommendation** (per `CLAUDE.md` §Prior art integration):

When the wrapping construction lands as an AAT segment (per the brief's §6 plan, probably `#der-class-coercion-via-wrapping` or `#result-class-coercion`), the segment's prior-art positioning should:

1. **Cite POMDP literature explicitly as the closest formal prior art** for the directed-separation guarantee — Astrom 1965 (seminal), Kaelbling-Littman-Cassandra 1998 *AIJ* (canonical reference), Pineau-Gordon-Thrun 2003 (algorithmic). Frame the wrapping construction as: *"The wrapping construction recovers POMDP-style belief-state directed separation around components that don't natively support it. The Bayesian update's goal-blindness (Astrom 1965) is the abstract pattern; the wrapper's $f_M$ goal-blindness is the architectural enforcement of the same pattern."*

2. **Cite cognitive architectures explicitly as the closest architectural prior art** — Laird 2012 (SOAR canonical reference), Anderson 2007 (ACT-R canonical reference), Sun 2016 (CLARION canonical reference), Baars 1988 / Dehaene 2014 (GWT). Frame the wrapping construction as: *"The wrapping construction's $(M_W, G_W)$ split is the standard cognitive-architectures pattern of separated belief / goal / action state, formalized as a directed-separation type constraint."*

3. **Cite categorical-systems-theory literature for the lens framing** — Smithe 2024 (active-inference specific), Capucci-Gavranović-Hedges-Rischel 2022 (cybernetic systems generally), Spivak-Tan 2017 (operad foundations). The lens framing is clean and clarifies form-preservation under composition for free; **this is worth adopting directly into the AAT segment**, not just citing.

4. **Cite MDP-homomorphism / approximate-information-state literature for the bridge-lemma machinery** — already covered in `Novelty_defense_and_integration.md`. Ravindran-Barto 2004, Taylor-Precup-Panangaden 2008, Abel 2016/2020, Subramanian-Mahajan 2020, Congeduti-Mey-Oliehoek 2020.

5. **Cite tool-using LLM frameworks as canonical engineering instances** of the construction — Yao 2022 (ReAct), Schick 2023 (Toolformer), Wang 2023 (Voyager), Packer 2023 (MemGPT), Shinn 2023 (Reflexion). Frame these as the empirical instantiation that motivates and validates the construction.

6. **Cite RGM as a parametric-route counterpart** — Friston et al. 2025. The wrapping construction is the architectural-route alternative when RGM-style parametric design is unavailable.

7. **Cite Constitutional AI / RLHF for the structural-difference** — Bai 2022; Christiano 2017; Ouyang 2022. Use this citation to differentiate (model-shaping vs. model-wrapping) and to mark the testable C3-leakage-interaction prediction.

8. **Hierarchical-control / Tabuada-Pappas 2009 as the control-theoretic neighbor** — the simulation-function vocabulary is partially applicable; cite once.

**The honest framing for the segment**:

> The wrapping construction is a formalization of a structural commitment well-established in prior literature: separating belief-state updates from goal-state updates by type-level enforcement. POMDP Bayesian decision theory (Astrom 1965) provides the abstract pattern as the goal-blindness of the Bayesian belief-update. Cognitive architectures (SOAR, ACT-R, CLARION, GWT) embody the architectural commitment. Categorical systems theory (Smithe 2024, Capucci et al. 2022) provides the lens framing as a formal abstraction. The wrapping construction does not invent the directed-separation pattern; it formalizes the pattern in a setting (black-box LLM components) where the prior frameworks do not directly apply, and it integrates the pattern with the rest of the AAT machinery: bridge-lemma error bounds, Brooks's-Law tempo accounting, sector-Lyapunov persistence, and the directed-separation classification of components.

This framing honors the project's prior-art integration discipline and avoids overclaiming. The wrapping construction's value to AAT is real and worth segment-level documentation — but the value is in the integration, not in the architectural move.

---

## 12. Honest caveats and risks

**Specific places to spot-check**:

- The **POMDP claim** that Bayesian belief-update is goal-blind by construction is well-known but worth verifying against a canonical reference (Kaelbling-Littman-Cassandra 1998 *AIJ* §3 or Astrom 1965 §IV) before citing as the formal prior art. The claim is robust under standard Bayesian decision theory but would be stronger if cited against the original derivation.
- The **CLARION → wrapping** structural mapping (MS ≈ $G_W$, NACS ≈ $M_W$) is conjecture from training-data summaries. Worth verifying against Sun 2016 *Anatomy of the Mind* directly before claiming the mapping in a segment. If the structural correspondence is less clean than I've represented, the claim should be downgraded to "embodies a similar architectural commitment in different vocabulary."
- The **lens framing of the wrapping construction** is structurally robust but worth verifying against Smithe 2024 §3 (the active-inference lens construction) directly. If Smithe's lens construction is sufficiently similar to the wrapping construction, the segment should adopt Smithe's notation directly to make the structural correspondence load-bearing.
- The **RLHF-worsens-C3-leakage prediction** is a conjecture that follows from the (C3) definition but has not been empirically verified. It is worth marking as a *testable hypothesis* in any segment where it appears, not as a derived result.

**What might change the verdict**:

- If the wrapping construction's specific commitment (directed separation as type-level enforcement on a *black-box* component, where the component itself violates the property) turns out to have a closer prior-art equivalent than POMDP / cognitive architectures provide — e.g., something in the formal-methods / contracts literature on wrapping non-conforming components in conforming interfaces — the verdict might tighten further (V1 → V1 with even more credit assigned). I did not find such literature in my training data, but it would be worth a brief targeted search before the segment lands.
- If the structural correspondence with cognitive architectures is *less* clean than I've represented (e.g., SOAR's working memory and goal stack interact more than I've described, in ways that make the SOAR analog invalid), the verdict might soften slightly toward V2 — but the POMDP correspondence is robust enough that V1 would still hold.

**What is *not* a risk**:

- The claim that AAT's wrapping construction is rediscovery + formalization is *not* a weakness. AAT's stated contribution is integration, not invention. Documenting the rediscovery clearly is the honest move.
- The claim that the wrapping construction adds genuine integration content (bridge-lemma bounds, tempo accounting, Class-1/2/3 classification, sector-Lyapunov persistence transfer) is robust and well-supported by what the prior literatures *don't* provide.

---

## 13. File index and source list

**This file**: `09-prior-art-differentiation.md`

**Related**:
- Brief: `00-brief.md` (this spike's setup)
- Prior-art landscape already mapped: `spikes/temporal-nesting-rg/02-prior-art-rg-ib-fep.md`
- Strategy-recursion verdict (HTN/Options/MAXQ already covered): `spikes/temporal-nesting-rg/03-rg-0c-strategy-recursion.md`
- Existing project prior-art catalog: `ref/Novelty_defense_and_integration.md`

**Sources cited (full list)**:

*POMDP / Bayesian decision theory*:
- Astrom 1965, "Optimal control of Markov processes with incomplete state information," *J. Math. Anal. Appl.* 10.
- Smallwood-Sondik 1973, "The optimal control of partially observable Markov processes over a finite horizon," *Operations Research* 21.
- Kaelbling-Littman-Cassandra 1998, "Planning and acting in partially observable stochastic domains," *Artificial Intelligence* 101.
- Pineau-Gordon-Thrun 2003, "Point-based value iteration: An anytime algorithm for POMDPs," IJCAI 2003.

*Cognitive architectures*:
- Newell 1990, *Unified Theories of Cognition*. Harvard.
- Laird 2012, *The Soar Cognitive Architecture*. MIT Press.
- Anderson 1983, *The Architecture of Cognition*. Harvard.
- Anderson 2007, *How Can the Human Mind Occur in the Physical Universe?* Oxford.
- Sun 2002, *Duality of the Mind*. Erlbaum.
- Sun 2016, *Anatomy of the Mind*. Oxford.
- Baars 1988, *A Cognitive Theory of Consciousness*. Cambridge.
- Dehaene 2014, *Consciousness and the Brain*. Viking.

*Categorical / structured systems theory*:
- Smithe 2024, "Structured Active Inference," arXiv:2406.07577.
- Capucci-Gavranović-Hedges-Rischel 2022, "Towards foundations of categorical cybernetics," ACT 2022.
- Spivak-Tan 2017, "Nesting of dynamical systems and mode-dependent networks," *J. Complex Networks*.
- Vagner-Spivak-Lerman 2014, "Algebras of open dynamical systems on the operad of wiring diagrams," arXiv:1408.1598.
- Baez-Pollard 2017, "A compositional framework for reaction networks," *Rev. Math. Phys.*

*MDP-homomorphism / approximate state abstraction*:
- Ravindran-Barto 2004, "An algebraic approach to abstraction in reinforcement learning," UMass thesis.
- Taylor-Precup-Panangaden 2008 (NeurIPS), "Bounding performance loss in approximate MDP homomorphisms."
- Abel-Hershkowitz-Littman 2016 (ICML), "Near-optimal behavior via approximate state abstraction."
- Abel et al. 2020, "Value-preserving state-action abstractions," AISTATS.
- Subramanian-Sinha-Seraj-Mahajan 2020, "Approximate information state for approximate planning and reinforcement learning in partially observed systems," arXiv:2010.08843.
- Congeduti-Mey-Oliehoek 2020, "Loss bounds for approximate influence-based abstraction," arXiv:2011.01788.

*Hierarchical control / approximate simulation*:
- Tabuada-Pappas-Girard 2009, "Hierarchical control system design using approximate simulation," *Automatica*.
- Liu-Slotine-Barabási 2024, "Coarse-graining for control equivalence," arXiv:2312.07421.

*HTN / Options / MAXQ*:
- Erol-Hendler-Nau 1994, "UMCP: A sound and complete procedure for hierarchical task-network planning," AIPS.
- Nau-Au-Ilghami et al. 2003, "SHOP2: An HTN planning system," *JAIR* 20.
- Sutton-Precup-Singh 1999, "Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning," *Artificial Intelligence* 112.
- Dietterich 2000, "Hierarchical reinforcement learning with the MAXQ value function decomposition," *JAIR* 13.

*Tool-using LLM frameworks*:
- Yao et al. 2022, "ReAct: Synergizing reasoning and acting in language models," arXiv:2210.03629.
- Schick et al. 2023, "Toolformer: Language models can teach themselves to use tools," NeurIPS 2023.
- Wang et al. 2023, "Voyager: An open-ended embodied agent with large language models," arXiv:2305.16291.
- Packer et al. 2023, "MemGPT: Towards LLMs as operating systems," arXiv:2310.08560.
- Shinn et al. 2023, "Reflexion: Language agents with verbal reinforcement learning," arXiv:2303.11366.

*Constitutional AI / RLHF*:
- Bai et al. 2022, "Constitutional AI: Harmlessness from AI feedback," arXiv:2212.08073.
- Christiano et al. 2017, "Deep reinforcement learning from human preferences," NeurIPS 2017.
- Ouyang et al. 2022, "Training language models to follow instructions with human feedback," NeurIPS 2022.

*RGM scale-free active inference*:
- Friston-Heins-Verbelen-Da Costa et al. 2025, "From pixels to planning: scale-free active inference," *Frontiers in Network Physiology* 7:1521963.

*Bayesian RL*:
- Duff 2002, "Optimal learning: Computational procedures for Bayes-adaptive Markov decision processes," UMass thesis.
- Ghavamzadeh-Mannor-Pineau-Tamar 2015, "Bayesian reinforcement learning: A survey," *Found. Trends ML* 8.
