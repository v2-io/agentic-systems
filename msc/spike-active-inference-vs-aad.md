# Spike: AAD ↔ Active Inference — Positioning, Mapping, and Tier-Strength Analysis on G-BP2

**Status**: Scoping spike. No segments modified. The document answers two coupled questions: the strategic positioning question ("why AAD when Active Inference exists?") and the tactical question on architectural proposal G-BP2 (whether AAD's strategy/objective machinery should be reframed as variational free-energy minimization).

**Date**: 2026-04-22.

**Depends on**: `01-aad-core/OUTLINE.md`; the AAD core segments listed in §B; `msc/architectural-proposals-2026-04-22.md` (G-BP1, G-BP2, G-BP3, O-BP2); `msc/spike-ib-unification-plan.md` (the precedent the tier-strength analysis parallels); `msc/02-prior-art-assessment.md` (prior thin engagement with active inference, pre-AAD).

**Deliverable**: positioning argument plus per-claim mapping plus tier-strength recommendation on G-BP2, all comparable in shape to the IB-unification spike so Joseph can hold the two scoping decisions side by side.

**Reframing of the original question (executed up front).** The user-facing prompt asks "Why do we need AAD when we already have Active Inference?" The honest answer requires reframing the question rather than executing it as posed: there is no single "Active Inference," and AAD's relationship to each variant differs. The body distinguishes (a) **Strong FEP** — the metaphysical claim that all self-organizing systems minimize variational free energy and that Markov blankets demarcate agent-from-environment ontologically (Friston 2010; critiqued by Bruineberg et al. 2022, Aguilera et al. 2022, Colombo & Wright 2018); (b) **Weak active-inference machinery** — the modeling toolkit (variational posteriors, generative models, expected free energy as policy objective) used without the metaphysical claims (Friston et al. 2017; Da Costa et al. 2020; Sajid et al. 2021); (c) **Hierarchical predictive coding** — the neuroscience-flavored cousin (Clark, Hohwy, Rao & Ballard); (d) **Sophisticated / bounded-rational active inference** — explicit treatment of computation cost via recursive EFE (Friston, Da Costa, Hafner, Hesp & Parr 2021); (e) **Discrete-state active inference** (Da Costa et al. 2020; A/B/C/D matrices) versus **continuous-state active inference** (classical Friston, Karl-style continuous formulations). AAD's relationship to each is mapped separately in §B–§D. Treating "AI" as a single thing is the failure mode the IB-unification spike avoided by distinguishing U-strong / U-medium / U-weak; the same posture applies here.

---

## §A — Reviewer-Facing One-Page Summary

AAD and Active Inference (AI) overlap substantially in the *machinery they make available*: both use Bayesian agents, both formalize action-perception loops, both connect epistemic and instrumental drives, and both can be cast as compression problems. They diverge in *what is foundational*, *what is derived*, *what is presented as a constraint vs. a free choice*, and *what scope is claimed*.

**The four load-bearing differences, stated for a reviewer.**

1. **Foundational stance.** AI begins from a single optimization principle — minimize variational free energy / maximize Bayesian model evidence — and recovers perception, action, and learning as cases. AAD begins from operational requirements on a feedback-coupled adaptive system (the persistence template, causal access via the loop, directed separation as architectural classification) and uses information-theoretic compression (IB) as one of several modeling moves rather than as the master objective. Where AI says "everything is one thing" (FEP) AAD says "several distinct things compose under a shared persistence template." The IB-unification spike recently affirmed *U-medium*, not *U-strong*, for AAD's own internal compression operations precisely to avoid the unification-by-fiat failure mode that Litwin & Miłkowski (2020) attribute to predictive processing.

2. **Treatment of preferences and objectives.** AI typically encodes preferences as a *prior over outcomes* $C(o) = \log P(o)$, making "what the agent wants" formally indistinguishable from "what the agent expects" (the dark-room problem of Sun & Firestone 2020 is the diagnostic; the EFE epistemic-pragmatic split is the standard repair). AAD insists on a **definitional split** $G_t = (O_t, \Sigma_t)$ with $O_t$ as a *value functional on trajectories* (real-valued by scope, see #objective-functional) and $\Sigma_t$ as a *probabilistic causal DAG* (#strategy-dag). The split exposes the **satisfaction-gap / control-regret diagnostic** (#satisfaction-gap, #control-regret) — a 2×2 cell map distinguishing "goal too hard" from "strategy too weak" — and the **convention hierarchy** C1/C2/C3 over continuation policies (#value-object). These are diagnostics AI does not produce for free.

3. **Scope honesty about architecture.** AAD classifies agents into Class 1 (modular), Class 2 (fully merged, e.g. transformer LLMs), Class 3 (partially modular) via the directed-separation structure (#directed-separation) — and admits that Section II's exact results apply only to Class 1. Class 2 agents need a coupled formulation; that is what `03-logogenic-agents/` is for. AI's Markov-blanket apparatus is widely *interpreted* as architecture-blind ("any self-organizing system has a Markov blanket"), but the Bruineberg et al. (2022) Pearl-vs-Friston critique shows that the metaphysical use overruns what the formalism delivers. AAD does not claim architecture-blindness it cannot deliver; it states the scope and provides escape hatches.

4. **Causal and compositional content beyond Bayesian inference.** AAD makes Pearl-Level-2 (interventional) and Level-3 (counterfactual) access part of the load-bearing structure: the feedback loop *generates* interventional data by construction (#loop-interventional-access); the strategy DAG is regime-indexed for the strength of its causal interpretation (A/B/C in #edge-update-causal-validity); the correlation hierarchy (L0/L1/L2 in #strategy-dag) treats correlated failure as first-class rather than as a tractable limit. AI is generally Level-1 (associational) — the generative models in standard active inference are joint distributions, not causal graphs in Pearl's sense — and there is no native compositional persistence theorem comparable to AAD's sector-Lyapunov template applied to closure defects (#composition-closure, #sector-persistence-template).

**The honest reduction (one sentence).** AAD is a *control-theoretic / causal-inference* synthesis with a Bayesian-compression component, presented as a portfolio of distinct results held together by a persistence template and a directed-separation scope; Active Inference is a *Bayesian-compression* synthesis with control-theoretic and causal components, presented as one master optimization principle with broad metaphysical reach. They are competitors *only if* one interprets "we already have AI" as "we already have a unified theory of adaptive purposeful agency" — a claim the AI literature itself contests (Andrews 2021, Gershman 2019, Litwin & Miłkowski 2020).

**The recommended framing for paper introductions.** "AAD and Active Inference share substantial machinery; we credit and cite the overlap (Friston 2010, Friston et al. 2017, Parr & Pezzulo 2022). Where AAD differs deliberately — in foundational stance, in the objective-strategy split with diagnostics, in architectural scope honesty, and in the causal-and-compositional content — we state the difference and the reason. Where AAD borrows the variational machinery without the metaphysical commitments (sophisticated inference's bounded-rationality form, the EFE epistemic split), we say so."

---

## §B — AAD ↔ Active Inference Concept Mapping

Each row maps an AAD object to its closest AI counterpart and classifies the fit as **clean** (the same object up to notation), **partial** (related but with substantive differences), **divergent** (related framing, opposite stance), or **no-fit** (no canonical AI counterpart). When fit varies by AI variant, the cell names the variant. Citations to AAD segments use `#slug`. Citations to AI use author-year.

| AAD object | Closest AI counterpart | Fit | Brief justification |
|---|---|---|---|
| $M_t$ ( #agent-model) — compressed model state | Variational posterior $Q(s)$ over hidden states (Friston 2017; Da Costa 2020) | **Clean (machinery), partial (interpretation)** | Both are compressed beliefs under uncertainty. AAD makes $M_t$ the substrate of mismatch dynamics; AI makes $Q$ the result of free-energy minimization. The objects play the same role; the surrounding theory differs. |
| $\mathcal C_t$ — chronica (interaction history) | The data $o_{1:t}$ on which the posterior is conditioned | **Clean** | Standard. Both store the agent's history of observations and actions. |
| $\Omega_t$ — environment state (unobservable totality) | Hidden states $s$ in the generative model | **Partial** | AAD is agnostic about $\Omega$'s structure; AI commits the generative model to a specific factorization (A, B, C, D matrices in discrete-state form). |
| $\delta_t$ — mismatch signal (#mismatch-signal) | Prediction error in predictive coding (Rao & Ballard 1999; Friston 2010) | **Clean (qualitative), partial (form)** | Same object: predicted minus observed. AAD analyzes its dynamics via the sector-Lyapunov template; predictive coding interprets it as the message passed up the hierarchy. |
| $\eta^\ast$ — optimal update gain (#update-gain) | Precision (inverse variance) on prediction errors in PC; learning rate in variational schemes | **Clean** | Both encode "how much to weight new evidence." AAD's gain principle is dimensionally explicit; AI's precision is the standard Bayesian operation. |
| $\mathcal{T}$ — adaptive tempo (#adaptive-tempo) | Effective update rate (no canonical AI term); precision-weighted update frequency | **Partial** | AAD makes tempo a first-class scalar (rate of useful information acquisition). AI does not name tempo as a primary object — it is implicit in the rate of variational message passing. |
| Sector condition (#sector-condition-stability) | No clean counterpart | **No-fit** | AAD's Lyapunov-based persistence is control-theoretic; AI's stability arguments come from the mathematics of variational optimization (and have been challenged by Aguilera et al. 2022 for narrow validity). |
| Persistence template (#sector-persistence-template) | No clean counterpart | **No-fit** | This is one of AAD's strongest distinctive claims — see §C below. |
| $G_t = (O_t, \Sigma_t)$ — purposeful substate split (#strategy-dimension) | $C$ (preferences) plus $\pi$ (policy posterior) in active inference | **Divergent** | Both factor "what I want" from "what I do." AAD makes objectives *value functionals* and strategy a *causal DAG*. AI makes preferences *log priors over outcomes* and policy a *softmax over -EFE*. The categorical structure differs; see §C and §D for why this matters. |
| $O_t$ — objective as value functional (#objective-functional) | $C(o) = \log P_{\text{pref}}(o)$ — preferences as priors over observations (Friston 2017 §2.3; Sajid et al. 2021) | **Divergent** | AAD treats $O_t$ as a real-valued evaluator over trajectories and explicitly defends scalarizability. AI conflates "want $o$" with "expect $o$" via the prior. The dark-room problem (Sun & Firestone 2020) is the diagnostic. |
| $\Sigma_t$ — strategy DAG (#strategy-dag) | $\pi$ as a softmax over policies $\pi_i$ ranked by expected free energy | **Divergent** | AAD: strategy is causally structured (DAG with AND/OR, regime-indexed edges, correlation hierarchy). AI: policies are typically enumerated sequences of actions over a horizon, scored by EFE. Different representational commitments. |
| Satisfaction gap $\delta_{\text{sat}}$ (#satisfaction-gap) | No clean counterpart in standard AI; partially implicit in EFE pragmatic-value comparisons | **Partial / no-fit** | AAD: $V_{O_t}^{\min} - A_O$ — explicit "is the goal feasible from here?" diagnostic. AI in standard form does not separate "goal-too-hard" from "policy-too-weak"; both increase EFE. |
| Control regret $\delta_{\text{regret}}$ (#control-regret) | Bayesian regret (decision theory); related to softmax-policy slack in AI | **Partial** | AAD: $A_O - V_O(\pi_{\text{current}})$. The 2×2 with $\delta_{\text{sat}}$ produces a diagnostic table that standard AI does not. |
| Convention hierarchy C1/C2/C3 (#value-object) | One-step lookahead / receding horizon / Bellman-optimal — universal across decision theory and RL | **Clean** | These are not AAD-specific conventions; they are the standard horizon choices. AAD's contribution is the monotonicity proof and the diagnostic implications across the three. |
| Orient cascade (#orient-cascade) | Variational message passing schedule; precision-weighted prediction-error propagation | **Partial** | Both order updates by information dependency. AAD: derived sequential ordering ($M$ → $\Sigma$ → $O$). AI: simultaneous updates within the variational scheme; the "order" is the message-passing order, not a logical dependency. |
| Exploit / explore / deliberate (#exploit-explore-deliberate) | Pragmatic value (exploit) + epistemic value (explore) in EFE; deliberation as recursive EFE in sophisticated inference | **Partial** | The two-axis exploit/explore corresponds to the EFE decomposition. Deliberation as a third axis is *not* standard in classical AI; "sophisticated inference" (Friston, Da Costa et al. 2021) approximates it via recursive EFE. AAD's "deliberation as internal exploration in model-space" is a third factor classical AI doesn't lift cleanly. |
| Directed separation (#directed-separation) | Markov blanket (Friston 2013, 2019; canonical FEP construct) | **Divergent** | This is the most-asked comparison. AAD: an *architectural classification* (Class 1/2/3) about whether $f_M$ depends on $G_t$ in the agent's processing graph, with empirical operationalization $\kappa_{\text{processing}}$. AI: a *statistical conditional independence* meant to demarcate self-from-other. The Bruineberg et al. (2022) Pearl-vs-Friston critique shows the AI version overruns its formalism; AAD's version stays within it. See §C. |
| Class 1 / Class 2 / Class 3 architecture | Modular generative model vs. monolithic generative model — discussed informally; no canonical AI partition | **Partial / no-fit** | AAD names the partition explicitly and assigns scope by class; AI literature treats architecture as a modeling choice without the scope-restriction discipline. |
| Composition closure (#composition-closure) | No canonical AI counterpart; loosely related to hierarchical generative models with multiple levels | **Partial / divergent** | AAD: a *measurable closure defect* $\varepsilon^\ast$ between micro and macro dynamics, with admissibility constraints (P1)–(P3) and a sector-Lyapunov bridge lemma. AI: hierarchical generative models layer abstractions but do not compute a closure-defect bound; the macro level is an *additional generative-model layer*, not a coarse-grained dynamical homomorphism. |
| Composition consistency (#postulate-composition-consistency) | Multi-scale renormalization in physics-flavored FEP work (Friston 2019); approximate | **Partial** | Both want scale-invariant results. AAD requires scope-condition level-independence; AI's multi-scale work is informal and contested (Aguilera et al. 2022). |
| Regime-indexed edges A/B/C (#edge-update-causal-validity) | No canonical counterpart | **No-fit** | AI works at Pearl Level 1 (associational); regime A (interventional), B (partial intervention), C (observational) is a Level-1/Level-2 distinction AI does not natively make at the modeling level. |
| Correlation hierarchy L0/L1/L1'/L2 (#strategy-dag) | No canonical counterpart | **No-fit** | AI handles correlated outcomes through joint generative models; it does not partition them into a hierarchy with explicit augmentation procedures (L1 common-cause nodes; L1' mixture form). |
| Causal hierarchy requirement (#causal-hierarchy-requirement) | Partial — AI uses Bayes nets (Level 1); does not commit to Pearl Level 2 as load-bearing | **Divergent** | AAD insists Level 2 is required to evaluate $Q_O$; AI tools like EFE typically use Level 1 generative models as their causal substrate, with the agent's policy treated as the intervention but the world model treated associationally. |
| Loop interventional access (#loop-interventional-access) | Implicit — the action-perception loop in AI also generates intervention-produced data, but AI literature does not state this as a load-bearing theorem | **Partial** | The substantive content overlaps; the framing differs. AAD makes "loop is a Level-2 engine" explicit; AI absorbs this implicitly. |
| Causal information yield (#causal-information-yield) | Epistemic value in EFE (expected information gain about hidden states) | **Clean (idea), partial (form)** | Both formalize "how much does this action teach me?" AAD: KL between interventional outcome distributions across actions. AI: expected mutual information between hidden states and future outcomes under a candidate policy. The conceptual move is the same; the formal object differs (AAD is action-distinguishability under do; AI is state-information under softmax-weighted policy). |
| Strategy complexity cost / max useful depth $d^\ast$ (#strategy-complexity-cost) | KL-control complexity penalty (Todorov, Kappen); resource-rational analyses (Lieder & Griffiths 2020); sophisticated inference's recursion-depth limits | **Partial / clean (machinery)** | AAD: cognitive cost of $\Sigma_t$ via DL/IB and a per-edge persistence-derived depth bound. AI counterpart exists in KL-control and bounded-rational variants; the classical Friston EFE does not have this as a primary axis. |
| Information bottleneck on $M_t$ (#information-bottleneck) | Variational free-energy minimization (in the $-F = $ accuracy $-$ complexity decomposition) | **Clean** | Both are rate-distortion / IB-type objectives. Tishby's IB and Friston's $F = \text{accuracy} - \text{complexity}$ are cousins; the IB-unification spike (`spike-ib-unification-plan.md`) treats them under the same shape (U-medium). |
| Compression-operations synthesis (#compression-operations) | Hierarchical generative models with multiple compression layers | **Partial** | AAD names four compression instances explicitly with a $(X, T, Y, \beta)$ binding table. AI handles all of them implicitly through nested generative models and EFE. |
| Sector-Lyapunov template (#sector-persistence-template) | No canonical AI counterpart | **No-fit** | AI's stability claims come from variational geometry (and are contested for narrow validity, Aguilera 2022). AAD's persistence-by-sector-condition is a control-theoretic export from the TFT lineage that AI does not have a clean analog for. |
| Agent identity (#scope-agent-identity) | Markov blanket as identity / "particular partition" in Friston 2019 | **Divergent** | AAD: identity grounded in singular causal trajectory $\mathcal C_t$, not in $M_t$. AI: identity collocated with the Markov blanket / particular partition. The Bruineberg critique applies. |
| Adversarial dynamics (#adversarial-tempo-advantage et al.) | No native AI counterpart | **No-fit** | Adversarial / multi-agent persistence is a specifically AAD development (TFT lineage). AI has work on multi-agent active inference (Heins et al., Maisto et al.), but the adversarial-tempo-advantage exponents (#adversarial-exponent-regimes) are not in that literature. |

**Aggregate count.** Of the 28 mappings: 5 clean, 12 partial, 7 divergent, 4 no-fit. The pattern is informative: most of AAD's *machinery* (Bayesian inference, gain, mismatch, IB) maps cleanly onto AI's. Most of AAD's *interpretive commitments* (objective vs. preference, directed separation as architectural classification, strategy as causal DAG, satisfaction-gap diagnostic) are divergent. And several AAD pieces (sector template, composition closure, correlation hierarchy, regime-indexed edges, adversarial dynamics) have no clean AI counterpart at all. This is not "AAD has more"; it is "the two theories cover different territory with substantial overlap on the shared machinery."

---

## §C — AAD's Load-Bearing Distinctive Claims

For each candidate distinctive claim: (i) is it genuinely distinctive, or actually present in some AI variant under different vocabulary? (ii) is it load-bearing for AAD's identity? (iii) what changes if AAD adopts the AI framing instead?

### C.1 The persistence template as derivation generator

**The claim.** AAD's persistence-flavored results — epistemic, strategic, team, composition closure, tempo composition, adversarial destabilization — are instances of one Lyapunov-based template parameterized by state variable, correction function, and effective disturbance rate (#sector-persistence-template).

**(i) Distinctive?** Yes. AI's stability arguments come from variational geometry (the dynamics flow on the free-energy gradient). The Aguilera et al. (2022) result *narrows* the parameter regime in which the FEP-flow argument works for non-equilibrium systems. AAD's sector-condition machinery makes no such narrow assumption — it is the standard control-theoretic apparatus, applies to bounded disturbance and to mean-square stochastic disturbance, and gives explicit ultimate-bound and reserve formulas. Critically, AAD's template is *parameter-free* — it abstracts away from the specific state and disturbance choice, leaving instantiation as the per-result work. AI does not have this template form.

**(ii) Load-bearing?** Yes. The template is the organizing principle proposal in O-BP1, currently under review. Without it, the persistence-flavored results read as six independent Lyapunov arguments. With it, they read as one result instantiated six ways.

**(iii) If AAD adopts AI's framing.** AAD would lose explicit ultimate-bound formulas and the per-result independence of the template instantiations. The Aguilera critique would propagate: AAD's persistence claims would inherit the narrow-parameter-regime restriction. *Net loss substantial.* This is a place AAD genuinely differs and should keep differing.

### C.2 Satisfaction-gap / control-regret diagnostic split

**The claim.** $\delta_{\text{sat}} = V_{O_t}^{\min} - A_O$ and $\delta_{\text{regret}} = A_O - V_O(\pi_{\text{current}})$ form a 2×2 diagnostic table distinguishing "goal too hard" from "strategy too weak," with monotonicity along the convention hierarchy C1/C2/C3 (#satisfaction-gap, #control-regret, #value-object).

**(i) Distinctive?** Partial. The expected-utility regret literature has decompositions that are *cousins* (regret vs. attainability gap; Bayes risk vs. minimax regret). The specific split in AAD is novel — the 2×2 diagnostic and the disambiguation table for $\delta_{\text{sat}}\gt 0$ are not in standard AI. EFE has its own decomposition (pragmatic + epistemic), which is *different* in content: pragmatic value asks "how preferred are the expected outcomes?" (akin to $A_O$ alone); it does not separate "is the preferred outcome attainable?" from "am I doing the best available?"

**(ii) Load-bearing?** Yes. The diagnostic is what makes the orient cascade actionable (#orient-cascade) — each cell prescribes a different corrective action. Without it the cascade has nothing to disambiguate at the strategy/objective branch.

**(iii) If AAD adopts AI's framing.** Replacing $V_{O_t}$ with $C(o) = \log P_{\text{pref}}(o)$ and reading $\delta_{\text{sat}}$ as "expected log-evidence shortfall" loses the disambiguation. The 2×2 collapses because both axes become "expected free energy is too high." The rich diagnostic structure depends on $V_{O_t}$ being a *value functional* and $A_O$ being an *attainability supremum*, not a log-prior comparison. *Net loss substantial.* This is the strongest case against G-BP2's strong form.

### C.3 Directed separation as architectural classification

**The claim.** Whether the agent's epistemic update $f_M$ depends on its goals $G_t$ is an architectural property (Class 1 modular / Class 2 fully merged / Class 3 partial), with operational measurement $\kappa_{\text{processing}}$ and explicit scope assignment (Section II's exact results apply to Class 1; Class 2 needs the coupled formulation in `03-logogenic-agents/`) (#directed-separation).

**(i) Distinctive?** Yes — but it is the same vicinity as the Markov blanket. The substantive difference: AAD treats directed separation as a *property of the agent's processing graph* (does $G_t$ have a causal path to $f_M$ that bypasses observation?) and admits the property fails for transformer LLMs by construction. AI's Markov blanket is typically presented as *universal* (every system has one) and as *demarcating self from other*. The Bruineberg et al. (2022) critique splits "Pearl blankets" (statistical, well-defined) from "Friston blankets" (metaphysical, overruns the formalism); AAD's directed separation is structurally a Pearl-blanket move with *honest scope failure modes*, not a Friston-blanket move with universal claims.

**(ii) Load-bearing?** Yes. Section II's exact results depend on it; the Class 2 honest-scope-exit (`section-ii-survival.md`'s 16/24 exact survival) depends on it; the entire `03-logogenic-agents/` framework exists because directed separation fails for the agent class everyone cares about.

**(iii) If AAD adopts AI's framing.** Two possibilities. Adopting the *strong* Friston-blanket reading would import the Bruineberg critique and overclaim what the formalism justifies. Adopting the *weak* Pearl-blanket reading would lose the architectural classification (Class 1/2/3 as a partition) and keep only the conditional-independence statement, losing the scope honesty. *Either net loss substantial.* AAD should keep its architectural-classification framing and explicitly cite the Bruineberg critique as the reason.

### C.4 Strategy as a probabilistic causal DAG with regime-indexed edges and a correlation hierarchy

**The claim.** $\Sigma_t$ is a DAG (acyclicity derived from temporal ordering, Markov factorization derived from causal sufficiency via the CMC theorem — see #graph-structure-uniqueness), with single-parameter edges, AND/OR combination, regime-indexed causal-validity (A/B/C in #edge-update-causal-validity), and a correlation hierarchy (L0/L1/L1'/L2 in #strategy-dag).

**(i) Distinctive?** Yes, strongly. AI's policies are typically enumerated action sequences (in discrete-state AI) or continuous policy distributions (in continuous-state AI). They are scored by EFE but *not structurally a causal DAG*. AAD's strategy-as-DAG is a fundamentally different representational commitment. The correlation hierarchy explicitly handles correlated failure (which is a known weakness of naive Bayes-net reasoning when the DAG is causally insufficient — see CMC literature) — this is a contribution AI does not make.

**(ii) Load-bearing?** Yes. The strategy persistence schema (#strategy-persistence-schema), the credit-assignment boundary (#credit-assignment-boundary), the cognitive cost of strategy (#strategy-complexity-cost), the orient cascade's strategy-revision step (4a/4b/4c), all rest on $\Sigma_t$-as-DAG.

**(iii) If AAD adopts AI's framing.** The DAG structure would be replaced by an EFE-scored policy distribution. The correlation hierarchy would have to be reformulated (and it is unclear what shape it would take in EFE). The regime-indexed edges would have no clear home. *Net loss very substantial.* This is the second strongest case against G-BP2's strong form.

### C.5 Causal hierarchy requirement and loop-interventional-access

**The claim.** Evaluating $Q_O$ requires Pearl Level-2 access; the feedback loop generates interventional data by construction (#causal-hierarchy-requirement, #loop-interventional-access).

**(i) Distinctive?** Partial. The substantive observation that "the agent's actions causally precede outcomes, so loop data is interventional in character" is implicit in AI but not lifted as a load-bearing theorem. The Bareinboim et al. (2022) causal-hierarchy theorem is not invoked in standard AI literature. AAD makes this explicit. The strength of identification (Regime A/B/C) is purely AAD.

**(ii) Load-bearing?** Yes for AAD's relationship to causal inference. It is what makes the strategy DAG a *causal* DAG rather than a *Bayesian-network* DAG.

**(iii) If AAD adopts AI's framing.** Would lose the explicit Level-1/Level-2 distinction and the regime-indexed edge interpretation. The CIY definition would shift from "action-distinguishability under do" to "expected information gain under softmax-weighted policy" (the EFE epistemic-value form). *Moderate loss.* The CIY shift is recoverable; the regime indexing is harder.

### C.6 Composition closure with measurable closure defect

**The claim.** A group of agents is a meaningful composite when its closed-loop dynamics approximately commute with coarse-graining — measured by the closure defect $\varepsilon^\ast$ over admissible projections satisfying (P1)–(P3) and admissible macro-dynamics satisfying (A1)–(A4), with a sector-Lyapunov bridge lemma (#composition-closure).

**(i) Distinctive?** Yes. AI's hierarchical generative models stack abstractions but do not produce a quantitative homomorphism bound between micro and macro dynamics. The Mori-Zwanzig connection AAD draws (in #composition-closure's Working Notes) is to dynamical-systems coarse-graining literature, not to AI literature.

**(ii) Load-bearing?** Yes. Section III's entire program rests on it.

**(iii) If AAD adopts AI's framing.** Composition would become "additional layer of generative model," losing the dynamical-homomorphism bound and the bridge-lemma persistence transfer. *Net loss substantial.*

### C.7 Convention hierarchy C1/C2/C3 with monotonicity

**The claim.** Three named continuation conventions form a hierarchy with proved monotonicity of $A_O$ and inverse monotonicity of $\delta_{\text{sat}}$ (#value-object).

**(i) Distinctive?** No. These are standard horizon choices across decision theory and RL — one-step lookahead, receding horizon, Bellman-optimal. AAD's contribution is making the choice *explicit* in the diagnostic interpretation of $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$ and proving the monotonicity. AI typically uses the C3-Bellman convention without naming it as a convention; the convention-hierarchy framing helps AAD distinguish "globally infeasible" from "locally stuck" diagnoses.

**(ii) Load-bearing?** Yes for AAD's diagnostic apparatus; not particularly for AI comparison.

**(iii) If AAD adopts AI's framing.** Almost no change — AI works at C3 implicitly, and AAD's C2 default (one-step improvement) is a costed-down approximation. The hierarchy itself is convention-neutral.

### C.8 The G_t = (O_t, Σ_t) split as definitional-not-derived

**The claim.** $G_t$ decomposes into objective (evaluation) and strategy (guidance) — a definitional split at the level of *kinds of question being asked*, not a timescale or empirical claim (#strategy-dimension).

**(i) Distinctive?** Yes versus AI's standard preferences-and-policy framing. AI also separates preferences ($C$) from policy ($\pi$), so the structural split is similar. The content of the split differs: AAD makes objectives value functionals on trajectories and strategy a causal DAG; AI makes preferences log priors on outcomes and policy a softmax over EFE.

**(ii) Load-bearing?** Yes. O-BP2 (compressions-as-projections) currently proposes generalizing this to "$G_t$ as a single object with $(O_t, \Sigma_t)$ as a property"; the strategic-architectural-proposal review notes this is a *property*-based reframing that would change the segments but is being considered against G-BP2 directly.

**(iii) If AAD adopts AI's framing.** Mostly recoverable — the structural split survives; the content of each component would change. The most significant losses are in §C.2 (satisfaction gap) and §C.4 (strategy as DAG), which are the cases where the *content* matters, not the *split*.

### Honest summary of distinctive claims

The distinctive claims that survive the AI engagement most strongly are: §C.1 (persistence template as derivation generator), §C.2 (satisfaction-gap / control-regret diagnostic), §C.4 (strategy as causal DAG with correlation hierarchy), §C.6 (composition closure with measurable defect), and §C.3 (directed separation as architectural classification with honest scope). The claims that *partially* hold but with significant overlap are §C.5 (causal hierarchy and loop-interventional-access — substantive overlap with AI's implicit treatment) and §C.8 (the $G_t$ split — structural overlap, content divergence). The claim that does *not* hold as distinctive is §C.7 (convention hierarchy — these are standard).

The IB-shape across compression operations (#compression-operations) is *not* listed as a distinctive AAD claim because the IB-unification spike already affirmed it as U-medium (shared shape, not unified objective). On that axis AAD and AI overlap rather than diverge.

---

## §D — AI Claims AAD Does Not Make

For each: should AAD adopt, explicitly refuse, or remain agnostic? Reasoning per choice.

### D.1 Priors-as-preferences (C(o) = log P_pref(o))

**The claim.** The agent's preferences are encoded as a prior over outcomes; "wanting $o$" and "expecting $o$" are formally the same operation.

**Recommendation: explicitly refuse.** The conflation creates the dark-room problem (Sun & Firestone 2020) and requires the EFE epistemic-pragmatic split as a repair. AAD's value-functional framing (#objective-functional) is cleaner: $V_{O_t}$ evaluates a trajectory; $\hat{o}_t$ predicts an observation; the two are different operations on different objects. The §C.2 satisfaction-gap diagnostic depends on this separation.

### D.2 Strong FEP (all self-organizing systems minimize VFE; Markov blankets demarcate self ontologically)

**The claim.** Every self-organizing system that resists dispersion can be cast as an inferential agent minimizing variational free energy on its sensory states; Markov blankets are the ontological boundary between self and world.

**Recommendation: explicitly refuse.** This is the metaphysical claim that AAD's contemporaries (Bruineberg et al. 2022, Andrews 2021, Colombo & Wright 2018, Aguilera et al. 2022) substantially contest. Adopting it would saddle AAD with the same critique. AAD already has scope honesty via the agent-environment definition (#agent-environment) and the Class 1/2/3 architectural classification — it does not need the universal claim to make its results work, and adopting it would obscure the scope honesty.

### D.3 Markov blanket as ontologically fundamental

**The claim.** The Markov blanket is the principled boundary between agent and environment, with internal states "owning" the blanket statistically.

**Recommendation: explicitly refuse the metaphysical reading; adopt only as the technical conditional-independence statement.** AAD's directed separation (#directed-separation) does the work the Markov blanket is asked to do, with the extra benefit of architectural classification and operational $\kappa_{\text{processing}}$. The Bruineberg Pearl-vs-Friston distinction is the literature signal: AAD should keep the Pearl-style use and refuse the Friston-style use.

### D.4 Expected free energy as master objective

**The claim.** EFE = pragmatic value + epistemic value is *the* policy objective; agents minimize expected free energy under softmax($-G(\pi)$).

**Recommendation: remain agnostic at the master-objective level; adopt EFE-style decomposition where it adds clarity.** This is the G-BP2 question, addressed in §E. The honest reading: EFE is one of several principled policy objectives (others: expected utility, KL-control, posterior-sampling Thompson-style). AAD's $\pi^\ast = \arg\max_a [Q_O + \lambda \cdot \text{CIY}]$ is a *specific* exploit-explore form (#ciy-unified-objective) that maps cleanly to the EFE pragmatic-plus-epistemic decomposition without committing to EFE's preferences-as-priors form. AAD can borrow the *shape* (objective decomposes into pragmatic and epistemic) without the *substance* (preferences are log priors).

### D.5 Action-as-inference

**The claim.** Action selection is itself a form of Bayesian inference — selecting the action whose outcomes are most consistent with prior preferences.

**Recommendation: remain agnostic.** This is a presentational stance, not a load-bearing commitment. AAD presents action as the policy $\pi(M_t, G_t)$ that solves an explicit objective; AI presents action as inference under the EFE prior. The objects and computations are equivalent up to relabeling for the Bellman case (compare AAD's #value-object C3 convention with AI's softmax-over-EFE). For C1 and C2 conventions the action-as-inference framing is more strained. AAD can credit AI's framing as one valid interpretation without adopting it.

### D.6 Hierarchical generative models

**The claim.** Cognition is a hierarchy of generative models, each level predicting the next, with prediction errors flowing up and predictions flowing down (Friston 2008, 2010; Clark 2013).

**Recommendation: remain agnostic; partial adoption via composition machinery.** This is the substantive overlap with AAD's compositional structure. AAD's composition-closure (#composition-closure) is a *dynamical homomorphism* claim about admissible projections; the hierarchical-generative-model picture is a *generative-model factorization* claim. The two are compatible — admissible projections (P1)–(P3) for AAD are compatible with hierarchical-model layering for AI — but they answer different questions. AAD can credit the framing as motivation; the formal content stays AAD's.

### D.7 Precision dynamics (Friston's precision-as-attention)

**The claim.** The brain modulates the precision (inverse variance) on prediction errors at different levels to implement attention; precision dynamics is the signature of cognitive control.

**Recommendation: adopt as the natural realization of $\eta^\ast$ in neural-flavored agents.** AAD's update gain $\eta^\ast$ (#update-gain) is precisely the precision-on-the-prediction-error in the Bayesian setting. The AI literature has worked out the realization extensively; AAD can cite that work as a domain instantiation of the gain principle. The two frameworks agree on this object.

### D.8 Ergodic-density / NESS framing of the FEP

**The claim.** Self-organizing systems have a non-equilibrium steady-state density on which the FEP-flow argument runs; this is the bridge between the formal FEP and physical realization (Friston 2019, Friston et al. 2023).

**Recommendation: explicitly refuse.** This is the part of FEP that the Aguilera et al. (2022) critique narrows the validity of: the NESS-density framing works only in a small parameter regime for non-equilibrium linear stochastic systems. AAD's persistence template (#sector-persistence-template) makes a *much weaker* and *much broader* stability claim that does not depend on NESS structure. Adopting the NESS framing would import a debate that AAD does not need.

### Summary of D

AAD should: **explicitly refuse** D.1 (priors-as-preferences), D.2 (Strong FEP), D.3-strong (Friston-blanket reading of Markov blanket), D.8 (NESS framing). **Remain agnostic on / cite without adopting** D.4 (EFE as master objective — that is the G-BP2 question), D.5 (action-as-inference), D.6 (hierarchical generative models). **Adopt as instantiation** D.3-weak (Pearl-blanket conditional independence — already has it via #directed-separation), D.7 (precision dynamics — already has it via $\eta^\ast$ and update gain).

The pattern: AAD borrows AI's mathematical machinery where it cleanly maps and refuses AI's metaphysical commitments where they overrun the formalism.

---

## §E — Tier-Strength Analysis on G-BP2

This section parallels §1.2 of `msc/spike-ib-unification-plan.md`. The IB spike distinguished (U-strong) full reduction, (U-medium) shared shape, (U-weak) presentational lens, and recommended the synthesis-segment route (which became `#compression-operations`). The same three-strength analysis applies to G-BP2.

### E.1 The G-BP2 unification conjecture, stated formally

G-BP2 (Gemini bigger-picture §2, 2026-04-22) proposes reframing $\Sigma_t$ not as an information bottleneck of the causal history but as a *variational approximation of the true, intractable optimal policy* $\pi^\ast$. The cognitive cost becomes the KL-divergence between the tractable DAG structure and the combinatorial optimal-policy space; the agent minimizes a variational free-energy objective balancing expected reward of the plan against informational cost of maintaining DAG constraints. The Shannon zero-MI degeneracy of `#strategy-complexity-cost` (Gemini Finding 2: when $\pi^\ast$ is deterministic-from-$M_t$, $I(\Sigma_t; \pi^\ast \mid M_t) = 0$) is replaced with a bounded-computation-aware KL objective.

Three strengths:

**(V-strong) Full VFE reformulation.** AAD's strategy/objective machinery is *recast* as variational free-energy minimization. $O_t$ becomes preferences encoded as $C(o) = \log P_{\text{pref}}(o)$; $\Sigma_t$ becomes a variational policy posterior; the orient cascade becomes the message-passing schedule for variational inference; satisfaction gap and control regret become components of EFE. The persistence machinery is interpreted as flow on the free-energy gradient. [Hypothesis]

**(V-medium) Shared variational shape with selective adoption.** AAD adopts the *variational form* of the strategy-IB objective (KL between tractable $\Sigma_t$ and the policy-relevant target rather than Shannon mutual information) — this resolves Gemini Finding 2 by construction. AAD does *not* adopt EFE as master objective, does *not* adopt preferences-as-priors, does *not* reinterpret the persistence template as VFE-flow. Other AAD machinery (objective as value functional, strategy as causal DAG, satisfaction-gap diagnostic, directed-separation classification) is preserved unchanged. The variational framing appears specifically where it resolves Finding 2 and adjacent issues. [Discussion / Formulation]

**(V-weak) Presentational lens with shared vocabulary.** AAD's segments adopt variational vocabulary in Discussions where it clarifies the connection to AI. No formal commitment changes; cross-references to Friston et al. and Da Costa et al. are added to relevant segments (#strategy-complexity-cost, #information-bottleneck, #ciy-unified-objective). The strategy-IB objective stays in its current form; Gemini Finding 2 is addressed by a smaller technical patch (e.g., regularization or a different functional form for the relevance term). [Discussion]

Honest defaults: V-weak is trivially achievable and would close Finding 2 only if the technical patch addresses it independently. V-medium is the substantive option that mirrors what `#compression-operations` did for IB unification. V-strong is the most ambitious option and the one most directly comparable to Friston-style framings.

### E.2 What V-strong would cost and buy

**Cost.** Substantial. Touches the central strategic objective and the satisfaction-gap / control-regret diagnostic apparatus. Requires deciding the AI variant to adopt (sophisticated inference is the closest fit for AAD's bounded-rationality flavor). Importing EFE's preferences-as-priors collapses the §C.2 diagnostic split (see §C.2 above for why). Importing the FEP-as-flow framing would import the Aguilera critique (see §D.8).

**Buy.** Direct integration with AI literature; ML-literate readers immediately recognize the framework; the dark-room and exploration-exploitation literature becomes directly available; Finding 2 is resolved by construction. The unification narrative — "AAD is a control-theoretic specialization of active inference" — becomes legible (which is what some reviewers will want to hear).

**Net.** The buy is rhetorical; the cost is the satisfaction-gap diagnostic and the architectural-classification scope honesty. Both are core distinctive AAD claims (§C.2, §C.3). Recommendation: **do not pursue V-strong.** The IB spike's parallel verdict was the same — U-strong was unlikely to be achievable cleanly because cross-instance theorems do not follow from the shared shape alone; here V-strong is unlikely to be achievable cleanly because AAD's distinctive content does not survive the reformulation.

### E.3 What V-medium would cost and buy

**Cost.** Moderate. Touches `#strategy-complexity-cost` directly (the Finding 2 segment): replace the Shannon mutual information $I(\Sigma_t; \pi^\ast \mid M_t)$ with the KL between $\Sigma_t$ (as a tractable distribution over policies) and the policy-relevant target. The relevance variable becomes a *KL target*, not a *mutual-information argument*. Other segments touched lightly: `#compression-operations` adds a paragraph on the variational reading of strategy compression; `#exploit-explore-deliberate` notes that the AAD exploit/explore framing maps to EFE's pragmatic/epistemic decomposition (a Discussion-level cross-reference). The IB spike's `#compression-operations` synthesis segment provides the model.

**Buy.** Resolves Gemini Finding 2 cleanly (no Shannon-zero degeneracy because KL handles deterministic $\pi^\ast$ correctly). Makes the strategy-cost objective interoperable with the broader variational-inference literature. Inherits the literature's bounded-rationality variants (sophisticated inference; KL-control; resource-rational analyses) for free. Does *not* require adopting preferences-as-priors, EFE as master, or the FEP-as-flow framing — so the §C.2 diagnostic split, §C.3 scope honesty, and §C.4 strategy-as-DAG content all survive.

**Net.** The buy is concrete and load-bearing (Finding 2 is currently open); the cost is moderate and contained. Recommendation: **pursue V-medium.** The execution shape mirrors `#compression-operations`: a synthesis-segment-first move, with the option to escalate later if downstream segments reveal pulling in inconsistent directions.

### E.4 What V-weak would cost and buy

**Cost.** Minimal. Each affected segment's Discussion gets one paragraph naming the variational analog and citing Friston et al. and Da Costa et al. No formal content changes.

**Buy.** Reader navigation. AI-fluent reviewers see the connection without having to construct it themselves. Does not resolve Finding 2 unless that finding is addressed independently.

**Net.** Insufficient on its own (Finding 2 stays open); useful as a compositional add-on to V-medium. Recommendation: **subsume into V-medium** — V-medium naturally includes the Discussion-level cross-references that V-weak would provide.

### E.5 Comparison to the IB spike's verdict on O-BP2 / IB unification

The IB spike (`spike-ib-unification-plan.md` §8) recommended *executing the synthesis segment first* (which became `#compression-operations`) and proceeding to the full Path A + B unification only if the four instance segments were revealed as pulling inconsistently. The verdict here parallels: **execute the V-medium variational reframing of the strategy-cost objective** (which is the cheapest fix for Finding 2 with minimal collateral damage), **do not adopt V-strong** (which would import AI's contested commitments and erode AAD's distinctive diagnostic content), **subsume V-weak into V-medium** as Discussion-level cross-references.

The two verdicts are structurally parallel:

| Question | IB-unification spike | This spike (G-BP2) |
|---|---|---|
| What is the strongest version (`U-strong` / `V-strong`)? | Cross-instance theorems from shared IB shape | Full VFE reformulation of AAD |
| Is it achievable? | No — cross-instance theorems don't follow from shared shape alone | No — distinctive AAD content (§C.2, §C.3, §C.4) does not survive |
| What is the medium version? | Synthesis segment with $(X, T, Y, \beta)$ binding table for the four instances | Variational form of the strategy-cost objective; selective adoption elsewhere |
| Is it worth executing? | Yes — clarifies implicit pattern, fixes ($\Sigma_t$) source ambiguity | Yes — fixes Finding 2 without collateral damage |
| What is the weak version? | Cross-references in Discussion paragraphs | Same |
| Verdict | Synthesis-segment-first; full unification only on signal | V-medium-first; full reformulation only on signal |

The pattern: AAD's most defensible move is to absorb AI's machinery selectively where it cleanly resolves an internal issue, while keeping the foundational stance (control-theoretic, with directed-separation scope honesty and the satisfaction-gap diagnostic) distinct.

### E.6 Specific implementation sketch for V-medium

**Single segment touch: `#strategy-complexity-cost`.** Replace the Strategy IB Objective subsection's mutual-information form with a variational form *with KL direction forced by a regret-bound derivation* (F20 strengthening, commit following 2026-04-22 evening audit; the derivation now lives in appendix segment #strategy-cost-regret-bound; see `msc/spike-f20-kl-direction-strengthening.md` for the strengthening-cycle reasoning trail):

```
Theoretical form (variational). Σ_t is a tractable variational approximation of the
optimal-policy posterior Q*(π | M_t). The strategy-cost objective:

  Σ_t* = arg min_Σ [ DL(Σ_t) + β_Σ · D_KL( π* || Σ_t | M_t ) ]

The KL direction with π* first is forced by a regret-bound derivation: strategy-induced
regret R(Q_Σ) = V(a*) - E_Q[V(a)] is bounded above by V_max · sqrt(0.5 · D_KL(π* || Q_Σ))
via Pinsker under bounded value range. Forward-KL (Q_Σ || π*) is +∞ under deterministic π*
whenever Q_Σ has off-optimum mass — a vacuous bound. The π*-first direction is graded and
finite; under deterministic π*, D_KL(π* || Q_Σ) = -log Q_Σ(a*). This closes the Shannon-MI
zero degeneracy AND the forward-KL infinity degeneracy simultaneously.

This variational form is the strategy-layer analog of variational free energy
minimization in the active-inference literature (Friston 2017; Da Costa et al.
2020; Sajid et al. 2021), without committing to preferences-as-priors or to EFE
as master objective. The direction alignment is convergent: AAD derives reverse-KL
from the regret bound, AI from the free-energy-gradient argument; both arrive at
π*-first KL.
```

**Initial V-medium footnote (2026-04-22 evening correction).** The initial V-medium move (commit `a14642e`) used $D_{\mathrm{KL}}(Q_{\Sigma_t} \Vert \pi^\ast)$ (forward-KL), which has a *different* degeneracy under deterministic $\pi^\ast$: it is $+\infty$ whenever $Q_{\Sigma_t}$ places any off-optimum mass. Opus evening audit (F20) flagged this; the F20 strengthening spike derived the correct direction from the regret bound. Current segment uses reverse-KL ($\pi^\ast$-first), with direction defended by derivation rather than selected by convenience.

**Synthesis segment touch: `#compression-operations`.** Add a paragraph noting that the strategy-compression instance can be read either as Shannon-IB (current discussion) or as variational-policy-approximation (the V-medium move). Both are admissible bindings under the master IB shape — the second resolves the Shannon-zero degeneracy.

**Cross-reference touches: `#exploit-explore-deliberate`, `#ciy-unified-objective`.** One paragraph each in Discussion, noting that the exploit-explore-deliberate decomposition maps cleanly onto EFE's pragmatic-epistemic split when AAD's value object is read as expected log preferences and CIY is read as expected information gain. Cite Friston et al. 2017 and Da Costa et al. 2020. Do not commit to the full EFE master-objective interpretation.

**Effort estimate.** 1–2 sessions. Smaller than the full IB unification (2 sessions per Path A in `spike-ib-unification-plan.md` §7). Comparable to `#compression-operations` itself. No scoping spike beyond this document needed.

---

## §F — Reviewer Q&A (Anticipated)

Twelve questions a sympathetic-but-rigorous reviewer would raise, with answers grounded in §A–E.

### Q1. "Isn't directed separation just the Markov blanket?"

**Answer.** Directed separation is the *Pearl-blanket* form of conditional independence (Bruineberg et al. 2022's distinction): $M_{\tau^+} \perp G_t \mid (M_{\tau^-}, e_\tau)$. It is *not* the Friston-blanket form, which makes ontological claims about self-from-other demarcation that the formalism does not justify. The substantive AAD addition is the *architectural classification* (Class 1 modular / Class 2 fully merged / Class 3 partial) with operational $\kappa_{\text{processing}}$, which gives an honest scope-failure-mode account: Section II's exact results apply to Class 1; transformer LLMs are Class 2 by construction and need the coupled formulation in `03-logogenic-agents/`. This is AAD acknowledging where its results break, which the standard Markov-blanket framing does not naturally do (because it positions the blanket as universal). The two are kin; AAD is the conservative form.

### Q2. "Isn't the satisfaction-gap / control-regret split just expected-utility regret decomposition?"

**Answer.** Closely related but materially different. Standard regret decompositions (Bayes risk, minimax regret, attainability vs. policy gap) typically work in fully observable / closed-form settings. AAD's $\delta_{\text{sat}} = V_{O_t}^{\min} - A_O$ and $\delta_{\text{regret}} = A_O - V_O(\pi_{\text{current}})$ are defined relative to a *current model state* $M_t$ and a *named continuation convention* C1/C2/C3, and the 2×2 cell map separates "goal too hard" (capability limit) from "strategy too weak" (revisable suboptimality). The AI EFE decomposition (pragmatic + epistemic) does not separate these — both increase EFE without distinguishing cause. AAD's separation lets the orient cascade act differently in the four cells; AI's EFE does not.

### Q3. "Isn't composition closure just hierarchical generative models?"

**Answer.** No. Hierarchical generative models *layer* generative models with prediction errors flowing up and predictions flowing down. They are an architectural choice for the inference engine. AAD's composition closure is a *measurable defect* between micro and macro dynamics — given admissibility constraints (P1)–(P3) on projections and (A1)–(A4) on macro-dynamics, the closure defect $\varepsilon^\ast$ is the irreducible cost of representing a multi-agent system as a single AAD agent, and a sector-Lyapunov bridge lemma transfers persistence from sub-agents to composite. There is no such homomorphism-defect bound in the hierarchical-generative-model literature. The two are complementary: hierarchical generative models could *implement* AAD-admissible projections, but they don't deliver the closure defect or the persistence transfer.

### Q4. "Isn't the orient cascade just precision-weighted prediction-error message passing?"

**Answer.** They overlap on the substrate (both order updates by information dependency) and diverge on the structure. AAD's orient cascade is a *derived sequential ordering* — $M_t$ first, then strategic feasibility evaluation ($\delta_{\text{sat}}$), then strategy revision ($\delta_{\text{regret}}$, then $\delta_s$, then strategic-calibration), then objective revision. Each step depends on prior outputs by *logical* dependency, not by message-passing schedule. AI's variational message passing is *simultaneous within the variational scheme* — the "order" is the order of message updates, not a logical dependency that locks step 5 (objective revision) behind step 1 (epistemic update). The cascade's diagnostic content (the 2×2 with disambiguation table) does not survive the message-passing reframing.

### Q5. "Why use IB at all when VFE subsumes it? Isn't IB the rate-distortion specialization of VFE?"

**Answer.** IB and VFE share rate-distortion structure. The IB-unification spike (`spike-ib-unification-plan.md`) was specifically designed to evaluate this — its verdict was U-medium (shared shape) not U-strong (single master problem). The reasons: (a) different relevance variables across AAD's four compression operations don't unify into one VFE objective without strong additional commitments (resource-allocation across the four $\beta$'s); (b) (P2) Lipschitz and (P3) dimensional reduction in composition are *separate* admissibility conditions that VFE does not impose; (c) the strategy-compression Shannon-zero degeneracy (Gemini Finding 2) is a real issue under IB and is what V-medium of G-BP2 would fix. AAD adopts VFE's variational form selectively where it resolves an issue (the V-medium move on $\Sigma_t$); it does not subsume IB into VFE wholesale because the cross-instance theorems do not follow.

### Q6. "What does AAD's persistence template give you that Friston's flow on the free-energy gradient doesn't?"

**Answer.** Three things. (a) *Broader validity:* the Aguilera et al. (2022) critique narrows the FEP-flow argument to a small parameter regime for non-equilibrium linear stochastic systems; AAD's sector-condition machinery makes no such narrow assumption — bounded disturbance (Model D) and mean-square stochastic (Model S) cover the standard cases. (b) *Quantitative ultimate-bound formulas:* $R^\ast = \rho/\alpha$ in the deterministic case; $R^\ast_S = \sigma\sqrt{n/(2\alpha)}$ in the stochastic case; explicit adaptive reserve $\Delta\rho^\ast = \alpha R - \rho$. The Friston flow argument is qualitative about stability; the AAD template is quantitative about both stability and reserve. (c) *Direct instantiation across results:* the same template applies to epistemic mismatch, strategic mismatch, team mismatch, composite trajectory error, composite mismatch, and adversarial destabilization (#sector-persistence-template's instantiation table). The Friston-flow framing does not have this template-and-instantiations structure.

### Q7. "Why a separate theory rather than a domain-applied AI?"

**Answer.** Because the two foundational stances differ substantively. AAD starts from operational requirements on a feedback-coupled adaptive system and adds compression as a modeling move; AI starts from a single optimization principle and recovers the rest. Treating AAD as domain-applied AI would require: (a) accepting preferences-as-priors (which collapses the satisfaction-gap diagnostic — §C.2); (b) accepting Strong FEP or its NESS framing (which imports the Aguilera and Bruineberg critiques — §D.2, §D.8); (c) replacing the strategy-as-causal-DAG with EFE-scored policy enumeration (which loses the correlation hierarchy and regime-indexed edges — §C.4); (d) replacing directed-separation-as-architecture with Markov-blanket-as-ontology (which loses the Class 1/2/3 scope honesty — §C.3). The cost is the distinctive content; the buy is rhetorical alignment with one (contested) tradition. The honest framing is that AAD and AI are *neighboring theories* with shared machinery and divergent foundational stances, with substantive overlap and substantive disagreement on what is foundational.

### Q8. "Don't your 'four compression operations as IB' just rediscover the EFE?"

**Answer.** They share rate-distortion structure (see Q5). The four AAD compression operations are: $M_t$ (model compression for prediction), $\Sigma_t$ (strategy compression for guidance), shared intent (compression for coordination), and composition projection (compression for level-bridging). EFE is a different decomposition: pragmatic value (preferences-aligned outcomes) plus epistemic value (information gain about hidden states), summed over a planning horizon. The substantive overlap: $M_t$-compression's relevance variable (predictive information) corresponds to EFE's epistemic value if the relevance is read as information about the world; AAD's CIY corresponds to EFE's epistemic value if read as information about the world. The substantive non-overlap: AAD's shared intent and composition projection have no canonical EFE counterpart; EFE's pragmatic value has no canonical AAD compression counterpart (AAD's pragmatic content lives in $V_{O_t}$ not in compression). The two decompositions operate at different levels and on different objects.

### Q9. "Doesn't sophisticated active inference (Friston, Da Costa et al. 2021) already handle bounded computation? Why does AAD need its own complexity-cost machinery?"

**Answer.** Sophisticated inference handles bounded computation via *recursive EFE* with depth-limited belief-about-belief reasoning. AAD's strategy-complexity-cost (#strategy-complexity-cost) handles it via DL/IB on the strategy DAG, with a derived maximum-useful-depth $d^\ast$ from per-edge persistence and evidence-starvation under Beta-Bernoulli updates. The two address the same problem with different machinery. AAD's machinery is more *causally structured* (the depth limit is derived from the strategy DAG's chain confidence decay and edge calibration dynamics, not from belief-recursion depth). Sophisticated inference is more *Bayesian-uniform* (the same EFE form applied recursively). Either could be adopted; the V-medium move on G-BP2 specifically opens the door to citing sophisticated inference as a co-developed alternative.

### Q10. "Where does AAD's loop-interventional-access (the 'loop is a Level-2 engine' result) actually differ from saying 'the agent's own actions create the data it learns from'?"

**Answer.** The substantive content overlaps; the framing makes the difference. Standard AI recognizes that the agent's actions cause its observations but does not lift this to a load-bearing theorem about access to Pearl Level 2. AAD invokes the Bareinboim et al. (2022) causal-hierarchy theorem and concludes: the loop produces *intervention-generated* data, which is the substrate Level-2 queries need; without the loop, only Level-1 access is available. This makes the regime-indexed interpretation of strategy edges (A: intervention-rich; B: partial; C: observation-only — see #edge-update-causal-validity) sensible, and underwrites AAD's commitment to "$\Sigma_t$ is a causal DAG, not a Bayesian-network DAG." AI uses Bayesian-network-style generative models without committing to Pearl-Level-2 access as load-bearing.

### Q11. "What's the strongest concession AAD should make to AI?"

**Answer.** Three concessions, all already made or in flight:

(a) The IB-shape across compression operations is *the same shape* as variational free energy in its $-F = $ accuracy $-$ complexity decomposition. AAD has acknowledged this in `#compression-operations` (U-medium, shared shape, not unified objective).

(b) The strategy-IB objective's Shannon zero-MI degeneracy under deterministic $\pi^\ast$ (Gemini Finding 2) is real and the cleanest fix is the variational-form move (V-medium of G-BP2 above). AAD should execute this and credit AI's variational-inference machinery for the form.

(c) The exploit/explore decomposition is structurally the EFE pragmatic/epistemic decomposition. AAD's exploit-explore-deliberate framing adds the deliberation axis (which sophisticated inference handles via recursive EFE; the AAD framing is structurally adjacent). Discussion-level cross-references should be added.

The pattern: concede shared *machinery* explicitly; do not concede divergent *foundational stance*.

### Q12. "If a reviewer insists 'this is just AI in disguise,' what do you say?"

**Answer.** Three responses, in order of escalation:

(a) Cite the §B mapping table: 5 clean, 12 partial, 7 divergent, 4 no-fit. The 7 divergent and 4 no-fit are AAD's distinctive territory; the 5 clean are the shared machinery; the 12 partial are where the substantive overlap lives. "Just AI" understates the divergent and no-fit content.

(b) Cite the §D refusals: priors-as-preferences, Strong FEP, NESS framing, Friston-blanket Markov-blanket reading. AAD explicitly does not commit to these, and the AI literature itself is contested on each (Bruineberg, Aguilera, Andrews, Litwin & Miłkowski, Sun & Firestone). "Just AI" elides which AI variant; AAD's refusals are about specific contested claims, not about AI machinery in general.

(c) Cite the §C distinctive claims: persistence template as derivation generator, satisfaction-gap diagnostic, strategy as causal DAG with correlation hierarchy, composition closure with measurable defect, directed-separation as architectural classification. These are five places where AAD makes a distinctive contribution. If the reviewer can show that any of these is actually present in AI under different vocabulary, the concession is honest and AAD should incorporate; if the reviewer cannot, the "just AI" framing is itself the disguise.

---

## §G — Open Positions and Research Questions Surfaced

The AI engagement reveals genuine open work for AAD itself.

**G.1 The interventional-IB / causal-IB extension (Wieczorek & Roth 2017 and follow-ups).** AAD's regime-indexed edges (A/B/C) want interventional relevance for Regime A; the standard IB and the standard EFE both work at Level 1. There is a small literature on causal IB; adapting it to AAD's regime-indexed edges is a real research direction. This is logged in `#composition-operations` Working Notes as "open: interventional IB for regime-A edges" and is noted in IB-unification spike §6.4.

**G.2 The $\beta$-coordination problem.** AAD's four compression operations each have their own $\beta$. The IB-unification spike (§6.5) flagged this; AI's master-EFE framing has the same issue under bounded-rationality variants (different EFE temperatures across hierarchical levels). Whether AAD wants a resource-allocation-across-compressions theory is open. The G-BP2 V-medium move does not address this; nor does AI directly.

**G.3 The deliberation axis in EFE.** Sophisticated active inference (Friston, Da Costa, Hafner, Hesp, Parr 2021) handles bounded computation via recursive EFE. AAD's exploit-explore-deliberate (#exploit-explore-deliberate) handles it via a third axis with extended deliberation threshold. The two are related but not identical; whether AAD wants to adopt the recursive-EFE form for the deliberation axis is open. Listed in `#exploit-explore-deliberate`'s Working Notes as "open: conditions for deliberation dominance."

**G.4 The G_t-as-single-object reframing (O-BP2 in `architectural-proposals-2026-04-22.md`).** O-BP2 proposes treating $G_t$ as a single compression with $(O_t, \Sigma_t)$ as a *property*, not as separate axiomatic objects. This is structurally similar to AI's policy-with-priors framing (where $C$ and $\pi$ are projections of one variational object). The G-BP2 vs. O-BP2 tension is noted in `architectural-proposals-2026-04-22.md` cross-proposal interactions; the V-medium move on G-BP2 does not preclude pursuing O-BP2 separately, and the two together would push AAD significantly closer to AI's framing (without quite reaching V-strong because the diagnostic separation §C.2 still requires the object-level distinction at use time).

**G.5 The architectural classification's relationship to AI's bounded-rational variants.** AAD's Class 1/2/3 maps loosely onto AI's modular vs. fully-merged generative-model architectures, but AI literature does not name the partition or use it for scope assignment. Whether the AI bounded-rational lineage (KL-control, sophisticated inference, resource-rational analyses) has a parallel scope-honesty discussion that AAD could engage with is an open literature question.

**G.6 The empirical embeddings work (Joseph's `~/src/embeddings/`) and AI's predictive-coding lineage.** The CMCL 2026 paper-in-prep on calibrated probability geometry in pretrained embeddings is structurally adjacent to AI's predictive-coding-in-language-models work. Whether AAD's logogenic-agent program should engage that literature directly is open.

---

## §H — Honest Dissenting Note

The honest read after working through the comparison: **AAD does have substantive distinctive content, but the project is currently *underclaiming* on three of its strongest contributions and *overlapping more than it acknowledges* on two others.**

### Underclaim 1 — The persistence template's broader-validity advantage over FEP-flow.

The Aguilera et al. (2022) critique of the FEP-flow stability argument is a major literature signal that the AI field has not fully absorbed. AAD's sector-Lyapunov template makes a *much weaker* and *much broader* stability claim. Currently AAD presents this as "we do control theory rigorously"; it could present it as "we do the persistence work AI tries to do, with broader validity and explicit ultimate-bound formulas." The strategic positioning here is stronger than current AAD framing acknowledges.

### Underclaim 2 — The directed-separation architectural classification as scope honesty.

The Bruineberg et al. (2022) Pearl-vs-Friston critique is the literature signal that AI's metaphysical use of Markov blankets overruns its formalism. AAD's directed-separation classification (Class 1/2/3 with $\kappa_{\text{processing}}$) is the *honest version* of the same machinery — it uses the conditional-independence statement without the metaphysical reach, and it explicitly assigns scope by class. Currently AAD's framing is "directed separation is a scope condition we admit fails for Class 2 agents"; it could be "directed separation is the conservative-form version of the Markov blanket, which the AI literature itself contests in its strong form." The reframing is rhetorically substantial without changing any content.

### Underclaim 3 — The satisfaction-gap / control-regret diagnostic as material decision-making content.

The 2×2 diagnostic with disambiguation table is operationally rich content that AI's EFE decomposition does not produce. Currently AAD presents this as part of Section II's "diagnostic core"; it could present it as "the working decision-theory apparatus AI's preferences-as-priors framework collapses." For deployed agentic systems (the audience that cares about diagnostics, not metaphysics), this is a stronger selling point than current framing makes visible.

### Overlap 1 — AAD's loop-interventional-access overlaps more with implicit AI content than acknowledged.

The substantive observation (the agent's actions cause its observations, so loop data is intervention-generated) is implicit in any agent-environment loop framing, including AI's. AAD's distinctive contribution is *naming this as a load-bearing theorem and connecting it to Pearl Level 2 via Bareinboim et al. (2022)*. The framing is distinctive; the substantive content is closer to shared than current AAD treatment suggests. Honest credit to AI's implicit treatment is appropriate.

### Overlap 2 — AAD's compression operations and AI's hierarchical generative models share more than the IB-unification spike acknowledged.

The IB-unification spike treated AAD's four compression operations as internally unified at U-medium (shared shape). The further question — to what extent these four are jointly the same family as AI's hierarchical generative models — was not addressed. The honest read: AAD's compressions are a *subset of the operations* AI's hierarchical-generative-model framework could express, with additional structure (the relevance variables are made first-class; the (P1)–(P3) admissibility for composition; the regime-indexed edges for strategy). The shared family is real; AAD's additions are also real. Crediting AI for the family while keeping AAD's additions is the honest move.

### Net dissenting verdict

AAD is *not* substantially overlapping with AI to the point of being "AI in disguise" — the distinctive claims in §C are real. But AAD is *also not* a wholesale alternative — it overlaps substantially with AI's machinery in compression, in mismatch dynamics, in the exploit/explore decomposition. The honest positioning is "neighboring theory with shared machinery and divergent foundational stance, with five distinctive contributions and two substantive overlap acknowledgments." Joseph's instinct to engage Active Inference seriously is correct; the engagement should be neither defensive (AAD is fundamentally different from AI in every respect) nor capitulatory (AAD is just AI applied to control-theoretic domains). The middle position is the defensible one and is what §A's reviewer-facing summary articulates.

The G-BP2 verdict (V-medium, executed via the synthesis-segment route paralleling `#compression-operations`) is consistent with this middle position: borrow AI's variational machinery selectively where it cleanly resolves an internal issue (Finding 2), do not adopt AI's foundational commitments wholesale.

---

## §I — Summary and Recommended Actions

**Strategic positioning (§A).** AAD and AI overlap substantially in machinery, diverge in foundational stance, in objective-strategy split with diagnostics, in architectural scope honesty, and in causal-and-compositional content. The defensible reviewer-facing framing is "neighboring theory with shared machinery and divergent foundational stance."

**Mapping (§B).** 28 mappings: 5 clean, 12 partial, 7 divergent, 4 no-fit. Most machinery overlaps; most interpretive commitments diverge; several pieces (sector template, composition closure, correlation hierarchy, regime-indexed edges, adversarial dynamics) are AAD-only.

**Distinctive AAD claims (§C).** Five strongest: persistence template as derivation generator, satisfaction-gap diagnostic split, strategy as causal DAG with correlation hierarchy, composition closure with measurable defect, directed separation as architectural classification with honest scope. Two partial: causal hierarchy with loop-interventional-access, the $G_t$ split (structural overlap, content divergence). One non-distinctive: convention hierarchy C1/C2/C3.

**AI claims AAD does not make (§D).** Refuse: priors-as-preferences, Strong FEP, Friston-blanket reading of Markov blanket, NESS framing. Remain agnostic / cite without adopting: EFE as master objective (G-BP2 question), action-as-inference, hierarchical generative models. Adopt as instantiation: Pearl-blanket conditional independence, precision dynamics.

**G-BP2 tier-strength verdict (§E).** Pursue V-medium (variational form of strategy-cost objective; selective adoption elsewhere). Do not adopt V-strong. Subsume V-weak into V-medium. Effort 1–2 sessions, comparable to `#compression-operations`. Parallel to IB-unification spike's verdict on O-BP2.

**Reviewer Q&A (§F).** Twelve prepared answers, including the four most-likely-asked: directed separation vs. Markov blanket, satisfaction-gap vs. expected-utility regret, composition closure vs. hierarchical generative models, orient cascade vs. precision-weighted message passing.

**Open research questions (§G).** Six. Notable: causal-IB extension for regime-A edges; the $\beta$-coordination problem; relationship to sophisticated-inference's recursive EFE on the deliberation axis; tension between G-BP2 and O-BP2.

**Honest dissenting note (§H).** AAD currently underclaims on three of its strongest contributions (persistence template's broader validity, directed-separation as scope-honest version of Markov blanket, satisfaction-gap as decision-theory content) and overlaps more than it acknowledges on two (loop-interventional-access has implicit AI content; compression operations and hierarchical generative models share a family).

**Recommended next actions (in priority order).**

1. **Execute G-BP2 V-medium** as scoped in §E.6 (1–2 sessions). Resolves Gemini Finding 2 and brings AAD into clean dialogue with AI's variational machinery without importing the foundational commitments.

2. **Add the §C and §D framing to AAD's introductory materials** when a paper draft is being prepared (CLAUDE.md, OUTLINE.md preamble in Section II). This addresses the Underclaim 1–3 of §H and pre-empts the most-likely reviewer questions.

3. **Add cross-references to AI literature** in `#strategy-complexity-cost`, `#information-bottleneck`, `#compression-operations`, `#exploit-explore-deliberate`, `#ciy-unified-objective`, `#directed-separation`, `#sector-persistence-template`. Cite Friston 2010, Friston et al. 2017, Da Costa et al. 2020, Sajid et al. 2021, Parr & Pezzulo 2022 as the canonical AI references; Bruineberg et al. 2022, Aguilera et al. 2022, Andrews 2021, Sun & Firestone 2020, Litwin & Miłkowski 2020, Gershman 2019, Colombo & Wright 2018 as the critique references; Wieczorek & Roth 2017 as the causal-IB reference.

4. **Treat the G-BP2 vs. O-BP2 tension as not yet resolved.** The two proposals interact (both reframe what $G_t$ and $\Sigma_t$ are at the foundational level). The G-BP2 V-medium move is *compatible* with O-BP2's compressions-as-projections framing — both could be adopted, in either order. The O-BP2 scoping spike (when written) should explicitly compare against G-BP2 V-medium to confirm compatibility.

5. **Defer the V-strong decision to a paper-writing moment, not a theory-development moment.** Whether AAD ever wants to present itself as a control-theoretic specialization of active inference is a *rhetorical* decision about how to position the work for a specific audience. The current theory-development task is to keep both options open — the V-medium move on G-BP2 does this — and to make the substantive distinctions visible enough that the rhetorical move is later defensible whichever way it goes.

---

## Working Notes

- **Open: deeper engagement with sophisticated inference (Friston, Da Costa, Hafner, Hesp, Parr 2021).** The recursive-EFE form is the closest AI cousin of AAD's strategy-complexity-cost machinery and deserves a focused read. The V-medium move on G-BP2 opens the door to citing it; an actual reading of the paper would refine that citation.

- **Open: deeper engagement with continuous-state active inference.** Most of this spike has worked with the discrete-state Da Costa 2020 form because it is the cleanest reference. The continuous-state classical-Friston form (active inference on continuous state spaces) is closer to AAD's continuous-time mismatch ODE framing. Whether the comparison would change with continuous-state AI is an open question that the spike's recommendation does not depend on.

- **Open: how the comparison interacts with the C-BP1 three-layer epistemic separation (defined / causally valid / operationally extractable) proposal in `architectural-proposals-2026-04-22.md`.** Each AAD ↔ AI mapping in §B could be classified by which of the three layers the overlap occurs at. Many of the "clean" and "partial" mappings are clean at the *defined* layer but partial or divergent at *causally valid* and *operationally extractable*. C-BP1, if adopted, would let the §B table be more precise.

- **The PDF-extraction obstacles encountered during the literature review** (the WebFetch tool returned binary data for several arXiv PDFs) mean some of the AI-side citations are based on abstracts and search-result summaries rather than full-paper readings. The citations are accurate at the level used in the spike (the conceptual claims are well-attested in the literature; the mathematical formulas are conceptually but not literally extracted). For paper-writing, the references should be checked against the full PDFs.

- **The IB-unification spike (`spike-ib-unification-plan.md`) has been extensively cross-referenced as the structural precedent.** Joseph should compare the two spikes' recommendations directly — they should have parallel shapes and parallel verdicts, which they do. The G-BP2 V-medium move and the O-BP2-variant-that-became-`#compression-operations` are the two sister moves, both selective adoption of broader frameworks where they cleanly resolve internal issues without committing to the broader framework's foundational stance.

- **Citations whose specific equations were not extracted from PDFs but whose conceptual claims are well-attested.** Friston 2017 ("Active Inference: A Process Theory" — EFE pragmatic-epistemic decomposition); Da Costa et al. 2020 ("Active inference on discrete state-spaces" — A/B/C/D matrices, F and G formulas); Sajid et al. 2021 ("Active inference: demystified and compared" — comparison to RL/KL-control); Friston Da Costa Hafner Hesp Parr 2021 ("Sophisticated Inference" — recursive EFE for bounded computation); Bareinboim et al. 2022 (causal hierarchy theorem — referenced in `#causal-hierarchy-requirement` already); Bruineberg Dolega Dewhurst Baltieri 2022 ("The Emperor's New Markov Blankets" — Pearl vs. Friston blankets); Aguilera Millidge Tschantz Buckley 2022 ("How particular is the physics of the FEP?" — narrow-parameter validity); Andrews 2021 ("The math is not the territory"); Sun & Firestone 2020 ("The dark room problem"); Litwin & Miłkowski 2020 ("Unification by fiat"); Gershman 2019 ("What does the FEP tell us about the brain?"); Colombo & Wright 2018 ("First principles in the life sciences"); Wieczorek & Roth 2017 (causal information bottleneck — referenced for §G.1).
