# Enrichment Candidates: Prior Art That May Strengthen AAT

*Sweep author: Claude Opus 4.7 (1M context), 2026-05-21.
A different-posture document from the usual novelty-defense work:
candidates from the prior-art landscape that look like they could
**enrich** AAT toward its actual purpose (holistic agency theory from
first principles) rather than challenge its novelty. Per Joseph's
2026-05-21 framing: "we have no problem recapitulating important
findings from others, especially if we end up building on it."*

> **Honest scope.** This is a *pointer document*, not a systematic
> survey. The candidates below struck me as either (a) genuinely new
> to me during the prior-art refresh cycle, (b) named in memos /
> cluster_references / the Pillar prior-art report but not yet
> deeply engaged by AAT, or (c) areas where I noticed AAT touches
> something but doesn't go as deep as the literature would allow. A
> deeper Undermind-style sweep on each area would surface more; a
> focused expert with topic-specific knowledge would catch things I
> miss. Filter is: *what would other agents flesh-out cycles
> likely not have drawn on readily?* — under-touched specifically.

## 0. What's *not* here (already integrated)

To avoid repeating what AAT already cites: Pearl's $do$-calculus and
the Bareinboim hierarchy program; the IB master objective (Tishby-
Pereira-Bialek 1999); the Cramér-Rao bound + Fisher information;
Zames/Lur'e sector conditions; Lyapunov stability + monotone-operator
theory; Active Inference / FEP (Friston line); AIXI (Hutter); Sandholm
*Population Games* is referenced via the Pillar report but should
land; Monderer-Shapley potential games + Rosen monotone games;
Hart-Mas-Colell CCE; Kalman/Ho-Kalman canonical-form non-uniqueness;
common-Lyapunov-nonexistence (Liberzon / Dayawansa-Martin / Shorten);
Čencov's invariance theorem; Sahai-Mitter anytime capacity; Omohundro
basic AI drives; Bostrom *Superintelligence*; Bareinboim-Correa-Ibeling-
Icard 2022 CHT; Conant-Ashby good regulator (via Virgo 2025).

These are the existing AAT citation set per the prior-art-analysis
files + the cluster_references + the Pillar report. The candidates
below are *additional*.

---

## 1. Foundational mathematical results AAT could anchor in more deeply

### 1.a Conley's Fundamental Theorem of Dynamical Systems (Conley 1978)

*Conley, C. (1978). Isolated Invariant Sets and the Morse Index. AMS
Regional Conference Series 38.*

Every continuous flow on a compact metric space admits a continuous
real-valued function (a "complete Lyapunov function") that is
strictly decreasing on the complement of the **chain-recurrent
set** and constant on each chain-recurrent component. This is
*literally* the universal-Lyapunov result AAT's persistence machinery
gestures at — and is the foundation Omidshafiei et al. (2019) build
$\alpha$-Rank on via Markov-Chain Components. AAT cites Lyapunov
stability extensively but doesn't anchor in Conley's universality.
**Why it would enrich AAT:** the universality claim "if an agent's
dynamics admit *any* persistent structure, there is a Lyapunov-style
certificate" is a theorem, not an assumption. AAT could cite Conley
as the foundation that makes the sector-persistence template's
universality honest. Connects directly to the dynamic-regime axis
work (R0/R1/R2/R3).

### 1.b The Hodge / Helmholtz decomposition for games (Candogan-Menache-Ozdaglar-Parrilo 2011; Letcher-Balduzzi et al. 2019)

*Candogan, O., Menache, I., Ozdaglar, A., Parrilo, P. A. (2011).
Flows and Decompositions of Games: Harmonic and Potential Games.
Math. of OR 36:474–503. + Letcher, A., Balduzzi, D., Racanière, S.,
Martens, J., Foerster, J., Tuyls, K., Graepel, T. (2019).
Differentiable Game Mechanics. JMLR 20.*

Every finite normal-form game decomposes *uniquely* as a sum of
(i) a **potential** component (gradient flow / cooperative), (ii) a
**harmonic** component (conservative flow / conflicting), (iii) a
**nonstrategic** component. Letcher-Balduzzi gives the continuous /
dynamics-side version via Helmholtz decomposition of the joint
pseudo-gradient field, with Symplectic Gradient Adjustment (SGA) as
the algorithm that handles both components. **Why it would enrich
AAT:** this is the deep mathematical structure under the dynamic-
regime axis's R1 (potential) vs R2 (cyclic / harmonic) distinction.
It's named in the Pillar report (T1) as substantial-overlap prior art
but the *integration depth* AAT could reach hasn't been explored —
SGA might be the AAT-native update rule for actuated agents under
strategic composition, and the Hodge decomposition might illuminate
the (C-iv) strategic-equilibrium scope route structurally.

### 1.c $\alpha$-Rank's Markov-Chain Component machinery (Omidshafiei et al. 2019)

*Omidshafiei, S., Tuyls, K., Czarnecki, W. M., Santos, F. C., Rowland,
M., Connor, J., Hennes, D., Muller, P., Pérolat, J., De Vylder, B.,
Gruslys, A., Munos, R. (2019). $\alpha$-Rank: Multi-Agent Evaluation
by Evolution. Scientific Reports 9:9937.*

Replaces Nash equilibrium with a **dynamical solution concept** based
on Conley's chain-recurrent decomposition: the Markov-Chain Component
(MCC) is the solution. The framing is explicit about why Nash fails
when dynamics don't converge to a point. **Why it would enrich AAT:**
when AAT's strategic-composition machinery lands the dynamic-regime
axis, MCC is the natural solution concept for R2 (cyclic-distributional)
— *not* just "regret minimization converges to CCE" as a fallback,
but "the recurrent set *is* the macro-state." This is sharper than
AAT's current §F treatment of distributional macro-states.

### 1.d Symplectic Gradient Adjustment (SGA) and Hamiltonian-respecting learning dynamics

Subsumed under 1.b but worth its own pointer. The algorithm provably
converges locally to stable fixed points in games where vanilla
gradient descent cycles. If AAT lands the actuated-agent learning
rule for strategic composition (currently under-specified at the
sub-scope-α' layer), SGA is the natural candidate. **Direct
practical hook for `#deriv-strategic-composition` machinery.**

### 1.e Cheung-Piliouras-Tao 2021: passivity ↔ regret ↔ Poincaré recurrence

*Cheung, Y. K., Piliouras, G., Tao, Y. (2021). Online Optimization in
Games via Control Theory: Connecting Regret, Passivity and Poincaré
Recurrence. ICML 2021 (arXiv:2106.04748).*

Establishes a **direct mathematical correspondence** between
control-theoretic passivity, online-learning regret bounds, and
Poincaré recurrence (the empirical play visiting everywhere). This is
arguably the deepest single result on the regret/dynamics/control
intersection. **Why it would enrich AAT:** AAT's sector condition is
passivity-shaped; AAT's directional-fidelity B1 condition (row 17) is
regret-shaped; AAT's R2 cyclic-distributional regime is Poincaré-
recurrence-shaped. Cheung-Piliouras-Tao *unifies all three*. This
might be the precise mathematical content under the convergent
meta-finding that AAT's tools across rows 03 / 10 / 14 / 17 are
secretly the same.

---

## 2. Recent papers (2020+) that postdate most existing AAT searches

### 2.a Mertikopoulos-Papadimitriou-Piliouras "Cycles in adversarial regularized learning" (2018) + sequels

*Mertikopoulos, P., Papadimitriou, C., Piliouras, G. (2018). Cycles
in adversarial regularized learning. SODA 2018.*

In two-player zero-sum games, no-regret play does *not* converge to
Nash even pointwise — it Poincaré-recurs around the equilibrium.
Last-iterate vs time-average distinction. **Why it would enrich AAT:**
AAT's row 14 mentions Daskalakis et al. on last-iterate non-convergence
but doesn't fully engage with the Mertikopoulos line, which is now
the modern multi-agent-learning baseline. AAT's adversarial-tempo
machinery (row 10) could be deepened by the cycles-not-convergence
formal structure.

### 2.b Yu-Davis et al. 2025: Inverse Noncooperative Games With Indistinguishable Observations

*IEEE Transactions on Automatic Control 70:6513–.*

Recent inverse-game-theory work on parameter reconstruction from
*permuted* observations. The negative side of identification — what
*can't* be recovered from observation — is structurally adjacent to
AAT's identifiability-floor work (row 11, Instance 4). **Why it
would enrich AAT:** the inverse-game-theory literature has been
mostly orthogonal to AAT; engaging with Yu-Davis 2025 specifically
might surface formal connections between AAT's regime-from-marginals
no-go (broadened Instance 3) and the inverse-game-theory positive
identification program.

### 2.c Richens-Abel-Bellot-Everitt 2025: General agents contain world models

*arXiv 2506.* (Cited in the row-20 refresh but not deeply integrated.)

Theorem-shape: sufficiently general goal-directed behavior *forces*
an implicit world model. **Why it would enrich AAT:** this is the
strongest formal statement to date on model-richness as a forced
property of goal-directed agency. AAT cites it for the agent-spectrum
work but could integrate the result more deeply — particularly as a
formal anchor for what the "structured $M_t$" of an actuated agent
must contain.

### 2.d Virgo-Biehl-Baltieri-Capucci 2025: A "good regulator theorem" for embodied agents

*arXiv:2508.06326.*

Embodied / situated extension of Conant-Ashby's good regulator
theorem. **Why it would enrich AAT:** AAT's relationship to the
Conant-Ashby tradition is via Virgo 2025; the embodied extension may
matter for the `04-eli-core/` and `03-llm-core/` work where the
substrate is not state-space-clean.

### 2.e Cohen-Hutter-Osborne 2022: Advanced artificial agents intervene in the provision of reward

A formal argument that sufficiently advanced agents will tamper with
reward. **Why it would enrich AAT:** AAT's self-actuation grounding
no-go (row 13) directly addresses this; engaging with Cohen-Hutter-
Osborne explicitly would strengthen the alignment-community
positioning.

### 2.f Smithe 2024: Structured Active Inference (arXiv:2406.07577) + Capucci-Gavranović-Hedges-Rischel 2022: Towards foundations of categorical cybernetics

These are the *categorical cybernetics / open-games / lens-based*
approach to compositional agents. **Why it would enrich AAT:** AAT's
composition machinery (rows 08, 14) is heavily structural but not
yet category-theoretic. The categorical-cybernetics tradition has
developed lens-shaped composition for agents — a formal home for
"composition as the agent-level operation" that AAT does informally.
Worth at least an honest engagement (probably not full categorical
re-foundation, but acknowledgment + integration of the lens-shape
where useful).

### 2.g Friston-Heins-Verbelen-Da Costa et al. 2025: From pixels to planning — scale-free active inference

*Front. Network Physiology 2025.*

Recent FEP extension dealing with hierarchical generative models
under scale-free renormalization-group framing. **Why it would
enrich AAT:** AAT's compression-operations machinery (row 19)
acknowledges FEP via "preferences as priors" critique but doesn't
engage with the recent scale-free RG work. If AAT's stability-
certificate spine ever wants a hierarchical version, the RG framing
is the natural place to look.

---

## 3. Adjacent formal frameworks worth engaging

### 3.a Constructor Theory (Deutsch-Marletto)

*Deutsch, D. (2013). Constructor Theory. Synthese 190:4331–4359. +
Marletto, C. (2015). Constructor Theory of Information. Proc. R. Soc.
A 471.*

"What tasks are possible / impossible" as a foundational physical
framework. **Why it would enrich AAT:** structurally adjacent to AAT's
constructive-impossibility posture (`#disc-constructive-impossibility-
posture`). The Deutsch-Marletto framing of physics-as-task-possibility
is a respected alternative-foundations program that engages directly
with what AAT is doing methodologically. Could provide framework-level
positioning support.

### 3.b Sheaf theory and contextuality (Abramsky-Brandenburger 2011 + sequels)

*Abramsky, S., Brandenburger, A. (2011). The Sheaf-Theoretic Structure
of Non-Locality and Contextuality. New J. Phys. 13:113036.*

A sheaf-theoretic account of how local consistency fails to glue into
global consistency under contextuality. **Why it would enrich AAT:**
AAT's closure-defect $\varepsilon^\ast$ at the composition layer is
asking essentially this question (local sub-agent consistency vs
global composite consistency). Sheaf-theoretic contextuality might
provide a sharper mathematical home for the closure-defect machinery,
particularly when the sub-agents' local laws don't glue into a
coherent global law.

### 3.c Aumann's agreement theorem and common-knowledge

*Aumann, R. J. (1976). Agreeing to Disagree. Annals of Statistics
4:1236–1239.*

If two Bayesian agents with common priors share posteriors, they must
agree. **Why it would enrich AAT:** AAT's shared-intent / coordination
machinery (row 09) cites Hart-Mas-Colell + Dessein but not Aumann.
Aumann's theorem is *the* foundational result on when agents *must*
converge in beliefs under common knowledge — directly relevant to the
unity-of-objective dimension and to the closure-defect minimum in
maximally-aligned composites.

### 3.d Conway-Coecke ZX-calculus and process-theoretic foundations

Process-theoretic / diagrammatic-categorical approaches to
information-flow. **Why it would enrich AAT:** speculative, but the
diagrammatic process-theory work might offer a graphical / categorical
discipline for AAT's information-flow diagrams (the orient cascade,
the strategy-DAG-as-causal-graph machinery). Lower priority than 3.a–c
but worth a pointer.

---

## 4. Cross-disciplinary anchors AAT could ground in

### 4.a Cognitive ethology and animal-agency comparative work

*Allen, C., Bekoff, M. (1997). Species of Mind: The Philosophy and
Biology of Cognitive Ethology. MIT Press. + Andrews, K. (2020). How
to Study Animal Minds. Cambridge.*

Cross-species comparative work on what counts as agency. **Why it
would enrich AAT:** AAT's agent-spectrum (row 20) is mostly
mathematical / state-space. The cognitive-ethology tradition has
detailed empirical taxonomies of animal agency — could ground AAT's
spectrum claims in concrete cases (octopus, corvid, primate, social
insect) beyond the Moore-machine and Hafez bi-predictability anchors.

### 4.b Csibra-Gergely "naive theory of rational action" and developmental psychology

*Csibra, G., Gergely, G. (2007). 'Obsessed with goals': Functions and
mechanisms of teleological interpretation of actions in humans. Acta
Psychologica 124:60–78.*

Empirical work on infants' teleological stance — when humans (or
infants) attribute goal-directedness to observed agents. **Why it
would enrich AAT:** AAT's self-actuation and continuity-stance
machinery is normative; Csibra-Gergely provides the *empirical
psychology* of how observers detect agency. The Hafez bi-
predictability metric is roughly the formal version of what
Csibra-Gergely's teleological-stance work measures behaviorally.

### 4.c Anders Ericsson's deliberate-practice + Hatano-Inagaki adaptive vs routine expertise

Expertise / skill-acquisition empirical work. **Why it would enrich
AAT:** AAT's action-fluency (row 16) cites EVC, anytime algorithms,
and model-based-vs-model-free arbitration. The Ericsson / Hatano-
Inagaki tradition has detailed empirical accounts of how *deliberation
becomes fluency* over training — the temporal-developmental side of
AAT's deliberation-threshold derivation. Could empirically ground the
"action-generating capacity has been absorbed into the model's
structure" claim.

### 4.d Pessoa and Lewis on cognition-emotion integration

*Pessoa, L. (2013). The Cognitive-Emotional Brain. MIT Press.*

Empirical neuroscience showing that emotion is not separate from
cognition but integrated into goal-directed action selection. **Why
it would enrich AAT:** AAT's continuity stance (row 15) is normative
("morally continuous" / "indifferent" etc.) but doesn't have a
mechanism story for how the stance is *implemented* in real agents.
Emotion-regulation work (Gross 1998, Pessoa 2013) is the closest
mechanism literature. Could ground continuity-stance in something
concrete for the `04-eli-core/` discussions.

### 4.e Friston-Sajid-Da Costa-Heins recent precision-weighted work

Specifically the active-inference precision-weighting machinery, where
attention modulates prediction-error-driven updates. **Why it would
enrich AAT:** AAT's update gain $\eta^\ast = U_M / (U_M + U_o)$
already has the right shape (precision-weighted balance between prior
and likelihood). The active-inference precision-weighting line offers
empirical / neuro support for this functional form — could
substantially strengthen the gain principle's empirical anchoring.

---

## 5. Specific connections in things AAT already cites but uses lightly

### 5.a Wolpert-Grochow-Libby-DeDeo: Optimal high-level descriptions of dynamical systems (2014)

AAT cites this in row 19 (IB unification) as the closest precedent
for the composition-projection compression operation. But the Wolpert
et al. machinery is *more general* than AAT currently uses — they
develop a full predictive-compression framework for macro-projections.
**Worth deepening engagement** in the composition-closure work
(row 08).

### 5.b Rungger-Zamani: Compositional Construction of Approximate Abstractions of Interconnected Control Systems (2015/2018)

*IEEE TCNS 5:116.* The closest formal ancestor of AAT's closure-defect
quantitative-error machinery. AAT cites in row 08 but the actual
mathematical machinery (output-error bounds compositional under
interconnection) could be a directly-usable formal foundation for the
composition-closure (P1)–(P3) machinery.

### 5.c Genewein-Leibfried-Grau-Moya-Braun: Bounded Rationality, Abstraction, and Hierarchical Decision-Making (2015)

*Frontiers Robotics AI 2:27.* Multi-node bounded-rational architectures
under one information-theoretic objective. AAT's row 19 cites this as
the closest U-medium ancestor, but the actual Genewein et al. machinery
(unified objective across one-step / serial / parallel hierarchies)
is more developed than AAT's current treatment uses. **Could
strengthen the four-compression-operations bindings table** by
identifying which AAT compression operations map onto which Genewein
et al. hierarchies.

### 5.d Marzen 2016 predictive rate-distortion for infinite-order Markov processes

Already cited (PDF in `ref/`); but the predictive-rate-distortion
machinery for non-finite-order processes could ground AAT's $M_t$
compression machinery (row 01) more deeply. **Worth re-engaging** to
see if the infinite-order PRD framework illuminates AAT's chronica
compression.

### 5.e Subramanian-Sinha-Seraj-Mahajan 2020: Approximate information state for approximate planning

*arXiv:2010.08843.* AAT cites in row 01; the AIS machinery is a deep
foundation for information-state-as-compressed-sufficient-statistic
that AAT could engage more substantially — particularly for the
formal definition of "information state" that underwrites AAT's
recursive Markovian-update axiom.

---

## 6. Things I'm uncertain about (lower-confidence candidates)

### 6.a Sheaf-theoretic accounts of cognition (Bonchi, Sobocinski, etc.)

Compositional / categorical accounts of computation that might
ground AAT's compositional structure in category theory. Lower
confidence because I'm not sure how relevant the specific results
are; might be a tangent.

### 6.b Critical-slowing-down as a regime-transition signature

*Scheffer, M. et al. (2009). Early-warning signals for critical
transitions. Nature 461:53–59.*

Empirical signature of dynamical-systems transitions: variance
increases and autocorrelation lengthens before a regime change. **If**
AAT's dynamic-regime axis ever wants empirical signatures of regime
transitions, this is the canonical literature. Lower confidence
because I'm not sure if regime-transition empirical detection is in
AAT's scope.

### 6.c Bayesian model averaging and ensemble methods

A connection point between AAT's bounded-cognition machinery and the
ML practice of ensembling. Lower confidence — possibly too
narrow / practical to land in the framework.

### 6.d The "thinking, fast and slow" empirical-psychology line (Kahneman-Tversky-Stanovich)

AAT touches via Kahneman's System 1 / System 2 in row 16; the deeper
empirical-psychology tradition (Stanovich, Evans dual-process work)
might ground action-fluency more concretely. Lower confidence because
it could pull AAT into psychology-of-decision-making in a way that
might not fit.

---

## 7. Honest meta-observations

**What I'm probably missing:** specific niche literatures that an
expert in (say) algebraic game theory, theoretical neuroscience,
mechanism-design beyond the impossibility cluster, philosophy of
action, or AI safety would catch. The candidates above are biased
toward what I happened to notice during the prior-art refresh cycle.

**Where the highest-yield deepening probably is** (my guess, not a
recommendation):
- §1.a Conley's Fundamental Theorem — foundational and AAT has been
  using its consequences without anchoring in it.
- §1.b Hodge / Helmholtz decomposition for games + §1.d SGA — the
  dynamic-regime axis work has direct use for this.
- §1.e Cheung-Piliouras-Tao passivity↔regret↔Poincaré — the
  potential cross-row unification it might enable.
- §2.f Categorical cybernetics — substantial framework-foundation
  engagement; long-horizon but high-leverage.
- §3.a Constructor theory — framework-positioning support for the
  constructive-impossibility-posture.

**What this document is *not*:** an exhaustive sweep. A targeted
Undermind cycle on (say) "AAT's compositional structure × categorical
cybernetics" or "dynamic-regime axis × Conley/Hodge/MCC machinery"
would surface more depth in each area. The candidates here are
pointers worth looking into; deciding which to invest cycles in is
your call.

**Sequencing recommendation if you want to act on any of these:**
none of them block any current work. They are all candidates for
*post-Phase-4* enrichment cycles — when the strategic-composition
canon settles. If the dynamic-regime axis lands as a meta-segment
(Track A Phase 6), the §1.a/b/c/d/e cluster becomes immediately
load-bearing for that meta-segment's authoring.

---

*End of sweep. The framework's posture toward this kind of enrichment
— recapitulate-and-build rather than novelty-chase — is itself rare
and load-bearing for AAT's purpose; this document is a small
contribution to that posture.*
