# Architectural Proposals — 2026-04-22

**Status:** Working document. Ten architectural proposals surfaced in the three de novo audits of 2026-04-22 (Gemini, Codex, Opus). Each is documented here as an *independent architectural investment option*, evaluated on its own merits — not as machinery for subsuming local findings.

## How to read this

This is not a deferrals pile and not a to-do list. It is a portfolio of structural moves proposed for the theory, each with a thesis about what it would advance. The project's governing purpose (CLAUDE.md) makes beauty, concision, correctness, approachability, and fundamentality first-class virtues, not afterthoughts — and some of these proposals advance those virtues regardless of whether any current finding forces them. The subsumption of local findings is noted per-proposal as a secondary signal; it should not be read as the primary motivation.

Each entry carries:

- **Thesis** — what the proposal asserts / reframes.
- **Merits by dimension** — which of beauty / concision / correctness / approachability / fundamentality the move advances, with a rough strength.
- **Scope** — which segments, preambles, or appendices would change.
- **Findings subsumed** — which open findings in `pending-findings-2026-04-22.md` (or earlier) it would close if executed. Secondary signal.
- **Interactions** — which other proposals reinforce, conflict, or depend on this one.
- **Effort shape** — framing touch / scoping spike needed / multi-session refactor / substantial rewrite.
- **Risks** — what could go wrong, what makes it non-trivial.
- **Status** — unexamined / scoped / in-progress / absorbed.

Decisions about whether to pursue, scope, or defer a proposal are made by Joseph and tracked in `TODO.md` under "Strategic Architectural Proposals."

---

## G-BP1 — Natural-parameter / logit reparameterization

**Source:** Gemini bigger-picture §1 (2026-04-22).

**Thesis.** All beliefs that AAD's continuous control machinery acts on (edge credences, leaf credences, possibly $M_t$ parameters) should be represented in their natural exponential-family parameter space — log-odds for Bernoulli edges, natural parameters generally — rather than directly as probabilities in $[0, 1]$. Additive gradient updates and mismatch ODEs apply in $\mathbb{R}^n$; link functions (logit/softmax) convert to $[0, 1]$ only at the interface. This eliminates the structural tension between continuous control (which wants $\mathbb{R}^n$) and probability DAGs (which live in $[0, 1]$).

**Merits.**

- **Correctness (high).** Fixes the unbounded-gradient mechanical break (Gemini Finding 1) by construction — with log-odds, no denominator explosion pushes parameters outside valid probabilities.
- **Concision (medium).** Normalization hacks, clipping constants, and domain-bound caveats disappear throughout the strategy layer.
- **Fundamentality (medium-high).** The exponential-family parameterization is the standard bridge between information geometry and control theory; adopting it makes AAD's dual allegiance to both disciplines less awkward.
- **Beauty (medium).** Standard exponential-family treatment; familiar to readers from either lineage.

**Scope.** `#strategy-dag` (edge and leaf credence representation), `#edge-update-via-gain` (the update rule in natural parameters), `#credit-assignment-boundary` (signal function in $\mathbb{R}$), `#strategic-dynamics-derivation` (Props B.1–B.6 restated in natural parameters; Beta-Bernoulli remains the generative model but the update rule operates on log-odds). Possibly extends to `#agent-model` if $M_t$'s parameters are treated similarly. Worked examples (Kalman, bandit, L1) need minor restating.

**Findings subsumed.**

- **Gemini Finding 1** (unbounded gradient) — direct.
- Possibly resolves or simplifies parts of how `#edge-update-causal-validity`'s $\iota_{ij}$ enters the update formula.

**Interactions.**

- **Strong synergy with G-BP3 (Fisher information).** Natural parameters + Fisher information metric → natural gradient descent. These two proposals compose cleanly.
- **Natural support for O-BP4 (continuous strategy DAG).** If the DAG is continuous-valued, natural parameterization is the obvious move.
- No direct conflict with other proposals.

**Effort shape.** Framing touch in `#strategy-dag` is small; the propagation through the derivation segments and worked examples is 2–3 focused sessions. A 90-minute scoping spike would characterize the exact scope and expose any edge cases before execution. The prior spike `msc/spike-gain-sector-bridge-nonlinear.md` already explores gradient descent on logistic loss and notes that natural parameter spaces satisfy the sector condition while keeping probabilities bounded — the groundwork is partially done.

**Risks.** May expose other places in the strategy layer where probability updates are happening naively (not just in credit-assignment). May require rewriting worked examples in two representations (natural for dynamics, probability for interpretation). The Beta-Bernoulli update machinery is well-developed; recasting it in log-odds must preserve its pedagogical clarity.

**Status:** unexamined.

---

## G-BP2 — Variational free-energy framing of strategy IB

**Source:** Gemini bigger-picture §2 (2026-04-22).

**Thesis.** Reframe $\Sigma_t$ not as an information bottleneck of the causal history but as a *variational approximation* of the true, intractable optimal policy $\pi^\ast$. The cognitive cost of a strategy (description length) becomes the KL-divergence between the tractable DAG structure and the combinatorial optimal-policy space; the agent minimizes variational free energy balancing expected reward of the plan against informational cost of maintaining DAG constraints. Shannon MI's logical-omniscience assumption (which makes $I(\Sigma_t; \pi^\ast \mid M_t) = 0$ when $\pi^\ast$ is deterministic-from-$M_t$) is replaced with a bounded-computation-aware objective.

**Merits.**

- **Correctness (high).** Resolves the Shannon-zero degeneracy of `#strategy-complexity-cost` (Gemini Finding 2). The variational objective does not collapse under logical omniscience because the KL penalty directly measures representational distance from $\pi^\ast$, not information-theoretic surprise.
- **Fundamentality (high).** Aligns AAD with variational inference and active-inference literature (Friston et al.) without adopting their full commitment to priors-as-preferences. Makes bounded-computation cost intrinsic rather than imposed.
- **Approachability (medium).** Variational inference is familiar to ML-literate readers.
- **Beauty (medium-high).** A single objective balancing expected utility against representational cost is conceptually clean.

**Scope.** `#strategy-complexity-cost` primarily (the objective would be restated). Touches `#strategy-dag` (DAG as variational family), `#exploit-explore-deliberate` (the deliberation-vs-exploit tradeoff becomes a free-energy balancing). Repositions `#information-bottleneck` — possibly as a rate-distortion special case of the variational objective. Cross-ref from `#compression-operations`.

**Findings subsumed.**

- **Gemini Finding 2** (degenerate MI in strategy IB) — direct.
- Partial subsumption of **Opus Finding 4** (`#information-bottleneck` status mismatch): if IB is a special case of variational inference, its classification may clarify.

**Interactions.**

- **Tension with O-BP2 (four compressions as one hierarchy).** Both are unifying framings but may posit different master objectives (IB vs. VFE). Worth scoping both together before committing to either.
- **Related to O-BP5 (orient cascade as recursive AAD).** Variational framing naturally supports nested inner-outer cycles.
- Orthogonal to G-BP1 (natural parameters) and G-BP3 (Fisher information).

**Effort shape.** Scoping spike essential — the variational framing has several specific forms and the choice matters. A 90–120 minute spike can identify the cleanest form. Execution is multi-session (touches the central strategic objective and its downstream consumers).

**Risks.** Active inference has commitments (priors-as-preferences, free-energy-as-surprise-plus-KL) that may not fit AAD's current formulation. Adopting a watered-down variational framing without those commitments requires care. Could blur the $M_t$ / $\Sigma_t$ boundary in ways that complicate rather than clarify.

**Status:** unexamined.

---

## G-BP3 — Fisher-information unification of tempo and gain

**Source:** Gemini bigger-picture §3 (2026-04-22).

**Thesis.** Define mismatch $\delta$ in terms of KL-divergence between model and reality. Then the sector condition and update gain collapse into a single concept: natural gradient descent. Tempo $\mathcal{T}$ becomes the projection of the environment's drift rate onto the agent's Fisher information manifold — not a heuristic scalar. Per-dimension persistence becomes the anisotropic special case of a Riemannian Lyapunov argument. Adaptive tempo, update gain, and sector-condition stability are three faces of one object.

**Merits.**

- **Fundamentality (very high).** Connects AAD to information geometry (Amari) in a way the current scalar treatment cannot. Makes the theory's tempo/gain machinery derivable from a single geometric structure rather than built up from independent scalars.
- **Concision (high).** Eliminates separate $\alpha$, $\eta^\ast$, $\mathcal{T}$ as independent theoretical objects; they become projections of a single Fisher-information object onto different quantities.
- **Beauty (high).** Natural gradient is one of the aesthetically strong moves in machine learning theory; adopting it gives AAD a cleaner core.
- **Correctness (medium).** May resolve edge cases in `#per-dimension-persistence` where scalar tempo overestimates by 72% (track-b Variant F finding); anisotropic treatment becomes natural rather than special.

**Scope.** Essentially all of Section I: `#adaptive-tempo`, `#update-gain`, `#gain-sector-bridge`, `#persistence-condition`, `#mismatch-signal`, `#mismatch-decomposition`, `#per-dimension-persistence`, `#sector-condition-derivation`. Bridge-lemma instantiations in Section III may need re-derivation. The sector-persistence template stays but becomes Riemannian rather than Euclidean.

**Findings subsumed.**

- None directly. This move is motivated by beauty/concision/fundamentality, not by any current finding.
- Indirectly strengthens per-dimension-persistence honesty.

**Interactions.**

- **Strong synergy with G-BP1 (natural parameters).** Natural parameters + Fisher metric → natural gradient. G-BP1 is the parameter-space move; G-BP3 is the geometric metric move; they compose.
- **Strong synergy with O-BP1 (template as organizing principle).** A Riemannian template is cleaner than the current Euclidean one when the state space is naturally probabilistic.
- **Synergy with O-BP3 (continuous-parameter tiering).** Fisher information suggests continuous parameter spaces for L0/L1/L2 correlation depths.
- Neutral toward G-BP2, O-BP2.

**Effort shape.** Major rewrite of Section I. Multi-session. Scoping spike essential — this is the largest single proposal in the portfolio and needs a careful scope analysis before any execution. The spike should answer: does the natural-gradient form genuinely generalize Section III's bridge lemma, or break it?

**Risks.** Readability — information geometry is unfamiliar to control-theory readers, who are a natural audience for AAD. The current linear-ODE pedagogical scaffold becomes harder to present without the Fisher structure upfront. Natural-gradient-based persistence proofs are technically more involved. The payoff (beauty, concision, fundamentality) is real but depends on the exposition being approachable, which is non-trivial.

**Status:** unexamined.

---

## O-BP1 — Sector-persistence template as organizing principle

**Source:** Opus bigger-picture §1 (2026-04-22).

**Thesis.** `#sector-persistence-template` is already factored out, but its role is undersold. Read through the template's lens: Section I is the template applied to $\delta$ with environmental $\rho$; strategy persistence is the template with plan-confidence error and strategic disturbance; team persistence, composition closure, tempo composition, adversarial destabilization are all instantiations with different effective-disturbance decompositions. The distinctive content of each segment is *how it characterizes $\rho_{\text{eff}}$*; the persistence conclusion is mechanical. Reframe the OUTLINE preamble: **AAD is the theory of how to decompose disturbance for bounded-correction dynamics at each scale.** Promote this framing to organizing principle.

**Merits.**

- **Approachability (very high).** A single organizing principle replaces six-plus separately-motivated Lyapunov arguments. The theory has one result (bounded correction + bounded disturbance → bounded mismatch); the segments differ only in how they account for effective disturbance.
- **Beauty (high).** Reveals what the theory actually is, rather than presenting it as a pile of instantiations.
- **Concision (high).** The content is already there; only the presentation compresses.
- **Fundamentality (medium).** Reframing, not new content. But the reframing makes the template's role visible as the *derivation generator*, not just one of many derived results.

**Scope.** `01-aad-core/OUTLINE.md` preamble (rewrite around disturbance decomposition). Section I, II, III preambles get refreshed framing. Small touch on `#temporal-optimality` (TST postulate) — becomes "the scarce resource is correction capacity relative to effective disturbance." No segment edits required; purely editorial.

**Findings subsumed.**

- **Opus Finding 3** (Section II preamble framing). If the whole theory is reframed around disturbance decomposition at scales, "Class 2 is a scope exit from Section II" becomes "Class 2 is one more scale with a coupled update rule; the template still applies with the coupled formulation."

**Interactions.**

- **Strong with O-BP5 (orient cascade as recursive AAD).** Both are "one pattern recurring at every scale" arguments. They converge on recursion as the theory's shape.
- **Strong with G-BP3 (Fisher unification).** If the template becomes Riemannian, the organizing principle becomes even sharper.
- Neutral toward others.

**Effort shape.** Framing touch. 1–2 focused sessions. No scoping spike needed because the content exists; only the presentation is new.

**Risks.** Low. The worst case is a preamble that overstates the simplicity of the theory — but since the template is already factored and the content is already in the segments, that risk is small. Review the preamble carefully against `#sector-persistence-template` to ensure it doesn't overclaim.

**Status:** unexamined (but the underlying `#sector-persistence-template` segment exists and is claims-verified-adjacent).

---

## O-BP2 — Four compression operations as one hierarchy

**Source:** Opus bigger-picture §2 (2026-04-22).

**Thesis.** An agent is a collection of compression maps over its causal history, each tuned to a different relevance variable: prediction ($M_t$), guidance ($\Sigma_t$), coordination (shared intent), abstraction ($\Lambda$). $M_t$ and $\Sigma_t$ are not two distinct *objects* but two *projections* of the same source with different relevance variables. Under this view: no boundary between $M_t$ and $\Sigma_t$ needs policing (L1 augmentation is a different rate-distortion operating point, not ontology shift); Class 2 agents are natural (an LLM's forward pass is one compression producing all four projections simultaneously); modularity is the special case of disjoint sub-graphs.

**Merits.**

- **Fundamentality (high).** Unifies the four substates as one family, grounded in information-theoretic compression.
- **Approachability (high).** One ontological picture ("agent as compression portfolio") replaces four separate objects.
- **Beauty (high).** Aesthetically strong; aligns with the "agent as predictor with objectives" lineage (Clark, Friston, etc.) without requiring their full machinery.
- **Correctness (medium).** May repair the $M_t$/$\Sigma_t$ boundary question during L1 augmentation (where does $\Sigma_t$ absorb environmental common causes? Answer: it's a different relevance variable, not a different object).

**Scope.** `#compression-operations` (extended from U-medium to U-strong), `#agent-model`, `#strategy-dimension`, `#shared-intent`. Possibly absorbs the existing tier-C "$G_t$ as single object" proposal. Effect on `#information-bottleneck` status (see G-BP2). Scope for further absorption: projection admissibility (P1) in `#composition-closure` becomes a fifth compression, with its own relevance variable.

**Findings subsumed.**

- **Opus Finding 4** (IB status mismatch). If IB is the shared shape of four compression operations, the "discussion-grade" label becomes "exact formulation (external theorem)" naturally.
- **Existing tier-C "$G_t$ as single object; $(O_t, \Sigma_t)$ as a property."** O-BP2 strengthens and generalizes the motivation for this move — the relevance-variable framing gives $G_t$ the specific reason for being a single object (one projection with a particular relevance variable).

**Interactions.**

- **Tension with G-BP2 (variational IB reframing).** Both are unifying framings but posit different master objectives (IB vs. VFE). Worth scoping together.
- **Strong with the tier-C "$G_t$ as single object."** Converges.
- **Related to O-BP5 (orient cascade as recursive AAD).** Both support the "theory is recursive at every scale" reading.

**Effort shape.** Scoping spike valuable to identify the cleanest form before touching segments. Substantial if adopted (touches foundational ontology). Multi-session.

**Risks.** May blur useful distinctions. $M_t$ and $\Sigma_t$ currently have well-understood separate dynamics (epistemic update vs. strategy revision); unifying them might lose the specificity that makes those dynamics tractable. Requires careful treatment of what separates the compressions (relevance variables, update rules, storage structure) versus what unifies them (shared source, shared rate-distortion form).

**Status:** unexamined.

---

## O-BP3 — Continuous-parameter approximation tiering

**Source:** Opus bigger-picture §3 (2026-04-22).

**Thesis.** L0/L1/L2 (correlation), C1/C2/C3 (value convention), Tier 1/2/3 (bridge-lemma contraction) are three instances of the same meta-pattern: rate-distortion operating points with monotonicity to finer resolutions and an ascension diagnostic. Rather than three discrete-label hierarchies, treat each as a continuous parameter (correlation depth $\lambda \in [0, 1]$; replanning horizon $N_r \in [1, \infty]$; contraction tightness $\mu \in [0, 1]$). AAD results then live at a point in a 3D operating-regime space with monotonicity along each axis. Closer to information geometry than to the current enumerative treatment.

**Merits.**

- **Fundamentality (medium-high).** Converges on information geometry; treats approximation as a continuous rather than discrete choice.
- **Beauty (high).** Smooth parameter family instead of enumerated labels.
- **Concision (high).** Dissolves ad-hoc labels across three hierarchies.
- **Approachability (medium).** May become more technical rather than less — continuous parameterization is powerful but adds mathematical weight.

**Scope.** `#value-object` (C1–C3 becomes $N_r$ family), `#strategy-dag` (L0–L2 becomes correlation depth), `#composition-closure` (Tier 1–3 becomes contraction tightness), `#approximation-tiering` (meta-segment restated). Downstream: all segments that reference specific tier labels get restated in parameter form.

**Findings subsumed.**

- **Existing tier-C "continuous convention hierarchy."** Direct — this is the generalization.
- **Opus Finding 5 (step 4c convergence)** partial. If L0→L1 is a continuous parameter, the escalation is smooth rather than triggered; the step-4c convergence-required-to-trigger framing may dissolve.

**Interactions.**

- **Strong with G-BP3 (Fisher information).** Natural parameter spaces are continuous by construction; Fisher metric gives the geometry for smooth tiering.
- **Reinforces O-BP1.** Template + continuous parameterization = smooth family of persistence results.
- Neutral toward others.

**Effort shape.** Scoping spike first. Substantial if adopted (touches three hierarchies plus their instantiating segments). Multi-session.

**Risks.** Loss of clean discrete labels that are useful for engineering decisions ("agent is at L1," "using C2 evaluation"). May be cleaner to keep the labels for engineering intuition while showing they are points on a continuum. The scoping spike's primary job is deciding whether to fully continuize or to add a parameter layer atop existing labels.

**Status:** unexamined.

---

## O-BP4 — Continuous-valued strategy DAG

**Source:** Opus bigger-picture §4 (2026-04-22).

**Thesis.** The strategy DAG has AND/OR nodes and binary-success edges, scoped in `#and-or-scope` to binary outcomes. But most real strategic progress is continuous: "approach target," "reduce defect rate," "close the gap." Continuous extension: edges carry expected-progress rates; nodes aggregate progress fields; terminal satisfaction is a continuous threshold. Status propagation in the Boolean case is multiplicative; in the continuous case it is additive-convex or tropical-semiring depending on the combination rule. Dissolves the "operational threshold for continuous objectives" hack; handles L1 soft-facilitator natively as graded parent influences.

**Merits.**

- **Correctness (high).** Resolves the continuous-objective hack in `#strategy-dag`; handles L1 soft-facilitator as a native feature rather than a stretched extension of the Boolean machinery.
- **Approachability (medium).** Real strategic progress is continuous, not binary. Chess, navigation, financial planning — none is naturally AND/OR.
- **Fundamentality (medium).** Extends theory to new domains.
- **Beauty (medium).** Depends on whether the continuous formulation preserves the parsimony of AND/OR. Uncertain until scoped.

**Scope.** `#strategy-dag`, `#and-or-scope`, `#strategic-dynamics-derivation`, `#strategy-persistence-schema`, `#credit-assignment-boundary`, `#worked-example-L1`. Essentially rewrites the strategy layer.

**Findings subsumed.**

- **Partial Gemini Finding 1** (unbounded gradient). If the strategy is continuous, log-odds parameterization is the obvious choice and the domain-escape problem is structural.
- **Tier-C L1 soft-facilitator gap** (recently resolved for strict-prerequisite case; continuous formulation handles soft case natively).

**Interactions.**

- **Strong with G-BP1 (logit reparameterization).** Natural partner — if the DAG is continuous, log-odds is the parameterization. The two proposals almost demand being done together.
- **Some tension with O-BP2 (four compressions).** Continuous $\Sigma_t$ may require different compression formulation (value-based rather than structure-based).
- **Strong with G-BP2 (variational free energy).** Continuous policies are naturally variational.

**Effort shape.** Substantial rewrite. Scoping spike essential — and this proposal probably wants a *dedicated* spike (similar to `msc/spike-composition-scaling-N.md`), not just an evaluation in this portfolio.

**Risks.** AND/OR has been convergent across three independent formalism attempts (noted in `#and-or-scope`) — there's a real reason for it, and a continuous form may not have the same parsimony properties. The scoping spike must genuinely test whether the continuous form is as clean as the Boolean one, not just whether it handles more cases.

**Status:** unexamined. **Recommended next step:** dedicated scoping spike before any portfolio decision.

---

## O-BP5 — Orient cascade as recursive adaptive cycle

**Source:** Opus bigger-picture §5 (2026-04-22).

**Thesis.** Steps 1–5 of the orient cascade consume prior outputs, produce diagnostic signals, and trigger structural adaptation when parameters cannot close the gap. This is an adaptive cycle operating over the agent's *internal* state (diagnostics), nested inside the outer cycle over external state (reality). Deliberation in `#exploit-explore-deliberate` is already described as "internal exploration in model-space"; together with the cascade this suggests the agent's reasoning process is a miniature AAD system whose environment is its own model-state. Formalize a recursive framing: **AAD applies at every level where a state variable has a correction function and bounded disturbance.** Composition-consistency already asserts AAD's scale-invariance; making the inner-cycle recursion explicit would unify deliberation, orient cascade, and composition.

**Merits.**

- **Beauty (medium-high).** Unifies three currently separate mechanisms under one recursive pattern.
- **Fundamentality (medium).** Makes composition-consistency truly recursive rather than merely scale-invariant.
- **Approachability (medium).** A recursive structure can be clearer than three parallel mechanisms, if presented well.
- **Concision (medium).** One mechanism does the work of three.

**Scope.** `#orient-cascade`, `#composition-consistency`, `#exploit-explore-deliberate`. Possible new meta-segment for recursion principle. Related: `#agent-identity` (agent's reasoning is its own trajectory).

**Findings subsumed.**

- None directly. Strengthens existing structural claims (composition-consistency becomes more foundational).

**Interactions.**

- **Strong with O-BP1 (template as organizing principle).** Both are "one pattern at every scale" moves. Together they're the natural shape: *AAD is recursion of the persistence template across scales.*
- **Strong with O-BP6 (identity as load-bearing).** Identity grounds which levels count as adaptive systems; recursion makes the cross-level structure explicit.
- Related to O-BP2 (compressions-as-projections) — the four compressions can themselves be viewed as inner-cycle machinery.

**Effort shape.** Scoping spike likely needed; multi-session to execute fully. Introducing recursion-in-the-theory-itself requires care to avoid confusion.

**Risks.** Recursion-in-theory-itself can get confusing for readers. May not materially change any results — only reframe existing structure. The test of whether the move is worth it: does the recursive formulation clarify any currently-murky distinction (e.g., when deliberation graduates into structural adaptation), or only restate?

**Status:** unexamined.

---

## O-BP6 — Identity promotion (`#agent-identity` to formal scope statement)

**Source:** Opus bigger-picture §6 (2026-04-22).

**Thesis.** `#agent-identity` is currently `discussion-grade` but establishes something formally consequential: sufficiency is defined relative to a *singular causal trajectory*. A duplicated $M_t$ is not sufficient for either copy's trajectory; merging divergent models is lossy; continuity is what gives the sufficient statistic its meaning. Promote to a formal scope statement: **AAD applies to agents instantiated on singular causal trajectories.** This may be load-bearing in ways not currently made explicit — for example, the reason Level 2 data from the feedback loop is *interventional* is precisely because the loop is a singular causal trajectory; replaying is not intervening.

**Merits.**

- **Fundamentality (medium-high).** Clarifies what AAD assumes about the agent's ontological status. Identity-on-singular-trajectories is a clean scope claim with philosophical heft.
- **Correctness (medium).** May strengthen the loop-interventional-access claim (Codex Finding 2 territory) by providing the missing ontological ground for calling the loop "interventional."
- **Approachability (low–medium).** The content is philosophical; presenting it rigorously without drifting into metaphysics is the challenge.

**Scope.** `#agent-identity` (promoted from discussion-grade to formal scope statement). Cross-references added in `#loop-interventional-access` (ground for interventional interpretation), `#chronica` (singular sequence), `#model-sufficiency` (sufficiency-relative-to-trajectory). Relevant for `04-logozoetic-agents/` (identity central there).

**Findings subsumed.**

- None directly. Strengthens Codex Finding 2 (loop framing) by providing the ontological ground that makes Level 2 interventional access honest — without that ground, the loop gives interventional-like data but not interventional access; with it, the trajectory's singular causal structure is what makes the agent's actions genuine interventions.

**Interactions.**

- **Strong with O-BP5 (recursive AAD).** Identity grounds which levels count as adaptive systems on trajectories.
- **Strong with logozoetic work.** Identity is a qualifying property for logozoetic agents.
- Neutral toward others.

**Effort shape.** Small. One focused session: promote the segment, add cross-references in 2–3 downstream segments. No scoping spike needed — the content is already in `#agent-identity`, just marked as discussion.

**Risks.** Low, but touches philosophical territory. The promotion must preserve the segment's current epistemic honesty (it's a claim about what AAD presumes, not a metaphysical commitment).

**Status:** unexamined.

---

## O-BP7 — Known structural absences (meta-proposal)

**Source:** Opus bigger-picture §7 (2026-04-22).

**Thesis.** Not a single proposal but a list of four structural absences in the current theory, each a candidate for future work. These are not findings (the theory doesn't *claim* these things and then fail to deliver); they are gaps between the theory's current scope and the scope a fully worked-out AAD would have. Treating them as a meta-proposal rather than individually lets them sit as a research agenda.

**Absences:**

1. **Tier-switching policy.** When should the agent move from L0 to L1? C1 to C2? Tier 3 to Tier 1? `#approximation-tiering` enumerates the patterns but does not derive the switching policy. The natural target for applying AAD's own cost-benefit machinery to itself: the tier-switch decision is itself a deliberation-cost problem.

2. **Misspecification cost quantification.** `#structural-adaptation-necessity` says *when* to switch model classes; nothing quantifies the *continuous degradation* from a mildly misspecified model. Adjacent to `#observation-ambiguity-modulation`'s $\kappa \cdot \mathcal{A}$ bound but not covered by it.

3. **Cross-hierarchy monotonicity.** The three tierings (L0/L1/L2, C1/C2/C3, Tier 1/2/3) interact — does L0→L1 change the C1/C2/C3 ordering? `#approximation-tiering` flags this; no segment addresses it.

4. **CIY / EIG gap.** The exploration objective uses Causal Information Yield as a surrogate for expected information gain. The honest substitution is unresolved.

**Merits (collectively).**

- **Fundamentality (medium).** Each absence, if addressed, would deepen the theory.
- **Correctness (medium).** Tier-switching and misspecification cost quantification would close genuine gaps.

**Scope.** Each absence has its own scope. Tier-switching touches `#approximation-tiering`, `#deliberation-cost`. Misspecification touches `#structural-adaptation-necessity`, `#observation-ambiguity-modulation`. Cross-hierarchy monotonicity is `#approximation-tiering` meta-work. CIY/EIG touches `#causal-information-yield`.

**Findings subsumed.** None.

**Interactions.**

- Tier-switching relates to O-BP3 (continuous tiering — parameter-switching becomes parameter-tracking).
- Misspecification relates to G-BP2 (variational — KL-based misspecification cost is natural there).
- Cross-hierarchy monotonicity relates to O-BP3.
- CIY/EIG relates to G-BP2 (variational handling of exploration objectives).

**Effort shape.** Each absence is a candidate for a dedicated scoping spike. Collectively: long-term research agenda.

**Risks.** Treating these as a single proposal risks them getting treated as one big thing; treating them as four separate proposals clutters the portfolio. Current compromise: documented as a meta-proposal with explicit sub-items, so they're findable and trackable without crowding the other proposals.

**Status:** all four absences: unexamined. Each may deserve its own scoping spike over the long term.

---

## Cross-proposal interaction summary

The strongest inter-proposal couplings, for planning purposes:

- **G-BP1 + G-BP3 + O-BP3 form a cluster** (natural parameters + Fisher geometry + continuous tiering). Doing one without the others is possible but less cohesive. All three together would be a major unification pass.
- **G-BP1 + O-BP4 form a cluster** (logit parameterization + continuous strategy DAG). These almost demand being done together.
- **G-BP2 + O-BP2 are alternatives** (variational vs. IB-as-shared-shape). Picking one affects the other.
- **O-BP1 + O-BP5 + O-BP6 form a cluster** (template as principle + recursion + identity). Together they articulate the theory as "recursive persistence template applied on singular trajectories at every scale."

## Ordering suggestions

From smallest-payoff-to-effort to largest, rough ordering for planning:

1. **O-BP1 (template as organizing principle)** — framing touch, high payoff, low risk. Natural first move.
2. **O-BP6 (identity promotion)** — one session, localized. Good second move.
3. **G-BP1 (logit reparameterization)** — fixes a real finding, groundwork in spike. 2–3 sessions. Third.
4. **G-BP2 (variational reframing)** — fixes a real finding, requires scoping. Possible fourth, or parallel to G-BP1.
5. **O-BP3 (continuous tiering)** — requires scoping, multi-session execution.
6. **O-BP2 (compressions-as-projections)** — requires scoping, substantial.
7. **O-BP5 (recursive AAD)** — requires scoping, substantial; natural after O-BP1.
8. **O-BP4 (continuous strategy DAG)** — requires dedicated spike before any portfolio decision.
9. **G-BP3 (Fisher unification)** — largest single move; requires the most careful scoping.
10. **O-BP7 (structural absences)** — research agenda; individual scoping spikes over time.

This ordering is a sketch, not a commitment. Decisions about which proposals to scope or execute are Joseph's, tracked in `TODO.md`.
