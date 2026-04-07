---
slug: software-epistemic-properties
type: observation
status: discussion-grade
depends:
  - software-scope
  - pearl-causal-hierarchy
  - observation-function
  - adaptive-tempo
stage: draft
---

# Observation: Software's Epistemic Properties

Software development possesses six epistemic properties that collectively make it the richest operationalization domain for ACT — not merely another instantiation, but a domain where ACT's formal machinery can be tested with unusually high fidelity.

## Formal Expression

*[Observation (software-epistemic-properties)]*

Six properties distinguish software development from other adaptive domains. Each is stated with its ACT-theoretic consequence.

**P1. Environment inspectability.** The codebase state $\Omega_t$ is fully observable in principle. The partial observability in software arises from the *agent's* limited attention and comprehension bandwidth, not from the environment hiding state. Formally: the observation function $h$ is lossy because of cognitive limits on the agent side, not because $\Omega_t$ is physically inaccessible.

$$U_o^{\text{(code)}} = f(\text{agent bandwidth}) \quad \text{not} \quad f(\text{environment opacity})$$

*Consequence:* The observation uncertainty $U_o$ for code-reading channels is under the agent's (and previous agents') partial control — unlike most domains where $U_o$ is set by physics. This enables P6 below.

**P2. Executable counterfactuals (Level 3 access).** Version control provides literal counterfactual execution: `git checkout` a past state, implement an alternative decision, and run the result. This is Level 3 epistemic access ( #pearl-causal-hierarchy) with ground-truth verification — nearly unique among ACT domains.

*Consequence:* Model class fitness $\mathcal{F}(\mathcal{M})$ ( #model-class-fitness) becomes empirically measurable: fork at a past decision point, try an alternative architecture, and measure whether it achieves higher sufficiency for the actual subsequent workload.

**P3. Genuine interventions (Level 2 access).** Developers perform real interventions: running tests, deploying to staging, making speculative changes. Each is a $do(\cdot)$ operation ( #pearl-causal-hierarchy) whose outcome is observed through well-characterized channels. Software provides a spectrum of Level 2 channels with known $(\nu, U_o)$ profiles:

| Channel | $\nu$ | $U_o$ | Coverage |
|---------|--------|--------|----------|
| Type checker | Instant | Near-zero | Syntactic/type |
| Linter | Instant | Very low | Style + common errors |
| Unit tests | Seconds–minutes | Low | Tested paths |
| Integration tests | Minutes | Low–medium | Cross-module |
| Staging deploy | Minutes–hours | Medium | Near-production |
| Production canary | Hours | Low (real traffic) | Full |

*Consequence:* Causal information yield ( #causal-information-yield) is concretely estimable per channel, enabling principled sequencing: fast narrow channels first, slower broader channels when needed.

**P4. Partially explicit causal structure.** Import graphs, dependency declarations, API contracts, and type systems declare causal structure explicitly. Change propagation follows these paths. This is richer causal identification than most domains offer.

*Consequence:* The causal DAG required for strategy representation ( #strategy-dag) is partially given by the environment, not entirely inferred by the agent.

**P5. Perfect history.** Git provides a complete, immutable record of every change: what changed, when, by whom, and (partially) why. This is the chronica $\mathcal{C}_t$ ( #chronica) without information loss — the full interaction history preserved exactly.

*Consequence:* Empirical estimation of ACT quantities ($\rho$, coupling, change frequency) is possible from the historical record, without the sampling and recall biases that afflict other domains.

**P6. Agent-controlled observation quality.** Code quality IS observation channel quality. Well-written code with clear naming has low $U_o$ for the code-reading channel; obfuscated code has high $U_o$. Agents can improve their own future observation channels by writing better code — a feedback loop within the feedback loop.

*Consequence:* The agent's environment-modifying actions at time $t$ affect the observation function $h$ at time $t+k$, creating a second-order dynamic where current code quality investments compound into future adaptive capacity via $U_o \to \eta^\ast \to \mathcal{T}$. See #code-quality-as-observation-infrastructure.

## Epistemic Status

These six properties are *observations* — empirical features of the software development domain, not derived from ACT. Their ACT-theoretic consequences are *discussion-grade*: structurally motivated mappings from domain features to formal quantities, not derivations. The individual properties are independently verifiable (P1: can you read all the source? P2: can you `git checkout`? P3: can you run tests? etc.) and uncontroversial as descriptions of the domain.

The claim that these properties *collectively* make software the richest ACT testbed is comparative and harder to verify — it requires showing that no other accessible domain offers all six simultaneously. This is plausible (biological systems lack P1, P2, P5; military systems lack P1, P5; financial systems lack P4, P6) but the comparison has not been systematic.

Max attainable: *discussion-grade*. These are domain observations with theoretical interpretation, not derivable claims.

## Discussion

**The inspectability distinction (P1) is load-bearing.** Most ACT domains are POMDPs because the environment hides state. Software is a POMDP because the *agent* cannot attend to all state simultaneously. This means observation quality improvements are possible by restructuring the environment (the codebase) rather than by building better sensors. The observation function $h$ is partially a design choice, not a physical constraint. This fundamentally changes the adaptive dynamics: the agent can invest in improving $h$ itself, not just in improving $M_t$ given a fixed $h$.

**P2 limitations.** Counterfactual replay is not free. Re-implementing features under an alternative architecture costs real effort, the sequence of features may have been influenced by the architecture chosen (path dependence), and environmental coupling (team changes, market shifts) cannot be replayed. These limitations are much less severe than in other domains — a partial replay of 10 representative features provides far more information than model-based speculation — but they prevent Level 3 access from being costless or complete.

**P5 and the completeness gap.** Git records *what* changed and *when*, but only partially records *why*. Commit messages and PR descriptions encode compressed intent, but their quality varies enormously. The chronica is complete for state transitions but incomplete for the agent's reasoning. This is relevant for #causal-discovery-from-git: the interventional record is complete, but the confounder record is partial.

**Multi-agent amplification.** P5 (perfect history) combined with P6 (agent-controlled observation quality) creates a distinctive multi-agent dynamic: agents can externalize parts of $M_t$ into the environment (documentation, clear naming, architecture decisions) where future agents can observe it. This converts ephemeral model state into persistent environmental state — the agent writes its model into $\Omega$ so that future agents can reconstruct $M_t$ through observation. The quality of this externalization determines how much of the previous agent's model survives turnover, and directly affects #comprehension-time for subsequent agents.

## Working Notes

- P1 says the environment is inspectable *in principle*, but for large codebases the cost of full inspection may exceed the agent's available time. There may be a useful formalization of "effective observability" that accounts for the agent's time budget — something like $U_o^{\text{eff}} = U_o^{\text{intrinsic}} + f(\lvert\Omega\rvert / \text{budget})$. This connects to #information-bottleneck: the agent must compress because full observation is too expensive, even though it is in principle available.
- The "feedback loop within the feedback loop" (P6) is the most theoretically interesting property. It creates a self-referential dynamic where the adaptive cycle's own outputs modify its future inputs. ACT's current formulation allows action-dependent observation ($o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$), but the cumulative effect of many past actions on $h$ is a longer-timescale phenomenon. Whether this requires extending ACT or is already captured by the existing formalism (with $h$ treated as slowly varying) is an open question.
- The table in P3 invites a formal treatment: given the $(\nu, U_o)$ profile per channel and the agent's current $U_M$, what is the CIY-optimal sequencing of probes? This would be a concrete worked example for #causal-information-yield applied to software.

*(Source: old-tst-via-tft-readme.md, "What Software Development Uniquely Offers.")*
