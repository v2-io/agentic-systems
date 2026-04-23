---
slug: observation-ambiguity-modulation
type: scope
status: conditional
depends:
  - scope-logogenic-agent
  - coupled-update-dynamics
  - directed-separation
  - section-ii-survival
  - mismatch-signal
stage: draft
---

# Scope: Observation Ambiguity Modulation

The approximation error of Section II results for Class 2 agents depends on the product $\kappa_{\text{processing}} \times \mathcal{A}(e_\tau)$, not on $\kappa_{\text{processing}}$ alone. Observation ambiguity $\mathcal{A}(e_\tau)$ is an *observation-stream property*: it measures, at the Bayesian-optimal level, how much the residual world-state uncertainty left by the observation is goal-resolvable — i.e., how much the observation's interpretation depends on goal context, independently of any agent's processing architecture. Binary, verifiable observations (test pass/fail, deployment success, measurable metrics) have low ambiguity — they pin down the world-state sharply, leaving little goal-conditional residual — and limit the damage from goal-conditioned processing. Interpretive observations (code quality assessments, strategic evaluations, user intent) have high ambiguity and are where directed-separation violations have maximal impact.

## Formal Expression

*[Definition (observation-ambiguity)]*

The **observation ambiguity** of event $e_\tau$ is a property of the observation-world joint distribution given the agent's prior model $M_{\tau^-}$ and a reference goal prior $P_{\text{ref}}(G)$:

$$\mathcal{A}(e_\tau) = \frac{I(G \,;\, \Omega_\tau \mid e_\tau,\, M_{\tau^-})}{H(\Omega_\tau \mid e_\tau,\, M_{\tau^-})}$$

The numerator is the mutual information (computed under $P_{\text{ref}}(G)$ and the Bayesian-optimal posterior $P(\Omega_\tau \mid e_\tau, M_{\tau^-}, G)$) between goal-context and world-state *after conditioning on the observation*: residual goal-relevant uncertainty not resolved by the observation itself. The denominator normalizes by total residual world-state uncertainty after the observation. The ratio is the fraction of the observation's residual ambiguity that is goal-resolvable.

Both quantities are defined at the Bayesian-optimal level — no reference to any agent architecture, processor, or $\kappa$ value appears in the definition. $\mathcal{A}(e_\tau)$ is a property of the observation channel, the world's generative model, the prior $M_{\tau^-}$, and the reference goal distribution $P_{\text{ref}}(G)$. The reference goal prior is a specification detail (analogous to the reference convention in #value-object) — it parameterizes the definition without tying it to the processing architecture of any particular agent.

- $\mathcal{A}(e_\tau) \approx 0$ in two regimes: (i) the observation resolves the world-state sharply ($H(\Omega_\tau \mid e_\tau) \to 0$, so both numerator and denominator shrink and, generically, the numerator shrinks at least as fast) — *factually unambiguous* observations like a test passing or failing, a compiler error with a specific message, a file's existence; (ii) the residual uncertainty is goal-neutral ($I(G;\Omega \mid e_\tau) \to 0$) — the goal tells you nothing about the world that the observation didn't already determine. Both regimes correspond to the informal notion "the observation's meaning does not depend on goals."
- $\mathcal{A}(e_\tau) \approx 1$: the observation underdetermines the world, and the residual uncertainty is substantially goal-resolvable. Different plausible goals map the same observation to systematically different world-states. Examples: a code review comment could be interpreted as "minor style issue" or "critical design flaw" depending on whether the relevant goal is "ship fast" or "ensure correctness"; "the user seemed frustrated" interpreted differently depending on whether the goal is "get the task done" or "build a long-term relationship."

*[Scope Condition (ambiguity-modulation)]*

The epistemic bias introduced by a Class 2 agent's coupled update is a product of two independent quantities: $\kappa_{\text{processing}}$ (an *architectural* property from #directed-separation — how much the agent's processing couples goals and beliefs) and $\mathcal{A}(e_\tau)$ (an *observational* property defined above — how much the observation's residual uncertainty is goal-resolvable). Neither alone produces bias: a fully-merged processor operating on unambiguous observations ($\mathcal{A} = 0$) has no bias because the observation leaves nothing for goal-coupling to exploit; a modular processor ($\kappa = 0$) operating on ambiguous observations has no bias because the processing does not channel goal information into belief updates.

Define the **effective coupling for event $e_\tau$**:

$$\kappa_{\text{eff}}(e_\tau) = \kappa_{\text{processing}} \cdot \mathcal{A}(e_\tau)$$

This is the quantity that governs the approximation error for the five approximately-surviving Section II results ( #section-ii-survival). The epistemic bias satisfies:

$$\lVert\Delta M_{\text{bias}}\rVert \leq C \cdot \kappa_{\text{eff}}(e_\tau) \cdot H(\Omega_\tau \mid e_\tau, M_{\tau^-})  = C \cdot \kappa_{\text{processing}} \cdot I(G;\, \Omega_\tau \mid e_\tau, M_{\tau^-})$$

The constant $C$ was previously treated as "domain-dependent" and the bound as order-of-magnitude guidance. **Since 2026-04-24, $C$ is derived under two named sub-scopes** (see [#bias-bound-derivation](../../01-aad-core/src/bias-bound-derivation.md)): Track 1 gives $C_{W_2}^2 = 2 L_{\text{post}}^2/\rho_{\text{LSI}}$ linear in $I$ under log-Sobolev + Lipschitz-posterior regularity (H1-H3); Track 2 gives universal dimension-free $C_{FR} = \sqrt{2}$ under (PI) + Čencov + small-information regime (H1+H4). A no-go result in the appendix shows universal $C$ under Euclidean-parameter norm cannot exist — justifying the (PI) parameterization-invariance axiom in [#agent-identity](../../01-aad-core/src/agent-identity.md) as load-bearing for this bound rather than coincidental. The bound's epistemic tier upgrades from "order-of-magnitude guidance" to *conditional theorem (exact under H1-H3 or H1+H4)*.

The two forms are algebraically equivalent — $\mathcal{A} \cdot H(\Omega\mid e, M) = I(G;\Omega\mid e, M)$ by the definition of $\mathcal{A}$ — and expose the bound's semantic content: bias is upper-bounded by architectural coupling times the residual goal-world mutual information left over after the observation. This is a strict refinement of the coarser bound $\lVert\Delta M_{\text{bias}}\rVert \leq C \cdot \kappa \cdot H(G\mid e, M)$ in #section-ii-survival, since $I(G;\Omega\mid e, M) \leq H(G\mid e, M)$: when the goal-resolvable portion of the observation's residual is small, bias is correspondingly tighter. The product form is the simplest composition consistent with the boundary conditions ($\mathcal{A} = 0 \Rightarrow$ no bias; $\kappa = 0 \Rightarrow$ no bias); see Epistemic Status for what the product does and does not establish.

**Consequence for the survival classification.** A Class 2 agent ($\kappa_{\text{processing}} \approx 1$) operating in a domain with low observation ambiguity ($\mathcal{A}(e_\tau) \ll 1$ for most events) has:

$$\kappa_{\text{eff}} \approx \mathcal{A}(e_\tau) \ll 1$$

In such domains, the Section II results classified as "approximately surviving" become *good approximations* despite the agent being fully merged. The directed-separation violation is real but inconsequential because the observations, as generative objects, carry minimal interpretive latitude.

*[Scope Condition (domain-classification)]*

Domains can be classified by their typical observation ambiguity, which determines how much of Section II's machinery is directly applicable to Class 2 agents operating in that domain:

| Domain class | Typical $\mathcal{A}$ | Section II applicability | Examples |
|---|---|---|---|
| **Low ambiguity** | $\mathcal{A} \ll 1$ | Section II approximately exact even for Class 2 | Software with comprehensive tests, manufacturing with precise sensors, formal verification |
| **Mixed ambiguity** | $\mathcal{A}$ varies by observation type | Section II reliable for verifiable observations, degraded for interpretive ones | Software development (tests are low-$\mathcal{A}$, code reviews are high-$\mathcal{A}$), clinical medicine (lab results vs. symptom interpretation) |
| **High ambiguity** | $\mathcal{A} \approx 1$ | Section II results significantly degraded for Class 2 | Organizational strategy, intelligence analysis, creative evaluation, philosophical reasoning |

### Operationalization

*[Definition (ambiguity-operationalization)]*

Estimating $\mathcal{A}(e_\tau)$ requires probing how the interpretation of $e_\tau$ depends on goal context, *not* how a specific agent's processing responds. A high-capacity reference interpreter (LLM oracle, ensemble of human annotators, or any inference engine approximating Bayesian-optimal posteriors) is used as a **measurement instrument**, not as the subject of measurement. Present the same observation to the reference interpreter under multiple goal-primings $G_1, \ldots, G_K \sim P_{\text{ref}}(G)$, and measure the divergence of the world-state interpretations:

$$\hat{\mathcal{A}}(e_\tau) = \frac{\mathrm{Var}_{k}\big[\, \hat\Omega_{\tau}^{(G_k)}(e_\tau)\,\big]}{\mathrm{Var}_{k}\big[\, \hat\Omega_{\tau}^{(G_k)}(e_\tau)\,\big] + \mathbb{E}_k\big[\,\mathrm{Var}\big(\hat\Omega_\tau \mid e_\tau, G_k\big)\,\big]}$$

where $\hat\Omega_\tau^{(G_k)}(e_\tau)$ is the reference interpreter's posterior-mean world-state estimate for observation $e_\tau$ under goal-priming $G_k$. The numerator is the between-goal variance of interpretations (goal-resolvable uncertainty); the denominator adds the within-goal residual variance (total residual uncertainty). This is the empirical analog of the information-theoretic ratio in the definition.

A critical distinction from a processor-bound estimator: the reference interpreter's own $\kappa_{\text{processing}}$ does not enter $\hat{\mathcal{A}}$ as a confound, because the between-goal variance directly measures goal-resolvable uncertainty about the *world*, not about the interpreter's belief-update dynamics. An LLM with $\kappa \approx 1$ used as the reference interpreter will correctly report low $\hat{\mathcal{A}}$ for "test failed" (all goal-primings yield the same factual interpretation) and high $\hat{\mathcal{A}}$ for "the code is messy" (goal-primings yield systematically different factual readings of *what the world is*). The measurement remains robust because a reference interpreter with high capacity approximates the Bayesian-optimal posterior up to a goal-neutral baseline, and the ratio structure cancels architecture-dependent baselines.

**Caveat.** A processor with $\kappa = 0$ — a truly modular reference interpreter that cannot use goal information at all — would produce no between-goal variance and would under-estimate $\hat{\mathcal{A}}$ for genuinely goal-resolvable observations. The estimator requires the reference interpreter to have $\kappa_{\text{processing}} \gt 0$ and sufficient capacity to use goal information when it is genuinely informative. For current-generation LLMs operating on ambiguous natural-language observations, this condition holds comfortably.

**Separately, $\kappa_{\text{processing}}$ for a specific agent** ( #directed-separation) is still measurable by the original processor-probing procedure — present the same observation to the *agent under test* with different goal states and measure the divergence of its epistemic component. That quantity genuinely is a processor property and belongs in #directed-separation; the conflation with $\mathcal{A}$ was the earlier-formulation bug Finding B identified.

## Epistemic Status

*Conditional.* Two distinct claims, at different epistemic levels:

**The definition of $\mathcal{A}(e_\tau)$** — as a conditional-mutual-information ratio at the Bayesian-optimal level — is *robust qualitative*. It is a well-defined property of the observation-world joint distribution given a specified reference goal prior, with no dependence on any agent's processing. Its two boundary regimes (factually sharp observations, goal-neutral residual uncertainty) correspond to the informal intended reading ("observation meaning is not goal-dependent"). The dependence on $P_{\text{ref}}(G)$ is a specification choice — different reference goal distributions yield different ambiguity values, analogous to the convention choice for $V_O$ in #value-object. Within a fixed $P_{\text{ref}}(G)$, the quantity is exact. This is a strictly stronger status than the prior formulation, which conditioned on hypothetical $\kappa=0, \kappa=1$ processors and conflated observation properties with architecture properties.

**The scope condition $\kappa_{\text{eff}} = \kappa \cdot \mathcal{A}$** is *conditional*. The multiplicative composition is the simplest form consistent with the two boundary conditions ($\mathcal{A} = 0 \Rightarrow$ no bias; $\kappa = 0 \Rightarrow$ no bias) and is structurally motivated by the survival analysis (`msc/spike-coupled-survival-analysis.md`), but it is not derived from a specific coupled-update model. The actual composition could be nonlinear ($\kappa^a \cdot \mathcal{A}^b$ with $a, b \neq 1$), or involve threshold effects, or depend on features of the observation beyond $\mathcal{A}$ alone.

**The bias bound** upgrades from "order-of-magnitude guidance" to *conditional theorem* with the [#bias-bound-derivation](../../01-aad-core/src/bias-bound-derivation.md) appendix (2026-04-24). Track 1 is exact under (H1) statistical-manifold sub-case + (H2) log-Sobolev on observation distribution + (H3) Lipschitz-posterior stability (Stuart 2010) — linear in $I$ with $C_{W_2}^2 = 2L_{\text{post}}^2/\rho_{\text{LSI}}$. Track 2 is exact under (H1) + (H4) small-information regime with (PI)+Čencov — $\sqrt{I}$ scaling with universal $C_{FR} = \sqrt{2}$. Outside these sub-scopes (e.g., heavy-tailed observations violating LSI, ill-posed inverse problems violating Lipschitz-posterior, large-$I$ regime beyond the Fisher-metric small-$I$ expansion), the bound degrades to Pinsker's $O(\sqrt\varepsilon)$ baseline or fails with explicit scope-exit statements.

The domain classification (low/mixed/high ambiguity) is robust-qualitative — the examples are well-motivated and the categories are useful for engineering guidance. The operational estimator $\hat{\mathcal{A}}$ is a measurement proposal conditional on the reference interpreter's capacity assumption (stated in §Operationalization), not a validated instrument.

Max attainable: the multiplicative composition could be derived from the information geometry of the coupled update, relating $\mathcal{A}(e_\tau)$ and $\kappa_{\text{processing}}$ to the Fisher-information decomposition of the likelihood $P(o \mid M, G)$. A specific model of how goal-conditioning enters the likelihood function (e.g., attention-weighted Bayesian inference) would close this gap — feasible in principle but not attempted here. **The constant $C$ half of this gap is closed** by the 2026-04-24 [#bias-bound-derivation](../../01-aad-core/src/bias-bound-derivation.md) appendix; the multiplicative $\kappa \cdot \mathcal{A}$ decomposition half remains open pending a specific coupled-update model.

## Discussion

**Why ambiguity matters more than coupling.** For LLM-based agents, $\kappa_{\text{processing}} \approx 1$ is architectural — it cannot be reduced without changing the architecture (e.g., from a single LLM to a modular system). But $\mathcal{A}(e_\tau)$ is a property of the *domain and observation design*, which is under the system designer's control. The practical lever for making Section II results applicable to LLM agents is not reducing $\kappa$ (which requires architectural changes) but reducing $\mathcal{A}$ (which requires better observation design): more tests, more precise metrics, more structured outputs, less reliance on interpretive judgments.

**The software domain advantage.** Software development is a mixed-ambiguity domain with an unusually high proportion of low-ambiguity observations: tests pass or fail, linters report specific violations, type checkers give precise errors, deployments succeed or fail, metrics are numerical. This makes software a favorable domain for applying AAD's Section II machinery to LLM agents — the goal-conditioning effects are limited to the interpretive observations (code review, architectural assessment, requirement interpretation). The low-ambiguity observations anchor the agent's epistemic state in goal-independent reality, limiting the damage from goal-conditioned interpretation of the ambiguous observations.

**Goal-conditioned ambiguity as motivated reasoning.** High $\mathcal{A}(e_\tau)$ with high $\kappa_{\text{processing}}$ is the formal characterization of motivated reasoning: the agent's goals shape how it interprets evidence. An LLM agent reading code with goal "ship the feature today" may downweight evidence of bugs that would delay shipping. The $\kappa \times \mathcal{A}$ framework quantifies this: the motivated reasoning is maximal when the observation is ambiguous ($\mathcal{A} \approx 1$) and the processing is fully merged ($\kappa \approx 1$). It vanishes when the observation is unambiguous ($\mathcal{A} \approx 0$) — a test failure is a test failure regardless of the agent's shipping deadline.

**Relationship to Section I quantities.** The mismatch signal $\delta_t$ ( #mismatch-signal) is defined on observable prediction error. For low-ambiguity observations, $\delta_t$ is goal-independent (the prediction error is what it is). For high-ambiguity observations, the *prediction* itself may be goal-conditioned (the agent's expectation about what it will observe depends on what it hopes to observe), introducing bias into $\delta_t$. This means that even Section I quantities, while formally well-defined regardless of coupling, can be *effectively biased* by goal-conditioning in high-ambiguity domains. The ambiguity modulation applies not just to Section II's survival but to the practical accuracy of Section I's quantities in coupled architectures.

## Working Notes

- **Resolved (2026-04-22): architecture-contamination in the ambiguity definition.** The prior formulation defined $\mathcal{A}(e_\tau)$ via posterior beliefs $M_{\tau^+}$ conditioned on hypothetical $\kappa = 1$ and $\kappa = 0$ processors — an architecture probe embedded in what should have been an observation-stream property. Per `msc/pending-findings-2026-04-21.md` Finding B: recast as the conditional-mutual-information ratio $I(G;\Omega \mid e, M)/H(\Omega \mid e, M)$ under a reference goal prior. Both quantities are Bayesian-optimal with no reference to any processor; the architectural $\kappa$ enters explicitly (and only) through composition with $\mathcal{A}$ in the downstream scope condition. This is also the information-geometric direction flagged by the prior Working Note (Fisher-information form) and by `msc/spike-coupled-survival-analysis.md` line 596. Downstream consumers (`section-ii-survival` line 75, `coupled-diagnostic-framework` line 87) use the product form $\kappa \cdot \mathcal{A}$ and are unaffected by this reformulation.
- The Fisher-information form $\mathcal A(e) \propto \mathrm{tr}(\mathcal I_G(e)) / \mathrm{tr}(\mathcal I_M(e))$ is a local (small-perturbation) analog of the MI ratio now adopted. For a smooth likelihood $P(o \mid M, G)$, the two agree to leading order around any reference point; they diverge on observations with high-curvature or long-tail posterior structure. The MI ratio handles long-tail cases correctly (the MI sees the full distribution; Fisher trace sees only local curvature), which is why it is the primary form.
- The domain classification (low/mixed/high) is coarse. A finer classification would characterize the *distribution* of $\mathcal{A}$ across the observation stream: what fraction of events are low-ambiguity, what fraction are high-ambiguity, and how the agent's strategy depends on each type. In a software domain, the high-ambiguity observations (code review, architecture decisions) are often the most *strategically important* ones, creating a worst-case correlation between ambiguity and strategic significance.
- The $\kappa_{\text{processing}}$ operationalization (presenting the same observation to the *agent under test* with different goal states and measuring divergence of its epistemic component) now lives canonically in #directed-separation, not here. This segment keeps only the $\hat{\mathcal{A}}$ estimator, which uses a reference interpreter as a measurement instrument (not as the subject of measurement). The reference interpreter and the agent under test can be the same model, but they are being asked different questions: "what does this observation mean under these goal primings?" (measuring $\mathcal{A}$) versus "how does this agent's belief update depend on the goal in its context?" (measuring $\kappa$).
- The reference goal prior $P_{\text{ref}}(G)$ is a specification degree of freedom. Different choices yield different ambiguity values. For engineering, sensible choices include: (a) a uniform prior over a task-relevant goal taxonomy (for generic application), (b) the agent's actual deployed-goal distribution (for calibrated diagnostics), or (c) an adversarial prior concentrated on goals that maximize interpretive divergence (for worst-case analysis). None is canonical; the theory makes the choice explicit rather than hiding it in an architectural probe.
