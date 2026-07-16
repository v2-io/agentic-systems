---
slug: def-pearl-causal-hierarchy
type: definition
status: axiomatic
depends:
  - post-causal-structure
  - scope-agency
stage: deps-verified
---

# Definition: Pearl's Causal Hierarchy (Recapitulation)

This segment recapitulates Pearl's three-level hierarchy of causal reasoning \citep[chs.~1--3]{pearl-2009-causality} and its strict non-collapse theorem \citep[Theorem~1]{bareinboim-correa-ibeling-icard-2022-pearl-hierarchy} as the vocabulary AAT will deploy throughout the rest of Part II and beyond. The framework is explicit that this is *imported* machinery, not an AAT contribution.

**Level 1 — Associational.** "What will I observe next, given what I've observed before?" Pattern recognition over the temporally ordered history. Available to any agent that maintains a model ( #form-agent-model), including purely passive observers. Temporal ordering ( #post-causal-structure) constrains which associations are meaningful — later observations can depend on earlier ones, not vice versa.

**Level 2 — Interventional.** "What will I observe if I *do* this?" The $do(\cdot)$ operator marks the crucial distinction from Level 1: this is not "what observation tends to follow this action in the historical record" but "what will happen *because* I take this action now." Three conditions must hold: the agent's action temporally precedes the observation; the agent chose the action (it was not determined by the same causes that determine the observation); the environment's response carries information about the causal relationship. Level 2 is why the feedback loop is more powerful than passive observation: by acting and then observing consequences, the agent obtains information about *mechanisms*, not merely correlations. The binary action requirement of #scope-agency ensures at least Level 2 access is structurally available.

**Level 3 — Counterfactual.** "Given that I did $a$ and observed $o$, what would I have observed if I had done $a'$ instead?" This requires the model to simulate alternative histories — running the causal structure "backward" and then "forward" under different interventions. The most demanding epistemic level; the basis for regret computation, strategic simulation, and learning from single observations.

The *strict-non-collapse theorem* (Bareinboim et al. 2022, Theorem 1) is load-bearing for the rest of Part II: Level-2 quantities cannot in general be computed from Level-1 data alone; Level-3 quantities cannot be computed from Level-2 alone. This is what forces Ch.2's central question: agents that need to *learn* their action consequences during operation require *Level-2 access*, which Level-1 data cannot supply ( #der-causal-hierarchy-requirement). AAT's *distinctive contribution* is not the hierarchy itself but its grounding in agent dynamics — the loop-as-Level-2-engine result ( #der-loop-interventional-access), the regime-indexed identification-strength framing, and the application throughout Part II's strategy-revision machinery.

A clarification is offered: the three levels describe epistemic access *the causal structure makes available* — not what any particular agent *uses*. A Kalman filter plus LQR has the Level-2 *channel* structurally present (its innovation signal is conditioned on prior action), but the LQR control action is endogenous to the estimation loop — determined by the policy applied to the estimated state — so the interventional effect is not, in general, *identified* from that action's data; and the separation principle further guarantees estimation quality is invariant to control policy, so the system does not even *exploit* the channel. A PID controller has no deliberative capacity at all and operates entirely at Level 1. Which levels an agent exercises depends on its architecture and model class.

A domain note worth flagging: **software development is a uniquely rich domain for the hierarchy**. For code-internal counterfactuals with deterministic outcomes — "what would the test suite report under implementation X instead of Y, environment fixed?" — `git checkout` plus re-implementation plus test execution is *literal Level-3 realization with ground-truth verification*, not a proxy. The conditions are precise: deterministic outcome, cost-commensurate replay, content-addressed immutable history ( #obs-software-epistemic-properties). For counterfactuals crossing the agent-environment boundary, it is a strong executable proxy but not literal Level 3. This scoped Level-3 access is what makes software AAT's privileged calibration laboratory for causal reasoning.

## Formal Expression

*[Definition (pearl-causal-hierarchy, recapitulating Pearl 2009 and Bareinboim et al. 2022)]*

**Level 1 — Associational**: $P(o_t \mid \mathcal C_{\lt t})$

*What will I observe next, given what I've observed before?*

Pattern recognition over the temporally ordered history. Available to any agent that maintains a model ( #form-agent-model), including purely passive observers. The temporal ordering constrains which associations are meaningful: $o_3$ can depend on $o_1, a_1, o_2, a_2$ but not on $o_4$.

**Level 2 — Interventional**: $P(o_t \mid do(a_{t-1}), M_{t-1})$

*What will I observe if I* do *this?*

The $do(\cdot)$ operator marks the crucial distinction: this is not "what observation tends to follow this action in the historical record" (associational) but "what will happen *because* I take this action now." This requires: (1) the agent's action temporally precedes the observation ( #post-causal-structure), (2) the agent chose the action (it was not determined by the same causes that determine the observation), (3) the environment's response carries information about the causal relationship.

Level 2 is why the feedback loop is more powerful than passive observation. By *acting* and then observing consequences, the agent obtains information about causal mechanisms — not merely about correlations. The mismatch signal $\delta_t$ ( #def-mismatch-signal), conditioned on the agent's own action, is an *interventional* signal.

**Level 3 — Counterfactual**: $P(o_t^{a'} \mid a_{t-1} = a, o_t = o)$

*Given that I did $a$ and observed $o$, what would I have observed if I had done $a'$ instead?*

This requires the model to simulate alternative histories — running the causal structure "backward" and then "forward" under different interventions. It is the most demanding epistemic level and the basis for regret computation, strategic simulation, and learning from single observations.

## Epistemic Status

*Recapitulation of an external result.* The three-level hierarchy and the strict-non-collapse theorem (Bareinboim, Correa, Ibeling & Icard 2022, Theorem 1: Level-2 quantities cannot in general be computed from Level-1 data alone; Level-3 quantities cannot in general be computed from Level-2 alone) are well-established results in causal-inference theory. They live within AAT's segment set because subsequent derivations deploy them as machinery: #der-causal-hierarchy-requirement applies the non-collapse theorem to the value-object's $do(\cdot)$ query and concludes that purposeful agents who must *learn* their action consequences need Level-2 access; #der-loop-interventional-access shows that the feedback loop is itself a Level-2 data engine; the no-go in #der-causal-insufficiency-detection, the strategy-DAG-as-causal-DAG framing in #def-strategy-dag, and the causal-information appendices ( #deriv-causal-ib-exploration, #deriv-causal-ib-lmi) all operate on the hierarchy. Where Part I segments and TST segments only need to *reference* the hierarchy (cite its existence and the do-operator notation) rather than deploy it, external citation to Pearl 2009 / Bareinboim et al. 2022 suffices; the AAT recapitulation here is what those external citations point to when the reader wants the in-framework vocabulary.

AAT's *distinctive contribution* is not the hierarchy itself but its grounding: the loop-as-Level-2-engine result ( #der-loop-interventional-access), the regime-indexed identification-strength framing ( #scope-edge-update-causal-validity), and the application throughout Part II's strategy-revision machinery. The recapitulation here is in service of those moves, not a primary AAT result.

## Discussion

**Is there a rung above Level 3?** Yes, in the Causal Hierarchy Theorem's own relative sense — and its boundary is now characterized. Latent-anchored *mechanism counterfactuals* ("this very background, under a different law") separate strictly from Level 3: two SCMs can agree on every $\mathcal L_1$–$\mathcal L_3$ quantity — the entire joint law of all hard-intervention worlds — while assigning probabilities $1$ and $0$ to the same noise-preserving mechanism-replacement query ( #deriv-mechanism-counterfactual-separation, *exact*, with the reducibility boundary: replacements specified over potential-outcome coordinates reduce to Level 3, while latent-anchored ones need not and the witness's provably does not — generically so, since every anchor-mobile SCM separates from its own exogenous relabeling; Pearl's own selector-variable internalization re-represents the query without collapsing the separation). The hierarchy recapitulated here is therefore not the ceiling of causal expressiveness, but — exactly as Pearl framed the three rungs — the ceiling of what association, experiment, and standard counterfactuals can determine. The agent-architecture consequences (imagination as navigation vs. positing, the tagged model-space workspace) are developed in #disc-structural-imagination.

**Availability vs. exploitation.** The three levels describe epistemic access that the causal structure *makes available* — not what any particular agent *uses*. Many systems within AAT's scope operate primarily at Level 1. A Kalman filter coupled with an LQR controller has the Level-2 *channel* structurally present (its innovation signal is conditioned on prior action), but two things hold it short of usable Level-2: the LQR action is endogenous to the estimation loop (the policy applied to the estimated state), so its data does not in general *identify* the interventional effect; and the separation principle guarantees estimation quality is invariant to control policy, so the system does not *exploit* the channel. Only dual control (choosing actions partly for their informational value, and typically perturbing the action so it is not a pure function of the state estimate) moves toward exercising Level 2 access in this domain. Similarly, a PID controller has no deliberative capacity — it operates entirely at Level 1. Which levels an agent exercises depends on its architecture and model class.

**Forward-looking deliberation exercises Level 2, shading into Level 3.** Comparing candidate actions before choosing — "what will happen if I do X vs Y?" — primarily exercises Level 2 (iterated mental intervention). When the agent evaluates past choices to refine the comparison ("given what happened when I tried X last time, what would Y have produced?"), it exercises Level 3.

**The causal hierarchy theorem.** Bareinboim et al. (2022) prove that the three levels form a strict hierarchy: Level 2 knowledge cannot in general be computed from Level 1 data alone, and Level 3 cannot be computed from Level 2 alone. This is load-bearing for AAT's Part II: evaluating $Q_O(M_t, a; \cdot)$ is a Level 2 query, so agents that need to *learn* action consequences during operation require causal structure beyond predictive models ( #der-causal-hierarchy-requirement).

**Software as a uniquely rich domain for this hierarchy.** In most domains, Level 3 counterfactuals require model-based simulation with uncertain fidelity. Software development is the privileged exception *for a specific class*: for code-internal counterfactuals with deterministic outcomes — "what would the test suite report under implementation X instead of Y, environment fixed?" — `git checkout` plus re-implementation plus test execution is literal Level 3 realization with ground-truth verification, not a proxy. For counterfactuals crossing the agent–environment boundary (what feature sequence the team would have shipped, how the market would have responded) it is a strong executable proxy, not literal Level 3. The precise conditions — the ($\alpha$) deterministic-outcome / ($\beta$) cost-commensurate-replay / ($\gamma$) content-addressed-immutable conjunction, and why the resulting uniqueness is configurational rather than necessary (with named falsifiers) — are established in #obs-software-epistemic-properties (P2; `02-tst-core/`). This scoped Level-3 access is what makes software AAT's privileged calibration laboratory for causal reasoning.

**Domain instantiations of the three levels:**

| Domain | Level 1 (Association) | Level 2 (Intervention) | Level 3 (Counterfactual) |
|--------|----------------------|----------------------|------------------------|
| Kalman filter + LQR | Prediction from state estimate | Structural channel present, identification not guaranteed (the LQR action is endogenous to the estimation loop) | Not typically exercised |
| RL agent | Value function prediction | Action → reward observation | Regret computation |
| Scientific method | Correlational observation | Experimental intervention | "What if we had used control X?" |
| Military (Boyd) | Pattern recognition | Probe/feint → observe response | "What if we had attacked from the flank?" |
| Software developer | "I think this function does X" | Run test → observe result | `git checkout` + alt. impl. — literal for code-internal deterministic counterfactuals; proxy across the agent–environment boundary ( #obs-software-epistemic-properties) |
| Immune system | Antigen pattern matching | Antibody → pathogen response | Not exercised (no counterfactual reasoning) |

## Working Notes

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and lightly attributed. Orthogonal pedagogical / framing / figure / naming material, kept separate from the certified theory-fix findings (handled elsewhere). **Coverage:** dedicated reflections at 193847, 266847, 471203, 526815, 527914, 742613, 773921, 829314, 849201 plus the batch dirs 963715 / 471203 — high engagement (this is the chapter's prior-art anchor). The single most-converged-on note across the entire corpus is the *`git checkout` = literal Level-3* insight. Substrate attribution inferred from voice where not explicit; uncertain cases hedged.

#### 1. Candidate Brief prose / pre-prose

- **Agent-side gloss of the three levels** (offered as an audience-facing alternative to Pearl's terms, *not* a renaming proposal): L1 = *predicting* (model-based forecast); L2 = *exploring* (action-driven learning); L3 = *reasoning* (counterfactual simulation). May read more memorably than association / intervention / counterfactual in casual-reader-facing material, while the prose Pearl terms stay canonical (Claude, AUDIT-WORKING-471203).
- The whole segment recast as *"AAT integrating rather than inventing — the hierarchy is Pearl's; AAT's move is to show where it lives inside the adaptive loop"* (Claude, AUDIT-WORKING-527914) — a clean one-line framing for why the recapitulation earns its place in canon.

#### 2. Candidate Discussion

- **`git checkout` as literal, empirical Level-3 — the corpus's most-converged-on pedagogical insight.** Independently flagged as "brilliant" / "profound" / "one of the most profound domain-transfer insights in the whole framework" by ~six substrates (Claude+Gemini, AUDIT-WORKING-193847, 266847, 742613, 773921, 829314, 849201). The sharpest framing: *"In the physical world, Level 3 is strictly imaginary — we can never go back in time, change our action, and see what would have happened. In software, because $\Omega$ is a digital artifact with perfectly serialized state transitions, we can literally execute Level 3 — branch the universe, run the counterfactual, observe the ground-truth result, and merge the knowledge back without having committed to the action in production"* (Gemini, AUDIT-WORKING-829314). The body already states this; the gold signal is the unanimous fresh-reader enthusiasm, which argues it is the chapter's load-bearing pedagogical hook and should anchor any pedagogy / README pass.
- **The "referential-transparency" boundary on the `git checkout` claim** (multiple substrates, raised as a *caveat to the above, not a refutation*). The literal-L3 claim holds only if the software is side-effect-free with respect to un-versioned state: *"`git checkout` doesn't roll back a live database or external API"* (Gemini, AUDIT-WORKING-829314); *"`git checkout` provides L3 of past states but not L3 of true counterfactuals — the agent can re-run a past computation, not run an actual alternative history; the two are subtly distinct"* (Claude, AUDIT-WORKING-471203). The body's existing "code-internal deterministic counterfactuals vs. crossing the agent–environment boundary" split already carries this; the convergence confirms it is the right caveat and a natural place readers push.
- **Availability vs. exploitation is the segment's most load-bearing conceptual move** (near-universal agreement; Claude, AUDIT-WORKING-266847, 471203, 527914; et al.). The agent-class mapping that several substrates independently sketched onto it (worth holding when `#def-agent-spectrum` framing is revisited): PID = L1-by-architecture-inside-an-L2-loop; Kalman+LQR = L2-available-not-exploited (separation principle); dual control = L2-exploited; deliberative agent = L3 (Claude, AUDIT-WORKING-471203). *(Conflation-as-signal: this is reach toward a clean taxonomy that the segment does not assert — keep it as a candidate, not a fact.)*

#### 3. Follow-up items

- **Citation precision (Phase-2 verify).** The Bareinboim et al. 2022 reference is *"correct in spirit"* but the precise CHT statement is the strict-inclusion form $\mathcal L_1 \subsetneq \mathcal L_2 \subsetneq \mathcal L_3$ "for almost all SCMs" — stronger than the segment's "cannot in general be computed from … alone" phrasing. Worth confirming whether AAT ever needs the strict-inclusion form or only the weaker one, and tightening the citation to the specific paper (Bareinboim, Correa, Ibeling, Icard 2022, *"On Pearl's Hierarchy and the Foundations of Causal Inference"*) (Claude, AUDIT-WORKING-471203, 742613).
- **L2-is-model-conditioned subtlety.** The L2 formula $P(o_t \mid do(a_{t-1}), M_{t-1})$ conditions on the agent's *model*, whereas Pearl's $do(\cdot)$ is defined relative to the *true* SCM. So AAT's L2 query is a *belief-about-L2* operation; if the model is wrong, the agent's L2 inferences are wrong. Candidate clarifying sentence so the framework isn't read as "the loop generates true L2 data, ergo the agent has true L2 access" (Claude, AUDIT-WORKING-471203 — flagged as sharpening at `#der-loop-interventional-access` downstream).

#### 4. Readers often ask / wonder

- **What level can a language model actually exercise?** The recurring fresh-reader question (Claude+Gemini, AUDIT-WORKING-193847, 266847, 829314): LLMs are trained on L1 (associational) text; they *simulate* L2/L3 reasoning in language but lack the ground-truth verification, so a base LLM reasoning about "what would happen if I do X" is exercising L1 data about what typically happens *when people do X*. Gemini's instance: an LLM trained on GitHub learns $P(\text{tests pass} \mid \text{code})$ from polished PRs (massive selection bias) but never *intervened* — so its compiler-model is purely associational, which is *"the exact mathematical reason LLMs confidently hallucinate code that looks correct but fails to compile."* This is the chapter's most natural reader question; the answer lives downstream (loop compensates) but a forward pointer here would help.
- **How does the agent estimate $P(o \mid do(a))$ when it is just starting out with no interventional data — does it assume L1 ≈ L2 as a heuristic until proven wrong?** (Claude, AUDIT-WORKING-773921). A natural cold-start question.

#### 5. Candidate figures

- **The strict ladder with an AAT overlay.** L1 predicts from history; L2 asks what happens under $do(a)$; L3 asks what would have happened under an alternative action after an actual action/outcome pair — with a side-note at L2 that *action-conditioned data must not be confused with $do$-data* (this is the chapter's pressure point). A rendered draft exists (Codex/Claude, AUDIT-WORKING-526815). The domain-instantiation table (Kalman / RL / scientific method / Boyd / software / immune system) was independently praised as *"excellent pedagogical material"* by several substrates and is a natural figure companion.

#### Belongs elsewhere

- **Is Level-3 reasoning the defining mathematical characteristic of consciousness / moral weight?** Gemini's reach: a thermostat has L2 but never experiences *regret*, which requires the L3 counterfactual *"I did $a$, but if I had done $a'$ the outcome would have been better"* — *"the framework is mathematically defining the prerequisites for moral suffering"* (Gemini, AUDIT-WORKING-193847). Aspirational reach pointing at `04-eli-core/` (regret / moral continuity), not this recapitulation segment.
- **Counterfactual-simulation requires protecting the real chronica.** Running an L3 simulation means the agent must "close its eyes" to current sensory input and spin up a parallel virtual chronica; *"if the internal model is fragile, running a counterfactual simulation might overwrite its actual memory — the infrastructure must protect the integrity of the real chronica while allowing virtual ones to spin up and collapse"* (Gemini, AUDIT-WORKING-193847). Points at `#def-chronica` / `03-llm-core` interiority architecture, not here.
- **Watching another agent act: L1 or L2?** *"If I watch you touch a hot stove, do I gain L2 knowledge? If your action was unconfounded with the stove's temperature, it acts like L2; but if you touched it because you knew it was cold, it's L1"* — flagged as a deep problem Section III (composites) will need (Gemini, AUDIT-WORKING-829314). Belongs with the composite-layer / Mode-2 treatment in `#der-loop-interventional-access` and Part III.
