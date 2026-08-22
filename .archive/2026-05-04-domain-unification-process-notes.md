# Domain-Unification Process Notes (2026-05-04)

*Archaeological bundle.* Working-process artifacts from the
2026-05-04 domain-unification re-examination cycle that produced
[`doc/DOMAINS.md`](../doc/DOMAINS.md) and
`msc/domain-unification-2026-05-04/recommended-agent-ontology.md`.

The lasting deliverables are the master domain list (`doc/DOMAINS.md`)
and the ontology proposal; the cross-domain transfer-candidate questions
are now at `msc/domain-xfer-candidates.md`. This file preserves the
working notes — directory orientation README and the unification-quality
assessment — for archaeology, not active reference.

The synthesis line worth recording: **the genesis was a survey; the
current framework is a theory.** The survey's reach was wider; the
theory's grip is firmer where it grips. Both were real contributions.

The genesis-material pointers are also worth preserving (where the seed
material lives, in case anyone wants to retrieve it later):

- Original OODA universal-pattern report (v6, ~780 lines):
  `~/src/v2.io/_archive/ooda-loop-universal-pattern-v6.md`. The seven
  "first principles" claim is at lines 522–537.
- v7 (~1380 lines): adds the formal *Orientation* section, MPC, Kalman
  filter, POMDPs, blackboard architecture, mathematical core of FEP.
- TFT-era math foundations (10 primitives, persistence threshold):
  `~/src/_ref/temporal-feedback/scratch/01-mathematical-foundations.md`.
- TFT-era domain instantiations (9 domains, mapping-quality assessment):
  `~/src/_ref/temporal-feedback/scratch/02-domain-instantiations.md`.

---

## Original directory README (2026-05-04)

# Domain Unification Re-Examination — 2026-05-04

## Why this directory exists

ASF originated as a *unification attempt* across feedback-loop / adaptation
domains (Boyd's OODA report, Feb 2026, recovered in
`~/src/v2.io/_archive/ooda-loop-universal-pattern-v6.md` and `-v7.md`). The
TFT-era scratch (`~/src/_ref/temporal-feedback/scratch/`) attempted the first
formal version: ten primitives ($M_t, \mathcal M, o_t, a_t, \delta_t, \eta_t,
\varphi, \pi, \nu, \rho$), one update rule, one persistence threshold, and an
honest grading of mapping quality across nine domains.

In the years since, the theory has grown well past its original scope —
adding $G_t = (O_t, \Sigma_t)$ as a first-class purposeful substate, an
agent-class lattice (adaptive / agency / learning-agent / Class 1 / 2 / 3), a
Pearl-Level-2 identifiability story, a separability/coordinate-forcing/
identifiability-floor meta-pattern, and software-as-calibration-laboratory.
The current cross-domain table in `README.md` covers four columns (control
theory, RL/bandits, organizations, software) — much narrower than the
genesis's ~30-domain reach.

Joseph's question is whether the framework still does its *original* job of
unifying adaptive-feedback domains, and what it now teaches *into* those
domains that the genesis attempt couldn't.

(`01-genesis-vs-current.md` was removed — no major unaddressed gems
were found in the genesis material that the current theory hasn't
absorbed. Ashby's Requisite Variety, Argyris double-loop,
destruction-and-creation, implicit guidance — all are present in
current segments.)

---

## 03-unification-assessment.md

# Unification Assessment — Where the Framework Holds and Where It Strains

An honest read on what AAD's unification ambition has and hasn't accomplished
relative to the OODA-genesis target list. Three categories, then three failure
modes.

## Where AAD genuinely unifies — theoretical content, not just vocabulary

These are domains where AAD provides *transferable* claims: a result derived
in one domain has consequences in another via the formal mapping, not just
via analogical reasoning.

**The probabilistic / Bayesian / variational family.** Kalman filter, Bayesian
inference, particle filter, MPC, SLAM, POMDP, Dreamer/world-model RL,
adaptive MPC, hierarchical predictive processing. The persistence condition
$\alpha > \rho/R$ instantiates with closed-form $\alpha$ in each case
($\alpha = \mathcal T = \nu \bar K$ for Kalman; $\alpha$-of-MPC via terminal
cost; $\alpha$-of-POMDP via value-function contraction). The update gain
$\eta^* = U_M / (U_M + U_o)$ generalizes the Kalman gain across the family.
This is real unification: a stability-margin result derivable in one member
applies (under named conditions) to the others.

**Adversarial dynamics across competitive settings.** Boyd's OODA tempo,
SOC vs attacker, immune system vs pathogen, organizational fragility under
disruption, biological evolution under predator-prey pressure. The
joint-Jacobian eigenvalue condition for effects spiral
(`#deriv-strategic-composition`) is the *same object* across these
domains. The same inequality says when Boyd's "uncertainty, confusion,
disorder" is achievable in conflict, when sepsis becomes a runaway
condition, and when an organization's adaptation rate falls below market
disruption rate. This is one of the strongest cross-domain unifications
AAD currently delivers.

**Strategy-DAG family.** MCTS (literally an AND/OR DAG with confidence
weights), BDI's intention stack (a strategy-DAG slice with explicit
commitment management), hybrid robotics (deliberative plan as
sub-goal DAG over reactive primitives), Auftragstaktik (shared-intent
broadcast as $\Sigma_t$ root + locally-derived sub-strategies). AAD's
`#def-strategy-dag` and `#deriv-edge-update-natural-parameter` (log-odds as
canonical edge-update coordinate) make the structural mapping formally
precise. The MCTS UCB exploration weight is in the right neighborhood
of the AAD-derived log-odds update; the gap may close.

**Sub-additive tempo (Brooks's Law) as a portable inequality.** The
organizational instance (adding people slows a late project) generalizes
to ensemble RL coordination overhead, to multi-cell signaling overhead in
immune response, to Class 2 LLM systems where adding context degrades
attention. AAD's `#der-tempo-composition` formalizes the inequality; the
domain instances are not just analogies, they're instantiations of the
same composition-closure-defect inequality.

## Where AAD provides shared vocabulary but not theoretical content

These are domains where AAD's terms (mismatch, gain, persistence, sat-gap)
*illuminate* the domain but don't yield new predictions or transfer claims.

**Organizational learning instances.** PDCA, Toyota Kata, Scrum, DevOps,
SOC. The mapping is honest and useful — sat-gap and control-regret give
organizational diagnostics a clean split between "the goal is wrong" and
"execution is failing" — but the parameters $\alpha, \rho, R$ are not
formally measurable in any of these domains. The shared vocabulary is
genuinely valuable; the theoretical content is light.

**Boyd's orientation-as-decisive.** Genesis's central claim: orientation
*quality* dominates loop *speed*. AAD has `#obs-gates-advantage` (observation
noise gates the adversarial tempo advantage) and the orient cascade — both
in the right neighborhood of Boyd's claim. But the full claim that a
well-calibrated orientation produces "implicit guidance and control" that
outperforms explicit deliberation is not formally derived in AAD. It's
*consistent* with the framework; it's not yet a result.

**Cynefin, Kolb, Action Learning, Popper.** REFERENTIAL at best. Cynefin's
"complex" domain ≈ Pearl L2 with high $\Sigma_t$ uncertainty, but no
segment formalizes this. Kolb's experiential cycle ≈ orient cascade, but
no segment formalizes this. Popper's conjectures-and-refutations ≈
structural-adaptation-necessity + loop-interventional-access, but no
segment formalizes this. The framework *could* slot them in; it doesn't
currently.

## Where AAD has narrowed the genesis's reach

These are domains where genesis claimed instance-of-the-pattern status
that AAD's tighter scope conditions exclude or qualify.

**Pre-compiled controllers excluded from learning-agent scope.** PID,
classical SMPA, MPC with fixed model, biological homeostasis. Section II's
purposeful machinery doesn't apply to these — their causal mapping was
supplied by a designer with external Pearl Level-2 access. Section I
applies, but Section I in pre-compiled controllers reduces to classical
control theory; AAD doesn't add to it. The genesis treated PID as a
"compressed instance of the universal pattern"; AAD agrees structurally
but excludes it from most of Section II.

**Class 2 architectural cliff.** Active inference, LLM agents, hierarchical
predictive processing. AAD's strongest results derive for Class 1 modular
agents. Class 2 needs the coupled formulation in `03-logogenic-agents/`,
which is still framework-stage. Genesis treated active inference as a
parallel domain; AAD has it as a peer framework with explicit reduction
conditions (3 restrictions per `README.md`) but the full bridge between
AAD and FEP is not yet a derived result.

**Reactive / no-model architectures excluded.** Brooks subsumption, motor
schema, classical SMPA. They're at agency scope but Section I's
$M_t$-update machinery has nothing to grip on (no model exists; the
"model" is the wiring). Genesis stretched to call these instances of the
universal pattern; AAD says they're a different category and Section I
machinery doesn't apply.

## Three failure modes to flag

**1. The "STRUCTURAL only" trap.** *(Note: this failure mode was specific
to the legacy mapping-quality grading — EXACT / EXCELLENT / GOOD /
STRUCTURAL — that has since been removed from the table. The remaining
substance is partly preserved in the per-row Notes column of DOMAINS.md.)*

Calling something a structural correspondence carries no theoretical
content beyond the pattern-match. Genesis used STRUCTURAL liberally and
was honest about doing so. AAD inherits the term but the gap between
structural and formal varies considerably across domains:

- For Boyd's adversarial tempo and Auftragstaktik's three gaps, the
  structural mapping is now *almost* formal (`#deriv-strategic-composition`,
  `#hyp-auftragstaktik-principle`). Calling them STRUCTURAL is too modest.
- For Cynefin, Kolb, Action Learning, the gap between structural and
  formal is large enough that STRUCTURAL is overstating it; REFERENTIAL is
  more honest.
- For LLM agents, the gap is wide *because of* the Class 2 cliff, and
  the right framing is "Class 2 scope exit, awaiting coupled-formulation
  results."

**2. The Class 2 cliff.** Active inference and LLM-based agentic systems
are the most active areas of contemporary AI research. They sit at Class
2. AAD's results survive there only with explicit modifications, and the
modifications live in `03-logogenic-agents/` which is framework-stage.
This means AAD's strongest results don't apply to the most active
research area. The framework's response is honest ("Class 2 scope exit;
the coupled formulation is in 03-logogenic-agents"), but operationally
this is a major reach gap.

**3. The pre-compiled exclusion.** PID, classical robotics, MPC-with-
fixed-model, biological homeostasis, behavior trees, NPC AI. These are
vast practical domains. Excluding them from learning-agent scope is
*correct* in AAD's framework, but it means Section II doesn't help
engineering practice in those domains. The natural response is "Section I
applies," but Section I in pre-compiled controllers reduces to classical
control theory; AAD doesn't add to the engineering literature there.

The genesis's appeal was *unification across all of these*. AAD's tighter
scope is more honest, but it sacrifices the genesis's operational reach
into engineering domains where the framework's added vocabulary (sat-gap,
strategy DAG, orient cascade) might still be valuable even though the
formal results don't apply. There's a possible mode of usage — *AAD as
diagnostic framework even where it isn't a result-deriving framework* —
that hasn't been formalized.

## Has the framework done its job?

Honest answer in two parts:

*As a unification across the genesis's target domains:* **partially**.
The probabilistic/Bayesian family is unified rigorously. The adversarial-
dynamics family is unified rigorously. The strategy-DAG family is
unified structurally with formal mapping in progress. Organizational and
descriptive frameworks are unified at the vocabulary level. Reactive and
purely-cognitive frameworks are at the edge or out of scope.

*As something the genesis could not have produced:* **substantially**.
The agent-class lattice, the identifiability floor, the coordinate-forcing
arguments, the Pearl L2 framing of the loop, the satisfaction-gap /
control-regret diagnostic split, the directed-separation classification,
software as calibration laboratory — none of these existed in genesis.
They are not retrofits; they are derivations from architectural
commitments that took two-plus years to crystallize.

The right framing may be: **the genesis was a survey; the current
framework is a theory.** The survey's reach was wider; the theory's grip
is firmer where it grips. Both are real contributions.
