# Reformulated TST: A Sketch

**Status**: Very early sketch. This outlines what TST might look like if rebuilt on TFT's foundations, incorporating causal structure, the feedback loop, and the unique properties of software development. This is NOT a finished reformulation — it's a structural sketch meant to be refined, challenged, and possibly discarded.

**Design principles for this reformulation:**
1. Preserve TST's practical insights (they're hard-won and valuable)
2. Ground them in TFT's formal machinery (for rigor and generality)
3. Extend with causal theory where software uniquely permits
4. Make the feedback loop explicit (TST's biggest structural gap)
5. Separate formal content from instructional/motivational framing
6. Apply TFT's epistemic status conventions throughout

---

## Part I: Foundations

### S-00: Notation, Conventions, and Epistemic Status

(Modeled on TF-00. Defines all symbols, epistemic status tags, and the dependency structure. Separates formal content from instructional guidance.)

Key notational choices:
- Use TFT notation where the mapping is exact ($\delta$, $\eta^\ast$, $T$, $\rho$, etc.)
- Introduce software-specific notation where needed (changeset, proximity, etc.)
- Epistemic tags follow TFT: Definition / Formulation / Derived / Hypothesis / Empirical Claim / Discussion

### S-01: Scope — Software Systems Under Change

*[Scope Definition]*

TST-via-TFT applies to any system where:
1. A codebase exists and evolves through intentional modification
2. One or more agents (human or AI) observe the codebase and make changes
3. External requirements change over time ($\rho \gt 0$)
4. The agents' understanding of the codebase is necessarily incomplete

This is a specialization of TFT's scope (TF-01): the agent-environment pair is (developer, codebase+requirements+runtime), observations are lossy (the developer can't hold the full codebase in mind), actions affect the environment (code changes modify the codebase), and residual uncertainty persists (the developer never fully knows how the system will behave under all conditions).

**Formal scope condition (specializing TF-01):**

$$S_{\mathrm{TST}} = \{(\text{Developer}, \text{Codebase}) \mid O \ne \emptyset, \lvert A \rvert \ge 2, H(\Omega_t \mid \mathcal C_t) \gt 0, P(\text{change-future}) \gt \varepsilon \}$$

The last condition (from TST's T-03) restricts to evolving systems — static artifacts are outside scope.

**What's different from TFT's scope**: Software has the unique properties listed in README.md (inspectable environment, executable counterfactuals, explicit causal DAGs, perfect history). These don't change the scope but enrich what's possible within it.

**What's different from TST's T-01**: TST's T-01 (temporal optimality) is absorbed into the optimization target. It remains valid as a meta-principle but is not a theorem — it's the choice of optimization objective. We make this explicit:

*[Formulation — Optimization Target]*

The objective is to minimize total expected time across all future interactions:

$$\text{minimize } E\left[\sum_i \left(t_{\text{comprehend}}(F_i) + t_{\text{implement}}(F_i)\right)\right]$$

This is a formulation choice, not a derived result. Other objectives are possible (minimize cost, maximize reliability, etc.). TST-via-TFT claims that time is the right objective for evolving software systems because (a) time is uniquely fungible (TST's T-01 argument), and (b) all other objectives either reduce to time (a defect costs time to fix) or are captured by the constraints (quality equivalence, sustainability equivalence from TST's T-01 conditions).

### S-02: Causal Structure of Software Development

*[Postulate — inheriting TF-02]*

The interaction between developer and codebase has irreducible causal structure. The temporal ordering of events is constitutive: you cannot use information from code you haven't read, and your changes have consequences you can only observe after the fact.

**Extending TF-02 for software**: The causal structure in software is richer than TF-02's general treatment because much of it is *declared*:

*[Definition — Dependency DAG]*

$$G = (V, E) \text{ where } V = \{\text{modules}\} \text{ and } E = \{(A,B) : A \text{ depends on } B\}$$

This declared causal structure constrains change propagation: a change to B may require changes to all A such that (A,B) in E.

*[Definition — Empirical Causal DAG]*

$$G' = (V, E') \text{ where } E' \text{ is inferred from historical co-change patterns, adjusted for confounders, with temporal ordering providing causal direction.}$$

$G'$ may differ from $G$ (see causal-extensions.md §1.3). The divergence $G' \setminus G$ reveals hidden coupling; the divergence $G \setminus G'$ reveals stable interfaces.

**Pearl's three levels in software (specializing TF-02's epistemic hierarchy):**

- Level 1 (Associational): "Files that historically changed together will likely change together again." Pure co-change prediction.

- Level 2 (Interventional): "If I change this module, what else needs to change?" Answerable through the DAG + tests + static analysis.

- Level 3 (Counterfactual): "What would have happened if we had chosen a different architecture?" Answerable (uniquely in software) through git fork + replay.

### S-03: The Developer's Model

*[Formulation — specializing TF-03]*

The developer maintains a model $M_t$ — a compressed representation of their understanding of the codebase, requirements, and runtime behavior:

$$M_t = \phi(\mathcal C_t)$$

where $\mathcal C_t$ is the developer's interaction history (files read, tests run, changes made, feedback received).

**Model space M varies by agent type:**

| Agent | $M_t$ contents | Model space |
|-------|-------------|-------------|
| Experienced human | Mental model of architecture + domain + conventions | Cognitive (implicit) |
| New human | Fragmentary understanding, mostly from docs/onboarding | Cognitive (sparse) |
| AI agent (fresh session) | Whatever CLAUDE.md + initial file reads provide | Context window |
| AI agent (with memory) | Context + persistent memory from past sessions | Context + external store |

**Model quality as compression efficiency (TF-03's IB objective, specialized):**

$$\phi^\ast = \arg\min_\phi \left[I(M_t; \mathcal C_t) - \beta \cdot I(M_t; \text{future-observations} \mid \text{future-actions})\right]$$

- High beta (retain detail): Appropriate for stable codebases where historical detail predicts the future well.
- Low beta (compress aggressively): Appropriate for volatile codebases where historical detail quickly becomes stale. (This is TF-03's connection to environmental volatility, directly applicable.)

---

## Part II: The Feedback Loop

This is TST's biggest structural gap. TST describes optimization of individual decisions but doesn't close the loop: predict → observe → mismatch → update → act → predict. TST-via-TFT makes the loop explicit.

### S-04: The Mismatch Signal

*[Derived — specializing TF-05]*

The developer's model generates predictions; reality provides observations. Their difference is the mismatch:

$$\delta_t = o_t - \hat o_t$$

**Software-specific mismatch taxonomy:**

| Mismatch type | Prediction | Observation | Update mechanism |
|---------------|-----------|-------------|-----------------|
| Comprehension mismatch | "I think this function does X" | "It actually does Y" | Read more carefully, trace code |
| Behavioral mismatch | "I think this change will pass tests" | "Tests fail" | Debug, fix, learn |
| Architectural mismatch | "I think this feature needs changes in A,B" | "It also needs changes in C,D,E" | Update architectural mental model |
| Requirements mismatch | "I think the user wants X" | "They actually want Y" | Clarify requirements, update model |
| Convention mismatch | "I think the pattern here is X" | "The codebase actually uses Y" | Update convention knowledge |

**Mismatch inevitability (Prop 5.1, applied):** For any developer working on a non-trivial evolving codebase, $E[\lVert\delta_t\rVert^2] \gt 0$. The developer can reduce the model-error component (by better comprehension) but cannot eliminate the observation-noise component (the codebase is inherently complex and ambiguous).

**Zero-mismatch ambiguity (TF-05, critical in software):** $\delta \approx 0$ does NOT mean the developer understands the codebase. It may mean they're only reading code they already understand (confirmation bias), or the code is so unclear that misunderstanding is invisible (high $U_o$ masking model error). This formally grounds the engineering intuition that "feeling comfortable with the code" is not the same as understanding it.

### S-05: The Update Gain

*[Empirical Claim — specializing TF-06]*

The developer should weight new information by the uncertainty ratio:

$$\eta^\ast = \frac{U_M}{U_M + U_o}$$

**Gain by observation channel** (true aisthesis — signals arriving from $\Omega$):

| Observation channel | $U_o$ | Typical $\eta^\ast$ | Notes |
|---------------------|-----|-------------|-------|
| Compiler/type-checker output | Near-zero | ~1.0 | Always trust — deterministic |
| Failing test | Low | ~1.0 | Strong signal; low noise |
| Passing test suite | Low | 0.7-0.9 | Absence of evidence ≠ evidence of absence; coverage matters |
| CI pipeline results | Low | 0.7-0.9 | Integration-level signal |
| Runtime telemetry | Medium | 0.5-0.7 | Sampling noise, aggregation artifacts |
| Monitoring alerts | Low-medium | 0.6-0.8 | Depends on alert quality; can have false positives |
| Code review feedback | Medium-high | 0.4-0.7 | Subjective; reviewer's own $U_M$ matters (Appendix F's $U_{\text{src}}$) |
| Bug reports | High | 0.3-0.5 | User-reported; ambiguous, may conflate symptoms |
| Analytics/user data | High | 0.3-0.5 | Heavily aggregated; interpretation required |

**Gain by exploration action result** (signal returned from a directed attention choice — the observation is $o_t$, but the agent chose which part of $\Omega$ to look at):

| Exploration result | $U_o$ factor | Notes |
|--------------------|-----------|-------|
| Content of clear, well-named code | Low | Low $U_o$ → accurate model update |
| Content of unclear/obfuscated code | High | High $U_o$ → unreliable model update; the developer may *think* they understood but didn't |
| Content of a query to a reliable expert | Low-medium | Pre-compressed model; high CIY per unit time (TF-08) |
| Content of outdated documentation | Very high | The observation itself is unreliable — the channel has degraded |
| Git blame / commit messages | Medium | Depends on quality of messages; often terse |

The distinction: *observation channels* have inherent $U_o$ determined by the channel physics (compiler determinism, test coverage, sampling rates). *Exploration results* have $U_o$ determined by the *quality of the part of $\Omega$ being explored* — which is itself shaped by past actions (the code-quality feedback loop from mapping.md).

[Plausible] These numbers are illustrative, not measured. The structural point is that $\eta^\ast$ should vary by both channel type and by the developer's current $U_M$. A new developer (high $U_M$) should have high $\eta^\ast$ — absorb everything, question nothing. An experienced developer (low $U_M$) should be skeptical of surprising observations from high-noise sources, while still trusting deterministic channels fully.

**Gain reset after structural change**: When the codebase undergoes a major refactoring or architectural change, experienced developers' $U_M$ should spike — their old model is unreliable. If they don't reset their gain (continue trusting their stale model), they will make errors based on outdated understanding. This is the TF-06 "incestuous amplification" failure mode applied to software: the experienced developer who "knows the system" but whose knowledge is no longer current.

### S-06: Action Selection and the Feedback Loop Closure

*[Derived — specializing TF-07]*

The developer's actions are functions of their model:

$$a_t = \pi(M_t)$$

Actions include: which file to read next, what code to write, what test to run, whom to ask, whether to refactor.

**The explore/exploit tension (TF-08, specialized):**

$$\pi^\ast(M_t) = \arg\max_a \left[E[\text{value}(a) \mid M_t] + \lambda(M_t) \cdot \text{CIY}(a; M_t)\right]$$

- **Exploit**: Write code based on current understanding. Ship features.
- **Explore**: Read unfamiliar code, write tests for untested paths, ask questions about unclear areas, prototype alternative approaches.

**When to explore**: $\lambda$ should be high when:
- $U_M$ is high (the developer doesn't understand the codebase well)
- The upcoming work is in an unfamiliar area
- Past actions have produced surprising mismatch (there's a model error to find)
- The codebase has changed significantly since last interaction ($\rho$ has been high)

**When to exploit**: $\lambda$ should be low when:
- $U_M$ is low (the developer has a good model)
- The work is routine and in familiar territory
- Time pressure is high ($\rho_{\text{deliberation}}$ is high — TF-09)

**Query actions (TF-08, highly relevant):** Asking a colleague or reading documentation is a query action with potentially enormous CIY. The barometer insight applies: don't reconstruct the architecture from source when you can ask someone who already knows. For AI agents, this means: read CLAUDE.md and architecture docs before diving into source code.

---

## Part III: Temporal Dynamics

### S-07: Adaptive Tempo for Software Development

*[Definition + Hypothesis — specializing TF-11]*

The developer's adaptive tempo:

$$T = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$$

is the effective rate at which they reduce their mismatch with the codebase.

**The mismatch dynamics (hypothesis, as in TF-11):**

$$\frac{d\lVert\delta\rVert}{dt} = -T \cdot \lVert\delta\rVert + \rho(t)$$

where $\rho(t)$ is the rate at which new mismatch is introduced by: requirement changes, other developers' commits, dependency updates, and the developer's own imperfect changes (the self-adversarial feedback loop from mapping.md).

**The persistence condition:**

$$T_{\text{team}} \gt \frac{\rho_{\text{total}}}{\lVert\delta_{\text{critical}}\rVert}$$

The team's aggregate adaptive tempo must exceed the total rate of change (normalized by the tolerable mismatch level). Below this threshold, the codebase becomes unmaintainable — the team's model degrades faster than they can maintain it.

### S-08: The Investment Calculus

*[Derived — reformulating TST's T-06 on TFT foundations]*

TST's change investment theorem (T-06) becomes a consequence of the persistence condition. An action that increases $T$ (by reducing future $U_o$, or by improving architectural coherence so that future change-sets are smaller) is justified when the persistence benefit exceeds the immediate time cost.

*[Derived (from TFT's persistence condition)]*

Choose the code change C that maximizes the integral of future tempo improvement:

$$\text{benefit}(C) = \int_0^{T_{\text{horizon}}} \left[T_{\text{team}}(t \mid C) - T_{\text{team}}(t \mid C')\right] dt$$

where C' is the "quick" alternative. Choose C over C' when benefit(C) > cost(C) - cost(C').

This is more precise than TST's "X < n_future * Y" because it integrates over the tempo trajectory rather than summing discrete future events. The integral form captures compounding effects that the discrete sum misses.

**Connection to TST's original formulation**: In the simple case where each future feature has the same impact and the tempo improvement is constant, this reduces to TST's T-06: invest when immediate cost < n_future * per-feature savings.

### S-09: Structural Adaptation for Architectures

*[Derived — reformulating TST's T-07 and refactoring decisions on TF-10]*

**Model sufficiency for architectures:**

$$S(\text{Architecture}) = 1 - \frac{\text{predictive information lost by the architecture}}{\text{total predictive information in the change history}}$$

An architecture has high sufficiency when it captures the change patterns — when related changes are co-located (high coherence) and unrelated changes are decoupled (low coupling). This IS TST's T-10, grounded in TF-10's sufficiency measure.

**Model class fitness:**

$$F(\text{ArchitectureClass}) = \sup_{A \in \text{ArchitectureClass}} S(A)$$

When F < 1 - epsilon (the best architecture within the current paradigm still can't accommodate the change patterns), no amount of incremental refactoring helps. The paradigm must change: monolith → microservices, or MVC → event-driven, or relational → document store. This is TST's refactoring decision grounded in TF-10's Proposition 10.1.

**Symptoms (from TF-10, in software language):**
1. Persistent large change-sets despite experienced team → model class inadequacy
2. Developers confident but still slow → gain collapse without performance
3. The same kinds of features always cause the same kinds of cross-cutting changes → systematic mismatch patterns

### S-10: Deliberation Cost and the Comprehension/Action Tradeoff

*[Derived — reformulating TST's T-05 on TF-09]*

Deliberation (reading code, planning, analyzing) costs time during which the environment changes:

$$\delta_{\text{mismatch-during-deliberation}} = \rho_{\text{delib}} \cdot \delta\tau$$

Deliberation is justified when:

$$\delta\eta^\ast(\delta\tau) \cdot \lVert\delta_{\text{post}}\rVert \gt \rho_{\text{delib}} \cdot \delta\tau$$

**The AI agent's dilemma**: An AI agent with 100% context turnover faces a severe version of this tradeoff. It MUST deliberate (comprehend the codebase) before it can act effectively. But during comprehension, its context window fills, requirements may change, and other agents may modify the codebase. The optimal comprehension depth depends on $\rho$ and the session's action horizon.

TST's T-05 ("bias toward comprehension" in high-turnover settings) is the practical prescription. TFT provides the formal justification: when $U_M$ is very high (as it is at session start), the deliberation benefit (large $\delta\eta^\ast$) is worth the deliberation cost ($\rho \cdot \delta\tau$), up to the point of diminishing returns.

---

## Part IV: Software-Specific Extensions

### S-11: The Causal DAG and Change Propagation

*[Extension — beyond TFT's current scope]*

The codebase dependency DAG provides explicit causal structure for change propagation analysis (see causal-extensions.md). Key results:

- Change-set size for feature F ≈ |downstream(intervention(F), DAG)| (TST's T-08 grounded in causal graph theory)

- Architecture optimization ≈ DAG optimization: minimize expected downstream set size for the distribution of anticipated features

- Coupling (TST's D-06) ≈ P(change(B) | do(change(A))), estimable from the DAG with adjustment for confounders

### S-12: Counterfactual Evaluation via Git

*[Extension — uniquely available in software]*

Level 3 counterfactual reasoning is available through git fork + replay:

1. Retrospective evaluation: fork from past decision point, implement the alternative, measure the difference.

2. Prospective evaluation: implement small proofs-of-concept in alternative architectures, project forward using the causal DAG.

3. Calibration: use counterfactual data to update the parameters in the investment calculus (S-08) and structural adaptation trigger (S-09).

### S-13: Multi-Agent Software Development

*[Extension — specializing Appendix F]*

The trust meta-model (F.2) applies directly to software teams:

$$\eta_{ji}^\ast = \frac{U_M^i}{U_M^i + U_o^{ji} + U_{\text{src}}^j + U_{\text{align}}^{ji}}$$

- $U_o^{ji}$: communication channel quality (clear code comments → low; ambiguous PR descriptions → high)
- $U_{\text{src}}^j$: source quality (Alice writes reliable code → low; legacy module with no tests → high)
- $U_{\text{align}}^{ji}$: alignment (teammate with shared goals → low; external contributor with unknown motives → medium; potentially adversarial PR → high)

**Team persistence** (from F.3):

$$T_{\text{team}} = \sum_i T_i + \sum_{i,j} \nu_{ij}^{\text{comm}} \cdot \eta_{ij}^\ast$$

Teams persist in environments where individuals cannot, because cooperative communication tempo offsets disturbance that exceeds individual capacity.

### S-14: Runtime Systems and Operational Dynamics

*[Extension — reformulating TST's T-12 on TFT foundations]*

The running system is a separate TFT agent-environment coupling:

- Agent: The operations team / monitoring system / automated remediation
- Environment: The running system + its infrastructure + user load
- Model: Expected runtime behavior (latency targets, error rates, resource usage)
- Mismatch: Anomaly detection (observed behavior - expected behavior)
- Tempo: Monitoring frequency * detection accuracy

**Deployment as intervention**: do(deploy(new_code)) → observe(production_behavior)

**The persistence condition for operations**:

$$T_{\text{ops}} \gt \frac{\rho_{\text{incidents}}}{\lVert\delta_{\text{critical-sla}}\rVert}$$

Below this threshold: outages accumulate faster than the team can resolve them.

TST's T-12 insight — that system availability = MTTF/(MTTF+MTTR) — becomes a consequence of the persistence condition: MTTR is inversely proportional to T_ops, and MTTF is inversely proportional to rho. The "let it crash" philosophy optimizes by raising T_ops (fast recovery) rather than lowering rho (preventing failures).

---

## Part V: What's Changed from Original TST

### What's preserved

All of TST's practical insights survive — they're reframed, not discarded:

| Original TST | TST-via-TFT | What changed |
|-------------|-------------|-------------|
| T-01 (Temporal optimality) | S-01 formulation choice | Demoted from "first principle" to explicit optimization target |
| T-02 (Specification bound) | Absorbed into S-01's scope | The insight about specification time remains; TFT adds the information-theoretic framing |
| T-03 (Evolving systems scope) | S-01 scope condition | Nearly unchanged; the $P(\text{change}) \gt \varepsilon$ condition persists |
| T-04 (Change expectation baseline) | Absorbed into S-07's rho estimation | The Bayesian baseline becomes the prior for rho estimation |
| T-05 (Dual optimization) | S-10 (deliberation cost) | Comprehension vs. implementation becomes deliberation vs. action, with formal tradeoff |
| T-06 (Change investment) | S-08 (investment calculus) | The "X < n_future * Y" rule is derived from the persistence condition with integral form |
| T-07 (Conceptual alignment) | S-09 (structural adaptation) | Domain alignment becomes architectural sufficiency |
| T-08 (Change-set size) | S-11 (causal DAG) | Proportionality claim grounded in causal graph structure |
| T-09 (Change proximity) | S-11 (downstream set size) | Proximity becomes graph distance in the causal DAG |
| T-10 (Coherence-coupling) | S-09 + S-11 | Measured through the causal DAG rather than correlation |
| T-11 (Decision integration) | Natural consequence of S-08 | The integration framework falls out of the tempo optimization |
| T-12 (Continuous operation) | S-14 (runtime dynamics) | Grounded in TFT's persistence condition |

### What's new

1. **The feedback loop is explicit.** TST described individual decisions; TST-via-TFT describes the full predict → observe → mismatch → update → act cycle.

2. **The gain framework.** TST treated all information equally. TST-via-TFT weights information by the uncertainty ratio, giving formal guidance on when to trust observations vs. prior model.

3. **Causal structure.** TST used correlation (co-change) as a proxy for coupling.
   TST-via-TFT uses causal analysis.

4. **Counterfactual evaluation.** TST could only argue qualitatively about architectural decisions. TST-via-TFT can (in principle) measure counterfactually.

5. **Multi-agent dynamics.** TST had no treatment of teams, trust, or adversarial modification. TST-via-TFT inherits Appendix F's full framework.

6. **The persistence condition.** TST's "vicious cycle" becomes quantitative: a measurable threshold below which codebases degrade.

7. **Epistemic rigor.** Every claim has an explicit status (Definition / Derived / Hypothesis / Empirical / Discussion) and a dependency chain.

### What's removed

1. **Motivational framing.** "Feel the mathematics" and "mathematical recognition moments" are instructional, not theoretical. They belong in system prompts or onboarding materials, not in the theory itself.

2. **T-01 as a theorem.** The temporal optimality principle is real but tautological.
   It becomes a formulation choice (S-01) rather than a first principle.

3. **Ungrounded proportionality claims.** T-08's "time ∝ changeset size" and T-09's proximity claims are reframed as consequences of the causal DAG structure rather than standalone empirical claims.

---

## Open Questions (many — this is a sketch, not a theory)

1. Can the TFT quantities ($\eta^\ast$, $T$, $\rho$, $\alpha$, $R$) be measured from real software development data? This is the operationalization question. Appendix B provides general recipes; the software domain needs specific procedures.

2. Is the linear mismatch ODE a useful approximation for software development dynamics, or is the nonlinear case (saturation, thresholds, structural breakdown) essential? Simulation 1 would address this.

3. How should the dependency DAG and the empirical causal DAG be reconciled when they disagree? Which one should drive architecture decisions?

4. The "observation channel quality is under the agent's control" second-order feedback loop: can TFT be extended to handle this, or does it require new formalism?

5. The 100% turnover problem: is there a formal "cold-start protocol" derivable from TFT that tells an AI agent how to optimally allocate its first N tokens between reading code (observation), reading docs (query action), and starting to code (exploitation)?

6. How much of this reformulation is genuinely useful vs. formally impressive but practically equivalent to "write clean code, refactor when needed, communicate well"? The test is: does the formal machinery generate non-obvious predictions that the informal wisdom misses?
