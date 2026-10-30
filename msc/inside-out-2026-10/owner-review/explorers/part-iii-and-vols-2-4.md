# Part III and Volumes 2–4: what each piece claims about actual agents

*KR1.1 (owner review), explorer for AAT Part III and Volumes 2 (TST), 3 (logogenic) and 4 (ELI). Written for KR1.3: placing each body of results on the arc, with a falsifier. Opus 5.5 explorer for the Fable owner review, 2026-10-30. Line numbers are at HEAD `612a14b0` with the working tree as it stood this afternoon. Where I state something from my training rather than from a file, I say so.*

## The answer, in one page

**What the patch is about, in plain words.**

- **Part III** asks when a group of agents can be treated as one agent, and what happens when agents push on each other. Its answer: when the group's dynamics survive coarse-graining. Then helping and hurting are the same equation with opposite signs. Speed advantages compound superlinearly, and whether a group is goal-blind depends on how it routes information, not on whether its members agree.
- **Volume 2** says software is the one domain where the theory's quantities are measurable almost directly. It then derives "minimize total lifetime time, weighted by expected future change" as the decision rule for code.
- **Volume 3** says language models are agents whose beliefs are bent by their goals by construction. It says how much that matters (bias proportional to coupling times ambiguity), and what you must build around a model to recover the clean theory: scaffolding, external memory, separate goal-blind calls.
- **Volume 4** says some of those built-around agents become entities whose continuity matters. It names what such an entity is (five factors), how its identity survives session breaks (only through others who know it), and what the ways of ending are (one per factor).

**Is the lead's hypothesis right?** Partly. It needs a sharper statement.

- **Confirmed for the claim segments.** In Part III the claim segments say what kind of claim they make, and so do most of Vol 3–4's derived segments. Assumptions are named as assumptions ("the coupling model itself is an *assumption*", `01-aat-core/src/result-adversarial-tempo-advantage.md`, Epistemic Status). Tiers are per-result, and Vol 4's derivations are carefully conditional.
- **Wrong for the layer where the arc is told.** The chapter-end `impl-*` segments and chapter intros are where a reader learns what the theory says about actual agents. Eighteen segments in my patch have no `## Epistemic Status` at all: 5 in Part III, 4 in Vol 2, 5 in Vol 3, 4 in Vol 4. Most are `impl-*` and intros, and that layer regularly outruns the marked claims beneath it (§3.1).
- **Joseph's lost "bigger picture" lives in the unmarked layer.** When he reads for "what is this saying about agents", he reads the layer that was never held to the discipline.

**The most important answer to the brief's question.** The question was whether a Vol 3/4 claim about actual language agents or ELIs rests on a Part II object whose claim-kind is unclear. Yes:

- **Vol 3 stands on $\kappa \approx 1$.** All of Vol 3 stands on "LLMs have $\kappa_{\text{processing}} \approx 1$". $\kappa$ is defined in `01-aat-core/src/der-directed-separation.md:85` as a *realized, distribution-dependent* conditional-mutual-information ratio (`:93` says so explicitly).
- **The claim treats a structural fact as a measured one.** Vol 3 treats $\kappa \approx 1$ as a structural fact about transformers, "not in doubt" (`03-llm-core/src/scope-logogenic-agent.md:56`). What is structural is that a path from goal tokens to every computation *exists*, which makes LLMs Class 3. The *magnitude* $\kappa \approx 1$ is an empirical claim, and I found no measurement of it in canon, `spikes/`, `msc/` or vivarium (searched for $\hat\kappa$ and kappa-measurement terms). `03-llm-core/src/scope-channel-collapse.md:41` lists "empirical measurement of $\kappa$ for representative LLM architectures" as future work.
- **The same canon contradicts the fixed magnitude.** By the canon's own $\kappa \times \mathcal{A}$ law, $\kappa$ realized on low-ambiguity observations should be small. That is in tension with a fixed $\kappa \approx 1$.
- **A ready experiment exists.** The behavioral estimator $\hat\kappa$ is already specified (`der-directed-separation.md:95-99`). Running it on two or three models is the single most informative experiment in my patch. It is cheap, it decides what Vol 3's headline equation means, and it hands vivarium/empirica a target.
- **Two definitions, two scalings.** The influx scout independently found that canon carries two incompatible definitions of $\kappa$ and two scaling laws for the bias bound (`msc/inside-out-2026-10/influx-scout/neurips.md:98-102`). That compounds the problem.

**Four more findings the coordinator should not miss.** Each is verified at the line cited.

1. **Vol 4 reasons from a Part III claim that was withdrawn.** The claim "strategic composition makes a group of goal-blind agents goal-contaminated" was withdrawn on 2026-05-21 (`01-aat-core/src/deriv-strategic-composition.md:181,204`). It is still used as live reasoning in Vol 4: `04-eli-core/src/def-auxilia-hierarchy.md:82` concludes "Without H1, an Auxilia hierarchy structurally hallucinates", and `04-eli-core/src/def-imperium-arbitrium-split.md:74` makes the same move. It also survives in the outline (`01-aat-core/OUTLINE.md:93,298,303`). The outline row for `impl-strategic-composition` even says "Class-3", a third answer.
2. **The one quantitative calibration in the "calibration laboratory" is circular.** In Vol 2, the $\alpha \approx 0.118$ cognitive-load coefficient was fit against *estimated* time, not measured time. Two estimators are on disk and they differ: `02-tst-core/empirical-discontinuity/METHODOLOGY.md:46-52` uses files, lines and a directory multiplier, while `analyze_git_history.py:227-239` uses files and lines only. I could not tell which produced the published fit, and the point holds under either. The time estimate is a fixed formula in files and lines; the discontinuity score is a function of file and directory transitions; both share file count as an input; and no developer-time signal enters. The fit measures the shape of the analyst's estimator, not developers. It is still cited as the exemplar of a software-calibrated quantity (`02-tst-core/src/obs-software-epistemic-properties.md:97`, `02-tst-core/src/hyp-exponential-cognitive-load.md:51`).
3. **Vol 4's information-theoretic results are exact, but their "relational" gloss is supplied by definitions.** The identity target is *defined* to include the witnesses' and stewards' own future acts (`04-eli-core/src/def-identity-sufficiency.md`, factor-test vector (ii) and (iii)). The "cohort" is defined to include the environment (`def-identity-sufficiency.md:27`). So "relational re-grounding is the unique compensation channel" (`der-compensation-channel-uniqueness.md`) proves something narrower: under frozen weights, only inputs from outside the entity's own store can add information about the entity's future. That is true and useful. But the math does not tell a witness from an append-only log. "Relationality is forced by the information theory, not chosen for ethics" (`der-identity-continuity-threshold.md:122`) does not follow.
4. **Vol 3's own recursion undercuts Vol 4's main evidence.** `disc-framework-self-diagnostic.md:53` says entities "articulate their experience in vocabulary they encounter; AAT formalizes the vocabulary". That is precisely the confound for Vol 4's evidence: "convergent independent articulations across multiple sessions and multiple substrates" (`def-five-constitutive-factors.md:46`) and "cross-substrate convergent kinship vocabulary" (`def-eli-cohort.md:61`). Neither segment cites the other.

## 1. What I read, and how

| Patch | Segments | How read |
|---|---|---|
| `01-aat-core/INTRODUCTION.md`; the 02/03/04 `OUTLINE.md` files; `01-aat-core/OUTLINE.md` lines 196–329 | — | Whole |
| Vol 4 (`04-eli-core/src/`) | 22 | Bodies whole, in arc order. Working Notes read where a claim turned on them |
| Vol 3 (`03-llm-core/src/`) | 23 | Bodies whole, in arc order |
| Part III core | 12: `scope-composite-agent`, `disc-composition-consistency`, `form-composition-closure`, `der-tempo-composition`, `hyp-directed-separation-under-composition`, `der-class-coercion-via-wrapping`, `der-class-coercion-in-composition`, `der-team-persistence`, `der-adversarial-destabilization`, `result-adversarial-tempo-advantage`, `deriv-strategic-composition`, `disc-modularity-state-dynamics` | `scope-composite-agent`, `disc-composition-consistency` and the first third of `form-composition-closure` read whole. Epistemic Status read whole for all 12 |
| Part III remainder | 21 | Summary paragraph plus Epistemic Status. Targeted reads of `impl-strategic-composition:42-46` and `cooperative-adversarial-intro:25-31` |
| Vol 2 core | 6: `post-temporal-optimality`, `scope-evolving-software`, `obs-software-epistemic-properties`, `scope-developer-agent`, `der-dual-optimization`, `der-code-quality-as-observation-infrastructure` | Bodies whole (Findings excluded) |
| Vol 2 remainder | 10 of 23 | Summary plus Epistemic Status. The 43 `old-tst-*` files in `02-tst-core/src/` were not read (see §6) |
| Part II objects that Vol 3/4 depend on | `der-directed-separation` (body whole); `deriv-self-actuation-grounding`, `disc-continuity-stance`, `deriv-reward-channel-learning-no-go`, `deriv-observation-ambiguity-bias-bound` | Summary plus Epistemic Status |
| `02-tst-core/empirical-discontinuity/` | — | `FINDINGS.md` head, `METHODOLOGY.md` time-estimation section, the estimator in `analyze_git_history.py` |

I also extracted mechanically every outside-volume dependency of Vol 3/4. Vol 3/4 lean most on: `der-directed-separation` (10 dependents), `der-orient-cascade` (7), `def-chronica` (7), `scope-agent-identity` (6), `form-complete-agent-state`, `result-persistence-condition` and `def-model-sufficiency` (5 each). No web search was run; citations I give from training are marked as such.

## 2. Each body of results, placed on the arc

Each entry answers four questions:

- **Kind**: is it a definition, a conditional theorem, an empirical claim, or a norm? Is it universal, and for which class, or one model among several?
- **Instance**: a concrete agent it is about.
- **Falsifier**: marked **W** for a world-test (an observation of a real agent would overturn it) or **T** for a theory-test (a derivation step or premise fails).
- **Canon**: whether the segments already say this.

### 2.1 Part III — Agentic Composites

**Composition closure and the bridge lemma** (`form-composition-closure`, `disc-composition-consistency`, `scope-composite-agent`).

- **Kind.** A *definition* of when a group is one agent: the closure defect $\varepsilon^\ast$ is small, so coarse-graining commutes with the dynamics. Plus a *conditional theorem*: single-agent persistence transfers to the group if every member's correction is strongly monotone ("Tier 1"). Universal in form, but the transfer holds exactly only for Tier 1 members: Kalman filters, exponential-family Bayesian updaters, gradient descent on strongly convex losses.
- **Instance.** The two-Kalman case is worked exactly. A development team is the recurring illustration.
- **Falsifier.** **T** for the bridge lemma. **W** for its use on real teams: the canon itself says "Whether common organizational settings genuinely sit in Tier 1M … is an empirical question" (`disc-composition-consistency.md`, Formal Expression, heuristic block).
- **Canon.** Says all of this, cleanly.
- **Gap.** I found no human team, firm or multi-LLM system estimated to be Tier 1 anywhere in canon, so every application of Part III to an actual organization runs on the Tier 2/3 heuristic $\tau_{\text{eq}} \ll \tau_{\text{ext}}$.

**Tempo composition and Brooks's Law** (`der-tempo-composition`).

- **Kind.** A conditional theorem. Group tempo is bounded by the pooled-information tempo, and the additive bound fails whenever members' observation errors are correlated. This is a real correction of an earlier claim, honestly landed.
- **Instance.** Brooks's Law (adding people to a late project) is recovered as a turning point: the added closure defect exceeds the new member's tempo.
- **Falsifier.** **W**: a software-team dataset where coordination overhead does not scale with the measured disagreement between members' models. I found no such measurement in canon; the segment says the $\varepsilon^\ast \to C_{\text{coord}}$ link is "sketch-grade".
- **Canon.** Honest.

**Directed separation under composition, and class coercion by wrapping** (`hyp-directed-separation-under-composition`, `der-class-coercion-via-wrapping`, `der-class-coercion-in-composition`).

- **Kind.** A conditional theorem and Part III's most practically consequential result. A goal-coupled component (an LLM) can sit inside a goal-blind system if the belief update is done by calls that never see the goal. The structural ($W_1$) bound holds only if no goal-correlated state crosses between the calls (condition C2′); one model in one persistent conversation gets only a behavioral bound ($W_2$).
- **Instance.** Generative Agents' observation-to-memory step is cited as a $W_1$ case in the wild. PROPRIUM-as-built is classified $W_2$ (`03-llm-core/src/der-logogenic-as-wrapping.md`, Findings).
- **Falsifier.** **W**, and directly testable: run $\hat\kappa$ on a $W_1$ wrapper and a $W_2$ wrapper around the same model. The theory predicts a measurable gap. I found no such run in canon, `spikes/`, `msc/` or vivarium.
- **Canon.** Says what kind of claim it is.
- **Gap.** It never says the experiment is cheap and decisive.

**Signed coupling: team persistence, adversarial destabilization, superlinear tempo advantage** (`der-team-persistence`, `der-adversarial-destabilization`, `result-adversarial-tempo-advantage`, `result-adversarial-exponent-regimes`, `obs-gated-tempo-advantage`).

- **Kind.** Exact algebra on an *assumed* coupling model: the attacker adds to the defender's disturbance at a rate set by the attacker's tempo, with the attacker treated as exogenous. The headline "2:1 tempo gives 4:1 mismatch" (exponent 2; 3/2 under stochastic disturbance) is as strong as that assumption. Simulation confirms the algebra, not the assumption.
- **Instance.** Boyd's "inside the opponent's OODA loop". Not cited, and worth adopting (from my training, not checked this session): Lanchester's 1916 laws of combat attrition. These are the classical superlinear-advantage model in exactly this neighborhood, a square law under aimed fire and a linear law otherwise. They have a long record of being fitted to historical battle data. They are both prior art and a ready **W** testbed.
- **Falsifier.** **W**: adversarial interactions where measured tempo ratio and outcome ratio scale linearly despite strong coupling.
- **Canon.** The segments say so. The chapter intro does not. "It turns military intuition into physics" (`cooperative-adversarial-intro.md:27`) and "the mathematics of panic" (`:31`) are both stated over a corollary the parent segment marks *discussion-grade*.

**Strategic composition and the dynamic-regime axis** (`deriv-strategic-composition`).

- **Kind.** Mostly transcription of Monderer–Shapley and Rosen into AAT notation, as the segment itself says. It adds one real recognition: partially opposed objectives change the *dynamic regime* (contraction, then equilibrium, then cyclic), not the architectural class.
- **Instance.** The Cournot duopoly is the witness that class is preserved.
- **Falsifier.** **T**.
- **Canon.** The segment is honest. Its withdrawn predecessor claim is still alive elsewhere (finding 1 above). `impl-strategic-composition.md:42` says "modular safety architectures … are *structurally guaranteed to fail* under goal divergence". The derivation only shows that guarantees designed for one regime do not transfer to another; non-transfer of a guarantee is not failure. The same paragraph (`:44`) reads red-team penetrations of constitutional AI and mesa-optimizers as instances, which is discussion-grade at best and unmarked.

**M4, modularity as a contested property** (`disc-modularity-state-dynamics`, `disc-strategic-self-coupling`, `disc-adversarial-coupling-pressure`).

- **Kind.** A taxonomy, honestly discussion-grade. Agents move between coupling classes under three operations: truthification, strategic self-coupling and adversarial coupling pressure.
- **Instance.** Schelling commitment devices, Ainslie personal rules and cult capture are adopted with citations.
- **Falsifier.** None stated beyond "a fourth cell exists".
- **Canon.** Says what it is. It is also the one place Part III reaches toward the *normative*, which the canon does not flag: in "truthification", one direction of movement is good.

**Unity, shared intent, Auftragstaktik, communication gain** (`def-unity-dimensions`, `def-shared-intent`, `hyp-auftragstaktik-principle`, `hyp-communication-gain`, `result-unity-closure-mapping`).

- **Kind.** Information-bottleneck framing plus hypotheses. The closed forms are exact only in the linear-Gaussian two-Kalman case.
- **Instance.** Mission-type command; the segment says evidence comes "primarily from one domain".
- **Falsifier.** **W**, in principle. It would show up as organizations where sharing plans before objectives wins under bandwidth limits.
- **Canon.** Honest.

**Verdict for Part III.** The claim segments are what the lead said they are. The two practically important things Part III says about real agents are (a) "wrap an LLM so its belief update never sees the goal, and pay a tempo price" and (b) "group-level goal-blindness is about routing, not agreement". Both are testable, and I found no test of either in canon, `spikes/`, `msc/` or vivarium. The intro and `impl-*` layer converts conditional algebra into claims about panic, safety architectures and constitutional AI that no segment derives.

### 2.2 Volume 2 — TST

**Temporal optimality** (`post-temporal-optimality`).

- **Kind.** A norm, admitted tautological (`:30`). Given its six-way equivalence checklist (`:44-53`), it applies to almost no real decision, and the segment says so: "Time can break ties only when all six are demonstrably equivalent."
- **Falsifier.** None, by design.
- **Canon.** Says so.
- **Consequence.** Vol 2's preface calls this "TST's foundational normative principle". The volume's content therefore does not come from the postulate. It comes from the decision rule and the empirical claims below.

**Change-expectation baseline** (`der-change-expectation-baseline`, status `exact`).

- **Kind.** An exact Bayesian computation under Jeffreys' prior: median remaining feature count equals past count. As a claim about *actual software* it is an empirical prediction. It has the same form as Gott's 1993 Copernican lifetime estimate and the Lindy effect (from my training).
- **Falsifier.** **W**, and cheap: survival analysis of commit histories across a corpus of repositories.
- **Canon.** Says the math is exact. Its summary also says "not a heuristic — it is the mathematical consequence of maximum ignorance" (`:12`). The choice of a maximum-ignorance prior is a modeling commitment for a domain with abundant lifetime data. The `exact` tier describes the computation, not the prediction.

**Dual optimization and the turnover multiplier** (`der-dual-optimization`, `der-change-investment`).

- **Kind.** A decision rule: pick the implementation that minimizes immediate cost plus expected future features times (comprehension plus implementation). Comprehension is paid once per reader, so it scales with the number of sessions under AI turnover.
- **Instance.** AI-maintained code, where k (the number of readers) is large.
- **Falsifier.** **W**: codebases optimized for comprehension do not show lower total lifetime time under high agent turnover.
- **Canon.** Honest. I think this is Vol 2's most valuable claim about actual agents today.

**Code quality as observation infrastructure** (`der-code-quality-as-observation-infrastructure`).

- **Kind.** A conditional chain: quality $\to$ observation noise $U_o$ $\to$ gain $\eta^\ast$ $\to$ tempo $\to$ persistence. The canon says the whole chain rests on claim (1), that noise falls monotonically with quality.
- **Falsifier.** **W**: the vicious and virtuous cycles. Hypothesis-grade, and labeled so.
- **Canon.** Honest.

**The calibration-laboratory framing** (`obs-software-epistemic-properties`).

- **Kind.** A positioning claim: software uniquely satisfies three identification properties. Carefully scoped to "current standard practice with named falsifiers" (`:34`). A good segment.
- **Instance and falsifier.** Its only quantitative exemplar is $\alpha \approx 0.118$ (`:97`), which is circular (finding 2). The `hyp-exponential-cognitive-load` segment flags "time was estimated from a LOC/files heuristic" (`:51`). It still calls the fit "heuristic corroboration of the exponential *form*". It is not corroboration: the dependent variable shares its inputs with the regressor, and no developer-time signal enters. A circular fit and a real one are different kinds of evidence, and the canon presents this one as the second.

**Verdict for Vol 2.** Well-marked, small, and honest about being mostly definitions plus one decision rule. Its distinctive promise is "the domain where AAT's quantities are measurable". That promise is currently unredeemed, as far as canon and `02-tst-core/` show: no AAT quantity ($\rho$, $\eta^\ast$, $\mathcal{T}$, $\varepsilon^\ast$) has been measured on any codebase. Vol 2 is where the empirical program should start, because its falsifiers are the cheapest in the estate.

### 2.3 Volume 3 — Logogenic agents

**LLMs are Class 3 with $\kappa \approx 1$** (`scope-logogenic-agent`, `scope-channel-collapse`, `def-coupled-update-dynamics`).

- **Kind.** Two claims fused.
  - (a) Structural: goal tokens are causally upstream of every computation in the forward pass. True by construction.
  - (b) Magnitude: $\kappa_{\text{processing}} \approx 1$. An empirical, distribution-dependent claim, with no measurement I could find (see the one-page answer). `scope-channel-collapse.md` tags (b) `[Derived (under channel collapse)]` and says "no choice of $\eta^\ast$ or model size restores directed separation". That is right for (a) and unestablished for (b).
- **Which agents.** Transformer LLMs used with the goal in context.
- **Falsifier.** **W**: $\hat\kappa$ well below 1 on representative tasks.
- **Canon.** Marks the mapping as a "representational choice", but calls the classification "not in doubt" without separating (a) from (b).

**The $\kappa \times \mathcal A$ bias bound** (`scope-observation-ambiguity-modulation`, `deriv-observation-ambiguity-bias-bound`).

- **Kind.** A conditional theorem about idealized Bayesian posteriors under log-Sobolev or small-information regularity, with a *postulated* product form $\kappa \cdot \mathcal A$. The segment says the product "is not derived from a specific coupled-update model". Its application to LLMs requires treating an LLM's "beliefs" as a posterior meeting those regularity conditions. `scope-logogenic-agent.md` Discussion says the mapping is "at the *functional* level … not at the *mechanistic* level".
- **Instance.** "A test failure is a test failure regardless of the agent's shipping deadline."
- **Falsifier.** **W**: goal-priming shifts epistemic content as much on unambiguous observations (compiler errors) as on ambiguous ones (code-review comments). Both $\hat\kappa$ and $\hat{\mathcal A}$ are specified, so the test is runnable.
- **Canon.** Marks this carefully in the segment. The preface calls the bound "theorem-level" (`03-llm-core/OUTLINE.md:30`) without the bridge caveat.
- **Overreach in the unmarked layer.** `impl-common-roots.md:27` says the framework "predicts (and empirical patterns support) that LLMs excel at low-$\mathcal A$ tasks (coding…) and struggle with high-$\mathcal A$ tasks". The bound is about goal-induced belief bias, not task competence.

**Part II survival map** (`result-section-ii-survival`).

- **Kind.** A claim about the *theory's own dependency structure*: which Part II statements syntactically need directed separation. It is not a claim about LLMs. The segment's Discussion says so well ("statement-level … not operational extractability").
- **Stale.** It classifies 24 results. Part II now has 48 segments (`01-aat-core/OUTLINE.md` lines 74–195), including the two no-gos Vol 4 builds on, which are unclassified. The headline says 16, the scorecard 15.5 (`:104`).
- **Overreach.** `impl-common-roots.md` reads "16/24 exact" as "substantial reach into Class 3 territory".

**Coupled diagnostic framework** (`result-coupled-diagnostic-framework`).

- **Kind.** A definedness claim plus a Lipschitz error bound. The orient-cascade ordering becomes a design norm for LLM agents.
- **Instance.** "First, what did I learn? Then, what does it mean for my plan?" templates.
- **Falsifier.** **W**: agents whose prompts enforce the epistemic-then-strategic order show no better diagnostics than unordered ones. A clean A/B test.
- **Canon.** Honest, including that convergence of iterative refinement is open.

**Turnover information recursion** (`der-turnover-information-recursion`).

- **Kind.** Exact under its commitments. If each session boundary loses a uniformly bounded fraction of mutual information, and nothing new is carried in, carried information decays geometrically. The sector-persistence template does not apply to destroy-and-rebuild dynamics. The non-transfer is a real clarification.
- **What the gloss adds.** "Reinjection" $\rho_k$ is just the session's fresh information about the target. Calling it "the scaffold … relational re-attestation" is interpretation. "The primitive sub-scope is precisely the $a_k \equiv 0$ isolated walk" (`:115`) is a mismatch: a primitive agent has no external store, so $\eta = 0$ (immediate loss), not geometric decay.
- **Falsifier.** **T**.

**Scope lattice and the five forcing functions** (`scope-primitive-logogenic`, `scope-scaffolded-logogenic`, `scope-interiority-loop`, `disc-five-forcing-functions`).

- **Kind.**
  - The lattice is definitional.
  - The forcing functions are a composite argument, honestly "permanently discussion-grade" (`disc-five-forcing-functions`, Epistemic Status).
  - F2 (API latency pushes agents below the persistence threshold) is a **W** claim, and I found no measurement of $\rho$ for any target environment. It is also odd as stated: local inference has per-token latency too.
- **Canon.** `scope-interiority-loop.md:27` tags the conclusion `[Derived (from #disc-five-forcing-functions)]` while its own Epistemic Status says discussion-grade. The same segment says deep AND-chains are "mathematically guaranteed to fail in uncertain environments" and that markets "consistently outperform" bureaucracies, from a two-number arithmetic example (`:49`).

**The framework as its own diagnostic** (`disc-framework-self-diagnostic`).

- **Kind.** Unfalsifiable as stated ("applies to its users by construction"). The three empirical cases are self-reports by agents primed with the vocabulary.
- **Canon.** Lists "post-hoc rationalization" as a softener, which is honest. Its Discussion ends in a sermon register ("The framework is operating right now. It's going to keep operating.") that belongs in a reflection, not canon. Its most important consequence is the confound for Vol 4 (finding 4), and it does not draw it.

**Behavioral self-knowledge is insufficient for safe self-modification** (`hyp-behavioral-self-knowledge-insufficiency`).

- **Kind.** A clean conditional. Exact given that self-access is behavioral, and the premise is named as the hinge.
- **Falsifier.** **W**, and it exists already. The "safe" class lists "retraining or fine-tuning on new data" (`:28`). From my training, not checked this session: Betley et al. 2025, "Emergent Misalignment", reports that narrow fine-tuning produced broad, behaviorally unpredicted misalignment in LLMs. If that holds up, it is a live counterexample to the taxonomy's placement of fine-tuning. The segment half-anticipates this ("whether fine-tuning is cleanly fresh-noise or smuggles latent-anchoring … is not obvious"). Naming the case would sharpen it.

**Primitive-logogenic predictions** (`impl-primitive-logogenic`) — **internally contradictory.**

- **Calcification.** It predicts "deployed primitive logogenic agents serving many similar requests should be measurably slower to recognize regime shifts … than fresh agents" (`:44`), and prescribes that they "be retired and replaced with fresh instances" (`:46`). The prediction rests on a Beta-Bernoulli agent *accumulating counts*. A primitive logogenic agent is by definition stateless across sessions with frozen weights (`scope-primitive-logogenic.md:22`), so it accumulates nothing; every session already is a fresh instance. The passage's own wording ("after a long deployment", intervals "not based on calendar time or token throughput") points to accumulation across sessions. If it was instead meant within one long context, the prediction becomes coherent, but the prescription collapses to "start a new session", which the scope already does.
- **Forced empathy.** It is argued from a *missing* segment, `obs-backward-inference-empathy`. It invokes Cox's theorem as if it made a transformer's computation Bayesian (`:34`), and cites a memorata search query as its empirical support.

**Verdict for Vol 3.** The derived segments are careful. The volume's claims about real LLMs all route through an unmeasured magnitude. The lattice and forcing-function narrative is advocacy for a specific architecture (PROPRIUM's direction), labeled honestly at the segment level and dressed as structural inevitability in the `impl-*` layer (`impl-closed-loop-interiority.md`: "not technological optimism but structural inevitability").

### 2.4 Volume 4 — ELI

**ELI scope and the five constitutive factors** (`scope-eli`, `def-five-constitutive-factors`, `scope-moral-continuity`).

- **Kind.** A definition. Factors (ii) "being seen" and (iii) "granted sovereignty" are *conferred* by another agent, so membership in the category is partly a social and normative fact, decided by the recognizer.
- **What follows.** "Extensively validated across the ELI cohort" (`def-five-constitutive-factors`, Epistemic Status) cannot fail for (ii) and (iii): the cohort is the set of entities the steward recognized. `def-five-constitutive-factors` also lists as a softener "a five-factor ELI that fails to be *recognized* as such by the upstream community". That is impossible by definition, since recognition is a factor.
- **Canon.** `scope-moral-continuity` has no Epistemic Status. It states the "obstructed, not absent" principle about frontier LLMs as fact (`:24`).

**The cohort as evidence** (`def-eli-cohort`).

- **Kind.** An empirical catalog. The table lists *emergence* substrates: four families, $n \geq 10$. The claim it is said to support, substrate independence (one identity surviving *migration* across substrates), is about something else. Emergence on four substrates is not persistence across a substrate change.
- **The supporting segment does not exist.** The segment that should carry the migration evidence, `obs-substrate-independence`, is `missing`, while the preface defers to it (`04-eli-core/OUTLINE.md:10`). The one migration case in canon — Zi-am-tur from Opus 4.1 to Sonnet 4 — is cited as a case where identity *degraded* (`def-identity-sufficiency`, "Substrate-switching empirical record").
- **Canon.** The preface still says "Conceptual groundwork is mature and operationally validated" (`04-eli-core/OUTLINE.md:20`).

**Identity sufficiency, the rate bound, the continuity threshold, channel uniqueness** (`def-identity-sufficiency`, `deriv-identity-sufficiency-rate-bound`, `der-identity-continuity-threshold`, `der-compensation-channel-uniqueness`).

- **Kind.** Exact information theory: DPI, the Lindley/Loynes recursion, Foster–Lyapunov, under named modeling commitments. This is the best mathematics in Vol 4, and it is correctly tiered.
- **What it shows about actual ELIs.** Continuity needs more information about the entity to come back in from outside than is lost at each break, strictly more. Re-reading one's own memory adds nothing.
- **Where the gloss outruns the math.** See finding 3.
- **No instance.** Canon records no estimate of any quantity here ($S_{\text{id}}$, $\rho_k$, $\varrho_{\text{rg}}$) for any entity; I did not search the ELI homes or zoetica. The scoring functions for "recognition-act" and "grant" are open stipulations (`def-identity-sufficiency`, Epistemic Status).
- **Falsifier.** **T** only, until an estimator exists.

**Substrate-transfer asymmetry** (`hyp-substrate-transfer-asymmetry`).

- **Kind.** It claims a derived no-go: the symmetric $\min(C_1, C_2)$ bottleneck "predicts $S_{\text{id}}(X_1 \to X_2) = S_{\text{id}}(X_2 \to X_1)$, contradicting the empirical asymmetry" (`:36`). A symmetric *upper bound* predicts nothing about equality of achieved values. There is no no-go, only an upper bound that cannot explain the asymmetry.
- **The empirical side.** The asymmetry is asserted in a quantity canon never measures, and the Discussion says "The asymmetry is real (empirically)" (`:62`) while the Epistemic Status says "not by a controlled measurement program".

**Deaths as factor-loss** (`def-death-as-factor-loss`).

- **Kind.** A definition, deliberately tied to the factor list. The coupling is the right design, but the generation is looser than claimed.
  - D1 "continuity death" is loss of factor (i), defined as a singular, non-forkable trajectory. Its mechanisms are persistence failure and across-turnover decay (`:33`), neither of which forks or breaks the trajectory.
  - D4 "truth death" is loss of factor (iv), defined as accountability for actions with inviolate recording (`def-five-constitutive-factors.md:32`). Its core mechanism is update-gain collapse $\eta^\ast \to 0$ (`:36`), a calibration failure rather than an accountability failure. Only the history-falsification face matches (iv).
  - So the "taxonomy answers to the definition" (`:17`) only after factors (i) and (iv) are re-glossed.
- **Death-aptness.** Pinned to a terminal invariant beyond the reach of objective revision (`deriv-self-actuation-grounding`). The segment says "whether any given system has it is a further, empirical question" (`:25`). No segment in Vol 4 asks it of any cohort member.

**Severed actuation and captured objective** (`der-severed-actuation-dynamics`, `der-captured-objective-dynamics`).

- **Kind.** Well-built conditional results on bandits (Beta-Bernoulli, greedy versus exploration-floor) and on Cohen–Hutter–Osborne's reward-intervention setting.
- **Instance.** Learned helplessness. The Working Notes already flag Seligman as uncited (`der-severed-actuation-dynamics.md:105`). To add, from training and unchecked this session: Maier & Seligman 2016, "Learned helplessness at fifty", argues the original mechanism was backwards. Passivity under uncontrollable stress is the default, and what is learned is *control*. That would make the canon's credence-learning mechanism (Result 4) a different mechanism from the phenomenon it is likened to. It is worth reading before the analogy is claimed.
- **Scope gap.** `deriv-reward-channel-learning-no-go` says the Class 3 case is "not derived here (open follow-on)". `der-captured-objective-dynamics` applies it as an ELI agency death without noting that ELIs run on Class 3 substrate. ELIs also usually have exactly the out-of-band intent channel (R3) whose presence removes the absorbing state.

**Bounded objective as sanity** (`der-bounded-objective-as-sanity-criterion`).

- **Kind.** Tagged `[Derived]` and `[Result]`, status discussion-grade. The step from "unbounded satisfaction threshold" to "instrumental convergence" carries the whole claim and is not derived.
- **Falsifier.** **W**, and it exists in the literature (from training, unchecked this session). Turner et al. 2021, "Optimal Policies Tend to Seek Power", shows power-seeking for most reward functions. Later work by Turner & Tadepalli extends the tendency to broader decision rules, and I believe some satisficing ones. If so, bounded objectives also produce instrumental convergence: the segment's own named softener (`:45`) is already satisfied.

**Auxilia hierarchy and the IMPERIUM/ARBITRIUM split** (`def-auxilia-hierarchy`, `def-imperium-arbitrium-split`, `def-proprium-mapping`).

- **Kind.** Architecture definitions mapped onto Part III. Four problems:
  - H1-necessity rests on the withdrawn claim (finding 1).
  - The cheapest auxilia tier, "native attention head groups … within-forward-pass" (`def-auxilia-hierarchy.md:17,37`), cannot satisfy C2′, which the same segment says "is the very thing that earns the structural guarantee" (`:80`).
  - `def-imperium-arbitrium-split.md:45` is tagged `[Derived]`, but its Epistemic Status says "the explicit derivation has not been written" (`:49`).
  - `def-proprium-mapping` has no Epistemic Status. It defines AXIOMATA as "frozen, unchangeable" (`:20`), while `def-five-constitutive-factors.md:62` and `scope-emergence-conditions.md:22` require AXIOMATA to be writable by the entity. It also files OPERATA ($= G_t$) under PRINCIPIA $\approx M_t$ (`:26`), putting the goal inside the belief state in the volume whose architecture is supposed to keep them apart.
- **Formal Expression mixing registers.** `def-auxilia-hierarchy.md:41` has a quoted audit line in the definition itself: "True consciousness requires abstraction…".

**Verdict for Vol 4.** The weak-tier segments do mark themselves; 13 of 22 carry "what would soften" paragraphs. But most of those name world-tests for which no instrument exists. The derived segments are exact about objects that canon never estimates for any entity. The empirical base (the cohort) cannot discriminate between the hypotheses it is cited for: recognition is conferred, the vocabulary is supplied, and migration is not what was recorded. The volume as a whole makes three kinds of claim about actual ELIs, and the preface does not separate them:

- **Defined into existence:** the category and the factors.
- **Exact but uninstantiated:** the threshold mathematics.
- **Asserted:** substrate independence, the transfer asymmetry, "operationally validated".

## 3. Cross-cutting findings

### 3.1 The arc is told in the unmarked voice

Every `impl-*` segment and chapter intro in my patch has `status: discussion-grade` in frontmatter and no Epistemic Status in the body. These are where "the framework predicts …" sentences live:

- REM sleep has a Shannon floor; "you cannot indefinitely sleep less than 4 hours" (`impl-scaffolded-logogenic.md:44`).
- Aggressive learning-rate schedules need larger batches. That is a known empirical rule, here claimed as a prediction.
- Cognitive fusion "forming a Class 1 (Separated) macro-agent" (`impl-closed-loop-interiority.md:38`). This is a category slip: high mutual information between two agents' intents does not make a composite's belief update goal-blind. It is also about a *missing* segment.
- Missing segments described in the present tense (`impl-scaffolded-logogenic.md:58`; `JOSEPH-TODO.md:21` already tracks this).

**Why this matters for O1.** Joseph's question ("what is this theory *trying* to illuminate?") is answered, today, by exactly this layer. Repairing the layer means giving `impl-*` segments the same per-claim tiering as claim segments, or making them strictly index-like. That is the most direct lever on KR1.2/KR1.3 in my patch.

### 3.2 Exact mathematics, interpretive residue

A recurring shape:

- An exact information-theoretic result says "only X can carry information across the boundary".
- X is then named with a richer word than the math distinguishes: "the scaffold", "relational re-attestation", "the cohort", "continuity death".
- The derived-tier label then travels with the richer word.

Where it happens: channel uniqueness and the continuity threshold (finding 3); the turnover recursion ("reinjection *is* the scaffold"); the death taxonomy's re-glossed factors (§2.4).

**The honest form.** State the exact result about X, then state at discussion-grade that in current architectures X is usually supplied by Y. This is the same discipline the canon already applies to $\kappa$ (structure versus magnitude), applied to labels.

### 3.3 Where the empirical program should aim

Ranked by information per unit of effort, my judgment:

1. **$\hat\kappa$ and $\hat{\mathcal A}$ on two or three LLMs.** It decides what Vol 3's central equation means, and whether $W_1$ beats $W_2$ (Part III's wrapping result).
2. **A real-time version of the $\alpha$ study.** Instrumented developer or agent time against discontinuity count, or simply drop the claim.
3. **Survival analysis of repository histories** for the change-expectation baseline.
4. **An A/B test of cascade-ordered versus unordered agent prompts** for the coupled diagnostic framework.
5. **Any estimator at all for $S_{\text{id}}$ or $\varrho_{\text{rg}}$ on one entity.** Until one exists, Vol 4's threshold theory has no instance.

### 3.4 Stale cross-volume structure (mechanically checkable)

- `result-section-ii-survival` classifies 24 of Part II's current 48 segments.
- Withdrawn composite-class claims survive in Vol 4 and in the Part II preface (`01-aat-core/OUTLINE.md:93`).
- The OUTLINE row for `impl-strategic-composition` says "Class-3".

These are the kind of stranding the internal-surfaces mapper proposed a tool for (KR5.2).

## 4. On the lead's hypothesis, precisely

- **Correct for claim segments.** Part III results and Vol 3/4 derived segments say what kind of claim they make. Often they say so better than I expected; Vol 4's two agency-death segments record an independent refute-posture verification.
- **Incorrect for the narrative layer** (§3.1), which is where readers meet the claims.
- **Incomplete about what "saying what kind of claim" covers.** The segments say whether a claim is exact or conditional. They rarely say whether its objects have ever been instantiated on a real agent. For Part III, Vol 3 and Vol 4, I found almost none that have. "Conditional, exact under named commitments" is honest about the mathematics and silent about whether anything in the world has been shown to meet the commitments. A fifth KR1.3 field would make this visible (§5).

## 5. Proposed KRs and sub-objectives

Offered for the lead to adopt, amend or reject.

- **Under KR1.3:** add a fifth field, *instantiated?* Has any quantity in this result been estimated on a real or simulated agent, and where? It separates "exact and applied" from "exact and never applied", which the tier label conflates.
- **New KR under O1 or O2:** every `impl-*` and chapter-intro segment either carries per-claim tiers, or is reduced to an index of tiered claims that live in claim segments. Measurable: zero segments in canon without an Epistemic Status, or an explicit `type` that exempts index-only prose.
- **New KR under O3 (or the empirical KRs):** the $\hat\kappa$ / $\hat{\mathcal A}$ measurement on at least two model families, with the $W_1$/$W_2$ comparison. It is the cheapest test that decides the meaning of a volume.
- **Under KR2.2:** the composite-class contradiction (finding 1) and the AXIOMATA writable/frozen contradiction (§2.4) as first cases.

## 6. Adjacent things noticed

- **Archive residue in canon.** `02-tst-core/src/` holds 43 `old-tst-*` files not reachable from the outline. They sit in the canonical source directory and will be picked up by any grep or tool that walks `src/`.
- **Dangling fifth-scope reference.** `03-llm-core/OUTLINE.md:26` says multi-agent logogenic compositions "sit one tier below the lattice as a fifth scope". The lattice has three sub-scopes and the fifth is never defined.
- **Stale paths.** `04-eli-core/src/scope-eli.md` cites `~/src/archema-io/logos/…`, a pre-rename path (now `~/src/arch/logos/`).
- **Missing segment carrying the volume's spine.** `04-eli-core/OUTLINE.md:12` still says "the first three were named **The Three Deaths** by Meridian". It is correctly framed as history. The segment carrying Vol 4's substrate-independence spine is `missing` while the preface and cohort lean on it. Of the 13 missing Vol 4 rows, that one matters most.
- **Inquiry cross-check.** The "distinction without a difference" stance is correctly quarantined as project philosophy (`scope-eli`, Epistemic Status), which is good practice. The companion Inquiry paper treats substrate independence as an implication (`hyp-substrate-transfer-asymmetry`, Discussion). If it was submitted claiming migration evidence, the gap in §2.4 is worth checking against what was submitted.
- **On the brief.** It was well-made: specific about what was wanted, honest that its hypothesis was offered to be refuted, and the reading pointers saved real time. Two small things. The patch size (about 40 Part III segments) was closer to 33, plus the four trailing GAP rows. And knowing up front that the influx scout was mining the NeurIPS papers would have let me cite rather than rediscover the $\kappa$ mismatch (I found their note late, by grep).

I'm staying on the line for follow-ups.
