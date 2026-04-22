# Architectural Proposals — 2026-04-22

**Status:** Working document. Fourteen architectural proposals surfaced across the four de novo audits of 2026-04-22 (Gemini, Codex round-1, Opus, Codex round-2). Each is documented here as an *independent architectural investment option*, evaluated on its own merits — not as machinery for subsuming local findings.

**Execution status (2026-04-22 strengthening cycle, post-AI-integration):**

- **G-BP2 V-medium — EXECUTED** (commit `a14682e`). Variational form of the strategy IB objective: KL-divergence to the optimal-policy posterior replaces Shannon-MI relevance term in `#strategy-complexity-cost`, with cross-references in `#compression-operations`, `#exploit-explore-deliberate`, `#ciy-unified-objective`. Closes Gemini Findings 2 (Shannon-zero degeneracy) and 3. **V-strong remains open** as a paper-writing-time decision per `msc/spike-active-inference-vs-aad.md` §I action 5 — V-medium does not preclude either V-strong or V-weak; both options stay open.
- **O-BP2 partially executed.** The synthesis-segment route landed in 2026-04-21 (`#compression-operations`); the §H Overlap-2 honest credit landed in commit `a14682e`. Full four-segment rewrite remains open per `msc/spike-ib-unification-plan.md`.
- **AI engagement at the segment level — EXECUTED** for the §H Underclaim 1+2+3 positioning moves and §H Overlap 1+2 honest credits (commit `a14682e`). See `msc/spike-active-inference-vs-aad.md` §I and `msc/spike-ai-integration-pass.md` for the per-segment proposed text.
- All other proposals (G-BP1, G-BP3, O-BP1, O-BP3, O-BP4, O-BP5, O-BP6, O-BP7, C-BP1, C-BP2, C-BP3, C-BP4) remain in the original characterization below; see `TODO.md` for current status and recommended ordering.

**Identifier conventions:** G-BP = Gemini bigger-picture; O-BP = Opus bigger-picture; C-BP = Codex round-2 bigger-picture. Codex round-1 did not have a bigger-picture section.

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

## C-BP1 — Three-layer epistemic separation: defined / causally valid / operationally extractable

**Source:** Codex round-2 audit bigger-picture §1 (2026-04-22).

**Thesis.** Most of AAD's live frictions are not raw contradictions; they are places where three distinct epistemic layers get collapsed: (1) **defined** — the formal object exists and is well-typed; (2) **causally valid** — the definition is grounded in reality and supports the causal claims made about it; (3) **operationally extractable** — a real agent can actually compute the quantity at runtime. Segments frequently assert one layer and readers silently import the other two. Codex Finding 12 is the clearest instance: `section-ii-survival.md`'s "16 survive exactly" is a *defined*-layer claim that readers take as *operationally extractable*, and only three documents deep does the survival analysis distinguish them.

**Merits.**

- **Approachability (high).** Makes segments' actual assertions unambiguous to readers.
- **Correctness (medium).** Prevents over-promotion of formal claims to operational claims — a systematic failure mode the repo has repeatedly fallen into (Findings 12 and 14 this round; Finding 9 prior round).
- **Fundamentality (medium).** Not a new mathematical object, but a crisp epistemic framework for what segments can and cannot claim.
- **Concision (medium).** Replaces ad-hoc "this is defined but not computable" caveats with a shared convention.

**Scope.** Meta-level change touching: (a) `FORMAT.md` conventions (see C-BP4 for the mechanical implementation), (b) systematic pass across segments to apply the three-layer convention, (c) affected segments' Epistemic Status blocks.

**Findings subsumed.**

- **Finding 12** (Section II survival slides from statement-level to operational) — direct.
- **Partial Finding 14** (developer-as-act-agent exact-status mismatch) — the segment's status collapse is an instance of layer-collapse; separating layers makes the mismatch visible.
- **Partial Finding 9** (Section II preamble framing) — the preamble's slippage between "exact scope" and "operational applicability" is another layer-collapse.
- Makes other scope-mismatch findings easier to spot and repair.

**Interactions.**

- **Strong with C-BP4** (claim-level epistemic statuses). C-BP1 is the conceptual framework; C-BP4 is the mechanical implementation. Adopting one without the other is possible but half-measures.
- **Supports C-BP2** (master separability pattern). The separability/repair pattern fits within the three-layer framework naturally: separability is about when a definition remains causally valid; the repair is about when the definition becomes operationally extractable in practice.
- **Supports G-BP2** (variational framing): the variational objective explicitly bounds operational extractability by representational complexity, which is the three-layer framework applied to strategy.

**Effort shape.** Convention change plus multi-session application pass. Scoping spike worthwhile — the spike should identify the cleanest way to label the three layers without cluttering every Epistemic Status block, and should pilot on 2–3 segments where layer-collapse is acute (Finding 12 and 14 segments are obvious candidates).

**Risks.** Could become a convention-bureaucracy move if overspecified. Segments that genuinely only make one of the three kinds of claim (e.g., a pure definition with no causal-validity or operational claims) should not be forced to produce empty labels for the other two. The spike must establish the "when a layer doesn't apply, say so once or omit" convention up front.

**Status:** unexamined.

---

## C-BP2 — Master separability pattern as explicit organizing principle

**Source:** Codex round-2 audit bigger-picture §2 (2026-04-22).

**Thesis.** A lot of AAD already runs on one master pattern: **exact core under a separability assumption; structured repair when separability fails; general case expensive or open.** L0 / L1 / L1' / L2 (correlation hierarchy) is one instance. Class 1 / Class 2 / Class 3 (directed separation topology) is another. Tier 1 / Tier 2 / Tier 3 (bridge-lemma contraction) is another. C1 / C2 / C3 (value convention) is a fourth. Making the master pattern explicit — as a meta-segment or OUTLINE-level organizing principle — would reveal that AAD is a single theoretical posture (name the clean case, name the failure mode, name the repair, name what remains open) applied to several structurally distinct state-spaces.

**Merits.**

- **Approachability (very high).** Single organizing pattern replaces four parallel hierarchies each presented with its own specific language. Readers who learn the pattern once can navigate any instance.
- **Beauty (high).** Reveals shared structure. This is the naming-what-was-implicit move that strong theories eventually make.
- **Concision (high).** The pattern itself is short; each instance becomes an instantiation rather than a freshly-motivated architecture.
- **Fundamentality (medium).** Reframing rather than new derivation; but the reframing shifts AAD's identity from "a control theory with many tierings" to "a theoretical posture for managing separability and its failure."

**Scope.** New meta-segment (or substantial preamble addition) stating the master pattern and enumerating the current instances. Small per-segment touches to align each instance's framing with the master pattern's vocabulary.

**Findings subsumed.**

- Not directly. Strengthens several findings' repairs by providing shared framing. Finding 13's "L1 is the default but only for strict-prerequisite; L1' for soft" becomes a direct instance of the master pattern ("L0 is the separable case; L1 is the repair for strict-prerequisite non-separability; L1' is the repair for soft-facilitator non-separability; full L2 is expensive/open").

**Interactions.**

- **Strong with O-BP1** (template as organizing principle). O-BP1 names the *result-level* organizing principle (sector-persistence template); C-BP2 names the *epistemic-posture-level* organizing principle (separability → repair → open). They compose: the theory has one result (persistence template) applied under one posture (separability management) across multiple state spaces.
- **Strong with O-BP3** (continuous-parameter tiering). If the tierings become continuous parameters (O-BP3), C-BP2 still holds as the conceptual framework — each continuous parameter indexes the separability-to-repair path.
- **Supports C-BP1** (three-layer separation). Both are epistemic-posture moves; they are complementary conventions rather than competitors.

**Effort shape.** 1–2 sessions for the meta-segment; framing touches across the four hierarchy-instantiating segments. No scoping spike needed — the content is already there; only the explicit naming is new.

**Risks.** Low. Could be dismissed as "just naming the obvious," but naming the obvious is what lets readers transfer understanding across instances. Main risk: the naming becomes a *rigid* convention and segments start contorting to fit the master-pattern template rather than stating themselves naturally.

**Status:** unexamined.

---

## C-BP3 — Software as calibration laboratory, not universal exemplar

**Source:** Codex round-2 audit bigger-picture §3 (2026-04-22).

**Thesis.** TST's current positioning ("richest operationalization domain") overclaims. The tighter and more defensible claim is: **software is the privileged high-identifiability domain where $\Sigma_t$ edges can sometimes be genuinely interventional** (tests, deploys, git bisect) and where the chronica is partially exteriorized. This makes software a *calibration laboratory* for AAD: the domain where quantitative claims can be grounded, where ambiguity modulation can be measured, where bridge-lemma contraction can be tested against Tier-1 reality. Other domains export the calibrated results under *stronger or additional assumptions*, making the transfer claims explicit rather than left to the reader.

**Merits.**

- **Correctness (high).** Resolves Finding 15 (richest-domain headline) and, more broadly, the rhetorical asymmetry between TST's self-presentation and its actual evidential base.
- **Approachability (high).** A clear "rule for what transfers outward, under which additional assumptions" replaces the current "TST is rich, see if your domain is similar" framing.
- **Concision (high).** Removes the low-grade back-and-forth between "TST is the richest domain" (in headlines) and "TST's claims are scoped to identifiable-edge regimes" (in bodies).
- **Fundamentality (medium).** Repositions TST's role in the framework without changing its content.

**Scope.** `02-tst-core/OUTLINE.md` preamble; `#software-epistemic-properties` headline and scope block; possibly a short new segment or appendix stating the "calibration laboratory + exports under assumptions" framework explicitly. Optional: a "domain-transfer assumptions" table that names the specific additional assumptions needed to export TST's quantitative claims to non-software domains.

**Findings subsumed.**

- **Finding 15** (software richest-domain headline) — direct.
- Partially strengthens Finding 7 / Finding 14 (TST overclaims on git and on developer mapping) — both are made cleaner by positioning TST as calibration-lab-with-domain-limits rather than universal-exemplar.

**Interactions.**

- **Strong with C-BP1** (three-layer separation). Software is where the three layers can all be established; other domains export to those layers under additional assumptions.
- **Neutral** toward others.

**Effort shape.** 45–90 min. Mostly editorial reframing; does not require new theory. A brief scoping pass to identify which TST claims are "calibration-laboratory grade" (software-native) vs. "domain-transfer grade" (exports under assumptions) would tighten execution.

**Risks.** Low. Could feel like a demotion of TST's ambition — but the repositioning actually *strengthens* TST's claims by making them defensible and transferable rather than unbounded.

**Status:** unexamined.

---

## C-BP4 — Claim-level epistemic statuses

**Source:** Codex round-2 audit bigger-picture §4 (2026-04-22).

**Thesis.** Move from segment-level `status:` tags to **claim-level** statuses. A single segment often makes three different kinds of claim — the definitional core (what's being defined), the transfer result (how it connects to other segments / domains), and the operationalization layer (how to measure or compute it) — each with different epistemic strength. Current segment-level tags force an umbrella label that over-promotes the weakest claim or under-sells the strongest. Claim-level statuses (already partially supported via equation-level tags per FORMAT.md) would be promoted to a first-class convention: segments explicitly label each load-bearing claim with its own status.

**Merits.**

- **Approachability (medium-high).** Readers can see at a glance which parts of a segment are *exact*, which are *robust-qualitative*, which are *discussion-grade*, rather than reading an umbrella tag that obscures the mix.
- **Correctness (medium).** Directly addresses Finding 14 (the `exact` tag on developer-as-act-agent forced over-promotion across distinct regimes) and prevents similar failures.
- **Concision (medium).** The extra labels are offset by the removal of apologetic "this claim is X but this other claim is Y" prose.
- **Fundamentality (low).** A workflow/convention change, not a theoretical move.

**Scope.** `FORMAT.md` convention addition. Equation-level tags already exist (`*[Definition]*`, `*[Derived]*`, `*[Hypothesis]*`, etc.); the move here is to extend them with explicit status qualifiers (`*[Derived, status: exact]*`, `*[Formulation, status: conditional]*`). Then a systematic pass across segments to apply the new convention to load-bearing claims. Segment frontmatter `status:` retains a meaning as the "weakest load-bearing claim's status" or similar aggregate — or is dropped entirely.

**Findings subsumed.**

- **Partial Finding 14** (developer-as-act-agent status mismatch) — direct; the segment's "exact" umbrella fails precisely because it forces one label across claims of different strengths.
- **Partial Finding 10** (IB status mismatch with unification role) — also a single-label-forced-to-cover-multiple-claims problem.

**Interactions.**

- **Strong with C-BP1** (three-layer separation). C-BP1 is the conceptual framework (defined / causally valid / operationally extractable); C-BP4 is the mechanical implementation (each layer's claim carries its own status). Both adopted together gives a clean convention; C-BP1 alone is philosophy without enforcement; C-BP4 alone is bureaucracy without purpose.
- **Neutral** toward others.

**Effort shape.** Small convention change in FORMAT.md. Application pass across segments is multi-session, but each segment's pass is quick (10–20 min typically). Could be executed incrementally — applied first to the segments where umbrella-status-tags are actively misleading (Finding 14 segments + Finding 10 segment), then propagated as segments are next touched.

**Risks.** Could become a bureaucratic overhead if applied mechanically to segments that make only one load-bearing claim. The convention must include "when only one kind of claim is present, segment-level status suffices" as a first principle.

**Status:** unexamined.

---

## Cross-proposal interaction summary

The strongest inter-proposal couplings, for planning purposes:

- **G-BP1 + G-BP3 + O-BP3 form a cluster** (natural parameters + Fisher geometry + continuous tiering). Doing one without the others is possible but less cohesive. All three together would be a major unification pass.
- **G-BP1 + O-BP4 form a cluster** (logit parameterization + continuous strategy DAG). These almost demand being done together.
- **G-BP2 + O-BP2 are alternatives** (variational vs. IB-as-shared-shape). Picking one affects the other.
- **O-BP1 + O-BP5 + O-BP6 form a cluster** (template as principle + recursion + identity). Together they articulate the theory as "recursive persistence template applied on singular trajectories at every scale."
- **C-BP1 + C-BP4 form a cluster** (three-layer separation as framework + claim-level statuses as implementation). Adopting one without the other is half-measures — C-BP1 alone is philosophy without enforcement; C-BP4 alone is bureaucracy without purpose.
- **C-BP1 + C-BP2 are complementary epistemic-posture moves** (three-layer separation + separability-pattern naming). They share the "name what the theory is already doing, systematically" spirit.
- **O-BP1 + C-BP2 compose** (result-level organizing principle + epistemic-posture organizing principle). Together: "AAD is one persistence result applied under one epistemic posture (separability → repair → open) across multiple state spaces."

## Ordering suggestions

From smallest-payoff-to-effort to largest, rough ordering for planning:

1. **O-BP1 (template as organizing principle)** — framing touch, high payoff, low risk. Natural first move.
2. **O-BP6 (identity promotion)** — one session, localized. Good second move.
3. **C-BP3 (software as calibration laboratory)** — 45–90 min, mostly editorial. Closes Finding 15; strengthens Finding 7/14. Good third.
4. **C-BP2 (master separability pattern)** — 1–2 sessions for meta-segment + framing touches. No new theory. Pairs well with O-BP1.
5. **G-BP1 (logit reparameterization)** — fixes a real finding, groundwork in spike. 2–3 sessions.
6. **G-BP2 (variational reframing)** — fixes a real finding, requires scoping.
7. **C-BP1 + C-BP4 (three-layer separation + claim-level statuses)** — conceptual framework + mechanical convention. Scoping spike worthwhile. Multi-session application but each segment's pass is quick.
8. **O-BP3 (continuous tiering)** — requires scoping, multi-session execution.
9. **O-BP2 (compressions-as-projections)** — requires scoping, substantial.
10. **O-BP5 (recursive AAD)** — requires scoping, substantial; natural after O-BP1.
11. **O-BP4 (continuous strategy DAG)** — requires dedicated spike before any portfolio decision.
12. **G-BP3 (Fisher unification)** — largest single move; requires the most careful scoping.
13. **O-BP7 (structural absences)** — research agenda; individual scoping spikes over time.

This ordering is a sketch, not a commitment. Decisions about which proposals to scope or execute are Joseph's, tracked in `TODO.md`.


---

## Post-strengthening evening additions (2026-04-22)

A second triple-audit cycle (Codex / Gemini / Opus) ran *after* the strengthening cycle had landed. Several of the bigger-picture moves restate or extend proposals already in the portfolio above; the substantive extensions are captured immediately below before the genuinely new proposals (O-BP8 through O-BP16).

### Extensions to existing proposals (from 2026-04-22 evening audits)

**G-BP1 (natural-parameter / logit reparameterization) — Gemini reaffirms with Riemannian framing.**
Gemini's evening-audit bigger-picture §4 reaffirms G-BP1 and adds explicit framing: shifting the strategy DAG update rules entirely into log-odds (natural parameter space) and defining mismatch $\delta$ via KL-divergence collapses sector condition, update gain, and tempo into "natural gradient descent on a Riemannian manifold." This phrasing makes the G-BP1 + G-BP3 cluster's deep unity even more visible than the original characterization: G-BP1 supplies the parameter space, G-BP3 supplies the metric, and together they yield natural gradient descent. Gemini specifically notes this would address the $O(1/n)$ bias observed in the spikes — a concrete defect-driven motivation beyond the original "correctness/concision" merits.

**G-BP3 (Fisher-information unification) — Gemini reaffirms (Riemannian manifold framing).**
Same Gemini §4 — the natural-gradient-on-Riemannian-manifold form is exactly G-BP3's content. The evening-audit framing makes G-BP1 + G-BP3 read as a single move (parameter + metric together) rather than two independent proposals, sharpening the cluster recommendation.

**O-BP2 (four compressions as one hierarchy) — Codex reframes via "predictive relevance under bounded loss"; Gemini explicitly dissolves Class 2 problem.**

- *Codex bigger-picture (evening) §4 phrasing:* "the same projection/compression shape recurs: $M_t$, $\Sigma_t$, shared intent, and macro-projection all preserve predictive relevance under bounded loss. That feels like the deepest available simplification without overclaiming." This adds a precise epistemic-tier qualifier ("without overclaiming") that O-BP2's original characterization lacked — specifically pointing at the U-medium ceiling found in `msc/spike-ib-unification-plan.md`. Codex's framing is consonant with `#compression-operations` already at U-medium and explicitly cautions against the U-strong overreach.
- *Gemini bigger-picture (evening) §2 phrasing:* The strict separation between $M_t$ and $\Sigma_t$ "forces immense complexity (like the L1 common-cause node repair). If an agent is viewed purely as a collection of compression maps over its causal history, $M_t$ and $\Sigma_t$ are not distinct objects, but merely two projections of the same causal source tuned to different relevance variables (prediction vs. guidance). This perspective elegantly dissolves the Class 2 Agent problem: an LLM's forward pass is simply one holistic compression producing both projections simultaneously, making logogenic agents native to the theory rather than a scope-violating exception." Gemini's evening framing adds a major motivation O-BP2's original entry only hinted at: under O-BP2, the Class 2 logogenic-agent scope-exit ceases to be a scope violation and becomes a natural special case (one compression producing all projections at once). This substantially strengthens the case for O-BP2 by promising to dissolve, not just relabel, a long-standing open scope problem.

**O-BP3 (continuous-parameter approximation tiering) — Gemini explicit parameter form.**

Gemini bigger-picture (evening) §1 makes the continuous-parameter form concrete: "treating correlation depth, replanning horizons, and contraction tightness as continuous variables ($\lambda, N_r, \mu \in [0,1]$), the 'tier switches' simply become gradient descent over a rate-distortion tradeoff." This adds (a) explicit parameter naming for what O-BP3 had only schematically described, and (b) the observation that tier-switch *detection* (a known open question in the existing tiered framework) becomes gradient-descent on the parameter space — which would absorb the "tier-switching policy" sub-item of O-BP7.

**C-BP1 (three-layer epistemic separation) — Codex restates with slightly different layer naming.**

Codex bigger-picture (evening): "one explicit three-layer contract for every major claim: `object exists`, `exact theorem transfers`, `quantity is operationally extractable`. Several current seams are really layer-collapses, not mathematical contradictions." Compare to C-BP1's original: defined / causally valid / operationally extractable. The two layer-set choices differ slightly:

- *C-BP1's "defined":* The formal object exists and is well-typed.
- *Codex evening "object exists":* Same content; minor rephrasing.
- *C-BP1's "causally valid":* The definition supports the causal claims made about it.
- *Codex evening "exact theorem transfers":* Subtly different — focuses on whether a downstream theorem applies to the object, rather than whether the object's definition is causally well-grounded. The evening framing is more procedural; C-BP1's is more ontological. Both are defensible; choice between them is a presentational decision that affects whether the layer-separation reads as epistemic-foundations work or as theorem-transfer-checking work.
- *C-BP1's "operationally extractable" / Codex evening's "operationally extractable":* Identical content.

**Recommended absorption:** Update C-BP1's characterization to acknowledge both phrasings as admissible and note the presentational tradeoff. The Codex evening framing is sometimes the more useful one (specifically when the question at hand is "does this segment's downstream theorem apply to its definitional object?"), while C-BP1's original is the more useful one when the question is "is the definition itself causally well-grounded?" Both suggest C-BP4 (claim-level epistemic statuses) as the implementation mechanism.

**C-BP2 (master separability pattern) — Opus expands ladder list and adds the positive-half observation.**

Opus bigger-picture (evening) §B identifies six ladders (not four), all sharing the same "separable-core → structured-repair → general-open" shape:

1. L0/L1/L1'/L2 (correlation)
2. C1/C2/C3 (convention)
3. Class 1/2/3 (architecture, directed-separation topology)
4. Tier 1/2/3 (contraction)
5. **A/B/C (identification regime, from `#edge-update-causal-validity`)** — added by Opus
6. **adaptive / agency / composite (scope hierarchy)** — added by Opus

Opus's additional observation: "The #identifiability-floor segment has named half of this pattern (the no-go half). The positive half is implicit everywhere and named nowhere." C-BP2 + #identifiability-floor would together name both halves of the meta-pattern: positive (separable-core / structured-repair / general-open) and negative (information-theoretic floors that prevent escape from the general-open case).

**Recommended absorption:** Update C-BP2's characterization to (a) list the six ladders rather than four, (b) note the explicit complementarity with `#identifiability-floor`, and (c) flag that the meta-pattern's positive and negative halves together would constitute a stronger organizing principle than either alone.

**O-BP1 (sector-persistence template as organizing principle) — Opus §F adds the composition-as-third-application path.**

Opus bigger-picture (evening) §F observes: "There's a natural move that could pull Section III up: composition closure is the sector-persistence template applied to a projection defect, which is itself a compression operation, which has the same IB shape as $M_t$, $\Sigma_t$, and shared intent ( #compression-operations gets close to this). If the four compressions are unified under one variational problem, and the six persistence results are unified under one Lyapunov template, then composition emerges as a third application of the same machinery rather than new theory."

This identifies an O-BP1 + O-BP2 composition path that the original entries did not articulate: pursued together, they would lift Section III from "promising structure" to "third instance of the same machinery already present in Sections I and II." This is the cleanest available path to the Section-III asymmetry that the OUTLINE preamble currently acknowledges as the theory's main weakness.

**Recommended absorption:** Add a cross-reference in O-BP1 noting the O-BP1 + O-BP2 → Section III pull-up path. Same in O-BP2.

---

The genuinely new proposals (not extensions of existing ones) are listed below.

### O-BP8 — Explicit scope lattice as named-once-and-reused object

**Source:** Codex bigger-picture (2026-04-22 evening).

**Thesis.** AAD's scope is a five-tier lattice: **adaptive → agency → learning-purposeful → exact Section II modular (Class 1) → coupled/logogenic**. Each layer narrows the prior. Currently distributed across `#scope-condition`, `#agent-spectrum`, `#causal-hierarchy-requirement`, `#directed-separation`, and the Section II preamble — a reader has to assemble the full intersection statement themselves. Named once (e.g., as a meta-segment `#section-ii-scope-lattice` or as the canonical scope statement in `#scope-condition`), the lattice serves as a single referent that all downstream segments can invoke.

**Merits.** Approachability (very high), concision (high), correctness (medium — closes the headline-vs-actual-scope friction). Subsumes Finding 16 (Section II scope lattice underspecified). Strengthens the case for several of the existing proposals: O-BP1 (template-as-organizing-principle) acquires a clean scope referent; C-BP1 (three-layer separation) composes naturally because each lattice layer has its own "defined / causally valid / operationally extractable" pattern.

**Effort shape.** Scoping spike worthwhile (1 session) to decide whether to promote a new meta-segment or add a canonical statement to existing segments. Application: 30–60 min for option (a); 1–2 sessions for the meta-segment route.

**Status:** unexamined.

### O-BP9 — Typed admissibility for composition (model-only / goal-bearing / strategy-bearing × Tier)

**Source:** Codex bigger-picture (2026-04-22 evening).

**Thesis.** Replace the blanket "composite agent" with typed admissibility: **model-only composites** (no $G_c$, only $M_c$ and joint dynamics — currently absent from segments), **goal-bearing composites** (with thin $O_c$ but no full $\Sigma_c$ — what (C-iii) actually supplies under positive-sum coupling), **strategy-bearing composites** (full $G_c = (O_c, \Sigma_c)$, currently the only kind the closure framework formally handles). Each crossed with Tier 1/2/3 contraction status.

**Merits.** Correctness (high — closes Finding 8/F8 cleanly by giving (C-iii) a proper destination type that doesn't require full $G_c$). Approachability (medium — adds a partition that has to be learned but resolves ambiguity once internalized). Subsumes Finding 8; partially supports Finding 17 (coupled-diagnostic-framework's M/G decomposition is post-hoc analytical — the typed composition lets goal-bearing composites be the right scope for that diagnostic without forcing the strategy-bearing apparatus).

**Scope.** `#composition-scope-condition` (extends route table), `#composition-closure` (adds typed admissibility before requirements), `#multi-agent-scope` (adds composite-type-distinction). Possibly a new meta-segment `#composition-types`.

**Effort shape.** Scoping spike valuable (1–2 sessions). Substantial editorial pass to reframe `#composition-closure`'s (A1)–(A4) as type-conditional rather than universal.

**Status:** unexamined. Strong companion to G-BP1's typed-admissibility instinct.

### O-BP10 — Projection-contraction framing of the sector-persistence template

**Source:** Opus bigger-picture (2026-04-22 evening), §A.

**Thesis.** Generalize the sector-persistence template to a single organizing slogan: **"An adaptive system is a projection whose contraction rate exceeds its target's drift rate."** Every named defect in AAD is a projection-fidelity measurement: epistemic mismatch is $\Omega$-projected-to-$M$, strategic mismatch is truth-projected-to-edge-credences, closure defect is micro-projected-to-macro, adversarial destabilization is target-projected-to-observable, IB compression cost is history-projected-to-state. The template's $\xi$ is always a projection defect; the disturbance is always the rate at which the projection target shifts faster than the projection can track.

**Merits.** Beauty (high), concision (high — single slogan replaces extensive scaffolding), fundamentality (medium-high — surfaces what AAD actually is at the deepest level). Composes with O-BP1 (template as organizing principle): O-BP1 names the *result-level* organizing principle; O-BP10 names the *object-level* organizing principle. Both compose with C-BP2 (master separability pattern) which names the *epistemic-posture-level* organizing principle.

**Scope.** OUTLINE.md preamble rewrite (replace "AAD" elevator pitch with the projection-contraction form); introductory passage in `#sector-persistence-template`; potentially a top-level naming pass across all defect-named segments.

**Effort shape.** Substantial editorial reframing. 2–3 sessions if comprehensive; 1 session for a preamble + template-segment touch.

**Status:** unexamined. **One of the most concise potential restatements of the entire theory available.**

### O-BP11 — Observability as a master variable across the theory

**Source:** Opus bigger-picture (2026-04-22 evening), §C.

**Thesis.** Observability appears repeatedly as a recurring master variable across distinct AAD machinery, currently presented as separate machinery in each instance. The unifying observation: **every structural AAD move is ultimately about what's observable to whom, at what cost, with what identification strength.** Specific instances:

- L1' refutation under unobservable $C$ (Prop B.7's identifiability obstruction → instance of #identifiability-floor)
- P4 in `#graph-structure-uniqueness` (observable intermediates as a structural property)
- P6 in `#software-epistemic-properties` (agent-controlled $U_o$)
- B.2 vs B.3 in `#strategic-dynamics-derivation` (observable vs unobservable intermediate as the structural pivot)
- `#observability-dominance` (unobservable edges freeze)
- Directed-separation's $\kappa_{\mathrm{processing}}$ (observability of $G_t$ to $f_M$, forbidden in Class 1)
- Loop-interventional-access (observability of causal structure via action-contrast)
- `#shared-intent` (observability of composite $O_c$ to sub-agents)
- TST P6 + code-quality-as-observation-infrastructure (observability of intent to future developers)

A single segment (or reorganization around) **"Observability: what can be seen, by whom, at what cost, with what identification strength"** could re-center the theory. It would subsume parts of `#edge-update-causal-validity` (regime A/B/C), `#observability-dominance`, parts of `#scope-condition`, `#directed-separation`'s $\kappa_{\mathrm{processing}}$, the identifiability-floor instances — all currently presented as distinct machinery.

**Merits.** Fundamentality (very high), concision (high — would subsume many segments' scaffolding into one variable's parameterization), beauty (high). Subsumes parts of Finding 5, F11, and the identifiability-floor segment's adjacency claims. Could be a much larger reorganization than any other proposal in the portfolio if pursued seriously.

**Effort shape.** Substantial. Scoping spike essential; multi-session if pursued in segment form. Probably 4–6 sessions for the full re-centering. **The largest available reorganization.**

**Risks.** Observability is genuinely a master variable, but the current segment-distributed treatment may have advantages (each instance can be reasoned about with its specific dynamics). A premature unification could lose the per-instance specificity that makes the theory tractable. Scoping spike must validate that the unified treatment preserves what's currently usable per-instance.

**Status:** unexamined. **Probably the deepest available structural insight from the audit cycle.**

### O-BP12 — Resource budget $B_t$ as master variable for bounded rationality

**Source:** Opus bigger-picture (2026-04-22 evening), §D.

**Thesis.** Bounded rationality currently appears piecewise: cognitive cost of $\Sigma_t$ (IB/MDL); deliberation cost; update gain's implicit dependence on agent capacity; context window constraints for LLMs; description length limits for strategies. There's no single $B_t$ (budget) variable that the agent allocates across $(M_t, \Sigma_t, O_t)$ maintenance. Introducing one would let you derive — rather than separately postulate — quantities like $d^\ast$, $\eta^\ast$'s dependence on capacity, $\beta_\Sigma$'s calibration, and the compression ratios across the four IB instances.

**Pragmatic form.** A `#resource-budget` segment with $B_t$ as the master variable, from which $\mathrm{DL}(\Sigma_t) + \mathrm{DL}(M_t) + \mathrm{DL}(O_t) \leq B_t$ is a constraint, and the three (or four, with shared intent) compressions are a joint allocation problem.

**Merits.** Fundamentality (medium-high), concision (medium), correctness (medium). Adjacent to O-BP7's known structural absences (specifically the tier-switching policy). Provides a unified frame for the four $\beta$ values currently calibrated independently in `#compression-operations`.

**Effort shape.** Scoping spike valuable (1–2 sessions). 2–3 sessions to execute as a new segment with the joint-allocation derivation.

**Risks.** The unification may over-promise: in practice, the four $\beta$s in compression-operations are calibrated separately because they live in different cognitive sub-systems. A master $B_t$ might be a presentational device rather than a derivation engine.

**Status:** unexamined.

### O-BP13 — Cox-parallel necessity for `#graph-structure-uniqueness`

**Source:** Opus bigger-picture (2026-04-22 evening), §E.

**Thesis.** `#graph-structure-uniqueness` proves sufficiency: P1–P4 + causal sufficiency → DAG with Markov property. The necessity direction is open: any non-DAG structure satisfying P1–P4 + causal sufficiency is isomorphic to a DAG. Reachable via Lauritzen's characterization of Markov properties on different graph classes (factor graphs, junction trees, chain graphs encode different independence relations; the question is whether the specific independence relation forced by P1–P4 + causal sufficiency requires DAG semantics).

**Merits.** Fundamentality (high — elevates from sufficiency-only Cox-analog to full Cox-style theorem). Worth a dedicated spike to assess tractability.

**Effort shape.** Dedicated scoping spike (1–2 sessions). If tractable, 2–3 sessions to derive and integrate.

**Status:** unexamined.

### O-BP14 — Per-segment "what's derived vs. chosen vs. assumed" table convention

**Source:** Opus bigger-picture (2026-04-22 evening), §G(1).

**Thesis.** `#graph-structure-uniqueness` lines 154–165 carry a compact "what's derived vs. chosen vs. assumed" table that is the clearest epistemic signal in the entire repo. A compact version in every derivation-type segment would save future agents (and reviewers) hours of careful reading.

**Merits.** Approachability (very high), correctness (medium — pre-empts the "is X derived or chosen?" ambiguity that fresh readers repeatedly stumble on). Pairs naturally with C-BP4 (claim-level epistemic statuses) — C-BP4 is the inline tagging system; O-BP14 is the segment-level executive summary.

**Scope.** FORMAT.md convention addition (declare the table as a recommended optional section for derivation-type segments). Per-segment application — incremental, low-risk.

**Effort shape.** Convention change in FORMAT.md: 30 min. Per-segment application: ~10 min each, roughly 40 segments touched over time. Total: 1–2 sessions for the convention + first batch of high-value segments (the Section I derivations, B.5–B.7 in `#strategic-dynamics-derivation`, the composition-closure segment).

**Status:** unexamined. **Potentially highest-payoff-to-effort move in this batch.**

### O-BP15 — Comprehensive "minimal proof of viability" worked example

**Source:** Opus bigger-picture (2026-04-22 evening), §G(2).

**Thesis.** Build a single concrete worked example that hits *every* major Section I/II result. Candidate domain: a literal two-service deployment with specified $\rho$, $\mathcal{T}$, $\Sigma_t$ — something a software engineer can run mentally without the formal apparatus. The example threads through `#mismatch-signal`, `#update-gain`, `#adaptive-tempo`, `#sector-condition`, `#satisfaction-gap`, `#control-regret`, `#orient-cascade`, `#strategy-dag`, the L0/L1 calibration, and Prop B.6 + B.7. Crystallizes "this is a theory of real agents, not a formal game."

**Merits.** Approachability (very high), correctness (medium — running the example end-to-end exposes any unspecified parameters or formal gaps), beauty (medium — a single concrete instantiation showing the whole machinery in action). Subsumes nothing directly but removes the friction of fragmentary worked examples (`#worked-example-kalman`, `#worked-example-bandit`, `#worked-example-strategy`, `#worked-example-L1` each demonstrate one slice).

**Scope.** New worked-example segment. Choosing the right domain matters (software is a strong candidate per TST, but the example should demonstrate AAD generality, not just TST). Pre-existing worked examples could be cross-referenced or partially absorbed.

**Effort shape.** Major content effort: 3–4 sessions for the example itself + cross-reference integration. Best done after O-BP1 + O-BP2 framing has stabilized so the example reflects the cleanest theoretical framing.

**Status:** unexamined.

### O-BP16 — Population-level Lyapunov dynamics (Gemini bigger-picture)

**Source:** Gemini bigger-picture (2026-04-22 evening), §3.

**Thesis.** The sector condition successfully proves persistence for individual agents but acts as a behavioral black box at the population level. To complete Section III for multi-agent and composition dynamics, the Lyapunov machinery should be elevated from agent-level to population-level — tracking the *distribution* of correction architectures and endogenous coupling coefficients ($\gamma$) rather than just static bounds. `msc/spike-neutral-drift-lyapunov.md` already noted that the sector condition is blind to "neutral drift" (agents that behave identically now but will fail differently later), which is exactly the population-level missing structure.

**Merits.** Fundamentality (medium-high — closes a known Section III gap), correctness (medium). Maps onto the existing Section III gaps in TODO ("Latent structural diversity," "Endogenous coupling," "Composition transition dynamics") — population-Lyapunov is the apparatus that would let those gaps be addressed coherently rather than as separate ad-hoc extensions.

**Scope.** New segments in Section III. Substantial multi-session work.

**Effort shape.** Major. Scoping spike essential; 4–6 sessions if pursued.

**Status:** unexamined. Adjacent to O-BP7 (structural absences) — could be added there as a fifth absence.

### Closing meta-observation (Opus, §"One closing observation")

> "The framework's honesty is load-bearing… The theory's conservatism is not a limitation — it is the theory's architectural principle."

This is not a proposal but an observation about the project's character. The strengthen-first feedback memory captures part of this; the identifiability-floor segment's structural-impossibility-as-positive-content reframe captures another part. Worth surfacing in the OUTLINE.md preamble or CLAUDE.md "Theory Character" section as an explicit principle: AAD makes its scope and limits visible at the segment level rather than burying them; this is what gives the theory its load-bearing posture against critical scrutiny.

This deserves a small CLAUDE.md addition — not a full proposal but a one-paragraph principle statement under "Theory Character."


---

## Discovered structural patterns (2026-04-22/23 strengthening cycle)

The strengthening cycle ran after the audit-derived proposals above and surfaced a theoretical pattern that was not visible to any single audit. Unlike the G-BP / O-BP / C-BP proposals — which are *choices* about how the theory should be reorganized — this is a *discovery* about what the theory already does across multiple segments. It is documented here as an architectural observation so future work can deploy it deliberately rather than re-discover it.

### SP-1 — The three-layer additive-decomposition pattern

**Source:** 2026-04-22/23 strengthening cycle, surfaced by the F20 regret-bound spike (commit `f70fb68`), the reverse-KL uniqueness spike (commit `e777f01` with corrected citations), and the G-BP1 logit scoping spike (commit `a39dfb7`).

**The pattern.** AAD now carries **three independent uniqueness theorems**, each forcing a logarithmic coordinate through a Cauchy-functional-equation argument on an AAD-internally-motivated additivity axiom:

| Layer | Quantity | Axiom | Forced form | Segment |
|---|---|---|---|---|
| **Chain** | Confidence along causal chains | Additive log-confidence decay | $\log P(	ext{chain}) = \sum_i \log P(E_i \mid E_{\lt i})$ | #chain-confidence-decay |
| **Divergence** | Policy mismatch between $\pi^st$ and $Q_{\Sigma_t}$ | Chain-rule additivity over conditional factorizations | $f(t) = c 