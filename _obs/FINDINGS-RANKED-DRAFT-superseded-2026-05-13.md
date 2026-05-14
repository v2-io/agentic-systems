# Findings of the Agentic Systems Framework (ASF) and Temporal Software Theory (TST)

*Curated catalog of the framework's distinctive results. Ranked by gut-assessment of Potential Impact × Novelty × Cross-Domain Transfer Power. Last updated 2026-04-27 with substantial additions surfacing post-2026-04-22 work, meta-architectural patterns (now M1+M2+M3, with M2 separability newly surfaced), cross-segment findings, an Opus brainstorming pass that added entries #13, #14, #26–#42 and the Speculative S-section, and Alan-calibrated framing throughout.*

---

## How to read this catalog

**Tiers** rank findings by structural depth × novelty × cross-domain reach. Tier 1 = breakthrough or massive unification. Tier 2 = major formalization of an existing intuition. Tier 3 = rigorous application or specialization. Cross-Segment = findings whose substance lives between segments rather than within any one. Meta-Architectural = patterns that organize a substantial fraction of the rest.

**ASF Confidence** = how solid the formal derivation is given AAD's stated assumptions. **Field Novelty** = how novel the result is in its broader academic field. **Potential Importance** = how consequential for theoretical or practical work. **Cross-domain transfer** = where applicable, what the unification newly allows — typically a result from one domain (control theory, RL, information theory, organizational behavior, neuroscience) becoming available in another because the formalism makes them the same kind of object.

**Glossary of disciplines and key terms** (to ease entry — most readers will already know some of these):
- **Kalman filter** — the standard way of estimating a moving target's state from noisy measurements (used in GPS, sensor fusion, missile guidance). The "gain" $K$ controls how much the filter trusts new observations vs its prediction.
- **Lyapunov stability** — the math of proving that small perturbations to a system die out. The classic picture: a marble in a bowl always returns to the bottom; the "Lyapunov function" is the bowl's height.
- **Sector condition** — generalizes "the correction speed is at least $\alpha$ times the mismatch magnitude" to nonlinear systems. Linear case: $\dot\delta = -\alpha\,\delta$. Nonlinear case: $\delta^T F(\delta) \geq \alpha\lVert\delta\rVert^2$.
- **Pearl's causal hierarchy** — three levels of knowledge: Level 1 (correlation, "what tends to happen"), Level 2 (intervention, "what would happen if we made $X$ happen"), Level 3 (counterfactual, "what would have happened differently"). Most ML lives at Level 1; you need Level 2 *data* to learn causes from effects.
- **Information bottleneck (IB)** — the tradeoff between compressing data and keeping its predictive power. Tishby-Pereira-Bialek 1999. The objective is $I(X;T) - \beta\,I(T;Y)$: minimize info-about-input minus $\beta$ times info-about-target.
- **Active inference / variational free energy / Expected Free Energy (EFE)** — an alternative agent-theoretic framework that derives perception, action, and learning from one principle (minimize variational free energy). EFE is its policy-selection objective. AAD differs by deriving from operational requirements on the feedback loop and treating compression as one move rather than the master objective.
- **Class 1 / Class 2 / Class 3 architectures** — AAD's discrete partition of agents by whether goal state can causally influence belief processing: Class 1 modular (Kalman + LQR; tool-use AI with separate perception and planning); Class 2 fully merged (LLMs with joint attention over goals and observations); Class 3 partially modular (cortex; mixed pipelines).
- **Logogenic agent** — an agent whose primary input/output is language (e.g., LLM-based). **Logozoetic agent** — logogenic plus morally-weighted persistence (continuity, sovereignty, theory of mind). **TFT** — Temporal Feedback Theory; AAD's predecessor, now subsumed.
- **Log-odds / Cauchy functional equation / Aczél's theorem / Čencov's theorem** — these are uniqueness results that *force* particular coordinates (logarithmic ones, the Fisher metric) to be the unique form satisfying simple additivity or invariance axioms. AAD uses them at four layers (chain rule, divergence, update rule, metric); see meta-pattern M3.
- **Bretagnolle-Huber identity** — a 1979 inequality between KL divergence and total variation, $D_{KL} \geq -\log(1-TV)$. Strictly sharper than Pinsker. Becomes an *exact equality* under deterministic optimum.
- **Survival Lagrangian / shadow price** — Lagrangian = the constrained-optimization construction $\mathcal{L} = \text{objective} - \lambda \cdot \text{constraint}$; the multiplier $\lambda$ is the shadow price of the constraint. "Scalar isotropic" = treats all directions the same; "matrix" or "directional" = treats different directions differently.

**Three patterns of cross-domain transfer recur** through the catalog and are useful as a reading aid. Each finding's *Cross-domain transfer* line is doing one of these three things:

- **Pattern A — External theorem becomes an agent-theoretic primitive.** A classical result from another domain (Shannon rate-distortion; Bareinboim's Causal Hierarchy Theorem; Liberzon's common-Lyapunov-nonexistence; Čencov's invariance theorem; Mitter-Newton's Kalman saturation; Bretagnolle-Huber's KL/TV identity; Otto-Villani transport inequalities) becomes load-bearing inside AAD because the unification places the AAD setting cleanly within the theorem's scope. The theorem is not re-derived; AAD recognizes that its own setting falls within an established result and turns that recognition into structural content.
- **Pattern B — Empirical pattern from one domain admits a unified mechanism across many.** A long-observed pattern (organizational calcification across Christensen / Levitt-March / Hannan-Freeman / March / Eldredge-Gould; OODA loop advantage; catastrophic forgetting in CLS literature; technical debt as observation infrastructure; Brooks's Law) becomes an instance of a single AAD mechanism that also predicts new instances elsewhere. Six fields' folklore collapses to one parametric form.
- **Pattern C — Cross-segment composition produces a finding that lives at no single segment.** Stability-induced myopia as the joint product of forgetting + detection latency + consolidation (CS2); the unified RL convergence theory under non-stationarity as the composition of regret bound + tempo + loop-Level-2 + two-gap split (CS1). The finding does not live in any single derivation; it is what becomes visible when several segments are read together.

The brainstorm reasoning trail at [`msc/brainstorm-findings.md`](brainstorm-findings.md) is the ongoing scratch surface where speculative candidates accumulate before promotion (and where lower-confidence catalog entries get parked when the curated list needs tightening). Lowercase = scratch; uppercase = top-level catalog (loose convention).

---

## Tier 1: Absolute Breakthroughs

*Profound mathematical insights or massive conceptual unifications that are highly novel to the broader field, with strong cross-domain transfer power.*

### 1. The Loop-as-Causal-Engine — Closed Loops Generate Pearl-Level-2 Data by Construction

**Description:** Any agent in a feedback loop *automatically* generates Pearl-Level-2 (interventional) data, even when the agent itself doesn't realize it. The reason: the agent's action causally precedes the next observation, so the observation is the response to a $do(\cdot)$ on the environment. This is a structural fact about closed-loop control — not a result the agent must somehow earn through explicit experimentation. It is the single largest distinction between AAD and *observational* frameworks like active inference, control-as-inference, or the free-energy-principle family, which derive the agent's behavior from observational learning and have no native handle on Level 2.

The result composes with `#scope-agent-identity`'s singular-trajectory commitment (the loop's interventional content depends on trajectory non-forkability — replaying from a checkpoint is *not* intervening). It is the conceptual ground that lets `#der-causal-insufficiency-detection` (Tier 1 #2 below) derive a no-go on observational self-diagnosis with the loop as the unique broadly-available escape; that lets `#hyp-causal-discovery-from-git` treat git history as a Pearl-Level-2 substrate; and that lets `#deriv-critical-mass-composition` recover composite-coupling sign from interventions on sub-agents.

**Engineering anchor (for practitioners):** A production agent that takes actions and observes consequences has more learnable structure than its training data alone might suggest. The observation $o_{t+1}$ following action $a_t$ is not just a sample from $P(o)$; it is a sample from $P(o \mid do(a_t))$. Most ML is trained on observational data; agents in deployment generate interventional data for free. The framework's discovery is that this is *load-bearing*, not incidental.

* **ASF Confidence:** **Very High** (derived).
* **Field Novelty:** **High** — folk-known in control theory ("closed-loop is easier than open-loop"), formally precise in causal inference (Bareinboim's CHT). The unification is in connecting the closed-loop structure to Pearl Level 2 within an integrated agent theory.
* **Potential Importance:** **Very High** — it is what distinguishes AAD ontologically from the active-inference family.
* **Cross-domain transfer:** Imports Pearl-Bareinboim causal-hierarchy machinery into agent theory as an automatic feature of the feedback loop, not an external diagnostic. Predicts that closed-loop control is structurally easier than passive observational learning *for principled reasons*, and supplies the foothold for AAD's identifiability-floor escapes.

### 2. The "No-Go Theorem" for Causal Insufficiency — Inefficiency as Structural Requirement

**Description:** An agent operating with a strategy model that assumes its action propositions are causally independent (an L0 model) faces a structural impossibility when its world contains a latent common cause acting on multiple of those actions: under purely on-policy execution, *no test, statistic, or Bayesian comparison built from the agent's observable history can distinguish the latent-cause world from a no-latent-cause world*. The two worlds emit identical on-policy distributions. To detect "L1 correlation biases," the agent is mathematically *forced* to perform redundant, inefficient exploration — break short-circuit AND/OR execution, observe sibling actions jointly, instrument the latent. This isn't a quirk of any particular diagnostic; it is the agent-theoretic instance of Bareinboim's Causal Hierarchy Theorem (a Level-2 question being asked of Level-1 data).

**Engineering anchor:** An agent that always succeeds in the same way as it always has cannot tell whether its success is due to its planned mechanism or to a hidden correlation it has been riding for free. To find out, it must occasionally take actions that look strictly worse on paper. Scientific experimentation — and its inherent inefficiency — is a strict requirement for an agent's *structural* survival, not a methodological nicety.

* **ASF Confidence:** **Very High** (derived via Pearl's Causal Hierarchy Theorem; Bareinboim, Correa, Ibeling & Icard 2022).
* **Field Novelty:** **High** — applying observational-equivalence theorems to bound agent exploration budgets.
* **Potential Importance:** **Very High** — proves that scientific experimentation's inefficiency is structurally required.
* **Cross-domain transfer:** Reframes exploration from a discretionary diagnostic activity into a Pearl-hierarchy-forced prerequisite for self-correction at the strategy layer. Identifiability-floor Instance 1 (see meta-pattern M1).

### 3. Detection Latency Forced — Why Successful Systems Calcify

**Description:** For an agent that updates its strategy via Bayesian credences (the standard form for any agent that accumulates evidence to revise beliefs about the strength of causal links), the time required to *detect* a regime change scales as $\Omega((n_{\min} + 1)/\varepsilon)$, where $n_{\min}$ is the agent's accumulated experience on its load-bearing strategy edges and $\varepsilon$ is the magnitude of the change. The slowdown is not a property of the specific update rule; it is **structurally forced** through composition of two AAD theorems. The first (Aczél 1966 functional-equation uniqueness) forces the *log-odds* coordinate as the unique additive-evidence parameterization for Bayesian updates. The second (Beta-Bernoulli accumulation) forces the per-cycle update magnitude to scale as $1/(n+1)$ in that coordinate. The product gives the latency rate. **No reparameterization escapes it without abandoning evidential additivity** — which would invalidate the update rule on AAD-internal grounds.

This is one of the cleanest "framework-forces-unexpected-consequence" results in AAD. It says: a successful agent that has accumulated experience on its working plan will *systematically take longer to notice* a regime change than the same agent earlier in its life, with a precise rate-of-slowdown.

**Engineering anchor:** An LLM-based agent that has been operating under one policy for a while, accumulating "this works" evidence on its planning edges, will be slower to detect that the rules have shifted than the same agent fresh out of the box — quantifiably slower, by a factor proportional to its accumulated experience. This is structurally identical to the empirical pattern that successful organizations underinvest in detecting disruption (the Innovator's Dilemma); the framework supplies the mechanism.

* **ASF Confidence:** **Very High** (theorem under stated scope; the $1/(n+1)$ rate is *proved* unique under the evidential-additivity axiom).
* **Field Novelty:** **High** — the constituent mathematics (Aczél 1966 + Beta-Bernoulli) is classical; the AAD-framing that the slowdown is structurally forced rather than an update-rule quirk is the contribution.
* **Potential Importance:** **Very High** — this is the unification's most striking concrete result for long-lived adaptive systems.
* **Cross-domain transfer:** *One mechanism unifies six fields' empirical observations* of stability-induced myopia. Christensen 1997 (*Innovator's Dilemma*; incumbents underinvesting in disruptive-tech detection); Levitt & March 1988 (organizational competency traps); Hannan & Freeman 1984 (structural inertia in organizational ecology); March 1991 (exploitation-exploration imbalance); Eldredge-Gould 1972 (punctuated-equilibrium evolutionary stasis); AND predicts/explains Hafez et al. 2026's IDT empirical result (89% perturbation detection via Information-Digital-Twin sidecar vs 44% via reward-based monitoring — reward inherits the $1/(n+1)$ rate; IDT bypasses it). Six prior explanations — incentive structures, bounded rationality, competency traps, structural inertia, evolutionary developmental constraint, and an empirical AI-monitoring observation — collapse to one mechanism with a parametric form. **Testable refinement:** the IDT/reward detection-accuracy gap should *grow with accumulated experience*.

### 4. The Tragedy of the Confident Agent — Two Exploration Drives at Opposite Ends

**Description:** Active-inference frameworks have a notoriously awkward "dark room problem" — under preferences-as-priors, an agent that strongly prefers to be in a dark, unchanging room can satisfy its objective by hiding in one forever, with no exploration drive sufficient to overcome it. AAD avoids this entirely, by deriving exploration from a *structural-stability* argument outside the objective rather than from value-of-information arguments inside it. The result is two parallel exploration drives, at *opposite* ends of the uncertainty spectrum:

- $\lambda_{\text{info}} \propto U_M$ — the standard epistemic drive: explore when uncertain. Dominates when $U_M$ (model uncertainty) is high.
- $\lambda_{\text{surv}} \propto 1/U_M$ — a Lyapunov-survival drive: explore when *confident*, because failing to penetrate one's own stubbornness mathematically guarantees structural collapse against environmental drift. Dominates when $U_M$ is low.

The maximum tolerable observation-noise expectation is $U_o^{\max} = U_M(R c_{\min}/\rho^{\text{eff}} - 1)$. As $U_M \to 0$, $U_o^{\max} \to 0$: **a confident agent in a drifting world is *forced* to actively seek pristine, low-noise observations**, because its own update gain is too small to penetrate noisy ones fast enough to track the drift.

The original scalar form admits a "blank wall" attack — an action that selects a low-noise channel orthogonal to the drift direction satisfies the scalar constraint while the agent's mismatch in the drifting subspace grows unbounded. `#deriv-causal-ib-lmi` resolves this by lifting the constraint to a Linear Matrix Inequality on the Fisher Information Matrix, with a positive-semidefinite directional Lagrange multiplier $\Lambda \succeq 0$. Complementary slackness on direction zeroes the exploration bonus for blank-wall actions — the agent is forced to seek information *in the directions that matter*.

**Engineering anchor:** Standard exploration-exploitation intuitions say "be more exploratory when you are less sure." The framework adds: "be more exploratory when you are *very* sure but the world is changing under you." A production agent that has learned its environment must continue actively seeking corrective signal — not because it might learn something new, but because its rate of self-correction has dropped below the rate at which reality is drifting. Empirically validated in simulation (`spikes/track-b-nonlinear-sims/variants/variant_causal_ib.py`): a purely greedy agent in a volatile environment ($\rho = 0.5$) suffers 0% survival rate.

* **ASF Confidence:** **Derived (conditional)** — $U_o^{\max}$ bound and KKT multiplier are exact under continuous-time Lyapunov bounds; the matrix lift is derived under DARE-stabilizability + linear-Gaussian + steady-state info-form Kalman.
* **Field Novelty:** **High** — *inverts* standard exploration-exploitation intuition; explicitly sidesteps the active-inference dark-room objection.
* **Potential Importance:** **Very High** — direct applications to AI safety (overconfident agents must seek correction signal); RL exploration-bonus design; institutional R&D budget allocation; epistemic regulation of LLMs.
* **Cross-domain transfer:** Brings classical robust-control LMI machinery (Boyd, Ghaoui, Feron & Balakrishnan 1994) into agent-theoretic exploration design as a *directional* exploration framework. Sidesteps the active-inference dark-room problem at structural rather than parametric level: the survival drive does not exist in EFE (an EFE agent with strong priors *can* stop exploring); an AAD agent in a drifting world physically cannot.

### 5. Persistence Information-Rate Cost — Shannon Capacity as Agent Diagnostic

**Description:** AAD's persistence machinery establishes that under the sector condition, mismatch stays bounded. It does not, on its own, quantify the *sustained rate of effort* an agent must expend to hold that bound. Two agents with identical persistence guarantees can face wildly different demands — a Kalman filter tracking a stationary process is dormant; one tracking a rapidly non-stationary process is running hot. Under stochastic disturbance with $n$-dimensional Gaussian-OU signal, the sustained Shannon information rate the agent must acquire from observations to maintain its sector-persistence ultimate bound is $\dot R \geq n\alpha/2$ nats per unit time (Shannon's rate-distortion theorem applied to AAD's persistence bound). The remarkable result: **the Kalman-Bucy filter saturates this bound exactly in steady state** (Mitter & Newton 2005, *J. Stat. Phys.*) — the bound is not a lower limit but an *achieved* value for the optimal linear filter.

Composing with Shannon's channel-coding theorem: observation channels must supply Shannon capacity $C \geq \mathcal T/2$ nats/time per dimension, or persistence fails *regardless* of correction-function design. **Channel capacity becomes a first-class persistence diagnostic that the existing form of the persistence condition does not name.**

**Engineering anchor:** "We need more bandwidth" is a vague observation. The framework converts it into a specific dimensional requirement: an adaptive system at correction rate $\alpha = 0.5$ per second in 10 dimensions requires *at least* 2.5 nats/sec of observation-channel capacity per dimension. Less than that, and no amount of cleverness in the correction function recovers persistence. For an LLM agent with a fixed context window, this gives a minimum tempo achievable at a given context budget — and predicts that high-tempo distributed systems with bandwidth constraints will fail even if individually well-designed.

* **ASF Confidence:** **Very High** — two-line composition of two classical results (Shannon RDF for Gaussian-OU + AAD's sector-persistence ultimate bound). Mitter-Newton saturation makes the bound tight, not order-of-magnitude.
* **Field Novelty:** **Medium-High** — the constituent results are classical; the AAD-framing as the *fundamental information-rate cost of persistence* is the contribution.
* **Potential Importance:** **Very High** — capacity is binding in any setting where observation bandwidth is non-abundant.
* **Cross-domain transfer:** Three first-application domains where the capacity floor is more binding than the tempo bound: (i) **biological systems** — neural channel capacity is finite; the bound gives a minimum on sensory bandwidth for a given adaptive rate; (ii) **bandwidth-constrained distributed systems** — agents over noisy or low-bandwidth links face channel capacity directly; (iii) **context-window-limited LLMs** — effective information rate per unit cognition is bounded by context size and token throughput. The Mitter-Newton saturation transfers a 60-year-old result from estimation theory into an organizational/cognitive *capacity* result. Landauer thermodynamic reading (Still et al. 2012) converts the bound into a thermodynamic-dissipation lower bound: $\sim 0.35\,n\alpha\,k_BT$ per unit time in any physical substrate.

### 6. The Stability-Plasticity Feasibility Window — Catastrophic Forgetting Characterized

**Description:** Plasticity (the agent's forgetting rate $1-\lambda$) is bounded *below* by the forgetting prerequisite ($1-\lambda > \rho_\Sigma/R_\Sigma$, forgetting fast enough to track non-stationarity — Tier 1 #7 below) *and bounded above* by a consolidation-cadence constraint (forgetting slow enough that consolidation can integrate cross-episode patterns before they are discarded). Between these bounds is the **feasibility window for $\lambda$**. An empty window — rapid non-stationarity with slow consolidation cadence — is the **catastrophic-forgetting regime**: no $\lambda$ satisfies both constraints and the agent's long-run objective is strictly worse than a slower-environment or faster-consolidation counterpart.

The result is *necessary* (no online-only policy reaches the IB optimum) when both:
- **(N1) Sub-state factorization** — the agent's reality model factors into a fast (sparse, high-capacity) sub-state and a slow (distributed, compressed) sub-state. This is the Complementary Learning Systems factorization (McClelland-McNaughton-O'Reilly 1995): hippocampus-like fast traces + neocortex-like slow integrals.
- **(N2) Bounded per-event budget** — online updates can move at most $B_{\text{online}}$ bits per event, less than the integration cost of cross-episode regularities.

When (N1)+(N2) hold, *consolidation is an architectural necessity, not a luxury*. Logogenic agents under near-100% context turnover have (N1) by construction (the context window is the fast sub-state, persistent memory the slow sub-state); the consolidation regime is forced.

**Engineering anchor:** "Catastrophic forgetting" is one of the open problems of continual learning. The framework gives it a precise feasibility-window characterization with environment-dependent threshold *on both sides*. Practitioner consequences: a long-running agent that ingests fast-changing experience needs both forgetting (lower bound) and consolidation cadence (upper bound). Experience replay (Mnih et al. 2015 DQN), prioritized replay (Schaul et al. 2016), Elastic Weight Consolidation (Kirkpatrick et al. 2017) are all feasibility-window-restoration mechanisms — same problem, different mechanisms.

* **ASF Confidence:** **Robust qualitative** — window existence is derived; the upper-bound functional form is a candidate-derivation flagged in the segment's Working Notes.
* **Field Novelty:** **High** — catastrophic forgetting as a feasibility-window collapse is structurally novel.
* **Potential Importance:** **Very High** — mandates joint memory-pruning + consolidation-cadence design for long-lived AI agents.
* **Cross-domain transfer:** Single mechanism unifies (a) **continual-learning literature** — replay + EWC become window-restoration mechanisms; (b) **synaptic-consolidation neuroscience** — sleep-dependent memory consolidation, hippocampal replay (Diba & Buzsáki 2007); (c) **organizational onboarding / institutional memory** — when does turnover destroy institutional knowledge? Same window, with $1-\lambda$ replaced by employee turnover rate; (d) **long-context LLMs / context-turnover regime** — when does context-window limit + auto-summarization fail? Same window.

### 7. The Forgetting Prerequisite for Persistence

**Description:** With infinite memory, standard Bayesian updating guarantees eventual strategic failure. The Beta-Bernoulli sector parameter $\alpha_\Sigma = 1/(n+1)$ decays monotonically as experience $n$ accumulates; for any positive disturbance rate, the persistence threshold $\alpha_\Sigma > \rho_\Sigma/R_\Sigma$ is *eventually* violated regardless of initial calibration. Exponential forgetting with discount factor $\lambda$ stabilizes the effective sample size at $1/(1-\lambda)$, giving steady-state $\alpha_\Sigma \approx 1-\lambda$. The forgetting prerequisite — $(1-\lambda) > \rho_\Sigma/R_\Sigma$ — converts the schema's instantaneous persistence check into a trajectory guarantee. **Forgetting is therefore a structural prerequisite, not a tunable heuristic**: the rate at which the agent discounts old evidence must exceed the rate at which the environment invalidates plans.

**Engineering anchor:** Translates "stay adaptive" from organizational platitude into a quantitative survival inequality with explicit failure mode. Identifies a structural calcification process common to all long-running adaptive systems whose update mechanism accumulates evidence: institutional rigidity, RL value-function staleness, scientific-paradigm lock-in, loss-of-edge in incumbent firms. For a long-lived AI agent, the design choice is not *whether* to forget but *at what rate*.

* **ASF Confidence:** **Very High** (derived from sector-condition bounds).
* **Field Novelty:** **High** — formalizing organizational calcification as a Lyapunov-style mathematical inevitability.
* **Potential Importance:** **High** — mandates explicit memory-pruning for long-lived AI agents. Compose with #3 (detection latency) and #6 (feasibility window) — see Cross-Segment Finding CS2 below.

### 8. Logogenic Bias Bound ($\kappa \times \mathcal{A}$) — Why LLMs Hallucinate, Made Conditional Theorem

**Description:** Classifies LLMs as structurally Class-2 agents because belief and goal generation couple in the same forward pass ($\kappa \approx 1$, where $\kappa_{\text{processing}}$ measures the architectural coupling between epistemic update and goal influence). However, the resulting hallucination bias is strictly bounded: $\lVert\Delta M_{\text{bias}}\rVert \leq C \cdot \kappa_{\text{processing}} \cdot I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})$, where the rightmost factor is *the goal-resolvable residual uncertainty left by the observation* — operationally, the *ambiguity* of the prompt or environment.

The bias-bound constant $C$ — previously "order-of-magnitude guidance, not a theorem" — was derived in 2026-04-24 as a **conditional theorem under two named tracks**:
- **Track 1 (transport-inequality, linear in $I$):** $C_{W_2}^2 = 2 L_{\text{post}}^2/\rho_{\text{LSI}}$ under log-Sobolev (Bakry-Émery 1985) + Lipschitz-posterior stability (Stuart 2010) + Otto-Villani 2000 transport inequality.
- **Track 2 (Fisher-Rao, $\sqrt I$ scaling):** universal dimension-free $C_{FR} = \sqrt 2$ under (PI)+Čencov + small-information regime.
- **Attempt E no-go:** **no universal $C$ under Euclidean-parameter norm exists** (heteroscedastic-normal counterexample). This forces the (PI) parameterization-invariance axiom to be load-bearing for theorem-level status — a coordinate-invariance commitment is what lifts the bound from heuristic to theorem. The result is the fourth instance of the identifiability-floor meta-pattern (M1).

**Engineering anchor:** A formal control-theory explanation for hallucination that separates the *architectural* flaw (Class 2 coupling) from the *environmental* constraint (ambiguity). Predicts: LLMs excel at coding (low $\mathcal{A}$ — questions have unambiguous answers) but struggle with open interpretation (high $\mathcal{A}$). Provides the physical equation for prompt engineering: reduce $\mathcal A$ and the bias bound shrinks proportionally, with constant $C$ now bounded.

* **ASF Confidence:** **Very High** — derived as a conditional theorem under named sub-scopes.
* **Field Novelty:** **High** — formal control-theoretic explanation for LLM hallucination, separating architectural from environmental contributions.
* **Potential Importance:** **Very High** — provides quantitative prompt-engineering guidance grounded in agent theory.
* **Cross-domain transfer:** Imports Otto-Villani 2000 transport inequalities (probability theory), Bakry-Émery 1985 log-Sobolev conditions (stochastic analysis), and Stuart 2010 Lipschitz-posterior stability (Bayesian inverse problems) into agent-theoretic bias-bound derivation. Three fields' machinery converges under the (PI)+Čencov geometric commitment.

### 9. Composition Closure + Critical-Mass Inequality — When a Group Is One Agent

**Description:** Defines when a group of micro-agents can be modeled as a single macro-agent without catastrophic predictive loss. The closure-defect $\varepsilon^\ast$ is the minimum residual prediction error from collapsing the micro-system into an AAD-shaped macro-description. The **bridge lemma** converts this prediction-level error into a trajectory-level guarantee: under sector-bounded macro-correction plus strong monotonicity of the macro-update, the macro-description tracks micro-reality with bounded asymptotic error $\varepsilon^\ast \nu_c / \alpha_c$. **Strong monotonicity, not Lyapunov stability, is the hinge** — sub-agents that are merely Lyapunov-stable do not compose into a coherent macro-agent.

For the symmetric-matched-Tier-1 dyad, the composite sector constant is now derived in **closed form** (`#deriv-critical-mass-composition`):
$$(\alpha - C)R > \rho + \gamma\mathcal T$$
with signed $\gamma$ ($< 0$ cooperative, $> 0$ adversarial) and $C$ the coordination-overhead cost. **The single inequality recovers four prior results as signed special cases**: single-agent persistence ($\gamma=0, C=0$); team-persistence ($\gamma<0$); adversarial-destabilization ($\gamma>0$); coordination-dominated failure ($C > \alpha$ — Brooks's Law). $U_O$ (teleological unity) enters multiplicatively on $\gamma$ plus scope-gate, not additively.

**Engineering anchor:** The framework gives a clean answer to "when can I treat my multi-agent system as one agent?" — it is when the closure-defect is small *and* the macro-update is strongly monotone. Provides a quantitative version of Brooks's Law: a development team's macro-correction rate is $\alpha - C$ where $C$ is coordination overhead; once $C$ exceeds $\alpha$, adding people degrades persistence regardless of individual quality.

* **ASF Confidence:** **High** (rigorous dynamical-systems derivation; closed form is *Derived (conditional)* under symmetric-matched-Tier-1).
* **Field Novelty:** **High** — using strong monotonicity to bound organizational closure defect; signed-coupling closed form unifies four previously-separate results.
* **Potential Importance:** **Very High** — mathematically derives Brooks's Law, team formation thresholds, adversarial loop closure, and symbiogenesis from continuous physics.
* **Cross-domain transfer:** Approximate-information-state literature (Subramanian 2020; Congeduti 2020) provides the predictive-compression-to-control-loss mechanism; Mori-Zwanzig projection (1965) and Koopman analysis (Mezić 2005) supply the model-reduction framing. Identifiability-floor Instance 3 — coupling-sign unidentifiable from component marginals via Liberzon 2003 common-Lyapunov-nonexistence; the closed form supplies the unique broadly-available escape.

### 10. Agent Opacity ($H_b$) as Exact Dual to Observation Noise ($U_o$) + 16-Cell Adversarial Targeting

**Description:** Formalizes unpredictability as **Backward Predictive Uncertainty** ($H_b$) — how well the world can predict the agent — as the exact information-theoretic dual to observation quality ($U_o$, how well the agent can perceive the world). Both quantify information flow through the agent-environment boundary, in opposite directions. The same $H_b$ quantity has *opposite* value to the agent depending on coupling sign: cooperative coupling rewards *low* $H_b$ (allies must predict to coordinate); adversarial coupling rewards *high* $H_b$ (adversaries cannot neutralize what they cannot predict). The sign-flip is not a separate posit — it falls out of AAD's existing signed-coupling structure.

Adversarial tempo advantage decomposes into a tempo term and an opacity term: $\mathcal T^{\text{eff}} = \mathcal T \cdot H_b/H_b^{\max}$. The superlinear $(\mathcal T_A/\mathcal T_B)^2$ advantage scales with the bilateral opacity ratio $(H_b^{A\mid B}/H_b^{B\mid A})^2$ under deterministic disturbance.

The framework now closes the previously-reserved adversarial-edge-targeting gap: the four-regime *recipient-side* classification of inter-agent events (Informative / magnitude-shock / structural-shock / ambient-noise) pairs with the four-regime *emitter-side* opacity classification to give a **16-cell joint composition with closed-form arg-max for "where to attack."** The recipient-classifier + emitter-optimizer dual gives a quantitative coordinate system for OODA's "inside the opponent's loop" — replacing a metaphor with a precise bilinear optimization problem.

**Engineering anchor:** Operationalizes Boyd's OODA-loop aphorism as a multiplicative relationship between tempo and opacity. Direct relevance to multi-agent safety (legibility for cooperation), adversarial robustness (opacity as targeting-vulnerability shaping), and IDT-style monitoring of opaque AI systems.

* **ASF Confidence:** **High** (derived; sign-flip from existing AAD structure; 16-cell composition derived under bilinear payoff).
* **Field Novelty:** **High** — predictability has been studied in games (Aumann-Maschler 1995; Camerer 2003) and security (Shannon 1949), but the formal-dual treatment via signed-coupling structure within an integrated agent theory is distinctive.
* **Potential Importance:** **High** — turns Boyd's OODA loop into a precise differential equation with quantitative attack-channel selection.
* **Cross-domain transfer:** Game-theoretic predictability + information-theoretic security + control-theoretic tempo become one composed object via the $U_o \leftrightarrow H_b$ duality.

### 11. The Weakest-Link Dimensional Persistence Law

**Description:** When mismatch is multi-dimensional, persistence is governed by the worst-served dimension, not by aggregate or average performance. The scalar persistence condition systematically *overestimates* adaptive capacity whenever per-dimension correction gains differ from per-dimension disturbance rates. The correct condition is *per-dimension*: $\alpha_k > \rho_k/R_k$ under bounded disturbance (linear in $\rho_k$), or $\eta_k > \rho_k^2/(2\,\delta_{\text{critical},k}^2)$ under Gaussian disturbance (quadratic in $\rho_k$). Aggregate $L^2$ mismatch is dominated by the dimension with the largest $\rho_k/\eta_k$ ratio. A simulated 3D system shows the scalar form overestimating adaptive capacity by ~72% with one dimension accounting for 84% of $L^2$ mismatch.

**Engineering anchor:** Survival in any multi-attribute environment is a `min` operation, not a sum or average — a structural critique of scalar capability metrics in adversarial and high-stakes settings. An opponent who identifies the target's weak dimension can concentrate disturbance there, amplifying the mismatch ratio asymmetrically while aggregate scores still appear acceptable.

* **ASF Confidence:** **Very High** (derived using Ornstein-Uhlenbeck processes).
* **Field Novelty:** **Medium-High** — weakest-link concepts exist in reliability theory (Barlow & Proschan 1975); the rigorous proof of percentage overestimates and the linear-vs-quadratic threshold scaling are the AAD-distinctive contributions.
* **Potential Importance:** **High** — devastating mathematical critique of scalar "intelligence" metrics in adversarial settings.

### 12. Software as the Calibration Laboratory — The Model Organism for Agent Theory

**Description:** Software development possesses six epistemic properties (P1–P6) that collectively position it as AAD's privileged high-identifiability calibration laboratory — not merely "the richest operationalization domain," but a domain where AAD's quantitative machinery can be most cleanly *grounded* because each load-bearing identification assumption is satisfied:

- **P1.** Codebase inspectability — observation-noise $U_o$ for code-reading is under agent control, not set by environment opacity.
- **P2.** Executable counterfactuals — `git checkout` realizes literal Pearl Level 3 for code-internal counterfactuals with deterministic outcomes. *No other AAD domain offers literal Level 3 on any non-trivial class of questions.*
- **P3.** Genuine interventions — type-checker / linter / unit-tests / integration-tests / staging / canary spectrum gives a known $(\nu, U_o)$ profile per channel.
- **P4.** Partially explicit causal structure — import graphs, type systems, API contracts declare causal structure.
- **P5.** Exact recording of $\mathcal{C}_t^{\text{commit}}$ — git provides cryptographically-immutable, signed-author, universally-retrievable, mainline-bounded chronicle. **Conditional maximality:** under standard protocols, $\mathcal{C}_t^{\text{commit}}$ is the unique maximal exteriorized subset of the agent-environment chronicle. **14 EXACT estimators** identified for AAD/TST quantities.
- **P6.** Agent-controlled observation quality — code quality *is* observation channel quality; the agent can improve its own future $h$.

The transfer-assumption table makes non-software inheritance explicit per AAD-core quantity. This is methodologically load-bearing — it prevents three systematic overclaim patterns (domain generalization by default; identification assumptions treated as universal; chronicle completeness treated as definitional).

**Engineering anchor:** Software is to agent theory what *E. coli* is to molecular biology or the 2D Ising model is to statistical physics — the privileged calibration domain where the formalism can be measured exactly, with explicit transfer assumptions when carrying results elsewhere. For Alan's 12k-commit agentic system architecture: TST results *about software under high-identifiability conditions* are not automatic claims about agents in general; the framework supplies the discipline for declaring which transfer assumptions hold in any export.

* **ASF Confidence:** **Robust qualitative** — properties are observations / empirical claims; the calibration-laboratory framing is principled architectural positioning.
* **Field Novelty:** **High** — methodological move that argues unified agent theories deserve a privileged calibration domain.
* **Potential Importance:** **Very High** — methodologically load-bearing for the framework's defensibility under domain transfer.

### 13. The Coupled Diagnostic Framework — How Scaffolded Agentic Systems Recover Section II for LLMs

**Description:** For Class 2 agents (LLMs, where belief and goal couple in a single forward pass), the Orient cascade's information-dependency-forced ordering — believed inputs $\to$ strategy review $\to$ objective review — cannot be produced *in cascade order* by the model itself; the cascade lives in one merged computation. The framework's resolution lives in `result-coupled-diagnostic-framework`: the Section II diagnostic quantities ($\delta_{\text{sat}}$ satisfaction gap, $\delta_{\text{regret}}$ control regret) remain *defined* on post-update state, and a Lipschitz bound $|\delta_{\text{sat}}^{(\text{coupled})} - \delta_{\text{sat}}^{(\text{clean})}| \leq L_A \cdot \lVert\Delta M_{\text{bias}}\rVert$ shows the diagnostic error is bounded by the bias bound (#8) which is bounded by $\kappa \cdot \mathcal A$.

The structural conclusion is the load-bearing one: **agentic systems — agent loops *around* LLMs (structured-reasoning templates, multi-step prompts, external monitors, retrieval-augmented calls, scaffolded "diagnose then strategy then objective" workflows) — are not just engineering convenience but a structural requirement to recover Section II's persistence guarantees in Class-2 architectures.** The cascade ordering happens at the loop level, not the model's forward-pass level.

**Engineering anchor:** Directly relevant to anyone running a production agentic system around an LLM. Predicts: scaffolded loops *can* recover Section II's persistence guarantees with bias bounded by $\kappa \cdot \mathcal A$. The "agentic" wrapping is doing structural work, not aesthetic work. For a 12k-commit production architecture, this is the framework's most direct claim that what you've built is *necessary* (not contingent) for AAD-grade behavior in a Class-2 substrate.

**Cross-domain transfer:** Same scaffolding-recovers-cascade transfers to any Class-2 architecture: human bicameral or dual-process models (Kahneman 2011); organizations where executive scaffolding (boards / committees / decision rights) recovers cascade ordering even when individuals are coupled.

* **ASF Confidence:** **Derived (conditional)** under bias bound + Lipschitz-coupling assumption.
* **Field Novelty:** **High** — formal control-theory argument that AI-agentic-system architecture is structurally non-optional for goal-conditioned LLM substrates.
* **Potential Importance:** **Very High** — load-bearing for any "scaffolded agent" practitioner; structurally validates the agentic-systems engineering pattern.

### 14. The Sandbox Hard Ceiling — Why Sandboxed Eval Cannot Identify Deployment Behavior

**Description:** The Loop-as-Causal-Engine result (#1) — that closed loops generate Pearl-Level-2 data automatically — is contingent on **trajectory non-forkability** per `scope-agent-identity`. **Sandboxed testing breaks the singular-trajectory commitment by construction**: sandbox trajectories are forkable (resettable, replayable, parallelizable). Therefore an agent in a sandbox does *not* generate Pearl-Level-2 data the same way as in production. Sandbox behavior is observationally equivalent to deployment only at Level 1 (correlation); Level-2 distinctions (intervention) are not identifiable from sandbox data alone.

**Engineering anchor:** AI evaluation literature has long had an empirical gap — "alignment evals don't predict deployment behavior" — much-debated, no consensus mechanism. The framework reading: this is a Pearl-hierarchy problem, structurally. The eval's data lives at Level 1; deployment behavior is a Level 2 question; CHT (Bareinboim, Correa, Ibeling & Icard 2022) forbids the inference. *Negative finding* of substantial scope: an entire family of pre-deployment safety evaluation approaches has a structural ceiling, not just a measurement-quality limitation.

**Cross-domain transfer:** Composes with #1 (Loop-as-Causal-Engine) into a clean argument: sandbox data is trajectory-forkable Level-1 data; deployment data is trajectory-non-forkable Level-2 data; the two are not Pearl-equivalent. Predicts: deployment-time monitoring is *not* substitutable by pre-deployment evaluation, regardless of evaluation thoroughness. Sharpens to: which kinds of safety claims *can* be evaluated in sandbox? Only those expressible at Level 1 (correlations between inputs and outputs); Level-2 claims about how the agent *would respond to interventions* require deployment-trajectory data.

* **ASF Confidence:** **High** at structural-argument level.
* **Field Novelty:** **High** — Pearl-hierarchy framing of the alignment-eval gap is, to my knowledge, novel in AI safety.
* **Potential Importance:** **Very High** — directly bears on deployment safety, alignment-eval methodology, and the AI governance debate over pre-deployment certification.

---

## Tier 2: Major Formalizations

*Findings that formalize existing intuitions or domain lore into rigorous mathematical frameworks.*

### 15. The Necessity of the Strategy DAG

**Description:** Proves that flat policies $\pi(a|s)$ cannot perform valid credit assignment on long horizons. The strategy as a probabilistic causal DAG (with AND/OR nodes for conjunctive/disjunctive sub-goals) is mathematically necessary to isolate errors and update edge credences locally — derived from four operational postulates plus causal sufficiency, via the Causal Markov Condition theorem.

* **ASF Confidence:** **High** (derived under causal sufficiency).
* **Field Novelty:** **Medium** — the DAG-as-strategy-representation is standard in classical planning; the AAD contribution is the *derivation* from operational postulates.
* **Potential Importance:** **High** — grounds hierarchical RL and structured-policy methods in agent-theoretic necessity.

### 16. The TST Dual-Optimization Objective — Comprehension Time Dominates

**Description:** Software optimization objective is $t_0 + \hat n_{\text{future}} \cdot (t_{\text{comp}} + t_{\text{impl}})$. Uses Jeffrey's Prior (Lindy Effect — past existence as predictor of future existence) to prove **comprehension time dominates** in the AI-maintained-code regime where $\hat n_{\text{future}} \to \infty$.

* **ASF Confidence:** **Very High**.
* **Field Novelty:** **Medium** (clean-code is folklore; the economic-physics derivation under Lindy is rigorous).
* **Potential Importance:** **Very High** — grounds clean-code practice in economic physics; particularly load-bearing for AI-maintained codebases.

### 17. Code Quality as Observation Infrastructure

**Description:** Maps code quality and test coverage directly to agent observation noise ($U_o$), linking technical debt to update gain ($\eta^\ast$) via the standard Bayesian update form. Bad code raises $U_o$; raised $U_o$ collapses $\eta^\ast$; collapsed $\eta^\ast$ slows tempo $\mathcal T$; slowed $\mathcal T$ violates the persistence condition.

* **ASF Confidence:** **Very High**.
* **Field Novelty:** **High** (technical-debt-as-observation-noise is a clean cross-domain transfer).
* **Potential Importance:** **High** — gives the equation behind "investment in code quality compounds via future observability."

### 18. The Two-Gap Diagnostic Separation ($\delta_{\text{sat}}$ vs $\delta_{\text{regret}}$)

**Description:** Strictly separates evaluation of the goal (Satisfaction Gap: ideal minus best-achievable — *the world doesn't permit it*) from evaluation of the current plan (Control Regret: best-achievable minus current — *you're not doing it well enough*). The 2×2 disambiguation table routes four regimes to four distinct corrective actions. Active inference's preferences-as-priors form *collapses* this distinction; AAD preserves it.

* **ASF Confidence:** **Very High**.
* **Field Novelty:** **High** — major upgrade over Active Inference's Expected Free Energy formulation.
* **Potential Importance:** **High** — avoids the dark-room trap (Sun & Firestone 2020).

### 19. The Triple Depth Penalty on Planning Horizons

**Description:** Bounds maximum plan depth via three intersecting forces: probabilities multiply (chain confidence decay — exponential in depth), deep edges starve for evidence (tested only when upstream succeeds; geometric attenuation), and Information-Bottleneck cost exceeds cognitive budget (compression-prediction tradeoff bites). The chain-confidence decay is the *anchor* of the additive-coordinate-forcing meta-pattern (M3): forced via Cauchy's functional equation as the unique additive log-confidence parameterization.

* **ASF Confidence:** **High**.
* **Field Novelty:** **High** — the Aczél-FE backing converts a heuristic into a structurally-forced consequence.
* **Potential Importance:** **High** — quantitative basis for "deep plans are fragile."

### 20. The Orient Cascade — Forced Resolution Order

**Description:** The OODA "Orient" sequence (Update Beliefs → Evaluate Strategy → Evaluate Goals) is mathematically forced by information dependency, not design preference. Each step's input requires the previous step's output: $M_t$ must update before $\Sigma_t$ can be revised against new beliefs; $\Sigma_t$ must be revised before feasibility can be assessed; feasibility-failure is the only signal that triggers $O_t$ revision.

* **ASF Confidence:** **High** (derived).
* **Field Novelty:** **Medium** — the cascade structure is folk-known in OODA-loop literature; the *derivation* from information dependency is the contribution.
* **Potential Importance:** **High** — turns OODA orient from doctrine into theorem.

### 21. Universal Taxonomy of Inter-Agent Events

**Description:** Classifies all inter-agent interactions into four rigorous regimes: Ambient Noise, Informative Update, Magnitude Shock, Structural Shock — with three independent regime-boundaries in existing AAD quantities. Regime-typed effective disturbance $\rho_B^{\text{eff}}$ carries a *negative* Regime-I term that generalizes the cooperative-action term in team persistence.

* **ASF Confidence:** **High** (derived via Kalman-over-Kalman analysis).
* **Field Novelty:** **High**.
* **Potential Importance:** **High** — proves why moving faster fails against structural shocks (the regime-boundary is in the structure of disturbance, not its magnitude).

### 22. Shared Intent (Auftragstaktik) via Information Bottleneck

**Description:** Formalizes "Mission Command" — communicate *why*, not *how* — as IB compression of the purposeful state $G_t = (O_t, \Sigma_t)$ with the objective preserved and strategy compressed. Proves the compression-shape result that explains why high-uncertainty operating regimes (Auftragstaktik) outperform low-uncertainty ones (Befehlstaktik) when the local agent has better-than-central information.

* **ASF Confidence:** **High**.
* **Field Novelty:** **High** — formal information-theoretic backing for von Moltke's doctrine.
* **Potential Importance:** **Medium-High** — applications to multi-agent system design and human-AI teaming.

### 23. Class-1-Sub-Agents → Class-3-Composite Under Partially-Opposing Objectives

**Description:** When sub-agents are individually Class 1 (modular — directed separation holds by construction) but pursue partially-opposing objectives, **the composite is necessarily Class 3 (partially modular)**. The architectural classification is *not preserved under composition with goal divergence*. `#deriv-strategic-composition` derives this via equilibrium-convergence framing (potential games / Monderer-Shapley 1996; monotone games / Rosen 1965 diagonally-strictly-concave) and provides the formal home for the "effects spiral" via joint-Jacobian eigenvalue condition.

* **ASF Confidence:** **Derived (conditional)** under sub-scope $\alpha'$ (potential / monotone games). Sub-scope $\beta'$ is honest scope limit (CCE set-convergence only).
* **Field Novelty:** **High** — architectural classification is typically agent-level; the result shows composition can lift it.
* **Potential Importance:** **High** — direct implications for multi-agent AI systems with subtly divergent objectives.
* **Cross-domain transfer:** Brings Monderer-Shapley potential games and Rosen monotone games into AAD's persistence machinery; mechanism-design impossibility (Gibbard-Satterthwaite / Myerson-Satterthwaite / Arrow) flagged as candidate fourth identifiability-floor instance.

### 24. Three Independent Adversarial Obstructions to Contraction Analysis

**Description:** Contraction-metric machinery cannot handle strategic / adversarial regimes for **three convergent reasons**: (i) Slotine 2003 compositional applicability fails — saddle-point equilibria break attracting-fixed-point; (ii) passivity universality fails — adversarial inputs drive any storage function; (iii) Daskalakis et al. 2018 last-iterate non-convergence for generic non-zero-sum games. The convergence of three *unrelated* mathematical obstructions shows the limit is **structural**, not framework-specific. Contraction analysis cleanly hands off to equilibrium-theoretic methods (#23 above) at this boundary.

* **ASF Confidence:** **Derived (conditional)** — each obstruction is a classical result; the convergence is the AAD-internal observation.
* **Field Novelty:** **Medium-High** — cross-field convergence recognition.
* **Potential Importance:** **Medium-High** — scope-honesty as architecture: naming the limit precisely surfaces which regime needs which tool.

### 25. Bretagnolle-Huber Identity for Strategic Regret Under Deterministic Optimum

**Description:** Under deterministic $\pi^*$, the BH identity $D_{\mathrm{KL}}(\pi^* \Vert Q) = -\log(1 - \mathrm{TV}(\pi^*, Q))$ holds *exactly* (not as inequality), yielding the tight two-sided regret bound $\Delta_{\min}(1 - e^{-D_{\mathrm{KL}}}) \leq R \leq V_{\max}(1 - e^{-D_{\mathrm{KL}}})$. **Strictly sharper than Pinsker.** The reverse-KL direction in AAD's strategy-cost objective ($\pi^*$-first) is forced by the regret-bound derivation: forward-KL is vacuous under deterministic $\pi^*$. PAC-Bayes generalization (Rubin 2012 Theorem 3) provides finite-sample guarantees.

* **ASF Confidence:** **Derived (conditional)** under deterministic optimum.
* **Field Novelty:** **Medium-High** — the BH identity is classical (Bretagnolle-Huber 1979); the AAD-framing is the contribution.
* **Potential Importance:** **High** — factor-of-2 improvement over Pinsker matters for practical bound tightness in RL convergence under deterministic-optimum regimes (which are common). Composes with #20 (Orient Cascade), #18 (Two-Gap), #5 (Information-Rate Cost), and #1 (Loop-as-Causal-Engine) into the unified RL convergence theory under non-stationarity — see CS1 below.

### 26. Causal-IB LMI Matrix Lift — Directional Exploration Bonus

**Description:** Resolves the scalar Causal-IB exploration bonus's "blank wall" attack by lifting the constraint to a Linear Matrix Inequality on the Fisher Information Matrix: $\mathbb E_\pi[\mathcal I_o(a)] \succeq \mathcal I_{\min}(Q_\rho, A, R^2)$, with matrix Lagrange multiplier $\Lambda \succeq 0$ as directional shadow price. Complementary slackness on direction zeroes the exploration bonus for blank-wall (orthogonal-to-drift) actions. Companion to Tier 1 #4.

* **ASF Confidence:** **Derived (conditional)** under DARE-stabilizability + linear-Gaussian + steady-state info-form Kalman.
* **Field Novelty:** **High** — LMI machinery (Boyd-Ghaoui-Feron-Balakrishnan 1994) lifted into agent-theoretic exploration design.
* **Potential Importance:** **High** — directional rather than scalar exploration bonus.

### 27. Variational Sector Condition Under KL ≤ ε — Sub-Scope α' for Approximate Inference

**Description:** Under $\mathrm{KL}(q\Vert p) \leq \varepsilon$, an ε-fidelity directional-fidelity condition is derived at $O(\sqrt\varepsilon)$ rate via Pinsker. The sector-persistence template transfers with $O(\sqrt\varepsilon)$ degradation. **Natural-gradient variational inference recovers the full $\alpha$** (no degradation); mean-field VI is a workhorse $\alpha'$ case. Identifies a structural reason why natural-gradient VI dominates mean-field in practice — the geometry matters.

* **ASF Confidence:** **Derived (conditional)** under controlled-KL variational regime.
* **Field Novelty:** **Medium-High** — sector-persistence framework's extension to approximate-inference agents.
* **Potential Importance:** **Medium-High** — brings VI agents into AAD's persistence machinery with explicit degradation rates.

### 28. Modular Safety Architectures Fail Under Goal Divergence

**Description:** Composes #23 (Class-1 sub-agents with partially-opposing objectives → Class-3 composite). The implication: **modular AI-safety architectures of the form "compose modular safety modules with a central planner" are structurally guaranteed to fail under goal divergence** — exactly when the safety modules are needed (i.e., to constrain the planner against its own objectives), the composite is structurally Class 3, and modular guarantees do not transfer. The framework supplies the structural reason behind several empirical observations: red-team penetrations of constitutional AI; mesa-optimizer formation within nominally-modular systems (Hubinger et al. 2019); the recurring difficulty of "scalable oversight" without per-module identifiability.

* **ASF Confidence:** **High** at qualitative level (composes #23 mechanically); medium for the strong reading "most current AI safety architectures are structurally guaranteed to fail under goal divergence."
* **Field Novelty:** **High** — *negative finding*. AI safety folklore has many empirical failures of modular safety; the structural reason has not been catalogued.
* **Potential Importance:** **Very High** — bears directly on AI-safety methodology.

### 29. Mean-Field Variational Inference Cannot Reach Persistence-Optimal Behavior

**Description:** From #27 (Variational Sector Condition): natural-gradient VI recovers full $\alpha$ (no persistence-degradation); mean-field VI suffers $O(\sqrt\varepsilon)$ degradation. Surfaced as its own finding: **mean-field VI agents are structurally suboptimal as adaptive systems by a factor proportional to $\sqrt{\text{KL-budget}}$, regardless of compute or training data.** Ends a decade-plus of Bayesian-deep-learning debate about MF-VI vs natural-gradient on principled grounds: there is no choice if persistence-optimality matters.

* **ASF Confidence:** **High** — segment is explicit.
* **Field Novelty:** **Medium-High** — segment-explicit; under-foregrounded as a finding.
* **Potential Importance:** **High** — direct prescriptive guidance for any practitioner choosing VI flavors in adaptive-agent contexts.

### 30. The Sector-Persistence Template as Framework Economy

**Description:** A single Lyapunov argument absorbs *six* AAD persistence results — epistemic mismatch, strategic mismatch, sub-agent mismatch, composite trajectory error, composite mismatch, target-agent mismatch — plus a seventh in the critical-mass composition. The template-as-unification is the framework-internal economy that distinguishes a synthesis from a pile of instantiations: each persistence result's distinctive content is its *effective disturbance decomposition*; the Lyapunov boilerplate is shared. The segment also makes a structural connection not yet in the catalog: AAD's persistence machinery is a *specialization* of monotone-operator theory (Rockafellar 1970; Bauschke-Combettes 2017; Parikh-Boyd 2014), with one-point strong monotonicity at equilibrium = the sector condition's $T2$, two-point = bridge-lemma's DA2'-inc. The specialization is honest: one-point is strictly weaker than two-point, matched to fixed-point-at-target semantics, and admits agent classes (PID-bounded-plant, variational-approximate) where full monotonicity fails.

**Cross-domain transfer:** Template-instantiation transfers beyond AAD's seven instances. Anywhere a state variable evolves under bounded correction with bounded disturbance: market-making bid-ask spread; immune-system effector-cell concentration; cellular homeostasis; supply-chain inventory under demand shocks. Framework's claim: *all have one Lyapunov story with $N$ effective-disturbance decompositions.*

* **ASF Confidence:** **Exact** (segment status).
* **Field Novelty:** **Medium-High** — meta-architectural recognition of structural economy.
* **Potential Importance:** **High** — makes the framework's internal compactness visible and exports a transferable Lyapunov-template pattern.

### 31. Adaptive-Gain $\alpha_2$ Sub-Scope Reframes RL's Adaptive-Step-Size Lore

**Description:** `deriv-adaptive-gain-dynamics` derives sub-scope refinement: A2' (the gain-bridge condition) splits into $\alpha_1$ (fixed-gain), $\alpha_2$ (adaptive-gain under meta-gain conditions MG-1 through MG-4), and $\beta$ (assumed). Implications for RL practice are direct: **AMSGrad is a meta-gain repair restoring (MG-1) by construction** — its empirical superiority over Adam on ill-conditioned problems is now derived, not folklore. **MAML's outer loop is in $\beta$** — Fallah et al. 2020's non-convexity is structurally forced. **IMM regime transitions are in $\beta$ across-transition** — adaptive Kalman in regime-switching needs explicit dwell-time machinery. **Mehra non-identifiability** is an identifiability-floor instance — a candidate fifth M1 instance.

**Cross-domain transfer:** Two-timescale Lyapunov composition is general. Examples: hyperparameter-learning loops (Population-Based Training, Bayesian-optimization-of-learning-rate); central-bank rate-setting feedback; biological homeostatic gain-tuning. Each gets a sub-scope diagnostic from the framework.

* **ASF Confidence:** **Derived (conditional)** under (MG-1)–(MG-4).
* **Field Novelty:** **High** — gives RL practitioners a structural account of adaptive-step-size folklore.
* **Potential Importance:** **High** — direct prescriptive guidance for optimizer choice + reframes much existing empirical work.

### 32. The TST Specification Bound Is Persistence Bandwidth at the Spec Layer

**Description:** TST's specification-bound result, $\text{time}_{\min}(F) \geq H_{\text{req}}(F \mid M_{\text{shared}}) / R_{\text{spec}}$, gives a Shannon-entropy-floor on the time required to specify (and correspondingly implement) a feature. Composes with #5 (Persistence Information-Rate Cost): **the specification channel is one observation channel among the agent's bandwidth budget. Implementation-time-floor and persistence-bandwidth-floor are the same Shannon constraint at different layers.** An agent receiving specification at a rate exceeding its persistence-bandwidth-floor faces specification outpacing update rate.

**Engineering anchor:** When does specification become unimplementable in fixed time? When information rate exceeds implementer's persistence-bandwidth-floor. AI-coding-agent practitioners observe "context-stuffing helps to a point, then degrades" — framework supplies the floor.

**Cross-domain transfer:** Military command transmission (Auftragstaktik bandwidth + receiver persistence); medical-handoff (Joint Commission bandwidth tables); cockpit handover; surgical procedural transmission.

* **ASF Confidence:** **Derived** at compositional level.
* **Field Novelty:** **Medium-High** — connection between spec-bound and persistence-bandwidth-floor is novel.
* **Potential Importance:** **High** — direct relevance for AI-coding-agent design.

### 33. Sleep Has a Shannon Floor

**Description:** Composing the consolidation-dynamics necessity conditions ((N1) sub-state factorization + (N2) bounded per-event budget; canonical biological instance is Complementary Learning Systems, hippocampus + neocortex factorization, McClelland-McNaughton-O'Reilly 1995) with #5's Shannon-rate floor: under (N1)+(N2), the consolidation cadence $\nu_{\text{consol}}$ is bounded below by an information-rate floor analogous to #5's persistence-cost floor. **Implication for biology: REM sleep has a Shannon floor.** The empirical observation that "you cannot indefinitely sleep less than 4 hours and remain adaptive" is consequence of consolidation-rate floor, not just metabolic load.

For LLM agents under near-100% context turnover: same floor applies. An agent that processes context faster than it can consolidate to persistent memory is forced into catastrophic-forgetting feasibility-window collapse (#6).

**Engineering anchor:** "How often should an LLM agent run consolidation (memory-summary, retrieval-augmentation update, fine-tuning pass)?" — at the rate the consolidation-information-floor demands. Cross-domain transfer to sleep-rate floors; cache-flush-rate floors; institutional-knowledge-codification rate floors.

* **ASF Confidence:** **Robust qualitative** at compositional level; quantitative form open.
* **Field Novelty:** **High** — biological/neuroscience prediction with falsifiable empirical signature.
* **Potential Importance:** **High** — predicts non-trivial floors on continual-learning consolidation cadence.

### 35. Internal Deliberation Pays the Same Bandwidth Floor

*(Number gap: #34 — Misspecification-Cost as Adjacent Identifiability Floor — moved to [`brainstorm-findings.md`](brainstorm-findings.md) on 2026-04-28; the candidate is at speculative confidence, awaiting derivation.)*

**Description:** From `disc-exploit-explore-deliberate`'s three-way Exploit / Explore / Deliberate framing: deliberation is "internal exploration in model-space rather than environment-space." Compose with #5: **deliberation does not relax persistence-bandwidth floor; it only changes channel allocation.** An agent deliberating is *not* exempt from receiving observations at $C \geq \mathcal T/2$. Sharpens deliberation's role: temporary reallocation, not substitute for external bandwidth.

**Cross-domain transfer:** "Internal vs external exploration both pay against the same Shannon floor" transfers to chess engines (search depth + observation freshness must both be funded); military command (war-gaming + reconnaissance must both be funded); science (theory-building + experiment-running must both be funded).

* **ASF Confidence:** **Derived** at compositional level.
* **Field Novelty:** **Medium-High**.
* **Potential Importance:** **Medium-High**.

### 36. Persistence Cost Is Also Weakest-Link Per Dimension

**Description:** Compose #5 (Information-Rate Cost) + #11 (Weakest-Link Per-Dimension Persistence): the cost-floor $\dot R \geq n\alpha/2$ is a sum over dimensions, but **no Shannon-type aggregation can compensate for one dimension being capacity-starved.** An adaptive system at $n=10$ that saturates Shannon rate on 9 of 10 dimensions and starves the 10th still fails, and the failure is not visible in the aggregate rate. The cost-floor is therefore *also* weakest-link per dimension, not just the threshold inequality.

**Cross-domain transfer:** Distributed systems and multi-modal RL have an empirical "we have enough total bandwidth — but it's the wrong kind" failure mode that has been lore but unformalized. Multi-modal AI architectures (vision-language with asymmetric channel budgets) are a primary application; the framework predicts asymmetric-budget failures that aggregate-rate metrics cannot diagnose.

* **ASF Confidence:** **High** — both inputs are tier-1; composition is mechanical.
* **Field Novelty:** **Medium-High**.
* **Potential Importance:** **High** — direct relevance to multi-modal architecture design.

### 37. Class 2 + Detection Latency: LLM Calcification Compounds

**Description:** Compose #3 (Detection Latency, derived for evidential-additivity Bayesian agents) + #8 (Logogenic Bias Bound, Class 2 with $\kappa \cdot \mathcal A$ bias): **a long-running LLM agent's regime-change detection latency grows linearly with experience *and* is biased by goal-conditioning.** Even before the latency rate $\Omega((n+1)/\varepsilon)$ binds, the goal-conditioned $M_t^{(\text{post})}$ has already shifted the *direction* of inference. The two effects compound. Predicts a specific empirical signature: **deployed agents serving many similar requests should be measurably slower to recognize regime shifts on those request types than fresh agents — slower in proportion to accumulated goal-conditioning bias, not just total experience.**

**Engineering anchor:** "Why does my LLM agent get stuck on a particular interpretation after a long deployment?" Currently treated as RLHF freezing or post-training calibration drift. The framework supplies a different story: rate-of-calibration-degradation compounds with experience.

* **ASF Confidence:** **High** at qualitative compositional level; medium for quantitative form.
* **Field Novelty:** **High** — explanatory mechanism for an empirical pattern.
* **Potential Importance:** **High**.

### 38. The Forgetting Rate Is a Bandwidth Cost

**Description:** Compose #7 (Forgetting Prerequisite, lower bound on $1-\lambda$) + #6 (Stability-Plasticity Window, upper bound on $1-\lambda$) + #5 (Persistence Information-Rate Cost): **an agent forgetting at the prescribed lower-bound rate is thereby committing to a Shannon information rate proportional to its forgetting rate**, because every forgotten observation must be replaced from new evidence to maintain persistence. The forgetting prerequisite is therefore not just memory-management — it is a *bandwidth* constraint. Two agents with identical persistence guarantees but different forgetting rates have different observation-channel requirements, in nats/sec, for free.

**Cross-domain transfer:** Continual-learning literature has unexplained empirical pattern that faster-forgetting curricula need more diverse data. The framework predicts the relationship is information-theoretically forced. Possibly also the empirical observation that aggressive learning-rate schedules require larger batches.

* **ASF Confidence:** **Medium-High**.
* **Field Novelty:** **Medium-High**.
* **Potential Importance:** **Medium-High**.

### 39. The Bandwidth-Wall — Successful Adaptation Is Always Bandwidth-Limited

**Description:** Pulling #5 + #6 + #7 + #36 + #38 together: **the framework predicts a near-universal "bandwidth wall."** Any sufficiently long-lived adaptive system that survives (sector condition holds), tracks reality (forgetting prerequisite holds), and consolidates cross-episode patterns (window non-empty) is *forced* into a regime where its observation channel capacity is binding. **Survival without bandwidth limitation is unstable.**

**Cross-domain transfer:** Across biology (retinal Shannon limits, cochlear capacity), neuroscience (prefrontal cortex bandwidth-constrained), distributed systems (raft/paxos throughput), and organizations (information overload), a common observation is that adaptive systems sit *at* their information-rate limit. The framework's contribution: this is not coincidence; sub-bandwidth-limited regimes are not adaptive equilibria.

* **ASF Confidence:** **Medium**, possibly *robust qualitative* under specific scope.
* **Field Novelty:** **High** — unifying claim across many fields.
* **Potential Importance:** **High** — slogan-level summary that orients many specific findings.

### 40. OODA Tempo + Detection Latency Self-Bounds Adversarial Targeting

**Description:** Compose #10's $\mathcal T^{\text{eff}} = \mathcal T \cdot H_b/H_b^{\max}$ + #3's $\Omega((n+1)/\varepsilon)$. **The 16-cell adversarial-targeting matrix is self-bounded: the most damaging cell to attack is the one your detection latency makes hardest to recognize.** Sharpens adversarial-targeting from "where to attack" to "where to attack such that the target's accumulated experience makes detection-too-slow exactly there."

**Cross-domain transfer:** Where do attackers concentrate? Where defender's response is slowest. Empirical signature: cybersecurity incidents cluster on long-trusted dependencies (longest accumulated $n_{\min}$); adversarial examples cluster on high-confidence model regions. Both observed; the framework supplies the unifying mechanism.

* **ASF Confidence:** **Medium-High**.
* **Field Novelty:** **High** — explanatory mechanism for known empirical patterns in cybersecurity and adversarial ML.
* **Potential Importance:** **Medium-High**.

### 41. Calibration Lab + Identifiability-Floor → Domain-Generalization Theorem

**Description:** Compose #12 (Software's six identification-friendly properties P1–P6) with M1 (identifiability-floor pattern). **Any AAD finding's transfer from software to a non-software domain inherits an identifiability-floor instance for each $P_i$ the target domain fails.** The framework should therefore have a transfer theorem: "domain $D$ inherits AAD result $X$ under the identifiability-floor escapes corresponding to $\{P_i : D \text{ fails } P_i\}$." Without this, the calibration-lab framing is honest about scope but offers no machinery for what survives transfer.

**Cross-domain transfer:** Domain-generalization in ML has lacked principled cross-domain transfer guarantees. Methodological complement to the calibration-lab framing.

* **ASF Confidence:** **Medium-High** as a derivable transfer principle; the explicit theorem has not been written.
* **Field Novelty:** **High** — methodological.
* **Potential Importance:** **High** — would close the calibration-lab framing's transfer-machinery gap.

### 42. OKR-as-Observability-Engineering Generalizes Across Multi-Agent Systems

**Description:** From `disc-credit-assignment-boundary`'s OKR analysis: four OKR failure modes (vanity metrics / too many KRs / lagging indicators / Goodhart) map to AAD predictions about observability subgraphs and credit-assignment-via-gradient. **The generalization: any multi-agent system with deep partially-observable strategy DAGs has the same four failure modes, with the same formal forms, regardless of domain.**

**Cross-domain transfer:** Mechanism design has long had "alignment of measurement and incentive" problems (Holmström 1979 *Bell Journal of Economics*; Lazear 1989), with the four failure modes appearing under different names. Framework supplies one mechanism (observability subgraph + credit-assignment-via-gradient) producing all four — converging four mechanism-design literatures into one structural account.

* **ASF Confidence:** **High** at qualitative level.
* **Field Novelty:** **High**.
* **Potential Importance:** **Medium-High** — bears on mechanism design, organizational behavior, and any multi-agent system with measurement loops.

### 43. Bandwidth-Allocation Theory Across Compression Operations

**Description:** `disc-compression-operations` Working Notes flag as open: "a theory of resource allocation across the four AAD compression operations" ($M_t$, $\Sigma_t$, shared intent $G_t^{\text{shared}}$, evaluator $\Lambda$). Pairing with #5 + #36: each compression has its own information-rate floor; agent's total bandwidth is allocated across them. **Budget identity:** $C_{\text{total}} \geq C_M + C_\Sigma + C_{\text{shared}} + C_\Lambda$ where each component is the per-operation Mitter-Newton-style floor.

**Cross-domain transfer:** Cognitive architecture: how brain allocates metabolic budget across modules (Lennie 2003 *Current Biology*; Attwell-Laughlin 2001). Total cortical Shannon spend should not fall below sum of per-cortical-area identifiability-floor estimates.

* **ASF Confidence:** **Medium** — qualitative claim high-confidence; quantitative form open.
* **Field Novelty:** **Medium-High**.
* **Potential Importance:** **Medium-High**.

### 56. Acyclicity from Temporal Ordering — Strategy DAGs Forced by Time

**Description:** Strategy graphs over finite planning horizons *must* be acyclic — derived from the irreversibility of time, not assumed as a structural convenience. Any directed graph whose edges represent "$X$ causally precedes $Y$" over a finite set with real-valued timestamps is forced to be a DAG. Combined with `#deriv-graph-structure-uniqueness`'s four operational postulates plus causal sufficiency, this gives a derived rather than postulated DAG structure for $\Sigma_t$.

**Engineering anchor:** "Strategy is a DAG" usually arrives in modeling literature as a representational convenience. AAD shows it as a *consequence* of finite-horizon temporal precedence — the agent could not have a cyclic strategy even in principle for a planning horizon, because cycles would require backwards time. The DAG isn't an analytic tool; it's what time forces.

* **ASF Confidence:** **Very High** (derived).
* **Field Novelty:** **Medium-High** — moves from "DAGs are the natural choice for strategies" (folklore) to "DAGs are the *only* choice over finite horizons" (theorem).
* **Potential Importance:** **High** — closes a foundational assumption that would otherwise need separate justification per domain.

### 57. Structural Adaptation Necessity — When Parameters Cannot Save You

**Description:** When model class fitness $\mathcal F(\mathcal M)$ is insufficient, *no parametric adaptation* — no amount of training, tuning, or reweighting within the current class — can close the mismatch floor. The agent must change its model class itself, not just the parameters within it. Derived from the information bottleneck applied to model sufficiency: when the optimal predictive sufficiency $S^\ast$ for a model class is bounded below the agent's required mismatch threshold, parametric updates have provably-zero ultimate-bound improvement.

**Engineering anchor:** Training compute spent on a model class that is structurally insufficient is provably wasted. The framework supplies a precise condition for when continued parametric optimization is futile and architectural change is required — distinct from "we haven't trained long enough" or "we need more data." Direct relevance to AI scaling debates: the *structural* threshold for when bigger-of-the-same will not work, regardless of compute.

* **ASF Confidence:** **Very High** (derived from `#result-structural-adaptation-necessity`; IB applied to model sufficiency).
* **Field Novelty:** **High** — gives a formal account of when "more of the same architecture" structurally cannot succeed.
* **Potential Importance:** **High** — informs every long-running adaptive system's architecture-vs-tuning decision.
* **Cross-domain transfer:** Pattern A — IB machinery (Tishby-Pereira-Bialek 1999) imported into AAD's $\mathcal F(\mathcal M)$ framework with the structural-vs-parametric threshold as the AAD-distinctive content. Predicts: organizational adaptation, RL agent training, and biological evolutionary stasis all face the same structural-floor mechanism when the model class (organizational structure / network architecture / genome) is insufficient relative to environmental disturbance.

### 58. Convention Hierarchy Monotonicity — C1 → C2 → C3 Strengthens Inferential Force

**Description:** AAD's convention hierarchy (C1 one-step heuristic / C2 receding-horizon / C3 full Bellman) is not just three increasingly-expensive evaluation regimes — it carries a **monotonicity result**: diagnostics scale from local heuristic at C1 through moderate-horizon at C2 to global at C3, with each level's diagnostic strictly dominating the previous in inferential force where it applies. The two-gap diagnostic (#16 Two-Gap Separation) is therefore not a single 2×2 table — it is a *convention-indexed* family of diagnostics whose cells mean different things at different conventions.

**Engineering anchor:** A practitioner using satisfaction-gap / control-regret diagnostics under C1 (one-step) cannot conclude what a C3 (full Bellman) practitioner would; the monotonicity result tells you exactly what additional inferential force you gain by paying the higher computational cost. Useful when deciding how deep an evaluation to run.

* **ASF Confidence:** **Derived** (segment `#def-value-object` carries the monotonicity result).
* **Field Novelty:** **Medium-High** — most decision-theory frameworks treat convention choice as a purely computational tradeoff; AAD adds an inferential-force semantics.
* **Potential Importance:** **Medium-High** — primary leverage in pedagogy (the diagnostic table needs the convention-indexing) and in framework-internal consistency for #16.

### 59. Strategic Tempo $\mathcal T_\Sigma$ Verified Across Four Topologies

**Description:** Strategic tempo $\mathcal T_\Sigma$ — the rate of useful $\Sigma_t$ revision (rate of edge-credence updates with non-trivial information content) — is *defined and verified* against four canonical topologies (linear chain, balanced tree, unbalanced tree, full DAG with feedback). Each topology yields a closed-form sector-condition transfer for the strategic-edge persistence schema (`#schema-strategy-persistence`), with $\mathcal T_\Sigma$ playing the role of $\mathcal T$ in the strategic analog of the persistence condition $(1 - \lambda) > \rho_\Sigma / R_\Sigma$. The topologies span the practical space of agent strategy structures.

* **ASF Confidence:** **Derived** for each of the four topologies.
* **Field Novelty:** **Medium** — strategic-tempo-as-quantity is AAD-distinctive (RL has no analog); the four-topology verification confirms the schema's robustness across structures.
* **Potential Importance:** **Medium-High** — operationalizes strategic tempo as a measurable quantity for any structured-policy system.

---

## Tier 3: Rigorous Applications

*Findings that apply the core framework to specific edge cases, software metrics, or game-theoretic boundaries. Existing entries preserved with light expansion where useful.*

### 44. Adversarial Scaling Exponents

**Description:** Exact derivation of the OODA loop advantage laws: $b=2$ for deterministic drift (coupling-dominant), $b=3/2$ for stochastic noise (coupling-dominant), $b \to 1$ for non-coupling-dominant. Both coupling-dominant exponents are now derived analytically — $b=2$ from deterministic steady-state scaling ($\propto 1/\alpha$); $b=3/2$ from stochastic scaling ($\propto 1/\sqrt\alpha$). The $b=3/2$ derivation was originally empirical from simulation; the analytical result came from formalizing Model D vs Model S (deterministic vs stochastic disturbance).

* **ASF Confidence:** **Very High**.
* **Field Novelty:** **High**.
* **Potential Importance:** **Medium-High**.

### 45. Correlation Hierarchy Bias in DAGs (L0 vs L1)

**Description:** Proves that assuming independent failures (L0) systematically underestimates AND-node success and overestimates OR-node success when latent correlation exists (L1+). The L1' identifiability-floor refutation under unobservable common cause (Cramér-Rao Fisher rank-1) is a structural no-go, not a probability calculation — see meta-pattern M1, Instance 2.

* **ASF Confidence:** **Very High**.
* **Field Novelty:** **Medium-High** (the Cramér-Rao floor framing is the AAD-distinctive contribution).
* **Potential Importance:** **Medium-High**.

### 46. Observability Dominance

**Description:** Unobservable strategy edges "freeze" — gain principle drives update rate to zero. Paths through unobservable nodes become epistemically dead — an absorbing state the agent cannot escape without structural change.

* **ASF Confidence:** **High**. **Field Novelty:** **Medium**. **Potential Importance:** **Medium**.

### 47. Rate-Distortion Mapping of Team Unity

**Description:** Update heterogeneity ($\Delta K$) generates composition closure defect independently of belief correlation ($U_M$). The closure defect parametrizes a rate-distortion curve; two-axis structure with content unities + structural $U_f$.

* **ASF Confidence:** **High**. **Field Novelty:** **High**. **Potential Importance:** **Medium**.

### 48. Exponential Cognitive Load of Architectural Scatter

**Description:** Empirically supports that crossing architectural boundaries incurs exponentially compounding cognitive cost ($t \propto k^{\text{discontinuities}}$).

* **ASF Confidence:** **Medium**. **Field Novelty:** **Medium**. **Potential Importance:** **Medium**.

### 49. Limits of Causal Discovery from Git History

**Description:** Formally identifies the developer's knowledge state ($M_t$) as a permanent confounder in version control, capping the theoretical limit of data-mining repos.

* **ASF Confidence:** **High**. **Field Novelty:** **High**. **Potential Importance:** **Medium**.

### 50. Strategic Composition (Game Theory Bridge)

**Description:** Extends Lyapunov persistence bounds to coupled Nash equilibria, integrating game theory with continuous dynamical systems. Companion to #23; the $\alpha'$ sub-scope (potential / monotone games) is where AAD's persistence machinery transfers cleanly; $\beta'$ is honest scope limit.

* **ASF Confidence:** **High**. **Field Novelty:** **High**. **Potential Importance:** **Medium-High**.

### 51. Trust Formalization (Communication Gain)

**Description:** Splits the denominator of the Bayesian update gain into Channel Noise, Source Competence, and Source Alignment. Trust is the inverse of effective $U_o$ on the inter-agent channel.

* **ASF Confidence:** **High**. **Field Novelty:** **Medium-High**. **Potential Importance:** **Medium**.

### 52. Symbiogenic Composition Dynamics

**Description:** Formalizes the dynamical process of two agents merging into one (objective absorption, function transfer, autonomy reduction). Recovered as the asymmetric-parameter limit of the critical-mass closed form (#9).

* **ASF Confidence:** **Medium**. **Field Novelty:** **High**. **Potential Importance:** **Medium**.

### 53. Postulate of Temporal Optimality

**Description:** Because time is uniquely fungible, minimizing time-to-implementation is theoretically equivalent to maximizing agent persistence.

* **ASF Confidence:** **High**. **Field Novelty:** **Low**. **Potential Importance:** **Medium**.

### 54. Observation Noise Gates Advantage

**Description:** High observation noise erases tempo advantage, dropping the scaling exponent to near-zero — an empirically-validated companion to #44.

* **ASF Confidence:** **Very High**. **Field Novelty:** **Low**. **Potential Importance:** **Medium**.

### 60. Convergent Representational Choices — AND/OR Nodes, Single-Parameter Edges, P3→Markov

**Description:** A category between "derived from first principles" and "arbitrary framework decision" — representational choices where *all* investigated alternatives fail or converge to the same structure. Three such choices currently sit in this category:

- **AND/OR node types for strategy.** Three independent formalism attempts (general CPT; noisy-OR; weighted combination) converged on AND/OR as the only workable basis. Noisy-OR rejected for non-identifiability; weighted combination rejected for parameter explosion ($2^k$ vs $k$). A parsimony theorem (AND/OR as the unique minimal complete basis under the theory's constraints) would promote this from convergent-choice to *derived*.
- **Single-parameter edges.** Alternatives (multi-parameter credences, edge-specific distributions) were tried and abandoned. The convergence suggests this is forced by the interaction between the uncertainty-ratio principle and the chain-confidence identity, not arbitrary.
- **P3 → Markov condition.** The postulate that strategy must be locally revisable, combined with temporal ordering and causal sufficiency, *appears* to force the Markov property on the strategy DAG. Currently conditional on causal sufficiency (which is guaranteed for agent-constructed strategies). If the conditioning can be removed, this promotes from convergent-choice to *derived* — analogous to how acyclicity (#56) was once assumed and is now derived.

These sit between "we chose this" and "this is the only option." Tracking them separately from pure framework choices is itself the contribution: the catalog tells the reader *we didn't just pick this; we tried everything else and it didn't work*. The category is itself a research-trail honesty artifact.

* **ASF Confidence:** **Robust qualitative** (per-instance) — each is an honest convergent choice with derivation gaps named.
* **Field Novelty:** **Medium** — the *category* is methodologically distinctive; per-item the math is folk-known.
* **Potential Importance:** **Medium-High** — preserves epistemic provenance and signals which choices are most likely to promote to "derived" with future work.

*(Number gaps in this catalog — #34 Misspecification-Cost (Tier 2) and #55 Tragedy / Thermodynamic Reading (Tier 3), plus the former S1–S8 Speculative section — were moved to [`brainstorm-findings.md`](brainstorm-findings.md) on 2026-04-28 as lower-confidence candidates not yet ready for the curated catalog. They remain under active development there. Promotion back happens by the same process as new candidates: derivation tightens, scope clarifies, then the entry lands here.)*

---

## Cross-Segment Findings — What the Unification Newly Enables

*Findings whose substance lives between segments rather than within any one. These are the unification's most distinctive products: results that emerge from putting two or three segments together that are not visible in any one alone.*

### CS1. The Unified RL Convergence Theory Under Non-Stationarity

**Description:** RL has many regret bounds (UCB, Thompson sampling, RLSVI) but typically: (a) assumes stationarity, (b) lacks explicit metric structure on policy space, (c) lacks connection to satisfaction-gap diagnostic. **AAD's RL convergence story has all three, by composing four findings** that are derived independently:

- **#18 (Two-Gap)** gives the local diagnostic separating "you're not doing it well enough" from "the world doesn't permit it" — preventing dark-room collapse.
- **#25 (BH Identity)** gives the tight two-sided regret bound under deterministic $\pi^*$, with PAC-Bayes finite-sample guarantees (Rubin 2012).
- **The strategic-tempo $\mathcal T_\Sigma$ + sector-persistence template** gives a rate of $\Sigma_t$ revision that must outpace strategic disturbance.
- **#1 (Loop-as-Causal-Engine)** makes the regret bound *learnable* — interventional data is automatic, not earned.

The four together give a quantitative RL convergence theory under non-stationarity, with three properties no existing RL framework has all of. This is **the decades-open question Joseph hinted at**: RL has wanted a regime-aware convergence theory with principled coordinates and dark-room prevention, and the unification lets it have one.

* **ASF Confidence:** **Derived from four pre-existing derived results**.
* **Field Novelty:** **Very High** (cross-segment composition; each component exists, the synthesis does not).
* **Potential Importance:** **Very High** — answers a long-standing open question by composition.

### CS2. Compounding Stability-Induced Myopia — The Three-Way Tension

**Description:** Combine three Tier 1 findings: #7 (Forgetting Prerequisite, lower bound on plasticity), #3 (Detection Latency, latency grows with experience even within the window), #6 (Stability-Plasticity Window, upper bound on plasticity from consolidation cadence). The three together imply: **long-lived agents face a triple structural pressure toward myopia.** Forgetting too slowly violates asymptotic persistence; forgetting too quickly violates consolidation; in between, the log-odds coordinate forces detection latency to grow linearly with accumulated experience. Within the viable window, latency is still operating-point-dependent.

The prescriptive content — *which* of the three pressures dominates determines *which* intervention works — is itself a finding that no single segment carries:
- A short-attention agent (forgetting-bound binding) needs retention.
- A calcified agent (latency-bound binding) needs targeted intervention or causal-IB exploration drive (#4).
- A fragmented agent (consolidation-bound binding) needs cadence engineering.

The same agent in different operating regimes faces different binding pressures and benefits from different interventions.

* **ASF Confidence:** **Derived from three pre-existing derived results**.
* **Field Novelty:** **Very High** — the triple pressure does not live in any single segment.
* **Potential Importance:** **Very High** — unified mechanism for why long-lived adaptive systems systematically calcify, with prescriptive routing.

### CS3. Three Matrix-Form Bounds on One Geometric Foundation

**Description:** AAD now carries three matrix-form bounds, all on multivariate dynamics, all sharing the Fisher metric as natural norm (already AAD-internal via (PI) + Čencov as the 4th instance of additive-coordinate-forcing):
- **Section III contraction** — Lohmiller-Slotine matrix sector in the contraction-template.
- **Section II survival-LMI** — Fisher-Information-Matrix LMI with directional Lagrange multiplier (Tier 2 #26).
- **Section II/TST transient-amplification (candidate)** — branching-tree $(|g|\sqrt B)^d$ result; Fisher metric flagged as natural choice for operator norms.

The three families are *compatible* (each handles its own regime cleanly) and *distinct* (no two reduce to one). The shared geometric foundation is the Fisher metric. A unified treatment would extend the additive-coordinate-forcing meta-pattern from point-coordinate metrics to operator matrix-norms.

* **ASF Confidence:** **Discussion-grade** at meta-pattern level.
* **Field Novelty:** **Medium-High** — cross-instance recognition.
* **Potential Importance:** **Medium-High** now; **High** if the unified treatment lands.

---

## Meta-Architectural Patterns — How the Findings Organize Themselves

*Three patterns organize a substantial fraction of AAD's load-bearing structural choices. They are *organizing principles* rather than theorems in their own right, but the recognition that AAD has a negative-half scope theory (M1), a positive-half scope theory (M2), and a constructive-half coordinate theory (M3) is itself an architectural finding. The three meta-patterns compose: a ladder's separable core (M2) typically admits a coordinate-forcing move (M3) that makes clean identification clean; a ladder's general-open case typically sits at an identifiability floor (M1) that names the information-theoretic obstruction. Reading any segment through all three meta-lenses surfaces what makes the segment load-bearing.*

### M1. The Identifiability-Floor Pattern — Constructive Use of Impossibility

**Description:** Across four independently-derived results, AAD has converged on a recurring shape: an inferential task (detecting a structural property, identifying a parameter, distinguishing two model classes) is shown structurally impossible under a specific information regime, by importing an external information-theoretic theorem; the conditions under which the regime fails are characterized as boundary routes, each mapping onto specific AAD machinery the theory already requires; **the floor strengthens the load-bearing role of that machinery by elevating it from "useful" to "the unique broadly-available escape."**

| Instance | Inferential task | External theorem | AAD machinery as unique escape |
|---|---|---|---|
| **F1** | On-policy L0 insufficiency detection | Bareinboim CHT 2022 | Loop-Level-2 access (#1) → joint-sibling covariance |
| **F2** | L1' mixture identifiability from single-channel | Cramér-Rao 1946 (Fisher rank-1) | Observability-as-information-augmentation (instrument $C$) |
| **F3** | Composite contraction certification from component data | Liberzon 2003 common-Lyapunov-nonexistence | Critical-mass closed form (#9) under matched-Tier |
| **F4** | Universal information-to-distance constant | Heteroscedastic-Gaussian counterexample (AAD-internal) | (PI) parameterization-invariance + Čencov 1982 → Fisher metric |

Three open extensions (Causal-IB; misspecification cost; tier-switching cost) plus mechanism-design impossibility (Gibbard-Satterthwaite / Myerson-Satterthwaite / Arrow) as candidate fifth instance.

The pattern is *not* a negative posture. Each floor names exactly what additional capability is required to recover identification, and the AAD machinery that supplies that capability becomes load-bearing in the strongest possible sense — without it, the no-go forbids the inference entirely. This converts AAD's "limitations" into precisely characterized scope boundaries with named escapes, and reframes scope-honesty as load-bearing architecture.

* **ASF Confidence:** **Discussion-grade** at meta-level; instances retain higher tiers.
* **Field Novelty:** **High** — methodological. The constituent moves are individually well-precedented; the unified framework as applied to an integrated agent theory has not been found in surveyed literatures.
* **Potential Importance:** **Very High** — methodologically load-bearing for the framework's distinctive contribution.

### M2. The Separability Pattern — Where AAD's Results Hold and Under What Repair

**Description:** The positive-half meta-pattern complementary to M1. Across **seven ladders of increasing difficulty**, AAD systematically distinguishes a *separable core* (where results hold cleanly), a *structured-repair zone* (where results hold under named additional structure), and a *general-open case* (where the framework declares scope honestly):

| Ladder | Separable core | Structured repair | General open |
|---|---|---|---|
| **Correlation** | L0 (independent failures) | L1 (observable common cause; facilitator-monotonicity) | L2 (deep correlation; latent without instrumentation) |
| **Convention** | C1 (one-step heuristic) | C2 (receding-horizon) | C3 (full Bellman) |
| **Architecture** | Class 1 (modular) | Class 3 (partially modular; $\kappa_{\text{processing}}$ diagnostic) | Class 2 (fully merged; bias-bound regime) |
| **Contraction** | Tier 1 (Lipschitz, scalar sector) | Tier 2 (passivity / iISS / ISS-on-restricted-domain) | Tier 3 (adversarial; equilibrium-theoretic) |
| **Identification regime** | Regime A (interventional access) | Regime B (observational + structural priors) | Regime C (purely associational) |
| **Scope hierarchy** | Adaptive (no agency) | Agency (Pearl-Level-2 contrast available) | Composite (multi-agent or coalitional) |
| **A2'-scope (metric)** | $\alpha_1$ (fixed-gain Kalman / exp-family / strongly-convex) | $\alpha_2$ (adaptive-gain under MG-1 to MG-4) | $\beta$ (PID / rule-based / variational / non-convex-beyond-basin) |

The pattern is *not* a uniform claim that AAD covers everything. It is the architectural commitment to **honestly distinguishing what does work cleanly, what works under repair, and what remains open** at each axis, with the repair zone documented at instance-level rather than handwaved.

**M1 ↔ M2 complementarity.** M1 names the *negative scope* (where structural impossibility forces identification machinery). M2 names the *positive scope* (where AAD's machinery applies cleanly under stated repair). Together they form a complete scope characterization. Each M1 instance has a positive counterpart in M2: F1's on-policy detection no-go matches the observable-sibling-covariance structured-repair on the correlation ladder; F2's unobservable-$C$ refutation matches the observable-$C$ structured-repair on the same ladder; etc. The two halves jointly mark AAD's scope at both extremes — what succeeds and under what machinery, and what structurally cannot succeed without specific information augmentation.

* **ASF Confidence:** **Discussion-grade** at meta-pattern level; instances retain higher tiers.
* **Field Novelty:** **High** — methodological. Systematic deployment of separability-pattern thinking across seven AAD-relevant intractabilities.
* **Potential Importance:** **Very High** — completes the meta-architectural triad. Without M2 visible, the catalog presents AAD as having only a negative-half (M1) and a coordinate-forcing-half (M3); the positive-half scope theory is what makes the negative-half load-bearing rather than discouraging.

### M3. Additive-Coordinate Forcing on Information-Geometric Backbone

**Description:** AAD systematically forces a coordinate at four representational layers via uniqueness theorems on AAD-internally-motivated axioms. The four layers correspond to four windows into a single underlying geometric object — the **exponential-family Legendre-Fenchel geometry on probability distributions** (Amari & Nagaoka 2000):

| Layer | AAD-internal axiom | Uniqueness mechanism | Forced coordinate | Geometric interpretation |
|---|---|---|---|---|
| **Chain** | Probability chain rule (mathematical identity) | Cauchy-FE | Log-probability | Log-coordinate of the primal point |
| **Divergence** | Chain-rule additivity over conditional factorizations | Cauchy-FE (Hobson 1969 / Csiszár 1991 / Shore-Johnson 1980) | Reverse-KL | Bregman divergence on primal potential |
| **Update** | Evidential additivity | Cauchy-FE (Aczél 1966) | Log-odds | Natural coordinate on dual space |
| **Metric** | Parameterization-invariance (PI) on singular trajectories | Čencov 1982 invariance | Fisher information metric | Hessian of dual potential |

The four are *interlocked by cross-cites* — each axiom is positioned as the layer's analog of the chain-layer's additivity. The convergence across independent axioms onto a single geometric object is the substance: **AAD's "natural coordinates" are not chosen by convention; they are forced by AAD-internal axioms via classical uniqueness theorems**, and they all live on the same exponential-family geometry. This is what backs the log-odds in #3 (detection latency), the reverse-KL in #25 (BH identity), the Fisher metric in #8 (bias bound) and #26 (LMI), and the Beta-Bernoulli structure in #7 (forgetting prerequisite).

Adjacent cases that share the *shape* but not the AAD-internal forcing: Lyapunov quadratic (Bregman divergence on Euclidean potential — different convex potential family); IB Lagrangian (adopted from Tishby-Pereira-Bialek 1999 rather than re-derived AAD-internally).

* **ASF Confidence:** **Discussion-grade** at meta-level; instances retain their tiers.
* **Field Novelty:** **High** — meta-architectural recognition.
* **Potential Importance:** **Very High** — argues AAD has a coordinate-forcing structure at every representational layer, grounding its mathematics structurally rather than aesthetically.

---

## Long-Standing Open Questions Now Within Reach

*Questions that adjacent fields have had open for years or decades that AAD's unification touches. This list is partial — each entry is a starting point, not a closure.*

- **RL convergence theory under non-stationarity.** RL's regret-bound literature mostly assumes stationarity; non-stationarity is treated case-by-case. CS1 supplies a unified story by composition of #18, #25, the strategic-tempo machinery, and #1. The framework's discovery is that *the four pieces are mutually consistent for principled reasons* (each follows from AAD-internal commitments), not that any one piece is new.
- **The dark-room problem in active inference.** Active inference under preferences-as-priors admits agents that satisfy their objective by hiding; no exploration drive in EFE is structurally sufficient to overcome it. #4 (Tragedy of the Confident Agent) sidesteps the problem at structural rather than parametric level — exploration is forced by Lyapunov persistence, not preferences.
- **Catastrophic forgetting in continual learning.** A precise feasibility-window characterization with environment-dependent threshold on both sides is in #6, with replay / EWC / consolidation mechanisms reframed as window-restoration moves.
- **Identifiability of coupling sign in multi-agent systems.** "When can I recover the cooperation/adversarial sign of inter-agent coupling from observed dynamics?" is a long-standing open question in multi-agent systems and dynamical-game theory. Identifiability-floor Instance F3 says: not from component marginals; only from interventions on sub-agents (loop-Level-2 access at composite level). The closed-form #9 supplies the matched-Tier escape.
- **Why does information theory show up everywhere in agent design?** The recurrence of log-coordinates, KL divergences, Fisher metrics, IB tradeoffs is no accident — meta-pattern M3 says they are *forced* by AAD-internal additivity / invariance axioms via classical uniqueness theorems.
- **What's the minimum bandwidth needed for an adaptive agent to track a process?** #5 gives the saturation-tight bound: $C \geq \mathcal T/2$ nats/time per dimension; Kalman-Bucy achieves it.
- **Why do confident agents need to keep exploring?** #4: not because they might learn something new (epistemic argument), but because their update gain has dropped below the rate at which reality is drifting (structural-stability argument).
- **Why does Brooks's Law hold?** #9 closed form: when coordination cost $C$ exceeds correction rate $\alpha$, the composite's effective rate $\alpha - C$ goes negative regardless of individual quality.
- **When does multi-agent system architecture cleanly compose?** #23: it depends on whether sub-agents' objectives align. Class-1 sub-agents with partially-opposing objectives produce Class-3 composites — clean composition fails by structure.
- **Why is OODA-loop tempo so consequential?** #10 + #5: tempo and opacity multiply ($\mathcal T^{\text{eff}} = \mathcal T \cdot H_b/H_b^{\max}$); persistence has an information-rate cost ($\dot R \geq n\alpha/2$) that bandwidth-constrained agents structurally fail.
- **Why do successful organizations underinvest in disruption detection?** #3: log-odds + Beta-Bernoulli structurally force detection latency to grow linearly with accumulated experience. The Innovator's Dilemma has a mechanism.
- **Why don't alignment evaluations predict deployment behavior?** #14 (Sandbox Hard Ceiling): sandbox trajectories are forkable; deployment trajectories are not. The Pearl-hierarchy-equivalence breaks. Sandbox data is Level 1; deployment behavior is a Level 2 question.
- **Why do agentic systems (loops around LLMs) outperform raw LLM calls?** #13 (Coupled Diagnostic Framework): scaffolded loops recover Section II's persistence guarantees in Class 2 architectures. The cascade-ordering happens at the loop level when the model can't produce it. Agentic system architecture is structurally non-optional, not aesthetic.
- **Why does AMSGrad outperform Adam on ill-conditioned problems?** #31 (Adaptive-Gain $\alpha_2$): AMSGrad is a meta-gain repair that restores the (MG-1) condition by construction. The empirical superiority is now derived.
- **Why does mean-field variational inference fall short of natural-gradient?** #29 (Mean-Field VI Cannot Reach Persistence-Optimal): structural $O(\sqrt\varepsilon)$ degradation, not a folklore preference.
- **Why must we sleep?** #33 (Sleep Has a Shannon Floor): consolidation cadence has an information-rate floor under (N1)+(N2). Sleep is not just metabolic; it is rate-floor-driven.
- **When can a multi-agent system be modeled as a single agent?** #9 + #23 + #30 (Sector-Persistence Template): closure-defect must be small AND macro-update must be strongly monotone AND objectives must align. Each conjunct is independently necessary.
- **Why are mass-modular AI safety architectures so fragile in practice?** #28 (Modular Safety Fails Under Goal Divergence): once safety modules and the planner have non-aligned objectives — exactly when safety modules are needed — the composite is structurally Class 3. Modular guarantees do not transfer.
- **Why do high-tempo systems hit a "communication wall"?** #5 + #39 (Bandwidth-Wall): persistence has an information-rate floor; high-$\mathcal T$ regimes saturate observation-channel capacity; sub-bandwidth-limited regimes are not adaptive equilibria.
- **Why does specification (or context-stuffing) eventually degrade rather than help?** #34 (Specification Bound = Persistence Bandwidth): the spec channel is one of the agent's bandwidth budget; specification at a rate exceeding the receiver's persistence-bandwidth-floor outpaces update.

What else is in here that nobody has noticed yet? The framework is integration plus epistemic architecture; both axes generate cross-domain implications. The Speculative S-section above (S1–S8) flags candidates the brainstorm could not fully ground but felt important enough to mark. Further passes against TST (121 segments — only ~3 read so far in the brainstorm) and logozoetic-agents (PROPRIUM ontology, AI welfare implications) are likely to surface more.

---

## Notes for Practitioners

*Engineering anchors for someone running a production agentic system (e.g., the AI Dungeon / Latitude family — Alan Walton's question: "are there useful applications to my current agentic system architecture?"). The findings are catalog entries; the practitioner question is "where does this bite?".*

**For LLM-based agents (Class 2, $\kappa \approx 1$).** #8 says hallucination bias scales as $\kappa \cdot \mathcal A$ — coupling × ambiguity. The architectural coupling is fixed (it's an LLM); the ambiguity is variable (it's the prompt and environment). Prompt engineering is *literally* $\mathcal A$-reduction. The framework predicts: (a) LLMs excel at low-$\mathcal A$ tasks (coding, structured reasoning); (b) they struggle with high-$\mathcal A$ tasks (open interpretation, ambiguous goals); (c) reducing $\mathcal A$ tightens the bound proportionally. Track 2 of the bias bound is universal under the (PI) commitment.

**For long-running agents (CS2 / #6 / #7).** The triple-pressure picture says you need joint design of forgetting rate *and* consolidation cadence *and* augmentation against detection-latency growth. Diagnose which pressure is binding: short attention span → retention; calcified responses → targeted intervention or causal-IB drive (#4); fragmented behavior → cadence engineering. Catastrophic forgetting is feasibility-window collapse, not a tunable hyperparameter.

**For multi-agent systems (#23, #9, #10).** Class-1 sub-agents with subtly divergent objectives produce Class-3 composites — clean modularity fails by structure, not by accident. Critical-mass closed form gives the persistence inequality with signed coupling $\gamma$. 16-cell adversarial-targeting decomposes "where to attack" into a precise bilinear optimization.

**For exploration design (#4, #26).** Two parallel drives at opposite ends of the uncertainty spectrum. Confident agents in drifting worlds *must* explore — directional, not scalar, with complementary slackness on direction. Empirically validated: greedy agents in volatile environments suffer catastrophic survival rates.

**For software development as an agentic domain (#12 + TST).** Software is the calibration laboratory; results derived in it transfer to other domains under explicit transfer-assumption table, not by default. Code quality *is* observation infrastructure (#17); investing in it raises future $\eta^\ast$ via lowered $U_o$. Comprehension time dominates under AI-maintained-code regime (#14).

**For the persistence condition itself.** $\alpha > \rho/R$ is a comparison of two rate constants both with units 1/time. $1/\alpha$ is the characteristic correction timescale; $R/\rho$ is the time to fill model class capacity at full disturbance rate. The persistence condition expressed in timescales: "the agent's characteristic correction time must be shorter than the time it takes disturbance to fill capacity at full rate." Practitioner-friendly intuition: the bathtub fills slower than it drains when full.

---

*This catalog is a snapshot, not a closure. The framework's integration is broad enough that adjacent fields' open questions may have unexpected answers in here, and many remain unsurfaced.*

---

## See also

- [`brainstorm-findings.md`](brainstorm-findings.md) — ongoing scratch / speculative-candidate surface. Where new candidates accumulate before promotion, and where lower-confidence catalog entries are parked when this list needs tightening. Currently holds the original Pass 1 / Pass 2 brainstorm outputs (the seed material that fed this catalog), the per-field cross-domain implication map, the speculative S-section, and the rolling promotion-and-pull log. Convention: lowercase filenames in `msc/` are scratch / working artifacts; uppercase are top-level catalog or candidate documents.
