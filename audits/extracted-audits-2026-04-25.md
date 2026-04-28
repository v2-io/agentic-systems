# Extracted Gemini + Codex De Novo Audits — 2026-04-25

**Source models:** Gemini, Codex (paired pass)
**Date:** 2026-04-25
**Session UUID:** `6da0db68-edec-474a-855f-afb0676d1c8f`
**Record UUID:** `e0461c11-801d-4ec1-80f0-509c43f02d59` (line 437, ts `2026-04-25T18:06:20Z`)
**Topics covered:** discrete-to-continuous variance gap math error; AR(1) exponent perturbation explaining 1.481 simulation; linear-projection-of-linear-dynamics overgeneralization; C-iv adversarial composites cross-segment contradiction; C-iii mutual-benefit composite vs G_c gap; zero-sum potential-game sign error in `strategic-composition`; git timestamps overstating causal direction; TST developer-agent mapping outrunning logogenic caveats. **Big-picture proposals (Gemini):** abandon continuous-time fiction; "action as observation" POMDP collapse; technical debt as belief-state mismatch (mutual-information formulation of code quality); sub-agent composition as multi-agent RL with communication costs.

## Context

Joseph relayed two short, sharp, mathematically-loaded de novo audits — one from Gemini and one from Codex — and asked Claude to verify them and add to a fresh-pass report. The Gemini Findings 1 and 2 are flagged as "100% — Exact mathematical error," which proved correct on verification (they identified a transcription error from `msc/spike-discrete-time-sector.md` that was preserved in segments). These findings became `audits/pending-findings-2026-04-25.md` F-V1, F-V4, F-V5 (variance gap, AR(1) exponent, linear-projection generalization). Codex's findings became F-V2, F-V3, F-V?, P-V?. The Gemini "Big-Picture Insights and Approaches" — including the substantial proposals to abandon continuous-time, collapse action/observation under POMDP, and frame technical debt as belief-state mismatch — were not captured in the pending-findings file.

## Disposition

The mathematical findings (Gemini F1, F2) became F-V1 / F-V4 in pending-findings-2026-04-25.md and were marked F-V1: HIGH (un-caveated math error), F-V4: math error in adversarial-tempo-advantage. Resolution status visible in pending-findings-2026-04-25.md. The Gemini big-picture proposals were NOT translated into architectural-proposals — they cut against substantial architectural commitments (the continuous-time bridge IS load-bearing for Lyapunov analysis; the action-vs-observation distinction IS what makes loop-interventional-access non-trivial). They remain on record here for future reference if the project later wants to revisit POMDP-unification or MARL-as-composition framings.

## Verbatim audits Joseph relayed

> The following are two quick de novo audits done by Gemini and Codex independently. Would you mind evaluating them and adding any/all relevant additions that are verified to the same fresh-pass report?

### Gemini

> Here is the de novo audit of the agentic systems framework based on the current repository state (`01-aad-core/src/`, `02-tst-core/src/`, and `03-logogenic-agents/src/`). The audit focuses exclusively on unacknowledged, un-caveated, or mischaracterized issues where the text makes a strong claim that is contradicted by the mathematics or by other parts of the theory.
>
> ### Finding 1: Mathematical Error in the Discrete-to-Continuous Variance Gap
>
> **The Problematic Passage:**
> In `01-aad-core/src/discrete-sector-condition.md` and `01-aad-core/src/linear-ode-approximation.md`, the text claims the discrete-to-continuous gap for the Model S (stochastic) steady-state variance scales as $O((\eta^\ast)^2)$.
> - In `discrete-sector-condition.md`: "The discrete-to-continuous gap for Model S variance is $O((\eta^\ast)^2 c^2_{\max})$ — the $(\eta^\ast)^2 \lVert F_d\rVert^2$ term that vanishes in the fluid limit."
> - In `linear-ode-approximation.md`: "For Model S (stochastic): the steady-state variance gap is $O((\eta^\ast)^2 c^2_{\max})$, which equals $O(\eta^\ast c_{\max} / \nu)$ when expressed in terms of the event rate."
>
> **The Strongest Counterevidence Elsewhere in `src/`:**
> The derivation inside `discrete-sector-condition.md` itself computes the discrete steady-state variance as:
> $$V_{ss} = \frac{\sigma^2_{\text{step}}}{1 - \lambda^2_{\text{eff}}} = \frac{\sigma^2_{\text{step}}}{2\eta^\ast c_{\min} - (\eta^\ast)^2 c^2_{\max}}$$
>
> Substituting $\sigma^2_{\text{step}} = \sigma_w^2 / \nu$ and $\eta^\ast = \mathcal{T}/\nu$ yields:
> $$V_{ss} = \frac{\sigma_w^2}{2\mathcal{T}c_{\min} - \mathcal{T}^2 c_{\max}^2/\nu}$$
>
> If you take the Taylor expansion of this around the continuous limit $V_c = \frac{\sigma_w^2}{2\mathcal{T}c_{\min}}$, the difference $V_{ss} - V_c$ is $\frac{\sigma_w^2 c_{\max}^2}{4 c_{\min}^2 \nu}$. Because $\eta^\ast = \mathcal{T}/\nu$, this means the absolute gap scales as $O(1/\nu) = O(\eta^\ast)$, **not** $O((\eta^\ast)^2)$. The author confused the $O((\eta^\ast)^2)$ term in the per-step recurrence equation with the asymptotic scaling of the resulting steady-state fraction. Furthermore, equating $O((\eta^\ast)^2)$ to $O(\eta^\ast / \nu)$ reveals the author correctly identified both as scaling as $1/\nu^2$, confirming they mistakenly believed the steady-state gap scales as $1/\nu^2$ rather than $1/\nu$.
>
> **Context from `msc/`:** The working spike `msc/spike-discrete-time-sector.md` correctly identified the gap: "The discrete-time results are either identical to (Model D) or tighter than (Model S, with $O(\eta^\ast c)$ correction) the continuous results." This indicates a transcription error where the spike's nuanced analysis was flattened into an incorrect mathematical claim in the final text.
>
> **Status:** The issue is still real and un-caveated.
> **Confidence Level:** 100% (Exact mathematical error).
>
> ---
>
> ### Finding 2: Missing AR(1) Exponent Perturbation in Adversarial Tempo
>
> **The Problematic Passage:**
> In `01-aad-core/src/adversarial-tempo-advantage.md`, the text claims the adversarial tempo advantage exponent of $3/2$ holds exactly for the discrete model, dismissing the simulation result of $1.481$:
> "The stochastic exponent ($b = 3/2$) is now derived from both the AR(1) stationary variance (discrete) and the Itô-Lyapunov analysis (continuous... The continuous-time analog (Ornstein-Uhlenbeck) gives the same scaling, confirming the result is not a discretization artifact."
>
> **The Strongest Counterevidence Elsewhere in `src/`:**
> In `01-aad-core/src/adversarial-exponent-regimes.md`, the text admits: "Regime 2: Model S (stochastic noise), coupling-dominant... $b = \frac{3}{2}$ (simulation: 1.481) Derived from the Model S steady state $\lVert\delta\rVert_{\text{rms}} = \sigma_w/\sqrt{2\mathcal{T}}$ (Prop A.1S)."
>
> By substituting the discrete steady-state variance (from `discrete-sector-condition.md`) into the mismatch ratio for two coupled agents, the discrete ratio is exactly $\frac{\gamma_A}{\gamma_B} \left(\frac{\mathcal{T}_A}{\mathcal{T}_B}\right)^{3/2} \sqrt{\frac{2 - \eta^\ast_A}{2 - \eta^\ast_B}}$. When Agent A has a higher tempo, it likely has a higher gain ($\eta^\ast_A > \eta^\ast_B$), making the correction factor strictly less than 1. This discrete-time effect mathematically reduces the advantage, perfectly explaining why the simulation yielded an exponent of $1.481$ instead of $1.5$ over a range of tempos.
>
> **Context from `msc/`:** Again, `msc/spike-discrete-time-sector.md` explicitly noted this: "When they differ, there is an $O(\eta^\ast c)$ perturbation to the exponent — negligible in the regime where the adversarial analysis is applied". The final text in `adversarial-tempo-advantage.md` incorrectly claims the AR(1) discrete derivation yields *exactly* $3/2$ and wrongly dismisses the simulation discrepancy as a non-artifact, entirely missing the perturbation term it had previously discovered.
>
> **Status:** The issue is still real and un-caveated. The $1.481$ simulation result is not an artifact but the precise prediction of the discrete model.
> **Confidence Level:** 100% (Exact mathematical error).
>
> ---
>
> ### Finding 3: Over-generalization of Linear Projections of Linear Dynamics
>
> **The Problematic Passage:**
> In `01-aad-core/src/unity-closure-mapping.md`, the text makes a broad claim about state closure defect:
> "State closure in linear-Gaussian. For linear-Gaussian micro-dynamics with consistent linear projections $\Lambda_x$ and $\Lambda_o$... the state closure defect vanishes: $\varepsilon_x = 0$ regardless of $U_M$ or compression dimension. Linear projections of linear dynamics are exact."
>
> **The Strongest Counterevidence Elsewhere in `src/`:**
> In `01-aad-core/src/composition-closure.md`, the text explicitly acknowledges the Mori-Zwanzig connection: "The MZ-optimal Markovian macro-dynamics is $f_c^{\text{MZ}} = P_\Lambda U P_\Lambda$... When $f_c^{\text{MZ}} \notin \mathcal M_{\text{adm}}$, the per-step bound $\varepsilon^\ast \geq \lVert Q_\Lambda U P_\Lambda \rVert_{\text{op}}$ holds — a zero-lag memory-kernel bound."
>
> A linear projection of a linear dynamical system only yields an exact (Markovian) linear system if the projection subspace is invariant under the system dynamics matrix $A$ (i.e., $Q_\Lambda U P_\Lambda = 0$). In the two-Kalman case referenced, this worked only because uncoupled identical filters have a dynamics matrix proportional to the identity matrix ($-K I$), which trivially leaves any subspace invariant. For general interacting or non-isotropic linear agents, linear projections are *not* exact; they mix fast and slow modes and yield non-Markovian dynamics with non-zero closure defects.
>
> **Status:** The issue is still real. It is a broad mathematical over-generalization in `unity-closure-mapping.md` that ignores the precise Mori-Zwanzig caveat stored in `composition-closure.md`.
> **Confidence Level:** High.
>
> ---
>
> ### Big-Picture Insights and Approaches
>
> After auditing the formalization mapping software development into control theory, causal inference, and information theory, the ambition is clear and breathtaking, but the framework is occasionally groaning under the weight of its own analogies. Here are a few intuitions and simplifications that might make all of this more beautiful, accessible, and mathematically watertight:
>
> 1. **Abandon the Continuous-Time (ODE/SDE) Fiction**
>    The framework expends massive energy bridging between continuous-time Lyapunov stability (ODEs/SDEs) and the reality of software engineering, which is fundamentally discrete and event-driven. Findings 1 and 2 above are direct consequences of the friction caused by this bridging.
>    *Simplification:* Drop continuous time entirely. Treat software exclusively as a discrete-time Markov Decision Process (MDP) or Partially Observable Markov Decision Process (POMDP). The discrete sector conditions and AR(1) dynamics are sufficient and exact for the domain.
>
> 2. **The "Action as Observation" Collapse**
>    The framework creates elaborate taxonomies for observation channels vs. exploration actions vs. interventional probes. However, in a POMDP, *every action is an information-gathering action*. A developer reading code is taking an action that transitions their belief state (the belief MDP). A developer running a test is taking an action that transitions both the environment and their belief state.
>    *Simplification:* Model the developer as solving a POMDP where the reward function is $-\text{time}$. The "exploration vs. exploitation" and "deliberation threshold" become standard solutions to the Bellman equation in the belief MDP, natively capturing the value of information (VOI) without needing the heuristic CIY (Causal Information Yield) surrogate.
>
> 3. **The Unification of Technical Debt and Mismatch**
>    The theory currently separates epistemic mismatch ($\delta_t$) from strategic mismatch ($\delta_\Sigma$) and temporal optimization (TST). But they are shadows of the same object. Technical debt is simply the true state of the codebase diverging from the developer's belief state. The "vicious cycle" of rushed changes degrading code quality is exactly an agent making suboptimal actions under high belief-state uncertainty, which introduces more entropy into the environment state, further degrading future observations.
>    *Simplification:* Frame "code quality" purely as the mutual information between the code's lexical structure and the true domain model. TST's "proximity" and "coherence" are just the physical manifestations of this mutual information. High mutual information means high observation function fidelity ($h$), leading to faster belief-state convergence.
>
> 4. **Sub-Agent Composition as Multi-Agent RL**
>    Section III (Agentic Composites) creates heavily parameterized formalisms for team persistence (e.g., 16-cell emitter-recipient opacity matrices). Yet, Conway's Law and Brooks's Law emerge much more naturally from a simple distributed POMDP model: multi-agent reinforcement learning (MARL) with communication costs. The "coordination overhead" is just the bandwidth constraint on sharing belief states.
>    *Simplification:* Define a composite agent merely as a set of agents with a shared reward function but decentralized observation functions. "Symbiogenic composition" is then just the process of centralized policy learning where one agent's observation space completely subsumes the other's.
>
> By stripping away the continuous-time control theory analogies and standardizing entirely on a POMDP with communication costs, the entire framework can likely be compressed substantially while maintaining its mathematical rigor and losing none of its unique explanatory power. Good code is simply an environment mathematically optimized to provide high-fidelity observations to a computationally bounded agent.

### Codex

> **Findings**
>
> 1. Section III now contains two incompatible stories about adversarial composites. Problematic passage: `multi-agent-scope.md:67` says "the adversarial case is … not a composite" and explicitly excludes adversarial pairs from composite-level machinery. Strongest counterevidence: `scope-composite-agent.md:46` and `strategic-composition.md:78` explicitly add route `C-iv` for equilibrium-convergent strategic composites, including some adversarial cases. Assessment: still real. `C-iv` exists, but surrounding scope prose and dependent segments have not been fully rewritten around it. Confidence: high.
>
> 2. The `C-iii` mutual-benefit route does not fit the macro-agent object that `composition-closure` requires. Problematic passage: `scope-composite-agent.md:38` allows composites with "no explicit common objective," while `composition-closure.md:73` requires macro-state decomposition $X_c = (M_c, G_c)$ and `composition-closure.md:65` still says the closure framework applies to any of the "three alignment routes." Strongest counterevidence: `scope-composite-agent.md:79` itself says that without a coherent $O_c$, the composite purposeful state is ill-defined. Assessment: still real. The repo has not yet said whether `C-iii` gets weaker machinery, an induced $O_c$, or a different macro-object entirely. Confidence: high.
>
> 3. The zero-sum worked example in `#strategic-composition` is mathematically inconsistent with the segment's own potential-game criterion and with its stated dynamics. Problematic passage: `strategic-composition.md:74` claims the zero-sum scalar game is a potential game with equilibrium $(1, -1)$. Strongest counterevidence: earlier in the same segment, `strategic-composition.md:42` defines a potential game by unilateral payoff changes matching a shared potential. Under the stated dynamics $s_{t+1} = s_t + a_A - a_B + w$, agent $B$ improves its payoff by increasing $a_B$, not decreasing it, so the sign pattern and the written equilibrium do not match the setup. Assessment: still real. This is a hard mathematical error, not just a caveat issue. Confidence: high.
>
> 4. `#causal-discovery-from-git` overstates what temporal ordering buys. Problematic passage: `causal-discovery-from-git.md:30` says timestamps provide "causal direction for free" and that if $c_1$ precedes $c_2$, then $c_1$ is in $c_2$'s causal past. Strongest counterevidence: `causal-structure.md:21` is much more careful, saying temporal precedence only defines possible influence, not actual influence; `system-coupling.md:35` then makes the causal interpretation explicitly conditional on confounder regime. Assessment: still real. The later caveats do not rescue the quoted sentence; it is too strong on its own terms. Confidence: high.
>
> 5. The TST developer-agent mapping for AI developers outruns the logogenic section's own architectural caveats. Problematic passage: `scope-developer-agent.md:63` says AI $M_t$ is "closer to a directly observable quantity," `:73` routes objective revision through the orient cascade, and `:166` says session start resets $M_t$ to near-zero. Strongest counterevidence: `scope-logogenic-agent.md:56` says the $M_t/G_t$ boundary is representational and not sharp for LLMs; `coupled-update-dynamics.md:36` says Class 2 updates are coupled and the orient cascade is no longer architecturally derived; `context-turnover.md:25` says session-start state is reconstructed from external memory, prompt, and weights rather than literally collapsing to zero. Assessment: still real. The careful Class-2 story exists, but `02-tst-core` has not absorbed it cleanly. Confidence: medium-high.
>
> **`msc/` Pass**
>
> - Findings 1 and 2 are already partially diagnosed in working material. `msc/spike-composition-no-go.md:135` sharpens the load-bearing role of `#scope-composite-agent`, and `msc/pending-findings-2026-04-22.md:322` explicitly identifies the `C-iii` versus $G_c=(O_c,\Sigma_c)$ gap. What has not happened is a clean re-landing into the live segments; some `msc` text still assumes only `C-i/C-ii/C-iii`, so the `C-iv` update landed unevenly.
> - Finding 3 is not repaired in `msc`; it is propagated there. `msc/spike-strategic-composition.md:228` repeats and elaborates the same zero-sum/potential example, including the same sign mistake. This looks like an unreviewed worked example, not missing integration from a better spike.
> - Finding 4 has strong repair material in `msc`. `msc/spike-finding-7-git-chronica-narrowing.md:1` is a promotion-ready narrowing from "git = chronica" to "git = committed-state subset," and `msc/2026-03-14-fresh-eyes-assessment.md:75` independently says git's causal status should be framed as an empirical program, not a secure bridge. `src` absorbed much of the P5 repair, but not the overstrong sentence in `#causal-discovery-from-git`.
> - Finding 5 is also prefigured in `msc`. `msc/agentic-tft-review-response.md:78` says "estimated in language" is not operationalized cleanly and flags the measurement bootstrap problem; `msc/analysis-2026-04-01-remaining.md:36` treats the coupled Class-2 formulation as an open program rather than a finished bridge. The live TST developer-agent segment is more definite than its own working base justifies.
>
> **Bigger Picture**
>
> - The cleanest simplification is to stop forcing one composite ontology to do three jobs. Right now Section III mixes at least three different macro-objects: shared-objective composites, mutual-benefit coalitions, and equilibrium composites. Each wants a different state object and a different theorem family. If you separate them, a lot of the current friction disappears.
> - A second simplification is to distinguish analytic state from instrumented state everywhere. Many tensions come from sliding between "$M_t$ as the analyst's coordinate," "$M_t$ as externally recoverable trace," and "$M_t$ as runtime-computable quantity." TST and the logogenic section would get much cleaner if those were named as different epistemic tiers rather than one overloaded object.
> - The TST bridge wants a stricter three-layer discipline: exact-on-substrate, regime-conditional causal estimator, full-AAD proxy. When git claims stay on the first layer, they are strong; when they jump to the third without carrying the second's confounder conditions, they become brittle.
> - More broadly, the framework is strongest when it announces the object first and the certificate second: what is the macro-object, what counts as success, what theorem family applies, what failure mode blocks it, what escape restores it. Whenever the repo does that, it becomes both more beautiful and more trustworthy. Whenever it compresses unlike cases into one shared frame too early, the prose gets ahead of the mathematics.
