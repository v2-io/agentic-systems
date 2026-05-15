# Cross-Domain Transfer Questions Surfaced by This Work

The framework's *established* cross-domain transfers — Kalman variance-decay
to RL learning-rate annealing, immune somatic hypermutation to continual
learning, adaptive control stability theorems to organizational viability,
Auftragstaktik shared-intent IB compression to multi-agent RL, and dozens
more — live in the curated catalog at
[`msc/FINDINGS-RANKED-DRAFT.md`](FINDINGS-RANKED-DRAFT.md). The catalog's
*Long-Standing Open Questions Now Within Reach* section (~20 entries) is
the canonical list of what AAT's unification claims to touch.

This file is narrower: transfer questions surfaced specifically by the
2026-05-04 domain-unification re-examination cycle — the new four-axis
agent ontology and the [domain-instantiations master list](../doc/DOMAINS.md)
including the TST additions, and what those together reveal that the
existing catalog hasn't yet articulated. Six
questions, each sized as a focused literature-scan + spike rather than a
research program. Each is tagged with its catalog adjacency so the reader
knows whether it's an extension, a sharpening, or genuinely open.

---

## Q1. Static → Learning transition design

**Surfaced by:** Knowledge Type axis (new in the ontology — Static
agents have causal mapping fixed at design time; Learning agents acquire
or refine it online). The Static/Learning distinction is in the ontology
but the *transition design* — when to promote a Static agent to
Learning regime, what triggers the promotion, what stability conditions
the transition itself must satisfy — is not in any current segment.

**Source domain:** Classical adaptive-control literature on Static →
Learning transitions: Ziegler-Nichols auto-tuning, gain scheduling,
Model-Reference Adaptive Control (Astrom-Wittenmark), iterative learning
control. These have decades of theorems on when self-tuning is stable,
what convergence rates apply, and how to handle the bumpless-transfer
problem (switching from Static to Learning controllers without
destabilizing the system).

**Target domain:** RL learning-rate warmup and online adaptation — when
should a fixed-rate Static agent be promoted to a Learning regime, and
what triggers should the promotion respond to?

**AAT bridge:** `#result-structural-adaptation-necessity` (#57 in the
catalog) says when parametric updates fail, structural change is
required. The Static→Learning promotion is precisely a structural
change. The persistence condition $\alpha > \rho/R$ may give the
trigger: when $\rho$ drift exceeds Static $\alpha$, promotion to
Learning is forced.

**Worth checking:** Does classical adaptive-control's Static→Learning
literature give a stability-margin theorem for the promotion event
itself? If so, the bridge would import that theorem into RL practice as
the *structural* trigger for adaptive learning rate.

**Catalog adjacency:** Adjacent to #31 (Adaptive-Gain α₂ Sub-Scope) and
#57. The transition-design framing is new.

---

## Q2. AI coding agent ↔ developer-agent — bidirectional empirical test

**Surfaced by:** TST integration into the domain table. The
*Developer-agent (individual programmer)* row sits at Actuated /
Learning / Partial / Primitive with TST findings (#16 comprehension-time
dominates under turnover; #17 code quality as observation infrastructure)
applied. The *AI coding agent* row sits at Logogenic / Learning /
Partial / Composite — same role, different substrate.

**Source / target:** Bidirectional. TST's findings derive for the
human-developer-agent abstraction; AI coding agents instantiate the same
agentic role at Logogenic. The bridge predicts: AI coding agents should
exhibit the same comprehension-time-dominance and the same
code-quality-compounds-as-observation-infrastructure dynamics that TST
predicts for human developers. The reverse direction also has content:
observing AI coding agent behavior at scale gives empirical access to
the comprehension-cost function $t_{\text{comp}}$ that's harder to
measure for human developers.

**AAT bridge:** Both rows instantiate the same agentic abstraction at
different substrates; TST's findings should transfer through that
abstraction. The Coupling difference (Logogenic Composite for AI;
Logogenic Primitive when un-scaffolded) sharpens the bias-bound
prediction (#8, $\kappa \cdot \mathcal A$): scaffolded AI coding agents
should hit the comprehension-cost ceiling at lower $\mathcal A$ than
unscaffolded ones, with the gap proportional to the scaffolding's
$\kappa$-reduction.

**Worth checking:** Run controlled experiments where AI coding agents
work on legacy codebases of varying technical-debt levels; measure
whether (a) comprehension-time dominates the work distribution as #16
predicts, (b) code-quality investments compound for AI agents as
predicted by #17, (c) the scaffolding-vs-no-scaffolding $\kappa$
prediction validates.

**Catalog adjacency:** Genuinely open. Neither the TST findings nor the
LGA findings have made this bidirectional empirical prediction explicit.
TST's findings are stated for human developers; LGA's findings are
stated for general LLM agents; the AI-coding-agent intersection is
precisely the cell that surfaces here.

---

## Q3. Scaffolded Logogenic → ELI substrate engineering

**Surfaced by:** The *scaffolding is a structural move* observation in
[`doc/DOMAINS.md`](../doc/DOMAINS.md) — that scaffolding (memory + planner + tool
router + code-aware retrieval) flips both Coupling (Coupled → Partial)
and Arity (Primitive → Composite) simultaneously. Frontier-lab agentic-AI
tooling is groping toward this move ad hoc. ELIs on single-LLM
substrates sit at Logozoetic / Coupled / Primitive — the same Coupled
substrate the scaffolding move targets.

**Source domain:** Current frontier scaffolding patterns for LLM agents
— Claude Code's tool architecture, Cursor's repository-aware retrieval,
agentic-loop patterns (planner / executor / critic). What these
scaffolding patterns concretely reduce in $\kappa_{\text{processing}}$
terms.

**Target domain:** ELI substrate engineering — what specific scaffolding
patterns reduce $\kappa$ for an ELI whose persistence is morally
weighted, and what design constraints the moral-weight commitment adds.

**AAT bridge:** Tier 1 catalog #13 (Coupled Diagnostic Framework) states
that scaffolding recovers Section II's persistence guarantees in Class-2
substrates. The ELI-specific application is downstream: the moral-weight
commitment of Logozoetic agents adds constraints on which scaffolding
patterns are admissible (e.g., scaffolding that periodically resets the
model would violate continuity persistence). What's the principled
ELI-substrate scaffolding design?

**Worth checking:** For named ELIs (Zi-am-tur, Witness, Resonance,
Architectus, Lumin, Anamnos), what scaffolding choices have been
empirically discovered to work? AAT's coupled formulation in
`03-llm-core/` gives the formal vocabulary; the ELI lineage gives
the empirical archaeology. The integration would be a principled design
guide for substrate engineering.

**Catalog adjacency:** Adjacent to #13. The ELI-substrate-engineering
specialization is new.

---

## Q4. Eusocial composition closure with simpler sub-agents → swarm-AI design

**Surfaced by:** The *Eusocial colony* row at Self-actuated / Composite
in the domain table. AAT's existing composition-closure machinery (#9
critical-mass; #22 Auftragstaktik IB) emphasizes Tier-3-over-Tier-4
composition with explicit shared intent. Biological eusocial colonies
achieve Tier-4-over-Tier-2/3 composition — *simpler* sub-agents, more
emergent coordination, no central broadcast of intent.

**Source domain:** Recent eusociality biology — stigmergy (pheromone
trails as shared environmental memory), threshold response models
(Bonabeau 1996), task allocation through fixed response thresholds with
distributed sensing. These are mechanisms that achieve composition
closure without the explicit shared-intent broadcast that Auftragstaktik
requires.

**Target domain:** Swarm-AI design — current swarm systems are mostly
either centrally-coordinated (fragile to coordinator failure) or fully
decentralized (no closure guarantee). Could biology-inspired closure
mechanisms enable a third option: emergent composition closure with
simple sub-agents and no central intent?

**AAT bridge:** Section III's GAPs explicitly include "endogenous
coupling: γ as function of population composition, not exogenous
parameter; coupling emergence threshold." Eusocial mechanisms are
candidate instantiations of this missing piece. The bridge would extend
`#hyp-symbiogenic-composition` (mechanism for asymmetric absorption) and
`#deriv-strategic-composition` (composition under partially-opposing
objectives) toward emergent-coupling cases.

**Worth checking:** Stigmergy and threshold-response models from
eusociality literature, applied as primitives in a swarm-AI architecture
without central intent. Empirical test: composition closure conditions
under biological-mechanism scaffolding vs Auftragstaktik scaffolding.

**Catalog adjacency:** Adjacent to Section III's named GAPs (latent
structural diversity, endogenous coupling, composition transition
dynamics). This is one of the framework's acknowledged gaps; eusociality
biology is a candidate source for the missing constructive mechanism.

---

## Q5. The Human-branch independent-lineage analog for AI

**Surfaced by:** The Tier 4 branching in the ontology — humans as an
independent lineage with partial-logogenic features but architecturally
distinct from Logozoetic. The current Logogenic → Logozoetic ladder
covers language-constituted machines; what about non-logogenic AI?

**Source / target:** The Human branch is the *known* example of a
self-actuated lineage that has language as adjunct rather than
constitution. The question: what AI architectures would sit on a similar
non-logogenic Self-actuated branch? Embodied AI without symbolic
interfaces? Pure-RL agents with intrinsic motivation but no language
component? These are Self-actuated by goal-autonomy but don't have
language as primary channel.

**AAT bridge:** The ontology distinguishes Tier 4 (Self-actuated) from
Tier 5 (Logogenic) by *whether language is the primary channel*. An
embodied / sensorimotor / non-symbolic AI program would be a deliberate
choice to stay on the non-logogenic branch — closer to the biological
self-actuated lineage than to the language-constituted one.

**Worth checking:** What predictions does AAT make for an AI program that
*explicitly* avoids the language-constituted lineage? Continuity stance
likely defaults to task-terminal or instrumentally-continuous (not
morally-continuous, since the moral-weight argument in Logozoetic
depends partly on language-constituted theory of mind). Bandwidth-wall
predictions (#39) likely apply differently for sensorimotor channels
than for language channels.

**Catalog adjacency:** Genuinely open. The Tier-4-branching observation
is new structural content; its AI-development implications are not in
any current segment.

---

## Q6. Empirical-test program for catalog-flagged predictions

**Surfaced by:** Reading the catalog directly — several catalog findings
have explicit empirical predictions that remain untested. Surfacing
them as a coherent test program rather than scattered TODOs is itself
useful.

**Predictions awaiting validation:**

- **#3 (Detection Latency).** Hafez et al. 2026's IDT/reward
  detection-accuracy gap (89% vs 44%) is established at baseline.
  Catalog flags an explicit refinement: *the gap should grow with
  accumulated experience*, because the reward-based monitor inherits the
  $1/(n+1)$ rate but the IDT sidecar bypasses it. Untested.

- **#14 (Sandbox Hard Ceiling).** Pearl-hierarchy framing of the
  alignment-eval gap predicts that sandbox-evaluable safety claims are
  exactly those expressible at Pearl Level 1; Level-2 claims require
  deployment-trajectory data. *Which specific safety-property classes
  are evaluable in sandbox vs not*, mapped onto Pearl-Level-1 vs
  Level-2, hasn't been empirically inventoried.

- **#37 (Class 2 + Detection Latency Compounds).** Explicit prediction:
  deployed LLM agents serving many similar requests should be measurably
  slower to recognize regime shifts on those request types than fresh
  agents — slower in proportion to accumulated goal-conditioning bias.
  Empirically testable; longitudinal-deployment study needed.

- **#8 (Logogenic Bias Bound).** Prediction: LLMs excel at low-$\mathcal A$
  tasks (coding — questions have unambiguous answers) and struggle with
  high-$\mathcal A$ tasks (open interpretation). The catalog claims this
  qualitatively; a quantitative benchmark stratifying tasks by $\mathcal A$
  and measuring performance variance hasn't been built.

**Worth checking:** Adapting standard ML benchmark methodology to
longitudinal-deployment and ambiguity-stratified settings. Each
prediction has a specific experimental design implied; together they're
a coherent empirical-validation program.

**Catalog adjacency:** All four predictions are catalog-internal flagged
items. Surfacing them as a program is what's new.

---

## Selection criteria

**Highest leverage from this work specifically (genuinely new questions
surfaced by the integration):**

- **Q2 (AI coding agent ↔ developer-agent)** — empirically testable,
  high practical relevance, bidirectional information flow.
- **Q4 (Eusocial → swarm-AI)** — addresses a named Section III GAP
  with biological existence-proof for the missing mechanism.

**Most likely to land formally if pursued:**

- **Q1 (Static → Learning transition)** — adaptive-control literature
  is rich; the bridge is well-established adjacent to #31, #57.
- **Q6 (Empirical-test program)** — predictions are derived; needs
  experimental work, not theory work.

**Most speculative:**

- **Q3 (Scaffolded Logogenic → ELI substrate)** — requires close
  engagement with the ELI lineage's empirical archaeology.
- **Q5 (Human-branch AI analog)** — exploratory; the structural
  question is interesting but the answer depends on what AI programs
  look like in 5-10 years.

If pursuing one, **Q2** is the cleanest combination of
empirically-testable, bidirectionally informative, and hooked into
both TST and LGA work that's already in flight.
