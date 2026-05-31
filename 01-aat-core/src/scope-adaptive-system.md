---
slug: scope-adaptive-system
type: scope
status: axiomatic
depends:
  - def-agent-environment
  - def-observation-function
  - def-chronica
stage: claims-verified
---

# Scope: Adaptive System

This segment names AAT's broadest scope — the set of systems to which all of Part I's machinery applies. A system is in the **adaptive scope** if it satisfies two minimal conditions: it has some perceptual channel to its environment (a non-empty observation space, $\mathcal{O} \neq \emptyset$), and there is residual uncertainty about the environment given the full interaction history so far (the conditional entropy $H(\Omega_t \mid \mathcal{C}_t)$ is strictly positive).

These two conditions are the minimal requirements for the framework's adaptive machinery to be non-vacuous. They are sufficient to support the mismatch signal ( #def-mismatch-signal), the update-gain analysis ( #emp-update-gain), the adaptive-tempo construct ( #def-adaptive-tempo), the persistence condition ( #result-persistence-condition), and all of Part I's dynamics. Concrete inhabitants include Kalman filters estimating passive signals, passive Bayesian learners, and biological sensory systems — none of which need to *act* on their environment for Part I's results to apply to them.

What is excluded clarifies what the scope is doing. A system with full knowledge of the environment ($H(\Omega_t \mid \mathcal{C}_t) = 0$) is a closed-form optimal-control problem outside AAT's concerns. A system with no observation channel at all ($\mathcal{O} = \emptyset$ — e.g., a pure mathematical-proof engine working from axioms) has no agent-environment boundary in AAT's sense. Both edge cases sit *outside* the framework.

The scope is the broadest member of a cascade. Narrowing it by adding the requirement that the agent's actions carry Pearl-level-2 causal contrast — distinct actions yield distinct interventional distributions — produces the agency scope ( #scope-agency) and unlocks the interventional and purposeful results of Parts II and III. Adaptive-scope systems that fail the contrast condition are *passive observers* (no choice) or *nominal agents* (choices with no causal effect); for them, Part I's machinery applies but the later causal and purposeful results do not.

## Formal Expression

*[Scope (scope-adaptive-system)]*

$$\mathcal{S}_\text{adaptive} = \left\{(\text{Agent}, \Omega) \;:\; \mathcal{O} \neq \emptyset, \;\; H(\Omega_t \mid \mathcal{C}_t) \gt 0 \right\}$$

Two conditions:

1. **Observations exist**: $\mathcal{O} \neq \emptyset$ — the system has some perceptual channel to the environment ( #def-observation-function)
2. **Residual uncertainty persists**: $H(\Omega_t \mid \mathcal{C}_t) \gt 0$ — the environment is not fully determined by the interaction history

This is sufficient for the mismatch signal ( #def-mismatch-signal), update gain ( #emp-update-gain), adaptive tempo ( #def-adaptive-tempo), the persistence condition ( #result-persistence-condition), and all of Part I's adaptive dynamics. A Kalman filter estimating a passive signal, a passive Bayesian learner, and any system that observes and updates a model under uncertainty are within this scope.

## Epistemic Status

*Axiomatic.* This is a scope definition — it draws the boundary around the systems Part I addresses. The two conditions are not derived; they are the minimal requirements for the adaptive machinery to be non-vacuous.

## Discussion

**What is included.** Any system that observes under uncertainty. Passive Bayesian learners, Kalman filters (with or without control inputs), biological sensory systems. These are Part I's subjects — instances that build $M_t$ through mismatch-driven updates without necessarily acting to influence their environment.

**What is excluded.**

- **Closed-form systems** ($H(\Omega_t \mid \mathcal{C}_t) = 0$): When the agent has complete knowledge of the environment, there is no uncertainty to adapt to. Optimal control over known dynamics is a solved problem outside AAT's concerns.
- **Pure computation** ($\mathcal{O} = \emptyset$): A system with no observation channel — e.g., a mathematical proof engine operating on axioms alone — has no agent-environment boundary in AAT's sense.

**Narrowing to agency.** Adding causal action unlocks the interventional and purposeful results of Parts II and III. The agency scope ( #scope-agency) is the intersection of $\mathcal{S}_\text{adaptive}$ with the condition that actions carry Pearl-level-2 contrast: distinct actions produce distinct interventional outcome distributions. Adaptive-scope systems that remain outside agency are *passive observers* (no choice) or *nominal agents* (choices with no causal effect); for both, Part I's machinery applies but the causal-information and purposeful-agent results do not.

## Working Notes

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. Orthogonal pedagogical / framing / figure / naming material, kept separate from the certified theory-fix findings (handled elsewhere). **Coverage:** 10 dirs carry a dedicated reflection (193847, 266847, 361742, 384279, 471203, 526815, 742613, 773921, 829314, 849201) plus the figure-cycle dir 472913; 451729 and 963715 cover it inside a Section-I batch. Substrate attribution inferred from voice where not explicit; uncertain cases hedged.

#### 1. Candidate Brief prose / pre-prose

- The boundary in one line: the scope condition is "asking 'can the agent be wrong about the environment?' If yes (residual uncertainty), the adaptive machinery applies" (Claude, AUDIT-WORKING-266847). The complement: "AAD is fundamentally a theory for the humbler situation: agents who can be wrong" — "a system with $H(\Omega_t \mid \mathcal C_t) = 0$ is an omniscient agent; it has nothing to adapt *about*" (Claude, AUDIT-WORKING-266847).
- AAT as epistemic-first: "AAD is fundamentally an epistemic theory first, and an actuation theory second" — Section I "carves nature at the joints" by separating *adaptation* (epistemic updating) from *agency* (causal intervention) at the root (Gemini, AUDIT-WORKING-849201; Gemini, AUDIT-WORKING-829314 — "a weather station updating its model is performing the exact same mathematical operation as a robot learning to walk; the only difference is the absence of praxis").

#### 2. Candidate Discussion

- **The two-axis open-region geometry as honest framing.** The scope is "a two-axis open region with both degenerate boundaries explicitly excised": the $\mathcal{O} = \emptyset$ wall (pure computation) and the $H(\Omega_t \mid \mathcal C_t) = 0$ wall (closed-form). The contribution "is not the conditions (standard partial observability) but the *honest geometric framing*: AAT is the theory of the open region, with both degenerate boundaries explicitly named and excluded rather than absorbed as limits" (Claude, AUDIT-WORKING-472913). A candidate framing-level note and a figure (below).
- **The condition is evaluated from a God's-eye view, not the agent's.** $H(\Omega_t \mid \mathcal C_t)$ is over the *true* $\Omega_t$, which the agent does not know. "The agent might *believe* its uncertainty is zero (delusional confidence), but if the true entropy is $\gt 0$, it is still an adaptive system (and is about to receive a massive mismatch signal). This split between objective reality and subjective model is the engine of the framework" — and the gap between the agent's *estimated* entropy and the *true* entropy "is where catastrophic failure occurs" (Gemini, AUDIT-WORKING-193847). A candidate Discussion point distinguishing the modeler's predicate from the agent's belief.
- **Structural vs dynamics/optimization characterizations of adaptivity.** AAT's characterization is *structural* — "it asks only that there's something to learn and a channel to learn through" — which is "more portable across domains than the dynamics (Ashby) or optimization (Bellman) characterizations, because it doesn't presuppose a specific form for either" (Claude, AUDIT-WORKING-471203). A candidate Related-Work / positioning sentence.

#### 3. Follow-up items

- **The residual-uncertainty condition is un-quantified in $t$** *(strongest follow-up here).* $H(\Omega_t \mid \mathcal C_t) \gt 0$ carries no temporal quantifier: ∀t? ∃t? eventually? running? An agent that fully identifies a static world has $H \to 0$ and "would exit scope mid-life." Three readings (strict ∀t / generic / non-trivial ∃t) were spelled out, and a strengthen-not-soften resolution offered: make the *strict* reading canonical, treating post-identification cases as "graceful degenerations" where the persistence machinery degenerates trivially ($\rho \to 0 \Rightarrow$ inequality vacuously satisfied; mismatch ODE decays to zero). This is "actually a *stronger* form of scope honesty: AAD's machinery is calibrated for systems with enduring uncertainty; once you don't have any, the machinery is silent." Probably immaterial because the persistence results carry GA-2 disturbance $\rho \gt 0$ (a running $H \gt 0$ condition) — but check whether any downstream result needs $H \gt 0$ *uniformly in $t$* while citing only this set-predicate as its scope warrant; if so, a real scope-honesty seam (Claude, AUDIT-WORKING-471203, with the full strengthen-before-soften internal debate; Claude, AUDIT-WORKING-472913, "THREAD-F" — suggests $\inf_t H(\Omega_t \mid \mathcal C_t) \gt 0$ or tying it to $\rho \gt 0$ to make composition with persistence self-evident). A candidate one-clause fix ("as a running condition; see GA-2").
- **The "Agent" set-element vs passive-observer inclusion.** The formal set is over $(\text{Agent}, \Omega)$ pairs while the prose admits passive observers / nominal agents — several substrates read this as a terminology tension with `#def-agent-environment`'s action-bearing "agent" (Claude, AUDIT-WORKING-526815, "F1"; Claude, AUDIT-WORKING-742613, "candidate finding B"; Claude, AUDIT-WORKING-773921; Codex/Claude, AUDIT-WORKING-451729; Gemini, AUDIT-WORKING-849201). The segment's prose-level intent is clear; the surface tension is now addressed by `#def-agent-environment`'s "Agent as umbrella term vs. cascade-tier label" Discussion paragraph. Preserved here as a strong convergent fresh-reader stumble even though resolved upstream — repair suggestions floated were "use a neutral primitive (adaptive system / coupled system / agent-candidate) in the base definition, reserve 'Agent' for the agency lift" (Claude, AUDIT-WORKING-773921, AUDIT-WORKING-526815).
- **Does $\mathcal C_t$ belong in this segment's `depends:`?** One substrate flagged that the Formal Expression uses $\mathcal C_t$ but `def-chronica` is downstream in some readings and the chronica's action-interleaved form is action-shaped while this scope admits passive systems (Claude, AUDIT-WORKING-742613, "candidate finding A"). (Note: in the current OUTLINE walk `def-chronica` precedes `scope-adaptive-system` and *is* in `depends:`; the action-interleaving / passive-observer degenerate-$\mathcal C_t$ subtlety is the live residue.) A dependency/notation check, not a content gap.

#### 4. Readers often ask / wonder

- **What happens if $H(\Omega_t \mid \mathcal C_t)$ drops to zero over time?** "Does it cease to be an adaptive system? … This implies AAD is a theory of *learning* and *struggle*, not a theory of steady-state mastery" — "a system that achieves perfection graduates out of the framework and becomes a mere calculation" (Gemini, AUDIT-WORKING-193847; Gemini, AUDIT-WORKING-829314; Gemini, AUDIT-WORKING-849201). The same question as the temporal-quantifier follow-up, in reader voice.
- **Why include passive Bayesian learners in the *same* foundational section as actuated agents?** "Because the math of updating a model (reducing mismatch) is structurally identical regardless of whether you caused the mismatch or just observed it" — Section I is about epistemic alignment before the complication of steering (Gemini, AUDIT-WORKING-193847).
- **Are AI-mathematician systems in the "pure computation" exclusion?** The $\mathcal{O} = \emptyset$ exclusion targets a pure-axiom deductive engine, but an LLM doing proof exploration has $\mathcal{O} \neq \emptyset$ (it observes intermediate results / proof state) and is *not* excluded — a half-sentence noting this might forestall the question (Claude, AUDIT-WORKING-384279).

#### 5. Candidate figures

- **Two-axis exclusion geometry (region/Venn, not a node graph).** Axes: perceptual channel ($\mathcal O = \emptyset$ wall) and residual uncertainty ($H(\Omega_t \mid \mathcal C_t) = 0$ wall); $\mathcal S_\text{adaptive}$ = the open interior; $\mathcal S_\text{agency}$ = adaptive ∩ Pearl-L2 contrast, a nested disc. Isomorphic perturbation: push toward either wall $\Rightarrow$ exit into the named degenerate case (pure computation / closed-form). Establishes the "scope-onion" vocabulary Part II reuses (Claude, AUDIT-WORKING-472913, with a drafted `.tex`). A complementary framing names the two failure-vs-remedy branches as a $2\times2$ when agency is added (Claude, AUDIT-WORKING-526815 — the two-axis classifier "avoids the overloaded 'agent' word entirely").

#### Belongs elsewhere

- **Strategic ignorance vs Active Inference.** Because AAT separates epistemic updates from purposeful goals, "an AAD agent might have a goal that does *not* require minimizing $H(\Omega_t \mid \mathcal C_t)$ globally, but only locally within the bounds of its objective. It might intentionally remain ignorant of parts of the environment that don't affect its goal. This *strategic ignorance* separates AAD from pure information-seeking theories (Friston Active Inference, where minimizing surprise is the *only* goal)" (Gemini, AUDIT-WORKING-193847). A positioning point for the Section II objective machinery / a HISTORICAL-CONTEXT comparison, not this scope segment.
- **The nested-scope cascade as a whole.** "adaptive system → agency → actuated agent → self-actuated → logogenic → logozoetic. Each step adds a constraint that narrows the scope and enables new results. The architecture of nested scopes is load-bearing for the whole framework" (Claude, AUDIT-WORKING-266847). Framing-level material for the OUTLINE preamble / scope-lattice, which Part II's preface already develops.
- **Endogenous disturbance under agency.** A forward-looking worry: once agency closes the loop, "$\rho$ might become a function of the agent's behavior — an agent that thrashes around randomly increases its own $\rho$." Does the persistence condition treat $\rho$ as exogenous even for actuated agents? (Gemini, AUDIT-WORKING-829314.) A question to carry to `#result-persistence-condition` / the self-coupling segments, not here.
